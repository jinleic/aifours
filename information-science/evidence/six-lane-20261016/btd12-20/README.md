# Lane info-2 (third target): existence of BTD(12,20;4,3,10;6,4)

Owner: worker `InfoCyclic100`. Contract (read-only; copied with SHA to `sources/contract-info-2-btd12-20.json`):
`institute/runs/six-lane-2026-10-16/screening/info-2-btd12-20-contract.json`, sha256
dd24495954bb300c1c1bf7a652a351200400bdc450d4436df1db67bc34995561, recorded 2026-10-17 10:05:37 PDT. Lane opened
2026-10-17 10:10:26 PDT (`notes/lane-opened.txt`). Deadline 2026-10-18 18:31:43 PDT.

Only this lane is writable. The btd12-15 and btd14-18 lanes and all review inputs are read-only; tools are copied
here with SHA-256 (`notes/copied-from-btd14-18.sha256`), never moved. No deletion, no overwrite, no /tmp, no commit,
no publication, no SIGKILL, no subprocess.run(timeout=...). No novelty, priority or "first" claim; a literature miss
is not novelty.

## 1. Frozen plan (written 2026-10-17 10:10:45-10:11:41 PDT, BEFORE any computation on this target)

### 1.1 Object (contract definition)
* M is a 12 x 20 matrix over {0,1,2} (rows = V = 12 elements, columns = B = 20 blocks).
* Every row has exactly four 1s and exactly three 2s (so thirteen 0s, row sum R = 10, squared row norm 16).
* Every column sums to K = 6.
* Distinct rows have inner product Lambda = 4. Equivalently M M^T = 12I + 4J together with the row compositions.
* Repeated columns are allowed (simplicity is NOT imposed); no automorphism, cyclicity, orbit, column-type or
  resolvability assumption.
* Necessary conditions: VR = 120 = BK; Lambda(V-1) = 44 = rho1(K-1) + 2 rho2(K-2) = 20 + 24.

### 1.2 Sources
* Status: Rosin arXiv:2501.17725v1 Table 1 (pinned layout text, line 96) lists "(12,20;4,3,10;6,4)?" without an
  "Exists" mark; arXiv:2505.23881v1 Table 1(a) does not solve it; the CPro1 definition file (line 16) lists
  [12,20,4,3,10,6,4] in OPEN_INSTANCES. No further status search is planned (the contract records the parent's
  bounded check). A miss is not novelty.
* Definition: Francel-Hurd 2008, pp.3-5, as in btd12-15 (pinned layout text copied).
* The parent lead cites Elkies-Kominers arXiv:0902.1942v1 Section 1.1 (irreducible tetrad codes are d_2k (k >= 2),
  e7, e8). It is not pinned in this lane. It will be used only after a pinned copy has been read here; otherwise every
  structural statement is proved from the definition in `notes/`, or replaced by an exact enumeration with a written
  completeness argument.

### 1.3 Representation, symmetry, implied constraints
* Write M = A + 2D with A, D the 0/1 indicator matrices of the entries 1 and 2 (disjoint supports; row i: |A_i| = 4,
  |D_i| = 3). Column j: a_j ones and d_j twos with a_j + 2 d_j = 6.
* (S0) Row 0 is 0^13 1^4 2^3 in this order. Complete by column permutation.
* (S1) Double-lex over 0 < 1 < 2 (rows and columns lexicographically nondecreasing). Completeness is the
  min-flattening argument of btd12-15 README 1.3 (the conditions are invariant under row and column permutations),
  and S1 implies S0. Used only in the plain SAT encodings.
* Implied facts, each proved in `notes/` before any run that uses it:
  * (I1) |A_i cap A_k| is even (inner product 4 is even and the D-terms are even), so it is 0, 2 or 4.
  * (I2) a_j is even (a_j = 6 - 2 d_j), so (a_j, d_j) is (0,3), (2,2), (4,1) or (6,0).
  * (I3) With x = |A_i cap A_k|, y = |A_i cap D_k| + |D_i cap A_k|, z = |D_i cap D_k|, the pair condition is
    x + 2y + 4z = 4, i.e. (x,y,z) is (4,0,0), (2,1,0), (0,2,0) or (0,0,1).
  * Gram facts (H := 12I - M^T M + (12/5) J satisfies H^2 = 12H, H 1 = 0, H_jj = a_j + 12/5, so H is positive
    semidefinite of rank 8) only after a written proof in `notes/`.
