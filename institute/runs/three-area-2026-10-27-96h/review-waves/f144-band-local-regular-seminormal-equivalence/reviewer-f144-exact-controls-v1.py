#!/usr/bin/env python3
"""reviewer-f144-exact-controls-v1.py  (reviewer-authored; f144 same-harness review)

Independent exact controls for the claim
    every local monoid eBe of a band B is regular (xyxzx=xyzx)  <=>  B |= abcda = abcacda.

Nothing here imports or executes author code.  The author's markdown is opened ONLY to
extract the literal rewrite-trace strings of its section 4 as text, so that transcription
by the reviewer cannot silently repair them.

Controls:
  C1  own Green-Rees signature gr(); positive controls |FB(1..3)| = 1, 6, 159 (optionally |FB(4)| = 332380)
      and classical equalities/inequalities;
  C2  own reconstruction of both local-regular substitutions (I: e=c, A=a, B=b, C=da; II: e=bc, A=a, B=ac, C=d)
      with their contexts, compared letter-for-letter to the authors' chain start words;
  C3  own literal parser: every transition of the four chains must be a consecutive-square deletion WW->W
      or (only where the author marks (C)) a factorization P.X.Y.Z.Q -> P.X.Z.Q with
      cont(Y) <= cont(X) = cont(Z); witnesses are printed; gr() must be constant along each chain;
  C4  combination logic of the two local equalities to (SN);
  C5  the 2=>1 substitution c:=e reduces, by ee->e deletions only, to the regular identity;
  C6  mutation (intended-reason negative) controls: corrupted steps are rejected AND are genuinely
      unequal in the free band; the (C) content condition is necessary; the exact substitution matters;
      (SN) is not a free-band identity (hypothesis essential); the local identity fails in FB(4);
  C7  writes a 159x159 multiplication table of FB(3) (as a finite band) for the separate exhaustive C++ check.
"""
import sys, re, hashlib, time, os

def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

FAILS = []
def check(cond, msg):
    tag = 'PASS' if cond else 'FAIL'
    print(f'[{tag}] {msg}')
    if not cond:
        FAILS.append(msg)

# ---------------------------------------------------------------- C1: Green-Rees signature
def gr(w):
    """Canonical invariant of a nonempty word in the free band FB(A).
    Green-Rees (1952): s=t iff cont(x)=cont(y), pref(x)~pref(y), ltof(x)=ltof(y), suff(x)~suff(y), ftol(x)=ftol(y)
    (H is trivial in a band).  pref = longest prefix missing exactly one letter; ltof = the letter after it;
    suff/ftol dual.  Words of one-letter content are all equal to that letter."""
    if not w:
        raise ValueError('empty word')
    K = frozenset(w)
    if len(K) == 1:
        return w[0]
    seen = set()
    for i, ch in enumerate(w):
        seen.add(ch)
        if len(seen) == len(K):
            ltof, pref = ch, w[:i]
            break
    seen = set()
    for j in range(len(w) - 1, -1, -1):
        seen.add(w[j])
        if len(seen) == len(K):
            ftol, suff = w[j], w[j + 1:]
            break
    return (K, gr(pref), ltof, ftol, gr(suff))

def eq(u, v):
    return gr(u) == gr(v)

def free_band(letters):
    """All elements of FB(letters) by right-multiplication closure; returns {gr-key: representative word}."""
    reps = {}
    frontier = []
    for x in letters:
        reps[gr(x)] = x
        frontier.append(x)
    while frontier:
        nxt = []
        for w in frontier:
            for x in letters:
                u = w + x
                k = gr(u)
                if k not in reps:
                    reps[k] = u
                    nxt.append(u)
        frontier = nxt
    return reps

# ---------------------------------------------------------------- C3: literal parser
def square_witnesses(u, v):
    """All (i,k,W) with u = u[:i] W W u[i+2k:] and v = u[:i] W u[i+2k:]."""
    out = []
    n = len(u)
    k = n - len(v)
    if k <= 0 or 2 * k > n:
        return out
    for i in range(0, n - 2 * k + 1):
        if u[i:i + k] == u[i + k:i + 2 * k] and u[:i + k] + u[i + 2 * k:] == v:
            out.append((i, k, u[i:i + k]))
    return out

def C_witnesses(u, v):
    """All (P,X,Y,Z,Q): u = P X Y Z Q, v = P X Z Q, X,Y,Z nonempty, cont(Y) <= cont(X) = cont(Z)."""
    out = []
    n = len(u)
    m = n - len(v)          # = |Y|
    if m <= 0:
        return out
    for j in range(1, n - m):               # Y = u[j:j+m]
        if u[:j] + u[j + m:] != v:
            continue
        cY = set(u[j:j + m])
        for i in range(0, j):               # X = u[i:j]
            X = u[i:j]
            cX = set(X)
            if not cY <= cX:
                continue
            for l in range(j + m + 1, n + 1):   # Z = u[j+m:l]
                Z = u[j + m:l]
                if set(Z) == cX:
                    out.append((u[:i], X, u[j:j + m], Z, u[l:]))
    return out

