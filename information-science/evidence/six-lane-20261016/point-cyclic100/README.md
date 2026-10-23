# Lane info-2: point-cyclic resolution of a 2-(100,4,1) design

Owner: worker `InfoCyclic100`. Contract (read-only): `institute/runs/six-lane-2026-10-16/screening/info-2-point-cyclic100-contract.json`
(recorded 2026-10-17T02:54:44-07:00). Lane opened 2026-10-17 03:04:10 PDT (host clock, `notes/lane-opened.txt`).
Deadline 2026-10-18 18:31:43 PDT. Prior lanes, review files and sources are read-only; nothing outside this lane is
written.

Status label (contract): DERIVED-OPEN. Topalova-Zhelezova (Axioms 15 (2026) 762, Section 7) call v = 88 the smallest
undetermined case; v = 100 is not named there verbatim. Do not call 100 "an explicitly named open case" and do not
state "smallest next" as a theorem. Handbook / Chang-Miao 2002 access holes remain (parent priority audit).

## 1. Frozen contract (written 2026-10-17 03:04-03:10 PDT, BEFORE any search in this lane)

### 1.1 Exact object
A 2-(100,4,1) design on Z_100 (825 distinct blocks, every one of the 4950 unordered pairs in exactly one block) with a
resolution into 33 parallel classes of 25 blocks such that x -> x + 1 maps the block set onto itself and every class
onto a class. Definitions and their binding: `REDUCTION.md` Section 0 (same binding as the accepted 88 lane).

### 1.2 Reduction (proved in `REDUCTION.md`, written before search; untrusted until parent review)
Corollary D: such a resolution exists iff there are 4-subsets X_1..X_6, Y_1, Y_2 of Z_100 with
* (S1) the 96 ordered differences of the eight blocks are exactly Z_100 \ H, H = {0,25,50,75}, each once;
* (S2) each X_i has four distinct residues mod 25, and the six residue sets partition Z_25 \ {0};
* (S3) each Y_j has one point in each residue class mod 4.
Types T1 and T3 are excluded by an elementary stabilizer/difference argument (every class containing a full block
would be invariant under +20, so the pair {0, 20} is uncovered; Theorem A), so the contract's "initial T2 ansatz" is
equivalent to the full problem (Theorems B, C). The T1 prime-power lemma of Mishima-Jimbo (quoted in LMM 2001,
Lemma 2.1, local preprint `sources/`) is NOT used; Theorem A re-derives T1 exclusion and also excludes T3 at v = 100.

Consequences frozen here: a found 8-block seed is an existence witness only after expansion and the direct check of
1.3; a search miss is UNKNOWN, never nonexistence. A nonexistence claim would require a certified exhaustive search of
(S1)-(S3) with every normalization proved in writing, or a proof; not planned in the first cycle.

### 1.3 Witness formats and acceptance
* Seed (compact, `PC-T2-SEED v`): line 1 `PC-T2-SEED 100`; line `H a b c d` (a coset of <v/4>; for v = 100 the
  coset {0,25,50,75}); (v/4 - 1)/4 lines `X a b c d`; (v/4 - 1)/12 lines `Y a b c d`; integers in [0, v), each line
  sorted ascending, single spaces, trailing newline, nothing else.
* Expander `code/pc_expand.py` (stdlib): checks (S1)-(S3) for the seed directly in Z_v (generalized with
  H = <v/4>, residues mod v/4, K = <4>, and res(H) in place of residue 0), builds the classes of Theorem C, sorts
  blocks inside classes and classes by their first block, and writes the certificate.
* Certificate (`POINT-CYCLIC-RESOLUTION v k nclasses blocks_per_class`, then exactly nclasses*blocks_per_class lines
  `c p1 p2 p3 p4`: class index c, points ascending; lines in ascending (c, block) order). Strict format.
