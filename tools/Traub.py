import math

def Traub(f,df,x0,tol,maxiter):
    iters = 0
    error = tol + 1

    while iters <= maxiter and error > tol:
        y = x0-f(x0)/df(x0)
        x = y-f(y)/df(x0)
        error = math.fabs(x-x0)
        iters += 1
        x0 = x
    return [x,iters, error]