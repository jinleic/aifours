# Lane log (host clock, PDT, 2026-10-17)

- 16:52 parent assignment received (M(7) target, contract 21b1b38b…d372). 16:59:37 lane created; sources copied (SHAs equal pins).
- 17:00:21 README §0 frozen (protocol) before any computation.
- 17:23:33 process-cap slip: launched 5 numeric scans at once (cap 4); class-4 scan stopped with SIGTERM within seconds, to be rerun after the others. Its partial output file explore/onb/many_c4_s11_ap200.json is void.
- 17:26 CORRECTION to the 17:23:33 entry: the 5 detached scans never ran (the detached subshells ended with the tool call; all 5 output files are empty). No process ran beyond the cap. Scans relaunched as one async job, at most 4 at a time.
- 17:20:57 nets7 classification rerun complete: evidence/nets7_classes.json (78d1728f…0d67), 7 classes, orbit sums 342480 / 341880 = Egan–Wanless totals.
- 17:25:17 exploration: 300-start alternating-projection + L-BFGS scans on the 5 maximal nets: no zero (minima 9.6–22.4), explore/onb/.
- 17:27–17:28 exploration: weight-push search on Desarguesian nets (exact-gradient rerun): no zero; first run had an inexact penalty gradient (superseded, explore/onb/push_c*_s21.json).
- 17:29:51 K1 pattern SAT (encoder A, F1–F4): maximal nets UNSAT; harmonic SAT (classical); equianharmonic SAT incl. a weight-≥3 model.
- 17:32–17:33 enumeration: harmonic 4 models (all classical), equianharmonic 5 (4 classical + all-weight-4).
- 17:38:57 exploration: weight-4 pattern numerically unrealizable with coefficients ≥0.1 (explore/k1/c6_w4pattern_delta*.json); equivariant ansatz only classical.
- 17:40–17:44 exact: two-overlap phase relations of the weight-4 pattern are inconsistent (97 contradictions; minimum 7-relation cycle by MILP).
- 17:46:25 evidence/k1A (encoder A, CaDiCaL DRAT, drat-trim s VERIFIED for all 7 final CNFs), summary 3f5843c9…af2a.
- 17:47:20 evidence/k1B (independent encoder B, kissat DRAT, all s VERIFIED), identical model sets; summaryB c9ac0158…387f.
- 17:48 phase certificate evidence/k1A/phase_cycle_certificate.json (efd6a51b…1e7c), checker k1_phase_cert.py.
- 17:50 controls evidence/k1A/pattern_controls.json (abfd2a94…38fa); first C1 run void (unshifted f, not a QLS) retired to archive/void-2026-10-17/.
- 17:51:49 review/K1-THEOREM.r1.md frozen (b702b021…8767): Theorem K1 (no set with exactly one non-classical square) + reduction of K2/K3 to weight-≥3 squares. Draft archived as archive/K1-THEOREM.draft-2026-10-17T1751.md (first archived under a wrong guessed label T1803, renamed at once).
- 17:53 note: LOG entries above written with minute-only labels (17:48, 17:50) are bracketed by the host-clock readings 17:47:20 and 17:51:49; they are not exact.
- 17:52:20 correction: the line labelled '17:53 note' was written before 17:52:12 host clock (label guessed); from now on every LOG label is taken from date in the same command.
- 17:57:15 parent steering: until parent verification of K1 finishes, lane cap is <=2 busy processes and <=4 GiB RSS. The K2 no-w3 control solve (explore/k2/k2A.cnf, pid 50124) was stopped with SIGTERM after 2:09 and ended within 1 s; its result is void/UNKNOWN. Still running: K2 w3 (explore/k2/k2A_w3.cnf) and K3 w3+sym (explore/k3/k3A_w3sym.cnf), 1800 s caps. Controls so far: explore/k2/k2_controls_v1.json (classical triple SAT, 15/15 mutations UNSAT, genuine Psi(f) SAT with drop-psi2, tensor families pass on the genuine pair).
- 18:26:28 single-frame K2 (w3) and K3 (w3+sym) CaDiCaL runs ended UNKNOWN at their 1800 s caps (explore/k2/k2A_w3.out, explore/k3/k3A_w3sym.out). Gram-support encoder code/gram_enc.py written; controls explore/gram/gram_controls_v1.json: classical triple SAT, genuine (Psi(f),Phi(m)) pair SAT, Psi(f) on its 3-net heavy SAT, 6/40 single-bit mutations rejected.
- 18:34:06 main classes of Latin squares of order 7: 147 classes, sum of reduced counts 16942080 (MATCH), evidence/ls7_main_classes.txt (BFS by cycle switches from 32 seed classes, ls_classes.c). An empty evidence/ls7_main_classes.txt created by a failed build at 18:28:29 was retired to archive/void-2026-10-17/.
- 18:49:23 review/AMENDMENT-1.r1.md frozen (Gram representation, per-class K2, K3 instance, FIFO DRAT certification); draft archived as archive/AMENDMENT-1.draft-2026-10-17T184923.md. Parent update received: K1 parent routes complete (review/moqls7-k1-parent-check-v1); r2 text corrections queued (full k1_certify SHA; EW reduced sets vs lists wording; no minimality/97-independence claims).
- 19:01:26 review/GRAM-ENCODING.r1.md frozen with pinned encoder hashes (A b2c206d8…8833, B c7583efe…2b45, certify 8eba2bd3…9778); draft archived archive/GRAM-ENCODING.draft-2026-10-17T190126.md. Parent: certification pipeline (2 procs) must not overlap the exploratory K3 solver.
- 19:01:35 note: in review/GRAM-ENCODING.r1.md the pinned-code block was inserted inside the first 'Status' sentence (cosmetic split, no content change); to be fixed only in a later r2 with an explicit delta.
- 19:06:18 frozen-code controls re-run (amendment D): evidence/gram/gram_controlsA_frozen.json, gram_controlsB_frozen.json; encoder-B K2 exploration screen complete: 147/147 UNSAT (kissat, max 60.9 s), explore/k2classes/screenB_v1.jsonl.
- 19:28:00 K3 Gram exploration finished at 19:26:33 with UNKNOWN (native 3600-second cap). All exploratory solvers
  are finished. Before production, froze `review/CERTIFY-DRIVER-DELTA.r2.json`: bounded driver
  `code/gram_certify_r2.py` c031d5eaf7c2a859621e5d5902e82adb5094eabdbbb7ba6f61feda7d6df05163; encoder A/B and
  proof text unchanged. Native solver/checker caps, requested per-child 1536-MiB address-space ceilings, strict
  verifier acceptance, per-instance exclusive evidence and code/CNF/log hashes. First batch: K2 class 0, A and B.
- 19:30:55 froze driver-only r4 delta after two rejected starts. r2 failed before spawning a native child
  (Darwin preexec RLIMIT request). r3's named-proof FIFO auto-detection lost prefix bytes, giving NOT VERIFIED and
  solver SIGPIPE. Both failed outputs remain unchanged. r4 sends the binary FIFO to drat-trim stdin with `-i`,
  avoiding the source's close/reopen detection branch; kissat uses documented `-f`. RSS is sampled directly from
  libproc by the waiting parent, with cooperative safety stops and no third sampling process.
- 19:33:35 class 0 production certificates passed under both encoders: A finished 19:31:44, B 19:33:29, exact
  `s VERIFIED`, solver rc 20 and checker rc 0. Sampled aggregate peaks were 496599040 and 562118656 bytes,
  respectively. Receipts/logs: `evidence/gram/cert_r4/k2{A,B}_0.*`. Encoder hashes are unchanged.
