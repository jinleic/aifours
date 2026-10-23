#!/usr/bin/env python3
"""Per-item outer owner: tier1 token (3.5GiB), tier2 ALL token flocks+bigmem (7GiB), then reviewed supervise_r3.
Both native CNF feeds are measured. SAT/INVALID/safety holds persist BEFORE ownership is released; known quiescence
is always required. An unambiguous sole-RSS tier1 stop alone is eligible for exactly one separately named tier2.
The ordinary retained-output budget is384KiB/input (hardlinks charged per path); one diagnostic outcome may use the
separate64MiB reserve and halts admission. No proof/CNF file copies; no setuid helper in the group.
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import m2_ms09_contract as C
import m2_supervised_runtime_v2 as R
import m2_supervised_evidence_v2 as EVIDENCE

L = C.LANE
WORKER = L/'src'/'m2_native_staged_v2.py'


def bounded_publish(path,value,stage,limit):
    raw = (json.dumps(value,indent=1)+'\n').encode()
    assert len(raw) <= limit, 'frozen metadata publication bound exceeded'
    C.publish_bytes(path,raw,stage)
    return hashlib.sha256(raw).hexdigest()


def persist_veto(result,paths,contract_sha,recipe):
    if result['status'] not in ('SAT','INVALID') and not result.get('halt_production'):
        return
    name = 'm2k1-'+(result['status'] if result['status'] in ('SAT','INVALID') else 'HALT')+'.flag'
    flag = L/'cycle2'/name
    note = {'status':result['status'],'halt_production':True,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'production_contract_sha256':contract_sha,'recipe':recipe,'owner_pid':os.getpid(),
            'worker_result':str(Path(paths['worker_result']).relative_to(L)),
            'supervisor_record':str(Path(paths['supervisor']).relative_to(L)),
            'scope':'persistent unverified SAT / invalid-evidence / safety veto; not a mathematical result'}
    while not flag.exists():
        try:
            with flag.open('x') as f:
                json.dump(note,f,indent=1)
            return
        except FileExistsError:
            return
        except OSError:
            # Group is already quiescent, but future admission must not race an unrecorded veto.
            # The caller is still INSIDE Capacity and retains every owned tier1/tier2 flock throughout this wait.
            time.sleep(0.25)


def execute(constructor,recipe,contract_sha,source_sha,paths,deadline,accounting_envelope,solver='kissat',seconds=600,tier=1,prior=None):
    """One attempt in its tier. Tier2 binds immutable tier1 sole-RSS evidence; no other retry is admitted."""
    result = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v2','status':'UNKNOWN','checked':False,
              'group_started':False,'halt_production':False,'production_contract_sha256':contract_sha,
              'multiset':recipe['multiset'],'b_index':recipe['b_index'],'indices':recipe.get('indices'),
              'encoder':'encode_skel_b.build_v2' if recipe['mode'] == 'direct' else 'encode_skel_b.build_partbatch',
              'recipe':recipe,'proof_retained':False,'cnf_retained':False,'solver_name':solver,
              'native_limit_seconds':seconds,'checker_limit_seconds':1200}
    result['tier'] = tier
    if tier == 2:
        assert isinstance(prior,dict) and R.digest(L/prior['path']) == prior['sha256']
        previous = C.read(L/prior['path'])
        assert previous['status'] == 'UNKNOWN' and previous['tier'] == 1 and previous['recipe'] == recipe
        assert previous.get('rss_retry_eligible') is True and R.rss_only_retry(previous['supervisor'],1,previous.get('native_result'))
        result['tier1_prior'] = prior
    stage = Path(paths['staging'])
    with R.Capacity(deadline,tier=tier) as capacity:
        try:
            now = time.monotonic()
            lease = {'owner_pid':os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,'accounting_envelope':accounting_envelope,
                     'group_rss_cap_bytes':R.GROUP_CAPS[tier],'chunk_deadline_monotonic':deadline,
                     'item_deadline_monotonic':now+2400,'tier':tier,'busy_units':2,'lane_busy_ceiling':4,
                     'held_token_indices':capacity.token_indices,'exclusive_bigmem':tier == 2,'admitted_count':R.token_count()}
            pre = R.full_gate(lease,'item')
            result['owner_preconstruction_gate'] = pre
            if not pre['admitted']:
                result.update(resource_refusal=pre['errors'],unattempted=True,halt_production=True)
                return result
            raw = constructor()
            h,nbytes = hashlib.sha256(raw).hexdigest(),len(raw)
            result.update(cnf_sha256=h,cnf_bytes=nbytes)
            if tier == 2:
                assert previous['cnf_sha256'] == h and previous['cnf_bytes'] == nbytes, 'tier2 formula differs from tier1'
            pin = {'schema':'PA19-K1-CNF-PIN-v2','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                   'production_contract_sha256':contract_sha,'multiset':recipe['multiset'],'b_index':recipe['b_index'],
                   'indices':recipe.get('indices'),'cnf_sha256':h,'cnf_bytes':nbytes,'recipe':recipe,
                   'source_sha256':source_sha,'supervisor_sha256':R.SUP_SHA,'no_cnf_or_proof_retained':True}
            pin.update(tier=tier,tier1_prior=prior)
            pin_sha = bounded_publish(paths['pin'],pin,stage,16384)
            result.update(pre_child_pin_sha256=pin_sha,pre_child_pin_path=str(Path(paths['pin']).relative_to(L)))
            lease['item_deadline_monotonic'] = time.monotonic()+2400
            job = {'schema':'PA19-NATIVE-JOB-v2','recipe':recipe,'cnf_sha256':h,'cnf_bytes':nbytes,
                   'solver':solver,'solver_seconds':seconds,'checker_seconds':1200,'lease':lease,'source_sha256':source_sha,
                   'solver_binary_sha256':R.digest('/opt/homebrew/bin/'+solver),
                   'checker_binary_sha256':R.digest(L/'tools/drat-trim/drat-trim'),
                   'workdir':str(paths['workdir']),'result_path':str(paths['worker_result'])}
            jsha = bounded_publish(paths['job'],job,stage,16384)
            del raw
            command = [sys.executable,'-B',str(WORKER),str(paths['job']),jsha]
            rec,gate = capacity.supervise(command,'PA19-'+paths['id'],lease,paths['supervisor'],paths['quarantine'])
            result['owner_prespawn_gate'] = gate
            if rec is None:
                result.update(resource_refusal=gate['errors'],halt_production=True)
                return result
            result.update(group_started=True,supervisor_record=str(Path(paths['supervisor']).relative_to(L)),
                          supervisor_record_sha256=R.digest(paths['supervisor']) if Path(paths['supervisor']).exists() else None,
                          supervisor=rec,job_path=str(Path(paths['job']).relative_to(L)),job_sha256=jsha,
                          solver_binary_sha256=job['solver_binary_sha256'],checker_binary_sha256=job['checker_binary_sha256'])
            native = None
            try:
                native = json.loads(Path(paths['worker_result']).read_bytes())
                assert native['schema'] == 'PA19-NATIVE-RESULT-v2'
                result.update(native_result=native,worker_result_path=str(Path(paths['worker_result']).relative_to(L)),
                              worker_result_sha256=R.digest(paths['worker_result']))
            except (OSError,ValueError,KeyError,AssertionError) as exc:
                if not R.rss_only_stop(rec,tier):
                    result.update(lifecycle_error='worker report unavailable/invalid: '+repr(exc),halt_production=True)
                    return result
                result['rss_stop_worker_report_unavailable'] = repr(exc)
            if R.rss_only_stop(rec,tier,native):
                result.update(status='UNKNOWN',checked=False,halt_production=False,rss_only_stop=True,
                              rss_retry_eligible=tier == 1,rss_threshold_bytes=R.GROUP_CAPS[tier])
                return result
            if native is None:
                result.update(lifecycle_error='non-sole-RSS stop without worker report',halt_production=True)
                return result
            stop_info = rec.get('stop') or {}
            known_stopped = rec.get('completed_cleanly') is True or (stop_info.get('listing_ok') is True and stop_info.get('survivors') == [])
            ordinary = native['status'] == 'UNKNOWN' and bool(native.get('bounded_unknown') or native.get('proof_cap_hit'))
            ordinary = ordinary and not native.get('lifecycle_error') and not rec.get('uncertain') and not rec.get('quarantine_record') and not rec.get('record_write_error') and known_stopped
            if native['status'] in ('SAT','INVALID'):
                result.update(status=native['status'],halt_production=True)
            elif ordinary:
                result.update(ordinary_bounded_unknown=True,halt_production=False)
            elif not rec.get('completed_cleanly') or rec.get('uncertain') or rec.get('quarantine_record') or rec.get('record_write_error'):
                result.update(halt_production=True,supervisor_nonclean=True)
            else:
                result.update(status=native['status'],halt_production=bool(native.get('halt_production')),checked=native['status'] == 'UNSAT')
            if result['status'] == 'UNSAT' and (Path(paths['supervisor']).stat().st_size > 8192 or len((json.dumps(result,indent=1)+'\n').encode()) > 65536):
                result.update(status='UNKNOWN',checked=False,halt_production=True,metadata_bound_error='ordinary supervisor/owner receipt exceeds frozen8KiB/64KiB bound')
            return result
        except BaseException as exc:
            result.update(lifecycle_error=repr(exc),halt_production=True)
            return result
        finally:
            if result['status'] == 'UNSAT':
                expected = {'multiset':recipe['multiset'],'b_index':recipe['b_index'],'indices':recipe.get('indices'),
                    'encoder':result['encoder'],'cnf_sha256':h,'cnf_bytes':nbytes,'native_limit':seconds,
                    'kissat_only':solver == 'kissat','solver_binary_sha256':job['solver_binary_sha256'],
                    'checker_binary_sha256':job['checker_binary_sha256'],'source_sha256':source_sha,'recipe':recipe}
                expected.update(tier=tier,tier1_prior=prior)
                errors = EVIDENCE.proof_errors(result,expected,L)
                result['proof_qualification_errors'] = errors
                if errors: result.update(status='INVALID',checked=False,halt_production=True)
            persist_veto(result,paths,contract_sha,recipe)
