# Candidate unrestricted mixed-geometry MSE asymptotic

Observed clock before creation: **2026-10-23T15:07:23-0700** (`/bin/date`). Owner `InfoResearch96h`, info-1. This addresses **the same** [frozen full-diamond privacy model](selection-v1.md), following [residual-unrestricted-optimum-v1.md](residual-unrestricted-optimum-v1.md); it is not a second problem. **CANDIDATE; author written argument only; no execution, finite replay, independent reconstruction, parent full reconstruction or formal verification for this packet. NOVELTY_UNCLEAR.**

The arbitrary-core Minkowski-shell mechanism is prior to Soria-Comas–Domingo-Ferrer 2013, as authenticated in [the mandatory provenance addendum](proof-diamond-staircase-counterexample-ADDENDUM-1-prior-mechanism.md). A Euclidean-disk core below is an instance of that known class in the asymptotic regime, not a new mechanism. The potentially substantive statement here is an **all-law lower bound and matching unrestricted leading optimum**, not the mechanism construction.

## 1. Exact claims

Let

\[
D=\{h\in\mathbb R^2:|h_1|+|h_2|\leq1\},\qquad b=e^{-\varepsilon}\in(0,1).
\]

Let \(\mathcal M_b\) be **all Borel probability measures** \(\mu\) on \(\mathbb R^2\) with

\[
\mu(E)\leq b^{-1}\mu(E+h)
\quad\text{for every Borel }E\text{ and every }h\in D.
\tag{1}
\]

Set

\[
J(\mu)=\int\|x\|_2^2\,d\mu(x),\qquad
V_b=\inf_{\mu\in\mathcal M_b}J(\mu).
\]

There is no assumed density, symmetry, radiality, regularity, independence or zero mean in this infimum.

**Theorem 1 (candidate all-law finite-b bound).** For every b in (0,1),

\[
V_b\geq L(b):=
2\sqrt{\frac b{3\pi}+\frac{b^2}{\pi^2}}-\frac{2b}{\pi}.
\tag{2}
\]

**Theorem 2 (candidate exact unrestricted leading asymptotic).**

\[
\lim_{b\downarrow0}\frac{V_b}{\sqrt b}
=\frac2{\sqrt{3\pi}},
\quad\text{equivalently}\quad
\lim_{\varepsilon\to\infty}e^{\varepsilon/2}V(\varepsilon)
=\frac2{\sqrt{3\pi}}.
\tag{3}
\]

The finite-b upper envelope in Section 5 is explicit and valid for every b in (0,1) and core radius r>0. These theorems do **not** identify an exact minimizer or exact finite-epsilon V, or claim that the disk-core family is globally optimal at finite b. They are separate candidates from the octagonal strict comparison and inherit none of its review verdicts.

## 2. From measure-level privacy to an essential cap and translated floor

Write \(\lambda\) for planar Lebesgue measure. We first derive absolute continuity directly from (1), rather than assuming it. For any Borel set N with \(\lambda(N)=0\), integrate (1) with E=N over h in D. Since \(|D|=2\),

\[
2\mu(N)\leq b^{-1}\int_D\mu(N+h)\,dh=0.
\tag{4}
\]

The final equality follows from Tonelli: for every fixed x, the h satisfying \(x\in N+h\) lie in \(x-N\), a Lebesgue-null set. Thus \(\mu\ll\lambda\). Choose a nonnegative Borel density p with integral one; it is finite a.e.

For each fixed h in D, applying (1) to all Borel E implies by comparison of densities

\[
p(x+h)\geq bp(x)\quad\text{for Lebesgue-a.e. }x.
\tag{5}
\]

The exceptional x set may depend on h. We do **not** assert that one version satisfies (5) for every h and every x. Instead apply Tonelli to the jointly measurable bad-pair set

\[
\{(x,h):h\in D,\ p(x+h)<bp(x)\}.
\]

Its x-section has measure zero for each h by (5). Consequently there is a full-Lebesgue-measure set H such that for every x in H,

