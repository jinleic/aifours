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

## 2026-10-17T12:46:35-0700 (cycle 2 checkpoint 14)
* Parent released the reserved CPU at ~12:38; chain run: control13_v5 ok (cycle2/control13-v5.json),
  r3 reruns UNSAT verified, bind_check 5,577/5,577 A2 CNFs + 940 sampled split results match,
  STATUS5.json: M1 drat-trim-certified 5,267/5,577 (open 310: ms06 103, ms08 170, ms09 37),
  E0 M1 486/486, E0 M2' re-cert 53/486, M2 A2 0/5,577, SAT none, uncertified records 68.
* Running (4): ms09 A3'' (rev 4), ms06 kissat_drat (hard5), E0 M2' (m2q0c), proof stream rev 5.
* Disk: filesystem free 24941416 KB (lane du deferred to a free slot; last 64000684 KB at 12:32).

## 2026-10-17T13:33:13-0700 (cycle 2 checkpoint 15)
* Disk: filesystem free 24374685696 bytes (floor 12e9).
* E0 M2' re-cert complete: 486/486 UNSAT, drat-trim verified (m2q0c/).
* Parent route A adopted; rev-8 parser bug caught by its smoke, 6 records archived; rev 9 smoke ok.
* Running (4): M1 ms06 kissat_drat (hard5), M1 ms09 A3'' (rev 4), M2 rev-9 direct (easy list then
  ms06 hard), M2 rev-9 partial batches (74 jobs). Disk guard watcher running.

## 2026-10-17T14:02:53-0700 (cycle 2 checkpoint 16)
* Disk: filesystem free 23317016576 bytes (floor 12e9); no proof files written.
* 13:34 both M2 runners stopped by stop files (parent reserved 2 slots for R5/R6); 14:00 parent
  released one slot (R5 PASS_WITH_PENDING) -> 3 production processes: M1 ms06 kissat_drat x2
  (run_hard8, shared h5_ claims), M1 ms09 A3'' (run_hard6).
* hard5 records: 22 / 106; M2 direct rev5+rev9 records: 709.
* Source delta for the parent: cycle2/src-delta-vs-parent-inputs-20261017T133454.txt (0 changed, 36 new).

## 2026-10-17T15:30:35-0700 (cycle 2 checkpoint 17)
* Disk: filesystem free 19816960000 bytes (floor 12e9).
* Parent R5-R8 complete (binding PASS); staged design approved with conditions; README amendment STAGED
  frozen with hashes; smoke_stream10 all_expected (forged empty clause rejected, timeout/cap UNKNOWN, SAT
  models verified by both verifiers, COUNT=1 serialization).
* M1 ms06: s00150 decided by split (49,902 placements, 500 batches UNSAT verified); direct rev 9
  continued to s00250; run_hard8 stopped at case boundary 15:29 via reservations (released, MANIFEST).
* Now: token COUNT=4; staged runners R1 M1 direct(600 s)->split, R2 M1 split, R3 M2 easy->partial,
  R4 M2 partial->easy, R5 M2 ms06 hard direct(600 s)->split; RSS watchdog (2 s) + busy sampler running.

## 2026-10-17T15:58:51-0700 (cycle 2 checkpoint 18)
* Disk: filesystem free 18624024576 bytes (floor 12e9); lane du deferred.
* Admission paused since 15:34:36 (COUNT=0; parent audit of rev 10). Rev 11 written, smoke run 3 all 12 tests
  pass (runs 1-2 found two defects, fixed); README REV11 and RUNCONF-REV11 frozen; waiting for explicit GO.
* Status unchanged since 15:35: M1 certified 5,500 + ms06 cases decided since 14:33 (s00182, s00183, s00187,
  s00236, s00250 direct; s00150, s00204 split); M2 progressing only for ms01 (direct/partial) and ms06 b101.

