#!/usr/bin/env python3
"""Independent dynamic-programming audit of common transversal counts."""
import argparse,collections,hashlib,json,pathlib,time
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max2-first-pair-v1.txt','710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd'),
   ('frontier-20261028-source-wanless-nonmax2-first-pair-v1.txt','2c32f66b0c4be0d995ff8db895e0b942034889ccd8523212f451bbab818a53a4')]
CERT='651620bd2cfe0845648bcff0eb1bed952b433e179c1632461101acece6ca49b5'
def load(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('source hash')
 z=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if len(z)!=17 or z[0].split()[:2]!=['8','8']:raise ValueError('source layout')
 A=[[[ord(c)-97 for c in z[1+8*k+i]] for i in range(8)] for k in range(2)]
 if any(any(sorted(row)!=list(range(8)) for row in S) or any(sorted(S[i][j] for i in range(8))!=list(range(8)) for j in range(8)) for S in A):raise ValueError('not Latin')
 if len({(A[0][i][j],A[1][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('not orthogonal')
 return A

def count(T,which):
 # State is the used column mask plus one or two used-symbol masks.
 states={(0,)+(0,)*len(which):1};layers=[1]
 for row in range(8):
  nxt=collections.Counter()
  for masks,count0 in states.items():
   for col in range(8):
    bits=(1<<col,)+tuple(1<<T[k][row][col] for k in which)
    if any(a&b for a,b in zip(masks,bits)):continue
    nxt[tuple(a|b for a,b in zip(masks,bits))]+=count0
  states=nxt;layers.append(sum(states.values()))
 return sum(states.values()),layers

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 b=(H/'frontier-20261028-two-nets-transversal-census-receipt-v1.json').read_bytes()
 if hashlib.sha256(b).hexdigest()!=CERT:raise ValueError('certificate hash')
 certificate=json.loads(b);rows=[]
 for i,(file,pin) in enumerate(P):
  T=load(file,pin);both,layers=count(T,[0,1]);one,_=count(T,[0]);two,_=count(T,[1]);rec=certificate['cases'][i]
  if (both,one,two)!=(rec['common_transversals'],rec['first_square_only'],rec['second_square_only']):raise ValueError('count mismatch')
  for p in rec['all_common_transversals']:
   if sorted(p)!=list(range(8)) or any(len({T[k][row][p[row]] for row in range(8)})!=8 for k in range(2)):raise ValueError('bad listed transversal')
  rows.append({'source':file,'common_transversals':both,'first_only':one,'second_only':two,'partial_assignment_counts_by_depth':layers})
 if [r['common_transversals'] for r in rows]!=[0,16]:raise ValueError('unexpected outcome')
 # Mutations checked against exact predicates rather than relying on solver failure.
 bad=list(certificate['cases'][1]['all_common_transversals'][0]);bad[1]=bad[0]
 if sorted(bad)==list(range(8)):raise ValueError('duplicate mutation')
 out={'result':'PASS_INDEPENDENT_TWO_NET_TRANSVERSAL_DP','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'producer_receipt_sha256':CERT,'cases':rows,'duplicate_column_mutation':'rejected',
      'elapsed_seconds':time.monotonic()-start,'limits':'Finite count only; no global two-MOLS classification import.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
