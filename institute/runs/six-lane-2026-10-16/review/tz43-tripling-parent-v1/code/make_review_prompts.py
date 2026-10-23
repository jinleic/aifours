#!/usr/bin/env python3
"""Build the two static-review prompts REVIEW/tz43-tripling-codex-v1.prompt.txt and
REVIEW/tz43-tripling-claude-v1.prompt.txt (exclusive create) from the frozen desk files.
Usage: /usr/bin/python3 -B make_review_prompts.py
"""
import hashlib
import json
import os

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
PARENT = os.path.join(REVIEW, 'tz43-fdgdd18-parent-v1', 'code', 'check_fdgdd_format_d.py')
CLAUDE = os.path.join(REVIEW, 'tz43-claude-verifier-v1', 'checker.py')
REVIEWED = ['lemma-v1.md', 'code/build_tripled_fdgdd.py', 'code/run_checker_matrix.py']
NAMES = ('tz43-tripling-codex-v1', 'tz43-tripling-claude-v1')


def raw(path):
    with open(path, 'rb') as f:
        return f.read()


def sha(path):
    return hashlib.sha256(raw(path)).hexdigest()


def numbered(path, lo=1, hi=None):
    lines = raw(path).decode('utf-8').split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    hi = hi or len(lines)
    return '\n'.join('%5d| %s' % (i, lines[i - 1]) for i in range(lo, hi + 1))


def results_summary():
    man = json.load(open(os.path.join(DESK, 'build-manifest.json')))
    mat = json.load(open(os.path.join(DESK, 'checker-matrix-v1.json')))
    out = ['Generator stats (build-manifest.json sha256 %s):' % sha(os.path.join(DESK, 'build-manifest.json')),
           json.dumps(man['stats'], sort_keys=False),
           'Written files: ' + json.dumps(dict((k, v['sha256']) for k, v in man['outputs'].items()))]
    for name, spec in man['mutations'].items():
        a = dict(spec['analysis'])
        d = a.pop('class_defects_uncovered_multicovered_by_part', None)
        if d is not None:
            a['per_class_[uncovered,multicovered]_by_part_A_B_C'] = [[x['A'], x['B'], x['C']] for x in d]
        out.append('%s: %s' % (name, json.dumps(a)))
    out.append('Checker matrix (checker-matrix-v1.json sha256 %s) summary: %s'
               % (sha(os.path.join(DESK, 'checker-matrix-v1.json')), json.dumps(mat['summary'])))
    seen = {}
    for r in mat['rows']:
        key = (r['checker'], r['case'])
        obs = r.get('failed_checks') if r['checker'] == 'parent' else r.get('invariant')
        seen.setdefault(key, set()).add((r['exit'], json.dumps(obs), r['ok']))
    for (chk, case), vals in sorted(seen.items()):
        out.append('  %s / %s: %s over 4 interpreter-mode runs' % (chk, case, sorted(vals)))
    return '\n'.join(out)


TASK = r"""You are a hostile static reviewer for a parent research verification desk. Review CORRECTNESS ONLY:
no novelty, priority or significance judgement is wanted (the desk claims none; Lemma 1 may be folklore).

Objects under review
(A) lemma-v1.md - Lemma 1 (the zero-sum Z3 blow-up of any 3-regular 3-partite 3-graph splits into 9 perfect
    matchings, via a proper 3-edge-colouring u of the incidence bipartite graph and labels
    P = (x+u(a,e), y+u(b,e))), Lemma 2 (missing-group families of a GDD(2,3,4g) of type g^4 are (g/2)-regular),
    Theorem 3 (every zero-sum-tripled GDD(3,4,30) of type 6^5, i.e. H(5,6,4,3), is an FDGDD(3,4,5{18}) whose
    Kirkman frames are written down explicitly). The only permitted external import is Hall's theorem.
(B) code/build_tripled_fdgdd.py - stdlib generator implementing Theorem 3 on one pinned master; writes a Format D
    certificate (same 14580 blocks as an earlier SAT-framed certificate, new constructive frames) and four
    intentionally broken mutation fixtures.
(C) code/run_checker_matrix.py - runner executing two pre-existing, unchanged checkers on the certificate and
    fixtures with hash binding and intended-failure categories.

Mandatory hostile checks
1. Lemma 1 Step 5(iii), third part: verify BOTH existence and uniqueness of the member of C_P through (c,z), the
   exact use of (U3), and that nothing silently assumes more (linearity, simple H, equal part sizes, the same s for
   all edges, a particular orientation of parts).
2. Lemma 1 Steps 1-4: regularity of the incidence graph, the Hall argument (including |L| = |R|), (U1)/(U2)/(U3),
   and "every lift has exactly one label".
3. Lemma 2: re-derive n_b = n_c = n_d = g/2 from the GDD definition; check every counting step.
4. Theorem 3 (a)-(d): inflation gives a GDD(3,4,90) of type 18^5; the derived design at (p,beta) is the zero-sum
   lift with s = -beta (check the sign); triples missing G_i are exactly the lifts of F_i(p); the 36 classes satisfy
   the Kirkman-frame definition D3 exactly (each class a PC of (X minus G_x) minus G_i). Check that frames on the
   derived triples are not conflated with resolving the 4-blocks (RH) or with resolvable derived designs (RDGDD).
5. Code: does (B) implement exactly the lemma (label 3p+beta, s = (-beta) mod 3, P = (x+u_a, y+u_b) with parts in
   increasing group order)? Are its internal checks strong enough that no wrong positive certificate can be
   written? Are the four mutations exactly as described (mut_b keeps u a bijection at every vertex and breaks only
   the zero sum on the edges at a*; mut_c uses s' = s + 1)? Do the expected checker categories follow from the two
   checkers' logic? Any Python 3.9 incompatibility, nondeterminism, overwrite risk or hash-binding gap in (C)?

Output format (strict)
Line 1 exactly one of: DISPOSITION: ACCEPT | DISPOSITION: ACCEPT-WITH-FIXES | DISPOSITION: REJECT
Then "Findings:" and a numbered list, each item: [FATAL|MAJOR|MINOR] <file>:<LF line(s)> - problem - exact
correction. Write "Findings: none" if there are none.
Then "Third-part audit:" (at most 10 lines, your own derivation outcome) and "Degree-count audit:" (at most 10
lines). Do not discuss novelty. Do not restate the documents.
"""