- 19:32:24 froze `review/AMENDMENT-2.r1.md` 82ee394ef6b41c62991e3e8cce4077159a9a6432522abd0f7b1aa48ad0f714e0,
  covering K3 cubes C311/C321/C411 and exact singleton same-ray identities. `code/k3_cubes.py`
  70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550. Before search, its finite predicate
  coverage control passed: 18 assignments, three disjoint six-element residual-symmetry orbits. A cube CNFs were
  generated, not yet searched. K2 A classes 1–146 certification now runs as one sequential two-process pipeline.
- 19:30:55 `review/K1-THEOREM.r2.md` 98b06d226d0c53d7db53540a6760be049e6df3aaba62aefdfa69024837842f59
  applies parent-requested wording/hash/unsupported-MILP-claim corrections only; section 8 and all mathematical
  statements remain unchanged. r1 is untouched.
- 19:55:28 K2 production: encoder A all 147 verified; inventory
  `evidence/gram/k2A_cert_summary_r4.json` 31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29
  (316.508 s total native pipeline time, sampled aggregate RSS peak 496599040 bytes). Encoder B classes 0–73
  completed with exact `s VERIFIED`, solver rc 20/checker rc 0 and no safety stops. Continuing B 74–146
  sequentially; no K3 search overlap.
- 20:14:20 both K2 production routes complete: A 147/147, B 147/147, every exact `s VERIFIED` with rc 20/0
  and no safety stop. B inventory `evidence/gram/k2B_cert_summary_r4.json`
  ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b (1863.771 s native pipeline time;
  sampled aggregate RSS peak 562118656 bytes). Candidate proof frozen as `review/K2-THEOREM.r1.md`
  e846e1d9e345db0630b4aeeee9722d47357daa07daa089b9ae5325c5e58ef05b, with draft archived. Parent acceptance
  remains separate. After certification ended, started the single-solver A K3 cube screen under the frozen
  amendment/bindings; 1800-second native caps, RSS/floor guards, no certification overlap.
- 21:18:13 K3 persisted cube checkpoints: A/C311 UNKNOWN at 20:43:35 after 1800.145 s (sampled RSS 842743808
  bytes); A/C321 UNSAT exploratory at 21:06:29 after 1373.284 s (sampled RSS 907886592 bytes). A/C411 is still
  the final sequential screen; no certificate run overlaps it. Receipts are `explore/k3cubes/screenA_r1/`.
- 21:18:13 proof-only addendum `review/G6-G2-DERIVATION.r1.md`
  8790e9e1af45d4b49e397a06fc4b8dbd70742278698c55561e03f0904f07e791 derives every appended singleton equality
  from G1/G2 and cube units. No base encoder/CNF changes. Exact G6 controls, recorded at 20:15:24, passed:
  three classical QLS7 controls each have 42 anchors and reject 42 own mutations; the non-classical QLS4 has
  8 anchors and rejects 8 mutations; Psi(f) has 0 singleton anchors (vacuous for G6); its Phi(m) mate has 42 and
  rejects 42. This is not a mutation suite for the base encoders or a vector witness for a triple.
- 21:41:14 original A/C411 returned UNSAT exploratory at 21:35:44 in 1755.924 s, sampled RSS peak1085865984
  bytes. Together with C321 this is not yet an exclusion; C311 remains UNKNOWN.
- 21:41:14 new controls completed: 26/26 matched component outcomes, summary
  6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685. These occurred after K2 certificates,
  before new K3 certification. Working transport controls summary
  34a69ae60c1f09bc4029ae9bb589b581d45204e68146af6dc4f5d54be6fd95e6 records both native UNSAT successes,
  both SAT-model retention/validation successes with no UNSAT acceptance, invalid binary-proof rejection and
  safe early-writer rejection. A rejected `/dev/fd` trial is preserved, not accepted.
- 21:41:14 froze `K3-CERTIFICATION-DRIVER-DELTA.r2.json` before A/C321 production: native3600/3600 caps,
  nonblocking FIFO startup/EOF keepalive, direct logs and binary hashes, RSS/floor guards and15-minute persisted
  checkpoints. A/C321 is now the sole two-child pipeline; no exploratory search overlaps.
- 21:41:14 published `K1-THEOREM.r3.md` 2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096,
  canonical `GRAM-ENCODING.md` with identical frozen r2 c6c506a7d1ecba15b2e31393b0da4caa248db5c9227f512c0df9ea5bd07ad6c7,
  and substantive late `LEMMAS.md` 4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9.
  `REVIEW-CORRECTIONS.r2.json` maps the findings, chronology and deliberately unchanged frozen artifacts.
- 22:11:46 first original K3 cube producer certificate: A/C321 verified UNSAT; rc20/0, exact `s VERIFIED`,
  no safety stop. Retained CNF d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388;
  receipt `evidence/k3cubes/cert_r2/A_C321.json`
  c3a30df311eff2ed9b9b5a3706c2ca03a8d4337d8663ea529a9978126fde9314.
  Pipeline21:39:49–22:11:36,1906.802 s; sampled RSS peak1275789312 bytes. Persisted checkpoints at21:54:49
  and22:09:49. Only A/C411 certification now runs, two native children; C311 lex and B routes are not overlapped.
- 22:11:46 corrected K2 candidate text `review/K2-THEOREM.r2.md`
  a73a90078a3b9923935755d2663ecba645ba7f231d8f07384b8f34656ab532cd cites K1-r3/Gram-r2, independent parent
  LS147 checks, precise solver provenance and the separately timed new controls. Original r1 is unchanged.
- 22:39:37 parent22:38 disk notice applied. Observed13557416 KiB free and lane644984 KiB retained; no new
  scientific launch while A/C411's monitored2-child certificate pipeline continues. Froze prospective
  `K3-CERTIFICATION-DRIVER-DELTA.r3.json`, new driver
  da9c210ebf8ab56c59a687155b8ccd106ff90fe748ff6f867ee01fc65997ac78: regenerate/hash in memory against the existing
  single search CNF, retain only logs/checkpoints/receipts, fresh floor plus10MiB projected-growth check. The A/B
  in-memory byte-identity control waits until this pipeline ends. Existing pre-notice copies remain untouched;
  no proof files, deletion or unlink compression.
- 22:43:50 completed new parent-requested corollary note `review/K1-COROLLARY.r1.md`
  7ded3c698163c18757a21964d3552e053f1081f9fd854895054a606e56ef6b6d; draft archived. It includes both
  order7 cardinality/classicality corollaries, exact diagonal-resolution/shear proof, and prior-art
  acknowledgement. Primary definitions/Lemma2.2 and the separate Ball–Simoens2603.02334v1 Lemma21 were reread
  using static URLs; no source PDF copies or new search data were retained. Parent K2 independent replay
  reservation acknowledged. Own active A/C411 certification remains the only two-child pipeline.
- 23:05:47 A/C411 original cube producer certificate passed at23:04:28: rc20/0, exact `s VERIFIED`,
  no safety stop,3143.930 s, sampled RSS peak1899347968 bytes. Receipt
  5f117b60c6b7833978ea012b3c07921d2d19fa6d0a161c4b93d1d13cd6aa23cf; original CNF SHA unchanged.
