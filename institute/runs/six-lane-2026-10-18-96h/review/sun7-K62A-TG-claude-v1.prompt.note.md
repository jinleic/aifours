# Hostile referee report: K62-A, Lemma TG, corrected K63-CLIQUE

**Boundary.** This is a written check only. I used the imports exactly as supplied: R0, L0.1–L0.3, LFC, INV, VFC (V1)–(V4), L1, and Sun(t) for t ≤ 6 inside subgroups. I re-derived L1's T2/T3 below. Three referenced texts are not in the packet: README §5, K7-M1 with its erratum, and K7-Z2-v1.md. Class facts are taken from rules-k7-v1 §4 / P1(iv), and every fact the candidates borrow from Z2 or M1 is re-derived here from VFC, INV and LFC. No computation, LP solver or census is used, and probe artefacts were not evaluated.

---

## (A) Theorem K62-A (v1 + erratum-v1)

**Verdict: CORRECT. ACCEPT-WITH-MINOR-FIXES. FATAL 0, MAJOR 0, MINOR 4.**

**Class facts.**
- e_c = 1, f_c = 1 (Hypothesis A), f* ≥ 1, f_d = 0, and at most one vertex has h ≥ 1.
- Hence g_dc = 2, so α = α* = 1 on those edges.
- g_di* = 4, so α_di* ∈ {1,2,3}.
- g = 6 inside C, for any f* and any 5-marker position.

**Step 1 (LFC at d).** The labels are λ_c = 3·5^{h_c}w_c (weight 1/2) and λ_i* = 2^{e*−2}3^{f*}5^{h*}w*·α_di* (weight α/4).
- c–c′: gcd = 3·5^{min h} = 3.
- c–i*: λ_c is odd; the 3-part is min(1, f* + v₃α) = 1; the 5-part is min(h_c, h*) = 0 (α ≤ 3); the w-parts are coprime to each other and to α.
- So all 15 gcds equal 3 for every e*, f* and 5-marker placement.

Sun(4) then caps allowed sets at size 3. The weights y ≡ 1/3 are feasible and give 5/6 + α/12, so α = 1.
- α = 2 gives exactly 1 and dies only by strictness (≤ 1 − 1/n_d).
- f_c = 1 is load-bearing exactly at α = 3 with f* = 1; otherwise the c–i* gcd is 9 and 4-sets become allowed.
- Hypothesis A is index-defined, so the same argument gives α*_di* = 1 (A2). ✓

**Step 2 (LFC at i*), in units of 1/6.** λ_d = 5^{h_d}w_d (uses e_d = 2 and α_i*d = 1; worth 3/2 units). λ_c = 5^{h_c}w_c·α_c (worth α_c units).
- gcd(λ_c, λ_c′) = gcd(α_c, α_c′), with one exception: c5 with α ≠ 5 against an α = 5 label gives 5, not 1.
- gcd(λ_d, λ_c) = 5 if h_d ≥ 1 and α_c = 5; otherwise 1.

*(a) Some entry is 5 (k5 ≥ 1).* Put y = 1/k5 on F5 (5 units; feasible because |T ∩ F5| ≤ k5).

| Sub-case | Certificate | Value |
|---|---|---|
| Some c ∉ F5 with c ≠ c5 | y_c = 1, y_d = 0; λ_c is coprime to all F5 labels (Sun(2)) | ≥ 6 |
| F5 = C′ (c5 inside F5, or 5-marker on d, on i*, or absent) | Inverted: α* ≡ 1 on C′; labels 5^{h_c}w_c and 5^{h_d}w_d pairwise coprime; y ≡ 1 | 13/2 |
| F5 = C′∖{c5} with c5 outside F5 (forces h_d = 0) | Inverted: labels w_c (×4), 5^h w_{c5}α*, w_d pairwise coprime; y ≡ 1 | ≥ 13/2 |

The cases are exhaustive. The inversion is used correctly: run for α*, the inverted certificates are LFC(d) of the original configuration (A2).

*(b) No entry 5 (k5 = 0).* Then d is singleton-only (Sun(2)), so the C-part must reach 9/2. All five-neighbour R1/R24/R3 rows:

