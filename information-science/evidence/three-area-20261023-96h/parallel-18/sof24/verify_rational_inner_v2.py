#!/usr/bin/env python3
"""Frozen exact coefficient/witness assay. Execute ONLY under a named parent GO.

Standard library only. This checks finite rational algebra, not the universal
geometric/open-neighborhood argument or novelty. No floating point is used in
scientific calculations; monotonic time only enforces the internal deadline.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import sys
import time

try:
    import resource
except ImportError:
    resource = None


@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def cast(x):
        return x if isinstance(x, QI) else QI(F(x), F(0))

    def __add__(self, other):
        q = self.cast(other)
        return QI(self.re + q.re, self.im + q.im)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        q = self.cast(other)
        return QI(self.re*q.re - self.im*q.im,
                  self.re*q.im + self.im*q.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = self.cast(other)
        den = q.re*q.re + q.im*q.im
        if not den:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        return QI((self.re*q.re + self.im*q.im)/den,
                  (self.im*q.re - self.re*q.im)/den)

    def __bool__(self):
        return bool(self.re or self.im)

    def conj(self):
        return QI(self.re, -self.im)


I = QI(F(0), F(1))
END = None
STOP_SIGNAL = None


class VerificationError(RuntimeError):
    pass


class VerificationInterrupted(VerificationError):
    pass


class VerificationDeadline(VerificationError):
    pass


def request_interrupt(signum, frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def tick():
    if STOP_SIGNAL is not None:
        raise VerificationInterrupted("received signal " + str(STOP_SIGNAL))
    if END is not None and time.monotonic() >= END:
        raise VerificationDeadline("internal finite-assay deadline reached")


def require(condition, message):
    tick()
    if not condition:
        raise VerificationError(message)


def trim(p):
    q = list(p)
    while q and not q[-1]:
        q.pop()
    return q


def add(p, q):
    r = [0] * max(len(p), len(q))
    for k, x in enumerate(p):
        r[k] = r[k] + x
    for k, x in enumerate(q):
        r[k] = r[k] + x
    return trim(r)


def scale(p, a):
    return trim([a*x for x in p])


def sub(p, q):
    return add(p, scale(q, -1))


def mul(p, q):
    tick()
    if not p or not q:
        return []
    r = [0] * (len(p) + len(q) - 1)
    for j, a in enumerate(p):
        for k, b in enumerate(q):
            r[j+k] = r[j+k] + a*b
    return trim(r)


def power(p, n):
    r = [F(1)]
    for _ in range(n):
        r = mul(r, p)
    return r


def conjugate(p):
    return [QI.cast(x).conj() for x in p]


def real(p):
    return trim([QI.cast(x).re for x in p])


def imag(p):
    return trim([QI.cast(x).im for x in p])


def coeff(p, k):
    return p[k] if k < len(p) else F(0)


def rref(a):
    b = [[F(x) for x in row] for row in a]
    pivots = []
    row = 0
    for col in range(len(b[0]) if b else 0):
        tick()
        pivot = next((j for j in range(row, len(b)) if b[j][col]), None)
        if pivot is None:
            continue
        b[row], b[pivot] = b[pivot], b[row]
        den = b[row][col]
        b[row] = [x/den for x in b[row]]
        for j in range(len(b)):
            if j != row and b[j][col]:
                x = b[j][col]
                b[j] = [u-x*v for u, v in zip(b[j], b[row])]
        pivots.append(col)
        row += 1
        if row == len(b):
            break
    return b, pivots


def rank(a):
    return len(rref(a)[1])


def transpose(a):
    return [list(row) for row in zip(*a)]


def nullspace(a):
    b, pivots = rref(a)
    n = len(a[0])
    out = []
    for free in (j for j in range(n) if j not in pivots):
        v = [F(0)] * n
        v[free] = F(1)
        for row, pivot in enumerate(pivots):
            v[pivot] = -b[row][free]
        out.append(v)
    return out


def determinant(a):
    b = [[F(x) for x in row] for row in a]
    value = F(1)
    for j in range(len(b)):
        tick()
        k = next((k for k in range(j, len(b)) if b[k][j]), None)
        if k is None:
            return F(0)
        if k != j:
            b[j], b[k] = b[k], b[j]
            value = -value
        pivot = b[j][j]
        value *= pivot
        for k in range(j+1, len(b)):
            factor = b[k][j]/pivot
            for m in range(j+1, len(b)):
                b[k][m] -= factor*b[j][m]
    return value


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def mm(a, b):
    tick()
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def laurent_norm(p):
    out = {}
    for j, a in enumerate(p):
        for k, b in enumerate(p):
            out[j-k] = out.get(j-k, QI()) + a*b.conj()
    return {j: x for j, x in out.items() if x}


def circle_controls():
    p = [QI(), QI(), 2*I/5, QI(F(3, 10), F(-2, 5)), QI(F(3, 10))]
    q = [QI(), QI(F(3, 10)), QI(F(-3, 10), F(2, 5)), 2*I/5]
    norm = laurent_norm(p)
    for j, x in laurent_norm(q).items():
        norm[j] = norm.get(j, QI()) + x
    norm = {j: x for j, x in norm.items() if x}
    require(norm == {0: QI(F(1))}, "raw circle-inner coefficient identity fails")
    bad = list(p)
    bad[0] = QI(F(1, 10))
    badnorm = laurent_norm(bad)
    for j, x in laurent_norm(q).items():
        badnorm[j] = badnorm.get(j, QI()) + x
    require(any(x != (QI(F(1)) if j == 0 else QI())
                for j, x in badnorm.items()), "inner mutation not detected")


def raw_curve():
    n, d = [I, F(1)], [-I, F(1)]
    p = scale(add(add(scale(mul(power(n, 2), power(d, 2)), 4*I),
                      scale(mul(power(n, 3), d), 3-4*I)),
                  scale(power(n, 4), 3)), F(1, 10))
    q = scale(add(add(scale(mul(n, power(d, 3)), 3),
                      scale(mul(power(n, 2), power(d, 2)), -3+4*I)),
                  scale(mul(power(n, 3), d), 4*I)), F(1, 10))
    c = power(d, 4)
    row = [real(p), imag(p), real(q), imag(q), real(c), imag(c)]
    v = [row, [scale(row[1], -1), row[0], scale(row[3], -1),
               row[2], scale(row[5], -1), row[4]]]
    return p, q, c, v


PAIRS = list(itertools.combinations(range(6), 2))


def minors(v):
    return [sub(mul(v[0][i], v[1][j]), mul(v[0][j], v[1][i]))
            for i, j in itertools.combinations(range(len(v[0])), 2)]


def coefficient_matrix(polys, n=9):
    return [[F(coeff(p, k)) for p in polys] for k in range(n)]


def expected_kernel():
    vectors = []
    def form(terms):
        v = [F(0)] * 15
        for i, j, x in terms:
            if i > j:
                i, j, x = j, i, -x
            v[PAIRS.index((i, j))] += F(x)
        return v
    for i, j in itertools.combinations(range(3), 2):
        vectors.append(form([(2*i, 2*j, 1), (2*i+1, 2*j+1, -1)]))
        vectors.append(form([(2*i, 2*j+1, 1), (2*i+1, 2*j, 1)]))
    vectors.append(form([(0, 1, 1), (2, 3, 1), (4, 5, -1)]))
    return vectors


def written_functional(j):
    gpoly = scale(mul(power([F(1), F(1)], j),
                      power([F(-1), F(1)], 8-j)), F(1, 256))
    phase = QI(F(1))
    for _ in range(j):
        phase = phase*I
    gs = [QI.cast(coeff(gpoly, k+4))*phase for k in range(1, 5)]
    g1, g2, g3, g4 = gs
    b = F(10, 3)*g4
    c0 = (QI(F(1), F(3, 4)))*b - F(5, 2)*I*g3
    t = -F(400, 3)*g2 + F(160, 3)*I*b + F(40, 3)*(-3+4*I)*c0
    a0 = t/QI(F(12), F(41))
    z = 400*g1 - 120*c0
    return 13776*z.re + 22300*z.im - 106164*a0.re + 4029152*a0.im


def source_controls():
    x = [F(0), F(1)]
    results = {}
    for tau in (F(1), F(-1)):
        v = [[power(x, 2), [F(1)], x, []],
             [add(x, [tau]), power(x, 2), [F(1)], x]]
        actual = minors(v)
        expected = [sub(sub(power(x, 4), x), [tau]), scale(x, -tau),
                    power(x, 3), sub([F(1)], power(x, 3)), x, power(x, 2)]
        require(actual == expected, "source-control raw minor mismatch")
        gain_map = [actual[0], actual[3], scale(actual[1], -1), actual[4],
                    scale(actual[2], -1), actual[5], scale(actual[5], -1)]
        target = [sub(sub(power(x, 4), x), [tau]), sub([F(1)], power(x, 3)),
                  scale(x, tau), x, scale(power(x, 3), -1),
                  power(x, 2), scale(power(x, 2), -1)]
        require(gain_map == target, "full symbolic gain-coefficient map mismatch")
        quadratic = [-tau*tau, F(-1), tau]
        disc = quadratic[1]**2 - 4*quadratic[0]*quadratic[2]
        require(disc == (5 if tau == 1 else -3), "source-control discriminant mismatch")
        results[str(tau)] = {"raw_minors": actual, "fibre_quadratic": quadratic,
                             "discriminant": disc}
    return results


def homogeneous_substitution(p, rho):
    out = []
    for j, a in enumerate(p):
        out = add(out, scale(mul(power([F(1), F(1)], j),
                                  power([F(-1), F(1)], 4-j)), a*rho**j))
    return out


def plant(v, rho):
    vt = [[homogeneous_substitution(p, rho) for p in row] for row in v]
    vt = [[row[j] for j in (4, 5, 0, 1, 2, 3)] for row in vt]
    lead = [[coeff(vt[i][j], 4) for j in range(2)] for i in range(2)]
    det = lead[0][0]*lead[1][1] - lead[0][1]*lead[1][0]
    require(det, "Cayley leading block is singular")
    inv = [[lead[1][1]/det, -lead[0][1]/det],
           [-lead[1][0]/det, lead[0][0]/det]]
    normalized = [[add(scale(vt[0][j], inv[i][0]), scale(vt[1][j], inv[i][1]))
                   for j in range(6)] for i in range(2)]
    d = [[normalized[i][j] for j in range(2)] for i in range(2)]
    raw_n = [row[2:] for row in normalized]
    lead_n = [[coeff(raw_n[i][j], 4) for j in range(4)] for i in range(2)]
    n = [[sub(raw_n[i][j], add(scale(d[i][0], lead_n[0][j]),
                                  scale(d[i][1], lead_n[1][j])))
          for j in range(4)] for i in range(2)]
    require(all(len(p) <= 4 for row in n for p in row), "N degree exceeds three")
    require([[coeff(d[i][j], 4) for j in range(2)] for i in range(2)] == eye(2), "D is not monic")
    a = [[F(0)]*8 for _ in range(8)]
    b = [[F(0)]*4 for _ in range(8)]
    for block in range(4):
        for i in range(2):
            for j in range(2):
                a[2*block+i][j] = -F(coeff(d[i][j], 3-block))
            if block < 3:
                a[2*block+i][2*(block+1)+i] = F(1)
            for j in range(4):
                b[2*block+i][j] = F(coeff(n[i][j], 3-block))
    c = [[F(int(i == j)) for j in range(8)] for i in range(2)]
    return d, n, a, b, c


def characteristic_and_transfer(d, n, a, b, c):
    ident = eye(8)
    bk = ident
    coefficients = [F(1)]
    adj_blocks = [ident]
    for k in range(1, 9):
        product = mm(a, bk)
        ck = -sum((product[i][i] for i in range(8)), F(0))/k
        coefficients.append(ck)
        bk = [[product[i][j] + ck*ident[i][j] for j in range(8)] for i in range(8)]
        if k < 8:
            adj_blocks.append(bk)
    require(not any(x for row in bk for x in row), "Cayley-Hamilton residual")
    char = trim(list(reversed(coefficients)))
    det_d = sub(mul(d[0][0], d[1][1]), mul(d[0][1], d[1][0]))
    require(char == det_d, "raw characteristic does not equal det D")
    adj_transfer = [[[] for _ in range(4)] for _ in range(2)]
    for k, block in enumerate(adj_blocks):
        term = mm(mm(c, block), b)
        for i in range(2):
            for j in range(4):
                adj_transfer[i][j] = add(adj_transfer[i][j], [F(0)]*(7-k)+[term[i][j]])
    for i in range(2):
        for j in range(4):
            left = add(mul(d[i][0], adj_transfer[0][j]), mul(d[i][1], adj_transfer[1][j]))
            require(left == mul(n[i][j], char), "universal transfer polynomial identity fails")
    ob, ct = [], [[] for _ in range(8)]
    ak = ident
    for k in range(8):
        if k < 4:
            ob.extend(mm(c, ak))
        block = mm(ak, b)
        for i in range(8):
            ct[i].extend(block[i])
        ak = mm(ak, a)
    require(rank(ob) == 8 and rank(ct) == 8, "ordinary plant is not minimal")
    return char


def peak_rss_metadata():
    if resource is None:
        return {"available": False, "reason": "standard resource module unavailable"}
    try:
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    except (AttributeError, OSError) as exc:
        return {"available": False, "reason": type(exc).__name__ + ": " + str(exc)}
    unit = "bytes" if sys.platform == "darwin" else "KiB" if sys.platform.startswith("linux") else "platform_native"
    result = {"available": True, "ru_maxrss": peak, "unit": unit,
              "admission_ceiling_bytes": 1073741824, "os_memory_limit_enforced": False}
    if unit == "bytes":
        result["peak_rss_bytes"] = peak
    elif unit == "KiB":
        result["peak_rss_bytes"] = peak*1024
    return result


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, QI):
        return {"re": str(x.re), "im": str(x.im)}
    if isinstance(x, dict):
        return {str(k): encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def assay():
    circle_controls()
    controls = source_controls()
    p, q, c, v = raw_curve()
    raw = coefficient_matrix(minors(v))
    require(rank(raw) == 8 and rank(raw[:8]) == 8, "raw coefficient ranks differ from eight")
    kernel = expected_kernel()
    require(rank(kernel) == 7, "expected kernel does not have dimension seven")
    require(all(not dot(row, k) for row in raw for k in kernel), "raw anti-J/B kernel mismatch")
    ell = nullspace(transpose(raw))
    require(len(ell) == 1 and ell[0][8], "raw left separator is not uniquely normalizable")
    ell = [x/ell[0][8] for x in ell[0]]
    badell = list(ell)
    badell[0] += 1
    require(any(dot(row, badell) for row in transpose(raw)), "separator mutation not detected")
    f = [real(mul(c, conjugate(c))), real(mul(p, conjugate(p))),
         real(mul(p, conjugate(q))), imag(mul(p, conjugate(q))),
         real(mul(p, conjugate(c))), imag(mul(p, conjugate(c))),
         real(mul(q, conjugate(c))), imag(mul(q, conjugate(c)))]
    fmatrix = coefficient_matrix(f)
    det9 = determinant([row+[F(int(j == 8))] for j, row in enumerate(fmatrix)])
    require(det9, "augmented nine-by-nine determinant vanishes")
    alpha = written_functional(8)
    require(alpha > 1000000, "written separator alpha bound fails")
    from_written = [written_functional(j)/alpha for j in range(9)]
    require(from_written == ell, "raw-minor separator disagrees with written Fourier formula")
    require(all(abs(x) < 122 for x in ell[:8]), "separator monomial bound fails")
    rho = F(1, 100000)
    error = sum((abs(ell[j])*math.comb(8, j)*rho**(8-j) for j in range(8)), F(0))
    require(error < F(1, 2), "closed disk separation fails")
    d, n, a, b, cout = plant(v, rho)
    char = characteristic_and_transfer(d, n, a, b, cout)
    return {"status": "FINITE_EXACT_COEFFICIENT_CHECKS_PASS",
            "source_controls": controls, "raw_minor_rank": 8,
            "raw_first_eight_rank": 8, "raw_kernel_basis": kernel,
            "raw_left_separator": ell, "determinant_9x9": det9,
            "written_functional_alpha": alpha, "rho": rho,
            "closed_disk_coefficient_error_bound": error,
            "D": d, "N": n, "A": a, "B": b, "C": cout,
            "characteristic": char,
            "universal_checks": ["circle Laurent identity", "source-control full gain coefficient maps",
                                 "raw minor kernel equality", "raw versus written separator",
                                 "characteristic and transfer polynomial identities", "minimality ranks"],
            "not_established_by_this_run": ["real decomposable-point lemma for all real planes",
                                           "projective root transport and open-neighborhood argument",
                                           "generic non-density theorem", "novelty", "formal verification"]}


def main():
    global END
    ap = argparse.ArgumentParser()
    ap.add_argument("--request", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--deadline-seconds", type=int, default=120)
    ap.add_argument("--max-output-bytes", type=int, default=2097152)
    args = ap.parse_args()
    out = Path(args.output)
    if out.exists():
        raise FileExistsError("refusing to overwrite an existing verification receipt")
    signal.signal(signal.SIGTERM, request_interrupt)
    signal.signal(signal.SIGINT, request_interrupt)
    started = time.monotonic()
    END = started + args.deadline_seconds
    code = 0
    try:
        request = json.loads(Path(args.request).read_text())
        require(request.get("execution_permission") == "NOT_GRANTED",
                "this frozen request must not be rewritten into a GO")
        for item in request["source_pins"]:
            tick()
            actual = hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest()
            require(actual == item["sha256"], "input source hash mismatch: " + item["path"])
        result = assay()
        tick()
    except VerificationInterrupted as exc:
        code = 128 + STOP_SIGNAL
        result = {"status": "INCOMPLETE_INTERRUPTED", "exception": type(exc).__name__, "message": str(exc)}
    except VerificationDeadline as exc:
        code = 2
        result = {"status": "INCOMPLETE_DEADLINE", "exception": type(exc).__name__, "message": str(exc)}
    except Exception as exc:
        code = 2
        result = {"status": "INCOMPLETE_OR_FAILED", "exception": type(exc).__name__, "message": str(exc)}
    # Science is stopped; protect the bounded final receipt from a second signal.
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if STOP_SIGNAL is not None:
        code = 128 + STOP_SIGNAL
        result["status"] = "INCOMPLETE_INTERRUPTED"
        result["signal"] = STOP_SIGNAL
    result["elapsed_seconds"] = time.monotonic()-started
    result["verifier_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["python_optimization_level"] = sys.flags.optimize
    result["peak_rss"] = peak_rss_metadata()
    text = json.dumps(encode(result), indent=2)+"\n"
    if len(text.encode()) > args.max_output_bytes:
        code = 2
        result = {"status": "INCOMPLETE_OR_FAILED", "exception": "VerificationError",
                  "message": "receipt exceeds frozen output limit", "peak_rss": peak_rss_metadata()}
        text = json.dumps(encode(result), indent=2)+"\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("x") as handle:
        handle.write(text)
    print(result["status"])
    return code


if __name__ == "__main__":
    sys.exit(main())