- 23:05:47 prospective storage-only driver r3 A/B C321 regeneration controls passed with byte-identical
  in-memory hashes, no duplicated CNF and no proof written; tiny receipt
  `evidence/k3cubes/no_duplicate_regen_controls_r1.json`. Fresh floor13040176 KiB before the sole A/C311 lex
  screen launch (1800-second native cap, projected new logs/model<=10 MiB). B cases and all other native jobs wait.
  Prepared `review/drafts/AMENDMENT-4.md` is explicitly unfrozen/inactive; no global-cut CNF or search exists.
- Parent23:17 notice: reported shared free12.16e9 bytes is below the new12.2e9 launch gate. Recorded
  `evidence/DISK-DEFERRAL-2317.json` and reported deferral once; did not remeasure to confirm or poll. All new
  native science/review stages, B cases and cut-refinement controls are deferred. Existing A/C311 lex may finish
  under its old continuous12e9/RSS guard; retain only its small outcome. No >10 MB snapshots/copies, proof
  retention, duplicate CNFs, deletion/thinning or unlink compression. Await parent release after the outcome.
- 23:18:55 completed sole in-flight stage: A/C311 lex UNKNOWN safety stop, free-space floor,769.881 s,
  cooperative SIGTERM rc-15, sampled RSS peak527564800 bytes. Receipt `explore/k3lex/screenA_r1/A_C311.json`
  binds unchanged CNF059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f.
  All own native science processes are now stopped. No new native stage or disk poll follows the23:17 notice.
  Resume only on parent resource release plus fresh>=12.2e9 growth-qualified launch gate and original-deadline
  headroom; use a new output directory, never overwrite the interrupted receipt. M(7) remains unresolved.
- 23:26:41 parent resource release applied after a fresh outer gate:13973892 KiB=14309265408 bytes free,
  greater than12.2e9 plus projected10MiB logs/model/receipt growth. `evidence/RESUME-GATE-2326.json` records it.
  Restarted only the interrupted A/C311 residual-lex solver (1800s) against unchanged existing059be616…a8c4f
  input; new output `explore/k3lex/screenA_r2`, old safety-stop receipt untouched. No CNF/proof copy or second
  science solver. This is resumption after external resource interruption, not a completed negative search.
- 23:47:55 authorized A/C311 lex resumption screenA_r2 ended UNKNOWN safety stop, free-space floor,
  1229.385 s, rc-15, sampled aggregate RSS492994560 bytes. Input059be616…a8c4f and old receipt are unchanged.
  Recorded renewed deferral once (`evidence/DISK-DEFERRAL-2347.json`), reported it and did not poll or launch
  another stage. No own native science process remains. Both lex runs are incomplete resource interruptions.
- 23:47:55 text-only `review/drafts/AMENDMENT-4.r2.md` preserves the earlier draft and clarifies that the
  proved local-case transport can justify future all-frame cuts independently of a full-cap C311 miss.
  It remains unfrozen/inactive; no generator, finite-control execution or cut CNF/search is claimed.
- Parent23:56 release: K1 and both requested order7 corollaries now parent-accepted; recorded the notice in
  `evidence/PARENT-K1-ACCEPTANCE-2356.json`. Parent reported293/294 K2 replays, not a final M(7) verdict.
- 23:58:07 froze prospective direct-B delta and driver
  bbed0b09f84459809d813a35723d77e5aa104f8be67873c36549f5f966a6631e. Began only the authorized B/C321 proof
  attempt behind fresh internal12.2e9-plus10MiB gates (before in-memory regeneration and native launch).
  Existing encoders/cubes and byte hashes unchanged; no B pre-screen result invented, no CNF/proof copy.
  B/C411 awaits this outcome and its own fresh gate. No C311 retry or inactive all-frame cuts were launched.
- 23:59:59 direct B/C321 certification attempt ended UNKNOWN, global free-space floor,77.704 s,
  solver/checker rc-15/-15, no status verdict, sampled aggregate RSS917635072 bytes. Valid fresh outer gates
  at23:58:39/23:58:41 were12584103936/12584140800 bytes (>=12.2e9+10MiB); later floor was hit in flight.
  Receipt `evidence/k3cubes/cert_B_r4/B_C321.json` binds byte-identical8b7b8124…12c6 input. No proof/CNF
  duplicate or retained input growth. Recorded `evidence/DISK-DEFERRAL-2359.json`, reported once, no confirming
  disk poll. All own science jobs ended; B/C411 remains unlaunched pending parent release/fresh gate.
- 00:53:26 (2026-10-18) parent 00:46 notice: K2 CORRECTNESS-ACCEPTED (verdict 25ecb6ba…1242); K3 cover
  disposition fbfc0e10…f369. Ordered work applied:
  (a) froze `review/K3-BMAP-ORACLE.r1.json` (oracle 13f4a5e6…cd8e, B driver r5 0e391cc7…e4f6) at 00:48:54,
  then ran the oracle 00:49:18–00:49:40 behind a 17617924096-byte gate: PASS, 12 binary designs plus 2 sign
  controls through B's own --fix-json branch, exact base prefixes, 0 mismatches, A map = wrapper map, B base
  42a5f304…0aac = both B metadata files; receipt 6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c.
  (b) B/C321 launched with r5 (oracle-gated, fresh gates inside, 3600/3600), output `evidence/k3cubes/cert_B_r5`.
  (d) new sidecar `review/K3-Q4-SIDECAR.r1.json` (34bb5251…16e5) and errata `review/K3-ERRATA.r1.md`
  (85fa93fa…c662); variable indices 109/145 re-verified. (e) new inactive draft `review/drafts/AMENDMENT-4.r1.md`
  (ef87fa49…abb1); my interim unreviewed 23:47 draft retired to
  `archive/AMENDMENT-4.interim-2347.unreviewed-draft.md` (e72233ca…2870). No C311 retry, no cuts, no frozen file
  rewritten.
- 01:02:35 cut generator `code/k3_cuts_r1.py` 0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a pinned
  at 01:00:31 (`review/AMENDMENT-4.GENERATOR.r1.json` 4c23ec44…5dd3), then run 01:00:59–01:02:16 with /usr/bin/python3
  behind a 15951609856-byte gate. Receipt 9cfc0e81bed2cbcbdcd2c205d697dc107b184609f722f0f799225e39092babbf: PASS for
  controls (a)–(e) as listed there; block SHA 05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd
  (6974640 bytes, in memory only). The parent message was labelled 01:12 PDT while the host clock read ~01:00.
  No freeze, no cut CNF, no C311 solve. B/C321 certification continues as the only solver+checker pipeline.
- 01:51:04 B/C321 (oracle-gated r5) ended UNKNOWN, 00:50:14–01:50:15, 3600.249 s: solver rc 20 before the 2700 s
  checkpoint, checker rc 0 with `s TIMEOUT` after parsing 1065624962 proof bytes and starting backward checking.
  Sampled RSS peak 1573158912 B, no safety stop. Receipt b07100e3a06c3a80f34e62dbc09071fc1f1146cb2031bf48c209098390467614.
  Cause: drat-trim -t counts from checker start, so streamed solver time consumes its budget. Started B/C411 under
  the same rule as ordered; asked the parent whether B retries may use drat-trim -t 7200 (pipeline <~2 h).
