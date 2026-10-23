# Checkpoint 01 (host clock 2026-10-18T03:14 PDT)

Written results ([W], unreviewed):
* proof-K0star-r1.md: Theorem K0* -- for every prime p >= 5, an avoider of length 4p - 2 with rotations in one {rho_x, rho_-x} and
  kappa = p - 1 - H = 0 has every maximal cyclic reflection run constant.  Unconditional (Theorem P, Davenport-alpha, EGZ/AR and
  elementary lemmas; no RGR theorem imported).  Its Lemma GR0 / PM0 are now covered by the parent-accepted GRX / PM*
  (R/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac...).
* proof-RED-r1.md: Theorem RED -- conditional on the parent-accepted RGR results (I1)-(I4) (Cor. B', the B = 0 chain, K0, KB/KBH):
  REFL(p) <=> no avoider in RES_<(p) with kappa >= 2 (all maximal blocks odd, rotation runs pure or empty, >= 1 empty run,
  0 <= B < kappa).  New sub-results for all p: KB*, CAP, KBH* (B = kappa excluded for all-odd G-words), K1* (kappa = 1),
  Lemma SING, TII, QQ (every last-FUS exit closed).
* Erratum noted for a later revision of proof-RED-r1.md Sec. 6 (F3): removing one reflection pair needs H >= 1 (kappa <= p - 2).

Finite aids (raw DP is the arbiter everywhere):
* E0 controls: sharpness family avoids at 4p - 3 (p = 5, 7, 11, 13; v = 0, 1, p - 1), its 3 extensions solvable (explicit index
  sets re-multiplied), rho_1^(2p-1) sigma_0^(2p-1) avoids, FILL example (README Sec. 3) avoids and its fillings are solvable;
  dp1 = dp2 = was_verify on 3,000 random words; GR0 = DP on 1,500, H0 = DP on 738 G-words (0 mismatches; few NO instances).
* E1: SL 405 spectrum equalities, FUS 540 inclusions, all 495 one-letter slides and 324 odd-FUS mutations detected;
  TR / PM0 / FUS transfers on 1,474 / 4,931 / 3,248 explicit words: 0 violations.
* E2: K0* Step 5 certificates on 1,950 configurations p = 5..31: all hold with sum exactly p + 1; without the boost (a) fails in
  all 1,170 C1a/C2a cases; 900 raw-DP solvable; 56,168 GR0-vs-H0 interval checks, 0 mismatches.
* E2c: every C1/C2 un-fusing of every RGR avoider in the read-only lists p5_N18_all (210) and p7_N26_all (3,738; sha 231617f9...):
  originals all avoid (positive control), 10,352 + 493,344 un-fused words, 0 avoiders (C++ DP; 7,194-sample Python DP agrees).
* E5: K1* 225, KB* 836, CAP 374, KBH* 444 certificate replays hold; 952 raw-DP solvable; TR 1,843 pairs (19 NO), 0 mismatches.

No model CLI, no /tmp, no Git, no deletion; every native run under ulimit -t with a fresh statvfs gate (last 13,395,820,544 B).

File hashes (sha256):
* README.md  af55df78f0a30126ef1dafefde651c2818da4bed72efb00b7f9cddd83a35d63b
* proof-K0star-r1.md  99a8f2e0403877bb571b66134be3889e9d606d4da16c9040b6bf0407edb69488
* proof-RED-r1.md  fa6c5054fc3d47862c8f8e668389b44200d4509b3fe2827141b19c4033b05bb3
* code/dp.py  fece1a8fea9fcbb5c340c02740c2a2334a6f9d1a53a039e62cc5ab2b992a555c
* code/gwin.py  c1a4d08baaa9b1161f7d9efdb831e7904401bdc5e1138d1d9ef59d7edb0365a0
* code/e0_controls.py  0bc6edc07275e8a1809afa0ab1901a3d6df58fe8d542ff182883fbadcc04212a
* code/e1_moves.py  19d00144c47b72caa1085fc55c770b21c11bf041799c3e8a8dc836231828c938
* code/e2_k0star_replay.py  24066a63c30fb353b654e55d2dd189fdd3a2f064924cdfa014a6b1e408728f7b
* code/e2c_prep.py  2ad9d1e23165b7e7e5114b93f7b8bc186287178932b1cc1a9c180ce1f93efdfa
* code/e2c_unfuse.cpp  18bc170d68131341d5f8b6b3350bd78d28bac9dbadd61f31c52f1f639f8a260e
* code/e2c_unfuse  3626178dd7b30d79a12b3202ab97bb6d27ae4f6b658cb0da0de2b8f4ab28ebba
* code/e2c_crosscheck.py  7fda4e9c106fdd2efdd3e7ab79bcc8155a5ce36029a4570d6ead4c054b13be51
* code/e5_red_replay.py  dc6871ffe75a418315cd87813f7002a8445f967bd8c91ec5a8f9c93c60e7812d
* out/e0_controls.json  6c7c1c47d20abcd2cb42e8701fbf73cf996eb3add88deca019b12c4f2fbe08c5
* out/e1_moves.json  0787e9617816c63db4819124aafef1fb7985244ba80cff7f8e570e11ad40fb91
* out/e2_k0star_replay.json  04071de30e69f63a7579a2e435594a4d49d172f731378e249c5c6aab9929cc42
* out/e2c_input_p5.txt  b31ce035fdb5f1b84c08093729adceb4f27f6867bed1163ed9e0eba5dad096da
* out/e2c_input_p7.txt  f5ab35b4365d4c13bf1a653d79a3e599d287d216d09b430bc57ce97dd6fcd8b1
* out/e2c_unfuse_p5.jsonl  bd6a8346d475398ae6e081119c426a32dd0736c6f70a089183bf65152f1aa713
* out/e2c_unfuse_p7.jsonl  ccccbe176aaf0557545ac1724120e1242649fa6b2d36b794a86ef18cca8c694d
* out/e2c_crosscheck.json  1a82772f11616e883ca54f66771eec89e500f3bafd51b3128f0036245f0a5023
* out/e5_red_replay.json  0007b9a1c1285679b377255362153a447b24d7f8943ca0961e2309757f1226b9
