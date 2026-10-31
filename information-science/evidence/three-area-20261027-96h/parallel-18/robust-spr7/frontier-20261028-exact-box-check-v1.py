#!/usr/bin/env python3
"""Independent rational checker for two-frequency in-box SPR obstruction.

Reads the search receipt as data, imports no search code, independently
constructs the four interval corners and exact Routh array and checks every
weighted pairing coefficient and the exact maximum over the entire b-box.
The conclusion is restricted to b in K and conditional on the classical
four-Kharitonov-corner Hurwitz theorem. It is NOT a no-numerator certificate.
Output path is exclusive-created and must be in the assigned root.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def as_q_list(xs):
    return [Q(x) for x in xs]


def construct_corners(lo,hi):
    # Ascending powers. Each pair is the (E-/E+, O-/O+) rectangle vertex.
    ev = ((lo[0],hi[2],lo[4],hi[6]), (hi[0],lo[2],hi[4],lo[6]))
    od = ((lo[1],hi[3],lo[5]), (hi[1],lo[3],hi[5]))
    output = []
    for ee in ev:
        for oo in od:
            output.append([ee[0],oo[0],ee[1],oo[1],ee[2],oo[2],ee[3],Q(1)])
    return output


def routh_exact(a):
    require(len(a)==8 and a[-1]==1, 'not a monic septic')
    descending = a[::-1]
    rows = [descending[0::2], descending[1::2]]
    for _ in range(6):
        upper,lower=rows[-2],rows[-1]
        require(lower[0] != 0, 'zero Routh pivot')
        row=[]
        for j in range(3):
            row.append((lower[0]*upper[j+1]-upper[0]*lower[j+1])/lower[0])
        rows.append(row+[Q(0)])
    col=[r[0] for r in rows]
    require(all(x>0 for x in col), 'nonpositive Routh first-column entry')
    return col


def pair_row(a,t):
    """Compute coefficients of Re[b(iw)conj(a(iw))]/(1+t)^7, t=w²."""
    require(t>=0,'negative frequency square')
    E=sum(((-1)**k)*a[2*k]*t**k for k in range(4))
    O=sum(((-1)**k)*a[2*k+1]*t**k for k in range(4))
    d=(1+t)**7
    ans=[]
    for j in range(8):
        k=j//2
        ans.append(Q((-1)**k)*t**k*E/d if j%2==0 else Q((-1)**k)*t**(k+1)*O/d)
    return ans


def validate(lo,hi,terms):
    require(len(lo)==8 and len(hi)==8 and lo[7]==hi[7]==1, 'leading coefficient mismatch')
    require(all(lo[j]<hi[j] for j in range(7)), 'not seven positive widths')
    require(all(lo[j]>0 for j in range(7)), 'nonpositive interval endpoint')
    cs=construct_corners(lo,hi)
    cols=[routh_exact(a) for a in cs]
    require(len(terms)>=1,'empty certificate')
    coefficient=[Q(0)]*8
    checked=[]
    for corner,t,weight in terms:
        require(0<=corner<4,'corner index out of range')
        require(t>=0,'negative frequency square')
        require(weight>0,'weight must be strictly positive')
        r=pair_row(cs[corner],t)
        coefficient=[v+weight*x for v,x in zip(coefficient,r)]
        checked.append({'corner':corner,'t':str(t),'weight':str(weight)})
    chosen=[hi[j] if coefficient[j]>=0 else lo[j] for j in range(7)]
    maximum=coefficient[7]+sum(coefficient[j]*chosen[j] for j in range(7))
    require(maximum<0,'weighted pairing maximum is not strictly negative')
    return {'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
            'corners':[[str(x) for x in a] for a in cs],
            'routh_first_columns':[[str(x) for x in col] for col in cols],
            'terms':checked, 'weighted_pairing_coefficients':[str(x) for x in coefficient],
            'maximizing_box_endpoint':[str(x) for x in chosen]+['1'],
            'exact_weighted_maximum':str(maximum)}


def nearest_decimal(x,den):
    return Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    data_bytes=Path(args.input).read_bytes()
    data=json.loads(data_bytes)
    raw=data['exact_restricted_certificate']
    require(raw is not None,'search receipt has no exact restricted certificate')
    lo,hi=as_q_list(raw['lower']),as_q_list(raw['upper'])
    raw_terms=[(int(a['corner']),Q(a['t']),Q(a['weight'])) for a in raw['certificate']['weights']]
    original=validate(lo,hi,raw_terms)
    require(Q(original['exact_weighted_maximum'])==Q(raw['certificate']['max_over_b_in_box']),
            'search and independent exact maximum disagree')
    require(len(raw_terms)==2,'simplifier expects exactly two weighted atoms')
    ratio=raw_terms[0][2]/raw_terms[1][2]
    simplified=None
    for power in range(1,8):
        den=10**power
        l=[nearest_decimal(x,den) for x in lo[:7]]+[Q(1)]
        h=[nearest_decimal(x,den) for x in hi[:7]]+[Q(1)]
        for max_den in (3,5,10,20,50,100,200,500,1000,10000):
            r=ratio.limit_denominator(max_den)
            if r<=0:
                continue
            terms=[(raw_terms[0][0],raw_terms[0][1],Q(r.numerator)),
                   (raw_terms[1][0],raw_terms[1][1],Q(r.denominator))]
            try:
                candidate=validate(l,h,terms)
            except ValueError:
                continue
            simplified={'decimal_denominator':den,'weight_ratio':str(r),'certificate':candidate}
            break
        if simplified:
            break
    # Non-vacuous negative controls check the verifier rejects exact wrong claims.
    controls=[]
    bad=[(raw_terms[0][0],raw_terms[0][1],-raw_terms[0][2])]+raw_terms[1:]
    try:
        validate(lo,hi,bad)
    except ValueError as exc:
        require(str(exc)=='weight must be strictly positive','wrong rejection for weight control')
        controls.append({'mutation':'negative first weight','reason':str(exc)})
    else:
        raise ValueError('negative-weight control was not rejected')
    badlo=lo.copy(); badlo[0]=hi[0]
    try:
        validate(badlo,hi,raw_terms)
    except ValueError as exc:
        require(str(exc)=='not seven positive widths','wrong rejection for width control')
        controls.append({'mutation':'collapse first interval','reason':str(exc)})
    else:
        raise ValueError('positive-width control was not rejected')
    with Path(args.output).open('x',encoding='utf-8') as out:
        json.dump({'schema':1,'input_sha256':hashlib.sha256(data_bytes).hexdigest(),
                   'original_independent_exact_check':original,'simplified':simplified,'controls':controls,
                   'stability_assumption':'exact positive Routh columns on four explicit Kharitonov corners; all-member stability follows from classical Kharitonov theorem (named import, not separately formally verified)',
                   'conclusion':'no monic numerator with all seven lower coefficients inside this K can be strictly SPR against the whole K; this does NOT exclude unrestricted numerators'},
                  out,indent=2,sort_keys=True)
        out.write('\n')
    print('ORIGINAL exact negative:',original['exact_weighted_maximum'])
    print('SIMPLIFIED:',json.dumps(simplified,sort_keys=True) if simplified else 'NONE')
    print('CONTROLS:',json.dumps(controls,sort_keys=True))


if __name__=='__main__':
    main()