- 01:57:03 parent message 15aadaf1be5e6ec0 (received ~01:52): ONE B/C321 retry after B/C411 r5 ends (solver 3600 s,
  drat-trim 7200 s); ONE B/C411 retry only if its r5 attempt ends solely on the checker-clock obstruction. Wrote
  `code/k3_direct_B_r6.py` 24fcfea8daeb275433480eaa4b223cab2d2d8bd85b856c29a0ed77b6ccc4c44d and
  `code/proof_stream_r2.py` 45163ed4442966779a818edf2e8a4cec9f7594fb78dcfb46ebda95fe1b7c5605 (both from cp -n of r5 /
  proof_stream, syntax-parsed only). Froze `review/K3-DIRECT-B-DELTA.r6.json`
  5beb6009bf1f06b1c7fede07d8015ceaf53219fc5b480cbffd47b8fee3df1eb8 (draft retired to
  `archive/K3-DIRECT-B-DELTA.r6.draft-0156.json`, same SHA). Nothing launched; B/C411 r5 continues uninterrupted.
- 02:05 parent acknowledgement 15aaddd9155e6ed1: the r6 delta (5beb6009…1eb8) matches the authorisation. Proceed
  exactly as frozen once B/C411 r5 has a receipt. An r6 attempt that again ends `s TIMEOUT` or hits any guard is a
  final UNKNOWN for this authorisation: no third attempt and no solver change without a new parent decision. Report
  each r6 receipt SHA, exact status lines and checker rc. The parent replay desk does not certify B-route cubes.
- 02:11:50 parent disposition of AMENDMENT-4.r1 (message 15aadf6d6d9e6ee5; file 3c9373c0…4e44; desk RESULT
  37920773…5dac):
  - Standard: A+B. A uses lex C311 059be616 plus cuts; B uses original B_C311 b3ec0108 plus cuts.
  - README:91: component-level ruling.
  - Required: r3 (never named r2), an appender/driver per MAJOR-A, m1–m16, and parent source review before launch.
  - Priority: B/C411 r5, then B/C321 r6.
- 02:32:06 statically drafted, unexecuted:
  - `review/drafts/AMENDMENT-4.r3.md` 1ded55bb85a44fc7e7c1be22c49dfe44b8c28ba32ebea0cdb568c6af5e55c366;
  - `review/drafts/K3-CUTS-CERT-DELTA.r1.json` b211321d8609ff06e5898994e90f6c03d26e44f84aa745e12bd1d8821523ac11;
  - `code/k3_cuts_certify_r1.py` 0e978302559f73b115ca2b7df4e67c5e99731a53c43c64e706ffb438a3d70b5a;
  - `code/k3_cuts_r2.py` 5c1c1d67f3d11fc4a087d3419305159e0685e6d2b7b34f0d0cfc46ff1088bdd9;
  - `code/k3_cuts_certify_controls_r1.py` 1dc761d1838b73977c477cd0f7bb1bea56e5503335e7ae917a7647ddf4970025.
  The code was syntax-parsed only. All SHAs were sent to the parent for source review. Proposed caps: 3600 / 7200 / 7320 s.
- ~02:40 parent source review 15aae4593f5e6f0b: HOLD on four issues (byte status parsing, guarded
  preparation/generator, SIGTERM/survivor quarantine, creation-only route directories). The header numbers were
  confirmed right. Caps 3600/7200/7320 approved in principle; not a launch GO.
- Parent notice: A-side exact-CNF facts parent-accepted (`moqls7-k3-A-cubes-parent-verdict-v1.md`
  0ba3fe4f0e14d17abbb21766523f1a18627cb1ca6178c5bf546d4eec2cb81f97; A/C321 and A/C411 replays PASS). A side only; B
  still required. Header erratum note `moqls7-amendment4-header-erratum-v1.md`
  effec3dbc145dc366678bec31c2aa2b2cf8a13b3992bc4838e8f91f1058eb148.
- 02:50:07 new versions written statically (syntax-parsed only); draft 1 and r1 code preserved, never run:
  - `code/stage_guard_r1.py` 2d945ed0274445ced50a99f6ed309734073aff92da79e2e3e3fe43ecdeae0fba;
  - `code/k3_cuts_certify_r2.py` 5b7ab798bb1d7d821152c6a94d4ca4bad542b93f93e0e362ba3da3527d58f0ff;
  - `code/k3_cuts_r3.py` e636924c919c94e2107b33f42f61cd6b6dd3b0b20a57972a842f43b65c8f3d0d;
  - `code/k3_cuts_certify_controls_r2.py` c9e287d995e4306e4c70f799e8bd2508725ac8a670c6724bda7de64fee522ef1;
  - `review/drafts/AMENDMENT-4.r3-d2.md` 157f38c38eae5c05d9720198b35bd8960ebe0228f8814f4c708c13d71ab28291;
  - `review/drafts/K3-CUTS-CERT-DELTA.r2.json` f3684ae19d7d1a7c412cdc6157d726e01279dbaefaa1cbea59746d5fdef6c4f9.
  All SHAs were sent to the parent. Nothing frozen or launched.
- 02:51:14 B/C411 r5 ended UNKNOWN, 01:50:59–02:51:00, 3600.561 s: solver rc 20 before the 2700 s checkpoint,
  checker rc 0, exactly ['s TIMEOUT'] after parsing 1629802 clauses and 1072845839 proof bytes, no safety stop, peak
  RSS 1603338240 B. Receipt 1acc121b735e9f537b7e3403cff6d788188d1ef042c8eefd04a5d0815dd17dfc. Same checker-clock
  obstruction, so the B/C411 r6 precondition holds. Started the authorised B/C321 r6 retry (k3_direct_B_r6.py C321,
  job bg_1793) under the frozen delta 5beb6009…1eb8. B/C411 r6 follows sequentially.
- ~02:58 parent review of draft 2: HOLD on stage_guard_r1. Issues: a failed/short RSS read counted as zero/dead;
  re-parented grandchildren could be lost; raw-PID signals had reuse risk; no completion check; my C9 outcomes were
  stated as if observed. Parent confirmed (02:5x) that the B r6 retries stay sequential and unchanged, with no
  third attempt.
- 03:07:05 statically written (syntax-parsed only); nothing executed; drafts 1/2 and their code preserved, never run:
  - `code/supervise_r1.py` 0755d68e77951798ed84e916d49e6faf42a0c1772c335efee3e9fcc9e65f8b53;
  - `code/supervise_controls_r1.py` 0f61b466ac448ad956c3a1b161d8577c6d7c58e50849045071a9c4fd278601c5;
  - `code/k3_cuts_certify_r3.py` 7453009c863c1017d1bfe5807e725e2906a04b0cf6df8f9996ee4c0732b95fbe;
  - `code/k3_cuts_r4.py` 5c19b64a9243ae2b34cd69e3077f6713a9d959eb1cd330ec58704515b43924d9;
  - `code/k3_cuts_certify_controls_r3.py` 90634fb36ef98b53dbcb7a7d9600508569657af4027f632fe56416b548323f1c;
  - `review/drafts/AMENDMENT-4.r3-d3.md` 9633ffa94083d3789ff4653f3d0c2381a621fe7eaf4f9140820f2e43e6677339;
  - `review/drafts/K3-CUTS-CERT-DELTA.r3.json` 1d728bacab5b62d4b74cdbb6efa9c8951a471d609889d01507c60c9b3e308b67.
  The only command run was a check that the /usr/bin/python3 shim execs in place (same PID). Told the parent that
  the C9 outcomes were expected results only. All SHAs were sent for source review.
