#!/usr/bin/env python3
"""Find an exact relation obstructing X^T A = X^T L = I.

Uses modular pivots/CRT rational reconstruction as search ONLY; any claimed
relation is independently checked in ALL 1780 integer target rows. If none
is found within the bound, no impossibility is inferred.
"""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('mod',ROOT/'frontier-20261028-level6-446-modular-determinant-replay.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)


def pivots_mod(M,p):
    A=M.copy()%p;m,n=A.shape;ids=list(range(m));row=0;rows=[];cols=[]
    for c in range(n):
        nz=np.flatnonzero(A[row:,c])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j],:]=A[[j,row],:];ids[row],ids[j]=ids[j],ids[row]
        q=int(A[row,c]);inv=pow(q,-1,p)
        if row+1<m:
            v=(A[row+1:,c]*inv)%p
            A[row+1:,c:]=(A[row+1:,c:]-v[:,None]*A[row,c:])%p
        rows.append(ids[row]);cols.append(c);row+=1
        if row==m:break
    return rows,cols


def solve_mod(M,b,p):
    A=np.concatenate((M.copy()%p,(-b.copy()%p).reshape(-1,1)),axis=1);n=len(b)
    for i in range(n):
        nz=np.flatnonzero(A[i:,i])
        if not len(nz):return None
        j=i+int(nz[0]);A[[i,j],:]=A[[j,i],:]
        q=int(A[i,i]);inv=pow(q,-1,p);A[i,i:]=(A[i,i:]*inv)%p
        if i+1<n:
            factors=A[i+1:,i].copy()
            A[i+1:,i:]=(A[i+1:,i:]-factors[:,None]*A[i,i:])%p
    x=[0]*n
    for i in range(n-1,-1,-1):x[i]=(int(A[i,n])-sum(int(A[i,j])*x[j] for j in range(i+1,n)))%p
    return x


def reconstruct(r,N):
    if r==0:return Q(0)
    bound=math.isqrt(N//2);r0,r1=N,r;t0,t1=0,1
    while abs(r1)>bound:
        if not r1:return None
        q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
    if not t1 or abs(t1)>bound:return None
    if t1<0:r1,t1=-r1,-t1
    if math.gcd(abs(r1),t1)!=1 or (r1-r*t1)%N:return None
    return Q(r1,t1)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert (m,n)==(1780,162)
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for z in row['entries']:
            l,e=Q(z['L'])*D,Q(z['E'])*D;assert l.denominator==e.denominator==1 and abs(l)<2**60 and abs(e)<2**60
            L[i,z['column']]=int(l);E[i,z['column']]=int(e)
    assert 6*int(np.max(np.abs(L)))+int(np.max(np.abs(E)))<2**63
    M=np.concatenate((6*L+E,L),axis=1);p0=32749;assert mod.prime(p0)
    R,C=pivots_mod(M,p0);rank=len(C);free=[j for j in range(2*n) if j not in set(C)]
    print('modular pivot rank',rank,'candidate free columns',len(free),flush=True)
    square=M[np.ix_(R,C)];attempted=[];found=None
    for freecol in free[:12]:
        residue=[0]*rank;N=1;used=[]
        for p in range(32749,16384,-2):
            if len(used)>=20:break
            if not mod.prime(p):continue
            sol=solve_mod(square,M[R,freecol],p)
            if sol is None:continue
            inv=pow(N,-1,p)
            residue=[r+N*(((a-r)%p)*inv%p) for r,a in zip(residue,sol)]
            N*=p;used.append(p)
            if len(used)<3:continue
            reconstructed=[reconstruct(r,N) for r in residue]
            if any(q is None for q in reconstructed):continue
            c=[Q(0)]*(2*n);c[freecol]=Q(1)
            for j,q in zip(C,reconstructed):c[j]=q
            den=math.lcm(*(q.denominator for q in c));integer=[int(q*den) for q in c]
            gcd=math.gcd(*(abs(q) for q in integer));integer=[q//gcd for q in integer]
            if not any(integer[j]+integer[n+j] for j in range(n)):continue
            if all(sum(int(M[i,j])*integer[j] for j in range(2*n))==0 for i in range(m)):
                found={'source_u':integer[:n],'source_v':integer[n:],
                       'u_plus_v_nonzero':True,'all_1780_exact_integer_row_relations_zero':True,
                       'reconstruction_primes':used,'modulus_bits':N.bit_length(),'free_column':freecol}
                break
        attempted.append({'free_column':freecol,'prime_count':len(used),'found':bool(found)})
        print('candidate free column',freecol,'primes',len(used),'verified',bool(found),flush=True)
        if found:break
    out=ROOT/'frontier-20261028-level6-446-common-left-relation-search-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':[4,4,6],'target_sha256':digest,'modular_pivot_rank':rank,
                               'attempted':attempted,'result':found,
                               'status':'EXACT_RELATION_OBSTRUCTS_EQUAL_LEFT' if found else 'NO_RELATION_FOUND_IN_BOUND',
                               'scope':'no assertion about arbitrary positive-left tests or D3 kernel'},indent=2)+'\n')
    print('DONE', 'EXACT_RELATION_OBSTRUCTS_EQUAL_LEFT' if found else 'NO_RELATION_FOUND_IN_BOUND',out.name,flush=True)

if __name__=='__main__':main()
