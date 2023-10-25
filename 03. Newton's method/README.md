# Интерполационна формула на Нютон

## Разделени разлики

Имаме $x_0 \lt x_1 \lt \dots \lt x_n$ и $f: \mathbb{R}\rightarrow \mathbb{R}$

Дефинираме разделената разлика $f[\cdots]$ рекурсивно като линеен функционал по следния начин:

$$ f[x_k] = f(x_k) $$
$$ f[x_0,x_1,\dots,x_{n-1},x_n] = \dfrac{f[x_1,\dots,x_n] - f[x_0,\dots,x_{n-1}]}{x_n-x_0}$$

И притежава следните свойства:

1) $$(f + c \cdot g)[x_0,\dots ,x_n]=f[x_0,\dots ,x_n]+c \cdot g[x_0,\dots ,x_n] $$

2) $$f(x)=x^n\in\Pi_n \Rightarrow f(x)=l_n(f,x)=f[x_0,\dots ,x_n] \cdot x^n $$

3) $$f(x)=a\cdot x^n + \dots \in\Pi_n \Rightarrow f[x_0,\dots ,x_n]=a \newline x^n[x_0,\dots ,x_n]=1 \newline x^k[x_0,\dots ,x_n] = 0$$


## Интерполационна формула на Нютон

Нека

$$ P_n(f,x) = f[x_0] + \sum_{k=1}^n \Bigg( f[x_0,\dots,x_k] \cdot \prod_{i=0}^{k-1} (x-x_i) \Bigg) $$

Тогава е в сила, че

$$ P_n(f,x) \equiv L_n(f,x) $$

Също така:

$$ f(x) - L_n(f,x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} \cdot \omega(x)$$

$$ f[x_0,\dots ,x_n] = \dfrac{f^n(\xi)}{n!} $$

## Смятане на интерполационния полином на Нютон с помощта на Wolfram Mathematica

Първо ни е необходима функция, която да смята разделените разлики:

```mathematica
dividedDiff[nodes_,values_] := (
    If[Length[nodes]==1,
        Return[ values[[1]]],
        Return[ (dividedDiff[nodes[[2;;]],values[[2;;]]] - dividedDiff[nodes[[1;;-2]],values[[1;;-2]]]) /
                (nodes[[-1]]-nodes[[1]])
        ]
    ]
)
```

Вече може да построим и самия полином:

```mathematica
newtonPoly[nodes_,values_, x_] := Simplify[
     values[[1]] + Sum[
        dividedDiff[nodes[[1;;k]],values[[1;;k]]] * Product[(x-nodes[[i]]),{i,1,k-1}],
        {k,2,Length[values]}
        ]
]
```