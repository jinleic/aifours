# P1-B3 full row 1 by own-frame reuse — CANDIDATE v1

Frozen at 2026-10-19T16:33:31-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `c0f104a9895ce093fb9f739408f2aa65e9a989766bebe6bdbe0a7be2c806bde3`). Status: CANDIDATE written mathematics, not reviewed or accepted. All hand-written finite tables below are verified line by line in the text; no code, CNF, binder, probe, enumeration, solver, checker, CLI, numerical package or nested agent was used to find or establish any statement.

**Outcome class (preregistered): EXACT_FULL_ROW_PARTIAL_CONSTRUCTION.** Genuine B3 row-1 joint feasibility holds. On a whole nonempty support class D of genuine B3 axis data, with ALL amplitudes and phases quantified, an explicit full row 1 satisfies every direct QLS equation and every pairwise tensor-orthogonality equation on R = row 0 ∪ column 0 ∪ row 1. Hence there is NO universal contradiction at the row-1 level. This is not a B3 exclusion, not a full configuration, not an extendability statement, and not a Boolean statement. GB 15/18, the three GB UNKNOWNs, B2, A10/A11 and the n=8 target are unchanged.

## 1. Setting

Write [8] = {0,...,7} and e_0,...,e_7 for the computational basis of C^8. Hypotheses (as in the earlier B3 notes):

- **H1.** Q_1,...,Q_5 are genuine QLS(8), pairwise orthogonal ([PRIM] LF195-225: rows and columns are ONBs; for s != t the 64 vectors Q_s(z) ⊗ Q_t(z) form an ONB).
- **H2.** Q_s(0,c) = w_{s,c} e_c with |w_{s,c}| = 1, for all s and c.
- **H3 (SB2).** supp Q_1(1,0) = {1,2,3}; supp Q_s(1,0) = {s+2} for s = 2,...,5.
- **H4 (exact P1-B3 template).** supp Q_1(i,0) for i = 2,...,7 is {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3}.

Put q_s^r := Q_s(r,0) (so q_s^0 = w_{s,0} e_0). For a unit vector a and square s, write S_s(a) := {c : <e_c,a> != 0} (common-frame support) and T_s(a) := {r : <q_s^r,a> != 0} (own-column-0-frame support).

Let R := {(0,c) : c ∈ [8]} ∪ {(r,0) : r ∈ [8]} ∪ {(1,j) : j ∈ [8]}. An **axis datum** is an assignment of unit vectors to row 0 ∪ column 0 satisfying H2-H4 and every direct equation of H1 among those cells. A **row-1 partial datum** is an assignment of unit vectors to R satisfying H2-H4 and every direct equation of H1 among cells of R:

- (E1) in each square, row 0, row 1 and column 0 are ONBs, and for each j = 1,...,7, Q_s(0,j) ⊥ Q_s(1,j);
- (E2) for s != t and distinct cells x, y ∈ R: <Q_s(x),Q_s(y)> <Q_t(x),Q_t(y)> = 0.

These are exactly the restrictions of the H1 axioms to R. Rows 0 and 1 and column 0 lie entirely in R. A column j >= 1 meets R in (0,j),(1,j), so its ONB axiom restricts to the orthogonality of that pair. A row i >= 2 meets R in (i,0) only, so its axiom restricts to unit norm. Tensor orthonormality restricts to pairwise orthogonality, since unit norms are automatic.

## 2. Lemma 1: exact characterization of row-1 extensions (re-proved here)

**Lemma 1.** Fix an axis datum and unit vectors a_{s,j} := Q_s(1,j), j = 1,...,7, s = 1,...,5, with Q_s(1,0) := q_s^1. The data on R form a row-1 partial datum iff, for every s and j:

- (i) {q_s^1, a_{s,1}, ..., a_{s,7}} is an ONB of C^8;
- (ii) j ∉ S_s(a_{s,j});
- (iii) for each fixed j, the sets S_1(a_{1,j}), ..., S_5(a_{5,j}) are pairwise disjoint;
- (iv) for each fixed j, the sets T_1(a_{1,j}), ..., T_5(a_{5,j}) are pairwise disjoint.

*Proof.* Condition (i) is the row-1 ONB part of (E1). Condition (ii) is equivalent to Q_s(0,j) ⊥ a_{s,j}, since Q_s(0,j) = w_{s,j} e_j. The remaining parts of (E1) are axis conditions.

