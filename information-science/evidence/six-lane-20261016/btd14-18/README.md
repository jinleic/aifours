# Lane info-2 (second target): existence of BTD(14,18;7,1,9;7,4)

Owner: worker `InfoCyclic100`. Contract (read-only; copied with SHA to `sources/contract-info-2-btd14-18.json`):
`institute/runs/six-lane-2026-10-16/screening/info-2-btd14-18-contract.json`, sha256
739dd45f3c731d6a5ebd5eb194746825be14bf9833a5cdce75b2b523a65431ba, recorded 2026-10-17 09:24:02 PDT. Lane opened
2026-10-17 09:25:05 PDT (`notes/lane-opened.txt`). Deadline 2026-10-18 18:31:43 PDT.

Only this lane is writable. The btd12-15 lane and all review inputs are read-only; tools from btd12-15 are copied
here with SHA-256 (`notes/copied-from-btd12-15.sha256`), never moved. No deletion, no overwrite, no /tmp, no commit,
no publication, no SIGKILL, no subprocess.run(timeout=...). No novelty, priority or "first" claim; a literature miss
is not novelty.

## 1. Frozen plan (written 2026-10-17 09:25 PDT, BEFORE any computation on this target)

### 1.1 Object (contract definition)
* M is a 14 x 18 matrix over {0,1,2} (rows = V = 14 elements, columns = B = 18 blocks).
* Every row has exactly seven 1s and exactly one 2 (so ten 0s, row sum R = 9, squared row norm 11).
* Every column sums to K = 7.
* Distinct rows have inner product Lambda = 4. Equivalently M M^T = 7I + 4J together with the row compositions.
* Repeated columns are allowed (simplicity is NOT imposed), and no automorphism, cyclicity or orbit assumption is
  made.
* Necessary conditions: VR = 126 = BK; Lambda(V-1) = 52 = rho1(K-1) + 2 rho2(K-2) = 42 + 10.

### 1.2 Sources
* Status: Rosin arXiv:2501.17725v1 Table 1 (pinned layout text, line 94) lists "(14,18;7,1,9;7,4)?" among the
  Handbook's smallest open instances with no progress. Rosin arXiv:2505.23881v1 Table 1(a) does not solve it. The
  CPro1 definition file lists it first in OPEN_INSTANCES.
* Definition: Francel-Hurd 2008, pp.3-5, as in btd12-15.
* Parent pins copied to `sources/parent-screen-*` with SHA-256 equal to the parent manifest.
* No further status search is planned: the contract records the parent's bounded check. A miss is not novelty.

### 1.3 Representation, symmetry, implied constraints (completeness arguments as in btd12-15 README 1.3-1.4)
* (S0) Row 0 is 0^10 1^7 2^1. This is complete by column permutation.
* (S1) Double-lex: rows and columns are lexicographically nondecreasing over 0 < 1 < 2. Completeness is the
  min-flattening argument of btd12-15 README 1.3, and S1 implies S0. Used only in the plain SAT encodings.
* Implied (proved before use, in `notes/` before any run that uses it):
  * (T1) Every column has at most one 2.
    * Proof sketch: G = M^T M, G^2 = 7G + 196J and GJ = 63J. H := 63I - 9G + 28J satisfies H^2 = 63H, so
      63 H_jj = sum_k H_jk^2 >= 0.
    * A column with t twos has H_jj = 28 - 18t, so t <= 1.
  * T1 appears only in "strengthened" witness-search variants, which are clearly labelled. A strengthened miss is
    never an exclusion.
* No other symmetry or pruning assumption anywhere.

### 1.4 Two parallel directions (contract first obligations)
* (a) Proof route (Connor/Gram method, parent lead untrusted):
  * write a candidate proof in `notes/` with an exact stdlib checker in `code/` (integers and Fraction only);
  * if it closes, repeat the btd12-15 Lean pipeline in `lean-kernel/` of this lane: explicit unrestricted root,
    only propext / Classical.choice / Quot.sound, no sorry / native_decide / ofReduceBool, a source scan, a negative
    control, and a fresh kernel replay.
* (b) Witness search, unrestricted, with native limits:
  * CP-SAT model with (S0), plain and (T1)-strengthened, <= 2 workers, `max_time_in_seconds` <= 3600 per run;
  * kissat on CNF encoding A (thermometer, S1) without proof, as a witness search only (`--time` <= 3600).

  A heuristic or solver miss, a timeout, or a solver UNSAT without a checked proof is UNKNOWN, never an exclusion.
  Exclusion comes only from route (a) with Lean, or from a checked DRAT over a proved-complete encoding.

### 1.5 Checkers and controls
* `code/verify_btd.py` (stdlib, definition-first) and `code/btd_check.c` (native) are copied unchanged.
* They are re-run on this lane's controls:
  * BTD(3,3;1,1,3;3,2);
  * published CPro1 BTDs;
  * intended-reason mutations;
  * BTD 14 18 7 1 9 7 4 parameter binding.
