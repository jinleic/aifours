#!/usr/bin/env python3
"""Reviewer-authored f144 assurance controls. Never imports or executes author code.
Rechecks manifest/input bytes; audits the precise content-rule rejection reasons;
refutes the original coordinate inference in a four-element rectangular band;
verifies two finite example tables from independently parsed identity expressions.
Creates only the exclusive reviewer-f144-assurance-v1.json receipt beside this file.
"""
from pathlib import Path
import hashlib
import itertools
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding')

def clock():
    return subprocess.check_output(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()

def info(path):
    raw = path.read_bytes()
    return dict(path=str(path), sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), LF=raw.count(b'\n'))

class Rejection(Exception):
    pass

checks = []
def must(condition, name, **details):
    if not condition:
        raise AssertionError(name)
    checks.append(dict(name=name, passed=True, **details))
    print('PASS', name, details if details else '')

def expect_rejection(name, wanted, call):
    try:
        call()
    except Rejection as exc:
        actual = str(exc)
        must(actual == wanted, name, expected_reason=wanted, actual_reason=actual)
        return
    raise AssertionError(name + ': accepted instead of intended rejection ' + wanted)

# A strict full factorization certificate, not an unrestricted equality oracle.
def verify_content_step(source, target, P, X, Y, Z, Q):
    if not X or not Y or not Z:
        raise Rejection('EMPTY_FACTOR')
    if P + X + Y + Z + Q != source or P + X + Z + Q != target:
        raise Rejection('LITERAL_FACTORIZATION_MISMATCH')
    if set(X) != set(Z):
        raise Rejection('END_CONTENT_MISMATCH')
    if not set(Y) <= set(X):
        raise Rejection('MIDDLE_CONTENT_NOT_CONTAINED')
    return True

def verify_square_step(source, target, P, W, Q):
    if not W or source != P + W + W + Q or target != P + W + Q:
        raise Rejection('NOT_THE_STATED_CONSECUTIVE_SQUARE')
    return True

# Independent parenthesized-word interpreter. Each nonempty lowercase word is a
# left-associated semigroup term; nested parentheses force recursive evaluation.
def parse_term(s):
    pos = 0
    def sequence(nested):
        nonlocal pos
        out = []
        while pos < len(s) and s[pos] != ')':
            ch = s[pos]
            pos += 1
            if ch == '(':
                out.append(sequence(True))
            elif ch.isascii() and ch.islower():
                out.append(ch)
            else:
                raise Rejection('TERM_SYNTAX')
        if not out:
            raise Rejection('EMPTY_TERM')
        if nested:
            if pos == len(s) or s[pos] != ')':
                raise Rejection('TERM_SYNTAX')
            pos += 1
        return tuple(out)
    term = sequence(False)
    if pos != len(s):
        raise Rejection('TERM_SYNTAX')
    return term

def value(tree, assignment, table):
    if isinstance(tree, str):
        return assignment[tree]
    factors = [value(t, assignment, table) for t in tree]
    total = factors[0]
    for factor in factors[1:]:
        total = table[total][factor]
    return total

def identity_audit(T, lhs, rhs, names):
    left, right = parse_term(lhs), parse_term(rhs)
    count, failures, first = 0, 0, None
    for vals in itertools.product(range(len(T)), repeat=len(names)):
        assignment = dict(zip(names, vals))
        lv, rv = value(left, assignment, T), value(right, assignment, T)
        count += 1
        if lv != rv:
            failures += 1
            if first is None:
                first = dict(assignment=assignment, left_value=lv, right_value=rv)
    return dict(assignments=count, failures=failures, first_failure=first)

B5 = [[0,0,0,0,0], [0,1,0,3,4], [2,2,2,2,2], [0,1,4,3,4], [4,4,4,4,4]]
B6 = [[0,0,0,0,0,0], [0,1,0,1,4,5], [2,2,2,2,2,2], [0,1,2,3,4,5], [0,1,5,4,4,5], [5,5,5,5,5,5]]

