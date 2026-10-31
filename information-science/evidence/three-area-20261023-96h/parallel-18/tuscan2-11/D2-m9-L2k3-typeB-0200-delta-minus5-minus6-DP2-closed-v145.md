# Original Tuscan-2(11), entire m = 9 distance-two branch, part 33: type B (0,2,0,0) with δ ∈ {−5, −6} closed by DP-2, so type B (0,2,0,0) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-0200-delta6-5-minus4-closed-v144.md` (SHA256 `2fdd8c287c44c36ad1fe14e9d97411decbbe4890bf0b89010a9c4743628086c9`), with the notation of v143 §1. Lemma DP-2 is v114 §2.

This uses (E) and the row-exchange rule (X) only. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The chain for negative δ

Let δ = −m with m ∈ {5, 6}. Then:
- G = A′ − m and H = A′ + 10 − m;
- x = δ + 10 − p3 ≥ 1;
- r1 = t2[H..G] is a pure t2-row.

**Exchange 1: R3 with r1.** These rows share t2[A′−m..A′].
- If ℓ1 ≥ 5, R3 = t1[ℓ1−5..1], b4, t2[1..A′].
- If ℓ1 < 5, R3 is the pure row t2[A′−10..A′].

In both cases:

    L(P1) = L(P1′),

where P1′ = t2[A′+1..A′+10−m] and P1 is the first 10 − m vertices of R3. P1 is a row-path disjoint from P1′.

**Exchange 2: R4 with r0.** These rows share t2[H..A′+10]:

    L(P2) = L(P2′),

where:
- P2 = t2[A′..A′+9−m] = (y, q1, …, q_{9−m}), with y = t2[A′] and P1′ = (q1, …, q_{10−m});
- P2′ is the 10 − m vertices of r0 beyond t2[A′+10]: t2[A′+11..ℓ2−1], then b5, then the t3-tail. These vertices lie in r0's head and are disjoint from P1, P1′ and P2.

**DP-2 applies.**
- P1 and P1′ are vertex-disjoint paths of 10 − m vertices with the same labels.
- P2 is (y, q1, …, q_{9−m}).
- P2′ is a path of 10 − m vertices with L(P2′) = L(P2), and its edges differ from those of P1, P1′ and P2.

Lemma DP-2 excludes 10 − m ∈ {4, 5}. **So δ = −5 (m = 5) and δ = −6 (m = 4) are impossible.**

The sizes check out: in Exchange 1, R3 keeps (ℓ1 − 5) + 1 + (A′ − m − 1) = 10 − m vertices outside the shared part, using A′ = 15 − ℓ1. In Exchange 2, r0 keeps (p3 − 1) + 1 + x = 10 − m vertices outside the shared part.

## 2. Result

**WRITTEN, using (E) and (X) only:** type B (0,2,0,0) is impossible for δ = −5 and δ = −6. Together with v143 (δ = 4) and v144 (δ ∈ {6, 5, −4}), and the shift screen δ ∈ {±4, ±5, ±6} of v143 §1, **type B (0,2,0,0) is closed.**

**OPEN residual of L2 (k = 3):**
- type B (0,1,1,0);
- type A (0,2,0,0) and (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
