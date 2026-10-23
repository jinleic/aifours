"""Replay of the new written kills of c2/proof-R4-closure.md (Lemma ZP, Lemma C, Lemma R4) and of Lemma KL's
arithmetic.  Research aid [F].
* census part: every configuration line of a census dump (SOL lines with d=, phi=) is tested with Lemma ZP and
  Lemma C where applicable; the produced KL prefix must satisfy x(P) in [-L_P, U_P] (Lemma H windows, integer
  containment) -- this is the exact kill.
* synthetic part: random integer data (d, phi) on normalized MIX_low run data that satisfy the HYPOTHESES of
  Lemma C, resp. of the Lemma R4 dichotomy (all phi <= g-1, all bh <= s, delta+ >= 2s - B, heavier Y-class
  BH >= s+1) but are NOT required to be interval-feasible: the lemmas' conclusions are pure arithmetic, so
  every produced prefix must satisfy integer window containment.
* mutation: the same with every window shrunk by one at both ends must FAIL in a positive number of cases.
Usage: python3 r4_replay.py DUMP p SEED NSYN
"""
import sys, re, json, random, collections
import rstar


def window(P, d, p, g, B, D, mut=0):
    k = len(d)
    m = rstar.blocks(P, k)
    DP = sum(d[t] for t in P)
    return -(rstar.Gm(m, D - DP, p, g, B) - mut), rstar.Gm(m, DP, p, g, B) - mut


def KL(S, d, phi, p, g, B, mut=0):
    """Lemma KL: returns (hypotheses_ok, prefix_in_window)."""
    k = len(d); D = sum(d); bh = [x - 2 * y for x, y in zip(d, phi)]
    S = set(S)
    if not S or len(S) == k or any(phi[t] > g - 1 for t in S):
        return False, None
    if sum(phi[t] for t in S) + rstar.blocks(S, k) < g + 1 or sum(bh[t] for t in S) > B:
        return False, None
    order = [t for t in sorted(S) if bh[t] <= 0] + [t for t in sorted(S) if bh[t] > 0]
    Q = set()
    for t in order:
        Q.add(t)
        c = sum(phi[u] for u in Q) + rstar.blocks(Q, k)
        if c >= g + 1:
            if c > 2 * g:
                return False, None
            lo, hi = window(Q, d, p, g, B, D, mut)
            xP = sum(d[u] - phi[u] for u in Q)
            return True, (lo <= xP <= hi)
    return False, None


def zp(d, phi, p, g, B, mut=0):
    k = len(d); bh = [x - 2 * y for x, y in zip(d, phi)]
    Zp = [t for t in range(k) if bh[t] <= 0 and phi[t] >= 0]
    if not Zp or len(Zp) == k or sum(phi[t] for t in Zp) + rstar.blocks(set(Zp), k) < g + 1:
        return None
    return KL(Zp, d, phi, p, g, B, mut)


def lc(d, phi, p, g, B, mut=0):
    k = len(d); bh = [x - 2 * y for x, y in zip(d, phi)]; s = k - 1 - 2 * g - B
    for t0 in range(k):
        if bh[t0] >= s + 1 and phi[t0] <= p - k + g and all(phi[t] <= g - 1 for t in range(k) if t != t0):
            return KL([t for t in range(k) if t != t0], d, phi, p, g, B, mut)
    return None


def r4(d, phi, p, g, B, mut=0):
    k = len(d); s = k - 1 - 2 * g - B; bh = [x - 2 * y for x, y in zip(d, phi)]
    if max(phi) > g - 1 or max(bh) > s:
        return None
    Z0 = [t for t in range(k) if bh[t] <= 0]
    if not Z0:
        return None
    Zp = [t for t in Z0 if phi[t] >= 0]
    dplus = -sum(bh[t] for t in Zp)
    if dplus < 2 * s - B:
        return None
    Y = set(range(k)) - set(Z0)
    start = Z0[0]; Q = []; j = 1
    while j <= k:
        t = (start + j) % k
        if t not in Y:
            j += 1; continue
        path = []
        while j <= k and (start + j) % k in Y:
            path.append((start + j) % k); j += 1
        odd, even = path[0::2], path[1::2]
        Q += odd if sum(bh[u] for u in odd) >= sum(bh[u] for u in even) else even
    if sum(bh[u] for u in Q) < s + 1:
        return None
    N = []
    for u in Q:
        N.append(u)
        if sum(bh[v] for v in N) >= s + 1:
            break
    if sum(phi[v] for v in N) <= p - k + g - 1 + len(N):
        S = [t for t in range(k) if t not in N]
    else:
        S = Zp + N
    return KL(S, d, phi, p, g, B, mut)


