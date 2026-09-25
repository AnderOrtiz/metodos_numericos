import pandas as pd

def Bisecciontabla(f,a,b,tol,maxiter):
    iters = 0
    error = tol+1
    lista_a = list(); lista_b = list()
    lista_a.append(a); lista_b.append(b);
    lista_x = list(); lista_e = list()

    while error>tol and iters<=maxiter:
        x = (a+b)/2
        error = (b-a)/2
        lista_e.append(error); lista_x.append(x)
        if f(a)*f(x)>0:
            a = x
        else:
            b = x
        iters = iters+1
        lista_a.append(a); lista_b.append(b);
    lista_a.pop(); lista_b.pop()
    tabla = pd.DataFrame({'a': lista_a, 'b': lista_b, 'x': lista_x, 'Errores': lista_e})
    pd.set_option('display.precision', 10)
    return tabla

