#!/usr/bin/env python3
"""Attempt exact rational first-copy Shannon extension of a fixed base profile.

The one-variable conditional-copy equalities are substituted before solving.
Z3 is used only to propose exact rational coordinates; every original 11-var
Shannon row is checked afterward with Fraction. Unknown/timeout proves nothing.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import time
from z3 import Real,SolverFor,Sum,sat

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-exact-first-copy-extension-result.json'
BASE='abcdefghij';COPY=1024;FULL=1023;ALL=2047
Y=FULL^(1<<1)^(1<<2)  # copy b given originals other than b,c
SOLVER_MS=40000


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw);known={sum(1<<BASE.index(v) for v in x['entropy_variables']):Fraction(x['value'])
                                for x in data['primal_values'] if set(x['entropy_variables'])<=set(BASE)}
    if len(known)!=1023:raise ValueError('BASE_COUNT')
    known[0]=Fraction(0)
    # Copy matching on all subsets of Y.
    T=Y
    while True:
        known[T|COPY]=known[T|(1<<1)]
        if not T:break
        T=(T-1)&Y
    # I(copy; b,c |Y)=0 implies all subset equalities by the chain rule.
    for omitted in (0,1<<1,1<<2,(1<<1)|(1<<2)):
        lhs=Y|omitted|COPY;value=known[Y|omitted]+known[Y|(1<<1)]-known[Y]
        if lhs in known and known[lhs]!=value:raise ValueError('COPY_FORCED_CONFLICT')
        known[lhs]=value
    unknown=[m for m in range(1,ALL+1) if m not in known]
    variables={m:Real(f'h_{m}') for m in unknown};solver=SolverFor('QF_LRA');solver.set(timeout=SOLVER_MS)
    for m in unknown:solver.add(variables[m]>=0)
    rows=[];known_only=0
    def add(terms):
        nonlocal known_only
        acc={}
        for m,c in terms:
            if m:acc[m]=acc.get(m,0)+c
        acc={m:c for m,c in acc.items() if c}
        const=sum((c*known[m] for m,c in acc.items() if m in known),Fraction(0))
        rest=[(m,c) for m,c in acc.items() if m not in known]
        if not rest:
            known_only+=1
            if const<0:raise ValueError(('FIXED_SHANNON_CONTRADICTION',terms,str(const)))
        else:
            solver.add(Sum([variables[m]*c for m,c in rest])>=str(-const))
            rows.append((rest,-const))
    for i in range(11):add(((ALL,1),(ALL^(1<<i),-1)))
    for i,j in combinations(range(11),2):
        rest=ALL^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)))
            if not z:break
            z=(z-1)&rest
    solve_t=time.monotonic();status=solver.check();elapsed=time.monotonic()-solve_t
    out={'input_sha256':EXPECTED,'known_entropy_coordinates':len(known)-1,'unknown_entropy_coordinates':len(unknown),
         'known_only_shannon_rows_checked':known_only,'nontrivial_shannon_rows':len(rows),
         'solver_timeout_ms':SOLVER_MS,'solver_status':str(status),'solve_elapsed_s':elapsed,
         'limits':'Only an exactly checked sat extension would prove first-copy Shannon feasibility. It would not establish full three-branch or entropic feasibility.'}
    if status==sat:
        model=solver.model();values={m:Fraction(model.eval(v,model_completion=True).as_fraction()) for m,v in variables.items()}
        if any(v<0 for v in values.values()):raise ValueError('NEGATIVE_COORDINATE')
        for terms,rhs in rows:
            if sum((values[m]*c for m,c in terms),Fraction())<rhs:raise ValueError('EXACT_ROW_FAILURE')
        allvalues=dict(known);allvalues.update(values)
        T=Y;copy_equalities=0
        while True:
            if allvalues[T|COPY]!=allvalues[T|(1<<1)]:raise ValueError('COPY_MARGINAL')
            copy_equalities+=1
            if not T:break
            T=(T-1)&Y
        if allvalues[Y|COPY]+allvalues[FULL]-allvalues[ALL]-allvalues[Y]!=0:raise ValueError('COPY_INDEPENDENCE')
        out.update({'exact_rational_extension_found':True,'all_shannon_rows_checked':known_only+len(rows),
                    'copy_marginal_equalities_checked':copy_equalities,
                    'copy_independence_checked':True,
                    'auxiliary_values':[[m,str(allvalues[m])] for m in range(1024,2048)]})
    out['total_elapsed_s']=time.monotonic()-started
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='auxiliary_values'},indent=2))


if __name__=='__main__':main()
