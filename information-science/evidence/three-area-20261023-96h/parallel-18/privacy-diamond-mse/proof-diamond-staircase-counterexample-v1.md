# Candidate counterexample to the planar diamond-staircase MSE conjecture

Observed checkpoint clock: **2026-10-23T14:49:43-0700** (`/bin/date`, copied verbatim). Owner: `InfoResearch96h`, info-1. Frozen model: [selection-v1.md](selection-v1.md). **CANDIDATE; written reasoning only; no program, solver, finite replay or formal verification. Current-source novelty remains UNCERTIFIED-OPEN / NOVELTY_UNCLEAR.** The same-norm resolutions in the selection are not contradicted.

## 1. Exact claimed delta and boundaries

Let

\[
D=\{x\in\mathbb R^2:|x_1|+|x_2|\leq1\},\qquad b=e^{-\varepsilon}\in(0,1).
\]

The feasible noise laws obey

\[
\mu(E)\leq b^{-1}\mu(E+h)\quad
\text{for every Borel }E\text{ and every }h\in D.
\tag{1}
\]

The cost is \(J(\mu)=\int(x_1^2+x_2^2)\,d\mu(x)\). Denote the full feasible infimum by \(V(\varepsilon)\). Let \(f_\gamma\), \(0\leq\gamma\leq1\), be exactly the **homothetic diamond** staircase family in the frozen selection and Geng–Viswanath arXiv:1312.0655v1, Section III. Denote its normalized cost by \(C_\gamma(b)\).

**Theorem (candidate).** For every

\[
\varepsilon\geq16\log 10\quad\text{equivalently}\quad0<b\leq10^{-16},
\tag{2}
\]

there is an explicitly specified centrally symmetric, non-diamond-radial additive density \(p_{r,b}\) satisfying (1), with

\[
V(\varepsilon)\leq J(p_{r,b})
<\frac{33}{50}\sqrt b
<\frac{333}{500}\sqrt b
\leq \min_{0\leq\gamma\leq1} C_\gamma(b).
\tag{3}
\]

Here \(r=\tfrac34b^{1/4}\), and the entire density, including every tail, is given in Section 4. In particular one exact instance is

\[
\varepsilon_0=16\log10,\quad b_0=10^{-16},\quad r_0=\frac3{40000}.
\tag{4}
\]

If correct, (3) refutes the literal all-epsilon conjecture that the **Section-III family \(f_\gamma\)** is optimal for squared-Euclidean cost under full diamond sensitivity. It does **not** determine the exact unrestricted \(V\), prove our family globally optimal, settle another epsilon regime, refute optimality of every abstract staircase-shaped density, or solve the whole book privacy tradeoff. Our own density has discrete geometric density levels; the excluded conjecture is specifically the homothetic-diamond family, not the word “staircase” without its defining formula.

## 2. Exact normalized baseline, including the entire gamma family

For \(t\geq0\), direct integration over the four quadrant triangles gives

\[
|tD|=2t^2,\qquad
M(tD):=\int_{tD}(x_1^2+x_2^2)\,dx=\frac23t^4.
\tag{5}
\]

For the moment computation, let the **auxiliary** geometric variable G have

\[
\Pr(G=k)=(1-b)b^k,\quad k=0,1,\ldots.
\]

This variable is a summation device, not an assumption on the noise law. The unnormalized \(f_\gamma\) equals, almost everywhere,

\[
(1-b)\sum_{k\geq0}b^k\mathbf1_{(k+\gamma)D}(x).
\tag{6}
\]

Indeed it is 1 for \(\|x\|_1<\gamma\), then b for \(\gamma<\|x\|_1<1+\gamma\), then \(b^2\), and so on, exactly the merged intervals of the frozen definition. Null boundaries do not change any integral. Formula (6) also covers gamma=0 and gamma=1; those two parameters yield the same normalized a.e. law.

Using Tonelli and (5), the exact normalized cost is

\[
C_\gamma(b)=\frac13
 \frac{\mathbb E(G+\gamma)^4}{\mathbb E(G+\gamma)^2}.
\tag{7}
\]

The denominator is strictly positive for every b>0 and gamma in [0,1], including gamma=0. In particular the cost is continuous on this compact gamma interval and its minimum is attained. No sampled or fixed gamma is substituted for that minimum.

For a completely explicit rational-in-b family formula, put \(T_j=\mathbb EG^j\), \(T_0=1\). Applying \(b\,d/db\) to the geometric series gives

\[
\begin{aligned}
T_1&=\frac b{1-b},&
T_2&=\frac{b(1+b)}{(1-b)^2},\\
T_3&=\frac{b(1+4b+b^2)}{(1-b)^3},&
T_4&=\frac{b(1+11b+11b^2+b^3)}{(1-b)^4}.
\end{aligned}
\tag{8}
\]

Thus

\[
C_\gamma(b)=\frac13
\frac{\gamma^4+4\gamma^3T_1+6\gamma^2T_2+4\gamma T_3+T_4}
 {\gamma^2+2\gamma T_1+T_2}.
\tag{9}
\]

