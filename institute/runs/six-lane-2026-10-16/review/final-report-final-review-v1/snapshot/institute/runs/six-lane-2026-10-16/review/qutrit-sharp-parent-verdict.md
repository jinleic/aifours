# Sharp two-qutrit entangling-power conjecture: parent verdict

## Result and exact scope

**The maximum normalized entangling power of a two-qutrit dual unitary that is not 2-unitary is 15/16. The same maximum holds for T-dual gates that are not 2-unitary.**

The stronger structural theorem is:

- If U and its realignment U^R are unitary, then **rank U^Γ ≤ 6 or U^Γ is unitary**.
- For a T-dual gate V (V and V^Γ unitary), the corresponding statement is **rank V^R ≤ 6 or V^R is unitary**. Its partial transpose V^Γ always has rank 9.
- Equality in the entangling-power bound occurs exactly when the remaining-cut Gram matrix has six eigenvalues 3/2 and three zeros. Two explicit exact attaining matrices are included.

This is a reviewed **written proof**, not a Lean-kernel formalization. It applies to all complex two-qutrit gates satisfying the stated dual/T-dual hypotheses, not only self-dual, real, Clifford, permutation, generic or nondegenerate gates. It does **not** bound entangling power on all of U(9); that stronger assertion would be false.

The proof answers Rather's **Conjecture 3.3.2**, IIT Madras thesis (2023), ch. 3, printed p. 85 (chapter PDF page 17): no dual or T-dual two-qutrit gate has 15/16 < e_p < 1. The same optimum is described as conjectural on p. 9 of [arXiv:2508.04777v3](https://arxiv.org/abs/2508.04777v3) (25 Jun 2026). [Frozen target](../screening/phys-2-dualunitary-ep15-16-contract.json); [primary-source comparison](qutrit-sharp-priority-audit.md).

## Frozen proof

[Final r4 proof](dualunitary-rank-bound-parent-inputs-v5/LEMMA_R_PROOF.r4.md), SHA-256:

`afd392daa38b9b8bccfded8d855bd72c1f1b824ab844a5f4c32c7db28d6659ed`

[Input manifest](dualunitary-rank-bound-parent-inputs-v5/manifest.json). Earlier versions are retained; their author-status lines remain historical. This verdict owns the integration status.

## Mathematical bridge

For dual U, put W = U^ΓU^Γ†. Realignment/partial-transpose conventions are fixed in the proof. Then tr W = 9 and

\[
 e_p(U)=\frac98-\frac{\operatorname{tr}(W^2)}{72}.
\]

If r = rank W ≤ 6, Cauchy–Schwarz gives tr(W²) ≥ 81/r ≥ 27/2, hence e_p ≤ 15/16. Equality forces r = 6 and all nonzero eigenvalues to equal 3/2. If U is 2-unitary, W = I and e_p = 1. The map U ↦ US transfers the conclusion to every T-dual non-2-unitary gate, with the rank bound on its **realignment**, not its partial transpose.

The rank theorem is not inferred from numerical searches. Its complete case tree is:

