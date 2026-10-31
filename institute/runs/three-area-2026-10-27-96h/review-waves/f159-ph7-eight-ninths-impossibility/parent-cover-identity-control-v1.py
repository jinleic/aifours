#!/usr/bin/env python3
"""Nonblind parent exact control for the geometric cycle-cover identity.

Own stdlib rational determinants at eight distinct arguments certify each
DEGREE-SEVEN polynomial identity on these explicit fixtures only. Includes
virtual and disjoint-extra-cycle mutation checks. No author/reviewer imports.
Also directly exercises the retained PH8 endpoint as an actual PH pair.
"""
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
import sys
import time
from fractions import Fraction as Q

HERE = pathlib.Path(__file__).resolve().parent
START = time.monotonic()

class Invalid(Exception):
    pass

def need(ok, reason):
    if not ok:
        raise Invalid(reason)

def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()

def sha(b):
    return hashlib.sha256(b).hexdigest()

def determinant(matrix):
    a = [list(map(Q,row)) for row in matrix]
    n = len(a)
    answer = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k],a[pivot]=a[pivot],a[k]
            answer = -answer
        value = a[k][k]
        answer *= value
        for i in range(k+1,n):
            factor = a[i][k]/value
            for j in range(k+1,n):
                a[i][j] -= factor*a[k][j]
    return answer

def solve(a,b):
    n = len(a)
    rows = [list(map(Q,a[i]))+[Q(b[i])] for i in range(n)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if rows[i][k]),None)
        need(pivot is not None,'SINGULAR_CONTROL')
        rows[k],rows[pivot]=rows[pivot],rows[k]
        value=rows[k][k]
        rows[k]=[x/value for x in rows[k]]
        for i in range(n):
            if i!=k:
                factor=rows[i][k]
                rows[i]=[x-factor*y for x,y in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]

def root(value):
    a,b=math.isqrt(value.numerator),math.isqrt(value.denominator)
    need(a*a==value.numerator and b*b==value.denominator,'NONSQUARE_FIXTURE')
    return Q(a,b)

def symmetrize(g):
    n=len(g)
    return [[g[i][i] if i==j else root(g[i][j]*g[j][i]) for j in range(n)] for i in range(n)]

def extras(g,s):
    """Enumerate cyclic permutations up to rotation, then pair reversals."""
    n=len(g)
    result=[]
    used=set()
    for k in range(3,n+1):
        for vertices in itertools.combinations(range(n),k):
            first=vertices[0]
            for rest in itertools.permutations(vertices[1:]):
                seq=(first,)+rest
                edges=tuple((seq[i],seq[(i+1)%k]) for i in range(k))
                weight=math.prod(g[i][j] for i,j in edges)
                if not weight:
                    continue
                reversed_weight=math.prod(g[j][i] for i,j in edges)
                if not reversed_weight:
                    result.append((frozenset(vertices),weight,'oneway'))
                    continue
                key=frozenset(frozenset((i,j)) for i,j in edges)
                if key in used:
                    continue
                used.add(key)
                symmetric_weight=math.prod(s[i][j] for i,j in edges)
                omega=weight+reversed_weight-2*symmetric_weight
                need(omega>=0,'NEGATIVE_OMEGA')
                if omega:
                    result.append((frozenset(vertices),omega,'virtual'))
    return result

def resolvent_det(matrix, y, keep):
    return determinant([[Q(y)-matrix[i][j] if i==j else -matrix[i][j] for j in keep] for i in keep])

def fixture():
    g=[[Q(0) for _ in range(7)] for _ in range(7)]
    # A virtual bidirected triangle on 0,1,2, disjoint from a one-way triangle.
    for i,j in ((0,1),(1,2),(2,0)):
        g[i][j]=Q(1)
        g[j][i]=Q(4)
    for i,j in ((3,4),(4,5),(5,3),(2,3),(5,6),(6,0)):
        g[i][j]=Q(1)
    for i in range(7):
        g[i][i]=-sum(g[i])
    return g

def identity_fixture(g):
    n=len(g)
    universe=frozenset(range(n))
    s=symmetrize(g)
    cycles=extras(g,s)
    disjoint=[(a,b) for a,b in itertools.combinations(cycles,2) if not(a[0]&b[0])]
    need(any(c[2]=='virtual' for c in cycles),'NO_VIRTUAL_CYCLE_FIXTURE')
    need(disjoint,'NO_DISJOINT_CYCLE_FIXTURE')
    point_results=[]
    mutation_virtual=False
    mutation_disjoint=False
    for y in range(1,9):
        cache={}
        def minor(removed):
            kept=tuple(sorted(universe-removed))
            if kept not in cache:
                cache[kept]=resolvent_det(s,y,kept)
            return cache[kept]
        base=minor(frozenset())
        singles=sum((weight*minor(vertices) for vertices,weight,kind in cycles),Q(0))
        pairs=sum((a[1]*b[1]*minor(a[0]|b[0]) for a,b in disjoint),Q(0))
        lhs=resolvent_det(g,y,tuple(range(n)))
        rhs=base-singles+pairs
        need(lhs==rhs,'FULL_COVER_IDENTITY')
        without_virtual=base-sum((w*minor(v) for v,w,k in cycles if k!='virtual'),Q(0))
        without_virtual+=sum((a[1]*b[1]*minor(a[0]|b[0]) for a,b in disjoint if a[2]!='virtual' and b[2]!='virtual'),Q(0))
        mutation_virtual |= lhs!=without_virtual
        mutation_disjoint |= lhs!=base-singles
        point_results.append({'argument':y,'determinant':str(lhs),'residual':'0'})
    need(mutation_virtual,'MUTATION_VIRTUAL_NOT_DETECTED')
    need(mutation_disjoint,'MUTATION_DISJOINT_NOT_DETECTED')
    return {'vertices':n,'extra_cycles':len(cycles),'virtual_cycles':sum(k=='virtual' for _,_,k in cycles),
            'disjoint_extra_pairs':len(disjoint),'degree_bound':7,'distinct_exact_arguments':point_results,
            'virtual_omission_rejected':mutation_virtual,'disjoint_term_omission_rejected':mutation_disjoint}

