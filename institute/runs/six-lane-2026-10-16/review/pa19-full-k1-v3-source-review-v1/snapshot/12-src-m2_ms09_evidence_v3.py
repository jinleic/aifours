#!/usr/bin/env python3
"""Fail-closed proof-flag/input-identity primitives for the new ms09 full-B inventory.
Only explicitly known staged schemas11..15 are supported; there is NO unknown-revision fallback, empty-cover
acceptance or SAT-to-UNSAT inference. Mathematical input SHA is provided by the frozen constructor recipe/pin
and is independently recomputable. Calibration proof validity is separate from parent permission to consume it.
"""
import hashlib
import json
import re
from pathlib import Path

SHA = re.compile(r'[0-9a-f]{64}\Z')
KNOWN_STAGED = (11,12,13,14,15)
KISSAT = '/opt/homebrew/bin/kissat'
CADICAL = '/opt/homebrew/bin/cadical'


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def is_int(v):
    return type(v) is int


def proof_errors(r,expected):
    if not isinstance(r,dict):
        return ['record is not an object']
    if not isinstance(expected,dict) or not all(is_int(expected.get(k)) for k in ('multiset','b_index','native_limit','cnf_bytes')):
        return ['expected formula identity/counts are missing or not integers']
    ei = expected.get('indices')
    if ei is not None and not (isinstance(ei,list) and len(ei) == 2 and all(is_int(v) for v in ei) and 0 <= ei[0] <= ei[1]):
        return ['expected interval is not a valid exact integer pair']
    if not isinstance(expected.get('cnf_sha256'),str) or SHA.fullmatch(expected['cnf_sha256']) is None or expected['cnf_bytes'] <= 0:
        return ['expected numeric formula SHA/size is invalid']
    e = []
    def need(ok,message):
        if not ok:
            e.append(message)
    need(is_int(r.get('stream_check_revision')) and r['stream_check_revision'] in KNOWN_STAGED,'unsupported/missing staged revision')
    need(r.get('staged') is True,'not a staged record')
    need(r.get('status') == 'UNSAT','not UNSAT (SAT is a veto, UNKNOWN stays open)')
    need(is_int(r.get('solver_rc')) and r['solver_rc'] == 20 and r.get('solver_stop') == 'self','solver did not self-exit20')
    for key in ('checked','drat_trim_verified','reader_ok','replay_ok','replay_sha256_matches'):
        need(r.get(key) is True,'required true flag: '+key)
    for key in ('checker_interrupted','aborted_by_sigterm'):
        need(r.get(key) is False,'required false flag: '+key)
    need(not r.get('admission_denied') and not r.get('proof_cap_hit'),'admission refusal/proof cap')
    need('lratstrict_verified' not in r,'lratstrict-only/mixed record not eligible')
    need(r.get('drat_trim_binary') == 'tools/drat-trim/drat-trim','wrong native checker identity')
    dt = r.get('drat_trim') or {}
    need(isinstance(dt,dict) and type(dt.get('rc')) is int and dt['rc'] == 0 and dt.get('stop') == 'self','drat-trim did not self-exit0')
    need(isinstance(dt,dict) and dt.get('s_lines') == ['s VERIFIED'] and dt.get('says_verified') is True,'checker verdict not exactly s VERIFIED')
    n = r.get('drat_bytes')
    ph = r.get('drat_sha256')
    need(is_int(n) and n >= 0 and isinstance(ph,str) and SHA.fullmatch(ph) is not None,'invalid streamed proof count/SHA')
    replay = r.get('replay') or {}
    need(isinstance(replay,dict) and replay.get('ok') is True and replay.get('error') is None,'replay failed/missing')
    need(isinstance(replay,dict) and is_int(replay.get('bytes')) and replay['bytes'] == n and replay.get('sha256') == ph,'delivered proof bytes/SHA differ')
    need(isinstance(r.get('cnf_sha256'),str) and SHA.fullmatch(r['cnf_sha256']) is not None,'invalid CNF SHA')
    need(r.get('cnf_sha256') == expected.get('cnf_sha256'),'CNF SHA not exact expected formula')
    need(is_int(r.get('cnf_bytes')) and r['cnf_bytes'] == expected.get('cnf_bytes') and r['cnf_bytes'] > 0,'CNF byte count differs')
    for key in ('multiset','b_index'):
        need(is_int(r.get(key)) and r[key] == expected[key],'identity differs: '+key)
    need(r.get('encoder') == expected['encoder'],'wrong encoder identity')
    idx = expected.get('indices')
    if idx is None:
        need('indices' not in r,'direct record unexpectedly names a subcase')
        need(r.get('generator') == 'gen_skel_b.py','direct generator differs')
    else:
        need(isinstance(r.get('indices'),list) and len(r['indices']) == 2 and all(is_int(v) for v in r['indices']) and r['indices'] == idx,'wrong batch indices')
    limit = expected['native_limit']
    tail = '; binary DRAT staged (zstd-1 in memory) then drat-trim -i -t 1200'
    kline = '%s -q -f --seed=1 --time=%d CNF PROOF%s' % (KISSAT,limit,tail)
    cline = '%s -q -t %d CNF PROOF%s' % (CADICAL,limit,tail)
    allowed = [kline] if expected.get('kissat_only') else [kline,cline]
    need(r.get('solver') in allowed,'solver command/limit differs')
    info = r.get('solver_info') or {}
    target_info = {'version':'kissat 4.0.4 (/opt/homebrew/bin/kissat)','seed':'--seed=1'} if r.get('solver') == kline else {'version':'cadical 3.0.1 (/opt/homebrew/bin/cadical)','seed':'default (no --seed option given)'}
    need(info == target_info and r.get('check_budget') == 1200,'solver version/seed/check budget differs')
    return e


