# Actividad de Repaso - Parcial 2

**Temas del parcial 2:**
- Métodos **iterativos** multipaso.
- Métodos iterativos para resolver sistemas de ecuaciones.

**Fecha:** 29 de octubre del 2026

De los problemas de la lista, seleccionar solamente tres de ellos y subirlos en el apartado correspondiente.

---

### 1. Método de Chun

A continuación, se define el método de Chun de la siguiente manera:

$$
\begin{aligned}
y_k &= x_k - \frac{f(x_k)}{f'(x_k)} \\
x_{k+1} &= y_k - \frac{f(x_k) + 2f(y_k)}{f(x_k)} \frac{f(y_k)}{f'(x_k)}
\end{aligned}
$$

a) Programar el método de Chun en Python.  
b) Resolver la ecuación utilizando el método de Chun la ecuación $(x - 1)^3 - 1 + e^x = 0$, utilizando una estimación de $x_0 = 0.1$ y la tolerancia de $10^{-7}$. Obtener la solución aproximada, el error, la cantidad de iteraciones realizadas y el ACOC.

---

### 2. Método SH4

Se considera el Método SH4 definido como:

$$
\begin{aligned}
y_k &= x_k - \frac{f(x_k)}{f'(x_k)} \\
z_k &= y_k - \frac{f(x_k)}{f(x_k) - 2f(y_k)} \frac{f(y_k)}{f'(x_k)} \\
x_{k+1} &= z_k - \frac{f(x_k) + 2f(y_k)}{f(x_k) + 4f(y_k)} \frac{f(z_k)}{f'(x_k)}
\end{aligned}
$$

a) Programar el método de SH4 en Python.  
b) Resolver la ecuación utilizando el método SH4 la ecuación $x^2 - x e^x + \cos(x) = 0$ utilizando una estimación de $x_0 = 1$ y la tolerancia de $10^{-8}$. Obtener la solución aproximada, el error, la cantidad de iteraciones realizadas y el ACOC.

---

### 3. Método MMC2

El método MMC2 está definido de la siguiente manera:

$$
\begin{aligned}
y_k &= x_k - \frac{f(x_k)}{f'(x_k)} \\
z_k &= y_k - \frac{f(x_k)}{f(x_k) - 2f(y_k)} \frac{f(y_k)}{f'(x_k)} \\
x_{k+1} &= z_k - \left( 2 + 3\frac{f(y_k)}{f(x_k)} - \frac{f(x_k)}{f(x_k) - f(y_k)} \right) \frac{f(z_k)}{f'(x_k)}
\end{aligned}
$$

a) Programar el método MMC2 en Python.  
b) Resolver la ecuación utilizando el método MMC2 la ecuación $\sqrt{x^2 + 2x + 5} - 2\sin(x) + x^2 - 3 = 0$ utilizando una estimación de $x_0 = 3$ y la tolerancia de $10^{-12}$. Obtener la solución aproximada, el error, la cantidad de iteraciones realizadas y el ACOC.

---

### 4. Método Iterativo de 3 Pasos SH8

Se considera el método iterativo de 3 pasos SH8:

$$
\begin{aligned}
y_k &= x_k - \frac{f(x_k)}{f'(x_k)} \\
z_k &= y_k - \frac{f(x_k)}{f(x_k) - 2f(y_k)} \frac{f(y_k)}{f'(x_k)} \\
x_{k+1} &= z_k - \frac{f(x_k) + 6f(y_k)}{f(x_k) + 8f(y_k)} \frac{f(z_k)}{f'(x_k)}
\end{aligned}
$$

a) Programar el método de SH8 en Python.  
b) Resolver la ecuación utilizando el método SH8 la ecuación $\sin(x) + x^2 - 1 = 0$ utilizando una estimación de $x_0 = -2$ y la tolerancia de $10^{-8}$. Obtener la solución aproximada, el error, la cantidad de iteraciones realizadas y el ACOC.

---

### 5. Método de Trapecios para Sistemas No Lineales

Otro método iterativo utilizado para resolver sistemas no lineales es el **Método** de Trapecios:

$$
\begin{aligned}
\mathbf{y}^{(k)} &= \mathbf{x}^{(k)} - J^{-1}(\mathbf{x}^{(k)}) F(\mathbf{x}^{(k)}) \\
\mathbf{x}^{(k+1)} &= \mathbf{x}^{(k)} - 2 \left[ J(\mathbf{y}^{(k)}) + J(\mathbf{x}^{(k)}) \right]^{-1} F(\mathbf{x}^{(k)})
\end{aligned}
$$

a) Diseñar el Método de Trapecios en Python.  
b) Con el Método de Trapecios resolver el sistema no lineal:

$$
\begin{aligned}
2x + 3y - 4 &= 0 \\
e^{-x} - y^2 + \cos(x) &= 0
\end{aligned}
$$

Considerando la estimación inicial $\mathbf{x}^{(0)} = (-1, 1)^T$ con una tolerancia de $10^{-10}$.

---

### 6. Método de Simpson para Sistemas No Lineales

El método de Simpson para resolver sistemas no lineales está definido como:

$$
\begin{aligned}
\mathbf{y}^{(k)} &= \mathbf{x}^{(k)} - J^{-1}(\mathbf{x}^{(k)}) F(\mathbf{x}^{(k)}) \\
\mathbf{x}^{(k+1)} &= \mathbf{x}^{(k)} - 6 \left[ J(\mathbf{x}^{(k)}) + 4 J\left( \frac{\mathbf{x}^{(k)} + \mathbf{y}^{(k)}}{2} \right) + J(\mathbf{y}^{(k)}) \right]^{-1} F(\mathbf{x}^{(k)})
\end{aligned}
$$

a) Implementar el Método de Simpson en Python.  
b) Resolver el sistema no lineal con el método de Simpson:

$$
\begin{aligned}
4x^2 + y^2 - 4 &= 0 \\
x + y - \sin(x - y) &= 0
\end{aligned}
$$

Usando una estimación inicial $\mathbf{x}^{(0)} = (0, 0)^T$ y establecer la tolerancia de $10^{-9}$.

---

### 7. Sistema No Lineal y Métodos Comparativos

Se considera el sistema no lineal:

$$
\begin{aligned}
3x^2 - y^2 &= 0 \\
3xy^2 - x^3 - 1 &= 0
\end{aligned}
$$

a) Obtener la matriz jacobiana asociada al sistema no lineal de ecuaciones.  
b) Resolver el sistema anterior usando los métodos de Newton, Simpson y Trapecios usando la estimación inicial $\mathbf{x}^{(0)} = (1, 1)^T$ y una tolerancia de $10^{-6}$. Obtener por cada método la solución aproximada, el error, la cantidad de iteraciones realizadas.


$$
J(x, y) = \begin{bmatrix} \dfrac{\partial f}{\partial x} & \dfrac{\partial f}{\partial y} \\[6pt] \dfrac{\partial g}{\partial x} & \dfrac{\partial g}{\partial y} \end{bmatrix} = \begin{bmatrix} 2 & 3 \\[6pt] -e^{-x} - \sin(x) & -2y \end{bmatrix}
$$