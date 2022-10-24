# Минимизиране на грешката

От предния път грешката на интерполация на $L_n(f,x)$ в $[a,b]$ е:
$$R_n(f,x) = f(x) - L_n(f,x) = \dfrac{f^{(n+1)}(\xi)}{(n+1)!} \omega(x), \xi \in [a,b]$$

Нека $$M_{n+1} = \max_{x \in [a,b]} f^{(n+1)}(x)$$
Тоест $M_{n+1}$ зависи от дадената функция (полинома) и тогава
$$|R_n(f,x)| \le \dfrac{M_{n+1}}{(n+1)!} \cdot\max_{x \in [a,b]} |\omega(x)|$$
Очевидно можем да минимизираме максималната стойност на $\omega(x)$.
Търсим 
$$\inf_{a \le x_0 < \cdot\cdot\cdot < x_n \le b} \Bigg( \max_{x \in [a,b]} |\omega(x)| \Bigg)$$

### Решение

Нека транслираме интервала $[a,b]$ в $[-1,1]$ с линейна трансформация:

$$ x = \dfrac{b-a}{2} t + \dfrac{a+b}{2} $$

Тогава нека транслираме корените на $T_{n+1}(x)$ - полинома на Чебишов от I род 
$$[-1,1] \ni t_k^* = \cos\dfrac{(2k+1)\pi}{2(n+1)} \longrightarrow x_k^* \in [a,b]$$
Разглеждаме стойността на $\omega(x)$:

$$
\begin{aligned}
|\omega(x)| &=\\
&= \Bigg| \displaystyle\prod_{k=0}^n ( x-x_k^* )\Bigg| = \\ 
&=\Bigg| \displaystyle\prod_{k=0}^n \Bigg(\dfrac{b-a}{2}t + \dfrac{a+b}{2} - \Bigg(\dfrac{b-a}{2}t_k + \dfrac{a+b}{2}\Bigg)\Bigg)\Bigg| = \\
&= \Bigg| \displaystyle\prod_{k=0}^n \dfrac{b-a}{2}(t- t_k)\Bigg| = \\
&= \Bigg(\dfrac{b-a}{2}\Bigg)^{(n+1)} \Bigg| \displaystyle\prod_{k=0}^n (t- t_k)\Bigg|\\
&\ge \Bigg(\dfrac{b-a}{2}\Bigg)^{(n+1)} \Bigg| \displaystyle\prod_{k=0}^n (t- t_k^*)\Bigg|\\
&= \Bigg(\dfrac{b-a}{2}\Bigg)^{(n+1)} \Bigg| \dfrac{1}{2^n}\Bigg|\\
&=\dfrac{(b-a)^{n+1}}{2^{2n+1}}\\
\end{aligned}
$$

$$"=" \Leftrightarrow t_k = t_k^* \Leftrightarrow x_k = x_k^*$$

$\Rightarrow |R_n(f,x)| \le \dfrac{M_{n+1}}{(n+1)!}\cdot \dfrac{(b-a)^{n+1}}{2^{2n+1}}$ за $x_k \equiv x_k^*$

$\Rightarrow$ най-добрите възли за интерполация са нулите на $(n+1)$-вия полином на Чебишов от I род, транслирани към интервала $[a,b]$. Така получаваме минималната възможна грешка при интерполация на $f(x)$ с $L_n(f,x)$ в $[a,b]$.
