# Candidate all-law full-tail peak bound and its exact finite-epsilon obstruction

Observed clock before creation: **2026-10-23T15:54:33-0700** (`/bin/date`). Same info-1 finite-epsilon V and [exploratory residual](residual-peak-envelope-duality-v1.md). **CANDIDATE; author written reasoning only; no execution, inherited verdict, numerical root solve or formal verification. NOVELTY_UNCLEAR.** This is an all-law necessary-envelope relaxation, not another upper-core family or a proposed exact solution of V.

## 1. Exact claims and the deliberately separated primal classes

Fix 0<b<1 and the full sensitivity diamond

\[
D=\{x\in\mathbb R^2:|x_1|+|x_2|\leq1\}.
\]

The original feasible laws satisfy

\[
\mu(E)\leq b^{-1}\mu(E+h)
\quad\text{for every Borel }E\text{ and every }h\in D.
\tag{1}
\]

Let V_b be their unrestricted squared-Euclidean MSE infimum. No density, symmetry, regularity, attained peak or single-core representation is assumed in this original class.

Define the **full** point-core geometric envelope

\[
g_b(x)=b^{\lceil\|x\|_1\rceil},\qquad g_b(0)=1.
\tag{2}
\]

Its values on integer-radius boundaries use this explicit closed-set convention; all integrals are unaffected by those null boundaries. Put

\[
Z_g=\int g_b(x)dx,\quad N_g=\int\|x\|_2^2g_b(x)dx,\quad
F_b(s)=\int(\|x\|_2^2-s)_+g_b(x)dx\quad(s\geq0).
\tag{3}
\]

Let s_b be the unique positive solution of the **explicit integral equation**

\[
F_b(s_b)=\frac\pi2s_b^2.
\tag{4}
\]

The root is a definition via a known integrand, not a numerical output or an asserted value of V.

The peak-envelope **relaxation** consists of normalized densities p for which some M>0 and center c satisfy

\[
M g_b(x-c)\leq p(x)\leq M\quad\text{a.e.}
\tag{5}
\]

It omits the original privacy conditions between all other pairs/level sets. This omission is intentional and its consequence is proved, not hidden.

**Theorem (candidate).**

1. Every finite-cost law satisfying (1) has a density and belongs to (5), with M its finite essential supremum and some **derived** center c, even if its essential peak is not attained.
2. The exact optimum of relaxation (5) is s_b. Its unique a.e. minimizing density is

\[
p_b^{\rm rel}(x)=M_b
\begin{cases}
1,&\|x\|_2^2\leq s_b,\\
g_b(x),&\|x\|_2^2>s_b,
\end{cases}
\quad
M_b^{-1}=\pi s_b+\int_{\|x\|_2^2>s_b}g_b(x)dx.
\tag{6}
\]

3. **The density (6) is not feasible for the original full-DP problem, for any 0<b<1.** It violates one fixed allowed shift on a positive-area open region. The original V_b is attained by some feasible law (a standard well-posedness fact proved below), so

\[
V_b>s_b>0\quad\text{for every finite }0<b<1.
\tag{7}
\]

This supplies an all-law finite-b lower bound and an exact obstruction to matching it by the one-peak relaxation. It does **not** compute V_b or an original feasible optimizer, provide an explicit magnitude for the strict gap in (7), or prove that no other all-law dual certificate can be sharp. The relaxed primal (6) must never be described as an admissible optimum of the original problem.

## 2. The full envelope and every geometric tail

Let G be a summation variable with probability (1-b)b^k on k=0,1,.... The identity

\[
g_b(x)=(1-b)\sum_{k\geq0}b^k\mathbf1_{kD}(x)
\tag{8}
\]

holds pointwise with (2)'s convention. Since \(|kD|=2k^2\) and \(\int_{kD}\|x\|_2^2dx=\tfrac23k^4\), Tonelli gives

