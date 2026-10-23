# Reflection slice (REFL(p) for rigid rotations): results, exact scope, open residual

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T03:45:41-0700.  Frozen target: README.md (af55df78...d63b).
REFL(p): every avoider of length 4p - 2 over D_(2p) whose rotations lie in one {rho_x, rho_-x}, x != 0, has every maximal cyclic
reflection run constant.  This is half (b) of INV*(p); it says nothing about rotation values, proves neither INV*(p) nor ordered
Olson, and a REFL counterexample (length 4p - 2) would not refute ordered Olson (length 4p - 1).  No novelty/priority claim.

## 1. Results (labels: [W] written proof; review status as recorded)

* Theorem K0* (proof-K0star-r2.md, 6681676e...96e1; r1 99a8f2e0...9488 kept): for EVERY prime p >= 5, REFL(p) holds for avoiders
  with kappa = p - 1 - H = 0 (H = sum of floor(l/2) over maximal constant reflection blocks).  Unconditional: uses only Theorem P,
  Davenport-alpha, EGZ / Lemma AR, GR0 (= accepted GRX) and new elementary lemmas: segment-spectrum dominance (SPEC, FUS, SL),
  pair transfer (TR), merge (PM0 = accepted PM*), and the block chain BC' with the GENUINENESS BOOST (an empty run between
  different reflection values has u_t != 0, which lifts lambda from 0 to 1; without it the partition sums are exactly p).
  Codex hostile review of r1: ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 3 MINOR on this file (R/olson-reflection-reduction-codex-v1.note.md
  311bdacc...a8b); all three applied in r2.  Claude review pending; no parent verdict yet.
* Theorem RED (proof-RED-r2.md, c4e7697f...d3d7; r1 fa6c5054...bb3 kept): conditional on the parent-accepted RGR results
  (I1) Cor. B', (I2) the B = 0 chain (OR, C0-B', A1, cut), (I3) K0 (+ branch C2), (I4) KB, KBH:
      REFL(p)  <=>  no avoider in RES_<(p) with kappa >= 2,
  RES_<(p) = words with >= 1 empty run, all maximal constant blocks odd, every rotation run pure (only rho_1 or only rho_-1) or
  empty, normalised A >= B and B < kappa.  Proved inside for all p: B = kappa excluded for all-odd words (KB*, CAP, KBH*), kappa = 1
  excluded (K1*), every "last fusion" exit closed (SING, TII, QQ).  Codex: ACCEPT-WITH-FIXES, 2 MINOR on this file, applied in r2.
* Tools (notes-RES-tools-r1.md, 734fdc8f...76a3): RPT (reflection-pair transfer, exact), SHIFT (an empty run shifts u_P inside
  the same window for every pattern touching it from one side), CON (an empty run with theta = +-2 next to a matching rotation
  contracts to rotations), FW-G, EVEN (all reflection runs even => solvable, any letters), and Theorem RED+ (residual may assume no
  CON+ move applies).
* Partial attack on RES_< with B = 0, k <= p, R <= 2p - 2 (notes-RES-B0-r1.md, 1942d3ec...5a89): Steps 0-1 of Proposition S1'
  extend to empty runs and giant runs (all eight min-cases); Step 2 fails exactly when Phi(Z) < 2 kappa + 2, which needs empty
  defects.  Correction to its Sec. 2 wording: the failing case forces |Z| <= kappa - m_Z, s := sum over non-defects of (bh_t - 1)
  <= 1 + g_Z - 2 m_Z and g_Z >= 2 m_Z + g_Y - 1 (not literally "every non-defect has bh_t = 1").

## 2. Exact open statement (obstruction)

REFL-RES(p): no word of RES_<(p) with kappa >= 2 avoids (proof-RED-r2.md Sec. 6, F1-F3; notes-RES-tools-r1.md Sec. 3).  It is the
G-word analogue of MIX_DEF (B >= 1) and of C0-B'/S1' (B = 0): single-window and interval certificates provably do not suffice
(E6), and the RGR lift/defect proofs use r_t >= 1 at named places.  Finite status: p = 5 empty (exhaustive D10); p = 7, k <= 9 inside
the old NF search (unreviewed code); k >= 10 at p = 7 and all p >= 11 not decided.

## 3. Finite aids (raw DP = arbiter; none is a premise)

E0 controls (out/e0_controls.json), E1 moves (out/e1_moves.json), E2 K0* replay (out/e2_k0star_replay.json), E2c all C1/C2
un-fusings of all RGR avoiders p = 5 (210) and p = 7 (3,738): 503,696 words, 0 avoiders (out/e2c_unfuse_p{5,7}.jsonl,
out/e2c_crosscheck.json), E5 lemma replays (out/e5_red_replay.json), E6 interval probe (plan-E6.md; out/e6_interval_probe.json:
442 strata, 5,971 DP decisions, 0 candidates, positive control found the sharpness avoider), E7 failing-lift family (plan-E7.md;
out/e7_failing_lifts.json: 1,200 words p = 11..19, all solvable).  Details and per-file hashes: checkpoint-01.md and below.

## 4. Resource and safety record

