#!/usr/bin/env python3
"""Runs the comparator as a SEPARATE PROCESS on every fixture listed in FIXROOT/manifest.json and checks, per fixture,
the expected verdict, the real process exit status and the failed checks (all of must_fail; exactly them, with no
missing required check, when 'exact').  Fixture directories are only read; each verdict goes to RESDIR.
Usage: run_fixtures_p5o4_v2.py COMPARATOR FIXROOT RESDIR    (RESDIR must not exist; exit 0 iff every fixture behaves)
"""
import sys, os, json, hashlib, subprocess


def sha_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    comp, fixroot, resdir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.mkdir(resdir)
    with open(os.path.join(fixroot, 'manifest.json'), 'rb') as f:
        manifest = json.loads(f.read().decode('ascii'))
    results, all_ok = [], True
    for fx in manifest['fixtures']:
        name = fx['name']
        out = os.path.join(resdir, name + '.verdict.json')
        p = subprocess.run([sys.executable, '-B', comp, os.path.join(fixroot, name), out],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        v = None
        if os.path.isfile(out):
            with open(out, 'rb') as f:
                v = json.loads(f.read().decode('ascii'))
        failed = sorted(v['failed']) if v else None
        ok = (v is not None and p.returncode == fx['expected_exit'] and v['verdict'] == fx['expected_verdict']
              and v['exit_status'] == fx['expected_exit'] and set(fx['must_fail']) <= set(failed)
              and (not fx['exact'] or (failed == sorted(fx['must_fail']) and not v['missing_required']
                                       and not v['unexpected_checks'])))
        all_ok = all_ok and ok
        results.append({'name': name, 'ok': ok, 'expected_verdict': fx['expected_verdict'],
                        'expected_exit': fx['expected_exit'], 'verdict': v['verdict'] if v else None,
                        'returncode': p.returncode, 'failed': failed, 'must_fail': fx['must_fail'], 'exact': fx['exact'],
                        'missing_required': len(v['missing_required']) if v else None,
                        'stdout': p.stdout.decode('ascii', 'replace').strip(),
                        'stderr_tail': p.stderr.decode('ascii', 'replace').strip()[-300:],
                        'verdict_sha256': sha_file(out) if v else None})
        print(name, 'ok' if ok else 'NOT-OK', p.returncode, v['verdict'] if v else None, flush=True)
    summary = {'comparator': comp, 'comparator_sha256': sha_file(comp),
               'manifest_sha256': sha_file(os.path.join(fixroot, 'manifest.json')), 'fixtures': len(results),
               'all_ok': all_ok, 'results': results}
    with open(os.path.join(resdir, 'fixture-results.json'), 'x') as f:
        json.dump(summary, f, indent=1, sort_keys=True)
        f.write('\n')
    print('ALL-OK' if all_ok else 'NOT-ALL-OK', len(results))
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
