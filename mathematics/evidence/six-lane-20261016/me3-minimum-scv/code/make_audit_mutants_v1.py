"""Create mutated copies of certified leaf records to test that check_cover_v2.py rejects them (controls).

argv[1] = run directory. Inputs (read-only): runs/d01-LW/leaves.txt.gz, runs/d01-LD2/leaves.txt.gz.
Mutants (each written exclusively into the run directory):
  LW_drop.gz        : one leaf line removed            -> expect an incomplete-cell / mismatch error
  LW_fail.gz        : one outcome replaced by FAIL     -> expect a bad-outcome error
  LW_path.gz        : one path's last bit flipped      -> expect a duplicate/mismatch error
  LD2_falseskip.gz  : one CERT leaf relabelled SKIP:skip-s -> expect a skip-rule error
"""
import sys
import gzip
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"
lw = gzip.open(L + "runs/d01-LW/leaves.txt.gz", "rt").read().splitlines()
ld2 = gzip.open(L + "runs/d01-LD2/leaves.txt.gz", "rt").read().splitlines()


def write(name, lines):
    with lane_guard.xopen(f"{RUN}/{name}", "xb") as fh:
        with gzip.GzipFile(fileobj=fh, mode="wb", mtime=0) as gz:
            gz.write(("\n".join(lines) + "\n").encode())


k = len(lw) // 2
write("LW_drop.gz", lw[:k] + lw[k + 1:])
m = list(lw)
c, p, o = m[k].split()
m[k] = f"{c} {p} FAIL"
write("LW_fail.gz", m)
m = list(lw)
idx = next(i for i in range(len(m)) if m[i].split()[1] != "-")
c, p, o = m[idx].split()
p2 = p[:-1] + ("1" if p[-1] == "0" else "0")
m[idx] = f"{c} {p2} {o}"
write("LW_path.gz", m)
m = list(ld2)
j = next(i for i in range(len(m)) if m[i].split()[2].startswith("CERT") and m[i].split()[1] != "-")
c, p, o = m[j].split()
m[j] = f"{c} {p} SKIP:skip-s"
write("LD2_falseskip.gz", m)
info = {"LW_lines": len(lw), "LD2_lines": len(ld2), "drop_index": k, "fail_index": k, "path_index": idx, "falseskip_index": j}
with lane_guard.xopen(RUN + "/mutants.json") as fh:
    json.dump(info, fh, indent=1)
print(json.dumps(info))
