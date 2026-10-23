# hcheck.py -- c3 README Sec. 8: independent re-check of hypothesis (H) on words dumped by map3.cpp.
# Written independently of cert.cpp/census3.cpp/map3.cpp: lambda from an explicit block decomposition, certification
# by a dictionary DP over subsets in order of size, pin test over all proper Q.  Words with k > KMAX are skipped.
# Mutation control (MUT=1): condition (B) demanded with p + 2 instead of p + 1 (must change some verdicts).
# Usage: python3 hcheck.py dumpfile KMAX MUT
import sys, json, itertools
fn, KMAX, MUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
def analyse(p, kB, B, d):
    k = len(d)
    def nblocks(S):
        if not S: return 0
        return sum(1 for t in S if (t - 1) % k not in S)
    lam = {}
    def L(S):
        if S in lam: return lam[S]
        m = nblocks(S); D = sum(d[t] for t in S)
        v = min(p - m + 1, D + m - kB, (D + B) // 2 + 1)
        lam[S] = v; return v
    full = frozenset(range(k))
    cert = set()
    for t in range(k): cert.add(frozenset([t]))
    allc = True
    for size in range(2, k):
        for comb in itertools.combinations(range(k), size):
            Q = frozenset(comb); ok = False
            for t in comb:
                Qp = Q - {t}
                if Qp not in cert: continue
                T = frozenset([t])
                if L(Qp) + L(T) + L(full - Q) >= 1 and L(Q) + L(full - Qp) + L(full - T) >= p + 1 + MUT:
                    ok = True; break
            if ok: cert.add(Q)
            else: allc = False
    pin = any((Q in cert) and ((full - Q) in cert) and L(Q) + L(full - Q) >= 1 for Q in cert)
    return allc, pin
n = agree = skipped = 0; dis = []
for line in open(fn):
    if '"dump"' not in line: continue
    w = json.loads(line)
    if len(w['d']) > KMAX: skipped += 1; continue
    allc, pin = analyse(w['p'], w['kB'], w['B'], w['d'])
    n += 1
    if (allc, pin) == (bool(w['allcert']), bool(w['pin'])): agree += 1
    elif len(dis) < 5: dis.append((w['d'], w['B'], w['kB'], (allc, pin), (w['allcert'], w['pin'])))
print({'file': fn, 'MUT': MUT, 'checked': n, 'agree': agree, 'disagree': n - agree, 'skipped_k_gt': skipped, 'examples': dis})