## 2026-10-17T16:28:09-0700 (cycle 2 checkpoint 19)
* GO: watchdog4 16:25:5x; rev-1 watchdog stopped 16:26:46; COUNT=2 16:26:50; R1/R2 launched 16:27:01.
* watchdog4 windows so far: 16:27:33 16:28:04 16 389456 2 2.00 2 1.81 2 2
* Disk: filesystem free 17993687040 bytes (floor 12e9).

## 2026-10-17T16:55:09-0700 (cycle 2 checkpoint 20)
* watchdog4: 53 windows since 16:25:54, busy_all max 3, solver/checker max 2, lane RSS max 5109408 KB; last: 16:54:33 16:55:04 16 806384 2 2.00 2 1.94 2 2
* RSS peak 5,109,408 KB (16:35:49-16:36:21) from extend_p1q on ms06_s00214 (387,814 raw placements, 16:33:23-16:36:43);
  7 split tags needing extend_p1q reserved (pb9_ claims) pending extend safeguards; parent informed.
* M1 rev-12: ms06_s00212 split decided (17,329 placements); direct checked: 9 in R1 log, 0 in R2 log.
* Disk: filesystem free 17770872832 bytes (floor 12e9). COUNT=2.

## 2026-10-17T17:47:39-0700 (cycle 2 checkpoint 21)
* watchdog4 since 17:21 (47 windows): busy_all max 4, solver/checker max 2, lane RSS max 2,203,840 KB; last: 17:46:58 17:47:29 16 1986848 3 2.06 2 2.00 3 2
* ms06 hard (106): about 59 decided (direct rev 9/12 checked or split decided), 47 open; R1b/R2b direct, R3 batch-only
  split (s00204, s00216, s00228 decided by 17:32), s00291 direct 1800 s (RUNCONF-S00291) queued under the tokens.
* No alert, no quarantine. Disk free 17442516992 bytes. COUNT=2.

## 2026-10-17T18:13:18-0700 (cycle 2 checkpoint 22)
* watchdog4 since 17:47 (46 windows): busy_all max 3, solver/checker max 2, lane RSS max 2,265,648 KB.
* ms06 hard: about 70 decided, 36 open; direct UNKNOWN (300 s) so far: ms06_s00310 ms06_s00311  -> need an
  exclusive extend window; R3 on ms06_s00266 batches (233 of 658); s00291 direct still waiting
  for a token (token polling is not fair; it will run when the direct list drains).
* No alert, no quarantine. Disk free 17665691648 bytes. COUNT=2.

## 2026-10-17T18:39:08-0700 (cycle 2 checkpoint 23)
* watchdog4 since 18:12 (47 windows): busy_all max 4, solver/checker max 2, lane RSS max 2,285,792 KB.
* ms06 hard: 81 decided, 25 open (20 without any direct record: remaining direct queue + split tags in R3 + s00291);
  direct UNKNOWN at 300 s: ms06_s00310 ms06_s00311 ms06_s00368 ms06_s00370 ms06_s00389 (reserved; exclusive extend window next).
* No alert, no quarantine. Disk free 17245597696 bytes. COUNT=2.

## 2026-10-17T19:04:51-0700 (cycle 2 checkpoint 24)
* watchdog4 since 18:38 (46 windows): busy_all max 3, solver/checker max 2, lane RSS max 2,532,560 KB.
* Direct queue: 6 left; direct UNKNOWN (300 s): ms06_s00310 ms06_s00311 ms06_s00368 ms06_s00370 ms06_s00389 ms06_s00406 ms06_s00410 ms06_s00414 .
* Second exclusive window approved (REV11c procedure); starts when the direct queue drains. Parent R6 replay data
  (review/pa19-placement-binding-v1): M2 extend_b regeneration for the 74 partial cases took <= 13.2 s and <= 122 MB.
* No alert, no quarantine. Disk free 18508107776 bytes. COUNT=2.

