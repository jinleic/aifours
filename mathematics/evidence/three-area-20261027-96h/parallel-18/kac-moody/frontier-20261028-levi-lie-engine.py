#!/usr/bin/env python3
"""Exact level-n Serre quotient via the explicit fixed-Levi level-one module.

The higher-level freeness/source-isomorphism is a separately stated candidate,
not assumed accepted.  This engine is only a computational experiment for
its proof.  It retains both node-3 Serre ideals, all Levi descendants, and the
actual three quotient lowerings.  It never identifies the *preliminary*
reached-target obstruction with the K-quotient obstruction.
"""
import argparse
import importlib.util
import itertools
import json
from collections import deque
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lift', ROOT / 'frontier-20261028-lift-exact.py')
lift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lift)
spec2 = importlib.util.spec_from_file_location('matrix_units', ROOT / 'frontier-20261028-levi-level1-check.py')
mu = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(mu)

WEIGHTS = ((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
BASIS = [
    mu.unit(3,1), mu.add((-1,mu.unit(3,2))), mu.unit(2,1),
    mu.add((1,mu.unit(1,1)),(-1,mu.unit(3,3))),
    mu.add((1,mu.unit(1,1)),(-1,mu.unit(2,2))),
    mu.add((-1,mu.unit(1,2))), mu.add((-1,mu.unit(2,3))),
    mu.add((-2,mu.unit(1,3))),
]
LEVI = {'e1':mu.unit(1,2), 'e2':mu.unit(2,3), 'e12':mu.unit(1,3),
        'f1':mu.unit(2,1), 'f2':mu.unit(3,2)}


def coordinates(M):
    vals = [M.get((3,1),0),-M.get((3,2),0),M.get((2,1),0),
            -M.get((3,3),0),-M.get((2,2),0),-M.get((1,2),0),
            -M.get((2,3),0),-M.get((1,3),0)/Q(2)]
    assert mu.add(*[(c,b) for c,b in zip(vals,BASIS)]) == M
    return {i:Q(c) for i,c in enumerate(vals) if c}


ACTIONS = {g:[coordinates(mu.bracket(M,b)) for b in BASIS] for g,M in LEVI.items()}


def degree(word):
    return (sum(WEIGHTS[j][0] for j in word),sum(WEIGHTS[j][1] for j in word),len(word))


def all_words(target):
    a,b,n=target
    if a<0 or b<0 or n<0: return
    for w in itertools.product(range(8),repeat=n):
        if degree(w)==target: yield w


def lie_basis(target):
    return [(w,lift.lyndon_bracket(w)) for w in all_words(target) if lift.is_lyndon(w)]


def action_letter(g,j,r,s):
    if g=='h3': return {j:Q(2-r*WEIGHTS[j][0]-s*WEIGHTS[j][1])}
    return ACTIONS[g][j]


def levi_action(vector,g,r,s):
    out={}
    for word,c in vector.items():
        for k,j in enumerate(word):
            for new, coefficient in action_letter(g,j,r,s).items():
                w=word[:k]+(new,)+word[k+1:]
                out[w]=out.get(w,Q(0))+c*coefficient
    return {w:c for w,c in out.items() if c}


def local_f3(j,r,s):
    return ({'h3':-1},{'e1':-r},{'e2':-s},{'e12':-(r+s)},
            {'e12':-s},{},{},{})[j]


def lower3(vector,r,s):
    """All Jacobi terms obtained by moving each local g0 bracket right."""
    assert all(len(word)>=2 for word in vector)
    out={}; cartan_tail={}
    for word,c in vector.items():
        for k,j in enumerate(word):
            shorter=word[:k]+word[k+1:]
            for g,coefficient in local_f3(j,r,s).items():
                key=(shorter,g)
                cartan_tail[key]=cartan_tail.get(key,Q(0))+c*coefficient
                for ell in range(k+1,len(word)):
                    position=ell-1
                    for new,act in action_letter(g,word[ell],r,s).items():
                        w=shorter[:position]+(new,)+shorter[position+1:]
                        out[w]=out.get(w,Q(0))+c*coefficient*act
    assert not any(cartan_tail.values()), 'unexpected right degree-zero term'
    return {w:c for w,c in out.items() if c}


def delta(vector,r,s):
    out={}
    for i,g in enumerate(('f1','f2')):
        out.update({(i,w):c for w,c in levi_action(vector,g,r,s).items()})
    out.update({(2,w):c for w,c in lower3(vector,r,s).items()})
    return out


def seed(j,power):
    # (ad e3)^(power+1) e_j = -(ad v)^power (e_j . v).
    v=lift.letter(j)
    for _ in range(power): v=lift.bracket(lift.letter(0),v)
    return {w:-c for w,c in v.items()}


def ideal_bases(bound,r,s):
    spaces={}; queue=deque()
    def add(d,v):
        if not v or not lift.fits(d,bound): return
        assert all(degree(w)==d for w in v), ('incorrect graded action',d)
        area=spaces.setdefault(d,lift.Span())
        row=area.add(v)
        if row is not None: queue.append((d,row))
    for j,power in ((1,r),(2,s)):
        d=(*WEIGHTS[j],power+1)
        if lift.fits(d,bound): add(d,seed(j,power))
    while queue:
        d,v=queue.popleft()
        for i,g in enumerate(('e1','e2')):
            nd=list(d);nd[i]+=1
            if lift.fits(nd,bound): add(tuple(nd),levi_action(v,g,r,s))
        if d[2]<bound[2]:
            for j,(a,b) in enumerate(WEIGHTS):
                nd=(d[0]+a,d[1]+b,d[2]+1)
                if lift.fits(nd,bound): add(nd,lift.bracket(lift.letter(j),v))
    return spaces


def target_ideal(spaces,alpha):
    result=lift.Span()
    for i in range(3):
        d=list(alpha);d[i]-=1
        if min(d)<0: continue
        for row in spaces.get(tuple(d),lift.Span()).rows.values():
            result.add({(i,w):c for w,c in row.items()})
    return result


def run(alpha,r,s):
    source=lie_basis(alpha)
    ideals=ideal_bases(alpha,r,s)
    I=ideals.get(alpha,lift.Span())
    T=target_ideal(ideals,alpha)
    for row in I.rows.values():
        assert not T.reduce(delta(row,r,s)), 'ideal derivative escaped full target'
    D=[delta(v,r,s) for _,v in source]
    mod=[T.reduce(v) for v in D]
    source_dim=len(source)-len(I)
    modrank=lift.rank(mod)
    kernel=source_dim-modrank
    assert kernel>=0
    return {'degree':alpha,'r':r,'s':s,'free_M_source_dim':len(source),
            'node3_ideal_dim':len(I),'actual_S_source_dim':source_dim,
            'compressed_target_ideal_dim':len(T),'quotient_delta_rank':modrank,
            'actual_simultaneous_quotient_kernel_dim':kernel,
            'caution':'compressed-source L is not identified with preliminary-G L; kernel zero does imply original LIFT'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--a',type=int,required=True);p.add_argument('--b',type=int,required=True)
    p.add_argument('--n',type=int,default=4);p.add_argument('--r',type=int,required=True);p.add_argument('--s',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();alpha=(args.a,args.b,args.n)
    if min(args.a,args.b,args.r,args.s)<1 or not 2<=args.n<=4 or args.a>8 or args.b>8:
        p.error('bounded positive data: a,b<=8, n=2..4')
    result=run(alpha,args.r,args.s)
    dest=args.output.resolve()
    if dest.parent!=ROOT or not dest.name.startswith('frontier-20261028-') or dest.exists():
        p.error('new frontier-20261028-* file in owner root required')
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,sort_keys=True));print('WROTE',dest.name)


if __name__=='__main__':main()
