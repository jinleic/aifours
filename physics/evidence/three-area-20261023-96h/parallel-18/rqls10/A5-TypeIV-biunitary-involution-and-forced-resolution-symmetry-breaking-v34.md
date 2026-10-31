# RQLS10 v34 — an exact19-complex-dimensional row/column involution, and EVERY valid resolution must BREAK A5 symmetry

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE writing this NEW manuscript: **Mon Oct 26 09:08:03 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite equivariance/Hilbert–Schmidt/subgroup/Latin-incidence proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or accepted finite-witness claim.

## 1. Whole TypeIV row/column problem is ONE biunitarity equation pair

Use the COMPLETE v31 TypeIV master, physical natural ten-duad permutation representation U, reference duad a0, H=S3. Let

    A=Comm(U(H)),         dim_C A=9+1+9=19.

For ANY V in this algebra—not necessarily unitary—define its full equivariant vector tensor by

    Q(V)_(a,b)=U(g_a) V U(g_a)^dagger e_b,

with g_a taking a0 to a. Commutation with H makes this independent of g_a. The tensor has exact vector covariance. Its reference ROW is V itself.

Define a LINEAR map F:A->A by its columns

    F(V)e_a=Q(V)_(a,a0)
           =U(g_a) V U(g_a)^dagger e_(a0).       (FLIP)

This is the complete literal definition, not an unprinted19x19 numerical matrix. It uses only the finite A5 action and may be expanded exactly if a later authorized gate chooses; no expansion program was run.

**Theorem.** F is a complex-linear Hilbert–Schmidt UNITARY INVOLUTION on A, and

    Q(V) is a QLS10  IFF  V and F(V) are BOTH unitary matrices.

This is the ENTIRE TypeIV row/column condition, not an ansatz, a single-column necessary test or a partial solution. Full Latin resolution and100-ray distinctness remain the separate literal v31 requirements.

Proof that F maps A to A: a reference-column stabilizer h in H fixes a0, so exact covariance gives

    U(h)F(V)e_a=Q(V)_(ha,a0)=F(V)U(h)e_a.

Thus F(V) commutes with H. Row/column swapping of the equivariant tensor preserves covariance. Its new reference row is EXACTLY F(V). An equivariant tensor of this form is uniquely determined by its reference row (the master construction), so

    Q(F(V))_(a,b)=Q(V)_(b,a).

Swapping twice yields F^2(V)=V.

Each row matrix of Q(V) is a unitary conjugate of V; hence the total tensor squared norm is10||V||_HS^2. Swapping its first two indices preserves that norm, so

    10||F(V)||_HS^2=10||V||_HS^2.

Complex linearity and polarization give preservation of the full Hilbert–Schmidt inner product; together with F^2=I this proves F is a unitary involution(F^dagger=F AS A SUPEROPERATOR). This does NOT mean F preserves the adjoint or products of its matrix inputs: for example F(I)=e_(a0)*1^T is rank1, not a unitary matrix.

If V is unitary all rows are ONBs. If F(V) is unitary the reference column is an ONB; A5 acts transitively on column labels and covariantly on their vectors, so EVERY column is a conjugate column ONB. Conversely any QLS gives both reference ONBs and hence both unitarities. The proof is exact and two-sided.

## 2. The full-resolution task cannot be simplified by demanding covariance

The following combinatorial obstruction is INDEPENDENT of the physical representation and quantum vectors.

**Resolution theorem.** There is NO partition of the10x10 ten-duad cell grid into ten full row-and-column transversals that is invariant under simultaneous A5 action on the two coordinates.

Equivalently, there is NO order10 Latin square on this grid for which the diagonal A5 action on row/column duads induces ANY permutation action on its ten symbols. The symbol action is NOT presumed the same ten-duad action; ALL possible A5 actions on ten symbols are covered below.

Thus ANY maximal resolvable quantum array having this row/column symmetry would have to use a resolution BREAKING that symmetry. This does NOT prohibit an arbitrary allowed noncovariant resolution, does not permit us to demand a covariant one WLOG, and does not by itself exclude an original array.

## 3. Complete proof for ALL possible symbol actions

A fixed symbol would represent an A5-invariant transversal of ten cells. The full ordered-cell action has orbit sizes10(diagonal),60(intersecting),30(disjoint); the ONLY invariant ten-cell subset is the diagonal itself. Thus at MOSTONE symbol can be fixed by A5.

