#!/usr/bin/env python3
"""Exact finite Green-relation check for the pinned 40-element Rees example.

Uses the preceding reviewer-owned explicit multiplication, not an external
semigroup system.  Every principal ideal is computed from the whole source;
no nonmembership is inferred from a truncated word search.
"""
import importlib.util
from hashlib import sha256
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
P=HERE/'frontier-20261028-unit-rees-mixed-checker-v1.py'
PIN='fc39f5641834bb015069d0487897093043300820908711f98f5c5c5c245e5a57'
if sha256(P.read_bytes()).hexdigest()!=PIN:
    raise ValueError('source checker pin mismatch')
spec=importlib.util.spec_from_file_location('unit_rees',P)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def require(ok,why):
    if not ok: raise ValueError(why)


def main():
    B=[None]+list(product(range(2),repeat=2))
    S=[(i,((0,0),e,h),lam) for i,e,h,lam in product(range(2),B,range(2),range(2))]
    E=[a for a in S if m.idem(a)]
    right={a:frozenset([a]+[m.sm(a,x) for x in S]) for a in S}
    left={a:frozenset([a]+[m.sm(x,a) for x in S]) for a in S}
    H={(a,b) for a,b in product(S,repeat=2) if right[a]==right[b] and left[a]==left[b]}
    a=(1,((0,0),None,1),1)
    b=(1,((0,0),None,0),1)
    x=(0,((0,0),(0,0),0),0)
    require((a,b) in H,'source pair not H')
    ax,bx=m.sm(a,x),m.sm(b,x)
    require((ax,bx) not in H,'H congruence negative witness')
    corner_e=(0,((0,0),None,0),0)
    corner={m.sm(m.sm(corner_e,z),corner_e) for z in S}
    ce=[v for v in corner if m.idem(v)]
    noncomm=next((u,v) for u,v in product(ce,repeat=2) if m.sm(u,v)!=m.sm(v,u))
    same=[(u,v) for u,v in product(E,repeat=2) if u!=v and m.actor(u)==m.actor(v)]
    rp=[(u,v) for u,v in same if m.sm(u,v)==v and m.sm(v,u)==u]
    lp=[(u,v) for u,v in same if m.sm(u,v)==u and m.sm(v,u)==v]
    require(rp and lp,'same-actor pair missing')
    require(all(m.beta(u)!=m.beta(v) for u,v in rp+lp),'R/L invariant failure')
    print('source_size=',len(S),' idempotents=',len(E),' H_ordered_pairs=',len(H),sep='')
    print('H_pair=',(a,b),' multiplier=',x,sep='')
    print('right_products=',(ax,bx),' left_ideals_equal=',left[ax]==left[bx],
          ' right_ideals_equal=',right[ax]==right[bx],sep='')
    print('local_corner_idempotent_noncommutativity=',(corner_e,noncomm),sep='')
    print('same_actor_distinct_idempotent_pairs=',len(same),' R=',len(rp),' L=',len(lp),sep='')
    print('PASS actual H-pair becomes non-H after multiplication; local corner not inverse; R/L separated')
    print('LIMIT: one finite source; uses same-owner multiplication implementation')


if __name__=='__main__':main()
