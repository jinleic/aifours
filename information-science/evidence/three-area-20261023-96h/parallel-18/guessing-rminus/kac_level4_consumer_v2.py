"""PREPARE ONLY. A NEW parent GO is required before import/compile/execution.

V2 repairs the two returned static-audit findings only: trusted bootstrap before
core use, and settlement coverage from before output-directory claiming. The
mathematical core and certificate validation algorithms remain frozen at v1.
"""
import argparse
import copy
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
import types

HERE = Path(__file__).resolve().parent
CORE_PATH = HERE/'kac_level4_definitions_v1.py'
m = None
INPUT_ROOT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/assay-small-row-level4-001')
MANIFEST_SHA = '1872d5e87dbafcf3e4cf28705963a5b0cb3a0950b271bb6364ed12d83f6ef9da'
SETTLEMENT_SHA = 'b654d5b7ac2e181042727e92b1bfb4f9d1723fe690ea7bdad20a974f2154c82e'
DEGREES = ((2,2),(3,2),(2,3),(3,3))
EXPECTED = {(r,s,a,b) for r in (1,2,3,4) for s in (1,2,3,4) for a,b in DEGREES}
FIELDS = {'cell','open_entry_value','degree','free_dimensions','ideal_dimensions',
          'free_primitive_dimension','actual_quotient_primitive_dimension',
          'source_ideal','target_ideal','primitive_representatives',
          'quotient_affine_images','positive_coefficient_minor','status'}
STOP = False
DEADLINE = None


class ConsumerError(Exception):
    """Trusted consumer/bootstrap error; never delegated to an unverified core."""
    def __init__(self,code,detail=''):
        self.code,self.detail = code,detail
        super().__init__(code+(': '+detail if detail else ''))


def stop_request(signum, frame):
    global STOP
    STOP = True


def guard():
    if STOP:
        raise ConsumerError('COOPERATIVE_STOP')
    if DEADLINE is None:
        raise ConsumerError('DEADLINE_NOT_CONFIGURED')
    if time.monotonic() >= DEADLINE:
        raise ConsumerError('COOPERATIVE_DEADLINE')


def require(condition, code, detail=''):
    guard()
    if not condition:
        raise ConsumerError(code,detail)


def load_verified_core(path,expected_sha,identity):
    """Future admitted execution compiles ONLY the captured authenticated bytes.

    No importlib/sys.path core lookup, no producer import and no file re-read
    between authentication and compilation. All pin gates are trusted local code.
    """
    guard()
    resolved = path.resolve()
    require(resolved==CORE_PATH and path==CORE_PATH and not path.is_symlink(),
            'CORE_PATH_BINDING')
    captured = path.read_bytes()
    actual = hashlib.sha256(captured).hexdigest()
    identity.update(core_source_path=str(resolved),core_sha256=actual,
                    core_loaded_from_verified_bytes=False)
    require(actual==expected_sha,'DEFINITION_CORE_PIN')
    guard()
    module = types.ModuleType('_kac_level4_authenticated_core_v1')
    module.__file__ = str(resolved)
    module.__package__ = None
    code = compile(captured,str(resolved),'exec',dont_inherit=True,optimize=sys.flags.optimize)
    exec(code,module.__dict__)
    require(module.__file__==str(resolved),'CORE_LOADED_FILE_BINDING')
    module.__verified_source_sha256__ = actual
    identity.update(core_loaded_file=module.__file__,core_loaded_source_sha256=actual,
                    core_loaded_from_verified_bytes=True)
    guard()
    return module


def error_fields(error):
    if isinstance(error,ConsumerError):
        return error.code,error.detail
    if m is not None and isinstance(error,m.ConsumerError):
        return error.code,error.detail
    return None


def integer(value):
    return type(value) is int


def fraction(value):
    require(isinstance(value,str) and 0<len(value)<=512,'RATIONAL_ENCODING')
    try:
        result = m.Q(value)
    except (ValueError,ZeroDivisionError) as error:
        raise ConsumerError('RATIONAL_ENCODING',str(error)) from error
    require(str(result)==value,'RATIONAL_ENCODING','noncanonical rational')
    return result


def unique_object(pairs):
    result = {}
    for key,value in pairs:
        require(key not in result,'DUPLICATE_JSON_KEYS',key)
        result[key] = value
    return result


