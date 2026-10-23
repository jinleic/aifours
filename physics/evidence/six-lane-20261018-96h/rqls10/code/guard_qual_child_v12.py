#!/usr/bin/env python3
"""Rebound qualification child v12 for qual-pkg-v9-v19, source only; no execution authority.

The 22 writer-selected controls retain their workloads, child return codes, thresholds and lifetimes. busy2 alone
spins two processes, requires its own ownership-negative GO and reserves two CPU slots at threshold 1; no busy3
exists. Other forking controls are ownership negatives, not science. All processes inherit the SAME module-entry
monotonic life deadline and the canonical cooperative cutoffs derived from it; work end, join and inner cutoffs are
earlier ABSOLUTE points of that original life, never now+life. An unresolved join fails; it never escalates.

Ordinary stdin is EXACTLY GO\\n then EOF. Only the two mutation negatives accept one additional canonical,
at-most-4096-byte creation JSON line then EOF. That line binds approved preparation and ORIGINAL created
directory/target inodes. Mutation opens no-create/no-follow, verifies original inode/hash/size/nlink before
appending one byte, and reports the exact line digest INCLUDING its newline. External parent approval, not
circular static child/writer/checker hashes, is the trust root.

Private joins have a canonical join_role: main_join (observer main, cutoff cooperative mono_join_deadline,
targets busy_spinner/intermediate) or inner_zombie_join (observer intermediate, cutoff mono_inner_deadline, target
zombie). BEFORE any wait call the observer acquires a full native observer/target/observer bracket and requires its
own fingerprint to equal the expected observer incarnation, the target fingerprint to equal the earlier intended
incarnation and the target ppid to equal the observer. A missing, unavailable or mismatched identity is a recorded
failure with NO wait call and a nonzero exit. Only WNOHANG calls begun before the cutoff are made; the first and
last actual calls keep pid/options inputs, returned pid/status or error and call/return clocks. A destructive wait
result is latched before any later clock read; an exit code exists only from the actual reaping call and a missing
clock stays null and fails. Unresolved or refused joins keep a fresh observation of the unfinished target.

Every report (child-out, IDS line, intermediate report, error line) deep-copies its included observations, joins,
identity polls and transports first and only then takes its own mono_output; no report digests itself. Private
transports keep deadline role, timing, EOF, error, byte count, SHA-256 and the bounded ORIGINAL payload as hex.
Main keeps the original intermediate report bytes with their EOF/read timing and merge offsets, so a checker can
decode and compare the merged report and its exec_status transport. exec_status must be an error-free empty EOF
before the native sleep identity is offered as exec proof. All bytes stay inside child-out.json under its cap.

Incarnation fields and libproc ABI match the frozen supervisor. Identity reads are bracketed; unavailable
identities stay null with actual error evidence. Child reports do not themselves establish supervisor ownership
or release any allocation. Parent must join every relevant incarnation to retained supervisor evidence and
independently prove all known/reported/unproved identities ended. Mandatory owned /bin/date, complete
mixed-UID/known/unproved fail-closed coverage and correction fabe57ab...4155a2 remain. Existing controls do NOT
cover the separately required cap/cleanup/post-ACK matrix.
Usage: guard_qual_child_v12.py SCENARIO LIFE_S. No helper or science is launched here.
"""
import time
START_MONO, START_EPOCH = time.monotonic(), time.time()
import copy
import ctypes
import errno
import hashlib
import json
import math
import mmap
import os
import select
import signal
import stat
import struct
import sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v9-v19"
CHILD = "guard_qual_child_v12"
INTERMEDIATE_KIND = "qualification-intermediate-report-v2"
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
SCENARIOS = {"go_unlisted", "ok", "rc_nonzero", "missing_output", "mutate_pin", "mutate_evidence", "stray_file",
             "deadline", "flood", "busy", "busy2", "rss", "ignore", "identity", "date_fault",
             "helper_overrun", "helper_group", "helper_eof", "ownership_group", "ownership_slow",
             "ownership_fast", "ownership_double", "zombie_hold"}
MUTATIONS = {"mutate_pin", "mutate_evidence"}
NEGATIVE_PROCESS = {"busy2", "ownership_group", "ownership_slow", "ownership_fast", "ownership_double", "zombie_hold"}
SOURCE_PATHS = {"supervisor": LANE + "/code/owned_supervisor_v19.py",
                "child": LANE + "/code/guard_qual_child_v12.py", "writer": LANE + "/code/guard_qual_configs_v12.py",
                "checker": LANE + "/code/guard_qual_check_v11.py"}
POLL_S, SMALL, REPORT_CAP, SZOMB = 0.01, 1 << 20, 32768, 5
IDENTITY_KEYS = ("pid", "uniqueid", "idversion", "euid", "ruid", "ppid", "pgid", "traced")
IDENTITY_FIELDS = frozenset(IDENTITY_KEYS + ("status", "comm"))
# Canonical private joins. Target role -> (join role, expected observer [role, phase], intended target [role, phase]);
# join role -> (observer role, ORIGINAL cooperative cutoff key). No join cutoff is derived from a later clock read.
JOIN_BINDINGS = {"busy_spinner": ("main_join", ("main", "post_go"), ("busy_spinner", "pre_spin")),
                 "intermediate": ("main_join", ("main", "post_go"), ("intermediate", "self_post_setup")),
                 "zombie": ("inner_zombie_join", ("intermediate", "self_post_setup"), ("zombie", "zombie_hold_start"))}
JOIN_ROLES = {"main_join": ("main", "mono_join_deadline"), "inner_zombie_join": ("intermediate", "mono_inner_deadline")}
LP = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
LP.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LP.proc_pidinfo.restype = ctypes.c_int


def check_deadline(deadline, operation):
    if time.monotonic() >= deadline:
        raise OSError("COOPERATIVE_DEADLINE " + operation)


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def finite(value):
    return isinstance(value, float) and math.isfinite(value)


