#!/usr/bin/env python3
"""Size measurements for proof retention (parent request 2026-10-17 ~13:05). Read-only on existing
files; writes cycle2/retention-measure/ (compressed outputs) and cycle2/retention-measure.json.
  R1 kissat binary DRAT (cycle-1 stored ms01_s00890.drat, 78.7 MB): drat-trim -l core -C (binary
     core lemmas) -> zstd -3; core re-checked by drat-trim (-t limits everywhere).
  R2 CaDiCaL LRAT (cycle-1 stored m2q0b/proof/g000.lrat, 912 MB) through bin/lratstrict2 with
     binary DRAT emission -> zstd -3; emitted DRAT re-checked by drat-trim against m2q0b/cnf/g000.cnf.
Processes: Popen + wait with bounds; SIGTERM only.
"""
import hashlib
import json
import os
import subprocess
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LS2 = os.path.join(LANE, "bin", "lratstrict2")
OUT = os.path.join(LANE, "cycle2", "retention-measure")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def run_bounded(cmd, bound, stdin=None, stdout=subprocess.PIPE):
    p = subprocess.Popen(cmd, stdin=stdin, stdout=stdout, stderr=subprocess.STDOUT)
    try:
        out, _ = p.communicate(timeout=bound)
        return p.returncode, (out or b"").decode(errors="replace"), "self"
    except subprocess.TimeoutExpired:
        p.terminate()
        try:
            out, _ = p.communicate(timeout=60)
            return p.returncode, (out or b"").decode(errors="replace"), "term"
        except subprocess.TimeoutExpired:
            return None, "", "left-running"


def zstd_fifo_to_file(fifo, dst):
    """reader thread: fifo -> zstd -3 -> dst (zstd started before the writer opens the fifo)"""
    z = subprocess.Popen(["/opt/homebrew/bin/zstd", "-q", "-3", "-c"], stdin=subprocess.PIPE, stdout=open(dst, "wb"))
    h, n = hashlib.sha256(), [0]

    def pump():
        with open(fifo, "rb") as f:
            for b in iter(lambda: f.read(1 << 16), b""):
                h.update(b)
                n[0] += len(b)
                z.stdin.write(b)
        z.stdin.close()

    t = threading.Thread(target=pump, daemon=True)
    t.start()
    return z, t, h, n


def main():
    os.makedirs(OUT, exist_ok=True)
    res = {}
    # R1
    cnf = os.path.join(LANE, "cases19skel", "cnf", "ms01_s00890.cnf")
    drat = os.path.join(LANE, "cases19skel", "proof", "ms01_s00890.drat")
    fifo = os.path.join(OUT, "r1_core_%d.fifo" % time.time_ns())
    os.mkfifo(fifo)
    dst = os.path.join(OUT, "r1_ms01_s00890.core.drat.zst")
    z, t, h, n = zstd_fifo_to_file(fifo, dst)
    t0 = time.time()
    rc, out, stop = run_bounded([DT, cnf, drat, "-l", fifo, "-C", "-w", "-t", "1200"], 1300)
    t.join(timeout=120)
    z.wait(timeout=120)
    r1 = {"drat_bytes": os.path.getsize(drat), "check_rc": rc, "check_stop": stop, "check_seconds": round(time.time() - t0, 1),
          "verified": rc == 0 and "s VERIFIED" in out, "core_raw_bytes": n[0], "core_raw_sha256": h.hexdigest(),
          "core_zst_bytes": os.path.getsize(dst), "core_zst_sha256": sha(dst)}
    # re-check the core proof (decompressed through a pipe)
    zd = subprocess.Popen(["/opt/homebrew/bin/zstd", "-q", "-d", "-c", dst], stdout=subprocess.PIPE)
    rc2, out2, stop2 = run_bounded([DT, cnf, "-i", "-w", "-t", "1200"], 1300, stdin=zd.stdout)
    zd.wait(timeout=60)
    r1.update({"core_recheck_rc": rc2, "core_recheck_stop": stop2, "core_recheck_verified": rc2 == 0 and "s VERIFIED" in out2})
    res["R1"] = r1
    print(json.dumps(r1), flush=True)
    # R2
    cnf = os.path.join(LANE, "m2q0b", "cnf", "g000.cnf")
    lrat = os.path.join(LANE, "m2q0b", "proof", "g000.lrat")
    fifo = os.path.join(OUT, "r2_drat_%d.fifo" % time.time_ns())
    os.mkfifo(fifo)
    dst = os.path.join(OUT, "r2_g000.lratstrict2.drat.zst")
    z, t, h, n = zstd_fifo_to_file(fifo, dst)
    t0 = time.time()
    rc, out, stop = run_bounded([LS2, cnf, lrat, fifo], 1300)
    t.join(timeout=120)
    z.wait(timeout=120)
    r2 = {"lrat_bytes": os.path.getsize(lrat), "lratstrict2_rc": rc, "stop": stop, "seconds": round(time.time() - t0, 1),
          "verified": rc == 0 and "s VERIFIED" in out.splitlines(), "tail": out.strip().splitlines()[-2:],
          "drat_raw_bytes": n[0], "drat_raw_sha256": h.hexdigest(), "drat_zst_bytes": os.path.getsize(dst), "drat_zst_sha256": sha(dst)}
    zd = subprocess.Popen(["/opt/homebrew/bin/zstd", "-q", "-d", "-c", dst], stdout=subprocess.PIPE)
    t0 = time.time()
    rc2, out2, stop2 = run_bounded([DT, cnf, "-i", "-w", "-t", "1200"], 1300, stdin=zd.stdout)
    zd.wait(timeout=60)
    r2.update({"drat_recheck_rc": rc2, "drat_recheck_stop": stop2, "drat_recheck_seconds": round(time.time() - t0, 1),
               "drat_recheck_verified": rc2 == 0 and "s VERIFIED" in out2})
    res["R2"] = r2
    print(json.dumps(r2), flush=True)
    json.dump(res, open(os.path.join(LANE, "cycle2", "retention-measure.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
