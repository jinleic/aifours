# Static assessment: Sun's disjoint-coset conjecture at k = 6 (no runs)

- **Written:** 2026-10-18, starting 10:22 PDT by the host clock. The freeze time is recorded in `evidence/k6-assessment-v1.sha256`.
- **Scope:** desk analysis only. No search or enumeration was run. This is for the parent's transition decision.
- **Labels:** statements marked [PROVED-HERE] carry a short written proof below. They are unreviewed. Estimates are marked [INFERENCE].

## 1. Exact target

**Sun(6).** Let a_1G_1, …, a_6G_6 be pairwise disjoint left cosets of finite-index subgroups of a group G. Then gcd([G:G_i], [G:G_j]) ≥ 6 for some i < j.

- **Source:** Sun, IJM 17 (2006), Conj. 1.2, at k = 6.
- **Sharpness:** six cosets of one subgroup of index 6.

**Status in sources already read.**
- Sun, MathOverflow Q316709 (2018), as quoted in the parent record: "Since 2010, there is no further progress on the conjecture." The progress meant there is k = 5, by Zhu Gong, unpublished.
- Fornal–Sun (2026-07-27) list only k = 3, 4 as proved for groups.
- For G = Z, k = 6 is known (O'Bryant, k ≤ 20). Menon shows that integer results do not transfer to groups at length 5.
- No k = 6 claim was found. A fresh targeted priority search is a precondition of any contract; a search miss is not novelty.

## 2. Reduction: Sun(6) is equivalent to Core5(6), given the k ≤ 5 results [PROVED-HERE]

> **Core5(6).** No finite group G has subgroups U_1, …, U_6 with [G:U_i] = 5r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.

*Proof.* G may be taken finite (R0 of the k = 5 lane). Suppose six disjoint cosets have all pairwise gcds ≤ 5, and write n_i = [G:G_i].

1. **Each pair has exactly one common prime in {2, 3, 5}.** By the k = 2 case every gcd lies in {2, 3, 4, 5}. So each pair has exactly one common prime in {2, 3, 5} and no other common prime: gcd 2 or 4 gives prime 2, gcd 3 gives 3, gcd 5 gives 5.
2. **One prime divides every index.** Put A_p = {i : p | n_i} for p ∈ {2, 3, 5}. Each of the 15 pairs lies in exactly one A_p, so Σ_p C(|A_p|, 2) = 15 and |A_p ∩ A_q| ≤ 1 for p ≠ q.
   - If no A_p has all six elements, then |A_p| ≤ 5. The only size multiset that works is {4, 4, 3}; for example 10 + 3 + 1 = 14 and 10 + 6 = 16 both fail.
   - In the {4, 4, 3} case, two sets of size 4 that meet in at most one point have a union of at least 7 > 6 points. That is impossible.
   - So some single prime p divides all six indices, and all pairwise gcds lie in {p, 4} (namely {2, 4} if p = 2, or {p} otherwise).
3. **p = 3.** All gcds equal 3 < 4. Any four of the cosets contradict Zhu Theorem 1.1 at k = 4.
4. **p = 2.** Write n_i = 2^{e_i}m_i. The m_i are pairwise coprime, min(e_i, e_j) ≤ 2, and at most one e_i ≥ 3.
   - Two indices with e = 1: contradicts Zhu at k = 3.
   - Exactly one with e = 1: this gives (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd, excluded by Prop 4.5 (sun-coset5 proof-v3 §2).
   - Otherwise any five of the indices form a Core(5) configuration, excluded by sun-coset5 proof-v3. That proof is a candidate pending the parent's replay.
5. **p = 5.** Then n_i = 5r_i with the r_i pairwise coprime, which is exactly Core5(6). Conversely, a Core5(6) configuration violates Sun(6).

**Dependencies.**
- Zhu Theorem 1.1.
- Prop 4.5 as proved in proof-v3.
- **Core(5), which is still a candidate.** Branch 4 inherits Core(5)'s verification status. If the replay of Core(5) failed, Sun(6) would stay open through that branch.

## 3. The calculus for Core5(6), ported from the k = 5 rules

For i ≠ j set α_ij = [G:U_i∩U_j]/(5r_ir_j). Then α_ij ∈ {1, 2, 3, 4}, and |U_iU_j| = α_ij|G|/5.

**Special vertices.**
- E2 is the vertex with r even. It must be split by 2-adic class, v₂(r_E2) = 1 or ≥ 2, because gcd(4, r) matters when α = 4.
- E3 is the vertex with 3 | r.
- E5 is the vertex with 5 | r. [INFERENCE] E5 is irrelevant: no α is divisible by 5, and no two vertices share the prime 5 in local indices. This has to be proved, or E5 must be carried as a separate status.

**Rules that carry over with only the constants changed** (the generic code paths already exist in `core5_engine_v1.py`):

| rule | k = 6 form |
|---|---|
| L1 (T) | τ_min = lcm of α_e/gcd(α_e, r_opp); τ_max = smallest vertex product |
| L2 / L3 (K) | Σ_{i∈S} α_iv ≤ 4 for linked S |
| L4 (P) | granularity |G|/(5·gcd(r_v, α_jk)) |
| F with H1 | an α = 1 triangle gives a subgroup of index 5 (M-S Lemma 3.7 with a = 5) |
| Lemma R | \|D_j\| = q_j\|G\|/5 with q_j ≤ 5 − α_vj, local index q_jr_j |

**A simplification specific to the prime 5.** For any a, b, the subgroup W = ⟨U_a, U_b⟩ has index dividing gcd(5r_a, 5r_b) = 5. So W = G or [G:W] = 5. [INFERENCE] The analogue of H2 should therefore have only one alternative: whenever W ≠ G, it is an index-5 subgroup containing U_a and U_b.

**Triangle filter with no special vertices.** These are hand checks of τ_min = lcm(α) ≤ τ_max.
- Triangles that pass: {1,1,1}, {1,2,2}, {1,3,3}, {1,4,4}, {2,2,2}, {2,2,4}, {2,3,3}, {2,4,4}, {3,3,3}, {3,4,4}, {4,4,4}.
- Of the 20 multisets, the other 9 are T-killed.
- K then removes {1,4,4}: τ = 4 is forced, which links both endpoints of the 1-edge, and 1 + 4 > 4.
- The triangle {1,3,3} survives K, since 1 + 3 = 4 ≤ 4. At k = 5 it was K-killed.

**New rules that will probably be needed** [INFERENCE]:
- constant-α analogues of N2 for α = 2, 3, 4 (these have no 1-edge, so no H);
- the H2 analogue with one alternative;
- a vertex form of Lemma R. The k = 5 S-D argument generalises: a vertex with α = 4 to four of its five neighbours forces disjoint D_j of size |G|/5 each. Note that the "three 3's" vertex lemma (§4) needs re-derivation for index 5.

## 4. Size of the pattern space and how the engine extends

**Counts.**
- Labelled α-patterns: 4^15 = 1,073,741,824. The number of S6-classes is about 4^15/720 ≈ 1.5 × 10^6 [INFERENCE: Burnside count not done].
- Special statuses: E2 has 13 options (none, or one of 6 vertices × 2 classes) and E3 has 7, giving 91 combinations; E5 is assumed irrelevant.
- Total: about 1.4 × 10^8 canonical patterns, or about 9.8 × 10^10 labelled patterns.

**What this rules out.** Neither the per-pattern loop of engine v1 nor check v2's labelled loop is feasible at this size in pure Python.

**What is needed.** A backtracking enumeration over the 15 edges, with τ-pruning on each of the 20 triangles as soon as it is complete. Choosing specials first allows canonical augmentation, or lexicographic-leader pruning under S6. [INFERENCE] The survivors after T and K should be at most about 10^5 labelled patterns, since T passes only 11 of 20 triangle types and couples overlapping triangles. That would make the P, R and F rules cheap afterwards.

**Code work** (standard library, single process): about 1.5–2.5 h to build the backtracking enumerator, port T/K/P/F/R with constants (5, 4), and run the controls. The controls would be:
- reproduce Core_3(4) (= M-S Prop 4.3) and Core(5) with the same engine;
- realisable 5-subconfigurations, for example five cosets of an index-5 subgroup and A5 families of indices 5r;
- selected-mutation demonstrations.

## 5. Feasibility, stated candidly [INFERENCE]

**Arguments for.**
- At k = 5, after freezing, the full case analysis took about 70 minutes, ending with one survivor that a new lemma (R) killed.
- The prime index 5 removes the index-2 branch of H2.
- Lemma R is strong when the α's are large.

**Arguments against.**
- The pattern space is roughly 10^4 times larger.
- α = 4 brings 2-adic subtleties (v₂(r_E2) ∈ {1, ≥2}).
- The new {1,3,3} triangles survive K.
- Survivors whose α's are mostly 2 or 3 may need new N2- or H2-type lemmas whose proofs are not yet in hand.
- The whole result also depends on Core(5) being verified.

**Estimates.**
- A complete computer-assisted proof of Core5(6), with written lemmas, frozen and ready for review by 17:30: about **20–30%**.
- A precise partial result, consisting of a frozen reduction Sun(6) ⟺ Core5(6), a frozen engine with certificates for every killed pattern, and an exact survivor list: about **75–85%**.
- New science would have to stop at 17:30, so the usable window is about 6.5 h. Hostile review of new lemmas would take place after that.

## 6. Draft contract

See `k6-contract-draft-v1.json`. It is a draft for the parent; it does not freeze anything.