| Row (k1 ones, a twos, b fours, k3 threes) | Weights | C-value |
|---|---|---|
| k3 ∈ {1,2,3} | 1/k3 on R3; standard weights on the rest | ≥ 3 + min(5−k3, 4) ≥ 5 |
| k3 ∈ {4,5} | 1/3 on R3 (Sun(4)); 1 on the leftover | ≥ 5 |
| k3 = 0, b ≤ 2 | 1 on ones, 1/2 on twos, 1/4 on fours (Sun(3)) | 5 |
| b = 3, (k1,a) = (2,0) or (1,1) | 1 on ones, 1/3 on fours | 6 or 5 |
| **b = 3, (k1,a) = (0,2): {2,2,4,4,4}** | — | **4, the LP optimum** |
| b = 4, (k1,a) = (1,0) | 1 on the one, 1/3 on three fours | 5 |
| b = 4, (k1,a) = (0,1): {2,4,4,4,4} | 1/4 on all (Sun(5)) | 9/2; total 6 > 6 − 6/n_i*, killed by strictness |
| b = 5 | 1/4 on all (Sun(5)) | 5 |

**{2,2,4,4,4} is the only survivor, and it is a genuine one.** The constraints on {2_j, 4, 4, 4} for j = 1, 2 sum to (y₂₁ + y₂₂) + 2Y₄ ≤ 2. The value equals 2[(y₂₁ + y₂₂) + 2Y₄] ≤ 4, so with d the total is 11/2 < 6. Step 3 is therefore necessary.

**Step 3.** The α-row and α*-row of i* are both {2,2,4,4,4}. A = {α = 4} and A* = {α* = 4} are disjoint, since 4 + 4 > 6 = g (INV(b)). But |A| + |A*| = 6 > 5. ✓

**ROW-U.** After A1, no six-neighbour ROW-U is invoked. v1's citation of ROW-U-deg (M1-erratum F3) was outside the supplied imports and is correctly superseded. The table above is self-contained.

**MINOR findings and repairs**
- **A-m1 (A1 justification).** State the real transfer principle: allowed-ness depends only on the pairwise label-gcd matrix. So ROW-U's class weights apply to any neighbour set with common g = 6 and gcd(λ,λ′) = gcd(α,α′).
- **A-m2 (§3(a) wording).**
  - Replace "standard weights on such c's add ≥1" with "y_c = 1 on one such c, y_d = 0". y_d = 0 is needed because d shares the prime 5 with F5 when h_d ≥ 1.
  - In the third case, state explicitly: c5 ∉ F5, k5 = 4, h_d = 0, α*_{i*c5} ≥ 1.
- **A-m3 (§3(b)).**
  - "Every C-label gcd equals the gcd of the alphas" holds only because k5 = 0; say so.
  - Add the LP-optimality line for {2,2,4,4,4} and the strictness remark for {2,4,4,4,4}.
- **A-m4 (Sun accounting).**
  - Replace "Sun(t), t ≤ 6" with the exact list: Sun(2), Sun(3), Sun(4) and Sun(5). Sun(6) is unused, and Sun(5) is used only for the rows {2,4,4,4,4} and {4,4,4,4,4}.
  - *Optional:* drop Sun(5) entirely. Those two rows would then survive Step 2, but each still has at least three 4s. Step 3 needs only |A|, |A*| ≥ 3, so K62-A would rest on Sun(2)–Sun(4) alone.

---

## (B) Lemma TG

**Verdict: CORRECT. ACCEPT. FATAL 0, MAJOR 0, MINOR 2 (+1 optional).**

**Re-derivation.**
- W ≤ U_a, U_b, U_c, so U_vW ⊆ X_a ∩ X_b ∩ X_c.
- By the product formula, μ(U_vW) = |U_v||W| / (|U_v ∩ W||G|) = Q/(n_v T), where Q = [G : U_v ∩ W].
- Q = n_v[U_v : U_v ∩ W] = T[W : U_v ∩ W], so lcm(n_v, T) divides Q.
- Hence μ ≥ lcm/(n_v T) = 1/gcd(n_v, T).
- No disjointness, INV or Sun is used.

**Arbitrary groups.** Let N be the intersection of the cores. It is normal, of finite index, and contained in U_v ∩ W. U_vW and the X_j are unions of N-cosets, and n_v, T and Q are unchanged in G/N. So TG holds for the induced density. In CLIQUE, R0 has already made G finite.

