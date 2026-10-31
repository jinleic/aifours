#!/usr/bin/env python3
"""Bounded actual scalar SDE check for the literal Minkowski-kernel bound."""
import json
import math
import random


def main():
    n, steps, seed=4000,100,20261028
    T=1.0; a=-0.3; sigma=0.7; dt=T/steps
    rng=random.Random(seed)
    Csum=[0.0]*steps
    in_sum=out_sum=triangle_sum=0.0
    strict_count=0
    max_path_ineq_violation=0.0
    for _ in range(n):
        W=0.0; phis=[]; ws=[]
        for j in range(steps):
            t=j*dt
            phis.append(math.exp((a-sigma*sigma/2)*t+sigma*W))
            ws.append(1.0+W)  # actual progressive adapted E2 input
            W += rng.gauss(0.0,math.sqrt(dt))
        suffix=[0.0]*steps; acc=0.0
        for j in range(steps-1,-1,-1):
            acc += phis[j]*phis[j]*dt
            suffix[j]=acc
        state=[]; acc=0.0; tri=0.0
        for j in range(steps):
            acc += ws[j]/phis[j]*dt
            state.append(phis[j]*acc)
            norm_future=math.sqrt(suffix[j])/phis[j]
            Csum[j]+=norm_future
            tri += abs(ws[j])*norm_future*dt
        inn=math.sqrt(sum(x*x*dt for x in ws))
        out=math.sqrt(sum(x*x*dt for x in state))
        in_sum+=inn; out_sum+=out; triangle_sum+=tri
        if out<tri: strict_count+=1
        max_path_ineq_violation=max(max_path_ineq_violation,out-tri)
    Cmeans=[x/n for x in Csum]
    estimated_upper=math.sqrt(sum(x*x*dt for x in Cmeans))
    rho=2*a+sigma*sigma
    integral=(math.expm1(rho*T)-rho*T)/(rho*rho) if rho else T*T/2.0
    gaussian_upper=math.sqrt(integral)
    print(json.dumps({
        'model':'h=0,u=0,dx=(a*x+w)dt+sigma*x dW,z=x,x0=0',
        'a':a,'sigma':sigma,'T':T,'paths':n,'steps':steps,'seed':seed,
        'actual_adapted_input':'w(t)=1+W_t',
        'sample_literal_ratio':out_sum/in_sum,
        'sample_mean_triangle_over_input_norm':triangle_sum/in_sum,
        'sampled_strict_triangle_paths':strict_count,
        'max_discrete_path_inequality_violation':max_path_ineq_violation,
        'sample_estimate_future_kernel_upper':estimated_upper,
        'gaussian_second_moment_upper_continuous':gaussian_upper,
        'limits':'Finite-grid Monte Carlo sanity check; it proves neither global gain sharpness nor an endpoint attainer.'
    },indent=2,sort_keys=True))


if __name__=='__main__': main()
