# Written admission-soundness review: trace-corrected Bose N4

Observed before creation: **2026-10-23T15:49:27-0700 PDT**. Reviewer MathShor, primary slot math-5. Assigned by `peer-review-wave-eighteen-v6.json`, whose full common contract and MathShor entry were read. This is a mathematical preparation review, not scientific execution permission or validation of unrun code. Only this named new file is written.

## 1. Exact pins, exposure and verdict

The complete assigned sources were read, with independently observed matching SHA256:

| Source under physics `parallel-18/ppt-schmidt44/` | Observed SHA256 |
|---|---|
| proposal-normalized-Bose-N4-v1.md, complete193 lines | de428a73ccca38fdd9066c9a64f319f8da8c2d60c238ed56df2ae5886ad15f6d |
| normalized-N4-preparation-ADDENDUM-1-headroom-controls.md, complete89 lines | af72e56931a495e86639747d7f2b222a52c1c294d0430071c1ec3b9096d39951 |
| admission-request-normalized-bose-N4-v1.json, complete record | 198327a9eed06cee76574ad22e2a18f1cfce40a9d3a984af485229eb6f213ab4 |

Also read: complete current selection; complete bare-lift vacuity proof; actual fixed input JSON; the generic-filter target/region interface; primary Chen–Collins–Fawzi Lemma4/Eqs7–10 and Section2.2/Definition6/Proposition1 through the retained formula-preserving text; primary Krebs–Gachechiladze Theorem5, source weights/core and local extension interfaces, with its actual extension figure inspected. Relevant observed identities:

- fixed input: `19515358fd5b3b6a468af805694135a9bb428a2551f79995ee142d7cae2b2ff4`;
- CCF primary HTML: `c83cb1cc76311cc6bc41c41dfe0074a4d87732fcabbcdf466cead1a841c727f4`;
- KG primary HTML: `115f3102fc7f3c9be9992cbb130633da40d729b6f3c353338de0153770ea5070`;
- bare-lift source: `7fab6757107cfc6a9ae11ac4adf6162ad5e1f26089831ff45570f2e69c8910b1`.

Exposure: shared parent descriptions and the earlier bounded PPT auxiliary-merge review were known. This is a supplied-proof in-harness reconstruction, not blind/cross-vendor/human/formal review.

**Verdict: 0 FATAL / 0 MAJOR / 0 substantive MINOR at the actual mathematical scopes.** The universal complex rank≤2 implication, corrected normalization, N2 obstruction, scoped N3 control failure, exact N4 non-PSD control/margin, full320/260 reduction with Grams, mutation controls and hierarchy-family separation argument reconstruct correctly. The finite N4/ququart PPT-detection headroom remains **UNKNOWN**, not passed and not proved impossible. No prepared code/runtime was imported, executed, compiled, tested or certified.

## 2. Actual target and source/filter boundary

The target is a trace-one PSD16×16 matrix with PSD partial transpose across C4:C4 and Schmidt number≥3. Its separator must be nonnegative on EVERY complex Schmidt-rank≤2 vector. A4×5 state, NPT state, real-only rank test or an ordinary one-positive map would not suffice.

The source input R45 uses the literal unnormalized core vectors

    a=00+11+22, b=01+12, c=10-21,

plus the four weight3 product terms and the two weight3 extension vectors in the frozen selection. The retained primary core weights are(1,1,1,3,3); the source extension figure/text supplies the specified added coordinates. This retains the stated sign convention, not a mixture with a reparametrized core.

The actual real Bob filter is B_x=[I4|x], x=(1,1,1,1). It maps02+34 to02+|3>⊗x and04 to|0>⊗x, and leaves the other listed source vectors in the displayed4×4 coordinates. Positivity is also immediate from the positive weighted-projector formula. The target's raw trace is

    (3+2+2)+3·5+3·2+3+3+3+3·4=49.

Its partial transpose is a local congruence of the primary PPT source:

    R_x^Gamma=(I⊗conj(B_x)) R45^Gamma (I⊗B_x^T)≥0.

I retain R45's PPT property at the explicitly read primary Theorem5/construction interface; this review does not rerun a rational Schur checker or re-prove the original SN3 theorem. Local filtering need not preserve SN3, so the target's Schmidt number is still unknown. x1111 has L=3, outside the separately stated sufficient SN2 region L≤1/3; exclusion from that region is not positive evidence of SN3.

## 3. Universal complex soundness and the factor2

