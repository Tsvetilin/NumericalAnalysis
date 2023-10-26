import numpy as np
import sympy as sp
import sympy.utilities.lambdify as lambdify
import math
import matplotlib.pyplot as plt

x_sym = sp.symbols('x')


def lagrange_basis(x, k, nodes):
    product = 1
    for i in range(0, len(nodes)):
        if (i == k):
            continue
        product *= (x - nodes[i]) / (nodes[k] - nodes[i])
    return product


def lagrange_poly(x, nodes, values):
    sum = 0
    for i in range(0, len(nodes)):
        sum += values[i] * lagrange_basis(x, i, nodes)
    return sp.expand(sum)

def lagrange_poly_equidistant_interaval(x, n, A, B, func):
    nodes = np.linspace(A, B, n+1)
    return lagrange_poly(x,nodes,func(nodes))
    

def eval_error(x, nodes, func):
    n = len(nodes)
    d = sp.diff(func(x_sym), x_sym, n)
    d_max = sp.maximum(d, x_sym, sp.Interval(nodes[0], nodes[len(nodes)-1]))
    w = 1
    for node in nodes:
        w *= x - node
    return (d_max / math.factorial(n)) * abs(w)


### EXAMPLE ###

# This sine function

x_axis = np.linspace(0, np.pi/2, 100)
nodes = np.array([0, np.pi/6, np.pi/3, np.pi/2])
values = np.sin(nodes)


sin_lagrange_poly = lagrange_poly(x_sym, nodes, values)
sin_lagrange = lambdify(x_sym, sin_lagrange_poly, 'numpy')
sin_equidistant = lagrange_poly_equidistant_interaval(x_sym, 3, 0, np.pi/2, np.sin)

plt.plot(nodes, np.sin(nodes), 'ro', color='blue')
plt.plot(x_axis, np.sin(x_axis), color='orange', linestyle='solid')
plt.plot(x_axis, sin_lagrange(x_axis), color='black', linestyle='dotted')
plt.legend(['values of nodes', 'sin(x)', 'Lagrange polynomial for sin(x)'])
plt.show()

plt.plot(x_axis, abs(np.sin(x_axis) - sin_lagrange(x_axis)))
plt.plot(x_axis, eval_error(x_axis, nodes, sp.sin))
plt.legend(["Absolute error",
           "Upper bound error approximation"], loc="lower right")
plt.show()

print('\033[1m' + 'Langrange interpolation polynomial: ', sin_lagrange_poly)
print('\033[1m' + 'Langrange interpolation polynomial with equidistant nodes: ', sin_equidistant)
print('\033[1m' + "Result from interpolation @ Pi/5: ",
lagrange_poly(np.pi/5, nodes, values))
print('\033[1m' + "Sin(Pi/5): ", np.sin(np.pi/5))
print('\033[1m' + "Upper bound error approximation: ",
eval_error(np.pi/5, nodes, sp.sin))