## 2026-10-17T19:28:13-0700 (cycle 2 checkpoint 25)
* Admissions COUNT=0 since 19:16:42. Direct queues drained; R3 stopped as a childless token waiter at 19:16:50, claim released. The sole remaining s00291 stage finished 19:26:45, UNSAT/checked under the full rev13 predicate (290.28 s solve, 379.96 s check, 600,779,427 DRAT bytes). No duplicate.
* STOP-hard12 is set. The queued exclusive tool acquired all token flocks + bigmem at 19:26:45. Three representative missing M2 lists completed 19:26:51: 1:2749 0.3 s / 1,460 raw /138 orbits / RSS unsampled (<1 s); 9:20 1.3 s /31,850 raw /8,373 orbits /39,552 KB sampled; 9:55 4.6 s /107,298 raw /27,082 orbits /107,776 KB sampled. All rc0, no cap hit. Remaining M2 helpers are now running exclusively; the ten pending M1 extensions follow.
* Strict coverage before s00291: M1 5,562/5,577, M2 1,131/5,577, E0 separately 486/486 each; no SAT claims. s00291 adds one M1 case pending next strict aggregation.
* Latest watchdog window 19:27:25-19:27:56: lane RSS 97,456 KB; busy_all=0, busy_sc=0. Rev13 runner/exclusive-tool processes are included in lane RSS via absolute lane paths but appear in the watchdog's "other" group, so busy_all is not a count of every helper/runner and is not a cap proof. The all-token exclusive locks enforce no concurrent solver/checker stage in this window.
* Lane allocation 64,195,656 KB (about +259,348 KB from the cycle-2 baseline); last filesystem available 17,442,188 KB, above the 12e9-byte floor. No RSS alert or production quarantine.

## 2026-10-17T19:50:10-0700 (cycle 2 checkpoint 26, exclusive window)
* All 74 M2 partial-job placement lists now exist: the three representatives plus the remaining 49 missing lists generated successfully (remaining-helper chunk 110.34 s wall; sampled helper peaks <=85,568 KB in that chunk; sub-second jobs may have no RSS sample). Existing lists were skipped, never rewritten.
* Ten M1 pending helpers are running sequentially/exclusively with COUNT=0, all-token + bigmem flocks. First four completed: s00310 403.9 s /388,326 raw /32,828 orbits /2,126,544 KB peak; s00311 90.1 s /199,799 /99,960 /4,151,680 KB; s00368 367.3 s /474,106 /59,995 /3,446,592 KB; s00370 204.1 s /398,406 /100,263 /5,070,832 KB. All rc0, no cap hit, ext.json retained.
* Watchdog4 latest window 19:49:08-19:49:39: lane RSS max 2,574,016 KB; busy_all/sc=0 because the exclusive helper lives in "other" (RSS counted, not a busy-count proof). No alert. The 19:47:28-19:47:59 window reached 5,163,632 KB, below 8 GiB.
* Filesystem available 16,720,836 KB, above the 12e9-byte floor. No concurrent production runner, solver or checker.

## 2026-10-17T20:10:45-0700 (cycle 2 checkpoint 27, exclusive window)
* COUNT=0; all token flocks + bigmem held by the sole exclusive tool. Eight of the ten M1 extensions now succeeded, no cap hit; s00430 and s00468 remain in this helper chunk.
* New successful helpers: s00389 263.9 s /368,016 raw /46,577 orbits /2,647,664 KB sampled peak; s00406 238.4 s /232,950 /9,830 /844,512 KB; s00410 445.4 s /473,434 /59,574 /3,484,848 KB; s00414 315.1 s /362,378 /91,250 /4,709,408 KB.
* Last watchdog window 20:10:11-20:10:42: lane RSS max 2,640,432 KB, reported busy_all/sc 0 because this helper is in "other". No RSS alert; no concurrent solver/checker. Free filesystem 16,735,884 KB, above the floor.

