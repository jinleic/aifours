# Referee report: K7-D23-NO4-v1

Scope of this review:
- I reviewed the embedded text only. I could not check the SHA because I have no tools.
- Line references are approximate. L1 is the title line of the embedded candidate, and blank lines are counted.
- Every step was re-derived against the embedded accepted sources, at their stated scopes.

## Verdicts

- **(A) Claim D23-CENTER: ACCEPT-WITH-FIXES.** 0 FATAL, 0 MAJOR, 5 MINOR.
  - The proof is correct as written for every allowed 5-marker placement and for unbounded exponents.
  - All fixes are wording or citation changes. No statement changes.
- **(B) Claim D23-MIX: ACCEPT-WITH-FIXES.** 0 FATAL, 0 MAJOR, 8 MINOR, plus 1 general MINOR in §4.
  - The row dichotomy is correct, and so are the 3/4 and 4/3 exclusions.
  - All fixes are wording or citation changes. No statement changes.
- No step needs more than the imports provide at their stated scopes. Two citations should name the exact accepted scope they rely on (A-4 and B-1).

---

## Attack-point checks

### 1. C1 (CENTER cross triangle)

Set-up for the triangle {z,a,b} with a ∈ F\*, b ∈ F:
- The α-values are (α_za, α_zb, α_ab) = (s, 4, x).
- All g and γ equal 6, ℓ_z = r_z, and ℓ_a, ℓ_b are odd.
- τ_min = lcm(s/gcd(s,ℓ_b), 4/gcd(4,ℓ_a), x/gcd(x,r_z)) = lcm(4, x/gcd(x,r_z)).
- τ_max = min(xs, 4·min(s,x), s·min(4,x)), taking apexes z, a, b in that order.

| x | x/gcd(x,r_z) | τ_min | τ_max (s=1) | τ_max (s=2) | survives at s=1 | survives at s=2 |
|---|---|---|---|---|---|---|
| 1 | 1 | 4 | 1 | 2 | no | no |
| 2 | 1 | 4 | 2 | 4 | no | yes (τ=4) |
| 3 | 3 (3∤r_z) | 12 | 3 | 6 | no | no |
| 4 | 2 if E=1; 1 if E≥2 | 4 | 4 | 8 | yes | yes |
| 5 | 5 if Bz=0; 1 if Bz≥1 | 20 or 4 | 4 | 8 | no / yes | no / yes |

- **Marker invariance.** The terms that depend on ℓ_a or ℓ_b have numerators s and 4, or 4 and s\* in the inverse triangle.
  - These numerators are powers of 2 and ℓ_a, ℓ_b are odd, so the terms are unchanged when a or b is t (3^A5^Bt) or a 5-marked p.
  - τ_max contains no ℓ at all, and the x-term depends only on r_z. Confirmed.
- **INV kills.**
  - x=5 forces x\*=1. The inverse triangle (4, s\*_b, 1) then has τ\*_min = 4 > τ\*_max = s\*_b ≤ 2, so it dies.
  - x\*=5 forces x=1, which dies in the table above.
  - Hence x, x\* ∈ {2,4} and (x, x\*) ≠ (4,4). The s=1 lines give x=4, and the s\*=1 lines give x\*=4. Confirmed.
- **F7 instances.** The rule is τ_min·g_za ≥ γ_z·α_ab·α_za, at apex z.
  - Original, pair (a,b): 24 ≥ 6xs, i.e. xs ≤ 4. This gives X_a ⊆ X_b (measure s/6 inside 4/6). It holds at (s,x) = (2,2) and (1,4) and fails at (2,4).
  - The reverse orientation (b,a) would need 24 ≥ 24x, i.e. x ≤ 1. It never applies and is never used.
  - Inverse, pair (b,a): τ\*_min = 4 and the test x\*s\*_b ≤ 4 gives X\*_b ⊆ X\*_a.
  - Every use in C3 is the (2,2) instance. Confirmed.

### 2. C2 (VFC facts at z)

