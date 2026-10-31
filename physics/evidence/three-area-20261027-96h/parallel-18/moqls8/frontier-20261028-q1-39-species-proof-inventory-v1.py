#!/usr/bin/env python3
"""Bind the completed per-species retained formulas, proofs and local receipts.

Metadata/integrity inventory; it does not rerun scientific proofs or claim
parent replay, classification completeness, or checker soundness.
"""
import argparse,datetime,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
PINS={'frontier-20261028-q1-support-cnf-v1.py':'4c95605057d0dd540041b905f889b68e35fb6a8682011faed021a403c0cd4d53',
      'frontier-20261028-q1-support-cnf-check-v1.py':'e824a35b1f304ce8472770d1d281a36d88ce983a95b480ce7de2697d0f19021b',
      'frontier-20261028-rup-proof-check-v1.py':'82e0b595da1798a67e83fc2b80885856dab3c004b07abddadb04fb59f31c08cc',
      'frontier-20261028-rup-scan-check-v1.py':'77fdc7f3918c6945adce1e7124c6e21552da1d57fbcedad3c52549e73c39321c',
      'frontier-20261028-q1-support-proof-batch-v1.py':'22a99215f45b9d56ce975d58ff98786e3f19d5fc26be4e4bbe9e05d68ccb7215',
      'frontier-20261028-q1-support-physical-control-receipt-v1.json':'48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3',
      'frontier-20261028-source-wanless-max3-order8-v1.txt':'95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',
      'frontier-20261028-source-wanless-nonmax3-order8-v1.txt':'f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5'}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(name):return (H/name).read_bytes()
