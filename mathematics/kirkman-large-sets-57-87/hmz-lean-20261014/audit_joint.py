#!/usr/bin/env python3
"""Read-only check of every saved joint-model row and exact-cover column; no solve."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,itertools,json
from collections import Counter,defaultdict
from ortools.sat.python import cp_model
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'evidence'/'joint57'
sys.path.insert(0,str(OUT))
import c19_verify as independent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    manifest=json.loads((OUT/'manifest.json').read_text())
    assert sha(OUT/'model.pbtxt')==manifest['model_sha256']
    assert sha(OUT/'rows.json')==manifest['rows_sha256']
    assert sha(OUT/'input-packing17.json')==manifest['packing_sha256']
    data=json.loads((OUT/'inventory.json').read_text())
    independent.verify_inventory(data)
    packing=json.loads((OUT/'input-packing17.json').read_text())
    keys={tuple(rec['representative']):i for i,rec in enumerate(data['triple_orbits'])}
    forbidden=set()
    for candidate in packing[:16]:
        actual={keys[k] for k in independent.check_fixed(candidate)}
        assert actual==set(candidate['orbit_ids']) and not actual.intersection(forbidden)
        forbidden.update(actual)
    remaining=sorted(set(range(1540))-forbidden)
    rows=json.loads((OUT/'rows.json').read_text())
    fixed=rows['fixed_rows']; free=rows['free_rows']
    model=cp_model.CpModel()
    assert model.proto.parse_text_format((OUT/'model.pbtxt').read_text())
    assert len(model.proto.variables)==len(fixed)+len(free)==61948
    assert all(list(v.domain)==[0,1] for v in model.proto.variables)
    assert not model.validate()
    expected=[]
    # These are the exact row conventions of c19_search.fixed_model, but the
    # full19 canonicalizer and block shifter come from the independent checker.
    for oid in remaining:
        rec=data['triple_orbits'][oid]
        if rec['fixed_admissible']:
            expected.extend([oid,s] for s in range(19))
            if rec['type']=='ABC': expected.append([oid,-1])
    assert fixed==expected
    expected_free=[]
    for oid in remaining:
        for shift in range(19):
            b=independent.shifted(data['triple_orbits'][oid]['representative'],shift)
            expected_free.extend([a,oid,shift,list(b)] for a in range(2))
    assert free==expected_free
    columns=[[] for _ in range(57+84)]
    aaa=[]
    orbits={oid:[] for oid in remaining}
    for var,(oid,shift) in enumerate(fixed):
        rec=data['triple_orbits'][oid]
        orbits[oid].append(var)
        if shift!=-1:
            b=independent.shifted(rec['representative'],shift)
            for point in b: columns[point].append(var)
            if rec['type']=='AAA': aaa.append(var)
        else:
            assert rec['type']=='ABC'
        for pair in rec['pair_orbits']: columns[57+pair].append(var)
    pairs=list(itertools.combinations(range(57),2))
    pair_ids={p:i for i,p in enumerate(pairs)}
    concrete=[[[] for _ in pairs] for a in range(2)]
    for index,(base,oid,shift,b) in enumerate(free):
        var=len(fixed)+index
        orbits[oid].append(var)
        for pair in itertools.combinations(b,2):
            concrete[base][pair_ids[pair]].append(var)
    expected_columns=columns+[orbits[oid] for oid in remaining]+concrete[0]+concrete[1]
    actual_columns=[]; linear=[]
    for c in model.proto.constraints:
        assert not list(c.enforcement_literal)
        if c.has_exactly_one(): actual_columns.append(list(c.exactly_one.literals))
        elif c.has_linear(): linear.append(c.linear)
        else: raise AssertionError('unexpected constraint type')
    assert actual_columns==expected_columns
    assert len(linear)==2
    assert list(linear[0].vars)==aaa
    assert list(linear[0].coeffs)==[1]*len(aaa)
    assert list(linear[0].domain)==[4,9]
    anchor=manifest['anchor']
    anchor_idx=len(fixed)+next(i for i,row in enumerate(free) if row[:3]==[anchor['base'],anchor['orbit_id'],anchor['shift']])
    assert list(linear[1].vars)==[anchor_idx] and list(linear[1].coeffs)==[1] and list(linear[1].domain)==[1,1]
    assert anchor['orbit_id'] in data['inadmissible_fixed_AAA_orbit_ids']
    assert len(actual_columns)==4425 and len(model.proto.constraints)==4427
    assert all(len(col)==39 for base in concrete for col in base)
    assert set(map(len,columns[:57]))=={1065}
    orbit_lengths=Counter(len(c) for c in orbits.values())
    assert orbit_lengths=={38:27,57:848,58:217}
    kinds=Counter(data['triple_orbits'][oid]['type'] for oid in remaining)
    assert kinds=={'AAA':89,'AAB':786,'ABC':217}
    result={'verdict':'PASS','scope':'complete read-only row/column audit, not a SAT or nonexistence proof',
            'audit_source_sha256':sha(Path(__file__)),'manifest_sha256':sha(OUT/'manifest.json'),
            'model_sha256':sha(OUT/'model.pbtxt'),'row_sha256':sha(OUT/'rows.json'),
            'remaining_types':dict(kinds),'orbit_column_degrees':dict(orbit_lengths),
            'replacement_point_column_degree':1065,'free_pair_column_degree':39,
            'fixed_rows':len(fixed),'free_rows':len(free),'exact_one_columns':len(actual_columns),
            'linear_constraints':2,'constraints':len(model.proto.constraints),
            'all_replacement_AAA_counts_allowed':list(range(4,10)),
            'solver_calls':0}
    (ROOT/'evidence'/'joint-model-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
