# Actual k3 continuation v23 — exact low-noise obstruction to the FULL four-copy operator certificate

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:27:51 PDT 2026**. Owner PhysicsDepol4-2. **NEW AUTHOR-WRITTEN method refutation, NOT an ORIGINAL channel counterexample or global closure.** Exact source-SYMBOLIC written derivation including privately; no scientific program/interpreter/calculator/eval/CAS/enumeration/solver/replay/CLI/nested agent/GO or numeric physical-parameter probe. This argument is independent of, and MUST be read with, `v22-entire-draft-withdrawal-v1.json`: the ENTIRE inconsistent v22 research trail is WITHDRAWN from mathematical credit, sourceSHA `ef8dd82cb7121469043b6d67ada477694bceb88a5ef77bffdff876fdfbfa9812`. The localized own MATHEMATICAL MAJOR remains, not cured by this successor. The current proof explicitly displays every matrix entry used.

## 1. Exact physical lift and the STRICTLY STRONGER attempted certificate

For physical H=(C^2)^tensor4, use copies0/reference and1,2,3/code. F_a^(i) swaps qubit i between copies0 and a. Define for SYMBOLIC u>=0

    K(u)=sum_(a=1)^3 tensor_(i=1)^4(F_a^(i)+uI),
    L3(u)=(1+u)^3(1+3u).

For the normalized Slater vector C_Pi of an ACTUAL rank-three orthogonal projector Pi, each code marginal is Pi/3. The partial-swap identity and summing a therefore give

    <psi tensor C_Pi|K(u)|psi tensor C_Pi>
       =Tr Pi H_u(|psi><psi|),
    H_u(rho)=rho+uX3+u^2X2+u^3X1+u^4I.                   (LIFT)

Thus K<=L3I on ALL of H tensor wedge^3H WOULD imply original k3, but is stronger than testing these actual reference-times-Slater vectors. We REFUTE that full relaxed inequality at symbolic low noise, WITHOUT supplying an eligible original witness.

Named ordinary input: qubit four-copy Schur-Weyl decomposition has local S4 types(4),(31),(22), with physical multiplicities5,3,1. The global sign sector of code S3 is exactly H tensor wedge^3H. We use the LOCAL types(31) at physical sites1,2 and(22) at sites3,4. These types actually occur in the physical tensor product; no fictitious local alternating S4 type or complex physical SVD is introduced. Multiplicity choices do not affect the displayed operator entries.

## 2. Explicit local swap matrices on the SAME code-standard plane

Let E={x in R^3:sum x=0}, q_a=e_a-(1,1,1)/3. Then q_a.q_b=delta_ab-1/3 and sum q_aq_a^T=I_E. The local(31) representation is the zero-sum subspace of R^4, with its code-trivial unit vector t=(3,-1,-1,-1)/sqrt12 plus E on code coordinates. Directly swapping coordinate0 with a gives

    F_a^(31)=[[-1/3,(2/sqrt3)q_a^T],
              [(2/sqrt3)q_a,I_E-q_aq_a^T]].              (31)

The local(22) representation is the zero-sum standard plane of the permutation representation on the three pair partitions of four labels; each swap(0a) fixes one partition and interchanges the other two. With consistent labels it is

    F_a^(22)=3q_aq_a^T-I_E.                              (22)

The code permutations act by the SAME standard representation on E in BOTH local types. Choose h=q_1/||q_1|| and perpendicular unit k. Then in the ordered(t,h,k) and(h,k) bases respectively,

    F_1^(31)+uI=[[a,g,0],[g,b,0],[0,0,c]],
    F_1^(22)+uI=diag(c,d),
    a=u-1/3, b=u+1/3, c=u+1, d=u-1,
    g=2sqrt2/3, g^2=8/9.                               (LOCAL)

All these are exact variable identities. The standard code reflection fixes h and reverses k; the code3-cycle is its real120-degree rotation. Hence the tensors

    T=(hhk+hkh+khh-kkk)/2 in E^tensor3,
    epsilon=(kh-hk)/sqrt2, delta=(hh+kk)/sqrt2 in E^tensor2

are respectively code-S3 sign, sign, trivial. The cubic T is the imaginary harmonic of degree3; the two-form epsilon picks up det(g); the metric delta is invariant. These transformation laws directly verify every global sign vector below.

## 3. An actual two-dimensional sign subspace, with exact compression

With physical sites1,2 type(31),3,4 type(22), set

    v1=t_1 T_234, v2=t_2 T_134,
    v_-=(v1-v2)/sqrt2,
    w=epsilon_12 delta_34
      =(k1h2-h1k2)(h3h4+k3k4)/2.

v1,v2 are orthonormal. w is unit and orthogonal to both because it has NO code-trivial local factor at site1 or2. Thus v_-,w are orthonormal GLOBAL code-sign vectors in the physical space H tensor wedge^3H. They may carry reference/code entanglement; they are NOT asserted to be of LIFT's product form.

