#!/usr/bin/env python3
"""Check all 64 degree-222 parameter cells independently and exactly.

Each off-diagonal magnitude is 1 or 2+x (x>=0). Only the choice of which
magnitudes equal 1 affects Serre ideals in degrees <=(2,2,2). The checker
rebuilds these ideals and the affine lowering matrices without producer or
SymPy imports, then verifies every positive determinant in FLINT by Bareiss.
"""
import argparse
import ast
import gzip
import hashlib
import json
import math
import time
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import fmpz_mpoly_ctx
from check_certificate import TensorCoordinates, ExactSpan, tensor, comm, word_lowering
from check_interior_minor import bareiss

EDGES=((0,1),(0,2),(1,0),(1,2),(2,0),(2,1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def linear_coefficients(text, variable_count):
    """Safe exact parser of affine rational expressions, not Python eval."""
    zero=(Q(0),)*(variable_count+1)
    def scalar(value):
        return (Q(value),)+zero[1:]
    def walk(node):
        if isinstance(node, ast.Constant) and isinstance(node.value,int):
            return scalar(node.value)
        if isinstance(node,ast.Name) and node.id in {'x'+str(i) for i in range(variable_count)}:
            index=int(node.id[1:])+1
            return tuple(Q(int(i==index)) for i in range(variable_count+1))
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):
            return tuple(-x for x in walk(node.operand))
        if isinstance(node,ast.BinOp):
            left,right=walk(node.left),walk(node.right)
            if isinstance(node.op,ast.Add):
                return tuple(a+b for a,b in zip(left,right))
            if isinstance(node.op,ast.Sub):
                return tuple(a-b for a,b in zip(left,right))
            if isinstance(node.op,ast.Mult):
                if all(x==0 for x in left[1:]):
                    return tuple(left[0]*x for x in right)
                if all(x==0 for x in right[1:]):
                    return tuple(right[0]*x for x in left)
                raise ValueError('non-affine matrix entry')
            if isinstance(node.op,ast.Div):
                require(all(x==0 for x in right[1:]) and right[0]!=0,'nonconstant denominator')
                return tuple(x/right[0] for x in left)
        raise ValueError('unexpected expression syntax')
    return walk(ast.parse(text,mode='eval').body)


def ideals_through_222(matrix, basis):
    spaces={}
    for alpha in basis.ordered:
        if max(alpha)>2:
            continue
        generated=[]
        for i in range(3):
            for j in range(3):
                if i==j:
                    continue
                exponent=1-matrix[i][j]
                degree=tuple(exponent if k==i else 1 if k==j else 0 for k in range(3))
                if degree==alpha:
                    p={(j,):Q(1)}
                    for _ in range(exponent):
                        p=comm({(i,):Q(1)},p)
                    generated.append(basis.solve(p,alpha))
            previous=tuple(a-int(k==i) for k,a in enumerate(alpha))
            if previous in spaces:
                generated.extend(basis.raise_row(i,previous,row) for row in spaces[previous].pivots.values())
        spaces[alpha]=ExactSpan(generated)
    return spaces


def verify_cell(data, mask, basis):
    require(data['mask']==mask and data['degree']==[2,2,2],'wrong cell/degree')
    matrix=[[2 if i==j else -2 for j in range(3)] for i in range(3)]
    edges=[]
    for bit,(i,j) in enumerate(EDGES):
        if mask>>bit&1:
            matrix[i][j]=-1
        else:
            edges.append((i,j))
    require(data['baseline_matrix']==matrix and list(map(tuple,data['variable_edges']))==edges,'parameter dictionary mismatch')
    ideals=ideals_through_222(matrix,basis)
    alpha=(2,2,2)
    columns=[i for i in range(len(basis.words[alpha])) if i not in ideals[alpha].pivots]
    require(len(columns)==data['quotient_dimension'],'quotient dimension mismatch')
    if not columns:
        require(data['status']=='ZERO_QUOTIENT','zero quotient mislabeled')
        return {'mask':mask,'status':'PASS','dimension':0,'monomials':0}
    require(data['status']=='POSITIVE_MINOR_CANDIDATE','cell has no positive-minor certificate')
    targets=[]
    for i in range(3):
        previous=tuple(2-int(i==k) for k in range(3))
        targets.extend((i,j) for j in range(len(basis.words[previous])) if j not in ideals[previous].pivots)
    def numbers(cartan):
        out=[[Q(0)]*len(columns) for _ in targets]
        for column,index in enumerate(columns):
            image={}
            for i in range(3):
                previous=tuple(2-int(i==k) for k in range(3))
                raw=word_lowering(tensor(basis.words[alpha][index]),i,cartan)
                reduced=ideals[previous].remainder(basis.solve(raw,previous))
                image.update({(i,j):value for j,value in reduced.items()})
            for row,key in enumerate(targets):
                out[row][column]=Q(image.get(key,0))
        return out
    baseline=numbers(matrix)
    slopes=[]
    for i,j in edges:
        shifted=[row[:] for row in matrix]
        shifted[i][j]-=1
        value=numbers(shifted)
        slopes.append([[value[r][c]-baseline[r][c] for c in range(len(columns))] for r in range(len(targets))])
    rows=data['chosen_rows']
    n=len(columns)
    require(len(rows)==n and len(set(rows))==n and all(0<=r<len(targets) for r in rows),'invalid selected rows')
    require(len(data['minor'])==n and all(len(row)==n for row in data['minor']),'minor shape mismatch')
    entries=[[(baseline[r][c],)+tuple(slope[r][c] for slope in slopes) for c in range(n)] for r in rows]
    require(all(linear_coefficients(data['minor'][r][c],len(edges))==entries[r][c] for r in range(n) for c in range(n)),'saved minor is not the independently rebuilt lowering minor')
    denominator=math.lcm(*(value.denominator for row in entries for entry in row for value in entry))
    # For a constant cell, Z is embedded faithfully in Z[dummy]; the dummy
    # variable has zero exponent everywhere and introduces no new parameter.
    arity=max(1,len(edges))
    ring=fmpz_mpoly_ctx.get(tuple('x'+str(i) for i in range(arity)))
    gens=ring.gens()
    scaled=[]
    for row in entries:
        scaled.append([ring.constant(int(entry[0]*denominator))+sum((gens[k]*int(entry[k+1]*denominator) for k in range(len(edges))),ring.constant(0)) for entry in row])
    determinant,divisions=bareiss(scaled,ring)
    orientation=data['orientation']
    require(orientation in (-1,1),'bad determinant orientation')
    terms={}
    for powers,coefficient in data['polynomial_terms']:
        require(len(powers)==len(edges) and all(isinstance(p,int) and p>=0 for p in powers),'bad exponents')
        key=tuple(powers) if edges else (0,)
        require(key not in terms,'duplicate monomial')
        value=Q(coefficient)
        require(value>0,'nonpositive listed coefficient')
        scaled_coefficient=value*denominator**n
        require(scaled_coefficient.denominator==1,'nonintegral cleared determinant coefficient')
        terms[key]=scaled_coefficient.numerator
    require(len(terms)==data['monomials'],'term count mismatch')
    constant=Q(data['constant'])
    require(constant>0 and terms.get((0,)*arity)==constant*denominator**n,'constant mismatch')
    require(ring.from_dict(terms)==orientation*determinant,'exact determinant identity failed')
    # Negative control within each cell: changing the constant must be rejected
    # by the exact identity, without recomputing the determinant.
    changed=dict(terms)
    changed[(0,)*arity]+=1
    require(ring.from_dict(changed)!=orientation*determinant,'tampered determinant accepted')
    return {'mask':mask,'status':'PASS','dimension':n,'variables':len(edges),'monomials':len(terms),
            'positive_constant':str(constant),'denominator_clearing':denominator,
            'exact_divisions':divisions,'tampered_coefficient_rejected':True}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('directory',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    started=time.monotonic()
    flint.ctx.threads=1
    expected=set(range(64))
    paths={mask:args.directory/f'mask-{mask}.json.gz' for mask in expected}
    require(all(path.is_file() for path in paths.values()),'missing cell in required complete 64-cell scope')
    basis=TensorCoordinates(6)
    records=[]
    for mask in sorted(expected):
        blob=paths[mask].read_bytes()
        record=verify_cell(json.loads(gzip.decompress(blob)),mask,basis)
        record['certificate_sha256']=hashlib.sha256(blob).hexdigest()
        records.append(record)
        print(json.dumps({'checked_mask':mask,'dimension':record['dimension'],'monomials':record['monomials']}),flush=True)
    source_paths=['work/check_interior_cells.py','work/check_interior_minor.py','work/check_certificate.py']
    result={'status':'PASS','scope':'all 64 cells covering strictly negative rank3 GCM off-diagonals, degree222 only',
            'cells':records,'cell_count':len(records),'field':'Q / exact polynomial identities over Z',
            'python_flint_version':flint.__version__,'threads':1,
            'source_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in source_paths},
            'elapsed_seconds':round(time.monotonic()-started,3),
            'logical_bridge':'Serre spans are constant within each cell through degree222. Lower degrees have coefficient one and are already settled. Positive maximal minors exclude K/I in degree222 only.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cells'},indent=2))


if __name__=='__main__':
    main()
