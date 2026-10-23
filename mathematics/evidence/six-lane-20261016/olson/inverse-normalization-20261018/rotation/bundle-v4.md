# Rotation slice: final lane summary, bundle v4 (claims, hashes, UNKNOWNs, deviations, remaining obstruction)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T14:55:32-07:00.  Supersedes bundle-v3.md
(2ee8601c154ec4feaa628b17fa55cb2ffa2b301ef3c2ff3f604dfee412ca6785) as the summary; README.md stays the append-only log.
W = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/ (file names below are in W);
R = institute/runs/six-lane-2026-10-16/review/.  No claim of full ROT(p), INV*(p) or ordered Olson for D_(2p); no
novelty claim; no Lean / Comparator / human-review claim.  Every accepted item is read THROUGH its parent verdict's
mandatory overlay; the overlays are not restated here.

## 1. Parent-accepted results of this slice (text of record -> parent verdict)

| result | text of record (sha256) | parent verdict (sha256) |
|---|---|---|
| GRX, PM*, K1/K2, ROT-o2 | notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-ROT-lowodd-v1.md 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785 | R/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 |
| ROT-o3 (p >= 5), ROT-o4 (p >= 7) | proof-ROT-o3-v4.md 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf; proof-ROT-o4-v4.md 7fa49e970603210639f1a0b834c54f5418859bc3dfaf164e34e67836cdaa425a (wording errata of the accepted v3) | R/olson-rotation-o3o4-parent-verdict-v1.md 1225ce75847bfd748cacec51a5f0d41e1e686606b03b4b06a3c35112db34547f |
| C5: ROT-o4 at p = 5 (finite exact, computer-assisted) | p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588; proof-ROT-o4-p5-finite-v3.md 3a2acf7bd7edae272410f3a7816a0c7b49ba596519fda1ada5465c07a6a0e5c9 | R/olson-rotation-p5o4-parent-verdict-v1.md 92d35e67b811ffefdb6eb802fb428cf1e098f20ffe87b0aa12205fb0f5d78db0 |
| p = 5 few lift (o_F <= 4 or 5 o_F <= 2p + 4) | proof-FEW-p5-lift-v3.md aa2fb35092e8eb7621772428925898f5f000584cd9ff069004afc8e353bcb9cb | R/olson-p5-few-lift-parent-verdict-v1.md c2d06e1478f9aae7354505c81dae3fc7a782c4591a41c3bc288d380d85136d7b |
| INV*-FEW, OLSON-FEW (a); SHgen; ROT-FEW, MULT; SHgen-E, ROT-FEW-E; (b) | proof-INVstar-few-v3.md 779218b4a92c29c996172c361052d2ac9c16cbca003f49921af3713b3ca05531; proof-OLSON-few-v3.md ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a; proof-SHgen-v3.md fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e; proof-ROT-few-v4.md abd3973cd606fe3acc4d534edba13c45e8bbd3764129eaf1f5ca8c7993b7b521; proof-ROT-few-E-v4.md ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R/olson-fewodd-parent-verdict-v1.md 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8; addendum-1 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a |
| ZS, ROT/INV*/OLSON-HALF | proof-ROT-half-v1.md 3b8fa50e7a15eb58d215568407238e31d78468562be198035d6bf2d00641c738 | R/olson-half-range-parent-verdict-v1.md b3afb0016e4788209a77c25274f40f6d48edd99136bdade6b1388268d4951c3b |
| generalized ZS, ROT/INV*/OLSON-ZS | proof-ROT-half-v2.md 7403098f15cbb8b7954364a874cc58646d2a91bf11f3e29fee969c5f7c3748eb | R/olson-zs-v2-parent-verdict-v1.md 2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734 |
| ZX, S1 (a)-(c), S1+, terminal ROT-ZX, uniform ZX+ | proof-ROT-ZX-v1.md ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b; proof-ROT-ZX-addendum-S1c-v1.md 7ce7102c3db86c09e6662b353e542e56f104a097442440ebc9ea5e22c012b0b6; notes-ZX-deps-v1.md f98eb3ebe65cdb36419d002c1eecbb430dd96406993df280f88c9d0a9ba92b33 | R/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af |
| S1 (d), S1++, ZX++ (p >= 11) | proof-ROT-ZX-addendum-S1d-v1.md aefcfc58edfd878b8417d96f278406aedac99bd453c0553fb6979f838d3ac61b | R/olson-s1d-parent-verdict-v1.md 9f712b5247271adc40374df4bcc19f6c07ce90052c78255f09e427f13280ce2b |
| S1 (g) v2: (ZP) => (S1) for 0 <= kappa <= (p + delta*)/2 | proof-ROT-ZX-addendum-S1g-v2.md cbbbfecc2de710ca0fda22301a575f7586a13246f356f462c3dd40e10731b31c | R/olson-s1g-parent-verdict-v1.md cc9e27fbabdd14e8cc35e9d6d1477ea1ca90742a985629d8a362c89505b3605e |
| SC0, ZX-SC, ROT/INV*/OLSON-ZX-SC | proof-ROT-ZXSC-v1.md 15958303cffafae29f656f9ab0db0f26df9872415396d19097c07310b92dbb1a | R/olson-zxsc-parent-verdict-v1.md cf039654d40ae568ebe6de27eae62b610dd6be14dd2113e4b3939b0e00f1b134 |
| KETA, PAIR1, ROT-K01, INV*-K01, OLSON-K01 | proof-ROT-K01-v1.md b3ecdb4e09d2eae964322b96e0cddb3c48c91bcea258bebbd4324d16c59eb378 | R/olson-k01-parent-verdict-v1.md e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 |
| ROT-KP (k = p, kappa^ in {0,1}), INV*-KP, OLSON-KP | proof-ROT-KP-v1.md 472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e | R/olson-rotkp-parent-verdict-v1.md dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3 |
| index-one primary statement (import record) | - | R/olson-index-one-primary-statement-parent-v1.md e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 |

