# Classical proofs for the piecewise-LTI question

Date: 2026-10-14 (PT). These are written mathematical proofs, not Lean-kernel certificates. All positive results below have the label **Certification; novelty not claimed**. The regulated-function theorem is classical; the applications, estimates and counterexamples are elementary consequences. No statement here equates a deterministic trajectory with a stationary stochastic process.

## 0. Fixed conventions and scope

Lebesgue measure is used throughout. Functions and kernels are identified almost everywhere. The input-indexed model printed in book equation (1) is

\[
 (T_w r)(t)=\int_I w_\tau(t-\tau)r(\tau)\,d\tau,
 \qquad w_\tau(u)=w(\tau,u).
\]

An input-piecewise LTI approximation means
\(s_\tau=h_j\) for \(\tau\in I_j\), so
\(T_s r=\sum_j h_j*(r1_{I_j})\).
It does **not** mean \(\sum_j1_{I_j}(h_j*r)\), which freezes at output time instead. We allow arbitrary filters in the stated Banach space, not only filters sampled from the original family. Finite partitions use intervals; endpoint values do not affect operators. Output is on all of \(\mathbb R\) unless a window \(J\) is explicitly named. Truncating output changes the column norm and can hide kernel differences.

For a Banach space \(B\), a strongly measurable family \(f:I\to B\) is **essentially regulated** on compact \(I=[a,b]\) if the essential norm limits \(f(x-)\), \(f(x+)\) exist at all interior points and the appropriate one-sided limits exist at the endpoints. Thus the limit is in norm, not weak convergence or convergence in measure. A pointwise regulated representative may be selected, but values on null sets are immaterial here.

## 1. Exact deterministic norms

### Theorem 1 (column and row norms; Schur estimate)

Let \(e_\tau=w_\tau-s_\tau\) and \(K_e(t,\tau)=e_\tau(t-\tau)\). Suppose the required measurability holds. Set

\[
 A=\mathop{\rm ess\,sup}_{\tau\in I}\int_{\mathbb R}|K_e(t,\tau)|\,dt
   =\mathop{\rm ess\,sup}_{\tau\in I}\|e_\tau\|_1,
\quad
 D=\mathop{\rm ess\,sup}_{t\in\mathbb R}\int_I|K_e(t,\tau)|\,d\tau.
\]

If \(A<\infty\), then \(\|T_e\|_{L^1(I)\to L^1(\mathbb R)}=A\). If \(D<\infty\), then \(\|T_e\|_{L^\infty(I)\to L^\infty(\mathbb R)}=D\). If both are finite, for \(1\le p\le\infty\),

\[
 \|T_e\|_{p\to p}\le A^{1/p}D^{1-1/p}.                 \tag{1.1}
\]

In particular the Schur constant for \(p=2\) is \(\sqrt{AD}\). A uniform \(L^1\) bound on the columns alone must not be substituted for \(D\).

**Proof.** Tonelli and the triangle inequality give the two upper bounds. For the first lower bound put \(v(\tau)=K_e(\cdot,\tau)\in L^1(\mathbb R)\). It is strongly measurable and locally Bochner integrable. The differentiation theorem for Bochner integrable functions follows by approximation by continuous functions in local \(L^1\), the scalar maximal inequality and completeness; consequently, at almost every \(\tau_0\), the normalized averages of \(v\) on intervals shrinking to \(\tau_0\) converge to \(v(\tau_0)\) in \(L^1\). These averages are \(T_e\) applied to inputs of norm one. Hence \(\|T_e\|\ge\|v(\tau_0)\|_1\) almost everywhere, proving equality. This argument requires only Bochner integrability, not a Radon–Nikodym property of the range Banach space.

For the row lower bound, a countable set of simple bounded functions on \(I\), with rational endpoints and rational complex phases, is norming for \(L^1(I)\): for every \(q\in L^1(I)\), the supremum of \(|\int qr|\) over this set equals \(\|q\|_1\). This follows by approximating the conjugate phase of \(q\) in \(L^1(|q|d\tau)\), first truncating \(I\) when necessary. Supremum over this countable family commutes with essential supremum in \(t\). Thus \(D\le\sup_r\|T_er\|_\infty\). For \(1<p<\infty\), weighted Hölder gives
\(|T_er(t)|^p\le (\int|K_e(t,\tau)|d\tau)^{p-1}\int|K_e(t,\tau)||r(\tau)|^pd\tau\).
Integration proves (1.1). Constant nonnegative convolution kernels on the full line make the endpoint bounds and Schur coefficient sharp. ∎

**Important nonimplication.** Let \(I=[0,1]\), \(0<\delta<1\), and \(e_\tau(u)=\delta^{-1}1_{[0,\delta]}(u+\tau)\). Then every column has norm one, while \(T_er(t)=\delta^{-1}1_{[0,\delta]}(t)\int_0^1r\), so \(D=1/\delta\) and \(\|T_e\|_{2\to2}=1/\sqrt\delta\). Small column errors alone do not control the other norms uniformly across systems.

If \(|e_\tau(u)|\le\eta q(u)\) with \(q\in L^1\), then \(A,D\le\eta\|q\|_1\), hence \(\|T_e\|_{p\to p}\le\eta\|q\|_1\) for every \(p\). This is one useful, explicitly stronger filter norm: \(\|h\|_{B_q}=\operatorname{ess\,sup}_u|h(u)|/q(u)\), on functions vanishing where \(q=0\).

## 2. Necessary and sufficient uniform approximability

### Theorem 2 (regulated-function characterization)

For strongly measurable \(f:[a,b]\to B\), the following are equivalent:

1. For every \(\varepsilon>0\), there is a finite interval-step function \(s\) with \(\operatorname{ess\,sup}\|f-s\|_B<\varepsilon\).
2. \(f\) is essentially regulated.

