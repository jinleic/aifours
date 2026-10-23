#!/usr/bin/env python3
"""Exhaustively recompute deterministic, separated windows with Python integers.

Every class member in each stated window receives a FULL modular power, even
when the production sieve would reject its modulus. Hash canonical records
(n, decision, full residue) for EVERY member. Only a subset of any main scan is
checked; hashes do not certify the rest. No C binary/source is loaded.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--start', type=int, default=200000000000)
    p.add_argument('--step', type=int, default=24)
    p.add_argument('--block-size', type=int, default=8388608)
    p.add_argument('--every-blocks', type=int, default=512)
    p.add_argument('--windows', type=int, default=100)
    p.add_argument('--length', type=int, default=1048576)
    p.add_argument('--first-window', type=int, default=0)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    assert args.start >= 2 and args.step > 0 and args.length > 0
    assert args.length <= args.block_size and args.every_blocks > 0
    assert args.windows > 0 and args.first_window >= 0
    any_hits = False
    with Path(args.output).open('x') as out:
        for w in range(args.first_window, args.first_window+args.windows):
            t0 = time.monotonic()
            block = w*args.every_blocks
            start = args.start+args.step*args.block_size*block
            stop = start+args.step*args.length
            digest = hashlib.sha256()
            hits = []
            for n in range(start, stop, args.step):
                modulus = n*n+n+1
                residue = pow(2, n+1, modulus)
                decision = 'base2-fail' if residue != 1 else 'needs-exact-elimination'
                digest.update(('%d\t%s\t%d\n' % (n, decision, residue)).encode())
                if residue == 1:
                    hits.append(dict(n=n, p=str(modulus), residue=str(residue)))
                    any_hits = True
            record = dict(window=w, block=block, start=start, end=stop,
                          step=args.step, count=args.length,
                          base_two_hits=hits,
                          sha256_every_n_decision_full_residue=digest.hexdigest(),
                          seconds=time.monotonic()-t0)
            line = json.dumps(record, separators=(',', ':'))+'\n'
            out.write(line); out.flush()
            print(line, end='', flush=True)
    if any_hits:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
