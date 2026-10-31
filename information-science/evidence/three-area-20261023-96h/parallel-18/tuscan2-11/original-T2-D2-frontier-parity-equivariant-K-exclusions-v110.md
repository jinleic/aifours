# Original Tuscan-2(11): what the distance-two coupling yields by written means — parity, orthogonal partial Latin squares, and exclusion of equivariant turn systems

Actual `/bin/date` before this body: **Mon Oct 26 15:56:26 PDT 2026**. InfoRecursiveMDS18-2.

**Status.** NEW exact WRITTEN CANDIDATE: not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, chosen row or chosen control.

**Scope.** This is a second pivot packet after v108 (SHA256 `b1c6504a65fa911aeb016d77daca5c6b24f3efee893ae7de539b7354b67802ed`) and v109 (SHA256 `3f5d69a66c03e10ace51ea65c532b490cdfc5faf383a77c70d77c73be8b1b98d`).
- §§1–2 concern every eligible array.
- §3 excludes two algebraic turn-system mechanisms for every Tuscan-1(11) array. It uses (R1)–(R2) only, as is stated there. These are mechanism exclusions for any construction attempt, not a substitute family for the book target.

Notation is that of v1 (SHA256 `e54953336e35bd7a535d147ca6a564f9db30ddca966f1ad31dc58485167d8275`) and v109.

## 1. Parity: the Latin structure adds no obstruction

For any Latin square Q of order n, write:
- ε_rows for the product of the signs of the row maps b ↦ Q(a,b);
- ε_cols for the product of the signs of the column maps;
- ε_sym for the product of the signs of the symbol maps σ_x (a ↦ b with Q(a,b) = x).

**Identity.**
ε_rows · ε_cols · ε_sym = (−1)^(n(n−1)/2).

**Proof.** On X×X, put A(a,b) = (a, Q(a,b)), B(a,b) = (Q(a,b), b), S(a,x) = (σ_x(a), x) and θ(u,v) = (v,u). Then:
- sgn A = ε_rows and sgn B = ε_cols;
- sgn S = ε_sym and sgn θ = (−1)^(n(n−1)/2);
- B∘A^(-1) = θ∘S, both being the map (a,x) ↦ (x, σ_x(a)). ∎

**Applied to the Latin case of v109 Theorem B** (n = 11, symbol maps K_x):
- θ∘S is the turn map T on the 110 arcs, plus 11 fixed diagonal points. So sgn T = (−1)^(110−f) = (−1)^f, where f is the number of faces.
- This gives Π_x sgn K_x = (−1)^(f+1) = sgn τ, which is exactly v1 eq. (4).
- It also gives ε_rows·ε_cols = (−1)^f. That relation is satisfiable for every f, because ε_rows and ε_cols are otherwise free.

So the distance-two Latin structure yields no parity obstruction beyond the T1 identity (4).

## 2. Orthogonal partial Latin squares (all eligible arrays)

On the 99 cells (a,b) that carry a distance-two event, let:
- μ(a,b) be the middle symbol;
- ρ(a,b) be the row containing the event.

Both are partial Latin squares:
- μ by v109 §2;
- ρ because a symbol occurs once per row, so row a of ρ and column b of ρ list distinct rows.

They are **orthogonal**. A pair (x, R), with x internal to row R, determines the position of x in R, hence the cell. Under (R1)–(R2), (R3) is equivalent to: μ and ρ are well-defined functions on the distance-two cells. When defined, they are automatically an orthogonal pair.

This is an exact reformulation, recorded for completeness. It adds no counting constraint.

## 3. Mechanism exclusions: no equivariant turn system at order 11

Call the turn system {K_x} **G-equivariant** for a group G of symbol permutations if K_(gx)(ga) = g·K_x(a) for all g, x, a. The boundary data p and f are NOT assumed equivariant, and the square itself need not be G-invariant. (A G-invariant square is already impossible: `unrestricted-prime-order-asymmetry-v1.md`.)

### 3.1 Translation equivariance on Z_11

