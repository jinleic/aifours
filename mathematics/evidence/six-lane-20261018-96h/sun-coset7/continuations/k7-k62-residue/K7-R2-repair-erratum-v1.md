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
