#!/usr/bin/env python3
"""Independent three-color test: delete each independent set containing vertex0,
then test remaining graph for bipartiteness. A graph is 3-colorable iff some
such deletion works. Input parity sets independently enumerated in replay v1.
"""
import datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;A=P/'frontier-20261029-pauli40-parity-core-census-v2.json';B=P/'frontier-20261029-pauli40-parity-core-replay-v1.json';a=A.read_bytes();b=B.read_bytes();D=json.loads(a);R=json.loads(b)
assert [x['basis_indices']for x in D['records']]==[x['basis_indices']for x in R['records']];bases=D['bases'];counts=[]
for item in D['records']:
 Q=[set(bases[i])for i in item['basis_indices']];adj=[0]*15
 for i,j in itertools.combinations(range(15),2):
  if Q[i]&Q[j]:adj[i]|=1<<j;adj[j]|=1<<i
 examined=0;answer=None
 for rest in range(1<<14):
  S=(rest<<1)|1;valid=True;tmp=S
  while tmp:
   bit=tmp&-tmp;tmp-=bit;i=bit.bit_length()-1
   if adj[i]&S:valid=False;break
  if not valid:continue
  examined+=1;remaining=((1<<15)-1)^S;colors=[-1]*15;ok=True
  for start in range(15):
   if not(remaining>>start&1)or colors[start]>=0:continue
   colors[start]=0;stack=[start]
   while stack and ok:
    x=stack.pop();nb=adj[x]&remaining
    while nb:
     bit=nb&-nb;nb-=bit;y=bit.bit_length()-1
     if colors[y]<0:colors[y]=1-colors[x];stack.append(y)
     elif colors[y]==colors[x]:ok=False;break
   if not ok:break
  if ok:answer=S;break
 assert answer is None
 counts.append(examined)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(a).hexdigest(),
 'independent_parity_replay_sha256':hashlib.sha256(b).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'cases':len(counts),'all_not_3colorable':True,'independent_subsets_tested':sum(counts),'per_case_counts':counts,'status':'PASS'}
(P/'frontier-20261029-pauli40-3color-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='per_case_counts'},indent=2))
