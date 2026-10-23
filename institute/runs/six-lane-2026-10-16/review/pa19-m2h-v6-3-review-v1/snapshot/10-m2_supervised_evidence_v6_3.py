#!/usr/bin/env python3
"""Known v3 schema only: frozen binary authorities, measured feeds, explicit reaping and cached-census gates.
Rejected/incomplete evidence is scientific UNKNOWN; integrity/SAT/safety vetoes are separately persistent.
"""
import json
import stat
from pathlib import Path

import m2_supervised_runtime_v6_3 as R


def identity_errors(r,ex):
    if not isinstance(r,dict) or r.get('pipeline_schema') != 'PA19-SUPERVISED-DRAT-v6_3': return ['unsupported supervised schema']
    errors = []
    for key in ('multiset','b_index'):
        if type(r.get(key)) is not int or r[key] != ex[key]: errors.append('wrong '+key)
    if ex.get('indices') is None:
        if r.get('indices') is not None: errors.append('unexpected direct split')
    elif not isinstance(r.get('indices'),list) or any(type(v) is not int for v in r['indices']) or r['indices'] != ex['indices']:
        errors.append('wrong exact integer interval')
    if r.get('encoder') != ex['encoder']: errors.append('wrong independent encoder')
    if type(r.get('cnf_bytes')) is not int or r['cnf_bytes'] != ex['cnf_bytes'] or r.get('cnf_sha256') != ex['cnf_sha256']: errors.append('wrong exact CNF bytes/SHA')
    return errors


def gate_errors(g,ex,lane):
    errors = []
    def need(ok,msg):
        if not ok: errors.append(msg)
    try:
        need(g.get('admitted') is True and g.get('errors') == [],'admission refused/missing')
        need(type(g.get('count')) is int and 0 <= g['count'] <= 2,'COUNT ceiling')
        need(type(g.get('free_bytes')) is int and g['free_bytes'] >= g['required_free_bytes'] >= R.BASE_GATE+R.ITEM_GROWTH,'fresh statvfs/growth gate')
        need((g.get('rss') or {}).get('known') is True,'RSS unknown')
        need(g.get('group_rss_cap_bytes') == R.GROUP_RSS_CAP and g.get('busy_units') == 2 and g.get('lane_busy_ceiling') == 4,'normal resource budget differs')
        obs = g['binary_observations']
        need(set(obs) == set(ex['binary_authority']) == {'python','solver','checker'},'binary observation roles missing')
        for kind,authority in ex['binary_authority'].items():
            o = obs[kind]
            need(o.get('path') == authority['path'] and o.get('expected_sha256') == o.get('observed_sha256') == authority['sha256']
                 and o.get('matches') is True,'contract binary authority/observation differs: '+kind)
        c = g['census']; ref = c['reference']; path = Path(lane)/ref['path']
        need(path.resolve().is_relative_to((Path(lane)/'cycle2/accounting-v3').resolve()),'census path escapes')
        need(R.digest(path) == ref['sha256'],'census record SHA differs')
        saved = json.loads(path.read_bytes())
        need(saved == c['record'] and saved.get('schema') == 'PA19-ALLOCATED-CENSUS-v3','census contents/schema differ')
        need(saved.get('ttl_seconds') == R.CENSUS_TTL and saved['data']['known'] is True and saved['data']['stat_errors'] == [],'census unknown/TTL differs')
        age = g['at_monotonic']-saved['finished_monotonic']
        need(0 <= age <= R.CENSUS_TTL and 0 <= c['age_seconds'] <= R.CENSUS_TTL,'census stale at admission')
        usage = saved['data']['new_data_usage_upper_bytes']; bound = g['whole_plan_remaining_bound_bytes']
        need(type(usage) is int and usage == c['current_data_upper_bytes'] and type(bound) is int and bound >= R.ALL_PLANNED_RETAINED_BOUND,'unknown/narrow whole-plan accounting')
        need(g['other_writer_margin_bytes'] == R.OTHER_WRITER_MARGIN and g['additional_data_cap_bytes'] == R.DATA_CAP
             and usage+bound+R.OTHER_WRITER_MARGIN <= R.DATA_CAP,'allocated-data reservation/margin cap')
    except (OSError,ValueError,KeyError,TypeError,AttributeError) as exc:
        errors.append('missing/invalid gate observation: '+repr(exc))
    return errors


