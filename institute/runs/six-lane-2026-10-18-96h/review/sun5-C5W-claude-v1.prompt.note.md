# Hostile review: C5W-v1 (written Core(5) theorem)

**Basis.** I used only the pasted texts, with no tools, execution, edits or delegation. Hashes, byte counts and line numbers are taken as given, not verified. Line references are to files in `…/sun-coset7/continuations/core5-written-bridge/` unless prefixed `proof-v4:`. The proof of Prop 4.5 (proof-v4 §2, after line 61) is not in the package, which limits the corollary audit.

## Verdict

| Part | FATAL | MAJOR | MINOR |
|---|---|---|---|
| Theorem C5W (MU, INV, FC, §3, PR, AR, case split) | 0 | 0 | 8 |
| Conditional Sun(5) composite (corollary) | 0 | 0 | 3 |

I find Theorem C5W correct as written. It covers every finite G, every E2/E3 placement and r_i = 1, with no exponent or cofactor cap and no minimal-order frame. It uses only Lagrange/product-formula facts, Sun(2) (proved inside FC) and Zhu's Sun(3).

I found no logical gap. Every finding is either a missing one-line justification or a scope/bookkeeping wording issue.

## 1. Per-claim re-derivation

**Q1. Statement, α, markers (`C5W-v1.md:17-18, 36, 40-42`): PASS.**
- The quotation matches proof-v4:49, except that "..." replaces "…".
- Since gcd(n_i, n_j) = 4, lcm = 4r_ir_j, so the α of line 36 is the α of proof-v4:113.
- E2 and E3 are functions of the labelled r-tuple. Each is unique by pairwise coprimality, and E2 = E3 is allowed.
- No hypothesis is added or dropped.

**Q2. MU (`:37-39`): PASS.**
- n_i and n_j both divide I_ij, so α is a positive integer.
- |U_iU_j|/|G| = I_ij/(n_in_j) = α/4.
- g_i⁻¹g_j ∉ U_iU_j, so α ≤ 3.

**Q3. INV and the all-3 → all-1 step (`:45-50`): PASS (m1).**
- (g_iU_i)⁻¹ = g_i⁻¹U_i\*. Inversion is a bijection, and [G:U_i\*] = n_i.
- With h = g_i⁻¹g_j, we have U_i\* ∩ U_j\* = g_i(U_i ∩ hU_jh⁻¹)g_i⁻¹. Hence α\*_ij = [G : U_i ∩ hU_jh⁻¹]/lcm and |U_ihU_j|/|G| = α\*_ij/4.
- h lies in U_ihU_j but not in U_iU_j. So these are distinct, hence disjoint, (U_i,U_j)-double cosets, and α + α\* ≤ 4.
- α = 3 gives α\* ≤ 1, and α\* ≥ 1 by MU applied to Γ\*.

*Same labelled class.* Coset i of Γ\* is (g_iU_i)⁻¹ with index n_i. So r_i, E2, E3, P and plainness, which are all functions of the labelled index tuple, are identical.
- α\*_vj is Γ\*'s own multiplier at the same labelled pair, and INV is an inequality for each pair separately.
- PR and AR quantify over all Core(5) configurations with a given marker placement. Each application uses one configuration's data only; Γ and Γ\* data are never mixed.
- Only index-defined data cross over, which is what sun7-lfc-inv-parent-verdict-v1:19 permits.

The step is legitimate.

**Q4. FC (`:52-65`): PASS (m2, m3).**
- U_v ∩ U_j has index I_vj = 4r_vr_jα_vj. So λ_j = I_vj/n_v = r_jα_vj and t_j = I_vj/n_j = r_vα_vj.
- g_juU_v = g_ju′U_v iff u⁻¹u′ ∈ U_j ∩ U_v. So exactly t_j fibres are met, and none of them is g_vU_v.
- The piece in B = bU_v is p_j(U_j ∩ U_v). Its translate b⁻¹p_j(U_j ∩ U_v) ⊂ U_v is a left coset of index λ_j, and distinct j give disjoint pieces.
- The Sun(2) proof is complete: [U_v:H∩K] ≥ λλ′, so HK = U_v, so xH ∩ yK ≠ ∅. Sun(3) is then applied to any three pieces.
- Every actual S_B, including the empty set, is admissible. Omitting the |T| = 4 clause only enlarges the constrained family, so it is a sound relaxation.
- Summing over B ≠ g_vU_v gives Σ_j w_j t_j ≤ n_v − 1, hence Σ w_jα_vj/4 ≤ 1 − 1/n_v.

The strict margin comes from the exclusive fibre g_vU_v, and it is what closes every case below whose value is exactly 1. No Sun(t) with t ≥ 4 is used.

