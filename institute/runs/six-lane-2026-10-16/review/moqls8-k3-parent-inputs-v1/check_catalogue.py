"""Parent K3 catalogue check before certificate replay. No search/solver.
Pins the two classical-square source catalogues and encoders. Strictly parses all declared source squares;
validates each pair as 2-MOLS(8); normalizes first rows; canonically labels all 2165 incidence graphs with
nauty labelg, independently of the worker's pynauty code. With Egan-Wanless Table6's count 2165, local validity
and distinctness give coverage independently of the archive's authenticity.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
LABELG = Path('/opt/homebrew/Cellar/nauty/2.9.3/bin/labelg')
EXPECTED_ENCODERS = {'code/enc8_a2.py': '175badf04283b0bff461c250d8cfca40a8fa6575daeb154d8264de9d46262f31',
                     'code/enc8_b2.py': '087a26e3e595bcca55303e4bb38068909b66bb0b9527e1a81551a936ab31d474'}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def parse_source(p):
    lines = p.read_text().split('\n')
    head = lines[0].split()
    n, k, m = map(int, head[:3])
    if (n, k) != (8, 8) or m % 2:
        raise ValueError('source header')
    rows = [line.strip() for line in lines[1:] if line.strip()]
    if len(rows) != m * 8 or any(len(r) != 8 or any(c not in 'abcdefgh' for c in r) for r in rows):
        raise ValueError('source data not exactly all declared squares')
    squares = [[[ord(c) - 97 for c in r] for r in rows[i * 8:(i + 1) * 8]] for i in range(m)]
    return [squares[i:i + 2] for i in range(0, m, 2)]


def latin(L):
    return all(sorted(r) == list(range(8)) for r in L) and all(sorted(L[i][j] for i in range(8)) == list(range(8)) for j in range(8))


def orth(L, M):
    return len({(L[i][j], M[i][j]) for i in range(8) for j in range(8)}) == 64


def normalize(L):
    perm = {x: j for j, x in enumerate(L[0])}
    return [[perm[x] for x in row] for row in L]


def graph6_net(pair):
    # Point vertices 0..63; row, column, square1, square2 line vertices 64..95.
    edges = set()
    for i in range(8):
        for j in range(8):
            p = i * 8 + j
            for line in (64 + i, 72 + j, 80 + pair[0][i][j], 88 + pair[1][i][j]):
                edges.add((p, line))
    n = 96
    bits = [int((i, j) in edges) for j in range(1, n) for i in range(j)]
    while len(bits) % 6:
        bits.append(0)
    out = ['~'] + [chr(((n >> s) & 63) + 63) for s in (12, 6, 0)]
    for t in range(0, len(bits), 6):
        v = 0
        for b in bits[t:t + 6]:
            v = 2 * v + b
        out.append(chr(63 + v))
    return ''.join(out)


def canon(graphs):
    r = subprocess.run([str(LABELG), '-q'], input=''.join(g + '\n' for g in graphs).encode(), capture_output=True)
    if r.returncode:
        raise ValueError('labelg failed: ' + r.stderr.decode('utf-8', 'replace'))
    out = [x for x in r.stdout.decode().split('\n') if x]
    if len(out) != len(graphs):
        raise ValueError('labelg output coverage')
    return out


def main():
    inputs = HERE / 'inputs'
    inputs.mkdir(exist_ok=False)
    rec = {'started': now(), 'files': {}, 'labelg_sha256': sha(LABELG)}
    files = list(EXPECTED_ENCODERS) + ['code/run_fixed_k3.py', 'code/ew_nets2.py', 'evidence/k3_fixed/ew_nets2.json',
                                    'sources/ew_data/maxMOLS8.2.txt', 'sources/ew_data/nmaxMOLS8.2.txt',
                                    'sources/1406.3681v2.layout.txt']
    for rel in files:
        src, dst = LANE / rel, inputs / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        h = sha(src)
        r = subprocess.run(['cp', '-c', str(src), str(dst)], capture_output=True, text=True)
        if r.returncode or sha(dst) != h:
            raise ValueError('pin mismatch ' + rel)
        if rel in EXPECTED_ENCODERS and h != EXPECTED_ENCODERS[rel]:
            raise ValueError('encoder differs from K2-reviewed bytes: ' + rel)
        rec['files'][rel] = h
    nets = []
    source_counts = {}
    for kind in ('max', 'nmax'):
        pairs = parse_source(inputs / ('sources/ew_data/%sMOLS8.2.txt' % kind))
        source_counts[kind] = len(pairs)
        for idx, pair in enumerate(pairs):
            if not all(latin(L) for L in pair) or not orth(*pair):
                raise ValueError('source pair is not 2-MOLS(8): ' + kind + str(idx))
            nets.append({'tag': '%s%04d' % (kind, idx), 'squares': [normalize(L) for L in pair]})
    c = canon([graph6_net(item['squares']) for item in nets])
    rec['source_counts'] = source_counts
    rec['valid_pairs'] = len(nets)
    rec['distinct_net_classes'] = len(set(c))
    rec['worker_tags_equal'] = sorted(json.loads((inputs / 'evidence/k3_fixed/ew_nets2.json').read_text())['nets']) == sorted(x['tag'] for x in nets)
    # Relabel rows/columns and exchange the two squares. Net class must be unchanged.
    p = nets[42]['squares']
    pc = [[[L[(i + 3) % 8][7 - j] for j in range(8)] for i in range(8)] for L in reversed(p)]
    rec['relabel_control'] = canon([graph6_net(pc)])[0] == c[42]
    mutant = [[r[:] for r in L] for L in p]
    mutant[0][0][0] = mutant[0][0][1]
    rec['mutation_rejected'] = not latin(mutant[0])
    rec['row0_identity'] = all(L[0] == list(range(8)) for item in nets for L in item['squares'])
    with open(HERE / 'nets.json', 'x') as f:
        json.dump(nets, f)
        f.write('\n')
    rec['nets_sha256'] = sha(HERE / 'nets.json')
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if (len(nets) == 2165 and len(set(c)) == 2165 and rec['worker_tags_equal']
                                and rec['relabel_control'] and rec['mutation_rejected'] and rec['row0_identity']) else 'FAIL'
    with open(HERE / 'catalogue-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({k: rec[k] for k in ('source_counts', 'valid_pairs', 'distinct_net_classes', 'worker_tags_equal', 'verdict')}))


if __name__ == '__main__':
    main()
