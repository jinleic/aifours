# Referee report: Theorem Z23-P5 (K7-Z23-P5-v1, SHA 6325503…8e04)

## Verdict: **ACCEPT-WITH-FIXES** (0 FATAL, 0 MAJOR, 6 MINOR)

I re-derived every step by hand. Each local certificate, each triangle evaluation and each containment argument holds as written, with E, A, B ≥ 1 arbitrary. All six findings are wording or overlay fixes; none changes a statement or a weight. The theorem holds in finite groups and, through R0, in arbitrary groups with finite-index subgroups.

Convention below: at an apex v the label of neighbour j is λ_j = r_j·α_vj. A certificate means a feasible y with Σ y_j α_vj ≥ 6, which contradicts LFC (d) (the sum must be < 6).

## Sub-verdicts

| Section | Sub-verdict |
|---|---|
| §1 (z-rows) | ACCEPT |
| §2 (LT1–LT3; not requested but used in §§5, 7) | ACCEPT |
| §3 (no W–W five) | ACCEPT |
| §4.1 | ACCEPT |
| §4.2 | ACCEPT |
| §4.3 | ACCEPT-WITH-FIXES (m3: the feasibility audit is incomplete as written; every certificate is in fact feasible) |
| §5 | ACCEPT (editorial m4–m6) |
| §6 | ACCEPT |
| §7 | ACCEPT |
| Inverse scope, R0, import scope | ACCEPT (m1) |

## Attack point 1: §1

**G2 applies at z.** The G2 conditions at z are:
- g_zj = 6 for all six neighbours.
- Five labels have the form w_u α_zu, with the w's pairwise coprime and prime to 30.
- The sixth label is 5^B w_p α_zp, whose marker 5^B is odd and {3,5}-smooth (actual exponent, per M1 erratum F2).
- LFC (d) holds at z.

ROW-1's proof reads only the six neighbour labels and LFC (d). The apex cofactor 2^E3^A w_z enters only through 1 − 1/n_z. So G2 applies, with ROW-1's apex renamed z and its marked neighbour renamed p.

**k5 = 5.** INV gives α*_zu = 1 for all five u. The inverse labels w_u and 5^B w_p α*_zp are pairwise coprime, since w_u is prime to 30 and α* ≤ 5. Then y ≡ 1 is feasible with value 5 + α*_zp ≥ 6. ✓

**3-type row.** ROW-1(b) gives k3 ≥ 3, W-entries in {1, 2, 3} and α_zp ∈ {1, 2}.
- The W-weights (threes 1/3, ones 1, twos 1/2) have value exactly k3 + k1 + k2 = 5. They are feasible:
  - no allowed set holds more than three threes (Sun(4));
  - no allowed set holds more than two twos (an all-gcd-2 triple is forbidden by Sun(3));
  - the classes never mix.
- **α_zp = 1:** λ_p = 5^B w_p is coprime to every label, so p lies only in {p}. y_p = 1 adds 1.
- **α_zp = 2:** gcd(λ_p, ·) is 2 with a two and 1 with a one or a three. The allowed sets through p are:
  - {p}: weight 1/2;
  - {p, two}: weight 1/2 + 1/2 = 1;
  - {p, two, two}: all gcds 2, forbidden;
  - {p, one}, {p, three}, {p, two, three}: forbidden.
  
  y_p = 1/2 adds 1.
- The total is 6 in both cases. ✓

**ROW-1(c).** All W-entries now lie in {1, 2, 4}, i.e. are powers of 2. Hence gcd(5^B α_zp w_p, α_zu w_u) = gcd(α_zp, α_zu), so ROW-U-deg holds. The full six-entry row, including α_zp ∈ {1, 2, 4}, is 4-type. ✓

**Inverse.** The same hypotheses hold for α*, and the inverse k5 = 5 kill uses the original LFC (α** = α). This gives |F| = |F*| = 3 and s_a, s*_b ∈ {1, 2}. ✓

## Attack point 2: §3

**Cross-class gcds.** For unmarked labels, gcd(α, α′) is 1 between any two of the classes {1}, {2, 4}, {3}, {5}. So these gcds really are all 1. ✓

