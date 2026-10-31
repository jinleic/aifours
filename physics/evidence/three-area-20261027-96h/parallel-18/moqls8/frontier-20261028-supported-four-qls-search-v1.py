#!/usr/bin/env python3
"""Bounded restricted-support numerical search with exact intermediate target.

Output is floating point and cannot certify an ordinary MOQLS witness. This
uses a random subset of support patterns near ONE classical net, not WLOG.
"""
import argparse
import hashlib
import importlib.util
import json
import pathlib
import time
import numpy as np

BASE = pathlib.Path(__file__).with_name('frontier-20261028-four-qls-numeric-search-v1.py')
EXPECTED = 'ec6d8043704a923f80dc3b6c313f7d70cf4ae45736bd6ee6dcdc96844a2a8df5'
if hashlib.sha256(BASE.read_bytes()).hexdigest() != EXPECTED:
    raise ValueError('numeric Gram primitives source hash mismatch')
spec = importlib.util.spec_from_file_location('own_four_gram', BASE)
K = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K)
N,M,N2=K.N,K.M,K.N2
SEED=2026102818


def make_mask(rng):
    mask=np.zeros((M,N,N2),dtype=bool)
    for a in range(M):
        for j in range(N):
            mask[a,j,j]=True
    for i in range(1,N):
        for j in range(N):
            x=i*N+j
            primaries=[K.gf8mul(a+1,i)^j for a in range(M)]
            if len(set(primaries))!=4 or j in primaries:
                raise ValueError('classical base support disjointness failed')
            for a,p in enumerate(primaries):
                mask[a,p,x]=True
            free=[v for v in range(N) if v!=j and v not in primaries]
            for z,v in enumerate(free):
                # Force one additional component for the target vector.
                owner=0 if (i==1 and j==1 and z==0) else int(rng.integers(M))
                mask[owner,v,x]=True
    return mask


def project(V,mask):
    V=V*mask
    lengths=np.sqrt(np.sum(np.abs(V)**2,axis=1))
    if np.any(lengths<1e-14) or not np.all(np.isfinite(lengths)):
        raise ValueError('vanishing/nonfinite masked vector')
    V=V/lengths[:,None,:]
    for a in range(M):
        V[a,:,:N]=np.eye(N,dtype=np.complex128)
    # Constraint: Q_0(0,0)=e0 and |<Q_0(0,0),Q_0(1,1)>|^2=1/2.
    x=9
    target=V[0,:,x].copy()
    if abs(target[0])<1e-14:
        raise ValueError('target anchor coordinate vanished')
    target[0]=target[0]/abs(target[0])*np.sqrt(0.5)
    tail=target.copy();tail[0]=0
    tailnorm=np.linalg.norm(tail)
    if tailnorm<1e-14:
        raise ValueError('target lacks a nonzero second coordinate')
    tail*=np.sqrt(0.5)/tailnorm
    tail[0]=target[0]
    V[0,:,x]=tail
    return V


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--candidate',required=True);args=ap.parse_args()
    start=time.monotonic();rng=np.random.default_rng(SEED)
    baseline=K.classical_input();positive=K.physical_diagnostics(baseline)
    if max(positive[k] for k in ('norm_max_abs_error','row_max_abs_error','column_max_abs_error','pair_product_gram_max_abs_error'))>1e-14:
        raise ValueError('positive classical full-Gram control failed')
    bad=baseline.copy();bad[1]=bad[0];negative=K.physical_diagnostics(bad)
    if negative['row_max_abs_error']>1e-14 or negative['column_max_abs_error']>1e-14 or negative['pair_product_gram_max_abs_error']<.9:
        raise ValueError('duplicate-square control failed')
    runs=[];best=None;best_mask=None;best_loss=float('inf')
    for restart in range(8):
        if time.monotonic()-start>30:
            break
        mask=make_mask(rng)
        V=project((rng.normal(size=mask.shape)+1j*rng.normal(size=mask.shape))*mask,mask)
        mom=np.zeros_like(V);var=np.zeros(V.shape,dtype=float)
        local=float('inf');diag=None;steps=0;first=time.monotonic()
        for step in range(1,4001):
            if time.monotonic()-start>30 or time.monotonic()-first>4:
                break
            loss,grad=K.loss_grad(V)
            if not np.isfinite(loss) or not np.all(np.isfinite(grad)):
                raise ValueError('nonfinite optimizer state')
            if loss<local:
                local=float(loss);diag=K.physical_diagnostics(V)
            if loss<best_loss:
                best_loss=float(loss);best=V.copy();best_mask=mask.copy()
            grad*=mask
            mom=.9*mom+.1*grad;var=.999*var+.001*np.abs(grad)**2
            mh=mom/(1-.9**step);vh=var/(1-.999**step)
            V=project(V-.012*mh/(np.sqrt(vh)+1e-8),mask)
            steps=step
        runs.append({'restart':restart,'iterations':steps,'best_objective':local,
                     'full_gram_diagnostics':diag,'elapsed_seconds':time.monotonic()-first})
    if best is None:
        raise ValueError('no candidate reached')
    d=K.physical_diagnostics(best)
    if d['target_abs_error']>1e-12:
        raise ValueError('target projection not retained')
    candidate={'shape':list(best.shape),'real':best.real.tolist(),'imag':best.imag.tolist(),
               'support_mask':best_mask.astype(int).tolist(),
               'limits':'FLOATING approximate only; chosen support masks/target do not cover arbitrary families.'}
    path=pathlib.Path(args.candidate)
    with path.open('x',encoding='utf-8') as h:json.dump(candidate,h,separators=(',',':'));h.write('\n')
    report={'result':'BOUNDED_RESTRICTED_SUPPORT_EXPLORATION_NOT_A_WITNESS',
            'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'imported_own_gram_source_sha256':EXPECTED,'candidate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'numpy_version':np.__version__,'seed':SEED,'target_overlap_squared':0.5,
            'positive_control':positive,'duplicate_square_control':negative,
            'restarts':runs,'best_objective':best_loss,'best_full_diagnostics':d,
            'elapsed_seconds':time.monotonic()-start,
            'limits':'8 bounded random support-pattern restarts near one classical net; no exact or global conclusion.'}
    with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2,allow_nan=False);h.write('\n')
    print(json.dumps(report,indent=2,allow_nan=False))

if __name__=='__main__':main()
