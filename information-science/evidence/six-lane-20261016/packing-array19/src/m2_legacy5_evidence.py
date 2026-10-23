#!/usr/bin/env python3
"""Explicit ORIGINAL-QUALIFIED LEGACY5 M2 classification, global inventory only.
No unknown-revision fallback; no guard15 fields are fabricated. Native self20 + original standard-DRAT checker
self0/says_verified/!says_timeout/checked is historical evidence, NOT a final independent M2 certificate.
Parent RC3 observed a truncated CNF plus empty proof return rc0/'s VERIFIED'; formula bindings alone therefore
cannot repair unmeasured checker input. A separately reviewed exact-delivery source/receipt or measured parent
re-solve/replay is REQUIRED before final acceptance. This module never accepts that supplemental gate itself.
It never mixes M1 replay/exposure results into M2 and never starts a solver/checker.
"""
import hashlib
import re
from pathlib import Path

SHA = re.compile(r'[0-9a-f]{64}\Z')
NOT_RETAINED = {
    'solver_status_lines':'NOT_RETAINED (legacy5 discards UNSAT solver stdout)',
    'checker_exact_status_lines':'NOT_RETAINED (legacy5 retains derived says_verified/says_timeout booleans only)',
    'solver_cnf_delivered_count_sha':'NOT_RETAINED (legacy5 CNF feeder has no measured completion predicate)',
    'checker_cnf_delivered_count_sha':'NOT_RETAINED (legacy5 CNF feeder has no measured completion predicate)',
    'delivered_proof_count_sha':'NOT_RETAINED (legacy5 has streamed counters, not guard15 delivery/replay flags)',
    'replay_ok':'NOT_RETAINED (not part of the explicit legacy5 schema)'}


def gate_errors(r,identity):
    if not isinstance(r,dict):
        return ['legacy5 record is not an object']
    errors = []
    def need(ok,text):
        if not ok: errors.append(text)
    need(type(r.get('stream_check_revision')) is int and r['stream_check_revision'] == 5,'not the explicitly supported legacy5 schema')
    need(r.get('status') == 'UNSAT' and r.get('checked') is True and r.get('drat_trim_verified') is True,'not original checked standard-DRAT UNSAT')
    need(type(r.get('solver_rc')) is int and r['solver_rc'] == 20 and r.get('solver_stop') == 'self','solver did not self-exit20')
    dt = r.get('drat_trim') or {}
    need(isinstance(dt,dict) and type(dt.get('rc')) is int and dt['rc'] == 0 and dt.get('stop') == 'self','checker did not self-exit0')
    need(isinstance(dt,dict) and dt.get('says_verified') is True and dt.get('says_timeout') is False,'legacy checker booleans do not qualify')
    need(r.get('checker_interrupted') is False,'checker interrupted/missing')
    need(not r.get('admission_denied') and not r.get('proof_cap_hit') and not r.get('lratstrict_verified'),'refusal/cap/strict-LRAT is not eligible')
    need(isinstance(r.get('cnf_sha256'),str) and SHA.fullmatch(r['cnf_sha256']) is not None and type(r.get('cnf_bytes')) is int and r['cnf_bytes'] > 0,'invalid CNF SHA/bytes')
    need(isinstance(r.get('drat_sha256'),str) and SHA.fullmatch(r['drat_sha256']) is not None and type(r.get('drat_bytes')) is int and r['drat_bytes'] >= 0,'invalid original streamed proof SHA/count')
    for k,v in identity.items():
        actual = r.get(k)
        need(actual == v and (type(actual) is int if type(v) is int else True),'legacy identity differs: '+k)
    return errors


def final_binding_errors(record_path,record_sha,r,parent_binding):
    """Screen formula binding only; deliberately retain the unresolved exact-checker-delivery veto."""
    if not isinstance(parent_binding,dict):
        return ['parent independent M2 formula binding missing']
    errors = ['LEGACY5 alone cannot satisfy the final M2 gate: separate exact-delivery source/receipt evidence or measured supplemental parent re-solve/replay is required']
    if hashlib.sha256(Path(record_path).read_bytes()).hexdigest() != record_sha:
        errors.append('immutable receipt SHA changed')
    if parent_binding.get('record_sha256') != record_sha:
        errors.append('parent binding names another receipt')
    if parent_binding.get('cnf_sha256') != r.get('cnf_sha256') or parent_binding.get('cnf_bytes') != r.get('cnf_bytes'):
        errors.append('parent regenerated formula differs')
    if parent_binding.get('status') != 'BYTE_EQUAL' or parent_binding.get('method') != 'M2':
        errors.append('parent formula binding not explicit M2 BYTE_EQUAL')
    return errors
