#!/usr/bin/env python3
"""supervise_r3.py: minimal single-threaded supervisor for one command and its process group (macOS libproc).
PA19 supervise_pa19_v6.py = supervise_pa19_v5.py (sha256 a7540cded7c4...bbf5) plus ONE repair (parent re-review of v5): the
finalization window (final signal check, record build/write, handler restoration) runs with SIGTERM/SIGINT BLOCKED;
a signal arriving in that window is delivered only after the outer handlers are restored, so the written record, the
returned record and the observed_signal field are always identical; no record field is changed after the write.
v5 text: PA19 supervise_pa19_v5.py = supervise_pa19_v3.py (sha256 79c463589c9c...573b3) plus the delayed-reap repair (parent
review of v4, 2026-10-18): when the monitor ends with reason None after its zombie-completion branch and the single
poll() has not reaped the leader, delayed_reap() re-checks the signal flag, wall, floor, RSS and strict-sample
problems BEFORE every poll for at most 5 s (no poll after the bound; sleeps bounded by the remaining time). Any trip
stays nonclean; the stop then runs only while the leader is still unreaped (its zombie reserves the PGID), never
after reaping. A signal flagged before the completion record makes the record nonclean, and the observed signal
is returned to the caller (observed_signal) so an outer cancellation is never swallowed.

New version of supervise_r2.py (0b023e2c...8c37), whose controls FAILED on this host (receipt
evidence/k3cubes/supervise_controls_r2.json, 8313d092...18a1). Observed macOS facts behind this version:
  - proc_pidinfo (PROC_PIDTBSDINFO and SHORTBSDINFO) returns 0 with ESRCH for an unreaped exited child (a zombie);
  - proc_listpids(PROC_PGRP_ONLY) still lists that zombie in its group;
  - killpg on a group whose only member is a zombie raises EPERM;
  - os.waitid is not available in this Python 3.9.
Changes from r2:
  - a pid is classified zombie only on positive evidence: ESRCH from proc_pidinfo while the kernel still lists the pid
    in our process group. A leader with ESRCH that is no longer listed stays "leader gone while unreaped"
    (uncertain). A failed or short read is still unknown, never death;
  - the stop sends killpg only while the group has live or unknown members (or when the listing failed). An error
    from killpg is recorded; any live member is then a survivor and causes quarantine;
  - member_state(pid, pgid) exposes the same rule for the controls.
Unchanged from r2: the fail-closed exception path (uncertain UNKNOWN, SIGTERM to the reserved group, bounded wait,
quarantine, a record attempt with fallback, signal handlers restored in a finally block), strict probes, escape
detection, final completion check, no SIGKILL and no subprocess timeout.
Scope, stated exactly. The command starts as a new session and process-group leader. The supervisor watches the
members of that process group, and nothing else. Members keep the group when they are re-parented. A descendant that
leaves the group (setsid/setpgid) is detected only while it is still a child of a live member; detection trips the
run and quarantines capacity. Nothing outside the group is ever signalled. The production commands (lane python
drivers, gram_encB.py, cadical, kissat, drat-trim) do not leave the group.

Every 0.25 s, in the one thread, it probes itself, the leader and every member through proc_pidinfo, using a fresh
group listing from the same sample. Each probe is one of four states:
  - alive: full BSD info, not a zombie, full task info with RSS > 0;
  - zombie: BSD status SZOMB, or (as on this Darwin host) ESRCH while the pid is still listed in our process group;
  - gone: ESRCH and not listed;
  - unknown: any other short, failed or zero-RSS read.
Alive RSS is summed, including the supervisor's own.

Trips:
  - RSS above the cap, free bytes below the floor, elapsed time above the wall cap;
  - SIGTERM or SIGINT to the supervisor (recorded by a flag and handled in the loop);
  - uncertain conditions: an unknown probe, a failed listing, a leader gone while unreaped, or a process that left
    the group;
  - a member still alive after the leader exited.
The leader is never reaped before the stop sequence ends. Its zombie keeps the group ID reserved, so killpg(group,
SIGTERM) cannot reach an unrelated process. killpg is sent only while live or unknown members exist (a zombie-only
group raises EPERM on Darwin). After the signal the supervisor waits at most `grace` seconds for every member to
become a zombie or gone. Survivors, or any uncertain trip, produce an exclusive-create quarantine record
of process identities (pid, ppid, pgid, start time). Code never removes it, and the supervisor refuses to start while
it exists.

Completion: once the leader is a zombie, one final synchronous sample (members, RSS, floor, wall) runs before the
leader is reaped. There is no SIGKILL, no thread and no subprocess timeout. The child environment gets
K3_SUPERVISOR_PID, K3_SUPERVISOR_SCRIPT and K3_SUPERVISOR_RECORD so that workers can refuse to run unsupervised.
Usage: /usr/bin/python3 -I -B supervise_r3.py --name N --wall S --rss-cap B --floor B --lane DIR
                                              --record OUT.json --quarantine Q.json [--grace 30] -- COMMAND [ARGS...]
"""
import argparse
import ctypes
import datetime
import errno
import hashlib
import json
import os
import signal
import struct
import subprocess
import sys
import time

