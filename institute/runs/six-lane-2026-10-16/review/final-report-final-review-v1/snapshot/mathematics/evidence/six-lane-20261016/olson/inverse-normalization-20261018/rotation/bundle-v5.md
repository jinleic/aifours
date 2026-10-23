# Rotation slice: final lane summary, bundle v5 (supersedes bundle v4; adds the accepted ROT-ZR)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T15:25:50-07:00 (a /bin/date read taken immediately before this file
was created by a single exclusive write).  Supersedes bundle-v4.md
(df4db23e4dd419bc1bb1a85327c71ebeef36dd63386613927ff2fe85cfd5cb2d) as the summary; README.md remains the append-only
log.  W = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/ (file names below are
in W); R = institute/runs/six-lane-2026-10-16/review/.
- The unrestricted target - full ROT(p), both halves of INV*(p), ordered Olson for D_(2p) - remains OPEN; nothing here
  claims it.  No novelty claim; no Lean, Comparator or human-review claim.
- Every accepted item is read THROUGH its parent verdict's mandatory overlay; the overlays are not restated here.
- Changes from v4: ROT-ZR is parent-accepted (Sec. 1, 5); Sec. 3 adds earlier UNKNOWNs; Sec. 4 adds the deviations and
  labels that arose after v4 was written and earlier ones that v4 omitted.  The remaining boundaries are those of v4,
  with the ROT-ZR conditional now resolved.

## 1. Parent-accepted results of this slice (text of record -> parent verdict)

