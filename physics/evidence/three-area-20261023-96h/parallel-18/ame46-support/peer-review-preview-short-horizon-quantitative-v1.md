# v64-B — complete written reconstruction of short-horizon quantitative separation and the Robin reduction

Actual returned `/bin/date` before creation: **Sun Oct 25 09:18:20 PDT 2026**. Reviewer PhysicsAME46-2; author InfoHinfPreview-2. **WRITTEN supplied-proof review only. No scientific interpreter/eval, arithmetic/symbolic program, enumeration, eigensolve, interval program, simulation, certificate replay, scientific job, external-model CLI or nested agent was used.** Metadata hashes/clocks and source reads only. V9, V10 and HOLD remain binding.

## 1. Verdict, exact supplied scope and complete coverage

**FATAL0 / MAJOR0 / MINOR0 for the asserted new short-horizon, Gaussian quantitative-gap, conditional coefficient-extraction and Rayleigh/Robin identity claims at their stated domains.** The explicit rational spectral enclosure and resulting numerical coefficient witness are intentionally NOT supplied; those are retained as the literal next unproved certificate obligation, not marked PASS.

The long/infinite separating-family theorem is retained as its explicitly named prior WRITTEN import after checking that its plant, admissibility and counted horizon domains match. The Geiss–Scheutzow theorem is a named classical import with its exact used hypotheses below, not a theorem newly proved or formally validated by this review. No old unadmitted arithmetic has verification/certificate credit.

Metadata hashes actually observed matching manifest/receipt:

- Manifest `peer-review-wave-eighteen-v64.json`: `d896681fa2e6600a953d15f05c8ec90acdfe05ee02f6896f09074d0bd3a5dd0e`.
- ALL assigned literal parts: ONE part, `peer-review-wave-v64-v64-B-part1-v1.md`, `ab16bb4d1e4f9527c76aa7f66f999ae6fec1ada5e912990107491b1b7769a049`.
- S3 `literal-preview-separation-consolidated-v1.md`: `863df2a96cb6a547a88961b7e5d595590941333b61ef10508f40f092fc50050b`, complete459LF.
- S4 `preview-full-packet-parent-v1.md`: `2d14983500510e72f08877b3256f96f2fda92f068e1d3346e93aa86b420db131`, complete44LF.

S1/v9 was read FIRST and S2/v10 immediately SECOND, complete35+31LF, before the exact assignment/receipt. The complete592-line literal part was then read RAW in windows1–180,181–335,336–490,491–592, covering EVERY declared source LF of S1–S4. No reader-truncated mathematical line remains. The own manifest scope was explicitly recovered RAW. The actual byte-equality receipt was read; no source-execution credit is inferred from it.

The exposure ACK was written at the actual09:11:36 observation BEFORE this review body. The reviewer previously returned v29-G/general-family and v34-A/short-horizon reviews and read the printed criterion images and actual Geiss–Scheutzow statement then; that exposure is disclosed, not confidence inherited by the NEW quantitative successor. The AME primary candidate was returned before this duty. No v63 review was pending for this owner. This is same-harness/different-domain supplied-proof review, not blind, configured-family, human, formal or novelty acceptance.

References below use ORIGINAL S3/S4 line numbers, not literal packet wrapper offsets.

## 2. Literal criterion, actual plant and all-controller bounds — S3:26–108

The target is `E(time-L2 norm)`, not the square root of expected energy. The full precision conventions are disclosed interpretations: zero data/history, progressive disturbances of finite expected squared counted input energy, strong nonanticipative nonexplosive well-posedness and local pathwise control integrability. They are not misrepresented as all verbatim book quantifiers. Finite output is counted on[0,T], input EXACTLY on[0,T-h].

The displayed matrices reproduce the actual two-state cascade: delayed disturbance drives f through kappa*c; f drives y diffusion through sigma; nonzero b and beta actuate y in drift AND diffusion; actual output stacks d*y and r*u. The positive r*u channel is not omitted. For u=0 and zero input, the f^2 coefficient of the expected derivative of V0 is `-(sigma^2+1)+sigma^2=-1`; its y^2 coefficient is-2epsilon. This gives the claimed strict exponential mean-square stability relative to its positive storage.

