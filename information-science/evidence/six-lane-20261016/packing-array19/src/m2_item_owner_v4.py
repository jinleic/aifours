#!/usr/bin/env python3
"""V3: one attempt, contract-authoritative binaries, retained Popen reaping, safety-first UNKNOWN/integrity veto.
No automatic RSS retry. A safety trip always dominates a worker's bounded-UNKNOWN/proof-cap report. Every veto is
persistent before token release; group quiescence AND explicit owned-leader wait are prerequisites for release.
"""
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v4 as C
import m2_supervised_runtime_v4 as R
import m2_supervised_evidence_v4 as EVIDENCE

L = C.LANE
WORKER = L/'src/m2_native_staged_v4.py'


def bounded_publish(path,value,stage,limit):
    raw = (json.dumps(value,indent=1)+'\n').encode()
    if len(raw) > limit: raise ValueError('frozen metadata publication bound exceeded')
    C.publish_bytes(path,raw,stage)
    return hashlib.sha256(raw).hexdigest()


def persist_veto(result,paths,contract_sha,recipe):
    if result.get('sat_candidate'):
        kind = 'SAT'
    elif result.get('integrity_status') == 'INVALID':
        kind = 'INTEGRITY'
    elif result.get('halt_production'):
        kind = 'HALT'
    else: return
    flag = L/'cycle2'/('m2k3-'+kind+'.flag')
    note = {'status':'UNKNOWN','veto':kind,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'production_contract_sha256':contract_sha,'recipe':recipe,'owner_pid':os.getpid(),
        'worker_result':str(Path(paths['worker_result']).relative_to(L)),
        'supervisor_record':str(Path(paths['supervisor']).relative_to(L)),
        'integrity_errors':result.get('integrity_errors'),'safety_veto':result.get('safety_veto'),
        'scope':'persistent unverified SAT / integrity / safety hold; scientific result UNKNOWN'}
    while not flag.exists():
        try:
            with flag.open('x') as f: json.dump(note,f,indent=1)
            return
        except FileExistsError: return
        except OSError: time.sleep(0.25)  # token stays owned throughout this receipt-only wait


def supervisor_safety_errors(rec,settlement):
    errors = []
    if rec.get('completed_cleanly') is not True: errors.append('supervisor did not complete cleanly')
    for key in ('trip_reason','uncertain','exception','quarantine_record','quarantine_write_error','cleanup_exception','record_write_error','stop_error'):
        if rec.get(key): errors.append(key+': '+str(rec[key]))
    stop = rec.get('stop') or {}
    if stop: errors.append('supervisor performed safety-stop cleanup')
    if stop.get('killpg_error'): errors.append('killpg_error: '+str(stop['killpg_error']))
    if not isinstance(settlement,dict) or settlement.get('group_quiescent') is not True or settlement.get('leader_reaped') is not True or settlement.get('explicit_owned_popen_wait') is not True:
        errors.append('group quiescence/explicit owned leader reaping not affirmed')
    return errors


def apply_worker_outcome(result,native,rec,settlement):
    """Shared actual production/control composition; a worker bounded-UNKNOWN can NEVER clear a safety hold."""
    safety = supervisor_safety_errors(rec,settlement)
    if safety:
        result.update(status='UNKNOWN',checked=False,halt_production=True,safety_veto=safety)
    elif native is not None:
        if native['status'] == 'UNSAT' and native['integrity_status'] == 'VALIDATED' and not native.get('sat_candidate') and not native.get('halt_production'):
            result.update(status='UNSAT',checked=True,halt_production=False)
        else:
            result.update(status='UNKNOWN',checked=False,halt_production=bool(native.get('halt_production') or result.get('sat_candidate') or native['integrity_status'] == 'INVALID'))
    result['chunk_stop'] = bool(result.get('halt_production') or (native or {}).get('chunk_stop'))
    return result


