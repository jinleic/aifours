#!/usr/bin/env python3
"""MOLS39 N1 fault-case DRIVER v1 (ContinueCFR21c). WRITTEN ONLY. Never run without an exact parent GO for ONE case.

Parent launch, one case per invocation (no autochain, polling or retry):
    printf 'GO\n' | PYTHON_APP -I -B <this file> --case CASE
Without exactly b"GO\n" on stdin within 120 s the driver exits 97 silently (lane entrypoint protocol).

Before any child: digests of the pinned child source, PYTHON_APP, the case's entrypoint and algorithm; exclusive
creation of OUT_ROOT/CASE/{input,job} and of the fixture (exact DATA neg6.raw bytes). Then one bounded /bin/date
helper, exactly one fault child (PYTHON_APP -I -B, new session, pinned child, ACTUAL pinned entrypoint), complete
stdout/stderr capture to EOF (stored up to caps), bounded waits, at most one SIGTERM per owned unreaped process
group and never SIGKILL, the actual exit status, a group-closure probe, bounded ps/lsof census helpers, a final
bounded /bin/date helper and exclusive-create evidence files plus one receipt.

The driver records evidence and mechanical byte relations only. It issues NO verdict, NO audit record and NO
release record: the parent's five-part release transaction judges. INSTRUMENTED RawIO faults live in the child and
are labelled there; no clock or /bin/date output is faked. Exit: 0 evidence recorded without anomaly, 1 evidence
recorded with anomaly, 2 refused before any child, 97 no GO.
"""
import os
import select
import sys
import time

_T0 = time.monotonic()
GO_WAIT_S = 120.0


def _no_go():
    os._exit(97)


def _await_go():
    buf = b""
    while len(buf) < 3:
        remaining = GO_WAIT_S - (time.monotonic() - _T0)
        if remaining <= 0:
            _no_go()
        try:
            ready, _, _ = select.select([0], [], [], remaining)
        except (OSError, ValueError):
            _no_go()
        if not ready:
            _no_go()
        try:
            chunk = os.read(0, 3 - len(buf))
        except OSError:
            _no_go()
        if not chunk:
            _no_go()
        buf += chunk
        if time.monotonic() - _T0 >= GO_WAIT_S:
            _no_go()
    if buf != b"GO\n":
        _no_go()
    try:
        ready, _, _ = select.select([0], [], [], 0)
        if ready and os.read(0, 1):
            _no_go()
    except (OSError, ValueError):
        _no_go()
    if time.monotonic() - _T0 >= GO_WAIT_S:
        _no_go()


_await_go()

import hashlib
import json
import re
import resource
import signal
import stat
import subprocess

FORMAT = "mols39-n1-fault-receipt-v1"
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39"
EVIDENCE = LANE + "/evidence"
OUT_NAME = "n1-fault-v1"
OUT_ROOT = EVIDENCE + "/" + OUT_NAME
DRIVER_PATH = LANE + "/code/n1_fault_driver_v1.py"
MAPPING = EVIDENCE + "/ext-search-n1-fault-mapping-v1.md"
CHILD = (LANE + "/code/n1_fault_child_v1.py", "c47c23ab2ac99f73b8f604a1abd751fdccb3f8a60f32f54ca8e355096d111757")
PYTHON_APP = ("/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/"
              "Python.app/Contents/MacOS/Python",
              "7ecc1ecbf9daa9303c4bf502ff62ffdd9010ed5c08729d470ae9380c10ce1211")
