# Referee report: K6.2* follow-on (SETTING-v1, K62-FG-v1 + errata v1/v2, K62-R2-v1)

**Scope.** I reviewed the embedded texts only. I did not check the hashes myself, because no tools were used. I treated K63-RES as a non-import: it was accepted only at K6.3.

**Rubric.**
- **FATAL**: a stated result is false, or its proof cannot be repaired locally.
- **MAJOR**: a false assertion, a missing load-bearing argument, or an import-boundary breach. It needs a mandatory overlay before acceptance; a repair is given below.
- **MINOR**: wording, citation or presentation.

**Index check.** The setting matches README §5 and P1:
- gcd(n_d, n_i*) = 2^min(e_d,e*) = 4. This holds because min(h_d, h*) = 0, and it forces min(e_d, e*) = 2.
- The d–c gcd is 2 and the C–C gcd is 6, because min e = min f = 1 inside C.
- α_dc = α*_dc = 1, and α_di* + α*_di* ≤ 4.
- There is one 3-marker: on i*, on some t in O, or absent (never on d).
- There is one 5-marker, placed anywhere; t = p is allowed.

## Verdicts

| Item | Verdict |
|---|---|
| Lemma D | **CORRECT** |
| Lemma OO (with the E1 Q1 text) | **CORRECT** |
| FG-62 | **CORRECT** |
| Corollary 5/6-62 | **The statement and its orientation are CORRECT.** The proof exists only by reference to a K6.3-scoped text, so it needs an overlay (M3). K62-FG §6 states the orientation backwards (M1). |
| Theorem R2-11 | **CORRECT** |
| R1 single-vertex obstruction | **CORRECT as a local LP obstruction** at an unmarked O-vertex. The concluding sentence overreaches (m6). |
| Theorem K62-R2 (e* ≤ 3) | **CORRECT after a one-line fill** of a missing Step C sub-case (M2). There is no other gap, and no explicit certificate is infeasible once y_d = 0 is written out (m1). |

Totals: FATAL 0, MAJOR 3, MINOR 8.

## 1. Lemma D

**Labels at d (LFC with x = α_di*).**
- λ_c = 3^f_c 5^h_c w_c, with weight 1/2.
- λ_i* = 2^(e*−2) 3^f* 5^h* w_* x, with weight x/4.

**Pairwise gcds.**
- Every λ_c is odd, so no gcd with an O-label has a factor 2.
- There is at most one 5-marker and x ≤ 3, so no gcd has a factor 5.
- O–O gcds are exactly 3.
- v3 gcd(λ_c, λ_i*) = min(f_c, f* + v3 x). This equals 2 only when c = t (which forces f* = 1) and x = 3.

**Conclusion.**
- Outside that exception all 15 gcds equal 3. Allowed sets then have size at most 3 (Sun(4) plus heredity), so y ≡ 1/3 is feasible. It gives 5/6 + x/12 < 1, hence x = 1.
- x = 2 never produces a gcd of 9, so x = 2 is excluded in every residue.
- x = 3 survives only when t lies in O. The exception is genuine: {t, i*, c, c′} is then allowed and the uniform weight is infeasible.
- The α* case follows from INV(a) with E6, since markers are index-defined. The pair list follows from INV(b).

The argument is valid for all e_d ≥ 2 and e* ≥ 2, so it covers R1 and R2. No finding.

## 2. Lemma OO

I re-derived it for every v in O (marked or not), both orientations, and arbitrary exponents. The labels at v are λ_u = 3^(f_u−1) 5^h_u w_u x_vu, and λ_d = 2^(e_d−1) 5^h_d w_d with load 3.

- **x_vu = 3.** λ_u is odd, λ_d has no factor 3, and a shared 5 would need two markers. So u and d are incompatible; y_u = y_d = 1 gives val = 6, which LFC(d) forbids because its bound is strict.
- **Three 1s.** These labels are pairwise coprime (one 3-marker, one 5-marker) and coprime to λ_d, so val = 6.
- **x_vu = 5 with h_d = 0.** val = 8.
- **x_vu = 5 with h_d ≥ 1.** O is then 5-free, so 5 | λ_u exactly when x_vu = 5.
  - (i) A non-five u′ (entry in {1,2,4}) shares no 2 with a five (fives are odd) and no 5. A shared 3 would need two 3-markers. So val ≥ 6.
  - (ii) Correct: λ_i* is even and 5-free, and it shares a 3 only with t, and only when x_vi* = 3. The pair {i*, t} sums to 1.
  - (iii) Correct.
