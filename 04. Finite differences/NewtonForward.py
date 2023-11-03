import numpy as np

def binom(n, k):
    return 1 if k == 0 or k == n else np.prod([(n + 1 - i) / i for i in range(1, k + 1)])


def finite_diff(values, k, i):
    if k == 0:
        return values[i]

    return finite_diff(values, k-1, i+1) - finite_diff(values, k-1, i)


def newton_forward(x, values, A, B):
    n = len(values)
    nodes = np.linspace(A, B, n)
    t = (x - nodes[0]) / (nodes[1] - nodes[0])

    sum = 0
    for i in range(0, n):
        sum += finite_diff(values, i, 0) * binom(t, i)
    return sum


### EXAMPLE ###
nodes = np.linspace(np.pi/4, np.pi/3, 4)
values = np.cos(nodes)
deg_52 = 13 * np.pi / 45

print(newton_forward(deg_52, values, np.pi/4, np.pi/3))
print(np.cos(deg_52))
