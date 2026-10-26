# Candidate coupled optimal-level condition and eventual forced tails

Observed clock before creation: **2026-10-23T16:11:41-0700**. Same info-1 finite-epsilon all-Borel problem and [coupled-level residual](residual-coupled-level-tail-v1.md). **CANDIDATE, structural only: exact finite V and the optimal head sets remain OPEN.** Author written reasoning, no inherited verdict, scientific execution, solver, numerical level search or formal verification. **NOVELTY_UNCLEAR.**

This is not another envelope constant or core-family improvement. It uses the genuine privacy coupling at **every** level and an actual feasible factor-b mass lowering. Standard amplitude slicing, well-posedness and measure tools are not separately claimed discoveries.

## 1. Model and exact proposed structural result

Fix 0<b<1, epsilon=-log b, and

\[
D=\{h\in\mathbb R^2:|h_1|+|h_2|\leq1\}.
\]

The original class is **all Borel probability laws** with

\[
\mu(E)\leq b^{-1}\mu(E+h)
\quad\text{for every Borel }E\text{ and every }h\in D.
\tag{1}
\]

Write \(V_b\) for their squared-Euclidean MSE infimum. No density, symmetry, radiality, convexity or one-core assumption is imposed on this class.

**Theorem (candidate).** An original minimizer exists, and one can choose a minimizer with density

\[
q(x)=a b^{n(x)},\qquad a>0,\quad n(x)\in\mathbb Z_{\geq0}\text{ a.e.},
\tag{2}
\]

whose top plateau \(\{n=0\}\) has positive area. This does not say every optimal density must have that form.

For any optimizer (2) with that top-level convention, put

\[
J=V_b=\int\|x\|_2^2q(x)dx,\quad
E_k=\{n\leq k\},\quad
K_k=\operatorname{supp}(\mathbf1_{E_k}\,dx),\quad
B_R=\{x:\|x\|_2\leq R\},\ R=\sqrt J.
\tag{3}
\]

The essential supports K_k are nonempty compact sets, **not assumed convex**. For every integer k>=0,

\[
K_k+D\ \subseteq\ K_{k+1}\ \subseteq\ (K_k+D)\cup B_R.
\tag{4}
\]

In addition, \(K_k+D\subseteq E_{k+1}\) up to a planar null set.

The cost ball lies in a finite level, with a coarse explicit bound depending only on b. Define

\[
Z_g=\frac{2b(1+b)}{(1-b)^2},\quad
U_b=\frac4{\varepsilon^2},\quad
T_b=1+\left\lceil2\sqrt{\frac\pi{Z_g}}\,U_b+\sqrt{2U_b}\right\rceil.
\tag{5}
\]

Then \(B_R\subseteq K_{T_b}\) and \(B_R\subseteq E_{T_b}\) a.e. Consequently for every k>=T_b,

\[
K_{k+1}=K_k+D,\qquad E_{k+1}=K_k+D\quad\text{a.e.}
\tag{6}
\]

Equivalently, with the compact tail core \(P=K_{T_b}+D\),

\[
E_{T_b+1+j}=P+jD\quad\text{a.e. for every }j\geq0.
\tag{7}
\]

Thus **some unrestricted optimum has a finite arbitrary head and one forced Minkowski tail**. This is not a supplied optimal density/value: the head sets and P remain unknown shapes, possibly nonconvex. It is not a finite-dimensional reduction or a fast algorithm. In particular it does not assume \(E_k=E_0+kD\) at early levels.

## 2. All-law preliminary facts, with the correct null-set quantifiers

These are standard tools, included to avoid a hidden density or attained-peak ansatz.

For a Borel Lebesgue-null set N, integrating (1) over h in the area-two diamond gives

\[
2\mu(N)\leq b^{-1}\int_D\mu(N+h)dh=0
\]

by Tonelli on \(\mathbf1_N(x-h)\). Therefore every original law has a nonnegative Borel density p.

For each integer j>=1 and fixed t in jD, j repetitions of t/j give \(\mu(E)\leq b^{-j}\mu(E+t)\). Comparing densities gives \(p(x+t)\geq b^jp(x)\) for a.e. x, possibly with a t-dependent exception. Tonelli on \(\mathbb R^2\times jD\), followed only by a **countable intersection over j**, produces a full-measure set H such that for every c in H,

\[
p(y)\geq p(c)g_b(y-c)\quad\text{for a.e. }y,
\quad g_b(z)=b^{\lceil\|z\|_1\rceil},\ g_b(0)=1.
\tag{8}
\]

One removes the countably many exceptional translated sections and chooses the smallest positive integer containing y-c. The isolated y=c point is irrelevant. No common pointwise density version for all shifts is asserted.

