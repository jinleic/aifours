"""Independent word-deletion audit; imports no producer code.

The source is independently reconstructed as a genuine Lie polynomial by
checking its Dynkin bracket expansion equals four times the supplied tensor.
Lowering moves each level-zero leaf image to the right in associative words.
Its canceled terminal actor and every affine output coefficient are checked.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


LABELS = ['E12', 'E23', 'E13', 'E21', 'E32', 'E31', 'H1-model', 'H2-model']
MATRICES = [
    (0,1,0,0,0,0,0,0,0), (0,0,0,0,0,1,0,0,0), (0,0,1,0,0,0,0,0,0),
    (0,0,0,1,0,0,0,0,0), (0,0,0,0,0,0,0,1,0), (0,0,0,0,0,0,1,0,0),
    (1,0,0,0,-1,0,0,0,0), (0,0,0,0,1,0,0,0,-1),
]
FULL = [(2,1), (1,2), (2,2), (0,1), (1,0), (0,0), (1,1), (1,1)]


def adjoint_action(actor, vector):
    left, right = MATRICES[actor], MATRICES[vector]
    bracket = [sum(left[3*i+k]*right[3*k+j] - right[3*i+k]*left[3*k+j]
                   for k in range(3)) for i in range(3) for j in range(3)]
    coefficients = [bracket[1], bracket[5], bracket[2], bracket[3],
                    bracket[7], bracket[6], bracket[0], -bracket[8]]
    assert all(sum(c * b[i] for c,b in zip(coefficients,MATRICES)) == bracket[i]
               for i in range(9))
    return {i: Q(c) for i,c in enumerate(coefficients) if c}


def commutator(left, right):
    result = defaultdict(Q)
    for a, ca in left.items():
        for b, cb in right.items():
            result[a+b] += ca*cb
            result[b+a] -= ca*cb
    return {w:c for w,c in result.items() if c}


def bracket_word(word):
    result = {(word[-1],): Q(1)}
    for letter in reversed(word[:-1]):
        result = commutator({(letter,): Q(1)}, result)
    return result


def read_word(word):
    return tuple(LABELS.index(x) for x in word)


def main():
    root = Path(__file__).resolve().parent
    vector_file = root/'level4-invariant-vectors.json'
    vectors = json.loads(vector_file.read_text())
    assert vectors['basis_order'] == LABELS
    source = {read_word(e['word']): Q(e['coefficient']) for e in vectors['invariant']}
    saved = {read_word(e['word']): tuple(Q(x) for x in e['constant_r_s'])
             for e in vectors['lowering']}
    assert len(source) == len(vectors['invariant'])
    assert len(saved) == len(vectors['lowering'])
    assert source and saved
    dynkin = defaultdict(Q)
    for word, scalar in source.items():
        assert len(word) == 4
        assert tuple(sum(FULL[i][j] for i in word) for j in range(2)) == (4,4)
        for w,c in bracket_word(word).items():
            dynkin[w] += scalar*c
    dynkin = {w:c for w,c in dynkin.items() if c}
    assert dynkin == {w:4*c for w,c in source.items()}
    # Hence x = (1/4) sum_w x_w [w0,[w1,[w2,w3]]], a genuine Lie element.
    for actor in (0,1,3,4,6,7):
        result = defaultdict(Q)
        for word, scalar in source.items():
            for position, letter in enumerate(word):
                for new_letter, c in adjoint_action(actor, letter).items():
                    result[word[:position]+(new_letter,)+word[position+1:]] += scalar*c
        assert all(c == 0 for c in result.values())
    # D3 images of the eight level-one vectors, from the original defining brackets.
    # Actor -1 denotes h3; parameter slots 0,1,2 denote constant,r,s.
    leaf_images = {3: (1, 2, Q(-1)), 4: (0, 1, Q(1)),
                   5: (-1, 0, Q(-1)), 6: (2, 2, Q(-1)), 7: (2, 1, Q(-1))}
    output = defaultdict(lambda: [Q(0), Q(0), Q(0)])
    terminal = defaultdict(Q)
    for word, scalar in source.items():
        for position, letter in enumerate(word):
            if letter not in leaf_images:
                continue
            actor, parameter, c = leaf_images[letter]
            deleted = word[:position]+word[position+1:]
            terminal[(deleted, actor, parameter)] += scalar*c
            for later in range(position+1, len(word)):
                suffix_letter = word[later]
                if actor == -1:
                    a,b = FULL[suffix_letter]
                    for slot,value in enumerate((2,-a,-b)):
                        output[deleted][slot] += scalar*c*value
                else:
                    for new_letter,value in adjoint_action(actor, suffix_letter).items():
                        replaced = deleted[:later-1]+(new_letter,)+deleted[later:]
                        output[replaced][parameter] += scalar*c*value
    assert all(c == 0 for c in terminal.values()), 'Uncanceled terminal Levi/Cartan actor'
    output = {w:tuple(c) for w,c in output.items() if any(c)}
    assert output == saved, 'Independent word lowering disagrees with recursive producer'
    witness = (0,1,6)
    assert output[witness] == (Q(-4,3), Q(4,3), Q(0))
    # On r >= 4 this coefficient is 4(r-1)/3 >= 4 > 0.
    altered = dict(saved)
    old = altered[witness]
    altered[witness] = (old[0]+1, old[1], old[2])
    assert altered != output
    bad_source = dict(source)
    first = next(iter(bad_source))
    bad_source[first] += 1
    bad_dynkin = defaultdict(Q)
    for word, scalar in bad_source.items():
        for w,c in bracket_word(word).items():
            bad_dynkin[w] += scalar*c
    bad_dynkin = {w:c for w,c in bad_dynkin.items() if c}
    assert bad_dynkin != {w:4*c for w,c in bad_source.items()}
    receipt = {
        'status': 'PASS',
        'scope': 'one invariant line of free L4(ad sl3), original D3, r,s >= 4',
        'universal_serre_equality': False,
        'producer_imported': False,
        'lie_expression_checked': 'Dynkin right bracket(source) = 4 * source',
        'levi_generators_checked': ['e1','e2','f1','f2','h1','h2'],
        'terminal_levi_and_cartan_actor_cancellation_checked': True,
        'all_affine_lowering_coefficients_checked': True,
        'witness_coefficient': '4*(r-1)/3 on E12 E23 H1-model',
        'negative_controls_rejected': ['altered lowering constant','altered Lie tensor coefficient'],
        'vector_sha256': hashlib.sha256(vector_file.read_bytes()).hexdigest(),
        'producer_sha256': hashlib.sha256((root/'level4_invariant_check.py').read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (root/'level4-independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__ == '__main__':
    main()
