#!/usr/bin/env python3
"""ADDENDUM-v1 evidence for the parent replay of C5' (parent-desk MINORs m1-m7 of the Claude hostile review
olson-p5o4-complete-claim-claude-v1, note sha 7816550f...6a5f).  Read-only on every existing desk file; creates
DESK/out/addendum-v1/evidence/ exclusively and writes evidence.json and avoider_classes_oF.txt there with mode 'x'.
  (1) the four published deliverables against their reported SHA-256, and every file pinned by RESULT-v1.json and
      RESULT-primary-v1.json re-hashed (sha256 and size);
  (2) route-1 files and runs: current hash vs both RESULT pins, file mtimes and run start/end (from the run logs)
      relative to the external SIGTERM at 2026-10-18 09:25:51 PDT, binary/script attribution from the logged commands;
  (3) m5 pins of enum-clean-v2 (and of its v1 twin and of the fresh rerun) with fail-closed emptiness checks;
  (4) byte comparison of the fresh rerun enum-clean-v2-rerun-a1 with enum-clean-v2, masking only "elapsed_s";
  (5) maximal o_F of every avoider class, computed from the literal words of ALL its l-tuples (maximal cyclic runs of
      equal letters) and from the block structure; the two must agree and be constant over the l-tuples;
  (6) provenance facts parsed from out/addendum-v1/provenance and out/addendum-v1/rebuild, and an automated check that
      every line changed between the v1 and v2 C++ sources is a comment, inside run_brute, or the brute dispatcher.
Usage: python3 -B addendum_evidence_v1.py DESK
"""
import datetime
import difflib
import glob
import hashlib
import json
import os
import re
import sys

EMPTY = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
DELIVERABLES = {'RESULT-v1.json': 'd823a969064fbf473ea9ab8288b487dbd75c3b68608e857fb3ae6aa7e9efddf1',
                'NOTE-v1.md': '1c3ae5faab8df3518cd578c98ed5a287766b80016e4c9987783058bb13a555ec',
                'RESULT-primary-v1.json': '7dfe21eb72ca4f474ffd7730284ca6c9ae7e7d5ab251a052fc336a5845d3b911',
                'NOTE-primary-v1.md': '844575b692cd170b71c3c10bf20a74c04e8ab21834130757d31df3a1efd8234f'}
REVIEW = ('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/'
          'olson-p5o4-complete-claim-claude-v1.note.md',
          '7816550f746a00ee330cd83a3613d9103f6d423e1820664985d5f9d0dd006a5f')
SIGTERM = datetime.datetime(2026, 10, 18, 9, 25, 51).astimezone()
ROUTE1_RUNS = ['controls-v2', 'enum-clean-v2', 'enum-bug-untwisted-v2', 'enum-bug-target8-v2', 'enum-bug-parity-v2',
               'check-all-avoiders-v2', 'indep-check-v1', 'compare-primary-v1']
V1_TWIN_RUNS = ['controls-v1', 'enum-clean-v1']
ROUTE1_CODE = ['src/olson_p5o4_replay_v2.cpp', 'bin/replay_v2', 'src/indep_check_v1.py', 'src/compare_primary_v1.py',
               'src/make_result_primary_v1.py', 'src/olson_p5o4_replay_v1.cpp', 'bin/replay_v1']
LIST_FILES = ['avoider_classes.txt', 'mixed_classes.txt', 'nonrigid_avoider_classes.txt', 'survivor_multisets.txt']
P = 5


