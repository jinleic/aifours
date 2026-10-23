"""Independent semantic audit of a signed-FWHT circuit on a free flat.

No producing code imported. Gate truth tables and all full-adder local
identities are exhausted. The complete transform wiring and all 512
character/block rows are reconstructed. This proves the correspondence
for every truth assignment, without sampling the 2^n free-site range.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from itertools import product
import hashlib
import gzip
import json
from pathlib import Path
import re
import numpy as np


def neg(v): return not v if isinstance(v,bool) else -v


def artifact_bytes(name):
    path=Path(name)
    if path.exists():
        return path.read_bytes()
    return gzip.decompress(Path(name+'.gz').read_bytes())


def main():
    p=argparse.ArgumentParser()
    p.add_argument('prefix')
    p.add_argument('--output')
    p.add_argument('--model-log')
    p.add_argument('--broken',action='store_true')
    p.add_argument('--seed-json',help='explicit 512-bit source for a separately scoped experiment')
    args=p.parse_args()
    meta=json.loads(artifact_bytes(args.prefix+'.encoding.json'))
    assert not meta.get('quadratic_spectral_bit',False),'global quadratic-bit reduction is experimental and not an accepted exclusion here'
    rows=[]; nv=nc=None
    cnf_bytes=artifact_bytes(args.prefix+'.cnf')
    for line in cnf_bytes.decode().splitlines():
        if not line or line[0]=='c': continue
        if line[0]=='p':
            _,kind,nv,nc=line.split(); assert kind=='cnf'; nv,nc=int(nv),int(nc)
        else:
            row=list(map(int,line.split())); assert row[-1]==0; rows.append(row[:-1])
    assert nv==meta['variables'] and nc==meta['clauses']==len(rows)
    assert hashlib.sha256(cnf_bytes).hexdigest()==meta['cnf_sha256']
    if args.broken: rows[0][0]*=-1
    primary=meta['primary']; defined=set(primary.values())
    assert defined==set(range(1,len(primary)+1))
    gates={}; require={}; offset=0
    const=1<<(len(primary)+1)
    linear={v:1<<v for v in defined}
    def linear_lit(lit):
        if isinstance(lit,bool): return const if lit else 0
        val=linear.get(abs(lit)); assert val is not None
        return val^(const if lit<0 else 0)
    for block in meta['blocks']:
        assert block['start']==offset
        clauses=rows[offset:block['end']]; offset=block['end']
        if block['kind']=='gate':
            a,b,o,op=block['a'],block['b'],block['out'],block['op']
            assert type(a) is int and type(b) is int and abs(a)!=abs(b)
            assert abs(a) in defined and abs(b) in defined and o not in defined
            assert all(abs(v) in (abs(a),abs(b),o) for row in clauses for v in row)
            for av,bv,ov in product((False,True),repeat=3):
                vals={abs(a):av,abs(b):bv,o:ov}
                def lit(v): return vals[abs(v)]==(v>0)
                aa,bb=lit(a),lit(b)
                want={'xor':aa!=bb,'and':aa and bb,'or':aa or bb}[op]
                assert all(any(lit(v) for v in row) for row in clauses)==(ov==want)
            gates[o]=(op,a,b); defined.add(o)
            linear[o]=(linear_lit(a)^linear_lit(b)) if op=='xor' and linear.get(abs(a)) is not None and linear.get(abs(b)) is not None else None
        elif block['kind']=='require':
            assert clauses==[block['lits']]
            assert block['role'] not in require
            require[block['role']]=block['lits']
        else: raise AssertionError(('unexpected block',block['kind']))
    assert offset==nc and defined==set(range(1,nv+1))
    def evaluate(lit,external,cache=None):
        if isinstance(lit,bool): return lit
        if cache is None: cache={}
        v=abs(lit)
        if v in external: result=external[v]
        elif v in cache: result=cache[v]
        else:
            assert v in gates,('unexpected external dependency',v)
            op,a,b=gates[v]
            aa=evaluate(a,external,cache); bb=evaluate(b,external,cache)
            result={'xor':aa!=bb,'and':aa and bb,'or':aa or bb}[op]
            cache[v]=result
        return result if lit>0 else not result
    def all_external(literals):
        variables=sorted({abs(v) for v in literals if type(v) is int})
        for vals in product((False,True),repeat=len(variables)): yield dict(zip(variables,vals))
    n=len(meta['points']); d=n.bit_length()-1; width=meta['word_width']
    assert n in (64,128,256,512) and n==1<<d and width==d+2
    words=[[True]+[x]*(width-1) for x in meta['xs']]
    adder_bits=0
    for level,stage in enumerate(meta['stages']):
        h=1<<level; assert stage['width']==h
        new=[None]*n; ai=0
        for start in range(0,n,2*h):
            for j in range(h):
                A,B=words[start+j],words[start+j+h]
                for subtract,index in ((False,start+j),(True,start+j+h)):
                    adder=stage['adders'][ai]; ai+=1
                    assert adder['A']==A and adder['B']==B and adder['subtract']==subtract
                    assert len(adder['steps'])==width
                    carry=subtract
                    for bit,step in enumerate(adder['steps']):
                        a=A[bit]; b=neg(B[bit]) if subtract else B[bit]
                        assert step['a']==a and step['b']==b and step['cin']==carry and step['sum']==adder['out'][bit]
                        for external in all_external((a,b,carry)):
                            total=int(evaluate(a,external))+int(evaluate(b,external))+int(evaluate(carry,external))
                            assert evaluate(step['sum'],external)==bool(total&1)
                            assert evaluate(step['cout'],external)==bool(total>=2)
                        carry=step['cout']; adder_bits+=1
                    new[index]=adder['out']
        assert ai==len(stage['adders'])==n and new==stage['outputs']
        words=new
    assert len(meta['stages'])==d and words==meta['outputs']
    # Stages are exact modulo 2^width. Every true intermediate transform
    # lies in [-n,n], strictly inside this signed word range, so these
    # checked modular additions also equal the integer FWHT universally.
    if args.seed_json:
        seed_data=json.loads(Path(args.seed_json).read_text())
        seed_text=seed_data['bits']
        assert len(seed_text)==512 and set(seed_text)<={'0','1'}
        assert hashlib.sha256(seed_text.encode()).hexdigest()==seed_data['sha256_ascii_bits']
        hx=''.join(format(int(seed_text[i:i+4],2),'X') for i in range(0,512,4))
        assert meta['seed']=='slice-fixed' and not meta['degree_eight_necessary_constraint']
    else:
        source=Path('selection-inputs/literature/kavut-yucel.reader.md').read_text().split('#### 3.2')[0]
        raw=re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$',source)
        assert len(raw)==3
        hx=''.join(dict(zip(('dsbf40','dsbf32','rsbf56'),raw))[meta['seed']])
    assert hx==meta['seed_hex']
    f=np.array([int(b) for ch in hx for b in format(int(ch,16),'04b')],dtype=np.int32)
    basis=meta['basis']; origin=meta['origin']; points=meta['points']
    assert len(basis)==d and len(set(points))==n
    for t,x in enumerate(points):
        expected=origin
        for j,b in enumerate(basis):
            if (t>>j)&1: expected^=b
        assert x==expected
    H=np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int32)
    Hn=np.array([[1-2*(bin(a&t).count('1')%2) for t in range(n)] for a in range(n)],dtype=np.int32)
    dual=np.array([sum((1<<j) for j,b in enumerate(basis) if bin(a&b).count('1')%2) for a in range(512)],dtype=np.int32)
    phase=H[:,origin]
    assert np.array_equal(H[:,points],phase[:,None]*Hn[dual,:])
    outside=np.ones(512,dtype=bool); outside[points]=False
    fixed=H[:,outside]@(1-2*f[outside])
    groups=[(phase*fixed)[dual==h].tolist() for h in range(n)]
    assert all(sorted(g)==sorted(old) for g,old in zip(groups,meta['outside_offsets']))
    targetsets={h:sorted({-c for c in group if -n<=-c<=n and c%2==0}) for h,group in enumerate(groups)}
    required=meta.get('required_zero_origin')
    if required is not None:
        targetsets={h:([-int(phase[required]*fixed[required])] if h==int(dual[required]) else []) for h in range(n)}
    selectors={(h,v):s for h,v,s in meta['zero_selectors']}
    assert set(selectors)=={(h,v) for h,vs in targetsets.items() for v in vs}
    want_primary={'new_f_%d'%t:x for t,x in enumerate(meta['xs'])}
    want_primary.update({'zero_%d_%d'%(h,v):s for (h,v),s in selectors.items()})
    assert want_primary==primary
    expected_require={}
    def req(role,lits):
        if any(v is True for v in lits): return
        expected_require[role]=[v for v in lits if v is not False]
    bound=meta['bound']
    comparators={item['h']:item for item in meta.get('comparators',[])}
    comparator_values=0
    for h,group in enumerate(groups):
        low=-bound-min(group); high=bound-max(group)
        if n==64:
            for rawvalue in range(1<<width):
                value=rawvalue if rawvalue<(1<<(width-1)) else rawvalue-(1<<width)
                if low<=value<=high: continue
                req('forbid-%d-%d'%(h,rawvalue),[neg(words[h][j]) if (rawvalue>>j)&1 else words[h][j] for j in range(width)])
        else:
            item=comparators[h]; assert (item['low'],item['high'])==(low,high)
            for rawvalue in range(1<<width):
                external={}; consistent=True
                for j,wire in enumerate(words[h]):
                    bit=bool((rawvalue>>j)&1)
                    if isinstance(wire,bool):
                        consistent &= wire==bit
                    else:
                        val=bit if wire>0 else not bit
                        if abs(wire) in external: consistent &= external[abs(wire)]==val
                        external[abs(wire)]=val
                if not consistent: continue
                value=rawvalue if rawvalue<(1<<(width-1)) else rawvalue-(1<<width)
                assert evaluate(item['lower'],external)==(value>=low)
                assert evaluate(item['upper'],external)==(value<=high)
                comparator_values+=1
            req('lower-%d'%h,[item['lower']]); req('upper-%d'%h,[item['upper']])
        for v in targetsets[h]:
            selector=selectors[h,v]
            for j in range(width): req('zero-%d-%d-%d'%(h,v,j),[-selector,words[h][j] if ((v%(1<<width))>>j)&1 else neg(words[h][j])])
    req('some-walsh-zero',list(selectors.values()))
    canonical=meta.get('canonical_support_xor')
    if meta['degree_eight_necessary_constraint']:
        # The seed has support XOR zero. Thus the parity of changed
        # support indices is exactly the new function's support XOR.
        seedxor=0
        for x,b in enumerate(f):
            if b: seedxor^=x
        assert seedxor==0
        for j,out in enumerate(meta['support_xor']):
            expected=0
            for t,x in enumerate(points):
                if (x>>j)&1: expected^=(1<<meta['xs'][t])^(const if f[x] else 0)
            assert linear_lit(out)==expected
        if canonical is None: req('nonzero-support-xor',meta['support_xor'])
        else:
            assert n==512
            for j in range(9): req('canonical-support-xor-%d'%j,[meta['support_xor'][j] if (canonical>>j)&1 else neg(meta['support_xor'][j])])
    if n==512: req('complement-normalization',[neg(meta['xs'][points.index(0)])])
    forced=meta.get('forced_truth_json')
    if forced:
        bits=Path(forced).read_text(); bits=json.loads(bits)['bits']
        for t,x in enumerate(points): req('forced-truth-%d'%t,[meta['xs'][t] if bits[x]=='1' else neg(meta['xs'][t])])
    assert require==expected_require,('missing or extra constraints',set(require)^set(expected_require))
    result={'status':'PASS','prefix':args.prefix,'free_points':n,'signed_word_width':width,'variables':nv,'clauses':nc,'all_gate_truth_tables_checked':len(gates),'full_adder_bit_identities_checked':adder_bits,'all_original_character_rows_checked':512,'comparator_values_checked':comparator_values,'cnf_sha256':meta['cnf_sha256'],'scope':'universal composition audit of the free-flat constraints, with the necessary degree-eight/support-XOR restriction from the self-contained proof'}
    if not meta['degree_eight_necessary_constraint']:
        result['scope']='universal composition audit of the free-flat constraints; no algebraic-degree or support-XOR restriction included'
    if args.model_log:
        model={}
        text=Path(args.model_log).read_text(); assert 's SATISFIABLE' in text
        for line in text.splitlines():
            if line.startswith('v '):
                for v in map(int,line.split()[1:]):
                    if v: model[abs(v)]=v>0
        def lit(v): return model[abs(v)]==(v>0)
        assert all(any(lit(v) for v in row) for row in rows)
        g=f.copy()
        for x,var in zip(points,meta['xs']): g[x]=int(model[var])
        wg=H@(1-2*g)
        assert int(max(abs(wg)))<=bound and np.any(wg==0)
        if required is not None: assert wg[required]==0
        result['satisfying_model_checked']=True
        result['model_max_abs_W']=int(max(abs(wg)))
    if args.output: Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__=='__main__': main()
