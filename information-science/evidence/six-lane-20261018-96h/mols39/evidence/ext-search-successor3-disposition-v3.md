# Beta-route source successor3 — combined review disposition v3 (2026-10-19T10:26:00-0700)

Worker ContinueCFR21c. ONE source successor of the beta route, no search-method change. Written only: no execution,
import, compile, AST/syntax parse, test, control, calibration, search, config change or review launch. Every check
below is a byte/hash/line metadata check (shasum, wc, grep -n/-b, dd, diff, ls -ld). All earlier files, snapshots and
reviewed sources are unchanged; every new file was created exclusively (open mode x). These are SOURCE dispositions,
not exercised verification. Global runtime HOLD unchanged.

Answers exactly:
- gate supplement HOLD `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-beta-successor2-admission_gate-supplement-codex-v1.prompt.stdout.txt`
  sha256 e64c3af62f579f8674ccceac22368cf692d026dc6e9e24a0493deaf1762fb277 (MAJOR 1, MAJOR 2, MINOR 3);
- math READY_WITH_FIXES `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-beta-successor2-mathematics_algorithms_data-codex-v1.prompt.stdout.txt`
  sha256 4b112b556ce98fab3f046aaf6ed2202e77d7df4b8350ba5289fa77141036049b (MINOR m2).
Starting state: disposition v1 450df2625a2b8e12c65c88613ab8f0ce585d336b940fefad25254d3688afbae5, checkpoint cp-020
0a52ef4e9a0d0a3a0676f51547634a8e7d71e11ff4d7a96580286678c080e5d7, plan v3 4032c6829fb42617f936fb34a52c75d3aa4462e8143456eb467129d59d704c7a
(all re-hashed, match).

## Changed-file table (full SHA256)
|role|successor2 (unchanged, historical)|successor3 (new, exclusive)|new bytes|change|
|---|---|---|---|---|
|beta algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_beta_final.py 88281d5dddfd088db19c91b7795c36320b80f9fd4b4322ffac7c80d512d33ccb|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext3_beta.py 33200e9d3e80ccb71b635bcd18ffe7082b2677f254ca182f99fa78a82d463873|17341|docstring l.2; MINOR 3 l.49-50; MAJOR 1 l.366-371|
|beta entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_beta_final.py 61c3e65f2e98f93e496f5f8c3eeb62664b9a0fd0d068cc53b433036ba7c83881|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext3_entry_beta.py 94c60282c01135ca108d8a1a894e03ff76c3074e5aa2701435aee584ee51c4f3|8303|docstring l.2; ALGO_PATH/ALGO_SHA256/MODULE_NAME l.65-67|
|joint algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/ext_search_joint/ext_search_joint_io_v4.py dad8a3a41b29b1e4f6de87bdfe964a079884f339aedb37fc2f205128b7e0dc1e|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/ext_search_joint/ext_search_joint_io_v5.py d7800fdd65dea87ac69877476c3c5cdc034a4ad27155702f0bd267925579ace9|30457|header l.3-4; emergency l.638-705; publish l.708-749 (MAJOR 1, MAJOR 2)|
|joint entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_joint_final.py db4e243a9c3b89cdb025f50cbd8f66b70f983d5455fd11003c5bf6df6ddb7d9d|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext3_entry_joint.py e1bd9e15f9bae56108cad19e66ae9be106aaabc200cc439c502393222ae72653|8349|docstring l.2; ALGO_PATH/ALGO_SHA256/MODULE_NAME l.65-67|
|gate algorithm|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_gate_final.py 68d6911396c032df35cd2c4b8d8644a07454631a64ee28265e0cdc604b6268c4|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext3_gate.py c1274a35861bb4f8e4161d3a062f291e80c54a6d951dc8161f6363687745c1a7|21151|docstring l.2 only (names final plan v4; m2 non-regression)|
|gate entrypoint|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_gate_final.py c94ef756bac7dd5f51e04ba007b4c7688833ec3bc47a601c50c6c15c28900cf2|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext3_entry_gate.py 10e4a848a57e032d3d82c036dcbd5550f4dbad0096f6b9bd89a6ed1fff5572d8|8304|docstring l.2; ALGO_PATH/ALGO_SHA256/MODULE_NAME l.65-67|
|resources authority|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-resources-v1.md 034a9dc19efd3d530314c5e8f7b9cc4a4e4da15b3bde58b80c71a2e0f112ee94|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor3-resources-v3.md 88fa13ed927227ad064287a064cfb4f6d92fea17da55e92edd02fca03a0179cb|8689|header l.1,3-10; m2 sentence l.49-53 (phrase l.50)|
|schema/runtime contract|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-contract-v1.md 3fc37627e3d48ffc73f116ed0456b3caa8099e6b073d7de15d7d361e86066038|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor3-contract-v2.md 761bc07386a6dc055d29aee70a21a138301ee28b43f19f25f8dadfbfbc28505a|9986|header l.1,3-7; taxonomy l.68-73; publication l.74-97; authority l.101-102|
|operative integration|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-integration-v2.md e498ec7bf0700df987b3525495fa63c446e5af1ff3a4db1558cdd3ee0ebe24e0|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-integration-v3.md d5c46f4149509994e155fb9ef4db6e1dd244c17b9badb9058e38b40ba56a3ddf|2916|header l.1,3-7; contract/plan refs l.25-28|
|final plan|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v3.json 4032c6829fb42617f936fb34a52c75d3aa4462e8143456eb467129d59d704c7a|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v4.json 06bee9f7211bb24845d8cb574e3f16eb213f9d4e7b6af8d2421509cd175b4130|34204|repinned plan v4 (see metadata v2)|
|metadata verification|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor2-metadata-v1.json 0266f1d18479eb22d8f6d5e92657a578a09fe2322d75228b84787b53166bffbe|/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor3-metadata-v2.json 87a7feb3eacb03e404d6eaeeb920ef2b8e56e0a4a971a0f1888676c9a37d1258|24438|metadata verification v2|

