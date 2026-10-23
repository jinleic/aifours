# Slice B referee report: Corollary MID, Corollary TOP, and the I.14 coverage table

**Text of record.** v5 (`4e463746…cff1c`) read through:
- errata 1 (`512e1d9e…`), 2 (`b4451461…`) and 3 (`380106c9…`);
- erratum 4 (`32811de5…`), which governs SEG when Π_need < 0;
- erratum 5 Part I (`40832206…`).

Part II is not reviewed and is not used anywhere in this slice.

**Foundations.** Facts 2.1–2.2, ARC+, Lemma SEG, Lemmas 3.1/3.2, BAL, FP, K2P+ and ETA are taken as stated with I.1–I.11. All checks are by hand. I used no tools, ran no computation and made no edits. The hashes are as you supplied them; I did not recompute them.

## A. Disposition

**Overall: 0 FATAL / 0 MAJOR / 7 MINOR. No REJECT.**

| Target | Verdict | FATAL / MAJOR / MINOR | Findings |
|---|---|---|---|
| Cor. MID (+e3, I.12) | ACCEPT-WITH-FIXES | 0 / 0 / 2 | m1, m2 |
| Cor. TOP (+e4, I.15) | ACCEPT | 0 / 0 / 0 | remark R1 only |
| I.14, R = p table | ACCEPT-WITH-FIXES | 0 / 0 / 3 | m3, m4, m5 |
| I.14, R = p+δ bands | ACCEPT-WITH-FIXES | 0 / 0 / 2 | m6, m7 |

**Every requested check passes:**
- MID: λ₀ ≤ 3, |L∩O| ≤ 4, the rate dichotomy (base pair or a rate-two first segment), Σt ≤ Π_need−1, and every m in [m_lo, m_hi].
- TOP: the pair plus designated singleton for odd and even |M_l|, the exact count 2m₀, the pair-loss bound and the Π_need+2 budget.
- Every table cell at p = 5, 7 and 11, and the general integer endpoints.

**Repairs that change use in the target.**
- I.7/e2 changes how MID's parity moves are justified (m1).
- Erratum 4 changes how I.14's conditional SEG clause must be read (m7).
- I.1–I.6, I.8–I.11 and I.13 make implicit steps explicit, and MID, TOP and I.14 satisfy the added side conditions.

**No hypothesis-dependent result becomes universal coverage.** Theorem SEG, Theorem FP and FP-1 are never used that way. SEG-p and SEG-num verify SEG's hypotheses for every word in their cells, with Π_need ≥ 1.

**Accepted scopes.** Every claim carries the ambient setting (S): length 4p−2, rotations in one pair, all maximal constant reflection blocks odd, any B.
- **MID:** words with R = p, κ = (p−1)/2 and p ≥ 11 have an identity 2p-subword.
- **TOP:** the same holds for R = p, κ ∈ {p−2, p−1} and p ≥ 7. The same proof also covers (p, κ) = (5, 4).
- **I.14:** the R = p table is exact as the file's universal coverage, and the two R = p+δ bands are correct.

## B. Findings (all MINOR) and minimal repairs

**m1 (MID, read with e2 and I.7).** e2 says MID's change rule "is a special case" of e5. For AB-runs it is not:
- Removing a base pair-arc (c_j: 1→0) is not one of e5's moves.
- Adding a pair-arc (c_j: 0→1) is not one of e5's moves either.
- e5 offers only: delete a singleton, add a singleton, split a pair.

The moves are still valid. Each toggles c_j and so flips its parity, and BAL and Lemma 3.1 use only parities. MID never uses e5's pair-loss accounting, because it counts gain after balancing. The same applies to Theorem SEG.

*Repair:* replace "is a special case" with "toggles c_j between 0 and 1 (one whole base arc), which flips its parity; this is all BAL uses; e5 is not invoked."

**m2 (MID).** Choosing O₀ needs N_O ≤ q = p, which is equivalent to λ₀ ≤ |L|. That inequality (N_O = p+3−2r ≤ p−3) appears only later, inside e3.

*Repair:* state it at the choice of O₀.

**m3 (I.14).** The Sec. 8 "Remaining" bullet for R = p reads "κ < (p+1)/4; p = 7, κ = 3". It is not on I.14's list of superseded items, and it omits (5,2) and (5,3), because at p = 5 the condition κ < 3/2 is empty.

*Repair:* add that bullet to I.14's supersession list, so that I.14's right-hand column becomes the remaining list.

**m4 (I.14).** The "FP-1 diversity only" annotation appears only for (5,2) and (7,3). Yet FP-1's condition (K), κ ≤ (p−3)/2 + r, also holds at every other non-excluded R = p cell except (5,3), for example (11,2) and every cell with 2 ≤ κ < ⌈(p+1)/4⌉. This is not an overclaim, but the table implies a status difference that does not exist.

