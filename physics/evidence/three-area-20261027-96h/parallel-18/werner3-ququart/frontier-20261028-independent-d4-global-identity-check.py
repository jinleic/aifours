#!/usr/bin/env python3
"""Independent exact global orbit identity for the corrected d4 certificate.

Uses only public certificate data, saved exact corrections, independently
constructed literal local maps, and independently generated source orbits.
It DOES NOT import/execute the author's ep3core/verify_perd. Integer tensor
contractions use FLINT; all 4675 residual numerators share one exact common
denominator, so zero counts establish rational identity (subject to software).
"""
import collections
import hashlib
import importlib.util
import io
import itertools
import json
import lzma
import math
import sys
import tarfile
import time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-python-deps'))
import flint
ARCHIVE=ROOT/'frontier-20261028-tomar-release-ep3-v3.tar.gz'
CORRECTED=ROOT/'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
OUT=ROOT/'frontier-20261028-independent-d4-global-identity-check-results.json'
EXPECTED_ARCHIVE='2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
EXPECTED_CERT='0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
EXPECTED_CORRECTED='c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
PERMS=list(itertools.permutations(range(4)))
LETTERS={'31':'aaab','22':'aabb','13':'bbba'}


def digest(b): return hashlib.sha256(b).hexdigest()


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def load_data():
    raw=ARCHIVE.read_bytes()
    if digest(raw)!=EXPECTED_ARCHIVE: raise ValueError('archive hash mismatch')
    base=module('base_independent',ROOT/'frontier-20261028-independent-d4-base-check.py')
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:gz') as tf:
        cert=tf.extractfile('release_ep3/certs/ep3_perd_d4.pkl.xz').read()
    if digest(cert)!=EXPECTED_CERT: raise ValueError('certificate hash mismatch')
    pkg=base.DataOnlyUnpickler(io.BytesIO(lzma.decompress(cert,memlimit=256*1024*1024))).load()
    errors,_,_=base.structural_checks(pkg)
    if errors: raise ValueError('package structures invalid: '+str(errors[:5]))
    cb=CORRECTED.read_bytes()
    if digest(cb)!=EXPECTED_CORRECTED: raise ValueError('corrected data hash mismatch')
    corrected=json.loads(lzma.decompress(cb,memlimit=256*1024*1024))
    if corrected['source_member_sha256']!=EXPECTED_CERT or corrected['dimension']!=4 or corrected['copies']!=3:
        raise ValueError('corrected data source mismatch')
    return pkg,corrected


def literal_rule(row1,row2):
    a,b=row1.split(),row2.split(); unc=[];conj=[]
    if len(a)!=4 or len(b)!=4: raise ValueError('invalid row length')
    for j,(x,y) in enumerate(zip(a,b)):
        if x not in ('a','b','a*','b*') or y not in ('a','b','a*','b*') or x.endswith('*')!=y.endswith('*'):
            raise ValueError('invalid row tokens')
        if x.endswith('*'):
            unc.append((y[0],('j',j)));conj.append((x[0],('i',j)))
        else:
            unc.append((x[0],('i',j)));conj.append((y[0],('j',j)))
    matching=[f for f,letters in LETTERS.items() if collections.Counter(letters)==collections.Counter(v[0] for v in unc)]
    if len(matching)!=1 or collections.Counter(v[0] for v in unc)!=collections.Counter(v[0] for v in conj):
        raise ValueError('unbalanced row family')
    fam=matching[0]
    def positions(pool):
        pool=list(pool); result=[]
        for letter in LETTERS[fam]:
            idx=next((i for i,v in enumerate(pool) if v[0]==letter),None)
            if idx is None: raise ValueError('unmatched vector factor')
            result.append(pool.pop(idx)[1])
        return tuple(result)
    return fam,positions(unc),positions(conj)


def perm_entry(row,col,p,kpos,lpos):
    def pick(q):return (row if q[0]=='i' else col)[q[1]]
    ket=tuple(map(pick,kpos));bra=tuple(map(pick,lpos))
    return int(all(ket[p[j]]==bra[j] for j in range(4)))


