#!/usr/bin/env python3
"""witness_structure.py -- informational description of a v = 100 T2 seed (not acceptance): base blocks in CRT
coordinates (residue mod 25, height mod 4), the full block containing {0, 20}, and the units u mod 100 with
u * B = B for the developed design (multiplier automorphisms).
Usage: witness_structure.py SEED
"""
import math
import sys


def main(argv):
    lines = open(argv[1]).read().rstrip("\n").split("\n")
    blocks = [(l.split()[0], list(map(int, l.split()[1:]))) for l in lines[1:]]
    design = set()
    for tag, B in blocks:
        for t in range(100):
            design.add(tuple(sorted((x + t) % 100 for x in B)))
    for tag, B in blocks:
        print(tag, B, "(residue mod 25, height mod 4):", sorted((x % 25, x % 4) for x in B))
    print("blocks containing {0, 20}:", sorted(B for B in design if 0 in B and 20 in B))
    print("design blocks:", len(design))
    mult = [u for u in range(1, 100) if math.gcd(u, 100) == 1
            and {tuple(sorted(u * x % 100 for x in B)) for B in design} == design]
    print("units u with u*B = B:", mult)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
