# Independent review: K62-M13 A–D, corrected v2 snapshot (M13-ov applied last to C58–63)

**Reviewer and method.** claude-opus-5-5, written reasoning only, with no tools, computation, edits or delegation. Every new claim was re-derived from the embedded texts, which were treated as evidence. The M13-ov Old block matches C:58–63 verbatim; the New block was read in its place.

**Line references.** A, B, C, D and M13-ov are the pinned `K/K62-M13-*.md` files.

**Scope.** K6.2* with e_d ≥ 4, e* = 2, in orientation (α_{di*}, α*_{di*}) = (1,3). This forces t ∈ O, f* = 1 and f_t ≥ 2; the 5-marker may be anywhere admissible. (3,1) is covered only through INV (a) with E6, swapping α and α*.

## Verdict

**Packet: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR.** Every mathematical claim in A–D and M13-ov holds at its stated scope. The three MINORs concern provenance and exposition. They change no statement, centre, orientation or strictness.

| Claim group | Verdict | F | M | m |
|---|---|---|---|---|
| A1 (a)–(e) | ACCEPT | 0 | 0 | 0 |
| DG-1*, DG-2*, DG* | ACCEPT | 0 | 0 | 0 |
| C1*, C2*, budget | ACCEPT | 0 | 0 | 0 |
| B1, B2, B3 (+ B §4) | ACCEPT | 0 | 0 | 0 |
| C1w, C2, repaired rows (M13-ov) | ACCEPT-WITH-FIXES | 0 | 0 | 1 (m1) |
| CI13, CI13′ (+ C §4) | ACCEPT-WITH-FIXES | 0 | 0 | 1 (m2) |
| D4, D3 | ACCEPT-WITH-FIXES | 0 | 0 | 1 (m3) |
| L1–L4 | ACCEPT | 0 | 0 | 0 (premise pointer covered by m3) |

## A: inverted d-row (accepted imports only, no CAP/DT)

**A1(b), size bound.**
- In Γ* at d the labels are λ*_c = 3^{f_c}5^{h_c}w_c for c ∈ O and λ*_{i*} = 3n_{i*}/4 = 9·5^{h*}w_*.
- All pairwise gcds are 3, except gcd(λ*_t, λ*_{i*}) = 9.
- Sun(4) therefore puts t and i* into every 4-subset of S*_F.
- So |S*_F ∩ O| ≤ 3 and |S*_F| ≤ 4, and five-piece fibres are impossible. ✓

**A1(c), complements.** L*_j and U_jU_d are disjoint: otherwise g_j ∈ U_dU_j and g_jU_j meets U_d. Their measures sum to 1:
- 1/2 + 1/2 for c ∈ O;
- 3/4 + 1/4 for i*, which uses α_{di*} = 1. ✓

**A1(d)/(e), counting with four-piece fibres possible.**
- |A∖A_t| ≥ n_d/4 uses only |A_t| ≤ t*_t = n_d/2.
- A fibre in A∖A_t lacks t, so |S*_F| ≤ 3 and |B*| ≥ 3. The fibre U_d adds one more.
- Bounding Σ|S*_F ∩ O| by 2, by 2 + [|S*_F| = 4], and by 3 on the three fibre classes gives N_4 ≥ n_d/4 + 3, all inside A_t.
- Four-piece fibres are in fact forced: Σ|S*_F| = 13n_d/4 > 3(n_d − 1). The count routes all of them through A_t correctly. ✓

**DG-1\*.**
- Γ* has g*_d = 1, d-subgroup U_d and conjugated family (U_j), and A1(c) is SH-1(a) for Γ*.
- N*(Q) therefore counts the fibres in ∩_{c∈Q} U_cU_d. That set is a union of (W_Q, U_d) double cosets, each holding a multiple of n_d/gcd(n_d, T_α(Q)) fibres.
- The Z10 chain (every O–O step has k ∈ {1,2,4}) gives gcd = 2^{min(e_d, v2 T_α(Q))}.
- V-SHDG item 2 accepts DG-1 without α_{di*} = 1, so applying it to an entry-3 configuration is in scope. ✓

