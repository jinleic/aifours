# Ordered four-reflection lemma and the first odd-run boundary

Owner **MathOlson-2-2**, original math-2. Native `/bin/date` immediately before writing: **Wed Oct 28 19:18:09 PDT 2026**. This is a self-contained **WRITTEN proof candidate**, with actual bounded checks in §7. No independent scientific review, formal proof, novelty or global-adoption verdict has yet occurred.

## 1. The two exact statements

**Ordered-four lemma.** For every odd prime p, ANY sequence `z_1,...,z_(p+2)` in F_p with `z_i != z_(i+1)` for each consecutive linear pair contains indices `i<j<k<l` with

`z_i−z_j+z_k−z_l=0`.  (1)

No full-support, distinctness of non-neighboring terms, or prescribed order is assumed.

**Actual odd-run theorem.** Let an arbitrary actual `D_(2p)` word have exactly `F=3p−2` reflections. Decompose the CYCLIC reflection-only order into maximal constant-exponent runs. If the number of odd-length runs is `o_F=p+2` and the number of even-length runs satisfies `e_F<=1`, the original word is REF-covered: it has an identity selector of exactly2p actual reflections in original full-word order.

These are direct REF proofs, independent of rotation values and of every historical caller. They do NOT prove L_RES for all residual words, construct an avoiding word, settle the full original count band or assert novelty. The separately stated old-floor consequence in §6 has an explicit historical trust boundary.

## 2. Full-support auxiliary lemma

Suppose a sequence of n>=p+2 elements has ALL p field values and adjacent terms unequal. If it has no ordered zero quadruple, for each consecutive triple let `t=z_i−z_(i+1)+z_(i+2)`. The value t occurs somewhere by full support. If an occurrence is before or after that triple, it and the triple give an ordered zero quadruple. Thus it must occur inside the triple. It cannot equal either endpoint because adjacent terms differ; hence it equals the middle, so consecutive differences are equal. All steps are one nonzero d, and the actual positions `1,2,3,p+2` have alternating sum `−p d=0`, contradiction. This elementary argument works for p=3 as well.

## 3. Prove the ordered-four lemma for ALL supports

Assume the length-p+2 sequence has no ordered zero quadruple.

**Multiplicity at least four.** Four occurrences of the same value give zero immediately.

**One value a occurs at least three times and a different value b at least twice.** Consider the two chosen b positions and divide the three chosen a positions into before, strictly between and after them. If any region contains two a's, the a-pair and b-pair are either disjoint or nested and give `a−a+b−b=0` or `b−a+a−b=0` in actual order. If the three regions contain one a each, their order is `a,b,a,b,a`; select the outer a's and both b's to get `a−b+b−a=0`. Thus this case is impossible.

If a value occurs exactly three times and no other value repeats, the length p+2 sequence has exactly p distinct values. It has full support, contradicting §2. We have therefore reduced to the case in which EVERY value has multiplicity at most two.

Let s be the number of values occurring twice. The support size is `r=p+2−s<=p`, so s>=2. If two distinct repeated values a,b had disjoint occurrence intervals, the four positions would be `a,a,b,b` or the reverse and give zero. If their intervals were nested, the positions would be `a,b,b,a` or the reverse and give zero. Thus EVERY pair of repeated-value intervals must CROSS: their four occurrences are ordered `a,b,a,b` or `b,a,b,a`.

For such a crossing pair, put `x=2a−b`. It is distinct from both a and b, because p is odd. We claim x cannot occur ANYWHERE in the sequence. In the order `a_1<b_1<a_2<b_2`:

* if x occurs before a_1, select `x,a_1,b_1,a_2`;
* if it occurs between a_1 and a_2, select `a_1,x,a_2,b_2`;
* if it occurs after a_2, select `a_1,b_1,a_2,x`.

Their alternating sums are respectively `x−a+b−a`, `a−x+a−b`, `a−b+a−x`, all zero. In the reverse crossing order `b_1<a_1<b_2<a_2`, use respectively `x,a_1,b_2,a_2`, `b_1,a_1,x,a_2`, or `a_1,b_2,a_2,x`. These are again four DISTINCT actual indices and have alternating sum0. Thus x is absent.

Fix one repeated value a and let b range over the other s−1 repeated values. The values `2a−b` are all distinct, and all are absent, so at least s−1 field values are missing from the sequence. But its support size is p+2−s, so exactly `p−(p+2−s)=s−2` field values are missing. Contradiction. This proves (1).

## 4. Lift the lemma to original reflection indices

For F=3p−2, the number of actual equal-reflection pairs contained within the cyclic constant runs is

`H=sum floor(ell_i/2)=(F−o_F)/2=p−2`

when `o_F=p+2`. In their cyclic run order list the p+2 odd-run exponents. Each adjacent pair of equal odd-run exponents has at least one EVEN run between them, since consecutive full maximal-run labels differ. The intervening groups of even runs are disjoint, so there are at most e_F<=1 equal-adjacency edges in the CYCLIC odd-run label list.

