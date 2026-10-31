# No uniform coefficient cap for common septic numerators

**Status: WRITTEN theorem candidate with WRITTEN-checked-in-kernel exact symbolic replay; not parent adoption.** There are explicit all-member-Hurwitz, all-seven-width septic boxes which possess explicit common numerators, yet force the \(s^6\) coefficient of **every** monic common numerator to be arbitrarily large compared with the same denominator coefficient. This is a genuine obstruction to a broad class of proposed constructive certificates, not an unrestricted negative-box verdict.

## The theorem

For every real \(R\ge100\), set
\[
L=R^2/5,\quad u=1/20,\quad\lambda=1001/1000,\quad
\rho=1-R^{-4},
\]
and form boundary parity polynomials
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-R)(t-R-1),&
E_+&=-(t-1)(t-3/2)(t-L),\\
O_-&=-(t-1)(t-R-1)(t-L),&
O_+&=-(t-3/2)(t-R)(t-L-1).
\end{aligned}
\]
Use their coefficients to form the seven independent boundary intervals: for example, \(\ell_0^\partial=E_-(0)\), \(u_0^\partial=E_+(0)\), \(\ell_2^\partial=-[t]E_+\), \(u_2^\partial=-[t]E_-\), with the same alternating rule for the remaining even and odd coefficients. Let \(K_R\) be the midpoint-centered radial box at factor \(\rho\), always monic degree seven.

**Claims.**

1. All seven widths of \(K_R\) are positive, every member is Hurwitz, and there is an explicit monic common SPR numerator \(b_R\), constructed below.
2. Every common numerator \(b\) of \(K_R\) with positive leading coefficient satisfies
\[
\boxed{\quad b_6>\frac{R^2}{20}b_7.\quad}
\]
Every denominator satisfies \(a_6<1001/1000\). Consequently, after monic normalization,
\[
\frac{b_6}{\sup_{a\in K_R}a_6}>\frac{50R^2}{1001}\longrightarrow\infty.
\]
Thus no universal constant \(C\) can guarantee a common monic numerator with \(b_6\le C\sup_{a\in K}a_6\), even when \(K\) is a full-width stable septic box that actually has a common numerator. The statement does not assert that arbitrary stable boxes have or lack one.

## Whole-box stability

The exact sign certificate below proves every boundary lower coefficient and every one of the seven boundary widths strictly positive. For \(R\ge100\),
\(0<u<1<3/2<R<R+1<L<L+1\). At the five displayed contact nodes, the interior radial parity extrema have successive sign pairs
\[
(-,+),\quad(-,-),\quad(+,-),\quad(+,+),\quad(-,+).
\]
At zero both are positive, and at infinity both are negative. Each actual even and odd cubic consequently has exactly three positive simple zeros in six disjoint interlacing bands; the evaluation extrema bracket every actual member because the intervals are independent. No member has an imaginary-axis zero. The sequence of quadrant crossings gives a total argument increase of \(7\pi\) from \(-i\infty\) to \(+i\infty\); the argument principle for the monic septic then gives zero right-half-plane roots. Thus every actual member is Hurwitz. This step uses the written root/argument principle, not a sampled stability check.

## Five positive atoms force the lower bound

Number the four actual radial parity corners 0–3 as \((--),(-+),(+-),(++)\). Put \(d=1/(10R)\), and use the five actual corner/squared-frequency pairs
\[
\begin{array}{c|ccccc}
\text{corner}&3&1&0&0&0\\
t&\tfrac32(1+d)&R(1+d)&(R+1)(1-d)&\tfrac13&\tfrac{4093}{30000}R^2.
\end{array}
\]
Let \(r_i=(r_{i0},\ldots,r_{i7})\) be the **raw** pairing row of atom \(i\), and form the \(4\times5\) matrix with rows \((r_{i1})_i,(r_{i2})_i,(r_{i3})_i,(r_{i5})_i\). For zero-based \(i=0,\ldots,4\), use the cofactor weights
\[
w_i=(-1)^{i+1}\det M_{\widehat i}.
\]
The symbolic exact replay verifies for **every real \(R\ge100\)** that all \(w_i>0\) and the aggregate \(C_j=\sum_iw_ir_{ij}\) obeys
\[
C_1=C_2=C_3=C_5=0,\quad C_0<0,\ C_4<0,\ C_6>0,\quad
C_7+\frac{R^2}{20}C_6<0.
\]
Any common numerator is itself Hurwitz by the positive-real segment homotopy, so its coefficients are positive. Its five actual pairings are strictly positive, giving
\[
0<C\cdot b<C_6\left(b_6-\frac{R^2}{20}b_7\right).
\]
This proves the bound for every possible common numerator, not merely a chosen ansatz. The five-atom vector has a positive \(b_6\) coordinate and is **not** an all-negative certificate.

