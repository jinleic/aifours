# RQLS10 v90 — Dense cells are chirality-balanced, pairwise product cells, an explicit dense normal form, and a three-trail chirality lock

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 19:27:02 PDT 2026**. AUTHOR-WRITTEN CANDIDATE, not machine/kernel checked. Written Clifford/projection/row-ONB arguments only; no scientific Eval/interpreter/CAS/program/enumeration/solver/replay, approximate scout, chosen angle/state/control/probe or newGO.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption or verdict inheritance.

## 1. Setting

D is a DENSE vertex with column planes A_1..A_4, rows e_i (row one) and f_i (row two), e_i,f_i in A_i. v88 Lemma TD makes the planes pairwise interior-isoclinic, and v89 Theorem CH gives the unique chirality projection Pi = Pi^D. A_i meets V_+ = range Pi in a line p_i and V_- in a line m_i, with |<p_i|p_j>|^2 = |<m_i|m_j>|^2 = lambda_ij > 0. Ordinary MAX only; no resolution is used.

## 2. Theorem B: every cell at a dense vertex is chirality-balanced

Write e_i = alpha_i p_i + beta_i m_i, with |alpha_i|^2 + |beta_i|^2 = 1. Since V_+ is orthogonal to V_-, for i not equal to j

    0 = <e_i,e_j> = conj(alpha_i) alpha_j <p_i|p_j> + conj(beta_i) beta_j <m_i|m_j>.

Equal moduli |<p_i|p_j>| = |<m_i|m_j>| = sqrt(lambda_ij) > 0 give |alpha_i alpha_j| = |beta_i beta_j|. With r_i = |alpha_i|^2 this reads r_i + r_j = 1 for ALL six pairs among four indices, so r_i = 1/2 for every i. The same argument applies to row two. Hence

    <x, Pi^D x> = 1/2   for EVERY one of the eight cells x at D.

## 3. Theorem PF: pairwise product form of dense cells

Fix i not equal to j. In the A_i/A_j isoclinic identification, A_i = |a+><a+| tensor I and A_j = |b+><b+| tensor I, with <a+|b+> not zero, and Pi^D = I tensor |v><v| (v89). Then e_i = a+ tensor g for a second-factor ray g with |<v|g>|^2 = 1/2 by Theorem B. Further e_j = b+ tensor g', and orthogonality <a+|b+><g|g'> = 0 forces g' = g-perp. Inside each plane the row-two cell is the orthogonal complement. Therefore, up to phases,

    e_i = a+ tensor g,     f_i = a+ tensor g-perp,
    e_j = b+ tensor g-perp, f_j = b+ tensor g,

and the other two row-one cells span (a- tensor g, b- tensor g-perp), while the other two row-two cells span (a- tensor g-perp, b- tensor g). The transition entries W_ij = <a+|b+> and W_ji are recovered with modulus sqrt(lambda_ij), consistent with v77.

## 4. Theorem NF: explicit dense normal form of the four planes

In the identification of section 3, write a,b for the Bloch vectors of a+,b+ and n for the unit normal to their plane. Then the four column reflections R_k = 2A_k - I are

    R_i = sigma_a tensor I,       R_j = sigma_b tensor I,
    R_k = (u . sigma) tensor I + t sigma_n tensor Z_v,
    R_l = -((a+b+u) . sigma) tensor I - t sigma_n tensor Z_v,

where u lies in the a-b plane, |u|^2 + t^2 = 1, |a+b+u| = |u|, Z_v = |v><v| - |v-perp><v-perp|, and t is NOT zero.

Proof: the Clifford span of v89 is three-dimensional; Gamma_1,Gamma_2 can be taken in span(sigma_a,sigma_b) tensor I. The third generator anticommutes with both, hence has the form sigma_n tensor T with T a Hermitian unitary (v80 section4). The chirality is +-(I tensor T), so T = +-Z_v by uniqueness of Pi^D. sum R = 0 gives R_l. t = 0 would put all R's in M2 tensor I, i.e. scalar chirality, which v89 excludes. Hence every dense vertex is a MIXED-chirality Clifford frame, the dense counterpart of v80's three-circuit residual.

## 5. Theorem L3: three trails lock chiralities

Let dense D and Y be joined by AT LEAST THREE distinct trails. Then Pi^Y is Pi^D or I-Pi^D. By v89 (ii), otherwise (Pi^D,Pi^Y) is interior-isoclinic, and every trail projection joining them lies in I tensor M2 of that identification. Then at least three of D's four reflections R_k, and hence by sum R = 0 all four, lie in I tensor M2. That would make the chirality at D scalar, contradicting v89. Applications:

* d=2: four trails join D,D', recovering Pi^D' = I-Pi^D.
* Any triple or quadruple column between dense vertices in d=4 or d=5 locks their chiralities.
* In d=3 with exactly two trails per pair, the isoclinic alternative of v89 remains possible. There the two joining planes are I tensor |x><x| and I tensor |x'><x'|, and the other two planes at D are NOT in I tensor M2 (mirror form of section4).

## 6. Scope and frontier

Theorems B, PF, NF and L3 are exact structural results, not closures. Together with v87-v89 they give a complete explicit parametrization of every dense local frame relative to any pair of its columns: a,b,u,t,v and a balanced g. This is the input needed to attack the remaining d in {2,3,4,5} gluings. The d=2 (m in {1,2}), d=3 (m=2), d=4 and d=5 residuals, the all-sparse residuals, other sector placements, minimal-rank-3 and higher-rank families, complementH6, actual100 distinct rays and the SAME TEN-class resolution remain unpaid. All original irreducible10, 4+6 and 5+5 branches remain OPEN.

Imports: v77 DENSE classification, v80 Clifford/third-generator form, v88 Lemma TD, v89 Theorem CH, and elementary finite-dimensional linear algebra. No NR/classifier/Butson/Gaussian/code premise, chosen frame or global tensor WLOG. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S90, retaining ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including the disclosed v29 parallel-intent minor, the v30 dangling-reference defect and the v34 capture retry. Frozen Mainv17/S72/input map/proofs/live151 stay immutable.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
