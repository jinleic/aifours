#!/usr/bin/env python3
# Independent exact sign realization of the surviving binary residual graph.
import hashlib, itertools, json, subprocess
from collections import Counter, deque
from pathlib import Path

base=Path(__file__).parent
src=base/'enumeration-independent-v1.json'
data=src.read_bytes()
if hashlib.sha256(data).hexdigest() != 'c2254cf5e50e93aeacec00746f6d1099edc62bf4b4b443300d29600fb1b2e42e':
    raise ValueError('independent upstream receipt changed')
items=json.loads(data)['six_fibers_binary']['examples']
selected=[entry for entry in items if entry['bipartite']]
if len(selected)!=1:
    raise ValueError('expected one bipartite support')
S=[tuple(x) for x in selected[0]['S']]
adj={s:set() for s in S}
for s,t in itertools.combinations(S,2):
    if any(s[j]==t[j] for j in range(3)):
        adj[s].add(t); adj[t].add(s)
colors={}
for root in S:
    if root in colors: continue
    colors[root]=0; q=deque([root])
    while q:
        s=q.popleft()
        for t in adj[s]:
            if t in colors and colors[t]==colors[s]: raise ValueError('odd cycle')
            if t not in colors:
                colors[t]=1-colors[s]; q.append(t)
# Integer numerator coefficients; divide all entries by sqrt(2).
E={(a,b,c,d):(1 if b==0 or colors[(a,c,d)]==0 else -1)
   for (a,c,d) in S for b in (0,1)}
if len(E)!=12: raise ValueError('duplicate support')
projections={}
for a,b in itertools.combinations(range(4),2):
    counts=Counter((x[a],x[b]) for x in E)
    projections[f'{a}{b}']={'pairs':len(counts),'multiplicities':sorted(counts.values())}
    if len(counts)!=6 or set(counts.values())!={2}: raise ValueError('pair degree')
matrices={}
for a in (1,2,3):
    # The first coordinate is B=1; pair B with each of the other axes.
    row_axes=(1,0 if a==1 else a)
    col_axes=tuple(i for i in range(4) if i not in row_axes)
    rows=sorted({tuple(p[i] for i in row_axes) for p in E})
    cols=sorted({tuple(p[i] for i in col_axes) for p in E})
    M=[[0 for _ in cols] for _ in rows]
    for x,v in E.items(): M[rows.index(tuple(x[i] for i in row_axes))][cols.index(tuple(x[i] for i in col_axes))]=v
    if len(rows)!=6 or len(cols)!=6: raise ValueError('not six-by-six')
    gram=[[sum(M[i][k]*M[j][k] for k in range(6)) for j in range(6)] for i in range(6)]
    if gram!=[[2 if i==j else 0 for j in range(6)] for i in range(6)]: raise ValueError('nonunitary cut')
    matrices[str(row_axes)]={'row_axes':row_axes,'column_axes':col_axes,'rows':rows,'columns':cols,'matrix':M,'numerator_gram':gram}
result={'upstream_receipt_sha256':hashlib.sha256(data).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'S':S,'colors':[{'triple':s,'color':colors[s]} for s in S],
        'pair_projections':projections,'three_flattenings':matrices,
        'meaning':'Each listed numerator matrix divided by sqrt(2) is exactly unitary. This is a residual fragment, not a completed AME(4,6) state.',
        'clock_before_write':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()}
out=base/'enumeration-bipartite-v1.json'
with out.open('x',encoding='utf-8') as f: json.dump(result,f,indent=2,sort_keys=True); f.write(chr(10))
print('receipt',out,'sha256',hashlib.sha256(out.read_bytes()).hexdigest(),'code_sha256',result['code_sha256'])
