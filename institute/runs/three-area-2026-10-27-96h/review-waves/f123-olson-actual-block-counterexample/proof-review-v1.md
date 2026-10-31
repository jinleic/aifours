# f123 proof review v1 — actual constant blocks versus reflection-only projection, and the explicit p ≥ 11 counterfamily

Review wave `f123-olson-actual-block-counterexample`; manifest SHA-256 `71777b4b6013d9775a9fd78e1ea6b27602f2e707a9d903cd19cabee504155e39` (3849 bytes). Observed clock before this file's creation: `2026-10-29T03:12:50Z` (Wed Oct 28 20:12:50 PDT 2026), a lower bound. Reviewer: in-harness subagent (Claude), fresh disjoint scope.

## 0. Boundary of this review

- The ENTIRE f111 adoption remains withdrawn. Nothing below rehabilitates it, adopts a repaired lift, adopts the old standalone four-term lemma, infers L_RES membership or emptiness, or transfers any prior 0F/fragment/control credit.
- Premises used: only the seven manifest inputs, read in declared order after full hash/bytes/LF verification (receipt: `proof-control-receipt-v1.json`). The three files pinned by the withdrawal disposition and every held candidate in the correction inventory were NOT opened.
- Author code (`…-checker.py`, `…-audit.py`) was read, not imported or executed. All finite checks reported here come from my own script `proof-control-v1.py` (SHA-256 `6621ff7c…71dd6`), which actually ran (§8).
- No human, independent-family, formal/kernel, novelty, SEL-predicate, L_RES-class or original-Olson-closure claim is made.

## 1. Definitions reconstructed from the literal excerpts only

From `source-definition-excerpts-v1.md` (SHA-256 `efcc70ab…115d`), lines quoted from `proof-UNIFORM-RESIDUAL-PARTIAL-v1.md` 219–231 and `consolidated-lower-band-v1.md` 85–115:

**D1 (actual block).** "o_F count[s] ODD maximal CYCLIC CONSTANT reflection blocks, not ordinary reflection runs." Lemma 7.1's proof fixes the fusion rule: removing a singleton concatenates its two rotation gaps; "If the resulting gap is nonempty, neighboring reflection blocks remain separated"; "If that gap is empty, the neighboring reflection blocks become adjacent. When their values differ they stay distinct … When their values are equal they fuse." Hence: two cyclically consecutive reflections lie in the same actual block **iff** the gap between them contains no rotation **and** their values are equal. Blocks are taken cyclically (the wrap gap between the last and first reflection counts).

**D2 (projected run).** The reflection-only projection deletes all rotations; its maximal cyclic constant runs fuse on equal value alone. This is the notion the correction says the withdrawn lift silently used.

**D3 (raw edge).** "an edge is present when the raw endpoint reflection values differ OR its gap is occupied by a rotation." So an absent raw edge is exactly an empty equal-value gap, i.e. exactly an internal adjacency of an actual block. The raw graph is the F-cycle minus absent edges; if not the full cycle its components are paths, and `nu_M = (F − o_M)/2` with `o_M` the number of odd-size components.

**D4 (statistics).** With actual block lengths ℓ_i: `H = Σ⌊ℓ_i/2⌋`, `o_F`/`e_F` = numbers of odd/even actual blocks, `k_F = o_F + e_F`, `κ = p − 1 − H`. The excerpt states "The number of empty equal-value gaps is exactly F − k_F = 2H − e_F", bound (B) `2κ + e_F ≤ p − 4`, and at the old floor `o_F = p + 2κ`. These are identities whenever there is at least one block boundary: Σ(ℓ_i − 1) = F − k_F counts internal adjacencies, and Σ 2⌊ℓ_i/2⌋ = F − o_F gives 2H − e_F = F − k_F and o_F = F − 2H = 3p − 2 − 2(p − 1 − κ) = p + 2κ. (My diagnostic re-checks these on 400 random words, control F.)

