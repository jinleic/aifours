# Review package A2-ZT5 v2: complete receipts and active overlays

Written: 2026-10-19T08:07:24-0700 (`/bin/date` immediately before the exclusive create). Owner: Sun7K62Successor.

**CONDITIONAL; no family closure claim.** This is a review manifest, not an acceptance or a new theorem. It supersedes
manifest `D/review-package-A2-ZT5-v1.md` `75146e9faf7db2be4b337a5b8ec75e01a43f0a61c09facefe7cd274a47280157` for routing purposes. It preserves all frozen source bytes and includes the self-found gap,
its reinstatement proof and the additional t-row prerequisite repair. R3 is declared conditional on the R2 statements.

## 1. Files under review and overlay precedence

- `D` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue`.
- `B` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7`.
- `O` = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7`.
- `R` = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review`.
- `R16` = `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review`.


| key | frozen file | full SHA256 |
|---|---|---|
| TX | `D/K7-CASEA-CELL-A2-TRANSFER-v1.md` | `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6` |
| ZA | `D/K7-A2-ZT5-A-v1.md` | `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919` |
| ZB | `D/K7-A2-ZT5-B-v1.md` | `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8` |
| ZE1 | `D/K7-A2-ZT5-erratum-v1.md` | `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4` |
| ZE2 | `D/K7-A2-ZT5-erratum-v2.md` | `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47` |
| ZE3 | `D/K7-A2-ZT5-erratum-v3.md` | `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667` |

Read ZA and ZB with ZE1, ZE2 and ZE3 in this order. Active changes:
- ZE1 ZB.1 adds the missing e*=3 kill in ZB Step 2(ii); ZB.2 changes the Step 2(iii) bound to e*<=3. Both remain active.
- ZE1 ZA.1/ZA.2 withdrew Theorem ZT5-A for the missing alpha*-side prerequisites. ZE2 closes that gap by new Lemma ZW
  and reinstates the statement **only as a conditional candidate**. ZE3 supplies new Lemma ZT before the Cor L invocation
  in ZW(ii) and ZB Step 1; neither ZW nor ZT is an accepted premise.
- The broad FG-zf consequences paragraph is read with ZE3 item 3: no full Cor L may be imported before its entry-type
  prerequisites. The needed alpha-side connected-graph t-row assertion is Lemma ZT.
- ZE1 MAP.1 and PKG.1 (the withdrawn edge / restricted manifest scope) are superseded by ZE2/ZE3 and this manifest.
  ZE1 MAP.2 (wording nit only) stays active. Earlier maps/manifests are navigation, not additional mathematical premises.

## 2. Exact family definition, normalization and |T*| split

**K7:** seven pairwise disjoint cosets with n_i=6r_i, gcd(r_i,r_j)=1 for i!=j, r_i=m_i w_i where m_i is the {2,3,5}-part
and gcd(w_i,30)=1. **(a2):** distinct vertices z,t,p with r_z=2^E w_z, r_t=3^A w_t, r_p=5^B w_p, E,A,B>=1 arbitrary actual
exponents, W'=V\{z,t,p} the four unmarked vertices. Put W=W' union {p}.

**(a2-zt5):** at least one orientation x in {alpha,alpha*} has x_zt=5. Lemma F, pending R1, says no other pair can carry
5; alpha_zt+alpha*_zt<=6 makes the orientation unique. INV/E6 allows us to call it alpha. Then the data S1-S5 of A2 are:
alpha_zW=3, alpha_zt=5, alpha*_zt=1; alpha* has a 3-type z-row with at least three entries 3 on W; alpha_tu in {2,4}
for u in W', alpha_tp in {1,2,4}; no other entry 5; E>=2. In particular T=W.

**(a2-no5):** no entry of either orientation equals 5. Lemma F gives the exhaustive, disjoint (a2-no5)/(a2-zt5) split
conditional on R1. These two index-and-pair conditions are inversion-stable. Normalizing the five exchanges orientations,
not the labelled marker vertices. Put T*={u in W:alpha*_zu=3}. Lemma ZS gives exactly T*=W or |T*|=3; in the latter branch
O*=W\T*={v1,v2}, alpha_v1v2=4, alpha_tv=4, alpha_va=2 (a in T*), and the v alpha-rows are (2,2,2,4|4).

## 3. Statements verbatim from frozen sources

### Corollary K7-CC-A2

Source `D/K7-CASEA-CELL-A2-TRANSFER-v1.md` `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`.

