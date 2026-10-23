# sun-coset5: Sun's disjoint-coset conjecture at k = 5 in every group

**Slot:** math-1, transition 42. **Created:** 2026-10-18, about 09:40 PDT by the host clock, then frozen read-only. Later corrections and results go only into new files: `README-addendum-vN.md`, `proof-vN.md`, `evidence/...`.

**Frozen contract:** `institute/runs/six-lane-2026-10-16/screening/math-1-sun-coset5-contract.json` (sha256 8c61ff00…1367).

**Rules (lemmas, with proofs):** `rules-v1.md`, frozen together with this file. Hashes are in `evidence/freeze-v1.sha256`.

## 1. Exact target

Let G be any group. Let a_1G_1, …, a_5G_5 be pairwise disjoint left cosets of subgroups G_i of finite index. The G_i need not be distinct. Then gcd([G:G_i], [G:G_j]) ≥ 5 for some i < j.

- **Source:** Sun, Internat. J. Math. 17 (2006), Conjecture 1.2, at k = 5 (`sources/arxiv-math0501451v4.pdf`).
- **Sharpness:** five cosets of one subgroup of index 5.
- **Deliverable:** a complete written proof, or an explicit counterexample checked by two independent exact computations. If neither is reached, a PARTIAL report.

**Known before this lane (from primary sources):**
- k = 2, and all p-groups: Sun 2006.
- k = 3, 4 in every group: Zhu, arXiv:0807.2207, Theorem 1.1. Reproved by Margolis–Schnabel (M-S), arXiv:1803.03569, Theorem B with Props 4.2, 4.3, 4.5.
- k ≤ 20 for the group Z only: O'Bryant.
- Menon, arXiv:2608.15873 (2026-08-16), realises (6,6,6,10,15) in A5 although it is not Z-harmonic. So results for Z do not transfer to groups at length 5.

The priority re-search of 2026-10-18 08:34 PDT found no claim of k = 5 for groups; see `evidence/priority-search-v1/summary.json`. A search miss is not novelty.

## 2. Reductions

**R0. Reduction to finite groups.** This is standard; Menon §2 gives the same argument.
- Put N = ∩_i core_G(G_i). It is a normal subgroup of finite index, contained in every G_i.
- Each coset a_iG_i is the full preimage of its image in G/N.
- Passing to G/N therefore preserves all indices [G:G_i], all indices of intersections, and disjointness.
- Hence a counterexample in any group yields one in a finite group with the same data. From here on G is finite.

**R1. Reduction to Core(5).** Sun at k = 5 in all groups is equivalent to the following statement, which is correct as stated in the screen.

> **Core(5).** No finite group G has subgroups U_1, …, U_5 with [G:U_i] = 4r_i, the r_i pairwise coprime, and with pairwise disjoint cosets g_iU_i.

