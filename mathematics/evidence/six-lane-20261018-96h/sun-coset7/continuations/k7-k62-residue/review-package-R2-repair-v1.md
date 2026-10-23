# Review package R2-repair v1: `K7-R2-repair-erratum-v1.md` (Claude R2 v2 m1-m14), compact

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:21:21-0700.
- **Owner:** Sun7K62Successor. Manifest only; no computation, no model CLI, no new theorem. For the parent-owned narrow
  repair review. **Candidate repair; the R2 verdict is pending; nothing here accepts R2 or excludes (a1).**

## 1. Pins and reading order

| role | file | sha256 |
|---|---|---|
| repair under review (embedded in full, section 2) | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-repair-erratum-v1.md` | `3bd5474def3d3115dad6883bb509509f2631adb9ac31af0723968012b4922423` |
| Claude R2 v2 findings | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R2-claude-v2.prompt.note.md` | `d25e8cd0034669442d5dbbfbbd6f2892a9a3a21187c6f2027e7667a575a0c68c` |
| Codex R2 findings | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R2-codex-v1.prompt.stdout.txt` | `3e40ddf2ab2094822ad7520b4f6ff455e391b45e17159539ab2bc7b59d9eeacb` |
| consolidated repair (items R2.1-R2.4 apply first) | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md` | `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940` |
| K7-CASEA-K23 / K23E | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` / `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-erratum-v1.md` | `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3` / `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` |
| K7-CELL / CELLE | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` / `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-erratum-v1.md` | `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae` / `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132` |
| R2 package (metadata target) | `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` | `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583` |
| A1/A2 verdict (accepted imports, overlays v1 then v2) | `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` | `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966` |

Reading order (as in the repair): amend ecff Item 1 New and CELLE C.2 New; K23 <- K23E, ecff R2.1-R2.2, repair;
CELL <- CELLE C.1-C.4 (C.1 via ecff R2.4), ecff R2.3, repair; package <- repair. All Old spans were checked clerically
to be unique and non-overlapping, and the full sequence replays without conflict (string matching only).

## 2. The repair, verbatim and complete

`````text
# K7-R2-repair-erratum-v1: R2-only repair of the Claude R2 v2 findings m1-m14 (read after ecff4e76 R2.1-R2.4)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T10:20:38-0700.
- **Owner:** Sun7K62Successor. Written proof/citation repairs only; no computation, no model CLI, no new theorem.
  Every original and every earlier erratum stays byte-identical. Candidate repair; the parent owns the narrow repair
  review and the R2 verdict. **No R2 claim is accepted or promoted here; (a1) is not excluded by these files.**
- **Responds to:** Claude R2 v2 `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R2-claude-v2.prompt.note.md` `d25e8cd0034669442d5dbbfbbd6f2892a9a3a21187c6f2027e7667a575a0c68c` (0 FATAL / 0 MAJOR / 14 MINOR, read in full incl. its limits and scope
  boundaries). Earlier R2 inputs: Codex R2 `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R2-codex-v1.prompt.stdout.txt` `3e40ddf2ab2094822ad7520b4f6ff455e391b45e17159539ab2bc7b59d9eeacb`; consolidated repair `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md` `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940`, items R2.1-R2.4. The parent
  reports that the Codex R2 findings and the ecff repair were accepted by its review; no R2 verdict has been issued.
- **Accepted authorities used for citations (exact scopes):** A1/A2 verdict `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966` (overlays v1
  `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`, then v2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`); RICH/D23P verdict
  `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` `1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0`; LFC/INV verdict `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md` `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18`; written rules verdict `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35` (L0.x, L1 (T1)-(T3), VFC);
  Z2 verdict `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-Z2-parent-verdict-v1.md` `0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c` (erratum G5: L1 in the inverted configuration). Transitive closure: computer-assisted Sun(5)
  `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset5-parent-verdict-v1.md` `2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301` and Sun(6) `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset6-parent-gate-verdict-v1.md` `efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29`, unchanged.

## Reading order and scope

1. Amend the New field of ecff Item 1 (R2.1) by the item targeting `K7-R2-R3-consolidated-erratum-v1.md`; amend the New
   field of CELLE Item C.2 by the item targeting `K7-CELL-erratum-v1.md` (ecff R2.4 has already amended C.1).
