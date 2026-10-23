#!/usr/bin/env python3
"""Run the parent checker on the pinned candidate and on every control fixture under an interpreter matrix.

Usage: python3 -B run_matrix.py CHECKER CERT MANIFEST OUTDIR
Interpreters: /usr/bin/python3 and /opt/homebrew/bin/python3, each with flags -B and -O -B.
Runs are sequential (one busy child at a time); no timeouts, no kills. Each run writes
OUTDIR/<fixture>__<interp>__<mode>.json through the checker's --out (exclusive create); the summary goes to
OUTDIR/matrix-summary.json (exclusive create). A control counts as rejected for the intended reason iff the
checker exits 1 with verdict FAIL, no CHECKER_EXCEPTION, every intended check FAILs and, where the manifest
names an intended F06 status, a recorded F06 example carries that status.
"""
import json
import os
import subprocess
import sys
import time

INTERPRETERS = [('sys39', '/usr/bin/python3'), ('brew', '/opt/homebrew/bin/python3')]
MODES = [('B', ['-B']), ('OB', ['-O', '-B'])]


def run_one(interp, flags, checker, cert, out):
    t0 = time.perf_counter()
    proc = subprocess.run([interp] + flags + [checker, cert, '--out', out], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, universal_newlines=True)
    wall = time.perf_counter() - t0
    rep = None
    if os.path.exists(out):
        with open(out) as f:
            rep = json.load(f)
    return proc, wall, rep


def main(argv):
    if len(argv) != 5:
        sys.stderr.write('usage: run_matrix.py CHECKER CERT MANIFEST OUTDIR\n')
        return 64
    checker, cert, manifest_path, outdir = argv[1:]
    with open(manifest_path) as f:
        manifest = json.load(f)
    jobs = [('positive', cert, None)] + [(c['name'], c['fixture'], c) for c in manifest['controls']]
    rows = []
    for name, path, ctl in jobs:
        for itag, interp in INTERPRETERS:
            for mtag, flags in MODES:
                out = os.path.join(outdir, '%s__%s__%s.json' % (name, itag, mtag))
                proc, wall, rep = run_one(interp, flags, checker, path, out)
                row = {'fixture': name, 'interpreter': interp, 'flags': flags, 'exit_code': proc.returncode,
                       'stdout': proc.stdout.strip(), 'stderr': proc.stderr.strip()[-2000:],
                       'outer_wall_seconds': round(wall, 3), 'report': out}
                if rep is not None:
                    row.update({'verdict': rep.get('verdict'), 'failed_checks': rep.get('failed_checks'),
                                'first_failed_check': rep.get('first_failed_check'),
                                'not_run_checks': rep.get('not_run_checks'),
                                'input_sha256': rep['input']['sha256'],
                                'python_version': rep['python']['version'],
                                'optimize_flag': rep['python']['optimize_flag'],
                                'checker_sha256': rep['checker']['sha256'],
                                'wall_seconds': rep['timing']['wall_seconds'],
                                'max_rss_bytes': rep['max_rss_bytes']})
                if ctl is None:
                    row['expected'] = 'PASS'
                    row['ok'] = (rep is not None and proc.returncode == 0 and rep.get('verdict') == 'PASS')
                else:
                    failed = (rep or {}).get('failed_checks') or []
                    intended_ok = all(c in failed for c in ctl['intended_failed_checks'])
                    detail_ok = True
                    if ctl.get('intended_detail'):
                        chk, status = ctl['intended_detail']
                        exs = rep['checks'][chk]['examples'] if rep and chk in rep.get('checks', {}) else []
                        detail_ok = any(e.get('status') == status for e in exs)
                    row['expected'] = 'FAIL for ' + ', '.join(ctl['intended_failed_checks']) + (
                        ' with F06 status %s' % ctl['intended_detail'][1] if ctl.get('intended_detail') else '')
                    row['input_sha256_matches_manifest'] = (rep is not None and rep['input']['sha256'] == ctl['sha256'])
                    row['ok'] = (rep is not None and proc.returncode == 1 and rep.get('verdict') == 'FAIL'
                                 and 'CHECKER_EXCEPTION' not in failed and intended_ok and detail_ok
                                 and row['input_sha256_matches_manifest'])
                rows.append(row)
                sys.stdout.write('%-48s %-6s %-3s exit=%d ok=%s %s\n' % (name, itag, mtag, proc.returncode, row['ok'],
                                                                      ','.join(row.get('failed_checks') or [])))
                sys.stdout.flush()
    summary = {'checker': os.path.abspath(checker), 'candidate': os.path.abspath(cert),
               'manifest': os.path.abspath(manifest_path),
               'runs': len(rows), 'all_ok': all(r['ok'] for r in rows),
               'positive_runs_ok': [r['ok'] for r in rows if r['fixture'] == 'positive'],
               'controls_rejected_for_intended_reason': sum(1 for r in rows if r['fixture'] != 'positive' and r['ok']),
               'control_runs': sum(1 for r in rows if r['fixture'] != 'positive'),
               'rows': rows}
    with open(os.path.join(outdir, 'matrix-summary.json'), 'x') as f:
        f.write(json.dumps(summary, indent=1) + '\n')
    sys.stdout.write('ALL_OK=%s runs=%d\n' % (summary['all_ok'], len(rows)))
    return 0 if summary['all_ok'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
