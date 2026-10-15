# Exact acceptance

The frozen goal is Olson's ORDERED EGZ conjecture for all finite groups, not the reorderable theorem.

1. A positive resolution must prove for every finite group G, n=|G|, every list xs of length 2n-1 contains an ordered sublist ys of length n and product 1. No group-class restriction or substantive additional hypothesis is allowed. Formal.lean must prove theorem Olson.ordered_egz with that exact statement; verify.py appends a type check against it.
2. A negative resolution must exhibit a complete finite group multiplication table with identity, inverses and associativity, and a list of length exactly 2|G|-1. Exhaustively check all increasing-index |G|-subsets and prove all products nonidentity. certificate.json schema: {"table": [[integer,...],...], "identity": integer, "sequence": [integer,...]}. Formal.lean must prove theorem Olson.ordered_egz_false negating the same all-group statement, including group cardinality and list-length semantics. Independent raw-subset and DP checks must agree. A one-short extremal word is not a refutation.
3. A written proof.md must faithfully explain the actual argument. claims.json states route as "proof" or "counterexample", full_goal_solved true only if justified, and separates partial/reproduced results. Kernel and script success do not establish originality; compare dated primary sources.
4. The frozen verifier must pass. If raw subset count exceeds its safety cap, do not weaken the finite quantifier or claim acceptance: record the obstruction and seek a rigorous exact certificate that the independent parent can check.
5. No unproved hypotheses, no axiom/sorry/unsafe/native_decide/ofReduceBool/opaque/external proof bypass. No changed frozen files. Preserve every unsuccessful attempt.
6. Reviewer returns done:false for all partial results, finite-prefix exclusions, counterexample-search misses, known results, or incomplete full-proof formalization. Terminal acceptance additionally requires genuine reviewer acceptance and journal how=done, ok=true.

Parent D5 order-10 BFS reached a 900-second timeout without a result: UNKNOWN. Do not repeat that BFS.
