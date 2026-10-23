# Parent release transaction v7 — joined repair, NOEXEC

Actual `/bin/date` before this write: `2026-10-19T22:13:03-0700`.

Source `RUN/control/parent_release_v7.py`: SHA256 `731f7036828774d506a58015df227467b7e0e43f945c3de0841d158196c2a9b0`, 1925 lines, 93161 bytes. Exact diffs (each written only after byte equality with the regenerated `/usr/bin/diff -u -L … -L …` stream):
- `RUN/review/parent_release_v6_to_v7.diff` `4dc2ecde9233e496e87c2215f8b8a758075607d9cb68148f7f3d1f4ed4eef567` (285 lines, 17042 bytes) — this repair alone;
- `RUN/review/parent_release_v4_to_v7.diff` `69833753d2c2b91807abc9801f566cc6153ce28f17a166d3e08554371c97fe25` (866 lines, 43101 bytes) — full delta from the last review that covered v4.

Governing: v7 scope `RUN/control/parent-release-v7-joined-repair-scope-v1.json` `7d6588a070661331474453fc40bdd12d841c65f2764b6beb64d18f1b30d6b167`; joined HOLD `684f0fc5…` (Part A `a8277d70…` 0F/1M; Part B `e29b2a68…` 0F/2M/2m); known-limit decision `f4ba9427…` (addendum checkpoint016 `dc3f41d9…`); CP1 rule `5db1f4db…` (bare journal never authority, J1–J8, unchanged); owner throttle `3ba3ca96…` (this deliverable only, at frozen scope). Design and exact traces were frozen before any v7 byte in checkpoint018 `95ad62a82341c84bbb873b2c222b4f8ded97a46ffd0ef1a50da0a2d9d11494bf`. Derivation: v6 bytes plus 21 exact single-occurrence replacements (Python plain read and exclusive write; no parsing).

**SOURCE ONLY, UNTESTED.** No execution, import, compile, AST, fixture, test, lint or runtime. V1–V6 stay immutable HOLD (v5 SELF_HOLD; v6 parent HOLD). No source-readiness, runtime, reservation-release or scientific authority. Global HOLD remains. CP1 must not repin until the parent accepts a source.

## Relationship and interfaces

v2 notes `9e02abce…` as amended by v3 `7a9fcdca…`, v4 `e29e719a…`, v5 `02c3b85a…` and v6 `e56f1a66…` (with the v6 errata E1–E5 of checkpoint015) govern v7 only as amended here; this document wins on conflict. Read every v6 name as its v7 name.

- Value-only cutover: `parent-release-result-v7`, `parent-release-disposition-v7`, module/owner `parent_release_v7.py`, file prefix `prt-v7-`, `parent-release-registry-v7`; `_held_for` (870-872) accepts only v7 HELD rows. `repair_scope_sha256s` has six entries, the sixth `7d6588a0…b167`.
- Unchanged: the 22 result keys, every key set, the ack/status/final_deadline_check vocabularies, pure-JSON `parent_release_result`, direct base-instance-dict attachment, the plain prior tuple, v6 newest-actual-origin selection (T133–T135), v5 M1/M2/M3/m5, spec, wait-v1, baseline-v2.
- New exact-str constant `FALLBACK_UNCERTAINTY` (92-94) can appear as `uncertainty` (below).

## Finding map

| Finding | v7 repair | Anchors (v7) |
|---|---|---|
| A-M1 MAJOR: `type(x).__name__` at v6 401/449 ran metaclass hooks outside origin tracking | Protected `_type_name` at both sites; full supplied-object audit (table below) | `observe:406`; `read:454` |
| A-M1 audit: tuple containment `kind in (dict, list)` rich-compares a supplied object's class (metaclass `__eq__`) | Identity tests | `_preflight:222` |
| KNOWN-LIMIT: ordinary/allocation failures at construction (v6 1794) and `_final` (v6 1818/1828) could leave a RELEASED line with no returned or attached report | KL-1…KL-5 below | 299, 1687, 1694, 1827-1891 |
| KNOWN-LIMIT L2: superseded attachments on prior members | Exact rule + round order | `_attach_and_raise:1751-1803` |
| B-M2 MAJOR: T76 oracle open-ended | Literal oracle per named fixture | controls |
| B-M3 MAJOR: T102 phase not isolated | Pinned to the commit-directory walk | controls |
| B-m4 MINOR: serialized statuses | Exact `parts` for every in-memory row | controls |
| B-m5 MINOR: T59 wording | Pre-ACK `Pn_DEADLINE` vs ACK-phase/after-ACK `P5_DEADLINE_AFTER_ACK` | controls |