1. A product-to-product pair exists by the complex projective dimension theorem. Local unitaries put U into the stated normal form, and biunitarity forces its zero pattern.
2. Four triples of 2×2 blocks are Kraus families of unital trace-preserving qubit channels. The classical Bloch/Pauli normal form and Kraus-span invariance place each three-dimensional span in a twisted symmetric-matrix space, or each smaller span inside a twisted diagonal space.
3. Norm-one corner: Lemma S gives rank ≤ 6.
4. Two three-dimensional sectors: N1, the 2×2 tensor-rank lemma and the explicit pivot/rank lemma give rank ≤ 6.
5. One three-dimensional sector: Proposition A* forces the opposite border blocks diagonal and gives rank ≤ 6.
6. All sectors at most two-dimensional, both corners strict contractions: Proposition B* exhausts the two support patterns, giving rank ≤ 5 or a 2-unitary gate.
7. The stated party permutations cover every normal form, including zero corners, one-dimensional sectors and complex isotropic kernel vectors.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent definition-first symbolic re-derivation | All 96 displayed relation entries match entries/signs/conjugates of the original four biunitarity equations over exact sparse polynomial arithmetic; two wrong-conjugation/dagger controls reject. An independently specified Q(√3) attaining gate satisfies the exact Gram identities | Verifies the algebra and a witness, not the case-tree logic by itself. [Receipt](qutrit-rank-parent-exact-relations-v1.json), [driver](qutrit_rank_parent_exact_relations.py) |
| Parent Q(√6) attaining-gate check | A separate construction from the Codex normal-form data verifies unitary, self-realigned, W = (3/4)(I+SWAP), rank 6, not 2-unitary and e_p = 15/16 exactly | SymPy exact arithmetic. [Receipt](qutrit-sqrt6-gate-parent-check-v1.json), [driver](qutrit_sqrt6_gate_parent_check.py) |
| Worker exact-algebra replay by parent | The four pinned scripts for relations, tensor/N1 algebra, degenerate-case algebra and marginal identities produce byte-identical JSON with every expected Boolean result | Replay, not a second implementation. [Receipt](qutrit-rank-exact-replay-v1/parent-result.json) |
| Parent Lemma-T instance controls | 72 exact complex-rational instances across generic, singular and Jordan pencils satisfy rank ≤ 2; all six no-hypothesis controls have rank 4 | Finite sanity checks only; the universal argument is written. [Receipt](qutrit-lemmaT-parent-check-v1.json) |
| Two task-agent mathematical reviews | Generic branch ACCEPT-WITH-FIXES; residual S/A*/B* and assembly ACCEPT | Model reviews, not human peer review; superseded by the complete CLI reviews for the integrated claim |
| Codex CLI `gpt-6.1-sol`, read-only | ACCEPT-WITH-FIXES, no fatal or major defect; independently reconstructs every case and supplies the Q(√6) witness | Reviewed the pinned interim proof. Its four minor findings are resolved in r2/r3. [Note](qutrit-sharp-codex-hostile-review-v1.note.md), [receipt](qutrit-sharp-codex-hostile-review-v1.receipt.json) |
| Claude CLI `claude-opus-5-5`, no tools | ACCEPT-WITH-FIXES, no missing case or fatal/major issue; independently re-derives §§0–5 and hand-checks both printed matrices entry by entry | Reviewed frozen r3, not code execution. Its 12 editorial findings are applied in r4. [Note](qutrit-sharp-claude-complete-r3-review-v1.note.md), [receipt](qutrit-sharp-claude-complete-r3-review-v1.receipt.json) |
| Parent final-delta review | Complete r3→r4 diff read; all 16 CLI findings discharged; all 18 witness-table rows byte-identical to reviewed r3 | No further substantive mathematical change. [Dispositions](qutrit-sharp-review-dispositions.json) |

Counterexample searches provide no evidential weight for the universal proof. A failed numerical run is not an exclusion.

## Trust, priority and significance

- The core theorem uses standard complex projective geometry and finite-dimensional linear algebra. Fact K is proved in the document and compared with the published King–Ruskai / Ruskai–Szarek–Werner normal form.
- Identification of the 2-unitary set with the single orbit O9 = LU·P9 imports Rather–Ramadas–Kodiyalam–Lakshminarayan Theorem 1. That import is **not needed** for the theorem stated as “not 2-unitary,” nor for Conjecture 3.3.2.
- There is **no Lean formalization**, independent-kernel certification, human peer review or publication of this result.
- The bounded [priority audit](qutrit-sharp-priority-audit.md) found no earlier full optimum or rank theorem. It identifies the prior normal form and self-dual bound and records unread journal/forthcoming sources. This is **NOVELTY-UNCLEAR**, not priority clearance.
- Calibrated significance: a potentially substantive specialist resolution of a concrete two-qutrit conjecture, conditional on independent expert scrutiny and the priority audit's access limits. No broad “major breakthrough” or new-method priority claim is established.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof with exact algebra/witness checks; NOVELTY-UNCLEAR. The frozen phys-2 sharp-15/16 gate is met (2026-10-17 PT).**

Process deviation: the worker initially wrote two r4 table-comparison extracts to `/tmp`, outside the repository-only boundary, then moved them into lane evidence. This is recorded in the worker log and the parent dispositions; it does not change the mathematical result. No commit, push, publication or external contact was authorized.
