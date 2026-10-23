"""Constructive replacement for slow unseeded SAT positive controls: pin every primary L/S variable to
four explicit classical MOLS L_a(i,j)=a*i+j mod7, using slopes1..4. Only auxiliaries are left to SAT.
The base CNFs keep P1-P3 but drop P4/SB2. A SAT assignment to the strengthened CNF is checked against every
base clause, proving the original relaxed instance SAT without the difficult unseeded search.
Also fixes an intentionally colliding pair of slopes and requires UNSAT (a small consistency control).
Usage: python3 -B moqls7_parent_classical_controls.py NEW_OUTPUT_DIR
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo
import moqls7_parent_positive_controls as parent

HERE = Path(__file__).resolve().parent
PIN = HERE / 'moqls7-parent-inputs-r2'


def save(path, data):
    with path.open('x') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def bindings(path, enc, generic, collide=False):
    data = json.loads(path.read_text())
    variables = data['vars'] if enc == 'A' else data
    units = []
    labels = set()
    for name, var in variables.items():
        item = json.loads(name)
        if not isinstance(item, list):
            continue
        if enc == 'A':
            label, cell, symbol = item
            if not label.startswith(('L', 'S')):
                continue
            i, j = cell
            s = int(label[1:])
            slope = s - (4 - generic) if label.startswith('L') else generic + s
            if collide and label == 'S1':
                slope = 1
        else:
            if item[0] not in ('L', 'S'):
                continue
            kind, s, i, j, symbol = item
            label = kind + str(s)
            slope = s - 2 if kind == 'L' else generic + s
            if collide and kind == 'S' and s == 1:
                slope = 1
        labels.add(label)
        units.append(var if symbol == (slope * i + j) % 7 else -var)
    if len(labels) != 4 or not units:
        raise ValueError('primary-variable map did not specify four squares')
    return units


def constrain(base, dest, units):
    with base.open() as src, dest.open('x') as out:
        header = False
        for line in src:
            if line.startswith('p cnf '):
                _, _, nv, nc = line.split()
                out.write(f'p cnf {nv} {int(nc) + len(units)}\n')
                header = True
            else:
                out.write(line)
        if not header:
            raise ValueError('missing CNF header')
        for lit in units:
            out.write(f'{lit} 0\n')


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(exist_ok=False)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'driver_sha256': parent.sha(__file__), 'status': 'FAILED', 'runs': []}
    try:
        manifest = json.loads((PIN / 'manifest.json').read_text())
        for enc in 'AB':
            rel = f'code/k2_encode_{enc.lower()}_r2.py'
            if parent.sha(PIN / rel) != manifest['files'][rel]['sha256']:
                raise ValueError('encoder changed')
        for m in (2, 3, 4):
            generic = 4 - m
            for enc in 'AB':
                case = f'K{m}{enc}'
                base, mapping = out / (case + '.base.cnf'), out / (case + '.map.json')
                cmd = [sys.executable, '-B', str(PIN / f'code/k2_encode_{enc.lower()}_r2.py'), '--mode', 'generic',
                       '--quantum', ''.join(map(str, range(1, m + 1))), '--ngeneric', str(generic), '--p4', 'none',
                       '--cnf', str(base), '--map', str(mapping)]
                p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                if p.returncode:
                    raise ValueError('encoding failed: ' + p.stderr)
                units = bindings(mapping, enc, generic)
                fixed = out / (case + '.classical.cnf')
                constrain(base, fixed, units)
                p = subprocess.run(['kissat', '-q', str(fixed)], capture_output=True, text=True, timeout=120)
                with (out / (case + '.solver.txt')).open('x') as f:
                    f.write(p.stdout + p.stderr)
                assignment = {int(t) for line in p.stdout.splitlines() if line.startswith('v ') for t in line[2:].split() if int(t) > 0}
                ok, count = parent.check_model(base, assignment) if p.returncode == 10 else (False, 0)
                fixed_ok, fixed_count = parent.check_model(fixed, assignment) if p.returncode == 10 else (False, 0)
                with base.open() as f:
                    declared = next(int(line.split()[3]) for line in f if line.startswith('p cnf '))
                row = {'case': case, 'encoder_command': cmd, 'base_cnf_sha256': parent.sha(base),
                       'fixed_cnf_sha256': parent.sha(fixed), 'bound_primary_literals': len(units),
                       'solver_exit': p.returncode, 'base_clauses_checked': count,
                       'every_base_clause_satisfied': ok and count == declared,
                       'every_fixed_clause_satisfied': fixed_ok and fixed_count == declared + len(units)}
                result['runs'].append(row)
                if not row['every_base_clause_satisfied'] or not row['every_fixed_clause_satisfied']:
                    raise ValueError('classical assignment failed: ' + case)
                print(json.dumps({'case': case, 'status': 'SAT_MODEL_CHECKED', 'base_clauses': count}), flush=True)
                if case == 'K2B':
                    bad = out / 'K2B.colliding-slopes.cnf'
                    constrain(base, bad, bindings(mapping, enc, generic, collide=True))
                    p = subprocess.run(['kissat', '-q', str(bad)], capture_output=True, text=True, timeout=120)
                    result['colliding_slopes_control'] = {'solver_exit': p.returncode, 'expected_exit': 20,
                                                          'scope': 'Consistency control only; not a main UNSAT certificate.'}
                    if p.returncode != 20:
                        raise ValueError('colliding slopes were not rejected')
        result['status'] = 'ALL_SIX_CLASSICAL_POSITIVE_CONTROLS_PASS'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    save(out / 'parent-result.json', result)
    print(result['status'], result.get('error', ''), flush=True)
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
