#!/usr/bin/env python3
"""Reviewer-owned bounded exact control for wave f270-nl242-uv-caller-coupling-necessary.

Python standard library only; integer/Fraction arithmetic only (perf_counter is used
solely for wall-clock reporting, never in the mathematics); no author code; no network.
All objects are SYNTHETIC balanced Boolean functions on F2^9 or GENERIC finite sets
(4-point blocks on F2^2, 16-subsets of F2^6 via exact character formula validated by
brute force on the smaller F2^4/k=4 analogue). The target object is never constructed.

Finite identities checked (never universal claims, never the target):
  A. caller split identities, Lemma 1, Parseval split, orthogonality, XOR/balance
     parity structure on seeded synthetic balanced f with T!=0;
  B. generic subset-XOR statistics (validates the "63/64" generic-16-set remark);
  C. four-point block taxonomy finite identities (spike/quartet, class-forced delta,
     even-count cancellation, A1 gap structure);
  D. generic 64-block class-profile system: W_s odd exactly on D, the mod-4 identity,
     flatness iff (N1)+(VB) in positive and two intended-negative configurations,
     Omega XOR decomposition (28-pair cancellation, N2 non-vacuity).
"""
import itertools, json, hashlib, os, random, subprocess, sys, time
from fractions import Fraction

T0 = time.perf_counter()
results = []
def check(name, ok, note=""):
    results.append({"check": name, "status": "PASS" if ok else "FAIL", "note": note})
    if not ok:
        print("FAIL:", name, note)
    return ok

def pc(x):  # popcount
    return bin(x).count("1")
def dot(a, x):
    return (pc(a & x) & 1)

# ---------------- Section A: synthetic balanced Boolean functions on F2^9 ----------------
rng = random.Random(20261029)
def synth_balanced_with_T(rng):
    supp = set(rng.sample(range(512), 256))
    T = 0
    for x in supp: T ^= x
    if T == 0: return None
    s = [1]*512
    for x in supp: s[x] = -1
    return supp, T, s

