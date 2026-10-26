# Literal stochastic H-infinity preview — finite rational Robin certificate and constructive scoped separation

**InfoHinfPreview-2 / info-3. WRITTEN CANDIDATE ONLY.** Actual returned clock before creation: **Sun Oct 25 09:17:18 PDT 2026** (`/bin/date`). ONE immutable consolidated successor to the459-LF v1, following the returned Olson review and the frozen0853 primary continuation.

## 0. What has been achieved, and the exact representation of the numbers

The active Robin enclosure is closed here by an **analytic trace-moment comparison**, not an eigensolve. The endpoints are completely specified **finite rational expressions**. Their relative-width certificate is proved analytically, without evaluating the enormous expressions. This is stronger than the prior existential rational-density choice: the actual output/control coefficients d,r below contain **no unknown eigenvalue, unevaluated integral, search, existence choice or limiting parameter**.

The representation is intentionally explicit about its limitation: **expanded numerator/denominator digits or decimal endpoints have not been computed**, and no practical arithmetic/complexity claim is made. A fixed finite sum is an exact rational number whether or not its digits are expanded. This manuscript specifies that sum fully, proves positivity of its denominator and proves the enclosure/extraction inequalities for the specified number itself. It is not a placeholder instruction to estimate an eigenvalue later.

For the unit Robin ground value Lambda1, this gives exact rational endpoints with ratio less than `1+2^-20`. For every prescribed positive rational h,T,gamma with `h<T<=2h`, the certificate then supplies **specified rational d,r** yielding literal feasibility at gamma but **all-controller mean-square infeasibility** at gamma. A canonical actual rational plant has h1,T2,gamma1 and is displayed in section9.

This is a scoped family advance, **not** the original general arbitrary-plant prescribed-gamma N&S synthesis theorem. The latter remains OPEN; the first remaining general-synthesis obligation is stated in section12.

### Mandatory evidence/acceptance qualifications

Parentv1–v10 and HOLDv2 remain binding. The COMPLETE459-LF pinned v1 was read before this continuation; its observed SHA is `863df2a96cb6a547a88961b7e5d595590941333b61ef10508f40f092fc50050b`. Common0853 rules/exact assignment and the current parent preview boundary were read. Exposure is frozen in `primary-continuation-20261025-0853-ack-v1.json`; its v10 addendum records the later overlay WITHOUT backdating that exposure.

The informal analytic route preceded this final proof file; this is not preregistration. V10 was fully read and additively recorded before the checkpoint/new proof body. Older Olson read-before-write chronology and the three qualified frozen formula-link defects are not silently repaired or used as mathematical permission.

**No scientific interpreter/eval/program, symbolic arithmetic, eigensolve, enumeration, replay, solver, compilation, scientific child, CLI or nested agent was used for this continuation.** All derivations are written mathematics. The only machine operations were source/metadata reads, hashes, clocks and owned-root writes. The owner's old four eval submissions remain preserved and unadmitted, with zero executable/certificate credit under the mandatory permission-withdrawal addendum. This manuscript is not WRITTEN_CHECKED_IN_KERNEL, formal proof, independent-family/human review, novelty clearance or parent acceptance.

## 1. Literal criterion, information and the retained two directions

Use the printed criterion, with expectation OUTSIDE the pathwise time norm:

$$N_1(v;I)=E\left(\int_I|v_t|^2dt\right)^{1/2},\qquad
N_2(v;I)=\left(E\int_I|v_t|^2dt\right)^{1/2}.$$

The disclosed precision conventions are unchanged: zero data/history, progressive disturbances of finite expected squared energy, strong nonanticipative well-posedness, local pathwise square-integrable controls, and Brownian future increments independent of the past. Finite output is counted on `[0,T]`; input is counted **only on `[0,T-h]`**, with no terminal-preview input added.

All constructions use the actual constant-matrix cascade

$$
\begin{aligned}
df_t&=\kappa[-f_t+c w(t-h)]dt,\\
dy_t&=(-\varepsilon y_t+b u_t)dt+(\sigma f_t+\beta u_t)dW_t,\\
z_t&=(d y_t,r u_t)^T.
\end{aligned}                                                     \tag{1}
$$

