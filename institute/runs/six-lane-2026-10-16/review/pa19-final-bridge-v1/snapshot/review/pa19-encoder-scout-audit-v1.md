# PA19EncoderAudit (read-only scout report, verbatim)

Recorded 2026-10-17 12:38:58 PDT. Static audit; hashes quoted by the scout were worker-recorded, not independently computed. Subsequent worker fixes are not part of this snapshot.

I couldn't certify any verdict here, and PA(19,8,6) is still undecided (overall UNKNOWN). Reading the code, the M1 and M2 encoders look sound and their symmetry breaking doesn't exclude real completions. The blocking problem is the checker. The lane's `lrat-check`, read line by line, accepts an empty-clause LRAT step that never reaches a conflict. That means every result checked only by CaDiCaL plus `lrat-check` is not yet certified. The kissat results are not affected, because drat-trim refuses to verify without a real conflict.

Everything below is static reading. I ran nothing and computed no hashes. The hashes I quote come from lane manifests and records. Tags: **[OBS]** = I read the file; **[CODE]** = my conclusion from reading code; **[CLAIM]** = the worker says so but I found no receipt.

LANE = `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19`. `README.md`, `STATUS3.json` and `cycle2/proofstream/` change while I read them. `README.md:262` was edited during this audit. I found no earlier parent audit of the encoders. The only earlier parent PA19 notes are the SIGKILL/containment entries at `institute/runs/six-lane-2026-10-16/checkpoints.md:280,289,395`.

## (1) Code and data map of the real production paths

Live counts from `STATUS3.json` [OBS]: M1 has decided 4504 of 5577 cases (a 2490, b 1894, c 60, d 30, e 30) and 1073 are open. M2 has decided 0 of 5577. The balanced multiset ms00 (E0, 486 cases) is UNSAT in both pipelines, copied from `STATUS.json`.

| Path | Enumerator / input | Encoder | Solver → checker | Runner | Records |
|---|---|---|---|---|---|
| E0, M1 | `data/quadgraphs-8v-13to16e-D4.g6` (`68760273…56d8c`) | `src/encode_q0.py` (`8d2840f4…9299`) | kissat DRAT file → drat-trim `-t 50000` → LRAT file → lrat-check | `run_cases.py` (`c32de708…`), `check_proofs.py` (`69c5b76d…`) | `cases19q0/results/*.json`, `*.check.json`; proofs in `cases19q0/proof` |
| E0, M2' | same `.g6` | `src/encode_q0b.py` (`3c431849…e24d`) | CaDiCaL LRAT file → **lrat-check only** | `run_m2.py` (`fd6ffed6…`) | `m2q0b/{cnf,proof,results}` |
| Pass 1 (5577 cases) | `gen_skel.py` → `skeletons/*.json` (SHAs in manifest) → `gen_skel_cases.py` → `cases19skel/specs` | `src/encode_skel.py` (`0783c3ea…dc3a`) plus `encode_e1.py` (`2a76e8bd…6b830`) | kissat for 30 s, no proof | `run_cases.py` | `cases19skel/results/<tag>.json` (`cnf_sha256`), CNFs in `cnf/` |
| a (2490) | stored pass-1 CNF | — | kissat `-q --seed=1` → DRAT file → drat-trim → LRAT FIFO → lrat-check | `run_proofpass.py` (`f2f29167…`) | `cases19skel/proofcheck/*.json`, DRATs in `cases19skel/proof/*.drat` |
| b (1894, growing) | stored CNF; SHA must equal pass 1 (`run_proofpass_stream4.py:34-35`) | — | kissat `-q -f --seed=1 --time=600` → drat-trim `-i -t 1800` → lrat-check, all streamed | `run_proofpass_stream4.py`, `stream_check4.py:121-182` | `cycle2/proofstream/*.json` |
| c (60, all ms06) | `encode_skel` CNF rebuilt in memory, SHA must equal pass 1 (`run_hard5.py:78-79`) | `encode_skel.py` | CaDiCaL `--lrat` → **lrat-check only** (`stream_check4.py:185-231`; 21 runs used revision 1, `stream_check.py:181`) | `run_hard.py`, `run_hard4.py`, `run_hard5.py directc` | `cycle2/hard/*.json` (62 files) |
| d (30, ms01) | `extend_p1.py` (networkx 3.7, venv) → `a3/<tag>/ext.json` (`run_hard4.py:91`) | `encode_full.py` | kissat → drat-trim → lrat-check; one CaDiCaL rerun (`f01788_r2`) | `run_hard4.py a3`, `rerun_unknown.py:54` | `cycle2/a3/<tag>/*` |
| e (30, ms09) | `extend_p1q.py`, m=1 (`run_hard5.py:97`, `run_hard7.py:69`) | `encode_partq.py` (singles), `encode_partbatch.py` (batches of 100) | kissat → drat-trim → lrat-check; one CaDiCaL batch rerun (`batch_04300_04399_r2`) | `run_hard5.py part`, `run_hard6.py`/`run_hard7.py` | `cycle2/part/<tag>/*` |
| M2 generator | `gen_skel_b.py` (nauty genbg `-Z1`), checked by `compare_skel.py`: bijection for all 9 multisets [OBS] | — | — | — | `cycle2/skel-b/*` |
| M2 direct (planned) | — | `encode_skel_b.build_v2` (`encode_skel_b.py:503`) | CaDiCaL → **lrat-check only** | `run_m2skel5.py:41` | `cycle2/m2skel_v2/` (absent) |
| M2 split (planned) | `extend_b.py` | `build_part` (`:256`), `build_partbatch` (`:382`) | CaDiCaL → **lrat-check only** | `run_m2part.py`, `run_m2partbatch.py` | `cycle2/m2part/` (absent) |
| Aggregation | — | — | — | `summarize3.py` | `STATUS3.json` |

