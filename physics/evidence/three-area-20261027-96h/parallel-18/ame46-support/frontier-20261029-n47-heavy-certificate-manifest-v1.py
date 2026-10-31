#!/usr/bin/env python3
"""Bind all thirteen N47/r4444 exact-CNF RUP certificates and controls.

This is a hash/coverage manifest; it does not re-run a solver or checker.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    records=[];totalcnf=totalproof=0
    for case in range(13):
        prefix=a.root/'sat-20261029'/f'n47-heavy-case{case:02d}'
        cnf=Path(str(prefix)+'.cnf');proof=Path(str(prefix)+'.lrat');receipt=Path(str(prefix)+'.rup-check-v2.json');r=json.loads(receipt.read_text())
        if r['status']!='VERIFIED_TEXT_LRAT_RUP' or not r['verified_empty_clause_IDs'] or not r['all_lines_parsed']:raise ValueError(f'incomplete certificate {case}')
        if (sha(cnf),cnf.stat().st_size,sha(proof),proof.stat().st_size)!=(r['cnf_sha256'],r['cnf_bytes'],r['proof_sha256'],r['proof_bytes']):raise ValueError(f'certificate binding mismatch {case}')
        totalcnf+=r['cnf_bytes'];totalproof+=r['proof_bytes']
        records.append({'case':case,'cnf':str(cnf.relative_to(a.root)),'cnf_sha256':r['cnf_sha256'],'cnf_bytes':r['cnf_bytes'],
          'proof':str(proof.relative_to(a.root)),'proof_sha256':r['proof_sha256'],'proof_bytes':r['proof_bytes'],
          'checker_receipt':str(receipt.relative_to(a.root)),'checker_receipt_sha256':sha(receipt),
          'added_clauses':r['added_clauses'],'deleted_clauses':r['deleted_clauses'],
          'verified_empty_clause_IDs':r['verified_empty_clause_IDs']})
    names=['frontier-20261029-n47-heavy-support-cnf-v1.py','frontier-20261029-lrat-rup-check-v1.py','frontier-20261029-lrat-rup-check-v2.py',
      'frontier-20261029-lrat-rup-controls-v2.py','frontier-20261029-n47-cnf-gadget-controls-v1.py',
      'sat-20261029/lrat-rup-controls-v2.json','sat-20261029/n47-cnf-gadget-controls-v1.json',
      'frontier-20261029-n47-4444-heavy-support-z3-v1.py','frontier-20261029-n47-4444-heavy-support-z3-v1.json']
    result={'cases':records,'case_count':13,'cnf_bytes_total':totalcnf,'proof_bytes_total':totalproof,
      'sources_and_controls':[{'path':n,'sha256':sha(a.root/n)} for n in names],
      'scope':'Exact pinned-CNF RUP proof coverage only; mathematical reduction, encoder soundness and checker correctness are separate review obligations.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'case_count':13,'cnf_bytes_total':totalcnf,'proof_bytes_total':totalproof,'manifest_sha256':sha(a.out),'scope':result['scope']},indent=2))


if __name__=='__main__':main()