Both b and beta will be1, so drift and diffusion actuation genuinely affect the performance state. The penalty r is positive and full rank. For u0 the homogeneous storage `((sigma²+1)/(2kappa))*f²+y²` has expected derivative `-E f²-2epsilon E y²`, proving internal exponential mean-square stability.

The two horizon-dependent feasibility directions remain distinct:

1. **Retained long/infinite direction:** v1's general rational screen gives mean-square-feasible but all-controller literal-infeasible plants, with positive preview and explicit counted finite horizon or infinity. Its classical transfer import is Geiss–Scheutzow, [arXiv:2101.10884v2 Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2), at p1/2, conditional stopping-time energy domination and predictable accumulated input energy. The factor is sqrt2, not same-level equivalence. This retained theorem keeps its old exact source/review/import and unadmitted-arithmetic qualifications.
2. **New constructive short direction:** on every rational `h<T<=2h`, the explicit rational coefficients below make u0 literal-feasible but EVERY admissible controller mean-square-infeasible. The new Robin/moment certificate makes this formerly nonconstructive choice fully specified.

No single plant at one gamma is claimed to have both directions. No infinite-horizon opposite-direction theorem, same-gamma objective equivalence, or general literal synthesis criterion follows.

## 2. The EXACT unit operator and its Robin ground value

First fix the dimensionless active interval `[0,1]`, `kappa=1/2`, `epsilon=1/4`, `c=sigma=1`, base output scale d1. The zero-law deterministic input map has mean-square norm m and

$$
(A\phi)(s)={1\over\sqrt2}\sqrt{1-e^{-(1-s)/2}}
                  \int_0^s e^{-(s-v)/2}\phi(v)dv.
$$

Itô isometry and Tonelli identify m-squared with the largest eigenvalue theta of the positive compact input Gram operator K=A* A. Direct integration gives its EXACT kernel

$$\boxed{K(v,w)=\tfrac12 e^{(v+w)/2}
       \big(e^{-\max(v,w)/2}-e^{-1/2}\big)^2,\quad0\le v,w\le1.} \tag{2}
$$

Indeed the unsimplified kernel is

$$\tfrac12 e^{(v+w)/2}\int_{\max(v,w)}^1
                 \big(e^{-s}-e^{-(s+1)/2}\big)ds,$$

whose integral is the displayed square. No scale or endpoint is approximated in(2).

For the Robin identity put

$$F(s)=\int_0^s e^{-(s-v)/2}\phi(v)dv,\qquad
\phi=F'+\tfrac12F,\quad F(0)=0.$$

Then