def parse_site(mod,pkg):
    side,cut,lab=mod.split('|'); cut=tuple(map(int,cut.split(','))) if cut else ()
    f,l,r=lab.split('_')
    label=(int(f[1:]),() if l=='e' else tuple(map(int,l)),() if r=='e' else tuple(map(int,r)))
    if side!='S': raise ValueError('not a site module')
    return pkg['diagrams'][(4,cut)][label]


def explicit_vector(key,n):
    pairs,top,bottom=key; out=collections.Counter()
    for vals in itertools.product(range(n),repeat=len(pairs)):
        q=[None]*4
        for (a,b),v in zip(pairs,vals):q[a]=q[b]=v
        for a,v in top:q[a]=v
        for a,v in bottom:q[a]=n+v
        if any(v is None or not 0<=v<n for v in q):raise ValueError('invalid diagram key')
        out[tuple(q)]+=1
    return out


def make_site_map(mod,kpos,lpos,pkg):
    keys,C=parse_site(mod,pkg)
    vec=[explicit_vector(k,4) for k in keys]
    C=np.asarray(C,dtype=object);out=[]
    for p in PERMS:
        raw=np.array([[sum(wa*wb*perm_entry(a,b,p,kpos,lpos)
                           for a,wa in va.items() for b,wb in vb.items())
                       for vb in vec] for va in vec],dtype=object)
        out.append((C.T@raw@C).ravel())
    return np.array(out,dtype=object)


def make_aux_map(mod,kpos,lpos,pkg):
    J=np.asarray(pkg['aux'][mod],dtype=object)
    basis=list(itertools.product(range(2),repeat=4));out=[]
    for p in PERMS:
        raw=np.array([[perm_entry(a,b,p,kpos,lpos) for b in basis] for a in basis],dtype=object)
        out.append((J.T@raw@J).ravel())
    return np.array(out,dtype=object)


def eq_reference(spec,pkg,aux):
    side,slot,order,kind,mkeys=spec;blocks=[]
    order=tuple(order)
    for mk in mkeys:
        if side=='S':
            J,basis=aux.three_site_J(pkg,mk.split('|')[-1],4)
            entry=lambda row,col,p:aux.trace_perm_entry(row,col,p,slot,order,4)
        else:
            J=pkg['aux'][mk]; m=4 if kind=='stiefel_aux' else 3
            basis=list(itertools.product(range(2),repeat=m))
            entry=(lambda row,col,p:aux.stiefel_entry(row,col,p,slot)) if kind=='stiefel_aux' else (lambda row,col,p:aux.trace_perm_entry(row,col,p,slot,order,2))
        cols=[]
        for p in PERMS:
            mat=aux.compressed(J,basis,basis,lambda row,col:entry(row,col,p))
            cols.append([x for row in mat for x in row])
        blocks.append(np.asarray(cols,dtype=object).T)
    return np.vstack(blocks)


def generate_orbits(letters):
    """Independent union-find under two-sided stabilizer, sites and inverse."""
    ix={p:i for i,p in enumerate(PERMS)}
    def compose(a,b):return tuple(a[b[i]] for i in range(4))
    def inv(a):
        out=[0]*4
        for i,j in enumerate(a):out[j]=i
        return tuple(out)
    inverse=[ix[inv(p)] for p in PERMS]
    trans=[]
    for ch in ('a','b'):
        slots=[i for i,x in enumerate(letters) if x==ch]
        for i,j in zip(slots,slots[1:]):
            q=list(range(4));q[i],q[j]=q[j],q[i];trans.append(tuple(q))
    maps=[]
    for g in trans:
        maps.append([ix[compose(g,p)] for p in PERMS]);maps.append([ix[compose(p,g)] for p in PERMS])
    n=24**4;parent=list(range(n));rank=bytearray(n)
    def find(a):
        while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
        return a
    def join(a,b):
        a,b=find(a),find(b)
        if a==b:return
        if rank[a]<rank[b]:a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:rank[a]+=1
    for x in range(n):
        q=x;d3=q%24;q//=24;d2=q%24;q//=24;d1=q%24;d0=q//24
        for m in maps:join(x,((m[d0]*24+m[d1])*24+m[d2])*24+m[d3])
        join(x,((d1*24+d0)*24+d2)*24+d3)
        join(x,((d0*24+d2)*24+d1)*24+d3)
        join(x,((inverse[d0]*24+inverse[d1])*24+inverse[d2])*24+inverse[d3])
    roots=[find(i) for i in range(n)]
    mapping={r:j for j,r in enumerate(sorted(set(roots)))}
    return np.array([mapping[r] for r in roots],dtype=np.int64),len(mapping)