- ~03:10 parent 15aaec33b09e6f64: the narrow production domain is acceptable, and a failed RSS read is never death.
  Parent 15aaec72049e6f66: the process-group design is acceptable; one HOLD remains: no exception path after Popen.
- 03:15:23 statically written (syntax-parsed only, nothing executed; every earlier file preserved):
  - `code/supervise_r2.py` 0b023e2cf720e492ac2d96b3ca06d2acc2976da69d13050e3a29420284b78c37 (fail-closed exception
    path: uncertain UNKNOWN, SIGTERM to the reserved group, bounded wait, quarantine, record fallback, handlers
    restored in finally);
  - `code/supervise_controls_r2.py` f8f712542e543988a73d1712120f3744314daec70921e1c7a3e7444d68b811ec (adds S12 statvfs
    exception and S13 raising probe with stop fallback);
  - `code/k3_cuts_certify_r4.py` 3ad6a4df44c62994ddb2a212983f6c953e53fa97d1ff33e7d1f8a020de12c038 (supervisor pin
    read from the frozen delta);
  - `code/k3_cuts_r5.py` 2b9b11891fe641ba9c98f31430b375e48f67aa48712116dddf9026b5f8658e87;
  - `code/k3_cuts_certify_controls_r4.py` 646798ef773d0bd894557134db7b9a6a3e0bf82cbea9ecdd37c29d4f253907e5;
  - `review/drafts/AMENDMENT-4.r3-d4.md` c390a8bfcc2e8663278264729271a744e91d0d9231044a9cd74ea2159997034c;
  - `review/drafts/K3-CUTS-CERT-DELTA.r4.json` 9d93687e2f07e1563c81608fa929c3560efcab35efac26c42219ae2bed72006c.
  All SHAs were sent to the parent.
- 03:16 parent 15aaeeb9b6de6f79: source-review PASS and GO for the control stages only. Frozen x-create:
  `review/AMENDMENT-4.r3.md` c390a8bf…034c and `review/K3-CUTS-CERT-DELTA.r4.json` 9d93687e…006c (drafts kept).
- 03:19:19 gate 13355683840 B free. Ran supervisor controls r2 at top level (TMPDIR explore/tmp_controls_r4).
  Result: **FAIL**, receipt `evidence/k3cubes/supervise_controls_r2.json`
  8313d092308a2de1df38e9cf09d2d8e0bade9cfe6b625e49aa40e12a30e918a1 (40.674 s). P2, S1, S6 and S7 failed; the
  rest passed. No active survivors (all 14 test PIDs gone); no production quarantine. Sequence stopped: generator r5
  and controls r4 were not run.
- 03:20 one-second diagnostic on this Darwin host:
  - proc_pidinfo BSD flavors return ESRCH for an unreaped zombie;
  - PGRP_ONLY still lists the zombie;
  - killpg on a zombie-only group returns EPERM;
  - no os.waitid.
  The parent accepted the failure as ground truth (no rerun) and approved the minimal Darwin correction.
- 03:31:05 statically written, nothing executed:
  - `code/supervise_r3.py` 0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d;
  - `code/supervise_controls_r3.py` 60a94eb2e0324975db81b7117b3717eec24d348d2e05a98fbd57433a91993cd3;
  - `code/k3_cuts_certify_r5.py` a12f9632f23cc76f66de7d619da6f2217480544625d047f0e21c27a3325ee0a5;
  - `code/k3_cuts_r6.py` d0fc540e71c6de97027b59e74f35ed4d30a72c70cc57a830f67b5f0b58b2b1aa;
  - `code/k3_cuts_certify_controls_r5.py` e244ddda0d3e8beaaad9ac293c1fc5f3dc3ffd6c4c6cfb0e77fc37f9c6f2dff0;
  - `review/drafts/AMENDMENT-4.r4.md` 75ac7aece0f050160bf147be91eec906ab99e68294bf9f70feb453b9bcbd9a91;
  - `review/drafts/K3-CUTS-CERT-DELTA.r5.json` 75f8c3823dfab4fc036e90f3fc2df50471b464d79d4e0045b406c73472acb6e2;
  - changeset `review/drafts/SUPERVISOR-R3-CHANGESET.diff` 0ca0d2d5…618c.
  All SHAs were sent to the parent.
- 03:32 parent PASS and GO for the corrected control stages. Frozen x-create: `review/AMENDMENT-4.r4.md`
  75ac7aec…9a91 and `review/K3-CUTS-CERT-DELTA.r5.json` 75f8c382…b6e2. Gate 13236170752 B free; TMPDIR
  explore/tmp_controls_r5.
- 03:32–03:35 OBSERVED:
  - supervisor controls r3 PASS, 34.965 s, receipt 3c77be50cbbd9bc07cf44036ac40ab14d21f5805ea03a895bf68f3b11de799de;
  - generator r6 under supervise_r3 PASS, 60.282 s, receipt
    9624d6127890f90a279ab398888524ed0c5e89376b428e68130ad3bab6db4a24; supervisor record
    b6e72f120ec578c8f9f5d971187b5dfa56d51b88526bce99be4ed95522238821 completed cleanly, peak 806764544 B;
  - controls r5 under supervise_r3 PASS, 7.606 s, receipt bb9445a2e62d7ed970bf031784934bfa85dc7c43f552554bf178720128beb3e3;
    supervisor record eb8244dfee936b45a19bfcdfb81ef379ec5c9d4b27cc58c208bbf9758f8c2b32 completed cleanly.
  Strengthened SHAs: A 18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e (24477803 B), B
  ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a (38353647 B). No production quarantine. No
  scientific C311 launch: that awaits a separate parent GO.
- 03:36:36 parent 15aaf2b0fe9e6f9f: SCIENTIFIC GO for route A only, once, under supervise_r3 + driver r5 with the
  frozen r4/delta r5. Input A is 18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e; the parent
  clarified that its "ae…" was a typo. Route B is not GO; decide after B/C321 r6. If B/C321 r6 is again UNKNOWN,
  report before B/C411 r6.
  Gate: 13212151808 B free (≥ 12.2e9 + 10 MiB); no quarantine; route dir absent. rss-cap =
  min(3758096384, 8 GiB − 3758096384 − 64 MiB) = 3758096384. Lane load: B r6 drat-trim (1 busy).
  Launched route A: supervise_r3 --wall 8400 --rss-cap 3758096384 --floor 12000000000, record
  evidence/k3cubes/C311cuts_A_r5.supervisor.json, command k3_cuts_certify_r5.py A (job bg_1841). Caps: cadical 3600 s,
  drat-trim 7200 s, driver wall guard 7320 s.
- 03:59:13 B/C321 r6 ended **VERIFIED_UNSAT_CASE**, 02:51:24–03:58:40, 4035.475 s. kissat rc 20; solver log
  exactly b"s UNSATISFIABLE\n". drat-trim rc 0 with exactly ['s VERIFIED'] (the raw log line is "\rs VERIFIED"); proof
  1065624962 bytes; 877293 of 1629732 clauses in core; 44276 RAT lemmas. Peak RSS 1629880320 B; no safety stop.
  CNF 8b7b8124…12c6 equals the regeneration. Receipt
  2ffc2fa87d1c1882a067125b0f6bc5520b1e215946b5285052c0355755d832ac. This is a producer certificate only; parent
  replay and acceptance are pending. Started the one authorised B/C411 r6 retry (k3_direct_B_r6.py C411, job
  bg_1849), sequential and unchanged, concurrent with route A within 4 busy.
