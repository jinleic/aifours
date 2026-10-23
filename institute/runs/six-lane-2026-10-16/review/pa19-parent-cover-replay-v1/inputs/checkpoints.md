# Lane checkpoints (host clock, PDT)

## 2026-10-17T04:02
* Priority kill check done (README): no published v=19 KPD({3,4*}) / PA(19,8,6) construction
  found; Su-Wang 2009 Thm 1.3 summary covers v>25 only; primary PDFs inaccessible (captcha).
* Profiles: 6 column profiles, 10 multisets (data/profiles-19-8-6.json), matches README.
* Verifiers: verify_pa.py + bin/verify_pa2 pass CPro1 PA(18,8,6) (sha256 9b8a24dd... normalized
  copy; original 42006fbc...); 8/8 mutations rejected by both (controls/verifier-mutations/).
* Encoder controls: (13,5,4) normalized cases: 2 SAT (models verified by both verifiers),
  6 UNSAT incl. all-balanced; (7,2,2) has 0 admissible M classes (trivial).
* M1 (M-class split, 290 cases): kissat timing: 4 cases UNKNOWN at 900 s (cases19/), with PB
  and COVER options one E3a case UNSAT in 326 s, E0/E3c cases UNKNOWN at 600 s (trials/).
  Too slow for 290 cases; proofs ~2 GB per 15 min.
* New E0 split (encode_q0.py): quads of an all-balanced array are the dual of a simple graph
  on 8 columns with max degree 4 and 13..16 edges: 486 graphs (geng). Timing run started.
* No witness, no UNSAT claim yet.

