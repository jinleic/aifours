#!/opt/homebrew/bin/python3
"""Independent check of a rank-four even-half ternary control (not a Boolean witness)."""
import argparse, json, pathlib, collections
def chi(a,b): return 1-2*(bin(a&b).count('1')&1)
def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=pathlib.Path,required=True); p.add_argument('--output',type=pathlib.Path,required=True); a=p.parse_args()
    if a.output.exists(): raise FileExistsError(a.output)
    d=json.loads(a.input.read_text(encoding='utf-8')); u=d['u']
    assert len(u)==256 and set(u)<={-1,0,1}
    Q4=lambda s:((s&1)*((s>>1)&1)+((s>>2)&1)*((s>>3)&1)+((s>>2)&1)+((s>>3)&1))%2
    W={}
    for A in range(256):
        W[A]=sum(u[y]*(1-2*(bin(A&y).count('1')&1)) for y in range(256))
    bad=[]
    for A,w in W.items():
        r,s=A&15,A>>4
        if Q4(s)==0:
            if w not in (0,8,-8): bad.append(A)
        elif w not in (4,-4,12,-12): bad.append(A)
    # local block transform check: y=c+16z, A=r+16s gives A.y=r.c+s.z
    m=sum(abs(x) for x in u); Z=sum(1 for w in W.values() if w==0)
    E=sum(1 for A,w in W.items() if Q4(A>>4)==1 and abs(w)==4)
    hist=collections.Counter(W.values())
    out={'u_sum':sum(u),'m':m,'Z':Z,'E':E,'violations':bad,'walsh_hist':{str(k):v for k,v in sorted(hist.items())},
         'rank4_even_half_conditions':not bad and sum(u)==0,
         'scope':'even half only; peak-28 odd half not addressed; NOT a Boolean function'}
    with a.output.open('x',encoding='utf-8') as fh: json.dump(out,fh,indent=2,sort_keys=True); fh.write('\n')
    print('m',m,'Z',Z,'E',E,'violations',len(bad),'sum',sum(u))
if __name__=='__main__': main()
