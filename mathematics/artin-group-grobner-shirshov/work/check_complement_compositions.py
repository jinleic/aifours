"""Bounded explicit intersection/inclusion checks using the UNBOUNDED reducer.
Evidence only: the all-rank/all-length result is Theorem G, not these samples.
Usage: python3 work/check_complement_compositions.py SPEC.json --length 10
"""
import argparse
import json
from check_complement_rules import make_reducer

parser = argparse.ArgumentParser()
parser.add_argument('spec')
parser.add_argument('--length', type=int, default=10)
args = parser.parse_args()
data = json.load(open(args.spec))
graph = data['graph']
outgoing = {i: [] for i in range(len(graph['states']))}
for s, t, a, b in graph['edges']:
    outgoing[s].append((t, a, b))
rules = set(tuple(r) for r in data['twists'] + data['cancellations'])
stack = [(graph['start'], '', '')]
while stack:
    s, left, right = stack.pop()
    if len(left) == args.length:
        continue
    for t, a, b in outgoing[s]:
        if t == graph['accept']:
            rules.add((left + a, right + b))
        else:
            stack.append((t, left + a, right + b))
reduce = make_reducer(data)
cache = {}
def nf(w):
    if w not in cache:
        cache[w] = reduce(w)
    return cache[w]
intersection = inclusion = 0
seen = set()
for a, aa in sorted(rules):
    for b, bb in sorted(rules):
        for k in range(1, min(len(a), len(b))):
            if a[-k:] != b[:k]:
                continue
            w = a + b[k:]
            left, right = aa + b[k:], a[:-k] + bb
            key = w, left, right
            if key not in seen:
                seen.add(key)
                assert nf(left) == nf(right), key
                intersection += 1
        pos = a.find(b)
        while pos >= 0:
            left, right = aa, a[:pos] + bb + a[pos + len(b):]
            if left != right:
                key = a, left, right
                if key not in seen:
                    seen.add(key)
                    assert nf(left) == nf(right), key
                    inclusion += 1
            pos = a.find(b, pos + 1)
print(json.dumps({'type':data['type'],'order':data['order'],'leading_length_cap':args.length,
                  'binomials':len(rules),'intersection_compositions':intersection,
                  'inclusion_compositions':inclusion,'all_joinable':True,
                  'scope':'bounded leading words; reductions use the full infinite family'},indent=1))