2. `K7-CASEA-K23-v1.md`: apply K23E, then ecff R2.1 (as amended) and R2.2, then the K23 items below.
3. `K7-CELL-v1.md`: apply CELLE C.1-C.4 (as amended), then ecff R2.3, then the CELL items below.
4. `review-package-CASEA-CELL-v1.md`: apply the package items below (metadata only).
Every Old span below is exact, occurs exactly once in its pinned target, and does not overlap any other Old span of this
file or of K23E, CELLE, or ecff R2.1-R2.4 in the same file; the whole sequence was replayed clerically on the text
(string matching only, no mathematical computation). Items 5-42 of ecff target only ZE2, ZE3, ZT5-B, the transfer
audit, ZT5-A, the closure map, the A2 package and its addendum; none targets K23, K23E, CELL, CELLE or this package
(answering the review's limit on unseen ecff items). R3a/R3b sources are not touched by this file.

## Disposition (every finding)

| finding | disposition | items |
|---|---|---|
| m1 | K23 header Sun accounting now names the section-4 exclusion of 44411 (Sun(2)-only b = 3, k1 = 2 kill; equivalently LFC (d) at t). Package section 5 corrected to "Sun(2) only". | E4, E28 |
| m2 | Provenance note: K23 R4 is new at c = 3 (accepted TC R4 has c in {1,2}), R5 is proved E-free here (equals accepted TC R5 when E >= 2); both e = 1 exclusions are new at c = 3. Not renamed, so later references to "R4" (section 3 (S-f), section 4) keep meaning this c = 3 row. | E7, E9 |
| m3 | R6 conclusion now also states L_f = L_f' for any two fours (used in (S-f)), and "the two s" is corrected to the single vertex s with entry 2. | E8 |
| m4 | (R-a) adds d + d* <= 4 from d* >= 1 and F, F* disjoint. | E5 |
| m5 | Minimal twin-neighbourhood justification inserted at the start of (S-f): N is empty, all F- and F*-neighbourhoods are listed, and (R-b) gives alpha = 2 on c v1, c v2 and alpha* = 2 on every F-pair except v1 v2 (covering alpha*_v3c, alpha*_v1v3, alpha*_v1v4 and their symmetric uses). The one-line CL kill was not adopted: it would replace a proof whose step list is cited by the running R3b consumer audit; R2.1 stays (correct, non-load-bearing). (S-e) is unchanged (accepted; its only starred two, alpha*_v1b1 = 2, is already justified by distinct F*-neighbourhoods in the text). | E10 |
| m6 | Section 4 alpha_v1v2 = 1 branch: mass list adds t: alpha*_xt/6 <= 2/6 (unused); the witness is a right U_x-coset R subset D_y cap D_v1 (= D_y cap D_v2) outside D_z. | E11, E12 |
| m7 | CASEB-T proof opens with a scope note: R1 (accepted TC row, every E >= 1), R1- and Lemma K3 read only the labels at a in T* (W-part {2,2,4,4}, c* = alpha*_az = 3, e* = alpha*_ta), RICH Corollary 5/6 at a in W, Lemma TC and Lemma FG-V; these hold verbatim for the actual Case-B labels (E >= 2 there by CASEB). | E13 |
| m8 | (R-b) cites the accepted rules-k7-v1 L1 (T1)-(T3) (written verdict 73a25ba6...), Z2 erratum G5 for the inverse, and the A1-STRUCT section 0 specialisation (tau_min = r, tau_max = p q). The R2.1 New field (ecff Item 1) cites the same rule with the entry list (1, alpha_tv2, 4). | E1, E6 |
| m9 | EQ: Q := D_g1 cup D_g2 defined explicitly, with the right-coset characterisation; the z-mass hypothesis is noted as unused. | E16 |
| m10 | Lemma CELL restated at its proved scope: hypothesis LK = G (from U_xK = G for an L-vertex x with m^K_x = 3), vertex-wise (i) with no coset-distinctness assumption, the previous form recovered as a special case; index 9 is said explicitly to come from LK = G, not from K != L (S_3 example). CELLE C.2 New field, CELL-A (LK = G) and CELL-B (HK' = G; t placement) now cite this form. | E2, E18, E20, E21, E22 |
| m11 | CELL-A crossing count uses g_v1K != g_v2K (SUB) and pigeonhole; t's position is not used. | E19 |
| m12 | CELL-B: N_z = [K' cap H : U*_z cap H] = [G : U*_z cap H]/9 written as a cell-piece index, using U*_z subset K'. | E23 |
| m13 | CELL imports add L0.2 (SUB) and INV erratum E6 (inverse and mirror); IN's "y_i = 1 is feasible" sentence replaced by the plain fibre count; package IN line corrected to LFC (a)-(b). | E15, E17, E29 |
| m14 | K23 and CELL status headers, CELL section 7 and the package import table/scope/section-2 notes updated to: R1 imports ACCEPTED-SCOPED by verdict 2a7c5b6c... through overlays v1 then v2; K23/CELL candidates pending the parent R2 verdict; mandatory reading K23E, ecff R2.1-R2.4 and this file. Nothing is promoted; (a1) is not excluded by these files. | E3, E14, E24, E25, E26, E27 |

**Statement audit.** No theorem changes: Theorem K7-CASEA-K23, Proposition K7-CASEB-T and Theorems K7-CELL-A/B keep
their statements and scopes. Lemma CELL is restated at exactly the scope its proof establishes (hypothesis LK = G,
vertex-wise conclusions), and its previous form is stated as a special case. R6's conclusion adds only the containment
already given by its displayed fibre property. EQ's statement is unchanged up to the explicit definition of Q.
Original scopes and the transitive computer-assisted Sun(5)/Sun(6) imports are retained; direct Sun use stays Sun(2)
and Sun(3) (the latter also inside K cap L). No Sun(7).

## Verbatim Old -> New replacements

### E1 (m8): ecff Item 1 (R2.1) New field: triangle-rule citation

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md` `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940`.

Old:

````text
If alpha_tv1 = 1, the accepted triangle rule forces alpha_tv2 = 4, a contradiction.
````

New:

````text
If alpha_tv1 = 1, the triangle rule of (R-b) (rules-k7-v1 L1 (T1)-(T3) as specialised in A1-STRUCT
  section 0), applied to the entries (1, alpha_tv2, 4) with alpha_tv2 in {1, 2, 4} (E3, NO5), forces alpha_tv2 = 4, a
  contradiction.
````

### E2 (m10): CELLE Item C.2 New field: cite vertex-wise (i)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-erratum-v1.md` `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.

Old:

````text
this uses only part (i)
  of Lemma CELL (which needs U_xK = G for an L-vertex x, not the distinctness of the K-cosets) and Sun(3), and excludes it.
````

New:

````text
this uses only the vertex-wise
  part (i) of Lemma CELL as restated by `K7-R2-repair-erratum-v1.md` (index 9 from LK = G, which holds because
  U_xK = G for an L-vertex x with m^K_x = 3; t has a piece in every cell of its own K-coset because U_t subset K and
  m^L_t = 3, whatever that coset is) and Sun(3) inside K cap L (part (iii)), and excludes it.
````

### E3 (m14): K23 header status

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
- **Status:** CANDIDATE, **conditional** on the unreviewed candidates `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf: section 0
  triangle rule and two/four classes, Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem CASEB),
  `K7-TC-v1.md` (cc48340d...e117: Lemma TC, rows R1 (every E >= 1) and R3, Lemma FG-V, Theorem K7-TC-B) and
  `K7-TC-A22-v1.md` (9ebec279...1b46b41: the all-(2,2) case), all read through the overlay `K7-A1-A2-delta-erratum-v1.md`
  (sha256 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e). (a1) is NOT excluded; full Sun(7) remains
  OPEN.
````

New:

````text
- **Status:** CANDIDATE. R2 review: Codex ACCEPT-WITH-FIXES (repaired by items R2.1-R2.2 below) and Claude 0 FATAL / 0 MAJOR /
  14 MINOR (repaired by the last file below); read with
  `K7-CASEA-K23-erratum-v1.md` (K23E), items R2.1-R2.2 of `K7-R2-R3-consolidated-erratum-v1.md` and
  `K7-R2-repair-erratum-v1.md`. The parent R2 verdict is PENDING. The imports `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf: section 0
  triangle rule and two/four classes, Corollary W3, Lemma E3, Lemma PFG-t with Corollary L, Lemma B, Theorem CASEB),
  `K7-TC-v1.md` (cc48340d...e117: Lemma TC, rows R1 (every E >= 1) and R3, Lemma FG-V, Theorem K7-TC-B) and
  `K7-TC-A22-v1.md` (9ebec279...1b46b41: the all-(2,2) case) are ACCEPTED-SCOPED by
  `RUN/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` (2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966), read through
  `K7-A1-A2-delta-erratum-v1.md` (0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e) and then
  `K7-A1-A2-delta-erratum-v2.md` (9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181). (a1) is NOT excluded by this file; full Sun(7)
  remains OPEN.
````

### E4 (m1): K23 header Sun accounting

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
Sun(2), Sun(3) (Corollary L enters only through "at least two entries 4", which is Sun(5)-free); transitive closure as
````

New:

````text
Sun(2), Sun(3) (Corollary L enters only through "at least two entries 4" and, in section 4, through the exclusion of
  44411 by its b = 3, k1 = 2 kill; both uses are Sun(5)-free, and the 44411 kill uses only Sun(2): y = 1/3 on the three
  fours and 1 on the two ones is feasible with value 6, which also contradicts LFC (d) at t in C^alpha directly);
  transitive closure as
````

### E5 (m4): (R-a) degree bound

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
- (R-a) Every x-row has a W-four (otherwise it has >= 3 entries <= 2 and Lemma B forces exactly one four), so d, d* lie
  in {1,2,3}.
````

New:

````text
- (R-a) Every x-row has a W-four (otherwise it has >= 3 entries <= 2 and Lemma B forces exactly one four), so d, d* >= 1;
  as F and F* are disjoint (INV) and u has four W-neighbours, d + d* <= 4, so d, d* lie in {1,2,3}.
````

### E6 (m8): (R-b) triangle-rule citation

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
(triangle rule of A1-STRUCT section 0;
  the ell's of W and t are odd)
````

New:

````text
(triangle rule: the
  accepted rules-k7-v1 L1 (T1)-(T3), applied also to the inverted configuration by Z2 erratum G5, as specialised in
  A1-STRUCT section 0 - in a triangle inside W cup {t} with entries p <= q <= r in {1,2,4} every ell is odd, so
  tau_min = r and tau_max = p q, and the triangle passes iff r <= p q; with p = 1 this forces q = r)
````

### E7 (m2): (R-c) R4/R5 provenance

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
    occupied fibre C with o not in S_C contains every four; so **L_j subset L_f for every four f and every j != o**.
````

New:

````text
    occupied fibre C with o not in S_C contains every four; so **L_j subset L_f for every four f and every j != o**.
    (Both rows are proved here at c = 3 for every E >= 1: the displayed vectors, their feasibility and the equality
    clause use no exponent condition. R4 here is new at c = 3 - the accepted K7-TC row R4 is ({1,4,4,4} | c | 2) with
    c in {1,2} - and R5 here coincides with the accepted K7-TC row R5 when E >= 2.)
````

### E8 (m3): (R-c) R6 conclusion

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
contains all three fours; so **L_s subset L_f** for the two s and every four f.
````

New:

````text
contains all three fours; so **L_s subset L_f** for the vertex s with entry 2 and every four f, and
    **L_f = L_f'** for any two fours f, f' (a fibre meeting the coset of a four is occupied and is not of the two
    excepted kinds, so it contains all three fours).
````

### E9 (m2): (R-c) e = 1 exclusions provenance

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
  - (1,2,4,4 | 1) and (1,4,4,4 | 1) do not occur (y = (o 1, fours 1/2 resp. 1/3, t 1) has value 6). The remaining rows,
````

New:

````text
  - (1,2,4,4 | 1) and (1,4,4,4 | 1) do not occur (new at c = 3, every E >= 1; y = (o 1, fours 1/2 resp. 1/3, t 1) has
    value 6). The remaining rows,
````

### E10 (m5): (S-f) entry justification

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
**(S-f) (n31, n21, n22) = (4,0,1).** F* = {c v1, c v2, v3 v4} with c the (2,2)-vertex.
````

New:

````text
**(S-f) (n31, n21, n22) = (4,0,1).** F* = {c v1, c v2, v3 v4} with c the (2,2)-vertex.
Here N is empty (seven F-pairs and three F*-pairs exhaust the ten pairs of W), so alpha <= 2 on F* and alpha* <= 2 on F
(INV). The F-neighbourhoods are N_F(v1) = {v2, v3, v4}, N_F(v2) = {v1, v3, v4}, N_F(v3) = N_F(v4) = {v1, v2, c} and
N_F(c) = {v3, v4}; the F*-neighbourhoods are N_F*(v1) = N_F*(v2) = {c}, N_F*(v3) = {v4}, N_F*(v4) = {v3} and
N_F*(c) = {v1, v2}. By (R-b) an x-entry 1 joins only vertices with equal F_x-neighbourhoods, so alpha = 2 on c v1 and
c v2 (alpha_v3v4 in {1, 2} stays open and is treated below), and alpha* = 2 on every F-pair other than v1 v2; in
particular alpha*_v3c = alpha*_v4c = alpha*_v1v3 = alpha*_v1v4 = alpha*_v2v3 = alpha*_v2v4 = 2, the starred twos used
below (alpha*_v1v2 is not determined and is not used).
````

### E11 (m6): section 4 mass list

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
at apex x in C^alpha the masses are y, w: 4/6, v1, v2: 2/6, z: 3/6, and D_z is disjoint from D_v1 and D_v2.
````

New:

````text
at apex x in C^alpha the masses are y, w: 4/6, v1, v2: 2/6, z: 3/6, t: alpha*_xt/6 <= 2/6 (unused), and D_z is
disjoint from D_v1 and D_v2.
````

### E12 (m6): section 4 witness coset

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
some coset outside D_z holds y, v1 and v2,
````

New:

````text
some right U_x-coset R subset D_y cap D_v1 (= D_y cap D_v2), outside D_z, holds y, v1 and v2,
````

### E13 (m7): CASEB-T rigid rows in Case B

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
*Proof.* v1's alpha-row is R3 (four v2; twos a1, a2, a3), with alpha_tv1 = 4.
````

New:

````text
*Proof.* Scope note (Case B lies outside the Case-A conventions of section 0): the rows R1 (accepted K7-TC row, every
E >= 1) and R1- ((R-c), proved here) and Lemma K3 read only the following data, which hold verbatim at a in T* in
Case B. In C^alpha* the alpha*-row of a has W-part {2,2,4,4} (fours v1, v2 by CASEB; twos the other two a's by
K7-TC-B), c* = alpha*_az = 3 (a in T*) and e* = alpha*_ta in {1,2,4} (E3, NO5); its labels at a are 4 w_v, 2 w_a' (W is
unmarked, so W-label gcds are entry gcds), 3 2^E 5^Bz w_z for z and e* 3^A 5^Bt w_t for t with Bz Bt = 0 - exactly the
labels of (R-c). The value bound and the occupied-fibre equality clause are RICH Corollary 5/6 at a in W, valid in both
orientations throughout (a1); Lemma K3 uses only Lemma TC and Lemma FG-V, accepted for all of (a1) (verdict
2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966). None of these proofs uses T = T* = W, a degree type or a bound on E (and E >= 2 in
Case B by CASEB). v1's alpha-row is R3 (four v2; twos a1, a2, a3), with alpha_tv1 = 4.
````

### E14 (m14): CELL header status

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
- **Status:** CANDIDATE, **conditional** on the unreviewed candidates `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf),
  `K7-TC-v1.md` (cc48340d...e117) and `K7-TC-A22-v1.md` (9ebec279...1b46b41), read through the overlay
  `K7-A1-A2-delta-erratum-v1.md` (0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e), and on
  `K7-CASEA-K23-v1.md` (f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3: Theorem K7-CASEA-K23,
  Proposition K7-CASEB-T). Used from them: Lemma TC, Lemma FG-V, Theorem CASEB, Theorem K7-TC-B, Theorem K7-CASEA-K23,
  Proposition K7-CASEB-T. No closure claim: Sun(7) remains OPEN.
````

New:

````text
- **Status:** CANDIDATE. R2 review: Codex ACCEPT-WITH-FIXES (repaired by items R2.3-R2.4 below) and Claude 0 FATAL / 0 MAJOR /
  14 MINOR (repaired by the last file below); read with
  `K7-CELL-erratum-v1.md` (CELLE, whose C.1 is amended by item R2.4), items R2.3-R2.4 of
  `K7-R2-R3-consolidated-erratum-v1.md` and `K7-R2-repair-erratum-v1.md`. The parent R2 verdict is PENDING. **Conditional** on
  `K7-CASEA-K23-v1.md` (f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3: Theorem K7-CASEA-K23,
  Proposition K7-CASEB-T; R2 candidate). The imports `K7-A1-STRUCT-v1.md` (c8a16f14...e3ccf), `K7-TC-v1.md`
  (cc48340d...e117) and `K7-TC-A22-v1.md` (9ebec279...1b46b41) are ACCEPTED-SCOPED by verdict
  2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966 through `K7-A1-A2-delta-erratum-v1.md`
  (0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e) and then `K7-A1-A2-delta-erratum-v2.md`
  (9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181). Used from them: Lemma TC, Lemma FG-V, Theorem CASEB, Theorem
  K7-TC-B, Theorem K7-CASEA-K23, Proposition K7-CASEB-T. No closure claim: Sun(7) remains OPEN.
````

### E15 (m13): CELL header imports

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
  (a)-(d), INV, VFC (V1)-(V4), L0.1, L0.3, R0.
````

New:

````text
  (a)-(d), INV with erratum E6 (the inverted configuration has the same labelled indices and markers; used for "nor in
  its inverse" in Theorem K7-CELL-A and for the mirror case in Theorem K7-CELL-B), VFC (V1)-(V4), L0.1, L0.2 (used in
  Lemma SUB), L0.3, R0.
````

### E16 (m9): Lemma EQ statement

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
z has mass 3/6. Then **D_g1 = D_g2**, both equal to the union Q of the right U_a-cosets meeting g1 or g2, and
mu(Q) = 4/6.
````

New:

````text
z has mass 3/6 (this hypothesis on z is not used in the proof). Then **D_g1 = D_g2**, both equal to
Q := D_g1 cup D_g2, and mu(Q) = 4/6. (A right U_a-coset meets g_jU_j iff it lies in D_j = U_a g_j U_j, so Q is the
union of the right U_a-cosets meeting the cosets of g1 or g2.)
````

### E17 (m13): Lemma IN proof sentence

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
The weight y_i = 1 (all others 0) is feasible, so summing over the fibres inside g_jK:
````

New:

````text
These fibres of L_i are distinct fibres inside g_jK other than g_jU_j, so counting them:
````

### E18 (m10): Lemma CELL restated vertex-wise at its proved LK = G scope

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
Let K != L be subgroups of index 3, and let K contain U_v for three vertices v (the "K-vertices") whose cosets lie in the
three distinct left K-cosets, L contain U_x for three vertices x (the "L-vertices") whose cosets lie in the three
distinct left L-cosets, with m^L_v = 3 for every K-vertex and m^K_x = 3 for every L-vertex. Then:
- (i) [G : K cap L] = 9, and the nine left (K cap L)-cosets ("cells") correspond bijectively to the pairs
  (left K-coset, left L-coset); every cell contains a piece of the K-vertex of its K-coset (a left coset of U_v cap L, of
  index n_v/3 in K cap L) and a piece of the L-vertex of its L-coset (index n_x/3).
- (ii) For any other vertex z, a nonempty piece g_zU_z cap c of a cell c is a left coset of U_z cap K cap L, whose index
  N_z in K cap L has all prime factors in {2, 3} or dividing r_z.
- (iii) If in a cell c the three pieces of v, x and z have pairwise gcds of indices <= 2, then g_zU_z does not meet c
  (Sun(3) inside K cap L).
*Proof.* (i) U_xK = G for an L-vertex x, so LK = G and |L||K|/|L cap K| = |G|. A K-coset meets each L-coset in at most
one (K cap L)-coset and is the union of three of them, which gives the bijection. g_vU_v meets all three L-cosets
(m^L_v = 3), each in a left coset of U_v cap L subset K cap L, of index n_v m^L_v / 9 = n_v/3; likewise for x.
(ii) [G : U_z cap K cap L] = n_z [U_z : U_z cap K] [U_z cap K : U_z cap K cap L], and both brackets are integers <= 3.
(iii) Translating c to K cap L, the three pieces are pairwise disjoint left cosets of subgroups of K cap L. QED
````

New:

````text
Let K and L be subgroups of G of index 3 with **LK = G**. (LK = G holds as soon as some vertex x has U_x subset L and
m^K_x = 3: then mu(U_xK) = m^K_x/3 = 1, i.e. U_xK = G, and U_xK subset LK. Index 9 below is derived from LK = G, not
from K != L alone: two distinct subgroups of index 3 can meet in a subgroup of index 6, e.g. two subgroups of order 2 of
S_3.) Then:
- (i) [G : K cap L] = 9, and c -> (cK, cL) is a bijection from the nine left (K cap L)-cosets ("cells") onto the pairs
  (left K-coset, left L-coset); the cell of the pair (gK, hL) is gK cap hL. **Vertex-wise:** if v is a vertex with
  U_v subset K and m^L_v = 3, then g_vU_v (contained in g_vK) meets each of the three cells contained in g_vK, and each
  such piece g_vU_v cap c is a left coset of U_v cap L, a subgroup of K cap L of index n_v/3. Symmetrically, if x is a
  vertex with U_x subset L and m^K_x = 3, then g_xU_x meets each of the three cells contained in g_xL, in a left coset of
  U_x cap K of index n_x/3 in K cap L. No assumption is made on which K-cosets (resp. L-cosets) such vertices occupy;
  two of them may share a coset. Under the hypotheses of the previous form of this lemma (three "K-vertices" v with
  U_v subset K in the three distinct left K-cosets and m^L_v = 3, three "L-vertices" x with U_x subset L in the three
  distinct left L-cosets and m^K_x = 3), LK = G holds, and every cell contains a piece of the K-vertex of its K-coset
  (index n_v/3) and a piece of the L-vertex of its L-coset (index n_x/3).
- (ii) For any vertex z, a nonempty piece g_zU_z cap c of a cell c is a left coset of U_z cap K cap L, whose index
  N_z in K cap L has all prime factors in {2, 3} or dividing r_z.
- (iii) Three nonempty pieces of three distinct vertices in one cell c are, after left translation of c onto K cap L,
  pairwise disjoint left cosets of subgroups of K cap L; if their indices in K cap L have pairwise gcds <= 2, this
  contradicts Sun(3) inside K cap L. In particular, if in a cell c the pieces of v and x and a possible piece of z have
  pairwise gcds of indices <= 2, then g_zU_z does not meet c (Sun(3) inside K cap L).
*Proof.* (i) L0.1 gives |LK| = |L||K|/|L cap K|, so LK = G gives [G : K cap L] = [G : K][G : L] = 9. Each left K-coset
is the union of [K : K cap L] = 3 cells, and two points y, y' of gK cap hL satisfy y^-1 y' in K cap L, so gK cap hL is
empty or a single cell; hence c -> (cK, cL) is an injective map from the nine cells to the nine pairs, so it is
bijective and every gK cap hL is a cell. If U_v subset K and m^L_v = 3, then g_vU_v, contained in g_vK, meets all three
left L-cosets hL; for y in g_vU_v cap hL one has g_vU_v cap hL = yU_v cap yL = y(U_v cap L), inside the cell
g_vK cap hL, and [K cap L : U_v cap L] = [G : U_v cap L]/9 = n_v [U_v : U_v cap L]/9 = n_v m^L_v/9 = n_v/3. The
statement for x is symmetric, and the last sentence of (i) follows by applying the vertex-wise statement to the vertex
of each coset. (ii) [G : U_z cap K cap L] = n_z [U_z : U_z cap K] [U_z cap K : U_z cap K cap L], both brackets are
integers <= 3, and N_z = [G : U_z cap K cap L]/9. (iii) Translating c to K cap L, the pieces are pairwise disjoint
(the cosets g_iU_i are) left cosets of subgroups of K cap L; apply Sun(3) inside K cap L. QED
````

### E19 (m11): CELL-A crossing count without t placement

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
- **m's.** For u in {x, y, w}: mu(U_uU_v1) = 4/6, so m^K_u >= 2; if m^K_u = 2, g_uU_u meets a K-coset containing the coset
  of v1, v2 or t, and Lemma IN at that apex (alpha_vu = alpha_tu = 4) gives m^K_u = 3. So m^K_u = 3.
````

New:

````text
- **m's.** For u in {x, y, w}: mu(U_uU_v1) = 4/6, so m^K_u >= 2 (IN, lower bound). As g_v1K != g_v2K (Lemma SUB:
  v1 and v2 occupy distinct K-cosets), any two of the three left K-cosets include g_v1K or g_v2K; so g_uU_u meets the
  K-coset of some v in {v1, v2}, and Lemma IN at apex v (U_v subset K, alpha_vu = 4) gives m^K_u = 3. The position of
  t is not used here. So m^K_u = 3.