LIBPROC = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
LIBPROC.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_pidinfo.restype = ctypes.c_int
LIBPROC.proc_listpids.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_int)
LIBPROC.proc_listpids.restype = ctypes.c_int
PROC_PGRP_ONLY, PROC_PPID_ONLY = 2, 6
PROC_PIDTBSDINFO, BSD_SIZE = 3, 136
PROC_PIDTASKINFO, TASK_SIZE = 4, 96
SZOMB = 5
PERIOD = 0.25
LIST_SLOTS = 4096


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _read(pidinfo, pid, flavor, size):
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    n = pidinfo(pid, flavor, 0, buf, size)
    return n, ctypes.get_errno(), buf.raw


def _identity(raw):
    status, _xstatus, pid, ppid = struct.unpack_from("=IIII", raw, 4)
    return {"pid": pid, "ppid": ppid, "pgid": struct.unpack_from("=I", raw, 100)[0], "status": status,
            "start": list(struct.unpack_from("=QQ", raw, 120)),
            "comm": raw[48:64].split(b"\0")[0].decode("ascii", "replace")}


def probe(pid, pidinfo=None):
    """Return (state, rss, identity) with state alive, zombie, gone or unknown. Never maps a failed read to zero."""
    pidinfo = pidinfo or LIBPROC.proc_pidinfo
    n, err, raw = _read(pidinfo, pid, PROC_PIDTBSDINFO, BSD_SIZE)
    if n != BSD_SIZE:
        state = "gone" if n == 0 and err == errno.ESRCH else "unknown"
        return state, 0, {"pid": pid, "bsd_bytes": n, "errno": err}
    ident = _identity(raw)
    if ident["pid"] != pid:
        return "unknown", 0, dict(ident, reason="pid mismatch")
    if ident["status"] == SZOMB:
        return "zombie", 0, ident
    m, terr, traw = _read(pidinfo, pid, PROC_PIDTASKINFO, TASK_SIZE)
    if m == TASK_SIZE:
        rss = struct.unpack_from("=Q", traw, 8)[0]
        if rss > 0:
            return "alive", rss, ident
        return "unknown", 0, dict(ident, reason="zero resident size")
    n2, err2, raw2 = _read(pidinfo, pid, PROC_PIDTBSDINFO, BSD_SIZE)
    if n2 == 0 and err2 == errno.ESRCH:
        return "gone", 0, ident
    if n2 == BSD_SIZE and _identity(raw2)["status"] == SZOMB and _identity(raw2)["start"] == ident["start"]:
        return "zombie", 0, ident
    return "unknown", 0, dict(ident, task_bytes=m, task_errno=terr)


