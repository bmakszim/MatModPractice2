import numpy as np
import sympy

class TaylorPol:
    # f fuggveny, x argumentum
    def __init__(self, f, x):
        self.f = f
        self.x = x

    # x_0 koruli, n-ed rendu Taylor-polinom
    def get_taylor(self, x_0, n):
        deriv = [self.f]
        for k in range(1, n + 1):
            deriv.append(sympy.diff(self.f, self.x, k))

        taylor = 0
        for k in range(0, n + 1):
            taylor += deriv[k].subs(self.x, x_0) / sympy.factorial(k) * (self.x - x_0) ** k
        
        return taylor

x_s = sympy.Symbol('x')
f_s = sympy.cos(x_s ** 6 + 2 * x_s) + x_s ** 5

taylorPol = TaylorPol(f_s, x_s)
taylor_s = taylorPol.get_taylor(0, 3)

taylor_np = sympy.lambdify(x_s, taylor_s, "numpy")
f_np = sympy.lambdify(x_s, f_s, "numpy")

diff = np.abs(taylor_np(1/3) - f_np(1/3))

print(diff)
# result is 0.011375726310031364