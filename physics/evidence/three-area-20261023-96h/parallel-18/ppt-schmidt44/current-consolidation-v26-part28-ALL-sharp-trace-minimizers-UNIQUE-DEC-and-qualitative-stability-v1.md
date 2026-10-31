# P44 v26 — PART28: ALL sharp-trace minimizers are the UNIQUE canonical DEC witness; exact qualitative stability

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 07:05:24 PDT 2026**. AUTHOR-WRITTEN, LATER UNREVIEWED. Exact symbolic complex linear algebra and ordinary compactness/integration only. No machine check, scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nestedagent/new GO.

## V0. Truth and authority, no retroactive expansion of Part27

The equality-classification derivation in V1–V6 was already COMPLETED privately AFTER checkpoint127 but BEFORE actual worker receipt of v121-A. Its full symbolic steps were saved BEFORE the opaque ACK in checkpoint128, SHA256 **2273b05afd95044911e2748b88f3ffd8bd7bbff75cb8fab0569c0b505cf8a1b0**. It is NOT a fresh post-review discovery or a claim that no private reasoning existed. It was not expanded during the review or while saving checkpoints.

The complete251LF v121-A review was ACTUALLY RETURNED, then whole checkpoint131 preceded the separate resumption ACK **356e8c00bdbb4c336c1e8d4d6dde8c2274582bef8675c8be37fff63f0a19074f**, actual **Mon Oct 26 07:03:58 PDT 2026**, which was actually SENT before the present primary/source reasoning. The literal consolidation below follows that prospective boundary; the qualitative compactness lead was also already held, and its full proof is now supplied prospectively.

Part27,173LF, SHA256 **407ac110f17ee77a88e40e2f891012659ab925dcb28325eede7454dc4055646a**, proves the full-cone SHARP trace bound and constructs DEC extremizers. It explicitly did NOT classify ALL equality cases. This NEW successor supplies that additional theorem without editing or backdating the old packet. Part27 and this part remain unreviewed WRITTEN candidates, not an adopted import-free proof.

All27parts/twoaddenda/TWOcomplete positive-PRIOR source intakes and every older lead remain through checkpoint127/128/131. Generic Schur/border/ALL-complex-plane methods remain explicitly PRIOR under KG2509.07086v1 and MOM2104.14058v5. No world novelty/current-status claim. **Original P44 remains UNMET:** a full trace-minimizing-face theorem is not an unrestricted K2⊆DEC theorem or an actual indecomposable W/PPT-negative pair.

## V1. Exact theorem and inherited WRITTEN facts

Use Part27's coefficient matrices `X=[[A,B],[C,N]]`, X0=[[I2,0],[0,0]], Omega=vec(I2) in the A-space. Let K2 be Hermitian W nonnegative on EVERY COMPLEX rank<=2 matrix. For prescribed Delta∈M2(C), define the ENTIRE affine cone slice

    F_Delta={W in K2:q_W(X0)=0, W X0=normal Delta}.

This is not a selected symmetry/family restriction. Part24 proves the normal first-variation form; here it is imposed explicitly. Part27 proves

    Tr W>=M(Delta):=4||Delta||_*+sqrt(6)||Delta||_F,

and constructs a W_Delta in K2∩DEC attaining it for EVERY Delta.

**Theorem V1 — WRITTEN at Part24/27's supplied facts and ordinary finite-dimensional analysis.** For EVERY Delta, the trace minimizer over the WHOLE F_Delta is UNIQUE and is EXACTLY Part27's canonical W_Delta. In particular EVERY sharp-trace minimizer is DEC. Any W_j∈F_Delta with Tr W_j→M(Delta) converges in operator norm to W_Delta. This is qualitative stability, with no rate, no eventual-DEC assertion and no theorem that every nonminimizer is DEC.

For nonzero Delta write F=||Delta||_F, alpha=F/sqrt(6), c=1/(2alpha). In bottom SVD coordinates Delta=D=diag(d1,d2)>=0, W_Delta is the exact Part27 quadratic form

    alpha(||A||_F²-|Tr A|²/2)
    +||B sqrt(D)||_F²+||sqrt(D)C||_F²
    +|Tr(DN)|²/(2alpha)+Re(conjugate(Tr A)Tr(DN)).       (CAN)