def parse_json(raw):
    require(isinstance(raw,bytes) and len(raw)<=2*1024*1024,'INPUT_SIZE')
    try:
        return json.loads(raw,object_pairs_hook=unique_object)
    except (UnicodeDecodeError,json.JSONDecodeError) as error:
        raise ConsumerError('MALFORMED_JSON',str(error)) from error


def pinned_bytes(raw,size,digest):
    require(len(raw)==size,'INPUT_SIZE')
    require(hashlib.sha256(raw).hexdigest()==digest,'INPUT_HASH')
    return raw


def filename(key):
    r,s,a,b = key
    return f'cell-{r}-{s}-degree-{a}-{b}-4.json'


def record_key(record):
    require(isinstance(record,dict),'SCHEMA')
    require(isinstance(record.get('cell'),list) and len(record['cell'])==2 and
            all(integer(v) for v in record['cell']),'SCHEMA','cell')
    require(isinstance(record.get('degree'),list) and len(record['degree'])==3 and
            all(integer(v) for v in record['degree']),'SCHEMA','degree')
    require(record['degree'][2]==4,'SCHEMA','wrong level')
    key = tuple(record['cell']+record['degree'][:2])
    require(key in EXPECTED,'SCOPE_RECORD',str(key))
    return key


def check_coverage(records):
    require(isinstance(records,list),'SCHEMA','record list')
    actual = {}
    for record in records:
        key = record_key(record)
        require(key not in actual,'COVERAGE_DUPLICATE',str(key))
        actual[key] = record
    require(set(actual)==EXPECTED,'COVERAGE_MISSING',str(sorted(EXPECTED-set(actual))))
    require(len(records)==64,'COVERAGE_COUNT')
    return actual


def parse_tensor(encoded,a,b,k,allow_zero=False,primitive_code='TENSOR_COPRODUCT'):
    require(isinstance(encoded,list) and len(encoded)<=4096,'TENSOR_ENCODING')
    result,previous = {},None
    for entry in encoded:
        require(isinstance(entry,list) and len(entry)==2,'TENSOR_ENCODING')
        word,value = entry
        require(isinstance(word,list) and len(word)==k and
                all(integer(i) and 0<=i<8 for i in word),'TENSOR_ENCODING')
        word = tuple(word)
        require(previous is None or previous<word,'TENSOR_ENCODING','duplicate/unordered word')
        previous = word
        value = fraction(value)
        require(bool(value),'TENSOR_ENCODING','explicit zero coefficient')
        result[word] = value
    require(allow_zero or bool(result),'TENSOR_ENCODING','empty basis tensor')
    converted = m.translate(result,m.OLD_TO_NEW)
    require(not converted or m.full_degree(converted)==(a,b,k),'TENSOR_DEGREE')
    require(not m.coproduct(converted),primitive_code)
    return result,converted


