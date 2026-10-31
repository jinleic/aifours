#!/usr/bin/env python3
"""Direct Walsh control with nonzero quadratic polar form, without author code."""
import functools
import hashlib
import json
import operator
import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
M = (set(range(256, 512)) - {256, 259, 320}) | {1, 2, 64}
assert len(M) == 256 and 0 not in M
T = functools.reduce(operator.xor, M, 0)
assert T == 256
W = [sum((-1 if x in M else 1) * (-1 if (a & x).bit_count() & 1 else 1)
         for x in range(512)) for a in range(512)]
assert W[0] == 0 and all(v % 4 == 0 for v in W)
k = [v//4 for v in W]
assert sum(v*v for v in k) == 16384
assert all(v % 2 == a//256 for a,v in enumerate(k))
q = [k[x]//2 % 2 for x in range(256)]
Q = [(k[256+x]-1)//2 % 2 for x in range(256)]
q_formula = [((x >> 0)&1)*((x >> 1)&1) for x in range(256)]
Q_formula = [q_formula[x] ^ ((x >> 0)&1) ^ ((x >> 1)&1) ^ ((x >> 6)&1) for x in range(256)]
assert q == q_formula and Q == Q_formula
assert all((q[u^v]^q[u]^q[v]^q[0]) == (Q[u^v]^Q[u]^Q[v]^Q[0])
           for u in range(256) for v in range(256))
truth = bytes(int(x in M) for x in range(512))
receipt = {
    'support':'{256,...,511} minus {256,259,320} union {1,2,64}',
    'truth_table_sha256':hashlib.sha256(truth).hexdigest(),
    'support_size':len(M),'T':T,'max_abs_W':max(map(abs,W)),
    'satisfies_28_cap':max(map(abs,W)) <= 28,
    'q_formula':'x0*x1','Q_formula':'x0*x1+x0+x1+x6',
    'q_zero_count':q.count(0),'Q_one_count':sum(Q),'common_polar_rank':2,
    'polar_pairs_checked':256*256,'sum_k_squared':sum(v*v for v in k),
    'native_clock_before_receipt':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
}
with (root/'independent-balanced-nontrivial-result-v1.json').open('x') as f:
    json.dump(receipt,f,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps(receipt,indent=2))
