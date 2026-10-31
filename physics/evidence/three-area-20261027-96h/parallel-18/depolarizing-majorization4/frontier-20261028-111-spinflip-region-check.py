#!/usr/bin/env python3
"""Exact rank-three projector in a nontrivial proven spinflip-dual region."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent

def load(name,filename):
    sp=importlib.util.spec_from_file_location(name,ROOT/filename)
    mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
    return mod

s=load('simple','frontier-20261028-33-simple-frame-witness.py')
r=load('rank6','frontier-20261028-97-rank6-tail-check.py')
e,b,d=s.e,s.b,s.d


def main():
    v=[F(0)]*16;v[0],v[15]=F(12,13),F(5,13)
    Q=[[e.z(v[i]*v[j]) for j in range(16)] for i in range(16)]
    for i in (1,2):Q[i][i]=e.add(Q[i][i],e.ONE)
    assert Q==e.adjoint(Q) and e.matmul(Q,Q)==Q and e.trace(Q)==e.z(3)
    m=[]
    for i in range(4):
        marginal=e.local_marginal(Q,i)
        assert marginal[0][1]==e.ZERO and marginal[1][0]==e.ZERO
        m.append(marginal[0][0][0]-marginal[1][1][0])
    assert m==[F(457,169),F(457,169),F(119,169),F(119,169)]
    S=sum(m);c=(S-6)/2;q=Q[15][15][0]
    assert S==F(1152,169) and c==F(69,169) and q==F(25,169)
    assert min(m)>=3*c/2 and q<=(1-c)/3
    ident=e.zero(16);E=e.zero(16)
    for i in range(16):ident[i][i]=e.ONE
    E[15][15]=e.ONE
    projector_lemma=e.add_matrix(e.add_matrix(e.add_matrix(ident,e.scale_matrix(Q,-1)),e.scale_matrix(E,-c)),
                                 e.scale_matrix(e.add_matrix(ident,e.scale_matrix(E,-1)),c/2))
    assert len(r.c.positive_definite_ldl(projector_lemma))==16
    HQ=r.h1(Q)
    dual=e.add_matrix(e.add_matrix(HQ,e.scale_matrix(Q,-1)),e.scale_matrix(ident,-2))
    assert len(r.c.positive_definite_ldl(dual))==16
    fq=d.local_pauli_frame(Q)
    assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,8),e.scale_matrix(fq,-1))))==16
    u=[F(0)]*16;u[1],u[14]=F(24,25),F(7,25)
    outside=[[e.z(u[i]*u[j]) for j in range(16)] for i in range(16)]
    outside[0][0]=e.add(outside[0][0],e.ONE)
    for i in (3,4):
        for j in (3,4):
            outside[i][j]=e.add(outside[i][j],e.z(F(1,2)))
    assert outside==e.adjoint(outside) and e.matmul(outside,outside)==outside and e.trace(outside)==e.z(3)
    om=[]
    for i in range(4):
        marginal=e.local_marginal(outside,i)
        assert marginal[0][1]==e.ZERO and marginal[1][0]==e.ZERO
        om.append(marginal[0][0][0]-marginal[1][1][0])
    assert om==[F(1777,625),F(1152,625),F(1152,625),F(98,625)]
    oc=(sum(om)-6)/2
    assert sum(om)==F(4179,625) and oc==F(429,1250) and min(om)<3*oc/2
    assert outside[14][14]==e.z(F(49,625))
    outside_dual=e.add_matrix(e.add_matrix(r.h1(outside),e.scale_matrix(outside,-1)),e.scale_matrix(ident,-2))
    assert len(r.c.positive_definite_ldl(outside_dual))==16
    outputs=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(Q,p);assert out==b.direct_pauli(Q,p)
        assert len(r.c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,F(3,8)),e.scale_matrix(out,-1))))==16
        outputs.append({'p':str(p),'dual_upper':'3/8','strict_ldl_pivots':16,'reference':'32/81'})
    print(json.dumps({'scope':'two actual Q and exact constant checks; not an all-Q proof',
                      'm':list(map(str,m)),'S':str(S),'c':str(c),'q':str(q),
                      'm_min_minus_3c_over_2':str(min(m)-3*c/2),'q_gap':str((1-c)/3-q),
                      'projection_lemma_ldl_pivots':16,'H1_minus_Q_minus_2I_LDL_pivots':16,
                      '8I_minus_FQ_LDL_pivots':16,'original_channels':outputs,
                      'uncovered_actual_Q':{'m':list(map(str,om)),'S':str(sum(om)),'c':str(oc),
                                             'weight3_occupancy':'49/625','dual_positive_ldl_pivots':16}},
                     indent=2,sort_keys=True))


if __name__=='__main__':main()
