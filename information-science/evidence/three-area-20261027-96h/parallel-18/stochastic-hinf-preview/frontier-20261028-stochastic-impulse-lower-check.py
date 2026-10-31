#!/usr/bin/env python3
"""One bounded physical pulse experiment: dx=w dW, z=w+x, h=0."""
import json
import math
import random


def integrate(f,lo,hi,n=20000):
    dt=(hi-lo)/n
    return dt/3*(f(lo)+f(hi)+4*sum(f(lo+(2*k-1)*dt) for k in range(1,n//2+1))+2*sum(f(lo+2*k*dt) for k in range(1,n//2)))


def main():
    gaussian=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
    target=integrate(lambda x:math.sqrt(1+x*x)*gaussian(x),-9,9)
    lower=1+(math.sqrt(2)-1)*math.erfc(1/math.sqrt(2))
    eps=(.1,.04,.01); steps=80; paths=30000; rng=random.Random(20261028)
    sums=[0.0]*len(eps)
    for _ in range(paths):
        B=0.0; values=[]
        for _k in range(steps):
            values.append(B); B+=rng.gauss(0.0,1/math.sqrt(steps))
        for j,e in enumerate(eps):
            early=sum((1+math.sqrt(e)*v)**2 for v in values)/steps
            sums[j]+=math.sqrt(early+(1-e)*B*B)
    print(json.dumps({'model':'dx=w dW,z=w+x,h=0,T=1,x0=0',
      'input':'w=1/sqrt(epsilon) on [0,epsilon]','epsilons':eps,
      'sample_E_path_norm':[v/paths for v in sums],
      'gaussian_limit_quadrature':target,'rigorous_symbolic_lower_numeric':lower,
      'paths':paths,'pulse_steps':steps,'seed':20261028,
      'limits':'Riemann/Monte Carlo and truncated floating Gaussian quadrature; not proof or exact gain.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
