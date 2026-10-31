# Actual Tuscan11 distinct-centre 4+4, class (b) with d = 1 — impossible (branch-vertex residue lemma)

Actual `/bin/date` before this body: **Mon Oct 26 10:33:12 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting and imports

Class (b) is as in v54 §2 and v57 §2 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`):
- F_1 = T1 L_w T1^- L_v and F_2 = T2 L_w^- T2^- L_v^-;
- a = |T1|, b = |T2|, p = |L_v|, q = |L_w|.

Here d = 1, so r_1 = 5, r_2 = 6, b = a+5 and 2a+p+q = 50.

**Imports:**
- the cross-path lemma (L1) and boundary coincidence (L3) of v57;
- rule (R), the bd chain and the shift-5 chain of v49 §4 and v50 §2;
- distinct cut labels;
- the **exchange identity**: for two rows, the labels of the vertices in one row but not the other equal those of the vertices in the other row but not the first, since every row carries all 11 labels once;
- the same rule-(R) comparison of the two passes of a doubly traversed thread used in v60 §3 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`).

Nothing from v73/v74 is used.

**Positions.**
- F_1 has length 50: T1 forward at [0,a], L_w at [a, a+q], T1^- at [a+q, 2a+q], L_v at [2a+q, 50].
- F_2 has length 60: T2 at [0,b], L_w^- at [b, b+q], T2^- at [b+q, 2b+q], L_v^- at [2b+q, 60].
- β ∈ 1..10 is F_1's least positive boundary on the forward T1 pass. γ is the least positive boundary of the backward T1 pass, in T1-coordinates.
- β' and γ' are the same for F_2 on T2.
- Since T1-coordinate s sits at F_1-position 2a+q−s on the way back, and similarly for F_2, we get γ ≡ 2a+q−β and γ' ≡ 2b+q−β' ≡ 2a+q−β' (mod 10). Hence

      γ' − γ ≡ β − β'  (mod 10).          (★)

**No row meets both passes of its thread.** Such a row would contain a whole loop together with both visits of its branch vertex, i.e. one label twice. Within each loop, each face has at most one row lying on the loop (a **gap row**), by (L1).

## 2. The four rows at a branch vertex

Let z ∈ {b_v, b_w} with loop L of length ℓ. Measure L from the visit where F_1 enters L (coordinate 0) to where F_1 leaves it (coordinate ℓ). F_2 runs the other way.

**The four z-rows:**
- F_1's row P0 contains the 0-visit of z, with L-part [0, c]. F_1's row Pℓ contains the ℓ-visit, with L-part [ℓ−d, ℓ].
- F_2's row Q0 contains the 0-visit, with L-part [0, α]. F_2's row Qℓ contains the ℓ-visit, with L-part [ℓ−β0, ℓ].
- With g1, g2 ∈ {0,1} the gap-row counts, ℓ = c+d+10·g1 = α+β0+10·g2.

**Residues.** From the boundary positions:
- at b_v: α ≡ −β', β0 ≡ −γ', c ≡ −γ, d ≡ −β;
- at b_w: α ≡ γ'−b, β0 ≡ β'−b, c ≡ β−a, d ≡ γ−a.

For example, P0 at b_w is the forward F_1 row containing T1-coordinate a, whose L_w-part ends at the next boundary, at a residue of β−a.

With Δ := β'−γ and (★), these give

    c − α ≡ Δ at b_v,        c − α ≡ β − γ' + 5 ≡ Δ + 5 at b_w   (mod 10).

### Lemma G (a gap forces offset 4, 5 or 6)

**Claim.** If either face has a gap row on L, then c − α ≡ 4, 5 or 6 (mod 10).

**Proof.** A gap row lies on L (possibly ending at z), so it does not leave L. Hence it is clean against every overlapping row of the other face.

*Case g2 = 1, g1 = 0.* Then c, d ≥ 1, since otherwise one F_1 row would contain z twice. So c + d ≤ 18 and ℓ = c+d ≥ 10. F_2's gap row is O2 = [α, α+10]. From c+d = α+β0+10 and d ≤ 9 we get c ≥ α+1. Also c ≤ 9 < α+10. So F_1's boundary c lies strictly inside O2. The pairs (P0, O2) and (O2, Pℓ) share single stretches with k = 10−(c−α) and k = c−α. Rule (R) gives c−α ∈ {4,5,6}.

*Case g1 = 1, g2 = 0.* Symmetrically, α−c ∈ {4,5,6}.

*Case g1 = g2 = 1.* Here O1 = [c, c+10] and O2 = [α, α+10]. If c = α, the vertices L[c] and L[c+10] are boundaries of both faces, which doubles a cut (if c = 0, z itself is a boundary of both faces). Say c > α; the other case is symmetric.
- (O2, O1) is clean with k = c−α, and (P0, O2) is clean with k = 10−(c−α). So c−α ∈ {4,5,6}.
- **c−α = 5:** (P0, O2) and (O1, Qℓ) are clean, with starts α−5, α, α+5, α+10. This is a shift-5 chain.
- **c−α = 6:** (P0, O2) and (O1, Qℓ) are clean k = 4 pairs, with starts α−4, α, α+6, α+10. This is a bd chain, whose middle 5-path [α+6, α+10] lies inside L.

So c−α = ±4. In every case c−α ≡ 4, 5 or 6 (mod 10). ∎

### Lemma N (no gap forces equal crossing lengths)