* Witness format: `BTD 14 18 7 1 9 7 4`, then 14 lines of 18 entries, final LF.

### 1.6 Stop rules and resources
* On ANY witness: stop all searches, verify it with both checkers, pin it under `certs/` with its SHA-256, and message
  Main immediately.
* On a closed proof: message Main with the SHA before starting the Lean work.
* At most 4 CPU in total: CP-SAT 2 workers + kissat 1 + 1 slot for the proof work, the Lean builds and the checkers.
  <= 8 GiB, <= 10 GiB new data, checkpoints <= 30 min, initial assay <= 3 h (to about 12:30 PDT), native limits only.

## 2. Status
(below the freeze only; updated 10:07 PDT)
* PARENT VERDICT (message received 10:05-10:06): GATE MET (nonexistence), parent Lean replay PASS; verdict file
  `institute/runs/six-lane-2026-10-16/review/btd14-18-parent-verdict.md`. The lines below are the worker-side record.
* Candidate nonexistence proof: `notes/nonexistence-proof-r1.md` (fd508ffb…87c0f, pinned by the parent for review)
  and its editorial revision `notes/nonexistence-proof-r2.md` (8769c218…a847; delta
  `notes/nonexistence-proof-r1-to-r2.diff`). Same mathematics: Gram matrix H = 63I - 9G + 28J, column types, entries
  {-8, 1, 10} next to type-1 columns, lemmas (E) and (F), Lemma D4 (729 det(N)^2 = 7^10 det H[S]), closure by a
  column sum of 36 against 0.
* Exact stdlib checker `code/proof_check.py` (3436337c…daac): PROOF-CHECK PASS (`evidence/proof-check-v1.json`).
* Parent-side reviews of r1 (files under `institute/runs/six-lane-2026-10-16/review/`, as reported by the parent):
  gpt-6.1-sol (Codex CLI) hostile review ACCEPT with no findings; claude-opus-5-5 (Claude CLI) complete review ACCEPT
  with five editorial minors, which r2 applies.
* Lean 4 kernel proof (`lean-kernel/`, manifest ffdbc4c2…1305): clean replay r01 VERDICT PASS; root
  `BTD14.Audit.root` is the explicit unrestricted 14 x 18 statement; axioms [propext, Classical.choice, Quot.sound];
  `leanchecker --fresh` exit 0 on Audit and Controls. Parent fresh-kernel replay and parent literal binding pending.
* Status: CANDIDATE nonexistence, pending the parent's verdict. Not promoted by this worker.
* Witness searches (independent route, unrestricted; a miss is UNKNOWN): CP-SAT plain S0 and kissat on encoding A
  plain S1, 3600 s native limits from 09:31:13. Declared moot by the parent after the verdict and stopped by SIGTERM
  at 10:06:10; both exited by 10:06:16. Both UNKNOWN (no witness).

## 3. Log (host clock, PDT)
- 09:24:24 contract read; its SHA-256 matches the parent message. 09:25:05 lane created; tools and pins copied.
- 09:25:40 first freeze receipt. 09:25:52 receipt r2, a wording-only repair of the README header (a misplaced edit
  had dropped a line); the plan text is unchanged (`notes/freeze-receipt.txt`).
- 09:26:00-09:26:01 checker controls with the copied tools (`controls/checkers-v1/`): CHECKER-CONTROLS PASS.
  `bin/btd_check` 3f8c148e…3ba1; `bin/btd_cnf_b` compiled. `tools/pydeps312` copied (132 MB).
- Closing record for the btd12-15 lane, read-only from here (its driver wrote its own receipt): A-plain level 1,
  kissat `--time=3600` with binary DRAT, ended at 09:30:42 with status UNKNOWN at 3600.065 s. Partial proof
  3800655532 bytes compressed, sha256 de29adac1b35cedd4b6187eec4fb2c432295b822d91421c5f2696e3bae323d68. Not a
  certificate. Per the parent, drat-trim is not run on it.
- 09:31:13 witness searches started:
  - CP-SAT plain (S0), 2 workers, 3600 s, seed 0 (`runs/cpsat-v1/`);
  - kissat on encoding A plain S1 (`runs/encA-v1/A-plain-S1.cnf`, 45602 vars, 167917 clauses, sha256 0fc9f65d…0899),
    `--time=3600`, no proof, as a witness search only.
- 09:26-09:32 candidate proof `notes/nonexistence-proof-r1.md` (sha256
  fd508ffbf77d7777e24f5b743589cab34ac17564d30654d471cf048d72287c0f).
  - From the definition: H = 63I - 9G + 28J with H^2 = 63H and H1 = 0, positivity from 63 x^T H x = |Hx|^2, so
    c_j <= 1, giving 14 type-1 and 4 type-0 columns.
  - A type-1 row has exactly two entries 10 and five entries -8. Lemmas (E) (equal H-columns) and (F) (no -8 to two
    columns in distinct classes).
  - Lemma D4: 729 det(N)^2 = 7^10 det H[S] for |S| = 4.
  - Closure: a type-1 pair (a, b) with H_ab = -8. Every type-1 c has H_ca + H_cb = 2. A type-0 c has
    H_ca + H_cb in {-7, 2}, and -7 is killed by Lemma D4 on {a, b, u, c} (det 3645 or -2187). So the sum over all
    18 columns is 36, against the zero row sums.
  - No rank argument and no configuration count are needed.