It is globally K2-positive and explicitly P+Q^Gamma by Part27's full Schur-chart/density proof and PSD decomposition, not merely by a local Hessian. Bottom LOCAL unitaries send D to arbitrary complex Delta while fixing X0 and trace. V2–V6 prove there are NO OTHER minimizers.

The standard facts used are PSD range/kernel/Schur complements, Takagi/SVD, rank-one projector spans, product-zero annihilation for GLOBAL K2, ordinary unitary-invariant product-sphere averages, compactness and continuity. Every equality-specific coupling elimination is supplied below; no external4x4 classification is an input.

## V2. Equality in the entire trace chain fixes the tangent Schur matrix and kills A/U coupling

Let W∈F_Delta attain M(Delta), with Delta≠0. Put h=Tr H_AA, U=(B,C), and S=H_UU-H_UA H_AA^+ H_AU. Part27 gives the ENTIRE chain

    Tr W=h+Tr H_UU+Tr W_NN
      >=h+4||Delta||_*+3F²/(2h)
      >=4||Delta||_*+sqrt(6)F.

Every discarded quantity is nonnegative, so equality forces

    h=sqrt(3/2)F=3alpha,
    Tr(H_UA H_AA^+ H_AU)=0,
    Tr S=4||Delta||_*,
    Tr W_NN=3F²/(2h)=c F².                           (EQ-TRACE)

The second identity gives H_AU=0: its PSD product has zero trace, so (H_AA^+)^(1/2)H_AU=0; range(H_AU)⊆range(H_AA), and the inverse square root is injective there. This retains singular H_AA branches rather than discarding them.

The FULL complex Hessian inequality is equivalent, by Part24, to the doubled Hermitian PSD matrix

    [[S,-conjugate(R)],[-R,conjugate(S)]]>=0,
    R=R_Delta=R^T.

In Takagi coordinates R=U D_R U^T, the transformed S'=U^T S conjugate(U) satisfies the same condition with R=D_R>=0 diagonal. Testing individual coordinates first gives S'jj>=D_R,jj; trace equality makes every one an equality. For each j, (e_j,e_j) has ZERO quadratic form in the doubled PSD matrix, hence is an ACTUAL kernel vector. Its first block gives S'e_j=D_R,jj e_j. Thus

    S'=D_R, S=sqrt(R^dagger R).                      (EQ-HESS)

This proves uniqueness of the minimum-trace Hessian matrix, not just uniqueness of its diagonal. The global-to-doubled equivalence is essential; no finite phase tests are used as a positivity converse.

For Delta=D diagonal, R's singular coordinates give EXACTLY the two weighted norm operators in CAN: H_UU=S, with B_{ik} and C_{ki} weights d_k and NO B/C cross block. General Delta follows by the legitimate bottom SVD unitaries.

## V3. Equality in normal trace gives the ENTIRE normal block, not merely its diagonal

Part27's global rank-two average proves for EVERY complex normal rank-one Y

    <Y,W_NN Y> >= c |<Delta,Y>|².

Consequently D_N=W_NN-c|Delta><Delta| is BLOCK-POSITIVE on C2 tensor C2. By EQ-TRACE, Tr D_N=0. Average its nonnegative continuous product expectation over independent unit vectors in the two factors. The mean is Tr D_N/4=0, hence the expectation vanishes on EVERY product vector. Product projectors span the Hermitian operators, so

    W_NN=c|Delta><Delta| EXACTLY.                    (EQ-N)

No invalid assertion that a block-positive product zero annihilates a vector is made here: the zero-trace/product-expectation argument is what proves D_N=0. Product-zero annihilation is applied only to the GLOBAL K2 W in V4.

## V4. Product zeros span Delta-perp and force all normal cross blocks to factor

For ANY normal product Y with <Delta,Y>=0, EQ-N gives q_W(Y)=0. Part24's GLOBAL K2 product-zero lemma then gives W Y=0: for every product Z, Y+tZ has rank<=2 for all complex t, so the linear coefficient vanishes, and product Z span the full space.

