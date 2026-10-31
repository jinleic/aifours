#!/usr/bin/env python3
"""Independent bitmask-DP count for six explicit maximal-source net pairs."""
import argparse,hashlib,importlib.util,json,pathlib,time
H=pathlib.Path(__file__).parent
MOD='frontier-20261028-two-nets-transversal-dp-check-v1.py';MP='9d6e97947d01e878a7b14b34a30622eab2b3cf239f5b41eadef23c23c1666189'
CERT='frontier-20261028-max2-first6-extract-receipt-v1.json';CP='f58411c0dda157fe44468e9b8be9d6312d73c5fbd9bfd8c9cb172f291624a491'
if hashlib.sha256((H/MOD).read_bytes()).hexdigest()!=MP:raise ValueError('DP module pin')
s=importlib.util.spec_from_file_location('dp',H/MOD);dp=importlib.util.module_from_spec(s);s.loader.exec_module(dp)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();start=time.monotonic();b=(H/CERT).read_bytes()
 if hashlib.sha256(b).hexdigest()!=CP:raise ValueError('source receipt pin')
 rec=json.loads(b)['records']
 if [z['index'] for z in rec]!=list(range(6)):raise ValueError('sample coverage')
 out=[]
 for x in rec:
  T=dp.load(x['file'],x['sha256']);n,layers=dp.count(T,[0,1]);n1,_=dp.count(T,[0]);n2,_=dp.count(T,[1])
  if (n,n1,n2)!=(x['common_transversals'],x['first_only'],x['second_only']):raise ValueError('count mismatch')
  out.append({'index':x['index'],'source_sha256':x['sha256'],'common_transversals':n,'partial_counts_by_depth':layers})
 if any(x['common_transversals'] for x in out):raise ValueError('unexpected nonzero')
 report={'result':'PASS_INDEPENDENT_SIX_ZERO_TRANSVERSAL_COUNTS','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
         'input_receipt_sha256':CP,'dp_module_sha256':MP,'cases':out,'elapsed_seconds':time.monotonic()-start,
         'limits':'Finite invariant for six explicit pairs; no source classification/completeness implied.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
