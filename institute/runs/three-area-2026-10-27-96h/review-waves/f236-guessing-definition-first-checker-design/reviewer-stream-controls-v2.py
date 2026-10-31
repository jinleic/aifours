#!/usr/bin/env python3
"""Small self-authored streaming and gate controls. Retains all fixtures."""
import copy
import hashlib
import importlib.util
import itertools
import json
import os
import signal
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CHECKER=ROOT/'reviewer-checker-v2.py'
OUT=ROOT/'stream-controls-v2f'
sys.dont_write_bytecode=True

def sha(b): return hashlib.sha256(b).hexdigest()
def enc(obj): return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
def clock(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
def create(p,b):
    with open(p,'xb') as f: f.write(b); f.flush(); os.fsync(f.fileno())
def require(v,msg):
    if not v: raise RuntimeError(msg)
def vector(terms):
    d={}
    for k,v in terms:
        if k:
            d[k]=d.get(k,0)+v
            if not d[k]: del d[k]
    return [[k,d[k]] for k in sorted(d)]
def make_row(name,relation,mul,terms):
    return {'name':name,'relation':relation,'multiplier':str(mul),'image_vectors':[vector(terms)]}

TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
NG={1:{2,3,4,5,6,7},2:{1,3,7,9,10},3:{1,2,4,8,9},4:{1,3,5,8,10},5:{1,4,6,9,10},
    6:{1,5,7,8,9},7:{1,2,6,8,10},8:{3,4,6,7,9,10},9:{2,3,5,6,8},10:{2,4,5,7,8}}
PROPER=[[1,2,3,4,5,6,7,8,9,10],[1,2,7,6,5,4,3,8,10,9],
        [1,5,4,3,2,7,6,8,10,9],[1,5,6,7,2,3,4,8,9,10],
        [8,9,3,4,10,7,6,1,2,5],[8,9,6,7,10,4,3,1,5,2],
        [8,10,4,3,9,6,7,1,5,2],[8,10,7,6,9,3,4,1,2,5]]
FACTOR=[PROPER[i] for i in (0,2,4,6)]

def factor_map(action):
    lookup={frozenset(t):i for i,t in enumerate(TRI)}
    return [lookup[frozenset(action[v-1] for v in t)] for t in TRI]
def transform_plane(plane,action):
    f=factor_map(action)
    return sorted(sum(1<<f[i] for i in range(10) if x & (1<<i)) for x in plane)
def graph_meta():
    return {'factor_preserving_vertex_actions':FACTOR,'factor_actions_zero_based':[factor_map(a) for a in FACTOR],
            'proper_subgraph_graph_actions_order8':PROPER,
            'proper_delete_1_color':{'2':0,'3':1,'4':2,'5':0,'6':1,'7':2,'8':0,'9':2,'10':1},
            'visibility_generators':[[6],[7],[2,5],[9,10],[1,2,10],[1,5,9],[5,8,9],[2,8,10]]}

def proper_certificate():
    active=list(range(2,11)); coloring=[0,1,2,0,1,2,0,2,1]
    groups=[[i for i,c in enumerate(coloring) if c==j] for j in range(3)]
    masks=[sum(1<<i for i in group) for group in groups]; rows=[]
    for group in groups:
        prefix=0
        for i in group:
            if prefix:
                x=1<<i; rows.append(make_row(['set-cmi',x,prefix,0],'ge',2,[(x,1),(prefix,1),(x|prefix,-1)]))
            prefix |= 1<<i
    for a,b in itertools.combinations(masks,2):
        rows.append(make_row(['set-cmi',a,b,0],'ge',1,[(a,1),(b,1),(a|b,-1)]))
    for c,part in enumerate(masks):
        rows.append(make_row(['proper-color-decoder',c],'eq',-1,[(511,1),(511^part,-1)]))
    return {'certificate_id':'D1-synthetic','source_member':'sources/fixture.json','source_index':0,
            'coordinate_system':{'type':'entropy_bitmask','variables':active,'nonempty_coordinates':511},
            'target_vector':[[511,'-3']]+[[1<<i,'2'] for i in range(9)],'target_relation':'ge',
            'action_count':1,'actions':[list(range(9))],
            'scope':{'missing_vertex':1,'active_vertices':active,'scale':1,'proper_coloring':coloring},'rows':rows}

def roster_row(plane):
    selected=plane[0]|plane[1]; visible=0
    for v in range(1,11):
        inc=sum(1<<i for i,t in enumerate(TRI) if v in t)
        if all(d & inc for d in plane): visible |= 1<<(v-1)
    return {'plane':plane,'J':selected,'W':visible,'category':'noncover','proof_id':'D1-synthetic',
            'missing_vertex':1,'representative_missing_vertex':1,'proper_graph_action':0}

UNIVERSE=[[8,16,24],[8,32,40],[8,48,56],[16,32,48],[16,40,56],[24,32,56],[24,40,48]]

def fixture(label,variant=None):
    rec=proper_certificate(); planes=[roster_row(p) for p in UNIVERSE]; graph=graph_meta()
    source=b'{}\n'; extras={}; remove=None; wrong_member_hash=None
    if variant=='wrong-identity-index': rec['source_index']=1
    if variant=='wrong-sign': rec['rows'][0]['multiplier']='-2'
    if variant=='wrong-image': rec['rows'][0]['image_vectors'][0][0][1]=2
    if variant=='wrong-plane-J': planes[0]['J'] ^= 1
    if variant=='wrong-plane-W': planes[0]['W'] ^= 1
    if variant=='wrong-category': planes[0]['category']='full_visibility'
    if variant=='wrong-transport': planes[0]['missing_vertex']=2
    if variant=='wrong-proof': planes[0]['proof_id']='undeclared'
    if variant=='missing-plane': planes.pop()
    if variant=='same-count-wrong-plane': planes[-1]=roster_row([8,64,72])
    if variant=='duplicate-plane': planes[-1]=copy.deepcopy(planes[0])
    if variant=='extra-member': extras['data/unlisted.json']=b'{}\n'
    if variant=='missing-member': remove='sources/fixture.json'
    if variant=='wrong-factor-table': graph['factor_actions_zero_based'][0][0]=1
    coeff=enc(rec); index={'certificate_id':'D1-synthetic','source_member':'sources/fixture.json','source_index':0,
                         'rows':12,'coordinate_system':rec['coordinate_system'],'scope':rec['scope']}
    blobs={'coefficients/synthetic.jsonl':coeff,'data/graph.json':enc(graph),'data/class.json':enc([]),
           'data/four.jsonl':b'','data/planes.jsonl':b''.join(enc(p) for p in planes),
           'sources/fixture.json':source}
    table=[]
    for name,b in blobs.items():
        item={'member':name,'bytes':len(b),'sha256':sha(b),'role':'synthetic'}
        if name=='coefficients/synthetic.jsonl': item['records']=1
        if name=='data/four.jsonl': item['records']=0
        if name=='data/planes.jsonl': item['records']=len(planes)
        if variant=='wrong-coefficient-pin' and name=='coefficients/synthetic.jsonl': item['sha256']='0'*64
        table.append(item)
    if variant=='wrong-source-pin': blobs['sources/fixture.json']=b'[]\n'
    if remove: del blobs[remove]
    packet={'members':table,'coefficient_certificate_index':[index],
            'literal_coverage_data':{'category_records':{'noncover':7,'four_factor':0,'full_visibility':0,
                                                        'mixed_visibility':0,'residual_functional':0}}}
    packet_bytes=enc(packet); path=OUT/(label+'.zip')
    with open(path,'xb') as f:
        with zipfile.ZipFile(f,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for name,b in blobs.items(): z.writestr(name,b)
            for name,b in extras.items(): z.writestr(name,b)
            z.writestr('packet-manifest.json',packet_bytes)
        f.flush(); os.fsync(f.fileno())
    raw=path.read_bytes()
    with zipfile.ZipFile(path) as z:
        infos=z.infolist(); uncompressed=sum(x.file_size for x in infos)
    contract={'sha256':sha(raw),'bytes':len(raw),'members':len(infos),'uncompressed':uncompressed,
              'packet_sha256':sha(packet_bytes),'certificates':1,'rows':12,'planes':7,'four_cases':0,'classes':0,
              'coefficient_members':('coefficients/synthetic.jsonl',),'graph_member':'data/graph.json',
              'class_member':'data/class.json','four_member':'data/four.jsonl','plane_member':'data/planes.jsonl',
              'fixture_universe':tuple(tuple(x) for x in UNIVERSE)}
    return path,contract

def outcome(module,fn,expected,reason=None):
    try:
        value=fn(); good=reason is None and (expected is None or value==expected)
        return {'met':good,'actual':str(value)[:700],'actual_reason':None,'expected_reason':reason}
    except Exception as e:
        return {'met':reason is not None and str(e)==reason,'actual_exception':type(e).__name__,
                'actual_reason':str(e),'expected_reason':reason}

def independent_masks(plane):
    j=[i for i in range(10) if (plane[0]|plane[1]) & (1<<i)]; result=set()
    for direction in [0]+plane:
        opts=[[b for b in range(8) if b.bit_count()%2==((direction>>i)&1)] for i in j]
        for choices in itertools.product(*opts):
            active=set()
            for factor,bits in zip(j,choices): active.update(TRI[factor][k] for k in range(3) if bits&(1<<k))
            if active and all(NG[v]&active for v in active): result.add(sum(1<<(v-1) for v in active))
    return sorted(result)

def class_fixture():
    base=[1,2,3]; colors=[0,1,None,None,None,None,None,None,None,None]
    cert={'certificate_id':'R-synthetic','source_member':'sources/functional.json','source_index':0,
          'coordinate_system':{'type':'functional_branch'},
          'scope':{'class_id_zero_based':0,'coloring':'01--------','colors':colors}}
    item={'class_id_zero_based':0,'coloring':'01--------','base_plane':base,
          'proof':{'certificate_id':'R-synthetic','source':'functional.json','source_certificate_index':0,'historical_declared_id':None},
          'action_images':[{'plane':transform_plane(base,a),'source_to_target_action':i} for i,a in enumerate(FACTOR)]}
    return item,{'R-synthetic':cert},{'R-synthetic':cert}

def cli_controls():
    cases=[]; started=clock()
    record=proper_certificate(); raw=enc(record)
    binding={k:record[k] for k in ('certificate_id','source_member','source_index','coordinate_system','scope')}
    binding['record_sha256']=sha(raw); bb=enc(binding)
    rp=OUT/'cli-record.json';bp=OUT/'cli-binding.json';create(rp,raw);create(bp,bb)
    sentinel=OUT/'cli-existing.json';create(sentinel,b'owner-sentinel\n')
    argv=[sys.executable,'-B',str(CHECKER),'identity','--record',str(rp),'--record-sha256',sha(raw),
          '--binding',str(bp),'--binding-sha256',sha(bb),'--output',str(sentinel)]
    done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
    cases.append({'name':'exclusive-existing','start':started,'end':clock(),'argv':argv,'actual_exit':done.returncode,
                  'output_sha256':sha(sentinel.read_bytes()),'stderr':done.stderr[-400:],
                  'met':done.returncode==73 and sentinel.read_bytes()==b'owner-sentinel\n' and 'OUTPUT_EXCLUSIVE_FAILED' in done.stderr})
    for label,raw_bad,reason in [('duplicate-json',b'{"x":1,"x":2}\n','DUPLICATE_JSON_KEY:x'),
                                 ('json-float',b'{"x":0.5}\n','FLOAT_OR_NONFINITE_FORBIDDEN'),
                                 ('json-nan',b'{"x":NaN}\n','FLOAT_OR_NONFINITE_FORBIDDEN')]:
        t=clock(); inp=OUT/('cli-'+label+'-record.json'); out=OUT/('cli-'+label+'-output.json');create(inp,raw_bad)
        argv=[sys.executable,'-B',str(CHECKER),'identity','--record',str(inp),'--record-sha256',sha(raw_bad),'--output',str(out)]
        done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
        result=json.loads(out.read_bytes()) if out.exists() else {}
        cases.append({'name':label,'start':t,'end':clock(),'argv':argv,'actual_exit':done.returncode,
                      'actual_status':result.get('status'),'actual_reason':result.get('reason'),
                      'record_sha256':sha(raw_bad),'output_sha256':sha(out.read_bytes()) if out.exists() else None,
                      'met':done.returncode==2 and result.get('status')=='REJECT' and result.get('reason')==reason})
    capout=OUT/'cli-archive-cap-output.json';t=clock()
    argv=[sys.executable,'-B',str(CHECKER),'archive','--archive',str(OUT/'never-opened.zip'),'--output',str(capout)]
    done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
    result=json.loads(capout.read_bytes()) if capout.exists() else {}
    cases.append({'name':'archive-default-cap','start':t,'end':clock(),'argv':argv,'actual_exit':done.returncode,
                  'actual_status':result.get('status'),'actual_reason':result.get('reason'),
                  'output_sha256':sha(capout.read_bytes()) if capout.exists() else None,
                  'met':done.returncode==3 and result.get('status')=='UNKNOWN' and result.get('reason')=='ARCHIVE_CERTIFICATE_CAP'})
    big=copy.deepcopy(record);big['rows']=record['rows']*3000; bigraw=enc(big)
    require(len(bigraw)<8*1024*1024,'interrupt-fixture-size')
    bigbinding={k:big[k] for k in ('certificate_id','source_member','source_index','coordinate_system','scope')}
    bigbinding['record_sha256']=sha(bigraw);bigbb=enc(bigbinding)
    br=OUT/'cli-interrupt-record.json';bs=OUT/'cli-interrupt-binding.json';bo=OUT/'cli-interrupt-output.json'
    t=clock();create(br,bigraw);create(bs,bigbb)
    argv=[sys.executable,'-B',str(CHECKER),'identity','--record',str(br),'--record-sha256',sha(bigraw),
          '--binding',str(bs),'--binding-sha256',sha(bigbb),'--output',str(bo),'--max-items','50000','--time-limit-ms','20000']
    child=subprocess.Popen(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    time.sleep(0.12);sent=child.poll() is None
    if sent: os.kill(child.pid,signal.SIGINT)
    stdout,stderr=child.communicate(timeout=30)
    result=json.loads(bo.read_bytes()) if bo.exists() else {}
    cases.append({'name':'cooperative-interrupt','start':t,'end':clock(),'argv':argv,'signal_sent':sent,
                  'actual_exit':child.returncode,'actual_status':result.get('status'),'actual_reason':result.get('reason'),
                  'record_sha256':sha(bigraw),'output_sha256':sha(bo.read_bytes()) if bo.exists() else None,'stderr':stderr[-400:],
                  'met':sent and child.returncode==3 and result.get('status')=='UNKNOWN' and str(result.get('reason')).startswith('INTERRUPTED_SIGNAL_2')})
    return cases


def main():
    start=clock(); mono=time.monotonic(); os.mkdir(OUT)
    csha=sha(CHECKER.read_bytes()); ssha=sha(Path(__file__).read_bytes())
    spec=importlib.util.spec_from_file_location('own_v2_checker',CHECKER); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    m.DEADLINE=time.monotonic()+110
    cases=[]; fixtures={}
    specifications=[('baseline',None,None),('extra-member','extra-member','ARCHIVE_MEMBER_SET'),
        ('missing-member','missing-member','ARCHIVE_MEMBER_SET'),
        ('wrong-source-pin','wrong-source-pin','INDEXED_SOURCE_PIN_MISMATCH:sources/fixture.json'),
        ('wrong-coefficient-pin','wrong-coefficient-pin','MEMBER_PIN_MISMATCH:coefficients/synthetic.jsonl'),
        ('wrong-identity-index','wrong-identity-index','SOURCE_BINDING_MISMATCH:source_index'),
        ('wrong-image','wrong-image','IMAGE_VECTOR_MISMATCH:D1-synthetic:row=0:action=0'),
        ('wrong-sign','wrong-sign','ROW_SIGN'),('wrong-plane-J','wrong-plane-J','PLANE_FACTOR_MASK_MISMATCH'),
        ('wrong-plane-W','wrong-plane-W','PLANE_VISIBILITY_MASK_MISMATCH'),
        ('wrong-category','wrong-category','PLANE_CATEGORY_MISMATCH'),
        ('wrong-transport','wrong-transport','NONCOVER_TRANSPORT'),
        ('wrong-proof','wrong-proof','NONCOVER_PROOF_BINDING'),
        ('missing-plane','missing-plane','PLANE_UNIVERSE_SET_MISMATCH'),
        ('same-count-wrong-plane','same-count-wrong-plane','PLANE_UNIVERSE_SET_MISMATCH'),
        ('duplicate-plane','duplicate-plane','DUPLICATE_PLANE'),
        ('wrong-factor-table','wrong-factor-table','FACTOR_IMAGE_TABLE_MISMATCH')]
    for label,variant,reason in specifications:
        t=clock(); path,contract=fixture(label,variant); fixtures[label]=(path,contract)
        result=outcome(m,lambda p=path,c=contract:m.verify_archive(p,c,1,12,7),None,reason)
        result.update({'name':label,'start':t,'end':clock(),'fixture':str(path),'fixture_sha256':sha(path.read_bytes())})
        if label=='baseline' and result['actual_reason'] is None:
            result['met']='\'planes\': 7' in result.get('actual','') and '\'certificates\': 1' in result.get('actual','')
        cases.append(result)
    basepath,basecontract=fixtures['baseline']; wrong=copy.deepcopy(basecontract); wrong['sha256']='0'*64
    for label,fun,reason in [('wrong-archive-sha',lambda:m.verify_archive(basepath,wrong,1,12,7),'ARCHIVE_PIN_MISMATCH'),
                             ('certificate-cap',lambda:m.verify_archive(basepath,basecontract,0,12,7),'ARCHIVE_CERTIFICATE_CAP'),
                             ('row-cap',lambda:m.verify_archive(basepath,basecontract,1,11,7),'ARCHIVE_ROW_CAP'),
                             ('plane-cap',lambda:m.verify_archive(basepath,basecontract,1,12,6),'ARCHIVE_PLANE_CAP')]:
        result=outcome(m,fun,None,reason);result['name']=label;cases.append(result)
    scope={'colors':[0,1,None,None,None,None,None,None,None,None]}; system={'type':'functional_branch'}
    expected_gate={5115:3,1:17,6:-2,11:-2,21:-2,41:-2,81:-2,161:-2,321:-2,641:-2,1281:-2,2561:-2}
    direct=[]
    def add_direct(name,fn,expected=None,reason=None):
        item=outcome(m,fn,expected,reason); item['name']=name; direct.append(item)
    add_direct('gate-full-state',lambda:m.row_vector(['gate',1],system,scope),(expected_gate,'le'))
    add_direct('gate-wrong-branch',lambda:m.row_vector(['gate',2],system,scope),reason='GATE_BRANCH_NOT_FULL_STATE')
    add_direct('gate-boolean-branch',lambda:m.row_vector(['gate',True],system,scope),reason='GATE_BRANCH_NOT_FULL_STATE')
    add_direct('unknown-gate-descriptor',lambda:m.row_vector(['other-gate',1],system,scope),reason='UNSPECIFIED_FUNCTIONAL_DESCRIPTOR:other-gate')
    add_direct('data-processing-ambiguous',lambda:m.row_vector(['data-processing',5,2],system,scope),
               reason='AMBIGUOUS_DATA_PROCESSING_DESCRIPTOR')
    entropy_scope=scope|{'data_processing_semantics':'entropy_monotonicity'}
    mutual_scope=scope|{'data_processing_semantics':'mutual_information'}
    add_direct('data-processing-explicit-entropy',lambda:m.row_vector(['data-processing',5,2],system,entropy_scope),
               ({27:1,26:-1},'le'))
    add_direct('data-processing-explicit-mutual',lambda:m.row_vector(['data-processing',5,2],system,mutual_scope),
               ({26:1,27:-1,2:1,1:-1},'le'))
    item,index,verified=class_fixture(); factor_actions=tuple(tuple(x) for x in FACTOR)
    mixed_cert={'coordinate_system':{'type':'entropy_bitmask','variables':list(range(1,11))+['S']},
                'scope':{'factors':[4,5],'visibility_required':[2]}}
    add_direct('mixed-applicability',lambda:0 in m.certificate_actions(mixed_cert,(8,16,24),factor_actions),True)
    bad_mixed=copy.deepcopy(mixed_cert); bad_mixed['scope']['visibility_required']=[1]
    add_direct('mixed-invisible',lambda:m.certificate_actions(bad_mixed,(8,16,24),factor_actions),set())
    full_cert={'coordinate_system':mixed_cert['coordinate_system'],'scope':{'visibility_required':[2]}}
    add_direct('full-visibility-applicability',lambda:0 in m.certificate_actions(full_cert,(8,16,24),factor_actions),True)
    add_direct('action-inverse-positive',lambda:m.action_constraint({'certificate_to_client_action':0,
               'client_to_certificate_action':0},{0},factor_actions))
    add_direct('action-inverse-negative',lambda:m.action_constraint({'certificate_to_client_action':0,
               'client_to_certificate_action':1},{0},factor_actions),reason='TRANSPORT_ACTIONS_NOT_INVERSES')
    expected_map={tuple(x['plane']):(0,'R-synthetic') for x in item['action_images']}
    add_direct('class-map-positive',lambda:m.build_class_map([item],index,verified,factor_actions,1),expected_map)
    bad=copy.deepcopy(item);bad['proof']['source_certificate_index']=1
    add_direct('class-source-substitution',lambda:m.build_class_map([bad],index,verified,factor_actions,1),reason='CLASS_SOURCE_INDEX_BINDING')
    bad_color=copy.deepcopy(item);bad_color['coloring']='10--------'
    add_direct('class-color-substitution',lambda:m.build_class_map([bad_color],index,verified,factor_actions,1),reason='CLASS_CERTIFICATE_COLOR_BINDING')
    bad_action=copy.deepcopy(item);bad_action['action_images'][0]['plane']=[1,4,5]
    add_direct('class-action-image',lambda:m.build_class_map([bad_action],index,verified,factor_actions,1),reason='CLASS_ACTION_IMAGE_MISMATCH')
    plane=[5,96,101]; masks=independent_masks(plane)
    four={'case_id_zero_based':0,'global_plane':plane,'factors':[1,3,6,7],'syndrome_plane':[3,12,15],
          'allowed_masks':masks,'color':[0,1,2,0,1,1,2,1,0,2]}
    add_direct('four-factor-color',lambda:m.verify_four_case(four,{},factor_actions),(0,tuple(plane),'color',set()))
    bad_four=copy.deepcopy(four);bad_four['syndrome_plane']=[1,2,3]
    add_direct('four-factor-local-plane',lambda:m.verify_four_case(bad_four,{},factor_actions),reason='FOUR_CASE_LOCAL_PLANE')
    bad_masks=copy.deepcopy(four);bad_masks['allowed_masks'][-1]=next(x for x in range(1,1024) if x not in set(masks))
    add_direct('four-factor-mask-set',lambda:m.verify_four_case(bad_masks,{},factor_actions),reason='ALLOWED_MASK_SET_MISMATCH')
    # Mutate one verifier protection at a time; execute only these own fixtures.
    source=CHECKER.read_text(); mutations=[
      ('archive-pin',"need(actual_sha==contract['sha256'] and actual_bytes==contract['bytes'],'ARCHIVE_PIN_MISMATCH')",
       "need(True,'ARCHIVE_PIN_MISMATCH')",'wrong-archive-sha'),
      ('member-set',"need(set(names)==set(table)|{'packet-manifest.json'}, 'ARCHIVE_MEMBER_SET')",
       "need(True, 'ARCHIVE_MEMBER_SET')",'extra-member'),
      ('source-binding',"need(record[k]==binding[k], 'SOURCE_BINDING_MISMATCH:' + k)",
       "need(True, 'SOURCE_BINDING_MISMATCH:' + k)",'wrong-identity-index'),
      ('image-vector',"need(parse_vector(advertised,max_id,False)==actual,\n                 'IMAGE_VECTOR_MISMATCH:'+record['certificate_id']+':row='+str(row_index)+':action='+str(action_index))",
       "need(True,'IMAGE_VECTOR_MISMATCH')",'wrong-image'),
      ('ambiguous-selection',"choice=scope.get('data_processing_semantics')",
       "choice=scope.get('data_processing_semantics','entropy_monotonicity')",'data-processing-ambiguous'),
      ('transport',"need(missing not in covered and proper_actions[aid][rep-1]==missing,'NONCOVER_TRANSPORT')",
       "need(True,'NONCOVER_TRANSPORT')",'wrong-transport'),
      ('universe-set',"need(actual==universe,'PLANE_UNIVERSE_SET_MISMATCH')",
       "need(True,'PLANE_UNIVERSE_SET_MISMATCH')",'missing-plane'),
      ('gate-branch',"need(type(name[1]) is int and name[1]==1,'GATE_BRANCH_NOT_FULL_STATE')",
       "need(True,'GATE_BRANCH_NOT_FULL_STATE')",'gate-wrong-branch'),
    ]
    mutants=[]
    for name,anchor,replacement,case in mutations:
        observed=clock();require(source.count(anchor)==1,'mutant-anchor:'+name)
        raw=source.replace(anchor,replacement).encode();path=ROOT/('reviewer-stream-mutant-v2f-'+name+'.py');create(path,raw)
        spec=importlib.util.spec_from_file_location('mutant_'+name.replace('-','_'),path)
        mm=importlib.util.module_from_spec(spec);spec.loader.exec_module(mm);mm.DEADLINE=time.monotonic()+30
        if case=='gate-wrong-branch':
            got=outcome(mm,lambda:mm.row_vector(['gate',2],system,scope),None,'GATE_BRANCH_NOT_FULL_STATE')
        elif case=='data-processing-ambiguous':
            got=outcome(mm,lambda:mm.row_vector(['data-processing',5,2],system,scope),None,'AMBIGUOUS_DATA_PROCESSING_DESCRIPTOR')
        elif case=='wrong-archive-sha':
            got=outcome(mm,lambda:mm.verify_archive(basepath,wrong,1,12,7),None,'ARCHIVE_PIN_MISMATCH')
        else:
            path0,contract0=fixtures[case]
            original=next(x for x in cases if x['name']==case)
            got=outcome(mm,lambda:mm.verify_archive(path0,contract0,1,12,7),None,original['expected_reason'])
        mutants.append({'name':name,'source_sha256':sha(raw),'source_path':str(path),'clock_before_creation':observed,
                        'actual_reason':got.get('actual_reason'),'actual':got.get('actual'),'killed':not got['met']})
    cli=cli_controls()
    facts={'kind':'SELF_AUTHORED_SMALL_STREAMING_CONTROLS','started':start,'ended':clock(),
           'elapsed_seconds':round(time.monotonic()-mono,4),'checker_sha256':csha,'driver_sha256':ssha,
           'cases':cases,'direct_checks':direct,'mutants':mutants,'cli_checks':cli,
           'limitations':'Seven embedded synthetic planes and one synthetic identity; not the archived census or theorem.'}
    facts['all_expectations_met']=all(x['met'] for x in cases+direct+cli) and all(x['killed'] for x in mutants)
    create(ROOT/'reviewer-stream-controls-v2f-results.json',enc(facts))
    print(json.dumps({'all_expectations_met':facts['all_expectations_met'],'elapsed_seconds':facts['elapsed_seconds'],
                      'cases':len(cases),'direct_checks':len(direct),'mutants':len(mutants),'cli_checks':len(cli),
                      'failed':[x for x in cases+direct+cli if not x['met']]+[x for x in mutants if not x['killed']]},sort_keys=True))
    return 0 if facts['all_expectations_met'] else 1

if __name__=='__main__': sys.exit(main())
