"""Finite strict certificate pass for the13 frozen full-column template formulas.
Old unconditional F +42units only (NO H3). Separate template ledger; no mutation
of the Boolean-cover ledger. No genuine-K5 coverage claim is made by this code.
Exact identity on resume: manifest SHA, base SHA, id, all42units, leaf-CNF SHA.
Each attempted case gets a new ledger version, even UNKNOWN. No retry here.
CaDiCaL900s; binary DRAT streamed/hashed into the same strict drat-trim path,
checker native limit<=3600s; aggregate6GiB guard. Shared free floor per case.
Finite chunk<=10400s (stops between cases; no auto-restart), resume explicitly.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.cnf'
BASE_SHA='6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
NOTE_SHA='1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a'
EXPECTED=[p+'-'+b for p in('P0','P1') for b in('B1','B2','B3','B4','B5')]+['P2-C1','P2-C2','P2-C3']


def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'code'/str(name+'.py'))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def sha(b): return hashlib.sha256(b).hexdigest()


def write_new(path,obj):
    raw=json.dumps(obj,indent=1).encode()
    with path.open('xb') as f: f.write(raw)
    return sha(raw)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--outdir',required=True)
    a=ap.parse_args(); t0=time.monotonic(); out=Path(a.outdir); out.mkdir(exist_ok=True)
    C=load('k5_cover'); R=load('k5_resplit_r2')
    mb=Path(a.manifest).read_bytes(); m=json.loads(mb); mh=sha(mb)
    if m.get('schema')!='k5-column-template-manifest/1' or m.get('base_cnf_sha256')!=BASE_SHA \
       or m.get('proof_note_sha256')!=NOTE_SHA or m.get('run_cases')!=EXPECTED:
        raise RuntimeError('manifest schema/base/proof/case list mismatch')
    base=C.Base(BASE)
    if base.sha!=BASE_SHA: raise RuntimeError('actual base changed')
    cases={x['id']:x for x in m['cases'] if x['run_required']}
    if len(cases)!=13 or set(cases)!=set(EXPECTED): raise RuntimeError('missing/duplicate template')
    for i in EXPECTED:
        x=cases[i]
        if len(x['units'])!=42 or len({abs(v) for v in x['units']})!=42 \
           or x['cnf_sha256']!=base.leaf_sha(x['units']) or x['cnf_clauses']!=base.nc+42:
            raise RuntimeError('case CNF identity mismatch')
        regen=[]
        for row,S in enumerate(x['supports_row2to7'],start=2):
            for co,v in enumerate(C.CHAIN[row-1],start=1): regen.append(v if co in S else -v)
        if regen!=x['units']: raise RuntimeError('support-to-unit mismatch')
    def identity(r):
        x=cases.get(r.get('id'))
        return (x is not None and r.get('manifest_sha256')==mh and r.get('base_cnf_sha256')==base.sha
                and r.get('units')==x['units'] and r.get('cnf_sha256')==x['cnf_sha256'])
    results=out/'RESULTS.jsonl'; recs={}; rec_lines={}
    if results.exists():
        for line in results.read_bytes().split(b'\n'):
            if not line.strip(): continue
            r=json.loads(line)
            if not identity(r) or r['id'] in recs or r.get('strict_ok') is not C.strict_ok(r):
                raise RuntimeError('stale/duplicate/misclassified receipt on resume')
            recs[r['id']]=r; rec_lines[r['id']]=sha(line)
    versions=sorted(out.glob('LEDGER.v*.json'))
    if versions:
        lb=versions[-1].read_bytes(); L=json.loads(lb); lh=sha(lb)
        if L['manifest_sha256']!=mh or L['base_cnf_sha256']!=base.sha or set(L['cases'])!=set(EXPECTED):
            raise RuntimeError('ledger belongs to different inputs')
        for i,x in L['cases'].items():
            if x['units']!=cases[i]['units'] or x['cnf_sha256']!=cases[i]['cnf_sha256']:
                raise RuntimeError('ledger case identity differs')
    else:
        L={'schema':'k5-semantic-template-ledger/1','version':1,'prev_sha256':None,
           'manifest_sha256':mh,'base_cnf_sha256':base.sha,'proof_note_sha256':NOTE_SHA,
           'claim':'restricted CNF cases only; genuine-K5 coverage pending parent review',
           'cases':{i:{'units':cases[i]['units'],'cnf_sha256':cases[i]['cnf_sha256'],
                       'state':'UNSTARTED','evidence':None} for i in EXPECTED}}
        lh=write_new(out/'LEDGER.v001.json',L)
    def update(i,r,line_hash):
        nonlocal L,lh
        old=L['cases'][i]
        new='STRICT_UNSAT' if C.strict_ok(r) else 'UNKNOWN'
        ev={'file':'RESULTS.jsonl','line_sha256':line_hash}
        if old['state']!='UNSTARTED':
            if old['state']!=new or old['evidence']!=ev: raise RuntimeError('ledger/receipt disagreement')
            return
        L=copy.deepcopy(L); L['prev_sha256']=lh; L['version']+=1
        L['cases'][i].update(state=new,evidence=ev)
        L['all_13_strict']=all(x['state']=='STRICT_UNSAT' for x in L['cases'].values())
        L['writer_sha256']=sha(Path(__file__).read_bytes())
        lh=write_new(out/('LEDGER.v%03d.json'%L['version']),L)
    for i,r in recs.items(): update(i,r,rec_lines[i])
    for i,x in L['cases'].items():
        if x['state']!='UNSTARTED' and i not in recs: raise RuntimeError('ledger evidence missing')
    cad=Path(shutil.which('cadical')).resolve()
    meta={'argv':sys.argv,'script_sha256':sha(Path(__file__).read_bytes()),'manifest_sha256':mh,
          'base_cnf_sha256':base.sha,'pipeline_sha256':sha((ROOT/'code/k5_resplit_r2.py').read_bytes()),
          'strict_predicate_sha256':sha((ROOT/'code/k5_cover.py').read_bytes()),
          'cadical_binary':str(cad),'cadical_sha256':sha(cad.read_bytes()),
          'cadical_version':subprocess.run([str(cad),'--version'],capture_output=True,text=True).stdout.strip(),'seed':'default',
          'drat_trim_binary':R.DT,'drat_trim_sha256':sha(Path(R.DT).read_bytes()),
          'solver_limit':900,'checker_limit_max':3600,'aggregate_rss_limit':6*2**30,
          'shared_free_launch_floor':12_200_000_000,'projected_retained_growth_upper_bound':10_000_000,
          'chunk_wall_cap':10400,'start':datetime.now().astimezone().isoformat()}
    write_new(out/('META.%d.json'%int(time.time())),meta)
    fifos=tuple(str(out/('w0.%s.fifo'%x)) for x in('cnf_s','cnf_c','proof'))
    for f in fifos:
        if not Path(f).exists(): os.mkfifo(f)
    for i in EXPECTED:
        if i in recs: continue
        remaining=int(10400-(time.monotonic()-t0))
        free=shutil.disk_usage(out).free
        if free<12_200_000_000 or remaining<960:
            write_new(out/('DEFERRED.%d.json'%int(time.time())),{'before_case':i,'free':free,'remaining':remaining})
            break
        x=cases[i]; n=1
        while (out/(i+'.a%d.solver.log'%n)).exists(): n+=1
        tag=i+'.a%d'%n
        r={'id':i,'manifest_sha256':mh,'base_cnf_sha256':base.sha,'units':x['units'],
           'attempt':1,'tag':tag,'H3_used':False,'semantic_cover_not_yet_accepted':True}
        r.update(R.certify(tag,x['units'],base.nv,base.nc,base.body,str(out),fifos,900,6*2**30,
                           checker_limit=min(3600,remaining-60)))
        if not identity(r): raise RuntimeError('actual streamed formula differs from manifest')
        r['strict_ok']=C.strict_ok(r)
        line=json.dumps(r).encode()
        with results.open('ab') as f: f.write(line+b'\n')
        update(i,r,sha(line)); recs[i]=r
        print(json.dumps({'id':i,'strict_ok':r['strict_ok'],'seconds':r['secs'],
                          'peak_rss':r['aggregate_peak_rss_bytes'],'ledger_version':L['version'],
                          'ledger_sha256':lh}),flush=True)
    print(json.dumps({'ledger_version':L['version'],'ledger_sha256':lh,
                      'counts':{s:sum(x['state']==s for x in L['cases'].values())
                                for s in('UNSTARTED','STRICT_UNSAT','UNKNOWN')},
                      'all_13_strict':all(x['state']=='STRICT_UNSAT' for x in L['cases'].values()),
                      'not_a_K5_exclusion_claim':True}),flush=True)


if __name__=='__main__': main()
