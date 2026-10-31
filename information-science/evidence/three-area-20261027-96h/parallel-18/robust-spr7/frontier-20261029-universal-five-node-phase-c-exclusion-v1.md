# No direct five-node phase-C certificate for any eligible septic box

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:51:00 PDT 2026**. **WRITTEN theorem candidate**, importing a WRITTEN-checked-in-kernel integer certificate for its first-gap part. No parent adoption, independent scientific review, formal proof or novelty clearance is claimed.

## Result

For every compact independent coefficient box of monic Hurwitz septics, a positive-weight aggregate of actual frequency/denominator pairing atoms cannot have all eight numerator-monomial coordinates strictly negative if its five distinct positive squared frequencies have the direct phase word **C = (2,4,3,5,4)**. This remains true with additional zero or compactified-infinity atoms.

The exact direct phase classification and eight odd-moment rays are imported from `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`. The other classified phase words **A** and **B** retain their previously stated mixed-band residuals; this result does not establish the requested universal five-node exclusion, exclude six-node certificates, or settle the original common-numerator problem.

Write the odd root bands as \([a,b],[c,d],[e,f]\). The phase-C signs and interlacing force
\[
a<t_1<c,\quad c<t_2<t_3<d,\quad d<t_4<t_5<e. \tag{1}
\]
At \(t_1=a\) an actual odd evaluation cannot be negative; at \(t_1=c\) an actual even evaluation cannot be negative. The necessary strict signs likewise preclude \(t_2=c\), \(t_3=d\), \(t_4=d\), and \(t_5=e\). The case \(b<t_1<c\) is the named gap theorem `frontier-20261029-universal-phase-c-first-gap-exclusion-v1.md`, SHA-256 `76ad6dcf6cb8a22ddd6ca0bf88a61280540678893e6aa4a8f04069650801e1b6`. It remains to prove \(a<t_1\le b\), including the boundary.

## 1. Drop the first pairing, not the positive tail

Use the same even test numerator
\[
F(t)=(-t)(b-t)(e-t). \tag{2}
\]
For \(a<t_1<b\), both \(F(t_1)\) and every actual \(E(t_1)\) are negative, so the first even pairing is positive; at \(t_1=b\), it is zero. At the later four nodes \(F>0\), so replacing actual even evaluations by the lower envelope \(E_-\) only lowers their contributions. Zero and infinity atoms contribute zero to this even test.

