# K7 family closure map v2: complete conditional DAG for distinct 2/3 markers

Written: 2026-10-19T08:08:58-0700 (`/bin/date` immediately before exclusive create). Owner: Sun7K62Successor.

**CONDITIONAL; NO CLOSURE CLAIM.** This map supersedes navigation map `D/K7-family-closure-map-v1.md` `922572acd826c3e18ef661c50a617c197c9623e287f560d3e3eae2108b43a81e`. No proof source is overwritten.
It includes the self-found ZT5-A gap and its candidate repairs: ZE2 reinstates the theorem only conditionally, and ZE3
adds the required t-row step. Every source pin below is full SHA256 of the current frozen file; every edge gives its
source pins, status and covering review. Pending statements must not be treated as accepted by following this map.

## 1. Roots and definitions

- `D` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue`.
- `B` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`.
- `O` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`.
- `R` = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review`.
- `R16` = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.


K7 is the README class C=V, all pairwise index gcds 6. Equivalently n_i=6r_i with gcd(r_i,r_j)=1 for i!=j. Write
r_i=2^e_i 3^a_i 5^b_i w_i, gcd(w_i,30)=1. These are exponents in r_i (so the 2/3 markers mean extra powers beyond the
common 6), not the README exponents in n_i. The w_i are pairwise coprime. **F** is only the K7 subfamily with both a
2-marker z and a 3-marker t and z!=t. This restriction does not assert that all other K7 members have been excluded.
Each of the primes 2,3,5 divides at most one r_i, by pairwise coprimality.

- **(a1):** r_z=2^E 5^Bz w_z, r_t=3^A 5^Bt w_t, E,A>=1, Bz,Bt>=0, Bz*Bt=0; all five vertices W=V\{z,t} are unmarked.
- **(a2):** a distinct p has r_p=5^B w_p with B>=1; r_z=2^E w_z, r_t=3^A w_t, W'=V\{z,t,p} unmarked; W=W' union {p}.
- **(a2-no5):** (a2) and neither matrix has an entry 5.
- **(a2-zt5):** (a2) and alpha_zt=5 or alpha*_zt=5. The defining union of these two components is inversion-stable.
  Since alpha_zt+alpha*_zt<=6 and entries are positive, exactly one orientation has the five. The component with the
  five in alpha* is reduced by one inversion to alpha_zt=5, without moving the markers or changing any exponent.

At every case split T={u in W:alpha_zu=3}, T*={u in W:alpha*_zu=3}. A **mirror** exchanges these two orientation
roles, and is realized by the actual inverted configuration (INV/E6), not by postulating an extra matrix symmetry.
The DAG is understood on these inverse-paired classes; inverse arrows are normalization maps, not logical cycles.

## 2. Exhaustion proof (not an emptiness proof)

Take C in F. Pairwise coprimality makes its possible 5-marker unique. If absent, on z or on t, C has precisely the
(a1) index shape above. Otherwise it lies at one third vertex p, giving exactly (a2). These alternatives are disjoint.
In (a2), define an auxiliary set (a2-o5): some entry equals 5, but neither z-t orientation equals 5. By definitions,
(a2) is the disjoint union of (a2-no5), (a2-zt5) and (a2-o5). Lemma F (PENDING R1, edge E12) says that (a2-o5) is empty.
Thus **conditional on that named lemma**, F is exhausted by the three disjoint classes

    (a1)  /  (a2-no5)  /  (a2-zt5).

All three are inversion-stable: index shapes are unchanged (INV/E6); the no-five condition quantifies over both
matrices; the z-t-five condition is the union of the two normalized components. In (a1) and its transferred no-five
branch, RICH TZ(iii) or its named bridge yields T=W or T*=W, which splits without loss into Case A (both), Case B
(only T=W) and its mirror (only T*=W). Case A's K2,3 conclusion is explicitly up to inversion, and CELL-A treats both
orientations. In normalized (a2-zt5), ZS (PENDING R3) instead splits T*=W versus size(T*)=3, covering both possibilities
because its asserted proof excludes size 4 and the accepted/conditional z-row data give size at least 3. No other
marker placement, orientation component, or internal branch of F is omitted by these conditional splits. QED.

This proof says nothing about emptiness of any of the three classes; each exclusion edge remains subject to review.

## 3. Review keys and full source catalog

**R1**: parent-owned A1/A2 repair review, covering A1/TC/A22/A2 with overlay OV; verdict pending.
**R2**: parent-owned CASEA/CELL review, package `D/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`; statements are conditional premises of R3, not accepted
by this manifest. **R3**: parent-owned A2-side review requested with this manifest; no reviewer verdict exists here.
Accepted statements are marked **ACCEPTED-SCOPED** and their frozen parent record is identified separately.