For any realized progressive control, linear variation of constants of the PLANT gives `d*y=d*y0+S_d u`. It does not require that the feedback producing u is linear, stationary, smooth, Markov or resettable. Both convolutions begin at0, so preview pre-action before h remains in the response and is charged in r*u.

For square-energy u, the ordinary stable convolution has L2 norm at most1/epsilon. Itô isometry and integrating the squared exponential kernel give1/sqrt(2epsilon) for the stochastic part. Triangle gives(2.2) with the stated Mbar when `2epsilon U^2>=1`. Zero extension after T is only extension of the realized INPUT to this causal linear map, not extension or resetting of the feedback law.

The exact classical transfer import used for(2.3) is Geiss–Scheutzow [arXiv2101.10884v2, Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2): nonnegative nondecreasing adapted right-continuous X,G, predictable G, and conditional domination `E[X_tau|F0]<=E[G_tau|F0]` for EVERY bounded stopping time; at p=1/2 its coefficient is sqrt2. Take X as accumulated output energy of S_d and G as Mbar^2 times accumulated input energy. Both are continuous/increasing; G is predictable. Stopping the INPUT at tau preserves the earlier output, and discarding its later nonnegative energy lets(2.2) give the required stopping-time inequality. Multiplication by any initial-measurable event commutes with this linear causal event-local map and its stochastic integral, giving the conditional version. Thus its hypotheses, not just a deterministic-time energy bound, are supplied.

Accumulated-energy localization gives square-energy stopped inputs, and Fatou/local causality extend(2.3) to finite N1(u) when N2(u) is infinite. A finite N1 output forces finite N1(u) through r*u; finite N2 output likewise forces finite N2(u). Infinite output already fails the corresponding attenuation. Triangle followed by two-dimensional Cauchy–Schwarz yields exactly factors `sqrt(1+2Mbar^2/r^2)` and `sqrt(1+Mbar^2/r^2)` in(2.4)/(2.5). Both are valid for the enlarged all-progressive realized-control class, including all pre-action. No independence between control and the uncontrolled response is assumed.

The Geiss–Scheutzow proof/sharpness and foundational stochastic-calculus results remain classical imports. The supplied S4:19 records the precise statement and scope; this review does not newly formalize that external theorem.

## 3. Square-root deficit identity and the retained long/infinite baseline — S3:112–271

For X>=0, EX=1 and finite third moment, let v=E(X-1)^2 and w=E[(X-1)^2(X+1)]. Cauchy–Schwarz on `|X-1|/sqrt(X+1)` and `|X-1|sqrt(X+1)` gives

    E[(X-1)^2/(X+1)] >= v^2/w

when w>0. Also `(sqrt(X)+1)^2<=2(X+1)` and

    E(sqrt(X)-1)^2=2-2E sqrt(X).

Combining gives(3.1), `1-E sqrt(X)>=v^2/(4w)`. All denominators are positive; finite third moment supplies integrability. The w=0 case is the trivial constant X=1 and is not divided by. No random input denominator is replaced.

The retained long/infinite baseline is the exact prior general-parameter theorem pinned in S3:15 (`proof-general-parameter-separation-v1.md`, SHA58777c6e1b7b83766d0a969cfd0dbca4b41729577de732ece5dd2a1ad861d575), at its disclosed admissibility and probability imports. S3 preserves its actual cascade, signs/positive parameters, finite input endpoint L=T-h and separate infinite/supplied-long-finite regimes. It does not assert a reverse separation on every short preassigned horizon. The old source's now-withdrawn kernel-verification language supplies no credit here.

The summary is consistent at its interfaces: stopped-Dynkin polynomials have zero endpoint values and generator relations `mu_j''/2=-j mu_(j-1)`; their values at0 give1,5/3,61/15. Their stopped/bounded strong-Markov induction is the named prior written argument, not an unbounded optional-stopping shortcut. The deficit inputs are v=2/3 and w=12/5, hence deficit5/108 and q0=103/108. The OU endpoint is averaged with E tau_a=a^2, while the finite event cutoff uses the second moment. The actual delay/filter error is an upper estimate paid separately; no uncounted infinite output tail or input after T-h appears in the lower anchor.

