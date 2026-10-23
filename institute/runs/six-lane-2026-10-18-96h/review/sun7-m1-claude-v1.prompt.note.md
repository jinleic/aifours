**VERDICT: ACCEPT-WITH-FIXES.** There are 0 FATAL, 0 MAJOR and 8 MINOR findings. Every implication checks out, and the fixes are editorial or import bookkeeping. The scope is exactly as stated: K7 with exactly one marked vertex z, e_z = 1, and markers ⊆ {3,5}. Sun(7), marked-2 K7, multi-marked K7, K6.2* and marked K6.3 are untouched. I reviewed the embedded text as given and did not recompute its hash (no tools).

## Findings

**FATAL:** none.
**MAJOR:** none.

**MINOR**
1. **Header, "Imports" line.**
   - R0 is invoked in the §3 statement ("by R0") but is not imported.
   - LFC (a) supplies the label formula in "Notation". LFC (c) supplies the hereditary allowed-set definition, including Sun(2) (E2). Only LFC (d) is listed.
   - "Same unique marked vertex" rests on erratum E6.
   - *Fix:* add "R0 (README §1); LFC (a),(c); erratum E2, E6".
2. **§1, "after capping".** This term is defined neither in the candidate nor in the embedded imports. *Fix:* "m_z is odd with prime divisors in {3,5}. Label gcds depend on m_z only through [3 | m_z] and [5 | m_z], because every α ≤ 5 (E1)." I verified below that nothing else about m_z enters.
3. **§2 (c), last sentence.**
   - ROW-U's *statement* does not apply at v ∈ U, because neighbour z is marked.
   - What is used is ROW-U's *proof*, under the hypothesis "all label gcds equal α-gcds, g = 6, α ≤ 5". This is declared in the imports and is valid; I checked it below.
   - *Fix:* add one sentence naming that abstract statement ("ROW-U°"), citing parent verdict item 3.
4. **§2 (b), first case.** "(y = 1/k3... = 1/min(3,k3))" is garbled. *Fix:* "(y = 1/k3 = 1/min(3,k3))".
5. **§2 (b), final case, feasibility sentence.**
   - "with 3-elements the gcd is 3" is false when 3 ∤ m_z and α_vz ∈ {4,5}; the gcd is then 1.
   - "twos (label 2)" should read label 2w_u.
   - This is harmless: the resulting list of sets containing z is a superset of the true allowed sets.
   - *Fix:* "is at most 3 (equal to 3 iff 3 | m_z α_vz)".
6. **§3 step (3), "Steps (1)-(3) apply verbatim … |A4*(v)| ≥ 3 for all v".**
   - For v = z this bound comes from step (0) (|F*| = 3), not from steps (1)-(3).
   - In the inverted run, F and F* swap roles, which needs α** = α (INV (a)).
   - *Fix:* "Steps (0)-(3) applied to the inverted configuration (α-matrix α*, inverse = original by INV (a), so its F, F* are our F*, F) give |A4*(v)| ≥ 3 for v ∈ U and |A4*(z)| = 3."
7. **§1/§3 notation.** U := V∖{z} collides with the subgroups U_v of LFC. *Fix:* rename it, e.g. W.
8. **§4 parenthetical.** "every configuration with a 2-marker survives … and is killed only after adding RPLP" reads as a universal claim, which probes cannot establish. It is not load-bearing. *Fix:* qualify it ("in the probed range") or delete it.

**Non-defect remark.**
- Step (0)'s sentence "For u in F*, α_zu ∈ {1,2}" is never used.
- Step (2) needs only |F| ≥ 3, since U3 ⊆ U∖F and |U∖F| ≤ 3.
- So INV is load-bearing only in steps (1) and (3).

## Independent re-derivation

### (1) Label gcds

In K7, g_ij = 6, so λ_j = m_j w_j α_vj with α ∈ {1,…,5}. The w's are pairwise coprime, prime to 30, and every α ≤ 5, so the w's never enter a gcd.