\[
Z_g=2\mathbb EG^2=\frac{2b(1+b)}{(1-b)^2},\qquad
N_g=\frac23\mathbb EG^4
=\frac{2b(1+11b+11b^2+b^3)}{3(1-b)^4}.
\tag{9}
\]

Both are positive and finite. The first vector moment is zero by evenness and is absolutely integrable by the finite mass/second moment. No tail is truncated. Likewise

\[
F_b(s)=(1-b)\sum_{k\geq0}b^k
\int_{kD}(\|x\|_2^2-s)_+dx
\tag{10}
\]

is an exact nonnegative full-tail expression. One may also use the exact identity

\[
F_b(s)=N_g-sZ_g+
\int_{\|x\|_2^2\leq s}(s-\|x\|_2^2)g_b(x)dx.
\tag{11}
\]

These specify the root's function completely; no experiment or hidden finite cutoff defines it.

## 3. Necessary envelope for every finite-cost original law

### 3.1 Density and the correct countable quantifiers

As in the standalone earlier all-law argument, absolute continuity follows directly from (1): for any Borel Lebesgue-null N, integration over h in D gives

\[
2\mu(N)\leq b^{-1}\int_D\mu(N+h)dh=0.
\]

The final equality is Tonelli for \(\mathbf1_N(x-h)\): every fixed-x section is a translated null set. Choose a nonnegative Borel density p with unit integral, finite a.e.

For **each integer k>=1** and **each fixed t in kD**, iterate (1) with the allowed shift t/k, k times:

\[
\mu(E)\leq b^{-k}\mu(E+t).
\tag{12}
\]

All-Borel domination implies \(p(x+t)\geq b^kp(x)\) for a.e. x, with an exception possibly depending on t. For this k, apply Tonelli to its jointly measurable bad-pair set on \(\mathbb R^2\times kD\). The result is a full-measure set H_k of x for which the inequality holds for **almost every t in kD**, not every t pointwise.

Intersect the H_k over the **countably many** positive integers, also discarding the null set where p is infinite. For every c in the resulting full-measure H, countable union of its exceptional translated sets gives

\[
p(y)\geq p(c)g_b(y-c)\quad\text{for a.e. }y.
\tag{13}
\]

Indeed choose the smallest positive integer k with y-c in kD; the isolated point y=c is irrelevant. This is the best available integer-step envelope at every finite radius, not only the first diamond.

Integrating (13) shows p(c)Z_g<=1 for c in H. Consequently

\[
0<M=\operatorname*{ess\,sup}p\leq Z_g^{-1}<\infty.
\tag{14}
\]

Choose actual c_n in H and in the full-measure set p<=M so that a_n=p(c_n) tends to M. Essential near-peak sets have positive measure, so these choices require no attained maximum.

### 3.2 The center is derived from finite cost, not imposed

For every n, (13) and the full envelope moment give

\[
J(p)\geq a_n\int\|y\|_2^2g_b(y-c_n)dy
=a_n\big(N_g+Z_g\|c_n\|_2^2\big).
\tag{15}
\]

If J is finite, a_n is eventually at least M/2>0, hence c_n is bounded. Pass to a subsequence c_n tending to c. Every floor (13) holds on one common full-measure y set after taking their countable intersection. For y-c off the countable family of integer-l1-radius boundaries, \(g_b(y-c_n)\) is eventually equal to \(g_b(y-c)\), by continuity of the l1 norm away from integer radii. The excluded boundaries have planar measure zero. Letting n tend to infinity in (13) therefore yields

\[
p(y)\geq M g_b(y-c)\quad\text{a.e.}
\tag{16}
\]

Together with p<=M, this proves membership in relaxation (5). It does not assert p(c)=M or a pointwise privacy version for all shifts. Boundedness/convergence of the selected centers was proved using the **full** finite-cost envelope, not silently assumed.

## 4. Root, centering and the valid all-law lower certificate