| result | text of record (sha256) | parent verdict (sha256) |
|---|---|---|
| GRX, PM*, K1/K2, ROT-o2 | notes-GRX-v1.md afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30; proof-ROT-lowodd-v1.md 8ba3e6c7eeff5ec556166b76eb014d8141d5541c9c702ec3f537e602522f9785 | R/olson-rotation-lowodd-parent-verdict-v2.md 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 |
| ROT-o3 (p >= 5), ROT-o4 (p >= 7) | proof-ROT-o3-v4.md 55670658a819af5ef5570fa71137ad51ee111e46e720cbac5bfdbfd7f51be8cf; proof-ROT-o4-v4.md 7fa49e970603210639f1a0b834c54f5418859bc3dfaf164e34e67836cdaa425a (wording errata of the accepted v3) | R/olson-rotation-o3o4-parent-verdict-v1.md 1225ce75847bfd748cacec51a5f0d41e1e686606b03b4b06a3c35112db34547f |
| C5: ROT-o4 at p = 5 (finite exact, computer-assisted); ROT-o<=4 for every p >= 5 | p5o4-v1/PLAN-v1.md 7d7793cbf137f2ddf01d7cc64872657ba26d15fbac0276101894972038e50588; proof-ROT-o4-p5-finite-v3.md 3a2acf7bd7edae272410f3a7816a0c7b49ba596519fda1ada5465c07a6a0e5c9 | R/olson-rotation-p5o4-parent-verdict-v1.md 92d35e67b811ffefdb6eb802fb428cf1e098f20ffe87b0aa12205fb0f5d78db0 |
| p = 5 few lift (o_F <= 4 or 5 o_F <= 2p + 4) | proof-FEW-p5-lift-v3.md aa2fb35092e8eb7621772428925898f5f000584cd9ff069004afc8e353bcb9cb | R/olson-p5-few-lift-parent-verdict-v1.md c2d06e1478f9aae7354505c81dae3fc7a782c4591a41c3bc288d380d85136d7b |
| INV*-FEW, OLSON-FEW; SHgen; ROT-FEW, MULT; SHgen-E, ROT-FEW-E | proof-INVstar-few-v3.md 779218b4a92c29c996172c361052d2ac9c16cbca003f49921af3713b3ca05531; proof-OLSON-few-v3.md ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a; proof-SHgen-v3.md fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e; proof-ROT-few-v4.md abd3973cd606fe3acc4d534edba13c45e8bbd3764129eaf1f5ca8c7993b7b521; proof-ROT-few-E-v4.md ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R/olson-fewodd-parent-verdict-v1.md 375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8; R/olson-fewodd-parent-verdict-v1-addendum-1.md 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a |
| ZS, ROT/INV*/OLSON-HALF | proof-ROT-half-v1.md 3b8fa50e7a15eb58d215568407238e31d78468562be198035d6bf2d00641c738 | R/olson-half-range-parent-verdict-v1.md b3afb0016e4788209a77c25274f40f6d48edd99136bdade6b1388268d4951c3b |
| generalized ZS, ROT/INV*/OLSON-ZS | proof-ROT-half-v2.md 7403098f15cbb8b7954364a874cc58646d2a91bf11f3e29fee969c5f7c3748eb | R/olson-zs-v2-parent-verdict-v1.md 2ba1fedce1646ae66ba4c510f77f5c40e697a168c144d71d1540a441f9740734 |
| ZX, S1 (a)-(c), S1+, terminal ROT-ZX, uniform ZX+ | proof-ROT-ZX-v1.md ad2460b251b54e93611a7f632349671ce0727cb2a1a812da6ca48d84d1b6815b; proof-ROT-ZX-addendum-S1c-v1.md 7ce7102c3db86c09e6662b353e542e56f104a097442440ebc9ea5e22c012b0b6; notes-ZX-deps-v1.md f98eb3ebe65cdb36419d002c1eecbb430dd96406993df280f88c9d0a9ba92b33 | R/olson-zx-s1c-parent-verdict-v1.md 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af |
| S1 (d), S1++, ZX++ (p >= 11) | proof-ROT-ZX-addendum-S1d-v1.md aefcfc58edfd878b8417d96f278406aedac99bd453c0553fb6979f838d3ac61b | R/olson-s1d-parent-verdict-v1.md 9f712b5247271adc40374df4bcc19f6c07ce90052c78255f09e427f13280ce2b |
| S1 (g) v2: (ZP) => (S1) for integers 0 <= kappa <= (p + delta*)/2 | proof-ROT-ZX-addendum-S1g-v2.md cbbbfecc2de710ca0fda22301a575f7586a13246f356f462c3dd40e10731b31c | R/olson-s1g-parent-verdict-v1.md cc9e27fbabdd14e8cc35e9d6d1477ea1ca90742a985629d8a362c89505b3605e |
| SC0, ZX-SC, ROT/INV*/OLSON-ZX-SC | proof-ROT-ZXSC-v1.md 15958303cffafae29f656f9ab0db0f26df9872415396d19097c07310b92dbb1a | R/olson-zxsc-parent-verdict-v1.md cf039654d40ae568ebe6de27eae62b610dd6be14dd2113e4b3939b0e00f1b134 |
| KETA, PAIR1, ROT-K01, INV*-K01, OLSON-K01 | proof-ROT-K01-v1.md b3ecdb4e09d2eae964322b96e0cddb3c48c91bcea258bebbd4324d16c59eb378 | R/olson-k01-parent-verdict-v1.md e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 |
| ROT-KP (k = p, kappa^ in {0, 1}), INV*-KP, OLSON-KP | proof-ROT-KP-v1.md 472e43cf6c2652ecbc68704dea99fc84263ea241ef3a3147feb51902c43a800e | R/olson-rotkp-parent-verdict-v1.md dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3 |
| REALIZE, ZSTRUCT, LAMBDA, EBOUND, Theorem ROT-ZR (Lambda, H', K'), ZR2, ZR3, INV*/OLSON-ZR2, INV*/OLSON-ZR3 | proof-ROT-ZR-v1.md e8903ff49f22c74ad8253599701a11f7d0af7efb63c7e9dc02cbcde4a77669a7 | R/olson-rotzr-parent-verdict-v1.md 6d8bb6c94f6263834c39130c6d39a2ab54e557740eb45f904732664e879dde73 |
| index-one primary statement (import record) | - | R/olson-index-one-primary-statement-parent-v1.md e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 |