- Case (ii) is redundant. Whenever all four O-entries are 5, INV(b) gives four 1s in the other orientation, whatever x_vi* is.

Only Sun(2) is used. No finding beyond m7.

## 3. FG-62

**Step bound.** For each earlier j, Φ_e W_m ⊆ Φ_e Φ_j. L0.1 with Lagrange then gives T_(m+1) = lcm(n_e, T_m)·k with k ≤ gcd(n_e, T_m)·β_ej/g_ej.

**The steps.**
- **Base.** T_2 = lcm(n_d, n_i*)·β_di* with β ≤ 3. Its prime-to-30 part is w_d w_*, and T_2 is 5-free whenever the 5-marker lies in O.
- **Adding t (f* = 1).**
  - v3(T_2) = 1 + v3(β_di*), and this equals 1 exactly when β_di* ≤ 2.
  - The 5-part of gcd(n_t, T_2) is trivial: if t = p then h_d = h* = 0, and otherwise h_t = 0.
  - So the gcd is 6, and k ≤ 6·β_td/2 = 3, since β_td ≤ 1.
- **Adding p ≠ t.** n_d, n_i* and n_t are 5-free, as are β_di* ≤ 3 and every earlier k ≤ 3. So gcd(n_p, T) = 6 and k ≤ 3. Adding p before every unmarked vertex is what keeps a hidden 5 out of T.
- **Adding an unmarked vertex.** The gcd divides 6, so k ≤ 3.

**Conclusion.**
- If t is absent, β_di* = 3 only raises v3(T_2), which does not matter for vertices with f = 1.
- Every k lies in {1, 2, 3}. So the prime-to-30 part of T is the product of the w_j for j ≠ v, and gcd(n_v, T) divides 6.
- The argument does not depend on e_d or e*. Correct.

**Which β the hypothesis concerns.** The hypothesis applies to the family that FG-62 is applied to:
- For Φ = U it needs α_di* ≤ 2.
- For Φ = U* it needs α*_di* ≤ 2.
- Either condition matters only when t lies in O.

If β_di* = 3 and t is present, then gcd(n_t, T_2) = 18 and k ≤ 9, which allows k = 7. That case is not established, and E1 Q3 now says so correctly.

## 4. Corollary 5/6-62: orientation

**Which bound needs which family.**

| Row bound | Fibre argument | Needs FG-62 for | Which requires (only when t ∈ O) |
|---|---|---|---|
| α-row (LFC) | W*U_v avoids every g_jU_jU_v | U* | α*_di* ≤ 2 |
| α*-row (VFC) | U_vW avoids every D_j | U | α_di* ≤ 2 |

- The Corollary's sentence "the α-side holds when α*_di* = 1" is therefore right.
- **Consequence.** For (α, α*)_di* = (3, 1), the 5/6-bound is established in the α-row, whose d–i* entry is **3**. It is not established in the α*-row, whose entry is 1.
- K62-FG §6, bullet 2, says the reverse (M1).

**Proof.** I re-derived both sides in the K6.2* setting (text under M3), and they are sound. As written, though, the proof says "verbatim as K63-RES §2". That is literally false: it relies on the K6.3 Lemma FG, and the K6.3 d-term 2·y_d·x_vd differs from the K6.2* d-term 3·y_d. It also lies outside SETTING's re-proof boundary (M3).

## 5. Theorem R2-11

**Row lemma.** Assume e_d = 2, v unmarked, entries in {1,2,4} by Lemma OO, and at most two fours.

**Gcd structure.**
- 1-entries are isolated.
- Even entries have pairwise gcd 2, except four–four, which is 4.
- d has type 2·5^h_d, with 2-part exactly 2, so it behaves as one more two.

**Hereditary allowed sets.** i* has weight 0 and drops out by heredity. What remains:
- singletons;
- pairs of even entries, including d;
- triples containing both fours, including {d, f1, f2}, whose weights sum to 1/2 + 1/4 + 1/4 = 1;
- no 4-sets: some 3-subset has at most one four, so all its gcds are 2, which Sun(3) forbids.

