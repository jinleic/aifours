#!/usr/bin/env python3
"""w8_exotic_structure_v1: float stdlib analysis (evidence only, never a proof premise) of the 100 "exotic" flat planes
recorded in evidence/w8_flat_planes_couples_v5.result.json (sha256 pinned in argv[2], checked before use).

Hypothesis tested: every exotic plane is invariant under exactly one of the 25 conjugates W U W^* (W = X^a Z^c) of the
order-3 Clifford unitary U = Q X Q F (Q = diag(zeta^(t^2)), F_(j,t) = zeta^(-jt)/sqrt5), which cycles the used bases
X -> Z -> T -> X and the complementary lines L_1 -> L_3 -> L_2; and the plane is (line in the omega-eigenspace) (+)
(line in the omega^2-eigenspace) of that conjugate (eigen-multiplicities 1, 2, 2). Also: the exotic couple graph per
basis with the gap rule of v5, its K4-pattern count (exhaustive), and the stabiliser-label differences of compatible
pairs. Standard library; budget 200 s; output JSON (exclusive) argv[3].
Usage: w8_exotic_structure_v1.py V5_RESULT_JSON V5_SHA256 OUT.json
"""
import cmath, hashlib, json, math, sys, time

T0 = time.monotonic()
raw = open(sys.argv[1], "rb").read()
sha_ok = hashlib.sha256(raw).hexdigest() == sys.argv[2]
if not sha_ok:
    sys.exit(9)
d5 = json.loads(raw.decode("utf-8"))
N = 5
Z5 = cmath.exp(2j * math.pi / 5)
R5 = math.sqrt(5.0)


def zp(e):
    return Z5 ** (e % 5)


def vk(k, m):
    return [zp(3 * k * t * t + m * t) / R5 for t in range(N)]


def outer(u):
    return [[u[i] * u[j].conjugate() for j in range(N)] for i in range(N)]


def mm(A, B):
    return [[sum(A[i][l] * B[l][j] for l in range(N)) for j in range(N)] for i in range(N)]


def dag(M):
    return [[M[j][i].conjugate() for j in range(N)] for i in range(N)]


def dist(A, B):
    return math.sqrt(sum(abs(A[i][j] - B[i][j]) ** 2 for i in range(N) for j in range(N)))


def tr(M):
    return sum(M[i][i] for i in range(N))


def eye():
    return [[1.0 + 0j if i == j else 0j for j in range(N)] for i in range(N)]


def is_scalar(M):
    c = M[0][0]
    return abs(c) > 1e-9 and all(abs(M[i][j] - (c if i == j else 0)) < 1e-9 for i in range(N) for j in range(N))


def Pof(blocks):
    P = [[0.4 + 0j if i == j else 0j for j in range(N)] for i in range(N)]
    for k, b in zip((1, 2, 3), blocks):
        for m in range(N):
            O = outer(vk(k, m))
            for i in range(N):
                for j in range(N):
                    P[i][j] += b[m] / 5.0 * O[i][j]
    return P


BASES = {"Z": [[1.0 + 0j if t == s else 0j for t in range(N)] for s in range(N)],
         "X": [[zp(n * t) / R5 for t in range(N)] for n in range(N)],
         "T": [vk(4, m) for m in range(N)]}
F = [[zp(-j * t) / R5 for t in range(N)] for j in range(N)]
Q = [[zp(t * t) if i == t else 0j for t in range(N)] for i in range(N)]
Xs = [[1.0 + 0j if i == (j + 1) % N else 0j for j in range(N)] for i in range(N)]
U = mm(Q, mm(Xs, mm(Q, F)))
WHm = {}
for a in range(N):
    for c in range(N):
        W = [[0j] * N for _ in range(N)]
        for t in range(N):
            W[(t + a) % N][t] = zp(c * t)
        WHm[(a, c)] = W

# order and eigenspaces of U
order, Mpow = None, eye()
for k_ in range(1, 13):
    Mpow = mm(U, Mpow)
    if is_scalar(Mpow):
        order = k_
        break
