# Original Tuscan-2(11), entire m = 9 distance-two branch, part 5: L2 with k = 3 — the universal segment/offset parametrization, universal kills, and the exact residual family

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues:
- v114 `D2-m9-L2k3-double-pass-lemma-typeA-b2-excluded-v114.md` (`e5b74dd0bb1a4064811de2578b9fcc607a6d89c9a09e89c8cec90dd0c15ee4d0`);
- v115 `D2-m9-L2k3-extended-overlap-thresholds-typeA-b3-reduced-v115.md` (`fd3f5d8b4a391c885a758f22a9d7864a5cde45ae225b5db27c2ba1af63775a2d`).

Notation and imports are as in v114 §1 and v115 §1–2.

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. The six v-segments

**The v-passages.** Label v has these passages:
- ℓ, on the F1 cut at 0;
- the five corners of b5, none of them on a cut;
- the four passages of its two 2-vertices V.

Cutting both faces at these passages gives six segments, the same in every type:

| Segment | Walk | Length | V-passages inside |
|---|---|---|---|
| S_out | ℓ, T, b4, t1, b5 | t + ℓ1 | n1 |
| S_Λ1, S_Λ2 | the two passes of Λ | λ each | nΛ each |
| S_12 | b5, t1⁻, b4, t2, b5 | ℓ1 + ℓ2 | n1 + n2 |
| S_23 | b5, t2⁻, b4, t3, b5 | ℓ2 + ℓ3 | n2 + n3 |
| S_in | b5, t3⁻, b4, T, ℓ | ℓ3 + t | n3 |

Here n1, n2, n3 and nΛ count the V's on t1, t2, t3 and Λ. So n1 + n2 + n3 + nΛ = 2, and T carries no v.

**How the types assemble them.** The faces are these segments joined in order:
- **A:** F1 = S_out S_Λ1 S_12 S_in, and F2 = S_Λ2 S_23.
- **B:** F1 = S_out S_Λ1 S_12 S_Λ2 S_in, and F2 = S_23.
- **C:** F1 = S_out S_in, and F2 = S_12 S_Λ1 S_23 S_Λ2.
- **E:** F1 = S_out S_Λ1 S_in, and F2 = S_12 S_Λ2 S_23.

**Offsets.** Give every b5-passage its offset in [1, 9], measured within its face's cut grid. ℓ counts as offset 0 at the start of S_out and as 10 at the end of S_in.

Consecutive v-passages lie in consecutive rows (v114 (I)). So a segment with n inside passages, start offset q_s and end offset q_e has length:

    10n + 10 + q_e − q_s.

A thread's ρ is the sum of the offsets of its two b5 corners (v115 §2).

## 2. The parametrization by type

**Type A.**
- F1 offsets: 0 → p1 → p2 → p3 → 10. F2 offsets: y0 → y1 → y0.
- Equal Λ-passes and the two expressions for ℓ2 force **p1 = 5** and y1 = y0 + p2 − 5.
- Lengths:
  - ℓ1 = 10n1 + 5 + u
  - λ = 10nΛ + 5 + p2
  - ℓ2 = 10n2 + 5 + p3 − p2 − u
  - ℓ3 = 10n3 + 10 − p3 + u
- Pass offsets:
  - ρ1 = 5 + p2, ρ2 = p3 + y1, ρ3 = y0 + p3, ρΛ = 5 + y1
  - φ1 = u, φ2 = −(p2 + 5 + u), φΛ = 5
  - backward cuts of t3 at ≡ u.

**Type B.**
- F1 offsets: 0 → p1 → p2 → p3 → p4 → 10. F2 offsets: x → x.
- These force **p2 = 5** and p4 = p3 + 5 − p1.
- Lengths:
  - ℓ1 = 10n1 + p1 + u
  - λ = 10nΛ + 15 − p1
  - ℓ2 = 10n2 + 5 + p3 − p1 − u
  - ℓ3 = 10n3 + 5 − p3 + p1 + u
- Pass offsets:
  - ρ1 = p1 + 5, ρ2 = p3 + x, ρ3 = x + p4, ρΛ = p1 + p4
  - φ2 = −(5 + p1 + u), φΛ = −p1
- Constraint: b = 1 + n2 + n3 ≥ 2.

**Type C.**
- F1 offsets: 0 → p1 → 10. F2 offsets: x0 → x1 → x2 → x3 → x0.
- These force x2 = x0 + p1 − 5 and x3 = x1 + 5 − p1.
- Lengths:
  - ℓ1 = 10n1 + p1 + u
  - ℓ3 = 10n3 + 10 − p1 + u
  - λ = 10nΛ + 5 + x0 + p1 − x1
  - ℓ2 = 10n2 + 10 + x1 − x0 − p1 − u
- Pass offsets:
  - ρ1 = p1 + x0, ρ2 = x0 + x1 + p1 − 5, ρ3 = x1 + 5, ρΛ = x0 + x1
  - φ2 = −(x0 + p1 + u), φΛ = −x1

