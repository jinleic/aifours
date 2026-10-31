#!/usr/bin/env python3
"""Pinned R382 source-to-export projection; no producer or prior checker imports."""
import copy
import hashlib
import json
import os
import re
import signal
import sys
import zipfile
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST_SHA = '7864409178e5c45b649dbb68ca2d40bb61cd77882882c0b2d1d6019f343885e8'
RECORD_OFFSET = 43967  # Derived from the authorized record's observed trailing LF and length.
V = 1023
TRIANGLES = [(1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 3, 9),
             (2, 7, 10), (3, 8, 9), (4, 5, 10), (4, 8, 10),
             (5, 6, 9), (6, 7, 8)]
NEIGHBORS = {
    1: (2, 3, 4, 5, 6, 7), 2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9), 4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10), 6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10), 8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8), 10: (2, 4, 5, 7, 8)}
COORDINATES = {
    'type': 'functional_branch', 'coordinate_id': '5*A+b',
    'A_vertex_subset_mask': [0, 1023],
    'b': {'0': 'none', '1': 'S=(A_bit,B_bit)', '2': 'A_bit',
          '3': 'B_bit', '4': 'A_bit XOR B_bit'},
    'nonempty_coordinates': 5119}
RATIONAL = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z')
SHA = re.compile(r'[0-9a-f]{64}\Z')


class Reject(Exception):
    def __init__(self, reason, detail=''):
        self.reason = reason
        self.detail = detail
        super().__init__(reason + (': ' + detail if detail else ''))


def require(condition, reason, detail=''):
    if not condition:
        raise Reject(reason, detail)


def integer(x, lo, hi, reason):
    require(type(x) is int and lo <= x <= hi, reason)
    return x


def keys(x, expected, reason):
    require(type(x) is dict and set(x) == set(expected), reason)


def loads(data):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            require(key not in out, 'json.duplicate-key', str(key))
            out[key] = value
        return out
    try:
        return json.loads(data, object_pairs_hook=unique)
    except Reject:
        raise
    except (ValueError, UnicodeError) as e:
        raise Reject('json.invalid', str(e)) from e


def rational(x, reason):
    require(type(x) is str and RATIONAL.fullmatch(x) is not None, reason)
    return Fraction(x)


def mask(vertices):
    return sum(1 << (v - 1) for v in vertices)


def sparse(terms):
    out = {}
    for coordinate, value in terms:
        if coordinate:
            out[coordinate] = out.get(coordinate, 0) + value
    return {k: v for k, v in out.items() if v}


def hb(branch, m):
    return 5 * (m & V) + (branch if m & 1024 else 0)


def selected_neighbors(v, colors):
    return mask({u for i, tri in enumerate(TRIANGLES)
                 if colors[i] is not None and v in tri for u in tri if u != v})


def incident_colors(v, colors):
    return {colors[i] for i, tri in enumerate(TRIANGLES)
            if v in tri and colors[i] is not None}