def sha(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def load(path):
    with open(path) as fh:
        return json.load(fh)


def mtime(path):
    return datetime.datetime.fromtimestamp(os.stat(path).st_mtime).astimezone()


def btime(path):
    return datetime.datetime.fromtimestamp(os.stat(path).st_birthtime).astimezone()


def iso(t):
    return t.isoformat(timespec='seconds')


def parse_date_line(ln):
    return datetime.datetime.strptime(ln.replace('PDT ', ''), '%a %b %d %H:%M:%S %Y').astimezone()


def run_log(path):
    txt = open(path).read()
    dates = [ln for ln in txt.splitlines()
             if re.match(r'^[A-Z][a-z]{2} [A-Z][a-z]{2} +\d+ \d\d:\d\d:\d\d PDT \d{4}$', ln)]
    cmd = re.search(r'^cmd: (.*)$', txt, re.M)
    ex = re.findall(r'^exit=(\d+)$', txt, re.M)
    real = re.search(r'([\d.]+) real', txt)
    rss = re.search(r'(\d+)\s+maximum resident set size', txt)
    start = parse_date_line(dates[0]) if dates else None
    end = parse_date_line(dates[-1]) if len(dates) > 1 else None
    return dict(log=os.path.basename(path), cmd=cmd.group(1) if cmd else None, start=iso(start) if start else None,
                end=iso(end) if end else None, exit=int(ex[-1]) if ex else None,
                wall_s=float(real.group(1)) if real else None, maxrss_bytes=int(rss.group(1)) if rss else None,
                end_seconds_before_sigterm=(SIGTERM - end).total_seconds() if end else None)


def mask(text, keys):
    for k in keys:
        text = re.sub(r'("%s": )[-0-9.eE]+' % re.escape(k), r'\1<MASKED>', text)
    return text


def json_diff(a, b, path=''):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append(path + '/' + k)
            else:
                out += json_diff(a[k], b[k], path + '/' + k)
        return out
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += json_diff(x, y, '%s[%d]' % (path, i))
        return out
    return [] if a == b else [path]


def ltuples(H):
    return [(a1, a2, a3, H - a1 - a2 - a3) for a1 in range(H + 1) for a2 in range(H + 1 - a1)
            for a3 in range(H + 1 - a1 - a2)]


def parse_class(ln):
    f = dict(kv.split('=', 1) for kv in ln.split('|'))
    runs = [[] if r == '-' else [int(ch) for ch in r] for r in f['runs'].split('/')]
    return int(f['H']), runs, [int(ch) for ch in f['y']]


def word(runs, ls, ys):
    w = []
    for i in range(4):
        w += [('r', x) for x in sorted(runs[i])]
        w += [('s', ys[i])] * ls[i]
    return w


def maximal_oF(w):
    """Odd maximal cyclic constant reflection blocks of the cyclic word w (maximal cyclic runs of equal letters)."""
    n = len(w)
    if all(c == w[0] for c in w):
        return 1 if (w[0][0] == 's' and n % 2 == 1) else 0
    k = next(i for i in range(n) if w[i] != w[i - 1])
    v = w[k:] + w[:k]
    odd, i = 0, 0
    while i < n:
        j = i
        while j < n and v[j] == v[i]:
            j += 1
        if v[i][0] == 's' and (j - i) % 2 == 1:
            odd += 1
        i = j
    return odd


def oF_struct(runs, ys):
    """Same quantity from the block structure: odd blocks S_i, S_(i+1) merge iff R_(i+1) is empty and y_i = y_(i+1)."""
    links = [len(runs[(i + 1) % 4]) == 0 and ys[i] == ys[(i + 1) % 4] for i in range(4)]
    if all(links):
        return 0
    start = next(i for i in range(4) if not links[(i - 1) % 4])
    groups, size = [], 0
    for t in range(4):
        i = (start + t) % 4
        size += 1
        if not links[i]:
            groups.append(size)
            size = 0
    return sum(1 for g in groups if g % 2 == 1)


def main():
    desk = sys.argv[1]
    out = os.path.join(desk, 'out')
    edir = os.path.join(out, 'addendum-v1', 'evidence')
    os.mkdir(edir)
    ev, fails = {'script': 'addendum_evidence_v1.py',
                 'written_host_clock': iso(datetime.datetime.now().astimezone()),
                 'sigterm_event': iso(SIGTERM)}, []

    # ---- (1) deliverables and re-hash of every pinned file
    dl = {}
    for rel, exp in DELIVERABLES.items():
        s = sha(os.path.join(desk, rel))
        dl[rel] = dict(sha256=s, reported=exp, ok=s == exp)
    rv = sha(REVIEW[0])
    dl['review_note'] = dict(path=REVIEW[0], sha256=rv, reported=REVIEW[1], ok=rv == REVIEW[1])
    r1, rp = load(os.path.join(desk, 'RESULT-v1.json')), load(os.path.join(desk, 'RESULT-primary-v1.json'))
    dl['RESULT-v1_pins_NOTE-v1'] = r1['note']['sha256'] == DELIVERABLES['NOTE-v1.md']
    dl['RESULT-primary-v1_pins_NOTE-primary-v1'] = rp['note']['sha256'] == DELIVERABLES['NOTE-primary-v1.md']
    dl['RESULT-v1_pins_primary_pair'] = (
        r1['primary_deliverable']['result']['sha256'] == DELIVERABLES['RESULT-primary-v1.json']
        and r1['primary_deliverable']['note']['sha256'] == DELIVERABLES['NOTE-primary-v1.md'])
    ev['deliverables'] = dl
    if not all(v['ok'] if isinstance(v, dict) else v for v in dl.values()):
        fails.append('deliverable hash')
    rehash = {}
    for name, pins in (('RESULT-v1.json', r1['files_sha256']), ('RESULT-primary-v1.json', rp['files_sha256'])):
        bad, missing = [], []
        for rel, d in sorted(pins.items()):
            p = os.path.join(desk, rel)
            if not os.path.exists(p):
                missing.append(rel)
            elif sha(p) != d['sha256'] or os.path.getsize(p) != d['bytes']:
                bad.append(rel)
        rehash[name] = dict(pinned_files=len(pins), matching=len(pins) - len(bad) - len(missing), mismatching=bad,
                            missing=missing)
        if bad or missing:
            fails.append('re-hash vs %s' % name)
    ev['rehash_all_pinned_files'] = rehash

    # ---- (2) route-1 files and run timeline
    info = {r: run_log(os.path.join(out, r + '.log')) for r in ROUTE1_RUNS + V1_TWIN_RUNS}
    tol = datetime.timedelta(seconds=1)
    result_primary_birth = btime(os.path.join(desk, 'RESULT-primary-v1.json'))
    first_use = {'src/olson_p5o4_replay_v2.cpp': 'controls-v2', 'bin/replay_v2': 'controls-v2',
                 'src/indep_check_v1.py': 'indep-check-v1', 'src/compare_primary_v1.py': 'compare-primary-v1',
                 'src/olson_p5o4_replay_v1.cpp': 'controls-v1', 'bin/replay_v1': 'controls-v1'}
    files = []
    for run in ROUTE1_RUNS + V1_TWIN_RUNS:
        for p in sorted(glob.glob(os.path.join(out, run, '*'))) + [os.path.join(out, run + '.log')]:
            files.append((os.path.relpath(p, desk), run))
    files += [(rel, None) for rel in ROUTE1_CODE]
    rows = []
    for rel, run in files:
        p = os.path.join(desk, rel)
        s, t, tb = sha(p), mtime(p), btime(p)
        a = r1['files_sha256'].get(rel, {}).get('sha256')
        b = rp['files_sha256'].get(rel, {}).get('sha256')
        row = dict(file=rel, sha256=s, bytes=os.path.getsize(p), pinned_RESULT_v1=a == s if a else None,
                   pinned_RESULT_primary_v1=b == s if b else None, birth=iso(tb), mtime=iso(t),
                   mtime_before_sigterm=t < SIGTERM)
        if run is not None:
            st, en = (datetime.datetime.fromisoformat(info[run][k]) for k in ('start', 'end'))
            row['producing_run'] = run
            row['written_within_run_window'] = tb >= st - tol and t <= en + tol
        else:
            use = (datetime.datetime.fromisoformat(info[first_use[rel]]['start']) if rel in first_use
                   else result_primary_birth)
            row['first_use'] = first_use.get(rel, 'make_result_primary_v1 (RESULT-primary-v1.json birth)')
            row['last_written_before_first_use'] = t <= use
        rows.append(row)
    ev['route1_files'] = rows
    ev['route1_files_summary'] = dict(
        files=len(rows), all_pinned_in_RESULT_v1_and_matching=all(r['pinned_RESULT_v1'] is True for r in rows),
        all_pinned_in_RESULT_primary_v1_and_matching=all(r['pinned_RESULT_primary_v1'] is True for r in rows),
        all_run_files_written_within_their_run_window=all(r.get('written_within_run_window', True) for r in rows),
        all_code_files_last_written_before_first_use=all(r.get('last_written_before_first_use', True) for r in rows),
        written_after_sigterm=[r['file'] for r in rows if not r['mtime_before_sigterm']])
    if not all(v for k, v in ev['route1_files_summary'].items() if k.startswith('all_')):
        fails.append('route-1 file pins/times')
    runs = [dict(run=r, role='route 1 (verdict)', **info[r]) for r in ROUTE1_RUNS]
    runs += [dict(run=r, role='v1 twin (byte-identity cross-check only)', **info[r]) for r in V1_TWIN_RUNS]
    runs.append(dict(run='enum-clean-v2-rerun-a1', role='ADDENDUM fresh rerun (review m6)',
                     **run_log(os.path.join(out, 'enum-clean-v2-rerun-a1.log'))))
    ev['runs'] = runs
    native = [r for r in runs if r['run'] in ROUTE1_RUNS and r['run'] != 'compare-primary-v1']
    ev['route1_native_runs_all_ended_before_sigterm'] = all(r['end_seconds_before_sigterm'] > 0 for r in native)
    ev['route1_native_runs_latest_end'] = max(r['end'] for r in native)
    ev['route1_runs_exit0'] = all(r['exit'] == 0 for r in runs if r['run'] in ROUTE1_RUNS)
    if not (ev['route1_native_runs_all_ended_before_sigterm'] and ev['route1_runs_exit0']):
        fails.append('route-1 timeline/exit')

    # ---- (3) m5 pins with fail-closed checks
    pins = {}
    for run in ('enum-clean-v2', 'enum-clean-v1', 'enum-clean-v2-rerun-a1'):
        d = os.path.join(out, run)
        fs = {f: dict(sha256=sha(os.path.join(d, f)), bytes=os.path.getsize(os.path.join(d, f)))
              for f in LIST_FILES + ['summary.json']}
        sm = load(os.path.join(d, 'summary.json'))
        chk = dict(mixed_is_empty_file=fs['mixed_classes.txt']['sha256'] == EMPTY,
                   nonrigid_is_empty_file=fs['nonrigid_avoider_classes.txt']['sha256'] == EMPTY,
                   summary_all_checks_ok=sm['all_checks_ok'] is True, summary_bug_none=sm['bug'] == 'none',
                   summary_mixed_0=sm['totals']['mixed_classes'] == 0 and all(h['classes_mixed'] == 0 for h in sm['per_H']),
                   summary_nonrigid_0=sm['totals']['nonrigid_avoider_words'] == 0
                   and all(h['nonrigid_avoider_classes'] == 0 and h['nonrigid_avoider_words'] == 0 for h in sm['per_H']),
                   strata_0_7=[h['H'] for h in sm['per_H']] == list(range(8)),
                   avoider_lines_640=sum(1 for _ in open(os.path.join(d, 'avoider_classes.txt'))) == 640)
        pins[run] = dict(files=fs, checks=chk, all_ok=all(chk.values()))
        if not pins[run]['all_ok']:
            fails.append('m5 checks %s' % run)
    ev['m5_pins'] = pins

    # ---- (4) fresh rerun vs original, byte for byte, masking only "elapsed_s"
    a_dir, b_dir, v1_dir = (os.path.join(out, x) for x in ('enum-clean-v2', 'enum-clean-v2-rerun-a1', 'enum-clean-v1'))
    cmpf = {}
    for f in LIST_FILES:
        ba, bb, bv = (open(os.path.join(x, f), 'rb').read() for x in (a_dir, b_dir, v1_dir))
        cmpf[f] = dict(rerun_equals_original=ba == bb, rerun_equals_v1_twin=bb == bv)
    sa, sb, sv = (open(os.path.join(x, 'summary.json')).read() for x in (a_dir, b_dir, v1_dir))
    cmpf['summary.json'] = dict(
        raw_bytes_equal=sa == sb,
        equal_with_only_elapsed_s_masked=mask(sa, ['elapsed_s']) == mask(sb, ['elapsed_s']),
        json_paths_differing=json_diff(json.loads(sa), json.loads(sb)),
        original_elapsed_s=json.loads(sa)['elapsed_s'], rerun_elapsed_s=json.loads(sb)['elapsed_s'],
        original_maxrss_bytes=json.loads(sa)['maxrss_bytes'], rerun_maxrss_bytes=json.loads(sb)['maxrss_bytes'],
        v1_twin_json_paths_differing=json_diff(json.loads(sv), json.loads(sb)))
    rl = open(os.path.join(out, 'enum-clean-v2-rerun-a1.log')).read()
    hashes = re.findall(r'^([0-9a-f]{64})  bin/replay_v2$', rl, re.M)
    ev['rerun'] = dict(dir='out/enum-clean-v2-rerun-a1', log='out/enum-clean-v2-rerun-a1.log',
                       binary_hash_pre_post=hashes, binary_is_frozen=hashes == [sha(os.path.join(desk, 'bin/replay_v2'))] * 2,
                       comparison=cmpf)
    rr_ok = (all(cmpf[f]['rerun_equals_original'] for f in LIST_FILES)
             and cmpf['summary.json']['equal_with_only_elapsed_s_masked']
             and cmpf['summary.json']['json_paths_differing'] == ['/elapsed_s'] and ev['rerun']['binary_is_frozen'])
    ev['rerun']['identical_except_elapsed_s'] = rr_ok
    if not rr_ok:
        fails.append('rerun comparison')

    # ---- (5) maximal o_F of every avoider class
    lines = [ln.rstrip('\n') for ln in open(os.path.join(a_dir, 'avoider_classes.txt')) if ln.strip()]
    by_oF, by_H_oF, reps_by_oF, nonempty_all, bad = {}, {}, {}, 0, []
    of_lines = []
    for ln in lines:
        H, runs_, ys = parse_class(ln)
        vals = {maximal_oF(word(runs_, [2 * t + 1 for t in a], ys)) for a in ltuples(H)}
        st = oF_struct(runs_, ys)
        if len(vals) != 1 or vals != {st}:
            bad.append(ln)
        k = st
        ne = all(len(r) > 0 for r in runs_)
        nonempty_all += ne
        by_oF[k] = by_oF.get(k, 0) + 1
        by_H_oF['H=%d,oF=%d' % (H, k)] = by_H_oF.get('H=%d,oF=%d' % (H, k), 0) + 1
        reps_by_oF[k] = reps_by_oF.get(k, 0) + len(ltuples(H))
        of_lines.append('%s|oF=%d|all_runs_nonempty=%d' % (ln, k, ne))
    with open(os.path.join(edir, 'avoider_classes_oF.txt'), 'x') as fh:
        fh.write(''.join(x + '\n' for x in of_lines))
    pc = [('r', 1)] * 9 + [('s', 0)] * 7 + [('r', 4)] + [('s', 0)]
    named = {'PC-k2 class': 'H=2|runs=111111111/-/-/4|y=0000', 'A1': 'H=1|runs=4/4/4/111111111|y=0000',
             'A2': 'H=3|runs=-/-/4/4444444|y=0020', 'A3': 'H=4|runs=4/4/4/444|y=0243'}
    named_oF = {}
    for nm, cl in named.items():
        H, runs_, ys = parse_class(cl)
        named_oF[nm] = dict(cls=cl, maximal_oF=oF_struct(runs_, ys), all_runs_nonempty=all(len(r) > 0 for r in runs_),
                            is_avoider_class=any(x.startswith(cl + '|') for x in lines))
    ev['maximal_oF'] = dict(
        definition='maximal cyclic constant-block decomposition of the literal cyclic word (PLAN-v1 R1): maximal cyclic'
                   ' runs of equal letters; o_F = number of reflection runs of odd length',
        classes=len(lines), classes_by_oF={str(k): v for k, v in sorted(by_oF.items())},
        classes_by_H_oF=dict(sorted(by_H_oF.items())),
        avoiding_reps_by_oF={str(k): v for k, v in sorted(reps_by_oF.items())},
        oF0_classes=by_oF.get(0, 0), classes_with_all_runs_nonempty=nonempty_all,
        word_vs_structure_or_l_dependence_failures=len(bad), pc_k2_literal_word_maximal_oF=maximal_oF(pc),
        named=named_oF, per_class_file='out/addendum-v1/evidence/avoider_classes_oF.txt')
    if bad or by_oF.get(0, 0) or maximal_oF(pc) != 2 or not all(v['is_avoider_class'] for v in named_oF.values()):
        fails.append('maximal o_F classification')

    # ---- (6) provenance facts
    pv = os.path.join(out, 'addendum-v1', 'provenance')
    rb = os.path.join(out, 'addendum-v1', 'rebuild')
    tc = open(os.path.join(pv, 'toolchain.txt')).read()
    prov = dict(toolchain_file='out/addendum-v1/provenance/toolchain.txt',
                clang_version=re.search(r'^(Apple clang version .*)$', tc, re.M).group(1),
                clang_driver=re.search(r'== type -a clang\+\+\n(.*)\n', tc).group(1),
                clang_resolved=re.search(r'== xcrun --find clang\+\+\n(.*)\n', tc).group(1),
                target=re.search(r'^Target: (.*)$', tc, re.M).group(1),
                sdk_version=re.search(r'== xcrun --show-sdk-version\n(.*)\n', tc).group(1),
                ld_version=re.search(r'PROJECT:(ld-[\d.]+)', tc).group(1),
                macos=re.search(r'ProductVersion:\s*(.*)', tc).group(1) + ' ' + re.search(r'BuildVersion:\s*(.*)', tc).group(1),
                python=re.search(r'== python\n(.*)\n', tc).group(1))
    rebuild = {}
    for b in ('replay_v1', 'replay_v2'):
        lg = open(os.path.join(rb, 'build-%s.log' % b)).read()
        compiler_out = lg.split('== compiler output (warnings/errors) begin\n', 1)[1].split('exit=', 1)[0]
        rb_sha, bin_sha = sha(os.path.join(rb, b)), sha(os.path.join(desk, 'bin', b))
        uuids = re.findall(r'UUID: ([0-9A-F-]+) \(arm64\)', lg + open(os.path.join(pv, 'sig_%s.txt' % b)).read())
        rebuild[b] = dict(command=re.search(r'^cmd: (.*)$', lg, re.M).group(1),
                          exit=int(re.search(r'^exit=(\d+)$', lg, re.M).group(1)),
                          compiler_output_bytes=len(compiler_out), rebuilt_sha256=rb_sha, frozen_sha256=bin_sha,
                          bit_identical=rb_sha == bin_sha, lc_uuids_seen=sorted(set(uuids)),
                          identifier=sorted(set(re.findall(r'^Identifier=(.*)$', lg, re.M))))
        if not (rebuild[b]['bit_identical'] and rebuild[b]['exit'] == 0 and rebuild[b]['compiler_output_bytes'] == 0):
            fails.append('rebuild %s' % b)
    prov['rebuild'] = rebuild
    ff = open(os.path.join(pv, 'frozen_files.txt')).read()
    prov['frozen_file_times'] = re.findall(r'^(\S+ birth=\S+ mtime=\S+ ctime=\S+ size=\d+)$', ff, re.M)
    v1 = open(os.path.join(desk, 'src/olson_p5o4_replay_v1.cpp')).read().split('\n')
    v2 = open(os.path.join(desk, 'src/olson_p5o4_replay_v2.cpp')).read().split('\n')

    def brute_span(lines_):
        s = next(i for i, x in enumerate(lines_) if x.startswith('static int run_brute('))
        e = next(i for i in range(s, len(lines_)) if lines_[i] == '}')
        return s, e

    s1, s2 = brute_span(v1), brute_span(v2)

    def allowed(lines_, span, i):
        x = lines_[i]
        return x.lstrip().startswith('//') or span[0] <= i <= span[1] or 'mode == "brute"' in x

    ops = [o for o in difflib.SequenceMatcher(None, v1, v2, autojunk=False).get_opcodes() if o[0] != 'equal']
    viol = [(o, 'v1', i + 1) for o in ops for i in range(o[1], o[2]) if not allowed(v1, s1, i)]
    viol += [(o, 'v2', j + 1) for o in ops for j in range(o[3], o[4]) if not allowed(v2, s2, j)]
    prov['source_v1_to_v2'] = dict(
        diff_file='out/addendum-v1/provenance/src_v1_to_v2.diff',
        hunks=re.findall(r'^(@@ .* @@)$', open(os.path.join(pv, 'src_v1_to_v2.diff')).read(), re.M),
        changed_lines_outside_comment_brute_dispatcher=len(viol),
        run_brute_span_v1=[s1[0] + 1, s1[1] + 1], run_brute_span_v2=[s2[0] + 1, s2[1] + 1],
        build_comment_line9_v1=v1[8], build_comment_line9_v2=v2[8], build_comment_identical=v1[8] == v2[8])
    if viol:
        fails.append('source diff outside brute')
    ev['provenance'] = prov
    ev['fails'] = fails
    ev['all_ok'] = not fails
    with open(os.path.join(edir, 'evidence.json'), 'x') as fh:
        json.dump(ev, fh, indent=1)
        fh.write('\n')
    print('evidence all_ok=%s fails=%s' % (ev['all_ok'], fails))
    return 0 if ev['all_ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
