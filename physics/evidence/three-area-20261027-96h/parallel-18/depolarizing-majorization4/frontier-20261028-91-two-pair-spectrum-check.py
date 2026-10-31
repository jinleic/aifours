#!/usr/bin/env python3
"""Exact two-pair Pauli-frame spectrum and original physical endpoint check."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT = Path(__file__).parent

def load(name, filename):
    spec=importlib.util.spec_from_file_location(name, ROOT/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

frame = load('frame', 'frontier-20261028-26-dicke-pauli-counterexample.py')
endpoint = load('endpoint', 'frontier-20261028-66-noise-endpoint-check.py')
m,c,b,e=endpoint.m,endpoint.c,endpoint.b,endpoint.e


def main():
    vec=[F(0)]*16
    for i,x in ((0,15),(3,36),(12,20),(15,48)): vec[i]=F(x,65)
    rho=[[e.z(vec[i]*vec[j]) for j in range(16)] for i in range(16)]
    assert rho==e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    kappa=F(833,4225)
    spectrum={2+2*kappa:1,F(2):4,2-2*kappa:1,F(0):10}
    actual=frame.local_pauli_frame(rho)
    eig=frame.verify_spectrum(actual,spectrum)
    assert sum(eig[:3])==F(27016,4225)
    assert sum(max(x-F(2),F(0)) for x in eig)==F(1666,4225)
    assert 1+sum(eig[:3])/4==F(10979,4225)<3
    ident=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    P=e.zero(16)
    for i in (0,1,2):P[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        assert len(c.positive_definite_ldl(out))==16
        assert len(c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(141,1000)),e.scale_matrix(out,-1))))==16
        inertia=m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,F(9,100)),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        upper=F(321,1000);ref=F(32,81);assert upper<ref
        actual_p=P if p<1 else e.global_spinflip(P)
        assert actual_p==e.adjoint(actual_p) and e.matmul(actual_p,actual_p)==actual_p and e.trace(actual_p)==e.z(3)
        trace=e.trace(e.matmul(actual_p,out));assert trace[1]==0 and trace[0]<upper
        arr=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
        oeig=np.linalg.eigvalsh(arr)[::-1]
        rows.append({'p':str(p),'pauli_equals_sequential':True,'positive_ldl_pivots':16,
                     'lambda1_upper_ldl_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'top3_upper':str(upper),'reference_top3':str(ref),'gap_lower':str(ref-upper),
                     'same_projector_trace':str(trace[0]),'approximate_top3':oeig[:3].tolist()})
    print(json.dumps({'scope':'one exact pure 2+2 example; not a global proof',
      'state':'(15|0000>+36|0011>+20|1100>+48|1111>)/65',
      'kappa':str(kappa),'frame_spectrum':{str(k):v for k,v in spectrum.items()},
      'frame_top3':str(sum(eig[:3])),'frame_positive_excess':str(F(1666,4225)),
      'same_pair_t1_upper':str(F(10979,4225)),'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__': main()
