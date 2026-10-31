# A stable convex septic polytope with separated root bands and no common numerator

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact finite replay; not parent adoption.** An explicit compact **convex** family of monic Hurwitz septics has globally disjoint, ordered even/odd root bands but admits a strictly negative five-atom certificate and has no common SPR numerator. Its independent coefficient interval hull is unstable, so this is **not** an original eligible interval-box counterexample. It proves that convex stability and separated root bands alone cannot establish the desired universal positive theorem: the extra independent-box structure must be used.

## Five stable vertices and a negative atom sum

For \(i=1,\ldots,5\), let
\[
E_i(t)=-\lambda_i(t-1/2)(t-e_i)(t-5),\qquad
O_i(t)=-(t-o_i)(t-9/2)(t-7),
\]
and define the monic septic \(a_i\) by \(a_i(i\sqrt t)=E_i(t)+i\sqrt t\,O_i(t)\). Set
\[
\begin{aligned}
(e_i)&=(16/5,16/5,2,16/5,2),\\
(o_i)&=(9/10,13/10,9/10,9/10,9/10),\\
(\lambda_i)&=\left(
\frac{858880477}{14596514350},\frac{1812236890464}{316363077984025},
\frac{259887278802528}{5798793702625},\frac{16273752080992}{22780291875},
\frac{2716132065361}{252194101600}\right).
\end{aligned}
\]
Their even and odd roots interlace strictly; the independent checker also verifies all 35 positive leading Hurwitz minors. At frequencies
\[
(\omega_1,\ldots,\omega_5)=\left(1,\frac{11}{10},\frac32,\frac74,\frac{11}{5}\right)
\]
take the positive integer weights
\[
\begin{aligned}
(w_1,\ldots,w_5)=(&14826023178193030376722149,\
17669313092578582968750000,\
186715719700951025634896,\\
&14459019461750882304000,\
38701270664860781250000).
\end{aligned}
\]
Exact raw monomial pairing accumulation yields
\[
C=542000236386270050789400\left(-1,-1,-1,-1,-1,-1,-1,
-\frac{1256521167}{64000000}\right).
\]
Thus all eight coordinates are strictly negative. Any common equal-degree SPR numerator would be Hurwitz with strictly positive coefficients, so \(C\cdot b<0\); every one of its five actual atom pairings would be positive, so \(C\cdot b>0\). Contradiction.

## The whole convex hull is stable, with common ordered bands

Let \(a=\sum_i\theta_i a_i\), \(\theta_i\ge0\), \(\sum_i\theta_i=1\). Its parity parts factor **exactly** as
\[
E_a(t)=-\bar\lambda(t-1/2)(t-\bar e)(t-5),\quad
O_a(t)=-(t-\bar o)(t-9/2)(t-7),
\]
where
\[
\bar\lambda=\sum_i\theta_i\lambda_i>0,\quad
\bar e=\frac{\sum_i\theta_i\lambda_i e_i}{\bar\lambda}\in[2,16/5],\quad
\bar o=\sum_i\theta_i o_i\in[9/10,13/10].
\]
Hence **every** convex member has the separated interlacing roots
\[
1/2<\bar o<\bar e<9/2<5<7.
\]
The six global parity-root bands are exactly
\[
\{1/2\},\quad[9/10,13/10],\quad[2,16/5],\quad
\{9/2\},\quad\{5\},\quad\{7\},
\]
in alternating even/odd order. The argument principle (or Hermite–Biehler interlacing criterion) makes every convex member Hurwitz. Equivalently, the checker verifies the six strict parity-sign markers at \(3/4,3/2,4,19/4,6,8\) for all five vertices; affine averaging preserves those signs, excludes axis roots throughout the convex hull, and homotopy from a checked Hurwitz vertex gives all-member stability.

The five atom samples have classes \((2,1,3,2,4)\), two genuine reversed intervals in \(O_1,E_2\), and the necessary ratio \(r_2>r_3\). Thus even the separated-band and ratio restrictions do not, by themselves, exclude this strict negative certificate. The missing premise is **independent coefficient-box closure**, not compactness, convexity or all-member stability of the displayed polytope.

## Why no original interval box is supplied

The componentwise independent coefficient hull of these five vertices has seven positive widths, but contains the actual monic polynomial
\[
(s^7+700s^6+\tfrac{25}{2}s^5+s^4+46s^3+10000s^2+29s+1),
\]
whose third leading Hurwitz minor is exactly \(-15531251<0\). The checker verifies every one of its seven coefficients lies inside the vertex-wise minimum/maximum interval. Therefore **every** independent coefficient box containing the vertices contains an unstable member and is ineligible for the original problem. This countermechanism must not be promoted to an eligible-box negative verdict.

## Evidence and limits

Frozen vertex factors, weights, exact sums and unstable interval member: `frontier-20261029-stable-polytope-five-atom-negative-frozen-v1.json`, SHA-256 `eca087b6a3290627a12b8121c8359f12b5b4814a839500a7638f331f2de61bab`. Independent exact checker `frontier-20261029-stable-polytope-five-atom-negative-independent-kernel-v1.py`, SHA-256 `6c0cd1ca82def495a34a33524a9e1b6833a687d19b51cc8154940489cbe5a404`, verifies 35 positive vertex Hurwitz minors, 60 strict marker signs, all eight negative sums, the ratio condition and the unstable hull member; receipt `frontier-20261029-stable-polytope-five-atom-negative-independent-result-v1.json`, SHA-256 `ea82d733c6d2d60a7b01e037a6e9ea3e9bef956b1b81585383e5e2db30cf64bd`. The finite arithmetic is exact integer/`fractions.Fraction` on one Python Eval host; convex-factor, interlacing and homotopy arguments are written mathematics. No formal proof, cross-vendor review, novelty clearance, or original interval-box verdict is claimed.
