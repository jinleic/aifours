#!/usr/bin/env python3
"""Independently verify the finite factor chain and exceptional D collision.

The universal reduction of exponents is a mathematical proof, not an assertion
that this script enumerates all exponents or solves the headline conjecture.
The producing factor search used full big integers; this checker uses small
modular binary exponentiation and imports no producing code.
"""
import json
from pathlib import Path
import sys


def need(ok, message):
    if not ok:
        raise ValueError(message)


def power(a, b, m):
    answer = 1
    while b:
        if b % 2:
            answer = (answer*a) % m
        a = (a*a) % m
        b //= 2
    return answer


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'evidence/power-two-family.json'
    data = json.loads(Path(path).read_text())
    stop = data['first_unresolved_t']
    need(data['max_exponent_exclusive'] == 3**stop, 'family exponent bound')
    need([r['t'] for r in data['factors']] == list(range(3, stop)), 'gap in exponent chain')
    for r in data['factors']:
        a = r['a']; q = r['proper_factor']
        need(a == 3**r['t'], 'wrong exponent')
        # q<2^(2a) proves properness without writing a huge decimal p.
        need(1 < q < 2**(2*a), 'factor not proper')
        residue = power(2, a, q)
        need(residue == r['two_to_a_mod_factor'], 'small modular witness mismatch')
        need((residue*residue+residue+1) % q == 0, 'claimed factor does not divide p')
    need(data['excluded_small_exponent'] == 9, 'small exception missing')
    controls = json.loads(Path(data['small_collision_source']).read_text())['controls']
    r = next(r for r in controls if r['n'] == 512)
    need(int(r['p']) == 262657, 'wrong n=512 modulus')
    # Independently prove this small p prime by trial division.
    need(all(262657 % d for d in range(2, 513)), 'p=262657 not prime')
    w = r['result']; ab = tuple(w['pair1']); cd = tuple(w['pair2'])
    need(w['kind'] == 'difference-collision' and ab != cd, 'missing collision')
    need(ab[0] != ab[1] and cd[0] != cd[1], 'diagonal pair')
    need(all(0 < x < 262657 and power(x, 513, 262657) == 1 for x in ab+cd), 'collision outside D')
    need((ab[0]-ab[1]) % 262657 == (cd[0]-cd[1]) % 262657 != 0, 'false collision')
    print('PASS: exact witnesses plus the proved exponent reduction exclude only powers-of-two orders 2^a with 3<a<%d. All other orders and a>=%d remain outside this claim.' % (3**stop, 3**stop))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, AssertionError, KeyError, IndexError) as error:
        print('CHECK FAILED: '+str(error), file=sys.stderr)
        sys.exit(1)
