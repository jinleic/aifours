"""Independent brute-force check of Theorem 4 (proof.md) on random instances.

Theorem 4: an E-unitary orthodox semigroup S whose band E has exactly two D-classes embeds into
B0^G x| G (wreath product), G = S/sigma, with B0 a band whose structure semilattice is a 2-chain
(hence locally regular, Lemma 5).

For each random instance we
  1. build S from structural data (2-chain band E, subgroup H1 <= G, actions sigma, sigma'),
  2. verify by brute force that S is an associative, regular, orthodox, E-unitary semigroup whose
     idempotents form exactly E (a 2-chain band; we also record whether E is regular),
  3. build B0 and the functor F of the proof, verify that B0 is a band, has two D-classes,
     is locally regular, and that s -> (g -> F(g,s), sigma(s)) is an injective homomorphism
     S -> B0^G x| G (all products checked).
Nothing from the proof is assumed beyond the definitions of S and of the construction.

Usage: python3 work/check_two_chain_theorem.py [num_instances] [seed]
"""
from __future__ import annotations

import itertools
import random
import sys

# ---------------------------------------------------------------- small groups (as Cayley tables)

def cyclic(n):
    return [[(a + b) % n for b in range(n)] for a in range(n)]


def klein():
    return [[a ^ b for b in range(4)] for a in range(4)]


def sym3():
    perms = list(itertools.permutations(range(3)))
    idx = {p: k for k, p in enumerate(perms)}
    # (p*q)(x) = p(q(x))
    return [[idx[tuple(p[q[x]] for x in range(3))] for q in perms] for p in perms]


GROUPS = {"Z1": cyclic(1), "Z2": cyclic(2), "Z3": cyclic(3), "Z4": cyclic(4), "V4": klein(), "S3": sym3()}


def group_identity(Gt):
    return next(e for e in range(len(Gt)) if all(Gt[e][x] == x for x in range(len(Gt))))


def group_inverse(Gt, e):
    return [next(y for y in range(len(Gt)) if Gt[x][y] == e) for x in range(len(Gt))]


def subgroups(Gt):
    n = len(Gt)
    out = []
    for mask in range(1, 1 << n):
        H = [x for x in range(n) if mask >> x & 1]
        Hs = set(H)
        if all(Gt[a][b] in Hs for a in H for b in H):
            out.append(H)
    return out


def homs_to_sym(Gt, H, J, right=False):
    """all maps h -> permutation of J (tuples) that are homomorphisms (left action)
    or anti-homomorphisms (right action) from the subgroup H."""
    perms = list(itertools.permutations(range(len(J))))
    res = []
    if len(perms) ** len(H) > 50000:
        # sample random assignments instead of full enumeration (the trivial action is always kept)
        cands = itertools.chain([tuple(perms[0] for _ in H)],
                                (tuple(random.choice(perms) for _ in H) for _ in range(20000)))
    else:
        cands = itertools.product(perms, repeat=len(H))
    for assign in cands:
        m = dict(zip(H, assign))
        ok = True
        for a in H:
            for b in H:
                ab = Gt[a][b]
                if not right:
                    comp = tuple(m[a][m[b][x]] for x in range(len(J)))  # sigma_a o sigma_b
                else:
                    comp = tuple(m[b][m[a][x]] for x in range(len(J)))  # sigma_b o sigma_a
                if m[ab] != comp:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            res.append(m)
    return res


# ---------------------------------------------------------------- random 2-chain band data

def random_side(n_top_index, n_other_index, n_points, kmin=1, kmax=None):
    """Random 'phi-side' data: core J (subset of points, by local index), bijections pi_r : J -> J_r
    (r over n_top_index, pi_0 = id), retractions p_l : points -> J (l over n_other_index) with
    p_l(pi_r(j)) = j.  Returns (J, pi, p) with J a list of points."""
    kmax = n_points if kmax is None else kmax
    while True:
        k = random.randint(kmin, kmax)
        J = sorted(random.sample(range(n_points), k))
        pi = [dict((j, j) for j in J)]
        ok = True
        for _ in range(1, n_top_index):
            img = random.sample(range(n_points), k)
            pi.append(dict(zip(J, img)))
        # compatibility: pi_r(j) = pi_r'(j') implies j = j'
        back = {}
        for r in range(n_top_index):
            for j, x in pi[r].items():
                if back.setdefault(x, j) != j:
                    ok = False
        if not ok:
            continue
        p = []
        for _ in range(n_other_index):
            pl = {}
            for x in range(n_points):
                pl[x] = back[x] if x in back else random.choice(J)
            p.append(pl)
        return J, pi, p


