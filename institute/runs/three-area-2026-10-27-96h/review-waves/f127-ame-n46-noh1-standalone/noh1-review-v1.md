# f127 standalone review: N=46, t=26 no-Hamming-1 lemma and the (4,4,4,4) finite exclusion

Reviewer: same-harness subagent (f127-ame-n46-noh1-standalone). This is **not** a human, independent-model-family, formal/kernel, or novelty review. Native clock observed immediately before this write: see `noh1-review-receipt-v1.json` (`review_write_clock`); the file-creation time is an upper bound, not an asserted exact time.

## 0. Pins (freeze was not performed by this reviewer)

| Item | Path | SHA-256 | Bytes / LF |
|---|---|---|---|
| Candidate packet (sole mathematical input) | `physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-n46-noh1-4444-standalone-review-v1.md` | `4ba6941467b6fc06e530a008c047fef81ba0c60805d29a86ea3ac50ed5829306` | 14631 B / 108 LF, trailing `0x0a` present |
| Adopted ≥44 disposition (framework only) | `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-global-support-lower44-parent-v1.md` | `c6e578a2555f476c45ac5e3e31753fceda1e855c1d5a3adf90847f477444d90a` | 8288 B / 36 LF |
| Reviewer program (written from the packet's definitions, no author code) | `review-waves/f127-ame-n46-noh1-standalone/noh1-independent-enum-v1.py` | `18d50579a50542cb1a10bfef68b4f0213b20415e9e38adf5530b02a8124d5c68` | 24083 B |
| Reviewer receipt (`python3 -B`, exclusive create) | `review-waves/f127-ame-n46-noh1-standalone/noh1-independent-enum-receipt-v1.json` | `d7d124e81492dcc317ba9885d4dbe19454824d160fbc5b503f9dd2e0a6f7c759` | 80541 B; start `2026-10-28T20:24:56-0700`, end `2026-10-28T20:25:41-0700`, 45.67 s |

The candidate SHA equals the assignment pin; the review proceeded. The packet's six frozen author artifacts (`…noh1-enum-v1.py/.json`, `…noh1-latin-replay-v1.py/.json`, `…freefiber-component-control-v1.py/.json`) were **checksummed only** (contents not opened); all six hashes equal the values stated in packet §4/§8. Author programs were not executed or read.

## 1. Scope reviewed

Exactly the packet's input: a normalized complex AME(4,6) state with support N=46 in a fixed product basis, exactly t=26 coefficients of modulus 1/6 (set P), 20 remaining nonzero coefficients (set E); for Candidate B additionally that every E coordinate alphabet has size 4. Candidate A: no two E words at Hamming distance one. Candidate B: under (4,4,4,4), E cannot carry the residual unitary support. Nothing outside this scope is assessed (see §7).

## 2. Verdict (scoped)

**Candidate A (standalone no-Hamming-1 lemma for N=46, t=26): 0 FATAL / 0 MAJOR / 0 MINOR.** Every step was reconstructed from the unitary definitions (§3 below) and holds. Sole external import: Tarry's theorem (no pair of orthogonal Latin squares of order 6), used only in the m=10 case; not reconstructed here.

**Candidate B ((4,4,4,4) finite exclusion, conditional on Candidate A): 0 FATAL / 0 MAJOR / 0 MINOR.** The P-count normal form, the X/Y type restriction, the fibre shapes, the orbit representatives, the 144-fibre catalog, the XOR/no-fourfold reduction, the 2,975/10/40 all-Y outcome, the 240/10/no-cover one-X outcome, the per-cut unitary-overlap failure of all 40 supports, and the disclosed 30-of-40 cross-fibre superset were all reproduced by independently written exact enumeration (§5). A fully labelled enumeration with **no** orbit reduction (34³ and 15³ incidence patterns) reaches the same exclusion, so the finite result does not depend on the correctness of the orbit normalisation.

Conclusion within scope: at the no-OLS(6) import, the branch `N=46, t=26, E-alphabets (4,4,4,4)` is excluded, and the no-distance-one lemma holds for every N=46, t=26 configuration regardless of alphabet profile. **No** statement about N=46 globally, about t≠26, about other alphabet profiles, about ≥46/≥47, or about priority follows from this review.

## 3. Reconstruction of Candidate A from the unitary definitions

Notation: for each 2|2 cut the 36×36 flattening U=6ψ is unitary because both pair marginals are I/36.

1. **Residual structure (packet §2).** |6ψ|=1 at a P position forces the whole row and column norm, so each P position is a singleton row and column in every cut; 26 P positions occupy 26 distinct rows/columns (two in one row would exceed norm 1). Deleting them leaves a 10×10 unitary on E in each cut. A residual row with a single nonzero would have modulus 1, i.e. a 1/6 coefficient, contradicting its membership in E; so every residual row/column has ≥2 E entries; 20 entries over 10 rows gives exactly 2 per row and per column. Hence each of the six coordinate-pair projections of E has exactly 10 cells, each with exactly 2 extensions, and P-cells and E-cells are disjoint (together all 36). Verified.
2. **Propagation (§3).** With (a,b,c,d₀),(a,b,c,d₁)∈E, the pairs (a,b),(a,c),(b,c) are saturated. In cut AD|BC the columns (a,d₀) and (a,d₁) both contain row (b,c) and each has exactly one further E entry; two unitary columns cannot share exactly one nonzero row, so the second rows coincide: (a,b′,c′,d₀),(a,b′,c′,d₁)∈E with b′≠b, c′≠c by saturation. The same holds for the B and C coordinates. Uniqueness: any triple sharing value a with s at both D values sits in column (a,d₀), which is full. The closure S therefore has injective base-pair projections, exactly two triples per base value, and a simple 3-regular graph (three distinct partners, since equal partners would share two coordinates). Verified.
3. **All-cut isolation (§4).** In cut AB|CD the m rows (a,b) of S have both entries in columns C(S)×D₀ (m/2·2=m columns), and each column (c,d) is saturated by the two S-triples with C-value c; the same for AC|BD and AD|BC with the roles of the base coordinates exchanged. A unitary whose row/column sets split with no cross entries is block diagonal, so S×D₀ is an isolated m×m unitary and its complement a (10−m)×(10−m) unitary, each row/column still of degree 2. Verified.
4. **Ratio involution (§4).** For A-partners s,s′ in cut AD|BC, columns (b,c),(b′,c′) have the same two rows (a,d₀),(a,d₁); orthogonality u_{s,d₀}ū_{s′,d₀}+u_{s,d₁}ū_{s′,d₁}=0 gives r_{s′}=−1/r̄_s for r_s=u_{s,d₀}/u_{s,d₁}, a ratio that is cut-independent. f(r)=−1/r̄ is an involution; a fixed point needs |r|²=−1. Odd cycles are impossible, the graph is bipartite, a simple cubic bipartite graph has even order with ≥3 per side, and 2m≤20, so m∈{6,8,10}. Verified (numeric involution control also in receipt).
5. **m=10.** A proper 2-colouring assigns d₀/d₁ so that the two triples sharing any base value receive different D values; the 10 words are pairwise distinct in all six projections and share no cell with the 26 P words, so 36 words with six bijective pair projections form OA(36,4,6,2) ≡ two MOLS(6), contradicting Tarry. Verified (Tarry imported).
6. **m=8.** The complement has 4 words, every pair projection of size 2 with exactly two extensions each. A fibre varying in ≤1 other coordinate would give some pair with a single extension, so each fibre varies in ≥2 others; counting variations gives 2r≤3(n′−r) with n′=2, hence r≤1 for every coordinate, contradicting projection size 2. Verified by hand and by exhaustive binary brute force (`m8_complement_binary_bruteforce_hits`=0; {0,1}⁴ is exhaustive because size-2 projections force ≤2 symbols per coordinate).
7. **m=6.** n′=4 gives r≤2, no coordinate constant, so all four binary with full 2×2 projections; the complementary 4×4 block is unitary in all three cuts, so 3ψ restricted to E′ is a four-qubit state with all six two-qubit marginals maximally mixed. Spin-flip: weights 1,2 vanish by two-uniformity; purity Σr_P²=16; each three-qubit marginal has purity 1/2 so its weight-3 sum is 3, total 12; weight-4 sum 3; Y^{⊗4}P̄Y^{⊗4}=(−1)^{w}P gives Tr(ρρ̃)=(1−12+3)/16=−1/2<0 for a product of two positive operators. Verified; the sign identity was additionally checked numerically on random 4-qubit states (max error 1.4e-16). The receipt also records that **combinatorial** binary 8-word supports with the required projections do exist (10 of them), confirming the packet's point that only the unitary/spin-flip argument closes m=6.

No step uses the (4,4,4,4) assumption, so Candidate A holds for every alphabet profile at N=46, t=26.

## 4. Reconstruction of the normal form (packet §5–§6)

- Party-independent degree: every AB cell is either the unique cell of one P word or an E cell, so #P words at active symbol a equals 6−d_B(a)=6−d_C(a)=6−d_D(a). Fibre-variation gives d≥2; d≤4; Σd=10 over four active symbols ⇒ multisets X=(2,2,2,4), Y=(2,2,3,3) only. Verified.
- P counts: Σn_k=26, Σk·n_k=4(24−10)=56, ΣC(k,2)n_k=6(16−10)=36 have exactly the three non-negative solutions `(0,2,18,6,0),(0,1,21,3,1),(0,0,24,0,2)` (receipt `pcount_solutions`, exhaustive integer search). Verified.
- s−q−2h=2d−6 (6−d P words at a; 3(4−d) other-active incidences). d=4 ⇒ s≥2; n₁≤2 ⇒ at most one X party. Verified.
- Fibre shapes under Candidate A: degree-2 fibre = 4 points of a 2×2×2 box with each symbol twice and no adjacent pair ⇒ one of the two parity classes (the only maximum independent sets of Q₃), all projections full rectangles; degree-3 fibre = 6 points, each symbol twice, pair-injective; degree-4 fibre = 8 points, each symbol twice, pair-injective with 2-regular 4×4 projections. Verified.
- Reduction to BC/BD/CD: AB, AC, AD degree-2 conditions hold by fibre shape; the B-, C-, D-side degree equalities are automatic once each BC/BD/CD cell has multiplicity 0 or 2; with each fibre contributing 0/1 per cell, multiplicity∈{0,2} ⟺ (XOR = 0) ∧ (no cell in all four fibres). Verified — the search conditions are complete for the support problem, and the unitary obstruction is then applied to the resulting supports.

## 5. Independent exact enumeration (packet claims vs reviewer results)

| Claim (packet §6–§7) | Reviewer result (receipt key) |
|---|---|
| 34 labelled Y–Y graphs; 5 orbit representatives listed | 34; 5 orbits of sizes 4,4,8,16,2; the five listed tuples hit each orbit exactly once (`packet_YY_reps_check.complete_and_irredundant=true`) |
| 15 labelled X–Y graphs; 2 representatives listed | 15; 2 orbits of sizes 3,12; listed pair complete and irredundant |
| 144 six-point high fibres | 144 (`Y6_fibre_count`); each is uniquely determined by its three pair projections (`Y6_max_fibres_per_projection_triple=1`), so "projection signature" = fibre |
| 5·34·35/2=2,975 all-Y patterns → 10 signature pairs → 40 supports | 2,975 patterns; 10 high-fibre solutions = 10 distinct signature pairs; 40 pairwise-distinct supports, all passing an independent six-projection recount; all ten solutions occur under the representative `(02,13,023,123)` |
| All 40 fail by a row/column pair sharing exactly one nonzero in **each** of the three cuts | True for all 40 in all three cuts (`Y_all_supports_fail_in_every_cut=true`); e.g. the first support has rows (a,b)=(0,0),(2,2) in AB\|CD sharing only column (c,d)=(0,0) |
| 30 of 40 contain a cross-fibre distance-one pair; within-fibre none | 30 (20 supports with 3 such pairs, 10 with 6); within-fibre count 0 for all 40 |
| 2·15·16/2=240 one-X patterns → 10 graph triples → no pair-injective eight-point fibre | 240; exactly 10 patterns yield 2-regular required projections, forming 10 distinct graph triples; each has exactly 8 compatible (b,c,d) triples that are **not** pair-injective (6 distinct edges per projection); lookup against the full reviewer catalog of 67,824 eight-point fibres (67,500 distinct projection triples) finds 0 matches |
| (not claimed; reviewer extension) fully labelled runs | 34³=39,304 all-Y patterns: 128 high-fibre solutions, 512 supports, **all** fail in every cut; the 512 and the 40 occupy the same 3 classes under the full within-class relabelling and B/C/D permutation group; 15³=3,375 one-X patterns: 192 pass 2-regularity, 0 fibre matches |

Controls in the same run: recount of every found support against the six exactly-10-cells/exactly-2-extensions conditions; a one-word mutation of a found support is rejected by the recount; every catalog X-fibre is recovered from its own projections (lookup positive control); a known Y solution is re-found when re-solving its own pattern.

## 6. Observations (none rise to MINOR)

- The packet's "10 pairs of high-fibre projection signatures" is representative-dependent: the normalisation is a superset, not a canonical form (different orbit representatives could give a different count). The exclusion is unaffected; the fully labelled run above makes the conclusion independent of the choice.
- The nonvacuity control (packet §4, free six-row component) is not load-bearing for either candidate and was not re-run here; only its hashes were checked.
- The packet correctly says only Tarry is imported; the spin-flip and OA↔MOLS steps are self-contained as written.

## 7. What remains conditional or outside this review (explicit)

1. **Tarry's theorem** (no OLS(6)) — imported in the m=10 case; not reconstructed.
2. **The input `N=46, t=26`** — the packet does not establish that N=46 forces t=26; the separate t-pinning lemma referenced by the parent as the "t≤29 lemma" is not part of this packet and was not read or reviewed here.
3. **Alphabet profiles** — only (4,4,4,4) is excluded; any other N=46, t=26 profile (including whatever the parent calls the "three-excess" branch) is not covered. Candidate A itself is profile-independent.
4. **The ≥46 chain** — the ≥45 candidate and the remaining N=46 branches are not reviewed; this result is one branch input, not an adoption; **no global ≥47 (or ≥46) claim** follows.
5. **Verification family** — the author's two programs were neither read nor executed; agreement is between the packet's stated outcomes and this reviewer's independently written Python enumeration in the same harness. No formal/kernel, human, or independent-model-family verification exists. Novelty/priority not assessed.

## 8. Files written by this review (all under `review-waves/f127-ame-n46-noh1-standalone/`)

`noh1-independent-enum-v1.py`, `noh1-independent-enum-receipt-v1.json`, `noh1-review-v1.md` (this file), `noh1-review-receipt-v1.json` (hash/clock receipt binding the above).
