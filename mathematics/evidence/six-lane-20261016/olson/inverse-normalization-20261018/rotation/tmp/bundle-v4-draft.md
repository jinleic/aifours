# Rotation slice: final lane summary, bundle v4 (claims, hashes, UNKNOWNs, deviations, parent overlays)

Owner OlsonRotationRigidity.  Written after host clock __CLOCK__.  Supersedes bundle-v3.md
(2ee8601c154ec4feaa628b17fa55cb2ffa2b301ef3c2ff3f604dfee412ca6785) as the summary; README.md stays the append-only log.
Paths: W = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/;
R = institute/runs/six-lane-2026-10-16/review/.  No claim of full ROT(p), INV*(p), or ordered Olson for D_(2p); no
novelty claim; no Lean / Comparator / human-review claim.  Every accepted item is read THROUGH its parent verdict's
mandatory overlay (not restated here).

## 1. Parent-accepted rotation-slice results (text of record -> verdict)

| result | text of record (sha256) | parent verdict (sha256) |
|---|---|---|
| GRX, PM*, K1/K2, ROT-o2 | notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-ROT-lowodd-v1.md | R/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 |
| ROT-o3, ROT-o4 (p >= 7) | proof-ROT-o3-v3/v4, proof-ROT-o4-v3/v4 (see verdict) | R/olson-rotation-o3o4-parent-verdict-v1.md 1225ce75847bfd748cacec51a5f0d41e1e686606b03b4b06a3c35112db34547f |
| ROT-o4 at p = 5 (finite exact, computer-assisted) | p5o4-v1/ packet | R/olson-rotation-p5o4-parent-verdict-v1.md 92d35e67b811ffefdb6eb802fb428cf1e098f20ffe87b0aa12205fb0f5d78db0 |
| p = 5 few lift | proof-FEW-p5-lift-v3.md | R/olson-p5-few-lift-parent-verdict-v1.md c2d06e1478f9aae7354505c81dae3fc7a782c4591a41c3bc288d380d85136d7b |
| INV*-FEW / OLSON-FEW (a); SHgen; ROT-FEW, MULT; (b) | proof-INVstar-few-v3, proof-OLSON-few-v3, proof-SHgen-v3 fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e, proof-ROT-few-v4 abd3973c... | R/olson-fewodd-parent-verdict-v1.md 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8 + addendum-1 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a |
| ZS, ROT/INV*/OLSON-HALF | proof-ROT-half-v1.md 3b8fa50e7a15eb58d215568407238e31d78468562be198035d6bf2d00641c738 | R/olson-half-range-parent-verdict-v1.md b3afb0016e4788209a77c25274f40f6d48edd99136bdade6b1388268d4951c3b |
| generalized ZS, ROT/INV*/OLSON-ZS | proof-ROT-half-v2.md 7403098f15cbb8b7954364a874cc58646d2a91bf11f3e29fee969c5f7c3748eb | R/olson-zs-v2-parent-verdict-v1.md 2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734 |
| ZX, S1 (a)-(c), S1+, terminal ROT-ZX, uniform ZX+ | proof-ROT-ZX-v1.md ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b; proof-ROT-ZX-addendum-S1c-v1.md 7ce7102c3db86c09e6662b353e542e56f104a097442440ebc9ea5e22c012b0b6; notes-ZX-deps-v1.md f98eb3ebe65cdb36419d002c1eecbb430dd96406993df280f88c9d0a9ba92b33 | R/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af |
| S1 (d), S1++, ZX++ (p >= 11) | proof-ROT-ZX-addendum-S1d-v1.md aefcfc58edfd878b8417d96f278406aedac99bd453c0553fb6979f838d3ac61b | R/olson-s1d-parent-verdict-v1.md 9f712b5247271adc40374df4bcc19f6c07ce90052c78255f09e427f13280ce2b |
| S1 (g) v2, (ZP) => (S1) for kappa <= (p + delta*)/2 | proof-ROT-ZX-addendum-S1g-v2.md cbbbfecc2de710ca0fda22301a575f7586a13246f356f462c3dd40e10731b31c | R/olson-s1g-parent-verdict-v1.md cc9e27fbabdd14e8cc35e9d6d1477ea1ca90742a985629d8a362c89505b3605e |
| SC0, ZX-SC, ROT/INV*/OLSON-ZX-SC | proof-ROT-ZXSC-v1.md 15958303cffafae29f656f9ab0db0f26df9872415396d19097c07310b92dbb1a | R/olson-zxsc-parent-verdict-v1.md cf039654d40ae568ebe6de27eae62b610dd6be14dd2113e4b3939b0e00f1b134 |
| KETA, PAIR1, ROT-K01, INV*-K01, OLSON-K01 | proof-ROT-K01-v1.md b3ecdb4e09d2eae964322b96e0cddb3c48c91bcea258bebbd4324d16c59eb378 | R/olson-k01-parent-verdict-v1.md e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 |
| index-one primary statement (import record) | - | R/olson-index-one-primary-statement-parent-v1.md e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 |

Accepted uniform conclusions (INV* at length 4p - 2 and increasing-order identity 2p-subword at length 4p - 1), union:
- o_F <= max(4, (p + 3)/2), every F (ZX + p = 5 finite); and 3o_F <= 2p + 1 with [o_F <= (p + delta* + 2)/2 or
  F >= o_F + p - delta* - 2] (S1 (g)); for 5 <= p <= 29 this is every F whenever 3o_F <= 2p + 1; first gap p = 31,
  terminal (21, 20), i.e. (o_F, F) = (21, 41).
