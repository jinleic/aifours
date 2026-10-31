# Original Tuscan-2(11), entire m = 9 distance-two branch, part 63: Lemma A4 (arm exactness gives u ≥ 4 in every open L1 type), and the closure of form (b) of v174

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-consolidated-status-L1-types3-9-closed-type7-reduced-atlas-v175.md` (SHA256 `9e800e98a6bd766d178031ec75dd81d8199202533a30b7b16c5fb3a2b3cb9167`). It uses:
- the arm description of v117 §2 (R_out = ℓ, T_int, b6, h1[1..u] and R_in = h5[u..1], b6, T_int, ℓ, both arms carrying S);
- exactness (E): one H-edge per unordered label pair, v117 §1.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Lemma A4

**Lemma A4.** Suppose the arms h1[1..u] and h5[1..u] lie on two different threads, or on a thread and the loop Λ. Then u ≥ 4.

*Proof.*
- **Setup.** The arms are vertex-disjoint paths of H with L(h1[1..u]) = L(h5[1..u]) = S and |S| = u. The labels c1 = L(h1[u]) and c5 = L(h5[u]) carry the cuts at 10 and at 10(r1 − 1). Since each label has one cut, c1 ≠ c5, so u ≥ 2.
- **u = 2.** S = {c1, c5}, so L(h1[1]) = c5 and L(h5[1]) = c1. The edges h1[1]h1[2] and h5[1]h5[2] both join c1 and c5, against (E).
- **u = 3.** Write S = {c1, c5, s}, so h1[1..2] carries {c5, s} and h5[1..2] carries {c1, s}.
  - If L(h1[2]) = s, the edge h1[2]h1[3] joins {s, c1}. The h5-arm always contains an edge joining c1 and s: either h5[1]h5[2], or h5[2]h5[3] when L(h5[2]) = s.
  - If L(h1[2]) = c5, the h1-arm has the edges {c5, s} and {c5, c1}. The h5-arm has {c1, s} and {L(h5[2]), c5}, which is {s, c5} or {c1, c5}.
  - Either way two different edges join the same pair, against (E). ∎

**Scope.** Lemma A4 applies to every L1 type that is still open:
- type 7 (arms on t1 and t3);
- type 8 (t1 and t2);
- types 1 and 2 (Λ and t3, Λ and t2);
- types 11 and 12 (t1 and Λ).

It also gives the earlier u ≤ 3 closures (for example v159) at once, but those packets stand as written.

## 2. Consequences

**Type 7 with r2 = 3, form (b) of v174 §5.** That form needs u ≤ 3 (ℓ1 ≥ u + 11 with ℓ1 ≤ 14), so Lemma A4 excludes it.

**Types 1 and 11 with r1 = 6.** By v167's atlas (written, not packeted there), ℓ3 = 5 − u, so u ≤ 4. With Lemma A4, u = 4 and ℓ3 = 1. Recorded as a restriction only.

**Type 7 with r2 = 3: what remains.** c′ = 0 with v's G2-V on t1, in α-i form (ii) (x ≤ u − 1, P1 ≤ 19) or form (iii) (y ≤ u − 1, P4 ≥ 61), together with the mirrors (G2-V on t3). In every remaining type 7 configuration, u ≥ 4.

**A note on exploration.** A consistent-looking skeleton for form (b) with u = 2 (ℓ1 = 14, ℓ3 = 10, x = y = 7) was built in the checkpoint-220 exploration. It satisfies every row-level condition used so far, but fails (E) on its arms. This shows that (E) carries information which the row counts alone do not.

## 3. Result

**WRITTEN:**
- Lemma A4: u ≥ 4 in every open L1 type.
- Form (b) of v174 is impossible.
- Types 1 and 11 with r1 = 6 need u = 4 and ℓ3 = 1.

**OPEN (m = 9, L1):**
- type 7 with r2 = 3 (α-i forms (ii) and (iii), with mirrors);
- type 7 with r2 = 4 (a G2-V of v on t1 or t3);
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