IMPLS = {
    "ext4": {"entry": (LANE + "/code/ext4_entry_beta.py",
                       "c6c21b83b3190685b3559c2ae08ba345ab3c931a986026d7fcab586909c656eb"),
             "algorithm": (LANE + "/code/ext4_beta.py",
                           "a319a4be1cc219a2de4c53211ac61cabc42bdc19d000f8bc740c6e4bc262b978")},
    "ext3": {"entry": (LANE + "/code/ext3_entry_beta.py",
                       "94c60282c01135ca108d8a1a894e03ff76c3074e5aa2701435aee584ee51c4f3"),
             "algorithm": (LANE + "/code/ext3_beta.py",
                           "33200e9d3e80ccb71b635bcd18ffe7082b2677f254ca182f99fa78a82d463873")},
}
FIXTURE_NAME = "neg6.raw"
FIXTURE_BYTES = b"0 0 0 0 0 0\n0 1 2 3 4 5\n"
FIXTURE_SHA256 = "32ae7f1897aa091c68d97a731ad912d4c93acf07bb09e45302be2f4bda8c2209"
BAD_PIN = "70c8c2e579961ead65bb2abf03cc2d86cc799d1976f31d5333b52b26a142e825"
# case: (implementation, prefix_bytes, fault, sleep_s, budget_s, role)
CASES = {
    "B0": ("ext4", 0, "none", "0", "240", "POSITIVE baseline: no fault, complete stdout"),
    "C1": ("ext4", 0, "wouldblock", "0", "240", "REQUIRED N1: empty capture x unexpired deadline"),
    "C2": ("ext4", 64, "wouldblock", "0", "240", "REQUIRED N1: strict-prefix capture x unexpired deadline"),
    "C3": ("ext4", 0, "wouldblock", "3", "2", "REQUIRED N1: empty capture x expired deadline"),
    "C4": ("ext4", 64, "wouldblock", "3", "2", "REQUIRED N1: strict-prefix capture x expired deadline"),
    "A5": ("ext4", 0, "none", "3", "2", "AUDIT EVIDENCE: complete stdout, deadline passes inside the write"),
    "A94": ("ext4", 0, "interrupt", "0", "240", "AUDIT EVIDENCE: complete stdout, escaping BaseException, quiet 94"),
    "S1": ("ext3", 64, "wouldblock", "0", "240", "SENSITIVITY on superseded ext3: shutdown retry expected"),
    "S2": ("ext3", 64, "wouldblock", "3", "2", "SENSITIVITY on superseded ext3: late shutdown retry expected"),
}
BUFFER_SIZE = 8192
CHILD_WALL_S = 45.0
TERM_GRACE_S = 10.0
HELPER_WALL_S = 10.0
HELPER_GRACE_S = 5.0
STREAM_CAP = 1 << 20
FILE_CAP = 1 << 20
APP_CAP = 64 << 20
CHILD_ENV = {"PATH": "/usr/bin:/bin", "LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
             "TMPDIR": LANE + "/tmp", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
             "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1"}
HELPER_ENV = {"PATH": "/usr/bin:/bin:/usr/sbin", "LC_ALL": "C", "LANG": "C"}
DATE_ARGV = ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"]
PS_ARGV = ["/bin/ps", "-A", "-o", "pid=,ppid=,pgid=,uid="]
LSOF_ARGV = ["/usr/sbin/lsof", "-nP", "-w", "-d", "cwd", "-F", "pn"]
DATE_RE = re.compile(rb"\A[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}[+-][0-9]{4}\n\Z")


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _emit_line(obj, code):
    line = (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    view = memoryview(line)
    try:
        while view:
            count = os.write(1, view)
            if count <= 0:
                break
            view = view[count:]
    except OSError:
        pass
    os._exit(code)


def _refuse(reason):
    _emit_line({"format": FORMAT, "status": "REFUSED_BEFORE_CHILD", "reason": reason}, 2)


def _anchored_dir(path):
    if type(path) is not str or not path.startswith("/") or "\x00" in path:
        raise OSError("absolute normalized directory path required")
    parts = path.split("/")[1:]
    if not parts or any(p in ("", ".", "..") for p in parts):
        raise OSError("non-normalized directory path")
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        return fd
    except BaseException:
        os.close(fd)
        raise


def _read_at(dir_fd, name, cap):
    """Regular one-link leaf relative to dir_fd, NONBLOCK|NOFOLLOW, size<=cap, cap+1 consumption."""
    fd = os.open(name, os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=dir_fd)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size > cap:
            raise OSError("file kind/link/cap")
        blocks, total = [], 0
        while True:
            block = os.read(fd, min(65536, cap + 1 - total))
            if not block:
                break
            total += len(block)
            if total > cap:
                raise OSError("file grew beyond cap")
            blocks.append(block)
        after = os.fstat(fd)
        if after.st_nlink != 1:
            raise OSError("file link count changed")
        meta = {"dev": after.st_dev, "ino": after.st_ino, "nlink": after.st_nlink,
                "mode": stat.S_IMODE(after.st_mode), "size": after.st_size}
        return b"".join(blocks), meta
    finally:
        os.close(fd)


def _read_path(path, cap):
    parent, sep, name = path.rpartition("/")
    if not sep or not parent or name in ("", ".", ".."):
        raise OSError("absolute normalized file path required")
    dfd = _anchored_dir(parent)
    try:
        return _read_at(dfd, name, cap)
    finally:
        os.close(dfd)


def _xwrite_at(dir_fd, name, data, mode):
    """Exclusive create, complete write, close, then same-name readback and digest/meta record."""
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode, dir_fd=dir_fd)
    try:
        view = memoryview(data)
        while view:
            count = os.write(fd, view)
            if count <= 0:
                raise OSError("zero write")
            view = view[count:]
    finally:
        os.close(fd)
    back, meta = _read_at(dir_fd, name, max(len(data), 1))
    if back != data:
        raise OSError("readback mismatch " + name)
    meta["sha256"] = _sha(back)
    return meta


