#!/usr/bin/env python3
"""reviewer-f144-exact-controls-v2-mutations.py  (reviewer-authored; additive to v1, f144 review)

Why v2 exists: control C6 "wrong deletion abcacbcdbcabcda -> abcacbcdbabcda" in v1 was mis-designed by the
reviewer: deleting that 'c' IS a valid (C) absorption (X=abcacbcdb, Y=c, Z=abcd), so parser and Green-Rees
correctly agreed it is valid and the v1 line reported FAIL.  The v1 log is preserved unchanged.  Here:
  M1  a genuinely invalid deletion (the first 'd', leaving X without d) is rejected AND unequal in FB;
  M2  parser soundness sweep: for every word u of the 23 author transitions and every deletion of a factor of
      length 1..4 from u, if the reviewer parser accepts (square or (C)) then gr(u)==gr(v) must hold
      (acceptance never contradicts Green-Rees); counts of accepted/rejected/equal are reported;
  M3  completeness note: rejected-but-equal deletions (valid band equalities not expressible as ONE square or
      (C) step) are counted, not failed - the author only claims single-step moves for the displayed steps;
  M4  independent Python re-verification of the two example tables printed by reviewer-f144-small-bands-v2
      (order-5 band: locally regular, SN, not regular; order-6 band: not locally regular, not SN).
Imports only the reviewer's own v1 module (never author code).
"""
import sys, os, time, importlib.util, itertools

def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('v1', os.path.join(here, 'reviewer-f144-exact-controls-v1.py'))
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)
gr, eq, square_witnesses, C_witnesses, extract_traces = v1.gr, v1.eq, v1.square_witnesses, v1.C_witnesses, v1.extract_traces

FAILS = []
def check(cond, msg):
    print(f"[{'PASS' if cond else 'FAIL'}] {msg}")
    if not cond:
        FAILS.append(msg)

B5 = [[0,0,0,0,0],
      [0,1,0,3,4],
      [2,2,2,2,2],
      [0,1,4,3,4],
      [4,4,4,4,4]]
B6 = [[0,0,0,0,0,0],
      [0,1,0,1,4,5],
      [2,2,2,2,2,2],
      [0,1,2,3,4,5],
      [0,1,5,4,4,5],
      [5,5,5,5,5,5]]

def band_flags(T):
    n = len(T)
    M = lambda x, y: T[x][y]
    idem = all(M(i, i) == i for i in range(n))
    assoc = all(M(M(x, y), z) == M(x, M(y, z)) for x in range(n) for y in range(n) for z in range(n))
    reg = all(M(M(M(M(x, y), x), z), x) == M(M(M(x, y), z), x) for x in range(n) for y in range(n) for z in range(n))
    loc = True
    for e in range(n):
        L = [M(M(e, x), e) for x in range(n)]
        for X, Y, Z in itertools.product(L, L, L):
            if M(M(M(M(X, Y), X), Z), X) != M(M(M(X, Y), Z), X):
                loc = False
    sn = all(M(M(M(M(a, b), c), d), a) == M(M(M(M(M(M(a, b), c), a), c), d), a) for a in range(n) for b in range(n) for c in range(n) for d in range(n))
    return idem, assoc, reg, loc, sn

def main():
    md_path = sys.argv[1]
    print('reviewer-f144-exact-controls-v2-mutations start', utc())
    print('author md sha256', v1.sha256_file(md_path))
    traces = extract_traces(open(md_path, encoding='utf-8').read())

    print('\n== M1 genuinely invalid deletion ==')
    u = 'abcacbcdbcabcda'
    v = u[:7] + u[8:]          # deletes the first 'd' -> abcacbc bcabcda
    check(v == 'abcacbcbcabcda', f'mutant is {v}')
    check(len(square_witnesses(u, v)) == 0 and len(C_witnesses(u, v)) == 0 and not eq(u, v),
          f'{u} -> {v}: rejected by parser AND unequal in FB (intended reason: X would lack d, cont(Y)={{d}} not<= cont(X))')
    v_old = u[:9] + u[10:]
    cw = C_witnesses(u, v_old)
    check(len(cw) >= 1 and eq(u, v_old),
          f'v1 mutant {u} -> {v_old} is in fact a valid (C) step, e.g. {cw[0]}; parser and gr agree (reviewer control-design error in v1, not a proof defect)')

    print('\n== M2 parser soundness sweep over all 23 transition sources ==')
    words = []
    for nm, (ws, mk) in traces.items():
        words += ws[:-1]
    check(len(words) == 23, f'{len(words)} transition source words')
    accepted = rejected = acc_eq = acc_neq = rej_eq = rej_neq = 0
    bad = []
    for u in words:
        n = len(u)
        for k in range(1, 5):
            for i in range(0, n - k + 1):
                v = u[:i] + u[i + k:]
                if not v:
                    continue
                acc = bool(square_witnesses(u, v)) or bool(C_witnesses(u, v))
                same = eq(u, v)
                if acc:
                    accepted += 1
                    if same: acc_eq += 1
                    else:
                        acc_neq += 1; bad.append((u, v))
                else:
                    rejected += 1
                    if same: rej_eq += 1
                    else: rej_neq += 1
    print(f'   deletions tried: {accepted + rejected}; accepted {accepted} (gr-equal {acc_eq}, gr-UNEQUAL {acc_neq}); rejected {rejected} (gr-equal {rej_eq}, gr-unequal {rej_neq})')
    check(acc_neq == 0, 'parser soundness: every accepted single square/(C) step is a Green-Rees equality' + (f' violations {bad[:3]}' if bad else ''))
    check(rej_neq > 0, 'negative controls exist: many rejected deletions are genuinely unequal in FB (the parser is not vacuous)')
    print(f'   M3 note: {rej_eq} rejected deletions are nevertheless free-band equalities (multi-step or other rules); not claimed by the author as single steps.')

    print('\n== M4 independent recheck of the example tables printed by reviewer-f144-small-bands-v2 ==')
    idem, assoc, reg, loc, sn = band_flags(B5)
    check(idem and assoc, 'order-5 table is a band (idempotent, associative)')
    check(loc and sn and not reg, f'order-5 band: locally regular={loc}, SN={sn}, regular={reg}  (expected True, True, False)')
    idem, assoc, reg, loc, sn = band_flags(B6)
    check(idem and assoc, 'order-6 table is a band (idempotent, associative)')
    check((not loc) and (not sn) and (not reg), f'order-6 band: locally regular={loc}, SN={sn}, regular={reg}  (expected False, False, False)')
    check(all(B6[3][j] == j and B6[j][3] == j for j in range(6)), 'order-6 band: element 3 is a two-sided identity, so eBe=B for e=3 and LOC there reduces to REG')

    print('\n== SUMMARY ==')
    print('FAIL count', len(FAILS))
    for m in FAILS:
        print('  FAIL:', m)
    print('end', utc())
    sys.exit(1 if FAILS else 0)

if __name__ == '__main__':
    main()
