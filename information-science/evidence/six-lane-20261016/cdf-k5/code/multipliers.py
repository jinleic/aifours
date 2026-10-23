#!/usr/bin/env python3
"""Exact multiplier analysis for cyclic (v,5,1) difference families (stdlib only).

Setting.  F = {B_1..B_n} is a (v,5,1)-CDF, n = (v-1)/20, v = 1 (mod 20).  Write [d] = {d,-d} for a difference
class.  A unit mu is a *(+-)-multiplier* of F if mu permutes the base blocks up to translation and negation:
mu*B_i = e_i*B_s(i) + t_i with e_i = +-1 and s a permutation.  This contains the usual multiplier definition
(all e_i = +1) and the ACF 2004 order-2 usage (blocks invariant under -m).  Whether mu is a (+-)-multiplier only
depends on mu modulo {+1,-1}, and a nontrivial group of them contains an element of prime order in
Q = Z_v^*/{+-1}.  So it suffices to rule out, or describe, every mu of prime order in Q:
(a) mu^2 = 1, mu != +-1;  (b) mu^2 = -1;  (c) mu of odd prime order r (wlog mu^r = 1).

Facts used (each re-checked numerically below where it is a finite statement):
  F1. No block satisfies -B = B + t (an affine involution of a 5-set has a fixed point x0 and then the pair
      {x0+d, x0-d} repeats the class [d]).  Hence for odd r no block satisfies mu^j B = -B + t, and for (b) no block
      is mu-stable at all (mu^2 = -1).
  F2. If [d] is fixed by mu (mu*d = +-d) and [d] lies in Delta(B) with B not mu-stable, then mu*B is (+-) a translate
      of another base block and [d] is covered twice.  So every mu-fixed class is covered by a mu-stable block, and
      blocks in proper mu-orbits cover no fixed class.
  F3. A mu-stable block B (mu*B = e*B + t, e = +-1) is invariant under f(x) = e*mu*x + t, a permutation of B whose
      order divides ord(e*mu); its fixed points lie in one coset of ker(e*mu - 1).
For each prime-order mu the script enumerates every stable-block type exactly (over its parameters), tabulates the
fixed classes each covers, decides whether 'free' blocks (all 10 classes non-fixed, in distinct mu-orbits) exist,
and solves the counting equations.  Output: JSON + a markdown table.
"""
import itertools
import json
import math
import random
import sys

CAP = 1000000


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def order(a, v):
    x, k = a % v, 1
    while x != 1:
        x = x * a % v
        k += 1
    return k


def cls(d, v):
    d %= v
    return min(d, v - d)


def classes(block, v):
    out = []
    for a, b in itertools.combinations(block, 2):
        c = cls(a - b, v)
        if c == 0:
            return None
        out.append(c)
    return out if len(set(out)) == len(out) else None


def kernel(m, v):
    return [x for x in range(v) if (m * x) % v == 0]


