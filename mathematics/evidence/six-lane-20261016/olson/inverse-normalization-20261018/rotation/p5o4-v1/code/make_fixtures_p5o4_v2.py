#!/usr/bin/env python3
"""Builds the rejection fixtures for code/compare_p5o4_v2.py from a retained run directory, which is only read.

Usage: make_fixtures_p5o4_v2.py RUNDIR FIXROOT
FIXROOT must not exist.  Every fixture is a new directory FIXROOT/<name>/ holding the comparator's nine input files
(written with open(..., 'xb')), equal to the RUNDIR files except for ONE stated defect (F00 is a byte-exact copy).
Some defects are made self-consistent (the summaries are adjusted too) so that exactly one protection can catch them.
FIXROOT/manifest.json (written last, exclusively) records for every fixture: the defect, the expected verdict and exit
status, the checks that must fail ('exact': true means the failed checks must be exactly these and no required check
may be missing), and the sha256 of every file written.
"""
import sys, os, json, hashlib

INPUTS = ['grx_summary.json', 'grx_survivors.txt', 'grx_avoiders.txt', 'grx_mutations.txt',
          'dp_summary.json', 'dp_survivors.txt', 'dp_avoiders.txt', 'dp_mutations.txt', 'dp_mixed.txt']
G_LISTS = ('grx_survivors.txt', 'grx_avoiders.txt', 'grx_mutations.txt')
BOTH = {'surv': ('grx_survivors.txt', 'dp_survivors.txt'), 'av': ('grx_avoiders.txt', 'dp_avoiders.txt'),
        'mut': ('grx_mutations.txt', 'dp_mutations.txt')}
SURV_DROP = 'H=2|Y=0,0,0,1,9|rigid=0|ndist=880'          # a non-rigid survivor of the pairs filter (no avoider)
FAKE_AV = 'H=2|dist=0,0,0,1,9/0,0,0,0,0/0,0,0,0,0/0,0,0,0,0|y=0000'   # a class of that non-rigid survivor


def sha(b):
    return hashlib.sha256(b).hexdigest()


def jload(b):
    return json.loads(b.decode('ascii'))


def jdump(o):
    return (json.dumps(o, indent=1, sort_keys=True) + '\n').encode('ascii')


def lines_of(b):
    t = b.decode('ascii')
    assert t == '' or t.endswith('\n')
    return t[:-1].split('\n') if t else []


def lines_bytes(ls):
    return ''.join(l + '\n' for l in ls).encode('ascii')


def edit(fx, name, fn):
    o = jload(fx[name])
    fn(o)
    fx[name] = jdump(o)


def edit_lines(fx, names, fn):
    for n in names:
        ls = lines_of(fx[n])
        fn(ls)
        fx[n] = lines_bytes(ls)


def refresh_g_files(fx):
    def fn(G):
        for f in G_LISTS:
            G['files'][f] = {'lines': len(lines_of(fx[f])), 'sha256': sha(fx[f])}
    edit(fx, 'grx_summary.json', fn)


def assert_sorted(fx, names):
    for n in names:
        ls = lines_of(fx[n])
        assert ls == sorted(ls) and len(set(ls)) == len(ls), n


def per_h_names(tags, hs):
    return ['%s_H%d_%s' % (t, H, x) for H in hs for t in tags for x in ('shape', 'formula', 'examined', 'cover', 'counts')]


def fx_identity(fx):
    pass


def fx_missing_stratum_g(fx):
    edit(fx, 'grx_summary.json', lambda G: G['per_H'].pop('3'))


def fx_missing_stratum_d(fx):
    edit(fx, 'dp_summary.json', lambda D: D['per_H'].pop('3'))


def fx_empty_strata(fx):
    edit(fx, 'grx_summary.json', lambda G: G.__setitem__('per_H', {}))
    edit(fx, 'dp_summary.json', lambda D: D.__setitem__('per_H', {}))


def fx_p_g(fx):
    edit(fx, 'grx_summary.json', lambda G: G.__setitem__('p', 7))


