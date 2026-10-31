#!/usr/bin/env python3
"""Independent exact checks for the frozen f70 written review; stdlib only."""
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
RECEIPT = HERE / 'receipt-v1.json'
MANIFEST_SHA = '58bc6ef69b3bba96616a5a96e19b64d685590380482d537f749c617df0e0661a'
COLOR = ({0: 3, 3: 2, 4: 0, 5: 1},
         {0: 3, 3: 0, 4: 2, 5: 1},
         {0: 3, 3: 0, 4: 2, 5: 1},
         {0: 3, 3: 2, 4: 1, 5: 0})
P_EQ6 = '0344 3505 4053 5430 0455 3034 4540 5303 0533 3350 4404 5045'.split()
P_PRIME_EQ6 = '0353 3530 4044 5405 0434 3055 4503 5340 0545 3304 4450 5033'.split()
I = ((1, 0), (0, 1))
X = ((0, 1), (1, 0))
Z = ((1, 0), (0, -1))
J = ((0, 1), (-1, 0))
Y = ((0, -1j), (1j, 0))
PAULIS = {'I': I, 'X': X, 'Z': Z, 'J': J}
CUTS = ((0, 1), (0, 2), (0, 3))


class CheckError(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckError(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parity(values):
    return sum(a > b for n, a in enumerate(values) for b in values[n + 1:]) % 2


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def scale(a, k):
    return tuple(tuple(k * z for z in row) for row in a)


def plus(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def parse_table(data):
    lines = data.decode('utf-8').splitlines()
    require(len(lines) == 38 and all(s.startswith('#') for s in lines[:2]), 'table headers or line count')
    e, p = {}, set()
    pat = re.compile(r'([0-5]) ([0-5]) ([+\-s][0-5][0-5])(?: ([+\-][0-5][0-5]))?')
    for n, line in enumerate(lines[2:]):
        m = pat.fullmatch(line)
        require(m is not None, 'malformed table row')
        a, b, first, second = m.groups()
        require((int(a), int(b)) == divmod(n, 6), 'table row order')
        require((first[0] == 's') == (second is None), 'bad table coefficient encoding')
        for token in (first,) if second is None else (first, second):
            coord = (int(a), int(b), int(token[1]), int(token[2]))
            require(coord not in e and coord not in p, 'duplicate table coordinate')
            if token[0] == 's':
                p.add(coord)
            else:
                e[coord] = 1 if token[0] == '+' else -1
    require(len(e) == 48 and len(p) == 12, 'E/P counts')
    return e, p


def physical(words):
    require(all(re.fullmatch(r'[0-5]{4}', w) for w in words), 'physical tuple encoding')
    return {tuple(map(int, w)) for w in words}


def colored(terms):
    try:
        return {tuple(COLOR[i][x[i]] for i in range(4)) for x in terms}
    except KeyError as exc:
        raise CheckError('non-K P coordinate') from exc


def check_parity(terms, wanted):
    colors = colored(terms)
    target = {s for s in itertools.permutations(range(4)) if parity(s) == wanted}
    require(len(terms) == 12 and colors == target, 'P parity class mismatch')
    return colors


def check_e_blocks(e):
    blocks = {}
    for coord, coefficient in e.items():
        active = tuple(i for i in range(4) if coord[i] in (1, 2))
        require(len(active) == 2, 'E has other than two H positions')
        spectator = tuple(i for i in range(4) if i not in active)
        g, h = (COLOR[i][coord[i]] for i in spectator)
        require(g == h, 'E spectator color mismatch')
        key = active + (g,)
        q = blocks.setdefault(key, [[0, 0], [0, 0]])
        r, c = (coord[i] - 1 for i in active)
        require(q[r][c] == 0, 'duplicate E matrix entry')
        q[r][c] = coefficient
    require(len(blocks) == 24, 'wrong E block count')
    counts = {}
    for pair in itertools.combinations(range(4), 2):
        names = []
        for g in range(4):
            q = tuple(map(tuple, blocks[pair + (g,)]))
            hits = [name for name, candidate in PAULIS.items()
                    if q in (candidate, scale(candidate, -1))]
            require(len(hits) == 1, 'E block is not a signed Pauli')
            names.append(hits[0])
        require(set(names) == set(PAULIS), 'E Pauli labels are not complete')
        counts[''.join(map(str, pair))] = names
    return counts


def check_e_gram(e):
    result = {}
    for out in CUTS:
        inp = tuple(i for i in range(4) if i not in out)
        m = [[0] * 36 for _ in range(36)]
        for coord, sign in e.items():
            r = 6 * coord[out[0]] + coord[out[1]]
            c = 6 * coord[inp[0]] + coord[inp[1]]
            m[r][c] = sign
        def is_classical(index, pair):
            a, b = divmod(index, 6)
            return a in COLOR[pair[0]] and b in COLOR[pair[1]] and COLOR[pair[0]][a] != COLOR[pair[1]][b]
        row_active = {r for r in range(36) if not is_classical(r, out)}
        col_active = {c for c in range(36) if not is_classical(c, inp)}
        require(len(row_active) == len(col_active) == 24, 'wrong E active dimension')
        require(all((r in row_active) == any(m[r]) for r in range(36)), 'E row occupancy')
        require(all((c in col_active) == any(m[r][c] for r in range(36)) for c in range(36)), 'E column occupancy')
        for r in range(36):
            for s in range(36):
                gram = sum(m[r][c] * m[s][c] for c in range(36))
                require(gram == (2 if r == s and r in row_active else 0), 'E row Gram mismatch')
                gram_t = sum(m[c][r] * m[c][s] for c in range(36))
                require(gram_t == (2 if r == s and r in col_active else 0), 'E column Gram mismatch')
        result[''.join(map(str, out))] = {'active_rows': len(row_active), 'active_columns': len(col_active),
                                          'row_and_column_gram_entries': 2 * 36 * 36}
    return result


def check_p_monomial(terms):
    result = {}
    for out in CUTS:
        inp = tuple(i for i in range(4) if i not in out)
        rows = {(x[out[0]], x[out[1]]) for x in terms}
        cols = {(x[inp[0]], x[inp[1]]) for x in terms}
        row_target = {(a, b) for a in COLOR[out[0]] for b in COLOR[out[1]]
                      if COLOR[out[0]][a] != COLOR[out[1]][b]}
        col_target = {(a, b) for a in COLOR[inp[0]] for b in COLOR[inp[1]]
                      if COLOR[inp[0]][a] != COLOR[inp[1]][b]}
        require(len(terms) == 12 and rows == row_target and cols == col_target, 'P monomial support mismatch')
        result[''.join(map(str, out))] = {'rows': len(rows), 'columns': len(cols)}
    return result


def permitted(mask, permutations):
    return all(sum(bool(mask[i] & (1 << p[i])) for i in range(4)) not in (2, 3)
               for p in permutations)


def check_masks(permutations):
    found = {m for m in itertools.product(range(1, 16), repeat=4) if permitted(m, permutations)}
    expected = {tuple([1 << g] * 4) for g in range(4)}
    expected |= {tuple(1 << g for g in p) for p in permutations}
    expected.add((15, 15, 15, 15))
    require(found == expected, 'support mask classification mismatch')
    return len(found)


def check_propagation():
    perms = [(1, 3, 2, 0), (1, 2, 0, 3), (3, 2, 1, 0), (3, 1, 0, 2),
             (2, 3, 0, 1), (2, 0, 1, 3), (2, 1, 3, 0)]
    sets = [{0, 1}, {1}, {2}, {3}]
    before = []
    for p in perms:
        require(parity(p) == 0, 'propagation tuple not even')
        hits = sum(p[i] in sets[i] for i in range(4))
        require(hits >= 2, 'propagation step not forced')
        before.append(hits)
        for i in range(4):
            sets[i].add(p[i])
    require(all(s == set(range(4)) for s in sets), 'propagation not full')
    return before


def check_connected(permutations):
    vertices = set(itertools.product(range(4), repeat=2))
    adj = {v: set() for v in vertices}
    for perm in permutations:
        for i, j in itertools.combinations(range(4), 2):
            a, b = (i, perm[i]), (j, perm[j])
            adj[a].add(b)
            adj[b].add(a)
    reached, stack = set(), [(0, 0)]
    while stack:
        v = stack.pop()
        if v not in reached:
            reached.add(v)
            stack.extend(adj[v] - reached)
    require(reached == vertices, 'probability co-occurrence graph disconnected')
    return {'vertices': len(vertices), 'undirected_edges': sum(map(len, adj.values())) // 2}


def check_pauli_algebra():
    zero = ((0, 0), (0, 0))
    for a, b, c in itertools.combinations(PAULIS.values(), 3):
        left, right = matmul(transpose(a), b), matmul(transpose(a), c)
        require(plus(matmul(left, right), matmul(right, left)) == zero, 'Pauli triple does not anticommute')
    expected = {'I': (1, 1, 1), 'X': (1, -1, -1), 'Z': (-1, -1, 1), 'J': (-1, 1, -1)}
    for name, q in PAULIS.items():
        observed = []
        for sigma in (X, Y, Z):
            transformed = matmul(matmul(q, sigma), transpose(q))
            matches = [sgn for sgn in (-1, 1) if transformed == scale(sigma, sgn)]
            require(len(matches) == 1, 'Pauli conjugation not a sign')
            observed.append(matches[0])
        require(tuple(observed) == expected[name], 'Bloch sign table mismatch')
    return {'anticommuting_triples': 4, 'Q_sigma_Q_dagger_signs': expected,
            'complex_conjugation_Bloch_signs': (1, -1, 1)}


def expect_failure(fn, expected):
    try:
        fn()
    except CheckError as exc:
        require(str(exc) == expected, 'control failed for unexpected reason: ' + str(exc))
        return str(exc)
    raise CheckError('control unexpectedly accepted: ' + expected)


def main():
    require(not RECEIPT.exists(), 'refusing to overwrite receipt')
    manifest_bytes = MANIFEST.read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'manifest hash mismatch')
    manifest = json.loads(manifest_bytes)
    records, input_bytes = [], []
    for item in manifest['inputs_in_read_order']:
        raw = Path(item['path']).read_bytes()
        require(sha(raw) == item['sha256'], 'input hash mismatch: ' + item['path'])
        require(len(raw) == item['bytes'] and raw.count(b'\n') == item['LF'], 'input size or LF mismatch')
        input_bytes.append(raw)
        records.append({'path': item['path'], 'sha256': sha(raw), 'bytes': len(raw), 'LF': raw.count(b'\n')})
    e, p = parse_table(input_bytes[0])
    require(p == physical(P_EQ6), 'P disagrees with transcribed public Eq6')
    p_prime = physical(P_PRIME_EQ6)
    require(len(p_prime) == 12 and p.isdisjoint(p_prime), 'P prime count or overlap')
    even = check_parity(p, 0)
    odd = check_parity(p_prime, 1)
    eblocks = check_e_blocks(e)
    gram = check_e_gram(e)
    monomial = {'P': check_p_monomial(p), 'P_prime': check_p_monomial(p_prime)}
    masks = {'even_accepted': check_masks(even), 'odd_accepted': check_masks(odd), 'tested_per_parity': 15 ** 4}
    graph = {'even': check_connected(even), 'odd': check_connected(odd)}
    algebra = check_pauli_algebra()
    controls = {}
    controls['deleted_P'] = expect_failure(lambda: check_parity(set(sorted(p)[1:]), 0), 'P parity class mismatch')
    flipped = dict(e)
    first = sorted(flipped)[0]
    flipped[first] *= -1
    controls['flipped_E_sign_coordinate'] = ''.join(map(str, first))
    controls['flipped_E_sign'] = expect_failure(lambda: check_e_gram(flipped), 'E row Gram mismatch')
    bad_mask = (1, 2, 4, 4)
    require(not permitted(bad_mask, even), 'inconsistent mask control accepted')
    controls['three_hits_mask'] = {'mask': bad_mask, 'rejected': True}
    checker_sha = sha(Path(__file__).read_bytes())
    clock = subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], check=True, capture_output=True, text=True).stdout.strip()
    receipt = {'kind': 'INDEPENDENT_EXACT_TARGETED_CHECK_NOT_COMPLEX_PROOF',
               'observed_native_clock_before_receipt_write': clock,
               'manifest_sha256': sha(manifest_bytes), 'inputs': records,
               'checker_path': str(Path(__file__).resolve()), 'checker_sha256': checker_sha,
               'public_source_note': 'Eq6 tuple literals were independently transcribed from the public HTML; the HTML itself is not included in this receipt.',
               'table_coefficients': {'E_signed_terms': len(e), 'P_sqrt2_terms': len(p)},
               'E_block_Pauli_labels_by_color': eblocks, 'E_exact_gram': gram,
               'P_and_P_prime_monomial': monomial, 'support_masks': masks,
               'probability_graph': graph, 'seven_step_propagation_hit_counts': check_propagation(),
               'pauli_algebra': algebra, 'negative_controls': controls,
               'limits': ['No sampled or finite-field computation proves the universal complex theorem.',
                          'The source-P tuple transcription is not a machine fetch of the public page.',
                          'This checker is not a human, formal-kernel, cross-model, or novelty review.']}
    with RECEIPT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print('PASS independent exact structural, mask, propagation, Pauli-algebra and intended-failure checks')
    print('receipt:', RECEIPT)
    print('checker SHA256:', checker_sha)
    print('observed native clock:', clock)


if __name__ == '__main__':
    main()
