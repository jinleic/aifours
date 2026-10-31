"""Validation of a parent GO record; this module does not grant a GO."""
import math

class AdmissionError(Exception): pass

def require(condition, code, detail=''):
    if not condition: raise AdmissionError(f'{code}: {detail}')

def _sha(value):
    return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)

def validate(go, expected, invocation):
    keys={'schema_version','kind','status','run_id','candidate_sha256','bundle_path','bundle_sha256',
          'author_verifier_sha256','runtime_sha256','obligation_engine_sha256','environment_guard_sha256',
          'source_binding_sha256','gate_validator_sha256','local_hardened_sha256','environment_manifest_path','environment_manifest_sha256',
          'source_manifest_path','source_manifest_sha256',
          'python_executable_sha256','seconds','rss_bytes','output_bytes','invocation',
          'reviews','independent_checker','hardening_review','prior_art_scope','settlement','obligations'}
    require(isinstance(go,dict) and set(go)==keys, 'GO_SCHEMA')
    require(type(go['schema_version']) is int and go['schema_version']==1 and go['kind']=='PH7_GLOBAL_EXECUTABLE_GO_V1' and True, 'GO_NOT_AUTHORIZED')
    run=go['run_id']; require(isinstance(run,str) and run and len(run)<=48 and all(c.isalnum() or c in '-_' for c in run), 'GO_RUN_ID')
    for field in ('candidate_sha256','author_verifier_sha256','runtime_sha256','obligation_engine_sha256','environment_guard_sha256','source_binding_sha256','gate_validator_sha256','local_hardened_sha256'):
        require(go[field]==expected[field], 'GO_CODE_OR_SCOPE_PIN', field)
    for field in ('bundle_sha256','environment_manifest_sha256','source_manifest_sha256','python_executable_sha256'):
        require(_sha(go[field]), 'GO_INVALID_SHA', field)
    for field in ('bundle_path','environment_manifest_path','source_manifest_path'):
        require(isinstance(go[field],str) and go[field].startswith('/'), 'GO_ABSOLUTE_INPUT_PATH', field)
    require(type(go['seconds']) is int and 0<go['seconds']<=14400, 'GO_TIME_BOUND')
    require(type(go['rss_bytes']) is int and 0<go['rss_bytes']<=8589934592, 'GO_RSS_BOUND')
    require(type(go['output_bytes']) is int and 0<go['output_bytes']<=536870912, 'GO_OUTPUT_BOUND')
    require(go['invocation']==invocation, 'GO_INVOCATION_MISMATCH')
    require(go['obligations']==['QO','HO','NB','MC','R3','SB','MP'], 'GO_OBLIGATION_SET')
    reviews=go['reviews']; require(isinstance(reviews,dict) and set(reviews)=={'f202','f203','f223'}, 'GO_REVIEW_SET')
    required_reviews={'f202':('NO_MAJOR',expected['candidate_sha256']),
                      'f203':('THREE_MAJORS_RETAINED',expected['candidate_sha256']),
                      'f223':('M2_M3_REPAIR_SUPPORTED',expected['repair_sha256'])}
    for name,rec in reviews.items():
        require(isinstance(rec,dict) and set(rec)=={'verdict','review_sha256','scope_sha256'}, 'GO_REVIEW_SCHEMA',name)
        verdict,scope=required_reviews[name]
        require(rec['verdict']==verdict and _sha(rec['review_sha256']) and rec['scope_sha256']==scope, 'GO_REVIEW_NOT_CLEARED',name)
    checker=go['independent_checker']
    require(isinstance(checker,dict) and set(checker)=={'status','code_sha256','definition_first'}, 'GO_INDEPENDENT_SCHEMA')
    require(checker['status']=='READY' and checker['definition_first'] is True and _sha(checker['code_sha256']), 'GO_INDEPENDENT_NOT_READY')
    require(checker['code_sha256'] not in (expected['author_verifier_sha256'],expected['obligation_engine_sha256']), 'GO_CHECKER_NOT_DISTINCT')
    hard=go['hardening_review']
    require(isinstance(hard,dict) and set(hard)=={'verdict','report_sha256','verifier_sha256'}, 'GO_HARDENING_SCHEMA')
    require(hard['verdict']=='NO_MAJOR' and _sha(hard['report_sha256']) and hard['verifier_sha256']==expected['author_verifier_sha256'], 'GO_HARDENING_NOT_CLEARED')
    source=go['prior_art_scope']
    require(isinstance(source,dict) and set(source)=={'status','scope_sha256'}, 'GO_PRIOR_ART_SCHEMA')
    require(source['status'] in ('PARENT_AUTHORIZED','PARENT_EXPLICITLY_DEFERRED') and _sha(source['scope_sha256']), 'GO_PRIOR_ART_NOT_DISPOSITIONED')
    require(go['settlement']=={'timeout':'INTERNAL_COOPERATIVE','tool_timeout_seconds':0,'auto_retry':False,'on_failure':'INCOMPLETE'}, 'GO_SETTLEMENT')
    return go