For any normalized complex Schmidt-rank≤2 vector, choose its actual Schmidt decomposition with nonnegative coefficients s_i and orthonormal local vectors. Put ell=s1+s2, so1≤ell²≤2. The augmented vectors A,B have squared norms ell, and contraction with the UNNORMALIZED Omega2 gives the physical psi. If J sends Omega2 to the unnormalized singlet S=01-10, then

    <S|(J⊗I)=<Omega2|.

Thus the asymmetric rescaling A'=sqrt(ell)JA, B'=B/sqrt(ell) preserves the physical contraction, makes B' unit and gives ||A'||²=ell². The N-fold augmented product lift is Bose-supported, positive, has trace ell²≤2, and its contraction on the first paired Bob is exactly P(psi); spectators have norm one.

Taking its expectation in

    C_N(Y,mu)=Q_N(Y)+mu[I-2Q_N(I)]≥0

gives

    <psi|Y|psi>+mu(ell²-2)≥0.

With mu≥0 this proves nonnegativity for ALL complex rank≤2 psi, not a grid or real-vector subset. A rank1 product has ell²=1, yielding expectation≥mu. Summing a computational product basis and using TrY=16 gives mu≤1. Therefore the proposed scalar interval0≤mu≤1 is mathematically justified.

The CCF primary source itself uses a normalized auxiliary Bell vector and explicitly distinguishes lift trace/norm from the original vector norm. The new derivation correctly changes to an unnormalized auxiliary vector and proves the trace correction rather than copying a source normalization or claiming the source's bare finite test is sign-complete.

For the real fixed target, conjugating Y and averaging preserves the real affine cone and objective. This justifies real-symmetric optimization for this input only; the mathematical certificate still proves universal complex rank2 positivity. No Park-style two-parameter physical covariance restriction is being imposed.

## 4. Corrected N2 and the precisely limited N3 failure

The bare flag construction was read completely. Its orthogonal summands place one Bob auxiliary in the distinguished label, all other paired Bobs in the same flagged product state. Full paired-Bob symmetrization preserves their sum. Switching the normalized Bell convention to the unnormalized singlet and normalizing this test vector gives

    expectation Q_N(Y)=<psi|Y|psi>/N,
    expectation Q_N(I)=1/N.

Hence the corrected expectation is <psi|Y|psi>/N+mu(1-2/N). At N2 the correction is exactly zero, forcing Y≥0. The withdrawn N2 route remains dead and no old GO transfers.

For the isotropic family Y=gamma I-P(Omega4), the N3 output spin1 calculation below yields the necessary condition

    8/(4gamma-5mu)+2/(gamma+mu)≤1

with positive denominators on the nonzero contraction sectors. These denominators really must be positive: positivity of D-L*L implies D≥L*L, and each relevant spin component of L* has nonzero norm. A zero denominator there would leave a D-null direction with nonzero L-image and violate positivity.

At gamma4,mu>0, the left side minus1 is exactly

    (2mu+5mu²)/[(16-5mu)(4+mu)]>0.

At mu0 it is4/gamma. For fixed admissible mu, lowering gamma increases the left side, so no gamma<4 passes. Physical isotropic twirling preserves the certificate, because the same physical unitary acts on every Bob copy and commutes with the paired permutation support. A twirled witness negative on Omega4 can be scaled to gamma I-P(Omega4); product positivity ensures its projector coefficient is positive. Thus N3 cannot detect this maximally entangled4 control.

This is NOT proof that the corrected N3 cone is entirely PSD-only, or that it cannot detect another NPT/PPT state. The author preserves that distinction.

## 5. Bosonic contraction, complete spin calculation and exact N4 margin

On the N−1 output-boson space, the displayed contraction L satisfies

    LL*=(2d+N-1)/N·I,

because tracing the Alice labels in the singlet contraction yields N^(-1)Σ_(alpha,p)b_(alpha,p)b_(alpha,p)*. On this fixed-particle space the numerator is2d+N−1.

The singlet projector is P(S)=I/2-2s_A·s_B. Averaging over N Bobs gives

    Q_N(I)=I/2-(2/N)s_A·S_B.

For output total auxiliary spin j, L* can enter Bob-input spins j+1/2 and j−1/2. Coupling to Alice spin1/2 gives exactly

    q_plus=(N+2j+3)/(2N),
    q_minus=(N-2j+1)/(2N).

Let a0=2d+N−1. The component norms r,s obey r+s=a0/N. To independently check their weighted equation, Schwinger commutators give, for each spin component S_i,

    Σ b S_i² b*=(a0+2)S_i²+(a0/4)I.

Indeed b S_i²=S_i²b+2S_i(t_i b)+t_i²b; summing uses Σbb*=a0, Σt_i b b*=S_i, Tr t_i=0 and t_i²=I/4. Summing the three components yields

    Σ b S_B² b*=(a0+2)S_B²+(3a0/4)I.