For (E2), sort the pairs of distinct cells x, y ∈ R.

- **Same row or same column.** Then x and y lie together in row 0, row 1 or column 0, or form the pair {(0,j),(1,j)} with j >= 1. Every square's factor vanishes by (E1), so (E2) holds automatically.
- **Different row and different column, both in row 0 ∪ column 0.** Then x = (0,c), y = (r,0) with c, r >= 1. These are axis equations, which hold by assumption.
- **Remaining pairs.** These involve a cell (1,j) with j >= 1 and a cell outside row 1 and column j. Here (1,0) is excluded, being in row 1 and column 0. So the other cell is (0,c) with c != j, or (r,0) with r != 1. The cell (0,0) belongs to both families.
  - **Type I.** x = (0,c), c != j. Here <Q_s(0,c),a_{s,j}> = conj(w_{s,c}) <e_c,a_{s,j}>, which is nonzero iff c ∈ S_s(a_{s,j}). So (E2) for all s != t says no c != j lies in two of the sets S_s(a_{s,j}). Given (ii), this is (iii).
  - **Type II.** x = (r,0), r != 1. Here <q_s^r,a_{s,j}> is nonzero iff r ∈ T_s(a_{s,j}). So (E2) says no r != 1 lies in two of the T-sets. By (i), 1 ∉ T_s(a_{s,j}), so this is (iv).
  - The two descriptions of the pair {(0,0),(1,j)} agree: q_s^0 = w_{s,0} e_0 gives 0 ∈ S_s(a) iff 0 ∈ T_s(a).

This exhausts all pairs. QED

This is the row-scope content of the earlier interior candidate's single-cell criterion together with its one-row conditions, re-proved here and not imported.

## 3. Lemma 2: own-frame reuse criterion

**Lemma 2.** Fix an axis datum. Suppose for each s there is a bijection φ_s : {1,...,7} → {0,2,3,4,5,6,7} such that, for every j:

- (R1) j ∉ supp(q_s^{φ_s(j)}) for every s;
- (R2) φ_1(j), ..., φ_5(j) are pairwise distinct;
- (R3) supp(q_1^{φ_1(j)}), ..., supp(q_5^{φ_5(j)}) are pairwise disjoint.

Then a_{s,j} := q_s^{φ_s(j)} satisfies (i)-(iv) of Lemma 1. Hence Q_s(1,j) := Q_s(φ_s(j),0) defines a row-1 partial datum. (R1)-(R3) involve only the column-0 support patterns, not amplitudes or phases.

*Proof.*
- (i): {q_s^1} ∪ {q_s^{φ_s(j)} : j = 1,...,7} = {q_s^r : r ∈ [8]}, which is the column-0 ONB of square s.
- (ii) is (R1).
- (iii): S_s(q_s^r) = supp(q_s^r), so this is (R3).
- (iv): <q_s^r, q_s^{φ_s(j)}> = δ_{r,φ_s(j)} by orthonormality, so T_s(a_{s,j}) = {φ_s(j)} and (iv) is (R2).

QED

## 4. The support class D

Define the permutations π_s of [8], s = 2,...,5, with π_s(0) = 0 and:

| r | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| π_2(r) | 4 | 2 | 3 | 1 | 6 | 7 | 5 |
| π_3(r) | 5 | 3 | 2 | 7 | 1 | 6 | 4 |
| π_4(r) | 6 | 1 | 4 | 2 | 3 | 5 | 7 |
| π_5(r) | 7 | 5 | 1 | 3 | 2 | 4 | 6 |

Each row of the table lists 1,...,7 once, so each π_s is a permutation.

**Class D.** D is the set of all assignments to row 0 ∪ column 0 with the following properties.
- H2 holds with arbitrary unit-modulus w_{s,c}.
- For each s, (q_s^0, ..., q_s^7) is an ONB with q_s^0 = w_{s,0} e_0.
- supp(q_1^r) = {1,2,3}, {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3} for r = 1,...,7.
- supp(q_s^r) = {π_s(r)} for s = 2,...,5 and r = 1,...,7.

