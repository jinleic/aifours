# Results r3: final continuation package of the reflection desk (REFL-RES(p)), after host clock 2026-10-18T12:20:52-0700

Owner OlsonReflectionRigidity.  This supersedes results-r2.md (interim), which is kept unchanged.  No claim is made about REFL(p)
in full, INV*(p) or ordered Olson.  Finite aids are not premises.

## A. Accepted or reviewed written results (exact scopes in the files and the parent verdicts)

1. **B0S++** (proof-B0SPP-r5.md; r4 Codex ACCEPT-WITH-FIXES).  Imported base of B0S-CJ.
2. **Theorem B0S-CJ** (proof-B0SCJ-r2.md) and **B0S-CJ'''** (proof-B0SCJx-r4.md).
   - Parent CORRECTNESS-ACCEPTED in R/olson-cj-cjx-parent-verdict-v1.md (5cfd6a4f...45f6d, with overlay); Codex and Claude
     reviewed.
   - B = 0, all blocks odd, kappa >= 1, R >= 4 kappa - 4 and 2 kappa <= p - 1.
   - Solvable if Delta <= 1, if p >= kappa + 5 Delta - 5, or more generally under the word-level condition (2HA).
3. **Corollary REFL-few-odd** (proof-REFL-fewodd-r5.md).  REFL(p) holds for avoiders with o_F <= p odd maximal constant blocks.
   - Parent-ACCEPTED (R/olson-refl-fewodd-parent-verdict-v1.md); Codex ACCEPT twice; Claude ACCEPT-WITH-FIXES, errata in r3-r5.
4. Documentation errata: proof-K0star-r3.md and proof-RED-r3.md.

## B. New written results awaiting review

5. **Corollary REFL-B0** (proof-REFL-B0-r3.md; r2 is under review, r3 is a wording-only change).
   - REFL(p) for avoiders whose rotation letters are all equal.
   - Hypotheses: R >= 4 kappa - 4, 2 kappa <= p - 1, and (R >= p + kappa - 2 or 5R >= 4p + 6 kappa - 10).
   - No bound o_F <= p is imposed; o_F = 2p - R + 2 kappa.
6. **Lemma EDGE** (proof-B0Sedge-r2.md).
   - B = 0 has no avoider in the edge cells kappa = (p + 1)/2, R in {2p - 2, 2p - 1}.
   - Hence B0S-CJ''' holds under R >= 4 kappa - 4 alone.  With it, REFL-B0 can drop "2 kappa <= p - 1".

## C. Exact open gaps (B = 0, k >= p + 1), as of this package

(a) Numerical failures of Corollary 2 under R >= 4 kappa - 4: cells with Delta >= 2 and p < kappa + 5 Delta - 5.
    - They occur only when (p + 10)/6 < kappa < (2p + 5)/7.  The first is (13, 4, 13, 3, 21).
    - There (2HA) must be checked word by word.
(b) CLOSED by Lemma EDGE, pending review.
(c) Deep IIIa: 2 kappa < R <= 4 kappa - 5.
(d) IIIb: R <= 2 kappa, equivalently k >= 2p.
In (c) and (d), interval-level SIGMA is false in general (E14c/E14d).  Any proof must use patterns with >= 2 intervals
(notes-RIII-r2.md).
Untouched: B >= 1 with k >= p + 1.  MXG covers only k <= p; the B >= 1 c-function has pair indices summing to 2R - B.

## D. Finite aids (pre-registered; not premises)

- E14-E14f (notes-RIII-r2.md Sec. 3).
- p = 7, B = 0 census (census-receipts-r1.md).  It is exhaustive over P0-valid run data and all residue assignments, with exact
  H0 windows.
  - 0 full avoiders in every cell with kappa <= 5, i.e. (3,13), (4,9..15), (5,11..17), and in (6,13).
  - (6,14)-(6,19) are UNKNOWN or not run.
  - The positive control finds the known length-(4p - 3) avoider.
- E16 (p = 11 sampling) is planned, not launched.
Process deviation, recorded: the census runs used hard `ulimit -t` backstops, which the frozen round contract prohibits.  All
stops are UNKNOWN; see census-receipts-r1.md.

## E. Suggested next steps

1. A 2-interval kill lemma for deep IIIa: the E15/E15b data show <= 2 survivors per p = 7 cell after intervals and 2-patterns.
2. For IIIb, multi-interval windows.  The strongest come from balanced patterns with about kappa + 1 - R/4 intervals, whose
   forbidden size is about R/2.  3-patterns sufficed at p = 7.
3. A B >= 1 analogue of Lemma CJ (indices E = D_P + B), and then of MXG's kill for k >= p + 1.

## F. File hashes (sha256)

