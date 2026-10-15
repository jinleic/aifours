#!/usr/bin/env python3
"""Check explicit disjoint resolved KTSs WITHOUT claiming a full large set.
Format: PACKING v k, KTS i, CLASS j, then integer triples, zero-based ids.
Run: python3 work/check_partial_packing.py evidence/c19-partial17.txt --expected-systems 17
This checker imports neither search code nor the full LKTS checker.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("certificate",type=Path)
ap.add_argument("--expected-systems",type=int,required=True)
ap.add_argument("--output",type=Path)
args = ap.parse_args()
lines = [line.partition("#")[0].split() for line in args.certificate.read_text().splitlines()]
lines = [row for row in lines if row]
assert len(lines[0]) == 3 and lines[0][0] == "PACKING"
v,k = map(int,lines[0][1:])
assert v>=3 and v%6==3 and 1<=k<=v-2 and k==args.expected_systems
systems = []
for row in lines[1:]:
    if row[0] == "KTS":
        assert len(row)==2 and int(row[1])==len(systems)
        systems.append([])
    elif row[0] == "CLASS":
        assert systems and len(row)==2 and int(row[1])==len(systems[-1])
        systems[-1].append([])
    else:
        assert systems and systems[-1] and len(row)==3
        block = tuple(sorted(map(int,row)))
        assert len(set(block))==3 and 0<=block[0]<block[-1]<v
        systems[-1][-1].append(block)
assert len(systems)==k
all_blocks = Counter()
expected_pairs = Counter(itertools.combinations(range(v),2))
for system in systems:
    assert len(system)==(v-1)//2
    pairs = Counter()
    for parallel in system:
        assert len(parallel)==v//3
        assert Counter(x for block in parallel for x in block)==Counter(range(v))
        for block in parallel:
            pairs.update(itertools.combinations(block,2))
            all_blocks[block] += 1
    assert pairs==expected_pairs
assert set(all_blocks.values())=={1}
assert len(all_blocks)==k*v*(v-1)//6
result = {"verdict":"PASS","certificate_type":"PARTIAL_KTS_PACKING","v":v,"systems":k,
          "required_for_full_large_set":v-2,"is_full_large_set":k==v-2,
          "classes_per_system":(v-1)//2,"blocks_per_system":v*(v-1)//6,
          "distinct_blocks":len(all_blocks),"total_possible_triples":math.comb(v,3),
          "certificate_sha256":hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
          "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if args.output:
    args.output.write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
