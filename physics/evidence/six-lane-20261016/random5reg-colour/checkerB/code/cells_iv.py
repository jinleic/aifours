#!/usr/bin/env python3
r"""Checker B, OUTER CELL TREES (exact rational bisection + mpmath.iv D-leaf bound).

Replays tree JSON files in the format of the task spec / README "FROZEN: outer cell certificate
scheme" (items 1-4).  Independence: written from README + format spec + primary preprint only;
no file under code/, outer/code/ or archive/ was read or imported.

What is verified for one tree (facet (fi, fj), u0 = 3 fi + fj):
  * root simplex: n* = (1/9)^4 and, for sigma in itertools.permutations(range(3)) with
    sigma[fi] != fj (4 of them, in that order), (sigma[0]==0, sigma[0]==1, sigma[1]==0,
    sigma[1]==1)/3; checked exactly: n^{u0} = 0 at the 4 facet points, and the 5 points are
    affinely independent.  (Cover: Delta is the affine image of (1/3) x Birkhoff polytope with
    n* interior; every point of Delta lies in conv(n*, F_u) for a facet F_u = Delta cap {n^u = 0},
    and F_u = conv{P_sigma/3 : sigma(i) != j} by Birkhoff-von Neumann.  So the 9 root simplices
    cover Delta; this script reports which facets the given files cover.)
  * preorder replay: ['S', i, j] replaces the current simplex by child 1 (vertex i -> exact
    midpoint of edge ij) then child 2 (vertex j -> midpoint); the two children cover the parent.
    The node list must be consumed exactly.
  * the tree's 'r0' must EQUAL the trusted constant r1 = 1/10000 (--trusted-r1; the radius
    certified by central_iv.py), else the tree is rejected.  ['C']: all 5 vertices satisfy
    |n_k - 1/9| <= r1 (exact; k = 00, 01, 10, 11), so the simplex lies in the central box
    (convexity), which central_iv.py covers minus n*.
  * ['D', y, mu0]: y (18) and mu0 (9 x 4) are float.hex strings read exactly.  For every vertex
    v: every n^u(v) >= 0 (else INVALID), and with z^u = C_u y,
       a_u := psi(m0) + <z^u, m0> + max_{s in S} <(1/2) ln m0 - ln mu0 + z^u, s - m0>,
       m0 := sum_s s w_s mu0^s / Phi(mu0),
       psi(m0) = (1/2) sum_k m0_k ln m0_k + ln Phi(mu0) - <ln mu0, m0>,
    U_y(v) := sum_u [n^u a_u + (3/2) n^u ln n^u] (terms with n^u = 0 vanish) must satisfy
    U_y(v) < L* := (5/2) ln 5 + ln(25/24) rigorously (iv upper bound < iv lower bound).
    Evaluated through the exact algebraic identity (g := (1/2) ln m0 - ln mu0 + z^u):
       psi(m0) + <z^u, m0> = ln Phi(mu0) + <g, m0>,  hence  a_u = ln Phi(mu0) + max_{s in S} <g, s>.
    The max over S equals the max over the candidate list CAND (the 8 vertices of conv(S) of
    Lemma 5.2), and CAND is verified at run time to be EXACTLY the vertex set of conv(S): every
    s in S is an exact convex combination of CAND, and every element of CAND is a spectrum exposed
    by an integer functional h (<h,v> > <h,s> for all other s in S).  Phi and mu_k dPhi/dmu_k
    use the closed form (7.7) and its derivatives,
    checked at run time to equal sum_s w_s mu^s and sum_s w_s s_k mu^s as polynomials (equality on
    the grid {0..5}^4; both sides have degree <= 5 in each variable).
    Soundness of the leaf test is rule 1 of the frozen scheme (weak pairing duality + per-class
    max-entropy + concavity of psi on conv(S) (README input lemma) + convexity of U_y in n, so the
    5 vertex values bound U_y on the simplex).  A positive mu0^u is required only for classes u
    with n^u > 0 at some vertex; other classes contribute 0.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
import platform
import resource
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cb_common as cb  # noqa: E402
import mpmath  # noqa: E402
from mpmath import iv, mp  # noqa: E402

THIRD, NINTH = Fr(1, 3), Fr(1, 9)


def float_down(m):
    """A float <= the mpf m (so printed margins stay lower bounds)."""
    f = float(m)
    if mp.mpf(f) > m:
        f = math.nextafter(f, -math.inf)
    return f


def lo(x):
    return mp.make_mpf(x._mpi_[0])


def hi(x):
    return mp.make_mpf(x._mpi_[1])


def ivq(x):
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


# ------------------------------------------------------------------ exact import-time checks
def phi_grad_closed(x, y, z, w):
    """(7.7) and mu_k * dPhi/dmu_k from it (generic ring elements: ints or iv intervals)."""
    s = x + y + z + w
    xy, xz, yw, zw = x + y, x + z, y + w, z + w

    def p4(t):
        t2 = t * t
        return t2 * t2
    s4, xy4, xz4, yw4, zw4 = p4(s), p4(xy), p4(xz), p4(yw), p4(zw)
    x4, y4, z4, w4 = p4(x), p4(y), p4(z), p4(w)
    phi = s4 * s - xy4 * xy - xz4 * xz - yw4 * yw - zw4 * zw + x4 * x + y4 * y + z4 * z + w4 * w
    mg = (5 * x * (s4 - xy4 - xz4 + x4), 5 * y * (s4 - xy4 - yw4 + y4),
          5 * z * (s4 - xz4 - zw4 + z4), 5 * w * (s4 - yw4 - zw4 + w4))
    return phi, mg


def check_closed_forms():
    for p in itertools.product(range(6), repeat=4):
        phi, mg = phi_grad_closed(*p)
        assert phi == cb.phi_sum(p)
        for k in range(4):
            assert mg[k] == sum(wt * s[k] * p[0] ** s[0] * p[1] ** s[1] * p[2] ** s[2] * p[3] ** s[3]
                                for s, wt in zip(cb.SPECTRA, cb.WEIGHT))
    return True


# Lemma 5.2 vertices (c = 1), k-order (x, y, z, w) = (s_{-1,-1}, s_{-1,1}, s_{1,-1}, s_{1,1})
LEMMA52 = [(1, 0, 0, 4), (0, 1, 1, 3), (0, 1, 4, 0), (1, 0, 3, 1),
           (0, 4, 1, 0), (1, 3, 0, 1), (4, 0, 0, 1), (3, 1, 1, 0)]


def convex_certificate():
    """Return CAND (subset of S) with an exact convex-combination certificate for every s in S."""
    cand = [v for v in LEMMA52]
    assert all(v in cb.SPECTRA for v in cand)
    cert = {}
    for s in cb.SPECTRA:
        found = None
        for sub in itertools.combinations(range(len(cand)), 4):
            # unknown lambda (4); equations: coordinates 0..2 and sum lambda = 1 (coordinate 3
            # then follows from sum = 5 for both sides)
            M = [[Fr(cand[v][k]) for v in sub] for k in range(3)] + [[Fr(1)] * 4]
            if cb.det(M) == 0:
                continue
            lam = [sum(row[c] * rhs for c, rhs in enumerate([Fr(s[0]), Fr(s[1]), Fr(s[2]), Fr(1)]))
                   for row in cb.inv(M)]
            if all(x >= 0 for x in lam):
                assert all(sum(lam[i] * cand[sub[i]][k] for i in range(4)) == s[k] for k in range(4))
                found = {sub[i]: lam[i] for i in range(4)}
                break
        if found is None:          # not expected; keep the max exact anyway
            cand.append(s)
            found = {len(cand) - 1: Fr(1)}
        cert[s] = found
    return cand, cert


def verify_vertex_set(cand):
    """Exact check that cand is EXACTLY the vertex set of conv(S): (a) every s in S is a convex
    combination of cand (convex_certificate), (b) every v in cand is exposed: some integer h has
    <h, v> > <h, s> for all s in S other than v."""
    assert sorted(cand) == sorted(LEMMA52), "fallback candidates were needed"
    witnesses = {}
    for v in cand:
        for h in itertools.product(range(-3, 4), repeat=4):
            hv = sum(a * b for a, b in zip(h, v))
            if all(sum(a * b for a, b in zip(h, s)) < hv for s in cb.SPECTRA if s != v):
                witnesses[v] = h
                break
        assert v in witnesses, f"{v} not certified as a vertex"
    return witnesses


# (u, k) -> (edge index e, sign of C_u[k][e]); every (u, k) is an end of exactly one edge
EDGE_OF = {}
for _e, (_u, _k, _v, _kv) in enumerate(cb.EDGES):
    EDGE_OF[(_u, _k)] = (_e, 1)
    EDGE_OF[(_v, _kv)] = (_e, -1)
assert len(EDGE_OF) == 36 and all(cb.CMAT[u][k][e] == sg for (u, k), (e, sg) in EDGE_OF.items())


# ------------------------------------------------------------------ replay
class Replayer:
    def __init__(self, cand, lstar_shift=Fr(0), trusted_r1=Fr(1, 10000)):
        self.cand = cand
        self.lstar = (iv.mpf(5) / 2) * iv.log(iv.mpf(5)) + iv.log(iv.mpf(25) / 24) - ivq(lstar_shift)
        self.lstar_lo = lo(self.lstar)
        self.trusted_r1 = trusted_r1
        self.nlnn = {}
        self.mucache = {}

    def nlogn15(self, n):
        v = self.nlnn.get(n)
        if v is None:
            nv = ivq(n)
            v = (iv.mpf(3) / 2) * nv * iv.log(nv)
            if len(self.nlnn) > 50000:      # bounded memory; values are recomputed on demand
                self.nlnn.clear()
            self.nlnn[n] = v
        return v

    def mu_part(self, mu):
        """(ln Phi(mu0), g0 = (1/2) ln m0 - ln mu0) for a 4-tuple of positive floats."""
        v = self.mucache.get(mu)
        if v is None:
            m = [iv.mpf(x) for x in mu]
            phi, mg = phi_grad_closed(*m)
            lphi = iv.log(phi)
            g0 = [iv.log(mg[k] / phi) / 2 - iv.log(m[k]) for k in range(4)]
            v = (lphi, g0)
            if len(self.mucache) > 50000:
                self.mucache.clear()
            self.mucache[mu] = v
        return v

    def a_u(self, mu, z):
        lphi, g0 = self.mu_part(mu)
        g = [g0[k] + z[k] for k in range(4)]
        best_lo = best_hi = None
        for s in self.cand:
            acc = None
            for k in range(4):
                if s[k]:
                    t = g[k] * s[k]
                    acc = t if acc is None else acc + t
            a, b = lo(acc), hi(acc)
            best_lo = a if best_lo is None or a > best_lo else best_lo
            best_hi = b if best_hi is None or b > best_hi else best_hi
        return lphi + iv.mpf([best_lo, best_hi])

    def dleaf(self, verts, node):
        if len(node) != 3 or len(node[1]) != 18 or len(node[2]) != 9 or any(len(r) != 4 for r in node[2]):
            return None, "malformed D node"
        try:
            yf = [float.fromhex(s) for s in node[1]]
            muf = [tuple(float.fromhex(s) for s in row) for row in node[2]]
        except (TypeError, ValueError):
            return None, "unparsable hex"
        if any(x != x or x in (float("inf"), float("-inf")) for x in yf + [t for r in muf for t in r]):
            return None, "non-finite entry"
        nvals = [cb.nine_values(v) for v in verts]
        if any(x < 0 for nv in nvals for x in nv):
            return None, "negative n^u at a vertex"
        active = [u for u in range(9) if any(nv[u] > 0 for nv in nvals)]
        au = {}
        for u in active:
            if any(x <= 0 for x in muf[u]):
                return None, f"mu0^{u} not positive"
            # z^u_k = (C_u y)_k = +-y_e: exact (float times +-1)
            z = [iv.mpf(EDGE_OF[(u, k)][1] * yf[EDGE_OF[(u, k)][0]]) for k in range(4)]
            au[u] = self.a_u(muf[u], z)
        worst = None
        for nv in nvals:
            U = iv.mpf(0)
            for u in active:
                n = nv[u]
                if n > 0:
                    U += ivq(n) * au[u] + self.nlogn15(n)
            margin = self.lstar - U
            m = lo(margin)
            worst = m if worst is None or m < worst else worst
        return worst, None

    def central_ok(self, verts):
        """C leaf: all 5 vertices in the box |n_k - 1/9| <= trusted r1 (k = 00, 01, 10, 11)."""
        return all(abs(v[k] - NINTH) <= self.trusted_r1 for v in verts for k in range(4))

    def replay(self, data, max_fail_report=10):
        t0 = time.time()
        fi, fj = data["facet"]
        r1 = Fr(data["r0"])
        u0 = 3 * fi + fj
        root = [(NINTH,) * 4]
        for sig in itertools.permutations(range(3)):
            if sig[fi] != fj:
                root.append(tuple(Fr(int(x), 3) for x in
                                  (sig[0] == 0, sig[0] == 1, sig[1] == 0, sig[1] == 1)))
        res = {"facet": [fi, fj], "r1": f"{r1.numerator}/{r1.denominator}", "nodes": 0, "S": 0, "D": 0,
               "C": 0, "failed_leaves": 0, "invalid_leaves": 0, "failures": [], "structure_error": None,
               "min_margin": None, "min_margin_leaf_index": None}
        assert len(root) == 5
        if not all(cb.nine_values(v)[u0] == 0 for v in root[1:]):
            res["structure_error"] = "root facet points not on n^u0 = 0"
        vol = cb.det([[v[k] - root[0][k] for k in range(4)] for v in root[1:]])
        if vol == 0:
            res["structure_error"] = "degenerate root simplex"
        if r1 != self.trusted_r1:
            res["structure_error"] = (f"tree r0 = {data['r0']} differs from the trusted constant "
                                      f"{self.trusted_r1} (radius certified by central_iv.py)")
        tree = data["tree"]
        pos, stack = 0, [root]
        leaf_index = 0
        while stack and res["structure_error"] is None:
            verts = stack.pop()
            if pos >= len(tree):
                res["structure_error"] = f"tree truncated (needed node {pos}, have {len(tree)})"
                break
            node = tree[pos]
            pos += 1
            kind = node[0] if isinstance(node, list) and node else None
            if kind == "S":
                if len(node) != 3 or node[1] not in range(5) or node[2] not in range(5) or node[1] == node[2]:
                    res["structure_error"] = f"bad S node at {pos - 1}: {node}"
                    break
                i, j = node[1], node[2]
                mid = tuple((a + b) / 2 for a, b in zip(verts[i], verts[j]))
                c1 = list(verts)
                c1[i] = mid
                c2 = list(verts)
                c2[j] = mid
                stack.append(c2)
                stack.append(c1)        # child 1 is processed first (preorder)
                res["S"] += 1
            elif kind == "C":
                res["C"] += 1
                if len(node) != 1 or not self.central_ok(verts):
                    res["failed_leaves"] += 1
                    if len(res["failures"]) < max_fail_report:
                        res["failures"].append({"leaf": leaf_index, "node": pos - 1, "why": "C leaf outside box"})
                leaf_index += 1
            elif kind == "D":
                res["D"] += 1
                m, why = self.dleaf(verts, node)
                if why is not None:
                    res["invalid_leaves"] += 1
                    res["failed_leaves"] += 1
                    if len(res["failures"]) < max_fail_report:
                        res["failures"].append({"leaf": leaf_index, "node": pos - 1, "why": why})
                else:
                    if res["min_margin"] is None or m < res["min_margin"]:
                        res["min_margin"], res["min_margin_leaf_index"] = m, leaf_index
                    if m <= 0:
                        res["failed_leaves"] += 1
                        if len(res["failures"]) < max_fail_report:
                            res["failures"].append({"leaf": leaf_index, "node": pos - 1,
                                                    "why": "U_y(v) < L* not certified",
                                                    "margin_lo": float_down(m)})
                leaf_index += 1
            else:
                res["structure_error"] = f"unknown node at {pos - 1}: {str(node)[:60]}"
                break
        if res["structure_error"] is None and pos != len(tree):
            res["structure_error"] = f"{len(tree) - pos} unconsumed trailing nodes"
        res["nodes"] = pos
        res["leaves"] = leaf_index
        res["PASS"] = (res["structure_error"] is None and res["failed_leaves"] == 0 and leaf_index > 0)
        if res["min_margin"] is not None:
            res["min_margin"] = float_down(res["min_margin"])   # iv lower endpoint of L* - U
        res["runtime_s"] = round(time.time() - t0, 2)
        return res


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("trees", nargs="+")
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--lstar-shift", default="0", help="test only: replace L* by L* - shift")
    ap.add_argument("--trusted-r1", default="1/10000",
                    help="radius of the central certificate; a tree's 'r0' must equal it exactly")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    assert a.prec >= 128
    iv.prec = a.prec
    mp.prec = a.prec
    t0 = time.time()
    assert cb.check_spectra() and check_closed_forms()
    cand, cert = convex_certificate()
    witnesses = verify_vertex_set(cand)
    rep = Replayer(cand, Fr(a.lstar_shift), Fr(a.trusted_r1))
    results = []
    for path in a.trees:
        with open(path) as f:
            data = json.load(f)
        r = rep.replay(data)
        r["file"] = path
        r["sha256"] = sha256(path)
        results.append(r)
        print(json.dumps({k: r[k] for k in ("file", "facet", "PASS", "nodes", "S", "D", "C", "leaves",
                                              "failed_leaves", "invalid_leaves", "structure_error",
                                              "min_margin", "runtime_s")}), flush=True)
    facets = sorted({tuple(r["facet"]) for r in results if r["PASS"]})
    out = {
        "checker": "B (mpmath.iv + fractions), outer cell trees",
        "params": {"iv_prec_bits": a.prec, "lstar_shift": a.lstar_shift, "trusted_r1": a.trusted_r1},
        "candidates_for_max_over_S": [list(s) for s in cand],
        "candidates_are_exactly_vertices_of_convS": {
            "every_spectrum_convex_combination": {",".join(map(str, s)): {",".join(map(str, cand[i])): str(l)
                                                                       for i, l in c.items()}
                                                  for s, c in cert.items()},
            "exposing_functional_per_candidate": {",".join(map(str, v)): list(h) for v, h in witnesses.items()}},
        "results": results,
        "ALL_PASS": all(r["PASS"] for r in results),
        "facets_passed": [list(f) for f in facets],
        "all_9_facets_covered": len(facets) == 9,
        "runtime_s": round(time.time() - t0, 2),
        "max_rss_MiB": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20, 1),
        "versions": {"python": sys.version.split()[0], "mpmath": mpmath.__version__,
                     "mpmath_backend": mpmath.libmp.BACKEND, "platform": platform.platform()},
        "script_sha256": {os.path.basename(p): sha256(p) for p in
                          (os.path.abspath(__file__),
                           os.path.join(os.path.dirname(os.path.abspath(__file__)), "cb_common.py"))},
    }
    if a.out:
        with open(a.out, "w") as f:
            f.write(json.dumps(out, indent=1) + "\n")
    print(json.dumps({"ALL_PASS": out["ALL_PASS"], "facets_passed": out["facets_passed"],
                      "runtime_s": out["runtime_s"], "max_rss_MiB": out["max_rss_MiB"]}))
    return 0 if out["ALL_PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())