* proof-B0SPP-r4.md  669e5d97392fef8b27f0ada8cead81a1b24c0a2897bf98b67bea9a0d2c5424dc
* proof-B0SPP-r5.md  d388d3910ef12aa59c3a12878c578edf1608b444342fb99cc417f271a2a6bd64
* proof-B0SCJ-r1.md  a775321c2e70d9adf86963c59d15fcb66f63042f7ec84edcf36e34731f4940af
* proof-B0SCJ-r2.md  f90c8b53cfeea9b909266be0b27c3e15a39b400c721cba70af49538dbf92c0ed
* proof-B0SCJx-r1.md  58c02ebea88b9198cc0bf7f1218e83e5433515b571521a10a4c173db4642d42e
* proof-B0SCJx-r2.md  43032a0f712064bd765c4bef3aad3d4695e803ec39d234b8f9bde32df6485779
* proof-B0SCJx-r3.md  565f79d956fa7bc39c66a848981683c3bb2f6e2d4e37cebb2b98194f6c1d083b
* proof-B0SCJx-r4.md  f2779c243289713b5e8b34a4206379d7054ff8cc8e0b0479893f1d44e189843d
* proof-B0Sedge-r1.md  893c04ff677a24b002e4507f2d26d0388f226789aab14b7e89b97991e16ffa35
* proof-B0Sedge-r2.md  ac2de0d299849aa50e733fbe01deb2448bfa19f8e67f33137daa0a2459a70ba3
* proof-B0SEED-r1.md  33a164cdf0a738f91a48619d4e54b5da61f0de86cabf331dd114e6c760088e55
* proof-REFL-fewodd-r1.md  6058831acc970e86a33f007bf900de397eaba5ccac7318bd3ba93a0bd61d7dd7
* proof-REFL-fewodd-r2.md  db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6
* proof-REFL-fewodd-r3.md  d1cdb96e03f3d24faa11914ffc35d83997172689d761175f71e7dd4a952cc435
* proof-REFL-fewodd-r4.md  1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d
* proof-REFL-fewodd-r5.md  4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363
* proof-REFL-B0-r1.md  66375f8fb9085c567a7b2649118557a091557850f0f4dce8456498ca7089020e
* proof-REFL-B0-r2.md  32671067ff7a6b355da0882d85416a2a472599e31a171aac6a2e7e7ef00c475b
* proof-REFL-B0-r3.md  c05eb38386e8e1a239f6abf51875f3fcc02c1ce2304cf14063be9d95bd412272
* proof-K0star-r3.md  845d2ddf5e0fb42156111168b99f7749c7742f8bed5ce68ae5707b3364c8ba1d
* proof-RED-r3.md  9eb74e96860701c3d4dfdca347fb2efbecd26fb44714122ae3d7bb28d4e7e3e6
* notes-RIII-r1.md  82548b93f82ee81fef0ca3e32e2f573b09fd880af13a83923e826e1fc3257b1f
* notes-RIII-r2.md  df2b96ad68eca33483f0a05765109d0b1d077575b4ee57f1d9111da790da4b4a
* results-r2.md  69372ce2c4abda4c82613ebb242efbc74352cfbfde115eb3ac37e70839e3a6ae
* census-receipts-r1.md  aafbc20751cbe1964203fecc13b66e0af52c8d53567ce314f99a1e24382ed23f
* plan-E14.md  84784dc089a80485d71e2f6823e080f37d4926e03ea78b928c19bbc38e965df1
* plan-E14b.md  d71ab2d074bb02a5b3781250f28853505c388967ac5d5b49451ec17544d2ccfa
* plan-E14c.md  c2f080aed6cffbffdf12ee5a12bcac565231144c9f7cbaecf43c10910daac5f2
* plan-E14d.md  3d46499624be15ca1ded9e91f3c232575504822a106e497f0d99660add5ab2ec
* plan-E14e.md  78e69f9ee26ec4adb7d96371ad6cfffedb80a22c378ded0fce49bbd9d93fcddf
* plan-E14f.md  b1ef0f80529ca832c1a234fa35b73bffb77e70c290b7c8da2694c90d8a2d62c9
* plan-E15.md  c9bd4cf06796f5c3d7f653b2fc6b1bd07b82c929379783b1d5795554cd895feb
* plan-E15b.md  8c6fb1e55f4b12ad4e7cc40542aae664332ccf0fe4dcabe491381bedc4112b4d
* plan-E15c.md  de7adc451b5360879ab4f91b5dc3d95a7ca16a3ef234251be5a02e3185cdad76
* plan-E16.md  ae24f21fafa8e070c75a3c81dec8326a5ffff7ecf3c07126bcd5cbafcc1c4bb6
* plan-E16-addendum.md  4dd0cf273f888f3771d20cf8b45ee81cf3e04a8a2464fec96248b21833875809
* code/e14_cfunc_regime3.py  ce09e887d2c4da152fcb4d8e9df5781e3231d1b7607f86b6200d507eedbb9892
* code/e14b_cfunc_general.py  6134d687647a3253317a89bf902d4815902a8229b9d82260ef18b2c36939ff98
* code/e14b_cfunc_general_v2.py  f8729c90fd2587a40c75eb6f2b4cb1c9525cc896f16ac52f40b6d4bf0709b905
* code/e14c_driver.py  460a4656ffee2fa68e07369f5dadf4583c181ec80b635d0945141ae3e9a3ffed
* code/e14d_driver.py  d09e68d0706bb281b08015dacc9906c9ef328e3016767d6ac75ebf48c2643860
* code/e14e_kills.py  1addf50b58326f076f91a8b6c07141b7321c980a55726181eba6d86c00cb3e49
* code/e14f_kills_iiib.py  75c7f119c1685459c98e2a097c5119e59fc76bf24c0577b6a8d8963840ccdc0c
* code/e15_two_avoiders.py  133eeb7ad24ae76072e076e1a651c66fcf9ac24cae1b4ef25997062267cb144d
* code/e15b_census.py  fe1e0b0fe46abeba5ae4f22c0b6e5d24e13d3f7172f80309b92eb22c65d3334c
* code/e15b_census_v2.py  5c9b9b57c3e58537a8e15753a2ca5ee99612c8035a607400fad181397ca80a7e
* code/e15c_census.py  e05616aabc84acc308aa75ca50820e9ac4811d79febbb7c0f7f8579f665565e7
* code/e15_control_pos.py  5f561c90b2ba50c6142751e1b9423e072a5e60e274f64dfe2156336c0f0c71bf
* code/e16_p11_sample.py  6ac746776044f454e1ca51658878b970e7292f3a2fe62474cb6b189774f87abd
* code/e16_p11_sample_v2.py  536858537093a68ada6bd3fc361e4111cba252554f27302e64928ad1db522d62
* out/e14_cfunc_regime3.json  e91fe646c70f17b1343526fb87342f56d07fefdc7d77a1677612ab959548f442
* out/e14b_cfunc_general.json  bbbc3a5f63112f9e2ae3ea0dd012eadff589c5eab72eb4558914dfb888102c3e
* out/e14c_cfunc_theta.json  6eb10a8881783973eb63d756f9b1043c514a0487f9e573f76e692b86c6bf613e
* out/e14d_cfunc_theta.json  74e54186335f63e30629bf387f9d0af67ca5390535f2c715f9518fdb5ece8669
* out/e14e_kills.json  d54c19ff9abcbb8e673d6f5e9995a7990ddfe4551ad9fc6b65e50c5f5cc54097
* out/e14f_kills_iiib.json  16178e5e31d8b8d5d9c43a727674d1b3390bbccc30e1bbeff8455e454d979564
* out/e15_two_avoiders_p7k3.json  0e01fdda17b8b731a1f4b97ea88d44dba844f69b5d134d70baa0b9220a74c035
* out/e15b_4_10.json  c2043c7542dbcf8d37f2d085652de3b7367fe3687da0b374a643af199a02f30f
* out/e15b_4_11.json  538042bdae1c8be07c5f95dc0e0622c8ae2f90c765c94f2bef2cc2dd34983968
* out/e15b_4_12.json  09f100252be24de43c3c80f64a58b83123a170a99e9e5d4a938f7f9d0b948b1e
* out/e15b_4_13.json  e5832afb5f369b580fa5d2e55e35fb7c5b5c360f9d198f875b12ae57004e8ddf
* out/e15b_4_14.json  21725b2a7f95d2dba5cf551e04949182efca89a1d148cda2546e47fd6c8ea92c
* out/e15b_4_15.json  ff370b2f3a3c9e28196e0d5eba999fbedadb4ae74aa4e6edd31a59ab494f07e3
* out/e15b_4_9.json  fc5adafae6e89fd476e298b83af2c3347fe9b4b2b0923b4b2bc154ebbc570a2a
* out/e15b_5_11.json  93477cff776bccd52dc45264919bd8bacd7e9d751b40a2ae03a08d540cffc9f1
* out/e15b_5_12.json  3b6e7f8a1cbadf0943225ada7342fe49832781efb7e33c465e704e9be85c3f2d
* out/e15b_5_13.json  807c9d148e01380eb2bf89927fd7496acfd4a8b9b763aee86dbc1fc08ae59437
* out/e15b_6_13.json  f5aace4843aeea80a1a898b63baa0d2e9d6f892c7cd3fba29ff1d64bca96cdc1
* out/e15c_4_15.json  b0d8827ffc02ae759b97609b4783d192738e08d81650a99a302337776797ef2a
* out/e15c_5_14.json  a4d5cce959c1f388e51884dce01612e1dc3458f9cf464dbb11c0ee567f06ab36
* out/e15c_5_15.json  deae28f11d0021def913f2374607facd1e26b1d262c58c0cfb3f4269330d6e2b
* out/e15c_5_16.json  8482e760e1b8cc9561d0600d4d0dcb3f49ee2b2b98fe679bb2da892c003710a5
* out/e15c_5_17.json  31efcbf1635b2032fa720d0151429c3835e53cd1161b661f02b8d26181350d22
