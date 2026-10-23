# Review package: A2 side - K7-CASEA-CELL-A2-TRANSFER + K7-A2-ZT5-A + K7-A2-ZT5-B (conditional on the CASEA/CELL package)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T07:56:00-0700.
- **Owner:** Sun7K62Successor. Manifest only (no new mathematics, no computation). Declared conditional on the statements
  of review package `review-package-CASEA-CELL-v1.md` (sha256 e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583).

## 1. Files under review (frozen, byte-identical)

| file | sha256 | written |
|---|---|---|
| `K7-CASEA-CELL-A2-TRANSFER-v1.md` | 84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6 | 2026-10-19T07:43:44-0700 |
| `K7-A2-ZT5-A-v1.md` | 4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919 | 2026-10-19T07:51:01-0700 |
| `K7-A2-ZT5-B-v1.md` | f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8 | 2026-10-19T07:53:56-0700 |

Directory: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/`.

## 2. Exact (a2-zt5) definition and the |T*| split

- **(a2)** (A2-FIVE section 0): class K7 with three distinct marked vertices, r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p
  (E, A, B >= 1), W' := V \ {z, t, p} unmarked.
- **(a2-zt5)** (A2-FIVE section 4): some orientation x has x_zt = 5; by Lemma F this is the only possible entry 5, and
  x*_zt = 1, so the orientation is unique; by inversion (E6) it is called alpha. Then (Proposition K7-A2-ZT5) the alpha-row
  at z is (3,3,3,3 | p 3 | t 5), so T = W := W' cup {p}; the alpha*-row at z is 3-type relative to W; alpha_tu in {2,4} on
  W', alpha_tp in {1,2,4}; E >= 2.
- **(a2-no5)**: no entry 5 in alpha or alpha*. (a2-zt5) and (a2-no5) partition (a2) (Lemma F; inversion-stable).
- **|T*| split** (Lemma ZS): T* := {u in W : alpha*_zu = 3}; either T* = W (Theorem K7-ZT5-A) or |T*| = 3 with
  W \ T* = {v1, v2} (Theorem K7-ZT5-B).

## 3. Exact statements (verbatim; statement paragraphs as frozen, proofs included where the frozen paragraph includes them)

**TRANSFER Corollary K7-CC-A2.**

```text
**Corollary K7-CC-A2 (conditional).** In (a2-no5), with W := W' cup {p}, T, T* as in Theorem K7-A2-BRIDGE, the following
named claims hold, with RICH replaced by Theorem K7-A2-BRIDGE and A1-STRUCT/K7-TC/K7-TC-A22 replaced by their
transferred versions (Corollary K7-A2-TRANSFER): from K7-CASEA-K23 - the rigid-row list (R), Lemmas K3, K2, CL, S, the
exclusions (S-a)-(S-f), Theorem K7-CASEA-K23 and Proposition K7-CASEB-T; from K7-CELL - Lemmas EQ, SUB, IN, CELL and
Theorems K7-CELL-A, K7-CELL-B. Not transferred: navigation remarks and the conditional chain of K7-CELL section 7 as a
claim.
```

**ZT5-A section 0 setting ((a2-zt5) definition).**

```text
(a2-zt5) with the five in orientation alpha (the other orientation is symmetric by inversion): alpha_zt = 5,
alpha_zu = 3 for u in W := W' cup {p}, alpha*_zt = 1, alpha*_zu in {1,2,3}, T* := {u in W : alpha*_zu = 3}, |T*| >= 3,
alpha_tu in {2,4} (u in W'), alpha_tp in {1,2,4}, no other entry 5, E >= 2 (Proposition K7-A2-ZT5).
```

**ZT5-A Lemma FG-zf.**

```text
For u in W, x in {alpha, alpha*}:
- (a) every feasible y at u (orientation x) with y_z = 0, resp. y_t = 0, has val(y) <= 5; if val(y) = 5, every fibre C
  with S_C not contained in {z}, resp. {t}, has weight exactly 1;
- (b) at an apex a in W of C^alpha and of C^alpha*, the union of the D_j over j not in {a, z}, resp. not in {a, t}, has
  measure <= 5/6.
*Proof.* For x = alpha (and for C^alpha*) this is Corollary 5/6-a2 / FG-a2 with beta = alpha* (alpha*_zt = 1). For
x = alpha* (and for C^alpha), let N' := V \ {u, z}, resp. V \ {u, t}, and W' := the intersection of the conjugates (or
of the U_j) over N', pair parameters beta = alpha. Order N' as t, p, then W' (resp. z, p, then W'), omitting u: the base
factor is alpha_tp <= 4 (resp. alpha_zp = 3), and every later step factor is <= beta to an earlier vertex <= 4 (all
entries other than z-t are <= 4); so no prime >= 5 enters any factor, the prime-to-30 part of [G : W'] is the product of
the w_j (j in N'), and 5 divides [G : W'] only through n_p (p in N'). Hence gcd(n_u, [G : W']) = 6 for u in W' and for
u = p. The rest is the proof of RICH Corollary 5/6 (resp. Lemma FG-V) with W' in place of W*: the fibres (resp. cosets)
in W'U_u avoid every L_j (resp. D_j) with j in N' and may meet only z (resp. t), which carries weight 0. QED
**Consequences.** Rigid rows whose weight vectors vanish on z keep their containments L_i subset L_j for i != z (and, if
the vectors also vanish on t, the containments with i = z via the t-free version). Lemma K3, K2, EQ hold with unions
taken without z; Lemmas SUB, IN, CELL are unaffected; Lemma B holds in both orientations at rows with c = 3 (each of its
kills vanishes on z or on t); PFG-t and the "at least two entries 4" part of Corollary L hold in both orientations.
```

**ZT5-A Lemma ZS (the |T*| split).**

```text
**Either T* = W, or |T*| = 3 and W \ T* = {v1, v2} with alpha_v1v2 = 4, alpha_tv = 4 and alpha_va = 2 for every
a in T*, the alpha-rows of v1, v2 being (2,2,2,4 | 4).**
*Proof.* For u in T*, v in O* := W \ T*, the triangle {z, u, v} (alpha*_zu = 3, alpha*_zv in {1,2}) forces
alpha*_uv in {3,4} (RICH TZ (i) argument; no five), hence alpha_uv <= 3, and alpha_uv in {1,2} (alpha has no W-three by
the W3 argument: RICH R3 for alpha-rows with FG, TR and CC at z in C^alpha with alpha*_zt = 1, and the triangle step of
A1-STRUCT Corollary W3). A vertex v in O* has >= 3 alpha-entries <= 2, so Lemma B gives a single alpha-four inside O* and
alpha_tv = 4; hence |O*| != 1, and |O*| <= 2 as |T*| >= 3. The triangle (4, alpha_v1a, alpha_v2a) passes only as
(4, 2, 2). QED
```

**ZT5-A Theorem K7-ZT5-A.**

```text
**In (a2-zt5) there is no configuration with T* = W.**
*Proof (dependency audit).* With T = T* = W both orientations have c = 3 at every W-vertex, so the setting is the
(a2-no5)-type Case A with p in W, except that granularity is available only in the z-free / t-free form of Lemma FG-zf.
The proofs of K7-CASEA-K23 and Theorem K7-CELL-A go through verbatim with these replacements:
- every rigid row of (R-c) is used only through containments not involving z on the left (all weight vectors vanish
  on z), except R4 at v_i in the alpha_v1v2 = 1 branch, whose vectors vanish on z and t, so L_z subset L_x holds by the
  t-free version;