Accepted imports from other slices, used above at their accepted scopes: restricted REFL (Corollary REFL-few-odd,
o_F <= p), R/olson-refl-fewodd-parent-verdict-v1.md 16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca;
RUNS, INV_Res and RGR-LONG(p), R/olson-runs-parent-verdict-v1.md
82adbdddd87dff5af0ef8e0e1ceb82b2a20257213966ae45789811a91a859237.

Accepted uniform conclusions.  INV* for avoiders of length 4p - 2, and an identity 2p-subword in increasing index order
for words of length 4p - 1, hold for every prime p >= 5 under ANY of the following (a union of sufficient conditions):
- (U1) o_F <= max(4, (p + 3)/2), every F (ZX+ with S1 (c); p = 5, o_F = 4 by C5 and the p = 5 lift);
- (U2) 3 o_F <= 2p + 1 and [o_F <= (p + delta* + 2)/2 or F >= o_F + p - delta* - 2] (S1 (g); delta* as in its
  verdict).  For 5 <= p <= 29 the first alternative holds whenever 3 o_F <= 2p + 1.  At p = 31 and o_F = 21 it needs
  F >= 43; among avoiders of length 4p - 2 (which have F >= 2p - o_F) this leaves F = 41, terminal pair (21, 20);
- (U3) o_F <= p and F - o_F >= 2p - 4 (K01 for o_F <= p - 1; ROT-KP for o_F = p);
- (U4) p >= 7: o_F <= p - 1 and F - o_F >= 2p - 6 (ZR2); p >= 17: o_F <= p - 1 and F - o_F >= 2p - 8 (ZR3).
The earlier accepted uniform statements of this slice (FEW, the p = 5 lift, HALF, ZS, ZX+, ZX++, ZX-SC) are contained in
this union.  Restricted REFL (o_F <= p) supplies the reflection half throughout.

## 2. Candidates, notes and superseded files (NOT premises)

| file | sha256 | status |
|---|---|---|
| bundle-v4.md | df4db23e4dd419bc1bb1a85327c71ebeef36dd63386613927ff2fe85cfd5cb2d | superseded by this file |
| bundle-v3.md | 2ee8601c154ec4feaa628b17fa55cb2ffa2b301ef3c2ff3f604dfee412ca6785 | superseded (still the reference for files older than its writing) |
| proof-ROT-ZR-addendum-plus-v1.md | 88eecd13a9f7aa411701460565d1181a8b9511b97a629a4e4692bc947b3d55e5 | PARKED; never submitted; not promoted by the ROT-ZR verdict, which also does not promote Claude's optional (Lambda) sharpening, improved G(3) or extra small-prime corollaries |
| notes-coverage-union-v1.md | e45f8320ec47d0b9aac547fc16a749e7dd45906df23a405a3b6f6d8fa94826af | planning aid only, not a premise (ROT-ZR verdict).  Hand-derived and unreviewed.  It assumed K01, ROT-KP, ROT-ZR and S1 (g) accepted, which now holds, but its table is not parent-checked; entries beyond the accepted uniform conclusions of Sec. 1 (e.g. p = 11, o_F = 8, F = 22) rest on my unreviewed combination of accepted terminal theorems with the deletion ledger |
| proof-ROT-K0-v1.md / proof-ROT-K0-v2.md | 5be6b45d18261adfd856a58b0ed80d2b673f5f79d9aad75edaee655f78184c4a / 4e7ae21cea295228a5fbee27fcb37ccb57df630be353bcc7b6bb3fcbf906da57 | not reviewed; content covered by the accepted K01 (not a premise); v1 carries a hash typo and was never sent |
| proof-ROT-ZX-addendum-S1e-v1.md | ec9fe140647bf375fc13bd8ae156ae0b9a19276f5ed3fc4af1b598d76a27a330 | unreviewed; not cited (S1 (g) verdict overlay 2) |
| proof-ROT-ZX-addendum-S1g-v1.md | 4c45d7047412fdbc569a5aa628a9ff6d574863de7edf2d461b0a4db68d27d415 | superseded by the accepted v2; unreviewed |
| notes-ZX-residual-v1.md / v2 / v3 | fdb5ad4a499377a298aa2d8f0e6f6638d0874a1baad50325426d204021d8ee98 / 4cd9175889e3e1d85b77be80e33bad3f4d94ca0bfa49e749e3a9baa92754e19c / e69a0acc2c0817a0e684a6261edbef79a7d03e42f02b8b9329cd04077a2b03c3 | unreviewed notes (v2 never sent: hash typo; v3 is its erratum) |
| addendum-timestamps-v1.md / v2 / v3 / v4 | 276c4f01d9808a31cdf4e98ed3965a0f7909857d18c89cc4ca0e150e5c990ada / 01d42b3abb34b63b51b26451055794ae25aa0faa597d189b16981ca8d1b19aec / fb423070d1762aee39d10f64863365cd7af56d64dd9edde26c95b78db4f681bb / 55f43d3e3b557ae055bc23b1feb5e0f947adec3549a997fe9aef9cec3498925a | time-label addenda (v1 superseded by v2); every label they list is NOT a clock read |
| earlier notes and superseded versions | see bundle-v3.md | statuses as recorded there (e.g. notes-SC-lengthp: partial; S(p) OPEN) |

