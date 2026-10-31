#!/usr/bin/env python3
"""Independent meet-in-the-middle replay of the zero-fiber 46-subcase.

It independently generates the zero-free universe via balanced columns,
checks orbit coverage from the supplied receipt, and enumerates compatible
four-fiber cliques using bitset intersections. No SMT is used.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));SYMS=(1,2,3);PERMS=list(itertools.permutations(range(4)))


def zero_universe():
    cols=[(x,x,x,x) for x in SYMS]
    for a,b in itertools.combinations(SYMS,2):
      for loc in itertools.combinations(range(4),2):
        cols.append(tuple(a if i in loc else b for i in range(4)))
    if len(cols)!=21:raise ValueError('balanced-column count')
    out=set()
    for C in itertools.product(cols,repeat=4):
        rows=tuple(sorted(tuple(C[j][i] for j in range(4)) for i in range(4)))
        if len(set(rows))!=4:continue
        if any(max(Counter((q[i],q[j]) for q in rows).values())>2 for i,j in PAIRS):continue
        out.add(rows)
    return out


def images(W):
    out=set()
    for p in PERMS:
      for sw in range(16):
        row=[]
        for q in W:
            row.append(tuple(5-q[p[i]] if (sw>>i&1) and q[p[i]] in (2,3) else q[p[i]] for i in range(4)))
        out.add(tuple(sorted(row)))
    return out


def fibers():
    out=set()
    for alph in itertools.product(list(itertools.combinations(SYMS,2)),repeat=3):
      for pair in (-1,0,1,2):
       for sign in (0,1):
        selected=[]
        for q in itertools.product(range(2),repeat=3):
            flag=(q[0]^q[1]^q[2]) if pair==-1 else (q[(pair+1)%3]^q[(pair+2)%3])
            if flag==sign:selected.append(tuple(alph[j][q[j]] for j in range(3)))
        out.add(tuple(sorted(selected)))
    if len(out)!=216:raise ValueError('independent fiber catalog mismatch')
    return sorted(out)


def candidates(W,idx,options,target):
    other=[i for i in range(4) if i!=idx];out=[]
    prior={p:Counter((q[p[0]],q[p[1]]) for q in W) for p in itertools.combinations(other,2)}
    for F in options:
        rows=tuple(tuple(0 if j==idx else q[other.index(j)] for j in range(4)) for q in F)
        values={j:{q[j] for q in rows} for j in other}
        if any(target[j,x]==0 for j in other for x in values[j]):continue
        profiles={p:Counter((q[p[0]],q[p[1]]) for q in rows) for p in itertools.combinations(other,2)}
        if any(any(count+prior[p].get(key,0)>2 for key,count in d.items()) for p,d in profiles.items()):continue
        out.append((rows,profiles))
    return out


def iterbits(x):
    while x:
        b=x&-x;yield b.bit_length()-1;x-=b


def solve(W,F):
    target={(j,x):((4 if x==1 else 6)-sum(q[j]==x for q in W))//2 for j in range(4) for x in SYMS}
    C=[candidates(W,i,F,target) for i in range(4)];edges={}
    for i,j in PAIRS:
        p=tuple(x for x in range(4) if x not in (i,j));prior=Counter((q[p[0]],q[p[1]]) for q in W);table=[]
        for ca in C[i]:
            X=ca[1][p];bits=0
            for h,cb in enumerate(C[j]):
                Y=cb[1][p]
                if all(prior.get(z,0)+X.get(z,0)+Y.get(z,0) in (0,2) for z in set(prior)|set(X)|set(Y)):bits|=1<<h
            table.append(bits)
        edges[i,j]=table
    cliques=matches=0
    for x in range(len(C[0])):
      for y in iterbits(edges[0,1][x]):
       c2=edges[0,2][x]&edges[1,2][y];c3=edges[0,3][x]&edges[1,3][y]
       for z in iterbits(c2):
        for w in iterbits(c3&edges[2,3][z]):
            cliques+=1;S=list(W)+list(C[0][x][0])+list(C[1][y][0])+list(C[2][z][0])+list(C[3][w][0])
            if len(set(S))!=20:raise ValueError('distinct fiber support collision')
            if all(sum(q[j]==v for q in S)==(4 if v<2 else 6) for j in range(4) for v in range(4)):
                for i,j in PAIRS:
                    if any(v!=2 for v in Counter((q[i],q[j]) for q in S).values()):raise ValueError('compatibility gap')
                matches+=1
    return cliques,matches,[len(x) for x in C]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('orbit_receipt',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    data=a.orbit_receipt.read_bytes();source=json.loads(data);records=source['orbit_records']
    universe=zero_universe();covered=set();summaries=[];options=fibers();cliques=matches=0
    for rec in records:
        W=tuple(tuple(q) for q in rec['zero_free']);orbit=images(W)
        if len(orbit)!=rec['orbit_size'] or covered&orbit:raise ValueError('overlapping or wrong-sized orbit')
        covered.update(orbit);c,m,sizes=solve(W,options);cliques+=c;matches+=m
        summaries.append({'zero_free':W,'orbit_size':len(orbit),'fiber_candidate_counts':sizes,'pairwise_compatible_cliques':c,'fiber_count_matches':m})
    if len(records)!=62 or len(universe)!=6804 or covered!=universe:raise ValueError('orbit universe coverage')
    if matches:raise ValueError('unexpected full solution')
    result={'orbit_input_sha256':hashlib.sha256(data).hexdigest(),'independent_zero_free_universe':len(universe),
      'independently_covered_orbits':len(records),'balanced_fiber_catalog':len(options),
      'pairwise_compatible_four_fiber_cliques':cliques,'full_symbol_count_matches':matches,
      'per_orbit':summaries,'scope':'Exact independent meet-in-middle support replay; mathematical completeness of zero-fiber reduction is separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='per_orbit'},indent=2))


if __name__=='__main__':main()