The general strict-storage quadratic form and long-family rational comparisons remain at the same source's prior written scope. Their domains agree: h,gamma arbitrary positive rationals, but the finite family supplies T=2080a^2. The strict positive squared weights at eta<gamma are mean-square storage, not a literal-gain Riccati certificate. The two feasibility directions below concern different data/horizon regimes. No same-plant same-level contradiction or full arbitrary-plant N&S synthesis is inferred.

## 4. Full progressive-input conditioning, compactness and strict supremum gap — S3:275–312

With u=0, output is zero before h. Set L=T-h and active time t-h in[0,L]. The actual filtered input is `f_(h+t)=kappa*c integral_0^t exp(-kappa(t-s))*w_s ds`. Itô isometry and Tonelli, without assuming deterministic w, give

    E||y0||^2
      =sigma^2/(2epsilon) E integral_0^L
          (1-exp(-2epsilon(L-t)))*f_(h+t)^2 dt
      =E||A_L w||^2.

This establishes the mean-square norm identity for ALL progressive square-energy inputs. The pathwise deterministic operator bound gives G2(0)<=||A_L||; deterministic inputs give equality. Its bounded triangular kernel is Hilbert–Schmidt, nonzero and compact. Multiplying its kernels gives the exact positive kernel at S3:288–289.

When L<=h, the ENTIRE input is an F_L-measurable random element of the separable space L2(0,L), known before any output noise starts. Future increments after h are independent of F_L. For a simple F_L-measurable random input `sum 1_Ej phi_j`, the post-h response is `sum 1_Ej R phi_j`; independence gives the conditional deterministic-response law. These simple variables need NOT be admissible disturbances before L: they approximate only the already-known parameter of a stochastic integral AFTER h, where F_L-measurability is adapted.

Approximation in L2(Omega;L2(input)) and the mean-square identity give convergence of responses in L2(Omega;L2(output)); hence norms converge in L1. Conditional expectation contracts L1, and `|J(phi)-J(psi)|<=||A_L(phi-psi)||` gives the matching convergence on the right. Thus `E[||y0|||F_L]=J(w)` holds. The same argument gives its conditional second moment. It includes the boundary L=h, using increments after h, not any future information during the counted input.

Consequently `E J(w)<=ell E||w||`, preserving the RANDOM denominator, and deterministic inputs give G1(0)=ell. No blanket Jensen ratio comparison is used. For L>h this conditioning is not asserted.

For strictness, a maximizing sequence for J on the Hilbert unit ball has a weakly convergent subsequence. Compactness of A_L makes its images converge strongly. Since `||R(phi_n-phi_*)||_(L2(Omega;L2))=||A_L(phi_n-phi_*)||`, J converges and attains its positive supremum. Homogeneity forces the maximizing phi_* to have norm1.

Its nonzero deterministic-input response is a centered Gaussian Hilbert variable. Some scalar projection has positive variance, by a countable orthonormal expansion and positive second moment. Almost-sure constant finite norm would bound every scalar projection, contradicting the unbounded support of that nondegenerate Gaussian. Therefore the norm is not constant; strict Cauchy–Schwarz gives J(phi_*)<||A_L phi_*||<=m. This is a STRICT GAP BETWEEN SUPREMA, not an unsupported passage from pointwise Jensen. All steps apply to the full progressive input class through the conditional reduction.

## 5. Opposite separation for every positive rational short horizon/level — S3:316–332

Fix rational h,T,gamma with h<T<=2h and any stated rational base coefficients. Since0<ell<m, the interval(gamma/m,gamma/ell) is nonempty. Rational density supplies positive rational d with `d*ell<gamma<d*m`. Choose positive rational U large enough for the diffusion bound; Mbar is rational. A sufficiently large rational r satisfies(6.1) by the positive gap d^2m^2-gamma^2.

For a SINGLE deterministic unit maximizing input of the compact mean-square operator, the uncontrolled mean-square output is d*m. Inequality(2.5) holds for the response of EVERY controller to this same disturbance, including pre-action, and gives the claimed uniform lower bound. A norm-approaching deterministic sequence would also suffice. Therefore all controllers have mean-square gain>gamma, while u=0 has full-progressive literal gain<gamma and the previously proved internal stability.