**Q5. §3 valuations, G1, G2, V2 (`:68-75`): PASS (m4, m5).**
- A prime p ≥ 5 dividing both r_jα_vj and r_kα_vk would divide both r_j and r_k, which is impossible.
- v_2(λ_j) = v_2(r_j) + [α = 2] and v_3(λ_j) = v_3(r_j) + [α = 3].
- G1 holds against every other neighbour, including the non-plain b of AR.
- G2 gives gcd 2 for (2,2), gcd 3 for (3,3), and gcd 1 for every other pair.
- Pairwise-gcd-2 vertices admit no admissible triple, so the V2 weights are feasible within their class.
- Sun(3) only ever restricts sets of three or more pairwise-gcd-2 vertices. That happens for PR with n₂ ≥ 3, and for AR with β = 2 and n₂ ≥ 2, or with n₂ = 3.

**Q6. Lemma PR (`:78-86`): PASS.**

By G1/G2, every admissible set lies inside one multiplier class:
- class 1: singletons only;
- class 2: at most 2 members;
- class 3: at most n₃ members.

So every admissible set has weight at most 1. Values for all 14 tuples with n₃ ≤ 3:

| n1,n2,n3 | value | n1,n2,n3 | value |
|---|---|---|---|
| 4,0,0 | 1 | 2,1,1 | 7/4 |
| 3,1,0 | 5/4 | 1,2,1 | 3/2 |
| 2,2,0 | 1 | 0,3,1 | 3/2 |
| 1,3,0 | 1 | 2,0,2 | 5/4 |
| 0,4,0 | 1 | 1,1,2 | 3/2 |
| 3,0,1 | 3/2 | 0,2,2 | 5/4 |
| 1,0,3 | 1 | 0,1,3 | 5/4 |

Every value is at least 1, which exceeds 1 − 1/n_v. The tuple (0,0,4) gives only 3/4 and is correctly routed to Γ\*.

**Q7. Lemma AR (`:89-107`): PASS (m7).**
- v_2(λ_b) = [β = 2] because r_b is odd, and v_3(λ_b) ≥ 1.
- gcd(λ_b, λ_p) = 2^[β=2 ∧ α_ap=2] · 3^[α_ap=3].

Feasibility, case by case:
- **n₃ ∈ {1,2}, any β.** Any admissible set containing p\* lies inside {p\*, q, b}. A class-1 vertex appears only as a singleton. Every other admissible set lies inside class 2 ∪ {b} or inside {q, b}. The zero-weight vertices b and q never push a set above 1.
- **n₃ = 0, β ∈ {1,3}.** b is isolated.
- **n₃ = 0, β = 2.** The vertices of {b} ∪ class 2 are pairwise of gcd 2, so there is no admissible triple among them. If n₂ = 0, b is isolated.

| n1,n2,n3 | β=1 | β=2 | β=3 |
|---|---|---|---|
| 1,0,2 | 1 | 1 | 1 |
| 0,1,2 | 5/4 | 5/4 | 5/4 |
| 2,0,1 | 5/4 | 5/4 | 5/4 |
| 1,1,1 | 3/2 | 3/2 | 3/2 |
| 0,2,1 | 5/4 | 5/4 | 5/4 |
| 3,0,0 | 1 | 5/4 | 3/2 |
| 2,1,0 | 5/4 | 1 | 7/4 |
| 1,2,0 | 1 | 1 | 3/2 |
| 0,3,0 | 1 | 1 | 3/2 |

Every value is at least 1. The tuple (0,0,3) is routed to Γ\*. There it becomes (3,0,0) with an arbitrary β\*, which the table covers.

**Q8. Theorem case split (`:110-120`): PASS (m6).**
- Case 1 ("E2 and E3 are not two distinct vertices") covers: neither exists, only E2, only E3, and E2 = E3. Case 2 is the complement, so the split is exhaustive.
- In every Case-1 subcase, all four neighbours of v are plain.
- In Case 2, P is plain, r_b is odd and 3 divides r_b.
- Γ\* has the same markers, so the same v (or the same a, b, P) qualifies. α = 3 gives α\* = 1 ≠ 3, which satisfies the hypothesis of PR or AR.

Unrolled, both inverse branches are pure packing. Case 1 needs 4r_v exclusive fibres, but only 4r_v − 1 are available. Case 2 needs 3r_a + β\*r_a ≥ 4r_a, but only 4r_a − 1 are available.

**Q9. Import boundary (`:11-12, 25-32, 129-130, 141-142`): PASS.**
- None of the following is used: the bridge, certificates, counts, the engine, the S-D step, the minimal frame, or Sun(4) through Sun(6).
- The accepted K7 LFC/INV package, which carries Sun(5)/Sun(6) (sun7 verdict:18), is not imported. FC is re-proved at k = 5, where at most 4 pieces share a fibre.
- The citation of K7 erratum E1 at line 26 only points to facts that MU re-proves.
- The S-D check at :129-130 is labelled as not a premise, and it is itself correct: it is AR's n₃ = 0 case applied to Γ\*.

