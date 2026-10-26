"""Exact coefficient replay only. DO NOT EXECUTE without a named parent GO.

No optimization, group enumeration, floating-point entropy, external imports or file
writes. Reads only pinned graph input and nine pre-existing rational certificate files.
Prints success only after every identity and in-memory intended-reason control passes.
This is ordinary Fraction arithmetic, not proof-assistant verification.
"""
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = Path('/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus')
GRAPH_PIN = 'bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6'
PINS = {
    'diamond_2_4_1_3.json': 'c570b19e84685964493af9db86eec41639ceb40d3cbfa5c7dac855f9326a3b9a',
    'diamond_2_6_1_7.json': '9d623cc6bcbdf49e10e22da468b0c744f08571dfc15b9c97bef18f374f762e46',
    'diamond_3_5_1_4.json': '78ec434ce4cae98bdb589dd4e0017318be0d3f774a825f5154d4533a6e9a5cbc',
    'diamond_5_7_1_6.json': '190e687c8b7c8438243b5b9f76130eeb197bcd3da065f40c0d7e9aa55d1cad8d',
    'diamond_3_10_4_8.json': '4b058c8a8718ad023d0e9d81f1bf62cf885659498d7194008823539fbc210ab0',
    'diamond_4_9_3_8.json': '9b5d1d18f7662af5614cdac3a8d8ba6c2986cfd4db3d6f83e6cab0a9e526305f',
    'diamond_6_10_7_8.json': '3620de2b76d8d50404bbd75667e363872624d648802bf8f610490d3bf4d32eae',
    'diamond_7_9_6_8.json': 'cf9d517c563a3097cc95b40557a41d9dc27a8de4b5342599e3d3d9aec9efc6e7',
    'avg-ratio-9vertex.json': '59fa20148006b43b93e1cb9f644fdd1778725de1a973bb2549ac8666913ebf94',
}


def need(condition, reason):
    if not condition:
        raise ValueError(reason)


def pinned_json(data, digest):
    need(hashlib.sha256(data).hexdigest() == digest, 'input hash mismatch')
    return json.loads(data)


def load_pinned(path, digest):
    try:
        data = path.read_bytes()
    except FileNotFoundError as error:
        raise ValueError('pinned input missing') from error
    return pinned_json(data, digest)


def canonical(row):
    result = {}
    for key, value in row.items():
        mask = int(key)
        need(str(mask) == str(key) and mask > 0, 'invalid entropy mask')
        coefficient = Fraction(value)
        if coefficient:
            result[mask] = coefficient
    return result


def signature(row):
    return tuple(sorted(row.items()))


def add(accumulator, row, factor=1):
    for mask, coefficient in row.items():
        accumulator[mask] = accumulator.get(mask, Fraction(0)) + factor * coefficient


def information(i, j, k):
    result = {}
    for mask, coefficient in ((i | k, 1), (j | k, 1), (i | j | k, -1), (k, -1)):
        if mask:
            result[mask] = result.get(mask, 0) + coefficient
    return {mask: value for mask, value in result.items() if value}


