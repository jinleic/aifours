#!/usr/bin/env python3
"""For a certificate (verify_cdf.py format) and a unit mu, classify each base block B by where mu*B goes:
a translate of a base block (Definition 1.2 sense), or only a translate of a negated base block.
Usage: group_action.py CERT MU"""
import sys


def tclass(block, v):
    return min(tuple(sorted((b - t) % v for b in block)) for t in block)


def main(argv):
    lines = open(argv[1]).read().split("\n")
    v = int(lines[0].split()[1])
    fam = [list(map(int, x.split())) for x in lines[1:] if x]
    mu = int(argv[2]) % v
    base = {tclass(b, v): i for i, b in enumerate(fam)}
    neg = {tclass([(-x) % v for x in b], v): i for i, b in enumerate(fam)}
    to_base = to_self = to_neg = to_own_neg = unclosed = 0
    for i, b in enumerate(fam):
        c = tclass([(mu * x) % v for x in b], v)
        if c in base:
            to_base += 1
            to_self += base[c] == i
        elif c in neg:
            to_neg += 1
            to_own_neg += neg[c] == i
        else:
            unclosed += 1
    strict = to_base == len(fam)
    print("v=%d mu=%d blocks=%d to_translate_of_base=%d (itself %d) to_translate_of_negated_base=%d (own %d) "
          "not_closed=%d definition_1_2_multiplier=%s" % (v, mu, len(fam), to_base, to_self, to_neg, to_own_neg,
                                                         unclosed, strict))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