````

### E20 (m10): CELL-A: LK = G from U_xK = G

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
m^L_j = 3. K != L since U_x is not inside K.
````

New:

````text
m^L_j = 3. K != L since U_x is not inside K; moreover U_xK = G (m^K_x = 3) and U_x subset L give LK = G, the
  hypothesis of Lemma CELL as restated (index 9 uses this, not K != L).
````

### E21 (m10): CELL-B: HK' = G from U*_aK' = G

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
(any two K'-cosets contain the coset of v1 or v2). K' != H.
````

New:

````text
(any two K'-cosets contain the coset of v1 or v2). K' != H; moreover U*_aK' = G (m^K'_a = 3)
  and U*_a subset H give HK' = G, the hypothesis of Lemma CELL as restated (with K := K', L := H).
````

### E22 (m10): CELL-B: t placement via vertex-wise (i)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
As in section 5, t cannot share a K'-coset with v1 or v2
````

New:

````text
As in section 5 (vertex-wise Lemma CELL (i) and (iii) with K := K', L := H), t cannot share a K'-coset with v1 or v2
````

### E23 (m12): CELL-B: N_z as a cell-piece index

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
Then N_z = [G : U*_z cap H]/9 = n_z m^H_z/9 is an integer only if m^H_z = 3, so
````

New:

````text
Then U*_z cap H = U*_z cap K' cap H (as U*_z subset K'), so every piece of z in a cell is a left coset of U*_z cap H,
  of index N_z = [K' cap H : U*_z cap H] = [G : U*_z cap H]/9 = n_z m^H_z/9 in K' cap H; N_z is an integer,
  v3(n_z) = 1 and 1 <= m^H_z <= 3, so m^H_z = 3 and
````

### E24 (m14): CELL section 7 link status

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
Each link is pending review; no exclusion of (a1) is asserted here.
````

New:

````text
The RICH link and the A1-STRUCT, K7-TC and K7-TC-A22 links are accepted at their stated scopes
  (verdicts 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0 and 2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966);
  the K7-CASEA-K23 and K7-CELL links await the parent R2 verdict; no exclusion of (a1) is asserted here.
````

### E25 (m14): package section 2 reading notes

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Old:

````text
Lemma EQ is read with erratum C.1 (odd parts of the local indices pairwise coprime).
````

New:

````text
Lemma EQ is read with erratum C.1 as amended by item R2.4 of `K7-R2-R3-consolidated-erratum-v1.md` (only the five
non-z local indices of g1, g2, s1, s2, s3 have pairwise coprime odd parts) and with item m9 of `K7-R2-repair-erratum-v1.md`.
The (R-c) quotation above is the frozen original: its R3' second vector (t weight 1) is superseded by
`K7-CASEA-K23-erratum-v1.md` (t weight 1/2), and R4/R5 and R6 are read with items m2 and m3 of `K7-R2-repair-erratum-v1.md`.
Lemma K3 is read with item R2.2, Lemma IN with item R2.3, and Lemma CELL in its vertex-wise restatement (item m10).
````

### E26 (m14): package import table statuses

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Old:

````text
| A1-STRUCT (section 0 triangle rule and two/four classes, Cor W3, E3, PFG-t + Cor L, Lemma B, CASEB) | `K7-A1-STRUCT-v1.md` | c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf | dual-reviewed 0/0/MINOR; overlay repair review RUNNING; NOT accepted |
| K7-TC (Lemma TC, R1 for every E >= 1, R3, Lemma FG-V, TC-B) | `K7-TC-v1.md` | cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117 | as above; R1 (E = 1) and FG-V are materially new overlay items |
| K7-TC-A22 (all-(2,2) Case A excluded) | `K7-TC-A22-v1.md` | 9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41 | as above; uses R1 at E = 1 |
| combined overlay | `K7-A1-A2-delta-erratum-v1.md` | 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e | repair review RUNNING |
````

New:

````text
| A1-STRUCT (section 0 triangle rule and two/four classes, Cor W3, E3, PFG-t + Cor L, Lemma B, CASEB) | `K7-A1-STRUCT-v1.md` | c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf | ACCEPTED-SCOPED (verdict 2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966; overlay v1 then v2); the triangle rule is cited through rules-k7-v1 L1 (T1)-(T3) |
| K7-TC (Lemma TC, R1 for every E >= 1, R3, Lemma FG-V, TC-B) | `K7-TC-v1.md` | cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117 | ACCEPTED-SCOPED (same verdict): R1 for every E >= 1; R3, R4, R5 at E >= 2; FG-V for finite G and actual families |
| K7-TC-A22 (all-(2,2) Case A excluded) | `K7-TC-A22-v1.md` | 9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41 | ACCEPTED-SCOPED (same verdict), every E >= 1 |
| combined overlays | `K7-A1-A2-delta-erratum-v1.md`, then `K7-A1-A2-delta-erratum-v2.md` | 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e; 9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181 | ACCEPTED-SCOPED as read by verdict 2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966 |
| R2 repairs (mandatory reading of the files under review) | `K7-CASEA-K23-erratum-v1.md`; items R2.1-R2.4 of `K7-R2-R3-consolidated-erratum-v1.md`; `K7-R2-repair-erratum-v1.md` | 15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1; ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940; see its own receipt | R2 candidate repairs; parent R2 verdict PENDING |
````

### E27 (m14): package scope link status

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Old:

````text
every link except RICH is pending.
````

New:

````text
the RICH, CASEB, K7-TC and K7-TC-A22
  links are accepted at their scopes (verdicts 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0 and
  2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966); K7-CASEA-K23 and Theorems K7-CELL-A/B await the parent R2 verdict.
````

### E28 (m1): package 44411 kill Sun accounting

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Old:

````text
(b = 3,
  k1 = 2 kill: Sun(2), Sun(3))
````

New:

````text
(b = 3,
  k1 = 2 kill: Sun(2) only; value 6 with y = 1/3 on the fours and 1 on the ones)
````

### E29 (m13): package Lemma IN imports

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Old:

````text
- Lemma IN: LFC (a)-(c) at the apex (the single weight y_i = 1 is feasible without any Sun instance); homogeneity of
````

New:

````text
- Lemma IN: LFC (a)-(b) at the apex (a count of distinct fibres; no weight vector and no Sun instance); homogeneity of
````

## Boundary

Unlisted text of every file is unchanged. Parent R2 verdict, the narrow repair review and any R3a/R3b consolidation are
parent-owned; if R3a/R3b findings arrive, they go into one later consolidated delta that does not modify this file.
K23 and CELL remain conditional candidates; (a1), the (a2) residues, K6.2*, full K7 and Sun(7) remain OPEN here.
No novelty, Lean or human-review claim.

`````

## 3. Exact ranges needed to assess m10 (Lemma CELL at its proved scope; callers)

#### CELL section 0 conventions (m^K_i, measures)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 15-21 (1-based, inclusive):

`````text
## 0. Conventions

Setting (a1) (RICH section 0). C is the configuration (subgroups U_j, representatives g_j) or its inverse (subgroups
g_jU_jg_j^-1, representatives g_j^-1); x denotes the alpha-matrix of C and x* that of its inverse, so in C:
mu(U_jU_k) = x_jk/6 (L0.3) and, at an apex a normalised g_a = 1, X_j := U_aU_j (measure x_aj/6), Y_j := G \ X_j,
D_j := U_a g_j U_j subset Y_j (V1) of measure x*_aj/6 with local index x*_aj r_j (INV (b)). For a subgroup K of G and a
vertex i, m^K_i := [U_i : U_i cap K] is the number of left K-cosets met by g_iU_i, and mu(U_iK) = mu(KU_i) = m^K_i/[G : K].
`````

#### Lemma SUB (distinct cosets used by m11)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 35-43 (1-based, inclusive):

`````text
## 2. Lemma SUB (index-3 subgroup) [NEW]

At an apex a of C (g_a = 1) let D_j = D_k with mu(D_j) + mu(X_j) = 1 (so D_j = Y_j), and suppose x_jk = x_aj = 2. Then
**K := U_aU_j = U_jU_k is a subgroup of index 3 containing U_a, U_j, U_k**, and g_aK, g_jK, g_kK are pairwise distinct
except that g_aK = g_kK is possible when x_ak != 2.
*Proof.* X_j = G \ D_k is right-invariant under U_k (D_k is) and under U_j, hence under <U_j, U_k>, and contains 1; so
<U_j, U_k> subset X_j and mu(<U_j, U_k>) <= 2/6. Also U_jU_k subset <U_j, U_k> and mu(U_jU_k) = x_jk/6 = 2/6. Hence
<U_j, U_k> = X_j = U_jU_k =: K, of measure 1/3, and U_a subset U_aU_j = K. Disjointness of g_iU_i and g_lU_l means
g_i^-1 g_l is not in U_iU_l (L0.2); U_aU_j = U_jU_k = K, and U_aU_k = K when x_ak = 2. QED
`````

#### Lemma IN (statement amended by ecff R2.3; proof sentence by E-item m13)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 45-54 (1-based, inclusive):

`````text
## 3. Lemma IN (counting inside a subgroup of index 3) [NEW]

Let K have index 3 and contain U_j for a vertex j (apex j of C). For every vertex i whose coset meets g_jK,
**x_ji < 2 m^K_i**; in particular, if x_ji = 4 then m^K_i = 3.
*Proof.* The fibres at j (left U_j-cosets) inside g_jK number n_j/3, one of them g_jU_j (no piece, LFC (b)). The left
multiplications by g_iug_i^-1 (u in U_i) preserve g_iU_i, the fibres and the set L_i of fibres meeting g_iU_i, and
permute transitively the m^K_i left K-cosets met by g_iU_i; so each of them contains t_i/m^K_i fibres of L_i, with
t_i = n_j x_ji/6 (LFC (a)-(b)). The weight y_i = 1 (all others 0) is feasible, so summing over the fibres inside g_jK:
n_j x_ji/(6 m^K_i) <= n_j/3 - 1 < n_j/3. QED
**Lower bound.** If U_l subset K and mu(U_iU_l) = x_il/6 > 1/3, then m^K_i >= 2 (U_iU_l subset U_iK).
`````

#### ecff Item 3 = R2.3 (IN i != j)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md` sha256 `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940`, lines 83-97 (1-based, inclusive):

`````text
### Item 3: R2.3 (Codex MINOR: IN excludes its own apex)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`.

Old:

````text
Let K have index 3 and contain U_j for a vertex j (apex j of C). For every vertex i whose coset meets g_jK,
````

New:

````text
Let K have index 3 and contain U_j for a vertex j (apex j of C). For every vertex i != j whose coset meets g_jK,
````
`````

#### Lemma CELL original statement/proof and (a1) remark (replaced by m10)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 56-75 (1-based, inclusive):

`````text
## 4. Lemma CELL [NEW]

Let K != L be subgroups of index 3, and let K contain U_v for three vertices v (the "K-vertices") whose cosets lie in the
three distinct left K-cosets, L contain U_x for three vertices x (the "L-vertices") whose cosets lie in the three
distinct left L-cosets, with m^L_v = 3 for every K-vertex and m^K_x = 3 for every L-vertex. Then:
- (i) [G : K cap L] = 9, and the nine left (K cap L)-cosets ("cells") correspond bijectively to the pairs
  (left K-coset, left L-coset); every cell contains a piece of the K-vertex of its K-coset (a left coset of U_v cap L, of
  index n_v/3 in K cap L) and a piece of the L-vertex of its L-coset (index n_x/3).
- (ii) For any other vertex z, a nonempty piece g_zU_z cap c of a cell c is a left coset of U_z cap K cap L, whose index
  N_z in K cap L has all prime factors in {2, 3} or dividing r_z.
- (iii) If in a cell c the three pieces of v, x and z have pairwise gcds of indices <= 2, then g_zU_z does not meet c
  (Sun(3) inside K cap L).
*Proof.* (i) U_xK = G for an L-vertex x, so LK = G and |L||K|/|L cap K| = |G|. A K-coset meets each L-coset in at most
one (K cap L)-coset and is the union of three of them, which gives the bijection. g_vU_v meets all three L-cosets
(m^L_v = 3), each in a left coset of U_v cap L subset K cap L, of index n_v m^L_v / 9 = n_v/3; likewise for x.
(ii) [G : U_z cap K cap L] = n_z [U_z : U_z cap K] [U_z cap K : U_z cap K cap L], and both brackets are integers <= 3.
(iii) Translating c to K cap L, the three pieces are pairwise disjoint left cosets of subgroups of K cap L. QED

In setting (a1), n_v/3 = 2 r_v with r_v = w_v for v in W and r_t = 3^A 5^Bt w_t; the w's are coprime to 30 and Bz Bt = 0.
Hence for v, x in W and any third vertex z: gcd(2 w_v, 2 w_x) = 2 and gcd(2 w_v, N_z), gcd(2 w_x, N_z) divide 2.
`````

#### Theorem K7-CELL-A (consumer)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 77-105 (1-based, inclusive):

`````text
## 5. Theorem K7-CELL-A (conditional) [NEW]

**No (a1) configuration lies in the K_{2,3} family of Theorem K7-CASEA-K23 (nor in its inverse).**

*Proof.* Work in C = C^alpha (the inverse family is the same statement for the inverted configuration, E6). Data
(K7-CASEA-K23): W = {v1, v2} cup {x, y, w}; alpha = 4 on v-(x,y,w) and t-(x,y,w), alpha = 2 inside {x, y, w} and on
v1 v2, alpha_zu = 3 on W, alpha_tv in {1, 2} not both 1; alpha* = 2 on v-(x,y,w), alpha* = 4 inside {x, y, w} and on
v1 v2, alpha*_tv = 4, alpha*_t in {1, 2} on {x, y, w}.
- **K.** Choose i in {1, 2} with alpha_tv_i' = 2 for the other index i' (possible as not both alpha_tv are 1). At apex
  v_i the masses alpha*_(v_i j)/6 are v_i' and t: 4/6, x, y, w: 2/6, z: 3/6 (local indices 4w, 4 3^A 5^Bt w_t, 2w,
  3 2^E 5^Bz w_z). Lemma EQ gives D_(v_i') = D_t; alpha_(v_i v_i') = 2 gives D_(v_i') = Y_(v_i'); Lemma SUB
  (j = v_i', k = t, x_jk = alpha_(v_i' t) = 2) gives K = U_v1U_v2 = U_(v_i')U_t of index 3 containing U_v1, U_v2, U_t,
  with v1, v2 and v_i', t in distinct K-cosets.
- **t has its own K-coset.** See the cell step below.
- **L.** By LFC (d) at t in C^alpha* (labels: v1, v2: 4w; a 3-side vertex with alpha*_t = 1: w, coprime to all), at most
  one of x, y, w has alpha*_t = 1 (y = 1/2 on v1, v2 and 1 on two such ones gives value 6). Take x with alpha*_tx = 2.
  At apex x the masses are y, w: 4/6; v1, v2, t: 2/6; z: 3/6. Lemma EQ gives D_y = D_w; alpha_xy = 2 gives D_y = Y_y;
  Lemma SUB (j = y, k = w, alpha_yw = 2) gives L = U_xU_y = U_yU_w of index 3 containing U_x, U_y, U_w, with x, y, w in
  distinct L-cosets (all alpha = 2 inside {x, y, w}).
- **m's.** For u in {x, y, w}: mu(U_uU_v1) = 4/6, so m^K_u >= 2; if m^K_u = 2, g_uU_u meets a K-coset containing the coset
  of v1, v2 or t, and Lemma IN at that apex (alpha_vu = alpha_tu = 4) gives m^K_u = 3. So m^K_u = 3. Likewise, for
  j in {v1, v2, t}: mu(U_jU_x) = 4/6, every L-coset contains one of x, y, w, and alpha_(u j) = 4 for u in {x, y, w}, so
  m^L_j = 3. K != L since U_x is not inside K.
- **Cells.** If t shared its K-coset with v1 (or v2), the cells of that K-coset would contain pieces of v1, t and an
  L-vertex u with indices 2w_v1, 2 3^A 5^Bt w_t, 2w_u, pairwise gcd 2: Lemma CELL (iii) applied to the vertex t (with
  N_t = 2 3^A 5^Bt w_t) excludes it. So v1, v2, t occupy the three K-coset and Lemma CELL applies. In a cell of the
  K-coset of v1 or v2 the pieces of v, u (an L-vertex) and z have pairwise gcds <= 2 (section 4), so g_zU_z meets none
  of these cells; hence g_zU_z lies in the K-coset of t, i.e. U_z subset K. Then U_zU_v1 subset K has measure <= 1/3,
  while mu(U_zU_v1) = alpha_zv1/6 = 1/2. Contradiction. QED
`````

#### Theorem K7-CELL-B (consumer)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-v1.md` sha256 `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`, lines 107-131 (1-based, inclusive):

`````text
## 6. Theorem K7-CELL-B (conditional) [NEW]

**No (a1) configuration lies in Case B (T = W != T*), nor in its mirror (T* = W != T).**

*Proof.* Work in C = C^alpha* (the mirror is the inverted configuration). Data (CASEB, K7-TC-B, K7-CASEB-T):
T* = {a1, a2, a3}, W \ T* = {v1, v2}; alpha: a-a 4, a-v 2, v1 v2 4, t-v 4, t-a 2; alpha*: a-v 4, a-a 2, v1 v2 2,
t-a 4, z-a 3, alpha*_tv in {1, 2}. In C the masses at an apex u are alpha_uj/6 and mu(U*_jU*_k) = alpha*_jk/6.
- **H.** At apex a1 the masses are a2, a3: 4/6; v1, v2, t: 2/6 (alpha_ta1 = 2); z: 3/6 (local indices 4w, 2w,
  2 3^A 5^Bt w_t, 3 2^E 5^Bz w_z). Lemma EQ gives D*_a2 = D*_a3; alpha*_(a1 a2) = 2 gives D*_a2 = Y*_a2; Lemma SUB
  (alpha*_(a2 a3) = 2) gives H = U*_a1U*_a2 = U*_a2U*_a3 of index 3 containing U*_a1, U*_a2, U*_a3; as alpha* = 2 on all
  a-a pairs, the three a's occupy the three H-cosets.
- **K'.** LFC (d) at t in C^alpha (labels a: 4w; v with alpha*_tv = 1: w) forbids alpha*_tv1 = alpha*_tv2 = 1 (y = 1/3 on
  the a's, 1 on the two ones: value 6). Choose i with alpha*_(t v_i') = 2. At apex v_i the masses are v_i': 4/6
  (alpha_v1v2 = 4), t: 4/6 (alpha_tv = 4), a1, a2, a3: 2/6, z: 3/6; Lemma EQ gives D*_(v_i') = D*_t;
  alpha*_v1v2 = 2 gives D*_(v_i') = Y*_(v_i'); Lemma SUB (alpha*_(v_i' t) = 2) gives K' = U*_v1U*_v2 = U*_(v_i')U*_t of
  index 3 containing U*_v1, U*_v2, U*_t.
- **m's.** m^H_v, m^H_t >= 2 (mu(U*_aU*_v) = mu(U*_aU*_t) = 4/6) and Lemma IN at the a's (alpha*_av = alpha*_at = 4) give
  m^H_v1 = m^H_v2 = m^H_t = 3; m^K'_a >= 2 (mu(U*_aU*_v1) = 4/6) and Lemma IN at v1, v2, t (alpha*_va = alpha*_ta = 4)
  give m^K'_a = 3 (any two K'-cosets contain the coset of v1 or v2). K' != H.
- **Cells.** As in section 5, t cannot share a K'-coset with v1 or v2 (pieces v, t, a with indices 2w_v,
  2 3^A 5^Bt w_t, 2w_a, pairwise gcd 2), so Lemma CELL applies with K-vertices v1, v2, t and L-vertices a1, a2, a3.
  z meets no cell of the K'-cosets of v1, v2 (pieces v, a, z, pairwise gcds <= 2), so U*_z subset K' and z lies in the
  K'-coset of t. Then N_z = [G : U*_z cap H]/9 = n_z m^H_z/9 is an integer only if m^H_z = 3, so
  N_z = 2^(E+1) 5^Bz w_z, and in every cell of that K'-coset the pieces of t, of the a and of z have indices
  2 3^A 5^Bt w_t, 2 w_a and 2^(E+1) 5^Bz w_z, pairwise gcd 2 (Bz Bt = 0): z meets no cell. Contradiction. QED
`````

#### CELLE C.1-C.4 (C.2 amended by m10; C.1 by ecff R2.4)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-erratum-v1.md` sha256 `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`, lines 1-60 (1-based, inclusive):

`````text
# K7-CELL-erratum-v1: four corrections to K7-CELL-v1 (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:40:17-0700.
- **Overlays:** `K7-CELL-v1.md` sha256 d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae, frozen byte-identical.
- **Source:** author's own re-read immediately after freezing (no review yet). No computation.
- C.1 states the coprimality of odd parts used in Lemma EQ; C.2 removes a citation of Lemma CELL (iii) whose hypothesis
  (distinct K-cosets) is what the step proves, and records that only CELL (i) and Sun(3) are used; C.3 is a typo;
  **C.4 corrects the configuration in which LFC (d) at t is applied in Theorem K7-CELL-B (C^alpha*, not C^alpha).**

**Item C.1.** Old:

```text
(local indices 4 times an odd number)
```

New:

```text
(local indices 4 times an odd number; the odd parts of all local indices involved are pairwise coprime, as they are products of distinct w's and of 3^A 5^Bt for t)
```

**Item C.2.** Old:

```text
Lemma CELL (iii) applied to the vertex t (with
  N_t = 2 3^A 5^Bt w_t) excludes it.
```

New:

```text
these three pieces are pairwise disjoint left cosets of subgroups of K cap L after translation; this uses only part (i)
  of Lemma CELL (which needs U_xK = G for an L-vertex x, not the distinctness of the K-cosets) and Sun(3), and excludes it.
```

**Item C.3.** Old:

```text
So v1, v2, t occupy the three K-coset and Lemma CELL applies.
```

New:

```text
So v1, v2, t occupy the three K-cosets and Lemma CELL applies.
```

**Item C.4.** Old:

```text
LFC (d) at t in C^alpha (labels a: 4w; v with alpha*_tv = 1: w)
```

New:

```text
LFC (d) at t in C^alpha* (the inverted configuration, whose alpha-matrix is alpha*; labels a: 4w; v with alpha*_tv = 1: w)
```

No other change. Every statement of K7-CELL-v1 is unchanged; it remains a conditional candidate.
`````

#### README L0.1, L0.2 (accepted via written verdict)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/README.md` sha256 `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1`, lines 21-23 (1-based, inclusive):

`````text
**Elementary facts used throughout** (G finite; proofs in sun-coset5 rules-v1 L0, which hold for arbitrary indices):
- **L0.1** |XY| = |X||Y|/|X∩Y| for subgroups X, Y.
- **L0.2** gU ∩ hV = ∅ iff g⁻¹h ∉ UV.
`````

## 4. Exact ranges needed to assess m7 (rigid rows and K3 at the actual Case-B labels)

#### K23 section 0 (Case-A conventions)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` sha256 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`, lines 16-25 (1-based, inclusive):

`````text
## 0. Setting and conventions

(a1), **Case A**: T = T* = W. By Corollary W3, E3 and NO5 every W-W and W-t entry of alpha and alpha* lies in {1,2,4},
and x_uz = 3 for every u in W and x in {alpha, alpha*}. F := {uv in W : alpha_uv = 4}, F* := {uv : alpha*_uv = 4}
(disjoint, INV), N := the pairs of W in neither; d(u), d*(u) are the F- and F*-degrees in W; P := {u : alpha_tu = 4},
P* := {u : alpha*_tu = 4} (disjoint). A row is written (W-multiset | e) with e = x_ut (x_uz = 3 understood); its fours,
twos, ones are its W-entries 4, 2, 1. C^x is the configuration whose alpha-matrix is x. In C^x the rows at u are x-rows,
and at an apex a in W the VFC sets D_j = D_j^(a) have measure x*_aj/6 and local indices x*_aj r_j (INV (b)); **Lemma
FG-V** gives mu(union of the D_j^(a)) <= 5/6 for a in W, in C^alpha and in C^alpha*. "u is single-x-four" means
d(u) = 1 (x = alpha), resp. d*(u) = 1 (x = alpha*). L_j denotes the union of the fibres at u meeting j's coset.
`````

#### K23 (R-c) rows and Lemma K3 (R3' via K23E; K3 first line via ecff R2.2)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` sha256 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`, lines 38-53 (1-based, inclusive):

`````text
- (R-c) **Rigid rows.** For each row below two feasible weight vectors of value 5 are displayed; by the equality
  clause every occupied fibre C at u has weight 1 under both, which gives the stated containment.
  - R1 = (2,2,4,4 | 2) (K7-TC, every E >= 1) and **R1- = (2,2,4,4 | 1)** (y = (f 1/2, f' 1/2, t 1) and
    (s 1/2, s' 1/2, f 1/2, t 1); t's label 3^A w_t meets only z): **L_f = L_f'** for the two fours.
  - **R5 = (1,2,4,4 | e)** and **R4 = (1,4,4,4 | e)**, e in {2,4} (y_i = (o 1, f_i 1); o's label is prime to all): every
    occupied fibre C with o not in S_C contains every four; so **L_j subset L_f for every four f and every j != o**.
  - **R6 = (2,4,4,4 | 1)** (y_i = (f_i 1, t 1)): every occupied fibre other than those with S_C in {{t}, {t, z}}
    contains all three fours; so **L_s subset L_f** for the two s and every four f.
  - R3 (K7-TC) and **R3'** (y = (o 1, f 1/2, s 1/2, s' 1/2) and (o 1, s 1/2, s' 1/2, t 1); {f,s,s'}, {t,s,s'}, {z,s,s'} have
    all gcds 2; {f,t,s}, {z,t,s}, {z,f,s}, {z,f,t,s} are allowed of weight 1 (E >= 2)): **L_f = L_t and L_z subset L_t**.
  - (1,2,4,4 | 1) and (1,4,4,4 | 1) do not occur (y = (o 1, fours 1/2 resp. 1/3, t 1) has value 6). The remaining rows,
    R2 = (2,2,4,4 | 4) and (2,4,4,4 | e) with e in {2,4}, are called slack; nothing is claimed for them.

**Lemma K3 (transfer kill) [NEW].** If u in W has a rigid x-row forcing L_j subset L_a (a in W \ {u}, j != u), then in
C^x at apex a, D_j cap D_u = empty (Lemma TC), so by Lemma FG-V **x*_aj + x*_au <= 5**. In particular x*_aj = 4 and
x*_au >= 2 is impossible.
`````

#### ecff Item 2 = R2.2 (K3 distinct vertices)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-R2-R3-consolidated-erratum-v1.md` sha256 `ecff4e76605746f2e53b5ca5e779560bade7a47592e12a72ea4ab1052cce9940`, lines 66-81 (1-based, inclusive):

`````text
### Item 2: R2.2 (Codex MINOR: K3 distinct vertices)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
**Lemma K3 (transfer kill) [NEW].** If u in W has a rigid x-row forcing L_j subset L_a (a in W \ {u}, j != u), then in
````

New:

````text
**Lemma K3 (transfer kill) [NEW].** Let u,a,j be pairwise distinct, with u,a in W. If the rigid x-row at u forces
L_j subset L_a, then in
````
`````

#### Proposition K7-CASEB-T (consumer; m7)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` sha256 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`, lines 148-154 (1-based, inclusive):

`````text
## 5. Proposition K7-CASEB-T (conditional) [NEW]

**In Case B (Theorem CASEB and Theorem K7-TC-B), alpha_ta = 2 and alpha*_ta = 4 for every a in T*.**
*Proof.* v1's alpha-row is R3 (four v2; twos a1, a2, a3), with alpha_tv1 = 4. For a in T*, the alpha*-row of a is
(2,2,4,4 | alpha*_ta) (alpha*_za = 3; fours v1, v2; twos the other two a's, by K7-TC-B). If alpha*_ta is 1 or 2 it is R1-* or
R1*, so L*_v1 = L*_v2 at a, and at apex v1 in C^alpha* the masses alpha_v1v2 = 4 and alpha_v1a = 2 contradict K3. So
alpha*_ta = 4, alpha_ta <= 2, and alpha_ta = 2 (CASEB: alpha_ta in {2, 4}). QED
`````

#### Theorem CASEB (accepted, VA1)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-STRUCT-v1.md` sha256 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`, lines 118-133 (1-based, inclusive):

`````text
## 5. Theorem K7-CASEB (conditional on RICH) [NEW]

**If T = W and T* != W, then |T*| = 3; writing T* = {a1, a2, a3} and W \ T* = {v1, v2}: E >= 2; alpha_v1v2 = 4;
alpha_tv = 4 (v = v1, v2); alpha_av = 2 for all a in T*, v in {v1, v2}; alpha_aa' = 4 for all a != a' in T*;
alpha_ta in {2, 4} for every a in T*, with alpha_ta = 2 and alpha*_ta = 4 for at least two a; alpha*_av = 4; alpha*_aa',
alpha*_v1v2, alpha*_tv, alpha*_zv lie in {1, 2}.** (The case T* = W, T != W is the same with alpha and alpha* exchanged.)

*Proof.* TZ (ii) for alpha* gives alpha* = 4 on T* x (W \ T*), so alpha <= 2 there (INV). Each v in W \ T* has c = 3
(T = W) and at least |T*| >= 3 W-entries <= 2; by Lemma B its W-part has exactly one 4, E >= 2 and alpha_vt = 4. The 4
cannot point into T*, so |W \ T*| >= 2 and |T*| = 3, alpha_v1v2 = 4. Triangle {v1, v2, a}: entries (4, alpha_v1a,
alpha_v2a) with the last two <= 2; only (2, 2, 4) passes, so alpha_av = 2. For a in T*: the t-triangle {t, a, v} has entries
(alpha_ta, 4, 2), so alpha_ta != 1, i.e. alpha_ta in {2, 4} (E3, NO5). Gamma^alpha contains all six a-v edges and is
connected, so Corollary L applies in C^alpha: t's alpha*-row on W has at least two entries 4, and alpha*_tv <= 6 - 4 = 2, so
at least two a have alpha*_ta = 4, hence alpha_ta <= 2, hence alpha_ta = 2. For such an a, Lemma B (which would force
alpha_ta = 4 if a had three W-entries <= 2) gives alpha_aa' = alpha_aa'' = 4; two such a make all three T*-edges 4. The
alpha*-statements follow from INV and the 3-type alpha*-row at z (D23-MIX). QED
`````

#### Lemma TC, rigidity source and R1 (accepted, VA1)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-v1.md` sha256 `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`, lines 22-40 (1-based, inclusive):

`````text
## 1. Lemma TC (transfer) [NEW]

**For distinct vertices u, a, j and C in {C^alpha, C^alpha*}: L_j^(u) subset L_a^(u) iff D_j^(a) subset X_u^(a)
(g_a = 1). In that case D_j^(a) cap D_u^(a) = empty.**

*Proof.* Both statements are invariant under a common left translation; take g_a = 1, so L_a^(u) = U_aU_u. If
g_jU_jU_u subset U_aU_u then g_jU_j subset U_aU_u, so U_a g_j U_j subset U_aU_aU_u = U_aU_u. Conversely, if
U_a g_j U_j subset U_aU_u then g_jU_jU_u subset U_a g_j U_j U_u subset U_aU_u. Finally D_u^(a) cap X_u^(a) = empty (V1). QED
(RICH's Lemma TR is the case (j, a) = (t, z).)

**Rigidity source (RICH Corollary 5/6, equality clause).** At u in W, if feasible weights y_1, ..., y_m (for C's labels at u)
all have value 5, then every fibre meeting a coset has an allowed S-set S with y_i(S) = 1 for every i. Hence: if every
allowed S with y_i(S) = 1 (all i) and j in S contains a, then L_j^(u) subset L_a^(u).

## 2. Rigid rows used (E >= 2 throughout; each value-5 weight is feasible and FG gives <= 5, so it is optimal)

- **R1 = ({2,2,4,4} | 3 | 2)**, fours f1, f2, twos s1, s2. Maximal allowed sets: {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
  (z-t gcd 6). y_A = (f1 1/2, f2 0, s 1/2, 1/2, t 1/2, z 0) and y_B (f1 0, f2 1/2, rest equal) have value 5. y_A(S) = y_B(S)
  forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.**
`````

#### overlay v1 TC.4 (R1 for every E >= 1)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v1.md` sha256 `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`, lines 263-276 (1-based, inclusive):

`````text
**Item TC.4.** `K7-TC-v1.md`, section 2, R1. Old:

```text
forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.**
```

New:

```text
forces [f1 in S] = [f2 in S]. **L_f1 = L_f2.** *E = 1 (needed only for K7-TC-A22):* the only label gcds at u
  that change are those between z and the two fours, which drop from 4 to 2 (gcd(z, t) = 6 and gcd(z, s) = 2 are
  unchanged); this only removes allowed sets, so y_A and y_B (both vanish on z) stay feasible of value 5, and
  y_A - y_B = (1/2)([f1] - [f2]) still forces L_f1 = L_f2. Hence R1 holds for every E >= 1.
```
`````

#### overlay v2 V2.2 (R1 list tag)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v2.md` sha256 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`, lines 30-44 (1-based, inclusive):

`````text
## V2.2 — optional R1 list tag; original TC section 2

Target: `D/K7-TC-v1.md`.

Old:

````text
twos s1, s2. Maximal allowed sets: {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
````

New:

````text
twos s1, s2. Maximal allowed sets (E >= 2): {f1,f2,z,s_i}, {f1,f2,z,t}, {z,t,s_i}, {s1,s2}
````
`````

#### Theorem K7-TC-B statement (accepted, VA1)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-v1.md` sha256 `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`, lines 53-56 (1-based, inclusive):

`````text
## 3. Theorem K7-TC-B (conditional) [NEW]

**In Case B of Theorem CASEB (T = W, T* = {a1,a2,a3} != W, W \ T* = {v1,v2}): alpha*_v1v2 = 2 and alpha*_aa' = 2 for all
a != a' in T*.**
`````

#### overlay v1 TC.7 (Lemma FG-V)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v1.md` sha256 `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`, lines 302-319 (1-based, inclusive):

`````text
**Item TC.7.** `K7-TC-v1.md`, before section 3 (insert Lemma FG-V). Old:

```text
## 3. Theorem K7-TC-B (conditional) [NEW]
```

New:

```text
**Lemma FG-V (VFC union bound) [NEW].** Let a in W and C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for
C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C. Then mu(union over j != a of D_j^(a)) <= 5/6.
*Proof.* Put Y := intersection of the U^C_j (j != a). For every j != a, U^C_a Y lies in U^C_a U^C_j = X_j^(a), which
is disjoint from D_j^(a) by (V1); so U^C_a Y avoids the union. G0 gives mu(U^C_a Y) >= 1/gcd(n_a, [G : Y]), and FG7 (b)
(N = Q = V \ {a}, V_j = U^C_j, beta = the alpha-matrix of C, <= 5 by E1, resp. INV (b) with E1) gives
gcd(n_a, [G : Y]) | 6. QED

## 3. Theorem K7-TC-B (conditional) [NEW]
```
`````

#### overlay v2 V2.3 (FG-V finite G)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v2.md` sha256 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`, lines 46-63 (1-based, inclusive):

`````text
## V2.3 — optional finite-G note; Item TC.7 New field

Target: `D/K7-A1-A2-delta-erratum-v1.md`.

Old:

````text
**Lemma FG-V (VFC union bound) [NEW].** Let a in W and C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for
C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C. Then mu(union over j != a of D_j^(a)) <= 5/6.
````

New:

````text
**Lemma FG-V (VFC union bound) [NEW].** Work in finite G (R0 lifts the statement to arbitrary G). Let a in W and
C in {C^alpha, C^alpha*}, with subgroups U^C_j (U_j for C^alpha, g_jU_jg_j^-1 for C^alpha*), normalised g_a = 1 in C.
Then mu(union over j != a of D_j^(a)) <= 5/6.
````
`````

#### RICH Corollary 5/6 with equality clause (accepted, VRICH)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23RICH-D23P-erratum-v1.md` sha256 `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428`, lines 102-117 (1-based, inclusive):

`````text
**Item 2a.** `K7-D23-RICH-v1.md`, section 1, statement of Corollary 5/6. Old:

```text
**Corollary 5/6.** For u in W, x in {alpha, alpha*} and every feasible y at u: **val(y) <= 5**. If val(y) = 5, then
every left fibre at u (orientation x) that meets one of the cosets carries weight exactly 1.
```

New:

```text
**Corollary 5/6.** For u in W, x in {alpha, alpha*} and every feasible y at u: **val(y) <= 5**. For a fibre C at u
in orientation x (a left coset of the subgroup of u, other than the coset of u itself, in the configuration if
x = alpha and in the inverted configuration if x = alpha*) let S_C be the set of j != u whose coset meets C, and call
sum_(j in S_C) y_j the weight of C. If val(y) = 5, then sum_(j in S_C) y_j = 1 whenever S_C is non-empty, i.e. every
left fibre at u (orientation x) that meets one of the cosets carries weight exactly 1.
```
`````

## 5. Accepted rule authorities for the triangle and import citations

#### rules-k7 L0.3, L1 (T1)-(T3) triangle rule

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md` sha256 `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee`, lines 17-24 (1-based, inclusive):

`````text
**L0.3 [GEN].** μ(U_iU_j) = α_ij / g_ij and 1 ≤ α_ij ≤ g_ij − 1. Per gcd: g = 2 ⇒ α = 1; g = 3 ⇒ α ∈ {1,2}; g = 4 ⇒ α ∈ {1,2,3}; g = 5 ⇒ α ∈ {1,…,4}; g = 6 ⇒ α ∈ {1,…,5}.

**L1 (T) [GEN, general form].** For a triangle {a,b,c} let L = lcm(n_a,n_b,n_c) and T = [G:U_a∩U_b∩U_c]. Then L | T; put τ = T/L. For every labelling {x,y,z} = {a,b,c}:
- **(T1)** I_xy | Lτ, equivalently α_xy | ℓ_z·τ. *Proof:* I_xy = lcm(n_x,n_y)α_xy, and L = lcm(n_x,n_y)·ℓ_z because lcm(lcm(n_x,n_y), n_z) = lcm(n_x,n_y)·n_z/gcd(n_z, lcm(n_x,n_y)).
- **(T3)** μ(U_y(U_x∩U_z)) = τ / (γ_y·α_xz). *Proof:* by L0.1 it equals Lτ/(n_y I_xz) = Lτ/(n_y lcm(n_x,n_z) α_xz), and L/lcm(n_x,n_z) = ℓ_y = n_y/γ_y.
- **(T2)** μ(U_y(U_x∩U_z)) ≤ min(μ(U_yU_x), μ(U_yU_z)), since U_y(U_x∩U_z) ⊆ U_yU_x ∩ U_yU_z.

Hence τ is a multiple of τ_min := lcm over the three edges of α_xy / gcd(α_xy, ℓ_z), and τ ≤ τ_max := min over apexes y of ⌊γ_y·α_xz·min(α_xy/g_xy, α_yz/g_yz)⌋. **T-kill:** τ_min > τ_max. (Core specialisation: when all indices are d·r_i with r_i pairwise coprime, γ = d and ℓ_z = r_z, recovering the k5/k6 forms.)
`````

#### written verdict header (rules-k7 accepted)

`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` sha256 `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35`, lines 1-11 (1-based, inclusive):

`````text
# Sun k7: written reduction/rules accepted, finite exclusions pending

Recorded at 2026-10-18T14:24:47-07:00.

**CORRECTNESS-ACCEPTED for the written statements and active rule soundness below, with the mandatory overlay. No Sun(7) theorem and no class exclusion are accepted by this verdict.** All six residual classes remain OPEN pending full independent finite coverage checks. The late specification/freeze violation remains an unresolved process MAJOR for the exploratory A/B promotion, not an erased historical event.

## Exact texts and review dispositions

- [Frozen k7 reduction](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/README.md), SHA256 `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1`.
- [General rules](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-v1.md), SHA256 `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee`.
- [RPLP/CAP addendum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/rules-k7-addendum-v1.md), SHA256 `fb2c306b17a258181bb770c7c6c38585da77c0e312c68463cee7dc0f15fd1066`.
`````

#### written verdict: triangle T, K, P, VFC accepted as sound necessary rules

`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` sha256 `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35`, lines 23-23 (1-based, inclusive):

`````text
- Active triangle T, containment/packing K/K1/K2, grid/Bonferroni P, VFC and RPLP rules are sound necessary conditions with every stated universal subset/q condition. CAP preserves all active quantities using capped profiles(min(e,4),min(f,2),min(h,2)) under the explicit pairwise-min/coprime hypotheses; the five-vertex control universes have their own hypotheses in addendumA3.
`````

#### Z2 erratum G5 (L1 in the inverted configuration)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-Z2-erratum-v1.md` sha256 `3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9`, lines 43-47 (1-based, inclusive):

`````text
## G5 (Claude 5): complete import list

Add: **R0** (README section 1; theorem statement), **LFC (a), (c), (d)** by name, **Sun(2)** (erratum E2; used via (V3)
in LIGHT (L2)), **E6**, and the note that **L1 (T1)-(T3) and (F7) are applied to the inverted configuration as well**
(Lemma CROSS for alpha*, T1 inverted step, T2).
`````

#### A1-STRUCT section 0: triangle specialisation and two/four classes

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-STRUCT-v1.md` sha256 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`, lines 21-30 (1-based, inclusive):

`````text
**Triangle evaluation used throughout.** For a triangle all of whose vertices are in W, or {t, a, b} with a, b in W,
and whose three entries lie in {1, 2, 4}, every ell-divisor is trivial (w's and 3^A 5^Bt are prime to 2), so with the
entries sorted p <= q <= r: tau_min = lcm = r and tau_max = min(r p, p q, q p) = p q. **T passes iff r <= p q**:
allowed (1,1,1), (1,2,2), (1,4,4), (2,2,2), (2,2,4), (2,4,4), (4,4,4); forbidden (1,1,2), (1,1,4), (1,2,4).

**Allowed sets of a two/four class.** For local indices or labels 2^i w (i in {1, 2}; "twos" and "fours") with pairwise
coprime w's prime to 30, the pairwise gcds are 2, except 4 between two fours. Hence (through LFC (c) / VFC (V3)) the
allowed sets inside such a class are exactly: singletons, all pairs, the triples with >= 2 fours (Sun(3)), the 4-sets
with >= 3 fours (Sun(4)); no 5-set is allowed (five pieces with pairwise gcds <= 4) [Sun(5)]. Elements of local index or
label w alone ("ones") lie only in singletons (Sun(2)).
`````

#### LFC (a)-(b)

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-v1.md` sha256 `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`, lines 20-27 (1-based, inclusive):

`````text
Let G be finite, let g_1U_1, ..., g_kU_k (k <= 7) be pairwise disjoint left cosets, and fix a vertex v.
For j != v put

  lambda_j := [U_v : U_v cap U_j],   t_j := [U_j : U_j cap U_v].

**(a)** lambda_j = I_vj / n_v = n_j alpha_vj / g_vj and t_j = I_vj / n_j = n_v alpha_vj / g_vj.

**(b)** g_jU_j meets exactly t_j left cosets of U_v, and none of them is g_vU_v.
`````

#### INV erratum E6

`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/K7-LFC-INV-erratum-v1.md` sha256 `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`, lines 47-53 (1-based, inclusive):

`````text
## E6 (Claude m7): "same class" in INV (a)

Replace the clause "so it lies in the same class (K7, K6.2*, K6.3, K5.2*, K5.3, KII) with the same marking" by: "so it
has the same labelled index tuple (n_1, ..., n_7). Every class of README section 5 (and the marking, i.e. which vertex
carries e >= 2, f >= 2 or h >= 1) is defined from the labelled index tuple alone, so the inverted configuration lies in
the same class with the same marking." The parent has read the class definitions (README section 5, sha256
2a6d6d6e...) directly. The only load-bearing use in K7-LFC-INV-v1 is Theorem K7-M0, where the hypothesis itself
`````

#### A1/A2 parent verdict (full)

`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` sha256 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`, lines 1-56 (1-based, inclusive):

`````text
# Sun(7) lane: K7 A1-STRUCT, TC, TC-A22 and A2-FIVE repairs

Recorded at 2026-10-19T08:24:22-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** This verdict accepts written, model-reviewed proofs relative to the accepted RICH/D23P verdict (`1167bc4f…`) and LFC/INV verdict (`8621e744…`). Every closure includes the computer-assisted Sun(5)/Sun(6) imports. K6.2*, full K7 and Sun(7) all remain **OPEN**.

## Text of record

The four frozen sources are read through [overlay v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v1.md) `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` and then [overlay v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-A2-delta-erratum-v2.md) `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`, which amends v1:

| Source | sha256 |
|---|---|
| [A1-STRUCT](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A1-STRUCT-v1.md) | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` |
| [TC](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-v1.md) | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` |
| [TC-A22](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-TC-A22-v1.md) | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` |
| [A2-FIVE](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-FIVE-v1.md) | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` |

The parent read v2 in full. It implements the reviewers' minimal fixes and strengthens no statement. In particular:
- V2.6 states the actual-family marked-first chain for every Q, including empty and singleton Q. This removes the remaining reliance on the earlier FG7-use inventory.
- V2.7 adds β_zu ≤ 3 on W′ via D23P, and adds (iv′) for the new R1/A22 consumers.
- V2.8 replaces the TC-P proof with Codex's minimal one: R1 at u3 and Lemma TC at u4 give D_u2∩D_u3=∅; then 4/6 + 2/6 = 1, which contradicts V4.

## Accepted conclusions

**(a1)**
- Corollary W3 (W3 = W3* = ∅, and all W–W entries in {1,2,4}); Lemma E3; Lemma PFG-t (i)/(ii) under connectivity, with Corollary L as a necessary condition only; Lemma B and Theorem CASEB under their stated hypotheses.
- Lemma TC and Lemma FG-V (finite G; actual families only).
- R1 for every E≥1; R3, R4, R5 and the ({1,4,4,4}|c|1) exclusion for E≥2.
- Theorem K7-TC-B: α*_v1v2 = 2 and α* = 2 on T*.
- Proposition TC-P for the TC.11 matrix data. It is generalised to every E≥1 via TC.4, so Pc5′ is not realised.
- Theorem K7-TC-A22 for every E≥1 and every group. Case A with two fours in each orientation at every W-vertex is excluded.

**(a2)**
- Lemma F: only the z–t entry can be 5, and in at most one orientation.
- FG-a2, Corollary 5/6-a2, D23-a2, and Proposition ZT5 (S1)–(S5).
- Theorem K7-A2-BRIDGE in its enumerated A2.10 form.
- Corollary K7-A2-TRANSFER for exactly its named list in (a2-no5), with W = W′∪{p}.

## Reviews

- [Codex repair review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repair-codex-v1.prompt.stdout.txt) `1697abdf74e577e7ec9ab673bb50b3161bfce6b836816e602536a1f45af4ecde`, observed gpt-6.1-sol max, read-only: ACCEPT_REPAIRS_WITH_FIXES, 0 FATAL / 0 MAJOR / 3 MINOR (M1–M3), all folded into v2.
- [Claude repair review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repair-claude-v1.prompt.note.md) `66c93000ab9a35aaa34b004e6262e82b698dd657dd283c613366d91dd4bf8157`, observed claude-opus-5-5 max, no tools: 0 FATAL / 0 MAJOR / 7 MINOR plus 4 optional, all folded into v2.

## Not accepted or open

- **Bound by their own hypotheses:** PFG-t (connectivity), CC (separation), TC-B (Case B), A22 (Case A plus the A22 hypothesis), and S1–S4 (survivors only).
- **Not transferred:** FG7 for auxiliary families; RICH §§6 and 9; A1-STRUCT §§6–7; TC §§5–6, including Q_B′; A22 §4.
- **Open:**
  - (a1) as a whole;
  - Case A four-degree patterns (3,1), (1,3), (2,1), (1,2);
  - the Case B residue;
  - (a2-zt5) beyond S1–S5;
  - the (a2-no5) residue;
  - K6.2*, full K7 and Sun(7).
- **Pending, not part of this verdict:** the candidates CASEA-K23, K7-CELL, the A2-ZT5 errata v1–v4 and the conditional closure map. They are pending their own dual review.
- **No novelty claim.**
`````

#### RICH/D23P verdict (accepted statements)

`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` sha256 `1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0`, lines 1-14 (1-based, inclusive):

`````text
# Sun(7) lane: K7-D23-RICH and K7-D23P

Recorded at 2026-10-19T06:24:26-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Both are written proofs, produced by a model and reviewed by models of both families. This is not a Lean or human check.

## Accepted statements (exact scope)
- **K7-D23-RICH, setting (a1).** Texts: [RICH-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-RICH-v1.md) `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3`, with [erratum-1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-RICH-erratum-v1.md) `8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69` (whose R-1 replacement of the last NO5(a) branch is mandatory) and the [consolidated erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23RICH-D23P-erratum-v1.md) `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428`.
  - No K7 configuration in setting (a1) has T* ⊆ W3 or T ⊆ W3*.
  - The structural lemmas G0, FG7 (chain form), Cor 5/6 with its equality clause, NO5, R3 (survivors S1–S4 are local-test survivors only), TR, CC, TZ (i)–(iii) and LZ hold at their stated scopes.
  - The abstract pattern P is excluded only conditionally, as a navigation remark: **if** it has T* ⊆ W3 or T ⊆ W3*, it is not realised. No other local pattern is excluded.
- **K7-D23P, setting (a2).** Texts: [D23P-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23P-v1.md) `89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880` with the consolidated erratum.
  - No configuration in setting (a2) has a 4-type z-row in either orientation, so both z-rows are of type (b′).

`````

#### LFC/INV verdict (accepted statements)

`/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-lfc-inv-parent-verdict-v1.md` sha256 `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18`, lines 16-23 (1-based, inclusive):

`````text
## Accepted statements and parent derivation

1. **LFC, k≤7.** For disjoint left cosets and a fixed vertex v, lambda_j=[U_v:U_v∩U_j]=n_j alpha_vj/g_vj, and g_jU_j meets t_j=n_v alpha_vj/g_vj left U_v-fibres. A common point p writes each intersection as p(U_j∩U_v); after translating into U_v these are disjoint left cosets with those lambda indices. At most six pieces share any nonexclusive fibre. Sun(t),2≤t≤6, applied to every subfamily gives the hereditary allowed-set condition. Summing feasible weights over the n_v−1 fibres gives sum y_j alpha_vj/g_vj≤1−1/n_v<1. No conjugation is missing from this left-fibre argument.
2. **INV.** Invert each coset and write it as g_i^−1(g_iU_i g_i^−1). This preserves disjointness and the labelled index tuple. With h=g_v^−1g_j, the double coset U_v h U_j has measure alpha*_vj/g_vj. It is disjoint from U_vU_j, so alpha_vj+alpha*_vj≤g_vj. The original VFC(V1) defines q by that same double-coset measure, hence q=alpha*. The parent directly read VFC(V1) and the index-defined class definitions; same-class assertions do not extend to classes defined using additional unpreserved data.
3. **ROW-U.** In K7, a vertex with six unmarked neighbours has only alpha∈{1,2,4}, at most one 1 and at least three 4s. Pairwise-coprime w_j prime to30 reduce fibre gcds to gcds of alpha≤5. The R1/R24/R3/R5 feasible weights in the candidate cover every hereditary subset; for N entries of R1∪R24 the value is at least min(N,4). Every excluded row gives a value≥6, contradicting LFC.
4. **K7-M0.** If all seven indices are 6w_i, with w_i pairwise coprime and prime to30, ROW-U applies globally to alpha and alpha*. Each vertex has at least three alpha=4 and at least three alpha*=4 edges, disjoint by INV. Thus exactly three alpha=4 edges meet every vertex. Symmetry would give a 3-regular graph on seven vertices, with odd degree sum21, impossible. This excludes the previously open all-2 singleton pattern and the entire unmarked Q24 branch, not only a bounded range.
5. **K63-U0.** Six indices 6w_i and one 3w_d, all w pairwise coprime and prime to30, cannot occur. If some C–d alpha=1, the d fibre contributes1/3 and the five other C-neighbours contribute at least4/6, contradicting LFC. Therefore all C–d alpha=2. At d the six local indices are4w_i; weights1/4 give total1, another contradiction.
6. **Arbitrary groups.** The intersection of the finitely many subgroup cores is normal, finite-index and contained in every subgroup. The quotient preserves indices, intersections and coset disjointness; normality also preserves the conjugated intersections in INV. Therefore the finite arguments lift to the stated arbitrary-group scopes.
`````

## 6. Reviewer focus (narrow)

1. m10: the restated Lemma CELL proves exactly its statement from LK = G (index 9, cell bijection, vertex-wise pieces
   of index n_v/3); that CELL-A obtains LK = G from U_xK = G (m^K_x = 3, U_x in L) and CELL-B obtains HK' = G from
   U*_aK' = G before t's placement is known; that C.2's t-step and both final cell contradictions need only the
   vertex-wise form; that the S_3 remark is correct; that the previous form is a special case.
2. m7: that R1 (accepted TC row, every E >= 1), R1- and Lemma K3 read only the displayed labels at a in T* plus RICH
   Corollary 5/6, Lemma TC and FG-V, all valid at the actual Case-B data of CASEB and K7-TC-B.
3. m5: the listed F- and F*-neighbourhoods in (S-f) and the resulting alpha = 2 / alpha* = 2 entries; that the (S-f)
   step list is otherwise unchanged and every K3 application has the stated masses.
4. m1-m4, m6, m8, m9, m11-m14: wording/citation/metadata only; check that no statement is strengthened, original
   scopes and the transitive computer-assisted Sun(5)/Sun(6) imports are retained, and no (a1) closure is asserted.
