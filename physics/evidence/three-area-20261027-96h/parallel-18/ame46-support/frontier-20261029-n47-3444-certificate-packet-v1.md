# Candidate support-47 exclusion of residual alphabet (3,4,4,4): fifty-six checked CNF certificates

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Thu Oct 29 09:50:23 PDT 2026`; not an exact completion time. **WRITTEN reduction plus exact pinned-CNF RUP certificates**, not independently reviewed, adopted, formally verified, or novelty-cleared. A checked proof certifies an exact encoded formula; the mathematical normal form, encoder soundness and checker correctness require independent review.

## 1. Exact scope and boundary

Assume a normalized complex AME(4,6) state in a product basis has `N=47`, exactly `t=27` modulus-1/6 coefficients P, and other support E of size20. Assume the E-alphabet sizes are `(3,4,4,4)` at parties A,B,C,D respectively. The candidate claim is that this branch is impossible.

The branch-specific reasoning below uses no no-OLS(6) theorem or no-Hamming-one import. The separate, unreviewed N=47→t=27 reduction and the two residual-profile reduction are in `frontier-20261029-n47-residual-reduction-v1.md`, SHA-256 `9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`, and `frontier-20261029-n47-two-alphabet-profiles-v1.md`, SHA-256 `d18eade8bd13a8dda3cee88c20daff812834b3a54d8eef26eb6345d2fe10da0d`. They are not adopted by this packet. The separate `(4,4,4,4)` certificate packet has SHA-256 `875028cb394cea863097110d4cca9620ff6a137e0ede4fd080da51c58d7415f2`. No global support lower bound48 is claimed or adopted here.

## 2. Common P/E partition, degree and heavy excess

In every 2|2 cut, `U=6ψ` is unitary. Each modulus-1/6 coefficient is isolated in its pair row and column; deleting the27 P entries leaves a9×9 unitary with20 nonzeros and every line degree at least2. The complex-unitary two-excess classification gives one eight-entry3×3 block and three full2×2 blocks. The proof is reproduced in §2 of the `(4,4,4,4)` packet and uses only row/column orthogonality and norm, not SAT. Consequently every coordinate-pair projection of E has9 values: two heavy ones with multiplicity3 and seven others with multiplicity2. P occupies each of the other27 pair values exactly once.

For a residual symbol a at party i, let m_i(a) count P words using a. P pair injectivity and the full pair partition give `d_i(a)=6−m_i(a)=|π_j(E_a)|` for **every** j≠i. Thus d_i(a) is j-independent; d≥2 since d=1 at all other coordinates would force a singleton E fiber. The degrees at every party sum to9 and are bounded above by each partner's residual-alphabet size.

For any other party j, let h_ij(a) count heavy (i,j) values using a. Counting E_a gives `|E_a|=2d_i(a)+h_ij(a)`, so h_ij(a) is likewise j-independent. Write it h_i(a); its sum over symbols at i is2. Every party is either **split**, with two h=1 symbols, or **merged**, with one h=2 symbol. At most one party is merged, since two merged parties would make their two distinct heavy pair values coincide at one pair of symbols.

## 3. Fifty-six complete type normal forms

At each size4 party B,C,D the degrees must be `(2,2,2,3)`. Relabel within the degree classes as in the other branch:

- S0: `h=(1,0,0,1)`;
- S1: `h=(1,1,0,0)`;
- M0: `h=(0,0,0,2)`;
- M1: `h=(2,0,0,0)`.

At the size3 party A, d≥2, Σd=9 and d≤4 leave two degree multisets: **U=(2,3,4)** and **V=(3,3,3)**. Since U degrees are distinct, all three split pairs and all three merged symbols must be kept. V degrees are equal, so one split and one merged representative suffice. The eight A types are:

| A type | d | h | fiber sizes `2d+h` |
|---|---|---|---|
| U_S01 | (2,3,4) | (1,1,0) | (5,7,8) |
| U_S02 | (2,3,4) | (1,0,1) | (5,6,9) |
| U_S12 | (2,3,4) | (0,1,1) | (4,7,9) |
| V_S | (3,3,3) | (1,1,0) | (7,7,6) |
| U_M0 | (2,3,4) | (2,0,0) | (6,6,8) |
| U_M1 | (2,3,4) | (0,2,0) | (4,8,8) |
| U_M2 | (2,3,4) | (0,0,2) | (4,6,10) |
| V_M | (3,3,3) | (2,0,0) | (8,6,6) |

For each of the four A-split types:

- with B,C,D all split there are four multisets (0,…,3 S0 parties);
- with one merged partner, put it at B by permuting B,C,D: two merged types times three split multisets on C,D, giving six cases.

That gives `4·(4+6)=40` cases. For each of the four A-merged types, all B,C,D are split, giving four multisets: `4·4=16` more. Total **56**. Every possible heavy matching orientation between parties is retained as variables in every formula; it is not normalized away.

## 4. Necessary direction of the CNF encoding

Primary variables are the192 `e_x` for `x∈{0,1,2}×{0,1,2,3}³` in lexicographic order. A fixed type case imposes:

1. Exact local fiber sizes `2d_i(a)+h_i(a)`, which sum to20.
2. For each party pair and pair value, multiplicity exactly0,2 or3. Auxiliary y,h have the exact relation `(count,y,h)=(0,0,0),(2,1,0),(3,1,1)`. Every local y-degree is d_i(a) and every local h-degree is h_i(a), at **both** ends of every pair system.
3. No two rows or columns in any 2|2 cut may share exactly one nonzero position. For each line pair, witness variables imply the conjunction of the two entries at another position. Two present entries at one shared position require one other shared witness.

Any actual tensor in the stated branch produces primary e values and actual nonzero/heavy pair values y,h satisfying items1–2. Sequential-prefix-count auxiliaries extend all valid exact cardinalities. For item3 choose each witness equal to its actual conjunction; complex-unitary orthogonality ensures the clause is satisfied. Thus every actual tensor extends to a SAT assignment in one of the56 cases. This necessary direction is essential: a proof of a too-strong formula would not imply a mathematical exclusion.

Encoder `frontier-20261029-n47-3444-support-cnf-v1.py`, SHA-256 `0467681eb970416d266271c3c5a789001bc58e1cd50c055340fa3a78dfe7c13e`, imports **only** the frozen standard-library `Encoder` cardinality primitive from neighboring `frontier-20261029-n47-heavy-support-cnf-v1.py`, SHA-256 `844ea38848e6678e806113f91ed1a6ca2f9541eae5d009b0b7e833c516a4ecf9`. Both files must be in the review snapshot. No Z3 dependency is used to generate or check these CNFs.

## 5. Complete certificate coverage and controls

All56 formulas were solved with CaDiCaL3.0.1, `--plain --lrat --no-binary`, each with its own60-second bound. Every run terminated with rc20 and the sole status line `s UNSATISFIABLE`. Each full textual LRAT file was then replayed through EOF by a separately authored positive-hint RUP verifier, deriving a verified empty clause.

Manifest `sat-20261029/n47-3444-certificate-manifest-v1.json`, SHA-256 `d4ce47c7b1ffc3c28c9431e8cd566efc69bb019fb5f31461b0cd23bf7ee930dc`, binds all56 case types, CNF/proof bytes and hashes, and checker receipts. Total retained evidence is187,940,876 CNF bytes and96,936,145 proof bytes. The batch receipt `sat-20261029/n47-3444-certificate-batch-v1.json`, SHA-256 `8b13b3e03d62cb1bac93f27f7faefb4eec3df871d2776c03cb610e9f5e883179`, additionally binds solver logs, the imported encoder hash, input/binary hashes before and after, solver status and actual monotonic runtimes.

RUP verifier `frontier-20261029-lrat-rup-check-v2.py`, SHA-256 `d04eb821104b12bfddfb3d6e9a6f7a03b4f97ae65247959de6eddaa39ab99366`, imports no SAT solver. It reads complete CNF/proof bytes and hashes them, strictly checks the DIMACS header/clause count, validates every addition by positive-hint unit propagation under the negated candidate clause, rejects negative/RAT hints rather than skipping them, handles deletion as weakening, requires a derived empty clause and parses every line through EOF. It is not the upstream `lrat-check` program. Its v1 conservative rejection of standard repeated deletion timestamps and the v2 correction are preserved and described fully in the other branch's packet.

Exact controls shared with the other branch:

- `sat-20261029/lrat-rup-controls-v2.json`, SHA-256 `3112b1ec4952d079b9516633f642f52f318ed14e246c1d56d433bb3d992137c5`: valid small proof and repeated-deletion positive; nine intended-reason rejections including bogus empty, SAT-formula false proof, truncated CNF/proof, wrong formula, unsupported hint and deleted hint.
- `sat-20261029/n47-cnf-gadget-controls-v1.json`, SHA-256 `5990c316050a9944a731e884cf2fe98d9f7e2f371985727631565f3046750215`: every small at-most counter with n≤8, every k and both polarities;4,606 valid input assignments with satisfying auxiliary extensions,3,586 invalid inputs conflicting by unit propagation, and all68 pair-cell truth-relation cases. A20-word AB/CD-only relaxed positive is not presented as a full six-marginal support.

An independently coded Z3 pseudo-Boolean formulation (source SHA-256 `d75377567140e8de2fe58325a9c8d21c0743dab629a14f84310ac4ecce2e3ad3`, output SHA-256 `a0f4fed56df5d722e2e3ebd60d2b9d8c5bfe6bdcd70a25552f4814ca95d41041`) also reports56 UNSAT statuses. These are supplementary diagnostics, not proof certificates.

## 6. What has and has not been established

The author-run verifier establishes exact UNSAT proof coverage of the56 serialized CNFs, at that checker's trust boundary. Mathematical exclusion of the stated AME branch requires independent reconstruction of §§2–4, the encoder's necessary direction, the cardinality primitive and proof-checker correctness. No independent model-family review, human proof, Lean/kernel proof, novelty finding or parent adoption is claimed.

Together with the separate `(4,4,4,4)` branch candidate, both residual profiles in the unreviewed N=47 reduction would be excluded. This does not itself adopt the N=47 reduction or any global lower bound. All earlier N=45 and N=46 compositions remain separate parent decisions.
