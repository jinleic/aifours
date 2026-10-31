# An actual family requiring six selected reflections

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 18:17:12 PDT 2026**. Exact written family plus finite checks; no independent review, novelty/priority or global Olson claim.

## 1. The exact all-prime family

For every odd prime `p>=5` and any nonzero `a∈F_p`, take the ACTUAL original word

`W_p(a) = [p+3 copies of s] · [2p−1 copies of r^a] · [p−3 copies of r^(−a)]`.

The brackets denote occurrence repetitions in THAT order, not cancellation or a reordered group product. It has F=p+3 reflections, R=3p−4 rotations and length `4p−1`.

**Theorem.** The minimum number of reflections in any actual identity subsequence of W_p(a) of length2p is **exactly six**.

This is a counterexample to any purported universal claim that, in this count band, some length2p selector can always be chosen with at most four reflections. It is NOT a counterexample to the ordered Olson statement: §3 explicitly constructs a length2p selector. It is NOT a counterexample to L_RES unless L_RES independently asserts the stronger at-most-four-reflection property, which is not asserted here.

## 2. Prove no selector uses 0, 2 or 4 reflections

Every selected reflection is s and every reflection occurs before EVERY rotation. An identity selection has an even number 2k of reflections, so the reflection subword is `s^(2k)=1` and the selected rotations multiply with positive exponents in the ACTUAL selected order. If q of the selected rotations are `r^(−a)`, their total exponent is

`(2p−2k−2q)a = −2(k+q)a` in F_p.  (1)

There are at most p−3 negative-a rotations.

* For k=0, selecting 2p rotations requires at least one negative-a rotation because only 2p−1 positive-a rotations exist. Thus `1<=q<=p−3`, and (1) is nonzero.
* For k=1, `1<=k+q<=p−2`, so (1) is nonzero.
* For k=2, `2<=k+q<=p−1`, so (1) is nonzero.

Here 2a is nonzero because p is odd and a!=0. Odd numbers of reflections give odd reflection parity and cannot yield identity. Therefore no `2p` selector uses fewer than six reflections. This quantifies over ALL allowed rotation index selections, not just a particular run or chosen witness.

## 3. Six reflections actually work

Select any six of the p+3 initial s occurrences, any p−3 of the `r^a` occurrences, and all p−3 `r^(−a)` occurrences. These are `6+2(p−3)=2p` original positions. The reflection subword is `s^6=1` and the selected rotation exponent is `(p−3)a−(p−3)a=0`. Thus the original-order product is identity, and the minimum is exactly six. QED.

## 4. Exact obstruction to the previous two-reflection route

For ANY pair of reflection positions, every rotation lies after both, so the signed rotation multiset is the actual raw multiset. Its maximum multiplicity is `2p−1`; the minority multiplicity is p−3, which is strictly below p−2. Hence none of the preceding low-maximum (`M<=2p−2`) two-support, diverse-swap, half-total or coupled-triangle sufficient conditions applies to any pair. The family also defeats the stronger idea of using an arbitrary four-reflection selector, by the all-index proof in §2. The six-reflection selector is a genuinely different original-order mechanism, not a shortened-word witness.

A bounded prefix search first exposed the p=5 member, `frontier-20261028-dihedral-prefix-obstruction-search.py`, SHA256 `d74b0106734d7f52bd526c5672a8f50168dd782210b25cb2775813612d1bbb53`, result `frontier-20261028-dihedral-prefix-obstruction-results.json`, SHA256 `1095ef05d4a86a17926f08a72f9ee7b60a51aacf122f5cf53cd8b5c71066fd1f`. Only the actual displayed family member and its zero low-pair edges are used; the search's other cases are not an all-prime premise.

## 5. Finite exact check and remaining scope

`frontier-20261028-dihedral-six-reflection-minimum-checker.py`, SHA256 `f223e5116d461c59d93edd05ec467047dd25b1ff1fb665ddc36119f6b6ae3303`, actually returned `PASS_MINIMUM_SIX_REFLECTIONS` in `frontier-20261028-dihedral-six-reflection-minimum-check-results.json`, SHA256 `90330444feff9d65595896155b41706f4fe224852fc662accea1ba29a974b19a`. At p=5,7,11,13,17 it checked every feasible negative-rotation multiplicity q for each of 0,2,4 reflections via direct multiplication of representative actual index selections, and directly multiplied an explicit six-reflection original-index identity selector. Indices with the same group values are interchangeable only for THIS grouped family, as the proof in §2 explains; no exhaustive all-word claim is made.

The full R=3p−4 band, other count bands, L_RES and the original all-finite-groups problem remain unresolved by this family. No human/cross-family review or formal proof has occurred.

**END — exact global reflection-count minimum within this family.**