R3 manifest: `D/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

| key | frozen file | full SHA256 |
|---|---|---|
| BASE | `O/README.md` | `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1` |
| RULES | `O/rules-k7-v1.md` | `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee` |
| INV | `B/K7-LFC-INV-v1.md` | `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c` |
| INVE | `B/K7-LFC-INV-erratum-v1.md` | `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5` |
| Z2E | `B/K7-Z2-erratum-v1.md` | `3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9` |
| NO4 | `D/K7-D23-NO4-v1.md` | `a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d` |
| NO4E | `D/K7-D23-NO4-erratum-v1.md` | `594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a` |
| RICH | `D/K7-D23-RICH-v1.md` | `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3` |
| RICHE | `D/K7-D23-RICH-erratum-v1.md` | `8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69` |
| RICHE2 | `D/K7-D23RICH-D23P-erratum-v1.md` | `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428` |
| D23P | `D/K7-D23P-v1.md` | `89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880` |
| A1 | `D/K7-A1-STRUCT-v1.md` | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` |
| TC | `D/K7-TC-v1.md` | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` |
| A22 | `D/K7-TC-A22-v1.md` | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` |
| A2 | `D/K7-A2-FIVE-v1.md` | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` |
| OV | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` |
| K23 | `D/K7-CASEA-K23-v1.md` | `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3` |
| CELL | `D/K7-CELL-v1.md` | `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae` |
| CELLE | `D/K7-CELL-erratum-v1.md` | `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132` |
| TX | `D/K7-CASEA-CELL-A2-TRANSFER-v1.md` | `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6` |
| ZA | `D/K7-A2-ZT5-A-v1.md` | `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919` |
| ZB | `D/K7-A2-ZT5-B-v1.md` | `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8` |
| ZE1 | `D/K7-A2-ZT5-erratum-v1.md` | `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4` |
| ZE2 | `D/K7-A2-ZT5-erratum-v2.md` | `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47` |
| ZE3 | `D/K7-A2-ZT5-erratum-v3.md` | `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667` |

Accepted parent records (status applies only to their stated scopes):

- VWRITE: `R16/sun-coset7-written-parent-verdict-v1.md` `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35`.
- VINV: `R/sun7-lfc-inv-parent-verdict-v1.md` `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18`.
- VZ2: `R/sun7-Z2-parent-verdict-v1.md` `0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c`.
- VNO4: `R/sun7-D23-parent-verdict-v1.md` `d3453de10eafab4d4666eb1902e18a13140beb4aee511df3c35febf21e4f37db`.
- VRICH: `R/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` `1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0`.
- VSUN5: `R16/sun-coset5-parent-verdict-v1.md` `2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301`.
- VSUN6: `R16/sun-coset6-parent-gate-verdict-v1.md` `efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29`.

RICH has mandatory RICHE and RICHE2; D23P mandatory RICHE2; NO4 mandatory NO4E; INV mandatory INVE. The R1 files all
use OV. CELL uses CELLE. For ZE1: ZB.1/ZB.2 and MAP.2 remain active; ZA.1/ZA.2 withdrawal, MAP.1 and old PKG.1 are
superseded by ZE2/ZE3 and the R3 v2 manifest. P3 gives verbatim statements, import statuses and every Sun/index step.

## 4. DAG edges (pin = catalog key with full SHA; file names resolved uniquely above)

### E00: K7 -> F (restriction, not an exclusion)

- Claim: Select K7 members whose 2-marker z and 3-marker t both exist and differ.
- Source pins: BASE `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1`.
- Status: **Definition; elementary**. Covering review: A: VWRITE; no exclusion asserted.

### E01: F -> (a1) or (a2)

- Claim: Unique 5-marker absent/on z/on t gives (a1); otherwise a third p gives (a2). Section 2 proves this exhaustively.
- Source pins: BASE `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **Elementary; inversion-compatible**. Covering review: A: VWRITE/VINV.

### E02: (a1) -> 3-type z-rows in both orientations

- Claim: D23-MIX: at least three W-threes in each z-row, remaining entries <=3, z-t entries in {1,2}.
- Source pins: NO4 `a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d`; NO4E `594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a`.
- Status: **ACCEPTED-SCOPED**. Covering review: A: VNO4.

### E03: (a1) -> T=W or T*=W

- Claim: RICH TZ(iii); uses the accepted R3/TR/CC and no-W3 obstruction.
- Source pins: RICH `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3`; RICHE `8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69`; RICHE2 `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428`.
- Status: **ACCEPTED-SCOPED**. Covering review: A: VRICH.

### E04: T=W or T*=W -> Case A, B, B-mirror

- Claim: A: T=T*=W; B: T=W!=T*; mirror: T*=W!=T. The last is inverse-normalized B.
- Source pins: RICH `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **Elementary split from E03**. Covering review: A: VRICH/VINV.

### E05: Case A/B -> A1 local row and t-row claims

- Claim: Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB (not the obsolete obstruction patterns).
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.

### E06: Case A all-(2,2) -> empty

- Claim: A22 uses the R1 row at E=1 as well as E>=2, with the mandatory overlay.
- Source pins: A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.

### E07: Case A not all-(2,2) -> K2,3 structure or its inverse

