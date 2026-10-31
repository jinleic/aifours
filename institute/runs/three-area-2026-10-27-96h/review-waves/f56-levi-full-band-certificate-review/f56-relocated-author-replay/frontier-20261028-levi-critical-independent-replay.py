#!/usr/bin/env python3
"""Independent exact replay of the 64 Levi-critical quotient certificates.

No import of the Levi producer.  Constructs matrix-unit actions independently,
generates source/ideal spans by right-nested words and Gauss-Jordan, and
computes f3 on bracket trees recursively by Jacobi rather than by the
producer's tensor-word suffix algorithm.  Its scope depends on the separately
written free-Levi source theorem; this is not a formal proof checker.
"""
import importlib.util
import itertools
import json
from collections import deque
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ind',ROOT/'frontier-20261028-214-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)
WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))


def matunit(i,j):
    return tuple(tuple(Q(1 if a==i and b==j else 0) for b in range(3)) for a in range(3))


def lin(*terms):
    return tuple(tuple(sum(Q(c)*M[i][j] for c,M in terms) for j in range(3)) for i in range(3))


def mmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mbracket(A,B):return lin((1,mmul(A,B)),(-1,mmul(B,A)))


BASIS=(matunit(2,0),lin((-1,matunit(2,1))),matunit(1,0),
       lin((1,matunit(0,0)),(-1,matunit(2,2))),
       lin((1,matunit(0,0)),(-1,matunit(1,1))),
       lin((-1,matunit(0,1))),lin((-1,matunit(1,2))),lin((-2,matunit(0,2))))
OPS={'e1':matunit(0,1),'e2':matunit(1,2),'e12':matunit(0,2),
     'f1':matunit(1,0),'f2':matunit(2,1)}


def coords(A):
    c=(A[2][0],-A[2][1],A[1][0],-A[2][2],-A[1][1],-A[0][1],-A[1][2],-A[0][2]/2)
    assert lin(*[(x,m) for x,m in zip(c,BASIS)])==A
    return {str(i):x for i,x in enumerate(c) if x}


ACTION={g:tuple(coords(mbracket(op,b)) for b in BASIS) for g,op in OPS.items()}


def deg(word):return (sum(WEIGHTS[int(x)][0] for x in word),sum(WEIGHTS[int(x)][1] for x in word),len(word))


def words_at(degree):
    a,b,n=degree
    if min(degree)<0:return []
    return [''.join(map(str,w)) for w in itertools.product(range(8),repeat=n)
            if sum(WEIGHTS[x][0] for x in w)==a and sum(WEIGHTS[x][1] for x in w)==b]


@lru_cache(maxsize=None)
def source_basis(degree):
    return ind.ReducedSpace(ind.nested(w) for w in words_at(degree) if w)


@lru_cache(maxsize=None)
def lyndon_words(degree):
    return tuple(w for w in words_at(degree) if w and ind.lyndon(w))


def l_action_letter(g,j,r,s):
    if g=='h3':
        a,b=WEIGHTS[int(j)]; q=Q(2-r*a-s*b)
        return {j:q} if q else {}
    return ACTION[g][int(j)]


def act(vector,g,r,s):
    out={}
    for word,c in vector.items():
        for i,j in enumerate(word):
            for target,coefficient in l_action_letter(g,j,r,s).items():
                w=word[:i]+target+word[i+1:]
                out[w]=out.get(w,Q(0))+c*coefficient
    return {w:c for w,c in out.items() if c}


def g_action(vector,gdict,r,s):
    out={}
    for g,c in gdict.items():ind.add_scaled(out,act(vector,g,r,s),Q(c))
    return out


def local(j,r,s):
    return ({'h3':-1},{'e1':-r},{'e2':-s},{'e12':-(r+s)},
            {'e12':-s},{},{},{})[int(j)]


