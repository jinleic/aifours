# Addendum5 — exact coherent-row gluing, gauge-invariant holonomy and all-member path collisions

Actual native clock before writing: **Tue Oct 27 15:26:13 PDT 2026**.
PhysicsMOQLS8-2 / same physics-4 slot. **WRITTEN, UNREVIEWED** all-variable actual-family criterion and obstruction. Only admitted original definitions and elementary unitary/inner-product facts are inputs. No old proof, held guide, local/channel/commutant candidate or bibliography expansion; no numerical state, selected probe, interpreter, CAS, enumeration or solver.

## 1. Why this is a static gluing question, not another move assumption

The motion packets do not supply universal reachability. The tensor packet does not supply a normalized common factor/grid decomposition from generic operator data. Here I return directly to the ACTUAL row ONBs and isolate their exact global consistency condition.

The row-connection representation alone would be an encoding, not progress. The substantive consequences below are: **nonflat triangle holonomy cannot be repaired by any allowed cell phases/member output frames**, and **unique two-step support-path collisions force an all-member obstruction or exact complex cancellation obligations**. These are genuine physical gluing tests, not a scalar budget or an asserted realization of separate local patterns.

All statements are conditional/universal; they do not show that the obstruction occurs in every potential nonclassical four-family or construct a surviving one. Framework/source novelty is not claimed.

## 2. Actual row transitions, full phase conventions

Let Q1,…,Q4 be ANY actual ordinary complex four-MOQLS(n) family, n=8 included. Denote the unitary row-basis matrix of member a,row r by

    R_a(r)=[Q_a(r,1) ... Q_a(r,n)].

For every ordered row pair define

    U_a(r,s)=R_a(r)* R_a(s).

Thus U_a(r,s)_(j,k)=<Q_a(r,j),Q_a(s,k)>. These are unitary matrices, U_a(r,r)=I, and satisfy the exact SAME-member flatness identity

    U_a(r,t)=U_a(r,s) U_a(s,t) for ALL r,s,t.             (FLAT)

For r≠s, the column QLS conditions give

    (U_a(r,s))_(j,j)=0 for EVERY j.                      (COL)

For every two different members a,b, product-basis orthogonality between cells in different rows gives

    U_a(r,s) Hadamard U_b(r,s)=0  for r≠s.               (DISJ)

All factors are the actual complex matrix entries; no absolute-value replacement or real-sign restriction is made.

## 3. Exact forward/converse actual-family caller

Conversely, suppose unitary edge matrices U_a(r,s) are supplied for ALL four members and all row pairs, with U_a(r,r)=I, (FLAT), (COL) and (DISJ). Then they arise from an ACTUAL four-family, up to separate member output unitaries.

**Proof.** From (FLAT) with t=r, U_a(r,s)U_a(s,r)=I, so U_a(s,r)=U_a(r,s)*. Fix an arbitrary common row label r0 and set

    R_a(r)=U_a(r0,r),    Q_a(r,j)=R_a(r)e_j.

Each row is an ONB. Flatness/adjoints give

    R_a(r)*R_a(s)=U_a(r,r0)U_a(r0,s)=U_a(r,s).

Condition(COL) makes the n vectors in any fixed column orthogonal across its n rows. Their norms are1, so columns are ONBs. Hence every Q_a is an actual QLS.

For distinct cells(r,j),(s,k), if r=s then j≠k and row orthogonality already gives zero. If r≠s, (DISJ) gives zero product overlap for every two members. There are n² unit product vectors in dimension n², so every product list is an ONB. The tuple is actual.

Changing the anchor's physical ONB multiplies all R_a(r) on the left by one member-specific unitary and does not change its transitions. No common output frame is required. ∎

This proves the **whole** physical converse, not just local unitary-pattern feasibility. It also shows the exact missing implication when separately proposed row-pair data satisfy local conditions but have not been proven flat.

## 4. Holonomy is a gauge-invariant obstruction to phase-only repair

For any three row labels put

    H_a(r,s,t)=U_a(r,s)U_a(s,t)U_a(t,r).

