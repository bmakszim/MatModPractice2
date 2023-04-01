import numpy as np
import sympy

x_s = sympy.Symbol('x')
num_s = sympy.root(x_s ** 5 - x_s ** 2 - 2, 3)
den_s = sympy.exp(
    sympy.cos(x_s ** 3 - 3 * x_s + 1)
    )
f_s = num_s / den_s

def get_tangent_of_function(f, x, x_0):
    y = f.subs(x, x_0) + sympy.diff(f, x, 1).subs(x, x_0) * (x - x_0)

    return y

tangent = get_tangent_of_function(f_s, x_s, sympy.pi)

tangent_np = sympy.lambdify(x_s, tangent, "numpy")

print(tangent_np(np.sqrt(2) / 13))
# result is 675.6880252029908