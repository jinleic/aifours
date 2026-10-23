# Checkpoint 001: inputs, inherited STOP registry, frozen dependency/gap map, target selection

Owner ContinueOlson (lane math-2, NEW path /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson).  Written after /bin/date 2026-10-18T23:22:42-0700.
Declared parent identity per parent IRC: openai-codex/gpt-6-astra (no runtime receipt).  This worker: Claude (session
model identity as configured by the harness; no CLI review run yet).  Nothing here is a proof claim.

## 1. Inputs read (sha256 observed at 2026-10-18T23:2x; every load-bearing hash below matches its controlling record)

- pinned bundle: six-lane-20261016/olson/inverse-normalization-20261018/rotation/bundle-v5.md
  2584bd8c3aacf729b8f67a5cfae49dd04548e43b6e5fe5745bc1838e2f8a210e (= manifest pin); final-report-v7.md
  420a3140150930ba91f95167647ddfdeb27811d223960e0449be32a077209dc5 (= manifest pin).
- parent verdicts (old run review/): ROT-KP dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3;
  ROT-ZR 6d8bb6c94f6263834c39130c6d39a2ab54e557740eb45f904732664e879dde73; S1(g)
  cc9e27fbabdd14e8cc35e9d6d1477ea1ca90742a985629d8a362c89505b3605e; ZX/S1(c)
  2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; RUNS
  82adbdddd87dff5af0ef8e0e1ceb82b2a20257213966ae45789811a91a859237; REFL-few-odd
  16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca; REFL-B0
  7f1041bd07d3fe66581ad67752dea9385bd3510975a5661f060c8fe38cc35ddb; EDGE
  d2b67d96ee697da6536c443354a2ea9f6a7bb32851ecd07fff9050c2fd40b58b (observed; no controlling pin seen); index-one import
  e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6.
- texts: S1(g) v2 cbbbfecc2de710ca0fda22301a575f7586a13246f356f462c3dd40e10731b31c; ROT-KP v1
  472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e; ROT-ZR v1
  e8903ff49f22c74ad8253599701a11f7d0af7efb63c7e9dc02cbcde4a77669a7; ZX v1
  ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b; GRX
  afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-DR.md
  dbaa48bbd96e6d0e9c21e2a01cb5f1dbb78e5cdead550157113bd2a7cb84308d; repr-WAS.md
  87d7cade40e69c11e11200ae4034c0265c98d0618f715c67fccb43b43c1f6806; notes-SC-lengthp-v2
  0c991ac3a1e7c4ab0e3be81433ca5a3a39e52efcda8d1cc9bb016778c9f1eadf; notes-SC-lengthp-addendum-v2
  dbf768c5be7d764d3028f02261ee26c4776a4a4ae7bce3641ecaf3b063232080.

## 2. Inherited STOP/UNKNOWN registry (Olson; all closed-round; none restarted; markers untouched)

- rotation/zx-check-v1/STOP-RECEIPT-v1.md a8ab8e2f18146f834e10fef3df2ace245e0bcc75c4c6e9c3a538b7cddb39c72d: owned SIGTERM
  (parent decision); (17,11,9) UNKNOWN, (17,10,9)/(17,11,10) NOT_STARTED.  Finite aid only.
- t-search-v1 UNKNOWN (wrong admission rule); t-search-v2 PARTIAL/UNKNOWN (wrapper defects, floor breach).  Aids only.
- S(7,25,7) SIGXCPU UNKNOWN; reflection cell (6,19) SIGXCPU (prior ulimit violations).  UNKNOWN, no proof weight.
- Classification: all are closed-round resource/process stops, not open correctness defects of accepted texts.  This
  lane plans no replay of any of them; any future native item will cite this registry and a parent GO.

## 3. Frozen dependency/gap map (accepted scopes only; bundle-v5 Sec. 1, 5 and the verdicts above)