**1 ≤ k5 ≤ 3.** The fives contribute 5. The remaining 4 − k5 ≥ 1 vertices take the standard weights, and each nonempty class contributes ≥ 1. With y_z = y_p = 0, heredity makes the certificate valid. ✓

**k5 = 4.** λ_z = 2^E3^A α_vz w_z, with α_vz ∈ {1, 2, 4} from §1 and symmetry, so λ_z is coprime to every 5w_u. Thus z is a singleton among the positive-weight vertices. The fives contribute 5 and z adds α_vz, for a total ≥ 6. ✓ Correctly, y_p is not used here, since p shares the prime 5 with the fives.

**Inverse.** The same argument applies, using §1 for α*. ✓

## Attack point 3: §4

### §4.1
- **k = 1:** 3 + min(3, 4) = 6. ✓
- **k = 2:** the remainders (1,2), (1,4), (2,4), (4,4) contribute 3, 5, 3, 4 with the stated weights. With the threes at 1/2 (value 3) each total is ≥ 6. The remainders (1,1) and (2,2) are capped at 2, so they survive. ✓
- **k = 3:** a remaining 4 at weight 1 gives 3 + 4 = 7. ✓

### §4.2
- **c ∈ {1, 5}:** p is coprime to the labels with α ∈ {1, 2, 3}, so y_p = 1 adds c ≥ 1.
- **c ∈ {2, 4} with remainder ones:** p is isolated, so y_p = 1 adds c ≥ 2.
- **c ∈ {2, 4} with remainder twos:** y_p = 1/2. The set {p, two} has weight 1; {p, two, two} has all gcds 2 and is forbidden. This adds c/2 ≥ 1.
- Hence c = 3. ✓

### §4.3: every row recomputed (b = 4)

Pair gcds of the labels, independent of the sizes of E, A, B ≥ 1:

| Pair | gcd |
|---|---|
| three–three | 3 |
| three–z | 3 |
| two–two | 2 |
| two–z | 2 |
| two–three | 1 |
| one–anything | 1 |
| p–three | gcd(c, 3) |
| p–two | gcd(c, 2) |
| p–z | c for c ∈ {2, 3, 4}; 1 for c ∈ {1, 5} |

The only pair with gcd ≥ 4 is (p, z) at c = 4. With one remainder two at most, no 4-set is allowed, so every allowed set has size ≤ 3.

Weights: y = 1/3 on each three and on z.

| k | rem | c | rem wts; y_p | total (recomputed) | binding allowed sets |
|---|---|---|---|---|---|
| 2 | (1,1) | 3 | 1, 1; 1/3 | 2 + 2 + 4/3 + 1 = 19/3 | 3-subsets of {t, t, z, p} = 1 |
| 2 | (2,2) | 3 | ½, ½; 1/3 | 19/3 | {two, two} = 1; {two, z} = 5/6; {two, two, z} forbidden |
| 3 | 1 | 1, 5 | 1; 1 | 16/3 + c ≥ 19/3 | p a singleton |
| 3 | 1 | 2, 4 | 1; 2/3 | 20/3 or 8 | {p, z} = 1 |
| 3 | 1 | 3 | 1; 1/3 | 19/3 | 3-subsets of {t, t, t, z, p} |
| 3 | 2 | 1, 5 | 2/3; 1 | ≥ 20/3 | **{two, z} = 1 (unstated)** |
| 3 | 2 | 2 | 2/3; 1/3 | 19/3 | {two, z} = 1; {p, two} = 1; {p, z} = 2/3; {p, z, two} forbidden |
| 3 | 2 | 3 | 2/3; 1/3 | 20/3 | **{two, z} = 1 (unstated)**; cluster 3-subsets = 1 |
| 3 | 2 | 4 | 0; 2/3 | 7 | {p, z} = 1; {p, z, two} allowed with weight 1 |
| 4 | – | 1, 5 | –; 1 | ≥ 19/3 | p a singleton |
| 4 | – | 2, 4 | –; 2/3 | ≥ 20/3 | {p, z} = 1 |
| 4 | – | 3 | –; 1/3 | 19/3 | 3-subsets of the 6-cluster |

