#!/usr/bin/env python3
"""Independent exact SMT-question audit and full-table controls; no producer imports."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import re
import time

ROOT = Path(__file__).resolve().parents[1]
PIN = '441e85e5289c34a15bc0caf5387cae77d9039da3a47efdbde9d429d5f7c91cbb'


def direct(bits):
    return [sum((1 - 2 * b) * (-1 if (a & x).bit_count() & 1 else 1) for x, b in enumerate(bits)) for a in range(512)]


def fwht(bits):
    W = [1 - 2 * b for b in bits]
    for bit in range(9):
        step = 1 << bit
        for i in range(512):
            if i & step:
                continue
            u, v = W[i], W[i | step]
            W[i], W[i | step] = u + v, u - v
    return W


def table(text, reported=None):
    assert len(text) == 512 and set(text) <= {'0', '1'}
    bits = list(map(int, text))
    W = direct(bits)
    assert W == fwht(bits)
    if reported is not None:
        assert W == reported, 'corrupt spectrum'
    sx = 0
    for x, b in enumerate(bits):
        if b:
            sx ^= x
    anf = bits.copy()
    for i in range(9):
        for x in range(512):
            if x >> i & 1:
                anf[x] ^= anf[x ^ (1 << i)]
    degree = max((x.bit_count() for x, b in enumerate(anf) if b), default=-1)
    return bits, W, {'weight': sum(bits), 'support_xor': sx, 'max_abs_W': max(map(abs, W)),
                     'degree': degree, 'nonlinearity': 256 - max(map(abs, W)) // 2,
                     'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest()}


def permute(x, destinations):
    return sum(((x >> i) & 1) << destination for i, destination in enumerate(destinations))


def group_audit(imported, decomposition):
    rotation = [(i + 3) % 9 for i in range(9)]
    reflection = [8 - i for i in range(9)]
    maps = [rotation, reflection]
    images = [[permute(1 << i, p) for i in range(9)] for p in maps]
    matrices = [[[int(p[col] == row) for col in range(9)] for row in range(9)] for p in maps]
    assert images == decomposition['generators_basis_images']
    assert matrices == decomposition['generator_matrices']
    fixed = [s for s in range(512) if all(permute(s, p) == s for p in maps)]
    assert fixed == decomposition['fixed_support_vectors_including_zero']
    assert fixed[1:] == decomposition['nonzero_types'] == [146, 365, 511]
    expected, used = [], set()
    for x in range(512):
        if x in used:
            continue
        three = {x, permute(x, rotation), permute(permute(x, rotation), rotation)}
        orbit = sorted(three | {permute(y, reflection) for y in three})
        expected.append(orbit)
        used |= set(orbit)
    cls = imported['classes']['3-dsbf']
    assert expected == cls['orbits'] and len(expected) == 104
    assert sorted(x for o in expected for x in o) == list(range(512))
    ox = []
    for orbit in expected:
        value = 0
        for x in orbit:
            value ^= x
        ox.append(value)
    assert ox == cls['orbit_xors']
    span = {0}
    for v in ox:
        span |= {s ^ v for s in span}
    assert sorted(span) == fixed == decomposition['orbit_xor_span']
    assert cls['orbit_sizes'] == list(map(len, expected))
    assert cls['representatives'] == [o[0] for o in expected]
    where = {a: j for j, orbit in enumerate(expected) for a in orbit}
    for a in range(512):
        coefficients = [sum((-1) ** ((a & x).bit_count() & 1) for x in orbit) for orbit in expected]
        assert coefficients == cls['C'][where[a]]
    return cls, fixed[1:]


def parse(text):
    tokens = re.findall(r'\(|\)|[^\s()]+', text)
    roots, stack = [], []
    for token in tokens:
        if token == '(':
            item = []
            if stack:
                stack[-1].append(item)
            else:
                roots.append(item)
            stack.append(item)
        elif token == ')':
            assert stack
            stack.pop()
        else:
            assert stack
            stack[-1].append(token)
    assert not stack
    return roots


def atom_form(expr):
    positive = True
    if isinstance(expr, list):
        assert len(expr) == 2 and expr[0] == 'not'
        positive, expr = False, expr[1]
    assert isinstance(expr, str) and re.fullmatch(r'x(?:0|[1-9][0-9]*)', expr)
    index = int(expr[1:])
    assert 0 <= index < 104
    return index, positive


def linear_pb(expr):
    assert isinstance(expr, list) and isinstance(expr[0], list)
    header = expr[0]
    assert header[0] == '_' and header[1] in ('pbge', 'pble', 'pbeq')
    weights = list(map(int, header[3:]))
    assert len(weights) == len(expr) - 1 and all(w > 0 for w in weights)
    constant, coefficients = 0, [0] * 104
    for w, atom in zip(weights, expr[1:]):
        i, positive = atom_form(atom)
        if positive:
            coefficients[i] += w
        else:
            constant += w
            coefficients[i] -= w
    return header[1], coefficients, int(header[2]) - constant


def xor_form(expr):
    if expr == 'false':
        return 0, 0
    if expr == 'true':
        return 1, 0
    if isinstance(expr, str):
        i, positive = atom_form(expr)
        assert positive
        return 0, 1 << i
    assert isinstance(expr, list)
    if expr[0] == 'not':
        c, m = xor_form(expr[1])
        return c ^ 1, m
    assert expr[0] == 'xor' and len(expr) == 3
    ca, ma = xor_form(expr[1])
    cb, mb = xor_form(expr[2])
    return ca ^ cb, ma ^ mb


def truth(expr, assignment):
    if expr == 'false':
        return False
    if expr == 'true':
        return True
    if isinstance(expr, str):
        i, positive = atom_form(expr)
        assert positive
        return bool(assignment[i])
    if isinstance(expr[0], list):
        op, coefficients, rhs = linear_pb(expr)
        value = sum(c * b for c, b in zip(coefficients, assignment))
        return value >= rhs if op == 'pbge' else value <= rhs if op == 'pble' else value == rhs
    if expr[0] == 'not':
        return not truth(expr[1], assignment)
    if expr[0] == 'xor':
        return truth(expr[1], assignment) != truth(expr[2], assignment)
    assert expr[0] == '=' and len(expr) == 3
    return truth(expr[1], assignment) == truth(expr[2], assignment)


def audit_question(path, s, bound, cls, mutation=None):
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    expressions = parse(raw.decode())
    assert expressions[0] == ['set-logic', 'QF_FD']
    assert expressions[1:105] == [['declare-fun', f'x{i}', [], 'Bool'] for i in range(104)]
    assert len(expressions) == 105 + 219
    assert all(len(e) == 2 and e[0] == 'assert' for e in expressions[105:])
    assertions = [e[1] for e in expressions[105:]]
    if mutation == 'encoding':
        # Alter a real nonzero-frequency PB coefficient, not a filename.
        head = assertions[2][0]
        head[4] = str(int(head[4]) + 1)
    if mutation == 'type':
        assertions[209][2] = 'false' if assertions[209][2] == 'true' else 'true'
    if mutation == 'balance':
        assertions[208][0][2] = '255'
    caps = []
    for j, (a, C) in enumerate(zip(cls['representatives'], cls['C'])):
        residue = 4 * ((a & s).bit_count() & 1)
        peak = bound - ((bound - residue) % 8)
        caps.append(peak)
        # Derive directly from W=sum C-2sum C*f; this is independent of
        # the producer's absolute-coefficient/negated-literal transform.
        c0 = sum(C)
        minimum = sum(c for c in C if c < 0)
        maximum = sum(c for c in C if c > 0)
        lower = max(minimum, (c0 - peak + 1) // 2)
        upper = min(maximum, (c0 + peak) // 2)
        assert linear_pb(assertions[2 * j]) == ('pbge', C, lower), 'corrupt Walsh/PB correspondence'
        assert linear_pb(assertions[2 * j + 1]) == ('pble', C, upper), 'corrupt Walsh/PB correspondence'
        # Every point in this frequency orbit has the same type cap.
        assert all((x & s).bit_count() % 2 == (a & s).bit_count() % 2 for x in cls['orbits'][j])
    assert linear_pb(assertions[208]) == ('pbeq', cls['orbit_sizes'], 256), 'corrupt exact-balance constraint'
    for bit in range(9):
        e = assertions[209 + bit]
        assert len(e) == 3 and e[0] == '='
        ca, ma = xor_form(e[1])
        cb, mb = xor_form(e[2])
        expected = sum(1 << j for j, v in enumerate(cls['orbit_xors']) if v >> bit & 1)
        assert (ma ^ mb, ca ^ cb) == (expected, (s >> bit) & 1), 'corrupt support-type constraint'
    assert assertions[218] == ['not', 'x0']
    return assertions, {'s': s, 'nominal_bound': bound, 'assertions_checked': len(assertions),
                        'frequency_orbit_cap_counts': dict(Counter(caps)),
                        'full512_cap_counts': dict(Counter({p: sum(len(o) for o, q in zip(cls['orbits'], caps) if q == p) for p in set(caps)})),
                        'smt_sha256': hashlib.sha256(raw).hexdigest(),
                        'compressed_smt_sha256': hashlib.sha256(compressed).hexdigest()}


def assignment_from_bits(bits, cls):
    orbit_bits = []
    for orbit in cls['orbits']:
        values = {bits[x] for x in orbit}
        assert len(values) == 1, 'model not dihedral-invariant'
        orbit_bits.append(values.pop())
    return orbit_bits


def equivalence_audit(cls, decomposition, questions):
    recorded = json.loads((ROOT / 'inputs/type-equivalence.json').read_text())
    assert recorded['input_sha256'] == PIN
    # Independent matrix-column construction, rather than the producer's
    # conditional point/dual formulas.
    columns = [(1 << i) ^ (365 if i in (1, 4, 7) else 0) for i in range(9)]
    def multiply(x):
        y = 0
        for i, column in enumerate(columns):
            if x >> i & 1:
                y ^= column
        return y
    def transpose_multiply(a):
        return sum(((a & column).bit_count() & 1) << i for i, column in enumerate(columns))
    point = [multiply(x) for x in range(512)]
    dual = [transpose_multiply(a) for a in range(512)]
    assert point == recorded['point_map'] and dual == recorded['dual_map']
    assert sorted(point) == sorted(dual) == list(range(512))
    rotation, reflection = [(i + 3) % 9 for i in range(9)], [8 - i for i in range(9)]
    for x in range(512):
        assert point[point[x]] == dual[dual[x]] == x
        assert multiply(permute(x, rotation)) == permute(multiply(x), rotation)
        assert multiply(permute(x, reflection)) == permute(multiply(x), reflection)
    for a in range(512):
        for x in range(512):
            assert (a & point[x]).bit_count() % 2 == (dual[a] & x).bit_count() % 2
    where = {x: i for i, orbit in enumerate(cls['orbits']) for x in orbit}
    primary = [where[point[o[0]]] for o in cls['orbits']]
    frequency = [where[dual[o[0]]] for o in cls['orbits']]
    assert primary == recorded['input_orbit_permutation']
    assert frequency == recorded['frequency_orbit_permutation']
    assert sorted(primary) == sorted(frequency) == list(range(104))
    for i, orbit in enumerate(cls['orbits']):
        assert sorted(point[x] for x in orbit) == cls['orbits'][primary[i]]
        assert sorted(dual[x] for x in orbit) == cls['orbits'][frequency[i]]
    for i in range(104):
        for j in range(104):
            assert cls['C'][i][j] == cls['C'][frequency[i]][primary[j]]
    assert point[146] == 511 and point[511] == 146 and point[365] == 365
    assert primary[0] == 0
    def rename_coefficients(coefficients):
        renamed = [0] * 104
        for j, c in enumerate(coefficients):
            renamed[primary[j]] += c
        return renamed
    def rename_mask(mask):
        return sum(1 << primary[j] for j in range(104) if mask >> j & 1)
    for i in range(104):
        for side in (0, 1):
            op, coefficients, rhs = linear_pb(questions[511][2 * i + side])
            assert (op, rename_coefficients(coefficients), rhs) == linear_pb(questions[146][2 * frequency[i] + side])
    op, coefficients, rhs = linear_pb(questions[511][208])
    assert (op, rename_coefficients(coefficients), rhs) == linear_pb(questions[146][208])
    old_forms = []
    for expr in questions[146][209:218]:
        ca, ma = xor_form(expr[1])
        cb, mb = xor_form(expr[2])
        old_forms.append((ca ^ cb, ma ^ mb))
    for bit, expr in enumerate(questions[511][209:218]):
        ca, ma = xor_form(expr[1])
        cb, mb = xor_form(expr[2])
        expected_rhs, expected_mask = 0, 0
        for i, column in enumerate(columns):
            if column >> bit & 1:
                expected_rhs ^= old_forms[i][0]
                expected_mask ^= old_forms[i][1]
        assert (ca ^ cb, rename_mask(ma ^ mb)) == (expected_rhs, expected_mask)
    assert questions[146][218] == questions[511][218] == ['not', 'x0']
    old_control = next(c for c in decomposition['controls'] if c['s'] == 146)
    moved = recorded['transformed_balanced_control']
    expected_text = ''.join(old_control['bits'][point[x]] for x in range(512))
    assert moved['bits'] == expected_text
    bits, W, audit = table(expected_text, moved['walsh'])
    assert audit['weight'] == 256 and audit['support_xor'] == 511 and audit['max_abs_W'] == 36 and bits[0] == 0
    assert W == [old_control['walsh'][dual[a]] for a in range(512)]
    assert all(abs(v) <= 36 - ((36 - 4 * ((a & 511).bit_count() & 1)) % 8) for a, v in enumerate(W))
    assignment_from_bits(bits, cls)
    return {'equivalent_types': [146, 511], 'recorded_type_groups': [[146, 511], [365]],
            'no_inequivalence_claim_for_365': True, 'point_and_dual_pairings_checked': 262144,
            'character_matrix_permutation_entries_checked': 10816,
            'actual_target_PB_balance_and_fixed_type_assertions_mapped': True,
            'transported_balanced_s511_control': audit}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt-encoding', action='store_true')
    ap.add_argument('--corrupt-type', action='store_true')
    ap.add_argument('--corrupt-balance', action='store_true')
    ap.add_argument('--corrupt-spectrum', action='store_true')
    args = ap.parse_args()
    started = time.monotonic()
    raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PIN
    imported = json.loads(gzip.decompress(raw))
    decomposition = json.loads((ROOT / 'inputs/decomposition.json').read_text())
    cls, types = group_audit(imported, decomposition)
    mutation = 'encoding' if args.corrupt_encoding else 'type' if args.corrupt_type else 'balance' if args.corrupt_balance else None
    questions, controls, target_expressions = {}, {}, {}
    for s in types:
        path = ROOT / f'inputs/target-s{s}.smt2.gz'
        assertions, audit = audit_question(path, s, 28, cls, mutation)
        metadata = json.loads((ROOT / f'inputs/target-s{s}.encoding.json').read_text())
        assert metadata['smt_sha256'] == audit['smt_sha256'] and metadata['s'] == s
        assert audit['full512_cap_counts'] == {24: 256, 28: 256}
        questions[s], target_expressions[s] = audit, assertions
    base = next(v['bits'] for v in imported['published_seeds'] if v['name'] == 'dsbf40')
    for record in decomposition['controls']:
        s = record['s']
        before = list(map(int, base))
        flips = record['flipped_orbits_from_published_seed']
        for j in flips:
            for x in cls['orbits'][j]:
                before[x] ^= 1
        assert sum(len(cls['orbits'][j]) for j in flips) == record['changed_points_before_optional_complement'] == 6
        if record['output_complemented']:
            before = [b ^ 1 for b in before]
        assert ''.join(map(str, before)) == record['bits']
        reported = record['walsh'].copy()
        if args.corrupt_spectrum:
            reported[37] += 8
        bits, W, audit = table(record['bits'], reported)
        assert audit['sha256_ascii_bits'] == record['sha256_ascii_bits']
        assert audit['weight'] == 256 and audit['support_xor'] == s and audit['degree'] == 8 and bits[0] == 0
        assert audit['max_abs_W'] == record['max_abs_W'] > 28
        for a, value in enumerate(W):
            assert value % 8 == 4 * ((a & s).bit_count() & 1)
        assignment = assignment_from_bits(bits, cls)
        relaxed, relaxed_audit = audit_question(ROOT / f'inputs/control-s{s}.smt2.gz', s, record['nominal_relaxed_bound'], cls)
        assert all(truth(e, assignment) for e in relaxed), 'planted balanced model rejected at relaxed bounds'
        failed_target = [i for i, e in enumerate(target_expressions[s]) if not truth(e, assignment)]
        assert failed_target and all(i < 208 for i in failed_target), 'planted control should fail only target Walsh bounds'
        assert all(truth(e, assignment) for e in target_expressions[s][208:])
        wrong_type_failures = {}
        for other in types:
            if other == s:
                continue
            failures = [i for i, e in enumerate(target_expressions[other][209:218]) if not truth(e, assignment)]
            assert len(failures) == (s ^ other).bit_count()
            wrong_type_failures[other] = failures
        controls[s] = {**audit, 'relaxed_question': relaxed_audit, 'all_relaxed_assertions_pass': True,
                       'failed_target_Walsh_assertions': failed_target, 'wrong_type_constraint_failures': wrong_type_failures}
    equivalence = equivalence_audit(cls, decomposition, target_expressions)
    results, witnesses = {}, []
    for s in types:
        result = json.loads((ROOT / f'results/s{s}-run.json').read_text())
        assert result['s'] == s and result['smt_sha256'] == questions[s]['smt_sha256']
        assert result['input_sha256'] == PIN
        certified = 'UNKNOWN'
        if result['solver_status'] == 'SAT':
            bits, W, audit = table(result['candidate_bits'], result['candidate_walsh'])
            assert audit['weight'] == 256 and audit['support_xor'] == s and audit['max_abs_W'] <= 28
            assert all(truth(e, assignment_from_bits(bits, cls)) for e in target_expressions[s])
            certified = 'SAT_VERIFIED'
            witness = {'bits': result['candidate_bits'], 'bit_order': 'bits[x]=f(x); x_i=(x>>i)&1',
                       'walsh': W, 'source_type': s, 'balance_shift': 0, **audit}
            (ROOT / f'results/witness-s{s}.json').write_text(json.dumps(witness, indent=2) + '\n')
            witnesses.append(witness)
        assert result['solver_status'] in ('SAT', 'UNSAT', 'UNKNOWN')
        results[s] = {'solver_status': result['solver_status'], 'certified_status': certified,
                      'elapsed_seconds': result['elapsed_seconds'], 'reason_unknown': result['reason_unknown'],
                      'complete_negative_certificate': False}
    out = {'status': 'PASS', 'types_derived_from_group': types, 'fixed_space_size': 4, 'orbit_count': 104,
           'all512_character_rows_checked': True, 'questions': questions, 'planted_controls': controls,
           'results': results, 'witnesses': witnesses, 'certified_exclusions': 0,
           'type_equivalence': equivalence,
           'input_sha256': PIN, 'checker_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started}
    (ROOT / 'results/check.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'types': types, 'certified_results': results,
                      'witness_count': len(witnesses), 'elapsed_seconds': out['elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
