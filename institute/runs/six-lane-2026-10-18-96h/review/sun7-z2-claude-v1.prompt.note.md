**VERDICT: ACCEPT-WITH-FIXES.** There are 0 FATAL, 0 MAJOR and 10 MINOR findings.

I re-derived every step independently (record below) and found no missing case and no counterexample. All fixes are wording or import overlays; none changes a statement.

## Findings

**FATAL:** none.

**MAJOR:** none.

**MINOR**

1. **Stale ROW-1 import (header, §2, §7).**
   - ROW-1 is cited from `K7-M1-v1.md` as "CANDIDATE, under review". It is now accepted only together with the mandatory overlay `K7-M1-erratum-v1.md` (4094b537…c510).
   - Z2 must cite that overlay, specifically:
     - F2: actual exponents. Here m_p = 5^{h_p}, A = 0, B = h_p ≥ 1, and only [5 | m_p] enters a gcd.
     - F3: ROW-U-deg, used by ROW-1 (c).
     - F5: the corrected feasibility sentence in the last case of ROW-1 (b).
   - Update "K7-M1 (candidate)" in §7.

2. **ROW-1 is used outside its literal statement (§2).**
   - ROW-1 is stated for an unmarked apex v ∈ W in a configuration with exactly one marked vertex. Z-ROW applies it at the marked z, in a configuration with two marked vertices.
   - The parenthesis "its proof uses only the neighbours' labels" gives the right reason. It must be written as an explicit transfer hypothesis analogous to F3, call it **ROW-1-deg at v**:
     - g_vj = 6 for all six neighbours;
     - five neighbour labels have the form w_u·α_vu;
     - one neighbour label has the form m·w·α with m odd and {3,5}-smooth;
     - the w's are pairwise coprime and coprime to 30;
     - the LFC (d) bound holds at v.
   - Give the renaming explicitly: ROW-1's v ↦ z, ROW-1's z ↦ p.
   - The transfer is valid (D1).

3. **Undefined weights in the k3 ≥ 1 kill (§2).**
   - "U-part value 5" uses an undefined U and weights that are never stated in Z2. State them: 1/3 on the threes (k3 ≥ 3), 1 on the remaining ones, 1/2 on the remaining twos. There are no fours or fives by ROW-1 (b), so the value is 5.
   - Then state the weight on p with its feasibility check:
     - If α_zp = 1, put y_p = 1. λ_p = 5^{h_p}w_p is coprime to every label, because k5 = 0 and the unmarked entries lie in {1,2,3}.
     - If α_zp = 2, put y_p = 1/2. The only allowed sets through p are {p} and {p, two}, because every triple has all gcds equal to 2.

4. **Inverted application (§2, last sentence).**
   - State that excluding k5* = 5 for α* uses LFC (d) on α** = α (the INV (a) involution, as in M1-erratum F6).
   - In the case with no p, ROW-U applies to α* because of LFC-erratum E6.

