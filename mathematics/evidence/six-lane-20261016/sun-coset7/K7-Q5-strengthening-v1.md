# K7-Q5-strengthening-v1: the family Q5 is empty for every |U| (a written candidate)

- **Freeze record:** host-clock time and sha256 in `evidence/k7-q5-strengthening-v1.sha256`.
- **Status:** a single written candidate, permitted by the parent, to be reviewed only if time allows. It is unreviewed and not a premise. No computation was run. K7 stays OPEN.
- **Origin:** the argument follows the sketch in the Claude review of K7-structure-v1, `review/sun-coset7-k7-structure-claude-v1.note.md` (4c794266…e476e), lines 104–113, which that review explicitly labels as not accepted. This file writes it out in full.
- **Imports, all accepted at written scope:**
  - From `review/sun-coset7-k7-structure-parent-verdict-v1.md` (2154c317…0059): K7-TRI, K7-U, K7-Q in the X1 convention, and K7-Q5 for |U| ≥ 5. These come from `K7-structure-v1.md` (f4534c07…9fc1) with `K7-structure-erratum-v1.md` (f8642cb6…7138) and the parent overlay.
  - From `review/sun-coset7-written-parent-verdict-v1.md` (73a25ba6…9f35): Corollary VFC-count and VFC (V1).
- **Notation (per the parent overlay):**
  - n_i = 2^{e_i}3^{f_i}5^{h_i}w_i.
  - δ_v(r) := 2^{min(e_v−1, v_2 r)}·3^{min(f_v−1, v_3 r)}·5^{min(h_v, v_5 r)} is the triangle relaxation function, called d_v(r) in K7-structure-v1.
  - d_j denotes only the VFC local index, d_j = q_j·n_j/6.
  - m_z := 2^{e_z−1}3^{f_z−1}5^{h_z}, so n_z = 6·m_z·w_z.

## Lemma K7-Q5⁺ [NEW candidate]

If a K7 configuration has quotient family Q5, then |U| ≥ 5, and K7-Q5 then excludes it. So **no K7 configuration of family Q5 exists**, for any number of marked vertices.

### Step 1: a vertex without marker 5 has α = 5 to every unmarked vertex

Assume Q5: every pair in U has α = 5. Let z ∈ M carry no marker 5, and take any v ≠ v′ in U (|U| ≥ 4).

1. **The triangle {v, v′, z} behaves like an all-unmarked triangle.**
   - **Apex z:** its opposite edge vv′ has r = 5. Since z has h_z = 0, δ_z(5) = 1, so the τ_min term of vv′ is 5 and the grid at z is 1/6.
   - **Apexes v and v′:** these are unmarked, so δ ≡ 1, and the edges vz and v′z enter τ_min unreduced.
   - **Conclusion:** by K7-TRI, the T and Ppair conditions of this triangle coincide with those of an all-unmarked triangle with the same three α values.
2. **Its type must be (5,5,5).** K7-U says the only surviving type that contains a 5 is (5,5,5). Hence α_vz = α_v′z = 5.
3. **Consequence for VFC at v.** VFC (V1) at v gives q_{v→z} ≤ 6 − 5 = 1, so q_{v→z} = 1 and d_z = m_z w_z.

### Step 2: the case |U| = 4 is impossible

If |U| = 4, then |M| = 3. The three markers 2, 3, 5 each sit on their own vertex: z_2, z_3, z_5. Fix v ∈ U and apply VFC-count at v, for every admissible q.

**Local indices at v.**

| neighbour | q at v | local index d |
|---|---|---|
| each of the three unmarked v′ | 1 (Q5 and V1) | w_v′ |
| z_2 | 1 (Step 1) | m_{z_2} w_{z_2} = 2^{e−1}w |
| z_3 | 1 (Step 1) | m_{z_3} w_{z_3} = 3^{f−1}w |
| z_5 | q_5 ∈ {1, …, 6 − α_{vz_5}} | q_5·5^{h}·w_{z_5} |

**Which sets are allowed.** The w-parts are pairwise coprime and coprime to 30, and q ≤ 5. So:
- an unmarked neighbour has gcd 1 with every other neighbour, and lies in no allowed set of size ≥ 2;
- gcd(d_{z_2}, d_{z_3}) = 1, so {z_2, z_3} is not allowed, and neither is {z_2, z_3, z_5}, since allowed sets are hereditary;
- {z_2, z_5} is allowed iff gcd(2^{e−1}, q_5) ≥ 2, i.e. iff q_5 is even;
- {z_3, z_5} is allowed iff gcd(3^{f−1}, q_5) ≥ 2, i.e. iff 3 divides q_5.

**Weights.** In each case below, every allowed set has total weight ≤ 1.

| case | weights | Σ y_j q_j/6 |
|---|---|---|
| q_5 = 1 | No pair is allowed. y ≡ 1. | 6/6 = 1 |
| q_5 ≥ 2, neither pair allowed | y ≡ 1 | (5 + q_5)/6 > 1 |
| q_5 ≥ 2, exactly one pair allowed | Both pairs would need 6 ∣ q_5, which is impossible for q_5 ≤ 5. Put weight 0 on the partner of z_5 in the allowed pair, and weight 1 on everything else. The only allowed set with two positive weights would be that pair, which now sums to 1. | (3 + 1 + q_5)/6 ≥ 6/6 = 1 |

In every case some feasible y has Σ ≥ 1. This contradicts VFC-count, which requires Σ < 1, for every admissible q-vector at v. ∎

### Conclusion

- **|U| ≥ 5:** K7-Q5 (accepted) excludes Q5.
- **|U| = 4:** excluded by Step 2. Here |U| = 4 forces |M| = 3, one vertex per marker.
- **Hence Q5 is empty in K7.**
- **Effect if accepted:** in K7-COV with X1–X3, the family Q5 can be dropped from the reduced data. Q23 and Q24 would remain.

## Not claimed

- No exclusion of K7.
- No result for Q23 or Q24.
- No computation. Every check here is by hand.
