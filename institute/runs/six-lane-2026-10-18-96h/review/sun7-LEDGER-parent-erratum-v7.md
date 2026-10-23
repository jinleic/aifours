# Closed ledger parent erratum v7 — ARED N17–N27 findings m1–m4

Recorded 2026-10-20T05:55:45-0700 (`/bin/date`). Disposes ARED review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-LEDGER-ARED-claude-v1.prompt.note.md (dc18fa1d1692f993d0963b6efb53f5c71c623723bbf3eaffa40e5ed8c6ccdb82):0F/0M/4m, no correctness defect. Read after ledger errata v2–v6 (v6 still at its separate review gate).

1. **m1 — R0 row.** Drop N17 from R01's R0 consumer list: N17 is stated in a CE, hence finite by definition. S1/S2 ambient group is "the CE's G, supplied by R0 at N23". R0 is consumed by N23/N59, not internally by N17.
2. **m2 — direct elementary edges.** Add N02 to N18, N19 and N21 input cells (deletion and integer alpha range). R05's consumer list means exactly the nodes whose input cell lists N02; N23 is not one of them. New cells: N18=N01,N02,N15; N19=N01,N02,N15; N21=N01,N02,N11,N15. No new assumption, backward edge or cycle.
3. **m3 — N26's self-contained inversion proof is supplied.** K52-W LF71–79 explicitly proves actual INV: inversion is a bijection, conjugation preserves indices, g_j*U_j*=(g_jU_j)^−1 are disjoint left cosets; after conjugation, alpha* comes from U_i∩hU_jh^−1. The distinct (U_i,U_j) double cosets U_iU_j and U_ihU_j are disjoint; their normalised sizes are alpha/g and alpha*/g, so alpha+alpha*≤g. Parent erratum item4 (literal below) explicitly labels LF52/LF187 "re-proved here; VFC not used", with LF189 also using LF83. Thus R08 discharges INV with **K52 LF71–79 + K52 parent erratum item4**. No N13/N11/VFC or Sun5/6 edge is added to N26.
4. **m4 — missing governing texts supplied and compared.** Parent read every item1–5 of both errata below against the displayed declarations/scopes. K52 item2 makes explicit the exact gcd matrix in arbitrary G, not an already-formed finite CE; item3 permits equal trace subgroups under Zhu Sun4; item4 explicitly supplies the re-proved INV scope. KII item1 makes SHAPE conditional on an actual given configuration, not numerical-data realizability; item2's Sun2 proof is elementary; items3–5 correct counts/notation/zero-weight reasoning. None introduces any new imported theorem or alters the exact N26/N27 exclusion scopes. Their literal primary import tables, read with these errata, match N26/N27's existing providers.

## Literal K52 parent erratum (a21ab9a0ec085d85e01904e81f23ab30249227d2537a8436b9387111a7a37852)
00001|# K52-W parent erratum v1
00002|
00003|Recorded 2026-10-19T17:40:19-0700 (`/bin/date`). Applies to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k52-written/K52-W-v1.md` SHA256 `c9c5ecbf106e7a9744558837b79567bd9ec3ad2988a562f5e15462b92a3a8e5d`; original unchanged. Disposes of Claude's four MINOR findings and three uncounted nits; no mathematical conclusion or weight changes.
00004|
00005|1. LF78: write U_i h U_j=(U_i · hU_jh^-1)h. Hence its cardinality is |U_i||U_j|/|U_i∩hU_jh^-1| = |G|[G:U_i∩hU_jh^-1]/(n_i n_j). Translation permits the subgroup product formula.
00006|2. LF19–23 and LF175–176: the labelled index tuple satisfies README LF94 **including its gcd-matrix column**. This is a numerical condition in arbitrary G, not an assumption that README's finite-G CE has already been formed. Equivalently the pairwise gcd bound <=6, 4|n_d, 12|n_s, v2(n_o)=1 and 3 not dividing n_d force the displayed matrix. The finite reduction is proved at LF59–61.
00007|3. LF51 and its use at LF93: Sun(4) permits equal subgroups; only the four left cosets must be pairwise disjoint. This is the accepted classical import's literal scope.
00008|4. LF52/LF187: “INV(a) and the inequality alpha+alpha*<=g (erratum E7), re-proved here; VFC not used.” LF189 additionally depends on the index formula LF83.
00009|5. Notation: g_ij means gcd(n_i,n_j); the two ordinary vertices at LF140 may be named u,w, not the apex-v variable. Sun(2) at LF92 uses index divisibility inside U_v and the coset-intersection criterion. “Shared markers” means distinct higher prime-power parts may occur on the same vertex; their exponents remain unbounded. Name the raised LF136 weighting U-prime, including the B1 table's first row.

## Literal KII parent erratum (7c38c327b0c4d11d8b1692d281c75e3533e3891f5a1ecd819645ce57fb0232c3)
00001|# KII-W parent erratum v1
00002|
00003|Recorded 2026-10-19T17:52:52-0700 (`/bin/date`). Applies to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/kii-written/KII-W-v1.md` SHA256 `b25d4274d09b24b7eaa346d5287af95cee65f99ae4939c4bd32f20eda2eb5c03`; original immutable. Resolves Codex3 MINOR and Claude5 MINOR findings (overlap counted per review, not as eight unique defects). No theorem or weighting changes.
00004|
00005|1. SHAPE LF38 begins “For a given pairwise-disjoint coset configuration as in section0, its labelled index tuple has all pairwise gcds<=6 and a=2 iff …”. LF53 says “the given configuration is a CE with a=2”, not that numerical data imply realizability. At LF51 note gcd(r_y,r_c)<=2 is1 because r_y is odd. R0 first reduces arbitrary G to finite G.
00006|2. The Sun(2) justification at LF43–44 is the argument of LF86–88 with U_v replaced by G, finite after R0; it does not depend on SHAPE or KII exclusion.
00007|3. LF95: **six** other vertices, consisting of x,y and four C-neighbours. LF130 and LF167 concern the **four C-entries** Phi_cq, q in C minus{c}; LemmaB's unequal entry must be a C-entry, not the always1 x-entry. LF164/packageLF19 reads “every permitted multiplier assignment”, not “both values of every multiplier”.
00008|4. Fibre counts t_j, distinguished marker t, core N, plain count N, intersection index I_ij and local label I are distinct notation. Use m_j for fibre counts and N_pl for the MainLemma plain count if ambiguity arises.
00009|5. “Compatible” means local-index gcd>=2. M2 sets containing y lie in{x,y}. M4c gives y weight0, so{x,y,i*} weighs at most1; zero-weight additions cannot cure a forbidden subset of positive-weight vertices.


This is local ARED closure only, not global graph/final join or full Sun7 acceptance. Historical StageB/F-1 unchanged.
