# sun-coset6: Sun's disjoint-coset conjecture at k = 6 in every group

- **Slot:** math-1, transition 43.
- **Contract:** `institute/runs/six-lane-2026-10-16/screening/math-1-sun-coset6-contract.json` (sha256 17fe5a9e…1769, frozen 10:24:35 PDT).
- **Freeze time and hashes:** host-clock record in `evidence/freeze-v1.sha256`. Times written inside this file are not authoritative.
- **Rules (lemmas and proofs):** `rules-k6-v1.md`, frozen together with this file.
- **Labels:** "[NEW]" means only that something was written in this lane; it is not a novelty claim. Exploratory cells are labelled EXPLORATORY and are never counted.

## 1. Exact target

**Statement.** Let a_1G_1, …, a_6G_6 be pairwise disjoint left cosets of finite-index subgroups of an arbitrary group G. The subgroups may coincide. Then gcd([G:G_i], [G:G_j]) ≥ 6 for some i < j. Otherwise an exact counterexample is required.

**Source and sharpness.** This is Sun, Internat. J. Math. 17 (2006), Conjecture 1.2, at k = 6. Six cosets of one subgroup of index 6 show the bound is sharp.

**Status.**
- The parent's pre-check (S/math-1-sun-coset6-priority-precheck-v1.md) located no k ≥ 6 claim for groups.
- Sun (MathOverflow Q316709, 2018) wrote: "since 2010, there is no further progress".
- For G = Z, O'Bryant proved k ≤ 20. That proof is integer-only and is not imported here.
- A search miss is not novelty.

## 2. Reductions

**R0. Reduction to finite groups.** Same proof as sun-coset5 proof-v4 §1. core_G(G_i) is the kernel of the action of G on G/G_i, so it has index at most [G:G_i]!. The intersection of these cores is a normal subgroup of finite index lying inside every G_i. Every coset a_iG_i is the full preimage of its image in the quotient, so indices, intersections and disjointness all pass to the finite quotient.

**R1(6). Sun(6) ⟺ Core5(6), given the results for k ≤ 5.** [NEW; the parent re-derived it by hand; not yet hostile-reviewed]

> **Core5(6).** No finite group G has subgroups U_1, …, U_6 with [G:U_i] = 5r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.

**(Sun(6) ⇒ Core5(6)).** A Core5(6) configuration has every pairwise gcd equal to 5, and 5 < 6.

**(Core5(6) ⇒ Sun(6)), group by group.** Assume six disjoint cosets in G have pairwise gcds all ≤ 5, and write n_i = [G:G_i].

1. **Each gcd is 2, 3, 4 or 5.** No gcd is 1, by the k = 2 case (L0.2 + L0.6). So each pair shares exactly one prime from {2, 3, 5} and no other prime.
2. **The cover by A_p.** Put A_p = {i : p | n_i} for p ∈ {2, 3, 5}. Each of the 15 pairs lies in exactly one A_p. Hence Σ_p C(|A_p|, 2) = 15, and |A_p ∩ A_q| ≤ 1 for p ≠ q.
   - Suppose every |A_p| ≤ 5. The only values of C(|A_p|, 2) are 0, 1, 3, 6 and 10, and the only way for three of them to sum to 15 is 6 + 6 + 3, i.e. sizes {4, 4, 3}.
   - But two 4-sets meeting in at most one point have a union of at least 7 points, and there are only 6. So this case is impossible.
   - Therefore one prime p divides all six n_i.
3. **p = 3.** All six gcds equal 3, which is < 4. Any four of the cosets contradict Zhu Theorem 1.1 at k = 4.
4. **p = 2.** Write n_i = 2^{e_i}m_i with m_i odd. The m_i are pairwise coprime, min(e_i, e_j) ≤ 2, and at most one e_i ≥ 3.
   - If two indices have e = 1, then with any third index all pairwise gcds are 2 < 3. This contradicts Zhu Theorem 1.1 at k = 3.
   - If exactly one has e = 1, that index together with three others has the form (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd. This is excluded by Prop 4.5 as proved in sun-coset5 proof-v4 §2.
   - Otherwise any five of the indices form a Core(5) configuration in G. Core(5) is excluded by sun-coset5 proof-v4.
5. **p = 5.** Every gcd is exactly 5. So n_i = 5r_i with the r_i pairwise coprime, which is a Core5(6) configuration in G.

**Dependence.** Branch p = 2 relies on Core(5) (sun-coset5 proof-v4; parent bridge PASS). That result still awaits the parent's correctness verdict. Any k = 6 gate is conditional on that verdict, as the contract states. k = 5 itself carries a prior unpublished claim (Z. Gong, as reported by Sun). That claim does not affect whether k = 6 is open.

**Minimal-counterexample frame.** Suppose Sun(6) fails. Choose G of minimal order among finite groups that contain six pairwise disjoint cosets with all pairwise index-gcds ≤ 5. R1(6) holds group by group, so G carries a Core5(6) configuration. In this frame:
- every proper subgroup of G satisfies Sun(6);
- every group satisfies Sun(k) for k ≤ 4 (Zhu Theorem 1.1, plus L0.6);
- every group satisfies Sun(5) (sun-coset5 proof-v4, under the stated dependence).

## 3. The attack

**Patterns.** For a Core5(6) configuration put α_ij = [G:U_i∩U_j]/(5r_ir_j) ∈ {1, 2, 3, 4}. Special vertices:
- E2: the vertex with r even, together with its class (v₂(r) = 1, or v₂(r) ≥ 2);
- E3: the vertex with 3 | r;
- E5: the vertex with 5 | r. E5 matters only inside fibre rules (rules-k6-v1 L8).

**Enumeration.**
- Under S6, every (α, E2-class, E3) is equivalent to one with E2 and E3 in a canonical position. There are 8 types: none; E3 only; E2 of class 1 or 2 alone; E2 together with E3 on the same vertex; E2 and E3 on different vertices.
- For each type, all 4^15 α-labellings are enumerated by backtracking. Triangles are pruned with the T lemma, so every labelling that contains a T-forbidden triangle is covered by a triangle-local certificate.
- Every leaf, i.e. every T-consistent labelling, receives a rule certificate or is listed as a survivor. Leaves are deduplicated up to the stabiliser of the special placement.

**Order of work.**
1. Frozen program.
2. Second checker, coded independently.
3. Written lemmas against the survivors, frozen in rules-k6-v2 and later.

**PARTIAL if needed.** If no survivor beyond the frozen list is eliminated by 15:30 PDT, the lane reports PARTIAL exactly as the contract defines it.

## 4. Exploratory calibration before the freeze (EXPLORATORY; not counted; not evidence)

Eval-kernel cells run between 10:27 and 11:00 PDT tried T, K, P, a fibre rule and a Lemma-R LP rule on some special types.

| special type | T/K leaves | survivors |
|---|---|---|
| none | 15,513 | 0 |
| E3 only | 15,785 | 0 |
| E2, class 1 | 22,863 | 700 labelled (11 orbits) |
| E2, class 2 | 25,103 | 830 labelled (14 orbits) |
| other four types | not completed (cell hit its 1800 s timeout) | — |

In both E2 types, every surviving orbit had the E2 vertex with star (1,1,2,2,2) and all other α in {2, 4}.

No file was written by these cells, and they are not counted.
