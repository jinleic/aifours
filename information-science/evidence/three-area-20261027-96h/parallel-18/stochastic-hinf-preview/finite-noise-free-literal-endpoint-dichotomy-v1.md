# Finite-horizon literal strictness: essential-norm dichotomy and an actual nonattaining family

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 17:05:30 PDT 2026**. Admitted non-construction structural/strictness work. This does NOT use the stopped diffusion-annihilating controller route: the stated plant has A0=B0=0 as GIVEN physical data, not as equations solved by a controller. No storage/dissipation certificate, old guide, new source or scientific execution.

## 1. Entire deterministic-state subclass and actual literal operator

Fix all compatible real A,B,C,D0,D1, zero physical A0=B0, finite T>h>=0, zero state/history and the full bound deterministic stationary linear preview law with K,L0,Lh,H. Inputs are canonical progressive E2 on [0,T-h], zero-extended. At h=0 combine endpoints and omit the kernel.

The state equation is an actual ordinary linear ODE driven samplewise by the input; finite-horizon unique/progressive E2 state/control follows from the explicit bounded window operator. The ORIGINAL output is therefore a bounded deterministic path operator

`z=T_F w`,

with

`T_F=D_feed+K_compact`,

`D_feed=(D1L0)E0+(D1Lh)Eh` for h>0, and the combined tap for h=0. The dynamic Volterra term and direct L2-kernel term are compact by their square-integrable finite-horizon kernels. No other state/output/controller is substituted.

Set `g=||T_F||`. Pathwise boundedness and the inclusion of actual deterministic inputs give **G_prog=G_det=g** at the ORIGINAL expected-path-norm criterion. Define

`e=||B_(ceil((T-h)/h))||` for h>0,

`e=||D1(L0+Lh)||` for h=0.

The exact all-chain/essential-norm result in current source `direct-preview-tap-chain-essential-bound-v1.md`, SHA `240ca6c4b186835b46da8978e9b551c230c3b6686cae1643a2504729d8abc76f` (UNREVIEWED), identifies ||D_feed|| and its essential norm as e, with complete real zero-extended time fibers. These are not separate unconstrained coefficient profiles.

**Theorem A.** If **g>e**, the actual finite-horizon deterministic operator attains its norm at a nonzero real input. Thus for g>e, pointwise-strict and uniform-strict feasibility for this fixed law both require gamma>g. At g=e, the tap essential lower bound ALONE cannot decide norm attainment or pointwise strictness. The actual symbolic families below show both possibilities.

## 2. Proof of the g>e actual norm-attainment caller

Take real unit maximizing inputs v_n with ||T_F v_n||->g. Hilbert weak compactness gives a subsequence v_n weakly converging to v, ||v||<=1. Put y_n=v_n-v. Then y_n is weakly null, compactness gives K_compact y_n->0 strongly, and

`||y_n||^2 -> 1-||v||^2`,

`||T_F y_n|| <= e||y_n||+o(1)`.

The cross inner product between T_F v and T_F y_n tends to zero by weak continuity of the bounded operator. Therefore

`g^2 <= ||T_F v||^2+e^2(1-||v||^2)`

`<= g^2||v||^2+e^2(1-||v||^2)`.

Since g>e, this forces ||v||=1, and then ||T_F v||=g. It is an actual real deterministic E2 input on the original interval; no spectral relaxation or maximizer of an unrelated output is used. If e=0 and g>0 this includes every nonzero compact dynamic output operator. No conclusion is asserted at a zero threshold outside the source's gamma>0 convention.

## 3. A whole physical family with g=e but NO nonzero norm attainer

Let a>0 and c,d,ell be arbitrary nonzero real parameters. For EVERY finite h>=0 and T>h choose the ORIGINAL scalar plant/law

`A=-a`, `B=0`, `C=c`, `A0=B0=0`,

`D0=-a d/c`, `D1=d/ell`,

`K=L0=0`, `Lh=ell`, `H=0`.

At h=0 the same left tap is the combined current tap. The fixed original-information controller is just `u(t)=ell w(t-h)`; it does not solve a noise-cancellation equation, add state, or depend on the chosen input. The original forcing c w(t-h) is nonzero and drives a nontrivial state.

The actual state/output are zero before h. For s=t-h in [0,S], S=T-h, define y(s)=x(s+h)/c. The exact equations give