def formula(name, colors):
    require(type(name) is list and bool(name) and type(name[0]) is str,
            'descriptor.shape')
    k = name[0]
    arity = {'mono': 3, 'cmi': 5, 'gate': 2, 'graph-fd': 2,
             'mixed-local-fd': 2, 'state-neighborhood': 2,
             'functional-neighborhood': 3, 'functional-triangle': 2,
             'data-processing': 3, 'pair-determines-state': 4}
    require(k in arity, 'descriptor.kind', k)
    require(len(name) == arity[k], 'descriptor.arity', k)
    if k == 'mono':
        b = integer(name[1], 1, 4, 'descriptor.branch')
        i = integer(name[2], 0, 10, 'descriptor.variable')
        return 'ge', sparse([(hb(b, 2047), 1), (hb(b, 2047 ^ (1 << i)), -1)])
    if k == 'cmi':
        b = integer(name[1], 1, 4, 'descriptor.branch')
        i = integer(name[2], 0, 10, 'descriptor.variable')
        j = integer(name[3], 0, 10, 'descriptor.variable')
        K = integer(name[4], 0, 2047, 'descriptor.conditioning')
        require(i < j and not (K & ((1 << i) | (1 << j))), 'descriptor.conditioning')
        return 'ge', sparse([(hb(b, K | (1 << i)), 1),
                             (hb(b, K | (1 << j)), 1),
                             (hb(b, K | (1 << i) | (1 << j)), -1),
                             (hb(b, K), -1)])
    if k == 'gate':
        require(type(name[1]) is int and name[1] == 1, 'descriptor.gate')
        return 'le', sparse([(5 * V, 3), (1, 17)] +
                            [(5 * (1 << i) + 1, -2) for i in range(10)])
    if k in ('graph-fd', 'mixed-local-fd', 'state-neighborhood', 'functional-neighborhood'):
        v = integer(name[1], 1, 10, 'descriptor.vertex')
        nb = mask(NEIGHBORS[v])
        if k == 'graph-fd':
            return 'eq', sparse([(5 * (nb | (1 << (v - 1))), 1), (5 * nb, -1)])
        if k == 'mixed-local-fd':
            local = selected_neighbors(v, colors)
            return 'eq', sparse([(5 * (local | (1 << (v - 1))) + 1, 1),
                                 (5 * local + 1, -1)])
        if k == 'state-neighborhood':
            require(len(incident_colors(v, colors)) >= 2, 'premise.state-neighborhood')
            return 'eq', sparse([(5 * nb + 1, 1), (5 * nb, -1)])
        c = integer(name[2], 0, 2, 'descriptor.color')
        require(c in incident_colors(v, colors), 'premise.functional-neighborhood')
        return 'eq', sparse([(5 * nb + 2 + c, 1), (5 * nb, -1)])
    if k == 'functional-triangle':
        t = integer(name[1], 1, 10, 'descriptor.triangle')
        c = colors[t - 1]
        require(c is not None, 'premise.functional-triangle')
        a = mask(TRIANGLES[t - 1])
        return 'eq', sparse([(5 * a + 2 + c, 1), (5 * a, -1)])
    a = integer(name[1], 0, 1023, 'descriptor.mask')
    j = integer(name[2], 2, 4, 'descriptor.branch')
    if k == 'data-processing':
        return 'le', sparse([(5 * a + j, 1), (5 * a + 1, -1)])
    ell = integer(name[3], 2, 4, 'descriptor.branch')
    require(j < ell, 'descriptor.branch-order')
    return 'le', sparse([(5 * a + 1, 1), (5 * a + j, -1),
                         (5 * a + ell, -1), (5 * a, 1)])


def action_valid(action, colors):
    require(type(action) is list and len(action) == 2, 'action.shape')
    p, cp = action
    require(type(p) is list and len(p) == 10 and all(type(x) is int for x in p)
            and sorted(p) == list(range(1, 11)), 'action.vertex-permutation')
    require(type(cp) is list and len(cp) == 3 and all(type(x) is int for x in cp)
            and sorted(cp) == [0, 1, 2], 'action.color-permutation')
    for v in range(1, 11):
        require({p[u - 1] for u in NEIGHBORS[v]} == set(NEIGHBORS[p[v - 1]]),
                'action.graph')
    lookup = {frozenset(t): i for i, t in enumerate(TRIANGLES)}
    for i, tri in enumerate(TRIANGLES):
        image = frozenset(p[v - 1] for v in tri)
        require(image in lookup, 'action.factor')
        color = colors[i]
        require(colors[lookup[image]] == (None if color is None else cp[color]),
                'action.coloring')


def push(vector, action):
    p, cp = action
    moved = []
    for coordinate, value in vector.items():
        a, b = divmod(coordinate, 5)
        new_a = sum(1 << (p[i] - 1) for i in range(10) if a & (1 << i))
        new_b = 2 + cp[b - 2] if b >= 2 else b
        moved.append((5 * new_a + new_b, value))
    return sparse(moved)


