**DISPOSITION: ACCEPT-WITH-FIXES** (advisory only; I have no gate authority)

Theorem K0* (00:156-159) is correct at its displayed scope. I found **0 FATAL, 0 MAJOR and 6 MINOR** issues. Every fix is wording or scope, and none changes a formula, case or conclusion. I ran no computations and checked no hashes or paths.

## Findings (all MINOR)

**m1 — 00:55-59 (with 00:28).** H0's H, κ, o_F, m and β, including the κ inside I(∅), must be those of the named representation.
- H depends on the representation. Writing σ_y² as one block versus σ_y [ ] σ_y shifts (H, o_F) by (−1, +2). Both window systems are exact, but they differ.
- Every use in the file is consistent: (Z0), CH and Step 5 use maximal decompositions, and PM0 compares two representations with H′ = H.
- *Repair:* "For a representation (H, κ, o_F, m, β computed from its own blocks)…".

**m2 — 00:145.** CH uses "R_Q ≤ R ≤ 2p−1", but this is not among CH's hypotheses (00:141-143).
- It follows from (Z0): A ≤ 2p−1 and B = 0.
- It is what makes the cap p inactive.
- *Repair:* cite (Z0).

**m3 — 00:171-180.** Two bookkeeping facts are implicit. Both are true; they should be stated.
- (i) At least one FUS step occurs, because g(w) ≥ 1 and g(w_end) = 0 by Step 2. So w′ exists, and possibly w′ = w.
- (ii) After the Step 4 merges, w″ is re-indexed so its empty run(s) are R_t (and R_{t+1}). The surviving adjacent blocks keep the names S_{t−1}, S_t (and S_{t+1}) with unchanged values and parities; their lengths grow only by even amounts.
- Optional: phrase 00:165-166 conditionally. An odd–odd double fusion would output a length-(4p−2) avoider with H = p, contradicting (Pairs).

**m4 — 00:159 (with 00:70-72).** The dependency line lists Davenport-alpha, but (V) is never used.
- o_F ≥ 1 comes from (Z0) (00:68-69, 00:162).
- This is harmless over-listing. *Repair:* drop it, or mark (V) "not used for K0*".

**m5 — 00:157-159, 00:207-208.** Two claims cannot be checked from this packet, because README.md is not supplied:
- "Equivalently REFL(p) holds for avoiders with κ = 0".
- Remark (1)'s "RGR avoiders in general".

What is proved is exactly 00:156-158 with κ := p−1−Σ⌊l_i/2⌋ over maximal **constant blocks**.
- On non-RGR words this differs from any count over maximal reflection runs. So "equivalently" holds only if README's REFL uses the same κ.
- Remark (1) is an unverified side claim and carries no load.
- Also make the parenthetical read "H = p−1 exactly (H ≤ p−1 for every avoider by (Pairs))".

**m6 — 00:6.** "No mathematical step, case or conclusion is changed" is inaccurate.
- Fix 1 replaced a false lemma statement. I confirm the refutation at 00:85-86: for u ≠ v, (3, σ_v) ∉ Spec(σ_v²σ_u).
- *Repair:* "no use of FUS, no case and no conclusion changed".

## Per-theorem verdicts

| Item | Lines | Verdict |
|---|---|---|
| GR0 | 00:40-54 | Correct (re-derived) |
| H0 | 00:55-65 | Correct (re-derived; m1) |
| (Z0), (Pairs), (P0), (Par) | 00:66-76 | Correct ((P0) given Theorem P). (V) is correct given Davenport-alpha but unused |
| SPEC | 00:80-83 | Correct, one-way |
| FUS r2 + FUS-step bookkeeping | 00:84-97 | Correct, both orientations, one-way |
| SL | 00:98-103 | Correct, two-way; not used by K0* |
| TR | 00:104-106 | Correct, two-way; not used by K0* |
| PM0 | 00:107-114 | Correct (k ≥ 2), one-way; also a special case of accepted PM* (09:31-39) |
| BC′ | 00:116-139 | Correct |
| CH | 00:141-152 | Correct (m2) |
| Theorem K0* | 00:154-205 | Correct at displayed scope (m3, m5) |

## Per-question audit

