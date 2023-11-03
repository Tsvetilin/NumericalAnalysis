import numpy as np

def binom(n, k):
    return 1 if k == 0 or k == n else np.prod([(n + 1 - i) / i for i in range(1, k + 1)])

def finite_diff(values, k, i):
    if k == 0:
        return values[i]

    return finite_diff(values, k-1, i+1) - finite_diff(values, k-1, i)


def newton_backward(x, values, A, B):
    n = len(values) - 1
    nodes = np.linspace(A, B, n + 1)
    t = (x - nodes[-1]) / (nodes[1] - nodes[0])
    sum = 0
    for i in range(0, n + 1):
        sum += finite_diff(values, i, n-i) * binom(t+i-1, i)
    return sum


### EXAMPLE ###
nodes = np.linspace(np.pi/4, np.pi/3, 4)
values = np.cos(nodes)
deg_65 = 13 * np.pi / 36

print(newton_backward(deg_65, values, np.pi/4, np.pi/3))
print(np.cos(deg_65))
