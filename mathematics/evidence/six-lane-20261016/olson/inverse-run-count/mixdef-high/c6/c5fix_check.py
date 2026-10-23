#!/usr/bin/env python3
"""c5fix_check.py -- [F] check for the c5 review fix S10 (c6, task OlsonRunCount5).  Independent re-implementation of the
mutation control D2 of c5/seeds.py: for every prime 11 <= p <= 61 and every kB with 3kB >= p + 5, kB <= p - 4 (W(p, kB), B = 1),
replace the lower end a = 3 - ceil(delta/2) of the pair seed by a - w and find the least w for which a 2-run step of Lemma SCW
(c5/proof-SEED-r2.md Sec. 3, Case s = 2, condition (A^s)) fails: aligned pair 2(a - w) >= U(2, m) + 1 - p, anti pair
-kB + (a - w) >= U(0, m) + 1 - p, m in {1, 2}.  Claim of the review (hand): least w = 3 iff delta is odd, else 4."""
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def cdiv(a, b): return -((-a) // b)
cases = agree = 0; bad = []
for p in [q for q in range(11, 62) if isprime(q)]:
    for kB in range(1, p - 3):
        if 3 * kB < p + 5: continue
        d = p - kB
        lamc = lambda y, m: min(p - m + 1, p - 1 - y + m, (p + kB - y) // 2 + 1)
        U = lambda y, m: p - lamc(y, m)
        a = 3 - cdiv(d, 2)
        least = None
        for w in range(0, 3 * p):
            aw = a - w
            fail = any(2 * aw < U(2, m) + 1 - p for m in (1, 2)) or any(-kB + aw < U(0, m) + 1 - p for m in (1, 2))
            if fail: least = w; break
        cases += 1
        pred = 3 if d % 2 else 4
        if least == pred: agree += 1
        else: bad.append((p, kB, d, least))
print({'cases': cases, 'least_w_equals_3_if_delta_odd_else_4': agree, 'disagree': bad[:10]})
