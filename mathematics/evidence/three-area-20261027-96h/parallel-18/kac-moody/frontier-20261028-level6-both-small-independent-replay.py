#!/usr/bin/env python3
"""Independent literal BOTH-seed source/ideal/matrix replay for finite corners.

Does not import the corner producer or use its one-seed components as premises.
Regenerates both Serre ideals from raw integral PBW and positive adjoint words,
checks BOTH source/target span directions, all primitive classes and ideal
basis derivatives, and EVERY actual target minor entry. Determinants are
replayed with ordinary Python-integer fraction-free Bareiss, not FLINT's
producer determinant. Final ideal RREF arithmetic remains shared FLINT.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent_small_row_tools',ROOT/'frontier-20261028-level6-coordinate-row-independent-replay.py')
tools=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)
whole=tools.whole
ind=whole.ind


def integer_determinant(matrix):
    n=len(matrix)
    assert n and all(len(row)==n for row in matrix)
    A=[list(row) for row in matrix]
    sign=1
    previous=1
    for k in range(n-1):
        pivot=next((j for j in range(k,n) if A[j][k]),None)
        if pivot is None:
            return 0
        if pivot!=k:
            A[pivot],A[k]=A[k],A[pivot]
            sign=-sign
        value=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=value*A[i][j]-A[i][k]*A[k][j]
                assert numerator%previous==0
                A[i][j]=numerator//previous
            A[i][k]=0
        previous=value
    return sign*A[-1][-1]


def parse(rows):
    return [{w:Q(c) for w,c in row.items() if Q(c)} for row in rows]


def load_free(pins,char,r,s):
    free={}
    for pin in pins:
        raw=(ROOT/pin['file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==pin['sha256']
        P=json.loads(raw)
        a,b,n=P['degree']
        assert n==6
        words=P['source_words']
        assert len(words)==len(set(words))==char.get((a,b),0) and words==sorted(words)
        assert all(ind.ind.lyndon(w) and ind.deg(w)==(a,b,6) for w in words)
        vectors=[{words[int(j)]:Q(c) for j,c in co.items() if Q(c)} for co in P['horizontal_kernel_coefficients']]
        expected=char.get((a,b),0)-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
        assert len(vectors)==expected and len(tools.basis_span(vectors))==expected
        for v in vectors:
            assert not tools.linear_image(v,'f1',r,s) and not tools.linear_image(v,'f2',r,s)
        free[a,b]=vectors
    oriented=set(free)|{(b,a) for a,b in free}
    expected_oriented=set()
    for a,b in char:
        if 2*a-b<=6 and 2*b-a<=6:
            expected=char[a,b]-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
            if expected:
                assert expected>0
                expected_oriented.add((a,b))
    assert len(free)==15 and len(oriented)==24 and oriented==expected_oriented
    return free


def replay_pair(pin,free,char):
    raw=(ROOT/pin['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256']
    C=json.loads(raw)
    r,s=C['r'],C['s']
    assert r==pin['r'] and s==pin['s'] and min(r,s)>=1 and max(r,s)<=4
    entries=[]
    for piece in C['parts']:
        body=(ROOT/piece['file']).read_bytes()
        assert hashlib.sha256(body).hexdigest()==piece['sha256']
        e=json.loads(body)
        assert e['r']==r and e['s']==s
        entries.append(e)
    assert len(entries)==15 and {tuple(e['degree'][:2]) for e in entries}==set(free)
    queries={tuple(e['degree']) for e in entries}|{(*e['degree'][:2],5) for e in entries}
    spaces=whole.ideal_spaces(queries,r,s)
    reports=[]
    for e in entries:
        degree=tuple(e['degree'])
        a,b,n=degree
        assert n==6
        I=spaces[degree]
        T=spaces[a,b,5]
        claimedI=parse(e['source_ideal_lyndon_coordinate_rows'])
        claimedT=parse(e['target_ideal_lyndon_coordinate_rows'])
        whole.same_space(I,claimedI)
        whole.same_space(T,claimedT)
        assert len(I)==e['full_source_ideal_dimension'] and len(T)==e['full_target_ideal_dimension']
        quotient=tools.basis_span(I.rows.values())
        retained=[]
        vectors=free[a,b]
        for j,v in enumerate(vectors):
            if quotient.insert(v):
                retained.append(j)
        assert retained==e['retained_free_primitive_indices']
        k=len(retained)
        assert k==e['actual_primitive_quotient_dimension']
        for row in I.rows.values():
            assert not T.reduce(tools.linear_image(row,'f3',r,s)), 'fresh whole BOTH-seed ideal did not descend'
        summary={'degree':list(degree),'source_ideal_dimension':len(I),'target_ideal_dimension':len(T),'actual_primitive_dimension':k,
                 'both_source_target_span_directions_checked':True,'all_fresh_source_ideal_basis_derivatives_checked':True}
        if not k:
            assert e['status']=='ZERO_ACTUAL_PRIMITIVE_SOURCE'
            reports.append(summary)
            continue
        assert e['status']=='FULL_ACTUAL_BOTH_SEED_PRIMITIVE_RANK'
        target_rows={min(row):row for row in claimedT}
        columns=[whole.normal_form(tools.linear_image(vectors[j],'f3',r,s),target_rows) for j in retained]
        assert len(tools.basis_span(columns))==k==e['actual_D3_rank']
        selected=e['selected_target_lyndon_coordinates']
        matrix=[[Q(v.get(w,0)) for v in columns] for w in selected]
        assert len(matrix)==k and matrix==[[Q(c) for c in row] for row in e['matrix']]
        scales=[math.lcm(*(c.denominator for c in row)) for row in matrix]
        integer=[[int(c*scale) for c in row] for row,scale in zip(matrix,scales)]
        determinant=Q(integer_determinant(integer),math.prod(scales))
        assert determinant and determinant==Q(e['exact_nonzero_determinant'])
        summary.update({'all_actual_matrix_entries_matched':True,'independent_integer_Bareiss_determinant':str(determinant)})
        reports.append(summary)
        print('PASS independent BOTH-seed',r,s,degree,'P',k,'I',len(I),'T',len(T),flush=True)
    output=ROOT/f'frontier-20261028-level6-r{r}s{s}-corner-independent-replay-v1.json'
    with output.open('x') as stream:
        json.dump({'r':r,'s':s,'input_family':pin['file'],'input_sha256':pin['sha256'],'records':reports,
                   'fresh_both_seed_ideal_trace':[row for row in whole.TRACE if tuple(row['degree']) in queries],
                   'status':'PASS_ALL_FIFTEEN_LITERAL_BOTH_SEED_PRIMITIVE_MAPS',
                   'independent_integer_determinant_count':sum('independent_integer_Bareiss_determinant' in row for row in reports),
                   'limits':'independent literal PBW/adjoint/tree-Jacobi generation and Python-integer determinants; FLINT final ideal RREF shared. Named actual free-Levi/PBW/finite-sl3 inputs. Not formal, parent, independent-model or novelty acceptance.'},stream,indent=2)
        stream.write('\n')
    print('WROTE',output.name,flush=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--r',type=int,choices=[1,2,3,4],required=True)
    ap.add_argument('--manifest-sha256',required=True)
    args=ap.parse_args()
    raw=(ROOT/'frontier-20261028-level6-both-small-produced-family-pins-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.manifest_sha256
    C=json.loads(raw)
    pins=[p for p in C['families'] if p['r']==args.r]
    assert len(pins)==4 and {p['s'] for p in pins}=={1,2,3,4}
    char=tools.source_character()
    free=load_free(C['free_pencils'],char,args.r,1)
    for pin in pins:
        whole.TRACE.clear()
        replay_pair(pin,free,char)
    print('DONE independent both-small r',args.r,flush=True)


if __name__=='__main__':
    main()