* Implied facts are used only in clearly labelled "strengthened" variants. A strengthened miss is never an exclusion.
* Restricted (structured) searches fix part of the structure, for example the A-pattern to one tetrad configuration.
  They are labelled RESTRICTED. A restricted miss or restricted UNSAT is never an exclusion.
* No other symmetry or pruning assumption anywhere.

### 1.4 Two parallel directions (contract first obligations)
* (a) Structure route (nonexistence or existence by structure):
  * classify the possible A-patterns (12 x 20 0/1 matrices with row weight 4, pairwise even row intersections and
    column weights in {0, 2, 4, 6}) up to row and column permutations, either by a written argument (tetrad codes)
    or by an exact orderly enumeration with a written completeness argument and an independent cross-check;
  * for each A-class decide the D-completion problem exactly (written argument, or SAT with a checked DRAT/LRAT
    proof for every UNSAT case; a CP-SAT INFEASIBLE alone is information only);
  * a complete case split is a candidate only; machine-checked proof per contract (Lean or checked DRAT/LRAT over a
    proved-complete encoding) before any exclusion claim.
* (b) Witness search, unrestricted, native limits:
  * CP-SAT model `code/btd_cpsat.py` with (S0), plain, 2 workers, `max_time_in_seconds` <= 3600 per run;
  * kissat on CNF encoding A plain (S1, `code/btd_cnf_a.py`) without proof (`--time` <= 3600), witness search only;
  * RESTRICTED structured CP-SAT searches (A fixed to a tetrad configuration), 1 worker, when a CPU is free.

  A heuristic or solver miss, a timeout, or a solver UNSAT without a checked proof is UNKNOWN, never an exclusion.

### 1.5 Checkers and controls
* `code/verify_btd.py` (stdlib, definition-first) and `code/btd_check.c` (native) are copied unchanged.
* `code/checker_controls_v2.py` = the copied `checker_controls.py` with only the parameter-binding control retargeted
  to `BTD 12 20 4 3 10 6 4`. It re-runs: BTD(3,3;1,1,3;3,2); published CPro1 BTDs; intended-reason mutations; the
  binding control.
* Witness format: `BTD 12 20 4 3 10 6 4`, then 12 lines of 20 entries, final LF.

### 1.6 Stop rules and resources
* On ANY witness: stop all searches, verify it with both checkers, pin it under `certs/` with its SHA-256, and
  message Main immediately.
* On a closed case split or proof: message Main with the SHA before starting machine-checked work.
* At most 4 CPU in total: CP-SAT 2 workers + kissat 1 + 1 slot for the structure route, restricted searches and
  checkers. <= 8 GiB, <= 10 GiB new data, checkpoints <= 30 min, initial assay <= 3 h (to about 13:15 PDT), native
  limits or SIGTERM plus bounded wait only.

## 2. Status
(below the freeze only; updated 11:06 PDT)
* PARENT VERDICT (message received 11:04-11:05): GATE MET (nonexistence, computer-assisted), on `notes/case-split-r2.md`
  and its frozen manifest; parent byte-identical replay PASS with 3073/3073 drat-trim VERIFIED; verdict file
  `institute/runs/six-lane-2026-10-16/review/btd12-20-parent-verdict.md`, dispositions
  `review/btd12-20-review-dispositions.json`. The lines below are the worker-side record.
* Case split: `notes/case-split-r1.md` (d405956c…4da2), `notes/case-split-r2.md` (6ef1e73b…e34f), editorial
  `notes/case-split-r3.md` (4c1935c6…291a; no change to mathematics, code or certificates).
* Certificates: all 3073 completion CNFs UNSAT by kissat with binary DRAT proofs verified by drat-trim
  (`runs/cert-v1/`); manifest `evidence/case-split-manifest-v1.json` (054be2d4…45da); worker replay r01 PASS.
