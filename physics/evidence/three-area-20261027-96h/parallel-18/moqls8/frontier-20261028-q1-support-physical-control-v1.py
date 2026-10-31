#!/usr/bin/env python3
"""Positive actual classical 4-family and negative mutation for q1 support CNF."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
import z3
H=pathlib.Path(__file__).parent
FILES=[('cnf','frontier-20261028-q1-support-cnf-v1.py','4c95605057d0dd540041b905f889b68e35fb6a8682011faed021a403c0cd4d53'),
       ('net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3')]
modules={}
for name,file,pin in FILES:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('source pin')
 spec=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);modules[name]=m
C=modules['cnf'];N=modules['net'];V=range(8)

def physical(Q,T):
 squares=[Q]+[[T[k][i][j] for i in V for j in V] for k in range(3)]
 row=col=pair=0
 for S in squares:
  for i in V:
   for j in V:
    for k in V:
     row+=(S[8*i+j]==S[8*i+k])!=(j==k)
     col+=(S[8*j+i]==S[8*k+i])!=(j==k)
 for a,b in itertools.combinations(range(4),2):
  for x in range(64):
   for y in range(64):pair+=((squares[a][x]==squares[a][y] and squares[b][x]==squares[b][y])!=(x==y))
 return {'row_gram_errors':int(row),'column_gram_errors':int(col),'pair_product_gram_errors':int(pair)}

def clauses(data):
 L=data.decode('ascii').splitlines();v=L[0].split();n,m=int(v[2]),int(v[3]);F=[list(map(int,s.split()))[:-1] for s in L[1:]]
 if len(F)!=m or any(not c or any(abs(z)>n for z in c) for c in F):raise ValueError('CNF')
 return n,F

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 triples=sum((N.read_catalogue(*z) for z in N.P),[]);T=N.orient(triples[38],0,1,0)
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(k for k in V if k not in facts[x][1:]) for x in range(8,64)}
 P={(x,t):z3.Bool(f'p_{x}_{t}') for x in A for t in A[x]};s=z3.Solver();s.set(timeout=4000)
 for x in A:s.add(z3.PbEq([(P[x,t],1) for t in A[x]],1))
 for k in range(5):
  for v in V:
   line=[x for x in range(64) if facts[x][k]==v]
   for t in V:
    if t in line:continue
    eligible=[P[x,t] for x in line if x>=8 and t in A[x]]
    if len(eligible)!=4:raise ValueError('axis count')
    s.add(z3.PbEq([(q,1) for q in eligible],1))
 if s.check()!=z3.sat:raise ValueError('classical completion unavailable')
 M=s.model();Q=list(V)+[next(t for t in A[x] if z3.is_true(M.eval(P[x,t],model_completion=True))) for x in range(8,64)]
 good=physical(Q,T)
 if any(good.values()):raise ValueError('classical family failed original physical check')
 data,meta=C.build(38,0,1,0,False);n,F=clauses(data);X=[None]+[z3.Bool(f'cnf_{i}') for i in range(1,n+1)];v=0
 for x in A:
  for t in A[x]:
   v+=1
   if v>224:raise ValueError('support ids')
 assert v==224
 def extension(q):
  ss=z3.Solver();ss.set(timeout=4000)
  for clause in F:ss.add(z3.Or([X[abs(lit)] if lit>0 else z3.Not(X[abs(lit)]) for lit in clause]))
  idx=0
  for x in A:
   for t in A[x]:idx+=1;ss.add(X[idx]==(q[x]==t))
  status=ss.check()
  if status==z3.sat:
   model=ss.model();bad=sum(not any(z3.is_true(model.eval(X[abs(l)] if l>0 else z3.Not(X[abs(l)]),model_completion=True)) for l in clause) for clause in F)
   if bad:raise ValueError('clause model')
  return str(status)
 goodcnf=extension(Q)
 if goodcnf!='sat':raise ValueError('physical family rejected by CNF')
 bad=Q.copy();bad[9]=bad[8];badphysical=physical(bad,T);badcnf=extension(bad)
 if not badphysical['row_gram_errors'] or badcnf!='unsat':raise ValueError('duplicate not rejected')
 out={'result':'PASS_PHYSICAL_FOUR_FAMILY_POSITIVE_AND_DUPLICATE_NEGATIVE',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'encoder_sha256':FILES[0][2],'net_module_sha256':FILES[1][2],
      'control_case':[38,0,1,0],'positive_Q_classical_symbols':Q,
      'positive_physical_full_gram_errors':good,'positive_cnf_status':goodcnf,
      'control_formula_sha256':meta['formula_sha256'],'control_formula_bytes':meta['formula_bytes'],
      'negative_duplicate_indices':[8,9],'negative_physical_full_gram_errors':badphysical,'negative_cnf_status':badcnf,
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Only a positive/negative control for encoder construction. No nonclassical witness or classification claim.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