## 3. Finite aids and UNKNOWNs (aids only; never premises, except the accepted finite result C5)

- S(7,25,7) (README line 142): stopped by its own CPU limit (SIGXCPU) at 04:44:17: UNKNOWN.
- Gate refusals at 07:10:46 and 07:15:46 (README lines 343-348): nothing ran at those times (recorded as UNKNOWN, not
  relabelled); code/sc_explore_v1.py later ran at 07:22:41 under a fresh gate (exploration, not a premise).
- zs-check-v1: PLAN 55d82db104cc400e521450cdb6a43941895a7649a292b4c0cf115076e7df8ed3, code
  d9d0e0737009f42bf42e25e0d9f86936cf68a74182126cb626bb62ba5af66818, out/run1.jsonl
  bb8ddafb418a4ea62d4907cff98c13483ff0ff0854a3f1d01f7dcd9e6b7b9b1a: aid PASS (deviation: ulimit -t 3000).
- zx-check-v1: PLAN 4791686d2c053b89262551e8c2dc18c91369b56a8c8a88185e03f1578e4a3361, EXPECTED
  dca5b5b55ac6af62359863f7fe18cd1b7457de5a048187fd4fd86367eba5720b, code
  2988e18051eb05bbcdb6d5d8343c1190f4cc3b8fdd487ee33c792aa09e992f8d, out/run1.jsonl
  cf8f4dec4a88807b5dc8eb3d9a500efd54933b9ef4491b5d70eca9953c739f95: 75/78 items PASS; (17,11,9) UNKNOWN; (17,10,9) and
  (17,11,10) NOT_STARTED.  Stopped at 12:38:08 by an owned SIGTERM (parent decision, exit 143): STOP-RECEIPT-v1.md
  a8ab8e2f18146f834e10fef3df2ace245e0bcc75c4c6e9c3a538b7cddb39c72d; DEVIATION-v1.md
  30e70dd874f09352190a1e7720296a9487c1b7b5cc99d7990a3943bed8e4d63b (ulimit -t 9300 backstop).
- t-search-v1: UNKNOWN by parent ruling (admission used a wrong rule; the frozen 300 s rule failed: drop 6.49e9 >
  allowed 2.44e9).  PLAN 00a993fd32908d407dfadefb13e4597b2144eb38e842e1b142670c13cf84451e, EXPECTED
  84107ddac1a3ae7c016f94955ce27fc0d7b0cb2b55eac616cae11636797cec98, code
  0fa86f5c4c7a2ffc21997370aa0466ad5c1c8373feb169aa7e2f14504829ed0f, ADMISSION-AUDIT-RECEIPT-v1.md
  49066bc952da5079ce2ebe234fa1346f314cfdd02e8d7c5ffd58df9a5095eb07, out/run1.jsonl
  e79de63132ab3d23b510b1c45f788da96a97e36b13287494193b02bd870d2780.  Not evidence either way.