def list_pids(kind, value, listpids=None):
    listpids = listpids or LIBPROC.proc_listpids
    buf = (ctypes.c_int * LIST_SLOTS)()
    ctypes.set_errno(0)
    n = listpids(kind, value, buf, ctypes.sizeof(buf))
    err = ctypes.get_errno()
    if n < 0 or (n == 0 and err != 0) or n >= ctypes.sizeof(buf):
        raise OSError(err, "proc_listpids(%d, %d) returned %d" % (kind, value, n))
    return sorted({p for p in buf if p > 0})


def member_state(pid, pgid, probe_fn=probe, members=None):
    """probe() plus the macOS zombie rule: ESRCH while still listed in our process group means zombie."""
    state, rss, ident = probe_fn(pid)
    if state == "gone":
        listed = members if members is not None else list_pids(PROC_PGRP_ONLY, pgid)
        if pid in listed:
            return "zombie", 0, dict(ident, zombie_evidence="ESRCH while listed in process group %d" % pgid)
    return state, rss, ident


def sample(pgid, leader, probe_fn, observed):
    """One strict sample of the supervisor and the group. Problems are (reason, uncertain) pairs."""
    problems, total, alive_others = [], 0, []
    state, rss, ident = probe_fn(os.getpid())
    if state != "alive":
        problems.append(("unknown probe of the supervisor itself: %r" % (ident,), True))
    total += rss
    try:
        members = list_pids(PROC_PGRP_ONLY, pgid)
        listing_ok = True
    except OSError as exc:
        problems.append(("process-group listing failed: %r" % (exc,), True))
        members, listing_ok = [], False
    leader_state = None
    for pid in sorted(set(members) | {leader}):
        if listing_ok:
            state, rss, ident = member_state(pid, pgid, probe_fn, members)
        else:
            state, rss, ident = probe_fn(pid)
        if state in ("alive", "zombie"):
            observed.setdefault(str(pid), ident)
        if pid == leader:
            leader_state = state
            if state == "gone":
                problems.append(("leader gone while unreaped", True))
        if state == "unknown":
            problems.append(("unknown probe of pid %d: %r" % (pid, ident), True))
        if state != "alive":
            continue
        total += rss
        if pid != leader:
            alive_others.append(pid)
        try:
            kids = list_pids(PROC_PPID_ONLY, pid)
        except OSError as exc:
            problems.append(("child listing failed for pid %d: %r" % (pid, exc), True))
            continue
        for kid in kids:
            kstate, _, kident = probe_fn(kid)
            if kstate == "unknown":
                problems.append(("unknown probe of pid %d: %r" % (kid, kident), True))
            elif kstate == "alive" and kident.get("pgid") != pgid:
                observed.setdefault(str(kid), kident)
                problems.append(("pid %d left the supervised process group" % kid, True))
    return {"total_rss": total, "leader_state": leader_state, "members": members, "alive_others": alive_others,
            "problems": problems}


def live_members(pgid, probe_fn, observed):
    """Members that are alive or unknown (zombies excluded by the listed-ESRCH rule). Raises OSError if the listing
    fails; probe exceptions propagate to the caller's fallback."""
    members = list_pids(PROC_PGRP_ONLY, pgid)
    live = []
    for pid in members:
        state, _, ident = member_state(pid, pgid, probe_fn, members)
        if state in ("alive", "unknown"):
            observed.setdefault(str(pid), ident)
            live.append({"pid": pid, "state": state, "identity": ident})
    return live


def stop_group(pgid, grace, probe_fn, observed):
    """SIGTERM the group while it has live or unknown members (the unreaped leader reserves the group ID); wait at most
    `grace` seconds. Members that are only zombies are not signalled, because killpg would raise EPERM."""
    sent, kill_error = False, None
    try:
        live = live_members(pgid, probe_fn, observed)
    except OSError:
        live = None
    if live is None or live:
        try:
            os.killpg(pgid, signal.SIGTERM)
            sent = True
        except OSError as exc:
            kill_error = repr(exc)
    deadline = time.monotonic() + grace
    while True:
        try:
            live, listing_ok = live_members(pgid, probe_fn, observed), True
        except OSError:
            live, listing_ok = None, False
        if listing_ok and not live:
            return {"sigterm_sent": sent, "killpg_error": kill_error, "survivors": [], "listing_ok": True}
        if time.monotonic() > deadline:
            return {"sigterm_sent": sent, "killpg_error": kill_error,
                    "survivors": live if live is not None else "unknown: group listing failed",
                    "listing_ok": listing_ok}
        time.sleep(0.1)


