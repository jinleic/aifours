#!/usr/bin/env python3
"""Verify a zstd-compressed binary DRAT proof with the lane's drat-trim, streaming (no decompressed copy on disk).

Usage: python3 -B code/drat_check.py CNF PROOF.drat.zst OUT.json [--ascii]
Runs `zstd -dc PROOF | bin/drat-trim CNF -i -t 40000` (or -I with --ascii). Writes OUT.json (mode x) and
OUT.json.drat-trim.stdout (mode x).  VERIFIED iff some output line, after stripping '\r' and surrounding
whitespace, equals 's VERIFIED' and no line equals 's NOT VERIFIED'.
"""
import hashlib
import json
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def host_date():
    return subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    cnf, proof, out = sys.argv[1], sys.argv[2], sys.argv[3]
    mode = "-I" if "--ascii" in sys.argv[4:] else "-i"
    drat = os.path.join(LANE, "bin/drat-trim")
    rec = {"cnf": cnf, "cnf_sha256": sha256_file(cnf), "proof": proof, "proof_sha256": sha256_file(proof),
           "drat_trim": drat, "drat_trim_sha256": sha256_file(drat), "start": host_date()}
    with open(out + ".drat-trim.stdout", "x") as so:
        z = subprocess.Popen(["zstd", "-dc", proof], stdout=subprocess.PIPE)
        d = subprocess.Popen([drat, cnf, mode, "-t", "40000"], stdin=z.stdout, stdout=so, stderr=subprocess.STDOUT)
        z.stdout.close()
        drc = d.wait()
        zrc = z.wait()
    rec["end"] = host_date()
    rec["drat_trim_exit"] = drc
    rec["zstd_exit"] = zrc
    lines = [ln.replace("\r", "").strip() for ln in open(out + ".drat-trim.stdout", errors="replace")]
    rec["s_lines"] = [ln for ln in lines if ln.startswith("s ")]
    rec["verified"] = ("s VERIFIED" in lines) and ("s NOT VERIFIED" not in lines) and zrc == 0
    with open(out, "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({"cnf": cnf, "verified": rec["verified"], "s_lines": rec["s_lines"], "exit": drc}))


if __name__ == "__main__":
    main()
