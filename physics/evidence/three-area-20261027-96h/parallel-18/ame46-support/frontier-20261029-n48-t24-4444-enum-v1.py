#!/usr/bin/env python3
"""Exact finite N48/t24/r4444 residual enumeration and odd phase relations.

Mathematical normal form (proved separately): after normalizing the missing
A-to-B/C/D pair matchings to identity, every A fiber has six pair-injective
triples on the three symbols other than A. Its local missing matching on each
other pair is obtained by deleting A from the corresponding global permutation
cycle. All 24^3 global matching triples are enumerated. Every zero-excess2x2
block imposes phi11-phi12-phi21+phi22=pi. An integer left relation with odd sum
certifies incompatibility for ANY nonzero amplitudes, not just equal moduli.
"""
import argparse
from collections import Counter,defaultdict,deque
import itertools
import json
from pathlib import Path

P3=((0,1),(0,2),(1,2));P4=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def fiber_catalog():
    cube=list(itertools.product(range(3),repeat=3));F=[]
    for T in itertools.combinations(cube,6):
        if all(sum(q[i]==x for q in T)==2 for i in range(3) for x in range(3)) and all(len({(q[i],q[j]) for q in T})==6 for i,j in P3):F.append(T)
    if len(F)!=144:raise ValueError('six-fiber catalog')
    catalog={}
    for a in range(4):
        V=[x for x in range(4) if x!=a];D={}
        for T in F:
            T=tuple(tuple(V[q[i]] for i in range(3)) for q in T);sig=tuple(frozenset((q[i],q[j]) for q in T) for i,j in P3)
            if sig in D:raise ValueError('duplicate local projection signature')
            D[sig]=T
        catalog[a]=D
    return catalog


def deletion_graph(p,a):
    V=[x for x in range(4) if x!=a];g={b:(p[b] if p[b]!=a else p[a]) for b in V}
    if set(g.values())!=set(V):raise ValueError('cycle deletion not permutation')
    return frozenset((b,c) for b in V for c in V if c!=g[b])


def projected_ok(E):
    return all(len(C:=Counter((q[i],q[j]) for q in E))==12 and set(C.values())=={2} for i,j in P4)


def blocks(E):
    equations=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(set)
        for q in E:R[tuple(q[i] for i in A)].add(tuple(q[i] for i in B))
        seen=set()
        for r in sorted(R):
            if r in seen:continue
            partners=[s for s in R if s!=r and R[r]&R[s]]
            if len(partners)!=1 or R[partners[0]]!=R[r] or len(R[r])!=2:return None
            s=partners[0];seen|={r,s};c,d=sorted(R[r]);terms=[]
            for row,col,sign in ((r,c,1),(r,d,-1),(s,c,-1),(s,d,1)):
                q=[0]*4
                for i,x in zip(A,row):q[i]=x
                for i,x in zip(B,col):q[i]=x
                terms.append((tuple(q),sign))
            equations.append(terms)
    if len(equations)!=18:raise ValueError('block count')
    return equations


def phase_matrix(E,eqs):
    idx={q:i for i,q in enumerate(E)};M=[]
    for terms in eqs:
        row=[0]*len(E)
        for q,s in terms:row[idx[q]]+=s
        M.append(row)
    return M


def odd_relation(M):
    m=len(M);n=len(M[0]);A=[row[:]+[int(i==j) for j in range(m)] for i,row in enumerate(M)];rank=0
    for c in range(n):
        if rank==m:break
        while True:
            nz=[i for i in range(rank,m) if A[i][c]]
            if not nz:break
            p=min(nz,key=lambda i:abs(A[i][c]));A[rank],A[p]=A[p],A[rank]
            for i in range(rank+1,m):
                if A[i][c]:
                    q=A[i][c]//A[rank][c];A[i]=[x-q*y for x,y in zip(A[i],A[rank])]
            if not any(A[i][c] for i in range(rank+1,m)):break
        if A[rank][c]:rank+=1
    for row in A[rank:]:
        if any(row[:n]):raise ValueError('integer elimination did not reach kernel')
        lam=row[n:]
        if sum(lam)%2:
            if any(sum(lam[i]*M[i][j] for i in range(m)) for j in range(n)):raise ValueError('invalid odd relation')
            return lam
    return None


def selector(E):
    index={q:i for i,q in enumerate(E)};adj=[set() for _ in E]
    for i,j in P4:
        C=defaultdict(list)
        for k,q in enumerate(E):C[q[i],q[j]].append(k)
        for u,v in C.values():adj[u].add(v);adj[v].add(u)
    col={}
    for start in range(len(E)):
        if start in col:continue
        col[start]=0;queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v in col and col[v]==col[u]:return None
                if v not in col:col[v]=1-col[u];queue.append(v)
    out=[q for i,q in enumerate(E) if col[i]==0]
    if len(out)!=12 or any(len({(q[i],q[j]) for q in out})!=12 for i,j in P4):raise ValueError('selector invalid')
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args();catalog=fiber_catalog();perms=list(itertools.permutations(range(4)));counts=Counter();records=[]
    for f,g,h in itertools.product(perms,repeat=3):
        counts['global_matching_triples']+=1;fib=[]
        for v in range(4):
            F=catalog[v].get(tuple(deletion_graph(p,v) for p in (f,g,h)))
            if F is None:break
            fib.append(F)
        if len(fib)!=4:continue
        counts['all_four_local_fibers_exist']+=1;E=sorted({(v,)+q for v,F in enumerate(fib) for q in F})
        if not projected_ok(E):continue
        counts['global_pair12_degree2']+=1
        if any(any(p[p[i]]!=i for i in range(4)) for p in (f,g,h)):raise ValueError('noninvolution survived global multiplicity')
        eqs=blocks(E)
        if eqs is None:continue
        counts['all_cut_2x2_block_supports']+=1
        if not(f==g==h):raise ValueError('surviving matching triple not diagonal')
        M=phase_matrix(E,eqs);lam=odd_relation(M)
        rec={'global_matchings':[f,g,h],'support':E,'block_equations':eqs}
        if lam is not None:
            rec['odd_integer_phase_relation']=lam;rec['relation_sum']=sum(lam);counts['odd_phase_relations']+=1
        else:
            choice=selector(E)
            if choice is None:raise ValueError('neither odd relation nor selector')
            rec['classical_selector']=choice;counts['classical_selector']+=1
        records.append(rec)
    if (counts['global_matching_triples'],counts['all_four_local_fibers_exist'],counts['global_pair12_degree2'],counts['all_cut_2x2_block_supports'],counts['odd_phase_relations'],counts['classical_selector'])!=(13824,3054,382,10,9,1):raise ValueError(f'unexpected enumeration {counts}')
    result={'counts':dict(counts),'records':records,'six_fiber_catalog_size':144,
      'scope':'Exact normalized residual-support enumeration and directly verifiable integer phase relations/selectors. Mathematical completeness and original AME/no-OLS composition are separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'counts':dict(counts),'scope':result['scope']},indent=2))


if __name__=='__main__':main()