\[
p(x+h)\geq bp(x)\quad\text{for a.e. }h\in D.
\tag{6}
\]

Discard also the null set where p is infinite. At such an x, with m=p(x), integration of (6) gives

\[
1\geq\int_{x+D}p(y)\,dy\geq2bm.
\tag{7}
\]

It follows that the **essential**, not pointwise, supremum obeys

\[
0<M:=\operatorname*{ess\,sup}p\leq\frac1{2b}<\infty.
\tag{8}
\]

Positivity follows from the unit integral. Intersect H with the full-measure set p<=M. By the definition of essential supremum, there is a sequence \(x_n\) in that intersection with \(m_n=p(x_n)\to M\). No attained maximum and no compactness of the sequence is required. For each n,

\[
p(y)\geq bm_n\mathbf1_{x_n+D}(y)\quad\text{for a.e. }y.
\tag{9}
\]

Thus the residual

\[
q_n(y)=p(y)-bm_n\mathbf1_{x_n+D}(y)
\tag{10}
\]

has the exact properties

\[
0\leq q_n\leq M\ \text{a.e.},\qquad
\int q_n=\alpha_n:=1-2bm_n\geq0.
\tag{11}
\]

The joint-measurability/Tonelli step is load-bearing: it produces an a.e. floor on a whole translated diamond from a good near-peak point despite h-dependent null sets.

## 3. Sharp quadratic moment bound under a density cap

For any measurable q with \(0\leq q\leq M\), total mass alpha>=0 and M>0,

\[
\int\|x\|_2^2q(x)\,dx\geq\frac{\alpha^2}{2\pi M}.
\tag{12}
\]

Here is a complete proof, including the sharp constant. If alpha=0 it is immediate. Otherwise set \(R^2=\alpha/(\pi M)\) and \(q_0=M\mathbf1_{B_R}\), where \(B_R\) is the Euclidean disk centered at zero. Pointwise a.e.,

\[
(\|x\|_2^2-R^2)(q(x)-q_0(x))\geq0:
\]

inside the disk both factors are nonpositive, and outside both are nonnegative. Since q and q0 have the same mass, integration gives

\[
\int\|x\|_2^2q\geq M\int_{B_R}\|x\|_2^2dx
=M\frac\pi2R^4=\frac{\alpha^2}{2\pi M}.
\]

If the left side is infinite, the inequality is trivial; otherwise the calculation is integrable. This is the elementary density-cap/bathtub bound, not claimed as a new general principle.

The diamond has

\[
|D|=2,\quad\int_Du\,du=0,\quad\int_D\|u\|_2^2du=\frac23.
\tag{13}
\]

For example \(\int_{u,v\geq0,u+v\leq1}u^2\,du\,dv=1/12\); the second coordinate and four quadrants give 2/3. Therefore for every x,

\[
\int_{x+D}\|y\|_2^2dy=\frac23+2\|x\|_2^2\geq\frac23.
\tag{14}
\]

No assumption that a near-peak point lies near the origin is needed.

## 4. Proof of the all-law lower bound

Fix any feasible mu. If J(mu) is infinite, (2) is automatic. Otherwise use the exact decomposition (10), the cap bound (12) with mass alpha_n, and (14):

\[
\begin{aligned}
J(\mu)
&=bm_n\int_{x_n+D}\|y\|_2^2dy+\int\|y\|_2^2q_n(y)dy\\
&\geq\frac23bm_n+\frac{(1-2bm_n)^2}{2\pi M}.
\end{aligned}
\tag{15}
\]

Let n tend to infinity. The discarded translation term is nonnegative for every n; its position need not converge. Because m_n tends to the finite positive M, (15) gives

\[
\begin{aligned}
J(\mu)
&\geq\frac23bM+\frac{(1-2bM)^2}{2\pi M}\\
&=\frac1{2\pi M}
+\left(\frac{2b}{3}+\frac{2b^2}{\pi}\right)M-\frac{2b}{\pi}.
\end{aligned}
\tag{16}
\]

