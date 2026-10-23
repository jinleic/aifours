"""FWHT bit-circuit search on an explicitly free affine flat.

Eight-bit signed arithmetic suffices for up to 64 input signs. Each
adder records its bit steps for an independent local-identity audit.
This producer does not treat solver UNKNOWN as an exclusion.
"""
import argparse
import hashlib
import json
from pathlib import Path
from local_sat import CNF,neg
from seeds import SEEDS,decode,fwht


def add(cnf,A,B,subtract=False):
    carry=bool(subtract)
    out=[]; steps=[]
    for j,(a,oldb) in enumerate(zip(A,B)):
        b=neg(oldb) if subtract else oldb
        cin=carry
        t=cnf.gate('xor',a,b)
        s=cnf.gate('xor',t,cin)
        carry=cnf.gate('or',cnf.gate('and',a,b),cnf.gate('and',t,cin))
        out.append(s)
        steps.append({'a':a,'b':b,'cin':cin,'sum':s,'cout':carry})
    return out,{'A':A,'B':B,'subtract':subtract,'out':out,'steps':steps}


def unsigned_le(cnf,bits,constant):
    if constant<0: return False
    if constant>=(1<<len(bits))-1: return True
    lt=False; eq=True
    for j in reversed(range(len(bits))):
        if (constant>>j)&1:
            lt=cnf.gate('or',lt,cnf.gate('and',eq,neg(bits[j])))
            eq=cnf.gate('and',eq,bits[j])
        else:
            eq=cnf.gate('and',eq,neg(bits[j]))
    return cnf.gate('or',lt,eq)


