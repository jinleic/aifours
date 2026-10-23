#!/usr/bin/env python3
"""Base-word files for rot_nbhd.cpp (rotation slice, 2026-10-18).  Reads only unchanged olson/ evidence files.
  p5: all 3,730 exhaustive D10 avoiders of length 18 (converted as in test_grx_v1.d10_dump), scaled so that the
      rotation values are +-1 (automorphism v -> v/x on all letters).
  p7: every 'all' row of olson/evidence/was/p7_N26_all.jsonl (RGR avoiders, x = 1).
Usage: make_bases_v1.py p OUTFILE   (OUTFILE created exclusively)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import test_grx_v1 as T  # noqa: E402


def norm(w, p):
    xs = [v % p for k, v in w if k == 'r']
    if not xs:
        return w
    inv = pow(xs[0], p - 2, p)
    return [(k, (v * inv) % p) for k, v in w]


def main():
    p, out = int(sys.argv[1]), sys.argv[2]
    words = [norm(w, 5) for w in T.d10_dump()] if p == 5 else T.p7_was()
    with open(out, 'x') as f:
        f.write('%d\n' % p)
        for w in words:
            f.write(' '.join('%s%d' % (k, v) for k, v in w) + '\n')
    print(len(words))


if __name__ == '__main__':
    main()