U3 = mm(U, mm(U, U))
lam = U3[0][0] ** (1.0 / 3.0)
Un = [[x / lam for x in row] for row in U]
w3 = cmath.exp(2j * math.pi / 3)
EP = []
for j in range(3):
    Pj = [[0j] * N for _ in range(N)]
    Mk = eye()
    for k in range(3):
        for a in range(N):
            for b in range(N):
                Pj[a][b] += (w3 ** (-j * k)) * Mk[a][b] / 3
        Mk = mm(Un, Mk)
    EP.append(Pj)
mults = [round(tr(Pj).real, 9) for Pj in EP]


# action of U on the six bases (as sets of rays): image of basis b is basis b' if all |<U e, f>|^2 in {0, 1}
def basis_image(bname):
    allb = dict(BASES)
    for k in (1, 2, 3):
        allb["L%d" % k] = [vk(k, m) for m in range(N)]
    imgs = [[sum(U[i][t] * e[t] for t in range(N)) for i in range(N)] for e in allb[bname]]
    for nm, fb in allb.items():
        ok = all(any(abs(abs(sum(f[i].conjugate() * v[i] for i in range(N))) ** 2 - 1.0) < 1e-9 for f in fb) for v in imgs)
        if ok:
            return nm
    return None


action = {b: basis_image(b) for b in ("Z", "X", "T", "L1", "L2", "L3")}

# exotic planes and their stabilising conjugates
Pex = [Pof(b) for b in d5["exotic_a_blocks"]]
conj = {w: mm(mm(W, U), dag(W)) for w, W in WHm.items()}
conjE = {}
for w, W in WHm.items():
    conjE[w] = [mm(mm(W, Pj), dag(W)) for Pj in EP]
stab, decomp_dev = [], 0.0
for P in Pex:
    hits = [w for w, Uw in conj.items() if dist(mm(Uw, P), mm(P, Uw)) < 1e-8]
    stab.append(hits)
    for w in hits:
        t = [tr(mm(P, E)).real for E in conjE[w]]
        j1 = min(range(3), key=lambda j: abs(mults[j] - 1.0))
        decomp_dev = max([decomp_dev, abs(t[j1])] + [abs(t[j] - 1.0) for j in range(3) if j != j1])
per_conj = {}
for hits in stab:
    for w in hits:
        per_conj[w] = per_conj.get(w, 0) + 1
mubP = []
for k in (1, 2, 3):
    for m1 in range(N):
        for m2 in range(m1 + 1, N):
            O1, O2 = outer(vk(k, m1)), outer(vk(k, m2))
            mubP.append([[O1[i][j] + O2[i][j] for j in range(N)] for i in range(N)])
mub_inv = sum(1 for P in mubP if any(dist(mm(Uw, P), mm(P, Uw)) < 1e-8 for Uw in conj.values()))


# exotic couple graph (gap rule of v5)
def frame(P):
    cols = [[P[i][j] for i in range(N)] for j in range(N)]
    j1 = max(range(N), key=lambda j: sum(abs(x) ** 2 for x in cols[j]))
    n1 = math.sqrt(sum(abs(x) ** 2 for x in cols[j1]))
    v1 = [x / n1 for x in cols[j1]]
    best, bw = -1.0, None
    for j in range(N):
        pr = sum(v1[i].conjugate() * cols[j][i] for i in range(N))
        w = [cols[j][i] - pr * v1[i] for i in range(N)]
        nw = math.sqrt(sum(abs(x) ** 2 for x in w))
        if nw > best:
            best, bw = nw, w
    return [v1, [x / best for x in bw]]


def jacobi(S):
    n = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(60):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-32:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
                cs, sn = math.cos(th), math.sin(th)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p], A[k][q] = cs * akp - sn * akq, sn * akp + cs * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k], A[q][k] = cs * apk - sn * aqk, sn * apk + cs * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p], V[k][q] = cs * vkp - sn * vkq, sn * vkp + cs * vkq
    order_ = sorted(range(n), key=lambda i: A[i][i])
    return [A[i][i] for i in order_], [[V[k][i] for k in range(n)] for i in order_]