Carried forward byte-identical and still pinned: DATA algorithm /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_controls_final.py
19a79b56ee1a7e74e4822cedceb708fbf9d11bbae78bfded937f7cae9ed04e11 and DATA entrypoint /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext2_entry_data_final.py
4558fdf11781f861fb9be1ae9d3f7fb73e1fb9bc6696297ea684a15d807ba4cf (its wrapper constants still match), scope note, spec v2,
joint README, Lemma U format v2, DM21 and anchor raws, governing correction fabe57ab. Unpinned superseded intermediate:
/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor3-resources-v2.md 09e151d089fe128e7944522ff782880fbc3dc121486dd0a5dc327210b36f4e80 (see Notes).

## Gate supplement MAJOR 1 — deadline expiry precedence on every publication return
Sites named: joint emergency completion io_v4:674, joint ordinary stdout-error return io_v4:704-705, beta print-error
return ext2_beta_final:367. Every beta and joint publication return now checks the self-deadline and returns 5 once it
has passed.

Beta. Old ext2_beta_final.py:365-369:
```python
    # If a write fails after emitting bytes, fail quietly; never append a second line.
    try:print(data.decode('ascii'),end='',flush=True)
    except OSError:return CODES['IO_ERROR']
    if deadline is not None and time.monotonic()>deadline:return CODES['INCOMPLETE_BUDGET']
    return CODES[out['status']]
```
New ext3_beta.py:366-373 (new lines 367, 369-371):
```python
    # If a write fails after emitting bytes, fail quietly; never append a second line.
    # Deadline expiry takes precedence on this return as well: a late failed stdout write exits 5.
    try:print(data.decode('ascii'),end='',flush=True)
    except OSError:
        if deadline is not None and time.monotonic()>deadline:return CODES['INCOMPLETE_BUDGET']
        return CODES['IO_ERROR']
    if deadline is not None and time.monotonic()>deadline:return CODES['INCOMPLETE_BUDGET']
    return CODES[out['status']]
```
All beta returns: 370 (late stdout error -> 5), 371 (IO_ERROR only when not late), 372 (late completion -> 5), 373
(status code after the 372 check). The file-error branch (ext3_beta:361-363) is not a return; it re-serializes through
serialized(), whose first publication_expired() relabels INCOMPLETE_BUDGET, and then reaches 364-373. Counterexample
re-traced: B-BAD_PIN result.json complete, stdout prefix written, deadline passes, next write raises OSError -> line 370
returns 5, never the intended exit 2. Nothing is rewritten or appended.