Target chain: INV*(p) [every length-(4p-2) avoider is RGR: rotations in one {rho_x, rho_-x}, x != 0, and every maximal
cyclic reflection run constant] + RGR-LONG(p) [RUNS verdict] => ordered Olson for D_2p (DR' deletion argument).  INV* =
ROT half (rotations, read on any admissible all-odd normal form w^ with terminal k blocks, kappa^ = p-1-(F-k)/2) + REFL
half (accepted only for o_F <= p, plus the B = 0 numeric range REFL-B0/EDGE).
Accepted ROT terminal criteria: T1 k = 1; T2 2 <= k <= p, kappa^ <= 1 (K01, ROT-KP); T3 3k <= 2p+1 and kappa^ <=
(p+delta*)/2 (ZX + S1(g)+); T4 ROT-ZR (p >= 7, k <= p-1, kappa^ <= (p-1)/2, Lambda/H'/K').
Residual (necessary conditions relative to T1-T4): Q1a k = p, kappa^ >= 2; Q1b (2p+1)/3 < k <= p-1, kappa^ >= 2, T4
fails; Q2 3k <= 2p+1, kappa^ > (p+delta*)/2 (empty p <= 29; p = 31 only (21,20)); REFL for o_F > p (all regimes
except REFL-B0/EDGE cells).  Separate and untouched: all non-dihedral groups.
Interfaces I will rely on, with their accepted scope: ZX terminal criterion needs ONLY 3k <= 2p+1 and (S1) at
kappa^ (proof-ROT-ZX-v1 L204-206, ZX verdict); uniform consequences via restricted REFL (o <= (2p+1)/3 <= p) and the
ordered deletion ledger (Cases 1-3 preserve 3o <= 2p+1) and RGR-LONG, exactly as in the S1(g) verdict.

## 4. Target selection (frozen for the first work block)

PRIMARY: Lemma S1-full.  For every prime p >= 5 and integer kappa >= 0 with 3kappa <= 2p - 2: every sequence Y of odd
elements of Z_2p with no zero-sum subsequence of length in [2kappa+2, 2p] has every zero-sum subsequence of length
<= 2kappa.  Planned consequence (bridge above): INV* and ordered Olson for D_2p for EVERY word with 3o_F <= 2p+1, every
prime p >= 5; Q2 empty for all p.  Rationale: (a) Q2 is the only residual family whose obstruction is purely sequence-
level (T3's word step is accepted for all 3k <= 2p+1); (b) the S1(g) verdict localizes the gap: its (P1) p >= 3delta+4
is EXACTLY 3kappa <= 2p-2 (kappa = (p+delta)/2), while (P2) enters only Step (6c) and (P3) only Step (8); (c) sharpness
control exists: the parent-checked family g^(p+3)(3g)^(p-1) satisfies (ZP) and violates (S1) for every kappa >=
ceil((2p+1)/3); for p = 1 mod 3 the needed kappa = (2p-2)/3 is the last value before that failure, so any proof must be
sharp there.  This closes one of three ROT residual families uniformly in p; it is NOT unrestricted INV*.
SECONDARY (written exploration, no claim): Q1a k = p, 2 <= kappa^.  Own derivation (unreviewed): w^ avoids iff its
cyclic reduced word (one sigma_(y_j) per odd block, all rotations) of length 2p + 2kappa^ has no identity subword of
even length in [2kappa^+2, 2p].  Finite aid (repr-WAS 4.3, p = 5, 7 RGR census, not a premise): RGR avoiders with k = p
have kappa = 0 or kappa >= (p+1)/2.
Not selected now: REFL o_F > p and Q1b (no localized obstruction identified in reading).

## 5. Actual result / blocker / next action

Result: reading complete for the named inputs; map and target frozen above.  Blocker: S1(g) Steps (6c), (8) fail
without (P2), (P3); first open instance p = 31, delta = 9 (kappa = 20).  Next bounded action: written replacement of
Steps (6c) and (8) under (P1) alone; then freeze a <=300 s stdlib falsification-probe plan (sharp-family control plus
exhaustive small-p checks) for parent-visible admission before any execution.  Source limits: Savchev-Chen/Yuan proofs
not read (import record only); no literature search yet; a search miss will never be used as novelty evidence.
