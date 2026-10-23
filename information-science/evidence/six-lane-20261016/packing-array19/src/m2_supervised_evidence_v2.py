#!/usr/bin/env python3
"""Known v2 supervised proof schema only. Every required observation is real and measured; no padding of legacy
records. INVALID verdicts are vetoes, ordinary bounded UNKNOWNs remain uncounted, and no unknown schema qualifies.
"""
import json
import stat
from pathlib import Path

import m2_supervised_runtime_v2 as R


def identity_errors(r,ex):
    errors = []
    if not isinstance(r,dict) or r.get('pipeline_schema') != 'PA19-SUPERVISED-DRAT-v2':
        return ['unsupported supervised proof schema']
    for k in ('multiset','b_index'):
        if type(r.get(k)) is not int or r[k] != ex[k]: errors.append('wrong '+k)
    idx = ex.get('indices')
    if idx is None:
        if r.get('indices') is not None: errors.append('direct input unexpectedly split')
    elif not isinstance(r.get('indices'),list) or any(type(x) is not int for x in r['indices']) or r['indices'] != idx:
        errors.append('wrong exact interval')
    if r.get('encoder') != ex['encoder']: errors.append('wrong encoder')
    if r.get('cnf_sha256') != ex['cnf_sha256'] or r.get('cnf_bytes') != ex['cnf_bytes'] or type(r.get('cnf_bytes')) is not int:
        errors.append('wrong exact CNF bytes/SHA')
    return errors


