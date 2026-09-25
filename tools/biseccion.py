def Biseccion(f,a,b,tol,maxiter):
    iters = 0
    error = tol+1

    while error>tol and iters<=maxiter:
        x = (a+b)/2
        error = (b-a)/2
        if f(a)*f(x)>0:
            a = x
        else:
            b = x
        iters = iters+1

    return [x,iters,error]