**Value.** The weights 1, 1/2, 1/4 with y_d = 1/2 are feasible, and val = 4 + 3/2 = 11/2. This is excluded by the 5/6-bound but not by the plain bound val < 6, as intended.

**Main argument.**
- The pair (1, 1) satisfies the FG-62 hypothesis for both U and U*, so both bounds hold at an unmarked v.
- So there are at least three α-fours and at least three α*-fours among the same four positions.
- They overlap in at least two positions, where α + α* = 8 > 6, contradicting INV(b).

This is correct for every e*. The citation of Lemma D inside the proof is unnecessary.

## 6. R1 obstruction (§5)

**Types in the α-row.** Take e_d ≥ 3, e* = 2, x_vi* = 1 and no 5-marker.
- u1, u2: type 4.
- u3, u4: type 2.
- i*: type 2·3^(f*−1).
- d: type 2^(e_d−1), divisible by 4.

**Gcd graph.** {u1, u2, d} have pairwise gcd 4, and every other pair has gcd 2. No 3 or 5 is shared; the 3-marker is inert wherever it sits.

**Allowed sets.**
- all pairs;
- triples containing two of {u1, u2, d};
- 4-sets {u1, u2, d, z};
- no 5-sets.

**Dual certificate.** Weight 2 on {u1,u2,d,u3}, weight 2 on {u1,u2,d,u4} and weight 1 on {i*}. This covers the loads (4,4,3,2,2,1), so weak duality gives val ≤ 5. The α*-row is the same up to renaming. INV at v and Lemma OO both hold.

**Status.**
- All three dual sets are allowed by definition. So this bounds the LP whose constraint family is all λ-allowed sets, and no Sun theorem is used.
- It obstructs the single-row method at an unmarked O-vertex only. It claims nothing about a symmetric α-matrix, other rows, or a group that realizes the configuration.
- Overreach: the sentence "closing R1 needs constraints coupling several vertices" is not supported. Single-row arguments at i*, d, t and p are untested, and K62-A and K62-R2 are themselves single-row arguments at i* (m6).

## 7. Theorem K62-R2 (e* ≤ 3)

**§0 (reduction).** Correct. Inversion preserves e_d, e*, t and p and swaps (α, α*). So it suffices to exclude (α, α*)_di* = (3, 1).

**Step A.** Correct.
- d has load 9/2 at i*.
- c is compatible with d exactly when α = 3, or when h_d ≥ 1 and α = 5.
- The certificate is feasible in both sub-cases: a compatible pair shares only 2 or 5, so its larger entry is at least 2.
- In fact a single incompatible c with α ≥ 2 already contradicts LFC. This is not needed.
- So |S| ≥ 3, z ≤ 3 on S, and z = 1 wherever α = 5.

**Step B.** Correct.
- **Chain d, t, p, rest.**
  - Adding t: k_t = 1, because gcd(n_t, n_d) = 2 and α_td = 1.
  - Adding p, then each unmarked vertex: k ≤ 3.
- **Index of the intersection.**
  - The prime-to-30 part of T is the product of the w_j for j ≠ i*.
  - When h* ≥ 1, 5 does not divide T.
  - So gcd(n_i*, T) = 2^min(e*, v2 T)·3 ≤ 3·2^e* ≤ 24.
- **Measure and bound.** This gives μ(U_i* W) ≥ 1/24, and therefore the bound (B): val* ≤ 23/4.
- **Orientation.**
  - The chain never touches the d–i* pair, so no hypothesis on β_di* enters.
  - (B) is an α*-row bound, from VFC at i*.
  - That is consistent with α*_di* = 1: d's α*-label is 5^h_d w_d, with load 3/2.

**Step C.** I checked every branch under each 5-marker position: none, d, i*, t = p, p in S, p = r, and p in T3.
- The types and facts (G1)–(G3) are correct.
- The "generic" claim is correct: inside K every gcd is 3, except that gcd(t, p) contains 5 exactly when p ∈ T3 and z_t = 5, which is case II.2. When t = p the threes are 5-free.

