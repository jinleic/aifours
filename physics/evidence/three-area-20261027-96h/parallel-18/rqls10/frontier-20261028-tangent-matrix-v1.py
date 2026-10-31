#!/usr/bin/env python3
"""Generate integer linearized original-vector constraints at a real array.

The real and imaginary perturbation sectors are independent at a real array.
Output sparse rows for modular rank checking. This does not prove nonlinear
integrability of any kernel direction.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent
N=10


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('certificate')
    parser.add_argument('--prefix',default='frontier-20261028-parker13-tangent')
    args=parser.parse_args()
    d=json.loads(Path(args.certificate).read_text())['partial_witness']
    arr=d['array']
    labels=d['labels']
    denom=d['denominator']
    blocks=[[(r,c) for c in range(N)] for r in range(N)]
    blocks += [[(r,c) for r in range(N)] for c in range(N)]
    blocks += [[(r,c) for r in range(N) for c in range(N) if labels[r][c]==k] for k in range(N)]
    assert len(blocks)==30 and all(len(block)==10 for block in blocks)
    vec=[arr[r][c] for r in range(N) for c in range(N)]
    assert all(len(v)==N and sum(z*z for z in v)==denom*denom for v in vec)
    real=[]
    imag=[]
    for x in range(N*N):
        row=[(N*x+k,vec[x][k]) for k in range(N) if vec[x][k]]
        real.append(row)
    for block in blocks:
        for (r,c),(s,d) in combinations(block,2):
            x,y=N*r+c,N*s+d
            assert sum(a*b for a,b in zip(vec[x],vec[y]))==0
            real.append([(N*x+k,vec[y][k]) for k in range(N) if vec[y][k]]
                        +[(N*y+k,vec[x][k]) for k in range(N) if vec[x][k]])
            imag.append([(N*x+k,-vec[y][k]) for k in range(N) if vec[y][k]]
                        +[(N*y+k,vec[x][k]) for k in range(N) if vec[x][k]])
    for kind,rows in (('real',real),('imag',imag)):
        path=HERE/(args.prefix+'-'+kind+'-v2.txt')
        with path.open('w') as f:
            f.write(f'{len(rows)} {N*N*N}\n')
            for row in rows:
                f.write(str(len(row))+''.join(f' {col} {value}' for col,value in row)+'\n')
        print(kind,'rows',len(rows),'columns',N*N*N,'nonzeros',sum(map(len,rows)),'file',path.name)


if __name__=='__main__':
    main()
