import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

def divided_diff(nodes, values):
    if len(nodes) == 1:
        return values[0]
    return (divided_diff(nodes[1:], values[1:]) - divided_diff(nodes[:-1], values[:-1])) / (nodes[-1] - nodes[0])


def w_product(x, nodes, k):
    result = 1
    for i in range(0, k):
        result *= x-nodes[i]
    return result


def newton_poly(x, nodes, values):
    result = 0
    for i in range(0, len(nodes)):
        result += divided_diff(nodes[0:(i+1)],
                               values[0:(i+1)])*w_product(x, nodes, i)
    return sp.simplify(result)

### EXAMPLES ###

nodes = np.array([0, 1, 3, 4, 6])
values = np.array([1, 2, 10, 17, 37])
x_sym = sp.symbols('x')
print(newton_poly(x_sym, nodes, values))
