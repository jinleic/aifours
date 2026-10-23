"""Pinned independent GB analogue of F_one: sixteen templates + six M_s inputs.
No solver and NO CNF on disk. Only GB's clause-storage F.c sink is replaced by
its exact CLI byte serialization; inherited GB.new/encode logic is unchanged.
All g IDs come from GB's OWN F.tab, never GA unit IDs. Generation is one Python
process with a1GiB self-RSS guard. The relaxed classical control drops exactly
one Q1 P4-ALO and seven nonconstant Q1-SB2 units FOR EVALUATION ONLY; emitted
base bytes retain every clause. No unrelaxed classical SAT claim is made.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import resource
import shutil
import stat
import sys
import time
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
GB = ROOT/'code/gram_b_r2.py'
GB_SHA = '4b593e557fe5b26053537e7107ca5e7a11b3df8ce011bdf78981bc7e068beae0'
WMAN = ROOT/'evidence/n8_one_p4_templates_v1/MANIFEST.json'
WMAN_SHA = '355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'
GA_STRONG_HASHES = ROOT/'evidence/P1_MONOMIAL_FORMULA_HASHES.r2.json'
GA_STRONG_SHA = 'e04557a4ea83875caa265e9928b488386fe52c2f95306bd6078f7706265eb709'
FREEZE = ROOT/'review/GB_ONE_P4_FREEZE.r1.json'
OUT = ROOT/'evidence/GB_ONE_P4_MANIFEST.r1.json'
OWN_NAMES = ROOT/'evidence/GB_ONE_P4_OWN_NAMES.r1.json'
MAPPING = ROOT/'evidence/GB_ONE_P4_MAPPING.r1.json'
FLAGS = ['--order','8','--quantum','12345','--ngeneric','0','--p4','1','--sb2','--g5']
STRENGTHENED = (('P1-B1',2),('P1-B2',2),('P1-B2',4),('P1-B3',2),('P1-B5',2),('P1-B5',3))
SLOPES = {1:1,2:4,3:5,4:6,5:7}
RSS_CAP = 1073741824
SCIENCE_STOP = datetime.fromisoformat('2026-10-18T17:30:00-07:00').timestamp()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def new_json(path,obj):
    raw=json.dumps(obj,indent=1).encode()
    with path.open('xb') as f:
        f.write(raw)
    return sha(raw)


def allocated_bytes(root):
    pending,seen,total=[Path(root)],set(),0
    while pending:
        p=pending.pop();s=p.lstat();key=(s.st_dev,s.st_ino)
        if key in seen:
            continue
        seen.add(key);total+=s.st_blocks*512
        if stat.S_ISDIR(s.st_mode):
            with os.scandir(p) as entries:
                pending.extend(Path(e.path) for e in entries)
    return ((total+1023)//1024)*1024


def gf8(a,b):
    x=0
    while b:
        if b&1:x^=a
        b>>=1;a<<=1
        if a&8:a^=11
    return x


def classical_configuration():
    squares={s:[[c^gf8(a,r) for c in range(8)] for r in range(8)] for s,a in SLOPES.items()}
    for rows in squares.values():
        if rows[0]!=list(range(8)):
            raise RuntimeError('classical control row0 not standard')
        if any(sorted(row)!=list(range(8)) for row in rows):
            raise RuntimeError('classical control row not permutation')
        if any(sorted(rows[r][c] for r in range(8))!=list(range(8)) for c in range(8)):
            raise RuntimeError('classical control column not permutation')
    for a,b in itertools.combinations(squares,2):
        if len({(squares[a][r][c],squares[b][r][c]) for r in range(8) for c in range(8)})!=64:
            raise RuntimeError('classical control squares not orthogonal')
    return squares


def load_gb():
    if sha(GB.read_bytes())!=GB_SHA:
        raise RuntimeError('independent GB source pin mismatch')
    spec=importlib.util.spec_from_file_location('pinned_independent_GB_r2',GB)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m


def make_sink(original,model=None):
    class Sink(original):
        def __init__(self):
            super().__init__()
            self.body=bytearray();self.count=0;self.started=time.monotonic();self.max_rss=0
            self.values=bytearray([0]);self.q1_sb2=set();self.relaxed=[];self.pending=[]
            self.positive_checked=0;self.positive_units_forced=0
        def new(self,key=None):
            v=super().new(key)
            self.values.append(0)
            if model is not None:
                if key=='TRUE':self.values[v]=2
                elif isinstance(key,tuple) and key[0]=='g':
                    _,s,p,q=key
                    self.values[v]=2 if model[s][p[0]][p[1]]==model[s][q[0]][q[1]] else 1
                    if s==1 and p[0]==0 and 1<=p[1]<=7 and q==(1,0):self.q1_sb2.add(v)
                elif key is not None:raise RuntimeError('unexpected named variable in no-classical GB')
            return v
        def evaluate(self,lits,allow_pending=True):
            unknown=0;last=0
            for lit in lits:
                value=self.values[abs(lit)]
                if not value:unknown+=1;last=lit
                elif (value==2)==(lit>0):return True
            if unknown==0:return False
            if unknown==1:
                self.values[abs(last)]=2 if last>0 else 1
                self.positive_units_forced+=1
                return True
            if allow_pending:self.pending.append(tuple(lits))
            return None
        def guard(self):
            self.max_rss=max(self.max_rss,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            if self.max_rss>RSS_CAP:raise RuntimeError('GB generation1GiB self-RSS cap exceeded')
            if time.monotonic()-self.started>2700 or time.time()>=SCIENCE_STOP:
                raise RuntimeError('GB generation wall/science-stop cap')
            if shutil.disk_usage(ROOT).free<12000000000:
                raise RuntimeError('GB generation in-flight floor lost; no output/CNF')
        def c(self,*lits):
            line=(' '.join(map(str,lits))+' 0\n').encode()
            index=self.count;self.count+=1;self.body.extend(line)
            if model is not None:
                relax=None
                if len(lits)==56 and all(x>0 for x in lits):relax='Q1 row0 P4-ALO'
                elif len(lits)==1 and abs(lits[0]) in self.q1_sb2:relax='Q1 nonconstant SB2 unit'
                if relax:
                    self.relaxed.append({'clause_index_zero_based':index,'kind':relax,'literals':list(lits),'line_sha256':sha(line)})
                else:
                    result=self.evaluate(lits)
                    if result is False:raise RuntimeError('classical relaxed model violates GB clause%d'%index)
                    self.positive_checked+=1
            if self.count%65536==0:self.guard()
    return Sink


def component_controls(gb):
    """Run exact nested GB gate source with fixed inputs; no branching/solver."""
    tree=ast.parse(GB.read_text())
    encode=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='encode')
    gates={x.name:x for x in encode.body if isinstance(x,ast.FunctionDef) and x.name in ('conj','counter2','atleast3')}
    if set(gates)!= {'conj','counter2','atleast3'}:raise RuntimeError('GB component source not found')
    gate_module=ast.fix_missing_locations(ast.Module(body=[copy.deepcopy(gates[n]) for n in ('conj','counter2','atleast3')],type_ignores=[]))
    compiled=compile(gate_module,str(GB)+'#exact-components','exec')

    def fixed_model(f,inputs):
        values={1:True,**inputs}
        while True:
            changed=False
            for clause in f.cl:
                if any(abs(v) in values and values[abs(v)]==(v>0) for v in clause):continue
                unknown=[v for v in clause if abs(v) not in values]
                if not unknown:return None
                if len(unknown)==1:
                    values[abs(unknown[0])]=unknown[0]>0;changed=True
            if not changed:break
        if not all(any(abs(v) in values and values[abs(v)]==(v>0) for v in clause) for clause in f.cl):
            raise RuntimeError('GB component aux extension unresolved')
        return values

    counts={'conj':0,'counter2':0,'atleast3':0}
    wrong_output_rejections=0
    for gate,width in (('conj',2),('counter2',8),('atleast3',8)):
        for bits in range(1<<width):
            f=gb.F();T=f.new('TRUE');f.c(T)
            ids=[f.new() for _ in range(width)]
            env={'F_':f,'T':T};exec(compiled,env)
            out=env[gate](*ids) if gate=='conj' else env[gate](ids)
            inputs={v:bool((bits>>i)&1) for i,v in enumerate(ids)}
            values=fixed_model(f,inputs)
            if values is None:raise RuntimeError('GB component rejects fixed-input definition')
            weight=bits.bit_count()
            if gate=='conj':expected=weight==2;actual=values[abs(out)]==(out>0)
            elif gate=='atleast3':expected=weight>=3;actual=values[abs(out)]==(out>0)
            else:expected=(weight>=1,weight>=2);actual=tuple(values[abs(v)]==(v>0) for v in out)
            if actual!=expected:raise RuntimeError('GB component truth-table mismatch')
            counts[gate]+=1
            if gate=='atleast3' and bits in (6,14):
                # Weight2 must reject a demanded TRUE threshold3; weight3 must
                # reject a demanded FALSE threshold3. These are nonvacuous.
                f.c(out if weight==2 else -out)
                if fixed_model(f,inputs) is not None:raise RuntimeError('GB wrong-threshold component mutation accepted')
                wrong_output_rejections+=1
    return {'exact_source_GB_sha256':GB_SHA,'fixed_input_cases':counts,'wrong_threshold_output_rejections':wrong_output_rejections,
            'weight2_threshold3_false_and_weight3_true':True,
            'method':'exact nested GB AST; deterministic forced aux evaluation, no search or solver',
            'scope':'component equivalence, not full heavy-formula SAT or n8 exclusion'}


def sink_parity_control(gb):
    original=gb.F
    small=gb.encode(3,[1],0,[],False,fixg=None,g5=True,allrows=False,allcols=False)
    expected=''.join(' '.join(map(str,c))+' 0\n' for c in small.cl).encode()
    try:
        gb.F=make_sink(original)
        streamed=gb.encode(3,[1],0,[],False,fixg=None,g5=True,allrows=False,allcols=False)
    finally:
        gb.F=original
    if streamed.n!=small.n or streamed.tab!=small.tab or streamed.count!=len(small.cl) or streamed.body!=expected:
        raise RuntimeError('storage-only sink differs from original GB')
    return {'toy_n':3,'quantum':[1],'clauses':len(small.cl),'variables':small.n,'body_sha256':sha(expected),
            'clause_bytes_name_table_allocator_equal':True,'scope':'I/O adapter equivalence only, not n8 exclusion'}


def finish_positive(f):
    if len(f.relaxed)!=8 or sum(x['kind']=='Q1 row0 P4-ALO' for x in f.relaxed)!=1:
        raise RuntimeError('positive control did not relax exactly1ALO+7SB2')
    if f.pending:
        pending=f.pending;f.pending=[]
        for _ in range(16):
            next_pending=[];before=f.positive_units_forced
            for clause in pending:
                r=f.evaluate(clause,False)
                if r is False:raise RuntimeError('positive pending clause violated')
                if r is None:next_pending.append(clause)
            pending=next_pending
            if not pending:break
            if f.positive_units_forced==before:raise RuntimeError('positive aux extension not fully verified')
        if pending:raise RuntimeError('positive aux extension iteration cap')
    unassigned=sum(x==0 for x in f.values[1:])
    for i in range(1,len(f.values)):
        if f.values[i]==0:f.values[i]=1
    dropped_false=[]
    for rec in f.relaxed:
        if not any((f.values[abs(x)]==2)==(x>0) for x in rec['literals']):dropped_false.append(rec['clause_index_zero_based'])
    return {'status':'PASS_RELAXED_CLASSICAL_CONFIGURATION','configuration_slopes':SLOPES,
            'row_column_and_pairwise_MOLS_checks':True,'relaxations_for_evaluation_ONLY':f.relaxed,
            'relaxed_clause_count':8,'verified_remaining_clauses':f.positive_checked,
            'unassigned_irrelevant_before_final_false':unassigned,'aux_values_sha256':sha(f.values),
            'dropped_clauses_actually_false':dropped_false,'body_clauses_dropped':0,
            'no_unrelaxed_base_SAT_claim':True,'method':'fixed primary Gram model plus deterministic forced aux extension; no branching or solver'}


def own_g(f,s,c,i):
    key=('g',s,(0,c),(i,0))
    v=f.tab.get(key)
    if type(v) is not int or not 1<=v<=f.n:raise RuntimeError('GB own primary name missing')
    return v


def template_units(f,case):
    supports=case['supports_row2to7']
    if len(supports)!=6:raise RuntimeError('source template does not have6rows')
    # Deliberately NEVER read case['units']; those are GA IDs, not GB IDs.
    return [own_g(f,1,c,i) if c in supports[i-2] else -own_g(f,1,c,i)
            for i in range(2,8) for c in range(1,8)]


def m_clauses(f,s):
    clauses=[tuple(sorted((-own_g(f,s,c,i),-own_g(f,s,d,i)))) for i in range(2,8)
             for c,d in itertools.combinations(range(1,8),2)]
    if len(clauses)!=126 or len(set(clauses))!=126:raise RuntimeError('GB M_s count/uniqueness error')
    return clauses


def hash_tail(prefix,tail):
    h=prefix.copy();h.update(tail);return h.hexdigest()


def main():
    t0=time.monotonic();script_sha=sha(Path(__file__).read_bytes());freeze_raw=FREEZE.read_bytes();freeze=json.loads(freeze_raw)
    if freeze['generator_sha256']!=script_sha or freeze['GB_sha256']!=GB_SHA or freeze['flags']!=FLAGS:
        raise RuntimeError('GB generator must be frozen before execution')
    free=shutil.disk_usage(ROOT).free;used=allocated_bytes(ROOT)
    if free-1000000<12200000000 or used+1000000>10200547328:raise SystemExit('DEFERRED: GB generation disk/lane gate')
    wraw=WMAN.read_bytes();sraw=GA_STRONG_HASHES.read_bytes()
    if sha(wraw)!=WMAN_SHA or sha(sraw)!=GA_STRONG_SHA:raise RuntimeError('semantic source-template/hash pin changed')
    source=json.loads(wraw);cases={x['id']:x for x in source['cases']}
    if len(cases)!=16:raise RuntimeError('sixteen source support templates required')
    ga_strong={x['id']:x['CNF_sha256_PLANNED'] for x in json.loads(sraw)['formulas']}
    gb=load_gb();parity=sink_parity_control(gb);components=component_controls(gb);configuration=classical_configuration();original=gb.F
    try:
        gb.F=make_sink(original,configuration)
        f=gb.encode(8,[1,2,3,4,5],0,[1],True,fixg=None,g5=True,allrows=False,allcols=False)
    finally:
        gb.F=original
    f.guard();positive=finish_positive(f)
    if sha(GB.read_bytes())!=GB_SHA:raise RuntimeError('GB file changed during generation')
    if f.cl:raise RuntimeError('I/O sink unexpectedly accumulated original clause lists')
    own_names={json.dumps(k):v for k,v in f.tab.items()}
    own_names_raw=json.dumps(own_names).encode();own_names_sha=sha(own_names_raw)
    reverse={v:k for k,v in f.tab.items()}
    mapping=[]
    for s in range(1,6):
        for i in range(1,8):
            for c in range(1,8):
                v=own_g(f,s,c,i)
                if reverse[v]!=('g',s,(0,c),(i,0)):raise RuntimeError('GB own-name decode mismatch')
                mapping.append({'s':s,'c':c,'i':i,'GB_variable':v,'GB_decoded_name':list(reverse[v])})
    prefixes={}
    for extra in (0,42,168):
        h=hashlib.sha256(('p cnf %d %d\n'%(f.n,f.count+extra)).encode());h.update(f.body);prefixes[extra]=h
    direct=[];strength=[];unit_lookup={};m_lookup={}
    for cid,case in cases.items():
        units=template_units(f,case);unit_lookup[cid]=units
        if len(units)!=42:raise RuntimeError('GB source template not42units')
        for pos,lit in enumerate(units):
            i,c=2+pos//7,1+pos%7
            if reverse[abs(lit)]!=('g',1,(0,c),(i,0)) or (lit>0)!=(c in case['supports_row2to7'][i-2]):
                raise RuntimeError('GB template unit sign/decode mismatch')
        tail=''.join('%d 0\n'%v for v in units).encode();digest=hash_tail(prefixes[42],tail)
        direct.append({'id':cid,'variables':f.n,'clauses':f.count+42,'CNF_sha256_PLANNED':digest,
                       'source_semantic_template':cid,'GA_counterpart_sha256_REFERENCE':case['cnf_sha256'],
                       'GB_unit_literals':units,'GB_unit_tail_sha256':sha(tail),'decoded_units_checked':42})
    for cid,s in STRENGTHENED:
        clauses=m_clauses(f,s);m_lookup[(cid,s)]=clauses
        for row_index,cl in enumerate(clauses):
            i=2+row_index//21
            if any(reverse[abs(v)][1]!=s or reverse[abs(v)][3]!=(i,0) for v in cl):raise RuntimeError('M_s own-name decode mismatch')
        units=''.join('%d 0\n'%v for v in unit_lookup[cid]).encode()
        binaries=''.join('%d %d 0\n'%cl for cl in clauses).encode();tail=units+binaries
        ident=cid+'.M%d'%s
        strength.append({'id':ident,'variables':f.n,'clauses':f.count+168,'CNF_sha256_PLANNED':hash_tail(prefixes[168],tail),
                         'source_semantic_template':cid,'monomial_square':s,'appended_unit_count':42,'appended_binary_count':126,
                         'GA_counterpart_sha256_REFERENCE':ga_strong[ident],'GB_M_binary_tail_sha256':sha(binaries),
                         'all_M_literals_decode_to_intended_square_row':True})
    mutated_units=list(unit_lookup['P0-B1']);mutated_units[0]*=-1
    unit_mut_hash=hash_tail(prefixes[42],''.join('%d 0\n'%x for x in mutated_units).encode())
    original_unit_hash=next(x['CNF_sha256_PLANNED'] for x in direct if x['id']=='P0-B1')
    mutated_m=[list(x) for x in m_lookup[('P1-B1',2)]];mutated_m[0][0]*=-1
    mtail=''.join('%d 0\n'%x for x in unit_lookup['P1-B1']).encode()+''.join('%d %d 0\n'%tuple(cl) for cl in mutated_m).encode()
    m_mut_hash=hash_tail(prefixes[168],mtail);original_m_hash=next(x['CNF_sha256_PLANNED'] for x in strength if x['id']=='P1-B1.M2')
    if unit_mut_hash==original_unit_hash or m_mut_hash==original_m_hash:raise RuntimeError('GB hash sign-flip control failed')
    if len(direct)!=16 or len(strength)!=6 or len({x['CNF_sha256_PLANNED'] for x in direct+strength})!=22:
        raise RuntimeError('GB22 distinct formulas required')
    with OWN_NAMES.open('xb') as out:out.write(own_names_raw)
    mapping_sha=new_json(MAPPING,{'GB_sha256':GB_SHA,'GB_own_names_sha256':own_names_sha,'TRUE_variable':f.tab['TRUE'],
                                'constant_g_s((0,0),(i,0))':'-TRUE for i>0','mapping':mapping,
                                'GA_IDs_used':False,'GB_decoded_mapping_rows':len(mapping)})
    result={'schema':'gb-one-p4-22hashes/1','status':'GENERATED_INPUT_HASHES_NOT_REFUTATIONS',
            'generator_sha256':script_sha,'freeze_sha256':sha(freeze_raw),'GB_sha256':GB_SHA,'GB_file_modified':False,
            'exact_flags':FLAGS,'encode_kwargs':{'n':8,'Q':[1,2,3,4,5],'ngen':0,'p4':[1],'sb2':True,'g5':True,
                                               'fixg':None,'allrows':False,'allcols':False,'ROWLEX':False},
            'source_WMAN_sha256':WMAN_SHA,'GB_base':{'variables':f.n,'clauses':f.count,'body_bytes':len(f.body),
                                                 'body_sha256':sha(f.body),'CNF_sha256_PLANNED':prefixes[0].hexdigest()},
            'GB_own_names_file':str(OWN_NAMES.relative_to(ROOT)),'GB_own_names_sha256':own_names_sha,
            'mapping_file':str(MAPPING.relative_to(ROOT)),'mapping_sha256':mapping_sha,'mapping_decodes':len(mapping),
            'direct_16':direct,'strengthened_6':strength,'controls':{'storage_sink_parity':parity,'components':components,'positive':positive,
            'template_sign_flip':{'source':'P0-B1','changed':True,'mutated_hash':unit_mut_hash,'original_hash':original_unit_hash},
            'M_literal_sign_flip':{'source':'P1-B1.M2','changed':True,'mutated_hash':m_mut_hash,'original_hash':original_m_hash},
            'scope':'hash sign-flips are binding controls only; no SAT/UNSAT claim about mutants'},
            'CNF_or_proof_files_written':False,'solver_calls':0,'GA_IDs_used_for_GB':False,'generation_CPU_processes':1,
            'self_RSS_cap_bytes':RSS_CAP,'peak_RSS_bytes_Darwin':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'seconds':time.monotonic()-t0,'fresh_free_bytes':free,'fresh_lane_bytes':used,
            'acceptance_status':'parent mapping/necessity review and independent GB solves/checks still required'}
    rh=new_json(OUT,result)
    print(json.dumps({'manifest_sha256':rh,'GB_base':result['GB_base'],'direct_count':16,'strength_count':6,
                      'mapping_sha256':mapping_sha,'own_names_sha256':own_names_sha,'positive_status':positive['status'],
                      'seconds':result['seconds'],'peak_RSS_bytes_Darwin':result['peak_RSS_bytes_Darwin'],
                      'solver_calls':0,'CNF_files_written':False}),flush=True)


if __name__=='__main__':
    main()
