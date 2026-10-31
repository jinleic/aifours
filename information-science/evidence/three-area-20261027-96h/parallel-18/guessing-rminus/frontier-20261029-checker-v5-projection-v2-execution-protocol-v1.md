# Execution protocol (DRAFT ONLY — NO GO until parent freezes it and the owner authorizes the heavy-run budget)

Observed clock before drafting: **Thu Oct 29 18:31:36 PDT 2026**. Nothing in this document authorizes execution. No checker, diagnostic, fixture or archive byte was run, opened for consumption, or modified while drafting it.

## 0. Checkers and frozen inputs of record

| Object | Pin |
|---|---|
| `checker-v5.py` (f267-closed successors, checker of record) | SHA-256 `8258ab4935e3f42ca74e9dc8e2287b6e31a7ddbcffdfb06fc085a62bdc6f7a06` |
| `projection-checker-v2.py` | SHA-256 `b60b85b65fd1b355132e6dbd7a14b0fe6ec9f8e71d76bd99a432b13b06ab72b4` |
| Immutable archive | `3bde5418e776a88b6a8f9c3e7a147a016b2b09272908eac226e1f3b33ced3040` (67,393,983 B) |
| Row-semantics declaration | `c67ecd5bce3ef5cab01a0e9949f56a5f801d80e17209864b7b85ea51b16eea4d` |
| v5 input manifest (f257 `manifest-v1.json`) | `2db2c57022d0039b323046a855cff91ec84fa99278aded14358e25532329fd93` (18 inputs) |
| PJ2 input manifest (f258 `manifest-v1.json`) | `7864409178e5c45b649dbb68ca2d40bb61cd77882882c0b2d1d6019f343885e8` (16 inputs) |
| f267 static outcome | `7a6aff39…088` (both f264 MAJORs CLOSED; v5/PJ2 = checkers of record) |

Contract inside v5 (`TARGET_ARCHIVE`): 71 members, 457,373,801 uncompressed bytes, packet SHA `999b2a8d…086`, **748 certificates / 1,811,001 rows / 174,251 planes**, 247 four-cases, 515 classes. `fixture_universe` is absent, so the 174,251-plane universe is enumerated by `all_planes(10, cap)` at run time.

## 1. Phases (each requires its own explicit parent GO; order is mandatory)

