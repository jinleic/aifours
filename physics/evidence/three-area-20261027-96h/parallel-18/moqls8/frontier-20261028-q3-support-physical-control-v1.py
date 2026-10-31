#!/usr/bin/env python3
"""Actual classical four-family positive/duplicate-negative for q3 support conditions."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
MODS=[('net','frontier-20261028-anchor-sparse-net-obstructions-v1.py','6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3'),
      ('phys','frontier-20261028-q1-support-physical-control-v1.py','ca8f42999f128a8f42a98c480c81eca747abeb60497af9513202f881d0234a8c')]
mods={}
for name,file,pin in MODS:
 if hashlib.sha256((H/file).read_bytes()).hexdigest()!=pin:raise ValueError('module hash')
 s=importlib.util.spec_from_file_location(name,H/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);mods[name]=m
V=range(8)
def necessary(Qs,L):
 f={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:set(V)-set(f[x][1:]) for x in range(8,64)}
 lines=[[x for x in range(64) if f[x][k]==v] for k in range(3) for v in V]
 S=[{x:{Q[x]} for x in A} for Q in Qs];e={'allowed':0,'same_cell_disjoint':0,'line_singleton':0,'axis_coverage':0,'cross_member_product_singleton':0}
 for x in A:
  for q in range(3):e['allowed']+=not(S[q][x]<=A[x])
  for p,q in itertools.combinations(range(3),2):e['same_cell_disjoint']+=bool(S[p][x]&S[q][x])
 for line in lines:
  for q in range(3):
   for x,y in itertools.combinations((x for x in line if x>=8),2):e['line_singleton']+=len(S[q][x]&S[q][y])==1
   for t in V:
    if t not in line:e['axis_coverage']+=not any(t in S[q][x] for x in line if x>=8)
 for p,q in itertools.combinations(range(3),2):
  for x,y in itertools.combinations(A,2):e['cross_member_product_singleton']+=(len(S[p][x]&S[p][y])==1 and len(S[q][x]&S[q][y])==1)
 return {k:int(v) for k,v in e.items()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 file=H/'frontier-20261028-q1-support-physical-control-receipt-v1.json';b=file.read_bytes();pin='48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3'
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('control pin')
 Q=json.loads(b)['positive_Q_classical_symbols'];nets=sum((mods['net'].read_catalogue(*v) for v in mods['net'].P),[]);T=mods['net'].orient(nets[38],0,1,0)
 Qs=[Q]+[[T[k][i][j] for i in V for j in V] for k in (0,1)];L=T[2]
 original=mods['phys'].physical(Q,T);good=necessary(Qs,L)
 if any(original.values()) or any(good.values()):raise ValueError('physical control fails')
 bad=[q.copy() for q in Qs];bad[0][9]=bad[0][8];badphysics=mods['phys'].physical(bad[0],T);badnecessary=necessary(bad,L)
 if not badphysics['row_gram_errors'] or not any(badnecessary.values()):raise ValueError('duplicate not rejected')
 out={'result':'PASS_ACTUAL_FOUR_FAMILY_Q3_NECESSARY_CONDITION_CONTROL',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'control_receipt_sha256':pin,'positive_full_physical_gram_errors':original,'positive_necessary_errors':good,
      'negative_duplicate_physical_errors':badphysics,'negative_necessary_errors':badnecessary,
      'elapsed_seconds':time.monotonic()-start,'limits':'Control uses four classical squares; it is not a q3 example or positive support formula model.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
