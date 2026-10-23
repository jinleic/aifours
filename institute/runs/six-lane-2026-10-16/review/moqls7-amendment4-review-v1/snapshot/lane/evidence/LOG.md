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
