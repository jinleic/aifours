#!/usr/bin/env python3
"""Contiguous-coverage check of certify.py receipts (math-p0039 continuation).

Walks the class n = 8 (mod 24) from n = 8 through four consecutive segments:

  low        blocks 0..993     [8, 2*10^11)                 this lane, certify.py
  prior      main blocks 0..255 [2*10^11, 251539607552)     attack-e2 exact Python
                                                             replay; bookkeeping only
  main       blocks 256..8940  [251539607552, 2*10^12)      this lane, certify.py
  extension  blocks 0..2891    [2*10^12, 2582236504064)     this lane, certify.py

Provenance: every production receipt was computed and stamped by the archived
producer source (PRODUCER_SHA256, bytes kept in code/archive/ and verified on
every run).  The current code/certify.py is the guarded verifier
(VERIFIER_SHA256); receipts it writes carry its own hash plus the hash of the
shared receipt_checks.py (HELPER_SHA256).  The shipped verifier and helper are
verified too.  A receipt with any other stamp is rejected.

Block rows and survivor witnesses are checked by the shared receipt_checks.py,
the same rules certify.py replay applies.  This program checks strict integer
types and canonical values,
recomputes each block's geometry from the task constants, checks bookkeeping
identities, the documented libmpdec sampling policy and subset size, the absence
of unresolved survivors, re-verifies every survivor resolution witness exactly
(integer factors; collision pairs in canonical representatives 1..p-1 with a
nonzero difference), and for main/extension requires each block digest to
equal BOTH preserved C digests.  For the prior segment it only checks the
archived replay records (pinned file hashes, exit codes, block lists, digests
equal to both C logs).  It reports the maximal gap-free prefix from n = 8.
No block is recomputed here; `certify.py replay` does that.
"""
import argparse
import gzip
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

# Strict row and witness rules shared with certify.py replay (no sieve/residue arithmetic inside).
from receipt_checks import CheckFailed, canonical, check_block_row, is_int, need

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = HERE.parents[3]
# attack-e2 snapshot (C logs + prior replay records); a handoff bundle carries a pinned copy in inputs/.
ATTACK = BASE / 'inputs' if (BASE / 'inputs').is_dir() else \
    ROOT / 'institute/runs/hard-2026-10-15/problems/math-p0039/attack-e2'
SCHEMA = 'math-p0039-cert-receipt/2'
PRODUCER_SHA256 = 'f6eaa1a80c4112d7af3caa54901f5451a88f9527bb9f23c4be54e89b897941a6'
PRODUCER_SOURCE = HERE / 'archive' / 'certify-f6eaa1a8.py'
VERIFIER_SHA256 = 'd66fdcf0a9c46c9c25dd1f00fe18b651bb3ad9302a1f6c839bcf651c5fabaef6'
HELPER_SHA256 = '85e43af3931bf1215b29d3278f7217d87b72708a338fce226d09f60e3b11b419'
HELPER_SOURCE = HERE / 'receipt_checks.py'
TASKS = {
    'low': (8, 200000000000, 24, 8388608),
    'main': (200000000000, 2000000000000, 24, 8388608),
    'extension': (2000000000000, 4000000000000, 24, 8388608),
}
STRIDE = {'low': 1, 'main': 32, 'extension': 32}
LOG_SHA256 = {
    'e2-main-scan32.blocks.jsonl': '74e8a84b5bb34f26f00600ceb9570c942e922f92382a99d9de9981e4d1b0b036',
    'e2-main-scan128_digest.blocks.jsonl': 'ffae5842bae87f84eb35006c1a86e659b2e2888f8ac952980bf92c1217b12b0d',
    'e2-extension-scan32.blocks.jsonl': '3b54ff6b9a2e3d4bf2e7ca9f285cbac81f8b91160bd6c628a75e4f8cb2a858fd',
    'e2-extension-scan128_digest.blocks.jsonl': '0e61292cc48886e1ea35a5f47d528d583b006e552561600a2f98415b84156acf',
}
PRIOR_GROUP_SHA256 = {  # attack-e2/evidence/epoch2/prefix-groups/NN-run.json
    '00': '4a1d4d6425883826ddcf6eff1702f0dd5f48f407afe54c971356db2d1fd9fb00',
    '01': '39436803ddb68ae7358481f10104130282b1b3e9dce6ee5bff2bf2975ec1e709',
    '02': '04c7b0c6707d5d758380fd66bd1775f00515157771b922e2d495d324ae42bb4e',
    '03': '8fbf6200a82e0ca61217f7934c2d0452c497eaa146469ac7f87458c75e44eb5f',
    '04': '86a3f0b2ac9532441afea488246c3de51f37312157fdae5bf17e181e328b4c1c',
    '05': '1bcf31064cc457e942af00a867717e2497ce042bb3e9b18797c1ed4b525af1df',
    '06': '56ed9b3808124e2e8caf3dcd4f4ca58c13bad24a740f1dcd175ab7aefc550711',
    '07': '10007d2ce73ee0d68a8248d0f0319531bdb2227e117af67df615b08ced1abc0a',
}
SEGMENTS = [('low', 'low', 0, 993), ('prior', 'main', 0, 255),
            ('main', 'main', 256, 8940), ('extension', 'extension', 0, 2891)]