These normal products span the WHOLE Delta-perp in M2(C). Here is an explicit proof of all singular cases, not a generic full-rank assertion. Bottom local SVD reduces to Delta=D diagonal. If rank D=1, the hyperplane N11=0 is spanned by the three product matrices E12,E21,E22. If rank D=2, the two off-diagonal product matrices E12,E21 and the rank-one matrix

    Y=(d2,-d1)^T (1,1)

are independent, all orthogonal to D, and span its three-dimensional orthogonal hyperplane. Local unitary transport preserves product rank and orthogonality, proving the statement for EVERY nonzero complex Delta.

Therefore W kills ALL normal Delta-perp, and its cross blocks have the form

    W_A,N=v Delta^dagger,
    W_U,N=w Delta^dagger,
    W_N,A=Delta v^dagger,

for some A-vector v and U-vector w. Since W X0=Delta, v^dagger Omega=1. Thus these are the only possible leftover couplings; none has yet been set to zero by an unsupported PSD full-W assumption.

## V5. The averaged zeros fix v, and actual rank-two first variations fix ALL A/U/N couplings

Fix ANY normal rank-one Y with z=<Delta,Y>≠0, which exists because Delta≠0 and product matrices span. For unit u∈C2 put A_u=u u^dagger. Part27's exact moment identities and h=3alpha give

    E_u q_W(diag(s A_u,Y))
      =(alpha/2)|s|²+c|z|²+Re(conjugate(s)z).

At the SYMBOLIC scalar s=-z/alpha this mean is0. EVERY individual value is nonnegative because the block-diagonal matrix has rank<=2, and it is continuous in u. Hence

    q_W(diag(-(z/alpha)A_u,Y))=0 for EVERY unit u.     (ALL-ZEROS)

This is an exact all-variable equality argument, not a sampled sphere or chosen numeric trial.

Let X be one of these zeros. V2 gives H_UA=0. Its normal W image is

    (W X)_N=Delta[s v^dagger A_u+c z].

The entire path diag(s A_u,tY) has rank<=2 for every complex t. First variation at t=1 of its nonnegative quadratic form forces <Y,W X>=0. Since z≠0 and s=-z/alpha, this gives

    v^dagger A_u=alpha c=1/2 for EVERY unit u.

Rank-one Hermitian projectors span complex M2, so

    v=Omega/2,  (W X)_N=0.                           (EQ-CROSS-A)

Next vary the left and right factors of the top rank-one A_u, keeping Y fixed. Each perturbed top product plus Y still has rank<=2; complex first variation implies that (W X)_A is orthogonal to every w u^dagger and every u w^dagger. Thus it is a scalar multiple of I2-A_u. Its trace is exactly z, because H_AA Omega=0 and v=Omega/2. Therefore

    (W X)_A=z(I2-A_u).

But the same vector is `-(z/alpha)H_AA A_u+z Omega/2`. Dividing by nonzero z gives

    H_AA A_u=alpha(A_u-I2/2) for EVERY unit u.

Again the rank-one projectors span, so

    H_AA=alpha(I4-|Omega><Omega|/2).                 (EQ-A)

Finally `(W X)_U=z w` is independent of u. Replace the Bob factor of the TOP product by an arbitrary bottom-Bob perturbation. This is still a sum of two product vectors, so the first variation makes its B-block orthogonal to every u r^dagger. As u varies, these span the entire B-space, forcing w_B=0. The analogous arbitrary bottom-Alice perturbation gives C-block orthogonality to every r u^dagger and w_C=0. Hence

    w=0, W_U,N=0.                                  (EQ-CROSS-U)

No primary/normal coupling or complex phase has been silently discarded. Every elimination follows from global rank-two zeros and exact all-complex paths, not a local-Hessian sufficiency claim.

## V6. All blocks are now determined: UNIQUE canonical minimizer, therefore ALL minimizers DEC

V2 fixes H_UU and kills H_AU. V3 fixes W_NN. V4–V5 fix W_A,N=Omega Delta^dagger/2, kill W_U,N and identify H_AA. In bottom SVD coordinates these are EXACTLY CAN, with alpha=F/sqrt(6). Thus ANY trace-minimizing W is Part27's constructed W_Delta. This is uniqueness on the WHOLE F_Delta, not only within its displayed symmetric construction.

