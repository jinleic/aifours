# A REF-failing lower-matching family with an original mixed selector

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 19:05:28 PDT 2026**. Exact written all-prime family and separately checked finite instances; no disjoint mathematical review, formal proof, novelty or global-adoption verdict.

## 1. Actual word and exact claims

For every prime `p>=7` and any nonzero `a∈F_p`, write `Z=σ_0=s`, `T_j=σ_(ja)=r^(ja)s` for `1<=j<=p−1`, and `ρ=r^a`. Construct the ACTUAL original-order word

`W = Z_1 · ρ · Z_2 · ... · Z_(2p−1) · ρ · T_1 · ρ · T_2 · ρ · ... · T_(p−1) · ρ`.

There are exactly `2p−1` named Z reflections, `p−1` named T reflections and `p+1` named ρ rotations. Thus `F=3p−2`, `R=p+1`, and `|W|=4p−1`. Every rotation is nonzero. Every cyclic reflection gap contains at most one rotation, including the final ρ gap from `T_(p−1)` to Z_1.

The family satisfies, for all p>=7:

1. **REF-failure:** NO identity `2p` selector uses reflections only; indeed the possible reflection-only `2p` products have exactly the p−1 nonzero rotation exponents.
2. **Actual lower raw matching:** for the specified possible-switch raw graph, `ν_M=(p+1)/2<=p−3`.
3. **An explicit original mixed selector:** W nevertheless has an identity selection of exactly2p actual original occurrences, given in §4.

Thus the combined count/zero-free/singleton-gap/low-matching/REF-failure constraints are nonempty, and this particular all-prime family is SOLVED by an actual mixed selector. The retained OLD/SEL/IPGEN/GS/DS3 caller failures have NOT been checked for this family. Therefore it is NOT asserted to belong to their full L_RES residual, and is NOT a counterexample to L_RES or ordered Olson.

## 2. Exact REF-failure, including all original index selections

Any `2p` reflection-only selection uses at least one T, because there are only `2p−1` Z occurrences. Suppose it uses t tail reflections with chronological tail ordinals

`1<=j_1<...<j_t<=p−1`.

It uses `2p−t` Z occurrences, all before those tail reflections. If t is even, the zero block has even length and the tail's alternating exponent is

`−a * sum_(h=1)^(t/2) (j_(2h)−j_(2h−1))`.

The integer sum is positive and at most p−2: its intervals are disjoint inside `[1,p−1]`. It is therefore nonzero modulo p.

If t is odd, the zero block has odd length and reverses the tail's initial sign. Up to that overall sign, the tail alternating exponent is

`a * [ j_1 + sum_(h=1)^((t−1)/2) (j_(2h+1)−j_(2h)) ]`.

This integer lies between 1 and `j_t<=p−1`: it is the first index plus disjoint positive gaps ending at j_t. It is again nonzero modulo p. These arguments depend only on the number of selected Z's, not which identical original Z indices are chosen, and cover EVERY possible reflection-only selection.

Conversely, selecting all `2p−1` Z occurrences and any single T_j gives reflection-only exponent `−ja`; as j runs from1 to p−1 these are all nonzero F_p values. Thus the exact reflection-only support is `F_p\{0}`, proving REF-failure.

## 3. Exact actual raw graph

Use the original literal raw graph definition: two consecutive CYCLIC reflection occurrences form an edge when their endpoint exponents differ OR their actual reflection gap contains a rotation. This is the local graph definition only, not an import of any prior historical theorem.

The actual edges form the one path

`Z_(2p−1) — T_1 — T_2 — ... — T_(p−1) — Z_1 — Z_2`.

The T-to-T and Z-to-T edges are present by unequal exponents (and occupied in this word); the last `Z_1—Z_2` edge is present because its gap contains ρ. Every other gap is empty between equal Z reflections and is absent. The path has p+1 edges and p+2 vertices; the remaining `2p−4` reflection vertices are isolated. Hence

`ν_M=floor((p+2)/2)=(p+1)/2<=p−3` for every p>=7.

No claim about the other residual callers follows from this graph computation.

## 4. A separate all-prime actual mixed selector

Let d be the integer in `{1,...,p−2}` representing `−1/3∈F_p`. It exists because p>=7; it cannot be −1, as that would force 2=0 in F_p.

Select these EXACT original occurrences:

* the first `p−3` Z reflections (this number is even);
* EVERY one of the p+1 actual ρ rotations;
* exactly the two actual tail reflections `T_1` and `T_(1+d)`.

The total count is `(p−3)+(p+1)+2=2p` and reflection parity is even. The first ρ is after the selected Z_1 and contributes `−a`. After the even number p−3 of selected Z reflections, the remaining p ρ occurrences contribute `p−2d` copies of a in signed exponent: exactly d lie between the two selected tail reflections and have negative sign, while the other p−d have positive sign. The two selected tail reflections contribute `a−(1+d)a=−d a`.

The ordered exponent is therefore

`[−1 + p−2d−d]a = (p−1−3d)a = 0`,

because `3d=−1` in F_p. These are the original indices and the calculation uses their actual order; no reflection-only witness, reordering or hidden caller is substituted.

## 5. Exact checks and remaining goal

`frontier-20261028-olson-ref-fail-lower-family-checker.py`, SHA256 `efb492ab8ada88a44d0a092e33b4bac5f9c3ada45c33a418679a14d6bb05d5bb`, returned `PASS_REF_FAIL_LOWER_SOLVABLE_FAMILY`; its saved result `frontier-20261028-olson-ref-fail-lower-family-check-results.json`, SHA256 `e22d4133ce4bbd32a694a55cf264973f32112c58f8aa60eb981e364775e6befc`, used a separate reflection-subsequence dynamic program and direct original-word multiplication for p=7,11,13,17,19.

A separately written audit `frontier-20261028-olson-ref-fail-lower-family-audit.py`, SHA256 `cbdc50451edd3496fd0ac094f2509fc916efa7a0fd387c212bd9f0baf058f488`, returned `PASS_INDEPENDENT_REF_FAIL_LOWER_FAMILY` in `frontier-20261028-olson-ref-fail-lower-family-audit-results.json`, SHA256 `11d1c927ca1b336614b05fee2f2c64807b9c85d046133b8eeab2c7aa7ac86d14`. It independently constructed the cyclic raw graph and traversed the claimed path, exhaustively checked every nonempty tail-index subset (63,1,023,4,095,65,535,262,143 classes respectively) with representative original zero indices, verified the exact nonzero reflection-only support, and directly multiplied the mixed identity selector. Zero indices with the same group element are interchangeable for this reflection-only check because they are all in one initial contiguous reflection-only block; the mixed selector was checked with its exact indices.

These are finite instance checks, not a formal proof, independent-model-family review, novelty or acceptance of historical caller failures. L_RES remains open for the ENTIRE retained residual. A disjoint full-source scientific review is requested.

**END — actual REF-failing lower-matching family, not an L_RES counterexample.**