`y'=-a y+w`, `y(0)=0`,

`z(s+h)=d [w(s)-a y(s)]`.                                  (F)

All finite-horizon controls, states and outputs are actual progressive E2 and nonexplosive. Nothing in (F) replaces the physical regulated output; it is the displayed original D0x+D1u for this ENTIRE symbolic parameter family.

## 4. Strict contraction on every finite path, without a storage-method import

For ANY nonzero real v in L2([0,S]), zero-extend to the real time line and form its causal full response `q=v-a exp(-a .)1_(.>=0)*v`. Standard L2 Plancherel and the L1-convolution identity give the multiplier

`1-a/(a+i omega)=i omega/(a+i omega)`.

Its squared modulus is `omega^2/(a^2+omega^2)<1` at every real finite omega. The unitary L2 Fourier transform of a nonzero input is nonzero on a positive-measure set, so

`||q||_L2(real line) < ||v||_L2[0,S]`.

Restricting q to [0,S] cannot increase its norm. That restriction is exactly the ACTUAL finite-horizon output in (F), divided by d. Thus

**||z(v)||_[0,T] < |d| ||v||_[0,S] for EVERY nonzero v.**       (S)

Precise ordinary imports are Plancherel's unitary L2 identity and Fourier multiplication for convolution with the integrable causal exponential; the latter follows first by ordinary Fubini on dense integrable inputs and then by L2 continuity. The exact exponential integral a/(a+i omega) is elementary. No frequency, horizon or state was sampled, and no quadratic state/storage identity or source-page frequency-method guidance is imported.

For EVERY nonzero canonical progressive E2 input, apply (S) samplewise. The gap `|d|||w||-||z||` is nonnegative, positive on the positive-probability nonzero-path event and bounded by the integrable |d|||w||. Taking expectations preserves a STRICT inequality. Thus the literal pointwise criterion holds at **gamma=|d|** for every admitted disturbance.

## 5. The exact gain is still |d|, and both boundary behaviors are real

For this physical family the direct tap is the scalar isometric left shift d S_h (or dI at h=0), with essential norm |d|, and the actual state-response term is compact on the finite interval. A real orthonormal weak-null sequence in the original input space makes that compact term vanish; hence g>=|d|. The preceding upper inequality gives g<=|d|. Therefore

**G_prog=G_det=g=e=|d|**, with NO nonzero norm-attaining input.

So gamma=|d| passes all-input POINTWISE strictness but fails uniform G<gamma, on EVERY finite T>h in the family. Any gamma<|d| fails by actual deterministic near-maximizers; any gamma>|d| works uniformly. This supplies a genuine finite-horizon original-object strictness distinction, not only an infinite-horizon example.

For the opposite g=e boundary behavior, the already stated pure endpoint original family with identically zero state and one nonzero output tap has an actual isometry d S_h. It attains |d| at every nonzero deterministic input, so its pointwise endpoint fails. Thus equality with the essential tap bound cannot by itself decide the strictness convention; both outcomes occur in the admitted physical class.

## 6. Exact residuals and source/process limits

Theorem A is all-matrix for the stated GIVEN noise-free plants; the counterfamily is all a>0,c*d*ell!=0,h>=0,T>h. Zero-output cases are not divided by zero; c=0/ell=0 are excluded only from the displayed normalization family, not from the general operator theorem. No claim for general noisy plants, arbitrary nonlinear full-information policies, source-domain equivalence, optimized controller impossibility or a prescribed arbitrary noisy-plant N&S criterion follows.

The source prints a strict ratio, but its full input/common-margin convention is an explicit interpretation; no historical three-page assertion is used as an input. The mathematical pointwise/uniform difference and actual callers above do not depend on NR-GAIN or the pending first-moment lemma. No direct diffusion-annihilating controller is proposed: zero noise is physical data of this comparison class, and every law is already in the bound policy family.

Only standard deterministic ODE/finite-kernel compactness/Hilbert weak compactness and the precisely named L2 Fourier facts are used. No old stopped realization/storage/changed-output guide, selected diagnostic, new source, scientific program/CAS/enumeration, model CLI or nested agent occurred. All prior process/cadence/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP, source-render/copyright and parent physics-2 L1 quarantine controls persist. Written only; no parent/peer, formal/kernel, executable, human/configured-family or novelty acceptance.