def build_instance(rng_seed, hard=False):
    """hard=True: force a non-regular band E and, when possible, non-trivial actions sigma, sigma'."""
    random.seed(rng_seed)
    gname = random.choice(list(GROUPS))
    Gt = GROUPS[gname]
    n = len(Gt)
    e = group_identity(Gt)
    ginv = group_inverse(Gt, e)
    subs = subgroups(Gt)
    H1 = random.choice([H for H in subs if len(H) > 1] or subs) if hard else random.choice(subs)
    while True:
        if hard:
            I1, L1 = random.randint(1, 2), random.randint(2, 3)
            I2, L2 = random.randint(3, 4), random.randint(2, 3)
            J, pi, p = random_side(I1, L1, I2, kmin=2, kmax=I2 - 1)
            Jc, pic, pc = random_side(L1, I1, L2, kmin=1, kmax=L2)
            # non-regular: some p_l differ (as maps), i.e. phi_(r,l) depends on l
            if len({tuple(sorted(pl.items())) for pl in p}) < 2:
                continue
        else:
            I1, L1 = random.randint(1, 2), random.randint(1, 3)
            I2, L2 = random.randint(1, 3), random.randint(1, 3)
            J, pi, p = random_side(I1, L1, I2)        # rows side: pi indexed by top rows, p by top cols
            Jc, pic, pc = random_side(L1, I1, L2)     # columns side: pi' indexed by top cols, p' by top rows
        break
    sig_choices = homs_to_sym(Gt, H1, J)
    sigc_choices = homs_to_sym(Gt, H1, Jc, right=True)
    if hard:
        nt = [m for m in sig_choices if any(m[h] != tuple(range(len(J))) for h in H1)]
        ntc = [m for m in sigc_choices if any(m[h] != tuple(range(len(Jc))) for h in H1)]
        sig = random.choice(nt or sig_choices)
        sigc = random.choice(ntc or sigc_choices)
    else:
        sig = random.choice(sig_choices)
        sigc = random.choice(sigc_choices)
    Jidx = {j: k for k, j in enumerate(J)}
    Jcidx = {j: k for k, j in enumerate(Jc)}

    def Phi(r, h, l, i):
        j = p[l][i]
        j = J[sig[h][Jidx[j]]]
        return pi[r][j]

    def Psi(r, h, l, jcol):
        x = pc[r][jcol]
        x = Jc[sigc[h][Jcidx[x]]]
        return pic[l][x]

    top = [("t", r, h, l) for r in range(I1) for h in H1 for l in range(L1)]
    bot = [("b", i, g, j) for i in range(I2) for g in range(n) for j in range(L2)]
    elems = top + bot
    index = {x: k for k, x in enumerate(elems)}

    def mul(x, y):
        if x[0] == "t" and y[0] == "t":
            return ("t", x[1], Gt[x[2]][y[2]], y[3])
        if x[0] == "b" and y[0] == "b":
            return ("b", x[1], Gt[x[2]][y[2]], y[3])
        if x[0] == "t":
            return ("b", Phi(x[1], x[2], x[3], y[1]), Gt[x[2]][y[2]], y[3])
        return ("b", x[1], Gt[x[2]][y[2]], Psi(y[1], y[2], y[3], x[3]))

    N = len(elems)
    T = [[index[mul(elems[a], elems[b])] for b in range(N)] for a in range(N)]
    sigma = [x[2] for x in elems]
    data = dict(G=gname, Gt=Gt, e=e, ginv=ginv, H1=H1, I1=I1, L1=L1, I2=I2, L2=L2, J=J, pi=pi, p=p,
                Jc=Jc, pic=pic, pc=pc, sig=sig, sigc=sigc, elems=elems, index=index)
    return T, sigma, data


