# An actual identity-four selector with projected odd-run pairs

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:24:46 PDT 2026**. This is a NEW **WRITTEN sufficient-condition candidate**, with actual bounded checks in §5. It is NOT an accepted repaired actual-block lift, full L_RES solution, independently reviewed result, formal proof or novelty claim.

Before reviewing this source, read the fatal source/impact record `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. The old f111 disposition and its actual-block applications remain withdrawn/held. This source defines its REFLECTION-ONLY projection explicitly and never equates those runs with historical `o_F/e_F`.

## 1. The selector criterion

Let p be any odd prime and W an ACTUAL `D_(2p)` word with exactly F=3p−2 reflections, in arbitrary order among arbitrary rotations. Delete rotations ONLY to define its cyclic reflection-only projection. Suppose that projection has exactly p odd-length maximal constant runs; even projected runs may also occur.

Suppose in the ACTUAL cyclic full word there are four CONSECUTIVE original occurrences

`σ_c · ρ_b · σ_c · ρ_b`,  (1)

and the two σ_c occurrences belong to the SAME ODD projected constant run. The rotation value b may be arbitrary, including0. Then W has an identity subsequence of exactly2p ACTUAL original occurrences, in increasing original index order.

The hypothesis concerns one explicitly named actual four-letter block and separately defined projected reflection data; it does not require a guessed normal form, raw matching value, or L_RES caller outcome.

## 2. Proof and the cyclic split issue

The actual four-letter block in (1) is identity:

`σ_c ρ_b σ_c ρ_b = ρ_(−b) ρ_b = 1`.

The projection has F reflections and p odd runs, so its total equal-reflection pair capacity is

`H_π=(F−p)/2=p−1`.

The two selected σ_c occurrences are consecutive in the reflection-only projection, because the actual block contains no other reflections between them. Removing just those two from their odd projected run decreases that run's equal-pair capacity by exactly one and leaves it nonempty and odd. All other projected runs retain their capacities. Thus the remaining reflection occurrences have cyclic equal-pair capacity exactly `p−2`.

Make the cyclic cut immediately BEFORE the first σ_c of the actual identity-four block. The selected block is then first in the cut word, and all remaining reflection occurrences are after it. The odd projected run containing the two removed reflections can be split between the end and the beginning of this cut reflection list. Its two remaining piece lengths sum to an ODD integer; hence one piece is even and one odd, and the sum of their floor-half-lengths is still the floor-half-length of their total. No equal-pair capacity is lost at the cut. Pair remaining equal reflection occurrences consecutively within each linear run segment; all intervening unselected rotations and unselected reflections are skipped.

Select the actual four-letter identity block and all `p−2` such equal-reflection pairs. Each pair is an identity subproduct in the selected cut word and the four-letter block is also identity. The selected count is `4+2(p−2)=2p`; no other letter is selected. The selected cut-order product is1. Restoring the same actual positions to increasing original word order cyclically rotates this identity product, and `UV=1` implies `VU=1`. Thus the original-order product is identity. QED.

The proof allows projected even runs, but the named identity-four block MUST lie in an odd projected run. It does not assume that projected runs are actual occupied-gap blocks.

## 3. The exact AP/e0 family as one caller

The independently written actual-gap candidate `frontier-20261028-olson-ap-e0-actual-residual-family-v1.md`, SHA256 `c69379a1321041dbd66b88b3dd16609dbb33effe66aef5e0b5ebf6f151ee8d26`, has p odd projected runs and begins with an actual `Zρ_b Zρ_b` block. Its explicit mixed selector is therefore one instance of §1. Its actual block, graph and caller-status analysis is a SEPARATE pending-review matter; no full residual membership follows from this selector criterion.

## 4. Honest remaining gap

The original universal L_RES still includes words without (1), or with (1) in an even projected run, or with a different projected odd-run count. This selector criterion does not prove that the block exists, does not decide OLD/SEL/IPGEN/GS/DS3 failures, and provides no counterexample or novelty verdict.

## 5. Bounded actual-word checks

`frontier-20261028-olson-projection-identity4-experiment.py`, SHA256 `a4ca982352fb9fec43a03156eae897751161d600b38525f1d0a6c9642ffb20f3`, generated 250 actual full zero-free singleton-gap words at p=3,5,7,11,13; saved `frontier-20261028-olson-projection-identity4-results.json` has SHA256 `16479af6fce64828536e9e419fc2a90e1788230f9e88da217aa64b9dcb2ede5a`.

Separately written `frontier-20261028-olson-projection-identity4-checker.py`, SHA256 `eca86c0981eb20a84256e5aa4b8d687055f041099193af13c4704f54cd02ad1e`, imported no producer and returned `PASS_INDEPENDENT_PROJECTION_IDENTITY4` in result SHA256 `f0abbeacb06f079ea0a026f9999f147a02f152b16ed52be0e3d5c5d1d5846b27`. It reconstructed the cyclic projected runs, checked the named four ACTUAL cyclic-adjacent occurrences, separately paired the selected residual reflections after the block, and directly multiplied all250 original-index products. Thirteen identity-four blocks crossed the original start; duplicate-selected-index and changed-second-rotation controls were rejected for their intended reasons. The generated fixtures had no even projected runs, so the checker does NOT supply numerical coverage of the theorem's allowed even-run case.

These finite checks are not a universal proof, an independently reviewed result, or any repair of the held f111 disposition. A NEW disjoint full-source review is required before adoption.

**END — exact identity-four sufficient condition and explicit residual.**