- Claim: K3/K2/CL/S and S-a..S-f classify the remaining row graphs; no representative outside the inverse pair is dropped.
- Source pins: K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).

### E08: K2,3 structure and its inverse -> empty

- Claim: CELL-A via EQ/SUB/IN/CELL; the inverse has the same labelled index hypothesis.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).

### E09: Case B -> TC-B plus t-a data

- Claim: TC-B supplies alpha*_v1v2=2 and alpha*=2 inside T*; CASEB-T supplies alpha_ta=2, alpha*_ta=4.
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.
- Status: **PENDING**. Covering review: R1 and R2.

### E10: Case B and B-mirror -> empty

- Claim: CELL-B, corrected LFC orientation C^alpha* (CELLE C.4); mirror by INV, not a new assumed symmetry.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).

### E11: (a2) -> accepted 3-type z-row precursor

- Claim: D23P gives both z-rows type (b-prime).
- Source pins: D23P `89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880`; RICHE2 `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428`.
- Status: **ACCEPTED-SCOPED**. Covering review: A: VRICH.

### E12: (a2) -> (a2-no5) or (a2-zt5)

- Claim: Lemma F excludes every five except z-t in at most one orientation. The auxiliary (a2-o5) set of section 2 is empty if F holds.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.

### E13: (a2-no5) -> enumerated RICH-type proof data

- Claim: BRIDGE gives its named claims and actual-family/auxiliary beta<=4 index chains, not an abstract beta<=5 theorem. W=W-prime union {p}.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.

### E14: (a2-no5) -> transferred A1/TC/A22 claims

- Claim: Cor A2-TRANSFER gives the explicitly enumerated A1/TC/A22 claims including FG-V. It does not turn p into an unmarked index.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.

### E15: (a2-no5), both orientation case splits -> empty

- Claim: Cor CC-A2 transfers K23/CELL named claims. Apply the same A/all-(2,2)/K2,3/B/mirror split to those claims.
- Source pins: TX `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.

### E16: (a2-zt5) -> unique normalized five orientation

- Claim: INV/E7 makes the other z-t entry 1; A2 S1-S5 give T=W, E>=2, prescribed t-W values and no other five. Inverse swaps the two orientation-labelled components.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING (structure); inversion accepted**. Covering review: R1; A: VINV.

### E17: Normalized (a2-zt5) -> T*=W or size(T*)=3

- Claim: FG-zf and ZS; latter supplies the exact O*={v1,v2} structure in the size-3 branch.
- Source pins: ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.
- Status: **PENDING**. Covering review: R3.

### E18: Normalized (a2-zt5) plus connected Gamma^alpha -> t-row lemma ZT

- Claim: Initially allow alpha*_tu=3; PFG equality excludes those cases before invoking Cor L. Conclusion: no threes and at least two fours.
- Source pins: ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`.
- Status: **PENDING, materially new**. Covering review: R3 (A1 premise conditional on R1).

### E19: T*=W -> no alpha* W-three and no alpha* W-t three

- Claim: ZW uses FG-zf and the Theta* complement-clique proof; its connected-Gamma step invokes ZT (E18), not the unqualified old Cor L.
- Source pins: ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.
- Status: **PENDING, materially new**. Covering review: R3.

### E20: T*=W, with ZW/ZT prerequisites -> empty

- Claim: ZT5-A audit: transfer K23/CELL-A using only justified z-free/t-free containments and unions; restoration is a candidate, not acceptance.
- Source pins: ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.

### E21: size(T*)=3 -> empty

- Claim: ZT5-B uses ZT before Step 1, ZE1 missing-case/e*<=3 repairs, and the two index-3 subgroup cell contradiction.
- Source pins: ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.

### E22: Five in alpha* (the inverse-labelled (a2-zt5) component) -> same normalized branches

- Claim: Apply INV once, retaining z,t,p and all actual exponents; then E16-E21 apply. No equal-marker or other K7 case is selected.
- Source pins: INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`; A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.
- Status: **Conditional on E16-E21; inversion ACCEPTED**. Covering review: A: VINV; R1/R3.

## 5. Foundation and conditional conclusion

All index/coset operations use the finite quotient R0 and L0.1-L0.3; both orientations are actual configurations by
INV. L1/VFC are applied to the inverse as explicitly allowed in Z2E G5. Direct instances are Sun(2), Sun(3), Sun(4)
(and Sun(5) inside the full transferred Cor L, where stated). The accepted transitive import closure still reaches
computer-assisted Sun(5)/Sun(6); the newly written steps do not use a computational search as a premise.

**If** R1, R2 and R3 accept every pending claim at the indicated scope, E06/E08/E10 exclude the (a1) cases and mirrors,
E13-E15 transfer those exclusions to (a2-no5), and E16-E22 exclude the normalized (a2-zt5) branches and their inverses.
Together with E01/E12 this would leave F empty. This is only a conditional implication, **not a closure verdict for F,
K7 or Sun(7)**. The accepted frontier is unchanged by this map. Other K7 marker coincidences and K6.2* are outside it.
