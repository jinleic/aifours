#!/usr/bin/env python3
"""Stage C of PLAN-v1.md: compare Stage G (GRX) and Stage D (direct DP) outputs and evaluate the acceptance list.
Usage: compare_p5o4_v1.py OUTDIR   (reads the stage outputs in OUTDIR, writes OUTDIR/verdict.json)
"""
import sys, os, json, hashlib

def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def main():
    od = sys.argv[1]
    G = json.load(open(os.path.join(od, 'grx_summary.json')))
    D = json.load(open(os.path.join(od, 'dp_summary.json')))
    files = ['grx_summary.json', 'grx_avoiders.txt', 'grx_survivors.txt', 'grx_mutations.txt',
             'dp_summary.json', 'dp_avoiders.txt', 'dp_survivors.txt', 'dp_mutations.txt', 'dp_mixed.txt']
    hashes = {f: sha(os.path.join(od, f)) for f in files}
    av = [l.rstrip('\n') for l in open(os.path.join(od, 'grx_avoiders.txt'))]
    def has_type(H, pred):
        for l in av:
            parts = dict(s.split('=', 1) for s in l.split('|'))
            if int(parts['H']) != H:
                continue
            runs = [list(map(int, r.split(','))) for r in parts['dist'].split('/')]
            tot = [sum(r[x] for r in runs) for x in range(5)]
            if pred(tot):
                return True
        return False
    typeI = has_type(4, lambda t: sum(1 for x in t if x) == 1 and t[0] == 0)
    typeII = has_type(1, lambda t: sorted(t)[-2:] == [3, 9] and t[0] == 0)
    gc, dc = G['controls'], D['controls']
    checks = {
        'survivors_identical': hashes['grx_survivors.txt'] == hashes['dp_survivors.txt'],
        'avoiders_identical': hashes['grx_avoiders.txt'] == hashes['dp_avoiders.txt'],
        'mutations_identical': hashes['grx_mutations.txt'] == hashes['dp_mutations.txt'],
        'no_mixed_classes': os.path.getsize(os.path.join(od, 'dp_mixed.txt')) == 0 and D['mixed_classes'] == 0,
        'grx_no_nonrigid_avoider': G['total_nonrigid_avoider_classes'] == 0,
        'dp_no_nonrigid_avoider': D['total_nonrigid_avoider_classes'] == 0,
        'grx_coverage': all(v['classes_allplus_solved'] + v['classes_enumerated'] == v['classes_formula'] for v in G['per_H'].values()),
        'dp_coverage': all(v['words_p1prime_solved'] + v['words_enumerated'] == v['words_formula'] for v in D['per_H'].values()),
        'positive_avoiders_present_typeI_typeII': bool(av) and typeI and typeII,
        'positive_k2_example_both': gc['positive_k2_example_avoider'] and dc['positive_k2_example_avoider'],
        'grx_translation_invariant': gc['translation_invariant'],
        'TC1_fires_nonrigid_spurious': gc['TC1_nonrigid'] > 0,
        'TC2_fires_flips': gc['TC2_true_avoiders_flipped'] > 0,
        'TC3_fires_corrupted_law': dc['TC3_verdict_differences'] > 0,
        'TC4_fires_target8': dc['TC4_target8_solvable'] > 0,
        'TC5_mutations_nontrivial': gc['mutation_solvable'] > 0 and gc['mutation_lines'] == dc['mutation_lines'],
        'p1prime_sample_ok': dc['p1prime_sample_tested'] == 20000 and dc['p1prime_sample_failures'] == 0,
        'shift_reversal_ok': dc['shift_reversal_failures'] == 0,
    }
    verdict = 'PASS' if all(checks.values()) else 'FAIL'
    out = dict(verdict=verdict, checks=checks, hashes=hashes,
               grx_per_H=G['per_H'], dp_per_H=D['per_H'], avoider_classes=len(av))
    with open(os.path.join(od, 'verdict.json'), 'x') as f:
        json.dump(out, f, indent=1, sort_keys=True)
    print(verdict, json.dumps(checks))

if __name__ == '__main__':
    main()
