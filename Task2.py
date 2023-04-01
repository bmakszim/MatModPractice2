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
f_s = sympy.exp(-1 * x_s ** 2) * sympy.cos(2 * x_s + 3)

taylor_s = TaylorPol(f_s, x_s).get_taylor(0, 6)

taylor_np = sympy.lambdify(x_s, taylor_s, "numpy")

print(taylor_np(2 * np.pi / 7))
#result is 0.23617826445743773