- **Tools [OBS]:** `tools/drat-trim/drat-trim.c` (`d834b649…c2ee`) and `lrat-check.c` (`bf07c2ac…8f95`) come from upstream commit `2e3b2dc0…a985` (`COMMIT.txt`).
- **Binaries with no recorded hash or build flags:** the lane's `drat-trim`, `lrat-check` and `bin/verify_pa2`.
- **Solvers** are system Homebrew binaries (`stream_check4.py:32-35`). The Cellar holds kissat 4.0.4, cadical 3.0.1 and nauty 2.9.3 [OBS], but no hashes are recorded.
- **Source manifests:** the only one is `SHA256SUMS-cycle1.txt`. No cycle-2 source file has a recorded hash (the stream_check, run_hard, extend, encode_full/partq/partbatch, encode_skel_b, gen_skel_b, compare_skel, run_m2 and summarize3 scripts).

**What I checked in the encoders [CODE]:**
- **Necessary conditions:** every constraint family holds for any valid completion. This covers the one-symbol-per-cell clauses, fixed P0 quads, exact counts, row-pair at-most-one agreement (M1) and column-pair 4-clauses (M2). It also covers the row budget `18-L ≤ Σ(n−1) ≤ 18` (`encode_skel.py:67-69`), at most L non-agreeing pairs (`:83`), the M2 per-row identity, the `encode_full` leave degrees (`:43-44`, `:83-84`), and the exclusions in fixed columns.
- **Cardinality encodings:** the sequential counter (`encode_e1.py:44-67`), the weighted counter (`:69-93`) and the totalizer (`encode_skel_b.py:40`) are correct. Literals are repeated only on purpose, as M2 totalizer weights. The empty clauses at `encode_skel_b.py:138,574` are emitted only when the identity is impossible.
- **Symmetry breaking:** value precedence, row lex and column lex are lex-leader constraints for one shared row-major order. In the partial and full encoders, the non-adjacent row-lex pairs are lex-leaders for those transpositions too. M2 v1's P0 label fixing is an independent relabelling within each column, and v1 has no row lex. M2 v2 correctly replaced that fixing with first-occurrence ordering.
- **Batch encoders:** each batch CNF is UNSAT exactly when every one of its placements is UNSAT.
- **Placement enumerators:** `extend_b` and `extend_p1q` use the same necessary conditions and valid orbit reductions.

