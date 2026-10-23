# Hostile audit of SOURCE00 (K7-structure-v1), written mathematics only

Every check below was done by hand. No computation was run.

## Verdicts

| Claim | Verdict | Worst finding |
|---|---|---|
| K7-TRI | ACCEPT-WITH-FIXES | MINOR |
| K7-U | ACCEPT-WITH-FIXES | MINOR |
| K7-TWIN | ACCEPT | — |
| K7-Q | ACCEPT-WITH-FIXES | MINOR |
| K7-Q5 | ACCEPT-WITH-FIXES | MINOR |
| K7-COV | ACCEPT-WITH-FIXES | **MAJOR** |

- There is no FATAL finding.
- These verdicts cover written statements only. K7 stays OPEN.
- Nothing computational, nothing using FH, and nothing from §7 is accepted.

## K7-TRI (SOURCE00:35–62)

**What I checked.**
- γ = lcm(6,6) = 6 (SOURCE02:11), so ℓ_v = n_v/6. For r ≤ 5, gcd(r, w_v) = 1, hence gcd(r, ℓ_v) = d_v(r).
- τ_max: the apex terms are ca, ba and ab, so the minimum is ab.
- The P-grid: v_p gcd(n_v, lcm(n_j,n_k)·r_v) = min(v_p n_v, max(v_p n_j, v_p n_k) + v_p r_v).
  - Each prime has at most one carrier, so this is 1 + min(ε_p(v), v_p r_v) for p = 2, 3, and min(ε_5(v), v_5 r_v) for p = 5.
  - The w-parts contribute 0.
  - Hence gcd(n_v, I_jk) = 6·d_v(r_v), as claimed.
- The K2 condition r_k + r_v < 6 matches SOURCE03:49. K2 is L2/L3 at j with S = {v, k}.
- The floor in hi is exact.

**Probes (all consistent).**

| Marking | r_v | gcd(n_v, I_jk) |
|---|---|---|
| ε_2(v) = 1 | 4 | 12 = 6·2 |
| ε_2(v) = 3 | 4 | 24 = 6·4 |
| v carries markers {2, 5} | 5 | 30 = 6·5 |
| only j carries marker 2 | any | 6 |

The claim also extends to the K1/F7 forced test. With g = γ = 6 it reduces to τ_min ≥ α_ab·α_va (SOURCE03:58).

**Findings.**
- MINOR, SOURCE00:14, 18, 21, 25: the 5-valuation is written g_i. This breaks mandatory overlay A-1 (SOURCE06:46) and clashes with "g = 6" at SOURCE00:53. Fix: rename it h_i, and cite the SOURCE06 overlay at SOURCE00:6.
- MINOR, SOURCE00:45: u_v depends on the triangle through r_v. Fix: write u_{v;jk}.
- MINOR, SOURCE00:29 versus SOURCE00:166–167: d_v(r) collides with the VFC local index d_j (SOURCE02:42). Fix: rename one of them.

## K7-U (SOURCE00:64–94)

**What I checked.**
- Of the 35 multisets, exactly the 16 listed pass T and the other 19 fail.
- In each of the five killed types, τ_min = pq and lo = p/6 > hi = (p−1)/6, as tabled.
- All 33 apex checks for the 11 surviving types pass. Several are tight (lo = hi):
  - (2,2,4) at the apex opposite 4: 1/6 = 1/6, with K2 barring because 2 + 4 = 6.
  - (2,4,4) at the apex opposite 4: 1/6 = 1/6.
  - (5,5,5): 4/6 = 4/6.

**Findings.**
- MINOR, SOURCE00:10: the claim that the cut is "not by K" is wrong.
  - K1 together with L2/L3 kills the same five types. In (p,q,q), take α_iv = p and α_vj = α_ij = q.
  - Then τ_min = pq satisfies 6τ_min ≥ 6·α_vj·α_iv (SOURCE02:27), so the pair condition is forced.
  - L2/L3 then needs (p+q)/6 < 1, but p + q ≥ 6 (SOURCE02:26).
  - Both rules are active (SOURCE06:23). Fix: write "Ppair, equivalently K1+K2".
- MINOR, SOURCE00:78–80: the rows a = 3, 4, 5 give no reasons. Fix: list the failing inequalities, for example (3,3,4): 12 > 9.

## K7-TWIN (SOURCE00:96–129)

Parts (a)–(d) and both consequences hold, including when z is marked.
- The only τ_min term that z can relax is the one for edge xy, and 1/d_z(1) = 1.
- In (c), u_x = 1/6 and τ_min = 5 whatever z's markers are.
- (d) is the L4 equality argument. Equivalently, it is F7 with τ_min = b ≥ 1·b.

**Probes.**
- z with marker 2, α_xz = 2, α_yz = 4: τ_min = 4 > τ_max = 2, so the pattern is killed.
- z with marker 5 and α = 5 to both twins: hi = 0 < lo = 1/6, so it is killed.

**Cosmetic.** SOURCE00:124 should read lcm(b, b, 1).

## K7-Q (SOURCE00:131–158)

The following are correct:
- the seven inter-block types;
- the propagation of a 5;
- the forced (2,2,3);
- transitivity of β = 2 in Q23.

A 4-edge touching s or t is excluded first, by the step "s, t have no 4-edges".

