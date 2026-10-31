#!/usr/bin/env python3
"""Construct and check one actual QLS + two classical mates with 8 mixed cells."""
import argparse,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
MOD='frontier-20261028-anchor-sparse-net-obstructions-v1.py';PIN='6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'
if hashlib.sha256((H/MOD).read_bytes()).hexdigest()!=PIN:raise ValueError('source module pin')
spec=importlib.util.spec_from_file_location('net',H/MOD);net=importlib.util.module_from_spec(spec);spec.loader.exec_module(net)
V=range(8);TRADE={18,19,26,27,36,37,44,45}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def main():
 p=argparse.ArgumentParser();p.add_argument('--witness',required=True);p.add_argument('--receipt',required=True);a=p.parse_args();start=time.monotonic()
 triples=net.read_catalogue(*net.P[0]);T=triples[4];norm={symbol:j for j,symbol in enumerate(T[0][0])}
 Q0=[[norm[T[0][i][j]] for j in V] for i in V];M=[T[1],T[2]]
 if any(Q0[x//8][x%8] not in (0,1) for x in TRADE):raise ValueError('trade labels')
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in M)) for x in range(64)}
 checks=0
 for k in range(4):
  for v in V:
   line=[x for x in TRADE if facts[x][k]==v];checks+=1
   if len(line) not in (0,2) or (line and {Q0[x//8][x%8] for x in line}!={0,1}):raise ValueError('not a two-symbol four-net trade')
 Q=[];den=[]
 for x in range(64):
  z=Q0[x//8][x%8];vec=[0]*8
  if x in TRADE:vec[0]=1;vec[1]=1 if z==0 else -1;d=2
  else:vec[z]=1;d=1
  Q.append(vec);den.append(d)
 if any(den[j]!=1 or Q[j]!=[int(k==j) for k in V] for j in V):raise ValueError('first row not standard')
 rowerr=colerr=pairerr=0
 for member in range(3):
  for i in V:
   for j in V:
    for k in V:
     x=8*i+j;y=8*i+k;u=8*j+i;v=8*k+i
     if member==0:
      rowerr+=dot(Q[x],Q[y])!=(den[x] if j==k else 0)
      colerr+=dot(Q[u],Q[v])!=(den[u] if j==k else 0)
     else:
      L=M[member-1]
      rowerr+=(L[i][j]==L[i][k])!=(j==k)
      colerr+=(L[j][i]==L[k][i])!=(j==k)
 for p0 in range(3):
  for p1 in range(p0+1,3):
   for x in range(64):
    for y in range(64):
     if p0==0:
      b=M[p1-1][x//8][x%8]==M[p1-1][y//8][y%8]
      pairerr+=(dot(Q[x],Q[y])*b)!=(den[x] if x==y else 0)
     else:
      b0=M[p0-1][x//8][x%8]==M[p0-1][y//8][y%8]
      b1=M[p1-1][x//8][x%8]==M[p1-1][y//8][y%8]
      pairerr+=(b0 and b1)!=(x==y)
 if rowerr or colerr or pairerr or sum(d==2 for d in den)!=8:raise ValueError('full physical check')
 bad=[v[:] for v in Q];bad[19]=bad[18]
 if dot(bad[18],bad[19])==0:raise ValueError('duplicate mutation')
 witness={'kind':'ACTUAL_THREE_MOQLS_ONE_NONCLASSICAL_MIXED8','source_triple_index':4,'source_square_index':0,
          'quantum_square_numerators':Q,'quantum_square_denominator_squared':den,
          'classical_mates':M,'trade_cells':sorted(TRADE),
          'normalization':'Each numerator vector divided by sqrt(denominator_squared); independent per-cell phases irrelevant.',
          'limits':'Three-member family only, NOT a four-family witness; novelty not assessed.'}
 with pathlib.Path(a.witness).open('x',encoding='utf-8') as f:json.dump(witness,f,indent=2);f.write('\n')
 raw=pathlib.Path(a.witness).read_bytes()
 out={'result':'PASS_EXACT_THREE_FAMILY_MIXED8_WITNESS','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'source_module_sha256':PIN,'source_catalogue_sha256':net.P[0][1],'witness_sha256':hashlib.sha256(raw).hexdigest(),
      'line_trade_checks':checks,'row_gram_errors':int(rowerr),'column_gram_errors':int(colerr),'pair_product_gram_errors':int(pairerr),
      'mixed_cells':8,'first_row_standard':True,'duplicate_quantum_ray_control':'rejected',
      'elapsed_seconds':time.monotonic()-start,'limits':'Producer check only; independent finite-witness review and novelty screen still required.'}
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