The odd sign word is \((- ,+,-,+,+)\). By the named ray reduction, it suffices to establish strictly positive **tail** pairing for each of the eight four-node rays with support
\((u_1,u_2,u_3,u_4)=(t_1,t_2,t_3,t_4)\) or \((t_1,t_2,t_3,t_5)\). Their physical weights are
\[
w_i^{(k)}=\frac{e_{3-k}(\widehat u_i)}{u_iO_i(u_i)H'(u_i)}>0,
\qquad H(t)=\prod_{j=1}^4(t-u_j). \tag{3}
\]
Normalize \(E_-\) by its positive leading even coefficient; its root vector is a convex combination of
\[
E_{x,y,z}(t)=(x-t)(y-t)(z-t),\quad
x\in\{0,a\},\ y\in\{b,c\},\ z\in\{d,e\}. \tag{4}
\]
At \(u_2,u_3\), every such even vertex is positive. If \(z=e\), it is also positive at \(u_4\), so its tail is immediately positive. If \(z=d\), it is negative at \(u_4\), and the worst odd endpoint choices are \(O_+,O_-,O_-\) at nodes 2,3,4 respectively. Actual reciprocal odd magnitudes cannot make this lower, including as the inside-band odd values approach zero. The first odd value is irrelevant to the unnormalized tail and need only be negative for the ray sign pattern.

It suffices to prove positivity for \(k=3\), where \(e_0=1\). Indeed the three tail terms have signs \((+,+,-)\), and the multipliers \(e_m(\widehat u_i)\), \(m=3-k\), are nonincreasing in \(i\). If their unweighted sum is positive, every such reweighted sum is positive as well.

## 2. A monotone odd-box inequality

Abbreviate \((A,B,C,D)=(u_1,u_2,u_3,u_4)\). Let
\[
\Delta(t)=O_+(t)-O_-(t)=\delta_0+\delta_1t+\delta_2t^2,\qquad \delta_j\ge0, \tag{5}
\]
which is nondecreasing on positive \(t\) because the odd coefficient intervals are independent. For \(a<A<b\), \(O_-(A)<0<O_+(A)\), hence
\[
\frac{\Delta(B)}{f-B}>\frac{\Delta(A)}{f-A}>
(b-A)(c-A). \tag{6}
\]
For \(A=b\), \(\Delta(A)>0\) and the first quotient in (6) remains positive; the right side is zero.

For a vertex \(z=d\), write \(g_\pm(t)=E_{x,y,d}(t)F(t)/(tO_\pm(t))\), and let \(J_3(g_-)=\sum_i g_-(u_i)/H'(u_i)\). The worst-endpoint tail is
\[
T=J_3(g_-)-\frac{g_-(A)}{H'(A)}
  +\frac{g_+(B)-g_-(B)}{H'(B)}. \tag{7}
\]
First take \(x=a\), and set
\[
D_y=\frac{B-y}{B-c}\,\frac{\Delta(B)}{f-B},\qquad y\in\{b,c\}. \tag{8}
\]
Then \(g_-(t)=-(t-b)(t-y)\), \(J_3(g_-)=0\), and \(g_+(B)-g_-(B)=D_y\). Equation (6) implies
\[
D_y>(b-A)(y-A)=:w\ge0. \tag{9}
\]
Since \(H'(B)=(B-A)(C-B)(D-B)\) is positive and smaller than \(|H'(A)|=(B-A)(C-A)(D-A)\), (7) is strictly positive.

## 3. The opposite first-root endpoint

For \(x=0\), both formal baseline and correction in the preceding case acquire the positive factor \(t/(t-a)\). Polynomial division gives
\[
J_3(g_-)=\frac{a(b-a)(y-a)}{(A-a)(B-a)(C-a)(D-a)}>0. \tag{10}
\]
Using (9) in (7), with \(G(t)=1/[(C-t)(D-t)]\), gives the strict lower bound
\[
T>J_3(g_-)+\frac{w}{B-A}
 \left[\frac{B}{B-a}G(B)-\frac{A}{A-a}G(A)\right]. \tag{11}
\]
The bracket divided by \(B-A\) exceeds \(-aG(A)/[(A-a)(B-a)]\), because \(G(B)>G(A)\). Thus
\[
T>\frac{a}{(A-a)(B-a)}\left[
\frac{(b-a)(y-a)}{(C-a)(D-a)}
-\frac{(b-A)(y-A)}{(C-A)(D-A)}\right]>0. \tag{12}
\]
The final bracket is positive termwise: for \(C>b\) and \(D>y\),
\[
\frac{b-a}{C-a}>\frac{b-A}{C-A},\qquad
\frac{y-a}{D-a}>\frac{y-A}{D-A}. \tag{13}
\]
This also covers \(A=b\), where \(w=0\). We have proved all even vertices and all odd rays have positive tail pairing. Convex interpolation, positive combinations of rays, and the nonnegative first/endpoint contributions contradict an all-negative even-coordinate aggregate.

## 4. Nonvacuity, imported computation and limits

An actual full-width stable box with first node in the odd band and phase signs \((--),(++),(+-),(-+),(++)\), together with all 64 exact tail-vertex/ray values, is frozen in `frontier-20261029-first-band-phase-c-tail-example-frozen-v1.json`, SHA-256 `95115bd35b160547572e52a2a01f0f3a09b11f0f622cd7b1c808aadcc70f0972`. Its finite checks used exact Python `fractions.Fraction`/integers in one Eval host.

Sections 1–3 are written mathematics. The imported first-gap theorem additionally uses eight exact integer expansions with 225,019 positive coefficients, checked in the same host and described in its linked receipt. The global phase classification, odd-ray decomposition and interlacing are named author-written imports. None is an independent review, Lean/kernel proof or novelty clearance. Original arbitrary-box synthesis-or-no-go and five-node phases A/B remain open. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
