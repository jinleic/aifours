#!/usr/bin/env python3
"""Independent finite identity assay, not a proof of either all-language theorem.

The actual proofs quantify over arbitrary languages and are in proof.md. This
bounded assay catches parity, derivative-direction and empty-word mutations.
All input languages here have finite support; no sampled nonregular language
is claimed to be certified. Uses the standard library only.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

ALPHABET = 'ab'


def words(max_length):
    return [''.join(w) for n in range(max_length + 1)
            for w in itertools.product(ALPHABET, repeat=n)]


def subsets(items):
    return [frozenset(w for i, w in enumerate(items) if mask >> i & 1)
            for mask in range(1 << len(items))]


def parity(values):
    total = 0
    for value in values:
        total ^= int(value)
    return total


def product_coefficient(left, letter, right, word):
    return parity(left(word[:i]) and right(word[i + 1:])
                  for i, a in enumerate(word) if a == letter)


def derivative_rhs(left, letter, right, prefix, suffix, reverse=False):
    first = product_coefficient(lambda u: left(prefix + u), letter, right, suffix)
    crossed = parity(left(prefix[:i]) and
                     right((suffix + prefix[i + 1:]) if reverse else
                           (prefix[i + 1:] + suffix))
                     for i, a in enumerate(prefix) if a == letter)
    return first ^ crossed


def run():
    short_languages = subsets(words(1))
    contexts = words(3)
    split_cases = 0
    empty_prefix_cases = 0
    for a_language, b_language, letter, x, y in itertools.product(
            short_languages, short_languages, ALPHABET, contexts, contexts):
        left, right = a_language.__contains__, b_language.__contains__
        actual = product_coefficient(left, letter, right, x + y)
        predicted = derivative_rhs(left, letter, right, x, y)
        assert actual == predicted, (a_language, b_language, letter, x, y)
        split_cases += 1
        empty_prefix_cases += not x

    # With two accepting cuts, existential and parity concatenation differ.
    left = frozenset(['', 'a']).__contains__
    right = frozenset(['', 'a']).__contains__
    ordinary = any(left('aa'[:i]) and right('aa'[i + 1:]) for i in range(2))
    parity_value = product_coefficient(left, 'a', right, 'aa')
    assert ordinary and parity_value == 0

    # The crossed residual is LEFT, not right: a^{-1}{ab} contains b.
    left = frozenset(['']).__contains__
    right = frozenset(['ab']).__contains__
    direction_actual = product_coefficient(left, 'a', right, 'aab')
    direction_mutant = derivative_rhs(left, 'a', right, 'aa', 'b', reverse=True)
    assert direction_actual == 1 and direction_mutant == 0

    normal_cases = 0
    no_terminal_witness = None
    existential_witness = None
    representatives = ['', 'a']
    for support, transitions in itertools.product(subsets(words(2)),
                                                  itertools.product(range(2), repeat=4)):
        def step(q, a):
            return transitions[2 * q + ALPHABET.index(a)]

        def state(word):
            q = 0
            for a in word:
                q = step(q, a)
            return q

        def error(q, a, suffix):
            return ((representatives[q] + a + suffix in support) ^
                    (representatives[step(q, a)] + suffix in support))

        for word in words(6):
            terminal = int(representatives[state(word)] in support)
            # Evaluate the grouped finite language expression, independently
            # of iterating the residual recurrence along the input word.
            summands = [product_coefficient(
                lambda u, q=q: state(u) == q,
                letter,
                lambda suffix, q=q, letter=letter: error(q, letter, suffix),
                word)
                for q, letter in itertools.product(range(2), ALPHABET)]
            expression = terminal ^ parity(summands)
            assert expression == int(word in support), (support, transitions, word)
            normal_cases += 1
            if no_terminal_witness is None and parity(summands) != int(word in support):
                no_terminal_witness = {'support': sorted(support), 'word': word,
                                       'transitions': list(transitions)}
            if existential_witness is None and int(any([terminal] + summands)) != int(word in support):
                existential_witness = {'support': sorted(support), 'word': word,
                                       'transitions': list(transitions)}
    assert no_terminal_witness is not None
    assert existential_witness is not None
    return {
        'schema': 'semifilter-parity-assay/1',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_checked_equalities_passed': True,
        'derivative_split_cases': split_cases,
        'empty_prefix_split_cases': empty_prefix_cases,
        'normal_form_coefficient_cases': normal_cases,
        'input_scope': {'alphabet': ALPHABET, 'split_support_max_length': 1,
                        'split_prefix_and_suffix_max_length': 3,
                        'normal_form_support_max_length': 2,
                        'normal_form_test_word_max_length': 6,
                        'normal_form_states': 2, 'normal_form_transition_tables': 16},
        'negative_controls': {
            'existential_product': {'left': ['', 'a'], 'right': ['', 'a'],
                                    'letter': 'a', 'word': 'aa',
                                    'parity_value': parity_value, 'existential_value': int(ordinary)},
            'right_instead_of_left_quotient': {'left': [''], 'right': ['ab'],
                                             'letter': 'a', 'prefix': 'aa', 'suffix': 'b',
                                             'correct': direction_actual, 'mutant': direction_mutant},
            'omitted_terminal_term': no_terminal_witness,
            'existential_outer_sum': existential_witness},
        'limits': 'Bounded independent coefficient assay only. Not a proof of Q2, Q3, regularity of an infinite language, or novelty.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2) + '\n'
    if args.output:
        if args.output.exists():
            raise SystemExit('Refusing to overwrite an existing receipt')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end='')