def write_quarantine(path, record):
    try:
        with open(path, "x") as f:
            json.dump(record, f, indent=2)
            f.write("\n")
        return path
    except FileExistsError:
        return path + " (already present)"


def stop_with_fallback(pgid, grace, probe_fn, observed):
    """stop_group; if measurement fails during the stop, one killpg SIGTERM to the reserved group, a bounded wait
    without measurement, and survivors reported as unknown (the caller quarantines)."""
    try:
        return stop_group(pgid, grace, probe_fn, observed), None
    except Exception as exc:
        try:
            os.killpg(pgid, signal.SIGTERM)
            sent = True
        except Exception:
            sent = False
        time.sleep(grace)
        return {"sigterm_sent": sent, "survivors": "unknown: stop measurement failed", "listing_ok": False}, repr(exc)


def monitor(child, state, wall, rss_cap, floor, lane, probe_fn, flag, t0):
    """The sampling loop. Sets state['reason'], state['uncertain'] and state['final']; any exception propagates."""
    pgid, observed = child.pid, state["observed"]
    state["leader_identity_at_start"] = probe_fn(child.pid)[2]
    while True:
        s = sample(pgid, child.pid, probe_fn, observed)
        state["samples"] += 1
        state["peak"] = max(state["peak"], s["total_rss"])
        st = os.statvfs(lane)
        free, elapsed = st.f_bavail * st.f_frsize, time.monotonic() - t0
        if s["problems"]:
            state["reason"], state["uncertain"] = s["problems"][0]
        elif s["total_rss"] > rss_cap:
            state["reason"] = "aggregate RSS %d above %d" % (s["total_rss"], rss_cap)
        elif free < floor:
            state["reason"] = "free bytes %d below floor %d" % (free, floor)
        elif elapsed > wall:
            state["reason"] = "wall cap %s s" % wall
        elif "signal" in flag:
            state["reason"] = "external %s" % flag["signal"]
        elif s["leader_state"] == "zombie" and s["alive_others"]:
            state["reason"] = "group member alive after leader exit: %r" % (s["alive_others"],)
        elif s["leader_state"] == "zombie":
            final = sample(pgid, child.pid, probe_fn, observed)
            st = os.statvfs(lane)
            free, elapsed = st.f_bavail * st.f_frsize, time.monotonic() - t0
            state["peak"] = max(state["peak"], final["total_rss"])
            state["final"] = {"problems": final["problems"], "members": final["members"],
                              "alive_others": final["alive_others"]}
            if final["problems"]:
                state["reason"], state["uncertain"] = final["problems"][0]
            elif final["alive_others"]:
                state["reason"] = "group member alive at completion: %r" % (final["alive_others"],)
            elif final["total_rss"] > rss_cap:
                state["reason"] = "aggregate RSS %d above %d at completion" % (final["total_rss"], rss_cap)
            elif free < floor:
                state["reason"] = "free bytes %d below floor %d at completion" % (free, floor)
            elif elapsed > wall:
                state["reason"] = "wall cap %s s at completion" % wall
            return
        if state["reason"] is not None:
            return
        time.sleep(PERIOD)