**Claim.** Suppose neither face has a gap row on L. Suppose also that each z-row meets only its thread next to z: P0 = X[10−c..1], z, L[1..c] and Pℓ = L[ℓ−d..ℓ−1], z, X[1..10−d], with X F_1's thread; Q0 = L[α..1], z, Y[1..10−α] and Qℓ = Y[10−β0..1], z, L[ℓ−1..ℓ−β0], with Y F_2's thread. All these thread vertices are interior. Then α = d and β0 = c.

**Proof.** Now α, β0, c, d ≥ 1 and ℓ = α+β0 = c+d. If α = c, then L[α] is a boundary of both faces (a doubled cut). Take α > c, so β0 < d; the case α < c is symmetric. Write x_i = L(X[i]), y_i = L(Y[i]) and λ_j = L(L[j]).

- Exchange of Q0 and P0, which share z and L[1..c]: {λ_(c+1)..λ_α} ∪ {y_1..y_(10−α)} = {x_1..x_(10−c)}.
- Exchange of Qℓ and Pℓ, which share z and L[α..ℓ−1]: {y_1..y_(10−β0)} = {λ_c..λ_(α−1)} ∪ {x_1..x_(10−d)}.
- Pℓ contains L[c+1..α] and X[1..10−d], so {λ_(c+1)..λ_α} avoids {x_1..x_(10−d)}. The first identity then places these α−c labels in {x_(11−d)..x_(10−c)}, so α−c ≤ d−c.
- Q0 contains L[c..α−1] and Y[1..10−α]. The second identity places these α−c labels in {y_(11−α)..y_(10−β0)}, so α−c ≤ α−β0.

Hence α ≤ d and β0 ≤ c. With α+β0 = c+d, both are equalities. ∎

### Lemma T (nearly equal pass residues forbid an inside row)

**Claim.** Let a face traverse a thread T of length t twice, with pass residues σ and τ in T-coordinates and τ−σ ≡ 0 or ±1 (mod 10). Then no row of either pass lies strictly inside T, i.e. as [s, s+10] with 0 < s and s+10 < t.

**Proof.** Suppose Q = [s, s+10] is such a row, with s ≡ σ. The other pass covers T, so one of its rows Q' contains the coordinate s+5. Its start s0 ≡ τ lies in (s−5, s+5], so s0 ∈ {s−1, s, s+1}.
- **s0 = s:** T[s] is a boundary at both of its visits, which doubles a cut.
- **s0 = s+1:** Q and Q' share T[s+1..s+10]. The exchange identity gives L(T[s]) = L(vertex at coordinate s+11). Both are cuts, of the two passes, and they are distinct vertices. This is a doubled label.
- **s0 = s−1:** likewise L(T[s+10]) = L(vertex at coordinate s−1). If s−1 = 0 that vertex is the branch vertex, again a cut.

Each case is a contradiction. ∎

## 3. Class (b) with d = 1 is impossible

A gap (of either face) at both b_v and b_w forces, by Lemma G, both Δ ≡ 4, 5 or 6 and Δ+5 ≡ 4, 5 or 6 (mod 10). These are incompatible.

So at least one branch vertex is gap-free in both faces.

**(i) A face with a single-row pass.**
- F_2 cannot have one. That needs b ≤ 10; then the other F_2 pass meets at most 2 rows, and F_2 would need 3 gap rows, against (L1).
- Suppose F_1 has one, say β ≥ a (the γ ≥ a case is the same). Then a ≤ 10, the backward pass meets at most 2 rows, and F_1's remaining 4 rows need a gap row on each loop. So both branch vertices carry an F_1 gap. Excluded above.

**(ii) Otherwise all four passes meet at least 2 rows.** So β, γ < a and β', γ' < b, and all eight z-rows have the form required by Lemma N (their thread parts consist of interior vertices).

*Both branch vertices gap-free.*
- Lemma N at b_v gives 10−β' = α = d = 10−β and β0 = c. So β = β' and γ = γ'.
- Lemma N at b_w gives equalities of L_w-lengths. With b = a+5 these read β' ≡ β+5 and γ' ≡ γ+5 (mod 10).
- These contradict each other.

*Exactly one branch vertex gap-free.*
- Then F_2 has at most one gap row. So its two T2 passes meet at least 5 rows, and one pass meets 3 rows, giving a row strictly inside T2.
- If b_v is gap-free: Lemma N gives β = β' and γ = γ', and Lemma G at b_w gives Δ+5 ≡ 4, 5 or 6. So β'−γ' = β'−γ = Δ ≡ 9, 0 or 1.
- If b_w is gap-free: Lemma N gives β' ≡ β+5 and γ' ≡ γ+5, and Lemma G at b_v gives Δ = β'−γ ≡ 4, 5 or 6. So β'−γ' ≡ β−γ ≡ Δ−5 ≡ 9, 0 or 1.
- Either way Lemma T on T2 is contradicted.

## 4. Result

Class (b) with d = 1 is impossible (WRITTEN). With v54 (d = 7), v57 (d = 5), v58 (d = 3, two gaps) and v73+v74 (d = 3, one gap; conditional on v73 §§2–5, parent-v60 qualifications retained), **every class-(b) case is excluded**. Here d = r_2−r_1 is odd; d = 9 would give F_1 a single row containing b_v twice, which is trivially impossible.

If the unreviewed bodies are correct, the distinct-centre 4+4 core is now excluded at m = 8. This combines with the gated (a)-I result, the (a)-II line v47–v72 (R1 and R2 empty) and class (b).

The owner-written residual becomes:
- **R4:** distinct 3+5 connected;
- **R5:** distinct 3+5 disconnected, except Type I with r_P = 2 (v60);
- **R6:** all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