* Direct checker `code/pc_check.py` (stdlib, independent of the expander and of any base-block structure): format;
  825 distinct blocks of 4 distinct points; all 4950 pairs exactly once; each of the 33 classes a partition of Z_100;
  the classes partition the block set; x -> x + 1 maps the block set onto itself and each class onto a class. It
  also reports (not as acceptance) short blocks, class stabilizers and class orbit lengths.
* Acceptance for a reported witness: strict certificate + SHA-256, seed + SHA-256, expander/checker source SHA-256,
  exact replay (seed -> certificate byte-identical), checker PASS, mutation controls rejected. Parent supplies the
  independent checkers and review.

### 1.4 Search representations (frozen)
* R1 (constructive tabu search, `code/t2_tabu.c`, C, deterministic per seed via splitmix64; wall clock only for the
  time limit). CRT coordinates Z_v = Z_4 x Z_q (q = v/4 odd), x <-> (x mod 4, x mod q); the ordered difference of
  two points is computed componentwise. State: for every residue r in Z_q \ {0} a block label in {0..a-1}
  (a = (q-1)/4, every label used by exactly 4 residues; this is (S2) by construction) and a height in Z_4; for each
  of the c = (q-1)/12 transversal blocks Y_j four pairwise distinct residues s_{j,0..3} placed at heights 0..3 (this
  is (S3) by construction). Since gcd(4, q) = 1, no difference of a state block lies in H except through equal
  residues, which the state excludes. Each unordered pair of a block gives one +-class {d, -d} of Z_4 x (Z_q \ {0})
  (d != -d always); there are 48 = 2q - 2 classes for q = 25 and exactly 48 pairs. Cost = sum over classes of
  max(0, count - 1); cost 0 <=> (S1). Moves: height change of one X-element; swap of two residues between two
  X-blocks (heights travel with residues, or stay with slots); change of one residue of a Y-block; swap of two
  residues inside a Y-block. Best non-tabu move with random tie-break, aspiration on the descent's best cost,
  random perturbation after a stall. No normalization is imposed in R1 (the state space is exactly the set of
  (S2)+(S3) configurations), so R1 cannot miss solutions "by normalization"; it is a heuristic and can miss anyway.
  On cost 0 the program recounts from scratch and writes a seed in the format of 1.3.
* R2 (fallback, only if R1 misses its budget): CNF encoding of (S1)-(S3) for kissat 4.0.4 with residue-block labels,
  heights and Y residues as one-hot variables. Not written unless needed; its encoding will be frozen here first.
* Positive search control: R1 with q = 13 (v = 52, a = 3, c = 1) must find seeds; each found 52-seed is expanded,
  checked by `pc_check.py`, and tested for affine equivalence (x -> u x + t, u a unit mod 52) to one of the six
  published LMM 2001 designs (`code/control52.py`). LMM state the six designs have full automorphism group of
  order 52; then any isomorphism between two of these cyclic designs normalizes the cyclic group and is affine
  [standard; stated as the reason for the test, the test itself is only a consistency check].

### 1.5 Controls (before any 100 claim)
* `code/control52.py`: the six published v = 52 base-block sets (LMM 2001 Appendix A, machine-parsed from the
  preprint text layer, `sources/lmm2001-preprint.layout.txt`) mapped by CRT Z_4 x Z_13 -> Z_52, expanded by the T2
  rule of their Section 4 (= Theorem C with q = 13) and checked by `pc_check.py`: all must PASS.
* `code/control64.py`: the published point-cyclic 2-(64,4,1) resolution (Topalova-Zhelezova 2026 pp.6-7, T1 type)
  machine-parsed from the PDF text layer, expanded (P1, P2 + t (t < 4), P3 + t (t < 16)), checked: must PASS with
  class orbit lengths 1, 4, 16 (general semantics control; not a T2 structure).
* `code/mutations.py`: deliberate corruptions of a PASS certificate (one point changed; two points swapped between
  classes; a block moved between classes; a block duplicated; non-affine random point relabeling, which keeps the
  design and resolution valid but should break +1 invariance; format errors) must all FAIL for the intended reason,
  and affine relabelings x -> u x + t must PASS.

