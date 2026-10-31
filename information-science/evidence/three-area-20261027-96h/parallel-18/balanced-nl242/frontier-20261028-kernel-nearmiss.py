#!/opt/homebrew/bin/python3
"""Run the SAME kernel pairing model with only crossing changed to 72.

This is an intentionally non-Boolean near-miss, not a target or UNSAT proof.
"""
import argparse
import importlib.util
import json
import pathlib
import sys
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    source=pathlib.Path(__file__).with_name('frontier-20261028-fourzero-kernel-pairing.py')
    spec=importlib.util.spec_from_file_location('kernel_model',source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    Original=z3.Solver;instances=[]
    class NearMiss:
        def __init__(self):self.s=Original();self.index=0;self.replaced=0;instances.append(self)
        def set(self,*a,**kw):return self.s.set(*a,**kw)
        def add(self,*conditions):
            for condition in conditions:
                if self.index==91:
                    if not z3.is_or(condition) or len(condition.children())!=3:raise ValueError('expected crossing constraint changed')
                    branch=condition.children()[0]
                    if not z3.is_eq(branch) or branch.arg(1).as_long()!=0:raise ValueError('unexpected crossing expression')
                    self.s.add(branch.arg(0)==72);self.replaced+=1
                else:self.s.add(condition)
                self.index+=1
        def check(self):return self.s.check()
        def reason_unknown(self):return self.s.reason_unknown()
        def model(self):return self.s.model()
    z3.Solver=NearMiss;oldargv=sys.argv;sys.argv=[str(source),'--timeout-ms',str(args.timeout_ms),'--output',str(args.output)]
    try:mod.main()
    finally:z3.Solver=Original;sys.argv=oldargv
    if len(instances)!=1 or instances[0].replaced!=1:raise ValueError('crossing constraint not uniquely replaced')
    data=json.loads(args.output.read_text(encoding='utf-8'))
    if data['status']=='sat' and data['kernel_P_crossing_pairs']!=72:raise AssertionError('near-miss crossing')
    print('only-crossing-replaced=72 status=',data['status'],flush=True)


if __name__=='__main__':main()
