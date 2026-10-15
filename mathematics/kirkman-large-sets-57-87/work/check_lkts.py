#!/usr/bin/env python3
"""Independent, standard-library-only checker for an explicit LKTS certificate.

Text format: LKTS <v>; KTS <id>; CLASS <id>; then one line per triple.
Ids are zero-based, consecutive. Blank lines and # comments are ignored.
Every point is an integer in range(v); no automorphism assumptions are used.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys


def parse_certificate(path):
    v = None
    systems = []
    for lineno, raw in enumerate(Path(path).read_text().splitlines(), 1):
        line = raw.partition("#")[0].strip()
        if not line:
            continue
        fields = line.split()
        try:
            if fields[0] == "LKTS":
                if len(fields) != 2 or v is not None or systems:
                    raise ValueError("invalid/duplicate LKTS header")
                v = int(fields[1])
            elif fields[0] == "KTS":
                if v is None or len(fields) != 2 or int(fields[1]) != len(systems):
                    raise ValueError("KTS ids must be consecutive starting at zero")
                systems.append([])
            elif fields[0] == "CLASS":
                if not systems or len(fields) != 2 or int(fields[1]) != len(systems[-1]):
                    raise ValueError("CLASS ids must be consecutive within each KTS")
                systems[-1].append([])
            else:
                if not systems or not systems[-1] or len(fields) != 3:
                    raise ValueError("a triple needs three points inside a CLASS")
                systems[-1][-1].append(tuple(map(int, fields)))
        except ValueError as error:
            raise ValueError(f"line {lineno}: {error}") from error
    if v is None:
        raise ValueError("missing LKTS header")
    return v, systems


def check(v, systems):
    if type(v) is not int or v < 3 or v % 6 != 3:
        raise ValueError("v must be an integer >=3 congruent to 3 modulo 6")
    if len(systems) != v - 2:
        raise ValueError(f"expected {v - 2} systems, found {len(systems)}")
    points = set(range(v))
    all_pairs = set(itertools.combinations(range(v), 2))
    all_triples = set(itertools.combinations(range(v), 3))
    union = set()
    for si, system in enumerate(systems):
        if len(system) != (v - 1) // 2:
            raise ValueError(f"KTS {si}: wrong number of parallel classes")
        pairs = set()
        blocks = set()
        for ci, parallel in enumerate(system):
            if len(parallel) != v // 3:
                raise ValueError(f"KTS {si} CLASS {ci}: wrong number of blocks")
            used = set()
            for block in parallel:
                if len(block) != 3 or any(type(x) is not int for x in block):
                    raise ValueError(f"KTS {si} CLASS {ci}: malformed triple")
                b = tuple(sorted(block))
                if len(set(b)) != 3 or not set(b) <= points:
                    raise ValueError(f"KTS {si} CLASS {ci}: not a 3-subset of the point set")
                if used.intersection(b):
                    raise ValueError(f"KTS {si} CLASS {ci}: repeated point")
                used.update(b)
                if b in blocks:
                    raise ValueError(f"KTS {si}: repeated block")
                blocks.add(b)
                for pair in itertools.combinations(b, 2):
                    if pair in pairs:
                        raise ValueError(f"KTS {si}: repeated pair {pair}")
                    pairs.add(pair)
            if used != points:
                raise ValueError(f"KTS {si} CLASS {ci}: class is not a partition")
        if pairs != all_pairs or len(blocks) != v * (v - 1) // 6:
            raise ValueError(f"KTS {si}: not a Steiner triple system")
        if union.intersection(blocks):
            raise ValueError(f"KTS {si}: shares a block with an earlier system")
        union.update(blocks)
    if union != all_triples:
        raise ValueError("union is not all triples")
    return {"verdict": "PASS", "v": v, "systems": len(systems),
            "classes_per_system": (v - 1) // 2, "blocks_per_system": v * (v - 1) // 6,
            "total_distinct_blocks": len(union), "expected_total": math.comb(v, 3)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        result = check(*parse_certificate(args.certificate))
    except (ValueError, OSError) as error:
        print(json.dumps({"verdict": "FAIL", "error": str(error)}))
        return 1
    result["certificate_sha256"] = hashlib.sha256(args.certificate.read_bytes()).hexdigest()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
