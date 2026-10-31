#!/usr/bin/env python3
"""Independent triangle-cover replay and phase-relation verifier for N48/r4444.

No producer code, integer elimination, phase engine or SAT solver is imported.
Regenerates all13824 matching triples by extending the local forbidden pairs to
one of six 3x3 matchings, and enumerates each six-triangle cover directly. Checks
complete coverage of the10 residual supports, all18 actual block equations,9 odd
integer phase contradictions, and the remaining12-word classical selector.
"""
import argparse
from collections import Counter,defaultdict
import hashlib
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


class CertificateError(ValueError):pass


def allowed_local(p,a):
    V=tuple(x for x in range(4) if x!=a);fixed={(b,p[b]) for b in V if p[b]!=a};choices=[]
    for images in itertools.permutations(V):
        missing=set(zip(V,images))
        if fixed<=missing:choices.append(missing)
    if len(choices)!=1:raise CertificateError('local forbidden matching extension not unique')
    return frozenset((b,c) for b,c in itertools.product(V,repeat=2) if (b,c) not in choices[0])


def triangles(G):
    BC,BD,CD=G;cells=sorted(BC);out=[]
    def search(k,usedBD,usedCD,T):
        if k==len(cells):
            if usedBD==set(BD) and usedCD==set(CD):out.append(tuple(T))
            return
        b,c=cells[k]
        for d in range(4):
            if (b,d) not in BD or (c,d) not in CD or (b,d) in usedBD or (c,d) in usedCD:continue
            search(k+1,usedBD|{(b,d)},usedCD|{(c,d)},T+[(b,c,d)])
    search(0,set(),set(),[])
    return out


def actual_blocks(E):
    equations=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
        for q in E:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
        if len(rows)!=12 or len(cols)!=12 or any(len(x)!=2 for x in rows.values()) or any(len(x)!=2 for x in cols.values()):return None
        remain=set(rows)
        while remain:
            R={min(remain)}
            while True:
                C=set().union(*(rows[r] for r in R));grow=set().union(*(cols[c] for c in C))
                if grow==R:break
                R=grow
            if len(R)!=2 or len(C)!=2:return None
            rr=sorted(R);cc=sorted(C);terms=[]
            for u,v,s in ((0,0,1),(0,1,-1),(1,0,-1),(1,1,1)):
                q=[0]*4
                for i,x in zip(A,rr[u]):q[i]=x
                for i,x in zip(B,cc[v]):q[i]=x
                terms.append((tuple(q),s))
            equations.append(terms);remain-=R
    return equations


def canonical_vector(terms,index):
    v=[0]*len(index)
    for q,s in terms:
        if tuple(q) not in index or type(s)!=int or s not in (-1,1):raise CertificateError('invalid phase equation term')
        v[index[tuple(q)]]+=s
    first=next((x for x in v if x),0)
    return tuple(-x for x in v) if first<0 else tuple(v)


def verify_record(rec):
    E=[tuple(q) for q in rec['support']]
    if len(E)!=24 or len(set(E))!=24 or any(len(q)!=4 or any(type(x)!=int or not 0<=x<4 for x in q) for q in E):raise CertificateError('invalid residual support')
    for i,j in PAIRS:
        C=Counter((q[i],q[j]) for q in E)
        if len(C)!=12 or set(C.values())!={2}:raise CertificateError('pair projection or multiplicity mismatch')
    actual=actual_blocks(E)
    if actual is None:raise CertificateError('residual cut not full2x2 blocks')
    index={q:i for i,q in enumerate(E)};given=rec['block_equations']
    if Counter(canonical_vector(t,index) for t in given)!=Counter(canonical_vector(t,index) for t in actual):raise CertificateError('phase block coverage mismatch')
    if 'odd_integer_phase_relation' in rec:
        lam=rec['odd_integer_phase_relation']
        if len(lam)!=len(given) or any(type(x)!=int for x in lam):raise CertificateError('invalid relation dimensions')
        total=[0]*len(E)
        for c,terms in zip(lam,given):
            for q,s in terms:total[index[tuple(q)]]+=c*s
        if any(total):raise CertificateError('phase relation does not cancel')
        if sum(lam)%2!=1:raise CertificateError('phase relation sum not odd')
        return 'ODD_INTEGER_PHASE_CONTRADICTION'
    if 'classical_selector' in rec:
        S=[tuple(q) for q in rec['classical_selector']]
        if len(S)!=12 or len(set(S))!=12 or not set(S)<=set(E):raise CertificateError('invalid selector support')
        if any(len({(q[i],q[j]) for q in S})!=12 for i,j in PAIRS):raise CertificateError('selector pair collision')
        return 'CLASSICAL_SELECTOR'
    raise CertificateError('no certificate')


