# K52-W hostile review: verdict

**The written proof establishes Theorem K52-W at its stated scope.**

| Severity | Count |
|---|---|
| FATAL | 0 |
| MAJOR | 0 |
| MINOR | 4 |
| Nits (not counted) | 3 |

None of the findings changes a lemma statement, a case, a certificate or an objective value. Status stays CANDIDATE_UNVERIFIED: this is one model family, and the other family and the parent are still outstanding.

**Basis.** I reviewed the pasted text only. Per your no-tools instruction I opened no files and recomputed no hashes, byte counts or manifest ranges. Sun(4) is taken at its accepted README:11/:15 scope and not re-proved.

**Paths.** All references are to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k52-written/K52-W-v1.md` unless marked `pkg` (the review package in the same directory).

## Claim-by-claim

| # | Claim | Lines | Verdict |
|---|---|---|---|
| 1 | Class identification | 19–23 | Correct; MINOR-2 |
| 2 | SHAPE ⇔ README:94 | 25–43 | Correct in both directions |
| 3 | R0 | 59–61 | Correct |
| 4 | Lemma A | 63–69 | Correct |
| 5 | INV on the actual inverse | 71–79 | Correct; MINOR-1 |
| 6 | Fibre geometry and 24-admissibility | 82–94 | Correct; MINOR-3 |
| 7 | FC24 | 96–99 | Correct |
| 8 | Local gcd table and d–s table | 101–128 | Correct |
| 9 | Certificate U | 131–137 | Correct |
| 10 | Defect in the uniform sketch | 139–142 | Correct; the defect is genuine |
| 11 | Certificate E | 144–152 | Correct |
| 12 | B1 | 155–164 | Correct |
| 13 | B2 | 166–173 | Correct |
| 14 | Theorem K52-W | 175–181 | Correct |
| 15 | DAG and import boundary | 183–196 | Correct; MINOR-4 |
| 16 | Review package | pkg 1–70 | Verbatim block at pkg 18–24 matches candidate 175–181; every section pointer at pkg 37–49 is right |

## Independent re-derivation

### SHAPE

**Forward direction.**
- d_j ∈ E∖A_3 gives n_dj = 4q_j with 3∤q_j.
- s ∈ C∩E gives 12 | n_s.
- o ∈ C∖E gives v_2(n_o) = 1 and 3 | n_o, so n_o = 6r_o with r_o odd.

**The gcd identities:**
- gcd(4q_1, 4q_2) = 4·gcd(q_1, q_2)
- gcd(4q_j, 12q_s) = 4·gcd(q_j, 3q_s)
- gcd(4q_j, 6r_o) = 2·gcd(2q_j, 3r_o)
- gcd(12q_s, 6r_o) = 6·gcd(2q_s, r_o)
- gcd(6r_o, 6r_u) = 6·gcd(r_o, r_u)

So the line-94 matrix (4, 4, 2, 6, 6) holds exactly when:
- the seven cofactors are pairwise coprime,
- 3 ∤ q_1q_2, and
- every r_o is odd.

**Converse.** The same identities give the matrix, and from it:
- C = {s}∪O_4, since 6 divides n_s and every n_o, and 3∤n_d.
- D ⊆ (A_2∖A_3)∩E.
- C∩E = {s}, since v_2(n_o) = 1.
- a ≤ 1, since 4, 6 and 12 are prime to 5, so 5 divides at most one cofactor.

**Markers.** Nothing is dropped or strengthened:
- The higher 2-part can sit on q_1, q_2 or q_s, at most one of them.
- The higher 3-part can sit on q_s, on one r_o, or nowhere.
- The factor 5 can sit anywhere or nowhere.
- No exponent or cofactor is bounded.

### R0, Lemma A and INV

**R0.** N ⊆ U_j, so each coset is a union of N-cosets. Images keep index n_j, and disjointness is preserved. Class, SHAPE and marker data are functions of the labelled index tuple (erratum E6), so they are preserved too. All α are recomputed in G/N.

**Lemma A.**
- lcm(n_i, n_j) divides I_ij.
- |U_iU_j|/|G| = α/g.
- g_i⁻¹g_j ∉ U_iU_j, so α ≤ g−1.

Hence α_{d_j o} = 1, and α_{d_1d_2}, α_{d_j s} ∈ {1, 2, 3}. The same holds in the inverted configuration.

**INV.**
- (g_jU_j)⁻¹ = g_j⁻¹(g_jU_jg_j⁻¹), a left coset of a conjugate with the same index.
- Conjugating by g_i⁻¹ gives α*_ij = [G : U_i∩hU_jh⁻¹]/lcm, with h = g_i⁻¹g_j.
- U_iU_j and U_ihU_j are distinct double cosets, hence disjoint, with measures α/g and α*/g.
- Therefore b + b* ≤ 4.

### FC24

- λ_j = n_j·α/g and t_j = n_v·α/g, so t_j/n_v = α/g.
- The translated pieces x⁻¹p_j(U_j∩U_v) are pairwise disjoint left cosets in U_v of indices λ_j.
- Condition (i) is Sun(2) applied to each pair. Condition (ii) is Sun(4) applied to each 4-subfamily.
- For |S_B| = 5 or 6, only the 2- and 4-subfamilies are invoked. No statement about a 5- or 6-subfamily is used anywhere.
- Summing over the n_v − 1 fibres other than the own fibre gives Σ y_j t_j ≤ n_v − 1.
- The strict gap comes from the missing own fibre, not from an approximation.

### Local data at apex d_1 (b ∈ {1, 2})

The labels are λ_d = bq_2, λ_s = 3aq_s and λ_o = 3r_o, with masses b/4, a/4 and 1/2.

**Pair gcds:**
- o–u: 3.
- s–o: 3·gcd(a, r_o). This is 9 exactly when a = 3 and 3 | r_o, which happens for at most one t.
- d–o: gcd(bq_2, 3r_o) = 1, because r_o is odd, 3∤q_2, and the cofactors are coprime.
- d–s, for a = 1, 2, 3:
  - b = 1: 1, gcd(q_2, 2), 1.
  - b = 2: gcd(2, q_s), 2, gcd(2, q_s).

The d–s values match lines 120–123.

**Other primes.** The primes 5 and ≥7 never enter, because a, b ≤ 3 contribute only the primes 2 and 3.

**Edge cases checked.**
- λ_d = 1 (b = 1, q_2 = 1) is harmless: d is singleton-only.
- Equal trace subgroups are possible (see MINOR-3).

### Complete list of 24-admissible sets at d_1

- **Sets containing d:** any set with d and some o has a gcd-1 pair, so these sets are ⊆ {d, s}. The pair {d, s} is admissible only when the d–s entry is 2.
- **Sets without d:** these are ⊆ L = {s}∪O_4.
  - Generic case: exactly the subsets of size ≤ 3.
  - Exceptional case: also the three sets {s, t, x, y}.
  - L itself is never admissible, because O_4 is a mutually-gcd-3 4-set.
- **Size bound:** no admissible set has 5 or 6 elements. This is derived, not assumed.

### Feasibility of U and E

**Certificate U.**
- Subsets of L weigh at most 3·(1/3) = 1.
- {d, s} weighs at most 2/3 + 1/3 = 1.
- y_d = 1 is used only when the d–s gcd is 1 (b = a = 1).

**Certificate E.**
- The positive-weight vertices {s}∪(O_4∖{t}) are mutually gcd 3, so any admissible set contains at most three of them.
- The sets {s, t, x, y} weigh exactly 1, with the zero-weight t present.
- For b = 2, {d, s} weighs 2/3 + 1/3 = 1.
- For b = 1, a = 3, {d, s} is inadmissible because gcd(q_2, 9q_s) = 1, so y_d = 1 is feasible.

### Every case

| b | a | t? | Certificate | y_d | Objective |
|---|---|---|---|---|---|
| 1 | 1 | – | U′ (line 136) | 1 | 1 |
| 1 | 2 | – | U | 2/3 | 1 |
| 1 | 3 | no | U | 2/3 | 13/12 |
| 1 | 3 | yes | E | 1 | 1 |
| 2 | 1 | – | U | 2/3 | 13/12 |
| 2 | 2 | – | U | 2/3 | 7/6 |
| 2 | 3 | no | U | 2/3 | 5/4 |
| 2 | 3 | yes | E | 2/3 | 13/12 |

Every value is ≥ 1, while FC24 gives an upper bound of 1 − 1/n_{d_1} < 1. So B1 and B2 hold.

### Finish

1. B1 and B2 together force α_{d_1d_2} = 3 in every finite K5.2* configuration.
2. The actual inverted configuration is such a configuration: same finite group, same labelled tuple, same t-status, and every a* ∈ {1, 2, 3} is covered.
3. So b* = 3 as well, and 3 + 3 ≤ 4 is false.

The text's route (b, b* ≥ 2 and b + b* ≤ 4 give b = 2, contradicting B2) is the same argument. The case b = 3 forces b* = 1, which B1 rules out on the inverse. It is not omitted.

## Your specific checks

- **Class normalisation against README:94:** exact. Every gcd, prime-incidence and marker condition is encoded, and nothing is dropped or strengthened.
- **R0 preserves indices, disjointness, labelled tuple, SHAPE and markers:** yes.
- **B1 on the actual inverse (b* ≥ 2):** yes. B1's only hypotheses are a finite G, pairwise disjoint left cosets, and a labelled tuple in K5.2*.
- **B2 and INV, including b = 3:** yes.
- **FC24 on 5- and 6-element fibres via 2- and 4-subsets:** yes.
- **Sun(3), Sun(5), Sun(6):** not used anywhere, including in R0, A, INV and SHAPE.
- **Hidden premises:** none from StageB code or outputs, from any K52 conclusion, or from a minimal-counterexample frame. The parent sketch is re-derived and corrected, not used as a premise.
- **KII and D2′:** not claimed.

## Findings and minimal repairs

**MINOR-1: `K52-W-v1.md:78` (INV).**
- **Problem:** "by the same product-count formula" is not literally applicable. The formula at lines 65–66 covers HK for subgroups H and K, and U_ihU_j is not such a product.
- **Repair:** insert "U_ihU_j = (U_i·hU_jh⁻¹)h, so |U_ihU_j| = |U_i||U_j|/|U_i∩hU_jh⁻¹| = |G|·[G:U_i∩hU_jh⁻¹]/(n_in_j)."

**MINOR-2: `K52-W-v1.md:19-23`, with `:175-176`.**
- **Problem:** the CE bound (gcd ≤ 6 for all 21 pairs) enters only as "within its CE/P0/P1 setting". Line 23's "Thus the gcds are…" is asserted, not derived.
- **Why it matters:** SHAPE's forward direction (lines 31–35) depends on it. For example, gcd(r_o, r_u) = 1 needs gcd(6r_o, 6r_u) = 6, which is what excludes a shared prime ≥ 7.
- **Second gap:** README:33 defines CE only for finite G, so for arbitrary G the class must be read as a condition on the index tuple.
- **Repair:** state the hypothesis as "the labelled index tuple satisfies README:94 including its gcd-matrix column. Equivalently, all pairwise gcds are ≤ 6, and then 4 | n_d, 12 | n_s, v_2(n_o) = 1 and 3∤n_d force exactly the displayed values."

**MINOR-3: `K52-W-v1.md:51`, with `:93`.**
- **Problem:** Sun(4) is restated without "subgroups not necessarily distinct".
- **Why it matters:** fibre pieces can be cosets of equal trace subgroups. For example, a = 1 and q_s = r_o = 1 give λ_s = λ_o = 3, and nothing forces U_s∩U_{d_1} ≠ U_o∩U_{d_1}.
- **Why it is only MINOR:** the accepted form covers this (README:11 "possibly equal"; written verdict :18 "equal subgroups allowed"). This is a precision fix only.
- **Repair:** append "(subgroups possibly equal; README line 11 form)" to line 51.

**MINOR-4: `K52-W-v1.md:52`, `:187`, `:189` (provenance and DAG).**
- **Problem 1:** lines 52 and 187 cite "INV(a),(b)". INV(b) literally includes the VFC identification q_j = α*_vj, which K52-W does not use; only the E7 inequality is used, and it is re-proved at lines 75–79.
  - **Repair:** replace with "INV(a) and the inequality α + α* ≤ g (erratum E7); VFC not used."
- **Problem 2:** line 189 lists the local table's dependencies as "SHAPE, A" only. The table also uses the index formula λ_j = n_jα/g from line 83.
  - **Repair:** add "index formula, line 83".

**Nits (not counted):**
- **n1:** notation clashes.
  - g_ij (a gcd) sits beside the coset representatives g_i, g_j and g_j* at `:63`, `:71` and `:74`.
  - `:140` reuses v for an O_4 vertex, while v is the apex at `:82`.
  - **Repair:** rename the vertices at `:140` to u, w, and add a one-line note that g_ij always means gcd(n_i, n_j).
- **n2:** the Sun(2) re-proof at `:92` is compressed.
  - **Repair:** cite Lemma A's divisibility applied inside U_v, and L0.2 at `:67`.
- **n3:** labels and terms.
  - "Shared markers" at `:128` is undefined.
  - The B1 row at `:160` labels as "U" the raised variant from `:136` (y_d = 1).
  - **Repair:** name that variant U′.

## Not checked

- Hashes, byte counts and manifest ranges. These are metadata, and the review used no tools.
- The content and attribution of Zhu Thm 1.1. It is treated as the accepted import.
- The full Sun(7) gate, KII and D2′. These are outside this claim, as lines 193–196 correctly state.
