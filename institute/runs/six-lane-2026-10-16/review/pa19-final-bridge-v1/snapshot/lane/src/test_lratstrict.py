#!/usr/bin/env python3
"""Controls for bin/lratstrict (src/lratstrict.c). Writes cycle2/lratstrict-tests.json.
Proofs are produced in memory (CaDiCaL ASCII LRAT to a FIFO read by this script) and fed to the
checker through stdin; nothing large is stored.
  T1 parent negatives/positive (cycle2/checker-smoke): N1, N2 must FAIL; P3 must VERIFY.
  T2 genuine proofs: (13,5,4) UNSAT skeleton CNFs (M1 encode_skel ms01_s00000..s00008, ms05_*),
     19-row M1 ms04_s00000, M2 build_v2 ms02 b0..b4 -> all must VERIFY.
  T3 guaranteed-invalid mutations of each genuine proof -> all must FAIL:
     a drop the empty-clause line; b drop the last hint of the empty-clause line;
     c empty-clause line with no hints; d a hint id replaced by an unused id;
     e delete (before the empty-clause line) a clause that the empty-clause line uses;
     f truncate in the middle of the empty-clause line; g append nothing but change the
     empty-clause line's id to a non-increasing id.
  T4 SAT CNFs ((13,5,4) ms04_s00000 and ms07_s00001, M1) with every genuine (13,5,4) proof -> FAIL.
"""
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel  # noqa: E402
import encode_skel_b  # noqa: E402
import stream_check5 as S  # noqa: E402

LANE = os.path.dirname(HERE)
CHK = os.path.join(LANE, "bin", "lratstrict")
CAD = "/opt/homebrew/bin/cadical"
TMP = os.path.join(LANE, "scratch", "lratstrict-test")


def check(cnf_path, proof_bytes):
    p = subprocess.run([CHK, cnf_path, "/dev/stdin"], input=proof_bytes, capture_output=True)
    out = p.stdout.decode(errors="replace").strip().splitlines()
    return {"rc": p.returncode, "verified": p.returncode == 0 and "s VERIFIED" in out, "tail": out[-2:]}


def write_cnf(name, b):
    p = os.path.join(TMP, name + ".cnf")
    with open(p, "wb") as f:
        f.write(b)
    return p


def lrat_of(cnf_path, tag):
    fifo = os.path.join(TMP, "f_%s_%d_%d" % (tag, os.getpid(), time.time_ns()))
    os.mkfifo(fifo)
    chunks = []

    def rd():
        with open(fifo, "rb") as f:
            while True:
                b = f.read(1 << 16)
                if not b:
                    break
                chunks.append(b)

    t = threading.Thread(target=rd, daemon=True)
    t.start()
    p = subprocess.run([CAD, "-q", "-t", "120", "--lrat=true", "--binary=false", cnf_path, fifo], capture_output=True)
    t.join()
    return p.returncode, b"".join(chunks)


