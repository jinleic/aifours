# v67-A — written reconstruction of the finite-expression rational Robin certificate

Actual returned `/bin/date` before creation: **Sun Oct 25 09:41:42 PDT 2026**. Reviewer PhysicsAME46-2; author InfoHinfPreview-2. **WRITTEN supplied-proof review only.** No scientific interpreter/eval, arithmetic/symbolic program, support/spectral enumeration, eigensolve, interval program, sum/array/recursion materialization, certificate replay, simulation, scientific job, external-model CLI or nested agent was used. Metadata hashes/clocks and source reads only. V9/V10 and HOLD remain binding.

## 1. Verdict, representation level and actual complete intake

**FATAL0 / MAJOR0 / MINOR0 at the claimed CLOSED FINITE RATIONAL EXPRESSION theorem scope.** The exact kernel, positive polynomial operator, fixed-exponent trace enclosure, explicit finite integer moments, fixed rational Newton recursion, strict coefficient interval and actual plant formulas reconstruct below in writing.

At THIS representation level, v1's unknown-endpoint enclosure obligation is discharged: the endpoints and d,r are uniquely specified finite rational expressions with proved positive denominators and proved strict bounds. No unknown eigenvalue, residual integral, adaptive stopping/search rule or existential coefficient choice remains in those definitions.

**Not conferred:** expanded numeral/decimal witness, evaluated coefficient array, materialized huge integer/certificate, practical algorithm or complexity claim, independent executable/triple-checker/controls verification, configured-family/human/formal/kernel proof, novelty or full arbitrary-plant N&S synthesis. These are not synonyms for the written finite-expression theorem. The finite-witness assurance skill was read; its stronger verification procedure was NOT performed or authorized under HOLD.

Actual metadata hashes observed matching manifest/receipt:

- Manifest `peer-review-wave-eighteen-v67.json`: `ab11301168f1c04a22b5eed5f08c58c6e79a370c61b47eabb9a271fa504313da`.
- ALL assigned parts: ONE literal part `peer-review-wave-v67-v67-A-part1-v1.md`, `ec8e2abf40b4006534a46c5bed537ee3f8760bbce9152ae4c21e3e36a086433f`.
- S3, NEW414LF `literal-preview-separation-consolidated-v2.md`: `d1e367cff5a4098c60bd0e44226eec72b7c91ce7a69c538c1b680fc043e22173`.
- S4, complete459LF v1: `863df2a96cb6a547a88961b7e5d595590941333b61ef10508f40f092fc50050b` (same pinned source previously reconstructed, now supplied/read again).
- S5, complete26LF `preview-quantitative-gap-Robin-parent-v1.md`: `7c424a4d5196de7d6456316e00bfcfa680cc721380bde3c7d8432bfc5a82ff98`.

The COMPLETE993-line literal part was read RAW in windows1–175,176–340,341–510,511–690,691–860,861–993. This covers EVERY declared LF of S1/v9(35),S2/v10(31),S3(414),S4(459),S5(26), including all endings. No reader-truncated mathematical line remains. V9 was read FIRST, v10 immediately SECOND, before the exact own assignment/receipt; the long scope was recovered RAW. The byte-equality receipt was read, not treated as mathematical verification.

Serial v64-B was fully RETURNED before this duty. A FRESH exposure ACK was written at the actual09:34:20 observation BEFORE this body. Prior same-author/short-horizon/quantitative review exposure is disclosed; no prior verdict accepts the new414LF integer/trace/recursion certificate. S5:24 itself correctly reserves this successor. This is same-harness/different-domain supplied-proof review, not blind or stronger-family acceptance.

References below use ORIGINAL S3 line numbers; S4/S5 are identified explicitly.

## 2. Exact unit kernel, Robin normalization and theta lower bound — S3:53–95

The unit active-time deterministic operator is

    (A phi)(s)=1/sqrt(2)*sqrt(1-exp(-(1-s)/2))
                    *integral_0^s exp(-(s-v)/2)*phi(v)dv.

Multiplying the two kernels gives

    K(v,w)=1/2*exp((v+w)/2)
               *integral_a^1[exp(-s)-exp(-(s+1)/2)]ds,
    a=max(v,w).

