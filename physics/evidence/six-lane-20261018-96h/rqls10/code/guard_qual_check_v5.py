#!/usr/bin/env python3
"""guard_qual_check_v5: check one guard-qualification scenario of code/owned_supervisor_v9.py against its preregistered
expectation (plan evidence/owned_supervisor_v9-guard-qualification-plan-v5.md). Supersedes guard_qual_check_v4.py (never
run) after the Codex review of package v4 (RUN/review/rqls10-guard-qualification-v4-codex-v1.prompt.stdout.txt):
independent hashing of every artifact (findings 1, 3), exact outcome sets (finding 2), identity proofs from samples and
child reports (finding 3), fixed anchored locations (finding 4), correct identifier and exit code (finding 7).
Usage: guard_qual_check_v5.py SCENARIO     (reads QROOT/SCENARIO only; writes QROOT/SCENARIO/check.json exclusively)
Exit 0 only for PASS, 1 for FAIL, 2 for a checker error. A PASS is evidence for this one observed control only; the
parent's release transaction (plan v5) is separate and required before any next invocation.
"""
import hashlib, json, math, os, stat, sys

VERSION = "guard_qual_check_v5"
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
QROOT = LANE + "/qual-pkg-v5"
CHILD = LANE + "/code/guard_qual_child_v6.py"
SUPERVISOR_SHA = "c7674b907a37297cc35758ce994983b5b6878c07f994b387225e422a3283a1cd"
ITEM = "owned_supervisor_v9 guard qualification"
RESERVATION = 20971520
FIXTURE = b"pinned scratch file for the mutate_pin scenario\n"
SC = {
    "date_fault": ("ok", 5, 60, "date_helper_fails", True, 2147483648, None),
    "go_unlisted": ("ok", 5, 60, None, True, 2147483648, None),
    "ok": ("ok", 5, 60, None, True, 2147483648, None),
    "rc_nonzero": ("rc_nonzero", 5, 60, None, True, 2147483648, None),
    "missing_output": ("no_output", 5, 60, None, True, 2147483648, None),
    "mutate_pin": ("mutate_pin", 5, 60, None, True, 2147483648, "PIN"),
    "mutate_evidence": ("mutate_evidence", 5, 60, None, True, 2147483648, "LAUNCH_RECORD"),
    "stray_file": ("stray_file", 5, 60, None, True, 2147483648, None),
    "deadline": ("sleep", 120, 10, None, False, 2147483648, None),
    "flood": ("flood", 60, 60, None, False, 2147483648, None),
    "busy": ("busy2", 60, 60, None, False, 2147483648, None),
    "rss": ("rss", 60, 60, None, False, 268435456, None),
    "zombie_hold": ("zombie_hold", 10, 60, None, True, 2147483648, None),
    "escape_slow": ("escape_slow", 40, 60, None, True, 2147483648, None),
    "escape_fast": ("escape_fast", 40, 60, None, True, 2147483648, None),
    "double_fork_escape": ("double_fork_escape", 40, 60, None, True, 2147483648, None),
    "ignore": ("ignore_term", 60, 10, None, False, 2147483648, None),
    "identity": ("sleep", 60, 10, "identity_check_fails", False, 2147483648, None),
}
BASE = {"launch.json", "samples.jsonl", "stdout.txt", "stderr.txt", "supervisor-receipt.json", "settlement.json",
        "settlement.json.staged"}
PUB = {"supervisor-receipt.json", "settlement.json", "settlement.json.staged"}
ESC = {"GRACE_EXPIRED_AFTER_CHILD_EXIT", "BLOCKING_LIVE", "STREAMS_NOT_CLOSED", "SINK_THREADS_NOT_FINISHED"}
IGN = {"GRACE_EXPIRED_AFTER_STOP_REQUEST", "CHILD_NOT_REAPED", "BLOCKING_LIVE", "STREAMS_NOT_CLOSED",
       "SINK_THREADS_NOT_FINISHED"}


