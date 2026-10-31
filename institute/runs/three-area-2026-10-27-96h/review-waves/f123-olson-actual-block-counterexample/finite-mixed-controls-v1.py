#!/usr/bin/env python3
"""Find actual original-word 2p mixed identity selectors by exact reachability.

This additional finite control reads only the SHA-pinned independently built
word instances, not an author checker.  States retain one original-index
witness for each (selected length, full dihedral product, used-kind mask).
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess

INPUT = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f123-olson-actual-block-counterexample/finite-results-v1.json')
INPUT_SHA = '8107905a7fc10830aa607ff3f1854940ce542b56f728c6f82f611b60776c8375'


def require(value, reason):
    if not value:
        raise ValueError(reason)


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def combine(x, y, p):
    a, parity = x
    b, flip = y
    return ((a + (-b if parity else b)) % p, parity ^ flip)


def multiply_indices(word, indices, p):
    current = (0, 0)
    for i in indices:
        current = combine(current, word[i], p)
    return current


def parse_word(tokens, p):
    result = []
    for token in tokens:
        require(len(token) >= 2 and token[0] in 'rs' and token[1:].isdigit(), 'invalid token')
        value = int(token[1:])
        require(0 <= value < p, 'invalid exponent')
        result.append((value, 0 if token[0] == 'r' else 1))
    require(len(result) == 4 * p - 1, 'unexpected original length')
    return result


def find_selector(word, p):
    # Each input position is either skipped or appended exactly once in order.
    states = {(0, 0, 0, 0): ()}
    for i, token in enumerate(word):
        updated = dict(states)
        for (k, a, parity, kinds), indices in states.items():
            if k >= 2 * p:
                continue
            new_a, new_parity = combine((a, parity), token, p)
            key = (k + 1, new_a, new_parity, kinds | (1 if token[1] == 0 else 2))
            if key not in updated:
                updated[key] = indices + (i,)
        states = updated
    selector = states.get((2 * p, 0, 0, 3))
    require(selector is not None, 'no mixed identity reached for this original word')
    require(len(selector) == 2 * p and tuple(sorted(set(selector))) == selector,
            'invalid selected original indices')
    require(multiply_indices(word, selector, p) == (0, 0), 'replayed selector not identity')
    require({word[i][1] for i in selector} == {0, 1}, 'selector is not mixed')
    used = set(selector)
    negative = None
    for removed in selector:
        for added in range(len(word)):
            if added in used:
                continue
            mutant = sorted((used - {removed}) | {added})
            if multiply_indices(word, mutant, p) != (0, 0):
                negative = {'removed': removed, 'added': added, 'indices': mutant,
                            'direct_product': multiply_indices(word, mutant, p)}
                break
        if negative:
            break
    require(negative is not None, 'no one-index negative control')
    return {'p': p, 'indices_0_based': selector,
            'rotation_count': sum(word[i][1] == 0 for i in selector),
            'reflection_count': sum(word[i][1] == 1 for i in selector),
            'direct_product': multiply_indices(word, selector, p),
            'reachable_states': len(states), 'one_index_nonidentity_control': negative}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = clock()
    raw = INPUT.read_bytes()
    require(sha256(raw).hexdigest() == INPUT_SHA, 'finite word-instance result SHA mismatch')
    data = json.loads(raw)
    require([case['p'] for case in data['instances']] == [7, 11, 13, 17], 'unexpected instance set')
    controls = []
    for case in data['instances']:
        p = case['p']
        controls.append(find_selector(parse_word(case['word_tokens_0_based'], p), p))
    source = Path(__file__).read_bytes()
    receipt = {'status': 'PASS_ORIGINAL_MIXED_IDENTITY_CONTROLS',
               'scope': 'explicit selectors for these four original finite words only; no SEL predicate or L_RES conclusion',
               'clock_before_start': started, 'input_path': str(INPUT),
               'input_sha256': INPUT_SHA, 'input_bytes': len(raw), 'input_LF': raw.count(b'\n'),
               'checker_sha256': sha256(source).hexdigest(),
               'checker_bytes': len(source), 'checker_LF': source.count(b'\n'),
               'controls': controls}
    receipt['clock_before_exclusive_output_write'] = clock()
    with open(args.output, 'x', encoding='utf-8') as out:
        json.dump(receipt, out, sort_keys=True, indent=2)
        out.write('\n')
    print(json.dumps({'status': receipt['status'], 'output': args.output,
                      'checker_sha256': receipt['checker_sha256']}))


if __name__ == '__main__':
    main()
