# P44 v26 — PART24: an UNRESTRICTED regular-SR2-zero representation of a hypothetical indecomposable witness, and an exact complex Hessian matrix constraint

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 05:37:27 PDT 2026**. AUTHOR-WRITTEN candidate; exact symbolic/complex linear algebra only. No scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/new GO. Original HOLD, eighteen owners and October27 cutoff/deadline unchanged. This follows the separate whole-primary ACK sent BEFORE new primary source/reasoning, not live-review interleaving.

## Z0. Actual original target, prior boundary and non-claim

P44 remains UNMET. The target is an explicit eligible4×4 PPT state rho and Hermitian W nonnegative on EVERY COMPLEX Schmidt-rank<=2 vector with Tr(W rho)<0, or an unrestricted theorem that no such pair exists. No old PV/closed chart/normalized-N4 mechanism is promoted as that outcome.

This part changes representation of the FULL witness problem, not of a selected construction family. It proves that any counterexample can be moved to a witness with a rank-TWO zero at Omega2=|00>+|11>, then derives the exact universally-complex second-order constraint there. It does NOT prove that this constraint suffices for global SR2 positivity or for decomposability, and supplies no W/rho counterexample. Those are the exact missing steps below.

All23 earlier parts and both addenda remain preserved through checkpoint107/park-v11. Their later union is still under v113-C/D, not parent-adopted by this part. C19–C27 carry the actual parent four-minor/old-N4 ZERO-new-method-credit/N4-UNKNOWN boundary, whose entire parent record was read after the resumption ACK. The new arguments below do not consume a new scientific result from that union.

Static source intake after the ACK: Yang–Leung–Tang, https://arxiv.org/html/1603.03534v1, Theorem2.7 and its block-Schur proof, Theorem3.2 and Question3.9. Their general Choi peeling leaves a positive M3->M4 remainder in the M4 case; it does NOT say that remainder is decomposable. Their Question3.9 explicitly asks for an indecomposable2-positive M3->M4 map. This is historical problem context, not a current-status/novelty certificate or an imported solution. Johnston–Lovitz https://arxiv.org/html/2609.11849v1, introduction/technical overview and Lemmas4–6/Theorem7, gives a higher-dimensional range perturbation: its rank7 seed at4×4 does not satisfy the required rank<4 condition for excluding SR2. The new route here is not presented as that paper's small-dimensional theorem. Neither source is a premise of Z1–Z3; their finite proofs are inline.

Notation: identify vectors with complex4×4 coefficient matrices; SR equals matrix rank. Let K2 be the closed cone of Hermitian W with q_W(X)=vec(X)^dagger W vec(X)>=0 whenever rank(X)<=2. Let DEC={P+Q^Gamma:P,Q>=0}, with Bob partial transpose. Local invertible congruences preserve both cones. DEC is the dual of the PPT cone under the trace pairing.

## Z1. Product-zero fact and closedness of DEC

**Lemma Z1a.** If W in K2 and x=a tensor b is a product vector with q_W(x)=0, then Wx=0.

*Proof.* For EVERY product vector y, x+t y has Schmidt rank<=2 for every complex t. Thus q_W(x+t y)=2Re(t<x,Wy>)+|t|²q_W(y)>=0 for all t. The linear coefficient must vanish. Product vectors span the entire16-dimensional space, so <Wx,y>=0 for every y and Wx=0. No reality restriction is used. ∎

**Lemma Z1b.** DEC is closed.

*Proof.* If W_j=P_j+Q_j^Gamma converges, Tr(W_j)=Tr(P_j)+Tr(Q_j) stays bounded and is nonnegative. Each PSD sequence has bounded trace and hence lies in a compact finite-dimensional bounded set. A common subsequence converges to PSD P,Q, giving W=P+Q^Gamma. ∎

These two facts are used in the unrestricted reduction, not as a low-dimensional ansatz.

## Z2. Any counterexample admits a rank-two zero

**Theorem Z2 (full-cone regular-zero reduction).** K2 is NOT contained in DEC iff there exists W in K2 outside DEC with

    q_W(Omega2)=0,  Omega2=vec([[I2,0],[0,0]]).

*Proof.* The reverse implication is immediate. For the forward one take any W0 in K2 outside DEC. By closedness, its complement is open. Add a sufficiently small positive scalar epsilon I while staying outside DEC. This makes SR2 positivity STRICT: q>=epsilon||X||_F² on rank<=2.