if __name__ == '__main__':
    before = clock()
    print('START', before)
    expected_manifests = [('manifest-v1.json', '24d290eac38f25d87fdaee0276f8ecae04609da0b20c810e852efc5e121f42d1', 2488, 33),
                          ('manifest-v2.json', '843b051c235415a7e5faed2cd9a36e59737770a1c6b05acafc4c2c5b11a46344', 3566, 43)]
    manifests = []
    # v1 LF is recorded, not independently preclaimed: its manifest did not pin its own LF.
    for filename, wanted, size, lf in expected_manifests:
        path = HERE / filename
        item = info(path)
        must(item['sha256'] == wanted and item['bytes'] == size, 'manifest integrity ' + filename)
        manifest = json.loads(path.read_text())
        item['complete_inputs'] = []
        for source in manifest['inputs_in_read_order']:
            actual = info(Path(source['path']))
            must(all(actual[k] == source[k] for k in ('sha256', 'bytes', 'LF')), 'pinned full SHA/bytes/LF ' + Path(source['path']).name)
            item['complete_inputs'].append(actual)
        manifests.append(item)

    # Original inference is false in a fully checked four-element rectangular band.
    rb = list(itertools.product(range(2), repeat=2))
    mul = lambda p, q: (p[0], q[1])
    must(all(mul(p,p) == p for p in rb) and all(mul(mul(p,q),r) == mul(p,mul(q,r)) for p,q,r in itertools.product(rb,repeat=3)), '2x2 rectangular band idempotent and associative')
    X, U = (0,0), (1,1)
    must(mul(mul(X,U),X) == X and X[0] != U[0], 'original XUX=X does not imply same R-row', X=X, U=U, XUX=mul(mul(X,U),X))
    must(all(mul(p,mul(p,q)) == mul(p,q) for p,q in itertools.product(rb,repeat=2)), 'separate X(XY)=(XX)Y=XY identity')
    must(all((mul(p,q) == q) == (p[0] == q[0]) for p,q in itertools.product(rb,repeat=2)), 'erratum uv=v iff same R-row')
    must(all(mul(mul(p,q),r) == mul(p,r) for p,q,r in itertools.product(rb,repeat=3)), 'rectangular pqr=pr identity')

    c1 = ('abcacbcdbcabcda','abcacbcdcabcda','','abcacbcd','b','cabcd','a')
    c2 = ('abcacbcdcabcda','abcacbcdabcda','','abcacbcd','c','abcd','a')
    must(verify_content_step(*c1), 'actual content step 1 certificate')
    must(verify_content_step(*c2), 'actual content step 2 certificate')
    expect_rejection('end-content mutation is rejected for its intended reason', 'END_CONTENT_MISMATCH',
                     lambda: verify_content_step('abcacbcdbcabca','abcacbcdcabca','','abcacbcd','b','cabc','a'))
    expect_rejection('middle-content mutation is rejected for its intended reason', 'MIDDLE_CONTENT_NOT_CONTAINED',
                     lambda: verify_content_step('abcacbcdcabca','abcacbccabca','','abcacbc','d','cabc','a'))
    expect_rejection('missing context mutation is rejected for its intended reason', 'LITERAL_FACTORIZATION_MISMATCH',
                     lambda: verify_content_step(*c1[:-1], ''))
    must(verify_square_step('xabab','xab','x','ab',''), 'square certificate positive control')
    expect_rejection('non-square deletion is rejected for its intended reason', 'NOT_THE_STATED_CONSECUTIVE_SQUARE',
                     lambda: verify_square_step('xabac','xab','x','ab',''))

    def ends(w):
        alphabet = set(w)
        for i in range(len(w)):
            if set(w[:i+1]) == alphabet:
                pref, ltof = w[:i], w[i]
                break
        for j in range(len(w)-1,-1,-1):
            if set(w[j:]) == alphabet:
                ftol, suff = w[j], w[j+1:]
                break
        return dict(pref=pref, ltof=ltof, ftol=ftol, suff=suff)
    for cert in (c1,c2):
        u,v,P,X,Y,Z,Q = cert
        a,b = ends(X+Y+Z),ends(X+Z)
        must(a == b, 'literal Green-Rees prefix/suffix boundary check', source=X+Y+Z, target=X+Z, boundary=a)

    # Three independent term-syntax evaluation layers; these table results do not
    # require interpreting the table as a free band or importing Green-Rees.
    finite = []
    for T, expected in ((B5, (False,True,True)), (B6, (False,False,False))):
        n = len(T)
        audits = dict(
            idempotence=identity_audit(T,'xx','x','x'),
            associativity=identity_audit(T,'(xy)z','x(yz)','xyz'),
            regular=identity_audit(T,'xyxzx','xyzx','xyz'),
            local=identity_audit(T,'(exe)(eye)(exe)(eze)(exe)','(exe)(eye)(eze)(exe)','exyz'),
            SN=identity_audit(T,'abcda','abcacda','abcd'))
        must(audits['idempotence']['failures'] == 0 and audits['associativity']['failures'] == 0, f'term-parser order-{n} band axioms')
        observed = tuple(audits[name]['failures'] == 0 for name in ('regular','local','SN'))
        must(observed == expected, f'term-parser order-{n} regular/local/SN flags', expected=expected, observed=observed)
        for e in range(n):
            localset = {T[T[e][x]][e] for x in range(n)}
            must(all(T[e][q] == q and T[q][e] == q for q in localset), f'order-{n} e={e} identity on eBe', local_elements=sorted(localset))
        finite.append(dict(order=n, table=T, expected_regular_local_SN=expected, audits=audits))
    must(value(parse_term('(ab)c'), dict(a=1,b=3,c=2), B5) == value(parse_term('a(bc)'), dict(a=1,b=3,c=2), B5), 'term-parser associativity positive control')
    # Concrete SN failure in B6 is a negative identity-control; regular failure in
    # B5 rules out conflating global regularity and local regularity.
    must(finite[0]['audits']['regular']['failures'] > 0 and finite[0]['audits']['local']['failures'] == 0, 'global-versus-local regularity negative control')
    must(finite[1]['audits']['SN']['failures'] > 0 and finite[1]['audits']['local']['failures'] > 0, 'B6 negative control rejects both identities')
    receipt = dict(kind='REVIEWER_OWN_EXACT_CONTROLS', clock_before=before, clock_after=clock(), script=info(Path(__file__)), manifests=manifests, checks=checks, finite_bands=finite,
                   imports='Green-Rees structure/word problem theorem is a classical import, not proved by these controls. No author program executed or imported. No external model, paid API, novelty or embedding verification.')
    dest = HERE / 'reviewer-f144-assurance-v1.json'
    with dest.open('x') as f:
        json.dump(receipt,f,indent=2)
        f.write('\n')
    print('RECEIPT', json.dumps(info(dest)))
    print('END', clock())
