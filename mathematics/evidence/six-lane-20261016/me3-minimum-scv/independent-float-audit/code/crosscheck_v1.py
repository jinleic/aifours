"""Cross-check report-v1.md site tables against the scanner inventory (text only; stdlib; prints JSON to stdout).
argv[1] = run dir (unused except by the launcher). Reads independent-float-audit/report-v1.md and
independent-float-audit/runs/s01-scan/sites.tsv. Checks 1-1 coverage of the required kinds and counts dispositions."""
import json
import re
import sys

REQ = {"DIV", "MOD", "POW", "FLOATLIT", "MODATTR", "CALL:float", "CALL:round", "CALL:int", "CALL:str",
       "CALL:Fraction", "CALL:fmpq", "CALL:arb", "CALL:acb", "CALL:abs", "CALL:bool", "METHOD:upper",
       "CALL:time.time", "CALL:min", "CALL:max", "CALL:divmod", "CALL:json.load", "CALL:json.dump",
       "CALL:json.dumps", "DEFAULT"}
scan = {}
for ln in open("independent-float-audit/runs/s01-scan/sites.tsv", encoding="utf-8").read().splitlines()[1:]:
    f, line, col, kind = ln.split("\t")[:4]
    scan.setdefault((f, int(line), int(col), kind), True)
req = {k for k in scan if k[3] in REQ or k[3].startswith("CALL:math.")}
seen = {}
counts, perfile, errors = {}, {}, []
cur = None
for ln in open("independent-float-audit/report-v1.md", encoding="utf-8").read().splitlines():
    if ln.startswith("## "):
        cur = None
    m = re.match(r"^### (code/\S+)", ln)
    if m:
        cur = m.group(1)
        continue
    if cur is None or not ln.startswith("| ") or ln.startswith("| sites") or ln.startswith("|---"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split(" | ")]
    sites, kind, disp = cells[0], cells[1], cells[-1]
    d = next((x for x in ("OK-exact", "OK-heuristic", "OK-reporting-only", "DEAD", "DEFECT") if disp.startswith(x)),
             None)
    if d is None:
        errors.append(f"bad disposition {disp!r} in {cur}")
        continue
    for a, b in re.findall(r"(\d+):(\d+)", sites):
        key = (cur, int(a), int(b), kind)
        if key not in scan:
            errors.append(f"not in scanner: {key}")
        if key in seen:
            errors.append(f"duplicate: {key}")
        seen[key] = d
        counts[d] = counts.get(d, 0) + 1
        perfile.setdefault(cur, {}).setdefault(d, 0)
        perfile[cur][d] += 1
missing = sorted(k for k in req if k not in seen)
print(json.dumps({"required_sites": len(req), "classified_sites": len(seen), "missing": missing[:60],
                  "n_missing": len(missing), "errors": errors[:60], "n_errors": len(errors), "counts": counts,
                  "per_file": perfile}, indent=0))
