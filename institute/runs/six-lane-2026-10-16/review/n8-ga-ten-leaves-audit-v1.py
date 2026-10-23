"""Parent receipt/log audit for completed GA run 20261018T143444; no solver execution."""
import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

R = Path(__file__).resolve().parent
D = R / 'moqls8-strengthened-parent-replay-v1'
P = D / 'PRE-EXEC-v5d-leaves-parent-a1.json'
S = D / 'runs/run-20261018T143444.json'
OUT = R / 'n8-ga-ten-leaves-parent-audit-v1.json'
EXPECTED_PRE = '3886ed710fce6cad542f44e7d5a3e58214a0ea6b745893d93b38555e676d189a'
EXPECTED_RUN = '45c840acee747eca39423ae841d8aa6c01b2ce4c62efc1112ce8615723e9fff5'
EXPECTED_NEW = {'P1-B4', 'P0-B6', 'P1-B6', 'P2-C4', 'P2-C3', 'P0-B1', 'P0-B2', 'P0-B3', 'P2-C2', 'P2-C1'}
cache = {}

def digest(p):
    p = Path(p)
    if p not in cache:
        hs = hashlib.sha256()
        with p.open('rb') as f:
            for part in iter(lambda: f.read(1048576), b''):
                hs.update(part)
        cache[p] = hs.hexdigest()
    return cache[p]

def pin(p):
    p = Path(p)
    return {'path': str(p), 'sha256': digest(p), 'bytes': p.stat().st_size}

def stamp():
    s = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], text=True).strip()
    return s[:-2] + ':' + s[-2:]

assert not OUT.exists()
assert digest(P) == EXPECTED_PRE and digest(S) == EXPECTED_RUN
pre = json.loads(P.read_text())
run = json.loads(S.read_text())
binding = pre['inputs']['parent_binding']
assert digest(binding['result']) == binding['result_sha256']
assert digest(binding['manifest']) == binding['manifest_sha256']
assert digest(binding['script']) == binding['script_sha256']
assert digest(pre['inputs']['source_cnf']) == pre['inputs']['source_cnf_sha256']
for rel, sha in pre['inputs']['pins_verified'].items():
    assert digest(Path(pre['inputs']['lane']) / rel) == sha
bound = {x['id']: x for x in json.loads(Path(binding['result']).read_text())['leaves']}
manifest = {x['id']: x for x in json.loads(Path(binding['manifest']).read_text())['cases']}
pre_items = {x['item']: x for x in pre['items']}
assert run['stopped_reason'] is None and not run['events'] and not run['helper_survivors']
assert digest(D / run['driver_log']) == run['driver_log_sha256_at_close']
assert digest(D / pre['script']['path']) == pre['script']['sha256'] == run['script_sha256']
assert digest(pre['python']['realpath']) == pre['python']['sha256']
control_hashes = {x['label']: x['receipt_sha256'] for x in pre['admission_controls']}
for control in pre['admission_controls']:
    assert digest(D / control['receipt']) == control['receipt_sha256']
    assert json.loads((D / control['receipt']).read_text())['verdict'] == control['verdict']
