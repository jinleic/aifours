import numpy as np, sympy as sp
p0,p1,p2=sp.symbols('p0 p1 p2',positive=True)
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Z=sp.Matrix([[1,0],[0,-1]]); Yp=sp.Matrix([[0,-sp.I],[sp.I,0]])
N=[sp.sqrt(p0)*I2, sp.sqrt(p1)*X, sp.sqrt(p2)*Z]
ys=sp.symbols('y0:12')
Y=[sp.Matrix(2,2,ys[4*k:4*k+4]) for k in range(3)]
c1=sum((Y[d]*N[d].H for d in range(3)),sp.zeros(2,2)); c2=sum((N[d].H*Y[d] for d in range(3)),sp.zeros(2,2))
eqs=list(c1)+list(c2)
sol=sp.solve(eqs,ys,dict=True)
print(sol)