def hex64(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def pairs(items):
    obj = {}
    for key, value in items:
        if key in obj:
            raise ValueError("duplicate JSON key %r" % key)
        obj[key] = value
    return obj


def json_float(text):
    value = float(text)
    if not math.isfinite(value):
        raise ValueError("nonfinite JSON number")
    return value


def json_constant(text):
    raise ValueError("nonfinite JSON constant " + text)


def parse_json(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_float=json_float,
                      parse_constant=json_constant)


def json_line(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def complete_write(fd, data, deadline):
    old = os.get_blocking(fd)
    try:
        os.set_blocking(fd, False)
        view = memoryview(data)
        while view:
            check_deadline(deadline, "before write")
            try:
                n = os.write(fd, view)
            except BlockingIOError:
                select.select([], [fd], [], max(0.0, deadline - time.monotonic()))
                continue
            if n <= 0:
                raise OSError("zero-progress write")
            view = view[n:]
        check_deadline(deadline, "after write")
    finally:
        os.set_blocking(fd, old)


def read_pipe(fd, cap, coop, role):
    """Read through EOF, never accept a prefix merely because a newline arrived. The cutoff is the named ORIGINAL
    cooperative role. Consumed bytes and EOF are latched before any later clock read; the bounded original payload
    is kept as hex beside its byte count and SHA-256, and an unavailable end clock stays null with its error."""
    deadline = coop[role]
    proof = {"mono_start": time.monotonic(), "deadline_mono": deadline, "deadline_role": role, "eof": False,
             "mono_eof": None, "bytes": 0, "sha256": None, "raw_hex": None, "error": None, "mono_end": None}
    raw = bytearray()
    old = os.get_blocking(fd)
    try:
        os.set_blocking(fd, False)
        while True:
            check_deadline(deadline, "pipe read")
            ready, _, _ = select.select([fd], [], [], max(0.0, deadline - time.monotonic()))
            if not ready:
                check_deadline(deadline, "pipe readiness")
                continue
            try:
                part = os.read(fd, min(4096, cap + 1 - len(raw)))
            except BlockingIOError:
                continue
            if not part:
                proof["eof"] = True
                proof["mono_eof"] = time.monotonic()
                check_deadline(deadline, "pipe EOF")
                break
            raw.extend(part)
            if len(raw) > cap:
                raise ValueError("pipe byte cap exceeded")
    except Exception as error:
        proof["error"] = repr(error)
    finally:
        os.set_blocking(fd, old)
    proof.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), raw_hex=raw.hex())
    try:
        proof["mono_end"] = time.monotonic()
    except Exception as error:
        proof["error"] = proof["error"] or repr(error)
    return bytes(raw), proof


def write_pipe(fd, data, coop, role):
    """One bounded private write before the named ORIGINAL cooperative cutoff. returned is true only after every
    byte was written AND the post-write cutoff check passed; payload, timing and the actual error are retained."""
    proof = {"mono_start": time.monotonic(), "deadline_mono": coop[role], "deadline_role": role, "bytes": len(data),
             "sha256": hashlib.sha256(data).hexdigest(), "raw_hex": data.hex(), "returned": False, "error": None,
             "mono_end": None}
    try:
        complete_write(fd, data, coop[role])
        proof["returned"] = True
    except Exception as error:
        proof["error"] = repr(error)
    try:
        proof["mono_end"] = time.monotonic()
    except Exception as error:
        proof["error"] = proof["error"] or repr(error)
    return proof


def wait_go(name, join_deadline):
    """Signature unchanged from child11; main passes cooperative mono_join_deadline, recorded under that role."""
    mutation = name in MUTATIONS
    raw, proof = read_pipe(0, 4099 if mutation else 3, {"mono_join_deadline": join_deadline}, "mono_join_deadline")
    protocol = dict(proof, creation_line_bytes=None, creation_manifest_sha256=None)
    if proof["error"] is not None or not proof["eof"]:
        raise ValueError("GO_READ_REFUSED " + json.dumps(protocol, sort_keys=True))
    if not mutation:
        if raw != b"GO\n":
            raise ValueError("ORDINARY_GO_NOT_EXACT " + json.dumps(protocol, sort_keys=True))
        return protocol, None
    line = raw[3:]
    if raw[:3] != b"GO\n" or not 1 <= len(line) <= 4096 or not line.endswith(b"\n") or line.count(b"\n") != 1:
        raise ValueError("MUTATION_GO_NOT_EXACT " + json.dumps(protocol, sort_keys=True))
    manifest = parse_json(line)
    if json_line(manifest) != line:
        raise ValueError("CREATION_LINE_NOT_CANONICAL")
    protocol.update(creation_line_bytes=len(line), creation_manifest_sha256=hashlib.sha256(line).hexdigest())
    return protocol, manifest


def directory(path, deadline):
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for component in path.lstrip("/").split("/"):
            check_deadline(deadline, "directory traversal")
            if component in ("", ".", ".."):
                raise ValueError("invalid directory component")
            nxt = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = nxt
        check_deadline(deadline, "directory completion")
        return fd
    except BaseException:
        os.close(fd)
        raise


def inode(fd):
    value = os.fstat(fd)
    return [value.st_dev, value.st_ino]


def create_json(outfd, name, obj, deadline):
    data = json_line(obj)
    if len(data) > 1 << 18:
        raise ValueError("child evidence byte cap")
    check_deadline(deadline, "before exclusive child output")
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK, 0o644, dir_fd=outfd)
    try:
        complete_write(fd, data, deadline)
        os.fsync(fd)
        check_deadline(deadline, "after child output fsync")
    finally:
        os.close(fd)
    check_deadline(deadline, "after child output close")


def pidinfo(pid, flavor, size, deadline):
    check_deadline(deadline, "before proc_pidinfo")
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    got = LP.proc_pidinfo(pid, flavor, 1 if flavor in (13, 17) else 0, buf, size)
    error = ctypes.get_errno()
    check_deadline(deadline, "after proc_pidinfo")
    if got != size:
        raise OSError(error or errno.EIO, "PIDINFO %d flavor %d bytes %d" % (pid, flavor, got))
    return buf.raw


def unique(pid, deadline):
    raw = pidinfo(pid, 17, 56, deadline)
    return [struct.unpack_from("=Q", raw, 16)[0], struct.unpack_from("=i", raw, 32)[0]]


def short(pid, deadline):
    raw = pidinfo(pid, 13, 64, deadline)
    p, pp, pg, status = struct.unpack_from("=IIII", raw)
    flags, uid = struct.unpack_from("=II", raw, 32)
    return {"pid": p, "ppid": pp, "pgid": pg, "status": status, "euid": uid,
            "ruid": struct.unpack_from("=I", raw, 44)[0], "traced": bool(flags & 2),
            "comm": raw[16:32].split(b"\0")[0].decode("utf-8", "replace")}


def fingerprint(identity):
    return tuple(identity[key] for key in IDENTITY_KEYS)


def identity_valid(value):
    """Exact acquired identity shape (fingerprint keys plus status/comm) with JSON-exact scalar types."""
    return isinstance(value, dict) and set(value) == IDENTITY_FIELDS and isinstance(value["traced"], bool) and \
        isinstance(value["comm"], str) and all(integer(value[key]) for key in IDENTITY_FIELDS - {"traced", "comm"})


def observe(pid, role, phase, deadline):
    """Keep partial raw brackets even when identification fails; never fill missing identity fields."""
    record = {"role": role, "phase": phase, "observer": os.getpid(), "pid": pid,
              "mono_start": time.monotonic(), "observed_mono": None, "identity": None, "error": None, "bracket": {}}
    bracket = record["bracket"]
    try:
        bracket["unique_before"] = unique(pid, deadline)
        bracket["short_before"] = short(pid, deadline)
        bracket["unique_middle"] = unique(pid, deadline)
        bracket["short_after"] = short(pid, deadline)
        bracket["unique_after"] = unique(pid, deadline)
        if not bracket["unique_before"] == bracket["unique_middle"] == bracket["unique_after"]:
            raise ValueError("IDENTITY_CHANGED %d" % pid)
        a, b = dict(bracket["short_before"]), dict(bracket["short_after"])
        for item in (a, b):
            item.update(uniqueid=bracket["unique_before"][0], idversion=bracket["unique_before"][1])
        if a["pid"] != pid or b["pid"] != pid or fingerprint(a) != fingerprint(b):
            raise ValueError("IDENTITY_METADATA_CHANGED %d" % pid)
        record["identity"] = b
    except Exception as error:
        record["error"] = repr(error)
    record["observed_mono"] = time.monotonic()
    return record


