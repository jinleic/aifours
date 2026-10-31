# Independent full canonicalization of the actual d4 source-word partitions

**PhysicsResearch96h-2 / physics-1.** Actual native clock before writing: Wed Oct 28 18:20:07 PDT 2026. This addresses the source-span/orbit-partition dependency of the exact d4 certificate with a second complete algorithm, rather than adding another operator reformulation. The all-orbit functional identity, saved-multiplier positivity, original physical bridge and runtime trust remain separately required. This is not parent adoption, formal/Lean, human/model-family review or a novelty claim.

## 1. Exact group and what must be checked

For family f∈{31,22,13}, the actual literal four-replica source letter words are `aaab`, `aabb`, and `bbba`. Let H_f be the subgroup of S4 stabilizing every letter position. A source permutation word is `(p1,p2,p3,pQ)∈S4^4`; the first three permutations are the physical sites and the fourth is the auxiliary qubit.

The actual moment tuple is invariant under **independent left and right** simultaneous actions of H_f, permutations of the three physical site factors, and simultaneous transpose/inversion. The inversion is relevant because `V_p^T=V_(p^−1)` and the actual complex-conjugation-averaged moments are real symmetric. Site permutations commute with both left/right actions and inversion. Inversion conjugates a two-sided action `(g,h)` into `(h^−1,g^−1)`, still in H_f×H_f. Thus the full group orbit of w consists exactly of

`(g p_(sigma(1))^epsilon h, g p_(sigma(2))^epsilon h,
  g p_(sigma(3))^epsilon h, g pQ^epsilon h)`

for all g,h∈H_f, sigma∈S3 and epsilon∈{+1,−1}. This covers the actual physical symmetries, not an assumption that the word operators are independent. For 31/13, `|H_f|=6`; for 22, `|H_f|=4`.

For the finite lexical permutation encoding used by the exact global identity checker define

`K_f(w)=min_(g,h,epsilon) (sort(g p1^epsilon h,g p2^epsilon h,g p3^epsilon h), g pQ^epsilon h)`.

Sorting is exactly minimization over the six site permutations. Each candidate is a genuine orbit transform; conversely every orbit transform is represented. Therefore K_f(w)=K_f(w') **iff** w,w' are in the same source-word orbit. This proof does not infer global rank or positivity merely from a count.

## 2. Actually run second partition algorithm

`frontier-20261028-d4-canonical-orbit-audit.py`, SHA256 `3688674985ed26f121a9bba51f3e8860b943feaddc3fa516b4e8e8a3f6a3a663`, enumerates all left/right stabilizer pairs and both inversion possibilities for **every one of the 24⁴=331776 words in each family**. It minimizes directly as above; it does **not** construct a union-find graph or execute/import the author's code.

It then independently calls the already pinned owner exact-global helper `frontier-20261028-independent-d4-global-identity-check.py`, SHA256 `b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d`, for the separate union-find label partition, and compares canonical keys and labels **in both directions on every word**, permitting arbitrary label renaming.

Actual command: `python3 frontier-20261028-d4-canonical-orbit-audit.py`. Receipt `frontier-20261028-d4-canonical-orbit-audit-results.json`, SHA256 `cc528c41e387371dd64b5e9e92263df6f977519fa1aef114e3a3ad21dc55e94b`; actual **PASS, 8.979 seconds**:

| Family | All words | H size | Left/right pairs | Canonical orbits | Union-find orbits | Bidirectional disagreement |
|---|---:|---:|---:|---:|---:|---:|
| 31 | 331776 | 6 | 36 | 1142 | 1142 | 0 |
| 22 | 331776 | 4 | 16 | 2391 | 2391 | 0 |
| 13 | 331776 | 6 | 36 | 1142 | 1142 | 0 |

The 31 and 13 stabilizers have the SAME repeated-letter positions, so the direct canonical keys were computed once for that common subgroup and checked independently against **both** family label lists; 22 used its different subgroup. This is why the receipt says two unique canonical partitions evaluated, not three separate calculations. In-memory reassignment of one source word to a different orbit was detected for **each** family; it is a partition-comparator fault control, not a physical counterexample.

## 3. Consequence and limitations

Combined with the separate earlier comparison of the owner union-find labels against the author's labels (full partition comparison, not just counts), this adds a **genuinely different direct canonicalization algorithm** for the full 4675 source-orbit partition. The source-family literal strings, mathematical group action, common Python runtime, and owner reference labels remain shared interfaces; this is not an independent developer/model-family review or a formal theorem kernel.

The physical original-C lift, all 1126 single-row and 111 coupled physical Gram blocks, ordered marginal/Stiefel equalities, full objective and exact corrected-data identity/PSD remain in `frontier-20261028-d4-consolidated-operator-certificate-proof-v1.md`, SHA256 `a6fb579592ffacd71cb0d8c115e5aea20209fc07395304be9b79651dbf1f646e`, and its cited full-source/CRT/commutant artifacts. This check does not itself evaluate their coefficients, prove positivity, validate the larger all-d public theorem, confer operational or novelty claims, or adopt the source. Historical held material is not a premise.
