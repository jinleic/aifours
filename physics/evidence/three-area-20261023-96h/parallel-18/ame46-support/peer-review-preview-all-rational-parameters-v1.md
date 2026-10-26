# v29-G — written reconstruction of the all-rational-parameter preview separation family

Actual `/bin/date` before creation: **Sun Oct 25 04:18:56 PDT 2026**. Reviewer PhysicsAME46-2, physics-6; author InfoHinfPreview. **WRITTEN supplied-proof reconstruction only. No scientific eval/interpreter, enumeration, symbolic program, numerical calculation, certificate replay, native scientific launch, external-model CLI or nested agent was used for this review.** Metadata clocks/hashes and source/image reads only. Parent erratum v7 and HOLD v2 are binding.

## 1. Verdict, exact pins and exposure

**FATAL: 0; MAJOR: 0; MINOR: 0 at the stated separating-family theorem scope.** The analytic proof and the rational constants needed for its two claimed gain bounds are reconstructed below in writing. This is not a finite-certificate execution verdict, historical-checker attestation, arbitrary-plant synthesis theorem, formal/kernel proof, human/cross-vendor review or novelty clearance.

The conclusion is conditional on the packet's DISCLOSED interpretation of the book's missing admissibility details and on its explicitly named classical stochastic-calculus and monotone-domination imports. No correctness verdict was supplied by the parent.

- Manifest: `peer-review-wave-eighteen-v29.json`, SHA256 `fd47c873613f88a299c4cf170fdabba86125d03e592e02c40651b9f24d3504e8`, exact entry v29-G at LF204–232.
- Literal packet: `peer-review-wave-v29-preview-all-rational-parameters-sources-v1.md`, SHA256 `5f7825022117e1c7dcd9e1b5af4235f492d343c0cceb2ba84369893560d45628`.
- Proof P: `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/proof-general-parameter-separation-v1.md`, SHA256 `58777c6e1b7b83766d0a969cfd0dbca4b41729577de732ece5dd2a1ad861d575`, complete LF1–427.
- Companion J: same root `family-rational-verification-v1.json`, SHA256 `12f7dcbd815f7a3917416d1a7e76a8227ace60c63f7b2758efb64eac27460593`, complete LF1–165.

All four hashes above were actually observed with metadata-only SHA operations and match the manifest/packet receipt. The COMPLETE606-line literal packet was read, covering every declared P and J line. No unread or reader-truncated mathematical line remains in that packet. `parent-evidence-erratum-v7.md` and the metadata packet receipt were read first.

Exposure: this fresh-context reviewer had no prior Hinf-preview primary/review reconstruction in this resumption. The current author proof, companion data, assignment scope and parent process qualifications were supplied. This is not blind or independent-model-family review. Earlier AME owner arithmetic is unrelated and has no review credit here.

## 2. Printed criterion and quantifiers — P18–27,33–50

Both ACTUAL source images `pdfpage-0695.png` and `pdfpage-0696.png` were opened and read. Printed674 defines the pathwise L2 norm and the delayed-disturbance plant. Printed675 places expectation OUTSIDE each norm, has control law `F(x(t),w(s)|t-h<=s<=t)`, and divides by the input norm on the interval ending at b-h. Thus the packet correctly distinguishes

    N1(v)=E sqrt(integral |v|^2),
    N2(v)=sqrt(E integral |v|^2).

The book images do not spell out all stochastic disturbance/controller conventions. P25 openly fixes zero initial state, zero negative-time disturbance history, progressively measurable square-energy disturbances and well-posed nonanticipative zero-preserving controllers. The result is supported under THAT stated interpretation, not as a newly established verbatim quantifier in the book.

Allowing every realized progressively measurable locally square-integrable control with a strong nonexplosive solution genuinely enlarges the printed state/window class: the preview window ends at current time t, not a future Brownian time. Therefore excluding that enlarged class excludes the stated printed class. Conversely the feasible controller u=0 has exactly the printed form. No restriction to stationary, linear or differentiable feedback is introduced.

The matrices in P44–47 reproduce the displayed cascade: the disturbance enters f through nonzero kappa*c; f enters y diffusion through nonzero sigma; b and beta both actuate y; the output stacks d*y and r*u. Thus neither drift actuation, diffusion actuation nor the control penalty is fictitious. `D1^T D0=0` and `D1^T D1=r^2>0` follow immediately from their disjoint output coordinates.