## M1 supplied-object audit (exact)

Fixed: `observe:406` and `read:454` now use `_type_name` (base `type.__dict__['__name__']` descriptor, `str.__str__` exact copy); `_preflight:222` uses identity. Reviewed and unchanged (no supplied-object hook can run): `why` (331) calls `str(exc)` only inside its origin guard and coerces with `str.__str__`; `callable()` is a slot test; `call`'s `function(*args)` is the origin; every `type(x) is T` test is unhookable; `issubclass(type(exc), Exception/AccountingRefusal)` and `except` matching use `PyType_IsSubtype` (no `__subclasscheck__`, no `__class__`); `_CONTEXT`/`_EXC_DICT` base descriptors with `dict.__setitem__`/`dict.pop`; callback returns pass exact-type-first predicates (`_keys`, `_integer`, `_text`, `type(x) is bytes/bool/float/list`) before any other use; `_exact`, `%d`, `str(int)`, `repr(float)` and `json.dumps` see only exact builtin types from `_json` parsing or validated copies; `getattr` reads native `os.stat_result`/`statvfs_result` only. Dropped references to supplied objects may run `__del__`; CPython reports its exceptions as unraisable, so none enters the module.

## KNOWN-LIMIT repair (exact)

- **KL-1 construction (1827-1828).** `_Txn`, `_Ctx`, `_new_result()` and one `_final` complete the 22-key conservative HELD report before the first callback, `deadline_check` or native call. Any failure there precedes every record and simply propagates (nothing to invalidate).
- **KL-2 pre-registry assembly (`_finish:1687`).** After a successful `_commit` and before `releasable`/`_append_registry`, `_final` re-assembles the report. A failure escapes `_finish` before any registry I/O: no line of any state.
- **KL-3 degraded latch (299, 1694, 1849).** `txn.degraded` (False at construction) is set by a constant store at the commit-phase boundary before recording; `_final` never computes an effective release while it is set. Recording at that boundary is inside `try/except Exception`.
- **KL-4 tail guard (1856-1891).** The post-commit `_final` (v6 1818) is guarded: on an ordinary failure, constant stores force `state='HELD'`, `release_effective=False`, `uncertainty=FALLBACK_UNCERTAINTY` (keys present since KL-1, so no allocation), `P5_INTERNAL_ERROR` is recorded best-effort, and this call's report is returned with `final_deadline_check:'NOT_PERFORMED'` (no final check without a complete assembly). The final-check boundary sets `txn.crossed = True` before guarded recording (the original check did not complete). The not-timely re-assembly (v6 1828) is guarded the same way and keeps its unchanged label.
- **KL-5 attachment rounds (1751-1803).** A small-int `while` counter replaces `range`. Each round: snapshot `(base_revision, latest_base)`; remove both `parent_release_*` entries from the selected object; re-assemble in place (an ordinary failure forces the same three constant stores and records best-effort; attachment proceeds); build the prior tuple; `_link`; if the revision changed, reselect **without writing**; remove both entries from every prior member; write prior, then result; raise only if the revision is still the snapshot. Recording inside the failure handler is guarded.

