#!/usr/bin/env python3
"""wh10_exact_v1: EXACT stdlib probe for the WH_d single-orbit ansatz (lane note evidence/wh10-reduction-v1.md, sha256
7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8). Every DECISION is made in integer cyclotomic arithmetic
(elements of Z[zeta_N] as integer coefficient vectors; zero test = remainder modulo the cyclotomic polynomial Phi_N).
Floats are used only as a SCREEN whose margins are proved (see part E) and every reported object is re-verified exactly.

Part C (CRT identities, d = 10 and d = 6): Z_d -> Z_2 (x) Z_p^r as an exponent identity; the eigen-equation of
  f_k(t) = zeta_(2d)^(-t^2) omega^(-kt) for U = X Z^-1; f_k equals (ray by ray) g_j(t mod 2) h_b(t mod p) with g_j the
  sigma_y eigenvectors (1, -+i) and h_b the Gauss eigenvectors of X_p Z_p^r'; the map k -> (j, b) is a bijection.
Part A (anchors): odd d in {5, 7, 9}, x_t = zeta_d^(a t^2 + b t) for every valid a and b in {0, 1}: all 3d lines of the
  d x d configuration q_ij = X^i Z^j x orthogonal (exact), exact distinct-ray count (parallel iff |<q,q'>|^2 = |q|^2|q'|^2);
  mutation control (exponent of x_0 changed by 1) must break orthogonality. d = 10 relaxed anchors (N = 20): Chu
  zeta_20^(t^2), the constant vector, e_0: which line families are orthogonal, and the exact CRT Bloch components of M^* M
  (prediction W9: zero components exactly on the axes paired with the satisfied families).
Part E (exhaustive CAZAC enumeration over mu_N, (d, p, N) in {(10, 5, 20), (6, 3, 12)}, h_0 = 1): CRT split h <-> (b_0, b_1);
  X-flatness <=> for every m: |B_0(m)|^2 + |B_1(m)|^2 = d and Re(B_0(m) conj B_1(m)) = 0 (B_j(m) = sum_s b_j(s) zeta_p^(ms)).
  (i) B_0 without zero: B_1(m) = +-i (B_0(m)/|B_0(m)|) sqrt(d - |B_0(m)|^2), so b_1 is one of 2^p candidates; (ii) zeros on
  both sides: b_0, b_1 in c mu_p^p (a p-term vanishing sum in mu_N, N = 4p, is a rotated regular p-gon), enumerated
  directly; (iii) zero only in B_0: covered by the shift t -> t + p (swaps b_0, b_1) inside the closure under all D_w.
  Margins: a nonzero |B(m)|^2 is a totally positive algebraic integer of degree <= 4 (N = 20) or <= 2 (N = 12) with
  conjugates <= p^2, hence >= p^(-6) > 1e-7; exact solutions are reproduced to ~1e-13 and all float tolerances are 1e-7.
  Every candidate is verified EXACTLY; the closure under D_w (d^2 maps) is verified exactly element by element.
  Controls: the Chu set {zeta_N^(a t^2) omega^(b t): gcd(a, N) = 1} must be contained in the result; for d = 6 an
  independent brute force over all of mu_12^6 (h_0 = 1) must give the same set. Tests on the result: condition (iii) of the
  note (|sum_t zeta_N^(t^2) omega^(kt) h_t|^2 = d for all k: the WH single-orbit condition), the twisted control
  zeta_N^(2 t^2) (must accept some Chu sequences), and the predicted Re <b_0, b_1> = 0 (W9) for every CAZAC.
Standard library only; budget 270 s (checked between units); output JSON (exclusive) argv[1].
"""
import cmath, itertools, json, math, sys, time

T0 = time.monotonic()
BUDGET = 270.0
OUT = sys.argv[1]
TOL = 1e-7


def over():
    return time.monotonic() - T0 > BUDGET


# ---------------------------------------------------------------- integer polynomial / cyclotomic arithmetic
def pdiv_exact(a, b):
    a = list(a)
    db = len(b) - 1
    q = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    if any(a[:db]):
        raise ValueError("inexact division")
    return q


