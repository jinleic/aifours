#!/usr/bin/env python3
"""proof-control-decode-model-v1.py  (reviewer-authored, f113 review)

Decode a kissat/cadical model (lines starting with 'v ') against a .map
file produced by proof-control-t30-sat-v1.py, and report the E (and P) sets
with their pair-projection structure: cell counts, per-row degrees, whether
each 3x3 residual projection is 2-regular (complement a perfect matching),
and the residual alphabet profile.

If P is present, the model is also validated DIRECTLY against the
combinatorial abstraction (independently of the CNF encoding): for every
coordinate pair, every cell of [6]^2 is either a P-cell (exactly one P word,
no E word) or an E-cell (no P word, >= 2 E words), with exactly n E-cells,
where n = 36 - |P| is inferred from the model.
Usage: python3 -B proof-control-decode-model-v1.py <solver.log> <cnf.map> [out.json]
"""
import json, sys
from collections import Counter
from pathlib import Path

PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def validate(E, P):
    n = 36 - len(P)
    problems = []
    for (i, j) in PAIRS:
        pc = Counter((w[i], w[j]) for w in P)
        ec = Counter((w[i], w[j]) for w in E)
        if any(v > 1 for v in pc.values()):
            problems.append(f'{i}{j}: P not pair-injective')
        if set(pc) & set(ec):
            problems.append(f'{i}{j}: P-cell and E-cell overlap')
        if len(ec) != n:
            problems.append(f'{i}{j}: E-cells {len(ec)} != n {n}')
        if ec and min(ec.values()) < 2:
            problems.append(f'{i}{j}: an E-cell has < 2 extensions')
        if len(pc) + len(ec) != 36:
            problems.append(f'{i}{j}: cells not partitioned ({len(pc)}+{len(ec)})')
    return n, problems


def main():
    log, mp = sys.argv[1], sys.argv[2]
    true = set()
    status = None
    for line in Path(log).read_text().splitlines():
        if line.startswith('s '):
            status = line[2:].strip()
        if line.startswith('v '):
            for tok in line[2:].split():
                v = int(tok)
                if v > 0:
                    true.add(v)
    E, P = [], []
    for line in Path(mp).read_text().splitlines():
        kind, v, *w = line.split()
        if int(v) in true:
            (E if kind == 'E' else P).append(tuple(map(int, w)))
    rep = {'status': status, 'E_size': len(E), 'P_size': len(P), 'E': sorted(E), 'P': sorted(P),
           'profile': [len({w[i] for w in E}) for i in range(4)], 'projections': {}}
    for (i, j) in PAIRS:
        cnt = Counter((w[i], w[j]) for w in E)
        rows = Counter(a for (a, b) in cnt)
        cols = Counter(b for (a, b) in cnt)
        rep['projections'][f'{i}{j}'] = {
            'cells': len(cnt), 'min_ext': min(cnt.values()) if cnt else 0,
            'row_degrees': sorted(rows.values()), 'col_degrees': sorted(cols.values()),
            'two_regular': set(rows.values()) == {2} and set(cols.values()) == {2} and len(cnt) == 6,
            'P_cells': len({(w[i], w[j]) for w in P}),
        }
    if P and status == 'SATISFIABLE':
        n, problems = validate(E, P)
        rep['abstraction_check'] = {'n': n, 'problems': problems, 'valid': not problems}
    print(json.dumps({k: v for k, v in rep.items() if k not in ('E', 'P')}, indent=None))
    if len(sys.argv) > 3:
        with Path(sys.argv[3]).open('x', encoding='utf-8') as fh:
            json.dump(rep, fh, indent=1); fh.write('\n')


if __name__ == '__main__':
    main()