The function F_b(s) is finite and continuous for s>=0 by domination with \(\|x\|^2g_b(x)\). It is strictly decreasing: for s1<s2 its positive tail outside the radius-sqrt(s2) disk contributes at least \((s2-s1)\int_{\|x\|^2>s2}g_b>0\) to the decrease. It starts at N_g>0 and tends to zero by dominated convergence. The right side of (4) starts at zero and increases strictly to infinity. Thus (4) has exactly one positive root.

For fixed s>=0 define the translated floor penalty

\[
\mathcal F_{b,s}(c)=
\int(\|x\|_2^2-s)_+g_b(x-c)dx
=\int(\|u+c\|_2^2-s)_+g_b(u)du.
\tag{17}
\]

The function \(f_s(u)=(\|u\|^2-s)_+\) is convex and even. Since g_b is even, its convolution penalty is convex/even, so \(\mathcal F_{b,s}(c)\geq\mathcal F_{b,s}(0)=F_b(s)\). The inequality is **strict for c not equal to0**: the midpoint convexity gap

\[
f_s(u+c)+f_s(u-c)-2f_s(u)
\]

is nonnegative everywhere and equals \(2\|c\|^2>0\) whenever \(\|u\|>\sqrt s+\|c\|\). That region has positive g_b mass. Thus0 is the unique minimizer of the translated penalty. No symmetry assumption on the original law was needed.

Now fix any relaxed density (5) with finite cost and set R=sqrt(s). Split the quadratic excess inside/outside B_R. The upper cap controls the negative part, and the envelope controls the positive part:

\[
\begin{aligned}
J(p)-s
&=\int(\|x\|^2-s)p(x)dx\\
&\geq-M\int_{B_R}(s-\|x\|^2)dx
+M\int_{B_R^c}(\|x\|^2-s)g_b(x-c)dx\\
&=-M\frac\pi2s^2+M\mathcal F_{b,s}(c).
\end{aligned}
\tag{18}
\]

At s=s_b, (4) makes this at least zero, proving J>=s_b for every relaxed density and therefore for every original finite-cost law by Section3. Infinite-cost laws satisfy the bound trivially. This is a valid all-law lower certificate; it uses no one-core restriction on that feasible set.

## 5. Exact relaxed optimum and its equality characterization

Let R=sqrt(s_b), and let p_b^rel be (6). Its denominator H_b is positive finite. Because0<g_b<=1, the density has mass one, cap M_b, floor M_b g_b and finite cost. Direct subtraction gives

\[
\begin{aligned}
J(p_b^{\rm rel})-s_b
&=M_b\left[-\frac\pi2s_b^2+
\int_{B_R^c}(\|x\|^2-s_b)g_b(x)dx\right]=0.
\end{aligned}
\tag{19}
\]

Thus the relaxation really has optimum s_b, not merely a lower estimate.

Conversely equality in (18) at that value forces c=0 by strict centering. The cap slack inside the disk and floor slack outside are nonnegative and weighted by strictly positive quadratic excess away from the circular boundary. Both integrals must vanish. Hence p=M a.e. inside B_R and p=M g_b a.e. outside. Normalization determines M=M_b. This proves the unique a.e. minimizing density (6), without asserting original feasibility.

## 6. Full-DP negative control: the relaxed optimizer fails on positive area

Take the **fixed allowed shift** h=(1,0). Let

\[
\delta=\min\{R/2,1/2\},\qquad x_0=(R-\delta,0).
\]

Then x_0 lies strictly inside B_R, its first coordinate is positive, x_0+h lies strictly outside B_R, and \(\|x_0+h\|_1>1\). These strict inequalities persist on a nonempty open neighborhood U of x_0. For almost every x in U,

\[
p_b^{\rm rel}(x)=M_b,\qquad
p_b^{\rm rel}(x+h)=M_b g_b(x+h)\leq b^2M_b<bM_b.
\tag{20}
\]