The branches:
- **I.1** (no fives, k3 = 0). d is isolated.
  - If z_t = 3, t is isolated too, and val* ≥ 15/2.
  - Otherwise there are at most two fours (t and r), the label gcds equal the z-gcds, and val* ≥ 13/2.
- **I.2** (fives only at t or r). s is chosen in S∖{p}, which is right because p's type shares 5 with every five. val* ≥ 6.
- **II.1, k3 = 4.** val* ≥ 4 + z_t/3 + (3/2 or 1), which is at least 35/6.
- **II.1, k3 = 3** — four cases for r:
  - (a) r meets nothing in K ∪ {d}: val* ≥ 35/6.
  - (b) r meets t but no three:
    - if d is isolated, val* ≥ 37/6 when z_r ≥ 2, and 41/6 when z_r = 1 (which forces r = p and z_t = 5);
    - if d is not isolated, r is a five, and val* ≥ 20/3;
    - "a five t with r not a five" is vacuous.
  - (c) r meets a three: then r is a five, the three is p, and h_d = 0, so val* ≥ 19/2.
  - (d) **r meets d only: MISSING (M2).**
- **II.1, k3 = 2.** val* ≥ 13/2; with a five outside K, val* ≥ 8 with y_d = 0; if some r meets a three, val* ≥ 19/2.
- **II.1, k3 = 1.** val* ≥ 6, with the exception case at 13/2.
- **II.2.** For k3 = 4, 3, 2, 1 the values are 37/6, at least 37/6 (or 19/2), at least 13/2, and at least 15/2.

**Margin.**
- The minimum value 35/6 occurs at II.1 k3 = 4 (z_t = 1, d isolated) and at II.1 k3 = 3 case (a) (z_t = z_r = 1, d isolated).
- These values are LP-exact. For the K-block at k3 = 4, put dual weight 1/6 on each {t,a,b} and 5/6 on each {a,b,c}.
- So the method's margin over 23/4 is exactly 1/12, and it fails at e* = 4, where the bound is 47/8 > 35/6. §4 says this correctly.

## Findings and minimal repairs

### MAJOR

**M1 — K62-FG §6, bullet 2: orientation inverted.** The error survives both errata. It does not support any theorem here, but it is a false claim about what is established. Replacement text:

> "R2 with {α_di*, α*_di*} = {1,3}: open. FG-62 holds for the family whose d–i* entry is 1. By Corollary 5/6-62 this gives the 5/6-bound in the *opposite* row, the one whose d–i* entry is 3 (for (3,1), the α-row). The row lemma then gives at least three 4-entries in that row at every unmarked v. The row whose d–i* entry is 1 has only the plain LFC/VFC bound at v. FG-62 is not established for the family whose d–i* entry is 3."

(For e* ≤ 3 this is superseded by K62-R2.)

**M2 — K62-R2 §3, II.1, k3 = 3: missing sub-case.** This sub-case is load-bearing.
- **The case.** r is compatible with d but with nothing in K; that is, h_d ≥ 1, z_r = 5 and z_t ≠ 5.
- **Why it is missed.** It falls in none of the three bullets ("meets nothing of K∪{d}", "meets t", "meets a three"). Reading "y_d as before" would make {r, d} infeasible.
- **It is reachable at row level.** Take S = T3 with α = 3, α_i*r = 1 and α*_i*r = 5.
- **Insert:**

> "If r meets d but nothing of K: y = 1/3 on K, y_r = 1, y_d = 0. Every set through r lies in {r, d}, so val* ≥ 3 + 1/3 + 5 = 25/3."

**M3 — Corollary 5/6-62: proof given only by reference to K63-RES §2.** K63-RES §2 is accepted only at K6.3. "Verbatim" is literally inaccurate, because both the FG input and the d-term differ. Erratum v2's phrase "with their own proofs" is also inaccurate for the Corollary, and its reference to "(B)" is undefined in K62-FG. Overlay text:

