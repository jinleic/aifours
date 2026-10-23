"""Produce the explicit quadratic attainer for the restricted class."""
import argparse
import hashlib
import json
from pathlib import Path
from seeds import fwht


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--compare',action='store_true')
    args=p.parse_args()
    bits=[]
    for x in range(512):
        b=(x>>0)&1
        for i in (1,3,5,7):
            b^=((x>>i)&1)*((x>>(i+1))&1)
        bits.append(b)
    txt=''.join(map(str,bits))
    W=fwht(bits)
    out={'formula':'x0+x1*x2+x3*x4+x5*x6+x7*x8 over F2','bit_order':'bits[x]=f(x), x=0..511, x_i=(x>>i)&1','bits':txt,'sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(bits),'walsh':W,'nonlinearity':256-max(map(abs,W))//2,'algebraic_degree':2}
    path=Path('results/baseline240.json')
    if args.compare:
        assert json.loads(path.read_text())==out
    else:
        path.write_text(json.dumps(out,indent=2)+'\n')
        broken=out.copy()
        broken['bits']=str(1-int(txt[0]))+txt[1:]
        Path('results/baseline240-broken.json').write_text(json.dumps(broken,indent=2)+'\n')
    print('baseline weight',out['weight'],'nonlinearity',out['nonlinearity'],'sha256',out['sha256_ascii_bits'])


if __name__=='__main__':
    main()
