# Parent release transaction v6 — successor repair, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T21:23:58-0700`.

Source `RUN/control/parent_release_v6.py`: SHA256 `65eef494580b81adcd6e80eda54c26c368f3b009c435c9941b3d9cdd0bc01e69`, 1864 lines, 88789 bytes. Exact diffs (each file written only after its bytes equalled the regenerated `/usr/bin/diff -u -L … -L …` stream):
- `RUN/review/parent_release_v4_to_v6.diff` `9314a678775c9b13b41259260ac56e55b0371c75942936c2527cebacd7d07783` (773 lines, 37361 bytes) — full delta from the last reviewed source;
- `RUN/review/parent_release_v5_to_v6.diff` `3153a21834aa862a772a5c0d5cd97a8bc3e325693ec0965af724e4828dc2d8b9` (268 lines, 15222 bytes) — the successor repair alone.

Governing: base `4d122872…`; scopes v2 `2fdf13b4…`, v3 `1f9befdb…`, v4 `32d161b0…`, v5 `ef0ab41a…`; v6 authority `RUN/control/parent-release-and-cp2-v6-successor-authority-v1.json` `b08a12dd36d52a020a3927e64d28d483886505b4d02df4407142aaae3393e27e`; v4 Codex HOLD 0 FATAL/3 MAJOR/2 MINOR `b38745818f96a032106eea3da675a40adf640d19c483c83dac64691f7228a8e8`. Freezes: checkpoint010 `16fefc37…` (v5 plan), 011 `ae1306a1…` (helper retention), 012 `5dc45da4…` (v5 artifacts), 013 `d054228d…` (self-detected selector defect), 014 `6d731e7dec90f7346e0398be4a51e1e9d763a69a2c307eb899122f8838f9f7bf` (v6 scope and exact encounter traces, frozen before any v6 byte).

**SOURCE ONLY, UNTESTED.** No execution, import, compile, AST, fixture, test, lint, runtime or model CLI. Derivation: v6 bytes = the frozen v5 bytes (`82feb74c…`) with the 22 exact, single-occurrence segment replacements listed in checkpoint014, written exclusive-create; no parsing. V1–V4 remain immutable HOLD. **v5 is SELF_HOLD**: never reviewed, never CP1-eligible, never runnable. No source-readiness, runtime, reservation-release or scientific authority. Global runtime HOLD remains.

## Relationship to earlier notes

v2 notes `9e02abce…`, amended by v3 `7a9fcdca…`, v4 `e29e719a…` and v5 `02c3b85a…`, govern v6 only as amended here; this document wins on conflict. Because v5 was never reviewed, every v5 statement and control is in scope for the v6 review. Read every v5 name as its v6 name. The v5 navigation anchors and the checkpoint012 anchor errata are superseded by the v6 anchors below. **Superseded v5 text:** "Newest means the last distinct object first encountered" and "selects the newest retained exception" — v6 selects the newest *actual origin* (below); narrowing to newest distinct is rejected.

## Interfaces (value-only cutover; CP1 must not repin until the parent accepts a source)

- Result `parent-release-result-v6`; disposition `parent-release-disposition-v6`, module `parent_release_v6.py`, file `prt-v6-<slug>-<sha256>.json`; registry `parent-release-registry-v6`, owner `parent_release_v6.py`; `_held_for` (865-867) accepts only v6 HELD rows for the same allocation. No earlier version ran; no compatibility branch.
- `repair_scope_sha256s` = `[2fdf13b4…, 1f9befdb…, 32d161b0…, ef0ab41a…, b08a12dd36d52a020a3927e64d28d483886505b4d02df4407142aaae3393e27e]` (1424-1426).
- Unchanged from v4/v5: the 22 result keys, disposition/registry/resources key sets, ack/status/final_deadline_check vocabularies, spec, wait-v1, late-baseline-v2. `parent_release_result` is pure JSON (dict/list/str/int/bool/None). Attachment writes go directly into the base instance dict (`_EXC_DICT.__get__(exc)` then `dict.__setitem__`), never setattr. `parent_release_prior_exceptions` is a plain tuple of the original objects in first-retention order, excluding the propagated identity.
- New evidence text only: `Pn_BASE_EXCEPTION` gains `raised again at origin: <type>` for each repeated origin of an already-retained object.
- Effective release still requires caller-observed returned `state:'RELEASED'` AND `final_deadline_check:'PASSED'`, with ACK_OK, APPENDED/RELEASED/fsync/clean closes, no live or unresolved resource and no retained BaseException (`_final:1686-1703`, 1688). No disk syntax is authority.

