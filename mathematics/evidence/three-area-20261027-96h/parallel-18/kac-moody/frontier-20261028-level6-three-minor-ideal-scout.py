#!/usr/bin/env python3
"""Bounded exact three-minor ideal investigation after two-resultant timeouts.

Remove ONLY verified one-sign factors with nonzero constant from three actual
minor tables. Such factors cannot vanish on the closed parameter quadrant.
Investigate the remaining THREE polynomial generators in degree-reverse-lex
order, rather than expanding a degree~8000 two-polynomial resultant.

Native Buchberger has explicit basis/term/coefficient limits. An incomplete
return is INCONCLUSIVE, not a rank or kernel theorem. A positive ideal member
is only a candidate until an explicit generator-combination certificate is
produced and independently checked; no unseen combination is fabricated.
"""
import argparse
import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def terms(poly):
    return [{'x_power':int(i),'y_power':int(j),'coefficient':str(c)} for (i,j),c in sorted(poly.to_dict().items())]


def positive(poly):
    c=poly.to_dict()
    return bool(c.get((0,0),0)) and (all(v>0 for v in c.values()) or all(v<0 for v in c.values()))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a',type=int,required=True)
    ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args()
    ctx=flint.fmpz_mpoly_ctx.get(('x','y'),'degrevlex')
    packets,pins,bads,reports=[],[],[],[]
    prefix=f'frontier-20261028-level6-{args.a}{args.b}6'
    out=ROOT/(prefix+'-three-minor-ideal-scout-v1.json')
    if out.exists():
        raise FileExistsError(out)
    for tag in ('baseline','seed1','seed2'):
        name=prefix+f'-minor-{tag}-v1.json'
        raw=(ROOT/name).read_bytes()
        M=json.loads(raw)
        packets.append(M)
        q={(e['x_power'],e['y_power']):Fraction(e['coefficient']) for e in M['coefficients']}
        den=math.lcm(*(v.denominator for v in q.values()))
        ints={mon:int(c*den) for mon,c in q.items()}
        content=math.gcd(*ints.values())
        poly=ctx.from_dict({m:c//content for m,c in ints.items()})
        constant,factors=poly.factor()
        rebuilt=ctx.constant(constant)
        bad=ctx.constant(1)
        removed=[]
        for fac,exponent in factors:
            rebuilt*=fac**exponent
            if positive(fac):
                removed.append({'factor':terms(fac),'exponent':int(exponent)})
            else:
                bad*=fac**exponent
        assert rebuilt==poly
        bads.append(bad)
        reports.append({'removed_positive_factors':removed,'remaining_generator':terms(bad)})
        pins.append({'file':name,'sha256':hashlib.sha256(raw).hexdigest()})
    assert len({p['pencil_sha256'] for p in packets})==1
    assert len({tuple(p['rows']) for p in packets})==3
    V=flint.fmpz_mpoly_vec(bads,ctx)
    limits=(48,16000,4096)
    start=time.monotonic()
    G,completed=V.buchberger_naive(limits=limits)
    elapsed=time.monotonic()-start
    isgb=bool(G.is_groebner()) if completed else False
    if completed:
        assert isgb
        G=G.autoreduction(groebner=True)
    descriptions=[]
    candidates=[]
    total=0
    for poly in G:
        dd=poly.to_dict()
        total+=len(dd)
        descriptions.append({'total_degree':int(poly.total_degree()),'term_count':len(dd),
                             'maximum_coefficient_bits':max(abs(int(v)).bit_length() for v in dd.values()),
                             'one_sign_nonzero_constant':positive(poly)})
        if positive(poly):
            candidates.append(terms(poly))
    full=bool(completed and total<=20000)
    record={'degree':[args.a,args.b,6],'inputs':pins,'factorizations':reports,
            'field':'Q (primitive integer scaling does not change complex zero sets)',
            'monomial_order':'degrevlex','Buchberger_limits':list(limits),'native_completed':bool(completed),
            'native_Groebner_check':isgb,'seconds':elapsed,'computed_basis_summary':descriptions,
            'basis_total_terms':total,'full_basis_frozen':full,
            'basis_coefficients':[terms(p) for p in G] if full else None,
            'positive_member_candidates':candidates,
            'status':'POSITIVE_MEMBER_CANDIDATE_NEEDS_EXPLICIT_COMBINATION' if candidates else ('COMPLETED_BASIS_STRUCTURE_ONLY' if completed else 'BOUNDED_GROEBNER_INCONCLUSIVE'),
            'limits':'NO original-map rank conclusion yet: explicit ideal-membership combination and independent verification remain required. Incomplete basis/timeout is not a counterexample.'}
    with out.open('x') as stream:
        json.dump(record,stream,indent=2)
        stream.write('\n')
    print('DONE three-minor ideal',record['status'],'completed',completed,'basis size',len(G),'terms',total,out.name,flush=True)


if __name__=='__main__':
    main()
