#!/usr/bin/env python3
"""Actual bounded 2x2 stochastic-state preview kernel diagnostic."""
import json
import math
import random


def gv(t, x, y):
    # A=[[-.2,1],[-.6,-.4]], D=[[1,.2],[-.3,.7]].
    k=math.sqrt(.59); factor=math.exp(-.3*t)
    co=math.cos(k*t); si=math.sin(k*t)/k
    v0=factor*(co*x+si*(.1*x+y))
    v1=factor*(co*y+si*(-.6*x-.1*y))
    return (v0+.2*v1,-.3*v0+.7*v1)


def simpson(f,lo,hi,n=2000):
    dt=(hi-lo)/n
    return dt/3*(f(lo)+f(hi)+4*sum(f(lo+(2*k-1)*dt) for k in range(1,n//2+1))+2*sum(f(lo+2*k*dt) for k in range(1,n//2)))


def n2(v):return v[0]*v[0]+v[1]*v[1]


def main():
    T=1.5; h=.45; S=T-h; sigma=.7; N=100; shift=30; active=N-shift; dt=T/N
    paths=1000; seed=20261028; rng=random.Random(seed)
    gb=[gv(j*dt,1.0,.4) for j in range(N)]
    gc=[gv(j*dt,-.4,1.2) for j in range(N)]
    def early(v):return math.exp(sigma*sigma*v)*n2(gv(v,1.0,.4))
    def late(v):
        b=gv(h+v,1.0,.4); c=gv(v,-.4,1.2)
        joint=(b[0]+c[0],b[1]+c[1])
        return (S-v)*math.exp(sigma*sigma*v)*(n2(joint)+math.expm1(sigma*sigma*h)*n2(b))
    H=math.sqrt(S*simpson(early,0,h)+simpson(late,0,S))
    mean_C=[0.0]*active; total_in=total_out=total_tri=0.0; max_violation=0.0; strict=0
    for _ in range(paths):
        W=0.0; ws=[]; phi=[]
        for i in range(N):
            ws.append(1.0+W)
            phi.append(math.exp(-sigma*sigma*i*dt/2+sigma*W))
            W+=rng.gauss(0.0,math.sqrt(dt))
        out0=[0.0]*N; out1=[0.0]*N; tri=0.0
        for j in range(active):
            col2=0.0
            for i in range(j,N):
                ratio=phi[i]/phi[j]
                k0=ratio*gb[i-j][0]; k1=ratio*gb[i-j][1]
                if i>=j+shift:
                    ratio2=phi[i]/phi[j+shift]
                    k0+=ratio2*gc[i-j-shift][0]; k1+=ratio2*gc[i-j-shift][1]
                col2+=(k0*k0+k1*k1)*dt
                out0[i]+=ws[j]*k0*dt; out1[i]+=ws[j]*k1*dt
            column=math.sqrt(col2)
            mean_C[j]+=column
            tri+=abs(ws[j])*column*dt
        inn=math.sqrt(sum(ws[j]**2*dt for j in range(active)))
        out=math.sqrt(sum((out0[i]**2+out1[i]**2)*dt for i in range(N)))
        total_in+=inn; total_out+=out; total_tri+=tri
        max_violation=max(max_violation,out-tri)
        if out<tri:strict+=1
    gamma_est=math.sqrt(sum((x/paths)**2*dt for x in mean_C))
    print(json.dumps({'A':[[-.2,1],[-.6,-.4]],'D':[[1,.2],[-.3,.7]],
      'b':[1,.4],'c':[-.4,1.2],'T':T,'h':h,'sigma':sigma,'paths':paths,'steps':N,'seed':seed,
      'model':'dx=(Ax+b*w_t+c*w_(t-h))dt+sigma*x dW,z=Dx',
      'input':'actual progressive w_t=1+W_t','sample_literal_ratio':total_out/total_in,
      'sample_triangle_ratio':total_tri/total_in,'sampled_kernel_Gamma':gamma_est,
      'H_quadrature':H,'strict_discrete_triangle_paths':strict,
      'max_discrete_triangle_violation':max_violation,
      'limits':'Finite-grid Monte Carlo and floating quadrature; not proof of a gain or endpoint.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