def execute(constructor,recipe,contract_sha,source_sha,paths,deadline,admission,solver='kissat',seconds=600):
    """All expectations derive from the frozen contract admission object; observed hashes NEVER become authority."""
    authority = admission['binary_authority']
    assert authority['solver']['path'] == '/opt/homebrew/bin/'+solver
    result = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v4','status':'UNKNOWN','checked':False,
        'integrity_status':'NOT_EVALUATED','integrity_errors':[],'sat_candidate':False,'halt_production':False,
        'group_started':False,'production_contract_sha256':contract_sha,'multiset':recipe['multiset'],'b_index':recipe['b_index'],
        'indices':recipe.get('indices'),'encoder':'encode_skel_b.build_v2' if recipe['mode'] == 'direct' else 'encode_skel_b.build_partbatch',
        'recipe':recipe,'proof_retained':False,'cnf_retained':False,'solver_name':solver,'native_limit_seconds':seconds,
        'checker_limit_seconds':1200,'binary_authority':authority,'automatic_retry_allowed':False}
    stage = Path(paths['staging'])
    with R.Capacity(deadline) as capacity:
        try:
            now = time.monotonic()
            lease = {'owner_pid':os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,
                'census_reference':admission['census_reference'],'whole_plan_remaining_bound_bytes':admission['whole_plan_remaining_bound_bytes'],
                'force_census_refresh':capacity.wait_seconds > R.CENSUS_TTL,'binary_authority':authority,
                'group_rss_cap_bytes':R.GROUP_RSS_CAP,'busy_units':2,'lane_busy_ceiling':4,
                'chunk_deadline_monotonic':deadline,'item_deadline_monotonic':now+2400}
            pre = R.full_gate(lease,'construct')
            result['owner_preconstruction_gate'] = pre
            if not pre['admitted']:
                # refusal rule1: before any pin/job; unattempted, no record and no persistent HALT.
                result.update(resource_refusal=pre['errors'],unattempted='before-pin',halt_production=False,chunk_stop=True)
                return result
            raw = constructor()
            h,nbytes = hashlib.sha256(raw).hexdigest(),len(raw)
            result.update(cnf_sha256=h,cnf_bytes=nbytes)
            pin = {'schema':'PA19-K1-CNF-PIN-v4','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                'production_contract_sha256':contract_sha,'multiset':recipe['multiset'],'b_index':recipe['b_index'],
                'indices':recipe.get('indices'),'cnf_sha256':h,'cnf_bytes':nbytes,'recipe':recipe,'source_sha256':source_sha,
                'supervisor_sha256':R.SUP_SHA,'binary_authority':authority,'no_cnf_or_proof_retained':True}
            pin_sha = bounded_publish(paths['pin'],pin,stage,16384)
            result.update(pre_child_pin_sha256=pin_sha,pre_child_pin_path=str(Path(paths['pin']).relative_to(L)))
            lease['item_deadline_monotonic'] = time.monotonic()+2400
            job = {'schema':'PA19-NATIVE-JOB-v4','recipe':recipe,'cnf_sha256':h,'cnf_bytes':nbytes,'solver':solver,
                'solver_seconds':seconds,'checker_seconds':1200,'lease':lease,'source_sha256':source_sha,'binary_authority':authority,
                'workdir':str(paths['workdir']),'result_path':str(paths['worker_result'])}
            job_sha = bounded_publish(paths['job'],job,stage,16384)
            del raw
            command = [authority['python']['path'],'-B',str(WORKER),str(paths['job']),job_sha]
            rec,gate = capacity.supervise(command,'PA19-'+paths['id'],lease,paths['supervisor'],paths['quarantine'])
            result['owner_prespawn_gate'] = gate
            if rec is None:
                # refusal rule2: pin/job exist but no worker process started; runner retires own metadata, no record/HALT.
                result.update(resource_refusal=gate['errors'],unattempted='after-pin-before-worker',halt_production=False,chunk_stop=True)
                return result
            result.update(group_started=rec.get('leader_pid') is not None,supervisor_record=str(Path(paths['supervisor']).relative_to(L)),
                supervisor_record_sha256=R.digest(paths['supervisor']) if Path(paths['supervisor']).exists() else None,
                supervisor=rec,owner_settlement=capacity.settlement,job_path=str(Path(paths['job']).relative_to(L)),job_sha256=job_sha)
            safety = supervisor_safety_errors(rec,capacity.settlement)
            native = None
            try:
                native = json.loads(Path(paths['worker_result']).read_bytes())
                assert native['schema'] == 'PA19-NATIVE-RESULT-v4' and native['status'] in ('UNSAT','UNKNOWN')
                assert native['integrity_status'] in ('VALIDATED','INVALID','NOT_EVALUATED')
                result.update(native_result=native,worker_result_path=str(Path(paths['worker_result']).relative_to(L)),
                              worker_result_sha256=R.digest(paths['worker_result']))
                result.update(sat_candidate=bool(native.get('sat_candidate')),integrity_status=native['integrity_status'],
                              integrity_errors=list(native.get('integrity_errors') or []))
            except (OSError,ValueError,KeyError,TypeError,AssertionError) as exc:
                if supervisor_safety_errors(rec,capacity.settlement):
                    result['worker_report_missing_after_safety_stop'] = repr(exc)  # safety HALT below; not evidence corruption
                else:
                    result.update(integrity_status='INVALID',integrity_errors=['worker report unavailable/invalid: '+repr(exc)],halt_production=True)
            apply_worker_outcome(result,native,rec,capacity.settlement)
            if result['status'] == 'UNSAT':
                ex = {'multiset':recipe['multiset'],'b_index':recipe['b_index'],'indices':recipe.get('indices'),'encoder':result['encoder'],
                    'cnf_sha256':h,'cnf_bytes':nbytes,'native_limit':seconds,'binary_authority':authority,
                    'source_sha256':source_sha,'recipe':recipe}
                errors = EVIDENCE.proof_errors(result,ex,L)
                result['proof_qualification_errors'] = errors
                if errors: result.update(status='UNKNOWN',checked=False,integrity_status='INVALID',integrity_errors=errors,halt_production=True)
            if result['status'] == 'UNSAT' and (Path(paths['supervisor']).stat().st_size > 8192 or len((json.dumps(result,indent=1)+'\n').encode()) > 65536):
                result.update(status='UNKNOWN',checked=False,halt_production=True,metadata_bound_error='ordinary supervisor/owner8KiB/64KiB bound')
            return result
        except BaseException as exc:
            result.update(status='UNKNOWN',checked=False,integrity_status='INVALID',integrity_errors=[repr(exc)],halt_production=True)
            return result
        finally:
            persist_veto(result,paths,contract_sha,recipe)
