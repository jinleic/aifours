#!/usr/bin/env python3
"""Physical bounded diagnostic of preview plus delayed stochastic input kernels."""
import json
import math
import random


def main():
    T=1.5; h=0.5; a=-0.3; sigma=0.7; c0=0.6; ch=1.2
    steps=150; shift=50; active=steps-shift; dt=T/steps
    n=4000; seed=20261028; rng=random.Random(seed)
    sum_in=sum_out=sum_tri=0.0; strict=0; max_violation=0.0
    mean_C=[0.0]*active
    for _ in range(n):
        W=0.0; Ws=[]; phis=[]
        for i in range(steps):
            Ws.append(W)
            phis.append(math.exp((a-sigma*sigma/2)*i*dt+sigma*W))
            W+=rng.gauss(0.0,math.sqrt(dt))
        w=[1+Ws[j] for j in range(active)]
        suffix=[0.0]*steps; accum=0.0
        for i in range(steps-1,-1,-1):
            accum+=phis[i]*phis[i]*dt
            suffix[i]=accum
        norm_columns=[]
        for j in range(active):
            A=c0/phis[j]; B=ch/phis[j+shift]
            norm_columns.append(math.sqrt(A*A*suffix[j]+(2*A*B+B*B)*suffix[j+shift]))
            mean_C[j]+=norm_columns[j]
        now=later=0.0; out=[]
        for i in range(steps):
            if i<active: now+=c0*w[i]/phis[i]*dt
            j=i-shift
            if 0<=j<active: later+=ch*w[j]/phis[i]*dt
            out.append(phis[i]*(now+later))
        inn=math.sqrt(sum(x*x*dt for x in w))
        outn=math.sqrt(sum(x*x*dt for x in out))
        tri=sum(abs(w[j])*norm_columns[j]*dt for j in range(active))
        sum_in+=inn; sum_out+=outn; sum_tri+=tri
        if outn<tri: strict+=1
        max_violation=max(max_violation,outn-tri)
    C=[x/n for x in mean_C]
    gamma_est=math.sqrt(sum(x*x*dt for x in C))
    rho=2*a+sigma*sigma
    def F(x):
        return (math.expm1(rho*x)-rho*x)/(rho*rho) if rho else x*x/2
    H=math.sqrt(c0*c0*(F(T)-F(h))+(ch*ch+2*c0*ch*math.exp(a*h))*F(T-h))
    print(json.dumps({'T':T,'h':h,'S':T-h,'a':a,'sigma':sigma,'c0':c0,'ch':ch,
      'paths':n,'steps':steps,'seed':seed,'actual_input':'w_s=1+W_s',
      'model':'dx=(a*x+c0*w_t+ch*w_(t-h))dt+sigma*x dW,z=x,u=preview feedforward',
      'literal_sample_ratio':sum_out/sum_in,'triangle_sample_ratio':sum_tri/sum_in,
      'empirical_future_kernel_Gamma':gamma_est,'Gaussian_cross_term_H':H,
      'strict_discrete_triangle_paths':strict,'maximum_path_violation':max_violation,
      'limits':'Monte Carlo/finite-grid kernel sanity check; not a proof of the bound or an endpoint.'},indent=2,sort_keys=True))


if __name__=='__main__': main()
