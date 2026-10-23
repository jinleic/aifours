#!/usr/bin/env python3
"""Find exact proper factors for the exceptional pure-power exponents 3^t.

The proof in POWER-TWO-LEMMA.md eliminates all other exponents when p is prime.
This is a restricted family of the original question, never an all-orders claim.
Only actual exact factors count. A search limit or timeout remains unresolved.
"""
import argparse
import json
from pathlib import Path
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--first-t', type=int, default=3)
    parser.add_argument('--last-t', type=int, default=8)
    parser.add_argument('--bound', type=int, default=10000000)
    parser.add_argument('--cap', type=float, default=30)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    assert 3 <= args.first_t <= args.last_t <= 16 and args.bound >= 2 and args.cap > 0
    start = time.monotonic()
    rows = []
    for t in range(args.first_t, args.last_t+1):
        a = 3**t
        p = (1 << (2*a)) + (1 << a) + 1
        factor = None
        last_q = 1
        timed_out = False
        stride = 6*a
        for k, q in enumerate(range(stride+1, args.bound+1, stride)):
            if k % 4096 == 0 and time.monotonic()-start >= args.cap:
                timed_out = True
                break
            last_q = q
            if p % q == 0 and 1 < q < p:
                factor = q
                break
        row = dict(t=t, a=a, n_expression='2^%d' % a,
                   p_expression='2^%d+2^%d+1' % (2*a, a), p_bits=p.bit_length(),
                   proper_factor=factor, searched_q_max=last_q,
                   search_stride=stride, timed_out=timed_out)
        rows.append(row)
        print(json.dumps(row), flush=True)
        if factor is None:
            break
    result = dict(rows=rows, seconds=time.monotonic()-start,
                  bound=args.bound, cap_seconds=args.cap,
                  limitation='An unsuccessful factor search is not primality or nonexistence. Only displayed proper factors eliminate cases.')
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
