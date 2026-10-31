# P44 v26 — PART25: CP peeling and an EXACT ALL-complex-two-plane formulation of the unrestricted witness problem

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 06:21:50 PDT 2026**. AUTHOR-WRITTEN, LATER UNREVIEWED. Exact symbolic complex linear algebra only; no mathematical identity was machine checked. Original HOLD/eighteen/cutoff/deadline remain.

## S0. Truth, authority and whole-primary boundary

This is the literal consolidation of the COMPLETED private Schur/all-complex-two-plane iff derivation saved in checkpoint120, SHA256 **cfc5db612fc2d02e03e778e2c5e333343a7939b59c02ea9862c02a8185279cc4**, BEFORE worker receipt of v118-A. It is NOT a fresh post-review discovery, not a claim that no earlier private reasoning occurred, and not independent/preregistered evidence. The extra frame-covariance/rank observations below are direct consequences supplied explicitly, not a backdated expansion of checkpoint120.

The complete300LF v118-A review was ACTUALLY RETURNED before checkpoint123 and the separate whole-primary resumption ACK `primary-resumption-after-v118A-ack-v1.json`, SHA256 **5315c8e48b34da02fd7240e576b90547ec6781ac876c183dc75758a8194d3057**, observed **Mon Oct 26 06:16:37 PDT 2026**. That ACK was actually SENT to Main BEFORE the present source/reasoning. P44 source and reasoning stayed paused from review receipt THROUGH actual return and during checkpoint/ACK saving. No old ACK grants retroactive permission.

All24 preceding parts and both addenda remain through checkpoint119, SHA256 **8de89458a989444dae01425ce270e2f81ecd40238413ca14a7fd95a9366b1ac9**,4884LF/349978bytes. Part24 is later unreviewed, not an already accepted premise. Here its elementary product-zero and regular-zero reduction are precisely named WRITTEN imports, and the new algebraic equivalences are proved below. No restricted chart, PV/normalized-N4 mechanism or old finite table is revived as an original outcome.

**P44 remains UNMET.** Required is an actual globally COMPLEX-SR<=2-positive indecomposable W and eligible PPT rho with Tr(W rho)<0, or an unrestricted theorem that ALL4x4 PPT states have Schmidt number<=2. This part is a full-quantifier representation of that SAME problem, not a solved family or an actual pair.

## S1. Cones, blocks and why the normalization loses no hypothetical counterexample

Let K2 consist of Hermitian W on C4 tensor C4 with q_W(x)>=0 for EVERY complex vector of Schmidt rank<=2. Let DEC={P+Q^Gamma:P,Q>=0}, where Gamma is Bob partial transpose. Write vectors as four Bob rows `x=(x0,x1,x2,x3)`, xi∈C4, and W in Alice blocks Wij∈M4(C). Schmidt rank is the dimension of the complex span of the xi.

Part24 Z1a proves: a product zero of W∈K2 is an actual kernel vector, using nonnegativity of x+t y for every product y and every COMPLEX t. Part24 Z2 proves: if K2 is not contained in DEC, a hypothetical non-DEC member can be made strictly K2-positive, perturbed to have no product eigenvector, then reduced by its minimum on the compact unit-SR<=2 set to a K2 member outside DEC with a rank-TWO zero and NO product zero. Local invertible filters put its zero on Alice indices0,1.

Consequently, conditional on any counterexample, one may take a W∈K2 outside DEC which is STRICTLY positive on every nonzero product vector, and has a zero

    z=e0 tensor a+e1 tensor b,

with a,b linearly independent. This uses the exact regular-zero reduction, not a numerical genericity trial.

For such W, W00 is positive DEFINITE: `u^dagger W00 u=q_W(e0 tensor u)>0` for every nonzero u. A Bob congruence by W00^(-1/2) puts W00=I4. Local invertible congruence preserves K2, DEC and linear independence of the two zero rows. Thus the zero remains of the form above for independent a,b.

**Do not impose two incompatible normal forms:** W00=I and zero=Omega2 with orthonormal Bob rows are not simultaneously established by this argument. After normalization a,b need not be orthogonal, equal norm or coordinate vectors. Their entire complex two-plane must be retained.

The algebraic results S2–S4 require only W00=I and global K2 positivity, not strictness or an anchored zero. The zero is used separately in S5.

## S2. Exact rank-four CP peel and positivity of the M3-to-M4 remainder

Set

    V0=I4, Vi=Wi0 (i=1,2,3),
    Uij=Vi Vj^dagger (i,j=0,1,2,3),
    chiij=Wij-Vi Vj^dagger (i,j=1,2,3).

Hermiticity gives W0j=Vj^dagger. Therefore

    W=U+tilde(chi),

