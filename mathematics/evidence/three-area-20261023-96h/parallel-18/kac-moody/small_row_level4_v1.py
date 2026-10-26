"""Exact actual-quotient level-four assay. SOURCE ONLY until a named parent GO.

One process; standard library; no old checker imports, network, or subprocesses.
Sixteen row cells {1,2,3,4+} squared, four residual primitive degrees.
Produces explicit rational tensor/ideal bases, original-row affine maps, and
positive-coefficient determinant identities when found. Missing certificates
are UNKNOWN, never UNSAT or a claim of quotient equality. No formal proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
from itertools import product
import json
import os
from pathlib import Path
import random
import sys
import time

ROOT = Path(__file__).resolve().parent
MATRICES = (
    (0,1,0,0,0,0,0,0,0), (0,0,0,0,0,1,0,0,0),
    (0,0,1,0,0,0,0,0,0), (0,0,0,1,0,0,0,0,0),
    (0,0,0,0,0,0,0,1,0), (0,0,0,0,0,0,1,0,0),
    (1,0,0,0,-1,0,0,0,0), (0,0,0,0,1,0,0,0,-1),
)
DEGREES = ((2,1),(1,2),(2,2),(0,1),(1,0),(0,0),(1,1),(1,1))
CELLS = tuple(product((1,2,3,4), repeat=2))
TARGETS = ((2,2),(3,2),(2,3),(3,3))
DEADLINE = float('inf')


class CooperativeDeadline(Exception):
    pass


def tick():
    if time.monotonic() >= DEADLINE:
        raise CooperativeDeadline('Internal cooperative scientific deadline')


def clean(v):
    return {w:c for w,c in v.items() if c}


def add(a,b,scale=Q(1)):
    out = dict(a)
    for w,c in b.items():
        out[w] = out.get(w,Q(0)) + scale*c
        if not out[w]:
            del out[w]
    return out


def bracket(a,b):
    out = defaultdict(Q)
    for u,c in a.items():
        for v,d in b.items():
            out[u+v] += c*d
            out[v+u] -= c*d
    return clean(out)


@lru_cache(None)
def dynkin(word):
    if len(word) == 1:
        return {word:Q(1)}
    return bracket({(word[0],):Q(1)}, dynkin(word[1:]))


@lru_cache(None)
def matrix_action(actor,letter):
    a,b = MATRICES[actor],MATRICES[letter]
    c = [sum(a[3*i+k]*b[3*k+j]-b[3*i+k]*a[3*k+j]
             for k in range(3)) for i in range(3) for j in range(3)]
    v = (c[1],c[5],c[2],c[3],c[7],c[6],c[0],-c[8])
    assert all(sum(x*m[i] for x,m in zip(v,MATRICES)) == c[i]
               for i in range(9)), 'Incorrect traceless-matrix coordinates'
    return {i:Q(x) for i,x in enumerate(v) if x}


def action(actor,p):
    out = defaultdict(Q)
    for word,c in p.items():
        for pos,letter in enumerate(word):
            for new,d in matrix_action(actor,letter).items():
                out[word[:pos]+(new,)+word[pos+1:]] += c*d
    return clean(out)


def reduce(v,basis):
    out = dict(v)
    for pivot,row in sorted(basis.items()):
        if pivot in out:
            out = add(out,row,-out[pivot])
    return out


def insert(v,basis):
    tick()
    v = reduce(v,basis)
    if not v:
        return False
    pivot = min(v)
    scale = v[pivot]
    basis[pivot] = {w:c/scale for w,c in v.items()}
    return True


def span(vectors):
    basis = {}
    for v in vectors:
        insert(v,basis)
    return basis


def nullspace(columns):
    n = len(columns)
    words = sorted(set().union(*(set(v) for v in columns))) if columns else []
    pivots = {}
    for word in words:
        insert({j:columns[j][word] for j in range(n) if word in columns[j]},pivots)
    vectors = []
    for free in sorted(set(range(n))-set(pivots)):
        x = [Q(0)]*n
        x[free] = Q(1)
        for p,row in sorted(pivots.items(),reverse=True):
            x[p] = -sum(c*x[j] for j,c in row.items() if j != p)
        vectors.append(x)
    return vectors


def combination(coefficients,vectors):
    out = {}
    for c,v in zip(coefficients,vectors):
        if c:
            out = add(out,v,c)
    return out


@lru_cache(None)
def lie_basis(a,b,k):
    if a < 0 or b < 0 or k < 1:
        return {}
    vectors = []
    for word in product(range(8),repeat=k):
        tick()
        if (sum(DEGREES[i][0] for i in word),
            sum(DEGREES[i][1] for i in word)) == (a,b):
            vectors.append(dynkin(word))
    return span(vectors)


@lru_cache(None)
def free_primitives(a,b):
    basis = list(lie_basis(a,b,4).values())
    columns = []
    for v in basis:
        columns.append({(actor,w):c for actor in (3,4)
                        for w,c in action(actor,v).items()})
    p = [combination(c,basis) for c in nullspace(columns)]
    for v in p:
        assert not action(3,v) and not action(4,v)
        assert not reduce(v,lie_basis(a,b,4))
    assert len(span(p)) == len(p)
    return p


@lru_cache(None)
def serre_generator(q,j):
    v = {(5,):Q(1)}
    out = action(j,v)  # j=0,1 denotes e1,e2; overall Serre sign is immaterial.
    for _ in range(q):
        out = bracket(v,out)
    assert out and not action(3,out) and not action(4,out)
    return out


@lru_cache(None)
def ideal(a,b,k,r,s):
    """Exact positive ideal, not a selected set of relation consequences.

    E1/E2 and all V brackets generate ideal closure in n_J+ semidirect L(V).
    Degree decreases strictly in a+b+k on every recursive call.
    A cell value4 denotes an entry>=4 and adds no Serre generator by level4.
    """
    if a < 0 or b < 0 or k < 2:
        return {}
    tick()
    out = {}
    for p in ideal(a-1,b,k,r,s).values():
        insert(action(0,p),out)
    for p in ideal(a,b-1,k,r,s).values():
        insert(action(1,p),out)
    for letter,(da,db) in enumerate(DEGREES):
        for p in ideal(a-da,b-db,k-1,r,s).values():
            insert(bracket({(letter,):Q(1)},p),out)
    if r <= 3 and (a,b,k) == (1,0,r+1):
        insert(serre_generator(r,0),out)
    if s <= 3 and (a,b,k) == (0,1,s+1):
        insert(serre_generator(s,1),out)
    assert all(not reduce(v,lie_basis(a,b,k)) for v in out.values())
    return out


def lowering(p):
    """Original row (-r,-s,2), associative deletion, slots constant/r/s.

    Leaf actors: -s e2, r e1, -h3, -s[e1,e2], -r[e1,e2].
    Their labels are independently derived from the printed Chevalley brackets.
    Terminal actors must cancel, not be discarded.
    """
    leaf = {3:(1,2,Q(-1)), 4:(0,1,Q(1)), 5:(-1,0,Q(-1)),
            6:(2,2,Q(-1)), 7:(2,1,Q(-1))}
    out = [defaultdict(Q) for _ in range(3)]
    terminal = defaultdict(Q)
    for word,c in p.items():
        for pos,letter in enumerate(word):
            if letter not in leaf:
                continue
            actor,slot,d = leaf[letter]
            deleted = word[:pos]+word[pos+1:]
            terminal[deleted,actor,slot] += c*d
            for later in range(pos+1,len(word)):
                if actor == -1:
                    a,b = DEGREES[word[later]]
                    for j,value in enumerate((2,-a,-b)):
                        out[j][deleted] += c*d*value
                else:
                    for new,value in matrix_action(actor,word[later]).items():
                        replaced = deleted[:later-1]+(new,)+deleted[later:]
                        out[slot][replaced] += c*d*value
    assert not clean(terminal), 'Uncancelled terminal local actor'
    return tuple(clean(v) for v in out)


def in_cell(images,r,s):
    c,rr,ss = images
    constant = add(add(c,rr,Q(r)),ss,Q(s))
    return constant, rr if r == 4 else {}, ss if s == 4 else {}


def quotient_image(p,a,b,r,s):
    images = in_cell(lowering(p),r,s)
    target = ideal(a,b,3,r,s)
    return tuple(reduce(v,target) for v in images)


def poly_mul(a,b):
    out = defaultdict(Q)
    for (i,j),c in a.items():
        for (k,l),d in b.items():
            out[i+k,j+l] += c*d
    return clean(out)


def determinant(matrix):
    n = len(matrix)
    @lru_cache(None)
    def rec(row,columns):
        tick()
        if not columns:
            return {(0,0):Q(1)}
        out = {}
        for position,col in enumerate(columns):
            if matrix[row][col]:
                term = poly_mul(matrix[row][col],
                                rec(row+1,columns[:position]+columns[position+1:]))
                out = add(out,term,Q((-1)**position))
        return out
    return rec(0,tuple(range(n)))


def selected_rows(matrix,order):
    pivots,chosen = {},[]
    n = len(matrix[0]) if matrix else 0
    for row in order:
        if insert({j:p.get((0,0),Q(0)) for j,p in enumerate(matrix[row])
                   if p.get((0,0),Q(0))},pivots):
            chosen.append(row)
        if len(chosen) == n:
            return chosen
    return None


def encoded(v):
    return [[list(w) if isinstance(w,tuple) else w,str(c)] for w,c in sorted(v.items())]


def dynkin_identity(v,k):
    result = {}
    for w,c in v.items():
        result = add(result,dynkin(w),c)
    return result == {w:k*c for w,c in v.items()}


def controls():
    v = {(5,):Q(1)}
    u,w = action(0,v),action(1,v)
    assert lowering(bracket(v,u)) == ({i:-2*c for i,c in u.items()},
                                      {i:2*c for i,c in u.items()}, {})
    assert lowering(bracket(v,w)) == ({i:-2*c for i,c in w.items()}, {},
                                      {i:2*c for i,c in w.items()})
    p = next(x for x in free_primitives(2,2) if x)
    assert dynkin_identity(p,4)
    bad = dict(p)
    first = min(bad)
    bad[first] += 1
    assert not dynkin_identity(clean(bad),4), 'Altered source tensor accepted'
    bad_target = {(5,5,5):Q(1)}
    assert not dynkin_identity(bad_target,3), 'Non-Lie target accepted'
    return {'original_row_t1_t2_identities':True,
            'altered_source_tensor_rejected':True,
            'non_Lie_target_rejected':True}


def one_record(r,s,a,b):
    tick()
    I4 = ideal(a,b,4,r,s)
    I3 = ideal(a,b,3,r,s)
    L4,L3 = lie_basis(a,b,4),lie_basis(a,b,3)
    for p in I4.values():
        assert all(not v for v in quotient_image(p,a,b,r,s)), 'Ideal not lowering-stable'
        assert not reduce(action(3,p),ideal(a-1,b,4,r,s))
        assert not reduce(action(4,p),ideal(a,b-1,4,r,s))
    primitive = free_primitives(a,b)
    quotient_span,representatives = {},[]
    for p in primitive:
        assert dynkin_identity(p,4)
        if insert(reduce(p,I4),quotient_span):
            representatives.append(p)
    # Exact lowest-space lifting is the WRITTEN complete-reducibility lemma,
    # not an unproved claim that reduction of a primitive remains primitive.
    images = [quotient_image(p,a,b,r,s) for p in representatives]
    for triple in images:
        for component in triple:
            assert not reduce(component,L3), 'Lowering target not a genuine Lie element'
    words = sorted(set().union(*(set(v) for triple in images for v in triple))) if images else []
    matrix = [[clean({(0,0):im[0].get(w,Q(0)),(1,0):im[1].get(w,Q(0)),
                      (0,1):im[2].get(w,Q(0))}) for im in images] for w in words]
    n = len(representatives)
    witness = None
    if n == 0:
        witness = {'rows':[],'determinant':[[[0,0],'1']], 'orientation':1}
    else:
        rng = random.Random(20261023+1000*r+100*s+10*a+b)
        for attempt in range(24):
            order = list(range(len(words)))
            if attempt == 1:
                order.reverse()
            elif attempt > 1:
                rng.shuffle(order)
            chosen = selected_rows(matrix,order)
            if chosen is None:
                break
            polynomial = determinant([matrix[i] for i in chosen])
            constant = polynomial.get((0,0),Q(0))
            if constant and all(c*constant > 0 for c in polynomial.values()):
                witness = {'rows':[list(words[i]) for i in chosen],
                           'determinant':encoded(polynomial),
                           'orientation':1 if constant > 0 else -1,
                           'attempt':attempt}
                break
    return {'cell':[r,s], 'open_entry_value':4,
            'degree':[a,b,4], 'free_dimensions':[len(L4),len(L3)],
            'ideal_dimensions':[len(I4),len(I3)],
            'free_primitive_dimension':len(primitive),
            'actual_quotient_primitive_dimension':n,
            'source_ideal':[encoded(p) for p in I4.values()],
            'target_ideal':[encoded(p) for p in I3.values()],
            'primitive_representatives':[encoded(p) for p in representatives],
            'quotient_affine_images':[[encoded(v) for v in im] for im in images],
            'positive_coefficient_minor':witness,
            'status':'CERTIFICATE_CANDIDATE' if witness else 'UNKNOWN_NO_POSITIVE_MINOR'}


def main():
    global DEADLINE
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    if not 1 <= args.seconds <= 900:
        parser.error('One-shot internal bound must be between1 and900 seconds')
    output = args.output.resolve()
    if ROOT not in output.parents or output == ROOT:
        parser.error('All output must be a fresh subdirectory of exact owned root')
    output.mkdir(exist_ok=False)
    started_mono,started_unix = time.monotonic(),time.time()
    DEADLINE = started_mono+args.seconds
    identity = {'pid':os.getpid(),'pgid':os.getpgid(0),'cwd':os.getcwd(),
                'argv':sys.argv,'interpreter':sys.executable,
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'interpreter_sha256':hashlib.sha256(Path(sys.executable).read_bytes()).hexdigest(),
                'observed_start_unix':started_unix}
    with (output/'launch.json').open('x') as f:
        json.dump(identity,f,indent=2)
    records,checks,error = [],None,None
    try:
        checks = controls()
        for r,s in CELLS:
            for a,b in TARGETS:
                record = one_record(r,s,a,b)
                with (output/f'cell-{r}-{s}-degree-{a}-{b}-4.json').open('x') as f:
                    json.dump(record,f,indent=2)
                records.append({key:record[key] for key in (
                    'cell','degree','actual_quotient_primitive_dimension','status')})
                print(json.dumps(records[-1]),flush=True)
        expected = {(r,s,a,b) for r,s in CELLS for a,b in TARGETS}
        actual = {tuple(x['cell'])+tuple(x['degree'][:2]) for x in records}
        assert actual == expected and len(records) == len(expected)
        assert {tuple(x['cell'])+tuple(x['degree'][:2]) for x in records[:-1]} != expected
        checks['missing_cell_rejected'] = True
    except CooperativeDeadline as exc:
        error = {'type':'CooperativeDeadline','detail':str(exc)}
    except Exception as exc:
        error = {'type':type(exc).__name__,'detail':str(exc)}
    status = ('COMPLETE_CERTIFICATE_CANDIDATES' if len(records) == 64 and
              all(r['status'] == 'CERTIFICATE_CANDIDATE' for r in records) and not error
              else 'UNKNOWN')
    receipt = {'status':status,'records':records,'controls':checks,'error':error,
               'identity':identity,'observed_end_unix':time.time(),
               'elapsed_seconds':time.monotonic()-started_mono,
               'full_book_problem_solved':False,'formal_proof':False,
               'interpretation':'Exact certificates need separate reconstruction and written quotient bridge; UNKNOWN is not a counterexample.'}
    with (output/'settlement.json').open('x') as f:
        json.dump(receipt,f,indent=2)
    print(json.dumps({'status':status,'records':len(records),'error':error}),flush=True)
    return 0 if status == 'COMPLETE_CERTIFICATE_CANDIDATES' else 2


if __name__ == '__main__':
    raise SystemExit(main())
