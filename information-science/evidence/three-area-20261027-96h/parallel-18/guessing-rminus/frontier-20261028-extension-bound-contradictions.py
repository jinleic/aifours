#!/usr/bin/env python3
"""Find exact one-unknown Shannon bound contradictions for a frozen point.

Only actual entropy coordinates present in the point are treated as known;
all missing coordinates are unknown. No numerical LP result is assumed.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUTPUT=ROOT/'frontier-20261028-extension-bound-contradictions-result.json'
BASE=tuple('abcdefghij')
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values']
    values={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    if len(values)!=len(entries):raise ValueError('DUPLICATE')
    results=[]
    for branch,vars in enumerate(BRANCHES,1):
        bounds={};single=0;knownonly=0;multi=0
        def record(terms,kind):
            nonlocal single,knownonly,multi
            coeff={};constant=Fraction(0)
            for subset,c in terms:
                k=tuple(sorted(subset))
                if not k:continue
                if k in values:constant+=c*values[k]
                else:coeff[k]=coeff.get(k,0)+c
            coeff={k:v for k,v in coeff.items() if v}
            if not coeff:
                knownonly+=1
                if constant<0:raise ValueError(('KNOWN_NEGATIVE',kind,str(constant)))
                return
            if len(coeff)>1:multi+=1;return
            single+=1;(key,c),=coeff.items()
            if c not in (-1,1):raise ValueError(('COEFF',c))
            item=bounds.setdefault(key,{})
            val=-constant/c
            desc={'kind':kind,'terms':[[list(sorted(s)),x] for s,x in terms],
                  'known_constant':str(constant),'unknown_coefficient':c,'bound':str(val)}
            direction='lower' if c>0 else 'upper'
            if direction not in item or (val>item[direction][0] if c>0 else val<item[direction][0]):
                item[direction]=(val,desc)
        universe=set(vars)
        for v in vars:record(((universe,1),(universe-{v},-1)),{'type':'conditional_entropy','v':v})
        for a,b in combinations(vars,2):
            rest=sorted(universe-{a,b})
            for size in range(len(rest)+1):
                for subset in combinations(rest,size):
                    z=set(subset)
                    record(((z|{a},1),(z|{b},1),(z|{a,b},-1),(z,-1)),
                           {'type':'CMI','a':a,'b':b,'condition':list(subset)})
        contradictions=[]
        for k,item in sorted(bounds.items()):
            if 'lower' in item and 'upper' in item and item['lower'][0]>item['upper'][0]:
                contradictions.append({'entropy_variables':list(k),'lower':item['lower'][1],
                                       'upper':item['upper'][1],
                                       'positive_gap':str(item['lower'][0]-item['upper'][0])})
        results.append({'branch':branch,'single_unknown_rows':single,'known_only_rows':knownonly,
                        'multi_unknown_rows':multi,'variables_with_single_bounds':len(bounds),
                        'contradiction_count':len(contradictions),'first_20':contradictions[:20]})
    output={'primal_sha256':EXPECTED,'branches':results,
            'limits':'An exact one-coordinate contradiction disproves extension of this fixed partial point to the branch Shannon cone. Absence of such a contradiction is not a feasibility certificate; no global bound follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