Accepted uniform conclusions (INV* for avoiders of length 4p - 2 and an increasing-order identity 2p-subword for words
of length 4p - 1), as a union of sufficient conditions, every prime p >= 5:
- o_F <= max(4, (p + 3)/2), every F;
- 3 o_F <= 2p + 1 and [o_F <= (p + delta* + 2)/2 or F >= o_F + p - delta* - 2] (S1 (g)); for 5 <= p <= 29 this is every
  F whenever 3 o_F <= 2p + 1; at p = 31 the only gap there is (o_F, F) = (21, 41) (terminal (21, 20));
- o_F <= p and F - o_F >= 2p - 4 (K01 for o_F <= p - 1, ROT-KP for o_F = p; subsumes ZX-SC).
Restricted REFL (o_F <= p) supplies the reflection half throughout.

## 2. Candidates and notes (NOT premises unless a parent verdict says so)

| file | sha256 | status at writing |
|---|---|---|
| proof-ROT-ZR-v1.md | e8903ff49f22c74ad8253599701a11f7d0af7efb63c7e9dc02cbcde4a77669a7 | UNDER REVIEW: Codex ACCEPT on all 8 items, 0 findings; Claude review running; not a premise. Claims: Theorem ROT-ZR; ROT-ZR2 (kappa^ = 2, 3 <= k <= p - 1, p >= 7); ROT-ZR3 (kappa^ = 3, p >= 17; p = 11, 13 for k <= 8, 11); uniform o_F <= p - 1 with F - o_F >= 2p - 6 (p >= 7), 2p - 8 (p >= 17) |
| proof-ROT-ZR-addendum-plus-v1.md | 88eecd13a9f7aa411701460565d1181a8b9511b97a629a4e4692bc947b3d55e5 | PARKED: written 14:44:56 before the parent's "no third candidate" message arrived; not submitted |
| notes-coverage-union-v1.md | e45f8320ec47d0b9aac547fc16a749e7dd45906df23a405a3b6f6d8fa94826af | planning aid only (parent): exact (p, o_F, F) table for 5 <= p <= 31 assuming ROT-ZR is accepted |
| proof-ROT-K0-v1.md / proof-ROT-K0-v2.md | 5be6b45d18261adfd856a58b0ed80d2b673f5f79d9aad75edaee655f78184c4a / 4e7ae21cea295228a5fbee27fcb37ccb57df630be353bcc7b6bb3fcbf906da57 | not reviewed; superseded in content by the accepted K01 (parent: not a premise); v1 carries a hash typo and was never sent |
| proof-ROT-ZX-addendum-S1e-v1.md | ec9fe140647bf375fc13bd8ae156ae0b9a19276f5ed3fc4af1b598d76a27a330 | unreviewed; not cited (S1 (g) verdict overlay 2) |
| proof-ROT-ZX-addendum-S1g-v1.md | 4c45d7047412fdbc569a5aa628a9ff6d574863de7edf2d461b0a4db68d27d415 | superseded by the accepted v2; unreviewed |
| notes-ZX-residual-v1.md / v2 / v3 | fdb5ad4a499377a298aa2d8f0e6f6638d0874a1baad50325426d204021d8ee98 / 4cd9175889e3e1d85b77be80e33bad3f4d94ca0bfa49e749e3a9baa92754e19c / e69a0acc2c0817a0e684a6261edbef79a7d03e42f02b8b9329cd04077a2b03c3 | unreviewed notes (v2 never sent: hash typo; v3 its erratum) |
| addendum-timestamps-v4.md | 55f43d3e3b557ae055bc23b1feb5e0f947adec3549a997fe9aef9cec3498925a | every approximate time label after 06:37:56: timestamps UNAVAILABLE |
| earlier notes and superseded versions | see bundle-v3.md and addendum-timestamps-v1..v3 | statuses as recorded there (e.g. S(p) notes: partial, OPEN) |

