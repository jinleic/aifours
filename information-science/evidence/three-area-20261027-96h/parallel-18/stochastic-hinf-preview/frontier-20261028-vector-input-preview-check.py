#!/usr/bin/env python3
"""Bounded matrix-noise vector-disturbance physical-kernel diagnostic."""
import json
import math
import random

P=((-0.2,0.8),(-0.5,-0.3)); Q=((0.35,0.7),(-0.2,-0.15))
D=((1.0,0.2),(-0.3,0.7)); B=((1.0,0.0),(0.0,1.0)); C=((-0.4,0.2),(1.2,-0.3))


def main():
    T=1.5; h=.45; N=100; shift=30; active=N-shift; dt=T/N
    paths=600; seed=20261028; rng=random.Random(seed)
    op_sum=[0.0]*active; hs2_sum=[0.0]*active
    total_in=total_out=total_R=total_Rbar=0.0; max_violation=0.0; strict=0
    for _ in range(paths):
        W=0.0; ws=[]; Fs=[]
        for _i in range(N):
            ws.append((1+W,1-W)); dw=rng.gauss(0.0,math.sqrt(dt)); W+=dw
            Fs.append((1+P[0][0]*dt+Q[0][0]*dw,P[0][1]*dt+Q[0][1]*dw,
                       P[1][0]*dt+Q[1][0]*dw,1+P[1][1]*dt+Q[1][1]*dw))
        out0=[0.0]*N; out1=[0.0]*N; tri=tri_bar=0.0
        for j in range(active):
            a=b=c=d=0.0; g00=g01=g11=0.0; resp2=0.0
            w0,w1=ws[j]
            for i in range(j,N):
                aa,bb,cc,dd=Fs[i]
                a,b,c,d=aa*a+bb*c,aa*b+bb*d,cc*a+dd*c,cc*b+dd*d
                if i==j:a+=B[0][0]; b+=B[0][1]; c+=B[1][0]; d+=B[1][1]
                if i==j+shift:a+=C[0][0]; b+=C[0][1]; c+=C[1][0]; d+=C[1][1]
                k00=D[0][0]*a+D[0][1]*c; k01=D[0][0]*b+D[0][1]*d
                k10=D[1][0]*a+D[1][1]*c; k11=D[1][0]*b+D[1][1]*d
                g00+=(k00*k00+k10*k10)*dt; g01+=(k00*k01+k10*k11)*dt; g11+=(k01*k01+k11*k11)*dt
                y0=k00*w0+k01*w1; y1=k10*w0+k11*w1
                resp2+=(y0*y0+y1*y1)*dt
                out0[i]+=dt*y0; out1[i]+=dt*y1
            top=(g00+g11+math.sqrt((g00-g11)**2+4*g01*g01))/2
            op=math.sqrt(top); op_sum[j]+=op; hs2_sum[j]+=g00+g11
            tri+=math.sqrt(resp2)*dt; tri_bar+=op*math.hypot(w0,w1)*dt
        inn=math.sqrt(sum((w0*w0+w1*w1)*dt for w0,w1 in ws[:active]))
        out=math.sqrt(sum((out0[i]**2+out1[i]**2)*dt for i in range(N)))
        total_in+=inn; total_out+=out; total_R+=tri; total_Rbar+=tri_bar
        max_violation=max(max_violation,out-tri,tri-tri_bar)
        if out<tri:strict+=1
    gamma=math.sqrt(sum((v/paths)**2*dt for v in op_sum))
    H=math.sqrt(sum(v/paths*dt for v in hs2_sum))
    print(json.dumps({'P':P,'Q':Q,'D':D,'b':B,'c':C,'T':T,'h':h,'paths':paths,'steps':N,'seed':seed,
      'model':'dx=(Px+B*w_t+C*w_(t-h))dt+Qx dW,z=Dx; scalar W, w in R^2',
      'input':'progressive w=(1+W,1-W)','sample_literal_ratio':total_out/total_in,
      'sample_R_ratio':total_R/total_in,'sample_Rbar_ratio':total_Rbar/total_in,
      'empirical_operator_Gamma':gamma,'empirical_HS_H':H,
      'strict_triangle_paths':strict,'max_two_stage_violation':max_violation,
      'limits':'Finite-grid Euler/Monte Carlo and sample singular values; not an all-input proof or endpoint.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
