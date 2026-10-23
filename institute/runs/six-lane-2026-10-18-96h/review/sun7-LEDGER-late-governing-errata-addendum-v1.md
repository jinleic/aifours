# Late governing errata addendum for remaining local closure packets

Recorded 2026-10-20T06:12:18-0700 (`/bin/date`). Applies to the not-yet-launched BROW, BK63, CRICH, CA2 and CK62 second-family packets, which were frozen before these parent errata. Their own scopes and source records are unchanged. Read these governing texts first; they change no proof step or class scope and add no imported theorem.

- Errata v5 (AROOT): N01–N08 bookkeeping; deletion and R0-conjugation one-line proofs; N04/N05 bodies end at their theorems.
- Errata v6 (AFIBRE, accepted with v8 by sun7-DEFORDER-parent-verdict-v1.md): stable IDs with explicit topological order N01–N08,N15,N09–N14,N16–N59; DEF→INV/ROWU and N02→F7/ROWU edges; DEF exports only definitions, P0/P1, class and case predicates with conditional matrices; ROWU-deg/E8 abstract exports only (consumers verify their own gcd hypotheses); RW row alignment.
- Erratum v7 (ARED): N02 edges for N18/N19/N21, R0 row, K52 self-contained INV proof, K52/KII parent errata items.
- Erratum v8: (I)-2/(I)-3/(II) predicates/matrices and overlay A-1 retained in DEF; R16 literal range; N16 body entries retained outside RK7/ADD replacement.

In particular, any statement in your packet that "every input number is smaller" must be read against the explicit order above, not numeric order. Owned consumers that use ROWU-deg/E8 must verify the abstract gcd hypothesis themselves (it is no longer an N14 export of their instance).

## Erratum v5
00001|# Closed ledger parent erratum v5 — AROOT (N01–N08) second-family findings m1–m6
00002|
00003|Recorded 2026-10-20T04:56:26-0700 (`/bin/date`). Disposes Claude AROOT review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-LEDGER-AROOT-claude-v1.prompt.note.md (919be03168a73f9ddd00fd7006063af0a2f2eb5b040c490f2d0b74de44690a11): 0F/0M/6m, all completeness/bookkeeping. Read after LEDGER-v1, worker erratum v1 and parent errata v2–v4. No exported statement, proof step or node order changes; every edge stays forward.
00004|
00005|1. **m1 — node bodies end at the theorems.** N04's body is C5W LF1–120 (theorem LF110–120); N05's is C56W LF1–120. C5W LF121–150 (conditional Sun(5) corollary, needing Prop4.5/R1/Zhu Sun(4)) and C56W LF121–141 (provenance) are unconsumed text with no node; S5W/S6W replace them. No N04/N05 edge to N06/N07 exists.
00006|2. **m2 — N02 root body.** N02's LE body is LE LF14–18 and LF23–24 only. LE LF19 (K7/K63-U0 instances) is owned by those consumers under their own gcd hypotheses; LE LF25's "granted Sun(t), t≤6 import" attribution is superseded provenance (CR LF64): L0.3/L0.6 have complete elementary proofs at S56 LF40–42, LF47–48, so N02 carries no Sun(5)/(6) premise.
00007|3. **m3 — deletion export.** N02 exports deletion with this one-line proof: a subfamily of a pairwise-disjoint family of left cosets is pairwise disjoint, with the same subgroups, ambient group and indices.
00008|4. **m4 — R0 conjugated intersections.** Add to N03: if N⊴G and N≤U_j then N=xNx^−1≤xU_jx^−1, so N≤U_i∩xU_jx^−1 when also N≤U_i, and (U_i∩xU_jx^−1)/N = (U_i/N)∩x̄(U_j/N)x̄^−1 with the same index in G and G/N (correspondence theorem). With R0's core N = intersection of the cores of all U_j, every conjugated intersection index is preserved.
00009|5. **m5 — rows/edges.** (i) N06 rows cell: add F01. (ii) N08's optional N07 edge is declared at S56 LF140–141 with S56 parent erratum v2 LF6 (S56 LF158/LF160 list the main route without S5W). (iii) Mark N02→N03 as (cons.): R0's proof uses Lagrange and cores only (S56 LF144–147). (iv) Replace F01's consumer list: elementary facts (N02) are consumed exactly by nodes listing N02 in section 3; R0 (N03) exactly by nodes listing N03; no node consumes itself; N04/N05 are finite-group theorems consuming N02 (and N01) only.
00010|6. **m6 — N01 sources.** Define key TR = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-sun7-closed-interface-ledger-transition-v1.json (50ba9d9c2aec544983a246bd435221b6d7a74a608fc81d320fa2af7d9a948cd1). N01's literal scope source is C56W parent erratum v2 LF7 (/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun6-C56W-parent-erratum-v2.md, 7ff97a8a63a9dc5200dba177e968dd55718c831a24cde3cad7bda66118c34706): any group, k=3 or 4, pairwise-disjoint left cosets of finite-index subgroups, equal subgroups allowed. Zhu's proof/provenance is not certified here.
00011|
00012|Local AROOT closure is VALID relative to named boundaries after these amendments (second-family 0F/0M). Other packets, the global graph and the final join remain separate gates; full Sun7 UNACCEPTED.

