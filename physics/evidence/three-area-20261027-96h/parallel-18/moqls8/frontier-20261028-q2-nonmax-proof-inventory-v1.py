#!/usr/bin/env python3
"""Metadata binding of bounded q2 proofs and unresolved net cases."""
import argparse,datetime,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
PINS={'frontier-20261028-source-wanless-nonmax2-complete-v1.txt':'9011d27cf7d1d2383d106d1b01d4dcb897e51743fa7496833fe12679faa02061',
      'frontier-20261028-nonmax2-net-extract-receipt-v1.json':'cda00277e356426194cc2051d7e92b32ad6f639f017f621ef0b69e9d0fbcdf8d',
      'frontier-20261028-q2-nonmax0-fifo-replay-receipt-v1.json':'406aeff1f89ad79e2c5855671bd700f1e1e7634e0fba34f290e66405af743eb9',
      'frontier-20261028-q2-nonmaxpair0-cnf-check-receipt-v1.json':'5e479a2f8c84007ebd61c00309eaf7cc4c9a67aec9efdeececda0115365888ae',
      'frontier-20261028-q2-nonmaxpair0-v1.cnf':'fdd256377bb78ccb9493774832a4269600146feb0f3df67a5092c3c770388efe',
      'frontier-20261028-q2-nonmaxpair0-proof-v1.drup':'4ed008668cd3f1cecbbf121e9c339814a6c4581922f4eb6e6cbe258da356d91f'}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(name,pin=None):
 b=(H/name).read_bytes()
 if pin and sha(b)!=pin:raise ValueError('pin mismatch '+name)
 return b

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 for name,h in PINS.items():get(name,h)
 extract=json.loads(get('frontier-20261028-nonmax2-net-extract-receipt-v1.json'));items={z['index']:z for z in extract['pairs']}
 if set(items)!=set(range(1,38)):raise ValueError('pair coverage')
 batches=[]
 for name in ('frontier-20261028-q2-nonmax-batch-01-03-receipt-v1.json','frontier-20261028-q2-nonmax-batch-04-37-receipt-v1.json'):
  b=get(name);z=json.loads(b)
  if z['result']!='BOUNDED_BATCH_COMPLETE':raise ValueError('batch incomplete')
  batches.append({'file':name,'sha256':sha(b),'range':z['range'],'records':z['records']})
 if [z['range'] for z in batches]!=[[1,3],[4,37]]:raise ValueError('range')
 allrec=[r for b in batches for r in b['records']]
 if [r['index'] for r in allrec]!=list(range(1,38)):raise ValueError('coverage')
 r0=json.loads(get('frontier-20261028-q2-nonmax0-fifo-replay-receipt-v1.json',PINS['frontier-20261028-q2-nonmax0-fifo-replay-receipt-v1.json']))
 if r0['result']!='OWNER_LOCAL_MEASURED_FIFO_PASS' or not r0['actual']['strict_pass']:raise ValueError('case0')
 rows=[{'index':0,'outcome':'OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW',
        'formula':'frontier-20261028-q2-nonmaxpair0-v1.cnf','formula_sha256':PINS['frontier-20261028-q2-nonmaxpair0-v1.cnf'],
        'proof':'frontier-20261028-q2-nonmaxpair0-proof-v1.drup','proof_sha256':PINS['frontier-20261028-q2-nonmaxpair0-proof-v1.drup'],
        'replay_receipt':'frontier-20261028-q2-nonmax0-fifo-replay-receipt-v1.json','replay_receipt_sha256':PINS['frontier-20261028-q2-nonmax0-fifo-replay-receipt-v1.json']}]
 for rec in allrec:
  i=rec['index'];item=items[i]
  if rec['pair']!=item:raise ValueError('pair metadata mismatch')
  get(item['file'],item['sha256']);cb=get(rec['formula'],rec['formula_sha256'])
  if len(cb)!=rec['formula_bytes']:raise ValueError('CNF length')
  if rec['proof']:
   pb=get(rec['proof'],rec['proof_sha256'])
   if len(pb)!=rec['proof_bytes']:raise ValueError('proof length')
  rb=get(rec['case_receipt'],rec['case_receipt_sha256']);stored=json.loads(rb)
  if stored['index']!=i or stored['outcome']!=rec['outcome'] or stored['formula_sha256']!=rec['formula_sha256']:raise ValueError('receipt mismatch')
  s=rec['solver'];o=rec['outcome']
  if rec['independent_clause_multiset']!='PASS':raise ValueError('encoding audit')
  if o=='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW':
   rr=rec['replay']
   if s['returncode']!=20 or s['status_lines']!=['s UNSATISFIABLE'] or s['stop'] is not None or s['stderr'] or not rr['strict_pass'] or not rr['transport_exact'] or rr['status_lines']!=['s VERIFIED'] or rr['returncode']!=0:raise ValueError('pass predicate')
   if rr['checker_reported_proof_bytes']!=rr['proof_feed']['bytes'] or rr['cnf_feed']['sha256']!=rec['formula_sha256'] or rr['cnf_fifo_remaining_bytes']!=0:raise ValueError('delivery')
  elif o=='UNKNOWN':
   if s['status_lines']!=['s UNKNOWN']:raise ValueError('unexplained unknown')
  elif o!='SAT_SUPPORT_ONLY_NOT_PHYSICAL_WITNESS':raise ValueError('unrecognized outcome')
  rows.append({'index':i,'outcome':o,'pair_file':item['file'],'pair_sha256':item['sha256'],
               'formula':rec['formula'],'formula_sha256':rec['formula_sha256'],'proof':rec['proof'],
               'proof_sha256':rec['proof_sha256'],'proof_bytes':rec['proof_bytes'],
               'case_receipt':rec['case_receipt'],'case_receipt_sha256':rec['case_receipt_sha256']})
 counts={}
 for r in rows:counts[r['outcome']]=counts.get(r['outcome'],0)+1
 unresolved=[r['index'] for r in rows if r['outcome']!='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW']
 out={'result':'Q2_NONMAX_RETAINED_EVIDENCE_INVENTORIED','source_sha256':sha(pathlib.Path(__file__).read_bytes()),
      'observed_at':datetime.datetime.now().astimezone().isoformat(),'source_pins':PINS,
      'batch_receipts':[{k:v for k,v in b.items() if k!='records'} for b in batches],
      'indices':len(rows),'outcomes':counts,'unresolved_indices':unresolved,'records':rows,
      'limits':'Metadata inventory of owner-local proof/transport receipts only. Unknowns remain unresolved; no parent replay, physical proof review or catalogue completeness.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
