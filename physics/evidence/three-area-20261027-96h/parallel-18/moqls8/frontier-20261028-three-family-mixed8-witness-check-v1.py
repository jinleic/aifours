#!/usr/bin/env python3
"""Independent complete Gram replay over Q(sqrt(2)) of the three-family witness."""
import argparse,copy,hashlib,json,pathlib,time
from fractions import Fraction as F
W='frontier-20261028-three-family-mixed8-witness-v1.json';PIN='a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413'
H=pathlib.Path(__file__).parent;Z=(F(0),F(0));ONE=(F(1),F(0))
def mul(a,b):return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def quantum_inner(a,da,b,db):
 v=sum(x*y for x,y in zip(a,b));d=da*db
 if d==1:return (F(v),F(0))
 if d==2:return (F(0),F(v,2))
 if d==4:return (F(v,2),F(0))
 raise ValueError('denominator')
def check(W):
 Q=W['quantum_square_numerators'];D=W['quantum_square_denominator_squared'];M=W['classical_mates']
 if len(Q)!=64 or len(D)!=64 or len(M)!=2 or any(len(x)!=8 for x in Q):raise ValueError('shape')
 if any(d not in (1,2) or any(not isinstance(v,int) or v not in (-1,0,1) for v in row) or sum(v*v for v in row)!=d for row,d in zip(Q,D)):raise ValueError('quantum norms')
 if any(len(L)!=8 or any(len(row)!=8 or any(x not in range(8) for x in row) for row in L) for L in M):raise ValueError('mate labels')
 G=[[[Z for _ in range(64)] for _ in range(64)] for _ in range(3)]
 for x in range(64):
  for y in range(64):
   G[0][x][y]=quantum_inner(Q[x],D[x],Q[y],D[y])
   for k in range(2):G[k+1][x][y]=(F(M[k][x//8][x%8]==M[k][y//8][y%8]),F(0))
 row=col=pair=0
 for q in range(3):
  for i in range(8):
   for j in range(8):
    for k in range(8):
     want=ONE if j==k else Z
     row+=G[q][8*i+j][8*i+k]!=want;col+=G[q][8*j+i][8*k+i]!=want
 for q in range(3):
  for r in range(q+1,3):
   for x in range(64):
    for y in range(64):pair+=mul(G[q][x][y],G[r][x][y])!=(ONE if x==y else Z)
 return int(row),int(col),int(pair)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 b=(H/W).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('witness hash')
 w=json.loads(b);r,c,p=check(w)
 if r or c or p:raise ValueError('physical Gram failure')
 if any(w['quantum_square_denominator_squared'][j]!=1 or w['quantum_square_numerators'][j]!=[int(k==j) for k in range(8)] for j in range(8)):raise ValueError('first row')
 mixed=[x for x,row in enumerate(w['quantum_square_numerators']) if sum(v!=0 for v in row)>1]
 if len(mixed)!=8 or mixed!=w['trade_cells']:raise ValueError('mixed count')
 controls={}
 bad=copy.deepcopy(w);bad['quantum_square_numerators'][19]=bad['quantum_square_numerators'][18][:];bad['quantum_square_denominator_squared'][19]=bad['quantum_square_denominator_squared'][18]
 if check(bad)[0]==0:raise ValueError('quantum duplicate mutation not detected')
 controls['quantum_duplicate_same_row']='rejected'
 bad=copy.deepcopy(w);bad['classical_mates'][0][0][1]=bad['classical_mates'][0][0][0]
 if check(bad)[0]==0:raise ValueError('mate duplicate mutation not detected')
 controls['mate_duplicate_same_row']='rejected'
 out={'result':'PASS_INDEPENDENT_FULL_THREE_FAMILY_GRAM_IN_Q_SQRT2',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'witness_sha256':PIN,
      'row_gram_entries_checked':1536,'column_gram_entries_checked':1536,'pair_product_gram_entries_checked':12288,
      'row_errors':r,'column_errors':c,'pair_product_errors':p,'mixed_cells':mixed,'mutation_controls':controls,
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Actual THREE-member family and nonclassicality only; no fourth mate, independent-model review or novelty claim.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
