#!/usr/bin/env python3
"""Exercise valid certificates and independent adversarial mutations.
Run from target dir: python3 work/test_checker.py
"""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
from check_lkts import check, parse_certificate

root = Path(__file__).resolve().parent.parent
v, good = parse_certificate(root / "evidence/cyclic9.txt")
results = []


def expect(name, action, accepted):
    try:
        action()
        observed = True
        reason = None
    except ValueError as error:
        observed = False
        reason = str(error)
    assert observed == accepted, (name, observed, reason)
    results.append({"case":name,"expected_accept":accepted,"observed_accept":observed,"reason":reason})


expect("known9",lambda:check(v,good),True)
expect("known15_search",lambda:check(*parse_certificate(root/"evidence/cyclic15.txt")),True)
expect("known15_Denniston",lambda:check(*parse_certificate(root/"evidence/denniston15.txt")),True)
expect("degenerate3",lambda:check(3,[[[(0,1,2)]]]),True)
expect("admissibility",lambda:check(7,good),False)
expect("missing_KTS",lambda:check(v,good[:-1]),False)
expect("extra_KTS",lambda:check(v,good+[good[0]]),False)
for name, mutation in [
    ("repeated_point_in_triple",lambda s:s[0][0].__setitem__(0,(0,0,1))),
    ("out_of_range",lambda s:s[0][0].__setitem__(0,(0,1,v))),
    ("non_integer",lambda s:s[0][0].__setitem__(0,(0,1,2.5))),
    ("wrong_triple_length",lambda s:s[0][0].__setitem__(0,(0,1))),
    ("missing_parallel_class",lambda s:s[0].pop()),
    ("missing_block",lambda s:s[0][0].pop()),
    ("repeated_block_in_class",lambda s:s[0][0].__setitem__(1,s[0][0][0])),
    ("repeated_parallel_class",lambda s:s[0].__setitem__(1,s[0][0])),
    ("constituents_identical",lambda s:s.__setitem__(1,s[0])),
    ("foreign_parallel_class",lambda s:s[0].__setitem__(0,s[1][0])),
]:
    corrupted = copy.deepcopy(good)
    mutation(corrupted)
    expect(name,lambda s=corrupted:check(v,s),False)
# Valid relabelling, block reordering, and resolution reordering must be accepted.
changed = [[list(reversed([tuple((2*x+1)%v for x in b) for b in pc])) for pc in reversed(system)] for system in reversed(good)]
expect("isomorphic_reordering",lambda:check(v,changed),True)
with tempfile.TemporaryDirectory(prefix="lkts-checker-",dir="/tmp") as tmp:
    p = Path(tmp)/"bad.txt"
    for name,text in [
        ("missing_header","KTS 0\nCLASS 0\n0 1 2\n"),
        ("duplicate_header","LKTS 3\nLKTS 3\nKTS 0\nCLASS 0\n0 1 2\n"),
        ("bad_system_id","LKTS 3\nKTS 1\nCLASS 0\n0 1 2\n"),
        ("bad_class_id","LKTS 3\nKTS 0\nCLASS 1\n0 1 2\n"),
        ("unknown_keyword","LKTS 3\nKTS 0\nCLASS 0\nBOGUS\n"),
    ]:
        p.write_text(text)
        expect(name,lambda:parse_certificate(p),False)
receipt = {"verdict":"PASS","cases":results,"case_count":len(results),
           "checker_sha256":hashlib.sha256((root/"work/check_lkts.py").read_bytes()).hexdigest(),
           "test_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/"evidence/checker-mutations.json").write_text(json.dumps(receipt,indent=2))
print(json.dumps({"verdict":"PASS","case_count":len(results)}))