@lru_cache(maxsize=None)
def tree_d3(word,r,s):
    assert len(word)>=2 and ind.lyndon(word)
    split=next(i for i in range(1,len(word)) if ind.lyndon(word[i:]))
    left,right=word[:split],word[split:]
    L,R=ind.standard_bracket(left),ind.standard_bracket(right)
    out={}
    if len(left)==1:ind.add_scaled(out,g_action(R,local(left,r,s),r,s),1)
    else:ind.add_scaled(out,ind.bracket(tree_d3(left,r,s),R),1)
    if len(right)==1:ind.add_scaled(out,g_action(L,local(right,r,s),r,s),-1)
    else:ind.add_scaled(out,ind.bracket(L,tree_d3(right,r,s)),1)
    return out


def d3(vector,degree,r,s):
    rem={w:Q(c) for w,c in vector.items() if c};out={}
    for word in lyndon_words(degree):
        coefficient=rem.get(word,Q(0))
        if coefficient:
            ind.add_scaled(rem,ind.standard_bracket(word),-coefficient)
            ind.add_scaled(out,tree_d3(word,r,s),coefficient)
    assert not rem,('non-Lie vector in independent decomposition',degree)
    return out


def delta(vector,degree,r,s):
    out={}
    for i,g in enumerate(('f1','f2'),1):
        out.update({f'{i}:{w}':c for w,c in act(vector,g,r,s).items()})
    out.update({f'3:{w}':c for w,c in d3(vector,degree,r,s).items()})
    return out


def seed(index,power):
    v=ind.e(index)
    for _ in range(power):v=ind.bracket(ind.e(0),v)
    return {w:-c for w,c in v.items()}


def fits(a,b):return all(x<=y for x,y in zip(a,b))


def ideal_spaces(bound,r,s):
    spaces={};queue=deque()
    def add(degree,v):
        if not v or not fits(degree,bound):return
        assert all(deg(w)==degree for w in v)
        area=spaces.setdefault(degree,ind.ReducedSpace())
        if area.insert(v):queue.append((degree,v))
    for index,power in ((1,r),(2,s)):
        d=(*WEIGHTS[index],power+1)
        if fits(d,bound):add(d,seed(index,power))
    while queue:
        d,v=queue.popleft()
        for i,g in enumerate(('e1','e2')):
            nd=list(d);nd[i]+=1;nd=tuple(nd)
            if fits(nd,bound):add(nd,act(v,g,r,s))
        if d[2]<bound[2]:
            for j,(a,b) in enumerate(WEIGHTS):
                nd=(d[0]+a,d[1]+b,d[2]+1)
                if fits(nd,bound):add(nd,ind.bracket(ind.e(j),v))
    return spaces


def target_space(spaces,degree):
    rows=[]
    for i in range(3):
        d=list(degree);d[i]-=1
        if min(d)<0:continue
        for row in spaces.get(tuple(d),ind.ReducedSpace()).pivots.values():
            rows.append({f'{i+1}:{w}':c for w,c in row.items()})
    return ind.ReducedSpace(rows)


def combine(vectors,coefficients):
    out={}
    for j,c in coefficients.items():ind.add_scaled(out,vectors[int(j)],Q(c))
    return out


def restrict(v,prefixes):return {k:c for k,c in v.items() if k.startswith(prefixes)}


