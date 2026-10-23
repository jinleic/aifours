# K7 R2/R3 consolidated Codex-requested repair overlay v1

Written: 2026-10-19T08:59:07-0700 (`/bin/date` immediately before exclusive create). Owner: Sun7K62Successor.
This single final overlay preserves every original and prior erratum. No computation and no new theorem.

## Authority, review status and exact scope

- Accepted A1/A2 authority: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`, with OV v1 then OV2. Its acceptance does not extend to R2/R3.
- Codex R2: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R2-codex-v1.prompt.stdout.txt` `3e40ddf2ab2094822ad7520b4f6ff455e391b45e17159539ab2bc7b59d9eeacb` (ACCEPT-WITH-FIXES, 1 MAJOR, 2 MINOR).
- Codex R3a: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R3a-codex-v1.prompt.stdout.txt` `a9cd5ab4c95bdad537eb3c11febe2dcc4e3aae87f90ce497b1e822f6911470fa` (ACCEPT-WITH-FIXES, 0 MAJOR, 2 MINOR).
- Codex R3b: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/sun7-K7-R3b-codex-v1.prompt.stdout.txt` `9de994d4718eb725fc7c4e9c8695c587e07ae1bdf6ca4ba7f39e2e6454520020` (conditional ACCEPT-WITH-FIXES, 1 MAJOR and listed MINOR repairs).
- The parent reports the three Claude R2/R3a/R3b attempts terminated NO_VERDICT rc1 from provider capacity, not
  mathematical verdicts, and authorized this freeze without further findings. Fresh whole-slice Claude review and
  scoped Codex repair review remain parent-owned and pending. Nothing here promotes closure or parent acceptance.

Read K23 with K23E and CELL with CELLE; read ZA/ZB with ZE1-ZE4 and the binding P3/PADD manifests. This overlay is read
last. Where it targets CELLE's New text, amend that overlay before applying it to CELL. Source quotations in old
manifests remain frozen quotations; consumers use the corresponding source through these mandatory repairs.
No changed-marker condition is dropped: (a2-no5) retains E>=1, actual r_p=5^B w_p, actual-family FG-a2 and the apex-p
beta_zu<=3 condition; normalized (a2-zt5) retains all accepted S1-S5, including E>=2, alpha_zt=5 and alpha*_zt=1.
Connectedness and T*=W hypotheses of ZT/ZTR/ZW are retained at their stated scopes. IN excludes i=j, K3 has three
distinct vertices, and the EQ proof uses only the five non-z labels. Full-six odd coprimality is never asserted.

## Disposition

| Codex finding | exact items |
|---|---|
| R2 MAJOR, unsupported S-f mass | R2.1 |
| R2 distinct vertices / IN apex | R2.2, R2.3 |
| R2 five-index EQ coprimality | R2.4 |
| R3a M1 pair vectors | R3a.2, R3a.4 |
| R3a M2 labels / <=2 gcds | R3a.1, R3a.3; same correction in R3b.1 |
| R3b MAJOR five-non-z EQ audit | R3b.2-R3b.4, read with R2.4 |
| R3b p/z sentence scope | R3b.5 |
| R3b noncircular crossing counts and cells | R3b.6 |
| R3b current conditional DAG/status/pin closure | DAG.* and META.* |

## Verbatim Old -> New replacements

Every Old span is exact and occurs once in the pinned target. No target byte is changed. All unlisted hypotheses,
prior repairs, conclusions and exclusions remain at their existing scopes. The patch set only repairs the reviewed
arguments and status descriptions; the family partition is not an emptiness verdict.

### Item 1: R2.1 (Codex MAJOR: S-f mass replaced by the t-triangle)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-K23-v1.md` `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.

Old:

````text
- v1's alpha-row is (2,4,4,4 | alpha_tv1) (fours v2, v3, v4; alpha_v1c = 2 as v1, c are not alpha-twins), with
  alpha_tv1 <= 2 (v1 is single-alpha*-four). If alpha_tv1 = 1 it is R6: L_c subset L_v2 at v1, and at apex v2 in
  C^alpha the masses alpha*_v2c = 4 (c v2 in F*) and alpha*_v2v1 = 2 contradict K3. So alpha_tv1 = 2; likewise
  alpha_tv2 = 2.
````

New:

````text
- All four v_i are single-alpha*-four vertices, so alpha_tv_i <= 2 by (R-a) and INV. In the triangle {t,v1,v2},
  alpha_v1v2 = 4. If alpha_tv1 = 1, the accepted triangle rule forces alpha_tv2 = 4, a contradiction. Thus
  alpha_tv1 = 2, and the same argument with v1,v2 exchanged gives alpha_tv2 = 2. No value for alpha*_v1v2 is
  needed here; their equal F*-neighbourhoods do not exclude that starred entry being 1.
````

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

### Item 4: R2.4 (Codex MINOR: CELLE C.1 concerns five non-z indices)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CELL-erratum-v1.md` `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.

Old:

