#!/usr/bin/env python3
"""Bounded row-unitary MOQLS(8) optimization, not a witness certificate."""
import argparse
import hashlib
import importlib.util
import json
import pathlib
import time
import numpy as np

BASE=pathlib.Path(__file__).with_name('frontier-20261028-four-qls-numeric-search-v1.py')
PIN='ec6d8043704a923f80dc3b6c313f7d70cf4ae45736bd6ee6dcdc96844a2a8df5'
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=PIN:raise ValueError('Gram source pin mismatch')
spec=importlib.util.spec_from_file_location('own_gram',BASE)
K=importlib.util.module_from_spec(spec);spec.loader.exec_module(K)
N,M,N2=K.N,K.M,K.N2
SEED=2026102819


def polar(A):
    U,_,Vh=np.linalg.svd(A,full_matrices=False)
    return U@Vh


def tangent(V,G):
    out=np.zeros_like(V)
    for a in range(M):
        for i in range(1,N):
            sl=slice(N*i,N*(i+1));U=V[a,:,sl];H=U.conj().T@G[a,:,sl]
            out[a,:,sl]=G[a,:,sl]-U@((H+H.conj().T)/2)
    return out


def retract(V,D,step):
    W=V.copy()
    for a in range(M):
        for i in range(1,N):
            sl=slice(N*i,N*(i+1));W[a,:,sl]=polar(V[a,:,sl]-step*D[a,:,sl])
    return W


def random_start(rng):
    V=np.zeros((M,N,N2),dtype=np.complex128)
    for a in range(M):
        V[a,:,:N]=np.eye(N)
        for i in range(1,N):
            Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
            V[a,:,N*i:N*(i+1)]=polar(Z)
    return V


def rotated_start(rng):
    V=K.classical_input()
    sl=slice(N,2*N)
    # Exact 45-degree mixing of two row columns, making the chosen overlap 1/2.
    rotation=np.eye(N,dtype=np.complex128)
    c=1/np.sqrt(2)
    rotation[0,0]=c;rotation[0,1]=-c;rotation[1,0]=c;rotation[1,1]=c
    V[0,:,sl]=V[0,:,sl]@rotation
    for a in range(M):
        for i in range(1,N):
            sl=slice(N*i,N*(i+1))
            V[a,:,sl]=polar(V[a,:,sl]+0.08*(rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))))
    return V


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--candidate',required=True);args=ap.parse_args()
    start=time.monotonic();rng=np.random.default_rng(SEED)
    baseline=K.classical_input();control=K.physical_diagnostics(baseline)
    if max(control[k] for k in ('norm_max_abs_error','row_max_abs_error','column_max_abs_error','pair_product_gram_max_abs_error'))>1e-14:raise ValueError('classical control failed')
    negative=baseline.copy();negative[1]=negative[0];neg=K.physical_diagnostics(negative)
    if neg['row_max_abs_error']>1e-14 or neg['column_max_abs_error']>1e-14 or neg['pair_product_gram_max_abs_error']<.9:raise ValueError('negative control failed')
    # Independent local check of tangent projected gradient versus a retracted direction.
    V=random_start(rng);val,G=K.loss_grad(V);D=tangent(V,G)
    h=1e-6;vp=retract(V,D,-h);vm=retract(V,D,h)
    measured=(K.loss_grad(vp)[0]-K.loss_grad(vm)[0])/(2*h)
    expected=float(2*np.vdot(D,D).real)
    grad_error=abs(measured-expected)/(1+abs(expected))
    if not np.isfinite(grad_error) or grad_error>1e-5:raise ValueError(f'row-manifold gradient check failed {grad_error}')
    best=None;bestval=float('inf');runs=[]
    for restart in range(5):
        if time.monotonic()-start>28:break
        V=rotated_start(rng) if restart==0 else random_start(rng)
        local=float('inf');diag=None;steps=0;first=time.monotonic();rate=0.04
        for iteration in range(1,2501):
            if time.monotonic()-start>28 or time.monotonic()-first>5.5:break
            val,G=K.loss_grad(V)
            if not np.isfinite(val):raise ValueError('nonfinite objective')
            if val<local:local=float(val);diag=K.physical_diagnostics(V)
            if val<bestval:bestval=float(val);best=V.copy()
            D=tangent(V,G)
            trial=retract(V,D,rate);candidate_val,_=K.loss_grad(trial)
            if candidate_val<=val:
                V=trial;rate=min(rate*1.01,.2)
            else:
                rate=max(rate*.5,1e-8)
            steps=iteration
        runs.append({'restart':restart,'iterations':steps,'best_objective':local,
                     'full_gram_diagnostics':diag,'elapsed_seconds':time.monotonic()-first})
    if best is None:raise ValueError('no finite optimizer state')
    diag=K.physical_diagnostics(best)
    cand={'shape':list(best.shape),'real':best.real.tolist(),'imag':best.imag.tolist(),
          'limits':'Floating point numerical candidate, not an actual witness or completeness claim.'}
    path=pathlib.Path(args.candidate)
    with path.open('x',encoding='utf-8') as h:json.dump(cand,h,separators=(',',':'));h.write('\n')
    report={'result':'BOUNDED_ROW_UNITARY_EXPLORATION_NOT_A_WITNESS',
            'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'own_gram_source_sha256':PIN,'candidate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'seed':SEED,'numpy_version':np.__version__,'tangent_gradient_relative_error':grad_error,
            'positive_classical_control':control,'duplicate_square_control':neg,
            'target_overlap_squared':K.TARGET,'target_penalty_weight':K.WEIGHT,
            'restarts':runs,'best_objective':bestval,'best_full_diagnostics':diag,
            'elapsed_seconds':time.monotonic()-start,
            'limits':'Five bounded restarts and a single forced intermediate overlap target. No global or exact claim.'}
    with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2,allow_nan=False);h.write('\n')
    print(json.dumps(report,indent=2,allow_nan=False))

if __name__=='__main__':main()
