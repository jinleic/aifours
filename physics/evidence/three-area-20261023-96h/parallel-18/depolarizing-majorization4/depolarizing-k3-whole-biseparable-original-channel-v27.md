# Actual k3 continuation v27 — WHOLE ORIGINAL index3 for EVERY four-qubit BISEPARABLE density

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 07:14:45 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN CANDIDATE, NOT adopted, NOT the unrestricted solution.** Exact SYMBOLIC written representation/algebra including privately; no scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/CLI/nested agent/GO, numerical parameter/control trial or decimal scout. All current/older candidates and mandatory F3/ENTIREv22 withdrawals remain. Same18/HOLD/OWNroot/October27 cutoff11:05:38/deadline12:35:38 PDT and <=30minute substantive checkpoints. Active original continuation, not a park.

## 1. Target and exact NEW result

For EVERY four-qubit biseparable density rho (the convex hull of pure products across ANY nontrivial bipartition), EVERY physical0<=p<=4/3 and EVERY complex rank-three orthogonal projector Pi,

    Tr Pi D_p^(tensor4)(rho)
       <=K3(D_p^(tensor4)(|0000><0000|)).                  (BISEP)

The NEW direct component is EVERY1|3-product input and its actual convex hull, with arbitrary complex entanglement of the three-qubit factor. The2|2-product component uses the separately parent-adopted PAR theorem at its exact current interface: each pure two-qubit factor is physically LU-Schmidt-diagonal, so their product is a physical LU image of an even-parity state. Mixed2|2 products and mixtures follow by original affine traces. No arbitrary pair-cut complex SVD covariance is invoked.

We prove the1|3 component by a complete THREE-physical-qubit original-channel theorem at indices1,2,3, with genuine FULL two-/three-/four-copy certificates. The analogous FOUR-physical-qubit relaxed rank3 certificate is FALSE by independentv23; nothing here resurrects it. The three-site rank3 isotypic blocks are all explicitly treated below, including every local(22) sector. No nonexistent fourth physical site/block is included or omitted.

**Important scope:** this is a DIRECT ORIGINAL noise-polynomial theorem on BISEP. It does NOT automatically prove K3(X3_4)<=6 on every1|3 factor, nor classify all coefficient-U3 violators as genuinely multipartite entangled. The latter sufficient coefficient inequality remains a distinct route. Every possible ORIGINAL counterexample can now be taken genuinely FOUR-partite entangled if BISEP is reconstructed/adopted.

## 2. Three-site literal polynomial and actual Slater lift

On H3=(C^2)^tensor3 define unnormalized erasure coefficients as usual. For0<=p<1 let u=p/[2(1-p)]>=0 and

    H3_u(rho)=rho+uX2_3(rho)+u^2X1_3(rho)+u^3 I,
    D_p^(tensor3)(rho)=(1-p)^3 H3_u(rho).

For k=1,2,3 the product-reference prefix is

    L_k(u)=(1+u)^2(1+k u).

For an ACTUAL rank-k projector Pi on H3 use its normalized Slater vector C_Pi in wedge^kH3. Copies are0/reference and a=1..k/code. At each of the THREE physical sites i let F_a^(i) swap copies0,a. Set

    K_k(u)=sum_(a=1)^k tensor_(i=1)^3 (F_a^(i)+uI).

Each code marginal of C_Pi is Pi/k. The partial-swap contraction and sum over a give EXACTLY

    <psi tensor C_Pi|K_k(u)|psi tensor C_Pi>
        =Tr Pi H3_u(|psi><psi|).                         (LIFT)

There is no extraneous k. The code-S_k global sign subspace is H3 tensor wedge^kH3; all matrices below act on that actual physical space. Proving K_k<=L_kI there suffices for arbitrary complex rho/Pi by fixed-projector affine extension.

Named ordinary interfaces: finite-dimensional Schur-Weyl decomposition for THREE/FOUR copies of a qubit, the explicit S3/S4 irreducibles/branching described below, and elementary real symmetric2x2 PSD. Every model-specific matrix, multiplicity/completeness check and polynomial gap is supplied, not imported from the old failed four-site draft or a representation table program.

## 3. Index1: whole two-copy operator bound, all u>=0

