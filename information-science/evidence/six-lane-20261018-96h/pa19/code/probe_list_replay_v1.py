#!/usr/bin/env python3
"""PA19 96h lane probe 7: independent-lane replay of the frozen M2 first-P1 placement lists for the
pilot cases ms09 b5 and b70 (bridge residual F-C 'post-R6 M2 lists producer-only', at case scope).

The frozen output-I/O-only generator extend_b_x.py (SHA 9862d9eb..., AST-identical to extend_b.py
31924ed6... apart from the output open mode) is vendored by exclusive byte copy into LANE/code/vendor
and run with the SAME absolute skeleton path argument as the original run, writing new exclusive
outputs under LANE/evidence/probes/list-replay-v1/.  The replayed bytes are compared with the old
ext.json bytes and SHA pins.  Standard library only; children: /bin/date and the vendored generator
(pure Python, run with -B and lane TMPDIR).  Admission as the other probes; self budget 280 s.
"""
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
GEN_OLD = (OLD + "/src/extend_b_x.py", "9862d9eb3541cc6a50ee3959cf4e1b909e8afe2b6d448875ddc0f394b07a14fb")
GEN_LANE = LANE + "/code/vendor/extend_b_x.py"
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
CASES = [(5, OLD + "/cycle2/m2part_drat/ms09_b00005/ext.json", "3f71e620c9efa7b3075f8579e357e5096f91282cf6434120706391bb8909fb00"),
         (70, OLD + "/cycle2/m2part_drat/ms09_b00070/ext.json", "c91d656a6c62426752fc6b9683bd8d491031d75bfdb9d3940055ddd22b536c10")]
PY = "/opt/homebrew/bin/python3"
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
T0 = time.monotonic()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def pinned(path, h):
    if not stat.S_ISREG(os.lstat(path).st_mode):
        raise SystemExit("REFUSED: not a regular file " + path)
    raw = open(path, "rb").read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED: pin mismatch " + path)
    return raw


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(LANE + "/evidence/probes/"):
        raise SystemExit("REFUSED: output outside probes")
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    gen_raw = pinned(*GEN_OLD)
    pinned(*SKEL)
    if not os.path.lexists(GEN_LANE):
        with open(GEN_LANE, "xb") as f:
            f.write(gen_raw)
    if hashlib.sha256(open(GEN_LANE, "rb").read()).hexdigest() != GEN_OLD[1] \
            or os.lstat(GEN_LANE).st_ino == os.lstat(GEN_OLD[0]).st_ino:
        raise SystemExit("REFUSED: vendored generator mismatch or shared inode")
    outdir = LANE + "/evidence/probes/list-replay-v1"
    os.mkdir(outdir)
    env = dict(os.environ, TMPDIR=LANE + "/tmp", PYTHONDONTWRITEBYTECODE="1")
    results = []
    for b, old_path, old_sha in CASES:
        if time.monotonic() - T0 > 240:
            raise SystemExit("REFUSED: self budget")
        old_raw = pinned(old_path, old_sha)
        new_path = os.path.join(outdir, "ms09_b%05d.ext.json" % b)
        t1 = time.monotonic()
        p = subprocess.run([PY, "-B", GEN_LANE, SKEL[0], str(b), new_path], capture_output=True, text=True,
                           cwd=LANE + "/tmp", env=env, stdin=subprocess.DEVNULL)
        dt = time.monotonic() - t1
        new_raw = open(new_path, "rb").read() if os.path.exists(new_path) else b""
        nj, oj = (json.loads(new_raw) if new_raw else None), json.loads(old_raw)
        results.append({"b_index": b, "returncode": p.returncode, "stdout": p.stdout[-400:], "stderr": p.stderr[-400:],
                        "seconds": round(dt, 3), "new_path": new_path,
                        "new_sha256": hashlib.sha256(new_raw).hexdigest(), "new_bytes": len(new_raw),
                        "old_path": old_path, "old_sha256": old_sha, "old_bytes": len(old_raw),
                        "byte_identical": new_raw == old_raw,
                        "same_except_source": (nj is not None and {k: v for k, v in nj.items() if k != "source"}
                                               == {k: v for k, v in oj.items() if k != "source"}),
                        "num_placements": None if nj is None else nj.get("num_placements")})
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-LIST-REPLAY-v1", "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3),
           "probe_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "generator": {"old": GEN_OLD, "lane_copy": GEN_LANE}, "skeleton": SKEL, "python": PY, "results": results,
           "scope": "reproducibility of the exact pilot-case lists by the same frozen algorithm in an independent "
                    "run; NOT an independent algorithm and not a completeness proof (that is bridge B5)"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), [(r["b_index"], r["byte_identical"]) for r in results])


if __name__ == "__main__":
    main()