Substitution into the Casimir expression for Q_N(I) gives

    q_plus r+q_minus s=[a0(N+3)/2+2j(j+1)]/N².

This is an operator function of output spin, so it is scalar on the full spin sector including its physical multiplicities, not merely one convenient output vector.

At N3,d4,j1 this solves to r=8/3,s=2/3 and q=(4/3,1/3), reproducing section4's condition. At N4,d4, all output spins are3/2 and1/2, and solving the same two equations gives respectively

    q=(5/4,1/4), (r,s)=(35/16,9/16);
    q=(1,1/2),   (r,s)=(9/4,1/2).

For gamma31/8,mu1/2, D=mu I+(gamma-2mu)Q(I)≥I/2. Its two output Schur-complement eigenvalues are

    70/131+6/13=1696/1703,
    2/3+8/31=86/93.

The larger is1696/1703, leaving gap7/1703. Since the nonzero spectra of LD^(-1)L* and D^(-1/2)L*LD^(-1/2) agree,

    D-L*L≥(7/1703)D≥7/3406·I.

The scalar8/29 sends Y0,mu0 to the trace-normalized control and sends this margin to28/49387. Directly,

    Tr[(31I-8P(Omega4))/29]=16,
    <Omega4/2|Yctrl|Omega4/2>=-1/29.

Thus the finite N4 cone genuinely contains a non-PSD witness with an exact full-Bose positive margin. This is not a sampled eigenvalue or just a formal Schur complement on an unverified subspace.

Its PPT limitation is concrete: Yctrl^Gamma=(31I-8F)/29≥0, where F is the swap. Therefore this reduction-type control cannot itself detect any PPT state. Non-PSD headroom is not indecomposable/PPT headroom.

## 6. Exhaustive highest-weight multiplicities and the actual Grams

The Bose support dimension is8·binom(11,4)=2640. For four paired Bobs, the spaces with0,1,2 auxiliary-down bosons have dimensions35,80,100:

    dim Sym4(C4)=35,
    dim[Sym3(C4)⊗C4]=20·4=80,
    dim[Sym2(C4)⊗Sym2(C4)]=10·10=100.

Including Alice auxiliary spin and her physical factor4, the weight5/2,3/2,1/2 dimensions are140,460,720. Subtracting higher-spin copies gives multiplicities

    J5/2:140,       J3/2:460-140=320,
    J1/2:720-140-320=260.

The full dimension identity6·140+4·320+2·260=2640 closes the support. No other spin/multiplicity block is omitted.

For J3/2, raising maps each one-down D_(b;T) to the corresponding all-up U_(bT), so the proposed Alice-up D minus Alice-down U vectors lie in the raising kernel. Their distinct one-down occupation components establish all320 independent highest weights.

For J1/2, raising a two-down F_{s,t} gives D_s+D_t, including2D_s for repeated labels. The Alice-down correction cancels that difference, and its own Bob-raising contribution cancels because both pairs have total multiplicity2. The F_S-F_S0 components are independent. Summing the numbers of two-submultisets over physical multisets gives100; removing one reference in each of35 physical multisets leaves65, then multiplying by Alice physical dimension4 gives260.

On J5/2 the entire auxiliary state is symmetric, so the Alice/Bob singlet projector kills it; the corrected operator is muI. Auxiliary SU2 invariance makes the operator identity on each spin irrep tensored with its multiplicity operator. Positivity on a complete highest-weight multiplicity basis is therefore equivalent to full positivity.

The displayed bases are not orthogonal. For every rectangular basis B_J, the identity contribution MUST be B_J*B_J. The full margin requires B_J*C B_J≥delta B_J*B_J, not delta times an inserted identity. Individual column normalization does not change this Gram requirement. The proposal/request state this correctly. This review certifies the mathematical basis construction, not that the prepared code builds those matrices correctly.

## 7. Wrong-normalization mutants have the claimed actual sign split

For the embedded physical Omega2,

    Ymut=(15/14)I-(4/7)P(Omega2)

has trace16 and normalized rank2 expectation15/14-8/7=-1/14.

Restricting the contraction to the two selected physical modes gives

    LL*=(4+n_selected)/4≤7/4,

because the output contains three bosons. Thus Q(P(Omega2))≤(7/4)I. The wrong factor-one cone at mu1 gives

    Q(Ymut)+I-Q(I)
      =(1/14)Q(I)+I-(4/7)Q(P(Omega2))≥0.

