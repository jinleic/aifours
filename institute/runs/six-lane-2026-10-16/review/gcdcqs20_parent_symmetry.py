"""Parent symmetry audit (informational; validity rests on check_gcdcqs_parent.py) for the pinned gcDCQS(20^4:0)
certificates. Points are 20*g + a. Tests all 480 maps (g, a) -> (sigma(g), a + c mod 20), sigma in S4, c in Z20, on
the block set; for the stabiliser, also tests whether the colouring at each point x is the image (as a set of classes,
and with class labels) of the colouring at 0 under some stabiliser element sending 0 to x. Negative control: a
transposition of two points must not preserve the block set.
Usage: python3 -B gcdcqs20_parent_symmetry.py OUT.json
"""
from datetime import datetime
from itertools import permutations
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PIN = HERE / 'gcdcqs20-parent-inputs-v1'
CERTS = {'A': ('gcdcqs20-e1s1_p10.txt', '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca'),
         'B': ('gcdcqs20-e1s0_p10.txt', '52c13d6aa5f1acf8cc6ca5e0bb27894263443ce6486e4007afeea41c2c60d0f8')}


def parse(path, want):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != want:
        raise SystemExit('hash mismatch ' + path.name)
    lines = [l for l in data.decode('ascii').split('\n') if l and not l.startswith('#')]
    groups = [list(map(int, lines[lines.index('GROUPS') + 1 + i].split())) for i in range(4)]
    if groups != [list(range(20 * g, 20 * g + 20)) for g in range(4)]:
        raise SystemExit('groups are not the label ranges')
    b0 = lines.index('BLOCKS') + 1
    blocks, col, x = set(), {}, None
    i = b0
    while not lines[i].startswith('POINT'):
        blocks.add(frozenset(map(int, lines[i].split())))
        i += 1
    for l in lines[i:]:
        if l.startswith('POINT'):
            x = int(l.split()[1]); col[x] = []
        elif l.startswith('CLASS'):
            col[x].append(set())
        else:
            col[x][-1].add(frozenset(map(int, l.split())))
    return blocks, col


def mapping(sigma, c):
    return [20 * sigma[p // 20] + (p % 20 + c) % 20 for p in range(80)]


def even(perm):
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
    return inv % 2 == 0


def main():
    out = Path(sys.argv[1])
    report = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds'),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'designs': {}}
    designs = {}
    for name, (fn, want) in CERTS.items():
        blocks, col = parse(PIN / fn, want)
        designs[name] = blocks
        stab = []
        for sigma in permutations(range(4)):
            for c in range(20):
                f = mapping(sigma, c)
                if all(frozenset(f[p] for p in b) in blocks for b in blocks):
                    stab.append((sigma, c))
        orbit0 = sorted({mapping(s, c)[0] for s, c in stab})
        transport_sets = transport_labels = 0
        base = [frozenset(frozenset(t) for t in cls) for cls in col[0]]
        for x in range(80):
            ok_set = ok_lab = False
            for s, c in stab:
                f = mapping(s, c)
                if f[0] != x:
                    continue
                img = [frozenset(frozenset(f[p] for p in t) for t in cls) for cls in base]
                tgt = [frozenset(cls) for cls in col[x]]
                if set(img) == set(tgt):
                    ok_set = True
                if img == tgt:
                    ok_lab = True
            transport_sets += ok_set
            transport_labels += ok_lab
        swap = list(range(80)); swap[0], swap[1] = 1, 0
        neg = all(frozenset(swap[p] for p in b) in blocks for b in blocks)
        report['designs'][name] = {
            'certificate_sha256': want, 'stabiliser_order_in_S4xC20': len(stab),
            'stabiliser_sigmas_all_even': all(even(s) for s, _ in stab),
            'stabiliser_is_A4xC20': len(stab) == 240 and all(even(s) for s, _ in stab),
            'orbit_of_point_0_size': len(orbit0),
            'points_whose_colouring_is_an_image_of_point0_colouring_as_class_set': transport_sets,
            'points_whose_colouring_is_an_image_with_identical_class_labels': transport_labels,
            'negative_control_transposition_0_1_preserves_blocks': neg}
    report['shared_blocks_A_B'] = len(designs['A'] & designs['B'])
    with out.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()