def parse_polynomial(encoded,n,r,s):
    require(isinstance(encoded,list) and len(encoded)<=(n+1)*(n+2)//2,'POLYNOMIAL_ENCODING')
    result,previous = {},None
    for entry in encoded:
        require(isinstance(entry,list) and len(entry)==2,'POLYNOMIAL_ENCODING')
        exponent,value = entry
        require(isinstance(exponent,list) and len(exponent)==2 and
                all(integer(i) and i>=0 for i in exponent) and sum(exponent)<=n,
                'POLYNOMIAL_ENCODING')
        exponent = tuple(exponent)
        require(previous is None or previous<exponent,'POLYNOMIAL_ENCODING')
        require((r==4 or exponent[0]==0) and (s==4 or exponent[1]==0),
                'FIXED_PARAMETER_DEPENDENCE')
        previous = exponent
        value = fraction(value)
        require(bool(value),'POLYNOMIAL_ENCODING')
        result[exponent] = value
    return result


def same_ideal(encoded,whole,free,a,b,k):
    require(isinstance(encoded,list) and len(encoded)<=1008,'IDEAL_ENCODING')
    converted = []
    for vector in encoded:
        unused,value = parse_tensor(vector,a,b,k,primitive_code='IDEAL_TENSOR_COPRODUCT')
        require(free.contains(value),'IDEAL_FREE_MEMBERSHIP')
        require(whole.contains(value),'IDEAL_SPAN','supplied row outside whole generated ideal')
        converted.append(value)
    supplied = m.LinearSpan(converted)
    require(supplied.dimension==len(converted),'IDEAL_DEPENDENT_BASIS')
    require(supplied.dimension==whole.dimension and
            all(supplied.contains(vector) for vector in whole.rows),'IDEAL_SPAN',
            'supplied basis omits generated ideal')
    return converted


def validate_record(record,context,key,swap_original_row=False):
    require(set(record)==FIELDS,'SCHEMA','unsupported/missing record field')
    require(record_key(record)==key,'SCOPE_RECORD')
    require(integer(record['open_entry_value']) and record['open_entry_value']==4,
            'SCHEMA','category4 must mean4+variable')
    require(record['status']=='CERTIFICATE_CANDIDATE','SCHEMA','unexpected producer status')
    for name in ('free_dimensions','ideal_dimensions'):
        require(isinstance(record[name],list) and len(record[name])==2 and
                all(integer(v) and 0<=v<=1008 for v in record[name]),'SCHEMA',name)
    for name in ('free_primitive_dimension','actual_quotient_primitive_dimension'):
        require(integer(record[name]) and 0<=record[name]<=8,'SCHEMA',name)
    r,s,a,b = key
    model = context.model
    source,target = model.free(a,b,4),model.free(a,b,3)
    ideal4,ideal3 = context.ideal(a,b,4),context.ideal(a,b,3)
    supplied4 = same_ideal(record['source_ideal'],ideal4,source,a,b,4)
    same_ideal(record['target_ideal'],ideal3,target,a,b,3)
    require(record['free_dimensions']==[source.dimension,target.dimension],
            'FREE_DIMENSION_CLAIM')
    require(record['ideal_dimensions']==[ideal4.dimension,ideal3.dimension],
            'IDEAL_DIMENSION_CLAIM')
    quotient_dimension,free_dimension = context.lowest(a,b)
    require(record['free_primitive_dimension']==free_dimension,'FREE_LOWEST_CLAIM')
    require(record['actual_quotient_primitive_dimension']==quotient_dimension,
            'QUOTIENT_LOWEST_CLAIM')
    require(isinstance(record['primitive_representatives'],list) and
            len(record['primitive_representatives'])<=8,'PRIMITIVE_ENCODING')
    primitive = []
    for encoded in record['primitive_representatives']:
        unused,vector = parse_tensor(encoded,a,b,4,primitive_code='SOURCE_TENSOR_COPRODUCT')
        require(source.contains(vector),'FULL_SOURCE_MEMBERSHIP')
        require(not model.act(2,vector) and not model.act(3,vector),'FREE_LOWEST_VECTOR')
        primitive.append(vector)
    require(len(primitive)==quotient_dimension,'QUOTIENT_LOWEST_COVERAGE')
    require(m.LinearSpan([ideal4.normal(vector) for vector in primitive]).dimension==quotient_dimension,
            'QUOTIENT_LOWEST_INDEPENDENCE')
    # WHOLE source ideal, not only producer-selected relations; coefficientwise in the cell.
    for vector in ideal4.rows:
        for component in context.affine_cell(model.raw_lowering(vector,a,b),swap_original_row):
            require(ideal3.contains(component),'RAW_ORIGINAL_ROW','whole ideal is not D3-stable')
    for vector in supplied4+primitive:
        model.terminal_check(vector)
    old_target_ideal = m.LinearSpan([m.translate(vector,m.NEW_TO_OLD) for vector in ideal3.rows])
    supplied_images = record['quotient_affine_images']
    require(isinstance(supplied_images,list) and len(supplied_images)==quotient_dimension,
            'IMAGE_COVERAGE')
    reconstructed = []
    for vector,encoded_triple in zip(primitive,supplied_images):
        require(isinstance(encoded_triple,list) and len(encoded_triple)==3,'IMAGE_ENCODING')
        raw = context.affine_cell(model.raw_lowering(vector,a,b),swap_original_row)
        triple = []
        for actual,encoded in zip(raw,encoded_triple):
            require(target.contains(actual),'RAW_TARGET_MEMBERSHIP')
            supplied,converted = parse_tensor(encoded,a,b,3,allow_zero=True,
                                              primitive_code='IMAGE_TENSOR_COPRODUCT')
            require(target.contains(converted),'IMAGE_FREE_MEMBERSHIP')
            require(not any(supplied.get(pivot) for pivot in old_target_ideal.pivots),
                    'QUOTIENT_NORMAL_FORM')
            normalized = old_target_ideal.normal(m.translate(actual,m.NEW_TO_OLD))
            require(normalized==supplied,'RAW_ORIGINAL_ROW','affine quotient image mismatch')
            triple.append(normalized)
        reconstructed.append(tuple(triple))
    minor = record['positive_coefficient_minor']
    require(isinstance(minor,dict) and {'rows','determinant','orientation'}<=set(minor) and
            set(minor)<={'rows','determinant','orientation','attempt'},'MINOR_SCHEMA')
    if 'attempt' in minor:
        require(integer(minor['attempt']) and 0<=minor['attempt']<24,'MINOR_SCHEMA')
    require(integer(minor['orientation']) and minor['orientation'] in (-1,1),'MINOR_SCHEMA')
    require(isinstance(minor['rows'],list) and len(minor['rows'])==quotient_dimension,
            'MINOR_ROW_COUNT')
    selected = []
    for word in minor['rows']:
        require(isinstance(word,list) and len(word)==3 and
                all(integer(i) and 0<=i<8 for i in word),'MINOR_COORDINATE')
        word = tuple(word)
        converted = m.translate({word:m.Q(1)},m.OLD_TO_NEW)
        require(m.full_degree(converted)==(a,b,3),'MINOR_COORDINATE')
        require(word not in selected and word not in old_target_ideal.pivots,'MINOR_COORDINATE')
        selected.append(word)
    matrix = []
    for word in selected:
        matrix.append([{exponent:component.get(word,m.Q(0)) for exponent,component in
                        zip(((0,0),(1,0),(0,1)),triple) if component.get(word)}
                       for triple in reconstructed])
    determinant = m.bareiss_determinant(matrix)
    expected = parse_polynomial(minor['determinant'],quotient_dimension,r,s)
    require(determinant==expected,'DETERMINANT_IDENTITY')
    sign = minor['orientation']
    require(sign*determinant.get((0,0),m.Q(0))>0 and
            all(sign*value>=0 for value in determinant.values()),'DETERMINANT_POSITIVITY')
    return {'cell':[r,s],'degree':[a,b,4],'free_dimensions':[source.dimension,target.dimension],
            'whole_ideal_dimensions':[ideal4.dimension,ideal3.dimension],
            'free_lowest_dimension':free_dimension,'whole_quotient_lowest_dimension':quotient_dimension,
            'determinant_terms':len(determinant),'oriented_constant':str(sign*determinant[(0,0)]),
            'terminal_tensors_checked':len(supplied4)+len(primitive),
            'status':'EXACT_FINITE_PREMISES_RECONSTRUCTED'}


def read_bundle(manifest_path):
    manifest_bytes = manifest_path.read_bytes()
    require(hashlib.sha256(manifest_bytes).hexdigest()==MANIFEST_SHA,'MANIFEST_HASH')
    manifest = parse_json(manifest_bytes)
    require(set(manifest)=={'status','input_root','expected_certificate_count','files'},'MANIFEST_SCHEMA')
    require(manifest['status']=='METADATA_ONLY_NO_CERTIFICATE_VALIDATION' and
            manifest['input_root']==str(INPUT_ROOT) and manifest['expected_certificate_count']==64,
            'MANIFEST_SCOPE')
    entries = manifest['files']
    require(isinstance(entries,list) and len(entries)==66,'MANIFEST_SCOPE')
    wanted = {filename(key) for key in EXPECTED}|{'launch.json','settlement.json'}
    inventory = {}
    for entry in entries:
        require(isinstance(entry,dict) and set(entry)=={'name','bytes','sha256'},'MANIFEST_SCHEMA')
        name = entry['name']
        require(name in wanted and name not in inventory,'MANIFEST_INVENTORY')
        require(integer(entry['bytes']) and 0<entry['bytes']<=2*1024*1024,'INPUT_SIZE')
        require(isinstance(entry['sha256'],str) and len(entry['sha256'])==64 and
                all(c in '0123456789abcdef' for c in entry['sha256']),'MANIFEST_SCHEMA')
        inventory[name] = entry
    require(set(inventory)==wanted,'MANIFEST_INVENTORY')
    # Filesystem listing is refusal-only. Required inputs come exclusively from the manifest.
    require(set(os.listdir(INPUT_ROOT))==wanted,'UNLISTED_OR_MISSING_INPUT')
    raw,parsed,total = {},{},0
    for name,entry in inventory.items():
        guard()
        path = INPUT_ROOT/name
        require(path.is_file() and not path.is_symlink(),'INPUT_NOT_REGULAR')
        value = path.read_bytes()
        total += len(value)
        require(total<=32*1024*1024,'INPUT_TOTAL_SIZE')
        raw[name] = pinned_bytes(value,entry['bytes'],entry['sha256'])
    # All hashes are checked BEFORE any certificate algebra or JSON-derived mathematics.
    for name,value in raw.items():
        parsed[name] = parse_json(value)
    require(inventory['settlement.json']['sha256']==SETTLEMENT_SHA,'SETTLEMENT_PIN')
    settlement = parsed['settlement.json']
    require(settlement.get('status')=='COMPLETE_CERTIFICATE_CANDIDATES','SETTLEMENT_STATUS')
    records = [parsed[filename(key)] for key in sorted(EXPECTED)]
    check_coverage(records)
    check_coverage(settlement.get('records'))
    require(all(record.get('status')=='CERTIFICATE_CANDIDATE' for record in settlement['records']),
            'SETTLEMENT_STATUS')
    for key,record in zip(sorted(EXPECTED),records):
        require(record_key(record)==key,'FILENAME_SCOPE')
    return records,raw,inventory


def expect_rejection(name,operation,code,payload=None):
    try:
        operation()
    except Exception as error:
        fields = error_fields(error)
        if fields is None:
            raise
        observed,unused = fields
        require(observed==code,'CONTROL_WRONG_REASON',name+' -> '+observed)
        encoded = json.dumps(payload,sort_keys=True,separators=(',',':')).encode() if payload is not None else b''
        return {'name':name,'expected_reason':code,'observed_reason':observed,
                'mutation_sha256':hashlib.sha256(encoded).hexdigest(),'status':'REJECTED_AS_INTENDED'}
    raise ConsumerError('CONTROL_SURVIVED',name)


def mutation_controls(records,raw,context):
    indexed = check_coverage(records)
    key = (1,4,3,3)
    original = indexed[key]
    outcomes = []
    def run_mutation(name,mutator,code):
        changed = copy.deepcopy(original)
        mutator(changed)
        outcomes.append(expect_rejection(name,lambda:validate_record(changed,context,key),code,changed))
    def tensor_mutation(record):
        term = record['primitive_representatives'][0][0]
        value = fraction(term[1])
        term[1] = str(value+(m.Q(2) if value==-1 else m.Q(1)))
    run_mutation('altered_source_tensor',tensor_mutation,'SOURCE_TENSOR_COPRODUCT')
    run_mutation('omitted_source_ideal_row',lambda rec:rec['source_ideal'].pop(0),'IDEAL_SPAN')
    run_mutation('omitted_target_ideal_row',lambda rec:rec['target_ideal'].pop(0),'IDEAL_SPAN')
    def image_mutation(record):
        component = next(component for triple in record['quotient_affine_images'] for component in triple if component)
        for entry in component:
            entry[1] = str(2*fraction(entry[1]))
    run_mutation('altered_lowering_image',image_mutation,'RAW_ORIGINAL_ROW')
    outcomes.append(expect_rejection('transposed_original_nonsymmetric_row',
        lambda:validate_record(copy.deepcopy(original),context,key,swap_original_row=True),
        'RAW_ORIGINAL_ROW',{'cell':[1,4],'row_mutation':'swap original r,s coefficients'}))
    def determinant_mutation(record):
        term = record['positive_coefficient_minor']['determinant'][0]
        value = fraction(term[1])
        term[1] = str(value+(m.Q(2) if value==-1 else m.Q(1)))
    run_mutation('determinant_coefficient',determinant_mutation,'DETERMINANT_IDENTITY')
    run_mutation('determinant_orientation',lambda rec:rec['positive_coefficient_minor'].__setitem__(
        'orientation',-rec['positive_coefficient_minor']['orientation']),'DETERMINANT_POSITIVITY')
    run_mutation('open_category_is_not_a_point',lambda rec:rec.__setitem__('open_entry_value',3),'SCHEMA')
    missing_degree = records[1:]
    outcomes.append(expect_rejection('missing_degree',lambda:check_coverage(missing_degree),
                                    'COVERAGE_MISSING',{'omitted':record_key(records[0])}))
    missing_cell = [record for record in records if record['cell']!=[1,1]]
    outcomes.append(expect_rejection('missing_cell',lambda:check_coverage(missing_cell),
                                    'COVERAGE_MISSING',{'omitted_cell':[1,1]}))
    outcomes.append(expect_rejection('duplicate_degree',lambda:check_coverage(records+[copy.deepcopy(records[0])]),
                                    'COVERAGE_DUPLICATE',{'duplicate':record_key(records[0])}))
    copied_cell = [copy.deepcopy(record) for record in records if record['cell']==[1,1]]
    outcomes.append(expect_rejection('duplicate_cell',lambda:check_coverage(records+copied_cell),
                                    'COVERAGE_DUPLICATE',{'duplicate_cell':[1,1]}))
    sample = raw[filename(key)].rstrip()
    outcomes.append(expect_rejection('truncated_artifact',lambda:parse_json(sample[:-1]),'MALFORMED_JSON',
                                    {'truncated_bytes':len(sample)-1}))
    outcomes.append(expect_rejection('duplicate_json_key',lambda:parse_json(b'{"x":1,"x":2}'),
                                    'DUPLICATE_JSON_KEYS',{'fixture':'duplicate-key JSON'}))
    wrong_bytes = bytes([sample[0]^1])+sample[1:]
    outcomes.append(expect_rejection('tampered_input_bytes',
        lambda:pinned_bytes(wrong_bytes,len(sample),hashlib.sha256(sample).hexdigest()),
        'INPUT_HASH',{'tamper':'one byte, unchanged size'}))
    # Audited bootstrap regression: the ACTUAL loader must stop before compilation/core use.
    outcomes.append(expect_rejection('unauthenticated_core_stops_before_load',
        lambda:load_verified_core(CORE_PATH,'0'*64,{}),'DEFINITION_CORE_PIN',
        {'fixture':'wrong expected core SHA; no core compilation/import permitted'}))
    return outcomes


def main():
    global DEADLINE,m
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=int,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--source-sha',required=True)
    parser.add_argument('--core-sha',required=True)
    parser.add_argument('--interpreter-sha',required=True)
    args = parser.parse_args()
    if not 1<=args.seconds<=600:
        parser.error('cooperative bound must be1..600 seconds')
    started = time.monotonic()
    DEADLINE = started+args.seconds
    output,claimed = None,False
    status,checks,controls,error,inventory = 'ERROR',[],[],None,{}
    identity = {'argv':sys.argv,'interpreter':sys.executable,'internal_seconds':args.seconds,
                'processes':1,'threads':1,'children':0,'optimization_level':sys.flags.optimize}
    try:
        # Install cooperative handlers BEFORE any output directory can be claimed.
        signal.signal(signal.SIGTERM,stop_request)
        signal.signal(signal.SIGINT,stop_request)
        identity.update(pid=os.getpid(),pgid=os.getpgrp(),cwd=os.getcwd(),
                        observed_start=datetime.datetime.now().astimezone().isoformat())
        guard()
        output = args.output.resolve()
        require(output!=HERE and HERE in output.parents,'OUTPUT_SCOPE')
        output.mkdir(exist_ok=False)
        claimed = True
        guard()
        # Trusted gates do not call or import ANY core implementation.
        source = Path(__file__).read_bytes()
        identity['source_sha256'] = hashlib.sha256(source).hexdigest()
        require(identity['source_sha256']==args.source_sha,'CONSUMER_SOURCE_PIN')
        interpreter = Path(sys.executable).read_bytes()
        identity['interpreter_sha256'] = hashlib.sha256(interpreter).hexdigest()
        require(identity['interpreter_sha256']==args.interpreter_sha,'INTERPRETER_PIN')
        m = load_verified_core(CORE_PATH,args.core_sha,identity)
        require(m.__file__==identity['core_source_path'] and
                m.__verified_source_sha256__==identity['core_sha256'],'CORE_LOADED_BINDING')
        m.configure_guard(guard)
        with (output/'launch.json').open('x') as destination:
            json.dump(identity,destination,indent=2)
        records,raw,inventory = read_bundle(HERE/'kac-level4-input-pins-v1.json')
        model = m.DefinitionModel()
        indexed = check_coverage(records)
        control_context = None
        for r in (1,2,3,4):
            for s in (1,2,3,4):
                context = m.CellModel(model,r,s)
                for a,b in DEGREES:
                    key = (r,s,a,b)
                    result = validate_record(indexed[key],context,key)
                    checks.append(result)
                    with (output/('checked-'+filename(key))).open('x') as destination:
                        json.dump(result,destination,indent=2)
                    print(json.dumps({'checked':key,'quotient_lowest':result['whole_quotient_lowest_dimension']}),flush=True)
                if (r,s)==(1,4):
                    control_context = context
        require(control_context is not None,'CONTROL_CONTEXT_MISSING')
        controls = mutation_controls(records,raw,control_context)
        require(len(checks)==64 and len(controls)==16,'FINAL_COVERAGE_OR_CONTROLS')
        require({tuple(x['cell']+x['degree'][:2]) for x in checks}==EXPECTED,'FINAL_COVERAGE')
        status = 'COMPLETE_INDEPENDENT_FINITE_RECONSTRUCTION'
    except Exception as exc:
        fields = error_fields(exc)
        if fields is not None:
            code,detail = fields
            error = {'type':'ConsumerError','code':code,'detail':detail}
            status = 'INCOMPLETE' if code in ('COOPERATIVE_STOP','COOPERATIVE_DEADLINE') else 'REJECTED'
        else:
            error = {'type':type(exc).__name__,'detail':str(exc)}
            status = 'ERROR'
    finally:
        # Settlement does not call a guard/core, so it also works before core loading,
        # after a deadline, or after a source/interpreter/launch initialization failure.
        metadata_errors = []
        try:
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        except Exception as exc:
            rss = None
            metadata_errors.append({'field':'maxrss','type':type(exc).__name__,'detail':str(exc)})
        try:
            finish = datetime.datetime.now().astimezone().isoformat()
        except Exception as exc:
            finish = None
            metadata_errors.append({'field':'observed_finish','type':type(exc).__name__,'detail':str(exc)})
        receipt = {'status':status,'mathematical_status':status,'identity':identity,
            'records':checks,'controls':controls,'error':error,'input_pins':inventory,
            'output_claimed':claimed,'observed_finish':finish,'observed_finish_unix':time.time(),
            'elapsed_seconds':time.monotonic()-started,'maxrss_native':rss,
            'maxrss_units':'bytes on darwin; KiB on Linux; informational, not enforced',
            'metadata_errors':metadata_errors,'formal_proof':False,'full_band_accepted':False,
            'novelty_cleared':False,
            'scope':'Finite64-certificate premises only; inherited lower-level/invariant/import composition remains separate.'}
        if metadata_errors:
            status = 'SETTLEMENT_METADATA_ERROR'
            receipt['status'] = status
        file_written = False
        if claimed:
            try:
                with (output/'settlement.json').open('x') as destination:
                    json.dump(receipt,destination,indent=2)
                file_written = True
            except Exception as exc:
                status = 'SETTLEMENT_IO_ERROR'
                receipt['status'] = status
                receipt['settlement_write_error'] = {'type':type(exc).__name__,'detail':str(exc)}
        # An unavailable filesystem cannot be promised a file receipt: stdout records
        # the complete fallback and forces nonzero status instead of hiding that failure.
        if not file_written:
            print(json.dumps({'settlement_fallback':receipt}),flush=True)
        print(json.dumps({'status':status,'checked':len(checks),'controls':len(controls),
                          'settlement_file_written':file_written,'error':error}),flush=True)
    return 0 if status=='COMPLETE_INDEPENDENT_FINITE_RECONSTRUCTION' and file_written else 2


if __name__=='__main__':
    raise SystemExit(main())