- **Local index.** d_j = q_j n_j/6 = α\*_zj r_j, using q = α\* from INV(b).
- **gcd reduction.** No odd prime divides two of the r_j, since they are pairwise coprime, and α\* is a power of 2. So gcd(d_j,d_k) = 2^min(v₂α\*_zj, v₂α\*_zk) = gcd(α\*_zj, α\*_zk). This holds when t or a 5-marked p is involved.
- **Sun(3) triple prohibition.** For a ∈ F\* and b ≠ b' ∈ F, the gcds are s\*_b, s\*_b' and gcd(s\*_b, s\*_b'), all ≤ 2 < 3. So {a,b,b'} is not allowed. Confirmed.
- **Sun(2) singleton rule.** If α\*_zj = 1, then d_j = r_j, which is coprime to every other d. So any S_R containing j equals {j}. Confirmed.
- **V4.** The union of the D_j lies in G∖U_z, so μ(∪D_j) ≤ 1−1/n_z. Confirmed.
- **Inverse versions.** d\*_j = α_zj r_j with α ∈ {1,2,4}. {b,a,a'} is forbidden for b ∈ F and a ≠ a' ∈ F\*, and the Sun(2) rule applies at α_za = 1. Confirmed.

### 3. C3 (the four types)

- **Exhaustiveness.** The types split on whether an a₀ with s_a₀ = 1 exists and whether a b₀ with s\*_b₀ = 1 exists. That is exhaustive. Confirmed.
- **Only b₀ exists.**
  - Here s_a = 2 for every a ∈ F\*. Since s\*_b₀ = 1, x\* = 4, so x = 2.
  - F7 at (2,2) gives X_a ⊆ X_b₀. Then D_b₀ ⊆ Y_b₀ ⊆ Y_a = D_a, because za is tight (2+4).
  - D_b₀ has measure 1/6, so it contains a right coset R. That R has {a,b₀} ⊆ S_R, contradicting the Sun(2) rule. Confirmed.
- **Only a₀ exists.** This is correct via the inverted configuration, but the role map is not written out (see A-3).
- **Neither exists.**
  - All six z-edges are tight.
  - For an "in" b, F7 at (2,2) gives D_b = Y_b ⊆ Y_a = D_a.
  - If D_b ∩ D_b' were nonempty, some right coset R would have {a,b,b'} ⊆ S_R, which C2 forbids.
  - If at most one b were "out", the three D_b would be pairwise disjoint with measure 2/6 each. Their union would have measure 1, contradicting V4.
  - So at least two b satisfy α_ab = 4 for every a, and by inversion at least two a satisfy α\*_ab = 4 for every b.
  - Their crossing edge has (4,4), which contradicts INV. Confirmed.

### 4. Section 2 (row dichotomy)

ROW-1-deg holds at z, so ROW-1 applies there. Its ingredients:
- g_zj = 6 for all six neighbours.
- Each W-label is w_u·α_zu, with the w_u pairwise coprime and prime to 30.
- The t-label is m_t·w_t·α_zt, with m_t = 3^A5^Bt odd and {3,5}-smooth, and w_t prime to 30 and to every w_u.
- LFC(d) holds at z. z's own index never enters.

Which import covers which part:
- Z2-erratum G2 states this transfer for a general odd {3,5}-smooth m. Its accepted instance was m = 5^h.
- The 3-part of m is covered by the M1 acceptance (erratum F2/F5).
- The composition is therefore within scope (B-1).

What ROW-1 gives (k5 and k3 count W-neighbours only):
- **(a)** k5 ∈ {0,5}.
- **(b)** If k3 ≥ 1, then k3 ≥ 3, no W-entry lies in {4,5}, and α_zt ∈ {1,2}.
  - Because 3 | m_t, the gcd of λ_t with a three-label is exactly 3 (the equality case of F5).
  - The listed sets {t}, {t,x}, {t,3,3} still contain every allowed set through t.
  - The weights (1/3, 1, 1/2, y_t = 1/3) give 5 + α_zt/3 ≥ 6 whenever α_zt ≥ 3.
  - Nothing more: (b) gives no bound on the number of 1s. The "3-type" definition (L111) records exactly this.
