#!/usr/bin/env python3
"""Own small synthetic controls; retained fixtures and no automatic cleanup."""
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
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CHECKER=ROOT/'reviewer-checker-v1.py'
OUT=ROOT/'synthetic-controls-v4'
sys.dont_write_bytecode=True


def digest(data): return hashlib.sha256(data).hexdigest()
def encode(obj): return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
def create(path,data):
    with open(path,'xb') as f:
        f.write(data); f.flush(); os.fsync(f.fileno())
def now(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
def need(ok,why):
    if not ok: raise RuntimeError(why)

def vec(terms):
    d={}
    for k,v in terms:
        if k:
            d[k]=d.get(k,0)+v
            if not d[k]: del d[k]
    return [[k,d[k]] for k in sorted(d)]
def cmi(a,b): return vec(((a,1),(b,1),(a|b,-1)))
def cond(a,b): return vec(((a|b,1),(b,-1)))
def row(name,relation,coefficient,vector):
    return {'name':name,'relation':relation,'multiplier':str(coefficient),'image_vectors':[vector]}

def fixture():
    active=list(range(2,11)); coloring=[0,1,2,0,1,2,0,2,1]
    groups=[[i for i,c in enumerate(coloring) if c==j] for j in range(3)]
    masks=[sum(1<<i for i in group) for group in groups]
    rows=[]
    for group in groups:
        prefix=0
        for i in group:
            if prefix:
                rows.append(row(['set-cmi',1<<i,prefix,0],'ge',2,cmi(1<<i,prefix)))
            prefix |= 1<<i
    for a,b in itertools.combinations(masks,2):
        rows.append(row(['set-cmi',a,b,0],'ge',1,cmi(a,b)))
    for color,part in enumerate(masks):
        rows.append(row(['proper-color-decoder',color],'eq',-1,cond(part,511^part)))
    return {'certificate_id':'SYNTHETIC-COLOR-DELETE-1','source_member':'self-authored/three-color',
            'source_index':0,'coordinate_system':{'type':'entropy_bitmask','variables':active,'nonempty_coordinates':511},
            'target_vector':[[511,'-3']]+[[1<<i,'2'] for i in range(9)],'target_relation':'ge',
            'action_count':1,'actions':[list(range(9))],
            'scope':{'missing_vertex':1,'active_vertices':active,'scale':1,'proper_coloring':coloring},
            'rows':rows}

def binding(record, record_bytes):
    return {k:record[k] for k in ('certificate_id','source_member','source_index','coordinate_system','scope')} | {'record_sha256':digest(record_bytes)}

def invoke(label,mode,raw,expect_status,expect_reason=None,expected_code=0,bind=None,extra=None,proof=None,record_sha=None):
    record_path=OUT/(label+'-record.json'); output_path=OUT/(label+'-output.json')
    create(record_path,raw)
    argv=[sys.executable,'-B',str(CHECKER),mode,'--record',str(record_path),'--record-sha256',record_sha or digest(raw),
          '--output',str(output_path),'--time-limit-ms','20000','--max-items','5000']
    if bind is not None:
        b=encode(bind); p=OUT/(label+'-binding.json'); create(p,b)
        argv+=['--binding',str(p),'--binding-sha256',digest(b)]
    if proof is not None:
        p=OUT/(label+'-proof.json'); pb=encode(proof); create(p,pb)
        argv+=['--proof',str(p),'--proof-sha256',digest(pb)]
    if extra: argv+=extra
    start=now(); t=time.monotonic()
    done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
    elapsed=round(time.monotonic()-t,4); end=now()
    result=json.loads(output_path.read_bytes()) if output_path.exists() else {}
    good=done.returncode==expected_code and result.get('status')==expect_status
    if expect_reason is not None: good=good and result.get('reason')==expect_reason
    return {'name':label,'argv':argv,'start':start,'end':end,'elapsed_seconds':elapsed,
            'record_sha256':digest(raw),'output_sha256':digest(output_path.read_bytes()) if output_path.exists() else None,
            'expected_status':expect_status,'expected_reason':expect_reason,'expected_exit':expected_code,
            'actual_status':result.get('status'),'actual_reason':result.get('reason'),'actual_exit':done.returncode,
            'stderr':done.stderr[-500:],'met_expectation':good}

def compute_masks(plane):
    triangles=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
    ng={1:{2,3,4,5,6,7},2:{1,3,7,9,10},3:{1,2,4,8,9},4:{1,3,5,8,10},
        5:{1,4,6,9,10},6:{1,5,7,8,9},7:{1,2,6,8,10},8:{3,4,6,7,9,10},
        9:{2,3,5,6,8},10:{2,4,5,7,8}}
    j=[i for i in range(10) if (plane[0]|plane[1]) & (1<<i)]
    masks=set()
    for direction in [0]+plane:
        options=[[bits for bits in range(8) if bits.bit_count()%2 == ((direction>>i)&1)] for i in j]
        for choices in itertools.product(*options):
            present=set()
            for factor,bits in zip(j,choices):
                present.update(triangles[factor][k] for k in range(3) if bits & (1<<k))
            if present and all(ng[v] & present for v in present):
                masks.add(sum(1<<(v-1) for v in present))
    return sorted(masks)

def find_coloring(masks):
    # Symmetry fixes color(1)=0; prune as soon as an entire mask is monochromatic.
    coloring=[None]*10
    def rec(i):
        if i==10: return list(coloring)
        for color in ([0] if i==0 else range(3)):
            coloring[i]=color; assigned=(1<<(i+1))-1
            bad=False
            for mask in masks:
                if mask & ~assigned == 0 and len({coloring[j] for j in range(i+1) if mask & (1<<j)})==1:
                    bad=True; break
            if not bad:
                found=rec(i+1)
                if found is not None: return found
        coloring[i]=None
        return None
    return rec(0)

def direct(label,func,expected=None,reason=None):
    try:
        value=func()
        ok=reason is None and (expected is None or value==expected)
        return {'name':label,'actual':str(value)[:700],'expected':str(expected)[:700],
                'expected_reason':reason,'actual_reason':None,'met_expectation':ok}
    except Exception as e:
        return {'name':label,'actual_exception':type(e).__name__,'actual_reason':str(e),
                'expected_reason':reason,'met_expectation':reason is not None and str(e)==reason}

def mutation_controls(cases, system, scope):
    source=CHECKER.read_text()
    specifications=[
        ('sign', "need(valid,'ROW_SIGN')", "need(True,'ROW_SIGN')", 'negative-ge-sign'),
        ('image', "need(parse_vector(advertised,max_id,False)==actual,'IMAGE_VECTOR_MISMATCH')",
         "need(True,'IMAGE_VECTOR_MISMATCH')", 'negative-image'),
        ('binding', "need(record[k]==binding[k], 'SOURCE_BINDING_MISMATCH:' + k)",
         "need(True, 'SOURCE_BINDING_MISMATCH:' + k)", 'negative-source-substitution'),
        ('mask-set', "need(set(advertised)==actual, 'ALLOWED_MASK_SET_MISMATCH')",
         "need(True, 'ALLOWED_MASK_SET_MISMATCH')", 'negative-same-count-mask-set'),
        ('duplicate-json', "if key in out:\n            raise Reject('DUPLICATE_JSON_KEY:' + key)",
         "if False:\n            raise Reject('DUPLICATE_JSON_KEY:' + key)", 'negative-duplicate-json'),
        ('local-decoder', "need(inc == {c},'LOCAL_DECODER_NOT_SINGLETON_COLOR')",
         "need(True,'LOCAL_DECODER_NOT_SINGLETON_COLOR')", None),
        ('plane-set', "need(set(left)==set(right),'PLANE_ACTUAL_SET_MISMATCH')",
         "need(True,'PLANE_ACTUAL_SET_MISMATCH')", None),
        ('exclusive-output', "os.O_WRONLY|os.O_CREAT|os.O_EXCL",
         "os.O_WRONLY|os.O_CREAT|os.O_TRUNC", 'exclusive-existing-output'),
    ]
    out=[]
    for label,anchor,replacement,case_name in specifications:
        observed_clock=now()
        need(source.count(anchor)==1,'MUTANT_ANCHOR_COUNT:'+label)
        mutated=source.replace(anchor,replacement)
        need(mutated!=source,'MUTANT_UNCHANGED:'+label)
        path=ROOT/('reviewer-mutant-v4-'+label+'.py')
        create(path,mutated.encode())
        entry={'name':label,'mutant_path':str(path),'mutant_sha256':digest(mutated.encode()),
               'observed_clock_before_creation':observed_clock,'start':now()}
        if case_name is None:
            spec=importlib.util.spec_from_file_location('own_mutant_'+label.replace('-','_'),path)
            mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
            try:
                if label=='local-decoder':
                    mm.row_vector(['functional-local-fd',1,0],system,scope)
                else:
                    mm.compare_plane_sets([[1,2,3],[1,4,5]],[[1,2,3],[1,6,7]],3)
                entry['actual']='NO_REJECTION'; entry['killed']=True
            except Exception as exc:
                expected='LOCAL_DECODER_NOT_SINGLETON_COLOR' if label=='local-decoder' else 'PLANE_ACTUAL_SET_MISMATCH'
                entry['actual']=type(exc).__name__+':'+str(exc); entry['killed']=str(exc)!=expected
        else:
            baseline=next(c for c in cases if c['name']==case_name)
            need(baseline['met_expectation'],'MUTANT_BASELINE_NOT_MET:'+label)
            argv=list(baseline['argv']); argv[2]=str(path)
            mutant_output=OUT/('mutant-'+label+'-output.json')
            if label=='exclusive-output': create(mutant_output,b'owner-sentinel\n')
            argv[argv.index('--output')+1]=str(mutant_output)
            done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
            result={}
            if mutant_output.exists():
                try: result=json.loads(mutant_output.read_bytes())
                except (ValueError,UnicodeDecodeError): pass
            if label=='exclusive-output':
                killed=done.returncode!=73 or mutant_output.read_bytes()!=b'owner-sentinel\n'
            else:
                killed=(done.returncode!=baseline['expected_exit'] or
                        result.get('status')!=baseline['expected_status'] or
                        result.get('reason')!=baseline['expected_reason'])
            entry.update({'argv':argv,'actual_exit':done.returncode,'actual_status':result.get('status'),
                          'actual_reason':result.get('reason'),'output_sha256':digest(mutant_output.read_bytes()) if mutant_output.exists() else None,
                          'stderr':done.stderr[-500:],'killed':killed})
        entry['end']=now()
        out.append(entry)
    return out


def main():
    start=now(); start_mono=time.monotonic()
    os.mkdir(OUT)
    checker_sha=digest(CHECKER.read_bytes()); control_sha=digest(Path(__file__).read_bytes())
    spec=importlib.util.spec_from_file_location('own_reviewer_checker',CHECKER)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    record=fixture(); raw=encode(record); bind=binding(record,raw)
    cases=[]
    cases.append(invoke('positive-proper-three-color','identity',raw,'VALID_IDENTITY_CONDITIONAL',bind=bind))
    for label,idx in [('positive-string-source-index','1'),('positive-null-source-index',None)]:
        value=copy.deepcopy(record); value['source_index']=idx; blob=encode(value)
        cases.append(invoke(label,'identity',blob,'VALID_IDENTITY_CONDITIONAL',bind=binding(value,blob)))
    def altered(label,mutator,reason,code=2,status='REJECT'):
        value=copy.deepcopy(record); mutator(value); blob=encode(value)
        return invoke(label,'identity',blob,status,reason,code,bind=binding(value,blob))
    cases.append(altered('negative-bool-source-index',lambda x:x.__setitem__('source_index',True),'SOURCE_ID_SCHEMA'))
    cases.append(altered('negative-ge-sign',lambda x:x['rows'][0].__setitem__('multiplier','-2'),'ROW_SIGN'))
    cases.append(altered('negative-image',lambda x:x['rows'][0]['image_vectors'][0][0].__setitem__(1,2),'IMAGE_VECTOR_MISMATCH'))
    cases.append(altered('negative-target',lambda x:x['target_vector'][0].__setitem__(1,'-2'),'TARGET_VECTOR_MISMATCH'))
    cases.append(altered('negative-rational',lambda x:x['rows'][0].__setitem__('multiplier','2.0'),'INVALID_RATIONAL'))
    cases.append(altered('negative-row-relation',lambda x:x['rows'][0].__setitem__('relation','eq'),'ROW_RELATION_MISMATCH'))
    cases.append(altered('negative-duplicate-coordinate',lambda x:x['rows'][0]['image_vectors'][0].append(x['rows'][0]['image_vectors'][0][0]),'DUPLICATE_VECTOR_COORDINATE'))
    cases.append(altered('negative-improper-color',lambda x:x['scope']['proper_coloring'].__setitem__(1,0),'IMPROPER_GRAPH_COLOR'))
    cases.append(altered('negative-action',lambda x:x.__setitem__('actions',[[1,0,2,3,4,5,6,7,8]]),'PROPER_ACTION_NOT_GRAPH'))
    cases.append(altered('unknown-row-family',lambda x:x['rows'][0].__setitem__('name',['not-defined']),'UNSPECIFIED_PROPER_DESCRIPTOR:not-defined',3,'UNKNOWN'))
    changed=copy.deepcopy(record); changed['source_index']=1; changedraw=encode(changed)
    b=copy.deepcopy(bind); b['record_sha256']=digest(changedraw)
    cases.append(invoke('negative-source-substitution','identity',changedraw,'REJECT','SOURCE_BINDING_MISMATCH:source_index',2,bind=b))
    cases.append(invoke('negative-hash-substitution','identity',raw,'REJECT','INPUT_SHA_MISMATCH',2,bind=bind,record_sha='0'*64))
    cases.append(invoke('negative-duplicate-json','identity',b'{"x":1,"x":2}\n','REJECT','DUPLICATE_JSON_KEY:x',2,bind=bind))
    cases.append(invoke('negative-json-float','identity',b'{"x":0.5}\n','REJECT','FLOAT_OR_NONFINITE_FORBIDDEN',2,bind=bind))
    cases.append(invoke('negative-json-nan','identity',b'{"x":NaN}\n','REJECT','FLOAT_OR_NONFINITE_FORBIDDEN',2,bind=bind))
    cases.append(invoke('unknown-row-cap','identity',raw,'UNKNOWN','ROW_CAP',3,bind=bind,extra=['--max-items','2']))
    planes=[[1,2,3],[1,4,5],[1,6,7],[2,4,6],[2,5,7],[3,4,7],[3,5,6]]
    cases.append(invoke('positive-seven-planes','planes',encode({'dimension':3,'planes':planes}),'VALID_DIRECTION_SET_ONLY'))
    cases.append(invoke('negative-rank-one-plane','planes',encode({'dimension':3,'planes':planes[:-1]+[[1,1,2]]}),'REJECT','PLANE_RANK_OR_ORDER',2))
    cases.append(invoke('unknown-plane-cap','planes',encode({'dimension':3,'planes':planes}),'UNKNOWN','PLANE_CAP',3,extra=['--max-items','6']))
    proof={'kind':'noncover','target_plane':[1,2,3],'target_missing':8,
           'vertex_action':[8,9,3,4,10,7,6,1,2,5]}
    cases.append(invoke('positive-proper-applicability','applicability',raw,'VALID_APPLICABILITY_CONDITIONAL',bind=bind,proof=proof))
    proof_bad=copy.deepcopy(proof); proof_bad['target_missing']=1
    cases.append(invoke('negative-covered-vertex','applicability',raw,'REJECT','VERTEX_IS_COVERED',2,bind=bind,proof=proof_bad))
    plane=[5,96,101]; masks=compute_masks(plane); coloring=find_coloring(masks)
    if coloring is not None:
        color_obj={'plane':plane,'coloring':coloring,'allowed_masks':masks}
        cases.append(invoke('positive-fourfactor-color','color',encode(color_obj),'VALID_COLOR_CONDITIONAL'))
        bad=copy.deepcopy(color_obj); bad['coloring']=[0]*10
        cases.append(invoke('negative-monochromatic','color',encode(bad),'REJECT','MONOCHROMATIC_ALLOWED_MASK',2))
        bad=copy.deepcopy(color_obj); substitute=next(x for x in range(1,1024) if x not in set(masks))
        bad['allowed_masks'][-1]=substitute
        cases.append(invoke('negative-same-count-mask-set','color',encode(bad),'REJECT','ALLOWED_MASK_SET_MISMATCH',2))
    else:
        cases.append({'name':'positive-fourfactor-color','met_expectation':False,'actual_reason':'NO_COLOR_FOUND_FOR_SYNTHETIC_PLANE'})
    funcs=[]
    system={'type':'functional_branch'}; scope={'colors':[0,1,None,None,None,None,None,None,None,None]}
    funcs.append(direct('functional-local-exact',lambda:m.row_vector(['functional-local-fd',2,0],system,scope),({37:1,27:-1},'eq')))
    funcs.append(direct('reject-two-color-local',lambda:m.row_vector(['functional-local-fd',1,0],system,scope),reason='LOCAL_DECODER_NOT_SINGLETON_COLOR'))
    funcs.append(direct('reject-nonincident-color',lambda:m.row_vector(['functional-neighborhood',2,1],system,scope),reason='FUNCTIONAL_NOT_INCIDENT'))
    funcs.append(direct('mixed-local-exact',lambda:m.row_vector(['mixed-local-fd',1],system,scope),({156:1,151:-1},'eq')))
    funcs.append(direct('state-visibility-exact',lambda:m.row_vector(['state-neighborhood',1],system,scope),({631:1,630:-1},'eq')))
    funcs.append(direct('state-not-visible',lambda:m.row_vector(['state-neighborhood',2],system,scope),reason='STATE_NOT_VISIBLE'))
    funcs.append(direct('triangle-exact',lambda:m.row_vector(['functional-triangle',1],system,scope),({37:1,35:-1},'eq')))
    funcs.append(direct('data-processing-exact',lambda:m.row_vector(['data-processing',5,2],system,scope),({26:1,27:-1,2:1,1:-1},'le')))
    funcs.append(direct('pair-determines-exact',lambda:m.row_vector(['pair-determines-state',5,2,3],system,scope),({26:1,25:1,27:-1,28:-1},'le')))
    funcs.append(direct('pair-same-form',lambda:m.row_vector(['pair-determines-state',5,2,2],system,scope),reason='PAIR_FUNCTIONALS_NOT_DISTINCT'))
    funcs.append(direct('functional-gate-vector',lambda:m.factor_gate_vector(True),
                        {5115:3,1:17,6:-2,11:-2,21:-2,41:-2,81:-2,161:-2,321:-2,641:-2,1281:-2,2561:-2}))
    funcs.append(direct('scalar-gate-vector',lambda:m.factor_gate_vector(False),
                        {1023:3,1024:17,1025:-2,1026:-2,1028:-2,1032:-2,1040:-2,1056:-2,1088:-2,1152:-2,1280:-2,1536:-2}))
    funcs.append(direct('unrecognized-gate-descriptor',lambda:m.row_vector(['undeclared-gate'],system,scope),
                        reason='UNSPECIFIED_FUNCTIONAL_DESCRIPTOR:undeclared-gate'))
    funcs.append(direct('graph-edge-3-4',lambda:m.row_vector(['graph-fd',3],system,scope),({1995:1,1975:-1},'eq')))
    funcs.append(direct('scalar-local-mask-guard',lambda:m.row_vector(['conditional-zero-rank-fd',0,1],{'type':'entropy_bitmask','variables':list(range(1,11))+['S']},{'factors':[1,2]}),reason='LOCAL_MASK_MISMATCH'))
    funcs.append(direct('cmi-overlap',lambda:m.row_vector(['cmi',1,0,1,1],system,scope),reason='CMI_OVERLAP'))
    funcs.append(direct('same-count-wrong-plane-set',lambda:m.compare_plane_sets([[1,2,3],[1,4,5]],[[1,2,3],[1,6,7]],3),reason='PLANE_ACTUAL_SET_MISMATCH'))
    funcs.append(direct('graph-automorphism-count',lambda:len(m.graph_actions()),8))
    funcs.append(direct('factor-automorphism-count',lambda:sum(m.factors_of_action(a) is not None for a in m.graph_actions()),4))
    fp={'kind':'functional','source_plane':[1,2,3],'target_plane':[1,2,3],
        'target_colors':scope['colors'],'vertex_action':list(range(1,11)),'color_action':[0,1,2]}
    frec={'coordinate_system':system,'scope':scope,'certificate_id':'own'}
    funcs.append(direct('functional-transport',lambda:m.verify_applicability(fp,frec),{'kind':'functional','plane':[1,2,3],'certificate_id':'own'}))
    fp_bad=copy.deepcopy(fp); fp_bad['target_colors']=[1,0,None,None,None,None,None,None,None,None]
    funcs.append(direct('functional-wrong-color-transport',lambda:m.verify_applicability(fp_bad,frec),reason='CERTIFICATE_COLOR_TRANSPORT_MISMATCH'))
    # Existing outputs are retained and must not be replaced.
    sentinel=OUT/'exclusive-existing.json'; create(sentinel,b'owner-sentinel\n')
    rp=OUT/'exclusive-record.json'; create(rp,raw); bp=OUT/'exclusive-binding.json'; bb=encode(bind); create(bp,bb)
    argv=[sys.executable,'-B',str(CHECKER),'identity','--record',str(rp),'--record-sha256',digest(raw),
          '--binding',str(bp),'--binding-sha256',digest(bb),'--output',str(sentinel)]
    t=now(); done=subprocess.run(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=30)
    cases.append({'name':'exclusive-existing-output','start':t,'end':now(),'argv':argv,'actual_exit':done.returncode,
                  'stderr':done.stderr[-500:],'output_sha256':digest(sentinel.read_bytes()),
                  'met_expectation':done.returncode==73 and sentinel.read_bytes()==b'owner-sentinel\n' and 'OUTPUT_EXCLUSIVE_FAILED' in done.stderr})
    # Cooperative SIGINT to this script's own child, while parsing/evaluating a large synthetic row list.
    big=copy.deepcopy(record); big['rows']=record['rows']*3000
    bigraw=encode(big); bigbind=encode(binding(big,bigraw))
    br=OUT/'interrupt-record.json'; bp=OUT/'interrupt-binding.json'; bo=OUT/'interrupt-output.json'
    create(br,bigraw); create(bp,bigbind)
    argv=[sys.executable,'-B',str(CHECKER),'identity','--record',str(br),'--record-sha256',digest(bigraw),
          '--binding',str(bp),'--binding-sha256',digest(bigbind),'--output',str(bo),
          '--time-limit-ms','20000','--max-items','50000']
    t=now(); child=subprocess.Popen(argv,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    time.sleep(0.12)
    sent=child.poll() is None
    if sent: os.kill(child.pid,signal.SIGINT)
    stdout,stderr=child.communicate(timeout=30)
    observed=json.loads(bo.read_bytes()) if bo.exists() else {}
    cases.append({'name':'cooperative-interrupt','start':t,'end':now(),'argv':argv,'signal_sent':sent,
                  'record_sha256':digest(bigraw),'actual_exit':child.returncode,'actual_status':observed.get('status'),
                  'actual_reason':observed.get('reason'),'output_sha256':digest(bo.read_bytes()) if bo.exists() else None,
                  'stderr':stderr[-500:],'met_expectation':sent and child.returncode==3 and observed.get('status')=='UNKNOWN' and observed.get('reason')=='INTERRUPTED_SIGNAL_2'})
    mutants=mutation_controls(cases,system,scope)
    facts={'kind':'SELF_AUTHORED_BOUNDED_FIXTURES_NOT_BULK_REPLAY','started_native_clock':start,'ended_native_clock':now(),
           'elapsed_seconds':round(time.monotonic()-start_mono,4),'checker_sha256':checker_sha,'control_sha256':control_sha,
           'cases':cases,'direct_checks':funcs,'single_guard_mutations':mutants,
           'color_fixture':{'plane':plane,'allowed_mask_count':len(masks),'coloring':coloring},
           'limitations':'Synthetic controls only; no archive certificate or census was replayed.'}
    facts['all_expectations_met']=all(c['met_expectation'] for c in cases+funcs) and all(x['killed'] for x in mutants)
    create(ROOT/'reviewer-synthetic-controls-v4-results.json',encode(facts))
    print(json.dumps({'all_expectations_met':facts['all_expectations_met'],
                      'elapsed_seconds':facts['elapsed_seconds'],
                      'cases':len(cases),'direct_checks':len(funcs),'mutants':len(mutants),
                      'failed':[x for x in cases+funcs if not x['met_expectation']]+[x for x in mutants if not x['killed']]},sort_keys=True))
    return 0 if facts['all_expectations_met'] else 1

if __name__=='__main__': sys.exit(main())
