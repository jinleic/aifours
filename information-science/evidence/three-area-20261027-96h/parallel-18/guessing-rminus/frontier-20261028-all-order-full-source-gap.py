#!/usr/bin/env python3
"""Check source-LP constraints evaluable on a sparse rational primal point.

Unknown entropy coordinates remain unknown, never assumed zero. Any observed
negative CMI is an explicit obstruction to extending this point to the full
published copy LP. No conclusion is drawn from unevaluable rows.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('cert2',ROOT/'frontier-20261028-gurpinar-certificate-independent.py')
cert=module_from_spec(spec);spec.loader.exec_module(cert)
INPUT=ROOT/'frontier-20261028-all-order-primal-frozen.json'
OUTPUT=ROOT/'frontier-20261028-all-order-full-source-gap-result.json'
EXPECTED='af431478fdad330f5f79fa416bdcaf1c56a56fb30ed4855fc65b50d1cac50545'
BRANCHES=(tuple(cert.BASE)+("b'0",),tuple(cert.BASE)+("d'1","e'1","g'2"),
          tuple(cert.BASE)+("f'3","g'3","h'4"))


def main():
    t=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw)
    values={tuple(x['entropy_variables']):Fraction(x['value']) for x in data['primal_values']}
    if len(values)!=len(data['primal_values']):raise ValueError('DUPLICATE')
    def H(labels):
        return Fraction(0) if not labels else values.get(tuple(sorted(labels)))
    branches=[]
    for number,variables in enumerate(BRANCHES,1):
        branch={'branch':number,'variables':variables,'elemental_rows_total':0,
                'fully_evaluable_rows':0,'unevaluable_rows':0,'negative_rows':0,
                'first_negative_examples':[]}
        def observe(terms,meta):
            branch['elemental_rows_total']+=1
            coordinates=[(H(subset),coef) for subset,coef in terms]
            if any(value is None for value,_ in coordinates):
                branch['unevaluable_rows']+=1;return
            branch['fully_evaluable_rows']+=1
            value=sum((x*c for x,c in coordinates),Fraction(0))
            if value<0:
                branch['negative_rows']+=1
                if len(branch['first_negative_examples'])<10:
                    branch['first_negative_examples'].append({'kind':meta,'terms':[(sorted(s),c) for s,c in terms],
                                                              'exact_value':str(value)})
        allvars=set(variables)
        for v in variables:
            observe([(allvars,1),(allvars-{v},-1)],{'type':'conditional_entropy','variable':v})
        for a,b in combinations(variables,2):
            rest=sorted(allvars-{a,b})
            for size in range(len(rest)+1):
                for chosen in combinations(rest,size):
                    z=set(chosen)
                    observe([(z|{a},1),(z|{b},1),(z|{a,b},-1),(z,-1)],
                            {'type':'CMI','first':a,'second':b,'condition':chosen})
        branches.append(branch)
    forms=cert.copy_forms(); canonical=[k for k in forms if k and k[0][1]>0]
    copy={'forms_total':len(canonical),'fully_evaluable':0,'unevaluable':0,'nonzero':0,'first_nonzero':[]}
    for form in canonical:
        pairs=[(H(set(names)),coef) for names,coef in form]
        if any(x is None for x,_ in pairs):copy['unevaluable']+=1;continue
        copy['fully_evaluable']+=1;value=sum((x*c for x,c in pairs),Fraction(0))
        if value:
            copy['nonzero']+=1
            if len(copy['first_nonzero'])<10:copy['first_nonzero'].append({'form':form,'exact_value':str(value)})
    out={'primal_sha256':EXPECTED,'coordinates':len(values),'branches':branches,
         'all_generated_copy_equalities':copy,'elapsed_s':time.monotonic()-t,
         'limits':'Only already present entropy coordinates are evaluated. A negative evaluable Shannon row or nonzero copy equality proves this exact point is not feasible for the full source LP. Unevaluable rows cannot be counted as passed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