## Finding map (v4 review b3874581, retained v5 repairs, and the v6 successor finding)

| Finding | Repair (all retained in v6) | v6 anchors |
|---|---|---|
| M1 MAJOR: caught shaping failures still enabled commit | `ctx.commit_dir` has one assignment, the last shaping statement, reached only after the independent job-dir exclusion succeeds AND the fresh transaction's `fired` set is empty. Every caught shaping failure fires (callables, commit_dir, spec, every field validator, capture keys/duplicate path, oracle keys, exclusion); any escaping exception never reaches the assignment | `_shape:728-784` (783-784); `_shape_field:707-712`; `_shape_captures:715-725`; `_commit:1556-1559` |
| M2 MAJOR: cleanup discarded BaseExceptions and propagated the oldest | Retention at encounter before description/cleanup; nine in-flight catches before `finally`; `release` attempts every owned close once and raises the newest non-Exception among those attempts (else the newest escaping ordinary Exception); phase boundaries use the transaction ledger, no pending variable; effective release requires an empty ledger | `keep:307-324`; `open:472-475`; `close:487-501`; `release:503-524`; `directory:536-539`; in-flight `_names:979-981`, `_artifacts:1031-1033`, `_hash_file:1205-1207`, `_scan:1234-1236`, `_walk:1277-1279`, `_free_bytes:1297-1299`, `_write_new:1511-1513`, `_commit:1584-1586`, `_append_registry:1646-1648`; `_absorb:1725-1738`; boundaries `decide_and_commit:1799-1802, 1806-1809, 1814-1817, 1822-1826`; helper `1858-1864` |
| M3 MAJOR: overridable metadata and escaping bookkeeping | Base descriptors `_CONTEXT`/`_EXC_DICT`/`_TYPE_NAME` (91-93); real-type classification `issubclass(type(exc), Exception)` (117-118, and AccountingRefusal at 563); exact-str description with failures retained (326-336); `_link` free-slot/acyclic/64-step and BaseException-guarded (1706-1722); bounded direct-dict attachment with reselection (1745-1774) | as listed |
| m4 MINOR: T121 ACK token | Notes only: `ACK_NOT_ATTEMPTED` (below) | `_new_result:1656-1663` |
| m5 MINOR: helper emitted paths its consumer rejects | `_parts(full)` before lstat/hash/insertion/descent; whole walk refused, never truncated; same predicate as the consumer | `_scan:1219`; consumer `_baseline:1312`; helper `1833-1864` |
| S1 (checkpoint013): A, B, then the same A selected B | Selection state `latest_base`/`base_revision` separate from identity-unique retention; origin handlers reselect even for an already-retained object; propagation-only catches never reorder; attachment selects `latest_base` and reselects on any revision change | `__init__:293-294`; `keep:307-324`; origins 332, 353, 430, 488, 1720, 1736, 1768; `_attach_and_raise:1756-1774` |

## Selection rule (S1), exact

`keep(exc, origin=False)` (307-324): ordinary Exceptions are ignored. If the object is already retained and the catch is not an origin, nothing changes. Otherwise `latest_base`/`base_revision` update first, the object is appended if new, and evidence records `retained at encounter` (first sighting) or `raised again at origin` (repeat).

