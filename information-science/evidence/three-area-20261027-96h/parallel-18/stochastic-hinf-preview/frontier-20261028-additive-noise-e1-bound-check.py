#!/usr/bin/env python3
"""Bounded full-preview diagnostic with Q=0 but additive control noise."""
import json
import math
import random


def main():
    T=1.25; h=.25; dt=.01; steps=125; shift=25; active=100
    A=-.2; B=.5; B0=.4; K=.1; A0=-B0*K; C=.7; D0=1.; D1=.2
    L0=.3; Lh=-.2; kernel=.1
    P=A+B*K; Q=A0+B0*K; O=D0+D1*K
    ad=abs(B*L0)+abs(B*Lh+C)+h*abs(B*kernel)
    ag=abs(B0*L0)+abs(B0*Lh)+h*abs(B0*kernel)
    ao=abs(D1*L0)+abs(D1*Lh)+h*abs(D1*kernel)
    rho=2*P
    gram=math.expm1(rho*T)/rho if rho else T
    double=(math.expm1(rho*T)-rho*T)/(rho*rho) if rho else T*T/2
    kd=abs(O)*math.sqrt(double); ks=abs(O)*math.sqrt(gram)
    tight=ao+kd*ad+8*ks*ag
    delta=min(T,1/(4*abs(P))) if P else T
    alpha=abs(P)*delta; n=math.ceil(T/delta)
    factor=math.expm1(-n*math.log1p(-alpha))/alpha if alpha else n
    generic=ao+abs(O)*math.sqrt(T)*(math.sqrt(delta)*ad+8*ag)*factor
    rng=random.Random(20261028); npaths=5000; sw=sz=0.0
    for _ in range(npaths):
        W=x=0.0; ws=[]; ew=ez=0.0
        for i in range(steps):
            w=math.exp(W*W/3) if i<active else 0.0; ws.append(w)
            wh=ws[i-shift] if i>=shift else 0.0
            conv=kernel*dt*sum(ws[max(0,i-shift+1):i+1])
            u=K*x+L0*w+Lh*wh+conv; z=D0*x+D1*u
            ew+=w*w*dt; ez+=z*z*dt
            dw=rng.gauss(0.0,math.sqrt(dt)); W+=dw
            x+=(A*x+B*u+C*wh)*dt+(A0*x+B0*u)*dw
        sw+=math.sqrt(ew); sz+=math.sqrt(ez)
    print(json.dumps({'T':T,'h':h,'P':P,'Q':Q,'O':O,'B0':B0,'D1':D1,
      'a_d':ad,'a_s':ag,'a_o':ao,'kappa_d':kd,'kappa_s':ks,
      'additive_noise_bound':tight,'generic_block_bound':generic,
      'paths':npaths,'steps':steps,'seed':20261028,
      'input':'w=exp(W_t^2/3), t<=1, zero after; exactly E1 not E2',
      'sample_literal_ratio':sz/sw,
      'limits':'Finite-grid Monte Carlo sanity check and floating analytic evaluation; not a sharp gain or proof.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