**DG-2\*.**
- From b_3 + 2b_4 + 3b_5 = n_d/2 and b_3 + b_4 + b_5 ≥ n_d/4 + 1 we get A*_4 + N*(O) = b_4 + 2b_5 ≤ n_d/4 − 1.
- The 3-subset and 4-subset sums equal b_3 + 4b_4 + 10b_5 and b_4 + 5b_5, and both re-express correctly. ✓

**DG\*.**
- (a) n_d/2^{r_Q} = 2^{4−r_Q}·(n_d/16), and n_d/16 is an integer including its odd cofactor.
  - So N*(Q) > n_d/16 forces N*(Q) ≥ n_d/8.
  - That gives N*(O) ≥ n_d/8 + 1/3, contradicting DG-2*.
  - The sum bound Σ_R 2^{−r_R} ≤ 19/16 − 2/n_d follows.
- (b) The totals 10/8 and 9/8 + 1/16 both exceed that bound.
  - G3, applied to (U_j) with Z11(a) for α, gives r_R ≤ 5.
  - It also limits deep triples to type (2,4,4) or (4,4,4) with τ_α ∈ {8, 16}.
  - r = 5 forces (4,4,4), τ = 16 and e_d ≥ 5.
- The four-subset hypothesis is stated and retained throughout. ✓

**C2\*.**
- Σ over pairs of N* = 2n_d + b_4 + 3b_5 ≤ 19n_d/8 − 3/2.
- The pair grid has r = 1 + v2 α ≤ 3 < e_d, so it is uncapped.
- Hence 4n_1 + 2n_2 + n_4 ≤ 18, which gives n_4 ≥ 2n_1 + 2.
- No four-subset hypothesis is used. ✓

**C1\*.** N*(Q) ≤ A*_4 < n_d/4 and N*(O) < n_d/8, compared against the grids, give r_Q ≥ 3 and r_O ≥ 4. These hold uncapped because e_d ≥ 4. ✓

**Budget.**
- J_O is {1,2,4}² without (4,4), because α + α* ≤ 6.
- Add accepted E3-C2 for α* (valid since α_{di*} = 1) to C2*, then eliminate N24 + N42 using the total of 10.
- This gives exactly 2N41 + 2N14 + 5N11 + 3N12 + 3N21 + N22 ≤ 6, and the stated consequences follow. ✓

## B: i*-row certificates (every positive support checked)

Family α is checked in Γ and family α* in Γ*.

| Lemma | Positive support | How prime collisions are avoided | Value | Contradicts |
|---|---|---|---|---|
| B1, k = 4 | 1-labels at weight 1; 2-labels and 4b_{c0} at ½; y_d = 0 | Odd b's are pairwise coprime, so 1-labels are isolated; {2b_c, 4b_{c0}} have pairwise gcd 2 | 1 | LFC(d) |
| B1, k ∈ {3,5} | y_{c0} = 1, y_r = 0, other y_c = 1/a_c | kb_{c0} can share only the prime k, and only with t (k = 3) or p (k = 5); that vertex is r. Covers c0 = t, c0 = p and p = t | (k+3)/6 ≥ 1 | LFC(d) |
| B2 (Γ*) | y_d = ½ and the four c ≠ t at ½ (a_c = 2 by SH(ii)) | λ_d = 3·2^{e_d−2}5^{h_d}w_d and λ_c = 2·5^{h_c}w_c; dropping t removes the only shared 3, leaving all gcds 2 | 25/24 | LFC(d) |
| B3 (Γ) | y_c = 1/a_c, y_d = ½ | λ_d = 2^{e_d−2}5^{h_d}w_d has no 3 and cannot share 5; {2b_c, λ_d} have gcd 2 | 23/24 | RC-i* (11/12) |

**B3 and RC-i\*.**
- B3 genuinely needs RC-i*, since 23/24 < 1.
- It is the α-row at i*, using gcd(n_{i*}, T_{α*}(V∖{i*})) = 12. That is V-CAP items 2–3, valid at f* = 1 in every orientation.
- B §4 follows from α + α* ≤ 6.
- The historical CONDITIONAL tag on B3 is discharged for RC-i* only.