Arithmetic–geometric mean for the first two positive terms implies

\[
J(\mu)\geq
2\sqrt{\frac1{2\pi}\left(\frac{2b}{3}+\frac{2b^2}{\pi}\right)}-\frac{2b}{\pi}
=L(b).
\tag{17}
\]

This holds for every feasible Borel law, not merely the known shell family, so taking the infimum proves Theorem 1. In particular

\[
\liminf_{b\downarrow0}\frac{V_b}{\sqrt b}
\geq\frac2{\sqrt{3\pi}}.
\tag{18}
\]

The bound does not assert finite-b equality; the residual-cap bound and translated floor need not be simultaneously attainable at finite b.

## 5. Explicit feasible disk-core upper envelope with all tails

For any r>0 let \(B_r=\{x:\|x\|_2\leq r\}\) and

\[
A_k=B_r+kD,\qquad
n_r(x)=\min\{k\in\mathbb Z_{\geq0}:x\in A_k\},\qquad
p^{\mathrm{disk}}_{r,b}(x)=Z_{r,b}^{-1}b^{n_r(x)}.
\tag{19}
\]

The compact sets are nested and exhaust the plane. If h in D then \(n_r(x+h)\leq n_r(x)+1\); applying -h gives the reverse inequality. Hence the same exact pointwise ratio argument as in (1) proves **all-shift** privacy once finite normalization is established below. Boundary conventions are closed sets; no generic-position exception is used.

Let G again be the auxiliary geometric variable with \(\Pr(G=k)=(1-b)b^k\). The identity

\[
b^{n_r(x)}=(1-b)\sum_{k\geq0}b^k\mathbf1_{A_k}(x)
\tag{20}
\]

and Tonelli give \(Z_{r,b}=\mathbb E|A_G|\) and the unnormalized quadratic moment \(N_{r,b}=\mathbb E M(A_G)\).

### 5.1 Exact normalization

For k>0, the parallel body kD+B_r consists of the diamond (area 2k²), four edge strips of total area \(4\sqrt2kr\), and four circular sectors whose angles total 2pi and whose total area is pi r². These pieces have disjoint interiors; this is the direct planar parallel-polygon decomposition. At k=0 it is just the radius-r disk, so the same formula holds:

\[
|A_k|=2k^2+4\sqrt2rk+\pi r^2.
\tag{21}
\]

Consequently the exact positive normalization is

\[
Z_{r,b}=\pi r^2+4\sqrt2rT_1+2T_2\geq\pi r^2>0,
\tag{22}
\]

where the entire geometric moments are

\[
T_1=\frac b{1-b},\quad T_2=\frac{b(1+b)}{(1-b)^2},\quad
T_3=\frac{b(1+4b+b^2)}{(1-b)^3},\quad
T_4=\frac{b(1+11b+11b^2+b^3)}{(1-b)^4}.
\tag{23}
\]

These identities follow by differentiating the geometric series; in particular they include all infinitely many shells.

### 5.2 Complete finite-b moment upper bound

At k=0, \(M(A_0)=\pi r^4/2\). For k>=1 use \(B_r\subseteq\sqrt2rD\), which follows from \(\|x\|_1\leq\sqrt2\|x\|_2\). Thus

\[
A_k\subseteq(k+\sqrt2r)D,\qquad
M(A_k)\leq\frac23(k+\sqrt2r)^4.
\tag{24}
\]

This inclusion, not an assumed homothetic shape, is all that is needed. Expanding the fourth power, and using \(\Pr(G\geq1)=b\), gives the finite bound

\[
\begin{aligned}
N_{r,b}\leq&(1-b)\frac\pi2r^4\\
&+\frac23\left(T_4+4\sqrt2rT_3+12r^2T_2+8\sqrt2r^3T_1+4r^4b\right).
\end{aligned}
\tag{25}
\]

