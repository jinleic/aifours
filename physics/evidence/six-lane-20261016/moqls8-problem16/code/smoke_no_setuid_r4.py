"""ONE explicitly authorised NON-native RSS smoke, only after parent source
PASS and static controls. Production quarantine is preserved byte-for-byte.
No CaDiCaL/drat-trim/certify call. The supervised worker samples the NEW R.rss_kb
on itself and a non-setuid sleeping Python child, and exercises shared selection.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
PRODUCTION_Q = ROOT / 'evidence/N8_FONE_REFINE_R3_QUARANTINE.json'
PRODUCTION_Q_SHA = 'c5f76542ff09bbac3a4ea75a4ed2eb22787feb07a60388e8b87354d2f34c1081'
WORKER_RESULT = ROOT / 'evidence/N8_NOSETUID_R4_SMOKE.worker.json'
OUTER_RESULT = ROOT / 'evidence/N8_NOSETUID_R4_SMOKE.supervisor.json'
SMOKE_Q = ROOT / 'evidence/N8_NOSETUID_R4_SMOKE.quarantine.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'code' / (name + '.py'))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def worker():
    T = load('run_n8_fone_refine')
    supervisor = T.require_supervisor()
    R = T.load('k5_resplit_r3', T.R_SHA)
    import darwin_process_metrics as M
    if T.disk_bytes(ROOT) + 1000000 > T.LANE_CAP:
        raise RuntimeError('smoke lane data gate failed')
    child = subprocess.Popen([sys.executable, '-B', '-c', 'import time; memory=bytearray(16*1024*1024); time.sleep(4)'],
                             stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    samples = []
    for _ in range(6):
        rss = R.rss_kb([os.getpid(), child.pid])
        snap = M.shared_snapshot([str(ROOT)])
        if rss <= 0 or os.getpid() not in snap['own_PIDs'] or child.pid not in snap['own_PIDs']:
            raise RuntimeError('non-native RSS/descendant positive control failed')
        samples.append({'rss_kb': rss, 'snapshot': snap})
        time.sleep(0.25)
    if child.wait() != 0:
        raise RuntimeError('sleeping Python child did not self-exit0')
    if sha(PRODUCTION_Q) != PRODUCTION_Q_SHA:
        raise RuntimeError('production quarantine changed during smoke')
    result = {'status': 'PASS_NON_NATIVE_RSS_PATH', 'samples': samples, 'sample_count': len(samples),
              'R_source_sha256': T.R_SHA, 'certify_invocations': 0, 'cadical_or_drat_trim_invocations': 0,
              'sampler': 'real pinned libproc probe; non-setuid audited pgrep; no ps/top/lsof',
              'supervisor': supervisor, 'production_quarantine_preserved_sha256': PRODUCTION_Q_SHA,
              'sleeping_child_returncode': child.returncode, 'unknown_measurements_caught_or_ignored': False}
    T.new_json(WORKER_RESULT, result)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--worker', action='store_true')
    a = ap.parse_args()
    if a.worker:
        worker()
        return
    T = load('run_n8_fone_refine')
    A = load('launch_n8_fone_refine_r4')
    if sha(PRODUCTION_Q) != PRODUCTION_Q_SHA:
        raise RuntimeError('expected original quarantine must persist for this authorised validation')
    if shutil.disk_usage(ROOT).free - 1000000 < 12200000000:
        raise SystemExit('DEFERRED: smoke fresh12.2e9+growth gate')
    lock = A.LOCK.open('a+b')
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    # The parent explicitly authorises this NON-native validation while the
    # production quarantine persists. It is NOT permission for native reruns.
    S = A.load_file('n8_approved_smoke_supervisor', A.SUPERVISOR, A.SUP_SHA)
    rec = S.supervise([sys.executable, '-B', str(Path(__file__).resolve()), '--worker'],
                      'N8-NOSETUID-R4-NONNATIVE', 20.0, 512 * 2 ** 20, 12000000000,
                      str(ROOT), str(OUTER_RESULT), str(SMOKE_Q), grace=10.0)
    positive = json.loads(WORKER_RESULT.read_bytes()) if WORKER_RESULT.exists() else None
    success = (rec['completed_cleanly'] and not rec['uncertain'] and rec['trip_reason'] is None
               and rec['quarantine_record'] is None and positive is not None
               and positive['status'] == 'PASS_NON_NATIVE_RSS_PATH' and sha(PRODUCTION_Q) == PRODUCTION_Q_SHA)
    result = {'status': 'PASS' if success else 'FAIL_UNKNOWN', 'supervisor_record_sha256': sha(OUTER_RESULT),
              'worker_result_sha256': sha(WORKER_RESULT) if WORKER_RESULT.exists() else None,
              'supervisor_sha256': A.SUP_SHA, 'observed_unknown_probe_count': 0 if success else None,
              'completed_cleanly': rec['completed_cleanly'], 'uncertain': rec['uncertain'],
              'trip_reason': rec['trip_reason'], 'production_quarantine_preserved': sha(PRODUCTION_Q) == PRODUCTION_Q_SHA,
              'native_invocations': 0, 'script_sha256': sha(Path(__file__)),
              'scope': 'one supervised non-native NEW-R RSS-path smoke, not a proof/refutation/native leaf'}
    rh = T.new_json(ROOT / 'evidence/N8_NOSETUID_R4_SMOKE.result.json', result)
    print(json.dumps({'RESULT_sha256': rh, **result}), flush=True)
    raise SystemExit(0 if success else 3)


if __name__ == '__main__':
    main()
