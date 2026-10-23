# Referee report: CAP-62, DT-A, DT-B, DT-C (with the mandatory DT-C erratum)

**Texts reviewed.** K62-CAP-v1 `19dccc3d…`, K62-DT-A-v1 `cd7266d4…`, K62-DT-B-v1 `51960d44…`, and K62-DT-C-v1 `7e8bde21…`, the last read through K62-DT-C-erratum-v1 `0f785140…`. I took the hashes from the manifest and did not recompute them, because I used no tools.

**Method.** I reviewed the files in dependency order: CAP, then DT-A, then DT-B, then DT-C.

**Premises admitted.** Only these, and only at the attached accepted scopes:
- README-old: R0, L0.1 with Lagrange, P0/P1, and the class definition.
- LFC-INV with E1 and E6.
- RULES-K7: L1/(T3) and VFC (V1)–(V4) with the count.
- K62-E3 with errata v1–v2.
- K62-SH/DG with both errata.

Every co-packaged candidate premise was re-derived here before I allowed it downstream. These are CAP (C) and its Consequences, CI, CI′, (3c), R3, R4, and B1–B5.

---

## 1. Verdict

**Overall: ACCEPT-WITH-FIXES at the stated scopes. FATAL 0 / MAJOR 0 / MINOR 12.**

- Every statement is correct as used.
- Three proof sentences are false in edge cases (m1, m2, m8). Each has a one-line repair, and no statement changes.
- One load-bearing paragraph, CAP "Consequences", must be written out (m3).
- No file excludes any regime of the residue.

| File / claim | Verdict | Severity |
|---|---|---|
| CAP (A1)–(A4): finite ranges, 1 ≤ δ ≤ 9 | ACCEPT | – |
| CAP (B1): g, γ, gcd(α, ℓ) | ACCEPT | – |
| CAP (B3): τ_min, τ_max, apex and pair measures | ACCEPT | m5 (editorial) |
| CAP (B4): d-grid exponent min(ê_d, v₂T) | ACCEPT | – |
| CAP (B5): normalized counts t_j/n_v | ACCEPT (normalized only) | – |
| CAP (B2): gcds of label pairs | ACCEPT-WITH-FIXES | m1 MINOR |
| CAP (C1): gcd(n_v, T_x(V∖v)) ∣ 6 | ACCEPT | – |
| CAP (C2): gcd(n_i*, T_x(V∖i*)) ∣ 12 when f* = 1 | ACCEPT-WITH-FIXES | m2 MINOR |
| CAP Consequences: 5/6 row bound, 11/12 at i* | ACCEPT-WITH-FIXES | m3 MINOR |
| CAP (D): transfer | ACCEPT-WITH-FIXES | m4 MINOR |
| DT-A §0 conventions and §1 apex table (all 10 value multisets) | ACCEPT | m7 (labels) |
| DT-A Lemma CI | ACCEPT | – |
| DT-A Corollary CI′ | ACCEPT | – |
| DT-A (3a), (3b) | ACCEPT | – |
| DT-A (3c): 2a + 3b ≥ 3 + 4c + 12e | ACCEPT-WITH-FIXES | m6 MINOR |
| DT-B §0: setting G | ACCEPT-WITH-FIXES | m8 MINOR |
| DT-B (R4), (R3) | ACCEPT | m10 (editorial) |
| DT-B B1, B2, B4 | ACCEPT | – |
| DT-B B3 | ACCEPT | m9 |
| DT-B B5 | ACCEPT-WITH-FIXES | m9 MINOR |
| DT-B §4: gap description | ACCEPT as a non-claim | m11 MINOR |
| DT-C C1: budget 2A + 2C + 5E + 3F + 3G + H ≤ 6 | ACCEPT | m12 |
| DT-C C2: minimum 4-degree ≥ 1; 3 ≤ A + B, C + D ≤ 7 | ACCEPT | – |
| DT-C C3 with erratum: A + C ∈ {1,2,3}, B + D ≥ 5 (not 6) | ACCEPT | – |
| DT-C C4: status | ACCEPT as a non-claim | – |

## 2. Minimal repairs (one consolidated erratum suffices)