- 09:32:52 `code/proof_check.py` (3436337c…daac) gave PROOF-CHECK PASS; receipt `evidence/proof-check-v1.json`
  (22277a8a…8725). It covers R1-R10, including the six 4x4 determinants (3645, -2187).
- 09:3x parent: r1 pinned for independent reviews, not yet promoted; Lean authorised (<= 3 h, 1 CPU, one thread while
  the two searches run). Later parent note: a Codex hostile review returned ACCEPT with no findings, the parent's own
  exact arithmetic passed and the pinned checker replayed byte-identically (parent files under `review/`); r1 stays
  frozen.
- 09:34-09:41 Lean formalization of r1 in `lean-kernel/` (adapted from the btd12-15 package; one Lean process, one
  thread). Modules Target, Proof, Audit, Controls, ControlFail; scanner clean. Dev rounds 01-05 compiled
  (round 01 = Steps 1-5 first try; 02-04 fixed Lemma D4 heartbeats, the 4x4 determinant polynomial and two case
  tactics), dev build directories retired to `lean-kernel/archive/dev-builds-20261017/`. Root `BTD14.Audit.root`
  states the explicit 14 x 18 matrix nonexistence; `#print axioms` = [propext, Classical.choice, Quot.sound].
  ControlFail fails for the intended reasons. 09:41:30 `manifest.json` (ffdbc4c2…1305); clean replay `r01` started.
- 09:42-09:44 parent forwarded the claude-opus-5-5 complete review of r1 (ACCEPT, no fatal or major finding, five
  editorial minors) and asked for a small editorial r2. `notes/nonexistence-proof-r2.md` written 09:44:51, sha256
  8769c218ca6ccd80beddbd2b13b2fb189095b513db9dc70dcc1a9a14c948a847; r1 unchanged. Delta
  `notes/nonexistence-proof-r1-to-r2.diff` (7acfea37…7e5c): exactly the five clarifications (g_jk defined; column
  permutation for M = [N | P]; J/1 sizes; Step 6 heading = the exact identity 729 det(N)^2 = 7^10 det H[S]; Sylvester's
  rank-4 identity and det(N N^T) = det(N)^2 named), plus title, Status and a change map. No arithmetic change. Two
  pre-send drafts (wrong review path; a wording slip) retired unchanged to `archive/notes-r2-draft-0943/` and
  `archive/notes-r2-draft-0944/`. SHA and delta sent to the parent.
- 09:41:33-09:51:14 Lean clean replay `lean-kernel/replay-r01/`: VERDICT PASS, all 14 checks
  (`result.json` 2ef82bdd9abbf9a98f3987ac241d558c7580c8677c67c02a25e94a9c03d8b457). Pins match; scan clean; Target,
  Proof, Controls, Audit build with no error; root `BTD14.Audit.root` is the explicit 14 x 18 statement and depends on
  [propext, Classical.choice, Quot.sound] only; ControlFail fails for the intended reasons with no olean;
  `leanchecker --fresh -v` exits 0 on BTDKernel.Audit (285.8 s, peak RSS 3.51 GB) and BTDKernel.Controls (277.9 s,
  3.51 GB). Sources: Target 3f650f4e…4df6, Proof 3ba7057c…292d, Audit ff151704…9478, Controls 991ab196…dd24,
  ControlFail 5b9434fe…3e16, replay.py 3faaad5d…6119. Reported to the parent.
- 10:05-10:06 parent message: BTD(14,18) VERDICT GATE MET (nonexistence); parent Lean replay PASS
  (`review/btd14-18-lean-parent-replay-v1/parent-result.json`); r2 diff confirmed editorial-only. The witness searches
  are moot; the parent allowed SIGTERM. A new target (BTD(12,20;4,3,10;6,4), lane `btd12-20/`) was opened by the parent.
- 10:06:10 SIGTERM sent to the CP-SAT driver (pid 63349) and to kissat (pid 63354); bounded wait: both gone by
  10:06:16 (no SIGKILL).
  - CP-SAT plain S0, 2 workers: killed before its native limit, so no record JSON was written; its log
    `runs/cpsat-v1/plain-s0-w2-seed0.log` (last progress line at 702 s) and the absence of any `.btd` file show no
    solution. Status UNKNOWN.
  - kissat A-plain S1: driver record `runs/encA-v1/kissat-plain-noproof.json` (returncode -15, status UNKNOWN,
    2096.676 s). kissat's self-reported maximum RSS line uses the wrong unit on macOS and is not a measurement.
