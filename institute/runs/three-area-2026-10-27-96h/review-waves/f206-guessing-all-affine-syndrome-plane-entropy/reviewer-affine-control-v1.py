#!/usr/bin/env python3
"""Independent finite controls from the two displayed frozen inputs only."""
from collections import Counter
from itertools import combinations, permutations

N = {
  1:{2,3,4,5,6,7}, 2:{1,3,7,9,10}, 3:{1,2,4,8,9},
  4:{1,3,5,8,10}, 5:{1,4,6,9,10}, 6:{1,5,7,8,9},
  7:{1,2,6,8,10}, 8:{3,4,6,7,9,10}, 9:{2,3,5,6,8},
  10:{2,4,5,7,8},
}
T = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
     (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
E = {tuple(sorted((v,w))) for v in N for w in N[v]}
assert all(v not in N[v] and all(v in N[w] for w in N[v]) for v in N)
assert len(E) == 26
assert all(tuple(sorted(pair)) in E for t in T for pair in combinations(t,2))
assert all(sum(v in t for t in T) == 3 for v in N)
assert (3,4) in E and (9,10) not in E
TE = {tuple(sorted(pair)) for t in T for pair in combinations(t,2)}
print('graph: vertices=10 edges=%d triangle-union-edges=%d extra=%s' %
      (len(E), len(TE), sorted(E-TE)))

# Independently enumerate graph automorphisms, then retain factor-set actions.
degree_six = (1,8)
degree_five = (2,3,4,5,6,7,9,10)
tset = {frozenset(t) for t in T}
graph_group, factor_group = [], []
for six in permutations(degree_six):
    for five in permutations(degree_five):
        p = dict(zip(degree_six + degree_five, six + five))
        if {tuple(sorted((p[v],p[w]))) for v,w in E} != E:
            continue
        graph_group.append(p)
        if {frozenset(p[v] for v in t) for t in T} == tset:
            factor_group.append(p)
print('automorphisms: graph=%d factor_preserving=%d' % (len(graph_group),len(factor_group)))
assert graph_group and factor_group

# Use only the literal representative visibility sets in the manuscript.
reps = [(6,),(7,),(2,5),(9,10),(1,2,10),(1,5,9),(5,8,9),(2,8,10)]
def mask(vertices):
    out=0
    for v in vertices:
        out |= 1 << (v-1)
    return out
vis_masks = sorted({mask(p[v] for v in rep) for p in factor_group for rep in reps})
print('visibility: representatives=%d distinct_transports=%d' % (len(reps),len(vis_masks)))
inc = {v:[i for i,t in enumerate(T) if v in t] for v in N}
union = []
for s in range(1<<10):
    union.append(mask(v for i,t in enumerate(T) if s >> i & 1 for v in t))

# Every 2-plane has unique ordered triple a<b<c=a XOR b, hence a,b enumerate it once.
counts=Counter()
factor_counts=Counter()
all_planes=set()
for a in range(1,1<<10):
    for b in range(a+1,1<<10):
        if (a^b) <= b:
            continue
        all_planes.add((a,b))
        colors=[((a>>i)&1) | (((b>>i)&1)<<1) for i in range(10)]
        support=sum((1<<i) for i,x in enumerate(colors) if x)
        size=sum(bool(x) for x in colors)
        factor_counts[size]+=1
        if union[support] != (1<<10)-1:
            counts['noncover']+=1
        elif size == 4:
            counts['cover_four']+=1
        else:
            visible=mask(v for v in N if len({colors[i] for i in inc[v] if colors[i]}) >= 2)
            if any(visible & r == r for r in vis_masks):
                counts['full_visibility']+=1
            else:
                counts['other_cover']+=1
print('planes: total=%d expected_formula=%d factor_size_counts=%s' %
      (len(all_planes), 1023*1022//6, sorted(factor_counts.items())))
print('disjoint_ordered_counts:',dict(counts))
assert len(all_planes) == 1023*1022//6 == sum(counts.values())

# Pairwise FD check for a two-point binary law and explicit component-local decoder.
def law_negative_case(a_factor):
    # Direction a is on a_factor, direction b is on factors 145 and 569.
    # Both support words have a=0; their shared changing bit b is copied at vertices 1 and 6.
    colors=[0]*10
    colors[a_factor]=1
    colors[1]=colors[8]=2
    words=[]
    for bval in (0,1):
        word={(i,v):0 for i,t in enumerate(T) for v in t}
        word[1,1]=bval
        word[8,6]=bval
        words.append(word)
    def y(word,v):
        return tuple(word[i,v] for i in inc[v] if colors[i])
    def yn(word,vs):
        return tuple(y(word,v) for v in sorted(vs))
    for w,bval in zip(words,(0,1)):
        assert all((sum(w[i,v] for v in t)%2)==(bval if colors[i]==2 else 0)
                   for i,t in enumerate(T))
    # Since only vertices 1 and 6 vary and are adjacent, every original FD holds.
    for v in N:
        assert yn(words[0],N[v]) != yn(words[1],N[v]) or y(words[0],v)==y(words[1],v)
    incident={colors[i] for i in inc[1] if colors[i]}
    local={v for i in inc[1] if colors[i] for v in T[i] if v != 1}
    assert yn(words[0],local)==yn(words[1],local)
    assert y(words[0],1)!=y(words[1],1)
    # a=0 in both words cannot decode; b separates the words.
    assert (0,yn(words[0],local))==(0,yn(words[1],local))
    assert (0,yn(words[0],local))!=(1,yn(words[1],local))
    return incident,sorted(local)
assert law_negative_case(3)[0] == {2}  # wrong auxiliary at a singleton-color vertex
assert law_negative_case(0)[0] == {1,2}  # wrong singleton predicate at a mixed vertex
print('negative controls: wrong-functional singleton and mixed-color singleton both rejected; original FDs hold')

# Rank-one input and same-cardinality wrong-set check must not be mistaken for valid coverage.
rank_one=(1,1)
assert rank_one not in all_planes
ordered=sorted(all_planes)
S=set(ordered[:100]); wrong=(S-{ordered[0]})|{ordered[100]}
assert len(S)==len(wrong) and S!=wrong
print('negative controls: rank-one fake rejected; same-count unequal sets detected')

# An incorrect graph or factor mutation must trip the stated structural conditions.
mutated=list(T); mutated[0]=(1,2,8)
assert not all(tuple(sorted(pair)) in E for t in mutated for pair in combinations(t,2))
print('negative control: non-clique factor rejected')