PRIOR_END = 251539607552
PAIRED_C_END = 2582236504064


def geometry(task, bid):
    start, stop, step, size = TASKS[task]
    total = (stop - start + step - 1) // step
    need(is_int(bid) and 0 <= bid < (total + size - 1) // size, 'block id outside task')
    count = min(size, total - bid * size)
    first = start + step * bid * size
    return first, first + step * count, count


def load_receipts(root):
    root = Path(root)
    out = []
    for path in sorted(root.glob('*/*.json')):
        out.append((str(path), json.loads(path.read_text())))
    for path in sorted(root.glob('*.jsonl.gz')):
        with gzip.open(path, 'rt') as f:
            for k, line in enumerate(f):
                out.append(('%s:%d' % (path, k + 1), json.loads(line)))
    return out


def load_logs(logs):
    digests = {}
    for task in ('main', 'extension'):
        per = []
        for exe in ('scan32', 'scan128_digest'):
            name = 'e2-%s-%s.blocks.jsonl' % (task, exe)
            data = (Path(logs) / name).read_bytes()
            need(hashlib.sha256(data).hexdigest() == LOG_SHA256[name], 'pinned C log hash differs: ' + name)
            rows = [json.loads(x) for x in data.decode().splitlines() if x.strip()]
            need(rows[0]['kind'] == 'header' and (rows[0]['start'], rows[0]['stop'], rows[0]['step'],
                 rows[0]['block_size']) == TASKS[task], 'C log scope ' + name)
            per.append({r['id']: r for r in rows[1:] if r['kind'] == 'block'})
        digests[task] = per
    return digests


def prior_segment(attack, logs):
    """Bookkeeping of the attack-e2 exact replay of main blocks 0..255."""
    rows = {}
    for g, pin in PRIOR_GROUP_SHA256.items():
        path = Path(attack) / 'evidence/epoch2/prefix-groups' / (g + '-run.json')
        data = path.read_bytes()
        need(hashlib.sha256(data).hexdigest() == pin, 'prior replay record hash differs: ' + g)
        run = json.loads(data)
        out = json.loads(run['stdout'])
        ids = list(range(32 * int(g), 32 * int(g) + 32))
        need(run['returncode'] == 0 and out['task'] == 'main' and out['base_two_survivors'] == []
             and [b['block'] for b in out['blocks']] == ids
             and out['fully_recomputed_members'] == 32 * 8388608, 'prior replay record ' + g)
        for b in out['blocks']:
            start, end, count = geometry('main', b['block'])
            need((b['start'], b['end'], b['count']) == (start, end, count), 'prior geometry')
            for c in logs['main']:
                need(c[b['block']]['decision_sha256'] == b['sha256'], 'prior digest differs from C')
            rows[b['block']] = b
    return rows


def check_receipt(where, r):
    """Strict shape, type and parameter check of one receipt (its blocks follow)."""
    need(isinstance(r, dict) and r.get('schema') == SCHEMA, 'schema: ' + where)
    need(r.get('checker_sha256') in (PRODUCER_SHA256, VERIFIER_SHA256),
         'receipt from another checker (neither the archived producer nor the current verifier): ' + where)
    if r['checker_sha256'] == VERIFIER_SHA256:
        need(r.get('helper_sha256') == HELPER_SHA256, 'receipt written with another receipt_checks.py: ' + where)
    else:
        need('helper_sha256' not in r, 'producer receipt carries a helper stamp: ' + where)
    task = r.get('task')
    need(task in TASKS, 'task: ' + where)
    pins = {k: v for k, v in LOG_SHA256.items() if k.startswith('e2-%s-' % task)}
    need(r.get('c_logs') == pins, 'C log pins in receipt: ' + where)
    need(is_int(r.get('sieve_bound')) and r['sieve_bound'] == 1000000
         and is_int(r.get('mpdec_stride')) and r['mpdec_stride'] == STRIDE[task], 'parameters: ' + where)
    scope = r.get('task_scope')
    need(isinstance(scope, dict) and all(is_int(v) for v in scope.values())
         and scope == dict(zip(('start', 'stop', 'step', 'block_size'), TASKS[task])), 'scope: ' + where)
    need(is_int(r.get('first')) and is_int(r.get('last')) and isinstance(r.get('blocks'), list)
         and len(r['blocks']) == r['last'] - r['first'] + 1 >= 1, 'receipt block list is not first..last: ' + where)
    need(is_int(r.get('selftest', {}).get('primes')) and r['selftest']['primes'] == 78498, 'selftest: ' + where)
    need(r.get('environment', {}).get('libmpdec'), 'libmpdec not recorded: ' + where)
    need(is_int(r.get('max_rss_bytes')) and isinstance(r.get('seconds'), (int, float)), 'resource fields: ' + where)
    return task


def check(receipts, logs, prior, current_checker, producer_source, helper_source):
    need(current_checker == VERIFIER_SHA256, 'shipped certify.py differs from the pinned verifier')
    need(producer_source == PRODUCER_SHA256, 'archived producer source differs from its pin')
    need(helper_source == HELPER_SHA256, 'shipped receipt_checks.py differs from its pin')
    blocks = {}
    totals = dict(receipts=0, seconds=0.0, max_rss_bytes=0)
    stamps = Counter()
    resolutions = []
    for where, r in receipts:
        task = check_receipt(where, r)
        stamps[r['checker_sha256']] += 1
        stride = r['mpdec_stride']
        for k, b in enumerate(r['blocks']):
            bid = r['first'] + k
            start, end, count = geometry(task, bid)
            tag = '%s block %d' % (where, bid)
            resolutions.extend(check_block_row(b, bid, (start, end, count), 24, stride, task == 'low', tag))
            if task != 'low':
                for c in logs[task]:
                    e = c.get(bid)
                    need(e is not None and e['decision_sha256'] == b['sha256']
                         and (e['sieved'], e['tested'], e['survivors']) == (b['sieved'], b['tested'], []),
                         'digest differs from a C log: ' + tag)
            key = (task, bid)
            row = {k2: v for k2, v in b.items() if k2 != 'seconds'}
            if key in blocks:
                need(canonical(blocks[key]) == canonical(row), 'conflicting duplicate block %s %d' % key)
            blocks[key] = row
        totals['receipts'] += 1
        totals['seconds'] += r['seconds']
        totals['max_rss_bytes'] = max(totals['max_rss_bytes'], r['max_rss_bytes'])
    # Walk the four segments from n = 8 and stop at the first missing block.
    cursor, gap, seg_out, walked = 8, None, [], set()
    for name, task, first, last in SEGMENTS:
        seg = dict(segment=name, task=task, blocks=0, members=0, sieved=0, tested=0, libmpdec=0,
                   start=geometry(task, first)[0])
        for bid in range(first, last + 1):
            start, end, count = geometry(task, bid)
            need(start == cursor, 'segments are not contiguous in n at %s %d' % (task, bid))
            row = prior.get(bid) if name == 'prior' else blocks.get((task, bid))
            if row is None:
                gap = dict(segment=name, task=task, block=bid, n=start)
                break
            cursor = end
            seg['blocks'] += 1
            seg['members'] += count
            if name != 'prior':
                walked.add((task, bid))
                seg['sieved'] += row['sieved']; seg['tested'] += row['tested']; seg['libmpdec'] += row['mpdec_residues']
        seg['end'] = cursor
        seg['complete'] = gap is None
        seg_out.append(seg)
        if gap:
            break
    need(sum(s['members'] for s in seg_out) == (cursor - 8) // 24, 'member count differs from the interval')
    beyond = sorted(k for k in blocks if k not in walked)
    low = next(s for s in seg_out if s['segment'] == 'low')
    return dict(
        gap_free_bound=cursor,
        statement=('Every n = 8 (mod 24) with 8 < n < %d has an exact elimination '
                   '(proper factor, base-two failure, or explicit difference collision) in the walked segments.' % cursor),
        replayed_from_scratch_interval=[8, low['end']],
        prior_exact_interval=[200000000000, PRIOR_END],
        extension_interval=[PRIOR_END, cursor] if cursor > PRIOR_END else None,
        paired_c_range_complete=cursor == PAIRED_C_END and gap is None,
        first_missing=gap, segments=seg_out, resolutions=resolutions,
        receipt_blocks_outside_walk=['%s:%d' % k for k in beyond],
        receipts=totals['receipts'], receipt_seconds_total=round(totals['seconds'], 3),
        max_rss_bytes=totals['max_rss_bytes'],
        provenance=dict(producer_sha256=PRODUCER_SHA256, producer_source_bytes_verified=True,
                        verifier_sha256=VERIFIER_SHA256, shipped_verifier_verified=True,
                        helper_sha256=HELPER_SHA256, shipped_helper_verified=True,
                        receipts_by_checker=dict(stamps)),
        premises=('Kantor 1987 (uses CFSG); Thas-Zagier 2008 reduction to D = mu_(n+1) in F_p with p = n^2+n+1 '
                  'prime and PG(2,2), PG(2,8) as the only special-and-Desarguesian cases; 8 | n (Feit 1990 Lemma 2.2); '
                  'Feit divisor condition d^(n+1) = 1 (mod p), giving n = 2 (mod 3).'),
        limitation=('Receipt and coverage check only; blocks are re-executable with certify.py replay. '
                    'The prior segment is accepted from attack-e2 and is not recomputed here.'))


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--receipts', default=str(BASE / 'receipts'))
    p.add_argument('--attack', default=str(ATTACK), help='attack-e2 snapshot (C logs, prior replay records)')
    p.add_argument('--checker', default=str(HERE / 'certify.py'),
                   help='shipped guarded verifier; its hash must equal VERIFIER_SHA256')
    p.add_argument('--producer-source', default=str(PRODUCER_SOURCE),
                   help='archived producer source; its bytes must hash to PRODUCER_SHA256')
    p.add_argument('--require-through', type=int, help='fail unless the gap-free bound reaches this n')
    p.add_argument('--output')
    args = p.parse_args()
    sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    logs = load_logs(Path(args.attack) / 'logs')
    result = check(load_receipts(args.receipts), logs, prior_segment(args.attack, logs),
                   sha(args.checker), sha(args.producer_source), sha(HELPER_SOURCE))
    if args.require_through is not None:
        need(result['gap_free_bound'] >= args.require_through,
             'gap-free prefix ends at %d before %d (first missing %s)'
             % (result['gap_free_bound'], args.require_through, result['first_missing']))
    text = json.dumps(result, indent=1)
    if args.output:
        Path(args.output).write_text(text + '\n')
    print(text)


if __name__ == '__main__':
    try:
        main()
    except CheckFailed as e:
        print('CHECK FAILED: ' + str(e), file=sys.stderr)
        sys.exit(1)
    except (KeyError, TypeError, AttributeError, ValueError, IndexError) as e:
        print('CHECK FAILED: malformed receipt or input (%s: %s)' % (type(e).__name__, e), file=sys.stderr)
        sys.exit(1)
