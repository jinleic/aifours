#!/usr/bin/env python3
"""ADD-25 stage: extract canonical P23 offset pairs, then run the separately written Gray checker
(crt3_graycheck_c21v1, count mode, rank cap26, native wall600s each) on every written beta.
Usage: p23_gray_stage_c21v1.py OUTDIR
One native child at a time; SIGTERM/SIGINT forwarded; no Python timeout, kill or SIGKILL.
Exit10 if any checked lift is FOUND (candidate DM written by the checker); 20 if every case is
ZERO_FOR_THIS_BETA; 0 otherwise (UNKNOWN). Restricted P23 sub-family only.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
GRAY = ROOT / 'bin/crt3_graycheck_c21v1'
STOP = False
CHILD = None


def term(signum, frame):
    global STOP
    STOP = True
    if CHILD is not None:
        try:
            CHILD.send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    global CHILD
    out = Path(sys.argv[1])
    os.mkdir(out)
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)
    spec = importlib.util.spec_from_file_location('c21_p23_extract', ROOT / 'code/offset_p23_canonical_c21v1.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sys.argv = [sys.argv[0], str(out / 'betas')]
    mod.main()
    pairs = json.loads((out / 'betas/record.json').read_text())['pairs']
    results, found, zero = [], False, 0
    for pair in pairs:
        if STOP:
            break
        beta = out / 'betas' / pair['beta']
        prefix = out / ('gray-key-%d' % pair['key'])
        with open(str(prefix) + '.out', 'xb') as log:
            CHILD = subprocess.Popen([str(GRAY), 'count', '7', '7', str(beta), str(prefix), '600', '26'],
                                     stdout=log, stderr=subprocess.STDOUT)
            rc = CHILD.wait()
            CHILD = None
        status = [l.split('=', 1)[1] for l in Path(str(prefix) + '.out').read_text().splitlines() if l.startswith('status=')]
        results.append({'key': pair['key'], 'rc': rc, 'status': status[-1] if status else None,
                        'out_sha256': sha(str(prefix) + '.out')})
        found |= rc == 10
        zero += rc == 20
    complete = not STOP and len(results) == len(pairs)
    verdict = 'FOUND' if found else 'ALL-ZERO' if complete and zero == len(pairs) else 'UNKNOWN'
    rec = {'clock': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'program_sha256': sha(__file__),
           'gray_sha256': sha(GRAY), 'pairs': len(pairs), 'results': results, 'verdict': verdict,
           'scope': 'canonical representatives of the P23 common-slope sub-family only'}
    with open(out / 'record.json', 'x') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(rec), flush=True)
    raise SystemExit(10 if found else 20 if verdict == 'ALL-ZERO' else 0)


if __name__ == '__main__':
    main()