def codex_prompt():
    files = '\n'.join('  %s  sha256 %s' % (os.path.join(DESK, p), sha(os.path.join(DESK, p))) for p in REVIEWED)
    ctx = '\n'.join('  %s  sha256 %s' % (p, sha(p)) for p in (
        PARENT, CLAUDE, os.path.join(DESK, 'build-manifest.json'), os.path.join(DESK, 'checker-matrix-v1.json'),
        os.path.join(DESK, 'incidence-colourings.json'), os.path.join(DESK, 'fdgdd_5_18_konig_tripled.txt')))
    return (TASK + """
Static review only. You may read files (cat, sed -n, nl, grep) and compute sha256 with shasum -a 256; do NOT
execute Python, the generator, the runner or either checker, and do not write any file. Verify the sha256 of each
reviewed file first and report any mismatch as FATAL.

Reviewed files (frozen):
""" + files + """
Context files (read as needed; the two checkers are pre-existing and are NOT under review, only how (B)/(C) use
them):
""" + ctx + """
Definitions source: lemma-v1.md section 0 quotes Tan-Zhou arXiv:2503.11934v1 LF 48-59, 69-70, 237-247.

Parent-reported execution results (context only; do not trust them as proof):
""" + results_summary() + '\n')


def claude_prompt():
    parts = [TASK, """
You have no tools. Everything you need is inlined below; cite lines as <file>:<LF>. The two checkers are
pre-existing and are NOT under review; excerpts are given only so that you can judge whether the expected failure
categories in (B)/(C) follow from their logic.
"""]
    for p in REVIEWED:
        full = os.path.join(DESK, p)
        parts.append('===== BEGIN %s (sha256 %s), LF-numbered =====\n%s\n===== END %s =====\n'
                     % (p, sha(full), numbered(full), p))
    parts.append('===== Parent checker excerpt %s (sha256 %s): classify_class and frame checks =====\n%s\n%s\n'
                 % (os.path.basename(PARENT), sha(PARENT), numbered(PARENT, 210, 230), numbered(PARENT, 461, 527)))
    parts.append('===== Claude-authored checker excerpt %s (sha256 %s): sha binding, fdgdd header, class checks =====\n'
                 '%s\n%s\n%s\n' % (os.path.basename(CLAUDE), sha(CLAUDE), numbered(CLAUDE, 77, 87),
                                   numbered(CLAUDE, 170, 183), numbered(CLAUDE, 426, 482)))
    parts.append('Parent-reported execution results (context only; do not trust them as proof):\n'
                 + results_summary() + '\n')
    return '\n'.join(parts)


def main():
    out = {}
    for name, text in zip(NAMES, (codex_prompt(), claude_prompt())):
        path = os.path.join(REVIEW, name + '.prompt.txt')
        with open(path, 'x') as f:
            f.write(text)
        out[name] = {'path': path, 'sha256': sha(path), 'bytes': len(raw(path))}
    out['reviewed_files'] = dict((p, sha(os.path.join(DESK, p))) for p in REVIEWED)
    with open(os.path.join(DESK, 'review-prompts-v1.json'), 'x') as f:
        json.dump(out, f, indent=1)
        f.write('\n')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