def E(settlement, exit_code, rc, loop, trips, failures, signal, stop, names, admission=None):
    return {"settlement": settlement, "exit": exit_code, "rc": rc, "loop": loop, "trips": trips,
            "failures": set(failures), "signal": signal, "stop": stop, "names": names, "admission": admission}


EXPECT = {
    "date_fault": E("NOT_LAUNCHED", 10, None, "NOT_STARTED", [], {"HELPER_FAULT_INJECTED"}, None, None, PUB,
                    {"DATE_HELPER_UNAVAILABLE", "STABILITY_AGE_UNVERIFIABLE", "FAILURE_LATCHED"}),
    "go_unlisted": E("NOT_LAUNCHED", 10, None, "NOT_STARTED", [], set(), None, None, PUB,
                     {"GO_DOES_NOT_NAME_THIS_CONFIG"}),
    "ok": E("SETTLED", 0, 0, "EXITED", [], set(), None, None, BASE | {"child-out.json"}),
    "rc_nonzero": E("SETTLED", 0, 3, "EXITED", [], set(), None, None, BASE | {"child-out.json"}),
    "missing_output": E("UNSETTLED", 11, 0, "EXITED", [], {"REQUIRED_OUTPUT_MISSING"}, "not_sent", "FAILURE", BASE),
    "mutate_pin": E("UNSETTLED", 11, 0, "EXITED", [], {"PIN_CHANGED_OR_UNREADABLE"}, "not_sent", "FAILURE",
                    BASE | {"child-out.json"}),
    "mutate_evidence": E("UNSETTLED", 11, 0, "EXITED", [], {"EVIDENCE_MUTATED"}, "not_sent", "FAILURE",
                         BASE | {"child-out.json"}),
    "stray_file": E("UNSETTLED", 11, 0, "EXITED", [], {"UNDECLARED_ENTRIES"}, "not_sent", "FAILURE",
                    BASE | {"child-out.json", "stray.txt"}),
    "deadline": E("SETTLED", 0, -15, "EXITED", ["DEADLINE"], set(), "sent", "DEADLINE", BASE),
    "flood": E("SETTLED", 0, -15, "EXITED", ["STREAM_CAP"], set(), "sent", "STREAM_CAP", BASE),
    "busy": E("SETTLED", 0, -15, "EXITED", ["BUSY"], set(), "sent", "BUSY", BASE),
    "rss": E("SETTLED", 0, -15, "EXITED", ["RSS"], set(), "sent", "RSS", BASE),
    "zombie_hold": E("SETTLED", 0, 0, "EXITED", [], set(), None, None, BASE | {"child-out.json"}),
    "escape_slow": E("UNSETTLED", 11, 0, "GRACE_EXPIRED_AFTER_CHILD_EXIT", [], ESC, "not_sent", "FAILURE",
                     BASE | {"child-out.json"}),
    "escape_fast": E("UNSETTLED", 11, 0, "GRACE_EXPIRED_AFTER_CHILD_EXIT", [], ESC, "not_sent", "FAILURE",
                     BASE | {"child-out.json"}),
    "double_fork_escape": E("UNSETTLED", 11, 0, "GRACE_EXPIRED_AFTER_CHILD_EXIT", [],
                            {"GRACE_EXPIRED_AFTER_CHILD_EXIT", "BLOCKING_LIVE"}, "not_sent", "FAILURE",
                            BASE | {"child-out.json"}),
    "ignore": E("UNSETTLED", 11, None, "GRACE_EXPIRED_AFTER_STOP_REQUEST", ["DEADLINE"], IGN, "sent", "DEADLINE", BASE),
    "identity": E("UNSETTLED", 11, None, "GRACE_EXPIRED_AFTER_STOP_REQUEST", ["DEADLINE"], IGN | {"IDENTITY_UNVERIFIED"},
                  "not_sent", "DEADLINE", BASE),
}


class Bad(Exception):
    pass


def _pairs(kv):
    d = {}
    for k, v in kv:
        if k in d:
            raise ValueError("duplicate key %r" % k)
        d[k] = v
    return d


def _const(name):
    raise ValueError("non-finite constant %s" % name)


def _float(s):
    x = float(s)
    if not math.isfinite(x):
        raise ValueError("overflowing numeric literal %s" % s)
    return x


