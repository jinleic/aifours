# Original Tuscan-2(11), entire m = 9 distance-two branch, part 81: L1 type 12 with r2 = 3, c′ = 1 and V's on t3 and t2 (and its type-2 mirror) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type12-r2eq3-cprime1-V-on-t3-and-t2-t3V-cut-reduced-to-four-shapes-v193.md` (SHA256 `74e71c8ab87b04a9da19edd1a31b35be3b6ede63616c83d20e8553f47ceed9d6`), with its notation and imports. It closes the four shapes of v193 §4.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Common data of the four shapes

In each shape, ℓ1 − 1 = u + 5, P1 = 16 and ℓ2 − α = 4. So R1 = t1[u] (c1, at 10), t1[u+1..u+5] (11..15), b3 (16), t2[ℓ2−1..α] (17..20), with t2[α] = X20 on the cut 20.

**R1's labels.** v (t2V, J > α), f2 (its upper t2-vertex, j > α) and X30 (its second G1, j > α) meet R1 only through t2-vertices with S_12 in R1. Indeed:
- v has no t1-vertex;
- f2's G2 are t3-vertices;
- X30's G1 are Λ[μ] (cut 30, covering R2 and R3; P+ in R7) and a t2-vertex t2[j] with j > α. That vertex has S_12 in R1 and S_23 = P3 + j < P4 ≤ 49, in R4. So X30's G2 are its t1-arm vertex and t3-vertices of R5 and R6.

So t2[α+1..ℓ2−1] carries exactly {v, f2, X30}, and t1[u+1..u+5] carries the other five labels, {c7, X40, X50, X60, f1}. In particular b3's neighbours carry:
- t1[ℓ1−1] ∈ {c7, X40, X50, X60, f1};
- t2[ℓ2−1] ∈ {v, f2, X30};
- t3[ℓ3−1], which is a vertex of R4 (R4 = t2[β..], b3 at P4 ≤ 49, then t3[ℓ3−1..ℓ2+5] up to 50).

**F2.** Q0 = t1[x..1], b6, t3[1..10−x]; Q1 = t3[10−x..20−x]; Q2 = v, t3[21−x..ℓ3−1], b3, t1[ℓ1−1..x]. b3 lies in Q2. On t3:
- t3[10−x] = f2;
- t3[ℓ2−5] = X60 (cut 60);
- t3[ℓ2+5] = X50 (cut 50);
- R6 holds t3[1..ℓ2−5] and R5 holds t3[ℓ2−4..ℓ2+4].

## 2. w

**w's vertices.**
- w's rows R0 and R7 (ℓ), R1 (P1), R4 (P4), and R2 and R3 (its t2[jw], jw < β) are covered. So its two G2-W's cover R5 and R6.
- By the W-rule (b3 in Q2) they lie in Q0 and Q1. R5's t3-vertices do not meet Q0, so w = {ℓ, b3, t2[jw], t3[a], t3[b]}, with:
  - a ≤ 9 − x (R6 ∩ Q0);
  - ℓ2 − 4 ≤ b ≤ 19 − x (R5 ∩ Q1).

**w's neighbours** are therefore:
- T_int[1] (through ℓ);
- t1[ℓ1−1], t2[ℓ2−1] and t3[ℓ3−1] (through b3);
- t2[jw±1] (or b6), all with index ≤ β;
- t3[a±1] (or b6), all inside t3[0..10−x];
- t3[b±1], all inside t3[ℓ2−5..20−x].

## 3. X20

X20 is a type-I S-label (v193 §4). Its rows R0 (t1-arm), R1 and R2 (cut 20 = t2[α]), R3 (arm P−), R4 (S_23 of t2[α], since α > β) and R7 are covered. So its two remaining G2 are t3-vertices covering R5 and R6.

Its t1-arm vertex lies in Q0 (x > u), so these two t3-vertices lie in Q1 and Q2. R6's t3-vertices do not meet Q2. So X20 has:
- a t3-vertex in R6 ∩ Q1 = t3[11−x..ℓ2−6];
- a t3-vertex in R5 ∩ Q2 = t3[21−x..ℓ2+4].

## 4. (PC) at w fails

By (PC), w must be joined to X20. Check w's neighbours in turn:
- **T_int[1]:** X20 is an S-label.
- **Through b3:** t1[ℓ1−1] and t2[ℓ2−1] carry other labels (§1). t3[ℓ3−1] lies in R4, while X20's t3-vertices lie in R5 and R6.
- **t2[jw±1]:** these have index ≤ β < α, and X20's only t2-vertex is t2[α].
- **t3[a±1]:** these lie in t3[0..10−x] (or are b6). X20's t3-indices are ≥ 11 − x.
- **t3[b±1]:** these have index in [ℓ2−5, 20−x]. X20's t3-indices are ≤ ℓ2 − 6 or ≥ 21 − x.

So no neighbour of w carries X20. **(PC) fails** in all four shapes.

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 1 and v's V's on t3 and t2 is impossible:
- v191 closes b6 on an F2-cut;
- v192 and v193 reduce t3V on an F2-cut to the four shapes;
- §4 closes the four shapes.

By the mirror (v160 §1, t1 ↔ t2), **L1 type 2 with r2 = 3, c′ = 1 and V's on t3 and t1 is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3:
  - c′ = 0 with one V on each G2-thread;
  - c′ = 1 with V's on (t1, t2) and t1V on an F2-cut.

  These are in type-12 notation; type 2 is the mirror.
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