The exact full-tail layer identity

\[
g_b=(1-b)\sum_{j\geq0}b^j\mathbf1_{jD}
\]

gives its positive finite mass Z_g in (5) and positive finite quadratic moment \(N_g=\tfrac23\mathbb EG^4\), with \(\Pr(G=j)=(1-b)b^j\). Evenness gives zero vector first moment; finite second moment makes it absolutely integrable. Integrating (8) yields

\[
0<M:=\operatorname*{ess\,sup}p\leq Z_g^{-1}<\infty.
\tag{9}
\]

A positive-integral density has a good c with p(c)>0, so (8) also proves p>0 a.e. For finite cost,

\[
J(p)\geq p(c)\big(N_g+Z_g\|c\|_2^2\big)
\tag{10}
\]

whenever c is good. These facts use every integer-radius tail, not a finite cutoff or an attained maximum.

The original infimum is attained by a standard compactness argument. The product Laplace density epsilon² exp(-epsilon||x||_1)/4 is feasible by the triangle inequality and has cost U_b. A minimizing sequence has uniformly bounded second moments, hence is tight by Markov. Prokhorov weak sequential compactness on Euclidean probability laws gives a probability limit. For arbitrary fixed h in D and phi in nonnegative C_c,

\[
\int\phi\,d\mu_m\leq b^{-1}\int\phi(\cdot-h)\,d\mu_m
\]

passes to that weak limit. Positivity of the resulting Radon measure against all such phi gives the original all-Borel inequality for that arbitrary h; the same weak convergence works for all bounded continuous tests, so no h-dependent subsequence or uncountable null-set intersection is used. Increasing bounded continuous truncations of ||x||² proves lower semicontinuity and attainment. These classical compactness/regularity facts are explicit standard imports, not new research claims. Let p_* be one finite-cost optimizer.

## 3. Amplitude slicing selects a geometric-valued genuine optimizer

Let M be the essential supremum of p_*. For each height t in [bM,M), define

\[
n_t(x)=\min\{k\geq0:p_*(x)>t b^k\},\quad
r_t(x)=b^{n_t(x)}.
\tag{11}
\]

At the null set p_*=0 use n_t=infinity and r_t=0. The index is finite a.e. by Section2 positivity. It is Borel. Its top plateau \(\{p_*>t\}\) has positive area because t<M is below the essential supremum.

For every fixed h in D, the a.e. inequality \(p_*(x+h)\geq bp_*(x)\) implies

\[
p_*(x)>t b^k\Longrightarrow p_*(x+h)>t b^{k+1}.
\]

The reverse shift gives \(|n_t(x+h)-n_t(x)|\leq1\) for a.e. x. Hence the normalized density \(q_t=r_t/Z_t\), \(Z_t=\int r_t\), satisfies the full measure privacy condition for **every** h. There is no restriction to grid shifts.

The elementary bounds

\[
\frac b t p_*(x)\leq r_t(x)\leq\frac1t p_*(x)
\tag{12}
\]

hold a.e. If n_t>=1 they follow from \(t b^{n_t}<p_*\leq t b^{n_t-1}\); if n_t=0 the lower bound follows from t>=bM. Thus \(b/t\leq Z_t\leq1/t\), and each q_t has positive finite normalization and finite cost.

Partition the ordinary layer integral at the geometric heights. Nonnegative Tonelli gives exactly

\[
\begin{aligned}
p_*(x)
&=\sum_{k\geq0}\int_{bM}^{M}b^k
 \mathbf1_{\{p_*(x)>t b^k\}}dt\\
&=\frac1{1-b}\int_{bM}^{M}r_t(x)dt.
\end{aligned}
\tag{13}
\]

The first equality is the substitution u=t b^k on each interval [b^(k+1)M,b^k M]; the second is the geometric tail starting at n_t. Consequently

\[
1=\int_{bM}^{M}\frac{Z_t}{1-b}dt,\qquad
J(p_*)=\int_{bM}^{M}J(q_t)\frac{Z_t}{1-b}dt.
\tag{14}
\]

All t-dependent functions are measurable by their countable indicator/layer expressions. Every q_t is genuinely feasible, so J(q_t)>=V_b. Since the average equals V_b, equality holds for almost every t under the displayed probability mixture. Select one such t. Then q=q_t has the form (2), a=1/Z_t, finite cost J=V_b and a positive-area top plateau.

This is an exact representation tool, not a claim that every optimizer or its level sets are homothetic staircases. No convexity, symmetry or one-core shape has been assumed.

## 4. Compact essential supports and exact forced dilation