## (2) Defects and gaps

**FATAL for certification (remediable; does not show any verdict is wrong)**

**F1. lrat-check accepts an empty clause without a conflict [CODE].** In `lrat-check.c` the trace is:
1. For a size-0 lemma, `pivot = convertLit(0) = 0` (`:137`).
2. With no hints, or hints that never conflict, `checkRedundancy` returns SUCCESS (`:89`, `:129-131`).
3. With no RAT hints, `start = intro[1]` (`:158`). `intro[1]` is never written (`:237`, `:337`), so it stays 0.
4. The branch at `:160-164` therefore returns SUCCESS. The guard "No RAT and no conflict is FAILED" is commented out at `:161`.
5. The lemma sets `found_empty_clause` (`:479`) and the run prints `c VERIFIED` (`:489-490`).

So a satisfiable CNF with the one-line LRAT `2 0 0` should verify. Separately, hint IDs are not bounds-checked (`:70-73`).

Affected records:
- all 60 path-c cases;
- `ms01_s03171` and `ms09_s00010`, through their CaDiCaL reruns;
- the 486 E0 M2' cases;
- every planned M2 result.

Not affected: the kissat paths a, b, d and e. drat-trim requires a real conflict (`drat-trim.c:874-875`, `:1480-1483`).

**MAJOR**
- **Missing control receipts.** No script or record exists for these README claims [CLAIM]:
  - the (13,5,4) control of `build_v2` (`README.md:313-314`);
  - "build_v2g(base_quad=True) is byte-identical to build_v2" (`:317`);
  - the A3'' batch controls for both M1 and M2 (`:300-302`).

  The PA18 M2 controls exercise copies of the code, not the production functions: `build_variant18` (`control18.py:118`) and `build_v2g(base_quad=False)` (`control18_v2.py:33`).
- **Production encoders with no positive control at all:**
  - `encode_full.py` hard-codes q=6 (`:33-42`), so it cannot run at (13,5,4).
  - `encode_q0.py` and `encode_q0b.py` hard-code 19/8/6.
  - The (13,5,4) positive controls contain only two SAT skeletons (ms04_s00000, ms07_s00001) and one SAT placement.
- **Weak binding between results and their inputs.**
  - `summarize3.py:34-57,82-93` counts subcases by file-name index only. It never checks them against the hash of `ext.json`, the encoder version or a regenerated CNF.
  - `ext.json` is created on demand, without the enumerator or networkx version.
  - Records carry no hash of the encoder, spec, `ext.json` or solver binary.
  - The CNFs for paths a and b are tied to the pass-1 SHA only.
  - Sources are still changing (`encode_skel_b.py` was modified about an hour before inspection).
- **One checker for everything.** All verdicts go through a single worker-built drat-trim/lrat-check with no build record. M2's independence stops at the encoder and generator: it shares both the checker and the `stream_check4` harness with M1.

**MINOR**

