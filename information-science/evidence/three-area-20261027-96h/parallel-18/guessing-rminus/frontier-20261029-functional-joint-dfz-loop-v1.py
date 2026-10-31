#!/usr/bin/env python3
"""Bounded separator/dual/primal loop, using existing exported proposals first.
Usage: python3 script.py PREFIX ROUNDS POINTS.jsonl POINTS_SHA CUTS.json CUTS_SHA INDICES
Every round consumes a frozen point, proposes already-admitted DFZ rows, writes
a NEW literal cut file, and tries a direct exact dual. Each produced dual is
independently checked before the corresponding case leaves the active set.
Only still-active cases are re-solved to new proposal points. All artifacts are
append-only exclusive outputs. No paused gate-import route is invoked.
"""
from hashlib import sha256
from pathlib import Path
import json,os,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
ENV=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
CLASSES='frontier-20261029-residual-plane-colorings-v1.json'
VERIFY=[('frontier-20261029-dfz-inequality-verify-result.json','12f6aa96a6ec70ee6622e4d6981d98d3e3d89ff717f061c137d8c1e52699a727'),
 ('frontier-20261029-dfz-inequality-verify-base-used.json','206f4a17575c632b3185030d2c58dd9c6bc47c098a93961eb6d827afa27434e5'),
 ('frontier-20261029-dfz-inequality-verify-v9b.json','614fda6760c476ff15330dc489dbb463930261808740c708cbcefb1048a574e5')]
def sha(path):return sha256((ROOT/path).read_bytes()).hexdigest()
def save(path,data):
    with open(ROOT/path,'x') as f:json.dump(data,f,indent=1);f.write('\n')
def run(args):
    p=subprocess.run(['python3',*args],cwd=ROOT,env=ENV,capture_output=True,text=True)
    if p.returncode:raise RuntimeError({'args':args,'returncode':p.returncode,'stderr':p.stderr[-3000:],'stdout':p.stdout[-1000:]})
    return p.stdout

def main():
    prefix=sys.argv[1];rounds=int(sys.argv[2]);point=sys.argv[3];pointsha=sys.argv[4];cutfile=sys.argv[5];cutsha=sys.argv[6];active=[int(x) for x in sys.argv[7].split(',')]
    if sha(point)!=pointsha or sha(cutfile)!=cutsha:raise ValueError('INPUT_HASH')
    if sha(CLASSES)!='103658a2febb098f0949c4fe010624ff7d20328d93f217352967e9eeb80ff956':raise ValueError('CLASS_HASH')
    literal=json.loads((ROOT/cutfile).read_text())['cuts'];seen={(tuple(c['coefficients']),*(c[k] for k in ('A','B','C','D','Z'))) for c in literal}
    entries=[];accepted=[];stop='round_limit';t=time.monotonic()
    for n in range(1,rounds+1):
        csv=','.join(map(str,active));scan=f'{prefix}-r{n}-scan.json'
        run(['frontier-20261029-functional-joint-dfz-proposal-scan-v1.py',scan,point,pointsha,csv]);scan_doc=json.loads((ROOT/scan).read_text());added=0
        for case in scan_doc['cases']:
            for c in case['cuts']:
                key=(tuple(c['coefficients']),*(c[k] for k in ('A','B','C','D','Z')))
                if key in seen:continue
                seen.add(key);literal.append({k:c[k] for k in ('coefficients','A','B','C','D','Z')});added+=1
        entry={'round':n,'input_points':point,'input_points_sha256':pointsha,'scan':scan,'scan_sha256':sha(scan),'active_before':active.copy(),'added_cuts':added,'literal_cuts':len(literal)}
        if not added:
            stop='no_new_singleton_separator_on_exported_proposals_NOT_an_exact_saturation_claim';entries.append(entry);save(f'{prefix}-r{n}-receipt.json',entry);break
        cutfile=f'{prefix}-r{n}-cuts.json';save(cutfile,{'source_scan_sha256':sha(scan),'cuts':literal});cutsha=sha(cutfile)
        dual=f'{prefix}-r{n}-dual.jsonl'
        run(['frontier-20261029-plane-functional-joint-dfz-dual-v2.py',dual,CLASSES,csv,'120',cutfile,cutsha]);dual_records=[json.loads(l) for l in (ROOT/dual).read_text().splitlines()]
        entry.update({'cuts':cutfile,'cuts_sha256':cutsha,'dual':dual,'dual_sha256':sha(dual),'dual_statuses':{str(r['index']):r['status'] for r in dual_records}})
        good=[r for r in dual_records if r['status']=='ok']
        if good:
            certfile=f'{prefix}-r{n}-certs.json';save(certfile,{'source_dual_sha256':sha(dual),'indices':[r['index'] for r in good],'certificates':[r['certificate'] for r in good]})
            checkfile=f'{prefix}-r{n}-check.json';args=['frontier-20261029-plane-functional-joint-dfz-check-v2.py',checkfile,certfile,sha(certfile)]+[x for pair in VERIFY for x in pair];run(args)
            if not json.loads((ROOT/checkfile).read_text())['all_checked']:raise ValueError('INDEPENDENT_CHECK')
            entry.update({'checked_cases':[r['index'] for r in good],'certificates':certfile,'certificates_sha256':sha(certfile),'independent_check':checkfile,'independent_check_sha256':sha(checkfile)})
            accepted.extend({'index':r['index'],'certificates':certfile,'checker_receipt':checkfile} for r in good);closed={r['index'] for r in good};active=[i for i in active if i not in closed]
        if not active:
            stop='all_requested_cases_have_independently_checked_exact_duals';entries.append(entry);save(f'{prefix}-r{n}-receipt.json',entry);print(entry,flush=True);break
        point=f'{prefix}-r{n}-points.jsonl'
        run(['frontier-20261029-plane-functional-joint-dfz-primal-v3.py',point,CLASSES,','.join(map(str,active)),'120',cutfile,cutsha]);pointsha=sha(point)
        pts=[json.loads(l) for l in (ROOT/point).read_text().splitlines()];entry.update({'next_points':point,'next_points_sha256':pointsha,'objective_3Delta_float':{str(r['index']):r['objective_3Delta_float'] for r in pts},'solver_statuses':{str(r['index']):r['status_float'] for r in pts},'elapsed_s':time.monotonic()-t})
        entries.append(entry);save(f'{prefix}-r{n}-receipt.json',entry);print(entry,flush=True)
        if any(not r.get('proposal_available') for r in pts):stop='no_exported_proposal_for_an_active_case';break
    final={'rounds':entries,'accepted_arithmetic_only_unreviewed':accepted,'remaining':active,'stop':stop,'last_points':point,'last_points_sha256':pointsha,'last_cuts':cutfile,'last_cuts_sha256':cutsha,'elapsed_s':time.monotonic()-t,
           'limits':'Only independently checked exact duals are exclusions. Floating objective/point data are proposals; no exact saturation, code witness, global bound, novelty or scientific adoption.'}
    save(f'{prefix}-final.json',final);print('STOP',stop,'remaining',active,flush=True)
if __name__=='__main__':main()
