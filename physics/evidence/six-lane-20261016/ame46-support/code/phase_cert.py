#!/usr/bin/env python3
"""phase_cert.py: explicit 2x2 phase-obstruction certificates in the parent's format. Lane ame46-support.

Certificate format: a list of entries {"sign": +1|-1, "k": k, "corners": [r1c1, r1c2, r2c1, r2c2]}.
- k is the reshaping: 0 = 12|34, 1 = 13|24, 2 = 14|23. Rows are the coordinate pair (0,1), (0,2) or (0,3), columns
  the complementary pair.
- Corners are 4-digit points (coordinates 1..4 written in order, values 0..5).
- Each entry stands for the form phi(r1c1) - phi(r1c2) - phi(r2c1) + phi(r2c2). For a genuine 2x2 component of the
  unitary, this form is congruent to pi mod 2*pi (L42-10).

Validity (verify_certificate, independent of phase_check.py):
 (a) the four corners lie in N, form a rectangle in reshaping k (rows r1 != r2, columns c1 != c2), and are a genuine
     component: each of the rows r1, r2 and the columns c1, c2 contains exactly two points of N;
 (b) the signed sum of the forms is the zero form;
 (c) the number of entries is odd.
Then summing the congruences gives 0 = (odd) * pi mod 2*pi, a contradiction.
extract_certificate(N) turns the left-kernel vector found by phase_check.phase_consistency into this format, with an
entry repeated |a| times for a coefficient a.
"""
import phase_check as pc

RESH = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def pt(x):
    return "".join(map(str, x))


def unpt(s):
    return tuple(int(c) for c in s)


def extract_certificate(N):
    eqs = pc.block_equations(set(N))
    elems = sorted({x for _, tt in eqs for x, _ in tt})
    ph = pc.phase_consistency(eqs, elems)
    if ph["complex_consistent"] or not ph.get("obstruction_verified"):
        return None
    cert = []
    for i, a in ph["obstruction"]:
        k, terms = eqs[i]
        corners = [pt(x) for x, _ in terms]            # order r1c1 (+), r1c2 (-), r2c1 (-), r2c2 (+)
        for _ in range(abs(a)):
            cert.append({"sign": 1 if a > 0 else -1, "k": k, "corners": corners})
    return cert


def verify_certificate(N, cert):
    """Returns (ok, reason). Independent of phase_check.py."""
    Nset = {tuple(x) if not isinstance(x, str) else unpt(x) for x in N}
    if not cert:
        return False, "empty certificate"
    if len(cert) % 2 != 1:
        return False, "even number of entries"
    total = {}
    for ent in cert:
        if ent.get("sign") not in (1, -1) or ent.get("k") not in (0, 1, 2) or len(ent.get("corners", [])) != 4:
            return False, "malformed entry"
        rows, cols = RESH[ent["k"]]
        P = [unpt(c) for c in ent["corners"]]
        if any(p not in Nset for p in P):
            return False, "corner not in N"
        row = lambda x: tuple(x[i] for i in rows)
        col = lambda x: tuple(x[i] for i in cols)
        a, b, c, d = P
        if not (row(a) == row(b) and row(c) == row(d) and col(a) == col(c) and col(b) == col(d)):
            return False, "corners do not form a rectangle"
        if row(a) == row(c) or col(a) == col(b):
            return False, "degenerate rectangle"
        for r in (row(a), row(c)):
            if sum(1 for x in Nset if row(x) == r) != 2:
                return False, "row %s does not contain exactly two points of N" % (r,)
        for cc in (col(a), col(b)):
            if sum(1 for x in Nset if col(x) == cc) != 2:
                return False, "column %s does not contain exactly two points of N" % (cc,)
        s = ent["sign"]
        for p, coef in ((a, 1), (b, -1), (c, -1), (d, 1)):
            total[p] = total.get(p, 0) + s * coef
    if any(v != 0 for v in total.values()):
        return False, "signed sum of forms is not zero"
    return True, "ok"


def counting_margin(prof, t, h):
    """Written counting argument for the classical completion. For x in T let c(x) = #{i : x_i in V_i}. Then
    sum 1 = t, sum c = 6*sum|V_i| - 4h, and sum C(c,2) = e2(|V|) - 6h, because every hole line lies in V_i x V_j and
    every other line holds exactly one officer. Since 1 - c + C(c,2) = (c-1)(c-2)/2 >= 0, it follows that
    sigma0 - sigma1 + sigma2 >= 0. Returns that margin; a negative value excludes the profile."""
    V = [len(p) for p in prof]
    s1 = 6 * sum(V) - 4 * h
    e2 = sum(V[i] * V[j] for i in range(4) for j in range(i + 1, 4))
    s2 = e2 - 6 * h
    return t - s1 + s2