- t-search-v2: PARTIAL/UNKNOWN as a whole by parent ruling.  The child exited 0 at 14:14:19 after its 3600 s
  self-budget (DONE_PARTIAL); child and wrapper exit 0 do not make it complete.  Nine completed item records (controls
  as expected; COVERED (29,18), (31,19), (37,22) found 0; BEYOND (31,20), (37,23), (37,24) found 0) are exploratory at
  their original timestamps and are not premises; (41,25) budget-stopped; (41,26), (43,27), (43,28) never started.  The
  parent-monitor sample 11,985,104,896 B at 14:07:50 (below the 12e9 floor, inside (41,25)) escaped the 20 s guard: a
  resource exception with no causal attribution.  END-RECEIPT-v1.md
  9323e19733b31b4174ca4c67bc0b8d136715b97a46f8cb0637b91f3c9c34c0ac; out/run1.jsonl
  ae12553b43e7ca4a2e76fde90533030f4dd96db90ecff3f73ff6fc42d1d2100e; out/wrapper-run1.log
  fa918f6100ba8af5e940f990ed05d044ac9d8d2eb675902e6473654d8f317be6; out/admission-run1.json
  984fca26943dbd6b01ffa79be01f9cd00a8255ff26b0ad9268321c941fee553c; gate_v1.sh
  ba112eca261da2e656f6429079454aca2dc56f6876fb72de82de2eb41e07bf81; code/t_search_v2.py
  ad22b19bf455e46d360dd74139a05388a72813b76cfcf08d144018d5bf59b119; code/admission_v1.py
  661379066d0fa56f641e587b6aca373f137f3e8b4fdb6289074bc3bdf39d0364; PLAN-v1.md
  2a7fd4628c7e0e541c95b2b8e1695625d8dc9fdbdf0043f3bfadeed754ba2b96; EXPECTED-v1.json
  48419050a767de7f3441f32af9b364de67403d02fdde60385199e8fa5c5b47ef.  No relaunch.
- Other finite aids recorded in README.md (stochastic searches, classifiers, controls, p5o4 fixtures and mutation
  checks) are aids only.
- No computational process of this slice was running when this file was written (the only process was the script that
  wrote it).

## 4. Deviations and labels (README line numbers refer to the append-only README.md)

1. CPU backstops.  `ulimit -t` was used for native runs launched before 11:53:11, contrary to the contract: among them
   S(7,25,7) (SIGXCPU at 04:44:17, UNKNOWN), the p5o4-v1 stages and its fixture and mutation runs, zs-check-v1 (3000 s)
   and zx-check-v1 (9300 s); disclosed in zx-check-v1/DEVIATION-v1.md.  No run launched after 11:53:11 used ulimit or
   timeout.
2. t-search-v1 was admitted under a wrong stability rule (UNKNOWN; Sec. 3).
3. t-search-v2 wrapper limits noted by the parent: it always exits 0; it would have skipped an empty ps RSS reading
   (none occurred); its 20 s cadence missed the 14:07:50 floor breach.  gate_v1.sh line 2 carries "13:17 PDT", an
   estimated label from a parent message; the actual admission and launch read is 13:14:14.
4. Tool-deadline termination (README lines 795-802).  A read-only hash-verification process (python3 -B hashing files
   under W and R), launched after 14:55:32 and before 14:57:21, ran under the bash tool's default 300 s deadline and was
   terminated by the tool harness after 300.08 s (signal not known to me; it wrote nothing).  This contravenes the rule
   against native children under tool deadlines.  The check was redone at 15:02:36 on an explicit file list (65 hashes,
   BAD 0).
