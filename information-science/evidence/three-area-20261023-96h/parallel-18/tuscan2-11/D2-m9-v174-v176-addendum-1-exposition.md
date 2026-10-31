# Addendum 1 to v174 and v176 (exposition only; the pinned files are unchanged)

NEW exact WRITTEN ADDENDUM (owner InfoRecursiveMDS18-2, slot info-4). Errata-not-edits: the files below remain as pinned. This addendum fills one justification step and corrects one attribution. No claim changes.

**Pinned files concerned:**
- `D2-m9-L1-type7-r2eq3-n1eq1-forced-shape-alphaII-and-wide-alphaI-closed-v174.md`, SHA256 `b213df8f4eac9cd80331d6f93c56175d0bc67915e5d19c3d92c9575a70054e40`;
- `D2-m9-L1-lemmaA4-arm-exactness-u-ge-4-type7-formb-closed-v176.md`, SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`.

## 1. v174 §2: why P2 ≤ 39 and P3 ≥ 41

v174 §2 states P2 ∈ [31, 39] and P3 ∈ [41, 49], but it only spells out the case P2 = 40. The full justification is as follows.

**Bounds on P2.**
- P2 ≥ 41 is impossible. Then P3 ∈ (P2, 49] by §1, so the two b6-corners P2 and P3 both lie in R4, and v occurs twice in R4.
- P2 = 40 makes it v's cut. The later passage P3 then falls in R5, against P3 ≤ 49.

**Bounds on P3.**
- P3 ≤ 39 would put P2 and P3 together in R3.
- P3 = 40 would be v's cut, with P2 also in R3, so v would occur twice in R3.

The rest of §2 is unchanged.

## 2. v176 §2: attribution of the u = 2 skeleton

checkpoint-220 recorded only the parameters of the pinned form-(b) skeleton (ℓ1 = 14, ℓ3 ∈ {9, 10}, …). The full row-level label placement for u = 2 was carried out afterwards, in in-session written reasoning:
- t1 = c5, c1, {w, X40, Z2, X50}, Z3, {v, c5, Z1, X30}, X20, X50;
- t2 = {c1, c5, Z2, Z3}, X50, {w, X20, Z1}, X30, {c1, c5, X40, Z2, Z3}, v, Z1;
- t3 = c1, c5, {X20, X30, X50, Z3}, Z2, {c1, X40};
- Λ = {X20, X30}, Z1, w, X40.

This placement meets every row condition of F1 and F2 used in v172–v174. It fails (E): t1[1]t1[2] and t3[1]t3[2] both join c1 and c5, exactly as Lemma A4 predicts.

This addendum is written reasoning only and needs its own source-bound gate.