**Findings**
- **B-m1.** Put "G finite, or pass to G/N" into the lemma statement; at present it appears only in the premises header.
- **B-m2.** The Ppair parenthetical is navigation only; Ppair is not imported.
- **Optional sharper form.** X_a ∩ X_b ∩ X_c is left U_v-invariant and right W-invariant, so it is a union of (U_v, W)-double cosets. Each has measure a positive multiple of 1/gcd(n_v, T), because conjugates of W have index T. So μ(X_a ∩ X_b ∩ X_c) is itself such a multiple, which is the exact triple analogue of L4's u.

---

## (C) Corrected Theorem K63-CLIQUE (v1 + E1–E4)

Statement audited: *no K6.3 configuration has α_ab = α*_ab = 3 for all distinct a, b ∈ C.*

**Verdict: CORRECT AS CORRECTED. ACCEPT-WITH-MINOR-FIXES. FATAL 0, MAJOR 0, MINOR 7 (+1 optional).** The v1 star statement had a MAJOR gap: it used inner-edge values it did not assume. The v1 Remark on the 3-marker was false. Both are withdrawn, and E1/E3 resolve them with no residue.

**Setting.**
- n_c = 6r_c and n_d = 3r_d, with all r pairwise coprime. This follows from: at most one C-vertex with e ≥ 2, at most one vertex with f ≥ 2, at most one with h ≥ 1.
- g = 6 inside C and g_cd = 3.
- Choose v ∈ C with e_v = f_v = 1; at least four candidates exist. Then r_v = 5^{h_v}w_v and gcd(r_v, 6) = 1. A 5-marker on v is allowed.

**(i) Triple bound.** Take a triple {a,b,c} ⊆ C′ = C∖{v}. All three inner edges have α = 3; this needs the full clique, not the star.
- L = 6r_a r_b r_c and γ = lcm(6,6) = 6.
- T3 gives μ(U_y(U_x ∩ U_z)) = T/(n_y I_xz) = τ/18. T2 bounds this by 3/6, so τ ≤ 9.
- I_xy = 18r_x r_y divides T, so 3L = 18r_a r_b r_c divides T. Hence 3 | τ and τ ∈ {3, 6, 9}.
- Both bounds are load-bearing: without 3 | τ, τ = 5 or 7 could share a prime with r_v.
- A 3-marker inside the triple only enlarges L.
- So gcd(n_v, T) = 6·gcd(r_v, τ r_a r_b r_c) = 6, for any e*, any 3-marker elsewhere, and a 5-marker on v.
- TG gives μ(Y_a ∪ Y_b ∪ Y_c) ≤ 5/6. ✓

**(ii) Tight C-edges.** α_vc + α*_vc = 6 = g. D_c ⊆ Y_c by V1, and both have measure 1/2, so D_c = Y_c. ✓

**(iii) Allowed sets.** The actual VFC labels, with q = α* (INV(b)), are d_c = 3r_c and d_d = q_d r_d, where q_d = α*_vd ∈ {1,2}.
- gcd(3r_c, 3r_c′) = 3.
- gcd(3r_c, q_d r_d) = 3^[f_d ≥ 2] · 2^[c = i*, q_d = 2].

The only pair with gcd ≥ 4 is (d, i*) when f_d ≥ 2 and q_d = 2, with gcd 6. Sun(4) then gives two facts:
- Every S_R contains at most three C-elements.
- d together with three C-elements occurs only as {d, i*, x, y}, with q_d = 2 and f_d ≥ 2.

If f_d = 1 this never occurs (E2). If there is no i*, every d–c gcd lies in {1, 3}, so it never occurs either (E4). ✓

**(iv) Counting.** Let m_k be the measure of cosets with k C-elements.
- Summing μ(D_c) over C′ gives m₁ + 2m₂ + 3m₃ = 5/2.
- A k-set meets 10 − C(5−k, 3) of the 10 triples, i.e. 6, 9 or 10 of them. So the ten triple bounds sum to 6m₁ + 9m₂ + 10m₃ ≤ 25/3.
- Subtract 10/3 times the identity: (8/3)m₁ + (7/3)m₂ ≤ 0.
- Hence m₁ = m₂ = 0 and the union has measure m₃ = 5/6.
- This C′-part is self-consistent, so the contradiction genuinely needs d.

