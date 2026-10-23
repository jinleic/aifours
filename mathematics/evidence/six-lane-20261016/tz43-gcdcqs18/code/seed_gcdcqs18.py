#!/usr/bin/env python3
"""Compact, stdlib-only seed replay and action audit for the pinned Z8 x Z3^2 gcDCQS(18^4:2).

make CERT SEED.json: read the raw certificate, reconstruct the claimed generators independently (S^2:
(z1,z2)->(z2,-z1)), verify all block-orbits and the least-element transport of POINT 0 to all group points,
construct the H-kernel frame orbits at both stem points, and require byte equality before writing a seed.
expand SEED.json OUT.txt: regenerate the complete raw certificate from generators, block orbit representatives,
POINT 0 classes and the comment header, without the SAT model or producer modules. Exclusive writes only.
The audit checks the claimed action, not correctness of the design; the independent definition-first checkers
remain the acceptance routes. The chosen class numbering is transported by the least element; the entire group
need not preserve class numbers.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
from lane_guard import xopen  # noqa: E402
import hashlib
import json
from collections import deque, Counter

V, N = 74, 72


def closure(gens):
    ident = tuple(range(V))
    seen, queue = {ident}, deque([ident])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = tuple(g[p] for p in a)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return sorted(seen)


def claimed_generators():
    def lab(a, z1, z2):
        return 9 * (a % 8) + 3 * (z1 % 3) + z2 % 3
    dec = [(p // 9, p // 3 % 3, p % 3) for p in range(N)]
    t8 = tuple([lab(a + 1, z1, z2) for a, z1, z2 in dec] + [73, 72])
    t31 = tuple([lab(a, z1 + 1, z2) for a, z1, z2 in dec] + [72, 73])
    t32 = tuple([lab(a, z1, z2 + 1) for a, z1, z2 in dec] + [72, 73])
    mu = tuple([lab(a, z2, -z1) for a, z1, z2 in dec] + [72, 73])
    t4 = tuple([lab(a + 4, z1, z2) for a, z1, z2 in dec] + [72, 73])
    return [t8, t31, t32, mu], [t4, t31, t32]


def read_cert(path):
    raw = open(path, 'rb').read()
    head = raw.decode().splitlines()[0]
    lines = [s.split('#', 1)[0].split() for s in raw.decode().splitlines()]
    lines = [s for s in lines if s]
    assert lines[:4] == [['GCDCQS', '74', '4', '18', '2'], ['COLOURS', '37'], ['HOLEFREE', '10'], ['GROUPS']]
    groups = [[int(z) for z in s] for s in lines[4:8]]
    assert lines[8] == ['STEM'] and lines[9] == ['72', '73'] and lines[10] == ['BLOCKS']
    pos, blocks = 11, []
    while pos < len(lines) and lines[pos][0] not in ('POINT', 'STEMPOINT'):
        blocks.append(tuple(int(z) for z in lines[pos]))
        pos += 1
    cols, frames = {}, {}
    x = kind = None
    for row in lines[pos:]:
        if row[0] == 'POINT':
            x, kind = int(row[1]), 'point'
            assert x not in cols
            cols[x] = []
        elif row[0] == 'STEMPOINT':
            x, kind = int(row[1]), 'stem'
            assert x not in frames
            frames[x] = []
        elif row[0] == 'CLASS':
            assert kind == 'point' and int(row[1]) == len(cols[x])
            cols[x].append([])
        elif row[0] == 'FRAME':
            assert kind == 'stem'
            frames[x].append((int(row[1]), []))
        elif kind == 'point':
            cols[x][-1].append(tuple(int(z) for z in row))
        else:
            frames[x][-1][1].append(tuple(int(z) for z in row))
    return raw, head, groups, set(blocks), cols, frames


def image(e, t):
    return tuple(sorted(e[p] for p in t))


def regenerate(seed):
    G = closure([tuple(g) for g in seed['generators']])
    H = closure([tuple(g) for g in seed['frame_generators']])
    assert len(G) == 288 and len(H) == 18
    blocks = {image(e, b) for b in seed['block_representatives'] for e in G}
    cols = {}
    for e in G:
        y = e[0]
        if y not in cols:
            cols[y] = [sorted(image(e, t) for t in C) for C in seed['classes_at_0']]
    frames = {}
    for a in (72, 73):
        remaining = {tuple(p for p in B if p != a) for B in blocks if a in B}
        out = []
        while remaining:
            t = min(remaining)
            orb = {image(e, t) for e in H}
            assert orb <= remaining
            remaining -= orb
            missing = set(range(4)) - {p // 9 % 4 for p in t}
            assert len(missing) == 1
            out.append((missing.pop(), sorted(orb)))
        frames[a] = sorted(out)
    lines = [seed['comment'], 'GCDCQS 74 4 18 2', 'COLOURS 37', 'HOLEFREE 10', 'GROUPS']
    lines += [' '.join(map(str, Gp)) for Gp in seed['groups']]
    lines += ['STEM', '72 73', 'BLOCKS']
    lines += [' '.join(map(str, B)) for B in sorted(blocks)]
    for p in range(N):
        lines.append(f'POINT {p}')
        for j, C in enumerate(cols[p]):
            lines.append(f'CLASS {j}')
            lines += [' '.join(map(str, t)) for t in C]
    for a in (72, 73):
        lines.append(f'STEMPOINT {a}')
        for j, C in frames[a]:
            lines.append(f'FRAME {j}')
            lines += [' '.join(map(str, t)) for t in C]
    return ('\n'.join(lines) + '\n').encode(), G, H, blocks, cols, frames


def main():
    if sys.argv[1] == 'make':
        src, out = sys.argv[2:4]
        raw, head, groups, blocks, cols, frames = read_cert(src)
        gens, hgens = claimed_generators()
        G = closure(gens)
        assert len(G) == 288
        remaining, reps, sizes = set(blocks), [], []
        while remaining:
            b = min(remaining)
            orb = {image(e, b) for e in G}
            assert orb <= remaining, 'block set is not invariant under the claimed group'
            remaining -= orb
            reps.append(b)
            sizes.append(len(orb))
        seed = {'source': src, 'source_sha256': hashlib.sha256(raw).hexdigest(), 'comment': head, 'groups': groups,
                'generators': gens, 'frame_generators': hgens, 'block_representatives': reps,
                'classes_at_0': cols[0], 'block_orbit_sizes': dict(Counter(sizes))}
        rebuilt, _, _, b2, c2, f2 = regenerate(seed)
        assert b2 == blocks and c2 == cols and f2 == frames, 'claimed action does not reproduce raw sections'
        assert rebuilt == raw, 'byte mismatch after seed regeneration'
        # Negative action control, independent of the producer: swap labels 0 and 1.
        transposition = list(range(V))
        transposition[0], transposition[1] = 1, 0
        assert any(image(transposition, B) not in blocks for B in blocks), 'transposition unexpectedly an automorphism'
        seed['action_negative_control'] = 'transposition (0 1) fails block invariance as required'
        seed['byte_identical_regeneration'] = True
        with xopen(out) as fh:
            json.dump(seed, fh, indent=1)
        print(json.dumps({'mode': 'make', 'seed': out, 'certificate_sha256': seed['source_sha256'],
                          'group_order': len(G), 'block_orbits': len(reps), 'orbit_sizes': dict(Counter(sizes)),
                          'byte_identical': True, 'negative_action_control': seed['action_negative_control']}))
    elif sys.argv[1] == 'expand':
        seed_path, out = sys.argv[2:4]
        seed = json.load(open(seed_path))
        raw, G, H, blocks, cols, frames = regenerate(seed)
        sha = hashlib.sha256(raw).hexdigest()
        assert sha == seed['source_sha256'], 'seed expansion SHA differs'
        with xopen(out, 'xb') as fh:
            fh.write(raw)
        print(json.dumps({'mode': 'expand', 'output': out, 'sha256': sha, 'blocks': len(blocks),
                          'group_order': len(G), 'frame_kernel_order': len(H)}))
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
