"""Parent regeneration of the six MOQLS(7) K2/K3/K4 CNFs from the pinned encoder copies, byte comparison
with the lane's solver inputs, and independent checking of the lane's DRAT proofs with a parent-compiled
drat-trim built from upstream source (marijnheule/drat-trim master 2e3b2dc0).

Never runs lane code other than the two pinned encoder copies; never modifies, moves or deletes lane files.
Usage: python3 -B moqls7_parent_proofcheck.py NEW_OUTPUT_DIR [CASE ...]   (CASE in K2A K2B K3A K3B K4A K4B)
"""
from concurrent.futures import ThreadPoolExecutor
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
TOOLS = HERE / 'moqls7-parent-proofcheck-tools-v1'
LANE = HERE.parents[3] / 'physics/evidence/six-lane-20261016/moqls7-problem16/evidence'
DRAT_SRC_SHA = 'd834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee'
CLASS_ARGS = {'K2': ['--quantum', '12', '--ngeneric', '2', '--p4', '12'],
              'K3': ['--quantum', '123', '--ngeneric', '1', '--p4', '123'],
              'K4': ['--quantum', '1234', '--ngeneric', '0', '--p4', '1234']}
LANE_FILES = {'K2A': ('k2', 'a_generic_sb2'), 'K2B': ('k2', 'b_generic_sb2'),
              'K3A': ('k3', 'a_k3_sb2'), 'K3B': ('k3', 'b_k3_sb2'),
              'K4A': ('k4', 'a_k4_sb2'), 'K4B': ('k4', 'b_k4_sb2')}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 22), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: NEW_OUTPUT_DIR [CASE ...]')
    out = Path(sys.argv[1]).resolve()
    cases = sys.argv[2:] or list(LANE_FILES)
    out.mkdir(exist_ok=False)
    (out / 'cnf').mkdir()
    (out / 'logs').mkdir()
    result = {'started_at_pt': stamp(), 'status': 'FAILED', 'driver_sha256': sha(__file__), 'cases': {}}
    try:
        manifest = json.loads((SNAP / 'manifest.json').read_text())
        for rel in ['code/k2_encode_a.py', 'code/k2_encode_b.py']:
            if sha(SNAP / rel) != manifest['files'][rel]['sha256']:
                raise ValueError('snapshot encoder changed: ' + rel)
        result['encoders'] = {rel: manifest['files'][rel]['sha256'] for rel in ['code/k2_encode_a.py', 'code/k2_encode_b.py']}
        if sha(TOOLS / 'drat-trim.c') != DRAT_SRC_SHA:
            raise ValueError('drat-trim source changed')
        binary = out / 'drat-trim'
        comp = subprocess.run(['cc', '-O2', '-o', str(binary), str(TOOLS / 'drat-trim.c')], capture_output=True, text=True)
        (out / 'logs/compile.stderr').write_text(comp.stderr)
        if comp.returncode != 0:
            raise ValueError('drat-trim compile failed')
        result['drat_trim'] = {'source_sha256': DRAT_SRC_SHA, 'upstream': 'github.com/marijnheule/drat-trim master 2e3b2dc0 (2024-11-25)',
                               'binary_sha256': sha(binary), 'compile': 'cc -O2'}

        def one(case):
            rec = {'case': case}
            cls, enc = case[:2], case[2]
            sub, stem = LANE_FILES[case]
            cnf = out / 'cnf' / (stem + '.cnf')
            cmd = [sys.executable, '-B', str(SNAP / 'code' / ('k2_encode_' + enc.lower() + '.py')), '--mode', 'generic', '--sb2',
                   *CLASS_ARGS[cls], '--cnf', str(cnf)]
            if enc == 'A':
                cmd += ['--map', str(out / 'cnf' / (stem + '.map.json'))]
            t = time.monotonic()
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
            (out / 'logs' / (case + '.encode.stdout')).write_text(p.stdout)
            (out / 'logs' / (case + '.encode.stderr')).write_text(p.stderr)
            rec['encode'] = {'command': cmd, 'returncode': p.returncode, 'seconds': round(time.monotonic() - t, 2)}
            if p.returncode != 0:
                rec['status'] = 'ENCODE_FAILED'
                return rec
            lane_cnf, lane_drat = LANE / sub / (stem + '.cnf'), LANE / sub / (stem + '.drat')
            rec['parent_cnf_sha256'] = sha(cnf)
            rec['lane_cnf_sha256'] = sha(lane_cnf)
            rec['cnf_bytes_equal'] = rec['parent_cnf_sha256'] == rec['lane_cnf_sha256']
            if not rec['cnf_bytes_equal']:
                rec['status'] = 'CNF_MISMATCH'
                return rec
            rec['lane_proof_sha256_before'] = sha(lane_drat)
            rec['lane_proof_bytes'] = lane_drat.stat().st_size
            t = time.monotonic()
            log = out / 'logs' / (case + '.drat-trim.txt')
            with log.open('w') as f:
                p = subprocess.run([str(binary), str(cnf), str(lane_drat), '-t', '20000'], stdout=f, stderr=subprocess.STDOUT, timeout=21000)
            rec['check'] = {'returncode': p.returncode, 'seconds': round(time.monotonic() - t, 1), 'log': str(log.relative_to(out))}
            text = log.read_text(errors='replace')
            rec['verified_line'] = any(line.strip() == 's VERIFIED' for line in text.splitlines())
            rec['lane_proof_sha256_after'] = sha(lane_drat)
            rec['proof_unchanged_during_check'] = rec['lane_proof_sha256_before'] == rec['lane_proof_sha256_after']
            rec['status'] = 'VERIFIED' if rec['verified_line'] and rec['proof_unchanged_during_check'] else 'NOT_VERIFIED'
            return rec

        with ThreadPoolExecutor(max_workers=3) as ex:
            for rec in ex.map(one, cases):
                result['cases'][rec['case']] = rec
                print(json.dumps({k: rec.get(k) for k in ['case', 'status', 'cnf_bytes_equal', 'check']}), flush=True)
        ok = all(r.get('status') == 'VERIFIED' for r in result['cases'].values())
        result['status'] = 'PARENT_CNF_REGENERATION_AND_DRAT_CHECK_PASS' if ok and len(result['cases']) == len(cases) else 'INCOMPLETE_OR_FAILED'
        result['scope'] = ('Certifies that each listed CNF, regenerated byte-identically by the parent from the pinned encoders with the '
                           'stated arguments, is UNSAT, via the lane proof checked by a parent-compiled upstream drat-trim. The '
                           'mathematical bridge from configurations to these CNFs rests on the written reduction and its reviews.')
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = stamp()
        with (out / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps({k: result.get(k) for k in ['status', 'error']}, indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