For unitary edges with adjoint reversal, (FLAT) is equivalent to H_a=I on all triangles. In the actual connection adjoint reversal already follows as above; a proposed local edge system must supply it as well or obtain it from full flatness.

Multiply each entry Q_a(r,j) by an arbitrary unit phase. Let D_a(r) be the corresponding diagonal matrix of phases. The row transitions transform as

    U_a(r,s) -> D_a(r)* U_a(r,s) D_a(s),
    H_a(r,s,t) -> D_a(r)* H_a(r,s,t) D_a(r).

A separate member output unitary cancels entirely from every U_a(r,s). Therefore

> **If a proposed coherent-edge candidate has H_a≠I, no entry-phase gauge or separate member output frame can repair that failure.**

Conjugation cannot turn a nonidentity matrix into the identity. This is a full complex/unitary statement, not an eigenvalue estimate or a selected triangle check.

Common row/column permutations merely relabel the shared row nodes/column coordinates. Row or column permutations chosen independently for different members are NOT silently allowed: they would change the original same-cell pairing. Local edge matrices cannot be assigned independent phase corrections unrelated to node gauges and still be called physical row-basis data.

No concrete nonflat instance is tested or asserted. The theorem identifies an exact obstruction and its irreparability under the model's allowed isotopies.

## 5. Exact all-member two-step cancellation obligation

Take three rows r,s,t with r≠t and any endpoint columns j,k. For each member a define the nonzero path-index set

    P_a(r,s,t;j,k)={ell: U_a(r,s)_(j,ell) U_a(s,t)_(ell,k)≠0}.

Flatness gives the actual amplitude identity

    U_a(r,t)_(j,k)
      =sum_(ell∈P_a) U_a(r,s)_(j,ell) U_a(s,t)_(ell,k).   (PATH)

No summand phase has been discarded. The endpoint condition(DISJ) says the four sums in(PATH) are pairwise zero-product: at most one member's sum may be nonzero.

### Unique-path collision obstruction

If P_a has exactly one element, its sum is a product of two nonzero complex entries and is nonzero. Therefore:

1. no different member b may also have exactly one nonzero path;
2. EVERY other member's path sum must vanish exactly;
3. if another member has two nonzero paths, their two products must be exact negatives.

Thus a unique-path amplitude in one member imposes simultaneous cancellation conditions on ALL THREE other members. It cannot be checked against only a convenient companion.

If the endpoints have j=k, (COL) forces the endpoint amplitude zero in EVERY member. Hence no member may have exactly one nonzero path at such a diagonal endpoint pair. This includes all column-completeness constraints, not just inter-member orthogonality.

The intermediate row s may be distinct from both endpoints, giving the nontrivial triangle interface. The identities remain valid if it coincides with one endpoint, where they reduce to the corresponding direct-edge statement; no exceptional row case is silently excluded.

### The two-path balance is phase-coherent, not just a cardinality bound

When exactly two paths ell1,ell2 must cancel, write

    z1=U_b(r,s)_(j,ell1) U_b(s,t)_(ell1,k),
    z2=U_b(r,s)_(j,ell2) U_b(s,t)_(ell2,k).

The necessary and sufficient cancellation equation is z1=−z2. In particular

    |U_b(r,s)_(j,ell1)|² |U_b(s,t)_(ell1,k)|²
      =|U_b(r,s)_(j,ell2)|² |U_b(s,t)_(ell2,k)|²,

but equality of those magnitudes alone is NOT the complete complex equation. All larger path sets retain their entire complex sum as the unpaid condition; they are not declared cancelable merely because their size is at least2.

No numeric phase or endpoint is chosen here: these are universal implications for the actual free variables.

## 6. Why intermediate cell phases cannot create the required cancellation

Under the node phase gauge, every path product at fixed(r,t;j,k) is multiplied by the SAME nonzero endpoint phase

    conj(D_a(r)_(j,j)) D_a(t)_(k,k).

The intermediate D_a(s) phases cancel term by term. Consequently the zero/nonzero sum in(PATH), the ratio of its two nonzero terms and every unique-path obstruction are invariant under all allowable entry rephasings.