*Proof.*
- (⇐) Core(5) is a special case of the target. In such a configuration every pairwise gcd equals 4, which is less than 5.
- (⇒) Suppose five disjoint cosets have all pairwise gcds ≤ 4. Write n_i = [G:G_i].
  1. **Each gcd is 2, 3 or 4.** By L0.6 no pair is coprime. So each pairwise gcd lies in {2, 3, 4}, and 6 divides none of them.
  2. **All n_i are divisible by 3, or all are even.** If some n_i is odd, it shares the factor 3 with every n_j, so 3 divides all five.
  3. **The case where 3 divides every n_i.** Then every gcd equals 3. Writing n_i = 3r_i, the r_i are pairwise coprime. Four of them contradict M-S Prop 4.3, which is also Zhu Theorem 3.1.
  4. **The case where every n_i is even.** Write n_i = 2^{e_i} m_i with m_i odd. From gcd ∈ {2, 4} we get: the m_i are pairwise coprime, every e_i ≥ 1, and min(e_i, e_j) ≤ 2. So at most one e_i is ≥ 3.
     - If two indices have e = 1, then together with any third index they form (2r, 2r', 2r'') with pairwise coprime r's. This contradicts M-S Prop 4.2, which is also Zhu Theorem 2.2.
     - If exactly one index has e = 1, say n_1 = 2m_1, take any three of the others. They are 4r_j with r_j = 2^{e_j−2} m_j, pairwise coprime because at most one e_j ≥ 3. With r_1 = m_1 odd, this contradicts M-S Prop 4.5.
     - Otherwise every e_i ≥ 2, so n_i = 4r_i with r_i = 2^{e_i−2} m_i pairwise coprime. That is a Core(5) configuration. ∎

**How R1 depends on published results.**
- R1 uses M-S Prop 4.5, which is not implied by Sun's statement for k = 4: in (2r_1, 4r_2, 4r_3, 4r_4) the pairwise gcd 4 already occurs.
- The printed proof of Prop 4.5 relies on Lemma 4.4. Its first bullet is misprinted and should read "α ≠ 2", as its proof shows; see `rules-v1.md` §L3.
- Control C1 re-derives Props 4.2, 4.3 and 4.5 with this lane's own rules T, K, P, as an independent check.

**R2. Restriction (not used for the gate).**
- *Statement.* Let K ≤ G with KG_i = G for every i. Then the configuration restricts to K with the same indices.
- *Proof.* Since g_i ∈ KG_i, the coset g_iG_i meets K, and g_iG_i ∩ K = k_i(K ∩ G_i). Also [K : K∩G_i] = |KG_i| / |G_i| = [G:G_i]. Disjointness is inherited.
- *Consequence.* A minimal counterexample has no proper subgroup K with KG_i = G for all i. If G is solvable, a Hall π-subgroup K, where π is the set of primes dividing the indices, satisfies KG_i = G. So a minimal solvable counterexample is a π-group.

**R3. Coprime-fibre descent (not used for the gate).**
- *Statement.* Let Q be a normal subgroup of G such that the numbers [Q : Q∩G_i] are pairwise coprime. Then the images g_iG_iQ/Q are pairwise disjoint cosets of subgroups of G/Q, and their indices divide the original indices.
- *Proof.* Suppose g_iG_iQ meets g_jG_jQ. Then x = g_i⁻¹g_j ∈ G_iQG_j, so x = u_i q u_j with q ∈ Q. By L0.6 applied in Q, (Q∩G_i)(Q∩G_j) = Q. Hence q ∈ G_iG_j, so x ∈ G_iG_j. By L0.2 this contradicts disjointness.
- *Core(5) application.* Let Q be normal of odd order. Then [Q : Q∩U_i] is odd and divides 4r_i, so it divides r_i, and these numbers are pairwise coprime. So a minimal counterexample to Core(5) has O(G) = 1.

## 3. The α-calculus: statement of the attack

**Set-up.** Take a Core(5) configuration and put α_ij = [G : U_i∩U_j] / (4r_ir_j). Then α_ij ∈ {1, 2, 3} and |U_iU_j| = α_ij |G| / 4 (L0.3). Let E2 be the vertex with r even and E3 the vertex with 3 | r, if they exist.

A **pattern** is a triple (α, E2, E3) taken up to relabelling. There are 792 α-classes and 21,150 patterns; these counts are from the exploratory run and are recomputed by the frozen program.

**Plan.**
1. The frozen program `code/core5_engine_v1.py` (standard library, deterministic) applies the rules of `rules-v1.md` in a fixed order. It writes one certificate per killed pattern (rule plus witness) and the list of survivors. It also runs controls C1–C4.
2. The survivors are attacked by written proofs (new lemmas in `proof-vN.md`).
3. A candidate full proof is frozen as `proof-v1.md`, and the parent is notified.
4. Theorem frame: a minimal-order counterexample G (rules-v1 §0) is assumed. Every pattern must be refuted by a proved lemma.

**Exploratory record, made before the freeze (not preregistered, not gate evidence).**
- Files: `archive/exploratory-pre-freeze-v1/explore_cells.py` and `outputs.txt`.
- Counts: 21,150 patterns gave 756 survivors under the M-S triangle rules plus screen N1–N3, then 28 under early T/K/P/F rules, then 23 after adding N2 and the early fibre rules.
- The 28 survivors fall into four α-shapes on vertices 0..4:
  - **S-A:** all ten α = 2.
  - **S-B:** α01 = 1, the other nine = 2.
  - **S-C:** α01 = α23 = 1, the other eight = 2.
  - **S-D:** α01 = α02 = 1, α03 = α04 = 2, and the six α among {1,2,3,4} all equal 3. This shape occurs only with E2 = 1 and E3 = 0.

## 4. What counts as success

**Gate.** Every pattern is refuted by proved lemmas; or there is an explicit counterexample verified twice, exactly. The gate also requires parent re-derivation, hostile reviews from both CLI families, and a post-result priority audit.

**Not the gate.** A partial reduction is not the gate. Neither is any small-group or permutation-group search; those are used only as sanity controls (C2, C3).

**Separation of claims.** Correctness, novelty and significance are reported separately.

## 5. Files at freeze time (sha256)

**Sources:**
- `sources/arxiv-1803.03569v1.pdf` 3c3341ba5c642fb4174430ffab4bbe92a10255111017de146f4a73c69a7e3ffe
- `sources/arxiv-0807.2207v1.pdf` 5f5b9a7172ec55ef7ffb629bf123de9538fcc821d24f499ee9a91c0e2e205c62
- `sources/arxiv-2608.15873v1.pdf` 2717059bdf6a7d38e92226bb35a887a8502a499a6808e4024961b87bd14f3296
- `sources/arxiv-2607.24655v1.pdf` 33bffe0628027510d69a51ce5f39ab72541e5562f4fcd29dd1fe2903e8728b08
- `sources/arxiv-math0501451v4.pdf` 9e62667f0c4ae77051a4b3da162428f91853dd7e995f0e18fbb8713ea03318e2

**Priority search:**
- `code/priority_search_v1.py` and `evidence/priority-search-v1/` (summary sha256 0c952a7196ad0a83b72a7e885317fb50e7794390182da7749cbe8a14eda41c03)

**Everything else:** the hashes of `README.md`, `rules-v1.md` and the archived exploratory files are in `evidence/freeze-v1.sha256`.
