#!/usr/bin/env python3
"""Standard-library encoder for the N47/t27/n9 residual alphabet4444 slices.

NECESSARY E-support conditions only. Exactly20 words on4^4. Local partner degree
vector d=(2,2,2,3). Thirteen party-type multisets cover split S0(h0=h3=1), split
S1(h0=h1=1), merged M0(h3=2), merged M1(h0=2), at most one merged. Pair multiplicities
are 0/2/3 with exact d and h degrees at both ends. Row/column unique overlaps are
forbidden in all3 cuts (a necessary condition for actual complex unitarity).
No amplitudes, P-code completion, or global AME theorem is encoded.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3));IDX=list(itertools.product(range(4),repeat=2))
TYPES={'S0':(1,0,0,1),'S1':(1,1,0,0),'M0':(0,0,0,2),'M1':(2,0,0,0)};DEG=(2,2,2,3)


class Encoder:
    def __init__(self):self.n=0;self.C=[]
    def var(self):self.n+=1;return self.n
    def add(self,*xs):self.C.append(tuple(xs))
    def amk(self,xs,k):
        n=len(xs)
        if k>=n:return
        if k==0:
            for x in xs:self.add(-x)
            return
        s=[[self.var() for _ in range(k)] for _ in range(n-1)]
        self.add(-xs[0],s[0][0])
        for j in range(1,k):self.add(-s[0][j])
        for i in range(1,n-1):
            self.add(-xs[i],s[i][0]);self.add(-s[i-1][0],s[i][0])
            for j in range(1,k):self.add(-xs[i],-s[i-1][j-1],s[i][j]);self.add(-s[i-1][j],s[i][j])
            self.add(-xs[i],-s[i-1][k-1])
        self.add(-xs[-1],-s[-1][k-1])
    def exact(self,xs,k):self.amk(xs,k);self.amk([-x for x in xs],len(xs)-k)


def cases():
    result=[['S0']*k+['S1']*(4-k) for k in range(5)]
    result += [[m]+['S0']*k+['S1']*(3-k) for m in ('M0','M1') for k in range(4)]
    return result


def cell(E,A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return E[tuple(q)]


def encode(typ,overlap=True):
    en=Encoder();E={q:en.var() for q in Q}
    for i in range(4):
        for a in range(4):en.exact([E[q] for q in Q if q[i]==a],2*DEG[a]+TYPES[typ[i]][a])
    for i,j in PAIRS:
        Y={p:en.var() for p in IDX};H={p:en.var() for p in IDX}
        for a,b in IDX:
            xs=[E[q] for q in Q if (q[i],q[j])==(a,b)];y=Y[a,b];h=H[a,b]
            for x in xs:en.add(-x,y)
            en.add(-y,*xs);en.add(-h,y)
            # y implies at least2 xs (each clause omits one possible true input).
            for omitted in range(len(xs)):en.add(-y,*[x for k,x in enumerate(xs) if k!=omitted])
            en.amk(xs,3)
            # At least3 iff h, under the already established cap3.
            for aa,bb in itertools.combinations(range(len(xs)),2):
                en.add(-h,*[x for k,x in enumerate(xs) if k not in (aa,bb)])
            for tri in itertools.combinations(xs,3):en.add(*[-x for x in tri],h)
        for a in range(4):
            en.exact([Y[a,b] for b in range(4)],DEG[a]);en.exact([Y[b,a] for b in range(4)],DEG[a])
            en.exact([H[a,b] for b in range(4)],TYPES[typ[i]][a]);en.exact([H[b,a] for b in range(4)],TYPES[typ[j]][a])
    if overlap:
        for A in CUTS:
            B=tuple(i for i in range(4) if i not in A)
            for side in (0,1):
                for r1,r2 in itertools.combinations(IDX,2):
                    both={};cells={}
                    for c in IDX:
                        a,b=(cell(E,A,r1,B,c),cell(E,A,r2,B,c)) if side==0 else (cell(E,A,c,B,r1),cell(E,A,c,B,r2))
                        v=en.var();both[c]=v;cells[c]=(a,b);en.add(-v,a);en.add(-v,b)
                    for c in IDX:
                        a,b=cells[c];en.add(-a,-b,*[v for t,v in both.items() if t!=c])
    return en,E


def main():
    ap=argparse.ArgumentParser();ap.add_argument('case',type=int);ap.add_argument('out',type=Path);ap.add_argument('--no-overlap',action='store_true');a=ap.parse_args()
    if a.out.exists():raise SystemExit('refusing to overwrite')
    typ=cases()[a.case];en,E=encode(typ,not a.no_overlap)
    with a.out.open('x',encoding='ascii') as f:
        f.write(f'p cnf {en.n} {len(en.C)}\n')
        for row in en.C:f.write(' '.join(map(str,row))+' 0\n')
    meta={'case':a.case,'types':typ,'variables':en.n,'clauses':len(en.C),'E_variables':'first256 in lex order on {0,1,2,3}^4',
      'row_and_column_no_unique_overlap':not a.no_overlap,'cnf_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest(),
      'scope':'Necessary support-only formula; no amplitudes or P completion.'}
    with Path(str(a.out)+'.meta.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2);f.write('\n')
    print(json.dumps(meta,indent=2))


if __name__=='__main__':main()
