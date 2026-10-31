# Full n=2/n=4 commutator-witness semantic domains

**PhysicsResearch96h-2 / physics-1.** Actual native observation: Wed Oct 28 20:15:15 PDT 2026. This is an exact source-witness domain check, not a new modular-rank computation, physical q3 theorem, parent/f62 adoption, or human/model-family/formal review.

## 1. Actual source row and column domains

For each n∈{2,4}, the local four-replica commutant proof indexes its same-weight unknowns by `(x,y)` with x,y∈{0,…,n−1}⁴ and `wt(x)=wt(y)`. A commutator row for `(i,j,x,y)` is valid only if i,j are distinct in-range integer generators, y contains j, and `wt(x)=wt(y)+e_i−e_j`. Every pivot column must be an integer index in the actual same-weight coordinate universe.

`frontier-20261028-d4-commutator-witness-domain-check.py`, SHA256 `2bf1e5b5319b3e6fa9de59aa9d8667beeff402f261d7bff05bf152976f855b97`, reads the exact pinned witness SHA256 `1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4`. It independently enumerates all n⁴ basis words and sums squared weight-block sizes, then checks **every** supplied row and pivot column against those literal domains, including exact integer types and uniqueness. Actual `python3` result `frontier-20261028-d4-commutator-witness-domain-check-results.json`, SHA256 `e3ffc40d4d2b0e233bc85c6eef028127bb5ac8d2751a5d7501441d99f8d4bc05`, is **PASS**:

| n | Same-weight unknowns | Distinct valid selected rows | Distinct valid pivot columns |
|---|---:|---:|---:|
| 2 | 70 | 56 | 56 |
| 4 | 2716 | 2692 | 2692 |

Seven deliberate in-memory metadata faults per n were each rejected: out-of-range and duplicate pivots, equal generator indices, out-of-range word, wrong weight, duplicate row, and noninteger pivot. They are checker guards, not original physical input states or counterexamples; pinned files are unchanged.

## 2. Exact relationship to the previous rank proof

The existing standalone rank verifier already reconstructs and validates each selected commutator row's generator/range/weight conditions and computes the actual full-rank selected minors modulo prime65521. Its full rank also rules out a pivot column that receives no valid source coordinate. This new audit adds explicit **strict integer/range/uniqueness** checks on the actual persisted row/column labels; it does not imply that the old rank verifier accepted an invalid input or that its actual rank result is false.

It reads, but does **not recompute**, the pinned standalone rank receipt `frontier-20261028-commutant-standalone-verifier-results.json`, SHA256 `941c109c36a1536bcf2abf1c6c25ca7e4417104ede684a21221fb5e0582459b6`, which reports ranks56 and2692 and independently checked all112 /20640 commutator rows against all24 permutation columns. The separate n2 permutation-minor row-domain/determinant guard audit is `frontier-20261028-d4-n2-permutation-minor-domain-audit-v1.md`, SHA256 `30d6fa839420bca24962cfcefbdacaeed7c8907663d1b9e05a62da431a1158e4`; the n4 permutation lower bound has its own exact witness.

Together with the written unitary-derivative/tensor-product invariant proof, these support the two **actual** d4-source local commutant spans, conditional on program/runtime correctness. The original physical lift/Gram/equality, all-orbit identity and corrected-matrix PSD are separate. This is not a general all-n theorem, physical operational claim, novelty, or formal/independent-family review. Prior timing gaps remain disclosed in the 19:04 self-stop record; no old held material is used as a premise.