def fz(A):
    a=np.asarray(A,dtype=object)
    return flint.fmpz_mat(a.shape[0],a.shape[1],[int(x) for x in a.ravel()])


def mode_product(T,A,axis):
    moved=np.moveaxis(T,axis,0);shape=moved.shape
    prod=fz(A)*fz(moved.reshape(shape[0],-1))
    out=np.asarray([int(x) for x in prod.entries()],dtype=object).reshape((A.shape[0],)+shape[1:])
    return np.moveaxis(out,0,axis)


def add_orbits(acc,oid,arr,sign):
    for label,value in zip(oid,arr.ravel()):
        if value:acc[int(label)]+=sign*int(value)


def main():
    start=time.monotonic();sys.set_int_max_str_digits(0)
    pkg,corr=load_data();aux=module('aux_reference',ROOT/'frontier-20261028-independent-d4-aux-equality-objective-check.py')
    matrices=corr['matrices']; lam=corr['equality_coefficients']
    if len(matrices)!=len(pkg['types']):raise ValueError('corrected type count mismatch')
    denominator=8*(2*4**3)**4
    for mat in matrices:
        for num,den in mat['values']:denominator=math.lcm(denominator,int(den))
    for item in lam:denominator=math.lcm(denominator,int(item['denominator']))
    print('common denominator bits',denominator.bit_length(),flush=True)
    Z=[]
    for t,m in zip(pkg['types'],matrices):
        r=t['r']
        if m['r']!=r or len(m['values'])!=r*r:raise ValueError('corrected matrix shape mismatch')
        vals=[int(num)*(denominator//int(den)) for num,den in m['values']]
        Z.append(flint.fmpz_mat(r,r,vals))
    orbits={f:generate_orbits(letters) for f,letters in LETTERS.items()}
    acc={f:[0]*orbits[f][1] for f in LETTERS}
    groups={}
    for ti,t in enumerate(pkg['types']):
        for r,a in enumerate(t['rows']):
            for s,b in enumerate(t['rows']):
                fam,kp,lp=literal_rule(a,b)
                cut=t['modules'][0].split('|')[1]
                groups.setdefault((fam,kp,lp,cut),[]).append((ti,r,s))
    sitecache={};auxcache={}
    for number,(g,items) in enumerate(sorted(groups.items(),key=lambda x:str(x[0])),1):
        fam,kp,lp,_=g
        smods=sorted({m for ti,_,_ in items for m in pkg['types'][ti]['modules'][:3]})
        amods=sorted({pkg['types'][ti]['modules'][3] for ti,_,_ in items})
        def getsite(m):
            key=(m,kp,lp)
            if key not in sitecache:sitecache[key]=make_site_map(m,kp,lp,pkg)
            return sitecache[key]
        def getaux(m):
            key=(m,kp,lp)
            if key not in auxcache:auxcache[key]=make_aux_map(m,kp,lp,pkg)
            return auxcache[key]
        offsets={};off=0
        for m in smods:offsets[m]=off;off+=getsite(m).shape[1]
        Ds=off; off=0
        for m in amods:offsets[m]=off;off+=getaux(m).shape[1]
        Da=off
        As=np.hstack([getsite(m) for m in smods]); Aa=np.hstack([getaux(m) for m in amods])
        block=np.zeros((Ds,Ds,Ds,Da),dtype=object)
        subgroups={}
        for ti,r,s in items:subgroups.setdefault(tuple(pkg['types'][ti]['modules']),[]).append((ti,r,s))
        for mods,triples in subgroups.items():
            dims=[math.isqrt((getaux(m) if i==3 else getsite(m)).shape[1]) for i,m in enumerate(mods)]
            if any(d*d!=(getaux(m) if i==3 else getsite(m)).shape[1] for i,(d,m) in enumerate(zip(dims,mods))):
                raise ValueError('local map is not square')
            n=math.prod(dims); total=flint.fmpz_mat(n,n)
            for ti,r,s in triples:
                W=pkg['types'][ti]['W'];rZ=pkg['types'][ti]['r']
                Wr=flint.fmpz_mat(n,rZ,[int(x) for row in W[r*n:(r+1)*n] for x in row])
                Ws=flint.fmpz_mat(n,rZ,[int(x) for row in W[s*n:(s+1)*n] for x in row])
                total+=Wr*Z[ti]*Ws.transpose()
            T=np.asarray([int(x) for x in total.entries()],dtype=object).reshape(dims+dims)
            T=T.transpose((0,4,1,5,2,6,3,7)).reshape([d*d for d in dims])
            sl=tuple(slice(offsets[m],offsets[m]+d*d) for m,d in zip(mods,dims))
            block[sl]+=T
        for axis in range(4):block=mode_product(block,Aa if axis==3 else As,axis)
        add_orbits(acc[fam],orbits[fam][0],block,-1)
        print('independent block group',number,'of',len(groups),'elapsed',round(time.monotonic()-start,1),flush=True)
    # Objective direct literal fixed-point counts; no author core imported.
    site=[aux.swap_trace_counts(4,p) for p in PERMS]; a2=[aux.swap_trace_counts(2,p) for p in PERMS]
    vs=np.array([2*x-y for x,y in site],dtype=object);vq=np.array([y for _,y in a2],dtype=object)
    obj=np.multiply.outer(np.multiply.outer(np.multiply.outer(vs,vs),vs),vq)
    obj*=denominator//(8*(2*4**3)**4)
    add_orbits(acc['31'],orbits['31'][0],obj,1)
    # All actual equality entries from separately implemented literal partial traces.
    bygroup=collections.defaultdict(list)
    for item in lam:bygroup[item['group']].append(item)
    eqcache={}
    for name,g in pkg['eq_groups'].items():
        for part in g['parts']:
            Es=[]
            for spec in part['local']:
                key=(spec[0],spec[1],tuple(spec[2]),spec[3],tuple(spec[4]))
                if key not in eqcache:eqcache[key]=eq_reference(spec,pkg,aux)
                Es.append(eqcache[key])
            T=np.zeros(tuple(e.shape[0] for e in Es),dtype=object)
            for item in bygroup[name]:
                T[tuple(item['index'])]+=int(item['numerator'])*(denominator//int(item['denominator']))
            for axis,e in enumerate(Es):T=mode_product(T,e.T,axis)
            add_orbits(acc[part['family']],orbits[part['family']][0],T,-int(part['sign']))
    bad={f:[i for i,v in enumerate(vals) if v!=0] for f,vals in acc.items()}
    counts={f:len(v) for f,v in bad.items()}; ok=all(not v for v in bad.values())
    result={'kind':'independent_exact_full_d4_certificate_orbit_identity',
            'archive_sha256':EXPECTED_ARCHIVE,'source_certificate_sha256':EXPECTED_CERT,
            'corrected_data_sha256':EXPECTED_CORRECTED,'d':4,'copies':3,
            'common_denominator_bits':denominator.bit_length(),
            'corrected_multiplier_count':len(matrices),'corrected_equality_count':len(lam),
            'independent_row_pattern_groups':len(groups),
            'independent_orbit_counts':{f:orbits[f][1] for f in LETTERS},
            'all_orbit_count':sum(orbits[f][1] for f in LETTERS),
            'nonzero_residual_counts':counts,'first_nonzero_orbit_indices':{f:v[:10] for f,v in bad.items()},
            'flint_version':flint.__version__,'numpy_version':np.__version__,
            'elapsed_seconds':round(time.monotonic()-start,3),
            'method':'Exact common-denominator integer arithmetic; independently rebuilt literal site/aux/equality/objective maps and union-find orbits; independent grouped tensor contraction; no author ep3core or verifier imported.',
            'scope':'Full exact corrected certificate identity on every orbit sum at d=4. Validity of physical moment relaxation, final PSD, and mathematical theorem require their separate evidence and review.',
            'verdict':'PASS' if ok else 'FAIL'}
    OUT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True,indent=2),flush=True)
    return 0 if ok else 1


if __name__=='__main__':raise SystemExit(main())
