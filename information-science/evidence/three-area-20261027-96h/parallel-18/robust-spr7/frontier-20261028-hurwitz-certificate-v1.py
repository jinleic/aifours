#!/usr/bin/env python3
"""Exact root-band / homotopy certificate of the entire candidate interval box.

No numerical roots or imported search code: using Fraction sign changes, prove
three distinct positive roots for each cubic endpoint, isolate and separate all
EVEN-vs-ODD root bands, verify one actual reference by exact Routh, and invoke
root continuity on the connected coefficient box. This is a direct stability
proof, not an import of the four-corner stability theorem.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def value(p,x):
    result=Q(0)
    for c in reversed(p):
        result=result*x+c
    return result


def scan(p,scale):
    assert len(p)==4 and p[3]!=0 and p[0]!=0
    cap=math.ceil(1+max(abs(c/p[3]) for c in p[:3]))
    previous_t=Q(0); previous_v=value(p,previous_t)
    intervals=[]
    for n in range(1,cap*scale+1):
        t=Q(n,scale); v=value(p,t)
        if v==0:
            continue
        if v*previous_v<0:
            intervals.append((previous_t,t))
        previous_t,previous_v=t,v
    return intervals


def refine(p,left,right,width=Q(1,2**32)):
    leftv=value(p,left)
    if leftv*value(p,right)>=0:
        raise ValueError('initial interval not a strict sign change')
    while right-left>width:
        mid=(left+right)/2
        m=value(p,mid)
        if m==0:
            newleft=(left+mid)/2
            newright=(mid+right)/2
            left,right=newleft,newright
            leftv=value(p,left)
            continue
        if leftv*m<0:
            right=mid
        else:
            left=mid
            leftv=m
    if value(p,left)*value(p,right)>=0:
        raise ValueError('refinement lost sign change')
    return left,right


def isolate(p):
    for scale in (8,64,512,4096):
        initial=scan(p,scale)
        if len(initial)==3:
            intervals=[refine(p,*r) for r in initial]
            if all(intervals[j][1]<intervals[j+1][0] for j in range(2)):
                return intervals
    raise ValueError('did not isolate exactly three positive sign-change roots')


def routh_one(a):
    d=a[::-1]
    rows=[d[0::2],d[1::2]]
    for _ in range(6):
        x,y=rows[-2:]
        if y[0]<=0:
            raise ValueError('nonpositive reference Routh pivot')
        rows.append([(y[0]*x[j+1]-x[0]*y[j+1])/y[0] for j in range(3)]+[Q(0)])
    result=[row[0] for row in rows]
    if any(z<=0 for z in result):
        raise ValueError('reference not certified Hurwitz')
    return result


def qstr(x):
    return str(x)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--output',required=True)
    args=p.parse_args()
    raw=Path(args.input).read_bytes()
    data=json.loads(raw)
    cert=data['simplified']['certificate']
    lo=[Q(x) for x in cert['lower']]
    hi=[Q(x) for x in cert['upper']]
    if not (len(lo)==len(hi)==8 and lo[7]==hi[7]==1 and all(lo[j]<hi[j] for j in range(7))):
        raise ValueError('bad interval/monicity')
    polynomials={'Eminus':[lo[0],-hi[2],lo[4],-hi[6]],
                 'Eplus':[hi[0],-lo[2],hi[4],-lo[6]],
                 'Ominus':[lo[1],-hi[3],lo[5],Q(-1)],
                 'Oplus':[hi[1],-lo[3],hi[5],Q(-1)]}
    intervals={key:isolate(poly) for key,poly in polynomials.items()}
    # Each band encloses the same-index roots of both extremal cubics.
    eb=[(min(intervals['Eminus'][j][0],intervals['Eplus'][j][0]),
         max(intervals['Eminus'][j][1],intervals['Eplus'][j][1])) for j in range(3)]
    ob=[(min(intervals['Ominus'][j][0],intervals['Oplus'][j][0]),
         max(intervals['Ominus'][j][1],intervals['Oplus'][j][1])) for j in range(3)]
    bands=[eb[0],ob[0],eb[1],ob[1],eb[2],ob[2]]
    if not all(bands[j][1]<bands[j+1][0] for j in range(5)):
        raise ValueError('even and odd root bands overlap or are not ordered')
    reference=[Q(x) for x in cert['corners'][0]]
    for j in range(7):
        if not lo[j]<=reference[j]<=hi[j]:
            raise ValueError('reference is not an actual box member')
    routh=routh_one(reference)
    out={'schema':1,'input_sha256':hashlib.sha256(raw).hexdigest(),
         'lower':[qstr(x) for x in lo], 'upper':[qstr(x) for x in hi],
         'endpoint_cubics':{key:[qstr(x) for x in poly] for key,poly in polynomials.items()},
         'root_intervals':{key:[[qstr(x),qstr(y)] for x,y in spans] for key,spans in intervals.items()},
         'ordered_bands':[[qstr(x),qstr(y)] for x,y in bands],
         'endpoint_signs':{key:[[str(value(polynomials[key],x)),str(value(polynomials[key],y))]
                                 for x,y in spans] for key,spans in intervals.items()},
         'actual_reference':[str(x) for x in reference],
         'reference_routh_first_column':[str(x) for x in routh],
         'proof':'Each of four real cubics has three disjoint positive sign-change intervals, so all three roots are real, simple and contained there. Each same-index pair is within its stated band; even-root and odd-root bands are disjoint. Outside all even bands Eminus,Eplus share a strict sign; outside all odd bands Ominus,Oplus share a strict sign. Thus the independent coefficient rectangle never contains zero for any t>0; at t=0 all a0>0. A continuous segment within the connected monic box from the exact-Routh stable reference to any member cannot cross the imaginary axis, so every member is Hurwitz.',
         'imports':'Intermediate value/root counting, exact Routh-Hurwitz criterion for one real polynomial, continuity of roots for fixed-degree monic coefficients; no Kharitonov theorem.'}
    with Path(args.output).open('x',encoding='utf-8') as f:
        json.dump(out,f,indent=2,sort_keys=True)
        f.write('\n')
    print('ALL-BOX HURWITZ CERTIFICATE: six disjoint rational bands; reference Routh positive')
    for name,band in zip(('E1','O1','E2','O2','E3','O3'),bands):
        print(name, str(band[0]), str(band[1]))
    print('reference first column:',*[str(x) for x in routh])


if __name__=='__main__':
    main()
