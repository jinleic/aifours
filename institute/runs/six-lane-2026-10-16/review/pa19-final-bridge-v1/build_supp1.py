#!/usr/bin/env python3
"""Supplement 1 to the PA19FinalBridgeDesk snapshot (versioned; snapshot/ and derived/ are never modified).
Adds: the M2 ms09 b-index 3 zero-placement files (Main IRC 2026-10-18 ~01:42, structural microproof pending),
the M1 records of the mapped case ms09_s00003, parent R5 per-tag rows for ms06_s00468 / ms09_s00003 and per-tag
status counts, and the list of ms06 split directories.  Read-only on the lane; no solver/checker/generator run.
"""
import glob
import hashlib
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19'
R = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review'
OUT = os.path.join(HERE, 'snapshot-supp1')


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def main():
    os.makedirs(OUT, exist_ok=False)
    started = now()
    files = sorted(glob.glob(LANE + '/cycle2/m2part_drat/ms09_b00003/*.json')) + [
        LANE + '/cases19skel/results/ms09_s00003.json', LANE + '/cycle2/proofstream/ms09_s00003.json',
        LANE + '/cases19skel/specs/ms09_s00003.json', LANE + '/cases19skel/results/ms06_s00468.json',
        LANE + '/cases19skel/specs/ms06_s00468.json']
    man = []
    for p in files:
        data = open(p, 'rb').read()
        rel = os.path.relpath(p, LANE)
        dst = os.path.join(OUT, 'lane', rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'xb') as f:
            f.write(data)
        man.append({'snapshot_path': 'snapshot-supp1/lane/' + rel, 'source': p,
                    'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)})
    J = json.load(open(R + '/pa19-cnf-binding-v1/cnf-binding-result.json'))
    counts, rows = {}, {}
    for v in J['per_tag']:
        counts[v.get('status')] = counts.get(v.get('status'), 0) + 1
        if v.get('tag') in ('ms06_s00468', 'ms09_s00003'):
            rows[v['tag']] = v
    split_dirs = {sub: sorted(os.path.basename(d) for d in glob.glob(LANE + '/cycle2/%s/*' % sub) if os.path.isdir(d))
                  for sub in ('a3', 'part', 'm2part_drat')}
    ext_present = {sub: sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(LANE + '/cycle2/%s/*/ext.json' % sub))
                   for sub in ('a3', 'part', 'm2part_drat')}
    derived = {'recorded_start': started, 'recorded_end': now(), 'files': man,
               'r5_per_tag_status_counts': counts, 'r5_per_tag_rows': rows,
               'split_dirs': split_dirs, 'ext_json_present': ext_present,
               'note': 'm2part_drat is live; listing is time-specific.'}
    with open(os.path.join(OUT, 'supp1-derived.json'), 'x') as f:
        json.dump(derived, f, indent=1)
    print(json.dumps({'copied': len(man), 'r5_counts': counts, 'rows': sorted(rows),
                      'ms06_part_dirs': split_dirs['part'][:0] or len([d for d in split_dirs['part'] if d.startswith('ms06')]),
                      'ended': now()}))


if __name__ == '__main__':
    main()