- **Two drat-trim stalls.** Both records stopped at exact multiples of 64 KiB of DRAT read: 589,824 = 9·65536 (`a3/ms01_s03171/f01788.json`) and 6,356,992 = 97·65536 (`part/ms09_s00010/batch_04300_04399.json`). Both have LRAT size 0 and ended with SIGTERM, which points to a pipe stall rather than slow checking [INFERENCE]. Both were correctly marked UNKNOWN, then rerun on the lrat-check-only path.
- **FIFO directory names are deterministic** for each case (`v4ps_<tag>`, `v4a3_…`, `v6pb_…`), so concurrent or orphaned attempts could cross-talk.
- **summarize3 does not report every SAT result** despite its docstring (`:12`). SAT outcomes in paths a and b are never listed, and the a3/part scan stops once a case is decided (`:72-93`).
- **M2 batch range inference** depends on a `"multiset"` key and a two-element list (`:53-54`). That matches today's writers (`run_m2partbatch.py:63`, `run_hard7.py:92`) but is fragile.
- **Weak or no-op controls:**
  - The PA18 mutations all change symbol counts (`control18.py:130-139`, `control18_v2.py:40-47`), so they can fail for an unintended reason.
  - The verifier mutation `non_digit_token` was rejected by `verify_pa.py` for "9 entries", not for the bad token.
  - The (7,2,2) control is vacuous.
  - `smoke-stream4.json` records `all_expected: false` because test D was never exercised; D2 replaced it.
  - No smoke test feeds a bogus proof, which is why F1 went unnoticed.
  - The M2 (13,5,4) controls reuse M1's skeleton lists (`control13_m2.py:24-26`).
  - The claim that `extend_p1q` reproduces `extend_p1` has no diff receipt.
- **Small code nits:**
  - The docstrings say "stream_check_revision=3", but the code writes 4 (`stream_check4.py:126`).
  - `build_v2` lacks `build()`'s `assert len(profs)==K` (`encode_skel_b.py:89`).
  - `run_m2.py:33-35` ignores the encoder's return code.

## (3) What the parent must pin, and the least-disk replay

**Pin first:**
- the source, data and tool hashes in the table above;
- a hash of every cycle-2 source file at freeze time;
- solver and checker binary hashes plus `--version`;
- Python 3.14 and networkx 3.7 from `~/.local/state/research-explorer/venv`;
- the PA18 canonical array `cycle2/control18/cpro1-canonical-m1.txt` (`31553e4f…`).

Copy only the small files: `src/`, specs, results, proofcheck, proofstream, hard, the `ext`/`f*`/`batch*`/summary files, `skel-b`, and the control files. Leave CNFs and proofs where they are.

**Replay steps:**
1. **Build checkers.** Compile drat-trim from `review/moqls7-parent-proofcheck-tools-v1/` with `cc -O2`, the same way `moqls7_parent_proofcheck.py:58-66` does. First check that those source hashes match the lane's copies.
2. **Rebuild CNFs in memory and compare hashes.**
   - All 5577 `encode_skel` CNFs against the pass-1 `cnf_sha256`.
   - Every a3/part subcase and batch, from (spec, `ext.json`[i] or the batch indices), against the record's `cnf_sha256`.
   - Optionally regenerate `ext.json`.
3. **Re-check proofs already on disk, without re-solving:**
   - Path a: run the parent's drat-trim on `cases19skel/cnf/<tag>.cnf` with `proof/<tag>.drat`, and compare the DRAT hash with the record.
   - E0 M1: the same on `cases19q0`.
   - E0 M2': the stored LRAT in `m2q0b/proof` must go through a checker that requires a conflict. cake_lpr would do, but it is not installed (`/opt/homebrew/bin` has none).
4. **Re-solve every CaDiCaL-only result** (the 60 path-c cases, the 2 reruns, and later all of M2). Use one of:
   - kissat or CaDiCaL binary DRAT streamed into the parent's drat-trim (`-i`, proof on stdin);
   - a strict RUP-only LRAT checker owned by the parent and tested with the step-4 smoke below.
5. **Kissat streamed paths b, d, e:** re-solve with the same arguments, stream the DRAT into the parent's drat-trim, and compare `drat_sha256`. Do all of b; do d and e in full or as a stratified sample.

