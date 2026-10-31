# Exact synthesis on a two-parameter three-contact family

**Status: WRITTEN-checked-in-kernel; author candidate, not a parent adoption.** This extends the previous all-scales result to an explicit, nondegenerate interval of anisotropic box shapes. It remains a restricted-family result, not an answer for arbitrary septic boxes.

## Family and numerator construction

Let \(a_0(s)=(s+1)\prod_{v\in\{2,4,8\}}((s+1)^2+v^2)\), with ascending coefficients \((5525,8555,4893,2219,455,105,7,1)\). Put

\[
x_0=\frac{1530997}{1512675},\qquad |x-x_0|\le 10^{-9},
\]
\[
h(x)=\left(7878-2925x,\ 2718,\ -\frac{17188}{15}+1215x,\
\frac{172}{15},\ \frac{1346}{15}-83x,\ \frac{106}{15},\ x\right).
\]
For \(\rho\ge0\), let \(K_{x,\rho}\) have independent coefficient intervals \([a_{0,j}-\rho h_j(x),a_{0,j}+\rho h_j(x)]\), \(j=0,\ldots,6\), and leading coefficient one.

**Claim.** For every \(x\) in the displayed interval, every member of \(K_{x,\rho}\) is strictly Hurwitz exactly when \(0\le\rho<1\). Moreover, for each such \(x\), one explicitly specified positive degree-seven numerator \(\widetilde b_x\), independent of \(\rho\), works for every \(0\le\rho<1\), every member, and every real frequency.

The coefficients of \(\widetilde b_x\) are constructed rationally and without an optimization. Take the monic vector \(b^*\) displayed in `frontier-20261028-three-gap-common-numerator-all-eligible-scales-v1.md` and fix \(b_j^*\) for \(j\in\{1,3,5,6,7\}\). At \(\rho=1\), let \(a_i(x)\) be actual corners \((E_+,O_-),(E_-,O_+),(E_+,O_-)\) at \(t_i=3,15,65\), respectively. Write their parity components as \(E_i,O_i\), and define the \(3\times3\) matrix and right side

\[
\begin{aligned}
A_i(x)&=E_i'(t_i)\,[1,-t_i,t_i^2],\\
r_i(x)&=E_i'(t_i)b_6^*t_i^3-
 t_iO_i'(t_i)\bigl(b_1^*-b_3^*t_i+b_5^*t_i^2-t_i^3\bigr).
\end{aligned}
\]

Let \(D(x)=\det A(x)\), and let \(A^{(j)}(x)\) replace column \(j\) of \(A(x)\) by \(r(x)\). Define

\[
\widetilde b_{x,k}=-D(x)b_k^*\quad(k=1,3,5,6,7),\qquad
(\widetilde b_{x,0},\widetilde b_{x,2},\widetilde b_{x,4})=
-\bigl(\det A^{(1)},\det A^{(2)},\det A^{(3)}\bigr).
\]

The minus sign is fixed by the exact determinant at \(x_0\), which is negative. The certificate below proves all eight \(\widetilde b_{x,j}>0\), including \(\widetilde b_{x,7}>0\), throughout the stated interval. Division by that positive leading coefficient gives a monic numerator if desired. The numerator may vary with \(x\); no single numerator is claimed for all shapes.

## Written proof and machine-checked inequalities

All \(h_j(x)\) are affine. At each endpoint of the stated \(x\)-interval, exact arithmetic checks \(0<h_j(x)<a_{0,j}\), the three boundary contacts, negative \((E,O)\) at \(t=17/2\), and positive \((E,O)\) at \(t=30\), for all actual corners. Affinity extends these facts to the entire interval. At \(t=3,15,65\), the contact endpoints are zero at \(\rho=1\) and have the center's strict signs for \(\rho<1\). The six alternating sign bands in the preceding stability packet therefore apply uniformly: no member has an imaginary-axis root, and every box is connected to the explicitly Hurwitz center. At \(\rho=1\), the same three actual corner polynomials have imaginary roots; every larger box contains them.

