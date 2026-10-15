# Positive time–frequency marginals: written proofs

Date: 2026-10-14 (America/Los_Angeles). All proofs below are classical written proofs; none is Lean/kernel-certified. The book's informal phrase “physical meaning” is not itself a mathematical axiom. Theorems explicitly distinguish a joint density from the more permissive joint-measure model.

## 0. Conventions and exact statements

Use the unitary Fourier transform
\[
 S(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}s(t)e^{-i\omega t}\,dt,
 \quad E=\|s\|_2^2>0,
 \quad \mu(dt)=|s(t)|^2dt/E,\quad\nu(d\omega)=|S(\omega)|^2d\omega/E.
\]
The displayed integral is the definition on \(L^1\cap L^2\); on general \(L^2\) we use its unique unitary Plancherel extension.
The book instead uses the nonunitary transform and an integration factor \(1/(2\pi)\); our normalized density is exactly its \(P/(2\pi E)\). This change has no effect on phase derivatives or existence.

A nonnegative joint distribution is a Borel probability measure \(\pi\) on \(\mathbb R^2\), with coordinate variables \(T,W\), marginals \(\mu,\nu\). A **density** additionally requires \(\pi(dt,d\omega)=p(t,\omega)dt\,d\omega\). Any nonexistence theorem for measures therefore also excludes densities. Equalities of conditional expectations hold marginal-almost everywhere, never at arbitrary zero-energy points.

