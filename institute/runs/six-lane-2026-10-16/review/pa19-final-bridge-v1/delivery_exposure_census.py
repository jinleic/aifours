#!/usr/bin/env python3
"""Read-only metadata census for the CNF-delivery evidence question (MJ-1 / N2 of the bridge reviews).

For every M1 case, take the route and chosen record/dir from PA19FinalReceiptAudit's manifest
(review/pa19-final-receipts-v1/M1-manifest-compact.tsv, pinned by sha256 below) and classify each COUNTED record by
the positive evidence it carries that drat-trim consumed the complete CNF:
  FILE      CNF read by drat-trim from a file on disk (route a; E0 M1 check_proofs)        -> no FIFO delivery
  LRAT      rev 1-4 streamed: acceptance also required lrat-check to verify an LRAT empty-clause step that drat-trim
            emits only after processing the proof (drat-trim's early-EOF path emits no LRAT)
  REPLAY    rev 11-15 staged with drat_bytes > 65536 (feeder completion implies drat-trim read the proof, so the CNF
            section was fully parsed) -- relies on macOS pipe capacity <= 64 KiB
  NONE      rev 5 / rev 9, or rev 11-15 with drat_bytes <= 65536: no recorded positive evidence
Split coverage uses the aggregate15 rule (certified f*/batch* records, _r2 ignored) restricted to the chosen dir.
No solver, checker, generator or encoder is run; only small JSON records are read.
"""
import csv
import glob
import hashlib
import json
import os
import re
import sys
from collections import Counter

LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19'
R = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review'
MANIFEST = R + '/pa19-final-receipts-v1/M1-manifest-compact.tsv'
HERE = os.path.dirname(os.path.abspath(__file__))
PIPE = 65536


def certified(r):  # verbatim logic of aggregate15.certified
    if not r or r.get("status") != "UNSAT":
        return False
    if "lratstrict_verified" in r:
        return False
    if r.get("stream_check_revision") == 8:
        return False
    if r.get("stream_check_revision") in (11, 12, 13, 14, 15):
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified")) and \
            (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"] and r.get("replay_ok") is True and \
            r.get("reader_ok") is True and not r.get("admission_denied") and not r.get("aborted_by_sigterm")
    if r.get("stream_check_revision") == 10:
        return False
    if r.get("stream_check_revision") == 9:
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified")) and \
            (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"]
    if r.get("stream_check_revision") == 5:
        return bool(r.get("checked")) and bool(r.get("drat_trim_verified"))
    return bool(r.get("drat_trim_verified")) and bool(r.get("checked"))


def klass(r):
    rev = r.get("stream_check_revision")
    if rev is None or rev in (1, 2, 3, 4):
        return 'LRAT' if r.get('lrat_verified') else 'NONE(rev%s-no-lrat-flag)' % rev
    if rev in (11, 12, 13, 14, 15):
        return 'REPLAY' if (r.get('drat_bytes') or 0) > PIPE else 'NONE(staged-small-proof)'
    return 'NONE(rev%d)' % rev


def jl(p):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return None


def main():
    msha = hashlib.sha256(open(MANIFEST, 'rb').read()).hexdigest()
    rows = list(csv.DictReader(open(MANIFEST), delimiter='\t'))
    by_route, cases_with_none, case_detail = Counter(), Counter(), {}
    for row in rows:
        tag, route, path = row['tag'], row['route'], row['chosen_path_or_dir']
        if route == 'a':
            by_route[('a', 'FILE')] += 1
            continue
        if route in ('b', 'c5'):
            r = jl(os.path.join(LANE, path))
            k = klass(r) if r else 'MISSING'
            by_route[(route, k)] += 1
            if k.startswith('NONE'):
                cases_with_none[route] += 1
                case_detail[tag] = {'route': route, 'class': k, 'drat_bytes': r.get('drat_bytes'), 'rev': r.get('stream_check_revision')}
            continue
        if route == 'cell':
            ks = []
            for p in sorted(glob.glob(os.path.join(LANE, 'cycle2/cell-cover', tag, 'r08_c06', 's0[0-5].json'))):
                r = jl(p)
                k = klass(r)
                by_route[('cell', k)] += 1
                ks.append(k)
            if any(k.startswith('NONE') for k in ks):
                cases_with_none['cell'] += 1
                case_detail[tag] = {'route': 'cell', 'classes': ks}
            continue
        if route in ('d', 'e'):
            d = os.path.join(LANE, path)
            E = jl(os.path.join(d, 'ext.json'))
            n = E.get('num_full') if E else None
            best = {}
            for f in sorted(glob.glob(os.path.join(d, '*.json'))):
                name = os.path.basename(f)
                ms = re.fullmatch(r'f(\d+)(_exact|_r2|_r3)?\.json', name)
                mb = re.fullmatch(r'batch_\d+_\d+(_r\d+)?\.json', name)
                if not (ms or mb) or name.endswith('_r2.json'):
                    continue
                r = jl(f)
                if not certified(r):
                    continue
                idx = [int(ms.group(1))] if ms else (r.get('indices') or [])
                k = klass(r)
                rank = {'LRAT': 0, 'REPLAY': 0}.get(k, 1)
                for i in idx:
                    if i not in best or rank < best[i][0]:
                        best[i] = (rank, k)
            cnt = Counter(k for _, k in best.values())
            for k, v in cnt.items():
                by_route[(route + '-indices', k)] += v
            none_idx = sum(v for k, v in cnt.items() if k.startswith('NONE'))
            if none_idx:
                cases_with_none[route] += 1
                case_detail[tag] = {'route': route, 'num_full': n, 'indices_without_positive_evidence': none_idx,
                                    'classes': dict(cnt)}
            continue
        by_route[(route, 'UNHANDLED')] += 1
    out = {'manifest': MANIFEST, 'manifest_sha256': msha, 'pipe_capacity_assumed': PIPE,
           'counts': {'%s|%s' % k: v for k, v in sorted(by_route.items())},
           'cases_with_some_counted_index_lacking_positive_delivery_evidence': dict(cases_with_none),
           'case_detail': case_detail,
           'note': 'Best evidence per index (an index covered by both an evidence-bearing and a non-evidence record counts '
                   'as evidence-bearing). Exposure census only; not a soundness verdict.'}
    with open(os.path.join(HERE, 'delivery-exposure-census-v1.json'), 'x') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: out[k] for k in ('counts', 'cases_with_some_counted_index_lacking_positive_delivery_evidence')}, indent=1))


if __name__ == '__main__':
    sys.exit(main())
