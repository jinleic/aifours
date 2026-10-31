#!/usr/bin/env python3
"""Independent bounded-multiset enumeration for the pinned index screen."""
from hashlib import sha256
from itertools import combinations_with_replacement
from math import factorial,prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-coset-index-screen-result.json','c22c725832df38b9542a9aaf8cb86d4c189878c7779f62650dc601d7b8890fb3')
OUT=ROOT/'frontier-20261028-coset-index-screen-independent-result.json'


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    source=json.loads(raw);patterns=[];survivors=[]
    for m in range(180,288):
        x=m;nu=0
        while x%2==0:nu+=1;x//=2
        for b in range(9):
            if b and (not nu or (1<<nu)-1<b):continue
            r=10-b
            # A largest nonbinary divisor d has r-1 companions >=3.
            choices=[d for d in range(3,m+1) if m%d==0 and ((2**b)*(3**(r-1))*d)**2<m**3]
            for high in combinations_with_replacement(choices,r):
                if (2**b*prod(high))**2>=m**3:continue
                fac=2**b*prod(factorial(d) for d in high);passes=(fac%m==0)
                row={'m':m,'binary_count':b,'nonbinary_indices':list(high),'factorial_divisibility':passes}
                patterns.append(row)
                if passes:survivors.append({k:row[k] for k in ('m','binary_count','nonbinary_indices')})
    def verify(rows):
        kept=[{k:row[k] for k in ('m','binary_count','nonbinary_indices')} for row in rows if row['factorial_divisibility']]
        if len(rows)!=6 or kept!=source['factorial_divisibility_survivors'] or len(rows)!=source['strict_product_bound_patterns']:raise ValueError(('SCREEN',rows))
        if rows[0]!={'m':192,'binary_count':8,'nonbinary_indices':[3,3],'factorial_divisibility':True}:raise ValueError('FIRST')
    verify(patterns)
    altered=[dict(x) for x in patterns];altered[0]['factorial_divisibility']=False
    try:verify(altered)
    except ValueError:pass
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'m_range':[180,287],'exact_product_bound_patterns':patterns,
         'factorial_divisibility_survivors':survivors,'all_checked':True,
         'controls':{'changed_factorial_outcome':'rejected'},
         'limits':'Exact arithmetic screen only; the coset action and group-character reductions are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