Thus in squares 2-5, q_s^r = u_{s,r} e_{π_s(r)} with arbitrary |u_{s,r}| = 1. Square 1's column 0 is ANY unitary with exactly this support pattern, so its amplitudes and phases are arbitrary subject to unitarity and the zero pattern.

**Lemma 3.** Every member of D is an axis datum (H2-H4 and all direct axis equations), and D is nonempty.

*Proof.* Row 0 and column 0 are ONBs by definition. Same-line axis pairs have vanishing factors. The off-line axis pairs are x = (0,c), y = (r,0) with r, c >= 1. In square s their factor conj(w_{s,c}) <e_c,q_s^r> is nonzero iff c ∈ supp(q_s^r). So all axis equations hold iff, for each fixed r, the five sets supp(q_1^r), {π_2(r)}, ..., {π_5(r)} are pairwise disjoint. Row by row:

| r | supp(q_1^r) | π_2(r), π_3(r), π_4(r), π_5(r) | disjoint |
|---|---|---|---|
| 1 | {1,2,3} | 4, 5, 6, 7 | yes |
| 2 | {6,7} | 2, 3, 1, 5 | yes |
| 3 | {6,7} | 3, 2, 4, 1 | yes |
| 4 | {4,5} | 1, 7, 2, 3 | yes |
| 5 | {4,5} | 6, 1, 3, 2 | yes |
| 6 | {2,3} | 7, 6, 5, 4 | yes |
| 7 | {1,2,3} | 5, 4, 7, 6 | yes |

H3 holds because π_s(1) = s+2 and supp(q_1^1) = {1,2,3}; H4 holds by the definition of D.

Nonemptiness: take w_{s,c} = 1, u_{s,r} = 1, q_s^0 = e_0, and

    q_1^1 = e_1/√2 + e_2/2 − e_3/2,   q_1^6 = (e_2+e_3)/√2,   q_1^7 = e_1/√2 − e_2/2 + e_3/2,
    q_1^2 = (e_6+e_7)/√2,   q_1^3 = (e_6−e_7)/√2,   q_1^4 = (e_4+e_5)/√2,   q_1^5 = (e_4−e_5)/√2.

The three vectors on {e_1,e_2,e_3} are orthonormal:
- each has norm 1 (1/2+1/4+1/4, 1/2+1/2, 1/2+1/4+1/4);
- <q_1^1,q_1^6> = (1/2−1/2)/√2 = 0 and <q_1^7,q_1^6> = (−1/2+1/2)/√2 = 0;
- <q_1^1,q_1^7> = 1/2 − 1/4 − 1/4 = 0.

The ± pairs are orthonormal, and vectors with disjoint supports are orthogonal. The supports are exactly those required. QED

This member is the earlier diagnostic axis datum, now re-verified from scratch. Membership in D depends only on supports.

## 5. Theorem R1: an explicit full row 1 on all of D

Define φ_s(j) by the table below (rows j = 1,...,7, columns s = 1,...,5):

| j | φ_1 | φ_2 | φ_3 | φ_4 | φ_5 |
|---|---|---|---|---|---|
| 1 | 4 | 3 | 6 | 7 | 5 |
| 2 | 2 | 4 | 0 | 5 | 6 |
| 3 | 3 | 2 | 7 | 6 | 0 |
| 4 | 7 | 5 | 4 | 0 | 2 |
| 5 | 6 | 0 | 5 | 3 | 7 |
| 6 | 5 | 6 | 3 | 2 | 4 |
| 7 | 0 | 7 | 2 | 4 | 3 |

**Theorem R1.** For EVERY member of D, setting Q_s(1,j) := Q_s(φ_s(j),0) = q_s^{φ_s(j)} for j = 1,...,7 and s = 1,...,5 gives a row-1 partial datum. Every direct QLS equation and every pairwise tensor-orthogonality equation on R holds, uniformly in all amplitudes and phases allowed in D.

*Proof.* By Lemmas 3, 2 and 1 it suffices to check (R1)-(R3) and bijectivity. These depend only on supports, and supports are constant on D.

**Bijectivity.** Reading down the columns, φ_1 = 4,2,3,7,6,5,0; φ_2 = 3,4,2,5,0,6,7; φ_3 = 6,0,7,4,5,3,2; φ_4 = 7,5,6,0,3,2,4; φ_5 = 5,6,0,2,7,4,3. Each is a list of {0,2,3,4,5,6,7} without repetition.

