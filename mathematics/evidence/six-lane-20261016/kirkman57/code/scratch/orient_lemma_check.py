"""Check the orientation lemma (P ≡ M mod 3 in every class) on the prior
dossier's 17-system C19 packing (read-only input)."""
import sys, collections
path = sys.argv[1]
classes = []; cur = None
for line in open(path):
    line = line.split('#')[0].strip()
    if not line: continue
    t = line.split()
    if t[0] in ('PACKING','LKTS','KTS'): continue
    if t[0] == 'CLASS':
        cur = []; classes.append(cur); continue
    cur.append(tuple(int(x) for x in t))
def orient(b):
    ls=[p//19 for p in b]; c=collections.Counter(ls)
    if len(c)!=2: return None
    two=[l for l,k in c.items() if k==2][0]; one=[l for l,k in c.items() if k==1][0]
    return '+' if one==(two+1)%3 else '-'
bad = 0; dist = collections.Counter()
for C in classes:
    c = collections.Counter(orient(b) for b in C)
    d = (c['+'] - c['-']) % 3
    dist[d] += 1
    if d: bad += 1
print("classes", len(classes), "P-M mod 3 distribution", dict(dist), "violations", bad)