One busy process at a time; every native/python run under ulimit -t with a fresh statvfs gate (free space 15.0e9 -> 13.19e9 B over
the session, mostly other agents; this directory uses 0.5 MB); TMPDIR = reflection/tmp (empty); python3 -B; no model CLI, network,
Git, /tmp, global config, deletion or overwrite (all files exclusive-create; r1 files kept).  No native child under an eval
deadline; no kill signal used.  Eval-kernel explorations (run-data counts, interval-DFS prototype, QQ arithmetic, killing-pattern
listing) are aids only and were not used as premises.

## 5. File hashes (sha256) at 03:45:41 PDT

README.md af55df78f0a30126ef1dafefde651c2818da4bed72efb00b7f9cddd83a35d63b
checkpoint-01.md 8e9700236e15f6d3458ba4ecb7881f5c5bfee846f41864635867b698063db4d3
proof-K0star-r1.md 99a8f2e0403877bb571b66134be3889e9d606d4da16c9040b6bf0407edb69488
proof-K0star-r2.md 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1
proof-RED-r1.md fa6c5054fc3d47862c8f8e668389b44200d4509b3fe2827141b19c4033b05bb3
proof-RED-r2.md c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7
notes-RES-tools-r1.md 734fdc8ff7dd3c33777070723eadfac32c56106bc147ffce2facb8eeaa4576a3
notes-RES-B0-r1.md 1942d3ec25d31ed0a387112172af94b86f2c8ae837d931a2b59ee2cea9ea5a89
plan-E6.md 9dd30dacbea6ba84798b67897b805665331e2854b8bed5226019affd0b94c8cb
plan-E7.md 0dcfd3716b6f5b130b80a35921270b14ae0155ca06bef8f4dc1e3e53993c1b86
code/dp.py fece1a8fea9fcbb5c340c02740c2a2334a6f9d1a53a039e62cc5ab2b992a555c
code/gwin.py c1a4d08baaa9b1161f7d9efdb831e7904401bdc5e1138d1d9ef59d7edb0365a0
code/e0_controls.py 0bc6edc07275e8a1809afa0ab1901a3d6df58fe8d542ff182883fbadcc04212a
code/e1_moves.py 19d00144c47b72caa1085fc55c770b21c11bf041799c3e8a8dc836231828c938
code/e2_k0star_replay.py 24066a63c30fb353b654e55d2dd189fdd3a2f064924cdfa014a6b1e408728f7b
code/e2c_prep.py 2ad9d1e23165b7e7e5114b93f7b8bc186287178932b1cc1a9c180ce1f93efdfa
code/e2c_unfuse.cpp 18bc170d68131341d5f8b6b3350bd78d28bac9dbadd61f31c52f1f639f8a260e
code/e2c_unfuse 3626178dd7b30d79a12b3202ab97bb6d27ae4f6b658cb0da0de2b8f4ab28ebba
code/e2c_crosscheck.py 7fda4e9c106fdd2efdd3e7ab79bcc8155a5ce36029a4570d6ead4c054b13be51
code/e5_red_replay.py dc6871ffe75a418315cd87813f7002a8445f967bd8c91ec5a8f9c93c60e7812d
code/e6_interval_probe.py b6a3400a4bff4f06ca780980d6151de11d2543fb3624cfea6748698ee36f59ad
code/e7_failing_lifts.py 07b0d59fa1347bc529b639d73c7756670d20f744b0f26f3910be0bd504dd8ee2
out/e0_controls.json 6c7c1c47d20abcd2cb42e8701fbf73cf996eb3add88deca019b12c4f2fbe08c5
out/e1_moves.json 0787e9617816c63db4819124aafef1fb7985244ba80cff7f8e570e11ad40fb91
out/e2_k0star_replay.json 04071de30e69f63a7579a2e435594a4d49d172f731378e249c5c6aab9929cc42
out/e2c_input_p5.txt b31ce035fdb5f1b84c08093729adceb4f27f6867bed1163ed9e0eba5dad096da
out/e2c_input_p7.txt f5ab35b4365d4c13bf1a653d79a3e599d287d216d09b430bc57ce97dd6fcd8b1
out/e2c_unfuse_p5.jsonl bd6a8346d475398ae6e081119c426a32dd0736c6f70a089183bf65152f1aa713
out/e2c_unfuse_p7.jsonl ccccbe176aaf0557545ac1724120e1242649fa6b2d36b794a86ef18cca8c694d
out/e2c_crosscheck.json 1a82772f11616e883ca54f66771eec89e500f3bafd51b3128f0036245f0a5023
out/e5_red_replay.json 0007b9a1c1285679b377255362153a447b24d7f8943ca0961e2309757f1226b9
out/e6_interval_probe.json 985d11c054025d48af8c1a0a2b0ad286db46e5da9dc38f09e4c12ba9cbc86e1f
out/e7_failing_lifts.json f8d925027ba3ebc1ba08e3fa8f6907a0344451e1460737c37d0616ad67605005
Read-only inputs: olson/evidence/was/p5_N18_all.jsonl 2ab5c79a...897b, p7_N26_all.jsonl 231617f9...1571;
c2/invstar/out/gwas_p5_N17.txt 81389b5c...308d (cited only); olson/code/was_verify.py (imported read-only in E0).
