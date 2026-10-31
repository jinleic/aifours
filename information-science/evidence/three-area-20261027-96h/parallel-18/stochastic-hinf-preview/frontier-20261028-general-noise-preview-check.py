#!/usr/bin/env python3
"""Bounded physical noncommuting-matrix Euler and second-moment ODE diagnostic."""
import json
import math
import random

P=((-0.2,0.8),(-0.5,-0.3)); Q=((0.35,0.7),(-0.2,-0.15))
D=((1.0,0.2),(-0.3,0.7)); b=(1.0,0.4); c=(-0.4,1.2)


def drho(X):
    x,y,z=X; a,b0=P[0]; c0,d=P[1]; e,f=Q[0]; g,h=Q[1]
    return (2*a*x+2*b0*y+e*e*x+2*e*f*y+f*f*z,
            c0*x+(a+d)*y+b0*z+e*g*x+(e*h+f*g)*y+f*h*z,
            2*c0*y+2*d*z+g*g*x+2*g*h*y+h*h*z)


def rk4(x,dt,fn):
    k1=fn(x); k2=fn(tuple(x[i]+dt*k1[i]/2 for i in range(len(x))))
    k3=fn(tuple(x[i]+dt*k2[i]/2 for i in range(len(x))))
    k4=fn(tuple(x[i]+dt*k3[i] for i in range(len(x))))
    return tuple(x[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(len(x)))


def observed(X):
    x,y,z=X
    return (D[0][0]**2+D[1][0]**2)*x+2*(D[0][0]*D[0][1]+D[1][0]*D[1][1])*y+(D[0][1]**2+D[1][1]**2)*z


def deterministic_H(T,h):
    S=T-h; dt=0.0005; nh=round(h/dt); ns=round(S/dt)
    X=(b[0]*b[0],b[0]*b[1],b[1]*b[1]); mu=b; early=0.0
    def dmu(v):return (P[0][0]*v[0]+P[0][1]*v[1],P[1][0]*v[0]+P[1][1]*v[1])
    for _ in range(nh):
        Xn=rk4(X,dt,drho); early+=(observed(X)+observed(Xn))*dt/2
        X=Xn; mu=rk4(mu,dt,dmu)
    Y=(X[0]+2*mu[0]*c[0]+c[0]**2,
       X[1]+mu[0]*c[1]+mu[1]*c[0]+c[0]*c[1],
       X[2]+2*mu[1]*c[1]+c[1]**2)
    tail=0.0
    for i in range(ns):
        Yn=rk4(Y,dt,drho)
        tail+=((S-i*dt)*observed(Y)+(S-(i+1)*dt)*observed(Yn))*dt/2
        Y=Yn
    return math.sqrt(S*early+tail)


def main():
    T=1.5; h=.45; N=100; shift=30; active=N-shift; dt=T/N
    paths=1000; seed=20261028; rng=random.Random(seed)
    C=[0.0]*active; C2=[0.0]*active
    input_sum=output_sum=triangle_sum=0.0; strict=0; max_violation=0.0
    for _ in range(paths):
        W=0.0; ws=[]; transitions=[]
        for i in range(N):
            ws.append(1+W); dw=rng.gauss(0.0,math.sqrt(dt)); W+=dw
            transitions.append((1+P[0][0]*dt+Q[0][0]*dw,P[0][1]*dt+Q[0][1]*dw,
                                P[1][0]*dt+Q[1][0]*dw,1+P[1][1]*dt+Q[1][1]*dw))
        out0=[0.0]*N; out1=[0.0]*N; tri=0.0
        for j in range(active):
            y0=y1=0.0; col2=0.0
            for i in range(j,N):
                aa,bb,cc,dd=transitions[i]; y0,y1=aa*y0+bb*y1,cc*y0+dd*y1
                if i==j:y0+=b[0]; y1+=b[1]
                if i==j+shift:y0+=c[0]; y1+=c[1]
                z0=D[0][0]*y0+D[0][1]*y1; z1=D[1][0]*y0+D[1][1]*y1
                col2+=(z0*z0+z1*z1)*dt
                out0[i]+=ws[j]*dt*z0; out1[i]+=ws[j]*dt*z1
            col=math.sqrt(col2); C[j]+=col; C2[j]+=col2; tri+=abs(ws[j])*col*dt
        inn=math.sqrt(sum(ws[j]**2*dt for j in range(active)))
        out=math.sqrt(sum((out0[i]**2+out1[i]**2)*dt for i in range(N)))
        input_sum+=inn; output_sum+=out; triangle_sum+=tri
        max_violation=max(max_violation,out-tri)
        if out<tri:strict+=1
    gamma_est=math.sqrt(sum((x/paths)**2*dt for x in C))
    H_mc=math.sqrt(sum(x/paths*dt for x in C2))
    print(json.dumps({'P':P,'Q':Q,'D':D,'b':b,'c':c,'T':T,'h':h,'paths':paths,'steps':N,'seed':seed,
      'model':'dx=(Px+b*w_t+c*w_(t-h))dt+Qx dW,z=Dx; P,Q do not commute',
      'input':'actual progressive w_t=1+W_t','sample_literal_ratio':output_sum/input_sum,
      'sample_triangle_ratio':triangle_sum/input_sum,'empirical_Gamma':gamma_est,
      'empirical_H':H_mc,'deterministic_H_RK4':deterministic_H(T,h),
      'strict_discrete_triangle_paths':strict,'max_triangle_violation':max_violation,
      'limits':'Euler time grid, finite Monte Carlo, RK4 quadrature; not proof of all-input gain or endpoint.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
