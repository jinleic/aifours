#!/usr/bin/env python3
"""Search one-variable copies omitting two originals from conditioning.

This is a genuinely different copy protocol from the source's single-copy
branch. Exact rational separators, if found, require independent checking and a
separate graph-bound certificate. Float feasibility is not proof.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('singlecopy',ROOT/'frontier-20261028-distinct-copy-orbit-search.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
INPUT=mod.INPUT;EXPECTED=mod.EXPECTED
OUTPUT=ROOT/'frontier-20261028-double-omission-copy-search-result.json'
MAX_ORBITS=40
MAX_WALL_S=80.0


def rows_for_triple(base,copied,omitted):
    # Reuse only the generic 11-variable Shannon rows, not the old copy step.
    generic=[r for r in mod.rows_for_pair(base,copied,omitted[0]) if not r['equality']]
    Y=mod.FULL^(1<<copied)^(1<<omitted[0])^(1<<omitted[1]);rows=[]
    def add(terms,kind,subset=None):
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        constant=sum((Fraction(c)*base[m] for m,c in full.items() if m in base),Fraction())
        unknown={m-1024:c for m,c in full.items() if m not in base}
        rows.append({'full':full,'unknown':unknown,'rhs':-constant,'equality':True,
                     'metadata':{'kind':kind,'conditioning_subset':subset}})
    T=Y
    while True:
        add(((T|(1<<copied),1),(T|mod.COPY,-1)),'copy_marginal',T)
        if T==0:break
        T=(T-1)&Y
    add(((Y|mod.COPY,1),(mod.FULL,1),(mod.FULL|mod.COPY,-1),(Y,-1)),
        'copy_independence')
    return generic+rows


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    obj=json.loads(raw);base={sum(1<<mod.BASE.index(v) for v in row['entropy_variables']):Fraction(row['value'])
                              for row in obj['primal_values'] if set(row['entropy_variables'])<=set(mod.BASE)}
    if len(base)!=1023:raise ValueError('BASE_COUNT')
    base[0]=Fraction(0);G=mod.group()
    triples={(i,tuple(sorted((j,k)))) for i in range(10) for j,k in combinations(range(10),2) if i not in (j,k)}
    orbits=[]
    while triples:
        i,omitted=min(triples)
        orbit={(p[i],tuple(sorted((p[omitted[0]],p[omitted[1]])))) for p in G}
        triples-=orbit;orbits.append(sorted(orbit))
    reps=[orbit[0] for orbit in orbits];records=[];found=None
    for copied,omitted in reps[:MAX_ORBITS]:
        if time.monotonic()-start>MAX_WALL_S:break
        rows=rows_for_triple(base,copied,omitted);out=mod.solve_pair(rows,base)
        out.update({'copied_vertex_one_based':copied+1,'omitted_vertices_one_based':[v+1 for v in omitted]})
        records.append({k:v for k,v in out.items() if k!='exact_separator'})
        if 'exact_separator' in out:
            found=out;break
    result={'input_sha256':EXPECTED,'group_size':len(G),'orbit_count':len(orbits),
            'representatives_one_based':[[i+1,*(v+1 for v in omitted)] for i,omitted in reps],
            'planned_orbit_cap':MAX_ORBITS,'examined':records,'exact_separator':found,
            'elapsed_s':time.monotonic()-start,
            'limits':'Only sampled orbits for one fixed base point. Any separator needs independent row/protocol verification and an exact original-bound dual; a failed search proves no global result.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='exact_separator'},indent=2))
    if found:print('EXACT_SEPARATOR',found['copied_vertex_one_based'],found['omitted_vertices_one_based'],
                   'rows',len(found['exact_separator']['selected_rows']),'base_value',found['exact_separator']['base_value'])


if __name__=='__main__':main()