## 2. Findings: Theorem (all MINOR)

| ID | Location | Problem | Minimal fix |
|---|---|---|---|
| m1 | `C5W-v1.md:50` | "α = 3 ⇒ α\* = 1" silently uses α\* ≥ 1 | "…⇒ α\*_ij ≤ 1, hence = 1 by Lemma MU for Γ\*" |
| m2 | `:53` | the values of λ_j and t_j are asserted, not derived | insert "(U_v ∩ U_j has index I_vj = 4r_vr_jα_vj; λ_j = I_vj/n_v, t_j = I_vj/n_j)" |
| m3 | `:59-60` | b⁻¹p_j ∈ U_v is not stated | insert "(b⁻¹p_j ∈ U_v since p_j ∈ bU_v)" |
| m4 | `:73` | "best value" is an optimality claim that is unproved (true, but unused) | "the value given by the following weights" |
| m5 | `:54`; used at 73, 80, 92-93, 96-98, 100, 104 | "compatible"/"incompatible" are never defined | at :54 add "j, k are compatible iff gcd(λ_j, λ_k) ≥ 2" |
| m6 | `:117-118`, `:120` | the apex for Γ\* is not fixed, which matters in the "any vertex" subcase | "Lemma PR for Γ\* at the same v"; "Lemma AR for Γ\* with the same a, b, P" |
| m7 | `:89`, `:91` | plainness of P and oddness of r_b are left implicit | append "(by uniqueness of E2, E3, :41)" |
| m8 | `:17`; `review-package-C5W-v1.md:18` | "verbatim" quote uses "..." for "…"; the package excerpt "110-122" stops mid-sentence in the corollary | "verbatim up to ASCII"; cite lines 110-120 |

## 3. Conditional Sun(5) composite (`C5W-v1.md:122-128`), audited separately

**The composition is valid. I found no circularity and no visible computational dependency.**
- R0 (proof-v4:41-45) reduces to finite G.
- R1 works group by group (proof-v4:53-61, F-3 at :103):
  - all gcds lie in {2,3,4} by Sun(2);
  - if all indices are divisible by 3, Zhu's theorem at k=4 excludes it;
  - two indices with e = 1 are excluded by Zhu at k=3;
  - one index with e = 1 is excluded by Prop 4.5;
  - otherwise there is a Core(5) configuration in the same G, and C5W refutes it.
- C5W's statement for every group is strictly stronger than what proof-v4 §7 consumes, which is only the refutation of the minimal G's configuration. So the substitution is sound.
- No Sun(5) instance occurs anywhere. Because R1 is group by group, the composite needs no minimal frame, provided Prop 4.5 does not use one; that proof is not excerpted here.
- proof-v4's finite-exact items (:270-273) and its orbit count (:113) feed only the certificate branch that C5W removes.

| ID | Location | Problem | Minimal fix |
|---|---|---|---|
| C1 | `C5W-v1.md:125-127`; `review-package-C5W-v1.md:60` | The hand-written list "Zhu Sun(3)/Sun(4), rules-v1 L0.3-L0.5, L1-L3 used by Prop 4.5" cannot be audited here, because Prop 4.5's proof is not excerpted. It also omits re-proved items that proof-v4 itself lists for §§1-2: L0.2+L0.6 (proof-v4:55, :259) and M-S Lemma 3.1, proved inline in §2(g) (:260). | Replace with "exactly the dependencies of proof-v4 §§1-2 as accepted in sun-coset5-parent-verdict-v1:18, read with erratum v3"; add the Prop 4.5 line range to the excerpt manifest. |
| C2 | `:25`, `:133-142`; `review-package-C5W-v1.md:61` | Claims that hold for the theorem read as global: "none load-bearing", "Only Sun(2) … and Zhu's Sun(3) enter", "Computation boundary: none". For the composite, erratum E6 (the patched Prop 4.5) and E9 (every L3/K2 use) are load-bearing, and Zhu's Sun(4) enters at proof-v4:57. The DAG has no corollary node. | Prefix those lines with "For Theorem C5W:"; add a DAG row "Corollary (conditional): C5W; R0; R1; Prop 4.5 + E6/E9; Zhu k=3,4; not accepted". |
| C3 | `:127` | The stated condition is only "review of this file". The composite also inherits the recorded status of proof-v4 §§1-2: v4 received no further CLI review (parent verdict:15), and §§1-2 were accepted as items inside a computer-assisted verdict (:5, :18). | "…conditional on review of this file; inherits the acceptance status of proof-v4 §§1-2 (parent verdict v1, item 1)". |

**Not assessed:** hashes, byte counts, timestamps and scope-freeze provenance; Zhu's proof (the permitted import); the text of Prop 4.5.
