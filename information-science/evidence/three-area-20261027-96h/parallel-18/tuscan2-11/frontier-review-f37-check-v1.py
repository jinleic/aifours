#!/usr/bin/env python3
"""Independent finite checks for f37, written from its explicit definitions.

Uses direct Sardinas-Patterson residual sets and a prefix-trie factor automaton
for finite family members, raw equal-word witnesses for new prefix residues,
and a full 2048-mask max-plus dynamic program for the period certificate and
cyclic optima. Does not invoke or load any author checker or result file.
"""
import hashlib
import json
import sys
import time
from collections import Counter
from pathlib import Path

A = (0,3,8,11)
Q = (3,5,8,11)
FULL = (1 << 11)-1


def family(n):
    if n%16 or n<32:
        raise ValueError('family requires n=16m>=32')
    m=n//16
    j={3:{v+16*k for v in (0,2,4,6) for k in range(m)},
       8:{v+16*k for v in (0,2,4,6) for k in range(m)},
       0:set((0,1,7,13,14,20,26)),
       11:set((0,1,2,14,16,18,20))}
    j[0].update(v+16*k for v in (30,32,36,42) for k in range(m-2))
    j[11].update(v+16*k for v in (30,32,34,36) for k in range(m-2))
    if any(not 0<=v<n for vals in j.values() for v in vals):
        raise AssertionError('out-of-range tail')
    return j


def word(i,j):
    return 'a'*i+'b'+'a'*j


def sardinas_patterson(code):
    """Actual finite residual-set recurrence; empty residual is ambiguity."""
    code=set(code)
    current={y[len(x):] for x in code for y in code if x!=y and y.startswith(x)}
    seen=set()
    rounds=0
    while current:
        if '' in current:
            return False,rounds
        frozen=frozenset(current)
        if frozen in seen:
            return True,rounds
        seen.add(frozen)
        nxt=set()
        for x in current:
            for y in code:
                if y.startswith(x):
                    nxt.add(y[len(x):])
                if x.startswith(y):
                    nxt.add(x[len(y):])
        current=nxt
        rounds+=1
    return True,rounds


def factor_present(code, pattern):
    """Trie/NFA: every trie prefix is reachable and coaccessible to root."""
    children=[{}]
    terminal=set()
    for codeword in code:
        v=0
        for letter in codeword:
            if letter not in children[v]:
                children[v][letter]=len(children)
                children.append({})
            v=children[v][letter]
        terminal.add(v)
    def closure(states):
        return states|{0} if states & terminal else states
    states=closure(set(range(len(children))))
    for letter in pattern:
        states=closure({children[v][letter] for v in states if letter in children[v]})
        if not states:
            return False
    return bool(states)