def jload(raw):
    return json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_const, parse_float=_float)


def probe(path, maxb=64 << 20):
    try:
        st0 = os.lstat(path)
    except FileNotFoundError:
        return ("ABSENT", None, None, None)
    if not stat.S_ISREG(st0.st_mode) or st0.st_size > maxb:
        raise Bad("not a bounded regular file: %s" % path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        st1 = os.fstat(fd)
        if (st1.st_dev, st1.st_ino, st1.st_size) != (st0.st_dev, st0.st_ino, st0.st_size):
            raise Bad("changed while opening: %s" % path)
        parts, got = [], 0
        while got < st0.st_size:
            chunk = os.read(fd, st0.st_size - got)
            if not chunk:
                raise Bad("short read: %s" % path)
            parts.append(chunk)
            got += len(chunk)
        if os.read(fd, 1):
            raise Bad("grew while read: %s" % path)
    finally:
        os.close(fd)
    raw = b"".join(parts)
    return ("PRESENT", raw, hashlib.sha256(raw).hexdigest(), st0)


def need(path, maxb=64 << 20):
    p = probe(path, maxb)
    if p[0] != "PRESENT":
        raise Bad("required file absent: %s" % path)
    return p


def isint(x, lo=None):
    return isinstance(x, int) and not isinstance(x, bool) and (lo is None or x >= lo)


def isfin(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def code(reason):
    return reason.split(" ", 1)[0] if isinstance(reason, str) else None


def config_for(name, py, py_sha, child_sha, outstanding, lane_outstanding):
    mode, life, wall, fault, req, rss_trip, target = SC[name]
    run = os.path.join(QROOT, name)
    outd = os.path.join(run, "out")
    out = os.path.join(outd, "child-out.json")
    launch = os.path.join(outd, "launch.json")
    pins = [{"path": CHILD, "sha256": child_sha}, {"path": py, "sha256": py_sha}]
    argv = [py, "-I", "-B", CHILD, mode, out, str(life)]
    if target == "PIN":
        pins.append({"path": os.path.join(run, "pinned-scratch.txt"), "sha256": hashlib.sha256(FIXTURE).hexdigest()})
        argv.append(os.path.join(run, "pinned-scratch.txt"))
    elif target == "LAUNCH_RECORD":
        argv.append(launch)
    return {
        "item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE, "argv": argv,
        "env": {"TMPDIR": os.path.join(run, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
                "OMP_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "stdout": os.path.join(outd, "stdout.txt"), "stderr": os.path.join(outd, "stderr.txt"),
        "stdout_cap_bytes": 1048576, "stderr_cap_bytes": 1048576,
        "outputs": [{"path": out, "required": req}],
        "launch_record": launch, "samples": os.path.join(outd, "samples.jsonl"),
        "samples_cap_bytes": 2097152, "receipt": os.path.join(outd, "supervisor-receipt.json"),
        "settlement_record": os.path.join(outd, "settlement.json"), "output_roots": [outd], "pins": pins,
        "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0, "max_chunk_seconds": 10800,
        "owned_compute_settled_by_epoch": 1792731393.0, "rss_trip_bytes": rss_trip, "free_trip_bytes": 12200000000,
        "output_trip_bytes": 9437184, "launch_free_min_bytes": 12200000000, "lane_roots": [LANE],
        "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 5.0,
        "busy_limit": 1 if name == "busy" else 2, "cpu_slots": 2 if name == "busy" else 1,
        "busy_cpu_fraction": 0.5, "rss_projection_bytes": 67108864,
        "admission": {"go_path": os.path.join(run, "go.json"), "reservation_bytes": RESERVATION,
                      "outstanding_reservations_bytes": outstanding,
                      "lane_outstanding_reservations_bytes": lane_outstanding,
                      "stability_receipt_path": os.path.join(run, "stability.json"), "stability_max_age_s": 300},
        "helper_budget": {"max_calls": 8, "call_budget_s": 5.0, "term_grace_s": 5.0},
        "fault_injection": ({fault: True} if fault else {})}


def ids_from_stdout(raw):
    out = {}
    for line in raw.decode("utf-8", "replace").split("\n"):
        if line.startswith("IDS "):
            out.update(jload(line[4:].encode("utf-8")))
    return out


def check(name):
    exp = EXPECT[name]
    run = os.path.join(QROOT, name)
    od = os.path.join(run, "out")
    C, notes = {}, []
    res = {"checker": VERSION, "scenario": name, "run_dir": run, "criteria": C, "notes": notes}
    # ---------------------------------------------------------------- binding
    cp = need(os.path.join(run, "config.json"), 1 << 20)
    cfg = jload(cp[1])
    pins = {p["path"]: p["sha256"] for p in cfg.get("pins", [])}
    py = cfg["argv"][0]
    child_sha = pins.get(CHILD)
    C["config_reconstructed_exactly"] = cfg == config_for(name, py, pins.get(py), child_sha,
                                                          cfg["admission"]["outstanding_reservations_bytes"],
                                                          cfg["admission"]["lane_outstanding_reservations_bytes"])
    C["pins_match_actual_files"] = all(need(p, 1 << 30)[2] == h for p, h in pins.items()) or name == "mutate_pin"
    if name == "mutate_pin":
        C["pins_match_actual_files"] = all(need(p, 1 << 30)[2] == h for p, h in pins.items()
                                           if not p.endswith("pinned-scratch.txt"))
    gop = need(cfg["admission"]["go_path"], 1 << 20)
    go = jload(gop[1])
    entry = {"output_roots": cfg["output_roots"], "argv": cfg["argv"], "max_wall_s": cfg["max_wall_s"],
             "cpu_slots": cfg["cpu_slots"], "reservation_bytes": RESERVATION,
             "outstanding_reservations_bytes": cfg["admission"]["outstanding_reservations_bytes"],
             "lane_outstanding_reservations_bytes": cfg["admission"]["lane_outstanding_reservations_bytes"]}
    if name == "go_unlisted":
        C["go_per_invocation"] = go.get("decision") == "GO" and go.get("item") == ITEM and \
            isinstance(go.get("configs"), dict) and cp[2] not in go["configs"] and isfin(go.get("not_after_epoch"))
    else:
        C["go_per_invocation"] = go.get("decision") == "GO" and go.get("item") == ITEM and \
            go.get("configs") == {cp[2]: entry} and isfin(go.get("not_after_epoch"))
    stp = need(cfg["admission"]["stability_receipt_path"], 1 << 20)
    rp = need(cfg["receipt"])
    rc_ = jload(rp[1])
    sp = need(cfg["settlement_record"], 1 << 20)
    stg = need(cfg["settlement_record"] + ".staged", 1 << 20)
    st = jload(sp[1])
    lines = [x for x in need(os.path.join(run, "supervisor-summary.txt"), 1 << 20)[1].decode("utf-8").split("\n")
             if x.strip()]
    if len(lines) != 1:
        raise Bad("the captured supervisor summary must be exactly one line")
    summ = jload(lines[0].encode("utf-8"))
    adm = rc_.get("admission") or {}
    C["receipt_binding"] = rc_.get("supervisor") == "owned_supervisor_v9" and \
        rc_.get("supervisor_sha256") == SUPERVISOR_SHA and rc_.get("config_sha256") == cp[2] and \
        adm.get("go_sha256") == gop[2] and adm.get("stability_sha256") == stp[2]
    C["settlement_binding"] = st.get("receipt_sha256") == rp[2] and st.get("config_sha256") == cp[2] and \
        st.get("settlement") == rc_.get("settlement") == exp["settlement"] and \
        st.get("failures") == [f.get("reason") for f in rc_.get("failures") or []] and \
        st.get("trips") == [t.get("trip") for t in rc_.get("trips") or []] and stg[2] == sp[2] and \
        (sp[3].st_dev, sp[3].st_ino) == (stg[3].st_dev, stg[3].st_ino) and sp[3].st_nlink == 2
    C["summary_binding"] = summ.get("acknowledged") is True and summ.get("exit_code") == exp["exit"] and \
        summ.get("settlement") == exp["settlement"] and summ.get("receipt_sha256") == rp[2] and \
        summ.get("settlement_record_sha256") == sp[2] and summ.get("supervisor") == "owned_supervisor_v9" and \
        summ.get("config_sha256") == cp[2] and isfin(summ.get("post_publish_mono")) and \
        isfin(rc_.get("mono_decision")) and summ["post_publish_mono"] >= rc_["mono_decision"]
    launched = exp["settlement"] != "NOT_LAUNCHED"
    names = sorted(os.listdir(od))
    late = []
    want = set(exp["names"])
    if name in ("ignore", "identity") and "child-out.json" in names:
        cop = need(os.path.join(od, "child-out.json"), 1 << 20)
        if not (isfin(rc_.get("epoch_decision")) and cop[3].st_birthtime > rc_["epoch_decision"]):
            raise Bad("child output present but not later than the supervisor decision")
        late.append("child-out.json")
        want = want | {"child-out.json"}
    res["late_artifacts"] = late
    C["inventory_exact"] = set(names) == want and \
        set((rc_.get("output_root_inventory") or {}).get(od) or []) | PUB == want - set(late) | PUB
    # ---------------------------------------------------------------- exact outcome
    failures = [code(f.get("reason")) for f in rc_.get("failures") or []]
    C["failure_codes_exact"] = set(failures) == exp["failures"] and rc_.get("failures_n") == len(failures)
    C["trips_exact"] = [t.get("trip") for t in rc_.get("trips") or []] == exp["trips"]
    C["child_rc"] = rc_.get("child_returncode") == exp["rc"] and (exp["rc"] is None or isint(exp["rc"]))
    C["loop_status"] = rc_.get("loop_status") == exp["loop"]
    sig = rc_.get("signal")
    if exp["signal"] is None:
        C["signal"] = sig is None
    elif exp["signal"] == "sent":
        C["signal"] = isinstance(sig, dict) and sig.get("sent") is True and sig.get("identity_ok") is True and \
            isfin(sig.get("mono_sent"))
    else:
        C["signal"] = isinstance(sig, dict) and sig.get("sent") is False
    stop = rc_.get("stop_request")
    C["stop_reason"] = (stop is None) if exp["stop"] is None else (isinstance(stop, dict) and stop.get("reason") == exp["stop"])
    if exp["admission"] is not None:
        C["admission_reasons_exact"] = {code(r) for r in adm.get("reasons") or []} == exp["admission"]
    helpers = rc_.get("helpers") or []
    hlog = rc_.get("helper_log") or []
    allowed = {"OK", "REFUSED_AFTER_FAILURE_LATCH"} | ({"FAULT_INJECTED"} if name == "date_fault" else set())
    C["helpers_settled"] = all(h.get("state") == "SETTLED" for h in helpers) and \
        all(e.get("outcome") in allowed for e in hlog) and rc_.get("helper_calls") == len(helpers) == \
        sum(1 for e in hlog if e.get("outcome") == "OK")
    C["dates_are_bin_date_or_null"] = all(d is None or (isinstance(d, str) and len(d) == 24)
                                          for d in (adm.get("date"), rc_.get("end_date")))
    if not launched:
        res["verdict"] = "PASS" if all(C.values()) else "FAIL"
        return res
    # ---------------------------------------------------------------- launched: artifacts, samples, proofs
    launch = jload(need(cfg["launch_record"], 1 << 20)[1])
    ident = launch.get("identity") or {}
    C["launch_binding"] = launch.get("supervisor_sha256") == SUPERVISOR_SHA and launch.get("config_sha256") == cp[2] and \
        launch.get("argv") == cfg["argv"] and all(isint(ident.get(k), 1) for k in ("pid", "uniqueid", "pgid")) and \
        ident.get("pgid") == ident.get("pid") and rc_.get("child_pid") == ident.get("pid")
    arts, ev = rc_.get("artifacts") or {}, rc_.get("evidence_expected_sha256") or {}
    ok_art = True
    own = {}
    for p in [cfg["stdout"], cfg["stderr"], cfg["launch_record"], cfg["samples"]] + [o["path"] for o in cfg["outputs"]]:
        pk = probe(p)
        own[p] = pk
        a = arts.get(p, "MISSING")
        if p.endswith("child-out.json") and "child-out.json" in late:
            ok_art = ok_art and a is None
            continue
        if pk[0] == "PRESENT":
            ok_art = ok_art and isinstance(a, dict) and a.get("sha256") == pk[2] and a.get("bytes") == len(pk[1])
        else:
            ok_art = ok_art and a is None
    C["artifacts_match_own_reads"] = ok_art
    ok_ev = True
    for p, h in ev.items():
        pk = own.get(p) or probe(p)
        if p == cfg["launch_record"] and name == "mutate_evidence":
            ok_ev = ok_ev and pk[0] == "PRESENT" and pk[1][-1:] == b"x" and hashlib.sha256(pk[1][:-1]).hexdigest() == h
        elif name in ("escape_slow", "escape_fast", "ignore", "identity") and p in (cfg["stdout"], cfg["stderr"]):
            ok_ev = False
        else:
            ok_ev = ok_ev and pk[0] == "PRESENT" and pk[2] == h
    C["evidence_digests_own"] = ok_ev and cfg["launch_record"] in ev and cfg["samples"] in ev
    sraw = own[cfg["samples"]][1] if own[cfg["samples"]][0] == "PRESENT" else b""
    samples = [jload(x.encode("utf-8")) for x in sraw.decode("utf-8").split("\n") if x.strip()]
    mono_ok, last, bmax, rmax = True, None, 0, 0
    for s in samples:
        c = s.get("census")
        mono_ok = mono_ok and isinstance(c, dict) and isint(c.get("lane_busy"), 0) and c["lane_busy"] <= 2 and \
            isint(c.get("lane_rss"), 0) and isfin(s.get("mono")) and (last is None or s["mono"] > last)
        if isinstance(c, dict) and isint(c.get("lane_busy"), 0) and isint(c.get("lane_rss"), 0):
            bmax, rmax = max(bmax, c["lane_busy"]), max(rmax, c["lane_rss"])
        last = s.get("mono") if isfin(s.get("mono")) else last
    mx = rc_.get("max") or {}
    C["samples_complete"] = bool(samples) and len(samples) == rc_.get("samples_written") and \
        len(sraw) == rc_.get("samples_bytes") and mono_ok and mx.get("lane_busy") == bmax and mx.get("lane_rss") == rmax
    fc = rc_.get("final_census") or {}
    stdout_raw = own[cfg["stdout"]][1] if own[cfg["stdout"]][0] == "PRESENT" else b""
    co = own[cfg["outputs"][0]["path"]]
    child_out = jload(co[1]) if co[0] == "PRESENT" and "child-out.json" not in late else None
    if name in ("ok", "rc_nonzero", "zombie_hold", "mutate_pin", "mutate_evidence", "stray_file", "escape_slow",
                "escape_fast", "double_fork_escape"):
        C["child_output_identity"] = isinstance(child_out, dict) and child_out.get("pid") == ident.get("pid") and \
            child_out.get("mode") == SC[name][0]
    if name == "ok":
        C["stdout_exact"] = stdout_raw == b"line 1\nline 2\nline 3\n"
    if name == "mutate_pin":
        C["fixture_mutated_once"] = need(os.path.join(run, "pinned-scratch.txt"), 1 << 20)[1] == FIXTURE + b"x"
    if name == "stray_file":
        C["stray_content"] = need(os.path.join(od, "stray.txt"), 1 << 20)[1] == b"undeclared file\n"
    if name in ("deadline", "flood", "busy", "rss"):
        trip = (rc_.get("trips") or [{}])[0]
        C["latency_signal_to_post_publish_le_7s"] = isfin(sig.get("mono_sent")) and \
            0 <= summ["post_publish_mono"] - sig["mono_sent"] <= 7.0
        C["latency_trip_to_post_publish_le_7s"] = isfin(trip.get("mono")) and \
            0 <= summ["post_publish_mono"] - trip["mono"] <= 7.0
        C["final_census_clear"] = fc.get("blocking_live") == [] and fc.get("complete") is True
    if name == "deadline":
        dt = rc_.get("deadline_timeliness") or {}
        trip = rc_["trips"][0]
        C["deadline_timing"] = isfin(rc_.get("mono_spawn")) and trip["mono"] >= rc_["mono_spawn"] + cfg["max_wall_s"] and \
            isfin(dt.get("bound_epoch")) and abs(dt["bound_epoch"] - (rc_["abs_end_epoch"] + cfg["sample_s"] + 5.0)) <= 1e-6 \
            and trip["epoch"] <= dt["bound_epoch"]
    if name == "flood":
        so = (rc_.get("streams") or {}).get("stdout") or {}
        C["flood_overflow_proved"] = so.get("overflow") is True and so.get("bytes_written") == 1048576 and \
            isint(so.get("bytes_seen")) and so["bytes_seen"] > 1048576 and len(stdout_raw) == 1048576 and \
            hashlib.sha256(stdout_raw).hexdigest() == so.get("sha256_written")
    if name == "busy":
        ids = ids_from_stdout(stdout_raw).get("busy_pids")
        trip = rc_["trips"][0]
        C["busy_identities_proved"] = isinstance(ids, list) and len(ids) == 2 and ids[0] == ident.get("pid") and \
            any(isinstance(s.get("census"), dict) and s["census"].get("lane_busy") == 2 and
                set(ids) <= set(s["census"].get("lane_busy_pids") or []) for s in samples) and \
            isinstance(trip.get("detail"), list) and trip["detail"][0] == 2 and set(ids) <= set(trip["detail"][1])
    if name == "rss":
        trip = rc_["trips"][0]
        C["rss_crossing_proved"] = ids_from_stdout(stdout_raw).get("rss_pid") == ident.get("pid") and \
            isint(trip.get("detail")) and trip["detail"] > cfg["rss_trip_bytes"] and \
            any(isinstance(s.get("census"), dict) and s["census"].get("lane_rss") == trip["detail"] for s in samples)
    if name == "zombie_hold":
        z = (child_out or {}).get("zombie")
        C["zombie_identity_proved"] = isint(z, 1) and any(isinstance(s.get("census"), dict) and
                                                          z in (s["census"].get("blocking_zombies") or [])
                                                          for s in samples) and fc.get("blocking_live") == []
    if name in ("escape_slow", "escape_fast", "double_fork_escape"):
        g = (child_out or {}).get("grandchild")
        C["escape_identity_proved"] = isint(g, 1) and fc.get("blocking_live") == [g] and fc.get("complete") is True
    if name in ("ignore", "identity"):
        C["blocking_is_child"] = fc.get("blocking_live") == [ident.get("pid")] and fc.get("complete") is True
    res["verdict"] = "PASS" if all(C.values()) else "FAIL"
    return res


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in EXPECT:
        sys.stderr.write("usage: guard_qual_check_v5.py SCENARIO\n")
        return 2
    name = sys.argv[1]
    try:
        res = check(name)
    except (Bad, OSError, ValueError, KeyError, TypeError, AttributeError, IndexError, UnicodeDecodeError) as ex:
        res = {"checker": VERSION, "scenario": name, "verdict": "FAIL", "criteria": {}, "notes": ["%r" % ex]}
    outp = os.path.join(QROOT, name, "check.json")
    data = (json.dumps(res, indent=1, sort_keys=True, allow_nan=False, default=repr) + "\n").encode("utf-8")
    fd = os.open(outp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        view = memoryview(data)
        while view:
            k = os.write(fd, view)
            if k <= 0:
                raise OSError("zero-progress write")
            view = view[k:]
        os.fsync(fd)
    finally:
        os.close(fd)
    print(json.dumps({"scenario": name, "verdict": res["verdict"],
                      "failed": sorted(k for k, v in res.get("criteria", {}).items() if not v)}))
    return 0 if res["verdict"] == "PASS" else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as ex:
        sys.stderr.write("CHECKER_ERROR %r\n" % ex)
        sys.exit(2)
