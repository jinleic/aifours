#!/usr/bin/env python3
"""Bounded independent check of the *original* hidden-noise plant.

Piecewise-constant adapted inputs; x1, input energy, output energy, and x1
energy use exact per-cell exponential/integral formulas evaluated in floating
point. Hidden x2 uses Euler-Maruyama only as a nonzero-diffusion diagnostic.
This is not a proof of any universal or exact stochastic statement.
"""
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-review-f45-hidden-noise-independent-check-results.json'
N=4096; STEPS=192; T=1.1; A=1.3; SIGMA=0.7; SEED=20261028045


def main():
    rng=np.random.default_rng(SEED);dt=T/STEPS
    decay=np.exp(-A*dt);i1=-np.expm1(-A*dt)/A;i2=-np.expm1(-2*A*dt)/(2*A)
    W=np.zeros(N);x1=np.zeros(N);x2=np.zeros(N)
    input_energy=np.zeros(N);output_energy=np.zeros(N);state_energy=np.zeros(N)
    for _ in range(STEPS):
        # w_i depends only on W up to the start of the current cell.
        w=1.0+0.25*W
        c=w/A;b=x1-c
        input_energy+=dt*w*w
        state_energy+=c*c*dt+2*c*b*i1+b*b*i2
        output_energy+=(w-A*x1)**2*i2
        x1=decay*x1+(1-decay)*c
        dW=np.sqrt(dt)*rng.standard_normal(N)
        x2+=(SIGMA*x2+w)*dW
        W+=dW
    lhs=input_energy-output_energy
    rhs=A*x1*x1+(A*A)*state_energy
    scaled=np.abs(lhs-rhs)/(1+input_energy)
    ratios=np.sqrt(output_energy/input_energy)
    finite=bool(np.isfinite(scaled).all() and np.isfinite(ratios).all() and np.isfinite(x2).all())
    result={'kind':'independent_sampled_original_hidden_noise_energy_identity',
            'plant':'dx1=(-a*x1+w)dt; dx2=(sigma*x2+w)dW; z=w-a*x1',
            'input':'w_i=1+W(t_i)/4, progressive piecewise constant',
            'sample_count':N,'steps':STEPS,'T':T,'a':A,'sigma':SIGMA,'seed':SEED,
            'max_scaled_energy_identity_residual':float(scaled.max()),
            'strict_sample_count':int(np.count_nonzero(output_energy<input_energy)),
            'max_sample_path_ratio':float(ratios.max()),
            'mean_absolute_terminal_hidden_state_euler':float(np.mean(np.abs(x2))),
            'finite':finite,'numpy_version':np.__version__,
            'scope':'Floating-point finite-sample diagnostic; x1 per-cell analytic, hidden x2 Euler approximate. Does not establish universal E1/E2 theorem or exact SDE distribution.',
            'verdict':'PASS' if finite and scaled.max()<1e-10 and np.all(output_energy<input_energy) else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0 if result['verdict']=='PASS' else 1


if __name__=='__main__':raise SystemExit(main())