def analyse(v, mu, rng):
    H, n = (v - 1) // 2, (v - 1) // 20
    mu %= v
    sq = mu * mu % v
    res = dict(mu=mu, ord_in_units=order(mu, v))
    if sq == v - 1:
        res.update(kind="mu^2=-1", fixed_classes=0,
                   verdict="feasible counting" if n % 2 == 0 else "IMPOSSIBLE",
                   reason="no stable block (F1), no fixed class; all blocks paired so n must be even; n=%d" % n)
        return res
    if sq == 1:
        r = 2
        kp, km = kernel(mu - 1, v), kernel(mu + 1, v)
        fixed_plus = {cls(x, v) for x in kp if x}
        fixed_minus = {cls(x, v) for x in km if x}
        res.update(kind="involution", Kplus=len(kp), Kminus=len(km), Fplus=len(fixed_plus), Fminus=len(fixed_minus))
    else:
        r = res["ord_in_units"]
        kk = kernel(mu - 1, v)
        fixed_plus, fixed_minus = {cls(x, v) for x in kk if x}, set()
        res.update(kind="odd prime order %d" % r, K=len(kk), F=len(fixed_plus))
    fixed = fixed_plus | fixed_minus

    def orbit_key(c):
        return min(cls(c * pow(mu, j, v), v) for j in range(r))

    norbits = len({orbit_key(c) for c in range(1, H + 1) if c not in fixed})
    res["nonfixed_orbits"] = norbits

    # ---- free blocks: exist?  (exact obstruction: a subgroup of index m<=4 all of whose classes are fixed)
    obstruction = None
    for m in range(2, 5):
        if v % m == 0:
            sub = {cls(x, v) for x in range(m, v, m)}
            if sub <= fixed:
                obstruction = "every class of the index-%d subgroup %dZ_v is mu-fixed; any 5 points have two in one " \
                              "coset (pigeonhole), so every block covers a fixed class" % (m, m)
                break
    free_example = None
    if obstruction is None:
        for _ in range(200000):
            blk = [0] + rng.sample(range(1, v), 4)
            cl = classes(blk, v)
            if cl and not (set(cl) & fixed) and len({orbit_key(c) for c in cl}) == 10:
                free_example = sorted(blk)
                break
    res["free_blocks"] = ("NONE: " + obstruction) if obstruction else (
        "exist, e.g. %s" % free_example if free_example else "none found in 200000 samples (not a proof)")

    # ---- stable block types, enumerated exactly over their parameters
    types = {}
    enum_modes = {}

    def record(name, blk):
        cl = classes(blk, v)
        if cl is None:
            return
        fp = sum(1 for c in cl if c in fixed_plus)
        fm = sum(1 for c in cl if c in fixed_minus)
        nf = [c for c in cl if c not in fixed]
        keys = [orbit_key(c) for c in nf]
        if len(set(keys)) * r != len(nf):     # non-fixed classes must form whole, distinct orbits
            return
        types.setdefault((name, fp, fm, len(set(keys))), blk)

    signs = (1, -1) if r == 2 else (1,)
    for e in signs:
        em = (e * mu) % v
        ker = [x for x in kernel(em - 1, v) if x]
        tag = "mu" if e == 1 else "-mu"
        if r == 2:
            # one fixed point (at 0) + two 2-cycles {d, em*d}; exhaustive if <= CAP parameter pairs, else sampled
            moving = [d for d in range(1, v) if (em * d) % v != d]
            if len(moving) * (len(moving) - 1) // 2 <= CAP:
                pairs = itertools.combinations(moving, 2)
                mode1 = "exhaustive"
            else:
                pairs = ((rng.choice(moving), rng.choice(moving)) for _ in range(CAP))
                mode1 = "sampled %d" % CAP
            for d1, d2 in pairs:
                record("%s:1fix" % tag, [0, d1, em * d1 % v, d2, em * d2 % v])
            # three fixed points 0,e1,e2 in ker + one 2-cycle
            if len(ker) * (len(ker) - 1) // 2 * len(moving) <= CAP:
                trip = ((e1, e2, d) for e1, e2 in itertools.combinations(ker, 2) for d in moving)
                mode3 = "exhaustive"
            else:
                trip = ((rng.choice(ker), rng.choice(ker), rng.choice(moving)) for _ in range(CAP)) if len(ker) >= 2 \
                    else iter(())
                mode3 = "sampled %d" % CAP
            for e1, e2, d in trip:
                if e1 != e2:
                    record("%s:3fix" % tag, [0, e1, e2, d, em * d % v])
            enum_modes["%s:1fix" % tag] = mode1
            enum_modes["%s:3fix" % tag] = mode3
        if r == 3:
            for e1 in ker:
                for d in range(1, v):
                    if (em * d) % v != d:
                        record("%s:2fix+3cycle" % tag, [0, e1, d, em * d % v, em * em * d % v])
        if r == 5:
            # 5-cycle of f(x) = mu*x + t; translation-normalise t over Z_v/(mu-1)Z_v
            img = sorted({((em - 1) * s) % v for s in range(v)})
            reps, seen = [], set()
            for t in range(v):
                key = min(((t + y) % v) for y in img)
                if key not in seen:
                    seen.add(key)
                    reps.append(t)
            for t in reps:
                for x in range(v):
                    blk, y = [], x
                    for _ in range(5):
                        blk.append(y)
                        y = (em * y + t) % v
                    if y == x and len(set(blk)) == 5:
                        record("%s:5cycle" % tag, blk)
        # all five points fixed: a 5-subset of a coset of ker(em-1) with 10 distinct classes
        if len(ker) + 1 >= 21:
            kset = [0] + ker
            ex = None
            for _ in range(200000):
                blk = rng.sample(kset, 5)
                if classes(blk, v):
                    ex = blk
                    break
            if ex:
                record("%s:5fix" % tag, ex)
    res["enumeration"] = enum_modes
    res["stable_types"] = [dict(type=k[0], fixed_plus=k[1], fixed_minus=k[2], orbits=k[3], example=sorted(b))
                           for k, b in sorted(types.items())]

    # ---- counting equations: sum a_T*(fp,fm) = (F+,F-), sum a_T*orbits + 10c = norbits, sum a_T + r c = n
    Fp, Fm = len(fixed_plus), len(fixed_minus)
    tl = sorted({(k[1], k[2], k[3]) for k in types})
    sols = []
    free_ok = obstruction is None and free_example is not None

    def rec(i, a, fp, fm, orb, cnt):
        if fp > Fp or fm > Fm or cnt > n:
            return
        if i == len(tl):
            if fp == Fp and fm == Fm:
                rest_orbits, rest_blocks = norbits - orb, n - cnt
                if rest_orbits >= 0 and rest_orbits % 10 == 0:
                    c = rest_orbits // 10
                    if rest_blocks == r * c and (c == 0 or free_ok):
                        sols.append(dict(stable=dict(zip(["%d/%d/%d" % t for t in tl], a)), free_orbits=c))
            return
        t = tl[i]
        for k in range(0, n + 1):
            rec(i + 1, a + [k], fp + k * t[0], fm + k * t[1], orb + k * t[2], cnt + k)
            if t[0] == 0 and t[1] == 0 and k * 10 > norbits:
                break
            if fp + k * t[0] > Fp or fm + k * t[1] > Fm:
                break

    rec(0, [], 0, 0, 0, 0)
    res["counting_solutions"] = len(sols)
    res["counting_examples"] = sols[:6]
    res["verdict"] = "feasible counting" if sols else "IMPOSSIBLE"
    if not sols:
        res["reason"] = "no nonnegative solution of the fixed-class counting equations with the enumerated types" + (
            "; free blocks impossible" if obstruction else "")
    return res