def delayed_reap(child, state, wall, rss_cap, floor, lane, probe_fn, flag, t0, limit=5.0, period=0.01):
    """PA19 v5: the leader was classified exited, but waitpid has not reaped it yet. Until it is reaped, for at most
    `limit` seconds, every iteration first runs the strict sample plus floor/wall/signal checks and only then polls;
    no poll happens after the bound. A trip sets the reason (nonclean) and returns with the leader still unreaped."""
    pgid, observed = child.pid, state["observed"]
    end = time.monotonic() + limit
    while True:
        s = sample(pgid, child.pid, probe_fn, observed)
        state["samples"] += 1
        state["peak"] = max(state["peak"], s["total_rss"])
        st = os.statvfs(lane)
        free, elapsed = st.f_bavail * st.f_frsize, time.monotonic() - t0
        if s["problems"]:
            state["reason"], state["uncertain"] = s["problems"][0]
        elif s["alive_others"]:
            state["reason"] = "group member alive during delayed reap: %r" % (s["alive_others"],)
        elif s["total_rss"] > rss_cap:
            state["reason"] = "aggregate RSS %d above %d during delayed reap" % (s["total_rss"], rss_cap)
        elif free < floor:
            state["reason"] = "free bytes %d below floor %d during delayed reap" % (free, floor)
        elif elapsed > wall:
            state["reason"] = "wall cap %s s during delayed reap" % wall
        elif "signal" in flag:
            state["reason"] = "external %s during delayed reap" % flag["signal"]
        if state["reason"] is not None or time.monotonic() >= end:
            return
        child.poll()
        if child.returncode is not None:
            return
        remaining = end - time.monotonic()
        if remaining <= 0:
            return
        time.sleep(min(period, remaining))