Fix a geometric-valued optimizer q as in Section3. Each E_k has finite positive area because q>=a b^k on E_k and E_0 has positive area. Its essential support K_k is closed, E_k is contained in K_k a.e., and the supports are nested.

They are bounded as well. For almost every x, the first-diamond section of privacy gives q(y)>=bq(x) a.e. on x+D. Since the diamond has area2, centroid0 and moment2/3,

\[
J\geq bq(x)(2/3+2\|x\|_2^2).
\]

For a.e. x in E_k this implies

\[
\|x\|_2^2\leq\frac{J}{2a b^{k+1}}.
\tag{15}
\]

Thus E_k is essentially bounded and K_k is nonempty compact. No convexification has occurred.

For every **fixed** h in D, the a.e. privacy index bound implies

\[
\lambda\big((E_k+h)\setminus E_{k+1}\big)=0.
\tag{16}
\]

Taking essential supports for that h gives \(K_k+h\subseteq K_{k+1}\). Since h was arbitrary, this proves the exact closed-set inclusion

\[
K_k+D\subseteq K_{k+1}.
\tag{17}
\]

It is a statement about supports, not a false pointwise upgrade of all density inequalities.

A stronger **a.e. filling** fact is needed later. Tonelli in the variables (y,h) gives, for almost every y, q(y)>=bq(y-h) for a.e. h in D. If

\[
(\mathbf1_{E_k}*\mathbf1_D)(y)>0,
\]

then q(y)>=a b^(k+1), so y belongs to E_(k+1), except on the global null set of bad y. For y in K_k+int(D), choose a support point z in K_k with y-z in int(D). A small ball about z lies in y-D and meets E_k in positive area by the definition of essential support. Therefore that convolution is positive. Hence

\[
K_k+\operatorname{int}D\subseteq E_{k+1}\quad\text{a.e.}
\tag{18}
\]

The following elementary parallel-set fact removes the remaining boundary **even when K_k is nonconvex**.

### Positive-offset boundary lemma

For any nonempty compact K, let d(x)=dist_1(x,K). Then

\[
K+D=\{d\leq1\},\quad K+\operatorname{int}D=\{d<1\},\quad
\lambda\{d=1\}=0.
\tag{19}
\]

Only the last assertion needs proof. The norm-distance function is Euclidean-Lipschitz, hence differentiable a.e. by the classical Rademacher theorem. At a differentiability point x outside K, take a nearest z in K and v=(x-z)/d(x), so ||v||_1=1. For 0<t<d(x), the nearest-point bound and the Lipschitz bound give exactly d(x-tv)=d(x)-t. Therefore grad(d) dot v=1, and the dual-norm Lipschitz bound implies ||grad(d)||_infinity=1. In particular its gradient is nonzero a.e. outside K.

If the level set {d=1} had positive area, almost every one of its points would be a Lebesgue density point and a differentiability point. A differentiable function constant on a set of density1 has gradient0 there: a nonzero gradient would confine that level set in arbitrarily thin slabs in small balls, contradicting density1. This contradicts the preceding nonzero gradient. Thus the level has area0. Nearest points exist because K is compact, giving the two set identities in (19). Rademacher and the Lebesgue density theorem are explicit classical imports, not new discoveries.

Apply (19) to K_k in (18). We obtain the promised full a.e. forcing

\[
K_k+D\subseteq E_{k+1}\quad\text{a.e.}
\tag{20}
\]

No regularity, convexity or zero-area boundary of K_k itself was assumed.

## 5. Actual feasible lowering yields the cost-ball optimality condition

Fix k>=0 and consider the Borel set

\[
U=\big(E_{k+1}\setminus E_k\big)
\setminus(K_k+D)
\quad\cap\quad\{x:\|x\|_2^2>J\}.
\tag{21}
\]

On U the old index is exactly k+1. Lower q by the factor b there and nowhere else:

\[
\widetilde q(x)=\begin{cases}bq(x),&x\in U,\\q(x),&x\notin U.\end{cases}
\tag{22}
\]

This is not just a first variation. We check exact privacy before renormalizing.

For an arbitrary fixed h in D, discard the original null sets on which the index bound fails, plus fixed translates of E_k outside K_k (a null set). If x is in U and y=x+h is not in U, then y cannot have index <=k: otherwise y would lie in K_k and x=y-h in K_k+D, a contradiction. The original bound leaves y's index either k+1 or k+2. After x is changed to index k+2, their index difference is still at most1. If both points lie in U they are changed equally; if neither does, nothing changes. The case only y in U is symmetric. Thus the full a.e. index privacy bound holds for this arbitrary h, and hence for every allowed h in the measure sense.

The new mass is

\[
z'=1-(1-b)\int_Uq>0.
\]

