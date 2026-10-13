import math
import pandas as pd


def NewtonTabla(f, df, x0, tol, maxiter):
    iters = 0
    error = tol + 1
    lista_e = []
    lista_x = []

    while error > tol and iters < maxiter:
        x = x0 - f(x0) / df(x0)
        error = math.fabs(x - x0)
        iters = iters + 1

        lista_e.append(error)
        lista_x.append(x)
        x0 = x

    pd.set_option('display.precision', 10)
    Tabla = pd.DataFrame({"x": lista_x, "Errores": lista_e})
    Tabla.index += 1  # Ajusta el índice para que las iteraciones empiecen en 1
    Tabla.index.name = "Iteración"

    return Tabla