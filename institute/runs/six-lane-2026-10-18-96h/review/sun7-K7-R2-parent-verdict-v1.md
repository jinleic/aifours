# Sun(7) K7 R2: CASEA-K23, CELL and the (a1) closure

Recorded at 2026-10-19T10:35:44-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL**, written mathematics relative to the exact accepted imports and mandatory overlays below. The K7 subfamily **(a1) contains no actual disjoint-coset configuration**, in any group (finite-core reduction R0). Computer-assisted Sun(5) and Sun(6) remain transitive imports. No novelty, Lean or human-referee claim. Full K7, K6.2* and Sun(7) remain OPEN.

## Exact setting and accepted conclusions

K7: V={z,t} disjoint-union W, |W|=5, pairwise index gcd6; n_i=6r_i and the r_i are pairwise coprime. In (a1), z and t are distinct: r_z=2^E5^Bz w_z, r_t=3^A5^Bt w_t, E,A>=1, Bz,Bt>=0, Bz*Bt=0; all five W vertices are unmarked, with w-parts pairwise coprime and prime to30. A 5-marker is absent or on z or t; a third 5-marked vertex is OUTSIDE (a1).

Accepted at the corrected literal scopes:
1. K23 row shapes/twin rule, R1/R1minus/R3prime/R4/R5/R6 and their stated exclusions (R4 new at c=3, not silently imported from TC); K3 with pairwise distinct vertices, K2, CL, Lemma S and exclusions S-a through S-f.
2. **Theorem K7-CASEA-K23:** Case A not all-(2,2) reduces, up to actual inversion, to the stated K2,3 family with its refined index/entry data.
3. **Proposition K7-CASEB-T:** in Case B, alpha_ta=2 and alpha*_ta=4 for every a in T*. Its rigid-row proof uses the actual Case-B labels, not the unrelated global Case-A setting.
4. EQ (Q=D_g1 union D_g2, five non-z odd parts only), SUB, IN (i!=j and its lower bound), and **vertex-wise CELL** at LK=G. CELL(i) does not require the qualifying vertices to occupy distinct K-cosets. Its old three-distinct-coset form is a special case. CELL(ii)/(iii) retain their literal piece-index and disjoint-coset hypotheses.
5. **Theorems K7-CELL-A/B:** the K2,3 family and its inverse, Case B and its mirror are empty.
6. **Corollary (a1) closure:** accepted TZ(iii) splits into Case A, Case B and its actual inversion mirror. Case A all-(2,2) is excluded by accepted TC-A22 for every E>=1; other Case A types go through corrected CASEA-K23 and CELL-A. Case B goes through accepted CASEB/TC-B, CASEB-T and CELL-B. INV/E6 covers mirrors; R0 transfers from finite groups. This chain introduces no unaccepted R3 premise.

## Immutable texts and mandatory reading order

| Text | SHA256 |
|---|---|
| [K7-CASEA-K23-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md) | `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3` |
| [K23E](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-erratum-v1.md) | `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` |
| [K7-CELL-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md) | `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae` |
| [CELLE](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-erratum-v1.md) | `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132` |
| [ecff consolidated overlay, R2.1-R2.4 only](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md) | `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940` |
| [R2-only repair, all E1-E29](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-repair-erratum-v1.md) | `3bd5474def3d3115dad6883bb509509f2631adb9ac31af0723968012b4922423` |
| [Complete repair review packet](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-R2-repair-v1.md) | `ce880260b035e70ec1b87e87c7431426477dd964c899937dc82876eb087d8006` |

Apply E1 to ecff R2.1's New field and E2 to CELLE C.2's New field first. K23 reads K23E, amended ecff R2.1 and R2.2, then the new K23 replacements. CELL reads CELLE C.1-C.4 (C.1 amended by ecff R2.4; C.2 by E2), ecff R2.3, then the new CELL replacements. Package status/citation replacements are informational only. All old bytes stay immutable.

## Reviews and disposition