Equivalently, \(f\) has a regulated representative modulo a null set. In the pointwise version, step functions may assign separate values at their finitely many endpoints. This is the classical regulated-function theorem: Dieudonné, *Foundations of Modern Analysis* (1960), §7.6, Theorem (7.6.1), p139. The original theorem and complete proof have been read in the scan saved as `sources/dieudonne-theorem-156.png`; p140 is also saved. The proof below supplies the essential-norm adaptation rather than importing the pointwise result on authority.

**Proof of 1 ⇒ 2.** Fix a point and a side. For any \(\varepsilon>0\), a step approximant of error \(<\varepsilon/3\) is constant on a sufficiently short interval on that side. Outside its null exceptional set, the oscillation of \(f\) on that interval is \(<2\varepsilon/3\). For a countable sequence \(\varepsilon_n\downarrow0\), remove the union of exceptional null sets and choose any sequence approaching the point from that side outside this union. Its values are Cauchy, with a common limit independent of the sequence. Completeness supplies the limit, and the same oscillation estimate proves it is the essential norm limit.

**Proof of 2 ⇒ 1.** Fix \(\varepsilon>0\). At every point \(x\), choose an open neighborhood \(U_x\) on whose left and right halves the essential oscillation is less than \(\varepsilon\). The neighborhoods cover the compact interval. Choose a finite subcover and a Lebesgue number \(\lambda>0\). Make a finite partition containing all selected centers and with mesh smaller than \(\lambda\). Each partition cell lies in one selected neighborhood, and, since its center is a partition point, lies entirely to one side of that center. Its essential oscillation is \(<\varepsilon\). Select a value from outside its exceptional set as its step value. This gives error \(\le\varepsilon\); starting with \(\varepsilon/2\) gives the strict requested bound. One-sided limits can be used to define a regulated representative; alternatively, common-null-set uniform convergence of step approximants constructs it directly. ∎

### Corollary 2A (the exact book-operator reading in \(L^1\))

For \(w\in L^\infty(I;L^1(\mathbb R))\) on finite \(I\), arbitrary-accuracy finite input-piecewise-LTI approximation in \(L^1\to L^1\) holds **if and only if** \(\tau\mapsto w_\tau\) is essentially regulated in \(L^1\). This follows by the equality in Theorem 1, with no loss of constants.

For \(B_q\), regulatedness is equivalent to approximation in the stronger filter norm \(L^\infty(I;B_q)\); it is sufficient, **not asserted necessary**, for all \(L^p\) operator norms. The theorem is not a necessary-and-sufficient theorem for arbitrary \(L^2\to L^2\) or \(L^\infty\to L^\infty\) kernels.

### Theorem 3 (infinite horizons)

Let \(f:\mathbb R\to B\) be essentially bounded.

* Uniform approximation on all \(\mathbb R\) by steps with **finitely many** intervals, including the two unbounded tails, holds iff \(f\) is locally essentially regulated and has essential norm limits at both \(+\infty\) and \(-\infty\).
* Uniform approximation on all \(\mathbb R\) by steps whose partition is **locally finite** holds iff \(f\) is locally essentially regulated.

The corresponding half-line result has just the one infinite endpoint.

**Proof.** Finite step approximants have constant tails; the same Cauchy-oscillation argument proves existence of the two tail limits. Local regulatedness follows by restriction. Conversely, approximate the tails by their limits, and apply Theorem 2 to the intervening compact interval. For locally finite partitions, restriction proves necessity; for sufficiency apply Theorem 2 separately on each \([n,n+1]\) with the same tolerance and take the union of all the finite partitions. A compact set intersects only finitely many such cells. ∎

For example \(f(\tau)=\sin\tau\,g\), \(g\ne0\), admits the latter approximations but not the former. A bounded family \(\sin(1/(\tau-a))g\) near an interior point fails both local uniform notions. These are genuine obstructions, not failures of a proposed algorithm.

## 3. Optimal segmentation when the system is known

### Theorem 4 (optimal segment count and best \(k\)-segment error)

For an interval \(H\), define its best constant-filter error
\[
 R(H)=\inf_{c\in B}\operatorname{ess\,sup}_{t\in H}\|f(t)-c\|_B. \tag{3.1}
\]
For a finite sampled sequence replace essential supremum by maximum. Use arbitrary centers; restricting centers to sampled filters changes the optimization problem. The elementary lower bound is half the essential diameter; the upper bound is the essential diameter. In a general Banach space the two need not coincide.

**Finite grid.** Assume the interval feasibility oracle says whether there **exists** a center of error \(\le\varepsilon\). Taking the longest feasible prefix, then repeating, gives the minimum number of contiguous segments. This holds in every metric space for which the stated oracle is exact. For best worst-case error with exactly \(k\) nonempty segments, writing \(R(i,j)\) for the interval radius,
\[
 E(1,j)=R(1,j),\quad
 E(k,j)=\min_{k-1\le i<j}\max\{E(k-1,i),R(i+1,j)\}.       \tag{3.2}
\]
The values are infima if centers fail to attain their infimum. Given the \(O(n^2)\) interval costs, this recurrence takes \(O(kn^2)\) comparisons and \(O(kn)\) storage (or \(O(n)\) values if no backtracking is required). It optimizes the specified uniform filter error, not a likelihood or the exact \(L^2\) operator error.

**Continuous interval.** Suppose \(B\) is reflexive (in particular, a Hilbert space), \(f\) is bounded and essentially regulated, and \(\varepsilon>0\). With \(R((x,y))\le\varepsilon\) as feasibility, the farthest feasible endpoint exists. The continuous longest-prefix algorithm terminates and minimizes segment count. The best-error value has the Bellman recurrence
\[
 E_k(b)=\inf_{a=x_0<\cdots<x_k=b}\max_jR((x_{j-1},x_j)),
\quad
 E_k(b)=\inf_{a<c<b}\max\{E_{k-1}(c),R((c,b))\},        \tag{3.3}
\]
with the natural admissibility restriction to \(k-1\) nonempty preceding intervals. Equation (3.3) is a value identity, **not** a finite-time algorithm for an arbitrary black-box continuous kernel. On a finite candidate grid it is the actual algorithm (3.2).

