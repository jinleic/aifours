# Sun k7: LFC/INV and two unmarked subclasses accepted

Recorded at 2026-10-18T23:41:29-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** The written LFC, INV and ROW-U lemmas hold with the exact hypotheses below. They exclude all-unmarked K7 and fully-unmarked K6.3 over arbitrary groups with finite-index subgroups. **Sun(7) remains open:** marked K7, marked K6.3 and K6.2* remain. No new breakthrough gate or novelty claim is recorded.

## Text and referee findings

- [Candidate](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md), SHA256 `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`.
- [Mandatory erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md), SHA256 `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`. The parent read it completely; it changes wording/import accounting only, not the theorem.
- [Codex referee](sun7-lfc-inv-codex-v1.prompt.stdout.txt): ACCEPT, no FATAL/MAJOR, one editorial MINOR. Observed CLI model gpt-6.1-sol, effort max, read-only; [receipt](sun7-lfc-inv-codex-v1.prompt.receipt.json).
- [Claude referee](sun7-lfc-inv-claude-v1.prompt.note.md): ACCEPT-WITH-FIXES, no FATAL/MAJOR, nine MINORs. Observed CLI model claude-opus-5-5, effort max, no tools; [receipt](sun7-lfc-inv-claude-v1.prompt.receipt.json).

Both reviews apply to the exact embedded candidate. Claude did not independently hash the file. The parent pinned it before review and verified all erratum dispositions.

## Accepted statements and parent derivation

1. **LFC, k≤7.** For disjoint left cosets and a fixed vertex v, lambda_j=[U_v:U_v∩U_j]=n_j alpha_vj/g_vj, and g_jU_j meets t_j=n_v alpha_vj/g_vj left U_v-fibres. A common point p writes each intersection as p(U_j∩U_v); after translating into U_v these are disjoint left cosets with those lambda indices. At most six pieces share any nonexclusive fibre. Sun(t),2≤t≤6, applied to every subfamily gives the hereditary allowed-set condition. Summing feasible weights over the n_v−1 fibres gives sum y_j alpha_vj/g_vj≤1−1/n_v<1. No conjugation is missing from this left-fibre argument.
2. **INV.** Invert each coset and write it as g_i^−1(g_iU_i g_i^−1). This preserves disjointness and the labelled index tuple. With h=g_v^−1g_j, the double coset U_v h U_j has measure alpha*_vj/g_vj. It is disjoint from U_vU_j, so alpha_vj+alpha*_vj≤g_vj. The original VFC(V1) defines q by that same double-coset measure, hence q=alpha*. The parent directly read VFC(V1) and the index-defined class definitions; same-class assertions do not extend to classes defined using additional unpreserved data.
3. **ROW-U.** In K7, a vertex with six unmarked neighbours has only alpha∈{1,2,4}, at most one 1 and at least three 4s. Pairwise-coprime w_j prime to30 reduce fibre gcds to gcds of alpha≤5. The R1/R24/R3/R5 feasible weights in the candidate cover every hereditary subset; for N entries of R1∪R24 the value is at least min(N,4). Every excluded row gives a value≥6, contradicting LFC.
4. **K7-M0.** If all seven indices are 6w_i, with w_i pairwise coprime and prime to30, ROW-U applies globally to alpha and alpha*. Each vertex has at least three alpha=4 and at least three alpha*=4 edges, disjoint by INV. Thus exactly three alpha=4 edges meet every vertex. Symmetry would give a 3-regular graph on seven vertices, with odd degree sum21, impossible. This excludes the previously open all-2 singleton pattern and the entire unmarked Q24 branch, not only a bounded range.
5. **K63-U0.** Six indices 6w_i and one 3w_d, all w pairwise coprime and prime to30, cannot occur. If some C–d alpha=1, the d fibre contributes1/3 and the five other C-neighbours contribute at least4/6, contradicting LFC. Therefore all C–d alpha=2. At d the six local indices are4w_i; weights1/4 give total1, another contradiction.
6. **Arbitrary groups.** The intersection of the finitely many subgroup cores is normal, finite-index and contained in every subgroup. The quotient preserves indices, intersections and coset disjointness; normality also preserves the conjugated intersections in INV. Therefore the finite arguments lift to the stated arbitrary-group scopes.

## Exact controls, not load-bearing computation

The [parent-owned control](sun7-lfc-inv-parent-check-v1/result.json) uses only standard-library exact fractions/permutations, importing no worker code. It checked all126 five-neighbour multisets and210 six-neighbour multisets; every proposed weight was feasible, and all203 six-row types violating ROW-U had objective≥6. The five-row minimum was4. All285 disjoint S3 coset configurations passed2066 directed-pair LFC/INV checks. An infeasible weight mutation gave7/6>1, and an omitted-conjugation mutation was exposed by a nonnormal S3 example with alpha=1,alpha*=2. Runtime0.146s, normal exit0. These finite aids do not prove the general theorem; the written arguments do.

## Finding dispositions and remaining limits

Erratum E1 addresses Codex MINOR and Claude m1/m2 (product formula, alpha integrality/bounds); E2 m3 (Sun2); E3 m4 (definition/fibre exclusion); E4 m5 (V,p_j notation); E5 m6 (K63 quotient lift); E6 m7 (index-defined classes); E7 m8 (direct VFC definition check and navigation-only old cross-references); E8 m9 (uniform value bound). All nine are applied with no new load-bearing premise.

Imports include accepted Sun(5) and Sun(6), themselves computer-assisted and model-reviewed; no Sun(7) is used inside any subgroup. This is written mathematics, not Lean or human peer review. Priority/significance remain unassessed for this exact delta. Exploratory worker marked-profile probes, including incomplete searches and a failed PID capture, are **not premises**. K5.3 is separately excluded by [the qualified StageA disposition](sun7-stageA-K53-parent-verdict-v1.md); its single-checker and permanent F-1 qualifications remain unchanged.
