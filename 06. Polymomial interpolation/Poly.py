import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import sympy.utilities.lambdify as lambdify

def exp_basis(i,x):
    return np.e**(i*x)

def trig_basis(i,x):
    return sp.cos(x * i/2) if i%2==0 else sp.sin(x * (i+1)/2)

def alg_basis(i,x):
    return x**i

def rec_basis(i,x):
    return 1 if i == 0 else 1/(x+i)
 
def poly_v1(nodes,values,basis,x):
    n = len(nodes)
    coeff = sp.symbols(f'x:{n}')
    poly = 0
    for i in range(0,n):
        poly+=coeff[i]*basis(i,x)
    equations = [sp.Eq(poly.subs(x,nodes[i]), values[i]) for i in range(n)]
    coeff_res= sp.solve(equations, coeff, dict=True)
    res = [poly.subs(c) for c in coeff_res]
    return res[0] if len(res)==1 else res


def poly_v2(nodes, values, func_basis, x ):
    A_matrix = np.zeros([len(nodes), len(values)])
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            A_matrix[i,j] = func_basis(j, nodes[i])
    coeff = np.linalg.solve(A_matrix,values)
    poly = 0
    for i in range(len(coeff)):
        poly += coeff[i] * func_basis(i, x)
    return poly



### Example ###

x_sym = sp.symbols('x')

nodes = np.array([1,1.03,1.07,1.15,1.21,1.27,1.3])
values = np.array([1,1.06,2.09,22.1,99.78,328.602,600])
x_axis = np.linspace(1,1.3,100)

basis_tries = [exp_basis,trig_basis,alg_basis, rec_basis]
for basis in basis_tries:
    solved = poly_v1(nodes, values, basis, x_sym)
    if isinstance(solved, list): 
        continue
    poly_res = sp.simplify(solved)
    poly_func = lambdify(x_sym, poly_res, 'numpy')

    print(poly_res)
    plt.plot(x_axis, poly_func(x_axis))
    
plt.plot(x_axis,poly_v2(nodes,values,exp_basis, x_axis))

plt.plot(nodes,values,'ro')
plt.show()