def read_vector(items, label, rational_coefficients=False):
    require(type(items) is list, label + '.shape')
    out = {}
    for pair in items:
        require(type(pair) is list and len(pair) == 2, label + '.shape')
        coord = integer(pair[0], 1, 5119, label + '.coordinate')
        require(coord not in out, label + '.duplicate-coordinate')
        if rational_coefficients:
            val = rational(pair[1], label + '.coefficient')
        else:
            require(type(pair[1]) is int, label + '.coefficient')
            val = pair[1]
        require(val != 0, label + '.coefficient')
        out[coord] = val
    return out


def target():
    return {5 * V: Fraction(3), **{5 * (1 << i): Fraction(-2) for i in range(10)}}


def validate_unique_rows(rows, key, reason):
    require(type(rows) is list, reason + '.shape')
    seen = set()
    for row in rows:
        require(type(row) is dict and key in row and type(row[key]) is list, reason + '.shape')
        name = json.dumps(row[key], separators=(',', ':'), ensure_ascii=True)
        require(name not in seen, reason + '.duplicate-row')
        seen.add(name)


def project(source, record, index, source_member):
    keys(source, ('source_files', 'indices', 'certificates'), 'source.schema')
    files, indices, certs = source['source_files'], source['indices'], source['certificates']
    require(type(files) is list and bool(files), 'source.provenance')
    for item in files:
        keys(item, ('path', 'sha256'), 'source.provenance')
        require(type(item['path']) is str and bool(item['path']) and
                type(item['sha256']) is str and SHA.fullmatch(item['sha256']) is not None,
                'source.provenance')
    require(type(indices) is list and type(certs) is list and len(indices) == len(certs),
            'source.index-list')
    require(all(type(i) is int and i >= 0 for i in indices) and len(indices) == len(set(indices)),
            'source.index-list')
    integer(index, 0, len(certs) - 1, 'source.index')
    cert = certs[index]
    keys(cert, ('colors', 'actions', 'multipliers', 'target'), 'source.certificate-schema')
    colors, actions, rows = cert['colors'], cert['actions'], cert['multipliers']
    require(type(colors) is list and len(colors) == 10 and
            all(c is None or (type(c) is int and c in (0, 1, 2)) for c in colors),
            'source.colors')
    require(type(actions) is list and bool(actions), 'action.shape')
    for action in actions:
        action_valid(action, colors)
    require(len({json.dumps(a, separators=(',', ':')) for a in actions}) == len(actions),
            'action.duplicate')
    require(cert['target'] == '3*Delta', 'source.target')
    validate_unique_rows(rows, 'row', 'source')
    for row in rows:
        keys(row, ('row', 'multiplier'), 'source.row-schema')
        relation, _ = formula(row['row'], colors)
        weight = rational(row['multiplier'], 'source.multiplier')
        require(weight != 0 and (relation == 'eq' or
                (relation == 'ge' and weight < 0) or (relation == 'le' and weight > 0)),
                'source.sign')
    keys(record, ('certificate_id', 'source_member', 'source_index', 'coordinate_system',
                  'target_vector', 'target_relation', 'action_count', 'actions', 'scope', 'rows'),
         'record.schema')
    require(type(record['source_index']) is int and record['source_index'] == index,
            'metadata.source-index')
    require(record['source_member'] == source_member, 'metadata.source-member')
    require(record['certificate_id'] == 'R%03d' % indices[index], 'metadata.certificate-id')
    require(json.dumps(record['coordinate_system'], sort_keys=True) ==
            json.dumps(COORDINATES, sort_keys=True), 'metadata.coordinate-system')
    require(type(record['action_count']) is int and record['action_count'] == len(actions),
            'metadata.action-count')
    require(json.dumps(record['actions']) == json.dumps(actions), 'metadata.actions')
    keys(record['scope'], ('class_id_zero_based', 'coloring', 'colors'), 'metadata.scope')
    require(type(record['scope']['class_id_zero_based']) is int and
            record['scope']['class_id_zero_based'] == indices[index], 'metadata.class-id')
    require(json.dumps(record['scope']['colors']) == json.dumps(colors), 'metadata.colors')
    require(record['scope']['coloring'] == ''.join('-' if c is None else str(c) for c in colors),
            'metadata.coloring')
    require(record['target_relation'] == 'le', 'target.relation')
    require(read_vector(record['target_vector'], 'target', True) == target(), 'target.mismatch')
    exported = record['rows']
    validate_unique_rows(exported, 'name', 'record')
    require(len(rows) == len(exported), 'row.count')
    kinds = Counter()
    spelling_equal = 0
    image_count = 0
    for position, (src_row, out_row) in enumerate(zip(rows, exported)):
        keys(out_row, ('name', 'relation', 'multiplier', 'image_vectors'), 'record.row-schema')
        require(json.dumps(out_row['name']) == json.dumps(src_row['row']), 'row.order', str(position))
        relation, base = formula(src_row['row'], colors)
        require(out_row['relation'] == relation, 'row.relation', str(position))
        require(rational(out_row['multiplier'], 'row.multiplier') ==
                rational(src_row['multiplier'], 'source.multiplier'), 'row.multiplier', str(position))
        spelling_equal += out_row['multiplier'] == src_row['multiplier']
        images = out_row['image_vectors']
        require(type(images) is list and len(images) == len(actions), 'image.count', str(position))
        for action, image in zip(actions, images):
            require(read_vector(image, 'image') == push(base, action), 'row.image', str(position))
            image_count += 1
        kinds[src_row['row'][0]] += 1
    return {'class_id': indices[index], 'colors': colors, 'actions': actions,
            'rows': len(rows), 'images': image_count, 'descriptor_counts': dict(sorted(kinds.items())),
            'identical_multiplier_spellings': spelling_equal, 'source_files_metadata': files,
            'source_indices_metadata': indices}


