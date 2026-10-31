#!/opt/homebrew/bin/python3
"""Analyze radical-fiber patterns of the 40 extreme mod-8 relaxation solutions."""
import argparse
import collections
import itertools
import json
import pathlib

TERMS=[sum(1<<i for i in I) for d in range(4) for I in itertools.combinations(range(8),d)]

def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    rows=[];odd=[]
    for x in range(256):
        if g0(x)%2:odd.append(x);continue
        row=sum(1<<j for j,t in enumerate(TERMS) if x&t==t);rhs=(g0(x)//2)%2 ^ int((x&63)!=0);rows.append((row,rhs))
    piv={}
    for row,rhs in rows:
        while row:
            j=row.bit_length()-1
            if j in piv:row^=piv[j][0];rhs^=piv[j][1]
            else:piv[j]=(row,rhs);break
        if not row:assert rhs==0
    free=[j for j in range(len(TERMS)) if j not in piv];assert len(free)==17
    def resolve(seed,inhom):
        value=seed
        for j in sorted(piv):
            row,rhs=piv[j]
            if ((value&(row^(1<<j))).bit_count()%2)^(rhs if inhom else 0):value|=1<<j
        return value
    basis=[resolve(1<<j,False) for j in free];part=resolve(0,True)
    ev=[sum(1<<j for j,t in enumerate(TERMS) if x&t==t) for x in odd]
    def image(v):return sum(1<<i for i,row in enumerate(ev) if (v&row).bit_count()%2)
    cur=image(part)^sum(1<<i for i,x in enumerate(odd) if g0(x)%4==3)
    shifts=[image(v) for v in basis];oldgray=0;patterns=collections.Counter();solutions=[]
    for i in range(1<<17):
        gray=i^(i>>1)
        if i:cur ^= shifts[(gray^oldgray).bit_length()-1]
        oldgray=gray
        if cur.bit_count()!=108:continue
        counts=[]
        for x in range(64):
            if g0(x)%2:
                counts.append(sum((cur>>odd.index(x|(r<<6)))&1 for r in range(4)))
        assert len(counts)==36 and sum(counts)==108
        pattern=tuple(sorted(collections.Counter(counts).items()));patterns[pattern]+=1
        solutions.append({'gray':gray,'fiber_count_histogram':dict(pattern)})
    assert len(solutions)==40
    receipt={'solutions':len(solutions),'radical_fibers':36,
             'fiber_patterns':[{'counts':dict(k),'solutions':v} for k,v in sorted(patterns.items())],
             'models':solutions,'scope':'finite necessary mod8 relaxation, not an actual Boolean target'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('solutions=40 fiber_patterns=',dict(patterns),flush=True)


if __name__=='__main__':main()
