"""Exact four-clause weakening from the frozen unified bridge. No CNF is written.
Read/hash source and deletion manifest once; verify all five pinned ALO lines,
remove only squares2–5, retain Q1 and every other original byte in order, then
adjust only the header count. The bridge was frozen before any call here.
CLI prepares16 recipe entries only; actual solving is separately ordered AFTER
the13 strong-F template runs and uses a separate consumer/ledger.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.cnf'
BASE_SHA='6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
DEL=ROOT/'evidence/UNIFIED_ONE_P4_DELETIONS_v1.json'
DEL_SHA='4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6'
BRIDGE=ROOT/'review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md'
BRIDGE_SHA='c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3'
STRONG=ROOT/'evidence/k5_column_templates_v1/MANIFEST.json'
STRONG_SHA='f77c061947aa64d1107736d27723373ccc9e02633dd099c1a58cf9d77a2c0b71'
OUT=ROOT/'evidence/n8_one_p4_templates_v1'


def sha(b): return hashlib.sha256(b).hexdigest()


class Formula:
    def __init__(self,nv,nc,body):
        self.nv,self.nc,self.body=nv,nc,body
        h=hashlib.sha256(('p cnf %d %d\n'%(nv,nc)).encode()); h.update(body)
        self.sha=h.hexdigest(); self._prefix={}
    def leaf_sha(self,units):
        k=len(units)
        if k not in self._prefix:
            h=hashlib.sha256(('p cnf %d %d\n'%(self.nv,self.nc+k)).encode()); h.update(self.body)
            self._prefix[k]=h
        h=self._prefix[k].copy(); h.update(''.join('%d 0\n'%x for x in units).encode()); return h.hexdigest()


def build():
    dr=DEL.read_bytes(); br=BRIDGE.read_bytes()
    if sha(dr)!=DEL_SHA or sha(br)!=BRIDGE_SHA: raise RuntimeError('frozen deletion/bridge pin mismatch')
    d=json.loads(dr); raw=BASE.read_bytes()
    if sha(raw)!=BASE_SHA or d['source_base_sha256']!=BASE_SHA: raise RuntimeError('source base pin mismatch')
    end_header=raw.index(b'\n')+1
    head=raw[:end_header].split()
    if head!=[b'p',b'cnf',b'509915',b'5740230']: raise RuntimeError('source header mismatch')
    deletes={x['clause_index_zero_based']:x for x in d['delete']}
    if sorted(deletes)!=[5735297,5736866,5738435,5740004] or {x['square'] for x in deletes.values()}!={2,3,4,5}:
        raise RuntimeError('not exactly the authorised four ALO clauses')
    keep=d['keep_q1']; verify=dict(deletes); verify[keep['clause_index_zero_based']]=keep
    pos=end_header; ranges=[]; checked=[]
    for i in range(5740230):
        end=raw.find(b'\n',pos)
        if end<0: raise RuntimeError('unterminated source clause')
        end+=1
        if i in verify:
            line=memoryview(raw)[pos:end]; rec=verify[i]
            if sha(line)!=rec['clause_bytes_sha256']: raise RuntimeError('pinned ALO line differs')
            vals=bytes(line).split()
            if vals[-1]!=b'0' or len(vals)!=57 or any(int(x)<=0 for x in vals[:-1]):
                raise RuntimeError('ALO not56 positive flags')
            checked.append({'index':i,'square':rec['square'],'sha256':sha(line),'operation':'delete' if i in deletes else 'keep'})
        if i in deletes: ranges.append((pos,end))
        pos=end
    if pos!=len(raw) or len(checked)!=5 or len(ranges)!=4: raise RuntimeError('source count or deletion verification incomplete')
    segments=[]; pos=end_header
    for start,end in ranges:
        segments.append(memoryview(raw)[pos:start]); pos=end
    segments.append(memoryview(raw)[pos:])
    body=b''.join(segments)
    f=Formula(509915,5740226,body)
    recipe={'source_base_sha256':BASE_SHA,'deletion_manifest_sha256':DEL_SHA,'bridge_sha256':BRIDGE_SHA,
            'source_vars':509915,'source_clauses':5740230,'source_bytes':len(raw),
            'weakened_vars':f.nv,'weakened_clauses':f.nc,'weakened_base_sha256':f.sha,
            'weakened_body_sha256':sha(body),'weakened_body_bytes':len(body),'removed':checked,
            'deleted_bytes':sum(b-a for a,b in ranges),'all_other_bytes_kept_in_order':True,
            'source_header_count_only_change':True,'CNF_retained':False,'H3_used':False}
    return f,recipe


def main():
    free=shutil.disk_usage(ROOT).free
    if free<12_200_000_000: raise SystemExit('DEFERRED: fresh12.2e9 launch gate failed; no weakened formula generated')
    sr=STRONG.read_bytes()
    if sha(sr)!=STRONG_SHA: raise RuntimeError('strong-template source manifest changed')
    s=json.loads(sr)
    f,recipe=build()
    recipe['free_before_preparation']=free
    recipe['launch_floor']=12_200_000_000
    recipe['projected_retained_growth_max_bytes']=100_000
    OUT.mkdir(exist_ok=False)
    cases=[]
    for x in s['cases']:
        y=dict(x); y['old_strong_leaf_cnf_sha256']=x['cnf_sha256']
        y['cnf_sha256']=f.leaf_sha(x['units']); y['cnf_clauses']=f.nc+42
        y['run_required']=True; y['excluded_by_imported_c112']=False
        cases.append(y)
    expected=[p+'-'+b for p in('P0','P1') for b in('B1','B2','B3','B4','B5','B6')]+['P2-C1','P2-C2','P2-C3','P2-C4']
    if [x['id'] for x in cases]!=expected or len(cases)!=16: raise RuntimeError('must run all16, includingc112')
    with(OUT/'BASE_RECIPE.json').open('x') as fp: json.dump(recipe,fp,indent=1)
    m={'schema':'n8-one-p4-template-manifest/1','producer_sha256':sha(Path(__file__).read_bytes()),
       'source_base_cnf_sha256':BASE_SHA,'base_cnf_sha256':f.sha,'base_vars':f.nv,'base_clauses':f.nc,
       'bridge_note_sha256':BRIDGE_SHA,'deletion_manifest_sha256':DEL_SHA,
       'strong_template_manifest_sha256':STRONG_SHA,'template_proof_sha256':s['proof_note_sha256'],
       'finite_orbit_control':s['finite_orbit_control'],'cases':cases,'run_cases':expected,
       'run_all_c112_templates':True,'H3_used':False,
       'claim':'conditional genuine-counterexample cover; no n8 exclusion before reviews and parent proof replay'}
    with(OUT/'MANIFEST.json').open('x') as fp: json.dump(m,fp,indent=1)
    print(json.dumps({'weakened_base_sha256':f.sha,'base_clauses':f.nc,'cases':16,'leaf_clauses':f.nc+42,
                      'removed':recipe['removed'],'CNF_retained':False}),flush=True)


if __name__=='__main__': main()