```text
**Corollary K7-CC-A2 (conditional).** In (a2-no5), with W := W' cup {p}, T, T* as in Theorem K7-A2-BRIDGE, the following
named claims hold, with RICH replaced by Theorem K7-A2-BRIDGE and A1-STRUCT/K7-TC/K7-TC-A22 replaced by their
transferred versions (Corollary K7-A2-TRANSFER): from K7-CASEA-K23 - the rigid-row list (R), Lemmas K3, K2, CL, S, the
exclusions (S-a)-(S-f), Theorem K7-CASEA-K23 and Proposition K7-CASEB-T; from K7-CELL - Lemmas EQ, SUB, IN, CELL and
Theorems K7-CELL-A, K7-CELL-B. Not transferred: navigation remarks and the conditional chain of K7-CELL section 7 as a
claim.
```

### Setting of FG-zf / ZS / ZT5-A (normalized (a2-zt5))

Source `D/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

```text
(a2-zt5) with the five in orientation alpha (the other orientation is symmetric by inversion): alpha_zt = 5,
alpha_zu = 3 for u in W := W' cup {p}, alpha*_zt = 1, alpha*_zu in {1,2,3}, T* := {u in W : alpha*_zu = 3}, |T*| >= 3,
alpha_tu in {2,4} (u in W'), alpha_tp in {1,2,4}, no other entry 5, E >= 2 (Proposition K7-A2-ZT5).
```

### Lemma FG-zf (a)-(b)

Source `D/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

```text
For u in W, x in {alpha, alpha*}:
- (a) every feasible y at u (orientation x) with y_z = 0, resp. y_t = 0, has val(y) <= 5; if val(y) = 5, every fibre C
  with S_C not contained in {z}, resp. {t}, has weight exactly 1;
- (b) at an apex a in W of C^alpha and of C^alpha*, the union of the D_j over j not in {a, z}, resp. not in {a, t}, has
  measure <= 5/6.
```

### Lemma ZS

Source `D/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

```text
**Either T* = W, or |T*| = 3 and W \ T* = {v1, v2} with alpha_v1v2 = 4, alpha_tv = 4 and alpha_va = 2 for every
a in T*, the alpha-rows of v1, v2 being (2,2,2,4 | 4).**
```

### Theorem K7-ZT5-A (reinstated as conditional, not accepted)

Source `D/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

```text
**In (a2-zt5) there is no configuration with T* = W.**
```

### Theorem K7-ZT5-B

Source `D/K7-A2-ZT5-B-v1.md` `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`.

```text
**Theorem K7-ZT5-B (conditional).** In (a2-zt5) (the five in orientation alpha) there is no configuration with
|T*| = 3.
```

### Lemma ZW (read with ZE3 changing its t-row invocation)

Source `D/K7-A2-ZT5-erratum-v2.md` `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`.

```text
In (a2-zt5) with T* = W (notation of K7-A2-ZT5-A): **(i)** an alpha*-row at u in W with a W-entry 3 has W-part (3,3,1,1),
(3,3,2,2), (3,3,3,1), (3,3,3,2) or (3,3,3,3) (in particular no W-entry 4), and for (3,3,1,1), (3,3,2,2) also
alpha*_ut <= 3; **(ii)** alpha* has no W-entry 3; **(iii)** alpha*_ut != 3 for u in W. Hence every W-W and W-t entry of
alpha* lies in {1,2,4}.
```

### Lemma ZT

Source `D/K7-A2-ZT5-erratum-v3.md` `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.

```text
In (a2-zt5), normalized alpha_zt = 5 and alpha*_zt = 1, if Gamma^alpha = {uv in W : alpha_uv <= 2} is connected, then
alpha*_tu is in {1,2,4} for all u in W and **at least two of these five entries equal 4**.
```

## 4. Import catalog, exact status and covering review

**R1**: parent-owned A1/A2 repair review, covering A1/TC/A22/A2 with overlay OV; verdict pending.
**R2**: parent-owned CASEA/CELL review, package `D/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`; statements are conditional premises of R3, not accepted
by this manifest. **R3**: parent-owned A2-side review requested with this manifest; no reviewer verdict exists here.
Accepted statements are marked **ACCEPTED-SCOPED** and their frozen parent record is identified separately.

| key | import / exact use | frozen file | full SHA256 | status / review |
|---|---|---|---|---|
| BASE | Class K7 definition; R0 finite quotient | `O/README.md` | `2a6d6d6e1dadbad522c8c8f9322c17eae719fb01fe373e6b1caf8c40cadc3fd1` | ACCEPTED-SCOPED through VWRITE; index notation also INV |
| RULES | L0.1-L0.3, L1, VFC V1-V4 | `O/rules-k7-v1.md` | `77b9afec448ab44605b9ee513778bffd3e40aa9157807e8402f5488330e73cee` | ACCEPTED-SCOPED through VWRITE |
| INV | LFC (a)-(d), INV (a)-(b) | `B/K7-LFC-INV-v1.md` | `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c` | ACCEPTED-SCOPED with INVE through VINV |
| INVE | E1, E2, E6-E8; preliminary alpha bounds | `B/K7-LFC-INV-erratum-v1.md` | `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5` | ACCEPTED-SCOPED through VINV |
| Z2E | G5: L1 also applied to inverse | `B/K7-Z2-erratum-v1.md` | `3aa305553cd44946de32cea5cb2703b1864489a6a12de2154feda4884ee456f9` | ACCEPTED-SCOPED through VZ2 |
| NO4 | D23-MIX (a1) z-row data | `D/K7-D23-NO4-v1.md` | `a3b47626687141dac49daf30aab302c1ea66f15a74f28ee638b2212258de189d` | ACCEPTED-SCOPED with NO4E through VNO4 |
| NO4E | Mandatory D23-MIX overlay | `D/K7-D23-NO4-erratum-v1.md` | `594c28aab89a269b32f79385552fd226eb22c41e8be538cc5bebf895acc54d6a` | ACCEPTED-SCOPED through VNO4 |
| RICH | G0, chain-form FG7, 5/6 equality, NO5/R3/TR/CC/TZ/LZ | `D/K7-D23-RICH-v1.md` | `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3` | ACCEPTED-SCOPED with RICHE/RICHE2 through VRICH |
| RICHE | Mandatory RICH erratum 1 | `D/K7-D23-RICH-erratum-v1.md` | `8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69` | ACCEPTED-SCOPED through VRICH |
| RICHE2 | Mandatory RICH/D23P consolidated erratum | `D/K7-D23RICH-D23P-erratum-v1.md` | `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428` | ACCEPTED-SCOPED through VRICH |
| D23P | (a2) both z-rows of type (b-prime) | `D/K7-D23P-v1.md` | `89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880` | ACCEPTED-SCOPED with RICHE2 through VRICH |
| A1 | Section 0 triangle/two-four rules; Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB | `D/K7-A1-STRUCT-v1.md` | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` | PENDING R1, with OV; not its section 6 obstruction record |
| TC | TC, R1 (every E>=1), R3, FG-V, TC-B | `D/K7-TC-v1.md` | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` | PENDING R1, with OV; E=1 extension and FG-V material |
| A22 | All-(2,2) Case A excluded | `D/K7-TC-A22-v1.md` | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` | PENDING R1, with OV |
| A2 | Lemma F, FG-a2, 5/6-a2, D23-a2, ZT5 structure; enumerated BRIDGE/TRANSFER | `D/K7-A2-FIVE-v1.md` | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` | PENDING R1, with OV; not a blanket beta<=5 FG extension |
| OV | Mandatory combined A1/A2 overlay | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` | PENDING R1 |
| K23 | Rigid-row list, K3/K2/CL/S, exclusions S-a..S-f, CASEA-K23/CASEB-T | `D/K7-CASEA-K23-v1.md` | `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3` | PENDING R2; premises declared conditional |
| CELL | EQ/SUB/IN/CELL; CELL-A/B | `D/K7-CELL-v1.md` | `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae` | PENDING R2, with CELLE; premises declared conditional |
| CELLE | Mandatory self-erratum C.1-C.4 | `D/K7-CELL-erratum-v1.md` | `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132` | PENDING R2 |
| VSUN5 | Accepted Sun(5) receipt | `R16/sun-coset5-parent-verdict-v1.md` | `2cf0243687714e42d128b7cfd65c19ce538d7a73a603b1e027a5ae04d7065301` | ACCEPTED, computer-assisted; transitive import and transferred Cor L |
| VSUN6 | Accepted Sun(6) receipt | `R16/sun-coset6-parent-gate-verdict-v1.md` | `efe1d849a082404d778bb2bde6984b62915822f8a381ec7c9019948b0a241e29` | ACCEPTED, computer-assisted; transitive import only |

Accepted parent record pins:

- VWRITE: `R16/sun-coset7-written-parent-verdict-v1.md` `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35`.
- VINV: `R/sun7-lfc-inv-parent-verdict-v1.md` `8621e74422f837c09842e304523cd06b331bdb0b6680e4e56ade66da86bcca18`.
- VZ2: `R/sun7-Z2-parent-verdict-v1.md` `0f6b9aa3e0552b0140bf581ac5a4d425b0732bcba639bdc49b61518d5fe5b19c`.
- VNO4: `R/sun7-D23-parent-verdict-v1.md` `d3453de10eafab4d4666eb1902e18a13140beb4aee511df3c35febf21e4f37db`.
- VRICH: `R/sun7-K7-D23RICH-D23P-parent-verdict-v1.md` `1167bc4fa09ea74f298d9f19b667ca4412746cc1956cf57ed73ccee23289aec0`.

Sun(2) and Zhu's Sun(3)/Sun(4) are the classical direct imports already bound by those records. Their use here is
inside at-most-six-piece LFC/VFC fibres, or for the explicitly stated three pieces in K cap L. No Sun(7) instance,
least-order premise or computational output is used. The accepted Sun(5)/Sun(6) receipts remain computer-assisted;
there is no claim that the entire transitive import closure is computation-free.

## 5. Scope

R3 covers Cor K7-CC-A2 on (a2-no5); FG-zf and ZS on normalized (a2-zt5); new ZT on normalized (a2-zt5) with connected
Gamma^alpha; new ZW and Theorem ZT5-A on T*=W; Theorem ZT5-B on |T*|=3. The inverse-normalized branch is obtained only
by INV/E6 (same labelled indices and markers). All results remain conditional on their pending imports. No scope outside
the distinct-2/3-marker K7 family is asserted, and neither that family nor full Sun(7) is claimed closed.

## 6. All Sun(2)/Sun(3), integrality and index steps (including new repairs)

### TX (named-claim transfer only)
The audit checks p's replacement factor 5^B w_p: it is coprime to every other label's 5-part because there is no entry
5 and z,t carry none. All label/local-index gcds and L1 ell-divisors used by K23/CELL remain the same. FG-V transfers
via G0 and actual-configuration FG-a2, including apex p. SUB/IN/CELL use n_p/3=2*5^B w_p; N_z=n_z m_z^H/9 and its
integrality are unchanged. The K23/CELL Sun(2)/Sun(3) instances transfer; the whole transferred Cor L additionally has
Sun(5) in its 44441/44444 equality kills, as already recorded by R1. This is not an unproved abstract beta<=5 extension.

### ZA: FG-zf, ZS and ZT5-A
- FG-zf: integral intersection-index chains omit z or t. The first marked pair has alpha<=4 (t,p) or alpha=3 (z,p);
  all later factors are <=4, with the omitted apex skipped. If the apex is p no factor 5 enters; otherwise the only
  5-part is that of n_p. The prime-to-30 parts are products of the w's present. Thus gcd(n_u,T_N')=6, including u=p.
  G0 gives a positive 1/6 avoiding block. If value=5, every occupied fibre not supported solely on the omitted vertex
  has weight 1. The VFC union bound uses the actual subgroups, G0 and V1. No new Sun instance in this index step.
