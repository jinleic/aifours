#!/usr/bin/env python3
"""Independent rational witness check for the C-projection left-test family."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    sp=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ind=load('ind','frontier-20261028-214-independent-replay.py')
solve=load('obstruct','frontier-20261028-level6-226-naive-accretivity-obstruction.py').solve


def main():
    raw=(ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    P=json.loads(raw);W=json.loads((ROOT/'frontier-20261028-level6-226-projected-axis-obstruction-v1.json').read_text())
    data=[[[Q(q) for q in e] for e in row] for row in P['full_target_affine_entries']];m=len(data);n=34;assert m==235
    A=[{i:data[i][j][0] for i in range(m) if data[i][j][0]} for j in range(n)]
    C=[{i:data[i][j][2] for i in range(m) if data[i][j][2]} for j in range(n)]
    assert len(ind.ReducedSpace(C))==33 and len(ind.ReducedSpace(C+A))==43
    indices=W['slope_basis_columns'];assert len(indices)==33 and len(ind.ReducedSpace([C[j] for j in indices]))==33
    v=[Q(x) for x in W['source_vector']];assert len(v)==n
    Av=[sum((data[i][j][0]*v[j] for j in range(n)),Q(0)) for i in range(m)]
    Cv=[sum((data[i][j][2]*v[j] for j in range(n)),Q(0)) for i in range(m)]
    gram=[[sum((data[t][i][2]*data[t][j][2] for t in range(m)),Q(0)) for j in indices] for i in indices]
    rhs=[sum((data[t][i][2]*Av[t] for t in range(m)),Q(0)) for i in indices]
    coeff=solve(gram,rhs)
    assert all(Av[t]==sum((data[t][j][2]*c for j,c in zip(indices,coeff)),Q(0)) for t in range(m))
    value=2*sum((a*c for a,c in zip(Av,Cv)),Q(0))
    assert value==Q(W['baseline_C_left_quadratic_value']) and value<0
    out=ROOT/'frontier-20261028-level6-226-projected-axis-obstruction-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':[2,2,6],'C_rank':33,'combined_A_C_rank':43,
                               'projected_A_rank':10,'witness_Av_in_imC':True,'quadratic_value':str(value),
                               'status':'PASS_EXACT_ALL_GAMMA_PROJECTED_LEFT_OBSTRUCTION',
                               'scope':'specific X=C+gamma*(I-proj_imC)A family; no D3 kernel or arbitrary-left impossibility'},indent=2)+'\n')
    print('PASS independent rank33/43 and exact Av in imC with negative quadratic witness;',out.name)

if __name__=='__main__':main()
