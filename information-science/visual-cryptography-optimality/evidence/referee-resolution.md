# Independent-referee disposition

Date: 2026-10-14 (PT). Two separate read-only Codex sessions used the configured **gpt-6.1-sol**, reasoning effort **max**, Codex CLI0.162.1. Prompts and original replies are preserved unchanged. Both delegates completed successfully; the main process exited0. No further delegation, edits, or experiments were requested from them. This is independent-model advice plus the author's checked resolutions, not a proof-assistant certificate or novelty clearance.

## Main review: correct-with-fixes

Original: [codex-referee.md](codex-referee.md). The referee accepted the six central mathematical claims and found no substantive counterexample in the specified model. Every numbered point is addressed:

| Finding | Checked resolution |
|---|---|
|1. Maximum contrast transfers; finite-expansion optima do not automatically transfer|Accepted. README and model.md distinguish basis and collection rows. Only LP/integrality bounds and the separate necessary-black-matrix certificate transfer. The five remaining collection cases are intervals, not solved. Divisibility uses the reduced optimum alpha denominator only at actual optimum attainment; the denominator of an arbitrary LP witness is never treated as a universal expansion divisor.|
|2. Strong versus weak, and all-qualified reconstruction|Accepted. Both solver and verifier impose the entire upward closure. Directly checked the referee's n2,m1 counterexample: the minimal qualified set has gap1 while its qualified superset has gap0. Read Ateniese1996 Example5.6, confirming that strong completion and basis restriction need not preserve an example's optimal m. No weak-to-strong optimization reduction is asserted.|
|3. Exact Mobius formula needs complete integer obligations|Accepted. The verifier separately excludes m below the claimed minimum, gap one greater at fixed m, and shorter lengths at global alpha. All18 nontrivial queries returned UNSAT; the other726 obligations have exact LP/integer bounds. `sum If(d>0,d,0)` is exactly the positive-part length, equivalent to the proposed auxiliary z formulation. Added proof that length<=M forces every moment into[-M,M], so there is no arbitrary hidden cutoff. The at-alpha query uses the **actual** length m on the right-hand side of q f(Q)>=p m, not an unpadded core length.|
|4. Separate trade-off functions and product collections|Corrected exposition. model.md now distinguishes G_basis and G_collection. Collection superadditivity explicitly uses Cartesian-product multisets with product multiplicities and the same access structure in both components, not arbitrary pairing. Only absolute integer gap is monotone under padding; relative contrast is not claimed monotone.|
|5. Security requires all forbidden moments; aggregate counts are basis-specific|Accepted. Generator uses all forbidden moments; verifier checks every projected pattern. Reproduced the referee's n3,m2 example with f({1,2})=0 but f({1})=-1 and f({2})=1. Added an explicit nonempty/common-expansion collection assumption. Uniform permutations are the step turning basis histogram equality into equality of full projected-matrix distributions.|
|6. “Bounded LP” requires a>=0|Corrected the written LP. The implementation already imposed nonnegativity on all variables; no computed result changed. Added compactness and positive-feasibility arguments: f=0 on forbidden sets, f=1 on qualified sets, integer inverse, positive/negative parts, then normalization. Exact primal/dual feasibility and objective agreement were already checked.|
|7. Contrast convention is an interpretation; 2-out-of-4 is old|Accepted. README explicitly interprets the book's “maximum contrast” as maximum relative difference g/m, since unnormalized g is unbounded. The 2-out-of-4 trade-off is labelled Reproduction/classical, not new or a published-conjecture counterexample. Primary1999 theorem comparison and the exact local certificates agree.|

## Narrow collection-lemma review: sound, matching size must be explicit

Original: [codex-collection.md](codex-collection.md). The referee accepted the pointwise necessary condition for each black encoding, its exact-UNSAT implication, and maximum-contrast basis/collection equivalence. Resolutions:

1. **All black column types and all qualified/forbidden incidences:** `collection_bounds.py` uses all2^n types, all qualified Q, and every forbidden F subset Q. It relaxes the original problem only by omitting other constraints; therefore UNSAT is a legitimate universal lower bound. SAT is explicitly not a VCS.
2. **Matching witness size:** the lower bound is q*ceil(L/q). Equality is reported only when the independently checked optimum-alpha witness has **exactly** that expansion. `summarize.py` compares the two numbers directly. model.md now states that requirement explicitly. This holds for243/248 rows; the five exceptions remain unresolved.
3. **Actual integer gap and expected-contrast pitfall:** alpha means actual guaranteed worst-case gap divided by m. Reproduced the m1 collection C0={00,11}, C1={01,10}: singleton privacy, expected gap1/2, but deterministic gap0. This is not admitted as a deterministic scheme; its denominator behavior cannot be imported.
4. **No full original solution inferred:** finite tables and formulations remain partial. No efficient-algorithm requirement, hardness theorem, or novelty claim is invented. The full general access-structure question remains unclosed here.

## Independently exercised counterexamples

Command:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv/bin/python work/review_controls.py
```

Output: [referee-controls.json](referee-controls.json), **four passed controls**: minimal-qualified-only failure; maximal-forbidden-zero-moment failure; expected-versus-guaranteed gap; and an m3 padding of the (2,2) scheme showing that optimum denominator2 need not divide a suboptimal scheme's expansion.

No numerical table was changed by the reviews. The main fixes were rigorous scope and proof exposition; the existing exact computations already obeyed the corrected conditions. The additional universal-collection lemma received its own bounded review rather than being assumed covered by the earlier main prompt.