- ZS: L1 gives the z,u,v triangle implication. Alpha-side no-W-three uses RICH R3/TR/CC with full FG (beta=alpha*,
  alpha*_zt=1) and the 3,a,b triangle from A1. These inherited fibre kills use Sun(2)-Sun(4); CC uses V3 at z. Lemma B
  uses Sun(2) for coprime labels and Sun(3) for three two-gcd pieces; the (4,a,b) triangle gives a=b=2.
- ZW is inserted before ZT5-A's CASEA/CELL audit, with ZT inserted before ZW(ii)'s t-row use. Its new steps are below.
- ZT5-A's remaining audit uses only z-free or t-free versions of FG-zf. K3/K2 are subgroup/coset implications; the
  alpha_v1v2=1 branch counts D_z and D_v1,D_v2 in the t-free union and excludes {y,v1,v2} by Sun(3). EQ excludes triples
  via V3 (Sun(3)); SUB uses L0.2/L0.3; IN uses LFC (a)-(c), homogeneity and integral indices n_j/3. CELL has nine cells
  by [G:K cap L]=9 and applies Sun(3) inside K cap L. The t-apex LFC(d) step isolates ones by Sun(2). The final measure
  comparison is mu(U_zU_v1)=alpha_zv1/6=1/2. The full transferred audit remains under R3, conditional on R2.