def fx_k_d(fx):
    edit(fx, 'dp_summary.json', lambda D: D.__setitem__('k', 5))


def fx_n_g(fx):
    edit(fx, 'grx_summary.json', lambda G: G.__setitem__('N', 17))


def fx_formula_consistent_g(fx):
    def fn(G):
        e = G['per_H']['1']
        e['classes_formula'] -= 625
        e['classes_allplus_solved'] -= 625
    edit(fx, 'grx_summary.json', fn)


def fx_formula_only_g(fx):
    def fn(G):
        G['per_H']['1']['classes_formula'] -= 625
    edit(fx, 'grx_summary.json', fn)


def fx_cover_only_g(fx):
    def fn(G):
        G['per_H']['1']['classes_allplus_solved'] += 1
    edit(fx, 'grx_summary.json', fn)


def fx_examined_shift_g(fx):
    def fn(G):
        e = G['per_H']['1']
        e['classes_enumerated'] += 625
        e['classes_allplus_solved'] -= 625
    edit(fx, 'grx_summary.json', fn)


def fx_formula_consistent_d(fx):
    def fn(D):
        e = D['per_H']['2']
        e['words_formula'] -= 6250
        e['words_p1prime_solved'] -= 6250
    edit(fx, 'dp_summary.json', fn)


def fx_avoider_dropped(fx):
    edit_lines(fx, BOTH['av'], lambda ls: ls.pop(0))


def drop_surv(ls):
    ls.remove(SURV_DROP)


def fx_survivor_dropped(fx):
    edit_lines(fx, BOTH['surv'], drop_surv)


def fx_survivor_dropped_consistent(fx):
    edit_lines(fx, BOTH['surv'], drop_surv)

    def fn(S):
        S['per_H']['2']['survivor_multisets'] -= 1
    edit(fx, 'grx_summary.json', fn)
    edit(fx, 'dp_summary.json', fn)
    refresh_g_files(fx)


def fx_survivor_field_flipped(fx):
    def fn(ls):
        ls[ls.index(SURV_DROP)] = SURV_DROP.replace('rigid=0', 'rigid=1')
    edit_lines(fx, BOTH['surv'], fn)
    assert_sorted(fx, BOTH['surv'])
    refresh_g_files(fx)


def fx_mutation_dropped(fx):
    edit_lines(fx, BOTH['mut'], lambda ls: ls.pop(0))


def fx_mutation_swapped(fx):
    def fn(ls):
        ls[0], ls[1] = ls[1], ls[0]
    edit_lines(fx, BOTH['mut'], fn)
    refresh_g_files(fx)


def fx_mutation_dropped_consistent(fx):
    assert lines_of(fx['grx_mutations.txt'])[0].endswith('|1')
    edit_lines(fx, BOTH['mut'], lambda ls: ls.pop(0))

    def fn(S):
        S['controls']['mutation_lines'] -= 1
        S['controls']['mutation_solvable'] -= 1
    edit(fx, 'grx_summary.json', fn)
    edit(fx, 'dp_summary.json', fn)
    refresh_g_files(fx)


def fx_extra_stratum_d(fx):
    edit(fx, 'dp_summary.json', lambda D: D['per_H'].__setitem__('5', dict(D['per_H']['4'])))


def fx_extra_key_g(fx):
    edit(fx, 'grx_summary.json', lambda G: G['per_H']['2'].__setitem__('classes_skipped', 0))


def fx_missing_input(fx):
    fx['dp_mixed.txt'] = None


def fx_malformed_json(fx):
    fx['grx_summary.json'] = fx['grx_summary.json'][:-20]


def fx_count_field_g(fx):
    def fn(G):
        G['per_H']['3']['avoider_classes'] += 1
    edit(fx, 'grx_summary.json', fn)