### 1.6 Stop rules and resources
* <= 4 concurrent CPU processes, <= 8 GiB, checkpoints <= 30 min in `README.md` Section 3 log, chunks <= 3 h.
* R1 first chunk: q = 13 control runs (seconds), then q = 25 with up to 4 seeds x 30 min. Stop all q = 25 searching
  at the first seed whose expansion passes `pc_check.py`; then do controls, replay, manifest and report.
* If R1 finds nothing in the first chunk: freeze R2 here, then run R2 for <= 4 x 1 h. Further budget only with a
  written reason in the log.
* Never report a miss, timeout or UNKNOWN as nonexistence. Never write "first"; no novelty or priority claim.

## 2. Status
Status 2026-10-17 03:29 PDT: CANDIDATE WITNESS, lane checks PASS; awaiting parent independent checkers, review and
priority audit. Claim scope: one explicit point-cyclic resolution of one 2-(100,4,1) design (type T2), i.e. a
cyclically resolvable 2-(100,4,1) design in the source's sense. No novelty, priority or significance claim; no claim
that 100 was an explicitly named open case (see status label above).

Witness (`certs/v100/`, read-only files):
* Seed `pc100_t2.seed` SHA-256 ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245:
  H = {0,25,50,75}; X = {23,57,63,87}, {26,70,74,77}, {19,35,56,78}, {15,17,84,89}, {22,36,68,83}, {46,54,55,66};
  Y = {19,37,54,92}, {0,13,23,42}. Residues mod 25 of the X blocks: {7,12,13,23}, {1,2,20,24}, {3,6,10,19},
  {9,14,15,17}, {8,11,18,22}, {4,5,16,21} (a partition of Z_25 \ {0}); Y blocks have heights (x mod 4) 0,1,2,3.
* Certificate `pc100_t2.cert` (strict format of 1.3; 825 block lines, 33 classes) SHA-256
  971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1.
* `code/pc_check.py` (SHA-256 8b29ab30b721d421694d589d741d3c2e3a293dbfebae4aaf41b7b811f29a18d5): PASS; receipt
  `evidence/pc100_t2-check.{txt,json}`: 825 distinct blocks, all 4950 pairs exactly once, 33 partitions of Z_100,
  block set and every class mapped onto a class by +1; informational: 25 short blocks (stabilizer order 4), class
  orbits of lengths 25 (stabilizer <25>, one short block per class) and 4, 4 (stabilizer <4>): type T2.
* Exact replay (`evidence/replay/`): a fresh `cc -O2` build of `code/t2_tabu.c` (SHA-256
  bc5d00f9b37a96b1bfca9826d9fbb3017ae9f6bde03e8e3c1ec3f97593032411) run as `t2_tabu 25 1 120 OUT 8 8 3000 4 1`
  regenerates the seed byte-identically (same iteration 1215332, about 22 s); `code/pc_expand.py` (SHA-256
  8fe20ef270defd0924c3c4fc296919fc6ffe8bf9fcaeae6c1ed8cfd687ff25c6) regenerates the certificate byte-identically.

Controls (all as intended):
* v = 52, published: the six LMM 2001 Appendix A base-block sets (machine-parsed) expand to certificates that PASS
  (`controls/v52/control52-report.json`). Ten R1 seeds for q = 13 (seeds 1-10) all PASS and each is affinely
  equivalent, design and resolution, to a published one (Nos. 125, 132, 163, 164).
* v = 64, published (TZ 2026 pp.6-7, machine-parsed): PASS, type T1, class orbits 1, 4, 16; the printed classes
  equal the development of the printed base blocks (`controls/v64/control64-report.json`).
