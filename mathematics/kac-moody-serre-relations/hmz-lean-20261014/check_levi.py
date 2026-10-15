#!/usr/bin/env python3
"""Independent exact tensor checker; imports no producer module."""
import argparse
from copy import deepcopy
from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path

BASELINE_HASH='7275abb3ecfc9b8c0efc4c437274229cec6be4245ae5674d69ef79df7b48c44d'
LABELS=['E12','E23','E13','E21','E32','E31','H1','H2']


def elementary(i,j):
    m=[[0]*3 for _ in range(3)];m[i][j]=1;return m


def matrix_sum(a,b,scale=1):
    return [[a[i][j]+scale*b[i][j] for j in range(3)] for i in range(3)]


V=[elementary(0,1),elementary(1,2),elementary(0,2),elementary(1,0),
   elementary(2,1),elementary(2,0),
   matrix_sum(elementary(0,0),elementary(1,1),-1),
   matrix_sum(elementary(1,1),elementary(2,2),-1)]


def commutator(a,b):
    return [[sum(a[i][k]*b[k][j]-b[i][k]*a[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def vcoordinates(a):
    values=[a[0][1],a[1][2],a[0][2],a[1][0],a[2][1],a[2][0],a[0][0],-a[2][2]]
    rebuilt=[[sum(values[k]*V[k][i][j] for k in range(8)) for j in range(3)] for i in range(3)]
    assert rebuilt==a,'sl3 coordinate error'
    return values


LOWERINGS=[[vcoordinates(commutator(V[f],v)) for v in V] for f in (3,4)]
WEIGHTS=[]
for j,v in enumerate(V):
    weight=[]
    for h in (6,7):
        action=vcoordinates(commutator(V[h],v))
        assert all(c==0 for k,c in enumerate(action) if k!=j)
        weight.append(action[j])
    WEIGHTS.append(tuple(weight))


def sum_vectors(terms):
    out={}
    for coefficient,vector in terms:
        for word,value in vector.items():
            out[word]=out.get(word,0)+coefficient*value
            if not out[word]: del out[word]
    return out


def tensor_bracket(a,b):
    terms=[]
    for w,c in a.items():
        for u,d in b.items():
            terms.extend([(c*d,{w+u:1}),(-c*d,{u+w:1})])
    return sum_vectors(terms)


def degree3_bracket(word):
    a,b,c=word
    if b<c:
        # [a,[b,c]], expanded directly, no recursive Lyndon conversion.
        terms=[(1,(a,b,c)),(-1,(a,c,b)),(-1,(b,c,a)),(1,(c,b,a))]
    else:
        # [[a,b],c].
        terms=[(1,(a,b,c)),(-1,(b,a,c)),(-1,(c,a,b)),(1,(c,b,a))]
    return sum_vectors((n,{w:1}) for n,w in terms)


def word_weight(w):
    return tuple(sum(WEIGHTS[j][i] for j in w) for i in range(2))


def cyclic_minimal(w):
    return all(w < w[k:]+w[:k] for k in range(1,len(w)))


def lowering(tensor,index):
    terms=[]
    for word,coefficient in tensor.items():
        for position,letter in enumerate(word):
            for replacement,value in enumerate(LOWERINGS[index][letter]):
                if value:
                    new=word[:position]+(replacement,)+word[position+1:]
                    terms.append((coefficient*value,{new:1}))
    return sum_vectors(terms)


def sparse_rank(vectors):
    pivots={}
    for vector in vectors:
        row={w:Fraction(c) for w,c in vector.items() if c}
        while row:
            pivot=min(row);coefficient=row[pivot]
            if pivot in pivots:
                row=sum_vectors([(1,row),(-coefficient,pivots[pivot])])
            else:
                pivots[pivot]={w:c/coefficient for w,c in row.items()}
                break
    return len(pivots)


def determinant_rational(rows):
    a=[[Fraction(x) for x in row] for row in rows];value=Fraction(1)
    assert all(len(row)==len(a) for row in a)
    for j in range(len(a)):
        p=next((i for i in range(j,len(a)) if a[i][j]),None)
        if p is None:return Fraction(0)
        if p!=j:a[j],a[p]=a[p],a[j];value=-value
        pivot=a[j][j];value*=pivot
        for i in range(j+1,len(a)):
            factor=a[i][j]/pivot
            for k in range(j+1,len(a)):a[i][k]-=factor*a[j][k]
            a[i][j]=0
    return value


def check_matrix(cert):
    assert cert['schema']=='sl3-free-lie-level3/1' and cert['field']=='Q'
    assert cert['basis']==LABELS
    words=[w for w in product(range(8),repeat=3) if cyclic_minimal(w)]
    sources=[w for w in words if word_weight(w)==(0,0)]
    targets=[[w for w in words if word_weight(w)==weight] for weight in [(-2,1),(1,-2)]]
    assert cert['source_words']==[list(w) for w in sources],'source basis differs'
    assert cert['target_words']==[[list(w) for w in group] for group in targets],'target basis differs'
    matrix=cert['matrix']
    assert len(matrix)==sum(map(len,targets)) and all(len(row)==len(sources) for row in matrix)
    assert all(type(x) is int for row in matrix for x in row)
    source_vectors=[degree3_bracket(w) for w in sources]
    offset=0
    for index,group in enumerate(targets):
        basis=[degree3_bracket(w) for w in group]
        for col,source in enumerate(source_vectors):
            described=sum_vectors((matrix[offset+row][col],v) for row,v in enumerate(basis))
            assert described==lowering(source,index),'lowering tensor identity failed'
        offset+=len(group)
    return sources,targets,source_vectors


def tree_tensor(tree):
    if type(tree) is int:
        assert 0<=tree<8
        return {(tree,):1},(tree,)
    assert isinstance(tree,list) and len(tree)==2
    left,lword=tree_tensor(tree[0]);right,rword=tree_tensor(tree[1])
    return tensor_bracket(left,right),lword+rword


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--baseline',type=Path,default=Path(__file__).resolve().parent.parent/'evidence/round2-uniform/parent-independent-check.json')
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite an acceptance receipt')
    cert=json.loads(args.certificate.read_text())
    sources,targets,source_vectors=check_matrix(cert)
    all_brackets=[];zero_brackets=[]
    for a,b,c in product(range(8),repeat=3):
        vector=tensor_bracket(tensor_bracket({(a,):1},{(b,):1}),{(c,):1})
        all_brackets.append(vector)
        if word_weight((a,b,c))==(0,0):zero_brackets.append(vector)
    full_rank=sparse_rank(all_brackets)
    source_rank=sparse_rank(source_vectors)
    zero_rank=sparse_rank(zero_brackets)
    assert full_rank==168 and source_rank==zero_rank==18
    # Every bracket of length three is a linear combination of the left-normed brackets.
    # They span the genuine free-Lie homogeneous component inside the tensor algebra.
    images=[{(i,)+w:c for i in (0,1) for w,c in lowering(v,i).items()} for v in source_vectors]
    image_rank=sparse_rank(images)
    assert image_rank==source_rank
    rows=cert['selected_rows']
    assert len(rows)==len(set(rows))==18 and all(type(r) is int and 0<=r<26 for r in rows)
    determinant=determinant_rational([cert['matrix'][r] for r in rows])
    assert determinant==cert['minor_determinant']==288
    negative=[]
    changed=deepcopy(cert);changed['matrix'][0][0]+=1
    try:check_matrix(changed)
    except AssertionError as error:negative.append({'mutation':'one lowering coefficient +1','rejected':True,'reason':str(error)})
    else:raise AssertionError('Broken lowering certificate accepted')
    changed=deepcopy(cert);changed['source_words'].pop()
    try:check_matrix(changed)
    except AssertionError as error:negative.append({'mutation':'omit one source basis vector','rejected':True,'reason':str(error)})
    else:raise AssertionError('Incomplete source accepted')
    individual=[sparse_rank(lowering(v,i) for v in source_vectors) for i in (0,1)]
    assert individual==[13,13]
    negative.append({'mutation':'retain only F1 (or only F2)','rejected_injectivity':True,'individual_ranks':individual,'source_dimension':18})
    terms=[]
    for entry in cert['degree4_primitive']:
        assert type(entry['coefficient']) is int and entry['coefficient']
        tensor,word=tree_tensor(entry['tree'])
        assert list(word)==entry['word'] and len(word)==4 and word_weight(word)==(0,0)
        terms.append((entry['coefficient'],tensor))
    witness=sum_vectors(terms)
    assert witness and all(not lowering(witness,i) for i in (0,1))
    assert sha(args.baseline)==BASELINE_HASH,'Inherited uniform-height7 receipt changed'
    baseline=json.loads(args.baseline.read_text())
    assert baseline['uniform_height7'] is True and baseline['uniform_height8'] is False
    result={'schema':'sl3-free-lie-level3-independent-check/1','status':'PASS',
        'full_lie_degree3_dimension':full_rank,'weight_zero_dimension':zero_rank,
        'joint_lowering_rank':image_rank,'selected_minor_determinant':int(determinant),
        'negative_controls':negative,
        'degree4_route_obstruction':{'bracket_terms':len(terms),'tensor_terms':len(witness),
            'nonzero':True,'weight':[0,0],'F1_zero':True,'F2_zero':True,
            'serre_quotient_survival_checked':False,'D3_checked':False,'counterexample':False},
        'baseline':{'path':str(args.baseline),'sha256':BASELINE_HASH,'uniform_height7':True},
        'certificate_sha256':sha(args.certificate),'checker_sha256':sha(Path(__file__)),
        'scope':'Exact finite Levi-module certificate; the coefficient-three family theorem also uses the written semisimplicity and first-defect argument.',
        'full_original_goal_solved':False,'lean_certificate_replay':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