This is nonconstructive rational existence, not displayed numerical d,r. The tame conditions of Section7 are not needed for this earlier qualitative theorem. The long-family finite screen also correctly fails here: its conditions imply `E0>=sqrt(2R)`; R>=1/2 gives E0>=1 and QT<0, while R<1/2 already makes the tail-loss parenthesis negative. No short/long direction is conflated.

## 6. Gaussian moments and exact algebra of(7.1) — S3:338–354

Let C be the positive trace-class covariance of a centered real Gaussian Hilbert variable Y, q=Tr C>0. In a covariance eigenbasis, finite-coordinate squared norms are `S_n=sum_(i<=n) lambda_i*g_i^2`, with independent standard normals. Gaussian integration by parts gives moments1,3,15 at powers2,4,6.

Writing q_n=sum lambda_i and r_j,n=sum lambda_i^j, direct expansion gives

    E S_n^2=q_n^2+2*r_2,n,
    E S_n^3=q_n^3+6*q_n*r_2,n+8*r_3,n.

For the third formula the individual lambda_i^3 coefficient is15, the ordered mixed lambda_i^2 lambda_j coefficient is9, and the unordered distinct-triple coefficient is6; the displayed expression has exactly those coefficients. The nonnegative sums S_n increase to||Y||^2. Monotone convergence gives the infinite-Hilbert formulas, and trace finiteness makes their limits finite (r2<=q^2,r3<=q^3). Thus no finite-rank assumption or prior unproved third-moment integrability is used.

For X=||Y||^2/q,

    EX^2=1+2s2, EX^3=1+6s2+8s3,
    v=2s2,
    w=EX^3-EX^2-EX+1=4s2+8s3.

Substituting in(3.1) gives EXACT deficit `s2^2/(4s2+8s3)`, not a coefficient guessed from a variance heuristic. Normalized eigenvalues a_i=lambda_i/q are nonnegative and sum1, so each a_i<=1 and `s3=sum a_i^3<=sum a_i^2=s2`. Hence the deficit is at least s2/12 and(7.1) follows. This is the stated general Gaussian-Hilbert inequality, independently reconstructed in writing.

## 7. Tame input bound, covariance Hilbert–Schmidt norm and terminal mass split — S3:356–377

Use active output time[0,L], base d=1 and deterministic unit input phi. Cauchy–Schwarz in the actual filtered convolution gives

    |f(t)|^2<=kappa^2*c^2*t<=kappa^2*c^2*L.

Itô isometry then gives `0<=v(t)<=sigma^2*kappa^2*c^2*L^2=B`, and q=integral v<=BL. B>0. For a unit input q>0: if q were zero, the positive-a.e. terminal weight in A_L would force the Volterra F to vanish, and `phi=F'+kappa F` would vanish, contradicting unit norm. The zero-response case could in any event be handled trivially without division.

For s<=t, OU variation of constants and orthogonality of the future stochastic increment to y_s give `C(s,t)=exp(-epsilon(t-s))*v(s)`. Deterministic forcing also makes Y Gaussian. The covariance kernel therefore has

    Tr(C^2)=2 integral_0^L integral_s^L
                    exp(-2epsilon(t-s))*v(s)^2 dt ds.

The factor2 is the two triangles; the diagonal is measure zero. Since `2epsilon L<=1/2`, the elementary `exp(-x)>=1-x` gives the exponential at least1/2 throughout the triangle. Thus `Tr(C^2)>=integral_0^L (L-s)*v(s)^2 ds`.

Set tau=q/(2B)<=L/2. The terminal interval has mass at most B*tau=q/2, leaving at least q/2 on[0,L-tau]. On this prefix L-s>=tau. Ordinary Cauchy–Schwarz on its length L-tau<=L gives

    Tr(C^2)>=tau integral_0^(L-tau) v(s)^2 ds
             >=tau*(q/2)^2/L
             =q^3/(8BL).

This proves(7.3) with the source's exact constant. It does not require a false bound on covariance effective rank for all tiny-q outputs, an unproved tail distribution or numerical quadrature.

## 8. Reference input BL/96 and the ENTIRE-class delta1/18432 — S3:379–397

