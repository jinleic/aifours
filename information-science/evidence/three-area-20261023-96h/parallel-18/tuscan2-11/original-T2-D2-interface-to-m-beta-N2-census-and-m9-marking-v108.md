# Original Tuscan-2(11): exact interface from the distance-two requirement to (m, β, N2, row census), and the m = 9 marking

Actual `/bin/date` before this body: **Mon Oct 26 15:27:36 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN interface and scope record, written at Main's request (original-target check before any further m-family increase). It is not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe, chosen row, chosen control or GO.

**Preserved.** All v19-manifest claims stay unreviewed and unchanged. The v150b freeze (manifest v18, through v93) is unchanged. All old zero-credit, cadence and process findings are unchanged.

## 1. The original requirements (actual source)

Source: `selection-v1.md` (SHA256 `fd62055310684ffcd28be47c3f0c6e8698e6d72bae7118aa1818b5d17df3af2b`, 65 LF), lines 7–17. These lines restate the primary definition `sources/cpro1-tuscan-definition.txt` (SHA256 `80c4c529c3526971139ee7e0e361d2e27f59879a7cdbd22f526010c6e603f5d0`, 46 LF; CPro1 `OPEN_INSTANCES=[[11],[13]]`).

An eligible array A = (A[r,c]), r,c ∈ {0..10}, with entries in X = {0..10}, must satisfy:
- **(R1)** every row is a permutation of X;
- **(R2)** each ordered pair (a,b) with a ≠ b occurs exactly once as A[r,c] = a, A[r,c+1] = b (c ≤ 9);
- **(R3)** each ordered pair (a,b) with a ≠ b occurs at most once as A[r,c] = a, A[r,c+2] = b (c ≤ 8).

Distances are linear, there is no Latin-column condition, and (R3) concerns distance 2 only. The safe normalizations are symbol relabelling, row permutation and reversal of all rows (line 17).

## 2. The frozen variables and their full source definitions

| Variable | Definition | Source |
|---|---|---|
| τ, f(v), p(v), F, G | τ maps a row's start to its end. f(v) is the second symbol of the row starting at v; p(v) is the penultimate symbol of the row ending at v. F_(v,b) = 1 iff f(v) = b; G_(a,v) = 1 iff p(v) = a. | v1 §1, lines 13–25 |
| K_v, boundary turn | K_v sends a to b for every internal triple (a,v,b), and is completed by K_v(p(v)) = f(v) and K_v(v) = v. It is a permutation of X (Lemma 1). The only possible off-v fixed point is the boundary turn p(v) = f(v). | v1 §2, lines 29–41 |
| M, Γ | Γ counts internal distance-two pairs with multiplicity. Σ_v K_v = I + Γ + GF (eq. 1). M is the missing distance-two matrix. | v1 §3, lines 45–61 |
| T, faces | T(a,v) = (v, K_v(a)) on the 110 arcs. Each τ-cycle of length ℓ is one T-cycle of length 10ℓ (Theorem 2). A face with r rows has 10r arcs, and each label occurs r − 1 times among its arc tails if it starts a row there, r times otherwise. Every face has ≥ 2 rows. | v1 §5, lines 103–113; v4 lines 15–19 |
| split graph | One vertex per off-v cycle of K_v, with its cyclic order. The 55 edges are the 55 unordered label pairs (F2). Leaves are exactly the fixed boundary turns. Its face walks are T. | v4 line 21; v12 §2 eq. (2) |
| m, N2, β | Consider the 110 off-diagonal K-arcs. m counts those in cycles of length ≥ 3, 2·N2 those in 2-cycles, and β the fixed boundary turns. So m + 2N2 + β = 110. | v4 line 9; β-record §2 |
| m = 9 census | Classes (S), L1, L2 (k = 1, 3), L3 and L4 (C1, C2, L4-B), with the cycle data and β of v94 §2. | v94 §2, §5 |

