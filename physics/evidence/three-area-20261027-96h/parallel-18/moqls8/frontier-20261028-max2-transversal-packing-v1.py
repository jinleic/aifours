#!/usr/bin/env python3
"""Exact common-transversal packing for the 147 positive maximal-source pairs."""
import argparse,collections,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-complete-v1.txt';SH='6786f29c22c354673df942485faeed7d462ebaf4e3916b7a649cc0ff6a303154'
REC='frontier-20261028-max2-transversal-scan-receipt-v1.json';RH='0745ac58eec8d02851910feedbff1ba29e6c8c8b247a1539d2f7e961b13142e4'
MOD='frontier-20261028-two-nets-transversal-census-v1.py';MH='035a11d4f02fa708a1d3a9e5693800b3d8af22ba68b3f8627bc6f334e7464990'
def pin(p,h):
 b=(H/p).read_bytes()
 if hashlib.sha256(b).hexdigest()!=h:raise ValueError('pin '+p)
 return b
pin(MOD,MH);sp=importlib.util.spec_from_file_location('transversal',H/MOD);tr=importlib.util.module_from_spec(sp);sp.loader.exec_module(tr)
V=range(8)
def packed(trans):
 masks=[sum(1<<(8*i+j) for i,j in enumerate(p)) for p in trans];n=len(masks);adj=[]
 for i in range(n):adj.append(sum(1<<j for j in range(n) if j!=i and masks[i]&masks[j]==0))
 best=[];nodes=0
 def visit(candidates,chosen):
  nonlocal best,nodes
  nodes+=1
  if len(chosen)+candidates.bit_count()<=len(best):return
  if not candidates:
   if len(chosen)>len(best):best=chosen[:]
   return
  while candidates:
   if len(chosen)+candidates.bit_count()<=len(best):return
   bit=candidates&-candidates;candidates-=bit;i=bit.bit_length()-1
   visit(candidates&adj[i],chosen+[i])
 visit((1<<n)-1,[])
 return best,nodes

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic()
 L=[s.strip() for s in pin(SRC,SH).decode('ascii').splitlines() if s.strip()];D=json.loads(pin(REC,RH))
 if L[0].split()[:3]!=['8','8','4254'] or len(L)!=34033 or D['completed_pairs']!=2127:raise ValueError('source/coverage')
 entries=[];hist=collections.Counter()
 for r in D['records']:
  k=r['index'];expected=r['common_transversals']
  if expected==0:continue
  T=[[[ord(c)-97 for c in L[1+16*k+8*j+i]] for i in V] for j in range(2)]
  trans,nodes=tr.dfs(T)
  if len(trans)!=expected:raise ValueError('transversal mismatch')
  best,search=packed(trans)
  if len(best)>=8:raise ValueError('source pair has an extension')
  hist[len(best)]+=1;entries.append({'index':k,'transversals':[list(z) for z in trans],
          'maximum_disjoint':len(best),'packing_witness_indices':best,'dfs_nodes':nodes,'packing_search_nodes':search})
 if len(entries)!=147:raise ValueError('positive case count')
 non=tr.matrices('frontier-20261028-source-wanless-nonmax2-first-pair-v1.txt','2c32f66b0c4be0d995ff8db895e0b942034889ccd8523212f451bbab818a53a4',2)
 control,_=tr.dfs(non);best,_=packed(control)
 if len(control)!=16 or len(best)!=8:raise ValueError('extendible positive control')
 out={'result':'PASS_ALL_147_POSITIVE_PAIRS_HAVE_PACKING_BELOW_8',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'source_snapshot_sha256':SH,'transversal_census_sha256':RH,'enumerator_sha256':MH,
      'zero_transversal_pairs':1980,'positive_pairs':len(entries),'maximum_packing_histogram':dict(sorted(hist.items())),
      'cases':entries,'extendible_control_transversals':16,'extendible_control_maximum_packing':len(best),
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact local pair/transversal packing; source species completeness and quantum-family conclusions are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
