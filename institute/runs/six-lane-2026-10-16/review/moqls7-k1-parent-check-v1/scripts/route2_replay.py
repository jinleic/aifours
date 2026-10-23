#!/usr/bin/env python3
"""route2_replay.py (parent moqls7-k1-parent-check-v1): replay the pinned lane encoders as subprocesses.
 - pinned k1_certify.py (encoder A driver, CaDiCaL enumeration + DRAT, lane drat-trim copy) -> route2/replayA/
 - pinned k1_encB.py (encoder B, CaDiCaL enumeration + kissat DRAT, lane drat-trim copy) -> route2/replayB/
 - pinned k1_sat.py CLI base CNF per class (w3=False, hall=False, the certify setting) -> route2/baseA/
 - base CNF of encoder B per class via a one-line shim that imports the pinned k1_encB (replay only) -> route2/baseB/
Nothing here imports lane code into this process."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import runlib

D = os.path.dirname(HERE)
LC = os.path.join(D, "inputs", "lane", "code")
CLS = os.path.join(D, "inputs", "lane", "evidence", "nets7_classes.json")
PY = "/usr/bin/python3"
R2 = os.path.join(D, "route2")
env = dict(os.environ, TMPDIR=os.path.join(D, "tmp"))
rec = {"started": runlib.now(), "python": PY, "pinned": {}, "runs": []}
for n in ("k1_sat.py", "k1_certify.py", "k1_encB.py"):
    rec["pinned"][n] = runlib.sha_file(os.path.join(LC, n))
rec["pinned"]["nets7_classes.json"] = runlib.sha_file(CLS)
rec["pinned"]["lane_drat_trim_copy"] = runlib.sha_file(os.path.join(D, "inputs", "lane", "env", "drat-trim", "drat-trim"))
for tool in ("/opt/homebrew/bin/cadical", "/opt/homebrew/bin/kissat"):
    rec["pinned"][tool] = runlib.sha_file(os.path.realpath(tool))
logs = os.path.join(R2, "logs")
os.mkdir(logs)
# base CNFs
os.mkdir(os.path.join(R2, "baseA"))
os.mkdir(os.path.join(R2, "baseB"))
shim = ("import json,sys; sys.path.insert(0,%r); import k1_encB; net=[tuple(q) for q in json.load(open(%r))"
        "['classes'][int(sys.argv[1])]['net']]; nv,cl,s=k1_encB.encode(net); open(sys.argv[2],'x').write(k1_encB.text(nv,cl))")
for i in range(7):
    out = os.path.join(R2, "baseA", "c%d.base.cnf" % i)
    rec["runs"].append(runlib.run([PY, "-B", os.path.join(LC, "k1_sat.py"), CLS, str(i), "--out", out], D,
                                  os.path.join(logs, "baseA%d.out" % i), os.path.join(logs, "baseA%d.err" % i), env=env))
    out = os.path.join(R2, "baseB", "c%d.B.base.cnf" % i)
    rec["runs"].append(runlib.run([PY, "-B", "-c", shim % (LC, CLS), str(i), out], D,
                                  os.path.join(logs, "baseB%d.out" % i), os.path.join(logs, "baseB%d.err" % i), env=env))
# full drivers (they create their own OUTDIR, which must not exist yet)
rec["runs"].append(runlib.run([PY, "-B", os.path.join(LC, "k1_certify.py"), CLS, os.path.join(R2, "replayA")], D,
                              os.path.join(logs, "replayA.out"), os.path.join(logs, "replayA.err"), env=env))
rec["runs"].append(runlib.run([PY, "-B", os.path.join(LC, "k1_encB.py"), CLS, os.path.join(R2, "replayB")], D,
                              os.path.join(logs, "replayB.out"), os.path.join(logs, "replayB.err"), env=env))
rec["finished"] = runlib.now()
with open(os.path.join(R2, "replay-runs.json"), "x") as f:
    json.dump(rec, f, indent=1)
print(json.dumps([(r["argv"][-2:], r["exit"], r["wall_s"], r["all_waited_descendants_maxrss_bytes"]) for r in rec["runs"]]))
