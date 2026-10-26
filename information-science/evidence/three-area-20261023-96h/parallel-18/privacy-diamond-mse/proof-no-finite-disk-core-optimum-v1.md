# Candidate finite-epsilon obstruction: every positive-radius disk core can be improved

Observed clock before creation: **2026-10-23T15:38:27-0700**. Same info-1 owner and [finite-epsilon selection](selection-v2-finite-epsilon.md). **CANDIDATE; complete author written derivation only; no inherited verdict, scientific program, sampling, solver or formal verification. NOVELTY_UNCLEAR.** The mechanism class is prior; this packet claims only the exact structural comparison below.

## 1. Exact statement and consequence for the active target

Fix **arbitrary** \(0<b<1\) and \(r>0\). Let

\[
D=\{x:|x_1|+|x_2|\leq1\},\qquad B_r=\{x:\|x\|_2\leq r\}.
\]

For any compact origin-containing core S with positive area, define

\[
n_S(x)=\min\{k\in\mathbb Z_{\geq0}:x\in S+kD\},\quad
Z_S=\int b^{n_S(x)}dx,\quad
p_S(x)=Z_S^{-1}b^{n_S(x)}.
\tag{1}
\]

The cost is the full squared-Euclidean moment \(J(p_S)\). The disk-core law is \(p_{B_r}\), the known family supplying the checked sharp leading weak-privacy constant. Its finite-b optimality was not previously established.

**Theorem (candidate).** For every finite b,r above, the explicit core \(S_\tau\) constructed in Sections2–3 is compact, convex, origin-containing, invariant under signed coordinate permutations and has

\[
|S_\tau|=\pi r^2,\quad
\max_{S_\tau}(|x_1|+|x_2|)=\sqrt2r.
\tag{2}
\]

Its complete law (1) satisfies the **full continuous-diamond privacy condition**

\[
\mu(E)\leq b^{-1}\mu(E+h)
\quad\text{for every Borel }E\text{ and every }h\in D,
\tag{3}
\]

and has the **same exact normalization** as the radius-r disk-core law, but strictly smaller cost:

\[
J(p_{S_\tau})
\leq J(p_{B_r})-
\frac{36\,m r w\tau}{35Z}
<J(p_{B_r}),
\quad m=\frac b{1-b}>0.
\tag{4}
\]

All parameters \(w,\tau,Z\) are explicit below. Thus **no positive-radius disk-core law is a finite-b minimizer of the unrestricted V**, for any finite epsilon>0 and any chosen radius. This is an exact obstruction to that ansatz, not an exact formula for V, not a restriction of the all-law target to symmetric/convex laws, and not a claim that the infimum over disk radii has a positive gap without a separate attainment argument. The degenerate zero-radius core is not included in this theorem.

## 2. A fully specified two-band perturbation

Put

\[
a=\frac r{\sqrt2},\qquad w=\frac a{16},\qquad
u_1=\frac a4,\qquad \nu_2=\frac{3a}4,
\qquad F(y)=\sqrt{r^2-y^2}\quad(0\leq y\leq a).
\tag{5}
\]

Define the C² bump

\[
\phi(s)=
\begin{cases}
(1-(s/w)^2)^3,&|s|\leq w,\\
0,&|s|>w,
\end{cases}
\quad
\psi(y)=\phi(y-\nu_2)-\phi(y-\nu_1).
\tag{6}
\]

The two supports are respectively

\[
[3a/16,5a/16],\qquad [11a/16,13a/16],
\tag{7}
\]

strictly inside (0,a) and disjoint. Choose the **explicit positive amplitude**

\[
\tau=\min\left\{\frac r{2^{18}},\frac{3mr}{128(m+r)}\right\}>0,
\qquad F_\tau(y)=F(y)+\tau\psi(y).
\tag{8}
\]

No numerical sign search, unknown optimizer or unspecified sufficiently-small constant appears in this choice.

Identical translated bumps and disjoint supports give exactly