- **(c)** If all W-entries lie in {1,2,4}, then for every α_zt ≤ 5, gcd(w_uα_zu, m_tw_tα_zt) = gcd(α_zu, α_zt).
  - So ROW-U-deg holds on all 15 label pairs, and ROW-U's proof applies to all six entries, t included.
  - It gives entries in {1,2,4}, at most one 1, and at least three 4s. That is exactly "4-type" as defined at L19.
  - For example, α_zt = 3 or 5 isolates t with value 3 or 5, against at least 4 from the five other neighbours.
  - **Yes, (c) yields the full six-entry 4-type row.**

**The k5 = 5 kill.**
- INV gives α\*_zu = 1 on W.
- The inverse labels are w_u for u ∈ W and 3^A5^Bt·w_t·α\*_zt for t. All 15 gcds are 1 in each sub-case:
  - 5-marker absent: Bt = 0.
  - 5-marker on z: r_z never enters labels at apex z.
  - 5-marker on t: 5^Bt is coprime to every w_u.
- So y ≡ 1 is feasible, with value 5 + α\*_zt ≥ 6. This contradicts LFC(d) of the inverted configuration. Confirmed.
- The α\*-version is killed by LFC(d) of the original configuration, since α\*\* = α.

The dichotomy is exhaustive and the two types are disjoint.

### 5. Section 3 (the 3/4 exclusion)

**|T| = 3.** T contains no α\*-entry 4 (since 3+4 > 6), and the α\*-row needs at least three 4s among at most 6−|T| positions. So |T| = 3, every entry in P ∪ {t} has α\* = 4, and q_a ∈ {1,2}. Confirmed.

**α-triangle (3, s_p, x), with a, p ∈ W:**
- τ_min = lcm(3, s_p, x/gcd(x,r_z)).
- τ_max = min(xs_p, s_p·min(3,x), 3·min(s_p,x)).

| x | τ_min / τ_max (s_p = 1) | τ_min / τ_max (s_p = 2) |
|---|---|---|
| 1 | 3 / 1: dies | 6 / 2: dies |
| 2 | 3 / 2: dies | 6 / 4: dies |
| 3 | 3 / 3: survives | 6 / 6: survives |
| 4 | 6 (E=1) or 3 (E≥2) / 3: dies or survives | 6 / 6: survives |
| 5 | 15, or 3 if Bz≥1 / 3: dies or survives | 30, or 6 if Bz≥1 / 6: dies or survives |

- The survivors lie in {3,4,5}, as claimed. The exact list is a proper subset, which is harmless.

**Inverse triangle (q_a, 4, x\*).**
- It has the same shape as C1: the small entry at a, 4 at p, odd ℓ_a and ℓ_p, and 3 ∤ r_z.
- So x\* ∈ {2,4} ∪ {5 if Bz ≥ 1} when q_a = 2, and x\* ∈ {4} ∪ {5 if Bz ≥ 1} when q_a = 1.

**INV step.**
- x\* = 5 forces x = 1, which is dead. x = 5 forces x\* = 1, which is dead because τ\*_max = q_a < 4.
- So x ∈ {3,4}, x\* ∈ {2,4}, and x + x\* ≤ 6 forces x\* = 2. Then q_a = 2. Confirmed.

**F7 (inverse, pair (a,p), apex z).** τ\*_min = lcm(2, 4, 2/gcd(2,r_z)) = 4, and 24 ≥ 6·2·2. So X\*_a ⊆ X\*_p (measure 2/6 inside 4/6). Confirmed.

