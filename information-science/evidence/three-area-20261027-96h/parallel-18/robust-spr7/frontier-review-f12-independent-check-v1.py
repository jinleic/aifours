#!/usr/bin/env python3
"""Independent finite physical checks for f12; no author checker imports.

The deterministic Volterra calculations use closed integrals and separate
midpoint quadrature. A seeded finite Brownian-step experiment checks the
revealed-event linearity caller. Neither proves the all-input theorem, the
strict-E2 premise, E1-only attainer existence, or universal synthesis.
"""
import argparse
import json
import math
import random
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    p.add_argument('--seed',type=int,default=928041)
    p.add_argument('--paths',type=int,default=6000)
    p.add_argument('--steps',type=int,default=160)
    args=p.parse_args()
    if not (1<=args.paths<=20000 and 8<=args.steps<=1000 and args.steps%8==0):
        p.error('bounded paths and steps divisible by8 required')
    k=math.pi/2
    tau=3/8
    st=math.sin(k*tau); ct=math.cos(k*tau)
    sin2=math.sin(2*k*tau)
    tail_energy=(1-tau)/2-sin2/(4*k)
    z_energy=((1-tau)*(0.5+st*st)+sin2/(4*k)-2*st*ct/k)/(k*k)
    input_norm=math.sqrt(0.5)
    tail_norm=math.sqrt(tail_energy)
    output_tail_norm=math.sqrt(z_energy)
    input_inner=tail_energy/input_norm
    output_inner=math.sqrt(2)/k*((1-tau)/2+sin2/(4*k)-st*ct/k)
    gamma=1/k
    angle_in=tail_norm-input_inner
    angle_out=output_tail_norm-output_inner
    deficit=gamma*tail_norm-output_tail_norm
    normal_residual=gamma*input_inner-output_inner
    budget_residual=deficit-(gamma*angle_in-angle_out)
    # Independent midpoint quadrature, not the formulas above.
    nq=20000
    dt=(1-tau)/nq
    numeric_energy=sum(math.cos(k*(tau+(j+0.5)*dt))**2*dt for j in range(nq))
    numeric_out=sum(((math.sin(k*(tau+(j+0.5)*dt))-st)/k)**2*dt for j in range(nq))
    numeric_inner=sum(math.sqrt(2)*math.sin(k*(tau+(j+0.5)*dt))
                      *(math.sin(k*(tau+(j+0.5)*dt))-st)/k*dt for j in range(nq))
    quad_error=max(abs(numeric_energy-tail_energy),abs(numeric_out-z_energy),abs(numeric_inner-output_inner))
    if abs(normal_residual)>1e-12 or abs(budget_residual)>1e-12 or quad_error>1e-8:
        raise ValueError('independent Volterra algebra/quadrature failed')
    # Actual x1'=w, dx2=w dW; event A={W_tau>0}; tail input
    # v=1_A 1_[tau,1] w. Discrete linear caller has shared increments.
    rng=random.Random(args.seed)
    step=1/args.steps; cut=3*args.steps//8
    selected=0; max_x1=0.0; max_x2=0.0
    for _ in range(args.paths):
        W=0.0; x1=x2=0.0; tail1=tail2=0.0; event1=event2=0.0
        event=False
        for j in range(args.steps):
            if j==cut:
                event=W>0
                selected+=int(event)
            dw=rng.gauss(0,math.sqrt(step)); weight=math.cos(k*(j+0.5)*step)
            W+=dw; x1+=weight*step; x2+=weight*dw
            if j>=cut:
                tail1+=weight*step; tail2+=weight*dw
                if event:
                    event1+=weight*step; event2+=weight*dw
                max_x1=max(max_x1,abs(event1-int(event)*tail1))
                max_x2=max(max_x2,abs(event2-int(event)*tail2))
    if max_x1>1e-12 or max_x2>1e-12:
        raise ValueError('discrete revealed-event identity failed')
    result={'schema':1,'model':'u=w; dx1=w dt; dx2=w dW; z=x1; fixed law; T=1, h=0',
            'seed':args.seed,'paths':args.paths,'steps':args.steps,'tau':'3/8',
            'gamma':gamma,'unmasked_tail_input_angle':angle_in,'unmasked_tail_output_angle':angle_out,
            'unmasked_tail_deficit':deficit,'normal_identity_residual':normal_residual,
            'angle_budget_residual':budget_residual,'max_closed_formula_midpoint_error':quad_error,
            'selected_fraction':selected/args.paths,'event_probability_exact':'1/2',
            'max_discrete_event_x1_residual':max_x1,'max_discrete_event_x2_residual':max_x2,
            'scope':'Numerical sanity checks only. This Volterra law has an E2 attainer and deliberately violates the strict-for-all-E2 premise; no endpoint-transfer theorem, E1-only attainer or original synthesis conclusion follows.'}
    with Path(args.output).open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False)
        f.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
