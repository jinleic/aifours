#!/usr/bin/env python3
"""Parent producer reproduction for the two pinned CFR(5,27) candidates (owner Cfr27ParentReproduce, v1).

Usage (always python3 -B):
  reproduce_producer_v1.py pin
  reproduce_producer_v1.py build savetemps|twostep
  reproduce_producer_v1.py replay BUILD TAG          (BUILD = savetemps|twostep; writes replay-TAG/)
  reproduce_producer_v1.py model-recompile

Rules implemented here: every directory/file is created exclusively (os.mkdir without exist_ok, open mode 'x');
lane bytes are copied only after SHA-256 verification against the frozen hashes; every child gets TMPDIR set to a
fresh directory inside this folder; children are reaped with os.wait4 polling, SIGTERM at the deadline (or on an
RSS > 2 GiB / free-disk < 12e9 B guard trip) followed by a bounded wait -- never SIGKILL; a child that outlives the
bounded wait is UNKNOWN. The native producer gets SECONDS=180 (the worker used 10800) and a fresh output prefix whose
.dmraw path is preflighted absent. Raw-output byte identity with the parent pins is the success criterion; the
binary hash comparison with the worker binary is informational.
"""
import hashlib
import json
import os
import re
import signal
import struct
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
ROOT = REVIEW.parents[3]
LANE = ROOT / "information-science/evidence/six-lane-20261016/cfr33"
PARENT_INPUTS = REVIEW / "cfr27-parent-inputs-v1"
PIN = HERE / "inputs"

FREE_FLOOR = 12_000_000_000
RSS_CAP = 2 * 1024 ** 3
NATIVE_SECONDS = "180"
WORKER_SECONDS = "10800"
WALL_GRACE = 30.0
TERM_WAIT = 30.0

SRC_SHA = "8aea035d4b99123e705ef9eaaff3d1e7a49f1225c25488cb9dfdf204de246ea8"
WORKER_BIN_SHA = "b9ab685625436c942ee8a2214f321453d7ab01b131049664b2d707f7aa572158"
FREEZE_SHA = "c24cb110443749d14e2d0746d48d54179baaab12628bd7fb807aebb5db6a73f5"

