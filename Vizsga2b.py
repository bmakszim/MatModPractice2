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

def get_result(x_s, fx_s, x_0, n, x):
  taylor_s = TaylorPol(fx_s, x_s).get_taylor(x_0, n)
  taylor_np = sympy.lambdify(x_s, taylor_s, "numpy")

  return taylor_np(x)

x_s = sympy.Symbol('x')
fx_s = sympy.sin(x_s) / (x_s ** 2 + sympy.exp(-1 * x_s))
x_0 = sympy.pi / 3
n = 8

print(get_result(x_s, fx_s, x_0, n, 2))