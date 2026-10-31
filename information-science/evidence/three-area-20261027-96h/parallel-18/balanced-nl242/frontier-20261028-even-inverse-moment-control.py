#!/opt/homebrew/bin/python3
"""Check reduced bitvector inverse-moment encoding on an actual ternary half."""
import argparse
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--control',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    k=json.loads(a.control.read_text())['half_spectrum'];assert len(k)==256
    g=[(x//2)%4 for x in k];b=[(2*g[x]-k[x])//8 for x in range(256)]
    assert all(v in(0,1) for v in b) and all(b[x]==0 for x in range(256) if not g[x])
    G=fw(g);B=fw(b);I=fw(k);assert all(v%4==0 for v in G)
    assert all((G[y]-4*B[y])%64==0 for y in range(256)) and all(v in(-128,0,128) for v in I)
    rhs=[(v//4)%16 for v in G]
    for i in range(8):
        for x in range(256):
            if x&(1<<i):rhs[x]=(rhs[x]-rhs[x^(1<<i)])%16
    assert all(rhs[x]==0 for x in range(256) if x.bit_count()>3)
    checks=0
    for mask in range(256):
        d=mask.bit_count()
        if d>3:continue
        assert rhs[mask]%(1<<d)==0
        modulus=1<<(4-d);target=(((-1)**d)*(rhs[mask]//(1<<d)))%modulus
        assert sum(b[x] for x in range(256) if x&mask==mask)%modulus==target;checks+=1
    assert checks==93 and sum(v!=0 for v in I)==62 and max(map(abs,k))==6
    out={'scope':'actual balanced eight-variable ternary half, not nine-variable target witness',
         'all_256_inverse_values_ternary':True,'all_256_divisibility_equations_checked':True,
         'all_93_reduced_moment_equations_checked':True,'half_support':62,'half_peak':6,
         'even_first_sum':sum(k),'E2':sum(abs(x)==2 for x in k)}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('actual ternary half passes all 256 inverse and 93 reduced moment equations')


if __name__=='__main__':main()