# (pinned relative path, lane source, frozen sha256)
PINS = [
    ("freeze-v1.json", LANE / "cfr27/candidates-v2/freeze-v1.json", FREEZE_SHA),
    ("code/dmorbit_xc_v1.c", LANE / "code/dmorbit_xc_v1.c", SRC_SHA),
    ("code/dm_to_cfr.py", LANE / "code/dm_to_cfr.py", "d9ff9b9c18314d21664226bccf8d57ab91d6d6d15232b3ac98a7affeac30d12a"),
    ("code/dmorbit_compile_v1.py", LANE / "code/dmorbit_compile_v1.py",
     "7e62129860420a05359b8a1b0a2768847e1f93972dffd98cf5b9612d1a4e502c"),
    ("specs/T10.spec.json", LANE / "cfr27/dmorbit-v1/specs/T10.spec.json",
     "1378292cf8a156e7c14cc114cd91bb4feac5364aa791eb7b4dd5042c7aae2178"),
    ("specs/T10.model", LANE / "cfr27/dmorbit-v1/specs/T10.model",
     "b9233e7ed7a1833c4f377ebad0419ed0a77368198cd0f826a1e6babb27582abc"),
    ("specs/S3a.spec.json", LANE / "cfr27/dmorbit-v1/specs/S3a.spec.json",
     "808e3dfff2dbf199b36b8881e61150221c57291c131dcb223fb3b1759605b622"),
    ("specs/S3a.model", LANE / "cfr27/dmorbit-v1/specs/S3a.model",
     "6540d72cb28d245a37702694cc89a53da86a3dbfc51056e01e9d374694962e7a"),
    ("worker/T10-zero-first.out", LANE / "cfr27/dmorbit-v1/runs-xc/sweep-v1/T10-zero-first.out",
     "e319b8eaa448c27f7c640d454e2f12fc3af5d3d4b8253227513982e61fe488f3"),
    ("worker/S3a-nozero-first.out", LANE / "cfr27/dmorbit-v1/runs-xc/sweep-v1/S3a-nozero-first.out",
     "db345baebdd53ee260e52290275223d6510b2a50ea4d32e6c278796f99110330"),
    ("worker/T10-zero-first.dmraw", LANE / "cfr27/dmorbit-v1/runs-xc/T10-zero-first.dmraw",
     "b8eec25f6d575aecfce12933a067b582774dd1be8738604797d5c76169c6c65c"),
    ("worker/S3a-nozero-first.dmraw", LANE / "cfr27/dmorbit-v1/runs-xc/S3a-nozero-first.dmraw",
     "3f45f8c33d4f2379a154dd4d6bb21da6ef40beb50b7548d56ee3bf799357b664"),
    ("worker/dmorbit_xc_v1.worker-binary.noexec", LANE / "bin/dmorbit_xc_v1", WORKER_BIN_SHA),
]
PARENT_PINS = {
    "A-DM.raw": "b8eec25f6d575aecfce12933a067b582774dd1be8738604797d5c76169c6c65c",
    "A-CFR.raw": "6ceed793b3cd733461b8bec06091c282e300b1f1feeef9c95cf6d1c679588c7a",
    "B-DM.raw": "3f45f8c33d4f2379a154dd4d6bb21da6ef40beb50b7548d56ee3bf799357b664",
    "B-CFR.raw": "a9faf3dd0d2c2bbff53499d869ed00eeeb7b876abbb75c294680b10969b35f0a",
    "manifest.json": "011627dccd70ae49f8810a9f10594607f779a390f61bca3823ada93e179198ee",
}
CASES = [  # name, model, mode, parent DM pin, parent CFR pin, worker stdout, worker dmraw
    ("T10-zero-first", "T10.model", "zero", "A-DM.raw", "A-CFR.raw", "worker/T10-zero-first.out",
     "worker/T10-zero-first.dmraw"),
    ("S3a-nozero-first", "S3a.model", "nozero", "B-DM.raw", "B-CFR.raw", "worker/S3a-nozero-first.out",
     "worker/S3a-nozero-first.dmraw"),
]
FROZEN_FLAGS = ["-O2", "-march=native", "-Wall", "-Wextra"]


def now():
    return datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d %H:%M:%S %Z")


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    return sha_bytes(Path(p).read_bytes())


def rel(p):
    p = Path(p)
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def require(ok, why):
    if not ok:
        raise RuntimeError(why)


def write_x(path, data):
    with open(path, "xb") as fh:
        fh.write(data)


def write_json_x(path, obj):
    write_x(path, (json.dumps(obj, indent=1) + "\n").encode())


def free_bytes():
    st = os.statvfs(HERE)
    return st.f_bavail * st.f_frsize


def check_free():
    f = free_bytes()
    require(f >= FREE_FLOOR, "free disk %d B below floor %d B" % (f, FREE_FLOOR))
    return f