def fx_fake_nonrigid_avoider(fx):
    specs = ['rot:0:%d>%d' % (x, x2) for x in (3, 4) for x2 in range(5) if x2 != x]
    specs += ['blk:%d>%d' % (i, y2) for i in range(4) for y2 in range(1, 5)]
    assert len(specs) == 24

    def add_av(ls):
        ls.append(FAKE_AV)
        ls.sort()

    def add_mut(ls):
        ls.extend('%s|%s|1' % (FAKE_AV, s) for s in specs)
        ls.sort()
    edit_lines(fx, BOTH['av'], add_av)
    edit_lines(fx, BOTH['mut'], add_mut)

    def fn(S):
        e = S['per_H']['2']
        e['avoider_classes'] += 1
        e['nonrigid_avoider_classes'] += 1
        S['total_nonrigid_avoider_classes'] += 1
        S['controls']['mutation_lines'] += 24
        S['controls']['mutation_solvable'] += 24

    def fn_g(G):
        fn(G)
        G['avoider_types']['H=2|Y=0,0,0,1,9'] = 1

    def fn_d(D):
        fn(D)
        D['avoider_classes'] += 1
        D['controls']['shift_reversal_checked_classes'] += 1
    edit(fx, 'grx_summary.json', fn_g)
    edit(fx, 'dp_summary.json', fn_d)
    refresh_g_files(fx)


def fx_mixed_nonempty(fx):
    fx['dp_mixed.txt'] = (FAKE_AV + '\n').encode('ascii')
    edit(fx, 'dp_summary.json', lambda D: D.__setitem__('mixed_classes', 1))


def fx_control_p1prime_d(fx):
    edit(fx, 'dp_summary.json', lambda D: D['controls'].__setitem__('p1prime_sample_failures', 1))


def fx_types_g(fx):
    def fn(G):
        assert G['avoider_types']['H=4|Y=0,6,0,0,0'] == 20
        G['avoider_types']['H=4|Y=0,6,0,0,0'] = 21
    edit(fx, 'grx_summary.json', fn)


def fx_d_list_differs(fx):
    edit_lines(fx, ('dp_mutations.txt',), lambda ls: ls.pop(0))


def fx_files_manifest_g(fx):
    edit(fx, 'grx_summary.json', lambda G: G['files']['grx_avoiders.txt'].__setitem__('sha256', '0' * 64))


def fx_shape_d(fx):
    def fn(D):
        assert D['per_H']['2']['multisets'] == 1001
        D['per_H']['2']['multisets'] = 1000
    edit(fx, 'dp_summary.json', fn)


def fx_mutation_solvable_g(fx):
    def fn(G):
        G['controls']['mutation_solvable'] -= 1
    edit(fx, 'grx_summary.json', fn)


def fx_bool_for_int_d(fx):
    edit(fx, 'dp_summary.json', lambda D: D.__setitem__('mixed_classes', False))


def fx_float_formula_g(fx):
    def fn(G):
        G['per_H']['1']['classes_formula'] = float(G['per_H']['1']['classes_formula'])
    edit(fx, 'grx_summary.json', fn)


def fx_noncanonical_avoider(fx):
    x = lines_of(fx['grx_avoiders.txt'])[0]
    assert x.count('0,9,0,0,0|y') == 1
    x2 = x.replace('0,9,0,0,0|y', '0,9,0,0,00|y')

    def fn_av(ls):
        ls[ls.index(x)] = x2

    def fn_mut(ls):
        for i, l in enumerate(ls):
            if l.startswith(x + '|'):
                ls[i] = x2 + l[len(x):]
    edit_lines(fx, BOTH['av'], fn_av)
    edit_lines(fx, BOTH['mut'], fn_mut)
    assert_sorted(fx, BOTH['av'] + BOTH['mut'])
    refresh_g_files(fx)


def fx_symlink_input(fx):
    fx['dp_mixed.txt'] = ('symlink', 'mixed_target.txt')