**At v ∈ U.** For two U-neighbours u, u', gcd(λ_u, λ_u') = gcd(α_vu, α_vu'). For z, gcd(λ_z, λ_u) = gcd(m_z α_vz, α_vu), where m_z is odd with prime support ⊆ {3,5}:

| α_vu | gcd(λ_z, λ_u) |
|---|---|
| 1 | 1 |
| 2 | 2 if α_vz ∈ {2,4}, else 1 |
| 4 | gcd(α_vz, 4) |
| 3 | 3 if 3 \| m_z or α_vz = 3, else 1 |
| 5 | 5 if 5 \| m_z or α_vz = 5, else 1 |

- The marker raises a gcd above the α-gcd only when α_vu ∈ {3,5} and the marker matches.
- In every case gcd(λ_z, λ_u) ≤ α_vu ≤ 5, so capping is harmless.
- Two U-neighbours from different classes (R1, R24, R3, R5) have gcd 1, which Sun(2) forbids in one fibre.
- Hence every allowed set is either T or {z} ∪ T, with T inside one class.
- R1 elements have gcd 1 with everything, including z, so they appear only as singletons.

**At z.** The labels are λ_u = w_u α_zu, so m_z never appears and all gcds are α-gcds. ROW-U applies verbatim, since its hypothesis concerns only the neighbours.

### (2) ROW-1

At v, LFC (d) gives Σ y_j α_vj < 6 for every feasible y.

**Reduction used whenever y_z = 0.** For an allowed T ∋ z, Σ_T y = Σ_{T∖z} y. The set T∖z is allowed (heredity) and lies inside one class. So the standard ROW-U weights stay feasible. I re-checked those weights:
- R24 allowed sets are singletons, pairs, and 3- or 4-sets with at most one two.
- R3 allowed sets have size ≤ 3; R5 allowed sets have size ≤ 5.

**(a) ✓.** Suppose 1 ≤ k5 ≤ 4.
- Put y = 1/k5 on R5. Since |R5| = k5, every allowed set has R5-sum ≤ 1.
- Use standard weights elsewhere and y_z = 0.
- The value is 5, plus at least 1 from some other nonempty class, so ≥ 6.

**(b) ✓.** If k3 ≥ 1 then k5 ≤ 4, so k5 = 0 by (a).
- **k3 ∈ {1,2}:** the value is 3 + min(5−k3, 4) ≥ 6 (E8).
- **Some U-entry equals 4** (y_z = 0 throughout):
  - k3 = 3, remainder {4,1}: 3 + 4 + 1.
  - k3 = 3, remainder {4,2}: 3 + (½·4 + ½·2) = 6.
  - k3 = 3, remainder {4,4}: 3 + 4.
  - k3 = 4, remainder {4}: 4 + 4.
  - k3 = 5 leaves no room for a 4.
- **α_vz ∈ {3,4,5}, remainder ⊆ {1,2} (at most two elements).** Weights: ⅓ on R3, 1 on ones, ½ on twos, ⅓ on z. Allowed sets containing z, by value of α_vz:
  - α_vz = 3: gcd 3 with threes, 1 with twos. Sets ⊆ {z}, {z,3}, {z,3,3}, with sums ⅓, ⅔, 1.
  - α_vz = 4: gcd 2 with twos; gcd 3 with threes iff 3 | m_z. The set {z,2,2} has all gcds 2 < 3, so it is not allowed. Sets ⊆ {z}, {z,2} (sum 5/6), {z,3}, {z,3,3}.
  - α_vz = 5: gcd 3 with threes iff 3 | m_z; gcd 1 with twos.
  - {z,3,3,3} is never allowed, since every pair has gcd ≤ 3 < 4. Any mixed set contains a gcd-1 pair.
  - Allowed sets without z: at most three 3s, {2,2}, or singletons; each sums to ≤ 1.
  - Each U-neighbour contributes exactly 1, so the value is 5 + α_vz/3 ≥ 6.

**(c) ✓.** The entries α_vu ∈ {1,2,4} are powers of 2, and m_z w_z is odd, so gcd(λ_z, λ_u) = gcd(α_vz, α_vu). All 15 label gcds are therefore α-gcds, with g = 6 and α_vz ≤ 5. ROW-U's proof uses nothing else: the class split, the allowed sets within each class, the weights, and the E8 value bound.

**Calibration (not a premise): ROW-1 is not over-claimed.** Two rows survive LFC at v:
- Row (3,3,3,1,1 | α_vz = 2) with 3 | m_z has LP optimum 17/3 < 6. The primal value is attained at t = s = ⅓, and the dual certificate puts 5/3 on {3,3,3} and ⅔ on each {z,3,3}.
- An all-5 U-block with 5 | m_z and α_vz ≤ 4 has optimum 5 + α_vz/5 < 6.

The global steps (2) and (1) are exactly what kill these two rows.

### (3) Theorem K7-M1

**(0) ✓.**
- By INV (a) and E6, the inverted configuration has the same labelled index tuple. It is therefore K7 with the same unique marked z and the same markers.
- ROW-U (iii) at z, applied to α and to α*, gives |F|, |F*| ≥ 3.
- INV (b) gives α + α* ≤ 6, so F ∩ F* = ∅. Hence |F| = |F*| = 3 and U = F ⊔ F*.

**(1) ✓.**
- α is symmetric. ROW-1 (a) at v makes v's whole U-row equal to 5.
- Each other u' then has k5 ≥ 1, hence k5 = 5. So α ≡ 5 on all 15 pairs inside U.
- On those pairs 1 ≤ α* ≤ 6 − 5, so α* ≡ 1.
- ROW-1 (c) for the inverted configuration at any v ∈ U then gives a row with five 1s, violating (ii) and (iii).
- Direct check: in the inverted configuration at v, the five U-labels w_u are pairwise coprime and coprime to λ*_z. So y ≡ 1 gives a value of 5 + α*_vz ≥ 6.

**(2) ✓.**
- U3 is closed under α = 3 adjacency.
- By ROW-1 (b), each member of U3 has at least three such neighbours, so |U3| ≥ 4.
- ROW-1 (b) also gives α_vz ∈ {1,2} on U3, so U3 ∩ F = ∅.
- Then |U3| ≤ |U∖F| = 3, a contradiction.

**(3) ✓.**
- All entries inside U lie in {1,2,4}. ROW-1 (c) gives |A4(v)| ≥ 3 for v ∈ U, and |A4(z)| = |F| = 3.
- The inverted run (same z, same markers) gives |A4*(v)| ≥ 3 for v ∈ U, and |A4*(z)| = |F*| = 3.
- Since 4 + 4 > 6, A4(v) and A4*(v) are disjoint, so every vertex has exactly 3 edges in the symmetric α = 4 graph.
- A 3-regular graph on 7 vertices has degree sum 21, which is odd. Contradiction.

**R0 lift ✓.** Class membership and marking are functions of the index tuple, which the core quotient preserves (parent verdict item 6).

### Requested missing-case audit

- **k3 = 3 remainders:**
  - {4,1}, {4,2}, {4,4} are killed with y_z = 0.
  - {1,1}, {1,2}, {2,2} are killed in the final case of (b).
  - 3 and 5 cannot appear in the remainder, since k3 = 3 exactly and k5 = 0.
- **k3 = 4 and k3 = 5:** for k3 = 4 the remainder is one entry in {1,2,4}, all covered; k3 = 5 leaves no remainder.
- **Values of α_vz:**
  - Each of 3, 4, 5 is handled separately in the final case of (b); α_vz ∈ {1,2} is that case's conclusion.
  - In (a) and the first two cases of (b), y_z = 0, so α_vz is irrelevant.
  - In (c), ROW-U's class analysis covers every α_vz ∈ {1,…,5}.
- **z-adjacency when α_vz = 4:**
  - gcd 2 with twos.
  - gcd 4 with fours; this arises only under (c), where it equals the α-gcd.
  - gcd 3 with threes iff 3 | m_z.
  - gcd 5 with fives iff 5 | m_z; this matters only in (a), where y_z = 0.
  - No gap.
- **k5 = 5 at v:** permitted by (a), and genuinely locally feasible when 5 | m_z. It is closed globally by step (1) via INV.
- **Mutation control:** with a 2-marker, ROW-1 (c) fails. For example, if 4 | m_z, α_vz = 1 and α_vu = 4, then gcd(λ_z, λ_u) = 4 ≠ 1. This is consistent with the stated exclusion.

**Scope.** Together with K7-M0, this excludes every K7 configuration with at most one marked vertex and no vertex with e ≥ 2. Everything listed as open stays open; exploratory probes are not premises. I make no novelty or significance assessment.
