# Parent independent streaming n8 F_one/16-leaf binding. No lane producer imports, no CNF copies.
import json, gzip, hashlib, re
from pathlib import Path
from datetime import datetime
ROOT=Path('/Users/jinleic/repos/aifours')
L=ROOT/'physics/evidence/six-lane-20261016/moqls8-problem16'
R=ROOT/'institute/runs/six-lane-2026-10-16/review'
PINS={
 'evidence/UNIFIED_ONE_P4_DELETIONS_v1.json':'4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6',
 'evidence/n8_one_p4_templates_v1/MANIFEST.json':'355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74',
 'evidence/n8_one_p4_templates_v1/BASE_RECIPE.json':'264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18',
 'review/K5_COLUMN0_TEMPLATE_COVER.r1.md':'1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a',
 'evidence/gram_dev_v1/GA5L_K5_sb2.map.json':'7b4dd597894a7bbe39374f314bdb2016995216aa07bc03d7aad4a09f8e54b197',
 'code/gram_a.py':'bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a'
}
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    raw={k:(L/k).read_bytes() for k in PINS}
    for k,v in PINS.items():
        if sha(raw[k])!=v:raise ValueError('pin '+k)
    d=json.loads(raw['evidence/UNIFIED_ONE_P4_DELETIONS_v1.json'])
    m=json.loads(raw['evidence/n8_one_p4_templates_v1/MANIFEST.json'])
    recipe=json.loads(raw['evidence/n8_one_p4_templates_v1/BASE_RECIPE.json'])
    source=L/d['source_base'];full=hashlib.sha256();body=hashlib.sha256()
    weak_header=b'p cnf 509915 5740226\n';leaf_header=b'p cnf 509915 5740268\n'
    weak=hashlib.sha256(weak_header);leaf=hashlib.sha256(leaf_header)
    deleted={r['clause_index_zero_based']:r for r in d['delete']}
    keep=d['keep_q1'];selected={};nc=retained=removed=body_bytes=deleted_bytes=0
    with source.open('rb') as f:
        header=f.readline();full.update(header)
        if header!=b'p cnf 509915 5740230\n':raise ValueError('source header')
        for i,line in enumerate(f):
            full.update(line);nc+=1
            if not line.endswith(b' 0\n') or b'\r' in line or line.startswith(b'c'):raise ValueError('clause format')
            if i in deleted:
                if sha(line)!=deleted[i]['clause_bytes_sha256']:raise ValueError('deleted clause')
                selected[i]=line;removed+=1;deleted_bytes+=len(line)
            else:
                body.update(line);weak.update(line);leaf.update(line);retained+=1;body_bytes+=len(line)
                if i==keep['clause_index_zero_based']:
                    if sha(line)!=keep['clause_bytes_sha256']:raise ValueError('kept clause')
                    selected[i]=line
    if full.hexdigest()!=d['source_base_sha256'] or full.hexdigest()!=m['source_base_cnf_sha256']:raise ValueError('source CNF hash')
    if (nc,retained,removed)!=(5740230,5740226,4):raise ValueError('counts')
    if weak.hexdigest()!=m['base_cnf_sha256'] or weak.hexdigest()!=recipe['weakened_base_sha256']:raise ValueError('weak hash')
    if body.hexdigest()!=recipe['weakened_body_sha256'] or body_bytes!=recipe['weakened_body_bytes'] or deleted_bytes!=1576:raise ValueError('body recipe')
    names_raw=Path(d['name_table']).read_bytes()
    if sha(names_raw)!=d['name_table_sha256']:raise ValueError('name table hash')
    allnames=json.loads(gzip.decompress(names_raw));wanted={int(x) for line in selected.values() for x in line.split()[:-1]}
    names={v:n for v,n in allnames if v in wanted};del allnames
    if len(names)!=280:raise ValueError('name subset')
    for rec in [keep]+d['delete']:
        vals=list(map(int,selected[rec['clause_index_zero_based']].split()[:-1]))
        expected_names={('w3',rec['square'],0,(i,j)) for i in range(1,8) for j in range(8)}
        observed={(names[v][0],names[v][1],names[v][2],tuple(names[v][3])) for v in vals}
        if len(vals)!=56 or len(set(vals))!=56 or min(vals)<=0 or observed!=expected_names:raise ValueError('ALO domain')
    # Parse the mathematical table itself, not the producer's strong-template manifest.
    text=raw['review/K5_COLUMN0_TEMPLATE_COVER.r1.md'].decode();B={};C={}
    for line in text.split('\n'):
        if re.match(r'^\| [BC][1-6]=',line):
            fields=line.split('|');key=fields[1].strip().split('=')[0]
            supports=[[int(x) for x in t.strip()] for t in fields[2].strip().split(';')]
            if key.startswith('B'):B[key]=supports
            else:C[key]=supports
    if len(B)!=6 or len(C)!=4:raise ValueError('table parsed count')
    lists={}
    for pre,tail in [('P0',[[1,2,3],[1,2,3]]),('P1',[[2,3],[1,2,3]])]:
        for key,vals in B.items():lists[pre+'-'+key]=vals+tail
    for key,vals in C.items():lists['P2-'+key]=vals
    gmap=json.loads(raw['evidence/gram_dev_v1/GA5L_K5_sb2.map.json'])
    lookup={}
    for key,v in gmap['vars'].items():
        n=json.loads(key)
        if n[0]=='g':lookup[(n[1],tuple(n[2]),tuple(n[3]))]=v
    if len(lookup)!=7840 or gmap['meta']['cnf_sha256']!=full.hexdigest() or gmap['meta']['script_sha256']!=PINS['code/gram_a.py']:raise ValueError('map binding')
    if len(m['cases'])!=16 or set(lists)!={x['id'] for x in m['cases']}:raise ValueError('manifest IDs')
    leaves=[]
    for case in m['cases']:
        supports=lists[case['id']]
        if supports!=case['supports_row2to7']:raise ValueError('support table identity '+case['id'])
        units=[]
        for i,S in enumerate(supports,2):
            for c in range(1,8):
                v=lookup[(1,(0,c),(i,0))]
                if v!=49*c+7*i-6:raise ValueError('map allocation')
                units.append(v if c in S else -v)
        if units!=case['units'] or len(units)!=42:raise ValueError('unit map')
        hh=leaf.copy();hh.update(b''.join(('%d 0\n'%u).encode('ascii') for u in units))
        if hh.hexdigest()!=case['cnf_sha256'] or case['cnf_clauses']!=5740268 or case['cnf_vars']!=509915 or not case['run_required'] or case['excluded_by_imported_c112']:raise ValueError('leaf identity')
        wrong=leaf.copy();wrong.update(b''.join(('%d 0\n'%u).encode('ascii') for u in [-units[0]]+units[1:]))
        if wrong.hexdigest()==case['cnf_sha256']:raise ValueError('mutation not detected')
        leaves.append({'id':case['id'],'cnf_sha256':hh.hexdigest(),'template_table_equal':True,'units_equal':True,'unit_flip_detected':True})
    binding=R/'moqls8-encoder-binding-v1/binding-result.v2.json'
    binding_raw=binding.read_bytes()
    if sha(binding_raw)!='dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112':raise ValueError('previous encoder binding')
    return {'at':datetime.now().astimezone().isoformat(timespec='seconds'),'status':'PASS','scope':'Independent parent byte/header/leaf SHA and support/map/name identity; no SAT/refutation or target verdict.',
        'source_cnf_sha256':full.hexdigest(),'weak_base_sha256':weak.hexdigest(),'body_sha256':body.hexdigest(),
        'source_clauses':nc,'retained_clauses':retained,'deleted_clauses':removed,'deleted_bytes':deleted_bytes,
        'all_five_ALO_domains':True,'template_lists_equal':16,'leaves':leaves,'old_encoder_binding_reused_sha256':sha(binding_raw),
        'negative_controls':'For each of16 leaves a first-unit sign flip changes the CNF hash. These are binding controls, not proof mutations.'}