For \(s\in H^1(\mathbb R)\), define
\[
 f(t)=\operatorname{Im}(\overline{s(t)}s'(t))/|s(t)|^2
\]
on \(s\ne0\), and arbitrarily on its zero set. This is \(\phi'(t)\) in any local polar representation \(s=Ae^{i\phi}\). It is \(\mu\)-integrable by Cauchy–Schwarz. The instantaneous-frequency axiom IF is \(\mathbb E[W\mid T]=f(T)\). For \(S\in H^1\), similarly define \(g(\omega)=-\operatorname{Im}(\overline S S')/|S|^2=-\psi'(\omega)\); GD is \(\mathbb E[T\mid W]=g(W)\). A complex signal is called analytic here iff its Fourier transform vanishes almost everywhere on \(( -\infty,0)\). Finite energy alone does not define a phase derivative or its moment: universal IF/GD claims are understood on the indicated regular subclasses, which already suffice to refute them.

## 1. Baseline existence, covariance, and finite support

**Theorem 1.** Every nonzero finite-energy signal has a nonnegative, marginal-correct density. One rule, simultaneously valid for all signals, also has time-shift, frequency-shift, positive scaling covariance, and strong finite support. None of these axioms, separately or jointly, imposes IF or GD.

**Proof.** Set \(p_s(t,\omega)=|s(t)|^2|S(\omega)|^2/E^2\). Tonelli and Plancherel give both normalized marginals. For \(r(t)=e^{ibt}s(t-a)\), absolute values give
\(p_r(t,\omega)=p_s(t-a,\omega-b)\). For \(r(t)=\sqrt c\,s(ct)\), \(c>0\), Fourier scaling gives \(|R(\omega)|^2=c^{-1}|S(\omega/c)|^2\), hence \(p_r(t,\omega)=p_s(ct,\omega/c)\); this is precisely pushforward by \((t,\omega)\mapsto(t/c,c\omega)\), whose Jacobian is one.

In fact **every** nonnegative marginal-correct measure has strong support: if \(\mu(A)=0\), then \(\pi(A\times\mathbb R)=0\); likewise \(\nu(B)=0\Rightarrow\pi(\mathbb R\times B)=0\). For densities this means vanishing almost everywhere over every measurable zero-energy set, including internal gaps. The weaker property “no mass outside a containing time/frequency interval” follows. Pointwise values on Lebesgue-null lines are irrelevant and can be chosen to be zero. Whenever the respective marginal has finite first moment, the product rule's conditional mean equals its unconditional mean; it need not have IF/GD. ∎

This is a reproduction of the elementary Cohen–Posch baseline already printed as equation (5) in the book. The book explicitly rejects this as a full account of local frequency content, so Theorem 1 is **not** a solution of its unrestricted physical-meaning question.

## 2. Explicit finite-energy analytic IF obstruction

**Theorem 2.** There is a finite-energy analytic signal with compact, strictly positive spectral support for which no nonnegative joint measure has both correct marginals and IF. Thus no universal rule with these three axioms exists, even allowing arbitrary nonlinear signal dependence. Adding GD, covariance or finite-support axioms cannot repair nonexistence.

**Proof.** Let
\[
 h(t)=\left({\sin(t/8)\over t/8}\right)^2,\quad h(0)=1,
 \qquad q(t)=h(t)\left(e^{it}-{3\over4}e^{2it}\right).
\]
The function \(h\) is real, smooth, \(O(t^{-2})\), and has derivative \(O(t^{-2})\); thus \(q\in H^1\), and also \(tq\in L^2\). The transform of \(\sin(t/8)/(t/8)\) is supported on \([-1/8,1/8]\). The product/convolution identity therefore puts \(\widehat h\) in \([-1/4,1/4]\). Modulation puts \(Q=\widehat q\) in
\[
 [3/4,5/4]\ \cup\ [7/4,9/4].
\]
Consequently \(q\) is analytic. It is nonzero since \(q(0)=1/4\).

Where \(h\ne0\), its logarithmic derivative is real and contributes no phase derivative. Direct multiplication yields
\[
 f_q(t)={34-36\cos t\over25-24\cos t},\qquad f_q(0)=-2.
\]
The denominator is at least one. On the interval
\(I=(-\arccos(17/18),\arccos(17/18))\), the numerator is negative, \(h\) has no zero and \(|q|>0\). Thus \(\mu(I)>0\) and \(f_q<0\) throughout \(I\).

If a nonnegative marginal-correct \(\pi\) existed, its frequency marginal would imply \(W\ge3/4\), \(\pi\)-almost surely. Conditional expectation preserves inequalities, so \(\mathbb E[W\mid T]\ge3/4\), \(\mu\)-almost everywhere. This contradicts IF on \(I\). ∎

An optional smooth-spectrum variant shows the same result within analytic Schwartz signals: choose a nonzero nonnegative, even \(H\in C_c^\infty((-1/4,1/4))\), let \(h=\mathcal F^{-1}H\), and use the same two carriers. Then \(h\) is real Schwartz with \(h(0)>0\), so the same IF formula holds on a neighborhood of zero, with the same positive spectral bands. This variant needs no numerical approximation.

**Prior-art boundary.** Loughlin–Pitton–Atlas (1994), §III-D, p.2700 explicitly states this incompatibility: analytic-signal phase derivatives can be negative, whereas nonnegative correct-marginal distributions cannot have a negative conditional mean. Loughlin–Tacer (1997), §§II–III, explains the broader out-of-band IF obstruction for unequal two-tone components. Our explicit finite-energy witness certifies that known argument without using infinite-energy pure tones; the universal obstruction is not a discovery.

## 3. GD fails universally, including on analytic signals

**Theorem 3.** There is a finite-energy analytic signal \(s\), with \(s\in H^1\) and \(ts\in L^2\), for which nonnegativity, both marginals and GD are inconsistent.

**Proof.** Reuse \(q\) from Theorem 2, but now as a function of a frequency-offset variable \(z\). Define the real \(C^1\) cutoff
\[
 \chi(u)=\begin{cases}0&u\le0,\\3u^2-2u^3&0<u<1,\\1&u\ge1.\end{cases}
\]
Then \(0\le\chi\le1\), \(|\chi'|\le3/2\). Set \(L=129\),
\[
 R_L(z)=\chi(L+z)q(z),\qquad S_L(\omega)=R_L(\omega-L),\qquad s_L=\mathcal F^{-1}S_L.
\]
This is analytic because \(S_L=0\) on negative frequencies. Its energy is finite and nonzero; \(R_L\in H^1\) and \(zR_L\in L^2\), which give \(ts_L,s_L'\in L^2\). Normalization is immaterial below because the same energy divides both sides of the necessary inequality.

Any GD coupling must satisfy conditional Jensen for \(x\mapsto x_+=\max(x,0)\):
\[
 \int g_L(\omega)_+|S_L(\omega)|^2d\omega
 \le \int t_+|s_L(t)|^2dt.\tag{3.1}
\]
We bound the left side below. On \(|z|\le1/8\), the cutoff is identically one; hence \(g_L(L+z)=-f_q(z)\). Here \(\cos z\ge1-z^2/2\ge127/128\), so
\[
 (-f_q(z))|q(z)|^2=h(z)^2{36\cos z-34\over16}
 \ge {1\over2}{55\over512}={55\over1024}.
\]
The bound \(h(z)^2>1/2\) follows from \(\sin x/x\ge1-x^2/6\) for \(|x|\le1/64\) and \((1-a)^4\ge1-4a\). Integration over an interval of length \(1/4\) gives the lower bound \(55/4096\).

For the right side, let \(d=R_L-q\), supported in \(z\le-128\), and put \(D=128\). For \(|z|\ge D\), direct differentiation of \(h(z)=64\sin^2(z/8)/z^2\) gives
\[
 |q(z)|\le112/z^2,\quad
 |q'(z)|\le188/z^2+224/|z|^3\le300/z^2.
\]
Thus \(|d|\le112/z^2\), \(|d'|\le468/z^2\), and
\[
 \|d\|_2\|d'\|_2\le {112\cdot468\over3D^3}={17472\over D^3}.
\]
The inverse transform \(\mathcal F^{-1}q\) is supported in the reflected bands \([-9/4,-7/4]\cup[-5/4,-3/4]\), by Theorem 2. Frequency translation only modulates the inverse transform. Therefore on \(t>0\), \(|s_L(t)|=|\mathcal F^{-1}d(t)|\). Cauchy–Schwarz and Plancherel imply
\[
 \int t_+|s_L(t)|^2dt
 \le\|\mathcal F^{-1}d\|_2\,\|t\mathcal F^{-1}d\|_2
 =\|d\|_2\|d'\|_2
 \le {273\over32768} < {440\over32768}={55\over4096}.
\]
This contradicts (3.1). ∎

This is a written, exact analytic-signal GD counterexample. Its separate novelty is not established. The simpler obstruction for unrestricted complex signals follows immediately by Fourier duality from Theorem 2; the cutoff is needed because the Fourier-dual signal is not automatically analytic.

## 4. Complete one-regression criterion for joint measures

**Theorem 4 (Strassen application).** Let \(\mu\) be a Borel probability on \(\mathbb R\), \(\nu\) a Borel probability with finite first moment, and \(f:\mathbb R\to\mathbb R\) Borel with \(\int|f|d\mu<\infty\). A coupling \(\pi\in\Pi(\mu,\nu)\) satisfying \(\mathbb E[W\mid T]=f(T)\) exists iff
\[
 f_\#\mu\le_{\rm cx}\nu.\tag{4.1}
\]
Here convex order means equal means and \(\int\varphi d(f_\#\mu)\le\int\varphi d\nu\) for all convex real functions, with extended integrals interpreted after subtracting an affine lower bound. Equivalently it suffices to check all call functions \((x-k)_+\), \(k\in\mathbb R\), and equal means. No first moment of \(T\) is required for this one-sided theorem.

**Proof.** Necessity is conditional Jensen followed by integration. For sufficiency use Strassen's martingale theorem: (4.1) gives a coupling \(\eta(du,d\omega)\) of \(\alpha=f_\#\mu\) and \(\nu\), with \(\mathbb E[W\mid U]=U\). Since the spaces are standard Borel, disintegrate \(\eta=\alpha(du)K(u,d\omega)\) into a Borel probability kernel; its first moment equals \(u\) for \(\alpha\)-almost every \(u\). Define
\[
 \pi(dt,d\omega)=\mu(dt)K(f(t),d\omega).
\]
Its first marginal is \(\mu\). Its second marginal is \(\int K(f(t),\cdot)d\mu=\int K(u,\cdot)d\alpha=\nu\). For every bounded Borel \(a\), absolute integrability follows from the finite first moment of \(\nu\), and
\[
 \int a(t)\omega\,d\pi=\int a(t)\left[\int\omega K(f(t),d\omega)\right]d\mu
 =\int a(t)f(t)d\mu.
\]
This is the defining identity for IF. ∎

The imported theorem is Strassen (1965), martingale-coupling theorem, reproduced as Theorem 1.1(i) in Leskelä–Vihola, arXiv:1404.0999v2. We read that precise statement; the present application uses it, rather than claiming a new proof of Strassen. Exchanging the variables gives the GD criterion \(g_\#\nu\le_{\rm cx}\mu\).

**Density warning.** This theorem is not a density-existence theorem. For example let \(\mu=\nu\) be uniform on \([-1,1]\) and \(f(t)=t\). Convex order holds with equality. In any coupling with IF,
\(\mathbb E[(W-T)^2]=\mathbb E[W^2]-2\mathbb E[Tf(T)]+\mathbb E[T^2]=0\).
The only possibility is \(W=T\), a measure on the diagonal, not a two-dimensional Lebesgue density. These data are an abstract coupling example, not asserted to be time/frequency data of one finite-energy signal. Thus no density conclusion for the book may be inferred from Theorem 4 alone.

## 5. Two regression constraints: necessary conditions and Fourier identity

**Theorem 5.** Suppose \(\mu,\nu\) have finite second moments, and a coupling satisfies both IF and GD. Then
\[
 f_\#\mu\le_{\rm cx}\nu,\qquad g_\#\nu\le_{\rm cx}\mu,\qquad
 \int t f(t)d\mu=\int\omega g(\omega)d\nu.\tag{5.1}
\]
For actual Fourier pairs with \(s\in H^1\) and \(ts\in L^2\), the last identity is automatic. Hence it is an important consistency check, not an independent extra restriction on such signal data.

**Proof.** The convex orders follow by Theorem 4. Finite second moments give \(\mathbb E|TW|<\infty\), and conditional expectations give
\(\mathbb E[TW]=\int tf\,d\mu=\int\omega g\,d\nu\).
For Fourier pairs, multiply by \(E\). The first expression is
\(\operatorname{Im}\int t\overline s s'\,dt\).
Plancherel, \(\widehat{ts}=iS'\) and \(\widehat{s'}=i\omega S\), yield
\[
 \int t\overline s s'\,dt=\int\omega\overline{S'}S\,d\omega.
\]
Taking imaginary parts gives
\(\operatorname{Im}\int t\overline s s'=-\operatorname{Im}\int\omega\overline S S'\), precisely the desired GD expression. All products are \(L^1\) by Cauchy–Schwarz. The Fourier differentiation identities extend from Schwartz functions by the usual \(L^2\) graph-norm approximation. The corresponding first-moment identities are \(\int f\,d\mu=\int\omega\,d\nu\) and \(\int g\,d\nu=\int t\,d\mu\), by the same Plancherel calculation. Subtracting the common product of means gives the centered covariance identity. ∎

## 6. The two convex orders and covariance are NOT sufficient

**Theorem 6.** Conditions (5.1) are insufficient for general joint-measure existence, even with absolutely continuous, compactly supported marginals and bounded smooth regression functions. The counterexamples below are abstract probability data; no Fourier-pair realization is claimed.

### 6.1 Exact three-point certificate

Let \(\mu=\nu=(\delta_{-1}+\delta_0+\delta_1)/3\). For \(r=3/4\), set
\[
 (f(-1),f(0),f(1))=(0,-r,r),\quad
 (g(-1),g(0),g(1))=(-r/2,0,r/2).
\]
Both have mean zero. The law of \(f(T)\) is the law of \(rX\), where \(X\sim\mu\); that of \(g(W)\) is the law of \((r/2)X\). For \(0\le c\le1\), convexity and Jensen imply
\(\mathbb E\varphi(cX)\le c\mathbb E\varphi(X)+(1-c)\varphi(0)\le\mathbb E\varphi(X)\).
Thus both convex orders hold (with genuine contraction rather than a variance-saturation degeneracy). Moreover
\[
 \mathbb E[Tf(T)]=r/3=1/4=\mathbb E[Wg(W)].
\]
Suppose a coupling exists, and set \(p_{ij}=\Pr(T=x_i,W=x_j)\), with \((x_1,x_2,x_3)=(-1,0,1)\). Its first-column mass, first-column GD and middle-row IF imply, respectively,
\[
 p_{11}+p_{21}+p_{31}=1/3,\quad
 -p_{11}+p_{31}=-r/6,\quad
 -p_{21}+p_{23}=-r/3.
\]
Adding gives
\[
 p_{23}+2p_{31}=1/3-r/2=-1/24,
\]
contradicting nonnegativity. This is an exact rational Farkas certificate using just three constraints. ∎

### 6.2 Absolutely continuous robust version

Fix \(\varepsilon=1/32\). Let \(\mu=\nu\) put mass \(1/3\), symmetrically about its center, on each interval
\(I_j=[x_j-\varepsilon,x_j+\varepsilon]\). Uniform density on each interval is sufficient; symmetric smooth bump densities are also allowed. Set \(f=(0,-r,r)\) on the three intervals and \(g=(-r/2,0,r/2)\), again \(r=3/4\). Extend these functions smoothly across the gaps and outside the intervals; the extensions have no effect on any integral.

Let \(C\) be the center of the interval containing a random variable with law \(\mu\). Then \(C\) is the three-point law above and \(\mathbb E[T\mid C]=C\), so \(\operatorname{law}(C)\le_{\rm cx}\mu\). The contraction argument proves both required convex orders by transitivity. The conditional means of the intervals are their centers, so both cross expressions still equal \(1/4\).

For any proposed joint coupling put \(p_{ij}=\pi(I_i\times I_j)\). The first-column mass remains \(1/3\). Replacing \(T\) by its interval center in the first-column GD integral makes an error of absolute value at most \(\varepsilon/3\). Replacing \(W\) by its interval center in the middle-row IF integral makes an error at most \(\varepsilon/3\). The same addition as above therefore gives
\[
 p_{23}+2p_{31}\le-1/24+2\varepsilon/3=-1/48<0,
\]
again impossible. ∎

This refutes the proposed general sufficiency claim completely, not just on a numerical grid. The probability data in §6 are not claimed to come from one Fourier pair. §10 gives a genuine Fourier-pair counterexample.

## 7. Nonnegativity is not needed for exact marginal and phase-moment identities

**Theorem 7.** For any nonzero Schwartz signal, the normalized Wigner function
\[
 w_s(t,\omega)={1\over2\pi E}\int s(t+\tau/2)\overline{s(t-\tau/2)}e^{-i\omega\tau}d\tau
\]
is real, has the two exact marginals, has IF and GD in the unnormalized moment sense, and is shift/scaling covariant. It need not be nonnegative.

**Proof.** Replacing \(\tau\) by \(-\tau\) proves reality. Fourier inversion at \(\tau=0\) gives \(\int w_s(t,\omega)d\omega=|s(t)|^2/E\). For the other marginal use \(u=t+\tau/2,v=t-\tau/2\), whose absolute Jacobian is one, obtaining \(\int w_s(t,\omega)dt=|S(\omega)|^2/E\).

Let \(A_t(\tau)=s(t+\tau/2)\overline{s(t-\tau/2)}\). Fourier differentiation gives
\(\int\omega w_s(t,\omega)d\omega=-iA_t'(0)/E=\operatorname{Im}(\overline s s')/E=f(t)|s(t)|^2/E\).
Fourier duality of the same formula gives
\(\int t w_s(t,\omega)dt=-\operatorname{Im}(\overline S S')/E=g(\omega)|S(\omega)|^2/E\).
All functions are Schwartz on the relevant variables, justifying these operations. Direct substitutions give the covariance formulas in Theorem 1. Applying this result to the analytic Schwartz variant in Theorem 2 proves that its Wigner function must be negative somewhere; otherwise Theorem 2 would be contradicted. ∎

For signed functions these ratios are algebraic moments, not conditional expectations of a probability measure. Consequently the theorem answers only the precise question “is positivity required for these representation identities?” (no). It does not settle what should count as a physical positive local energy measurement.

## 8. Universal quadratic positive rules are impossible

**Theorem 8.** There is no assignment \(s\mapsto Q_s\) of finite nonnegative Borel measures on \(\mathbb R^2\), quadratic/Hermitian in \(s\), with unnormalized marginals \(|s|^2dt\) and \(|S|^2d\omega\), for every \(s\in L^2\). The same nonexistence holds when the domain is only the linear subspace of analytic \(L^2\) signals.

**Proof.** “Quadratic/Hermitian” means that for every Borel set \(A\), \(Q_s(A)=B_A(s,s)\) for a positive semidefinite Hermitian form \(B_A\). Such forms satisfy Cauchy–Schwarz. Choose nonzero real nonnegative compactly supported smooth functions \(u,v\) with disjoint time supports, for example translates of one bump. Partition the time axis into a Borel set \(D\) containing the support of \(u\) and its complement containing the support of \(v\). For each Borel joint set \(A\), the time marginal gives \(Q_v(A\cap(D\times\mathbb R))=0\), so Cauchy–Schwarz makes the \(u,v\) cross term zero on that piece. On the complement \(Q_u=0\), and the same argument applies. Additivity of the polarized measures (which follows from additivity of \(Q_s\) and polarization) implies \(B_A(u,v)=0\). Thus \(Q_{u+v}=Q_u+Q_v\).

Taking frequency marginals would force \(|U+V|^2=|U|^2+|V|^2\) almost everywhere. But \(U(0),V(0)>0\), and these Fourier transforms are continuous, so \(\operatorname{Re}(U\overline V)>0\) on a neighborhood of zero. Contradiction.

For the analytic-only assertion, instead choose nonzero real nonnegative \(U,V\in C_c^\infty((0,\infty))\) with disjoint frequency supports, and let \(u,v\) be their inverse Fourier transforms. These and every linear combination are analytic Schwartz signals. Partition the frequency axis along the two supports. The frequency marginal and positive-form Cauchy–Schwarz kill the cross terms on the two pieces exactly as above, implying \(Q_{u+v}=Q_u+Q_v\). The time marginal would then require \(\operatorname{Re}(u\overline v)=0\) almost everywhere. But \(u(0),v(0)>0\) and continuity makes their real cross term positive near zero. This is the required contradiction within the analytic subspace. ∎

This is a self-contained reproduction of the classical obstruction already reported by the book and by Loughlin–Pitton–Atlas, pp.2697–2698; no novelty is claimed. It does not apply to nonlinear Cohen–Posch rules such as Theorem 1.

## 9. Continuation: exact density criterion for one conditional mean

This section closes the density/measure gap left open by §4 for one conditional mean. It does not settle two simultaneous conditional means. The proof below is relative to the same classical Strassen theorem, with the density construction and all barrier arguments supplied explicitly. Novelty is not claimed.

**Theorem 9 (one-regression density criterion).** Let \(\mu,\nu\) be Borel probabilities on \(\mathbb R\), both absolutely continuous with respect to Lebesgue measure. Assume \(\int |w|\,\nu(dw)<\infty\), and let \(f:\mathbb R\to\mathbb R\) be Borel with \(\int|f|\,d\mu<\infty\). Put
\[
 \alpha=f_\#\mu,\quad
 D(c)=\int|w-c|\,\nu(dw)-\int|u-c|\,\alpha(du),\quad
 I=\{c:D(c)>0\}.
\]
There exists a nonnegative two-dimensional Lebesgue density with marginals \(\mu,\nu\) and \(\mathbb E[W\mid T]=f(T)\) **if and only if**
\[
 \alpha\le_{\rm cx}\nu\quad\hbox{and}\quad \alpha(I)=1. \tag{9.1}
\]
Thus the extra condition is not global strict convex order: the initial regression law must give zero mass to the contact set of the two potentials. The law \(\alpha\) itself need not have a density.

### 9.1 Barrier lemma

Suppose \(U,W\) form a martingale coupling of integrable laws \(\alpha\le_{\rm cx}\nu\). For each \(c\) with \(D(c)=0\), conditional Jensen gives
\[
 \mathbb E[\,|W-c|\mid U\,]\ge |U-c|.
\]
The integrated difference is zero, so equality holds almost surely. If \(U<c\), this forces \(W\le c\); if \(U>c\), it forces \(W\ge c\); and on \(U=c\) it forces \(W=c\). These assertions follow from equality in the triangle inequality for a real variable with the specified conditional mean.

Let \(F=\{D=0\}\), a closed set. Take a countable dense subset of \(F\), including every finite endpoint of every component of the open set \(I\). (There are only countably many components.) Intersect the probability-one barrier events for these thresholds. On the resulting event, \(U\in F\) implies \(W=U\): if, say, \(W>U\), either \((U,W)\) contains a point of \(F\), hence one of the selected thresholds, or it lies in one component of \(I\), making \(U\) a selected left endpoint. Both cases contradict the corresponding barrier property. The case \(W<U\) is identical.

Moreover, if \(U\) lies in a component \(I_k=(a_k,b_k)\), the endpoint barriers force \(W\in[a_k,b_k]\), omitting a bound if that endpoint is infinite.

### 9.2 Necessity

Given the required density, set \(U=f(T)\). The tower property yields \(\mathbb E[W\mid U]=U\), so \(\alpha\le_{\rm cx}\nu\). The barrier lemma gives \(W=f(T)\) on \(f(T)\in F\). The graph of a Borel real function has two-dimensional Lebesgue measure zero, by Fubini. A joint density cannot charge that graph, so \(\Pr(f(T)\in F)=\alpha(F)=0\), proving (9.1).

### 9.3 A countable intermediate law

Assume (9.1). Strassen supplies some martingale coupling of \(\alpha,\nu\). The endpoint part of the barrier lemma and \(\alpha(I)=1\) imply that \(\nu\) is supported on the union of the closures of the components of \(I\). Their finite endpoints form a countable set. Since \(\nu\) is atomless, \(\nu(I)=1\).

Partition each component of \(I\), up to countably many endpoints, into countably many bounded intervals \(J_j\), each with compact closure \(K_j\subset I\), so small that
\[
 2\,\operatorname{diam}(J_j)\le \tfrac12\min_{c\in K_j}D(c). \tag{9.2}
\]
Such a partition exists: first tile each open component by bounded intervals whose closures stay inside it; on each compact tile, continuity and positivity of \(D\) give a positive minimum, and finite subdivision enforces (9.2). Interval endpoints have \(\nu\)-mass zero. Discard cells of zero mass. For each remaining cell set
\[
 b_j=\nu(J_j)>0,\qquad
 m_j=b_j^{-1}\int_{J_j}w\,\nu(dw),\qquad
 \gamma=\sum_j b_j\delta_{m_j}.
\]
Then \(\gamma\) is a probability with finite first moment and the same mean as \(\nu\). The means \(m_j\) lie in the interiors of their cells and are distinct. Jensen gives \(\gamma\le_{\rm cx}\nu\).

We also have \(\alpha\le_{\rm cx}\gamma\). Indeed, at any threshold \(c\), all cells lying wholly on one side of \(c\) have zero potential loss under replacement by their means, because \(w\mapsto|w-c|\) is affine there. At most one cell can straddle \(c\). If it is \(J_j\), its loss satisfies
\[
 0\le\int_{J_j}|w-c|\,\nu(dw)-b_j|m_j-c|
 \le 2b_j\operatorname{diam}(J_j)
 \le \tfrac12 D(c).
\]
At a cell endpoint the loss is zero, and outside \(I\) all cell losses are zero. Countable addition is legitimate since both laws have finite first moment. Thus \(u_\gamma(c)\ge u_\nu(c)-D(c)/2\ge u_\alpha(c)\) for \(c\in I\), and equality of the relevant potentials holds outside \(I\). Together with equal means, the potential characterization of convex order proves \(\alpha\le_{\rm cx}\gamma\).

### 9.4 Density construction and Fourier application

Apply Strassen to \(\alpha\le_{\rm cx}\gamma\), and disintegrate its coupling as \(\alpha(du)L(u,dm)\). Since \(\gamma\) is countable discrete, write \(l_j(u)=L(u,\{m_j\})\). Then
\[
 \sum_j l_j(u)=1,\quad \sum_j m_j l_j(u)=u
 \quad\alpha\text{-a.e.},\qquad
 \int l_j\,d\alpha=b_j.
\]
The mean series is absolutely convergent almost everywhere because \(\gamma\) has finite first moment. Define
\[
 K(u,dw)=\sum_j l_j(u)\frac{\mathbf1_{J_j}(w)}{b_j}\nu(dw),
 \qquad
 \pi(dt,dw)=\mu(dt)K(f(t),dw).
\]
This kernel is measurable and absolutely continuous with respect to \(\nu\). Its mean is \(\sum_jm_jl_j(u)=u\). Integrating over \(\alpha\) recovers \(\nu\), because \(\int l_j\,d\alpha=b_j\) and the cells partition \(\nu\)-almost all of the line. Therefore \(\pi\) has both required marginals and IF, and
\(\pi\ll\mu\otimes\nu\ll dt\,dw\). Explicitly, if \(\rho,\sigma\) are the marginal densities, then
\[
 p(t,w)=\rho(t)\sigma(w)\sum_j
 \frac{l_j(f(t))}{b_j}\mathbf1_{J_j}(w)
\]
is a valid nonnegative density, with no boundedness or smoothness assertion. This completes both directions. ∎

**Corollary 9.1 (genuine Fourier marginals).** For every nonzero \(s\in H^1(\mathbb R)\), define its normalized Fourier marginals and phase IF as in §0. A nonnegative exact-marginal **density** satisfying IF exists iff (9.1) holds with \(\alpha=f_\#\mu\). The hypotheses hold because both Fourier energy laws have Lebesgue densities, \(\int|\omega|d\nu<\infty\), and \(\int|f|d\mu<\infty\). For GD, exchange the variables and assume \(ts\in L^2\). This is an exact necessary-and-sufficient criterion for all signals in the indicated regular classes, not merely a finite-table or per-instance LP restatement.

**Primary comparison.** Beiglböck–Nutz–Touzi, *Complete Duality for Martingale Optimal Transport on the Line*, 2016 author PDF, Definition2.2, Proposition2.3, Theorem3.2, and Lemma3.3, explicitly identify the same potential contact barriers, irreducible intervals and forced diagonal transport. Their Lemma3.3 constructs a martingale plan that **dominates** a chosen measure in absolute continuity; that direction alone does not imply an absolutely continuous martingale plan and is not used as such here. Nutz–Wiesel, *On the Martingale Schrödinger Bridge between Two Distributions* (arXiv:2401.05209; author PDF dated 2024-01-10), Remark2.2, states that a martingale coupling **equivalent** to the product exists iff the pair is irreducible, citing BNT Lemma3.3 and its proof. Combining that statement with BNT's component decomposition already yields Theorem9 for absolutely continuous marginals. Theorem9 is therefore classified as a **reproduction / consequence of known martingale-transport results**, with a self-contained proof of the absolute-continuity direction via the small-cell intermediate law. No novelty is claimed.

## 10. A genuine Fourier pair: two convex orders and covariance are not sufficient

This section closes, negatively, the question left after §6: are the necessary conditions (5.1) sufficient for joint IF+GD existence when the data come from one genuine Fourier pair? It does **not** classify which Fourier pairs admit joint couplings, and it uses a complex signal with two-sided spectrum, not an analytic signal.

**Theorem 10.** Let
\[
 p(t)=4t^4-12t^2+3,\qquad
 s(t)=\pi^{-1/4}e^{-t^2/2}\Bigl(1+\tfrac{i}{14}p(t)\Bigr).
\]
(Equivalently \(s=h_0+i(\sqrt6/7)h_4\) in normalized Hermite functions; normalization constants are not used below.) Then:

1. \(s\) is a Schwartz function without zeros, \(S=s\) in the unitary convention of §0, and \(E=\|s\|_2^2=55/49\).
2. \(\mu=\nu\) has density \(\rho(t)=(196+p(t)^2)e^{-t^2}/(220\sqrt\pi)\); the IF is \(f=14p'/(196+p^2)\), smooth, odd and bounded with \(\sup|f|<301/100\); and the GD is \(g=-f\).
3. Both one-sided Strassen conditions hold: \(f_\#\mu\le_{\rm cx}\nu\) and \(g_\#\nu\le_{\rm cx}\mu\). Moreover the potential difference is strictly positive everywhere, so by Theorem9 **each one-sided problem separately has a nonnegative Lebesgue density** with both exact marginals.
4. The covariance identity holds automatically: \(\int tf\,d\mu=\int\omega g\,d\nu=0\).
5. There is **no** Borel probability measure \(\pi\) on \(\mathbb R^2\) with marginals \(\mu,\nu\) satisfying both \(\mathbb E_\pi[W\mid T]=f(T)\) and \(\mathbb E_\pi[T\mid W]=g(W)\). A fortiori no nonnegative density does.

Parts 1, 2 and 4 and the reduction steps are proved by hand below. The finite collections of strict inequalities in parts2, 3 and5 are certified by `work/verify_fourier_obstruction.py`, using exact rational arithmetic and FLINT/Arb ball arithmetic (python-flint0.9.0, 256-bit precision). No floating-point number is used to accept any inequality. This is a computer-assisted classical proof, not a Lean kernel check.

### 10.1 Fourier invariance, phase derivatives and moments

Write \(G(t)=\pi^{-1/4}e^{-t^2/2}\). In the convention \(S(\omega)=(2\pi)^{-1/2}\int s(t)e^{-i\omega t}dt\), \(\mathcal F[e^{-t^2/2}]=e^{-\omega^2/2}\) and, for Schwartz \(u\), \(\mathcal F[tu]=i(\mathcal Fu)'\). Rodrigues' formula \((d/d\omega)^ne^{-\omega^2/2}=(-1)^n\mathrm{He}_n(\omega)e^{-\omega^2/2}\) gives
\[
 \mathcal F[t^ne^{-t^2/2}]=(-i)^n\mathrm{He}_n(\omega)e^{-\omega^2/2}.
\]
With \(\mathrm{He}_2=\omega^2-1\) and \(\mathrm{He}_4=\omega^4-6\omega^2+3\),
\[
 \mathcal F[p\,e^{-t^2/2}]
 =\bigl[4\mathrm{He}_4+12\mathrm{He}_2+3\bigr]e^{-\omega^2/2}
 =p(\omega)e^{-\omega^2/2}.
\]
By linearity \(S=s\). The verifier rechecks this polynomial identity exactly and rejects the non-invariant control \(t^2e^{-t^2/2}\).

Since \(|1+ip/14|^2=1+p^2/196\ge1\), \(s\) has no zeros. With the exact Gaussian moments \(\int t^{2m}e^{-t^2}dt/\sqrt\pi=(2m-1)!!/2^m\), one gets \(\int p^2e^{-t^2}dt/\sqrt\pi=24\), so \(E=1+24/196=55/49\) and \(\rho=|s|^2/E\) is as stated; \(\int\rho=1\) is rechecked exactly.

Writing \(s=G(u+iv)\) with \(u=1,v=p/14\), \(G'=-tG\) gives \(\operatorname{Im}(\bar ss')=G^2(uv'-vu')=G^2p'/14\), hence
\[
 f={p'/14\over1+p^2/196}={14p'\over196+p^2},\qquad
 J:=f\rho={14p'(t)e^{-t^2}\over220\sqrt\pi}.
\]
Because \(S=s\), the spectral phase equals the time phase, so \(g(\omega)=-\operatorname{Im}(\bar SS')/|S|^2=-f(\omega)\). As \(196+p^2\ge196\), \(f\) is smooth; it is odd because \(p\) is even, and \(\rho\) is even. The moments \(\int J=0\) and \(\int tJ\,dt=14\int(16t^4-24t^2)e^{-t^2}dt/(220\sqrt\pi)=14(12-12)/220=0\) give part4; the GD side is \(\int\omega g\,d\nu=-\int\omega J(\omega)d\omega=0\).

**Sup bound.** \(|f|<c\) everywhere iff both \(c(196+p^2)\mp14p'>0\) everywhere. For \(c=301/100\) these degree-8 polynomials have positive leading coefficient and no real root, by an exact Sturm count (sign variations at \(\pm\infty\)) and independently by FLINT's certified complex-root isolation. Hence \(|f|<301/100\). Conversely the exact value \(f(9/5)=9450000/3143009=3+20973/3143009>3\) (also checked by the verifier) shows the cap cannot be lowered to \(3\); thus \(3<\sup|f|<3.01\), and the fine-grid float value is \(3.00667\).

### 10.2 Both convex orders, at every real strike

Since \(\nu=\mu\) and \(g=-f\), \(g_\#\nu\) is the reflection of \(f_\#\mu\). Because \(f\) is odd and \(\mu\) symmetric, \(f_\#\mu\) is symmetric, so both required orders are the single statement \(X:=f(T)\le_{\rm cx}T\), \(T\sim\mu\). Both means are zero. For symmetric integrable \(X\) and \(k\ge0\), \(\mathbb E(X-k)_+=\tfrac12\mathbb E(|X|-k)_+\), while for \(k<0\), \((x-k)_+=(x-k)+(k-x)_+\) gives \(\mathbb E(X-k)_+=|k|+\mathbb E(X-|k|)_+\). Hence convex order is equivalent to
\[
 C_f(k):=\mathbb E(|f(T)|-k)_+\le C_T(k):=\mathbb E(|T|-k)_+\qquad(k\ge0).
\]

* For \(k\ge301/100\): \(C_f(k)=0\) by the sup bound, while \(C_T(k)>0\). This covers the entire tail of strikes **without any grid**.
* For \(k\in[k_j,k_{j+1}]\subset[0,301/100]\), both call functions are nonincreasing, so \(C_f(k)\le C_f(k_j)\) and \(C_T(k)\ge C_T(k_{j+1})\). The verifier uses \(k_j=j/100\), \(j=0,\dots,301\), and certifies \(C_T(k_{j+1})-C_f(k_j)>0\) on all301 intervals. The smallest certified lower bound is \(0.0019989\ldots\), on \([3,3.01]\).

Rigorous evaluation: \(C_T(k)=2\int_k^\infty(t-k)\rho\), a finite combination of \(\operatorname{erfc}(k)\) and \(k^ne^{-k^2}\) terms. For \(k>0\), on \(t>0\), \((|f|-k)_+\rho=\bigl[(Q_k^+)_++(-Q_k^-)_+\bigr]e^{-t^2}/(220\sqrt\pi)\) with \(Q_k^\pm=14p'\mp k(196+p^2)\). Their positive roots are isolated by FLINT, the root count is matched against an exact Sturm count, and the sign between roots is evaluated exactly at rational sample points. The integrals \(\int Q e^{-t^2}\) between root balls use exact antiderivative recursions for \(\int_0^xt^me^{-t^2}\) in Arb. The value \(C_f(0)=\mathbb E|f(T)|=7(16e^{-3/2}+4)/(55\sqrt\pi)\) is in closed form.

The certified margins also give strict positivity of the potential difference: with equal means, \(D(c)=\mathbb E|T-c|-\mathbb E|f(T)-c|=2[\mathbb E(T-c)_+-\mathbb E(f(T)-c)_+]=C_T(|c|)-C_f(|c|)>0\) for every real \(c\). The contact set is empty, so Theorem9 applies to IF alone and, symmetrically, to GD alone.

### 10.3 Dual certificate excluding both regressions together

Let \(e_j=-4+j/4\) \((j=0,\ldots,32)\), cells \(C_i=[e_i,e_{i+1}]\), and let \(a_i,b_i,h_i,k_i\) be the 128 rational numbers in `evidence/fourier-certificate.json`. Put
\[
 A^-=\max(0,\max_i(-a_i))=0,\quad B^-=\max(0,\max_j(-b_j))={84071\over250000},\quad
 H=\max_i|h_i|={34463\over62500},\quad K=\max_j|k_j|={524791\over1000000}.
\]
Define step functions with \(a=a_i,h=h_i\) on \(C_i\) (any choice on shared endpoints), \(a(t)=B^-+K|t|\) and \(h(t)=0\) for \(|t|>4\); likewise \(b=b_j,k=k_j\) on \(C_j\), and \(b(w)=A^-+H|w|\), \(k(w)=0\) for \(|w|>4\).

**Lemma 10.1.** \(\Phi(t,w)=a(t)+b(w)+h(t)w+k(w)t\ge0\) on all of \(\mathbb R^2\).

*Proof.* On a closed rectangle \(C_i\times C_j\), \(\Phi=a_i+b_j+h_iw+k_jt\) is affine, so its minimum is attained at a corner; the verifier evaluates all \(4\cdot32^2\) corner values exactly, minimum \(10^{-6}\). If \(t\in C_i\) and \(|w|>4\): \(\Phi=a_i+A^-+H|w|+h_iw\ge a_i+A^-\ge0\). If \(|t|>4\) and \(w\in C_j\): \(\Phi=B^-+K|t|+b_j+k_jt\ge B^-+b_j\ge0\). If both are outside, \(\Phi=B^-+K|t|+A^-+H|w|\ge0\). ∎

*Proof of part5.* Suppose \(\pi\) exists. Since \(h,k\) are bounded and \(a,b\) grow at most linearly, every term below is integrable (\(\mu,\nu\) have all moments). Conditioning,
\[
 0\le\int\Phi\,d\pi=\int a\,d\mu+\int b\,d\nu+\int hf\,d\mu+\int kg\,d\nu=:\Lambda .
\]
With \(\nu=\mu\), \(g=-f\) and \(J=f\rho\),
\[
 \Lambda=\sum_i\bigl[(a_i+b_i)\mu(C_i)+(h_i-k_i)\!\int_{C_i}\!J\bigr]
 +(A^-+B^-)\mu(|t|>4)+(H+K)\!\int_{|t|>4}\!|t|\,d\mu .
\]
All integrals are explicit Gaussian-moment expressions (erf, erfc, exp at rational points). Arb encloses
\[
 \Lambda\in[-0.0057637133335289315486863553767\ldots\pm4.01\cdot10^{-74}],
\]
so \(\Lambda<0\), a contradiction. ∎

**Controls (not part of the proof).** The same certificate evaluated on Gaussian chirps \(s_\beta=\pi^{-1/4}e^{-(1-i\beta)t^2/2}\), whose nonnegative Wigner Gaussian is an actual coupling with IF \(\beta t\) and GD \(\beta\omega/(1+\beta^2)\), gives \(\Lambda>0\) for \(\beta\in\{0,1,-41/25,3\}\), as any correct evaluator must. Negating \(h,k\) or lowering every \(a_i\) by \(1/50\) is rejected by the corner check, and the convex-order verifier rejects cap \(3\). An independent floating-point rebuild from SciPy Hermite functions matches \(S=s\) (direct transform error \(1.8\cdot10^{-12}\)), \(\rho\), the IF, and GD \(=-f\) (errors \(\le3\cdot10^{-10}\)).

**Provenance and limits.** The certificate was found from a relaxed cell LP (HiGHS) and rounded; nothing in that search is evidence, and it remains in `evidence/` as exploration together with failed or inconclusive runs: the 24-cell relaxation was feasible (no certificate at that resolution); two 80-bin runs hit time limits; and a first screen imposed the moment constraints with tolerance \(10^{-8}\) and no bin-error allowance, which is not a valid relaxation, so its "infeasible" reports carry no evidence (the valid relaxation is feasible for amplitudes \(\le0.2\) at 40 bins). Only the exact/ball checks above carry the theorem.

**Heuristic reading (not used).** Near zero, \(f(t)\approx-(336/205)t\) while \(g(\omega)\approx+(336/205)\omega\): the two regressions ask \(W\) to move against \(T\) while \(T\) moves with \(W\). For a nonnegative coupling such local slopes are inconsistent unless compensated elsewhere, and the certificate shows the compensation available from the larger-\(|t|\) lobes is insufficient. For the same signal the Wigner function (Theorem7) reproduces marginals, IF and GD, and so does the real part of the normalized Rihaczek/Margenau–Hill function \(R(t,\omega)=s(t)\overline{S(\omega)}e^{-i\omega t}/(E\sqrt{2\pi})\) (its \(\omega\)-moment is \(i\,s\,\overline{s'}/E\), whose real part is \(\operatorname{Im}(\bar ss')/E\); the GD side is dual). Part5 implies both must take negative values.

**Prior-art boundary.** LPA94 §III-D and LT97 (one-sided range violations of IF), Spriet–Langrenez–Brummelhuis–De Bièvre, arXiv:2511.01996 (2025), Lemma3.9 (a one-sided, state-dependent quantum no-go: an *anomalous* conditional expectation outside the spectral range excludes a Born-compatible joint probability reproducing it), and BNT/NW (one-sided martingale couplings) do not cover this two-sided case: here each one-sided problem is solvable even with densities and no value is anomalous. No earlier two-sided Fourier-pair counterexample was located on 2026-10-14; novelty is **not** established.
