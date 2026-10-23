#!/usr/bin/env python3
"""Freeze a receipt for the exhaustive small-group automaton runs.

For each (group, L) it records the exact command, the JSON result, wall time,
and sha256 of the source files, compiled binary, table and orbit files.
Positive/mutation controls included:
  * abelian / p-groups at 2n-1 must report total 0 (theory: EGZ, Dimitrov)
  * S3, D10 at 2n-2 must report >0 (the odd-dihedral r^{2m-1}s^{2m-1} word)
  * a corrupted (non-associative) table must be rejected by the validator
Usage: python3 code/receipt_small.py OUT.json GROUP:L [GROUP:L ...]
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GDIR = os.path.join(LANE, 'evidence', 'groups')


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    out = sys.argv[1]
    jobs = [a.split(':') for a in sys.argv[2:]]
    binp = os.path.join(HERE, 'olson_dfs')
    rec = {
        'created_unix': time.time(),
        'compile': 'clang++ -std=c++17 -O3 -march=native -o code/olson_dfs code/olson_dfs.cpp',
        'clang': subprocess.run(['clang++', '--version'], capture_output=True, text=True).stdout.splitlines()[0],
        'sources': {f: sha(os.path.join(HERE, f)) for f in
                    ['olson_dfs.cpp', 'groups.py', 'autorbits.py', 'prep_group.py', 'receipt_small.py']},
        'binary_sha256': sha(binp),
        'runs': [],
    }
    for g, L in jobs:
        tab = os.path.join(GDIR, g + '.tab')
        orb = os.path.join(GDIR, g + '.orbits')
        n = int(open(tab).readline())
        cmd = [binp, tab, orb, L, str(n), 'count', '24']
        t0 = time.time()
        r = subprocess.run(cmd, capture_output=True, text=True)
        dt = time.time() - t0
        res = json.loads(r.stdout)
        rec['runs'].append({'group': g, 'n': n, 'L': int(L), 'K': n,
                            'cmd': ' '.join(os.path.relpath(c, LANE) if os.path.isabs(c) else c for c in cmd),
                            'table_sha256': sha(tab), 'orbits_sha256': sha(orb),
                            'aut_json_sha256': sha(os.path.join(GDIR, g + '.aut.json')),
                            'exit': r.returncode, 'wall_s': round(dt, 3), 'result': res})
        print(g, L, 'total=', res['total'], 'secs=', res['secs'])
    # mutation control: corrupt one table entry of S3, expect validator rejection (exit 3)
    s3 = os.path.join(GDIR, 'S3.tab')
    rows = open(s3).read().split('\n')
    n = int(rows[0])
    tabrows = [list(map(int, r.split())) for r in rows[1:1 + n]]
    a, b = tabrows[1][2], tabrows[1][3]
    tabrows[1][2], tabrows[1][3] = b, a
    bad = os.path.join(GDIR, 'S3.corrupt.tab')
    with open(bad, 'w') as f:
        f.write(f"{n}\n" + '\n'.join(' '.join(map(str, r)) for r in tabrows) + '\n')
    r = subprocess.run([binp, bad, os.path.join(GDIR, 'S3.orbits'), '11', '6', 'count', '20'],
                       capture_output=True, text=True)
    rec['mutation_control'] = {'what': 'S3 table with two entries of row 1 swapped',
                               'exit': r.returncode, 'stderr': r.stderr.strip(),
                               'expected': 'exit 3 (validator rejects)', 'corrupt_table_sha256': sha(bad)}
    print('mutation control exit', r.returncode, r.stderr.strip())
    with open(out, 'w') as f:
        json.dump(rec, f, indent=1)


if __name__ == '__main__':
    main()
