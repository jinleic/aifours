#!/usr/bin/env python3
"""Bind 56 disjoint exact-CNF RUP certificates for N47/r3444; no solver rerun."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    batch=a.root/'sat-20261029/n47-3444-certificate-batch-v1.json';B=json.loads(batch.read_text())
    if [r['case'] for r in B['cases']]!=list(range(56)):raise ValueError('batch coverage')
    records=[];cb=pb=0
    for item in B['cases']:
        case=item['case'];base=a.root/'sat-20261029'/f'n47-3444-case{case:02d}'
        cnf=Path(str(base)+'.cnf');proof=Path(str(base)+'.lrat');receipt=Path(str(base)+'.rup-check-v2.json');log=Path(str(base)+'.cadical.log')
        r=json.loads(receipt.read_text())
        if item['solver_rc']!=20 or item['solver_status_lines']!=['s UNSATISFIABLE'] or item['checked_status']!='VERIFIED':raise ValueError('not exact UNSAT result')
        if not r['verified_empty_clause_IDs'] or not r['all_lines_parsed'] or r['status']!='VERIFIED_TEXT_LRAT_RUP':raise ValueError('incomplete proof replay')
        if (sha(cnf),cnf.stat().st_size,sha(proof),proof.stat().st_size)!=(r['cnf_sha256'],r['cnf_bytes'],r['proof_sha256'],r['proof_bytes']):raise ValueError('data binding mismatch')
        if sha(log)!=item['solver_log_sha256'] or sha(receipt)!=item['checker_receipt_sha256']:raise ValueError('receipt/log binding mismatch')
        if r['imported_base_encoder_sha256']!=B['imported_base_encoder_sha256']:raise ValueError('import binding mismatch')
        cb+=r['cnf_bytes'];pb+=r['proof_bytes']
        records.append({'case':case,'types':item['types'],'cnf':str(cnf.relative_to(a.root)),'cnf_sha256':r['cnf_sha256'],'cnf_bytes':r['cnf_bytes'],
          'proof':str(proof.relative_to(a.root)),'proof_sha256':r['proof_sha256'],'proof_bytes':r['proof_bytes'],
          'checker_receipt':str(receipt.relative_to(a.root)),'checker_receipt_sha256':sha(receipt),
          'added_clauses':r['added_clauses'],'deleted_clauses':r['deleted_clauses'],'verified_empty_clause_IDs':r['verified_empty_clause_IDs']})
    names=['frontier-20261029-n47-3444-support-cnf-v1.py','frontier-20261029-n47-heavy-support-cnf-v1.py',
      'frontier-20261029-lrat-rup-check-v2.py','frontier-20261029-lrat-rup-controls-v2.py',
      'sat-20261029/lrat-rup-controls-v2.json','frontier-20261029-n47-cnf-gadget-controls-v1.py','sat-20261029/n47-cnf-gadget-controls-v1.json',
      'frontier-20261029-n47-3444-heavy-support-z3-v1.py','frontier-20261029-n47-3444-heavy-support-z3-v1.json']
    result={'case_count':56,'cases':records,'cnf_bytes_total':cb,'proof_bytes_total':pb,
      'batch_receipt_sha256':sha(batch),'sources_and_controls':[{'path':n,'sha256':sha(a.root/n)} for n in names],
      'scope':'Exact-CNF RUP coverage only; mathematical normal form, encoder and checker require independent review.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'case_count':56,'cnf_bytes_total':cb,'proof_bytes_total':pb,'manifest_sha256':sha(a.out),'scope':result['scope']},indent=2))


if __name__=='__main__':main()