**M2 bookkeeping.**
- μ(Y\*_a) = 4/6, μ(D\*_a) = 3/6, and D\*_a ⊆ Y\*_a.
- D\*_p ⊆ Y\*_p ⊆ Y\*_a, with μ(D\*_p) = s_p/6.
- d\*_a = 3w_a and d\*_p = s_p·w_p have gcd 1, so D\*_a and D\*_p are disjoint (Sun(2) plus the right-coset decomposition).
- Hence D\*_p lies in Y\*_a∖D\*_a, which has measure 1/6.
- If s_p = 2, then 2/6 > 1/6: contradiction.
- If s_p1 = s_p2 = 1, then w_p1 and w_p2 are coprime, so D\*_p1 and D\*_p2 are disjoint, giving 2/6 > 1/6: contradiction.
- The 4/3 combination follows by inversion, and 4/4 follows from CENTER. Confirmed.

### 6. Scope and the arbitrary-group lift

**CENTER.**
- It does not use that W is unmarked or that Bt = 0.
- Hypotheses that are load-bearing:
  - r_j is odd for every j ≠ z. This is used in the C1 compulsory terms and the C2 gcds.
  - 3 ∤ r_z. This is used only in the x = 3 kill; if 3 | r_z, the case (s,x) = (2,3) would survive with τ_min = 4 ≤ 6.
- A 5-marker on z only revives x = 5, which INV removes. A 5-marker on t or on p ∈ W changes no term or gcd, because α\* ∈ {1,2,4}.

**MIX.**
- Nothing outside "W unmarked" is excluded silently. That restriction is load-bearing only in §2.
- M1 and M2 correctly avoid t. For t, 3/gcd(3,ℓ_t) = 1 and gcd(d\*_t, d\*_a) = 3, so neither M1 nor M2 would transfer to t. |P| = 2 is exactly enough.

**R0 lift.**
- N = ∩core(U_i) is normal of finite index and lies in every conjugate of every U_i.
- So the indices of U_i∩U_j, the indices of g_iU_ig_i⁻¹ ∩ g_jU_jg_j⁻¹, and coset disjointness are all preserved.
- Therefore α, α\*, the markers and both row types are the same in G/N.
- The lift is valid for both claims, but it is stated only for CENTER (A-5, B-8).

---

## Findings

**FATAL: none. MAJOR: none.**

### MINOR, Claim (A) CENTER

**A-1** (§1 C2, ≈L80–81)
- Defect: the gcd reduction is justified by "only disjoint 3/5 marker powers". That wording does not exclude a common w-prime.
- Repair: write "the r_j (j≠z) are odd and pairwise coprime (K7), and α\*_zj ∈ {1,2,4}; hence no odd prime divides two of the d_j, and gcd(d_j,d_k) = 2^min(v₂α\*_zj, v₂α\*_zk)".

**A-2** (§1 C1, ≈L68–71)
- Defect: x ∈ {2,4} survival and the s = 1 line rest on τ_max values that are never written; for example, x = 2 at s = 1 has τ_max = 2 < 4. The sentence "This also rules out x\*=5" is unargued.
- Repair:
  - Insert the table above, with the E=1 / E≥2 and Bz=0 / Bz≥1 splits.
  - Add: "x\*=5 forces x=1, which dies in the original table."

**A-3** (§1 C3, ≈L89–91 and L95–96)
- Defect: the inversions say "same argument" without giving the role map.
- Repair, in the style of Z2-erratum G9: "The inverted configuration has the same indices (INV(a), E6) and z-rows (α\*, α\*\* = α), both 4-type. Its F, F\*, s, s\* are our F\*, F, s\*, s. a₀ plays the role of b₀. C1–C2 hold for it verbatim."

**A-4** (§0 imports, ≈L43–48)
- Defect: the Z2 parent verdict *inherits* the "accepted ... general T/VFC/F7 rules". It is not their acceptance record; Z2's own import list names written verdict 73a25ba6… for L1, VFC and F7. The candidate also applies L1 and F7 to the inverted configuration without a citation for that.
- Repair:
  - Cite 73a25ba6… as the acceptance of L1, VFC(V1)–(V4) and F7, and the Z2 verdict as confirmation.
  - Cite Z2-erratum G5 for applying L1 and F7 to the inverted configuration.