def proof_errors(r,ex,lane):
    errors = identity_errors(r,ex)
    if errors: return errors
    def need(ok,text):
        if not ok: errors.append(text)
    need(r.get('status') == 'UNSAT' and r.get('checked') is True and r.get('halt_production') is False,'not qualifying supervised UNSAT')
    tier = ex.get('tier')
    need(type(tier) is int and tier in (1,2) and r.get('tier') == tier,'wrong/missing tier')
    try:
        sp = Path(lane)/r['supervisor_record']
        need(R.digest(sp) == r['supervisor_record_sha256'],'supervisor receipt SHA differs')
        sr = json.loads(sp.read_bytes())
        need(sr == r['supervisor'],'supervisor receipt content differs')
        need(sr.get('supervisor_sha256') == R.SUP_SHA,'unreviewed supervisor')
        need(sr.get('completed_cleanly') is True and sr.get('uncertain') is False and not sr.get('trip_reason')
             and not sr.get('quarantine_record') and not sr.get('cleanup_exception') and not sr.get('record_write_error'), 'supervisor not clean/quiescent')
        need(sr.get('leader_returncode') == 0 and type(sr.get('leader_returncode')) is int,'worker leader did not exit0')
        final = sr.get('final_check') or {}
        need(bool(final) and isinstance(final.get('members'),list) and final.get('problems') == [] and final.get('alive_others') == [],'group not known quiescent at final check')
        jp = Path(lane)/r['job_path']
        need(R.digest(jp) == r['job_sha256'],'job SHA differs')
        job = json.loads(jp.read_bytes())
        need(job.get('lease',{}).get('tier') == tier,'job tier differs')
        if tier == 2:
            prior = r.get('tier1_prior')
            need(prior == ex.get('tier1_prior') and isinstance(prior,dict),'tier2 prior binding differs')
            previous_path = Path(lane)/prior['path']
            need(R.digest(previous_path) == prior['sha256'],'tier1 prior receipt SHA differs')
            previous = json.loads(previous_path.read_bytes())
            need(previous.get('status') == 'UNKNOWN' and previous.get('tier') == 1 and previous.get('rss_retry_eligible') is True
                 and R.rss_only_retry(previous.get('supervisor'),1,previous.get('native_result')),'tier2 prior not sole-RSS eligible')
            need(previous.get('cnf_sha256') == ex['cnf_sha256'] and previous.get('cnf_bytes') == ex['cnf_bytes'],'tier2 prior CNF differs')
        need(job.get('schema') == 'PA19-NATIVE-JOB-v2' and job.get('source_sha256') == ex.get('source_sha256') and job.get('recipe') == ex.get('recipe'),'job source/recipe binding differs')
        command = sr.get('command') or []
        need(len(command) == 5 and command[1:] == ['-B',str(Path(lane)/'src/m2_native_staged_v2.py'),str(jp),r['job_sha256']],'supervised worker/argv differs')
        files = sr.get('command_files_sha256') or {}
        need(files.get(str(jp)) == r['job_sha256'] and files.get(str(Path(lane)/'src/m2_native_staged_v2.py')) == R.digest(Path(lane)/'src/m2_native_staged_v2.py'),'supervised command hashes differ')
        need(job.get('cnf_sha256') == ex['cnf_sha256'] and job.get('cnf_bytes') == ex['cnf_bytes'],'job input binding differs')
        need(job.get('solver_seconds') == ex['native_limit'] and job.get('checker_seconds') == 1200,'native limits differ')
        need(job.get('solver') == ('kissat' if ex.get('kissat_only') else r.get('solver_name')),'solver identity differs')
        need(job.get('solver_binary_sha256') == ex.get('solver_binary_sha256') and job.get('checker_binary_sha256') == ex.get('checker_binary_sha256'),'binary not the frozen production input')
        need(R.digest(Path(lane)/r['worker_result_path']) == r['worker_result_sha256'],'worker result SHA differs')
        native = json.loads((Path(lane)/r['worker_result_path']).read_bytes())
        need(native == r['native_result'],'worker result content differs')
        need(native.get('schema') == 'PA19-NATIVE-RESULT-v2' and native.get('status') == 'UNSAT' and native.get('halt_production') is False,'worker outcome not UNSAT')
        need(native.get('cnf_sha256') == ex['cnf_sha256'] and native.get('cnf_bytes') == ex['cnf_bytes'],'worker regenerated CNF differs')
        folder = Path(job['workdir'])
        need(folder.resolve().is_relative_to(Path(lane).resolve()),'FIFO directory escapes owned lane')
        for name in ('solver-cnf.fifo','checker-cnf.fifo','proof.fifo'):
            st = (folder/name).lstat()
            need(stat.S_ISFIFO(st.st_mode) and st.st_size == 0,'CNF/proof transport is not a FIFO')
        limit = job['solver_seconds']
        prefix = ['/opt/homebrew/bin/kissat','-q','-f','--seed=1','--time=%d' % limit] if job['solver'] == 'kissat' else ['/opt/homebrew/bin/cadical','-q','-t',str(limit)]
        need(native.get('solver_command') == prefix+[str(folder/'solver-cnf.fifo'),str(folder/'proof.fifo')],'native solver command differs')
        need(native.get('checker_command') == [str(Path(lane)/'tools/drat-trim/drat-trim'),str(folder/'checker-cnf.fifo'),'-i','-t','1200'],'native checker command differs')
        for phase in ('owner_preconstruction_gate','owner_prespawn_gate'):
            gate = r.get(phase) or {}
            need(gate.get('admitted') is True and gate.get('errors') == [],'owner gate absent/refused: '+phase)
            need(type(gate.get('free_bytes')) is int and gate['free_bytes'] >= gate['required_free_bytes'] > R.BASE_GATE,'owner fresh growth margin missing')
            need(gate.get('tier') == tier and gate.get('group_rss_cap_bytes') == R.GROUP_CAPS[tier],'owner tier threshold differs')
        gates = native.get('gates') or []
        need([g.get('phase') for g in gates] == ['solver','checker'],'two immediate native gates missing')
        for g in gates:
            need(g.get('admitted') is True and g.get('errors') == [] and type(g.get('count')) is int and 0 <= g['count'] <= 2,'native gate refused/COUNT')
            need(type(g.get('free_bytes')) is int and g['free_bytes'] >= g['required_free_bytes'] > R.BASE_GATE,'native growth margin failed')
            need((g.get('rss') or {}).get('known') is True,'native RSS unknown')
            need(g.get('tier') == tier and g.get('group_rss_cap_bytes') == R.GROUP_CAPS[tier] and g.get('busy_units') == 2
                 and g.get('lane_busy_ceiling') == 4 and g.get('exclusive_bigmem') is (tier == 2),'native tier/busy/ownership differs')
        sc,dc = native['solver_collector'],native['checker_collector']
        need(all(k in sc and k in dc for k in ('complete','error','status_lines','sha256','bytes_read')),'collector observation fields missing')
        need(sc.get('complete') is True and sc.get('error') is None and sc.get('status_lines') == ['s UNSATISFIABLE'],'solver collector/verdict invalid')
        need(dc.get('complete') is True and dc.get('error') is None and dc.get('status_lines') == ['s VERIFIED'],'checker collector/verdict invalid')
        need(type(native.get('solver_rc')) is int and native['solver_rc'] == 20 and native.get('solver_stop') == 'self','solver not self20')
        need(type(native.get('checker_rc')) is int and native['checker_rc'] == 0 and native.get('checker_stop') == 'self','checker not self0')
        feeds = native['cnf_feeds']
        need(set(feeds) == {'solver','checker'},'both CNF feeds missing')
        for name,f in feeds.items():
            need(all(k in f for k in ('complete','close_ok','error','bytes','sha256')),'CNF feed observation fields missing: '+name)
            need(f.get('complete') is True and f.get('close_ok') is True and f.get('error') is None,'CNF feed failed: '+name)
            need(type(f.get('bytes')) is int and f['bytes'] == ex['cnf_bytes'] and f.get('sha256') == ex['cnf_sha256'],'CNF delivered bytes/SHA differ: '+name)
        p,d = native['proof_stream'],native['proof_delivery']
        need(p.get('reader_complete') is True and p.get('reader_error') is None and not p.get('proof_cap_hit'),'proof reader failed/capped')
        need(type(p.get('raw_bytes')) is int and 0 <= p['raw_bytes'] <= 1200*1024**2 and type(p.get('compressed_bytes')) is int and p['compressed_bytes'] <= 500*1024**2,'proof caps exceeded')
        need(d.get('complete') is True and d.get('close_ok') is True and d.get('error') is None,'proof delivery failed')
        need(d.get('bytes') == p.get('raw_bytes') and type(d.get('bytes')) is int and d.get('sha256') == p.get('raw_sha256'),'proof measured delivery differs')
        need(not native.get('resource_refusal') and not native.get('proof_cap_hit') and not native.get('lifecycle_error') and not native.get('bounded_unknown'),'worker anomaly')
        need(job['solver_binary_sha256'] == r['solver_binary_sha256'] and job['checker_binary_sha256'] == r['checker_binary_sha256'],'binary identity differs')
    except (OSError,ValueError,KeyError,TypeError,AttributeError) as exc:
        errors.append('missing/invalid supervised binding: '+repr(exc))
    return errors
