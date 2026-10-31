# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3 — shape (α) of survivor S1 excluded, so S1 and its mirror are impossible

Actual `/bin/date` before this body: **Mon Oct 26 12:19:55 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- v83 (SHA256 `a429177c9b9673bb062f485755a272e3efb6ecd980b1807bba6c08b1c5424159`)
- v84 (SHA256 `d3f1672c3c3169e5dc7cd3efd33420edb8a575d306f504e2b6e283e90c349a5d`)
- Lemma L of v81 (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`)
- Lemma U and pair uniqueness, and the Type II reversal symmetry (v77 §§2–3, SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`)

Two consequences of pair uniqueness are used throughout:
- the labels adjacent to the v-vertices of H are pairwise distinct;
- the same holds for the w-vertices.

## 2. Shape (α): standing facts

Parameters: K = t+2, τ = 3, β_P = 4, ρ = 18, t ∈ {9, ..., 12}, c = 15−t, x = t+2−σ and y = 30−x.

O's rows:
- Q_a = A[t−8..x−1], w, D[1..σ];
- Q_b = D[σ..t−1], w, B[y−1..18];
- N1 = B[8..18];
- N2 = B[8..1], v, C[1..2];
- Q_c = C[2..c−1], w, D[t−1..3];
- Q_d = D[3..1], w, C[c−1..1], v, A[1..t−8].

P's rows: R_P1 = A[6..1], v, B[1..4], R_Pmid = B[4..14], R_P* = B[14..y−1], w, A[x−1..6].

By v83–v84, both prefixes (α1)/(α2) share the following.

**Labels on C and B:**
- C1 = pA; C2 is an O-cut.
- b_v is adjacent to pB2 (via B1) and to pA (via C1).
- The second B w-copy is adjacent to ℓx and to one 𝒫 label, and b_w–D1 supplies the other. So **w is adjacent to ℓx, pB1 and pB2**.
- B[5..7] = a, b, c′ and B8 = ℓB8.
- B[9..13] carries {v, w, pA, ℓx, ℓC2}.
- B14 = pB2.
- B[15..18] is the complementary P4 of B[4..7], so **ℓB18 ∈ {a, b}**.

**Labels on D:**
- D3 = ℓx.
- All three hi vertices lie in D(σ, t−1].
- The v-copy u lies in D[4..t−1].
- 𝒪 ∩ L(D[4..t−1]) = L(A[1..t−8]) (Q_c/Q_d exchange).
- {ℓA[t−8], ℓD[σ]} = {a, b, c′} ∖ {ℓB18}.

**From the rows:**
- Q_a contains A6 = pA, so x ≥ 7.
- σ ≥ 4.
- R_P*'s labels give B[19..y−1] ∪ A[7..x−1] = {v, ℓx, ℓB8, ℓC2}.

**(F1) A[7..x−1] ⊆ {v, ℓB8}.** These labels lie in L(D[σ..t−1]) by the R_P*/Q_b exchange, whereas ℓx and ℓC2 have their unique C∪D vertices at D3 and C2. Moreover A7 ≠ v: A6 = pA would make v adjacent to pA twice. So A[7..x−1] is one of:
- **(i)** empty, x = 7;
- **(ii)** (ℓB8), x = 8;
- **(iii)** (ℓB8, v), x = 9.

**(F2)** Q_a and Q_b each take exactly one v, so u < σ ⟺ the second cross v-copy v2 lies on B. Hence u > σ in (iii), and u < σ in (i) and (ii).

Hence σ = t+2−x ∈ [max(4, t−7), t−5].

## 3. Every remaining (t, σ) fails

**t = 9, σ = 4, x = 7.** Case (i) needs u < 4, but u ≥ 4.

**t = 10, σ = 4, x = 8.** Case (ii) needs u < 4. Impossible.

**t = 10, σ = 5, x = 7.** Then u = D4.
- The 𝒪 labels on D[4..9] are {ℓD5, ℓA2}, so ℓA1 = ℓD5.
- v is then adjacent to ℓD5 twice: b_v–A1 and D4–D5.

**t = 11, σ = 4, x = 9, case (iii).** Here {ℓA1, ℓA2} = {ℓD4, ℓB8}.
- A8–A7 makes v adjacent to ℓB8, so ℓA1 = ℓD4 and A2 = ℓB8.
- A2's neighbours carry {ℓD4, ℓA3} = {a, b, c′} ∖ {ℓB18}, a set that contains c′.
- B8's neighbour B7 is c′, so ℓB8 is adjacent to c′ twice.

**t = 11, σ = 5, x = 8, case (ii), u = D4.**
- u = D4 gives v–ℓD5, so ℓA1 = ℓB8.
- N1's v-copy may only touch {w, ℓC2}, so it touches both. That makes N1's v–w the unique v–w edge.
- v2 lies in B[19..21] with B[19..21] = {v, ℓx, ℓC2}, and may only touch ℓB18. That is one available neighbour for two neighbour slots.

**t = 11, σ = 6, x = 7, case (i).** u ∈ D[4..5].
- u = D5 would make v adjacent to ℓA1 twice. So u = D4, ℓA1 = ℓD6, and o4 := ℓD5 ∈ {ℓB18, ℓB8}.
- **If o4 = ℓB18,** N1's v-copy and v2 need four distinct neighbours from {ℓB8, w, ℓC2}.
- **If o4 = ℓB8,** N1's v-copy uses w and ℓC2, so v2 may only touch ℓB18.

Both fail.

**t = 12, σ = 5, x = 9, case (iii).** Here c = 3, so C2 is adjacent to b_w and w–ℓC2 is used. B20 ∈ {ℓx, ℓC2} is adjacent to b_w, which repeats a w-pair.

**t = 12, σ = 6, x = 8, case (ii).**
- w is already adjacent to ℓB8 (A7) and ℓC2 (C2). So B21 = v, which becomes the unique v–w edge.
- N1's w-copy may then touch only pA (it must avoid ℓB8, v, ℓx, ℓC2 and pB2). That is too few.

**t = 12, σ = 7, x = 7, case (i).** Here A6 = pA is adjacent to b_w, so w–pA is used. N1's w-copy may only touch {ℓB8, v}, and B22 ∈ {v, ℓB8}.
- **If B22 = v,** the v–w edge is used and N1's w is left with only ℓB8.
- **If B22 = ℓB8,** N1's w is left with only v.

Both fail.

**Shape (α) is impossible** (WRITTEN).

## 4. Result

v84 excluded shape (β), and §3 excludes shape (α). So **survivor S1 is impossible**: Type II, r_P = 3, case (0,2), 10 < K < 15, two P-boundaries on B. By the reversal symmetry of v77 §3, its (2,0) mirror is impossible too.

**Owner-written residual** (assuming the unreviewed bodies v47–v85 are correct):
- R1–R4 are empty.
- R5 consists of:
  - Type I, r_P = 3, two/one sub-case (v82, including its through-b_w variant) and its mirror;
  - Type II, r_P = 2;
  - the Type II, r_P = 3 survivors S2 and S2′.
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
