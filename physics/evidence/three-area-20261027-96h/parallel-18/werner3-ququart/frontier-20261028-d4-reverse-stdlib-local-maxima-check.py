#!/usr/bin/env python3
"""Stdlib-only reconstruction of all reverse-source local-map maxima.

Unpickles only built-in data; directly enumerates actual 4-rep site/qubit and
3-rep equality basis entries under reverse physical row matching. No numpy,
FLINT, author source, owner local-map code or target physical state is used.
"""
import collections
import hashlib
import io
import itertools
import json
import lzma
import pickle
import tarfile
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ARCH=ROOT/'frontier-20261028-tomar-release-ep3-v3.tar.gz'
RESULT=ROOT/'frontier-20261028-d4-reverse-independent-crt-check-results.json'
PIN_ARCH='2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
PIN_RESULT='3afc85cf5f47645314fa4ec369247f357c6e415a834707e273425253eea0ca19'
MEMBER='release_ep3/certs/ep3_perd_d4.pkl.xz'
PIN_MEMBER='0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
OUT=ROOT/'frontier-20261028-d4-reverse-stdlib-local-maxima-check-results.json'
PERMS=list(itertools.permutations(range(4)));LETTERS={'31':'aaab','22':'aabb','13':'bbba'}

class SafeData(pickle.Unpickler):
    def find_class(self,module,name):raise pickle.UnpicklingError('globals forbidden')

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def reverse_rule(a,b):
    row=a.split();col=b.split();u=[];v=[]
    if len(row)!=4 or len(col)!=4:raise ValueError('bad row')
    for j,(x,y) in enumerate(zip(row,col)):
        if x not in ('a','b','a*','b*') or y not in ('a','b','a*','b*') or x.endswith('*')!=y.endswith('*'):raise ValueError('bad physical factors')
        if x.endswith('*'):u.append((y[0],('j',j)));v.append((x[0],('i',j)))
        else:u.append((x[0],('i',j)));v.append((y[0],('j',j)))
    families=[f for f,L in LETTERS.items() if collections.Counter(a for a,_ in u)==collections.Counter(L)]
    if len(families)!=1 or collections.Counter(a for a,_ in u)!=collections.Counter(a for a,_ in v):raise ValueError('bad family')
    f=families[0]
    def pick(pool):
        pool=list(pool);out=[]
        for c in LETTERS[f]:
            for i in range(len(pool)-1,-1,-1):
                if pool[i][0]==c:out.append(pool.pop(i)[1]);break
            else:raise ValueError('no matching factor')
        return tuple(out)
    return f,pick(u),pick(v)

def vec(key,n,m):
    pairs,top,bottom=key;out=collections.Counter()
    for vals in itertools.product(range(n),repeat=len(pairs)):
        a=[None]*m
        for (i,j),v in zip(pairs,vals):
            if i==j or a[i] is not None or a[j] is not None:raise ValueError('overlapping pair')
            a[i]=a[j]=v
        for i,v in top:
            if a[i] is not None:raise ValueError('overlapping top')
            a[i]=v
        for i,v in bottom:
            if a[i] is not None:raise ValueError('overlapping bottom')
            a[i]=n+v
        if any(v is None or not 0<=v<n for v in a):raise ValueError('bad diagram basis')
        out[tuple(a)]+=1
    return out

def gram_entry(row,col,p,kp,lp):
    def pick(k):return (row if k[0]=='i' else col)[k[1]]
    ket=tuple(map(pick,kp));bra=tuple(map(pick,lp))
    return int(all(ket[p[j]]==bra[j] for j in range(4)))

def perm_entry(row,col,p):return int(all(row[p[j]]==col[j] for j in range(4)))

def trace_entry(row,col,p,slot,order,n):
    if slot not in range(4) or sorted(order)!=[i for i in range(4) if i!=slot]:raise ValueError('bad trace ordering')
    out=0
    for z in range(n):
        r=[None]*4;c=[None]*4;r[slot]=c[slot]=z
        for j,s in enumerate(order):r[s]=row[j];c[s]=col[j]
        out+=perm_entry(r,c,p)
    return out

def aux_eq_entry(row,col,p,slot,order,kind):
    if kind=='del':return trace_entry(row,col,p,slot,order,2)
    if kind!='stiefel_aux':raise ValueError('bad aux kind')
    rr=[row[i] for i in order];cc=[col[i] for i in order]
    return 2*perm_entry(row,col,p)-int(row[slot]==col[slot])*trace_entry(rr,cc,p,slot,order,2)

def compress(raw,C):
    n=len(raw)
    if not C or len(C)!=n or not C[0] or any(len(row)!=len(C[0]) for row in C):raise ValueError('bad compression')
    r=len(C[0])
    return [sum(C[i][a]*raw[i][j]*C[j][b] for i in range(n) for j in range(n))
            for a in range(r) for b in range(r)]

def label(x):
    f,l,r=x.split('|')[-1].split('_')
    return (int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))

