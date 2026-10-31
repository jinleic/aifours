#!/usr/bin/env python3
"""Independent exact whole-box, no-in-box, and common-numerator verifier.

No imports from the numerical search or Sturm checker. All mathematics uses
fractions.Fraction. The supplied root isolators are verified by exact endpoint
signs and degree counting; positivity is certified by exact Bernstein
coefficients on dyadic subintervals of x=t/(1+t). Output is exclusive-created.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def need(cond,msg):
    if not cond:
        raise ValueError(msg)


def val(p,t):
    z=Q(0)
    for c in reversed(p):
        z=z*t+c
    return z


def corner_members(lo,hi):
    return [[ee[0],oo[0],ee[1],oo[1],ee[2],oo[2],ee[3],Q(1)]
            for ee in ((lo[0],hi[2],lo[4],hi[6]),(hi[0],lo[2],hi[4],lo[6]))
            for oo in ((lo[1],hi[3],lo[5]),(hi[1],lo[3],hi[5]))]


def polynomial_pair(a,b):
    # Direct coefficient expansion of Re[b(iw)a(-iw)]; independent of even/odd convolution.
    c=[Q(0)]*8
    for j in range(8):
        for k in range(8):
            if (j+k)%2==0:
                c[(j+k)//2]+=a[j]*b[k]*(Q(-1)**((j-k)//2))
    return c


def routh(a):
    d=a[::-1]; table=[d[0::2],d[1::2]]
    for _ in range(6):
        u,v=table[-2:]
        need(v[0]>0,'reference Routh pivot nonpositive')
        table.append([(v[0]*u[k+1]-u[0]*v[k+1])/v[0] for k in range(3)]+[Q(0)])
    col=[row[0] for row in table]
    need(all(v>0 for v in col),'reference Routh column nonpositive')
    return col


def verify_box(cert,root_cert):
    lo=[Q(x) for x in cert['lower']]; hi=[Q(x) for x in cert['upper']]
    need(len(lo)==len(hi)==8 and lo[7]==hi[7]==1,'monic degree mismatch')
    need(all(Q(0)<lo[j]<hi[j] for j in range(7)),'interval is not positive width')
    cs=corner_members(lo,hi)
    need([[str(x) for x in row] for row in cs]==cert['corners'],'corner mismatch')
    expect={'Eminus':[lo[0],-hi[2],lo[4],-hi[6]],
            'Eplus':[hi[0],-lo[2],hi[4],-lo[6]],
            'Ominus':[lo[1],-hi[3],lo[5],Q(-1)],
            'Oplus':[hi[1],-lo[3],hi[5],Q(-1)]}
    spans={}
    for key,p in expect.items():
        need([str(x) for x in p]==root_cert['endpoint_cubics'][key],'endpoint cubic mismatch')
        need(p[0]>0 and p[-1]<0,'endpoint sign convention mismatch')
        qspans=[tuple(Q(z) for z in pair) for pair in root_cert['root_intervals'][key]]
        need(len(qspans)==3,'not exactly three root intervals')
        for left,right in qspans:
            need(0<left<right and val(p,left)*val(p,right)<0,'invalid exact root bracket')
        need(all(qspans[i][1]<qspans[i+1][0] for i in range(2)),'root brackets overlap')
        # A cubic has at most three roots counting multiplicity. Three disjoint
        # sign changes imply exactly one simple positive root in each interval.
        spans[key]=qspans
    e=[(min(spans['Eminus'][j][0],spans['Eplus'][j][0]),
        max(spans['Eminus'][j][1],spans['Eplus'][j][1])) for j in range(3)]
    o=[(min(spans['Ominus'][j][0],spans['Oplus'][j][0]),
        max(spans['Ominus'][j][1],spans['Oplus'][j][1])) for j in range(3)]
    bands=[e[0],o[0],e[1],o[1],e[2],o[2]]
    need(all(bands[i][1]<bands[i+1][0] for i in range(5)), 'even/odd bands overlap')
    col=routh(cs[0])
    need([str(x) for x in col]==root_cert['reference_routh_first_column'],'Routh receipt mismatch')
    return lo,hi,cs,bands,col


def separation(lo,hi,cs,terms):
    v=[Q(0)]*8
    for entry in terms:
        i=int(entry['corner']); t=Q(entry['t']); w=Q(entry['weight'])
        need(0<=i<4 and t>=0 and w>0,'invalid weighted pairing atom')
        for j in range(8):
            unit=[Q(0)]*8; unit[j]=Q(1)
            v[j]+=w*val(polynomial_pair(cs[i],unit),t)/(1+t)**7
    endpoint=[hi[j] if v[j]>=0 else lo[j] for j in range(7)]+[Q(1)]
    maximum=sum(v[j]*endpoint[j] for j in range(8))
    need(maximum<0,'no strict rational separation')
    return v,endpoint,maximum


def subdivide(beta):
    rows=[beta]
    while len(rows[-1])>1:
        rows.append([(rows[-1][j]+rows[-1][j+1])/2 for j in range(len(rows[-1])-1)])
    return [row[0] for row in rows],[row[-1] for row in reversed(rows)]


def positive_bernstein(p,max_depth=28,max_nodes=50000):
    need(len(p)==8 and p[0]>0 and p[7]>0,'boundary coefficients must be positive')
    # (1-x)^7 P(x/(1-x)) = sum_k p_k / C(7,k) B_k^7(x).
    initial=[p[k]/math.comb(7,k) for k in range(8)]
    todo=[(Q(0),Q(1),initial,0)]; leaves=[]; count=0
    while todo:
        l,r,b,depth=todo.pop(); count+=1
        if count>max_nodes:
            raise ValueError('Bernstein subdivision node cap')
        if all(x>0 for x in b):
            leaves.append({'left':str(l),'right':str(r),'bernstein':[str(x) for x in b]})
            continue
        if depth>=max_depth:
            raise ValueError('Bernstein subdivision depth exhausted')
        bleft,bright=subdivide(b); mid=(l+r)/2
        todo.append((mid,r,bright,depth+1)); todo.append((l,mid,bleft,depth+1))
    least=min(Q(x) for leaf in leaves for x in leaf['bernstein'])
    need(least>0,'no positive Bernstein margin')
    return {'P':[str(x) for x in p], 'normalized_margin':str(least), 'subdivision_leaves':leaves,
            'subdivision_nodes':count}


def round_q(x,den):
    return Q((2*x.numerator*den+x.denominator)//(2*x.denominator),den)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--box',required=True); p.add_argument('--stability',required=True)
    p.add_argument('--candidate',required=True); p.add_argument('--output',required=True)
    args=p.parse_args()
    rb=Path(args.box).read_bytes(); rs=Path(args.stability).read_bytes(); rc=Path(args.candidate).read_bytes()
    box=json.loads(rb)['simplified']['certificate']; stable=json.loads(rs)
    candidate=json.loads(rc)['exact_candidate']
    need(candidate is not None,'candidate file has no exact b')
    lo,hi,cs,bands,col=verify_box(box,stable)
    v,endpoint,maximum=separation(lo,hi,cs,box['terms'])
    need(maximum==Q(box['exact_weighted_maximum']),'weighted maximum disagrees')
    base=[Q(x) for x in candidate['b']]
    need(len(base)==8 and base[7]==1,'candidate not monic')
    found=None
    # Try simple decimal rounding, then the exact source candidate. Every trial
    # is independently proven or rejected by exact Bernstein arithmetic.
    for den in (1,10,100,1000,10000,100000,1000000):
        for b0 in (Q(1,1000),Q(1,2000),Q(1,4000),base[0]):
            b=[b0]+[round_q(base[j],den) for j in range(1,7)]+[Q(1)]
            try:
                certs=[positive_bernstein(polynomial_pair(a,b)) for a in cs]
            except ValueError:
                continue
            found=(b,certs,den)
            break
        if found:
            break
    if found is None:
        certs=[positive_bernstein(polynomial_pair(a,base)) for a in cs]
        found=(base,certs,None)
    b,certs,den=found
    delta=min(Q(c['normalized_margin']) for c in certs)
    total=sum(hi[j] for j in range(7))+1
    ratio_bound=delta/(total*total)
    # Controls exercise exact boundary and atom validation, not solver behavior.
    controls=[]
    try:
        broken=polynomial_pair(cs[0],[Q(0)]*7+[Q(1)])
        positive_bernstein(broken)
    except ValueError as e:
        need(str(e)=='boundary coefficients must be positive','wrong boundary-control failure')
        controls.append({'mutation':'numerator with zero constant coefficient','reason':str(e)})
    else:
        raise ValueError('zero-constant control was not rejected')
    badterms=[dict(x) for x in box['terms']]; badterms[0]['weight']='-1'
    try:
        separation(lo,hi,cs,badterms)
    except ValueError as e:
        need(str(e)=='invalid weighted pairing atom','wrong negative-weight failure')
        controls.append({'mutation':'negative weighted pairing atom','reason':str(e)})
    else:
        raise ValueError('negative atom control was not rejected')
    out={'schema':1,'inputs_sha256':{'box':hashlib.sha256(rb).hexdigest(),
                                    'stability':hashlib.sha256(rs).hexdigest(),
                                    'candidate':hashlib.sha256(rc).hexdigest()},
         'lower':[str(x) for x in lo],'upper':[str(x) for x in hi],
         'corners':[[str(x) for x in a] for a in cs],
         'verified_root_bands':[[str(x),str(y)] for x,y in bands],
         'verified_reference_routh_first_column':[str(x) for x in col],
         'weighted_pairing_coefficients':[str(x) for x in v],
         'box_maximizing_endpoint':[str(x) for x in endpoint],
         'exact_no_in_box_weighted_maximum':str(maximum),
         'exact_unrestricted_common_numerator':[str(x) for x in b],
         'numerator_lower_coefficients_within_box':all(lo[j]<=b[j]<=hi[j] for j in range(7)),
         'rounding_denominator':den,'corner_bernstein_certificates':certs,
         'common_normalized_pairing_lower_bound':str(delta),
         'box_coefficient_sum_bound':str(total), 'common_real_ratio_lower_bound':str(ratio_bound),
         'negative_controls':controls,
         'proof_scope':'Exact all-member box Hurwitz via root bands/Routh/homotopy; no monic b in box from exact weighted inequality; common monic b outside box from Bernstein positivity at all four corners and pointwise value-rectangle transfer. Root-continuity/Routh are named classical facts, not formal-kernel verification.'}
    with Path(args.output).open('x',encoding='utf-8') as f:
        json.dump(out,f,indent=2,sort_keys=True)
        f.write('\n')
    print('ALL-BOX STABILITY: exact separated root bands + exact reference Routh + homotopy')
    print('NO b IN K: exact weighted maximum',str(maximum))
    print('COMMON b OUTSIDE K:',*[str(x) for x in b])
    print('EXACT NORMALIZED PAIRING MARGIN:',str(delta))
    print('EXACT RATIO LOWER BOUND:',str(ratio_bound))
    print('BERNSTEIN LEAVES:',*[len(c['subdivision_leaves']) for c in certs])
    print('NEGATIVE CONTROLS:',json.dumps(controls))


if __name__=='__main__':
    main()