\[
\int_0^a\psi(y)dy=0,\qquad
\int_0^a\psi(y)^3dy=0.
\tag{9}
\]

The first identity preserves area, and the second will cancel the **entire cubic perturbation term**, not merely a first variation. The signs of the bumps move boundary outwards nearer the diagonal and inwards nearer the coordinate axis.

## 3. Convexity and geometry of the actual competitor

### 3.1 Uniform C² control, valid for all b,r

On its support,

\[
\phi''(s)=w^{-2}\left[-6+36(s/w)^2-30(s/w)^4\right].
\]

At each support endpoint \(\phi,\phi',\phi''\) vanish, so the extension in (6) is C². The crude bounds

\[
\|\phi''\|_\infty\leq72/w^2,\qquad
\|\psi''\|_\infty\leq144/w^2
\tag{10}
\]

suffice. Since \(w^2=r^2/512\), (8) gives

\[
\tau\|\psi''\|_\infty
\leq\frac9{32r}.
\]

Also \(F''(y)=-r^2/(r^2-y^2)^{3/2}\leq-1/r\). Consequently

\[
F_\tau''(y)\leq-\frac{23}{32r}<0.
\tag{11}
\]

The perturbation vanishes near 0 and a, so

\[
F_\tau(0)=r,\quad F_\tau'(0)=0,\quad
F_\tau(a)=a,\quad F_\tau'(a)=-1.
\tag{12}
\]

It follows that \(F_\tau\) is strictly decreasing on (0,a], with derivative between -1 and 0. Its endpoint tangent and concavity imply

\[
a\leq F_\tau(y)\leq2a-y\quad(0\leq y\leq a).
\tag{13}
\]

### 3.2 Explicit core, not just a signed boundary variation

Take the first-octant region

\[
R_\tau=\{(x,y):0\leq y\leq a,\ y\leq x\leq F_\tau(y)\}.
\]

Let \(S_\tau\) be the union of its eight signed-coordinate/permutation images. This is an explicitly defined compact set. Here is a direct convexity check.

The inverse of \(F_\tau:[0,a]\to[a,r]\) exists and is decreasing. Define the full positive-quadrant right boundary

\[
q(y)=\begin{cases}
F_\tau(y),&0\leq y\leq a,\\
F_\tau^{-1}(y),&a\leq y\leq r.
\end{cases}
\tag{14}
\]

Both pieces are concave: on the inverse piece,

\[
(F_\tau^{-1})''=-\frac{F_\tau''\circ F_\tau^{-1}}
 {(F_\tau'\circ F_\tau^{-1})^3}<0
\]

away from the endpoint. At y=a the two derivatives both equal -1. Thus q is concave and decreasing on [0,r], continuous at the endpoints, with q'(0)=0. Its even extension q(|y|) is concave on [-r,r]. Therefore

\[
S_\tau=\{(x,y):|y|\leq r,\ |x|\leq q(|y|)\}
\]

is convex, as the intersection of the two hypographs \(x\leq q(|y|)\), \(-x\leq q(|y|)\) and the vertical strip. It is the same eight-octant set by construction. At tau=0 it is exactly the Euclidean disk B_r.

By (13), its l1 support is at most2a and is attained at (a,a). Its coordinate extrema remain r. Its area is

\[
|S_\tau|=8\int_0^a(F_\tau(y)-y)dy
=|B_r|+8\tau\int_0^a\psi=\pi r^2.
\tag{15}
\]

It contains the square [-a,a]² and hence the origin in its interior. These facts prove (2) and ensure an actual positive-area core.

## 4. Exact Minkowski profile for every shell

For every k>=0, the first-octant part of \(A_k^\tau=S_\tau+kD\) is exactly the union

\[
\begin{cases}
0\leq y\leq a,&y\leq x\leq k+F_\tau(y),\\
a\leq y\leq a+k/2,&y\leq x\leq k+2a-y.
\end{cases}
\tag{16}
\]

To justify the whole profile: the first-octant curved boundary of the core has outward normals ranging continuously from the positive x-axis to (1,1), since its slopes range from0 to-1. For any such normal with first coordinate strictly larger than the second, the maximizing point of D is (1,0). Support maximizers under a Minkowski sum add, so that whole boundary arc is translated by (k,0). At the diagonal normal, the core maximizer is (a,a), while D's maximizing face is the edge joining (1,0) to (0,1). Their sum is exactly the segment from (a+k,a) to (a,a+k). Its first-octant half has equation x+y=k+2a and endpoint y=a+k/2. Symmetry supplies all other arcs. Convexity and the origin then fill precisely the regions in (16); there is no unlisted facet or clipping transition. For k=0 the second region has zero area.

Integration of (16) gives

\[
\begin{aligned}
|A_k^\tau|
&=8\int_0^a[k+F_\tau(y)-y]dy
+8\int_a^{a+k/2}[k+2a-2y]dy\\
&=\pi r^2+8ak+2k^2.
\end{aligned}
\tag{17}
\]

This is **independent of tau for every integer k**, not just to first order. The same formula is the checked disk parallel-body area because 8a=4sqrt2 r.

## 5. Full-shift privacy, exact equal normalization and finite moments

For every h in D and every x, Minkowski inclusion gives

\[
n_{S_\tau}(x+h)\leq n_{S_\tau}(x)+1.
\]

Using -h gives the reverse bound, so the index difference has absolute value at most1, including every boundary point. The normalized density therefore has the pointwise ratio bound and, after integration, exactly (3).

The sets are compact, nested and exhaustive because the core contains0. The integer index is finite and Borel. As usual,

\[
b^{n_{S_\tau}(x)}=(1-b)\sum_{k\geq0}b^k\mathbf1_{A_k^\tau}(x).
\tag{18}
\]

Let G be only the summation variable with probability (1-b)b^k and put

\[
m=\mathbb EG=\frac b{1-b},\qquad
T_2=\mathbb EG^2=\frac{b(1+b)}{(1-b)^2}.
\]

Tonelli and (17) give the **same exact** positive finite normalizer for both the perturbed and disk law:

\[
Z=Z_{S_\tau}=Z_{B_r}
=\pi r^2+8am+2T_2
=\pi r^2+4\sqrt2rm+2T_2>0.
\tag{19}
\]

Since \(S_\tau\subseteq2aD\), every expanded set lies in (k+2a)D. Its quadratic moment is bounded by \(\tfrac23(k+2a)^4\). Thus all geometric moment sums are finite. Both densities in (4) are actual feasible probability laws with finite MSE, and all infinite-tail operations below are justified. The use of a symmetric competitor does not assume symmetry of any all-law optimizer.

## 6. Exact full-tail moment change, not a linearized guess

Only the curved-cap portion in (16) changes with tau; a and the diagonal triangle stay fixed. Write \(M(A)=\int_A(x^2+y^2)dxdy\). The exact difference is

\[
\begin{aligned}
M(A_k^\tau)-M(A_k^0)
=8\int_0^a\left[
\frac{(k+F_\tau)^3-(k+F)^3}{3}
+y^2(F_\tau-F)\right]dy.
\end{aligned}
\tag{20}
\]

This formula permits positive or negative boundary motion: it is the difference of two genuine cap integrals, both with the fixed lower boundary x=y. Expanding the cubic gives

\[
\begin{aligned}
\Delta M_k={}&8\tau\int_0^a[(k+F)^2+y^2]\psi\,dy\\
&+8\tau^2\int_0^a(k+F)\psi^2dy
+\frac83\tau^3\int_0^a\psi^3dy.
\end{aligned}
\tag{21}
\]

Define

\[
A=\int_0^a F\psi\,dy,\quad P_2=\int_0^a\psi^2dy,\quad
B_0=\int_0^aF\psi^2dy,\quad B=mP_2+B_0>0.
\tag{22}
\]

Because F²+y²=r² and both identities (9) hold, (21) reduces **exactly** to

\[
\Delta M_k=16kA\tau+8\tau^2(kP_2+B_0).
\tag{23}
\]

The cubic term is zero identically; there is no unbounded remainder or fourth-order term. Summing all geometric tails yields for the unnormalized moments N,

\[
N_\tau-N_0=16mA\tau+8B\tau^2.
\tag{24}
\]

The strict negative effect will come from the tail term m>0. At k=0 the first variation vanishes, consistently with the disk's area-constrained central-moment optimality.

## 7. Explicit sign margins and amplitude control

By translation of the two bumps,

\[
-A=\int_{-w}^{w}\phi(s)
\big[F(\nu_1+s)-F(\nu_2+s)\big]ds>0.
\tag{25}
\]

An explicit lower bound avoids relying only on that sign. Throughout the support, the left argument is at most5a/16 and the right argument is at least11a/16. Since F is decreasing,

\[
F(\nu_1+s)-F(\nu_2+s)
\geq\frac{(11a/16)^2-(5a/16)^2}{2r}
=\frac{3r}{32}.
\tag{26}
\]

The denominator2r is an upper bound for the sum of the two square roots in the identity for their difference. Also

\[
\int_{-w}^{w}\phi(s)ds
=w\int_{-1}^{1}(1-u^2)^3du=\frac{32w}{35}.
\]

Thus

\[
|A|\geq\frac{3rw}{35}.
\tag{27}
\]

Since 0<=phi<=1, disjoint supports give \(\psi^2\leq\phi(y-\nu_1)+\phi(y-\nu_2)\). Hence

\[
B\leq(m+r)\int\psi^2
\leq\frac{64(m+r)w}{35}.
\tag{28}
\]

The explicit second amplitude bound in (8) implies

\[
B\tau\leq\frac{3mrw}{70}\leq\frac12m|A|.
\tag{29}
\]

Therefore the **exact** change (24) obeys

\[
N_\tau-N_0
=-16m|A|\tau+8B\tau^2
\leq-12m|A|\tau
\leq-\frac{36mrw\tau}{35}<0.
\tag{30}
\]

Division by the identical exact normalizer (19) proves (4). Every inequality is uniform in the arbitrary finite parameters b and r. No gamma value, epsilon threshold, numerical integration or parameter sampling has been used.

## 8. What this obstruction does and does not resolve

The checked asymptotic upper used a Euclidean disk because it attains the density-cap leading constant. This packet shows why that leading construction cannot simply be promoted to an exact finite-epsilon optimum: a noncircular angular redistribution leaves every normalization shell area unchanged but reduces the complete tail moment enough to overcome the positive second-order core cost. It gives a genuinely admissible strict improvement for every disk radius and every finite epsilon.

For r<=1/sqrt2, the perturbed core is coordinate-downward and lies in D, so it is inside the authenticated SCDF2013 core/shell construction class. For larger r, feasibility is supplied by the independent all-shift argument above, not by extending that source's stated core-inside-sensitivity premise. No new general mechanism is claimed in either regime.

**Literal finite-V residual:** no matching all-law dual certificate or globally optimal finite-epsilon law has been supplied. It is not proved that an unrestricted minimizer can be reduced to one convex core with minimal Minkowski tails. Even if that reduction held, the optimal noncircular core remains to be characterized. This theorem only excludes positive-radius disk-core laws and strictly improves their actual costs. It does not by itself prove a positive gap from an unattained infimum over all disk radii or handle the zero-radius limiting core.

The new argument has not yet received its own actual peer or parent reconstruction. Prior octagonal and all-law-asymptotic verdicts do not verify its boundary/gluing, every-k profile, bump constants or exact cost cancellation. Its source-priority status remains **NOVELTY_UNCLEAR**; standard convexity, bump and density tools are not separately counted discoveries. No scientific execution or formal verification was performed.
