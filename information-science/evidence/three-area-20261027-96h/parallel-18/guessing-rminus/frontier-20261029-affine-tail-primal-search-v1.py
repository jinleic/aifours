#!/usr/bin/env python3
"""PRIMAL WITNESS SEARCH ONLY; contains ARTIFICIAL non-universal equalities.
Usage: python3 script.py OUT.json PRIOR.json PRIOR_SHA SPECS.json SPECS_SHA
Builds the specialized exchangeable-block model, fixes 389*h(V)=2603, and
requires every ordinary-base subset to have the same final copy-count
increment inside each exchangeable branch. These restrictions are used ONLY
to seek a finite all-orders primal witness; they MUST NOT be used as valid
entropy rows in any upper-bound certificate. Proposes a crossover point and
accepts a rational grid only after exact integer checks of EVERY model row.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
s=spec_from_file_location('ec',ROOT/'frontier-20261029-exchangeable-copy-lp-v1.py');ec=module_from_spec(s);s.loader.exec_module(ec)

def main():
    t=time.monotonic();pr=(ROOT/sys.argv[2]).read_bytes();sr=(ROOT/sys.argv[4]).read_bytes()
    if sha256(pr).hexdigest()!=sys.argv[3] or sha256(sr).hexdigest()!=sys.argv[5]:raise ValueError('HASH')
    res=json.loads(pr);specs=json.loads(sr)['branches'];M=ec.build(res,specs)
    for a,sp in enumerate(specs):
        k=sp['copies'];b=12 if sp.get('tail',False) else 11;tag=f'e{a}'
        def key(m,r):
            if m==0 and r==0:return None
            return ('o',m) if r==0 and m<1024 else (tag,m,r)
        for u in range(1,1<<b):
            M.add([(key(u,k),1),(key(u,k-1),-1),(key(0,k),-1),(key(0,k-1),1)],0,0,('PRIMAL_ONLY_COMMON_INCREMENT',a,u))
    M.add([(('o',1023),389)],2603,2603,('PRIMAL_ONLY_TARGET',))
    print('PRIMAL ONLY rows',len(M.rows),'columns',len(M.col),flush=True)
    h,status,obj,x,dt=ec.cp.solve(M)
    report={'kind':'PRIMAL_ONLY_ARTIFICIAL_RESTRICTIONS_NOT_UPPER_BOUND','prior_sha256':sys.argv[3],'specs_sha256':sys.argv[5],
      'exchangeable_copies':specs,'extra_single_copies':res['extra_single_copies'],'cuts':res['cuts'],'status_float':status,
      'objective_float':obj,'rows':len(M.rows),'columns':len(M.col),'solve_s':dt,'target':'2603/389','exact_grid_found':False}
    if status=='Optimal':
        failures=[]
        for factor in (1,2,3,4,6,8,12,24,48,96,192,384,768):
            D=389*factor;nums=[int(round(float(v)*D)) for v in x];bad=None
            for i,row in enumerate(M.rows):
                val=sum(int(c)*nums[j] for j,c in row.items())
                if M.lo[i]!=-ec.cp.INF and val<int(M.lo[i])*D:bad=i;break
                if M.hi[i]!=ec.cp.INF and val>int(M.hi[i])*D:bad=i;break
            if bad is None:
                report.update({'exact_grid_found':True,'common_denominator':D,'exact_profile':{repr(key):nums[j] for key,j in M.col.items()},
                    'exact_model_row_check':'All coefficients and every finite bound checked as Python integers; no float acceptance test.'});break
            failures.append({'denominator':D,'first_failing_row':bad,'row_kind':M.meta[bad][0]})
        report['grid_trials']=failures
        if not report['exact_grid_found']:
            report['float_profile_not_a_witness']={repr(key):float(x[j]) for key,j in M.col.items()}
    report['elapsed_s']=time.monotonic()-t
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f);f.write('\n')
    print({k:v for k,v in report.items() if k not in ('exact_profile','float_profile_not_a_witness','cuts','grid_trials')},flush=True)
if __name__=='__main__':main()