Choose an arbitrarily small Hermitian perturbation, still strict and outside DEC, having simple spectrum and NO product eigenvector. The existence of such perturbations is not a random/numerical assumption: first split repeated eigenvalues by an arbitrarily small diagonal perturbation in an eigenbasis. Then conjugate by a unitary arbitrarily close to identity. For each of the finitely many eigenlines, the condition that its image is product is a proper closed real-algebraic condition on the unitary (a nonzero2×2 minor excludes it). It has empty interior; otherwise the unitary orbit of that eigenline would have a product-only open subset of projective space, impossible since non-product vectors are dense. A finite union of those exceptional sets still has empty interior. Hence one common arbitrarily small conjugation avoids them all. Denote the resulting witness by H.

The set of norm-one matrices of rank<=2 is compact, so

    mu=min_(rank X<=2, ||X||_F=1) q_H(X)>0

is attained. W1=H-mu I belongs to K2. It stays outside DEC: if W1 were decomposable, H=W1+mu I would be decomposable as well. Let X0 attain zero. If X0 had rank1, LemmaZ1a would give (H-mu I)vec(X0)=0, a product eigenvector of H, contradiction. Thus rank(X0)=2.

By Schmidt decomposition and invertible LOCAL filters there is an L=A tensor B with L vec(X0)=Omega2. Put W=L^(-dagger) W1 L^(-1). Its quadratic form on Omega2 is zero. Every local invertible map preserves Schmidt rank, so W remains in K2. Decomposability is also preserved in both directions: PSD congruence stays PSD, and the partial-transposed term transforms by the corresponding conjugated Bob congruence. Thus W remains outside DEC. ∎

The generic perturbation is an existence proof over an OPEN set, not a scientific sampling operation or an explicit numerical parameter scout. No actual perturbed witness is claimed to have been constructed. It gives a full-quantifier reduction: a universal DEC theorem for the canonical rank-two-zero class WOULD settle the original all-state question. Conversely, a single globally K2-positive indecomposable member of that class WOULD yield a PPT separating state by cone duality. Neither conclusion is delivered here.

## Z3. First and second variations in the rank-two chart

Write an arbitrary coefficient matrix in2×2 blocks. At X0=[[I2,0],[0,0]] its rank-two tangent space is

    T={ V(A,B,C)=[[A,B],[C,0]] : A,B,C in M2(C) },

of complex dimension12. Its orthogonal complement is the lower-right space

    N={ [[0,0],[0,Z]] : Z in M2(C) },

of complex dimension4. EVERY vector in N has Schmidt rank<=2.

**Lemma Z3a (first variation).** If W in K2 and q_W(X0)=0, then W vec(X0) lies in N. Write its lower-right matrix as Delta.

*Proof.* For any A,B,C and sufficiently small COMPLEX t, define the EXACT rank-two curve

    X(t)=[[I+tA, tB],
          [tC, t² C(I+tA)^(-1) B]].

The upper-left block is invertible near t0; the displayed Schur complement is exactly zero, so rank X(t)=2. Its first coefficient is V(A,B,C). Nonnegativity for every complex phase of t forces <W X0,V>=0 for every V in T, proving the claim. ∎

The inverse has its ordinary convergent power series at0; only its exact first two coefficients are used, with no numeric approximation.

**Lemma Z3b (full complex Hessian inequality).** For ALL complex A,B,C,

    q_W(V(A,B,C)) >= 2 |Tr(Delta^dagger C B)|.          (ZH)

*Proof.* The second coefficient of the lower-right block of X(t) is CB. Writing t=s exp(i theta) and taking the exact coefficient after dividing q_W(X(t)) by s² as real s tends to0 gives

    q_W(V)+2Re(exp(2i theta) Tr(Delta^dagger C B)) >=0.

All theta are allowed. Choosing the phase of the displayed scalar gives ZH. No floating comparison or finite phase sample is used. ∎

Consequences:
- H:=W restricted to T is PSD, since ZH is nonnegative on its entire complex linear space.
- W restricted to N is PSD, since all N vectors have SR<=2.
- H vec(X0)=0, while the T/N coupling obeys W X0=Delta. A nonzero Delta can therefore obstruct full PSD even though both diagonal blocks are PSD. Replacing global SR2 positivity by those two PSD diagonal blocks would be invalid.

The normal coupling, rather than a scalar overlap cap or old normalized extension, is the operative new variable.

