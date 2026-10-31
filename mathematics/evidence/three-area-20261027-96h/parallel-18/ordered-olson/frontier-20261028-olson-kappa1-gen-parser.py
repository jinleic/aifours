#!/usr/bin/env python3
"""Decide literal GEN parse for same-rotation κ1/e2 fixture at bounded primes."""
import argparse
import json


def build(p,rotation):
    word=[(0,1)]*(2*p-7)+[(rotation,0)]+[(1,1)]*2+[(0,1)]+[(p-1,1)]*2+[(0,1),(rotation,0)]
    for j in range(1,p):
        word += [(j,1),(rotation,0)]
    return tuple(word)


def product(seq,p):
    x,e=0,0
    for y,b in seq:
        x=(x+(-y if e else y))%p
        e ^= b
    return x,e


def good(block,p):
    rot=[a for a,b in block if b==0]
    refs=[a for a,b in block if b==1]
    if len(rot)!=2 or len(refs)!=2:
        return False
    A=(rot[0]+rot[1])%p
    B=(refs[0]-refs[1])%p
    C,parity=product(block,p)
    return parity==0 and (A!=B or C==(2*A)%p)


def parse(word,p):
    n=len(word)
    dp={}
    for width in range(2,n+1,2):
        for left in range(n-width+1):
            right=left+width
            block=word[left:right]
            node=None
            if width==2 and block[0][1]==block[1][1]:
                node=('same-type',left,right)
            elif width==4 and good(block,p):
                node=('good-four',left,right)
            elif width>=4 and block[0][1]==0 and block[-1][1]==0 and (left+1,right-1) in dp:
                node=('rotation-wrap',left,right,dp[(left+1,right-1)])
            else:
                for mid in range(left+2,right-1,2):
                    if (left,mid) in dp and (mid,right) in dp:
                        node=('concat',left,right,dp[(left,mid)],dp[(mid,right)])
                        break
            if node is not None:
                dp[(left,right)]=node
    return dp.get((0,n))


def scan(p,rotation):
    word=build(p,rotation)
    unique=set()
    attempts=0
    for cut in range(len(word)):
        rotated=word[cut:]+word[:cut]
        for omit in range(len(word)):
            rem=rotated[:omit]+rotated[omit+1:]
            if rem in unique:
                continue
            unique.add(rem)
            attempts+=1
            tree=parse(rem,p)
            if tree is not None:
                return {'p':p,'rotation':rotation,'result':'GEN_CERTIFICATE_FOUND',
                        'cut':cut,'omit_in_cut':omit,'unique_inputs_examined':attempts,'tree':tree}
    return {'p':p,'rotation':rotation,'result':'NO_GEN_PARSE_IN_THIS_EXACT_GRAMMAR',
            'unique_inputs_examined':attempts,
            'limits':'not an IPGEN failure: arbitrary inverse-pair insertion is not implemented'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    cases=[]
    for p in (11,13):
        cases.append(scan(p,1))
        cases.append(scan(p,(-pow(2,-1,p))%p))
    result={'result':'BOUNDED_GEN_GRAMMAR_SCAN','cases':cases,
            'scope':'same-type, GOOD4, concat, rotation-wrap; SIX absent since all rotations identical; IP rule NOT included'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