## 3. Finite aids and UNKNOWNs (aids only; never premises)

- zs-check-v1: PLAN 55d82db104cc400e521450cdb6a43941895a7649a292b4c0cf115076e7df8ed3, code
  d9d0e0737009f42bf42e25e0d9f86936cf68a74182126cb626bb62ba5af66818, out/run1.jsonl
  bb8ddafb418a4ea62d4907cff98c13483ff0ff0854a3f1d01f7dcd9e6b7b9b1a: aid PASS (deviation: ulimit -t 3000).
- zx-check-v1: PLAN 4791686d2c053b89262551e8c2dc18c91369b56a8c8a88185e03f1578e4a3361, EXPECTED
  dca5b5b55ac6af62359863f7fe18cd1b7457de5a048187fd4fd86367eba5720b, code
  2988e18051eb05bbcdb6d5d8343c1190f4cc3b8fdd487ee33c792aa09e992f8d, out/run1.jsonl
  cf8f4dec4a88807b5dc8eb3d9a500efd54933b9ef4491b5d70eca9953c739f95: 75/78 PASS; (17,11,9) UNKNOWN; (17,10,9) and
  (17,11,10) NOT_STARTED; stopped 12:38:08 by owned SIGTERM (exit 143): STOP-RECEIPT-v1.md
  a8ab8e2f18146f834e10fef3df2ace245e0bcc75c4c6e9c3a538b7cddb39c72d; DEVIATION-v1.md
  30e70dd874f09352190a1e7720296a9487c1b7b5cc99d7990a3943bed8e4d63b (ulimit -t 9300 backstop).
- t-search-v1: UNKNOWN by parent ruling (admission used a wrong rule; the frozen 300 s rule failed: drop 6.49e9 >
  allowed 2.44e9): ADMISSION-AUDIT-RECEIPT-v1.md 49066bc952da5079ce2ebe234fa1346f314cfdd02e8d7c5ffd58df9a5095eb07;
  out/run1.jsonl e79de63132ab3d23b510b1c45f788da96a97e36b13287494193b02bd870d2780.  Not evidence either way.
- t-search-v2: PARTIAL/UNKNOWN as a whole by parent ruling.  Child exit 0 at 14:14:19 after its 3600 s self-budget
  (DONE_PARTIAL); nine complete item records (controls as expected; COVERED (29,18) (31,19) (37,22) found 0; BEYOND
  (31,20) (37,23) (37,24) found 0) are exploratory at their timestamps, not premises; (41,25) budget-stopped; (41,26)
  (43,27) (43,28) unstarted.  Parent-monitor floor breach 11,985,104,896 at 14:07:50 (inside (41,25)) escaped the 20 s
  guard: resource exception, no causal attribution.  END-RECEIPT-v1.md
  9323e19733b31b4174ca4c67bc0b8d136715b97a46f8cb0637b91f3c9c34c0ac; out/run1.jsonl
  ae12553b43e7ca4a2e76fde90533030f4dd96db90ecff3f73ff6fc42d1d2100e; out/wrapper-run1.log
  fa918f6100ba8af5e940f990ed05d044ac9d8d2eb675902e6473654d8f317be6; gate_v1.sh
  ba112eca261da2e656f6429079454aca2dc56f6876fb72de82de2eb41e07bf81; PLAN-v1.md
  2a7fd4628c7e0e541c95b2b8e1695625d8dc9fdbdf0043f3bfadeed754ba2b96; EXPECTED-v1.json
  48419050a767de7f3441f32af9b364de67403d02fdde60385199e8fa5c5b47ef.