**Formats and process:**
- CNF is plain DIMACS, rebuilt in memory.
- kissat writes binary DRAT. drat-trim needs `-i` when reading from stdin, can't take a FIFO as a named proof file (it peeks, then reopens it: `drat-trim.c:1430-1461`), and needs the CNF as argv[1] (`:1424`).
- LRAT from drat-trim and from CaDiCaL is ASCII. Nothing in the lane is compressed. If storage is unavoidable, stream through zstd as in `review/moqls8-k2-parent-inputs-v1/code/proof_run.py`.
- Stop processes with SIGTERM only, use the solvers' native limits, and create a fresh FIFO directory for each attempt.
- Write an aggregator separate from `summarize3`. It should check the whole chain per case: spec → CNF hash → solver binary and arguments → proof hash → checker binary, exit code and verdict line → all indices covered → no SAT anywhere.

## (4) Smallest useful smoke tests and intended-reason controls

1. **Checker negatives (F1).** Start from `p cnf 1 1 / 1 0`.
   - Feed LRAT `2 0 0` and then `2 0 1 0` to the lane's `tools/drat-trim/lrat-check`. A sound checker prints `c NOT VERIFIED` with exit code 1. I predict `c VERIFIED` with exit code 0.
   - Positive check: `p cnf 1 2 / 1 0 / -1 0` with LRAT `3 0 1 2 0` must give VERIFIED.
   - drat-trim on `s.cnf` with the proof `0` must not print `s VERIFIED`.
2. **True positive and binding.** Use `cases19skel/specs/ms04_s00000.json`: its CNF hash is `100f22b2…` and its stored DRAT `5ed9b29c…` is 853,664 bytes.
3. **One binding anchor per path:**

   | Path | Case | CNF hash | Proof stream |
   |---|---|---|---|
   | c | `ms06_s00028` | `5d1e08ae…` | LRAT `1efa5993…`, 826,154,765 B |
   | b | `ms06_s00188` | `882933fb…` | DRAT `dffe90ec…` |
   | d | `a3/ms01_s01021/f00000` | `f301fb7c…` | DRAT `93941602…` |
   | e | `part/ms09_s00010/batch_00000_00099` | `775844e2…` | DRAT `a8116334…` |
   | e (CaDiCaL rerun) | `batch_04300_04399_r2` | `7d9af598…` | LRAT `89e9383f…` |

   Re-check the CaDiCaL rerun with a checker that requires a conflict.
4. **Positive controls on the production functions at (13,5,4).** Inputs are `controls/skel13/skeletons-ms0{1,4,5,6,7}.json`, converted as in `control13_m2part.py:28-30`.
   - `encode_skel.build` and `build_v2` should be SAT exactly for ms04_s00000 and ms07_s00001.
   - `encode_partq`, `encode_partbatch` (all placements in one batch), `build_part` and `build_partbatch` should be SAT exactly for ms07_s00001.
   - Every SAT model must pass `verify_pa.py` and `bin/verify_pa2` with arguments `13 5 4`.
   - Also byte-compare `build_v2` with `build_v2g(base_quad=True)` on skel-b ms06 b85.
5. **Intended-reason mutations on the PA18 canonical array:**
   - Swap two symbols within one column so the counts stay the same but one row pair agrees twice. Expect UNSAT, and SAT once the agreement family is removed.
   - Relabel equal-count symbols, or swap two interchangeable rows. Expect UNSAT with symmetry breaking on and SAT with it off.
6. **Aggregator negatives**, on a scratch copy of the result tree:
   - delete one `f*.json` and the case must reopen;
   - inject a record with `checked: true` but a wrong CNF hash, which `summarize3` would still accept;
   - inject a SAT result into proofstream, which `summarize3` would not list.

**Scope limits:** I did not audit the cover itself (`gen_skel`, the genbg lemmas, the E0 graph lemma), `verify_pa2.c` or `sa19`. E0 results apply to the balanced multiset only. Every A2 verdict depends on the skeleton cover being complete.
