#!/usr/bin/env python3
"""Exact all-k singleton-block scan of Csirmaz 2026 Theorem 11.

Tests six distinct original vertices and arbitrary conditioning subsets of
the remaining four. This is a fixed relaxation point, not an entropic law.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
SOURCE=ROOT/'frontier-20261028-csirmaz-ingleton-stability-2026-v1.html'
SOURCE_SHA='36e107ae6654e59885f5ed264237134159238df72ca41072fd0d21e97ccba842'
OUTPUT=ROOT/'frontier-20261028-ingleton-sum-family-scan-result.json'


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_SHA:
        raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];values={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    names='abcdefghij';h=[Fraction(0)]+[values[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(v.denominator for v in h));H=[int(v*scale) for v in h]
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    def Ing(x,y,a,b,w):return -I(x,y,w)+I(x,y,a|w)+I(x,y,b|w)+I(a,b,w)
    count=0;minimum=None;maxk=1;witness=None
    for xi,yi in combinations(range(10),2):
        X,Y=1<<xi,1<<yi;rest=[i for i in range(10) if i not in (xi,yi)]
        for ai in rest:
            A=1<<ai
            for bi in rest:
                if bi==ai:continue
                B=1<<bi;remaining=[v for v in rest if v not in (ai,bi)]
                for ci,di in combinations(remaining,2):
                    C,D=1<<ci,1<<di;others=[v for v in remaining if v not in (ci,di)]
                    for W in range(1<<len(others)):
                        z=sum(1<<v for j,v in enumerate(others) if W&(1<<j));count+=1
                        g=I(X,Y,z)
                        a=I(X,A,Y|z)+I(Y,A,X|z)
                        S=Ing(X,Y,A,B,z)+Ing(X,Y,C,D,z)+I(X,B,Y|z)+I(Y,B,X|z)
                        if g<0 or a<0:raise ValueError('NEGATIVE_SHANNON_TERM')
                        if a==0 and S<0:k=g//(-S)+1
                        elif a==0:k=1
                        else:k=max(1,-(S//(2*a)))
                        maxk=max(maxk,k);slack=g+k*S+k*(k-1)*a
                        minimum=slack if minimum is None else min(minimum,slack)
                        if slack<0:
                            witness={'masks':[X,Y,A,B,C,D,z],'k':k,'g_scaled':g,
                                     'S_scaled':S,'A_scaled':a,'exact_slack':str(Fraction(slack,scale))}
                            break
                    if witness:break
                if witness:break
            if witness:break
        if witness:break
    out={'point_sha256':EXPECTED,'source_sha256':SOURCE_SHA,'scale':scale,
         'formula':'k*(Ing(X,Y,A,B)+Ing(X,Y,C,D)+I(X;B|Y)+I(Y;B|X)) + I(X;Y) + k*(k-1)*(I(X;A|Y)+I(Y;A|X)) >= 0',
         'scope':'six distinct singleton original variables; W any subset of remaining four, all terms conditioned on W; X/Y and C/D symmetries used',
         'substitutions_checked_before_stop':count,'expected_if_complete':604800,
         'max_candidate_k':maxk,'min_scaled_slack':minimum,'exact_violation':witness,
         'elapsed_s':time.monotonic()-started,
         'limits':'Single-coordinate-block scan on one rational LP point. Unchecked block sizes, overlapping substitutions, source theorem review and full LP feasibility remain open.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