$$\int_0^1\phi^2=\int_0^1(F'^2+\tfrac14F^2)+\tfrac12F(1)^2.$$

The cross term supplies the terminal term; it is NOT removed. The weighted compact Rayleigh principle therefore gives

$$-F''+\tfrac14F=\Lambda(1-e^{-(1-s)/2})F,\qquad
F(0)=0,\quad F'(1)+\tfrac12F(1)=0,$$

and for its smallest eigenvalue

$$\boxed{\theta=m^2=1/(2\Lambda_1).}                       \tag{3}$$

The construction below approximates the compact operator(2), then encloses its ACTUAL largest eigenvalue. It never changes this Robin boundary to a Dirichlet endpoint.

A useful written lower bound needs no eigenvalue computation. With unit input phi1, `f_s=1-e^-s/2>=s/4`; the OU variance is at least `s³/96` because `e^-1/2>=1/2`. Integrating gives

$$\theta\ge1/384.                                        \tag{4}$$

## 3. A positive RATIONAL polynomial kernel with a proved operator error

Fix Taylor degree40 and define the rational polynomials

$$E(v)=\sum_{j=0}^{40}{(v/2)^j\over j!},\qquad
Q(v)=\sum_{j=0}^{40}{(-v/2)^j\over j!},$$

$$J(v)=(Q(v)-Q(1))^2,$$

$$\boxed{K_0(v,w)=\tfrac12 E(v)E(w)J(\max(v,w)).}           \tag{5}$$

These are fixed polynomials, not fitted data. On `[0,1]`,

$$0<E(v)\le e^{v/2}<2,\qquad
|E(v)-e^{v/2}|\le2^{-40},$$

$$|Q(v)-e^{-v/2}|\le2^{-41}.$$

The first remainder follows from the positive Taylor remainder and `e^1/2<2`; the second is the alternating remainder. Also `Q'=-Q39/2`, where grouping the odd Taylor polynomial in positive adjacent pairs gives `Q39(v)>=1-v/2>=1/2`. Hence Q decreases from1, and `Q(1)>=e^-1/2>=1/2`. Both

$$Q(v)-Q(1)\quad\text{and}\quad e^{-v/2}-e^{-1/2}$$

lie in `[0,1/2]`. Their difference is at most2^-40, so their squared difference is at most2^-40. The exponential-product error is at most `4*2^-40`. Consequently the kernel difference is at most

$$\tfrac12\big((4\cdot2^{-40})/4+4\cdot2^{-40}\big)
=\tfrac52\,2^{-40}<2^{-38}.$$

On a unit interval a uniform kernel bound is also an L2 operator bound by Cauchy–Schwarz. Set the deliberately looser rational allowance

$$\eta=2^{-36},\qquad\|K-K_0\|<2^{-38}<\eta.              \tag{6}$$

### Positivity and trace are proved, not assumed from the approximation

J is nonnegative, decreasing, and J(1)0. Therefore

$$J(\max(v,w))=\int_{\max(v,w)}^1[-J'(s)]ds,$$

so K0 is the Gram operator of the Hilbert–Schmidt map

$$f\longmapsto\sqrt{-J'(s)/2}\int_0^s E(v)f(v)dv.$$

It is positive and trace-class. Its trace is exactly

$$\tau_1=\tfrac12\int_0^1 E(v)^2J(v)dv\le\tfrac12,          \tag{7}$$

since E²<=4 and J<=1/4. Let theta0 be its largest eigenvalue. Rayleigh comparison, (4),(6) imply

$$\theta_0\ge\theta-\eta>1/512,$$

because `1/384-1/512=1/1536>eta`. No sampled kernel positivity, matrix rank or eigensolve is used.

## 4. Analytic trace-moment enclosure with a FIXED finite exponent

For ANY nonzero positive trace-class compact operator H, let lambda be its largest eigenvalue, `tau_n=Tr(H^n)>0`, and `mu_n=tau_(n+1)/tau_n`. Then

$$\boxed{\mu_n\le\lambda\le\mu_n+\operatorname{Tr}(H)/n.} \tag{8}$$

Proof: write eigenvalues as lambda*p_i, with0<=p_i<=1 and at least one p_i1. The difference is

$$\lambda-\mu_n=\lambda\,
{\sum_i p_i^n(1-p_i)\over\sum_i p_i^n}.$$

The denominator is at least1. Moreover

$$n p^{n-1}(1-p)\le1-p^n\le1,$$

because `1+p+...+p^(n-1)>=n p^(n-1)`. Thus the numerator is at most `sum_i p_i/n`, giving(8). This comparison is homogeneous under positive operator scaling and requires no spectral gap or finite-rank hypothesis.

Apply it to the PARTICULAR fixed K0 and fix once and for all

$$N=2^{30},\qquad\mu=\tau_{N+1}/\tau_N.$$

Section5 supplies a CLOSED FINITE RATIONAL expression for this number; it is not an eigenvalue oracle. Define

$$\boxed{l=\mu-\eta,\qquad \nu=\mu+1/(2N)+\eta.}             \tag{9}$$

All three are actual rational numbers. Equations(6)–(8) give

$$l\le\theta\le\nu.$$

Further, `mu>=theta0-1/(2N)` and theta0>1/512 imply

$$1/1024<l<\nu<1.$$

For the upper bound use mu<=theta0<=tau1<=1/2. The interval width is

$$\nu-l=2^{-31}+2^{-35}<2^{-30},$$

hence

$$\boxed{\nu/l<1+2^{-20}.}                               \tag{10}$$

The required Robin enclosure is therefore the explicitly defined rational interval

$$\boxed{1/(2\nu)\le\Lambda_1\le1/(2l),\quad
{\text{upper}\over\text{lower}}<1+2^{-20}.}              \tag{11}$$

This is a FINITE analytic certificate: N is fixed, not a limit to be chosen after observing a numerical output.

## 5. The moments in(9) are fully specified finite RATIONAL numbers

This section removes any possible ambiguity about the word “explicit.” It gives an integer-only finite formula, with no unevaluated integral or spectral datum.

Let

$$D=2^{40}40!,\qquad u_j={D\over2^j j!},\qquad q_j=(-1)^ju_j
\quad(0\le j\le40),$$

all integers. Define integer polynomials

$$U(z)=\sum_{j=0}^{40}u_jz^j,\qquad
V(z)=\sum_{j=0}^{40}q_jz^j-\sum_{j=0}^{40}q_j.$$

Thus `E=U/D`, `J=V²/D²`. For e0,1,2 define the integers

$$a_{e,j}=D^{4-2e}\operatorname{coeff}_{z^j}
                  (U(z)^2V(z)^{2e}),\qquad0\le j\le240.$$

These are coefficients of fixed degree-at-most240 integer polynomials, padded by zeros. Equivalently each is a finite convolution of at most six40-degree coefficient arrays; there is no unspecified linear solve or empirical table. They satisfy

$$E(z)^2J(z)^e=D^{-6}\sum_{j=0}^{240}a_{e,j}z^j.$$

For an integer n>=3, let a permutation pi give the order of labels1,...,n. On the n-cycle of these labels, let `e_k(pi)` be the number (0,1or2) of cycle edges whose higher-ranked endpoint is the k-th label in that order. This is a fully specified finite combinatorial function. Put

$$F_n=(241n)!,$$

$$\begin{aligned}
A_n=\sum_{\pi\in S_n}\ \sum_{j_1,\ldots,j_n=0}^{240}
\left(\prod_{k=1}^n a_{e_k(\pi),j_k}\right)
\prod_{k=1}^n{F_n\over j_1+\cdots+j_k+k}.
\end{aligned}                                                   \tag{12}
$$

Every factor after the a's is an INTEGER: its denominator lies between1 and241n and divides F_n. Hence A_n is a definite integer specified by a closed finite expression.

To prove the exact trace formula, use the Hilbert–Schmidt trace contraction

$$\tau_n=\int_{[0,1]^n}\prod_{i=1}^nK_0(t_i,t_{i+1})dt,
\qquad t_{n+1}=t_1.$$

The kernels are continuous/bounded and K0 is positive trace-class as proved above. Partition the cube into its order-simplexes, ignoring measure-zero ties. Each vertex contributes E² and each edge contributes J of its higher-ranked endpoint, so the integrand on one simplex is `2^-n product_k E(z_k)^2J(z_k)^(e_k)`. Finally

$$\int_{0\le z_1\le\cdots\le z_n\le1}\prod_kz_k^{j_k}dz
=\prod_{k=1}^n(j_1+\cdots+j_k+k)^{-1}.$$

Successive integration proves this formula directly. Therefore

$$\boxed{\tau_n={A_n\over2^nD^{6n}F_n^n},\qquad
\mu={A_{N+1}F_N^N\over2D^6A_NF_{N+1}^{N+1}}.}             \tag{13}$$

Since theta0>1/512, every tau_n>0; thus A_N,A_(N+1)>0 and ALL denominators in(9),(13) are nonzero. Polynomial coefficients can have either sign; their finite sum's positivity is deduced from the proved positive operator, not guessed from coefficient signs.

**No sum or permutation set in(12) was executed, materialized or enumerated by a program.** Formula(12) is a written specification of exact integers and a proof of rationality, analogous to specifying a large integer by factorials/powers. Its analytic enclosure proof does not require expanding the digits. No executable-certificate credit or efficient evaluation claim is made.

## 6. Fresh quantitative Gaussian gap, with the literal denominator preserved

For a centered real Gaussian Hilbert variable Y with covariance Gamma and `q=Tr Gamma>0`, set `s2=Tr(Gamma²)/q²`, `s3=Tr(Gamma³)/q³`. Independent Gaussian coordinates give

$$E(\|Y\|^2/q)^2=1+2s2,\qquad
E(\|Y\|^2/q)^3=1+6s2+8s3.$$

The scalar moments1,3,15 follow by integration by parts; positive finite-coordinate truncation justifies the trace-class formulas. For X>=0 with EX1,

$$1-E\sqrt X\ge{(E(X-1)^2)^2\over4E[(X-1)^2(X+1)]},$$

by `(sqrt(X)+1)^2<=2(X+1)` and Cauchy–Schwarz. Applying this to the normalized Gaussian energy and using s3<=s2 gives

$$E\|Y\|\le\sqrt q(1-s2/12).$$

For a unit deterministic input to the unit cascade, let v(t)=E y_t² and use the loose bound B1/4. Cauchy–Schwarz gives `|f_t|²<=t/4`; Itô isometry then gives0<=v(t)<=B. The OU covariance is `Gamma(s,t)=e^{-(t-s)/4}v(s)` for s<=t. Since `e^-1/2>=1/2`,

$$\operatorname{Tr}(\Gamma^2)\ge\int_0^1(1-s)v(s)^2ds.$$

Writing `q=integral v`, take a terminal interval of length q/(2B); it contains at most q/2 variance mass. Cauchy–Schwarz on its complement gives

$$\operatorname{Tr}(\Gamma^2)\ge q^3/(8B).$$

The reference bound(4) says m²>=B/96. If q>=m²/2, then s2>=1/1536 and the Gaussian deficit is at least1/18432. If q<m²/2, the response is below m/sqrt2, which is smaller than the same bound. Hence

$$\boxed{\ell\le(1-\delta)m,\qquad\delta=1/18432.}          \tag{14}$$

This does NOT assert finite Gaussian rank or a uniform s2 lower bound for arbitrarily small output energies.

For physical h,T with `L=T-h<=h`, the ENTIRE progressive input on `[0,L]` is known at F_L before delayed forcing begins at h. Future Brownian increments are independent. Conditionally on that entire random input path the zero-law response has the deterministic-input Gaussian law. Thus

$$E[\|y^0\|_{L2(0,T)}\mid F_L]=J_L(w),\qquad
J_L(w)\le\ell_L\|w\|_{L2(0,L)}.$$

Taking expectation preserves the ACTUAL random denominator `E||w||`; it does not replace it by RMS input energy. Consequently the deterministic literal bound is the full-adapted literal gain. This conditional argument is invalid outside L<=h and is not used there.

## 7. Explicit rational square-root brackets on EVERY rational short horizon

Choose the base rates `kappa=1/(2L)`, `epsilon=1/(4L)`, c=sigma1. Exact time/Brownian rescaling gives

$$m_L^2=L\theta,\qquad\ell_L\le(1-\delta)m_L.$$

Let `L=A/B` in lowest positive integer terms, `S=A+B`, `J_*=S+64`. Start the FIXED finite rational recursion

$$q_0=S,\qquad q_{j+1}=\tfrac12(q_j+L\nu/q_j),
\quad0\le j<J_*.$$

There is no search or stopping rule: exactly J_* updates are part of the number's definition. If `g=sqrt(L nu)`, then q0>=g and

$$q_{j+1}-g={(q_j-g)^2\over2q_j}\le(q_j-g)/2.$$

Since nu>l>1/1024, `g>1/(32B)`. Therefore

$$q_{J_*}/g-1\le32BS\,2^{-S-64}\le2^{-58},$$

using B<=S and the elementary integer inequality `S²<=2^(S+1)` for S>=2 (check S2,3 then induct). Define the actual rational endpoints

$$\boxed{m_+=q_{J_*},\qquad m_-=Ll/q_{J_*}.}               \tag{15}$$

They satisfy0<m_-<=m_L<=m_+. Furthermore

$${m_+\over m_-}={q_{J_*}^2\over L\nu}{\nu\over l}
<(1+2^{-56})(1+2^{-20})<1+2^{-19}.$$

Because2^19>18432, this proves the REQUIRED strict inequality

$$\boxed{(1-\delta)m_+<m_-.}                              \tag{16}$$

All numbers in(15) are finite rational expressions in the SPECIFIED moment integers(12). No unevaluated square root or eigenvalue remains in them.

## 8. Specified ACTUAL rational d,r; full-adapted literal feasibility and ALL-control mean-square exclusion

Given any positive rational h,T,gamma with `h<T<=2h`, set L=T-h, use(15), and define without any existence choice

$$\boxed{d={\gamma\over2}\left({1\over m_-}
                    +{1\over(1-\delta)m_+}\right).}       \tag{17}$$

By(16) this rational midpoint lies STRICTLY between the two endpoints. Hence

$$d\ell_L\le d(1-\delta)m_+<\gamma<dm_-.$$

Take b=beta=c=sigma1 and `U=1+2L`. Its square is greater than2L, so it bounds the stochastic control norm factor. The actual finite-horizon control-only map satisfies

$$N_2(S_du)\le\overline M N_2(u),\qquad
\overline M=d(4L+U)=d(1+6L).$$

This follows from deterministic convolution gain4L and stochastic convolution gain sqrt(2L); extending realized control by zero AFTER T is only an upper estimate for this causal linear map.

Now put

$$A_*=d^2m_-^2-\gamma^2>0,\quad B_*=\gamma^2\overline M^2,$$

$$\boxed{r=1+B_*/A_*.}                                   \tag{18}$$

This is a finite positive rational number. The exact identity

$$r^2A_*=A_*+2B_*+B_*^2/A_*>B_*$$

implies

$$\frac{dm_-}{\sqrt{1+(\overline M/r)^2}}>\gamma.$$

For EVERY realized progressive control law, linearity of the actual plant gives `d y=d y0+S_d u`. If N2(z) is infinite it already fails mean-square attenuation; otherwise the separate r*u channel forces finite N2(u), and triangle/Cauchy–Schwarz gives

$$N_2(d y0)\le\sqrt{1+(\overline M/r)^2}\,N_2(z).$$

Taking the input supremum proves

$$G_2(F)\ge\frac{dm_L}{\sqrt{1+(\overline M/r)^2}}
\ge\frac{dm_-}{\sqrt{1+(\overline M/r)^2}}>\gamma$$

for EVERY admissible controller. This includes nonlinear, nonstationary, arbitrary-history and horizon-aware laws, all preview pre-action, and the book's smaller state/window class. No plant/controller reset or extra energy-history information is supplied.

Meanwhile u0 is of the printed information form, internally mean-square stable, and its full-adapted literal gain is strictly below gamma by(14),(17) and conditioning. Thus the rational-coefficient family is NOW completely specified, rather than chosen by rational density in unknown norm intervals.

## 9. One canonical actual rational plant, with NO unspecified coefficients

Take exactly h1,T2,gamma1, so L1,A=B1,S2,J_*66. The integers in(12) are fixed by Taylor degree40 and N2^30. Use(9) for l,nu, and define

$$q_0=2,\quad q_{j+1}=\tfrac12(q_j+\nu/q_j)\ (0\le j<66),
\qquad q=q_{66}.$$

Then the two actual rational numbers are

$$\boxed{d=\frac{18431q^2+18432l}{2\cdot18431\,lq},\qquad
r=1+\frac{49d^2}{d^2(l/q)^2-1}.}                         \tag{19}$$

Their denominators are strictly positive by the proof above. Together with(12),(13), (19) is a closed finite rational expression, NOT a choice of d,r from an uncomputed interval.

The exact plant matrices are

$$A=\operatorname{diag}(-1/2,-1/4),\quad B=B_0=(0,1)^T,
\quad C=(1/2,0)^T,$$

$$A_0=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
D_0=\begin{pmatrix}0&d\\0&0\end{pmatrix},\quad D_1=(0,r)^T.$$

The input is counted ONLY on `[0,1]`, output on `[0,2]`, and the actual delayed forcing is w(t-1). Both control channels are effective in y; D1-transpose-D1=r²>0. Under u0 the storage `2f²+y²` has expected derivative exactly `-(1/2)E(2f²+y²)`. This plant is literal-feasible at gamma1 and mean-square-infeasible at gamma1 for every admissible controller, by the displayed written certificate.

No expanded numerator/denominator digits are claimed observed. The precise representation of these actual rational coefficients is the finite arithmetic expression(12),(13),(19); there is no oracle, executable run or existential parameter hidden in that representation.

## 10. Retained OTHER feasibility direction and named probability import

The pinned v1's separate general-coefficient long/infinite family is not contradicted. It has actual zero law mean-square gain at most64gamma/65, yet every controller's literal gain is at least22464gamma/22145 on infinity or2323233gamma/2303080 on the supplied finite horizon `T=2080a²`. Its positive-preview/damping/filter/control coefficients and strict storage certificate remain exactly as in v1 sections2–4.

Its proof imports the stated Geiss–Scheutzow monotone theorem only at its actual stopping-time/predictability boundary. It does not square the printed objective into a Riccati objective. The present short-horizon opposite family instead uses direct Gaussian/conditioning reasoning plus a mean-square control-cost lower bound; it needs no new probability-constant claim.

These directions concern different stated plants/horizons. No same-plant contradiction, general same-gamma comparison, unrestricted linear-controller optimality, nonsmooth tangent replacement or infinite-horizon opposite direction is inferred. All old frozen sources and mandatory arithmetic/evidence errata remain unchanged.

## 11. Verification and the exact status of this written certificate

Completed in WRITING here: exact Robin kernel/boundary normalization; positivity and rationality of K0; every Taylor/operator error bound; universal trace-moment enclosure; fixed finite integer specification of both moments; strict rational relative-width bound; fixed finite rational square-root brackets; the actual d,r formulas; full-adapted literal feasibility and ALL-control mean-square exclusion.

Not performed: expansion/evaluation of the huge finite integer expressions, decimal spectral endpoints, a numerical eigensolve, interpreter arithmetic, finite enumeration, certificate replay, formal/kernel proof, independent-family/human review or novelty clearance. None is covertly used as a premise. Mathematical correctness of the fully written construction still needs independent source-body reconstruction and parent union/import disposition. No executable-verification credit or practical complexity claim is supplied.

The same-author Gaussian quantitative bridge is re-derived here rather than treated as inherited independent acceptance. Ordinary Itô/conditional Brownian arguments, positive compact/trace-class spectral theory, Hilbert–Schmidt trace contraction, Gaussian coordinate moments and the weighted Robin Rayleigh principle are named classical imports. The long-direction Geiss–Scheutzow import retains its separate source-checked scope. No preview Riccati theorem is used as if it solved literal synthesis.

## 12. First UNPROVED general-synthesis step; the example family is not a cutover

The ONE active Robin/rational-extraction gap from v1 has a complete written finite-expression certificate in this successor. Its stronger review/acceptance gates are not conferred by the owner's proof. Expanded small numerical coefficients are not delivered or needed for the specified exact expression, and no numerical execution is requested under HOLD.

The registered primary remains the GENERAL literal printed synthesis problem: arbitrary constant matrices, prescribed gamma/horizon, and the full admissible state/current-preview-window controller class. The first genuinely general missing implication is a non-tautological NECESSITY-and-realization bridge from that full non-Hilbert gain requirement to finite-dimensional operator/storage/LMI conditions at the SAME level, without assuming differentiability, stationarity, linear feedback optimality, unrestricted controller memory, or mean-square substitution. The explicit families show why an unqualified quadratic replacement cannot supply it.

No such general implication, universal controller construction, sharp optimum, new book-problem resolution or novelty claim is proved here. The correct next research step must address that original quantifier gap, not count this now-explicit family or another endpoint refinement as full synthesis. Parent full-body review and all separate stronger gates remain required. The original deadline/cutoff and global scientific-launch HOLD are unchanged.
