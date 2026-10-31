#!/usr/bin/env python3
"""Check an explicit actual GEN/IPGEN parse of the κ1/e2 family."""
import argparse
import json


def product(letters,p):
    x,b=0,0
    for y,c in letters:
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def build(p):
    word=[[0,1]]*(2*p-7)+[[1,0]]+[[1,1]]*2+[[0,1]]+[[p-1,1]]*2+[[0,1],[1,0]]
    for j in range(1,p):
        word += [[j,1],[1,0]]
    return word


def good(block,p):
    rot=[t for t in block if not t[1]]
    refl=[t for t in block if t[1]]
    if len(rot)!=2 or len(refl)!=2:
        raise ValueError('not a balanced four-block')
    A=(rot[0][0]+rot[1][0])%p
    B=(refl[0][0]-refl[1][0])%p
    C,parity=product(block,p)
    if parity:
        raise ValueError('all-four odd reflection parity')
    return A!=B or C==(2*A)%p,(A,B,C)


def check(p):
    word=build(p)
    if len(word)!=4*p-1:
        raise ValueError('wrong original length')
    retained=word[1:]
    prefix=retained[:2*p-8]
    if any(x!=[0,1] for x in prefix):
        raise ValueError('wrong same-type prefix')
    prefix_depth=len(prefix)//2
    wrapped=retained[2*p-8:2*p]
    if len(wrapped)!=8 or wrapped[0]!=[1,0] or wrapped[-1]!=[1,0] or any(x[1]!=1 for x in wrapped[1:-1]):
        raise ValueError('wrong rotation-wrapped interior')
    if any(wrapped[i][1]!=wrapped[i+1][1] for i in (1,3,5)):
        raise ValueError('interior not same-type paired')
    tail=retained[2*p:]
    if len(tail)!=2*p-2:
        raise ValueError('wrong tail length')
    cases=[]
    inv3=pow(3,-1,p)
    for k in range(0,len(tail),4):
        block=tail[k:k+4]
        if [t[1] for t in block]!=[1,0,1,0]:
            raise ValueError('tail block not FRFR')
        ok,(A,B,C)=good(block,p)
        if not ok or (A,B,C)!=(2%p,(-1)%p,(-1)%p):
            raise ValueError('tail not claimed GOOD form')
        u=(-inv3)%p
        v=(-5*inv3)%p
        if (1+u+v+1)%p or (u+v+2)%p or (A*u+B*v+C)%p:
            raise ValueError('GOOD actual-option moment failure')
        cases.append({'block_start':2*p+k,'A':A,'B':B,'C':C})
    # Mutate the second reflection in the first FRFR block to make B=A;
    # here C=A != 2A, so the literal GOOD condition must reject it.
    mutated=[x[:] for x in tail[:4]]
    mutated[2][0]=(mutated[0][0]-2)%p
    if good(mutated,p)[0]:
        raise ValueError('non-GOOD mutation survived')
    total_depth=prefix_depth+4+2*len(cases)
    if total_depth!=2*p-1 or len(retained)!=4*p-2:
        raise ValueError('wrong total certificate depth or length')
    return {'p':p,'omitted_original_index':0,'prefix_FF_pairs':prefix_depth,
            'wrapped_FF_pairs':3,'wrapped_depth':4,'GOOD_tail_blocks':len(cases),
            'total_depth':total_depth,'nonGOOD_mutation_rejected':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_EXPLICIT_GEN_PARSE','instances':[check(p) for p in (11,13,17,19)],
            'scope':'actual explicit parse and local option moments; no universal parser or complete residual claim'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
