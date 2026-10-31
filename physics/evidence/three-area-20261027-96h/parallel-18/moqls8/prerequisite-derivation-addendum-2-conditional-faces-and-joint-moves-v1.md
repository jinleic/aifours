# Addendum2 — exact conditional faces, common-unitary gluing and joint-move collision obstruction

Actual native clock before writing: **Tue Oct 27 15:01:27 PDT 2026**.
PhysicsMOQLS8-2 / same physics-4 slot. **WRITTEN / UNREVIEWED**, all-variable actual-object statements at named elementary complex-linear-algebra facts. No calculation tool, numerical state, selected probe or scientific execution.

The first packet and addendum1 remain immutable. This body is self-contained at the admitted QLS/MOQLS definitions: it does not take an unreviewed earlier candidate, old LOCAL/channel/commutant theorem, held source or private guide as an opaque correctness input. Prior contact is not erased; no private noninfluence or historical-novelty certificate is claimed.

## 1. Original physical quantifiers, not a support ansatz

Let (A,B2,B3,B4) be ANY actual ordinary complex four-MOQLS(n) tuple, in particular n=8. Individual rows/columns are ONBs; for every pair of members the n² same-cell products form an ONB. All classical/nonclassical combinations, phases and separate member output frames are allowed.

Let S⊂C^n be ANY nonzero subspace, and Omega ANY subset of cells such that A_x∈S for every x∈Omega. No assumption is made that Omega includes every vector lying in S, that entries have any global weight bound, or that outside projections are coordinate rays. A unitary U on S acts on A_x only for x∈Omega; all other entries and all mates are unchanged. Call the resulting array A^U.

The operation is an actual proposed move on one known family. It is not a global normalization of every unknown four-family and not an arbitrary per-cell choice of a different unitary.

## 2. Exact pair-product conditional resolution

Write P_v=|v><v| and P_S for orthogonal projection onto S. Pair-product completeness of A and a mate B_a says

    sum_(y∈X) P_(A_y) tensor P_(B_a(y)) = I tensor I.

Contract the second factor against the actual unit vector B_a(x). For EVERY cell x,

    sum_y |<B_a(x),B_a(y)>|² P_(A_y) = I.                (CR)

No entry phase, basis alignment or averaging of the original family is involved. This is an exact consequence of its actual ONB, not a separately assumed channel law.

For x∈Omega define, as an operator on S,

    F_x^a = sum_(y∈Omega) |<B_a(x),B_a(y)>|² P_(A_y),
    H_x^a = sum_(y∉Omega) |<B_a(x),B_a(y)>|²
                                   |P_S A_y><P_S A_y|.

Compressing(CR) to S gives

    F_x^a + H_x^a = I_S,       0≤F_x^a≤I_S.              (FACE)

Its one-eigenspace is precisely

    E1(F_x^a)=ker H_x^a
      = {v∈S: <v,P_S A_y>=0 for every y∉Omega
                               with <B_a(x),B_a(y)>≠0}.  (KERNEL)

**Proof of the last equality.** For any v, <v,Hv> is the sum of the nonnegative terms |<B_a(x),B_a(y)>|² |<v,P_S A_y>|². It vanishes iff each term with positive coefficient vanishes. A positive-semidefinite operator has zero quadratic form precisely on its kernel. These are finite sums, so there is no null-set or limit issue.

The original A_x belongs to E1(F_x^a): outside mixed-pair product orthogonality forces each of those terms zero. Equivalently the y=x term in F has weight1 and every other active term with positive weight is orthogonal to A_x. No maximal-eigenvalue assertion for a nonphysical operator is assumed.

## 3. Row and column boundary faces