It is strictly positive because the positive-mass top plateau E_0 is never changed. Therefore \(q'=\widetilde q/z'\) is a genuine feasible probability density with finite cost. If U had positive area, its q-mass would be positive, and the exact cost difference would be

\[
J(q')-J
=-\frac{(1-b)\int_U(\|x\|_2^2-J)q(x)dx}{z'}<0,
\tag{23}
\]

contradicting optimality. Every signed integral is finite because the original second moment is finite. Consequently U is null.

Since E_k lies in K_k+D a.e., this yields

\[
E_{k+1}\subseteq(K_k+D)\cup B_R\quad\text{a.e.}
\tag{24}
\]

The right side is closed. Taking essential supports gives \(K_{k+1}\subseteq(K_k+D)\cup B_R\). Together with (17) this proves (4).

The lowering proof is the genuine coupled-level step: removing mass is allowed only where **no previous-level point can force its old height**. It does not treat different plateaus as independent or assume minimal expansion at every level.

## 6. A finite cost-ball coverage level, with an explicit bound

The elementary density-cap moment inequality for q<=a and unit mass is

\[
J\geq\frac1{2\pi a}.
\tag{25}
\]

For clarity, compare q with a times the centered disk indicator of area1/a. The product (||x||²-R0²)(q-a1_(B_R0)) is nonnegative inside/outside that disk; equal masses remove the constant term and give exactly1/(2pi a). This standard bathtub inequality is a bound used in the proof, not another claimed discovery.

Choose c in the positive-area top plateau E_0 and in the full-measure good set for all integer translations. Then q(c)=a and the complete envelope (8) gives

\[
q(y)\geq a g_b(y-c)\quad\text{a.e.},\qquad
J\geq a(N_g+Z_g\|c\|_2^2).
\tag{26}
\]

This attained plateau belongs to the **selected geometric optimizer**; no attained-peak hypothesis was inserted into the original all-law class.

Combining (25) and (26) gives

\[
\|c\|_1\leq\sqrt2\|c\|_2
\leq2\sqrt{\frac\pi{Z_g}}J.
\tag{27}
\]

Since J<=U_b, every y in B_R satisfies

\[
\|y-c\|_1
\leq2\sqrt{\frac\pi{Z_g}}U_b+\sqrt{2U_b}
<T_b.
\tag{28}
\]

The a.e. floor in (26) therefore implies q(y)>=a b^(T_b) a.e. on B_R. Because the density takes only its geometric levels, this is precisely \(B_R\subseteq E_{T_b}\) a.e. The support of Lebesgue measure on the closed positive-radius ball is the whole ball, so \(B_R\subseteq K_{T_b}\). (J>0 because a unit-density law cannot have its finite moment0; it also follows from (25).)

The T_b bound is deliberately coarse. It establishes a finite structural tail-start index, not a computational performance bound or authorization to enumerate that many levels.

## 7. Exact eventual saturation and what remains unknown

For all k>=T_b, nesting gives B_R contained in K_k and hence in K_k+D. The two sides of (4) then force

\[
K_{k+1}=K_k+D.
\]

A.e. inclusion (20) and (24) simultaneously give \(E_{k+1}=K_k+D\) a.e. Induction proves (6)–(7), with compact P=K_(T_b)+D. P contains the cost ball and has positive area, but is **not asserted convex**.

The exact density layer identity is

\[
q(x)=a(1-b)\sum_{k\geq0}b^k\mathbf1_{E_k}(x)\quad\text{a.e.}
\]

so the whole remaining tail is determined by P+jD after the finite prefix. This does not license polynomial Steiner coefficients for an arbitrary nonconvex P, or replace the remaining shape optimization by a finite table. The head E_0,...,E_(T_b) and their coupling remain unknown; selecting them and a matching all-law dual is still necessary to compute V.

This is a theorem about the structure of **some genuine unrestricted optimizer**, not a construction of its unknown prefix or a claimed exact finite-epsilon noise formula. It does not reduce the original feasible set to symmetric/radial/convex cores and does not promote one-core minimal tails from level0. The familiar amplitude-slicing/compactness and geometric/measure lemmas are tools, not separately counted discoveries. The possible structural contribution is the exact cost-ball optimality condition and finite forced-tail statement at the actual unrestricted model; its source-priority status remains **NOVELTY_UNCLEAR**.

Each load-bearing step needs its own actual reconstruction: phase mixture weights/privacy; essential-support forcing with correct a.e. quantifiers; the nonconvex positive-offset boundary lemma; exact privacy and sign of the factor-b lowering; and the explicit finite coverage bound. No earlier octagonal, asymptotic, disk or peak-envelope verdict is inherited. No scientific execution or formal/kernel proof was performed.