def rss_of(pid):
    out = subprocess.run(["ps", "-o", "rss=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return int(out) * 1024 if out.isdigit() else None


def reap(p, deadline):
    """os.wait4 polling (exact child rusage); SIGTERM at deadline or guard trip; bounded wait; never SIGKILL."""
    termed, trip, peak, last = None, None, 0, 0.0
    while True:
        pid, status, ru = os.wait4(p.pid, os.WNOHANG)
        if pid == p.pid:
            p.returncode = os.waitstatus_to_exitcode(status)
            return {"rc": p.returncode, "ru_maxrss_bytes": ru.ru_maxrss, "user_s": round(ru.ru_utime, 3),
                    "sys_s": round(ru.ru_stime, 3), "sampled_peak_rss_bytes": peak, "sigterm_sent": termed is not None,
                    "guard_trip": trip, "status": "EXITED"}
        t = time.monotonic()
        if t - last >= 0.5:
            last = t
            r = rss_of(p.pid)
            if r:
                peak = max(peak, r)
                if r > RSS_CAP and trip is None:
                    trip = "rss %d B > cap %d B" % (r, RSS_CAP)
            fb = free_bytes()
            if fb < FREE_FLOOR and trip is None:
                trip = "free disk %d B < floor %d B" % (fb, FREE_FLOOR)
        if termed is None and (t > deadline or trip):
            p.send_signal(signal.SIGTERM)
            termed = t
        elif termed is not None and t - termed > TERM_WAIT:
            return {"rc": None, "status": "UNKNOWN", "survived_sigterm": True, "sigterm_sent": True,
                    "guard_trip": trip, "sampled_peak_rss_bytes": peak}
        time.sleep(0.02)


def run_child(argv, cwd, env_over, out_path, err_path, deadline_s):
    require(not out_path.exists() and not err_path.exists(), "log path exists")
    env = dict(os.environ, **env_over)
    start_pt, t0 = now(), time.monotonic()
    with open(out_path, "xb") as so, open(err_path, "xb") as se:
        p = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL, stdout=so, stderr=se)
        rec = reap(p, t0 + deadline_s)
    rec.update({"argv": [str(a) for a in argv], "cwd": rel(cwd), "env_overrides": env_over,
                "host_time_start": start_pt, "host_time_end": now(), "wall_s": round(time.monotonic() - t0, 3),
                "deadline_s": deadline_s, "stdout": rel(out_path), "stdout_sha256": sha_file(out_path),
                "stderr": rel(err_path), "stderr_sha256": sha_file(err_path),
                "stderr_bytes": out_size(err_path)})
    return rec


def out_size(p):
    return Path(p).stat().st_size


def inventory(base):
    files = []
    for p in sorted(base.rglob("*")):
        if p.is_file():
            st = p.stat()
            files.append({"path": str(p.relative_to(base)), "bytes": st.st_size, "mode": oct(st.st_mode & 0o7777),
                          "sha256": sha_file(p)})
    return files


def pinned_copy(src_rel, dest):
    src = PIN / src_rel
    data = src.read_bytes()
    want = dict((r, s) for r, _, s in PINS)[src_rel]
    require(sha_bytes(data) == want, "pinned copy hash changed: " + src_rel)
    write_x(dest, data)
    require(sha_file(dest) == want, "copy hash mismatch " + str(dest))


def xcrun_db_state():
    d = subprocess.run(["getconf", "DARWIN_USER_TEMP_DIR"], capture_output=True, text=True).stdout.strip()
    p = Path(d) / "xcrun_db"
    if not p.exists():
        return {"path": str(p), "exists": False}
    st = p.stat()
    return {"path": str(p), "exists": True, "bytes": st.st_size, "mtime_ns": st.st_mtime_ns}


# ------------------------------------------------------------------ Mach-O diff classification (informational)
def macho_regions(data):
    magic, cpu, sub, ftype, ncmds, sizeofcmds, flags, _ = struct.unpack_from("<IiiIIIII", data, 0)
    require(magic == 0xFEEDFACF, "not a 64-bit little-endian Mach-O")
    regions, off = [("mach_header", 0, 32), ("load_commands", 32, 32 + sizeofcmds)], 32
    info = {"ncmds": ncmds, "sizeofcmds": sizeofcmds, "uuid": None, "sections": []}
    for _ in range(ncmds):
        cmd, size = struct.unpack_from("<II", data, off)
        if cmd == 0x19:  # LC_SEGMENT_64
            seg = data[off + 8:off + 24].rstrip(b"\0").decode()
            fileoff, filesize = struct.unpack_from("<QQ", data, off + 40)
            nsects = struct.unpack_from("<I", data, off + 64)[0]
            regions.append(("segment " + seg, fileoff, fileoff + filesize))
            so = off + 72
            for _s in range(nsects):
                sect = data[so:so + 16].rstrip(b"\0").decode()
                ssize = struct.unpack_from("<Q", data, so + 40)[0]
                sofs = struct.unpack_from("<I", data, so + 48)[0]
                info["sections"].append({"name": seg + "," + sect, "offset": sofs, "size": ssize})
                if sofs:
                    regions.append(("section " + seg + "," + sect, sofs, sofs + ssize))
                so += 80
        elif cmd == 0x1B:  # LC_UUID
            info["uuid"] = data[off + 8:off + 24].hex()
            regions.append(("LC_UUID payload", off + 8, off + 24))
        elif cmd == 0x1D:  # LC_CODE_SIGNATURE
            dataoff, datasize = struct.unpack_from("<II", data, off + 8)
            regions.append(("code_signature", dataoff, dataoff + datasize))
        off += size
    return regions, info


def macho_diff(a, b):
    ra, ia = macho_regions(a)
    _, ib = macho_regions(b)
    out = {"bytes_a": len(a), "bytes_b": len(b), "uuid_a": ia["uuid"], "uuid_b": ib["uuid"],
           "sections_equal_layout": ia["sections"] == ib["sections"]}
    if len(a) != len(b):
        out["note"] = "sizes differ; no offset-wise classification"
        return out
    counts = {}
    for i in range(len(a)):
        if a[i] != b[i]:
            # most specific region containing i (smallest span)
            hits = [r for r in ra if r[1] <= i < r[2]]
            name = min(hits, key=lambda r: r[2] - r[1])[0] if hits else "unmapped"
            counts[name] = counts.get(name, 0) + 1
    out["differing_bytes_by_region"] = counts
    sec = {}
    for s in ia["sections"]:
        if s["offset"]:
            sec[s["name"]] = a[s["offset"]:s["offset"] + s["size"]] == b[s["offset"]:s["offset"] + s["size"]]
    out["section_bytes_equal"] = sec
    return out


# ------------------------------------------------------------------ stages
def stage_pin():
    check_free()
    os.mkdir(PIN)
    for sub in ("code", "specs", "worker", "tmp"):
        os.mkdir(PIN / sub)
    res = {"stage": "pin", "host_time_start": now(), "driver": rel(__file__), "driver_sha256": sha_file(__file__),
           "free_bytes_start": free_bytes(), "pins": [], "parent_pins_in_place": {}}
    for r, src, want in PINS:
        data = src.read_bytes()
        got = sha_bytes(data)
        require(got == want, "lane file hash mismatch %s: %s != %s" % (src, got, want))
        write_x(PIN / r, data)
        require(sha_file(PIN / r) == want, "pinned copy mismatch " + r)
        res["pins"].append({"pinned": rel(PIN / r), "source": rel(src), "sha256": want, "bytes": len(data)})
    for name, want in PARENT_PINS.items():
        got = sha_file(PARENT_INPUTS / name)
        require(got == want, "parent pin changed " + name)
        res["parent_pins_in_place"][rel(PARENT_INPUTS / name)] = got
    # worker dmraws are byte-identical to the parent DM pins
    for name, _, _, pdm, _, _, wdm in CASES:
        require((PIN / wdm).read_bytes() == (PARENT_INPUTS / pdm).read_bytes(), "worker dmraw != parent pin " + name)
    # freeze-internal hash claims vs frozen constants
    fz = json.loads((PIN / "freeze-v1.json").read_bytes())
    pin_sha = dict((r, s) for r, _, s in PINS)
    checks = {
        "producer.source_sha256": fz["producer"]["source_sha256"] == SRC_SHA,
        "producer.binary_sha256": fz["producer"]["binary_sha256"] == WORKER_BIN_SHA,
        "producer.compile_command": fz["producer"]["compile_command"] ==
        "cc -O2 -march=native -Wall -Wextra -o bin/dmorbit_xc_v1 code/dmorbit_xc_v1.c (cwd cfr33/)",
        "model_compiler.sha256": fz["model_compiler"]["sha256"] == pin_sha["code/dmorbit_compile_v1.py"],
        "expander.dm_to_cfr_sha256": fz["expander"]["dm_to_cfr_sha256"] == pin_sha["code/dm_to_cfr.py"],
    }
    want_groups = {"T10-zero-first": [[10, [1, 2, 3, 4, 5, 0]]],
                   "S3a-nozero-first": [[1, [1, 2, 0, 4, 5, 3]], [1, [3, 5, 4, 0, 2, 1]]]}
    for c in fz["candidates"]:
        nm = c["name"]
        case = [x for x in CASES if x[0] == nm][0]
        tag = nm.split("-")[0]
        checks[nm + ".group"] = c["group"] == want_groups[nm]
        checks[nm + ".mode"] = c["mode"] == case[2]
        checks[nm + ".spec_sha256"] = c["spec_sha256"] == pin_sha["specs/%s.spec.json" % tag]
        checks[nm + ".model_sha256"] = c["model_sha256"] == pin_sha["specs/%s.model" % tag]
        checks[nm + ".dm_raw_sha256==parent"] = c["dm_raw_sha256"] == PARENT_PINS[case[3]]
        checks[nm + ".cfr_raw_sha256==parent"] = c["cfr_raw_sha256"] == PARENT_PINS[case[4]]
        checks[nm + ".stdout_sha256"] = c["stdout_sha256"] == pin_sha[case[5]]
        checks[nm + ".command_args"] = c["command"][2:5] == [WORKER_SECONDS, case[2], "first"]
        spec = json.loads((PIN / ("specs/%s.spec.json" % tag)).read_bytes())
        checks[nm + ".spec_gens==freeze_group"] = spec["gens"] == c["group"]
    res["freeze_consistency"] = checks
    require(all(checks.values()), "freeze consistency failure: %s" % [k for k, v in checks.items() if not v])
    # toolchain provenance (children get TMPDIR inside this folder)
    env = {"TMPDIR": str(PIN / "tmp") + "/"}
    tools = {}
    for name, argv in [("cc_version", ["cc", "--version"]), ("xcrun_find_clang", ["xcrun", "--find", "clang"]),
                       ("ld_version", ["ld", "-v"]), ("sw_vers", ["sw_vers"]), ("uname", ["uname", "-a"])]:
        tools[name] = run_child(argv, PIN, env, PIN / (name + ".stdout.txt"), PIN / (name + ".stderr.txt"), 60)
        tools[name]["stdout_text"] = (PIN / (name + ".stdout.txt")).read_text()
        tools[name]["stderr_text"] = (PIN / (name + ".stderr.txt")).read_text()
    clang = (PIN / "xcrun_find_clang.stdout.txt").read_text().strip()
    tools["sha256"] = {"/usr/bin/cc": sha_file("/usr/bin/cc"), clang: sha_file(clang)}
    res["toolchain"] = tools
    res["python"] = {"executable": sys.executable, "version": sys.version, "dont_write_bytecode": sys.dont_write_bytecode}
    res["host_time_end"] = now()
    res["status"] = "PINNED"
    write_json_x(PIN / "pin-result.json", res)
    print(json.dumps({"stage": "pin", "status": res["status"], "pins": len(res["pins"])}))


def stage_build(mode):
    require(mode in ("savetemps", "twostep"), "mode")
    check_free()
    B = HERE / ("build-" + mode)
    os.mkdir(B)
    for sub in ("code", "bin", "tmp") + (("obj",) if mode == "twostep" else ()):
        os.mkdir(B / sub)
    pinned_copy("code/dmorbit_xc_v1.c", B / "code/dmorbit_xc_v1.c")
    env = {"TMPDIR": str(B / "tmp") + "/"}
    res = {"stage": "build-" + mode, "host_time_start": now(), "driver_sha256": sha_file(__file__),
           "source_sha256": sha_file(B / "code/dmorbit_xc_v1.c"), "xcrun_db_before": xcrun_db_state(),
           "worker_compile_command": "cc -O2 -march=native -Wall -Wextra -o bin/dmorbit_xc_v1 code/dmorbit_xc_v1.c"
                                     " (cwd cfr33/)", "steps": []}
    if mode == "savetemps":
        res["difference_from_worker"] = ("adds -save-temps=obj (retains .i/.bc/.s/.o next to the output) and "
                                         "TMPDIR=<this build>/tmp/; cwd is this build dir with the same relative "
                                         "layout code/ and bin/")
        argvs = [("compile_link", ["cc"] + FROZEN_FLAGS + ["-save-temps=obj", "-o", "bin/dmorbit_xc_v1",
                                                           "code/dmorbit_xc_v1.c"])]
    else:
        res["difference_from_worker"] = ("same flags split into compile (-c -o obj/dmorbit_xc_v1.o) and link "
                                         "(-o bin/dmorbit_xc_v1 obj/dmorbit_xc_v1.o) so the object is retained without "
                                         "a compiler-deleted temporary; TMPDIR=<this build>/tmp/")
        argvs = [("compile", ["cc"] + FROZEN_FLAGS + ["-c", "-o", "obj/dmorbit_xc_v1.o", "code/dmorbit_xc_v1.c"]),
                 ("link", ["cc"] + FROZEN_FLAGS + ["-o", "bin/dmorbit_xc_v1", "obj/dmorbit_xc_v1.o"])]
    ok = True
    for name, argv in argvs:
        rec = run_child(argv, B, env, B / (name + ".stdout.txt"), B / (name + ".stderr.txt"), 300)
        rec["stderr_text"] = (B / (name + ".stderr.txt")).read_text()
        res["steps"].append(rec)
        if rec.get("rc") != 0:
            ok = False
            break
    res["xcrun_db_after"] = xcrun_db_state()
    binp = B / "bin/dmorbit_xc_v1"
    if ok and binp.exists():
        data = binp.read_bytes()
        res["binary"] = {"path": rel(binp), "sha256": sha_bytes(data), "bytes": len(data)}
        worker = (PIN / "worker/dmorbit_xc_v1.worker-binary.noexec").read_bytes()
        res["binary"]["equals_worker_binary"] = data == worker
        res["binary"]["worker_binary_sha256"] = sha_bytes(worker)
        res["binary"]["macho_comparison_vs_worker"] = macho_diff(data, worker)
        cs = run_child(["codesign", "-dvv", str(binp)], B, env, B / "codesign.stdout.txt", B / "codesign.stderr.txt", 60)
        cs["stderr_text"] = (B / "codesign.stderr.txt").read_text()
        res["codesign"] = cs
        res["status"] = "BUILT"
    else:
        res["status"] = "BUILD_FAILED"
    res["inventory_after"] = inventory(B)
    res["host_time_end"] = now()
    write_json_x(B / "build-result.json", res)
    print(json.dumps({"stage": res["stage"], "status": res["status"], "binary": res.get("binary", {}).get("sha256"),
                      "equals_worker": res.get("binary", {}).get("equals_worker_binary")}))


def norm_stdout(text):
    lines, progress = [], 0
    for ln in text.split("\n"):
        if ln.startswith("c progress "):
            progress += 1
            continue
        ln = re.sub(r"limit \d+", "limit <L>", ln)
        ln = re.sub(r"\bt \d+\.\d+", "t <T>", ln)
        if ln.startswith("c wrote "):
            ln = "c wrote <PATH>"
        lines.append(ln)
    return lines, progress


def vlines(text):
    out = []
    for ln in text.split("\n"):
        m = re.fullmatch(r"v orbit size (\d+) base((?: \d+)+)", ln)
        if m:
            out.append({"size": int(m.group(1)), "base": [int(x) for x in m.group(2).split()]})
    return out


def stage_replay(build, tag):
    require(build in ("savetemps", "twostep"), "build")
    require(re.fullmatch(r"[a-z0-9]+", tag) is not None, "tag")
    check_free()
    B = HERE / ("build-" + build)
    br = json.loads((B / "build-result.json").read_bytes())
    require(br["status"] == "BUILT", "build not BUILT")
    binp = B / "bin/dmorbit_xc_v1"
    require(sha_file(binp) == br["binary"]["sha256"], "binary changed since build")
    RP = HERE / ("replay-" + tag)
    os.mkdir(RP)
    os.mkdir(RP / "tmp")
    env = {"TMPDIR": str(RP / "tmp") + "/"}
    fz = json.loads((PIN / "freeze-v1.json").read_bytes())
    bases = fz["expander"]["independent_python_reexpansion"]
    res = {"stage": "replay", "tag": tag, "build": build, "host_time_start": now(), "driver_sha256": sha_file(__file__),
           "binary": rel(binp), "binary_sha256": br["binary"]["sha256"],
           "native_seconds_argument": NATIVE_SECONDS, "worker_seconds_argument": WORKER_SECONDS,
           "seconds_disclosure": "native cap 180 s replaces the worker's 10800; the search is deterministic and the "
                                 "worker runs finished in < 10 s, so the cap can only turn a run into UNKNOWN",
           "native_output_mode_note": "dmorbit_xc_v1.c emit() opens OUTPREFIX.dmraw with open(O_WRONLY|O_CREAT|O_EXCL,"
                                      " 0444) per source text; the path was additionally preflighted absent",
           "wall_deadline_s": float(NATIVE_SECONDS) + WALL_GRACE, "term_wait_s": TERM_WAIT, "cases": []}
    all_ok = True
    for name, model, mode, pdm, pcfr, wout, wdm in CASES:
        outprefix = RP / (name + "-parent-" + tag)
        dmraw = Path(str(outprefix) + ".dmraw")
        require(not dmraw.exists(), "output prefix not fresh")
        require(not any(p.name.startswith(outprefix.name) for p in RP.iterdir()), "prefix collision")
        model_path = PIN / "specs" / model
        require(sha_file(model_path) == dict((r, s) for r, _, s in PINS)["specs/" + model], "model changed")
        argv = [str(binp), str(model_path), NATIVE_SECONDS, mode, "first", str(outprefix)]
        rec = run_child(argv, RP, env, RP / (name + ".stdout.txt"), RP / (name + ".stderr.txt"),
                        float(NATIVE_SECONDS) + WALL_GRACE)
        text = (RP / (name + ".stdout.txt")).read_text()
        status_lines = [ln for ln in text.split("\n") if ln.startswith("s ")]
        rec["status_line"] = status_lines[-1] if status_lines else None
        rec["stdout_text"] = text
        c = {"case": name, "model": rel(model_path), "mode": mode, "run": rec}
        if dmraw.exists():
            data = dmraw.read_bytes()
            c["dmraw"] = {"path": rel(dmraw), "sha256": sha_bytes(data), "bytes": len(data),
                          "mode": oct(dmraw.stat().st_mode & 0o7777)}
            c["dmraw_equals_parent_pin"] = data == (PARENT_INPUTS / pdm).read_bytes()
            c["parent_pin"] = {"path": rel(PARENT_INPUTS / pdm), "sha256": PARENT_PINS[pdm]}
            c["dmraw_equals_worker_dmraw"] = data == (PIN / wdm).read_bytes()
        else:
            c["dmraw"] = None
            c["dmraw_equals_parent_pin"] = False
        mine, prog_m = norm_stdout(text)
        theirs, prog_w = norm_stdout((PIN / wout).read_text())
        c["stdout_normalised_equal_worker"] = mine == theirs
        c["stdout_normalisation"] = "limit N -> <L>; 't x.y' -> 't <T>'; 'c wrote PATH' -> '<PATH>'; progress lines dropped"
        c["progress_lines"] = {"parent": prog_m, "worker": prog_w}
        if mine != theirs:
            c["stdout_diff"] = {"parent": mine, "worker": theirs}
        v = vlines(text)
        c["printed_orbits"] = v
        c["printed_bases_equal_freeze"] = [x["base"] for x in v] == bases[name]["bases"]
        ok = (rec.get("rc") == 10 and rec["status_line"] == "s SATISFIABLE" and c["dmraw_equals_parent_pin"]
              and c["printed_bases_equal_freeze"])
        c["verdict"] = "PASS" if ok else ("UNKNOWN" if rec.get("status") == "UNKNOWN" or rec.get("rc") == 0 else "FAIL")
        all_ok = all_ok and ok
        res["cases"].append(c)
    res["inventory_after"] = inventory(RP)
    res["free_bytes_end"] = free_bytes()
    res["host_time_end"] = now()
    res["verdict"] = "PASS_RAW_DM_BYTE_IDENTICAL_BOTH" if all_ok else "NOT_PASS"
    write_json_x(RP / "replay-result.json", res)
    print(json.dumps({"stage": "replay", "tag": tag, "verdict": res["verdict"],
                      "cases": [(c["case"], c["verdict"], c["run"].get("rc"), c["run"]["wall_s"],
                                 c["run"].get("ru_maxrss_bytes")) for c in res["cases"]]}))


def stage_model_recompile():
    check_free()
    MR = HERE / "model-recompile"
    os.mkdir(MR)
    os.mkdir(MR / "tmp")
    env = {"TMPDIR": str(MR / "tmp") + "/", "PYTHONDONTWRITEBYTECODE": "1"}
    pin_sha = dict((r, s) for r, _, s in PINS)
    res = {"stage": "model-recompile", "host_time_start": now(), "driver_sha256": sha_file(__file__),
           "compiler": rel(PIN / "code/dmorbit_compile_v1.py"), "compiler_sha256": sha_file(PIN / "code/dmorbit_compile_v1.py"),
           "cases": []}
    require(res["compiler_sha256"] == pin_sha["code/dmorbit_compile_v1.py"], "compiler changed")
    ok_all = True
    for tag in ("T10", "S3a"):
        out = MR / (tag + ".model")
        argv = [sys.executable, "-B", str(PIN / "code/dmorbit_compile_v1.py"), str(PIN / "specs" / (tag + ".spec.json")),
                str(out)]
        rec = run_child(argv, MR, env, MR / (tag + ".compile.stdout.txt"), MR / (tag + ".compile.stderr.txt"), 120)
        rec["stdout_text"] = (MR / (tag + ".compile.stdout.txt")).read_text()
        c = {"tag": tag, "run": rec}
        if out.exists():
            c["model_sha256"] = sha_file(out)
            c["equals_pinned_model"] = out.read_bytes() == (PIN / "specs" / (tag + ".model")).read_bytes()
        else:
            c["equals_pinned_model"] = False
        ok_all = ok_all and rec.get("rc") == 0 and c["equals_pinned_model"]
        res["cases"].append(c)
    res["inventory_after"] = inventory(MR)
    res["host_time_end"] = now()
    res["verdict"] = "PASS_MODEL_BYTES_IDENTICAL" if ok_all else "NOT_PASS"
    write_json_x(MR / "model-recompile-result.json", res)
    print(json.dumps({"stage": "model-recompile", "verdict": res["verdict"]}))


def main():
    require(sys.dont_write_bytecode, "run with python3 -B")
    a = sys.argv[1:]
    if a == ["pin"]:
        stage_pin()
    elif len(a) == 2 and a[0] == "build":
        stage_build(a[1])
    elif len(a) == 3 and a[0] == "replay":
        stage_replay(a[1], a[2])
    elif a == ["model-recompile"]:
        stage_model_recompile()
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
