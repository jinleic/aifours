#!/usr/bin/env python3
"""Bounded independent integer checker for one new 13-variable FD identity.
No producer/old checker/solver/archive is imported. This establishes the
identity under explicitly named functional and actual-component FD premises;
it does not itself referee the written component/fiber application.
"""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json,sys
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
PAT=('A','B','A','O','A','A','fixed','B','A','A')
Y=1023;A=1024;B=2048;T=4096;AB=A|B;FULL=8191

def vm(vs):return sum(1<<(v-1) for v in vs)
def sparse(terms):
    d={}
    for m,w in terms:
        if m:d[m]=d.get(m,0)+w
    return [[m,w] for m,w in sorted(d.items()) if w]
def conditional_entropy(block,given):
    if block&given:raise ValueError('DISJOINT_CE_BLOCK')
    return sparse(((block|given,1),(given,-1)))

def shannon(nm):
    if nm[0]=='cmi':
        if len(nm)!=4:raise ValueError('CMI_ARITY')
        _,i,j,K=nm
        if any(type(x) is not int for x in (i,j,K)) or not 0<=i<j<13 or not 0<=K<=FULL or K&((1<<i)|(1<<j)):raise ValueError('ORDINARY_CMI')
        return sparse(((K|1<<i,1),(K|1<<j,1),(K|1<<i|1<<j,-1),(K,-1)))
    if nm[0]=='ce':
        if len(nm)!=3:raise ValueError('CE_ARITY')
        _,i,K=nm
        if type(i) is not int or type(K) is not int or not 0<=i<13 or not 0<=K<=FULL or K>>i&1:raise ValueError('ORDINARY_CE')
        return conditional_entropy(1<<i,K)
    raise ValueError('NOT_ORDINARY_SHANNON')

def incident(v):return {PAT[t] for t,f in enumerate(TRI) if v in f and PAT[t]!='fixed'}
def info(v):
    labels=incident(v)
    if {'A','B'}<=labels:return AB
    if {'A','O'}<=labels:return T
    if labels=={'A'}:return A
    if labels=={'B'}:return B
    raise ValueError(('INCIDENT_INFORMATION',v,labels))
def known_from(block):return {A:{'A'},B:{'B'},T:{'A','O'},AB:{'A','B','O'}}[block]
def local(v):
    vs={u for t,f in enumerate(TRI) if PAT[t]!='fixed' and v in f for u in f if u!=v}
    if not vs or not vs<=set(N[v]):raise ValueError('ACTUAL_LOCAL_TRIANGLE_VERTICES')
    return vm(vs)

def fd(nm):
    if len(nm)!=2:raise ValueError('FD_ARITY')
    k,x=nm
    if type(x) is not int:raise ValueError('FD_INTEGER_ARGUMENT')
    if k in ('A-from-T','T-from-AB'):
        if not 0<=x<=Y:raise ValueError('ORIGINAL_CONDITION_MASK')
        return conditional_entropy(A,x|T) if k=='A-from-T' else conditional_entropy(T,x|AB)
    if k=='factor-info':
        if not 1<=x<=10 or PAT[x-1] not in ('A','B'):raise ValueError('FACTOR_INFORMATION_PREMISE')
        return conditional_entropy(A if PAT[x-1]=='A' else B,vm(TRI[x-1]))
    if x not in N:raise ValueError('VERTEX')
    if k=='graph-fd':return conditional_entropy(1<<(x-1),vm(N[x]))
    if k=='neighbor-info':
        # The original FD recovers Yv, making every incident parity known.
        return conditional_entropy(info(x),vm(N[x]))
    if k in ('local-info-fd','local-state-fd'):
        aux=AB if k=='local-state-fd' else info(x)
        if not incident(x)<=known_from(aux):raise ValueError('LOCAL_PARITIES_NOT_KNOWN')
        return conditional_entropy(1<<(x-1),local(x)|aux)
    raise ValueError(('UNSUPPORTED_FD',nm))

def verify(c,changed=False):
    if c['N']!={str(v):list(N[v]) for v in N} or c['TRI']!=[list(f) for f in TRI] or c['pattern']!=list(PAT):raise ValueError('LITERAL_COMPONENT_CONTRACT')
    scale=c['scale']
    if type(scale) is not int or scale<=0:raise ValueError('SCALE')
    if len(c['shannon_rows'])>1024 or len(c['fd_rows'])>256:raise ValueError('SMALL_IDENTITY_BOUND')
    acc=[0]*8192;counts=Counter()
    for family,key,parser in (('Shannon','shannon_rows',shannon),('FD','fd_rows',fd)):
        seen=set()
        for item in c[key]:
            nm=item['row'];q=item['multiplier'];name=tuple(nm)
            if type(q) is not int or not q or (family=='Shannon' and q<0):raise ValueError('INTEGER_SIGN')
            if name in seen:raise ValueError('DUPLICATE_ROW')
            seen.add(name);terms=parser(nm)
            if terms!=item['literal_vector']:raise ValueError('LITERAL_VECTOR_NOT_SEMANTIC_ROW')
            for m,w in terms:acc[m]+=q*w
            counts[family+':'+nm[0]]+=1
    expected=[0]*8192;expected[Y]=(-4 if changed else -3)*scale
    for i in range(10):expected[1<<i]=2*scale
    if acc!=expected:raise ValueError('FULL_INTEGER_IDENTITY')
    target=[[Y,-3*scale]]+[[1<<i,2*scale] for i in range(10)]
    if c['target_vector']!=target:raise ValueError('TARGET_RECORD')
    return {'Shannon_rows':len(c['shannon_rows']),'declared_zero_FD_rows':len(c['fd_rows']),'row_kinds':dict(counts),'scale':scale,'raw_nonempty_coordinates':8191,'zero_coefficient_residual':True}

def controls(c):
    result={}
    def rejects(name,x,changed=False):
        try:verify(x,changed)
        except ValueError as e:result[name]=str(e)
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    rejects('changed_target',c,True)
    d=deepcopy(c);d['shannon_rows'][0]['multiplier']*=-1;rejects('flipped_Shannon_sign',d)
    d=deepcopy(c);d['fd_rows'][0]['literal_vector'][0][1]+=1;rejects('altered_FD_vector',d)
    d=deepcopy(c);d['pattern'][6]='A';rejects('removed_fixed_factor_premise',d)
    d=deepcopy(c);d['fd_rows']=d['fd_rows'][:-1];rejects('dropped_FD_row',d)
    return result

def main():
    root=Path(__file__).resolve().parent;raw=(root/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('CERTIFICATE_HASH')
    c=json.loads(raw);r={'certificate_sha256':sys.argv[3],'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),**verify(c),'negative_controls':controls(c),'scope':'One small new conditional Shannon/FD integer identity. The listed FD rows must hold; the arbitrary-group actual-component/fiber application remains a written scientific-review obligation. No bulk archive replay, formal proof, probability witness, unrestricted bound, novelty or adoption.'}
    with (root/sys.argv[1]).open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps(r,indent=2))
if __name__=='__main__':main()