def site_values(pkg,mod,kp,lp):
    side,cut,_=mod.split('|')
    if side!='S':raise ValueError('bad site module')
    cut=tuple(map(int,cut.split(','))) if cut else ()
    keys,C=pkg['diagrams'][(4,cut)][label(mod)];vectors=[vec(k,4,4) for k in keys]
    for p in PERMS:
        raw=[[sum(wa*wb*gram_entry(a,b,p,kp,lp) for a,wa in va.items() for b,wb in vb.items())
              for vb in vectors] for va in vectors]
        yield from compress(raw,C)

def aux_values(pkg,mod,kp,lp):
    J=pkg['aux'][mod];basis=list(itertools.product(range(2),repeat=4))
    if len(J)!=len(basis):raise ValueError('bad aux shape')
    for p in PERMS:
        raw=[[gram_entry(a,b,p,kp,lp) for b in basis] for a in basis]
        yield from compress(raw,J)

def equality_values(pkg,spec,mk):
    side,slot,order,kind,_=spec;order=tuple(order)
    if side=='S':
        keys,C=pkg['diagrams'][(3,())][label(mk)];vectors=[vec(k,4,3) for k in keys]
        for p in PERMS:
            raw=[[sum(wa*wb*trace_entry(a,b,p,slot,order,4) for a,wa in va.items() for b,wb in vb.items())
                  for vb in vectors] for va in vectors]
            yield from compress(raw,C)
    elif side=='A':
        J=pkg['aux'][mk];m=4 if kind=='stiefel_aux' else 3
        basis=list(itertools.product(range(2),repeat=m))
        if len(J)!=len(basis):raise ValueError('bad equality aux shape')
        for p in PERMS:
            raw=[[aux_eq_entry(a,b,p,slot,order,kind) for b in basis] for a in basis]
            yield from compress(raw,J)
    else:raise ValueError('bad equality side')

def main():
    st=time.monotonic()
    if sha(ARCH)!=PIN_ARCH or sha(RESULT)!=PIN_RESULT:raise ValueError('pin mismatch')
    with tarfile.open(ARCH,mode='r:gz') as tf:raw=tf.extractfile(MEMBER).read()
    if hashlib.sha256(raw).hexdigest()!=PIN_MEMBER:raise ValueError('source member mismatch')
    pkg=SafeData(io.BytesIO(lzma.decompress(raw,memlimit=256*1024*1024))).load();rec=json.loads(RESULT.read_text())
    if (pkg['d'],pkg['k'])!=(4,3):raise ValueError('wrong source')
    sites={};auxs={};pairs=0
    for t in pkg['types']:
        for a in t['rows']:
            for b in t['rows']:
                _,kp,lp=reverse_rule(a,b);pairs+=1
                for m in t['modules'][:3]:sites[(m,kp,lp)]=(m,kp,lp)
                m=t['modules'][3];auxs[(m,kp,lp)]=(m,kp,lp)
    specs={}
    for group in pkg['eq_groups'].values():
        for part in group['parts']:
            for s in part['local']:
                key=(s[0],s[1],tuple(s[2]),s[3],tuple(s[4]));specs[key]=s
    smax=amax=emax=0;scount=acount=ecount=0
    for mod,kp,lp in sites.values():
        for v in site_values(pkg,mod,kp,lp):smax=max(smax,abs(v));scount+=1
    for mod,kp,lp in auxs.values():
        for v in aux_values(pkg,mod,kp,lp):amax=max(amax,abs(v));acount+=1
    for s in specs.values():
        for mk in s[4]:
            for v in equality_values(pkg,s,mk):emax=max(emax,abs(v));ecount+=1
    if sha(ARCH)!=PIN_ARCH or sha(RESULT)!=PIN_RESULT:raise ValueError('input changed during run')
    expected_A=rec['max_local_map'];expected_E=rec['max_equality_map']
    ok=pairs==1570 and len(sites)==60 and len(auxs)==36 and len(specs)==10 and max(smax,amax)==expected_A and emax==expected_E
    result={'kind':'stdlib_all_reverse_source_literal_local_maxima','archive_sha256':PIN_ARCH,
            'source_member_sha256':PIN_MEMBER,'reverse_receipt_sha256':PIN_RESULT,
            'row_pair_occurrences':pairs,'site_specs':len(sites),'aux_specs':len(auxs),'equality_specs':len(specs),
            'site_entries_scanned':scount,'aux_entries_scanned':acount,'equality_entries_scanned':ecount,
            'site_max_abs':smax,'aux_max_abs':amax,'gram_max_abs':max(smax,amax),'equality_max_abs':emax,
            'matches_reverse_receipt_gram':max(smax,amax)==expected_A,'matches_reverse_receipt_equality':emax==expected_E,
            'elapsed_seconds':round(time.monotonic()-st,3),
            'method':'Restricted builtin-only pickle parsing; independent literal finite basis/trace/permutation and integer compression; scan every actual reverse-matched site, auxiliary and equality local entry.',
            'scope':'Exact local maxima Amax/Emax only; does not recompute source orbit residuals, full integer B, physical theorem or PSD; no numpy/FLINT/author source, formal kernel or independent model-family review.',
            'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2));return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
