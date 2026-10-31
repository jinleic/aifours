#!/usr/bin/env python3
"""Exact disjoint-block/all-generation 2026 family scan on one LP point.

Checks both visually verified five-variable families with a sixth disjoint
conditioning block W. Infinite staircase minimization uses its negative-cell
order ideal; theorem-2 uses an exact discrete quadratic. This is a finite
relaxation-point calculation, not entropic realization or a graph-bound proof.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
SOURCE=ROOT/'frontier-20261028-csirmaz-2026-five-variable.pdf'
SOURCE_SHA='401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6'
OUTPUT=ROOT/'frontier-20261028-conditioned-five-variable-full-scan-result.json'
MAX_NEGATIVE_STAIRCASE_SIDE=1000


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_SHA:
        raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];vals={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    if len(vals)!=len(entries):raise ValueError('DUPLICATE')
    letters='abcdefghij';h=[Fraction(0)]+[vals[tuple(letters[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('SCALE_RANGE')
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    low_n=7**7;idx=np.arange(low_n,dtype=np.int64);low=[np.zeros(low_n,dtype=np.int64) for _ in range(6)];t=idx.copy()
    for i in range(7):
        digit=t%7;t//=7
        for j in range(6):low[j]|=np.where(digit==j+1,1<<i,0)
    total=0;negative1=0;negative2=0;unique={};min1=None;min2=None;max_k=1;violation2=None
    for code in range(7**3):
        t=code;high=[0]*6
        for i in range(7,10):
            digit=t%7;t//=7
            if digit:high[digit-1]|=1<<i
        sets=[low[j]|high[j] for j in range(6)]
        ok=(sets[0]>0)&(sets[1]>0)&(sets[2]>0)&(sets[3]>0)&(sets[0]<sets[1])
        A,B,C,D,Z,W=(x[ok] for x in sets);total+=len(A)
        if not len(A):continue
        g=I(A,B,Z|W)
        common=I(A,Z,B|W)+I(B,Z,A|W)
        c=I(A,C,B|W)+I(B,C,A|W)
        d=I(A,D,B|W)+I(B,D,A|W)
        v=-I(A,B,W)+I(A,B,C|W)+I(A,B,D|W)+I(C,D,W)+common
        if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('NEGATIVE_SHANNON_COMPONENT')
        active=np.flatnonzero(v<0);negative1+=len(active)
        for j in active:
            point=(int(g[j]),int(v[j]),int(c[j]),int(d[j]))
            if point not in unique:unique[point]=[int(x[j]) for x in (A,B,C,D,Z,W)]
        least=int(v.min());min1=least if min1 is None else min(min1,least)
        # Theorem 2 is not symmetric in A/B, so check both orders.
        for X,Y in ((A,B),(B,A)):
            zz=I(X,Z,Y|W)+I(Y,Z,X|W)
            slope=-I(X,C,W)+I(X,C,Y|W)+I(X,C,D|W)+I(Y,D,W)+zz
            Cterm=I(X,C,Y|W)+I(Y,C,X|W)
            if np.any((Cterm==0)&(slope<0)):
                j=int(np.flatnonzero((Cterm==0)&(slope<0))[0]);k=int(g[j]//(-slope[j])+1)
                violation2={'masks':[int(x[j]) for x in (X,Y,C,D,Z,W)],'k':k,
                            'exact_slack':str(Fraction(int(2*g[j]+2*k*slope[j]+k*(k-1)*Cterm[j]),2*scale))}
                break
            nz=Cterm>0;kstar=np.ones(len(X),dtype=np.int64)
            kstar[nz]=np.maximum(1,-np.floor_divide(slope[nz],Cterm[nz]))
            max_k=max(max_k,int(kstar.max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(slope)),np.max(np.abs(Cterm)),1))
            if 2*bound*(max_k+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            twice=2*g+2*kstar*slope+kstar*(kstar-1)*Cterm
            q=int(twice.min());min2=q if min2 is None else min(min2,q)
            negatives=np.flatnonzero(twice<0);negative2+=len(negatives)
            if len(negatives):
                j=int(negatives[0]);k=int(kstar[j])
                violation2={'masks':[int(x[j]) for x in (X,Y,C,D,Z,W)],'k':k,
                            'exact_slack':str(Fraction(int(twice[j]),2*scale))}
                break
        if violation2:break
    expected=(7**10-4*6**10+6*5**10-4*4**10+3**10)//2
    if not violation2 and total!=expected:raise ValueError(('SUBSTITUTION_COUNT',total,expected))
    # The minimum over all finite downward-closed S occurs by including exactly
    # the negative cells v+i*C+j*D. This is itself an order ideal because C,D>=0.
    cases=[];violation1=None;range_blocker=None
    for (g,v,c,d),masks in sorted(unique.items()):
        if c==0 or d==0:
            count=g//(-v)+1
            cells=[(i,0) for i in range(count)] if c==0 else [(0,j) for j in range(count)]
            violation1={'masks':masks,'linear_terms_scaled':[g,v,c,d],
                        'staircase_cells':cells,'exact_slack':str(Fraction(g+count*v,scale))}
            break
        imax=(-v-1)//c;jmax=(-v-1)//d
        if max(imax,jmax)>MAX_NEGATIVE_STAIRCASE_SIDE:
            range_blocker={'masks':masks,'linear_terms_scaled':[g,v,c,d],'imax':imax,'jmax':jmax};break
        alpha=beta=gamma=0;cells=[]
        for i in range(imax+1):
            for j in range((-v-1-i*c)//d+1):
                weight=comb(i+j,i);alpha+=weight;beta+=i*weight;gamma+=j*weight;cells.append((i,j))
        slack=g+alpha*v+beta*c+gamma*d
        cases.append({'masks':masks,'linear_terms_scaled':[g,v,c,d],
                      'negative_cells':len(cells),'minimal_scaled_slack':slack})
        if slack<0:
            violation1={'masks':masks,'linear_terms_scaled':[g,v,c,d],'staircase_cells':cells,
                        'triplet':[alpha,beta,gamma],'exact_slack':str(Fraction(slack,scale))}
            break
    out={'point_sha256':EXPECTED,'source_pdf_sha256':SOURCE_SHA,'scale':scale,
         'scope':'disjoint original blocks A,B,C,D,Z,W; A,B,C,D nonempty, Z/W may be empty; A/B symmetry applied for family1 and both orders checked for family2',
         'substitutions_mod_AB_swap_checked':total,'expected_if_complete':expected,
         'family1_negative_inner_assignments':negative1,'family1_unique_negative_term_profiles':len(unique),
         'family1_min_inner_scaled':min1,'family1_minimization_cases':cases,
         'family1_exact_violation':violation1,'family1_range_blocker':range_blocker,
         'family2_violation_count_before_stop':negative2,'family2_min_twice_scaled':min2,
         'family2_max_candidate_k':max_k,'family2_exact_violation':violation2,
         'elapsed_s':time.monotonic()-start,
         'limits':'One non-entropic-feasibility-unestablished point; overlapping block substitutions and full source-LP feasibility remain open. Source theorem validity needs separate proof review.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