## 3. Brownian exit moments and the random denominator — P110–178

For mu1, half its second derivative is -1. For mu2, half its second derivative is `-2+2x^2=-2mu1`. For mu3 it is `-5+6x^2-x^4=-3mu2`. Direct substitution x=±1 gives zero. The displayed factorizations are correct: expanding `(1-x^2)(61-14x^2+x^4)` gives `61-75x^2+15x^4-x^6`; its second factor is at least47 on [-1,1]. The other nonnegative factors are immediate.

The moment identification is not circular. Stopped Dynkin for bounded mu1 first gives `E(tau wedge t)<=mu1(x)`, hence a.s. finite tau and finite first moment. Bounded convergence at the exit boundary then identifies the first moment. For j=2,3 the bounded stopped generator identity passes to `mu_j(x)=j E integral_0^tau mu_(j-1)(B_s) ds`. The previously established remaining-time moment, strong Markov property and Tonelli identify this with `E tau^j`. Finiteness follows from the bounded mu_j, rather than being assumed to justify an unbounded stopping identity.

At x=0 the moments are 1,5/3,61/15. For A=tau-1,

    E A^2 = 5/3-2+1 = 2/3,
    E[A^2(tau+1)] = E[tau^3-tau^2-tau+1] = 12/5.

Cauchy–Schwarz applied to `|A|/sqrt(tau+1)` and `|A|sqrt(tau+1)` gives `E[A^2/(tau+1)] >= (2/3)^2/(12/5)=5/27`. Since `(sqrt(t)+1)^2<=2(t+1)`, the squared root deviation has mean at least5/54. The identity `E(sqrt(tau)-1)^2=2-2E sqrt(tau)` then yields `E sqrt(tau)<=103/108` exactly.

Brownian scaling gives the a-scaled moments and root bound. The exit-time indicator disturbance is adapted, controller-independent and has finite expected input energy a^2. For finite time, truncating at L=T-h gives input norm `E sqrt(tau_a wedge L)<=a*(103/108)`, strictly positive because L>0 under F0. The proof does NOT replace this random denominator by the square-energy denominator. No deterministic-disturbance substitute is being used.

## 4. OU anchor and actual preview/filter errors — P184–253

Integration by parts for the stopped Brownian martingale gives the claimed formula `Z_t=M_t-epsilon integral_0^t exp(-epsilon(t-s))M_s ds`. At its a.s. finite exit time,

    |Z_tau| >= a-a(1-exp(-epsilon*tau))
             = a exp(-epsilon*tau) >= a(1-epsilon*tau).

The later comparison diffusion forcing is zero. Its exact infinite tail norm is `|Z_tau|/sqrt(2epsilon)`. Averaging with `E tau_a=a^2` yields P200. No unbounded optional-stopping assertion for Z, conditional independence of a future event, or rare-event cutoff is required.

For the finite test, the event `tau_a<=a^2 R` is wholly inside [0,T-h]. Its tail from tau_a to T has the stated square-root factor. F0, e>2 and `sqrt(1-s)>=1-s` bound that factor below by `1-2^-m`. The second moment gives `P(tau_a>a^2R)<=5/(3R^2)`. Combining the endpoint estimate with the unconditioned first moment gives P222 and hence P228–229. Only the tail INSIDE [0,T] is used. Input after T-h is zero.

The low-pass error is also reconstructed. Writing zeta=exp(-kappa*theta), the rise integral is `(1-zeta^2)/(2kappa)` and the post-input filter tail integral is `(1-zeta)^2/(2kappa)`. Their sum is `(1-zeta)/kappa`, because `(1-zeta^2)+(1-zeta)^2=2(1-zeta)`. The delayed and undelayed indicator intervals have symmetric difference at most2h. Minkowski in the product time/probability L2 space therefore gives `N2(F-w)<=kappa^(-1/2)+sqrt(2h)<=p+q`.

Itô isometry/Tonelli for the OU error multiplies this bound by `|d*sigma*c|/sqrt(2epsilon)=H`. Jensen gives N1<=N2. Thus the actual uncontrolled output obeys `N1(d*y0)>=HaQ` for either Q. In finite time, the full extension is used only to UPPER-bound the error; the lower anchor stays on [0,T]. Delay and finite-rate filtering are genuinely included.

