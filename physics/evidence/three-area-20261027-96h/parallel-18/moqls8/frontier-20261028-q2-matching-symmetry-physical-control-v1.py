#!/usr/bin/env python3
"""Physical classical-family control for ONB support matching and Q/R swap."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
MODS=[('net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'),
      ('phys','frontier-20261028-q1-support-physical-control-v1.py','ca8f42999f128a8f42a98c480c81eca747abeb60497af9513202f881d0234a8c')]
mods={}
for name,file,pin in MODS:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('source pin')
 s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m
V=range(8)
def evaluate(Q,R,C):
 f={x:(x//8,x%8,*(L[x//8][x%8] for L in C)) for x in range(64)}
 A={x:set(V)-set(f[x][1:]) for x in range(8,64)};errors={'allowed':0,'cell_disjoint':0,'line_matching':0,'member_order':0};checked=0
 for x in A:
  errors['allowed']+=Q[x] not in A[x];errors['allowed']+=R[x] not in A[x];errors['cell_disjoint']+=Q[x]==R[x]
 for U in (Q,R):
  for k in range(4):
   for z in V:
    line=[x for x in range(64) if f[x][k]==z];checked+=1
    if len(line)!=8 or len({U[x] for x in line})!=8:errors['line_matching']+=1
 errors['member_order']+=not(Q[8]<R[8])
 return {k:int(v) for k,v in errors.items()},checked

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 b=(H/'frontier-20261028-q1-support-physical-control-receipt-v1.json').read_bytes();pin='48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3'
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('control pin')
 Q=json.loads(b)['positive_Q_classical_symbols'];nets=sum((mods['net'].read_catalogue(*z) for z in mods['net'].P),[]);T=mods['net'].orient(nets[38],0,1,0)
 R=[T[0][i][j] for i in V for j in V];C=[T[1],T[2]];physical=mods['phys'].physical(Q,T)
 if any(physical.values()):raise ValueError('physical control')
 swapped=Q[8]>R[8]
 if swapped:Q,R=R,Q
 good,count=evaluate(Q,R,C)
 if any(good.values()):raise ValueError('matching or symmetry positive control')
 wrongorder,_=evaluate(R,Q,C)
 if not wrongorder['member_order'] or any(v for k,v in wrongorder.items() if k!='member_order'):raise ValueError('swap ordering control')
 bad=Q.copy();bad[9]=bad[8];baderrors,_=evaluate(bad,R,C)
 if not baderrors['line_matching']:raise ValueError('matching duplicate control')
 out={'result':'PASS_PHYSICAL_MATCHING_AND_MEMBER_SWAP_CONTROLS',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'positive_full_physical_gram_errors':physical,'positive_matching_symmetry_errors':good,
      'member_swap_needed_for_order':swapped,'reversed_order_errors':wrongorder,
      'duplicate_cell_errors':baderrors,'member_line_matchings_checked':count,
      'elapsed_seconds':time.monotonic()-start,'limits':'Standalone all-classical positive control, not q2 witness or proof of full encoding.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
