#!/usr/bin/env python3
"""Actual classical four-family and duplicate mutation for the q2 support encoding."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
M=[('enc','frontier-20261028-q2-two-classical-support-cnf-v1.py','3bd85257dddab938638903ef737200791adf47c6a4869636b819d718cbda2ad8'),
   ('net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'),
   ('phys','frontier-20261028-q1-support-physical-control-v1.py','ca8f42999f128a8f42a98c480c81eca747abeb60497af9513202f881d0234a8c')]
mods={}
for name,file,pin in M:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('module pin')
 spec=importlib.util.spec_from_file_location(name,H/file);z=importlib.util.module_from_spec(spec);spec.loader.exec_module(z);mods[name]=z
V=range(8)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 name='frontier-20261028-q1-support-physical-control-receipt-v1.json';pin='48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3'
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('control pin')
 Q=json.loads(b)['positive_Q_classical_symbols'];nets=sum((mods['net'].read_catalogue(*v) for v in mods['net'].P),[])
 T=mods['net'].orient(nets[38],0,1,0);R=[T[0][i][j] for i in V for j in V];C=[T[1],T[2]]
 good=mods['phys'].physical(Q,T)
 if any(good.values()):raise ValueError('physical positive')
 data,info=mods['enc'].build(C,False);L=data.decode('ascii').splitlines();F=[list(map(int,z.split()))[:-1] for z in L[1:]]
 facts={x:(x//8,x%8,*(U[x//8][x%8] for U in C)) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 def adj(x,y):return any(u==v for u,v in zip(facts[x],facts[y]))
 E=[(x,y) for x,y in itertools.combinations(range(8,64),2) if adj(x,y)]
 def assign(Q0,R0):
  n=0;val={};P={}
  for q,S in enumerate((Q0,R0)):
   for x in A:
    for t in A[x]:n+=1;P[q,x,t]=n;val[n]=(S[x]==t)
  B={}
  for q in range(2):
   for x,y in E:
    common=sorted(set(A[x])&set(A[y]))
    if len(common)>=2:
     for t in common:n+=1;B[q,x,y,t]=n;val[n]=(val[P[q,x,t]] and val[P[q,y,t]])
  if n!=info['variables']:raise ValueError('control auxiliary numbering')
  bad=sum(not any(val[abs(l)] if l>0 else not val[abs(l)] for l in row) for row in F)
  triangle_viol=0;triangle_count=0
  for x,y,z in itertools.combinations(range(8,64),3):
   if not(adj(x,y) and adj(x,z) and adj(y,z)):continue
   common3=sorted(set(A[x])&set(A[y])&set(A[z]))
   for t,u in itertools.combinations(common3,2):
    triangle_count+=1
    for q in range(2):
     if all(val[B[q,i,j,t]] and val[B[q,i,j,u]] and not any(val[B[q,i,j,w]] for w in set(A[i])&set(A[j])-{t,u}) for i,j in ((x,y),(x,z),(y,z))):triangle_viol+=1
  return bad,triangle_count,triangle_viol
 goodcnf,triangles,tri_bad=assign(Q,R)
 if goodcnf or tri_bad:raise ValueError('physical family violates support encoding')
 bad=Q.copy();bad[9]=bad[8];badphys=mods['phys'].physical(bad,T);badcnf,_,_=assign(bad,R)
 if not badphys['row_gram_errors'] or not badcnf:raise ValueError('duplicate control not detected')
 out={'result':'PASS_ACTUAL_FOUR_FAMILY_Q2_SUPPORT_CONTROL','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'source_modules':{file:pin for name,file,pin in M},'q1_physical_control_receipt_sha256':pin,
      'positive_full_physical_gram_errors':good,'base_formula_sha256':info['formula_sha256'],
      'positive_base_clause_errors':goodcnf,'triangle_conditions_checked_per_member':triangles,
      'positive_triangle_violations':tri_bad,'negative_duplicate_physical_errors':badphys,
      'negative_base_clause_errors':badcnf,'elapsed_seconds':time.monotonic()-start,
      'limits':'Control on a different affine-extendible 4-net. No claim of nonclassical Q/R or classification completeness.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