## Erratum v6
00001|# Closed ledger parent erratum v6 — AFIBRE definitions, order and exact exports (candidate repair)
00002|
00003|Recorded 2026-10-20T05:36:54-0700 (`/bin/date`). Read after parent errata v2–v5. Responds to AFIBRE 0F/1M/4m. This is **CANDIDATE_UNVERIFIED** until the separate repair gate. Stable node IDs do not change; no class theorem is weakened or enlarged.
00004|
00005|## 1. MAJ-1 — DEF before INV/ROWU; explicit order replaces numeric order
00006|N15 DEF has only N02 as input. Place it immediately after N08. The proposed topological order is **N01,N02,…,N08,N15,N09,N10,N11,N12,N13,N14,N16,N17,…,N59**. All earlier assertions "input number smaller" or "N01,…,N59 is the order" are withdrawn and replaced by "every input precedes its consumer in this explicit order". The graph remains acyclic: moving N15 earlier crosses only N09–N14, none of which is an input of N15. Existing consumers of N15 numbered≥16 remain after it.
00007|
00008|Add N15 to N13 and N14 inputs. In INV(a) read "same profiles" as "same labelled index tuple, hence every index-determined invariant"; a profile vocabulary is supplied by its consumer (e.g. N16), not imported backward into N13. Actual inversion preserves the n_i, so every pure index/class/marking predicate is preserved (E6).
00009|
00010|## 2. MIN-3 — exact DEF export, with KII proof
00011|N15 exports only: finite seven-coset CE and its labelled index decomposition n_i=2^e_i 3^f_i 5^h_i w_i with gcd(w_i,30)=1; A_2/A_3/A_5, C,E,a,D; P0/P1 and their elementary proofs (README LF33–52); the six class PREDICATES (README LF89–96, without the preceding exhaustiveness assertion); and their conditional gcd matrices. In K7, "unmarked" means e_i=f_i=1,h_i=0, i.e. n_i=6w_i. No R0 clause, R1(7), Sun theorem, elimination or "every CE belongs to the six classes" is part of DEF; those belong to N03/N17/N23.
00012|
00013|**KII matrix from P0/P1 only (no R1(7)(II)).** Assume a=2 and write A_5={x,y}. There are five other vertices j. P0(a) and P1(i) force each of x,y to lie in A_2∪A_3: otherwise its pair with any j outside A_5 would have no common2/3/5 prime, contradicting gcd≥2. P1(ii) permits at most one member of A_5 in A_2 and at most one in A_3. Therefore, up to names, x∈A_2∖A_3 and y∈A_3∖A_2; neither can belong to both (then the other would belong to neither). For any j outside A_5, P1(i) on x,j forces j∈A_2 and on y,j forces j∈A_3. Thus the other five vertices are exactly C. Now P1 gives C–C gcd6, x–y gcd5, y–C gcd3, and x–j gcd4 iff both x,j∈E (otherwise2). This is precisely the KII predicate/matrix, with no exhaustiveness or Sun input. All other per-predicate matrices follow immediately from P1(i)/(iii).
00014|
00015|## 3. MIN-1 — explicit edge cells
00016|Add N02 to N10 (F7 directly uses L0.3) and to N14 (E1/L0.3). R05's consumer list includes N16. Label N13's VFC use **(V1) only** (the q definition); R14's (V2)–(V4) attribution is not its premise. New inputs:
00017|- N10: N02,N09.
00018|- N13: N02,N03(cons.),N11,N15.
00019|- N14: N02,N12,N15.
00020|
00021|## 4. MIN-2 — abstract ROWU transfer only
00022|N14 exports ROW-U-deg only at ME LF27–30 (abstract gcd hypothesis, standard weights, value bound and conclusions(i)–(iii)), and E8 only at LE LF71–78. ME LF26 and LF31–32 (M1/ROW1 verification) and LE LF79–80 (K63-U0 Step1 instance) are owned by the respective consumers, not N14's proof body. Each consumer checks the abstract gcd hypothesis for its own labels. No ROW1/M1 input or false cycle is added to N14.
00023|
00024|## 5. MIN-4 — RW literal alignment
00025|N16 export is RW LF10–23 **read only with RWE(3eb93c473858fb34b78802ce49626700db90e2176301a94ca20f90078c5d663c) and RWV(1bc8080a3cdd7ec87e62bdc45b62f4683f2ef0b55809016e64415068cbf32ded)**. Body/discharge ranges: RK7 LF19–24,LF26–28,LF30,LF40–49; LF70 for non-L5 quantities only,LF71–75;LF80 first sentence only. ADD LF21–110 (W2 governs LF106),LF124 first two sentences,LF128–139,LF143–148,LF155. No excluded range is an import. R12 retains only WV LF38/LF48's packing proof (drop the alternative S56 L3/K2 route). R18 follows the just-stated RWE ranges. F20's "no operative consumer" parenthetical applies only to K/P/RPLP: N16's capping export DOES feed N57 through CI62. RW's R0 clause is consumer-side; RWV's theorem takes finite input.
00026|
00027|No other incoming edge changes. This proposal does not accept AFIBRE closure, full Sun7 or any runtime.

