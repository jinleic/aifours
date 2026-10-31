# Original Tuscan-2(11), entire m = 9 distance-two branch, part 49: L1 types 11 and 1 with r1 = 3 are impossible

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types11-1-r1eq3-u-le-4-closed-v161.md` (SHA256 `dd12edbdd81da32b501e38360f10db7fc2e6219e5cc6bb2da5a1c10414cc48cb`) and uses its §1 data and notation:
- t3[j] lies at Z2 + j (forward) and at Z3 − j (backward);
- index 0 is b6 in both passes;
- ρ ≡ Z2 + Z3;
- s1 ∈ [1, 10] is the least positive forward-cut index.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. What remains after v161

**Remaining case.** v161 leaves u ≥ 5, ρ ∈ {4, 5, 6} and s1 ∈ [15 − u, 10] ⊆ [6, 10].

**Constants.** L = ℓ3 = 35 − u, so the interior of t3 is t3[1..34−u] with 34 − u ≥ 25.

**Low extension.** The forward row [s1 − 10, s1] starts at a forward cut and runs below index 1. It consists of Λ[10−s1..1] (the end of P−, at Z2 − 10 + s1..Z2 − 1), then b6 = Z2, then t3[1..s1]. If λ − 1 < 10 − s1, this row would reach b6 = Z3 as well and contain b6 twice. That is impossible, so the row is as described.

## 2. ρ = 4

**The two exchanges.**
- **(1)** The forward row [s1 − 10, s1] against the backward row [s1 − 6, s1 + 4], whose start s1 − 6 ≡ s1 + 4 is a backward cut:
  - If s1 ≥ 7, the backward row is interior.
  - If s1 = 6, it is b6 = Z3 followed by t3[1..10]. Its index-0 vertex is the same b6 as in the forward row.
  - In both cases the common vertices are t3[max(1, s1−6)..s1], together with b6 when s1 = 6.
  - The differences are P1 (the forward indices s1−10..s1−7: Λ[10−s1..1], b6, t3[1..s1−7], four vertices) and t3[s1+1..s1+4]. (When s1 = 6, P1 = Λ[4..1].)
- **(2)** The forward row [s1, s1 + 10] against the backward row [s1 + 4, s1 + 14]. Both are interior, since s1 + 14 ≤ 24 ≤ 34 − u. This gives L(t3[s1..s1+3]) = L(t3[s1+11..s1+14]).

**DP-2 with m = 4.**
- P1 as above;
- P1′ = (t3[s1+1], …, t3[s1+4]);
- P2 = (t3[s1], …, t3[s1+3]);
- P2′ = t3[s1+11..s1+14].

This is a contradiction.

## 3. ρ = 5

**The two exchanges.**
- **(1)** The forward row [s1 − 10, s1] against the interior backward row [s1 − 5, s1 + 5] (s1 ≥ 6). They share t3[s1−5..s1]. The differences are P1 (Λ[10−s1..1], b6, t3[1..s1−6], five vertices) and t3[s1+1..s1+5].
- **(2)** The forward row [s1, s1 + 10] against the backward row [s1 + 5, s1 + 15]. This gives L(t3[s1..s1+4]) = L(t3[s1+11..s1+15]), since s1 + 15 ≤ 25 ≤ 34 − u.

**DP-2 with m = 5.**
- P1 as above;
- P1′ = t3[s1+1..s1+5];
- P2 = t3[s1..s1+4];
- P2′ = t3[s1+11..s1+15].

This is a contradiction.

## 4. ρ = 6

**The two exchanges.**
- **(1)** The forward row [s1, s1 + 10] against the interior backward row [s1 − 4, s1 + 6] (s1 ≥ 6). This gives L(t3[s1−4..s1−1]) = L(t3[s1+7..s1+10]).
- **(2)** The forward row [s1 + 10, s1 + 20] against the backward row [s1 + 6, s1 + 16]:
  - The forward row runs past index L, into b3 and then t1[ℓ1−1], ….
  - Their common vertices are the t3-vertices with indices s1+10..min(s1+16, L−1), together with b3 when L ≤ s1 + 16. (The index-L vertex is the same b3 in both passes.)
  - So the differences are P1 (the forward indices s1+17..s1+20, a 4-vertex path) and t3[s1+6..s1+9].

**DP-2 with m = 4.**
- P1;
- P1′ = (t3[s1+9], t3[s1+8], t3[s1+7], t3[s1+6]);
- P2 = (t3[s1+10], …, t3[s1+7]);
- P2′ = t3[s1−4..s1−1].

This is a contradiction.

**DP-2 hypotheses.** In each case:
- P1 and P1′ are disjoint;
- y is the t3-neighbour of q1;
- P2′ is a t3-path at indices disjoint from those of P1′ and P2, and its edges are not edges of P1, which lies at other indices or outside t3.

## 5. Result

**WRITTEN:**
- With v161, **L1 type 11 with r1 = 3 is impossible**.
- By the mirror (v161 §4), **L1 type 1 with r1 = 3 is impossible**.

**OPEN (m = 9, L1):**
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8;
- types 2 and 12;
- type 7 with r2 ∈ {3, 4};
- types 3 and 9 with r2 = 3 (λ = 14, u ≥ 4) and with r2 = 4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