Suppose K_(x+t)(a+t) = K_x(a) + t.
- Then K_x(a) = x + κ(a−x), where κ = K_0 permutes Z_11^*.
- An arc of difference d = x − a goes to an arc of difference θ(d) = κ(−d), a permutation of Z_11^*, and its tail advances by d.
- A T-cycle over a θ-cycle of length L ≤ 10 and difference sum S has length L if S = 0, or 11L if S ≠ 0.
- Faces have length in 10ℤ and at least 20 (v1 Theorem 2; ≥ 2 rows). S = 0 forces length L ≤ 10, which is too short. S ≠ 0 forces 10 | 11L, so L = 10, so θ is one 10-cycle with sum Σ_(d≠0) d = 0, a contradiction.

### 3.2 Multiplicative equivariance on Z_11 (G = Z_11^*)

Suppose K_(gx)(ga) = g·K_x(a) for all g ∈ Z_11^*.

**Shape of the turn system.**
- K_0(a) = c·a with c ≠ 1, since K_0 has at most one off-0 fixed point (v1 Lemma 1).
- K_x(a) = x·K_1(a/x) for x ≠ 0.
- κ_0 := K_1(0) is neither 0 nor 1. If κ_0 = 0, every K_x with x ≠ 0 fixes 0, so p(x) = f(x) = 0 for ten x. Then 0 sits in column 9 of ten rows, which is impossible.

**The arc dynamics.** Type an arc as:
- I_r: (a, ar) with a ≠ 0 and r ∉ {0,1};
- II: (y, 0);
- III: (0, z).

Put ω(r) = K_1(1/r). It maps Z_11 ∖ {0,1} onto Z_11 ∖ {1, κ_0}, and ω(r_0) = 0 for exactly one r_0. Then T acts on types by:
- I_r → I_(ω(r)) for r ≠ r_0, multiplying the tail by r;
- I_(r_0) → II;
- II → III, with multiplier c;
- III → I_(κ_0), with multiplier 1.

This is a permutation σ of the 11 types, and each type carries 10 arcs.

**There is only one face.**
- A σ-cycle made of I-types only lifts to faces avoiding the symbol 0. But every row contains 0. So σ is one 11-cycle.
- Its total multiplier is P = c · Π_(r∉{0,1}) r = −c, by Wilson's theorem.
- The faces over σ have length 11·ord(P). This lies in 10ℤ only if ord(P) = 10, which gives one face of length 110.

**The Hamilton windows fail.**
- Z_11^* commutes with T and acts freely on that face, so it acts by shifts forming the subgroup ⟨11⟩ of Z_110.
- Hence some generator g_0 satisfies s_(i+11) = g_0·s_i for the face's symbol sequence.
- The 11 rows start at φ + 10m. Their offsets mod 11 run over all of 0..10.
- Offset 0 forces (s_0..s_10) to be a permutation.
- Offset 1 forces g_0 s_0 = s_0, so s_0 = 0.
- Offset 2 forces {g_0 s_0, g_0 s_1} = {s_0, s_1}, so s_1 = 0 = s_0. Contradiction.

**Theorem 3.** No Tuscan-1(11) array, and a fortiori no eligible Tuscan-2(11) array, has a turn system that is translation-equivariant or multiplicatively equivariant on Z_11. This holds with no Latin-column, distance-two or square-invariance assumption.

This extends the source-family exclusions of v24 §6 (single-0 relocation; one-rainbow-path insertion) and v109 §6 to the level of turn systems.

## 4. Frontier

Taken with v1 §7, v108 and v109, the distance-two coupling is exact for all arrays:
- it is the near-disjointness of the eleven K-matrices, equivalently orthogonal partial Latin squares;
- in the Latin case it is absorbed by an idempotent Latin square.

By written means, the following do NOT close the target:
- counting (v108 C3);
- parity (§1);
- the natural algebraic turn-system mechanisms (§3, excluded already at the T1 level).

The remaining step is exactly v1 §7: realize, or exclude for all arrays, a near-disjoint K-system with a ten-periodic Hamilton cut system.

## 5. Result

- **WRITTEN:** the Latin-square sign identity and its exact reduction to v1 (4) in the Latin case (§1).
- **WRITTEN:** the orthogonal-PLS reformulation (§2).
- **WRITTEN, (R1)–(R2) only:** Theorem 3 (§3).
- **Frontier statement:** §4.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