Any nontrivial A5 orbit of size<=10 has size5,6 or10. The orbit size divides60 and is a subgroup index;2,3,4 are impossible because a nontrivial action of simpleA5 is faithful, while S2,S3,S4 have order smaller than60;7,8,9 do not divide60. Therefore an action on ten symbols with at mostONE fixed symbol must be either a single transitive10-orbit or two5-orbits. The alternatives6+fourfixed,5+fivefixed andtenfixed contradict the at-mostONE condition.

### 3.1 Two5-orbits fail already at a diagonal cell

A symbol in a5-orbit has stabilizer of order12. Any order12 subgroup of A5 contains NO S3 subgroup: otherwise the S3 is normal of index2; its unique characteristic C3 would then be normal in that order12 group, contradicting N_A5(C3)=S3 of order6. The normalizer count is the direct permutation calculation from v27.

But the diagonal cell(a,a) has an S3 stabilizer, which would have to fix its symbol and hence lie in that symbol's order12 stabilizer. Impossible. Thus the5+5 symbol action cannot support a Latin resolution.

### 3.2 A transitive10-orbit forces a disjoint-cell row/column clash

A symbol stabilizer now has order6 and is S3. Every order6 subgroup of A5 is the normalizer of its unique C3, so these are exactly the ten duad stabilizers. The ten-symbol action may therefore be relabeled as the natural duad action. The map from the diagonal ten-cell orbit to symbols is equivariant; its point stabilizers have equal order6, so after this natural labeling the diagonal cell(a,a) has symbol a.

For a DISJOINT pair(a,b), its order2 cell stabilizer t swaps the two members of each duad and fixes the fifth point. It fixes exactlyTWO duads in the ten-symbol action, namely a and b. Thus the symbol of(a,b) must be either a or b. If it is a, that row repeats the symbol already at(a,a). If it is b, that column repeats the symbol already at(b,b). Either violates the Latin condition.

This rules out the entire remaining symbol action, and completes the resolution theorem. No list of Latin squares, finite search, assumption about cyclicity or numerical table is used.

## 4. EVERY valid quantum resolution has an orbit of at leastFIVE distinct resolutions

If a quantum array with the stated ray covariance nevertheless has some valid FULL resolution R, applying each A5 element to its cells produces another valid full resolution: rows/columns are permuted and the common physical unitary preserves each transversal ONB. The resolution theorem says its stabilizer is a PROPER subgroup of A5. A5 has no nontrivial permutation action of degree2,3,4, so the orbit has at least5 distinct resolutions.

This is a statement about several full partitions of the SAME cells, NOT a t-RQLS promotion: different orbit resolutions may have transversals sharing MORE THANONE cell with each other. The cross-resolution orthogonality/intersection requirements in t-resolvability have NOT been proved. Do not infer5-resolvability, a new family, or a numerical witness from the orbit count.

The same conclusion holds for ANY physical ray representation with simultaneous ten-duad covariance, not only TypeIV, provided an actual full resolution exists. It remains an orbit necessity, not proof of such existence.

## 5. Exact remaining task and full acceptance boundary

TypeIV is now reduced to finding V in the literal19-complex-dimensional commutant algebra with V,F(V) both unitary, subject to v32/v33's nonscalar-standard/minimum-rank constraints; then finding an ACTUAL necessarily symmetry-breaking resolution L and verifying ALL hundred distinct rays with v31's strict projective inequalities. Neither the biunitarity pair nor a resolution nor a100-ray witness is solved here.

An ENTIRE review must reconstruct v31's phase-gauged iff master, ALL of the F algebra/covariance/flip/norm/necessity-and-sufficiency proof, ALL symbol orbit classifications and BOTH Latin obstructions, and the distinction between orbit-many-resolutions and t-resolvability. A one-column norm check or a chosen ten-duad symbol action is not the whole result.

Named classical inputs are simplicity of A5, elementary orbit–stabilizer/finite subgroup facts printed in section3, and Hilbert-space polarization. No unprovided Pauli/600-cell/Latin/graph classifier is a premise. No scientific execution, external model or unperformed finite-witness/checker/control/vendor/priority gate was used or called passed. No A5-WLOG, unrestrictedno-go, formal/kernel/family/human/current-openness/novelty promotion. All original noncovariant intrinsic10/4+6/5+5 branches remain OPEN; inside A5 covariance the surviving ordinary types remain open as previously bounded. All old process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines persist. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; primary continues exact biunitary/higher-rank/symmetry-breaking geometry, no early pending-review park.