- [Full Codex R2](sun7-K7-R2-codex-v1.prompt.stdout.txt) `3e40ddf2ab2094822ad7520b4f6ff455e391b45e17159539ab2bc7b59d9eeacb`: observed gpt-6.1-sol/max/read-only, ACCEPT-WITH-FIXES0F/1M/2m. The unsupported S-f mass is repaired by ecff R2.1's triangle argument; K3/IN distinctness and five-index coprimality by R2.2-R2.4.
- [Codex consolidated repair](sun7-K7-R2-R3-repair-codex-v1.prompt.stdout.txt) `9ed1bdce9d112415e9ce9b5e31f2f0f8ccd29a3abe958bdc0e8845c39b9adf80`: R2 ACCEPT_REPAIRS0F/0M/0m. Its R3a/R3b repair assessments did not accept their underlying theorems.
- [Full Claude R2 v2](sun7-K7-R2-claude-v2.prompt.note.md) `d25e8cd0034669442d5dbbfbbd6f2892a9a3a21187c6f2027e7667a575a0c68c`: observed claude-opus-5-5/max/no tools; no rejected claim,0F/0M/14m. It received exactly the R2 subset of ecff, not R3/DAG status items; that is sufficient here, and unseen R3 items target no R2 source.
- [Codex R2-only repair](sun7-K7-R2-repair-codex-v1.prompt.stdout.txt) `3ecfc96dbc69f52ea12448250e36eec687254fca9e0ace5820451cba4457ea1e`: ACCEPT_REPAIRS0F/0M/0m, every Claude m1-m14 FIXED. Explicit proofs support R6's equal-four containment and the vertex-wise CELL formulation; main theorem scopes unchanged.

All29 repair items are mandatory. Highlights: m1 Sun(2)-only44411 accounting; m2 c=3 provenance; m3 R6 equality; m4 degree bound; m5 twin-neighbourhood justification retaining the S-f step list; m6 missing unused t-mass/witness coset; m7 Case-B applicability; m8 accepted L1 triangle citations; m9 Q definition; m10 vertex-wise CELL/product hypothesis; m11 crossing pigeonhole independent of t placement; m12 actual cell-piece index; m13 L0.2/E6/LFC(a)-(b) import precision; m14 current accepted-versus-pending labels.

## Parent verification and imported authorities

Parent verified29 unique nonoverlapping Old anchors,31 literal embedded source ranges with whole-file hashes, and replayed38 ordered Old/New replacements in memory without conflict. These are text-binding checks, not a substitute for proof review. Independent mathematical checks: (1) the S-f triangle with entries(1,b,4) forces b=4 via L1, contradicting b<=2; it does not assume the unsupported starred twin entry; (2) SUB uses U_jU_k contained in generated subgroup contained in X_j with equal measures, so no product-as-subgroup assumption is made; (3) U_x subset L and m_x^K=3 give U_xK=G and LK=G, hence index9; cell intersections and n_v/3 piece indices exist before proving t's placement; (4) the two distinct v-columns suffice for the crossing pigeonhole; (5) CELL-B integrality with v3(n_z)=1 forces m_z^H=3, and the actual marker factors yield pairwise-gcd2 indices.

Prerequisite parent authorities (with their own mandatory overlays): [A1/A2](sun7-K7-A1-A2-repairs-parent-verdict-v1.md) `2a7c5b6c…` through OVv1 then OVv2; [RICH/D23P](sun7-K7-D23RICH-D23P-parent-verdict-v1.md) `1167bc4f…`; [LFC/INV](sun7-lfc-inv-parent-verdict-v1.md) `8621e744…`; written rules `73a25ba6…`, L1/T1-T3, VFC and L0.2; INV E6. No marked-apex saturation is smuggled in: saturation is at actual unmarked W apexes; marked t uses ordinary LFC(d) and the stated connectedness hypotheses. Direct new Sun instances are Sun(2)/Sun(3), including inside K intersect L; the transitive closure still includes computer-assisted Sun(5)/Sun(6).

## Unchanged open boundary

No transfer to (a2) is accepted by this verdict. (a2-no5), (a2-zt5) beyond accepted S1-S5, R3a/R3b full theorem gates, K6.2*, full K7 and Sun(7) remain OPEN/pending. R3a's2700s Claude attempt was NO_VERDICT, not approval. Priority notes retain their bounded-search/no-novelty limits.