Excerpt conditions satisfied by the counterfamily (checked below): all rotations nonzero; every cyclic reflection gap of capacity ≤ 1; F = 3p − 2; graph not the full cycle; k_F = p + 2 ≥ 8 (Lemma 7.1's non-degenerate setting); bound (B); κ = 1 ∈ [1, (p−5)/2] for p ≥ 7.

## 2. The word W_p (author's explicit family, p odd prime ≥ 7)

Letters of D_{2p} = ⟨r, s | r^p = s² = 1, s r s = r^{-1}⟩: Z = s, T_j = r^j s, ρ = r. In actual order

    W_p = Z ρ Z ρ Z^{2p−3} ρ (T_1 ρ)(T_2 ρ) … (T_{p−2} ρ) T_{p−1}.

0-based positions: Z_1 = 0, ρ = 1, Z_2 = 2, ρ = 3, Z_3…Z_{2p−1} = 4…2p, ρ = 2p+1, T_j = 2p+2j (1 ≤ j ≤ p−1), ρ = 2p+2j+1 (1 ≤ j ≤ p−2). Counts: F = (2p−1) + (p−1) = 3p−2 reflections, R = 2 + 1 + (p−2) = p+1 rotations, N = 4p−1. Every rotation is r ≠ 1. Gaps between cyclically consecutive reflections: Z_1|Z_2 and Z_2|Z_3 occupied (one ρ each); Z_3|Z_4,…,Z_{2p−2}|Z_{2p−1} empty (2p−4 gaps); Z_{2p−1}|T_1 occupied; T_j|T_{j+1} occupied (p−2 gaps); wrap T_{p−1}|Z_1 empty. Maximum gap capacity 1. The scaling r ↦ r^a, s ↦ s (a ≠ 0) is an automorphism of D_{2p} preserving value equalities, gap occupancy and all product-one selections, so everything below holds for all scalings (my run also checks a = 2 directly).

## 3. Theorem A — actual block counts differ from projected run counts

**Claim.** Actual blocks of W_p are Z_1 | Z_2 | Z_3…Z_{2p−1} | T_1 | … | T_{p−1}: lengths 1, 1, 2p−3, 1^{p−1}; hence `o_F = p+2`, `e_F = 0`, `k_F = p+2`, `H = p−2`, `κ = 1`. Projected runs are Z^{2p−1} | T_1 | … | T_{p−1}: lengths 2p−1, 1^{p−1}; hence projected odd count p, projected even count 0.

**Proof.** By D1, Z_1|Z_2 and Z_2|Z_3 are occupied gaps, so they separate although the values are equal; the 2p−4 internal gaps of Z_3…Z_{2p−1} are empty with equal values, so they fuse; Z_{2p−1}|T_1 and all T_j|T_{j+1} are occupied (and unequal); the wrap T_{p−1}|Z_1 is empty but r^{p−1}s ≠ s since p−1 ≢ 0 (mod p), so it separates. This gives exactly the listed blocks; 2p−3 is odd, so all p+2 blocks are odd. By D2 the two occupied equal-value gaps disappear and Z_1 Z_2 Z_3…Z_{2p−1} fuse into one run of odd length 2p−1; the tail is unchanged. ∎

So the correction's FATAL statement is correct: the projection's (o, e) = (p, 0) is not the actual (o_F, e_F) = (p+2, 0); the difference is exactly the two occupied equal-value gaps. Identities check: F − k_F = 2p − 4 = 2H − e_F; o_F = p + 2κ with κ = 1; (B): 2·1 + 0 ≤ p − 4 for p ≥ 7.

## 4. Theorem B — raw graph and matching scope

**Claim.** The raw graph of W_p is one path on p+3 vertices with p+2 edges plus 2p−5 isolated vertices; its matching number is ν = (p+3)/2.

**Proof.** By D3 the present edges are exactly the non-fusing gaps of §3: T_{p−1}–Z_1 (unequal), Z_1–Z_2 and Z_2–Z_3 (occupied), Z_{2p−1}–T_1 (occupied), T_j–T_{j+1} for 1 ≤ j ≤ p−2 (occupied): 1 + 2 + 1 + (p−2) = p+2 edges, the other 2p−4 edges absent. These edges form the single chain Z_3 – Z_2 – Z_1 – T_{p−1} – T_{p−2} – … – T_1 – Z_{2p−1} (Z_3 and Z_{2p−1} have their other incident edge absent), i.e. a path on 3 + (p−1) + 1 = p+3 vertices. The remaining 2p−5 vertices Z_4…Z_{2p−2} have both incident edges absent. A path on an even number p+3 of vertices has matching number (p+3)/2; isolates add nothing. Cross-check with the excerpt formula: o_M = 2p−5 odd components, (F − o_M)/2 = (3p−2−2p+5)/2 = (p+3)/2. ∎

**Thresholds.** (p+3)/2 ≤ p−2 ⟺ p ≥ 7, so for every prime p ≥ 7 the word is outside GS by the excerpt's criterion ("Every actual survivor outside GS therefore has raw matching number at most p−2", GS1 ⟺ ν ≥ p−1). (p+3)/2 ≤ p−3 ⟺ p ≥ 9, so the author's stricter regime ν ≤ p−3 holds exactly for primes p ≥ 11, and at p = 7 ν = 5 = p−2 > p−3. The author's statements "matching (p+3)/2", "At p ≥ 11 this is ≤ p−3; at p = 7 it equals 5 > 4" are arithmetically correct. **Not derivable from my inputs:** why the relevant structural base is ν ≤ p−3 rather than the excerpt's ν ≤ p−2; the p−3 threshold is reported as the author's scope statement, not as a consequence of the excerpts.

## 5. Theorem C — REF failure by an elementary alternating-tail argument (independent of the author's)

**Convention.** For reflections r^{a_i}s, (r^a s)(r^b s) = r^{a−b}, so the left-to-right product of 2p reflections is r^{Σ_{i=1}^{2p} (−1)^{i+1} a_i}; it is 1 iff the alternating exponent sum is ≡ 0 (mod p). Since reflections are involutions, the right-to-left product is the inverse of the left-to-right one, so REF success/failure is independent of multiplication convention.

**Claim.** No 2p-term reflection-only in-order subsequence of W_p has product 1; the set of attained rotation exponents is exactly F_p ∖ {0}.

**Proof.** The reflection projection is 0^{2p−1} followed by 1, 2, …, p−1 (all zeros precede the tail). Any 2p-selection takes k zeros and a tail subset j_1 < … < j_m, with k + m = 2p, 1 ≤ m ≤ p−1 (m ≥ 1 because only 2p−1 zeros exist). The zeros contribute 0 whatever their positions; the tail occupies selection positions k+1, …, 2p, and position 2p has sign −, so the alternating sum is −A with

    A = j_m − j_{m−1} + j_{m−2} − … ± j_1.

If m is odd, A = (j_m − j_{m−1}) + … + (j_3 − j_2) + j_1 ≥ 1 and A = j_m − (j_{m−1} − j_{m−2}) − … − (j_2 − j_1) ≤ j_m ≤ p−1. If m is even, A = (j_m − j_{m−1}) + … + (j_2 − j_1) ≥ 1 and A = j_m − (j_{m−1} − j_{m−2}) − … − j_1 ≤ j_m − j_1 ≤ p−2. In all cases 1 ≤ A ≤ p−1, so A ≢ 0: no product-one reflection selection. Conversely m = 1, k = 2p−1 (all zeros) gives exponent −j for every j ∈ {1,…,p−1}, so the support is all of F_p ∖ {0}. ∎

This refutes the implication quoted in the withdrawal disposition — "Actual o_F = p+2 and e_F ≤ 1 alone implies an original-order product-one 2p-reflection selector" — for every prime p ≥ 7 (W_p has o_F = p+2, e_F = 0 by Theorem A and no such selector by Theorem C), and within the author's ν ≤ p−3 regime for every prime p ≥ 11 (Theorem B). I cannot see the withdrawn theorem's own wording (held); the refutation is relative to the implication as quoted in input 1 and to the structural conditions listed in the excerpt, all of which W_p satisfies (§1).

## 6. Theorem D — W_p has in-order mixed identity 2p-selectors, under either multiplication convention

(a) **Author's selector** (positions in increasing order): Z_1 ρ Z_2 ρ, then Z_3…Z_{p−3} (p−5 zeros, even), then ρ T_1 ρ^d T_{d+1} ρ^{p−2−d} with d ≡ −3^{−1} (mod p), 1 ≤ d ≤ p−2. Left-to-right: s r s r = 1; s^{p−5} = 1; r·rs = r²s; r²s·r^d = r^{2−d}s; r^{2−d}s·r^{d+1}s = r^{1−2d}; ·r^{p−2−d} = r^{p−1−3d} = 1 iff 3d ≡ −1. Length (p−3) + (p+1) + 2 = 2p. ✓ Right-to-left the same index set gives r^{p−1−d} ≠ 1 (d ≠ p−1), so this selector is convention-dependent.

(b) **Independent forward selector** (mine, p ≥ 7): Z_1 ρ Z_2 ρ Z^{2p−12} ρ T_1 ρ ρ T_3 ρ ρ ρ. Left-to-right: 1 · 1 · r·rs = r²s; ·r² = s; ·r³s = r^{−3}; ·r³ = 1. Length 4 + (2p−12) + 2 + 2 + 1 + 3 = 2p; needs 2p−12 ≥ 0 and three rotations after T_3 (p−1−3 ≥ 3), i.e. p ≥ 7. ✓

(c) **Independent reversed-convention selector** (mine, p ≥ 5): index set {2p−4 zeros of Z_3…Z_{2p−1}, T_1, the two ρ after T_1 and T_2, T_3}. Right-to-left product T_3 ρ ρ T_1 Z^{2p−4} = r³s·r²·rs·1 = r³s·r³s = 1. Length 2p−4 + 4 = 2p. ✓

Hence, whichever left/right multiplication convention the ordered problem uses, W_p contains an in-order product-one subsequence of length 2p = |D_{2p}| and is **not** a counterexample to an ordered Olson/EGZ-type statement at length 4p−1. This is the part of "not L_RES / not Olson" that is provable from my inputs. (At p = 11 my DP counts 37,602,420,590 forward and 3,491,945,682 reversed identity 22-selections among C(43,22) = 1,052,049,481,860 index sets.)

## 7. The exact p = 11 word as a real indexed word (from my run)

`0:Z 1:ρ 2:Z 3:ρ 4..22:Z(19) 23:ρ 24:T1 25:ρ 26:T2 27:ρ 28:T3 29:ρ 30:T4 31:ρ 32:T5 33:ρ 34:T6 35:ρ 36:T7 37:ρ 38:T8 39:ρ 40:T9 41:ρ 42:T10` — N = 43, F = 31, R = 12.

- Actual blocks (value, length, indices): (0,1,[0]), (0,1,[2]), (0,19,[4…22]), (j,1,[22+2j]) for j = 1…10 → o_F = 13, e_F = 0, H = 9, κ = 1. Projected (o,e) = (11, 0).
- Raw path indices: [22, 24, 26, …, 42, 0, 2, 4] (14 vertices, 13 edges); 17 isolates = indices 5…21 (Z_4…Z_{20}); 14 + 17 = 31. ν = 7 by formula and by exhaustive edge-subset brute force (2^13 subsets). 7 ≤ 8 = p−3.
- REF: group-element DP over the 31 real indices: identity absent from the 22-products; attained rotation exponents exactly {1,…,10}; no reflection products. Class exhaustion over all 1023 nonempty tail subsets with the forced zero count: no identity, 1 ≤ A ≤ 10, class cardinalities Σ_m C(21, 22−m)·C(10, m) = 20,160,075 = C(31,22), so all index-level 22-subsets are covered. 20,000 random index-level 22-subsets: 0 identities, 0 disagreements with the class representative.
- The author's stated selector `[0,1,2,3,4,5,6,7,8,9,23,24,25,27,29,31,33,35,37,38,39,41]` has 22 strictly increasing indices, equals the d = 7 formula (3^{−1} = 4, d = −4 ≡ 7), and multiplies step by step (a,b) = (x ↦ ax+b) to (10,6) after index 37, (1,9) after T8, (1,10), (1,0) = identity. Reversed convention: r³ ≠ 1 (as predicted r^{p−1−d} = r³).

## 8. Independent finite diagnostic — what actually ran

`proof-control-v1.py` (own code; affine-map dihedral arithmetic; cyclic block rule D1; projection D2; raw edge D3) was run once: `python3 proof-control-v1.py proof-control-results-v1.json`, clock before run `2026-10-29T03:10:33Z`, script-recorded start/end `03:10:34Z`/`03:10:37Z`, elapsed 3.703 s, exit 0, Python 3.14.3, macOS-27.0.1-arm64. Results SHA-256 `22ed06d06d1658c9cb0c346710062bd79a2a24042f2a6b1cb7f59624566d25a0` (32829 bytes); script SHA-256 `6621ff7cd2a92f2c39e9e6c1470daec313081416e3b8ae6b56c097376c671dd6` (28591 bytes), also self-recorded inside the results. Overall `ALL_EXPECTED`.

Per prime p ∈ {7, 11, 13, 17, 19, 23} (all true unless noted): N/F/R = 4p−1/3p−2/p+1; rotations nonzero; gap capacity 1; actual (o,e) = (p+2, 0) with lengths {1,1,2p−3,1^{p−1}}; projected (p, 0) with lengths {2p−1,1^{p−1}}; κ = 1; identities F−k_F = 2H−e_F and o_F = p+2κ; bound (B); raw components {p+3, 1^{2p−5}}; ν = (p+3)/2 by formula, equal to exhaustive edge-subset brute force for p ≤ 17; ν ≤ p−2 for all six, ν ≤ p−3 for {11,13,17,19,23} and not for 7; REF identity absent and support = F_p∖{0} (DP over real indices); class exhaustion complete for p ≤ 19 (classes 63/1023/4095/65535/262143, cardinalities summing to C(3p−2,2p)); full index-level brute force at p = 7 (all 11,628 14-subsets: 0 identities, support {1..6}); author selector, my forward selector and my reversed selector all identity under their conventions; mixed identity counts positive under both conventions; scaling a = 2 preserves counts and REF failure.

Controls (p = 7, 11, 13): **A moved occupied gap** (ρ at index 1 moved to the end): actual becomes (p, 1) with lengths {2, 2p−3, 1^{p−1}}, κ = 0, projection unchanged (p, 0), raw components {2, p+1, …}, ν still (p+3)/2, REF still fails — the diagnostic detects the actual-block change the projection cannot see. **B no occupied equal-value gap** (both splitting ρ moved to the wrap, capacity 2, N = 4p−1): actual = projected = (p, 0); the distinction vanishes exactly when no occupied equal-value gap exists. **C cyclic shifts** (start at 10 inside the Z block, at the last letter, at 4, at T_1): cyclic (o,e), block multiset, raw component multiset and ν invariant; a linear counter gives (p+2, 1) at shift 10 — the cyclic rule matters and is implemented. **D REF positive** (T_{p−1} → Z): identity found (all 2p zeros), actual (p, 1), projected (p−2, 1) with the wrap fusing Z_1 and the new last Z. **E mutations**: wrong tail index (sorted) gives r^8/r^10/r^4 at p = 11/13/7, dropping the last rotation gives non-identity. **F 400 random words**: 0 union-find disagreements, 0 identity failures, 0 component-count failures, 0 matching disagreements on 378 brute-forced words.

Own-artifact limitation: `family[p=11].p11_selector_mutation_38to36` multiplies an unsorted index list (…,37,36,…); it is a product-function mutation only (result r ≠ 1), not an in-order selector; control E is the in-order one. Brute-force matching only p ≤ 17.

## 9. Source/correction correspondence audit (author correction `e11fd873…f90e`)

| Author statement | Finding |
|---|---|
| Actual blocks Z, Z, Z^{2p−3}, T_1…T_{p−1}; o_F = p+2, e_F = 0; projection Z^{2p−1}, T's; projected p/0 | Correct (Theorem A; run p = 7…23) |
| R = p+1, F = 3p−2, N = 4p−1, rotations nonzero, gaps singleton/empty | Correct |
| Support of 2p-reflection products = F_p ∖ {0}; no reflection-only identity | Correct (Theorem C; three independent finite methods) |
| "Its reflection projection is the historically exhibited C_p" | Naming claim; not verifiable from my inputs (no such source supplied) |
| Raw graph: path on p+3 vertices, p+2 edges, 2p−5 isolates, ν = (p+3)/2; ≤ p−3 at p ≥ 11; 5 > 4 at p = 7 | Correct (Theorem B). The role of the p−3 threshold is not derivable from the excerpts, which give p−2 as the outside-GS bound |
| p11: N 43, F 31, R 12, o_F 13, e_F 0, projected 11/0, ν 7 ≤ 8, zero absent, stated selector | All correct (§7); selector verified letter by letter |
| "literal SEL predicate applies" (2p−1 copies of Z, actual Z ρ Z triple) | Not verifiable: no SEL definition among my inputs. The factual premises (2p−1 Z's; Z ρ Z at indices 0,1,2) are true |
| "neither an Olson nor L_RES counterexample" | Olson part proved from inputs (Theorem D, both conventions). L_RES part INCONCLUSIVE here: class not defined in my inputs |
| Inventory item on the f250-family word (blocks 1 and 2p−2, o_F = p, e_F = 1, H = p−1, κ = 0) | Arithmetic internally consistent; the word itself is a held file I did not open — unverified |
| Audit scope "all 63/1023/4095/65535 nonempty tail-subset classes" | Counts = 2^{p−1} − 1, correct; class method is complete because all zeros precede the tail (proved in Theorem C, also checked by cardinality sum) |

Author code observations (read-only): the checker's cyclic-merge guard compares only the values of the last and first reflections (ignores wrap-gap occupancy) and the audit's `actual_blocks` is linear, not cyclic; both are correct for W_p and the moved-gap mutant because the wrap is a genuine boundary there (T_{p−1} ≠ Z, and in the mutant the wrap is occupied), but neither would be valid on a word whose wrap gap is empty with equal values (my control C shows linear ≠ cyclic after a shift). The checker's DP sign rule, product rule, raw-edge rule and `d = −3^{−1}` selector are consistent with my independent derivations. Errors found in the correction's mathematics: none. Imprecisions: the p−3 threshold is a scope choice, not a consequence of the excerpts; the mixed selector is convention-dependent (covered by (c) above).

## 10. Verdict

- **Verified (full proof + independent finite run):** actual (o_F, e_F) = (p+2, 0) ≠ projected (p, 0) for every prime p ≥ 7 — the fatal actual-block/projection distinction is real; raw graph = path(p+3) + 2p−5 isolates, ν = (p+3)/2, ν ≤ p−2 for p ≥ 7 and ν ≤ p−3 exactly for primes p ≥ 11; no reflection-only in-order product-one 2p-selection (support F_p∖{0}); explicit in-order mixed identity 2p-selectors exist under both multiplication conventions, so W_p is not an ordered-Olson counterexample. The implication "actual o_F = p+2 and e_F ≤ 1 ⟹ reflection-only in-order 2p-selector" as quoted in the withdrawal is **refuted** by W_p for all primes p ≥ 7 (and inside the ν ≤ p−3 regime for p ≥ 11).
- **INCONCLUSIVE from my inputs:** formal SEL-predicate coverage and L_RES class non-membership (definitions absent); the "historically exhibited C_p" identification; the origin of the p−3 threshold; anything about the held f111 statements beyond the implication quoted in input 1.
- **Not claimed:** any repaired lift, standalone lemma adoption, p7 conditional floor, p11 profile exclusion, L_RES emptiness/non-emptiness, human/independent-family/formal/novelty status, original Olson closure.

Artifacts (this directory, `proof-` prefix only): `proof-review-v1.md` (this file), `proof-control-v1.py`, `proof-control-results-v1.json`, `proof-control-receipt-v1.json` (SHA-256 `6474d8f079e8d0690459a6d231deb1ae671615684d179eda994d44cf42687dd5`).