Cramer's identity makes each numerator coefficient a polynomial in \(x\) of degree at most three and makes the boundary pairing derivative vanish at each contact. Since the corresponding boundary pairing itself vanishes there, the same square-factor identities as in the preceding packet hold for all \(x\): \((t-15)^2\) at corner 1 and \((t-3)^2(t-65)^2\) at corner 2. A boundary pairing coefficient has degree at most four in \(x\); so does every coefficient of each fixed compactified-frequency Bernstein leaf.

The certificate covers the four boundary residual polynomials with 11, 8, 6, and 21 frequency leaves and the center pairing with 7 leaves. These produce 392 shape-polynomials: 8 numerator coefficients plus the frequency-leaf coefficients. Each is represented in degree-four Bernstein form over the explicit \(x\)-interval. **All 1,960 parameter Bernstein coefficients are strictly positive.** Consequently all boundary residuals are strictly positive, all boundary pairings nonnegative, all numerator coefficients positive, and the center pairing strictly positive, simultaneously over every \(x\) and \(t\ge0\).

At scale \(\rho<1\), every actual-corner pairing is \((1-\rho)\) times its center pairing plus \(\rho\) times its boundary pairing. Taking the minimum of the four actual corners gives strict positivity for the entire independent coefficient box. In particular, the finite nonnegative-atom obstruction from the previous packet now holds for **every** box in this two-parameter family. It makes no claim about a different box.

One quantitative bound for the *unnormalized* \(\widetilde b_x\) follows from the minimum checked parameter coefficient

\[
m=\frac{31509255746475197022567382259363836703893711525798864673589291033926389545309307}
{1956259870478912947068210870484992000000000000000000000000000000000000}>0
\]

and \(S_{\max}=6973595952923549/236355468750\):
\[
\operatorname{Re}\frac{\widetilde b_x(i\omega)}{a(i\omega)}
\ge (1-\rho)\frac{m}{S_{\max}^2}>0.
\]
This uses the common compactified center bound and \(|a(i\sqrt t)|\le S_{\max}(1+t)^{7/2}\); it is not claimed sharp.

## Evidence and limits

- Frozen construction and interval: `frontier-20261028-three-contact-shape-neighborhood-frozen-v1.json`, SHA-256 `f7888e1b48d2cb7de599e4d0c4f62082eb1e0d2d0e83a83d50e92888f87a9439`. The needed exact frequency partitions and base witness are hash-bound to the previous frozen packets.
- Producer `frontier-20261028-three-contact-shape-neighborhood-kernel-v1.py`, SHA-256 `5992d5d774619bc0e4840c92501df1ab8bc83e63bbce0af33940572b39593f10`. It tried radius \(10^{-6}\), whose chosen leaf certificate did not prove the claim, then certified radius \(10^{-9}\); the larger-radius failure is not a counterexample.
- Independent standalone replay `frontier-20261028-three-contact-shape-neighborhood-independent-kernel-v1.py`, SHA-256 `3bd3ed4c8bc7b0b0319772880a637c783506dee68c02d1ddd7377271d0fc1621`. It builds Cramer determinants directly, reconstructs all frequency leaves, interpolates parameter polynomials through a separate monomial/Vandermonde route, verifies all 1,960 strict signs and endpoint geometry, and rejects a negative-sign control. Receipt `frontier-20261028-three-contact-shape-neighborhood-independent-result-v1.json`, SHA-256 `e35d747740b85c138c425063fcdbc27ee39c2a77d67c366dcf120255b167a1b5`.

The exact arithmetic uses Python integers and `fractions.Fraction` in one Eval host. The written proof imports polynomial degree and Cramer identities, Bernstein positivity, elementary root continuity, and linearity over independent intervals. It is not formal verification, cross-vendor review, novelty clearance, or a universal septic synthesis verdict.
