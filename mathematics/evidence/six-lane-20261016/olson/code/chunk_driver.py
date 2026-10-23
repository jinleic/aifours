#!/usr/bin/env python3
"""Checkpointed exhaustive run: one olson_dfs process per Aut-orbit of the first
letter, second-letter subtrees reported as completed chunks (JSONL lines).
Resumable: completed (orbit, second) chunks are skipped on restart.

Usage: python3 code/chunk_driver.py GROUP L [memo_log2]
Output: evidence/runs/GROUP.L<L>.chunks.jsonl (+ .done.json when complete)
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GDIR = os.path.join(LANE, 'evidence', 'groups')
RDIR = os.path.join(LANE, 'evidence', 'runs')


def main():
    g, L = sys.argv[1], int(sys.argv[2])
    mlog = sys.argv[3] if len(sys.argv) > 3 else '23'
    os.makedirs(RDIR, exist_ok=True)
    tab = os.path.join(GDIR, g + '.tab')
    orb = os.path.join(GDIR, g + '.orbits')
    n = int(open(tab).readline())
    orbit_of = list(map(int, open(orb).read().split('\n')[1].split()))
    norb = max(orbit_of) + 1
    out = os.path.join(RDIR, f'{g}.L{L}.chunks.jsonl')
    done = {}
    if os.path.exists(out):
        for line in open(out):
            line = line.strip()
            if line:
                d = json.loads(line)
                done[(d['orbit'], d['second'])] = d
    for o in range(norb):
        seconds = [a for a in range(n) if orbit_of[a] >= o]
        todo = [a for a in seconds if (o, a) not in done]
        if not todo:
            continue
        start = todo[0]
        # chunks before `start` are done; the binary skips a2 < start
        cmd = [os.path.join(HERE, 'olson_dfs'), tab, orb, str(L), str(n), 'count', mlog, '-', str(o), str(start)]
        with open(out, 'a') as f:
            p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            for line in p.stderr:
                line = line.strip()
                if not line.startswith('{'):
                    continue
                d = json.loads(line)
                d['wall_unix'] = time.time()
                d['cmd'] = ' '.join(cmd[1:])
                if (d['orbit'], d['second']) in done:
                    continue
                f.write(json.dumps(d) + '\n')
                f.flush()
                done[(d['orbit'], d['second'])] = d
            p.wait()
            if p.returncode != 0:
                print('process failed', p.returncode, file=sys.stderr)
                sys.exit(1)
    total = sum(d['count'] for d in done.values())
    expected = sum(1 for o in range(norb) for a in range(n) if orbit_of[a] >= o)
    summ = {'group': g, 'n': n, 'L': L, 'K': n, 'chunks': len(done), 'expected_chunks': expected,
            'total_normalised_avoiders': total, 'complete': len(done) == expected}
    with open(os.path.join(RDIR, f'{g}.L{L}.done.json'), 'w') as f:
        json.dump(summ, f, indent=1)
    print(json.dumps(summ))


if __name__ == '__main__':
    main()
