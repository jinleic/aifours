#!/usr/bin/env python3
"""Reconstruct and verify all 1560 anchor-line support/phase certificates."""
import argparse,collections,copy,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
   ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
CERT='8197df87c67c2bfada19ce4a13d8d724b4ccfbfe60322456c9c234773cbd9191'
def pinned(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('hash mismatch')
 return b

def load():
 out=[]
 for name,pin,n in P:
  lines=[s.strip() for s in pinned(name,pin).decode('ascii').splitlines() if s.strip()]
  if lines[0].split()[:3]!=['8','8',str(n)] or len(lines)!=1+8*n:raise ValueError('source layout')
  S=[[[ord(ch)-97 for ch in lines[1+8*k+i]] for i in range(8)] for k in range(n)]
  for B in S:
   if any(sorted(row)!=list(range(8)) for row in B) or any(sorted(B[i][j] for i in range(8))!=list(range(8)) for j in range(8)):raise ValueError('not Latin')
  for k in range(0,n,3):
   T=S[k:k+3]
   for a,b in itertools.combinations(range(3),2):
    if len({(T[a][i][j],T[b][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('not orthogonal')
   out.append([(i,j,T[0][i][j],T[1][i][j],T[2][i][j]) for i in range(8) for j in range(8)])
 return out

def context(net,rec):
 r,c,s=rec['row_class'],rec['column_class'],rec['anchor_symbol']
 if r not in range(5) or c!=next(v for v in range(5) if v!=r) or s not in range(8):raise ValueError('orientation')
 rowvals=[s]+[v for v in range(8) if v!=s];other=[v for v in range(5) if v not in (r,c)]
 def point(x):
  i,j=divmod(x,8);cand=[p for p in net if p[r]==rowvals[i] and p[c]==j]
  if len(cand)!=1:raise ValueError('not OA2')
  return cand[0]
 def normalized(x):
  p=point(x);z=[x//8,x%8]
  for q in other:
   idx=[j for j in range(8) if point(j)[q]==p[q]]
   if len(idx)!=1:raise ValueError('bad first row')
   z.append(idx[0])
  if len(set(z[1:]))!=4:raise ValueError('forbidden labels repeat')
  return z
 return normalized

def validate_record(net,rec):
 norm=context(net,rec);cells=rec['cells']
 if any(x not in range(8,64) for x in cells) or len(set(cells))!=len(cells):raise ValueError('bad cell list')
 facts=[norm(x) for x in cells];allowed=[set(range(8))-set(z[1:]) for z in facts]
 if [sorted(z) for z in allowed]!=rec['allowed']:raise ValueError('allowed sets differ')
 if rec['kind']=='one_overlap':
  if len(cells)!=2:raise ValueError('pair size')
  k,v=rec['line']
  if k not in range(5) or facts[0][k]!=v or facts[1][k]!=v:raise ValueError('pair line')
  common=sorted(allowed[0]&allowed[1])
  if len(common)!=1 or common!=rec['intersection']:raise ValueError('pair overlap')
 elif rec['kind']=='odd_phase_cycle':
  axes=rec['axes']
  if len(axes)!=2 or sorted(set(axes))!=axes or any(z not in range(8) for z in axes):raise ValueError('axes')
  n=len(cells)
  if n<3 or n%2!=1 or len(rec['edge_lines'])!=n:raise ValueError('not odd cycle')
  for i,(k,v) in enumerate(rec['edge_lines']):
   j=(i+1)%n
   if k not in range(5) or facts[i][k]!=v or facts[j][k]!=v:raise ValueError('cycle line')
   if sorted(allowed[i]&allowed[j])!=axes:raise ValueError('cycle overlap')
 else:raise ValueError('unknown witness')

def validate_all(nets,C):
 R=C['records'];expected=[(s,r,a) for s in range(39) for r in range(5) for a in range(8)]
 if len(nets)!=39 or [(z['species_index'],z['row_class'],z['anchor_symbol']) for z in R]!=expected:raise ValueError('coverage')
 cnt=collections.Counter()
 for rec in R:validate_record(nets[rec['species_index']],rec);cnt[rec['kind']]+=1
 if cnt!={'one_overlap':1528,'odd_phase_cycle':32}:raise ValueError('kind counts')
 return cnt

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 C=json.loads(pinned('frontier-20261028-anchor-sparse-net-obstructions-v1.json',CERT));nets=load();cnt=validate_all(nets,C)
 ic=next(i for i,r in enumerate(C['records']) if r['kind']=='odd_phase_cycle')
 def duplicate_cycle(z):z['records'][ic]['cells'][1]=z['records'][ic]['cells'][0]
 def remove_cycle_edge(z):z['records'][ic]['edge_lines'].pop()
 cases=[('missing_anchor',lambda z:z['records'].pop()),('wrong_pair_line',lambda z:z['records'][0].update({'line':[0,9]})),
        ('duplicate_cycle_cell',duplicate_cycle),('missing_cycle_edge',remove_cycle_edge),
        ('changed_cycle_axis',lambda z:z['records'][ic]['axes'].__setitem__(1,7)),
        ('changed_allowed_set',lambda z:z['records'][0]['allowed'][0].__setitem__(0,9))]
 controls={}
 for name,mut in cases:
  bad=copy.deepcopy(C);mut(bad)
  try:validate_all(nets,bad)
  except (ValueError,KeyError,IndexError):controls[name]='rejected'
  else:raise ValueError('tamper passed '+name)
 report={'result':'PASS_ALL_1560_INDEPENDENT_ANCHOR_OBSTRUCTIONS',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'certificate_sha256':CERT,'contexts':1560,'kind_counts':dict(cnt),
         'odd_cycle_lengths':dict(collections.Counter(len(r['cells']) for r in C['records'] if r['kind']=='odd_phase_cycle')),
         'mutation_controls':controls,
         'limits':'Exact finite certificates only; mathematical implication and Hcat are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