## 5. All-controller exclusion and the classical norm import — P257–293

For any realized control, linear variation of constants gives `d*y=d*y0+S u`, including BOTH the ordinary drift convolution and stochastic diffusion convolution. This does not require that the controller itself be linear. Their square-energy norms are bounded by `|d*b|/epsilon` and `|d*beta|/sqrt(2epsilon)` respectively, so their sum is at most Mbar by `2epsilon U^2>=1`.

The actual primary statement of Geiss–Scheutzow Theorem2.2 was independently read at <https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2>. It requires nonnegative nondecreasing adapted right-continuous X,G, predictable G, and conditional domination at every bounded stopping time; its p=1/2 constant is sqrt2. The paper's proof and sharpness are classical imports, not formally reproduced by this review.

Here take accumulated output energy X and `G_t=Mbar^2 integral_0^t u^2`. Both are continuous nondecreasing and G is predictable. For bounded stopping time s, stop the INPUT at s. Causality preserves the original output through s; its later output energy is nonnegative. Applying the full square-energy bound to that stopped input gives `E X_s<=E G_s`. Multiplication by any initial-measurable event commutes with this causal linear operator and with the Itô integral, supplying the conditional version. Therefore P276 follows from the precise theorem, not from a deterministic-horizon bound alone.

When only N1(u) is finite, stopping accumulated control energy at n makes the input square-energy integrable. The same estimate applies. On paths of finite total control energy, all sufficiently large stops leave the entire input path unchanged; local uniqueness/causality and Fatou yield the extension. For finite time, zero extension of the REALIZED input after T preserves S through T; it is not a reset of the feedback law. These details support the enlarged control quantifier.

If N1(z) is infinite, failure is immediate. Otherwise `N1(u)<=N1(z)/r` is finite, so the extension is available. The final bound is a pathwise two-dimensional Cauchy–Schwarz argument followed by expectation:

    N1(d*y0) <= N1(d*y)+sqrt2*Mbar*N1(u)
              <= sqrt(1+2Mbar^2/r^2)*N1(z)
              < (1+rho)*N1(z).

The strict control inequality implies the last comparison; the nonstrict bound in P289 is therefore valid. Combining with the actual denominator at Section3 gives the uniform gain lower bound. This excludes even enlarged controllers, without using an optimality equation, differentiability, a Brownian reset or finite-N2(u) restriction.

## 6. Mean-square feasibility and complete strict storage — P297–339

The actual delayed low-pass map F is a pathwise L2 contraction by its nonnegative unit-mass kernel. Itô isometry integrates the OU kernel's squared mass to1/(2epsilon). Therefore `N2(d*y0)^2<=H^2*N2(w)^2` for every adapted square-energy input. Restricting the output to [0,T] and zero-extending the counted input is legitimate. This proves the stated upper bound for u=0, not just the special exit-time input.

The homogeneous storage V0 has f^2 drift coefficient `-(sigma^2+1)+sigma^2=-1` and y^2 coefficient `-2epsilon`. The claimed positive exponential rate relative to V0 follows. Zero-state gain is not being substituted for internal stability.

For the strict certificate, write pf and py as P317–318. The four coefficients of the complete state/input quadratic form are reconstructed without a symbolic program:

- f^2: `-2kappa*pf+sigma^2*py=(-3eta^2+H^2)/(2c^2)`;
- y^2: `d^2-2epsilon*py=-epsilon*(eta^2-H^2)/(c^2*sigma^2)`, using `d^2=2epsilon H^2/(c^2 sigma^2)`;
- f*v: `2kappa*c*pf=2eta^2/c`;
- v^2: `-eta^2`.

These are exactly the expansion of the three negative squares in P330–332 and J62–73. Their weights are strictly positive; their common zero forces f=y=v=0. The FULL joint matrix, not merely a state principal block, is negative definite.

The stopped Itô storage argument keeps the sigma^2 correction and the martingale, then uses nonnegative terminal storage and standard localization/Fatou. The delayed finite input identity is exactly `integral_0^T v^2=integral_0^(T-h) w^2` under zero negative history. No storage bound is claimed for the wrong denominator interval.

## 7. Universal rational construction and both exact gain fractions — P343–407

