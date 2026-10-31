# All other prefixes, every Schatten norm, and all shifted log determinants still do not imply k3

**Exact abstract spectral obstruction, NOT a physical channel counterexample.** At `p=2/3` the vector `y` below is the actual pure-product reference spectrum. The positive, normalized, sorted vector `x` violates only its index-three prefix, yet meets every other prefix inequality, every Schatten-q comparison for `1<=q<=infinity`, and every shifted log-determinant inequality `u>=0`. We do **not** assert that x is the spectrum of any depolarizing-channel output. Thus these scalar spectral inequalities alone, even all together, cannot close the original k3 problem; a genuine physical constraint is necessary. No novelty, prior-paper completeness, formal/human/stronger-family review, or history cure is claimed.

## 1. The exact two spectra

Set

\[
\begin{aligned}
405y&=(80,40,40,40,40,20,20,20,20,20,20,10,10,10,10,5),\\
405x&=(77,42,42,39,39,21,20,20,20,20,20,10,10,10,10,5).
\end{aligned}\tag{1}
\]

Both are nonnegative, sum to one, and are sorted. Since `a=2/3,b=1/3`, y is exactly the spectrum of `Phi_(2/3)^tensor4(|0000><0000|)` with binomial multiplicities. Their 16 prefix differences `sum_(j<=k)(x_j-y_j)`, with common denominator 405, are

\[
(-3,-1,1,0,-1,0,0,0,0,0,0,0,0,0,0,0).\tag{2}
\]

Thus every other prefix comparison holds, including k1,2,4,5,6,10–15 and trace; the strict k3 excess is `1/405`. This is a comparison of **abstract spectra**, not an actual rho/P/noise violation.

## 2. All positive shifted log determinants

The ten unchanged factors are positive and cancel. With `z=405u`, direct exact expansion gives

\[
\begin{aligned}
&(z+77)(z+42)^2(z+39)^2(z+21)
 -(z+80)(z+40)^4(z+20)\\
&=130z^4+19336z^3+1074361z^2+26418964z+242482148>0
\quad(z\ge0).
\end{aligned}\tag{3}
\]

Hence `prod_j(u+x_j)>prod_j(u+y_j)` for every `u>=0`, and the shifted logdet of diagonal x is strictly **greater**, the direction obeyed by the public comparison theorem. The relevant named public source is Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, Theorem 4, https://arxiv.org/html/2609.37240 ; its proof is not imported or independently reviewed here. Inequality (3) is a direct identity and is stronger for this example than appealing to any source.

## 3. Every Schatten-q norm, continuously in q

Put `A=16/81`, `Q=8/81`, `R=4/81`, `epsilon=1/405`. The six changing eigenvalues move continuously from the reference to x as

\[
(A-3s,\;Q+2s,\;Q+2s,\;Q-s,\;Q-s,\;R+s),
\qquad 0\le s\le\epsilon.\tag{4}
\]

For all such s, the exactly verified inequalities are

\[
\begin{aligned}
&A-3s\ge Q+2s\ge Q-s\ge R+s>0,\\
&Q-R\ge5s,\quad 3(A-Q)\ge18s,\quad
 3A-2Q-R\ge20s.
\end{aligned}\tag{5}
\]

For any real exponent `z>=1`, the derivative of `sum_j x_j(s)^z`, divided by z, equals

\[
-3\phi(A-3s)+4\phi(Q+2s)-2\phi(Q-s)+\phi(R+s),
\qquad\phi(v)=v^{z-1}.\tag{6}
\]

If `1<=z<=2`, `phi` is increasing and concave. Equation (5) gives both `A-3s>=Q+2s` and `(Q+2s+R+s)/2<=Q-s`; Jensen's inequality makes (6) nonpositive after splitting it as

\[
-3[\phi(A-3s)-\phi(Q+2s)]
+[\phi(Q+2s)+\phi(R+s)-2\phi(Q-s)].
\]

If `z>=2`, `phi` is increasing and convex. The five-vector

\[
U=(A-3s,A-3s,A-3s,Q-s,Q-s)
\]

weakly majorizes

\[
V=(Q+2s,Q+2s,Q+2s,Q+2s,R+s).
\]

Indeed, the first three prefix comparisons follow from the first line of (5); the fourth difference is `3(A-Q)-18s>=0`, and the fifth is `3A-2Q-R-20s>=0`. Therefore `sum phi(U)>=sum phi(V)` by the standard increasing-convex weak-majorization inequality, so (6) is again nonpositive. Integrating from zero to epsilon proves

\[
\sum_j x_j^z\le\sum_j y_j^z\qquad\text{for every real }z\ge1.
\tag{7}
\]

At `z=1` equality is trace equality. Taking z-th roots gives all finite Schatten-z comparisons, and `max(x)=77/405<80/405=max(y)` gives `z=infinity`. This is a genuine continuous-exponent written proof, not a finite grid.

## 4. Machine-checked exact identities and implications

`frontier-20261028-101-spectral-obstruction-check.py`, SHA256 `5a95587afdf5df2fd44a5470176e998a0ba69e3c88d245c8825cf02415697f92`, ran with `python3 -B`, exit0. Integer/Fraction arithmetic checked the exact vectors, all 16 prefix differences, every coefficient in (3), and the linear endpoint inequalities in (5). Since each inequality in (5) is affine in s, checking its two endpoints verifies it throughout `[0,epsilon]`; the continuous-exponent argument itself is the written Jensen/weak-majorization reasoning in §3, not a numerical exponent enumeration. Native checker-pin clock `Wed Oct 28 20:22:53 PDT 2026`.

The example is a rigorously stated **nonimplication at the scalar spectral-data level**. It does not disprove original k3, imply any channel can generate x, or verify any claim about genuinely multipartite-entangled rho. The unresolved requirement is an actual common-state/projector or other physical-structure constraint beyond all these spectral inequalities. The general k5/k6 and k10 candidates retain their own unreviewed status; even granting every other prefix as an assumption would not eliminate this obstruction.
