"""Parent intended-reason mutations and symmetry audit for the pinned mcDSQS(38) certificate.
Symmetry is informational (the definition assumes none); acceptance rests on check_mcdsqs_independent.py."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CERT = HERE / 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
CERT_SHA = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
CHECKER = HERE / 'check_mcdsqs_independent.py'
OUT = HERE / 'mcdsqs38-parent-controls-v1'
V = 38


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse(text):
    lines = text.rstrip('\n').split('\n')
    data = [i for i, l in enumerate(lines) if not l.startswith('#')]
    blocks_at = lines.index('BLOCKS') + 1
    blocks = [frozenset(map(int, lines[i].split())) for i in range(blocks_at, blocks_at + V * (V - 1) * (V - 2) // 24)]
    colourings, x, j = {}, None, None
    for i in range(blocks_at + len(blocks), len(lines)):
        l = lines[i]
        if l.startswith('POINT'):
            x = int(l.split()[1]); colourings[x] = []
        elif l.startswith('CLASS'):
            colourings[x].append([])
        elif l and not l.startswith('#'):
            colourings[x][-1].append((i, frozenset(map(int, l.split()))))
    return lines, blocks, colourings


def mutations(text):
    lines, blocks, col = parse(text)
    blocks_at = lines.index('BLOCKS') + 1
    out = {}
    def put(name, new, intended):
        out[name] = ('\n'.join(new) + '\n', intended)
    m = list(lines)
    a, b = lines[blocks_at].split(), lines[blocks_at + 1].split()
    pa, pb = list(map(int, a)), list(map(int, b))
    i = next(i for i in range(4) if pa[i] not in pb and pb[i] not in pa)
    pa[i], pb[i] = pb[i], pa[i]
    m[blocks_at], m[blocks_at + 1] = ' '.join(map(str, sorted(pa))), ' '.join(map(str, sorted(pb)))
    put('swap-points-between-blocks', m, '3-subset')
    m = list(lines); m[blocks_at + 2] = lines[blocks_at + 3]
    put('duplicate-block', m, 'duplicate block')
    m = list(lines); m[lines.index('COLOURS 19')] = 'COLOURS 18'
    put('colours-18', m, 'counting lower bound')
    m = list(lines); m[lines.index('COLOURS 19')] = 'COLOURS 20'
    put('colours-20', m, 'counting lower bound')
    # move a triple between two size-12 classes of point 0: 13 disjoint triples cannot fit in 37 points
    full = [c for c in col[0] if len(c) == 12]
    line_idx, _ = full[0][0]
    target_idx, _ = full[1][0]
    m = list(lines); moved = m.pop(line_idx)
    m.insert(target_idx - 1 if target_idx > line_idx else target_idx, moved)
    put('move-triple-to-other-class', m, 'not a partial parallel class')
    # drop one triple at point 5
    m = list(lines); del m[col[5][3][0][0]]
    put('drop-derived-triple', m, 'does not use every derived triple')
    p0 = lines.index('POINT 0'); p1 = lines.index('POINT 1')
    h18 = p0 + lines[p0:p1].index('CLASS 18')
    # merge class 18 into class 17 at point 0 by deleting the CLASS 18 header (18 triples > 12)
    m = list(lines); del m[h18]
    put('merge-last-two-classes', m, 'not a partial parallel class')
    # drop class 18 at point 0 entirely (header and triples)
    m = lines[:h18] + lines[p1:]
    put('drop-last-class', m, 'missing or out-of-order CLASS 18')
    # replace a triple {a,b,c} at point 3 by {missed,b,c}: still disjoint inside its class, not derived
    cls = next(c for c in col[3] if len(c) == 12)
    covered = set().union(*[t for _, t in cls])
    missed = (set(range(V)) - {3} - covered).pop()
    idx, t = cls[0]
    a0, b0, c0 = sorted(t)
    m = list(lines); m[idx] = ' '.join(map(str, sorted([missed, b0, c0])))
    put('non-derived-triple', m, 'not a derived triple')
    return out


def symmetry(text):
    _, blocks, col = parse(text)
    gens = {'y+2': [(y + 2) % V for y in range(V)], '3y+1': [(3 * y + 1) % V for y in range(V)]}
    group = {tuple(range(V))}
    frontier = [tuple(range(V))]
    while frontier:
        new = []
        for g in frontier:
            for h in gens.values():
                gh = tuple(h[g[y]] for y in range(V))
                if gh not in group:
                    group.add(gh); new.append(gh)
        frontier = new
    block_set = set(blocks)
    image = lambda g, s: frozenset(g[y] for y in s)
    invariant = all({image(g, b) for b in block_set} == block_set for g in gens.values())
    orbits, seen = {}, set()
    for b in block_set:
        if b in seen:
            continue
        orb = {image(g, b) for g in group}
        seen |= orb
        orbits[len(orb)] = orbits.get(len(orb), 0) + 1
    classes = {x: frozenset(frozenset(t for _, t in c) for c in cs) for x, cs in col.items()}
    stab = [g for g in group if g[0] == 0]
    stab_invariant = all(frozenset(frozenset(image(g, t) for t in c) for c in classes[0]) == classes[0] for g in stab)
    transported = all(any(g[0] == x and frozenset(frozenset(image(g, t) for t in c) for c in classes[0]) == classes[x]
                          for g in group) for x in range(V))
    return {'group_order': len(group), 'generators': list(gens), 'block_set_invariant_under_generators': invariant,
            'block_orbit_lengths': {str(k): n for k, n in sorted(orbits.items())},
            'stabilizer_of_0_order': len(stab), 'colouring_at_0_invariant_under_stabilizer': stab_invariant,
            'every_colouring_is_a_group_image_of_colouring_at_0': transported}


def main():
    OUT.mkdir(exist_ok=False)
    result = {'started_at_pt': stamp(), 'status': 'FAILED', 'driver_sha256': sha(__file__), 'checker_sha256': sha(CHECKER)}
    try:
        if sha(CERT) != CERT_SHA:
            raise ValueError('pin')
        text = CERT.read_text()
        controls = []
        for name, (mtext, intended) in mutations(text).items():
            path = OUT / (name + '.txt'); path.write_text(mtext)
            receipt = OUT / (name + '.json')
            p = subprocess.run([sys.executable, '-B', str(CHECKER), str(path), str(V), sha(path), str(receipt)],
                               capture_output=True, text=True, timeout=900)
            rec = json.loads(receipt.read_text())
            ok = p.returncode == 1 and rec['status'] == 'INVALID' and intended in rec['reason']
            controls.append({'name': name, 'returncode': p.returncode, 'reason': rec.get('reason'), 'intended': intended, 'intended_reason': ok})
            print(controls[-1], flush=True)
        result['mutations'] = controls
        result['symmetry'] = symmetry(text)
        print(result['symmetry'])
        if not all(c['intended_reason'] for c in controls):
            raise ValueError('mutation not rejected for intended reason')
        result['status'] = 'PARENT_MUTATIONS_PASS_AND_SYMMETRY_AUDITED'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = stamp()
        with (OUT / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2); f.write('\n')
        print(result['status'], result.get('error'))
    return 0 if result['status'].endswith('AUDITED') else 1


if __name__ == '__main__':
    raise SystemExit(main())
