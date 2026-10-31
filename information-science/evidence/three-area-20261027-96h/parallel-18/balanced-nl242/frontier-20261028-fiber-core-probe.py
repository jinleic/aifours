#!/opt/homebrew/bin/python3
"""Recheck selected clauses of a captured Z3 unsat core; no proof certificate."""
import argparse
import json
import pathlib
import re
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--core',type=pathlib.Path,required=True)
    p.add_argument('--omit',action='append',default=[]);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    doc=json.loads(args.core.read_text(encoding='utf-8'));omitted=set(args.omit)
    clauses=[x for x in doc['core'] if x['name'] not in omitted]
    if any(x not in {r['name'] for r in doc['core']} for x in omitted):raise ValueError('unknown omitted name')
    text='\n'.join(x['sexpr'] for x in clauses)
    names=sorted(set(re.findall(r'\b(?:k_[+-]\d+|(?:even|odd)_[A-Za-z0-9_]+)\b',text)))
    smt='\n'.join('(declare-const '+x+' Int)' for x in names)+'\n'+'\n'.join('(assert '+x['sexpr']+')' for x in clauses)
    s=z3.Solver();s.set(timeout=10000);s.from_string(smt);result=s.check()
    receipt={'status':str(result),'omitted':sorted(omitted),'clauses':len(clauses),'variables':len(names),
             'scope':'captured solver core only; no independent proof'}
    if result==z3.unknown:receipt['reason_unknown']=s.reason_unknown()
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('omitted=',sorted(omitted),'status=',result,flush=True)


if __name__=='__main__':main()