````text
(local indices 4 times an odd number; the odd parts of all local indices involved are pairwise coprime, as they are products of distinct w's and of 3^A 5^Bt for t)
````

New:

````text
(local indices 4 times an odd number; the odd parts of the five local indices belonging to g1,g2,s1,s2,s3 are pairwise coprime, as they use distinct w's and the possible factor 3^A 5^Bt for t; no odd-part coprimality involving z is assumed)
````

### Item 5: R3a.1 (Codex M2: retain p marker in W labels)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-erratum-v2.md` `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`.

Old:

````text
*Proof.* (i) At u in C^alpha* the labels are 3w (W-threes), e w (other W-entries e in {1,2,4}), 3 2^E w_z (z, as
c* = 3) and e* 3^A w_t (t).
````

New:

````text
*Proof.* (i) At u in C^alpha* the label of a W-neighbour v is alpha*_uv r_v: it is 3r_v for a W-three and e r_v
for another W-entry e in {1,2,4}, retaining r_p=5^B w_p when v=p. The other labels are 3 2^E w_z (z, as c*=3)
and e* 3^A w_t (t).
````

### Item 6: R3a.2 (Codex M1: ZW explicit feasible pair table)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-erratum-v2.md` `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`.

Old:

````text
k3 = 2, others b1, b2: y = 1/2 on the threes plus the standard
weights on {b1, b2}: 3 + 2, 3, 5, 2, 3, 4 for (1,1), (1,2), (1,4), (2,2), (2,4), (4,4); only (1,1), (2,2) are <= 5.
````

New:

````text
k3 = 2, others b1,b2: put weight 1/2 on each three and use the following explicit pair weights, in the displayed
order (these are not asserted to be the particular E8 vector):

| pair (b1,b2) | weights | pair value |
|---|---|---|
| (1,1) | (1,1) | 2 |
| (1,2) | (1,1) | 3 |
| (1,4) | (1,1) | 5 |
| (2,2) | (1/2,1/2) | 2 |
| (2,4) | (1/2,1/2) | 3 |
| (4,4) | (1/2,1/2) | 4 |

In the first three pairs the two local indices are coprime, so Sun(2) separates them; in the other three their
weights sum to 1. A three-label is coprime to both remainder labels, including a possible unique 5^B at p.
The total is 3 plus the pair value, so only (1,1) and (2,2) are <=5.
````

### Item 7: R3a.3 (Codex M2: two twos and odd t entry)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-erratum-v2.md` `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`.

Old:

````text
{s, s', t} has all gcds 2; a three never meets
````

New:

````text
{s,s',t} has gcds 2,gcd(2,e*),gcd(2,e*), all at most 2 (the odd cases already have a coprime pair); a three never meets
````

### Item 8: R3a.4 (Codex M1: ZT explicit feasible pair table)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-erratum-v3.md` `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.

Old:

````text
If k = 1 or 2, the total is >= 7 or 6, impossible. If k = 3, only remainders (1,1) and (2,2) avoid a value > 5:
(1,2) has value 3, (1,4) value 5, (2,4) value 3, and (4,4) value 4. The two surviving remainders have value 2, so the
````

New:

````text
If k = 1 or 2, the total is >= 7 or 6, impossible. For k=3 use these explicit feasible pair vectors (weights in
the displayed order), independently of the particular E8 vector:

| remainder pair | weights | pair value |
|---|---|---|
| (1,1) | (1,1) | 2 |
| (1,2) | (1,1) | 3 |
| (1,4) | (1,1) | 5 |
| (2,2) | (1/2,1/2) | 2 |
| (2,4) | (1/2,1/2) | 3 |
| (4,4) | (1/2,1/2) | 4 |

The first three pairs have coprime local indices (Sun(2)); the other pair weights sum to 1. Their labels are
coprime to the three-labels, so the combined vectors are feasible, retaining p's actual r_p=5^B w_p. Only
remainders (1,1) and (2,2), each of value 2, avoid total value >5. Thus the
````

### Item 9: R3b.1 (same local gcd clarification in ZB Step 2(iii))

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-B-v1.md` `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`.

Old:

````text
{s, s', t} has all gcds 2)
````

New:

````text
{s,s',t} has all gcds at most 2; if e* is odd it already has a coprime pair)
````

### Item 10: R3b.2 (Codex MAJOR M1: false six-index EQ audit)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-CELL-A2-TRANSFER-v1.md` `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`.

Old:

````text
| Lemma EQ | odd parts of local indices pairwise coprime | odd parts are distinct w's, 5^B w_p for p, 3^A w_t for t, 3 w_z for z: pairwise coprime |
````

New:

````text
| Lemma EQ | the five non-z two/four local indices have pairwise coprime odd parts | these five odd parts use distinct w's, the unique 5^B w_p if p occurs, and 3^A w_t if t occurs; no coprimality involving z is asserted (the t and z odd parts can share 3); use the explicit five-index saturation argument below |
````

### Item 11: R3b.3 (Codex MAJOR M1: explicit restricted five-index EQ saturation in TX)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-CASEA-CELL-A2-TRANSFER-v1.md` `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`.

Old:

````text
Every step above uses only facts in (B1)-(B7) of Theorem K7-A2-BRIDGE (as amended), Corollary 5/6-a2 / FG-a2, and
````

New:

````text
For each EQ use above, apply this local five-index argument, with every original marker and index hypothesis
retained. At the W-apex a, let Q be the union of the five non-z sets D_j (j in (W cup {t}) \ {a}). The actual-family
FG-V bound gives mu(Q)<=5/6, including when a=p: use FG-a2(b), beta_zt!=5 and beta_zu<=3 on W' (D23P), as in the
accepted OV-v2 transfer. Among these five sets two have mass 4/6 and three mass 2/6. Their five local indices have
pairwise coprime odd parts; hence the only pair gcd 4 is between the two large labels, and every other pair gcd is 2.
Let b be the measure of the union of the two large sets. Sun(3) implies that a right U_a-coset inside their union
holds at most one of the three small sets, and a coset outside it holds at most two. Summing the small masses gives

    1 <= b + 2(mu(Q)-b) <= 10/6-b.

Thus b<=4/6; since both large sets already have measure 4/6, they coincide and have union measure 4/6. This is precisely
the EQ equality consumed by SUB; it invokes no odd-part coprimality involving z and does not silently weaken an R2
hypothesis. It applies in either orientation of (a2-no5), for E>=1, with p in any allowed role or as apex.

Every step above uses only facts in (B1)-(B7) of Theorem K7-A2-BRIDGE (as amended), Corollary 5/6-a2 / FG-a2, and
````

### Item 12: R3b.4 (Codex MAJOR M1: explicit restricted five-index EQ saturation in ZA/ZB)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

Old:

````text
**Consequences.** Rigid rows whose weight vectors vanish on z keep their containments L_i subset L_j for i != z (and, if
the vectors also vanish on t, the containments with i = z via the t-free version). Lemma K3, K2, EQ hold with unions
taken without z; Lemmas SUB, IN, CELL are unaffected; Lemma B holds in both orientations at rows with c = 3 (each of its
kills vanishes on z or on t); PFG-t and the "at least two entries 4" part of Corollary L hold in both orientations.
````

New:

````text
**Consequences (restricted to the stated hypotheses).** Rigid rows whose weight vectors vanish on z keep their
containments L_i subset L_j for i!=z (and, if the vectors also vanish on t, the containments with i=z via the t-free
version). K3 is used only with pairwise distinct u,a,j and j,u!=z, so its two counted sets lie in the non-z union.
K2 uses the corrected R3' vectors (t weight 1/2). SUB, IN (i!=j) and CELL retain their group-theoretic hypotheses.
Lemma B is replayed only at rows with c=3 and its needed entry/label conditions, using vectors vanishing on z or t.
PFG-t's spanning-tree index argument holds at its connectivity scope; its connected-graph t-row consequences here
are ZT and ZTR (ZE3 and ZE4), not the old full Corollary L without its prerequisites.
For every EQ use in ZA or ZB, use this explicit local saturation proof. At a W-apex a, let Q be the union of the
five non-z D_j (j in (W cup {t}) \ {a}); FG-zf(b), omitting z, gives mu(Q)<=5/6. Two of these sets have mass 4/6 and
three have mass 2/6. The five local indices, not the z-index, have pairwise coprime odd parts: the actual r_p=5^B w_p
is retained and appears in no other label, and the possible 3^A is only at t. Thus every pair gcd is 2 except the
large-large pair gcd 4. Put b=mu(D_g1 cup D_g2). Sun(3) bounds small-set occupancy by one inside this union and by
two outside it. Their total mass is 1, so

    1 <= b + 2(mu(Q)-b) <= 10/6-b.

Hence b<=4/6, while b>=4/6 from each large mass. The two large sets therefore coincide with their union, of mass
4/6. No odd-part coprimality involving z is used. This proves exactly the needed EQ equality locally; it does not
assert a stronger full VFC union bound or an unqualified transfer of EQ. It covers p among the five labels or as
apex, and either configuration orientation under the stated z-free bound.
````

### Item 13: R3b.5 (Codex MINOR: restrict p/z prime assertion to actual uses)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-A-v1.md` `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`.

Old:

````text
  unchanged; labels of p and z carry no new common prime (z has no 5-part; only p carries 5^B).
````

New:

````text
  unchanged, with EQ replaced by the explicit five-non-z saturation argument in section 1. The assertion that
  p's unique 5^B introduces no extra common prime is restricted to the W-apex and cell gcd checks here: the
  W-apex z-label is 3*2^E w_z and the z-piece index has no factor 5. It is not a statement about apex t: in
  C^alpha* there the z-index is 5*2^E w_z and may share 5 with p. ZE4's ZTR and its W-only final 44411 filter,
  with weight zero on z, discharge those t-row obligations.
````

### Item 14: R3b.6 (Codex MINOR: explicit noncircular crossing and cell construction)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-A2-ZT5-B-v1.md` `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`.

Old:

````text
- m's: mu(U*_aU*_v) = mu(U*_aU*_t) = 4/6 and Lemma IN at the a's (alpha*_av = alpha*_at = 4) give m^H_v = m^H_t = 3;
  mu(U*_aU*_v1) = 4/6 and Lemma IN at v1, v2, t (alpha*_va = alpha*_ta = 4) give m^K'_a = 3; K' != H.
- Cells (Lemma CELL; piece indices n_v/3 = 2 r_v, with r_p = 5^B w_p, r_t = 3^A w_t, r_z = 2^E w_z): t does not share a
  K'-coset with v1 or v2 (pieces v, t, a with pairwise gcd 2, Sun(3)); z meets no cell of the K'-cosets of v1, v2
  (pieces v, a, z); so U*_z subset K' and z lies in the K'-coset of t; then N_z = n_z m^H_z / 9 forces m^H_z = 3 and
  N_z = 2^(E+1) w_z, and the pieces of t, a, z in any cell of that K'-coset have pairwise gcd 2: z meets no cell.
  Contradiction. QED
````

New:

````text
- m's, before any assertion about t's K'-coset: H contains all three a-subgroups, whose cosets occupy the three
  H-cosets. For j in {v1,v2,t}, mu(U*_aU*_j)=4/6 gives m^H_j>=2 by IN's lower bound, and any H-coset met by j
  contains an a-coset; IN there, using alpha*_aj=4, forces m^H_j=3. K' contains U*_v1,U*_v2,U*_t. The v1 and v2
  cosets are already distinct modulo K' by SUB, since U*_v1U*_v2=K'; t's placement is not yet used. For each a,
  mu(U*_aU*_v1)=4/6 gives m^K'_a>=2. Any two of the three K'-cosets include one of those two distinct v-cosets; IN at that
  v (alpha*_va=4) gives m^K'_a=3. Thus U*_aK'=G and H K'=G. In particular H!=K' and [G:H cap K']=9.
- Elementary cells, before using CELL's full distinct-coset hypothesis: put J=H cap K'. The index identity just
  proved gives nine left J-cosets, bijective with pairs of H- and K'-cosets. Each a-piece in any cell of its H-row
  is a coset of U*_a cap K' of index n_a/3=2r_a in J. For j in {v1,v2,t}, m^H_j=3 gives its pieces in its own
  K'-column index n_j/3=2r_j, whether or not t shares a column with a v. If t shared a K'-column with v1 or v2,
  each cell in that column would contain disjoint pieces of v,t and an a. Their three indices have pairwise gcd
  2, including p in any role (its unique fifth-prime factor has no partner); Sun(3) in J excludes t. Therefore
  v1,v2,t occupy three distinct K'-cosets. Only now invoke CELL with its full stated hypotheses.
- Final cells: r_p=5^B w_p, r_t=3^A w_t, r_z=2^E w_z. The CELL prime-factor bound for the z-piece gives pairwise
  gcds <=2 for pieces v,a,z in a v-column, so z meets no such cell. Thus its coset lies wholly in the remaining
  t-column and U*_z subset K'. Now N_z=n_z m^H_z/9 is an integer; n_z=3*2^(E+1)w_z has 3-valuation 1 and
  1<=m^H_z<=3, so m^H_z=3 and N_z=2^(E+1)w_z. Pieces t,a,z in any cell of that column then have pairwise gcd
  2, so Sun(3) excludes z from every remaining cell, contradicting its nonempty coset. QED
````

### Item 15: DAG.1 (current accepted R1 and unaccepted R2/R3 review gates)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
**R1**: parent-owned A1/A2 repair review, covering A1/TC/A22/A2 with overlay OV; verdict pending.
**R2**: parent-owned CASEA/CELL review, package `D/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`; statements are conditional premises of R3, not accepted
by this manifest. **R3**: parent-owned A2-side review requested with this manifest; no reviewer verdict exists here.
Accepted statements are marked **ACCEPTED-SCOPED** and their frozen parent record is identified separately.
````

New:

````text
**R1**: ACCEPTED-SCOPED by `R/sun7-K7-A1-A2-repairs-parent-verdict-v1.md`
`2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`, reading A1/TC/A22/A2 with OV v1 and OV2 (`9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`).
Only the verdict's named, hypothesis-bound claims are accepted; no whole-family closure follows from it.
**R2**: CASEA/CELL with CELLE, K23E and this consolidated repair: Codex ACCEPT-WITH-FIXES (1 MAJOR, 2 MINOR),
not parent-accepted. **R3a**: FG-zf/ZS/ZW/ZT/ZTR, Codex ACCEPT-WITH-FIXES (0 MAJOR, 2 MINOR), not parent-accepted.
**R3b**: TX/ZA22/ZT5-A/B and the conditional DAG, Codex ACCEPT-WITH-FIXES (1 MAJOR), not parent-accepted and still
conditional on R2/R3a at their scopes. The parent reports all three Claude attempts terminated NO_VERDICT rc1
(provider capacity); those exits are not mathematical verdicts. Fresh Claude review and scoped repair review remain
pending. None of R2/R3a/R3b is promoted to acceptance here. Accepted base records retain their exact scopes.
````

### Item 16: META.1 (same current gate labels in binding package)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

Old:

````text
**R1**: parent-owned A1/A2 repair review, covering A1/TC/A22/A2 with overlay OV; verdict pending.
**R2**: parent-owned CASEA/CELL review, package `D/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`; statements are conditional premises of R3, not accepted
by this manifest. **R3**: parent-owned A2-side review requested with this manifest; no reviewer verdict exists here.
Accepted statements are marked **ACCEPTED-SCOPED** and their frozen parent record is identified separately.
````

New:

````text
**R1**: ACCEPTED-SCOPED by `R/sun7-K7-A1-A2-repairs-parent-verdict-v1.md`
`2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`, reading A1/TC/A22/A2 with OV v1 and OV2 (`9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`).
Only the verdict's named, hypothesis-bound claims are accepted; no whole-family closure follows from it.
**R2**: CASEA/CELL with CELLE, K23E and this consolidated repair: Codex ACCEPT-WITH-FIXES (1 MAJOR, 2 MINOR),
not parent-accepted. **R3a**: FG-zf/ZS/ZW/ZT/ZTR, Codex ACCEPT-WITH-FIXES (0 MAJOR, 2 MINOR), not parent-accepted.
**R3b**: TX/ZA22/ZT5-A/B and the conditional DAG, Codex ACCEPT-WITH-FIXES (1 MAJOR), not parent-accepted and still
conditional on R2/R3a at their scopes. The parent reports all three Claude attempts terminated NO_VERDICT rc1
(provider capacity); those exits are not mathematical verdicts. Fresh Claude review and scoped repair review remain
pending. None of R2/R3a/R3b is promoted to acceptance here. Accepted base records retain their exact scopes.
````

### Item 17: DAG.2 (active pin closure includes OV2/K23E/ZE4/E18r/E19a and EQ)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
RICH has mandatory RICHE and RICHE2; D23P mandatory RICHE2; NO4 mandatory NO4E; INV mandatory INVE. The R1 files all
use OV. CELL uses CELLE. For ZE1: ZB.1/ZB.2 and MAP.2 remain active; ZA.1/ZA.2 withdrawal, MAP.1 and old PKG.1 are
superseded by ZE2/ZE3 and the R3 v2 manifest. P3 gives verbatim statements, import statuses and every Sun/index step.
````

New:

````text
RICH has mandatory RICHE and RICHE2; D23P mandatory RICHE2; NO4 mandatory NO4E; INV mandatory INVE. Every R1
source/edge citing OV is read with OV2 (`9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`), under accepted verdict VA1
(`2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`). Every K23 import includes K23E
(`15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1`), and CELL includes CELLE; both also include this consolidated repair.
Every ZA/ZA22/ZW/ZT/ZTR/ZB consumer is read with ZE1-ZE4, including ZE4
(`ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`), the binding addendum
(`06309c612a1543488f2a9db60f8b99aacdea7b3070eeeaeb8190441f291fd61a`) and this repair. E18r (ZTR), E19a (ZA22)
and the explicit five-non-z EQ consumer proof are prerequisites of E20/E21 at their stated scopes; none is accepted
merely by being listed. ZE1 ZB.1/ZB.2 and MAP.2 stay active; its withdrawal labels are superseded only conditionally
by ZE2-ZE4. The narrower zero-weight/omitted-vertex clauses are never replaced by a full-FG assertion.
````

### Item 18: DAG.3 (accepted exhaustion premise, not closure)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
Lemma F (PENDING R1, edge E12) says that (a2-o5) is empty.
Thus **conditional on that named lemma**, F is exhausted by the three disjoint classes
````

New:

````text
Lemma F (ACCEPTED-SCOPED by VA1, edge E12) says that (a2-o5) is empty.
Thus, using that accepted lemma, F is exhausted by the three disjoint classes
````

### Item 19: DAG.4 (ZS review gate)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
PENDING R3) instead splits T*=W versus size(T*)=3
````

New:

````text
PENDING R3a) instead splits T*=W versus size(T*)=3
````

### Item 20: DAG.E05 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E05: Case A/B -> A1 local row and t-row claims

- Claim: Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB (not the obsolete obstruction patterns).
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.
````

New:

````text
### E05: Case A/B -> A1 local row and t-row claims

- Claim: Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB (not the obsolete obstruction patterns).
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 21: DAG.E06 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E06: Case A all-(2,2) -> empty

- Claim: A22 uses the R1 row at E=1 as well as E>=2, with the mandatory overlay.
- Source pins: A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.
````

New:

````text
### E06: Case A all-(2,2) -> empty

- Claim: A22 uses the R1 row at E=1 as well as E>=2, with the mandatory overlay.
- Source pins: A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 22: DAG.E12 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E12: (a2) -> (a2-no5) or (a2-zt5)

- Claim: Lemma F excludes every five except z-t in at most one orientation. The auxiliary (a2-o5) set of section 2 is empty if F holds.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.
````

New:

````text
### E12: (a2) -> (a2-no5) or (a2-zt5)

- Claim: Lemma F excludes every five except z-t in at most one orientation. The auxiliary (a2-o5) set of section 2 is empty if F holds.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 23: DAG.E13 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E13: (a2-no5) -> enumerated RICH-type proof data

- Claim: BRIDGE gives its named claims and actual-family/auxiliary beta<=4 index chains, not an abstract beta<=5 theorem. W=W-prime union {p}.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.
````

New:

````text
### E13: (a2-no5) -> enumerated RICH-type proof data

- Claim: BRIDGE gives its named claims and actual-family/auxiliary beta<=4 index chains, not an abstract beta<=5 theorem. W=W-prime union {p}.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 24: DAG.E14 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E14: (a2-no5) -> transferred A1/TC/A22 claims

- Claim: Cor A2-TRANSFER gives the explicitly enumerated A1/TC/A22 claims including FG-V. It does not turn p into an unmarked index.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R1.
````

New:

````text
### E14: (a2-no5) -> transferred A1/TC/A22 claims

- Claim: Cor A2-TRANSFER gives the explicitly enumerated A1/TC/A22 claims including FG-V. It does not turn p into an unmarked index.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 25: DAG.E16 (replace obsolete R1-pending edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E16: (a2-zt5) -> unique normalized five orientation

- Claim: INV/E7 makes the other z-t entry 1; A2 S1-S5 give T=W, E>=2, prescribed t-W values and no other five. Inverse swaps the two orientation-labelled components.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING (structure); inversion accepted**. Covering review: R1; A: VINV.
````

New:

````text
### E16: (a2-zt5) -> unique normalized five orientation

- Claim: INV/E7 makes the other z-t entry 1; A2 S1-S5 give T=W, E>=2, prescribed t-W values and no other five. Inverse swaps the two orientation-labelled components.
- Source pins: A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`; OV2 `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`; VA1 `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`.
- Status: **ACCEPTED-SCOPED**, only at the displayed hypotheses. Covering record: VA1; no R2/R3 claim is accepted by this edge.
````

### Item 26: DAG.E07 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E07: Case A not all-(2,2) -> K2,3 structure or its inverse

- Claim: K3/K2/CL/S and S-a..S-f classify the remaining row graphs; no representative outside the inverse pair is dropped.
- Source pins: K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).
````

New:

````text
### E07: Case A not all-(2,2) -> K2,3 structure or its inverse

- Claim: K3/K2/CL/S and S-a..S-f classify the remaining row graphs; no representative outside the inverse pair is dropped.
- Source pins: K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`.
- Status: **PENDING**. Covering review: R2 PENDING; its R1 imports are ACCEPTED-SCOPED via VA1 and OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair.
````

### Item 27: DAG.E08 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E08: K2,3 structure and its inverse -> empty

- Claim: CELL-A via EQ/SUB/IN/CELL; the inverse has the same labelled index hypothesis.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).
````

New:

````text
### E08: K2,3 structure and its inverse -> empty

- Claim: CELL-A via EQ/SUB/IN/CELL; the inverse has the same labelled index hypothesis.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 PENDING; its R1 imports are ACCEPTED-SCOPED via VA1 and OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair.
````

### Item 28: DAG.E09 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E09: Case B -> TC-B plus t-a data

- Claim: TC-B supplies alpha*_v1v2=2 and alpha*=2 inside T*; CASEB-T supplies alpha_ta=2, alpha*_ta=4.
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.
- Status: **PENDING**. Covering review: R1 and R2.
````

New:

````text
### E09: Case B -> TC-B plus t-a data

- Claim: TC-B supplies alpha*_v1v2=2 and alpha*=2 inside T*; CASEB-T supplies alpha_ta=2, alpha*_ta=4.
- Source pins: A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`.
- Status: **PENDING**. Covering review: R1 part ACCEPTED-SCOPED via VA1/OV2; CASEB-T part PENDING R2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair.
````

### Item 29: DAG.E10 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E10: Case B and B-mirror -> empty

- Claim: CELL-B, corrected LFC orientation C^alpha* (CELLE C.4); mirror by INV, not a new assumed symmetry.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 (conditional on R1).
````

New:

````text
### E10: Case B and B-mirror -> empty

- Claim: CELL-B, corrected LFC orientation C^alpha* (CELLE C.4); mirror by INV, not a new assumed symmetry.
- Source pins: CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`.
- Status: **PENDING**. Covering review: R2 PENDING; its R1 imports are ACCEPTED-SCOPED via VA1 and OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair.
````

### Item 30: DAG.E15 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E15: (a2-no5), both orientation case splits -> empty

- Claim: Cor CC-A2 transfers K23/CELL named claims. Apply the same A/all-(2,2)/K2,3/B/mirror split to those claims.
- Source pins: TX `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.
````

New:

````text
### E15: (a2-no5), both orientation case splits -> empty

- Claim: Cor CC-A2 transfers K23/CELL named claims. Apply the same A/all-(2,2)/K2,3/B/mirror split to those claims.
- Source pins: TX `84cf955541c3ed6956fa59fd1e16e7ba3415b76e0a6b650c8f1b7b755cc775e6`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3b PENDING, conditional on R2/R3a as used; R1 imports ACCEPTED-SCOPED via VA1/OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair.
````

### Item 31: DAG.E18 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E18: Normalized (a2-zt5) plus connected Gamma^alpha -> t-row lemma ZT

- Claim: Initially allow alpha*_tu=3; PFG equality excludes those cases before invoking Cor L. Conclusion: no threes and at least two fours.
- Source pins: ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`.
- Status: **PENDING, materially new**. Covering review: R3 (A1 premise conditional on R1).
````

New:

````text
### E18: Normalized (a2-zt5) plus connected Gamma^alpha -> t-row lemma ZT

- Claim: Initially allow alpha*_tu=3; PFG equality excludes those cases before invoking Cor L. Conclusion: no threes and at least two fours.
- Source pins: ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`.
- Status: **PENDING, materially new**. Covering review: R3a PENDING; A1 premise ACCEPTED-SCOPED via VA1/OV2.
````

### Item 32: DAG.E20 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E20: T*=W, with ZW/ZT prerequisites -> empty

- Claim: ZT5-A audit: transfer K23/CELL-A using only justified z-free/t-free containments and unions; restoration is a candidate, not acceptance.
- Source pins: ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.
````

New:

````text
### E20: T*=W, with ZW/ZT prerequisites -> empty

- Claim: ZT5-A audit: transfer K23/CELL-A using only justified z-free/t-free containments and unions; restoration is a candidate, not acceptance.
- Source pins: ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3b PENDING, conditional on R2/R3a as used; R1 imports ACCEPTED-SCOPED via VA1/OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair. ZE4 `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`, E18r/E19a and the five-non-z EQ argument remain explicit prerequisites, not accepted conclusions.
````

### Item 33: DAG.E21 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E21: size(T*)=3 -> empty

- Claim: ZT5-B uses ZT before Step 1, ZE1 missing-case/e*<=3 repairs, and the two index-3 subgroup cell contradiction.
- Source pins: ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3, conditional on R1/R2.
````

New:

````text
### E21: size(T*)=3 -> empty

- Claim: ZT5-B uses ZT before Step 1, ZE1 missing-case/e*<=3 repairs, and the two index-3 subgroup cell contradiction.
- Source pins: ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`.
- Status: **PENDING**. Covering review: R3b PENDING, conditional on R2/R3a as used; R1 imports ACCEPTED-SCOPED via VA1/OV2.
- Mandatory consumer overlays: K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` and this consolidated repair. ZE4 `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`, E18r/E19a and the five-non-z EQ argument remain explicit prerequisites, not accepted conclusions.
````

### Item 34: DAG.E22 (retain conditional consumer gates and mandatory repairs)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
### E22: Five in alpha* (the inverse-labelled (a2-zt5) component) -> same normalized branches

- Claim: Apply INV once, retaining z,t,p and all actual exponents; then E16-E21 apply. No equal-marker or other K7 case is selected.
- Source pins: INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`; A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.
- Status: **Conditional on E16-E21; inversion ACCEPTED**. Covering review: A: VINV; R1/R3.
````

New:

````text
### E22: Five in alpha* (the inverse-labelled (a2-zt5) component) -> same normalized branches

- Claim: Apply INV once, retaining z,t,p and all actual exponents; then E16-E21 apply. No equal-marker or other K7 case is selected.
- Source pins: INV `45be91622b5973bf5e461d8ed08ae3e00544685d8a1728a8c3ae54738092726c`; INVE `7af9acf0f80659bdf875e0e7eb04fe281636050376d03fbbd83607dac7675bd5`; A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`.
- Status: **Conditional on E16-E21; inversion ACCEPTED**. Covering review: A: VINV and accepted R1 (VA1/OV2); downstream R3b and its R2/R3a premises PENDING.
````

### Item 35: DAG.final (current conditional implication only)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
**If** R1, R2 and R3 accept every pending claim at the indicated scope, E06/E08/E10 exclude the (a1) cases and mirrors,
````

New:

````text
With only the named R1 imports accepted by VA1, **if** the repaired R2, R3a and R3b claims are accepted at their
indicated scopes (including E18r, E19a and the explicit five-non-z EQ audit), E06/E08/E10 exclude the (a1) cases and mirrors,
````

### Item 36: META.2 (binding addendum current gate and edge status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-addendum-v1.md` `06309c612a1543488f2a9db60f8b99aacdea7b3070eeeaeb8190441f291fd61a`.

Old:

````text
R1 = A1/A2 overlay repair review, still PENDING. R2 = CASEA/CELL review, now read with K23E. R3 = A2-side review,
conditional on R1/R2 and now including ZE4. No reviewer output is claimed by this addendum.
````

New:

````text
R1 is ACCEPTED-SCOPED by VA1 (`2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966`), with OV v1 then OV2
(`9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181`). R2 (K23/K23E and CELL/CELLE plus this repair), R3a and R3b remain
PENDING parent acceptance. Their Codex ACCEPT-WITH-FIXES findings are repaired here; the parent reports all three
Claude capacity failures as NO_VERDICT rc1, not mathematical verdicts. All E18r/E19a and E20/E21 references below
retain ZE4 and add this repair's five-non-z EQ saturation proof and explicit noncircular cell construction.
Every stale 'conditional on R1' tag below means 'using the accepted named VA1 imports'; its R2/R3 gates stay pending.
````

### Item 37: META.3 (addendum concluding status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-addendum-v1.md` `06309c612a1543488f2a9db60f8b99aacdea7b3070eeeaeb8190441f291fd61a`.

Old:

````text
The pending R1/R2 statements remain conditional imports, and the overall chain is
````

New:

````text
The R1 imports are accepted only under VA1's scope; R2/R3a/R3b remain unaccepted conditional gates, and the overall chain is
````

### Item 38: META.4 (package concluding status)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

Old:

````text
Do not treat
any R1/R2/R3 candidate as accepted.
````

New:

````text
R1's named imports alone are accepted under VA1 with OV v1/v2; do not treat
any R2/R3a/R3b candidate or consumer transfer as accepted.
````

### Item 39: DAG.catalog (retain the missing mandatory source pins)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.

Old:

````text
| OV | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` |
````

New:

````text
| OV | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` |
| OV2 | `D/K7-A1-A2-delta-erratum-v2.md` | `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181` |
| VA1 | `R/sun7-K7-A1-A2-repairs-parent-verdict-v1.md` | `2a7c5b6c61b9e5df495cd15789af33fd017349572c3af2548d75245bd2def966` |
| K23E | `D/K7-CASEA-K23-erratum-v1.md` | `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` |
| ZE4 | `D/K7-A2-ZT5-erratum-v4.md` | `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e` |
| PADD | `D/review-package-A2-ZT5-addendum-v1.md` | `06309c612a1543488f2a9db60f8b99aacdea7b3070eeeaeb8190441f291fd61a` |
````

### Item 40: META.5 (replace obsolete import-status catalog rows)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

Old:

````text
| A1 | Section 0 triangle/two-four rules; Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB | `D/K7-A1-STRUCT-v1.md` | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` | PENDING R1, with OV; not its section 6 obstruction record |
| TC | TC, R1 (every E>=1), R3, FG-V, TC-B | `D/K7-TC-v1.md` | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` | PENDING R1, with OV; E=1 extension and FG-V material |
| A22 | All-(2,2) Case A excluded | `D/K7-TC-A22-v1.md` | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` | PENDING R1, with OV |
| A2 | Lemma F, FG-a2, 5/6-a2, D23-a2, ZT5 structure; enumerated BRIDGE/TRANSFER | `D/K7-A2-FIVE-v1.md` | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` | PENDING R1, with OV; not a blanket beta<=5 FG extension |
| OV | Mandatory combined A1/A2 overlay | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` | PENDING R1 |
````

New:

````text
| A1 | Section 0 triangle/two-four rules; Cor W3, E3, PFG-t/Cor L, Lemma B, CASEB | `D/K7-A1-STRUCT-v1.md` | `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf` | ACCEPTED-SCOPED by VA1, with OV+OV2; not its section 6 obstruction record |
| TC | TC, R1 (every E>=1), R3, FG-V, TC-B | `D/K7-TC-v1.md` | `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117` | ACCEPTED-SCOPED by VA1, with OV+OV2; row exponent hypotheses retained |
| A22 | All-(2,2) Case A excluded | `D/K7-TC-A22-v1.md` | `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41` | ACCEPTED-SCOPED by VA1, with OV+OV2 |
| A2 | Lemma F, FG-a2, 5/6-a2, D23-a2, ZT5 structure; enumerated BRIDGE/TRANSFER | `D/K7-A2-FIVE-v1.md` | `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc` | ACCEPTED-SCOPED by VA1, with OV+OV2; no blanket beta<=5 FG extension |
| OV | Mandatory combined A1/A2 overlay | `D/K7-A1-A2-delta-erratum-v1.md` | `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e` | ACCEPTED as amended by OV2 under VA1 |
| OV2 | Mandatory final A1/A2 overlay | `D/K7-A1-A2-delta-erratum-v2.md` | `9580ef7996d92d94f3f68c0df8934ab4889aeed227406e670cfd413281443181` | ACCEPTED-SCOPED by VA1 |
````

### Item 41: META.6 (accepted F premise)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

Old:

````text
**(a2-zt5):** at least one orientation x in {alpha,alpha*} has x_zt=5. Lemma F, pending R1, says no other pair can carry
````

New:

````text
**(a2-zt5):** at least one orientation x in {alpha,alpha*} has x_zt=5. Lemma F, accepted at VA1's scope, says no other pair can carry
````

### Item 42: META.7 (accepted partition premise)

Target: `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.

Old:

````text
conditional on R1. These two index-and-pair conditions are inversion-stable.
````

New:

````text
using the accepted Lemma F under VA1. These two index-and-pair conditions are inversion-stable.
````