- **Phase 0 — synthetic controls (≤10 min).** v5 modes `identity`/`planes`/`color`/`applicability` against the existing read-only f257 fixtures (`reviewer-synthetic-record.json`, `-binding.json`, `-applicability.json`, `-color.json`, `-planes.json`, `reviewer-synthetic-*.zip`). Purpose: confirm intended-path wiring after the v5 edits. No real archive record.
- **Phase 1 — PJ2 single-record projection (`--final`, ≤3 min).** One pinned R382/recovered-source projection; internal 115 s itimer.
- **Phase 2 — v5 one-record diagnostic (`mode r382`, ≤3 min).** `--max-rows 5000` (the mode's enforced ceiling; R382 needs < 5000).
- **Phase 3 — v5 full finite archive replay (the heavy run, ≤4 h 05 m wall).** Single attempt only.

Phase 3 runs only after Phases 0–2 each end in their expected terminal state, and only with the owner's explicit heavy-run authorization. Any phase may be dropped by the parent without affecting the others' gating.

## 2. Exact launch commands (owner root; absolute paths at GO time)

Environment for every phase (single-threaded, no bytecode writes):

```
/usr/sbin/taskpolicy -m 8192 /usr/bin/env \
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
  python3 checker-v5.py archive \
  --archive /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261029-all-plane-entropy-body-complete-review-packet-v2.zip \
  --output  <abs>/frontier-20261029-checker-v5-archive-run-v1.json \
  --max-certificates 800 --max-rows 2000000 --max-planes 175000 \
  --time-limit-ms 14400000
```

- Caps are **strictly above** the frozen contract totals (800 > 748; 2,000,000 > 1,811,001; 175,000 > 174,251) so no cap-UNKNOWN can fire on genuine data. `--time-limit-ms 14400000` is v5's archive-mode ceiling (4 h cooperative itimer; SIGALRM → `TIME_LIMIT`).
- `--max-items` is unused by archive mode (default 5000, inert); documented to prevent ambiguity.
- Phase 1: `python3 projection-checker-v2.py --final` (stdout captured to an O_EXCL file; exit 0/2/3).
- Phase 2: same env, `checker-v5.py r382 --output <abs>/frontier-20261029-checker-v5-r382-run-v1.json` (defaults; `--max-rows>5000` is rejected by design).
- Phase 0 argv follow f267/f257 fixture names; each output is its own O_EXCL JSON, e.g. `frontier-20261029-checker-v5-synthetic-<mode>-run-v1.json`.

The tool deadline is 0 (no client-side kill). The only deadlines are v5's internal itimer and PJ2's 115 s timer. `-m 8192` is a MiB memory **request**; enforcement is NOT independently tested and is not claimed — observed peak RSS is recorded instead.

## 3. Expected terminal states and UNKNOWN taxonomy

| Terminal state | Exit | Meaning / settlement |
|---|---:|---|
| `VALID_ARCHIVE_FINITE_REPLAY_CONDITIONAL` | 0 | Finite serialization/identity/coverage checks passed. **Not** theorem acceptance, source-projection equality, or actual-law applicability. |
| `REJECT` (+reason) | 2 | A declared premise failed on real data — a genuine finding. Freeze reason + output; report to parent; no reinterpretation, no retry. |
| `UNKNOWN` (+reason) | 3 | Incomplete. No scientific conclusion either way. |
| `OUTPUT_EXCLUSIVE_FAILED` | 73 | Receipt file could not be created exclusively; run counts as not performed; investigate before any re-attempt. |

UNKNOWN reasons, classified against the configured caps:

- **Plausible/expected on a heavy run:** `TIME_LIMIT`; `INPUT_UNAVAILABLE:*` or `ARCHIVE_UNAVAILABLE_OR_INVALID:*` (environment); `UNEXPECTED_EXCEPTION:*` (bug — freeze traceback reason).
- **Unexpected with correct inputs/caps (freeze and report, never silently raise caps):** `ARCHIVE_CERTIFICATE_CAP`, `ARCHIVE_ROW_CAP`, `ARCHIVE_PLANE_CAP`, `ROW_CAP`, `PLANE_CAP`, `PACKET_SIZE_CAP`, `R382_ROW_CAP`, `MISSING_NONCOVER_DELETE_ONE_COLOR_ARGUMENT`, `MISSING_NONCOVER_ARGUMENT_CATEGORY:*`, `MIXED_PLANE_SCOPE_NOT_CACHEABLE`, `FOUR_CASE_NO_VERIFIED_APPLICABLE_PROOF`, `UNSUPPORTED_SCOPE_FIELDS:*`, `UNSPECIFIED_PLANE_FIELDS:*`, `UNIMPLEMENTED_DECLARED_DESCRIPTOR:*`.
- **PJ2 only:** `cap.time-limit` / `interrupted.signal` (UNKNOWN), `pin.*` / `json.*` / `metadata.*` / `descriptor.*` / `premise.*` / `identity.*` / `unsupported.source-*` (REJECT), success string `R382_PROJECTION_AND_EXACT_IDENTITY_MATCH`.

The four new VALID admissions documented and justified by f267 are the expected Phase-0/2 admissions; this protocol does not restate them as facts, it binds them to the f267 outcome record.

## 4. Outputs, receipts and settlement discipline

1. Checker outputs are written by the checkers themselves (O_EXCL, 0600): one JSON per phase at the paths in §2.
2. A per-phase **settlement receipt** (written by the runner, also O_EXCL) records: verbatim `/bin/date` before and after; verbatim argv; PID and PGID; requested memory (8192 MiB) and observed peak RSS (darwin `ru_maxrss`); wall seconds; exit code; SHA-256 + bytes of the checker output; archive SHA before and after the phase (the checker also self-checks `ARCHIVE_CHANGED_DURING_REPLAY`); and a one-line classification from §3.
3. **Single attempt per phase. Nonzero exit (including 3/UNKNOWN and 73) = INCOMPLETE; no automatic retry, no cap inflation, no code edit.** Any re-attempt needs a new parent GO naming the changed condition.
4. Stop discipline: SIGTERM (v5 maps it to `INTERRUPTED_SIGNAL_*` UNKNOWN), then SIGINT; escalate to a parent decision only if both fail for >5 min. Never a silent SIGKILL.
5. No network, no git, no deletion, no writes outside the two O_EXCL files per phase; the archive is opened read-only and is never copied or touched.

## 5. Resource budget being requested (NOT yet authorized)

- Wall: Phase 3 ≤ 4 h 05 m (4 h internal itimer + startup); Phases 0–2 ≤ 16 min combined. Parent checkpoint observation at ≤30 min cadence with dated receipts; continuous supervision is NOT claimed for the whole window.
- Compute: 1 thread; admission estimate peak RSS < 4 GiB (per-record Fraction accumulation over ≤ 5119 coordinates; 71 members streamed, not materialized) — an estimate, not a measurement; request 8192 MiB headroom.
- Disk: < 10 MB outputs. No other resource consumption.

## 6. Boundary

Even a clean Phase-3 exit 0 establishes only the finite expanded-identity and set-coverage checks against the frozen declaration. Written caller/lift/tensorization premises, actual-law applicability, source-projection equality beyond PJ2's single pinned record, the theorem itself, novelty and any guessing-number conclusion all remain open and unadopted. The four f267 non-gating minors stay open and are not cured by any phase here.

**END OF DRAFT — awaiting (a) parent freeze of this protocol and (b) explicit owner authorization of the §5 budget. No execution permitted until both exist.**
