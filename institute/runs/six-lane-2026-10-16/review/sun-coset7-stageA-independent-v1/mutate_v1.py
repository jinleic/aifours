#!/usr/bin/env python3
"""Intended-reason mutation fixtures for sun-coset7-stageA-independent checker v1 (stdlib only).

make     --lane L --mutdir M                     build fixtures (exclusive) and a frozen manifest
run      --mutdir M --checker C --checker-sha S  run the frozen checker on each fixture, one at a time
evaluate --mutdir M --out F                      compare each result with its intended reason

Every fixture keeps the files parser-valid and internally consistent (run.json output hashes and
leaf statistics are recomputed for the mutated files), so a rejection must come from the
mathematics or the coverage correspondence, not from a hash or count mismatch.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import os
import signal
import subprocess
import sys
import time
from fractions import Fraction as Fr

RUN_FILES = ('run.json', 'survivors.json', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'leaves.jsonl.gz')
HASHED = ('leaves.jsonl.gz', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'survivors.json')
ADMISSION_FREE = 12_200_000_000 + 16 * 1024 * 1024
STOP = {'flag': False, 'child': None}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rd(p):
    with open(p, 'rb') as f:
        return f.read()


def wx(p, b):
    with open(p, 'xb') as f:
        f.write(b)


def load(src):
    raw = {fn: rd(os.path.join(src, fn)) for fn in RUN_FILES}
    text = gzip.decompress(raw['leaves.jsonl.gz']).decode()
    d = {'run': json.loads(raw['run.json']),
         'killed': json.loads(gzip.decompress(raw['vfc_killed.json.gz'])),
         'duals': json.loads(gzip.decompress(raw['lp_duals.json.gz'])),
         'lines': [json.loads(x) for x in text.split('\n') if x]}
    return raw, d


def encode(raw, d, changed):
    out = dict(raw)
    if 'killed' in changed:
        out['vfc_killed.json.gz'] = gzip.compress(json.dumps(d['killed'], separators=(',', ':')).encode(), mtime=0)
    if 'duals' in changed:
        out['lp_duals.json.gz'] = gzip.compress(json.dumps(d['duals'], separators=(',', ':')).encode(), mtime=0)
    if 'lines' in changed:
        txt = ''.join(json.dumps(l, separators=(',', ':')) + '\n' for l in d['lines']) if d['lines'] else '\n'
        out['leaves.jsonl.gz'] = gzip.compress(txt.encode(), mtime=0)
    rj = d['run']
    if 'lines' in changed:
        counts = {}
        for l in d['lines']:
            counts[l['rule']] = counts.get(l['rule'], 0) + 1
        rj['stats']['leaf_orbits'] = len(d['lines'])
        rj['stats']['leaf_rule'] = counts
    rj['output_sha256'] = {fn: sha(out[fn]) for fn in HASHED}
    out['run.json'] = (json.dumps(rj, indent=1) + '\n').encode()
    return out


def gp(p, q):
    return 2 ** min(p[0], q[0]) * 3 ** min(p[1], q[1]) * 5 ** min(p[2], q[2])


def key_all_ones(sig):
    ents = sorted((1, e[0], e[2], e[3], e[4]) for e in sig)
    return ';'.join('%d/%d,%d,%d,%d' % e for e in ents)


def key_objective(key, y):
    tot = Fr(0)
    for part, yy in zip(key.split(';'), y):
        num, rest = part.split('/')
        den = rest.split(',')[0]
        tot += Fr(int(num), int(den)) * Fr(yy)
    return tot


def edges(k):
    return [(i, j) for i in range(k) for j in range(i + 1, k)]


def p_cert_objective(line, t):
    """Objective of the t-th certificate of an RPLP line when its u and l parts are zero."""
    prof = line['prof']
    k = len(prof)
    E = edges(k)
    rep = [int(c) for c in line['rep']]
    alpha = {}
    for n, (i, j) in enumerate(E):
        alpha[(i, j)] = alpha[(j, i)] = rep[n]
    v, certs = line['witness']
    N = [u for u in range(k) if u != v]
    g = [gp(prof[v], prof[u]) for u in N]
    a = [alpha[(v, u)] for u in N]
    Q = list(itertools.product(*[range(1, g[x] - a[x] + 1) for x in range(len(N))]))
    vec = [Fr(s) for s in certs[t][1]]
    n = len(N)
    ca, cb = vec[:n], vec[n:2 * n]
    rest = vec[2 * n:]
    if any(x != 0 for x in rest):
        return None
    return sum(ca[x] * Fr(Q[t][x], g[x]) for x in range(n)) + sum(cb[x] * (1 - Fr(a[x], g[x])) for x in range(n))


def fstr(x):
    return str(Fr(x))


def build(lane):
    ev = os.path.join(lane, 'evidence')
    src = {U: os.path.join(ev, 'stageA-' + U) for U in ('X1', 'MSP45', 'CORE5')}
    fx = []

    def fixture(name, U, mutate, expect, why):
        raw, d = load(src[U])
        changed, detail = mutate(d)
        fx.append({'name': name, 'universe': U, 'files': encode(raw, d, changed), 'expect': expect,
                   'description': why, 'mutation_detail': detail})

    # --- VFC dual mutations (objective, sign, allowed-set, missing q) on distinct all-ones keys
    raw, d0 = load(src['X1'])
    cands, seen = [], set()
    for sig in d0['killed']:
        key = key_all_ones(sig)
        if key in d0['duals'] and key not in seen:
            seen.add(key)
            y = d0['duals'][key]['y']
            cands.append((key, y, key_objective(key, y)))
    halfable = [c for c in cands if c[2] < 2]
    k1 = halfable[0][0]
    k2, k3, k4 = [c[0] for c in cands if c[0] != k1][:3]

    def m01(d):
        d['duals'][k1]['y'] = [fstr(Fr(s) / 2) for s in d['duals'][k1]['y']]
        return {'duals'}, {'key': k1}
    fixture('X1-M01-vfc-dual-scaled-half', 'X1', m01,
            {'verdict_in': ['INVALID'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_OBJECTIVE_LT_1',
                                                    'LP_DUAL_INVALID_STORED:DUAL_OBJECTIVE_LT_1'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_OBJECTIVE_LT_1': k1, 'LP_DUAL_INVALID_STORED:DUAL_OBJECTIVE_LT_1': k1}},
            'scale one stored VFC dual (all-ones q key of a listed signature) by 1/2: objective < 1')

    def m02(d):
        y = [Fr(s) for s in d['duals'][k2]['y']]
        x = max(range(len(y)), key=lambda i: y[i])
        y[x] = -y[x]
        d['duals'][k2]['y'] = [fstr(t) for t in y]
        return {'duals'}, {'key': k2, 'position': x}
    fixture('X1-M02-vfc-dual-wrong-sign', 'X1', m02,
            {'verdict_in': ['INVALID'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_NEGATIVE', 'LP_DUAL_INVALID_STORED:DUAL_NEGATIVE'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_NEGATIVE': k2}},
            'negate the largest component of one stored VFC dual: y >= 0 violated')

    def m03(d):
        d['duals'][k3]['y'] = [fstr(Fr(s) + 1) for s in d['duals'][k3]['y']]
        return {'duals'}, {'key': k3}
    fixture('X1-M03-vfc-dual-allowed-set-violation', 'X1', m03,
            {'verdict_in': ['INVALID'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_ALLOWED_SUM_GT_1',
                                                    'LP_DUAL_INVALID_STORED:DUAL_ALLOWED_SUM_GT_1'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_ALLOWED_SUM_GT_1': k3}},
            'add 1 to every component of one stored VFC dual: an allowed set (a singleton) exceeds 1, objective still >= 1')

    def m04(d):
        del d['duals'][k4]
        return {'duals'}, {'key': k4}
    fixture('X1-M04-vfc-dual-missing-q', 'X1', m04,
            {'verdict_in': ['INVALID', 'INCOMPLETE'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_MISSING'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_MISSING': k4}},
            'delete the stored dual of one q (all-ones) of a listed signature: missing q')

    # --- RPLP mutations
    rplp = [n for n, l in enumerate(d0['lines']) if l['rule'] == 'RPLP']
    r0 = rplp[0]
    l0 = d0['lines'][r0]
    tP = [t for t, c in enumerate(l0['witness'][1]) if c[0] == 'P']
    tR = [t for t, c in enumerate(l0['witness'][1]) if c[0] == 'R']

    def m05(d):
        d['lines'][r0]['witness'][1].pop()
        return {'lines'}, {'line': r0}
    fixture('X1-M05-rplp-missing-last-q', 'X1', m05,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:RPLP_CERT_COUNT_MISMATCH'],
             'details': {'LEAF_WITNESS_FAILED:RPLP_CERT_COUNT_MISMATCH': l0['canon']}},
            'drop the last per-q certificate of the first RPLP line: one q unrefuted')

    half_t = [t for t in tP if (p_cert_objective(l0, t) or 2) < 2][0]

    def m06(d):
        c = d['lines'][r0]['witness'][1][half_t]
        c[1] = [fstr(Fr(s) / 2) for s in c[1]]
        return {'lines'}, {'line': r0, 'cert': half_t, 'objective_before': str(p_cert_objective(l0, half_t))}
    fixture('X1-M06-rplp-P-scaled-half', 'X1', m06,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:RPLP_P_OBJECTIVE_LT_1'],
             'details': {'LEAF_WITNESS_FAILED:RPLP_P_OBJECTIVE_LT_1': l0['canon']}},
            'scale one RPLP (P) vector by 1/2: columns still hold, objective < 1')

    def m07(d):
        c = d['lines'][r0]['witness'][1][tP[0]]
        n = len(l0['prof']) - 1
        npairs = n * (n - 1) // 2
        c[1][2 * n + npairs] = '-1'
        return {'lines'}, {'line': r0, 'cert': tP[0], 'entry': 2 * n + npairs}
    fixture('X1-M07-rplp-P-negative-l', 'X1', m07,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:RPLP_P_NEGATIVE_UL'],
             'details': {'LEAF_WITNESS_FAILED:RPLP_P_NEGATIVE_UL': l0['canon']}},
            'set the first l multiplier of one (P) vector to -1: wrong sign')

    flip = None
    for n_, l in enumerate(d0['lines']):
        if l['rule'] != 'RPLP':
            continue
        for t, c in enumerate(l['witness'][1]):
            if c[0] == 'P':
                k1n = len(l['prof']) - 1
                vec = [Fr(s) for s in c[1]]
                if all(x == 0 for x in vec[2 * k1n:]) and sum(vec[k1n:2 * k1n]) < -1:
                    flip = (n_, t)
                    break
        if flip:
            break

    def m08(d):
        n_, t = flip
        c = d['lines'][n_]['witness'][1][t]
        k1n = len(d['lines'][n_]['prof']) - 1
        c[1] = c[1][:k1n] + [fstr(-Fr(s)) for s in c[1][k1n:2 * k1n]] + c[1][2 * k1n:]
        return {'lines'}, {'line': n_, 'cert': t}
    fixture('X1-M08-rplp-P-b-sign-flipped', 'X1', m08,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:RPLP_P_COLUMN_VIOLATION'],
             'details': {'LEAF_WITNESS_FAILED:RPLP_P_COLUMN_VIOLATION': d0['lines'][flip[0]]['canon']}},
            'negate the free b multipliers of one (P) vector (sum b < -1): the full-A, empty-S column exceeds 1')

    orig_key = l0['witness'][1][tR[0]][1]
    other = sorted(k for k in d0['duals'] if k != orig_key and len(k.split(';')) == len(orig_key.split(';')))[0]

    def m09(d):
        d['lines'][r0]['witness'][1][tR[0]][1] = other
        return {'lines'}, {'line': r0, 'cert': tR[0], 'from': orig_key, 'to': other}
    fixture('X1-M09-rplp-R-key-swapped', 'X1', m09,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:RPLP_R_KEY_MISMATCH'],
             'details': {'LEAF_WITNESS_FAILED:RPLP_R_KEY_MISMATCH': l0['canon']}},
            'replace the key of one (R) certificate with another stored key: recomputed key differs')

    # --- leaf-line coverage mutations
    pb = [n for n, l in enumerate(d0['lines']) if l['rule'] == 'PB']
    p0 = pb[0]
    lp0 = d0['lines'][p0]

    def m10(d):
        del d['lines'][p0]
        return {'lines'}, {'deleted_line': p0, 'prof': lp0['prof'], 'canon': lp0['canon']}
    fixture('X1-M10-leaf-line-deleted', 'X1', m10,
            {'verdict_in': ['INCOMPLETE', 'INVALID'], 'required': ['LEAF_CLASS_MISSING_LINE'],
             'details': {'LEAF_CLASS_MISSING_LINE': lp0['canon']}},
            'delete one PB leaf line: its reached class has no line (missing leaf)')

    def m11(d):
        w = d['lines'][p0]['witness']
        w[1] = w[1][:1]
        return {'lines'}, {'line': p0, 'S': w[1]}
    fixture('X1-M11-pb-witness-singleton', 'X1', m11,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_WITNESS_FAILED:PB_SUM_LT_1'],
             'details': {'LEAF_WITNESS_FAILED:PB_SUM_LT_1': lp0['canon']}},
            'shrink one PB witness S to a singleton: Bonferroni sum 1 - X_j < 1')

    distinct = [n for n in pb if len({tuple(p) for p in d0['lines'][n]['prof']}) == 5][0]
    ld = d0['lines'][distinct]
    e23 = edges(5).index((2, 3))
    old = int(ld['rep'][e23])
    new = old % 5 + 1
    new_code = ld['rep'][:e23] + str(new) + ld['rep'][e23 + 1:]

    def m12(d):
        d['lines'][distinct]['rep'] = new_code
        d['lines'][distinct]['canon'] = new_code
        return {'lines'}, {'line': distinct, 'from': ld['rep'], 'to': new_code}
    fixture('X1-M12-alpha-altered-consistently', 'X1', m12,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_CLASS_MISSING_LINE'],
             'any_of': [['LEAF_LINE_UNREACHED_CLASS', 'LEAF_LINE_DUPLICATE_CLASS']],
             'details': {'LEAF_CLASS_MISSING_LINE': ld['canon']}},
            'change alpha_23 of a PB line (trivial stabiliser) in both rep and canon: parser-valid, '
            'self-consistent line for another class; the true class loses its line')

    def m13(d):
        d['lines'][distinct]['rep'] = new_code
        return {'lines'}, {'line': distinct, 'rep_to': new_code}
    fixture('X1-M13-alpha-altered-rep-only', 'X1', m13,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_LINE_CANON_MISMATCH'],
             'details': {'LEAF_LINE_CANON_MISMATCH': ld['canon']}},
            'change alpha_23 of rep only: recomputed canonical code differs from canon')

    def m14(d):
        p = d['lines'][p0]['prof']
        p[1], p[2] = p[2], p[1]
        return {'lines'}, {'line': p0, 'prof_after': p}
    fixture('X1-M14-role-swapped-profile', 'X1', m14,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_LINE_PROF_NOT_A_REPRESENTATIVE', 'LEAF_CLASS_MISSING_LINE'],
             'details': {'LEAF_CLASS_MISSING_LINE': lp0['canon']}},
            'swap the profiles of a D3 vertex and a C vertex in one line: role-violating profile tuple')

    target = tuple(map(tuple, l0['prof']))
    gone = [l['canon'] for l in d0['lines'] if tuple(map(tuple, l['prof'])) == target]

    def m15(d):
        d['lines'] = [l for l in d['lines'] if tuple(map(tuple, l['prof'])) != target]
        return {'lines'}, {'prof': list(map(list, target)), 'deleted_lines': len(gone)}
    fixture('X1-M15-profile-orbit-lines-deleted', 'X1', m15,
            {'verdict_in': ['INCOMPLETE', 'INVALID'], 'required': ['LEAF_CLASS_MISSING_LINE'],
             'min_count': {'LEAF_CLASS_MISSING_LINE': len(gone)}},
            'delete every leaf line of one profile orbit (the first RPLP profile): that orbit is uncovered')

    def m16(d):
        d['run']['profiles_total'] = d['run']['profiles_total'] - 1
        return set(), {'profiles_total': d['run']['profiles_total']}
    fixture('X1-M16-profiles-total-understated', 'X1', m16,
            {'verdict_in': ['INVALID'], 'required': ['RUN_JSON_PROFILES_TOTAL_MISMATCH']},
            'claim one profile orbit fewer in run.json: claim differs from the recomputed universe')

    def m17(d):
        d['lines'].append(json.loads(json.dumps(d['lines'][0])))
        return {'lines'}, {'duplicated_line': 0}
    fixture('X1-M17-duplicate-leaf-line', 'X1', m17,
            {'verdict_in': ['INVALID'], 'required': ['LEAF_LINE_DUPLICATE_CLASS']},
            'append a copy of the first leaf line: extra reference to an already-covered class')

    # --- controls universes
    rawm, dm = load(src['MSP45'])
    km = [key_all_ones(s) for s in dm['killed'] if key_all_ones(s) in dm['duals']
          and key_objective(key_all_ones(s), dm['duals'][key_all_ones(s)]['y']) < 2][0]

    def m18(d):
        d['duals'][km]['y'] = [fstr(Fr(s) / 2) for s in d['duals'][km]['y']]
        return {'duals'}, {'key': km}
    fixture('MSP45-M18-vfc-dual-scaled-half', 'MSP45', m18,
            {'verdict_in': ['INVALID'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_OBJECTIVE_LT_1'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_OBJECTIVE_LT_1': km}},
            'MSP45: scale one stored VFC dual by 1/2')

    rawc, dc = load(src['CORE5'])
    kc = [key_all_ones(s) for s in dc['killed'] if key_all_ones(s) in dc['duals']][0]

    def m19(d):
        del d['duals'][kc]
        return {'duals'}, {'key': kc}
    fixture('CORE5-M19-vfc-dual-missing-q', 'CORE5', m19,
            {'verdict_in': ['INVALID', 'INCOMPLETE'], 'required': ['VFC_SIG_NOT_VERIFIED:DUAL_MISSING'],
             'details': {'VFC_SIG_NOT_VERIFIED:DUAL_MISSING': kc}},
            'CORE5: delete the stored dual of one q of a listed signature')

    # --- benign controls (must stay COMPLETE_VALID)
    def b01(d):
        d['lines'] = list(reversed(d['lines']))
        return {'lines'}, {'reversed': True}
    fixture('X1-B01-lines-reordered', 'X1', b01, {'verdict_in': ['COMPLETE_VALID']},
            'benign: reverse the order of the leaf lines')

    def b02(d):
        return set(), {'unchanged': True}
    fixture('X1-B02-unchanged-copy', 'X1', b02, {'verdict_in': ['COMPLETE_VALID']},
            'benign: byte copy of the inputs (run.json re-serialised with identical output hashes)')
    return fx


def cmd_make(args):
    os.mkdir(args.mutdir)
    man = {'generator': os.path.abspath(__file__), 'generator_sha256': sha(rd(os.path.abspath(__file__))),
           'lane': args.lane, 'made_host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'fixtures': []}
    for f in build(args.lane):
        d = os.path.join(args.mutdir, f['name'])
        os.mkdir(d)
        os.mkdir(os.path.join(d, 'input'))
        hashes = {}
        for fn in RUN_FILES:
            wx(os.path.join(d, 'input', fn), f['files'][fn])
            hashes[fn] = sha(f['files'][fn])
        exp = {'name': f['name'], 'universe': f['universe'], 'description': f['description'],
               'mutation_detail': f['mutation_detail'], 'expect': f['expect'], 'input_sha256': hashes}
        wx(os.path.join(d, 'expect.json'), (json.dumps(exp, indent=1, default=str) + '\n').encode())
        man['fixtures'].append({'name': f['name'], 'universe': f['universe'], 'input_sha256': hashes,
                                'expect_sha256': sha(rd(os.path.join(d, 'expect.json')))})
    wx(os.path.join(args.mutdir, 'manifest.json'), (json.dumps(man, indent=1) + '\n').encode())
    print(json.dumps({'fixtures': len(man['fixtures'])}))
    return 0


def _term(signum, frame):
    STOP['flag'] = True
    if STOP['child'] is not None and STOP['child'].poll() is None:
        STOP['child'].send_signal(signal.SIGTERM)


def cmd_run(args):
    signal.signal(signal.SIGTERM, _term)
    man = json.loads(rd(os.path.join(args.mutdir, 'manifest.json')))
    env = dict(os.environ)
    env['TMPDIR'] = args.tmpdir
    records = []
    for f in man['fixtures']:
        d = os.path.join(args.mutdir, f['name'])
        rec = {'name': f['name']}
        if STOP['flag']:
            rec['status'] = 'NOT_STARTED_STOP_REQUESTED'
            records.append(rec)
            continue
        if sha(rd(args.checker)) != args.checker_sha:
            rec['status'] = 'NOT_STARTED_CHECKER_HASH_MISMATCH'
            records.append(rec)
            break
        bad = [fn for fn in RUN_FILES if sha(rd(os.path.join(d, 'input', fn))) != f['input_sha256'][fn]]
        st = os.statvfs(d)
        free = st.f_bavail * st.f_frsize
        rec['admission_free_bytes'] = free
        if bad or free < ADMISSION_FREE:
            rec['status'] = 'NOT_STARTED_ADMISSION' if not bad else 'NOT_STARTED_INPUT_HASH'
            records.append(rec)
            continue
        cmd = [sys.executable, args.checker, 'verify', '--universe', f['universe'],
               '--input-dir', os.path.join(d, 'input'), '--out', os.path.join(d, 'result.json')]
        rec['command'] = cmd
        t0 = time.monotonic()
        with open(os.path.join(d, 'stdout.txt'), 'xb') as so, open(os.path.join(d, 'stderr.txt'), 'xb') as se:
            p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=so, stderr=se, env=env)
            STOP['child'] = p
            rc = p.wait()
            STOP['child'] = None
        rec['exit_code'] = rc
        rec['wall_seconds'] = round(time.monotonic() - t0, 3)
        rec['status'] = 'RAN'
        wx(os.path.join(d, 'run_record.json'), (json.dumps(rec, indent=1) + '\n').encode())
        records.append(rec)
    wx(os.path.join(args.mutdir, 'run_records.json'), (json.dumps(records, indent=1) + '\n').encode())
    print(json.dumps({'ran': sum(1 for r in records if r.get('status') == 'RAN'), 'total': len(records)}))
    return 0


def cmd_evaluate(args):
    man = json.loads(rd(os.path.join(args.mutdir, 'manifest.json')))
    out = {'evaluated_host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'fixtures': []}
    allpass = True
    for f in man['fixtures']:
        d = os.path.join(args.mutdir, f['name'])
        exp = json.loads(rd(os.path.join(d, 'expect.json')))['expect']
        ev = {'name': f['name']}
        try:
            rr = json.loads(rd(os.path.join(d, 'run_record.json')))
            res = json.loads(rd(os.path.join(d, 'result.json')))
        except OSError as e:
            ev.update(passed=False, reason='missing record/result: %s' % e)
            out['fixtures'].append(ev)
            allpass = False
            continue
        uni = res['universes'][f['universe']]
        issues = uni.get('issues', {})
        ev['exit_code'] = rr.get('exit_code')
        ev['verdict'] = uni.get('status')
        ev['issue_codes'] = {c: r['count'] for c, r in issues.items()}
        reasons = []
        if ev['verdict'] not in exp['verdict_in']:
            reasons.append('verdict %s not in %s' % (ev['verdict'], exp['verdict_in']))
        if (ev['verdict'] == 'COMPLETE_VALID') != (rr.get('exit_code') == 0):
            reasons.append('exit code inconsistent with verdict')
        for c in exp.get('required', []):
            if c not in issues:
                reasons.append('required code %s absent' % c)
        for group in exp.get('any_of', []):
            if not any(c in issues for c in group):
                reasons.append('none of %s present' % group)
        for c, needle in exp.get('details', {}).items():
            if c in issues and needle not in json.dumps(issues[c]['examples']):
                reasons.append('code %s does not cite %s' % (c, needle))
        for c, m in exp.get('min_count', {}).items():
            if issues.get(c, {}).get('count', 0) < m:
                reasons.append('code %s count below %d' % (c, m))
        ev['passed'] = not reasons
        ev['reasons'] = reasons
        allpass &= ev['passed']
        out['fixtures'].append(ev)
    out['all_passed'] = allpass
    wx(args.out, (json.dumps(out, indent=1) + '\n').encode())
    print(json.dumps({'all_passed': allpass, 'n': len(out['fixtures']),
                      'failed': [e['name'] for e in out['fixtures'] if not e['passed']]}))
    return 0 if allpass else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('--lane', required=True)
    m.add_argument('--mutdir', required=True)
    r = sub.add_parser('run')
    r.add_argument('--mutdir', required=True)
    r.add_argument('--checker', required=True)
    r.add_argument('--checker-sha', required=True)
    r.add_argument('--tmpdir', required=True)
    e = sub.add_parser('evaluate')
    e.add_argument('--mutdir', required=True)
    e.add_argument('--out', required=True)
    args = ap.parse_args()
    return {'make': cmd_make, 'run': cmd_run, 'evaluate': cmd_evaluate}[args.cmd](args)


if __name__ == '__main__':
    sys.exit(main())
