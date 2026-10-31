#!/usr/bin/env python3
"""Independently enumerate all local parity tuples of rank at most 7.

Branch-and-bound visits the full 7^10 choice tree except subtrees that have
already accumulated rank 8; rank cannot later decrease.  The rank calculation
uses two free bits for each triangle, not the ambient quotient construction.
"""
from collections import Counter
from pathlib import Path
import json
import subprocess

T = ((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
     (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
occ = {v:[j for j,t in enumerate(T) if v in t] for v in range(1,11)}
coords = [(v,j) for v in range(1,11) for j in occ[v]]
pos = {item:i for i,item in enumerate(coords)}
options = []
for v in range(1,11):
    vv = []
    for mask in range(1,8):
        c20 = c30 = 0
        for i,j in enumerate(occ[v]):
            if not (mask & (1<<i)):
                continue
            k = T[j].index(v)
            c20 ^= (1<<(2*j)) if k==0 else (1<<(2*j+1)) if k==1 else (3<<(2*j))
            c30 ^= 1<<pos[v,j]
        vv.append((c20,c30))
    options.append(vv)

piv = [0]*20
choice = [0]*10
leaves = []
visits = [0]*11
pruned = [0]*11
rank_counts = Counter()

def visit(depth, rk):
    visits[depth] += 1
    if depth==10:
        rank_counts[rk] += 1
        leaves.append(tuple(choice))
        return
    for c20,c30 in options[depth]:
        x = c20
        while x:
            b = x.bit_length()-1
            if not piv[b]:
                break
            x ^= piv[b]
        if x and rk==7:
            pruned[depth+1] += 1
            continue
        choice[depth] = c30
        if x:
            piv[b] = x
            visit(depth+1,rk+1)
            piv[b] = 0
        else:
            visit(depth+1,rk)

visit(0,0)
assert len(leaves)==len(set(leaves))
assert dict(rank_counts)=={7:61}
review_dir=Path(__file__).parent
first=json.loads((review_dir/'independent-enumeration-result.json').read_text())
quotient_tuples={tuple(r['local_parity_masks_30bit']) for r in first['cases']}
assert set(leaves)==quotient_tuples
out={
 'clock_observed_before_receipt_write':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
 'method':'all seven nonzero local forms per vertex, monotonic-rank pruning at 8',
 'unpruned_choice_tree_total_leaves':7**10,
 'node_visits_by_depth':visits,
 'rank_8_pruned_subtrees_by_depth':pruned,
 'full_tuples_by_rank_at_most_7':dict(rank_counts),
 'all_61_local_tuples_equal_quotient_enumeration':True,
 'all_61_tuples_30bit':leaves,
}
with (review_dir/'independent-local-rank-result.json').open('x',encoding='utf-8') as f:
    json.dump(out,f,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_61_tuples_30bit'},indent=2))
