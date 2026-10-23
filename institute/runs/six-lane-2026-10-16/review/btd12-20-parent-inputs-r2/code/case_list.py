#!/usr/bin/env python3
"""case_list.py -- the 3073-case list of notes/case-split-r1.md Part C as one JSON-lines file (stdlib).

Inputs: the seven d-type files runs/mg-v1/mg-n{4..10}.txt (nauty multig -T lines, filtered by code/mg_filter.py)
and runs/e-v1/e-combos-v2.jsonl (code/e_combos.py).  Output OUT.jsonl (exclusive), one line per case:
{"id": "d-n<n>-<k>" or "e-<k>", "source": file:line, "rows": [[4 columns] x 12]} with d-type vertex v -> columns
2v, 2v+1 and edge uv -> {2u, 2u+1, 2v, 2v+1} repeated by multiplicity.  Every row set is checked: 12 rows of 4
distinct columns in 0..19, pairwise intersections in {0,2,4}, column covers in {0,2,4,6}.
Usage: case_list.py OUT.jsonl
"""
import hashlib
import json
import os
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check(rows):
    assert len(rows) == 12 and all(len(set(r)) == 4 and all(0 <= c < 20 for c in r) for r in rows)
    for i in range(12):
        for k in range(i + 1, 12):
            assert len(set(rows[i]) & set(rows[k])) in (0, 2, 4)
    for j in range(20):
        assert sum(1 for r in rows if j in r) in (0, 2, 4, 6)


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out, inputs, n = argv[1], {}, 0
    with open(out, "x") as f:
        for nv in range(4, 11):
            path = os.path.join(LANE, "runs", "mg-v1", f"mg-n{nv}.txt")
            data = open(path, "rb").read()
            inputs[os.path.relpath(path, LANE)] = hashlib.sha256(data).hexdigest()
            for k, line in enumerate(data.decode().splitlines()):
                t = line.split()
                rows = []
                for q in range(int(t[1])):
                    u, v, mu = int(t[2 + 3 * q]), int(t[3 + 3 * q]), int(t[4 + 3 * q])
                    rows += [[2 * u, 2 * u + 1, 2 * v, 2 * v + 1]] * mu
                check(rows)
                f.write(json.dumps({"id": f"d-n{nv}-{k}", "source": f"runs/mg-v1/mg-n{nv}.txt:{k + 1}",
                                    "rows": rows}) + "\n")
                n += 1
        path = os.path.join(LANE, "runs", "e-v1", "e-combos-v2.jsonl")
        data = open(path, "rb").read()
        inputs[os.path.relpath(path, LANE)] = hashlib.sha256(data).hexdigest()
        for k, line in enumerate(data.decode().splitlines()):
            obj = json.loads(line)
            rows = [sorted(r) for r in obj["rows"]]
            check(rows)
            f.write(json.dumps({"id": f"e-{k}", "source": f"runs/e-v1/e-combos-v2.jsonl:{k + 1}", "name": obj["name"],
                                "rows": rows}) + "\n")
            n += 1
    print(json.dumps({"cases": n, "inputs": inputs, "out_sha256": hashlib.sha256(open(out, "rb").read()).hexdigest()}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
