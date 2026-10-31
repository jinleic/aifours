"""Fail-closed post-run consumer for an author GLOBAL result.

This module does not authenticate a parent by itself. Its caller MUST obtain
an independently authenticated, parent-controlled settlement pin and policy
from the separately admitted launcher/supervisor; caller-provided hashes alone
are not authority. This module has no CLI and never promotes a scientific
result: any absent, malformed, incomplete or mismatched item is UNKNOWN.
"""
import hashlib
import json
from pathlib import Path

COVERS=('QO','HO','NB','MC','R3','SB','MP')

class Rejected(Exception): pass

def need(condition, code):
    if not condition: raise Rejected(code)

def digest(data): return hashlib.sha256(data).hexdigest()

def decode(data):
    need(isinstance(data,bytes),'MISSING_OR_NONBYTE_INPUT')
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'DUPLICATE_JSON_KEY');out[k]=v
        return out
    def bad(c):raise Rejected('NONFINITE_JSON')
    try:return json.loads(data,object_pairs_hook=pairs,parse_constant=bad)
    except (UnicodeDecodeError,json.JSONDecodeError) as exc:raise Rejected('INVALID_JSON') from exc

def sha_text(value):
    return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)

def consume(receipt_bytes, result_bytes, supervisor_bytes, trusted):
    """Return AUTHOR_COMPLETE_BOUND_NOT_ADOPTED or UNKNOWN with a reason.

    `trusted` must be assembled from the OUT-OF-BAND parent-controlled launch
    policy and independently attested terminal observation, not from the
    author result/receipt and not from user-provided self-hashes. The calling
    launcher must prove that provenance before invoking this routine.
    """
    try:
        required={'go_sha256','candidate_sha256','repair_sha256','face_sha256',
                  'bundle_sha256','entry_sha256','result_name','supervisor_sha256'}
        need(isinstance(trusted,dict) and set(trusted)==required,'TRUSTED_BINDING_SCHEMA')
        for key in required-{'result_name'}:need(sha_text(trusted[key]),'TRUSTED_BINDING_HASH')
        name=trusted['result_name']
        need(isinstance(name,str) and name and Path(name).name==name and name not in ('.','..'),'TRUSTED_RESULT_NAME')
        need(isinstance(supervisor_bytes,bytes) and digest(supervisor_bytes)==trusted['supervisor_sha256'],'SUPERVISOR_PIN')
        supervisor=decode(supervisor_bytes);receipt=decode(receipt_bytes);result=decode(result_bytes)
        need(isinstance(supervisor,dict) and isinstance(receipt,dict) and isinstance(result,dict),'RECORD_TYPE')
        need(supervisor.get('kind')=='PH7_PARENT_TERMINAL_OBSERVATION_V1','SUPERVISOR_KIND')
        need(supervisor.get('terminal_observed') is True,'PROCESS_NOT_OBSERVED')
        need(type(supervisor.get('exit_code')) is int and supervisor['exit_code']==0,'PROCESS_EXIT_NOT_ZERO')
        need(supervisor.get('go_sha256')==trusted['go_sha256'],'SUPERVISOR_GO')
        need(supervisor.get('entry_sha256')==trusted['entry_sha256'],'SUPERVISOR_ENTRY')
        need(supervisor.get('receipt_sha256')==digest(receipt_bytes),'SUPERVISOR_RECEIPT_HASH')
        need(supervisor.get('result_sha256')==digest(result_bytes),'SUPERVISOR_RESULT_HASH')
        need(type(supervisor.get('pid')) is int and supervisor['pid']>0,'SUPERVISOR_PID')
        need(receipt.get('pid')==supervisor['pid'],'PROCESS_IDENTITY_MISMATCH')
        need(receipt.get('status')=='AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','RECEIPT_NOT_COMPLETE')
        for name_key in ('go_sha256','candidate_sha256','repair_sha256','face_sha256','bundle_sha256'):
            need(receipt.get(name_key)==trusted[name_key],'RECEIPT_BINDING_'+name_key)
        need(receipt.get('author_verifier_sha256')==trusted['entry_sha256'],'RECEIPT_ENTRY')
        need(receipt.get('result_name')==trusted['result_name'],'RECEIPT_RESULT_NAME')
        need(receipt.get('result_sha256')==digest(result_bytes),'RECEIPT_RESULT_HASH')
        need(result.get('status')=='AUTHOR_GLOBAL_COVERS_COMPLETE_UNADOPTED','RESULT_NOT_COMPLETE')
        need(result.get('scope_sha256')==trusted['candidate_sha256'],'RESULT_SCOPE')
        for name_key in ('repair_sha256','face_sha256','bundle_sha256','go_sha256'):
            need(result.get(name_key)==trusted[name_key],'RESULT_BINDING_'+name_key)
        counts=result.get('counts');need(isinstance(counts,dict) and set(counts)==set(COVERS),'RESULT_COVER_SET')
        for cover in COVERS:
            c=counts[cover]
            need(isinstance(c,dict) and c and all(type(n) is int and n>0 for n in c.values()),'RESULT_EMPTY_OR_INVALID_COVER')
        need(receipt.get('counts')==counts,'RECEIPT_RESULT_COUNTS')
        return {'status':'AUTHOR_COMPLETE_BOUND_NOT_ADOPTED','reason':'parent-observed zero exit and matching terminal receipt/result',
                'promotion':'independent definition-first replay and parent disposition remain required'}
    except (Rejected,KeyError,TypeError,ValueError) as exc:
        return {'status':'AUTHOR_COMPLETE_BOUND_NOT_ADOPTED','reason':str(exc),'promotion':'NO'}

if __name__=='__main__':
    raise SystemExit('CONSUMER_REQUIRES_AUTHENTICATED_PARENT_CALLER; no standalone approval CLI')