*Repair:* add one note: "under its diversity hypothesis, FP-1 excludes words in every non-excluded R = p cell except (5,3)."

**m5 (I.14).** The (5,4) cell is credited to the "TOP argument (e7)", but TOP is stated only for p ≥ 7. The argument does go through (see C3).

*Repair:* state TOP for "p ≥ 7, or (p, κ) = (5, 4)".

**m6 (I.14, R = p+δ).** The clause "or the FP-1 diversity conditions" is vacuous for δ ≥ 1, because FP-1 requires exactly R = p. Read as the diversity inequality alone, it is unsupported.

*Repair:* delete the clause.

**m7 (I.14, R = p+δ).** For R ≥ 2p+1, "the hypotheses of Theorem SEG" are governed by erratum 4: (H1′), (H2) and (H3′). The printed (H1) would need Part II there.

*Repair:* append "(for R ≥ 2p+1: erratum 4's (H1′), (H3′); Part II not used)".

**R1 (TOP; a remark, not a finding).** The bound "at most two pairs lost" is valid but not sharp. e5 has no move that both lowers the arc count and loses a pair, so the two compensating moves lose at most one pair (see C3). One unit of the Π_need+2 budget is therefore slack. Any use of that slack, for example at (5,3), would be a new claim needing its own review. It is not credited here, and I.14 correctly leaves (5,3) open.

## C. Proof checks

### C1. Shared data at R = p

**Runs.**
- Fact 2.2 with δ = 0 gives at most one letter per run.
- (P0) gives o_R ≥ k − 2κ = p.
- Hence q = p one-letter runs and every other run is empty.

**Derived quantities.**
- g_E = 2κ and k = p + 2κ.
- d = 1, and T is odd.
- r = ⌈(p−1)/4⌉ = ⌊(p+1)/4⌋.

**Windows.**
- For E ∈ {(p∓1)/2}, min⌈E/2⌉ = max⌊E/2⌋ = r.
- The window sum is (p−1)/2 = Π_need.
- Fact 2.1 holds exactly when κ+1−r ≤ m ≤ p−r.
- Since ⌈(R−d)/4⌉ = ⌊(R+d)/4⌋ = r, we get m_lo = m₀ and m_hi = m₁.

### C2. MID (κ = (p−1)/2, p ≥ 11)

**Parameters.**
- H = Π_need = (p−1)/2, k = 2p−1 and g_E = p−1.
- m_lo = (p+1)/2 − r = a+1 ≥ 1 for p = 4a+1 or 4a+3, so there is no truncation.
- m_hi − m_lo = Π_need.
- N_O = p+3−2r ≤ p−3, since r ≥ 3 for p ≥ 11.

**λ₀ ≤ 3.**
- Every L-run has e ≥ 2, so |L| ≤ (p−1)/2 and n_CA ≥ (p+1)/2.
- So λ₀ ≤ (p+5)/2 − 2r, which equals 3 when p ≡ 1 and 2 when p ≡ 3 (mod 4).
- N_O ≤ p gives λ₀ ≤ |L|, so O₀ exists.
- O₀ contains min(N_O, n_CA) ≥ 1 runs from C∪AB, so a valid i exists.

**BAL removals and |L∩O| ≤ 4.**
- Σc = N_O is even and ≥ 4.
- The change at i removes one base arc. The change at i′ ≠ i removes or adds one whole base arc.
- So |O| ∈ {N_O−2, N_O} and m_b ∈ {m_lo, m_lo+1}.
- |T| ≤ 1 and T odd give |T| = 1, hence E^± = (p∓1)/2.
- L-runs enter O only through O₀ (λ₀ of them) or as i′ (at most one), so |L∩O| ≤ λ₀+1 ≤ 4.

**Capacity.** Each run contributes:

| Run type | Contribution |
|---|---|
| AB-run in O | 1 (base pair) |
| AB-run not in O | 1 |
| L-run not in O | e_j |
| L-run in O | e_j − 1 |
| C-run | 0 |

- The total is g_E − |L∩O| ≥ p−5.
- p−5 ≥ Π_need+1 holds exactly when p ≥ 11.
- Since b′−1 ≤ e_j ≤ p−1, the cap p−1 in g(t) never cuts capacity.