FR = [frame(P) for P in Pex]


def rowvec(fr, e):
    return [sum(e[i].conjugate() * fr[c][i] for i in range(N)) for c in range(2)]


def couple(r, s, b):
    rows = []
    for e in BASES[b]:
        u, v = rowvec(FR[r], e), rowvec(FR[s], e)
        rows.append([u[i] * v[j].conjugate() for i in range(2) for j in range(2)])
    G = [[sum(rows[e][p].conjugate() * rows[e][q] for e in range(5)) for q in range(4)] for p in range(4)]
    Rm = [[0.0] * 8 for _ in range(8)]
    for p in range(4):
        for q in range(4):
            Rm[p][q], Rm[p][q + 4] = G[p][q].real, -G[p][q].imag
            Rm[p + 4][q], Rm[p + 4][q + 4] = G[p][q].imag, G[p][q].real
    ev, evec = jacobi(Rm)
    sc = max(ev[-1], 1e-300)
    x = evec[0]
    K = [[complex(x[0], x[4]), complex(x[1], x[5])], [complex(x[2], x[6]), complex(x[3], x[7])]]
    KK = [[sum(K[i][l].conjugate() * K[i][j] for i in range(2)) for j in range(2)] for l in range(2)]
    t = (KK[0][0].real + KK[1][1].real) / 2
    dfc = math.sqrt(abs(KK[0][0] - t) ** 2 + abs(KK[1][1] - t) ** 2 + 2 * abs(KK[0][1]) ** 2) / max(t, 1e-300)
    return ev[0] / sc, ev[2] / sc, dfc


ADJ = {b: [set() for _ in Pex] for b in ("Z", "X", "T")}
lam_c, lam_i = [], []
labdiff = {}
nP = len(Pex)
for r in range(nP):
    for s in range(r, nP):
        for b in ("Z", "X", "T"):
            l1, l2, dfc = couple(r, s, b)
            ok = l1 < 1e-10 and (l2 < 1e-10 or dfc < 1e-3)
            (lam_c if ok else lam_i).append(l1)
            if ok:
                ADJ[b][r].add(s)
                ADJ[b][s].add(r)
                if stab[r] and stab[s]:
                    wr, ws = stab[r][0], stab[s][0]
                    key = "%s:(%d,%d)" % (b, (ws[0] - wr[0]) % 5, (ws[1] - wr[1]) % 5)
                    labdiff[key] = labdiff.get(key, 0) + 1
k4 = 0
for p00 in range(nP):
    for p01 in ADJ["Z"][p00]:
        for p10 in ADJ["X"][p00] & ADJ["T"][p01]:
            k4 += len(ADJ["T"][p00] & ADJ["X"][p01] & ADJ["Z"][p10])
out = {"probe": "w8_exotic_structure_v1", "kind": "float stdlib analysis; evidence only", "input_sha_ok": sha_ok,
       "U_projective_order": order, "U_eigen_multiplicities": mults, "U_action_on_bases": action,
       "exotic_planes": len(Pex), "stabilising_conjugates_per_plane": sorted(set(len(h) for h in stab)),
       "planes_per_conjugate": sorted(set(per_conj.values())), "conjugates_used": len(per_conj),
       "max_decomposition_deviation_(trace_with_E1,Eomega,Eomega2_vs_0,1,1)": decomp_dev,
       "mub_pair_planes_invariant_under_a_conjugate": mub_inv,
       "couple_graph": {"degree_per_basis": {b: sorted(set(len(x) for x in ADJ[b])) for b in ADJ},
                        "max_lambda1_compatible": max(lam_c) if lam_c else None,
                        "min_lambda1_incompatible": min(lam_i) if lam_i else None,
                        "label_differences_of_compatible_pairs": labdiff},
       "K4_patterns_all_exotic": k4, "elapsed_s": round(time.monotonic() - T0, 3)}
with open(sys.argv[3], "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out))
