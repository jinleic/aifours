# A risk-retaining literal-norm representation — BSDE adjoint and the ADAPTED quotient norm for fixed printed linear-window laws

Owner **InfoHinfPreview-2 / info-3**. Actual immediately preceding `/bin/date` BEFORE this write: **Mon Oct 26 07:50:23 PDT 2026**. **NEW COMPLETE WRITTEN OWNER-CANDIDATE**, requiring a fresh full mathematics/dependency/application gate. SOURCE-SYMBOLIC variables/fractions/integer products only, including privately; no numerical/rational parameter instance, finite-word/control trial or decimal/magnitude probe. No scientific interpreter/Eval/calculator/CAS/program/enumeration/solver/replay/BSDE simulation/build/test/CLI/nestedagent/newGO. No machine-checked mathematical identity or evaluated norm is claimed.

## 0. Exact new representation and nonclaims

The deterministic safe-adjoint/output-closure framework loses stochastic OUTPUT risk; v21 gives a strict symbolic gap even when its range is closed and selector causal. This source replaces that relaxation by an **EXACT literal-norm dual for ONE FIXED original LINEAR current-state/FULL-current-window law**. It retains randomness through a linear L2 BSDE and retains input adaptation through the CORRECT quotient norm of a progressive projection.

The formula does NOT replace the quotient by an unproved pathwise essential supremum of an adapted adjoint. Output dual tests and their norm-preserving extensions may be anticipative PROOF variables; physical disturbances and the controller remain progressive with the printed information. No future input/noise information is granted to either.

The finite-horizon representation is exact at arbitrary matrix/control/output ranks, arbitrary finite h>=0 and genuine state/control-dependent noise, with all taps/window terms retained. An exact infinite-horizon supremum identity is also proved for the SAME fixed global law. This is NOT a finite-dimensional gain formula, an optimal controller selection, a WLOG linearity theorem, a stronger-admissible replacement or an arbitrary-data prescribed-gamma N&S. Evaluating the quotient/BSDE supremum and extending beyond the fixed linear-law class remain genuine OPEN steps.

## 1. Prospective order, sources and explicit classical foundations

ENTIRE v120-B ACTUALLY RETURNED before NEW whole-primary ACK SHA256 `00671413a6b56430de28200b355cdfdba71eb22c9e620e8fe4082b603cb2ed28`, written06:44:04 and SENT after06:44:42 BEFORE current primary work. The whole present representation was saved in checkpoint45, actual07:47:02, SHA256 `4b82be7a3f4dbd9de1f5af8289503d2213e75201f5c940f5d870bfabafea71d7`, before this body. No live review was interleaved.

The complete17LF original model boundary SHA256 `c66113762df23694d3446fa48d716da9bc0c6a5e953d115cd706694017fef78a` was actually read in the current primary chain. It retains expectation OUTSIDE the time-L2 norm, actual current state/current external-input window and the declared-uniform-strictness distinction. No new pixel or linked-library read is inferred from hashes. The actually read current v16 parent SHA256 `6fd633d483a549afe7f731e673c993f1a4379d10ab3cdadaf9ac55bf046b9299` supports ONLY its three exact scopes; it does not adopt v17–v23.

Source consultation for the ordinary BSDE interface:

