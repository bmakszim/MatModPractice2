import numpy as np
import sympy

x_s = sympy.Symbol('x')
f_s = x_s ** 7 * sympy.exp(-2 * x_s)
fprimitive_s = sympy.integrate(f_s, x_s)

def get_primitive(f_p, x_s, x_0, y_0):
    y = f_p.subs(x_s, x_0)
    c = y_0 - y

    return f_p + c

F = get_primitive(fprimitive_s, x_s, 2, 5)

F_np = sympy.lambdify(x_s, F, "numpy")

print(F_np(np.pi / 2))

# result is 4.293784611178889