#!/usr/bin/env python3
"""List canonical P23-inside offset pairs and write their 7x21 beta for the Gray checker.
Usage: offset_p23_canonical_c21v1.py OUTDIR
Same definitions as offset_family_crosscheck_c21v1.py (ARC offsets f(0)=f(1)=0 over F7, the
252 actions T(f)(i)=l*(f(a*i+b)-f(b)-i*(f(a+b)-f(b))), six block rebasings, lexicographic
pair minimum), but it keeps ONLY the canonical pairs whose two offsets both lie in
P23=span{i^2-i, i^3-i}: exactly the pairs excluded from the offset batch because the earlier
2401-pattern common-slope assay covered them with one primary program. Writing their beta
lets the separately written Gray-code checker cross-check that assay at the representative
level. Pure Python, no native children, exclusive outputs.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
from datetime import datetime
from zoneinfo import ZoneInfo


def arc(f):
    for s in range(7):
        counts = [0] * 7
        for i in range(7):
            counts[(f[i] - s * i) % 7] += 1
        if max(counts) > 3:
            return False
    return True


def main():
    out = Path(sys.argv[1])
    os.mkdir(out)
    funcs = [(0, 0) + tail for tail in itertools.product(range(7), repeat=5)]
    arcs = [f for f in funcs if arc(f)]
    index = {f: i for i, f in enumerate(arcs)}
    N = len(arcs)
    actions = [(a, b, l) for a in range(1, 7) for b in range(7) for l in range(1, 7)]
    def act(f, a, b, l):
        return tuple(l * (f[(a * i + b) % 7] - f[b] - i * (f[(a + b) % 7] - f[b])) % 7 for i in range(7))
    images = [[index[act(f, *g)] for g in actions] for f in arcs]
    p23 = {tuple((u * (i * i - i) + v * (i ** 3 - i)) % 7 for i in range(7)) for u in range(7) for v in range(7)}
    def diff(x, y):
        return index.get(tuple((x[i] - y[i]) % 7 for i in range(7)), -1)
    zero = (0,) * 7
    keys = []
    for f1 in range(N):
        if min(images[f1]) != f1 or arcs[f1] not in p23:
            continue
        for f2 in range(N):
            if arcs[f2] not in p23 or diff(arcs[f1], arcs[f2]) < 0:
                continue
            offs = (zero, arcs[f1], arcs[f2])
            best = True
            for order in itertools.permutations(range(3)):
                base = offs[order[0]]
                x = diff(offs[order[1]], base)
                y = diff(offs[order[2]], base)
                for g in range(len(actions)):
                    a, b = images[x][g], images[y][g]
                    if a < f1 or (a == f1 and b < f2):
                        best = False
                        break
                if not best:
                    break
            if best:
                keys.append((f1, f2))
    rows = []
    for f1, f2 in keys:
        offs = (zero, arcs[f1], arcs[f2])
        beta = [[(i * c + offs[t][i]) % 7 for t in range(3) for c in range(7)] for i in range(7)]
        path = out / ('p23-key-%d.beta' % (f1 * N + f2))
        with open(path, 'x') as fh:
            fh.write(''.join(' '.join(map(str, r)) + '\n' for r in beta))
        rows.append({'key': f1 * N + f2, 'f1': list(arcs[f1]), 'f2': list(arcs[f2]),
                     'beta': path.name, 'beta_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    rec = {'clock': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
           'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'N': N, 'canonical_p23_pairs': len(rows), 'pairs': rows,
           'scope': 'representatives of the P23 sub-family only; coverage of all2401 patterns follows from the proved actions'}
    with open(out / 'record.json', 'x') as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: v for k, v in rec.items() if k != 'pairs'}), flush=True)


if __name__ == '__main__':
    main()
