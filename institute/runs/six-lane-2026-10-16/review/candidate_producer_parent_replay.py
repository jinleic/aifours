"""Rebuild and replay the two newly pinned finite-certificate producers, without touching lanes.
Usage: python3 -B candidate_producer_parent_replay.py pc100|mc38
Each invocation writes a new case-specific directory and refuses overwrite. Search success is
not certificate validity: every regenerated certificate is passed to the parent definition checker.
"""
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('pc100', 'mc38'):
        raise SystemExit('Usage: candidate_producer_parent_replay.py pc100|mc38')
    case = sys.argv[1]
    out = HERE / ('point-cyclic100-producer-parent-replay-v1' if case == 'pc100' else 'mcdsqs38-producer-parent-replay-v1')
    out.mkdir(exist_ok=False)
    (out / 'code').mkdir()
    (out / 'logs').mkdir()
    (out / 'tmp').mkdir()
    result = {'status': 'FAILED', 'case': case, 'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'driver_sha256': sha(__file__), 'steps': [], 'pins': {}}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0', OMP_NUM_THREADS='1',
               OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1', TMPDIR=str(out / 'tmp'))

    def run(name, args, timeout=900):
        start = time.monotonic()
        p = subprocess.run([str(a) for a in args], cwd=out, env=env, capture_output=True, text=True, timeout=timeout)
        (out / 'logs' / (name + '.stdout')).write_text(p.stdout)
        (out / 'logs' / (name + '.stderr')).write_text(p.stderr)
        row = {'name': name, 'command': [str(a) for a in args], 'returncode': p.returncode,
               'wall_seconds': round(time.monotonic() - start, 3)}
        result['steps'].append(row)
        print(json.dumps(row), flush=True)
        require(p.returncode == 0, 'command failed: ' + name)
        return p

    def copy(source, relative, digest):
        require(sha(source) == digest, 'source SHA mismatch ' + str(source))
        dest = out / relative
        shutil.copyfile(source, dest)
        require(sha(dest) == digest, 'copy SHA mismatch ' + relative)
        result['pins'][relative] = {'source': str(source.relative_to(ROOT)), 'sha256': digest}
        return dest

    try:
        if case == 'pc100':
            lane = ROOT / 'information-science/evidence/six-lane-20261016/point-cyclic100'
            pin = HERE / 'point-cyclic100-parent-inputs-v1'
            cert_sha = '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1'
            seed_sha = 'ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245'
            require(sha(pin / 'pc100_t2.cert') == cert_sha, 'certificate pin')
            copy(pin / 'pc100_t2.seed', 'pinned.seed', seed_sha)
            copy(lane / 'code/t2_tabu.c', 'code/t2_tabu.c', 'bc5d00f9b37a96b1bfca9826d9fbb3017ae9f6bde03e8e3c1ec3f97593032411')
            copy(lane / 'code/pc_expand.py', 'code/pc_expand.py', '8fe20ef270defd0924c3c4fc296919fc6ffe8bf9fcaeae6c1ed8cfd687ff25c6')
            run('compiler-version', ['clang', '--version'])
            run('compile', ['clang', '-O2', '-o', out / 't2_tabu', out / 'code/t2_tabu.c'])
            result['rebuilt_binary_sha256'] = sha(out / 't2_tabu')
            run('discovery', [out / 't2_tabu', '25', '1', '120', out / 'regenerated', '8', '8', '3000', '4', '1'], 300)
            require(sha(out / 'regenerated.seed') == seed_sha, 'discovery did not reproduce seed bytes')
            run('expand', ['/usr/bin/python3', '-B', out / 'code/pc_expand.py', out / 'regenerated.seed', out / 'regenerated.cert'])
            require(sha(out / 'regenerated.cert') == cert_sha, 'expanded certificate bytes differ')
            run('parent-check', ['/usr/bin/python3', '-B', HERE / 'check_point_cyclic_resolution_independent.py',
                                 out / 'regenerated.cert', '100', cert_sha, out / 'parent-check.json'])
            result['checks'] = {'seed_byte_identical': True, 'certificate_byte_identical': True,
                                'regenerated_certificate_parent_status': json.loads((out / 'parent-check.json').read_text())['status']}
        else:
            lane = ROOT / 'mathematics/evidence/six-lane-20261016/mcdsqs38'
            pin = HERE / 'mcdsqs38-parent-inputs-v1'
            cert_sha = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
            seed_sha = 'b945898255dec37f7a6ef98a099a7ed89e60b3aa07a8fd4af0bf50567f6b187e'
            require(sha(pin / 'mcdsqs38_g342_s0.txt') == cert_sha, 'certificate pin')
            copy(lane / 'evidence/mcdsqs38-g342/mcdsqs38_g342_s0_seed.json', 'pinned-seed.json', seed_sha)
            pins = {'expand_seed.py': '31bcd91c7039fcc32ddca4265ea96de660b2fb2e1002b4300b75f61c09ccb424',
                    'pipeline.py': '4dc82fb63aad8aea6a6025ce66e0d87c8c220df2fdf4534c1085e1996e8ceabf',
                    'mcdsqs_lib.py': '6f4c680265380a10d99b653d60e26e0bdbf1d359a025c6b38f4c33d04815c391',
                    'ppcsym.py': 'ea43b344a80008cfeab11aab9748180a373129fe738402b0982551ba98085276',
                    'check_mcdsqs.py': 'e2dc212d90119494f46e72807fcf64e82b0b9f842c23ffc27335f47a6a7f63a3',
                    'check_mcdsqs.c': '7d04c404ad37485aa96f7384f8d502a9c364f97f140704e240d855ec79bc72bd'}
            for name, digest in pins.items():
                copy(lane / 'code' / name, 'code/' + name, digest)
            run('expand-seed', ['/usr/bin/python3', '-B', out / 'code/expand_seed.py', out / 'pinned-seed.json',
                                out / 'expanded.txt', pin / 'mcdsqs38_g342_s0.txt'])
            require(sha(out / 'expanded.txt') == cert_sha, 'seed expansion mismatch')
            python = '/Users/jinleic/.local/state/research-explorer/venv/bin/python'
            run('versions', [python, '-B', '-c', 'import sys,numpy; print(sys.version); print("numpy",numpy.__version__)'])
            run('solver-version', ['kissat', '--version'])
            # The original producer removes failed colouring CNFs. Forbid removal in this replay;
            # the successful, deterministic single-sample path never invokes the guard.
            wrapper = ('import os,runpy,sys\n'
                       'def retain(*a,**k): raise RuntimeError("Replay forbids evidence deletion")\n'
                       'os.remove=retain;os.unlink=retain\n'
                       'sys.path.insert(0,os.path.dirname(sys.argv[1]))\n'
                       'sys.argv=sys.argv[1:];runpy.run_path(sys.argv[0],run_name="__main__")\n')
            (out / 'preserve_evidence.py').write_text(wrapper)
            run('pipeline', [python, '-B', out / 'preserve_evidence.py', out / 'code/pipeline.py', '38', out / 'pipeline',
                             '--affine', '1:2,3:1', '--res-mult', '9', '--samples', '1', '--col-timeout', '60',
                             '--km-timeout', '600', '--workers', '1'], 900)
            generated = out / 'pipeline/mcdsqs38_sample0.txt'
            require(sha(generated) == cert_sha, 'full producer certificate bytes differ')
            run('parent-check', ['/usr/bin/python3', '-B', HERE / 'check_mcdsqs_independent.py', generated, '38',
                                 cert_sha, out / 'parent-check.json'])
            run('compile-lane-C-checker', ['clang', '-O2', '-std=c11', '-o', out / 'check_mcdsqs', out / 'code/check_mcdsqs.c'])
            run('lane-C-candidate', [out / 'check_mcdsqs', pin / 'mcdsqs38_g342_s0.txt'])
            for v in (26, 32):
                run('lane-C-control-' + str(v), [out / 'check_mcdsqs', lane / 'controls' / ('tanzhou_mcdsqs' + str(v) + '.txt')])
            result['checks'] = {'seed_byte_identical': True, 'full_producer_byte_identical': True,
                                'regenerated_certificate_parent_status': json.loads((out / 'parent-check.json').read_text())['status'],
                                'parent_compiled_lane_C_checker': 'PASS on candidate and published 26/32 controls',
                                'KM_cnf_sha256': sha(out / 'pipeline/km_0.cnf'),
                                'colouring_cnf_sha256': sha(out / 'pipeline/col_0.cnf')}
        result['status'] = 'PARENT_REBUILT_PRODUCER_BYTE_REPLAY_AND_DEFINITION_CHECK_PASS'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        with (out / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2); f.write('\n')
        print(json.dumps(result, indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
