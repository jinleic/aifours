#!/usr/bin/env python3
"""f100 review controls addendum: corrects one mis-specified expectation in f100-review-run-v1.py
(a proof with its last unit lemma removed is still a valid refutation because that lemma is redundant),
and adds guaranteed-failure proof mutations plus an explicit redundancy diagnosis.  Reviewer code only."""
import hashlib, importlib.util, json, pathlib, time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8')
spec = importlib.util.spec_from_file_location('rupchk', HERE / 'f100-review-rup-check-v1.py')
rup = importlib.util.module_from_spec(spec); spec.loader.exec_module(rup)


def main():
    out = HERE / 'f100-review-controls-addendum-receipt-v1.json'
    if out.exists():
        raise SystemExit('refusing to overwrite')
    man = json.loads((ROOT / 'frontier-20261028-q1-39-species-local-proof-manifest-v1.json').read_text())
    results = []
    def ctl(name, cnf, proof, expect, note=''):
        try:
            r = rup.check(cnf, proof); v = r['verdict']
            d = {k: r[k] for k in ('additions', 'rup_verified', 'empty_clause_verified', 'first_failure')}
        except rup.CheckError as e:
            v = 'NOT_VERIFIED'; d = {'parse_error': str(e)}
        results.append({'control': name, 'expected': expect, 'observed': v, 'as_expected': (v == expect) if expect else None, 'note': note, 'detail': d})
        print('CONTROL', name, 'expected', expect, 'observed', v, flush=True)
    for sp in (0, 12, 38):
        rec = man['records'][sp]
        c = (ROOT / rec['formula']).read_bytes(); p = (ROOT / rec['proof']).read_bytes()
        lines = p.split(b'\n')[:-1]
        # guaranteed failures
        ctl(f'species{sp}_only_empty_clause', c, b'0\n', 'NOT_VERIFIED', 'formula is not refuted by unit propagation alone')
        ctl(f'species{sp}_empty_clause_moved_first', c, b'0\n' + p, 'NOT_VERIFIED', 'empty clause before any lemma must fail at line 1')
        half = b'\n'.join(lines[len(lines) // 2:]) + b'\n'
        ctl(f'species{sp}_first_half_of_lemmas_removed', c, half, None, 'informational: not guaranteed to fail')
        nolast = b'\n'.join(lines[:-2] + lines[-1:]) + b'\n'
        ctl(f'species{sp}_last_lemma_removed', c, nolast, None, 'informational: last lemma may be redundant')
        # explicit redundancy diagnosis for the last lemma: is the empty clause RUP from formula + all lemmas except the last?
        nv, cl = rup.parse_cnf(c)
        ck = rup.Checker(nv)
        for x in cl:
            ck.add(x)
        steps = rup.parse_proof(p, nv)
        for delete, lits in steps[:-2]:
            if delete:
                ck.delete(lits)
            else:
                ck.add(lits)
        results.append({'control': f'species{sp}_empty_clause_rup_without_last_lemma', 'observed': ck.rup([]), 'note': 'True means the last non-empty lemma is redundant for the final conflict'})
        print('DIAG', results[-1], flush=True)
    receipt = {'kind': 'F100_REVIEW_CONTROLS_ADDENDUM', 'checker_sha256': hashlib.sha256((HERE / 'f100-review-rup-check-v1.py').read_bytes()).hexdigest(),
               'correction': 'f100-review-run-v1.py control species0_proof_last_lemma_removed expected NOT_VERIFIED; the observed VERIFIED is correct checker behaviour because that unit lemma is redundant (see diagnosis). all_controls_as_expected=False in the v1 receipt reflects that mis-specified expectation only.',
               'all_guaranteed_controls_as_expected': all(r['as_expected'] for r in results if r.get('as_expected') is not None),
               'results': results}
    with out.open('x', encoding='utf-8') as h:
        json.dump(receipt, h, indent=1); h.write('\n')
    print('GUARANTEED_CONTROLS_OK', receipt['all_guaranteed_controls_as_expected'])


if __name__ == '__main__':
    main()
