#!/usr/bin/env python3
"""Check used d4 auxiliary, equality and objective maps by explicit indices.

The reference contractions use actual finite basis vectors, independently of
loop counting or the verifier's trace formulas. The pinned author core is
executed for the compared outputs; no certificate solve or construction code.
"""
import collections
import hashlib
import importlib.util
import io
import itertools
import json
import lzma
import sys
import tarfile
import time
import types
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
ARCHIVE=ROOT/'frontier-20261028-tomar-release-ep3-v3.tar.gz'
BASE=ROOT/'frontier-20261028-independent-d4-base-check.py'
OUT=ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check-results.json'
EXPECTED_ARCHIVE='2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
EXPECTED_CERT='0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
EXPECTED_CORE='0f0d84a9ce257edbf9b0b6cbbff2690041fbd6aad18d139c8845e8edf547d450'


def sha(raw): return hashlib.sha256(raw).hexdigest()


def load():
    raw=ARCHIVE.read_bytes()
    if sha(raw)!=EXPECTED_ARCHIVE: raise ValueError('archive hash mismatch')
    spec=importlib.util.spec_from_file_location('base_independent',BASE)
    base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        cert=tf.extractfile('release_ep3/certs/ep3_perd_d4.pkl.xz').read()
        source=tf.extractfile('release_ep3/ep3core.py').read()
    if sha(cert)!=EXPECTED_CERT or sha(source)!=EXPECTED_CORE: raise ValueError('member hash mismatch')
    pkg=base.DataOnlyUnpickler(io.BytesIO(lzma.decompress(cert,memlimit=256*1024*1024))).load()
    core=types.ModuleType('ep3core')
    core.__file__='archive:release_ep3/ep3core.py'
    exec(compile(source,core.__file__,'exec'),core.__dict__)
    rx=core.Relaxation(pkg['k'],pkg['types'],pkg['diagrams'],pkg['aux'],pkg['eq_groups'],{})
    return pkg,core,rx


def tuples(n,m): return list(itertools.product(range(n),repeat=m))


def permutation_entry(row,col,p):
    return int(all(row[p[i]]==col[i] for i in range(len(p))))


def reindexed_entry(row,col,p,kpos,lpos):
    def pick(x): return (row if x[0]=='i' else col)[x[1]]
    return permutation_entry(tuple(map(pick,kpos)),tuple(map(pick,lpos)),p)


def compressed(J, row_basis, col_basis, entry):
    """Direct J^T O J with exact integer basis summation."""
    r=len(J[0]); out=[[0]*r for _ in range(r)]
    for i,row in enumerate(row_basis):
        for j,col in enumerate(col_basis):
            v=entry(row,col)
            if v:
                for a in range(r):
                    if J[i][a]:
                        for b in range(r):
                            out[a][b]+=v*J[i][a]*J[j][b]
    return out


def three_site_J(pkg, label, n=4):
    f,l,r=label.split('_')
    key=(int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))
    keys,C=pkg['diagrams'][(3,())][key]
    basis=tuples(n,3); loc={v:i for i,v in enumerate(basis)}
    J=[[0]*len(C[0]) for _ in basis]
    for ki,(pairs,top,bottom) in enumerate(keys):
        for choices in itertools.product(range(n),repeat=len(pairs)):
            v=[None]*3
            for (x,y),u in zip(pairs,choices): v[x]=v[y]=u
            for x,u in top: v[x]=u
            for x,u in bottom: v[x]=n+u
            if any(x is None or not 0<=x<n for x in v): raise ValueError('invalid 3-site diagram')
            pos=loc[tuple(v)]
            for c,z in enumerate(C[ki]): J[pos][c]+=z
    return J,basis


def trace_perm_entry(row,col,p,slot,order,n):
    total=0
    for v in range(n):
        a=[None]*4; b=[None]*4
        a[slot]=b[slot]=v
        for i,s in enumerate(order): a[s]=row[i]; b[s]=col[i]
        total+=permutation_entry(a,b,p)
    return total


def stiefel_entry(row,col,p,slot):
    order=tuple(i for i in range(4) if i!=slot)
    tr=trace_perm_entry(tuple(row[i] for i in order),tuple(col[i] for i in order),p,slot,order,2)
    return 2*permutation_entry(row,col,p)-int(row[slot]==col[slot])*tr


def swap_trace_counts(n,p):
    plain=swapped=0
    for x in tuples(n,4):
        target=[None]*4
        for i in range(4): target[p[i]]=x[i]
        plain+=int(tuple(target)==x)
        target[0],target[3]=target[3],target[0]
        swapped+=int(tuple(target)==x)
    return plain,swapped


