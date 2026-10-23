# Olson reflection: Lemma EDGE, extended B0S-CJ and extended REFL-B0, parent verdict v1

Recorded at 2026-10-18T13:15:59-07:00.

**CORRECTNESS-ACCEPTED as written partial theorems relative to the imported B = 0 framework, with the overlay below.** The hypothesis 2κ ≤ p−1 can be dropped from the accepted equal-rotation results. Exactly two new cells per prime are added: κ = (p+1)/2 with R ∈ {2p−2, 2p−1}. Partial results on the B = 0, equal-nonidentity-rotation slice only. No full REFL(p), INV*(p) or ordered-Olson claim; no novelty claim; no Lean; no human peer review.

## Text of record

- [EDGE r2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0Sedge-r2.md), SHA256 `ac2de0d299849aa50e733fbe01deb2448bfa19f8e67f33137daa0a2459a70ba3`, read through this verdict's overlay.
- Upstream accepted scopes: [REFL-B0 parent verdict](olson-refl-b0-parent-verdict-v1.md), SHA256 `7f1041bd07d3fe66581ad67752dea9385bd3510975a5661f060c8fe38cc35ddb` (text r3 `c05eb383…2272`), and the [CJ/CJx parent verdict and overlay](olson-cj-cjx-parent-verdict-v1.md), SHA256 `5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d`.

## Exact accepted statements

Setting: an avoider of length 4p−2 over D_2p, p ≥ 5 prime, B = 0, after the standard normalization and the trivial cut R ≤ 2p−1, with F, R ≥ 1, genuine empty runs and rotations normalized to ρ_1 (Claude E4/E5).