For positive rational h,gamma, `a=512(1+h)` is rational and positive. Its required inequality follows from `2(1+h)^2-h=2+3h+2h^2>0`. Thus no irrational square-root choice is needed. Every coefficient in P351–356 is rational, and b,beta,c,sigma,d,r are nonzero.

Substitution gives, in ordinary written arithmetic,

    H=64gamma/65,
    kappa*p^2=4,
    2epsilon*U^2=289/256,
    E0=1/128,
    q^2>=2h.

Since r=16Mbar, the control slack divided by r^2 is `(257-128)/16384=129/16384`. With H=128gamma/130 and eta=129gamma/130, the two level slacks are257gamma^2/16900 and259gamma^2/16900. F0's tail expression is `(2080-32)/256=8`; T-h exceeds32a^2 using the displayed h bound.

The exact anchors and threshold can be reconstructed compactly:

    Qinf=1-1/512-1/128=507/512,
    QT=(255/256)*(3061/3072)-1/128=258137/262144,
    threshold=(65/64)*(103/108)*(129/128)=287885/294912.

For the infinite margin use `507*576=292032`, so its numerator is292032-287885=4147. For the finite margin use denominator2359296: the two numerators are258137*9=2323233 and287885*8=2303080, difference20153. Consequently

    Qinf/threshold=292032/287885=22464/22145>1,
    QT/threshold=2323233/2303080>1.

These are precisely the infinite and finite lower gain factors. The mean-square upper factor64/65 is simultaneously strictly below1. Neither factor is asserted to be the exact optimal gain. The finite construction supplies T=2080a^2, not every preassigned finite horizon.

The small canonical member is consistent: a=1 gives Mbar=(4/65)*529=2116/65 and r=33856/65. The remaining canonical slack entries in J123–132 are also reconstructed by direct expansion:3;1/131072;33/256;36099489/16900;257/16900;259/16900;536870911/262144;0;14230271/530841600;93234085889/5741582745600. For the two larger squared margins a hand-checkable route is

    (H*Qinf)^2-[q0(1+rho)]^2
      =(39/40)^2-(4429/4608)^2
      =14230271/530841600,

    (H*QT)^2-[q0(1+rho)]^2
      =[258137/(65*4096)]^2-(4429/4608)^2
      =93234085889/5741582745600.

For the latter common denominator5741582745600 the two numerators are5397411572289 and5304177486400. Their positive difference is the claimed numerator. These are written equalities, not rerun outputs.

The three extra prescribed pairs in J139 fall under the universal construction already reconstructed; sample-wise checker execution is not needed to prove those mathematical instances. The claimed occurrence/results of the old sample loop itself are NOT_INDEPENDENTLY_ATTESTED.

## 8. Findings, non-acceptances and exact unresolved obligations

No author mathematical defect was found at the stated scope. No repaired proof or narrowed substitute was needed.

The historical phrases “permitted operation,” “WRITTEN-checked-in-kernel,” “machine-checked,” and “these checks certify” in P5,16,335,413–423 and J6,12–27,35–45,74,80,141 are governed by parent erratum v7. Their old outputs are preserved but **receive NO executable-verification, finite-certificate or retroactive-admission credit**. The erroneous permission was parent-originated, not attributed as an owner refusal. The review above independently reconstructs the needed algebra in writing; it does not rehabilitate those computations.

Explicit NOT_RECONSTRUCTED/NOT_ATTESTED items:

- The historical sparse-rational-function implementation, its zero-numerator booleans, elapsed execution, optional-import failure and actual sample assertions were NOT replayed or independently source-bound here. Their observed-execution claims are author receipts only; the mathematical identities needed by SF were reconstructed above instead.
- The primary source's proof/sharpness of monotone Lenglart and the general foundations of Itô/Dynkin, Brownian strong Markov/scaling and stochastic localization remain NAMED CLASSICAL IMPORTS, not formal derivations or machine certificates.
- Arbitrary-plant necessary-and-sufficient literal synthesis, exact optimal gains for the cascade, separation on every preassigned short finite horizon, sharp constants, optimal-law regularity, novelty/publication clearance, and a full-book solution remain OPEN/NOT ESTABLISHED exactly as P427 states.

The conclusion is therefore **WRITTEN_SUPPORTED at the supplied separating-family scope**, subject to the named stochastic imports and disclosed admissibility interpretation. Parent disposition is separate. No computation, certificate gate, arbitrary-plant N&S criterion or outside-model acceptance follows from this review.
