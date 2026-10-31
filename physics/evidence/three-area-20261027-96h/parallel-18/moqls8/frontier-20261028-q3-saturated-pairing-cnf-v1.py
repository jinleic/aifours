#!/usr/bin/env python3
"""q3 (2,2,2) cell branch by an exact partition into three unordered axis pairs."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q3-cell-cardinality-cnf-v1.py';PIN='d39808618d682ddde86a854b957f9f6857bd7084bae418fbdca98ebb078f936d'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('cardinality encoder pin')
spec=importlib.util.spec_from_file_location('q3card',H/FILE);card=importlib.util.module_from_spec(spec);spec.loader.exec_module(card)
V=range(8)
def partitions(xs):
 if not xs:yield ();return
 x=xs[0]
 for j in range(1,len(xs)):
  y=xs[j];rest=xs[1:j]+xs[j+1:]
  for z in partitions(rest):yield ((x,y),)+z

def build(L,chosen):
 data,info=card.build(L,2,2,2);f={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:tuple(t for t in V if t not in f[x][1:]) for x in range(8,64)};P={};i=0
 for q in range(3):
  for x in A:
   for t in A[x]:i+=1;P[q,x,t]=i
 allp=list(partitions(A[8]));choice=tuple(tuple(z) for z in chosen)
 if i!=1008 or len(allp)!=15 or choice not in allp:raise ValueError('partition coverage')
 units=[(P[q,8,t],) for q,pair in enumerate(choice) for t in pair];lines=data.decode('ascii').splitlines()
 if len(lines)-1!=info['clauses']:raise ValueError('base count')
 out=('p cnf %d %d\n'%(info['variables'],info['clauses']+len(units))+'\n'.join(lines[1:])+'\n'+''.join('%d 0\n'%z[0] for z in units)).encode('ascii')
 return out,{'variables':info['variables'],'clauses':info['clauses']+len(units),'base_card222_sha256':info['formula_sha256'],
             'chosen_partition':[list(z) for z in choice],'all_unordered_pair_partitions':[[list(z) for z in p] for p in allp],
             'formula_bytes':len(out),'formula_sha256':hashlib.sha256(out).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--partition',required=True,help='six comma-separated axes in canonical paired order');ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 nums=[int(x) for x in a.partition.split(',')]
 if len(nums)!=6:raise ValueError('six axes')
 choice=tuple((nums[2*i],nums[2*i+1]) for i in range(3));data,info=build(card.prod.base.net.latin(),choice)
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'cardinality_encoder_sha256':PIN,'classical_source_sha256':card.prod.base.net.PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'One of 15 member-permutation orbits for (2,2,2); SAT is not physical; UNSAT needs independent encoding and proof audit.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