def _pins(items):
    out = []
    for role, path, want, cap in items:
        rec = {"role": role, "path": path, "pinned_sha256": want}
        try:
            data, meta = _read_path(path, cap)
            rec["observed_sha256"] = _sha(data)
            rec["bytes"] = len(data)
            rec["meta"] = meta
        except OSError as exc:
            rec["error"] = type(exc).__name__ + ": " + str(exc)
        rec["match"] = rec.get("observed_sha256") == want
        out.append(rec)
    return out


def _probe_group(pgid):
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return "EMPTY"
    except PermissionError:
        return "MEMBER_OTHER_UID"
    except OSError as exc:
        return "PROBE_ERROR_" + type(exc).__name__
    return "MEMBERS_PRESENT"


def _sigterm_once(proc, group_ok, history, why):
    """At most one SIGTERM per owned process; only while unreaped, so its pid/pgid identity is still ours."""
    rec = {"why": why, "t_monotonic": time.monotonic(), "pid": proc.pid, "group": group_ok, "sent": False}
    if any(h.get("sent") for h in history):
        rec["skipped"] = "a SIGTERM was already sent to this process"
    elif proc.poll() is not None:
        rec["skipped"] = "already reaped; identity no longer provable"
    else:
        try:
            if group_ok:
                os.killpg(proc.pid, signal.SIGTERM)
            else:
                os.kill(proc.pid, signal.SIGTERM)
            rec["sent"] = True
        except OSError as exc:
            rec["error"] = type(exc).__name__
    return rec


def _helper(argv, purpose):
    """Bounded owned helper: new session, captured streams, at most one SIGTERM, never SIGKILL."""
    rec = {"purpose": purpose, "argv": list(argv), "settled": False, "signals": []}
    t = time.monotonic()
    try:
        proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                close_fds=True, start_new_session=True, env=HELPER_ENV, cwd="/")
    except OSError as exc:
        rec["spawn_error"] = type(exc).__name__
        return rec, None
    rec["pid"] = proc.pid
    # Popen(start_new_session=True) runs setsid() in the child before exec and fails loudly otherwise, so the
    # unreaped helper leads its own group: pgid == pid by construction. The observation is recorded only.
    group_ok = True
    try:
        rec["pgid_observed"] = os.getpgid(proc.pid)
    except OSError as exc:
        rec["pgid_observed_error"] = type(exc).__name__
    try:
        out, err = proc.communicate(timeout=HELPER_WALL_S)
    except subprocess.TimeoutExpired:
        rec["signals"].append(_sigterm_once(proc, group_ok, rec["signals"], purpose + " wall"))
        try:
            out, err = proc.communicate(timeout=HELPER_GRACE_S)
        except subprocess.TimeoutExpired:
            rec["wall_s"] = time.monotonic() - t
            return rec, None
    rec["returncode"] = proc.returncode
    rec["group_after_reap"] = _probe_group(proc.pid)
    rec["stdout_len"] = len(out)
    rec["stdout_sha256"] = _sha(out)
    rec["stderr_len"] = len(err)
    rec["stderr_sha256"] = _sha(err)
    rec["wall_s"] = time.monotonic() - t
    rec["settled"] = rec["group_after_reap"] == "EMPTY"
    return rec, out