**(R2).** Each row of the φ table has five distinct entries: {4,3,6,7,5}, {2,4,0,5,6}, {3,2,7,6,0}, {7,5,4,0,2}, {6,0,5,3,7}, {5,6,3,2,4}, {0,7,2,4,3}.

**(R1), (R3).** Recall supp(q_1^0) = {0} and supp(q_s^r) = {π_s(r)} for s >= 2, with π_s(0) = 0. The supports supp(q_s^{φ_s(j)}) are:

| j | s=1 | s=2 | s=3 | s=4 | s=5 | j absent | disjoint |
|---|---|---|---|---|---|---|---|
| 1 | q^4: {4,5} | π_2(3) = 3 | π_3(6) = 6 | π_4(7) = 7 | π_5(5) = 2 | yes | yes |
| 2 | q^2: {6,7} | π_2(4) = 1 | 0 | π_4(5) = 3 | π_5(6) = 4 | yes | yes |
| 3 | q^3: {6,7} | π_2(2) = 2 | π_3(7) = 4 | π_4(6) = 5 | 0 | yes | yes |
| 4 | q^7: {1,2,3} | π_2(5) = 6 | π_3(4) = 7 | 0 | π_5(2) = 5 | yes | yes |
| 5 | q^6: {2,3} | 0 | π_3(5) = 1 | π_4(3) = 4 | π_5(7) = 6 | yes | yes |
| 6 | q^5: {4,5} | π_2(6) = 7 | π_3(3) = 2 | π_4(2) = 1 | π_5(4) = 3 | yes | yes |
| 7 | q^0: {0} | π_2(7) = 5 | π_3(2) = 3 | π_4(4) = 2 | π_5(3) = 1 | yes | yes |

Every π-value is read from the section-4 table. In each row the coordinate j occurs in none of the five supports, and the five supports are pairwise disjoint. QED

**Explicit form.** Row 1 of square 1 is (q_1^1 | q_1^4, q_1^2, q_1^3, q_1^7, q_1^6, q_1^5, q_1^0) at columns 0 | 1,...,7, a permutation of square 1's column-0 basis. For s >= 2, Q_s(1,j) is a unit multiple of e_{c_s(j)} with

| j | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| c_2(j) | 3 | 1 | 2 | 6 | 0 | 7 | 5 |
| c_3(j) | 6 | 0 | 4 | 7 | 1 | 2 | 3 |
| c_4(j) | 7 | 3 | 5 | 0 | 4 | 1 | 2 |
| c_5(j) | 2 | 4 | 0 | 5 | 6 | 3 | 1 |

Each row c_s lists [8] \ {s+2} once; together with Q_s(1,0) ∝ e_{s+2} it is a full ONB.

## 6. Limits and the exact remaining obligation

**Remark L1 (reuse cannot complete any column of square 1).** Assume H1-H4 for full squares. For every j >= 1, at least one of Q_1(1,j), ..., Q_1(7,j) is not a unit multiple of any q_1^m.

*Proof.* Column j is an ONB containing Q_1(0,j) = w_{1,j} e_j, so Q_1(1,j), ..., Q_1(7,j) are an ONB of e_j^⊥. Suppose each were a unit multiple of some q_1^{m_i}. Orthonormality makes the m_i distinct. Let m* be the missing index; then the span of the seven vectors is (q_1^{m*})^⊥, which equals e_j^⊥ only if q_1^{m*} is a unit multiple of e_j. But supp(q_1^0) = {0}, and by H3-H4 supp(q_1^m) has at least two elements for m >= 1. So no q_1^m is a unit multiple of e_j for j >= 1. QED

So Theorem R1 does not extend to full columns by reuse alone. Remark L1 proves nothing about extendability by other vectors.

**Exact scope of the consequence.** On every member of D, the direct restricted equations on R (with H2-H4) are jointly consistent. Therefore no argument whose premises are only these direct equations can exclude genuine P1-B3. In particular, the full-row two-frame conditions plus row ONBs give no universal contradiction. As in the parent's scope erratum to the sparsity Theorem D, this concerns only the direct-equation relaxation on R. Stronger necessary conditions on the R-variables, derived from cells outside R (rows 2-7 at columns >= 1), are not addressed. They could exclude some or all members of D. No full row-1-plus-anything extension, full configuration or extendability is claimed. Whether every admissible B3 support class (outside D) admits a row 1 is not decided; that question is not needed to refute a universal row-1 contradiction.

