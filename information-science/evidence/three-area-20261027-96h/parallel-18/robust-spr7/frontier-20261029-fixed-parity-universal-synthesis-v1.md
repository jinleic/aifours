# Constructive common SPR synthesis for any compact stable one-parity family

**Status: WRITTEN theorem candidate, with a separately WRITTEN-checked-in-kernel full-width example; not parent adoption.** This is an all-degree constructive positive theorem for a substantially restricted denominator family and gives an explicit full-width continuation. It is **not** a universal theorem for arbitrary seven-width boxes.

## The theorem

Let \(K\) be any nonempty **compact**, not necessarily convex or rectangular, family of monic strictly Hurwitz real polynomials of the same degree \(n\ge1\). Write
\[
a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t),\qquad t\ge0.
\]
Choose any reference \(a_*\in K\).

* If **all even parts are identical**, put \(E_b=E_*\), \(O_b=\varepsilon O_*\).
* If **all odd parts are identical**, put \(E_b=\varepsilon E_*\), \(O_b=O_*\).

For all sufficiently small \(\varepsilon>0\), the resulting real polynomial \(b\) has exact degree \(n\), positive leading coefficient and
\[
E_a(t)E_b(t)+tO_a(t)O_b(t)>0\quad (a\in K,\ 0\le t<\infty),
\]
with strictly positive normalized limit at infinity. A positive normalization makes \(b\) monic. Thus \(b/a\) is strictly positive real for every \(a\in K\). In each case \(b\) is obtained from a **single actual reference polynomial** by scaling just one parity; no numerator search over a higher-dimensional space is required.

### Proof

For any stable monic polynomial its unwrapped positive-frequency phase increases strictly from 0 to \(n\pi/2\). Therefore every positive zero of its even or odd part is simple; the two kinds alternate, and the sign of the opposite part at the \(j\)-th zero is determined by \(j\) and the parity, independently of the chosen stable polynomial. These are the standard phase/interlacing facts, following by summing the strictly positive derivatives of the phases of its left-half-plane linear factors.

In the fixed-even case, the unscaled pairing is
\[
P_{a,b}=E_*^2+\varepsilon t O_*O_a.
\]
The first term is nonnegative. At every positive zero of the common \(E_*\), \(O_*O_a>0\) for all \(a\in K\). At \(t=0\), \(E_*^2>0\). If \(n\) is odd, the normalized first term vanishes at infinity while the normalized second term has positive limit; if \(n\) is even, the normalized first term already has positive limit.

In the fixed-odd case,
\[
P_{a,b}=tO_*^2+\varepsilon E_*E_a.
\]
At every positive zero of \(O_*\), \(E_*E_a>0\) for all \(a\in K\), and at \(t=0\) the second term is strictly positive. If \(n\) is even, the normalized first term vanishes at infinity while the normalized second term has positive limit; if \(n\) is odd, the first term has positive limit.

In either case compactify by \(x=t/(1+t)\), dividing both terms by \((1+t)^n\). The first term is a continuous nonnegative function on \([0,1]\), with a finite zero set independent of \(a\). At each zero the second term is strictly positive for every \(a\in K\); compactness of \(K\) makes this positivity uniform and extends it to a neighborhood of the zero set. On the complementary compact set the first term has a positive minimum, while the second is uniformly bounded. Hence one sufficiently small \(\varepsilon>0\) makes the whole pairing uniformly strictly positive. The leading coefficient is either the reference leading coefficient or its positive \(\varepsilon\)-multiple, so exact degree and monic normalization follow.

## Effective rational algorithm and full-width neighborhood

For a rational coefficient box with one parity fixed, choose a rational reference \(a_*\). Try \(\varepsilon=1/N\) for \(N=1,2,\ldots\); test the two actual extremal choices of the variable parity by exact rational Sturm chains, requiring positive constant and leading coefficients and no positive root of each pairing polynomial. At each \(t\) the pairing is affine in the variable coefficients and these two parity corners give its minimum and maximum. The theorem proves this simple exact search **terminates**; it needs only the standard Sturm root-count theorem. The positive solution's compactified pairing polynomials admit positive rational Bernstein coefficients after finitely many dyadic subdivisions, yielding a certified rational uniform lower bound \(\gamma>0\).