def _date(purpose):
    rec, out = _helper(DATE_ARGV, purpose)
    value = None
    if out is not None and rec.get("returncode") == 0 and DATE_RE.match(out):
        value = out[:-1].decode("ascii")
    rec["value"] = value
    return rec


def _census(child_pid, child_pgid, case_dir, own_pids):
    hits = []
    ps_rec, ps_out = _helper(PS_ARGV, "census ps")
    ps_rows = None
    if ps_out is not None and ps_rec.get("returncode") == 0:
        ps_rows = 0
        for line in ps_out.decode("ascii", "replace").splitlines():
            fields = line.split()
            if len(fields) != 4 or not all(f.isdigit() for f in fields):
                ps_rows = None
                break
            pid, ppid, pgid, uid = (int(f) for f in fields)
            ps_rows += 1
            if pid not in own_pids and (pid == child_pid or ppid == child_pid or pgid == child_pgid):
                hits.append({"source": "ps", "pid": pid, "ppid": ppid, "pgid": pgid, "uid": uid})
    lsof_rec, lsof_out = _helper(LSOF_ARGV, "census lsof cwd")
    lsof_ok = lsof_out is not None and lsof_rec.get("returncode") in (0, 1) and len(lsof_out) > 0
    if lsof_ok:
        current = None
        for line in lsof_out.decode("utf-8", "replace").splitlines():
            if line.startswith("p") and line[1:].isdigit():
                current = int(line[1:])
            elif line.startswith("n") and current is not None and current not in own_pids:
                path = line[1:]
                if path == case_dir or path.startswith(case_dir + "/"):
                    hits.append({"source": "lsof_cwd", "pid": current, "cwd": path})
    census = {"ps": ps_rec, "ps_rows": ps_rows, "lsof": lsof_rec, "lsof_parsed": lsof_ok, "hits": hits,
              "complete": ps_rows is not None and lsof_ok}
    return census, ps_out, lsof_out


def _supervise(proc, group_ok, t_spawn):
    """Read stdout/stderr to EOF (stored up to STREAM_CAP), then reap; one SIGTERM at most; never SIGKILL."""
    signals, anomalies = [], []
    streams = {"stdout": {"fd": proc.stdout.fileno(), "data": bytearray(), "seen": 0, "eof": False, "over_cap": False},
               "stderr": {"fd": proc.stderr.fileno(), "data": bytearray(), "seen": 0, "eof": False, "over_cap": False}}
    state = {"deadline": t_spawn + CHILD_WALL_S, "grace": False}

    def escalate(why):
        anomalies.append(why)
        if state["grace"]:
            return False
        state["grace"] = True
        state["deadline"] = time.monotonic() + TERM_GRACE_S
        signals.append(_sigterm_once(proc, group_ok, signals, why))
        return True

    while not (streams["stdout"]["eof"] and streams["stderr"]["eof"]):
        now = time.monotonic()
        if now >= state["deadline"]:
            if escalate("child wall reached before stream EOF"):
                continue
            anomalies.append("UNSETTLED: stream EOF not reached after SIGTERM grace")
            break
        waiting = [s["fd"] for s in streams.values() if not s["eof"]]
        ready, _, _ = select.select(waiting, [], [], state["deadline"] - now)
        for name in ("stdout", "stderr"):
            s = streams[name]
            if s["eof"] or s["fd"] not in ready:
                continue
            chunk = os.read(s["fd"], 65536)
            if not chunk:
                s["eof"] = True
                continue
            s["seen"] += len(chunk)
            room = STREAM_CAP - len(s["data"])
            if room > 0:
                s["data"] += chunk[:room]
            if s["seen"] > STREAM_CAP and not s["over_cap"]:
                s["over_cap"] = True
                escalate(name + " exceeded capture cap")
    returncode = None
    while True:
        remaining = max(0.0, state["deadline"] - time.monotonic())
        try:
            returncode = proc.wait(timeout=remaining)
            break
        except subprocess.TimeoutExpired:
            if escalate("child not reaped within wall"):
                continue
            anomalies.append("UNSETTLED: child not reaped after SIGTERM grace")
            break
    return streams, returncode, signals, anomalies


def _trace_records(data):
    records, errors = [], 0
    for line in data.split(b"\n"):
        if not line:
            continue
        try:
            value = json.loads(line.decode("ascii"))
        except (ValueError, UnicodeError):
            errors += 1
            continue
        if type(value) is dict:
            records.append(value)
        else:
            errors += 1
    return records, errors