## 2026-10-17T20:25:59-0700 (cycle 2 checkpoint 28, production resumed)
* Second exclusive helper window finished: all 74 M2 partial-job ext.json lists valid; nine of ten M1 pending extensions succeeded. s00430 764.5 s /3,237,056 KB peak; s00468 sampled helper RSS reached 5,252,800 KB, guard sent SIGTERM to its own child, rc -15, no ext.json; reservation retained, UNKNOWN. Direct 1800/1200 fallback requested from parent (not yet run).
* Nine successful-list reservations and STOP-hard12 archived with MANIFEST lines; cycle2/exclusive2-resume-20261017T202415.json. COUNT=2 at 20:24:51. s00291 already certified, so it was not duplicated.
* Two bounded chunks now hold t0/t1: PID 86722 run_hard12 split 600/1200/B=100 (s00266/s00285/s00287/s00297, existing lists only), PID 86762 run_m2_12 direct 600/1200 (ms01 easy ranges, independent encoder).
* Watchdog4 first resumed window 20:25:09-20:25:40: busy_all max 3, busy_sc max 2, lane RSS 382,224 KB. No alert or quarantine. Last available filesystem 15,069,496 KB (12e9-byte floor).

## 2026-10-17T20:46:41-0700 (cycle 2 checkpoint 29)
* Two production pipelines, COUNT=2: M1 batch-only splits and independent M2 ms01 direct. s00266 split completed: 65,755 placements in 658 batches, all checked UNSAT, zero other/SAT. The other three tags in this bounded M1 chunk remain in progress/queued.
* Newest M2 record observed ms01_b02139: full rev12 predicate holds (CaDiCaL 3.0.1 default seed, solver UNSAT, checker self-exit rc0, exact s VERIFIED, replay_ok and reader_ok true); 2,153,795 DRAT bytes. Counts remain pending strict aggregation rather than inferred from the filename.
* Latest watchdog window 20:46:07-20:46:38: busy_all max 3, busy_sc max 2, lane RSS max 441,456 KB. No alert/quarantine. Filesystem available 14,915,480 KB, above the 12e9-byte floor.
* s00468 remains UNKNOWN and reserved after its exclusive helper cap trip; the direct fallback decision is pending.

## 2026-10-17T21:07:05-0700 (cycle 2 checkpoint 30)
* Strict summarize11 snapshot at 21:03 (run under a CPU token): M1 5,565/5,577 certified, 12 open; M2 3,202/5,577 certified, 2,375 open; E0 separately 486/486 for each; no SAT claims. M2 ms01 easy-direct is complete (3,184 cases), plus 18 partial cases. Retired rev10 and lrat-only records are not counted.
* Two pipelines, COUNT=2: M1 existing-list batch chunk; M2 direct ms02–ms05 (845 cases, 600/1200 settings) after completion of the ms01 easy chunk.
* Last watchdog window 21:06:33-21:07:04: busy_all max 2, busy_sc max 2, lane RSS max 409,280 KB; recent windows busy_all max 3. No alert or production quarantine. Filesystem available 14,530,644 KB.
* s00468 direct-only fallback remains awaiting parent decision; no new helper attempt.

## 2026-10-17T21:27:32-0700 (cycle 2 checkpoint 31)
* M1 existing-list chunk completed all four tags: s00266 65,755 placements/658 batches; s00285 48,672/487; s00287 34,040/341; s00297 44,839/449. All placements checked UNSAT, zero other/SAT. Next bounded M1 chunk: s00310/s00311/s00368, existing lists only, frozen 600/1200/B=100.
* Independent M2 ms02–ms05 direct chunk finished at 21:14; M2 ms06 easy-direct chunk now running with the frozen 600/1200 settings. A token-gated strict aggregation is queued; separate coverage totals will use that receipt.
* COUNT=2. Last watchdog window 21:26:57-21:27:28: busy_all max 2, busy_sc max 2, lane RSS max 774,352 KB (recent window max busy_all 3). No alert/quarantine. Filesystem available 13,929,792 KB, above the 12e9-byte floor.
* s00468 remains reserved and UNKNOWN; direct 1800/1200 fallback decision is still pending.