ALL_PER_H = per_h_names(('G', 'D'), range(5))
FIXTURES = [
    ('F00_identity', 'byte-exact copy of the run', fx_identity, 'PASS', [], True),
    ('F01_missing_stratum_G', 'G per_H stratum "3" deleted', fx_missing_stratum_g, 'FAIL',
     ['strata_G'] + per_h_names(('G',), (3,)), True),
    ('F02_missing_stratum_D', 'D per_H stratum "3" deleted', fx_missing_stratum_d, 'FAIL',
     ['strata_D'] + per_h_names(('D',), (3,)), True),
    ('F03_empty_strata', 'per_H = {} in both summaries', fx_empty_strata, 'FAIL', ['strata_G', 'strata_D'] + ALL_PER_H,
     True),
    ('F04_header_p_G', 'G p = 7', fx_p_g, 'FAIL', ['header_G'], True),
    ('F05_header_k_D', 'D k = 5', fx_k_d, 'FAIL', ['header_D'], True),
    ('F06_header_N_G', 'G N = 17', fx_n_g, 'FAIL', ['header_G'], True),
    ('F07_formula_consistent_G', 'G H=1 classes_formula and classes_allplus_solved both -625 (self-consistent sum)',
     fx_formula_consistent_g, 'FAIL', ['G_H1_formula', 'G_H1_cover'], True),
    ('F07a_formula_only_G', 'G H=1 classes_formula -625 only', fx_formula_only_g, 'FAIL', ['G_H1_formula'], True),
    ('F07b_cover_only_G', 'G H=1 classes_allplus_solved +1 only', fx_cover_only_g, 'FAIL', ['G_H1_cover'], True),
    ('F07c_examined_shift_G', 'G H=1 classes_enumerated +625 and classes_allplus_solved -625', fx_examined_shift_g,
     'FAIL', ['G_H1_examined'], True),
    ('F08_formula_consistent_D', 'D H=2 words_formula and words_p1prime_solved both -6250 (self-consistent sum)',
     fx_formula_consistent_d, 'FAIL', ['D_H2_formula', 'D_H2_cover'], True),
    ('F09_avoider_line_dropped', 'first avoider line dropped from both avoider lists (summaries unchanged)',
     fx_avoider_dropped, 'FAIL', ['G_H1_counts', 'D_H1_counts', 'counts_files', 'mutation_structure', 'controls',
                                   'types'], True),
    ('F10_survivor_line_dropped', 'non-rigid H=2 survivor line dropped from both survivor lists (summaries unchanged)',
     fx_survivor_dropped, 'FAIL', ['survivor_set', 'G_H2_counts', 'D_H2_counts', 'counts_files'], True),
    ('F10b_survivor_dropped_consistent', 'as F10 with survivor_multisets and the G files manifest adjusted',
     fx_survivor_dropped_consistent, 'FAIL', ['survivor_set'], True),
    ('F10c_survivor_field_flipped', 'rigid flag of that survivor line flipped in both lists (G manifest adjusted)',
     fx_survivor_field_flipped, 'FAIL', ['survivor_lines'], True),
    ('F11_mutation_line_dropped', 'first mutation line dropped from both mutation lists (summaries unchanged)',
     fx_mutation_dropped, 'FAIL', ['mutation_structure', 'mutation_counts', 'counts_files'], True),
    ('F11b_mutation_lines_swapped', 'first two mutation lines swapped in both lists (G manifest adjusted)',
     fx_mutation_swapped, 'FAIL', ['lists_wellformed'], True),
    ('F11c_mutation_dropped_consistent', 'as F11 with mutation_lines, mutation_solvable and the G manifest adjusted',
     fx_mutation_dropped_consistent, 'FAIL', ['mutation_structure'], True),
    ('F12_extra_stratum_D', 'D per_H gains a stratum "5" (copy of "4")', fx_extra_stratum_d, 'FAIL', ['strata_D'], True),
    ('F13_extra_key_G', 'G per_H "2" gains an unknown field classes_skipped', fx_extra_key_g, 'FAIL', ['keysets'], True),
    ('F14_missing_input', 'dp_mixed.txt absent', fx_missing_input, 'FAIL', ['inputs_regular_files', 'no_exception'],
     False),
    ('F15_malformed_json', 'grx_summary.json truncated by 20 bytes', fx_malformed_json, 'FAIL', ['no_exception'], False),
    ('F16_count_field_G', 'G H=3 avoider_classes +1', fx_count_field_g, 'FAIL', ['G_H3_counts'], True),
    ('F17_fake_nonrigid_avoider', 'self-consistent injection of a NON-RIGID avoider class (lists, mutation lines, '
     'counts, types, controls, manifest all adjusted)', fx_fake_nonrigid_avoider, 'FAIL', ['rigid_avoiders'], True),
    ('F18_mixed_nonempty', 'dp_mixed.txt holds one class and D mixed_classes = 1', fx_mixed_nonempty, 'FAIL',
     ['mixed_empty'], True),
    ('F19_control_p1prime_D', 'D p1prime_sample_failures = 1', fx_control_p1prime_d, 'FAIL', ['controls'], True),
    ('F20_types_G', 'G avoider_types count +1', fx_types_g, 'FAIL', ['types'], True),
    ('F21_D_list_differs', 'first line of dp_mutations.txt dropped (G lists and summaries unchanged)',
     fx_d_list_differs, 'FAIL', ['lists_identical'], True),
    ('F22_files_manifest_G', 'G files manifest sha256 of grx_avoiders.txt altered', fx_files_manifest_g, 'FAIL',
     ['counts_files'], True),
    ('F23_shape_D', 'D H=2 multisets 1001 -> 1000', fx_shape_d, 'FAIL', ['D_H2_shape'], True),
    ('F25_mutation_solvable_G', 'G mutation_solvable -1', fx_mutation_solvable_g, 'FAIL', ['mutation_counts'], True),
    ('F26_bool_for_int_D', 'D mixed_classes = false (JSON boolean for an integer 0)', fx_bool_for_int_d, 'FAIL',
     ['mixed_empty'], True),
    ('F27_float_formula_G', 'G H=1 classes_formula written as a float of the right value', fx_float_formula_g, 'FAIL',
     ['G_H1_formula'], True),
    ('F28_noncanonical_avoider', 'first avoider written with a non-canonical count "00" in both lists and in its '
     'mutation lines (manifest adjusted)', fx_noncanonical_avoider, 'FAIL', ['avoider_lines'], True),
    ('F29_symlink_input', 'dp_mixed.txt is a symlink to an empty file', fx_symlink_input, 'FAIL',
     ['inputs_regular_files'], True),
]