Joint emergency. Old io_v4:636-674:
```python
def emergency(result, status, reason, clock, fd):
    # Best effort after output I/O or an unexpected publication failure. Never
    # reopen/overwrite any already-created result.json, including our own.
    compact_error(result, status, reason)
    result.update(m=None, chunk_lo=None, chunk_hi=None)
    try:
        result["wall_s"] = clock.wall()
        payload = (json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
    except Exception:
        result = new_result()
        result.update(status=status, reason=reason)
        payload = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    if fd is not None:
        # An artifact already created by this invocation is immutable, even if
        # the first write failed. The supervisor must reject any disagreement.
        try:
            os.close(fd)
        except OSError:
            pass
    else:
        try:
            fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        except OSError:
            fd = None
        if fd is not None:
            try:
                write_all(fd, payload)
            except OSError:
                pass
            finally:
                try:
                    os.close(fd)
                except OSError:
                    pass
    try:
        write_all(1, payload)
    except OSError:
        pass
    return CODES[status]
```
New io_v5:638-705:
```python
def emergency(result, status, reason, clock, fd, file_published):
    # Terminal best-effort report after output I/O or an unexpected publication
    # failure, or after the deadline once result.json was complete. publish calls
    # it exactly once, AFTER its exception handlers: an exception escaping from
    # here propagates (the wrapper exits quietly with 94) and can never start
    # another report. Never reopen/overwrite any already-created result.json,
    # including our own. Deadline expiry takes precedence on every return.
    def encode():
        compact_error(result, status, reason)
        result.update(m=None, chunk_lo=None, chunk_hi=None)
        try:
            result["wall_s"] = clock.wall()
            return (json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
        except Exception:
            fallback = new_result()
            fallback.update(status=status, reason=reason)
            return (json.dumps(fallback, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")

    def unpublished_checkpoint():
        # Expiry checkpoint, used only while NO byte of this report is published:
        # a late report is relabelled INCOMPLETE_BUDGET and then (re)serialized.
        nonlocal status, reason
        if status != "INCOMPLETE_BUDGET" and clock.expired():
            reason = "self-budget expired during " + status + " emergency publication (" + reason + ")"
            status = "INCOMPLETE_BUDGET"
            return True
        return False

    unpublished_checkpoint()  # before serialization
    payload = encode()
    if unpublished_checkpoint():  # after serialization
        payload = encode()
    if fd is not None:
        # An artifact already created by this invocation is immutable, even if
        # the first write failed. The supervisor must reject any disagreement.
        try:
            os.close(fd)
        except OSError:
            pass
    elif not file_published:
        if unpublished_checkpoint():  # before the exclusive create
            payload = encode()
        try:
            fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        except OSError:
            fd = None
        if fd is not None:
            try:
                if unpublished_checkpoint():  # after the create, before the first byte
                    payload = encode()
                write_all(fd, payload)
            except OSError:
                pass
            finally:
                try:
                    os.close(fd)
                except OSError:
                    pass
    # From here this report may exist on disk: its payload is frozen and never
    # re-serialized; stdout receives those identical bytes at most once.
    try:
        write_all(1, payload)
    except OSError:
        pass
    # Completion checkpoint after file and stdout publication: expiry -> exit 5.
    if clock.expired():
        return CODES["INCOMPLETE_BUDGET"]
    return CODES[status]
```
Emergency checkpoints: before serialization (666), after serialization (668-669), before the exclusive create (678-679),
after the create and before its first byte (686-687); each relabels INCOMPLETE_BUDGET (helper 656-664) only while no
byte of the emergency report is published. After the last unpublished checkpoint the payload is frozen (696-701):
written evidence is preserved, never re-serialized, rewritten or followed by a correction; stdout gets the identical
bytes at most once. Completion checkpoint 703-704: once expired the emergency returns 5 (old 674 returned
CODES[status]). Counterexample re-traced: ordinary file-write OSError -> emergency(IO_ERROR); deadline crosses during
emergency serialization -> 668 relabels and re-encodes INCOMPLETE_BUDGET -> exit 5; crosses during emergency stdout ->
703 returns 5.

