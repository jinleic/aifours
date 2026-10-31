#!/usr/bin/env python3
"""Exact QLS whose first-row coordinates are 1-or-4 uniform but ray overlaps are not four-ray."""
import argparse,collections,hashlib,json,pathlib
from fractions import Fraction as F
Z=(F(0),F(0));ONE=(F(1),F(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def inner(a,b):
 s=Z
 for x,y in zip(a,b):s=add(s,mul(conj(x),y))
 return s
def qls():
 H=[[(F((-1)**((r&k).bit_count()),2),F(0)) for r in range(4)] for k in range(4)]
 p=(F(3,5),F(0));q=(F(0),F(4,5))
 X=[add(mul(p,H[0][r]),mul(q,H[1][r])) for r in range(4)]
 Y=[add(mul(q,H[0][r]),mul(p,H[1][r])) for r in range(4)]
 out=[]
 for i in range(8):
  a,b=divmod(i,4)
  for j in range(8):
   c,d=divmod(j,4);block=a^c;letter=b^d;v=[Z]*8
   if a==c==1:
    values=(X if letter==0 else Y) if b<2 and d<2 else H[letter]
    for r in range(4):v[4*block+r]=values[r]
   else:v[4*block+letter]=ONE
   out.append(v)
 return out
def check(Q):
 row=col=0
 for i in range(8):
  for j in range(8):
   for k in range(8):
    target=ONE if j==k else Z
    row+=inner(Q[8*i+j],Q[8*i+k])!=target
    col+=inner(Q[8*j+i],Q[8*k+i])!=target
 h=collections.Counter();allowed={F(0),F(1,4),F(1)}
 for x in range(64):
  for y in range(64):
   g=inner(Q[x],Q[y]);h[str(g[0]*g[0]+g[1]*g[1])]+=1
 anchor=[]
 for x in range(64):
  weights=[]
  for y in range(8):
   g=inner(Q[y],Q[x]);weights.append(g[0]*g[0]+g[1]*g[1])
  if sum(weights)!=1 or any(w not in allowed for w in weights) or sum(w!=0 for w in weights) not in (1,4):raise ValueError('anchor not sparse-uniform')
  anchor.append(sum(w!=0 for w in weights))
 return int(row),int(col),h,anchor

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 Q=qls();r,c,h,anchor=check(Q)
 if r or c:raise ValueError('not QLS')
 g=inner(Q[36],Q[54]);sq=g[0]*g[0]+g[1]*g[1]
 if sq!=F(9,25):raise ValueError('missing non-four-ray overlap')
 bad=Q.copy();bad[1]=bad[0]
 if inner(bad[0],bad[1])==Z:raise ValueError('duplicate control')
 out={'result':'EXACT_ANCHOR_SPARSE_QLS_NOT_FOUR_RAY_NOT_A_FOUR_FAMILY',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'row_gram_errors':r,'column_gram_errors':c,'anchor_support_histogram':dict(collections.Counter(anchor)),
      'all_squared_overlap_histogram':dict(h),'selected_cell_indices':[36,54],
      'selected_squared_overlap':str(sq),'duplicate_row_control_rejected':True,
      'limits':'Standalone QLS only; no claim of any orthogonal mates.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
