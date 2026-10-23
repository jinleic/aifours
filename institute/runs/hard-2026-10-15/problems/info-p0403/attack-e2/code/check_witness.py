"""Independent exact direct-character and Mobius checks of a table.

This code does not import any producer or FWHT code. The default minimum
nonlinearity is the frozen target 242. Lower baseline targets require an
explicit command-line argument.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('path')
    p.add_argument('--min-nl',type=int,default=242)
    p.add_argument('--expect-degree',type=int)
    p.add_argument('--xor-zero',action='store_true')
    args=p.parse_args()
    data=json.loads(Path(args.path).read_text())
    txt=data['bits']
    assert len(txt)==512 and set(txt)<={'0','1'}
    bits=list(map(int,txt))
    assert sum(bits)==256
    assert hashlib.sha256(txt.encode()).hexdigest()==data['sha256_ascii_bits']
    W=[]
    for a in range(512):
        W.append(sum(1 if (bits[x]+bin(a&x).count('1'))%2==0 else -1 for x in range(512)))
    assert sum(w*w for w in W)==512*512
    assert W[0]==0
    assert W==data['walsh']
    nl=256-max(map(abs,W))//2
    assert nl==data['nonlinearity'] and nl>=args.min_nl
    coeff=bits.copy()
    for i in range(9):
        for mask in range(512):
            if mask&(1<<i):
                coeff[mask]^=coeff[mask^(1<<i)]
    degree=max((bin(mask).count('1') for mask in range(512) if coeff[mask]),default=0)
    support_xor=0
    for x in range(512):
        if bits[x]:
            support_xor^=x
    if args.expect_degree is not None:
        assert degree==args.expect_degree
    if args.xor_zero:
        assert support_xor==0
    print('PASS direct-character witness check: weight=256, nl=%d, max|W|=%d, degree=%d, support XOR=%d'%(nl,max(map(abs,W)),degree,support_xor))


if __name__=='__main__':
    main()