5. Post-create edits before the first logged or sent hash, each disclosed in the README entry named:
   notes-ZX-residual-v1.md (12:26:59 entry), proof-ROT-ZX-addendum-S1d-v1.md (12:41:50), proof-ROT-ZX-addendum-S1g-v1.md
   (12:59:59), proof-ROT-ZXSC-v1.md (13:11:33; after an intermediate hash computed at 13:12:40, never logged or sent),
   proof-ROT-K0-v1.md (13:36:13; intermediate hash at 13:37:00; see item 6), proof-ROT-KP-v1.md (14:30:15),
   proof-ROT-ZR-v1.md (14:41:12) and bundle-v4.md (15:02:54).  For bundle-v4.md the one partial hash reference was
   replaced by the full sha256 through a scripted unique replacement and an atomic rename over the created file (an
   overwrite), between the clock reads 15:02:36 and 15:02:45; its pre-fix bytes had already been hashed in memory by the
   verification scripts of item 4 and of 15:02:36, without any such hash being printed, logged or sent, so that entry's
   "before any hash" means before any printed, logged or sent hash.  Draft code was edited before its freeze
   (zs-check-v1, t-search-v1; code/flexa_check_v1.cpp before compilation), as disclosed in the plans and README.md; an
   eval import created p5o4-v1/code/__pycache__/ (README line 409; unused by any run).  Every accepted text is the text
   whose hash was reviewed, which postdates these edits.
6. False README statement: the 13:36:13 entry says the K0 v1 abbreviated-hash typo was corrected before logging; the
   edit had failed (corrected by the 13:37:31 entry; proof-ROT-K0-v2.md is the erratum).
7. Time labels that are not second-exact clock reads: (a) every label containing "x" in README lines 81-747, with
   context or bounds in addendum-timestamps-v2..v4 (v1 superseded); (b) the proof-ROT-K0-v2.md header label "13:37:3x"
   (actual reads 13:37:31 before and 13:37:48 after writing); (c) the proof-ROT-ZX-addendum-S1g-v2.md header "after
   13:03:20", a lower bound (actual read 13:03:27); (d) README labels after line 747: "14:48" (line 773; that command's
   printed read was 14:48:22), "14:55" (line 789; reads 14:54:56 and 14:54:57, corrected at line 793), "15:0x-15:06" and
   "~15:01" (lines 795-796; appended at 15:02:21, corrected at lines 799-802); (e) README labels given only to the
   minute are not certified clock reads.
8. proof-ROT-ZR-addendum-plus-v1.md was created by a command issued before the parent's "do not start a third candidate
   before reviews return" message was delivered (the message arrived while that command ran; its clock read was
   14:44:56).  Parked; never submitted.
9. TMPDIR.  Many read-only shell commands (date, shasum, grep, ps, ls) and the README here-document appends ran without
   this slice's own TMPDIR exported, i.e. with the default per-user macOS TMPDIR outside the repository.  The tool shell
   is bash 5.2.37; bash >= 5.1 is documented to pass here-documents smaller than the pipe buffer through pipes, but
   whether any transient temporary file was created was not checked.
10. Hash checks by eye: the abbreviated hashes cited in notes-coverage-union-v1.md and addendum-timestamps-v4.md were
    checked by eye when written; they were checked mechanically before this file was created (3 abbreviated hashes, each matching exactly one file name).
11. Resource events with no cause established here: the parent-reported floor dip and its external cause (README lines
    329-331, 349-350); SIGTERM to parent-owned jobs at 09:25:51, with no signal sent by this slice (lines 451-453); the
    14:07:50 floor breach (Sec. 3).

## 5. Exact remaining obstruction

Accepted terminal criteria.  If SOME admissible normal form of an avoider w of length 4p - 2 has terminal (k, kappa^)
as below, all rotation letters of w lie in one set {rho_c, rho_-c}, c != 0 (for k >= 2 always 0 <= kappa^ <= k - 1, by
GRX and DAV):
- (T1) k = 1 (Proposition K1);
- (T2) 2 <= k <= p and kappa^ <= 1 (K01 for k <= p - 1; ROT-KP for k = p);
- (T3) 3k <= 2p + 1 and kappa^ <= (p + delta*)/2 (ZX with S1 (g)); for 5 <= p <= 29 this is every pair with
  3k <= 2p + 1;
