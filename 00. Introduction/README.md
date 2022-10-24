# Числени методи

## Полиноми

#### Алгебрични полиноми
Дефинираме множеството от абгебрични полиноми от степен ненадминаваща $n$ като:
$$\Pi_n = \left\lbrace \displaystyle\sum_{0\le k\le n}\ a_k x_k \Bigg| a_k \in \mathbb{R} \right\rbrace$$

#### Тригонометрични полиноми
Дефинираме тригонометрични полиноми от ред $n$ като:
$$\tau_n = \left\lbrace \dfrac{a_0}{2}+\displaystyle\sum_{1\le k\le n}\ a_k \cos(kx) + b_k \sin(kx) \Bigg| {a_k,b_k} \in \mathbb{R} \right\rbrace$$

#### Полиноми на Чебишов
Дефинираме полиномите на Чебишов от ред $n$ като:
$$T_n(x)= \cos(n \arccos(x)), x\in[-1,1]$$

Може да се забележи, че:
$T_{n+1}(x)=2xT_n(x)-T_{n-1}(x)$
$T_n(x) \in \Pi_n$ (точно $n$)
$T_n(x) =2^{n-1}x^n + \cdot\cdot\cdot$
$T_n(x)$ е четна при $n$-четно и нечетна при $n$-нечетно
$|T_n(x)| \le 1$
$T_n(x) = 0 \Leftrightarrow \xi_k = \cos\dfrac{(2k-1)\pi}{2n}, k\in\lbrace 1,\cdot\cdot\cdot,n\rbrace$ 

$\Rightarrow$ полиномите на Чебишов от I род $T_n(x)$ са **алгебрични полиноми** от степен $n$

## Подходи за приближаване

#### Интерполационен
Нека $L_0, L_1, \cdot\cdot\cdot, L_n$ - числови характеристики (функционали) $f\to L_i(f)$.
Нека $p \in \Pi_n$ и $f$ - сложа функция. Тогава казваме, че $f$ е _интерполирана_ от $p$ при $L_k$ ако $$L_k(f) \equiv L_k(p).$$

#### Метричен
Нека $\mathbb{F}$ - пространство от функции
Дефинираме _метрика_ $\rho(f,g): \mathbb{F} \times \mathbb{F} \rightarrow \mathbb{R}^{\ge 0}$
- $\rho(f,g) \ge 0$ и $\rho(f,g)=0 \Longleftrightarrow f \equiv g$
- $\rho(f,g) \ge 0 = \rho(g,f)$
- $\rho(f,g) \ge 0 + \rho(g,h) \ge \rho(f,h)$

Тогава казваме, че $f$ е _приближена_ от $p$ когато $\rho(f,p)$ е достатъчно малко.