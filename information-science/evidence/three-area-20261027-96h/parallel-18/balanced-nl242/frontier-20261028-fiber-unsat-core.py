#!/opt/homebrew/bin/python3
"""Extract a replayable unsat core from the explicit fiber relaxation.

A solver core is not itself an independent proof or a four-zero exclusion.
"""
import argparse
import importlib.util
import json
import pathlib
import sys
import z3


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--core',type=pathlib.Path,required=True);p.add_argument('--receipt',type=pathlib.Path,required=True);args=p.parse_args()
    if args.core.exists() or args.receipt.exists() or not 1<=args.timeout_ms<=60000:raise ValueError('invalid bounds/output')
    source=pathlib.Path(__file__).with_name('frontier-20261028-four-zero-fiber-energy.py')
    spec=importlib.util.spec_from_file_location('fiber_model',source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    Original=z3.Solver
    class Tracked:
        def __init__(self):self.s=Original();self.items={};self.counter=0
        def set(self,*a,**kw):return self.s.set(*a,**kw)
        def add(self,*conditions):
            for condition in conditions:
                key='tracked_'+str(self.counter);self.counter+=1;self.items[key]=condition
                self.s.assert_and_track(condition,z3.Bool(key))
        def check(self):
            verdict=self.s.check()
            if verdict==z3.unsat:
                core=[str(v) for v in self.s.unsat_core()]
                result={'status':str(verdict),'constraints_total':self.counter,'core_size':len(core),
                        'core':[{'name':name,'sexpr':self.items[name].sexpr()} for name in core],
                        'warning':'Z3 core only; no independently checked UNSAT proof'}
                with args.core.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
            return verdict
        def reason_unknown(self):return self.s.reason_unknown()
        def model(self):return self.s.model()
    z3.Solver=Tracked
    oldargv=sys.argv;sys.argv=[str(source),'--lambda-mode','0','--qrad-mode','0','--timeout-ms',str(args.timeout_ms),'--output',str(args.receipt)]
    try:mod.main()
    finally:z3.Solver=Original;sys.argv=oldargv
    if not args.core.exists():print('no core produced: unknown or SAT',flush=True)


if __name__=='__main__':main()