**Remaining obligation for genuine B3 exclusion.** It must use at least one direct equation involving a cell (i,j) with i >= 2 and j >= 1, or a non-direct consequence of such equations. By Remark L1, completing any interior column of square 1 needs vectors outside its column-0 basis.

## 7. Consistency with the earlier interior candidate (non-load-bearing)

The interior candidate's necessary row-1 conditions are satisfied by Theorem R1, as they must be. Square 1's row-1 vectors have Z at column 7 (q_1^0), A at columns 4 and 5 (q_1^7, q_1^6), B at columns 2 and 3 (q_1^2, q_1^3) and C at columns 1 and 6 (q_1^4, q_1^5): the demands Z:1, A:2, B:2, C:2. Also <q_1^7, Q_1(1,1)> = <q_1^7, q_1^4> = 0, and the q_1^7-energy in columns 2-7 is 1, attained at column 4 by q_1^7 itself. This check is not a premise. D consists of P-type (monomial) patterns only, so the unaccepted P/D1 refinement is not used either.

## 8. Import table

| item | role here | status |
|---|---|---|
| [PRIM] Ball-Simoens LF195-225 | definitions in H1 | primary source |
| [J] GBBINDING entry P1-B3 | template rows of H4 | identity metadata |
| H2-H4 normal form | hypotheses | conditioning; the U/T16 link to arbitrary nonclassical five-sets is not used |
| sparsity verdict/errata [SPV] | context; the diagnostic axis datum was accepted there as a partial witness | not a premise; Lemma 3 re-verifies it |
| interior candidate [INT], Codex review [INTC] | its row-scope criterion is re-proved as Lemma 1; its capacities appear only in section 7 | not a premise (Claude review pending per parent) |
| [TR] transition, [SC] scope freeze | authority | metadata |

## 9. Exhaustiveness ledger

| claim | status |
|---|---|
| Lemma 1 | exact (iff) for all direct equations on R |
| Lemma 2 | sufficient condition only |
| Lemma 3 | D well defined, support-only membership, nonempty |
| Theorem R1 | every member of D, all amplitudes and phases |
| row 1 on support classes outside D | not decided; no claim |
| rows 2-7, full columns, full configuration | open; Remark L1 limits reuse in square 1 |
| genuine B3 exclusion | not achieved; row 1 alone cannot achieve it in the direct-equation relaxation |
| Boolean/GB/UNSAT(H_23/H_24) | no statement |

## 10. Sources

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [INT] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-interior-two-frame/B3-INTERIOR-TWO-FRAME-CANDIDATE-v1.md`, SHA256 `3dba4891637c1b462197336f676472172fb62cbc314bd808c8fac0c2124a4a82`.
- [INTC] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-interior-codex-v1.prompt.stdout.txt`, SHA256 `13ba1d23047fefff45228c0f6dc2e109fc90386078d1bac6e3bfdeafc26389a5`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/six-slot-written-resumption-20261019-1603-v1.json`, SHA256 `ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-full-row/SCOPE-FREEZE-v1.json`, SHA256 `c0f104a9895ce093fb9f739408f2aa65e9a989766bebe6bdbe0a7be2c806bde3`.
- [SPV] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-claude-v2.prompt.note.md`, SHA256 `c475c98915af535233115ffa5d50c7881578419d521f4ca86ae1925eb32d078b`.
- [SPV] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v1.md`, SHA256 `a9748009e403b953938f56189c83a2e8040bacbb44b314cbb28929116a3e0279`.
- [SPV] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v2.md`, SHA256 `021bfe542ff870685483de66ba9bed4e927cac9bafcf38f162d02bab9b6c93ad`.
- [SPV] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-erratum-v3.md`, SHA256 `db5fffa7e3738e53ba843e937cacd028bd3221589c2ab8a317ba134cb1c8c9d2`.
- [SPV] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/moqls8-B3-sparsity-parent-verdict-v1.md`, SHA256 `644d8376cb12014d0592d70cefec9c56efb3bc24559e7c5d2cbb2900fbc78db1`.
