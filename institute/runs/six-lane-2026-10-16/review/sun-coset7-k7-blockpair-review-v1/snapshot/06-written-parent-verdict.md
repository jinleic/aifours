# Sun k7: written reduction/rules accepted, finite exclusions pending

Recorded at 2026-10-18T14:24:47-07:00.

**CORRECTNESS-ACCEPTED for the written statements and active rule soundness below, with the mandatory overlay. No Sun(7) theorem and no class exclusion are accepted by this verdict.** All six residual classes remain OPEN pending full independent finite coverage checks. The late specification/freeze violation remains an unresolved process MAJOR for the exploratory A/B promotion, not an erased historical event.

## Exact texts and review dispositions

- [Frozen k7 reduction](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/README.md), SHA256 `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1`.
- [General rules](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md), SHA256 `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee`.
- [RPLP/CAP addendum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-addendum-v1.md), SHA256 `fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066`.
- [Coverage contract](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/FINITE-COVERAGE-k7-v1.md), [certificate format](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/CERT-FORMAT-k7-v1.md), as qualified below.
- [Codex written review](sun-coset7-written-v1-codex-v1.note.md), SHA256 `6c9872c4363272243631bbec7b1475333df164517be60fcfb89ea5822d4808ea`: reduction/fibres/CAP ACCEPT; active rules and RPLP AWF; X1 bridge ACCEPT conditionally; finite coverage INCONCLUSIVE. 0 FATAL/MAJOR mathematical findings; 2 MINOR wording findings.
- [Claude written review](sun-coset7-written-v1-claude-v1.note.md), SHA256 `884a4d917ccc6582c24615452ab20064220f02fe71fa58ca1a3bce7acaf1ebcc`: reduction/fibres/RPLP/CAP ACCEPT; general rules and coverage bridge AWF. **1 process MAJOR F-1**, 11 MINORs (A-1; B-1/B-2; C-1/C-2/C-3; D-1/D-2; F-2/F-3/F-4); no mathematical counterexample. Hashes were not independently checked by Claude. Codex matched all nine snapshot hashes.

## Written claims accepted, at exact scope

For arbitrary G and seven pairwise disjoint LEFT cosets of finite-index subgroups (equal subgroups allowed, no cover assumption), suppose every pairwise index gcd is at most6. R0 passes to a finite quotient preserving every relevant index and disjointness. With n_i=2^e_i3^f_i5^h_iw_i, the prime-to30 parts w_i are pairwise coprime and pairwise gcds are in {2,3,4,5,6}. Let C=A_2∩A_3 and E={i:e_i≥2}.

- The complete prime-incidence reduction leaves either at most one5-divisible index, |C|≥4, and all outside vertices uniformly2-only or3-only; or exactly two5-vertices x,y of opposite2/3 roles with the other five vertices in C. Three5-vertices would force all seven pairwise gcds5 and contradict accepted Sun(6).
- Sun(4), Sun(3) and the exact accepted k5 proof-v4 Prop4.5 eliminate the |C|=4 branches. The vertex-fibre arguments D2 and D2′ eliminate the displayed uniform-gcd2 branches. The exact remaining six classes are **K7, K6.2*, K6.3, K5.2*, K5.3, KII**, with gcd matrices in the frozen reduction. No common-factor/Core6 template or bounded cofactor is assumed.
- Partial D3 excludes only K6.3 patterns with C∩E empty and at least four displayed α_di=2; it does not eliminate the K6.3 class.
- Active triangle T, containment/packing K/K1/K2, grid/Bonferroni P, VFC and RPLP rules are sound necessary conditions with every stated universal subset/q condition. CAP preserves all active quantities using capped profiles(min(e,4),min(f,2),min(h,2)) under the explicit pairwise-min/coprime hypotheses; the five-vertex control universes have their own hypotheses in addendumA3.
- Every K5.3 configuration contains a five-coset X1 tuple (3r_1,3r_2,6r_3,6r_4,6r_5), r_1,r_2 odd and all r_i pairwise coprime. **If** a complete independent X1 exclusion is accepted, it excludes K5.3. No Menon theorem or M-S Lemma4.6 is imported.

These are written structural results, not an independent claim of novelty or a completed k7 gate. FH is expressly UNUSED and is not accepted as an executable exclusion rule.

## Independent parent derivation

The parent read the full frozen reduction/rules and addendum, independently checked the prime-incidence split, fibre construction, D2/D2′/D3 arithmetic and the new RPLP/dual/CAP bridge, in addition to the separately authored written audit.

**Reduction.** Pairwise gcd6 is exactly membership of both endpoints in C; a5-edge cannot also share2 or3. At least three5-vertices force one without2/3, hence every vertex is5-divisible; every pair then has gcd5, violating Sun(6). Two5-vertices must have opposite2/3 roles to meet the other five, forcing those five into C. At most one5-vertex means every five vertices need a gcd6 pair by Sun(5), so |C|≥4 and no mixed2-only/3-only outside vertices are possible. Three3-only vertices with one C violate Sun(4). For three2-only vertices, Sun(3) forces all three into E. Choose a C vertex with e=1; dividing that index by2 and the other three by4 gives the exact pairwise-coprime tuple of the accepted Prop4.5, including unbounded remaining valuations.

