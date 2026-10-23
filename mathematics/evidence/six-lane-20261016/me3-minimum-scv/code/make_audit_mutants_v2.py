"""Mutation inputs for the hardened coverage checker check_cover_v3.py (controls; make_audit_mutants_v1.py kept).

argv[1] = run directory. Reads (read-only) runs/d01-LW, runs/d01-G, runs/d01-LD2, runs/d03-SWC and code/spec_dual_*.json.
Writes exclusively into the run directory:
  LW_notatest.gz : one CERT:small relabelled CERT:not-a-test         -> outcome not allowed
  LW_fail.gz     : one leaf relabelled FAIL                          -> FAIL rejected unconditionally
  LW_deep.gz     : one leaf replaced by a full subtree reaching max_depth + 1 (valid tiling) -> depth error
  G_corner.gz    : one CERT:radial relabelled CERT:corner (allowed only in SWC) -> outcome not allowed in G
  LD2_Pskip.gz   : one CERT:ld2 relabelled SKIP:in-primal-P (a G rule)  -> outcome not allowed in LD2
  spec_SWC_domain.json : spec_dual_v3.json with the delta range ending at 1/4 -> domain mismatch
  spec_G_params.json   : spec_dual_v1.json with P_r_hi = 4 -> parameter mismatch
  LW_summary_notok.json: d01-LW dual.json with certificate_ok false -> summary rejected
"""
import sys
import gzip
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"


def read(run):
    return gzip.open(L + f"runs/{run}/leaves.txt.gz", "rt").read().splitlines()


def write(name, lines):
    with lane_guard.xopen(f"{RUN}/{name}", "xb") as fh:
        with gzip.GzipFile(fileobj=fh, mode="wb", mtime=0) as gz:
            gz.write(("\n".join(lines) + "\n").encode())


def relabel(lines, old, new):
    m = list(lines)
    j = next(i for i in range(len(m)) if m[i].split()[2] == old and m[i].split()[1] != "-")
    c, p, o = m[j].split()
    m[j] = f"{c} {p} {new}"
    return m, j


info = {}
lw = read("d01-LW")
m, info["notatest"] = relabel(lw, "CERT:small", "CERT:not-a-test")
write("LW_notatest.gz", m)
m, info["fail"] = relabel(lw, "CERT:small", "FAIL")
write("LW_fail.gz", m)
maxd = json.load(open(L + "code/spec_dual_v1.json"))["charts"]["LW"]["max_depth"]
j = next(i for i in range(len(lw)) if lw[i].split()[1] != "-")
c, p, o = lw[j].split()
k = maxd + 1 - len(p)
sub = [f"{c} {p + '0' * k} {o}"] + [f"{c} {p + '0' * (k - 1 - i) + '1'} {o}" for i in range(k)]
write("LW_deep.gz", lw[:j] + sub + lw[j + 1:])
info["deep"] = {"index": j, "path": p, "levels_added": k, "new_max_depth": len(p) + k, "spec_max_depth": maxd}
g = read("d01-G")
m, info["G_corner"] = relabel(g, "CERT:radial", "CERT:corner")
write("G_corner.gz", m)
ld2 = read("d01-LD2")
m, info["LD2_Pskip"] = relabel(ld2, "CERT:ld2", "SKIP:in-primal-P")
write("LD2_Pskip.gz", m)
s3 = json.load(open(L + "code/spec_dual_v3.json"))
s3["charts"]["SWC"]["breakpoints"][1] = ["0", "1/10", "1/5", "1/4"]
with lane_guard.xopen(RUN + "/spec_SWC_domain.json") as fh:
    json.dump(s3, fh)
s1 = json.load(open(L + "code/spec_dual_v1.json"))
s1["charts"]["G"]["params"]["P_r_hi"] = "4"
with lane_guard.xopen(RUN + "/spec_G_params.json") as fh:
    json.dump(s1, fh)
sm = json.load(open(L + "runs/d01-LW/dual.json"))
sm["certificate_ok"] = False
with lane_guard.xopen(RUN + "/LW_summary_notok.json") as fh:
    json.dump(sm, fh)
with lane_guard.xopen(RUN + "/mutants.json") as fh:
    json.dump(info, fh, indent=1)
print(json.dumps(info))
