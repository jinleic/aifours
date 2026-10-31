#!/usr/bin/env python3
"""Independently replay a complete fixed-row actual quotient case."""
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser()
    for n in ('a','b','r','s'):ap.add_argument('--'+n,type=int,required=True)
    args=ap.parse_args();a,b,r,s=args.a,args.b,args.r,args.s
    inp=ROOT/f'frontier-20261028-level5-fixed-{a}{b}-r{r}-s{s}-v1.json'
    out=ROOT/f'frontier-20261028-level5-fixed-{a}{b}-r{r}-s{s}-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    P=json.loads(inp.read_text());case=P['case']
    assert case['status'] in ('ZERO_SOURCE','ZERO_HORIZONTAL_KERNEL','CERTIFIED_ONE_SIGN')
    result=ind.replay(tuple(P['degree']),case)
    result.update({'degree':P['degree'],'method':'independent whole ideal/source/target, tree-Jacobi, rational Gaussian',
                   'fixed_pair_only':True,'not_formal_or_external_model_review':True})
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',P['degree'],'r,s',r,s,'source',case['source_dim'],'horizontal',case['horizontal_kernel_dim'],result['status'],out.name,flush=True)

if __name__=='__main__':main()