## Z4. Eliminating the tangent A variables gives one finite doubled Hessian matrix

Partition T as the A-space M2(C) and U=(B,C) in C8, and write

    H=[[H_AA,H_AU],[H_UA,H_UU]].

Since H>=0, H_AA>=0 and range(H_AU) is contained in range(H_AA). Its exact Schur complement is

    S=H_UU-H_UA H_AA^+ H_AU >=0.

Minimizing the left side of ZH over ALL complex A yields exactly

    u^dagger S u >= 2|Tr(Delta^dagger C B)|,
    u=(b,c), b_(j,alpha)=B_(j,alpha), c_(beta,k)=C_(beta,k).   (ZHS)

No A-axis or singular H_AA case is dropped; the Moore–Penrose inverse/range condition handles them.

Define a4×4 complex matrix K_Delta by

    (K_Delta)_((j,alpha),(beta,k))
        = delta_(j,k) conj(Delta_(beta,alpha)).

Then b^T K_Delta c=Tr(Delta^dagger CB). Put the COMPLEX SYMMETRIC8×8 matrix

    R_Delta=[[0,K_Delta],[K_Delta^T,0]].

Thus u^T R_Delta u=2Tr(Delta^dagger CB).

**Theorem Z4 (exact finite Hessian interface).** The full universally-complex inequality ZHS is equivalent to the Hermitian PSD condition

    B_Delta(S)=[[S, -conj(R_Delta)],
                [-R_Delta, conj(S)]] >=0.             (ZH-LMI)

*Proof.* Global rephasing u->exp(i phi)u leaves u^dagger S u fixed and multiplies u^T R_Delta u by exp(2i phi). Therefore ZHS is equivalent to

    u^dagger S u - Re(u^T R_Delta u)>=0 for all complex u.

For y=(u,conj(u)), half the quadratic form of B_Delta(S) is exactly that expression. The doubled matrix commutes with the antiunitary involution J(y1,y2)=(conj(y2),conj(y1)). Every vector splits into y_+ + i y_- with J y_+=y_+, J y_-=y_-. Commutation and Hermiticity make the quadratic form on this split the sum of its values on the two J-real vectors (their cross contribution is purely imaginary and cancels). Hence nonnegativity on all (u,conj(u)) is equivalent to PSD on the WHOLE doubled complex space. This proves both directions. ∎

This is an EXACT characterization of the local Hessian inequality at the regular zero, not an equivalence to global W in K2. Its entries are explicit linear functions of S and Delta; S itself is the exact tangent Schur complement. A candidate failing it is impossible, but passing it is not a P44 certificate.

## Z5. Exact missing mathematical step and prospective attack

The FULL original problem has now been reduced, without a family assumption, to either:
1. construct a Hermitian W outside DEC, globally nonnegative on EVERY complex rank<=2 coefficient matrix, having q_W(X0)=0 and the necessary block/Hessian structure above; then exhibit the eligible PPT negative pair; OR
2. prove that EVERY globally K2-positive W with this rank-two zero is decomposable. By Z2 and closedness, that would imply K2 subset DEC and settle all4×4 PPT states in the SN2 direction.

**NOT_PROVED / named gaps:**
- `ZH-GLOBAL`: ZH-LMI plus PSD diagonal blocks does NOT currently have a proved converse to full SR2 positivity. All rank-two charts, not only the tangent at X0, remain required.
- `ZH-DEC`: no theorem here extracts P,Q>=0 with W=P+Q^Gamma from global K2 positivity and the zero. This is the precise unrestricted no-go gap, not a closed-family conclusion.
- `ZH-PAIR`: no actual globally positive indecomposable W or strictly negative eligible PPT rho has been delivered. Cone duality gives a logical existence bridge only after a genuine W outside DEC is established.

The next action is to analyze the exact Delta/cross-block coupling against PPT-dual positivity, or find a globally admissible counterexample to such a DEC extraction, retaining all complex variables. No new numeric tuple, parameter sweep, solver/certificate request or old N4 replay is admitted. This is parkable INCREMENTAL writing, not a final park or early turn-end. A local-Hessian result is tooling/structural progress toward the original missing step, NOT an answer to P44.

All prior process findings/qualified scopes remain. AUTHOR-WRITTEN, LATER UNREVIEWED; no formal/kernel/executable/triple/configured-family/human/novelty acceptance. **P44 remains UNMET.**

**END OF COMPLETE v26 PART24.**