## Erratum v7
00001|# Closed ledger parent erratum v7 — ARED N17–N27 findings m1–m4
00002|
00003|Recorded 2026-10-20T05:55:45-0700 (`/bin/date`). Disposes ARED review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-LEDGER-ARED-claude-v1.prompt.note.md (dc18fa1d1692f993d0963b6efb53f5c71c623723bbf3eaffa40e5ed8c6ccdb82):0F/0M/4m, no correctness defect. Read after ledger errata v2–v6 (v6 still at its separate review gate).
00004|
00005|1. **m1 — R0 row.** Drop N17 from R01's R0 consumer list: N17 is stated in a CE, hence finite by definition. S1/S2 ambient group is "the CE's G, supplied by R0 at N23". R0 is consumed by N23/N59, not internally by N17.
00006|2. **m2 — direct elementary edges.** Add N02 to N18, N19 and N21 input cells (deletion and integer alpha range). R05's consumer list means exactly the nodes whose input cell lists N02; N23 is not one of them. New cells: N18=N01,N02,N15; N19=N01,N02,N15; N21=N01,N02,N11,N15. No new assumption, backward edge or cycle.
00007|3. **m3 — N26's self-contained inversion proof is supplied.** K52-W LF71–79 explicitly proves actual INV: inversion is a bijection, conjugation preserves indices, g_j*U_j*=(g_jU_j)^−1 are disjoint left cosets; after conjugation, alpha* comes from U_i∩hU_jh^−1. The distinct (U_i,U_j) double cosets U_iU_j and U_ihU_j are disjoint; their normalised sizes are alpha/g and alpha*/g, so alpha+alpha*≤g. Parent erratum item4 (literal below) explicitly labels LF52/LF187 "re-proved here; VFC not used", with LF189 also using LF83. Thus R08 discharges INV with **K52 LF71–79 + K52 parent erratum item4**. No N13/N11/VFC or Sun5/6 edge is added to N26.
00008|4. **m4 — missing governing texts supplied and compared.** Parent read every item1–5 of both errata below against the displayed declarations/scopes. K52 item2 makes explicit the exact gcd matrix in arbitrary G, not an already-formed finite CE; item3 permits equal trace subgroups under Zhu Sun4; item4 explicitly supplies the re-proved INV scope. KII item1 makes SHAPE conditional on an actual given configuration, not numerical-data realizability; item2's Sun2 proof is elementary; items3–5 correct counts/notation/zero-weight reasoning. None introduces any new imported theorem or alters the exact N26/N27 exclusion scopes. Their literal primary import tables, read with these errata, match N26/N27's existing providers.
00009|
00010|## Literal K52 parent erratum (a21ab9a0ec085d85e01904e81f23ab30249227d2537a8436b9387111a7a37852)
00011|00001|# K52-W parent erratum v1
00012|00002|
00013|00003|Recorded 2026-10-19T17:40:19-0700 (`/bin/date`). Applies to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k52-written/K52-W-v1.md` SHA256 `c9c5ecbf106e7a9744558837b79567bd9ec3ad2988a562f5e15462b92a3a8e5d`; original unchanged. Disposes of Claude's four MINOR findings and three uncounted nits; no mathematical conclusion or weight changes.
00014|00004|
00015|00005|1. LF78: write U_i h U_j=(U_i · hU_jh^-1)h. Hence its cardinality is |U_i||U_j|/|U_i∩hU_jh^-1| = |G|[G:U_i∩hU_jh^-1]/(n_i n_j). Translation permits the subgroup product formula.
00016|00006|2. LF19–23 and LF175–176: the labelled index tuple satisfies README LF94 **including its gcd-matrix column**. This is a numerical condition in arbitrary G, not an assumption that README's finite-G CE has already been formed. Equivalently the pairwise gcd bound <=6, 4|n_d, 12|n_s, v2(n_o)=1 and 3 not dividing n_d force the displayed matrix. The finite reduction is proved at LF59–61.
00017|00007|3. LF51 and its use at LF93: Sun(4) permits equal subgroups; only the four left cosets must be pairwise disjoint. This is the accepted classical import's literal scope.
00018|00008|4. LF52/LF187: “INV(a) and the inequality alpha+alpha*<=g (erratum E7), re-proved here; VFC not used.” LF189 additionally depends on the index formula LF83.
00019|00009|5. Notation: g_ij means gcd(n_i,n_j); the two ordinary vertices at LF140 may be named u,w, not the apex-v variable. Sun(2) at LF92 uses index divisibility inside U_v and the coset-intersection criterion. “Shared markers” means distinct higher prime-power parts may occur on the same vertex; their exponents remain unbounded. Name the raised LF136 weighting U-prime, including the B1 table's first row.
00020|
00021|## Literal KII parent erratum (7c38c327b0c4d11d8b1692d281c75e3533e3891f5a1ecd819645ce57fb0232c3)
00022|00001|# KII-W parent erratum v1
00023|00002|
00024|00003|Recorded 2026-10-19T17:52:52-0700 (`/bin/date`). Applies to `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/kii-written/KII-W-v1.md` SHA256 `b25d4274d09b24b7eaa346d5287af95cee65f99ae4939c4bd32f20eda2eb5c03`; original immutable. Resolves Codex3 MINOR and Claude5 MINOR findings (overlap counted per review, not as eight unique defects). No theorem or weighting changes.
00025|00004|
00026|00005|1. SHAPE LF38 begins “For a given pairwise-disjoint coset configuration as in section0, its labelled index tuple has all pairwise gcds<=6 and a=2 iff …”. LF53 says “the given configuration is a CE with a=2”, not that numerical data imply realizability. At LF51 note gcd(r_y,r_c)<=2 is1 because r_y is odd. R0 first reduces arbitrary G to finite G.
00027|00006|2. The Sun(2) justification at LF43–44 is the argument of LF86–88 with U_v replaced by G, finite after R0; it does not depend on SHAPE or KII exclusion.
00028|00007|3. LF95: **six** other vertices, consisting of x,y and four C-neighbours. LF130 and LF167 concern the **four C-entries** Phi_cq, q in C minus{c}; LemmaB's unequal entry must be a C-entry, not the always1 x-entry. LF164/packageLF19 reads “every permitted multiplier assignment”, not “both values of every multiplier”.
00029|00008|4. Fibre counts t_j, distinguished marker t, core N, plain count N, intersection index I_ij and local label I are distinct notation. Use m_j for fibre counts and N_pl for the MainLemma plain count if ambiguity arises.
00030|00009|5. “Compatible” means local-index gcd>=2. M2 sets containing y lie in{x,y}. M4c gives y weight0, so{x,y,i*} weighs at most1; zero-weight additions cannot cure a forbidden subset of positive-weight vertices.
00031|
00032|
00033|This is local ARED closure only, not global graph/final join or full Sun7 acceptance. Historical StageB/F-1 unchanged.

## Erratum v8
00001|# Closed ledger parent erratum v8 — DEFORDER second-family m-A/m-B and notes
00002|
00003|Recorded 2026-10-20T06:11:59-0700 (`/bin/date`). Disposes Claude DEFORDER review /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-DEFORDER-claude-v1.prompt.note.md (3cc53cc28751b9fd59186944969fb4233dd778108983694a5ccd593616479c8f):0F/0M/2m. Codex DEFORDER (beb165cd9bf091caef544e36915461545620b3853bd1408ddb90e7133baeeeed) was0F/0M/0m. Read after candidate erratum v6. No proof or exported theorem changes.
00004|
00005|1. **m-A — N15 conditional case matrices re-exported.** Add to N15's export the following PREDICATES and conditional matrices, proved from P0/P1 only (no R1(7), Sun(t≥3) or exhaustiveness):
00006|   - (I)-2 := a≤1 and D⊆A_2∖A_3; (I)-3 := a≤1 and D⊆A_3∖A_2; (II) := a=2. (The |C|≥4 clause of R1(7)(I) is a CONSEQUENCE proved at N17, not part of these predicates.)
00007|   - Under (I)-2: C–C gcd6 (P1(iii)); for d∈D and any j≠d, the 5-part cannot be shared (a≤1), 3 is not shared (d∉A_3), and P_dj≠∅ (P1(i)); hence P_dj={2} and gcd is 2 or 4, 4 iff d,j∈E (P1(i)). Under (I)-3 symmetrically P_dj={3} and gcd3. Under (II), erratum v6's KII derivation gives the README LF67/LF96 matrix.
00008|   Thus README LF67's matrices are N15 exports read as these conditional statements; N18–N22, which cite "(I) type 2/3" vocabulary, receive them from N15. Their CASE HYPOTHESIS (that one is in (I) with |C|≥4) is supplied by N17/N23 consumers, as in the existing COVER tree. No new backward edge.
00009|   **Overlay A-1** (written verdict LF46; 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35) is retained in N15: the 5-valuation is h_i (README writes g_i), distinct from coset representatives g_i. Add explicitly "h_i := v_5(n_i)" to v6 LF11.
00010|2. **m-B — R16 and N16 body literal.** Rewrite R16's range as: RK7 LF70 (non-L5 quantities only), LF71–75, LF80 first sentence; ADD LF128–139, LF143–148, LF155; WV LF42; read with RWE m1 and m6 and CI62. v6 LF25 replaces ONLY the RK7/ADD entries of the N16 body cell: RKE W1–W2 and WV LF23, LF38–42, LF49–50 remain in N16's body; R12 = WV LF38/LF48 packing; R18 = ADD LF21–110 (W2 governs LF106), LF124 first sentence (not its second sentence, which points to the excluded LF80 clause; upward closure follows from τ≥τ_min alone, RWE m8).
00011|3. **Notes.** v6 LF13 "no Sun input" means "no Sun(t≥3) or Sun7 input"; P0(a) uses Sun(2)=L0.6 via the existing N02 edge. v6 LF8's "(e.g. N16)" means "via the consumer's own N16 import"; RK7 LF68 (profile pi_i) is inside RW LF10–23's restricted contract (RWE m1 LF70 vocabulary).
00012|
00013|AFIBRE MAJ-1 and MIN-1..4 are resolved by v6 as amended here; both families agree. Global graph/final join remain separate gates; full Sun7 UNACCEPTED.