- No native process of this slice is running at writing.

## 4. Deviations and labels (all disclosed in README.md)

1. ulimit -t CPU backstops in zs-check-v1 (3000 s), zx-check-v1 (9300 s) and earlier runs (DEVIATION-v1.md).
2. t-search-v1 admitted under a wrong stability rule (UNKNOWN).
3. t-search-v2 wrapper limits (parent-noted): the wrapper always exits 0; an empty ps RSS reading would have been
   skipped (none occurred); the 20 s cadence missed the 14:07:50 floor breach; gate_v1.sh's comment "13:17 PDT" is an
   estimated label (actual launch 13:14:14).
4. Approximate or bounded time labels: addendum-timestamps-v1..v4 (v4 covers README lines 286-747, the K0 v2 header
   "13:37:3x", the S1 (g) v2 header "after 13:03:20" (actual 13:03:27)); README label "14:3x" (actual 14:19:46) and
   "14:55" (actual 14:54:56) corrected by later entries.
5. A README entry falsely said the K0 v1 hash typo had been corrected (the edit had failed); corrected by a later
   entry; K0 v2 is the erratum.
6. Pre-hash edits of freshly created, not yet hashed or sent files (K0 v1, ROT-KP v1, ROT-ZR v1), each disclosed.
7. proof-ROT-ZR-addendum-plus-v1.md written before the parent's "no third candidate" message was received; parked.

## 5. Exact remaining obstruction (rotation half, o_F <= p)

Accepted terminal coverage: every admissible normal-form pair (k, kappa^) with k = 1 (K1); kappa^ <= 1 and
2 <= k <= p (K01, ROT-KP); 3k <= 2p + 1 and kappa^ <= (p + delta*)/2 (ZX with S1 (g); for p <= 29 every occurring pair
with 3k <= 2p + 1).  Hence a counterexample to the rotation half with o_F <= p is an avoider w of length 4p - 2 such that
EVERY admissible normal form has terminal (k, kappa^) in
- (Q1) kappa^ >= 2 and (2p + 1)/3 < k <= p, or
- (Q2) 3k <= 2p + 1 and kappa^ > (p + delta*)/2 (only for p >= 31; first pair (21, 20) at p = 31),
and whose rotation letters do not lie in one {rho_c, rho_-c}.  If ROT-ZR is accepted, (Q1) shrinks to k = p with
kappa^ >= 2, plus the pairs with k <= p - 1 failing (Lambda), (H') or (K') (smallest cases: p = 7 (6, >= 3); p = 11 (8,
>= 4), (9, >= 3), (10, >= 3); table in notes-coverage-union-v1.md).

What fails at sequence level (Y = rotation sequence of the normal form, with (ZP) at kappa^):
- (Q1) with k <= p - 1: for a longest zero-sum Z and the SC0 generator g of Y - Z, every z in Z is g or -s g,
  s <= min(|Z| - 1, slack) (Lemma ZSTRUCT, under review).  Not excluded: the negatives' s-sum exceeding n+ by a positive
  multiple of 2p outside (Lambda), and E(Y) above SHgen's accepted (H)/(K) thresholds when only E <= k - 1 + G(kappa^)
  is known.  No example of either is known to me; no claim either way.
- (Q1) with k = p and kappa^ >= 2: a longest zero-sum of length exactly 2 kappa^ leaves a zero-sum-free complement of
  length p, outside SC0 (length >= p + 1); the length-p question S(p) is open (notes-SC-lengthp-v2.md), and the
  ROT-KP arc argument needs distinct block values, which (ARC) with m = 0 forces only at kappa^ = 0.
- (Q2): (S1) may fail; by the accepted Lemma S1 (b) the rotation sequence then contains two disjoint minimal zero-sums
  P, P' with 2p - 2 kappa^ + 2 <= |P|, |P'| <= 2 kappa^ and |P| + |P'| >= 2p + 2.
- o_F > p: needs REFL beyond restricted REFL (reflection slice), not this slice.
The k = p sequence obstructions Y(0) Y(c)^(p-1) (kappa^ = 0) and Y(0)^3 Y(c)^(p-1) (kappa^ = 1) are excluded at word
level by the accepted ROT-KP; they remain valid sequences.  No sequence example refutes ordered Olson.
