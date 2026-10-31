# Original Tuscan-2(11), entire m = 9 distance-two branch, part 4: the extended overlap lemma, length thresholds for double-passed paths, and L2 type A with b = 3 reduced

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-double-pass-lemma-typeA-b2-excluded-v114.md` (SHA256 `e5b74dd0bb1a4064811de2578b9fcc607a6d89c9a09e89c8cec90dd0c15ee4d0`), and the notation is that of v114.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only; distance two (R3) is not needed.

## 1. Extended overlap lemma (OL)

**Set-up.** Let θ have interior θ[1..L−1]. Its forward cuts sit at indices ≡ φ and its backward cuts at ≡ φ + ρ (mod 10), as in v114 §2. Every row is a window of 11 consecutive face positions. A window may run past the ends of θ:
- beyond index 0 it runs through the branch at that end into the neighbouring half-edge of the same pass;
- beyond index L it does the same at the far end.

Such a window is still a path of H, because a row never crosses the leaf ℓ, which sits on a cut.

**Lemma OL.** Let F = [s, s+10] be a forward row (s ≡ φ) and G a backward row. Suppose their common index set is a segment lying inside [1, L−1]. Then the two differences are paths, and they carry equal label sets.

There are two shapes:
- **B-shape:** G = [s+ρ, s+ρ+10]. This needs s ∈ [1−ρ, L−11]. The differences are F's low part [s, s+ρ−1] and G's high part [s+11, s+ρ+10].
- **C-shape:** G = [s+ρ−10, s+ρ]. This needs s ∈ [1, L−1−ρ]. The differences are F's high part [s+ρ+1, s+10] and G's low part [s+ρ−10, s−1].

Each difference may extend beyond θ.

**Consequences.** These assume the two difference paths share no edge, which holds whenever they lie in different regions of H; it is checked in each use.
- A difference of size 1 puts one label on two cut positions, against v114 (C). This includes the case where b4 is on a cut.
- A difference of size 2 or 3 repeats a label pair, against v114 (E).
- Lemma DP-2 applies to two consecutive differences of size 4 or 5.

**Thresholds.** A residue class mod 10 always meets an interval of length at least 10. This gives:

| ρ | Kill window for s ≡ φ | Every φ is killed once L ≥ |
|---|---|---|
| 0 | [1, L−1] (forward cut = backward cut) | 11 |
| 1, 2, 3 | [1−ρ, L−11] | 20, 19, 18 |
| 4 | [−3, L−21] (B-chain) | 27 |
| 5 | [−4, L−21] ∪ [1, L−16] (B- or C-chain) | 21 |
| 6 | [1, L−17] (C-chain) | 27 |
| 7, 8, 9 | [1, L−1−ρ] | 18, 19, 20 |

**So every thread or loop of length L ≥ 27 is impossible. For L ≥ 21, only ρ ∈ {4, 6} can survive.**

## 2. The arm threads, and the relations among the ρ's (L2, k = 3)

**Corner offsets.** Write q for a branch corner's position mod 10, measured in its face's cut grid. At b4 the corners and their offsets are:
- (T→t1) at offset t;
- (t1→t2) at offset q12;
- (t2→t3) at offset q23;
- (t3→T) at offset u.

**The ρ's at b4.**
- t1: φ ≡ u and ρ1 = t + q12.
- t2: φ ≡ −q12 and ρ2 = q12 + q23.
- t3: backward cuts ≡ u and ρ3 = q23 + u.

Hence ρ2 ≡ ρ1 + ρ3 in every type. Also ρ1, ρ3 ≠ 0: t1[u] and t3[u] already carry one cut passage each, and a second would put two cut passages on one vertex.

**Relations at b5.** Write the rotation at b5 as (Λ+, t_x, Λ−, t_y, t_z), and let a1..a5 be the offsets of its corners (Λ+→t_x), (t_x→Λ−), (Λ−→t_y), (t_y→t_z), (t_z→Λ+). Then:
- ρ(t_x) = a1 + a2, ρ(t_y) = a3 + a4, ρ(t_z) = a4 + a5, ρ(Λ) = a2 + a3;
- a1 ≡ a2 + λ and a3 ≡ a5 + λ;
- no a_i is 0, since b5 is never on a cut.

Combining these with the b4 relation gives:
- **Type A:** a2 = 5.
- **Type B:** a1 = 5.
- **Types C and E:** a2 ≡ a4 + a5 (mod 5).

**Arm conditions** (OL with s ∈ {u − 10, u, u + 10}). Here s = u − 10 makes F = R_out. Thread t1 is killed when:

| ρ1 | t1 is killed if |
|---|---|
| 1 | ℓ1 ≥ u+11 |
| 2 | u ≥ 9 or ℓ1 ≥ u+11 |
| 3 | u ≥ 8 or ℓ1 ≥ u+11 |
| 4 | (u ≥ 7 and ℓ1 ≥ u+11) or ℓ1 ≥ u+21 |
| 5 | (u ≥ 6 and ℓ1 ≥ u+11) or ℓ1 ≥ u+16 |
| 6 | ℓ1 ≥ u+17 |
| 7, 8, 9 | ℓ1 ≥ u+1+ρ1 |

For t3, row reversal (v114 §1) gives the same table with ρ1 replaced by 10 − ρ3 and ℓ1 by ℓ3.

**v-gaps.** Along a face, consecutive v-passages lie in consecutive rows. So a face segment between two v-passages with n further v-passages inside has length in [10n+2, 10n+18], or [10n+11, 10n+19] when one end is the cut ℓ. The same holds for w.

## 3. Type A with b = 3 reduced

**Parameters.** a = 8, ℓ1 = u + 15, ℓ2 + ℓ3 + λ = 30, and ρ1 ≡ λ. Exactly one v-2-vertex V1 lies on t1, and the other, V2, lies on Λ ∪ t2 ∪ t3. The F1 positions are:
- b5 at 25;
- Λ[k] at 25 + k;
- b5 at 25 + λ;
- t1[j] at 40 + u + λ − j on the way back;
- b4 at 40 + u + λ;
- t3[u] at 70, followed by R_in.

**v-alternation in F1.**
- Row 1 = t1[u..u+10] contains V1.
- Since b5 appears at 25, we need λ ≥ 6, and λ ∉ {15, 25} so that b5 does not sit on a cut.
- V2 lies on Λ exactly when λ ≥ 16, and λ ≤ 24.

**Arm table for t1** (ℓ1 = u + 15):
- ρ1 ∈ {1, 2, 3, 7, 8, 9} is killed for every u.
- ρ1 = 4 is killed if u ≥ 7.
- ρ1 = 5 is killed if u ≥ 6. In any case it would force λ ∈ {5, 15, 25}, which is already excluded.

Hence λ ∈ {6, 14, 16, 24}, with λ = 14 only for u ≤ 6.

**λ = 6.** Rows 2 = t1[u+10..u+14], b5, Λ[1..5] and 3 = Λ[5], b5, t1[u+14..u+6] differ in the paths Λ[1..4] and t1[u+6..u+9].

The chain partner comes from the following exchange:
- For u ≥ 5, exchanging row 1 with row 4 = t1[u+6..u−4] gives L(t1[u−4..u−1]) = L(t1[u+7..u+10]).
- For u ≤ 4, row 4 = t1[u+6..1], b4, t2[1..4−u], and the same exchange gives L(t1[u+7..u+10]) = L(t1[u−1..1], b4, t2[1..4−u]).

Apply DP-2 with m = 4:
- P1 = the 4-path just named;
- P1′ = t1[u+7..u+10];
- P2 = t1[u+6..u+9], which starts at the backward cut at 40;
- P2′ = Λ[1..4].

Contradiction.

**λ = 24.** Here ℓ2 + ℓ3 = 6, so u ≤ 4. Row 6 = [60,70] is:

    t1[u+4..1], b4, t2_int, b5, t3[ℓ3−1..u].

It contains all of t1[1..u] and also t3[u], so the label c2 ∈ S occurs twice. Contradiction.

**What remains of type A with b = 3:**
- **λ = 16:** V2 ∈ Λ[6..14], any u, ℓ2 + ℓ3 = 14, ℓ3 ∈ [u+1, u+9]. Lemma OL on Λ, with forward cuts at Λ[5] and Λ[15], forces ρ(Λ) ∈ {4, 6} (ρ(Λ) = 5 + a3 with a3 ≠ 0).
- **λ = 14 with u ≤ 6:** V2 ∈ t2[1..6−u], and V1 ∈ t1[u+5..u+9]. Two exchanges hold: L(t1[u..u+3]) = L(t1[u+11..u+14]), and L(b5 Λ[1..5]) = L(t1[u+4..u+9]).

## 4. Status

**WRITTEN:**
- Lemma OL and the threshold table (§1): every thread or loop of length ≥ 27 is impossible;
- the b4/b5 ρ-relations and the arm table (§2);
- type A with b = 3 reduced to {λ = 16; λ = 14 with u ≤ 6} (§3).

**Open in the v143 branch:**
- L2 with k = 3: type A with b = 3 (the residue above); type A with b = 4; type B with b ∈ {2, 3}; type C; type E;
- L1.

L4-B is closed (v113), and type A with b = 2 is closed (v114). The v143 ceiling is unchanged:
- no support-9 statement is made;
- every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
