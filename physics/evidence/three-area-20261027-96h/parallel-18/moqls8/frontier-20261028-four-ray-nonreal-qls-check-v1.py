#!/usr/bin/env python3
"""Exact standalone QLS illustrating that four-ray overlap is broader than real-flat."""
import argparse,collections,hashlib,json,pathlib
from fractions import Fraction as F
Z=(F(0),F(0));ONE=(F(1),F(0));I=(F(0),F(1));MINUS=(F(-1),F(0));MINUSI=(F(0),F(-1));ROOTS=(ONE,I,MINUS,MINUSI)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def inner(a,b):
 s=Z
 for u,v in zip(a,b):s=add(s,mul(conj(u),v))
 return s
def qls():
 out=[]
 for row in range(8):
  a,b=divmod(row,4)
  for col in range(8):
   c,d=divmod(col,4);block=a^c;letter=b^d;v=[Z]*8
   if a==c==1:
    for k in range(4):v[4*block+k]=tuple(q/2 for q in ROOTS[(k*letter)%4])
   else:v[4*block+letter]=ONE
   out.append(v)
 return out
def verify(Q):
 row=col=0
 for i in range(8):
  for j in range(8):
   for k in range(8):
    target=ONE if j==k else Z
    row+=inner(Q[8*i+j],Q[8*i+k])!=target
    col+=inner(Q[8*j+i],Q[8*k+i])!=target
 histogram=collections.Counter()
 for x in range(64):
  for y in range(64):
   v=inner(Q[x],Q[y]);histogram[str(v[0]*v[0]+v[1]*v[1])]+=1
 return int(row),int(col),histogram
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 Q=qls();r,c,h=verify(Q)
 if r or c or set(h)!={'0','1/4','1'}:raise ValueError('QLS/overlap verification failed')
 p=ONE
 for x,y in [(0,36),(36,1),(1,37),(37,0)]:p=mul(p,inner(Q[x],Q[y]))
 if p!=(F(0),F(1,16)):raise ValueError('nonreal invariant')
 bad=Q.copy();bad[1]=bad[0]
 if verify(bad)[0]==0:raise ValueError('duplicate control')
 out={'result':'EXACT_NONREAL_FOUR_RAY_QLS_NOT_A_FOUR_FAMILY',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'row_gram_errors':r,'column_gram_errors':c,'pairwise_squared_overlap_histogram':dict(h),
      'four_ray_cycle_cells':[0,36,1,37],'four_ray_cycle_invariant':['0','1/16'],
      'duplicate_row_control_rejected':True,
      'limits':'Standalone QLS only; no claim of any classical or quantum mates.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