For k=1, the three site swaps commute and each has eigenvalues+-1. Every full tensor eigenvalue of K1 is a product of three factors u+-1, so its absolute value is at most(1+u)^3 for u>=0. Hence K1<=L1I on the WHOLE two-copy space. No state/product covariance assumption or inherited finite certificate is used. This gives the exact first three-qubit output prefix at index1.

## 4. Index2: ALL actual three-copy sign sectors, including singular u=0

A qubit's three-copy space decomposes into local S3 trivial type(3) with multiplicity4 and standard type(21) with multiplicity2; the alternating type is absent. In a standard factor choose basis(code-S2 trivial,code-S2 minus), where code-S2 exchanges copies1,2. The two reference-code swaps plus uI are

    F1+uI=[[a,g],[g,c]], F2+uI=[[a,-g],[-g,c]],
    a=u-1/2, c=u+1/2, g=sqrt3/2.

A local trivial factor contributes1+u. With m active standard physical sites the global code-minus subspace has basis the odd number of local minus signs, dimension2^(m-1); m=0 has none. The sum of the two tensor terms retains only even Hamming changes. These are ACTUAL local tensor matrices, not merely a character count.

- **m=1:** K2=2c(1+u)^2=L2. The gap is0.
- **m=2:** in the two odd basis vectors K2 has diagonal2ac and off-diagonal2g^2, times(1+u). Its eigenvalues are(1+u)(2u^2+1) and(1+u)(2u^2-2); the respective L2 gaps are3u(1+u) and3(1+u)^2.
- **m=3:** the three one-minus vectors decompose into a site-permutation standard2-space and their symmetric vector; the all-minus vector supplies a second symmetric component. The standard2-space has gap6u(1+u). On the two symmetric vectors, the EXACT gap is

      [[(3/4)(8u^2+2u+3), -(3sqrt3/2)(u+1/2)],
       [-(3sqrt3/2)(u+1/2),(1/4)(8u^2+10u+3)]].

  Its diagonal entries are positive and determinant is6u^2(1+u)(1+2u)>=0. This follows by multiplying the two displayed polynomials and subtracting(27/4)(u+1/2)^2; no gap division occurs. The full m=3 sector is covered.

Completeness: sign-space dimensions including physical multiplicities are96 for m1,96 for m2,32 for m3, totaling224=8*binom(8,2). Local isotypic projectors commute with every summand, so cross-isotypic terms are absent; the displayed internal blocks exhaust each sign sector. Hence K2<=L2I for ALL u>=0, including every zero/singular endpoint. This is the needed three-site index2 theorem, not the already adopted four-site theorem or its optional quartic M1 sentence.

## 5. Index3: explicit FOUR-copy local matrices on the SAME code-standard plane

A qubit's four-copy space has local S4 types(4),(31),(22), with physical multiplicities5,3,1 and representation dimensions1,3,2. No other type occurs. Under code S3 on labels1,2,3, these restrict respectively to trivial, trivial+standard, standard. Fix

    E={x in R^3:sum x=0}, q_a=e_a-(1,1,1)/3,
    q_a.q_b=delta_ab-1/3.

In(31) use t=(3,-1,-1,-1)/sqrt12 and E on code coordinates. In(22) use the zero-sum plane of the three pair-partitions. Direct swap(0a) matrices are

    F_a^(31)=[[-1/3,(2/sqrt3)q_a^T],
              [(2/sqrt3)q_a,I_E-q_aq_a^T]],
    F_a^(22)=3q_aq_a^T-I_E.

The code action on E is the SAME in both. Put h=q1/||q1|| and choose perpendicular k. For a=1,

    F_1^(31)+uI=[[a,g,0],[g,b,0],[0,0,c]],
    F_1^(22)+uI=diag(c,d),
    a=u-1/3,b=u+1/3,c=u+1,d=u-1,g=2sqrt2/3.

On the global code-S3 SIGN sector, all THREE summands of K3 have the SAME matrix entries: code conjugation maps one reference-code swap to another, and its two signs cancel between bra/ket. Thus the K3 sign matrix is THREE times the compression of the a=1 tensor matrix. This does not replace arbitrary eigenvectors by physical Schmidt vectors.

The normalized code-sign tensors needed are

    epsilon_ij=(h_i k_j-k_i h_j)/sqrt2,
    T_123=(hhk+hkh+khh-kkk)/2.

Epsilon is the two-form (code determinant), and T is the imaginary harmonic cubic: invariant under code120-degree rotation and odd under a code reflection. These directly verify their sign transformation. Local trivial factors are denoted t; a local(4) factor contributes c.

