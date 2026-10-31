#!/usr/bin/env python3
"""Recursive exact replay of a pinned conditioned group-index screen."""
from hashlib import sha256
from math import factorial,gcd
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-coset-index-screen432-result.json','fd8bce56db370e6006510ef1edf40aa89aff9fbcf028c8b3e4ac42f7f249af84')
OUT=ROOT/'frontier-20261028-coset-index-screen432-independent-result.json'


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    source=json.loads(raw);survivors=[];bounded=0
    for m in range(384,432):
        power=m;nu=0
        while power%2==0:nu+=1;power//=2
        divisors=[d for d in range(3,m+1) if m%d==0]
        for b in range(9):
            if b and (not nu or (1<<nu)-1<b):continue
            r=10-b
            def visit(pos,chosen,p,f):
                nonlocal bounded
                if len(chosen)==r:
                    z=p*p;minimum=2 if b else chosen[0]
                    if not z<m**3<=minimum*z:return
                    bounded+=1
                    if f%m:return
                    if r==2:
                        common=gcd(chosen[0],chosen[1]);possible=False
                        for s in range(2,common+1):
                            if common%s==0 and m%s==0:
                                q=m//s
                                if q&(q-1)==0:possible=True
                        if not possible:return
                    survivors.append({'m':m,'binary_count':b,'nonbinary_indices':list(chosen)});return
                for k in range(pos,len(divisors)):
                    d=divisors[k];new=p*d
                    if (new*d**(r-len(chosen)-1))**2>=m**3:break
                    visit(k,chosen+[d],new,f*factorial(d))
            visit(0,[],2**b,2**b)
    def verify(rows):
        if rows!=source['survivors'] or bounded!=source['strict_and_conditioned_product_patterns']:raise ValueError('MISMATCH')
    verify(survivors);bad=[dict(x) for x in survivors];bad[0]['m']=385
    try:verify(bad)
    except ValueError:pass
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'m_range':[384,431],
         'strict_and_conditioned_product_patterns':bounded,'survivors':survivors,'all_checked':True,
         'controls':{'changed_survivor_index':'rejected'},
         'limits':'Exact arithmetic only; the separate group/entropy reductions must still be reviewed.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
