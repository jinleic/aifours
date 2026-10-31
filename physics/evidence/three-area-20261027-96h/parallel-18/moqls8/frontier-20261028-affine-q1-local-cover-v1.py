#!/usr/bin/env python3
"""Exact 1152-case affine QLS local-obstruction certificate.

For every anchored real-flat first nonfirst row, either one later cell has
zero COMPLEX feasible space, or the second row has an empty real-flat cell
or a uniquely forced nonorthogonal pair. No full quantum arrays are sampled.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time
from fractions import Fraction


def mul(a,b):
 z=0
 for _ in range(3):
  if b&1:z^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return z


def raw(a):return a|((a.bit_count()&1)<<6)


def gram(a,b):return 8-2*(raw(a)^raw(b)).bit_count()


def ref(j):return (sum(1<<(x-1) for x in range(1,8) if (j&x).bit_count()&1))&63


REF=tuple(ref(j) for j in range(8));LIGHT=set(REF)


def first_domain(i,j):
 forbid={j^mul(s,i) for s in (0,1,2,3)}
 return tuple(r for r in range(64) if all(gram(r,REF[k])==0 for k in forbid))


def row1_options():
 groups={}
 for j in range(8):groups.setdefault(first_domain(1,j),[]).append(j)
 if len(groups)!=2 or any(len(v)!=4 for v in groups.values()):raise ValueError('invalid row cosets')
 choices=[]
 for domain,columns in sorted(groups.items()):
  group=[]
  for heavy in (False,True):
   rays=[v for v in domain if (v not in LIGHT)==heavy]
   if len(rays)!=4 or any(gram(a,b) for a,b in itertools.combinations(rays,2)):
    raise ValueError('invalid four-dimensional sign basis')
   group.extend((columns,p) for p in itertools.permutations(rays))
  choices.append(group)
 for a,b in itertools.product(*choices):
  row=[-1]*8
  for columns,perm in (a,b):
   for j,v in zip(columns,perm):row[j]=v
  if row[0] not in LIGHT:yield tuple(row)


def determinant(A):
 B=[[Fraction(v) for v in row] for row in A];out=Fraction(1)
 for j in range(4):
  pivot=next((k for k in range(j,4) if B[k][j]),None)
  if pivot is None:return Fraction(0)
  if pivot!=j:B[j],B[pivot]=B[pivot],B[j];out=-out
  z=B[j][j];out*=z
  for k in range(j+1,4):
   m=B[k][j]/z
   for t in range(j,4):B[k][t]-=m*B[j][t]
 return out


def rank_matrix(row,k):
 forbid=sorted(mul(s,k) for s in (0,1,2,3))
 allowed=[j for j in range(8) if j not in forbid]
 cols=[mul(s,k^1) for s in (0,1,2,3)]
 mat=[[gram(row[j],REF[z]) for z in allowed] for j in cols]
 return {'cell':[k,0],'row1_columns':cols,'remaining_first_row_labels':allowed,
         'matrix_numerators':mat,'determinant':str(determinant(mat))}


def second_domains(row):
 ans=[]
 for j in range(8):
  old=[row[j^mul(s,3)] for s in (0,1,2,3)]
  ans.append([v for v in first_domain(2,j) if all(gram(v,w)==0 for w in old)])
 return ans


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();rows=list(row1_options())
 if len(rows)!=1152 or len(set(rows))!=1152:raise ValueError('row1 coverage')
 records=[];counts=collections.Counter()
 for row in rows:
  ranks=[rank_matrix(row,k) for k in range(2,8)]
  hit=next((r for r in ranks if r['determinant']!='0'),None)
  if hit:
   rec={'row1':list(row),'kind':'COMPLEX_RANK','witness':hit}
  else:
   D=second_domains(row)
   empty=next((j for j,d in enumerate(D) if not d),None)
   if empty is not None:
    rec={'row1':list(row),'kind':'EMPTY_FLAT_CELL','witness':{'cell':[2,empty]}}
   else:
    if any(len(d)!=1 for d in D):raise ValueError('unexpected non-singleton unblocked row2')
    forced=[d[0] for d in D]
    conflict=next(((j,k) for j in range(8) for k in range(j+1,8) if gram(forced[j],forced[k])!=0),None)
    if conflict is None:raise ValueError('unblocked valid second row')
    rec={'row1':list(row),'kind':'FORCED_NONORTHOGONAL_ROW2',
         'witness':{'forced_row2':forced,'columns':list(conflict),'gram_numerator':gram(forced[conflict[0]],forced[conflict[1]])}}
  counts[rec['kind']]+=1;records.append(rec)
 if dict(counts)!={'COMPLEX_RANK':828,'EMPTY_FLAT_CELL':112,'FORCED_NONORTHOGONAL_ROW2':212}:
  raise ValueError('unexpected cover counts')
 report={'result':'COMPLETE_1152_CASE_LOCAL_OBSTRUCTION_COVER',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'field':'GF(2)[x]/(x^3+x+1)','slopes':[1,2,3],
         'first_row_rays6':list(REF),'heavy_anchor':[1,0],
         'row1_cases':len(rows),'case_counts':dict(counts),'records':records,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'One affine 5-net and normalized heavy anchor; exact finite cover needs independent verification and written symmetry caller.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))

if __name__=='__main__':main()