## Explicit common numerator for every parameter

The following determinant formula constructs one. Let \(a_i^\partial\) be the four **boundary** corners and take the five corner/contact pairs
\[
(2,1),\quad(3,3/2),\quad(1,R),\quad(0,R+1),\quad(2,L).
\]
For each contact \(t_i\), define the tangent row
\[
T_{ij}=\begin{cases}
E_{a_i^\partial}'(t_i)(-t_i)^{j/2},&j\text{ even},\\
t_iO_{a_i^\partial}'(t_i)(-t_i)^{(j-1)/2},&j\text{ odd}.
\end{cases}
\]
Let \(A=(T_{ij})_{i=1}^5{}_{j=2}^6\), \(D=\det A\), set \(b_0^\partial=E_+(0)\), \(b_1^\partial=O_+(0)\), \(b_7^\partial=1\), and define \(h_i=-(T_{i0}b_0^\partial+T_{i1}b_1^\partial+T_{i7})\). For \(j=2,\ldots,6\), set
\[
b_j^\partial=\frac{\det A[j\leftarrow h]}{D}.
\]
The symbolic replay proves \(D>0\), all eight coefficients positive, and all five tangent identities exactly. It also checks that each boundary corner pairing factors into the square of its contact factor(s) times a strictly positive residual on \(t\ge0\). The contact factors are \((t-(R+1))^2\), \((t-R)^2\), \((t-1)^2(t-L)^2\), and \((t-3/2)^2\), in corner order 0–3.

For reproducibility, the residual positivity checks are explicit. If the quintic residual at corner 0 or 1 is \(p_0+\cdots+p_5t^5\), the replay proves \(p_0,p_1,p_2,p_3,p_5>0\) and \(4p_3p_5-p_4^2>0\). The corner-2 cubic has all coefficients positive. At corner 3, write its quintic as \(p_0+t h(t)\) and divide \(h\) twice at \(L\):
\[
h(t)=(t-L)^2(Q_0+Q_1t+Q_2t^2)+v(t-L)+h(L).
\]
The checker proves \(p_0,Q_0,Q_1,Q_2>0\) and \(4Q_0h(L)-v^2>0\), so completing the square proves \(h>0\) on \([0,\infty)\). All divisions and tangent identities are exact.

At any nonnegative \(t\), at least three of the four boundary pairings are strictly positive, since the five contact nodes are distinct; their midpoint pairing is therefore strictly positive, including at infinity. A radial corner pairing is \((1-\rho)\) times the midpoint pairing plus \(\rho\) times its boundary pairing. It is strictly positive for every \(\rho<1\), and minimizing affine pairings over the independent box proves the same numerator works for every member. This establishes nonvacuity for the **whole** unbounded-parameter family, not merely selected numerical examples.

## Exact all-parameter evidence

Every relevant width, lower endpoint, cofactor weight, aggregate sign, Cramer coefficient and residual-gap polynomial is a rational Laurent polynomial in \(R\). Multiply each by its lowest power of \(R\) to clear negative exponents, then substitute \(R=100+u\). The independent checker reconstructs **53** such polynomials from the displayed factors using recursive determinants and parity convolution, verifies four zero aggregate coordinates, five tangent identities and all contact divisions, and checks **all 1,194 shifted coefficients are strictly positive**. Thus every listed sign holds for all real \(R\ge100\), not just for sampled values. A corrupted-coefficient control was rejected.

Exact sign coefficients: `frontier-20261029-unbounded-b6-family-signs-frozen-v1.json`, SHA-256 `e595395eed59d1dd26d223b1997a2e42f57f41c47bdc5ca9e7e881b979071bb9`. Standalone independent Laurent/determinant/convolution replay `frontier-20261029-unbounded-b6-family-independent-kernel-v1.py`, SHA-256 `b28723339572887764ebc355b6739d88fcebd835bd4d1b78988ac0453542ad61`; receipt `frontier-20261029-unbounded-b6-family-independent-result-v1.json`, SHA-256 `e4ccf829558ef23b5081b2322f3c3da4215910c3e6605bd4f6d73f8766eb58c6`. Exact arithmetic used integers and `fractions.Fraction` in one Python Eval host. The residual positivity, root/argument, affine-minimum and homotopy deductions are written mathematics. No formal proof, cross-vendor review, novelty clearance, all-negative-coordinate atom certificate, or arbitrary-box verdict is claimed.