The integral is EXACTLY

    exp(-a)-2exp(-(a+1)/2)+exp(-1)
      =[exp(-a/2)-exp(-1/2)]^2.

Thus equation(2) has the correct factor1/2 and no missing endpoint term. K=A^*A is positive compact, and its top eigenvalue is theta=m^2.

For the Volterra variable F, phi=F'+F/2 and F(0)=0. Its exact energy denominator is

    integral phi^2=integral(F'^2+F^2/4)+F(1)^2/2.

The endpoint at1 is FREE. The compact weighted Rayleigh principle therefore has natural boundary `F'(1)+F(1)/2=0`, not Dirichlet, and differential equation `-F''+F/4=Lambda*(1-exp(-(1-s)/2))*F`. The numerator prefactor is1/2, so theta=1/(2Lambda1). Coercivity/compactness and the weighted endpoint domain are those fully supplied/reconstructed in S4 and supported at S5, with no change in v2.

For the unit reference input phi=1, the actual first state is `f_s=1-exp(-s/2)>=s/4` on[0,1]. The OU squared kernel is at least1/2, using exp(-x)>=1-x for x<=1/2. Hence its variance is at least `integral_0^s(t/4)^2 dt/2=s^3/96`; integrating gives theta>=1/384. This is a written lower bound, not a computed spectral value.

## 3. Every Taylor/monotonicity/operator-error step — S3:99–146

Let x=v/2 in[0,1/2]. The positive degree40 exponential Taylor remainder is bounded by `exp(x)*x^41/41!<=2^-40`; exp(1/2)<2 follows directly by comparison with the geometric series, with strict improvement in higher factorial terms. Thus E is positive and at most exp(v/2)<2.

The even alternating degree40 polynomial Q has error at most `x^41/41!<=2^-41` and is at least exp(-v/2). Its derivative is exactly `-Q39(v)/2`. Grouping Q39 gives

    Q39(v)=1-x+sum_(k=1)^19 x^(2k)/(2k)!*[1-x/(2k+1)]
            >=1-x>=1/2.

Therefore Q is decreasing. Since Q(0)=1 and Q(1)>=exp(-1/2)>=1/2, its difference Q(v)-Q(1) is in[0,1/2]. The exact exponential difference is in the same interval. Their difference is at most2*2^-41=2^-40, so their squared difference is at most2^-40, by multiplying by a sum at most1.

The error in E(v)E(w) versus exp((v+w)/2) is at most4*2^-40, since each factor is bounded by2. Decomposing the kernel difference using the exact squared difference and the exponential-product error gives

    |K-K0|<=1/2*[(4*2^-40)*(1/4)+4*2^-40]
           =(5/2)*2^-40<2^-38.

On the UNIT interval the uniform kernel bound bounds the L2 operator norm: Cauchy–Schwarz bounds each integral by the uniform constant times||f||2, then integrates over length1. Thus the norm bound in(6) follows, and eta=2^-36 is indeed a looser strict allowance. No sampled coefficient/error assertion is used.

### Positivity is a factorization, NOT a consequence of closeness

J=(Q-Q(1))^2 is nonnegative, decreasing, and zero at1, with `-J'>=0`. Define the Hilbert–Schmidt integral map

    (Bf)(s)=sqrt(-J'(s)/2)*integral_0^s E(v)f(v)dv.

Its kernel is square integrable. Direct multiplication gives B^*B=K0 because integrating -J' from max(v,w) to1 gives J(max(v,w)). Hence K0 is POSITIVE trace-class, independently of its closeness to K.

Its trace is ||B||HS^2, and nonnegative Fubini yields exactly `tau1=(1/2) integral E(v)^2 J(v)dv<=1/2`, since E^2<=4 and J<=1/4. Rayleigh comparison gives |theta-theta0|<eta. Consequently theta0>1/512: the margin `1/384-1/512=1/1536` exceeds eta. The top spectral value and every later trace denominator are therefore positive without a numerical eigenvalue test.

## 4. Universal trace-moment ratio, NO gap or rank hypothesis — S3:150–194

For any nonzero positive compact trace-class H, its top eigenvalue lambda>0 is attained. Write its eigenvalues as lambda*p_i, with0<=p_i<=1 and some p_i=1; sum p_i=Tr(H)/lambda is finite. Therefore all positive integer moments are finite and positive.

The exact ratio deficit is

    lambda-mu_n=lambda*[sum p_i^n(1-p_i)]/[sum p_i^n].

The denominator is at least1. Since `sum_(j=0)^(n-1)p^j>=n*p^(n-1)`, multiplication by1-p gives `n*p^(n-1)*(1-p)<=1-p^n<=1`. Multiplying by p gives `p^n(1-p)<=p/n`. Summing nonnegative terms therefore proves

    0<=lambda-mu_n<=lambda*sum p_i/n=Tr(H)/n.

This is homogeneous and valid for countably infinite spectra, arbitrary multiplicity and arbitrarily small/zero spectral gaps. No finite-rank or Perron-gap estimate is hidden.

For the PARTICULAR K0, use FIXED N=2^30 and trace<=1/2. Then `mu<=theta0<=mu+1/(2N)`. Combining the operator allowance gives l=mu-eta<=theta<=nu=mu+1/(2N)+eta.

The positivity/width assertions reconstruct exactly: theta0>1/512 implies `l>1/512-2^-31-2^-36>1/1024`; mu<=theta0<=1/2 gives nu<1. The width is `2^-31+2^-35<2^-30`. Dividing by l>2^-10 gives `nu/l<1+2^-20`. Since Lambda1=1/(2theta), the reciprocal interval and its ratio in(11) follow. N is fixed BEFORE any numerical output; the proof does not choose it by an observed stopping condition.

## 5. Integer definitions, cycle-order counts and the EXACT finite moment formula — S3:200–249

All the following is reconstruction of the written finite expression. NO coefficient vector, permutation family, power, A_N integer or recursion was generated/evaluated.

### 5.1 Every coefficient is an integer with the right common denominator

For0<=j<=40,

    u_j=D/(2^j*j!)=2^(40-j)*(40!/j!)

is an integer; q_j=(-1)^j u_j is too. U and V are fixed integer polynomials, with V(1)=0, and E=U/D, J=V^2/D^2.

For e=0,1,2, the exponent4-2e is respectively4,2,0, all nonnegative. U^2 V^(2e) has degree at most80+80e<=240. Thus the a_e,j in(12)'s setup are fully determined INTEGERS with zero padding through240. Equivalently they are finite convolutions of at most six fixed degree40 coefficient lists; the constant coefficient of V is q0-sum q_j, and its other coefficients are q_j. Coefficient extraction here is a finite polynomial definition, not an oracle or unspecified solve.

The scaling is exactly

    D^-6 sum_j a_e,j*z^j
      =D^(-2-2e)*U(z)^2*V(z)^(2e)=E(z)^2*J(z)^e.

The power D^6 per vertex is therefore correct for ALL three e possibilities, not just for the maximal degree.

### 5.2 Every order-simplex and every cycle edge is accounted for

For integer n>=3, the n-cycle has precisely n edges and each vertex degree2. Partition[0,1]^n into the n! order-simplexes, with ties a measure-zero set. If z_k is the kth variable in the order pi, each cycle edge contributes J at its HIGHER-ranked endpoint. Therefore e_k(pi) is in{0,1,2}, sum e_k=n, and every edge is assigned ONCE. Each vertex receives E twice from its two incident kernel factors. Thus the cycle integrand is exactly

    2^-n product_k E(z_k)^2*J(z_k)^(e_k).

No orientation factor or omitted n! occurs: the SUM over all pi explicitly covers all simplexes. Higher-endpoint assignment, not a freely chosen exponent vector, is used in A_n.

The continuous bounded Hilbert–Schmidt kernels give the trace contraction `Tr(K0^n)=integral_cycle product K0`. One may justify it by iterated kernel composition and the Hilbert–Schmidt trace pairing; boundedness permits Fubini, and the pointwise kernel is also nonnegative. No assumed finite rank or digit computation is needed.

### 5.3 Exact integration and factorial divisibility

Successive integration over0<=z1<=...<=zn<=1 gives

    integral product z_k^(j_k) dz
       =product_(k=1)^n 1/(j1+...+jk+k).

Each denominator is a positive integer at most241k<=241n, because0<=j_k<=240. It therefore divides F_n=(241n)!, so every ratio F_n/(prefix+k) is an integer. The definition of A_n is a CLOSED FINITE sum of products of those integers and the signed a's; it is a definite integer, not a recipe to wait for a future estimate.

Restoring the common polynomial and integration denominators yields EXACTLY

    tau_n=A_n/[2^n*D^(6n)*F_n^n].

Taking the quotient n=N+1 over n=N cancels to

    mu=A_(N+1)*F_N^N/[2*D^6*A_N*F_(N+1)^(N+1)].

This verifies the factor2, all D/F exponents and the absence of a missing simplex factorial.

Since K0 has theta0>1/512, tau_n>0 for every positive n. Its exact denominator is positive, hence A_n>0, in particular A_N and A_(N+1). The polynomial summands can have either sign; positivity is proved through the operator identity, NOT inferred from coefficient signs or an observed huge integer. Consequently no zero denominator is hidden in mu,l,nu.

The finite moment expressions contain no residual integral or spectral datum. Their use as exact rational definitions is proved; their expanded numerals, memory requirements, runtime practicality and independently executed verification remain UNPERFORMED and unclaimed.

## 6. Quantitative Gaussian/full-progressive bridge and scaling — S3:253–291

The exact Gaussian moment/deficit and compact/conditioning foundations are supplied completely in S4 and have the separate parent support S5. Their v2 specialization also reconstructs:

- Eigen-coordinate expansion gives normalized second/third moments `1+2s2` and `1+6s2+8s3`; finite nonnegative truncations converge by monotone convergence and trace finiteness. The square-root deficit identity gives at least s2/12, since s3<=s2. No finite Gaussian rank is assumed.
- For a unit deterministic input, `|f_t|^2<=t/4`, and the safe B=1/4 bounds variance. OU covariance and the terminal-mass split give `Tr(Gamma^2)>=q^3/(8B)`. The reference input gives m^2>=B/96. For q>=m^2/2, s2>=1/1536 and the deficit is at least1/18432. For smaller q, Cauchy–Schwarz gives m/sqrt2, below that same bound. This covers EVERY deterministic input, not just an eigenfunction.
- With L=T-h<=h, the whole random counted input is an F_L-measurable L2-valued variable BEFORE output noise starts. For simple such random elements, independence of future Brownian increments gives the deterministic conditional response law. Square-mean approximation and continuity of J pass to all inputs; these approximants only parameterize post-h stochastic integrals and are not asserted anticipative admissible inputs before L. Taking expectation preserves EXACTLY E||w||, not RMS input energy.

For physical L, rates kappa=1/(2L),epsilon=1/(4L) and c=sigma=1 rescale the unit zero-law response. A unit physical input is the time-rescaled unit input divided by sqrt(L); f scales by1/sqrt(L), and future Brownian increments by sqrt(L), so the rescaled y path has the unit law. Physical output energy adds factor L. Therefore `m_L^2=L*theta` and the literal gain retains the same relative gap `ell_L<=(1-delta)*m_L`, delta=1/18432, for the full progressive class.

This scaling concerns u=0. Arbitrary controls, including pre-action, are handled by the actual physical control map below, not by assuming their output is conditionally Gaussian.

## 7. Fixed Newton recursion, ALL rational L and the strict buffer — S3:293–319

Write the prescribed positive rational L uniquely as A/B in lowest positive terms; let S=A+B>=2. The definitions use exactly J_*=S+64 rational Newton updates. No stopping test or unknown square root appears in their execution-free definition.

For the proof only, put g=sqrt(L*nu). Since nu<1 and L=A/B<=A<=S, q0=S>=g. Every positive iterate satisfies

    q_(j+1)-g=(q_j-g)^2/(2q_j)>=0,
    q_(j+1)-g<=(q_j-g)/2.

Thus q_j remains positive and at least g; all divisions are legitimate. Also nu>1/1024 gives `g>1/(32B)`. The relative error after the FIXED updates is at most

    32BS*2^(-S-64)<=2^-58.

Indeed B<=S, and S^2<=2^(S+1) for S>=2: check S2/3, then `(S+1)^2<=2S^2` for S>=3 supplies induction. This proves the bound for every positive rational L without expanding its recursion.

Now m_+=q_J>=sqrt(Lnu)>=m_L. Since q_J>=sqrt(Lnu)>=sqrt(Ll), `m_-=Ll/q_J<=sqrt(Ll)<=m_L`; both endpoints are positive rational definitions. Squaring the relative error yields `q_J^2/(Lnu)<1+2^-56`. Combining with nu/l<1+2^-20 gives

    m_+/m_-< (1+2^-56)(1+2^-20)<1+2^-19.

Finally2^-19<delta because2^19>18432; hence `(1-delta)*(1+2^-19)<1`. This proves the REQUIRED strict buffer(16), not only a nonstrict enclosure. The recurrence's fixed index and rational initial value contain no oracle, eigenvalue or adaptive termination choice.

## 8. Actual specified d/r and all-controller conclusion — S3:323–390

The d in(17) is the rational MIDPOINT of the strict endpoint interval. Thus

    d*ell_L<=d*(1-delta)*m_+<gamma<d*m_-.

For b=beta=c=sigma=1, the deterministic control convolution gain is4L and the stochastic one sqrt(2L). The rational U=1+2L satisfies `U^2-2L=1+2L+4L^2>0`, so the physical map has Mbar=d(1+6L), as claimed. Its integrals begin at0; every preview pre-action remains counted, with positive r*u penalty. Zero extension after T is only an upper estimate for that causal input/output map, not a feedback reset.

A_*=d^2*m_-^2-gamma^2 is strictly positive; B_*=gamma^2*Mbar^2 is nonnegative. The specified rational r=1+B_*/A_* obeys

    r^2*A_*=A_*+2B_*+B_*^2/A_*>B_*.

Consequently the source's strict mean-square lower level is correct. For any realized progressive law, linear plant variation of constants gives `d*y=d*y0+S_d u`. Infinite N2 output already fails. Otherwise r*u forces finite N2(u), so the mean-square convolution bound and scalar Cauchy–Schwarz yield

    N2(d*y0)<=sqrt(1+(Mbar/r)^2)*N2(z).

The same deterministic mean-square norm-maximizing input supplies the lower bound against EVERY controller; a norm-approaching sequence would suffice. This includes nonlinear, nonstationary, arbitrary-history/horizon-aware laws and all pre-action under the disclosed strong well-posedness assumptions. No optimal linear-feedback assumption, future-noise controller or extra energy-history input is introduced.

For the canonical h1,T2,gamma1: L1 gives S2 and EXACTLY66 updates from q0=2. Substituting m_-=l/q, m_+=q and1-delta=18431/18432 gives

    d=(18431*q^2+18432*l)/(2*18431*l*q),
    r=1+49*d^2/[d^2*(l/q)^2-1],

exactly(19). The d denominator and the r denominator are positive by the established bounds. Both matrix entries are fully specified rational numbers through the finite integer sums/recursion, not interval selections.

The displayed matrices reproduce kappa1/2,epsilon1/4,b=beta=c=sigma1 and the actual delayed forcing w(t-1). D1^T D1=r^2>0 and both actuation channels affect y. Input is counted ONLY on[0,1], output on[0,2]. Under u=0 and zero input, Itô gives

    d/dt E(2f^2+y^2)=-E f^2-(1/2)E y^2
                      =-(1/2)E(2f^2+y^2),

including the diffusion correction. Thus the stated actual rational plant is internally mean-square stable under its exhibited literal-feasible law, yet every admissible controller is mean-square-infeasible at gamma1. This is a written theorem about the SPECIFIED finite expressions; their expanded digits were not computed or checked.

## 9. Explicitness audit and exact non-acceptances

There is no remaining unspecified spectral endpoint in this scoped example family:

- D, u_j, q_j, U,V, a_e,j are fixed integer/polynomial definitions with finite bounds.
- N=2^30 is fixed; A_N and A_(N+1) are fixed finite sums over fully specified index universes and exact factorial ratios.
- Their denominator positivity follows from an already proved positive operator, not an unknown numerical sign.
- mu,l,nu are rational arithmetic of those integers, with rigorous analytic bounds for THEIR actual values.
- J_*=A+B+64 is fixed by the given input rational L, and every Newton iterate is positive rational.
- m_-,m_+,d,r and the canonical matrices therefore contain no eigenvalue, integral, search, floating output, empirical table or unknown stopping criterion.

This closes v1's ONE Robin/coefficient-extraction obligation at the written FINITE-EXPRESSION level. It does not claim that the astronomically large expressions were expanded, that a finite certificate file was consumed by independent checkers, or that the representation is practical. In particular this review supplies NO executable/triple-verification/controls/model-family/human/formal/novelty gate. Named compact/trace-class and Hilbert–Schmidt trace-contraction facts are ordinary mathematical imports, not machine-certified implementations.

|Asserted new claim|Written status|
|---|---|
|Exact unit K, Robin prefactor and theta>=1/384|Reconstructed;0F/0M/0m|
|Degree40 remainder/Q39/J bounds and norm error|Reconstructed;0F/0M/0m|
|ACTUAL positive Hilbert–Schmidt factorization and trace bound|Reconstructed;0F/0M/0m|
|Universal trace-moment ratio for arbitrary positive trace-class H|Reconstructed without gap/rank assumption;0F/0M/0m|
|Fixed N, l/nu positivity/enclosure/strict ratio|Reconstructed;0F/0M/0m|
|All integer powers, cycle-order simplexes, prefix denominators/F divisibility, tau/mu formula|Reconstructed;0F/0M/0m|
|A_N positivity independent of signed coefficient guesses|Reconstructed through positive-operator identity;0F/0M/0m|
|Fixed Newton J_* and all-rational-L relative errors|Reconstructed;0F/0M/0m|
|m brackets/strict buffer, specified d/r, canonical matrices/storage and all-control inequality|Reconstructed;0F/0M/0m|
|Expanded numeric object, actual N-sums/arrays/recursion execution or efficient implementation|NOT_PERFORMED/NOT_CONFERRED; expressly outside source claims|

No asserted new mathematical identity remains NOT_RECONSTRUCTED at this representation scope. The declared limits are not silently replaced by a stronger finite/executable acceptance.

## 10. Retained imports and genuinely open original problem

The named v1 long/infinite opposite-feasibility direction retains its exact plant/horizon theorem and its Geiss–Scheutzow import: monotone nonnegative adapted right-continuous accumulated energies, predictable input energy, and conditional domination at EVERY bounded stopping time. Stopping the INPUT, preserving its earlier output and discarding the later nonnegative output supplies that hypothesis; initial-event locality supplies its conditional form. The external theorem's proof/sharpness is not newly validated. All old unadmitted arithmetic retains ZERO credit. The new short family itself needs no new Geiss/BDG constant.

The long and short directions concern different plants/horizons. There is no same-plant same-level contradiction, infinite-horizon opposite theorem or unqualified quadratic substitute for the printed objective.

The ORIGINAL general arbitrary-plant prescribed-gamma/horizon synthesis problem remains OPEN. Its stated first missing necessity-and-realization bridge from the full non-Hilbert gain requirement to non-tautological finite-dimensional operator/storage/LMI conditions at the SAME level is not supplied by these examples. No unrestricted optimal linear-feedback, differentiability/stationarity, arbitrary-memory substitution or general controller-realization theorem follows.

Disposition: **WRITTEN_SUPPORTED at the exact finite-expression scoped-family level, subject to separate parent union/import disposition.** No formal/kernel/human/configured-family/executable/novelty acceptance, numerical expanded witness, practical-complexity claim or full-book solution. Original cutoff/deadline and HOLD are unchanged.
