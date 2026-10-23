#!/usr/bin/env python3
"""Single-protection mutation check of code/compare_p5o4_v2.py (skill evidence-analyzer-hardening-check, Sec. 3).

Each mutant removes exactly ONE protection (a line marked '# PROT-<id>' in the comparator) by ONE unique string
replacement: a check 'check(NAME, COND)' becomes 'check(NAME, True or COND)' (COND is then never evaluated); PROT-P
drops the fail-closed rule (exception or missing required check => FAIL); PROT-Q always exits 0.  The original and every
mutant run in-process on every fixture of FIXROOT/manifest.json.  The original must meet every expectation (verdict,
exit status, failed checks as in run_fixtures_p5o4_v2.py); a mutant is KILLED iff on some fixture its
(verdict, exit status) differs from the expectation.  Fixture directories are only read.
Usage: mutcheck_compare_p5o4_v2.py COMPARATOR FIXROOT OUTDIR   (OUTDIR must not exist; exit 0 iff the original meets
every expectation and every mutant is killed)
"""
import sys, os, io, json, hashlib, importlib.util, contextlib

sys.dont_write_bytecode = True
CHECK_MUTANTS = [
    ('IRF_inputs_regular_files', "check('inputs_regular_files', "),
    ('A_header', "check('header_' + tag, "),
    ('B_strata', "check('strata_' + tag, "),
    ('C_keysets', "check('keysets', "),
    ('H1_lists_identical', "check('lists_identical', "),
    ('H2_lists_wellformed', "check('lists_wellformed', "),
    ('K_mixed_empty', "check('mixed_empty', "),
    ('G2_survivor_lines', "check('survivor_lines', "),
    ('G1_survivor_set', "check('survivor_set', "),
    ('AL_avoider_lines', "check('avoider_lines', "),
    ('J_rigid_avoiders', "check('rigid_avoiders', "),
    ('L1_mutation_structure', "check('mutation_structure', "),
    ('L2_mutation_counts', "check('mutation_counts', "),
    ('S_shape', "check('%s_H%d_shape' % (tag, H), "),
    ('D_formula', "check('%s_H%d_formula' % (tag, H), "),
    ('E_examined', "check('%s_H%d_examined' % (tag, H), "),
    ('F_cover', "check('%s_H%d_cover' % (tag, H), "),
    ('I1_counts', "check('%s_H%d_counts' % (tag, H), "),
    ('I2_counts_files', "check('counts_files', "),
    ('M_controls', "check('controls', "),
    ('N_types', "check('types', "),
]
SPECIAL_MUTANTS = [
    ('P_fail_closed', "passed = not missing and not unexpected and all(checks[r] is True for r in REQUIRED)",
     "passed = all(v is True for k, v in checks.items() if k != 'no_exception')"),
    ('Q_exit_status', "sys.exit(0 if verdict == 'PASS' else 1)", "sys.exit(0)"),
]


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def load(path, modname):
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_one(mod, fixdir, outfile):
    buf = io.StringIO()
    code = None
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        try:
            mod.main([fixdir, outfile])
        except SystemExit as e:
            code = e.code
    with open(outfile, 'rb') as f:
        v = json.loads(f.read().decode('ascii'))
    return v, code


def meets(fx, v, code, full):
    if v['verdict'] != fx['expected_verdict'] or code != fx['expected_exit']:
        return False
    if not full:
        return True
    failed = sorted(v['failed'])
    return set(fx['must_fail']) <= set(failed) and (not fx['exact'] or (failed == sorted(fx['must_fail'])
                                                                        and not v['missing_required']
                                                                        and not v['unexpected_checks']))


def main():
    comp, fixroot, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(comp, 'rb') as f:
        src_b = f.read()
    src = src_b.decode('ascii')
    with open(os.path.join(fixroot, 'manifest.json'), 'rb') as f:
        man_b = f.read()
    fixtures = json.loads(man_b.decode('ascii'))['fixtures']
    os.mkdir(outdir)
    os.mkdir(os.path.join(outdir, 'mutants'))
    os.mkdir(os.path.join(outdir, 'verdicts'))
    mutants = [(mid, anchor, anchor + 'True or ') for mid, anchor in CHECK_MUTANTS] + SPECIAL_MUTANTS
    modules = [('ORIGINAL', comp, None, None)]
    for mid, anchor, repl in mutants:
        assert src.count(anchor) == 1, (mid, src.count(anchor))
        msrc = src.replace(anchor, repl)
        assert msrc != src
        mpath = os.path.join(outdir, 'mutants', mid + '.py')
        with open(mpath, 'x') as f:
            f.write(msrc)
        modules.append((mid, mpath, anchor, repl))
    report = {'comparator': comp, 'comparator_sha256': sha_bytes(src_b), 'manifest_sha256': sha_bytes(man_b),
              'fixtures': [fx['name'] for fx in fixtures], 'modules': {}}
    all_ok = True
    for mid, path, anchor, repl in modules:
        mod = load(path, 'cmp_' + mid)
        vdir = os.path.join(outdir, 'verdicts', mid)
        os.mkdir(vdir)
        per = {}
        for fx in fixtures:
            v, code = run_one(mod, os.path.join(fixroot, fx['name']), os.path.join(vdir, fx['name'] + '.json'))
            per[fx['name']] = {'verdict': v['verdict'], 'exit': code, 'failed': sorted(v['failed']),
                               'meets_expectation': meets(fx, v, code, mid == 'ORIGINAL')}
        with open(path, 'rb') as f:
            msha = sha_bytes(f.read())
        if mid == 'ORIGINAL':
            bad = [n for n, r in per.items() if not r['meets_expectation']]
            entry = {'sha256': msha, 'all_expectations_met': not bad, 'unmet': bad}
            all_ok = all_ok and not bad
        else:
            killed_by = [n for n, r in per.items() if not r['meets_expectation']]
            entry = {'sha256': msha, 'anchor': anchor, 'replacement': repl, 'killed': bool(killed_by),
                     'killed_by': killed_by, 'identity_fixture_verdict': per['F00_identity']['verdict']}
            all_ok = all_ok and bool(killed_by)
        entry['outcomes'] = {n: [r['verdict'], r['exit']] for n, r in per.items()}
        report['modules'][mid] = entry
        print(mid, 'ok' if (entry.get('all_expectations_met') or entry.get('killed')) else 'NOT-OK',
              entry.get('killed_by', entry.get('unmet')), flush=True)
    report['all_ok'] = all_ok
    report['mutants'] = len(mutants)
    report['killed'] = sum(1 for m in report['modules'].values() if m.get('killed'))
    with open(os.path.join(outdir, 'mutcheck-summary.json'), 'x') as f:
        json.dump(report, f, indent=1, sort_keys=True)
        f.write('\n')
    print('ALL-OK' if all_ok else 'NOT-ALL-OK', 'mutants', len(mutants), 'killed', report['killed'])
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