> "Normalise g_v = 1. This conjugates U* and W* by g_v^−1 and leaves indices, α and α* unchanged, so FG-62 applies to the conjugated family.
>
> **α*-row.** Assume FG-62's hypothesis holds for Φ = U. Put W = ∩_{j≠v} U_j. Then U_vW ⊆ U_vU_j and D_j ∩ U_vU_j = ∅ (V1), so ∪D_j ⊆ G∖U_vW. By L0.1, Lagrange and FG-62, μ(U_vW) ≥ 1/6. The VFC count, with μ(D_j) = α*_vj/g_vj (INV(b)) and (V3), gives Σ y_c α*_vc + 3y_d ≤ 5 for every λ*-feasible y.
>
> **α-row.** Assume the hypothesis holds for Φ = U*. Put W* = ∩_{j≠v} g_jU_jg_j^−1.
> - Suppose w ∈ W* lies in g_jU_jU_v.
> - Then g_j a g_j^−1 ∈ g_jU_jU_v for some a ∈ U_j, so g_j ∈ U_vU_j and g_jU_j meets U_v, a contradiction.
> - So the left U_v-cosets inside W*U_v (at least n_v/6 of them) meet no g_jU_j.
> - The LFC (a)–(c) count then gives Σ y_c α_vc + 3y_d ≤ 5 for every λ-feasible y.
>
> When t ∈ O, the α*-row bound needs α_di* ≤ 2 and the α-row bound needs α*_di* ≤ 2."

### MINOR

- **m1.** In K62-R2 Step C, write y_d = 0 explicitly in four places: II.1 k3 = 3 "five r" (where {d, r, t} is allowed, since gcd(d, r) = 5); II.1 k3 = 2 "five outside K" (where the value is ≥ 3 + 5, not 3 + 2 + 3/2); and I.2 and II.1 k3 =

1 whenever a five is compatible with d (h_d ≥ 1). With y_d = 0 every stated certificate is feasible, and the stated values already leave d out.
- **m2.** Fix three wording points in K62-R2 Step C:
  - II.1 k3 = 3: "a five t with r even" should read "with r not a five". t's type 3^F·5 is odd and shares no prime with z_r when z_r ∉ {3, 5}.
  - II.1 k3 = 1: "standard weights … a five gives 5" should spell out the weights. If R contains a five, put y = 1/k5 on the fives of R, 0 on the rest of R, and y_d = 0. Otherwise use the ROW-U standard weights on R, whose value is at least 3 by E8.
  - The letter r names the vertex outside S in Case I and the vertex outside K in II.1. Rename one of them.
- **m3.** K62-R2 pins K62-FG together with erratum v1 only. Erratum v2 (written 04:03:19) postdates K62-R2 (04:01:48), yet it is needed for the companion's citation chain: the TG deletion, the L0.1 attribution, the Φ renaming and the normalisation. The mandatory reading set is SETTING, FG, E1, E2 and R2, plus the M1–M3 overlay.
- **m4.** K62-R2's own proof uses only Sun(2), Sun(3) and Sun(4). The combined statement "with K62-A, every K6.2* configuration with e_d = 2 and e* ≤ 3 is excluded" also inherits **Sun(5)**, which is computer-assisted, from K62-A (verdict c792dc68 lists Sun instances 2, 3, 4, 5). Say so.
- **m5.** The ROW-U standard weights are accepted, literally, only for K7 rows (six unmarked neighbours, g = 6). K62-R2 applies them to sub-rows of the i*-row, in I.1 and in II.1 k3 = 1. This is valid by the gcd-matrix transfer principle, which should be stated:
  - whether a set is allowed depends only on the pairwise gcd matrix of its labels;
  - a block whose elements are incompatible with every other element of positive weight can be weighted separately.
  
  This is the principle of the K62-A parent overlay A-m1.
- **m6.** Repair the R1 obstruction text (§5) in four places:
  - Replace "closing R1 needs constraints coupling several vertices … FG-62 + LFC at one vertex cannot do it" with: "the single-row LFC/VFC method with the 5/6-bound at an unmarked O-vertex cannot exclude R1; rows at i*, d, t, p are not examined."
  - Replace "configuration data" with "row data".
  - Drop the restriction "3-marker on i* or on a vertex of O with entry 2". The 3-marker plays no role in this row.
  - When t ∈ O, note that "FG-62 in both orientations" presupposes (α, α*)_di* = (1, 1).
