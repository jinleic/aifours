#!/usr/bin/env python3
"""f100 review driver: replay all 39 retained proofs with the reviewer's checker, run checker controls,
and build the reviewer's own classical-witness positive control for the nonmaximal species (38).
Imports only the reviewer's two scripts from this directory (never author code).
"""
import hashlib, importlib.util, itertools, json, pathlib, sys, time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8')


def load(name):
    p = HERE / name
    spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m, hashlib.sha256(p.read_bytes()).hexdigest()


rup, rup_sha = load('f100-review-rup-check-v1.py')
enc, enc_sha = load('f100-review-encoder-v1.py')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    out = HERE / 'f100-review-rup-receipt-v1.json'
    if out.exists():
        raise SystemExit('refusing to overwrite')
    man_path = ROOT / 'frontier-20261028-q1-39-species-local-proof-manifest-v1.json'
    man = json.loads(man_path.read_text())
    t0 = time.monotonic()
    cases = []
    total_add = 0
    for rec in man['records']:
        cb = (ROOT / rec['formula']).read_bytes(); pb = (ROOT / rec['proof']).read_bytes()
        t1 = time.monotonic()
        r = rup.check(cb, pb)
        r.update({'species': rec['species'], 'formula': rec['formula'], 'cnf_sha256': sha(cb), 'cnf_hash_match': sha(cb) == rec['formula_sha256'],
                  'proof': rec['proof'], 'proof_sha256': sha(pb), 'proof_hash_match': sha(pb) == rec['proof_sha256'],
                  'manifest_rup_additions': rec['rup_additions'], 'additions_match_manifest': r['additions'] == rec['rup_additions'],
                  'elapsed_seconds': time.monotonic() - t1})
        total_add += r['additions']
        cases.append(r)
        print(json.dumps({k: r[k] for k in ('species', 'verdict', 'additions', 'rup_verified', 'empty_clause_verified', 'lines_after_empty', 'deletions', 'elapsed_seconds')}), flush=True)

    controls = []
    def ctl(name, cnf, proof, expect):
        try:
            r = rup.check(cnf, proof)
            v = r['verdict']; detail = {k: r[k] for k in ('additions', 'rup_verified', 'empty_clause_verified', 'first_failure')}
        except rup.CheckError as e:
            v = 'NOT_VERIFIED'; detail = {'parse_error': str(e)}
        controls.append({'control': name, 'expected': expect, 'observed': v, 'as_expected': v == expect, 'detail': detail})
        print('CONTROL', name, 'expected', expect, 'observed', v, flush=True)

    ctl('tiny_unsat_two_units', b'p cnf 1 2\n1 0\n-1 0\n', b'0\n', 'VERIFIED')
    ctl('tiny_sat_bogus_empty', b'p cnf 1 1\n1 0\n', b'0\n', 'NOT_VERIFIED')
    four = b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n'
    ctl('four_clause_unsat_with_lemma', four, b'1 0\n0\n', 'VERIFIED')
    ctl('four_clause_unsat_bogus_empty_without_lemma', four, b'0\n', 'NOT_VERIFIED')
    ctl('sat_formula_non_rup_lemma_rejected', b'p cnf 3 1\n1 2 3 0\n', b'1 0\n0\n', 'NOT_VERIFIED')
    ctl('header_count_mismatch_rejected', b'p cnf 1 3\n1 0\n-1 0\n', b'0\n', 'NOT_VERIFIED')
    ctl('proof_literal_out_of_range_rejected', b'p cnf 1 2\n1 0\n-1 0\n', b'2 0\n0\n', 'NOT_VERIFIED')
    s0 = man['records'][0]; s1 = man['records'][1]; s38 = man['records'][38]
    c0 = (ROOT / s0['formula']).read_bytes(); p0 = (ROOT / s0['proof']).read_bytes()
    c1 = (ROOT / s1['formula']).read_bytes()
    ctl('species0_proof_against_species1_cnf', c1, p0, 'NOT_VERIFIED')
    trunc = p0[:p0.rstrip(b'\n').rfind(b'\n') + 1]   # drop final "0" line
    ctl('species0_proof_truncated_no_empty_clause', c0, trunc, 'NOT_VERIFIED')
    lines0 = p0.split(b'\n')[:-1]
    drop_last_lemma = b'\n'.join(lines0[:-2] + lines0[-1:]) + b'\n'
    ctl('species0_proof_last_lemma_removed', c0, drop_last_lemma, 'NOT_VERIFIED')
    # species 38: remove the final nonclassicality clause -> formula satisfiable (classical 4th square), proof must fail
    c38 = (ROOT / s38['formula']).read_bytes(); p38 = (ROOT / s38['proof']).read_bytes()
    l38 = c38.split(b'\n')
    hdr = l38[0].split(); nv, nc = int(hdr[2]), int(hdr[3])
    c38_noN = (b'p cnf %d %d\n' % (nv, nc - 1)) + b'\n'.join(l38[1:-2]) + b'\n'
    ctl('species38_cnf_without_nonclassicality_clause_proof_must_fail', c38_noN, p38, 'NOT_VERIFIED')
    # species 0 without the N clause (maximal triple: formula stays UNSAT, outcome informational only)
    l0 = c0.split(b'\n'); hdr0 = l0[0].split()
    c0_noN = (b'p cnf %d %d\n' % (int(hdr0[2]), int(hdr0[3]) - 1)) + b'\n'.join(l0[1:-2]) + b'\n'
    r = rup.check(c0_noN, p0)
    informational = {'species0_cnf_without_nonclassicality_clause': r['verdict'], 'note': 'maximal triple: formula without the N clause is still UNSAT (a classical Q would be a fourth MOLS), so either outcome is consistent'}
    print('INFO', informational, flush=True)

    # Reviewer's classical witness for species 38 (nonmaximal): find a fourth square orthogonal to the oriented 5-net
    triples = enc.load_triples()
    r_, c_, s_ = s38['orientation']
    clauses, numbering, stats, A, lines = enc.build(triples[38], r_, c_, s_)
    col = enc.collinear_map(lines)
    cells = sorted(set(sorted(A) + [(0, j) for j in range(8)]))
    # common transversals: 8 pairwise non-collinear cells, one per row
    rows = [[(i, j) for j in range(8)] for i in range(8)]
    transversals = []
    def rec(i, chosen):
        if i == 8:
            transversals.append(tuple(chosen)); return
        for x in rows[i]:
            if all(x not in col[y] for y in chosen):
                chosen.append(x); rec(i + 1, chosen); chosen.pop()
    rec(0, [])
    # exact cover of the 64 cells by 8 disjoint transversals (small search)
    by_cell = {}
    for ti, T in enumerate(transversals):
        for x in T:
            by_cell.setdefault(x, []).append(ti)
    cover = None
    def xc(used, chosen):
        nonlocal cover
        if cover is not None:
            return
        if len(used) == 64:
            cover = list(chosen); return
        x = min((c for c in cells if c not in used), key=lambda c: len(by_cell.get(c, [])))
        for ti in by_cell.get(x, []):
            T = transversals[ti]
            if any(y in used for y in T):
                continue
            chosen.append(ti); xc(used | set(T), chosen); chosen.pop()
    xc(frozenset(), [])
    witness = {'common_transversals': len(transversals), 'cover_found': cover is not None}
    if cover is not None:
        f = {}
        for ti in cover:
            T = transversals[ti]
            j = [x for x in T if x[0] == 0][0][1]      # transversal meets the anchor row once; label it by that column
            for x in T:
                f[x] = j
        L4 = [[f[(i, j)] for j in range(8)] for i in range(8)]
        witness['fourth_square_is_latin'] = enc.is_latin(L4)
        witness['fourth_square_bijective_on_every_line_of_all_five_classes'] = all(sorted(f[x] for x in cl) == list(range(8)) for cl in lines.values())
        witness['support_inside_allowed_set_for_all_off_anchor_cells'] = all(f[x] in A[x] for x in A)
        # evaluate the semantic clauses: P[x,t] = (f[x]==t); B[x,y,t] = P[x,t]&P[y,t]; N = False
        def truth(name):
            if name[0] == 'P':
                return f[name[1]] == name[2]
            if name[0] == 'B':
                return f[name[1]] == name[3] and f[name[2]] == name[3]
            return False
        violated = [i for i, cl in enumerate(clauses) if not any(truth(n) == (sg == 1) for n, sg in cl)]
        witness['violated_clause_indices'] = violated
        witness['only_final_nonclassicality_clause_violated'] = violated == [len(clauses) - 1]
        witness['fourth_square_rows'] = [''.join(chr(97 + v) for v in row) for row in L4]
    print('WITNESS', json.dumps(witness), flush=True)

    receipt = {'kind': 'F100_REVIEW_RUP_REPLAY_AND_CONTROLS', 'checker_sha256': rup_sha, 'encoder_sha256': enc_sha,
               'manifest_sha256': sha(man_path.read_bytes()), 'species_checked': len(cases),
               'all_verified': all(c['verdict'] == 'VERIFIED' for c in cases),
               'all_hashes_match_manifest': all(c['cnf_hash_match'] and c['proof_hash_match'] for c in cases),
               'all_addition_counts_match_manifest': all(c['additions_match_manifest'] for c in cases),
               'total_rup_additions': total_add, 'total_deletions': sum(c['deletions'] for c in cases),
               'total_lines_after_empty': sum(c['lines_after_empty'] for c in cases),
               'all_controls_as_expected': all(c['as_expected'] for c in controls),
               'controls': controls, 'informational': informational, 'species38_classical_witness': witness,
               'elapsed_seconds': time.monotonic() - t0, 'cases': cases,
               'limits': 'Local same-harness RUP replay by the reviewer; not drat-trim, not a formal kernel, not external-family review; says nothing about Hcat.'}
    with out.open('x', encoding='utf-8') as h:
        json.dump(receipt, h, indent=1); h.write('\n')
    print('ALL_VERIFIED', receipt['all_verified'], 'TOTAL_ADDITIONS', total_add, 'CONTROLS_OK', receipt['all_controls_as_expected'], 'ELAPSED', round(receipt['elapsed_seconds'], 1))


if __name__ == '__main__':
    main()
