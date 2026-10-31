#!/usr/bin/env python3
"""Bounded actual 2D preview-design diagnostic; numeric, not a proof."""
import json
import math
import random

P=((-0.2,0.8),(-0.5,-0.3)); Q=((0.35,0.7),(-0.2,-0.15))
D=((1.0,0.2),(-0.3,0.7)); C=((-0.4,0.2),(1.2,-0.3))
T=1.5; h=0.45; S=T-h


def tr(A):return tuple(zip(*A))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def plus(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def mul(a,A):return tuple(tuple(a*A[i][j] for j in range(2)) for i in range(2))
def trace(A):return A[0][0]+A[1][1]
def inv(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return ((A[1][1]/d,-A[0][1]/d),(-A[1][0]/d,A[0][0]/d))
def flat(A):return (A[0][0],(A[0][1]+A[1][0])/2,A[1][1])
def mat(x):return ((x[0],x[1]),(x[1],x[2]))


def ode(X,A,B):
    x,y,z=X; a,b=A[0]; c,d=A[1]; e,f=B[0]; g,h=B[1]
    return (2*a*x+2*b*y+e*e*x+2*e*f*y+f*f*z,
            c*x+(a+d)*y+b*z+e*g*x+(e*h+f*g)*y+f*h*z,
            2*c*y+2*d*z+g*g*x+2*g*h*y+h*h*z)


def rk4(x,dt,A,B):
    k1=ode(x,A,B); k2=ode(tuple(x[i]+dt*k1[i]/2 for i in range(3)),A,B)
    k3=ode(tuple(x[i]+dt*k2[i]/2 for i in range(3)),A,B)
    k4=ode(tuple(x[i]+dt*k3[i] for i in range(3)),A,B)
    return tuple(x[i]+dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))


def expP(t):
    k=math.sqrt(.3975); co=math.cos(k*t); si=math.sin(k*t)/k; f=math.exp(-.25*t)
    return ((f*(co+.05*si),f*.8*si),(f*(-.5)*si,f*(co-.05*si)))


def build_design():
    dt=.0015; nh=round(h/dt); ns=round(S/dt)
    w=flat(mm(tr(D),D)); wc=(0.0,0.0,0.0); wh=(0.0,0.0,0.0)
    for i in range(ns):
        wn=rk4(w,dt,tr(P),tr(Q)); t=i*dt
        wc=tuple(wc[j]+dt*((S-t)*w[j]+(S-t-dt)*wn[j])/2 for j in range(3))
        if i<nh:wh=tuple(wh[j]+dt*(w[j]+wn[j])/2 for j in range(3))
        w=wn
    adj=wc
    for _ in range(nh):adj=rk4(adj,dt,tr(P),tr(Q))
    Gb=plus(mul(S,mat(wh)),mat(adj)); Wc=mat(wc); J=mm(tr(expP(h)),Wc)
    N=mm(J,C); L=mul(-1,mm(inv(Gb),N))
    Hc=trace(mm(mm(tr(C),Wc),C))
    Hstar2=Hc-trace(mm(tr(N),mm(inv(Gb),N)))
    return L,math.sqrt(Hc),math.sqrt(max(0.0,Hstar2)),Gb,Wc


def primal_H(L):
    dt=.0015; nh=round(h/dt); ns=round(S/dt)
    x=flat(mm(L,tr(L))); early=0.0; DTD=mm(tr(D),D)
    def obs(v):return trace(mm(DTD,mat(v)))
    for _ in range(nh):
        xn=rk4(x,dt,P,Q); early+=dt*(obs(x)+obs(xn))/2; x=xn
    mu=mm(expP(h),L)
    Xh=plus(plus(mat(x),mm(mu,tr(C))),plus(mm(C,tr(mu)),mm(C,tr(C))))
    y=flat(Xh); late=0.0
    for i in range(ns):
        yn=rk4(y,dt,P,Q); t=i*dt
        late+=dt*((S-t)*obs(y)+(S-t-dt)*obs(yn))/2; y=yn
    return math.sqrt(max(0.0,S*early+late))


def simulate(L,paths=1000,N=100):
    dt=T/N; shift=round(h/dt); active=N-shift; rng=random.Random(20261028)
    input_sum=out0=outstar=0.0
    for _ in range(paths):
        W=0.0; x0=x1=y0=y1=0.0; ws=[]; e0=e1=ew=0.0
        for i in range(N):
            w=(1+W,1-W) if i<active else (0.0,0.0); ws.append(w)
            old=ws[i-shift] if i>=shift else (0.0,0.0)
            d0=C[0][0]*old[0]+C[0][1]*old[1]; d1=C[1][0]*old[0]+C[1][1]*old[1]
            w0=L[0][0]*w[0]+L[0][1]*w[1]; w1=L[1][0]*w[0]+L[1][1]*w[1]
            dw=rng.gauss(0.0,math.sqrt(dt)); W+=dw
            x0,x1=(x0+(P[0][0]*x0+P[0][1]*x1+d0)*dt+(Q[0][0]*x0+Q[0][1]*x1)*dw,
                   x1+(P[1][0]*x0+P[1][1]*x1+d1)*dt+(Q[1][0]*x0+Q[1][1]*x1)*dw)
            y0,y1=(y0+(P[0][0]*y0+P[0][1]*y1+d0+w0)*dt+(Q[0][0]*y0+Q[0][1]*y1)*dw,
                   y1+(P[1][0]*y0+P[1][1]*y1+d1+w1)*dt+(Q[1][0]*y0+Q[1][1]*y1)*dw)
            e0+=((D[0][0]*x0+D[0][1]*x1)**2+(D[1][0]*x0+D[1][1]*x1)**2)*dt
            e1+=((D[0][0]*y0+D[0][1]*y1)**2+(D[1][0]*y0+D[1][1]*y1)**2)*dt
            ew+=(w[0]*w[0]+w[1]*w[1])*dt
        input_sum+=math.sqrt(ew); out0+=math.sqrt(e0); outstar+=math.sqrt(e1)
    return out0/input_sum,outstar/input_sum


def main():
    L,H0,Hstar,Gb,Wc=build_design(); primal=primal_H(L); r0,rstar=simulate(L)
    print(json.dumps({'P':P,'Q':Q,'D':D,'C':C,'T':T,'h':h,'B':'I2','B0':'0','D1':'0',
      'quadratic_Gb':Gb,'quadratic_Wc':Wc,'computed_Lstar':L,
      'H_no_preview':H0,'Hmin_dual':Hstar,'Hmin_primal':primal,
      'absolute_primal_dual_difference':abs(Hstar-primal),
      'sample_input':'w=(1+W,1-W)','paths':1000,'steps':100,'seed':20261028,
      'sample_literal_ratio_no_preview':r0,'sample_literal_ratio_Lstar':rstar,
      'limits':'Floating RK4/trapezoid, finite Euler/Monte Carlo. Not exact optimal literal synthesis or proof.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