def edge_observation(pid, role, phase, deadline):
    parent_before = observe(os.getpid(), "main" if role == "descendant" else "intermediate", phase + "_parent_before", deadline)
    child = observe(pid, role, phase, deadline)
    parent_after = observe(os.getpid(), parent_before["role"], phase + "_parent_after", deadline)
    proof = {"phase": phase, "parent_before": parent_before, "child": child, "parent_after": parent_after,
             "current_parent_verified": False, "same_group_verified": False, "error": None}
    a, b, c = parent_before["identity"], child["identity"], parent_after["identity"]
    if a is None or b is None or c is None:
        proof["error"] = "CURRENT_PARENT_IDENTITY_UNAVAILABLE"
    elif fingerprint(a) != fingerprint(c) or b["ppid"] != a["pid"]:
        proof["error"] = "CURRENT_PARENT_EDGE_CHANGED"
    else:
        proof.update(current_parent_verified=True, same_group_verified=b["pgid"] == a["pgid"])
    return child, proof


def sleep_to(deadline):
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        time.sleep(min(0.05, remaining))


def spin_to(deadline):
    n = 0
    while time.monotonic() < deadline:
        n += 1


def join_precheck(pid, role, join_role, observer_role, deadline, expected_observer, intended):
    """Actual full native observer/target/observer bracket acquired BEFORE any wait call; nothing missing is filled."""
    phase = join_role + "_precheck"
    proof = {"phase": phase, "mono_start": time.monotonic(), "parent_before": None, "target": None,
             "parent_after": None, "error": None, "mono_end": None}
    proof["parent_before"] = observe(os.getpid(), observer_role, phase + "_parent_before", deadline)
    proof["target"] = observe(pid, role, phase, deadline)
    proof["parent_after"] = observe(os.getpid(), observer_role, phase + "_parent_after", deadline)
    a, b, c = proof["parent_before"]["identity"], proof["target"]["identity"], proof["parent_after"]["identity"]
    if not identity_valid(expected_observer) or not identity_valid(intended):
        proof["error"] = "JOIN_EXPECTED_OBSERVER_OR_INTENDED_TARGET_MISSING"
    elif a is None or b is None or c is None:
        proof["error"] = "JOIN_PRECHECK_IDENTITY_UNAVAILABLE"
    elif a["pid"] != os.getpid() or fingerprint(a) != fingerprint(expected_observer) or \
            fingerprint(c) != fingerprint(expected_observer):
        proof["error"] = "JOIN_OBSERVER_NOT_EXPECTED_INCARNATION"
    elif intended["pid"] != pid or b["pid"] != pid or b["ppid"] != a["pid"] or fingerprint(b) != fingerprint(intended):
        proof["error"] = "JOIN_TARGET_NOT_INTENDED_CHILD_INCARNATION"
    proof["mono_end"] = time.monotonic()
    return proof


def join_child(pid, role, coop, expected_observer, intended):
    """WNOHANG-only join bound to its canonical role, actual observer, intended incarnation and ORIGINAL cutoff.
    Once a wait call is made nothing escapes: a destructive result is latched before later clocks/evidence work."""
    join_role, observer_source, intended_source = JOIN_BINDINGS[role]
    observer_role, deadline_role = JOIN_ROLES[join_role]
    deadline, life_deadline = coop[deadline_role], coop["mono_life_deadline"]
    report = {"role": role, "join_role": join_role, "observer_role": observer_role, "observer": os.getpid(),
              "pid": pid, "deadline_role": deadline_role, "deadline_mono": deadline,
              "mono_life_deadline": life_deadline, "expected_observer_source": list(observer_source),
              "expected_observer_identity": expected_observer, "intended_source": list(intended_source),
              "intended_identity": intended, "mono_start": time.monotonic(), "mono_end": None, "precheck": None,
              "precheck_ok": False, "wait_options": ["WNOHANG"], "wait_options_value": os.WNOHANG, "calls": 0,
              "interruptions": 0, "first_call": None, "last_call": None, "resolved": False, "wait_status": None,
              "exit_code": None, "mono_reaped": None, "error": None, "unresolved_observation": None,
              "unresolved_observation_error": None}
    try:
        report["precheck"] = join_precheck(pid, role, join_role, observer_role, deadline, expected_observer, intended)
        report["precheck_ok"] = report["precheck"]["error"] is None
        if not report["precheck_ok"]:
            report["error"] = report["precheck"]["error"]  # Never wait on an unbound target.
        while report["precheck_ok"] and not report["resolved"] and report["error"] is None:
            mono_call = time.monotonic()
            if mono_call >= deadline:
                break
            report["calls"] += 1
            call = {"index": report["calls"], "pid": pid, "options": os.WNOHANG, "mono_call": mono_call,
                    "mono_return": None, "returned_pid": None, "returned_status": None, "error": None}
            if report["first_call"] is None:
                report["first_call"] = call
            report["last_call"] = call
            returned = None
            try:
                returned = os.waitpid(pid, os.WNOHANG)
            except InterruptedError as error:
                call["error"] = repr(error)
                report["interruptions"] += 1
            except Exception as error:
                call["error"] = repr(error)
                report["error"] = "WAIT_CALL_ERROR"
            if returned is not None:
                # Latch the destructive native result BEFORE any clock read that could fail.
                call["returned_pid"], call["returned_status"] = returned
                if returned[0] == pid:
                    report["resolved"], report["wait_status"] = True, returned[1]
                    try:
                        report["exit_code"] = os.waitstatus_to_exitcode(returned[1])
                    except ValueError:
                        report["error"] = "WAIT_STATUS_NOT_EXIT_OR_SIGNAL"
                elif returned[0] != 0:
                    report["error"] = "WAIT_RETURNED_UNEXPECTED_PID"
            call["mono_return"] = time.monotonic()
            if report["resolved"]:
                report["mono_reaped"] = call["mono_return"]
                if report["mono_reaped"] >= deadline and report["error"] is None:
                    report["error"] = "WAIT_COMPLETED_AFTER_ABSOLUTE_DEADLINE"
            elif returned is not None and returned[0] == 0:
                time.sleep(min(POLL_S, max(0.0, deadline - time.monotonic())))
    except Exception as error:
        report["error"] = report["error"] or "JOIN_EVIDENCE_ERROR " + repr(error)
    if not report["resolved"]:
        if report["error"] is None:
            report["error"] = "WAIT_UNRESOLVED_AT_ABSOLUTE_DEADLINE"
        try:
            report["unresolved_observation"] = observe(pid, role, "unresolved_join", life_deadline)
        except Exception as error:
            report["unresolved_observation_error"] = repr(error)
    try:
        report["mono_end"] = time.monotonic()
    except Exception as error:
        report["error"] = report["error"] or "JOIN_END_CLOCK_UNAVAILABLE " + repr(error)
    return report


