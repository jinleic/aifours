#!/usr/bin/env python3
"""Bounded physical Euler diagnostic including additive control noise and feedthrough."""
import json
import math
import random


def main():
    T=1.25; h=.25; dt=.01; steps=125; shift=25; active=steps-shift
    A=-.2; A0=.3; B=.5; B0=.4; C=.7; D0=1.; D1=.2
    K=.1; L0=.3; Lh=-.2; kernel=.1
    P=A+B*K; Q=A0+B0*K; O=D0+D1*K
    bd=abs(B*L0)+abs(B*Lh+C)+h*abs(B*kernel)
    bs=abs(B0*L0)+abs(B0*Lh)+h*abs(B0*kernel)
    bo=abs(D1*L0)+abs(D1*Lh)+h*abs(D1*kernel)
    candidates=[T]
    if abs(P)>0:candidates.append(1/(4*abs(P)))
    if abs(Q)>0:candidates.append(1/(32*abs(Q))**2)
    delta=min(candidates); N=math.ceil(T/delta)
    alpha=abs(P)*delta+8*abs(Q)*math.sqrt(delta)
    factor=math.expm1(-N*math.log1p(-alpha))/alpha if alpha else N
    bound=bo+abs(O)*math.sqrt(T)*(math.sqrt(delta)*bd+8*bs)*factor
    rng=random.Random(20261028); paths=5000
    total_u=total_z=0.0; max_ratio=0.0
    for _ in range(paths):
        W=x=0.0; ws=[]; norm_w=norm_z=0.0
        for i in range(steps):
            w=math.exp(W*W/3) if i<active else 0.0; ws.append(w)
            wh=ws[i-shift] if i>=shift else 0.0
            conv=kernel*dt*sum(ws[max(0,i-shift+1):i+1])
            u=K*x+L0*w+Lh*wh+conv
            z=D0*x+D1*u
            norm_w+=w*w*dt; norm_z+=z*z*dt
            dw=rng.gauss(0.0,math.sqrt(dt)); W+=dw
            x+=(A*x+B*u+C*wh)*dt+(A0*x+B0*u)*dw
        wu=math.sqrt(norm_w); zz=math.sqrt(norm_z)
        total_u+=wu; total_z+=zz; max_ratio=max(max_ratio,zz/wu)
    print(json.dumps({'T':T,'h':h,'steps':steps,'paths':paths,'seed':20261028,
      'plant':{'A':A,'A0':A0,'B':B,'B0':B0,'C':C,'D0':D0,'D1':D1},
      'law':{'K':K,'L0':L0,'Lh':Lh,'H_constant':kernel},
      'actual_input':'w_t=exp(W_t^2/3) on [0,1], zero after; E1 finite, E2 infinite by Gaussian moments',
      'P':P,'Q':Q,'O':O,'drift_norm_bound':bd,'diffusion_norm_bound':bs,'output_norm_bound':bo,
      'block_delta':delta,'block_count':N,'alpha':alpha,'recurrence_factor':factor,
      'explicit_E1_upper_bound':bound,'sample_literal_ratio':total_z/total_u,
      'largest_sample_path_ratio':max_ratio,
      'limits':'Finite Euler/Monte Carlo sanity check; sample does not prove moments, gain or a sharp bound.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