**(v) The vertex d.** Any coset in D_d ∩ (∪D_c) must be of type {d, i*, x, y}, so that intersection lies inside D_d ∩ D_i*.

| Branch | Part of D_d outside the union | Total measure |
|---|---|---|
| q_d = 1 (any f_d, with or without i*) | 1/3 | 7/6 > 1 |
| q_d = 2, with f_d = 1 or no i* | 2/3 | 3/2 > 1 |
| q_d = 2, f_d ≥ 2, i* ∈ C′ | ≥ 2/3 − 1/2 = 1/6 | ≥ 1; killed by strict V4 (≤ 1 − 1/n_v) |

The no-i* branch is explicit (E4), and i* ∈ C′ whenever i* exists. ✓

**MINOR findings and repairs**
- **C-m1 (E3 wording).** Replace the choice sentence with: "choose v ∈ C with e_v = f_v = 1; this exists because |C| = 6, at most one C-vertex has e ≥ 2 and at most one has f ≥ 2."
- **C-m2 (§2(i)).** Delete the garbled clause "r_v odd, prime to 3 … see the remark below" and the withdrawn Remark. Replace them with: "gcd(r_v, τ r_a r_b r_c) = 1, since gcd(r_v, 6) = 1, the primes of τ lie in {2, 3}, and the r are pairwise coprime."
- **C-m3 (§2(iii)).** Merge (iii), E2 and E4 into the single gcd formula above. Only Sun(4) is load-bearing; E2's Sun(2) step is valid but not needed.
- **C-m4 (premises).** Cite VFC (V1)–(V4) and INV(b) directly, not "as used in K7-Z2-v1.md §5". Every borrowed fact re-derives from them: D ⊆ Y, μ(D) = α*/g, tight implies D = Y, labels n_j α*_vj / g_vj, and the union avoids U_v.
- **C-m5 ((iv)).** Add "each right coset has measure 1/n_v > 0", so that m₁ = m₂ = 0 means no such cosets exist.
- **C-m6 (statement).** Add the R0 lift to arbitrary groups. α and α* are preserved by the core quotient (LFC/INV verdict, item 6).
- **C-m7 (navigation and scope text).**
  - "In particular the three canonical probe-v14 patterns are impossible", and E3's parenthetical, rest on unreviewed exploratory output. Label both as navigation only.
  - Scope §3's "(i* with e* = 2 …)" contradicts the accepted frontier, where any e* ≥ 2 is open; CLIQUE itself has no e* restriction.
  - "Subject to v being a non-i* C-vertex" refers to the withdrawn star form and should go.
- **Optional (not the star form).** α* is used only on v's row. A valid weaker hypothesis is: α ≡ 3 on all C–C edges, and α*_vc = 3 for all c ≠ v at one v with e_v = f_v = 1. α must still be 3 on every inner edge.

**Imports and limits.**
- CLIQUE uses Sun(t) only through VFC (V3) inside U_v (|S_R| ≤ 6), and the only load-bearing instance is Sun(4).
- TG and L1 use no Sun.
- Sun(5), Sun(6) and Sun(7) are unused.
- Scope: CLIQUE excludes only the full-clique pattern α = α* = 3 on C. The K6.3 residue (3-marker on d, 2-marker i* in C) is otherwise untouched. Nothing here is evidence of a general K6.3 closure.
- The exploratory claim that TG kills every v14 survivor was not evaluated and is not a premise.

---

## Summary

| Item | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| (A) K62-A + erratum-v1 | Correct; accept with minor fixes | 0 | 0 | 4 |
| (B) Lemma TG | Correct; accept | 0 | 0 | 2 (+1 optional) |
| (C) K63-CLIQUE + E1–E4 | Correct as corrected; accept with minor fixes | 0 | 0 | 7 (+1 optional) |

Strictness of the LFC/V4 bound is load-bearing in exactly three places:
- Step 1 of K62-A at α_di* = 2;
- the row {2,4,4,4,4} in K62-A Step 2(b);
- CLIQUE's branch q_d = 2, f_d ≥ 2.

This is a single written hostile check, with no Lean and no human review. As written, (A) depends on the accepted, computer-assisted Sun(5); A-m4 shows how to remove it. No Sun(7), counterexample or novelty claim is made or supported.
