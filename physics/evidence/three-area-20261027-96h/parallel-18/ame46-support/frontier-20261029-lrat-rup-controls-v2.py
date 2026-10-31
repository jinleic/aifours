#!/usr/bin/env python3
"""Intended-reason controls of the independent positive-hint LRAT verifier."""
import argparse
import importlib.util
import json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser();ap.add_argument('checker',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rup_checker',a.checker);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    C=b'p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n';P=b'5 1 0 1 2 0\n6 2 0 5 3 0\n7 0 5 6 4 0\n'
    good=m.verify(C,P)
    repeated_delete=m.verify(C,b'5 1 0 1 2 0\n5 d 1 2 0\n6 2 0 5 3 0\n7 0 5 6 4 0\n')
    if repeated_delete['deleted_clauses']!=2:raise ValueError('standard deletion positive control')
    tests=[('bogus_empty',C,b'5 0 1 0\n','RUP hint not unit or conflicting'),
      ('truncated_cnf',b'p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n',P,'CNF clause count mismatch'),
      ('truncated_proof',C,b'5 1 0 1 2 0\n6 2 0 5 3 0\n','no verified empty clause'),
      ('wrong_formula',b'p cnf 2 4\n1 2 0\n1 -2 0\n1 2 0\n1 -2 0\n',P,'RUP hint already satisfied'),
      ('negative_hint',C,b'5 1 0 -1 2 0\n','unsupported nonpositive RUP hint'),
      ('deleted_hint',C,b'5 d 1 0\n6 1 0 1 2 0\n','unknown or deleted hint clause'),
      ('out_of_range',C,b'5 3 0 1 2 0\n','proof literal out of range'),
      ('nonmonotonic_ID',C,b'4 1 0 1 2 0\n','proof addition IDs not increasing')]
    report=[]
    for name,cnf,proof,reason in tests:
        try:m.verify(cnf,proof)
        except m.CertificateError as exc:
            if str(exc)!=reason:raise ValueError(f'{name}: wrong rejection {exc}; expected {reason}')
            report.append({'name':name,'rejection':str(exc)})
        else:raise ValueError(f'{name}: mutation accepted')
    # SAT formula has no proof, reject even if input itself is satisfiable.
    try:m.verify(b'p cnf 1 1\n1 0\n',b'2 0 1 0\n')
    except m.CertificateError as exc:
        if str(exc)!='RUP hints ended without conflict':raise
        report.append({'name':'SAT_formula_bogus_empty','rejection':str(exc)})
    else:raise ValueError('SAT formula accepted')
    result={'valid_small_proof':good,'repeated_timestamp_deletion_positive':repeated_delete,'intended_mutation_controls':report,
      'scope':'Exact checker controls, not a certificate of the research encoder or a mathematical exclusion.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