**m1. CAP (B2), proof.** The text says "every other label in a gcd with it has 3-part ≤ 3". This is false at v = d when x_(d i*) = 3.
- In that case t exists, so f* = 1, and λ_i* = n_i*·3/4 has 3-part 9.
- The conclusion still holds. The partner label is λ_t = n_t/2, with 3-part 3^(f_t) ≥ 9, so the gcd has 3-part 9 = 3^min(f_t, 2).
- Repair: "other labels have 3-part ≤ 9, with 9 only for λ_i* at d when x_(d i*) = 3; the cap min(f, 2) is exactly sufficient."

**m2. CAP (C2), proof.** The text claims gcd 6 at the first vertex added after d. This fails when t is absent; with f* = 1, that means m3 is absent.
- The vertex c₁ added right after d is p if p exists, otherwise an unmarked vertex.
- Then gcd(n_c₁, n_d) = 2, not 6. The reason is that n_d has no factor 3, and h_d = 0 when c₁ = p.
- The repair is exact: T₂ = lcm(n_d, n_c₁)·x_(d c₁), and x_(dc) = 1 for every c ∈ O by (A2). Hence k = 1.
- From the second O-vertex on, 6 ∣ T_m, so gcd = 6 and k ≤ 3 as stated. The statement of (C2) is unchanged.

**m3. CAP Consequences.** State the following as a lemma and prove it.

*Lemma.* Let v ∈ O be unmarked, or let v = i* with f* = 1. Let x′ be the family other than x, and in the O case assume x′_(d i*) = 1. Then for every y ≥ 0 that is feasible for the λ^x-allowed sets at v:

  Σ_(j≠v) y_j·x_vj/g_vj ≤ 1 − 1/gcd(n_v, T_x′(V∖v)) ≤ 5/6 (resp. 11/12).

*Proof outline.*
- Normalize g_v = 1 in the Φ^x-configuration. Its conjugated family is Φ^x′.
- Run the K62-E3 step 3 argument with v in place of d; this transposition is already accepted at c₄ in SH-DG-erratum G8. It shows that W^x′Φ_v misses every L_j = g_jΦ_jΦ_v.
- W^x′Φ_v is a union of at least n_v/gcd fibres, all of them empty.
- Sum LFC (d) over the remaining fibres.

The bound is non-strict and carries no slack depending on n_v. The orientation reads: **the x-row bound uses (C1) for x′**.

**m4. CAP (D).** Add the following discipline for what counts as a rule:
- (i) its side conditions (sub-case, orientation, DG hypotheses) are decidable from π;
- (ii) every inequality is either slack-free or used only in its strict form; "Σ ≤ c − ε(Γ)" with ε(Γ) > 0 depending on n_v, n_d or the w's yields only "Σ < c";
- (iii) rounding is allowed only onto a lattice that π determines;
- (iv) it uses only (B) quantities and the (C) bounds.

Add also: U62 is finite, but no element-wise check exists. (D) proves nothing about the residue until such a check is done and itself reviewed.

**m5. CAP, editorial.**
- In (B3), the letter x names both a vertex and a family.
- In (π1), min(f_m3, 2) ≡ 2 is constant, and min(h_m5, 2) could be min(h_m5, 1), since only h_m5 ≥ 1 enters any gcd.
- These are harmless for correctness, but an enumeration of U62 as written would duplicate patterns.

**m6. DT-A (3c).** State the following:
- "Depth" means the capped depth r_R = min(e_d, v₂T_x(R)), which is ≤ 5.
- DG (a) gives the π-level bound Σ_R 2^(−r_R) < 19/16. The term 2/n_d is not a π-quantity.
- Since Σ ∈ (1/32)ℤ, the bound gives Σ ≤ 37/32, which is equivalent to 2a + 3b ≥ 3 + 4c + 12e.
- The hypothesis of DG (a) concerns capped depths of 4-subsets.

**m7. DT-A labels.**
- The "CONDITIONAL ON DG" labels are discharged by verdict cae455c3.
- Cite the τ bound as DG-3 in its G3 form.
- Cite (T3) either as L1 (T3) from RULES-K7 or as the G3 apex identity.