Source pins:
- v1 `unrestricted-boundary-turn-coupling-v1.md` `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275` (191 LF);
- v4 `unrestricted-m6-core-frontier-v4.md` `ace3850290bfb16aa78f4bdee3fa4916184d892f38fbf2bcc84e3da9af4eaf87` (150 LF);
- v12 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2` (155 LF);
- v24 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422` (117 LF);
- β-record `v24-beta-consumption-additive-record-v1.md` `f04a9f9a8a7151a45f481193b65299cc3bf2d6a10f9ca80ee754616d558104b8` (55 LF);
- v94 `1c5465c4f0a5835ecda93a2a9877d42f3b607d774f63e49be9f1228a951c396c` (201 LF).

## 3. Exact translation of (R3)

### 3.1 Distance-two events are the internal turns

A distance-two event at columns c, c+2 (c ≤ 8) is the internal triple (a, v, b) = (A[r,c], A[r,c+1], A[r,c+2]). Here v is never a row end, so K_v(a) = b is an internal turn (v1 §2; v24 §5). The 11 boundary turns are not distance-two events.

So (R3) is equivalent to each of the following.
- **(I1)** Γ ≤ J − I entrywise.
- **(I2)** M := J + GF − Σ_v K_v is a 0/1 matrix with zero diagonal. It then has exactly 11 ones, with outdeg_M(a) = #{v : p(v) = a} and indeg_M(b) = #{v : f(v) = b} (v1 eq. 2 and lines 65–70).
- **(I3)** For each a, the map v ↦ K_v(a) is injective on the v with v ≠ a and p(v) ≠ a.
- **(I4) Partial-Latin form.** Put symbol b in cell (a, v) for every internal triple (a, v, b). Then:
  - cells are filled at most once, by (R2), since (a,v) is adjacent once;
  - columns have distinct symbols, by (R2), since (v,b) is adjacent once;
  - rows have distinct symbols exactly by (R3).

  So (R1)–(R3) make the 99 internal triples a partial Latin square on X. Its empty off-diagonal cells are exactly the 11 terminal cells (p(v), v). Filling cell (p(v), v) with f(v) gives the column-complete array whose column v is K_v. That array is also row-Latin iff GF = M. (R3) does **not** imply GF = M: the written n = 4 calibration of v1 §4 has GF = I.

### 3.2 Distance two on the row census

Index a face with r rows cyclically, s_0, …, s_(10r−1), with cuts at the positions ≡ 0 (mod 10). The turn at position i is internal iff i ≢ 0 (mod 10), and its distance-two arc is (s_(i−1), s_(i+1)). So:
- The turns at odd i are never cuts. Their arcs form a closed walk of length 5r through the even positions, and every one is internal.
- The turns at even i form a closed walk of length 5r through the odd positions. It contains exactly the r boundary turns of that face.

Over the whole census (Σ r_F = 11), (R3) is equivalent to: the 55 even-position arcs and the 44 internal odd-position arcs are 99 distinct ordered pairs. For one-face arrays this is v24 §7.3; here it is stated for every face census.

Each symbol a lies at e(a) = Σ_(j even) c_j(a) − 1 even face positions and at o(a) = Σ_(j odd) c_j(a) odd ones, where c_j(a) counts the rows with a in column j. The cut is one face position but two row slots.

## 4. What (R3) says in the census variables

Split N2 = N2_int + N2_bd, where N2_bd counts the 2-cycles that contain their K_v's boundary turn. Then N2_bd ≤ 11 − β.

The internal arcs are:
- 2·N2_int from fully internal 2-cycles;
- N2_bd from boundary 2-cycles;
- m − (11 − β − N2_bd) internal long-cycle arcs.

Their total is 99, which reproduces m + 2N2 + β = 110.

