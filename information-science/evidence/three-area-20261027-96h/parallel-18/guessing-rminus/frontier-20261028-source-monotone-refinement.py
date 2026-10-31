#!/usr/bin/env python3
"""Strengthen source-copy core with every known-coordinate monotonicity row.

Missing coordinates remain unassigned. Valid elemental CMIs are added lazily;
conditioned original-block F_n are separated using exact rational primal data.
All LP objective claims require an independently checked rational dual.
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
spec=spec_from_file_location('closure',ROOT/'frontier-20261028-source-closure-refinement.py')
closure=module_from_spec(spec);spec.loader.exec_module(closure)
probe=closure.probe;sparse=closure.sparse;cert=closure.cert
OUTPUT=ROOT/'frontier-20261028-source-monotone-refinement-result.json'
POINT=ROOT/'frontier-20261028-source-monotone-primal-frozen.json'
MAX_ROUNDS=15
MAX_WALL_S=120.0
MAX_ADDED=1000


def signatures(rows):return {closure.row_signature(t,lo,hi) for t,lo,hi,_ in rows}


def add_monotonicity(rows):
    keys={tuple(sparse.sets_from_mask(m)) for m in range(1,1024)}
    for terms,_,_,_ in rows:keys.update(terms)
    known={frozenset(k) for k in keys};known.add(frozenset())
    seen=signatures(rows);added=0
    for branch,variables in enumerate(closure.BRANCHES,1):
        allowed=frozenset(variables)
        for smaller in sorted((x for x in known if x<=allowed),key=lambda x:(len(x),sorted(x))):
            for v in sorted(allowed-smaller):
                larger=smaller|{v}
                if larger not in known:continue
                terms={tuple(sorted(larger)):1}
                if smaller:terms[tuple(sorted(smaller))]=-1
                sig=closure.row_signature(terms,0.0,highspy.kHighsInf)
                if sig not in seen:
                    seen.add(sig);rows.append((terms,0.0,highspy.kHighsInf,
                        {'kind':'known-monotonicity','branch':branch,'smaller':sorted(smaller),'vertex':v}))
                    added+=1
    return seen,added,len(keys)


def add_fn(scan,rows,extras,seen_fn):
    if scan['status']=='VIOLATION_AT_LARGE_N':
        A,B,C,D,Z=scan['assignment_masks'];a=scan['a_scaled'];c=scan['c_scaled']
        n=a//(-c)+1
    elif scan['status']=='EXACT_VIOLATION':
        A,B,C,D,Z=scan['example']['assignment_masks'];n=scan['example']['n']
    else:return []
    added=[]
    for multiple in (1,2,4):
        order=n*multiple
        if order>10000:continue
        key=(order,A,B,C,D,Z)
        if key not in seen_fn:
            seen_fn.add(key)
            meta={'kind':'copy-family','n':order,'A_mask':A,'B_mask':B,'C_mask':C,'D_mask':D,'condition_mask':Z}
            terms=sparse.fn_row(meta)
            rows.append((terms,0.0,highspy.kHighsInf,meta));extras.append(meta);added.append(meta)
    return added


def main():
    t0=time.monotonic();raw=closure.CUTS.read_bytes();extras=json.loads(raw)['all_added_cuts']
    data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text'])
    rows=sparse.build_constraints(source,extras)+closure.copy_rows()
    seen,monotone_count,initial_coordinates=add_monotonicity(rows)
    seen_fn={(m['n'],m['A_mask'],m['B_mask'],m['C_mask'],m['D_mask'],m['condition_mask']) for m in extras}
    rounds=[];stop='round limit';final=None;selected_cmi=[]
    for r in range(MAX_ROUNDS):
        if time.monotonic()-t0>MAX_WALL_S:stop='wall limit';break
        solve_t=time.monotonic();status,keys,col,vals=probe.solve(rows)
        rec={'round':r,'rows':len(rows),'solver_status':status,'solve_elapsed_s':time.monotonic()-solve_t}
        if vals is None:rounds.append(rec);stop='LP not optimal';break
        rec['objective_float_unverified']=float(vals[col[tuple(cert.BASE)]])
        chosen=None;attempts=[]
        for maxden in (1000,10000,100000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            bad=[x for x in bad if x['kind']!='objective']
            attempts.append({'max_denominator':maxden,'bad_count':len(bad),'first':bad[:2]})
            if not bad:chosen=x;break
        rec['rationalization']=attempts
        if chosen is not None:rec['exact_feasible_primal_objective']=str(chosen[col[tuple(cert.BASE)]])
        t=time.monotonic();checked,unknown,violations=closure.scan_branch_cmi(keys,vals,seen)
        ordered=sorted(violations.items(),key=lambda item:item[1][0])[:MAX_ADDED]
        rec.update({'elemental_checked':checked,'elemental_unevaluable':unknown,
                    'elemental_violated_evaluable':len(violations),
                    'elemental_cuts_added':len(ordered),'scan_elapsed_s':time.monotonic()-t})
        for sig,(slack,terms,meta) in ordered:
            seen.add(sig);rows.append((terms,0.0,highspy.kHighsInf,meta))
            selected_cmi.append({'terms':[[list(k),v] for k,v in sorted(terms.items())],'metadata':meta})
        if not ordered and chosen is not None:
            H=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
            scale=lcm(*(x.denominator for x in H));nums=[int(x*scale) for x in H]
            if max(map(abs,nums))<10**8:
                scan=probe.exhaustive_all_n(np.array(nums,dtype=np.int64));rec['all_n_scan']=scan
                added=add_fn(scan,rows,extras,seen_fn);rec['new_fn_cuts']=added
                if scan['status']=='ALL_DISJOINT_BLOCK_SUBSTITUTIONS_AND_ALL_POSITIVE_N_PASS':
                    final={'coordinates':len(keys),'base_scale':scale,
                           'primal_values':[{'entropy_variables':k,'value':str(chosen[i])} for i,k in enumerate(keys)],
                           'exact_objective':str(chosen[col[tuple(cert.BASE)]]),'all_n_scan':scan}
                    stop='exact point passes evaluable CMI and disjoint F_n';rounds.append(rec);break
                if not added:stop='unable to add exact separator';rounds.append(rec);break
            else:stop='integer range';rounds.append(rec);break
        if not ordered and chosen is None:stop='no numerical CMI violations but exact reconstruction failed';rounds.append(rec);break
        rounds.append(rec)
        with (ROOT/f'frontier-20261028-source-monotone-round-{r}.json').open('x',encoding='utf-8') as stream:
            json.dump(rec,stream,indent=2);stream.write('\n')
    output={'source_hashes':{k:v[1] for k,v in cert.FILES.items()},
            'initial_cut_sha256':sha256(raw).hexdigest(),'known_coordinate_count_initial':initial_coordinates,
            'known_monotonicity_rows_added':monotone_count,'full_copy_equalities_included':True,
            'rounds':rounds,'selected_CMI_rows':selected_cmi,'all_fn_cuts':extras,
            'stop':stop,'elapsed_s':time.monotonic()-t0,
            'limits':'Partial-coordinate valid-row LP only. Any numerical upper improvement needs exact dual proof; a feasible partial point is not a full Shannon or entropic witness.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')
    if final is not None:
        final['source_result_sha256']=sha256(OUTPUT.read_bytes()).hexdigest()
        with POINT.open('x',encoding='utf-8') as stream:json.dump(final,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('selected_CMI_rows','all_fn_cuts')},indent=2))
    print('selected_CMI_rows',len(selected_cmi),'final_point_saved',final is not None)


if __name__=='__main__':main()