## 2026-10-17T22:08:36-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 14206693376 bytes (floor 12000000000).
* Latest watchdog4 sample: `22:07:45 22:08:16 16 1054416 2 1.06 2 1.06 2 2`; sample-file age 20.3 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T22:23:36-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 14071365632 bytes (floor 12000000000).
* Latest watchdog4 sample: `22:22:40 22:23:11 16 993552 3 1.94 2 1.44 2 2`; sample-file age 25.4 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T22:38:36-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 13881184256 bytes (floor 12000000000).
* Latest watchdog4 sample: `22:37:34 22:38:05 16 934048 3 2.06 2 1.94 2 2`; sample-file age 31.8 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T22:53:36-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 13669523456 bytes (floor 12000000000).
* Latest watchdog4 sample: `22:52:58 22:53:29 16 458912 3 1.94 2 1.50 2 2`; sample-file age 7.5 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T23:08:36-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 12679237632 bytes (floor 12000000000).
* Latest watchdog4 sample: `23:07:57 23:08:28 16 1221616 2 1.06 2 1.94 2 2`; sample-file age 8.2 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T23:17:14-0700 (parent-directed shared-disk deferral)
* Parent reports shared free approximately 12.16e9 bytes and requires >=12.2e9 bytes plus projected-growth margin for EVERY new stage. I did not rerun a check to confirm the report.
* COUNT=0, STOP-hard12 and STOP-m2r12 set; no post-notice solver/checker/enumerator/compile/reviewer admission, no signal to in-flight stages. Existing stages may finish with RAM/FIFO proofs and small receipts. Receipt cycle2/disk-deferral-20261017T231714.json. Pending/unverified target cases are UNKNOWN/deferred.
* Deferral reported once; wait for parent/owner recovery decision, no manual disk polling or deletion/thinning. No snapshots/copies larger than 10 MB and no duplicate CNFs.
* Before the pause, s00468 unit subcases 0,1,2 were all strictly checked with pinned base/one-unit binding; not a full-case claim until all six are certified. Regular M1 chunk s00370/s00389/s00406 completed checked UNSAT; the final regular chunk s00410/s00414/s00430 and M2 ms07/ms08 were in progress.

## 2026-10-17T23:23:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 15202099200 bytes (floor 12000000000).
* Latest watchdog4 sample: `23:22:54 23:23:25 16 670784 0 0.00 0 0.00 2 0`; sample-file age 11.0 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T23:38:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 13553209344 bytes (floor 12000000000).
* Latest watchdog4 sample: `23:37:50 23:38:21 16 608208 0 0.00 2 1.75 0 2`; sample-file age 15.7 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-17T23:47:52-0700 (renewed shared-margin deferral)
* Guard14 fresh admission failed at 23:47:02: 12,247,617,536 B free <12,267,108,864 B required (12.2e9 +64 MiB retained-metadata margin). COUNT=0 and both STOP files retained; no ad-hoc margin/cap reduction. Parent notified once; no manual disk polling or further research stage while awaiting recovery.
* M1/M2 controllers stopped at admission boundaries, releasing pb9_ms06_s00410 and m2d9_ms09_b00003; no signal/proof interruption. All frozen six-unit s00468 records are checked and bound. The 66 aggregation controls passed, strictly in-memory metadata/binding mutations, not proof mutations.
* Last strict STATUS14: M1 certified 5,574/5,577 (three regular split cases open), M2 certified 5,387/5,577 (190 open); E0 separately 486/486 for each; SAT list empty. After that snapshot M2 ms09 b1 checked, b2 hit a proof cap (UNKNOWN/no checker), b3 deferred; no new strict recount is claimed.
* Watchdog4 remains live; its recognized-runner busy_all column under-reports the new14 runners, which are included in the "other" group for RSS. Busy solver/checker includes them; COUNT<=2 tokens with at most two busy processes per token is the admission bound, not the sampled busy_all column.