| Class | Sites (v6 line of the `keep` call) |
|---|---|
| Origin (`origin=True`): the handler directly around foreign or bookkeeping code | `why` 332 (description call); `call` 353 (callback); `native` 430 (native function); `close` 488 (os.close / iterator.close); `_link` 1720; `_absorb` 1736 (absorption bookkeeping); `_attach_and_raise` 1768 |
| Propagation (default): never reorders an already-retained object; a first sighting still becomes newest | `tick` 369; `observe` 393, 398; `failed` 410; `open` 473; `release` 516; `directory` 537; in-flight 980, 1032, 1206, 1235, 1278, 1298, 1512, 1585, 1647; `_absorb` arrival 1731 (four boundaries); helper 1859 |

`_attach_and_raise` (1745-1774) snapshots `(base_revision, latest_base)` each round, re-finalizes the report (when ctx exists), builds the prior tuple, links best-effort and writes directly; it raises only if the revision is unchanged, otherwise it reselects; after eight rounds it raises `latest_base`. `release` keeps its local newest-close choice for unwinding; final selection is global. Every finally-owned region has an in-flight catch before cleanup, so a propagating object is retained (and, if new, selected) before any cleanup origin can occur.

**CP2-pattern audit (no PRT change).** `native` (429-432), `observe` (397-400) and `close` (499-500) re-raise a non-Exception primary immediately, with no completion check; ordinary deadline failures inside cleanup only latch `crossed` and return False (`tick:356-372`). An ordinary primary followed by a non-Exception deadline secondary propagates the secondary (observe 392-395, failed 409-412). An ordinary exception can replace an in-flight non-Exception object only through an internal failure (MemoryError class) in retention/bookkeeping; that object stays retained and selected.

## Exact v4→v6 coverage

Every hunk of `parent_release_v4_to_v6.diff` belongs to exactly one of: version text/constants (1-28) and the value cutover (866, 898, 1423-1426, 1562, 1617, 1657); M1 (783-784); M2 (293, 307-324, 353, 369, 393, 398, 410, 430, 473, 488, 503-524, 537, the nine in-flight catches, 1688, 1725-1738, 1794-1830 boundaries, 1858-1864); M3 (91-93, 117-122, 326-336, the mechanical `_why`→`txn.why`/`self.why` conversions at every description site, 563, 1706-1722, 1745-1774 attachment); m5 (1219, helper docstring 1840); S1 (294, 307-324, the seven origin flags, 1745-1774 selection); docstrings (release, `_link`, `_absorb`, `_attach_and_raise`, `decide_and_commit`, helper). No other behaviour changed.

## Control amendments — authored, NOT exercised

Conventions unchanged: separate GO, isolated exclusive fixture paths, exact pins, labelled synthetic injection in an isolated control interpreter, no OS-provenance claim, never widen sets after output. H(c) = returned/attached HELD with exactly the listed causes in CAUSES order. `__context__` values are informational interpreter chaining, never a pass criterion; the prior tuple read through the base instance dict is.

- The v5 M1 convention and re-frozen rows (T12, T14, T21, T23, T37, T70, T76, T103–T105), the v5 context note for T112/T113/T120, and T122–T129, T131, T132 stand unchanged with v6 names.
- **T130 (evidence amended):** every description attempt that raises the same K is an origin. P4_BASE_EXCEPTION evidence is exactly [`retained at encounter: KeyboardInterrupt`, `raised again at origin: KeyboardInterrupt`] (observe description, then `_guard` description). K is retained once; causes [P4_CENSUS_FAILED, P4_BASE_EXCEPTION]; one HELD commit; K propagates with prior `()`; final NOT_PERFORMED.
- **T121 (m4):** for every ordinary outcome in T01–T135, ack ∈ {ACK_NOT_ATTEMPTED, ACK_OK, ACK_FAILED, ACK_UNPROVED_DEADLINE} and status ∈ {NOT_ATTEMPTED, APPENDED, DEADLINE_CROSSED, FAILED}; ACK_ATTEMPTED/ATTEMPTED occur only on attached BaseException reports.

