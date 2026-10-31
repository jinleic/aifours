#!/usr/bin/env python3
"""Independent WHOLE source/full-negative contraction/shifted-grid replay.

Does NOT import canonical producer code. Uses separately derived matrix units,
string Lyndon brackets and bracket-tree/Jacobi D3, then literal theta-transported
negative words and an inverse Gram computed from the separate matrix basis.
Every canonical output is compared in the ENTIRE primitive coordinate space.
The determinant polynomial is checked at a shifted full unisolvent triangle.
Shared FLINT exact determinant/RREF arithmetic remains a stated trust boundary.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
from multiprocessing import Pool
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


whole=load('separate_integral_pbw_tools','frontier-20261028-level6-independent-coordinate-ideals.py')
ind=whole.ind
ACTIONS={g:[{w:int(2*Q(c)) for w,c in row.items()} for row in ind.ACTION[g]] for g in ('f1','f2')}
assert all(2*Q(c)==int(2*Q(c)) for g in ACTIONS for row in ind.ACTION[g] for c in row.values())
DATA=None


def qmatrix(rows):
    return flint.fmpq_mat([[flint.fmpq(Q(c).numerator,Q(c).denominator) for c in row] for row in rows])


def plus(v,w,c=1):
    result=dict(v)
    for word,b in w.items():
        result[word]=result.get(word,0)+c*b
        if not result[word]:
            del result[word]
    return result


def act2(vector,g):
    result={}
    for word,c in vector.items():
        for position,j in enumerate(word):
            for target,b in ACTIONS[g][int(j)].items():
                w=word[:position]+target+word[position+1:]
                result[w]=result.get(w,0)+c*b
                if not result[w]:
                    del result[w]
    return result


def root4(vector):
    return plus(act2(act2(vector,'f1'),'f2'),act2(act2(vector,'f2'),'f1'),-1)


def word_image(vector,word):
    output=vector
    denominator=1
    for g in reversed(word):
        if g=='f12':
            output=root4(output)
            denominator*=4
        else:
            output=act2(output,g)
            denominator*=2
    return output,denominator


def independent_contraction(d,Gram_inverse):
    denominator=math.lcm(*(Q(c).denominator for c in d.values())) if d else 1
    D={w:int(Q(c)*denominator) for w,c in d.items()}
    # Derive w_j=-theta(u_j) from the explicit positive cyclic words.
    # theta(e_i)=-f_i, theta([e1,e2])=-[f2,f1].
    cyclic=[(1,()),(-1,('f1',)),(-1,('f2',)),(-1,('f12',)),
            (1,('f1','f2')),(1,('f1','f12')),(1,('f2','f12')),
            (-2,('f1','f2','f12'))]
    negative=[]
    factors=[]
    for j,(co,word) in enumerate(cyclic):
        v,den=word_image(D,word)
        negative.append((v,den,co))
        for i in range(8):
            factors.append(Q(Gram_inverse[i][j])*co/den)
    scale=math.lcm(*(q.denominator for q in factors))
    output={}
    for j,(v,den,co) in enumerate(negative):
        for i in range(8):
            multiplier=Q(Gram_inverse[i][j])*co*scale/den
            assert multiplier.denominator==1
            multiplier=int(multiplier)
            if not multiplier:
                continue
            for word,c in v.items():
                left=str(i)+word
                right=word+str(i)
                output[left]=output.get(left,0)+multiplier*c
                output[right]=output.get(right,0)-multiplier*c
    output={w:c for w,c in output.items() if c}
    return whole.decompose_integer(output),denominator*scale


@lru_cache(None)
def tree_at(word,r,s):
    return ind.tree_d3(word,r,s)


def full_tree_d3(coefficients,words,r,s):
    out={}
    for j,c in coefficients.items():
        ind.ind.add_scaled(out,tree_at(words[j],r,s),c)
    return out


def init(data):
    global DATA
    DATA=data


def grid_check(task):
    x,y,numerator,denominator,row_scale=task
    value=int(flint.fmpz_mat([[c+x*a+y*b for c,a,b in row] for row in DATA]).det())
    assert value*denominator==numerator*row_scale, ('independent canonical grid mismatch',x,y)
    return x,y


def seventh_dimensions(a,b):
    ch=Counter({(0,0):1})
    for _ in range(7):
        nxt=Counter()
        for (u,v),c in ch.items():
            for i,j in ind.WEIGHTS:
                nxt[u+i,v+j]+=c
        ch=nxt
    for i,j in ind.WEIGHTS:
        ch[7*i,7*j]-=1
    assert all(c>=0 and c%7==0 for c in ch.values())
    ch=Counter({ab:c//7 for ab,c in ch.items() if c})
    assert sum(ch.values())==(8**7-8)//7
    lowest=ch[a,b]-ch[a-1,b]-ch[a,b-1]+ch[a-2,b-1]+ch[a-1,b-2]-ch[a-2,b-2]
    return ch[a,b],lowest


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--pencil-sha256',required=True)
    ap.add_argument('--polynomial-sha256',required=True)
    ap.add_argument('--workers',type=int,default=2)
    args=ap.parse_args()
    label=f'{args.a}{args.b}'
    name=f'frontier-20261029-level7-{label}-canonical-contraction-pencil-v1.json'
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.pencil_sha256
    C=json.loads(raw)
    polyname=f'frontier-20261029-level7-{label}-canonical-determinant-v1.json'
    polyraw=(ROOT/polyname).read_bytes()
    assert hashlib.sha256(polyraw).hexdigest()==args.polynomial_sha256
    polynomial=json.loads(polyraw)
    assert polynomial['pencil_sha256']==args.pencil_sha256
    source_raw=(ROOT/C['source_pencil']).read_bytes()
    assert hashlib.sha256(source_raw).hexdigest()==C['source_pencil_sha256']
    P=json.loads(source_raw)
    degree=(args.a,args.b,7)
    assert P['degree']==C['degree']==polynomial['degree']==list(degree)
    words=P['source_words']
    assert tuple(words)==ind.lyndon_words(degree)
    dimension,k=seventh_dimensions(args.a,args.b)
    assert len(words)==dimension and k==C['entire_primitive_dimension']
    coefs=[{int(i):Q(c) for i,c in co.items() if Q(c)} for co in P['horizontal_kernel_coefficients']]
    free=C['source_primitive_free_coordinate_indices']
    assert len(coefs)==len(free)==len(set(free))==k
    assert all(co.get(j,0)==int(i==q) for i,co in enumerate(coefs) for q,j in enumerate(free))
    for co in coefs:
        vector=ind.combine([ind.ind.standard_bracket(w) for w in words],co)
        assert not ind.act(vector,'f1',7,7) and not ind.act(vector,'f2',7,7)
    primitive=qmatrix([[co.get(j,0) for co in coefs] for j in range(len(words))])
    Gram=[[sum(ind.BASIS[i][u][v]*ind.BASIS[j][u][v] for u in range(3) for v in range(3)) for j in range(8)] for i in range(8)]
    inverse=qmatrix(Gram).inv()
    Ginv=[[Q(int(inverse[i,j].numerator),int(inverse[i,j].denominator)) for j in range(8)] for i in range(8)]
    assert Ginv==[[Q(c) for c in row] for row in C['Gram_inverse']]
    matrices=[]
    for r,s in ((7,7),(8,7),(7,8)):
        columns=[]
        all_coords=[]
        for i,co in enumerate(coefs):
            d=full_tree_d3(co,words,r,s)
            vector,den=independent_contraction(d,Ginv)
            assert set(vector)<=set(words)
            all_coords.append({w:Q(c,den) for w,c in vector.items()})
            columns.append([Q(vector.get(words[j],0),den) for j in free])
        M=[list(row) for row in zip(*columns)]
        full=[[col.get(w,Q(0)) for col in all_coords] for w in words]
        assert primitive*qmatrix(M)==qmatrix(full), 'independent canonical image not in the complete primitive basis'
        matrices.append(M)
        print('PASS canonical complete source/actions',degree,r,s,'dimension',k,flush=True)
    triples=[[[matrices[0][i][j],matrices[1][i][j]-matrices[0][i][j],matrices[2][i][j]-matrices[0][i][j]] for j in range(k)] for i in range(k)]
    assert triples==[[[Q(c) for c in e] for e in row] for row in C['matrix']]
    coefficients={(e['x_power'],e['y_power']):Q(e['coefficient']) for e in polynomial['coefficients']}
    assert len(coefficients)==len(polynomial['coefficients']) and all(u>=0 and v>=0 and u+v<=k for u,v in coefficients)
    constant=coefficients.get((0,0),Q(0))
    assert constant and (all(c>0 for c in coefficients.values()) or all(c<0 for c in coefficients.values()))
    polyden=math.lcm(*(c.denominator for c in coefficients.values()))
    nums={mon:int(c*polyden) for mon,c in coefficients.items()}
    scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in triples]
    data=[[[int(c*scale) for c in e] for e in row] for row,scale in zip(triples,scales)]
    row_scale=math.prod(scales)
    tasks=[]
    for i in range(k+1):
        x=i-3
        inner=[0]*(k+1)
        for (u,v),c in nums.items():
            inner[v]+=c*x**u
        for j in range(k+1-i):
            y=j+2
            value=0
            for c in reversed(inner):
                value=value*y+c
            tasks.append((x,y,value,polyden,row_scale))
    with Pool(args.workers,initializer=init,initargs=(data,)) as pool:
        checks=list(pool.imap_unordered(grid_check,tasks,chunksize=16))
    assert len(checks)==(k+1)*(k+2)//2
    out=ROOT/f'frontier-20261029-level7-{label}-canonical-independent-replay-v1.json'
    with out.open('x') as stream:
        json.dump({'owner':'MathKacMoody-2','degree':list(degree),'source_pencil_sha256':C['source_pencil_sha256'],
                   'canonical_pencil_sha256':args.pencil_sha256,'canonical_polynomial_sha256':args.polynomial_sha256,
                   'entire_source_dimension':k,'all_free_source_membership_and_Witt_completeness_checked':True,
                   'all_three_entire_canonical_coordinate_matrix_products_checked':True,'all_affine_matrix_entries_match':True,
                   'Gram_computed_from_independent_matrix_units':True,'polynomial_terms':len(coefficients),
                   'shifted_unisolvent_determinants':len(checks),'shifted_grid':'x=i-3,y=j+2,i,j>=0,i+j<=dimension',
                   'all_coefficients_one_sign_and_constant_nonzero':True,
                   'status':'PASS_ENTIRE_CANONICAL_SOURCE_MATRIX_AND_WHOLE_QUADRANT_POLYNOMIAL',
                   'limits':'separate matrix-unit/string-Lyndon/tree-Jacobi generation; shared FLINT exact determinant arithmetic. D3-kernel containment and actual free-source/PBW transport require written review. Not formal/kernel, configured-model-family/human, parent or novelty acceptance.'},stream,indent=2)
        stream.write('\n')
    print('PASS independent canonical',degree,'dimension',k,'shifted determinants',len(checks),out.name,flush=True)


if __name__=='__main__':
    main()