**Findings.**
- MINOR, SOURCE00:133 versus SOURCE00:139: "Exactly one" contradicts the overlap the text itself states. Fix: write "at least one", and add that Q5 is disjoint from both other families and that Q23 ∩ Q24 is exactly "all β = 2", including b = 1.
- MINOR, SOURCE00:136: "β = 2 is an equivalence relation" needs "β = 2 or equal blocks".
- MINOR, notation: b, x and y are reused for the block count, a type entry and block names.

## K7-Q5 (SOURCE00:160–185)

The lemma is correct for |U| ≥ 5.
- V1 gives q_j ≤ 6 − 5 = 1.
- d_j = w_j is coprime to every other local index, so {j, x} fails the |T′| = 2 test (Sun(2) in U_v).
- Every y used is feasible, and the totals are 1, ≥ 1 and ≥ 1.
- In the |U| = 5 case where {z, z′} is allowed, q_z = q_z′ = 1 would indeed give gcd 1, so the larger q is ≥ 2.

**Findings.**
- MINOR, SOURCE00:185: the example q-vector (2,2,1) is not admissible.
  - In Q5, take z ∈ M without marker 5, and v, v′ ∈ U.
  - In the triangle {v, v′, z}, d_z(5) = 1 and u_z = 1/6, so it is exactly an all-unmarked triangle.
  - K7-U then forces type (5,5,5), so α_vz = 5 and q_z = 1.
  - When |U| = 4 this applies to the marker-3 vertex, so its q is 1, not 2.
  - Fix: delete or replace the example.
- A possible strengthening. This is my own derivation, it is not accepted here, and it needs its own frozen text and review.
  - The same fact gives q_{z2} = q_{z3} = 1, so {z2, z3} is never allowed.
  - If q_{z5} = 1, every neighbour is alone and Σ = 1.
  - Otherwise 6 does not divide q_{z5}, so at most one of z2, z3 can be allowed together with z5. Give that one weight 0; then Σ ≥ (3 + 1 + q_{z5})/6 ≥ 1.
  - This would remove Q5 entirely. Until it is reviewed, |U| = 4 stays in the family.
- Cosmetic, SOURCE00:162: state the claim conditionally ("if a Q5 configuration exists, then |U| = 4").

## K7-COV (SOURCE00:187–223)

The following are correct:
- the lifting in (ii);
- the stabiliser Sym(U) × id_M, because distinct marked vertices have disjoint, nonempty marker sets;
- the orbit criterion using size-preserving bijections of blocks;
- the argument for (v), which explicitly uses VFC.

The relaxation example also checks out.
- T: τ_min = lcm(2,1,2) = 2 ≤ 2.
- Apex z: u = 1/12, lo = 1/12, hi = 1/6; K2 allows X_x ⊆ X_y because 1 + 4 < 6.
- Apex x: lo = hi = 1/6.
- Apex y: lo = hi = 2/6.

**Findings.**
- **MAJOR, SOURCE00:189, 193, 205: quantifier/scope error.**
  - (i) quantifies over patterns that pass only T and Ppair, yet item 3 restricts Q5 to |U| = 4, which needs VFC.
  - (iv) says the reduction "removes nothing that T and Ppair keep".
  - Counterexample: M = ∅ with all 21 α = 5. Every triangle is (5,5,5).
    - T holds: 5 ≤ 25.
    - Ppair holds: lo = hi = 4/6.
    - F7 forces nothing: it would need 30 ≥ 150.
  - So this pattern passes T and Ppair but is not a lift of the data in (i).
  - Fix:
    1. List Q5 for every |U| in (i).
    2. In (v), apply K7-Q5 as an explicit VFC-LP pruning that holds for every q.
    3. Amend (iv) to read "T, Ppair and the VFC kill of K7-Q5".
    4. State that (v) depends on K7-Q5 being accepted.
- MINOR, SOURCE00:205: "the d-relaxed conditions" cover triangle quantities only. VFC and RPLP use local indices q_j·m_j·w_j with the full capped m_j (SOURCE02:42, 75). Fix: say so explicitly.
- MINOR, SOURCE00:215–217: the first bullet is false for a triangle with two marked vertices, and the all-marked triangle (|M| = 3) is not covered. Fix: restate per vertex, "each edge opposite a marked vertex is relaxed, and each marked apex refines its grid".
- MINOR, SOURCE00:199, 203: labelled data lift to exactly one pattern, so "up to Sym(U)" is unnecessary. The orbit "iff" also needs identical marking data and a fixed convention for the Q23/Q24 overlap (SOURCE00:139).
- MINOR (process), SOURCE00:207: this representation replaces the tree and node-certificate format of SOURCE05:33. Under F-4 (SOURCE06:54), no K7 run is credited without a separately frozen K7 format and parent permission.
- MINOR, SOURCE00:8: L6 is used in §7, not §6.

## Unverified

- The hashes and freeze records (SOURCE00:3).
- Every check in this audit is by hand and none is machine-checked: the 33 apex checks, the relaxation example and the Q5 LP bounds.
- Whether any lifted Q23, Q24 or Q5 (|U| = 4) pattern survives star-K, Bonferroni, VFC at marked vertices or RPLP. This is unknown, so K7 remains OPEN.
- §7 and FH were not audited for acceptance.
- The proposed strengthening of K7-Q5 to |U| = 4 is an unaccepted proposal.
