# Original Tuscan-2(11), entire m = 9 distance-two branch, part 13: L2 (k = 3) — two v-2-vertices on Λ is impossible in every type

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-b2-cells-excluded-v123.md` (SHA256 `fd1654f56dff6a3b75477eed1a3c9a8250c4c7bfbd27ec28010833b16a610294`). Notation is that of v116 §2, and the windows are those of v115 §1.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The claim

The cell (0,0,0,2) — both v-2-vertices on Λ — is impossible in every type:
- **Type A:** v116 (K4).
- **Type B:** b = 1 + n2 + n3 = 1 < 2, so the cell does not exist.
- **Types C and E:** §2 and §3 below.

In each case v116 (K3) gives λ ∈ [22, 26] and ρΛ ∈ {4, 6}. It remains to show that Lemma OL kills both values of ρΛ.

## 2. Type E

**Parameters.**
- λ = 30 + p2 − p1, so λ ∈ [22, 26] gives p2 − p1 ∈ [−8, −4].
- The forward cuts of Λ, in its F1 pass, sit at indices ≡ 10 − p1. Take s = 10 − p1 ∈ [1, 9].

**ρΛ = 4.** The B-chain window is [−3, λ − 21] = [−3, 9 + p2 − p1]. It contains s, because 10 − p1 ≤ 9 + p2 − p1 holds for p2 ≥ 1.

**ρΛ = 6.** The C-chain window is [1, λ − 17] = [1, 13 + p2 − p1]. It contains s for the same reason.

**DP-2 hypotheses.** Λ is a loop at b5, so index 0 and index λ are both b5. In each chain only two paths can leave Λ:
- P1, at the low end;
- P2′, at the high end.

The paths P1′ and P2 stay inside Λ. The two leaving paths are:

| Chain | P1 leaves through | P2′ leaves through |
|---|---|---|
| B (ρ = 4) | F1, Λ+ end, into t1 | F2, through K2, into t2 |
| C (ρ = 6) | F2, through K1, into t2 | F1, Λ− end, into t3 |

So in each chain P1 and P2′ lie in different regions; if both contain b5, they use different b5-edges. No chain uses both F2 exits, which are the same t2 vertices. Hence:
- P1 and P1′ are vertex-disjoint;
- the edges of P2′ differ from those of P1, P1′ and P2.

**So type E with nΛ = 2 is impossible.**

## 3. Type C

**Parameters.**
- λ = 25 + x0 + p1 − x1.
- The forward cuts of Λ, in its first F2 pass, sit at indices ≡ −x1, and ρΛ = x0 + x1.

**ρΛ = 6.** The window [1, λ − 17] = [1, 8 + x0 + p1 − x1] contains 10 − x1, because x0 + p1 ≥ 2. So ρΛ = 6 is killed.

**ρΛ = 4.** Then x1 ≡ 4 − x0. The window [−3, λ − 21] = [−3, 4 + x0 + p1 − x1] contains:
- the representative −x1, when x1 ≤ 3;
- the representative 10 − x1, when x0 + p1 ≥ 6.

So survival needs x1 ≥ 4 and x0 + p1 ≤ 5, hence x0 ≤ 4. But x1 ≡ 4 − x0 with x0 ≤ 4 forces x1 = 4 − x0 ≤ 3, or x1 ≡ 0 when x0 = 4. Contradiction either way.

**DP-2 hypotheses.** Both passes of Λ lie in F2:
- the forward pass S_Λ1 is entered from t2 through K2 and left into t2 through K1;
- the backward pass S_Λ2 is entered from t3 through K5 and left into t1 through K3.

The leaving paths are:

| Chain | P1 leaves through | P2′ leaves through |
|---|---|---|
| B (ρ = 4) | the forward pass, through K2, into t2 | the backward pass, through K5, into t3 |
| C (ρ = 6) | the backward pass, through K3, into t1 | the forward pass, through K1, into t2 |

In each chain they lie in different regions, so the hypotheses hold as in §2.

**So type C with nΛ = 2 is impossible.**

## 4. Result

**WRITTEN, (R1)–(R2) only:** in L2 with k = 3, the loop never carries both v-2-vertices. Cell (0,0,0,2) is removed from every type.

**Live residual:**
- Type A: (0,2,0,0) and (0,1,1,0).
- Type B: (0,2,0,0) and (0,1,1,0).
- Types C and E: the seven cells with n1, n3 ≤ 1 other than (0,0,0,2).
- L1: types 1–4 and 7–12.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