If one exists, cut that odd-run list there; if none, cut anywhere. The resulting linear list has adjacent terms unequal. By §3, four odd-run representatives have alternating exponent0. Select exactly one actual reflection from each of those four odd runs, and also select all H pairs of equal reflections inside the original runs. Each odd run can supply `2 floor(ell/2)` paired occurrences plus its one representative, and every even run supplies all its paired occurrences. The selected number is

`2H+4=2(p−2)+4=2p`.

Within each selected run, cancel its adjacent selected equal-reflection pairs. The remaining four reflections are the four chosen representatives in their ACTUAL cyclic order and have identity product by (1). No rotation is selected or relocated.

Finally, restore the selected occurrences to increasing indices in the original full word. This is a cyclic rotation of an identity product; if UV=1 then VU=1. Hence the original-order selector is valid even when the chosen cut crosses the original word start. This proves the actual odd-run theorem.

## 5. A sharper raw-graph bound for the requested lower branch

This section is an elementary conditional calculation from the literal original raw graph definition: consecutive cyclic reflections form an edge if their exponents differ OR their actual gap contains a rotation. Suppose an actual F=3p−2 word has raw matching `ν_M<=p−3` and is REF-failing. The graph cannot be the full cycle, whose matching size `(3p−3)/2` is larger. Remove its absent edges; its components are paths. If o_M is the number of odd-size components,

`ν_M=(F−o_M)/2`, so `o_M>=p+4`.

A proper subgraph of a cycle has as many components as absent edges; hence there are at least p+4 absent edges. Every absent edge is an EMPTY gap between equal neighboring reflection exponents. Since REF failure excludes the all-equal reflection word, the number of cyclic constant-reflection runs r obeys

`F−r >= p+4`, hence `r=o_F+e_F<=2p−6`.  (3)

Also REF failure directly forces `H<=p−1`: otherwise select p equal-reflection pairs. Define `κ=p−1−H>=0`. As `o_F=F−2H=p+2κ`, (3) is the sharper lower-branch inequality

`2κ+e_F<=p−6`.  (4)

This derivation uses only the ACTUAL graph/gaps and REF failure; it does not require the old P, S(p), Lev, Z1, a rotation alphabet, or a caller's outcome.

For κ=1, `o_F=p+2`. The direct theorem §4 eliminates e_F=0 or1. Thus a hypothetical REF-failing lower word with κ=1 must have e_F>=2 and, by (4), p>=11.

## 6. Exact historical-floor corollaries, explicitly conditional

The original L_RES selection freezes ALL retained caller failures. The separately retained historical interface `consolidated-lower-band-v1.md:111–115` states the floor `o_F>=p+2`, equivalently κ>=1, with its S(p)/Lev statement-level ancestry. The new proof above does NOT establish that old floor or upgrade its trust.

**Conditional on that exact retained floor**, at p=7 inequality (4) is `2κ+e_F<=1`, impossible for κ>=1. Thus the stated lower L_RES class at p=7 is EMPTY under that inherited interface, and its universal implication is vacuous there. This is NOT an unconditional full p=7 count-band theorem or a proof of S(7).

At p=11 the bound is `2κ+e_F<=5`. Under the same retained floor, the only profiles not eliminated here are

* `κ=1, e_F=2 or 3`; or
* `κ=2, e_F=0 or 1`.

These are necessary count profiles only; no realization, full L_RES proof or counterexample is claimed. Other primes and all original OLD/SEL/IPGEN/GS/DS3 trust boundaries remain intact.

## 7. Exact bounded checks

`frontier-20261028-olson-odd-run-boundary-experiment.py`, SHA256 `e2d140361d2c17e916bcae7b4c4f8b5bf72e9f85dd6409394891ea074d93bd41`, generated 600 actual full R=p+1, F=3p−2, zero-free singleton-gap words at p=3,5,7,11,13 with `o_F=p+2`, e_F=0 or1, including cases where the odd-run label equality occurs ACROSS the single even run. Saved `frontier-20261028-olson-odd-run-boundary-results.json`, SHA256 `601c90b0dd21fba1a86e7bb87ef8ffe67775e9c1edb69f5eb9ce9f5cbae3d98f`.

A separately written checker `frontier-20261028-olson-odd-run-boundary-checker.py`, SHA256 `72325542919d2e5bd59ff3686717e221a42163354e2a318754c0142659f5d13b`, imported no producer and returned `PASS_INDEPENDENT_ODD_RUN_BOUNDARY_CHECK`; output `frontier-20261028-olson-odd-run-boundary-check-results.json`, SHA256 `34242dc9c388e44e24ee90d76abefa34cffe3bf6b2dcb5661c2e7f63a9fe1fbb`. It reconstructed every actual cyclic reflection run, checked all 600 distinct-index original reflection selectors by direct group multiplication, and observed e0/zero odd-label equalities 200, e1/zero 147, and e1/one 253. It independently checked every normalized adjacent-distinct label list at p=3,5 (16,4,096 lists), every crossing-pair affine-extension insertion in p=3,5,7 (60,200,420 cases), and targeted index and run-count mutations.

These finite checks do NOT independently prove the all-prime lemma, authenticate the historical floor, establish all omitted callers or confer formal/human/cross-family/novelty status. A disjoint full-source scientific review is requested.

**END — universal ordered-four lemma and exact conditional lower residual.**