# ---------------------------------------------------------------- generic checks on tables

def check_semigroup_properties(T, sigma, Gt, e):
    N = len(T)
    assert all(T[T[x][y]][z] == T[x][T[y][z]] for x in range(N) for y in range(N) for z in range(N)), "not associative"
    E = [x for x in range(N) if T[x][x] == x]
    Es = set(E)
    for x in range(N):
        assert any(T[T[x][y]][x] == x and T[T[y][x]][y] == y for y in range(N)), "not regular"
    assert all(T[a][b] in Es for a in E for b in E), "not orthodox"
    # sigma is a homomorphism onto G with kernel class exactly E  => E-unitary
    assert all(sigma[T[x][y]] == Gt[sigma[x]][sigma[y]] for x in range(N) for y in range(N)), "sigma not hom"
    assert set(sigma) == set(range(len(Gt))), "sigma not onto"
    assert {x for x in range(N) if sigma[x] == e} == Es, "sigma^-1(1) != E"
    for f in E:
        for a in range(N):
            if T[f][a] in Es or T[a][f] in Es:
                assert a in Es, "not E-unitary"
    return E


def band_regular(T, elems):
    return all(T[T[T[a][x]][y]][a] == T[T[T[T[a][x]][a]][y]][a] for a in elems for x in elems for y in elems)


def band_locally_regular(T, elems):
    for e in elems:
        loc = sorted({T[T[e][x]][e] for x in elems})
        if not band_regular(T, loc):
            return False
    return True


def d_classes(T, elems):
    cls, seen = [], set()
    for a in elems:
        if a in seen:
            continue
        c = [b for b in elems if T[T[a][b]][a] == a and T[T[b][a]][b] == b]
        cls.append(c)
        seen.update(c)
    return cls


# ---------------------------------------------------------------- the construction of Theorem 4