def square_insert_witnesses(u, v):
    return square_witnesses(v, u)

def extract_traces(md_text):
    """Extract the four literal chains of section 4 from the author's markdown text."""
    names = ['I, left', 'I, right', 'II, left', 'II, right']
    traces = {}
    for nm in names:
        pat = re.compile(r'\*\*' + re.escape(nm) + r':\*\*\s*```text\n(.*?)```', re.S)
        m = pat.search(md_text)
        if not m:
            raise RuntimeError('trace block not found: ' + nm)
        words, marks = [], []
        for line in m.group(1).strip().split('\n'):
            mm = re.fullmatch(r'(?:→\s*)?([a-d]+)\s*(\(C\))?\s*', line.strip())
            if not mm:
                raise RuntimeError(f'unparseable trace line in {nm}: {line!r}')
            words.append(mm.group(1))
            marks.append(bool(mm.group(2)))
        traces[nm] = (words, marks)
    return traces

# ---------------------------------------------------------------- C2: own substitution
def local_pair(e, A, B, C):
    X, Y, Z = e + A + e, e + B + e, e + C + e
    L = X + Y + X + Z + X          # regular-band identity left side  xyxzx
    R = X + Y + Z + X              # right side                       xyzx
    return X, Y, Z, L, R

def main():
    if len(sys.argv) < 2:
        print('usage: reviewer-f144-exact-controls-v1.py <author-md> [--f4] [--table OUT]')
        sys.exit(2)
    md_path = sys.argv[1]
    do_f4 = '--f4' in sys.argv
    table_out = None
    if '--table' in sys.argv:
        table_out = sys.argv[sys.argv.index('--table') + 1]
    print('reviewer-f144-exact-controls-v1  start', utc())
    print('author md sha256', sha256_file(md_path), 'bytes', os.path.getsize(md_path))
    md_text = open(md_path, encoding='utf-8').read()

    # ---------------- C1 positive controls of gr()
    print('\n== C1 Green-Rees signature controls ==')
    t0 = time.time()
    f1, f2, f3 = free_band('a'), free_band('ab'), free_band('abc')
    check(len(f1) == 1, f'|FB(1)| = {len(f1)} (expected 1)')
    check(len(f2) == 6, f'|FB(2)| = {len(f2)} (expected 6)')
    check(len(f3) == 159, f'|FB(3)| = {len(f3)} (expected 159)')
    print(f'   FB(2) representatives: {sorted(f2.values(), key=lambda s:(len(s),s))}')
    if do_f4:
        t1 = time.time()
        f4 = free_band('abcd')
        check(len(f4) == 332380, f'|FB(4)| = {len(f4)} (expected 332380), {time.time()-t1:.1f}s')
    check(eq('abab', 'ab') and eq('aa', 'a') and eq('abcbabc', 'abc') and eq('abacaba', 'abaca' + 'ba'),
          'known free-band equalities abab=ab, aa=a, abcbabc=abc, abacaba=abacaba')
    check(not eq('ab', 'ba') and not eq('aba', 'ab') and not eq('abc', 'acb') and not eq('abaca', 'abacaba'),
          'known free-band inequalities ab!=ba, aba!=ab, abc!=acb, abaca!=abacaba')
    check(all(eq(w + w, w) for w in f3.values()), 'gr respects idempotency on all 159 FB(3) representatives')
    # associativity/consistency: gr(uv) depends only on gr(u), gr(v) on a sample
    reps3 = sorted(f3.values(), key=lambda s: (len(s), s))
    ok = True
    for u in reps3[:40]:
        for v in reps3[:40]:
            if gr(u + v) != gr(u + u + v) or gr(u + v) != gr(u + v + v):
                ok = False
    check(ok, 'gr(uv)=gr(uuv)=gr(uvv) on 40x40 FB(3) sample (congruence sanity)')
    print(f'   C1 time {time.time()-t0:.1f}s')

    # ---------------- C2 own substitutions vs. author chain starts
    print('\n== C2 local-regular substitutions and contexts ==')
    traces = extract_traces(md_text)
    for nm, (ws, mk) in traces.items():
        print(f'   extracted {nm}: {len(ws)} words, (C)-marked steps at {[i for i,b in enumerate(mk) if b]}')
    XI, YI, ZI, LI, RI = local_pair('c', 'a', 'b', 'da')
    XII, YII, ZII, LII, RII = local_pair('bc', 'a', 'ac', 'd')
    print(f'   I : e=c  X={XI} Y={YI} Z={ZI}  L={LI}  R={RI}')
    print(f'   II: e=bc X={XII} Y={YII} Z={ZII}  L={LII}  R={RII}')
    for X, e in ((XI, 'c'), (YI, 'c'), (ZI, 'c'), (XII, 'bc'), (YII, 'bc'), (ZII, 'bc')):
        check(X.startswith(e) and X.endswith(e) and eq(e + X + e, X), f'{X} is a literal e..e word and e{X}e = {X} in FB')
    starts = {
        'I, left':   'ab' + LI + 'da',
        'I, right':  'ab' + RI + 'da',
        'II, left':  'a' + LII + 'da',
        'II, right': 'a' + RII + 'da',
    }
    for nm, s in starts.items():
        check(traces[nm][0][0] == s, f'start of chain {nm} equals own context-built word {s}')
    check(not eq(LI, RI), 'instance I: L != R in the free band (the local hypothesis is actually used)')
    check(not eq(LII, RII), 'instance II: L != R in the free band (the local hypothesis is actually used)')

    # ---------------- C3 literal transitions
    print('\n== C3 literal transition parsing ==')
    counts = {'square': 0, 'C': 0}
    author_C = {('abcacbcdbcabcda', 'abcacbcdcabcda'): ('abcacbcd', 'b', 'cabcd'),
                ('abcacbcdcabcda', 'abcacbcdabcda'): ('abcacbcd', 'c', 'abcd')}
    for nm, (ws, mk) in traces.items():
        print(f'-- chain {nm}')
        g0 = gr(ws[0])
        for idx in range(1, len(ws)):
            u, v, isC = ws[idx - 1], ws[idx], mk[idx]
            if not isC:
                sw = square_witnesses(u, v)
                check(len(sw) >= 1, f'{nm} step {idx}: {u} -> {v} is a square deletion; witnesses {sw}')
                if sw:
                    counts['square'] += 1
            else:
                cw = C_witnesses(u, v)
                check(len(cw) >= 1, f'{nm} step {idx}: {u} -> {v} is a (C) application; witnesses {cw}')
                aX, aY, aZ = author_C[(u, v)]
                check(any(X == aX and Y == aY and Z == aZ for (_, X, Y, Z, _) in cw),
                      f'{nm} step {idx}: author factorization X={aX} Y={aY} Z={aZ} is among the witnesses')
                check(set(aY) <= set(aX) == set(aZ) == set('abcd'),
                      f'{nm} step {idx}: cont(Y)={set(aY)} <= cont(X)={set(aX)} = cont(Z)={set(aZ)}')
                check(len(square_witnesses(u, v)) == 0,
                      f'{nm} step {idx}: NOT a plain square deletion (so the (C) lemma is load-bearing here)')
                if cw:
                    counts['C'] += 1
            check(gr(v) == g0, f'{nm} step {idx}: gr unchanged (free-band equality consistent with Green-Rees)')
    check(counts == {'square': 21, 'C': 2}, f'transition counts {counts} (author states 21 squares, 2 absorptions)')

    # ---------------- C4 combination
    print('\n== C4 combination to (SN) ==')
    eI = (traces['I, left'][0][-1], traces['I, right'][0][-1])
    eII = (traces['II, left'][0][-1], traces['II, right'][0][-1])
    check(eI == ('abcacda', 'abcacbcda'), f'instance I yields abcacda = abcacbcda: ends {eI}')
    check(eII == ('abcda', 'abcacbcda'), f'instance II yields abcda = abcacbcda: ends {eII}')
    check(eI[1] == eII[1], 'common middle word abcacbcda => abcda = abcacda, i.e. (SN) with (a,b,c,d) literal')

    # ---------------- C5 direction 2 => 1
    print('\n== C5 direction 2=>1 (c := e inside eBe) ==')
    X, Y, Z = 'exe', 'eye', 'eze'
    sn_l, sn_r = X + Y + 'e' + Z + X, X + Y + 'e' + X + 'e' + Z + X    # (SN) at a=X,b=Y,c=e,d=Z
    reg_l, reg_r = X + Y + Z + X, X + Y + X + Z + X                    # xyzx , xyxzx
    def ee_only(u, target):
        # deletion-only search over 'ee'->'e'
        seen, stack = {u}, [u]
        while stack:
            w = stack.pop()
            if w == target:
                return True
            for i in range(len(w) - 1):
                if w[i] == 'e' and w[i + 1] == 'e':
                    nw = w[:i] + w[i + 1:]
                    if nw not in seen:
                        seen.add(nw); stack.append(nw)
        return False
    check(ee_only(sn_l, reg_l) and ee_only(sn_r, reg_r),
          f'(SN)[a=exe,b=eye,c=e,d=eze] = ({sn_l} , {sn_r}) reduces by ee->e only to ({reg_l} , {reg_r}) = regular identity')
    check(eq(sn_l, reg_l) and eq(sn_r, reg_r), 'same equalities confirmed by gr')

    # ---------------- C6 mutation controls
    print('\n== C6 mutation / intended-reason controls ==')
    check(not eq('abcda', 'abcacda'), '(SN) is NOT a free-band identity: abcda != abcacda in FB(4) (hypothesis essential)')
    e_, x_, y_, z_ = 'a', 'b', 'c', 'd'
    LX, LY, LZ = e_ + x_ + e_, e_ + y_ + e_, e_ + z_ + e_
    check(not eq(LX + LY + LX + LZ + LX, LX + LY + LZ + LX),
          'FB(4) is not locally regular: (aba)(aca)(aba)(ada)(aba) != (aba)(aca)(ada)(aba)')
    # corrupted square step: delete a non-square letter
    u = traces['I, left'][0][0]
    bad = u[:1] + u[2:]
    check(len(square_witnesses(u, bad)) == 0 and len(C_witnesses(u, bad)) == 0 and not eq(u, bad),
          f'corrupted step {u} -> {bad}: rejected by parser AND unequal in FB')
    # (C) with violated content condition (Z lacks d): parser rejects and words are unequal
    u2 = 'abcacbcd' + 'b' + 'cabc' + 'a'
    v2 = 'abcacbcd' + 'cabc' + 'a'
    check(len(C_witnesses(u2, v2)) == 0 and len(square_witnesses(u2, v2)) == 0 and not eq(u2, v2),
          f'(C) with cont(Z)!=cont(X): {u2} -> {v2} rejected AND unequal in FB (content condition necessary)')
    # (C) with Y not inside cont(X): X lacks d, Y=d
    u3 = 'abcacbc' + 'd' + 'cabc' + 'a'
    v3 = 'abcacbc' + 'cabc' + 'a'
    check(len(C_witnesses(u3, v3)) == 0 and not eq(u3, v3),
          f'(C) with cont(Y) not<= cont(X): {u3} -> {v3} rejected AND unequal in FB')
    # deleting a wrong single letter inside the real (C) step word
    u4 = 'abcacbcdbcabcda'
    v4 = u4[:9] + u4[10:]      # deletes the 'c' after the Y=b instead of b
    check(len(C_witnesses(u4, v4)) == 0 and len(square_witnesses(u4, v4)) == 0 and not eq(u4, v4),
          f'wrong deletion {u4} -> {v4} rejected AND unequal in FB')
    # exact substitution matters: C=d instead of C=da in instance I
    _, _, _, Lbad, Rbad = local_pair('c', 'a', 'b', 'd')
    check(not (eq('ab' + Lbad + 'da', 'abcacda') and eq('ab' + Rbad + 'da', 'abcacbcda')),
          'mutated instance I (C=d) does not reproduce the two target words')
    _, _, _, Lbad2, Rbad2 = local_pair('b', 'a', 'ac', 'd')
    check(not (eq('a' + Lbad2 + 'da', 'abcda') and eq('a' + Rbad2 + 'da', 'abcacbcda')),
          'mutated instance II (e=b) does not reproduce the two target words')
    # positive control for parser: a genuine square elsewhere is accepted
    check(len(square_witnesses('xabab', 'xab')) == 1, 'parser positive control: xabab -> xab accepted')
    check(len(C_witnesses('abcbabc', 'abcabc')) >= 1 and eq('abcbabc', 'abcabc'), 'parser positive control: abc.b.abc -> abc.abc accepted and equal')

    # ---------------- C7 FB(3) table for the C++ exhaustive check
    if table_out:
        reps = sorted(f3.values(), key=lambda s: (len(s), s))
        idx = {gr(w): i for i, w in enumerate(reps)}
        n = len(reps)
        with open(table_out, 'w') as f:
            f.write(f'{n}\n')
            f.write(' '.join(reps) + '\n')
            gens = [reps.index('a'), reps.index('b'), reps.index('c')]
            f.write(' '.join(map(str, gens)) + '\n')
            for i in range(n):
                row = [idx[gr(reps[i] + reps[j])] for j in range(n)]
                f.write(' '.join(map(str, row)) + '\n')
        print(f'   wrote FB(3) table {table_out} n={n} sha256 {sha256_file(table_out)}')

    print('\n== SUMMARY ==')
    print('FAIL count', len(FAILS))
    for m in FAILS:
        print('  FAIL:', m)
    print('end', utc())
    sys.exit(1 if FAILS else 0)

if __name__ == '__main__':
    main()