**Rate dichotomy (exhaustive).**
- **Case A: AB∩O ≠ ∅.** Every AB-run in O carries a base pair-arc, so G_b ≥ 1.
- **Case B: AB∩O = ∅.** O₀ held min(|AB|, N_O) AB-runs with N_O ≥ 4, and BAL removes at most two of them, so |AB| ≤ 2.
  - **B1: some L-run lies outside O.** Its segment is the whole M_j, with at least 3 blocks, so g(1) = 2.
  - **B2: every L-run lies in O.**
    - Suppose λ₀ > 0. Then |L| ≤ λ₀+1 = N_O−p+|L|+1, which forces N_O ≥ p−1. That contradicts N_O ≤ p−3. So λ₀ = 0 and L ⊆ {i′}.
    - |L| = 0 would give |AB| = g_E = p−1 > 2, which is impossible.
    - So |L| = 1, with e_j = g_E − |AB| ≥ p−3 ≥ 8. The segment M_j minus its first block has e_j ≥ 3 blocks, so g(1) = 2.

**Loop (I.12) and Σt ≤ Π_need−1.**
- While the certified gain is below Π_need ≤ (p−1)/2 < p−1, an unsaturated j exists, because the saturated total equals capacity ≥ Π_need+1.
- Each raise adds at least 1: g_j(t_j) = 2t_j < b′_j−1 gives g_j(t_j+1) ≥ 2t_j+1.
- Case A needs at most Π_need−1 raises.
- In Case B, the first raise goes to the segment with at least 3 blocks and adds 2; at most Π_need−2 further raises follow.
- Either way Σt_j ≤ Π_need−1.

**Range.**
- Every configuration has m ∈ [m_b, m_b+Σt] ⊆ [m_lo, m_lo+Π_need] = [m_lo, m_hi].
- By I.5 it suffices to check the endpoints: r ≥ κ+1−m and r ≤ p−m.
- The window sum (p−1)/2 plus gain Π_need gives p−1, so Lemma 3.2 applies.

**Edge case p = 11.** r = 3, m_lo = 3, m_hi = 8, N_O = 8 = p−3, λ₀ ≤ 2, capacity ≥ 7 ≥ 6, Σt ≤ 4, so m ≤ 8.

### C3. TOP (κ ∈ {p−2, p−1})

**Parameters.**
- H ∈ {1, 0} and k = p+2κ.
- g_E = 2κ ≥ 2p−4 > p for p ≥ 5, so some |M_l| ≥ 3.
- m₀ = κ+1−r ≥ 1, and m₁ − m₀ = H.

**Pair plus designated singleton (e4, I.15).** Σ⌊|M_i|/2⌋ = κ + o/2, where o, the number of odd e_i, is even because o ≡ g_E.
- *|M_l| odd:* the leftover block holds the singleton beside ⌊|M_l|/2⌋ ≥ 1 pairs, and the total stays ≥ κ.
- *|M_l| even (so ≥ 4):* e_l is odd, so o ≥ 2. Giving up one of M_l's (at least two) pairs leaves at least κ pairs overall and at least one in M_l.

**Budget.** g = Π_need+2 = (p+3)/2 ≤ p−2 ≤ κ, valid for p ≥ 7.

**Exact count 2m₀.**
- 2m₀ − g = (4κ+1−4r−p)/2 ≥ (3p−7−4r)/2 ≥ p−4 ≥ 3, using 4r ≤ p+1.
- The blocks used number g + 2m₀ = k + (7−p−4r)/2 ≤ k. I re-derived this identity independently.

**Balancing at i = l.**
- e5 applies at i′: the choice uses only singletons and pairs, and M_{i′} has at least one block.
- The compensating move at l flips c_l and keeps the count at exactly 2m₀.
- Pair loss, by case (ε′ is the change in arc count at i′):

  | ε′ | Move at i′ | Pairs lost at i′ | Move at l | Pairs lost at l | Total |
  |---|---|---|---|---|---|
  | −1 | delete singleton | 0 | split designated pair | 1 | 1 |
  | +1 | add singleton | 0 | delete designated singleton | 0 | 0 |
  | +1 | split pair | 1 | delete designated singleton | 0 | 1 |

- So at most one pair is lost (≤ 2 as stated), and at least Π_need pairs survive.

**Close.**
- m = m₀ and |T| = 1.
- Fact 2.1 holds at m₀; at κ = p−1 both inequalities hold with equality.
- The window (p−1)/2 plus gain Π_need gives p−1, so ARC applies.

**Spot checks.**

| (p, κ) | r | m₀ | m₁ | k | g | 2m₀+g | Fact 2.1 at m₀ |
|---|---|---|---|---|---|---|---|
| (7, 5) | 2 | 4 | 5 | 17 | 5 | 13 | ✓ |
| (7, 6) | 2 | 5 | 5 | 19 | 5 | 15 | ✓ |
| (5, 4) via e7 | 1 | 4 | 4 | 13 | 4 | 12 | ✓ (1 ≥ 1, 1 ≤ 1); g_E = 8 > 5 |

