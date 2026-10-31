#!/usr/bin/env python3
"""Independent exact verifier of all1152 affine-net local obstructions.

Per-cell DFS regenerates row1; dot products use actual 8-sign vectors; 4x4
determinants use the Leibniz formula. No producer module is imported.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time

PIN='8fb82c85418dc037f369bd466e2fade49f5ede56ee860616e145b178f0265d3b'


def mult(a,b):
 z=0
 for _ in range(3):
  if b&1:z^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return z


def signs(v):
 mask=v|((v.bit_count()&1)<<6)
 return (1,)+tuple(-1 if mask&(1<<(x-1)) else 1 for x in range(1,8))


def dot(v,w):return sum(a*b for a,b in zip(signs(v),signs(w)))


def ref(j):
 mask=sum(1<<(x-1) for x in range(1,8) if (j&x).bit_count()&1)
 low=mask&63
 if signs(low)!=(1,)+tuple(-1 if mask&(1<<(x-1)) else 1 for x in range(1,8)):
  raise ValueError('reference encoding')
 return low


REF=tuple(ref(j) for j in range(8));DOT=[[dot(a,b) for b in range(64)] for a in range(64)]


def labels(i,j):return (i,j,*(j^mult(a,i) for a in (1,2,3)))


def share(a,b):return any(x==y for x,y in zip(labels(*a),labels(*b)))


def first_domain(i,j):
 forced=[k for k in range(8) if share((i,j),(0,k))]
 if len(forced)!=4:raise ValueError('first-row line count')
 return [r for r in range(64) if all(DOT[r][REF[k]]==0 for k in forced)]


def generate_row1():
 domains=[first_domain(1,j) for j in range(8)]
 domains[0]=[r for r in domains[0] if r not in REF]
 out=[]
 def dfs(v):
  j=len(v)
  if j==8:out.append(tuple(v));return
  for r in domains[j]:
   if all(DOT[r][z]==0 for z in v):dfs(v+[r])
 dfs([])
 return out


def det4(A):
 ans=0
 for p in itertools.permutations(range(4)):
  inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
  term=1
  for i in range(4):term*=A[i][p[i]]
  ans+=-term if inv&1 else term
 return ans


def domains2(row):
 out=[]
 for j in range(8):
  old=[row[k] for k in range(8) if share((2,j),(1,k))]
  if len(old)!=4:raise ValueError('row1 line count')
  out.append([v for v in first_domain(2,j) if all(DOT[v][w]==0 for w in old)])
 return out


def verify_entry(entry):
 row=tuple(entry['row1']);kind=entry['kind'];w=entry['witness']
 if kind=='COMPLEX_RANK':
  k,j=w['cell']
  if k not in range(2,8) or j!=0:raise ValueError('rank witness cell')
  f=[x for x in range(8) if share((k,j),(0,x))]
  r=[x for x in range(8) if share((k,j),(1,x))]
  if len(f)!=4 or len(r)!=4 or set(r)!=set(w['row1_columns']):raise ValueError('rank witness lines')
  free=[z for z in range(8) if z not in f]
  if free!=w['remaining_first_row_labels']:raise ValueError('rank witness free labels')
  A=[[DOT[row[c]][REF[z]] for z in free] for c in w['row1_columns']]
  if A!=w['matrix_numerators']:raise ValueError('rank projection matrix')
  value=det4(A)
  if value==0 or str(value)!=w['determinant']:raise ValueError('singular or mismatched rank witness')
 elif kind=='EMPTY_FLAT_CELL':
  i,j=w['cell']
  if i!=2 or j not in range(8) or domains2(row)[j]:raise ValueError('claimed empty cell not empty')
 elif kind=='FORCED_NONORTHOGONAL_ROW2':
  D=domains2(row)
  if any(len(t)!=1 for t in D):raise ValueError('claimed row not uniquely forced')
  forced=[t[0] for t in D]
  if forced!=w['forced_row2']:raise ValueError('forced row values')
  a,b=w['columns']
  if not(0<=a<b<8) or DOT[forced[a]][forced[b]]==0 or DOT[forced[a]][forced[b]]!=w['gram_numerator']:
   raise ValueError('forced pair is orthogonal or misreported')
 else:raise ValueError('unrecognized certificate kind')


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--certificate',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
 start=time.monotonic();data=pathlib.Path(args.certificate).read_bytes()
 if hashlib.sha256(data).hexdigest()!=PIN:raise ValueError('certificate SHA mismatch')
 cert=json.loads(data);records=cert['records'];rows=generate_row1()
 if len(rows)!=1152 or len(set(rows))!=1152:raise ValueError('independent row DFS coverage')
 if len(records)!=len(rows) or set(tuple(e['row1']) for e in records)!=set(rows):raise ValueError('missing or extra row1 case')
 counts=collections.Counter()
 for entry in records:
  verify_entry(entry);counts[entry['kind']]+=1
 if dict(counts)!={'COMPLEX_RANK':828,'EMPTY_FLAT_CELL':112,'FORCED_NONORTHOGONAL_ROW2':212}:
  raise ValueError('case-category counts')
 # Negative controls are checked for their intended causes.
 if set(tuple(e['row1']) for e in records[:-1])==set(rows):raise ValueError('omitted-case mutation not rejected')
 rank=next(e for e in records if e['kind']=='COMPLEX_RANK');A=[x[:] for x in rank['witness']['matrix_numerators']];A[1]=A[0][:]
 if det4(A)!=0:raise ValueError('singular-rank mutation not rejected')
 forced=next(e for e in records if e['kind']=='FORCED_NONORTHOGONAL_ROW2');D=domains2(tuple(forced['row1']));vals=[d[0] for d in D]
 orthpair=next(((a,b) for a in range(8) for b in range(a+1,8) if DOT[vals[a]][vals[b]]==0),None)
 if orthpair is None:raise ValueError('forced-pair control not available')
 altered={'row1':forced['row1'],'kind':forced['kind'],'witness':dict(forced['witness'])}
 altered['witness']['columns']=list(orthpair);altered['witness']['gram_numerator']=0
 try:verify_entry(altered)
 except ValueError as exc:
  if str(exc)!='forced pair is orthogonal or misreported':raise
 else:raise ValueError('orthogonal-pair mutation not rejected')
 result={'result':'PASS_INDEPENDENT_ALL_1152_LOCAL_OBSTRUCTION_CASES',
         'checker_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'certificate_sha256':PIN,'independent_row1_DFS_cases':len(rows),'verified_case_counts':dict(counts),
         'all_complex_rank_determinants_nonzero':True,'all_flat_empty_cells_independently_checked':True,
         'all_forced_nonorthogonal_rows_independently_checked':True,
         'missing_coverage_control_rejected':True,'singular_rank_control_rejected':True,
         'orthogonal_forced_pair_control_rejected':True,'elapsed_seconds':time.monotonic()-start,
         'limits':'One normalized affine 5-net; mathematical symmetry and original-object callers still require review.'}
 with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(result,h,indent=2);h.write('\n')
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