def elemental_rows(n):
    full = (1 << n) - 1
    rows = [{full: 1, full ^ (1 << i): -1} for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            rest = full ^ (1 << i) ^ (1 << j)
            subset = rest
            while True:
                rows.append(information(1 << i, 1 << j, subset))
                if subset == 0:
                    break
                subset = (subset - 1) & rest
    return rows


def fd_rows(vertices, edges):
    positions = {vertex: index for index, vertex in enumerate(vertices)}
    neighbors = {vertex: set() for vertex in vertices}
    for a, b in edges:
        if a in positions and b in positions:
            neighbors[a].add(b)
            neighbors[b].add(a)
    result = []
    for vertex in vertices:
        neighbor_mask = sum(1 << positions[u] for u in neighbors[vertex])
        row = {neighbor_mask | (1 << positions[vertex]): 1}
        if neighbor_mask:
            row[neighbor_mask] = -1
        result.append(row)
    return result


def check_diamond(certificate, name, edges):
    need(certificate['name'] + '.json' == name, 'wrong diamond name')
    need(certificate['exact_bound'] == '20/3', 'wrong diamond bound label')
    need(Fraction(certificate['ingleton_multiplier']) == Fraction(1, 3), 'wrong Ingleton multiplier')
    weights = [Fraction(value) for value in certificate['u']]
    need(weights == [Fraction(2, 3)] * 10, 'wrong singleton weights')
    u, v, p, q = (int(value) for value in certificate['name'].split('_')[1:])
    need(len({u, v, p, q}) == 4 and all(1 <= t <= 10 for t in (u, v, p, q)), 'wrong diamond vertices')
    u, v, p, q = (1 << (t - 1) for t in (u, v, p, q))
    z = 1023 ^ u ^ v ^ p ^ q
    ingleton = {}
    for row, factor in ((information(u, v, z | p), 1), (information(u, v, z | q), 1),
                        (information(p, q, z), 1), (information(u, v, z), -1)):
        add(ingleton, row, factor)
    ingleton = {mask: value for mask, value in ingleton.items() if value}
    elemental = {signature(row) for row in elemental_rows(10)}
    accumulator = {1023: Fraction(1)}
    for index, weight in enumerate(weights):
        add(accumulator, {1 << index: 1}, -weight)
    found_ingleton = 0
    for entry in certificate['ge']:
        row = canonical(entry['row'])
        weight = Fraction(entry['y'])
        need(weight >= 0, 'negative inequality multiplier')
        if row == ingleton:
            found_ingleton += 1
            need(weight == Fraction(1, 3), 'wrong Ingleton row weight')
        else:
            need(signature(row) in elemental, 'non-elemental inequality row')
        add(accumulator, row, weight)
    need(found_ingleton == 1, 'wrong number of Ingleton rows')
    expected_fds = {signature(row) for row in fd_rows(list(range(1, 11)), edges)}
    observed_fds = []
    for entry in certificate['eq']:
        row = canonical(entry['row'])
        need(signature(row) in expected_fds, 'non-graph FD row')
        observed_fds.append(signature(row))
        add(accumulator, row, Fraction(entry['z']))
    need(len(observed_fds) == 10 and set(observed_fds) == expected_fds, 'incomplete graph FD rows')
    need(not any(accumulator.values()), 'nonzero diamond coefficient residual')


def check_deletion(certificate, vertex, edges):
    vertices = [u for u in range(1, 11) if u != vertex]
    need(certificate['W'] == vertices, 'wrong deleted-vertex coordinate order')
    need(Fraction(certificate['lam']) == Fraction(2, 3), 'wrong deletion coefficient')
    rows = elemental_rows(9)
    fds = fd_rows(vertices, edges)
    accumulator = {511: Fraction(1)}
    for index in range(9):
        add(accumulator, {1 << index: 1}, -Fraction(2, 3))
    for text, value in certificate['y'].items():
        index = int(text)
        need(0 <= index < len(rows), 'invalid elemental row index')
        weight = Fraction(value)
        need(weight >= 0, 'negative deletion multiplier')
        add(accumulator, rows[index], weight)
    for text, value in certificate['z'].items():
        index = int(text)
        need(0 <= index < len(fds), 'invalid FD row index')
        add(accumulator, fds[index], -Fraction(value))
    for text, value in certificate['c'].items():
        mask = int(text)
        weight = Fraction(value)
        need(1 <= mask <= 511 and weight >= 0, 'invalid entropy nonnegativity term')
        add(accumulator, {mask: 1}, weight)
    need(not any(accumulator.values()), 'nonzero deletion coefficient residual')


def reject_control(name, operation, expected_reason):
    try:
        operation()
    except ValueError as error:
        need(str(error) == expected_reason, name + ': wrong rejection reason: ' + str(error))
        return name
    raise ValueError(name + ': mutation was accepted')


def main():
    graph_data = load_pinned(HERE / 'inputs-v1.json', GRAPH_PIN)
    edges = graph_data['graph']['undirected_edges']
    need(graph_data['graph']['vertices'] == list(range(1, 11)), 'wrong graph vertices')
    need(len(edges) == 26 and len({tuple(edge) for edge in edges}) == 26, 'wrong graph edges')
    need(all(1 <= a < b <= 10 for a, b in edges), 'invalid graph edge')
    # Load and hash EVERY required input before checking or announcing any result.
    data = {name: load_pinned(BASE / 'evidence' / 'certs' / name, digest)
            for name, digest in PINS.items()}
    deletion_data = data['avg-ratio-9vertex.json']
    need(set(deletion_data) == {'minus' + str(v) for v in range(1, 11)}, 'incomplete deletion bundle')
    for name, certificate in data.items():
        if name.startswith('diamond_'):
            check_diamond(certificate, name, edges)
    for vertex in range(1, 11):
        check_deletion(deletion_data['minus' + str(vertex)], vertex, edges)

    controls = []
    name = 'diamond_3_10_4_8.json'
    altered = copy.deepcopy(data[name])
    altered['ge'][0]['y'] = str(Fraction(altered['ge'][0]['y']) + 1)
    controls.append(reject_control('diamond_weight_corruption', lambda: check_diamond(altered, name, edges), 'nonzero diamond coefficient residual'))
    altered = copy.deepcopy(data[name])
    altered['ge'][0]['row']['161'] = 2
    controls.append(reject_control('non_elemental_row', lambda: check_diamond(altered, name, edges), 'non-elemental inequality row'))
    altered = copy.deepcopy(data[name])
    altered['eq'][0]['row'] = {'127': 1, '125': -1}
    controls.append(reject_control('wrong_graph_fd', lambda: check_diamond(altered, name, edges), 'non-graph FD row'))
    altered = copy.deepcopy(data[name])
    altered['u'][0] = '1/2'
    controls.append(reject_control('singleton_normalization', lambda: check_diamond(altered, name, edges), 'wrong singleton weights'))
    altered = copy.deepcopy(deletion_data['minus1'])
    altered['y'][next(iter(altered['y']))] = '-1'
    controls.append(reject_control('negative_deletion_weight', lambda: check_deletion(altered, 1, edges), 'negative deletion multiplier'))
    altered = copy.deepcopy(deletion_data['minus1'])
    altered['y']['999999'] = '1'
    controls.append(reject_control('out_of_range_row', lambda: check_deletion(altered, 1, edges), 'invalid elemental row index'))
    altered = copy.deepcopy(deletion_data['minus1'])
    altered['W'] = list(range(1, 10))
    controls.append(reject_control('wrong_deletion_order', lambda: check_deletion(altered, 1, edges), 'wrong deleted-vertex coordinate order'))
    altered = copy.deepcopy(deletion_data['minus1'])
    altered['y'][next(iter(altered['y']))] = '1'
    controls.append(reject_control('deletion_residual', lambda: check_deletion(altered, 1, edges), 'nonzero deletion coefficient residual'))
    controls.append(reject_control('changed_input_bytes', lambda: pinned_json(b'{}', GRAPH_PIN), 'input hash mismatch'))
    controls.append(reject_control('missing_pinned_input', lambda: load_pinned(HERE / '__deliberately_absent_pinned_input_v1__', GRAPH_PIN), 'pinned input missing'))
    print(json.dumps({'status': 'EXACT_COEFFICIENT_IDENTITIES_AND_CONTROLS_PASS',
                      'diamond_identities': 8, 'deletion_identities': 10,
                      'controls': controls, 'input_pins': PINS,
                      'graph_input_sha256': GRAPH_PIN,
                      'limits': 'Ordinary stdlib Fraction arithmetic, not formal/kernel proof; no finite-group classification or manuscript theorem replay.'}, indent=2))


if __name__ == '__main__':
    main()
