"""Independent audit of binary-index neighborhood CNFs.

Does not import the producer. Audits every CNF block, every Boolean gate
by its full truth table, all lookup rows, every cardinality subset, all
character parities symbolically, and each ordering circuit on all 2^18
pairs of nine-bit words. Direct-Walsh tests on random complete flip sets
are supplemental sampled controls, explicitly not full-range checks.
Also checks SAT models and converts a zero coefficient to a balanced
table for planted satisfiable variants.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from collections import Counter
from itertools import combinations,product
import hashlib
import json
from pathlib import Path
import random
import re
import numpy as np


def clauses_read(path):
    clauses=[]
    n=m=None
    for line in Path(path).read_text().splitlines():
        if not line or line.startswith('c'): continue
        if line.startswith('p'):
            _,kind,n,m=line.split()
            assert kind=='cnf'
            n,m=int(n),int(m)
        else:
            row=list(map(int,line.split()))
            assert row[-1]==0 and all(row[:-1])
            clauses.append(row[:-1])
    assert len(clauses)==m
    assert all(abs(lit)<=n for row in clauses for lit in row)
    return n,clauses


def literal(lit,values):
    return values[abs(lit)] if lit>0 else not values[abs(lit)]


def audit(prefix,model_log=None,witness=None,samples=64):
    meta=json.loads(Path(prefix+'.encoding.json').read_text())
    n,clauses=clauses_read(prefix+'.cnf')
    assert n==meta['variables'] and len(clauses)==meta['clauses']
    assert hashlib.sha256(Path(prefix+'.cnf').read_bytes()).hexdigest()==meta['cnf_sha256']
    source=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text().split('#### 3.2')[0]
    tables=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',source)
    assert len(tables)==3
    name=meta['seed']
    hx=''.join(dict(zip(('dsbf40','dsbf32','rsbf56'),tables))[name])
    assert hx==meta['seed_hex']
    f=np.array([int(b) for ch in hx for b in format(int(ch,16),'04b')],dtype=np.int32)
    H=np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int32)
    W=H@(1-2*f)
    assert meta['walsh']==W.tolist()
    assert set(abs(W).tolist())=={4,12,20,28}
    r=meta['radius_exact']
    B=meta['bound']
    assert r in (2,4,6,8,10) and B in (28,32,36)
    xs,fs=meta['xs'],meta['fs']
    sel={int(a):s for a,s in meta['zero_selectors'].items()}
    possible=[a for a in range(512) if abs(int(W[a]))<=2*r and (2*r-abs(int(W[a])))%4==0]
    required=meta.get('required_zero_origin')
    if required is None: assert list(sel)==possible
    else: assert required in possible and list(sel)==[required]
    primary={}
    for i in range(r):
        assert len(xs[i])==9
        for j in range(9): primary['x%d_%d'%(i,j)]=xs[i][j]
        primary['f%d'%i]=fs[i]
    primary.update({'zero_%d'%a:s for a,s in sel.items()})
    assert primary==meta['primary']
    assert len(set(primary.values()))==len(primary)
    assert set(primary.values())==set(range(1,len(primary)+1))
    defined=set(primary.values())
    const=1<<(len(primary)+1)
    lin={v:1<<v for v in defined}
    deps={v:1<<v for v in defined}
    gates={}
    gate_order=[]
    roles=Counter()
    lookup_points=[]
    offset=0
    checked_truth_kinds=set()
    for block in meta['blocks']:
        assert block['start']==offset and block['end']>=offset
        rows=clauses[offset:block['end']]
        offset=block['end']
        kind=block['kind']
        if kind=='gate':
            a,b,out=block['a'],block['b'],block['out']
            op=block['op']
            assert type(a) is int and type(b) is int
            assert abs(a)!=abs(b)
            assert abs(a) in defined and abs(b) in defined
            assert out not in defined and out>0
            assert all(abs(v) in (abs(a),abs(b),out) for row in rows for v in row)
            # Universal local gate audit, independent of clause recipes.
            for av,bv,ov in product((False,True),repeat=3):
                env={abs(a):av,abs(b):bv,out:ov}
                aa=literal(a,env)
                bb=literal(b,env)
                want={'xor':aa!=bb,'and':aa and bb,'or':aa or bb}[op]
                holds=all(any(literal(v,env) for v in row) for row in rows)
                assert holds==(ov==want)
            defined.add(out)
            aa=lin.get(abs(a))
            bb=lin.get(abs(b))
            if op=='xor' and aa is not None and bb is not None:
                lin[out]=aa^bb^(const if a<0 else 0)^(const if b<0 else 0)
            else:
                lin[out]=None
            deps[out]=deps[abs(a)]|deps[abs(b)]
            gates[out]=(op,a,b)
            gate_order.append(out)
        elif kind=='lookup':
            i=block['point']
            assert block['bits']==xs[i] and block['out']==fs[i]
            want=[]
            for x in range(512):
                row=[]
                for j,node in enumerate(xs[i]): row.append(-node if (x>>j)&1 else node)
                row.append(fs[i] if int(f[x]) else -fs[i])
                want.append(row)
            assert rows==want
            lookup_points.append(i)
        elif kind=='atmost':
            lits,k,guard=block['lits'],block['k'],block['guard']
            role=block['role']
            roles[role]+=1
            assert all(abs(v) in defined for v in lits)
            assert guard is None or guard in sel.values()
            assert len(lits)==r
            assert 0<=k<r
            expected=[([] if guard is None else [-guard])+[-v for v in subset] for subset in combinations(lits,k+1)]
            assert rows==expected
            # Universal at-most semantics, once per small cardinality kind.
            key=(r,k,guard is not None)
            if key not in checked_truth_kinds:
                generic=list(range(1,r+1))
                generic_rows=[[-v for v in subset] for subset in combinations(generic,k+1)]
                for vals in product((False,True),repeat=r):
                    for g in (False,True):
                        holds=(not g) or all(any(not vals[v-1] for v in row) for row in [[abs(t) for t in row] for row in generic_rows])
                        assert holds==((not g) or sum(vals)<=k)
                checked_truth_kinds.add(key)
            if role.startswith('walsh-'):
                a=int(role.split('-')[-1])
                want=[meta['characters'][i][a]*(1 if W[a]>0 else -1) for i in range(r)]
                assert lits==want and guard is None
                assert k==(B-abs(int(W[a]))+2*r)//4
            elif role.startswith('zero-upper-') or role.startswith('zero-lower-'):
                a=int(role.split('-')[-1])
                want=[meta['characters'][i][a]*(1 if W[a]>0 else -1) for i in range(r)]
                target=(2*r-abs(int(W[a])))//4
                assert guard==sel[a]
                if role.startswith('zero-upper-'): assert lits==want and k==target
                else: assert lits==[-v for v in want] and k==r-target
            else: raise AssertionError(('unrecognized cardinality',role))
        elif kind=='require':
            role=block['role']
            roles[role]+=1
            assert rows==[block['lits']]
            if role.startswith('strict-order-'):
                i=int(role.split('-')[-1])
                assert block['lits']==[meta['less_outputs'][i]]
            elif role=='some-walsh-zero':
                assert block['lits']==list(sel.values())
            elif role=='nonzero-support-xor':
                assert meta['degree_eight_necessary_constraint'] and block['lits']==meta['support_xor']
            elif role.startswith('forced-point-'):
                i,j=map(int,role.split('-')[-2:])
                points=meta['forced_points']
                assert points is not None
                assert block['lits']==[xs[i][j] if (points[i]>>j)&1 else -xs[i][j]]
            else: raise AssertionError(('unrecognized requirement',role))
        else: raise AssertionError(kind)
    assert offset==len(clauses) and defined==set(range(1,n+1))
    assert sorted(lookup_points)==list(range(r))
    # Character circuits are checked symbolically for every point and a.
    def linear_literal(v):
        val=lin.get(abs(v))
        assert val is not None
        return val^(const if v<0 else 0)
    for i in range(r):
        for a in range(512):
            expected=1<<fs[i]
            for j in range(9):
                if (a>>j)&1: expected^=1<<xs[i][j]
            assert linear_literal(meta['characters'][i][a])==expected
    # Full truth tables of each numeric ordering circuit (not sampling).
    xx=np.repeat(np.arange(512,dtype=np.int32),512)
    yy=np.tile(np.arange(512,dtype=np.int32),512)
    for i,out in enumerate(meta['less_outputs']):
        allowed=sum(1<<v for v in xs[i]+xs[i+1])
        assert deps[abs(out)]&~allowed==0
        needed=set()
        def visit(v):
            v=abs(v)
            if v in gates and v not in needed:
                needed.add(v)
                visit(gates[v][1]); visit(gates[v][2])
        visit(out)
        values={}
        for j in range(9):
            values[xs[i][j]]=((xx>>j)&1).astype(bool)
            values[xs[i+1][j]]=((yy>>j)&1).astype(bool)
        for v in gate_order:
            if v not in needed: continue
            op,a,b=gates[v]
            aa=values[abs(a)] if a>0 else ~values[abs(a)]
            bb=values[abs(b)] if b>0 else ~values[abs(b)]
            values[v]={'xor':np.logical_xor,'and':np.logical_and,'or':np.logical_or}[op](aa,bb)
        actual=values[abs(out)] if out>0 else ~values[abs(out)]
        assert np.array_equal(actual,xx<yy)
    expected_roles=Counter({'some-walsh-zero':1})
    expected_roles.update({'strict-order-%d'%i:1 for i in range(r-1)})
    for a in range(512):
        upper=(B-abs(int(W[a]))+2*r)//4
        lower=-((-2*r+B+abs(int(W[a])))//4)
        assert lower<=0
        if upper<r: expected_roles['walsh-%d'%a]=1
        if a in sel:
            target=(2*r-abs(int(W[a])))//4
            if target<r: expected_roles['zero-upper-%d'%a]=1
            if r-target<r: expected_roles['zero-lower-%d'%a]=1
    if meta['degree_eight_necessary_constraint']:
        expected_roles['nonzero-support-xor']=1
        for j,out in enumerate(meta['support_xor']):
            expected=0
            for i in range(r): expected^=1<<xs[i][j]
            assert linear_literal(out)==expected
    if meta['forced_points'] is not None:
        points=meta['forced_points']
        assert len(points)==r and points==sorted(set(points))
        for i in range(r):
            for j in range(9): expected_roles['forced-point-%d-%d'%(i,j)]=1
    assert roles==expected_roles
    # Supplemental sampled end-to-end assignment checks, including an
    # independently decoded satisfying model if one was supplied.
    model=None
    model_points=None
    if model_log:
        model={}
        text=Path(model_log).read_text()
        assert 's SATISFIABLE' in text
        for line in text.splitlines():
            if line.startswith('v '):
                for v in map(int,line.split()[1:]):
                    if v: model[abs(v)]=(v>0)
        assert set(model)==set(range(1,n+1))
        assert all(any(literal(v,model) for v in row) for row in clauses)
        model_points=[sum((1<<j) for j in range(9) if model[xs[i][j]]) for i in range(r)]
    rng=random.Random(20261015)
    cases=[sorted(rng.sample(range(512),r)) for _ in range(samples)]
    cases.append(list(reversed(cases[0])))
    if model_points is not None: cases.append(model_points)
    for points in cases:
        h=f.copy()
        for x in points: h[x]^=1
        wh=H@(1-2*h)
        zeros=np.flatnonzero(wh==0).tolist()
        chosen=next((a for a in zeros if a in sel),next(iter(sel)))
        values={}
        for i in range(r):
            for j in range(9): values[xs[i][j]]=bool((points[i]>>j)&1)
            values[fs[i]]=bool(f[points[i]])
        for a,s in sel.items(): values[s]=(a==chosen)
        for v in gate_order:
            op,a,b=gates[v]
            aa,bb=literal(a,values),literal(b,values)
            values[v]={'xor':aa!=bb,'and':aa and bb,'or':aa or bb}[op]
        actual=all(any(literal(v,values) for v in row) for row in clauses)
        expected=points==sorted(set(points)) and int(max(abs(wh)))<=B and bool(zeros)
        if required is not None: expected &= required in zeros
        if meta['forced_points'] is not None: expected &= points==meta['forced_points']
        if meta['degree_eight_necessary_constraint']:
            xors=0
            for x in points: xors^=x
            expected &= bool(xors)
        assert actual==expected
    if model is not None:
        h=f.copy()
        for x in model_points: h[x]^=1
        wh=H@(1-2*h)
        zeros=np.flatnonzero(wh==0).tolist()
        assert zeros and int(max(abs(wh)))<=B
        shift=zeros[0]
        balanced=h^((1-H[shift])//2)
        wb=H@(1-2*balanced)
        assert sum(balanced)==256 and int(max(abs(wb)))<=B
        if witness:
            txt=''.join(map(str,balanced.tolist()))
            Path(witness).write_text(json.dumps({'bits':txt,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':int(sum(balanced)),'walsh':wb.tolist(),'nonlinearity':256-int(max(abs(wb)))//2,'source_seed':name,'flips':model_points,'linear_shift':shift,'scope':'relaxed-bound planted control only'},indent=2)+'\n')
    return {'status':'PASS','seed':name,'radius_exact':r,'bound':B,'cnf_sha256':meta['cnf_sha256'],'variables':n,'clauses':len(clauses),'universal_gate_truth_table_checks':len(gates),'character_parities_symbolically_checked':r*512,'order_truth_table_assignments_per_comparator':2**18,'lookup_rows_checked':r*512,'sampled_direct_walsh_assignments':len(cases),'sampling_scope':'supplemental controls only; universal encoding correspondence is checked by complete local-gate/subset/lookup/character/order audits','sat_model_checked':model is not None,'model_points':model_points}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('prefix')
    p.add_argument('--model-log')
    p.add_argument('--witness')
    p.add_argument('--output')
    p.add_argument('--samples',type=int,default=64)
    args=p.parse_args()
    result=audit(args.prefix,args.model_log,args.witness,args.samples)
    if args.output: Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__': main()
