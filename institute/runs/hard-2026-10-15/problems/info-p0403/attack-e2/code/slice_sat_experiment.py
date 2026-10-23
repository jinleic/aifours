"""Bounded exact completion search on a slice passing the analytic screen.

An inconclusive run supplies no negative claim. Any positive full table
is checked independently by direct sums before it may settle the target.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
from free_flat_sat import produce, SEEDS


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--choice',type=int,default=0)
    p.add_argument('--prefix',required=True)
    p.add_argument('--seconds',type=int,default=300)
    p.add_argument('--proof-mb',type=int,default=16)
    p.add_argument('--build-only',action='store_true')
    a=p.parse_args()
    with gzip.open('results/slice-screen.json.gz','rt') as fh:
        screen=json.load(fh)
    choices=sorted(screen['unresolved_case_records'],key=lambda r:(r['slice_l1'],r['source'],r['normal']))
    rec=choices[a.choice]
    source=screen['sources'][rec['source']]
    v=rec['normal']; pivot=(v&-v).bit_length()-1
    basis=[(1<<j)^((1<<pivot) if (v>>j)&1 else 0) for j in range(9) if j!=pivot]
    origin=1<<pivot
    assert bin(v&origin).count('1')%2
    text=source['bits']
    seed=dict(source,normal=v,basis=basis,origin=origin,screen_record=rec,
              choice_in_l1_sorted_viable_list=a.choice,
              scope='Fix source values on normal.x=0; arbitrary 256 values on normal.x=1; all linear output additions.')
    Path(a.prefix+'-seed.json').write_text(json.dumps(seed,indent=2)+'\n')
    SEEDS['slice-fixed']=''.join(format(int(text[i:i+4],2),'X') for i in range(0,512,4))
    produce('slice-fixed',basis,origin,a.prefix,degree_eight=False)
    subprocess.run(['python3','code/audit_free_flat.py',a.prefix,'--seed-json',a.prefix+'-seed.json',
                    '--output',a.prefix+'-encoding-audit.json'],check=True)
    # Keep metadata compact while the solver reads the uncompressed CNF.
    meta_path=Path(a.prefix+'.encoding.json')
    meta_bytes=meta_path.read_bytes()
    Path(a.prefix+'.encoding.json.gz').write_bytes(gzip.compress(meta_bytes,mtime=0)); meta_path.unlink()
    if a.build_only:
        raw=Path(a.prefix+'.cnf').read_bytes()
        Path(a.prefix+'.cnf.gz').write_bytes(gzip.compress(raw,mtime=0)); Path(a.prefix+'.cnf').unlink()
        print('Built audited completion instance:',a.prefix,flush=True)
        return
    subprocess.run(['python3','code/run_cadical.py',a.prefix,'--seconds',str(a.seconds),'--proof-mb',str(a.proof_mb)],check=True)
    run=json.loads(Path(a.prefix+'-run.json').read_text())
    if run['status']=='SAT':
        meta=json.loads(meta_bytes); model={}
        for line in Path(run['solver_log']).read_text().splitlines():
            if line.startswith('v '):
                for literal in map(int,line.split()[1:]):
                    if literal:
                        model[abs(literal)]=literal>0
        f=list(map(int,text))
        for x,var in zip(meta['points'],meta['xs']):
            f[x]=int(model[var])
        from seeds import fwht
        W=fwht(f)
        assert max(map(abs,W))<=28 and 0 in W
        shift=W.index(0)
        f=[b^(bin(x&shift).count('1')%2) for x,b in enumerate(f)]
        bits=''.join(map(str,f)); W=fwht(f)
        witness={'bits':bits,'bit_order':'bits[x]=f(x); x_i=(x>>i)&1',
                 'sha256_ascii_bits':hashlib.sha256(bits.encode()).hexdigest(),'weight':sum(f),
                 'walsh':W,'nonlinearity':256-max(map(abs,W))//2,'linear_shift':shift}
        path=a.prefix+'-witness.json'
        Path(path).write_text(json.dumps(witness,indent=2)+'\n')
        subprocess.run(['python3','code/check_witness.py',path],check=True)
    elif run['status']=='UNSAT':
        subprocess.run(['python3','code/check_lrat.py',a.prefix+'.cnf',a.prefix+'.lrat.gz',
                        '--output',a.prefix+'-proof-check.json'],check=True)
    raw=Path(a.prefix+'.cnf').read_bytes()
    Path(a.prefix+'.cnf.gz').write_bytes(gzip.compress(raw,mtime=0)); Path(a.prefix+'.cnf').unlink()
    print('Completion experiment finished:',a.prefix,run['status'],flush=True)


if __name__=='__main__':
    main()