For phi=1/sqrt(L), the actual filter has `|f(t)|=|c|(1-exp(-kappa*t))/sqrt(L)`. If kappa*t<=1/2, then `1-exp(-x)=integral_0^x exp(-u)du>=x/2`; the bound follows from exp(-u)>=1-u>=1/2. The OU squared kernel is likewise at least1/2 under epsilon L<=1/4. Consequently

    v(t)>=sigma^2*c^2*kappa^2/(8L) integral_0^t s^2 ds
         =sigma^2*c^2*kappa^2*t^3/(24L),

    q_ref>=sigma^2*c^2*kappa^2*L^3/96=BL/96.

Hence m^2>=BL/96. For ANY deterministic unit input with q>=m^2/2, (7.3) gives

    s2>=q/(8BL)>=m^2/(16BL)>=1/1536.

Combining with(7.1) and sqrt(q)<=m gives `J(phi)<=m*(1-1/18432)`.

For q<m^2/2, Cauchy–Schwarz gives `J(phi)<=sqrt(q)<m/sqrt(2)`. This is below the same bound: `1/sqrt(2)<3/4<1-1/18432`, using9/16>1/2 and18432>4. Therefore the bound holds for EVERY deterministic unit input, not just a maximizing eigenfunction. Homogeneity extends it to all deterministic inputs; Section4's full conditional reduction then proves it for the ENTIRE progressive short-horizon input class.

The constants8*192=1536 and12*1536=18432 arise from the exact displayed chain. All reasoning is written; no old Fraction/checker result is used. The near-maximal-q split is logically indispensable because(7.3) alone weakens as q tends to zero. This verifies(7.4), with its stated tame conditions and conservative—not optimal—delta.

## 9. Conditional rational extraction and the r-choice — S3:401–418

Assume the NOT YET PROVIDED positive rational bounds m_-,m_+ satisfy(8.1). Its strict relative condition makes the rational endpoint interval

    (gamma/m_-, gamma/[(1-delta)*m_+])

nonempty. Its rational midpoint d obeys `d*ell<=d*(1-delta)*m_+<gamma`, and `d*m>=d*m_->gamma`.

With rational U and base coefficients, Mbar is rational. Let A=d^2*m_-^2-gamma^2>0 and B_*=gamma^2*Mbar^2>=0. The rational choice r=1+B_*/A satisfies

    r^2*A=A+2B_*+B_*^2/A>B_*.

Thus r^2(d^2*m^2-gamma^2)>=r^2*A>B_*, which is exactly the strict all-controller mean-square exclusion from(2.5). This checks the ACTUAL coefficient-extraction formula, not merely an abstract statement that r can be made large.

No m_-,m_+, evaluated d,r or particular rational coefficient witness is supplied by the source, and none is invented here. Rational density proves qualitative existence but is not a displayed finite spectral-enclosure certificate. The explicit extraction statement is a valid CONDITIONAL theorem once(8.1) is actually certified.

## 10. Full Rayleigh principle, terminal Robin condition and dimensionless normalization — S3:420–449

The Volterra substitution maps phi in L2(0,L) bijectively onto F in H1(0,L) with F(0)=0:

    F(t)=integral_0^t exp(-kappa(t-s))*phi(s)ds,
    phi=F'+kappa F.