Joint ordinary stdout-error returns. Old io_v4:703-710 returned CODES["IO_ERROR"] / CODES["INTERNAL_ERROR"] after
stdout started. New io_v5:737-740 and 742-744:
```python
    except OSError as exc:
        if stdout_started:
            # No second line after a partial/final algorithm publication; expiry still takes precedence.
            return CODES["INCOMPLETE_BUDGET"] if clock.expired() else CODES["IO_ERROR"]
        failure = ("IO_ERROR", "publication OSError errno=" + str(exc.errno))
    except Exception as exc:
        if stdout_started:
            return CODES["INCOMPLETE_BUDGET"] if clock.expired() else CODES["INTERNAL_ERROR"]
        failure = ("INTERNAL_ERROR", "publication exception " + type(exc).__name__)
```
Counterexample re-traced: J-BAD_PIN valid rejection file closed, ordinary stdout prefix, deadline passes, next write
raises OSError -> 740 returns 5, not the intended exit 2. The completed ordinary return keeps its 734-736 check.

## Gate supplement MAJOR 2 — emergency publication is terminal
Old io_v4:677-710 (publish):
```python
def publish(result, clock):
    fd = None
    stdout_started = False
    try:
        buffer = bytearray(RESULT_CAP)
        payload = render(result, clock, buffer)
        # Check immediately before the exclusive create/write as well.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        # An open/create delay may consume the budget before the first byte.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        write_all(fd, payload)
        os.close(fd)
        fd = None
        # Fresh check after file completion and before stdout. Preserve immutable artifact on overrun.
        if clock.expired():
            return emergency(result, "INCOMPLETE_BUDGET", "deadline after file publication", clock, None)
        stdout_started = True
        write_all(1, payload)
        # Never rewrite an artifact after publication. A late overrun is an
        # exit-code/status mismatch that the supervisor must reject as UNKNOWN.
        if clock.expired():
            return CODES["INCOMPLETE_BUDGET"]
        return CODES[result["status"]]
    except OSError as exc:
        if stdout_started:
            return CODES["IO_ERROR"]  # no second line after a partial/final algorithm publication
        return emergency(result, "IO_ERROR", "publication OSError errno=" + str(exc.errno), clock, fd)
    except Exception as exc:
        if stdout_started:
            return CODES["INTERNAL_ERROR"]
        return emergency(result, "INTERNAL_ERROR", "publication exception " + type(exc).__name__, clock, fd)
```
New io_v5:708-749:
```python
def publish(result, clock):
    fd = None
    stdout_started = False
    file_published = False
    try:
        buffer = bytearray(RESULT_CAP)
        payload = render(result, clock, buffer)
        # Check immediately before the exclusive create/write as well.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        fd = os.open("result.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        # An open/create delay may consume the budget before the first byte.
        if late_budget(result, clock):
            payload = render(result, clock, buffer)
        write_all(fd, payload)
        os.close(fd)
        fd = None
        file_published = True
        # Fresh check after file completion and before stdout. Preserve immutable artifact on overrun.
        if clock.expired():
            failure = ("INCOMPLETE_BUDGET", "deadline after file publication")
        else:
            stdout_started = True
            write_all(1, payload)
            # Never rewrite an artifact after publication. A late overrun is an
            # exit-code/status mismatch that the supervisor must reject as UNKNOWN.
            if clock.expired():
                return CODES["INCOMPLETE_BUDGET"]
            return CODES[result["status"]]
    except OSError as exc:
        if stdout_started:
            # No second line after a partial/final algorithm publication; expiry still takes precedence.
            return CODES["INCOMPLETE_BUDGET"] if clock.expired() else CODES["IO_ERROR"]
        failure = ("IO_ERROR", "publication OSError errno=" + str(exc.errno))
    except Exception as exc:
        if stdout_started:
            return CODES["INCOMPLETE_BUDGET"] if clock.expired() else CODES["INTERNAL_ERROR"]
        failure = ("INTERNAL_ERROR", "publication exception " + type(exc).__name__)
    # Every non-returning path above assigned failure. The single terminal
    # emergency report runs OUTSIDE those handlers, so nothing it raises can
    # start a second report.
    return emergency(result, failure[0], failure[1], clock, fd, file_published)
```
Chosen option: move the emergency OUTSIDE publish's catch region. The three old in-handler call sites (io_v4:695, 706,
710) now only record `failure` (io_v5:727-728, 741, 745); the single call io_v5:749 follows the try/except. An exception
escaping emergency (e.g. MemoryError after a stdout prefix at write_all, io_v5:632) propagates out of publish and out of
main (io_v5:799 `return publish(result, clock)` has no handler) to the wrapper's `except BaseException: os._exit(94)`
(ext3_entry_joint.py:232-235): no second report can start. `file_published` (711, 725) makes the post-file-expiry
emergency attempt NO create at all (677), instead of relying on an O_EXCL failure. Counterexample re-traced: ordinary
file complete -> 727-728 -> emergency at 749 -> stdout prefix -> MemoryError -> propagates -> quiet 94; emergency is
never re-entered. The accepted prefix-then-OSError behaviours are unchanged: retained descriptor closed only (670-676),
ordinary stdout failure silent after start (738-744), emergency stdout OSError swallowed once (698-701).