def replay(degree,case):
    rc,sc=case['r_class'],case['s_class']
    r0=4 if rc=='>=4' else rc;s0=4 if sc=='>=4' else sc
    spaces=ideal_spaces(degree,r0,s0)
    ideal=spaces.get(degree,ind.ReducedSpace());source=source_basis(degree)
    for row in ideal.pivots.values():assert not source.remainder(row)
    m=case['source_dim'];assert len(source)-len(ideal)==m
    if case['status']=='ZERO_SOURCE':
        assert m==0
        return {'r_class':rc,'s_class':sc,'status':'PASS_ZERO_SOURCE','determinants':0}
    basis=[ind.standard_bracket(w) for w in case['source_words']]
    combined=ind.ReducedSpace(ideal.pivots.values())
    for v in basis:
        assert not source.remainder(v)
        assert combined.insert(v)
    assert len(combined)==len(source)
    target=target_space(spaces,degree)
    def projected(v,r,s):return target.remainder(delta(v,degree,r,s))
    dirs=[(r0,s0)]
    if rc=='>=4':dirs.append((r0+1,s0))
    if sc=='>=4':dirs.append((r0,s0+1))
    for r,s in dirs:
        for v in ideal.pivots.values():assert not projected(v,r,s),('unstableideal',degree,rc,sc)
    hor=[restrict(projected(v,r0,s0),('1:','2:')) for v in basis]
    k=case['horizontal_kernel_dim'];assert m-len(ind.ReducedSpace(hor))==k
    if case['status']=='ZERO_HORIZONTAL_KERNEL':
        assert k==0
        return {'r_class':rc,'s_class':sc,'status':'PASS_ZERO_HORIZONTAL','determinants':0}
    coeffs=case['horizontal_kernel_coefficients'];assert len(coeffs)==k
    assert len(ind.ReducedSpace([{int(j):Q(c) for j,c in row.items()} for row in coeffs]))==k
    vectors=[combine(basis,row) for row in coeffs]
    for v in vectors:
        for r,s in dirs:assert not restrict(projected(v,r,s),('1:','2:'))
    rows=['3:'+w for w in case['target_f3_word_pivots']]
    assert len(rows)==len(set(rows))==k
    p=case['determinant_coefficients']
    assert next(Q(t['coefficient']) for t in p if t['x_power']==0 and t['y_power']==0)!=0
    assert all(Q(t['coefficient'])>0 for t in p) or all(Q(t['coefficient'])<0 for t in p)
    assert all(t['x_power']<=k and t['y_power']<=k for t in p)
    xs=range(k+1) if rc=='>=4' else range(1)
    ys=range(k+1) if sc=='>=4' else range(1)
    count=0
    for x,y in itertools.product(xs,ys):
        r=r0+x if rc=='>=4' else r0;s=s0+y if sc=='>=4' else s0
        cols=[restrict(projected(v,r,s),('3:',)) for v in vectors]
        matrix=[[cols[j].get(row,Q(0)) for j in range(k)] for row in rows]
        assert ind.determinant(matrix)==ind.eval_polynomial(p,x,y),('minor mismatch',degree,rc,sc,x,y)
        count+=1
    return {'r_class':rc,'s_class':sc,'source_dim':m,'horizontal_kernel_dim':k,
            'status':'PASS_FULL_SPAN_TREE_JACOBI_GRID_SIGN','determinants':count}


def main():
    original=json.loads((ROOT/'frontier-20261028-levi-critical-minors-v1.json').read_text(encoding='utf-8'))
    replacement=json.loads((ROOT/'frontier-20261028-levi-critical-alternates-v1.json').read_text(encoding='utf-8'))
    alt={(tuple(x['degree']),x['case']['r_class'],x['case']['s_class']):x['case'] for x in replacement['cases']}
    assert len(alt)==3
    results=[]
    for block in original['degrees']:
        degree=tuple(block['degree'])
        cases=[alt.get((degree,c['r_class'],c['s_class']),c) for c in block['cases']]
        assert len(cases)==16
        checked=[replay(degree,c) for c in cases]
        results.append({'degree':degree,'cases':checked,'all_classes_passed':True,
                        'determinants':sum(x['determinants'] for x in checked)})
        print('PASS',degree,'16 classes',results[-1]['determinants'],'determinants',flush=True)
    out=ROOT/'frontier-20261028-levi-critical-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degrees':results,'total_classes':64,
                               'determinants':sum(x['determinants'] for x in results),
                               'scope':'independent matrix units, nested source/ideal spans, tree-Jacobi f3 and exact polynomial interpolation',
                               'conditional_on_free_Levi_source_and_earlier_PBW':True,
                               'not_a_formal_proof_or_external_review':True},indent=2)+'\n',encoding='utf-8')
    print('PASS all64 classes,',sum(x['determinants'] for x in results),'determinants;',out.name)


if __name__=='__main__':main()