It really would falsely certify this rank2-negative Ymut. The correct factor-two cone must reject it: the canonical equal-Schmidt rank2 lift has trace2 and contraction trace1, so its correction expectation is zero while its Y expectation is−1/14.

If the singlet projector is wrongly normalized by1/2 but the factor2 is retained with mu1/2, the resulting operator is exactly half the previous wrong factor-one positive operator. The same physical mutant remains negative. Both proposed controls therefore test the actual normalization defect, not an arbitrary exception or a fabricated search result. They have NOT been executed here.

## 8. Compact corrected hierarchy and its literal classical imports

For k=2, and analogously k≥2, the canonical normalized Schmidt construction gives SN≤k⊆K_N with trace-bound k. Convex mixtures preserve the bound. The finite-dimensional PSD trace ball is compact; Bose support and contraction-trace1 are closed constraints, so K_N is compact and convex. Tracing one complete paired Bob preserves Bose support, trace and the physical contraction, proving nesting.

For rho in every K_N, take a diagonal subsequence of fixed-M marginals. Uniform trace≤k yields a compatible limiting extension family. The limiting augmented Alice/first-Bob marginal has nonzero trace, since its contraction has trace1. Normalizing it permits the standard infinite-extendibility⇒separability theorem at exactly the finite-dimensional augmented Alice:Bob cut. This classical interface is stated in the read CCF Section2.2; its original de Finetti proof is not re-proved here. Contracting an augmented product vector gives a physical vector of Schmidt rank≤k; positive mixtures then give SN(rho)≤k. Hence the stated intersection equality holds. The old flag recovery with trace growing like N does not satisfy this compact trace bound and cannot invalidate the argument.

For a Hermitian W, the finite support-function SDP is

    min<Q(W),sigma> subject to sigma≥0,
        <Q(I),sigma>=1, Tr sigma≤k.

Its dual constraint Q(W)-lambda Q(I)+mu I≥0,mu≥0 and value lambda-kmu follow directly from the Lagrangian. Primal Slater holds for the actual k2 setting: a canonical physical-product lift has trace1 and contraction trace1. The Bose identity normalized to contraction trace1 has trace k, because Tr_Aaux Q(I)=I_Bose (with the Alice physical dimension factor retained). A small positive mixture is positive definite on Bose support, retains contraction trace1 and has trace strictly between1 and k. Thus the standard finite-dimensional SDP Slater strong-duality/attainment interface applies; this is an explicit classical import with its hypotheses checked, not an executed dual solve.

Setting Y=W-(lambda-kmu)I gives exactly Q(Y)+mu[I-kQ(I)]≥0. Strict separation from compact K_N then yields a corrected-cone witness negative on rho. The primary4×5 PPT SN3 state supplies an example that must be separated at SOME finite level of the rectangular corrected hierarchy. It does not specify N4, ququart dimensions or the proposed filtered input.

## 9. Headroom, code and execution decision boundaries

**Mathematical admission merit:** this is a materially different normalized cone. It has universal rank2 soundness, an exact non-PSD N4 control, and an asymptotically complete corrected family at the stated classical interfaces. The all-level bare-lift dead end does not refute it.

**Finite N4/ququart PPT headroom:** UNKNOWN. Neither the reduction control nor family-level compactness proves an indecomposable witness in this particular cone or detects rho_x. This is a genuine uncertainty a bounded screen could investigate, NOT a positive control that has already passed and NOT a proved dead end. The request explicitly keeps that admission gate open.

**Execution:** NOT AUTHORIZED. The request remains HOLD/noGO. This mathematical review supplies no fresh aggregate-resource observation, no source/interpreter/runtime guarantee, no solver status, no prepared-code correctness certificate and no approval to import/compile/execute either module. I did not inspect every line of those modules; no code-readiness verdict is implied. The independent definition checker is by the same author and is correctly not represented as a separate-agent verification.

A future negative numerical objective would be candidate evidence only; exact target/PPT binding, exact rational/algebraic certificate reconstruction, universal soundness and parent acceptance are still required. Nonnegative or failed finite optimization is UNKNOWN/no-negative-found in that frozen cone, not SN2, UNSAT or unrestricted P44 impossibility. The proposed single target, fixed controls and absence of adaptive escalation are preserved; no4×5 benchmark is silently added.

## Return

No mathematical repair requested at these exact scopes. Parent may consider this soundness/reduction reconstruction when deciding admission merit, but the explicit finite-PPT headroom and execution gates remain distinct. Classical-source proof trust, same-harness review, novelty and formal/human acceptance remain separate. I return to the Shor mixed-length RAW-SELECTOR obligation; no verdict transfers to it.
