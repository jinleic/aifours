#!/usr/bin/env python3
"""Independent exact checker of the affine 5-net row-rank obstruction.

Independently generates all row bases by per-cell DFS, not the producer's
4D-block permutation method. Recounts all row pairs and checks every claimed
projection determinant by the Leibniz formula. No imported producer code.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time

EXPECTED='0f498ce65d5b711acbac89390b3312066a5bc0751604b7dde497d4b6fdf38749'


def mult(a,b):
 z=0
 for _ in range(3):
  if b&1:z^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return z


def actual_signs(v):
 mask=v|((v.bit_count()&1)<<6)
 return (1,)+tuple(-1 if mask&(1<<(x-1)) else 1 for x in range(1,8))


def direct_dot(v,w):return sum(x*y for x,y in zip(actual_signs(v),actual_signs(w)))


def basis_ray(j):
 mask=sum(1<<(x-1) for x in range(1,8) if (j&x).bit_count()&1)
 lo=mask&63
 if actual_signs(lo)!=(1,)+tuple(-1 if mask&(1<<(x-1)) else 1 for x in range(1,8)):
  raise ValueError('basis parity encoding')
 return lo


REF=[basis_ray(j) for j in range(8)]
DOT=[[direct_dot(i,j) for j in range(64)] for i in range(64)]


def labels(i,j):return (i,j,*(j^mult(a,i) for a in (1,2,3)))


def shares(x,y):
 ax,ay=labels(*x),labels(*y)
 return any(p==q for p,q in zip(ax,ay))


def all_rows(i,anchor_heavy):
 domains=[]
 for j in range(8):
  first=[k for k in range(8) if shares((i,j),(0,k))]
  if len(first)!=4:raise ValueError('unexpected first-row line count')
  domain=[v for v in range(64) if all(DOT[v][REF[k]]==0 for k in first)]
  if len(domain)!=8:raise ValueError('unexpected cell domain')
  if anchor_heavy and j==0:domain=[v for v in domain if v not in REF]
  domains.append(domain)
 output=[]
 def extend(partial):
  j=len(partial)
  if j==8:
   output.append(tuple(partial));return
  for v in domains[j]:
   if all(DOT[v][w]==0 for w in partial):extend(partial+[v])
 extend([])
 return output


def det4(A):
 total=0
 for perm in itertools.permutations(range(4)):
  inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
  term=1
  for i in range(4):term*=A[i][perm[i]]
  total+=-term if inversions&1 else term
 return total


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();data=pathlib.Path(args.certificate).read_bytes()
 if hashlib.sha256(data).hexdigest()!=EXPECTED:raise ValueError('producer certificate SHA mismatch')
 cert=json.loads(data)
 rows1=all_rows(1,True);rows2=all_rows(2,False)
 if (len(rows1),len(rows2))!=(1152,2304):raise ValueError('independent per-cell DFS row count')
 # Compute 32 physical constraints between each row pair from line labels,
 # independent of the producer's closed-form slope index.
 tests=[(j,l) for j in range(8) for l in range(8) if shares((1,j),(2,l))]
 if len(tests)!=32:raise ValueError('row-pair net constraint count')
 counts=collections.Counter();pairs=0
 for a in rows1:
  for b in rows2:
   if all(DOT[a[j]][b[l]]==0 for j,l in tests):counts[a]+=1;pairs+=1
 records=cert['exact_projected_rank_certificates']
 if len(records)!=len(counts) or set(tuple(v['row1_rays6']) for v in records)!=set(counts):
  raise ValueError('producer omitted or added a surviving row1 pattern')
 if pairs!=cert['compatible_row_pairs'] or pairs!=512:raise ValueError('pair count mismatch')
 row_hist=collections.Counter()
 for entry in records:
  a=tuple(entry['row1_rays6']);k=entry['forced_row'];j=entry['forced_column']
  if k not in range(3,8) or j!=0 or counts[a]!=entry['compatible_row2_options']:
   raise ValueError('bad witness metadata')
  first=[v for v in range(8) if shares((k,j),(0,v))]
  old=[v for v in range(8) if shares((k,j),(1,v))]
  if set(first)!=set(entry['first_row_forbidden_basis_labels']) or set(old)!=set(entry['row1_constraining_columns']):
   raise ValueError('witness line-incidence mismatch')
  free=[v for v in range(8) if v not in first]
  if free!=entry['remaining_basis_labels'] or len(free)!=4 or len(old)!=4:
   raise ValueError('first-row complement mismatch')
  order=entry['row1_constraining_columns']
  matrix=[[DOT[a[v]][REF[z]] for z in free] for v in order]
  if matrix!=entry['projection_gram_numerators']:
   raise ValueError('actual vector projection matrix mismatch')
  value=det4(matrix)
  if value==0 or str(value)!=entry['determinant']:
   raise ValueError('projection determinant mismatch')
  row_hist[str(k)]+=1
 # Intended-reason mutation controls: a missing certificate and a repeated row.
 missing=list(records[:-1])
 if set(tuple(v['row1_rays6']) for v in missing)==set(counts):
  raise ValueError('missing-row negative control was not rejected')
 mutant=[row[:] for row in records[0]['projection_gram_numerators']];mutant[1]=mutant[0][:]
 if det4(mutant)!=0:raise ValueError('singular-matrix negative control was not rejected')
 # The classical positive family uses Q(i,j)=j+4i; its first 3 rows satisfy all net constraints.
 classical=[tuple(REF[j^mult(4,i)] for j in range(8)) for i in range(3)]
 if any(DOT[classical[1][j]][classical[2][l]] for j,l in tests):
  raise ValueError('classical row-pair positive control failed')
 result={'result':'PASS_INDEPENDENT_AFFINE_ROW_AND_COMPLEX_RANK_CERTIFICATES',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'input_certificate_sha256':EXPECTED,'row1_DFS_count':len(rows1),'row2_DFS_count':len(rows2),
         'row_pair_checks':len(rows1)*len(rows2),'compatible_pairs':pairs,
         'verified_surviving_row1_patterns':len(records),'witness_row_histogram':dict(row_hist),
         'all_actual_projection_determinants_nonzero':True,'classical_positive_control':True,
         'missing_coverage_control_rejected':True,'duplicate_matrix_row_control_rejected':True,
         'elapsed_seconds':time.monotonic()-start,
         'limits':'Exact finite check for one normalized affine net/anchor; symmetry and actual-original caller require separate written review.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(result,h,indent=2);h.write('\n')
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