- **Totals:** every total matches the candidate's table, and all exceed 6.
- **Completeness:**
  - k = 1 is dead by §4.1.
  - k = 2 forces remainder (1,1) or (2,2) and c = 3, by §4.1 and §4.2.
  - k = 3 forces remainder ∈ {1, 2}: no 4 by §4.1, no 5 by §3.
  - For k ∈ {3, 4} all c ∈ {1, …, 5} are enumerated.
  - **No (k, remainder, c) case is missing.**
- The k ≥ 3 rows are load-bearing: they are what place all of W3 inside F* in §5.

## Attack point 4: §5

**Locating W3.** Within W3 the 3-graph has minimum degree ≥ 2, so |W3| ≥ 3. By §4.3 and §1, W3 ⊆ W∖F = F* ∩ W. Hence W3 = F*, p ∈ F, and P = F ∩ W has size 2. Each v ∈ W3 has k = 2, so α_vp = 3 and α_vu1 = α_vu2 = x ∈ {1, 2}.

**Triangle (s_v, 4, x).**
- τ_min = lcm(s_v, 4, x/gcd(x, r_z)) = 4.
- τ_max = min(x s_v, 4 min(s_v, x), s_v x) = x s_v.
- So x = s_v = 2, the edge zv is tight, and D_v = Y_v. ✓

**Excluding s*_b = 1, case b = p.**
- The inverse triangle is (4, 1, x*), with 4/gcd(4, ℓ_p) = 4. So τ*_min ≥ 4 and τ*_max = min(x*, 4), forcing x* ≥ 4.
- x* = 5 gives τ*_min = 20, since 5 ∤ r_z.
- x* = 4 gives α_vp + α*_vp = 3 + 4 > 6, contradicting INV. ✓

**Excluding s*_b = 1, case b ∈ P.**
- F7 holds: 4·6 ≥ 6·2·2. So X_v ⊆ X_b and D_b ⊆ Y_b ⊆ Y_v = D_v.
- The local indices are d_b = w_b and d_v = 4w_v, which are coprime. Since μ(D_b) = 1/6 > 0, this contradicts LT2. ✓

**Three disjoint light sets.**
- D_u ⊆ D_v holds for u ∈ P.
- A nonempty D_u ∩ D_b′ contains a right coset R, because it is left U_z-invariant. Then R ⊆ D_v as well.
- The local indices 4w_v, 2w_u, 2r_b′ have all pairwise gcds 2, so {v, u, b′} ⊆ S_R contradicts LT1.
- So D_u1, D_u2, D_p are pairwise disjoint, each of measure 1/3 (since s*_b = 2). Their union has measure 1, contradicting LT3. ✓

## Attack point 5: §§6–7

**§6.**
- The W-entries lie in {1, 2, 4}, and E8 gives value ≥ 4.
- λ_p = 3·5^B w_p or 5^{B+1} w_p is coprime to every such W-label. So y_p = 1 adds 3 or 5, for totals 7 or 9.
- y_z = 0 together with heredity neutralises the gcd(λ_z, λ_p) > 1 issue. ✓

**§7: CROSS and the four types.**
- **CROSS, with r_z free of 5:** τ_min = 4 for x ∈ {1, 2, 4}.
  - s_a = 1 gives τ_max ∈ {1, 2, 4}; s_a = 2 gives τ_max ∈ {2, 4, 8}.
  - Hence x ∈ {2, 4}, and s_a = 1 forces x = 4.
- **F7** holds exactly when x s_a ≤ 4.
- **Exclusion of x = 3 is required and correctly ordered.** With A ≥ 1, x = 3 would give τ_min = 4 ≤ τ_max = 6 at s_a = 2. §§5–6 remove x = 3 before §7 needs it.
- **Odd ℓ.** ℓ_p = 5^B w_p is odd, so all CROSS, F7 and LT computations hold verbatim whether p ∈ F or p ∈ F*. This includes b0 = p, where d_p = 5^B w_p is coprime to 4r_a.
- **The four types are exhaustive and each closes:**
  - Both a0 and b0 exist: (4, 4) on their edge, contradicting INV.
  - Only b0: F7 + tightness + LT2.
  - Only a0: the same argument by inversion.
  - Neither: "in" sets are separated by LT1 and LT3, and the two "out" sides cross with α = α* = 4. ✓

