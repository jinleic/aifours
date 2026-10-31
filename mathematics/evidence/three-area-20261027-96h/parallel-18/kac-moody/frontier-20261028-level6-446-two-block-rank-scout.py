#!/usr/bin/env python3
"""Bounded exact modular rank scout for full-target [A,L] at level6.

A full 324-column rank modulo one prime proves full rational rank; any lower
modular rank alone proves no rational upper bound. Augmented-rank equality
modulo p is only exploratory unless separately lifted over Q.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent


def rank_mod(A,p):
    A=A.copy()%p;m,n=A.shape;row=0;piv=[]
    for col in range(n):
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        k=row+int(nz[0]);A[[row,k],:]=A[[k,row],:]
        q=int(A[row,col]);inv=pow(q,-1,p)
        if row+1<m:
            factors=(A[row+1:,col]*inv)%p
            A[row+1:,col:]=(A[row+1:,col:]-factors[:,None]*A[row,col:])%p
        piv.append(col);row+=1
        if row==m:break
    return row,piv


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);m=P['target_row_count'];n=P['whole_lowest_dim'];assert (m,n)==(1780,162);D=10368;p=32749
    assert all(p%d for d in range(2,math.isqrt(p)+1))
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for z in row['entries']:
            l,e=Q(z['L'])*D,Q(z['E'])*D;assert l.denominator==e.denominator==1 and abs(l)<2**60 and abs(e)<2**60
            L[i,z['column']]=int(l);E[i,z['column']]=int(e)
    assert 6*int(np.max(np.abs(L)))+int(np.max(np.abs(E)))<2**63
    A=6*L+E;X=np.concatenate((A%p,L%p),axis=1)
    rank,piv=rank_mod(X,p)
    bottom=np.concatenate((np.eye(n,dtype=np.int64),np.eye(n,dtype=np.int64)),axis=1)
    augmented,apiv=rank_mod(np.concatenate((X,bottom),axis=0),p)
    result={'degree':[4,4,6],'source_sha256':digest,'target_rows':m,'source_columns':n,'prime':p,
            'rank_A_L_mod_prime':rank,'rank_augmented_mod_prime':augmented,
            'pivots_A_L':piv,'pivots_augmented':apiv,
            'modular_product_safety':'p<2^15, each individual product <2^30',
            'full_column_rank_certified_over_Q':rank==2*n,
            'limits':'If modular rank is not 324, it is a lower bound only; equal modular augmented ranks do NOT alone prove rational inclusion or a cone.',
            'status':'EXACT_MODULAR_TWO_BLOCK_RANK_SCOUT'}
    out=ROOT/'frontier-20261028-level6-446-two-block-rank-scout-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE mod',p,'rank[A,L]',rank,'rank augmented',augmented,'full column rank',rank==2*n,out.name,flush=True)

if __name__=='__main__':main()
