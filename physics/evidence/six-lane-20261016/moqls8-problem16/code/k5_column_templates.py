"""Generate the16 frozen full-column support templates and the13 old-F+42unit
instances (no H3/new variables). Gate on the complete up-to8 component control.
Additional independent finite check: enumerate every3x3/4x4 nonempty support
matrix of maxdegree3 satisfying pair-overlap and H3; use these25/298 matrices
to enumerate ALL43290 labelled7x7 support patterns having the chosen column1
supportA under the theorem's three component cases. Canonicalise under ALL
S3(A)xS4(B) coordinate permutations and row2..7 sorting, and require the orbit
set to equal the16 table orbits. An outside orbit is recorded and blocks use.
Writes manifest/controls only, never CNFs/proofs. Parent proof review is still
needed for the general component theorem and genuine-vector coverage.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'evidence/k5_column_templates_v1'
NOTE=ROOT/'review/K5_COLUMN0_TEMPLATE_COVER.r1.md'
NOTE_SHA='1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a'
MAP=ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.map.json'
MAP_SHA='7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197'
BASE=ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.cnf'
CONTROL=ROOT/'evidence/k5_template_component_control_v2'
B_TABLE={'B1':['7','6','5','4'],'B2':['7','6','45','45'],'B3':['67','67','45','45'],
         'B4':['7','456','456','456'],'B5':['7','56','456','456'],'B6':['567','467','457','456']}
C_TABLE={'C1':['7','6','5','234','134','124'],'C2':['7','56','56','234','134','124'],
         'C3':['67','567','567','234','134','124'],'C4':['567','567','567','234','134','124']}


def sha(b): return hashlib.sha256(b).hexdigest()

def mask(s): return sum(1<<(int(c)-1) for c in s)

def lexrank(m): return sum(((m>>(c-1))&1)<<(7-c) for c in range(1,8))

def support_matrix(n):
    out=[]; choices=range(1,1<<n)
    for rows in itertools.product(choices,repeat=n):
        if any(x.bit_count()>3 for x in rows): continue
        cols=[sum(1<<r for r in range(n) if(rows[r]>>c)&1) for c in range(n)]
        if any(not 1<=x.bit_count()<=3 for x in cols): continue
        if any((a&b).bit_count()==1 for masks in (rows,cols) for a,b in itertools.combinations(masks,2)): continue
        if any((a|b|c).bit_count()<3 for masks in (rows,cols) for a,b,c in itertools.combinations(masks,3)): continue
        out.append(rows)
    return out


def main():
    free=shutil.disk_usage(ROOT).free
    if free<12_200_000_000:
        with (ROOT/'evidence/K5_TEMPLATE_MANIFEST_DEFERRED.json').open('x') as f:
            json.dump({'free_bytes':free,'launch_floor':12_200_000_000,'stage':'finite template control'},f)
        raise SystemExit('disk gate: defer until parent instruction')
    note=NOTE.read_bytes(); mb=MAP.read_bytes()
    if sha(note)!=NOTE_SHA or sha(mb)!=MAP_SHA: raise RuntimeError('input pin mismatch')
    cb=(CONTROL/'RESULT.json').read_bytes(); cm=(CONTROL/'META.json').read_bytes()
    c=json.loads(cb); meta=json.loads(cm)
    if c.get('complete') is not True or c.get('all_pass') is not True or c.get('outside_components')!=[]:
        raise RuntimeError('complete exhaustive component control is not PASS')
    if meta['proof_note_sha256']!=NOTE_SHA or meta['max_part_size']!=8:
        raise RuntimeError('component control proof/size mismatch')
    spec=importlib.util.spec_from_file_location('cover',ROOT/'code/k5_cover.py')
    C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    base=C.Base(BASE)
    if base.sha!=C.BASE_SHA: raise RuntimeError('base pin mismatch')
    gm={}
    for key,v in json.loads(mb)['vars'].items():
        nm=json.loads(key)
        if nm[0]=='g': gm[(nm[1],tuple(nm[2]),tuple(nm[3]))]=v
    rows=[]
    for p in ('P0','P1'):
        tail=['123','123'] if p=='P0' else ['23','123']
        for b,first in B_TABLE.items(): rows.append((p+'-'+b,first+tail))
    for ct,ss in C_TABLE.items(): rows.append(('P2-'+ct,ss))
    group=[]
    for pa in itertools.permutations((1,2,3)):
        for pb in itertools.permutations((4,5,6,7)):
            perm=(0,)+pa+pb
            group.append(tuple(sum(1<<(perm[c]-1) for c in range(1,8) if(m>>(c-1))&1) for m in range(128)))
    canonical_cache={}
    def canon(ms):
        key=tuple(sorted(ms))
        if key not in canonical_cache:
            canonical_cache[key]=min(tuple(sorted(lexrank(p[m]) for m in key)) for p in group)
        return canonical_cache[key]
    expected={canon([mask(s) for s in ss]):label for label,ss in rows}
    if len(expected)!=16: raise RuntimeError('table has duplicate orbits')
    # Independent small full-matrix enumeration, no component-type assumptions.
    small={n:support_matrix(n) for n in (3,4)}
    wanted=c['all_labelled_square_matrices_by_size_0to8']
    if len(small[3])!=wanted[3] or len(small[4])!=wanted[4]:
        raise RuntimeError('small direct enumeration differs from component-composition count')
    def put(local,coords):
        return [sum(1<<(coords[j]-1) for j in range(len(coords)) if(m>>j)&1) for m in local]
    keys=set(); labelled=0
    def visit(ms):
        nonlocal labelled
        labelled+=1
        # Row labels2..7 are fully enumerated by distinct permutations below.
        key=canon(ms)
        if key not in expected:
            OUT.mkdir(exist_ok=False)
            with (OUT/'OUTSIDE_ORBIT.json').open('x') as f: json.dump({'masks':ms,'canonical':key},f)
            raise RuntimeError('pattern outside16table orbits; recorded')
        keys.add(key)
    # 3x3 A-component full/minus-edge; remaining4 coordinates are B.
    for pure in small[4]:
        bms=put(pure,(4,5,6,7))
        for apos in itertools.combinations(range(6),2):
            slots=[i for i in range(6) if i not in apos]
            ms=[0]*6
            for i,m in zip(slots,bms): ms[i]=m
            ms[apos[0]]=ms[apos[1]]=mask('123'); visit(ms)
        for shortpos in range(6):
            for fullpos in range(6):
                if shortpos==fullpos: continue
                for missing in (1,2,3):
                    slots=[i for i in range(6) if i not in (shortpos,fullpos)]
                    ms=[0]*6
                    for i,m in zip(slots,bms): ms[i]=m
                    ms[shortpos]=mask('123')^(1<<(missing-1)); ms[fullpos]=mask('123'); visit(ms)
    # 4x4 matching-complement A+oneB; remaining3 pure coordinates.
    for b in (4,5,6,7):
        coords=tuple(x for x in (4,5,6,7) if x!=b)
        for pure in small[3]:
            pms=put(pure,coords)
            for mixedpos in itertools.combinations(range(6),3):
                purepos=[i for i in range(6) if i not in mixedpos]
                for missing in itertools.permutations((1,2,3)):
                    ms=[0]*6
                    for i,m in zip(purepos,pms): ms[i]=m
                    for i,a in zip(mixedpos,missing): ms[i]=(mask('123')^(1<<(a-1)))|(1<<(b-1))
                    visit(ms)
    if labelled!=43290 or keys!=set(expected): raise RuntimeError('labelled/orbit coverage count mismatch')
    OUT.mkdir(exist_ok=False)
    cases=[]
    for label,ss in rows:
        ms=[mask(s) for s in ss]
        if [lexrank(m) for m in ms]!=sorted(lexrank(m) for m in ms): raise RuntimeError('ROWLEX table error')
        units=[]
        for i,S in enumerate(ss,start=2):
            for co in range(1,8):
                v=gm[(1,(0,co),(i,0))]
                if v!=C.CHAIN[i-1][co-1]: raise RuntimeError('V1..V6 id mismatch')
                units.append(v if str(co) in S else -v)
        if len(units)!=42 or len({abs(x) for x in units})!=42: raise RuntimeError('unit identity count')
        root=sum(1<<(int(x)-1) for x in ss[0])
        if root not in(64,96,112): raise RuntimeError('unexpected root')
        cases.append({'id':label,'supports_row2to7':[[int(x) for x in s] for s in ss],
                      'units':units,'unit_count':42,'root':root,'cnf_sha256':base.leaf_sha(units),
                      'cnf_vars':base.nv,'cnf_clauses':base.nc+42,'run_required':root!=112,
                      'excluded_by_imported_c112':root==112})
    run=[x for x in cases if x['run_required']]
    result={'schema':'k5-column-template-manifest/1','proof_note_sha256':NOTE_SHA,
            'script_sha256':sha(Path(__file__).read_bytes()),'base_cnf_sha256':base.sha,'map_sha256':sha(mb),
            'component_control_result_sha256':sha(cb),'component_control_meta_sha256':sha(cm),
            'finite_orbit_control':{'small_full3x3_patterns':len(small[3]),'small_full4x4_patterns':len(small[4]),
                'labelled_patterns_with_fixed_column1_A':labelled,'coordinate_group_size':len(group),
                'canonical_orbits':len(keys),'table_orbits':len(expected),'all_pass':True},
            'cases':cases,'run_cases':[x['id'] for x in run],
            'run_cases_by_root':{str(r):sum(x['root']==r for x in run) for r in(64,96)},
            'semantic_cover_status':'conditional on parent proof review; NOT a Boolean cover of F',
            'c112_proof_sha256':'b6b1e6d23c5f4a1bbd7630027463d3bc2f398fb245ff6b450a718fd3305d14bd'}
    if len(run)!=13: raise RuntimeError('required case count differs')
    with(OUT/'MANIFEST.json').open('x') as f: json.dump(result,f,indent=1)
    print(json.dumps({'cases':len(cases),'run_cases':len(run),'finite_orbit_control':result['finite_orbit_control'],
                      'run_cases_by_root':result['run_cases_by_root']}),flush=True)


if __name__=='__main__': main()