def expect(rec,reason):
    try:verify_record(rec)
    except CertificateError as exc:
        if str(exc)!=reason:raise ValueError(f'wrong mutation failure {exc}; expected {reason}')
        return str(exc)
    raise ValueError('mutation accepted')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    raw=a.candidate.read_bytes();src=json.loads(raw);records=src['records'];perms=list(itertools.permutations(range(4)));cache={};stats=Counter();expected={}
    for f,g,h in itertools.product(perms,repeat=3):
        stats['matching_triples']+=1;options=[]
        for v in range(4):
            G=tuple(allowed_local(p,v) for p in (f,g,h))
            if G not in cache:cache[G]=triangles(G)
            opts=cache[G]
            if not opts:break
            options.append(opts)
        if len(options)!=4:continue
        stats['four_local_covers_exist']+=1
        for Fs in itertools.product(*options):
            E=tuple(sorted((v,)+q for v,F in enumerate(Fs) for q in F))
            if not all(len(C:=Counter((q[i],q[j]) for q in E))==12 and set(C.values())=={2} for i,j in PAIRS):continue
            stats['global_pair_counts_pass']+=1
            if actual_blocks(E) is None:continue
            stats['unitary_block_supports']+=1
            if E in expected:raise CertificateError('duplicate normalized residual support')
            expected[E]=(f,g,h)
    if (stats['matching_triples'],stats['four_local_covers_exist'],stats['global_pair_counts_pass'],stats['unitary_block_supports'])!=(13824,3054,382,10):raise CertificateError(f'coverage counts {stats}')
    seen=set();verdicts=Counter()
    for rec in records:
        E=tuple(sorted(tuple(q) for q in rec['support']))
        if E not in expected or E in seen:raise CertificateError('candidate coverage mismatch')
        if tuple(tuple(p) for p in rec['global_matchings'])!=expected[E]:raise CertificateError('matching/support binding mismatch')
        seen.add(E);verdicts[verify_record(rec)]+=1
    if seen!=set(expected) or verdicts!={'ODD_INTEGER_PHASE_CONTRADICTION':9,'CLASSICAL_SELECTOR':1}:raise CertificateError('incomplete certificate coverage')
    from copy import deepcopy
    bad=deepcopy(next(r for r in records if 'odd_integer_phase_relation' in r));bad['odd_integer_phase_relation'][0]+=1
    mut1=expect(bad,'phase relation does not cancel')
    bad=deepcopy(records[0]);bad['block_equations'].pop();mut2=expect(bad,'phase block coverage mismatch')
    bad=deepcopy(next(r for r in records if 'classical_selector' in r));bad['classical_selector'][1]=bad['classical_selector'][0]
    mut3=expect(bad,'invalid selector support')
    bad=deepcopy(records[0]);bad['support'][1]=bad['support'][0];mut4=expect(bad,'invalid residual support')
    result={'candidate_sha256':hashlib.sha256(raw).hexdigest(),'independent_coverage':dict(stats),
      'local_triangle_signature_cache':len(cache),'maximum_local_cover_multiplicity':max(map(len,cache.values())),
      'certificate_verdicts':dict(verdicts),'intended_mutation_controls':[mut1,mut2,mut3,mut4],
      'scope':'Exact finite normalized support coverage and direct phase/selector certificates. No original-AME/no-OLS composition or formal proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