This reconstructs the entire normalized baseline. For the strict comparison below a uniform all-gamma lower bound is sufficient; no closed-form optimizer is claimed or needed.

## 3. Uniform lower bound against the optimized baseline

Let

\[
a=\frac b{1-b},\qquad
v=\frac b{(1-b)^2},\qquad m=\gamma+a.
\]

The second centered moment of G is v. Substituting (8) into the centered third and fourth moments gives

\[
\tau_3=\frac{b(1+b)}{(1-b)^3}>0,\qquad
\tau_4=\frac{b(1+7b+b^2)}{(1-b)^4}\geq b.
\tag{10}
\]

For transparency, these follow respectively from
\(T_3-3aT_2+2a^3\) and
\(T_4-4aT_3+6a^2T_2-3a^4\).
Because m>=0,

\[
\mathbb E(G+\gamma)^2=m^2+v,\qquad
\mathbb E(G+\gamma)^4
=m^4+6m^2v+4m\tau_3+\tau_4\geq m^4+b.
\tag{11}
\]

For any real z>=0 the following is an exact identity:

\[
z^2+b-2(\sqrt b-v)(z+v)
=(z+v-\sqrt b)^2+v^2\geq0.
\tag{12}
\]

Use z=m^2 in (12), then (7) and (11), to obtain for **every** gamma in [0,1]

\[
C_\gamma(b)\geq\frac23(\sqrt b-v).
\tag{13}
\]

When b<=10^-16, it is in particular <=1/4, so
\((1-b)^2\geq9/16>1/2\) and v<=2b. Also
\(2\sqrt b\leq2\cdot10^{-8}<1/1000\). Hence

\[
C_\gamma(b)\geq\frac23\sqrt b(1-2\sqrt b)
\geq\frac23\frac{999}{1000}\sqrt b
=\frac{333}{500}\sqrt b.
\tag{14}
\]

The estimate holds simultaneously over the entire family, so it applies to the exact global minimum without locating its optimizer.

## 4. Explicit non-homothetic law and full translation privacy

Define the fixed rational octagon

\[
P=\{x:|x_1|\leq1,\ |x_2|\leq1,\ |x_1|+|x_2|\leq3/2\},\qquad S=rP.
\tag{15}
\]

For any r>0 and k>=0 let

\[
A_k=S+kD.
\]

These compact sets are nested and exhaust the plane. Define the integer-valued measurable function

\[
n(x)=\min\{k\in\mathbb Z_{\geq0}:x\in A_k\}.
\tag{16}
\]

It is finite everywhere because kD exhausts the plane and 0 belongs to S. Put

\[
Z=\int_{\mathbb R^2} b^{n(x)}\,dx,\qquad
p_{r,b}(x)=Z^{-1}b^{n(x)}.
\tag{17}
\]

The positive finite normalization and finite MSE are proved in Section 5, not assumed. For **every** h in D and **every** x,

\[
x\in A_{n(x)}\Longrightarrow x+h\in A_{n(x)+1},
\]

so \(n(x+h)\leq n(x)+1\). Applying the same implication at x+h with -h gives \(n(x)\leq n(x+h)+1\). Thus

\[
|n(x+h)-n(x)|\leq1,\qquad
p_{r,b}(x)\leq b^{-1}p_{r,b}(x+h).
\tag{18}
\]

Integrating (18) over any Borel E and changing variables proves exactly (1). This includes every real shift in the diamond, not just integer directions, vertices, a grid or sufficiently small shifts. The particular closed-boundary convention in (16) even gives the displayed density inequality pointwise; the measure statement therefore has no boundary exception.

All sets are centrally symmetric, hence the resulting law has mean zero once its finite second moment is established. For r>0 its first positive-area density plateau is an octagon, not a homothetic diamond.

## 5. Exact full-tail normalization and second moment

### 5.1 The Minkowski polygons and their moments

For k>=0 set L=k+r and c=k+r/2. The exact Minkowski sum is

\[
A_k=\{x:|x_1|\leq k+r,\ |x_2|\leq k+r,
\ |x_1|+|x_2|\leq k+3r/2\}.
\tag{19}
\]

One inclusion follows from the defining inequalities of S and kD. Conversely the polygon on the right has precisely the eight vertices

\[
(\pm(k+r),\pm r/2),\qquad(\pm r/2,\pm(k+r)),
\]

with independent signs in each pair. Each vertex is a vertex of rP plus respectively \((\pm k,0)\) or \((0,\pm k)\) in kD. Convexity proves the reverse inclusion. This also covers k=0 and every positive r.

The square [-L,L]^2 has four corner triangles removed, each with legs c, so

\[
|A_k|=4L^2-2c^2
=2k^2+6rk+\frac72r^2.
\tag{20}
\]

The full square has quadratic moment \(8L^4/3\). A removed corner triangle can be parameterized by u,v>=0, u+v<=c, with x=L-u, y=L-v. Its moment is

\[
\int_{u+v\leq c}\big[(L-u)^2+(L-v)^2\big]du\,dv
=L^2c^2-\frac23Lc^3+\frac16c^4.
\tag{21}
\]