**Proof.** Feasibility is hereditary under taking subintervals. Let greedy endpoints be \(g_j\), and those of any feasible comparison partition be \(p_j\). Inductively \(g_j\ge p_j\): if \(g_{j-1}<p_j\), then \((g_{j-1},p_j)\) is a subinterval of the comparison interval \((p_{j-1},p_j)\) and is feasible; if \(g_{j-1}\ge p_j\), the conclusion is immediate. Thus greedy needs no more segments than any comparison partition. In the continuous case, a finite feasible partition exists by Theorem 2. Radius infima for a bounded set in a reflexive space are attained: restrict candidate centers to a sufficiently large closed ball, use weak compactness and the weak lower semicontinuity of each distance constraint. If feasible endpoints increase to \(y\), these closed convex constraint sets are nested in that ball and have nonempty intersection, which proves feasibility at \(y\); the constraints are interpreted outside the union of countably many null sets. Consequently the farthest endpoint exists. Regulatedness gives positive progress, and the dominance argument against the finite feasible partition proves termination. Finally split any partition at its last cut to get the lower bound in (3.2)–(3.3); concatenating nearly optimal subpartitions and centers proves the reverse bound. ∎

**Computability limit.** No finitely sampled black-box algorithm can certify a uniform error for every continuous kernel without a supplied modulus: after its last query insert a continuous spike supported in a query-free interval. The samples are unchanged but the uniform error can be arbitrarily large. This explains the oracle/modulus requirement; it is not an unsolved algorithmic step disguised as an oracle.

## 4. Quantitative and sharp bounds

### Theorem 5 (modulus, Lipschitz and bounded variation)

Let \(f:[a,b]\to B\), \(T=b-a\), and let \(e_k(f)\) be the infimum uniform essential error over at most \(k\) interval pieces and arbitrary centers.

1. If \(\omega(\delta)=\sup_{|s-t|\le\delta}\|f(s)-f(t)\|\), sampling at cell midpoints on a uniform \(k\)-partition gives
\(e_k(f)\le\omega(T/(2k))\). For \(L\)-Lipschitz families this is \(LT/(2k)\), and the coefficient \(1/2\) and rate are sharp.
2. For a \(B\)-valued bounded-variation representative with total variation \(V\),
\[
 e_k(f)\le {V\over2k}.                                  \tag{4.1}
\]
This coefficient is also sharp, even for real continuous monotone functions. No assumption that all jumps are smaller than the tolerance is needed; partition cuts may be placed at jumps.

**Proof.** The midpoint is at distance at most \(T/(2k)\) from every point in its cell. For sharpness take \(f(t)=L(t-a)v\), \(\|v\|=1\). One of \(k\) cells has length at least \(T/k\), and the triangle inequality forces its approximation radius to be at least half its endpoint distance, \(LT/(2k)\).

For (4.1), set \(v(t)=\operatorname{Var}(f;[a,t])\). For \(s<t\), \(\|f(t)-f(s)\|\le v(t)-v(s)\). Hence the assignment \(F(v(t))=f(t)\) is well-defined and 1-Lipschitz on its domain in \([0,V]\). Extend it continuously to the closure of that domain, and linearly over each complementary open interval. This extension remains 1-Lipschitz: for points in different intervals split the connecting interval at its endpoints and add the distance estimates. Divide \([0,V]\) into \(k\) equal bins and use as centers \(F((j-1/2)V/k)\). Because \(v\) is nondecreasing, the inverse images of bins are ordered intervals; discard empty bins and ignore singleton boundary exceptions. The resulting interval-step approximant has error at most \(V/(2k)\). If endpoint assignment produces an isolated point, it is irrelevant in the essential norm. The affine example with variation \(V\) proves sharpness. For \(V=0\) the claim is immediate. ∎

These exact constants transfer to \(L^1\to L^1\) when \(B=L^1\), to the coupling metric of §7 when \(B=L^2\), and to every \(L^p\) via the envelope norm with the extra factor \(\|q\|_1\). They do not automatically transfer to the exact \(L^2\) operator norm.

## 5. Input-specific and mean-square-energy readings

### Theorem 6 (weighted integral approximation)

Let \(r\in L^1(I)\) on a finite or infinite interval and suppose \(w:I\to L^1(\mathbb R)\) is strongly measurable with
\(\int_I|r(\tau)|\|w_\tau\|_1d\tau<\infty\).
Then there are finite interval-step filters \(s_n\) such that
\[
 \|T_wr-T_{s_n}r\|_1
 \le\int_I|r(\tau)|\|w_\tau-s_{n,\tau}\|_1d\tau\longrightarrow0. \tag{5.1}
\]
No regulatedness is needed. The coefficient one is sharp for nonnegative errors and input.

**Proof.** Interval-step functions are dense in the Bochner space \(L^1(I,|r|d\tau;L^1)\). To see this, first approximate by simple Banach-valued functions and truncate their domain to a compact interval. The finite measure \(|r|d\tau\) is regular, so each measurable set is approximable in measure by finite unions of intervals. This approximates the simple functions in the Bochner norm. Set the step function to zero on the remaining tails. Tonelli proves (5.1). ∎

### Theorem 7 (why output-only input-specific accuracy is almost vacuous)

Fix a nonzero \(r\in L^1(I)\), where \(I\) has nonempty interior, and a target \(y\in L^p(\mathbb R)\), \(1\le p<\infty\). There are input-piecewise-LTI operators with at most **three** interval pieces and filters in \(L^1(\mathbb R)\) whose outputs on this one \(r\) converge to \(y\) in \(L^p\). If \(r=0\), only the zero output is approximable. No operator-uniform approximation or uniformly bounded filter norms is asserted.