monitor_raw = (R / 'disk-monitor-v1-20261018T0722-to-1810.jsonl').read_bytes()
items = []
for ent in run['items']:
    if ent['status'] == 'SKIPPED':
        assert ent['item'] in ('leaf:P0-B4', 'leaf:P0-B5')
        continue
    p = D / ent['receipt']
    rr = json.loads(p.read_text())
    it, pp = rr['item'], rr['pipeline']
    bad = []
    def need(ok, label):
        if not ok:
            bad.append(label)
    need(digest(p) == ent['receipt_sha256'], 'receipt digest')
    need(it == pre_items[ent['item']], 'exact frozen item')
    need(it['id'] in EXPECTED_NEW, 'expected new leaf')
    need(rr['verdict'] == ent['verdict'] == 'PASS' and not rr['reasons'], 'PASS verdict')
    need(all(v is True for v in rr['criteria'].values()), 'recorded predicates')
    need(rr['run_tag'] == run['run_tag'], 'run tag')
    need(digest(D / rr['pre_exec']['path']) == rr['pre_exec']['sha256'] == EXPECTED_PRE, 'preexec binding')
    need(digest(D / rr['script']['path']) == rr['script']['sha256'] == pre['script']['sha256'], 'script binding')
    need(it['bound_cnf_sha256'] == bound[it['id']]['cnf_sha256'] == manifest[it['id']]['cnf_sha256'], 'formula parent/manifest binding')
    need(it['units'] == manifest[it['id']]['units'] and it['supports_row2to7'] == manifest[it['id']]['supports_row2to7'], 'template and units binding')
    identity = rr['post_gate_identity']
    need(identity['ok'] is True and not identity['problems'] and identity['hashed'] == identity['expected'], 'post-gate identity')
    need(identity['controls_equal_pre_exec'] is True and {x['label']: x['receipt_sha256'] for x in identity['controls_revalidated']} == control_hashes, 'five controls binding')
    need(identity['hashed']['python_sha256'] == digest(pre['python']['realpath']), 'interpreter rehash')
    for name in ('cadical', 'drat-trim'):
        need(digest(rr['binaries'][name]['path']) == rr['binaries'][name]['sha256'], name + ' binary rehash')
    for which in ('solver', 'checker'):
        w = pp['writers'][which + '_feed']
        need(w['ok'] is True and w['thread_finished'] is True and not w.get('close_errors'), which + ' writer settled')
        need(w['written'] == w['expected_len'] == it['expected_' + which + '_feed_bytes'], which + ' measured feed length')
        need(w['sha256'] == it['expected_' + which + '_feed_sha256'] == it['bound_cnf_sha256'], which + ' measured feed hash')
    sl = (D / pp['solver_log']).read_bytes()
    cl = (D / pp['checker_log']).read_bytes()
    need(hashlib.sha256(sl).hexdigest() == pp['solver_log_sha256'] and len(sl) == pp['solver_log_bytes'], 'raw solver log binding')
    need(hashlib.sha256(cl).hexdigest() == pp['checker_log_sha256'] and len(cl) == pp['checker_log_bytes'], 'raw checker log binding')
    s_lines = sl.replace(b'\r', b'').decode().split('\n')
    c_lines = cl.replace(b'\r', b'').decode().split('\n')
    need([l for l in s_lines if l.startswith('s')] == ['s UNSATISFIABLE'], 'exact solver status')
    need([l for l in c_lines if l.startswith('s')] == ['s VERIFIED'], 'exact checker status, CR-only normalization')
    need(pp['children']['solver']['rc'] == 20 and pp['children']['checker']['rc'] == 0, 'native return codes')
    need(all(x.get('reaped_at') for x in pp['children'].values()), 'children reaped')
    parsed = [int(m.group(1)) for l in c_lines if (m := re.fullmatch(r'c finished parsing, read (\d+) bytes from proof file', l))]
    headers = [list(map(int, m.groups())) for l in c_lines if (m := re.fullmatch(r'c parsing input formula with (\d+) variables and (\d+) clauses', l))]
    relay = pp['relay']
    n, sha = relay['read_bytes'], relay['read_sha256']
    need(n > 0 and n == relay['delivered_bytes'] == pp['proof_stream_bytes'] and parsed == [n], 'read/delivered/checker-consumed proof bytes')
    need(sha == relay['delivered_sha256'] == pp['proof_stream_sha256'], 'measured proof digest equality')
    need(relay['ok'] is True and relay['fifo_eof_seen'] is True and relay['thread_finished'] is True and not relay['close_errors'] and relay['withheld_bytes'] == 0, 'relay settled and EOF')
    need(not relay['checker_exited_before_relay_finished'], 'checker did not finish before relay')
    need(headers == [it['expected_checker_header_counts']], 'checker input header')
    need(not any('early EOF' in l or 'clauses less than expected' in l or l.startswith('c ERROR:') for l in c_lines), 'no checker input errors')
    need(rr['stop_latched'] is None and rr['stop_latched_after_evaluation'] is None and pp['stop_latched_during_pipeline'] is None and pp['safety_stop_reason'] is None, 'no stop latch')
    need(not pp['events'] and not pp['helper_survivors'] and not pp['threads']['unfinished'] and not pp['sigterm_grace_exceeded'], 'no events/survivors/unfinished work')
    scan = pp['lane_scanner']
    need(scan['failed'] is None and scan['failures'] == 0 and scan['alive_after_join'] is False, 'scanner clean settlement')
    need(pp['min_free_bytes_in_flight'] >= 12000000000 and pp['peak_lane_total_rss_bytes'] <= pp['lane_rss_limit_bytes'] and pp['peak_desk_aggregate_rss_bytes'] <= pp['desk_stop_bytes'], 'resource limits')
    gates = rr['gate']['samples'][-2:]
    need(len(gates) == 2 and gates[-1]['streak'] >= 2, 'two admission passes')
    for gs in gates:
        st = gs['stability']
        need(all(gs[k] is True for k in ('ok_disk', 'ok_busy', 'ok_rss', 'ok_stable')), 'admission predicates')
        need(st['ok'] is True and all(st['checks'].values()), 'stability predicates')
        need(st['window_samples'] >= 25 and st['window_span_seconds'] >= 290 and 0 <= st['last_age_seconds'] <= 30 and st['last_free'] >= 13500000000 + 10485760 and st['max_peak_to_later_drop_bytes'] <= max(300000000, (st['last_free'] - 13500000000) // 12), 'stability numbers')
        prefix = monitor_raw[:st['monitor_bytes']]
        need(hashlib.sha256(prefix).hexdigest() == st['monitor_sha256_at_read'], 'retained monitor prefix binding')
    need((datetime.fromisoformat(gates[1]['at']) - datetime.fromisoformat(gates[0]['at'])).total_seconds() >= 60, 'admission pass separation')
    items.append({'item': it['item'], 'receipt': pin(p), 'problems': bad, 'formula_sha256': it['bound_cnf_sha256'], 'formula_bytes': it['expected_solver_feed_bytes'], 'proof_stream_sha256': sha, 'proof_bytes_read': n, 'proof_bytes_delivered': relay['delivered_bytes'], 'checker_N': parsed, 'solver_status': 'rc20 s UNSATISFIABLE', 'checker_status': 'rc0 s VERIFIED', 'solver_log': pin(D / pp['solver_log']), 'checker_log': pin(D / pp['checker_log']), 'peak_desk_rss_bytes': pp['peak_desk_aggregate_rss_bytes'], 'min_free_bytes': pp['min_free_bytes_in_flight'], 'pipeline_seconds': pp['pipeline_seconds']})
assert {x['item'].split(':')[1] for x in items} == EXPECTED_NEW and len(items) == 10
ps = subprocess.check_output(['/bin/ps', '-axo', 'pid,ppid,comm'], text=True)
# No long model prompts or unrelated arguments are captured.
survivors = [l.strip() for l in ps.splitlines() if any('/' + x in l for x in ('cadical', 'drat-trim', 'kissat'))]
result = {'at': stamp(), 'status': 'PARENT_QUALIFIED_PASS' if not survivors and all(not x['problems'] for x in items) else 'NOT_QUALIFIED', 'script': pin(__file__), 'run_summary': pin(S), 'pre_exec': pin(P), 'foreground_job': 'bg_2350', 'driver_exit_code': 0, 'controls_audit': pin(R / 'n8-v5d-native-control-parent-audit-v1.json'), 'native_survivors_after_exit': survivors, 'items': items, 'scope': 'Ten new exact-input GA leaf refutations only, supplementing the two earlier leaves and four strengthened formulas: GA16/18. GA P1-B2.M2 and P1-B3.M2 remain unqualified. GB and final n8 composition are not discharged.', 'method': 'Parent raw logs rehashed; exact CR-only statuses/native return codes, measured complete CNF feeds, formula identities against parent binding and producer manifest, positive and equal read/delivered/checker-consumed proof counts and measured digests, EOF/threads/scanner/native settlement, absence of stop latches, controls/source/binaries/interpreter pins and admission/resource predicates. No new solver run.', 'limits': 'Streamed proof payloads are not retained. Recorded digest equality is provenance, not a second proof-checking implementation. CPython, drat-trim, OS and hardware remain trusted.'}
with OUT.open('x') as f:
    json.dump(result, f, indent=1)
    f.write('\n')
print(result['status'], 'new_leaves', len(items), 'problems', {x['item']: x['problems'] for x in items if x['problems']}, 'survivors', survivors)
print(str(OUT), digest(OUT))
raise SystemExit(0 if result['status'] == 'PARENT_QUALIFIED_PASS' else 2)
