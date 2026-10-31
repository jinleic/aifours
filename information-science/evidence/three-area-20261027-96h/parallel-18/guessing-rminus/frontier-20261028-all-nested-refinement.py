#!/usr/bin/env python3
"""Add all violated known-coordinate nested Shannon monotonicities lazily.

Unspecified entropy coordinates remain unassigned. Bounds from this LP are
numerical unless independently certified, and a partial point is not a full
source-LP or entropic witness.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from math import lcm
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('mono',ROOT/'frontier-20261028-source-monotone-refinement.py')
mono=module_from_spec(spec);spec.loader.exec_module(mono)
closure=mono.closure;probe=mono.probe;sparse=mono.sparse;cert=mono.cert
PRIOR=ROOT/'frontier-20261028-source-monotone-refinement-result.json'
EXPECTED='89137afa724b1444fca90c6c2b79a6270c419fa53f5b78031c04d7591a067ee2'
OUTPUT=ROOT/'frontier-20261028-all-nested-refinement-result.json'
POINT=ROOT/'frontier-20261028-all-nested-primal-frozen.json'
MAX_ROUNDS=20
MAX_WALL_S=120.0
MAX_ADDED=1200


def nested_scan(keys,values,existing,exact=False):
    h={frozenset(k):v for k,v in zip(keys,values)};h[frozenset()]=Fraction(0) if exact else 0.0
    candidates={};checked=0;tol=0 if exact else 1e-8
    for branch,labels in enumerate(closure.BRANCHES,1):
        n=len(labels);full=(1<<n)-1;allowed=frozenset(labels)
        lookup={}
        for key,value in h.items():
            if key<=allowed:
                mask=sum(1<<i for i,v in enumerate(labels) if v in key)
                lookup[mask]=value
        for small,val in lookup.items():
            rem=full^small;extra=rem
            while extra:
                large=small|extra
                if large in lookup:
                    checked+=1;delta=lookup[large]-val
                    if delta < -tol:
                        lesser=tuple(sorted(labels[i] for i in range(n) if small&(1<<i)))
                        greater=tuple(sorted(labels[i] for i in range(n) if large&(1<<i)))
                        terms={greater:1}
                        if lesser:terms[lesser]=-1
                        sig=closure.row_signature(terms,0.0,highspy.kHighsInf)
                        if sig not in existing:
                            meta={'kind':'known-nested-monotonicity','branch':branch,'smaller':lesser,'larger':greater}
                            old=candidates.get(sig)
                            if old is None or delta<old[0]:candidates[sig]=(delta,terms,meta)
                extra=(extra-1)&rem
    return checked,candidates


def main():
    started=time.monotonic();raw=PRIOR.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('PRIOR_HASH')
    prior=json.loads(raw);extras=prior['all_fn_cuts']
    data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text'])
    rows=sparse.build_constraints(source,extras)+closure.copy_rows()
    seen,immediate,_=mono.add_monotonicity(rows)
    for entry in prior['selected_CMI_rows']:
        terms={tuple(k):value for k,value in entry['terms']}
        sig=closure.row_signature(terms,0.0,highspy.kHighsInf)
        if sig not in seen:
            seen.add(sig);rows.append((terms,0.0,highspy.kHighsInf,entry['metadata']))
    added_nested=[];added_cmi=[];rounds=[];point=None;stop='round limit'
    seen_fn={(x['n'],x['A_mask'],x['B_mask'],x['C_mask'],x['D_mask'],x['condition_mask']) for x in extras}
    for r in range(MAX_ROUNDS):
        if time.monotonic()-started>MAX_WALL_S:stop='wall limit';break
        t=time.monotonic();status,keys,col,vals=probe.solve(rows)
        rec={'round':r,'rows':len(rows),'solver_status':status,'solve_elapsed_s':time.monotonic()-t}
        if vals is None:stop='LP not optimal';rounds.append(rec);break
        rec['objective_float_unverified']=float(vals[col[tuple(cert.BASE)]])
        chosen=None;attempts=[]
        for maxden in (1000,10000,100000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            bad=[v for v in bad if v['kind']!='objective']
            attempts.append({'max_denominator':maxden,'bad_count':len(bad),'first':bad[:2]})
            if not bad:chosen=x;break
        rec['rationalization']=attempts
        if chosen is not None:rec['exact_feasible_primal_objective']=str(chosen[col[tuple(cert.BASE)]])
        t=time.monotonic();nested_checked,nested=nested_scan(keys,vals,seen)
        cmi_checked,unknown,cmi=closure.scan_branch_cmi(keys,vals,seen)
        combined=dict(nested)
        for sig,item in cmi.items():
            if sig not in combined or item[0]<combined[sig][0]:combined[sig]=item
        ordered=sorted(combined.items(),key=lambda x:x[1][0])[:MAX_ADDED]
        rec.update({'nested_pairs_checked':nested_checked,'nested_violations':len(nested),
                    'branch_elemental_checked':cmi_checked,'elemental_unknown':unknown,
                    'elemental_violations':len(cmi),'cuts_added':len(ordered),
                    'scan_elapsed_s':time.monotonic()-t})
        for sig,(slack,terms,meta) in ordered:
            seen.add(sig);rows.append((terms,0.0,highspy.kHighsInf,meta))
            item={'terms':[[list(k),v] for k,v in sorted(terms.items())],'metadata':meta}
            (added_nested if meta['kind']=='known-nested-monotonicity' else added_cmi).append(item)
        if not ordered and chosen is not None:
            _,nested_exact=nested_scan(keys,chosen,seen,exact=True)
            if nested_exact:
                for sig,(slack,terms,meta) in nested_exact.items():
                    seen.add(sig);rows.append((terms,0.0,highspy.kHighsInf,meta))
                    added_nested.append({'terms':[[list(k),v] for k,v in sorted(terms.items())],'metadata':meta})
                rec['additional_exact_nested_cuts']=len(nested_exact)
            else:
                H=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
                scale=lcm(*(x.denominator for x in H));nums=[int(x*scale) for x in H]
                if max(map(abs,nums))>=10**8:stop='integer range';rounds.append(rec);break
                scan=probe.exhaustive_all_n(np.array(nums,dtype=np.int64));rec['all_n_scan']=scan
                extra=mono.add_fn(scan,rows,extras,seen_fn);rec['new_fn_cuts']=extra
                if scan['status']=='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
                    point={'coordinates':len(keys),'base_scale':scale,'exact_objective':str(chosen[col[tuple(cert.BASE)]]),
                           'primal_values':[{'entropy_variables':k,'value':str(chosen[i])} for i,k in enumerate(keys)],
                           'all_n_scan':scan}
                    stop='exact point passes all known nested rows, evaluable CMI and disjoint F_n';rounds.append(rec);break
                if not extra:stop='unable to add exact separator';rounds.append(rec);break
        if not ordered and chosen is None:stop='exact reconstruction failed';rounds.append(rec);break
        rounds.append(rec)
        with (ROOT/f'frontier-20261028-all-nested-round-{r}.json').open('x',encoding='utf-8') as stream:
            json.dump(rec,stream,indent=2);stream.write('\n')
    out={'prior_result_sha256':EXPECTED,'source_hashes':{k:info[1] for k,info in cert.FILES.items()},
         'immediate_monotonic_rows':immediate,'all_fn_cuts':extras,'added_nested_rows':added_nested,
         'added_elemental_CMI_rows':added_cmi,'rounds':rounds,'stop':stop,'elapsed_s':time.monotonic()-started,
         'limits':'Partial-coordinate numerical LP only. Exact points do not imply full-source extension or entropic realization; numerical upper changes need exact dual.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    if point is not None:
        point['source_result_sha256']=sha256(OUTPUT.read_bytes()).hexdigest()
        with POINT.open('x',encoding='utf-8') as stream:json.dump(point,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('all_fn_cuts','added_nested_rows','added_elemental_CMI_rows')},indent=2))
    print('nested_added',len(added_nested),'CMI_added',len(added_cmi),'point_saved',point is not None)


if __name__=='__main__':main()