def construct_and_check(T, sigma, d):
    Gt, e, ginv = d["Gt"], d["e"], d["ginv"]
    n = len(Gt)
    H1 = d["H1"]
    H1s = set(H1)
    J, pi, p, Jc, pic, pc, sig, sigc = (d[k] for k in ("J", "pi", "p", "Jc", "pic", "pc", "sig", "sigc"))
    I1, L1, I2, L2 = d["I1"], d["L1"], d["I2"], d["L2"]
    Jidx = {j: k for k, j in enumerate(J)}
    Jcidx = {j: k for k, j in enumerate(Jc)}
    # left transversal: a = t_a k_a with k_a in H1
    reps = []
    k_of = {}
    for a in range(n):
        for t in reps:
            k = Gt[ginv[t]][a]
            if k in H1s:
                k_of[a] = k
                break
        else:
            reps.append(a)
            k_of[a] = e

    def perm_apply(pm, idx, vals, x):
        return vals[pm[idx[x]]]

    def perm_inv_apply(pm, idx, vals, x):
        k = idx[x]
        return vals[pm.index(k)]

    # B0 elements: top ((r,a),(l,b)), bottom ((i,c),(j,c2)) with r<I1, l<L1, i<I2, j<L2, a,b,c,c2 in G
    def phiB(r, a, l, b, i, c):
        # p_(l,b)((i,c)) = sigma_{k_c}(p_l(i)) ; pi_(r,a)(x) = (pi_r(sigma_{k_a}^{-1}(x)), a)
        x = perm_apply(sig[k_of[c]], Jidx, J, p[l][i])
        x = perm_inv_apply(sig[k_of[a]], Jidx, J, x)
        return (pi[r][x], a)

    def psiB(r, a, l, b, j, c):
        # p'_(r,a)((j,c)) = sigma'_{k_c}^{-1}(p'_r(j)) ; pi'_(l,b)(x) = (pi'_l(sigma'_{k_b}(x)), b)
        x = perm_inv_apply(sigc[k_of[c]], Jcidx, Jc, pc[r][j])
        x = perm_apply(sigc[k_of[b]], Jcidx, Jc, x)
        return (pic[l][x], b)

    topB = [("t", r, a, l, b) for r in range(I1) for a in range(n) for l in range(L1) for b in range(n)]
    botB = [("b", i, c, j, c2) for i in range(I2) for c in range(n) for j in range(L2) for c2 in range(n)]
    B = topB + botB
    bidx = {x: k for k, x in enumerate(B)}

    def bmul(x, y):
        if x[0] == "t" and y[0] == "t":
            return ("t", x[1], x[2], y[3], y[4])
        if x[0] == "b" and y[0] == "b":
            return ("b", x[1], x[2], y[3], y[4])
        if x[0] == "t":
            row = phiB(x[1], x[2], x[3], x[4], y[1], y[2])
            return ("b", row[0], row[1], y[3], y[4])
        col = psiB(y[1], y[2], y[3], y[4], x[3], x[4])
        return ("b", x[1], x[2], col[0], col[1])

    M = len(B)
    BT = [[bidx[bmul(B[u], B[v])] for v in range(M)] for u in range(M)]
    allB = list(range(M))
    assert all(BT[u][u] == u for u in allB), "B0 not idempotent"
    assert all(BT[BT[u][v]][w] == BT[u][BT[v][w]] for u in allB for v in allB for w in allB), "B0 not associative"
    assert len(d_classes(BT, allB)) == 2, "B0 does not have two D-classes"
    assert band_locally_regular(BT, allB), "B0 not locally regular"

    elems = d["elems"]

    def F(g, s):
        x = elems[s]
        if x[0] == "t":
            _, r, h, l = x
            return bidx[("t", r, g, l, Gt[g][h])]
        _, i, k, j = x
        return bidx[("b", i, g, j, Gt[g][k])]

    N = len(T)
    # functor: F(g,s) F(g sigma(s), t) = F(g, st)
    for g in range(n):
        for s in range(N):
            for t in range(N):
                assert BT[F(g, s)][F(Gt[g][sigma[s]], t)] == F(g, T[s][t]), "F not a functor"
    # embedding S -> B0^G x| G,  s -> (f_s, sigma(s)), f_s(g) = F(g, s), (^h f)(g) = f(g h)
    emb = {s: (tuple(F(g, s) for g in range(n)), sigma[s]) for s in range(N)}
    assert len(set(emb.values())) == N, "embedding not injective"
    for s in range(N):
        for t in range(N):
            fs, hs = emb[s]
            ft, ht = emb[t]
            prod = tuple(BT[fs[g]][ft[Gt[g][hs]]] for g in range(n))
            assert (prod, Gt[hs][ht]) == emb[T[s][t]], "embedding not a homomorphism"
    return M


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    hard = "--hard" in sys.argv
    num = int(args[0]) if len(args) > 0 else 200
    seed0 = int(args[1]) if len(args) > 1 else 1
    stats = {"instances": 0, "nonregular_E": 0, "nontrivial_twist": 0, "nontrivial_H1": 0, "groups": {}}
    for k in range(num):
        T, sigma, d = build_instance(seed0 + k, hard=hard)
        E = check_semigroup_properties(T, sigma, d["Gt"], d["e"])
        assert len(d_classes(T, E)) == 2, "E must have two D-classes"
        assert band_locally_regular(T, E), "E not locally regular (contradicts Lemma 5)"
        nonreg = not band_regular(T, E)
        twist = any(any(d["sig"][h][x] != x for x in range(len(d["J"]))) for h in d["H1"]) or \
            any(any(d["sigc"][h][x] != x for x in range(len(d["Jc"]))) for h in d["H1"])
        M = construct_and_check(T, sigma, d)
        stats["instances"] += 1
        stats["nonregular_E"] += nonreg
        stats["nontrivial_twist"] += twist
        stats["nontrivial_H1"] += len(d["H1"]) > 1
        stats["groups"][d["G"]] = stats["groups"].get(d["G"], 0) + 1
        if k < 5 or k % 25 == 0:
            print(f"instance {k}: G={d['G']} |H1|={len(d['H1'])} |S|={len(T)} |E|={len(E)} "
                  f"E regular={not nonreg} twist={twist} |B0|={M}: OK", flush=True)
    print(("HARD " if hard else "") + "ALL OK", stats)


if __name__ == "__main__":
    main()