**Fibre construction and counts.** Normalize g_v=1. D_j=U_vg_jU_j is disjoint from X_j=U_vU_j, with μ(D_j)=q_j/g_vj and1≤q_j≤g_vj−α_vj. Every right coset R=U_vy inside D_j meets g_jU_j. Choose w_j in that intersection; its piece is (U_v∩w_jU_jw_j^−1)w_j. Common right translation by y^−1 followed by inversion gives disjoint LEFT cosets in U_v, of index d_j=q_jn_j/g_vj. Thus every subset of at least two simultaneous pieces obeys Sun(t), t≤6. D_j and X_j are left-U_v-invariant and every D_j avoids U_v, so the union measure is strictly below1.

D2 has six masses1/2, with allowed multiplicity≤3 (local gcds3); the strict sum is contradicted. For D2′, q=1,2 gives an isolated D-piece and C union at least5/6, so total≥1/4+5/6>1; q=3 gives13/4>3 at multiplicity≤3. In partial D3, |Q|≤2, weights1/4 on q=2 vertices and1/2 otherwise satisfy every hereditary allowed set; weighted mass is6·1/6=1, again contradicting strictness. No Sun(7) or minimal-order assumption enters these active arguments.

**K/P.** The normalized packing sets g_iU_iU_v are disjoint under the stated pairwise product-containment disjuncts and avoid U_v; inversion supplies the equivalent orientation. The triangle τ_min divisibility uses the opposite vertex's ℓ. At centre v, μ(X_j∩X_k) lies on the grid1/gcd(n_v,I_jk); lower bounds round upward and upper bounds downward, subtracting one step exactly when equality would force a K2-barred containment. With equal measures, both containment directions must be allowed. Bonferroni uses intersection upper bounds with the correct subtracting sign.

**RPLP.** Right-U_v-coset types(A,S) satisfy S⊆A, allowed local indices and forced complement implications. Every X_j contains U_v, so total μ(∪Y_j)<1. The forced condition τ_min*g_va≥lcm(g_va,g_vb)*α_ab*α_va gives μ(U_v(U_a∩U_b))≥μ(X_a), while inclusion gives the reverse inequality. Equality forces X_a⊆X_b, hence b∈A⇒a∈A. For every q, free a/b dual variables multiply equalities; u,l≥0 multiply pair bounds with signs−u*yhi+l*ylo. Every column inequality≤1 gives actual total mass≥Obj. Obj≥1 already contradicts the strict total<1. Empty S columns remain included, and all allowed subsets/all q are mandatory. Farkas is used only for the CLOSED E1/E2/B relaxation, not strict TOT.

**CAP.** Pairwise valuations are bounded by2 for2 and1 for3/5, so at most one high vertex per prime exists. Caps4,2,2 preserve g/γ, every α-detectable ℓ-divisibility, the competing argument in gcd(n_v,I_jk), and local-index gcds with q≤5. A truncated high index either already exceeds the other bounded argument or is not the minimum. Pairwise-coprime prime-to30 factors cannot enter those gcds through α/q. RPLP's pair bounds, forced tests, allowed sets and columns are rational functions of these preserved quantities. This is not a claim about unspecified future FH domains.

## Mandatory overlay and disposition of all findings

1. **A-1:** coset representatives and5-valuations use different symbols; call the latter h_i. The profile's third coordinate is the5-valuation, never a group element.
2. **B-1:** the D2/D2′ citation is rules§3, not§R.
3. **B-2/C-2:** the explicit fibre/inversion and packing proofs above supply the previously citation-only steps. Their hypotheses remain pairwise disjointness and finite indices.
4. **C-1/C-3, Codex singleton finding:** only the active T/K/K1/K2/P/VFC/RPLP rules are pattern predicates killing every configuration. Subfamily pair tests require2≤|T|≤6. FH/L5's7-piece use needs a proper subgroup in a least-order counterexample and is UNUSED.
5. **D-1, Codex Farkas finding:** Farkas scaling applies to x≥0 with E1/E2/B, EXCLUDING strictTOT. The direct P-certificate weak-duality proof is unchanged. The worker's [wording erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-erratum-v1.md) preserves the original texts and makes these two repairs; it is not a new certificate or replay.
6. **D-2:** mathematics-to-code correspondence is not inferred. Independent checkers are written from the definitions, not imported producer functions.
7. **F-2:** “equivalent” in the coverage format means a sufficient independent pruning criterion. A checker must either mirror producer pruning exactly or define independently uncovered leaves as a subset of the reported survivors, while proving its own full universe coverage. Recompute all usable neighbour subsets and verify every claimed closure.
8. **F-3:** no node prefixes were stored. Full independent tree re-walk is mandatory; leaf records alone do not prove coverage.
9. **F-4:** the original format defines X1/K52/KII and controls, not K62/K63/K7. No later-universe run is credited without its separately frozen specification and parent permission.

**Process MAJOR F-1 remains unresolved for A/B promotion.** The certificate format13:38:43 and RPLP addendum14:00:41 postdate A/B starts. They are late specifications, never retroactive preregistration. Independent full replay from the now-frozen definitions can establish mathematical coverage; it cannot erase the original process violation. At this verdict no such complete result is supplied or inferred, and every class remains OPEN.

## Imports and limits

Sun(2), Zhu's Sun(3)/(4), locally accepted Sun(5) and Sun(6), the exact proved Prop4.5 scope, and elementary finite group cardinalities. The locally accepted Sun(5) proof is used, not Gong's unread historical proof. No M-S Lemma4.6, Menon result, producer count, engine behavior, native solver, numerical LP outcome, minimal-counterexample frame or Sun(7) assumption is a premise of the active written rules. No Lean, Comparator, human review, novelty claim or publication.
