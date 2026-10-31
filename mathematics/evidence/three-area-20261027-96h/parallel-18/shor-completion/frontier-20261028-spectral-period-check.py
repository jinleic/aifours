#!/usr/bin/env python3
"""Exact checks for Shor marginal nonperiodicity and 16-period templates."""
import json

HEAD = {0:5, 3:4, 8:4, 11:3}
TAIL = {0:4, 1:2, 2:3, 4:2, 6:2, 7:1, 13:1, 14:1}


def period_floor(weights,d):
    classes={}
    for i,v in weights.items():classes[i%d]=max(classes.get(i%d,0),v)
    return sum(classes.values())


def remainder2power(weights,d):
    counts=[0]*d
    for i,v in weights.items():counts[i%d]+=v
    return [counts[i]-counts[i+d//2] for i in range(d//2)]


def main():
    table=[]
    for d in range(1,16):
        h,t=period_floor(HEAD,d),period_floor(TAIL,d)
        if h<=d or t<=d:raise AssertionError(('not excluded',d,h,t))
        table.append({'d':d,'head_floor':h,'tail_floor':t})
    if sum(HEAD.values())!=16 or sum(TAIL.values())!=16:
        raise AssertionError('wrong literal anchor count')
    rem={}
    for d in (2,4,8,16):
        h,t=remainder2power(HEAD,d),remainder2power(TAIL,d)
        if not any(h) or not any(t):raise AssertionError(('unexpected Fourier zero',d))
        rem[d]={'head':h,'tail':t}
    uniform={i:1 for i in range(16)}
    if any(any(remainder2power(uniform,d)) for d in (2,4,8,16)):
        raise AssertionError('uniform control has nonzero Fourier residue')
    return {'period_floors':table,'period16_template_fourier_remainders':rem,
            'uniform_spectral_control_passed':True,
            'scope':'exact integer finite identities only; all-order proof separate'}


if __name__=='__main__':print(json.dumps(main(),indent=2))