def identity(record, expected):
    action_count = record['action_count']
    require(type(action_count) is int and action_count > 0, 'identity.action-count')
    accumulated = {}
    for row in record['rows']:
        weight = rational(row['multiplier'], 'identity.multiplier') / action_count
        require(len(row['image_vectors']) == action_count, 'identity.image-count')
        for image in row['image_vectors']:
            for coord, coeff in read_vector(image, 'identity.image').items():
                accumulated[coord] = accumulated.get(coord, Fraction(0)) + weight * coeff
    accumulated = {k: v for k, v in accumulated.items() if v}
    differences = sum(accumulated.get(k, 0) != expected.get(k, 0)
                      for k in set(accumulated) | set(expected))
    require(accumulated == expected, 'identity.mismatch',
            'differing_coordinates=' + str(differences))
    return len(accumulated)


def fixture():
    colors = [0, 0, 0, None, 0, 1, None, 1, 1, 1]
    ident = [list(range(1, 11)), [0, 1, 2]]
    symmetry = [[8, 9, 3, 4, 10, 7, 6, 1, 2, 5], [1, 0, 2]]
    actions = [ident, symmetry]
    multipliers = [
        {'row': ['data-processing', 1, 2], 'multiplier': '1/2'},
        {'row': ['data-processing', 2, 3], 'multiplier': '1'},
        {'row': ['mono', 1, 10], 'multiplier': '-1'}]
    source = {'source_files': [{'path': 'synthetic-source', 'sha256': '0' * 64}],
              'indices': [382], 'certificates': [{'colors': colors, 'actions': actions,
              'multipliers': multipliers, 'target': '3*Delta'}]}
    record = {'certificate_id': 'R382', 'source_member': 'synthetic-member', 'source_index': 0,
              'coordinate_system': copy.deepcopy(COORDINATES),
              'target_vector': [[5115, '3']] + [[5 * (1 << i), '-2'] for i in range(10)],
              'target_relation': 'le', 'action_count': 2, 'actions': copy.deepcopy(actions),
              'scope': {'class_id_zero_based': 382, 'coloring': '000-01-111',
                        'colors': copy.deepcopy(colors)},
              'rows': [
                  {'name': ['data-processing', 1, 2], 'relation': 'le', 'multiplier': '1/2',
                   'image_vectors': [[[6, -1], [7, 1]], [[641, -1], [643, 1]]]},
                  {'name': ['data-processing', 2, 3], 'relation': 'le', 'multiplier': '1',
                   'image_vectors': [[[11, -1], [13, 1]], [[1281, -1], [1282, 1]]]},
                  {'name': ['mono', 1, 10], 'relation': 'ge', 'multiplier': '-1',
                   'image_vectors': [[[5115, -1], [5116, 1]], [[5115, -1], [5116, 1]]]}]}
    return source, record