**Proof.** Choose an interior Lebesgue point \(\tau_0\) of \(r\) with \(r(\tau_0)\ne0\). On shrinking intervals \(H_h\) about it, \(m_h=\int_{H_h}r\ne0\) for small \(h\), and the signed/complex measures \(d\mu_h=r1_{H_h}d\tau/m_h\) have total mass one, uniformly bounded total variation, and supports shrinking to \(\tau_0\). First let \(y\in C_c^\infty\) and put \(g_h(u)=y(u+\tau_0)/m_h\) on the middle input segment, with zero filters on the left and right. Its output is \(y(\cdot+\tau_0)*\mu_h\). Its difference from \(y\) has norm at most
\(\|\mu_h\|_{\rm TV}\sup_{\tau\in H_h}\|y(\cdot+\tau_0-\tau)-y\|_p\), which tends to zero by continuity of translations. For general \(y\in L^p\), approximate it by \(C_c^\infty\) targets and choose \(h\) successively small. Each \(g_h\) belongs to \(L^1\). The zero-input assertion is linearity. ∎

Thus a meaningful physical input-specific requirement must also constrain the filters, their gain, their distance from \(w\), or their construction from data. The theorem is an exact answer to the unrestricted output-only reading, not a solution of blind deconvolution.

### Theorem 8 (finite-energy kernels and \(L^2\))

If \(w\in L^2(I;L^2(\mathbb R))\), finite interval-step filters, zero on unbounded tails, can approximate it in this Bochner norm. Moreover
\[
 \|T_w-T_s\|_{2\to2}\le\|T_w-T_s\|_{\rm HS}
 =\left(\int_I\|w_\tau-s_\tau\|_2^2d\tau\right)^{1/2}.     \tag{5.2}
\]
For standard real white noise \(Z\),
\[
 \mathbb E\|T_wZ-T_sZ\|_{L^2(\mathbb R)}^2
 =\int_I\|w_\tau-s_\tau\|_2^2d\tau.                    \tag{5.3}
\]

**Proof.** Density follows as in Theorem 6 with Lebesgue measure and squared norm, using domain and value truncation. The substitution \(u=t-\tau\) identifies the square-integrable integral kernel and its Hilbert–Schmidt norm. Cauchy–Schwarz gives the operator bound; expand white noise in any orthonormal basis and apply Parseval/Itô isometry to obtain (5.3). ∎

In this finite-energy class **every** strongly measurable kernel is approximable; discontinuities need not have one-sided limits. Thus essential regulatedness is not necessary for \(L^2\to L^2\) approximation. For instance \(w_\tau=\sin(1/(\tau-a))g\) on a bounded interval, \(g\in L^1\cap L^2\), is approximable by (5.2) but fails Corollary 2A. This is a full characterization in the declared finite-energy class, not in the class of all bounded \(L^2\) integral operators.

## 6. Explicit constant-Q rates, and the separate Gabor remainder

### Theorem 9 (constant-Q transfer family)

Use the Fourier convention \(\widehat h(f)=\int h(u)e^{-2\pi ifu}du\). Work on a finite observed frequency band \(F\subset(0,\infty)\), or include its conjugate-reflected negative-frequency band for real signals. Book equation (3) is written \(\alpha_Q(\tau,f)=\exp[-\pi f\tau/Q+iH(\pi f\tau/Q)]\). The damping term must be interpreted on positive frequencies (or with \(|f|\) on the full real line). The literal all-real-frequency expression without an absolute value is not a globally decaying transfer function. The book does not specify the normalization/regularization of the Hilbert-transform phase; we do not silently supply one.

Fix a real measurable phase function \(b(f)\), independent of \(\tau\), on the positive band and set
\[
 a(f)=\pi f/Q-i b(f),\quad \widehat w_\tau(f)=W_0(f)e^{-\tau a(f)},\quad \tau\in[\tau_0,\tau_0+T],\quad \tau_0\ge0.
\]
Assume \(Q>0\), \(W_0\in L^2\) is supported in \(F=[f_{\min},f_{\max}]\), \(f_{\min}>0\), and \(A=\operatorname{ess\,sup}_F|a|<\infty\). For real signals extend by \(a(-f)=\overline{a(f)}\), \(W_0(-f)=\overline{W_0(f)}\), and take all \(L^2\) norms over both bands; thus \(\operatorname{Re}a(f)=\pi|f|/Q\) on that extension. Identifying this family with the book's exact \(\alpha_Q\) additionally requires a declared interpretation of \(H\) satisfying \(e^{i\tau b(f)}=e^{iH(\pi f\tau/Q)}\) on the observed band for every relevant \(\tau\). The bounds are conditional on this compatibility when used for the printed model. Set \(c=\pi f_{\min}/Q>0\) and \(M=\|W_0\|_2\). Then
\[
 \|w_\tau-w_\sigma\|_2\le A M e^{-c\min(\tau,\sigma)}|\tau-\sigma|,
\quad
 e_k(w;L^2)\le {AMe^{-c\tau_0}T\over2k}.              \tag{6.1}
\]
A variation-adapted partition improves the latter to
\[
 e_k\le {AM\over2kc}\big(e^{-c\tau_0}-e^{-c(\tau_0+T)}\big). \tag{6.2}
\]
On \([\tau_0,\infty)\), include the terminal zero filter; the family tends to zero in \(L^2\) and is finite-step uniformly approximable. Equations (6.1)–(6.2) are filter-\(L^2\) bounds; (5.2) yields \(L^2\) operator error at most \(\sqrt T\,e_k\) on the finite input interval and (5.3) gives root mean-square energy error at most the same quantity.