**m8. DT-B §0.** The text says λ_d "shares no odd prime with the i*-label". This is false when m5 = d and x_(v i*) = 5; then gcd(λ_d, λ_i*) = 10.
- It is not load-bearing. No certificate gives positive weight to both d and i*, and allowed sets are hereditary, so only the support matters.
- Repair: qualify the sentence.

**m9. DT-B B3, B5 and §4.** The K4/diamond vertex named "d" clashes with the distinguished vertex d.
- Read literally, B5's "x′_(d i*) even" is false for the distinguished d in G, where x′_(d i*) = 1.
- Repair: rename the diamond {a, b, c, c′}.

**m10. DT-B (R3), (R4), editorial.** The letter x denotes both the i*-entry and a family. Rewrite the feasibility sentence in (R4) as follows:
- Two labels of 2-adic valuation 1 have gcd 2.
- Each has gcd ≤ 2 with every other label.
- So no 3-set containing both is allowed, by Sun(3).
- By heredity, positive-weight allowed sets are singletons or pairs.

**m11. DT-B §4.** Phrases like "satisfies DG through deep triples … whose forced apexes use non-tight pairs" are informal.
- Restate the residual as: every G-pattern in U62 satisfying (R3), (R4), B1–B5, C1–C3 and the accepted E3/SH/DG/L1 rules, in both families.
- Say explicitly that this is not a characterization.

**m12. DT-C.** The count names C, D, E and G clash with the vertex set C, the vertex d, the set E and the sub-case G.
- Rename them, e.g. N₄₁, N₄₂, N₁₄, N₂₄, N₁₁, N₁₂, N₂₁, N₂₂.
- Observation only, not a request to broaden: C1's algebra uses only (α_(d i*), α*_(d i*)) = (1,1).

## 3. Parent questions

**Q1. CAP (C2) when t is absent.** Confirmed, see m2.
- Under f* = 1 the only t-absent case is "m3 absent". There, both "Adding p: gcd = 6" and, when p is also absent, "Unmarked: gcd 6" are false for c₁: the gcd is 2.
- The stronger bound k = 1 is an exact identity, not just an inequality, because x_(d c₁) = 1.
- (C1) has no such defect, because i* is added before any O-vertex, so v₃T₂ = f* ≥ 1.

**Q2. Normalized versus absolute counts.** (B5) determines only t_j/n_v = x_vj/g_vj.

These are **not** functions of π:
- n_v and n_d (through 5^(h_d)·w_d, and e_d once e_d > 10);
- the absolute counts t_j, the light-fibre number M, and N(Q) as integers;
- the slacks 1/n_v, 2/n_d and 3/(2n_d).

These pattern-level forms **are** justified:
- LFC (d) gives Σ y·x/g < 1.
- With (C1)/(C2) light sets: ≤ 5/6 at an unmarked v ∈ O when the granularity family has d–i* entry 1, and ≤ 11/12 at i* when f* = 1. Both are non-strict and exact.
- DG (a) gives Σ_R 2^(−r_R) < 19/16. Since every r_R ≤ 5, this rounds to ≤ 37/32, which is what (3c) uses. This step is justified, but the 19/16 − 2/n_d form cannot be evaluated.
- DG-1: N(Q)/n_d ∈ 2^(−r_Q)·ℤ_{>0}, with r_Q = min(ê_d, v₂T).
- DG-2 forms with "−1" become strict normalized inequalities.
- K62-E3 C2, n₄ ≥ 2n₁ + 2, is already an integer statement at the level of π.

**Q3. Atom and subset grids at O or i\*.** None is granted or used.
- CI uses only the global (C1) bound and the exact VFC measures x′/g of individual D′-sets.
- DT-B and DT-C use only global row bounds and the accepted d-grid of E3 C2.
- A grid for S ∌ d at an O-vertex or at i* would need its own chain lemma. CAP §3 says so correctly.

**Q4. Capped versus raw depth when e_d = 4.**
- When e_d = 4, a τ = 16 triple has capped depth 4. It belongs to a, and b = 0.
- The raw-depth version of (3c) is also valid, but weaker, because 2^(−min(e_d, r)) ≥ 2^(−r).
- B4's case split is sound under either reading.
- DG (b)'s alternative "single deep triple of depth 5" needs e_d ≥ 5.

