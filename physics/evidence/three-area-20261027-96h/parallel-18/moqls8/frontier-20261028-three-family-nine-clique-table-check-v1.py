#!/usr/bin/env python3
"""Independent fixed-label audit of the nine-cell fourth-mate obstruction."""
import argparse,copy,hashlib,json,pathlib,time
H=pathlib.Path(__file__).parent;FILE='frontier-20261028-three-family-mixed8-witness-v1.json';PIN='a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413'
P=[0,1,2,9,17,18,19,26,37];TABLE=['RRQBQQQQ','RCCQQQQ','AQCBCB','CQQQQ','RRAA','RCQ','QB','A','']
def verify(w,table):
 if len(P)!=9 or len(set(P))!=9 or len(table)!=9 or any(len(table[i])!=8-i for i in range(9)):raise ValueError('table shape')
 Q=w['quantum_square_numerators'];A,B=w['classical_mates'];checked=0
 for i,x in enumerate(P):
  r,c=divmod(x,8)
  for j in range(i+1,9):
   y=P[j];s,t=divmod(y,8);label=table[i][j-i-1]
   ok=(label=='R' and r==s) or (label=='C' and c==t) or (label=='A' and A[r][c]==A[s][t]) or (label=='B' and B[r][c]==B[s][t]) or (label=='Q' and sum(a*b for a,b in zip(Q[x],Q[y]))!=0)
   if not ok:raise ValueError(f'invalid labeled edge {x},{y}:{label}')
   checked+=1
 if checked!=36:raise ValueError('edge count')
 return checked

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic();raw=(H/FILE).read_bytes()
 if hashlib.sha256(raw).hexdigest()!=PIN:raise ValueError('witness hash')
 w=json.loads(raw);n=verify(w,TABLE);bad=TABLE[:];bad[0]='B'+bad[0][1:]
 try:verify(w,bad)
 except ValueError as e:
  if str(e)!='invalid labeled edge 0,1:B':raise ValueError('wrong mutation reason '+str(e))
 else:raise ValueError('bad label accepted')
 out={'result':'PASS_EXPLICIT_36_LABELED_EDGES',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'witness_sha256':PIN,'cells':P,'upper_triangle_reason_rows':TABLE,'edges_verified':n,
      'changed_label_mutation':'invalid labeled edge 0,1:B','elapsed_seconds':time.monotonic()-start,
      'limits':'Finite edge table only; physical meaning and no-fourth-mate dimension argument require written review.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