Part27 supplies the ACTUAL global K2 proof and explicit PSD P,Q with W_Delta=P+Q^Gamma. Therefore EVERY sharp-trace minimizer is DEC. No new classical4x4 theorem/source label or numerical certificate is used to infer decomposability.

For Delta=0 the minimum trace is0, attained by W=0. If any W∈K2 has TrW=0, its nonnegative continuous product expectation has mean0, so it vanishes on all products; product projectors span Hermitian operators and W=0. Thus uniqueness holds in this case too.

**Original-gap consequence:** ANY non-DEC W in this regular-zero slice must have STRICT trace excess

    Tr W>4||Delta||_*+sqrt(6)||Delta||_F.

This is only pointwise strictness. No uniform positive lower gap, no all-state K2⊆DEC theorem and no actual non-DEC example follows.

## V7. Exact qualitative stability, and why it does NOT give a DEC neighborhood

A trace-bounded subset of the block-positive cone, and hence of K2, is bounded in operator norm. Otherwise take W_j with bounded nonnegative trace but ||W_j||->infinity. The normalized Z_j=W_j/||W_j|| have a subsequence converging to a unit-norm block-positive Z with TrZ=0. The product-expectation argument in V6 forces Z=0, contradiction. Closed trace-bounded K2 slices are therefore compact in finite dimensions.

Now W_j∈F_Delta and TrW_j→M(Delta). Their traces are bounded; every convergent subsequence has a limit in F_Delta with minimum trace. Uniqueness gives that limit W_Delta. If the whole sequence failed to converge in operator norm, a subsequence outside a fixed neighborhood would have a different compact cluster point. Contradiction. Thus

    ||W_j-W_Delta||->0,
    dist(W_j,DEC)->0.

This is an all-sequence qualitative limit, not a rate, uniform arithmetic bound or assertion W_j eventually belongs to DEC.

Indeed W_Delta is NOT an interior point of DEC: V4 supplies nonzero normal product Y orthogonal to Delta; CAN gives q_WDelta(Y)=0. The associated product-state PPT functional supports DEC there. If W_Delta were interior, W_Delta-epsilon I would still be DEC for small positive epsilon but would be negative on that product state, impossible. Therefore a bare closeness argument cannot establish a DEC neighborhood or close the original P44 gap. This explicitly prevents upgrading qualitative stability into an unproved local/global no-go.

## V8. Actual remaining task and process boundary

The full trace-minimizing face is now classified, and only globally admissible STRICT-excess witnesses could be non-DEC. The next original task is to decide whether such excess/coupling deviations can leave DEC while retaining ALL complex-SR2 positivity and a genuinely negative eligible PPT completion, or prove a universal DEC extraction. No such pair/theorem is supplied. The FULL Part25 plane criterion and Part26 actual CP-charge/PPT-entangled-compression obligations remain jointly unresolved; no closed candidate family or trace inequality is substituted for original P44.

All predecessor bytes,27parts/twoaddenda,TWOpositive-PRIOR source intakes, held Alice-gauge and cp120 Delta/conditional-norm/CPkernel-PPTtarget/fourWeyl/Laurent/chart/range/fullD/Bell/code/PV/DOC/source histories persist. The equality theorem's pre-v121 private chronology and later literal consolidation stay distinguished. All cp049/063/081/083/085/089/oldcp013/admission/ACK/cadence and parent histories remain; N4 UNKNOWN/incomplete/exit-unestablished, old21 NOT_RECONSTRUCTED, C19–C27 FOUR minors and normalized N4 ZERO new-method credit. No clean private-cognition/runtime/cadence/blind-family or worldwide novelty assurance.

Exact WRITTEN/source/metadata only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/build/test/nestedagent/newGO, no decimal/approximate/numeric parameter scouts or withdrawn-output guidance. No machine-checked identity, parent adoption, formal/kernel/human/configured-family/executable/triple/novelty/publication acceptance. Exclusive own root, all frozen files immutable. Same original eighteen, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**. Active primary increment, NOT early final park or round closeout. **P44 remains UNMET.**

**END OF COMPLETE v26 PART28.**