def _relations(stdout, result, trace, driver_pid):
    rel = {"stdout_len": len(stdout), "stdout_lf_count": stdout.count(b"\n"), "stdout_empty": len(stdout) == 0,
           "result_json_present": result is not None}
    if result is not None:
        rel["result_json_len"] = len(result)
        rel["result_json_fits_buffer"] = len(result) <= BUFFER_SIZE
        rel["stdout_equals_result_json"] = stdout == result
        rel["stdout_strict_prefix_of_result_json"] = 0 < len(stdout) < len(result) and result.startswith(stdout)
    starts = [r for r in trace if r.get("record") == "start"]
    calls = [r for r in trace if r.get("record") != "start"]
    rel["trace_start_records"] = len(starts)
    if len(starts) == 1:
        rel["trace_start_ppid_is_driver"] = starts[0].get("ppid") == driver_pid
        rel["trace_start_pid"] = starts[0].get("pid")
    rel["trace_write_calls"] = len(calls)
    rel["trace_actions"] = [r.get("action") for r in calls]
    rel["trace_requested"] = [r.get("requested") for r in calls]
    written = [r.get("written") for r in calls]
    rel["trace_bytes_written_total"] = sum(w for w in written if type(w) is int)
    after = [r for r in calls if r.get("action") == "pass_after_plan"]
    rel["trace_calls_after_plan"] = len(after)
    rel["trace_bytes_after_plan"] = sum(r.get("written") for r in after if type(r.get("written")) is int)
    for r in calls:
        if "sleep_requested_s" in r:
            rel["trace_sleep_requested_s"] = r.get("sleep_requested_s")
            enter, leave = r.get("t_monotonic_enter"), r.get("t_monotonic_before_return")
            if type(enter) is float and type(leave) is float:
                rel["trace_sleep_call_observed_s"] = leave - enter
    rel["stdout_len_equals_trace_bytes"] = len(stdout) == rel["trace_bytes_written_total"]
    return rel


