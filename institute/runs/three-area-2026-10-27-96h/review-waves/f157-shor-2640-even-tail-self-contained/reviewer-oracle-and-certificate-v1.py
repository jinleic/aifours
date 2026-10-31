#!/usr/bin/env python3
"""Brute subset oracle for reviewer solver, plus pinned certificate data audit.
No author source code is executed. AST extraction below uses REVIEWER code only.
"""
import ast
import collections
import datetime
import hashlib
import itertools
import json
import math
import pathlib
import random
import sys
import time
ROOT=pathlib.Path(__file__).resolve().parent
SOURCE=ROOT/'reviewer-independent-exact-v1.py'
b=SOURCE.read_bytes()
assert hashlib.sha256(b).hexdigest()=='6590dd5bb41b362fc213f6cfe6142c56badd1fc90fbdcbced213776cef6ed905'
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
N=2640
DG=tuple(math.gcd(i,N) for i in range(N))
DEADLINE=time.monotonic()+60
names={'gcdiff','delta','compatible','valid_selection','solve','screen','counts'}
tree=ast.parse(b)
functions=ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[])
assert len(functions.body)==len(names)
exec(compile(functions,str(SOURCE),'exec'),globals())
A=(0,3,8,11);Y=(0,1,7,13,14);GA=frozenset((3,5,8,11));GY=frozenset((1,2,6,12))
# Deliberately no capacity/graph/memo pruning in this powerset oracle.
def brute(candidates,F,quotas,anchors):
    vals=tuple(x for x in candidates if any(x%m==r for m,r,k in quotas))
    for mask in range(1<<len(vals)):
        w=tuple(x for i,x in enumerate(vals) if (mask>>i)&1)
        if not set(anchors)<=set(w):continue
        if not all(sum(x%m==r for x in w)==k for m,r,k in quotas):continue
        if all(math.gcd(x-y,N) not in F for x,y in itertools.combinations(w,2)):
            return True
    return False
rng=random.Random(1572640)
pool=(0,1,3,5,7,8,11,13,14,22,30,33,50,55,60,75,88,110,120,165,240,330,660,1320,1393,2236,2639)
cases=[((0,3,8,11),GY,[(3,0,1),(2,0,1)],(0,)),
       ((0,3,8,11),GA,[(3,0,2)],()),
       ((0,3,8,11),GY,[(3,0,0),(2,0,0)],()),
       ((0,3,8,11),GY,[(3,0,-1)],()),
       ((0,3,8,11),GY,[],()),
       ((0,3,8,11),GY,[],(0,))]
for _ in range(600):
    vals=tuple(sorted(rng.sample(pool,rng.randrange(1,12))))
    F=frozenset(rng.sample([1,2,3,4,5,6,8,11,12,16,20,24,55,240,660,1320],rng.randrange(0,7)))
    quotas=[]
    for _ in range(rng.randrange(1,6)):
        m=rng.choice((2,3,4,5,7,8,11))
        quotas.append((m,rng.randrange(m),rng.randrange(0,5)))
    anchors=tuple(rng.sample(vals,rng.randrange(0,min(3,len(vals))+1)))
    cases.append((vals,F,quotas,anchors))
hist=collections.Counter()
for index,(vals,F,quotas,anchors) in enumerate(cases):
    expected=brute(vals,F,quotas,anchors)
    ans=solve(vals,F,quotas,anchors)
    assert ans['sat'] is expected,(index,expected,ans,vals,F,quotas,anchors)
    hist['SAT' if expected else 'UNSAT']+=1
# The author's pinned cover is treated as finite data, not executable code.
CERT=pathlib.Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/shor-completion/frontier-20261028-2640-even-tail-cover-v1.json')
bc=CERT.read_bytes()
assert hashlib.sha256(bc).hexdigest()=='791016f119addb8367e729d803da53e8eb2ea4d1ed393ecbce9bfa830bbff758'
assert len(bc)==3689 and bc.count(b'\n')==1
cert=json.loads(bc)
qset=set(screen(Y,GA));pset=set(screen(A,GY))
def check_cover(groups):
    flat=[x for g in groups for x in g]
    assert all(groups) and len(groups)==266
    assert len(flat)==len(set(flat))==658 and set(flat)==qset
    assert all(math.gcd(x-y,N) in GA for g in groups for x,y in itertools.combinations(g,2))
assert cert['n']==N
check_cover(cert['Q_conflict_cliques'])
pairs=cert['P_mod3_1_conflict_pairs']
assert len(pairs)==8 and len(set(x for p in pairs for x in p))==16
assert all(x in pset and y in pset and x%3==y%3==1 and math.gcd(x-y,N) in GY for x,y in pairs)
# Intended negative keeps coverage, nonemptiness, and clique count unchanged.
altered=[list(g) for g in cert['Q_conflict_cliques']]
i=next(i for i,g in enumerate(altered) if g==[0])
j=next(i for i,g in enumerate(altered) if g==[330,674])
altered[i][0],altered[j][0]=altered[j][0],altered[i][0]
assert sorted(x for g in altered for x in g)==sorted(qset)
assert math.gcd(altered[j][0]-altered[j][1],N)==2
try:
    check_cover(altered)
except AssertionError:
    negative_detected=True
else:
    raise AssertionError('gcd-clique mutation not detected')
# Strengthen the P12 positive control to preserve ALL five old anchors.
h=frozenset((3,4,5,8,11,16,20,24,44,80,88,165))
run=json.loads((ROOT/'reviewer-independent-exact-v1-receipt.json').read_bytes())
w=sorted(set(run['sections']['P12_literal_two_quota_positive']['witness'])|set(Y))
valid_selection(w,screen(Y,h),h,[(5,0,44),(11,2,20)],Y)
assert len(w)==67
# Elementary cyclotomic identities; this is not an attempted proof of CM T2.
identities=[]
for p in (3,11):
    for s in (1,2,3,4):
        u=1<<(s-1)
        coeff=collections.Counter()
        for j in range(p):
            coeff[j*u]+=(-1)**j
            coeff[(j+1)*u]+=(-1)**j
        assert {e:c for e,c in coeff.items() if c}=={0:1,p*u:1}
        identities.append({'prime':p,'s':s,'degree':p*u})
result={'started_utc':started,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'solver_source_sha256':hashlib.sha256(b).hexdigest(),
        'oracle_cases':len(cases),'oracle_outcomes':dict(hist),'oracle_disagreements':0,
        'oracle_pruning':'none; powerset enumeration <=11 vertices',
        'author_programs_executed':False,'pinned_cover':{'sha256':hashlib.sha256(bc).hexdigest(),'vertices':658,'cliques':266,'verified':True},
        'certificate_mutation':{'preserved':'all 658 vertices, exact partition, 266 nonempty groups','swapped':[0,330],'new_nonedged_pair':[0,674],'gcd':2,'detected':negative_detected},
        'P12_remove_only_fibre_quotas_positive':{'witness':w,'all_five_Y_anchors':True,'two_quotas':[44,20],'pairwise_H_compatible':True,'not_claimed_full_Q':True,'mod8_counts':counts(w,8)},
        'polynomial_identities':identities,'all_assertions_passed':True}
OUT=ROOT/'reviewer-oracle-and-certificate-v1-receipt.json'
with OUT.open('x') as f:
    json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(result,sort_keys=True))
print('receipt_sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
