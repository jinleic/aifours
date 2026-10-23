# Review package / DAG addendum v1: corrected R3' display and the explicit ZTR / ZA22 prerequisites

Written: 2026-10-19T08:13:32-0700 (`/bin/date` immediately before exclusive create). Owner: Sun7K62Successor.
Written manifest only. No source overwrite or computation. All new items are PENDING, not accepted. No closure claim.

## 1. Binding packages and new source pins

Directory D = `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue`. These two navigation files remain frozen:
- R3 manifest v2: `D/review-package-A2-ZT5-v2.md` `7a63ea38dcf703315cc2f1917a07e336b0559feb9c705cd6cc3c83ddbaf0dfa1`.
- Conditional family DAG v2: `D/K7-family-closure-map-v2.md` `2120a3bcf7a20e42fd3f3d9f884cd8853318fa971249900fb5cd36fe5c09a32b`.
- R2 base package: `D/review-package-CASEA-CELL-v1.md` `e892c98b0331e3496f5cbc8dd101058e8f9125c823fa06559f47749e590c6583`.

Add the following frozen sources:

| key | source | full SHA256 | review / status |
|---|---|---|---|
| K23E | `D/K7-CASEA-K23-erratum-v1.md` | `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1` | R2, PENDING; corrected displayed R3' vector and written feasibility proof |
| ZE4 | `D/K7-A2-ZT5-erratum-v4.md` | `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e` | R3, PENDING; material new ZTR / ZA22 audit |

R1 = A1/A2 overlay repair review, still PENDING. R2 = CASEA/CELL review, now read with K23E. R3 = A2-side review,
conditional on R1/R2 and now including ZE4. No reviewer output is claimed by this addendum.

## 2. Exact new statements (verbatim)

### Lemma ZTR

```text
In normalized (a2-zt5), if Gamma^alpha* is connected, then at least two of the five alpha_tu (u in W) equal 4.
```

### Lemma ZA22

```text
In normalized (a2-zt5) with T*=W, no configuration has two alpha-fours and two alpha*-fours at every vertex of W.
This is a conditional transfer of A22, using FG-zf, ZW, ZT and ZTR, not an assertion that its (a1) statement already
covers the new family.
```

## 3. Active precedence and restricted transfers

Keep TX/ZA/ZB and ZE1-ZE3 from the R3 v2 manifest, adding ZE4 after ZE3. Read K23 with K23E everywhere it is imported.
The exact corrected R3' y2 has t weight **1/2**, not 1: the old vector had value 7 and was infeasible, while the new
one has value 5 and is feasible by the stated Sun(2)/Sun(3) checks. The theorem conclusions of K23 do not change.

The ZT5-A reinstatement remains a candidate. Its active audit is ZA plus ZE2 ZW, ZE3 ZT, ZE4 ZTR/ZA22 and K23E.
In particular:
- Before K23 classifies Case A, ZA22 must exclude the all-(2,2) case; this prerequisite was implicit in ZA v1.
- ZW(ii) and ZB Step 1 use ZT, allowing threes initially, not a prematurely applied full Cor L.
- The reverse at-least-two-fours use in CL and A22 uses ZTR. The extra z-label 5*2^E w_z can share 5 with p, so the full
  old Cor L equality classification is **not** transferred at that scope.
- K23's final 44411 exclusion in either K2,3 orientation is its direct value-6 PFG kill (weights 1/3 on three fours and
  1 on both ones), not a z-isolation equality argument.

## 4. DAG supplements / replacement pins

Every pin below resolves to its filename in this addendum or the v2 map; full SHA256s are repeated explicitly.

- **New E18r:** normalized (a2-zt5), connected Gamma^alpha* -> |P|>=2, by ZTR.
  Source pins: ZE4 `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`; A1 `c8a16f14c910a3550d0063a5217e96846947c43d2193da958f8ba769bc8e3ccf`; A2 `93fd95d7422c0dad3bd39fdd4bf01b66485aacd0f8da008971356ce30c9d8dfc`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`. Status PENDING; R3, conditional on R1.
- **New E19a:** normalized (a2-zt5), T*=W and all-(2,2) -> empty, by ZA22.
  Source pins: ZE4 `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; A22 `9ebec2797485ac18ff1f1080cafd0634edd86117d166338631e04c4db1a46b41`; TC `cc48340d016489347132099ae1178719c65d92b2dc5ecc6113da013e2cf7e117`; OV `0e477743c650e0db7d48b3b242f1e0a402e50117c28ff26c34bb3256a7b7e54e`. Status PENDING; R3, conditional on R1.
