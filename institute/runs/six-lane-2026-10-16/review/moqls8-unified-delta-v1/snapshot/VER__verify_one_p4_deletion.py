"""Independent traversal check of the observed one-P4 byte filter (no solver).
Build via frozen producer, then use a DIFFERENT line-by-line comparison to
check EVERY retained source clause against the next output clause, and all
four deleted hashes/Q1keep. Check LF-only/no-comments/count/header, all16unit
identities and delivered-formula SHA recipes. Writes a small dated receipt;
never a CNF. This is observed generation evidence NOW, not a claim that the
weakened formula existed at the earlier proof-note freeze.
"""
import gzip
import hashlib
import importlib.util
import io
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'evidence/n8_one_p4_templates_v1/BYTE_FILTER_VERIFICATION_v1.json'
PRODUCER_SHA='61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400'
PREP_SHA='264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18'
MANIFEST_SHA='355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'
WEAK_SHA='374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9'


def sha(b): return hashlib.sha256(b).hexdigest()


def main():
    free=shutil.disk_usage(ROOT).free
    if free<12_200_000_000:
        raise SystemExit('DEFERRED: fresh12.2e9 checker gate failed; do not poll')
    producer=ROOT/'code/n8_one_p4_formula.py'
    if sha(producer.read_bytes())!=PRODUCER_SHA: raise RuntimeError('producer pin')
    spec=importlib.util.spec_from_file_location('producer',producer)
    P=importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
    f,r=P.build()
    prep_raw=(ROOT/'evidence/n8_one_p4_templates_v1/BASE_RECIPE.json').read_bytes()
    manifest_raw=(ROOT/'evidence/n8_one_p4_templates_v1/MANIFEST.json').read_bytes()
    if sha(prep_raw)!=PREP_SHA or sha(manifest_raw)!=MANIFEST_SHA or f.sha!=WEAK_SHA:
        raise RuntimeError('prepared recipe/manifest/result changed')
    d=json.loads(P.DEL.read_bytes()); source=P.BASE.read_bytes()
    if sha(source)!=P.BASE_SHA or b'\r' in source: raise RuntimeError('source SHA/CR')
    src=io.BytesIO(source)
    if src.readline()!=b'p cnf 509915 5740230\n': raise RuntimeError('source header bytes')
    dst=io.BytesIO(f.body); deleted={x['clause_index_zero_based']:x for x in d['delete']}
    keep=d['keep_q1']; matched=removed=0; source_count=0; selected={}
    for i,line in enumerate(src):
        source_count+=1
        if not line.endswith(b' 0\n') or line.startswith(b'c') or line.strip()==b'':
            raise RuntimeError('source not canonical LF-only clause line')
        if i in deleted:
            if sha(line)!=deleted[i]['clause_bytes_sha256']: raise RuntimeError('deleted line hash')
            selected[i]=line; removed+=1
        else:
            if dst.readline()!=line: raise RuntimeError('retained byte/order mismatch at original index%d'%i)
            matched+=1
            if i==keep['clause_index_zero_based']:
                if sha(line)!=keep['clause_bytes_sha256']: raise RuntimeError('Q1 keep hash')
                selected[i]=line
    if dst.read()!=b'' or source_count!=5740230 or matched!=5740226 or removed!=4:
        raise RuntimeError('source/output count or suffix differs')
    if f.nv!=509915 or f.nc!=5740226: raise RuntimeError('output header fields')
    # Independently re-identify all280 flags in the full pinned name table.
    names_path=Path(d['name_table']); nr=names_path.read_bytes()
    if sha(nr)!=d['name_table_sha256']: raise RuntimeError('name table pin')
    wanted={int(t) for line in selected.values() for t in line.split()[:-1]}
    names={v:n for v,n in json.loads(gzip.decompress(nr)) if v in wanted}
    family_verified=0
    for rec in [keep]+d['delete']:
        line=selected[rec['clause_index_zero_based']]; vals=[int(x) for x in line.split()[:-1]]
        ns=[names[v] for v in vals]
        if len(vals)!=56 or any(n[0]!='w3' or n[1]!=rec['square'] or n[2]!=0 for n in ns):
            raise RuntimeError('ALO flag meaning mismatch')
        if {tuple(n[3]) for n in ns}!={(i,j) for i in range(1,8) for j in range(8)}:
            raise RuntimeError('ALO off-row0 domain')
        family_verified+=1
    m=json.loads(manifest_raw); cases=m['cases']
    if len(cases)!=16 or len({x['id'] for x in cases})!=16: raise RuntimeError('case count')
    mapraw=(ROOT/'evidence/gram_dev_v1/GA5L_K5_sb2.map.json').read_bytes()
    if sha(mapraw)!='7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197': raise RuntimeError('g map pin')
    g={}
    for key,v in json.loads(mapraw)['vars'].items():
        n=json.loads(key)
        if n[0]=='g': g[(n[1],tuple(n[2]),tuple(n[3]))]=v
    bound=0
    for x in cases:
        units=[g[(1,(0,c),(i,0))]*(1 if c in S else -1)
               for i,S in enumerate(x['supports_row2to7'],start=2) for c in range(1,8)]
        if units!=x['units'] or len(units)!=42 or x['cnf_sha256']!=f.leaf_sha(units) \
           or x['cnf_clauses']!=5740268 or x['run_required'] is not True:
            raise RuntimeError('16case exact-unit/formula binding')
        bound+=1
    result={'time':datetime.now().astimezone().isoformat(),'script_sha256':sha(Path(__file__).read_bytes()),
        'producer_sha256':PRODUCER_SHA,'prepared_recipe_sha256':PREP_SHA,'manifest_sha256':MANIFEST_SHA,
        'free_before':free,'source_sha256':sha(source),'source_header':'p cnf 509915 5740230\n',
        'source_clauses_checked':source_count,'LF_only_no_comment_clause_lines':True,
        'deleted_clauses_checked':removed,'Q1_retained':True,'retained_clauses_byte_equal_in_order':matched,
        'all_five_ALO_domains_verified':family_verified,'output_header':'p cnf 509915 5740226\n',
        'output_base_sha256':f.sha,'template_header':'p cnf 509915 5740268\n','exact_42unit_cases_bound':bound,
        'all_pass':True,'scope':'observed generation/identity control only; no refutation, no target exclusion'}
    with OUT.open('x') as fp: json.dump(result,fp,indent=1)
    print(json.dumps(result),flush=True)


if __name__=='__main__': main()