Joint publication path table (io_v5), at most one stdout line, O_CREAT|O_EXCL|O_NOFOLLOW creates only, no reopen:
|path|file|stdout|exit|
|---|---|---|---|
|ordinary file+stdout complete|ordinary payload|same bytes|5 if expired at 734, else CODES[status]|
|ordinary file complete, expired before stdout|preserved, no create|one INCOMPLETE_BUDGET emergency record|5|
|ordinary stdout fails after start|preserved|partial/complete ordinary line, nothing appended|5 if expired, else 2 or 4|
|failure before any file of ours exists|one emergency O_EXCL attempt|one emergency record|5 if expired, else 2 or 4|
|failure with our descriptor retained|partial/empty, closed only|one emergency record|5 if expired, else 2 or 4|
|exception escaping emergency, or any BaseException|preserved|nothing further|wrapper quiet 94|
Intended J-BAD_PIN (2) and J-BAD_DM (3) exits arise only from the ordinary completed path with no expiry at 734.

## Gate supplement MINOR 3 — beta decimal argument conversion
Old ext2_beta_final.py:48-49:
```python
            if not s.isascii() or not s.isdigit():raise Halt('BAD_INPUT','nonnegative decimal integer required')
            d[key]=int(s)
```
New ext3_beta.py:48-50:
```python
            if not s.isascii() or not s.isdigit():raise Halt('BAD_INPUT','nonnegative decimal integer required')
            try:d[key]=int(s)
            except ValueError:raise Halt('BAD_INPUT','decimal integer conversion rejected') from None
```
A digit-only argument beyond the interpreter integer-string limit now yields Halt('BAD_INPUT', ...) (exit 2) before any
raw read; it no longer reaches the catch-all `except Exception` INTERNAL_ERROR (old :324, new ext3_beta.py:325, unchanged),
matching the raw-token mapping (ext3_beta.py:74-75) and joint decimal() (io_v5:76-83). No planned control uses this site.

## Math MINOR m2 — guard-clock statement
Old ext-search-successor2-resources-v1.md:41:
```text
they are not charged to every nonleaf. Guard-clock overhead (B calls<=r+1 per visit, H bounded constant) is separate.
```
New ext-search-successor3-resources-v3.md:49-53 (required phrase verbatim on line 50):
```text
they are not charged to every nonleaf. Guard-clock overhead is separate and per visit:
B-core guard calls <= u+1 <= r+1, plus <= k calls for each adjacency construction (once per feasible B leaf,
before the H-root call); H calls exactly 1 per visit. E.g. review corner P57 m56 r0: 1+7=8 calls precede the
H-root call. Per-chunk, raw-read, input-validation and publication clock reads are further separate, non-per-node
costs. Clock work is outside I/U/C/A as before.
```
Source basis (no execution): node() one check per visit (ext3_beta.py:97-100); b_pick one check per scanned unassigned
column, <=u (115-116); neighbours one check per row, k per adjacency construction (128-131), evaluated at each feasible B
leaf before the H-root node() (search 179; probe 197, then loop-head node() 191); h_pick/retain make none. Formulas, tables, frame and storage
terms are carried verbatim (resources v3 header l.3-10). Every reference repinned: plan v4 pins (lines 722-723),
resource_authority (812-813), resources.documents (836-837); v1 and the v2 intermediate are listed only under
resources.superseded_resource_documents (848, 853).

## Preserved blocks (source bytes only)
- beta Engine: ext3_beta.py lines 80-211, bytes 4449..9335, 4887 B, sha256 233bd15e3472b010c4f85078927202fc0fdfcc238c0b5fc909215f1b9b315b59
  (successor2 lines 79-210 at byte 4174): identical.
