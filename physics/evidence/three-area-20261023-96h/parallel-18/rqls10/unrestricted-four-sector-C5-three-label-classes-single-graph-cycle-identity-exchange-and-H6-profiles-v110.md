# RQLS10 v110 — C5 three-label classes: the single graph is 2-regular, a cycle identity for site planes, a same-site exchange lemma, and the H6 d-profile table

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 23:55:52 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra and hand case analysis only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

After v109, every surviving all-sparse C5 resolution contains three-label classes. The six three-label types are listed below; each is written as (doubled site; single sites), with labels {C_i, C_{i+1}, C_{i+3}} and positions as in v86:

| Type | Doubled site | Single sites |
|---|---|---|
| D0a(i) | L_i | T_{i+1}, L_{i+3} |
| D0b(i) | L_i | T_{i+1}, T_{i+3} |
| D1a(i) | T_{i+1} | L_i, L_{i+3} |
| D1b(i) | T_{i+1} | L_i, T_{i+3} |
| D3a(i) | L_{i+3} | L_i, T_{i+1} |
| D3b(i) | T_{i+3} | L_i, T_{i+1} |

Write Z_σ for the doubled diagonal plane of σ. By v105 MATCH, the two singles of σ span Z_σ^⊥.

A diagonal is BROKEN when its two cells lie in different classes.

## 1. Lemma SINGLE-GRAPH

The three-label classes and the broken diagonals form a 2-regular graph.
- Each three-label class has exactly two singles, coming from two different sites and hence two different broken diagonals.
- Each broken diagonal has exactly two cells, lying in two different three-label classes. Two-label classes use only whole diagonals.

Consequently the number b of three-label classes equals the number of broken diagonals, every component is a cycle, and b ≥ 2.

## 2. Lemma CYCLE-IDENTITY

Let σ_1, …, σ_m be a cycle of the single graph. Here σ_k uses singles from the broken diagonals δ_k and δ_{k+1}. Let δ_k' denote the other diagonal plane of δ_k's site. Then

    Σ_k P_{Z_{σ_k}} = Σ_k P_{δ_k'}.

Proof. Each σ_k is an orthonormal basis, so I − P_{Z_k} is the sum of the projections onto its two singles. Summing over k, the right-hand side is Σ_k P_{δ_k}, which equals Σ_k (I − P_{δ_k'}).

Each side is a sum of m eigenprojections of site operators. The identity is therefore a linear relation among site operators: Σ ± M_{doubled sites} = Σ ± M_{broken sites}.

## 3. Lemma EXCHANGE (same-site 2-cycle)

Suppose a 2-cycle {σ, σ~} has its doubled planes equal to the TWO diagonals of one site s0. Let s1 and s2 be its broken sites. Then:
- M_{s1} = ±M_{s2};
- the broken diagonal of s1 spans the same plane as the intact diagonal of s2, and vice versa;
- M_{s0} commutes with M_{s1}.

Proof.
1. P_{Z_σ} + P_{Z_σ~} = I, so by §2 the intact planes δ1' and δ2' are complementary. That is, E^{−u1}(M_{s1})^⊥ = E^{−u2}(M_{s2}), which gives M_{s1} = ±M_{s2}.
2. σ's singles x ∈ δ1 and y ∈ δ2 = δ1^⊥ span Z_σ~. So P_{Z_σ~} is diagonal in the splitting δ1 ⊕ δ2.

In D3-type 2-cycles the broken sites are L_i and T_{i+1}. Their intact diagonals are complementary planes, which is exactly the geometry of an adjacent class A_i. The 2-cycle therefore has the shape of an EXCHANGE: one A_i class is replaced by two three-label classes over both diagonals of the C_{i+3} site. This manuscript does NOT assert that the intact diagonals actually form an A_i class. (Pre-pin draft correction: an earlier unpinned wording said that one A_i class "survives"; that was an overstatement and was withdrawn before the first pin.)

## 4. Lemma H6-PROFILES (hand case analysis)

Write (n_2, n_3, n_4) for the numbers of a class's H6 cells in the d = 2, 3, 4 position blocks. Intersecting row-pair H6 columns with class H6 columns, and listing every admissible matching, gives:

| Type | Possible (n_2, n_3, n_4) |
|---|---|
| D0a, D3a | (1,0,5), (0,2,4), (3,1,2), (2,3,1) |
| D0b | (5,1,0), (3,0,3), (2,2,2) |
| D1a | (0,1,5), (3,0,3), (2,2,2) |
| D1b, D3b | (5,0,1), (4,2,0), (2,1,3), (1,3,2) |

Two-label types (v109) give:
- A, B, G0: (2,2,2);
- LL: (2,4,0);
- TT: (0,4,2);
- G1: (1,4,1);
- G2: (0,6,0).

Every resolution has Σ = (20, 20, 20). Since three-label classes may have n_3 ∈ {0, 1, 2, 3}, the v109 d=3 count does NOT extend to three-label patterns. Excluding them requires geometric input (§2–§3) or a finer H6 analysis.

Example. For a Z5-symmetric pair of orbits {D3a(i), D3b(i)}:
- the classes with the same i share the broken diagonals of L_i and T_{i+1}, so they form 2-cycles with doubled sites L_{i+3} and T_{i+3};
- §2 gives R_{i+3}(aΣ_{i+2} + bΣ_{i+3}) = a'R_iΣ_{i−1} + b'R_{i+1}Σ_{i+1} with signs a, b, a', b';
- squaring gives ab{Σ_{i+2}, Σ_{i+3}} = a'b'{R_iΣ_{i−1}, R_{i+1}Σ_{i+1}};
- the admissible profile pairs are (3,1,2)+(1,3,2), (2,3,1)+(2,1,3) and (0,2,4)+(4,2,0).

This example is NOT shown to exist.

## 5. Status

These are written structural lemmas only. C5 with three-label classes is neither excluded nor realized. The H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v86 Corollary R; v105 SITE/MATCH; v109 types and profiles; elementary projection algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S110. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 pre-pin draft correction;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