## C: granularity, rows, cherry isolation

**C1w chain.** Each step was checked:
1. d, then t: the gcd is 2 and μ = 1/2, so k_t = 1 exactly.
2. Then p, if p ∈ O∖{t}: both d and t are 5-free.
3. Then the rest of O∖{v}: each has gcd(n_e, T_m) = 6 exactly, and comparison with d gives k_e ≤ 3.
4. i* last:
   - gcd(n_{i*}, T_0) = 12. The 2-part is 4 since e* = 2 ≤ e_d. The 3-part is 3 since f* = 1. The 5-part and w-part are trivial.
   - The witness gives k_{i*} ≤ 12·α*_{i*c0}/6 ≤ 6.

Both the witness and placing i* last are load-bearing. Comparing with d alone only gives k ≤ 12·(3/4) = 9, which admits the prime 7; this is the same obstruction as CAP's k ≤ 9 remark. With every k ≤ 6, the prime-to-30 part of T is ∏_{j≠v} w_j, so gcd(6w_v, T) = 6. The cases p = t, p = d, p = i* and p absent are all covered. ✓

**C2.** It uses B1 and B3. B3 concerns T_{α*}(V∖{i*}), a different intersection from C1w's, so there is no circularity. ✓

**Repaired rows (M13-ov:29–53).**
- **α-row (fresh proof).**
  - Take g_v = 1 and W′ = ∩_{j≠v} U*_j. Its index [G : W′] = T_{α*}(V∖{v}) is unchanged by the common conjugation.
  - Avoidance: if w = g_j a g_j⁻¹ lies in g_jU_jU_v, then g_j⁻¹ ∈ U_jU_v, so g_jU_j meets U_v.
  - The empty-fibre count is M = [W′ : W′∩U_v] ≥ n_v/6, and it includes U_v itself.
  - Then Σ y_j t_j ≤ n_v − M, which gives the bound 5/6.
  - This is a complete derivation from LFC (a)–(c), L0.1 and Lagrange. It does not use RC-O, whose opposite entry here is α*_{di*} = 3.
  - Naming: the bound that needed new granularity is the **α-row** (distinguished entry 1), proved from **α\*-granularity**. "High-family row bound" in the package should be read that way. ✓
- **α\*-row.** The same count in Γ* uses gcd(n_v, T_α(V∖{v})) | 6. That comes from accepted CAP C1, since α_{di*} = 1 and v is unmarked. This is exactly RC-O's opposite-entry-1 instance. ✓
- **i\*-rows.** RC-i* at f* = 1. No strict slack and no subset or atom grid is claimed. ✓

No RC-O instance beyond opposite-entry 1 appears anywhere in the corrected C or in D.

**CI13 is re-proved with the new granularity, not transferred.**
- **Light set.** Φ^y_v W lies in every X^v_j, misses every D′_j by (V1), and has measure ≥ 1/6.
  - For y = α this comes from CAP C1, which is within the accepted DT-A own-entry-1 scope.
  - For y = α* it comes from the new C2. This is the only place the new granularity enters.
- **Measures and labels.** INV(b) in the Φ^y-configuration gives μ(D′_j) = y′_vj/g_vj and labels λ′_j = n_j y′_vj/g_vj.
- **Step 2 (triples).**
  - Odd parts of λ′ at a, b, c, c′ and d are pairwise coprime, even when a, b, c or c′ is t or p.
  - The 2-parts are exactly 2 at a and b, at most 4 at c and c′, and at least 8 at d.
  - So every pair involving a or b has gcd ≤ 2, and each triple {a, b, j} is forbidden by (V3) with Sun(3).
- **Why i\* is excluded from step 2.** λ′_{i*} = 2y′_{vi*}5^{h*}w_* can share 3 with t or 5 with p. i* is constrained only by the step-3 containment, and nothing afterwards uses that.
- **Steps 3–5.**
  - 2/6 + 3/6 saturates the 5/6 bound.
  - Sun(2) makes y′_vc even, and μ ≤ 1/2 forces y′_vc = 2.
  - Sun(3) on {c, c′, d} gives disjointness, and 2/3 > 1/2 is the contradiction. ✓