where tilde(chi) is the trivial lift of the3x3 block matrix chi, with zero Alice0 row and column. U is PSD: if T is the4x16 block row

    T=[I4,V1^dagger,V2^dagger,V3^dagger],

then U=T^dagger T and

    q_U(x)=||x0+sum_(i=1)^3 Vi^dagger xi||^2.            (CP)

Since T has the identity block, rank U=4 EXACTLY. Calling U CP means its Choi matrix is PSD; no assumed positivity property of chi is hidden in that label.

**Lemma S2 (positive remainder).** If W∈K2 and W00=I, chi is block-positive on ALL product vectors in C3 tensor C4, equivalently the Choi matrix of a positive M3-to-M4 map.

*Proof.* Let xi=alpha_i u for i=1,2,3, with arbitrary complex alpha_i and u. Set g=sum Vi^dagger xi and choose x0=-g. All four rows lie in span_C{u,g}, of dimension at most2. Thus x has Schmidt rank<=2. CP vanishes by construction, so

    q_chi(alpha tensor u)=q_W(-g,alpha1u,alpha2u,alpha3u)>=0.

This proves positivity for EVERY complex product, not just real/coordinate products. It does NOT prove chi is2-positive or decomposable. ∎

This is the direct finite Schur/Choi-peeling argument; no source assertion about an unresolved M3-to-M4 map is imported as a theorem.

## S3. EXACT global K2 iff over ALL complex two-planes

Let F be ANY complex4x2 isometry, F^dagger F=I2, and P=FF^dagger. For i=1,2,3 write xi=F yi with yi∈C2. Define the6x6 Hermitian block matrix

    B_F(chi,V)=[ F^dagger chiij F
               +F^dagger Vi(I4-P)Vj^dagger F ]_(i,j=1)^3.  (B)

**Theorem S3.** For Hermitian W00=I and the data above,

    W∈K2  iff  B_F(chi,V)>=0 for EVERY complex4x2 isometry F. (ALL-PLANE)

This is a GLOBAL iff, not the local necessary Hessian condition of Part24.

*Proof, necessity.* Fix F and arbitrary yi. Put g=sum Vi^dagger F yi. Restrict x0 to the SAME plane range F. Completing the square in (CP), its exact minimum occurs at x0=-Pg and has value `||(I-P)g||^2`. Since every row lies in range F, this is a valid Schmidt-rank<=2 vector. Its W quadratic form is

    sum_(i,j) yi^dagger F^dagger chiij F yj+||(I-P)g||^2
       =y^dagger B_F y.

Global K2 positivity makes this nonnegative for EVERY y, proving B_F>=0.

*Proof, sufficiency.* Every Schmidt-rank<=2 row tuple fits inside SOME complex two-plane (a one-dimensional row span can be extended). Choose F for that plane. Decompose g=Pg+(I-P)g. Because x0∈range F, orthogonality gives EXACTLY

    q_W(x)=||x0+Pg||^2+y^dagger B_F y.                 (COMPLETE)

If all B_F are PSD, both terms are nonnegative. This covers every complex rank<=2 vector, proving W∈K2. ∎

The positivity lemma S2 follows from this iff as well, but its direct product proof shows no circularity. Conversely positive chi ALONE is insufficient for (ALL-PLANE); the complete6x6 matrices still must be PSD.

## S4. Frame covariance and the low-rank compensator, with exact limits

If F is replaced by F R for ANY2x2 unitary R, P is unchanged and

    B_(FR)=(I3 tensor R^dagger)B_F(I3 tensor R).

Thus (ALL-PLANE) genuinely depends on the COMPLEX Grassmannian of two-planes, not an arbitrary frame choice. It must cover all phases, all noncoordinate planes and all boundary/intersection configurations; no finite phase list or real chart is asserted exhaustive.

Take a4x2 isometry G for the orthogonal complement of range F. Let A_F be the6x2 block column with block i equal F^dagger Vi G. Then the added term in (B) is EXACTLY

    C_F=A_F A_F^dagger>=0, rank C_F<=2.                (COMP)

Hence the compressed chi must be nonnegative on ker(A_F^dagger), a subspace of dimension at least4, whenever (ALL-PLANE) holds. Its negative index is at most2: if its negative spectral subspace had dimension>=3, it would intersect ker(A_F^dagger) nontrivially, contradicting nonnegativity there.

These are NECESSARY consequences, not a sufficient negative-index test. Rank<=2 compensation cannot be replaced by a trace bound, a scalar overlap cap or merely counting negative eigenvalues. Its actual range, magnitudes and dependence on the SAME Vi for EVERY F remain essential. Even PSD at every coordinate plane does not establish the displayed universal quantifier.