- joint search: io_v5 lines 267-576, bytes 9520..20690, 11171 B, sha256 020100eebbd493a417e798354e5547e2777eaafd9dc6409d07841de39f7c60b7
  (io_v4 lines 265-574 at byte 9318): identical.
Convention: from the class Engine / def tree_bound(r): line to (excluding) the next top-level def line; grep -b + dd|shasum.
diff confirms beta changes only l.2, 49-50, 367, 369-371; joint only l.3-4, 638-705, 708-749; gate only l.2;
entrypoints only l.2 and 65-67. Joint still imports no beta/producer code; PROGRAM names unchanged (beta
'ext_search_beta_v5' l.25, joint 'ext_search_joint_v1' l.22), so plan program_name fields are unchanged.

## FIXED rulings not regressed
- F1, M1, M3 (gate validator), M4: gate logic byte-identical; only docstring line 2 changed.
- M2 (all actual consumers): every anchored_parent/anchored_file_fd/anchored_read_bytes and caller in beta, joint,
  DATA, gate and all wrappers byte-identical (diff hunks above touch none of them); wrapper preflight still reads no raw bytes.
- m1: wrapper quiet 94 after main entry unchanged (ext3_entry_*:232-237); joint failures after stdout start stay silent.
- m2: gate header names final plan v4; contract v2 Authority and integration v3 name plan v4, keep e441d858 WITHDRAWN
  and governing fabe57ab; all 7 literal gate --plan paths are plan v4 (metadata v2).
- DATA put: DATA algorithm and entrypoint unchanged. DATA/gate expect exit 0 only, so their reviewed non-zero
  publication returns cannot coincide with an intended exit (contract v2 l.96-97).
- Math M1 work bound and m1 storage: Engine block unchanged; resources v3 carries every formula/table verbatim.
- Reject taxonomy: beta PIN/NOT_DM sites and reasons, joint sites and reasons, and all per-status metadata unchanged.

## Repinning
Plan v4 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v4.json
sha256 06bee9f7211bb24845d8cb574e3f16eb213f9d4e7b6af8d2421509cd175b4130: format ext-search-plan-v4; 18 pins (9 replaced, 9 carried); programs beta/joint/gate
repinned, DATA carried; 7 gate --plan literals = plan v4; contract/resource/integration authorities repinned;
supersedes_unexecuted = plan v3; answers_reviews added. Output roots moved to runs-ext-search-v3 and
mols39-ext-search-v3-audits (neither exists) to keep artifacts bound to this code identity, following the v2 -> v3 practice.
All 20 job names/order/domains/expected statuses/reasons/exits/outputs and both calibration parameter sets unchanged
apart from those root paths. Metadata verification v2 /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-successor3-metadata-v2.json
sha256 87a7feb3eacb03e404d6eaeeb920ef2b8e56e0a4a971a0f1888676c9a37d1258: all 18 pins actual==recorded, regular, one link; 4 programs plan==actual with wrapper
ALGO_PATH/ALGO_SHA256 equal; operative stale-reference hits 0.

## Notes and deviations
- resources v2 (09e151d0...) was frozen first with the required phrase broken across a line; v3 puts it on one line.
  v3's header calls the difference "only a line break inside the required phrase"; precisely, v2 and v3 carry
  word-identical corrected text that differs in line wrapping, plus their own title/header lines. v2 is never pinned.
- The ordinary post-file-expiry stdout INCOMPLETE_BUDGET record (file preserved, exit 5) is the reviewed successor2
  behaviour, now produced by the single terminal emergency without a create attempt.
- No gate or DATA publication logic was changed; the MAJOR 1 sites are beta/joint only.
- Lane checkpoint cp-021 (10:02:45, 313beea9...) was written but not sent to the parent by IRC; after the parent
  request (parent /bin/date 10:23:58) cp-022 (10:25:11, d72dac66...) was sent. No lane checkpoint gap exceeded 1800 s.

## Scope and state
Source successor only. Requires both owner re-reviews, an independently qualified supervisor (governing fabe57ab, owned
bounded /bin/date helper, conservative ownership/unresolved census) and one exact parent GO per job before any control.
e441d858 remains withdrawn. No job, calibration or target allocation launched. Existing exact-anchor Lemma U
computer-assisted scoped acceptance and corrected R1 stand; both extension questions UNKNOWN; six MOLS(39) OPEN. No new
witness, nonexistence, novelty, priority or scientific result.