def controls():
    source, record = fixture()
    require(project(source, record, 0, 'synthetic-member')['rows'] == 3, 'control.positive')
    result = [{'name': 'synthetic-two-action-projection', 'result': 'PASS'}]
    expected_formulae = [
        (['mono', 1, 10], 'ge', {5115: -1, 5116: 1}),
        (['cmi', 2, 0, 1, 0], 'ge', {5: 1, 10: 1, 15: -1}),
        (['cmi', 2, 0, 10, 0], 'ge', {2: 1, 5: 1, 7: -1}),
        (['gate', 1], 'le', {5115: 3, 1: 17, 6: -2, 11: -2, 21: -2, 41: -2,
                             81: -2, 161: -2, 321: -2, 641: -2, 1281: -2, 2561: -2}),
        (['graph-fd', 3], 'eq', {1995: 1, 1975: -1}),
        (['mixed-local-fd', 3], 'eq', {1956: 1, 1936: -1}),
        (['state-neighborhood', 3], 'eq', {1976: 1, 1975: -1}),
        (['functional-neighborhood', 3, 0], 'eq', {1977: 1, 1975: -1}),
        (['functional-triangle', 1], 'eq', {37: 1, 35: -1}),
        (['data-processing', 1, 2], 'le', {6: -1, 7: 1}),
        (['pair-determines-state', 0, 2, 3], 'le', {1: 1, 2: -1, 3: -1})]
    for name, relation, vector in expected_formulae:
        require(formula(name, source['certificates'][0]['colors']) == (relation, vector),
                'control.formula', repr(name))
        result.append({'name': 'formula-' + repr(name), 'result': 'PASS'})
    simple = {'action_count': 2, 'rows': [{'multiplier': '2',
               'image_vectors': [[[5, 1]], [[10, 1]]]}]}
    require(identity(simple, {5: Fraction(1), 10: Fraction(1)}) == 2, 'control.identity-positive')
    result.append({'name': 'synthetic-action-average', 'result': 'PASS'})

    def reject(name, expected, mutate):
        s, r = copy.deepcopy(source), copy.deepcopy(record)
        mutate(s, r)
        try:
            project(s, r, 0, 'synthetic-member')
        except Reject as e:
            require(e.reason == expected, 'control.wrong-reason', name + ': ' + e.reason)
            result.append({'name': name, 'result': 'REJECTED', 'reason': e.reason})
            return
        raise Reject('control.accepted-mutation', name)

    reject('wrong-source-index', 'metadata.source-index', lambda s, r: r.update(source_index=1))
    reject('wrong-source-member', 'metadata.source-member', lambda s, r: r.update(source_member='wrong'))
    reject('wrong-class-id', 'metadata.class-id', lambda s, r: r['scope'].update(class_id_zero_based=381))
    reject('wrong-colors', 'metadata.colors', lambda s, r: r['scope']['colors'].__setitem__(0, 2))
    reject('wrong-coloring', 'metadata.coloring', lambda s, r: r['scope'].update(coloring='wrong'))
    reject('wrong-coordinate-system', 'metadata.coordinate-system', lambda s, r: r['coordinate_system'].update(nonempty_coordinates=5118))
    reject('wrong-action-count', 'metadata.action-count', lambda s, r: r.update(action_count=1))
    reject('wrong-action', 'metadata.actions', lambda s, r: r['actions'].reverse())
    def bad_permutation(s, r):
        s['certificates'][0]['actions'][0][0][0] = 2
    reject('bad-source-permutation', 'action.vertex-permutation', bad_permutation)
    reject('duplicate-source-row', 'source.duplicate-row', lambda s, r: s['certificates'][0]['multipliers'].append(copy.deepcopy(s['certificates'][0]['multipliers'][0])))
    reject('duplicate-export-row', 'record.duplicate-row', lambda s, r: r['rows'].append(copy.deepcopy(r['rows'][0])))
    reject('missing-export-row', 'row.count', lambda s, r: r['rows'].pop())
    reject('reordered-rows', 'row.order', lambda s, r: r['rows'].reverse())
    reject('wrong-relation', 'row.relation', lambda s, r: r['rows'][0].update(relation='ge'))
    reject('wrong-weight', 'row.multiplier', lambda s, r: r['rows'][0].update(multiplier='2'))
    def bad_sign(s, r):
        s['certificates'][0]['multipliers'][2]['multiplier'] = '1'
        r['rows'][2]['multiplier'] = '1'
    reject('wrong-shannon-sign', 'source.sign', bad_sign)
    reject('bad-source-branch', 'descriptor.branch', lambda s, r: s['certificates'][0]['multipliers'][0]['row'].__setitem__(2, 1))
    reject('unknown-descriptor', 'descriptor.kind', lambda s, r: s['certificates'][0]['multipliers'][0]['row'].__setitem__(0, 'invented'))
    reject('missing-action-image', 'image.count', lambda s, r: r['rows'][0]['image_vectors'].pop())
    reject('wrong-image-coefficient', 'row.image', lambda s, r: r['rows'][0]['image_vectors'][1][0].__setitem__(1, -2))
    reject('wrong-image-coordinate', 'row.image', lambda s, r: r['rows'][0]['image_vectors'][1][1].__setitem__(0, 644))
    reject('out-of-range-coordinate', 'image.coordinate', lambda s, r: r['rows'][0]['image_vectors'][0][0].__setitem__(0, 5120))
    reject('duplicate-image-coordinate', 'image.duplicate-coordinate', lambda s, r: r['rows'][0]['image_vectors'][0].append([6, 1]))
    reject('wrong-target', 'target.mismatch', lambda s, r: r['target_vector'][0].__setitem__(1, '4'))
    reject('duplicate-target-coordinate', 'target.duplicate-coordinate', lambda s, r: r['target_vector'].append([5, '-2']))
    for name, expected, thunk in [
        ('duplicate-json-key', 'json.duplicate-key', lambda: loads(b'{"x":1,"x":2}')),
        ('identity-mutation', 'identity.mismatch', lambda: identity(simple, {5: Fraction(2), 10: Fraction(1)}))]:
        try:
            thunk()
        except Reject as e:
            require(e.reason == expected, 'control.wrong-reason', name + ': ' + e.reason)
            result.append({'name': name, 'result': 'REJECTED', 'reason': e.reason})
        else:
            raise Reject('control.accepted-mutation', name)
    return result


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pinned_inputs():
    manifest_bytes = (HERE / 'manifest-v1.json').read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'pin.manifest')
    manifest = loads(manifest_bytes)
    require(len(manifest['inputs_in_read_order']) == 16, 'pin.input-count')
    evidence = []
    for entry in manifest['inputs_in_read_order']:
        data = Path(entry['path']).read_bytes()
        digest = sha(data)
        require(digest == entry['sha256'] and len(data) == entry['bytes'] and
                data.count(b'\n') == entry['LF'], 'pin.input', entry['path'])
        evidence.append({'path': entry['path'], 'sha256': digest,
                         'bytes': len(data), 'LF': data.count(b'\n')})
    archive = manifest['archive']
    with open(archive['path'], 'rb') as f:
        before = os.fstat(f.fileno())
        h = hashlib.sha256()
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
        require(before.st_size == archive['bytes'] and h.hexdigest() == archive['sha256'],
                'pin.archive')
        f.seek(0)
        with zipfile.ZipFile(f) as z:
            sm, rm = manifest['additional_bounded_member'], manifest['exported_record']
            for name in (sm['member'], rm['member']):
                require(sum(info.filename == name for info in z.infolist()) == 1, 'pin.member-name')
            require(z.getinfo(sm['member']).file_size == sm['bytes'], 'pin.source-size')
            with z.open(sm['member']) as member:
                source_bytes = member.read()
            require(len(source_bytes) == sm['bytes'] and sha(source_bytes) == sm['sha256'],
                    'pin.source')
            with z.open(rm['member']) as member:
                member.seek(RECORD_OFFSET)
                record_bytes = member.read(rm['bytes'])
            require(len(record_bytes) == rm['bytes'] and sha(record_bytes) == rm['sha256'],
                    'pin.record')
            require(record_bytes.startswith(b'{') and record_bytes.endswith(b'\n') and
                    record_bytes.count(b'\n') == 1, 'pin.record-framing')
        after = os.fstat(f.fileno())
        require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns) ==
                (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns),
                'pin.archive-changed')
    return manifest, evidence, source_bytes, record_bytes