For x∈Omega put

    R_x = span{A_y: y∈Omega and y shares x's row},
    C_x = span{A_y: y∈Omega and y shares x's column}.

The displayed active vectors within one row are orthonormal, so their projector sum is the orthogonal projector onto R_x; the analogous statement holds for C_x.
Compressing the complete original row/column resolutions to S shows

    span{P_S A_y: y∉Omega, same row as x} = S∩R_x^perp,
    span{P_S A_y: y∉Omega, same column as x} = S∩C_x^perp.

For example, the row's outside positive sum is I_S−P_(R_x), whose range is R_x^perp inside S. This proves the equality, not merely one containment. It also handles outside vectors with zero projection automatically.

Define the actual **permission subspace** for every active cell by

    M_x = R_x ∩ C_x ∩ E1(F_x^2) ∩ E1(F_x^3) ∩ E1(F_x^4).

It contains A_x and therefore is nonzero. All five factors come from the SAME original family and the SAME active-cell set; they may not be mixed between different source families.

## 4. Full actual-object iff criterion

> The updated tuple (A^U,B2,B3,B4) is an ACTUAL four-family iff
>
>     U A_x ∈ M_x for EVERY x∈Omega.                    (PERMIT)

### Necessity

Actual row/column orthogonality with every unchanged outside entry forces U A_x into R_x and C_x by §3. If a mate overlap at an outside cell is nonzero, updated pair-product orthogonality forces <U A_x,P_S A_y>=0. By(KERNEL) this is membership in every E1(F_x^a). Thus all conditions are necessary.

### Sufficiency

All norms are preserved. Two active entries undergo the same U, so their A inner product is unchanged; two inactive entries are unchanged. For a mixed row/column pair, membership in R_x/C_x gives zero A overlap. Hence every row and column is an orthonormal list of n unit vectors in dimension n and is an ONB.

For a mixed A^U–B_a cell pair, a zero B_a overlap already makes the product overlap zero; a nonzero B_a overlap is covered by E1(F_x^a). Pairs both active or both inactive retain the original A overlap and hence product orthogonality. All n² product vectors are unit and pairwise orthogonal in dimension n², so they form an ONB. Other member pairs are unchanged. This establishes the entire physical converse. ∎

This is a structural reduction to exact positive conditional faces, not just a new list of coordinates for the original condition. It shows which row, column and three-mate interfaces prohibit a proposed common operator even when a separate local support/normalization test would allow it.

## 5. Independent local choices do not supply a common U — exact Gram bridge

Suppose proposed target vectors v_x∈M_x are specified for all x∈Omega. There is a SINGLE unitary U on S with U A_x=v_x for all active cells iff

    <v_x,v_y>=<A_x,A_y> for EVERY x,y∈Omega.              (GRAM)

No spanning assumption is needed.

**Necessity** is unitarity. For **sufficiency**, on T=span{A_x:x∈Omega} define the linear map sum c_x A_x ↦ sum c_x v_x. Equality of all Gram entries makes its norm-squared exactly the same for every coefficient vector. A zero source combination therefore has zero target combination, so the map is well-defined and isometric. Its range is span{v_x} of the same dimension. Their orthogonal complements inside S have equal finite dimension; extend the isometry by a unitary between those complements. This gives the required U. The diagonal Gram entries give target norm1, including repeated/proportional source entries and every phase consistency relation. ∎

By §4 this common U supplies an actual family update. Thus full physical gluing of a move requires BOTH local membership and( GRAM ). The nonzero spaces M_x, or choosing a legal vector in each separately, do not by themselves establish common-unitary compatibility.

The original choice v_x=A_x is always a solution, so this theorem does not manufacture a nontrivial move. A projectively changed update requires at least one v_x outside the ray of A_x, in addition to all Gram constraints.

## 6. Rigidity from saturated permissions, with no dimension-two restriction

Call an active cell saturated if M_x=span{A_x}. Every admissible U then has U A_x=alpha_x A_x, with alpha_x a unit phase.

Join two saturated projective rays when their original inner product is nonzero. For every such edge, unitarity gives alpha_x=alpha_y. Consequently U is scalar on the span of each connected component of this graph. Different component spans are orthogonal: all their generating ray pairs have zero overlap.

> If saturated rays span S and their nonorthogonality graph is connected, EVERY admissible U is scalar on S.

More generally the saturated part forces a block-phase action on its orthogonal component spans; unsaturated active cells may impose further restrictions through(PERMIT). Disconnectedness by itself is NOT claimed sufficient for an admissible nontrivial move.

There is also a stronger projective conclusion when **all active cells are saturated**, even without connectedness or spanning S: every updated active entry differs only by its own phase. All inactive entries are unchanged. The resulting tuple is entrywise-phase isotopic to the original and cannot change its classical/nonclassical status. A projectively nontrivial admitted move therefore needs an unsaturated cell, but unsaturation alone is not sufficient because(GRAM) still couples all active targets.

### Two immediately checkable symbolic sufficient conditions for saturation

These are universal implications, not selected checks or evaluated examples.

1. If x is the only active cell in its row or its column, R_x or C_x is already span{A_x}, so x is saturated.
2. If for some actual mate B_a every other active cell y≠x has <B_a(x),B_a(y)>=0, then F_x^a=P_(A_x); its one-eigenspace is span{A_x}, so x is saturated.

The second condition comes from pair-product **completeness** (CR) and includes the actual complex overlaps of a mate, not only A's own row/column incidence. Either can prevent a support-shrinking or ray-changing operation. Neither is asserted to occur universally in the open four-family problem.

## 7. ALL-member synchronization — singly legal moves can collide

The preceding criteria keep the other three members fixed. Applying four independently certified moves simultaneously has an additional exact obstruction.

Let (A1,A2,A3,A4) be an actual original tuple. For each a let A'_a be an actual QLS such that replacing **only** A_a by A'_a, while all three other members stay ORIGINAL, gives an actual four-family. This hypothesis may be supplied by(PERMIT)+(GRAM), but no particular move form is required for the following theorem.

Define its zero-erasure set

    L_a={e: e∈Z(A_a) and e∉Z(A'_a)}.

> The simultaneous tuple (A'_1,A'_2,A'_3,A'_4) is actual iff the four zero-erasure sets L_a are PAIRWISE DISJOINT.                         (SYNC)

### Why every erasure is on an original common-zero pair

If e∈L_a, the new A'_a overlap is nonzero. Single-replacement legality therefore forces the overlap of EVERY other original member at e to be zero. The original A_a overlap was zero by definition. Hence all four original overlaps at e are zero.

### Necessity

A pair in both L_a and L_b has nonzero updated overlaps in two different members, contradicting updated pair-product orthogonality. Thus simultaneous actuality requires disjointness.

### Sufficiency and all original pair cases

For any e, originally at most one member has nonzero overlap.

- If one original member a has nonzero overlap, single-replacement legality for every b≠a forces the updated b overlap zero. Thus at most the updated a overlap can be nonzero; all updated member-pair products are orthogonal there.
- If all original overlaps are zero, an updated nonzero overlap occurs exactly when e belongs to that member's L_a. Pairwise disjointness permits at most one.

This covers every cell pair. Each A'_a was already an actual QLS, all entries are unit, and every updated product list has n² orthogonal unit vectors in dimension n². Hence all updated pair products are ONBs and the simultaneous tuple is actual. ∎

Thus individually legal one-member choices are not a substitute for same-family gluing of several simultaneous moves. At a collision they cannot be combined, even though every separate update was physical against the original mates. Sequential updates must recompute the conditional faces against the actual NEW mates.

If every move is zero-preserving, L_a is empty and synchronization is automatic. This recovers the forward safety of the paper's classicalization operations without licensing the reverse operation: inverse moves may erase newly created zeros and must satisfy(SYNC). No assertion of a strict collision in a particular physical instance, or of an actual inverse family, is made.

## 8. Degeneracies, frames and exact residual

- Omega empty gives no target constraints and the unchanged actual family. A one-dimensional S or fully saturated active set allows at most entry phases on the active rays; it is not a nonclassical construction.
- If Omega is the entire cell set and S=C^n, the row/column spans and every F_x^a are the identity on S. Any U is allowed, but it is just a global output isotopy of that member. Large permission dimension or a projectively changed ray therefore does NOT imply changed classicality.
- Projection-zero outside cells and mate-zero overlaps make zero terms in the positive resolutions, with no artificial eigenray constraint. The kernels/one-eigenspaces include all repeated/dependent entries.
- Every formula is invariant under entry rephasing in the relevant zero tests; the full(GRAM) equation retains actual complex phases rather than just their absolute values. Separate member output unitaries preserve the mate inner products. No common frame is used.
- Permitted vectors selected independently in M_x are not certified unless one common Gram-preserving U exists. Arbitrary pattern/net/operator data are not promoted to actual QLS or pair-product completeness.
- Saturation/connected spanning are sufficient rigidity conditions, not a theorem that every nonclassical family meets them. The failure of those sufficient conditions does not prove a deformable family.
- The single-member theorem allows arbitrary weights in all four original members. The simultaneous theorem assumes exact single-replacement actuality and proves the missing joint condition; it does not remove the need to obtain those single replacements from an original actual family.

**What is genuinely supplied here:** a complete actual-family iff permission theorem with positive conditional resolutions; the missing common-unitary Gram bridge; rigorous saturation/eigenphase obstructions; and an exact four-member collision criterion for simultaneous gluing. These are conditional all-variable coupling results, not a scalar necessary-budget increment.

**First remaining universal step:** the admitted definitions do not yet force a nontrivial unsaturated, Gram-compatible, collision-free update, nor do they force saturation/connected spanning for every possible nonclassical four-family. No such existence or global obstruction has been proved. That is an exact missing premise rather than a numerical M(8)/maximum-three result. Higher-component actual realization and original four-family classicality/existence remain OPEN.

Ordinary imports are finite-dimensional tensor-product ONB completeness, positivity of finite rank-one sums, kernel/range orthogonality, elementary isometry extension, and preservation of inner products by a unitary. All special applications are proved above. No old tested-channel, commutant or local-span proof is imported by resemblance of notation. No formal/kernel/human/configured-family/executable or historical-novelty acceptance is claimed; Main must read the full packet and a complete-scope review before adoption.

Only S1-permitted source/written work and new-owner-root writes occurred. Scientific HOLDv2, N4 UNKNOWN/exit UNESTABLISHED, auxiliary214 STOP, every prior finding/ZERO consumer and original STOP outside S1 persist. No interpreter/calculator/eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/boundary/decimal probe, nested agent/model CLI, Git/delete/contact/infrastructure action. The research window still ends2026-10-31T21:23:27.000Z; these candidate packets do not end the research assignment.