* Witness searches (unrestricted; a miss is UNKNOWN): both stopped after the verdict, both UNKNOWN (see log 11:05).

## 3. Log (host clock, PDT)
- 10:05-10:06 parent message opened this target; contract read; its SHA-256 matches the parent message. 10:10:26
  lane created; tools and pins copied (`notes/copied-from-btd14-18.sha256`); `bin/btd_check` (3f8c148e…3ba1) and
  `bin/btd_cnf_b` (08c841e1…a6a0) compiled with `cc -O2`, byte-identical to the btd14-18 binaries.
- 10:12:02 freeze receipt (`notes/freeze-receipt.txt`, README sha256 af918b96…2ada). 10:12:02-10:12:03
  `code/checker_controls_v2.py` (d5a7008e…daf6) into `controls/checkers-v1/`: CHECKER-CONTROLS PASS (binding control
  rejects a valid BTD(12,16) under `--expect 12 20 4 3 10 6 4`).
- 10:12:16-10:12:20 witness searches started (native limits, 3 CPU):
  - CP-SAT plain (S0), 2 workers, 3600 s, seed 0 (`runs/cpsat-v1/plain-s0-w2-seed0`);
  - kissat on encoding A plain S1 (`runs/encA-v1/A-plain-S1.cnf`, 37778 vars, 139290 clauses, sha256
    8c233e30…92e6), `--time=3600`, no proof.
- 10:14-10:25 structure route, exploratory and RESTRICTED (1 CPU). `code/restricted_afix.py` /
  `code/restricted_batch.py` fix the 1-pattern A and let CP-SAT (1 worker) decide the 2-pattern D. Information only.
  - Five hand-built d-type patterns (octahedron, C6 doubled, K4 doubled, two triangles doubled, K5 plus a double
    edge): all INFEASIBLE in < 0.02 s.
  - 10:16:59 pinned `sources/elkies-kominers-0902.1942v1.pdf` (sha256 a6ed9ca0…47b2). Its Section 1.1 states that the
    irreducible tetrad codes are exactly d_2k (k >= 2), e7, e8, citing Koch (ICM 1986); no proof is given there.
  - d-type patterns (every row a union of two column pairs, i.e. a multigraph whose edges are the rows): nauty 2.9.3
    (`geng -q -d1 -D6 n 1:12 | multig -q -e12 -D6 -T`, then `code/mg_filter.py` keeps degrees in {2,4,6}) gives
    2069 multigraphs for n = 4..10 vertices (7, 59, 312, 550, 616, 352, 173). CP-SAT: all 2069 INFEASIBLE
    (`runs/mg-v1/res-n*.jsonl`).
  - e-type components: `code/e_multisets.py` gives 29 e7 and 216 e8 tetrad multisets with point degrees in
    {0,2,4,6}, up to the groups of order 168 and 1344 (`runs/e-v1/e-multisets.json`). `code/e_combos.py` builds 1004
    A-patterns with one or two full-support e-components plus a d-type part (`runs/e-v1/e-combos-v2.jsonl`; a first
    run that stopped on a geng edge-range error left a partial file, retired unchanged to
    `archive/e-combos-failed-1023/`). Batch running from 10:25.
  - None of this is an exclusion: completeness of the pattern list needs a written argument (the tetrad-code
    classification) and every infeasibility needs an independent certificate.
- 10:25:17-10:29:14 e-combo batch: all 1004 INFEASIBLE (CP-SAT, information only; slowest 26.8 s).
- 10:30-10:33 candidate case split `notes/case-split-r1.md` (sha256
  d405956c09917073fa7a9c31347eef8ce9729bfb70158d39a946f329fccd4da2; an unsent draft with a wrong "exactly one" in
  Lemma T is retired unchanged to `archive/notes-case-split-draft-1035/`): Lemma T (connected tetrad families are
  d-type or inside e7/e8, self-contained proof), the case list E0 (2069) + E1 (1004) = 3073, CP-SAT evidence, and a
  certification plan. SHA sent to the parent. The parent pinned r1 and started structural reviews; it asked for
  every case certified with full coverage, carried multiplicities and zero columns, independent enumeration
  cross-checks, documented tools, and a frozen manifest for its replay.
