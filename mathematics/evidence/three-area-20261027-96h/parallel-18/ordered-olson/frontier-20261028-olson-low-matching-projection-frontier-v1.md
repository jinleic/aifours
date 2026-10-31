# Exact projection frontier after the low raw-matching bound

Owner MathOlson-2-2. Native `/bin/date` before writing: **Wed Oct 28 21:58:51 PDT 2026**. WRITTEN conditional integration, not a disjoint review or full L_RES result. Read the fatal actual-block/projection correction `frontier-20261028-olson-actual-block-fatal-correction-v1.json` (SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`) FIRST. No f111 verdict or historical floor is used.

## 1. Literal source and independent bookkeeping

The original `selection-lower-matching-packet-lift-v1.md:11–21,53–59` in the 20261023 root states the full L_RES residue: prime p>=7, N=4p−1, F=3p−2, R=p+1, nonzero rotations, singleton cyclic reflection gaps, raw possible-switch matching number ν<=p−3 and all applicable OLD/REF/SEL/IPGEN/GS/DS3 failures. The graph definition in `consolidated-lower-band-v1.md:85–89` is an edge between consecutive reflection occurrences iff the exponents differ OR the actual gap is occupied. These are source-interface imports, not proof adoption of other claims in those documents.

Let r_π=o_π+e_π be the number of maximal constant reflection-only PROJECTION runs. Let g_int count occupied actual gaps whose two reflection exponents agree. If r_π>=2, the number η of PRESENT graph edges is

`η = r_π + g_int = o_π+e_π+g_int`.  (1)

Every unequal-exponent gap is one projected-run boundary; the occupied equal gaps are disjoint from those boundaries. In contrast to the withdrawn identification, the ACTUAL rotation-separated block count is `r_F=η`, not generally r_π. If the entire projection is constant, it has one projected run but zero unequal-exponent boundaries; then η=g_int. Such a word is REF-covered since F>=2p.

Under ν<=p−3 the graph cannot be the full odd F-cycle, whose matching number is `(3p−3)/2>p−3`. Thus it is a union of paths. A path with h edges has matching size ceil(h/2), so summing over components gives `ν>=ceil(η/2)` and

`o_π+e_π+g_int <= 2p−6`  (2)

in every nonconstant projection. This is the explicit projection translation of the separate actual-block bound candidate `frontier-20261028-olson-actual-raw-bound-candidate-v1.md` (SHA256 `a99943dc702161aaf02f198a11004c3f4552b4169759afb2e127594994309ae7`), not a new projection-to-actual identification or inherited floor. The path proof above is complete without adopting that file.

## 2. Conditional remaining band

Read the COMPLETE candidate `frontier-20261028-olson-spare-sector-band-v1.md` (SHA256 `7ba998ffad4b8c52754675f92e8ed34ceb70f96728420bceeadbd85ec3b20802`) with ALL of its named odd/even stretched proof inputs in their required additive-source order. It conditionally covers o_π<=p. Separately, the self-contained candidate `frontier-20261028-olson-p2-band-v1.md` (SHA256 `2b02c24161f4cc2127ee180a0eebd6a03326a3428c6defbe176c80f9619046f1`) covers o_π=p+2. Neither has an observed disjoint mathematical adoption here.

**Conditional on those complete written candidates**, a still-unsolved actual low-matching word can only have

`o_π = p+2j,  j>=2,  and  2j+e_π+g_int <= p−6`.  (3)

The upper bound is `o_π<=2p−7`, because o_π is odd whereas 2p−6 is even. Thus p>=11 is necessary; at p=7 the low-matching word is already in the conditional o_π<=p band. This uses no old S(p)/Lev odd-block floor. At p=11, the only remaining projection cases are

`o_π=15, (e_π,g_int)=(0,0),(0,1),(1,0)`.

They are NOT eliminated here. At p=13, the remaining cases are j=2 with e_π+g_int<=3 or j=3 with e_π+g_int<=1. These are necessary conditions, not assertions of full residual membership, existence, avoiding words, or repaired scope accepted by a reviewer. Every original caller failure remains retained and unproved implications are not inferred from counts.

## 3. Numerical boundary

`frontier-20261028-olson-raw-run-bound-check.py` (SHA256 `8d89c2184a5093b94746e3abf24a373757c043f5c282e4902357c4d9fcb76d26`) ran 3000 sampled actual words at each p=7,11,13; `frontier-20261028-olson-raw-run-bound-check-results.json` (SHA256 `5e8fe2e279013022fd2910e66405340b56bc2cb02142d594327d1d3cedc5e3ea`) records PASS for the edge formula, cycle/path matching inequality and arithmetic conditions. **ZERO** sampled words simultaneously failed REF and had ν<=p−3. Accordingly these random observations supply NO finite coverage of the residual, no nonemptiness/emptiness conclusion, and no evidence eliminating (3). No separate checker was run for this exploratory file; the actual-block candidate has different exhaustive graph-mask evidence, separately pinned there.

**END — necessary remaining projection band, conditional on the named complete selector proofs.**
