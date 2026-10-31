# Three numerator coefficients simultaneously require unbounded overshoot

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel all-parameter symbolic evidence; not parent adoption.** For the explicit, constructively solvable, full-width stable septic family \(K_R\) defined in `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`), **every** common monic numerator simultaneously satisfies, for every real \(R\ge1000\),
\[
\boxed{b_2>R^4/65,\qquad b_4>R^4/100,\qquad b_6>R^2/20.}
\]
All three ratios \(b_j/\sup_{a\in K_R}a_j\) tend to infinity uniformly over the common numerators as \(R\to\infty\). Indeed, with \(\lambda=1001/1000\), every denominator has
\[
a_2<\lambda\left(R^2+R+\frac{2R+1}{20}\right),\quad
a_4<R^2/5+5/2,\quad a_6<\lambda.
\]
Thus no universal coordinatewise multiplicative cap, even on these three numerator coefficients alone, can characterize or construct a solution. The family actually has an explicit common numerator for every \(R\); this is not a negative answer to the arbitrary-box question.

## New six-atom bound for \(b_2\)

Put \(L=R^2/5\), \(h=1/(2R)\), and use the actual parity-corner numbering 0–3 from the source. The new six corner/squared-frequency atoms are
\[
(1,R-1/2),\quad(2,1+h),\quad(2,3),\quad(3,6/5),\quad
(3,3/2+h),\quad(3,L).
\]
Let \(r_i\) be their raw monomial pairing rows, and form the \(5\times6\) matrix with rows
\[
(r_{i1})_i,\ (r_{i3})_i,\ (r_{i5})_i,\ (r_{i6})_i,\
(r_{i7}+R^4r_{i2}/65)_i.
\]
Its zero-based signed cofactor weights \(w_i=(-1)^i\det M_{\widehat i}\) are strictly positive for every \(R\ge1000\). Their aggregate satisfies
\[
C_1=C_3=C_5=C_6=0,\quad C_0,C_4<0,\quad C_2>0,\quad
C_7+R^4C_2/65=0.
\]
As every common numerator is Hurwitz and has positive coefficients, \(0<C\cdot b\le C_2(b_2-R^4b_7/65)\), proving the new bound without restricting any numerator coefficient. The two other necessary bounds are from the source and `frontier-20261029-unbounded-common-numerator-b4-obstruction-v1.md` (SHA-256 `76846b831855f4becb039778365feec6033ff5d0665cb2e1b6fc54f5c2c5d9aa`).

## Constructive scale and evidence

For the source's explicit common monic numerator \(b_R\), the new replay additionally proves
\[
(b_R)_2<R^4/6,\qquad \lim_{R\to\infty}(b_R)_2/R^4=1251/8425.
\]
The matching b4 and b6 upper bounds and limits are in the two source packets. In particular the new construction matches the forced \(b_2=\Omega(R^4)\) order, although the exact optimal constant is not determined.

The frozen six-atom sign data and comparison coefficients are `frontier-20261029-unbounded-b2-family-frozen-v1.json`, SHA-256 `23b5de0abc72b49fa0ea8d6ca878c4ce052e970f3817a80fa4af699413c10099`. The checker `frontier-20261029-unbounded-b2-family-independent-kernel-v1.py`, SHA-256 `dd0fb1d459c958aaba13617d657a5233be34c75b8c252e69e316009bbdfbc7b4`, reconstructs the new atoms/cofactors from pinned independent geometry, verifies the exact four zeros and tail identity, **491** strictly positive Laurent coefficients after \(R=1000+u\), and **24** positive constructive-upper comparison coefficients. Its receipt is `frontier-20261029-unbounded-b2-family-independent-result-v1.json`, SHA-256 `db892cb32339a9a02657d991270e3574b93e7af78f02306052b6b6e344ee555b`.

All finite arithmetic uses exact `fractions.Fraction` on one Python Eval host. The sign-to-interval, homotopy and asymptotic arguments are written mathematics. The atom vectors each have a positive target coordinate; none is an all-negative certificate. No formal proof, cross-vendor review, novelty clearance, or original arbitrary-box verdict is claimed.