## 4. Sun provenance

**Direct local applications in the reviewed proofs.**
- Sun(2): CI step 4, and the isolation of 1-entries in (R3)/(R4), via LFC (c) or (V3) with |T| = 2.
- Sun(3): CI steps 2 and 5, and the (R3)/(R4) certificates, with |T| = 3.
- Through accepted imports only: Sun(4), in E3 Lemma 1 and step 2.
- CAP (A)–(C) are pure index arithmetic (L0.1 and Lagrange) and use no Sun instance.

**Sun(5) and Sun(6) are never directly invoked.** They stay in the import closure in two ways:
- through the accepted LFC/VFC package, whose (c)/(V3) is proved via Sun(|T|) for |T| ≤ 6, so the general row-count lemmas quantify over all allowed sets;
- through the README reduction R1(7), which defines K6.2*: a ≥ 3 is excluded by Sun(6), and |C| ≥ 4 comes from Sun(5).

These are the named, accepted, computer-assisted Sun(5)/(6). No closure here is free of Sun(5)/(6).

## 5. Scope, prerequisite closure, OPEN items

**Scope.**
- CAP-62 covers the whole residue: K6.2*, e_d ≥ 4, e* = 2, every marker placement, both d–i* orientations. It is a representation result only.
- DT-A §1–2 covers the whole residue. CI needs v unmarked and x_(d i*) = 1.
- DT-A §3 covers the orientation (1,1).
- DT-B and DT-C cover only the generic sub-case G: no marker in O, so the orientation is (1,1).

**Closure.** After the fixes, every premise is either an accepted import at the attached scope or a claim accepted in this review. No premise depends on:
- K62-ARCH, STATUS-v2, or "rules R1" (all navigation only);
- K63-RES or K62-FG;
- probe-survivor-map (unrun);
- any computation.

**Still OPEN:**
1. Every marked sub-case (a marker in O), including the d–i* orientations (1,3) and (3,1). There, DG and the (C1) granularity hold for one family only, and R3/R4 do not transfer, because marked O-labels carry a 3 or 5 that can be shared with λ_i* or λ_d.
2. The remaining G-patterns satisfying (R3), (R4), B1–B5 and C1–C3.
3. Full K6.2* with e_d ≥ 4, e* = 2.
4. K7, and full Sun(7).

U62 is finite, but nothing has been enumerated. The rule architecture is **not** a proof of the residue.

---

## 6. Verification record

### 6.1 CAP-62

**(A2): entry ranges.**
- d–O: g = 2 forces α = α* = 1.
- d–i*: E3 Lemma 1 gives each entry in {1, 3}, with 3 only when t ∈ O. The bound α + α* ≤ 4 removes (3,3).
- O–O: E3 Lemma 2 excludes 3, and excludes 5 when h_d ≥ 1. Z11(a) excludes 5 when h_d = 0, in both families. With α + α* ≤ 6, this leaves J_O with eight values.
- i*–O: E1 and INV(b).

**(A3).** L1 holds for every disjoint configuration; for α* apply it to the inverted configuration. The range is finite given (B1).

**(A4).** Run the chain with marked vertices first.
- The start has v₂ = 1, or v₂ ≤ 3 when the start is a marked pair t ≠ p.
- Each unmarked step has gcd(n_e, T_m) = 6 and k ≤ min_j x_ej ≤ 4, so v₂ grows by at most 2.
- Hence δ ≤ 1 + 2(|Q| − 1) ≤ 9, in both families.

**(B1)/(B2): which caps matter.**
- *2-parts.*
  - At an O-vertex: λ_d has 2-part 2^(e_d−1) ≥ 8, λ_u has 2^(v₂x), and λ_i* has 2^(1+v₂x) ≤ 8. A minimum never reads e_d.
  - At i*: λ_d has 2-part ≥ 4 and λ_c has 2-part ≤ 4.
  - At d: n_d does not appear.
  - For ℓ_d: v₂ℓ_d ≥ 2 ≥ v₂α.