def produce(seed,basis,origin,prefix,degree_eight=True,zero_origin=None,canonical_xor=None,quadratic_bit=False,bound=28,force_json=None,compare=False):
    d=len(basis); n=1<<d; width=d+2
    assert d in (6,7,8,9)
    f=decode(SEEDS[seed]); W=fwht(f)
    points=[]
    for t in range(n):
        x=origin
        for j,b in enumerate(basis):
            if (t>>j)&1: x^=b
        points.append(x)
    assert len(set(points))==n
    old=fwht([f[x] for x in points])
    groups=[[] for _ in range(n)]
    where=[]
    for a in range(512):
        h=sum((1<<j) for j,b in enumerate(basis) if bin(a&b).count('1')%2)
        phase=1-2*(bin(a&origin).count('1')%2)
        groups[h].append(phase*W[a]-old[h])
        where.append((h,phase*W[a]-old[h]))
    assert all(len(g)==512//n for g in groups)
    targets={h:sorted({-c for c in g if -n<=-c<=n and c%2==0}) for h,g in enumerate(groups)}
    if zero_origin is not None:
        h,c=where[zero_origin]
        targets={hh:([-c] if hh==h else []) for hh in range(n)}
    cnf=CNF()
    xs=[cnf.var('new_f_%d'%t) for t in range(n)]
    selectors={(h,v):cnf.var('zero_%d_%d'%(h,v)) for h,vs in targets.items() for v in vs}
    qvars={}
    if quadratic_bit:
        assert n==512 and origin==0 and basis==[1<<j for j in range(9)] and canonical_xor==1
        for i in range(9): qvars[str(1<<i)]=cnf.var('q_%d'%(1<<i))
        for i in range(9):
            for j in range(i+1,9):
                mask=(1<<i)|(1<<j); qvars[str(mask)]=cnf.var('q_%d'%mask)
    words=[[True]+[v]*(width-1) for v in xs]
    stages=[]
    k=1
    while k<n:
        adders=[]
        new=[None]*n
        for i in range(0,n,2*k):
            for j in range(k):
                a,b=words[i+j],words[i+j+k]
                new[i+j],plus=add(cnf,a,b)
                new[i+j+k],minus=add(cnf,a,b,True)
                adders.extend([plus,minus])
        stages.append({'width':k,'adders':adders,'outputs':new})
        words=new
        k*=2
    comparators=[]
    for h,g in enumerate(groups):
        low=-bound-min(g); high=bound-max(g)
        if n==64:
            for raw in range(256):
                val=raw if raw<128 else raw-256
                if low<=val<=high: continue
                cnf.require([neg(words[h][j]) if (raw>>j)&1 else words[h][j] for j in range(width)],'forbid-%d-%d'%(h,raw))
        else:
            biased=words[h][:-1]+[neg(words[h][-1])]
            lower=neg(unsigned_le(cnf,biased,low-1+(1<<(width-1))))
            upper=unsigned_le(cnf,biased,high+(1<<(width-1)))
            cnf.require([lower],'lower-%d'%h)
            cnf.require([upper],'upper-%d'%h)
            comparators.append({'h':h,'low':low,'high':high,'lower':lower,'upper':upper})
        for v in targets[h]:
            selector=selectors[h,v]
            for j in range(width):
                cnf.require([-selector,words[h][j] if ((v%(1<<width))>>j)&1 else neg(words[h][j])],'zero-%d-%d-%d'%(h,v,j))
    cnf.require(list(selectors.values()),'some-walsh-zero')
    xors=[]
    if degree_eight:
        for j in range(9):
            parity=False
            for t,x in enumerate(points):
                if (x>>j)&1:
                    term=neg(xs[t]) if f[x] else xs[t]
                    parity=cnf.gate('xor',parity,term)
            xors.append(parity)
        if canonical_xor is None: cnf.require(xors,'nonzero-support-xor')
        else:
            assert n==512
            for j in range(9): cnf.require([xors[j] if (canonical_xor>>j)&1 else neg(xors[j])],'canonical-support-xor-%d'%j)
    if n==512:
        cnf.require([neg(xs[points.index(0)])],'complement-normalization')
    if quadratic_bit:
        for a in range(512):
            q=False
            for mask,var in qvars.items():
                if int(mask)&a==int(mask): q=cnf.gate('xor',q,var)
            cnf.require([neg(cnf.gate('xor',words[a][3],q))],'quadratic-spectral-bit-%d'%a)
    if force_json:
        forced=json.loads(Path(force_json).read_text())['bits']
        for t,x in enumerate(points): cnf.require([xs[t] if forced[x]=='1' else neg(xs[t])],'forced-truth-%d'%t)
    text='p cnf %d %d\n'%(cnf.n,len(cnf.clauses))+''.join(' '.join(map(str,row))+' 0\n' for row in cnf.clauses)
    if compare: assert Path(prefix+'.cnf').read_text()==text
    else: Path(prefix+'.cnf').write_text(text)
    meta={'seed':seed,'seed_hex':SEEDS[seed],'basis':basis,'origin':origin,'points':points,'bound':bound,'word_width':width,'xs':xs,'zero_selectors':[[h,v,s] for (h,v),s in selectors.items()],'primary':cnf.primary,'stages':stages,'outputs':words,'outside_offsets':groups,'degree_eight_necessary_constraint':degree_eight,'support_xor':xors,'canonical_support_xor':canonical_xor,'required_zero_origin':zero_origin,'quadratic_spectral_bit':quadratic_bit,'q_variables':qvars,'comparators':comparators,'forced_truth_json':force_json,'variables':cnf.n,'clauses':len(cnf.clauses),'cnf_sha256':hashlib.sha256(text.encode()).hexdigest(),'blocks':cnf.blocks}
    if not compare: Path(prefix+'.encoding.json').write_text(json.dumps(meta,separators=(',',':'))+'\n')
    print(prefix,'variables',cnf.n,'clauses',len(cnf.clauses),'sha256',meta['cnf_sha256'])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seed',choices=SEEDS,default='dsbf40')
    p.add_argument('--prefix',default='results/dsbf40-free64')
    p.add_argument('--basis',default='27,45,195,325,1,2')
    p.add_argument('--origin',type=int,default=5)
    p.add_argument('--model-log')
    p.add_argument('--zero-origin',type=int)
    p.add_argument('--canonical-xor',type=int)
    p.add_argument('--quadratic-bit',action='store_true')
    p.add_argument('--bound',type=int,default=28)
    p.add_argument('--force-json')
    p.add_argument('--compare',action='store_true')
    args=p.parse_args()
    if args.model_log:
        meta=json.loads(Path(args.prefix+'.encoding.json').read_text())
        vals={}
        log=Path(args.model_log).read_text()
        assert 's SATISFIABLE' in log
        for line in log.splitlines():
            if line.startswith('v '):
                for v in map(int,line.split()[1:]):
                    if v: vals[abs(v)]=v>0
        f=decode(meta['seed_hex'])
        for x,var in zip(meta['points'],meta['xs']): f[x]=int(vals[var])
        W=fwht(f)
        assert max(map(abs,W))<=28 and 0 in W
        shift=W.index(0)
        f=[b^(bin(x&shift).count('1')%2) for x,b in enumerate(f)]
        txt=''.join(map(str,f))
        result={'bits':txt,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(f),'walsh':fwht(f),'nonlinearity':256-max(map(abs,fwht(f)))//2,'linear_shift':shift}
        Path(args.prefix+'-target.json').write_text(json.dumps(result,indent=2)+'\n')
    else:
        produce(args.seed,list(map(int,args.basis.split(','))),args.origin,args.prefix,True,args.zero_origin,args.canonical_xor,args.quadratic_bit,args.bound,args.force_json,args.compare)


if __name__=='__main__': main()