def main():
    t_start = time.monotonic()
    argv = sys.argv[1:]
    if len(argv) != 2 or argv[0] != "--case" or argv[1] not in CASES:
        _refuse("argv must be exactly --case " + "|".join(sorted(CASES)))
    case = argv[1]
    impl, prefix, fault, sleep_s, budget_s, role = CASES[case]
    entry, entry_sha = IMPLS[impl]["entry"]
    algorithm, algorithm_sha = IMPLS[impl]["algorithm"]
    pin_items = [("child", CHILD[0], CHILD[1], FILE_CAP), ("python_app", PYTHON_APP[0], PYTHON_APP[1], APP_CAP),
                 ("entry", entry, entry_sha, FILE_CAP), ("algorithm", algorithm, algorithm_sha, FILE_CAP)]
    pins_before = _pins(pin_items)
    for rec in pins_before:
        if not rec["match"]:
            _refuse("pin mismatch before child: " + rec["role"])
    try:
        driver_data, _meta = _read_path(DRIVER_PATH, FILE_CAP)
        driver_sha = _sha(driver_data)
    except OSError as exc:
        driver_sha = None
    case_dir = OUT_ROOT + "/" + case
    job_dir = case_dir + "/job"
    fixture = case_dir + "/input/" + FIXTURE_NAME
    try:
        ev_fd = _anchored_dir(EVIDENCE)
        try:
            try:
                os.mkdir(OUT_NAME, 0o700, dir_fd=ev_fd)
            except FileExistsError:
                pass
            root_fd = os.open(OUT_NAME, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=ev_fd)
        finally:
            os.close(ev_fd)
        info = os.fstat(root_fd)
        if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o022:
            raise OSError("output root ownership or mode")
        os.mkdir(case, 0o700, dir_fd=root_fd)
        case_fd = os.open(case, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=root_fd)
        os.close(root_fd)
        os.mkdir("input", 0o700, dir_fd=case_fd)
        os.mkdir("job", 0o700, dir_fd=case_fd)
        input_fd = os.open("input", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=case_fd)
        try:
            fixture_meta = _xwrite_at(input_fd, FIXTURE_NAME, FIXTURE_BYTES, 0o600)
        finally:
            os.close(input_fd)
    except OSError as exc:
        _refuse("output preparation failed: " + type(exc).__name__ + ": " + str(exc))
    if fixture_meta["sha256"] != FIXTURE_SHA256:
        _refuse("fixture digest")
    anomalies = []
    date_start = _date("start")
    if date_start["value"] is None:
        anomalies.append("start /bin/date helper failed or unsettled")
    child_argv = [PYTHON_APP[0], "-I", "-B", CHILD[0], "--case-dir", case_dir, "--entry", entry,
                  "--entry-sha256", entry_sha, "--prefix-bytes", str(prefix), "--fault", fault,
                  "--sleep-s", sleep_s, "--", "--job-root", job_dir, "--raw", fixture,
                  "--raw-sha256", BAD_PIN, "--m", "0", "--chunk-lo", "0", "--chunk-hi", "1",
                  "--max-solutions", "0", "--budget-s", budget_s]
    child = {"argv": child_argv, "cwd": case_dir, "env": CHILD_ENV}
    streams, signals = None, []
    t_spawn = time.monotonic()
    try:
        proc = subprocess.Popen(child_argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                close_fds=True, start_new_session=True, cwd=case_dir, env=CHILD_ENV)
    except OSError as exc:
        proc = None
        anomalies.append("child spawn failed: " + type(exc).__name__)
    if proc is not None:
        child["pid"] = proc.pid
        # setsid() before exec by construction (see _helper); observed pgid/sid are recorded and compared.
        group_ok = True
        child["pgid"] = proc.pid
        try:
            child["pgid_observed"] = os.getpgid(proc.pid)
            child["sid_observed"] = os.getsid(proc.pid)
        except OSError as exc:
            child["identity_observation_error"] = type(exc).__name__
        if child.get("pgid_observed", proc.pid) != proc.pid or child.get("sid_observed", proc.pid) != proc.pid:
            group_ok = False
            anomalies.append("child pgid/sid observation differs from its pid")
        try:
            proc.stdin.write(b"GO\n")
            proc.stdin.flush()
            child["go_written"] = True
        except OSError as exc:
            child["go_written"] = False
            child["go_error"] = type(exc).__name__
        try:
            proc.stdin.close()
        except OSError:
            pass
        streams, returncode, signals, more = _supervise(proc, group_ok, t_spawn)
        anomalies.extend(more)
        child["returncode"] = returncode
        child["reaped"] = returncode is not None
        child["wall_s"] = time.monotonic() - t_spawn
        child["group_after_reap"] = (_probe_group(proc.pid) if group_ok and returncode is not None
                                     else "NOT_PROBED")
        if child["group_after_reap"] != "EMPTY":
            anomalies.append("UNSETTLED: child process group not proven empty")
        for pipe in (proc.stdout, proc.stderr):
            try:
                pipe.close()
            except OSError:
                pass
        census, ps_out, lsof_out = _census(proc.pid, proc.pid, case_dir, {os.getpid()})
    else:
        census, ps_out, lsof_out = _census(-1, -1, case_dir, {os.getpid()})
    if census["hits"]:
        anomalies.append("UNSETTLED: census found a process tied to the child or case directory")
    if not census["complete"]:
        anomalies.append("census incomplete")
    pins_after = _pins(pin_items)
    if not all(rec["match"] for rec in pins_after):
        anomalies.append("pin changed during case")
    artifacts = {}
    result = None
    trace = []
    try:
        job_fd = os.open("job", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=case_fd)
        try:
            artifacts["job_entries"] = sorted(os.listdir(job_fd))
            try:
                result, meta = _read_at(job_fd, "result.json", FILE_CAP)
                artifacts["result_json"] = {"path": job_dir + "/result.json", "sha256": _sha(result), "meta": meta}
            except OSError as exc:
                artifacts["result_json"] = {"path": job_dir + "/result.json", "error": type(exc).__name__}
        finally:
            os.close(job_fd)
    except OSError as exc:
        artifacts["job_error"] = type(exc).__name__
    try:
        trace_bytes, meta = _read_at(case_fd, "fault-trace.jsonl", FILE_CAP)
        trace, trace_errors = _trace_records(trace_bytes)
        artifacts["fault_trace"] = {"path": case_dir + "/fault-trace.jsonl", "sha256": _sha(trace_bytes),
                                    "meta": meta, "records": len(trace), "parse_errors": trace_errors}
    except OSError as exc:
        artifacts["fault_trace"] = {"path": case_dir + "/fault-trace.jsonl", "error": type(exc).__name__}
    stream_records = {}
    if streams is not None:
        for name in ("stdout", "stderr"):
            s = streams[name]
            data = bytes(s["data"])
            rec = {"seen": s["seen"], "stored": len(data), "eof": s["eof"], "over_cap": s["over_cap"],
                   "sha256_stored": _sha(data), "file": case_dir + "/" + name + ".bin"}
            try:
                rec["file_meta"] = _xwrite_at(case_fd, name + ".bin", data, 0o600)
            except OSError as exc:
                rec["file_error"] = type(exc).__name__
                anomalies.append("capture file write failed: " + name)
            stream_records[name] = rec
            if not s["eof"] or s["over_cap"]:
                anomalies.append(name + " capture incomplete")
    helper_files = {}
    for name, data in (("census-ps.txt", ps_out), ("census-lsof.txt", lsof_out)):
        if data is None:
            continue
        try:
            helper_files[name] = _xwrite_at(case_fd, name, data[:FILE_CAP], 0o600)
            helper_files[name]["truncated"] = len(data) > FILE_CAP
        except OSError as exc:
            helper_files[name] = {"error": type(exc).__name__}
    stdout_bytes = bytes(streams["stdout"]["data"]) if streams is not None else b""
    relations = _relations(stdout_bytes, result, trace, os.getpid())
    try:
        case_entries = sorted(os.listdir(case_fd))
    except OSError as exc:
        case_entries = ["listing error " + type(exc).__name__]
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    date_end = _date("end")
    if date_end["value"] is None:
        anomalies.append("end /bin/date helper failed or unsettled")
    receipt = {
        "format": FORMAT,
        "case": case,
        "case_spec": {"implementation": impl, "prefix_bytes": prefix, "fault": fault, "sleep_s": sleep_s,
                      "budget_s": budget_s, "role": role, "buffer_size": BUFFER_SIZE},
        "label": ("INSTRUMENTED RawIO fault under real CPython io.BufferedWriter/io.TextIOWrapper; ACTUAL pinned "
                  "entrypoint and algorithm; evidence only"),
        "mapping": MAPPING,
        "driver": {"path": DRIVER_PATH, "observed_sha256": driver_sha, "pid": os.getpid(), "uid": os.getuid(),
                   "euid": os.geteuid(), "python": sys.version, "executable": sys.executable},
        "pins_before": pins_before,
        "pins_after": pins_after,
        "fixture": {"path": fixture, "sha256": FIXTURE_SHA256, "bytes": len(FIXTURE_BYTES), "meta": fixture_meta,
                    "raw_sha256_argument": BAD_PIN},
        "date_start": date_start,
        "date_end": date_end,
        "child": child,
        "signals": signals,
        "streams": stream_records,
        "artifacts": artifacts,
        "helper_files": helper_files,
        "case_entries_before_receipt": case_entries,
        "census": census,
        "relations": relations,
        "rusage_children": {"ru_maxrss": usage.ru_maxrss, "ru_utime": usage.ru_utime, "ru_stime": usage.ru_stime},
        "anomalies": anomalies,
        "wall_s": time.monotonic() - t_start,
        "judgement": "NONE: evidence only; the parent five-part release transaction decides.",
    }
    data = (json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    try:
        receipt_meta = _xwrite_at(case_fd, "receipt.json", data, 0o600)
    except OSError as exc:
        _emit_line({"format": FORMAT, "status": "RECEIPT_WRITE_FAILED", "case": case,
                    "error": type(exc).__name__, "child_returncode": child.get("returncode")}, 1)
    status = "RECORDED" if not anomalies else "RECORDED_WITH_ANOMALY"
    _emit_line({"format": FORMAT, "status": status, "case": case, "receipt": case_dir + "/receipt.json",
                "receipt_sha256": receipt_meta["sha256"], "receipt_ino": receipt_meta["ino"],
                "receipt_nlink": receipt_meta["nlink"], "receipt_bytes": receipt_meta["size"],
                "child_returncode": child.get("returncode"), "anomalies": len(anomalies)},
               0 if not anomalies else 1)


if __name__ == "__main__":
    main()
