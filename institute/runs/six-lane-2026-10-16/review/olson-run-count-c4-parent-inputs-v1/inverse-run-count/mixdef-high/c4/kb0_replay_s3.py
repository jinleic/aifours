# kb0_replay_s3.py -- c4 (T2): targeted replay of the Step-3 branch of c4/proof-KB0.md (Z a cyclic interval through the
# anti run with |Z| >= 3, c(Z) = K - 1, every aligned run outside Z has x = 1), which random vectors rarely reach.
# For each p = 1 (mod 6) in 13..61 and every interval Z = {-a, ..., 0, ..., b} (a + b >= 2, a + b <= K - 1) and every
# split of c(Z) = K - 1 with c_t >= 1 on aligned members, c_0 >= 0 (enumerated with a cap), the proof's pattern
# Q = Z u {s} (s the first aligned run adjacent to no run of Z) must be certified (2 <= |Q| <= K + 1, not an anti pair)
# and satisfy X_Q < lambda(Q); also asserts the singleton bounds and sum x = p.  lambda from explicit blocks.
# Usage: python3 -B kb0_replay_s3.py CAP
import sys, itertools
CAP = int(sys.argv[1])
tot = 0; fails = 0
for p in (13, 19, 31, 37, 43, 61):
    K = (p + 5) // 3; n = p + K; k = n + 1
    d = [-1] + [1] * n
    def blocks(Q): return sum(1 for t in Q if (t - 1) % k not in Q)
    def lam(Q):
        m = blocks(Q); D = sum(d[t] for t in Q); return min(p - m + 1, D + m - K, (D + 1) // 2 + 1)
    full = set(range(k))
    lo = [lam({t}) for t in range(k)]; hi = [p - lam(full - {t}) for t in range(k)]
    cnt = 0
    for a in range(0, K):
        for b in range(0, K):
            if a + b < 2 or a + b > K - 1: continue
            Z = [(-i) % k for i in range(a, 0, -1)] + [0] + list(range(1, b + 1))
            al = [t for t in Z if t]
            # c_t >= 1 on aligned members, c_0 >= 0, total K - 1, all c_t <= K - 1 and within singleton bounds
            rest = K - 1 - len(al)
            if rest < 0: continue
            for c0 in range(0, rest + 1):
                extra = rest - c0
                # distribute 'extra' over aligned members (first CAP compositions)
                for comp in itertools.islice((cc for cc in itertools.product(range(extra + 1), repeat=len(al)) if sum(cc) == extra), CAP):
                    x = [1] * k
                    x[0] = -1 - c0
                    for t, e in zip(al, comp): x[t] = 1 - (1 + e)
                    if any(not (lo[t] <= x[t] <= hi[t]) for t in range(k)): continue
                    if sum(x) != p: continue
                    Zs = set(Z)
                    s = [t for t in range(1, k) if t not in Zs and all((t - z) % k not in (1, k - 1) for z in Zs)][0]
                    Q = Zs | {s}
                    certified = 2 <= len(Q) <= K + 1 and not (len(Q) == 2 and 0 in Q)
                    ok = certified and sum(x[t] for t in Q) < lam(Q)
                    tot += 1; cnt += 1
                    if not ok:
                        fails += 1
                        if fails < 5: print('FAIL', p, Z, x[:8])
    print({'p': p, 'K': K, 'step3_vectors': cnt}, flush=True)
print({'total': tot, 'failures': fails})