- ~04:00 parent 15aaf872b31e6fba: SCIENTIFIC GO for route B (input ae3b8309…783a), once, to start when the lane has
  room. I replied that driver r5's lock allows only one C311+cuts pipeline, so B can start only after route A ends.
- 04:10:15 the global 12e9 free-space floor stopped both running pipelines at 04:09:50:
  - **Route A UNKNOWN.** Supervisor record f031159323ded86681b5b16f73db4cd67fac180539f9180e8564fd0a841504d2; trip
    "free bytes 11999735808 below floor 12000000000"; 1980.241 s; leader rc −15; no survivors; no quarantine. The
    driver was terminated and wrote no receipt. Solver log b"c UNKNOWN\n"; checker log empty.
  - **B/C411 r6 UNKNOWN, final.** Receipt 92354254f8a900688bfc7077a3563cfc556c5c732259412423496a6ee7fa0184;
    safety stop "global free-space floor"; 624.163 s; rc −15/−15; empty logs.
  Reported once to the parent. Route B was not started, since its gate cannot pass below the floor. Nothing is
  running in phys-2; waiting for a parent decision. No disk polling.
- ~04:16 parent: the floor stop is accepted as an external UNKNOWN (14.97e9 B free at 04:14). New authorisations:
  - (1) ONE route A attempt, slot 1;
  - (2) ONE route B attempt after A, slot 1;
  - (3) ONE B/C411 attempt with the r6 limits in slot 2, after desk M7BCubeParentReplay hands over;
  - name collisions are to be handled with path-only versions that need PASS.
- 04:18:10 collisions confirmed for route A (C311cuts_A_r5 directory and record) and B/C411 (cert_B_r6/B_C411). Wrote:
  - `code/k3_cuts_certify_r6.py` 12b141fd8e1e2997dec8966d66b2e5b1532069b3bd579f676201514cf271db91;
  - `code/k3_direct_B_r7.py` 386bff0cc014f3a46aee4c27b5057fb9230704c43dbb07ac74171ca8af894cfa;
  - `review/drafts/K3-CUTS-CERT-DELTA.r6.json` 899a04375ca79ca39de9d315a6a3be2bc8157746fa278d6741f7432c72830681;
  - `review/drafts/K3-DIRECT-B-DELTA.r7.json` 55b40519c6a67cee524cf002066eff220f6f621d8d04b5d2fcfef5e98bbeade4;
  - diff `review/drafts/ATTEMPT2-CHANGESET.diff` cd3992b5…1f6d.
  Sent to the parent; nothing launched.
- 04:19:47 parent PASS (changeset cd3992b5…1f6d) and GO. Frozen x-create: `review/K3-CUTS-CERT-DELTA.r6.json`
  899a0437…0681 and `review/K3-DIRECT-B-DELTA.r7.json` 55b40519…ade4. Minor deviation recorded: the B r7 output
  directory keeps the inherited exist_ok=True; every file in it is x-created. Gate 14862540800 B; no quarantine;
  lane busy 0. Launched **route A attempt 2**: supervise_r3 --name C311cuts_A_r6 --wall 8400 --rss-cap 3758096384
  --floor 12000000000 -- k3_cuts_certify_r6.py A (job bg_1865). Route B follows A. B/C411 r7 waits for the replay
  desk's handoff.
- 04:53:46 **route A attempt 2 UNKNOWN**, stopped by the external floor at 04:53:03 after 1981.974 s:
  - driver receipt 06bd12b0517c51a2d4be5f9b06997990e4ddc9e01811fa85d9b1140eaa3edab3: safety stop "global
    free-space floor"; rc −15/−15; no status lines; both feeds delivered all 24477803 B with SHA 18583aab…;
  - supervisor record 50a07ffd0716cf3068dee2fd08fe8a0cea46ff73d669f65d6eacac3e0395fc87: trip "free bytes
    11962544128 below floor 12000000000"; leader rc 3; no survivors; no quarantine.
  Route A's single authorised attempt is consumed. One-shot diagnostic: swap 161 MB of 1024 MB used; Time Machine
  local snapshots hourly plus one at 04:09:55; free space 12509372416 B at 04:53:27. Route B is held (floor rule:
  report once, wait) pending a parent decision. B/C411 r7 still waits for the desk's handoff. phys-2 is idle.
- ~04:59 parent: headroom back (25.96e9 B free at 04:58:46). GO now, one attempt each: slot 1 route B (driver r6,
  input ae3b8309…); slot 2 B/C411 r7, handed over after the desk's B/C321 replay ended UNKNOWN at the same floor
  stop. Also prepare a route-A attempt-3 path-only version.
- 04:59:21 gate 25957699584 B free; no quarantine; lane busy 0. Launched:
  - **route B** under supervise_r3 (name C311cuts_B_r6, wall 8400, rss-cap 3758096384), job bg_1892;
  - **B/C411 r7** (k3_direct_B_r7.py C411, frozen delta r7), job bg_1893.
- ~05:01 statically prepared route-A attempt 3:
  - `code/k3_cuts_certify_r7.py` 6485a1eb5634266becd115195a82cf12750f759de47d8a95a750af8997691c98;
  - `review/drafts/K3-CUTS-CERT-DELTA.r7.json` 0084423249a671cc234d89077fc9628c037bb2aa01f21ddfda31a37229ad9563;
  - diff `review/drafts/ATTEMPT3-CHANGESET.diff` d03e0b8a…43f7a.
  Sent for PASS; not launched.
- 05:02:41 parent PASS for route-A attempt 3 (diff d03e0b8a…, driver r7 6485a1eb…, delta r7 00844232…). Frozen
  x-create: `review/K3-CUTS-CERT-DELTA.r7.json` 0084423249a671cc234d89077fc9628c037bb2aa01f21ddfda31a37229ad9563.
  Attempt 3 runs once, only after route B r6 has fully ended and released slot 1 (per-file flocks do not exclude
  across versions), with a fresh gate, declared-cap sum and busy count rechecked. No r7 B authorisation.
- Parent correction on disk attribution: the cause and recurrence of the free-space declines are UNESTABLISHED. My
  04:53 "[INFERENCE] Time Machine snapshots and/or other lanes" remark is superseded: the snapshot timing coincidence
  establishes nothing. No host change was made. Gate and floor rules are unchanged.
- 06:09:25 **B/C411 r7 VERIFIED_UNSAT_CASE** (producer certificate; the parent replay is pending):
  - receipt `evidence/k3cubes/cert_B_r7/B_C411.json`
    644b5b23d98a55c44df88f15531644b9e8f825b790a9391791d0f50d082a6f75; ran 04:59:36–06:09:18, 4181.588 s;
  - solver rc 20 (log "s UNSATISFIABLE", bde6e1ee…a162); checker rc 0 with status lines ["s VERIFIED"]
    (log 5c01df04…7cd9);
  - CNF 01acf464…8bf8 regenerated and equal to the pin; proof 1072845839 B, streamed only; 3795724 of 9985028
    lemmas in core; peak RSS 1658093568 B.
  Slot 2 is released and both children are reaped. Reported to the parent and to M7BCubeParentReplay. Route B
  C311+cuts is still running: kissat has exited and drat-trim PID 60545 is checking.
