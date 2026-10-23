#!/usr/bin/env python3
"""PA19FinalBridgeDesk static snapshot builder (read-only on the lane; writes only under this directory).

Copies small load-bearing TEXT files byte-exact into snapshot/ (open mode 'xb'), records sha256/size/source path,
computes hash-only tree digests and single-file hashes for large evidence into derived/, and summarises large parent
receipts.  No solver, checker, generator, encoder or CNF construction is run.  No CNF/proof bytes are copied.
Usage: python3 -B build_snapshot.py   (cwd = this directory)
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = '/Users/jinleic/repos/aifours'
LANE = ROOT + '/information-science/evidence/six-lane-20261016/packing-array19'
RUN = ROOT + '/institute/runs/six-lane-2026-10-16'
R = RUN + '/review'
SNAP = os.path.join(HERE, 'snapshot')
DER = os.path.join(HERE, 'derived')
CAP = 10 * 1000 * 1000  # text snapshot cap (bytes), snapshot/ + derived/


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h, n = hashlib.sha256(), 0
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
            n += len(c)
    return h.hexdigest(), n


LANE_FILES = [
    'README.md', 'checkpoints.md', 'STATUS15.json', 'SHA256SUMS-cycle1.txt',
    'cycle2/m1-complete-candidate-20261018T012523.json',
    'cycle2/MANIFEST-cycle2-20261017T121839.json', 'cycle2/MANIFEST-cycle2-20261017T121839.sha256',
    'cycle2/binding-pass1.json', 'cycle2/s00468-six-unit-contract.json',
    'cycle2/s00468-retry-preparation-20261017T223835.json',
    'cycle2/cell-cover-controls-20261017T233552.json', 'cycle2/guard14-freeze-20261017T232900.json',
    'cycle2/guard15-freeze-20261018T004542.json', 'cycle2/genbg-help-flags.txt',
    'cycle2/src-delta-vs-parent-inputs-20261017T133454.txt',
    'cycle2/control13-v5.json', 'cycle2/control13-part.json', 'cycle2/control13-m2part.json', 'cycle2/control13-m2.json',
    'cycle2/smoke-stream5.json', 'cycle2/smoke-stream9.json', 'cycle2/smoke-stream11-run3.json',
    'cycle2/smoke-rev12-20261017T160454.json', 'cycle2/smoke-rev12b-20261017T162424.json',
    'cycle2/smoke-rev13-20261017T170337.json', 'cycle2/check-partial-ext-20261017T170532.json',
    'cycle2/extend-exclusive-20261017T172035.json', 'cycle2/extend-exclusive-20261017T192651.json',
    'cycle2/extend-exclusive-20261017T192946.json', 'cycle2/extend-exclusive-20261017T202335.json',
    'cycle2/extend-exclusive-20261017T235711.json', 'cycle2/exclusive2-resume-20261017T202415.json',
    'cycle2/hard-tags-ms01.txt', 'cycle2/hard-tags-ms06-ms09.txt', 'cycle2/tags-ms06-all-hard.txt',
    'cycle2/tags-ms06-m1-direct.txt', 'cycle2/tags-ms06-m1-split.txt', 'cycle2/exclusive2-m1-tags.txt',
    'cycle2/m2-jobs-easy.txt', 'cycle2/m2-jobs-part.txt', 'cycle2/m2-jobs-hard-direct.txt',
    'tools/drat-trim/drat-trim.c', 'tools/drat-trim/COMMIT.txt',
    'data/cpro1-pa-18-8-6.txt', 'data/profiles-19-8-6.json', 'data/quadgraphs-8v-13to16e-D4.g6',
    'data/quadgraphs-independent-check.json',
    'cases19skel/index.json', 'cases19q0/index.json',
]
LANE_GLOBS = [
    'src/*.py', 'src/*.c',
    'skeletons/skeletons-ms0[1-9].json', 'cycle2/skel-b/*.json',
    'cycle2/control18/*', 'cycle2/checker-smoke/*',
    'cycle2/cell-cover/ms06_s00468/r08_c06/*.json',
    'controls/verifier-mutations/*',
]
RUN_FILES = ['screening/info-1-packing-array19-contract.json']
R_FILES = [
    'pa19-cover-scout-audit-v1.md', 'pa19-encoder-scout-audit-v1.md',
    'pa19-parent-cover-replay-v1/balanced-index-pin.json', 'pa19-parent-cover-replay-v1/check_cover_bindings.py',
    'pa19-parent-cover-replay-v1/cover-binding-result.json', 'pa19-parent-cover-replay-v1/generator-replay-result.json',
    'pa19-parent-cover-replay-v1/generator-semantic-check-v1.json', 'pa19-parent-cover-replay-v1/replay_generators.py',
    'pa19-cnf-binding-v1/pins.json', 'pa19-cnf-binding-v1/bind_cnf.py',
    'pa19-placement-binding-v1/mutation-controls-v1.json', 'pa19-placement-binding-v1/placement-binding-result.json',
    'pa19-placement-binding-v1/code/r6_indep.py', 'pa19-placement-binding-v1/code/r6_replay.py',
    'pa19-placement-binding-v1/code/r6_aggregate.py', 'pa19-placement-binding-v1/code/r6_mutations.py',
    'pa19-placement-binding-v1/code/r6_pin.py',
    'pa19-ms06-placement-binding-v2/result.json', 'pa19-ms06-placement-binding-v2/spec.json',
    'pa19-subcase-binding-v1/README.md', 'pa19-subcase-binding-v1/bind_subcases.py',
    'pa19-subcase-binding-v1/incremental_bind.py', 'pa19-subcase-binding-v1/incremental/inc-001/inc-result.json',
    'pa19-strict-aggregate-schema-fix-v2.json', 'pa19_parent_aggregate_v2.py',
    'pa19-lratcheck-smoke-v1/result.json', 'pa19-lratcheck-smoke-v1/tool-hashes.txt',
    'pa19-staged10-parent-audit-v1.md', 'pa19-staged10-reviewer-v1.md', 'pa19-staged11-reviewer-v1.md',
    'pa19-staged11a-reviewer-v1.md', 'pa19-ms09-growth-parent-review-v1.json',
]
# Large parent receipts: summarised (selected keys) instead of copied.
R_SUMMARISE = {
    'pa19-cnf-binding-v1/cnf-binding-result.json': 'cnf-binding',
    'pa19-subcase-binding-v1/subcase-binding-result.json': 'subcase-binding',
    'pa19-strict-aggregate-v2/aggregate.json': 'strict-aggregate-v2',
}
# Hash-only record trees (file count, bytes, digest = sha256 of sorted 'sha256  bytes  relpath\n' lines).
TREES = ['cases19skel/results', 'cases19skel/proofcheck', 'cases19skel/specs', 'cases19q0/results', 'm2q0c/results',
         'cycle2/proofstream', 'cycle2/hard', 'cycle2/hard5', 'cycle2/a3', 'cycle2/part', 'cycle2/cell-cover',
         'cycle2/m2skel_drat', 'cycle2/m2part_drat', 'cycle2/skel-b', 'skeletons']
# Hash-only single large files and tools.
HASH_ONLY = [LANE + '/cases19skel/cnf/ms06_s00468.cnf', LANE + '/tools/drat-trim/drat-trim',
             LANE + '/tools/drat-trim/lrat-check', LANE + '/bin/verify_pa2',
             '/opt/homebrew/bin/kissat', '/opt/homebrew/bin/cadical', '/opt/homebrew/bin/geng',
             '/opt/homebrew/bin/genbg', '/opt/homebrew/bin/labelg']


def copy_one(src_abs, dst_rel, manifest):
    with open(src_abs, 'rb') as f:
        data = f.read()
    dst = os.path.join(SNAP, dst_rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'xb') as g:
        g.write(data)
    with open(dst, 'rb') as g:
        back = g.read()
    if back != data:
        raise SystemExit('copy mismatch ' + dst_rel)
    st = os.stat(src_abs)
    manifest.append({'snapshot_path': 'snapshot/' + dst_rel, 'source': src_abs, 'sha256': sha_bytes(data),
                     'bytes': len(data), 'source_mtime_ns': st.st_mtime_ns})


def tree_digest(rel):
    base = os.path.join(LANE, rel)
    lines, n, tot = [], 0, 0
    for dp, dns, fns in os.walk(base):
        dns.sort()
        for fn in sorted(fns):
            p = os.path.join(dp, fn)
            if os.path.islink(p) or not os.path.isfile(p):
                lines.append('LINK-OR-SPECIAL  0  %s\n' % os.path.relpath(p, LANE))
                continue
            h, b = sha_file(p)
            lines.append('%s  %d  %s\n' % (h, b, os.path.relpath(p, LANE)))
            n += 1
            tot += b
    lines.sort(key=lambda s: s.split('  ', 2)[2])
    return {'tree': rel, 'files': n, 'bytes': tot, 'digest_sha256': sha_bytes(''.join(lines).encode()),
            'digest_rule': "sha256 over lines '<sha256>  <bytes>  <lane-relative path>\\n' sorted by path"}


def main():
    os.makedirs(SNAP, exist_ok=False)
    os.makedirs(DER, exist_ok=False)
    started = now()
    manifest = []
    for rel in LANE_FILES:
        copy_one(os.path.join(LANE, rel), 'lane/' + rel, manifest)
    for g in LANE_GLOBS:
        for p in sorted(glob.glob(os.path.join(LANE, g))):
            if os.path.isfile(p):
                copy_one(p, 'lane/' + os.path.relpath(p, LANE), manifest)
    for rel in RUN_FILES:
        copy_one(os.path.join(RUN, rel), 'run/' + rel, manifest)
    for rel in R_FILES:
        copy_one(os.path.join(R, rel), 'review/' + rel, manifest)
    summaries = {}
    for rel, label in R_SUMMARISE.items():
        p = os.path.join(R, rel)
        h, b = sha_file(p)
        J = json.load(open(p))
        keep = {}
        for k, v in J.items():
            s = json.dumps(v)
            keep[k] = v if len(s) <= 20000 else {'omitted_bytes': len(s), 'type': type(v).__name__,
                                                   'len': len(v) if hasattr(v, '__len__') else None}
        if label == 'cnf-binding' and isinstance(J.get('per_tag'), dict):
            pt = J['per_tag']
            st = {}
            for t, v in pt.items():
                key = v.get('status') if isinstance(v, dict) else str(v)
                st[key] = st.get(key, 0) + 1
            keep['per_tag_status_counts'] = st
            keep['per_tag_ms06_s00468'] = pt.get('ms06_s00468')
        summaries[label] = {'source': p, 'sha256': h, 'bytes': b, 'summary': keep}
    with open(os.path.join(DER, 'large-parent-receipt-summaries.json'), 'x') as f:
        json.dump(summaries, f, indent=1)
    trees = [tree_digest(t) for t in TREES]
    hashes = []
    for p in HASH_ONLY:
        if os.path.isfile(p):
            real = os.path.realpath(p)
            h, b = sha_file(real)
            hashes.append({'path': p, 'realpath': real, 'sha256': h, 'bytes': b})
        else:
            hashes.append({'path': p, 'missing': True})
    with open(os.path.join(DER, 'hash-only-evidence.json'), 'x') as f:
        json.dump({'recorded_start': started, 'recorded_end': now(), 'trees': trees, 'files': hashes,
                   'note': 'Hash-only pins; contents NOT read by reviewers. M2 trees are live and may change later.'},
                  f, indent=1)
    with open(os.path.join(HERE, 'SNAPSHOT-MANIFEST.json'), 'x') as f:
        json.dump({'started': started, 'ended': now(), 'files': manifest}, f, indent=1)
    with open(os.path.join(SNAP, 'SHA256SUMS'), 'x') as f:
        for m in manifest:
            f.write('%s  %s\n' % (m['sha256'], m['snapshot_path'][len('snapshot/'):]))
    total = 0
    for dp, _, fns in os.walk(HERE):
        for fn in fns:
            if dp.startswith(SNAP) or dp.startswith(DER):
                total += os.path.getsize(os.path.join(dp, fn))
    print(json.dumps({'files_copied': len(manifest), 'snapshot_plus_derived_bytes': total, 'cap': CAP,
                      'within_cap': total <= CAP, 'started': started, 'ended': now()}))
    if total > CAP:
        sys.exit(2)


if __name__ == '__main__':
    main()
