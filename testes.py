import sympy as sp

x = sp.symbols("x")
Fx = (((2*x+3)/(5*x+4))/((2)/(5)))**x

print(sp.limit(Fx, x, "oo"))