The converse is obtained by integrating that first-order equation; no endpoint at L is imposed. The output-energy identity gives

    m^2=(sigma^2*kappa^2*c^2)/(2epsilon)
          *sup [integral W F^2]/[integral(F'+kappa F)^2].

The denominator expands EXACTLY to

    integral(F'^2+kappa^2 F^2)+kappa*F(L)^2,

because the cross term is kappa[F(L)^2-F(0)^2]. This proves the Rayleigh expression including its boundary term.

The denominator is a positive coercive form on H1 with F(0)=0; W is bounded, nonnegative and positive a.e. before L. Compact H1->L2 embedding gives attainment of the minimum denominator/weighted-norm quotient: normalize integral W F^2=1, take a weakly convergent bounded minimizing sequence, use strong L2 convergence to retain the normalization and weak lower semicontinuity for the energy. The minimum is positive by the coercive/Poincare estimate and is finite by any nonzero trial. This is the compact weighted Rayleigh principle at its actual domain, even though W(L)=0.

Its first variation against every H1 test G with G(0)=0 is

    integral(F'G'+kappa^2 FG)+kappa F(L)G(L)
       =lambda1 integral W FG.

Interior tests give `-F''+kappa^2 F=lambda1 W F`. Standard one-dimensional weak regularity supplies the endpoint derivative, and integration by parts with FREE G(L) gives precisely

    F'(L)+kappa F(L)=0.

A terminal Dirichlet condition would therefore be wrong. The reciprocal Rayleigh relation proves(8.2), including the full prefactor.

For the rational dimensionless base c=sigma=b=beta=1, kappa=1/(2L), epsilon=1/(4L), put x=t/L and f(x)=F(Lx). Then W becomes `1-exp(-(1-x)/2)`, and multiplying the physical differential equation by L^2 gives

    -f_xx+f/4=Lambda*W*f,   Lambda=lambda1*L^2.

The endpoint becomes `f_x(1)+f(1)/2=0`; the left endpoint remains f(0)=0. The physical prefactor is1/(2L), so

    m^2=[1/(2L)]/[Lambda1/L^2]=L/(2Lambda1).

This checks the source's exact normalization, not an eigenvalue of a different endpoint problem. L is the counted input length T-h throughout. The chosen rates satisfy the tame conditions at equality and are rational for every prescribed rational short horizon.

## 11. Claim-by-claim status and the exact one remaining enclosure

|Claim group|Written reconstruction status|
|---|---|
|Actual plant, stability, realized control bounds(2.2),(2.4),(2.5)|Reconstructed;0F/0M/0m|
|(2.3) literal causal transfer|Reconstructed APPLICATION at the precisely named Geiss–Scheutzow classical import; its external proof/sharpness is not newly validated|
|(3.1) square-root deficit|Independently derived;0F/0M/0m|
|Long/infinite screen/family|Retained at exact named prior written theorem after checking plant/admissibility/counted-horizon domains; no old computation or unqualified old formula repaired here|
|Full progressive short-horizon conditioning, compact attainment and strict supremum gap|Reconstructed;0F/0M/0m|
|Every prescribed rational short horizon/level and universal deterministic-test controller exclusion|Reconstructed;0F/0M/0m|
|Gaussian moments, infinite-Hilbert limits and(7.1)|Independently derived;0F/0M/0m|
|B bound, covariance kernel, Hilbert–Schmidt identity and terminal split(7.3)|Independently derived;0F/0M/0m|
|Reference BL/96, both q branches, entire-class delta1/18432|Independently derived;0F/0M/0m|
|Conditional interval/midpoint and r=1+B_*/A extraction|Independently derived;0F/0M/0m|
|Full Rayleigh/Robin identity and m^2=L/(2Lambda1)|Independently derived;0F/0M/0m|
|ACTUAL explicit rational enclosure meeting(8.1)|NOT_PROVIDED/NOT_RECONSTRUCTED as a finite certificate; expressly the source's next obligation, not an asserted completed result|
|Evaluated Lambda1,m_-,m_+,d,r or a numerical plant witness|NOT_PROVIDED; no value inferred or computed|

The single remaining explicit attack is a rigorous rational enclosure of the displayed dimensionless ground eigenvalue, with square-root/rounding buffers tight enough to furnish rational m_-,m_+ satisfying(8.1). Existence of some abstract rational brackets by density is not that certificate. Conversely the extraction algebra needs no additional stochastic optimization once such bounds are genuinely supplied.

No mathematical defect was found in the new claims at these stated scopes. Parent disposition is separate. Ordinary Brownian calculus, conditional expectations in separable Hilbert spaces, compact spectral/weak-convergence facts and Gaussian coordinates remain named classical foundations; no formal/kernel proof is claimed.

General prescribed-gamma N&S literal synthesis for arbitrary plants/controllers, exact optimal gains, optimal nonlinear-law structure, sharp constants, every unproved horizon extension, novelty and publication acceptance remain open exactly as the source states. The two feasibility directions concern different stated plants/horizons. No old unadmitted interpreter result, source hash, copied Boolean or reviewer agreement supplies an executable/configured-family/human/formal gate. All original deadlines and HOLD remain unchanged.
