#!/usr/bin/env python3
"""Sequential, single-solver exploratory screen of the frozen K3 cubes.

Only patterns are searched. SAT is not a quantum witness; UNKNOWN is not UNSAT.
Usage: k3_screen_r2.py A|B OUTDIR [--seconds 1800] [--cubes C311 ...]
       [--input-dir DIR] (defaults to explore/k3cubes).
"""
import argparse
import json
import os
import subprocess
import time

from gram_certify_r4 import now, rss, sha

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("encoder", choices=("A", "B"))
    ap.add_argument("outdir")
    ap.add_argument("--seconds", type=int, default=1800)
    ap.add_argument("--input-dir", default=os.path.join(LANE, "explore", "k3cubes"))
    ap.add_argument("--cubes", nargs="+", choices=("C311", "C321", "C411"),
                    default=("C311", "C321", "C411"))
    a = ap.parse_args()
    if not 1 <= a.seconds <= 1800:
        raise ValueError("Frozen screen cap is at most 1800 seconds")
    os.makedirs(a.outdir, exist_ok=True)
    if not rss(os.getpid()):
        raise RuntimeError("Native RSS sampler unavailable")
    for cube in a.cubes:
        label = a.encoder + "_" + cube
        cnf = os.path.join(a.input_dir, label + ".cnf")
        meta = cnf[:-4] + ".meta.json"
        with open(meta) as f:
            binding = json.load(f)
        assert sha(cnf) == binding["cnf_sha256"]
        receipt = os.path.join(a.outdir, label + ".json")
        log = os.path.join(a.outdir, label + ".solver.log")
        if os.path.exists(receipt) or os.path.exists(log):
            raise FileExistsError(label)
        command = (["cadical", "-q", "-t", str(a.seconds), cnf] if a.encoder == "A"
                   else ["kissat", "-q", "--time=%d" % a.seconds, cnf])
        start, t0 = now(), time.monotonic()
        peak, reason = 0, None
        with open(log, "x") as f:
            child = subprocess.Popen(command, stdout=f, stderr=subprocess.STDOUT)
            while child.poll() is None:
                current = rss(os.getpid()) + rss(child.pid)
                peak = max(peak, current)
                st = os.statvfs(LANE)
                if current > 3584 * 1024 * 1024:
                    reason = "RSS safety threshold"
                elif st.f_bavail * st.f_frsize < 12000000000:
                    reason = "free-space floor"
                elif time.monotonic() - t0 > a.seconds + 30:
                    reason = "native cap plus grace"
                if reason:
                    child.terminate()
                    stop = time.monotonic() + 30
                    while child.poll() is None:
                        if time.monotonic() >= stop:
                            raise RuntimeError("SIGTERM grace exceeded; no SIGKILL sent")
                        time.sleep(0.1)
                    break
                time.sleep(0.25)
        status = {10: "SAT pattern", 20: "UNSAT exploratory"}.get(child.returncode, "UNKNOWN")
        if reason:
            status = "UNKNOWN safety stop"
        rec = {"encoder": a.encoder, "cube": cube, "status": status, "started_at": start,
               "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
               "solver_command": command, "solver_rc": child.returncode,
               "cnf_sha256": binding["cnf_sha256"], "metadata_sha256": sha(meta),
               "input_directory": os.path.abspath(a.input_dir),
               "screen_driver_sha256": sha(__file__), "solver_log_sha256": sha(log),
               "peak_sampled_aggregate_rss_bytes": peak, "safety_stop_reason": reason,
               "claim_scope": "support patterns only; no UNSAT certificate or quantum witness"}
        with open(receipt, "x") as f:
            json.dump(rec, f, indent=2)
            f.write("\n")
        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
