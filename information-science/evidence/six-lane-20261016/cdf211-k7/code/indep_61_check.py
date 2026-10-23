"""Independent completeness check of the order-3 routines on (61,4,1), sharing no code with o3_models.c.

Enumerate EVERY cyclic (61,4,1) difference family by brute force:
  - all 4-subsets B = {0 < a < b < c} of Z_61 whose 6 unordered differences lie in distinct classes
    (class of d = min(d, 61 - d)), stored with their class sets;
  - exact cover of the 30 classes by 5 class sets (every family is counted once as an unordered set
    of 5 translation classes; a block is identified by its lexicographically least translate).
Then for w = 2^20 mod 61 (order 3) count the families mapped to themselves by x -> w x (as sets of
translation classes) and split them by orbit type (1+1+1+1+1 or 3+1+1).  Expected from o3_models:
type 3+1+1 = 160, all-fixed = 0.
"""
import itertools, json, sys
v, k = 61, 4
cls = lambda d: min(d % v, (-d) % v)
def canon(B):
    return min(tuple(sorted((x - s) % v for x in B)) for s in B)
blocks = {}
for a, b, c in itertools.combinations(range(1, v), 3):
    B = (0, a, b, c)
    cs = [cls(x - y) for x, y in itertools.combinations(B, 2)]
    if len(set(cs)) == 6:
        blocks.setdefault(canon(B), frozenset(cs))
by_class = {}
items = list(blocks.items())
for idx, (B, cs) in enumerate(items):
    for cc in cs: by_class.setdefault(cc, []).append(idx)
fams = []
def search(covered, chosen):
    if len(chosen) == 5:
        if len(covered) == 30: fams.append([items[i][0] for i in chosen])
        return
    c = min(set(range(1, 31)) - covered)
    for i in by_class[c]:
        cs = items[i][1]
        if not (cs & covered) and (not chosen or i > -1):
            search(covered | cs, chosen + [i])
search(frozenset(), [])
# each family found once per ordering of blocks by min uncovered class -> unique; dedupe anyway
fset = {tuple(sorted(F)) for F in fams}
w = pow(2, 20, v)
assert pow(w, 3, v) == 1 and w != 1
inv, t311, tall = 0, 0, 0
for F in fset:
    img = tuple(sorted(canon([w * x % v for x in B]) for B in F))
    if img == F:
        inv += 1
        fixed = sum(1 for B in F if canon([w * x % v for x in B]) == B)
        if fixed == 5: tall += 1
        elif fixed == 2: t311 += 1
out = dict(v=v, k=k, n_good_block_classes=len(blocks), n_families=len(fset), w=w, n_w_invariant=inv,
           n_type_311=t311, n_type_all_fixed=tall)
print(json.dumps(out))
json.dump(out, open(sys.argv[1], "w"), indent=1) if len(sys.argv) > 1 else None