**CI13′.**
- μ(Φ_v(Φ_a∩Φ_b)) = τ/(6y_ab) = 4/6, which equals μ(X^v_a) and μ(X^v_b).
- With containment this gives X^v_a = X^v_b, and a non-tight 4-edge then has y′ = 1.
- Only v needs to be unmarked. ✓

**C §4.**
- A (4,4,4) triple with τ = 16 and three unmarked apexes has at least two non-tight edges. A single non-tight edge would leave the opposite apex with two tight edges.
- The (2,4,4), τ = 8 forcing applies at the apex opposite the 2-edge, when that apex is unmarked.
- Each family's DG hypothesis is retained. ✓

## D: unmarked centres with marked neighbours

**Labels at unmarked v.**
- λ_u = a_u b_u, λ_{i*} = 2·5^{h*}w_*·z, λ_d = 2^{e_d−1}5^{h_d}w_d.
- The 5/6 bound reads val = 6 × (row sum) ≤ 5.

**Prime collisions.** Only three are possible:
- i* with t, when z = 3;
- i* with p, when z = 5 and p ∈ O;
- i* with d, when z = 5 and p = d.

Each certificate gives zero weight to one end of every collision that can occur.

**Certificates.** 1-labels carry weight 1 and are isolated in every row.

| Case | Zero weight | Half-weight positive labels (pairwise gcd 2) | val |
|---|---|---|---|
| D4 | i* | O-2-labels, d | 11/2 |
| D3, z = 1 | d | O-2-labels, the O-4-label, i* | 11/2 |
| D3, z = 3, a_t ∈ {1,2} | t, d | O-2-labels, the O-4-label (≠ t), i* | 11/2 |
| D3, z = 3, a_t = 4 | t | O-2-labels (≠ t), i* (2-part 2), d (2-part ≥ 8) | 6 |
| D3, z = 5, p ∉ O (incl. p = d) | d | O-2-labels, the O-4-label, i* | 15/2 |
| D3, z = 5, p ∈ O (incl. p = t) | p, d | all remaining | 13/2 or 11/2 |

Every value exceeds 5, so D4 and D3 hold at unmarked centres for every placement of the markers among the neighbours. ✓

**L1–L4.**
- **L1** needs the 5/6 bound for both rows at v. Both are available: the α-row via C2 and the α*-row via CAP C1.
- **L3** keeps the orientation explicit: x-degree 3 implies x′-degree exactly 1 and x′_{vi*} even.
- **L4** is only the contrapositive of L1.
- The "What does not follow" paragraph is correct: the G-only no-K4 argument needs L1 at the fifth vertex, which here may be t or p. ✓

## Findings (all MINOR, none mathematical)

**m1. C:13–17 and the status tag at C:1.**
- The premise list still names general "Lemma RC, item CD3".
- The corrected C actually uses only:
  - CAP C1 (for x = α);
  - RC-i* (at f* = 1);
  - the fresh light-fibre count at M13-ov:30–50;
  - the inline light-set derivation at C:74–76.
- *Fix:* a one-line overlay narrowing C:16–17 to these interfaces, stating that no general RC or VFC-form rule is imported.

**m2. C:66–68 and C:92–93.**
- Φ^y, X^v_j and "tight" are defined only by reference to DT-A and CAP-ov1.
- The parenthetical "y_ab = 1 forces this" leaves out its one-line reason: 4 divides τ and τ ≤ x₁x₂ = 4, so τ = 4 = 4·y_ab.
- *Fix:* define Φ^α = (U_j) in Γ and Φ^{α*} = (U*_j) in Γ*, with "tight" meaning y + y′ = g, i.e. X^v_j ⊔ D′_j = G. Then add the τ = 4 sentence.

**m3. D:11–13.**
- The 5/6 premise is pinned to the frozen C hash 13f2c8dc…. In that file, C58–63 is the superseded general-RC text.
- *Fix:* cite "M13-C §2 as replaced by the K62-M13-erratum-v1 (a4c476c1…) New block". The conclusions are unchanged.