- *3-parts.* The ℓ terms need only min(f* − 1, 1) and min(f_c − 1, 1). For labels see m1; cap 2 is exact.
- *5-parts.* Cap 1 is enough.
- *w-parts.* They never enter, since α ≤ 5.

**(B4).** The E3 Lemma 3 chain (Z10, every non-empty Q) uses neither the d–i* entry nor the orientation, so by inversion it also gives the result for T_α. Since v₂T ≤ 9 < 10, min(e_d, v₂T) = min(ê_d, v₂T).

**(C1) case check.** Order the vertices d, i*, t, p, then the rest. Since x_(d i*) = 1, T₂ = lcm(n_d, n_i*).

| Marker case | First O-step | Result |
|---|---|---|
| t only | v₃T₂ = f* = 1; h_t = 0 | gcd 6, k ≤ 6·(1/2) = 3 |
| t = p | h_d = h* = 0 | gcd 6, k ≤ 3 |
| t ≠ p | after t, T is 5-free | p step: gcd 6, k ≤ 3 |
| p only | f_p = 1; T₂ is 5-free | gcd 6, k ≤ 3 |
| neither | first unmarked vertex | gcd 6, k ≤ 3 |

- These cases hold for m3 ∈ {i*, none} and m5 ∈ {d, i*, none}.
- All later unmarked steps have gcd 6 and k ≤ 3.
- If instead x_(d i*) = 3, then v₃T₂ = 2 and only k ≤ 9 follows, which admits the prime 7. So the hypothesis is genuinely used.

**(C2) case check.** Order the vertices d, t, p, then the rest.
- t present (t = p or not): the t step is exact with k = x_dt = 1. The p step, for p ≠ t, has gcd 6 and k ≤ 3.
- t absent: see m2.
- Final gcd: the 2-part is 4, since v₂T ≥ e_d. The 3-part is 3, since f* = 1. The 5-part is 1, since h* ≥ 1 forces every other vertex to be 5-free and all k ≤ 3. The w-part is 1.

**(D).** The logic is sound: π(Γ) ∈ U62, every rule holds at π(Γ), and R0 preserves all the indices involved. Conjugated intersections are preserved because N is normal.

### 6.2 DT-A

**§0 conventions.** For x = α, VFC of the original configuration at v gives X_j = U_vU_j of measure α/g, D_j of measure α*/g, and d_j = α*·n_j/g. For x = α*, use the inverted configuration; left translation does not change its subgroups U*_j. INV(b) identifies q with x′.

**§1 apex table.**
- Criterion: at apex y, μ(Φ_y(Φ_x ∩ Φ_z)) = τ/(6x_xz) ≤ x_yx/6, with equality iff τ = x_xz·x_yx. Equality gives X^y_x = Φ_y(Φ_x ∩ Φ_z) ⊆ X^y_z.
- I checked all ten multisets.
- Each listed forcing is right, including the containments X(1) ⊆ X(2) and X(2) ⊆ X(4).
- The rows reported as "nothing" are right, for (2,2,2) with τ = 2, (2,4,4) with τ = 4, and (4,4,4) with τ ≠ 16.
- (1,1,2), (1,1,4) and (1,2,4) have lcm > x₁x₂, so they are forbidden.

**Lemma CI.**
- *Orientation is correct.* The set Φ_vW lies in every X^v_j, so (V1) makes it disjoint from every D′_j. Its measure is ≥ 1/gcd(n_v, T_x(V∖v)) = 1/6 by (C1) applied to x. So the granularity of Φ^x bounds the x′-row, and that is exactly where x_(d i*) = 1 is needed.
- *Labels.*
  - λ′_a = λ′_b = 2·3^(f−1)·5^h·w, since x′ = 2.
  - λ′_c = 2^(v₂x′_vc)·(odd).
  - λ′_d = 2^(e_d−1)·5^(h_d)·w_d, since x′_vd = 1 and g = 2.
  - λ′_i* is not used.
  - Odd parts are pairwise coprime: there is one 3-marker and one 5-marker, and x′ ∈ {1, 2, 4}.
