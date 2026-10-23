Self-tests passed at 128 and 200 bits; the separate validation harness passed 45 checks.

At 200 bits, both certificates passed with zero failed leaves:

- `base_cone00_r1_1over20.json`, using `--allow-r0 1/20`: **19,383 nodes**, 9,691 splits, 9,122 dual leaves, 570 central leaves; **6.589841 seconds**. Minimum-margin lower bound: `4.95259938059884678689092295522697720195837060082272860183311E-8`.
- `cone00.json`, requiring `r0=1/10000`: **67,079 nodes**, 33,539 splits, 33,032 dual leaves, 508 central leaves; **23.940698 seconds**. Minimum-margin lower bound: `1.72726858038650554297889643120399591920260765422683018961756E-11`.

No files were modified, no prohibited implementations were inspected, and no work was delegated.

BEGIN_CHECKER_C
#!/usr/bin/env python3
"""Independent, fail-closed certificate replay; requires python-flint.

All geometric and hexadecimal input arithmetic is exact fmpq arithmetic.
All logarithms, extrema and inequality decisions use Arb at --prec bits.
Preorder indices in diagnostics are zero based. A null margin means that
there were no dual vertices, or that not all dual margins could be computed.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, ROUND_FLOOR, localcontext
from functools import lru_cache
import hashlib
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import re
import sys

from flint import arb, ctx, fmpq

Q = fmpq
THIRD = Q(1, 3)
CENTER = (Q(1, 9),) * 4
REQUIRED_R0 = Q(1, 10000)
DIRECTIONS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
HEX = re.compile(
    r"([+-]?)0[xX]([0-9a-fA-F]+)\.([0-9a-fA-F]+)[pP]([+-]?[0-9]+)\Z"
)
RATIONAL = re.compile(r"([+-]?[0-9]+)/([+-]?[0-9]+)\Z")


class Invalid(ValueError):
    pass


def spectra():
    result = []
    for a in range(6):
        for b in range(6 - a):
            for c in range(6 - a - b):
                d = 5 - a - b - c
                if min(a + b, c + d, a + c, b + d) >= 1:
                    s = (a, b, c, d)
                    denominator = 1
                    for k in s:
                        denominator *= factorial(k)
                    result.append((s, 120 // denominator))
    return tuple(result)


def edges():
    used, result = set(), []
    for u in range(9):
        i, j = divmod(u, 3)
        for k, (r, t) in enumerate(DIRECTIONS):
            if (u, k) in used:
                continue
            v = 3 * ((i + r) % 3) + (j + t) % 3
            kv = DIRECTIONS.index((-r, -t))
            if (v, kv) in used:
                raise Invalid("edge construction reused an entry")
            result.append((u, k, v, kv))
            used.update(((u, k), (v, kv)))
    return tuple(result)


SPECTRA = spectra()
EDGES = edges()


def rational(text):
    if not isinstance(text, str):
        raise Invalid("r0 must be a P/Q string")
    m = RATIONAL.fullmatch(text)
    if m is None or int(m[2]) == 0:
        raise Invalid("invalid P/Q rational")
    return Q(int(m[1]), int(m[2]))


def hex_rational(text):
    """Parse the written binary rational, with no float conversion."""
    if not isinstance(text, str):
        raise Invalid("hexadecimal entry must be a string")
    m = HEX.fullmatch(text)
    if m is None:
        raise Invalid("invalid finite hexadecimal literal: " + repr(text)[:100])
    numerator = int(m[2] + m[3], 16)
    if m[1] == "-":
        numerator = -numerator
    exponent = int(m[4]) - 4 * len(m[3])
    if exponent >= 0:
        return Q(numerator << exponent)
    return Q(numerator, 1 << -exponent)


def facet_pair(value):
    if (not isinstance(value, list) or len(value) != 2
            or any(type(i) is not int or not 0 <= i < 3 for i in value)):
        raise Invalid("facet must be two integers in 0..2")
    return tuple(value)


def root_simplex(facet):
    fi, fj = facet
    vertices = [CENTER]
    for sigma in permutations(range(3)):
        if sigma[fi] != fj:
            vertices.append(tuple(
                THIRD * int(truth) for truth in (
                    sigma[0] == 0, sigma[0] == 1,
                    sigma[1] == 0, sigma[1] == 1
                )
            ))
    if len(vertices) != 5:
        raise Invalid("root construction did not produce five vertices")
    return tuple(vertices)


def class_values(p):
    x1, x2, x3, x4 = p
    return (
        x1, x2, THIRD - x1 - x2,
        x3, x4, THIRD - x3 - x4,
        THIRD - x1 - x3, THIRD - x2 - x4,
        x1 + x2 + x3 + x4 - THIRD
    )


def lower_decimal(value):
    """Round an exact dyadic lower endpoint DOWN when printing decimal."""
    value = value.lower()
    if not value.is_finite():
        return None
    m, e = (int(t) for t in value.man_exp())
    if e >= 0:
        return str(m << e)
    with localcontext() as dc:
        dc.prec = max(30, ctx.prec * 30103 // 100000)
        dc.rounding = ROUND_FLOOR
        return str(Decimal(m) / Decimal(1 << -e))


def a_bound(z, mu):
    """Enclose the specified a(z,mu), including the entire finite maximum."""
    powers = []
    for q in mu:
        row = [arb(1), arb(q)]
        for unused in range(2, 6):
            row.append(row[-1] * row[1])
        powers.append(row)
    phi = arb(0)
    moments = [arb(0) for unused in range(4)]
    for s, w in SPECTRA:
        term = arb(w)
        for k in range(4):
            if s[k]:
                term *= powers[k][s[k]]
        phi += term
        for k in range(4):
            if s[k]:
                moments[k] += s[k] * term
    if not (phi.is_finite() and phi > 0):
        raise Invalid("Phi is not certified finite and positive")
    means = [v / phi for v in moments]
    if any(not (v.is_finite() and v > 0) for v in means):
        raise Invalid("a moment is not certified finite and positive")
    g = [means[k].log() / 2 - arb(mu[k]).log() + z[k]
         for k in range(4)]
    # psi0 + z.m0 - g.m0 = log(Phi) exactly. No approximation
    # or assumed maximizer is used in this algebraic cancellation.
    maximum = None
    for s, unused in SPECTRA:
        score = arb(0)
        for k in range(4):
            if s[k]:
                score += s[k] * g[k]
        maximum = score if maximum is None else maximum.max(score)
    answer = phi.log() + maximum
    if not answer.is_finite():
        raise Invalid("nonfinite a(z,mu) enclosure")
    return answer


class Replay:
    def __init__(self, prec):
        self.prec = prec
        self.target = arb(5).log() * 5 / 2 + arb(Q(25, 24)).log()
        self.minimum = None
        self.complete_margins = True

        # Per-replay caches: never reuse balls computed at another precision.
        @lru_cache(maxsize=65536)
        def entropy_term(n):
            b = arb(n)
            return b * b.log() * 3 / 2

        @lru_cache(maxsize=65536)
        def vertex_data(p):
            active, entropy = [], arb(0)
            for u, n in enumerate(class_values(p)):
                if n < 0:
                    raise Invalid("vertex outside Delta: negative class " + str(u))
                if n > 0:
                    active.append((u, arb(n)))
                    entropy += entropy_term(n)
            return tuple(active), entropy

        self.vertex_data = vertex_data

    def dual_coefficients(self, node):
        if len(node) != 3:
            raise Invalid("D node must have exactly three fields")
        y, mus = node[1], node[2]
        if not isinstance(y, list) or len(y) != 18:
            raise Invalid("y must be a list of 18 hexadecimal strings")
        if (not isinstance(mus, list) or len(mus) != 9
                or any(not isinstance(row, list) or len(row) != 4
                       for row in mus)):
            raise Invalid("mus must be a 9 by 4 list")
        ys = [hex_rational(t) for t in y]
        qs = [[hex_rational(t) for t in row] for row in mus]
        if any(q <= 0 for row in qs for q in row):
            raise Invalid("every mu entry must be strictly positive")
        z = [[arb(0) for unused in range(4)] for unused in range(9)]
        for q, (u, k, v, kv) in zip(ys, EDGES):
            b = arb(q)
            z[u][k] += b
            z[v][kv] -= b
        return tuple(a_bound(z[u], qs[u]) for u in range(9))

    def margin(self, p, coefficients):
        active, total = self.vertex_data(p)
        for u, n in active:
            total += n * coefficients[u]
        margin = self.target - total
        if not margin.is_finite():
            raise Invalid("nonfinite vertex margin")
        lo = margin.lower()
        if self.minimum is None or lo < self.minimum:
            self.minimum = lo
        return margin

    def verify(self, document, required_r0=REQUIRED_R0, expect=None):
        stats = {
            "facet": None, "r0": None, "verdict": "FAIL",
            "nodes": 0, "splits": 0, "dual_leaves": 0,
            "central_leaves": 0, "failed_leaves": 0,
            "first_failures": [], "min_margin_lower_bound": None
        }
        bad = False

        def fail(index, kind, reason):
            nonlocal bad
            bad = True
            if len(stats["first_failures"]) < 10:
                stats["first_failures"].append([index, kind, reason])

        try:
            if not isinstance(document, dict):
                raise Invalid("top-level JSON must be an object")
            raw_r0 = document.get("r0")
            stats["r0"] = raw_r0 if isinstance(raw_r0, str) else None
            facet = facet_pair(document.get("facet"))
            stats["facet"] = list(facet)
            if expect is not None and facet != tuple(expect):
                raise Invalid("facet does not match --expect-facet")
            r0 = rational(document.get("r0"))
            if r0 != required_r0:
                raise Invalid("r0 must equal " + str(required_r0) + " exactly")
            tree = document.get("tree")
            if not isinstance(tree, list):
                raise Invalid("tree must be a list")
            stats["nodes"] = len(tree)
            stack = [root_simplex(facet)]
            index = 0
            structural_failure = False
            while stack:
                if index == len(tree):
                    fail(index, "tree", "truncated preorder: unfilled child slots")
                    structural_failure = True
                    break
                cell = stack.pop()
                node = tree[index]
                here = index
                index += 1
                if (not isinstance(node, list) or not node
                        or not isinstance(node[0], str)):
                    fail(here, "node", "node must be a nonempty list with a string kind")
                    structural_failure = True
                    break
                kind = node[0]
                if kind == "S":
                    if (len(node) != 3 or type(node[1]) is not int
                            or type(node[2]) is not int
                            or not 0 <= node[1] < 5
                            or not 0 <= node[2] < 5):
                        fail(here, kind, "split requires integer indices in 0..4")
                        structural_failure = True
                        break
                    stats["splits"] += 1
                    i, j = node[1:]
                    mid = tuple((a + b) / 2 for a, b in zip(cell[i], cell[j]))
                    first, second = list(cell), list(cell)
                    first[i], second[j] = mid, mid
                    # LIFO: first child must be visited before second child.
                    stack.append(tuple(second))
                    stack.append(tuple(first))
                elif kind == "C":
                    stats["central_leaves"] += 1
                    if len(node) != 1:
                        stats["failed_leaves"] += 1
                        fail(here, kind, "C node must have exactly one field")
                    elif any(abs(x - CENTER[k]) > r0
                             for p in cell for k, x in enumerate(p)):
                        stats["failed_leaves"] += 1
                        fail(here, kind, "a vertex is outside the closed central box")
                elif kind == "D":
                    stats["dual_leaves"] += 1
                    reasons = []
                    try:
                        coefficients = self.dual_coefficients(node)
                        for vi, p in enumerate(cell):
                            margin = self.margin(p, coefficients)
                            if not margin > 0:
                                reasons.append(
                                    "vertex " + str(vi)
                                    + ": L*-U is not rigorously positive"
                                    + " (lower bound " + lower_decimal(margin) + ")"
                                )
                    except (Invalid, ValueError, ArithmeticError, TypeError) as exc:
                        self.complete_margins = False
                        reasons.append(str(exc))
                    if reasons:
                        stats["failed_leaves"] += 1
                        fail(here, kind, "; ".join(reasons))
                else:
                    fail(here, kind, "unknown node kind")
                    structural_failure = True
                    break
            if structural_failure:
                self.complete_margins = False
            elif index != len(tree):
                fail(index, "tree", "trailing nodes after the root subtree")
                self.complete_margins = False
        except (Invalid, ValueError, ArithmeticError, TypeError) as exc:
            fail(-1, "metadata", str(exc))
            self.complete_margins = False
        if self.complete_margins and self.minimum is not None:
            stats["min_margin_lower_bound"] = lower_decimal(self.minimum)
        stats["verdict"] = "FAIL" if bad else "PASS"
        return stats


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise Invalid("duplicate JSON key: " + key)
        obj[key] = value
    return obj


def reject_constant(value):
    raise Invalid("nonstandard JSON constant: " + value)


def exact_phi_moments(mu):
    """Only used by selftest: an independent exact polynomial evaluation."""
    phi, moments = Q(0), [Q(0)] * 4
    for s, w in SPECTRA:
        term = Q(w)
        for k in range(4):
            term *= mu[k] ** s[k]
        phi += term
        for k in range(4):
            moments[k] += term * s[k]
    return phi, tuple(v / phi for v in moments)


def selftest(prec):
    checks = []

    def require(condition, name):
        if not condition:
            raise Invalid("selftest failed: " + name)
        checks.append(name)

    def close_zero(value):
        return value.contains(0) and abs(value) < arb(Q(1, 1 << (prec // 2)))

    require(len(SPECTRA) == 36, "36 spectra")
    entries = Counter((u, k) for e in EDGES
                      for u, k in ((e[0], e[1]), (e[2], e[3])))
    require(len(EDGES) == 18 and len(entries) == 36
            and set(entries) == {(u, k) for u in range(9) for k in range(4)}
            and all(v == 1 for v in entries.values()),
            "18 edges; every class entry used exactly once")
    one = (Q(1),) * 4
    phi, means = exact_phi_moments(one)
    require(phi == 900 and means == (Q(5, 4),) * 4,
            "exact Phi(1)=900 and all moments=5/4")
    require(all(sum(s) == 5 for s, unused in SPECTRA),
            "exact degree-five homogeneity")
    zeros = (arb(0),) * 4
    a = a_bound(zeros, one)
    expected_a = arb(Q(5, 4)).log() * 5 / 2 + arb(900).log()
    require(close_zero(a - expected_a),
            "a=(5/2)log(5/4)+log(900)")
    # These rational identities, equal moments and degree five give the
    # symbolic uniform-case equality, alongside the interval regressions.
    require(Q(900, 32 * 27) == Q(25, 24),
            "exact rational factor in U(center)=L*")
    replay = Replay(prec)
    margin = replay.margin(CENTER, (a,) * 9)
    require(close_zero(margin) and not margin > 0,
            "U(center)=L*; strict margin is rejected")
    uniform = ["D", ["0x0.0p+0"] * 18, [["0x1.0000000000000p+0"] * 4
                                     for unused in range(9)]]
    result = Replay(prec).verify(
        {"facet": [0, 0], "r0": "1/10000", "tree": [uniform]}
    )
    require(result["verdict"] == "FAIL" and result["failed_leaves"] == 1
            and "vertex 0:" in result["first_failures"][0][2],
            "dual root containing center is rejected")
    mu = (Q(3, 2), Q(5, 7), Q(11, 13), Q(17, 19))
    doubled = tuple(2 * q for q in mu)
    phi1, means1 = exact_phi_moments(mu)
    phi2, means2 = exact_phi_moments(doubled)
    require(phi2 == 32 * phi1 and means2 == means1,
            "exact Phi(2mu)=32Phi(mu), invariant moments")
    z = tuple(arb(q) for q in (Q(1, 7), Q(-2, 9), Q(3, 11), Q(-5, 13)))
    require(close_zero(a_bound(z, mu) - a_bound(z, doubled)),
            "a(z,2mu)=a(z,mu)")
    # Cross-check the cancellation against the unsimplified specification.
    m = tuple(arb(q) for q in means1)
    lm = tuple(arb(q).log() for q in mu)
    g = tuple(m[k].log() / 2 - lm[k] + z[k] for k in range(4))
    psi = arb(phi1).log()
    for k in range(4):
        psi += m[k] * m[k].log() / 2 - m[k] * lm[k]
    base = psi + sum((z[k] * m[k] for k in range(4)), arb(0))
    maximum = None
    for s, unused in SPECTRA:
        score = sum((g[k] * (s[k] - m[k]) for k in range(4)), arb(0))
        maximum = score if maximum is None else maximum.max(score)
    require(close_zero(a_bound(z, mu) - (base + maximum)),
            "simplified a agrees with the stated unsimplified formula")
    return {"verdict": "PASS", "selftest": True, "prec": prec,
            "checks": checks, "a_uniform": a.str(),
            "center_margin": margin.str()}


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Invalid(message)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def main(argv=None):
    started = utc_now()
    result = {
        "cert": None, "cert_sha256": None, "facet": None, "r0": None,
        "verdict": "FAIL", "nodes": 0, "splits": 0, "dual_leaves": 0,
        "central_leaves": 0, "failed_leaves": 0, "first_failures": [],
        "min_margin_lower_bound": None, "prec": 200, "started": started
    }
    try:
        parser = Parser(description=__doc__)
        parser.add_argument("cert", nargs="?")
        parser.add_argument("--expect-facet", nargs=2, type=int, metavar=("FI", "FJ"))
        parser.add_argument("--prec", type=int, default=200, metavar="BITS")
        parser.add_argument("--allow-r0", metavar="P/Q",
                            help="TEST ONLY: replace the required radius")
        parser.add_argument("--selftest", action="store_true")
        args = parser.parse_args(argv)
        result["cert"], result["prec"] = args.cert, args.prec
        if args.allow_r0 is not None:
            result["allow_r0"] = args.allow_r0
        if args.prec < 128:
            raise Invalid("--prec must be at least 128")
        ctx.prec = args.prec
        ctx.threads = 1
        if args.expect_facet is not None:
            facet_pair(args.expect_facet)
        required = REQUIRED_R0 if args.allow_r0 is None else rational(args.allow_r0)
        if required <= 0:
            raise Invalid("required radius must be positive")
        if args.selftest:
            if args.cert is not None or args.allow_r0 is not None or args.expect_facet:
                raise Invalid("--selftest cannot be combined with certificate options")
            result.update(selftest(args.prec))
        else:
            if args.cert is None:
                raise Invalid("a certificate path is required, or use --selftest")
            raw = Path(args.cert).read_bytes()
            result["cert_sha256"] = hashlib.sha256(raw).hexdigest()
            document = json.loads(raw, parse_float=Decimal,
                                  parse_constant=reject_constant,
                                  object_pairs_hook=unique_object)
            result.update(Replay(args.prec).verify(document, required, args.expect_facet))
    except Exception as exc:
        result["verdict"] = "FAIL"
        result["min_margin_lower_bound"] = None
        if len(result["first_failures"]) < 10:
            result["first_failures"].append([-1, "input", type(exc).__name__ + ": " + str(exc)])
    result["finished"] = utc_now()
    print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
END_CHECKER_C