- o_F <= p - 1 and F - o_F >= 2p - 4 (K01; subsumes ZX-SC).
- Restricted REFL (o_F <= p) is used for the reflection half throughout.

## 2. Candidates and notes (NOT premises unless a parent verdict says so)

__VERDICT_TABLE__

## 3. Finite aids and UNKNOWNs (aids only; never premises)

- zs-check-v1: PLAN 55d82db104cc400e521450cdb6a43941895a7649a292b4c0cf115076e7df8ed3, code d9d0e0737009f42bf42e25e0d9f86936cf68a74182126cb626bb62ba5af66818,
  out/run1.jsonl bb8ddafb418a4ea62d4907cff98c13483ff0ff0854a3f1d01f7dcd9e6b7b9b1a: aid PASS (deviation: ulimit -t 3000).
- zx-check-v1: PLAN 4791686d2c053b89262551e8c2dc18c91369b56a8c8a88185e03f1578e4a3361, EXPECTED
  dca5b5b55ac6af62359863f7fe18cd1b7457de5a048187fd4fd86367eba5720b, code 2988e18051eb05bbcdb6d5d8343c1190f4cc3b8fdd487ee33c792aa09e992f8d,
  out/run1.jsonl cf8f4dec4a88807b5dc8eb3d9a500efd54933b9ef4491b5d70eca9953c739f95: 75/78 PASS; (17,11,9) UNKNOWN; (17,10,9),
  (17,11,10) NOT_STARTED; stopped 12:38:08 by owned SIGTERM (exit 143), STOP-RECEIPT-v1.md
  a8ab8e2f18146f834e10fef3df2ace245e0bcc75c4c6e9c3a538b7cddb39c72d; DEVIATION-v1.md
  30e70dd874f09352190a1e7720296a9487c1b7b5cc99d7990a3943bed8e4d63b (ulimit -t 9300 backstop).
- t-search-v1: UNKNOWN by parent ruling (admission used the wrong rule; the correct 300 s rule failed: drop 6.49e9 >
  allowed 2.44e9); ADMISSION-AUDIT-RECEIPT-v1.md 49066bc952da5079ce2ebe234fa1346f314cfdd02e8d7c5ffd58df9a5095eb07;
  out/run1.jsonl e79de63132ab3d23b510b1c45f788da96a97e36b13287494193b02bd870d2780.  Not evidence either way.
- t-search-v2: PARTIAL/UNKNOWN as a whole by parent ruling.  Child exit 0 at 14:14:19 (self-budget; DONE_PARTIAL);
  9 item records complete (controls OK; COVERED (29,18) (31,19) (37,22) found 0; BEYOND (31,20) (37,23) (37,24) found 0)
  - exploratory at their timestamps, not proof premises; (41,25) budget-stopped; (41,26) (43,27) (43,28) unstarted.
  Parent-monitor floor breach 11,985,104,896 at 14:07:50 (inside (41,25)) escaped the 20 s guard: resource exception,
  no causal attribution.  END-RECEIPT-v1.md 9323e19733b31b4174ca4c67bc0b8d136715b97a46f8cb0637b91f3c9c34c0ac;
  out/run1.jsonl ae12553b43e7ca4a2e76fde90533030f4dd96db90ecff3f73ff6fc42d1d2100e; wrapper-run1.log
  fa918f6100ba8af5e940f990ed05d044ac9d8d2eb675902e6473654d8f317be6; gate_v1.sh ba112eca261da2e656f6429079454aca2dc56f6876fb72de82de2eb41e07bf81.

## 4. Deviations and labels (all disclosed in README.md)

1. ulimit -t CPU backstops in zs-check-v1 (3000 s) and zx-check-v1 (9300 s).
2. t-search-v1 admitted under the wrong stability rule (UNKNOWN).
3. t-search-v2 wrapper limits (parent-noted): wrapper always exits 0; an empty ps RSS reading would have been skipped
   (none occurred); 20 s guard cadence missed the 14:07:50 floor breach; gate_v1.sh comment "13:17 PDT" is an estimated
   label, actual launch 13:14:14.
4. Header-time lower bound: S1 (g) v2 header "after 13:03:20" vs actual read 13:03:27.
5. Approximate time strings: proof-ROT-K0-v2.md header "13:37:3x" (actual reads 13:37:31 / 13:37:48); README label
   "14:3x" corrected by a later entry (actual 14:19:46).
6. README entry claiming the K0 v1 hash typo was corrected was false (edit had failed); corrected by a later entry;
   v2 is the erratum.
7. Pre-hash edits to freshly created, not yet hashed or sent files (K0 v1, KP v1, ZR v1); each disclosed.
8. proof-ROT-ZR-addendum-plus-v1.md written at 14:44:56 before the parent's "no third candidate" message was received;
   parked, not submitted.

## 5. Exact remaining obstruction (rotation half; o_F <= p)

__REMAINING__

## 6. Coverage bookkeeping

notes-coverage-union-v1.md e45f8320ec47d0b9aac547fc16a749e7dd45906df23a405a3b6f6d8fa94826af: exact (p, o_F, F) table for
5 <= p <= 31 for K01 u ROT-KP u ROT-ZR u S1 (g) IF all were accepted (hand derived).