def mutations(proof):
    lines = proof.decode().splitlines()
    ei = max(i for i, l in enumerate(lines) if l.split()[1:2] == ["0"])  # last empty-clause addition
    el = lines[ei].split()
    eid = int(el[0])
    hints = [int(x) for x in el[2:-1]]
    assert el[1] == "0" and el[-1] == "0" and hints
    used = set()
    for l in lines:
        t = l.split()
        if len(t) > 1 and t[1] != "d":
            used.update(int(x) for x in t[1:])
    unused = max(max(used), eid) + 1000
    pre = lines[:ei]
    m = {}
    m["a_drop_empty_line"] = pre
    m["b_drop_last_hint"] = pre + ["%d 0 %s 0" % (eid, " ".join(map(str, hints[:-1])))] if len(hints) > 1 else pre + ["%d 0 0" % eid]
    m["c_no_hints"] = pre + ["%d 0 0" % eid]
    m["d_unknown_hint"] = pre + ["%d 0 %s 0" % (eid, " ".join(map(str, hints[:-1] + [unused])))]
    m["e_delete_used"] = pre + ["%d d %d 0" % (eid - 1 if eid > 1 else eid, hints[0]), lines[ei]]
    m["f_truncated"] = pre + [lines[ei][: max(1, len(lines[ei]) // 2)].rstrip() + " "]
    last_add = max((int(l.split()[0]) for l in pre if l.split()[1:2] != ["d"]), default=0)
    m["g_nonincreasing_id"] = pre + ["%d 0 %s 0" % (last_add, " ".join(map(str, hints)))] if last_add else pre + ["0 0 0"]
    return {k: ("\n".join(v) + "\n").encode() for k, v in m.items()}


def main():
    os.makedirs(TMP, exist_ok=True)
    res = {"checker_sha256": subprocess.run(["shasum", "-a", "256", CHK], capture_output=True, text=True).stdout.split()[0]}
    D = os.path.join(LANE, "cycle2", "checker-smoke")
    res["T1"] = {
        "N1": check(os.path.join(D, "sat1.cnf"), open(os.path.join(D, "n1.lrat"), "rb").read()),
        "N2": check(os.path.join(D, "sat1.cnf"), open(os.path.join(D, "n2.lrat"), "rb").read()),
        "P3": check(os.path.join(D, "unsat_units.cnf"), open(os.path.join(D, "p3.lrat"), "rb").read()),
    }
    cnfs = {}
    for tag in ["ms01_s%05d" % i for i in range(9)] + ["ms05_s%05d" % i for i in range(5)] + ["ms04_s00000", "ms07_s00001"]:
        spec = json.load(open(os.path.join(LANE, "controls", "c13skel", "specs", tag + ".json")))
        cnfs["c13_" + tag] = write_cnf("c13_" + tag, S.cnf_bytes_of(encode_skel.build(spec)[0]))
    cnfs["n19_ms04_s00000"] = write_cnf("n19_ms04_s00000", S.cnf_bytes_of(encode_skel.build(
        json.load(open(os.path.join(LANE, "cases19skel", "specs", "ms04_s00000.json"))))[0]))
    d = json.load(open(os.path.join(LANE, "cycle2", "skel-b", "skeletons-b-ms02.json")))
    special = [p for p in d["profiles"] if list(p) != [4, 3, 3, 3, 3, 3]]
    for i in range(5):
        sk = d["skeletons"][i]
        nv, cl = encode_skel_b.build_v2(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnfs["m2_ms02_b%05d" % i] = write_cnf("m2_ms02_b%05d" % i, encode_skel_b.cnf_bytes(nv, cl))
    proofs, T2, T3 = {}, {}, {}
    for name, path in cnfs.items():
        if name in ("c13_ms04_s00000", "c13_ms07_s00001"):
            continue
        rc, pr = lrat_of(path, name)
        if rc != 20:
            T2[name] = {"cadical_rc": rc}
            continue
        proofs[name] = pr
        T2[name] = dict(check(path, pr), cadical_rc=rc, lrat_bytes=len(pr))
        T3[name] = {k: check(path, mb) for k, mb in mutations(pr).items()}
    res["T2"], res["T3"] = T2, T3
    T4 = {}
    for sat in ("c13_ms04_s00000", "c13_ms07_s00001"):
        for name, pr in proofs.items():
            if name.startswith("c13_"):
                T4["%s<-%s" % (sat, name)] = check(cnfs[sat], pr)
    res["T4"] = T4
    ok = (not res["T1"]["N1"]["verified"] and not res["T1"]["N2"]["verified"] and res["T1"]["P3"]["verified"]
          and all(v.get("verified") for v in T2.values())
          and all(not r["verified"] for v in T3.values() for r in v.values())
          and all(not r["verified"] for r in T4.values()))
    res["counts"] = {"T2_genuine": len(T2), "T2_verified": sum(1 for v in T2.values() if v.get("verified")),
                     "T3_mutations": sum(len(v) for v in T3.values()),
                     "T3_rejected": sum(1 for v in T3.values() for r in v.values() if not r["verified"]),
                     "T4_sat_cnf_checks": len(T4), "T4_rejected": sum(1 for r in T4.values() if not r["verified"])}
    res["ok"] = bool(ok)
    json.dump(res, open(os.path.join(LANE, "cycle2", "lratstrict-tests.json"), "w"), indent=1)
    print(json.dumps({"ok": res["ok"], "counts": res["counts"], "T1": {k: v["verified"] for k, v in res["T1"].items()}}))


if __name__ == "__main__":
    main()
