#!/usr/bin/env python3
"""indstar_classes.py -- [F] (c5 README Sec. 7): complete lists of the all-singleton item-(iii) classes (p, k, B) that the
hypotheses of Theorem IND* (c4/proof-INDstar-r1.md) do NOT cover, primes 11..43, split by B = 1 (now closed by
c5/proof-SEED-r2.md + c3/proof-WALL.md) and B >= 2.  The coverage test is c4/ind_star3.py's own functions (arcs, lift_range,
check, covered; lines 25-65 of that frozen file, exec'ed read-only), so this only re-prints c4's Part A without truncation;
the per-p totals must equal those of c4/out/ind_star3.txt (checked below against the printed 'classes'/'covered' numbers)."""
import re, sys
src = open('../c4/ind_star3.py').read().splitlines()
g = {}
exec('\n'.join(src[24:65]), g)          # lines 25..65: isprime, fl, arcs, lift_range, check, covered
ref = {}
for line in open('../c4/out/ind_star3.txt'):
    m = re.match(r'p=(\d+) classes (\d+) covered (\d+)', line)
    if m and int(m.group(1)) not in ref: ref[int(m.group(1))] = (int(m.group(2)), int(m.group(3)))
allok = True
for p in range(11, 44):
    if not g['isprime'](p): continue
    cls = [(k, B) for k in range(p + 2, 2 * p - 2) for B in range(1, k - p)]
    unc = [(k, B, k - p - B) for (k, B) in cls if not g['covered'](p, k, B)]
    ok = ref.get(p) == (len(cls), len(cls) - len(unc)); allok &= ok
    u1 = [c for c in unc if c[1] == 1]; u2 = [c for c in unc if c[1] >= 2]
    print('p=%d classes %d covered %d (c4 receipt agrees: %s) | uncovered B=1: %d | uncovered B>=2: %d %s' % (p, len(cls), len(cls) - len(unc), ok, len(u1), len(u2), u2))
print('all per-p totals agree with c4/out/ind_star3.txt:', allok)