There is one useful exact special case, not an exhaustion claim: if every Vi is scalar times I4, the compensator vanishes for all F. Then (ALL-PLANE) says exactly that chi is2-block-positive on C3 tensor C4. This does not solve the general case or assert all Vi can be made scalar by a legitimate filter.

## S5. The anchored rank-two zero and its normal coupling

Suppose now W∈K2, W00=I and `q_W(e0 tensor a+e1 tensor b)=0` for independent a,b. By LemmaS2, chi11>=0. At this vector the exact decomposition gives

    0=||a+V1^dagger b||^2+b^dagger chi11 b.

Both terms are nonnegative, so

    V1^dagger b=-a,  chi11 b=0.                       (ZERO)

In particular rank chi11<=3, without discarding a zero-output/singular branch.

Let S_ab=span_C{a,b}, P_ab its orthogonal projector and F_ab any orthonormal frame. In (B), y=(F_ab^dagger b,0,0) has zero quadratic form: its chi11 term vanishes and `(I-P_ab)V1^dagger b=0`. Since B_Fab is PSD, the WHOLE vector is in its kernel. Every block row j therefore gives

    F_ab^dagger chij1 b=0, j=1,2,3,
    equivalently chij1 b is orthogonal to span_C{a,b}. (NORMAL)

The compensator contribution vanishes because `(I-P_ab)V1^dagger b=0`, not because the Vi preserve every plane.

For clarity, the full vector Wz has Alice0 component a+V1^dagger b=0; Alicej component is

    Vj a+(chij1+Vj V1^dagger)b=chij1 b.

Thus Wz has only the Alice2,3 components chi21b,chi31b, each in the TWO-dimensional Bob orthogonal complement of span(a,b); chi11b=0. This is precisely a four-complex-coordinate normal coupling, the normalized counterpart of Delta in Part24. It need not vanish. Imposing Wz=0 would silently discard the unresolved normal directions.

## S6. Indecomposability typing and the exact original gap

**Lemma S6.** If chi is decomposable as a3x4 Choi matrix, W is decomposable. Therefore an actual non-DEC W in this representation requires an INDECOMPOSABLE positive chi.

*Proof.* Trivial Alice lifting preserves PSD and commutes with Bob partial transpose. Thus if chi=P0+Q0^Gamma with P0,Q0>=0, its lift is decomposable, and adding PSD U preserves DEC. ∎

The converse is NOT supplied and cannot be assumed: adding a positive CP term can move an indecomposable lift into DEC. Thus even a positive indecomposable chi with all B_F>=0 is not by itself a P44 solution. The WHOLE W must be outside DEC, preferably by an actual eligible negative PPT pair.

The full-cone reduction plus (ALL-PLANE) now identifies an exact prospective route with no selected-family claim:

1. Choose actual complex data Vi and positive indecomposable chi, satisfying the ALL-complex-plane PSD matrices (and, if using the regular-zero normal form, ZERO/NORMAL with independent a,b).
2. Independently establish W=U+tilde(chi) outside DEC and supply an eligible PPT rho with Tr(W rho)<0; OR prove that every global data set from (ALL-PLANE) yields DEC.

Named remaining gaps are `SCHUR-ALLPLANES` (no actual nontrivial globally valid indecomposable data constructed), `SCHUR-DEC` (no universal DEC extraction), and `SCHUR-PAIR` (no actual negative PPT pair). The equivalence makes those GLOBAL missing tasks explicit; it does not close them by a local Hessian, frame sample or source label.

All prior Delta-rank/conditional-norm/CP-kernel-target/Laurent and chart/range/Bell/code/PV/DOC leads remain saved at their exact old status. None is called eliminated by this representation. All cp049/063/081/083/085/089/oldcp013/admission and parent histories survive; N4 UNKNOWN/incomplete/exit-unestablished, old21 NOT_RECONSTRUCTED, C19–C27 FOUR minors and normalized old N4 ZERO new-method credit. No clean cognition/runtime/cadence assurance or source-status/novelty promotion.

This is WRITTEN at the stated finite-dimensional facts and named Part24 reduction, NOT formal/kernel/executable/configured-family/human/novelty acceptance. No scientific program/interpreter/eval/calculator/CAS/enumeration/solver/replay/CLI/build/test/nestedagent/newGO, approximate/numeric parameter trials or withdrawn-output guidance. Exclusive own-root writing only; all frozen bytes unchanged. Original science cutoff **2026-10-27T11:05:38-07:00** and deadline **2026-10-27T12:35:38-07:00** remain. This is not an early final park or round closeout. **P44 remains UNMET.**

**END OF COMPLETE v26 PART25.**