This also supplies genuine **full-width** boxes. Let \(S=\sum_{j=0}^{n}|b_j|\). If every nonleading denominator coefficient is expanded by at most \(\delta\), then
\[
\frac{|P_{a',b}(t)-P_{a,b}(t)|}{(1+t)^n}\le n\delta S.
\]
Indeed \(|b(i\sqrt t)|\le S(1+t)^{n/2}\) and \(|(i\sqrt t)^j|\le(1+t)^{n/2}\) for \(j\le n\). Choose, for example, rational \(0<\delta<\gamma/(2nS)\). The same \(b\) works throughout the expanded box. Each segment from a member of the original box to a coefficient-clipped expanded member retains the strict pairing, so it has no imaginary-axis root, including zero; homotopy from the original Hurwitz member proves the expanded member Hurwitz. Thus every such one-parity box has an explicitly computable full-dimensional stable neighborhood with the same common numerator.

## Explicit full-width box where the midpoint fails

For \(n=7\), take ascending center and seven independent radii
\[
\begin{aligned}
m&=(6,36,16,49,17/2,14,1,1),\\
r&=(1/1000,10^{-8},1/1000,10^{-8},37/500,10^{-8},1/5).
\end{aligned}
\]
The degree-seven coefficient stays 1. All seven radii are positive. The displayed reference has odd part
\(O_*(t)=-(t-1)(t-4)(t-9)\). The monic parity-scaled numerator with \(\varepsilon=1/16\) is
\[
b=(3/8,36,1,49,17/32,14,1/16,1).
\]
The independent exact checker verifies all four parity-corner pairings have positive constant and leading terms and zero positive roots: each degree-seven Sturm chain has sign variations \((3,3)\) at \(0,+\infty\). Affinity therefore proves the same \(b\) works on the **whole** full-width box.

This is not merely using the midpoint: the actual member
\[
a=(5999/1000,36,16001/1000,49,4213/500,14,6/5,1)
\]
has, at \(t=41/10\), midpoint pairing
\[
P_{a,m}(41/10)=-7639163/50000000<0.
\]
Thus \(m\) itself fails while the parity-scaled reference succeeds.

For all-member stability, the checker verifies the six ordered signs \((-+),(--),(+-),(++),(-+),(--)\) simultaneously for each actual corner at squared frequencies
\(4/5,6/5,3999/1000,4001/1000,89/10,10\). Since each parity evaluation on the coefficient box lies between its corresponding two parity extrema, these signs hold for every member. Each parity cubic has three disjoint sign changes and no further positive roots; the even and odd root brackets are disjoint. Consequently no member has an imaginary-axis root. The checker also verifies all 28 positive corner Hurwitz minors; a segment from a reference corner through the box stays monic and avoids the imaginary axis, so every member is Hurwitz. This all-member conclusion does not rely solely on an unproved corner inference.

Exact frozen inputs `frontier-20261029-one-parity-synthesis-full-width-frozen-v1.json`, SHA-256 `c5dccada6b60d4f070be291b7209e3ead2acd316def14280808787ee91daa849`; standalone monomial/Sturm/marker/Hurwitz replay `frontier-20261029-one-parity-synthesis-full-width-independent-kernel-v1.py`, SHA-256 `0083b7a182312815d1fd6f4529f492cb3c92131291475b230bbe0809a9695cf5`; receipt `frontier-20261029-one-parity-synthesis-full-width-independent-result-v1.json`, SHA-256 `e62f5212d7a1036874da893095b47160c8de5208d2d647a6b01b33de921006c6`. The checker rejected zero-numerator-constant and over-wide-odd-radius controls.

All finite calculations use exact integers/`fractions.Fraction` on one Python Eval host. The phase, compactness, Sturm and homotopy arguments are written mathematics; no formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
