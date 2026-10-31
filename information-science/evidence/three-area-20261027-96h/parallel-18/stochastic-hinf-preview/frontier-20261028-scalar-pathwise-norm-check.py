#!/usr/bin/env python3
"""Bounded matrix check of the actual scalar stochastic Volterra operator."""
import json
import math
import random


def apply(w,phi,dt):
    acc=0.0
    out=[]
    for x,p in zip(w,phi):
        acc += x/p*dt
        out.append(p*acc)
    return out


def adjoint(y,phi,dt):
    out=[0.0]*len(phi)
    acc=0.0
    for i in range(len(phi)-1,-1,-1):
        acc += phi[i]*y[i]*dt
        out[i]=acc/phi[i]
    return out


def norm(x):
    return math.sqrt(sum(y*y for y in x))


def opnorm(phi,dt,iterations=80):
    v=[1.0/math.sqrt(len(phi))]*len(phi)
    for _ in range(iterations):
        u=adjoint(apply(v,phi,dt),phi,dt)
        un=norm(u)
        if un<=0 or not math.isfinite(un): raise RuntimeError('invalid power iteration')
        v=[x/un for x in u]
    y=apply(v,phi,dt)
    lam=norm(y)
    u=adjoint(y,phi,dt)
    residual=norm([x-lam*lam*z for x,z in zip(u,v)])
    return lam,residual


def main():
    T=1.0; sigma=0.7; a=0.0; steps=80; n=400; dt=T/steps
    zero=[math.exp((a-sigma*sigma/2)*(i+1)*dt) for i in range(steps)]
    slope=0.8
    rising=[math.exp((a-sigma*sigma/2+sigma*slope)*(i+1)*dt) for i in range(steps)]
    g0,r0=opnorm(zero,dt); g1,r1=opnorm(rising,dt)
    if not (g1>g0): raise RuntimeError('monotonic deterministic-kernel control failed')
    rng=random.Random(20261028)
    norms=[]; ratios=[]; residuals=[]
    for _ in range(n):
        W=0.0; phi=[]
        for i in range(steps):
            W+=rng.gauss(0.0,math.sqrt(dt))
            phi.append(math.exp(sigma*W+(a-sigma*sigma/2)*(i+1)*dt))
        G,res=opnorm(phi,dt)
        q=[1/p for p in phi]
        ratio=norm(apply(q,phi,dt))/norm(q)
        norms.append(G); ratios.append(ratio/G); residuals.append(res)
    print(json.dumps({
        'model':'dx=(a*x+w)dt+sigma*x dW, z=x, h=0, x0=0',
        'a':a,'sigma':sigma,'T':T,'steps':steps,'brownian_paths':n,'seed':20261028,
        'zero_path_discrete_operator_norm':g0,
        'linear_noise_path_discrete_operator_norm':g1,
        'zero_and_linear_eigen_residuals':[r0,r1],
        'sample_path_operator_norm_min':min(norms),
        'sample_path_operator_norm_max':max(norms),
        'sample_average_inverse_phi_input_ratio_over_path_norm':sum(ratios)/n,
        'sample_max_power_iteration_residual':max(residuals),
        'limits':'Finite-grid power iteration / simulation; proves neither nonattainment nor original expected-path gain.'
    },indent=2,sort_keys=True))


if __name__=='__main__': main()
