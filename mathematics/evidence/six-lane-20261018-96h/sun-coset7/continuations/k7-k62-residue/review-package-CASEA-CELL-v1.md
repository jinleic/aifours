# Review package: K7-CASEA-K23 + K7-CELL (with self-erratum) + K7-CELL section 7 (conditional chain)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:45:36-0700.
- **Owner:** Sun7K62Successor. Manifest only (no new mathematics, no computation). To be routed by the parent after the
  A1/A2 overlay verdict.

## 1. Files under review (frozen, byte-identical)

| file | sha256 | written |
|---|---|---|
| `K7-CASEA-K23-v1.md` | f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3 | 2026-10-19T07:26:58-0700 |
| `K7-CELL-v1.md` | d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae | 2026-10-19T07:39:34-0700 |
| `K7-CELL-erratum-v1.md` (self-erratum C.1-C.4; C.4 corrects LFC at t in Theorem K7-CELL-B to C^alpha*) | 56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132 | 2026-10-19T07:40:17-0700 |

Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/`.

## 2. Exact statements (verbatim from the frozen files)

**K7-CASEA-K23 (R-c) rigid rows.**

```text
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
```

**K7-CASEA-K23 Lemma K3.**

```text
**Lemma K3 (transfer kill) [NEW].** If u in W has a rigid x-row forcing L_j subset L_a (a in W \ {u}, j != u), then in
C^x at apex a, D_j cap D_u = empty (Lemma TC), so by Lemma FG-V **x*_aj + x*_au <= 5**. In particular x*_aj = 4 and
x*_au >= 2 is impossible.
```

**K7-CASEA-K23 Lemma K2.**

```text
**Lemma K2 [NEW].** There is no pair (a, s) with a single-x-four and s single-x*-four whose x*-four is a.
```

**K7-CASEA-K23 Lemma CL.**

```text
**Lemma CL.** If F contains neither K_{1,4} nor K_{2,3} (equivalently Gamma^alpha, the complement of F in W, is
connected), Corollary L in C^alpha gives |P*| >= 2. Dually, if F* contains neither, |P| >= 2.
```

**K7-CASEA-K23 Lemma S.**

```text
**Lemma S.** (i) If n31 >= 1 then n12 = n13 = 0; dually, n13 >= 1 implies n21 = n31 = 0. (ii) Up to inversion
(alpha <-> alpha*) and apart from the all-(2,2) case, the type vector is one of: without 3-vertices,
(n12, n21, n22) in {(2,0,3), (2,2,1), (4,0,1)}; with 3-vertices, (n31, n21, n22) in {(2,0,3), (2,2,1), (4,0,1)}.
```

**K7-CASEA-K23 Theorem K7-CASEA-K23.**

```text
**In (a1) Case A, every configuration not of the all-(2,2) type (excluded by K7-TC-A22) has, up to inversion
(alpha <-> alpha*), F = K_{2,3} with two-side {v1, v2} and three-side {x, y, w}, F* = {xy, yw, wx, v1 v2}, N empty, and
moreover: E >= 2; alpha* has no W-entry 1; the alpha-rows of x, y, w are R2 = (2,2,4,4 | 4), so alpha_t = 4 on {x, y, w}
and alpha = 2 inside {x, y, w}; alpha_v1v2 = 2; alpha*_tv1 = alpha*_tv2 = 4 and alpha_tv1, alpha_tv2 lie in {1, 2}, not
both 1; t's alpha-row on W is 44412 or 44422.**
```

**K7-CASEA-K23 Proposition K7-CASEB-T.**

```text
**In Case B (Theorem CASEB and Theorem K7-TC-B), alpha_ta = 2 and alpha*_ta = 4 for every a in T*.**
```

**K7-CELL Lemma EQ (as amended by C.1).**

```text
Let a in W and suppose that at apex a of C the masses x*_aj/6 on (W cup {t}) \ {a} are 4/6 at two vertices g1, g2
(local indices 4 times an odd number) and 2/6 at the three others s1, s2, s3 (local indices 2 times an odd number), and
z has mass 3/6. Then **D_g1 = D_g2**, both equal to the union Q of the right U_a-cosets meeting g1 or g2, and
mu(Q) = 4/6.
```

**K7-CELL Lemma SUB.**

```text
At an apex a of C (g_a = 1) let D_j = D_k with mu(D_j) + mu(X_j) = 1 (so D_j = Y_j), and suppose x_jk = x_aj = 2. Then
**K := U_aU_j = U_jU_k is a subgroup of index 3 containing U_a, U_j, U_k**, and g_aK, g_jK, g_kK are pairwise distinct
except that g_aK = g_kK is possible when x_ak != 2.
```

**K7-CELL Lemma IN.**

```text
Let K have index 3 and contain U_j for a vertex j (apex j of C). For every vertex i whose coset meets g_jK,
**x_ji < 2 m^K_i**; in particular, if x_ji = 4 then m^K_i = 3.
```

**K7-CELL Lemma IN, lower bound.**

```text
**Lower bound.** If U_l subset K and mu(U_iU_l) = x_il/6 > 1/3, then m^K_i >= 2 (U_iU_l subset U_iK).
```

**K7-CELL Lemma CELL.**

```text
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
```

**K7-CELL Theorem K7-CELL-A.**

```text
**No (a1) configuration lies in the K_{2,3} family of Theorem K7-CASEA-K23 (nor in its inverse).**
```

**K7-CELL Theorem K7-CELL-B.**

```text
**No (a1) configuration lies in Case B (T = W != T*), nor in its mirror (T* = W != T).**
```

**K7-CELL section 7 chain (CONDITIONAL, not a claim).**

```text
- **Chain (stated only as a conditional chain, not as a closure claim).** If RICH (accepted), A1-STRUCT, K7-TC, K7-TC-A22
  (through the overlay), K7-CASEA-K23 and this file are all correct, then in (a1): TZ (iii) gives T = W or T* = W;
  T = T* = W is Case A, which K7-TC-A22, K7-CASEA-K23 and Theorem K7-CELL-A leave empty; T = W != T* is Case B and its
  mirror, empty by Theorem K7-CELL-B. Each link is pending review; no exclusion of (a1) is asserted here.