def main():
    rundir, fixroot = sys.argv[1], sys.argv[2]
    orig = {}
    for n in INPUTS:
        with open(os.path.join(rundir, n), 'rb') as f:
            orig[n] = f.read()
    os.mkdir(fixroot)
    manifest = {'source_rundir': rundir, 'source_sha256': {n: sha(orig[n]) for n in INPUTS}, 'fixtures': []}
    for name, defect, fn, verdict, must_fail, exact in FIXTURES:
        fx = dict(orig)
        fn(fx)
        d = os.path.join(fixroot, name)
        os.mkdir(d)
        files = {}
        for n in INPUTS:
            b = fx[n]
            if b is None:
                files[n] = 'ABSENT'
            elif isinstance(b, tuple):
                with open(os.path.join(d, b[1]), 'xb') as f:
                    f.write(b'')
                os.symlink(b[1], os.path.join(d, n))
                files[n] = 'SYMLINK->' + b[1] + ' (sha256 of target %s)' % sha(b'')
            else:
                with open(os.path.join(d, n), 'xb') as f:
                    f.write(b)
                files[n] = sha(b)
        changed = sorted(n for n in INPUTS if fx[n] != orig[n])
        if name == 'F00_identity':
            assert not changed
        else:
            assert changed, name
        manifest['fixtures'].append({'name': name, 'defect': defect, 'expected_verdict': verdict,
                                     'expected_exit': 0 if verdict == 'PASS' else 1, 'must_fail': sorted(must_fail),
                                     'exact': exact, 'changed_files': changed, 'files': files})
    with open(os.path.join(fixroot, 'manifest.json'), 'x') as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
        f.write('\n')
    print('fixtures', len(manifest['fixtures']))


if __name__ == '__main__':
    main()