### ZE2: new ZW (with ZE3)
- Part (i): z-free weights split the coprime W-three and one/two/four classes (Sun(2)); E8 standard weights use
  hereditary fibre constraints. The k3=2 remainder values are 2,3,5,2,3,4 for 11,12,14,22,24,44. The value
  4+alpha*_ut/3 vector for remainders 11 or 22 uses Sun(2) to separate unlike classes and Sun(3) to forbid two twos
  together with t. The labels of p include 5^B but introduce no new gcd because no other label here has a factor 5.
- Part (ii): L1 gives the (3,4,4) alternative; no W-four beside a W-three propagates the dominating-edge property.
  Lemma B for alpha rules out Theta*-degree 4 (its Sun(2)/Sun(3) row kills). The complement is a union of cliques, each
  of size >=2, hence K3+K2. A second Lemma B use and the (4,a,b) triangle give alpha=2 on K3,2, making Gamma^alpha
  connected. **ZT**, not an unqualified Cor L, now gives two alpha*_ta=4; part (i) bounds those same entries by 3.
- Part (iii): t's three-label is coprime to the W labels (Sun(2)); z-free standard weights on W plus y_t=1 give value
  >=7 against FG-zf. No exhaustive enumeration is used: the k3 cases and five-vertex complement argument are written.

