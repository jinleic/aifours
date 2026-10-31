#!/usr/bin/env python3
"""Bounded exact-arithmetic search over overlapping gluing substitutions.

The inequality is universal under arbitrary vector substitutions. This is a
sample on one rational original LP point, not an exhaustive nonviolation claim.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
WITNESS=ROOT/'frontier-20261028-five-variable-nonshannon-witness-v1.json'
WHASH='def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392'
OUTPUT=ROOT/'frontier-20261028-fivevar-overlap-sample-result.json'
BATCH=400000;BATCHES=20;SEED=2026102810


def main():
    start=monotonic();raw=INPUT.read_bytes();wr=WITNESS.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(wr).hexdigest()!=WHASH:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];data={tuple(e['entropy_variables']):Fraction(e['value']) for e in entries}
    names='abcdefghij';vals=[Fraction(0)]+[data[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in vals));H=np.array([int(x*scale) for x in vals],dtype=np.int64)
    terms=[(int(m),int(c)) for m,c in json.loads(wr)['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0 or max(abs(int(x)) for x in H)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('TERM_OR_RANGE')
    masks={k:np.array([sum(1<<i for i in c) for c in combinations(range(10),k)],dtype=np.int64) for k in (1,2,3)}
    rng=np.random.default_rng(SEED);checked=0;minimum=None;viol=[]
    for batch in range(BATCHES):
        sizes=rng.choice((1,2,3),size=(BATCH,5),p=(0.45,0.4,0.15));roles=np.empty((BATCH,5),dtype=np.int64)
        for k in (1,2,3):
            sel=sizes==k;roles[sel]=rng.choice(masks[k],size=int(sel.sum()))
        zsize=rng.choice((0,1,2,3),size=BATCH,p=(0.45,0.3,0.2,0.05));z=np.zeros(BATCH,dtype=np.int64)
        for k in (1,2,3):
            sel=zsize==k;z[sel]=rng.choice(masks[k],size=int(sel.sum()))
        value=np.zeros(BATCH,dtype=np.int64)
        for m,c in terms:
            idx=z.copy()
            for j in range(5):
                if m&(1<<j):idx|=roles[:,j]
            value+=c*H[idx]
        checked+=BATCH;local=int(value.min());minimum=local if minimum is None else min(minimum,local)
        if local<0:
            for i in np.flatnonzero(value<0)[:20]:
                viol.append({'role_masks':[int(x) for x in roles[i]],'condition_mask':int(z[i]),
                             'exact_slack':str(Fraction(int(value[i]),scale))})
            break
    out={'profile_sha256':EXPECTED,'inequality_witness_sha256':WHASH,'seed':SEED,'base_scale':scale,
         'scope':'random overlapping nonempty original-variable roles of sizes 1–3, arbitrary sampled conditioning including overlaps',
         'substitutions_checked':checked,'planned_samples':BATCH*BATCHES,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'violations':viol,'elapsed_seconds':monotonic()-start,
         'limits':'A sampled overlap search only, on one rational source-LP point. A nonnegative sample is not an exhaustive bound or an entropy-realization claim.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