def timeout_handler(signum, frame):
    raise Reject('cap.exceeded')


def main():
    require(sys.argv[1:] == ['--final'], 'usage', 'expected --final')
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, 115)
    manifest, inputs, source_bytes, record_bytes = pinned_inputs()
    findings = controls()
    source = loads(source_bytes)
    record = loads(record_bytes)
    require(manifest['exported_record']['record_index_zero_based'] == 1, 'pin.record-index')
    require(record.get('certificate_id') == manifest['exported_record']['certificate_id'] == 'R382',
            'pin.certificate-id')
    projection = project(source, record, 1, manifest['additional_bounded_member']['member'])
    nonzero = identity(record, target())
    signal.setitimer(signal.ITIMER_REAL, 0)
    return {'result': 'R382_PROJECTION_AND_EXACT_IDENTITY_MATCH', 'controls': findings,
            'manifest_sha256': MANIFEST_SHA, 'written_inputs': inputs,
            'archive_sha256': manifest['archive']['sha256'],
            'archive_bytes': manifest['archive']['bytes'],
            'source_member': manifest['additional_bounded_member'],
            'exported_record': manifest['exported_record'], 'record_offset': RECORD_OFFSET,
            'record_line_ordinal': 'manifest-declared; prefix not inspected',
            'projection': projection, 'identity_nonzero_coordinates': nonzero,
            'limitations': ['No other archive record interpreted or compared',
              'Referenced source_files bodies not opened; provenance claims not independently verified',
              'No coverage, full-archive, theorem, formal, human, cross-family or novelty conclusion']}


if __name__ == '__main__':
    try:
        output = main()
    except Reject as e:
        print(json.dumps({'result': 'UNKNOWN_OR_REJECTED', 'reason': e.reason, 'detail': e.detail}, sort_keys=True))
        sys.exit(2)
    except Exception as e:
        print(json.dumps({'result': 'UNKNOWN', 'reason': type(e).__name__, 'detail': str(e)}, sort_keys=True))
        sys.exit(2)
    print(json.dumps(output, sort_keys=True))