This contradicts the necessary density inequality \(p(x+h)\geq bp(x)\) for the single shift h, on a **positive-area** set. It cannot be repaired by changing null-set boundary values. Therefore (6) fails the original privacy model for every b in (0,1).

The failure is precisely the omitted coupling: a positive-area maximum plateau B_R must generate a whole b-height floor on **B_R+D**, not just the b-height portion of the point-envelope centered at0. The relaxed construction fills a maximum plateau without paying for all its translated floors. No MSE optimizer of the original model is disproved merely by this one rejected relaxed density.

## 7. Standard well-posedness and strict original/relaxed separation

For completeness, the original infimum is attained. This is a standard tightness/weak-closure argument, not a separately claimed discovery. Its explicit standard imports are the weak sequential compactness of tight probability measures on Euclidean space (Prokhorov) and regularity/positivity characterization of finite Radon measures.

Write epsilon=-log b>0. The product Laplace density

\[
p_L(x)=\frac{\varepsilon^2}{4}e^{-\varepsilon\|x\|_1}
\]

is feasible by the l1 triangle inequality and has cost4/epsilon². Thus V_b is finite. A minimizing sequence has uniformly bounded second moments and is tight by Markov's inequality. Extract a weakly convergent subsequence with probability limit mu_*.

For any **arbitrary fixed** h in D and nonnegative compactly supported continuous test function phi, original feasibility gives

\[
\int\phi\,d\mu_n\leq b^{-1}\int\phi(\cdot-h)\,d\mu_n.
\tag{21}
\]

Both test functions are bounded continuous, so this inequality passes to the weak limit. Since h and phi were arbitrary and the whole weakly convergent subsequence has convergence for every bounded continuous test, no uncountable union of null sets is being taken here. Positivity against all such phi implies the all-Borel domination \(\mu_*(E)\leq b^{-1}\mu_*(E+h)\), by the standard positivity characterization of Radon measures. Thus mu_* is feasible for every h in D.

For each L>0 the bounded continuous function \(\min\{\|x\|^2,L\}\) has limiting integral at most liminf J(mu_n)=V_b. Increase L to infinity to obtain J(mu_*)<=V_b. Feasibility gives the reverse inequality, hence J(mu_*)=V_b.

If V_b equaled s_b, this minimizer would be a finite-cost original law, hence belong to the relaxation by Section3. Equality characterization would force its density to be (6), contradicting Section6. Therefore

\[
V_b>s_b\qquad(0<b<1).
\]

This strict statement does not supply a closed-form positive gap or an exact original minimizer. The existence argument is compatible with the nonexistence of multivariate *canonical noise distributions* in Awan–Dong2022: their Definition4.1 imposes additional ROC equality and monotone-likelihood-ratio conditions, not imposed by MSE minimization here.

## 8. Literal remaining coupled-level-set obligation

The full point-envelope g_b includes **every** integer-radius tail, so the obstruction is not a missing tail cutoff. It comes from considering only one limiting essential peak, while original privacy couples every nontrivial superlevel set to its diamond expansion. The height-cap/root certificate is exactly sharp for its stated relaxation and **never** sharp for original finite V.

A matching finite-epsilon certificate must enforce more of that coupled geometry, or an equally strong all-law condition, and be matched by an actually admissible law. It is not proved that one convex core with minimal Minkowski tails contains an original optimizer. The disk-core packet rules out another natural shortcut if independently accepted; its verdict does not verify the present peak-relaxation proof.

No new mechanism, CND theorem, density-cap principle, compactness theorem or layer-cake device is claimed as an invention. The exact peak-relaxation/root/strict-gap statement needs its own mathematical and source-priority checks. The current affine-square source audit and unresolved broad2026 vector comment remain operative; **NOVELTY_UNCLEAR**. No scientific execution, sample evaluation, numerical root solve, source-code test or formal proof assistant was used.