def finite_family(n, raw_witnesses):
    j=family(n)
    code={'a'*n}|{word(i,x) for i in A for x in j[i]}
    original={word(0,x) for x in (0,1,7,13,14)}|\
             {word(i,x) for i in (3,8) for x in (0,2,4,6)}|\
             {word(11,x) for x in (0,1,2)}
    if len(original)!=16 or not original<=code or len(code)!=n-1:
        raise AssertionError('family size or original inclusion')
    holes={}
    for r in A:
        sums=[(t+v)%n for t in j[r] for v in A]
        if len(sums)!=len(set(sums)):
            raise AssertionError('row not a direct A-packing')
        holes[r]=sorted(set(range(n))-set(sums))
        for t in set(range(n))-j[r]:
            if not any((t+v)%n in sums for v in A):
                raise AssertionError('an old-row tail could be added')
    if holes[3] or holes[8] or holes[0]!=sorted((6,19,27,n-2)) or holes[11]!=sorted((6,7,15,n-2)):
        raise AssertionError('incorrect family holes')
    d_ud,d_rounds=sardinas_patterson(code)
    e=code|{'bbaab'}
    e_ud,e_rounds=sardinas_patterson(e)
    if not d_ud or not e_ud or factor_present(code,'bbaab') or factor_present(e,'babaab'):
        raise AssertionError('UD or asserted missing factor check failed')
    checked=0
    if raw_witnesses:
        differences={}
        for p in j[3]:
            for q in j[3]:
                differences[(p-q)%n]=(p,q)
        tilings={u:{(x+v)%n:(x,v) for x in j[u] for v in A} for u in (3,8)}
        for r in set(range(n))-set(A):
            if r%2==0 and r%16!=0:
                u=8; p,q=differences[(r-u)%n]; t=3
            elif r%2==1 and r%16!=11:
                u=3; p,q=differences[(r-u)%n]; t=3
            elif r%16==0:
                k=r//16; u=3; p,q=14+16*(k-1),1; t=0
            else:
                k=(r-11)//16; u=8; p,q=1,14+16*(n//16-1-k); t=0
            if p not in j[t] or q not in j[t] or (p-q-r+u)%n:
                raise AssertionError('wrong three-word prefix certificate')
            for s in range(n):
                x,v=tilings[u][s]
                target1=max(p+u,q+r)
                target2=max(x+v,s)
                if (target1-p-u)%n or (target1-q-r)%n or (target2-x-v)%n or (target2-s)%n:
                    raise AssertionError('nonintegral padding')
                left=[word(t,p)]+['a'*n]*((target1-p-u)//n)+[word(u,x)]+['a'*n]*((target2-x-v)//n)+[word(v,0)]
                right=[word(t,q)]+['a'*n]*((target1-q-r)//n)+[word(r,s)]+['a'*n]*((target2-s)//n)+[word(0,0)]
                if left==right or ''.join(left)!=''.join(right) or any(x not in code for x in left):
                    raise AssertionError('invalid actual raw ambiguity')
                if any(x not in code|{word(r,s)} for x in right):
                    raise AssertionError('raw ambiguity uses an unauthorized atom')
                checked+=1
    return {'n':n,'code_words':len(code),'one_b_words':len(code)-1,'original_included':True,
            'd_ud':d_ud,'d_sp_rounds':d_rounds,'e_ud':e_ud,'e_sp_rounds':e_rounds,
            'bbaab_missing_from_d_star':True,'babaab_missing_from_e_star':True,
            'row0_holes':holes[0],'row11_holes':holes[11],
            'new_prefix_actual_raw_witnesses':checked}


def initial_state(anchors):
    legal=[]
    for mask in range(1<<11):
        points={i for i in range(11) if mask & (1<<i)}
        if not set(anchors)<=points:
            continue
        if any(j-i in Q for i in points for j in points if j>i):
            continue
        legal.append(points)
    if len(legal)!=1 or legal[0]!=set(anchors):
        raise AssertionError('first 11 positions not uniquely fixed by anchors')
    # State bit (age-1) for selected positions relative to next index 11.
    mask=sum(1<<(10-i) for i in legal[0])
    return {mask:(len(legal[0]),sum(1<<i for i in legal[0]))}


def step(vector, position, forced, veto):
    out={}
    for mask,(score,path) in vector.items():
        for bit in ((1,) if forced else (0,1)):
            if bit and (veto or any(mask & (1<<(q-1)) for q in Q)):
                continue
            nxt=((mask<<1)&FULL)|bit
            item=(score+bit,path | ((1<<position) if bit else 0))
            if nxt not in out or item[0]>out[nxt][0]:
                out[nxt]=item
    return out


def prefix_vector(anchors,t):
    vec=initial_state(anchors)
    for pos in range(11,t):
        vec=step(vec,pos,anchors==(0,1,7,13,14) and pos in (13,14),False)
    return vec


def cyclic_optimum(anchors,n):
    vec=initial_state(tuple(a for a in anchors if a<11))
    for pos in range(11,n):
        veto=pos>=n-11 and any(n-pos+a in Q for a in anchors if a<11)
        vec=step(vec,pos,anchors==(0,1,7,13,14) and pos in (13,14),veto)
    if not vec:
        raise AssertionError('empty cyclic DP')
    score,path=max(vec.values(),key=lambda item:item[0])
    chosen=[i for i in range(n) if path & (1<<i)]
    if not set(anchors)<=set(chosen) or len(chosen)!=score:
        raise AssertionError('reconstructed witness misses anchors')
    if any((j-i)%n in Q or (i-j)%n in Q for i,j in __import__('itertools').combinations(chosen,2)):
        raise AssertionError('reconstructed witness has a forbidden cyclic difference')
    return score,chosen


def main(argv):
    if len(argv)!=2:
        raise ValueError('usage: SCRIPT OUTPUT.json')
    start=time.monotonic()
    fam=[finite_family(n,n in (32,64)) for n in (32,48,64,80,96)]
    types=[((0,1,7,13,14),129),((0,2,4,6),29),((0,1,2),69)]
    identities=[]
    for anchors,t in types:
        begin=tuple(a for a in anchors if a<11)
        # prefix_vector expects all anchors; initial_state only the first 11.
        def vector_at(length):
            vec=initial_state(begin)
            for pos in range(11,length):
                vec=step(vec,pos,anchors==(0,1,7,13,14) and pos in (13,14),False)
            return vec
        left,right=vector_at(t),vector_at(t+16)
        equal=set(left)==set(right) and all(right[k][0]==left[k][0]+4 for k in left)
        if not equal:
            raise AssertionError('whole vector +4 periodicity mismatch')
        identities.append({'anchors':anchors,'t':t,'states':len(left),'identity_holds':True})
    representatives=[]
    for n in range(140,156):
        values=[]; witnesses=[]
        for anchors,_ in types:
            value,witness=cyclic_optimum(anchors,n)
            values.append(value); witnesses.append(witness)
        representatives.append({'n':n,'row0':values[0],'row3':values[1],
                                'row11':values[2],'outside_lower_bound':n-values[0]-2*values[1]-values[2],
                                'verified_witnesses':witnesses})
    result={'method':'own SP residual recurrence, raw padded word witnesses, trie factor NFA, full-mask max-plus DP',
            'family_cases':fam,'whole_vector_identities':identities,
            'representatives':representatives,'elapsed_ms':round((time.monotonic()-start)*1000),
            'scope':'Finite checks only; all-order assertions require the written induction.'}
    out=Path(argv[1])
    with out.open('x',encoding='utf-8') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({'family_cases':fam,'whole_vector_identities':identities,
                      'representatives':[{k:v for k,v in x.items() if k!='verified_witnesses'} for x in representatives],
                      'elapsed_ms':result['elapsed_ms'],'output':str(out)},sort_keys=True))


if __name__=='__main__':
    main(sys.argv)
