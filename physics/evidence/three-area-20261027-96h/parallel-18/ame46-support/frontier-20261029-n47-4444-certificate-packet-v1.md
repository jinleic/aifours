# Candidate support-47 exclusion of residual alphabet (4,4,4,4): thirteen checked CNF certificates

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Thu Oct 29 09:43:36 PDT 2026`; not an exact completion time. **WRITTEN reduction plus exact pinned-CNF RUP certificates**, not independently reviewed, adopted, formally verified, or novelty-cleared. A checked SAT certificate establishes its exact formula only; the mathematical reduction, encoder soundness and checker correctness remain independent review obligations.

## 1. Exact scope

Assume a normalized complex AME(4,6) state in a product basis has `N=47`, exactly `t=27` modulus-1/6 coefficients P, and nonmaximal support E with `|E|=20`. Assume every E coordinate alphabet has size4. The candidate claim is that this branch is impossible.

This packet does **not** assert N=47 is globally impossible. The `(3,4,4,4)` residual profile remains open here. The reductions from N=47 to this t value and those two profiles are in the separately unreviewed author packets `frontier-20261029-n47-residual-reduction-v1.md`, SHA-256 `9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`, and `frontier-20261029-n47-two-alphabet-profiles-v1.md`, SHA-256 `d18eade8bd13a8dda3cee88c20daff812834b3a54d8eef26eb6345d2fe10da0d`. They are not silently adopted. The branch-specific argument below imports neither no-OLS(6) nor no-Hamming-one; it is a support-necessity argument from actual complex unitarity.

## 2. Shared pair partition and local heavy types

For every 2|2 cut, `U=6ψ` is unitary. Modulus-1/6 entries are singleton rows and columns in every cut; deleting the27 P entries leaves a9×9 unitary V with every row and column degree at least2. At support20 it has excess2 and, by the two-excess argument re-derived below, is one eight-entry3×3 block plus three full2×2 blocks. Thus in each of the six coordinate-pair systems there are exactly9 E-carried values: seven have2 E extensions and two have3. Call the latter **heavy**. The other27 pair values are P singletons.

For a residual symbol a at i, the number of E partner values at any j≠i is `d_i(a)=6−m_i(a)`, where m_i(a) is the number of P words using a; this follows from the full pair partition and P-pair injectivity. Hence d_i(a) is j-independent. It is at least2, since d=1 at all other coordinates would make E_a a singleton. Four d values sum to9, so after local relabeling every party has

`d=(2,2,2,3)`.

Let h_ij(a) be the number of heavy (i,j) values using a. Counting E_a gives `|E_a|=2d_i(a)+h_ij(a)`, so h_ij(a) is also j-independent. Write it h_i(a); it is nonnegative and sums to2. It is either two ones (**split**) or one two (**merged**).

Two parties cannot both be merged: their two distinct heavy pair values would both be the same pair of distinguished symbols. Thus at most one party is merged. Relabeling only within each party's degree classes gives four types:

| type | h at labels0,1,2,3 | fiber sizes `2d+h` |
|---|---|---|
| S0 | (1,0,0,1) | (5,4,4,7) |
| S1 | (1,1,0,0) | (5,5,4,6) |
| M0 | (0,0,0,2) | (4,4,4,8) |
| M1 | (2,0,0,0) | (6,4,4,6) |

S0 means the degree-3 symbol is heavy; S1 means two of the three degree-2 symbols are heavy. M0/M1 distinguish whether the merged symbol has degree3 or2. No orientation of a heavy matching between two parties is frozen away; each formula allows **all** heavy pair placements with these degrees.

Party permutations leave thirteen type multisets: five all-split cases with 0,…,4 S0 parties, and eight one-merged cases (M0 or M1, with 0,…,3 S0 parties). This is the complete normal form for the stated branch.

### Two-excess source argument

A complex unitary has no two rows or columns sharing exactly one nonzero position. A support component is square. A zero-excess component is a full2×2 block. Excess1 is impossible: its unique degree3 row would require degree2 neighbours using one common pair of its three columns, leaving its third column degree1. Therefore an excess2 unitary has one positive component and all others2×2. In that component, degree2 rows have disjoint two-column supports (equal pairs would split off a2×2 block); if s such rows and b higher rows exist, `s≤b≤2`, so the component has size at most4. Size4 would have two degree3 rows meeting the two disjoint covering pairs in even numbers, impossible. The component is therefore3×3 with8 entries. This supplies the multiplicity profile used above without an external import.

## 3. Exact support formula for each type multiset

There are256 primary Boolean variables `e_x`, one for each `x∈{0,1,2,3}^4` in lexicographic order. For a fixed type tuple, the formula imposes:

1. Every local symbol a at party i occurs in exactly `2d(a)+h_i(a)` E positions. Each local sum is20, hence |E|=20.
2. For each of six party pairs and every value (a,b), Boolean variables y and h encode exact multiplicities:
   - `(count,y,h)=(0,false,false)`, `(2,true,false)` or `(3,true,true)` only.
   - For each symbol a at either endpoint, the y row/column count is d(a), and the h count is its prescribed h_i(a).
3. In each cut, distinct rows/columns cannot share exactly one nonzero column/row. For each pair of lines and each shared position, an auxiliary variable for every other position may be true only when both corresponding E entries are true, and the shared-position clause requires at least one such other witness.

**Necessary-direction proof.** Any actual residual E satisfying §2 gives primary e values. Its actual nonzero/heavy pair values give y,h and satisfy item2. All exact cardinalities admit the usual sequential-prefix-count auxiliary extension. For item3 choose every witness variable equal to the conjunction of its two E entries; actual complex orthogonality ensures that a shared nonzero position has another shared position. Thus an actual tensor in this branch would extend to a satisfying assignment of one of the thirteen formulas. No phase or coefficient value is assumed by the encoding.

Cardinality encoding is the standard Sinz sequential at-most counter. An exact-k gate is at-most-k on x and at-most-(n−k) on ¬x. The pair-cell relation uses: y iff any entry, y⇒at least2, at most3 entries, h⇒at least3, and any triple of entries⇒h. These are exactly the three allowed `(count,y,h)` patterns. All generated clauses can be reconstructed from the pinned source.

## 4. Exact-CNF certificates, not bare solver statuses

Encoder `frontier-20261029-n47-heavy-support-cnf-v1.py`, SHA-256 `844ea38848e6678e806113f91ed1a6ca2f9541eae5d009b0b7e833c516a4ecf9`, generated all13 instances. CaDiCaL3.0.1 with `--plain --lrat --no-binary` produced textual LRAT proofs; each instance completed with rc20 and `s UNSATISFIABLE` observed. All13 proofs were then checked **through EOF** by the separately authored checker described in §5.

The binding manifest `sat-20261029/n47-heavy-certificate-manifest-v1.json`, SHA-256 `447f0a9e6e6b0d4edf75eae534a94fedf32bff3968d174998fb944f41e71332e`, lists every case, CNF, proof and checker receipt with exact hashes/byte lengths. The13 CNFs total74,455,862 bytes; proofs total49,489,892 bytes. These on-disk CNF/proof files were intentionally retained as the finite evidence, not streamed or deleted.

Case0's example pin: CNF SHA-256 `f9627c1f54198bf3930b580f27ab82a3813f66f6b838c0cab478353a847d2c57`, proof SHA-256 `60f2df54bd3cad38661b10f90c56cab7af448566cd1cc1a4633351b4ca0fa3e9`, checker receipt SHA-256 `f182acd305e8fb38d03375c7ea8682e5ba927f8a73c85617dad6cab7f798cab9`; the receipt verifies67,862 added clauses and an empty clause at ID312742. Cases1–12 also bind native solver logs, binary hashes before/after and input hashes before/after in `sat-20261029/n47-heavy-certificate-batch-v1.json`, SHA-256 `0b50e84f376e433696247b7bb99b9709cf430ab206854a2e846669e05dd7404b`. Case0's solver log exists in the tool transcript rather than that batch; its mathematical certificate is the complete independently replayed CNF/proof pair, not a reconstructed log.

Every proof certifies UNSAT of **its exact encoded formula**. Mathematical branch exclusion additionally requires the §2 type-coverage and §3 necessary-direction proofs and correctness of the encoder/checker. No main-agent replay or independent-model review is inferred from author execution.

## 5. RUP checker and controls

Checker `frontier-20261029-lrat-rup-check-v2.py`, SHA-256 `d04eb821104b12bfddfb3d6e9a6f7a03b4f97ae65247959de6eddaa39ab99366`, imports no SAT solver. It strictly parses the complete DIMACS header and clause count and all proof lines. For each addition it negates the new clause and verifies positive-hint unit propagation until conflict against existing undeleted clauses. Unsupported negative/RAT hints are rejected; they are never skipped. Deletion weakens the current formula. A verified derived empty clause is mandatory, and parsing continues through EOF. The receipt hashes the complete input bytes read, not just a prefix. This is not the upstream `lrat-check` program.

**Checker correction preserved.** v1 conservatively rejected the first real proof because it incorrectly required strictly increasing IDs even for deletion timestamps. Standard LRAT deletion records may use the most recent addition ID. v2 allows that while addition IDs remain strictly increasing. All v1 bytes and its failed return remain; no prior pass is invented.

`frontier-20261029-lrat-rup-controls-v2.py`, source SHA-256 `2d488a6cc904158cdfe5b5073c3a4d9730786a04c4a30454e141813e7e4fe55f`, receipt `sat-20261029/lrat-rup-controls-v2.json`, SHA-256 `3112b1ec4952d079b9516633f642f52f318ed14e246c1d56d433bb3d992137c5`, checks a valid small proof, a repeated-ID deletion positive, and nine intended-reason rejections: bogus empty, SAT-formula false proof, truncated CNF, truncated proof, wrong formula, negative hint, missing/deleted hint, out-of-range literal and non-increasing addition ID.

Encoder primitive control `frontier-20261029-n47-cnf-gadget-controls-v1.py`, source SHA-256 `05f7d2cac1a488a744b65e497aa95c331fa48c107b2186db2e5bc2741bf559f2`, receipt SHA-256 `5990c316050a9944a731e884cf2fe98d9f7e2f371985727631565f3046750215`, exhausts every at-most counter for n≤8, every k and both input polarities:4,606 valid input assignments have a constructed satisfying auxiliary extension, and3,586 invalid ones conflict by unit propagation. It checks all68 pair-cell count/y/h truth cases and constructs a20-word relaxed support with correct fibers and exact multiplicities on the opposite AB and CD systems. That relaxed positive is **not** a full six-marginal support.

A no-unique-overlap-removed version of case0 was itself UNSAT, and is **not a positive control**. An independently coded Z3 integer sum-of-If formulation without overlap constraints agrees for case0 (uncertified); the full independent Z3 formulation also reports13 UNSAT. These solver diagnostics are supplementary; they do not replace the LRAT replay or the normal-form review.

## 6. Remaining research and review surface

If independently accepted, this would exclude only `(N,t,r)=(47,27,(4,4,4,4))`. The residual-alphabet `(3,4,4,4)` case remains unresolved. A global support bound48 would require that case, the N=47 reductions, and any earlier N=45/46 compositions to be separately reviewed; none is adopted here.

Review should attack: d/h j-independence from the P/E pair partition; the two-excess unitary proof; at most one merged party; all thirteen relabeling cases with all heavy-matching orientations retained; the implication from an actual tensor to a CNF assignment; the sequential counter and pair-cell relation; every proof binding and checker semantics; and replay all13 certificates with an independently written proof checker or a disjoint exhaustive method.
