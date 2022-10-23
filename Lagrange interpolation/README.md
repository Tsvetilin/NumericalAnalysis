# Интерполационна задача на Лагранж

## Постановка

Дадени са точките $(x_0, y_0),\cdot\cdot\cdot, (x_n, y_n)$. Търсим непрекъсната функция $f(x)$, за която $f(x_i)=y_i$ за $i \in \lbrace 0, \cdot\cdot\cdot, n\rbrace$.

## Решение

Съществува едниствен полином $p(x) \in \Pi_n$, такъв, че $p(x_i)=y_i$ за $i \in \lbrace 0, \cdot\cdot\cdot, n\rbrace$, който интерполира функцията $f(x)$ в точките $(x_0, y_0), \cdot\cdot\cdot, (x_n, y_n)$.

$x_i$ - възли на интерполацията

$y_i$ - стойности на интерполираната функция във възлите

### Базисни полиноми на Лагранж

Базисните полиноми на Лагранж са полиномите $l_{n,k}(x) \in \Pi_n$, които са дефинирани по следния начин:
$$l_{n,k}(x)= \delta_{n,k}$$ където $\delta_{n,k}$ е символа на Кронекер, тоест:

- $l_{n,k}(x_i)=1$ за $i=k$
- $l_{n,k}(x_i)=0$ за $i \neq k$

Тогава дефинираме:

$\omega(x)=(x-x_0)(x-x_1)\dots(x-x_n)$

$\omega_k(x)=\dfrac{\omega(x)}{(x-x_k)}$


Така получаваме, че $$l_{n,k}(x)=\dfrac{\omega_k(x)}{\omega_k(x_k)} = \dfrac{\omega(x)}{(x-x_k) \omega'(x_k)}$$
или по-общо:
$$l_{n,k}(x)=\displaystyle\prod_{\substack{i=0 \\ i \neq k}}^n \frac{x-x_i}{x_k-x_i}$$

### Интерполационен полином на Лагранж
$$L_n(f,x) = \displaystyle\sum_{0 \le k \le n} f(x_k) l_{n,k}(x)$$
Интерполационният полином на Лагранж от степен $n$ за $f$ с възли $x_0,\cdot\cdot\cdot, x_n$ има свойството $L_n(f,x_i)=f(x_i)$ за $i \in \lbrace 0,\cdot\cdot\cdot,n\rbrace$
### Грешка на интерполацията
Нека $f(x)$ e $(n+1)$ пъти диференцируема в  интервала $[a,b]$ и $a\le x_0 < x_1 < \cdot\cdot\cdot < x_n \le b$ и $L_n(f,x)$ е интерполационния полином на Лагранж от степен $n$, който интерполира функцията $f(x)$ в точките $\{(x_0, y_0), \cdot\cdot\cdot, (x_n, y_n)\}$. Тогава $$\forall x \in [a,b] \exists \xi \in (a,b) : f(x) - L_n(f,x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} \omega(x)$$

### Смятане на интерполационния полином на Лагранж с помощта на Wolfram Mathematica

```mathematica	
LagrangeInterpolationPolynomial[xvals_, yvals_] := Simplify[
    Sum[
      yvals[[i]] * Product[
                	(x - xvals[[k]]) / (xvals[[i]] - xvals[[k]]),
                  {k, Delete[Range[1, Count[xvals, _ ] ], i] } 
                  ],
      {i, 1, Count[xvals, _ ] } 
    ] 
]
```

Например, искаме да:
- построим интерполационен полином $p(x)$ на функцията $\sin(x)$ по дадени 9 възела,
- начертаем графиките на интерполиращия полином и дадената функция,
- сметнeмем абсолютната грешка и да я начертаем графично.
```mathematica	
xvals = {0, Pi/6, Pi/4, Pi/3, Pi/2, 2Pi/3, 3Pi/4, 5Pi/6, Pi};
yvals = {0, 1/2, Sqrt[2]/2, Sqrt[3]/2, 1, Sqrt[3]/2, Sqrt[2]/2, 1/2, 0};
p[x_]=LagrangeInterpolationPolynomial[xvals, yvals]

Plot[{Sin[x], p[x]}, {x, 0, Pi}, PlotLegends->"Expressions"]

error[x_] = Abs[Sin[x] - p[x]]
Plot[error[x], {x, 0, Pi}, PlotLegends->"Expressions"]
```