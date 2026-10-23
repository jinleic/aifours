"""Search groups on X = {0..n-1} x C (label g*i + a) preserving the four groups {i} x C (README §3).

build(name, n, g) -> dict(gens, group_of, groups, res) where res maps names to generator lists
of subgroups fixing x = label 0 and the anchor h = label 1 (the colouring symmetry choices).
* "A4xC":       A4 on the group index (pi1 = (1 2 3), pi2 = (0 1)(2 3)) x C_g (a -> a+1).
* "A4xA5":      g = 20; C = the 20 three-cycles of A5, A5 acting by conjugation; coordinate 0 is
                c0 = (0 1 2), coordinate 1 is c0^-1 (so R fixes x and h).
* "A4xAGL4xZ5": g = 20; C = F4 x Z5 (a = 5b + c), AGL(1,4) on b, Z5 on c.
F4 = {0,1,w,w^2} encoded 0,1,2,3: addition = XOR, multiplication by w: 1->2->3->1.
"""
from itertools import permutations


def _perm_from_maps(n, g, index_map, coord_map):
    return tuple(g * index_map[i] + coord_map[a] for i in range(n) for a in range(g))


def build(name, n, g):
    assert n == 4
    v = n * g
    group_of = [p // g for p in range(v)]
    groups = [list(range(g * i, g * i + g)) for i in range(n)]
    ident_i, ident_c = list(range(n)), list(range(g))
    pi1 = [0, 2, 3, 1]          # (1 2 3): multiplication by w on F4
    pi2 = [1, 0, 3, 2]          # (0 1)(2 3): translation by 1 on F4
    P1 = _perm_from_maps(n, g, pi1, ident_c)
    P2 = _perm_from_maps(n, g, pi2, ident_c)
    if name == "A4xC":
        tau = _perm_from_maps(n, g, ident_i, [(a + 1) % g for a in range(g)])
        return {"gens": [P1, P2, tau], "group_of": group_of, "groups": groups,
                "res": {"C3": [P1], "1": []}}
    if name == "A4xA5":
        assert g == 20
        def mul(p, q):  # (p*q)(x) = p(q(x))
            return tuple(p[q[x]] for x in range(5))
        def inv(p):
            r = [0] * 5
            for i, x in enumerate(p):
                r[x] = i
            return tuple(r)
        def is_even(p):
            s, seen = 0, set()
            for i in range(5):
                if i in seen:
                    continue
                L, j = 0, i
                while j not in seen:
                    seen.add(j); j = p[j]; L += 1
                s += L - 1
            return s % 2 == 0
        A5 = sorted(p for p in permutations(range(5)) if is_even(p))
        c0 = (1, 2, 0, 3, 4)    # 0->1->2->0
        threes = [p for p in A5 if sum(1 for i in range(5) if p[i] != i) == 3]
        assert len(threes) == 20
        coords = [c0, inv(c0)] + sorted(p for p in threes if p not in (c0, inv(c0)))
        idx = {c: k for k, c in enumerate(coords)}
        def conj(h):
            return [idx[mul(mul(h, c), inv(h))] for c in coords]
        gensA5 = [(1, 2, 3, 4, 0), (1, 2, 0, 3, 4)]   # 5-cycle and 3-cycle generate A5
        coord_gens = [_perm_from_maps(n, g, ident_i, conj(h)) for h in gensA5]
        Cc = _perm_from_maps(n, g, ident_i, conj(c0))  # coordinate C3 fixing c0, c0^-1
        return {"gens": [P1, P2] + coord_gens, "group_of": group_of, "groups": groups,
                "res": {"C3xC3": [P1, Cc], "C3": [P1], "C3coord": [Cc],
                        "C3diag": [tuple(P1[Cc[x]] for x in range(v))],
                        "C3anti": [tuple(P1[Cc[Cc[x]]] for x in range(v))], "1": []}}
    if name == "A4xAGL4xZ5":
        assert g == 20
        def cmap(fb, fc):
            return [5 * fb[a // 5] + fc[a % 5] for a in range(g)]
        idb, idc = list(range(4)), list(range(5))
        mw = _perm_from_maps(n, g, ident_i, cmap(pi1, idc))
        tb = _perm_from_maps(n, g, ident_i, cmap(pi2, idc))
        tc = _perm_from_maps(n, g, ident_i, cmap(idb, [(c + 1) % 5 for c in range(5)]))
        return {"gens": [P1, P2, mw, tb, tc], "group_of": group_of, "groups": groups,
                "res": {"C3xC3": [P1, mw], "C3": [P1], "C3coord": [mw],
                        "C3diag": [tuple(P1[mw[x]] for x in range(v))],
                        "C3anti": [tuple(P1[mw[mw[x]]] for x in range(v))], "1": []}}
    if name in ("A4xPSL19", "V4xPSL19", "A4x19:9", "A4x19:3"):
        assert g == 20
        INF = 19
        def mob(a, b, c, d):  # y -> (a y + b)/(c y + d) on PG(1,19), index 19 = infinity
            def f(y):
                if y == INF:
                    return INF if c % 19 == 0 else (a * pow(c, 17, 19)) % 19
                num, den = (a * y + b) % 19, (c * y + d) % 19
                return INF if den == 0 else (num * pow(den, 17, 19)) % 19
            return [f(y) for y in range(g)]
        t = _perm_from_maps(n, g, ident_i, mob(1, 1, 0, 1))
        m4 = _perm_from_maps(n, g, ident_i, mob(4, 0, 0, 1))
        m7 = _perm_from_maps(n, g, ident_i, mob(7, 0, 0, 1))
        j = _perm_from_maps(n, g, ident_i, mob(0, 18, 1, 0))
        V2 = _perm_from_maps(n, g, [2, 3, 0, 1], ident_c)
        m4c = tuple(m4[m4[m4[x]]] for x in range(v))          # y -> 7y (order 3)
        a_m4 = tuple(P1[m4[x]] for x in range(v))             # pi1 * m4 (order 9)
        if name == "A4xPSL19":
            gens, reps = [P1, P2, t, m4, j], [(0, INF)]
            res = {"C3xC9": [P1, m4], "C9": [m4], "C9tw": [a_m4], "C3c": [m4c], "C3": [P1], "1": []}
        elif name == "V4xPSL19":
            gens, reps = [P2, V2, t, m4, j], [(0, INF)]
            res = {"C9": [m4], "C3c": [m4c], "1": []}
        elif name == "A4x19:9":
            gens, reps = [P1, P2, t, m4], [(0, INF), (INF, 0)]
            res = {"C3xC9": [P1, m4], "C9": [m4], "C9tw": [a_m4], "C3c": [m4c], "C3": [P1], "1": []}
        else:
            gens, reps = [P1, P2, t, m7], [(0, INF), (INF, 0)]
            res = {"C3xC3": [P1, m7], "C3": [P1], "C3coord": [m7], "C3c": [m7], "1": []}
        # reps: (x, anchor h) as labels inside group 0 (label = coordinate index there)
        return {"gens": gens, "group_of": group_of, "groups": groups, "res": res, "reps": reps}
    if name in ("A4xV4xA5", "A4xZ4xA5"):
        # coordinates a = 5u + c, u in {0..3} (V4 by XOR, or Z4), c in {0..4} (A5 points 1..5)
        assert g == 20
        def cmap(fu, fc):
            return [5 * fu[a // 5] + fc[a % 5] for a in range(g)]
        idu, idc = list(range(4)), list(range(5))
        c5 = _perm_from_maps(n, g, ident_i, cmap(idu, [1, 2, 3, 4, 0]))
        h3 = _perm_from_maps(n, g, ident_i, cmap(idu, [1, 2, 0, 3, 4]))   # (0 1 2): fixes c = 3, 4
        if name == "A4xV4xA5":
            us = [_perm_from_maps(n, g, ident_i, cmap([u ^ 1 for u in range(4)], idc)),
                  _perm_from_maps(n, g, ident_i, cmap([u ^ 2 for u in range(4)], idc))]
        else:
            us = [_perm_from_maps(n, g, ident_i, cmap([(u + 1) % 4 for u in range(4)], idc))]
        gens = [P1, P2] + us + [c5, h3]
        res = {"C3xC3": [P1, h3], "C3": [P1], "C3h": [h3],
               "C3diag": [tuple(P1[h3[x]] for x in range(v))],
               "C3anti": [tuple(P1[h3[h3[x]]] for x in range(v))], "1": []}
        return {"gens": gens, "group_of": group_of, "groups": groups, "res": res, "reps": [(4, 3)]}
    if name == "S4xC":
        # AGL(2,2) = S4 on the group index (F4 labels) x C_g; phi = Frobenius w <-> w^2 (fixes labels 0, 1)
        tau = _perm_from_maps(n, g, ident_i, [(a + 1) % g for a in range(g)])
        Phi = _perm_from_maps(n, g, [0, 1, 3, 2], ident_c)
        return {"gens": [P1, P2, Phi, tau], "group_of": group_of, "groups": groups,
                "res": {"S3": [P1, Phi], "C3": [P1], "C2": [Phi], "1": []}}
    if name in ("A4xE", "A4xEA", "A4xEAB"):
        # gcdcqs32 lane README §3: coordinates a in F2^m (m-bit integers, XOR), g = 2^m; A4 on labels;
        # translations a -> a ^ e (e = 1, 2, 4, ...) in every group.  A (m = 5): (b0,b1,b2,b3,b4) ->
        # (b0,b1,b2,b4,b3^b4), order 3, Fix(A) = {0..7}; B: same map on the bit pair (b1, b2),
        # Fix(B) = {a : b1 = b2 = 0}; A and B commute (AB fixes only {0, 1}).
        m = g.bit_length() - 1
        assert g == 1 << m
        trans = [_perm_from_maps(n, g, ident_i, [a ^ (1 << j) for a in range(g)]) for j in range(m)]
        gens, res = [P1, P2] + trans, {"C3": [P1], "1": []}
        if name != "A4xE":
            assert m == 5
            def pair_map(a, lo):  # (b_lo, b_lo+1) -> (b_lo+1, b_lo ^ b_lo+1)
                x, y = (a >> lo) & 1, (a >> (lo + 1)) & 1
                return (a & ~(3 << lo)) | (y << lo) | ((x ^ y) << (lo + 1))
            A = _perm_from_maps(n, g, ident_i, [pair_map(a, 3) for a in range(g)])
            gens = gens + [A]
            res.update({"C3xC3": [P1, A], "C3A": [A]})
            if name == "A4xEAB":
                B = _perm_from_maps(n, g, ident_i, [pair_map(a, 1) for a in range(g)])
                gens = gens + [B]
                res.update({"C3xC3B": [P1, B], "C3B": [B]})
        return {"gens": gens, "group_of": group_of, "groups": groups, "res": res, "reps": [(0, 1)]}
    if name == "A4xES":
        # gcdcqs32 README E3d: A4 (labels) x| (F2^5 diagonal translations x shears), g = 32.  Shear S_psi:
        # (i, a) -> (i, a ^ psi(i)) with psi in {0, id, w*, w^2*} : F4 -> F2^2 (bits 0, 1) additive and
        # injective; S_id generates the shear V4 under conjugation by pi1.  Order 1536, transitive;
        # Stab((0,0)) = <pi1, S_id> = A4, fixing G0 pointwise (every element fixes the hole).
        assert g == 32
        trans = [_perm_from_maps(n, g, ident_i, [a ^ (1 << j) for a in range(g)]) for j in range(5)]
        S_id = tuple(g * i + (a ^ i) for i in range(n) for a in range(g))
        gens = [P1, P2] + trans + [S_id]
        return {"gens": gens, "group_of": group_of, "groups": groups,
                "res": {"A4": [P1, S_id], "C3": [P1], "V4": [S_id, tuple(P1[S_id[P1[P1[x]]]] for x in range(v))],
                        "1": []}, "reps": [(0, 1)]}
    if name == "A4xET":
        # gcdcqs32 README E3e: A4 x (F2^5 x| <mu>), mu the transvection a -> a ^ (b4(a) * 1) (flip bit 0 when
        # bit 4 is set), Fix(mu) = {0..15}; order 768, Stab((0,0)) = <pi1> x <mu> = C6; anchor (0,1) fixed.
        assert g == 32
        trans = [_perm_from_maps(n, g, ident_i, [a ^ (1 << j) for a in range(g)]) for j in range(5)]
        MU = _perm_from_maps(n, g, ident_i, [a ^ ((a >> 4) & 1) for a in range(g)])
        return {"gens": [P1, P2] + trans + [MU], "group_of": group_of, "groups": groups,
                "res": {"C6": [P1, MU], "C3": [P1], "C2mu": [MU], "1": []}, "reps": [(0, 1)]}
    if name.startswith("A4xP"):
        # gcdcqs32 README E7: A4 x (C_{m1} x ... x C_{mr}) on mixed-radix coordinates, e.g. "A4xP4.8"
        # (C4 x C8), "A4xP2.16", "A4xP2.2.8"; translations by the unit vectors in every group.
        mods = [int(z) for z in name[len("A4xP"):].split(".")]
        prod = 1
        for mm in mods:
            prod *= mm
        assert prod == g

        def digits(a):
            out = []
            for mm in mods:
                out.append(a % mm)
                a //= mm
            return out

        def number(ds):
            a, mul = 0, 1
            for d, mm in zip(ds, mods):
                a += d * mul
                mul *= mm
            return a

        trans = []
        for j in range(len(mods)):
            def tj(a, j=j):
                ds = digits(a)
                ds[j] = (ds[j] + 1) % mods[j]
                return number(ds)
            trans.append(_perm_from_maps(n, g, ident_i, [tj(a) for a in range(g)]))
        return {"gens": [P1, P2] + trans, "group_of": group_of, "groups": groups,
                "res": {"C3": [P1], "1": []}, "reps": [(0, 1)]}
    if name == "A4xC8E2M":
        # gcdcqs32 README E9a: coordinates a = m + 8c (m in C8 master coordinate, c in F2^2 copy, XOR);
        # A4 labels x (C8 x F2^2) x| <M>, M: c -> w*c on copies (order 3, fixes copy 0 = the master copy).
        assert g == 32
        tm = _perm_from_maps(n, g, ident_i, [((a % 8 + 1) % 8) + 8 * (a // 8) for a in range(g)])
        t1 = _perm_from_maps(n, g, ident_i, [a ^ 8 for a in range(g)])
        t2 = _perm_from_maps(n, g, ident_i, [a ^ 16 for a in range(g)])
        wmul = [0, 2, 3, 1]
        MC = _perm_from_maps(n, g, ident_i, [a % 8 + 8 * wmul[a // 8] for a in range(g)])
        return {"gens": [P1, P2, tm, t1, t2, MC], "group_of": group_of, "groups": groups,
                "res": {"C3M": [MC], "C3": [P1], "1": []}, "reps": [(0, 1)]}
    if name.startswith("A4xCm"):
        # A4 x (C_g x| <m>), coordinates a -> m*a (mod g); x = (0,0), anchor (0, h) fixed by m
        mult = int(name[len("A4xCm"):])
        tau = _perm_from_maps(n, g, ident_i, [(a + 1) % g for a in range(g)])
        M = _perm_from_maps(n, g, ident_i, [(mult * a) % g for a in range(g)])
        hh = next(a for a in range(1, g) if (mult * a) % g == a) if any((mult * a) % g == a for a in range(1, g)) else 1
        return {"gens": [P1, P2, tau, M], "group_of": group_of, "groups": groups,
                "res": {"C3": [P1], "C3xCm": [P1, M], "Cm": [M], "1": []}, "reps": [(0, hh)]}
    raise ValueError(name)
