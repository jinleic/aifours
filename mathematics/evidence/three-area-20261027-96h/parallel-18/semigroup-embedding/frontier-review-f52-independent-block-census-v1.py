#!/usr/bin/env python3
"""Independent full pair-choice/block census for a fixed 60-term tensor.

Uses a reviewer-owned table parser and new generic block/flattening logic;
no author code or certificates are imported. Exact F_17 specialization uses
sqrt(2)->6. W blocks are certified by a separately written rank lemma.
"""
import importlib.util
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PARSER=HERE/'frontier-review-f35-independent-sector-check-v1.py'
PIN='aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066'
if sha256(PARSER.read_bytes()).hexdigest()!=PIN:
    raise ValueError('reviewer parser pin mismatch')
spec=importlib.util.spec_from_file_location('reviewer_parser',PARSER)
parser=importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)


def require(ok, reason):
    if not ok: raise ValueError(reason)


def hamming_one(support):
    for a,b in combinations(support,2):
        if sum(x!=y for x,y in zip(a,b))==1:
            return a,b
    return None


def rank17(matrix):
    a=[[x%17 for x in row] for row in matrix]
    rows,cols=len(a),len(a[0])
    pivot=0
    for col in range(cols):
        j=next((j for j in range(pivot,rows) if a[j][col]),None)
        if j is None: continue
        a[pivot],a[j]=a[j],a[pivot]
        scale=pow(a[pivot][col],-1,17)
        a[pivot]=[(x*scale)%17 for x in a[pivot]]
        for j in range(rows):
            if j!=pivot and a[j][col]:
                f=a[j][col]
                a[j]=[(x-f*y)%17 for x,y in zip(a[j],a[pivot])]
        pivot+=1
        if pivot==rows: break
    return pivot


def block_flatten_rank(entries,active,left):
    right=tuple(i for i in active if i not in left)
    rows=list(product((0,1),repeat=len(left)))
    cols=list(product((0,1),repeat=len(right)))
    row_index={w:i for i,w in enumerate(rows)}
    col_index={w:i for i,w in enumerate(cols)}
    matrix=[[0]*len(cols) for _ in rows]
    for bits,coefficient in entries:
        row=tuple(bits[i] for i in left)
        col=tuple(bits[i] for i in right)
        # Ring map Z[sqrt2] -> F17; author's source coefficients are real.
        a,b,c,d=coefficient
        require(c==0 and d==0,'unexpected imaginary input')
        matrix[row_index[row]][col_index[col]]=(a+6*b)%17
    return rank17(matrix)


def main(path):
    raw,T=parser.parse(path)
    require(sha256(raw).hexdigest()=='cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38','table pin')
    require(hamming_one(list(T)) is None,'Hamming-one source collision')
    pairs=tuple(combinations(range(6),2))
    census=Counter()
    choices=blocks_seen=total_rank=0
    for pair_choice in product(pairs,repeat=4):
        groups={}
        for coords,coefficient in T.items():
            key=tuple(-1 if coords[i] in pair_choice[i] else coords[i] for i in range(4))
            bits=tuple(pair_choice[i].index(coords[i]) if key[i]==-1 else -1 for i in range(4))
            groups.setdefault(key,[]).append((bits,coefficient))
        choice_rank=0
        for key,entries in groups.items():
            active=tuple(i for i in range(4) if key[i]==-1)
            m,t=len(active),len(entries)
            require(1<=t<=4,('unsupported term count',pair_choice,key,t))
            if t==1:
                category='singleton'; bound=1
            elif t==2:
                support=[a for a,_ in entries]
                require(sum(a!=b for a,b in zip(*support))>=2,'two-term Hamming separation')
                category='two_separated'; bound=2
            elif t==3:
                support=[a for a,_ in entries]
                changing=tuple(i for i in active if len({a[i] for a in support})==2)
                if len(changing)==3:
                    require(all(sum(x!=y for x,y in zip(a,b))>=2 for a,b in combinations(support,2)),
                            'W Hamming collision')
                    category='W' if m==3 else 'W_constant_leg'
                    bound=3
                else:
                    require(m==4 and len(changing)==4,'uncovered three-term geometry')
                    ranks=[block_flatten_rank(entries,active,left) for left in combinations(active,2)
                           if active[0] in left]
                    require(max(ranks)>=3,('missing 3-minor',pair_choice,key,ranks))
                    category='modular3'; bound=3
            else:
                require(m==4,'unexpected four-term block')
                ranks=[block_flatten_rank(entries,active,left) for left in combinations(active,2)
                       if active[0] in left]
                require(max(ranks)==4,('missing 4-minor',pair_choice,key,ranks))
                category='modular4'; bound=4
            require(bound==t,'nonsaturated block')
            census[m,t,category]+=1
            choice_rank+=bound
            blocks_seen+=1
        require(choice_rank==60,('choice bound',pair_choice,choice_rank))
        choices+=1
        total_rank+=choice_rank
    require(choices==50625 and blocks_seen==2993046 and total_rank==60*choices,'coverage totals')
    print('pair_choices=',choices,' nonempty_blocks=',blocks_seen,' certified_support_sum_each=60',sep='')
    for key in sorted(census): print('block',key,'count=',census[key])
    print('PASS every block rank lower certificate equals exact source term count')
    sample=next(iter(T))
    mutation=None
    for i in range(4):
        for z in range(6):
            new=list(sample);new[i]=z;new=tuple(new)
            if new not in T:
                mutation=new;break
        if mutation is not None:break
    require(mutation is not None and hamming_one(list(T)+[mutation]) is not None,'Hamming mutation control')
    print('CONTROL added Hamming-one source coefficient rejected at collision predicate')
    print('LIMIT: F17 ranks prove lower bounds; W block rank3 is a separate written lemma')


if __name__=='__main__':
    require(len(sys.argv)==2,'usage: checker TABLE')
    main(sys.argv[1])
