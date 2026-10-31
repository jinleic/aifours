#!/usr/bin/env python3
"""Numerical directional derivative sanity check; not a proof or a witness."""
import importlib.util
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('adam',ROOT/'frontier-20261028-coupled-adam-v1.py')
adam=importlib.util.module_from_spec(spec)
spec.loader.exec_module(adam)
rng=np.random.default_rng(7531)
v=rng.normal(size=(10,100))+1j*rng.normal(size=(10,100))
v/=np.linalg.norm(v,axis=0)
d=rng.normal(size=v.shape)+1j*rng.normal(size=v.shape)
d/=np.linalg.norm(d)
loss,grad=adam.objective_gradient(v,0.05,0.98)
expected=float(np.real(np.vdot(grad,d)))
for h in (1e-4,1e-5,1e-6):
    left=adam.objective_gradient(v-h*d,0.05,0.98)[0]
    right=adam.objective_gradient(v+h*d,0.05,0.98)[0]
    observed=(right-left)/(2*h)
    print('h',h,'loss',loss,'analytic',expected,'central_difference',observed,
          'absolute_error',abs(observed-expected))