**Notes, not counted as findings.**
- **Stale CONDITIONAL or "candidate" tags.** They appear at B:1, 10–12, 61, 73, 80; C:1, 15–17, 52, 65, 99; D:1, 12, 99–100. A:117–118 also still calls DT-C "a candidate under review". Under V-CAP these tags are discharged only for the CAP C1 and RC-i* imports, not for the new M13 claims.
- **D:29–32** lists only odd z. Even z shares no odd prime, and nothing depends on it.
- **SCOPE:3** timing wording is superseded by checkpoint-017:39–42.

## New conclusions, recommended for parent acceptance

These hold in (1,3), and in (3,1) with α and α* swapped.

1. **A1 and the α-family DG suite.**
   - A1 as stated.
   - DG-1* and DG-2*.
   - DG* under the condition that every 4-subset Q has r_Q ≤ 4 in the α-family; this is automatic when e_d = 4.
2. **C1\* and C2\*.**
   - C1*: v2 T_α(Q) ≥ 3 for every 4-subset Q, and v2 T_α(O) ≥ 4.
   - C2*: n_4(α) ≥ 2n_1(α) + 2.
3. **Joint budget.** 2N41 + 2N14 + 5N11 + 3N12 + 3N21 + N22 ≤ 6. Consequences:
   - N11 ≤ 1;
   - if N11 = 1, then N41 = N14 = N12 = N21 = 0 and N22 ≤ 1;
   - N12 + N21 ≤ 2.
4. **i\*-row gaps.** |K_α| ≤ 3 and |K_{α*}| ≤ 3. At least two c ∈ O have α_{i*c} ≥ 3, and therefore α*_{i*c} ≤ 3.
5. **New granularity.** gcd(n_v, T_{α*}(V∖{v})) = 6 at every unmarked v ∈ O.
6. **Row bounds.** Both rows satisfy the nonstrict 5/6 bound at every unmarked v ∈ O, and both i*-rows satisfy 11/12.
7. **Cherry isolation.**
   - CI13 and CI13′ hold in both families at every unmarked apex; a and b may be marked.
   - The two C §4 forcing statements hold, each with its unmarked-apex hypothesis.
8. **Local row structure.** D4, D3 and L1–L4 hold at unmarked centres, for every placement of marked neighbours.

## Left open

- **Rows centred at t (always marked here) and at p ∈ O with p ≠ t.**
  - There is no 5/6 bound in either family at these centres, because C1 and C1w need n_v = 6w_v.
  - So D3, D4, L1–L3, CI13 and CI13′ are unavailable there.
  - Nothing prevents t (or p) from having H_x-degree 0 or 4, being a bowtie centre, or being the escaping fifth vertex of a K4.
- **Global graph conclusions.** No no-K4, bowtie, diamond, free-family or joint-pattern division is established. The G-only DT-C counts are not transferred (3 ≤ |H| ≤ 7, N11 = 0, s ∈ {1,2,3}, and the N42 + N24 bounds).
- **Uncovered triples.**
  - (4,4,4) triples with τ = 8 are not covered.
  - A deep triple escapes CI13′ at any marked apex.
- **Higher-depth DG alternative.** For e_d ≥ 5, a 4-subset of capped depth ≥ 5 remains possible, in each family.
- **Regime level.** Exclusion of (1,3)/(3,1), full K6.2* (e_d ≥ 4, e* = 2), K7 and Sun(7) all remain open.

## Provenance and status

- **Direct Sun instances.**
  - Sun(4) in A1(b).
  - Sun(2) and Sun(3) in the B and D certificates, through LFC(c).
  - Sun(2) and Sun(3) in CI13 steps 2, 4 and 5, through VFC (V3).
- **Transitive imports.** Sun(5) and Sun(6) remain computer-assisted, model-reviewed transitive imports through the allowed-set notion and the class reduction. No Sun(7) is used.
- **Status of this review.** It is a model review only; the new M13 claims stay candidates until a parent verdict.
- **Process.** Exploratory derivation preceded the scope freeze, so there is no preregistration claim. There is no novelty, Lean or human-referee claim.