## 2026-10-17T04:12
* E0 (all-balanced, multiset ms00) via Amendment A1: 486/486 quad-graph cases UNSAT with
  kissat 4.0.4 (947 CPU-s total, max 86 s g029); all 486 DRAT proofs verified by drat-trim and
  the emitted LRAT verified by lrat-check (cases19q0/results/*.check.json; 2.3 GB DRAT,
  9.4 GB LRAT). geng list independently reproduced as a bijection (networkx atlas).
* M2' independent E0 replication (encode_q0b.py + CaDiCaL LRAT) running (m2q0b/); first
  version without leave constraints retired to archive/m2q0-v1-no-leave/ (g001 UNSAT verified,
  g000 killed at 220 s).
* Non-balanced multisets: Amendment A2 skeleton split generated 5577 cases (cases19skel/);
  timing sample running. No witness, no full UNSAT claim.

## 2026-10-17T05:18 (end of cycle 1; overall verdict UNKNOWN)
* E0 (ms00, balanced only): 486/486 UNSAT, M1 DRAT->LRAT checked 486/486, independent M2'
  (encode_q0b + CaDiCaL LRAT) 486/486 UNSAT with lrat-check VERIFIED. Restricted result.
* A2 skeleton split, pass 1 (kissat, no proof, 30 s): 5397 UNSAT, 180 UNKNOWN (ms01 31,
  ms06 106, ms09 43), 0 SAT. Proof pass (kissat DRAT -> drat-trim -> LRAT streamed to
  lrat-check): ms02/03/04/05 complete (845/845 ok); ms01 1429+ and ms07 ~200 ok; ms06, ms08,
  ms09 and the rest of ms01/ms07 not yet proof-checked.
* 16 proofcheck records written while I was killing my own workers (05:15-05:16) were kill
  artifacts (checker processes terminated mid-run / FIFO pairing broken); retired to
  archive/proofpass-kill-artifacts-0516/ and re-checked.
* (13,5,4) end-to-end control of the A2 pipeline agrees with the M-class encoder (2 SAT
  multisets with verified models, 5 UNSAT).
* Disk: lane 61 GB; filesystem 61 GB free at 05:16. Nothing deleted.

## 2026-10-17T06:18 (cycle 2 checkpoint 1)
* Disk: filesystem free 47,404,184 KB (other lanes); this lane 63,879,520 KB vs 63,936,308 KB
  at cycle-2 start (05:23); cycle-2 new data so far: cycle2/ 616 KB (no CNFs/proofs stored).
* A2 generator replicated independently: src/gen_skel_b.py (nauty genbg, bicoloured graphs,
  -Z1) reproduces all 9 skeleton lists as bijections under isomorphism
  (cycle2/skel-b/compare-ms0*.json: 3215/59/674/39/73/482/482/482/71).
* PA18 positive control (cycle2/control18/): canonicalized CPro1 array satisfies the 18-row
  variants of the M1 skeleton encoder and of the M2 encoder (SAT with all cells fixed);
  3 corrupted arrays UNSAT for both.
* Online checking (src/stream_check.py) validated: same DRAT size/CNF SHA as stored cycle-1
  proofs; SAT controls return models.
* Hard cases: direct CaDiCaL+LRAT (streamed) on the M1 CNF running (2 workers):
  ms06_s00028/00040/00062 UNSAT checked (78/152/209 s). kissat timing: ms09_s00001 517 s,
  ms09_s00004 605 s (no proof). Full-skeleton split explodes for ms06/ms09 (one ms06 case:
  22,782 full skeletons), so ms06/ms09 use direct long runs; ms01 uses A3 (about 60 each).

## 2026-10-17T06:33 (cycle 2 checkpoint 2)
* Safety: past SIGKILLs recorded in README (196 cycle 1 via subprocess.run timeouts, 7 cycle 2
  via Popen.kill on checkers after SAT controls). New stream_check2/run_*2 use SIGTERM only.
* Direct revision-1 run stopped cooperatively (SIGTERM to main 06:29); results so far:
  all completed ms06 cases UNSAT with streamed LRAT checks.
* Disk at 06:18: lane 63,879,520 KB; cycle2/ < 1 MB new.

## 2026-10-17T06:44 (cycle 2 checkpoint 3; header first written as a wrong "07:00", corrected)
* Revision-2 batches stopped with SIGTERM (06:32 v1 direct workers; 06:34 v2 direct + M2
  test); no v2 results written; interrupted rows UNKNOWN: ms06_s00148, ms06_s00150 (v1),
  ms06_s00148 (v2), M2 ms06 b85 (v2 test). Record: cycle2/hard/STOP-0632-revision1.json.
* stream_check3/4 (no SIGKILL; strict checker gating; budget <= 1200 s) smoke-tested:
  cycle2/smoke-stream3*.json, cycle2/smoke-stream4*.json (D2: real drat-trim SIGTERM ->
  UNKNOWN). M2 encoder (13,5,4) control: cycle2/control13-m2.json ok. PA18 controls ok.
* ~06:43 resumed (first written as "06:58", wrong): run_hard4 direct (128 ms06/ms09 cases, cadical -t 3600, 1 worker) and
  run_hard4 a3 (31 ms01 cases, kissat --time 600 per full skeleton, 1 worker).

## 2026-10-17T07:05 (cycle 2 checkpoint 4)
* Disk: filesystem free 61,852,184 KB; lane 63,887,368 KB (cycle-2 start 63,936,308 KB, i.e. no
  net growth; new cycle-2 data only small JSON in cycle2/).
* Direct (cadical + streamed LRAT): 22/149 hard ms06/ms09 cases UNSAT checked (21 rev 1, 1 rev 4,
  ms06_s00148 484 s); A3 (kissat DRAT -> drat-trim -> lrat-check, rev 4): 6/31 ms01 cases decided
  UNSAT (1,516 full skeletons, all checked). No SAT, no UNKNOWN so far in rev 4.

## 2026-10-17T07:36:43-0700 (cycle 2 checkpoint 5)
* Direct CaDiCaL runner (run_hard4) main stopped with SIGTERM at 07:36:09 to switch to runner
  revision 5 (claim files, several runner processes); its orphaned worker finishes
  ms06_s00159 (claimed); ms06_s00174/ms06_s00177 reserved in case they were pre-queued.
  Direct results so far: 27 ms06 cases UNSAT checked (21 revision 1, 6 revision 4).
* A3' partial split (extend_p1q m=1, encode_partq) documented in README and validated:
  (13,5,4) control ok (cycle2/control13-part.json); extend_p1q reproduces extend_p1 on
  ms09_s00001. Test subcases of ms09_s00001 solve in 0.1-0.3 s each.
* Started run_hard5 part on all 43 ms09 cases (kissat --time 600 per subcase, check budget
  600 s). A3 ms01 continues (13/31 decided at 07:31).
* Disk: filesystem free 61258460 KB; lane 63897816 KB.

## 2026-10-17T08:07:04-0700 (cycle 2 checkpoint 6)
* Disk: filesystem free 60451928 KB; lane 63923952 KB (cycle-2 start 63,936,308 KB).
* M1: direct ms06 31/106 UNSAT checked (CaDiCaL runner rev 5 continuing); A3 ms01 18/31
  decided at 08:01; ms09 A3' single-subcase runner decided ms09_s00001 (815), ms09_s00004
  (41), ms09_s00005 (2076) and was stopped with SIGTERM at 08:06 in ms09_s00006 (945+/5733
  single subcases kept); replaced by batched A3'' runner run_hard6 (batches of 100).
* A3'' batching documented and validated ((13,5,4) controls for M1 and M2); M2 partial
  enumerator extend_b reproduces M1 counts; M2 job lists prepared (cycle2/m2-jobs-*.txt:
  74 partial, 106 ms06 direct, 5397 easy).

## 2026-10-17T09:16:45-0700 (cycle 2 checkpoint 7)
* Disk: filesystem free 53482856 KB; lane 63954764 KB.
* M1: ms06 direct 39/106 UNSAT checked; ms01 A3 27/31 summaries (26 decided; ms01_s02573 has
  1 UNKNOWN full skeleton f00012: kissat hit --time 600); ms09: 13/43 decided (3 single-subcase,
  10 batched); ms09_s00010 has one batch whose drat-trim check exceeded its budget (SIGTERM
  after 600+60 s, UNKNOWN). Both UNKNOWNs will be re-run with CaDiCaL + online LRAT
  (src/rerun_unknown.py, results *_r2.json, originals untouched). No SAT anywhere.
* Note: macOS ps/top on this host under-report CPU time by ~41.7x (Apple-silicon timebase);
  solver throughput itself is normal.

## 2026-10-17T10:22:31-0700 (cycle 2 checkpoint 8)
* Disk: filesystem free 47445144 KB; lane 63975160 KB (+~39 MB since cycle-2 start).
* M1 hard: ms06 direct 41/106 (CaDiCaL times median 119 s, mean 333 s, max 3091 s);
  ms01 A3 30/31 + last case ms01_s03171 at 1971/2796 full skeletons; ms09 20/43 decided
  (3 single-subcase + 17 batched). Open UNKNOWN pieces: ms01_s02573 f00012 (kissat 600 s),
  ms09_s00010 batch 4300-4399 (drat-trim budget) -> CaDiCaL reruns queued.
* M2 encoder v2 (row-major lex-leader incl. row lex) added and controlled ((13,5,4), PA18);
  aggregator src/summarize3.py written (STATUS3.json). No SAT anywhere.

## 2026-10-17T10:44:04-0700 (cycle 2 checkpoint 9)
* Disk: filesystem free 44138984 KB (other lanes); lane 63982932 KB.
* M1: A3 runner finished (ms01 31 cases): 29 decided directly; ms01_s03171 f01788 and
  ms09_s00010 batch 4300-4399 had drat-trim checks that ran past the budget on tiny proofs
  (590 KB DRAT; 6 MB DRAT); re-run with CaDiCaL + online LRAT: both UNSAT checked
  (*_r2.json). Open: ms01_s02573 f00012 (hard; CaDiCaL rerun queued).
* M1 streamed proof pass (run_proofpass_stream4, 1 worker) started 10:26 on the 2,907
  pass-1 UNSAT cases without a checked proof: 608 ok, 0 not ok so far.
* ms06 direct 42/106; ms09 23/43 decided.

## 2026-10-17T11:13:49-0700 (cycle 2 checkpoint 10)
* Disk: filesystem free 37883688 KB (falling because of other lanes); lane 63988936 KB (+~52 MB in cycle 2).
* M1 streamed proof pass: 1,376/2,907 ok, 0 not ok. ms06 direct 53/106; ms09 25/43 decided.

## 2026-10-17T11:40:19-0700 (cycle 2 checkpoint 11)
* Disk: filesystem free 35632592 KB; lane 63992680 KB.
* M1 streamed proof pass 1,860/2,907 ok (0 not ok); ms06 direct 58/106; ms09 28/43 decided.

## 2026-10-17T12:05:47-0700 (cycle 2 checkpoint 12)
* Disk: filesystem free 34048936 KB; lane 63995040 KB.
* M1 streamed proof pass 1,993/2,907 ok (0 not ok); ms06 direct 62/106; ms09 29/43 decided.
* Parent rule noted: <= 4 CPU processes including brief controls (wait for a slot).

## 2026-10-17T12:33:24-0700 (cycle 2 checkpoint 13)
* Disk: filesystem free 29131672 KB; lane 64000684 KB (cycle-2 new data ~+64 MB).
* PARENT FINDING: tools/drat-trim/lrat-check is unsound (accepts '2 0 0' on a SAT CNF);
  reproduced (cycle2/checker-smoke/checker-smoke.json). lrat-check dropped as acceptance;
  stream_check5 (kissat/CaDiCaL binary DRAT -> drat-trim only) + smoke (cycle2/smoke-stream5.json,
  all expected; the two former drat-trim stall subcases verified with CaDiCaL proofs).
* CaDiCaL-LRAT direct runner (path c) stopped by SIGTERM 12:24 (in-flight ms06_s00297 had just
  finished). All path-c results, both *_r2 reruns and cycle-1 E0 M2' (m2q0b) are UNCERTIFIED.
* Running (4): ms09 A3'' batches (rev 4, drat-trim-gated); M1 streamed proof pass (rev 4,
  2,569 results); ms06 106 hard cases with kissat_drat (cycle2/hard5, 1 done UNSAT checked);
  E0 M2' re-cert with CaDiCaL DRAT -> drat-trim (m2q0c, 17/486).
* ms01_s02573 f00012 decided by A3-exact (encode_full2): UNSAT, drat-trim verified (rev 4 run;
  its gate includes drat-trim's own verdict).
