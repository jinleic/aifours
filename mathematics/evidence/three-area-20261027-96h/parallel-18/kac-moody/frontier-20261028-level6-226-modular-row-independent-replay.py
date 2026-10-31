#!/usr/bin/env python3
"""Replay the full factorization by integer convolutions and residue table."""
import hashlib
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def multiply(a,b):
    out={}
    for (i,j),q in a.items():
        for (u,v),r in b.items():out[i+u,j+v]=out.get((i+u,j+v),0)+q*r
    return {k:v for k,v in out.items() if v}


def main():
    raw=(ROOT/'frontier-20261028-level6-free-22-determinant-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'
    P=json.loads(raw);C=json.loads((ROOT/'frontier-20261028-level6-226-modular-row-certificate-v1.json').read_text())
    assert C['status']=='EXACT_FACTORIZATION_AND_ROOT_FREE_RESIDUE_ROWS'
    original={(a['x_power'],a['y_power']):int(a['coefficient']) for a in P['determinant_coefficients']}
    Qpoly={(a['x_power'],a['y_power']):int(a['coefficient']) for a in C['Q_coefficients']}
    assert len(original)==592 and len(Qpoly)==341
    f1={(0,j):math.comb(7,j)*5**(7-j) for j in range(8)}
    f2={(2,0):4,(0,2):4,(0,0):361,(1,1):8,(1,0):76,(0,1):76}
    exact={k:393216*v for k,v in multiply(multiply(Qpoly,f1),f2).items()}
    assert exact==original
    validated=[];total=0
    for row in C['root_free_rows']:
        p=row['prime'];assert p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
        good=[]
        for x in range(p):
            hasroot=False
            for y in range(p):
                value=sum(c*pow(x,i,p)*pow(y,j,p) for (i,j),c in Qpoly.items())%p;total+=1
                if not value:hasroot=True;break
            if not hasroot:good.append(x)
        assert good==row['good_x_residues'] and good
        validated.append({'prime':p,'good_x_residues':good})
    out=ROOT/'frontier-20261028-level6-226-modular-row-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':P['degree'],'exact_integer_convolution_matches_all_592_coefficients':True,
                               'ten_prime_good_residue_sets':validated,'evaluated_pairs_with_early_root_stop':total,
                               'status':'PASS_FULL_FACTORIZATION_AND_ALL_DECLARED_ROOT_FREE_CLASSES',
                               'scope':'finite-field and factor proof only; source/determinant identity and node exchange separately named; not all-integer coverage'},indent=2)+'\n')
    print('PASS full integer factorization and 10 exact prime residue-class tables;',out.name)

if __name__=='__main__':main()
