# Universal row-support Hall obstructions and a concrete separation

Native `/bin/date` observed before writing: **Wed Oct 28 18:04:20 PDT 2026**. The general statements below are **WRITTEN, universally quantified necessary conditions** for every actual partial row set and every n≥3. The explicitly displayed six-row example is **EXACT FINITE COMPUTATION, independently replayed**. Neither part proves unrestricted T2(11) nonexistence, gives a witness, assumes Latin columns or wrapped distances, claims novelty, or constitutes formal/kernel/human/model review.

## Universal necessary conditions

A T2(n) array has n permutation rows with no repeated directed linear event separately at distances1 and2. Its n(n−1) distance-one events exhaust all ordered pairs of distinct symbols. Every symbol appears once per row, so counting incoming and outgoing D1 events shows that **every symbol starts exactly one row and ends exactly one row**.

Let P be ANY k rows of a hypothetical T2(n), and let Ω(P) be the complete set of all permutation rows that individually avoid every D1 and D2 event already used by P and avoid its used first and last symbols. Let S be the unused start symbols and T the unused end symbols; `|S|=|T|=m=n−k`. Every remaining row of that SAME completion belongs to Ω(P), and the rows' remaining starts and ends are both bijective.

For `U⊆S` and d∈{1,2}, define `Supp_d(U)` as the union of the actual linear distance-d events of every eligible row in Ω(P) whose first symbol lies in U. The completion has exactly |U| remaining rows with those starts, each contributing n−d distinct events at distance d; all of those events are mutually distinct. Consequently the following **Hall-type support inequalities** are necessary:

`|Supp_1(U)| ≥ |U|(n−1)` and `|Supp_2(U)| ≥ |U|(n−2)` for EVERY U⊆S.

Likewise, if `End(U)` is the set of eligible row endings reachable from starts in U, the completion supplies an injective assignment from U into End(U), so `|End(U)|≥|U|`. The analogous inequalities hold with starts and ends interchanged. They are necessary only: eligible rows may conflict with each other and a perfect matching or large support does not prove a completion.

In particular take U=S at distance2. A full T2(n) has n(n−2) distinct D2 events among n(n−1) ordered nonloops, so **exactly n D2 pairs are missing**. If more than n D2 pairs are neither already used by P nor supported by any row in Ω(P), then no T2 completion of P exists. This is equivalent to `|Supp_2(S)|<m(n−2)`. The argument remains valid for any independently proved **superset** of all possible next rows; an arbitrary restricted search set cannot certify the exclusion.

## Concrete six-row separation

Consider these actual six permutation rows on symbols0..10. The first three are rows 3,5,10 of `frontier-20261028-three-row-fast-run-01.json` (SHA-256 `fe7742f066d2a0a6d996eab1f2b65bc4f3c12b2032443de7f5af6154678e14fb`); the next three are an actual compatible continuation recorded in the solver output:

```text
1 7 2 10 0 9 5 8 4 3 6
4 9 7 5 0 8 6 10 1 2 3
10 6 3 5 2 0 7 9 4 1 8
5 10 3 8 9 2 7 6 1 0 4
3 7 4 6 2 9 8 0 1 10 5
8 5 4 2 1 3 9 0 6 7 10
```

An independent direct DFS enumerated **all 23** eligible next rows in 1,840 prefix nodes. The six rows have 60 distinct D1 and 54 distinct D2 events. Every one of the 50 missing D1 pairs has at least one eligible supporting row; every unused start and every unused end is also individually represented. Nonetheless two separate universal necessary conditions reject this partial array:

1. The unused starts are `{0,2,6,7,9}` and the unused ends are `{0,1,2,7,9}`. For `U={0,2,6,7}`, the eligible rows have endings only `{1,7,9}`. Four required distinct starts cannot use just three possible ends, so `|End(U)|=3<4`.
2. All 23 eligible rows together support only **44** unused D2 pairs, but the five remaining rows would require `5·9=45` pairwise distinct new D2 pairs. Equivalently these **12** ordered nonloops are forced missing: `(0,8),(1,10),(3,1),(3,7),(4,5),(5,7),(6,4),(7,8),(7,9),(8,6),(9,3),(9,10)`. A T2(11) can miss exactly11.

Thus singleton D1 support and singleton endpoint availability both pass, but genuine cross-row Hall and aggregate D2 support already prove that this PARTICULAR six-row continuation cannot be completed. It is not claimed that every six-row continuation has this property or that these rows are mandatory for the original problem.

## Evidence and computation limits

- The partial continuation was found as the first D2-support-pruned branch for which all D1 and endpoint singletons remain supported in `frontier-20261028-three-anchor-v4-run-01.json`, SHA-256 `e159e10f85cbaa12758010ce0b9e15ca2ba8bcefaba32e5c654fcdf7d1304c91`. Its actual 12-second three-anchor search remained **UNKNOWN**, not UNSAT. It observed 321,148 D2-support prunes, but that aggregate is not an independently certified exhaustive result. Source `frontier-20261028-three-anchor-exact-v4.cpp` SHA-256 `064300e403b9f63d19a968f1cd47adffdff4a812161f399df78315db52c2e211`.
- The separate direct DFS/checker `frontier-20261028-d2-support-check-v1.py`, SHA-256 `c6df82e00f1470d079523fceca4de3b7296d1287e3bab474ed6da9ab1025e5ce`, reconstructed all eligible rows and the forced-missing event list. Output `frontier-20261028-d2-support-check-run-02.json`, SHA-256 `49e2500d3dadca948cf03b104eb1fa145bcb7ff869ec829d76e7716206cda0`. A second exact in-kernel BFS grouped the 23 eligible rows by start/end and obtained the displayed Hall neighbor set. These finite checks share the elementary eligibility definition, and are not a formal certificate or novelty assessment.
- The theorem quantifies over every actual candidate P; the displayed P is only one diagnostic. No failed/unknown heuristic is a universal no-go, and no fixed row is imposed on an original-target witness.
