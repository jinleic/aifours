#!/usr/bin/env python3
"""Direct sums and universal local circuit audit; no producing code imports."""
import argparse
from collections import Counter
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]


def literal(v, env):
    if isinstance(v, bool):
        return v
    return env[abs(v)] if v > 0 else not env[abs(v)]


def inverse(v):
    return not v if isinstance(v, bool) else -v


def exact_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, list):
        return len(a) == len(b) and all(exact_equal(x, y) for x, y in zip(a, b))
    return a == b


def direct(bits):
    return [sum(1 - 2 * (b ^ ((a & x).bit_count() & 1)) for x, b in enumerate(bits)) for a in range(512)]


def transform(signs):
    a = list(signs)
    for bit in range(9):
        stride = 1 << bit
        for i in range(512):
            if i & stride:
                continue
            u, v = a[i], a[i | stride]
            a[i], a[i | stride] = u + v, u - v
    return a


def check_table(text, reported=None):
    assert len(text) == 512 and set(text) <= {'0', '1'}
    bits = list(map(int, text))
    W = direct(bits)
    assert W == transform([1 - 2 * b for b in bits])
    if reported is not None:
        assert W == reported, 'corrupted spectrum'
    s = 0
    for x, b in enumerate(bits):
        if b:
            s ^= x
    w = sum(bits)
    if w % 2 == 0:
        for a, v in enumerate(W):
            assert v % 8 == (-2 * w + 4 * ((a & s).bit_count() & 1)) % 8
        assert sum(v % 8 == 0 for v in W) == (256 if s else (512 if w % 4 == 0 else 0))
    return {'weight': w, 'support_xor': s, 'peak': max(map(abs, W)), 'nonlinearity': 256 - max(map(abs, W)) // 2,
            'walsh_zero_indices': [a for a, v in enumerate(W) if v == 0], 'walsh_0_mod8_count': sum(v % 8 == 0 for v in W),
            'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest(), 'walsh': W}


def permutation(x, p):
    return sum(((x >> i) & 1) << p[i] for i in range(9))


def audit_orbits(data):
    answer = {}
    rotation = [(i + 3) % 9 for i in range(9)]
    rotation2 = [(i + 6) % 9 for i in range(9)]
    reversal = [8 - i for i in range(9)]
    for kind, cls in data['classes'].items():
        expected = []
        used = set()
        for x in range(512):
            if x in used:
                continue
            orb = {x}
            if kind != 'unrestricted':
                orb |= {permutation(x, rotation), permutation(x, rotation2)}
            if kind == '3-dsbf':
                orb |= {permutation(y, reversal) for y in list(orb)}
            expected.append(sorted(orb))
            used |= orb
        assert expected == cls['orbits']
        assert len(expected) == {'3-dsbf': 104, '3-rsbf': 176, 'unrestricted': 512}[kind]
        assert sorted(x for orb in expected for x in orb) == list(range(512))
        assert cls['representatives'] == [o[0] for o in expected]
        assert cls['orbit_sizes'] == list(map(len, expected))
        ox = []
        for orb in expected:
            s = 0
            for x in orb:
                s ^= x
            ox.append(s)
        assert ox == cls['orbit_xors']
        where = {x: j for j, orb in enumerate(expected) for x in orb}
        for a in range(512):
            row = [sum((-1) ** ((a & x).bit_count() & 1) for x in orb) for orb in expected]
            assert row == cls['C'][where[a]], 'wrong or non-invariant orbit character matrix'
        matrix = ROOT / f'inputs/{kind}.matrix.txt'
        assert hashlib.sha256(matrix.read_bytes()).hexdigest() == cls['matrix_sha256']
        answer[kind] = {'orbit_count': len(expected), 'all512_character_rows_checked': True,
                        'orbit_size_histogram': dict(Counter(map(len, expected)))}
    return answer


def eval_local(v, free, gates, cache):
    if isinstance(v, bool):
        return v
    var = abs(v)
    if var in free:
        value = free[var]
    elif var in cache:
        value = cache[var]
    else:
        assert var in gates, ('unbound local gate leaf', var)
        g = gates[var]
        a = eval_local(g['a'], free, gates, cache)
        b = eval_local(g['b'], free, gates, cache)
        value = (a != b) if g['op'] == 'xor' else (a and b) if g['op'] == 'and' else (a or b)
        cache[var] = value
    return value if v > 0 else not value


def check_adder(a, A, B, subtract, gates):
    assert exact_equal(a['A'], A) and exact_equal(a['B'], B) and a['subtract'] is subtract
    assert len(a['steps']) == len(a['out']) == len(A) == len(B) == 11
    carry = bool(subtract)
    for j, (left, right, cin, out, cout) in enumerate(a['steps']):
        assert exact_equal(left, A[j]) and exact_equal(right, inverse(B[j]) if subtract else B[j])
        assert exact_equal(cin, carry) and exact_equal(out, a['out'][j])
        free_vars = sorted({abs(v) for v in (left, right, cin) if not isinstance(v, bool)})
        for choice in itertools.product((False, True), repeat=len(free_vars)):
            free = dict(zip(free_vars, choice))
            total = int(literal(left, free)) + int(literal(right, free)) + int(literal(cin, free))
            assert eval_local(out, free, gates, {}) == bool(total % 2), 'wrong full-adder sum'
            assert eval_local(cout, free, gates, {}) == bool(total >= 2), 'wrong full-adder carry'
        carry = cout
    return a['out']


def audit_circuit(cls, prefix, mutate=False):
    meta_raw = (ROOT / (prefix + '.encoding.json.gz')).read_bytes()
    meta = json.loads(gzip.decompress(meta_raw))
    rows = []
    sha = hashlib.sha256()
    with gzip.open(ROOT / (prefix + '.cnf.gz'), 'rb') as fh:
        for raw in fh:
            sha.update(raw)
            line = raw.decode().strip()
            if line.startswith('p '):
                _, typ, nv, nc = line.split()
                assert typ == 'cnf'
                nv, nc = int(nv), int(nc)
            elif line and not line.startswith('c'):
                vals = list(map(int, line.split()))
                assert vals[-1] == 0 and 0 not in vals[:-1]
                rows.append(vals[:-1])
    assert sha.hexdigest() == meta['cnf_sha256']
    assert len(rows) == nc == meta['clauses'] and nv == meta['variables']
    assert meta['primary_variables'] == list(range(1, 105)) and meta['word_width'] == 11
    if mutate:
        rows[0][0] *= -1
    gates = {}
    for offset, gate in enumerate(meta['gates']):
        z = gate['out']
        assert z == 105 + offset and gate['op'] in ('xor', 'and', 'or')
        assert all(not isinstance(v, bool) and abs(v) < z for v in (gate['a'], gate['b']))
        assert abs(gate['a']) != abs(gate['b'])
        first = 4 * offset
        assert first == gate['first_clause']
        block = rows[first:first + 4]
        assert len(block) == 4 and all(all(abs(v) in (abs(gate['a']), abs(gate['b']), z) for v in r) for r in block)
        variables = [abs(gate['a']), abs(gate['b']), z]
        for values in itertools.product((False, True), repeat=3):
            env = dict(zip(variables, values))
            av, bv = literal(gate['a'], env), literal(gate['b'], env)
            expected = (av != bv) if gate['op'] == 'xor' else (av and bv) if gate['op'] == 'and' else (av or bv)
            accepted = all(any(literal(v, env) for v in clause) for clause in block)
            assert accepted == (env[z] == expected), 'corrupt gate encoding'
        gates[z] = gate
    assert 104 + len(gates) == nv
    where = {x: j + 1 for j, orbit in enumerate(cls['orbits']) for x in orbit}
    words = [[True] + [where[x]] * 10 for x in range(512)]
    assert len(meta['layers']) == 9
    checked_steps = 0
    for bit, layer in enumerate(meta['layers']):
        stride = 1 << bit
        assert layer['stride'] == stride and len(layer['adders']) == 512
        new = [None] * 512
        pair_number = 0
        for i in range(512):
            if i & stride:
                continue
            j = i | stride
            new[i] = check_adder(layer['adders'][2 * pair_number], words[i], words[j], False, gates)
            new[j] = check_adder(layer['adders'][2 * pair_number + 1], words[i], words[j], True, gates)
            pair_number += 1
            checked_steps += 22
        assert exact_equal(new, layer['outputs'])
        words = new
    assert exact_equal(words, meta['outputs'])
    expected_requirements = []
    assert len(meta['comparators']) == 208
    for index, a in enumerate(cls['representatives']):
        biased = words[a][:-1] + [inverse(words[a][-1])]
        for side in range(2):
            comp = meta['comparators'][2 * index + side]
            cutoff = (1024 - meta['bound'] - 1) if side == 0 else (1024 + meta['bound'])
            assert exact_equal(comp['bits'], biased) and comp['cutoff'] == cutoff
            for value in range(2048):
                free = {}
                consistent = True
                for j, v in enumerate(biased):
                    target = bool(value >> j & 1)
                    if isinstance(v, bool):
                        if v != target:
                            consistent = False
                            break
                    else:
                        actual = target if v > 0 else not target
                        if abs(v) in free and free[abs(v)] != actual:
                            consistent = False
                            break
                        free[abs(v)] = actual
                if consistent:
                    assert eval_local(comp['out'], free, gates, {}) == (value <= cutoff), 'wrong comparator'
            expected_requirements.append([inverse(comp['out']) if side == 0 else comp['out']])
    memo_forms = {}
    def xor_form(v):
        if isinstance(v, bool):
            return int(v), 0
        var = abs(v)
        if var <= 104:
            c, m = 0, 1 << (var - 1)
        elif var in memo_forms:
            c, m = memo_forms[var]
        else:
            g = gates[var]
            assert g['op'] == 'xor', 'support-XOR expression is not a linear XOR circuit'
            ca, ma = xor_form(g['a'])
            cb, mb = xor_form(g['b'])
            c, m = ca ^ cb, ma ^ mb
            memo_forms[var] = (c, m)
        return c ^ int(v < 0), m
    sx = meta['support_xor_literals']
    for bit, v in enumerate(sx):
        expected_mask = sum(1 << j for j, x in enumerate(cls['orbit_xors']) if x >> bit & 1)
        assert xor_form(v) == (0, expected_mask)
    expected_requirements += [sx, [-1]]
    assert exact_equal(expected_requirements, meta['requirements'])
    physical = []
    for req in expected_requirements:
        if any(v is True for v in req):
            continue
        physical.append([v for v in req if not isinstance(v, bool)])
    assert rows[4 * len(gates):] == physical, 'extra or missing target clauses'
    def evaluate_model(text):
        bits = list(map(int, text))
        env = {}
        for j, orbit in enumerate(cls['orbits']):
            vals = {bits[x] for x in orbit}
            assert len(vals) == 1
            env[j + 1] = bool(vals.pop())
        for g in meta['gates']:
            av, bv = literal(g['a'], env), literal(g['b'], env)
            env[g['out']] = (av != bv) if g['op'] == 'xor' else (av and bv) if g['op'] == 'and' else (av or bv)
        assert all(any(literal(v, env) for v in clause) for clause in rows[:4 * len(gates)])
        failed = [i for i, req in enumerate(expected_requirements) if not any(literal(v, env) for v in req)]
        W = direct(bits)
        for a, word in enumerate(words):
            value = sum(int(literal(v, env)) << j for j, v in enumerate(word))
            signed = value if value < 1024 else value - 2048
            assert signed == W[a]
        return failed
    return {'variables': nv, 'clauses': nc, 'gates_all8_assignments_checked': len(gates),
            'adder_bit_steps_universally_checked': checked_steps, 'comparators_checked_all2048_words': 208,
            'cnf_sha256': meta['cnf_sha256'], 'bound': meta['bound']}, evaluate_model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt-spectrum', action='store_true')
    ap.add_argument('--corrupt-encoding', action='store_true')
    args = ap.parse_args()
    started = time.monotonic()
    raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    data = json.loads(gzip.decompress(raw))
    orbits = audit_orbits(data)
    seeds = []
    for seed in data['published_seeds']:
        text = seed['bits']
        audit = check_table(text)
        assert audit['support_xor'] == 0 and audit['weight'] % 4 == 2
        assert audit['peak'] == 28 and not audit['walsh_zero_indices'] and audit['walsh_0_mod8_count'] == 0
        assert all(v % 8 == 4 for v in audit['walsh'])
        if args.corrupt_spectrum:
            W = audit['walsh'].copy()
            W[17] += 8
            check_table(text, W)
        seeds.append({'name': seed['name'], **{k: v for k, v in audit.items() if k != 'walsh'}})
    cnf_audit, eval28 = audit_circuit(data['classes']['3-dsbf'], 'results/3-dsbf-snonzero', args.corrupt_encoding)
    assert cnf_audit['bound'] == 28
    base = next(r['bits'] for r in data['published_seeds'] if r['name'] == 'dsbf40')
    failures = eval28(base)
    assert failures == [208], 'known bound28 model must fail exactly the nonzero-support-XOR target'
    relaxed_audit, eval32 = audit_circuit(data['classes']['3-dsbf'], 'results/control-bound32-snonzero')
    assert relaxed_audit['bound'] == 32
    planted = list(map(int, base))
    planted[0] ^= 1
    planted[511] ^= 1
    if planted[0]:
        planted = [b ^ 1 for b in planted]
    planted_text = ''.join(map(str, planted))
    pa = check_table(planted_text)
    assert pa['peak'] <= 32 and pa['support_xor'] == 511
    assert eval32(planted_text) == [], 'genuine bound32/nonzero-XOR model rejected by circuit'
    search = {}
    witnesses = []
    for kind in ('3-dsbf', '3-rsbf', 'unrestricted'):
        result = json.loads((ROOT / f'results/search-{kind}.json').read_text())
        cls = data['classes'][kind]
        text = ['?'] * 512
        assert len(result['best_orbit_bits']) == len(cls['orbits'])
        for j, orbit in enumerate(cls['orbits']):
            for x in orbit:
                text[x] = result['best_orbit_bits'][j]
        text = ''.join(text)
        checked = check_table(text)
        assert checked['support_xor'] == result['best_support_xor'] != 0
        assert checked['weight'] == result['best_weight'] and checked['weight'] % 2 == 0
        assert checked['peak'] == result['best_max_abs_W']
        assert [checked['walsh'][a] for a in cls['representatives']] == result['best_orbit_walsh']
        assert result['best_tail28'] == sum(max(0, abs(v) - 28) ** 2 for v in checked['walsh'])
        if result['status'] == 'FOUND':
            assert checked['peak'] <= 28
            candidate = {'kind': kind, 'bits': text, **checked}
            witnesses.append(candidate)
            if checked['walsh_zero_indices']:
                shift = checked['walsh_zero_indices'][0]
                balanced = ''.join(str(int(b) ^ ((x & shift).bit_count() & 1)) for x, b in enumerate(text))
                ba = check_table(balanced)
                assert ba['weight'] == 256 and ba['peak'] <= 28
                (ROOT / f'results/balanced-witness-{kind}.json').write_text(json.dumps({'bits': balanced, 'linear_shift': shift, **ba}, indent=2) + '\n')
        else:
            assert result['status'] == 'NON_FIND'
        search[kind] = {k: v for k, v in result.items() if k not in ('best_orbit_bits', 'best_orbit_walsh')}
    control = json.loads((ROOT / 'results/search-recovery-control.json').read_text())
    assert control['status'] == 'FOUND' and control['best_tail28'] == 0
    cls = data['classes']['3-dsbf']
    control_text = ['?'] * 512
    for j, orbit in enumerate(cls['orbits']):
        for x in orbit:
            control_text[x] = control['best_orbit_bits'][j]
    ca = check_table(''.join(control_text))
    assert ca['peak'] == 28
    assert ca['support_xor'] == control['best_support_xor'] == 0
    assert ca['weight'] == control['best_weight']
    exact = json.loads((ROOT / 'results/exact-run.json').read_text())
    assert exact['cnf_sha256'] == cnf_audit['cnf_sha256']
    exact_candidate = None
    if exact['solver_status'] == 'SAT':
        exact_candidate = check_table(exact['candidate_bits'])
        assert exact_candidate['peak'] <= 28 and exact_candidate['support_xor'] != 0
        assert eval28(exact['candidate_bits']) == []
    # Independently check the weighted-PB identity coefficient by coefficient,
    # then every possible integer total (not a sample of Boolean models).
    for row in data['classes']['3-dsbf']['C']:
        L = sum(map(abs, row))
        assert L - 2 * sum(-v for v in row if v < 0) == sum(row)
        assert [(-2 * abs(v) if v > 0 else 2 * abs(v)) for v in row] == [-2 * v for v in row]
        lo, hi = (L - 28 + 1) // 2, (L + 28) // 2
        assert all((lo <= total <= hi) == (abs(L - 2 * total) <= 28) for total in range(L + 1))
    native = json.loads((ROOT / 'results/native-pb-run.json').read_text())
    assert native['input_sha256'] == hashlib.sha256(raw).hexdigest()
    smt = gzip.decompress((ROOT / 'results/native-pb.smt2.gz').read_bytes())
    assert hashlib.sha256(smt).hexdigest() == native['smt_sha256']
    native_candidate = None
    if native['solver_status'] == 'SAT':
        text = native['candidate_bits']
        native_candidate = check_table(text)
        assert native_candidate['peak'] <= 28 and native_candidate['support_xor'] != 0
        assert eval28(text) == []
        witnesses.append({'kind': 'native-pb', 'bits': text, **native_candidate})
        if native_candidate['walsh_zero_indices']:
            shift = native_candidate['walsh_zero_indices'][0]
            balanced = ''.join(str(int(b) ^ ((x & shift).bit_count() & 1)) for x, b in enumerate(text))
            ba = check_table(balanced)
            assert ba['weight'] == 256 and ba['peak'] <= 28
            (ROOT / 'results/balanced-witness-native-pb.json').write_text(json.dumps({'bits': balanced, 'linear_shift': shift, **ba}, indent=2) + '\n')
    out = {'status': 'PASS', 'published_seed_mod8_audits': seeds, 'orbit_audits': orbits,
           'target_circuit_universal_audit': cnf_audit, 'relaxed_circuit_universal_audit': relaxed_audit,
           'controls': {'published_bound28_rejected_only_for_s0': True, 'planted_bound32_s511_passes_all_clauses': True,
                        'planted_bound32_bits': planted_text, 'heuristic_recovery_peak': ca['peak']},
           'searches': search, 'type_witnesses': witnesses, 'exact_solver_status': exact['solver_status'],
           'certified_negative_claim': False, 'exact_candidate': exact_candidate,
           'native_pb_status': native['solver_status'], 'native_pb_candidate': native_candidate,
           'native_pb_identity_all_totals_checked': True,
           'input_sha256': hashlib.sha256(raw).hexdigest(), 'checker_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started}
    (ROOT / 'results/check.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': out['status'], 'type_witness_count': len(witnesses), 'exact_solver_status': exact['solver_status'], 'elapsed_seconds': out['elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