def inspect(path,expected,frozen_sha=None):
    p = Path(path)
    try: raw = p.read_bytes()
    except FileNotFoundError: return {'state':'MISSING','errors':['missing required record'],'sat':False}
    except OSError as exc: return {'state':'INTEGRITY_VETO','errors':['unreadable record: '+repr(exc)],'sat':False}
    h = hashlib.sha256(raw).hexdigest()
    try: r = json.loads(raw)
    except (ValueError,UnicodeError) as exc:
        return {'state':'INTEGRITY_VETO','errors':['invalid JSON: '+repr(exc)],'sha256':h,'sat':False}
    if not isinstance(r,dict):
        return {'state':'INTEGRITY_VETO','errors':['record is not an object'],'sha256':h,'sat':False,'record':r}
    inner = r.get('native_result') if isinstance(r.get('native_result'),dict) else {}
    sat = r.get('sat_candidate') is True or inner.get('sat_candidate') is True or r.get('status') == 'SAT' or inner.get('status') == 'SAT'
    if r.get('pipeline_schema') == 'PA19-SUPERVISED-DRAT-v3':
        import m2_supervised_evidence_v3 as supervised
        errors = supervised.identity_errors(r,expected)
        checker = inner.get('checker_collector') if isinstance(inner.get('checker_collector'),dict) else {}
        invalid = r.get('integrity_status') == 'INVALID' or inner.get('integrity_status') == 'INVALID' or any('NOT VERIFIED' in str(v) for v in checker.get('status_lines',[]))
        if errors or invalid:
            if invalid: errors.append('persistent INVALID integrity/verdict veto; scientific result UNKNOWN')
            state = 'INTEGRITY_VETO'
        elif r.get('halt_production') or r.get('safety_veto') or inner.get('halt_production'):
            errors.append('persistent supervisor/worker safety hold')
            state = 'HALT_UNKNOWN'
        elif r.get('status') == 'UNKNOWN':
            state = 'UNQUALIFIED'
        else:
            if not expected.get('lane_root'): errors.append('explicit owned input root required')
            else: errors += supervised.proof_errors(r,expected,expected['lane_root'])
            state = 'QUALIFIED' if not errors else 'INTEGRITY_VETO'
    elif 'pipeline_schema' in r:
        errors,state = ['unknown pipeline schema; no fallback'],'INTEGRITY_VETO'
    else:
        # Historical classification only; the final component reader never consumes these as measured-v3 evidence.
        errors = proof_errors(r,expected)
        dt = r.get('drat_trim') or {}
        bad = isinstance(dt,dict) and any('NOT VERIFIED' in str(v) for v in dt.get('s_lines',[]))
        state = 'QUALIFIED' if not errors else ('INTEGRITY_VETO' if bad or r.get('checked') is True or r.get('stream_check_revision') not in KNOWN_STAGED else 'UNQUALIFIED')
    if frozen_sha is not None and h != frozen_sha:
        errors.insert(0,'immutable record SHA differs')
        state = 'INTEGRITY_VETO'
    if sat: state = 'SAT_VETO'
    return {'state':state,'errors':errors,'sha256':h,'sat':sat,'record':r}


def expected(mi,bi,indices,cnf_sha,cnf_bytes,encoder='encode_skel_b.build_partbatch',native_limit=600,kissat_only=False):
    return {'multiset':mi,'b_index':bi,'indices':indices,'cnf_sha256':cnf_sha,'cnf_bytes':cnf_bytes,
            'encoder':encoder,'native_limit':native_limit,'kissat_only':kissat_only}