- **m7.** Three optional clean-ups:
  - Lemma OO (ii) can be dropped: four fives give four inverse 1s whatever x_vi* is.
  - R2-11's proof does not need to cite Lemma D.
  - In the Corollary, "if FG-62 holds for V = U*" should read "if the hypothesis of FG-62 holds for Φ = U*".
- **m8.** Two citation points:
  - In Lemma D (α* case) and K62-R2 §0, "same indices and markers" should cite E6 explicitly. R1, R2, t, p and e* ≤ 3 are all defined from the indices, so the inverted configuration stays in the same residue.
  - Optionally, Step A can record the stronger fact it proves: every c outside S has α_i*c = 1.

## Import closure (as traced)

**Accepted imports:**
- **R0** (README §1), including preservation of conjugated intersections (verdict 8621e744, item 6). Used in R2-11 and K62-R2.
- **K6.2* definition with P0/P1** (README §§2, 5; verdict 73a25ba6). Used in SETTING.
- **K62-A** (verdict c792dc68). It fixes the residue split in SETTING and enters K62-R2's combined statement. Its own closure includes Sun(2)–Sun(5); Sun(5) is computer-assisted.
- **L0.1 with Lagrange** (README §0), per E2 Y1. Used in the FG-62 steps and final bound, in Corollary 5/6-62, and in K62-R2 Step B.
- **E1 range 1 ≤ α ≤ g − 1**, via L0.2. Used for α_dc = 1, β ≤ g − 1 and β_td ≤ 1.
- **LFC (a)–(d) and INV (a)–(b) with E6** (verdict 8621e744).
- **VFC (V1)–(V4) and the VFC count** (rules-k7-v1 §2; verdict 73a25ba6).
- **ROW-U standard weights with E8** (verdict 8621e744). Used in K62-R2 Step C, through the transfer principle (m5).
- **Sun(2) (L0.6), and Sun(3), Sun(4) (Zhu)**, only through LFC (c) and VFC (V3). Sun(5) and Sun(6) are not used in these files.

**Not used:** TG (deleted by E2 Y1), the T rule, RPLP, CLIQUE, any K63-RES lemma (it serves only as a proof template), Sun(7), and any computation.

**Internal candidates.** Lemma D, Lemma OO, FG-62 and Corollary 5/6-62 feed R2-11, which feeds K62-R2. K62-R2 is therefore conditional on all five being accepted.

**Computation.** "No computation is a premise" is true for the arguments in these files. Computer-assisted Sun(5) enters only through K62-A, and only in the combined e_d = 2, e* ≤ 3 statement.

## Borrowed proofs whose literal scope must be re-derived

1. **Corollary 5/6-62, borrowed from K63-RES §2(a),(b)**, which was accepted at K6.3 only. It must be re-derived (M3). My re-derivation is sound once FG-62 replaces K63-RES Lemma FG and the K6.2* value (d-term 3·y_d) replaces the K6.3 one (2·y_d·x_vd).
2. **FG-62's final measure bound, "as in K63-RES §1".** E2 Y1 (superseding E1 Q2) now cites L0.1 with Lagrange. That argument holds for any two subgroups, so nothing more is needed.
3. **ROW-U standard weights**, whose literal scope is K7 rows. They are used on sub-rows at i*, which is valid through the transfer principle (m5).
4. **No other borrowing:**
   - Lemma D replaces K62-A Step 1 with a proof inside the file.
   - K62-R2 Step B re-proves the VFC-side disjointness inside the file.
   - The R2 row lemma supplies its own explicit weights.

## Frontier after the overlays, if accepted

- **K6.2* with e_d = 2.**
  - Excluded for e* ≤ 3, by K62-A, R2-11 and K62-R2.
  - For e* ≥ 4, the pair (1, 1) is excluded by R2-11, which has no restriction on e*.
  - For e* ≥ 4, the pairs {1, 3} remain **OPEN**. After the M1 correction, the (3, 1) normal form still supplies the α-row 5/6-bound, hence at least three α-fours at every unmarked O-vertex, together with Step A at i*.
- **R1 (e_d ≥ 3):** **OPEN** in every sub-case.
- **Marked K7:** **OPEN**; not examined here.
- **Full Sun(7):** **OPEN**. This report makes no Sun(7), novelty or priority claim. It is a model review of written proofs, with no Lean check and no human review.