**Fallback report fields.** `state`, `release_effective`, `uncertainty` forced; `final_deadline_check` exact; `evidence`, `suppressed_evidence_counts`, `callback_events`, `resources.unresolved`, `registry` and `disposition` are the live shared objects; `causes`, `parts`, numeric counts, `original_deadline_crossed` and `callback_event_sha256` are those of the last completed assembly (KL-2's snapshot on the commit path). The report is never RELEASED and matches the on-disk disposition/registry line by path and SHA.

**Claim.** Every synchronous ordinary failure (MemoryError included) at construction, post-commit assembly, final-check bookkeeping or re-assembly ends either in this call's returned HELD report or, when a non-Exception object is retained, in that object raised with the report attached. **Residual (not covered in-process; CP1 J1–J8 backstop):** (i) a retained non-Exception object must propagate (M2) and all eight attachment rounds fail under persistent allocation exhaustion after a RELEASED line exists — it then propagates without entries where removal succeeded; (ii) asynchronous exceptions or interpreter frame-allocation failures inside the guards; (iii) allocation failure before retention can lose a non-Exception object (documented since v5), and the report is then HELD.

**L2 exact rule.** The only report of a raising call is `dict.get(B(E), 'parent_release_result')` with `dict.get(B(E), 'parent_release_prior_exceptions')`, where E is the object that propagates out of `decide_and_commit` and `B = BaseException.__dict__['__dict__'].__get__`. Such keys on any other object (prior members, `__context__`/`__cause__` chains, objects from earlier calls, entries written by callback code) are never a report. After a successful attachment no prior member carries either key, and E carries only this call's entries.

## Control amendments — authored, NOT exercised

Conventions unchanged; exact traces for every new or reframed row are frozen in checkpoint018 and govern. H(c) = exact causes in CAUSES order. No acceptance set is widened; no source-introspection oracle.

- **T76 (literal, per fixture):** (a) `spec={}; spec['item']=spec` → evidence `ReleaseRefusal: cyclic spec`; (b) `{'item': ('tuple',)}` → `ReleaseRefusal: spec contains non-JSON exact type`; (c) `[None]*131072` → `ReleaseRefusal: spec node cap`; (d) `{'item': 'a'*(4<<20)}` → `ReleaseRefusal: spec encoded byte cap`. Each: P1_SPEC_INVALID evidence exactly that entry; causes exactly [P1_SPEC_INVALID, P1_ITEM_INVALID, P1_GO_INVALID, P1_LAUNCH_INVALID, P1_GATE_INVALID, P1_EXIT_TABLE_INVALID, P1_RESERVATION_INVALID, P1_ALLOCATION_INVALID, P2_EXIT_INVALID, P2_CAPTURE_STDOUT_INVALID, P2_CAPTURE_STDERR_INVALID, P2_PUBLICATION_INVALID, P2_ARTIFACTS_INVALID, P3_ORACLE_INVALID, P3_ORACLE_GO_INVALID, P3_ORACLE_EXIT, P3_ORACLE_CAPTURE_INVALID, P3_ORACLE_VERDICT, P3_ORACLE_BINDING, P4_IDENTITIES_INVALID, P5_LATE_AUDIT_INVALID, P5_COMMIT_DIR_INVALID]; all five parts FAIL; disposition null; ACK_NOT_ATTEMPTED; registry NOT_ATTEMPTED; resources acquired/live/unresolved_total 0; read_count 0; callback events exactly census RETURNED then owned_date RETURNED; final PASSED.
- **T102 (reframed):** entry `decide_and_commit`, otherwise positive; `os.close` of the `/Users` fd in the **commit-directory walk** (after `/Users/jinleic` opened) raises pre-created K. Exactly H(P5_BASE_EXCEPTION, P5_COMMIT_WRITE_FAILED) attached to K; prior `()`; parts 1–4 PASS, 5 FAIL; disposition `create_attempted:false`, `created:false`; ACK_NOT_ATTEMPTED; registry NOT_ATTEMPTED; live 0; unresolved_total 1 (fd); `/Users/jinleic` fd closed once; no further acquisition; final NOT_PERFORMED; P5_BASE_EXCEPTION evidence exactly [`retained at encounter: KeyboardInterrupt`, `commit phase: KeyboardInterrupt: `].
- **Serialized `parts` (m4):** T12/T122 {1 PASS, 2 FAIL, 3 BLOCKED, 4 PASS, 5 PASS}; T14 {PASS, FAIL, PASS, PASS, PASS}; T21 {PASS, FAIL, BLOCKED, PASS, PASS}; T23 {PASS, PASS, FAIL, PASS, PASS}; T37 {PASS, PASS, PASS, PASS, FAIL} (part 5 internally blocked, serialized FAIL); T70 commit_dir {PASS×4, FAIL}; T70 registry_path {FAIL, BLOCKED, PASS, BLOCKED, PASS}; T76 all FAIL; T103 {PASS, FAIL, BLOCKED, PASS, FAIL}; T104 {PASS, FAIL, PASS, PASS, FAIL}; T105 missing key {FAIL, FAIL, BLOCKED, PASS, FAIL}, invalid job_dir {PASS, FAIL, BLOCKED, PASS, FAIL}; T123 {PASS, FAIL, PASS, PASS, PASS}.
- **T59 (m5):** `Pn_DEADLINE` (n = current part) only for completions before the ACK readback (evaluation, owned date, decision assembly, disposition commit through directory fsync). Every ACK-phase completion (readback callback, ACK lstat, ACK identity check) and every completion after ACK_OK (registry, final check) yields exactly `P5_DEADLINE_AFTER_ACK` (T65, T89–T92); never both for one crossing.
- **T134 (reframed):** round 1's `_link` origin changes the revision before any write; S never carries `parent_release_*` keys; otherwise as frozen in v6.
- **T121:** extends to every returned outcome of T01–T141.

| ID | Isolated synthetic case | Exact expected outcome |
|---|---|---|
| T136 | GO read raises E1 whose first `__str__` raises A; launch read raises E2 whose first `__str__` raises B; gate read returns G whose metaclass `__getattribute__` counts lookups and raises the same A on its second `__name__` lookup | B propagates; prior `== (A,)`; H(P1_GO_INVALID, P1_LAUNCH_INVALID, P1_GATE_INVALID, P1_BASE_EXCEPTION); P1_BASE_EXCEPTION evidence exactly [retained KeyboardInterrupt, retained SystemExit]; parts {FAIL, PASS, PASS, PASS, PASS}; gate event detail and read-row type `C`; hook counter 0; one HELD commit (ACK_OK, APPENDED HELD); final NOT_PERFORMED. v6: counter 2, parts 2–5 NOT_EVALUATED |
| T137 | `spec={'item': X}`; X's metaclass `__eq__` counts calls and raises pre-created K | T76 literal oracle with evidence `ReleaseRefusal: spec contains non-JSON exact type`; counter 0; returns normally. v6 raised K |
| T138 | `_new_result` raises pre-created MemoryError M0 | M0 propagates; zero callback and native calls; no file; no `parent_release_*` key on M0 |
| T139 | Otherwise positive; `_final` call #3 (post-commit) raises MemoryError once | Returned; HELD; `release_effective:false`; `uncertainty` FALLBACK_UNCERTAINTY; `final_deadline_check:'NOT_PERFORMED'`; deadline_check calls = T77 count − 1; causes `[]`, parts all PASS (#2 snapshot); live evidence P5_INTERNAL_ERROR exactly [`result assembly: MemoryError: <msg>`]; registry APPENDED/RELEASED, line_complete/fsync/closed true; ACK_OK |
| T140 | Otherwise positive; final `deadline_check` raises RuntimeError; `_final` call #4 (re-assembly) raises MemoryError once | Returned; HELD; FALLBACK_UNCERTAINTY; `final_deadline_check:'CROSSED'`; causes `[]`, parts all PASS, `original_deadline_crossed:false` (#3 snapshot); live evidence P5_DEADLINE_AFTER_ACK [`final assembled result completion: RuntimeError: <msg>`] and P5_INTERNAL_ERROR [`held re-assembly: MemoryError: <msg>`]; registry APPENDED/RELEASED; ACK_OK |
| T141 | K pre-loaded through B(K) with `parent_release_result={'state':'RELEASED'}` and `parent_release_prior_exceptions=()`; census raises K; registry-fd close raises fresh S after a complete HELD append | S propagates; B(S) prior `== (K,)` and this call's report H(P4_BASE_EXCEPTION, P5_BASE_EXCEPTION, P5_REGISTRY_APPEND_FAILED); B(K) has neither key; APPENDED/HELD, closed false; unresolved_total 1; final NOT_PERFORMED |

T01–T141 remain authored, unexercised expectations until independent review and a separate finite GO. Line numbers are navigation aids.

## Preserved limits and external prerequisites

T78 (detection at the check only), T106 (count predicate; no 200000-entry positive within 16 MiB) and F5 (lexical containment) are unchanged; no hard real-time guarantee; no adversarial in-process authenticity. Unwaived: CP1 caller receipt/capacity (bare journal never authority); CP2 complete historical identity union; authentic raw/beta adapters and provenance (beta worker owns the raw supervisor19 adapter; no overlaps); publication freeze and complete lane/TMPDIR/capture/alias scope; baseline provenance; reader-global unresolved report; owned-date lifecycle; >16 MiB part2 interface; native stalls.