def main():
    start=time.monotonic(); pkg,core,rx=load()
    perms=list(itertools.permutations(range(4))); b2=tuples(2,4)
    errors=[]; aux_comps=0; eq_comps=0
    used={(a,b,t['modules'][3]) for t in pkg['types'] for a in t['rows'] for b in t['rows']}
    for a,b,mod in sorted(used):
        _,kp,lp=core.entry_rule(core.parse_pattern(a),core.parse_pattern(b))
        calc=rx.local_rows(mod,'a',4,kp,lp,False)
        J=pkg['aux'][mod]; dim=len(J[0])
        for pi,p in enumerate(perms):
            actual=compressed(J,b2,b2,lambda row,col: reindexed_entry(row,col,p,kp,lp))
            got=[int(x) for x in calc[pi]]
            if [x for row in actual for x in row]!=got:
                errors.append({'kind':'aux','rows':[a,b],'module':mod,'permutation':list(p)})
            aux_comps+=1
    eq_specs={}
    for name,group in pkg['eq_groups'].items():
        for part in group['parts']:
            for spec in part['local']:
                side,slot,order,kind,mkeys=spec
                key=(side,slot,tuple(order),kind,tuple(mkeys))
                eq_specs[key]=spec
    for key,spec in sorted(eq_specs.items(),key=str):
        side,slot,order,kind,mkeys=key
        got=rx.eq_local(4,spec,False)
        cursor=0
        for mk in mkeys:
            if side=='S':
                J,basis=three_site_J(pkg,mk.split('|')[-1],4)
                entry=lambda row,col,p:trace_perm_entry(row,col,p,slot,order,4)
            else:
                J=pkg['aux'][mk]
                m=4 if kind=='stiefel_aux' else 3
                basis=tuples(2,m)
                if len(J)!=len(basis): raise ValueError('auxiliary equality compression shape')
                entry=(lambda row,col,p:stiefel_entry(row,col,p,slot)) if kind=='stiefel_aux' else (lambda row,col,p:trace_perm_entry(row,col,p,slot,order,2))
            dim=len(J[0]); nentries=dim*dim
            for pi,p in enumerate(perms):
                actual=compressed(J,basis,basis,lambda row,col:entry(row,col,p))
                ref=[x for row in actual for x in row]
                calc=[int(x) for x in got[cursor:cursor+nentries,pi]]
                if ref!=calc: errors.append({'kind':'equality','spec':str(key),'module':mk,'permutation':list(p)})
                eq_comps+=1
            cursor+=nentries
        if cursor!=got.shape[0]: raise ValueError('equality column length mismatch')
    site=[swap_trace_counts(4,p) for p in perms]
    aux=[swap_trace_counts(2,p) for p in perms]
    target,den=core.objective_tensor(4,3)
    expected_den=8*(2*4**3)**4
    if den!=expected_den: errors.append({'kind':'objective_denominator','got':int(den),'want':expected_den})
    objective_comps=0
    for ix in itertools.product(range(24),repeat=4):
        direct=1
        for j in ix[:3]: direct*=2*site[j][0]-site[j][1]
        direct*=aux[ix[3]][1]
        if int(target[ix])!=direct:
            errors.append({'kind':'objective_word','index':list(ix)})
            if len(errors)>20: raise RuntimeError('too many errors')
        objective_comps+=1
    result={'kind':'independent_literal_aux_equality_objective_map_check','dimension':4,'copies':3,
            'archive_sha256':EXPECTED_ARCHIVE,'certificate_sha256':EXPECTED_CERT,'author_core_sha256':EXPECTED_CORE,
            'actual_used_aux_row_module_combinations':len(used),'aux_compressed_permutation_comparisons':aux_comps,
            'distinct_equality_slot_order_compression_specs':len(eq_specs),'equality_compressed_permutation_comparisons':eq_comps,
            'objective_word_comparisons':objective_comps,'objective_denominator':expected_den,
            'failure_count':len(errors),'failures':errors,'elapsed_seconds':round(time.monotonic()-start,3),
            'scope':'Actual d4 auxiliary Gram compression maps, canonical equality compression maps and every 24^4 objective word. Independent literal index contractions versus pinned author core; NOT final corrected orbit identity or independent theorem verification.',
            'verdict':'PASS' if not errors else 'FAIL'}
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True)); return 0 if not errors else 1


if __name__=='__main__': raise SystemExit(main())