def section_A():
    got = []
    tries = 0
    while len(got) < 8 and tries < 4000:
        tries += 1
        r = synth_balanged = synth_balanced_with_T(rng)
        if r is None: continue
        got.append(r)
    okA = len(got) == 8
    seen_m_mod4 = set()
    for idx, (supp, T, s) in enumerate(got):
        a0 = next(a for a in range(1, 512) if dot(a, T) == 1)
        V = [y for y in range(512) if dot(a0, y) == 0]
        u = {y: (s[y] + s[y ^ T]) // 2 for y in V}
        v = {y: (s[y] - s[y ^ T]) // 2 for y in V}
        m = sum(1 for y in V if u[y] != 0)
        seen_m_mod4.add(m % 4)
        # basic split facts
        ok = all(u[y]*v[y] == 0 and u[y]**2 + v[y]**2 == 1 for y in V)
        ok &= all(s[y] == u[y] + v[y] and s[y ^ T] == u[y] - v[y] for y in V)
        ok &= sum(u.values()) == 0
        ok &= (m + sum(1 for y in V if v[y] != 0)) == 256
        check(f"A{idx}.split-facts", ok)
        # full Walsh transform, direct
        Wf = [sum(s[x] * (1 if dot(a, x) == 0 else -1) for x in range(512)) for a in range(512)]
        K = [a for a in range(512) if dot(a, T) == 0]
        ok = len(K) == 256 and set(K) | set(a ^ a0 for a in K) == set(range(512)) \
             and not (set(K) & set(a ^ a0 for a in K))
        check(f"A{idx}.K-coset-partition", ok)
        Uhat = {r: sum(u[y] * (1 if dot(r, y) == 0 else -1) for y in V) for r in K}
        Vhat = {r: sum(v[y] * (1 if dot(r, y) == 0 else -1) for r in K)} if False else \
               {r: sum(v[y] * (1 if dot(r, y) == 0 else -1) for y in V) for r in K}
        ok = all(Wf[r] == 2*Uhat[r] and Wf[r ^ a0] == 2*Vhat[r] for r in K)
        check(f"A{idx}.caller-split", ok)
        ok = all(Wf[a] % 4 == 0 for a in range(512))
        check(f"A{idx}.lemma1-global-mod4", ok)
        sk = sum(Wf[r]**2 for r in K); so = sum(Wf[r ^ a0]**2 for r in K)
        check(f"A{idx}.parseval-split", sk == 1024*m and so == 1024*(256-m)
              and sk + so == 2**18, f"m={m}")
        check(f"A{idx}.fourier-orthogonal-halves",
              sum(Uhat[r]*Vhat[r] for r in K) == 256 * sum(u[y]*v[y] for y in V) == 0)
        # Theorem 2 structure
        q = sum(1 for y in V if s[y ^ T] == -1)        # #{y in V: f(y+T)=1}
        p = sum(1 for y in V if v[y] == 1)
        numin = sum(1 for y in V if u[y] == -1)
        numip = sum(1 for y in V if u[y] == 1)
        ok = (numin == numip == m // 2) and (q == p + numin)
        check(f"A{idx}.count-identity q = p + count(u=-1)", ok, f"m={m},p={p},q={q}")
        xorv = 0
        for y in V:
            if v[y] != 0: xorv ^= y
        check(f"A{idx}.T2-conclusion", q % 2 == 1 and xorv == 0
              and (p % 2) == ((1 + (m // 2)) % 2), f"m%4={m%4},p%2={p%2}")
        check(f"A{idx}.Wf(a0)-identity", Wf[a0] == 2*(2*p - (256 - m)))
    check("A.coverage-both-m-parities", 0 in seen_m_mod4 and 2 in seen_m_mod4,
          f"observed m%4 values: {sorted(seen_m_mod4)}")
    return

# ---------------- Section B: generic subset-XOR statistics ----------------
def xorcount_formula(n, k):
    # #{k-subsets of F2^n with XOR = x}:  x=0: (C(2^n,k)+(2^n-1)*[t^k](1-t^2)^{2^(n-1)})/2^n
    # x!=0: (C(2^n,k)-[t^k](1-t^2)^{2^(n-1)})/2^n ;  [t^k](1-t^2)^{N} nonzero iff k even.
    from math import comb
    N = 2**n; H = 2**(n-1)
    tot = comb(N, k)
    inner = comb(H, k//2) if k % 2 == 0 else 0   # (-1)^{k/2} * C(H, k/2), sign irrelevant here
    return tot, inner, (tot + (N-1)*inner)//N, (tot - inner)//N

def section_B():
    # brute-force validation of the character formula on F2^4, k=4
    cnt = {}
    for D in itertools.combinations(range(16), 4):
        x = 0
        for c in D: x ^= c
        cnt[x] = cnt.get(x, 0) + 1
    tot, inner, N0, Nx = xorcount_formula(4, 4)
    ok = (cnt.get(0, 0) == N0 and all(cnt.get(x, 0) == Nx for x in range(1, 16))
          and N0 + 15*Nx == tot)
    check("B.brute-force-F2^4-k=4-validates-formula", ok,
          f"N0={N0},Nx={Nx},tot={tot},inner={inner}")
    # generic 16-set statistics on F2^6, k=16, exact integers + Fraction
    tot, inner, N0, Nx = xorcount_formula(6, 16)
    ok = (N0 + 63*Nx == tot) and ((tot + 63*inner) % 64 == 0) and ((tot - inner) % 64 == 0)
    check("B.F2^6-k=16-exact-counts", ok, f"C(64,16)={tot},C(32,8)={inner},N0={N0},Nx={Nx}")
    P0 = Fraction(N0, tot)
    fail = 1 - P0
    delta = fail - Fraction(63, 64)
    check("B.63/64-generic-remark-essentially-exact",
          abs(delta) < Fraction(1, 10**7) and abs(delta) > 0,
          f"P(XOR=0)={float(P0):.12f}, P(fail)-63/64={delta} (exact) ~ {float(delta):.3e}")
    return

# ---------------- Section C: four-point block finite identities on F2^2 ----------------
def chi(s, z):
    return 1 if dot(s, z) == 0 else -1

def section_C():
    # (a) all 16 sign vectors: evenness, energy 16, spike/quartet dichotomy
    oka = True
    for eta in itertools.product((1, -1), repeat=4):
        W = [sum(eta[z]*chi(s, z) for z in range(4)) for s in range(4)]
        oka &= all(w % 2 == 0 for w in W) and sum(w*w for w in W) == 16
        oka &= sorted(abs(w) for w in W) in ([0, 0, 0, 4], [2, 2, 2, 2])
    check("C.a-O-block-spike-or-quartet", oka)
    # (b) 2-point supports: |U_s|=2 exactly on {s: chi_s(z1^z2)=eta1*eta2}
    okb = True
    for z1 in range(4):
        for z2 in range(4):
            if z1 == z2: continue
            for e1 in (1, -1):
                for e2 in (1, -1):
                    U = [e1*chi(s, z1) + e2*chi(s, z2) for s in range(4)]
                    okb &= all(abs(u) in (0, 2) for u in U)
                    okb &= all((abs(U[s]) == 2) == (chi(s, z1 ^ z2) == e1*e2) for s in range(4))
    check("C.b-class-forced-delta-fibre-pair", okb)
    # (c) annihilator pairs <-> three distinct nonzero deltas; v-option pairs
    pairs = {frozenset((0, 2)): None, frozenset((0, 3)): None, frozenset((0, 1)): None}
    for d in (1, 2, 3):
        ann = frozenset(s for s in range(4) if chi(s, d) == 1)
        if ann in pairs: pairs[ann] = d
    okc = len(set(pairs.values())) == 3 and None not in pairs.values()
    okc &= pairs[frozenset((0, 2))] != pairs[frozenset((0, 3))] != pairs[frozenset((0, 1))]
    opts = {"C2": ({0, 2}, {1, 3}), "C3": ({0, 3}, {1, 2}), "D1": ({0, 1}, {2, 3})}
    for name, (pa, pb) in opts.items():
        d = pairs[frozenset(pa)]
        okc &= ({s for s in range(4) if chi(s, d) == 1} == set(pa)
                and {s for s in range(4) if chi(s, d) == -1} == set(pb))
    check("C.c-annihilator-pairs-distinct-delta-and-v-options", okc, f"deltas={ {k: v for k, v in pairs.items()} }")
    # (d) even-count XOR cancellation 4, 6, 18
    def fold(d, n):
        x = 0
        for _ in range(n): x ^= d
        return x
    check("C.d-even-count-cancellation-4-6-18", all(fold(d, n) == 0 for d in (1, 2, 3) for n in (4, 6, 18)))
    # (e) A1 gap structure: peak magnitude 3 at peaking character, 1 elsewhere; W_s odd
    oke = True
    for z0 in range(4):
        for s1 in (1, 2, 3):
            for eps in (1, -1):
                for dc in (1, -1):
                    uu = [eps*chi(s1, z) if z != z0 else 0 for z in range(4)]
                    U = [sum(uu[z]*chi(s, z) for z in range(4)) for s in range(4)]
                    oke &= U[s1] == 3*eps and all(abs(U[s]) == 1 for s in range(4) if s != s1)
                    W = [dc*chi(s, z0) for s in range(4)]
                    oke &= all(abs(w) == 1 and w % 2 != 0 for w in W)
    check("C.e-A1-gap-structure", oke)
    return

# ---------------- Section D: generic 64-block class-profile system ----------------
def section_D():
    rngD = random.Random(270242)
    labels = list(range(64))
    # choose D (16 labels) with XOR 0 by rejection (generic, not the target)
    for _ in range(100000):
        D = set(rngD.sample(labels, 16))
        x = 0
        for c in D: x ^= c
        if x == 0: break
    Dhat0 = 0
    rest = [c for c in labels if c not in D]
    # class deltas from section C mapping
    delta = {}
    for d in (1, 2, 3):
        ann = frozenset(s for s in range(4) if chi(s, d) == 1)
        delta[{frozenset((0, 2)): "C2", frozenset((0, 3)): "C3", frozenset((0, 1)): "D1"}[ann]] = d
    pairclasses = ["C2"]*4 + ["C3"]*6 + ["D1"]*18
    pairlabels = rest[:28]; glabels = rest[28:31]; olabels = rest[31:48]
    assert len(pairlabels) == 28 and len(glabels) == 3 and len(olabels) == 17

    def draw(signs_rng):
        v = {}
        z0 = {}
        for c in D:
            z0[c] = signs_rng.randrange(4)
            v[(c, z0[c])] = 1 if signs_rng.randrange(2) else -1
        for c, cl in zip(pairlabels, pairclasses):
            d = delta[cl]
            zs = [z for z in range(4) if True]
            # pick any 2-subset with XOR d
            for z3 in range(4):
                z4 = z3 ^ d
                if z3 < z4: break
            v[(c, z3)] = 1 if signs_rng.randrange(2) else -1
            v[(c, z4)] = 1 if signs_rng.randrange(2) else -1
        for c in glabels:
            pass
        for c in olabels:
            for z in range(4):
                v[(c, z)] = 1 if signs_rng.randrange(2) else -1
        return v, z0

    def blockW(v):
        W = {s: {} for s in range(4)}
        for s in range(4):
            for c in labels:
                W[s][c] = sum(v.get((c, z), 0)*chi(s, z) for z in range(4))
        return W

    def Vhat(W, r, s):
        return sum(W[s][c]*(1 if dot(r, c) == 0 else -1) for c in labels)

    # D1: W_s odd exactly on D, all s
    # D2: mod-4 identity; D3: flatness iff (N1)+(VB); D6: Omega decomposition
    found = None
    for attempt in range(4000):
        v, z0 = draw(rngD)
        W = blockW(v)
        okD1 = all({c for c in labels if W[s][c] % 2 != 0} == D for s in range(4))
        if not okD1:
            check("D1.W_s-odd-exactly-on-D", False); return
        okD2 = True
        Dhat = 0
        for c in D: Dhat ^= c
        for s in range(4):
            S = sum(W[s][c] for c in labels)
            for r in range(64):
                resid = (S - 2*dot(r, Dhat)) % 4
                okD2 &= (Vhat(W, r, s) % 4) == resid
        if not okD2:
            check("D2.mod4-identity", False); return
        if all(sum(W[s][c] for c in labels) % 4 == 2 for s in range(4)):
            found = (v, z0, W)
            break
    check("D1.W_s-odd-exactly-on-D", True)
    check("D2.mod4-identity", True)
    check("D3.positive-config-found", found is not None)
    v, z0, W = found
    flat = all(Vhat(W, r, s) % 4 == 2 for r in range(64) for s in range(4))
    check("D3.N1-and-VB-imply-flatness", flat)
    # Omega decomposition: c-part XOR = XOR(D), z-part XOR = XOR of z0 over D
    cpart = 0; zpart = 0
    for (c, z), val in v.items():
        if val != 0:
            cpart ^= c; zpart ^= z
    xorD = 0
    for c in D: xorD ^= c
    xorz0 = 0
    for c in D: xorz0 ^= z0[c]
    check("D6.omega-decomposition", cpart == xorD and zpart == xorz0,
          f"cpart==XOR(D)={xorD==0}, zpart==XOR z0={zpart}=={xorz0}")
    # negative: D-hat != 0 (swap one A1 label with one pair label; per-fibre sums unchanged)
    c_in = next(iter(D)); c_out = pairlabels[0]
    D2set = (D - {c_in}) | {c_out}
    Dhat2 = 0
    for c in D2set: Dhat2 ^= c
    # relabel: move the A1 assignment of c_in to c_out and the pair assignment of c_out to c_in
    v2 = dict(v)
    zA = z0[c_in]
    del v2[(c_in, zA)]
    # pair block assignment of c_out:
    pv = [(z, v2[(c_out, z)]) for z in range(4) if (c_out, z) in v2]
    for z, val in pv: del v2[(c_out, z)]
    v2[(c_out, zA)] = v[(c_in, zA)]
    for z, val in pv: v2[(c_in, z)] = val
    W2 = blockW(v2)
    flat2 = all(Vhat(W2, r, s) % 4 == 2 for r in range(64) for s in range(4))
    same_sums = all(sum(W2[s][c] for c in labels) == sum(W[s][c] for c in labels) for s in range(4))
    check("D4.Dhat!=0-breaks-flatness", (not flat2) and Dhat2 != 0 and same_sums,
          f"Dhat2={Dhat2}, per-fibre sums unchanged={same_sums}")
    # negative: VB fails (flip one D-block sign; all four fibre sums shift by 2 mod 4)
    cD = next(iter(D))
    v3 = dict(v)
    zD = z0[cD]
    v3[(cD, zD)] = -v3[(cD, zD)]
    W3 = blockW(v3)
    sums3 = [sum(W3[s][c] for c in labels) % 4 for s in range(4)]
    flat3 = all(Vhat(W3, r, s) % 4 == 2 for r in range(64) for s in range(4))
    check("D5.VB-fails-breaks-flatness", (not flat3) and all(x == 0 for x in sums3),
          f"fibre sums mod4 after flip: {sums3}")
    # N2 non-vacuity: change one z0 so XOR z0 != 0, z-part becomes nonzero
    cD2 = sorted(D)[1]
    v4 = dict(v)
    del v4[(cD2, z0[cD2])]
    nz = (z0[cD2] + 1 + rngD.randrange(3)) % 4
    if nz == z0[cD2]: nz = (nz + 1) % 4
    v4[(cD2, nz)] = v[(cD2, z0[cD2])]
    zp4 = 0
    for (c, z), val in v4.items():
        if val != 0: zp4 ^= z
    check("D6b.N2-nonvacuity-on-generic-data", zp4 != 0 and zp4 == (xorz0 ^ z0[cD2] ^ nz),
          f"mutated XOR z-part={zp4}")
    return

section_A()
section_B()
section_C()
section_D()

wall = time.perf_counter() - T0
nfail = sum(1 for r in results if r["status"] == "FAIL")
try:
    native = subprocess.run(["/bin/date"], capture_output=True, text=True, timeout=5).stdout.strip()
except Exception as e:
    native = f"unavailable: {e}"
script_path = os.path.abspath(__file__)
sha = hashlib.sha256(open(script_path, "rb").read()).hexdigest()
receipt = {
    "kind": "REVIEWER_OWNED_BOUNDED_EXACT_CONTROL_RECEIPT",
    "wave": "f270-nl242-uv-caller-coupling-necessary",
    "script": script_path,
    "script_sha256": sha,
    "native_date_at_run_end": native,
    "python": sys.version.split()[0],
    "arithmetic": "integer and fractions.Fraction only (perf_counter used for wall-clock only)",
    "constraints": "stdlib only; no author code; no network; synthetic balanced Boolean functions and generic finite sets only; target object never constructed; no universal claim proven",
    "wall_seconds": round(wall, 3),
    "checks_total": len(results),
    "checks_failed": nfail,
    "checks": results,
    "overall": "ALL PASS" if nfail == 0 else "FAILURES PRESENT",
}
out = os.path.join(os.path.dirname(script_path), "reviewer-control-receipt-v1.json")
with open(out, "w") as fh:
    json.dump(receipt, fh, indent=1, sort_keys=False)
    fh.write("\n")
print(json.dumps({"overall": receipt["overall"], "checks": len(results),
                  "failed": nfail, "wall_s": round(wall, 2), "receipt": out}))
