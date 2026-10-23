#!/usr/bin/env python3
"""Explain the stored-but-unreferenced exact duals of the Stage A runs (stdlib only; read-only).

For each universe this re-runs the frozen checker_v1 functions (profile universe, mirrored walk,
listed-signature verification, leaf witnesses) to rebuild the referenced key set, then asks
whether every unreferenced stored key is the LP key of some q of a star that the mirrored walk
encounters at a VFC checkpoint but cannot kill (some other q has no valid stored dual).
It changes no verdict; it only classifies the NOTE LP_DUAL_UNREFERENCED_STORED_KEYS.
Usage: analysis_unreferenced_v1.py --lane L --out F
"""
import argparse
import importlib.util
import itertools
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('checker_v1', os.path.join(HERE, 'checker_v1.py'))
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)


def analyse(lane, U, guard):
    d = os.path.join(lane, 'evidence', 'stageA-' + U)
    iss = chk.Issues()
    raw = {fn: chk.read_bytes(os.path.join(d, fn)) for fn in chk.RUN_FILES}
    killed_raw = chk.strict_loads(chk.utf8(chk.gunzip(raw['vfc_killed.json.gz'])))
    book = chk.DualBook(chk.strict_loads(chk.utf8(chk.gunzip(raw['lp_duals.json.gz']))), iss)
    reps, G, info = chk.profile_universe(U, iss)
    pats = [chk.Pat(p) for p in reps]
    maps = [chk.stab_maps(p, G) for p in pats]
    reps_index = {p.prof: n for n, p in enumerate(pats)}
    killed = [tuple(sorted(tuple(e) for e in s)) for s in killed_raw]
    killed_set = set(killed)
    for sig in killed:
        recs = sorted((g, a, (b2, b3, b5), ((b2, b2), (b3, b3), (b5, b5))) for (g, a, b2, b3, b5) in sig)
        ok, why, keys = chk.verify_recs(recs, book)
        if ok:
            book.referenced.update(keys)
    stats = {'children': 0, 'closed_T': 0, 'closed_VFC': 0, 'closed_Kp': 0, 'open_internal': 0,
             'leaves': 0, 'vfc_checks': 0}
    star_memo, enc, reached = {}, set(), {}
    for ri, pat in enumerate(pats):
        reached[ri] = chk.walk_rep(pat, book, killed_set, star_memo, enc, iss, guard, stats)
    lines = chk.parse_leaves(chk.utf8(chk.gunzip(raw['leaves.jsonl.gz'])), pats[0].k, len(pats[0].E), iss)
    chk.process_leaves(pats, maps, reps_index, reached, lines, book, iss, guard)
    stored = set(book.y)
    unref = stored - book.referenced
    nonkilled_keys = set()
    failure_codes = {}
    for mk, (ok, why) in star_memo.items():
        if ok:
            continue
        failure_codes[why[0]] = failure_codes.get(why[0], 0) + 1
        recs = list(mk)
        for q in itertools.product(*[range(1, r[0] - r[1] + 1) for r in recs]):
            guard.tick()
            nonkilled_keys.add(chk.lp_instance(recs, q)[0])
    explained = unref & nonkilled_keys
    return {'universe': U, 'stored_keys': len(stored), 'referenced_stored_keys': len(stored & book.referenced),
            'unreferenced_stored_keys': len(unref),
            'encountered_star_patterns_not_killed': sum(1 for r in star_memo.values() if not r[0]),
            'not_killed_failure_codes': failure_codes,
            'unreferenced_keys_that_are_q_keys_of_encountered_unkilled_stars': len(explained),
            'unreferenced_keys_unexplained': len(unref - nonkilled_keys),
            'unexplained_examples': sorted(unref - nonkilled_keys)[:20],
            'walk_counts_reproduced': {k: stats[k] for k in ('closed_T', 'closed_VFC', 'closed_Kp', 'leaves')},
            'issue_codes_seen': {c: r['count'] for c, r in iss.items.items()}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    outf = open(args.out, 'x')
    guard = chk.Guard(os.path.dirname(os.path.abspath(args.out)))
    free0 = guard.free()
    res = {'analysis': 'unreferenced stored duals v1', 'script_sha256': chk.sha256_bytes(chk.read_bytes(os.path.abspath(__file__))),
           'checker_sha256': chk.sha256_bytes(chk.read_bytes(os.path.join(HERE, 'checker_v1.py'))),
           'started_host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'admission': {'statvfs_free_bytes': free0, 'required_bytes': chk.ADMISSION_FREE, 'ok': free0 >= chk.ADMISSION_FREE}}
    code = 0
    if free0 < chk.ADMISSION_FREE:
        res['status'] = 'NOT_STARTED'
        code = 4
    else:
        try:
            res['universes'] = [analyse(args.lane, U, guard) for U in ('X1', 'MSP45', 'CORE5')]
            res['status'] = 'DONE'
        except chk.Stopped as e:
            res['status'] = 'UNKNOWN'
            res['stop_reason'] = str(e)
            code = 3
    guard.sample()
    res['resources'] = guard.report()
    json.dump(res, outf, indent=1, default=str)
    outf.write('\n')
    outf.close()
    print(json.dumps({'status': res['status'], 'summary': [
        (u['universe'], u['unreferenced_stored_keys'], u['unreferenced_keys_that_are_q_keys_of_encountered_unkilled_stars'],
         u['unreferenced_keys_unexplained']) for u in res.get('universes', [])]}))
    return code


if __name__ == '__main__':
    sys.exit(main())