- 10:30-10:35 encoding tests (`runs/cert-test-v1/`): encoding A plus A-fixing clauses is UNSAT with a 2.7 MB proof per
  case; the dedicated completion encoding `code/dcomp_cnf.py` (2e7d68b4…6d3) gives about 7k variables, 25k clauses
  and about 0.13 MB of proof per case. kissat cannot read zstd input; plain files are kept (no scratch overwrites).
  `bin/drat-trim` and `bin/lrat-check` compiled from the pinned upstream source, byte-identical to btd12-15.
- 10:36:37-10:36:42 `code/dcomp_controls.py` (c80bd181…24fb): DCOMP-CONTROLS PASS (`controls/dcomp-v1/`): six
  published BTDs complete to SAT and decode to matrices accepted by both checkers; a column-parity mutation gives the
  empty clause and UNSAT; brute-force and CNF completion counts agree (27 and 60 one-patterns).
- 10:37:24-10:42:27 certificates (`code/cert_run.py`, `runs/cert-v1/`): all 3073 cases CERTIFIED (kissat UNSAT,
  max 1.09 s; drat-trim `s VERIFIED` exit 0, max 0.83 s; 666 MB of proofs, 1.8 GB with CNFs); case indices 0..3072
  each covered once. Case list `runs/cases-v1/cases.jsonl` (4a6aedb8…ad5f).
- 10:42:32 `code/tetrad_facts.py`: TETRAD-FACTS PASS (`evidence/tetrad-facts-v1.json`). 10:42:46-10:42:55
  `code/enum_crosscheck.py`: ENUM-CROSSCHECK PASS (`evidence/enum-crosscheck-v1.json`): nauty genbg counts equal the
  geng | multig counts for every (n, e) used (E0 2069, E1 1004); Burnside orbit counts 29 / 17 (e7) and 216 / 187
  (e8) equal the lists.
- 10:43-10:46 `notes/case-split-r2.md` (r1 unchanged): Part E results, the "Carried data" paragraph (row multiplicities,
  zero columns, overlaps, labels) and the tool table. Two unsent drafts retired unchanged
  (`archive/notes-case-split-r2-draft-1044/`, `-1045/`). Final r2 sha256
  6ef1e73b7e5e2b771cae6c2522d15837cc24ba36d4926d3d77e1b6bfc667e34f; diff `notes/case-split-r1-to-r2.diff`
  (4912733b…88dd8).
- 10:46 `code/case_split_replay.py --write-manifest` (`evidence/case-split-manifest-v1.json`), then replay r01
  started (regeneration, cross-checks, controls, CNF rebuild and drat-trim on every stored proof).
- 10:46:09-10:49:55 case-split replay r01: VERDICT PASS (18 checks: pins, byte-identical regeneration of the mg lists,
  e-multisets, e-combos and cases, facts, cross-check, controls, coverage, CNF rebuild for all 3073 cases, drat-trim
  on all 3073 stored proofs). Manifest 054be2d4…45da; result e2d62edc…edf9. Reported to the parent.
- 11:04-11:05 parent message: BTD(12,20) VERDICT GATE MET (nonexistence, computer-assisted); witness searches may be
  stopped; optional editorial r3; new target BTD(14,28;8,3,14;7,6) in lane `btd14-28/`.
- 11:05:12 SIGTERM sent to kissat (pid 78464); the CP-SAT driver (pid 78460) and the kissat driver (pid 78463) were
  already gone at that moment, and neither had written its record JSON (cause not determined; not stopped by this
  worker; the CP-SAT log stops after its header at 10:12, no `.btd` file exists). kissat logged `caught signal 15`
  after 3169.82 s of process time with no `s` line. Both searches: UNKNOWN, no witness.
- 11:06:35 `notes/case-split-r3.md` (4c1935c6e8536bee61900b3491a69c0aa776ed21e8ab8eb915da59036d43291a), editorial
  only; delta `notes/case-split-r2-to-r3.diff` (0888a678…ddc0). r1 and r2 unchanged.