**A-5** (≈L99)
- Defect: "R0 gives arbitrary groups" does not say why α\* survives the quotient.
- Repair: add "N lies in every conjugate of every U_i, so the inverted-configuration indices, and hence α\*, are preserved (LFC parent verdict, item 6)."

### MINOR, Claim (B) MIX

**B-1** (§2, ≈L103–105)
- Defect: the step "exactly the transfer accepted in G2" mixes two scopes. G2 supplies apex-independence, and its accepted instance was m = 5^h. The 3-sensitive step (the last case of ROW-1(b)) is covered by M1 erratum F2/F5.
- Repair:
  - Cite G2 together with M1-F2/F5, noting that 3 | m_t makes the gcd with a three-label exactly 3 and the listed sets still contain all allowed sets.
  - List the ROW-1-deg hypotheses explicitly, including that w_t is prime to 30 and to each w_u.

**B-2** (§2, ≈L113)
- Defect: "its five entries are {1,2,4}; ROW-1(c) gives a 4-type full row" is imprecise.
- Repair: "its five W-entries lie in {1,2,4} (k5 = k3 = 0). By ROW-1(c) and F3, gcd(w_uα_zu, m_tw_tα_zt) = gcd(α_zu, α_zt) for every α_zt ≤ 5. So all six entries, including α_zt, lie in {1,2,4}, with at most one 1 and at least three 4s."

**B-3** (§2, ≈L113–114)
- Defect: "the same dichotomy for α\*" relies on unstated facts.
- Repair: add "The α\*-version of the k5 = 5 kill uses LFC(d) of the original configuration, since α\*\* = α. The inverted configuration has W unmarked by E6."

**B-4** (§3, ≈L120 onward)
- Defect: P = {p1, p2} reuses the symbol p, which §0 reserves for a 5-marked third vertex. That vertex cannot occur under MIX, so the clash is notational only.
- Repair: rename P (for example Q = {u1, u2}), or add "(p ∈ W is unmarked here)".

**B-5** (§3 M1, ≈L134–135)
- Defect: "x\*=4 when q_a=1" is false before x\* = 5 is removed when Bz ≥ 1.
- Repair: write "x\* ∈ {4,5} when q_a = 1". The conclusion q_a = 2 then follows after the INV step, as already written.

**B-6** (§3 M1, ≈L133)
- Defect: the survivor list {3,4,5} is given without a table.
- Repair: add the (3, s_p, x) table. Optionally note that x = 4 also dies when s_p = 1 and E = 1.

**B-7** (§3 M2, ≈L141–150)
- Defect: three facts are used but not stated:
  - D\*_a ⊆ Y\*_a, which is VFC(V1) for the inverted configuration.
  - μ(D\*_j) = α_zj/6, which is INV(b) for the inverted configuration together with α\*\* = α.
  - With g_z = 1, g\*_z = 1 automatically, and X\*_j does not depend on the normalisation.
- Repair: state these three facts in the first sentence of M2.

**B-8** (end of §3, ≈L154)
- Defect: MIX has no arbitrary-group lift.
- Repair: add "By R0 (with α\* preserved, as for CENTER), D23-MIX holds for arbitrary groups."

### MINOR, general (§4)

**G-1** (§4, ≈L165–166)
- Defect: "K7-D23-obstruction-v1.md is a precise obstruction" is an unproved claim about an unreviewed artifact.
- Repair: mark it "(unreviewed; navigation only; not a claim of this file)", or delete it.

### Non-defect remarks (no change requested)

- E ≥ 1 is never load-bearing in C1: for x ∈ {2,4}, x/gcd(x,r_z) divides 4 for every r_z.
- "At most one 1" (L19, L58) is not used anywhere in CENTER.
- MIX's restriction to unmarked W is mandatory only because of §2, which needs exactly one marked neighbour. M1–M2 would survive a 5-marker on a or p, but the file correctly does not claim this.
