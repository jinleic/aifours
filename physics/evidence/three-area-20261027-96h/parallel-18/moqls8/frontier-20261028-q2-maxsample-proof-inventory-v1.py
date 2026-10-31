#!/usr/bin/env python3
"""Bind six explicit zero-transversal pairs and their local q2 proof evidence."""
import argparse,datetime,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
P={'frontier-20261028-max2-first6-extract-receipt-v1.json':'f58411c0dda157fe44468e9b8be9d6312d73c5fbd9bfd8c9cb172f291624a491',
   'frontier-20261028-max2-first6-transversal-check-receipt-v1.json':'42d28893afc43f2153facd780bb6c0ad8588c3fa5386839196cc3290c8ea600a',
   'frontier-20261028-q2-maxpair0-cnf-check-receipt-v2.json':'07ce52bbde17d0b25214f32205b15be9c59802e486e4065f6a46a0da26eb5694',
   'frontier-20261028-q2-measured-fifo-replay-receipt-v3.json':'bd8a9eaa2913dffaf784f958fdf51f654d5150e28c41ecfc1498259ceab6a4f9',
   'frontier-20261028-q2-maxpair0-v2.cnf':'0194fa8d89d6c9813a2a0c620e95a810148d5f33d3c9c43495572c91e318791a',
   'frontier-20261028-q2-maxpair0-proof-v2.drup':'b6514cbce482b0beb0be9fa7484fc4d70cc37767041dfe49fc73c2d3f3f8e46f'}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(name,pin=None):
 b=(H/name).read_bytes()
 if pin and sha(b)!=pin:raise ValueError('pin mismatch '+name)
 return b
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 for f,h in P.items():get(f,h)
 extract=json.loads(get('frontier-20261028-max2-first6-extract-receipt-v1.json'))['records'];dp=json.loads(get('frontier-20261028-max2-first6-transversal-check-receipt-v1.json'))['cases']
 if [z['index'] for z in extract]!=list(range(6)) or [z['index'] for z in dp]!=list(range(6)) or any(z['common_transversals']!=0 for z in extract+dp):raise ValueError('transversal coverage')
 rep=json.loads(get('frontier-20261028-q2-measured-fifo-replay-receipt-v3.json'));aud=json.loads(get('frontier-20261028-q2-maxpair0-cnf-check-receipt-v2.json'))
 if rep['result']!='OWNER_LOCAL_MEASURED_FIFO_PASS' or not rep['actual']['strict_pass'] or aud['result']!='PASS_INDEPENDENT_Q2_FULL_CLAUSE_MULTISET' or aud['formula_sha256']!=rep['cnf_sha256']:raise ValueError('case0')
 batchname='frontier-20261028-q2-maxsample-01-05-batch-receipt-v1.json';bb=get(batchname);batch=json.loads(bb)
 if batch['result']!='BOUNDED_BATCH_COMPLETE' or batch['range']!=[1,5] or [r['index'] for r in batch['records']]!=list(range(1,6)):raise ValueError('batch coverage')
 rows=[{'index':0,'pair':extract[0]['file'],'pair_sha256':extract[0]['sha256'],'common_transversals':0,
        'formula':'frontier-20261028-q2-maxpair0-v2.cnf','formula_sha256':P['frontier-20261028-q2-maxpair0-v2.cnf'],
        'proof':'frontier-20261028-q2-maxpair0-proof-v2.drup','proof_sha256':P['frontier-20261028-q2-maxpair0-proof-v2.drup'],
        'replay_receipt':'frontier-20261028-q2-measured-fifo-replay-receipt-v3.json','replay_receipt_sha256':P['frontier-20261028-q2-measured-fifo-replay-receipt-v3.json']}]
 for r in batch['records']:
  i=r['index'];s=r['solver'];z=r['replay'];pair=extract[i]
  if r['pair']!=pair or r['outcome']!='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW' or r['independent_clause_multiset']!='PASS':raise ValueError('case outcome')
  if s['returncode']!=20 or s['status_lines']!=['s UNSATISFIABLE'] or s['stop'] is not None or s['stderr'] or not z['strict_pass'] or not z['transport_exact'] or z['returncode']!=0 or z['status_lines']!=['s VERIFIED']:raise ValueError('process')
  if z['checker_reported_proof_bytes']!=z['proof_feed']['bytes'] or z['cnf_feed']['sha256']!=r['formula_sha256'] or z['cnf_fifo_remaining_bytes']!=0:raise ValueError('delivery')
  get(pair['file'],pair['sha256']);cb=get(r['formula'],r['formula_sha256']);pb=get(r['proof'],r['proof_sha256']);get(r['case_receipt'],r['case_receipt_sha256'])
  if len(cb)!=r['formula_bytes'] or len(pb)!=r['proof_bytes'] or pb.splitlines()[-1]!=b'0':raise ValueError('retained bytes')
  rows.append({'index':i,'pair':pair['file'],'pair_sha256':pair['sha256'],'common_transversals':0,
               'formula':r['formula'],'formula_sha256':r['formula_sha256'],'proof':r['proof'],'proof_sha256':r['proof_sha256'],
               'case_receipt':r['case_receipt'],'case_receipt_sha256':r['case_receipt_sha256']})
 out={'result':'SIX_ZERO_TRANSVERSAL_NETS_HAVE_OWNER_LOCAL_Q2_PROOF_EVIDENCE',
      'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'observed_at':datetime.datetime.now().astimezone().isoformat(),
      'input_pins':P,'batch_receipt':batchname,'batch_receipt_sha256':sha(bb),'records':rows,
      'limits':'Metadata composition only; owner-local proofs need disjoint review and separately owned parent replay; no complete maximal-pair classification.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
