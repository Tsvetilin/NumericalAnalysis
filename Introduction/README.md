# Числени методи

## Полиноми

Дефинираме множеството от абгебрични полиноми от степен ненадминаваща $n$ като:
$$\Pi_n = \left\{\displaystyle\sum_{0\le k\le n}\ a_k x_k\; |\; a_k \in \mathbb{R} \right\}$$

Дефинираме тригонометрични полиноми от степен ред $n$ като:
$$\mathcal{T}_n = \left\{\dfrac{a_0}{2}+\displaystyle\sum_{1\le k\le n}\ a_k \cos(kx)\; + b_k \sin(kx) \;|\; {a_k,b_k} \in \mathbb{R} \right\}$$

## Подходи за приближаване

#### Интерполационен
$L_0, L_1, \cdot\cdot\cdot, L_n$ - числови характеристики (функционали) $f\to L_i(f)$.
Нека $p \in \Pi_n$ и $f$ - сложа функция. Тогава казваме, че $f$ е _интерполирана_ от $p$ при $L_k$ ако $$L_k(f) \equiv L_k(p).$$

#### Метричен
Нека $\mathbb{F}$ - пространство от функции
Дефинираме _метрика_ 
$$\rho(f,g): \mathbb{F} \times \mathbb{F} \rightarrow \R^{\ge 0}$$
- $\rho(f,g) \ge 0$ и $\rho(f,g)=0 \Longleftrightarrow f \equiv g$
- $\rho(f,g) \ge 0 = \rho(g,f)$
- $\rho(f,g) \ge 0 + \rho(g,h) \ge \rho(f,h)$

Тогава казваме, че $f$ е _приближена_ от $p$ когато $\rho(f,p)$ е достатъчно малко.