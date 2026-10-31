#!/usr/bin/env python3
"""Exact affine 5-net two-row exhaustive / complex rank-obstruction checker.

No other search module is imported. This bounded finite computation treats
first three Q rows as real-flat sign rays; the obstructed fourth-row cell may
be an arbitrary complex vector. It is NOT an unrestricted MOQLS theorem.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time
from fractions import Fraction

LIMIT=30.0


def mul(a,b):
 out=0
 for _ in range(3):
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out


def raw(a):return a|((a.bit_count()&1)<<6)


def g(a,b):return 8-2*(raw(a)^raw(b)).bit_count()


def ref(j):
 rawvalue=sum(1<<(x-1) for x in range(1,8) if (j&x).bit_count()&1)
 lo=rawvalue&63
 if raw(lo)!=rawvalue:raise ValueError('even sign encoding')
 return lo


REF=tuple(ref(j) for j in range(8))
LIGHT=set(REF)


def row_options(i,force_heavy):
 groups={}
 for j in range(8):
  forbidden={j^mul(s,i) for s in (0,1,2,3)}
  allowed=tuple(r for r in range(64) if all(g(r,REF[k])==0 for k in forbidden))
  groups.setdefault(allowed,[]).append(j)
 if len(groups)!=2 or any(len(c)!=4 for c in groups.values()):raise ValueError('column coset structure')
 pieces=[]
 for domain,cols in sorted(groups.items()):
  options=[]
  for heavy in (False,True):
   rays=[v for v in domain if (v not in LIGHT)==heavy]
   if len(rays)!=4 or any(g(a,b) for a,b in itertools.combinations(rays,2)):
    raise ValueError('four-ray basis error')
   for perm in itertools.permutations(rays):options.append((cols,perm))
  pieces.append(options)
 for p0,p1 in itertools.product(*pieces):
  row=[-1]*8
  for cols,vals in (p0,p1):
   for j,v in zip(cols,vals):row[j]=v
  if not force_heavy or row[0] not in LIGHT:yield tuple(row)


def compatible(i,a,k,b):
 delta=i^k
 for j in range(8):
  for s in (0,1,2,3):
   if g(a[j],b[j^mul(s,delta)])!=0:return False
 return True


def determinant(matrix):
 A=[[Fraction(x) for x in row] for row in matrix];n=len(A);result=Fraction(1)
 for j in range(n):
  pivot=next((i for i in range(j,n) if A[i][j]),None)
  if pivot is None:return Fraction(0)
  if pivot!=j:A[j],A[pivot]=A[pivot],A[j];result=-result
  z=A[j][j];result*=z
  for i in range(j+1,n):
   c=A[i][j]/z
   for k in range(j,n):A[i][k]-=c*A[j][k]
 return result


def cell_certificate(row1,k):
 forbidden=sorted(mul(s,k) for s in (0,1,2,3))
 allowed=[j for j in range(8) if j not in forbidden]
 previous_columns=[mul(s,k^1) for s in (0,1,2,3)]
 previous_rays=[row1[j] for j in previous_columns]
 matrix=[[g(v,REF[z]) for z in allowed] for v in previous_rays]
 return {'forced_row':k,'forced_column':0,'first_row_forbidden_basis_labels':forbidden,
         'remaining_basis_labels':allowed,'row1_constraining_columns':previous_columns,
         'row1_constraining_rays':previous_rays,'projection_gram_numerators':matrix,
         'determinant':str(determinant(matrix))}


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();rows1=list(row_options(1,True));rows2=list(row_options(2,False))
 if (len(rows1),len(rows2))!=(1152,2304):raise ValueError('row enumeration cardinality')
 classical=lambda i:tuple(ref(j^mul(4,i)) for j in range(8))
 if not compatible(1,classical(1),2,classical(2)) or classical(1)[0] not in LIGHT:
  raise ValueError('classical positive control')
 counts=collections.Counter();pairs=0;tested=0;complete=True
 for a in rows1:
  if time.monotonic()-start>LIMIT:complete=False;break
  for b in rows2:
   tested+=1
   if compatible(1,a,2,b):counts[a]+=1;pairs+=1
 cert=[];uncovered=[]
 if complete:
  for row1,num in sorted(counts.items()):
   candidates=[cell_certificate(row1,k) for k in (3,4,5,6,7)]
   c=next((v for v in candidates if v['determinant']!='0'),None)
   if c is None:uncovered.append(list(row1))
   else:cert.append({'row1_rays6':list(row1),'compatible_row2_options':num,**c})
 if cert:
  mutant=[row[:] for row in cert[0]['projection_gram_numerators']]
  mutant[1]=mutant[0][:]
  if determinant(mutant)!=0:raise ValueError('singular determinant control failed')
 report={'result':('COMPLETE_32_ROW1_CLASSES_EACH_BLOCKED_BY_COMPLEX_RANK' if complete and not uncovered else
                   ('COMPLETE_WITH_UNCOVERED_CASES' if complete else 'UNKNOWN_TIME_BOUND')),
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'field':'GF(2)[x]/(x^3+x+1)','classical_mate_slopes':[1,2,3],
         'first_row_rays6':list(REF),'heavy_anchor':[1,0],
         'row1_options':len(rows1),'row2_options':len(rows2),'pair_tests':tested,
         'compatible_row_pairs':pairs,'surviving_row1_patterns':len(counts),
         'certified_patterns':len(cert),'uncovered_row1_patterns':uncovered,
         'witness_row_histogram':dict(collections.Counter(str(v['forced_row']) for v in cert)),
         'exact_projected_rank_certificates':cert,'complete':complete,
         'classical_positive_control':True,'repeated_matrix_row_determinant_negative_control':bool(cert),
         'elapsed_seconds':time.monotonic()-start,
         'limits':'One affine 5-net and one heavy anchor; conditional on independently checked row coverage and symmetry. Row after row2 is arbitrary complex.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k!='exact_projected_rank_certificates'},indent=2))

if __name__=='__main__':main()