def join_ok(report):
    return report["precheck_ok"] and report["resolved"] and report["error"] is None and report["exit_code"] == 0


def fork_body(body, deadline):
    pid = os.fork()
    if pid == 0:
        try:
            body()
        except BaseException as error:
            try:
                complete_write(2, ("DESCENDANT_ERROR %r\n" % error).encode(), deadline)
            except BaseException:
                pass
            os._exit(1)
        os._exit(0)
    return pid


def identity_wait(pid, role, phase, coop, deadline_role, predicate):
    deadline = coop[deadline_role]
    proof = {"role": role, "pid": pid, "phase": phase, "observer": os.getpid(), "deadline_mono": deadline,
             "deadline_role": deadline_role, "mono_start": time.monotonic(), "mono_end": None, "attempts": 0,
             "first_observation": None, "last_observation": None, "errors": [], "matched": False}
    while time.monotonic() < deadline:
        item = observe(pid, role, phase, deadline)
        proof["attempts"] += 1
        if proof["first_observation"] is None:
            proof["first_observation"] = item
        proof["last_observation"] = item
        if item["error"] is not None:
            proof["errors"].append(item)
            if len(proof["errors"]) >= 8:
                break  # Fail on a bounded evidence cap, never silently discard failed reads.
        elif predicate(item["identity"]):
            proof["matched"] = True
            break
        time.sleep(min(POLL_S, max(0.0, deadline - time.monotonic())))
    proof["mono_end"] = time.monotonic()
    return proof


def stat_signature(value):
    return (value.st_dev, value.st_ino, value.st_size, value.st_nlink, value.st_mtime_ns, value.st_ctime_ns)


def snapshot_fd(fd, path, cap, deadline):
    check_deadline(deadline, "before regular snapshot")
    before = os.fstat(fd)
    if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or not 0 <= before.st_size <= cap:
        raise ValueError("not a bounded single-link regular file")
    raw = bytearray()
    while len(raw) < before.st_size:
        check_deadline(deadline, "regular snapshot read")
        part = os.pread(fd, min(65536, before.st_size - len(raw)), len(raw))
        if not part:
            raise OSError("short regular snapshot")
        raw.extend(part)
    if os.pread(fd, 1, before.st_size) or stat_signature(os.fstat(fd)) != stat_signature(before):
        raise ValueError("regular file changed during snapshot")
    check_deadline(deadline, "after regular snapshot")
    return {"path": path, "inode": [before.st_dev, before.st_ino], "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "nlink": before.st_nlink}, bytes(raw)


def read_regular_at(rootfd, name, path, deadline):
    fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=rootfd)
    try:
        facts, raw = snapshot_fd(fd, path, SMALL, deadline)
        named = os.stat(name, dir_fd=rootfd, follow_symlinks=False)
        if [named.st_dev, named.st_ino] != facts["inode"] or not stat.S_ISREG(named.st_mode) or named.st_nlink != 1:
            raise ValueError("regular pathname replaced during read")
        return facts, raw
    finally:
        os.close(fd)


def anchor_schema(value, path):
    return (isinstance(value, dict) and set(value) == {"path", "inode"} and value["path"] == path and
            isinstance(value["inode"], list) and len(value["inode"]) == 2 and
            all(integer(v) and v >= 0 for v in value["inode"]))


def target_schema(value, path):
    return (isinstance(value, dict) and set(value) == {"path", "inode", "sha256", "bytes", "nlink"} and
            anchor_schema({"path": value["path"], "inode": value["inode"]}, path) and hex64(value["sha256"]) and
            integer(value["bytes"]) and 0 < value["bytes"] <= SMALL and integer(value["nlink"]) and value["nlink"] == 1)


def verify_anchors(run, rfd, ofd, expected_run, expected_out, deadline):
    fresh = directory(run, deadline)
    fresh_out = None
    try:
        fresh_out = os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fresh)
        actual_run, actual_out = {"path": run, "inode": inode(rfd)}, {"path": run + "/out", "inode": inode(ofd)}
        if not typed_equal(actual_run, expected_run) or not typed_equal(actual_out, expected_out) or \
                not typed_equal(inode(fresh), expected_run["inode"]) or \
                not typed_equal(inode(fresh_out), expected_out["inode"]) or actual_run["inode"][0] != actual_out["inode"][0]:
            raise ValueError("ORIGINAL_APPROVED_DIRECTORY_ANCHOR_CHANGED")
        check_deadline(deadline, "anchor verification")
        return actual_run, actual_out
    finally:
        if fresh_out is not None:
            os.close(fresh_out)
        os.close(fresh)