* Mutations (`controls/mutations-v100/mutations-report.json`): point changed -> FAIL D2; points swapped between
  classes -> FAIL D2; block moved to another class -> FAIL R1; block duplicated -> FAIL D1; random non-affine
  relabeling -> FAIL C1; affine relabelings 3x+7, x+1, -x -> PASS; 7 format corruptions -> FAIL F; C2 path on
  K_6 one-factorizations (k = 2): the +1-invariant one PASS, a non-invariant one FAIL C2 (no 2- or 3-class
  re-partition of the v = 100 certificate exists, so a C2-only mutation of it is not available:
  `evidence/class-trade-search.txt`, exhaustive); 3 seed mutations refused by the expander.
* Reduction arithmetic: `evidence/e1-blocks.txt` (all C(100,4) 4-subsets: Lemma 2), `evidence/reduction-arith.txt`
  (Lemma 3 / Corollary 4 table: (4,1), (20,5), (100,25) and m = 0 stabilizers 5, 25; 20 in every stabilizer but <25>;
  T2 m = 0 classes only stabilizer <4>). Controls of finite steps only; the proof is `REDUCTION.md`.
* Abundance (informational): seeds 2-4 for 90 s each produced 9 further seeds (5, 0, 4); with the witness these
  10 seeds expand to PASS certificates in 10 pairwise affinely inequivalent (design, resolution) pairs
  (`evidence/multi-solutions.txt`). The witness design has no multiplier automorphism other than u = 1; the pair
  {0, 20} lies in the full block {0, 8, 9, 20} of a class with stabilizer <25> (`evidence/witness-structure.txt`).