def supervise(command, name, wall, rss_cap, floor, lane, record_path, quarantine_path, grace=30.0, probe_fn=probe, owner_child=None):
    if os.path.exists(quarantine_path):
        raise SystemExit("quarantine record %s exists; admission refused" % quarantine_path)
    if os.path.exists(record_path):
        raise FileExistsError(record_path)
    flag = {}

    def on_signal(signum, frame):
        flag.setdefault("signal", signal.Signals(signum).name)
    previous = {s: signal.signal(s, on_signal) for s in (signal.SIGTERM, signal.SIGINT)}
    rec = {"name": name, "started_at": now(), "command": command, "supervisor_pid": os.getpid(),
           "limits": {"wall_seconds": wall, "rss_cap_bytes": rss_cap, "floor_bytes": floor, "grace_seconds": grace,
                      "period_seconds": PERIOD},
           "scope": "the command's process group only; members keep it across re-parenting; leaving the group is "
                    "detected while still a child of a live member; nothing outside the group is signalled"}
    state = {"reason": None, "uncertain": False, "final": None, "observed": {}, "samples": 0, "peak": 0,
             "leader_identity_at_start": None}
    stop = stop_error = quarantined = exception = None
    child = None
    t0 = time.monotonic()
    try:
        rec["supervisor_sha256"] = sha(os.path.abspath(__file__))
        rec["command_files_sha256"] = {a: sha(a) for a in command if os.path.isfile(a)}
        env = dict(os.environ, K3_SUPERVISOR_PID=str(os.getpid()), K3_SUPERVISOR_SCRIPT=os.path.abspath(__file__),
                   K3_SUPERVISOR_RECORD=os.path.abspath(record_path))
        child = subprocess.Popen(command, start_new_session=True, stdin=subprocess.DEVNULL, env=env)
        if owner_child is not None:
            owner_child.append(child)  # PA19 v3: outer owner retains the exact Popen through late reaping
        monitor(child, state, wall, rss_cap, floor, lane, probe_fn, flag, t0)
    except BaseException as exc:
        state["reason"] = "supervisor exception: %r" % (exc,)
        state["uncertain"] = True
        exception = repr(exc)
    finally:
        try:
            if child is not None and state["reason"] is None and state["final"] is not None:
                child.poll()  # PA19 v5: the single v3 poll, now before the stop decision
                if child.returncode is None:
                    delayed_reap(child, state, wall, rss_cap, floor, lane, probe_fn, flag, t0)
            if child is not None and state["reason"] is not None and child.returncode is None:
                stop, stop_error = stop_with_fallback(child.pid, grace, probe_fn, state["observed"])
                if stop_error is not None:
                    state["uncertain"] = True
            if child is not None and state["reason"] is not None:  # PA19 v5: clean path already polled (bounded)
                child.poll()
            survivors = stop is not None and (stop["survivors"] or not stop["listing_ok"])
            if child is not None and (state["uncertain"] or survivors):
                quarantined = write_quarantine(quarantine_path, {
                    "at": now(), "name": name, "reason": state["reason"], "uncertain": state["uncertain"],
                    "survivors": stop["survivors"] if stop else "unknown: no stop record",
                    "observed_identities": state["observed"], "leader_pid": child.pid,
                    "rule": "no SIGKILL sent; refuse every later admission while this record exists"})
        except Exception as exc:
            rec["cleanup_exception"] = repr(exc)
            state["uncertain"] = True
            if child is not None and quarantined is None:
                try:
                    quarantined = write_quarantine(quarantine_path, {
                        "at": now(), "name": name, "reason": state["reason"], "uncertain": True,
                        "cleanup_exception": repr(exc), "leader_pid": child.pid,
                        "observed_identities": state["observed"],
                        "rule": "no SIGKILL sent; refuse every later admission while this record exists"})
                except Exception as exc2:
                    rec["quarantine_write_error"] = repr(exc2)
        finally:
          blocked = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGTERM, signal.SIGINT})  # PA19 v6 finalization window
          try:
            if "signal" in flag and state["reason"] is None:  # PA19 v5: a flagged cancellation is never clean
                state["reason"] = "external %s before the completion record" % flag["signal"]
            rec.update({"finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
                        "samples": state["samples"], "peak_sampled_rss_bytes": state["peak"],
                        "leader_identity_at_start": state["leader_identity_at_start"],
                        "trip_reason": state["reason"], "uncertain": state["uncertain"], "exception": exception,
                        "final_check": state["final"], "stop": stop, "stop_error": stop_error,
                        "leader_pid": child.pid if child is not None else None,
                        "leader_returncode": child.returncode if child is not None else None,
                        "observed_identities": state["observed"], "quarantine_record": quarantined,
                        "observed_signal": flag.get("signal"),
                        "completed_cleanly": state["reason"] is None and child is not None
                        and child.returncode == 0 and not rec.get("cleanup_exception")})
            try:
                with open(record_path, "x") as f:
                    json.dump(rec, f, indent=2)
                    f.write("\n")
            except Exception as exc:
                rec["record_write_error"] = repr(exc)
                try:
                    with open(record_path + ".failure.json", "x") as f:
                        json.dump(rec, f, indent=2)
                        f.write("\n")
                except Exception:
                    pass
            for s_, handler in previous.items():
                signal.signal(s_, handler)
          finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, blocked)  # PA19 v6: pending signals reach the restored outer handlers
    return rec


def main():
    if "--" not in sys.argv:
        raise SystemExit("usage: supervise_r3.py OPTIONS -- COMMAND [ARGS...]")
    split = sys.argv.index("--")
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--wall", type=float, required=True)
    ap.add_argument("--rss-cap", type=int, required=True)
    ap.add_argument("--floor", type=int, required=True)
    ap.add_argument("--lane", required=True)
    ap.add_argument("--record", required=True)
    ap.add_argument("--quarantine", required=True)
    ap.add_argument("--grace", type=float, default=30.0)
    a = ap.parse_args(sys.argv[1:split])
    command = sys.argv[split + 1:]
    if not command:
        raise SystemExit("empty command")
    rec = supervise(command, a.name, a.wall, a.rss_cap, a.floor, a.lane, a.record, a.quarantine, a.grace)
    print(json.dumps({k: rec[k] for k in ("name", "completed_cleanly", "trip_reason", "uncertain", "leader_returncode",
                                          "quarantine_record", "seconds")}), flush=True)
    raise SystemExit(0 if rec["completed_cleanly"] else 3)


if __name__ == "__main__":
    main()