- (T4) p >= 7, 2 <= k <= p - 1, 1 <= kappa^ <= (p - 1)/2, and Lambda: 8kappa^ <= 4p - 3k + 5 or
  2kappa^(2kappa^ - 1) < 2p; H': k - 1 + G(kappa^) <= 2p - 2 - 2kappa^; K': k - 1 + G(kappa^) <= 2p - k - 3, where
  G(kappa) = max over odd s, 1 <= s <= 2kappa - 1, of 2kappa(s - 1)/(s + 1) - s, and G(1..5) = -1, -1, 0, 1, 2 (ROT-ZR).
  In particular ZR2: every (k, 2) with 3 <= k <= p - 1; ZR3: every (k, 3) with 4 <= k <= p - 1 for p >= 17, and
  4 <= k <= 8 at p = 11, 4 <= k <= 11 at p = 13.

Hence a counterexample to the rotation half must be an avoider w of length 4p - 2 whose rotation letters do not lie in
one nonzero pair and EVERY admissible normal form of which has terminal (k, kappa^) in
- (Q1a) k = p and kappa^ >= 2;
- (Q1b) (2p + 1)/3 < k <= p - 1, kappa^ >= 2, and (T4) does not apply: p = 5, or kappa^ > (p - 1)/2, or Lambda, H' or
  K' fails.  Smallest cases: p = 5: (4, 2), (4, 3) (relevant only for o_F >= 6, since ROT-o<=4 covers o_F <= 4);
  p = 7: (6, kappa^) with 3 <= kappa^ <= 5; p = 11: (8, kappa^ >= 4), (9, kappa^ >= 3), (10, kappa^ >= 3);
- (Q2) 3k <= 2p + 1 and kappa^ > (p + delta*)/2: empty for p <= 29; first pair (21, 20) at p = 31, not closed by ROT-ZR
  (20 > (p - 1)/2 = 15).
These are necessary conditions relative to the terminal criteria; the accepted uniform conclusions of Sec. 1 (e.g.
ROT-o<=4) exclude further words.  INV* also needs REFL for the original word: restricted REFL covers o_F <= p; o_F > p is
open (reflection slice, not this slice).

What fails at sequence level (Y = rotation sequence of the normal form, with (ZP) at kappa^):
- (Q1b): for a longest zero-sum Z and the SC0 generator g of Y - Z, the accepted ZSTRUCT gives z = g or z = -s g with
  odd s <= min(|Z| - 1, slack).  Not excluded: a negative-weight sum exceeding n_+ by a positive multiple of 2p when
  Lambda fails; E above SHgen's accepted (H)/(K) thresholds when only E <= k - 1 + G(kappa^) is known; kappa^ > (p - 1)/2,
  outside ROT-ZR's stated range (for kappa^ > (p + delta*)/2 even (S1) is not established).  No example of any of these
  is known to me; no claim either way.
- (Q1a): ROT-ZR is stated only for k <= p - 1.  When a longest zero-sum has length 2kappa^, its complement has length
  exactly p, outside SC0 (length >= p + 1), and the length-p question S(p) is open (notes-SC-lengthp-v2.md); for
  kappa^ > (p + delta*)/2 (S1) is not established either.  The ROT-KP arc argument needs pairwise distinct block values,
  which (ARC) with m = 0 forces only at kappa^ = 0.
- (Q2): (S1) may fail; by the accepted Lemma S1 (b) the rotation sequence then contains two disjoint minimal zero-sums
  P, P' with 2p - 2kappa^ + 2 <= |P|, |P'| <= 2kappa^ and |P| + |P'| >= 2p + 2.
The k = p sequence shapes Y(0) Y(c)^(p-1) (kappa^ = 0) and Y(0)^3 Y(c)^(p-1) (kappa^ = 1) are excluded at word level by
the accepted ROT-KP; they remain valid sequences.  No sequence example refutes ordered Olson, and no finite census is a
premise of any statement above.

## 6. Mechanical check of this file

Before this file was created, each of the 80 64-hex strings in it was checked to equal the sha256 of an existing
file (explicit list: the files directly in W, the four aid packets zs-check-v1, zx-check-v1, t-search-v1, t-search-v2
without tmp/, p5o4-v1/PLAN-v1.md, code/gate_v1.sh and R/olson-*.md); BAD 0.  No abbreviated hash is used in this file.