### ZE3: new ZT
The spanning-tree intersection index is 6 product(r_u) times a power of 2; integral factors are <=2, and p contributes
only its own 5^B. Hence gcd(n_t,T_W)=6, giving PFG-t(i). At value 5 equality pins the union measure and requires a
weight-1 W-set meeting D_z. Sun(2) separates W-three labels from other W-types; Sun(4) bounds three-label sets by
three. k3=1,2 violate value<=5. k3=3,4,5 yield only stated value-5 survivors, whose weight-1 sets cannot coexist with
z: coprime pair Sun(2), or z with two twos Sun(3). After removing threes, one-four rows violate the value bound, and
zero-four equality rows are excluded by the same Sun(2)/Sun(3) tests. No computation or extra Sun(5) step is involved.

### ZB (with ZE1 repairs and ZT before Step 1)
1. Gamma^alpha contains all T* x O* pairs. ZT (above) supplies two alpha*_ta=4. Lemma B uses Sun(2)/Sun(3) as above.
2. Coprime local labels 4r_v1 and 3r_v2 give the value-7 Sun(2) kill. In case (ii), the missing e*=3 case is excluded
   by t's coprimality to W (ZE1 ZB.1); R1/R1-/R5 rigidity then gives K3's subgroup contradiction. The 1144 row is a
   Sun(2) isolated-ones kill. Case (iii) uses a Sun(2) 3312 kill and Sun(3) for {s,s',t}; value=4+e*/3 gives e*<=3,
   not 2 (ZE1 ZB.2); that suffices to exclude e*=4.
3. Coprime labels 3r_a3 and 4r_a1,4r_a2 give the value-7 Sun(2) kill, with both z and t of weight zero.
4. The one and t's label (when e*=1) are isolated by Sun(2). R4 vectors vanish on z,t, so the t-free equality clause
   supplies the z-containment. TC-B(i)'s VFC count uses Sun(3) for {v1,v2,x} and full FG-V in C^alpha*; the union
   lower bound is 11/12>5/6.
5. At t in C^alpha*, LFC(d) isolates ones by Sun(2), so alpha*_tv1 and alpha*_tv2 are not both 1.
6. EQ uses Sun(3). SUB uses L0.2/L0.3 and integral subgroup index 3. IN uses LFC(a)-(c), homogeneity, n_j/3. The two
   index-3 subgroups H,K' have [G:H cap K']=9. Sun(3) inside H cap K' gives t its own K'-coset and keeps z out of the
   v1/v2 K'-rows. With U*_z subset K', N_z=n_z m_z^H/9 is an integer; n_z has 3-valuation 1 and m_z^H in {1,2,3},
   hence m_z^H=3 and N_z=2^(E+1)w_z. The final three cell-piece indices have pairwise gcd 2 and contradict Sun(3).

## 7. Reviewer focus

The new ZT t-row classification before using Cor L is load-bearing for both branches. Check its PFG equality argument,
all k3 cases, and the fifth-prime factor at p. In ZW check the complement-of-Theta* clique argument, degree-4 exclusion,
and the timing of ZT (after Gamma^alpha is proved connected). Check FG-zf at apex p and with an omitted z/t: light
fibres consisting only of the omitted vertex are permitted and cannot yield extra containments. Then check the full
CASEA/CELL transfer audit, the t-free containment in ZB Step 4, and the integrality/cell coverage in Step 6. Do not treat
any R1/R2/R3 candidate as accepted. Full Sun(7), novelty and Lean/human verification are outside this review.
