#!/usr/bin/env python3
"""Close the 20-vector source-span check using exact Witt character arithmetic.

Avoids a redundant 2520-column horizontal RREF. Independently checks the actual
20 stored combinations are horizontal, checks their coefficient independence,
and independently computes the full horizontal dimension as 20 from the L6
character and the finite-sl3 Weyl denominator. The Witt/finite-Levi/actual-source
interfaces remain named mathematical imports, not formal verification.
"""
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('independent_tree', ROOT / 'frontier-20261028-levi-critical-independent-replay.py')
ind = importlib.util.module_from_spec(sp)
sp.loader.exec_module(ind)


def main():
    cbytes = (ROOT / 'frontier-20261028-level6-666-two-minor-certificate-v1.json').read_bytes()
    assert hashlib.sha256(cbytes).hexdigest() == 'a59569fdecaff1c7c81a7c6d28b48ee8548d5ccbdc1107a145ede26d452a19ef'
    C = json.loads(cbytes)
    raw = (ROOT / C['pencil']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == C['pencil_sha256']
    P = json.loads(raw)
    assert tuple(P['source_words']) == ind.lyndon_words((6, 6, 6))
    basis = [ind.ind.standard_bracket(w) for w in P['source_words']]
    assert all(v.get(w) == 1 and min(v) == w for w, v in zip(P['source_words'], basis))
    coeffs = P['horizontal_kernel_coefficients']
    assert len(coeffs) == 20
    assert len(ind.ind.ReducedSpace([{int(i): Q(q) for i, q in co.items()} for co in coeffs])) == 20
    for co in coeffs:
        vector = ind.combine(basis, co)
        for generator in ('f1', 'f2'):
            assert not ind.act(vector, generator, 6, 6)
    weights = ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2))
    char = Counter()
    for d, mobius in ((1, 1), (2, -1), (3, -1), (6, 1)):
        tensor = Counter({(0, 0): 1})
        for _ in range(6 // d):
            nxt = Counter()
            for (a, b), count in tensor.items():
                for u, v in weights:
                    nxt[a + u, b + v] += count
            tensor = nxt
        for (a, b), count in tensor.items():
            char[d * a, d * b] += mobius * count
    assert all(c % 6 == 0 for c in char.values())
    char = {m: c // 6 for m, c in char.items()}
    lowest = char.get((6, 6), 0) - char.get((5, 6), 0) - char.get((6, 5), 0) + char.get((4, 5), 0) + char.get((5, 4), 0) - char.get((4, 4), 0)
    assert lowest == 20 and char[6, 6] == 2520
    out = ROOT / 'frontier-20261028-level6-666-source-by-character-v1.json'
    with out.open('x') as stream:
        json.dump({'degree': [6, 6, 6], 'pencil_sha256': C['pencil_sha256'],
                   'source_weight_dimension': 2520, 'lowest_character_multiplicity': lowest,
                   'independent_horizontal_combinations': 20, 'horizontal_action_checks': 40,
                   'Lyndon_basis_checked': 2520,
                   'Witt_character_formula': '(V^6-psi2(V^3)-psi3(V^2)+psi6(V))/6',
                   'status': 'PASS_FULL_20_DIMENSION_SOURCE_BY_CHARACTER_AND_INDEPENDENT_COMBINATIONS',
                   'limits': 'uses named Witt character, finite-sl3 complete reducibility and actual-source identification; not formal or independent-model verification'}, stream, indent=2)
        stream.write('\n')
    print('PASS exact full 666 lowest source: 20 independent horizontal combinations and character multiplicity20', out.name)


if __name__ == '__main__':
    main()