- **E07/E09 update:** all uses of K23's rigid R3' row are read with K23E.
  Source pins: K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1`. Status PENDING; R2 (conditional on R1).
- **E20 update:** the T*=W exclusion uses the corrected CASEA proof and all newly explicit prerequisites, including
  E18r and E19a before its cell contradiction.
  Source pins: ZA `4948e4d71f966da6d43c49a3316ad102db13eaaa0eaf0aa938d1508c618f6919`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE2 `c7c0d9bc61009421b79e817ac4c69d27e40a3914f04ba0b1d1b013b1abbf4f47`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; ZE4 `ee68f078df81bab2299c03d9c38eafb3f0737d3305b914c2a61876c78685ab9e`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`. Status PENDING; R3 conditional on R1/R2.
- **E21 update:** ZB's imported rigid-row list uses K23E; its t-row step still uses ZT, and its Step 2 uses ZE1 ZB.1/ZB.2.
  Source pins: ZB `f482090adae221ea7bcaa23e1102aa4d3d4081933fd762f756f190d4ddf1f3a8`; ZE1 `82d01721688ad10dfa44ed01aca0b914c515f0c508e24345587e063c6dca6dc4`; ZE3 `aa182c6c4bdaa5644c13db09fa661c40fbfc9e6d7aa2471c56f106c7a47a7667`; K23 `f70c8fdc9414642f33013dde704b887eac06a938f17ea22f11ccf65007dc3fd3`; K23E `15b1516d7bc5d124565c8e16ea686b2b9b4947080aa059f37fd02d83040e14e1`; CELL `d421e08c8ee39235cbde43700ffcdf2e92f03c0175ae076ec9214ca486db7aae`; CELLE `56829e8dde93fb8496a91e6a0739a2a60628cbfb0d33d5425805b4b7495c8132`. Status PENDING; R3 conditional on R1/R2.

The family exhaustion proof and inverse/mirror normalization are unchanged. New E18r/E19a fill prerequisite nodes;
they are not extra family assumptions and do not remove a branch without a proof candidate.

## 5. Additional Sun / index obligations for review

**K23E:** the isolated one uses Sun(2). Each pair of twos with f or t is forbidden by Sun(3), making the corrected
vectors feasible. Subtracting their weight-1 equations gives f iff t; z with two twos is also a Sun(3) exclusion.
The equality conclusion itself is the relevant full or z-free fibre clause, not a new Sun instance.

**ZTR:** the spanning-tree intersection index has factors <=2 and only p's own 5^B, so gcd(n_t,T_W)=6 as in ZT.
The one-four value-6 vector uses Sun(2)/Sun(3). In the zero-four equality case, Sun(3) excludes z together with two
W' twos; thus D_z cap Q subset D_p. The measure inequality 4/6<=mu(D_z cap Q)<=mu(D_p)<=2/6 is a capacity contradiction,
not an enumeration or an assumption that z is coprime to p.

**ZA22:** at e<=2 the R1/four-equality vectors vanish on z, so FG-zf applies to the needed four-containing fibres.
ZT and ZTR supply |P*|,|P|>=2. The cycle count uses TC and Sun(3) on two twos plus z or t, and contradicts V4's strict
union bound (<1); it does not claim a new full 5/6 bound. The unique 5^B of p has no second 5-part at those W-apices.
The extra final 44411 filter has value 6 from singleton ones (Sun(2)) and three fours of weight 1/3.

Reviewer focus: verify these newly exposed prerequisite edges as part of R3; do not substitute the old unqualified
Cor L in the reverse orientation. The pending R1/R2 statements remain conditional imports, and the overall chain is
not an accepted closure of F, K7 or Sun(7). No novelty, Lean or human-review claim.