## 6. Index3: EVERY active-two and active-three sign block

For THREE physical sites there can be m=2 or3 active nontrivial local S4 factors. m0/1 have no code-sign component. With m2 the sign vector is the unique epsilon in the two standard planes; the inactive(4) factor contributes c. The EXACT L3 gaps are

|active local types|sign dimension|L3-K3 gap|
|---|---:|---|
|(31),(31)|1|0|
|(31),(22)|1|2uc|
|(22),(22)|1|4c^2|

Indeed their a=1 standard contractions are bc,(bd+c^2)/2,cd respectively; multiply by3c and subtract L3=c^2(1+3u). These entries retain d=u-1, which may be NEGATIVE; it was not replaced by an absolute value or discarded tail.

For m3, list ALL four local-type patterns, up to actual physical-site permutation:

### 6.1 Three(31): dimension4, gaps4uc (twice),4c^2,uc

The j=2-standard tensors `t_l epsilon_ij` form the oriented edge space on THREE sites. Under physical-site S3 it is standard2 plus sign1; j=3 contributes the symmetric cubic T, a trivial1-space. They are inequivalent, so no mixing is possible. Direct pair contractions give K3 eigenvalues

    3c(ab+g^2/2) on standard2,
    3c(ab-g^2)   on sign1,
    3c(3b^2+c^2)/4 on trivial1.

Subtracting L3=c(3u^2+4u+1) gives respectively4uc,4c^2,uc, all nonnegative u>=0. The t/standard off-diagonal g is retained in the first two contractions; it is not a diagonal-only compression.

### 6.2 Two(31),one(22): dimension3, one scalar and ONE2x2

Put the(22) factor at site3 and set v1=t1 epsilon23,v2=t2 epsilon13. Their antisymmetric combination v_- has gap6uc. The symmetric v_+=(v1+v2)/sqrt2 couples to T123. The EXACT L3 gap on(v_+,T) is

    (1/3)[[18u^2+10u+8,4sqrt2(2u+1)],
          [4sqrt2(2u+1),9u^2+11u+4]].                  (MIXED)

For clarity the underlying a=1 contractions are diagonal `a(bd+c^2)/2` and `[d(b^2+c^2)+2bc^2]/4`, off-diagonal between v1,v2 `g^2d/2`, and between v_+,T `g(bd-c^2)/2`. These produce EVERY displayed MIXED entry after the factor3. The unscaled diagonal product minus squared off-diagonal is

    (18u^2+10u+8)(9u^2+11u+4)-32(2u+1)^2
       =18u^2(1+u)(9u+7)>=0.

Both diagonals are positive, so MIXED is PSD INCLUDING u=0. No local(22) sector or negative d term is omitted.

### 6.3 One(31),two(22): dimension2, gaps8uc and5uc

Use t1 epsilon23 and T123. The off-diagonal contraction vanishes because the hk and kh terms on the TWO identical(22) factors have equal cd weight and opposite epsilon signs. Their K3 diagonal entries are3acd and `3c(2bd+c^2+d^2)/4` respectively. Subtract L3 to obtain8uc,5uc. This is an actual zero from the two terms, not an assumption that all standard representations can be independently diagonalized.

### 6.4 Three(22): dimension1, gap7u^2+5u+4

Only T123 remains. Its contraction is(3c^2d+d^3)/4, so K3=3(u^3-1). Subtracting L3=3u^3+7u^2+5u+1 gives the positive gap7u^2+5u+4. The potentially negative K3 eigenvalue at small u is harmless; it was NEVER treated as a positive operator summand.

### 6.5 Actual dimension/completeness, not a selected subspace theorem

Including all positions and physical multiplicities, active-two contributions are135 for two(31),90 for one(31)/one(22),15 for two(22), totaling240. Active-three contributions are108,81,18,1 in the four patterns just treated, totaling208. Their sum448 is EXACTLY `dim(H3 tensor wedge^3H3)=8*binom(8,3)`. Every local isotypic projector commutes with the swap-polynomial, and the code-sign projection commutes with its summed operator. All internal code-sign blocks are now accounted for; multiplicities act by identity. Therefore

    K3(u)<=L3(u)I on ALL H3 tensor wedge^3H3, u>=0.