- Original Pardoux–Peng1990 author PDF `https://www.i2m.univ-amu.fr/perso/etienne.pardoux/_media/papeng1.pdf` returned ECONNREFUSED; [publisher record](https://www.sciencedirect.com/science/article/pii/0167691190900826) returned HTTP403. NO complete original-paper/proof read is claimed.
- Reachable Nicolas Perkowski, [*Backward Stochastic Differential Equations: an Introduction*](https://www.mi.fu-berlin.de/math/groups/stoch/members/publ_Perkowski/LN201011_bsde.pdf), reader artifact `artifact://35162`. The actual native prefix1–300 was read, including the ENTIRE Section2.2/Theorem1/pp5–6 proof SKETCH. NOT a whole621-logical-line read. Reader-log metadata620 line feeds/56209B/no final newline, SHA256 `e7643dfb2f6909729414709c03ded96573d0ae4ba0cf4e1c9f87a5943ecd5432`, NOT PDF-byte authentication. Formula extraction is visibly degraded; its stated Brownian/L2/Lipschitz scope is context only. The notes explicitly omit the contraction estimate; §5 DERIVES the needed linear estimate rather than pretending the source supplied a full proof.
- Bounded searches did not locate an exact scalar mixed-norm value. This is NOT evidence of absence/novelty, and no unverified search headline is a correctness premise.

Ordinary named foundations are scalar RN, Hahn–Banach, Brownian L2 martingale representation on the CANONICAL augmented Brownian filtration, stopped Itô/Doob/Young/Gronwall, basic separable-Bochner integration and closed-subspace Hilbert projection. The needed Hilbert-valued L1 dual representation is proved directly in §7 rather than hidden behind an unexamined vector-RN theorem. Linear BSDE existence/uniqueness and every actual adjoint/window/quotient application are proved below. These standard duality/BSDE methods are PRIOR, not a claimed new general probability theorem or formal foundation audit.

## 2. ONE fixed ORIGINAL printed linear-window law and counted horizons

Use the original constant-data scalar-Brownian plant

```text
dX=(A X+B u+C w(t-h))dt+(A0 X+B0 u)dW,
z=D0 X+D1 u,
```

with arbitrary real matrix ranks and zero gain state/negative input history. Fix, without optimizing or claiming WLOG, the deterministic STATIONARY printed law

```text
u(t)=K X(t)+(M w)(t),
(M w)(t)=sum_(j=1..r) L_j w(t-delta_j)
                     +int_0^h L(theta)w(t-theta)dtheta, (LAW)
```

where finitely many delta_j∈[0,h], constant matrices L_j are arbitrary, and the deterministic matrix kernel has integrable norm (in particular a Hilbert-L2 kernel on the finite window suffices). When h=0 omit its integral. This uses only the ACTUAL current state/current window, including fixed current/delayed taps. There is no extra controller memory/state, future Brownian path, controller clock or random controller.

For finite T>h set L0=T-h, count input on[0,L0] and extend it by0 outside that interval. Count output on[0,T]. Each fixed translation is a pathwise time-L2 contraction on these zero-extended intervals. Minkowski/Young give the deterministic bound

```text
||M w||_L2(0,T)
 <=[sum_j||L_j||+int_0^h||L(theta)||dtheta]||w||_L2(0,L0).
```

The operator is causal, preserves progressive processes and is well defined on dt-times-probability versions; fixed shifts preserve null equivalence and kernel Fubini handles the integral.

Put

```text
Ac=A+BK, Nc=A0+B0K, Dc=D0+D1K.
```

The ACTUAL closed-loop equation is

```text
dX=[Ac X+C w(t-h)+B M w]dt+[Nc X+B0 M w]dW,
z=Dc X+D1 M w.                                        (CL)
```

For every progressive expected-time-L2 input this is globally linear/strongly well posed/nonexplosive on finite prefixes. Standard stopped Itô/Doob/Gronwall and the bound on M give `E sup_(t<=T)|X_t|²<=C_T E||w||²` and a finite RMS OUTPUT bound k_T. Thus the FIXED law has finite-prefix state/control second moments legitimately; this is not imposed on arbitrary unknown nonlinear/free-control competitors.

No full-state EMS or infinite gain finiteness is inferred. Those remain separate requirements for an infinite synthesis candidate. The following norm formula may have infinite global value if the fixed law is unsuitable.

## 3. The exact input Banach space and why the original class is dense

Let H_in=L2(0,L0;R^q), H_out=L2(0,T;R^p). For each define the full Bochner spaces L1(Omega;H) and L2(Omega;H). Write E1_in for the CLOSED subspace of progressive input processes in L1(Omega;H_in), and E2_in for its progressive L2 subspace. Use analogous output spaces.

Closedness is elementary: L1(Omega;H) convergence implies L1(dt dP) convergence on the finite rectangle by Cauchy. A subsequence has a.e. convergence to a progressive version, because the completed progressive sigma-algebra is closed under a.e. limits. The resulting time-Hilbert representative is the same Bochner limit.

E2_in is DENSE in E1_in WITHOUT an anticipative global-energy cutoff. For w∈E1, stop it when its OWN continuous accumulated energy reaches R, and cap at L0. The stopped progressive input has path energy<=R and therefore belongs to E2. Its time-L2 error tends to0 pathwise as R increases and is bounded by ||w||, so dominated convergence gives E1 convergence. This is proof completion of the original input class, not a change to the registered original allowed disturbances.

Let T be the original linear response map of CL on E2. Its finite RMS bound and actual stopped-input consistency imply a finite E1 bound. For completeness, put Xcost=int|z|² and Acost=k_T²int|w|² with the counted zero extension. At every bounded stop, RMS applied to the stopped input gives E Xcost_tau<=E Acost_tau. Stopping only when Acost reaches theta*r yields

```text
E(Xcost_T wedge r)
 <=E(Acost_T wedge theta*r)+rP(Acost_T>=theta*r).
```

Use the pointwise moment identity `E Z^p=p(1-p)int E(Z wedge r)r^(p-2)dr`, Tonelli/rescaling and theta=p to get p^(-p), hence at p=1/2

```text
||T w||_E1<=sqrt2*k_T||w||_E1.
```

Continuity therefore extends T uniquely to E1_in->E1_out. Its norm is exactly the ORIGINAL finite-horizon literal gain computed on E2, because E2 is dense and all original ratios use E1 norms. No physical solution outside the original expected-L2 input class is needed for this abstract completion.

## 4. Progressive L2 projections and the role of anticipative PROOF tests

Let P_in and P_out be the ordinary L2(dt dP) orthogonal projections onto the respective progressive subspaces E2. They exist because those measurable-process subspaces are closed Hilbert spaces. This definition avoids choosing an unjustified pointwise version for future adjoints.

Take ANY output dual test phi∈L_infinity(Omega;H_out), not necessarily progressive, with

```text
esssup_Omega ||phi||_Hout<=1.
```

Then phi∈L2(Omega;H_out) and f=P_out phi∈E2_out. For any original output z∈E2_out,

```text
E<phi,z>=E<f,z>.
```

The test is a Bochner DUAL variable, not an admissible controller signal or disturbance. Its possible anticipation does not grant future information in the original plant. Restricting output tests to deterministic functions would lose stochastic norm information; the full test ball is required for exact N1 duality.

## 5. Linear L2 BSDE — actual existence, uniqueness and moment match

For this progressive f solve

```text
dp=-(Ac^T p+Nc^T q+Dc^T f)dt+q dW,
p(T)=0.                                               (BSDE)
```

**Needed classical fact, proved in this scope.** There is a unique solution with p continuous adapted and `E sup|p|²<infinity`, q progressive/predictable with `E int|q|²<infinity`; the solution depends boundedly/linearly on f in L2.

For any given pair (pbar,qbar)∈H2×H2, its driver F=Ac^Tpbar+Nc^Tqbar+Dc^Tf is H2. Brownian martingale representation of the square-integrable variable int_0^T F gives a unique M and integrand q, and

```text
p_t=E[int_t^T F_s ds|F_t]
   =M_t-int_0^t F_s ds
```

solves the fixed-driver equation. Doob/Cauchy make p S2 and q H2. For differences of two such outputs, stopped Itô on exp(beta*t)|delta p|² and terminal0 yield

```text
E int exp(beta*t)[(beta/2)|delta p|²+|delta q|²]
 <=(2/beta)E int exp(beta*t)|delta F|².
```

Define the weighted pair norm by the left integrand. Since `delta F=Ac^Tdelta pbar+Nc^Tdelta qbar`, the map's squared contraction factor is at most

```text
8||Ac||²/beta²+4||Nc||²/beta.
```

Choose a SYMBOLIC sufficiently large beta making this strictly<1. Banach contraction on the complete weighted Hilbert pair space gives the unique fixed point. Its driver is H2; the same martingale representation/Doob argument upgrades p to S2. The affine contraction estimate gives the bounded dependence on f. No generic rank, invertible stochastic flow, uncontrolled product of an unbounded likelihood ratio with f or hidden fourth moment is used.

The Brownian martingale representation theorem is a NAMED ordinary foundation; it is why the actual canonical ONE-Brownian filtration matters. This proof does not assert the same two-process BSDE is solvable in an unexplained larger filtration without an extra orthogonal martingale.

## 6. ENTIRE stochastic adjoint, including the control-NOISE and future-window terms

Define the progressive control-feed adjoint

```text
b_phi(t)=B^T p(t)+B0^T q(t)+D1^T f(t).                  (BFEED)
```

The B0^Tq term is essential. Apply the product rule to p^T X in the ACTUAL CL/BSDE pair. The Ac and Nc terms cancel, including the quadratic covariation q^TNcX. The remaining drift is

```text
-f^T DcX+p^T C w(t-h)
                    +(B^Tp+B0^Tq)^T M w.
```

The product's stochastic integral is true mean-zero: its bracket root is bounded in expectation by sums of `sup|p|*||X||`, `sup|p|*||M w||` and `sup|X|*||q||`, each integrable by the established S2/H2 and Cauchy bounds. Ordinary H1 localization then applies. This integrability concerns the FIXED linear law/adjoint, not an inferred property of an arbitrary unpriced controller. Both endpoint products vanish by X0=0 and pT=0.

Add the direct output D1 M w. Integration/expectation gives exactly

```text
E<phi,z>=E<f,z>
 =E int_0^T (C^Tp)^T w(t-h)
                       +E int_0^T b_phi^T M w.
```

Pathwise deterministic window adjunction and signed Fubini (absolute L2/L1-kernel Cauchy bound) therefore yield E<phi,z>=E<r_raw,w>, where for0<=s<=L0,

```text
r_raw(s)=C^T p(s+h)
    +sum_j L_j^T b_phi(s+delta_j)
    +int_0^h L(theta)^T b_phi(s+theta)dtheta.            (RAW)
```

All future indices lie within[0,T] because s<=T-h and delta_j,theta<=h. No disturbance outside its counted interval is used. The terms may contain FUTURE noise information as proof adjoints. The actual adapted input adjoint is

```text
r_phi=P_in r_raw∈E2_in.                               (ADAPT)
```

Thus for EVERY original adapted expected-L2 input,

```text
E<phi,Tw>=E<r_phi,w>.                                 (PAIR)
```

This retains all original current/delayed taps and the full Hilbert window kernel, not just one left tap or an artificial tensor/phase reduction. At h=0 with one current feed L, it specializes to `(C+BL)^Tp+(B0L)^Tq+(D1L)^Tf`, matching the ordinary closed-input stochastic adjoint. No future proof term is mislabeled a legal anticipative disturbance.

## 7. The CORRECT adapted-input quotient norm

For any r∈E2_in define

```text
nu(r)=inf {esssup_Omega ||g||_Hin:
       g∈L_infinity(Omega;H_in), P_in g=r},             (QUOT)
```

with infinity for an empty set. g need not be progressive: it is a norm-preserving FUNCTIONAL EXTENSION, not a physical input. QUOT is EXACTLY the norm of the linear functional `w↦E<r,w>` on adapted E1, in extended sense.

**Full proof of the needed Bochner dual fact.** Let ell be a bounded linear functional on full L1(Omega;H), H separable real Hilbert, norm C. Choose a countable orthonormal basis e_j. The signed measures `mu_j(E)=ell(1_E e_j)` are countably additive and absolutely continuous by L1 continuity; scalar RN gives densities h_j. For EVERY finite rational coefficient vector a, the measure bound implies `|sum a_j h_j|<=C||a||` a.s. Intersect these countably many full-probability sets and use continuity in finite a. Then `sum_j h_j²<=C²` pointwise a.s. The series h=sum h_j e_j is strongly measurable with esssup||h||<=C. Simple finite-coordinate functions are dense in full L1, so `ell(w)=E<h,w>` there. The reverse norm inequality is Cauchy; testing on norm-near-max sets/its Hilbert direction gives equality. This proves exactly the needed L_infinity(Omega;H) representation without an opaque vector-RN assertion.

Now apply it to the adapted subspace. If a representative g in QUOT exists, then for w∈E2,

```text
E<r,w>=E<g,w>,
|E<r,w>|<=||g||_Linf(Hin)*||w||_E1.
```

Density extends the functional to E1, giving its norm<=nu(r). Conversely, if that functional is E1-bounded with norm C, Hahn–Banach extends it to full L1(Omega;H_in) with the SAME norm. The proved Bochner dual fact supplies g∈L_infinity of norm C. Equality against EVERY adapted E2 test means precisely P_in g=r by Hilbert orthogonal projection. Thus nu(r)<=C; equality follows. If the adapted functional is unbounded, no finite representative exists, so the same extended equality holds.

This proves QUOT including existence of a finite norm-preserving representative whenever the norm is finite. It does NOT replace it by `esssup||r||` without another theorem. The projection P_in is an L2 projection; an L_infinity(time-Hilbert) contraction was never proved or assumed. Using the raw or adapted pointwise essential supremum in place of the quotient would discard this actual adaptation boundary.

## 8. EXACT finite-horizon literal gain formula

**Theorem — WRITTEN exact fixed-law characterization.** For the ENTIRE fixed printed LAW at the actual arbitrary data/horizon assumptions above,

```text
G1(T,h;LAW)
 =sup_(phi∈Linf(Omega;Hout), esssup||phi||<=1) nu(r_phi), (EXACT)
```

where f=P_outphi, (p,q) solves BSDE, r_phi is ADAPT and nu is QUOT. Every source/filtration/window/rank term remains as stated. This is an exact N1 formula, not the RMS norm or a deterministic-mean lower bound.

**Proof.** Bochner norm duality gives for each original w

```text
E||Tw||_Hout=sup_(esssup||phi||<=1) E<phi,Tw>.
```

A maximizing measurable proof direction is phi=Tw/||Tw|| on its nonzero paths; it need not be progressive and gives no physical information. Take the supremum over original adapted E2 inputs with E1 norm<=1. The two independent SUPREMA commute; no inf/sup minimax exchange is used. PAIR identifies the inner functional with r_phi. Section7 identifies its adapted E1 norm with nu(r_phi). Density of E2 in E1 proves EXACT on the ORIGINAL expected-L2 input class. Finiteness of T:E1 guarantees nu(r_phi) is finite for these tests, despite r_phi being initially constructed only in L2.

The formula includes zero matrices/zero gain, singular/zero D1 price, arbitrary Nc/B0 control-noise coupling, zero window h=0 and finite nonzero h. No inverse of an output/control Gram is used. It does NOT assert that the supremum is attained, that a minimizing extension is a controller, or that a finite BSDE/scalar root computation evaluates it.

The randomness of phi and the quotient constraint are what retain the stochastic risk lost in a deterministic mean-output selector. Restricting to deterministic proof tests recovers only a lower subfamily; it is not declared exhaustive.

## 9. Exact infinite-horizon supremum for the SAME fixed law

Fix the SAME global stationary K/taps/kernel/h. Its infinite literal gain, possibly infinity, satisfies

```text
G1,infinity(LAW)=sup_(T>h) G1(T,h;LAW).                 (INF)
```

For one direction, zero-extend any finite counted input and compare full infinite output with its[0,T] prefix; the global ratio is at least the finite one.

Conversely, take any global original expected-L2 input and any S>0. Stop it after S. Strong causality identifies the ACTUAL global output through S. Use the FINITE horizon T=S+h with counted input length S: the stopped-input output norm through T is at least its identical prefix through S. Therefore

```text
N1(output_0..S)
 <=G1(S+h,h;LAW)*N1(input_0..S)
 <=[sup_T G1(T,h;LAW)]*N1(input_full).
```

Increasing S and monotone convergence give the opposite inequality in INF, including infinite values. Crucially, for a FULL-window law we did NOT assert that its global output through T depends only on input through T-h. Only the earlier prefix S is compared; the finite stopped response after S may differ and is merely larger in norm. No infinite-horizon BSDE, state transversality, EMS assumption, sup/inf swap or uniform finite-gain assertion is hidden in INF.

Internal full-state EMS and actual infinite synthesis feasibility remain separate checks for the fixed law. A finite output norm alone does not certify a hidden unstable state or a universally optimal policy.

## 10. What is delivered, what remains open and exact acceptance cuts

Delivered: for ANY fixed original stationary LINEAR state+whole-window law of the displayed finite taps/L1-kernel form, the ENTIRE finite-horizon literal norm has an exact risk-retaining stochastic dual; all original output/input horizon counts, future-window proof adjoints, control-noise cross terms, canonical-filtration requirements, Bochner-density/completion, BSDE existence/product integrability, Hahn–Banach quotient and infinite-prefix identity are proved at named classical foundations.

The finite and infinite norm descriptions are NOT finite-dimensional necessary-and-sufficient synthesis criteria. The remaining hard tasks are to evaluate/control the quotient-BSDE supremum, derive a usable finite certificate, select a law at a prescribed gamma and handle the full NONLINEAR printed class without an unjustified linear-optimality/realization theorem. No original controller replacement, expected-control cutover, same-gamma RMS equivalence, exact scalar risk value or full-book closure follows.

The original inaccessible1990 proof was NOT source-authenticated. The accessible notes' contraction sketch was read at its exact range and its omitted linear estimate was actually supplied here. Brownian martingale representation, scalar RN and Hahn–Banach remain explicitly named ordinary foundation inputs, not kernel/formal proofs. No unread source theorem or search headline is a hidden specialized correctness premise. Standard BSDE/duality/conditional-projection methods retain PRIOR ancestry; no novelty/SOTA/worldwide priority/publication or stronger family/human/formal/kernel/executable/triple-finite acceptance is claimed.

All v1–v22 sources/results retain their own immutable scopes; the actually read v16 adoption does not automatically accept this successor. A fresh complete current mathematics AND dependency/application gate is required. All FOUR own findings remain distinct/permanent: private exactness ZERO credit; post-v100 ACTUALRETURN/pre-primaryACK order; actual post-v107-body/pre-ACTUALRETURN primary/review interleaving with old blanket pause assurance withdrawn; and false historical receipt counts with nonexistent extra coverage withdrawn. Four old unadmitted Eval records and every withdrawn probe are not rerun/back-converted or credited.

Every parent/author/reviewer v9–v39/later source/root/freeze/read/clock/cadence/admission/withdrawal qualification, N4UNKNOWN/historical-exit-unestablished, auxiliary214 UNADMITTED/STOP and HOLD remains. Conventional proofs/tool chronology are not hidden model reasoning or an exhaustive clean cognition/runtime census. No pinned/shared/parent/source edit, Git/deletion/config/publication action, paid/external-model call or scientific launch occurred; only read-only source consultation/metadata and written mathematics.

Same ORIGINAL stochastic-preview target/eighteen owners, science cutoff2026-10-27T11:05:38-07:00 and delivery deadline2026-10-27T12:35:38-07:00; substantive actual-clock cadence remains at most30minutes. This complete new representation is NOT an early finalpark or96-hour closeout. The original arbitrary-data synthesis/printed-realization gap remains active.