- *Steps 1–5 hold.*
  - Measures: 2/6 + 3/6 = 5/6, which equals the cap.
  - Sun(2) forces x′_vc to be even, and x′_vc ≤ 3, so x′_vc = 2.
  - Final contradiction: 4/6 > 3/6.

**CI′.** The value τ equals 4x_ab exactly in the cases (1,4,4) with τ = 4, (2,4,4) with τ = 8, and (4,4,4) with τ = 16. Then X^v_a = X^v_b. Since x = 4 forces x′ ∈ {1, 2}, "tight" is equivalent to x′ = 2.

**(3a).** A triple is deep iff τ ∈ {8, 16}. For T3 triples: any edge set meeting all three vertices of a triangle has at least 2 edges. **(3b)** holds.

**(3c).** 32Σ = 40 − 2a − 3b + 4c + 12e, and 32Σ ≤ 37 gives the stated inequality.

### 6.3 DT-B, in G

**Labels in G.**
- O-label: w_u·x_vu.
- λ_i* = 2·3^(f*−1)·5^(h*)·w_*·x_(v i*).
- λ_d = 2^(e_d−1)·5^(h_d)·w_d.
- Among O-labels and λ_i*, the only shared prime is 2. Between λ_d and any O-label, the only shared prime is 2.

**(R4).** All of (2,2,2,2), (2,2,2,1) and (2,2,1,1) give value 11/2 > 5. Rows with three or more 1-entries are excluded by E3 Lemma 2.

**(R3).**
- Every row gives 5 + x_(v i*)/2 ≥ 11/2. The certificate also works for (1,1,1,4).
- *Parity at i\* is sharp.* If x_(v i*) is even, then {two, four, i*} is allowed, since gcd ≥ 4, and the certificate fails.

**B1–B3** hold. For B3, B2 at each K4 vertex gives the fifth vertex H_x′-degree 4.

**B4.**
- In a free family, CI′ forces τ ≠ 4x_ab. So no triple has depth 5, and the only deep triples are 4-triangles with τ = 8.
- If no 4-subset has capped depth > 4: 2a ≥ 3 gives two triangles. They share a vertex; a bowtie is excluded, so they share an edge, which gives a diamond.
- Otherwise DG-4 applies at every e ∈ Q (all unmarked). Count H_x-triangles in Q: zero or one forces a K4, which B3 excludes, so there are at least two, which gives a diamond. This split is exhaustive.

**B5.** The complement of a diamond is {ab, ea, eb, ec, ec′}, which contains exactly one triangle. B2 at c and c′ gives x′_ce = x′_c′e = 4 and even x′_(· i*).

**Joint α/α\* at i\*.**
- B2 gives x′_(v i*) ∈ {2, 4}, hence x_(v i*) ≤ 4.
- (R3) on the x-row forces x_(v i*) even at every vertex of H_x-degree 1. This is C4's outlook remark, and it is correct.
- The marker boundaries inside G were checked for m3 ∈ {i*, none} and m5 ∈ {d, i*, none}. The only defect is m8, which is not load-bearing.

### 6.4 DT-C

**C1.** The algebra is correct:
- A + B ≥ 2(C + E + F) + 2 and C + D ≥ 2(A + E + G) + 2.
- Adding them and substituting B + D = 10 − (A + C + E + F + G + H) gives 2A + 2C + 5E + 3F + 3G + H ≤ 6.

**C2.** With minimum degree 1 and maximum degree 3 on 5 vertices, each family has between 3 and 7 edges.

**C3.** A + C ≥ 4 would give 8 > 6, so A + C ∈ {1, 2, 3}.

| A + C | Constraints | Tight 4-pairs |
|---|---|---|
| 1 | E = 0, F + G ≤ 1, H ≤ 4 − 3(F + G) | B + D = 9 − (F + G) − H ≥ 5, with equality only at F = G = 0, H = 4 |
| 2 | E = F = G = 0, H ≤ 2 | B + D = 8 − H ≥ 6 |
| 3 | E = F = G = H = 0 | B + D = 7 |

The erratum is therefore correct. The original "at least 6" was not supported by C1. Pairs carrying an entry 1 number A + C + E + F + G ≤ 3, and E = 0 throughout.