This is a COMPLETE three-site operator certificate. It is NOT the false four-site matrix assertion of v22/v23 and does not require any unprovided remaining positive block or numerical enumeration.

## 7. Whole three-qubit ORIGINAL first-three-prefix theorem

LIFT plus §§3–6 prove the three-qubit product-reference comparison at EACH index1,2,3 for0<=p<1, all complex projectors/pure states. Fixing a projector and averaging its ORIGINAL affine trace extends it to every mixed three-qubit density. At p=1 the output isI8/8. For1<p<=4/3, full three-qubit spin flip is a unitary-TOTAL-transpose map, positive and spectrum preserving even though its antiunitary squares to-I; on weight-w Pauli terms it multiplies(-1)^w. With q=2-p this sends D_q output to D_p output and preserves the reference spectrum. Thus all physical p are covered.

The ordinary Slater/Schur-Weyl/spectral facts are named inputs, not formal libraries. No global TC inequality, current CLIP/k4/NP/PAR theorem, inherited finite certificate or old rank2 optional scalar corollary is a premise of THIS three-site result.

## 8. Exact tensor-prefix transfer to EVERY1|3 product and ALL BISEP

Let a four-qubit input be `|a><a| tensor sigma3`, sigma3 arbitrary mixed, with physical factor positions permuted if necessary. For0<=p<=1 let q0=1-p/2,q1=p/2 be the pure one-qubit output eigenvalues and beta the three-qubit output spectrum. The full four-qubit output is the ACTUAL direct sum q0*beta,q1*beta. Its top3 sum is EXACTLY

    max_(j=0,1,2,3) [q0 K_j(beta)+q1 K_(3-j)(beta)].

The just-proved SAME-input first-three bounds give K_j(beta)<=K_j(beta_product3) for EACH j. Nonnegative q0,q1 preserve every allocation inequality. Maximizing the REFERENCE allocations recovers exactly K3 of the four-qubit product output. No claim that independently chosen marginal spectra are simultaneously attainable is used; all j inequalities hold on the SAME actual beta. This proves ORIGINAL k3 for every1|3 pure factor, hence for mixed one-qubit factor by fixed-Pi linear averaging, and their actual convex hull. p>1 again uses the full FOUR-qubit spin flip, not partial transpose or an unsupported sign of(1-p)^4 expansion.

For2|2 pure products, physical local-qubit Schmidt decompositions put each pair in span00/11, hence their product in an even-parity subspace. The separately parent-adopted Theorem PAR and its original all-p application apply, with every complex phase/degenerate pair retained. Its exact qualified source/parent boundary is mandatory, not re-proved by this three-site argument. Arbitrary mixed2|2 products decompose into such pure products; arbitrary BISEP states are their convex mixtures together with1|3 products across all physical bipartitions. At a FIXED original Pi,p, affine averaging proves BISEP exactly.

## 9. Original residual and permanent trust boundaries

New: a COMPLETE original all-p index3 theorem for the WHOLE BISEPARABLE four-qubit class, with an explicit new complete three-site first-three-prefix operator proof at ALL u>=0 and an actual tensor-allocation application. No trial state/noise, decimal gloss, interpreter/solver/checker or unadmitted old arithmetic was used. The k3 problem remains OPEN for genuinely four-partite entangled inputs outside precise separately supported regions. The coefficient-U3 conjecture, full-B CLIP-prime and actual common-projector quartic remain distinct held routes; no physical counterexample or complete unrestricted all-index majorization is supplied.

Current named PAR adoption is the sole substantive research import for the2|2 part of BISEP; the1|3 proof is direct at ordinary finite-dimensional interfaces. A future entire gate must reconstruct ALL three-site blocks and ALL actual application/convex/LU/noise boundaries, not accept a single2x2 or a dimension count alone. No formal/kernel/human/configured-family/executable/novelty/priority/publication clearance is claimed.

All priorF3falsefinal/cp062/ENTIREv22withdrawal and parentv35/localmathMAJOR, SEC/W2/optimizer/degeneratefirstorder/ROW qualifiers, cadence/privateapproxZERO/exactness/pause/inventory/orientation/readorder/freeze/clock/admission histories remain. Same18/HOLD/exclusiveOWNroot/originalcutoff/deadline/noGO. No frozenedit/Git/delete/newslot/model/deadlinereset/earlypark/roundcloseout; original unrestricted research continues.