def pinned(name,pin):
 b=get(name)
 if sha(b)!=pin:raise ValueError('pin mismatch '+name)
 return b

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
 for name,pin in PINS.items():pinned(name,pin)
 batches=[]
 for name in ('frontier-20261028-q1-support-batch-01-05-receipt-v1.json','frontier-20261028-q1-support-batch-06-38-receipt-v1.json'):
  b=get(name);record=json.loads(b)
  if record['result']!='COMPLETE' or record['source_sha256']!=PINS['frontier-20261028-q1-support-proof-batch-v1.py']:raise ValueError('incomplete batch or source mismatch')
  batches.append({'file':name,'sha256':sha(b),'range':record['batch_range'],'count':record['cases_completed'],'records':record['cases']})
 if [b['range'] for b in batches]!=[[1,5],[6,38]]:raise ValueError('batch range')
 allrec=[x for b in batches for x in b['records']]
 if [x['case'][0] for x in allrec]!=list(range(1,39)):raise ValueError('species coverage')
 rows=[]
 # Case 0 was run individually; its solver console was observed but not saved.
 cnf0='frontier-20261028-q1-support-species0-v1.cnf';proof0='frontier-20261028-q1-support-species0-proof-v1.drup'
 c0=pinned(cnf0,'0ddbe3818bba22fb3e040d669f0b81dcfe8f39f3b005db842a6c969db8f00f63')
 p0=pinned(proof0,'2d405f676add4fe7967e98722834c536d9545ed1a0038f4546b1721e55b33599')
 r0=json.loads(pinned('frontier-20261028-q1-support-species0-rup-receipt-v1.json','2aee669484ac244c590319e9c4b096ac3b07f809104bde8a408c0b238df8329c'))
 s0=json.loads(pinned('frontier-20261028-q1-support-species0-rup-scan-receipt-v1.json','a19976859fa40579fe89454c2834422c0f9ac949cfe14e9dc7db431a62f6503e'))
 e0=json.loads(pinned('frontier-20261028-q1-support-species0-cnf-check-receipt-v1.json','f1cb824dac1c117cd5041f5a268c6d3595c1453b4663701bd0501a09c204c26e'))
 if r0['result']!='PASS_EVERY_STEP_RUP_INCLUDING_FINAL_EMPTY' or s0['result']!='PASS_INDEPENDENT_SCAN_RUP_FINAL_EMPTY' or e0['result']!='PASS_INDEPENDENT_FULL_CNF_CLAUSE_MULTISET':raise ValueError('case0 receipt')
 if any(z['cnf_sha256']!=sha(c0) or z['proof_sha256']!=sha(p0) for z in (r0,s0)) or e0['formula_sha256']!=sha(c0):raise ValueError('case0 source/proof binding')
 if r0['counts']['rup_additions']!=s0['counts']['additions'] or len(p0.splitlines())!=r0['counts']['proof_steps'] or p0.splitlines()[-1]!=b'0':raise ValueError('case0 proof')
 rows.append({'species':0,'orientation':[0,1,0],'formula':cnf0,'formula_sha256':sha(c0),'proof':proof0,'proof_sha256':sha(p0),
              'formula_bytes':len(c0),'proof_bytes':len(p0),'rup_additions':r0['counts']['rup_additions'],
              'encoder_check_receipt':'frontier-20261028-q1-support-species0-cnf-check-receipt-v1.json',
              'fast_rup_receipt':'frontier-20261028-q1-support-species0-rup-receipt-v1.json',
              'scan_rup_receipt':'frontier-20261028-q1-support-species0-rup-scan-receipt-v1.json',
              'solver_console':'observed owner transcript; not separately retained', 'local_status':'DUAL_RUP_PASS'})
 for raw in allrec:
  sp,r,c,anchor=raw['case'];expected=[1,0,0] if sp==38 else [0,1,0]
  if [r,c,anchor]!=expected:raise ValueError('orientation mismatch')
  rb=pinned(raw['case_receipt'],raw['case_receipt_sha256']);rec=json.loads(rb)
  if rec['case']!=raw['case'] or rec['outcome']!='LOCAL_DUAL_RUP_PASS_PENDING_PARENT_REPLAY' or rec['independent_clause_multiset']!='PASS':raise ValueError('case outcome')
  solver=rec['solver']
  if solver['returncode']!=20 or solver['s_lines']!=['s UNSATISFIABLE'] or solver['stop'] is not None or solver['stderr']!='':raise ValueError('solver status')
  cb=pinned(rec['formula'],rec['formula_sha256']);pb=pinned(rec['proof'],rec['proof_sha256'])
  if len(cb)!=rec['formula_bytes'] or len(pb)!=rec['proof_bytes']:raise ValueError('artifact size')
  q=rec['rup'];z=rec['scan_rup'];lines=pb.splitlines()
  if q['original_clauses']!=rec['clauses'] or z['clauses']!=rec['clauses'] or q['rup_additions']!=z['additions'] or q['proof_steps']!=z['steps'] or q['proof_steps']!=len(lines) or not lines or lines[-1]!=b'0':raise ValueError('RUP receipt')
  rows.append({'species':sp,'orientation':[r,c,anchor],'formula':rec['formula'],'formula_sha256':rec['formula_sha256'],
               'proof':rec['proof'],'proof_sha256':rec['proof_sha256'],'formula_bytes':len(cb),'proof_bytes':len(pb),
               'rup_additions':q['rup_additions'],'case_receipt':raw['case_receipt'],'case_receipt_sha256':raw['case_receipt_sha256'],
               'local_status':'DUAL_RUP_PASS'})
 if [z['species'] for z in rows]!=list(range(39)):raise ValueError('final coverage')
 out={'result':'RETAINED_ARTIFACTS_MATCH_ALL_39_LOCAL_PROOF_RECEIPTS',
      'inventory_source_sha256':sha(pathlib.Path(__file__).read_bytes()),'observed_at':datetime.datetime.now().astimezone().isoformat(),
      'source_pins':PINS,'batch_receipts':[{k:v for k,v in x.items() if k!='records'} for x in batches],
      'species_count':len(rows),'formula_total_bytes':sum(x['formula_bytes'] for x in rows),
      'proof_total_bytes':sum(x['proof_bytes'] for x in rows),'rup_additions_total':sum(x['rup_additions'] for x in rows),
      'max_proof_bytes':max(x['proof_bytes'] for x in rows),'records':rows,
      'limits':'Metadata inventory only; local dual-RUP/case receipts are not a strict parent FIFO/drat-trim replay, mathematical peer review, source classification or novelty clearance.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