Let A_1=tensor_i(F_1^(i)+uI). Every code permutation conjugates the a=1 summand to the corresponding a, and its two sign factors cancel on these vectors. Therefore EVERY compressed matrix entry of K is exactly THREE times the corresponding entry of A_1. No block invariance claim is needed to refute a full operator bound: this exact compression already suffices.

Direct expansion of T and LOCAL gives

    <v_i|A_1|v_i>=a c[2bd+c^2+d^2]/4,
    <v1|A_1|v2>=g^2cd/2,
    <w|A_1|w>=bc(c^2+d^2)/2.

For the off-diagonal v_i entry, the hk and kh terms on sites3,4 BOTH contribute; their sum is the displayed1/2, not1/4. The remaining mixed entries are

    <v1|A_1|w>=g c(d^2-c^2)/4=-guc,
    <v2|A_1|w>=+guc,
    <v_-|K|w>=-3sqrt2*guc=-4uc.

Consequently, with the SAME symbolic a,b,c,d in every term,

    <v_-|K|v_->=c(3u^3-2u^2+1),
    <w|K|w>=c(3u^3+u^2+3u+1).

Use `L3=c(3u^3+7u^2+5u+1)`. The exact reference-gap compression on(v_-,w) is

    [L3I-K]_(v_-,w)
       =u(1+u) [[9u+5,4],[4,6u+2]].                     (GAP2)

All four entries have been derived; no earlier candidate3x3 identity, numerical diagonalization or absent-block inference is used. Its determinant is

    u^2(1+u)^2[(9u+5)(6u+2)-16]
       =6u^2(1+u)^3(9u-1).

Thus the FULL relaxed certificate already fails on a SYMBOLIC interval of low noise. A particularly direct exact variational form, without evaluating a radical, is the fixed representation vector

    chi=(v_--2w)/sqrt5,
    <chi|L3I-K|chi>=3u(1+u)(11u-1)/5 <0
                         for EVERY0<u<1/11.             (OBSTRUCTION)

The constants define a derived structural operator-test vector; no physical state/noise parameter was sampled or numerically instantiated. The open interval is a symbolic conclusion. Since p=2u/(1+2u), it lies within the ORIGINAL low-noise range, so merely restricting the attempted operator theorem to0<=u<=1 does NOT rescue it.

## 4. Why this is DEFINITIVELY NOT an actual reference-times-code witness

At physical sites3,4, local type(22) is the spin0 sector of the FOUR physical copy qubits. For any vector in this sector, every generator of simultaneous rotations obeys

    (S_alpha^(reference)+sum_(a=1)^3 S_alpha^(code a))chi=0

for all three Pauli axes at that physical site. Suppose a nonzero vector there were a PRODUCT psi_reference tensor C_code across the full reference/code cut. Projecting this equation orthogonally to psi on the reference factor would force `(S_alpha-<S_alpha>)psi=0` for ALL three reference single-site Paulis. No nonzero vector is a common eigenvector of their three anticommuting matrices. Contradiction.

Thus this local spin0 sector contains NO reference/code-product vector at all. In particular chi cannot have the actual reference-times-Slater form in LIFT, regardless of its codeword decomposability. The negative expectation REFUTES ONLY the relaxed FULL operator certificate, not the original channel comparison, not U3(3), and not the scalar actual-pair quartic. Additional positive blocks, covariance floors or an all-u qualification cannot repair a uniform operator assertion already false on this actual entangled sector. A valid proof would have to retain the product/Slater constraints or change representation.

## 5. Exact scientific boundary and next representation

New result: a complete exact negative compression of the attempted S4/three-code FULL operator certificate on a real symbolic low-noise interval, with explicit physical-sector realization and proof of noneligibility as an original witness. It replaces the abandoned inconsistent v22 trail; it is NOT a parent-adopted theorem, full original refutation, mathematical execution or finite-check certificate. The earlier new v21 ORIGINAL critical system and v20 strict-PAR/open-neighbourhood candidate remain independent alternatives, not refuted by this stronger-operator failure.

The ORIGINAL arbitrary-state k3, full-B CLIP-prime and actual common-projector quartic remain OPEN. The next live step must use actual reference-times-Slater/product compatibility (or the exact original critical system), not keep proving unused positive S4 sectors or conflate an entangled-copy witness with a physical channel input. All earlier v12–v19/heldleads, additive F3 withdrawal, SEC/W2/optimizer/degenerate-first-order qualifications, historical UNREPLAYED certificate boundaries and own/parent/peer process/zero-credit/cadence findings remain. No global/formal/kernel/human/configured-family/executable/novelty acceptance, old frozen edit, new owner/deadline or scientificGO. Active original continuation, NOT a park or round closeout.