def mul(left,right):
    out=[Q(0)]*(len(left)+len(right)-1)
    for i,x in enumerate(left):
        for j,y in enumerate(right):
            out[i+j]+=x*y
    return out

def horner(poly,x):
    value=Q(0)
    for coefficient in reversed(poly):
        value=value*x+coefficient
    return value

def ph8_control(c,d):
    eta=d/3
    lam=c+4*eta
    hidden=[Q(28),Q(26),Q(8),Q(1)]
    visible=mul([-4,1],mul([9,-2,1],[9,-2,1]))
    prod=mul(visible,hidden)
    need(prod==list(map(Q,[-9072,-2124,-214,-684,-3,0,0,0,1])),'PH8_FACTOR_IDENTITY')
    coeff=[prod[i]*eta**(8-i) for i in range(9)]
    f=[-coeff[8-j] for j in range(1,9)]
    need(all(x>=0 for x in f) and f[-1]>0,'PH8_FEEDBACK')
    t=[[Q(0) for _ in range(8)] for _ in range(8)]
    for i in range(8):
        t[i][i]=-lam
        if i<7:
            t[i][i+1]=lam
    for j in range(7):
        t[7][j]=f[7-j]/lam**(7-j)
    r=[hidden[i]*eta**(3-i) for i in range(4)]
    d0=horner(r,lam)
    alpha=[r[i]*lam**i/d0 for i in range(4)]+[Q(0)]*4
    omega=[-sum(row) for row in t]
    need(sum(alpha)==1 and min(alpha)>=0,'PH8_ALPHA')
    need(all(omega[i]==0 for i in range(7)) and omega[-1]>0,'PH8_ROW_SUMS')
    a=c+d
    b2=Q(8,9)*d*d
    k=c*(a*a+b2)**2
    need(omega[-1]==k*d0/lam**7,'PH8_EXIT')
    points=[]
    for s in (Q(0),Q(1),Q(2),Q(7,3)):
        system=[[s-t[i][j] if i==j else -t[i][j] for j in range(8)] for i in range(8)]
        vector=solve(system,omega)
        actual=sum(x*y for x,y in zip(alpha,vector))
        expected=k/((s+c)*((s+a)**2+b2)**2)
        need(actual==expected,'PH8_TRANSFER')
        wrong=sum(x*y for x,y in zip(alpha[1:]+alpha[:1],vector))
        points.append({'s':str(s),'value':str(actual),'wrong_initial_order_detected':wrong!=expected})
    need(any(x['wrong_initial_order_detected'] for x in points),'PH8_NEGATIVE_INITIAL_CONTROL')
    return {'c':str(c),'d':str(d),'alpha':list(map(str,alpha)),'exit':list(map(str,omega)),'points':points,
            'interpretation':'Exact actual PH-pair fixture; Hurwitz for the full parameter family follows from the separately written factor/cubic argument, not from this finite sample.'}

def main():
    need(len(sys.argv)==2,'USAGE_OUTPUT')
    dest=pathlib.Path(sys.argv[1])
    need(not dest.exists(),'OUTPUT_EXISTS')
    start=clock()
    identity=identity_fixture(fixture())
    ph8=[ph8_control(c,d) for c,d in ((Q(1),Q(3)),(Q(3,2),Q(2)),(Q(7,5),Q(9,4)))]
    need(time.monotonic()-START<60,'TIME_BOUND_UNKNOWN')
    out={'kind':'PARENT_EXACT_CYCLE_COVER_AND_PH8_CONTROL','started_native_clock':start,'finished_native_clock':clock(),
         'source_sha256':sha(pathlib.Path(__file__).read_bytes()),'identity_fixture':identity,'ph8_fixtures':ph8,
         'all_checks_passed':True,'elapsed_seconds':time.monotonic()-START,
         'limits':'Finite exact controls, not an all-matrix proof, parent certificate replay of thresholds, formal/kernel, independent-model or novelty acceptance. No author/reviewer program imported.'}
    with dest.open('x') as stream:
        json.dump(out,stream,indent=2)
        stream.write('\n')
    print(json.dumps({'status':'PASS','output':str(dest),'sha256':sha(dest.read_bytes()),'extra_cycles':identity['extra_cycles'],'ph8_fixtures':len(ph8)}))

if __name__=='__main__':
    try:
        main()
    except Invalid as error:
        print(json.dumps({'status':'REJECT_OR_UNKNOWN','reason':str(error)}),file=sys.stderr)
        raise SystemExit(2)