## 2026-10-17T23:53:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 13319081984 bytes (floor 12000000000).
* Latest watchdog4 sample: `23:52:45 23:53:16 16 90128 0 0.00 0 0.00 0 0`; sample-file age 20.7 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T00:08:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 13656764416 bytes (floor 12000000000).
* Latest watchdog4 sample: `00:07:42 00:08:13 16 159568 0 0.00 0 0.00 0 0`; sample-file age 23.1 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T00:23:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 14705537024 bytes (floor 12000000000).
* Latest watchdog4 sample: `00:22:41 00:23:12 16 159808 0 0.00 0 0.00 0 0`; sample-file age 24.0 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T00:38:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 12060934144 bytes (floor 12000000000).
* Latest watchdog4 sample: `00:37:37 00:38:09 16 159936 0 0.00 0 0.00 0 0`; sample-file age 28.0 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T00:53:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 16267550720 bytes (floor 12000000000).
* Latest watchdog4 sample: `00:52:36 00:53:07 16 504304 0 0.00 2 1.62 0 2`; sample-file age 29.7 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T01:08:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 15783682048 bytes (floor 12000000000).
* Latest watchdog4 sample: `01:07:34 01:08:06 16 593040 0 0.00 2 1.75 0 2`; sample-file age 30.9 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T01:23:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=2; filesystem free 15646035968 bytes (floor 12000000000).
* Latest watchdog4 sample: `01:22:36 01:23:07 16 899088 0 0.00 1 1.00 0 2`; sample-file age 29.4 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.

## 2026-10-18T01:34:01-0700 (complete M1 candidate; natural exclusive boundary)
* Strict STATUS15 now has M1 ALL5,577 A2 cases checked, balanced E0 separately486/486; no SAT. Final s00430 one-batch reader-empty miss was recertified with the unchanged alternate standard-checker path, CNF SHA matched, reader/replay true. This is a computer-assisted first-method candidate, NOT parent final acceptance.
* Pinned candidate cycle2/m1-complete-candidate-20261018T012523.json SHA cf3e87c5fd8201286aa7a2b1e09999733cab7e5018a7e49c738f91ff13d1d791. Parent was notified immediately. Independent M2 remains mandatory.
* Latest strict M2:5,412/5,577 checked,165 open (96 hard ms06 +69 ms09), E0 independently486/486. Both bounded five-case hard chunks finished, all10 cases checked. All research stages have naturally ended; COUNT=0 now. Parent receipt-audit peer released its token01:31:53 and holds further chunks for the exclusive helper window.
* New missing-ms09 helpers have NOT run: final owned-child exception/final-floor safety corrections are frozen with targeted smoke receipts, pending parent GO. Normal9 resource/I-O controls reused with provenance; new4 targeted controls pass, no full enumeration rerun or placement/proof-predicate change.
* Last watchdog window01:33:12-01:33:43: lane RSS312,112 KB, no busy solver/checker; recognized-runner busy_all does not include new variant names. Latest automatic free-space receipt01:23:37 was15,646,035,968 B. Actual helper admissions will freshly recheck their exact post-lock bound-specific gate and current new-data allowance.

## 2026-10-18T01:38:37-0700 (automatic host-clock checkpoint; metadata only)
* COUNT=0; filesystem free 15530287104 bytes (floor 12000000000).
* Latest watchdog4 sample: `01:37:40 01:38:11 16 97312 0 0.00 0 0.00 0 0`; sample-file age 25.1 seconds. Samples are observations, not a cap proof.
* last saved STATUS11 snapshot 2026-10-17T22:07:56-0700: M1 open 8; M2 open 1453; NOT a live recount.
