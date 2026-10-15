# Immutable acceptance criteria

1. Original finite-alphabet, left-divisible semifilter definition is used; complement of symmetric difference, not union closure. Include ε and empty alphabet. No properness assumption is smuggled in.
2. All-parameter written proof fully answers both book Question2 and Question3, separately scoped, with non-tautological cross-family finite-expression criterion.
3. Normal form has complete word-length elimination and parity semantics; no circular recognizable-series invocation. Every finite-span/quotient step is justified.
4. Filter case is justified for arbitrary infinite complements; examples and the suffix-closed-U parametrization actually satisfy all source axioms.
5. Formal.lean proves at least one genuinely load-bearing all-parameter mechanism, with no equivalent-to-goal hypothesis, no sorry/admit/new axiom/native_decide/ofReduceBool/unsafe/opaque or external computation. Prefer full Q2/Q3 finite-span proof if feasible. Partial formalization is explicitly labeled and is not confused with a fully Lean-certified answer.
6. claims.json records theorem roots only, exact intended statements/assumptions and full/partial scope, no novelty overclaim. #print and #print axioms cover every root.
7. python3 verify.py passes: final Lean compilation succeeds; the immutable false-proposition control is rejected for mathematical falsity; no prohibited formal escape hatches.
8. No baseline/global/shared/outside mutation. Preserve failed attempts and journals. No extra run or independent CLI reviewer launch.
9. RESULT.md records precise written proof status, formal coverage, existing theorem comparison and inaccessible-source novelty blockers. done:true requires both exact written questions proved or refuted and the substantive formal component checked. The entire multi-question chapter and discovery priority are not claimed.