def proof_errors(r,ex,lane):
    errors = identity_errors(r,ex)
    if errors: return errors
    def need(ok,msg):
        if not ok: errors.append(msg)
    need(r.get('status') == 'UNSAT' and r.get('checked') is True and r.get('integrity_status') == 'VALIDATED'
         and r.get('integrity_errors') == [] and r.get('sat_candidate') is False and r.get('halt_production') is False,'not a fully qualifying scientific UNSAT')
    try:
        authority = ex['binary_authority']
        need(r.get('binary_authority') == authority,'owner replaced frozen binary authority')
        sp = Path(lane)/r['supervisor_record']
        need(R.digest(sp) == r['supervisor_record_sha256'],'supervisor record SHA differs')
        sr = json.loads(sp.read_bytes())
        need(sr == r['supervisor'] and sr.get('supervisor_sha256') == R.SUP_SHA,'supervisor record/source differs')
        need(sr.get('completed_cleanly') is True and sr.get('uncertain') is False and not any(sr.get(k) for k in
             ('trip_reason','exception','quarantine_record','quarantine_write_error','cleanup_exception','record_write_error','stop_error','stop')),'supervisor safety trip/anomaly')
        need(not sr.get('observed_signal'),'supervisor observed a signal')  # v6_3
        need(r.get('owner_cancelled') is not True and not r.get('observed_signal'),'owner cancellation/signal during the item lifecycle')  # v6_3
        final = sr.get('final_check') or {}
        need(final.get('problems') == [] and final.get('alive_others') == [] and isinstance(final.get('members'),list),'final group check missing/nonclean')
        settle = r['owner_settlement']
        need(settle.get('group_quiescent') is True and settle.get('leader_reaped') is True and settle.get('explicit_owned_popen_wait') is True
             and settle.get('owned_leader_pid') == sr['leader_pid'] and type(settle.get('leader_returncode')) is int and settle['leader_returncode'] == 0,'owned leader not explicitly waited/reaped')
        need(type(sr.get('leader_returncode')) is int and sr['leader_returncode'] == 0,'worker did not self-exit0')
        jp = Path(lane)/r['job_path']; need(R.digest(jp) == r['job_sha256'],'job SHA differs')
        job = json.loads(jp.read_bytes())
        need(job.get('schema') == 'PA19-NATIVE-JOB-v6_3' and job.get('source_sha256') == ex['source_sha256'] and job.get('recipe') == ex['recipe'],'job source/recipe differs')
        need(job.get('binary_authority') == job.get('lease',{}).get('binary_authority') == authority,'job authority differs from contract')
        need(job['cnf_sha256'] == ex['cnf_sha256'] and type(job['cnf_bytes']) is int and job['cnf_bytes'] == ex['cnf_bytes'],'job input differs')
        need(job['solver_seconds'] == ex['native_limit'] and job['checker_seconds'] == 1200,'native/check limit differs')
        expected_command = [authority['python']['path'],'-B',str(Path(lane)/'src/m2_native_staged_v6_3.py'),str(jp),r['job_sha256']]
        need(sr.get('command') == expected_command,'supervised worker argv differs')
        files = sr.get('command_files_sha256') or {}
        need(files.get(expected_command[0]) == authority['python']['sha256'] and files.get(str(jp)) == r['job_sha256']
             and files.get(expected_command[2]) == ex['source_sha256']['src/m2_native_staged_v6_3.py'],'supervised executable/source/job hashes differ')
        np = Path(lane)/r['worker_result_path']; need(R.digest(np) == r['worker_result_sha256'],'worker report SHA differs')
        native = json.loads(np.read_bytes())
        need(native == r['native_result'] and native.get('schema') == 'PA19-NATIVE-RESULT-v6_3','worker report differs')
        need(native.get('status') == 'UNSAT' and native.get('integrity_status') == 'VALIDATED' and native.get('integrity_errors') == []
             and native.get('sat_candidate') is False and native.get('halt_production') is False,'worker outcome unqualified')
        need(native.get('cnf_sha256') == ex['cnf_sha256'] and native.get('cnf_bytes') == ex['cnf_bytes'],'worker regenerated CNF differs')
        folder = Path(job['workdir']); need(folder.resolve().is_relative_to(Path(lane).resolve()),'FIFO directory escapes')
        for name in ('solver-cnf.fifo','checker-cnf.fifo','proof.fifo'):
            st = (folder/name).lstat(); need(stat.S_ISFIFO(st.st_mode) and st.st_size == 0,'CNF/proof transport is not an empty FIFO')
        limit = ex['native_limit']; solver = authority['solver']['path']
        prefix = [solver,'-q','-f','--seed=1','--time=%d' % limit] if job['solver'] == 'kissat' else [solver,'-q','-t',str(limit)]
        need(native.get('solver_command') == prefix+[str(folder/'solver-cnf.fifo'),str(folder/'proof.fifo')],'solver argv differs')
        need(native.get('checker_command') == [authority['checker']['path'],str(folder/'checker-cnf.fifo'),'-i','-t','1200'],'checker argv differs')
        for name in ('owner_preconstruction_gate','owner_prespawn_gate'):
            errors += [name+': '+e for e in gate_errors(r.get(name) or {},ex,lane)]
        errors += ['worker_preconstruction: '+e for e in gate_errors(native.get('worker_preconstruction_gate') or {},ex,lane)]
        gates = native.get('gates') or []
        need([g.get('phase') for g in gates] == ['solver','checker'],'both immediate native gates missing')
        for gate in gates: errors += [gate.get('phase','?')+': '+e for e in gate_errors(gate,ex,lane)]
        sc,dc = native['solver_collector'],native['checker_collector']
        need(all(k in sc and k in dc for k in ('complete','error','status_lines','sha256','bytes_read')),'collector observations missing')
        need(sc['complete'] is True and sc['error'] is None and sc['status_lines'] == ['s UNSATISFIABLE'],'solver exact completed verdict failed')
        need(dc['complete'] is True and dc['error'] is None and dc['status_lines'] == ['s VERIFIED'],'checker exact completed verdict failed')
        need(type(native.get('solver_rc')) is int and native['solver_rc'] == 20 and native.get('solver_stop') == 'self','solver not self20')
        need(type(native.get('checker_rc')) is int and native['checker_rc'] == 0 and native.get('checker_stop') == 'self','checker not self0')
        feeds = native['cnf_feeds']; need(set(feeds) == {'solver','checker'},'both CNF feeds required')
        for name,f in feeds.items():
            need(all(k in f for k in ('complete','close_ok','error','bytes','sha256')),'CNF observation fields missing: '+name)
            need(f['complete'] is True and f['close_ok'] is True and f['error'] is None and type(f['bytes']) is int
                 and f['bytes'] == ex['cnf_bytes'] and f['sha256'] == ex['cnf_sha256'],'CNF delivery mismatch: '+name)
        p,d = native['proof_stream'],native['proof_delivery']
        need(p.get('reader_complete') is True and p.get('reader_error') is None and not p.get('proof_cap_hit'),'proof reader incomplete/capped')
        need(type(p.get('raw_bytes')) is int and 0 <= p['raw_bytes'] <= 1200*1024**2 and type(p.get('compressed_bytes')) is int and 0 <= p['compressed_bytes'] <= 500*1024**2,'proof caps')
        need(d.get('complete') is True and d.get('close_ok') is True and d.get('error') is None and type(d.get('bytes')) is int
             and d['bytes'] == p['raw_bytes'] and d.get('sha256') == p['raw_sha256'],'proof measured delivery/frame/close failed')
        need(not any(native.get(k) for k in ('resource_refusal','proof_cap_hit','lifecycle_error','bounded_unknown','metadata_bound_error')),'native anomaly')
    except (OSError,ValueError,KeyError,TypeError,AttributeError) as exc:
        errors.append('missing/invalid supervised proof binding: '+repr(exc))
    return errors