At (5, 3), g = 4 > κ = 3, so the printed budget fails and the cell is correctly left open.

### C4. I.14 at R = p (κ ∈ {2, …, p−1}, k = p+2κ)

**Bands.**

| Result | κ range |
|---|---|
| SEG-p | ⌈(p+1)/4⌉ ≤ κ ≤ (p−3)/2 |
| MID | κ = (p−1)/2, with p ≥ 11 |
| K2P+ | (p+1)/2 ≤ κ ≤ p−3 (vacuous at p = 5, by e2) |
| TOP | κ ∈ {p−2, p−1} for p ≥ 7, plus (5, 4) |

The K2P+ row comes from k ≥ 2p+1 ⇔ κ ≥ (p+1)/2 and k ≥ 3κ+3 ⇔ κ ≤ p−3.

**SEG-p's hypotheses hold for every word in its band.** Here m_lo = κ+1−r ≥ 1 and Π_need ≥ 2.
- (H1): p−1−κ ≥ (p+1)/2.
- (H2): n_CA ≥ p−κ ≥ 2κ+4−2r, which needs κ ≤ (p−3)/2 and 2r ≥ (p−1)/2.
- (H3): 2κ ≥ (p+1)/2.

**Cells.**

| p | κ | Result | Check |
|---|---|---|---|
| 5 | 4 | TOP proof (e7) | See C3 |
| 5 | 2 | FP-1, conditional | (K) gives κ ≤ 2 ✓ |
| 5 | 3 | Open | (K) fails |
| 7 | 2 | SEG-p | (H1) 4 ≥ 4; (H2) n_CA ≥ 5 ≥ 4; (H3) 4 ≥ 4 |
| 7 | 4 | K2P+ | k = 15 = 2p+1 = 3κ+3 |
| 7 | 5, 6 | TOP | See C3 |
| 7 | 3 | FP-1, conditional | (K) gives κ ≤ 4 ✓; MID needs p ≥ 11 |
| 11 | 3 | SEG-p | m_lo = 1; (H1) 7 ≥ 6; (H2) 8 ≥ 4; (H3) 6 ≥ 6 |
| 11 | 4 | SEG-p | m_lo = 2; (H1) 6 ≥ 6; (H2) 7 ≥ 6; (H3) 8 ≥ 6 |
| 11 | 5 | MID | See C2 |
| 11 | 6–8 | K2P+ | k = 23, 25, 27 against 3κ+3 = 21, 24, 27 |
| 11 | 9, 10 | TOP | See C3 |
| 11 | 2 | Open universally | — |

At (5,2), (5,3) and (7,3), Theorem SEG adds nothing, because (H1) fails: H < Π_need+1.

**General p ≥ 11.**
- The bands abut with no gap: (p−3)/2 | (p−1)/2 | (p+1)/2 … p−3 | p−2.
- The SEG-p band is nonempty exactly when p ≥ 11.
- For 2 ≤ κ < ⌈(p+1)/4⌉, (H3) fails for every word, because g_E = 2κ < (p+1)/2. Only FP-1 and FP give conditional exclusions there.

### C5. I.14 at R = p+δ, δ ≥ 1

**K2P+ band.** With k = p−δ+2κ, the band is ⌈(p+δ+1)/2⌉ ≤ κ ≤ p−δ−3, exactly.

**SEG-num band.** This is the corollary's statement read in integers, per I.13. Since 5δ ≤ p−10, R ≤ 2p−2 and so Π_need ≥ 1. Endpoint recheck:
- (H1): p−1−κ−δ ≥ (p−δ)/2+1 ≥ Π_need+1.
- (H3): 2κ−2δ ≥ (p−δ)/2+1.
- (H2): (3q−k)/2 ≥ p−δ−κ ≥ 2κ+4−(p−δ−1)/2 ≥ 2m_lo+2.

**Remainder.** The clause about further exclusions is conditional and correct once m6 and m7 are applied.

## D. Open

**Open problems.** REFL(p), REFL-HI(p), RES-HI(p), the reflection half of INV*(p), INV*(p) and ordered Olson for D_(2p) all remain open.

**Open cells.**
- At R = p:
  - p ≥ 11 with 2 ≤ κ < ⌈(p+1)/4⌉;
  - (5,2) and (7,3), excluded only under FP-1's diversity hypothesis;
  - (5,3), open.
- At R ≥ p+1, everything outside the two bands.

**Not reviewed.** Part II is not reviewed. Erratum 4 still governs SEG when Π_need < 0. I make no novelty or priority claim. Separately accepted sequence-level Olson cells are unaffected.
