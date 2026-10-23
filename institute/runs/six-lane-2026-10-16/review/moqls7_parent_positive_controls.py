"""Parent positive controls for the pinned MOQLS(7) encoders: drop only P4 and SB2 (keep generic MOLS
variables, P1-P3 and all line conditions). Classical configurations (four MOLS(7) in standard form) satisfy
every remaining condition, so each instance must be SAT; an UNSAT answer would expose over-restriction.
Also decodes nothing and trusts only the solver's SAT answer plus a direct check of the model against the
CNF clauses (no lane code beyond the pinned encoders).
Usage: python3 -B moqls7_parent_positive_controls.py NEW_OUTPUT_DIR
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'moqls7-review-snapshot-v1'
CLASS_ARGS = {'K2': ['--quantum', '12', '--ngeneric', '2'], 'K3': ['--quantum', '123', '--ngeneric', '1'],
              'K4': ['--quantum', '1234', '--ngeneric', '0']}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_model(cnf_path, model):
    clauses = 0
    with open(cnf_path) as f:
        cur = []
        for line in f:
            if line.startswith(('p', 'c')):
                continue
            for tok in line.split():
                lit = int(tok)
                if lit == 0:
                    if not any((l > 0) == (abs(l) in model) for l in cur):
                        return False, clauses
                    clauses += 1
                    cur = []
                else:
                    cur.append(lit)
    return True, clauses


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(exist_ok=False)
    manifest = json.loads((SNAP / 'manifest.json').read_text())
    result = {'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'driver_sha256': sha(__file__),
              'status': 'FAILED', 'runs': []}
    try:
        for rel in ['code/k2_encode_a.py', 'code/k2_encode_b.py']:
            if sha(SNAP / rel) != manifest['files'][rel]['sha256']:
                raise ValueError('snapshot encoder changed')
        for cls, args in CLASS_ARGS.items():
            for enc in 'AB':
                stem = f'{cls}{enc}-noP4-noSB2'
                cnf = out / (stem + '.cnf')
                cmd = [sys.executable, '-B', str(SNAP / 'code' / f'k2_encode_{enc.lower()}.py'), '--mode', 'generic',
                       *args, '--p4', 'none', '--cnf', str(cnf)]
                if enc == 'A':
                    cmd += ['--map', str(out / (stem + '.map.json'))]
                p = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
                if p.returncode != 0:
                    raise ValueError('encode failed ' + stem + ': ' + p.stderr[-300:])
                t = time.monotonic()
                s = subprocess.run(['kissat', '-q', str(cnf)], capture_output=True, text=True, timeout=1200)
                (out / (stem + '.kissat.txt')).write_text(s.stdout + s.stderr)
                model = set()
                for line in s.stdout.splitlines():
                    if line.startswith('v '):
                        model.update(int(x) for x in line[2:].split() if int(x) > 0)
                status = 'SAT' if s.returncode == 10 else 'UNSAT' if s.returncode == 20 else f'ERR{s.returncode}'
                ok_model, nclauses = check_model(cnf, model) if status == 'SAT' else (False, 0)
                row = {'instance': stem, 'encode_command': cmd, 'cnf_sha256': sha(cnf), 'solver': 'kissat -q',
                       'status': status, 'seconds': round(time.monotonic() - t, 2), 'model_satisfies_all_clauses': ok_model,
                       'clauses_checked': nclauses, 'expected': 'SAT'}
                row['as_expected'] = status == 'SAT' and ok_model
                result['runs'].append(row)
                print(json.dumps(row), flush=True)
        result['solver_version'] = subprocess.run(['kissat', '--version'], capture_output=True, text=True).stdout.strip()
        result['status'] = 'PARENT_POSITIVE_CONTROLS_PASS' if all(r['as_expected'] for r in result['runs']) else 'CONTROL_FAILURE'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        with (out / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(result['status'], result.get('error'))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
