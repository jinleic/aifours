#!/usr/bin/env python3
"""Bounded exact DP census of common transversals for pinned maximal-source pairs."""
import argparse,collections,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-complete-v1.txt';PIN='6786f29c22c354673df942485faeed7d462ebaf4e3916b7a649cc0ff6a303154'
DP='frontier-20261028-two-nets-transversal-dp-check-v1.py';DPH='9d6e97947d01e878a7b14b34a30622eab2b3cf239f5b41eadef23c23c1666189'
if hashlib.sha256((H/DP).read_bytes()).hexdigest()!=DPH:raise ValueError('DP source pin')
s=importlib.util.spec_from_file_location('dpmax',H/DP);dp=importlib.util.module_from_spec(s);s.loader.exec_module(dp)
V=range(8)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic();limit=25.0
 b=(H/SRC).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source pin')
 L=[z.strip() for z in b.decode('ascii').splitlines() if z.strip()]
 if L[0].split()[:3]!=['8','8','4254'] or len(L)!=34033:raise ValueError('source count')
 records=[];hist=collections.Counter()
 for k in range(2127):
  if time.monotonic()-start>limit:break
  T=[[[ord(c)-97 for c in L[1+16*k+8*j+i]] for i in V] for j in range(2)]
  for S in T:
   if any(set(row)!=set(V) for row in S) or any({S[i][j] for i in V}!=set(V) for j in V):raise ValueError('not Latin')
  if len({(T[0][i][j],T[1][i][j]) for i in V for j in V})!=64:raise ValueError('not MOLS')
  count,layers=dp.count(T,[0,1]);hist[count]+=1;records.append({'index':k,'common_transversals':count,'partial_assignment_counts':layers})
 if len(records)>=6 and any(x['common_transversals'] for x in records[:6]):raise ValueError('first-six control')
 out={'result':'COMPLETE_MAXIMAL_SOURCE_TRANSVERSAL_CENSUS' if len(records)==2127 else 'PARTIAL_TIME_BOUND',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'snapshot_sha256':PIN,'dp_module_sha256':DPH,
      'requested_pairs':2127,'completed_pairs':len(records),'common_transversal_histogram':dict(sorted(hist.items())),
      'records':records,'time_limit_seconds':limit,'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact combinatorial data for local source pairs, not a quantum-family proof; source completeness and independent full-census audit remain separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
