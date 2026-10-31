#!/usr/bin/env python3
"""Strengthen published certificate core by full copy equalities and CMI cuts.

All generated rows are valid for the stated source-copy branches. Missing
entropy coordinates are never assumed zero. LP output is exploratory until a
separate exact rational dual is reconstructed and checked.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('primal_scan',ROOT/'frontier-20261028-exact-primal-family-scan.py')
probe=module_from_spec(spec);spec.loader.exec_module(probe)
sparse=probe.sparse;cert=probe.cert
CUTS=ROOT/'frontier-20261028-all-order-cut-refinement-result.json'
OUTPUT=ROOT/'frontier-20261028-source-closure-refinement-result.json'
BRANCHES=(tuple(cert.BASE)+("b'0",),tuple(cert.BASE)+("d'1","e'1","g'2"),
          tuple(cert.BASE)+("f'3","g'3","h'4"))
MAX_ROUNDS=15
MAX_WALL_S=110.0
MAX_ADDED_CMI=600


def row_signature(terms,lo,hi):
    return (tuple(sorted((tuple(k),v) for k,v in terms.items() if v)),lo,hi)


def copy_rows():
    rows=[]
    for form in cert.copy_forms():
        if form and form[0][1]>0:
            rows.append(({tuple(k):v for k,v in form},0.0,0.0,{'kind':'full-copy-equality'}))
    return rows


def scan_branch_cmi(keys,values,existing):
    """Return only provably negative, fully evaluable elemental Shannon rows."""
    H={key:float(value) for key,value in zip(keys,values)};H[()]=0.0
    candidates={};checked=0;unknown=0
    def maybe(terms,meta):
        nonlocal checked,unknown
        checked+=1
        if any(tuple(sorted(labels)) not in H for labels,_ in terms):unknown+=1;return
        val=sum(H[tuple(sorted(labels))]*coef for labels,coef in terms)
        if val < -1e-8:
            accum={}
            for labels,coef in terms:
                k=tuple(sorted(labels))
                if k:accum[k]=accum.get(k,0)+coef
            accum={k:v for k,v in accum.items() if v}
            sig=row_signature(accum,0.0,highspy.kHighsInf)
            if sig not in existing:
                old=candidates.get(sig)
                if old is None or val<old[0]:candidates[sig]=(val,accum,meta)
    for number,variables in enumerate(BRANCHES,1):
        allvars=set(variables)
        for v in variables:
            maybe([(allvars,1),(allvars-{v},-1)],{'kind':'branch-conditional-entropy','branch':number,'vertex':v})
        for a,b in combinations(variables,2):
            rest=sorted(allvars-{a,b})
            for size in range(len(rest)+1):
                for context in combinations(rest,size):
                    z=set(context)
                    maybe([(z|{a},1),(z|{b},1),(z|{a,b},-1),(z,-1)],
                          {'kind':'branch-CMI','branch':number,'a':a,'b':b,'condition':context})
    return checked,unknown,candidates


def main():
    started=time.monotonic();cutraw=CUTS.read_bytes();cuts=json.loads(cutraw)['all_added_cuts']
    data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text'])
    rows=sparse.build_constraints(source,cuts)+copy_rows()
    signatures={row_signature(t,lo,hi) for t,lo,hi,_ in rows}
    rounds=[];stop='round limit'
    for r in range(MAX_ROUNDS):
        if time.monotonic()-started>MAX_WALL_S:stop='wall limit';break
        t=time.monotonic();status,keys,col,vals=probe.solve(rows)
        rec={'round':r,'row_count':len(rows),'solver_status':status,
             'solve_elapsed_s':time.monotonic()-t}
        if vals is None:stop='solver not optimal';rounds.append(rec);break
        rec['objective_float_unverified']=float(vals[col[tuple(cert.BASE)]])
        # Exact feasible reconstruction is informative only; numerical output
        # remains unproved until an independent exact dual is supplied.
        rec['rounding_attempts']=[];chosen=None
        for maxden in (1000,10000,100000):
            x,bad=probe.check_rounding(rows,keys,col,vals,maxden)
            bad=[item for item in bad if item['kind']!='objective']
            rec['rounding_attempts'].append({'max_denominator':maxden,'bad_count':len(bad),'first':bad[:2]})
            if not bad:chosen=x;break
        if chosen is not None:
            rec['exact_feasible_primal_objective']=str(chosen[col[tuple(cert.BASE)]])
            H=[Fraction(0)]+[chosen[col[tuple(sparse.sets_from_mask(m))]] for m in range(1,1024)]
            scale=lcm(*(x.denominator for x in H));ints=[int(x*scale) for x in H]
            if max(map(abs,ints))<10**8:
                rec['base_all_n_scan']=probe.exhaustive_all_n(np.array(ints,dtype=np.int64))
        t=time.monotonic();checked,unknown,negative=scan_branch_cmi(keys,vals,signatures)
        ordered=sorted(negative.items(),key=lambda x:x[1][0])[:MAX_ADDED_CMI]
        rec.update({'branch_elemental_checks':checked,'unevaluable':unknown,
                    'unique_violated_evaluable_rows':len(negative),
                    'min_slack_float':min((x[0] for x in negative.values()),default=0.0),
                    'scan_elapsed_s':time.monotonic()-t,'CMI_rows_added':len(ordered)})
        for sig,(slack,terms,meta) in ordered:
            signatures.add(sig);rows.append((terms,0.0,highspy.kHighsInf,meta))
        rounds.append(rec)
        with (ROOT/f'frontier-20261028-source-closure-round-{r}.json').open('x',encoding='utf-8') as stream:
            json.dump(rec,stream,indent=2);stream.write('\n')
        if not ordered:stop='no violated fully evaluable branch Shannon rows';break
    out={'source_hashes':{k:v[1] for k,v in cert.FILES.items()},
         'input_cut_sha256':sha256(cutraw).hexdigest(),
         'full_copy_equalities_included':True,'branches':BRANCHES,
         'max_rounds':MAX_ROUNDS,'wall_limit_checked_between_rounds_s':MAX_WALL_S,
         'cut_limit_per_round':MAX_ADDED_CMI,'rounds':rounds,'stop':stop,
         'total_elapsed_s':time.monotonic()-started,
         'limits':'Unknown coordinates are not tested. Float LP objectives are unverified proposals; a stronger all-decoder bound requires an exact dual certificate and mathematical review.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