New rows. The exact step-by-step traces (handler class, retention list, selection and revision after each event) are frozen in checkpoint014 and govern:

| ID | Isolated synthetic case | Exact expected outcome |
|---|---|---|
| T133 | Reused instance A,B,A: first `os.read` of F (inside child directory D of a late root) raises pre-created A=KeyboardInterrupt(); `os.close(F fd)` raises B=SystemExit(); `os.close(D fd)` raises the SAME A; root close succeeds | A propagates (identity); base-dict prior `== (B,)`; attached H(P5_LATE_CENSUS_INCOMPLETE, P5_BASE_EXCEPTION); P5_BASE_EXCEPTION evidence exactly [retained KeyboardInterrupt, retained SystemExit, raised again at origin KeyboardInterrupt, `evaluation: KeyboardInterrupt: `]; parts 1–4 PASS, 5 FAIL; disposition `late_audit:null`; `unresolved_total:2` (kind fd, fd), `live:0`; commit-safe HELD commit (ACK_OK, APPENDED HELD line, fsync and closed true); final NOT_PERFORMED. v5 raised B with prior (A,) |
| T134 | Revision-sensitive swallowed repeat: census raises K; after a complete registry append, registry-fd close raises S (directory close succeeds); labelled replacement of module `_CONTEXT` whose `__get__` raises the already-retained K on its first call only | Round 1 selects S; `_link` retains the repeat K as an origin (revision changes) and returns; round 2 selects K. K propagates; K base-dict prior `== (S,)`; attached H(P4_BASE_EXCEPTION, P5_BASE_EXCEPTION, P5_REGISTRY_APPEND_FAILED); APPENDED HELD line, fsync and line_complete true, closed false; `unresolved_total:1`; ACK_OK; final NOT_PERFORMED. S may keep superseded round-1 attachments; only the propagated object's attachment counts. A length-based or last-retained selector raises S |
| T135 | Propagation never reorders: K (KeyboardInterrupt subclass whose `__str__` raises pre-created S on its first call only, then returns `k`) is raised by registry-fd close after a complete RELEASED-line append; directory close succeeds | S propagates although K is the locally propagating object; S base-dict prior `== (K,)`; attached H(P5_BASE_EXCEPTION, P5_REGISTRY_APPEND_FAILED); APPENDED with RELEASED line state, fsync true, closed false, RELEASED-bytes uncertainty; ACK_OK; `unresolved_total:1`; final NOT_PERFORMED. A selector that reorders on propagation catches raises K |

T01–T135 remain authored, unexercised expectations until independent review and a separate finite GO. Line numbers are navigation aids, not execution evidence.

## Preserved limits

- An already-retained object re-raised asynchronously inside module code (not at an origin handler) is indistinguishable from propagation and does not reorder selection.
- No hard guarantee against MemoryError or asynchronous delivery inside retention, description, linking or attachment, or between an origin and its first handler; `keep` updates selection before appending to minimize the window.
- No adversarial in-process authenticity: caller getattr can be intercepted by subclass descriptors, objects are mutable in-process, interpreter compromise is outside the contract. Base-descriptor behaviour is source-reasoned, unexercised.
- T78 injects at the final check (normal-path `_final` now 1818; optional T78b wraps it) and shows detection-at-check only. T106 is a count predicate (`_scan:1225-1226`, root 1274, helper cap 1855); no 200000-entry positive is possible within the 16 MiB serialization/read caps. F5 lexical containment does not authenticate path origin, aliases or the namespace boundary.

## Unchanged external prerequisites (not waived)

CP1 caller receipt/capacity; CP2 complete historical identity union; authentic raw/beta adapters and provenance (the beta worker owns the raw supervisor19 adapter; no overlapping edits here); publication freeze and complete lane/TMPDIR/capture/alias scope; baseline provenance; reader-global unresolved report; owned-date lifecycle; the >16 MiB part2 streaming interface; native stalls (no hard real-time guarantee). The RQLS9 fixture capture schema is not the PRT API.