- 06:10:21 **route B C311+cuts VERIFIED_UNSAT_CASE** (producer certificate; the parent replay and composition review
  remain):
  - driver receipt `evidence/k3cubes/C311cuts_B_r6/C311cuts_B.json`
    1f00363467d3ed30787cd1b3e4c2e695b8b4d7249623fc6e3994130f4be6c535; ran 04:59:28–06:10:08, 4237.757 s;
  - solver rc 20, checker rc 0; status lines exactly ["s VERIFIED"] and ["s UNSATISFIABLE"];
  - both feeds 38353647 B with SHA ae3b8309…783a; feeds_match_strengthened true;
  - checker log 0cb8eea1…7587: 461370 variables, 1867942 clauses; 842063946 proof bytes;
  - supervisor record 43d481410c4060a755dabaa0d028d16a5c5763348549fad837b778f74e96e4cb: completed_cleanly true;
    no trip; uncertain false; leader rc 0; no quarantine; final_check alive_others [].
- 06:10:35 slot 1 free (route B fully ended). Gate 17676812288 B free; no quarantine; lane busy 0; no live declared
  caps. Launched **route A attempt 3**: supervise_r3 --name C311cuts_A_r7 --wall 8400 --rss-cap 3758096384
  --floor 12000000000 -- k3_cuts_certify_r7.py A (job bg_1957). Reported to the parent.
- ~06:12 parent slot plan: slot 2 runs parent replays (B/C321, then B/C411). Slot 1, after route A attempt 3 fully
  ends, is reserved for parent replays (B C311+cuts, then A C311+cuts if it certifies). No new producer work in slot
  1 without asking. Deliverable: a static, frozen K3 composition note.
- 06:20:23 froze `review/K3-COMPOSITION.r1.md` f17fdd9816f64390aa3773aca20c59e07e46b78bae021c57a597f7d2f6c6b90b
  (cp -n from the draft; 26952 B). It covers 14 links with statement, files, SHA and status; the conditional M(7)
  consequence; open obligations; and errata (AMENDMENT-4.r4:390 says r3 instead of r4; :224/:343 superseded by the
  path-only deltas). Reported to the parent. Route A attempt 3 is still running.
- ~06:29 parent: Codex audit of r1 (`R/moqls7-k3-composition-r1-codex-v1.note.md` 5a68a20d…47bf) returned
  ACCEPT-WITH-FIXES as a conditional proof: 0 FATAL, 0 MAJOR, 3 MINOR. The parent requested an errata-only r2.
- 06:30:54 froze `review/K3-COMPOSITION.r2.md` 803238a6a5c61516af8bfd3aed7760b96f23f330bf6ed745167f24d58cb43f9d and
  `review/K3-COMPOSITION.r1-to-r2.diff` a9f509982ba234dc957860b4371bd0cf9e17c3ac90617e1b5545cc1aeaa3930b (both
  cp -n from drafts). Fixes:
  - F1: the lex group is cube-specific, H_311;
  - F2: `--sym` is separated from the residual cube normalisation;
  - F3: A's G2 clauses with h hold by frame consistency.
  Fix map in §7. No other change. Reported to the parent.
- 07:02 parent disk notice: about 12.44e9 B free and falling about 0.3 GB/min, cause unidentified. Floor unchanged;
  hold all new launches; no retries until free space exceeds 12.2e9 plus growth. One read-only check (lsof/du,
  07:02:12): the only phys-2 job is route A attempt 3. Its write-open files are logs of 16 B, 4096 B and 695 B; TMPDIR
  0 KiB; FIFOs only. Solver exited rc 20 at about 06:49 (log "s UNSATISFIABLE"); drat-trim is checking (checkpoint
  06:55:49). Free space 12433158144 B at 07:02:27. Reported to the parent: no MB/s writers in phys-2.
- 07:05:34 **route A attempt 3 UNKNOWN**, stopped by the supervisor's floor at 07:04:14 after 3207.205 s:
  - supervisor record 6cf3bd5db65862924eddde2ef283756dbeb9eceaa88a5f334267003298c60496: trip "free bytes
    11956592640 below floor 12000000000"; SIGTERM sent; no survivors; no quarantine; leader rc null (the known
    quirk); no driver receipt;
  - solver log "s UNSATISFIABLE" (rc 20 at about 06:49);
  - checker log 1f7af11f…b4b4: 517255126 proof bytes parsed; backward checking had started; no verdict.
  Attempt 3 is consumed. Slot 1 is free and passes to the parent replays. Deviation, read-side only: a readout
  shasum glob matched the spent FIFO nodes and blocked until its 60 s tool timeout; no data moved and no file
  changed. Parent 07:05 update: free space recovered to 14.5e9 at 07:04:23; the cause is unidentified. Free space
  13635059712 B at 07:05:34.
- ~07:07 parent: the Claude composition review returned ACCEPT-WITH-FIXES (0/0/9 MINOR). Revised slot plan: SLOT 1
  route A attempt 4, then the parent A replay; SLOT 2 parent B/C321 a3, then B/C411, then B C311+cuts. Prepared the
  path-only r8 version:
  - driver `code/k3_cuts_certify_r8.py` 1a50f09c0019107637a7c97cf3e997040aa09bf04d626b381ff279f31e087eb5;
  - delta draft d2 `review/drafts/K3-CUTS-CERT-DELTA.r8-d2.json` 439e37ee…d3d4;
  - diff `review/drafts/ATTEMPT4-CHANGESET.r2.diff` 6af43b80…0113.
  Draft d1 (7e013b2b…) and diff 7ae82e1d… were written before the revised plan; never sent; preserved.
- 07:09:00 parent PASS and GO. Froze `review/K3-CUTS-CERT-DELTA.r8.json`
  439e37ee13687877be412c9fccc255305c11e37896c3f58e63ee1f536024d3d4 (cmp byte-identical). Lane-identity rule applied:
  the only live solver pair belongs to PA19 (cwd review/pa19-…/tmp), so the M7-lane count is 0. rss-cap 3758096384
  allows for the declared 2797076480 B of B/C321 a3. Gates passed: 13730205696 B at 07:08:36, plus a re-read just
  before launch. Launched **route A attempt 4**: supervise_r3 --name C311cuts_A_r8 -- k3_cuts_certify_r8.py A (job
  bg_2025); the route directory was created at 07:09.
- 07:10:54 **route A attempt 4 UNKNOWN**, stopped by the supervisor's floor at 07:10:39 after 99.203 s. The launch
  gate at 07:08:59 read 13722476544 B. Supervisor record
  eea330071e6d06cd3a6e2eee7d37ac4bfabc77c095701e341f4c4b1aff90aec6: trip "free bytes 11971710976 below floor
  12000000000"; SIGTERM sent; no survivors; no quarantine; leader rc null. Solver log 8fba55ce… ("c UNKNOWN"),
  checker log empty, no driver receipt. Attempt 4 is consumed. Free space 12019150848 B at 07:10:54, below the
  launch gate; holding with nothing running. Any further attempt needs a parent decision and an r9 version.
- 07:11:27 froze `review/K3-COMPOSITION.r3.md` b85daed48b15ebcc69ea2c8cdd54899911ce8565f9ceebe67a36cbdb01726aed and
  `review/K3-COMPOSITION.r2-to-r3.diff` 844f630647e14149dab2fab52bda26fdd1a3e4cebafcba5034004cb578227125 (cp -n,
  cmp byte-identical). Errata-only: Claude m1–m9 (note 786f3438…78e1), as wording and citation changes, plus a header
  pointer to the attempt 3/4 UNKNOWN records. Fix map in §8. Reported to the parent. The lane is idle.