If also \(W_0\in H^1(\mathbb R)\) with compact support inside the band and \(a\) is \(C^1\) on a neighborhood of that support, define the explicit finite constant
\[
 M_1=\sqrt\pi\sup_{\tau\in[\tau_0,\tau_0+T]}
 \left(\|aW_0e^{-\tau a}\|_2^2+(2\pi)^{-2}
 \|\partial_f(aW_0e^{-\tau a})\|_2^2\right)^{1/2}.       \tag{6.3}
\]
Then \(\|w_\tau-w_\sigma\|_1\le M_1|\tau-\sigma|\), and the exact \(L^1\to L^1\) approximation error is at most \(M_1T/(2k)\). In (6.3),
\(\partial_f(aW_0e^{-\tau a})=[a'W_0+aW_0'-\tau a a'W_0]e^{-\tau a}\), so every constant is computable from the declared wavelet, phase, band and Q.

**Proof.** Differentiate the transfer function in \(\tau\). Plancherel gives \(\|\partial_\tau w_\tau\|_2\le AM e^{-c\tau}\); integration and Theorem 5 give (6.1)–(6.2). Exponential decay proves the infinite-tail assertion. For any \(G\in H^1\), Cauchy–Schwarz with weight \(1+u^2\) and Plancherel give
\(\|\check G\|_1\le\sqrt\pi(\|G\|_2^2+(2\pi)^{-2}\|G'\|_2^2)^{1/2}\).
Apply this to \(G=aW_0e^{-\tau a}\), and integrate the derivative in \(L^1\). ∎

**Matching order.** A universal improvement from \(k^{-1}\) to \(o(k^{-1})\) for nontrivial constant-Q families is impossible. If \(\partial_\tau w_{\tau_*}=v\ne0\) in \(L^2\), choose a real continuous linear functional \(\ell\) of norm one with \(\ell(v)=\|v\|\) (realify a complex Hilbert space). Continuity of the derivative gives a subinterval of length \(L>0\) on which \(\ell(\partial_\tau w_\tau)\ge\|v\|/2\). Some one of at most \(k\) pieces meets that interval in length at least \(L/k\), so its radius is at least \(\|v\|L/(4k)\). This matches the order, not the upper constant for every wavelet. Here \(v\ne0\) when \(aW_0\ne0\).

### Theorem 10 (a direct, explicit Gabor-factorization remainder)

This theorem separates the book's approximation (5) from piecewise freezing. Suppose all integrals below are absolutely convergent. Let \(g\) be a bounded Lipschitz analysis window with constant \(L_g\). At window center \(x\), choose a reference filter \(h=w_x\). Then
\[
 |V_g(T_wr)(x,f)-\widehat h(f)V_gr(x,f)|
 \le \|g\|_\infty\int_I|r(\tau)|\|w_\tau-h\|_1d\tau
 +L_g\|r\|_1\int |u|\,|h(u)|du.                       \tag{6.4}
\]
A sharper local first term is \(\int |r(\tau)|\int|w_\tau(u)-h(u)|\,|g(\tau+u-x)|du\,d\tau\).

**Proof.** Substitute \(t=\tau+u\) in the STFT integral. Subtract the claimed product and add/subtract \(h(u)\overline{g(\tau+u-x)}\). The two resulting factors are respectively \(w_\tau-h\) and \(h(u)[\overline{g(\tau+u-x)}-\overline{g(\tau-x)}]\); take absolute values and use the window Lipschitz bound. ∎

For the exponential attenuation family, \(\widehat h=W_0e^{-x a}\); this equals \(W_0\alpha_Q(x,\cdot)\) only under Theorem 9's explicit phase-compatibility convention. The first term is a local system-variation error; the second is a window/filter commutator. Neither is zero merely because the system varies slowly in \(\tau\). There is a time/frequency localization trade-off, and no universal numerical remainder follows from Q alone without specifying the wavelet and window. Formula (6.4) does not assert that a fixed window gives a vanishing error as the segmentation mesh tends to zero.

## 7. Stochastic stationarity, metrics and non-equivalence

White noise means a real isonormal Gaussian random measure on \(L^2(\mathbb R)\); complex versions can be obtained by two real copies. Only filters with the stated square integrability are admitted. In Theorem 12 and its row-family consequences, take the input domain to be the full line. A finite-input-domain model is included by first setting \(w_\tau=0\) outside \(I\); equivalently its row is \(g_t(u)=1_I(t-u)w(t-u,u)\). The output-frozen stationary comparison process uses full-line white noise, so this convention does not pretend that zero-truncating a stationary input preserves stationarity.

### Theorem 11 (coupling, covariance and Wasserstein bounds)

On a finite output window \(J\), let the integral maps \(T_w,T_s:L^2(I)\to L^2(J)\) be Hilbert–Schmidt. Write \(\eta=\|T_w-T_s\|_{\rm HS}\), \(C_w=T_wT_w^*\), \(C_s=T_sT_s^*\). Under the same driving white noise,
\[
 \mathbb E\|Y_w-Y_s\|_{L^2(J)}^2=\eta^2,
\quad W_2(\mathcal L(Y_w),\mathcal L(Y_s))\le\eta,
\]
\[
 \|C_w-C_s\|_{\rm op}
 \le(\|T_w\|_{\rm op}+\|T_s\|_{\rm op})\|T_w-T_s\|_{\rm op}
 \le(2\|T_w\|_{\rm op}+\eta)\eta.                    \tag{7.1}
\]

**Proof.** The first equality is Itô isometry and Tonelli. This is one admissible coupling, so the infimum defining quadratic Wasserstein distance is no larger. Expand
\(C_w-C_s=(T_w-T_s)T_w^*+T_s(T_w-T_s)^*\), take norms, and use \(\|T_s\|\le\|T_w\|+\eta\). ∎

These bounds justify coupling/energy and covariance metrics: they control linear measurements of the trace and provide an explicit distributional metric on the entire finite window. They do not imply a Hellinger bound, which can fail without nondegeneracy and additional spectral assumptions.

### Theorem 12 (an exact piecewise-stationary characterization)

Use the **output-indexed** family
\(g_t(u)=w(t-u,u)\), so \(Y(t)=\int g_t(t-\tau)dZ(\tau)\).
Assume \(t\mapsto g_t\) is strongly measurable and essentially bounded in \(L^2(\mathbb R)\) on a finite output interval \(J\). For a finite partition of \(J\), put
\(\widetilde Y(t)=\int h_j(t-\tau)dZ(\tau)\) on its \(j\)-th interval.
Each piece is the restriction of a stationary Gaussian moving average; pieces may be dependent across boundaries. In the stated, driver-preserving uniform RMS metric,
\[
 d_*(Y,\widetilde Y)=\operatorname{ess\,sup}_{t\in J}
   (\mathbb E|Y(t)-\widetilde Y(t)|^2)^{1/2}
 =\operatorname{ess\,sup}_{t\in J}\|g_t-h_{j(t)}\|_2.   \tag{7.2}
\]
Arbitrary-accuracy finite-piece approximation in this metric holds iff \(g\) is essentially regulated in \(L^2\). Theorems 3–5 apply verbatim, including sharp rates and optimal greedy segmentation. Furthermore \(W_2\) on \(L^2(J)\) is at most \(\sqrt{|J|}d_*\), and if \(\sup_t\|g_t\|_2\le M\), then
\[
 \operatorname{ess\,sup}_{t,s\in J}|C_Y(t,s)-C_{\widetilde Y}(t,s)|
 \le (2M+d_*)d_*,\quad
 \|C_Y-C_{\widetilde Y}\|_{\rm op}\le |J|(2M+d_*)d_* . \tag{7.3}
\]

**Proof.** White-noise isometry and translation invariance give (7.2). Theorem 2 gives the iff. Constant \(h_j\) yields covariance depending only on time lag inside a piece; Gaussianity then gives stationarity of all within-piece finite-dimensional distributions. Integrate (7.2) for Wasserstein. For covariance write the difference of inner products of the two row kernels, apply Cauchy–Schwarz and \(\|\widetilde g_t\|_2\le M+d_*\). The integral-operator norm bound follows by the row/column Schur bound on \(J\). ∎

A sufficient condition directly on the book kernel is
\(|w(\tau,u)-w(\sigma,u)|\le L(u)|\tau-\sigma|\) for almost every \(u\), all \(\tau,\sigma\), with \(L\in L^2\), together with one square-integrable row. Then \(\|g_t-g_s\|_2\le\|L\|_2|t-s|\), giving \(d_*\le\|L\|_2|J|/(2k)\). Input-column \(L^2\) continuity alone is not this pointwise envelope assumption.

### Theorem 12A (a representation-invariant uniform covariance characterization)

Keep Theorem 12's strongly measurable, essentially bounded row family on compact \(J\). For two covariance functions define
\[
 d_{\rm cov}(C,\widetilde C)=\max\left\{
 \operatorname{ess\,sup}_{t\in J}|C(t,t)-\widetilde C(t,t)|,\
 \operatorname{ess\,sup}_{(t,s)\in J^2}|C(t,s)-\widetilde C(t,s)|
 \right\}.                                             \tag{7.4}
\]
The diagonal is included explicitly because a two-dimensional essential supremum alone does not prescribe values on a null diagonal. Arbitrarily small \(d_{\rm cov}\) approximation by finite piecewise-stationary Gaussian laws whose within-piece covariance functions are continuous holds **if and only if** \(g\) is essentially regulated in \(L^2\). This criterion is about the covariance law, not a fixed choice of coupling. Allowed approximants need not be driven by the same noise for the necessity direction.

**Proof.** Sufficiency is Theorem 12, including the identical bound for the diagonal. For necessity write \(v_t(\tau)=g_t(t-\tau)\), so \(C(t,s)=\langle v_t,v_s\rangle\). Fix a point \(x\), a side, and \(\delta>0\). Choose a piecewise-stationary covariance approximant of error at most \(\delta\). On a sufficiently short interval on that side of \(x\) there is no interior partition boundary, so its covariance is \(R_j(t-s)\), with constant variance \(R_j(0)\). For almost every pair \(t,s\) in this interval,
\[
 \|v_t-v_s\|_2^2
 =C(t,t)+C(s,s)-2\operatorname{Re}C(t,s)
 \le 2\{R_j(0)-\operatorname{Re}R_j(t-s)\}+4\delta .
\]
Continuity of \(R_j\) at zero makes the first term arbitrarily small by shortening the interval. Letting \(\delta\downarrow0\) shows that the essential pairwise diameter of \(v_t\) on one-sided neighborhoods tends to zero. For completeness, an a.e.-pair diameter bound yields an essential ball bound: by Fubini choose one \(s\) whose distances to almost all \(t\) satisfy it. On nested neighborhoods these chosen centers are Cauchy by taking a point in their full-measure intersection. Completeness therefore gives an essential one-sided limit \(v_{x\pm}\). Finally \(g_t=U_t v_t\), where \((U_t v)(u)=v(t-u)\). The isometries \(U_t\) are strongly continuous in \(t\), since translations are strongly continuous on \(L^2\). Thus \(g_t\to U_xv_{x\pm}\) essentially on that side. This proves essential regulatedness. ∎

The metric (7.4) controls every local variance and every pairwise covariance, whereas covariance **operator** norm allows errors concentrated on short time sets. These are different readings. The characterization in (7.4) does not by itself provide an optimal segmentation algorithm in that metric; Theorem 4 optimizes the stronger filter/coupling tolerance.

### Theorem 12B (all finite-energy rows admit finite-window Wasserstein approximation)

If \(g\in L^2(J;L^2(\mathbb R))\), there are finite interval-step \(s_n(t)=h_{n,j(t)}\) such that the associated piecewise-stationary moving averages converge to \(Y\) in \(W_2\) on \(L^2(J)\) and in covariance-operator norm. No regulatedness or continuity is required.

**Proof.** Bochner interval-step density gives \(\int_J\|g_t-s_n(t)\|_2^2dt\to0\), by the argument of Theorem 8. The shared-noise coupling has exactly this integrated mean-square error. Apply Theorem 11 to the row kernels \(v_t(\tau)=g_t(t-\tau)\). ∎

Thus in the declared finite-second-moment \(L^2(J)\)-valued Gaussian class there is no further regularity obstruction for these weaker metrics. Finite energy is exactly \(\mathbb E\|Y\|_{L^2(J)}^2<\infty\), the second-moment condition defining this Wasserstein space. This is not a uniform error theorem, a fixed-segment-count theorem, or a guarantee that each statistical segment contains enough observations.

### Counterexample 13 (input-piecewise LTI does not mean piecewise stationary)

On the full line let \(w_\tau(u)=a(\tau)1_{[0,1]}(u)\), where \(a(\tau)=1\) for \(\tau<0\) and \(a(\tau)=2\) for \(\tau\ge0\). This is exactly a two-piece input-LTI kernel. Nevertheless
\[
 \operatorname{Var}Y(t)=\int_{t-1}^t a(\tau)^2d\tau
 =\begin{cases}1&t\le0,\\1+3t&0<t<1,\\4&t\ge1.\end{cases}
\]
No nonempty open subinterval of \((0,1)\) is stationary because its variance varies. Thus no finite partition makes this output exactly piecewise stationary on a window containing \((0,1)\), although arbitrarily accurate approximations in Theorem 12's metric exist. This separates the exact model classes; it does **not** refute an equivalence of suitably specified arbitrary-accuracy approximation properties. The book says the question can alternatively be formulated in output terms; to make that mathematically precise one must specify both metrics and boundary treatment.

### Counterexample 14 (input-column ambiguity and weaker covariance metrics)

Let \(\sigma(\tau)\in\{-1,1\}\) be measurable and \(w_\tau(u)=\sigma(\tau)h(u)\), \(0\ne h\in L^2\). The transformed random measure \(dZ'=\sigma dZ\) is white noise, so \(Y\) has exactly the stationary law of \(h*Z\). Taking \(\sigma=\operatorname{sign}\sin(1/\tau)\) near zero makes the **input-column** family nonregulated. This refutes necessity of input-column regulatedness for stationary output laws, not necessity of output-row regulatedness. Indeed \(g_t(u)=\sigma(t-u)h(u)\) is continuous in \(L^2\): first approximate \(|h|^2\) by bounded compactly supported functions, then use local \(L^2\) translation continuity of the bounded measurable \(\sigma\); the discarded tails are bounded by \(4\int_{\rm tail}|h|^2\).

For a different example put \(g_t=\sigma(t)h\) on \(J=[0,1]\), with the same oscillatory \(\sigma\). This **row** family is not essentially regulated at zero, so Theorems 12 and 12A exclude arbitrary uniform-RMS and uniform-covariance approximation. Nevertheless it has finite energy and is approximable in \(W_2(L^2(J))\) and covariance-operator norm by Theorem 12B. This is the precise nonnecessity statement for the weaker metrics; it does not include (7.4).

## 8. The three extension questions: what is and is not identifiable

### Proposition 15 (slow/fast amplitude separation is not identification)

Even in the stationary subclass, slow wavelet magnitude and rapidly varying reflectivity magnitude do not uniquely determine their factors from the trace magnitude. On an observed frequency band, choose positive spectra \(W,R\). For any nonconstant positive smooth \(A\),
\(W' =WA\), \(R'=R/A\) gives exactly the same product. For a quantitative example on a fixed band take \(W=1\), \(\log R=b\cos(Nf)\), and \(\log A=\epsilon(\cos f-1)\). Both \(W,W'\) have arbitrarily small logarithmic slope by choosing \(\epsilon\) small; both reflectivity log-magnitudes contain the same arbitrarily rapid oscillation as \(N\to\infty\). Also \(A(0)=1\), so even a normalization at zero frequency does not resolve this ambiguity. Extend spectra smoothly outside the observed band as needed; equality on the band is sufficient to defeat unique band-limited recovery. Taking real even spectra gives real signals. Thus §4(1)'s qualitative assumptions cannot guarantee exact amplitude correction. A probabilistic whiteness model, calibrated source, minimum-phase convention and/or explicit regularization supplies genuinely additional information, not a logical consequence of “slow” and “fast”. ∎

### Proposition 16 (a known initial wavelet is a boundary value, not a modulus)

Knowing \(w_0=h\) alone imposes no finite uniform segmentation bound on later filters. The families \(w_\tau=h+A\phi(\tau)v\), where \(\phi(0)=0\) and \(v\ne0\), share the same initial wavelet but can have arbitrarily large amplitude and arbitrarily many alternating excursions, even with smooth \(\phi\). If successive extrema differ by \(>2\varepsilon\), no error-\(\varepsilon\) constant cell may contain both; arbitrarily many excursions require arbitrarily many segments. Without continuity, nonregulated families sharing \(w_0\) are not uniformly approximable at all. Moreover the exact gauge transformation \(w'_\tau=a(\tau)w_\tau\), \(r'(\tau)=r(\tau)/a(\tau)\), with \(a(0)=1\) and \(a\) bounded away from zero, preserves the entire deterministic output and its initial wavelet. Thus that datum alone cannot identify the subsequent kernel. When a known Q propagation law is added, Theorem 9 gives a real benefit: the initial wavelet fixes \(W_0\), and known Q/phase fix the whole family. ∎

### Proposition 17 (conditional Q recovery, with an explicit error bound)

In an ideal frozen-block stationary model assume positive continuous representatives of the spectral densities and a continuous nonvanishing \(W_0\) on the measured band, with the following pointwise identities (not merely arbitrary a.e. representatives):
\[
 S_j(f)=\sigma_j^2|W_0(f)|^2\exp[-2\pi f A_j],\qquad
 f\in[f_1,f_2]\subset(0,\infty),                         \tag{8.1}
\]
where \(W_0\ne0\), \(\sigma_j^2>0\) is frequency-independent (white reflectivity within each block), and \(A_j=\int_0^{\tau_j}Q(v)^{-1}dv\). For two blocks with \(\Delta\tau=\tau_2-\tau_1>0\), let \(D(f)=\log S_2(f)-\log S_1(f)\). Then
\[
 \overline{Q^{-1}}={A_2-A_1\over\Delta\tau}
 =-{D(f_2)-D(f_1)\over2\pi(f_2-f_1)\Delta\tau}.          \tag{8.2}
\]
Thus one identifies average inverse Q over this interval, not the unrestricted Q profile. If each of the four log-spectrum measurements has absolute error at most \(\delta\), then
\[
 |\widehat q-\overline{Q^{-1}}|
 \le {2\delta\over\pi(f_2-f_1)\Delta\tau}.              \tag{8.3}
\]
For constant Q, if this bound is \(\eta<q=1/Q\), the reciprocal estimate satisfies
\(|\widehat Q-Q|\le\eta/[q(q-\eta)]\).

**Proof.** Subtract the two logarithms in (8.1). The source cancels. Taking the difference at two frequencies also cancels the unknown blockwise white-noise variances. Divide by the slope coefficient to obtain (8.2). Four errors of size \(\delta\) give (8.3); elementary subtraction of reciprocals gives the final bound. ∎

Without whiteness, replace \(\sigma_j^2\) by arbitrary positive reflectivity spectra \(R_j(f)\). Any other values \(A'_j\) yield the identical observed spectra upon setting \(R'_j(f)=R_j(f)e^{-2\pi f(A_j-A'_j)}\). Q is then not identifiable from these spectra. A single finite sample does not give exact \(S_j\), and covariance-norm accuracy by itself is not a pointwise log-spectrum error bound. The book does not provide the assumptions needed to guarantee \(\delta\), an optimal statistical segment length, or a confidence interval for Q from one trace.

## 9. Reproduction of the classical locally stationary approximation rate

### Theorem 18 (explicit version of the no-overlap Ombao approximation)

Fix \(T\in\mathbb N\), \(T\ge1\), and exactly the \(T\) observation indices \(t=0,\ldots,T-1\); every maximum, supremum and sum over \(t\) below uses these indices. Let \(Z_f\) be Gaussian orthogonal-increment spectral noise on \(F=[-1/2,1/2]\) with control measure \(df\), using conjugate symmetry for real processes. Let
\[
 X_{t,T}=\int_F e^{2\pi ift}A_{t,T}(f)dZ_f,\qquad
 \sup_t\|A_{t,T}-A(t/T,\cdot)\|_{L^2(F)}\le D/T .
\]
Suppose \(u\mapsto A(u,\cdot)\) is \(L\)-Lipschitz into \(L^2(F)\). Partition \([0,1]\) into intervals of width at most \(h\) and freeze \(A\) at each midpoint \(c_j\). The resulting \(\widetilde X_{t,T}=\int e^{2\pi ift}A(c_{j(t)},f)dZ_f\) is stationary within each block and satisfies
\[
 \max_t\{\mathbb E|X_{t,T}-\widetilde X_{t,T}|^2\}^{1/2}
 \le D/T+Lh/2,\qquad
 T^{-1}\sum_t\mathbb E|X_{t,T}-\widetilde X_{t,T}|^2
 \le (D/T+Lh/2)^2.                                    \tag{9.1}
\]
For \(h=M/T\) with \(M\ge1\), this reproduces the \(O(M^2/T^2)\) order in Ombao–Raz–von Sachs–Malow, author preprint (11 May1999), Theorem 2.1, including piecewise stationary processes as its no-overlap case. The model-to-limit discrepancy \(D/T\) has not been omitted.

**Proof.** Itô isometry makes the squared error equal to \(\|A_{t,T}-A(c_{j(t)},\cdot)\|_2^2\). Apply the triangle inequality, the declared \(D/T\) bound, and \(|t/T-c_{j(t)}|\le h/2\). Take the maximum or average. A fixed transfer function on a block is a restriction of a stationary Gaussian spectral process. ∎

**Prior-art scope.** This is **Reproduction**, not Discovery. We read the original preprint theorem and appendix pp26–27 in `sources/ombao1999.txt`. Its published2001-version differences are unverified. We independently supply the short no-overlap argument, so its correctness does not rely on every inequality in the preprint's blended-overlap proof. The rate is about approximation of a known generative family, not consistency of data-selected breakpoints; the preprint's §5 Remark(6) explicitly restricts its spectral-consistency theorem to fixed segmentation.

## 10. What these proofs do not claim

* No proof that every bounded \(L^2\) or \(L^\infty\) operator admits these approximants; the exact \(L^1\) characterization, finite-energy theorem and envelope bounds have different hypotheses.
* No automatic identification of the unknown kernel, input, breakpoints or Q from a single seismic record.
* No equivalence between input freezing, output freezing, and stationary laws.
* No exact Gabor factorization, no Hellinger guarantee, and no novelty or Lean certification.
* No finite-table or dynamic-programming computation is being presented as a solution to the full book problem. The computational artifact checks only the already-proved finite-grid algorithm and exact counterexample arithmetic.