All expressions are finite, proving that (19) is a genuine normalized feasible density with finite MSE. Combining (22) and (25), and using 1-b<=1, yields the explicit all-b, all-r envelope

\[
\begin{aligned}
J(p^{\mathrm{disk}}_{r,b})\leq U(b,r):=
\frac{r^2}{2}
+\frac2{3\pi r^2}
\left(T_4+4\sqrt2rT_3+12r^2T_2+8\sqrt2r^3T_1+4r^4b\right).
\end{aligned}
\tag{26}
\]

No tail truncation or unbounded remainder is hidden in this upper bound.

## 6. Matching the exact leading unrestricted optimum

Choose

\[
c=\left(\frac4{3\pi}\right)^{1/4},\qquad r=c\,b^{1/4}.
\tag{27}
\]

Each \(T_j/b\) in (23) tends to one as b tends to zero. Divide (26) by sqrt(b). Its r² term tends to c²/2. Its T4 term tends to \(2/(3\pi c^2)\). The other four terms vanish: after division they are respectively constants times

\[
(T_3/b)b^{1/4},\quad
(T_2/b)b^{1/2},\quad
(T_1/b)b^{3/4},\quad b.
\tag{28}
\]

Thus

\[
\limsup_{b\downarrow0}\frac{V_b}{\sqrt b}
\leq\limsup_{b\downarrow0}\frac{J(p^{\mathrm{disk}}_{r,b})}{\sqrt b}
\leq\frac{c^2}{2}+\frac2{3\pi c^2}
=\frac2{\sqrt{3\pi}}.
\tag{29}
\]

The matching liminf (18) proves Theorem 2. Equations (2) and (26) are explicit finite-b envelopes underlying the squeeze, not fitted asymptotic data.

For sufficiently small b, the disk core is coordinate-downward and lies inside D because \(\sqrt2r<1\). Hence this upper law is in the authenticated SCDF2013 construction class. Our independent privacy proof works for every r>0 regardless of that source's core-inside-sensitivity hypothesis; it does not import their optimality assertion.

## 7. Relation to the original staircase comparison, without extra counting

As a dependent observation only, the same exact gamma-family formula from the comparison manuscript implies

\[
\lim_{b\downarrow0}\frac{\min_{0\leq\gamma\leq1}C_\gamma(b)}{\sqrt b}=\frac23.
\tag{30}
\]

The lower bound is \(C_\gamma\geq\tfrac23(\sqrt b-b/(1-b)^2)\), uniformly in gamma. For the matching upper choose the allowed parameter \(\gamma=b^{1/4}\) in

\[
C_\gamma=\frac13
\frac{\gamma^4+4\gamma^3T_1+6\gamma^2T_2+4\gamma T_3+T_4}
 {\gamma^2+2\gamma T_1+T_2};
\]

its numerator is \(2b+o(b)\), denominator \(\sqrt b+o(\sqrt b)\). Combining (3) and (30) gives a limiting diamond-family/global-optimum ratio \(\sqrt{\pi/3}>1\). This is a corollary of the named bounds, not a separately counted discovery or a substitute for the earlier explicit finite-parameter counterexample.

## 8. Reconstruction and prior-art obligations

The new lower-bound engine requires independent checking of the null-set integration (4), density/Radon–Nikodym step (5), joint bad-pair Tonelli step (6), essential-peak sequence with no attained/near-origin assumption, exact residual mass/cap, and the sharp constant in (12). The upper bound requires every parallel-body area piece, all coefficients/tail factors in (25), and the powers in (28). In particular, neither center symmetry nor mean-zero is used in the all-law lower bound.

The known mechanism, the elementary density-cap moment principle, and standard measure-theoretic tools are not claimed as inventions. The precise mixed-model lower bound and sharp leading optimum may themselves have prior history; the current bounded source audit did not certify their novelty. This candidate needs a fresh source-interface audit and separate actual peer/parent reconstruction. The octagonal packet's 0F/0M/0m return does **not** verify this proof. No computational or formal check was run.
