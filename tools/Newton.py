import math

def Newton(f, df, x0, tol, maxiter):
    iters = 0
    error = tol+1

    while error > tol and iters <= maxiter:
        x = x0-f(x0)/df(x0)
        error = math.fabs(x-x0)
        iters = iters+1
        x0 = x
    return [x, iters, error]