- Lemma K3 (all its uses have j, u != z), K2, CL, S, (S-a)-(S-f) and the 3-side R2 step are unchanged;
- the alpha_v1v2 = 1 branch of section 4 uses the t-free union: D_z (3/6) and D_v1, D_v2 (2/6 each, disjoint from D_z)
  lie in the union over j != t, of measure <= 5/6, so D_v1 = D_v2 = R with mu(R) = 2/6, and y (4/6) meets R: the triple
  {y, v1, v2} violates Sun(3) as before;
- Lemma EQ in Theorem K7-CELL-A uses the union over j != z (the counted vertices are v_i', t, x, y, w, resp. y, w, v1, v2,
  t); SUB, IN, CELL, the LFC (d) step at t (weights vanish on z) and the final step mu(U_zU_v1) = alpha_zv1/6 = 1/2 are
  unchanged; labels of p and z carry no new common prime (z has no 5-part; only p carries 5^B).
QED
```

**ZT5-B Theorem K7-ZT5-B.**

```text
**Theorem K7-ZT5-B (conditional).** In (a2-zt5) (the five in orientation alpha) there is no configuration with
|T*| = 3.
```

## 4. Imports with sha256, status and covering review

| import | file / record | sha256 | status / review |
|---|---|---|---|
| RICH (named claims), D23P | `K7-D23-RICH-v1.md` + erratum-1 + `K7-D23RICH-D23P-erratum-v1.md`; `K7-D23P-v1.md` | ba32d282...f2bb3; 8261831b...0ba69; 55cb66ca...4d428; 89739dc2...37880 | ACCEPTED (verdict 1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0) |
| LFC, INV, E1-E8, R0 | `K7-LFC-INV-v1.md` + erratum | 45be9162...726c; 7af9acf0...75bd5 | ACCEPTED (8621e744...ca18) |
| L0.1-L0.3, L1, VFC | `rules-k7-v1.md` | 77b9afec...cee | ACCEPTED (73a25ba6...3f9d); inverted configuration via Z2 G5 |
| Lemma F, FG-a2, Cor 5/6-a2, D23-a2, Prop K7-A2-ZT5, Thm K7-A2-BRIDGE, Cor K7-A2-TRANSFER | `K7-A2-FIVE-v1.md` | 93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc | A2 dual review returned (Codex 1 MAJOR scope repair, Claude 0/0/19); repair in overlay; verdict pending (review 1) |
| combined overlay (A1 + A2 repairs) | `K7-A1-A2-delta-erratum-v1.md` | 0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e | repair review RUNNING (review 1) |
| A1 package (A1-STRUCT, K7-TC incl. FG-V and R1 for E >= 1, K7-TC-A22) | `K7-A1-STRUCT-v1.md`, `K7-TC-v1.md`, `K7-TC-A22-v1.md` | c8a16f14...e3ccf; cc48340d...e117; 9ebec279...1b46b41 | NOT accepted; review 1 |
| CASEA-K23 (rows, K3, K2, CL, S, Thm, CASEB-T) | `K7-CASEA-K23-v1.md` | f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3 | review 2 (package e892c98b...) |
| CELL (EQ, SUB, IN, CELL, Thms A/B) + self-erratum | `K7-CELL-v1.md`, `K7-CELL-erratum-v1.md` | d421e08c...aae; 56829e8d...132 | review 2 |
| Sun(2) (E2), Sun(3) (Zhu) | direct | - | classical / accepted |
| Sun(5), Sun(6) | 2cf02436...5301, efe1d849...1e29 | - | transitive (computer-assisted); Sun(5) direct only inside the transferred Corollary L |

Reviews: (1) A1/A2 overlay repair verdict; (2) CASEA/CELL dual review (package e892c98b...); (3) this A2-side dual review.

## 5. Scope

- (a2) only: (a2-no5) through the named-claim transfer; (a2-zt5) through Theorems K7-ZT5-A and K7-ZT5-B.
- All three files are CONDITIONAL; nothing here is claimed if any import of section 4 fails. No closure claim; the
  family-level dependency map is `K7-family-closure-map-v1.md` (also conditional).
- Not covered: K6.2*, other K7 classes outside the 2-marker != 3-marker family, full Sun(7).

## 6. Every step using Sun(2)/Sun(3) or integrality / index arguments
**K7-CASEA-CELL-A2-TRANSFER** (audit only): every Sun use is that of its sources (CASEA-K23, CELL: Sun(2), Sun(3), the
latter also inside K cap L); Sun(5) only inside the transferred Corollary L. Index/gcd checks: p's piece index
2 5^B w_p; no other label or local index has a factor 5 in (a2-no5).
**K7-A2-ZT5-A**
- Lemma FG-zf: index chains omitting z (order t, p, W') or t (order z, p, W'); base factors alpha_tp <= 4, alpha_zp = 3;
  step factors <= 4; integrality of [G : W'] (no prime >= 5 enters a factor; 5 only through n_p); G0. No Sun.
- Lemma ZS: TZ (i) triangle (L1); the W3 argument (RICH R3 for alpha-rows with Sun(2)-Sun(4) as in RICH, TR, CC at z
  with Sun(2)-Sun(4) through VFC (V3)); Lemma B (Sun(2), Sun(3)); the triangle (4, a, b) (L1).
- Theorem K7-ZT5-A: the Sun uses of K7-CASEA-K23 and K7-CELL-A (Sun(2), Sun(3); Sun(3) inside K cap L), with z-free /
  t-free unions; the alpha_v1v2 = 1 branch: Sun(3) for {y, v1, v2} (VFC (V3)).
**K7-A2-ZT5-B**
- Step 1: PFG-t chain along a spanning tree of Gamma^alpha (index arithmetic) and Corollary L's b <= 1 kills (Sun(2),
  Sun(3)); Lemma B (Sun(2), Sun(3)).
- Step 2: (i) coprime labels 4w / 3w (Sun(2)); (ii) Lemma K3 (TC + FG-V; no Sun) and (1,1,4,4) (Sun(2)); (iii) {s, s', t}
  with all gcds 2 (Sun(3)); FG-zf.
- Step 3: coprime labels 3w / 4w (Sun(2)); FG-zf.
- Step 4: R4 rigidity (Sun(2) isolates o and t), t-free equality clause; the K7-TC-B (i) count (Sun(3) for {v1, v2, x});
  FG-V.
- Step 5: LFC (d) at t (Sun(2) isolates ones).
- Step 6: Lemma EQ (Sun(3)); SUB (L0.2, L0.3); IN (LFC, homogeneity, index n_j/3); CELL (index identities, Sun(3) inside
  H cap K'); integrality N_z = n_z m^H_z / 9 => m^H_z = 3 (index arithmetic).

## 7. Suggested reviewer focus

Lemma FG-zf (the omitted-vertex chains, especially u = p, and what the equality clause still gives when light fibres may
hold z or t); Lemma ZS (the W3 argument in (a2-zt5): R3 for alpha-rows uses full FG, CC at z uses alpha*_zt = 1); the
two explicit replacements in Theorem K7-ZT5-A (t-free union in the alpha_v1v2 = 1 branch; z-free unions in Lemma EQ);
Steps 2-4 of Theorem K7-ZT5-B (the 3/4 mixing kills, the exclusion of alpha*_(a3 v) = 3, the use of the t-free version
for L*_z subset L*_a in Step 4); Step 6 as in K7-CELL-B; the transfer table of K7-CASEA-CELL-A2-TRANSFER.
