import sympy as sp
import math


def divided_diff(nodes, values, l, r):
    if nodes[l] == nodes[r]:
        return values[nodes.index(nodes[l]) + r - l] / math.factorial(r - l)
    return (divided_diff(nodes, values, l + 1, r) - divided_diff(nodes, values, l, r - 1)) / (nodes[r] - nodes[l])


def w_product(x, nodes, k):
    result = 1
    for i in range(0, k):
        result *= x-nodes[i]
    return result


def hermit_poly_v1(x, nodes, values):
    result = 0
    for i in range(0, len(nodes)):
        result += divided_diff(nodes, values, 0, i) * w_product(x, nodes, i)
    return sp.expand(result)


def hermit_poly_v2(x, nodes, values):
    coeff = sp.symbols(f'x:{len(nodes)}')
    poly = 0
    for i in range(0, len(coeff)):
        poly += coeff[i]*(x**i)

    equations = []
    for i in range(0, len(nodes)):
        der = i - nodes.index(nodes[i])
        equations.append(sp.diff(poly, x, der).subs({x: nodes[i]}) - values[i])

    coeff_res = sp.solve(equations, coeff, dict=True)
    return [sp.expand(poly.subs(c)) for c in coeff_res]


### EXAMPLES ###
x_sym = sp.symbols('x')

nodes = [0, 0, 1, 1, 1]
values = [-1, -2, 0, 10, 40]

print(hermit_poly_v1(x_sym, nodes, values))
print(hermit_poly_v2(x_sym, nodes, values))