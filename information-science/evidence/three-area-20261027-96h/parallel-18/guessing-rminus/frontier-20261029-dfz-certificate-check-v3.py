#!/usr/bin/env python3
"""Independent exact checker for R-minus upper-bound certificates with DFZ rows.

Usage: python3 script.py OUT.json CERT.json CERT_SHA VERIFY.json VERIFY_SHA [VERIFY2.json VERIFY2_SHA ...]
Rebuilds every certificate row from its semantic description with Fractions:
elemental Shannon rows on the stated variable set, R-minus graph FD rows, caps
h(v)<=1, the publisher's three copy branches (transcribed independently below:
b'0 copies b over a,d,e,f,g,h,i,j; (d'1,e'1) copies (d,e) over a,b,c,f,g,h,i,
then g'2 copies g over a,b,c,d,e'1,f,h,i; (f'3,g'3) copies (f,g) over
a,b,c,d,e,h,i,j, then h'4 copies h over a,b,c,d,e,f,f'3,i,j), and conditional
union instances of DFZ inequalities whose coefficient tuple must appear as
exactly re-derived in a supplied verification receipt. Checks signs and the
coefficient identity sum(w*row)=h(V); the bound is the sum of cap multipliers.
Version 3 also accepts DFZ instances on a branch variable set (row kind dfzb,
branch-local masks), valid because DFZ inequalities hold for any random
variables including copies. Version 2 accepted automorphism symmetrization rows h(S)=h(g(S)) for the two
graph automorphism generators (re-verified here as automorphisms).
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
NB={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
L=list('abcdefghij')
BR={'base':L,'b1':L+["b'0"],'b2':L+["d'1","e'1","g'2"],'b3':L+["f'3","g'3","h'4"]}
COPIES={("b'0",):('b1',["b'0"],['b'],list('adefghij'),L),
        ("d'1","e'1"):('b2',["d'1","e'1"],['d','e'],list('abcfghi'),L),
        ("g'2",):('b2',["g'2"],['g'],['a','b','c','d',"e'1",'f','h','i'],L+["d'1","e'1"]),
        ("f'3","g'3"):('b3',["f'3","g'3"],['f','g'],list('abcdehij'),L),
        ("h'4",):('b3',["h'4"],['h'],['a','b','c','d','e','f',"f'3",'i','j'],L+["f'3","g'3"])}

GENS=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
_E={frozenset((u-1,v-1)) for u,ns in NB.items() for v in ns}
if len(_E)!=26 or any({frozenset(g[i] for i in e) for e in _E}!=_E or sorted(g)!=list(range(10)) for g in GENS):raise ValueError('AUTOMORPHISM')

def tag_of(names):
    for t,n in BR.items():
        if list(names)==n:return t
    raise ValueError(('UNKNOWN_VARIABLE_SET',names))

def key(tag,m):
    if m==0:return None
    return ('o',m) if m<1024 else (tag,m)

def row_terms(row):
    k=row[0]
    if k=='mono':
        tag=tag_of(row[1]);n=len(BR[tag]);i=row[2];full=(1<<n)-1
        if not 0<=i<n:raise ValueError('MONO')
        return [(key(tag,full),1),(key(tag,full^(1<<i)),-1)],'ge'
    if k=='cmi':
        tag=tag_of(row[1]);n=len(BR[tag]);i,j,z=row[2:]
        if not 0<=i<j<n or z>>n or z&((1<<i)|(1<<j)):raise ValueError('CMI')
        return [(key(tag,z|1<<i),1),(key(tag,z|1<<j),1),(key(tag,z|1<<i|1<<j),-1),(key(tag,z),-1)],'ge'
    if k=='fd':
        v=row[1];n=sum(1<<(u-1) for u in NB[v]);return [(('o',n|1<<(v-1)),1),(('o',n),-1)],'eq'
    if k=='cap':return [(('o',1<<(row[1]-1)),1)],'cap'
    if k=='sym':
        g=GENS[row[1]];m=row[2]
        if not 0<m<1024:raise ValueError('SYM_MASK')
        gm=sum(1<<g[i] for i in range(10) if m>>i&1);return [(('o',m),1),(('o',gm),-1)],'eq'
    if k in ('copy','independence'):
        tag,new,old,over,existing=COPIES[tuple(row[1])];names=BR[tag];pos={x:i for i,x in enumerate(names)}
        mk=lambda s:sum(1<<pos[x] for x in s);Y=mk(over)
        if k=='copy':
            q,U=row[2],row[3]
            if U&~Y or not 0<q<(1<<len(new)):raise ValueError('COPY_SUBSET')
            nm=sum(1<<pos[new[t]] for t in range(len(new)) if q>>t&1);om=sum(1<<pos[old[t]] for t in range(len(new)) if q>>t&1)
            return [(key(tag,U|nm),1),(key(tag,U|om),-1)],'eq'
        E=mk(existing);Nn=mk(new);return [(key(tag,E|Nn),1),(key(tag,Y),1),(key(tag,E),-1),(key(tag,Y|Nn),-1)],'eq'
    if k=='dfz':
        coef=tuple(row[1]);A,B,C,D,Z=row[2:]
        masks=[A,B,C,D,Z]
        if any(x<0 or x>=1024 for x in masks) or not all(masks[:4]):raise ValueError('DFZ_ROLES')
        for p in range(5):
            for q in range(p+1,5):
                if masks[p]&masks[q]:raise ValueError('DFZ_OVERLAP')
        a,b,c,d,e,f,g,h,i=coef
        def I(x,y,zz):return [(x|zz,1),(y|zz,1),(x|y|zz,-1),(zz,-1)]
        out=[]
        for w,t in [(-a,I(A,B,Z)),(b,I(A,B,C|Z)),(c,I(A,C,B|Z)),(d,I(B,C,A|Z)),(e,I(A,B,D|Z)),(f,I(A,D,B|Z)),(g,I(B,D,A|Z)),(h,I(C,D,Z)),(i,I(C,D,A|Z))]:
            out+=[(key('base',m),w*x) for m,x in t]
        return out,'ge'
    if k=='dfzb':
        tag=row[1];coef=tuple(row[2]);A,B,C,D,Z=row[3:]
        if tag not in ('b1','b2','b3'):raise ValueError('DFZB_TAG')
        n=len(BR[tag]);masks=[A,B,C,D,Z]
        if any(x<0 or x>>n for x in masks) or not all(masks[:4]):raise ValueError('DFZB_ROLES')
        for p in range(5):
            for q in range(p+1,5):
                if masks[p]&masks[q]:raise ValueError('DFZB_OVERLAP')
        a,b,c,d,e,f,g,h,i=coef
        def I(x,y,zz):return [(x|zz,1),(y|zz,1),(x|y|zz,-1),(zz,-1)]
        out=[]
        for w,t in [(-a,I(A,B,Z)),(b,I(A,B,C|Z)),(c,I(A,C,B|Z)),(d,I(B,C,A|Z)),(e,I(A,B,D|Z)),(f,I(A,D,B|Z)),(g,I(B,D,A|Z)),(h,I(C,D,Z)),(i,I(C,D,A|Z))]:
            out+=[(key(tag,m),w*x) for m,x in t]
        return out,'ge'
    raise ValueError(('ROW',k))

def check(cert,verified,mutate=None):
    acc={};beta=Fraction(0);used=set()
    for idx,item in enumerate(cert['multipliers']):
        row=item['row'];w=Fraction(item['multiplier'])
        if mutate and mutate[0]==idx:w=mutate[1](w)
        if row[0] in ('dfz','dfzb'):
            t=tuple(row[1] if row[0]=='dfz' else row[2])
            if t not in verified:raise ValueError(('UNVERIFIED_DFZ',list(t)))
            used.add(t)
        terms,kind=row_terms(row)
        if kind=='ge' and w>0:raise ValueError(('SIGN',row[0]))
        if kind=='cap':
            if w<0:raise ValueError('CAP_SIGN')
            beta+=w
        for kk,x in terms:
            if kk is None:continue
            acc[kk]=acc.get(kk,Fraction(0))+w*x
    acc={kk:x for kk,x in acc.items() if x}
    if acc!={('o',1023):Fraction(1)}:raise ValueError('IDENTITY')
    return beta,used

def main():
    out=ROOT/sys.argv[1];raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERT_HASH')
    cert=json.loads(raw);verified=set()
    for p,s in zip(sys.argv[4::2],sys.argv[5::2]):
        vr=(ROOT/p).read_bytes()
        if sha256(vr).hexdigest()!=s:raise ValueError('VERIFY_HASH')
        doc=json.loads(vr)
        for r in doc['results']:
            if r['valid_exact']:verified.add(tuple(r['coefficients']))
    beta,used=check(cert,verified);controls={}
    gi=next(i for i,m in enumerate(cert['multipliers']) if m['row'][0] in ('cmi','dfz','dfzb') and Fraction(m['multiplier'])!=0)
    try:check(cert,verified,(gi,lambda w:-w))
    except ValueError as e:controls['flipped_inequality_sign']=str(e)
    else:raise ValueError('CONTROL')
    ci=next(i for i,m in enumerate(cert['multipliers']) if m['row'][0]=='cap')
    try:check(cert,verified,(ci,lambda w:w*2))
    except ValueError as e:controls['changed_cap_multiplier']=str(e)
    else:raise ValueError('CONTROL')
    if used:
        try:check(cert,set(list(verified-{sorted(used)[0]})))
        except ValueError as e:controls['dropped_verified_dfz_tuple']=str(e)
        else:raise ValueError('CONTROL')
    rep={'certificate_sha256':sys.argv[3],'all_checked':True,'bound':str(beta),'bound_float':float(beta),
         'rows':len(cert['multipliers']),'row_kinds':{k:sum(1 for m in cert['multipliers'] if m['row'][0]==k) for k in sorted({m['row'][0] for m in cert['multipliers']})},
         'dfz_tuples_used':[list(t) for t in sorted(used)],'negative_controls':controls,
         'limits':'Exact coefficient identity and signs. Validity of each row type: Shannon (theorem), graph FD (definition of the guessing game), caps (alphabet normalization), symmetrization rows (convexity of the closed entropic cone plus invariance of every row family), copy rows (copy lemma), DFZ rows (exactly re-derived from the copy lemma in the cited receipt). The entropy formulation of the guessing number is the standard reduction (BCDRV).'}
    with open(out,'x',encoding='utf-8') as f:json.dump(rep,f,indent=1);f.write('\n')
    print(json.dumps(rep,indent=1))

if __name__=='__main__':main()
