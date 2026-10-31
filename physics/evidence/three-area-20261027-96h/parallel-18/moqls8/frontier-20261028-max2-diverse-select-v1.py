#!/usr/bin/env python3
"""Extract six maximal-source pairs with different positive transversal counts."""
import argparse,hashlib,json,pathlib,time
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-complete-v1.txt';SH='6786f29c22c354673df942485faeed7d462ebaf4e3916b7a649cc0ff6a303154'
REC='frontier-20261028-max2-transversal-compare-receipt-v1.json';RH='6b15489aaeedffbc3c2c7b3b73fb5ba631026aeb696461da6a7e1e031c98fd9a'
CSV='frontier-20261028-max2-transversal-exhaust-v1.csv';CH='379d3843d889cc1937e476788b5f57265cc95ece15f6e15cd276b224d585079d'
SELECT=[(620,1),(69,2),(1340,3),(64,4),(194,8),(921,12)]
def pin(name,h):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=h:raise ValueError('pin '+name)
 return b

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 rows=[s.strip() for s in pin(SRC,SH).decode('ascii').splitlines() if s.strip()]
 if rows[0].split()[:3]!=['8','8','4254'] or len(rows)!=34033:raise ValueError('source layout')
 check=json.loads(pin(REC,RH))
 if check['result']!='PASS_ALL_2127_DP_VS_40320_PERMUTATIONS':raise ValueError('count audit')
 entries=pin(CSV,CH).decode('ascii').splitlines()
 if len(entries)!=2128:raise ValueError('count coverage')
 out=[]
 for i,k in SELECT:
  idx,count,tests=map(int,entries[i+1].split(','))
  if (idx,count,tests)!=(i,k,40320):raise ValueError('selected count')
  name=f'frontier-20261028-source-wanless-max2-pair{i:04d}-v1.txt'
  text=f'8 8 2 ## maximal-source representative index {i}\n'+'\n'.join(rows[1+16*i:1+16*(i+1)])+'\n'
  with (H/name).open('x',encoding='ascii') as f:f.write(text)
  out.append({'index':i,'common_transversals':k,'file':name,'sha256':hashlib.sha256(text.encode()).hexdigest()})
 report={'result':'SIX_DIVERSE_MAXIMAL_SOURCE_PAIRS_EXTRACTED',
         'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'source_snapshot_sha256':SH,
         'independent_count_audit_sha256':RH,'records':out,'elapsed_seconds':time.monotonic()-start,
         'limits':'Six selected input pairs only; no exhaustive q2 proof, physical witness or source classification claim.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
