"""Short positive-only experiment with explicit odd-slice Walsh residues.

For odd-weight h on eight variables, H/2 mod4=-wt(h)+2 a.supportXOR.
Complementing h negates H, swaps the two full Walsh halves, and preserves
the bounds and existence of a zero. Hence wt(h)=1 mod4 is a legitimate
normalization and H bit2 = 1 XOR a.supportXOR. No negative solver verdict
from this experiment is a certified exclusion.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
from local_sat import CNF,neg
from seeds import fwht


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--base',required=True)
    p.add_argument('--prefix',required=True)
    p.add_argument('--seconds',type=int,default=180)
    a=p.parse_args()
    with gzip.open(a.base+'.encoding.json.gz','rt') as fh:
        meta=json.load(fh)
    assert len(meta['points'])==256 and not meta['degree_eight_necessary_constraint']
    original=gzip.decompress(Path(a.base+'.cnf.gz').read_bytes()).decode()
    header,body=original.split('\n',1)
    _,kind,nv,nc=header.split(); assert kind=='cnf'
    nv,nc=int(nv),int(nc)
    cnf=CNF(); cnf.n=nv
    xs=meta['xs']; words=meta['outputs']
    def parity(literals):
        out=False
        for literal in literals:
            out=cnf.gate('xor',out,literal)
        return out
    cnf.require([parity(xs)],'odd-slice-weight')
    support=[parity([x for t,x in enumerate(xs) if (t>>j)&1]) for j in range(8)]
    for frequency in range(256):
        expression=parity([support[j] for j in range(8) if (frequency>>j)&1])
        cnf.require([neg(cnf.gate('xor',words[frequency][2],neg(expression)))],
                    'linear-walsh-residue-%d'%frequency)
        cnf.require([words[frequency][1]],'odd-walsh-residue-%d'%frequency)
    # Concrete bound-32 planted completion checks every bit identity.
    f=[int(b) for c in meta['seed_hex'] for b in format(int(c,16),'04b')]
    h=[f[x] for x in meta['points']]
    assert sum(h)%2
    if sum(h)%4==3:
        h=[b^1 for b in h]
    W=fwht(h); s=0
    for t,b in enumerate(h):
        if b:
            s^=t
    assert sum(h)%4==1
    assert all(w%4==2 and ((w>>2)&1)==(1^(bin(i&s).count('1')%2)) for i,w in enumerate(W))
    # Exhaust all eight truth assignments of every new XOR gate.
    for block in cnf.blocks:
        if block['kind']=='gate':
            assert block['op']=='xor'
            aa,bb,out=block['a'],block['b'],block['out']
            rows=cnf.clauses[block['start']:block['end']]
            for av in (False,True):
                for bv in (False,True):
                    for ov in (False,True):
                        env={abs(aa):av,abs(bb):bv,out:ov}
                        literal=lambda v:env[abs(v)]==(v>0)
                        assert all(any(literal(v) for v in row) for row in rows)==(ov==(literal(aa)!=literal(bb)))
    delta=''.join(' '.join(map(str,row))+' 0\n' for row in cnf.clauses)
    text='p cnf %d %d\n'%(cnf.n,nc+len(cnf.clauses))+body+delta
    prefix=Path(a.prefix)
    Path(a.prefix+'.cnf.gz').write_bytes(gzip.compress(text.encode(),mtime=0))
    # Primary truth variables retain their IDs. The positive decoder
    # only uses those variables; this is not a full certificate auditor.
    meta.update(variables=cnf.n,clauses=nc+len(cnf.clauses),cnf_sha256=hashlib.sha256(text.encode()).hexdigest(),
                experimental_lowbit_normalization=True,base_encoding=a.base,
                normalization_gate_blocks=cnf.blocks,normalization_planted_control='all 256 coefficients of the source slice after optional complementation')
    Path(a.prefix+'.encoding.json.gz').write_bytes(gzip.compress(json.dumps(meta,separators=(',',':')).encode(),mtime=0))
    seed_path=Path(a.base+'-seed.json')
    Path(a.prefix+'-seed.json').write_bytes(seed_path.read_bytes())
    print('PASS planted residue identities and all new XOR truth tables; added variables',cnf.n-nv,
          'added clauses',len(cnf.clauses),flush=True)
    subprocess.run(['python3','code/slice_positive_search.py',a.prefix,'--seconds',str(a.seconds)],check=True)


if __name__=='__main__':
    main()