### Q1 — GR0 and H0

**Group law, sign and parity**
- The group law at 00:14 matches 05:11 and 06:10-11.
- (V,e)ρ_x = (V+ex, e) and (V,e)σ_y = (V+ey, −e), matching 00:47-48.
- A selection with an odd reflection count has a reflection as its product, so only even selections matter. Hence z_{k+1} = z_1, Φ is even, and C_max = F−δ ≡ Φ ≡ 0 (mod 2).
- Summation by parts (00:50) gives τ(z) = ½Σz_iθ_i, which is GRX's T(z) (08:16, 08:33-34). So the sign agrees with the accepted convention (12:30).

**Endpoints and exactness**
- For even t, admissible sizes M are even, lie in [s0, s1], and satisfy |t| ≤ M ≤ min(2E₊−t, 2E₋+t).
- Eliminating M gives exactly max(−s1, −E₋, s0−2E₋) ≤ t ≤ min(s1, E₊, 2E₊−s0), matching 00:42.
- Both directions are exact. No step uses r_i ≥ 1 or maximality.

**H0 algebra**
- τ(z_P) = 2u_P, Φ = 2m, δ = o_F−2m+2β, c = H+m−β, E₊(P) = D_P+B, and E₋(P) = E₊(P^c).
- These give ⌊hi/2⌋ = λ(P)−1 and ⌈lo/2⌉ = 1−λ(P^c). P = ∅ gives I(∅) and P = [k] gives −I(∅).
- Nothing depends on the word length.

**Accepted overlay versus new algebra**
- Accepted layer: GRX (12:7; every representation, empty gaps allowed) and PM* (12:8 with erratum M1, 12:29).
- GR0 is GRX specialised to rotation values ±1 (08:44-45).
- New in 00: H0's half-window algebra with representation-dependent H, the BC′ boost, CH, the moves, and K0*.
- I relied on neither 07's corollary H0 nor proof-GR.md (which is absent).

### Q2 — moves

- **SPEC** is correct and one-way. A cyclic rotation handles segments that wrap.
- **FUS**, both forms, checked in three cases:
  - c ≤ l;
  - c−l even;
  - c−l odd: then c−l ≤ l′−1, so take l−1 copies of σ_u and c−l+1 copies of σ_v.

  The even block is the one recoloured. FUS is one-way, original → fused, which is the only direction used.
- **FUS step:**
  - It never creates an empty run, and removes one or two.
  - H changes only in an odd–odd double fusion, where it rises by 1.
  - R ≥ 1 excludes k = 2 with both runs empty (self-fusion across the wrap).
  - The k = 2 and k = 3 cases are fine.
- **SL:** the four products are distinct because u ≠ v. The size ranges for each parity type are as stated and all nonempty for a, b ≥ 1. It is exact in both directions.
- **TR:** for every z the transfer moves one effectively positive and one effectively negative letter, so E± are invariant. It is exact in both directions; a non-maximal output is covered by GR0.
- **PM0:**
  - The patterns of w′ are the patterns of w that contain j and j+1 together or neither.
  - For these, m, β, D_P, B, H (because l_j is even) and u_P (θ′ = θ_j+θ_{j+1}) all agree. So the conditions on w′ are a subset of those on w.
  - With both neighbours nonempty the output is again maximal, and empty runs keep their neighbour values and parities.
  - Rotation order inside a run is irrelevant, since GR0 depends only on a_i and b_i.

### Q3 — BC′ boost and CH

**The boost (*) at 00:126-128**
- The boost adds exactly the residue 0 to I′(Q). It is justified because u_Q ≠ 0 and u_{Q^c} = −u_Q.
- All cases check: no boost, one side boosted, both sides boosted, and empty I′.
- The boost applies only when λ = 0. Negative λ are never boosted, correctly: boosting them would add a nonzero residue without justification.

**The BC′ arithmetic**
- |I′| ≤ p−1, so λ′(Q)+λ′(Q^c) ≤ p.
- The tiling claim holds, including when l+l′ ≤ 1.
- The choice of v_t works: the search interval has ≥ p integers, or ≥ p+1 when l+l′ ≤ 0.
- Condition (b) is equivalent to the two containments needed for the induction.
- The final step gives V_s ∈ [p+1, 2p−1] from (a) and (c). When s = 2, (b) is vacuous.

