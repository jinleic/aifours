#!/usr/bin/env python3
"""Bind all 15 proofs forming the complete q2 index-17 support split."""
import argparse,datetime,hashlib,itertools,json,pathlib
H=pathlib.Path(__file__).parent
P={'frontier-20261028-q2-cardinality-residual-batch-receipt-v1.json':'f691d447cfd43d29986411e4c1343721132eb790a1effddb97b9029c36ea17c4',
   'frontier-20261028-q2-singleton-residual-batch-receipt-v1.json':'bcde891a4a7336044e420e8dda0e61026cc5167c4a6af3df37e09c97f0be0da8',
   'frontier-20261028-q2-singleton34-fifo-replay-receipt-v1.json':'7e916829d492a1da4956d82759df46cc1ef2ed1ee60c97ecd02c2f8a4ba109d2',
   'frontier-20261028-q2-nonmax17-singleton34-cnf-check-receipt-v1.json':'2fe61b450c93be6b59c23d0826a2eb14958a52a3b7d2a7177da6b98f66e42c9e',
   'frontier-20261028-q2-nonmax17-singleton34-v1.cnf':'5de59996368c014482310ea4a4e35848720b0df9d86258c320bcbba7520d4203',
   'frontier-20261028-q2-nonmax17-singleton34-proof-v1.drup':'6c0e99f879af6fc1c0147f7c6e3c712ac6c30c98907ab4f2618b2a43bca0f38c',
   'frontier-20261028-source-wanless-nonmax2-pair17-v1.txt':'14471ce215e3c97e1fcaa4109bbd58dca4438adc5039e1d8df11d5f46d029415'}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(name,pin=None):
 b=(H/name).read_bytes()
 if pin and sha(b)!=pin:raise ValueError('pin '+name)
 return b

def passrec(r):
 if r['outcome']!='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW' or r['independent_clause_multiset']!='PASS':raise ValueError('case outcome')
 s=r['solver'];z=r['replay']
 if s['returncode']!=20 or s['status_lines']!=['s UNSATISFIABLE'] or s['stop'] is not None or s['stderr'] or not z['strict_pass'] or not z['transport_exact'] or z['status_lines']!=['s VERIFIED'] or z['returncode']!=0:raise ValueError('process status')
 if z['checker_reported_proof_bytes']!=z['proof_feed']['bytes'] or z['cnf_fifo_remaining_bytes']!=0 or z['cnf_feed']['sha256']!=r['formula_sha256']:raise ValueError('transport')
 cb=get(r['formula'],r['formula_sha256']);pb=get(r['proof'],r['proof_sha256'])
 if len(cb)!=r['formula_bytes'] or len(pb)!=r['proof_bytes'] or pb.splitlines()[-1]!=b'0':raise ValueError('retained bytes')
 raw=get(r['case_receipt'],r['case_receipt_sha256']);saved=json.loads(raw)
 if saved['outcome']!=r['outcome'] or saved['formula_sha256']!=r['formula_sha256']:raise ValueError('case receipt')
 return {'formula':r['formula'],'formula_sha256':r['formula_sha256'],'proof':r['proof'],'proof_sha256':r['proof_sha256'],
         'case_receipt':r['case_receipt'],'case_receipt_sha256':r['case_receipt_sha256'],'binary_bytes':z['proof_feed']['bytes'],
         'ascii_steps':r['ascii_steps'],'outcome':r['outcome']}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 for f,h in P.items():get(f,h)
 big=json.loads(get('frontier-20261028-q2-cardinality-residual-batch-receipt-v1.json'))
 small=json.loads(get('frontier-20261028-q2-singleton-residual-batch-receipt-v1.json'))
 if [r['support_sizes'] for r in big['records']]!=[[1,2],[1,3],[1,4],[2,2],[2,3]]:raise ValueError('five cardinality cases')
 expected=[list(z) for z in itertools.combinations([3,4,5,6,7],2) if z!=(3,4)]
 if [r['axes'] for r in small['records']]!=expected:raise ValueError('nine singleton cases')
 card=[{'support_sizes':r['support_sizes'],**passrec(r)} for r in big['records']]
 single=[{'axes':r['axes'],**passrec(r)} for r in small['records']]
 pilot=json.loads(get('frontier-20261028-q2-singleton34-fifo-replay-receipt-v1.json'))
 audit=json.loads(get('frontier-20261028-q2-nonmax17-singleton34-cnf-check-receipt-v1.json'))
 if pilot['result']!='OWNER_LOCAL_MEASURED_FIFO_PASS' or not pilot['actual']['strict_pass'] or audit['result']!='PASS_INDEPENDENT_SINGLETON_PAIR_CNF' or audit['axes']!=[3,4]:raise ValueError('pilot')
 cnf0='frontier-20261028-q2-nonmax17-singleton34-v1.cnf';proof0='frontier-20261028-q2-nonmax17-singleton34-proof-v1.drup'
 if pilot['cnf_sha256']!=P[cnf0] or pilot['ascii_proof_sha256']!=P[proof0] or audit['formula_sha256']!=P[cnf0] or get(proof0).splitlines()[-1]!=b'0':raise ValueError('pilot binding')
 single.insert(0,{'axes':[3,4],'formula':cnf0,'formula_sha256':P[cnf0],'proof':proof0,'proof_sha256':P[proof0],
                  'replay_receipt':'frontier-20261028-q2-singleton34-fifo-replay-receipt-v1.json','replay_receipt_sha256':P['frontier-20261028-q2-singleton34-fifo-replay-receipt-v1.json'],
                  'binary_bytes':pilot['binary_proof_bytes'],'ascii_steps':pilot['ascii_steps'],'outcome':'OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW'})
 if [r['axes'] for r in single]!=[list(z) for z in itertools.combinations([3,4,5,6,7],2)]:raise ValueError('full singleton coverage')
 out={'result':'INDEX17_ALL_15_SPLIT_PROOF_RECEIPTS_BOUND',
      'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'observed_at':datetime.datetime.now().astimezone().isoformat(),
      'input_pins':P,'five_non_singleton_size_cases':card,'ten_singleton_coordinate_cases':single,
      'proof_cases':len(card)+len(single),'binary_proof_bytes_total':sum(r['binary_bytes'] for r in card+single),
      'ascii_proof_steps_total':sum(r['ascii_steps'] for r in card+single),
      'limits':'Metadata/coverage inventory only; owner-local checks are not parent-independent replay, physical/symmetry review or source classification.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('five_non_singleton_size_cases','ten_singleton_coordinate_cases')},indent=2))
if __name__=='__main__':main()