def random_d(p, k, g, B, rng):
    D = 2 * p - k + 2 * g; A = D + B
    if A > 2 * p - 1:
        return None
    for _ in range(200):
        nP = rng.randrange(0, min(B, k - 1) + 1)
        Banti = B - nP
        nAnti = 0 if Banti == 0 else rng.randrange(1, min(Banti, k - nP - 1) + 1)
        nAl = k - nP - nAnti; Aal = A - nP
        if nAl < 1 or Aal < nAl or (Banti > 0 and nAnti == 0) or Banti < nAnti:
            continue
        def comp(total, parts):
            cuts = sorted(rng.sample(range(1, total), parts - 1)) if parts > 1 else []
            b = [0] + cuts + [total]
            return [b[i + 1] - b[i] for i in range(parts)]
        d = comp(Aal, nAl) + [0] * nP + [-c for c in (comp(Banti, nAnti) if nAnti else [])]
        rng.shuffle(d)
        prm = rstar.params(d, p)
        if prm is None or prm[4] != g:
            continue
        return d
    return None


def synth(p, rng, force_big):
    for _ in range(200):
        k = rng.randrange(6, p + 1); g = rng.randrange(1, (k - 2) // 2 + 1)
        Bmax = k - 1 - 2 * g
        if Bmax < 1:
            continue
        B = rng.randrange(1, Bmax + 1); s = k - 1 - 2 * g - B
        d = random_d(p, k, g, B, rng)
        if d is None:
            continue
        lo = [x - 2 * g + 2 for x in d]
        t0 = rng.randrange(k)
        hi = [None] * k
        bh = []
        for t, x in enumerate(d):
            l = lo[t]
            if force_big and t == t0:
                l = max(l, s + 1)
            l += (l - x) % 2
            h = l + 4 if force_big else s - ((s - x) % 2)
            if h < l:
                bh = None; break
            hi[t] = h
            bh.append(rng.randrange(l, h + 1, 2))
        if bh is None:
            continue
        target = k - 2 * g
        if (sum(bh) - target) % 2:
            continue
        for _ in range(400):
            diff = sum(bh) - target
            if diff == 0:
                break
            t = rng.randrange(k)
            lt = max(lo[t], s + 1) if (force_big and t == t0) else lo[t]
            lt += (lt - d[t]) % 2
            if diff > 0 and bh[t] - 2 >= lt:
                bh[t] -= 2
            elif diff < 0 and (force_big or bh[t] + 2 <= hi[t]):
                bh[t] += 2
        if sum(bh) != target:
            continue
        phi = [(x - b) // 2 for x, b in zip(d, bh)]
        if max(phi) > g - 1:
            continue
        return d, phi, g, B
    return None


def main():
    dump, p, seed, nsyn = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    out = {"dump": dump, "p": p, "seed": seed}
    cz = collections.Counter(); cc = collections.Counter()
    for line in open(dump):
        if not line.startswith("SOL"):
            continue
        g = int(re.search(r" g=(\d+)", line).group(1)); B = int(re.search(r" B=(\d+)", line).group(1))
        d = [int(x) for x in re.search(r" d=([-\d,]+)", line).group(1).split(",")]
        phi = [int(x) for x in re.search(r" phi=([-\d,]+)", line).group(1).split(",")]
        r = zp(d, phi, p, g, B); cz[str(r)] += 1
        r = lc(d, phi, p, g, B); cc[str(r)] += 1
    out["census_ZP"] = dict(cz); out["census_C"] = dict(cc)
    rng = random.Random(seed)
    syn = collections.Counter()
    for pp in (11, 13, 17, 19, 23, 29, 31, 37):
        for _ in range(nsyn):
            for kind, fb in (("C", True), ("R4", False)):
                res = synth(pp, rng, fb)
                if res is None:
                    syn[(kind, "nogen")] += 1; continue
                d, phi, g, B = res
                f = lc if kind == "C" else r4
                r0 = f(d, phi, pp, g, B, 0); r1 = f(d, phi, pp, g, B, 1)
                syn[(kind, "applicable" if r0 is not None else "n/a")] += 1
                if r0 is not None:
                    syn[(kind, "hyp_ok_and_in_window" if r0 == (True, True) else "FAIL:" + str(r0))] += 1
                    syn[(kind, "mutation_rejected" if r1 != (True, True) else "mutation_accepted")] += 1
    out["synthetic"] = {f"{a}:{b}": v for (a, b), v in sorted(syn.items())}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
