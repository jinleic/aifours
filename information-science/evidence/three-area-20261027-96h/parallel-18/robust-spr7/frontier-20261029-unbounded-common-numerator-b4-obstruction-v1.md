# A second forced unbounded numerator coefficient

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact symbolic replay; not parent adoption.** On the same explicitly solvable, all-seven-width stable family \(K_R\), \(R\ge100\), of `frontier-20261029-unbounded-common-numerator-b6-obstruction-v1.md` (SHA-256 `71896c927bafabc2098ab283bc6108a7b259bda028dc58c948cffb637106f8c7`), every common numerator also satisfies
\[
\boxed{\quad b_4>\frac{R^4}{100}b_7.\quad}
\]
For the monic common numerator \(b_R\) explicitly constructed there, the matching upper and exact asymptotic bounds are
\[
(b_R)_4<\frac{R^4}{40},\qquad
\lim_{R\to\infty}\frac{(b_R)_4}{R^4}=\frac8{337}.
\]
Every denominator has \(a_4<R^2/5+5/2\), so for every common monic numerator
\[
\frac{b_4}{\sup_{a\in K_R}a_4}>
\frac{R^4/100}{R^2/5+5/2}\longrightarrow\infty.
\]
Thus **both** \(b_4\) and \(b_6\) can be forced to exceed their corresponding denominator maxima by arbitrarily large factors, although the boxes have explicitly constructed common numerators. The displayed constructed \(b_4\) is within a factor \(5/2\) of the universal lower bound.

## Five-atom proof

Use the same corner numbering, \(d=1/(10R)\) and \(L=R^2/5\). Take the five actual radial corner/squared-frequency pairs
\[
(3,\tfrac32(1+d)),\quad (1,R(1+d)),\quad
(0,(R+1)(1-d)),\quad (2,L(1-d)),\quad(0,1/3).
\]
For their monomial pairing rows \(r_i\), form a \(4\times5\) matrix with rows
\[
(r_{i0})_i,\quad(r_{i1})_i,\quad(r_{i5})_i,\quad
(r_{i7}+R^4r_{i4}/100)_i.
\]
The zero-based signed cofactor weights \(w_i=(-1)^i\det M_{\widehat i}\) are strictly positive for all \(R\ge100\). Their aggregate \(C\) satisfies
\[
C_0=C_1=C_5=0,\quad C_2,C_3,C_6<0,\quad C_4>0,\quad
C_7+R^4C_4/100=0.
\]
A common numerator has strictly positive coefficients, so positivity of all five actual pairings gives \(0<C\cdot b\le C_4(b_4-R^4b_7/100)\), proving the inequality. This functional has a positive \(b_4\) coordinate and is **not** an all-negative certificate.

The independent replay checks the five cofactor signs, the target and three negative signs by verifying **466** exact Laurent-polynomial coefficients after \(R=100+u\). For the numerator from the source's positive Cramer determinant \(D\) and \(B_4\), it separately checks all **25** shifted coefficients of \(R^4D-40B_4\) are positive. Thus \(B_4/D<R^4/40\); the leading terms give the exact limit \(8/337\). The source's independent symbolic replay proves all-member stability and positivity of that numerator, so the present result is not a vacuous lower bound.

## Evidence and scope

Frozen exact sign arrays `frontier-20261029-unbounded-b4-family-frozen-v1.json`, SHA-256 `7dda51dc349ebc51b5e2f58f20c3b2e0e1a2e1d46091db48940ef50c8b99fba5`; checker `frontier-20261029-unbounded-b4-family-independent-kernel-v1.py`, SHA-256 `12f8b13cae54f481b0ab1e26b7b27702cfa77fcba9006414a7157b4fd0205bc7`; receipt `frontier-20261029-unbounded-b4-family-independent-result-v1.json`, SHA-256 `a240609b8baf93e1873df032d52a20f9b42e96c8a0a4fb2134ec9e60579225c1`. The checker reconstructs these new atoms from the pinned independent base geometry using exact `fractions.Fraction` arithmetic, and verifies the stated equalities and all signs for **every real** \(R\ge100\). The root, homotopy and positive-coefficient arguments are written mathematics. No formal proof, cross-vendor review, novelty clearance, negative-box verdict or universal arbitrary-box theorem is claimed.