Here the elementary triangular integrals are \(\int1=c^2/2\), \(\int(u+v)=c^3/3\), and \(\int(u^2+v^2)=c^4/6\). Subtracting four copies from the square moment yields, by expansion,

\[
\begin{aligned}
M(A_k)
&=\frac83L^4-4L^2c^2+\frac83Lc^3-\frac23c^4\\
&=\frac23k^4+4rk^3+8r^2k^2+\frac{20}{3}r^3k+\frac{47}{24}r^4.
\end{aligned}
\tag{22}
\]

In particular \(|P|=7/2\), \(M(P)=47/24\). No polygon coefficient has been inferred from point evaluations or numeric interpolation.

### 5.2 Exact summation, not a truncated tail

For every x, the geometric series beginning at n(x) gives

\[
b^{n(x)}=(1-b)\sum_{k\geq0}b^k\mathbf1_{A_k}(x).
\tag{23}
\]

Tonelli, (20), (22) and the geometric moments (8) give

\[
Z=\mathbb E|A_G|
=\frac72r^2+6rT_1+2T_2>0,
\tag{24}
\]

and

\[
J(p_{r,b})=
\frac{\frac{47}{24}r^4+\frac{20}{3}r^3T_1+8r^2T_2+4rT_3+\frac23T_4}
 {\frac72r^2+6rT_1+2T_2}.
\tag{25}
\]

Both series are finite because polynomial moments of G are finite for b in (0,1). Thus (17) is an actual probability density with finite quadratic cost, and (25) includes every tail exactly.

## 6. Explicit strict improvement in the stated regime

Set

\[
t=b^{1/4},\qquad r=\frac34t.
\tag{26}
\]

Under (2), 0<t<=1/10000. We first record an elementary uniform bound for (8). Since k^j<=k^4 for integer k>=1 and j=1,2,3,4,

\[
T_j\leq T_4\leq\frac{1001}{1000}b\quad(j=1,2,3,4).
\tag{27}
\]

To check the last inequality without an asymptotic approximation: b<=10^-16<=10^-5 and b<=1/16, so \(11b^2+b^3\leq b\); also \((1-b)^4\geq1-4b>0\). Therefore

\[
\frac{T_4}{b}\leq\frac{1+12b}{1-4b}\leq\frac{1001}{1000},
\]

where the final inequality is equivalent to \(16004b\leq1\), true already for b<=10^-5.

Drop the positive tail terms in the denominator of (25), apply (27) to its numerator, and substitute (26). Dividing by \(t^2=\sqrt b\) gives

\[
\frac{J(p_{r,b})}{\sqrt b}
\leq\frac{141}{448}
+\frac{1001}{1000}
 \left(\frac{64}{189}+\frac{32}{21}t+\frac{16}{7}t^2+\frac{10}{7}t^3\right).
\tag{28}
\]

Every coefficient follows directly from (25): respectively the scaled terms \((47/84)r^2\), \((4/21)b/r^2\), \((8/7)b/r\), \((16/7)b\), and \((40/21)br\).

Now

\[
\frac{141}{448}<\frac{63}{200},\qquad
\frac{64}{189}<\frac{339}{1000}.
\]

Because t<=1/10000<1,

\[
\frac{32}{21}t+\frac{16}{7}t^2+\frac{10}{7}t^3
\leq\frac{110}{21}t<6t\leq\frac6{10000}.
\]

Consequently the parenthesis in (28) is less than
\(339/1000+6/10000=3396/10000<17/50\). Hence

\[
\frac{J(p_{r,b})}{\sqrt b}
<\frac{63}{200}+\frac{1001}{1000}\frac{17}{50}
=\frac{32767}{50000}
<\frac{33}{50}.
\tag{29}
\]

Combining (14) and (29) proves every inequality in (3). This is a finite explicit bound, not merely a leading-order expansion. At (4) the strict separation from the entire optimized family is more than

\[
\left(\frac{333}{500}-\frac{33}{50}\right)10^{-8}
=\frac3{500}\,10^{-8}.
\tag{30}
\]

No claim about practical privacy budgets is made: the proved comparison is deliberately in the specified weak-privacy/large-epsilon regime.

## 7. Independent-check interface and source boundaries

The candidate's load-bearing checks are: (i) exact equivalence of the source's f_gamma with (6), including gamma endpoints; (ii) centered geometric moments and the all-gamma lower bound (10)–(14); (iii) full-shift privacy from integer level indices, not a local-only Lipschitz condition; (iv) Minkowski polygon (19), every moment coefficient in (20)–(22), and Tonelli normalization; (v) rational inequalities (27)–(29). These can all be reconstructed by hand without scientific execution.

The argument is an independent written derivation. Neither peer reconstruction, full parent reconstruction, formal verification, nor novelty acceptance has yet occurred for this manuscript. The source screen distinguishes the actual same-norm theorems from this mixed model; it does not certify that this octagonal/Minkowski construction has never appeared. The book provenance remains a broad privacy-utility article; only the exact frozen modern conjecture is addressed here. All older Kuroki/P24 qualifications are preserved unchanged in their retired evidence.