def mutate_original(name, run, rfd, ofd, manifest, protocol, deadline):
    keys = {"kind", "scenario", "preparation_sha256", "run", "output_root", "target"}
    target_path = run + ("/pinned-scratch.txt" if name == "mutate_pin" else "/out/launch.json")
    if not isinstance(manifest, dict) or set(manifest) != keys or manifest["kind"] != "qualification-creation-manifest-v1" or \
            manifest["scenario"] != name or not hex64(manifest["preparation_sha256"]) or \
            not anchor_schema(manifest["run"], run) or not anchor_schema(manifest["output_root"], run + "/out") or \
            not target_schema(manifest["target"], target_path):
        raise ValueError("CREATION_MANIFEST_SCHEMA_OR_FIXED_PATH")
    actual_run, actual_out = verify_anchors(run, rfd, ofd, manifest["run"], manifest["output_root"], deadline)
    prep_facts, prep_raw = read_regular_at(rfd, "preparation.json", run + "/preparation.json", deadline)
    if prep_facts["sha256"] != manifest["preparation_sha256"]:
        raise ValueError("APPROVED_PREPARATION_SHA256_MISMATCH")
    prep = parse_json(prep_raw)
    prep_keys = {"kind", "scenario", "run", "output_root", "fixture", "source_pins", "python", "allocation", "negative_control"}
    if not isinstance(prep, dict) or set(prep) != prep_keys or prep["kind"] != "qualification-creation-preparation-v1" or \
            prep["scenario"] != name or prep["negative_control"] is not True or not typed_equal(prep["run"], manifest["run"]) or \
            not typed_equal(prep["output_root"], manifest["output_root"]):
        raise ValueError("APPROVED_PREPARATION_SEMANTICS")
    pins = prep["source_pins"]
    if not isinstance(pins, dict) or set(pins) != {"supervisor", "child", "writer", "checker"} or any(
            not isinstance(v, dict) or set(v) != {"path", "sha256"} or not isinstance(v["path"], str) or
            not v["path"].startswith("/") or os.path.normpath(v["path"]) != v["path"] or not hex64(v["sha256"])
            for v in pins.values()) or any(pins[k]["path"] != path for k, path in SOURCE_PATHS.items()):
        raise ValueError("APPROVED_PREPARATION_SOURCE_PIN_METADATA")
    python, allocation = prep["python"], prep["allocation"]
    if not isinstance(python, dict) or set(python) != {"path", "sha256"} or not isinstance(python["path"], str) or \
            not python["path"].endswith("/Resources/Python.app/Contents/MacOS/Python") or \
            os.path.realpath(python["path"]) != python["path"] or python["path"] != os.path.realpath(sys.executable) or \
            not hex64(python["sha256"]):
        raise ValueError("APPROVED_PREPARATION_ACTUAL_PYTHON_APP")
    allocation_keys = {"bytes", "cpu_slots", "outstanding_reservations_bytes", "lane_outstanding_reservations_bytes"}
    if not isinstance(allocation, dict) or set(allocation) != allocation_keys or any(
            not integer(v) or not 0 <= v <= 1 << 60 for v in allocation.values()) or \
            allocation["bytes"] != 20971520 or allocation["cpu_slots"] != 1:
        raise ValueError("APPROVED_PREPARATION_ALLOCATION")
    target = manifest["target"]
    if name == "mutate_pin":
        if not typed_equal(prep["fixture"], target) or target["sha256"] != hashlib.sha256(FIXTURE).hexdigest() or target["bytes"] != len(FIXTURE):
            raise ValueError("ORIGINAL_CREATED_PIN_NOT_APPROVED_FIXTURE")
        rootfd, basename = rfd, "pinned-scratch.txt"
    else:
        if prep["fixture"] is not None:
            raise ValueError("LAUNCH_MUTATION_HAS_PIN_FIXTURE")
        rootfd, basename = ofd, "launch.json"
    # No O_CREAT, no pathname supplied by argv, no link/rename operations.
    fd = os.open(basename, os.O_RDWR | os.O_APPEND | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=rootfd)
    try:
        original, original_raw = snapshot_fd(fd, target_path, SMALL, deadline)
        if not typed_equal(original, target) or (name == "mutate_pin" and original_raw != FIXTURE):
            raise ValueError("ORIGINAL_CREATION_INODE_HASH_SIZE_LINK_MISMATCH")
        verify_anchors(run, rfd, ofd, manifest["run"], manifest["output_root"], deadline)
        named = os.stat(basename, dir_fd=rootfd, follow_symlinks=False)
        named_before = [named.st_dev, named.st_ino]
        if named_before != original["inode"] or not stat.S_ISREG(named.st_mode) or named.st_nlink != 1 or named.st_size != original["bytes"]:
            raise ValueError("ORIGINAL_TARGET_PATH_CHANGED_BEFORE_APPEND")
        # Re-snapshot on the SAME descriptor after anchor/name I/O and before the write.
        checked, checked_raw = snapshot_fd(fd, target_path, SMALL, deadline)
        if not typed_equal(checked, original) or checked_raw != original_raw:
            raise ValueError("ORIGINAL_TARGET_CHANGED_BEFORE_APPEND")
        mono_verified = time.monotonic()
        complete_write(fd, b"x", deadline)
        mono_append = time.monotonic()
        os.fsync(fd)
        check_deadline(deadline, "mutation fsync")
        mono_fsync = time.monotonic()
        after, after_raw = snapshot_fd(fd, target_path, SMALL + 1, deadline)
        named = os.stat(basename, dir_fd=rootfd, follow_symlinks=False)
        named_after = [named.st_dev, named.st_ino]
        if after["inode"] != original["inode"] or after["bytes"] != original["bytes"] + 1 or after_raw != original_raw + b"x" or \
                named_after != original["inode"] or named.st_nlink != 1 or not stat.S_ISREG(named.st_mode):
            raise ValueError("MUTATION_POST_APPEND_FACTS_CHANGED")
        return {"manifest": manifest, "manifest_sha256": protocol["creation_manifest_sha256"],
                "manifest_line_bytes": protocol["creation_line_bytes"], "preparation_sha256": prep_facts["sha256"],
                "preparation_facts": prep_facts, "run": actual_run, "output_root": actual_out,
                "original": original, "after": after, "name_inode_before": named_before, "name_inode_after": named_after,
                "append_bytes": 1, "mono_verified": mono_verified, "mono_append": mono_append,
                "mono_fsync_completed": mono_fsync, "mono_after_verified": time.monotonic()}
    finally:
        os.close(fd)


def task_observation(pid, deadline):
    before = observe(pid, "main", "rss_measurement_before", deadline)
    record = {"pid": pid, "identity_before": before, "identity_after": None, "rss_bytes": None,
              "mono_start": time.monotonic(), "mono_end": None, "error": None}
    try:
        if before["identity"] is None:
            raise ValueError("RSS_IDENTITY_BEFORE_UNAVAILABLE")
        raw = pidinfo(pid, 4, 96, deadline)
        rss = struct.unpack_from("=Q", raw, 8)[0]
        after = observe(pid, "main", "rss_measurement_after", deadline)
        record["identity_after"] = after
        if after["identity"] is None or fingerprint(before["identity"]) != fingerprint(after["identity"]):
            raise ValueError("RSS_IDENTITY_BRACKET_CHANGED")
        record["rss_bytes"] = rss
    except Exception as error:
        record["error"] = repr(error)
    record["mono_end"] = time.monotonic()
    return record


