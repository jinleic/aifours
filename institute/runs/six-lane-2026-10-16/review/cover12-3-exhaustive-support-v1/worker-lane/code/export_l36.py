#!/usr/bin/env python3
"""export_l36.py -- write every (12,3)-covering string of length 36 found by Impl B, and the 12 rotation-class
representatives found by Impl A, as strict witness files (README 1.5 format), then strictly verify each file.

Usage: export_l36.py RUNDIR CPRO1_TOKENS OUTDIR
  RUNDIR: runs/L36-v1 (reads B-12-3-36-00{0,1,2}.found and A-12-3-36.found; read-only)
  OUTDIR: fresh directory (must not exist); every file is created exclusively, nothing is deleted or overwritten.
Writes OUTDIR/all-432/*.cs (one file per string s found by B; bits x_0..x_35 with x_i = bit i of s),
OUTDIR/classes-12/*.cs (A's lex-minimal representatives), a SHA256SUMS file in each (shasum -a 256 -c format),
OUTDIR/index.json (per file: SHA-256, s, class, rotation offset, B job, CPro1 flag) and OUTDIR/verification.json
(verify_cs.py --expect 12 3 36 --sha256 <pinned> on every file).
Checks: |B| = 432 distinct strings; every A representative is lex-minimal with period 36; the set of B strings equals
the set of all 36 rotations of the 12 representatives; the CPro1 sequence is one of the B strings.
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
n, R, L = 12, 3, 36


def bits_of(s):
    return tuple((s >> i) & 1 for i in range(L))


def s_of(xs):
    return sum(b << i for i, b in enumerate(xs))


def rot(xs, k):
    return tuple(xs[(i + k) % L] for i in range(L))


def big_endian(xs):
    r = 0
    for b in xs:
        r = (r << 1) | b
    return r


def write_cert(path, xs):
    content = f"COVERING-SEQUENCE {n} {R} {L}\n" + " ".join(map(str, xs)) + "\n"
    with open(path, "x") as f:
        f.write(content)
    return hashlib.sha256(content.encode()).hexdigest()


def main(argv):
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    rundir, cpro1_path, out = argv[1], argv[2], argv[3]
    os.makedirs(out)
    ok = True
    # B strings, with job of origin
    bjobs = sorted(glob.glob(os.path.join(rundir, f"B-{n}-{R}-{L}-*.found")))
    bstr = {}
    for bj in bjobs:
        for line in open(bj):
            if line.strip():
                s = int(line, 16)
                ok &= s not in bstr
                bstr[s] = os.path.basename(bj)[:-len(".found")]
    # A representatives
    reps = []
    for line in open(os.path.join(rundir, f"A-{n}-{R}-{L}.found")):
        if line.strip():
            r_hex, s_hex, per = line.split()
            xs = bits_of(int(s_hex, 16))
            ok &= big_endian(xs) == int(r_hex, 16) and int(per) == L
            ok &= all(rot(xs, k) > xs for k in range(1, L))  # strictly lex-minimal, so period L
            reps.append(xs)
    reps.sort()
    rotmap = {}
    for ci, xs in enumerate(reps):
        for k in range(L):
            y = rot(xs, k)
            ok &= y not in rotmap
            rotmap[y] = (ci, k)
    sets_equal = set(bits_of(s) for s in bstr) == set(rotmap)
    ok &= len(bstr) == 432 and len(reps) == 12 and sets_equal
    cpro1 = tuple(int(t) for t in open(cpro1_path).read().split())
    ok &= len(cpro1) == L and s_of(cpro1) in bstr
    # write files
    d_all, d_cls = os.path.join(out, "all-432"), os.path.join(out, "classes-12")
    os.makedirs(d_all)
    os.makedirs(d_cls)
    index = {"n": n, "R": R, "L": L, "bit_convention": "token i (0-based) on line 2 is x_i = bit i of s",
             "rotation_convention": "file = representative rotated by k: x_i = rep_{(i+k) mod 36}",
             "classes": [], "strings": []}
    sums_cls = []
    for ci, xs in enumerate(reps):
        name = f"cs-12-3-36-class{ci + 1:02d}-r{big_endian(xs):09x}.cs"
        sha = write_cert(os.path.join(d_cls, name), xs)
        sums_cls.append(f"{sha}  {name}\n")
        index["classes"].append({"class": ci + 1, "file": f"classes-12/{name}", "sha256": sha,
                                 "lexmin_r_hex": f"{big_endian(xs):09x}", "s_hex": f"{s_of(xs):09x}",
                                 "bits": "".join(map(str, xs)), "period": L,
                                 "contains_cpro1": rotmap[cpro1][0] == ci})
    sums_all = []
    for s in sorted(bstr):
        xs = bits_of(s)
        ci, k = rotmap[xs]
        name = f"cs-12-3-36-s{s:09x}.cs"
        sha = write_cert(os.path.join(d_all, name), xs)
        sums_all.append(f"{sha}  {name}\n")
        index["strings"].append({"file": f"all-432/{name}", "sha256": sha, "s_hex": f"{s:09x}",
                                 "bits": "".join(map(str, xs)), "class": ci + 1, "rotation_k": k,
                                 "b_job": bstr[s], "is_cpro1_as_given": xs == cpro1})
    for d, lines in ((d_all, sums_all), (d_cls, sums_cls)):
        with open(os.path.join(d, "SHA256SUMS"), "x") as f:
            f.writelines(lines)
    index["checks"] = {"b_strings": len(bstr), "b_strings_distinct": True if ok else None, "a_classes": len(reps),
                       "b_set_equals_all_rotations_of_a_reps": sets_equal,
                       "cpro1_class": rotmap.get(cpro1, (-1, 0))[0] + 1, "cpro1_rotation_k": rotmap.get(cpro1, (0, -1))[1],
                       "all_ok_before_verification": ok}
    # strict verification of every exported file
    vres, vbad = [], 0
    vsha = hashlib.sha256(open(os.path.join(CODE, "verify_cs.py"), "rb").read()).hexdigest()
    for rec in index["classes"] + index["strings"]:
        path = os.path.join(out, rec["file"])
        p = subprocess.run([sys.executable, os.path.join(CODE, "verify_cs.py"), path, "--expect", str(n), str(R),
                            str(L), "--sha256", rec["sha256"]], capture_output=True, text=True)
        kv = dict(line.split(": ", 1) for line in p.stdout.strip().split("\n") if ": " in line)
        verdict = p.stdout.strip().split("\n")[-1] if p.stdout.strip() else ""
        good = p.returncode == 0 and verdict == "VALID" and kv.get("targets_checked") == "4096"
        vbad += not good
        vres.append({"file": rec["file"], "sha256": rec["sha256"], "verdict": verdict, "rc": p.returncode,
                     "targets_checked": kv.get("targets_checked"), "max_nearest_distance": kv.get("max_nearest_distance"),
                     "histogram": kv.get("nearest_distance_histogram"),
                     "all_zero": kv.get("all_zero_nearest_distance"), "all_one": kv.get("all_one_nearest_distance")})
    ok &= vbad == 0
    with open(os.path.join(out, "index.json"), "x") as f:
        json.dump(index, f, indent=1)
        f.write("\n")
    with open(os.path.join(out, "verification.json"), "x") as f:
        json.dump({"verifier": "code/verify_cs.py", "verifier_sha256": vsha,
                   "command": "verify_cs.py FILE --expect 12 3 36 --sha256 <sha256 from index.json>",
                   "files": len(vres), "valid": len(vres) - vbad, "invalid": vbad, "results": vres,
                   "all_ok": ok}, f, indent=1)
        f.write("\n")
    print(f"B strings {len(bstr)}, A classes {len(reps)}, B set = rotations of A reps: {sets_equal}, "
          f"CPro1 class {rotmap.get(cpro1, (-1, 0))[0] + 1} k {rotmap.get(cpro1, (0, -1))[1]}; "
          f"verified {len(vres) - vbad}/{len(vres)}; {'OK' if ok else 'NOT-OK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