- ~07:12 parent: prepare a path-only r9 statically. Admission rule for attempt 5 (parent decision, in addition to the
  frozen gate): the parent monitor shows free >= 13.5e9 B and no drop over 300 MB in the preceding 5 minutes.
- 07:14:18 r9 prepared:
  - driver `code/k3_cuts_certify_r9.py` 2f0ced454369242c47ee0f1446f433f92230aa58da4af3c3311aed7476077ed3;
  - read-only watcher `code/admission_wait_r1.py` d0374f5cfec3bcfe408fed0126c3ec5dba5c95737cb02745b98ff93df23e6141;
  - delta draft `review/drafts/K3-CUTS-CERT-DELTA.r9.json` 76f68d34…5487;
  - diff `review/drafts/ATTEMPT5-CHANGESET.diff` 1202c567…86bc.
  A one-shot evaluation at 07:14:14 was not admitted (free 12009799680 B; drop in window 1709424640 B). The first
  watcher draft failed on the monitor's start-event record; the fix skips sample-less events. Sent for GO; nothing
  launched.
- 07:16–07:19 parent: the disk consumer is outside this run (a separate session's /private/tmp scratchpad); free
  space jumped to about 189.5e9 B at 07:17:14. Small static writes are allowed below the gate; native work may resume
  under the frozen gates. Science stops 17:30; native work ends by 17:57.
- 07:19:56 parent GO for r9. Froze `review/K3-CUTS-CERT-DELTA.r9.json`
  76f68d348e2265796696ae4dd9626a3855478748f8c236bfaa4ad57c90525487 (cmp byte-identical). The watcher admitted at
  07:20:08: last sample 07:20:04 free 189510246400 B; 31 samples over 300 s; largest drop 30453760 B. Gate 189309120512
  B at 07:20:29, plus a re-read before launch. M7-lane busy 0 (the only drat-trim, PID 73466, belongs to PA19).
  rss-cap 3758096384. Launched **route A attempt 5**: supervise_r3 --name C311cuts_A_r9 -- k3_cuts_certify_r9.py A
  (job bg_2062); route directory created 07:20.
- 07:21:28 froze `review/K3-H3-INSTANTIATION.r1.md`
  c3d8c05db226781de915d7a98ee84eae16cb7392e7aef2fc4a37b897dfd65cdc (cp -n, cmp byte-identical). It is the written
  proof of Lemma H3 (Link 7): line-cited clause families of both pinned encoders with canonical auxiliaries,
  production-domain sizes and unreachable degenerate branches, the cube/G6 block, the A-route lex block and the cuts.
  Static, no claim. Reported to the parent. Route A attempt 5 is running.
- ~07:28 parent: Codex HOLD on watcher r1 (deadline order, negative age, no chronology check, partial-tail and stale
  handling). Attempt 5 continues; the parent verified its admission after the fact (addendum 595999fb…7c1a). Do not
  reuse r1.
- 07:30:29 wrote `code/admission_wait_r2.py`
  1201e7c6a454d73d55c2c47511748cc3cd30c3f372da273dbad94b06599f3242 statically, unused. It fixes every finding and
  reads the 0722-to-1810 monitor; deadline 15:37 PDT. In-memory controls C1–C13 were all observed as expected. One
  read at 07:30:21: free 186656481280 B but a 2.30e9 B drop in the window, so it would not admit. Reported to the
  parent.
- 07:32 parent rule amendment for long jobs: drop allowance max(300e6, (free_last − 13.5e9)/12); adopt it in the next
  frozen version. 07:32:21 wrote `code/admission_wait_r3.py`
  9e161533d76703b5053ada8f88414175958081b693e5c4f86a3b953cd7e2939c (r2 plus the amended allowance), static and
  unused. In-memory controls C1–C15 were all observed as expected. Reported to the parent.
- ~08:03 parent: the Codex review of H3 r1 returned ACCEPT-WITH-FIXES 0/0/1 (`R/m7-h3-instantiation-codex-v1.note.md`
  2cdda1de…7190): line 155 handles the one-item case validly. 08:04:23 froze
  `review/K3-H3-INSTANTIATION.r1-ERRATUM-1.md` 9559a54bea22d62c5a61b8bb8a66cd3c35785881d32bf6425d0b6fc4677c17b5
  (cp -n, byte-identical) with the parent's corrected wording; r1 is unchanged. Reported to the parent.
- ~08:10 parent policy: after attempt 5, phys-2 launches nothing native; M7BCubeParentReplay is the single M7
  admitter. Static work remains mine.
- 08:19:24 **route A C311+cuts attempt 5 VERIFIED_UNSAT_CASE** (producer certificate; the parent replay is pending):
  - driver receipt `evidence/k3cubes/C311cuts_A_r9/C311cuts_A.json`
    88c154b75e9fa7acb3ec05867d0542b6be4b349c189931ad5217a4f16235f37f; ran 07:20:37–08:19:11, 3511.49 s;
  - solver rc 20, checker rc 0; status lines exactly ["s VERIFIED"] and ["s UNSATISFIABLE"];
  - both feeds 24477803 B with SHA 18583aab…2e5e; feeds_match_strengthened true;
  - checker log d9f86ef6…89f1: 107513 variables, 897308 clauses; 517255126 proof bytes; 1471531 of 3690011 lemmas
    in core;
  - supervisor record 2fb5e03241f3d88416a04fe5c0671b15eb6b6c63329eec651f0d672458ff25b1: completed_cleanly true; no
    trip; leader rc 0; no quarantine; final_check alive_others [].
  Slot 1 released. Reported to the parent and to M7BCubeParentReplay. No further native work from phys-2.
- ~08:20 parent: write K3-COMPOSITION.r4 as a status refresh (H3 parent-accepted at conditional scope, verdict
  edba465a…abca7). 08:23:29 froze `review/K3-COMPOSITION.r4.md`
  152e13cbd6815ba54489bdf3d62857451f51514f0b34e52b2de1a7967d777b3e and `review/K3-COMPOSITION.r3-to-r4.diff`
  57183da275448da70cd6a95ad0aa5be996d9184de368be4b8566fd7007170930 (cp -n, cmp byte-identical). Status refresh
  only (S0–S10): Link 7 accepted at conditional scope; producer certificates with SHAs; replays pending (B_C321 a3
  running; B_C411, B C311+cuts and A C311+cuts queued under launcher v11); the certificates that discharge G1/G2;
  the non-contributing UNKNOWN attempts in §10. Cosmetic quirk: the new sections are numbered §10–§11, so there is
  no §9; references are consistent. Reported to the parent.
- ~11:07 parent: G1 (639fbf6b…b47f) and G2 (d41253f6…7aa7) accepted; H3 accepted at conditional scope; A C311+cuts
  exact-CNF UNSAT accepted (b18472b2…93a8); B_C311cuts-p2 running under the sole parent admitter. Prepare an
  unfrozen r5 composition draft; freeze only after the B-cut verdict.
- 11:17:10 wrote the unfrozen draft `review/drafts/K3-COMPOSITION.r5.md`
  0dbaefe30cc595c04ae2e98762d0ff3363d5d89ee3809012fe7b9a1fbe252486 (static, no M(7) claim). It updates link
  statuses U1–U6 and adds §12 exact A/B formulas, §13 proof-stream boundary (no digest; not the n8 protocol), §14
  reused controls and chronology, §15 lower-bound construction at q = 7, §16 imports and trust base, and §17 fix map.
  Reported to the parent. Not frozen.