**CH**
- For intervals with B = κ = 0, λ = ⌊R_Q/2⌋+1−def(Q).
- A union of two or more parts has R ≥ 1, so def ≤ 1 and λ ≥ 0.
- A single genuine empty part with β ≤ 1 has λ′ = 1.
- R ≥ 5 is used three times, and all three uses hold at p = 5 and at R = p:
  - the largest of X, Y, Z has R ≥ 2;
  - two def-1 unions would cover the cycle, forcing R ≤ 4;
  - one of P_s, P_s^c has R ≥ 3.
- At R = p the upper sum is R+1 = p+1: tight but sufficient.

### Q4 — Theorem K0*

- **Termination:** g strictly decreases under FUS steps, and k strictly decreases under PM0 merges.
- **Step 1:** κ = 0, B = 0 and avoidance are invariant.
- **Step 2:** merging every even block gives e_F = 0 < g ≤ e_R, contradicting (P0). The output is again a maximal decomposition, so (P0) applies.
- **Step 3:** C1 and C2 are exhaustive. A double fusion has the even block in the middle, and "a, c both odd" is excluded by Step 1.
- **Step 4:**
  - e_R ≤ e_F, e_R ≡ e_F (mod 2), and e_R ≥ g.
  - k−g ≤ R and k−g ≥ o_F together give o_F ≤ p, hence R ≥ p ≥ 5.
- **Step 5:**
  - The forced (e_F, e_R) are (1,1), (2,2), (2,2), (3,3), with k = o_F + e_F.
  - I recomputed every β and λ, including the small cases: k = 2 (C1a); k = 3, where S_{t−2} = S_{t+1} (C1b) or S_{t+2} = S_{t−1} (C2a); and k = 4 (C2b).
  - All sums equal p+1. The boost is needed exactly in C1a, C2a and the C2a mirror.
  - The number of parts s is k, k−1, k−1, k−2 respectively, all ≥ 2.
- **CH and BC′:** all CH hypotheses hold for w″. w″ is an avoider because every move is applied in its avoidance-preserving direction.
- **Premises:** only Theorem P, EGZ (via Lemma AR) and the elementary lemmas. There is no RGR premise (K0, RGR-LONG) and no INV*, REFL or ROT premise.

### Q5 — assumptions, circularity, scope

- **Circularity:** none.
- **Finite premises:** none. The finite aids at 00:210 and 00:216 are not premises, and none was run here.
- **Hidden assumptions:**
  - The only one is m2.
  - Primality and oddness of p are used for 2⁻¹, EGZ and Theorem P.
  - ρ_0 letters are excluded by the hypothesis x ≠ 0.
- **Scope:**
  - Correctly limited (00:8-10, 00:209).
  - K0* applies only to words already known to have rotation letters in one pair {ρ_x, ρ_{−x}}; it says nothing about rotation values.
  - Remaining scope caveats are in m5.

## Audited versus imported

**Fully audited** (re-derived here):
- GR0, including the Ach window, and H0.
- (Z0), (Pairs), (P0) given Theorem P, and (Par).
- SPEC, FUS in both forms with the FUS-step bookkeeping, SL, TR and PM0.
- BC′, together with the Lemma BC arithmetic at 02:67-87.
- CH.
- Every step and case of K0*.
- Lemma AR's argument, given EGZ.

**Taken as imports:**
- Theorem P (06:27-28). I checked that it applies with gaps equal to the rotation runs, empty runs included.
- EGZ for C_p (classical).
- GRX and PM*, as accepted by 12; used only as cross-checks.
- Davenport-alpha (05:61-73); used only for (V), which is unused.

**Not available in the packet:** README.md, proof-GR.md, proof-DR.md, the Codex r1 note, and the finite aids.

## Unresolved core (not endorsed)

- REFL for κ ≥ 1 (the separate reduction file, not audited here).
- ROT for o ≥ 3.
- Full INV*(p).
- Ordered Olson for D_(2p).

K0* settles only rigid-rotation avoiders of length 4p−2 with κ = 0.
