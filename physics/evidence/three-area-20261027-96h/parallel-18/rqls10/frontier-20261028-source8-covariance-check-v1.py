#!/usr/bin/env python3
"""Exact primary Example2.4 verification and necessary cyclic-row covariance.

Coefficients are Q(zeta8) with numerator basis 1,z,z²,z³ and common denom2.
Test absolute Gram-block invariance; a detected cycle is only necessary.
"""
from bs4 import BeautifulSoup
from pathlib import Path
from itertools import combinations
import datetime,hashlib,json,re
P=Path(__file__).resolve().parent;src=P/'frontier-20261028-zhang-cao-example24-source-v1.html'
soup=BeautifulSoup(src.read_text(),'html.parser');table=soup.find('table',id='S2.Thmtheorem4.p2.1')
rows=table.find('tbody').find_all('tr',recursive=False);assert len(rows)==8
pat=re.compile(r'(\\sqrt\{2\})?(\\omega(?:\^\{(\d+)\})?)?\|([0-7])\\rangle')
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def root(k):
 k%=8;out=[0]*4;out[k%4]=1 if k<4 else -1;return tuple(out)
def mul(a,b):
 out=[0]*4
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[(i+j)%4]+=(1 if i+j<4 else -1)*x*y
 return tuple(out)
def conj(a):
 out=(0,0,0,0)
 for i,x in enumerate(a):out=add(out,tuple(x*y for y in root(-i)))
 return out
SQ=(0,1,0,-1);V=[];allalt=[]
for row in rows:
 cells=row.find_all('td',recursive=False);assert len(cells)==8
 R=[]
 for cell in cells:
  alt=cell.math.get('alttext');allalt.append(alt);terms=pat.findall(alt)
  assert len(terms)==alt.count('\\rangle') and terms
  scalar=SQ if '\\tfrac{1}{\\sqrt{2}}' in alt else (1,0,0,0) if '\\tfrac{1}{2}' in alt else (2,0,0,0)
  v=[(0,0,0,0) for _ in range(8)]
  for sq,omega,powr,idx in terms:
   assert v[int(idx)]==(0,0,0,0)
   phase=int(powr) if powr else (1 if omega else 0)
   v[int(idx)]=mul(mul(scalar,SQ if sq else (1,0,0,0)),root(phase))
  R.append(v)
 V.append(R)
Z=(0,0,0,0);ONE=(4,0,0,0);ABS16=(16,0,0,0)
def gram(a,b):
 out=Z
 for x,y in zip(a,b):out=add(out,mul(conj(x),y))
 return out
def abssq(a,b):
 v=gram(a,b);return mul(v,conj(v))
for r in range(8):
 for c in range(8):assert gram(V[r][c],V[r][c])==ONE
 for c,d in combinations(range(8),2):assert gram(V[r][c],V[r][d])==Z
for c in range(8):
 for r,s in combinations(range(8),2):assert gram(V[r][c],V[s][c])==Z
for k in range(8):
 for r,s in combinations(range(8),2):assert gram(V[r][r^k],V[s][s^k])==Z
for (r,c),(s,d) in combinations([(r,c) for r in range(8) for c in range(8)],2):assert abssq(V[r][c],V[s][d])!=ABS16

def covariance(transpose):
 arr=[[V[c][r] if transpose else V[r][c] for c in range(8)]for r in range(8)]
 labels={(r,s):tuple(abssq(arr[r][c],arr[s][d]) for c in range(8)for d in range(8)) for r in range(8)for s in range(8)if r!=s}
 unique=set(labels.values());cycles=[]
 for label in unique:
  edge={(r,s) for (r,s),value in labels.items() if value==label}
  def go(path):
   if len(path)==8:
    if (path[-1],path[0]) in edge:cycles.append(path[:])
    return
   for s in range(1,8):
    if s not in path and (path[-1],s) in edge:go(path+[s])
  go([0])
 return {'distinct_directed_gram_labels':len(unique),'invariant_eight_cycles':len(cycles),'sample':cycles[:1]}
obj={'source_url':'https://arxiv.org/html/2608.29201v2#S2.Thmtheorem4',
 'source_fragment_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'exact_checks':{'cells':64,'row_grams':224,'column_grams':224,'xor_transversal_grams':224,'distinct_ray_pairs':2016},
 'row_covariance_necessary_test':covariance(False),'column_covariance_necessary_test':covariance(True),
 'interpretation':'Any actual Fourier-product representation forces a directed 8-cycle with identical squared-Gram blocks; passing this test is not sufficient.'}
(P/'frontier-20261028-source8-covariance-check-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