5. **Unlisted imports.** Add the following to the import list:
   - R0 (used in the theorem's parenthesis);
   - LFC (a), (c) and (d), by name;
   - Sun(2) (LFC-erratum E2, via (V3) in (L2));
   - E6;
   - an explicit note that L1 and (F7) are also applied to the inverted configuration.

6. **False scope sentence (header).**
   - "Sun(t) inside U_z only with t <= 3 (through V3)" is false.
   - Z-ROW runs LFC/ROW-U/ROW-1 at z for both α and α*. That uses Sun(4) (R3), Sun(5) (R24) and Sun(6) (R5, e.g. six entries equal to 5 when there is no p), inside both U_z and g_zU_zg_z⁻¹.
   - Replace it with: "Sun(t), t ≤ 6, inside U_z and g_zU_zg_z⁻¹ only through LFC (§2); §5 uses only Sun(2) and Sun(3), through (V3)."
   - This is not a logical gap, because all of these are accepted imports.

7. **CROSS notation and orientation (§4).**
   - x = α_ab collides with L1's vertex labels {x,y,z}.
   - "5^h" should be 5^{h_p}, and s, s* need their subscripts.
   - In the α*-triangle (4, s*, x*) the small entry sits at b, not a. The table still transfers, because:
     - both edge-at-z terms ignore odd ℓ (s/gcd(s,ℓ) = s and 4/gcd(4,ℓ) = 4);
     - τ_max is symmetric under a ↔ b.
     
     Say so.
   - (C3)'s "τ_min = 4" holds only for x ∈ {2,4}, i.e. after (C1). For x = 3 it is 12, and for x = 5 it is 20 or 4. Put this qualifier in the statement, not only in the proof.

8. **LIGHT gcd identity (§5) and the disjointness step (T1).**
   - State that d_v = q_v·n_v/6 = α*_zv·r_v = λ*_v.
   - State that gcd reduction needs two facts: α* ∈ {1,2,4} (from Z-ROW), and r_v odd for every v ≠ z. The second is the load-bearing "centre" fact (only z carries the 2-marker), and §5 does not state it.
   - In T1, add: D_b ∩ D_b′ is left U_z-invariant, so if it is nonempty it contains a right coset R ⊆ D_b ⊆ D_a. Also add: if at most one element of F is "out", every pair in F contains an "in" element.

9. **T2 by inversion (§6).** Spell out the swap:
   - F_inv = F* and F*_inv = F;
   - s_inv = s* and s*_inv = s;
   - a0 plays the role of b0;
   - Z-ROW, CROSS and LIGHT hold for the inverted configuration (same z, same markers, α** = α).

10. **Probe remark (status line).** Scope the "probe v10" remark to the probed range of capped tuples, as M1-erratum F8 does. It is not a premise.

## Independent re-derivation record

**D1. Z-ROW.**
- **Facts used at z.**
  - g_zj = 6 for every neighbour, and λ_j = r_j·α_zj (LFC (a)).
  - Σ y_j α_zj ≤ 6 − 6/n_z < 6 (LFC (d)).
  - For j ≠ z, r_j is odd and 3 ∤ r_j (H plus pairwise coprimality).
  - None of these depends on m_z. That is why ROW-U (stated for v "marked or not") and ROW-1's proof both apply at the marked centre.
- **No p.** All six neighbours are unmarked. ROW-U gives (i)–(iii) for α, and for α* via E6.
- **p exists** (m_p = 5^{h_p}, h_z = 0).
  - gcd(λ_u, λ_u′) = gcd(α, α′).
  - gcd(λ_p, λ_u) = gcd(α_zp, α_zu), except that it equals 5 whenever α_zu = 5.
  - This is exactly ROW-1's label structure with A = 0, B = h_p.
- **Weight checks with p present.**
  - 1 ≤ k5 ≤ 4: put y = 1/k5 on R5 and y_p = 0 (T∖{p} is allowed and has the same sum), with standard weights elsewhere. The value is ≥ 5 + 1.
  - k3 ∈ {1,2}: then k5 = 0, and the value is ≥ 3 + min(N,4) with N ≥ 3.
  - k3 ≥ 3 with a four: the value is ≥ 3 + {5,3,4} when k3 = 3, and 4 + 4 when k3 = 4.
  - α_zp ∈ {3,4,5}: the value is 5 + α_zp/3. The allowed sets through p are among {p}, {p,x} and {p,3,3}. {p,3,3,3} would need a gcd ≥ 4, and {p,2,2} would need a gcd ≥ 3.
  - α_zp = 1: the value is 5 + 1. α_zp = 2: the value is 5 + 1.
  - So k3 = 0.
- **k5 = 5.** Then α*_zu = 1 on those five neighbours. The α*-labels w_u and 5^{h_p}w_p·α*_zp are pairwise coprime. Putting y ≡ 1 gives 5 + α*_zp ≥ 6, contradicting LFC for the inverted configuration.
- **Conclusion.** The unmarked entries lie in {1,2,4}. ROW-U-deg then holds for the full row, for every α_zp, because a 2-power α_zu against the odd factor 5^{h_p}w_p gives gcd(α_zp, α_zu). The argument for α* is symmetric, using α** = α.

**D2. The two sides F and F*.**
- |F| ≥ 3 and |F*| ≥ 3 by (iii), and F ∩ F* = ∅ because 4 + 4 > 6. So N = F ⊔ F* with |F| = |F*| = 3.
- For a ∈ F*: s_a ≤ 6 − 4, so s_a ∈ {1,2}, and at most one s_a equals 1 by (ii).
- Symmetrically for s*_b with b ∈ F.

**D3. CROSS table.**
- Here γ = g = 6 and ℓ = r.
- τ_min = lcm(s, 4, x/gcd(x, r_z)), with gcd(x, r_z) = 2^{min(v₂x, ε)}·5^{min(v₅x, h_z)}. There is no 3-part, by H.
- τ_max = min(xs, 4·min(s,x), s·min(4,x)), from apexes z, a and b.

| s | x | τ_min | τ_max | outcome |
|---|---|---|---|---|
| 2 | 1 | 4 | 2 | kill |
| 2 | 2 | 4 | 4 | τ = 4 |
| 2 | 3 | 12 | 6 | kill |
| 2 | 4 | 4 | 8 | τ ∈ {4,8} |
| 2 | 5 | 20 / 4 | 8 | kill if h_z = 0 / survive if h_z ≥ 1 |
| 1 | 1, 2, 3 | 4, 4, 12 | 1, 2, 3 | kill |
| 1 | 4 | 4 | 4 | τ = 4 |
| 1 | 5 | 20 / 4 | 4 | kill / survive |

- The table holds for every ε ≥ 1; x = 4 gives τ_min = 4 whether ε = 1 or ε ≥ 2.
- The α*-triangle (4, s*_b, x*) gives the same table by a ↔ b symmetry.
- **Excluding 5.** x = 5 forces x* ≤ 1 (INV (b) on the pair ab). x* = 1 dies for both values of s*, because τ*_max = s* < 4. The case x* = 5 is symmetric.
- **Hence (C1):** (α_ab, α*_ab) ∈ {(2,2), (2,4), (4,2)}.
- **(C2)** is the s = 1 row, read after (C1).
- **Where the 5-marker sits.**
  - On p ≠ z: ℓ_z contains no 5, so x = 5 already dies by T.
  - On z: x = 5 dies only through the inverse.
  - A 5 inside ℓ_a or ℓ_b never matters, because s and 4 are 5-free.

**D4. F7 orientation.**
- At apex z with the pair (a,b), the F7 condition τ_min·6 ≥ 6·α_ab·α_za is equivalent to x·s_a ≤ 4.
- When it holds, (T3) at z meets the (T2) bound μ(X_a). So U_z(U_a ∩ U_b) = X_a ⊆ X_b. This is consistent with μ(X_a) = s_a/6 < 4/6 = μ(X_b).
- The pinned τ = x·s_a = 4 ≤ τ_max in both live instances, (s,x) = (2,2) and (1,4). The case (2,4) is not forced.
- Inverted configuration: X*_b ⊆ X*_a if and only if x*·s*_b ≤ 4.
- The X's do not depend on coset representatives, so F7 combines safely with the g_z = 1 normalisation used by VFC.

**D5. LIGHT.**
- **Measures.** D_v ∩ X_v = ∅ by (V1)/L0.2. μ(D_v) = α*_zv/6 because the true q is α* (INV (b)), and μ(Y_v) = 1 − α_zv/6.
- **Tight edges.** The two finite sets have equal size, so D_v = Y_v.
- **Coset structure.** Both D_v and Y_v are left U_z-invariant, so they are unions of right cosets.
- **Allowed sets.** By (V3), S_R is allowed for d_v = α*_zv·r_v. Its gcds are 2-power gcds of the α* values, because r_v is odd for v ≠ z.
- **(L1).** The gcds in {a,b,b′} are s*_b, s*_b′ and gcd(s*_b, s*_b′), all ≤ 2 < 3.
- **(L2).** α* = 1 gives a label coprime to every other label, so |S_R| = 1.
- **(V4).** μ(∪D) ≤ 1 − 1/n_z < 1.

**D6. Row types.**
- The four types (a0 present or not, b0 present or not) are exhaustive. Edge za is tight iff s_a = 2, and edge zb is tight iff s*_b = 2.
- **T4.** (C2) applied twice gives (4,4), contradicting (C1).
- **T3.**
  - α*_{ab0} = 4, so α_{ab0} = 2 by (C1).
  - Hence X_a ⊆ X_{b0} (since 2·2 = 4).
  - Then D_{b0} ⊆ Y_{b0} ⊆ Y_a = D_a, and μ(D_{b0}) = 1/6 > 0.
  - Any R ⊆ D_{b0} has {a, b0} ⊆ S_R, contradicting (L2).
- **T2.** I checked the inversion explicitly: X*_b ⊆ X*_{a0}, D*_{a0} ⊆ D*_b, and the label α_{za0} = 1 triggers (L2).
- **T1.**
  1. Call b "in" when some a ∈ F* has α_ab = 2. Then X_a ⊆ X_b, so D_b ⊆ D_a.
  2. By (L1), D_b is disjoint from every other light set D_b′. The light sets have μ = 2/6; the D_a are heavy, with μ = 4/6.
  3. If at most one b is out, the three D_b are pairwise disjoint. Their total measure is 3·2/6 = 1 > 1 − 1/n_z, a contradiction.
  4. So at least two b are out, which means α_ab = 4 for all a.
  5. The inverted argument gives at least two a with α*_ab = 4 for all b.
  6. Take an out a and an out b: then α_ab = α*_ab = 4, contradicting (C1).
- **Mutation controls.**
  - α ≡ 4, α* ≡ 2 on F*×F survives the forward step and dies only in the inverted step. The inverse step is load-bearing.
  - If z had a 3-marker, (s,x) = (2,3) would give τ_min = 4 ≤ 6, so (C1) would fail. H's no-3 clause is load-bearing.

**D7. Exponents, R0 and imports.**
- **Exponents.** ε ≥ 1, h_z ≥ 0 and h_p ≥ 1 are arbitrary. They enter only through x/gcd(x, r_z) and through [5 | m_p]. No capping is used anywhere.
- **R0.** The finite-core quotient preserves the labelled index tuple and coset disjointness, hence also H.
- **Imports actually used.**
  - LFC (a), (c), (d);
  - INV (a), (b) with E6;
  - ROW-U with E8;
  - ROW-1 with M1-erratum F2, F3 and F5;
  - L0.2/L0.3 and L1 (T1)–(T3);
  - VFC (V1), (V3), (V4) and (F7);
  - Sun(t) for t ≤ 6, through LFC;
  - R0.
- **Not used:** Ppair, K, the RPLP linear program, least-order frames, Sun(7) and any computation.
- **Claims.** Neither Sun(7) nor novelty is claimed.

After the overlay, the open part of K7 is exactly: configurations with both a 2-marker and a 3-marker, plus configurations with no 2-marker where the 3- and 5-markers sit on different vertices.
