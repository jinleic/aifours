#!/usr/bin/env python3
"""Small, solver-free, independent integer check of ONE 1008-row identity.
This is not a replay of the 1,811,001-row affine-plane archive. The checker
imports no exporter, model, old checker or scientific package. It reconstructs
ordinary CMI/CE vectors and the universal target on 2047 entropy coordinates.
"""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json,sys
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
LOCAL={6:(5,7,8,9),7:(2,6,8,10)}
V=1023;U=1024;FULL=2047

def mask(vs):return sum(1<<(v-1) for v in vs)
def row(name):
    if name[0]=='cmi':
        if len(name)!=4:raise ValueError('CMI_ARITY')
        _,i,j,K=name
        if any(type(v) is not int for v in (i,j,K)) or not 0<=i<j<11 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('CMI_PREMISE')
        terms=((K|1<<i,1),(K|1<<j,1),(K|1<<i|1<<j,-1),(K,-1))
    elif name[0]=='ce':
        if len(name)!=3:raise ValueError('CE_ARITY')
        _,i,K=name
        if type(i) is not int or type(K) is not int or not 0<=i<11 or not 0<=K<=FULL or K>>i&1:raise ValueError('CE_PREMISE')
        terms=((K|1<<i,1),(K,-1))
    else:raise ValueError('ONLY_ORDINARY_SHANNON_ROWS')
    out={}
    for m,c in terms:
        if m:out[m]=out.get(m,0)+c
    return [[m,c] for m,c in sorted(out.items()) if c]

def target(joint_coefficient=18):
    # RHS - 18 Delta. Every displayed FD is retained as an entropy defect,
    # not assumed to vanish in this unconditional eleven-variable inequality.
    out=[0]*2048
    out[V]-=joint_coefficient
    for i in range(10):out[1<<i]+=12
    for v in range(1,11):
        a=mask(N[v]);w=5 if v in (6,7) else 6
        out[a|1<<(v-1)]+=w;out[a]-=w
    for v in (6,7):
        a=mask(LOCAL[v])|U
        out[a|1<<(v-1)]+=1;out[a]-=1
    for v in (9,10):
        a=mask(N[v]);out[a|U]+=1;out[a]-=1
    return out

def verify(c,joint_coefficient=18):
    if c['N']!={str(v):list(N[v]) for v in N}:raise ValueError('GRAPH_BINDING')
    if c['local_sets']!={str(v):list(LOCAL[v]) for v in LOCAL}:raise ValueError('EXPLICIT_LOCAL_SETS')
    scale=c['scale']
    if type(scale) is not int or scale<=0:raise ValueError('SCALE')
    rows=c['rows']
    if not 1<=len(rows)<=2048:raise ValueError('SMALL_REPLAY_BOUND')
    acc=[0]*2048;seen=set();kinds=Counter()
    for item in rows:
        name=item['row'];key=tuple(name);q=item['multiplier']
        if type(q) is not int or q<=0:raise ValueError('POSITIVE_INTEGER_SHANNON_MULTIPLIER')
        if key in seen:raise ValueError('DUPLICATE_SHANNON_ROW')
        seen.add(key);ts=row(name);kinds[name[0]]+=1
        if ts!=item['literal_vector']:raise ValueError('LITERAL_VECTOR_NOT_SEMANTIC_ROW')
        for m,w in ts:acc[m]+=q*w
    expected=target(joint_coefficient)
    if acc!=[scale*w for w in expected]:raise ValueError('FULL_INTEGER_COEFFICIENT_IDENTITY')
    return {'ordinary_Shannon_rows':len(rows),'row_kinds':dict(kinds),'scale':scale,'raw_nonempty_coordinates':2047,'zero_coefficient_residual':True}

def controls(c):
    results={}
    def reject(name,x,changed_target=False):
        try:verify(x,19 if changed_target else 18)
        except ValueError as e:results[name]=str(e)
        else:raise ValueError(('CONTROL_NOT_REJECTED',name))
    reject('changed_target',c,True)
    x=deepcopy(c);x['rows'][0]['multiplier']*=-1;reject('flipped_multiplier',x)
    x=deepcopy(c);x['rows'][0]['literal_vector'][0][1]+=1;reject('altered_literal_vector',x)
    x=deepcopy(c);x['N']['3'].remove(4);reject('deleted_graph_edge',x)
    x=deepcopy(c);x['rows']=x['rows'][:-1];reject('dropped_row',x)
    return results

def main():
    root=Path(__file__).resolve().parent;raw=(root/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERTIFICATE_HASH')
    c=json.loads(raw);r={'certificate_sha256':sys.argv[3],'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),**verify(c),'negative_controls':controls(c),'scope':'Bounded exact integer arithmetic on one new 1008-row original-author universal Shannon identity. No old bulk-archive replay, graph-FD assumption in the raw identity, binary-state assumption, scientific-referee acceptance, novelty or unrestricted guessing-number claim.'}
    with (root/sys.argv[1]).open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps(r,indent=2))
if __name__=='__main__':main()