def class_order(a, v):
    """smallest j >= 1 with a^j = +-1 (mod v): the order of a in Q = Z_v^*/{+-1}"""
    j, x = 1, a % v
    while x not in (1, v - 1):
        x = x * a % v
        j += 1
    return j


def is_prime(j):
    return j >= 2 and all(j % p for p in range(2, int(j ** 0.5) + 1))


def prime_order_reps(v):
    """one representative mu per subgroup of prime order of Q; for odd order the representative has mu^r = 1"""
    reps, seen = [], set()
    for a in range(2, v - 1):
        if math.gcd(a, v) != 1:
            continue
        j = class_order(a, v)
        if not is_prime(j):
            continue
        if j > 2 and pow(a, j, v) != 1:
            continue
        sub = frozenset(min(pow(a, i, v), v - pow(a, i, v)) for i in range(1, j + 1))
        if sub in seen:
            continue
        seen.add(sub)
        reps.append(a)
    return reps


def main(argv):
    out_path = None
    args = []
    i = 1
    while i < len(argv):
        if argv[i] == "--out":
            out_path = argv[i + 1]
            i += 2
        else:
            args.append(int(argv[i]))
            i += 1
    vs = args or [321, 501, 621, 681, 801, 901]
    rng = random.Random(20261016)
    out = []
    for v in vs:
        row = dict(v=v, n=(v - 1) // 20, factorization={str(p): e for p, e in factor(v).items()},
                   phi=sum(1 for a in range(1, v) if math.gcd(a, v) == 1))
        reps = prime_order_reps(v)
        row["prime_order_class_multipliers"] = [dict(mu=m, class_order=class_order(m, v)) for m in reps]
        row["analyses"] = [analyse(v, mu, rng) for mu in reps]
        out.append(row)
        print("v=%d n=%d factors=%s reps=%s" % (v, row["n"], row["factorization"],
                                                [(m, class_order(m, v)) for m in reps]))
        for a in row["analyses"]:
            print("  mu=%d kind=%s verdict=%s free=%s" % (a["mu"], a["kind"], a["verdict"],
                                                         a.get("free_blocks", "-")[:100]))
            for t in a.get("stable_types", []):
                print("     type", t)
            if a.get("counting_examples"):
                print("     solutions=%d e.g. %s" % (a["counting_solutions"], a["counting_examples"][:3]))
            if a.get("reason"):
                print("     reason:", a["reason"])
        sys.stdout.flush()
    if out_path:
        with open(out_path, "w") as fh:
            json.dump(out, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