1. **Lemma EDGE.** No such word with all blocks odd has κ = (p+1)/2 and R ∈ {2p−2, 2p−1}.
2. **Theorem B0S-CJ'''' (extended CJ).** Theorem B0S-CJ''' holds with its hypothesis (H''') replaced by R ≥ 4κ−4 alone, read through the CJ overlay: "nonempty" in Corollary 1; only the first two sentences of Corollary 2, with the shortcut 4Δ ≤ 2κ+2; no wholesale strengthened p ≤ 23 conclusion. The other CJ conditions (Δ ≤ 0, or two disjoint heavy admissible intervals) are retained. The new range is exactly the two edge cells per prime, each with Δ ≤ −1.
3. **Extended REFL-B0.** The accepted REFL-B0 statement holds without the hypothesis 2κ ≤ p−1. Every other hypothesis is kept: equal non-identity rotations, R ≥ 4κ−4 and 5R ≥ 4p+6κ−10 (the alternative R ≥ p+κ−2 implies the latter because κ ≤ p−1). No initial block-parity or o_F ≤ p assumption is added. The new initial cells are κ(w_0) = (p+1)/2 with R ∈ {2p−2, 2p−1}; there o_F(w_0) = 3p+1−R ∈ {p+3, p+2} > p, so they lie entirely outside the fewodd range.

## Hostile reviews

| Reviewer | Note | Result |
|---|---|---|
| Codex gpt-6.1-sol | [note](olson-reflection-edge-r2-codex-v1.note.md), SHA256 `237d0950af926e9dcda3b2f94f877032ecd02d8f46b51cb6259afadb6420cdda` | EDGE ACCEPT; extended CJ ACCEPT; extended REFL-B0 ACCEPT. No new FATAL/MAJOR/MINOR; two inherited REFL-B0 r3 wording MINORs. All 11 snapshot hashes matched. |
| Claude claude-opus-5-5 | [note](olson-reflection-edge-r2-claude-v1.note.md), SHA256 `cc2e4db045e0f91586ddb96b42ab3f02611f3fe54ab7f4edf12b2b79b7fc2496` | EDGE ACCEPT-WITH-FIXES 0/0/5 (E1–E5); extended CJ ACCEPT-WITH-FIXES 0/0/1 (C1); extended REFL-B0 ACCEPT-WITH-FIXES 0/0/3 (R1–R3). No counterexample; every kill re-derived from the six H0 inequalities. |

## Independent parent derivation

The parent read the complete EDGE text and re-derived the new mathematics from the six H0 conditions, written with x = (ρ−δ)/2: U1 x ≤ p−m, U2 x ≤ ρ+m−κ−1, U3 x ≤ ⌊ρ/2⌋, and the mirrors L1–L3 with ρ replaced by R−ρ. Equivalently U1: Φ−2δ ≤ 2p; U2: Φ ≥ 2κ+2; U3: δ ≥ 0; L1: Φ−2ρ ≤ 2p; L2: Φ−4m ≤ 2R−2κ−2; L3: δ ≤ R−[R−ρ odd], where Φ = ρ+2m+δ.

- **Edge facts.** Δ = p+κ−1−R ≤ (3−p)/2 ≤ −1, k = 3p+1−R ∈ {p+3, p+2}, 4κ = 2p+2. g(R) = min(R−κ, ⌊R/2⌋) = p−1, so a singleton empty run has gap [1−κ, 0] and genuineness forces x_t ∈ [1−κ, −1]: every empty run is a defect. For a defect, x_t ≤ ⌊r_t/2⌋ and x_t ≥ g(r_t)+1 give c_t = r_t+δ_t = 2(r_t−x_t), even, in [2, 2κ−2] (derivation as in B0SPP-r5 lines 99–102, Claude E3).
- **(K1).** For P ⊆ Z proper with 2κ+2 ≤ Φ ≤ 2p: U2 by assumption, U3 since δ ≥ 0, U1 and L1 since both left sides are ≤ Φ ≤ 2p, L2 since Φ−4m ≤ 2p−4 ≤ 2R−p−3 (2R ≥ 4p−4), L3 since δ ≤ 2p−2−ρ, which is R−[R odd] at ρ = 0 and ≤ 2p−3 ≤ R−1 at ρ ≥ 1.
- **(K2).** Two non-adjacent defects with Φ = 2p+2: U1 ⟺ δ ≥ 1, L1 ⟺ ρ ≥ 1, L2: 2p−6 ≤ 2R−p−3, L3: δ = 2p−2−ρ.
- **(K3).** For an empty defect t with x_t = 1−κ and a non-adjacent non-defect y: δ = p−1−bh_y, Φ = p+3+r_y−bh_y. Then U2 ⟺ x_y ≤ r_y, U3 ⟺ bh_y ≤ p−1, U1 ⟺ x_y ≤ (3p−5)/2; L1 holds because x_y ≥ 1; L2 ⟺ r_y−x_y ≤ R−p+1, whose failure would force r_y ≥ 2R−2p+5 ≥ 2p+1 > R; L3 since δ ≤ p−2.
- **Step 1.** An inclusion-maximal P′ ⊆ Z with Φ(P′) ≤ 2κ is nonempty and proper. Adding any outside defect gives Φ ∈ [2κ+2, 4κ]; below 4κ, K1 kills. Equality forces Φ(P′) = 2κ, c_t = 2κ−2 and non-adjacency. Exchanging an end defect e gives Φ = 4κ−c_e (interval of length ≥ 2) or 4κ−2−c_e (singleton), killed by K1 unless e is a singleton with c_e = 2κ−2; then 2κ = Φ(P′) = 2κ|P′| gives P′ = {e}. Every other {t} is also inclusion-maximal: Φ({t}) = 2κ, and adding t′ raises Φ by at least c_t′ ≥ 2 because joining two intervals is impossible with one interval (Claude E2). So all defects are pairwise non-adjacent with c = p−1, and |Z| ≥ 2.
- **Step 2.** For a pair, δ = 2p−2−ρ and Φ = 2p+2. K2 kills unless ρ = 0 or ρ ≥ 2p−2; with each r ≤ p−1, either every defect is empty (EB) or every defect has r = p−1 (FM).
- **Step 3 (FM).** R ≥ |Z|(p−1) forces |Z| = 2, so Σ_Y bh = 2p−R ≤ 2, while |Y| = k−2 ≥ p non-defects each have bh ≥ 1.
- **Step 4 (EB, |Z| ≥ 3).** Three empty defects: m = 3, window [−g_3(R), g_3(0)] = [3−p, 2−κ] (κ ≥ 3), and x(P)+p = 3−3κ+p = 2−κ, the top endpoint. The H0 test is modulo p, so this kills.
- **Step 5 (EB, |Z| = 2).** Every run of Y is nonempty; N_+ = 3p−1−R and Σ_Y bh = 4p−2−R. At most one y_0 is adjacent to both defects (k ≥ 7). Every other y violates (a), (b) or (c), so bh_y ≥ r_y+2 if r_y ≤ p−2 and bh_y ≥ p−3 if r_y ≥ p−1; at most two runs are big. With S = big runs ∪ {y_0}, |S| = b+e: M_S ≤ 2R−3p+1+|S| ≤ p−1+|S|, and summing bh gives M_S ≥ 2p−2|S|+b(p−3)+e. Hence 2e ≥ p+1+b(p−6), impossible for b = 0, 1, 2 and p ≥ 5.
- **Corollary.** R ≥ 2p is killed by ρ_1^(2p). If 2κ > p−1 then 2κ ≥ p+1, and 4κ−4 ≤ R ≤ 2p−1 gives 2κ ≤ p+1. So 2κ = p+1 and R ∈ {2p−2, 2p−1}: exactly the edge cells.
- **REFL-B0 transfer.** The accepted normalization keeps R and does not increase κ; the terminal word has B = 0, all blocks odd, genuine empty runs and 2 ≤ κ′ ≤ κ, with R ≥ 4κ′−4. If 2κ′ ≥ p+1 it is an edge cell, excluded by EDGE; otherwise the accepted argument applies verbatim. The corrected corollary then forces Δ′ ≥ 2 and 5R < 4p+6κ′−10 ≤ 4p+6κ−10, contradicting the retained hypothesis.

Imported, interfaces checked only: the H0 instance and residue-class kill test; P0; Lemma C1; the six-condition equivalence; the Case II construction of B0S-r4 Section 5 (its numerical conditions were re-checked in the edge cells: L3 δ ≤ p−1 ≤ R−1, U1, L1 4κ−4 = 2p−2 < 2p, L2 both branches, |F| ≥ d/2 from k ≥ p+2); the CJ items 2–5 (windows, C2(a), C2(b), SIGMA-2P), which both reviewers confirmed use only R ≥ 4κ−4, R ≥ p and R ≤ 2p−1; RED, K0*, K1* and the small-k verdict.

## Mandatory overlay (disposition of all findings)

1. **E1** (F4 trichotomy): the fourth case, t adjacent on both sides to the same interval, would give P∪{t} = [k], impossible inside Z ⊊ [k].
2. **E2** (EDGE line 86): the inclusion-maximality of each other singleton is proved as above.
3. **E3** (defect bound citation): cite B0SPP-r5 lines 99–102 (x_t := w_t in the singleton gap), not B0S-r4 (2.1), whose prefix-lift facts assume k ≤ p and fail in the edge cells.
4. **E4/E5** (standing assumptions): F, R ≥ 1; normalization to ρ_1; genuine empty runs; the trivial cut R ≤ 2p−1; κ ≥ 1; avoidance. The uses of 2κ ≤ p−1 in the imported texts are: Case I U1/L1 through Φ ≤ 4κ ≤ 2p (replaced by EDGE); CJ (F2), used only when Δ ≥ 1; and the B0S++ corollary, used only when Δ = 1. Only the first is live in the edge cells.
5. **C1** (extended CJ scope): read through the CJ overlay as in statement 2. The p ≤ 23 claim is not extended. Earlier wording that keeps 2κ ≤ p−1 is superseded only by this verdict, at these scopes.
6. **R1** (transfer written only as a parenthetical): the transfer is accepted as derived above. Read REFL-B0 r3 line 17 without "2κ ≤ p−1", and its line 47 as "R ≥ 4κ′−4, so B0S-CJ'''' applies; 2κ′ ≥ p+1 is an edge cell, excluded by EDGE".
7. **R2** (stale remark): at p = 7, κ = 4 is now covered for R ∈ {12, 13}; κ ≥ 5 is excluded because 4κ−4 > 2p−1.
8. **R3 and the Codex inherited MINORs**: REFL-B0 r3 lines 42–43 read "the next block, of either parity"; lines 63–64 read "P3 preserves R, B, κ, while P4 changes them". The earlier review MINORs remain as disposed in the REFL-B0 verdict.
9. **Label**: B0S-CJ'''' at EDGE line 16 means CJ''' with (H''') replaced; the title's ''' is a typographic mismatch.

The finite aid E15b (0 avoiders in the two p = 7 edge cells) is not a premise.

## Boundary

Written mathematics relative to the imported, parent-accepted B = 0 framework. No Lean, Comparator or independent kernel; no human peer review; no priority or novelty assessment. The original all-groups ordered Olson target, full REFL(p) and INV*(p) remain open.