This is an exact failure of a tempting gluing step:

    “Choose independent phases at the intermediate row to repair the endpoint sum”

is not available for actual row-transition data. Such phases are only node gauges and cannot change whether the cancellation holds. A proof that local unitary/support data can be realized must supply the coherent row bases/flatness and the actual complex cancellation, not an appeal to independent phase freedom.

This does not forbid changing the actual row bases by a non-gauge physical deformation. Those changes must satisfy the full original QLS/product constraints and cannot be treated as entry-phase isotopy.

## 7. Source-compatible classicality criterion, not a closure theorem

For one member a, the following are equivalent:

- it is classical in the paper's per-member global-ONB-ray sense;
- for one anchor row r0, EVERY U_a(r0,r) is monomial (one unit-modulus entry in each row/column);
- EVERY transition U_a(r,s) is monomial.

**Proof.** In a classical square each row lists the same n ONB rays with phases, so all transitions are monomial. Conversely, if all anchor transitions are monomial, the construction in §3 puts every entry on a ray of the anchor ONB. Individual phases are allowed by the source definition. Flatness makes products of anchor monomial transitions monomial, yielding the third formulation. No common basis among different members is inferred. ∎

Thus the original four-family target has an exact static formulation: show that all FOUR coherent edge systems are monomial, or supply an actual flat/COL/DISJ system with a nonmonomial member. **I have not proved either alternative.**
The exact material obstruction supplied above is that locally feasible edges/supports and allowed cell phases do not replace coherent triangle amplitudes/holonomy. The encoding and monomial criterion alone are not counted as scientific progress.

## 8. Degeneracies, missing inputs and original-target boundary

- Zero entries/path sets are handled exactly; an empty path sum is0. A singleton is nonzero. Multiple paths require their actual complex sum, not a presumed generic cancellation.
- If r=t, the endpoint matrix is I, not a cross-row zero-disjointness condition. The collision theorem deliberately assumes r≠t. The identity/diagonal cases are not used as selected probes.
- The source's standard form is permitted using separate member output frames, but the proof never assumes different members' row/column indices can be normalized independently.
- Phase gauges preserve supports/monomialness and conjugate holonomy; output unitary frames cancel. None of these freedoms can supply a missing nonflat physical realization.
- This packet does not assert that local COL/DISJ unitary systems that fail flatness exist in a particular tested configuration, nor that no alternative physical realization of a pattern exists. It gives exact necessary/converse input conditions and an irreparable gauge obstruction **if** nonflatness/collision is established in a future all-variable argument.
- The existing adopted LOCAL/intrinsic statuses do not, by their safe descriptions, provide a theorem forcing these complete coherent complex equations or their universal monomial conclusion. No such old proof/candidate is imported from a metadata alias.

**Next original-model obligation:** derive a genuinely universal restriction on the flat four-member transition network at order8—rather than only a per-edge support budget—or identify an actual complete realization. The current paper's six-family proof and the new move/tensor criteria do not supply that universal monomiality/realization step. The problem remains OPEN at that exact gap.

Ordinary imports: finite-dimensional row-basis unitarity, inner-product/tensor-product identities, matrix multiplication/adjoints and ONB completeness by dimension. Every special gauge/holonomy/path/actual-family consequence is derived here. No compiled check, matrix instance, algebra interpreter, enumeration or numeric comparison was used.

S1/current parent standing direction remains the only written scope; source-equivalence/priority and stronger independent-model/human/formal/kernel/executable gates are not cleared. All old STOP outside S1, HOLDv2/N4 UNKNOWN historical exit UNESTABLISHED/aux214STOP/findings/ZERO consumers persist. No old proof/review/park/checkpoint/held-guide/bibliography expansion, nested agent/model CLI/paid API, Git/delete/contact/infrastructure action. New owner root only; prior frozen packets remain unchanged. This result is a conditional written coupling obstruction, not a numerical M(8),maximum-three,A10/A11/native or full four-family theorem.