def premainder(a, b):
    a = list(a)
    db = len(b) - 1
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    return a[:db]


CYC = {}


def cyclo(n):
    if n not in CYC:
        num = [-1] + [0] * (n - 1) + [1]
        for dd in range(1, n):
            if n % dd == 0:
                num = pdiv_exact(num, cyclo(dd))
        CYC[n] = num
    return CYC[n]


def is_zero(vec, N):
    return not any(premainder(vec, cyclo(N)))


def vec_from(pairs, N):
    v = [0] * N
    for e in pairs:
        v[e % N] += 1
    return v


def abs2_minus(v, N, c):
    w = [0] * N
    nz = [(k, x) for k, x in enumerate(v) if x]
    for i, xi in nz:
        for j, xj in nz:
            w[(i - j) % N] += xi * xj
    w[0] -= c
    return w


def conj_vec(v, N):
    return [v[(-k) % N] for k in range(N)]


# ---------------------------------------------------------------- part C: CRT identities
def part_C():
    out = {}
    for (d, p, N, r_z, r_t, g0, g1) in ((10, 5, 20, 3, 2, 15, 5), (6, 3, 12, 2, 1, 9, 3)):
        q = N // p
        scale = N // d
        rec = {"d": d, "p": p}
        # Z_d = Z_2 (x) Z_p^r_z : omega^t = (-1)^(t mod 2) zeta_p^(r_z (t mod p))  <=>  t = (d/2)(t mod 2) + (d/p) r_z (t mod p) mod d
        rec["Z_identity"] = all((t - (d // 2) * (t % 2) - (d // p) * r_z * (t % p)) % d == 0 for t in range(d))
        rec["X_identity"] = len({(t % 2, t % p) for t in range(d)}) == d and all(
            ((t + 1) % 2, (t + 1) % p) == ((t % 2 + 1) % 2, (t % p + 1) % p) for t in range(d))

        def fexp(k, t):
            return (-(t * t) - scale * k * t) % N
        # eigen-equation (U f)(t+1) = omega^-t f(t) = lambda f(t+1), cyclically
        eig = True
        for k in range(d):
            cs = {(fexp(k, t) - scale * t - fexp(k, (t + 1) % d)) % N for t in range(d)}
            eig = eig and len(cs) == 1
        rec["f_k_eigen_equation"] = eig
        # g_j eigenvectors of X_2 Z_2: (X2 Z2 g)(t2 + 1) = (-1)^t2 g(t2)
        half = N // 2
        geig = True
        for gexp in ((0, g0), (0, g1)):
            cs = {(gexp[t2] + half * t2 - gexp[(t2 + 1) % 2]) % N for t2 in range(2)}
            geig = geig and len(cs) == 1
        rec["g_sigma_y_eigen"] = geig
        # Gauss vectors h_b(s) = zeta_p^(a s^2 + b s) with 2a = r_t mod p are eigenvectors of X_p Z_p^r_t
        a_g = next(a for a in range(1, p) if (2 * a - r_t) % p == 0)

        def hexp(b, s):
            return (q * (a_g * s * s + b * s)) % N
        heig = True
        for b in range(p):
            cs = {(hexp(b, s) + q * r_t * s - hexp(b, (s + 1) % p)) % N for s in range(p)}
            heig = heig and len(cs) == 1
        rec["h_gauss_eigen_X_p_Z_p^r"] = {"r": r_t, "a": a_g, "ok": heig}
        match = {}
        for k in range(d):
            hits = []
            for j, gexp in ((0, (0, g0)), (1, (0, g1))):
                for b in range(p):
                    c = fexp(k, 0) % N
                    if all((fexp(k, t) - c - gexp[t % 2] - hexp(b, t % p)) % N == 0 for t in range(d)):
                        hits.append((j, b))
            match[k] = hits
        rec["f_k_product_match"] = {str(k): v for k, v in match.items()}
        rec["product_bijection"] = all(len(v) == 1 for v in match.values()) and len({v[0] for v in match.values()}) == d
        out[str(d)] = rec
    return out


# ---------------------------------------------------------------- part A: anchors
def configuration(xexp, d, N, scale):
    cells = {}
    for i in range(d):
        for j in range(d):
            cells[(i, j)] = {(t + i) % d: (e + scale * j * t) % N for t, e in xexp.items()}
    return cells


def inner_vec(q1, q2, N):
    v = [0] * N
    for t, e in q1.items():
        if t in q2:
            v[(q2[t] - e) % N] += 1
    return v


def families(d):
    rows = [[(i, j) for j in range(d)] for i in range(d)]
    cols = [[(i, j) for i in range(d)] for j in range(d)]
    cls = [[(i, (s - i) % d) for i in range(d)] for s in range(d)]
    return {"rows": rows, "columns": cols, "classes": cls}


def family_orthogonal(cells, lines, N):
    for L in lines:
        for x in range(len(L)):
            for y in range(x + 1, len(L)):
                if not is_zero(inner_vec(cells[L[x]], cells[L[y]], N), N):
                    return False
    return True


def ray_count(cells, N):
    keys = list(cells)
    parent = {k: k for k in keys}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for x in range(len(keys)):
        for y in range(x + 1, len(keys)):
            a, b = keys[x], keys[y]
            if find(a) == find(b):
                continue
            n1, n2 = len(cells[a]), len(cells[b])
            if is_zero(abs2_minus(inner_vec(cells[a], cells[b], N), N, n1 * n2), N):
                parent[find(a)] = find(b)
    return len({find(k) for k in keys})


def bloch_exact(xexp, d, p, N):
    b = {0: {}, 1: {}}
    for t, e in xexp.items():
        b[t % 2][t % p] = e
    v = [0] * N
    for s, e in b[0].items():
        if s in b[1]:
            v[(b[1][s] - e) % N] += 1
    cv = conj_vec(v, N)
    return {"z_component_zero": len(b[0]) == len(b[1]),
            "x_component_zero(Re rho01 = 0)": is_zero([v[k] + cv[k] for k in range(N)], N),
            "y_component_zero(Im rho01 = 0)": is_zero([v[k] - cv[k] for k in range(N)], N)}


def part_A():
    out = {"odd": [], "d10_relaxed": []}
    valid = {5: [1, 3, 4], 7: [1, 2, 4, 5, 6], 9: [2, 5, 8]}
    for d in (5, 7, 9):
        for a in valid[d]:
            assert math.gcd(2 * a, d) == 1 and math.gcd(2 * a + 1, d) == 1
            for b in (0, 1):
                if over():
                    out["odd"].append({"d": d, "a": a, "b": b, "status": "SKIPPED_BUDGET"})
                    continue
                xexp = {t: (a * t * t + b * t) % d for t in range(d)}
                cells = configuration(xexp, d, d, 1)
                fam = families(d)
                orth = {k: family_orthogonal(cells, L, d) for k, L in fam.items()}
                rays = ray_count(cells, d)
                mut = dict(xexp)
                mut[0] = (mut[0] + 1) % d
                mcells = configuration(mut, d, d, 1)
                morth = {k: family_orthogonal(mcells, L, d) for k, L in fam.items()}
                out["odd"].append({"d": d, "a": a, "b": b, "orthogonal": orth, "rays": rays,
                                   "mutation_orthogonal": morth})
    d, p, N = 10, 5, 20
    anchors = (("chu_zeta20^(t^2)", {t: (t * t) % N for t in range(d)}, ("rows", "columns")),
               ("constant", {t: 0 for t in range(d)}, ("rows", "classes")),
               ("e_0", {0: 0}, ("columns", "classes")))
    for name, xexp, expect in anchors:
        cells = configuration(xexp, d, N, 2)
        fam = families(d)
        orth = {k: family_orthogonal(cells, L, N) for k, L in fam.items()}
        out["d10_relaxed"].append({"anchor": name, "expected_orthogonal_families": list(expect), "orthogonal": orth,
                                   "bloch": bloch_exact(xexp, d, p, N)})
    return out


# ---------------------------------------------------------------- part E: exhaustive CAZAC enumeration over mu_N
def cazac_exact(h, d, N, scale):
    for k in range(d):
        if not is_zero(abs2_minus(vec_from([(h[t] - scale * k * t) for t in range(d)], N), N, d), N):
            return False
    return True


def chirp_test(h, d, N, scale, mult):
    for k in range(d):
        if not is_zero(abs2_minus(vec_from([(mult * t * t + scale * k * t + h[t]) for t in range(d)], N), N, d), N):
            return False
    return True


def re_b0b1_zero(h, d, p, N):
    v = [0] * N
    for s in range(p):
        t0 = next(t for t in range(d) if t % 2 == 0 and t % p == s)
        t1 = next(t for t in range(d) if t % 2 == 1 and t % p == s)
        v[(h[t1] - h[t0]) % N] += 1
    cv = conj_vec(v, N)
    return is_zero([v[k] + cv[k] for k in range(N)], N)


def act(h, a, c, d, N, scale):
    e = [0] * d
    for t in range(d):
        src = (t - a) % d
        e[t] = (h[src] + scale * c * src) % N
    e0 = e[0]
    return tuple((x - e0) % N for x in e)


def part_E(d, p, N, brute):
    q = N // p
    scale = N // d
    zf = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
    crt = {(t % 2, t % p): t for t in range(d)}
    st = {"b0_total": 0, "b0_rejected_modulus": 0, "b0_with_dft_zero": 0, "b0_passed": 0, "candidates_main": 0,
          "zero_class_b0": 0, "zero_class_b1": 0, "candidates_zero_pairs": 0}
    found = set()

    def to_h(b0, b1):
        h = [0] * d
        for s in range(p):
            h[crt[(0, s)]] = b0[s]
            h[crt[(1, s)]] = b1[s]
        return tuple(h)

    def dft(bexp):
        return [sum(zf[(bexp[s] + q * m * s) % N] for s in range(p)) for m in range(p)]
    status = "COMPLETED"
    for rest in itertools.product(range(N), repeat=p - 1):
        st["b0_total"] += 1
        if st["b0_total"] % 4096 == 0 and over():
            status = "BUDGET"
            break
        b0 = (0,) + rest
        B0 = dft(b0)
        mods = [B.real * B.real + B.imag * B.imag for B in B0]
        if max(mods) > d + TOL:
            st["b0_rejected_modulus"] += 1
            continue
        if min(mods) < TOL:
            st["b0_with_dft_zero"] += 1
            continue
        st["b0_passed"] += 1
        G = []
        for m in range(p):
            gam = 1j * B0[m] / math.sqrt(mods[m]) * math.sqrt(max(0.0, d - mods[m]))
            G.append([gam * zf[(-q * m * s) % N] / p for s in range(p)])
        for signs in itertools.product((1.0, -1.0), repeat=p):
            b1 = []
            for s in range(p):
                v = 0j
                for m in range(p):
                    v += signs[m] * G[m][s]
                if abs(abs(v) - 1.0) > TOL:
                    break
                e = int(round(cmath.phase(v) * N / (2 * math.pi))) % N
                if abs(v - zf[e]) > TOL:
                    break
                b1.append(e)
            if len(b1) == p:
                found.add(to_h(b0, tuple(b1)))
                st["candidates_main"] += 1
    zero0, zero1 = [], []
    for rest in itertools.product(range(p), repeat=p - 1):
        b0 = (0,) + tuple(q * x for x in rest)
        B0 = dft(b0)
        if min(abs(B) ** 2 for B in B0) < TOL:
            zero0.append((b0, B0))
    for c in range(q):
        for sig in itertools.product(range(p), repeat=p):
            b1 = tuple((c + q * x) % N for x in sig)
            B1 = dft(b1)
            if min(abs(B) ** 2 for B in B1) < TOL:
                zero1.append((b1, B1))
    st["zero_class_b0"], st["zero_class_b1"] = len(zero0), len(zero1)
    for b0, B0 in zero0:
        for b1, B1 in zero1:
            if all(abs(abs(B0[m]) ** 2 + abs(B1[m]) ** 2 - d) < TOL and abs((B0[m] * B1[m].conjugate()).real) < TOL
                   for m in range(p)):
                found.add(to_h(b0, b1))
                st["candidates_zero_pairs"] += 1
    exact_found = sorted(h for h in found if cazac_exact(h, d, N, scale))
    st["found_distinct"], st["found_exact"] = len(found), len(exact_found)
    closed = set()
    for h in exact_found:
        for a in range(d):
            for c in range(d):
                closed.add(act(h, a, c, d, N, scale))
    C = sorted(closed)
    closure_exact = all(cazac_exact(h, d, N, scale) for h in C)
    chu = sorted({tuple((a * t * t + scale * b * t) % N for t in range(d)) for a in range(N) if math.gcd(a, N) == 1
                  for b in range(d)})
    chu_set, C_set = set(chu), set(C)
    res = {"d": d, "p": p, "N": N, "status": status, "stats": st, "cazac_count_h0_1": len(C),
           "closure_all_exact_cazac": closure_exact, "chu_count": len(chu), "chu_subset": chu_set <= C_set,
           "non_chu": [list(h) for h in C if h not in chu_set],
           "wh_condition_iii_pass": [list(h) for h in C if chirp_test(h, d, N, scale, 1)],
           "twisted_control_2t2_pass_count": sum(1 for h in C if chirp_test(h, d, N, scale, 2)),
           "re_b0b1_zero_all": all(re_b0b1_zero(h, d, p, N) for h in C)}
    if brute:
        bf, tested = set(), 0
        for rest in itertools.product(range(N), repeat=d - 1):
            tested += 1
            h = (0,) + rest
            ok = True
            for k in range(d):
                S = 0j
                for t in range(d):
                    S += zf[(h[t] - scale * k * t) % N]
                if abs(S.real * S.real + S.imag * S.imag - d) > TOL:
                    ok = False
                    break
            if ok and cazac_exact(h, d, N, scale):
                bf.add(h)
        res["brute_force"] = {"sequences_tested": tested, "cazac_count": len(bf), "equal_to_crt_method": bf == C_set}
    res["elapsed_s"] = round(time.monotonic() - T0, 3)
    return res, C


out = {"probe": "wh10_exact_v1", "arithmetic": "integer cyclotomic (exact decisions); floats only as proved screens"}
out["part_C"] = part_C()
out["part_A"] = part_A()
out["part_E_d6"], C6 = part_E(6, 3, 12, True)
out["part_E_d10"], C10 = part_E(10, 5, 20, False)
out["cazacs_d10_exponents_mod20"] = [list(h) for h in C10]
out["cazacs_d6_exponents_mod12"] = [list(h) for h in C6]
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
summ = {"C": {d: {k: v for k, v in r.items() if k != "f_k_product_match"} for d, r in out["part_C"].items()},
        "A_odd": [(r["d"], r["a"], r["b"], r.get("orthogonal"), r.get("rays"), r.get("mutation_orthogonal")) for r in out["part_A"]["odd"]],
        "A_d10": out["part_A"]["d10_relaxed"]}
for key in ("part_E_d6", "part_E_d10"):
    r = out[key]
    summ[key] = {k: r[k] for k in ("status", "stats", "cazac_count_h0_1", "closure_all_exact_cazac", "chu_count", "chu_subset",
                                   "twisted_control_2t2_pass_count", "re_b0b1_zero_all", "elapsed_s")}
    summ[key]["non_chu_count"] = len(r["non_chu"])
    summ[key]["wh_condition_iii_pass_count"] = len(r["wh_condition_iii_pass"])
    if "brute_force" in r:
        summ[key]["brute_force"] = r["brute_force"]
summ["elapsed_s"] = out["elapsed_s"]
print(json.dumps(summ))
