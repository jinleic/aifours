#!/usr/bin/env python3
"""Bind prior 34 local proofs and four separately closed residual net cases."""
import argparse,datetime,hashlib,json,pathlib
H=pathlib.Path(__file__).parent
P={'frontier-20261028-q2-nonmax-proof-inventory-receipt-v1.json':'741b579a37ac054dedba903f030af1e65f35b5ec565875308cb1652c2872206f',
   'frontier-20261028-q2-product15-fifo-replay-receipt-v1.json':'dd4a848bdc6e06f9cc241d42dd9391d3760448c2004682ae26b7718fd915e813',
   'frontier-20261028-q2-nonmax15-product-cnf-check-receipt-v1.json':'2ce09c0edf3f6319d421699c1c631da7567dd3f61e8bdfae5b1042f9277d63ae',
   'frontier-20261028-q2-nonmax16-product-v1-receipt.json':'8e01a3c714105c0ee626d3057a0a3cdd56e20893914ed519185baa5e93cddbe0',
   'frontier-20261028-q2-sym35-fifo-replay-receipt-v1.json':'bac70ef962713eeacfbdf7d953cdc1172fd21c44ce51d2ec598ff4f2f9d2e433',
   'frontier-20261028-q2-nonmax35-symmetry-cnf-check-receipt-v1.json':'0e93b96460042e3b9c070af5eb99789772ffa036c1c9c8493d0a800c70d15853',
   'frontier-20261028-q2-index17-split-inventory-receipt-v1.json':'ebf5d077684b8b6f761f4c0a5931d917d7903632618120398790ce43c054195b',
   'frontier-20261028-nonmax2-net-extract-receipt-v1.json':'cda00277e356426194cc2051d7e92b32ad6f639f017f621ef0b69e9d0fbcdf8d'}
def sha(b):return hashlib.sha256(b).hexdigest()
def get(name,pin=None):
 b=(H/name).read_bytes()
 if pin and sha(b)!=pin:raise ValueError('pin '+name)
 return b

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 for name,pin in P.items():get(name,pin)
 old=json.loads(get('frontier-20261028-q2-nonmax-proof-inventory-receipt-v1.json'));extract=json.loads(get('frontier-20261028-nonmax2-net-extract-receipt-v1.json'))
 if old['unresolved_indices']!=[15,16,17,35] or len(old['records'])!=38:raise ValueError('old scope')
 pairs={x['index']:x for x in extract['pairs']};resolved={}
 for i,repfile,audfile in [(15,'frontier-20261028-q2-product15-fifo-replay-receipt-v1.json','frontier-20261028-q2-nonmax15-product-cnf-check-receipt-v1.json'),
                           (35,'frontier-20261028-q2-sym35-fifo-replay-receipt-v1.json','frontier-20261028-q2-nonmax35-symmetry-cnf-check-receipt-v1.json')]:
  r=json.loads(get(repfile));u=json.loads(get(audfile))
  if r['result']!='OWNER_LOCAL_MEASURED_FIFO_PASS' or not r['actual']['strict_pass'] or u['formula_sha256']!=r['cnf_sha256'] or u['pair_sha256']!=pairs[i]['sha256']:raise ValueError('refined case')
  names=('frontier-20261028-q2-nonmax15-product-v1.cnf','frontier-20261028-q2-nonmax15-product-proof-v1.drup') if i==15 else ('frontier-20261028-q2-nonmax35-symmetry-v1.cnf','frontier-20261028-q2-nonmax35-symmetry-proof-v1.drup')
  get(names[0],r['cnf_sha256']);get(names[1],r['ascii_proof_sha256']);get(pairs[i]['file'],pairs[i]['sha256'])
  resolved[i]={'method':'product' if i==15 else 'product+matching+member-symmetry','replay_receipt':repfile,'replay_receipt_sha256':P[repfile],
               'audit_receipt':audfile,'audit_receipt_sha256':P[audfile],'formula_sha256':r['cnf_sha256'],'ascii_proof_sha256':r['ascii_proof_sha256']}
 r=json.loads(get('frontier-20261028-q2-nonmax16-product-v1-receipt.json'))
 if r['index']!=16 or r['pair']!=pairs[16] or r['outcome']!='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW' or not r['replay']['strict_pass'] or r['independent_clause_multiset']!='PASS':raise ValueError('case16')
 get(r['formula'],r['formula_sha256']);get(r['proof'],r['proof_sha256'])
 resolved[16]={'method':'product','case_receipt':'frontier-20261028-q2-nonmax16-product-v1-receipt.json','case_receipt_sha256':P['frontier-20261028-q2-nonmax16-product-v1-receipt.json'],
               'formula_sha256':r['formula_sha256'],'ascii_proof_sha256':r['proof_sha256']}
 r=json.loads(get('frontier-20261028-q2-index17-split-inventory-receipt-v1.json'))
 if r['result']!='INDEX17_ALL_15_SPLIT_PROOF_RECEIPTS_BOUND' or r['proof_cases']!=15:raise ValueError('case17 split')
 resolved[17]={'method':'matching+six-cardinality-cases+ten-singleton-subcases','split_inventory':'frontier-20261028-q2-index17-split-inventory-receipt-v1.json','split_inventory_sha256':P['frontier-20261028-q2-index17-split-inventory-receipt-v1.json']}
 rows=[]
 for r in old['records']:
  i=r['index']
  if i in resolved:rows.append({'index':i,'earlier_outcome':r['outcome'],'new_evidence':resolved[i]})
  else:
   if r['outcome']!='OWNER_MEASURED_FIFO_PASS_PENDING_PARENT_REVIEW':raise ValueError('other case unresolved')
   rows.append({'index':i,'earlier_outcome':r['outcome'],'new_evidence':None})
 if [r['index'] for r in rows]!=list(range(38)):raise ValueError('coverage')
 out={'result':'ALL_38_PINNED_NONMAX_PAIR_INDICES_HAVE_OWNER_LOCAL_PROOF_EVIDENCE',
      'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'observed_at':datetime.datetime.now().astimezone().isoformat(),
      'input_pins':P,'source_indices':38,'baseline_pass':34,'previous_unknowns_resolved_by_new_formulas':[15,16,17,35],
      'records':rows,'limits':'Metadata composition only; all physical/encoding/split proofs and independently owned parent replays remain review obligations. No claim about unexamined maximal pairs or catalogue completeness.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