* T1 consistency: Lemma 2.1 of LMM 2001 (quoting Mishima-Jimbo 1997; local preprint p.4: "Let v = p^alpha for a prime
  number p and assume that p is relatively prime to k. Then there does not exist any CRCS(2, k, kv) of type (T1).")
  applies to v/k = 25 = 5^2 with gcd(5, 4) = 1 and agrees with Theorem A; it is not used anywhere in this lane.

Open for the parent: independent checkers and replay; review of `REDUCTION.md` (Theorem A excludes T1 and T3 at
v = 100 by the pair {0, 20}; the T3 part goes beyond the Mishima-Jimbo T3 condition quoted in the 88 audit, which
does not exclude 25 = 5 x 5, so it needs a hostile check; it is not needed for the existence claim, which rests on
the certificate alone); priority audit (Handbook, Chang-Miao 2002 and other access holes).

Hashes of all lane files: `evidence/MANIFEST.sha256` (`shasum -a 256 -c evidence/MANIFEST.sha256` from the lane
root), generated as the last step of this cycle; files are not edited after it.

### Cycle 2: Lean kernel existence formalization (requested by Main over IRC after 03:30 PDT)
Request: a full existence theorem on `Fin 100` stating that B is a 2-(100,4,1) design, R partitions its blocks into
point-partitioning classes and x -> x + 1 preserves both (with the one 100-cycle fact explicit); a Target module of
definitions only; data bound to the pinned seed and certificate with a strict external raw-binding audit; semantic
corruption controls; a source/binary hash manifest; a no-overwrite clean rebuild and a fresh leanchecker replay; at most
one Lean process and 8 GiB; no native_decide, ofReduceBool, sorry, new axioms or unsafe code; no search rerun.
Everything is in `lean-kernel/`. The patterns of `review/rdsqs-kernel-worker-v1/` and
`review/point-cyclic88-kernel-worker-v1/` were read and not modified; `lean_source_scan.py` is a byte copy of the shared
scanner (SHA-256 8e9eb834…af5bb).

Status 04:03 PDT: kernel-checked existence root READY; Main notified. No priority or novelty claim.
* `PC100Kernel/Target.lean` (definitions only): `IsDesign241`, `IsParallelClass`, `IsResolution`, `blockImage`,
  `IsResolutionAutomorphism` (B onto B and every class of R onto a class of R), `IsFullCycle` (`IsCycle` and
  `support = univ`), `IsPointCyclicResolution` (TZ Def. 5), `shift v = Equiv.addRight 1`, and `Target`,
  `TargetShift`, `TargetCounts`.
* Roots in `PC100Kernel/Audit100.lean`, each with axioms {propext, Classical.choice, Quot.sound} only:
  `root100 : Target 100`, `root100_shift : TargetShift 100`, `root100_counts : TargetCounts 100` (825 / 33 / 25),
  `root100_cycleType : (shift 100).cycleType = {100}`, `shift100_apply` (x + 1, by rfl), `witness100` (the explicit
  certificate objects) and `root100_unfolded` (written without the Target definitions).
* Method: the literal `cert100` is the pinned certificate (971f…4f7c1) copied verbatim by `gen_lean.py`. The Bool
  `certCheck` (`PC100Kernel/Check.lean`) checks ranges, a bitmask of all 4950 pair codes inserted exactly once, a
  point bitmask for each class, and, for each class translated by +1, equality with a listed class (point-set codes
  in both directions). The data-independent theorem `sound_of_check` turns `certCheck = true` into the design, the
  resolution, the shift automorphism and the counts. `decide +kernel` evaluates the checker in the kernel (about
  7 s). The cycle facts are Mathlib's `finRotate` lemmas. Theorem C is not formalized: the seed enters only through
  the external audit.
* Binding: `audit_binding.py` (stdlib) checks that the literal equals the certificate, that an independent
  re-implementation of the Theorem C expansion of the seed (ac72…6245) is byte-identical to the certificate, and that
  the Lean objects recomputed from the literal are the certificate's 825 blocks and 33 classes. It also checks a
  stdlib mirror of the checker. All 6 in-memory corruptions are rejected, each by the intended check.
* Kernel controls (`PC100Kernel/Controls100.lean`):
  * swap 1 and 2 between two blocks: `certCheck` false and `¬ IsDesign241`;
  * relabel 1 and 2 in every block: ranges, pairs and classes pass, the shift test fails, and the block set is not
    shift-invariant;
  * move one block between classes: `¬ IsResolution`;
  * write one number as n + 100 (same residue): rejected by the range test;
  * drop one block: `certCheck` false;
  * published v = 64 resolution (`controls/v64/tz64.cert` via `Data64.lean`): the checker accepts it, and
    `sound_of_check` gives its design, resolution and shift invariance;
  * Main's v = 64 class trade (classes 0 and 12): ranges, pairs and classes pass and the shift test fails; the block
    set is still shift-invariant, but not every class is mapped onto a class.

  The cycle-1 note that no C2-only mutation was available referred to 2- and 3-class re-partitions of the v = 100
  certificate only. `PC100Kernel/ControlFail100.lean` must fail and does: the kernel rejects both corrupted
  `certCheck` claims, and the dependent theorems depend on `sorryAx`.
* Replay: `lean-kernel/manifest.json` (SHA-256 18ca2e197c6561cfc88f3b6104e15f3eb1b2502e786ceedfffff97a413f8a60a) pins
  the sources, scripts, inputs, toolchain binaries, Mathlib olean, cache files and definition locations.
  `python3 -B replay.py worker` produced `lean-kernel/replay-worker/result.json` (SHA-256
  27ecefb1ba0bdb035410d4246312928a4ac05598a5f550a1adf2c4fd7533c813): REBUILD_AND_FRESH_KERNEL_REPLAY_PASS,
  03:56:40-04:01:56. In it, the data modules were regenerated byte-identically, the binding audit passed, the source
  scan was clean and the audit log was byte-identical to the pinned expected output. leanchecker --fresh took 117 s and
  2.9 GB for `Audit100` and 146 s and 3.4 GB for `Controls100`. Peak build RSS was 3.5 GB, with one Lean process at a
  time.
* Trust limits: lean and leanchecker come from one toolchain (not an independent kernel or Comparator). The
  raw-file-to-literal and seed-to-certificate equalities are the external stdlib audit, not Lean theorems.

README.md was edited after the cycle-1 manifest (`evidence/MANIFEST.sha256` records its cycle-1 hash). All lane
files after cycle 2: `evidence/MANIFEST-cycle2.sha256`.

## 3. Log (host clock, PDT)
- 03:04:10 lane created; LMM 2001 preprint fetched from the Wayback copy named in the 88 priority audit:
  `sources/lmm2001-preprint-a0801799.pdf` SHA-256 3c5f0740675009c0c55c4133abb9f7b45ed96ce15dc0612a252ff2f494207826;
  text layer `sources/lmm2001-preprint.layout.txt` (pdftotext -layout).
- 03:05-03:10 `REDUCTION.md` and this frozen section written; no search run before this point. Freeze hashes in
  `notes/freeze-receipt.txt` (03:09:44 PDT); afterwards only this log line and the Section 1 heading time were
  corrected to the real host-clock times (wording only, 03:10).
- 03:11 R1 compiled; q = 13 control seeds 1-3 found in < 0.1 s each.
- 03:12:02-03:12:25 R1 q = 25 seed 1: FOUND at iteration 1215332 (22.2 s), the only q = 25 search before the stop
  rule fired. 03:13:49 seed and certificate copied to `certs/v100/` (read-only); immediate message to Main with
  both SHA-256 values.
- 03:12:25-03:13:36 `pc_check.py` and `pc_expand.py` written (after the seed was found, before its first expansion
  at 03:13:42; file mtimes) and unchanged since.
- 03:14-03:25 `control52.py` (q = 13 seeds 4-10 found) PASS; `control64.py` PASS; `mutations.py` PASS (rerun after
  adding the K_6 C2 cases); `class_trade_search.py` (03:23); E1/E2 arithmetic controls (03:24). A 4-class
  re-partition search in the eval kernel hit its node limit and was inconclusive (not used).
- 03:22:48-03:23:10 replay: seed and certificate byte-identical.
- 03:24:59-03:26:29 abundance runs (seeds 2, 3, 4; 90 s each; 3 processes). DEVIATION: the frozen stop rule (1.6)
  says to stop q = 25 searching after the first PASS; these informational runs (about 4.5 CPU-minutes) are outside
  it and are recorded here; nothing in the witness or its checks depends on them.
- 03:26-03:30 abundance analysis (`multi_analyze.py`), checker receipt, this status (first written 03:29; an earlier
  draft of this line and of the status heading carried a guessed time 03:35, corrected at 03:30). Total q = 25 search
  CPU about 5.5 minutes.
- 03:30:37 witness_structure.py evidence; README status final for this cycle; manifest generated next (last write of the cycle).
- after 03:30 Main's IRC request for the Lean formalization (above). 03:37 read patterns (rdsqs, PC88 kernel
  workers). 03:39:18 `lean-kernel/` created (env scripts, scanner copy).
- 03:40:27 Target built; 03:42:53 Check built (one fix: unfold `shiftOK`; `finRotate_apply` replaces a deprecated
  lemma); 03:43:49 `Data100.lean` generated; 03:44:13 Cert100 built (kernel evaluation of `certCheck`, 6.7 s).
- 03:47:35 `gen_lean.py` extended to `Data64.lean`, regenerating `Data100.lean` byte-identically; 03:48-03:51
  Controls100 (two decidability fixes for bounded quantifiers); 03:52 Audit100 PASS; ControlFail100 fails as
  required.
- 03:54-03:56 `audit_binding.py` (one control-design fix: the recorded seed SHA moved into check 3) and `replay.py`;
  03:56:37 `manifest.json`; 03:56:40-04:01:56 clean replay PASS; about 04:03 Main notified.
- 04:03:10 README cycle-2 section written; evidence/MANIFEST-cycle2.sha256 generated next (last write of cycle 2).
