# Results r2 (interim) of the reflection desk, after host clock 2026-10-18T08:52:02-0700

Owner OlsonReflectionRigidity.  This is an interim summary; results.md and checkpoints 01-03 are earlier and kept unchanged.
It makes no claim about REFL(p), INV*(p) or ordered Olson beyond the scopes below.  Finite aids are not premises.

## Status of written results (this session)

1. B0S++ (proof-B0SPP-r5.md).  Errata-only r5 for Codex's MINOR on r4 (r4: ACCEPT-WITH-FIXES 0/0/1).  It is the imported base
   of B0S-CJ.
2. Theorem B0S-CJ (proof-B0SCJ-r1.md; errata r2 = Codex fixes 2 and 3).
   - Under R >= 4 kappa + 1, two disjoint heavy admissible intervals force J = 0, so the word is solvable.  The key is Lemma CJ:
     c(S) = J for every heavy admissible S.
   - Corollary: no B = 0 avoider with Delta <= 1 or p >= kappa + 5 Delta - 5.  For p <= 23 this covers all of R >= 4 kappa + 1.
   - Codex: ACCEPT-WITH-FIXES 0/0/MINOR (R/olson-b0scjx-r3-codex-v1.note.md).
3. Theorem B0S-CJ''' (proof-B0SCJx-r3.md; errata r4 = Codex fix 1).
   - The same under R >= 4 kappa - 4 and 2 kappa <= p - 1.
   - It uses the exact (A') criterion (m1 + m2 >= 4 kappa - 4 - R), the exact two-small (B') case, and a last-step analysis of
     B0S-r4's Case I greedy.
   - Codex: ACCEPT-WITH-FIXES 0/0/MINOR.  r1 and r2 are earlier, weaker versions.
4. Corollary REFL-few-odd (proof-REFL-fewodd-r5.md; r2 reviewed; r3-r5 errata).
   - REFL(p) holds for every avoider with at most p odd maximal constant reflection blocks.
   - It follows from RED's process, in which o_F is monotone, and the accepted small-k verdict.
   - Codex ACCEPT 0/0/0 (twice); Claude ACCEPT-WITH-FIXES 0/0/9 plus 3 chain-review MINORs.
   - Parent-ACCEPTED (R/olson-refl-fewodd-parent-verdict-v1.md, as reported by Main).
5. Documentation errata: proof-K0star-r3.md (Claude m1-m6) and proof-RED-r3.md (Claude 1-7).
6. proof-B0SEED-r1.md is a superseded, unsent draft.  Do not review it.

## Finite aids (pre-registered; plan mtimes precede output mtimes; "~HH:MM" labels inside plan-E14c..E15 were estimates)

- E14/E14b/E14c/E14d: interval-level structure in regime (III).
  - In some IIIa cells c = 0 everywhere and J = 0.
  - In others (theta+ <= 0, or (17,7,18)) and in IIIb, interval-feasible data have c != 0 and J != 0.  So interval-level SIGMA
    is false in parts of regime III (notes-RIII-r1.md Sec. 3).
- E14e/E14f: every tested interval-feasible leaf is killed by a 2-interval pattern.  These leaves are random-like, so the evidence
  is weak.
- E15: exhaustive.  p = 7, (kappa, k, R) = (3, 13, 7): 0 assignments survive all interval and 2-interval windows (132 data,
  70,759 nodes).  So, given H0, that cell has no avoider.
- E15b: exhaustive census of the remaining p = 7, B = 0 cells.
  - (4, 15, 7) (IIIb): 429 data, 3,533,152 nodes, 54,927 2-avoiders.  Every one is killed by a 3-interval pattern; 0 full
    avoiders.
  - (5, 17) was interrupted by the CPU limit (exit 152) and is UNKNOWN.  No output exists for it.
  - E15b v2 (survivors first tested with m = 3) is running on the IIIa cells (4, 13) and (4, 12).

## Open (B = 0, k >= p + 1)

- (a) Numerical failures of Corollary 2 (large Delta).
- (b) The edge cells kappa = (p + 1)/2, R >= 2p - 2.
- (c) Deep IIIa, 2 kappa < R <= 4 kappa - 5.
- (d) IIIb, R <= 2 kappa.
In (c) and (d) interval-level SIGMA fails in general.  The data suggest that 2-interval patterns suffice in IIIa and that
3-interval patterns are needed in IIIb.
B >= 1 with k >= p + 1 is untouched.

## Correction to notes-RIII-r1.md

Sec. 2 (W) says c(X u Y) - c(X) - c(Y) = -omega.  The correct sign is +omega, because c(X u Y) - c(X) - c(Y) = (v*_X + v*_Y +
v*_Z - mu)/p.  Its statements about upward and downward wraps are consistent with +omega.  A corrected notes version will
follow.

## File hashes (sha256)

* proof-B0SPP-r5.md  d388d3910ef12aa59c3a12878c578edf1608b444342fb99cc417f271a2a6bd64
* proof-B0SCJ-r1.md  a775321c2e70d9adf86963c59d15fcb66f63042f7ec84edcf36e34731f4940af
* proof-B0SCJ-r2.md  f90c8b53cfeea9b909266be0b27c3e15a39b400c721cba70af49538dbf92c0ed
* proof-B0SCJx-r1.md  58c02ebea88b9198cc0bf7f1218e83e5433515b571521a10a4c173db4642d42e
* proof-B0SCJx-r2.md  43032a0f712064bd765c4bef3aad3d4695e803ec39d234b8f9bde32df6485779
* proof-B0SCJx-r3.md  565f79d956fa7bc39c66a848981683c3bb2f6e2d4e37cebb2b98194f6c1d083b
* proof-B0SCJx-r4.md  f2779c243289713b5e8b34a4206379d7054ff8cc8e0b0479893f1d44e189843d
* proof-B0SEED-r1.md  33a164cdf0a738f91a48619d4e54b5da61f0de86cabf331dd114e6c760088e55
* proof-REFL-fewodd-r1.md  6058831acc970e86a33f007bf900de397eaba5ccac7318bd3ba93a0bd61d7dd7
* proof-REFL-fewodd-r2.md  db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6
* proof-REFL-fewodd-r3.md  d1cdb96e03f3d24faa11914ffc35d83997172689d761175f71e7dd4a952cc435
* proof-REFL-fewodd-r4.md  1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d
* proof-REFL-fewodd-r5.md  4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363
* proof-K0star-r3.md  845d2ddf5e0fb42156111168b99f7749c7742f8bed5ce68ae5707b3364c8ba1d
* proof-RED-r3.md  9eb74e96860701c3d4dfdca347fb2efbecd26fb44714122ae3d7bb28d4e7e3e6
* notes-RIII-r1.md  82548b93f82ee81fef0ca3e32e2f573b09fd880af13a83923e826e1fc3257b1f
* plan-E14.md  84784dc089a80485d71e2f6823e080f37d4926e03ea78b928c19bbc38e965df1
* plan-E14b.md  d71ab2d074bb02a5b3781250f28853505c388967ac5d5b49451ec17544d2ccfa
* plan-E14c.md  c2f080aed6cffbffdf12ee5a12bcac565231144c9f7cbaecf43c10910daac5f2
* plan-E14d.md  3d46499624be15ca1ded9e91f3c232575504822a106e497f0d99660add5ab2ec
* plan-E14e.md  78e69f9ee26ec4adb7d96371ad6cfffedb80a22c378ded0fce49bbd9d93fcddf
* plan-E14f.md  b1ef0f80529ca832c1a234fa35b73bffb77e70c290b7c8da2694c90d8a2d62c9
* plan-E15.md  c9bd4cf06796f5c3d7f653b2fc6b1bd07b82c929379783b1d5795554cd895feb
* plan-E15b.md  8c6fb1e55f4b12ad4e7cc40542aae664332ccf0fe4dcabe491381bedc4112b4d
* out/e14_cfunc_regime3.json  e91fe646c70f17b1343526fb87342f56d07fefdc7d77a1677612ab959548f442
* out/e14b_cfunc_general.json  bbbc3a5f63112f9e2ae3ea0dd012eadff589c5eab72eb4558914dfb888102c3e
* out/e14c_cfunc_theta.json  6eb10a8881783973eb63d756f9b1043c514a0487f9e573f76e692b86c6bf613e
* out/e14d_cfunc_theta.json  74e54186335f63e30629bf387f9d0af67ca5390535f2c715f9518fdb5ece8669
* out/e14e_kills.json  d54c19ff9abcbb8e673d6f5e9995a7990ddfe4551ad9fc6b65e50c5f5cc54097
* out/e14f_kills_iiib.json  16178e5e31d8b8d5d9c43a727674d1b3390bbccc30e1bbeff8455e454d979564
* out/e15_two_avoiders_p7k3.json  0e01fdda17b8b731a1f4b97ea88d44dba844f69b5d134d70baa0b9220a74c035
* out/e15b_4_15.json  ff370b2f3a3c9e28196e0d5eba999fbedadb4ae74aa4e6edd31a59ab494f07e3
* code/e14_cfunc_regime3.py  ce09e887d2c4da152fcb4d8e9df5781e3231d1b7607f86b6200d507eedbb9892
* code/e14b_cfunc_general_v2.py  f8729c90fd2587a40c75eb6f2b4cb1c9525cc896f16ac52f40b6d4bf0709b905
* code/e14c_driver.py  460a4656ffee2fa68e07369f5dadf4583c181ec80b635d0945141ae3e9a3ffed
* code/e14d_driver.py  d09e68d0706bb281b08015dacc9906c9ef328e3016767d6ac75ebf48c2643860
* code/e14e_kills.py  1addf50b58326f076f91a8b6c07141b7321c980a55726181eba6d86c00cb3e49
* code/e14f_kills_iiib.py  75c7f119c1685459c98e2a097c5119e59fc76bf24c0577b6a8d8963840ccdc0c
* code/e15_two_avoiders.py  133eeb7ad24ae76072e076e1a651c66fcf9ac24cae1b4ef25997062267cb144d
* code/e15b_census.py  fe1e0b0fe46abeba5ae4f22c0b6e5d24e13d3f7172f80309b92eb22c65d3334c
* code/e15b_census_v2.py  5c9b9b57c3e58537a8e15753a2ca5ee99612c8035a607400fad181397ca80a7e