**Type E.**
- F1 offsets: 0 → p1 → p2 → 10. F2 offsets: x0 → x1 → x2 → x0.
- These force x2 = x1 + p2 − p1 and x0 = x1 + 5 − p1.
- Lengths:
  - ℓ1 = 10n1 + p1 + u
  - λ = 10nΛ + 10 + p2 − p1
  - ℓ3 = 10n3 + 10 − p2 + u
  - **ℓ2 = 10n2 + 5 − u**
- Pass offsets:
  - ρ1 = x1 + 5, ρ2 = 2x1 + p2 − p1, ρ3 = x1 + 5 − p1 + p2, ρΛ = x1 + p2
  - φ2 = −(x1 + 5 + u), φΛ = −p1

**Common to all types.** Every listed offset lies in [1, 9], since b5 is never on a cut. In each type the lengths sum to 45 + u, and ρ2 = ρ1 + ρ3 holds identically.

## 3. Universal kills

**(K1)** n1 = 2 is impossible. Then ℓ1 ≥ u + 21, and every row of the arm table (v115 §2) kills t1. By row reversal, **n3 = 2 is impossible.**

This subsumes v114 §3 (type A with b = 2 is exactly n1 = 2). It also covers type B with b = 3 in the case where both V's lie on t3.

**(K2)** n1 = 1 gives ℓ1 ∈ [u+11, u+19], so ρ1 ∈ {4, 5, 6} with the arm conditions:
- ρ1 = 4 needs u ≤ 6;
- ρ1 = 5 needs u ≤ 5 and ℓ1 ≤ u + 15;
- ρ1 = 6 needs ℓ1 ≤ u + 16.

The mirror statement holds for n3 = 1.

**(K3)** nΛ = 2 gives λ ∈ [22, 26], so ρΛ ∈ {4, 6} (v115 threshold).

**(K4)** Type A with nΛ = 2 is impossible. Here λ = 25 + p2 ≥ 26 and φΛ = 5, and the v115 windows kill every ρ at L = 26 when φ = 5.

**(K5)** Type B with b = 2, n1 = 1 and λ = 6 (that is, p1 = 9) is impossible. Take the rows [20,30] = t1[u+10..u+18], b5, Λ[1] and [30,40] = Λ[1..5], b5, t1[u+18..u+14]. They give L(t1[u+10..u+13]) = L(Λ[2..5]). Rows 1 and 4 give L(t1[u..u+3]) = L(t1[u+11..u+14]). Lemma DP-2 with m = 4 then gives a contradiction.

**(K6)** The type A exclusions of v115 §3 still stand: λ ∈ {6, 7, 8, 9, 17, 18, 19, 24}, and λ = 14 with u ≥ 7.

## 4. The exact residual for L2 with k = 3

**Every surviving L2 (k = 3) array is described by:**
- a type in {A, B, C, E};
- a vector (n1, n2, n3, nΛ) with n1, n3 ≤ 1 and sum 2;
- u ∈ [1, 9];
- the type's free offsets in [1, 9]:
  - A: p2, p3, y0;
  - B: p1, p3, x;
  - C: p1, x0, x1;
  - E: p1, p2, x1.

All of §2 must hold, together with:
- every length ≥ 1;
- ℓ1, ℓ3 ≥ u + 1 (the arms);
- the v115 arm table for t1 and t3;
- the v115 OL windows for t2 (φ2, ρ2, ℓ2) and Λ (φΛ, ρΛ, λ).

It must avoid (K1)–(K6). Every row must also pass the remaining row-level tests, which have not been made: V-placement consistency, alternation of w, and the exchanges.

**This finite family is the exact L2 (k = 3) gap at this packet.** Its cells in (type, n-vector) are:

| Type | Live cells |
|---|---|
| A | n1 = 1: (1,1,0,0) with λ = 14 and u ≤ 6; (1,0,0,1) with λ = 16. n1 = 0: (0,2,0,0), (0,1,1,0), (0,1,0,1), (0,0,1,1). |
| B | The six vectors with n1, n3 ≤ 1 and n2 + n3 ≥ 1: (1,1,0,0), (1,0,1,0), (0,2,0,0), (0,1,1,0), (0,1,0,1), (0,0,1,1); minus (K5). |
| C, E | All eight vectors with n1, n3 ≤ 1, up to the self-mirror. |

**Type A row-level fixings for n1 = 1:**
- In cell (1,0,0,1), λ = 16 forces y0 = 5, y1 = 1 and ρΛ = 6, so the F2 cuts are at ℓ3 + 5 (mod 10). t3 forces p3 ≠ 5, with p3 = 2 only if u ≤ 7 and p3 = 3 only if u ≤ 8.
- In cell (1,1,0,0), V2 ∈ t2[1..6−u] (v115 §3).

## 5. Status

**WRITTEN:**
- the universal six-segment decomposition and the offset parametrization of all four types (§1–2);
- kills (K1)–(K6) (§3);
- the exact finite residual statement for L2 with k = 3 (§4).

L4-B is closed (v113). L1 is not yet reduced. The v143 ceiling is unchanged:
- no support-9 statement is made;
- every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