## Attack point 6: inverse scope, R0, silent imports

**Inverse.** Every step uses only the labelled index tuple:
- E6 gives the same markers on the same z and p.
- α** = α, and inversion is an involution.
- §§1, 3, 4, 5, 6 are each established for α* before they are used.

**R0.** The finite-core quotient preserves the indices and disjointness. INV is then applied inside the finite quotient. ✓

**Import scopes.**
- ROW-1 is used only at z, whose marked neighbour p carries an odd marker. It is never used at a W-apex.
- ROW-1(c) is never used with an even-marked neighbour.
- At W-apexes, only explicit LFC certificates appear. The ROW-U standard weights and E8 are used there only on unmarked neighbours with y_z = y_p = 0, the same zero-extension the accepted M1 proof uses.
- T and F7 are used in their general forms with γ = 6 and ℓ = r.
- VFC is used with q = α*.
- Sun(2), Sun(3), Sun(4) enter only through LFC(c)/(V3); Sun(5), Sun(6) only through the imported ROW-U/ROW-1 class analysis. Sun(7) is never used.
- No silent out-of-scope use found.

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

- **m1 (§0, import list).** Erratum E2 (Sun(2)) and E6 (the inverse has the same labelled tuple and markers) are used but not named. LT1/LT2 are (V3) applied with d_j = α*_zj r_j from (V2). The primary acceptance record for L1/VFC/F7, the written verdict 73a25ba6… cited by K7-Z2, is reached only through the Z2 parent verdict.
  - *Repair:* name E2, E6, (V2)/(V3) and 73a25ba6.
- **m2 (§1, sentence "This is precisely the accepted ROW-1 degree transfer…").**
  - *Repair:* list G2's four clauses explicitly: g_zj = 6; five labels w_uα_zu; sixth label m w α with m = 5^B under F2 actual exponents; LFC (d) at z. Also state the renaming (apex → z, marked neighbour → p).
- **m3 (§4.3, feasibility paragraph).** The claim "covering every allowed set" omits the allowed pair {two, z} (gcd 2) in rows (k=3, rem 2, c ∈ {1,5}) and (k=3, rem 2, c=3). Its weight there is 2/3 + 1/3 = 1, so the certificates stand.
  - *Repair:* insert "A remainder two always partners z (gcd 2), and partners p only for c ∈ {2,4}; {two, z} weighs 1/3 + 2/3 = 1 (k=3) or 1/3 + 1/2 (k=2)."
- **m4 (§5, paragraph "We next show s*_b = 2").** For b ∈ P the inverse-triangle computation (x* = 4) is unused. The contradiction there is F7 + tightness + LT2 alone.
  - *Repair:* split the paragraph into case b = p (inverse T + INV with α_vp = 3) and case b ∈ P (F7 + LT2).
- **m5 (§§5, 7, notation and precision).** The letter x for α_vu / α_ab collides with L1's vertex letters (Z2 G7 precedent). Also, "x/gcd(x, r_z) divides 2" should read "equals 1 (E ≥ 1)".
  - *Repair:* rename to x_vu / x_ab and fix the phrase.
- **m6 (§5 last sentence; §7 "inverse" steps).** The inverse dictionary is implicit.
  - *Repair:* state it as in Z2 G9:
    - W3* ⊆ F, p ∈ F*, P* = F* ∩ W;
    - the tight edges are zb for b ∈ F;
    - the excluded value is s_a = 1, using α*_vp = 3 when a = p;
    - the light sets are D*_a with μ = α_za/6 = 1/3, and LT1*–LT3* apply;
    - §§1, 3, 4 are invoked for α*.

**Non-defect remarks.**
- The §8 frontier sentence is correctly marked conditional and is not a premise.
- If A = 0 the §4.3 feasibility would only improve. That case is out of scope here, but it shows the certificates are not fragile in A.
