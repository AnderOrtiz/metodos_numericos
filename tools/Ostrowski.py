import math
import numpy as np


def Ostrowski(f,df,x0,tol,maxiter):
    iters = 0
    error = tol+1
    error_x = list()

    while error>tol and iters<=maxiter:
        y = x0-f(x0)/df(x0)
        x = y-f(x0)/(f(x0)-2*f(y))*f(y)/df(x0)
        error = math.fabs(x-x0)
        error_x.append(error)
        iters = iters+1
        x0 = x
        
    
    
    error_x = np.array(error_x)
    eps = 1e-16
    error_x_safe = np.maximum(error_x, eps)
    ACOC = np.log(error_x_safe[2:]/error_x_safe[1:-1])/np.log(error_x_safe[1:-1]/error_x_safe[0:-2])
    return [x,iters,error,ACOC]