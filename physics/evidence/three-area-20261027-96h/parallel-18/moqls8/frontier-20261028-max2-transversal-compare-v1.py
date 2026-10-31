#!/usr/bin/env python3
"""Compare every DP count with independently enumerated 8! permutations."""
import argparse,collections,csv,hashlib,io,json,pathlib,time
H=pathlib.Path(__file__).parent
DP='frontier-20261028-max2-transversal-scan-receipt-v1.json';DH='0745ac58eec8d02851910feedbff1ba29e6c8c8b247a1539d2f7e961b13142e4'
CSV='frontier-20261028-max2-transversal-exhaust-v1.csv';CH='379d3843d889cc1937e476788b5f57265cc95ece15f6e15cd276b224d585079d'
def get(name,pin):
 b=(H/name).read_bytes()
 if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('pin '+name)
 return b

def check(A,B):
 if len(A)!=2127 or len(B)!=2127:raise ValueError('coverage')
 for i,(x,y) in enumerate(zip(A,B)):
  if x['index']!=i or int(y['index'])!=i or int(y['permutations_tested'])!=40320 or x['common_transversals']!=int(y['common_transversals']):raise ValueError('case mismatch')
 return collections.Counter(x['common_transversals'] for x in A)

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 D=json.loads(get(DP,DH));rows=list(csv.DictReader(io.StringIO(get(CSV,CH).decode('ascii'))))
 if D['result']!='COMPLETE_MAXIMAL_SOURCE_TRANSVERSAL_CENSUS':raise ValueError('incomplete producer')
 hist=check(D['records'],rows);controls={}
 for name,mut in [('missing_case',lambda z:z.pop()),('changed_count',lambda z:z[0].update({'common_transversals':'1'}))]:
  b=[x.copy() for x in rows];mut(b)
  try:check(D['records'],b)
  except (ValueError,KeyError):controls[name]='rejected'
  else:raise ValueError('mutation passed')
 out={'result':'PASS_ALL_2127_DP_VS_40320_PERMUTATIONS',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'dp_receipt_sha256':DH,'independent_csv_sha256':CH,'cases':len(rows),'permutations_each':40320,
      'histogram':{str(k):v for k,v in sorted(hist.items())},'zero_transversal_pairs':hist[0],
      'positive_transversal_pairs':sum(v for k,v in hist.items() if k>0),
      'mutation_controls':controls,'elapsed_seconds':time.monotonic()-start,
      'limits':'Exact finite two-source-code count over the pinned local input. Source classification/completeness, maximality and any quantum family conclusion are separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
