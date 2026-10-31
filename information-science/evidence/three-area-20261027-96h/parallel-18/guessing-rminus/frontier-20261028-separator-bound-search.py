#!/usr/bin/env python3
"""Add an exact verified one-copy information inequality to the R-minus core.

Numerical LP objectives are proposals, never exact upper proofs. All partial
points retain missing coordinates; no entropic realization is asserted.
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
spec=spec_from_file_location('nested',ROOT/'frontier-20261028-all-nested-refinement.py')
nested=module_from_spec(spec);spec.loader.exec_module(nested)
mono=nested.mono;closure=nested.closure;probe=nested.probe;sparse=nested.sparse;cert=nested.cert
PRIOR=ROOT/'frontier-20261028-all-nested-refinement-result.json'
PRIOR_SHA='0e99b6a1dd8158564e7330fd16807d2541601dc57afa7d321890850e0b5c988a'
MONO=ROOT/'frontier-20261028-source-monotone-refinement-result.json'
MONO_SHA='89137afa724b1444fca90c6c2b79a6270c419fa53f5b78031c04d7591a067ee2'
SEP=ROOT/'frontier-20261028-branch1-cut-independent-result.json'
SEP_SHA='1597bb44bea62b842c65a973ec08a4b8867af1a92a979225458e280464f3e915'
OUTPUT=ROOT/'frontier-20261028-separator-bound-search-result.json'
POINT=ROOT/'frontier-20261028-separator-bound-primal.json'
MAX_ROUNDS=15
MAX_WALL_S=100.0
MAX_ADDED=1000


def load(path,digest):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=digest:raise ValueError(('HASH',str(path)))
    return json.loads(raw)


def add_rows(rows,seen,entries):
    for entry in entries:
        terms={tuple(k):v for k,v in entry['terms']}
        signature=closure.row_signature(terms,0.0,highspy.kHighsInf)
        if signature not in seen:
            seen.add(signature);rows.append((terms,0.0,highspy.kHighsInf,entry['metadata']))


def main():
    started=time.monotonic();old=load(PRIOR,PRIOR_SHA);previous=load(MONO,MONO_SHA);sep=load(SEP,SEP_SHA)
    data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text']);extras=old['all_fn_cuts']
    rows=sparse.build_constraints(source,extras)+closure.copy_rows()
    seen,immediate,_=mono.add_monotonicity(rows)
    add_rows(rows,seen,previous['selected_CMI_rows'])
    add_rows(rows,seen,old['added_nested_rows']);add_rows(rows,seen,old['added_elemental_CMI_rows'])
    terms={tuple(sparse.sets_from_mask(m)):int(Fraction(c)) for m,c in sep['verdict']['normalized_base_terms']}
    signature=closure.row_signature(terms,0.0,highspy.kHighsInf)
    if signature not in seen:
        seen.add(signature);rows.append((terms,0.0,highspy.kHighsInf,{'kind':'verified-one-copy-separator'}))
    seen_fn={(x['n'],x['A_mask'],x['B_mask'],x['C_mask'],x['D_mask'],x['condition_mask']) for x in extras}
    rounds=[];chosen_final=None;newrows=[];stop='round limit'
    for r in range(MAX_ROUNDS):
        if time.monotonic()-started>MAX_WALL_S:stop='wall limit';break
        t=time.monotonic();status,keys,col,vals=probe.solve(rows)
        rec={'round':r,'rows':len(rows),'status':status,'solve_elapsed_s':time.monotonic()-t}
        if vals is None:stop='LP not optimal';rounds.append(rec);break
        rec['objective_float_unverified']=float(vals[col[tuple(cert.BASE)]])
        chosen=None;attempts=[]
        for maxden in (1000,10000,100000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            bad=[x for x in bad if x['kind']!='objective']
            attempts.append({'max_denominator':maxden,'bad_count':len(bad),'first':bad[:2]})
            if not bad:chosen=x;break
        rec['rationalization']=attempts
        if chosen is not None:rec['exact_feasible_primal_objective']=str(chosen[col[tuple(cert.BASE)]])
        t=time.monotonic();nested_count,nest=nested.nested_scan(keys,vals,seen)
        cmi_count,unknown,cmi=closure.scan_branch_cmi(keys,vals,seen)
        merged=dict(nest)
        for sig,item in cmi.items():
            if sig not in merged or item[0]<merged[sig][0]:merged[sig]=item
        selected=sorted(merged.items(),key=lambda x:x[1][0])[:MAX_ADDED]
        rec.update({'nested_pairs_checked':nested_count,'nested_violations':len(nest),
                    'branch_elemental_checked':cmi_count,'elemental_unknown':unknown,
                    'elemental_violations':len(cmi),'cuts_added':len(selected),
                    'scan_elapsed_s':time.monotonic()-t})
        for sig,(slack,row,meta) in selected:
            seen.add(sig);rows.append((row,0.0,highspy.kHighsInf,meta))
            newrows.append({'terms':[[list(k),v] for k,v in sorted(row.items())],'metadata':meta})
        if not selected and chosen is not None:
            _,exact_nested=nested.nested_scan(keys,chosen,seen,exact=True)
            if exact_nested:
                for sig,(slack,row,meta) in exact_nested.items():
                    seen.add(sig);rows.append((row,0.0,highspy.kHighsInf,meta))
                    newrows.append({'terms':[[list(k),v] for k,v in sorted(row.items())],'metadata':meta})
                rec['exact_nested_cuts_added']=len(exact_nested)
            else:
                H=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
                scale=lcm(*(x.denominator for x in H));ints=[int(x*scale) for x in H]
                if max(map(abs,ints))>=10**8:stop='integer range';rounds.append(rec);break
                scan=probe.exhaustive_all_n(np.array(ints,dtype=np.int64));rec['all_n_scan']=scan
                additional=mono.add_fn(scan,rows,extras,seen_fn);rec['new_fn_cuts']=additional
                if scan['status']=='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
                    chosen_final={'exact_objective':str(chosen[col[tuple(cert.BASE)]]),'base_scale':scale,
                                  'coordinates':len(keys),'primal_values':[{'entropy_variables':k,'value':str(chosen[i])} for i,k in enumerate(keys)],
                                  'all_n_scan':scan}
                    stop='point passes checked partial constraints and all disjoint F_n';rounds.append(rec);break
                if not additional:stop='unable to add exact Fn separator';rounds.append(rec);break
        if not selected and chosen is None:stop='rationalization failed';rounds.append(rec);break
        rounds.append(rec)
        with (ROOT/f'frontier-20261028-separator-bound-round-{r}.json').open('x',encoding='utf-8') as stream:
            json.dump(rec,stream,indent=2);stream.write('\n')
    output={'prior_sha256':PRIOR_SHA,'monotone_sha256':MONO_SHA,'verified_separator_sha256':SEP_SHA,
            'published_source_pins':{k:v[1] for k,v in cert.FILES.items()},
            'source_core_rows':len(source),'full_copy_equalities':True,'immediate_monotonic_rows':immediate,
            'rounds':rounds,'new_rows':newrows,'all_fn_cuts':extras,'stop':stop,'elapsed_s':time.monotonic()-started,
            'limits':'This LP relaxation has unspecified entropy coordinates. Numerical bounds require a separate exact dual; a partial primal is not a full source LP or an entropic law.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')
    if chosen_final is not None:
        chosen_final['search_result_sha256']=sha256(OUTPUT.read_bytes()).hexdigest()
        with POINT.open('x',encoding='utf-8') as stream:json.dump(chosen_final,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('all_fn_cuts','new_rows')},indent=2))
    print('additional_rows',len(newrows),'point_saved',chosen_final is not None)


if __name__=='__main__':main()
