"""Optional hardening: exercise the --sb2 code path of the pinned MOQLS(7) encoders on relaxed instances
(--no-p3, keeping P1, P2, P4 and SB2). A SAT answer with a model that satisfies every clause shows the SB2
constants do not by themselves make the encodings unsatisfiable. UNSAT or timeout is reported as such and
is NOT evidence about the main claim. Usage: python3 -B moqls7_parent_sb2_controls.py NEW_OUTPUT_DIR
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from zoneinfo import ZoneInfo
import moqls7_parent_positive_controls as pc

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'moqls7-review-snapshot-v1'
CASES = {'K4': ['--quantum', '1234', '--ngeneric', '0', '--p4', '1234'],
         'K3': ['--quantum', '123', '--ngeneric', '1', '--p4', '123'],
         'K2': ['--quantum', '12', '--ngeneric', '2', '--p4', '12']}


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(exist_ok=False)
    result = {'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'runs': []}
    manifest = json.loads((SNAP / 'manifest.json').read_text())
    for rel in ['code/k2_encode_a.py', 'code/k2_encode_b.py']:
        if pc.sha(SNAP / rel) != manifest['files'][rel]['sha256']:
            raise SystemExit('snapshot encoder changed')
    for cls, args in CASES.items():
        for enc in 'AB':
            stem = f'{cls}{enc}-sb2-noP3'
            cnf = out / (stem + '.cnf')
            cmd = [sys.executable, '-B', str(SNAP / 'code' / f'k2_encode_{enc.lower()}.py'), '--mode', 'generic', '--sb2',
                   '--no-p3', *args, '--cnf', str(cnf)]
            if enc == 'A':
                cmd += ['--map', str(out / (stem + '.map.json'))]
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            row = {'instance': stem, 'encode_command': cmd, 'encode_returncode': p.returncode}
            if p.returncode == 0:
                row['cnf_sha256'] = pc.sha(cnf)
                t = time.monotonic()
                try:
                    s = subprocess.run(['kissat', '-q', str(cnf)], capture_output=True, text=True, timeout=600)
                    (out / (stem + '.kissat.txt')).write_text(s.stdout + s.stderr)
                    status = 'SAT' if s.returncode == 10 else 'UNSAT' if s.returncode == 20 else f'ERR{s.returncode}'
                    model = {int(x) for line in s.stdout.splitlines() if line.startswith('v ')
                             for x in line[2:].split() if int(x) > 0}
                except subprocess.TimeoutExpired:
                    status, model = 'UNKNOWN_TIMEOUT_600s', set()
                row['status'] = status
                row['seconds'] = round(time.monotonic() - t, 2)
                if status == 'SAT':
                    row['model_satisfies_all_clauses'], row['clauses_checked'] = pc.check_model(cnf, model)
            result['runs'].append(row)
            print(json.dumps({k: row.get(k) for k in ['instance', 'status', 'seconds', 'model_satisfies_all_clauses']}), flush=True)
    result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    result['interpretation'] = 'Hardening only; no main-claim dependence.'
    with (out / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