```

Lemma EQ is read with erratum C.1 (odd parts of the local indices pairwise coprime).

## 3. Imports with sha256 and status

| import | file / record | sha256 | status |
|---|---|---|---|
| RICH (FG7 chain form, Cor 5/6 + equality clause, NO5, R3, TR, CC, TZ, LZ, Theorem) | `K7-D23-RICH-v1.md` + `K7-D23-RICH-erratum-v1.md` + `K7-D23RICH-D23P-erratum-v1.md` | ba32d282...f2bb3; 8261831b...0ba69; 55cb66ca...4d428 | ACCEPTED (verdict 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0) |
| LFC (a)-(d), INV (a)-(b), E1/E2/E6/E7/E8, R0 (item 6) | `K7-LFC-INV-v1.md` + erratum | 45be9162...726c; 7af9acf0...75bd5 | ACCEPTED (verdict 8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18) |
| L0.1, L0.2, L0.3, L1, VFC (V1)-(V4) | `six-lane-20261016/sun-coset7/rules-k7-v1.md` | 77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee | ACCEPTED (written verdict 73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35); inverted configuration via Z2 erratum G5 (3aa30555...56f9, verdict 0f6b9aa3...b19c) |
| D23-MIX | `K7-D23-NO4-v1.md` + erratum | a3b47626...189d; 594c28aa...ba69 | ACCEPTED (verdict d3453de10eafab4d4666eb1902e18a13140beb4aee511df3c35febf21e4f37db) |
| A1-STRUCT (section 0 triangle rule and two/four classes, Cor W3, E3, PFG-t + Cor L, Lemma B, CASEB) | `K7-A1-STRUCT-v1.md` | c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf | dual-reviewed 0/0/MINOR; overlay repair review RUNNING; NOT accepted |
| K7-TC (Lemma TC, R1 for every E >= 1, R3, Lemma FG-V, TC-B) | `K7-TC-v1.md` | cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117 | as above; R1 (E = 1) and FG-V are materially new overlay items |
| K7-TC-A22 (all-(2,2) Case A excluded) | `K7-TC-A22-v1.md` | 9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41 | as above; uses R1 at E = 1 |
| combined overlay | `K7-A1-A2-delta-erratum-v1.md` | 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e | repair review RUNNING |
| Sun(2) (E2), Sun(3) (Zhu) | direct | - | classical / accepted |
| Sun(5), Sun(6) | records 2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301, efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29 | - | transitive only (computer-assisted); not instantiated in the two files under review |

## 4. Scope

- **(a1) only.** Both files are stated in setting (a1) (2-marker z != 3-marker t; 5-marker absent, on z or on t).
- **(a2): nothing is claimed in the files under review.** A separate named-claim transfer audit,
  `K7-CASEA-CELL-A2-TRANSFER-v1.md` (sha256 84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6, written
  07:43:44), is frozen but is NOT part of this package; it depends additionally on the A2 bridge decisions. (a2-zt5) is
  not covered anywhere.
- **Section 7 of K7-CELL is a conditional chain, not a claim**: it lists that RICH TZ (iii), CASEB, K7-TC-A22,
  K7-CASEA-K23 and Theorems K7-CELL-A/B together would leave no (a1) configuration; every link except RICH is pending.

## 5. Every step using Sun(2)/Sun(3) or integrality / index / coset arguments
**K7-CASEA-K23**
- (R-a): value >= 6 of (1,1,4,4) - Sun(2) (ones isolated); exclusions of single-four multisets by Lemma B (imported).
- (R-c): feasibility of the displayed vectors - Sun(3) excludes {f,s,s'}, {t,s,s'}, {z,s,s'} (R3') and {s,s',f} (R1-);
  Sun(2) isolates ones and t's label 3^A w_t outside {t, z}; rigidity then by the RF2 equality clause (coset count).
- Excluded rows (1,2,4,4 | 1), (1,4,4,4 | 1): Sun(2) (o and t isolated), heredity.
- Lemma K3: coset algebra only (Lemma TC) + FG-V (G0, FG7 (b), V1) - no Sun.
- Lemma K2: R3/R3' rigidity (above); x_as = 2 by the twin rule (L1 triangle rule) - no further Sun.
- Lemma CL / section 4 t-row: imported Corollary L, used only for "|P|, |P*| >= 2" and for excluding 44411 (b = 3,
  k1 = 2 kill: Sun(2), Sun(3)); its Sun(5) branches (44441, 44444) are not used.
- (S-a)-(S-f): K2, K3, CL, INV and degree counting - no new Sun.
- Section 4, alpha_v1v2 = 1 branch: {y, v1, v2} with local indices 4w, 2w, 2w excluded by Sun(3) (VFC (V3)).
**K7-CELL**
- Lemma EQ: Sun(3) via VFC (V3) (three twos; a four with two twos); then FG-V.
- Lemma SUB: L0.2 (disjointness <=> g^-1 g' not in UU'), L0.3 (measures), right-invariance - no Sun.
- Lemma IN: LFC (a)-(c) at the apex (the single weight y_i = 1 is feasible without any Sun instance); homogeneity of
  fibres across K-cosets (coset algebra); index count n_j/3 - no Sun.
- Lemma CELL (i)-(ii): index identities |LK| = |L||K|/|L cap K| and [U_z : U_z cap K], [U_z cap K : U_z cap K cap L] <= 3
  (integrality); (iii): **direct Sun(3) inside the subgroup K cap L** (three pairwise disjoint cosets, all index gcds <= 2).
- Theorem K7-CELL-A: LFC (d) at t in C^alpha* (Sun(2) isolates the 3-side ones); Sun(3) inside K cap L for the pieces
  (v1, t, u) [t has its own K-coset] and (v, u, z) [z avoids the cells of v1, v2]; final measure contradiction by L0.3.
- Theorem K7-CELL-B: LFC (d) at t in C^alpha* (corrected by erratum C.4; Sun(2)); Sun(3) inside H cap K' for (v, t, a),
  (v, a, z), (a, t, z); integrality of N_z = n_z m^H_z / 9 forces m^H_z = 3 (index arithmetic, no Sun).

## 6. Suggested reviewer focus
Lemma EQ (the s-mass count and FG-V); Lemma SUB (right-invariance, measure equalities); Lemma IN (homogeneity of fibres
across K-cosets); Lemma CELL (cell bijection; prime factors of N_z); the placement of t and z in Theorems K7-CELL-A/B,
including the integrality step m^H_z = 3; the structure enumeration (S-a)-(S-f) and the alpha_v1v2 = 1 branch of
K7-CASEA-K23; the use of R1 at E = 1 and of FG-V only through the overlay.
