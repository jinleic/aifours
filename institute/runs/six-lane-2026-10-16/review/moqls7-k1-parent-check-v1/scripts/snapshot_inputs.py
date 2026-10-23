#!/usr/bin/env python3
"""snapshot_inputs.py (parent moqls7-k1-parent-check-v1): copy pinned lane inputs into inputs/lane/ with exclusive
creation; record sha256 of the source before and after the copy and of the destination."""
import datetime, hashlib, json, os, sys
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(D, "inputs", "lane")
REL = ["README.md", "review/K1-THEOREM.r1.md", "evidence/nets7_classes.json", "evidence/LOG.md",
       "code/k1_sat.py", "code/k1_certify.py", "code/k1_encB.py", "code/k1_phase_cert.py", "code/pattern_check.py",
       "code/net_canon.c", "code/net_canon", "code/find_nets.py", "code/nets.py", "code/k1_phase.py",
       "env/drat-trim/drat-trim", "env/drat-trim/drat-trim.c", "env/drat-trim/ctl_sat.cnf",
       "env/drat-trim/ctl_unsat.cnf", "env/drat-trim/ctl_unsat.drat",
       "sources/1406.3681v2.pdf", "sources/1406.3681v2.layout.txt", "sources/2607.12933v2.layout.txt",
       "sources/2607.12933v2.raw.txt", "sources/quantum-latin-2607.12933v2.pdf",
       "archive/void-2026-10-17/pattern_controls.v0-wrong-psi-f-convention.json"]
for sub in ("k1A", "k1B"):
    for n in sorted(os.listdir(os.path.join(LANE, "evidence", sub))):
        REL.append("evidence/%s/%s" % (sub, n))
def sha(b):
    return hashlib.sha256(b).hexdigest()
os.mkdir(DST)
man = {"lane": LANE, "started": datetime.datetime.now().astimezone().isoformat(), "files": []}
for r in REL:
    src = os.path.join(LANE, r)
    with open(src, "rb") as f:
        b1 = f.read()
    st = os.stat(src)
    out = os.path.join(DST, r)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "xb") as f:
        f.write(b1)
    os.chmod(out, st.st_mode & 0o755)
    with open(src, "rb") as f:
        b2 = f.read()
    with open(out, "rb") as f:
        b3 = f.read()
    man["files"].append({"rel": r, "bytes": len(b1), "sha256_before": sha(b1), "sha256_after": sha(b2),
                         "sha256_copy": sha(b3), "src_mtime": st.st_mtime, "stable": sha(b1) == sha(b2) == sha(b3)})
man["finished"] = datetime.datetime.now().astimezone().isoformat()
man["all_stable"] = all(x["stable"] for x in man["files"])
with open(os.path.join(D, "inputs", "lane-manifest.json"), "x") as f:
    json.dump(man, f, indent=1)
print("files", len(man["files"]), "all_stable", man["all_stable"])