Under (R3):
- **(C1)** Two fully internal 2-cycles (a b), at centres v ≠ w, would repeat both events (a,b) and (b,a). So the N2_int fully internal 2-cycles lie on pairwise distinct unordered pairs, and N2_int ≤ 55. In split-graph terms, non-cut 2-vertices have pairwise distinct neighbour-label pairs. T1 alone permits a repeat.
- **(C2)** All 99 internal arcs of the three kinds are pairwise distinct ordered pairs.
- **(C3)** The only counting consequences are N2_int ≤ 55 and N2_bd ≤ 11 − β. These give m ≥ β − 22 (β-record §3), which is vacuous.
- **(C4)** (R3) is not a function of (m, β, N2, census class). It constrains which labels the cycles carry, not their cycle types. (m, β, N2, class) are invariant under the three safe normalizations: relabelling, row permutation, and global reversal (which sends K_v to K_v^(-1) and exchanges p with f).

## 5. Which eligible T2 instances can land in the m = 9 classes

Under (R3) the m = 9 classes keep their T1 values. These follow from v94 §2 and v1 Lemma 1. A leafless centre's boundary turn lies in a long cycle or in a 2-cycle. Every non-centre K_v is five 2-cycles, one of which contains its boundary turn.

| Class | Centres | β | N2 | N2_bd | N2_int |
|---|---|---|---|---|---|
| (S) | v: 9, 6+3, 5+4 or 3+3+3 | 1 | 50 | 10 | 40 |
| L1 | v: 6, w: 3 | 1 | 50 | 9 or 10 | 41 or 40 |
| L2 | v: 5, w: 4 | 1 | 50 | 9 or 10 | 41 or 40 |
| L3 | v: 3+3, w: 3 | 1 | 50 | 9 or 10 | 41 or 40 |
| L4 | v1, v2, v3: 3 each | 3 | 49 | 8 | 41 |

In each row, N2_int ≤ 41 ≤ 55. So (R3) gives no counting obstruction at m = 9, and it forces neither a different m nor a different (β, N2) family.

**Exact statement.**
- The eligible T2 instances landing at m = 9 are exactly the eligible arrays with support 9, if any exist.
- Each is a T1 array, so it lies in exactly one v94 class.
- The written T1 exclusions apply to it unchanged. These are (S), L4 connected, L2 with k = 1 and L3 (v94–v105), and L4-B W2 (v106–v107), all unreviewed WRITTEN.
- So such an instance lies in L1, in L2 with k = 3, or in L4-B W1.
- Whether any eligible array has support 9 is undecided. None is assumed, constructed or probed here.

## 6. Marking and pivot

**m = 9 is T1-side geometry only.**
- The m-ladder (v3–v107) uses (R1)–(R2) and their consequences; it never uses (R3).
- Its exclusions are valid necessary-case exclusions for eligible T2 arrays. But m = 9 is not a branch that (R3) creates, and the ladder cannot settle the original target alone: the actual T1(11) array of v24 has m = 36 and β = 0, so T1-only arguments cannot exclude every support value (v24 §7.1–7.2).
- So m = 9 is not an unpaid original-T2 branch. The unpaid original content is the distance-two coupling (R3) itself, on the unrestricted eligible family.

**Pivot (per Main).**
- No further m-family increase (m = 10 or any later T1 family) will be offered as a substitute for the book target.
- The open m = 9 classes (L1, L2 with k = 3, L4-B W1) are parked as T1-side residue. An L4-B W1 k_x = 1 argument was derived in reasoning only and is not claimed.
- Owner work now targets the exact unrestricted object of §3: permutations K_v with one boundary cell per column, satisfying:
  - the T-face census with cuts every 10 arcs;
  - every 10-arc segment Hamilton;
  - (I3)/(I4) row-injectivity, i.e. the partial-Latin distance-two coupling, for all eligible arrays.

## 7. Result

- **WRITTEN:** the exact all-variable interface (R3) ⇔ (I1) ⇔ (I2) ⇔ (I3) ⇔ (I4), together with the census form of §3.2 and consequences (C1)–(C4).
- **WRITTEN:** the m = 9 placement table of §5. (R3) yields no counting exclusion of m = 9 and no forced change of the m, β or N2 family.
- **Marking:** m = 9 is T1-side geometry only, and work pivots to the distance-two coupling.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. The two parent cadence MAJORs of parent v138 (103→104 30m02, 104→105 31m10) are carried. This candidate needs its own complete source-bound gate.