def intermediate_report(name, reportfd, coop, reserve):
    deadline, join_deadline, inner_deadline = coop["mono_life_deadline"], coop["mono_join_deadline"], coop["mono_inner_deadline"]
    report = {"kind": INTERMEDIATE_KIND, "scenario": name, "intermediate": os.getpid(), "mono_module_entry": START_MONO,
              "mono_life_deadline": deadline, "cooperative": coop, "grandchild": None, "descendants": [], "joins": [],
              "identity_waits": [], "ownership_edges": [], "transports": {}, "evidence_failures": [], "error": None}
    try:
        if name == "ownership_double":
            os.setsid()
        own = observe(os.getpid(), "intermediate", "self_post_setup", inner_deadline)
        report["descendants"].append(own)
        if own["identity"] is None:
            raise ValueError("INTERMEDIATE_IDENTITY_UNAVAILABLE")
        if name == "zombie_hold":
            def zombie():
                os.close(reportfd)
            kid = fork_body(zombie, deadline)
            report["grandchild"] = kid
            held = identity_wait(kid, "zombie", "zombie_hold_start", coop, "mono_inner_deadline",
                                 lambda p: p["status"] == SZOMB)
            report["identity_waits"].append(held)
            if held["last_observation"] is not None:
                report["descendants"].append(held["last_observation"])
            if not held["matched"] or held["errors"]:
                report["evidence_failures"].append("ZOMBIE_HELD_IDENTITY_NOT_PROVED")
            hold_start = time.monotonic()
            hold_until = min(hold_start + 3.0, inner_deadline - reserve)
            sleep_to(hold_until)
            end = observe(kid, "zombie", "zombie_hold_end", inner_deadline)
            report["descendants"].append(end)
            first = held["last_observation"]["identity"] if held["last_observation"] is not None else None
            if first is None or end["identity"] is None or end["identity"]["status"] != SZOMB or fingerprint(first) != fingerprint(end["identity"]):
                report["evidence_failures"].append("ZOMBIE_HOLD_END_IDENTITY_NOT_PROVED")
            report["zombie_hold"] = {"mono_start": hold_start, "mono_hold_until": hold_until, "mono_end": time.monotonic()}
            # Inner zombie join: observer is this intermediate incarnation, target the held zombie incarnation.
            joined = join_child(kid, "zombie", coop, own["identity"], first)
            report["joins"].append(joined)
            if not join_ok(joined):
                report["evidence_failures"].append("ZOMBIE_JOIN_UNRESOLVED_OR_NONZERO")
        else:
            exec_read, exec_write = os.pipe()
            gate_read, gate_write = os.pipe()
            os.set_inheritable(exec_write, False)
            def exec_descendant():
                os.close(exec_read)
                os.close(gate_write)
                os.close(reportfd)
                try:
                    gate, gate_proof = read_pipe(gate_read, 1, coop, "mono_inner_deadline")
                    os.close(gate_read)
                    if gate != b"S" or not gate_proof["eof"] or gate_proof["error"] is not None:
                        raise ValueError("EXEC_START_GATE_REFUSED")
                    os.chdir("/")
                    devnull = os.open("/dev/null", os.O_RDWR)
                    for standard in (0, 1, 2):
                        os.dup2(devnull, standard)
                    os.closerange(3, exec_write)
                    os.closerange(exec_write + 1, 65536)
                    check_deadline(deadline, "before fixed sleep exec")
                    remaining = max(0.0, deadline - time.monotonic())
                    os.execv("/bin/sleep", ["sleep", "%.6f" % remaining])
                    raise RuntimeError("exec unexpectedly returned")
                except BaseException as error:
                    try:
                        complete_write(exec_write, ("EXEC_ERROR %r\n" % error).encode()[:2048], deadline)
                    except BaseException:
                        pass
                    raise
            kid = fork_body(exec_descendant, deadline)
            report["grandchild"] = kid
            os.close(exec_write)
            os.close(gate_read)
            try:
                pre, edge = edge_observation(kid, "exec_descendant", "pre_exec", inner_deadline)
                report["descendants"].append(pre)
                report["ownership_edges"].append(edge)
                if pre["identity"] is None or not edge["current_parent_verified"]:
                    report["evidence_failures"].append("PRE_EXEC_CURRENT_PARENT_NOT_PROVED")
                gate = write_pipe(gate_write, b"S", coop, "mono_inner_deadline")
                report["transports"]["exec_start_gate"] = gate
            finally:
                os.close(gate_write)
            if gate["error"] is not None:
                report["evidence_failures"].append("EXEC_START_GATE_NOT_RETURNED")
                raise ValueError("EXEC_START_GATE_WRITE_FAILED")
            try:
                exec_raw, exec_proof = read_pipe(exec_read, 2048, coop, "mono_inner_deadline")
                report["transports"]["exec_status"] = exec_proof
            finally:
                os.close(exec_read)
            # Exec is proved only by an error-free, empty, EOF-terminated close-on-exec status pipe. Any byte, read
            # error or missing EOF is recorded and stops before a native sleep identity can be offered as exec proof.
            if exec_raw or not exec_proof["eof"] or exec_proof["error"] is not None:
                report["evidence_failures"].append("EXEC_STATUS_NOT_ERROR_FREE_EMPTY_EOF")
                raise ValueError("FIXED_SLEEP_EXEC_NOT_PROVED")
            post = identity_wait(kid, "exec_descendant", "post_exec_pre_reparent", coop, "mono_inner_deadline",
                                 lambda p: p["comm"] == "sleep" and p["ppid"] == os.getpid() and p["status"] != SZOMB)
            report["identity_waits"].append(post)
            if post["last_observation"] is not None:
                report["descendants"].append(post["last_observation"])
            if not post["matched"] or post["errors"]:
                report["evidence_failures"].append("POST_EXEC_INCARNATION_NOT_PROVED")
            if post["matched"]:
                current, edge = edge_observation(kid, "exec_descendant", "post_exec_current_parent", inner_deadline)
                report["descendants"].append(current)
                report["ownership_edges"].append(edge)
                if current["identity"] is None or not edge["current_parent_verified"]:
                    report["evidence_failures"].append("POST_EXEC_CURRENT_PARENT_NOT_PROVED")
    except BaseException as error:
        report["error"] = repr(error)
        report["evidence_failures"].append("INTERMEDIATE_BODY_ERROR")
    try:
        # Copy every included observation/join/poll/transport FIRST; only then take this report's own timestamp.
        snapshot = copy.deepcopy(report)
        snapshot["mono_output"] = time.monotonic()
        data = json_line(snapshot)
        if len(data) > REPORT_CAP:
            raise ValueError("intermediate report cap")
        complete_write(reportfd, data, join_deadline)
    finally:
        os.close(reportfd)
    if report["evidence_failures"]:
        raise ValueError("INTERMEDIATE_REPORTED_FAILURE " + ",".join(report["evidence_failures"]))


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in SCENARIOS:
        return 2
    name, life = sys.argv[1], float(sys.argv[2])
    if not math.isfinite(life) or not 1 <= life <= 120:
        return 2
    deadline = START_MONO + life
    # These are earlier ABSOLUTE cutoffs inside the original life, never now+life; forks inherit them unchanged.
    reserve = min(0.25, life / 8.0)
    coop = {"mono_life_deadline": deadline, "mono_work_end": deadline - 2 * reserve,
            "mono_join_deadline": deadline - reserve, "mono_inner_deadline": deadline - 3 * reserve,
            "poll_interval_s": POLL_S, "deadline_extended": False}
    work_end, join_deadline = coop["mono_work_end"], coop["mono_join_deadline"]
    try:
        protocol, manifest = wait_go(name, join_deadline)
    except Exception as error:
        complete_write(2, ("QUAL_CHILD_PROTOCOL_REFUSED %r\n" % error).encode(), deadline)
        return 6
    run = QROOT + "/" + name
    rfd = directory(run, deadline)
    ofd = None
    state = {"descendants": [], "joins": [], "identity_waits": [], "ownership_edges": [],
             "transports": {}, "evidence_failures": []}
    result_attempted = False
    main_observation = observe(os.getpid(), "main", "post_go", deadline)
    if main_observation["identity"] is None:
        state["evidence_failures"].append("MAIN_IDENTITY_UNAVAILABLE")
    def report_object(extra):
        # Copy every included observation/join/poll/transport FIRST; only then take this report's own timestamp.
        obj = copy.deepcopy({"child": CHILD, "scenario": name, "pid": os.getpid(), "pgid": os.getpgrp(),
                             "ppid": os.getppid(), "negative_control": name not in ("ok", "rc_nonzero"),
                             "mono_module_entry": START_MONO, "epoch_module_entry": START_EPOCH,
                             "mono_life_deadline": deadline, "stdin_protocol": protocol,
                             "main_identity": main_observation["identity"],
                             "main_identity_observed_mono": main_observation["observed_mono"],
                             "main_identity_observation": main_observation, "cooperative": coop, **state, **extra})
        obj["mono_output"] = time.monotonic()
        return obj
    def result(extra=None):
        nonlocal result_attempted
        result_attempted = True
        final = observe(os.getpid(), "main", "output", deadline)
        if final["identity"] is None:
            state["evidence_failures"].append("MAIN_OUTPUT_IDENTITY_UNAVAILABLE")
        create_json(ofd, "child-out.json", report_object(dict(extra or {}, main_identity_at_output=final)), deadline)
    def status(normal=0):
        return 1 if state["evidence_failures"] else normal
    try:
        ofd = os.open("out", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=rfd)
        if name in ("ok", "go_unlisted", "rc_nonzero", "date_fault", "helper_overrun", "helper_group", "helper_eof"):
            result()
            if name == "ok":
                complete_write(1, b"line 1\nline 2\nline 3\n", deadline)
            return status(3 if name == "rc_nonzero" else 0)
        if name == "missing_output":
            complete_write(1, b"no output written\n", deadline)
            return status()
        if name in MUTATIONS:
            creation = mutate_original(name, run, rfd, ofd, manifest, protocol, deadline)
            result({"creation": creation, "target_inode": creation["original"]["inode"],
                    "size_before": creation["original"]["bytes"]})
            return status()
        if name == "stray_file":
            result()
            fd = os.open("stray.txt", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK, 0o644, dir_fd=ofd)
            try:
                complete_write(fd, b"undeclared file\n", deadline)
                os.fsync(fd)
                check_deadline(deadline, "stray fsync")
            finally:
                os.close(fd)
            return status()
        if name == "flood":
            os.set_blocking(1, False)
            line = b"x" * 65535 + b"\n"
            view = memoryview(line)
            while time.monotonic() < work_end:
                try:
                    n = os.write(1, view)
                    if n <= 0:
                        raise OSError("zero-progress flood write")
                    view = view[n:] if n < len(view) else memoryview(line)
                except BlockingIOError:
                    time.sleep(min(0.005, max(0.0, work_end - time.monotonic())))
            return status()
        if name == "busy":
            ids = report_object({"busy_pid": os.getpid(), "mono_before_work": time.monotonic()})
            complete_write(1, b"IDS " + json_line(ids), deadline)
            spin_to(work_end)
            return status()
        if name == "rss":
            before = task_observation(os.getpid(), deadline)
            if before["error"] is not None:
                raise ValueError("RSS_BASELINE_NOT_PROVED " + repr(before))
            # Briefly defer the one ordinary TERM only until the bounded allocation/touch/
            # measurement/IDS write completes; then restore its DEFAULT disposition/mask.
            # This prevents an RSS trip racing away its own PID-specific evidence.
            old_mask = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGTERM})
            try:
                mono_allocate = time.monotonic()
                block = bytearray(320 * 1024 * 1024)
                touch_writes = 0
                for index in range(0, len(block), 4096):
                    block[index] = 1
                    touch_writes += 1
                    if touch_writes % 1024 == 0:
                        check_deadline(work_end, "RSS touch")
                after = task_observation(os.getpid(), deadline)
                if after["error"] is not None:
                    raise ValueError("RSS_AFTER_TOUCH_NOT_PROVED " + repr(after))
                ids = report_object({"rss_pid": os.getpid(), "allocated": len(block), "touched_bytes": len(block),
                                     "touch_stride": 4096, "touch_writes": touch_writes,
                                     "touch_write_bytes": touch_writes, "page_size": mmap.PAGESIZE,
                                     "rss_before_bytes": before["rss_bytes"], "rss_after_bytes": after["rss_bytes"],
                                     "rss_delta_bytes": after["rss_bytes"] - before["rss_bytes"],
                                     "rss_before": before, "rss_after": after,
                                     "mono_before_allocation": mono_allocate, "mono_after_touch": time.monotonic(),
                                     "term_masked_for_evidence": True})
                complete_write(1, b"IDS " + json_line(ids), deadline)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)
            sleep_to(work_end)
            return status()
        if name == "busy2":
            gate_read, gate_write = os.pipe()
            def spinner():
                os.close(gate_write)
                try:
                    raw, proof = read_pipe(gate_read, 1, coop, "mono_work_end")
                finally:
                    os.close(gate_read)
                if raw != b"S" or not proof["eof"] or proof["error"] is not None:
                    raise ValueError("BUSY_START_GATE_REFUSED")
                spin_to(work_end)
            kid = fork_body(spinner, deadline)
            os.close(gate_read)
            observed = observe(kid, "busy_spinner", "pre_spin", join_deadline)
            state["descendants"].append(observed)
            if observed["identity"] is None:
                state["evidence_failures"].append("BUSY_SPINNER_IDENTITY_UNAVAILABLE")
            ids = report_object({"busy_pids": [os.getpid(), kid], "mono_before_work": time.monotonic(),
                                 "mono_work_end": work_end, "busy_gate": "not_released_before_identity_and_IDS"})
            try:
                complete_write(1, b"IDS " + json_line(ids), deadline)
                if not state["evidence_failures"]:
                    gate = write_pipe(gate_write, b"S", coop, "mono_join_deadline")
                    state["transports"]["busy_start_gate"] = gate
                    if gate["error"] is not None:
                        raise ValueError("BUSY_START_GATE_WRITE_FAILED")
            finally:
                os.close(gate_write)
            if not state["evidence_failures"]:
                spin_to(work_end)
            joined = join_child(kid, "busy_spinner", coop, main_observation["identity"], observed["identity"])
            state["joins"].append(joined)
            if not join_ok(joined):
                state["evidence_failures"].append("BUSY_JOIN_UNRESOLVED_OR_NONZERO")
            result({"grandchild": kid, "busy_pids": [os.getpid(), kid]})
            return status()
        if name in ("ownership_group", "ownership_slow", "ownership_fast"):
            ready_read, ready_write = os.pipe()
            def descendant():
                os.close(ready_read)
                if name != "ownership_group":
                    os.setsid()
                try:
                    complete_write(ready_write, b"R", join_deadline)
                finally:
                    os.close(ready_write)
                sleep_to(deadline)
            kid = fork_body(descendant, deadline)
            os.close(ready_write)
            try:
                raw, proof = read_pipe(ready_read, 1, coop, "mono_join_deadline")
            finally:
                os.close(ready_read)
            state["transports"]["descendant_ready"] = proof
            if raw != b"R" or not proof["eof"] or proof["error"] is not None:
                state["evidence_failures"].append("DESCENDANT_READY_NOT_PROVED")
            item, edge = edge_observation(kid, "descendant", "post_setup", join_deadline)
            state["descendants"].append(item)
            state["ownership_edges"].append(edge)
            if item["identity"] is None or not edge["current_parent_verified"] or \
                    (name == "ownership_group" and not edge["same_group_verified"]) or \
                    (name != "ownership_group" and item["identity"]["pgid"] != kid):
                state["evidence_failures"].append("DESCENDANT_SETUP_EDGE_NOT_PROVED")
            hold = {"mono_start": time.monotonic(), "mono_end": None}
            if name != "ownership_fast":
                sleep_to(min(time.monotonic() + 3.0, work_end))
                item, edge = edge_observation(kid, "descendant", "hold_end", join_deadline)
                state["descendants"].append(item)
                state["ownership_edges"].append(edge)
                if item["identity"] is None or not edge["current_parent_verified"] or \
                        (name == "ownership_group" and not edge["same_group_verified"]):
                    state["evidence_failures"].append("DESCENDANT_HELD_EDGE_NOT_PROVED")
            hold["mono_end"] = time.monotonic()
            result({"grandchild": kid, "ownership_hold": hold,
                    "required_ownership_class": "known_group" if name == "ownership_group" else
                    "known_current_parent" if name == "ownership_slow" else "known_or_unproved"})
            return status()
        if name in ("ownership_double", "zombie_hold"):
            readfd, writefd = os.pipe()
            def intermediate():
                os.close(readfd)
                intermediate_report(name, writefd, coop, reserve)
            mid = fork_body(intermediate, deadline)
            os.close(writefd)
            try:
                raw, transport = read_pipe(readfd, REPORT_CAP, coop, "mono_join_deadline")
            finally:
                os.close(readfd)
            # The ORIGINAL bounded report bytes (raw_hex), digest, count and EOF/read timing stay beside the merge.
            state["transports"]["intermediate_report"] = transport
            kid, intended = None, None
            try:
                if not transport["eof"] or transport["error"] is not None or not raw.endswith(b"\n") or raw.count(b"\n") != 1:
                    raise ValueError("INTERMEDIATE_REPORT_NOT_COMPLETE")
                report = parse_json(raw)
                if json_line(report) != raw:
                    raise ValueError("INTERMEDIATE_REPORT_NOT_CANONICAL")
                if not isinstance(report, dict) or report.get("kind") != INTERMEDIATE_KIND or \
                        report.get("scenario") != name or report.get("intermediate") != mid or \
                        not integer(report.get("grandchild")) or report.get("mono_module_entry") != START_MONO or \
                        report.get("mono_life_deadline") != deadline or \
                        json_line(report.get("cooperative")) != json_line(coop) or \
                        not finite(report.get("mono_output")) or not report["mono_output"] <= transport["mono_eof"]:
                    raise ValueError("INTERMEDIATE_REPORT_BINDING")
                lists = ("descendants", "joins", "identity_waits", "ownership_edges", "evidence_failures")
                if any(not isinstance(report.get(key), list) for key in lists) or \
                        not isinstance(report.get("transports"), dict) or \
                        not (report.get("error") is None or isinstance(report.get("error"), str)):
                    raise ValueError("INTERMEDIATE_REPORT_LIST_SCHEMA")
                kid = report["grandchild"]
                merge = {}
                for key in lists:
                    merge[key] = [len(state[key]), len(report[key])]
                    state[key].extend(report[key])
                state["intermediate_merge"] = merge
                state["transports"]["intermediate_internal"] = report["transports"]
                if "zombie_hold" in report:
                    state["zombie_hold"] = report["zombie_hold"]
                if report.get("error") is not None:
                    state["intermediate_error"] = report["error"]
                selves = [o for o in report["descendants"] if isinstance(o, dict) and
                          o.get("role") == "intermediate" and o.get("phase") == "self_post_setup"]
                if len(selves) != 1 or selves[0].get("pid") != mid or selves[0].get("observer") != mid or \
                        not identity_valid(selves[0].get("identity")) or selves[0]["identity"]["pid"] != mid:
                    raise ValueError("INTERMEDIATE_INTENDED_INCARNATION_UNAVAILABLE")
                intended = selves[0]["identity"]
            except Exception as error:
                state["evidence_failures"].append("INTERMEDIATE_REPORT_INVALID")
                state["intermediate_report_error"] = repr(error)
            joined = join_child(mid, "intermediate", coop, main_observation["identity"], intended)
            state["joins"].append(joined)
            if not join_ok(joined):
                state["evidence_failures"].append("INTERMEDIATE_JOIN_UNRESOLVED_OR_NONZERO")
            if name == "ownership_double":
                before = next((x["identity"] for x in state["descendants"] if isinstance(x, dict) and
                               x.get("role") == "exec_descendant" and x.get("phase") == "post_exec_pre_reparent" and
                               identity_valid(x.get("identity"))), None)
                if kid is not None:
                    post = observe(kid, "exec_descendant", "post_exec_post_reparent", join_deadline)
                    state["descendants"].append(post)
                    after = post["identity"]
                    same = before is not None and after is not None and all(before[key] == after[key] for key in
                           ("pid", "uniqueid", "idversion", "euid", "ruid", "pgid", "traced"))
                    if not joined["resolved"] or not same or after["ppid"] == mid or after["comm"] != "sleep" or after["status"] == SZOMB:
                        state["evidence_failures"].append("POST_EXEC_REPARENTED_INCARNATION_NOT_PROVED")
                else:
                    state["evidence_failures"].append("EXEC_DESCENDANT_PID_UNAVAILABLE")
            result({"intermediate": mid, "grandchild": kid, "intermediate_status": joined["wait_status"],
                    "required_ownership_class": "known_or_unproved" if name == "ownership_double" else "known_zombie"})
            return status()
        arrivals = []
        if name == "ignore":
            signal.signal(signal.SIGTERM, lambda sig, frame: arrivals.append(time.monotonic()))
        sleep_to(work_end)
        result({"term_arrivals": arrivals})
        return status()
    except BaseException as error:
        state["evidence_failures"].append("MAIN_BODY_ERROR")
        state["main_error"] = repr(error)
        if ofd is not None and not result_attempted:
            try:
                result()
            except BaseException as output_error:
                state["output_error"] = repr(output_error)
        try:
            complete_write(2, b"QUAL_CHILD_ERROR " + json_line(report_object({})), deadline)
        except BaseException:
            pass
        return 1
    finally:
        if ofd is not None:
            os.close(ofd)
        os.close(rfd)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        try:
            os.set_blocking(2, False)
            os.write(2, ("QUAL_CHILD_ERROR %r\n" % error).encode()[:2048])
        except BaseException:
            pass
        sys.exit(2)
