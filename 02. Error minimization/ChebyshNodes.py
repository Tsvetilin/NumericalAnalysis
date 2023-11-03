import numpy as np
import matplotlib.pyplot as plt

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
    return sum

def translate(x, fromA, fromB, toA, toB):
    return (x-fromA+toA)*(toB-toA)/(fromB-fromA)

def chebyshNodes(n,A,B):
    defaultNodes=[np.cos(((2*k-1)*np.pi)/(2*n)) for k in range(1,n+1)]
    return [translate(x,-1,1,A,B) for x in defaultNodes]


### EXAMPLE ###

def func(x):
    return 1/(1+25*(x**2))

x_axis = np.linspace(0,2,100)

nodes_chebysh=chebyshNodes(10, 0, 2)
values_chebysh=func(np.array(nodes_chebysh))

nodes_equidistant = np.linspace(0,2,10)
values_equidistant = func(np.array(values_chebysh))

plt.plot(lagrange_poly(x_axis, nodes_chebysh, values_chebysh))
plt.plot(lagrange_poly(x_axis, nodes_equidistant, values_equidistant))
plt.plot(func(x_axis))
plt.show()