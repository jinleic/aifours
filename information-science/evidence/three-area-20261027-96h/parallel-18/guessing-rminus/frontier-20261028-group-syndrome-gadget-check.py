#!/usr/bin/env python3
"""Check two-syndrome appended-factor gadget on cyclic groups and S3."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent/'frontier-20261028-group-syndrome-gadget-check-result.json'

def check(name,elements,mul,ident,g,mutate=False):
    inv={x:next(y for y in elements if mul(x,y)==ident and mul(y,x)==ident) for x in elements}
    distributions=[];checked=0
    for s in (0,1):
        target=ident if s==0 else g;counts=[Counter() for _ in range(3)]
        for a in elements:
            for b in elements:
                c=mul(mul(inv[b],inv[a]),ident if mutate else target)
                if mul(mul(a,b),c)!=target:raise ValueError('SYNDROME')
                if a!=mul(mul(target,inv[c]),inv[b]):raise ValueError('DECODE_A')
                if b!=mul(mul(inv[a],target),inv[c]):raise ValueError('DECODE_B')
                if c!=mul(mul(inv[b],inv[a]),target):raise ValueError('DECODE_C')
                for i,x in enumerate((a,b,c)):counts[i][x]+=1
                checked+=1
        if any(set(c)!=set(elements) or set(c.values())!={len(elements)} for c in counts):raise ValueError('UNIFORM')
        distributions.append([len(c) for c in counts])
    return {'group':name,'order':len(elements),'binary_selector_and_pair_inputs_checked':checked,'uniform_symbols_per_component':distributions}


def main():
    results=[]
    for m in (2,3,4,5):results.append(check(f'Z/{m}',tuple(range(m)),lambda x,y,m=m:(x+y)%m,0,1))
    els=tuple(permutations(range(3)));e=(0,1,2);g=(1,0,2)
    mul=lambda a,b:tuple(a[b[i]] for i in range(3))
    results.append(check('S3',els,mul,e,g))
    try:check('bad-Z3',tuple(range(3)),lambda x,y:(x+y)%3,0,1,True)
    except ValueError as ex:control=str(ex)
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'all_checked':True,'cases':results,'negative_control':control,
         'limits':'Finite exact gadget checks only. The arbitrary finite-group statement uses the displayed algebraic inverse formulas and written entropy lifting.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
