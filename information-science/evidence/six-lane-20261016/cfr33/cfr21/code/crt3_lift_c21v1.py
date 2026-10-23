#!/usr/bin/env python3
"""Exact CRT lift of a (Z_q,k;3)-DM to a (Z_(3q),k;1)-DM, gcd(q,3)=1.
CFR21 continuation, InfoCFR27Lift. This is not a SAT encoding.

Usage:
  crt3_lift_c21v1.py solve PATTERN.json OUTPREFIX SECONDS
  crt3_lift_c21v1.py calibrate OUTDIR SECONDS
PATTERN: {"q": q, "beta": k rows of 3q residues 0..q-1}.
The lift has entries x = (3*(3^-1 mod q)*beta + q*(q^-1 mod 3)*alpha) mod 3q.
For every row pair and beta-difference d, the three alpha-differences must be
all distinct in F3. This is equivalent to their sum being zero and their first
two differing. We solve the sum equations exactly by Gaussian elimination mod3,
then seek a full-support image of the inequality forms on the nullspace.

Normalise beta row0 to zero by columnwise subtraction; alpha row0=0. Fix
alpha_i(column0)=0 by row translations. Let K be a basis of ker(A), B the
inequality forms. Choose independent rows Q of BK and a right inverse R of Q.
Every possible inequality image is realised by alpha=K R y, and coordinates y
are themselves inequality values, hence y_j in {1,2}. Scaling lets us fix y0=1.
DFS over these binary choices, checking a form as soon as its last coordinate
is assigned, is exhaustive; unused kernel directions do not affect validity.
A projected zero form gives an exact obstruction. Every produced lift is
rechecked over all row pairs in Z_(3q), independently of the linear constraints.
SIGTERM and native wall deadline return UNKNOWN; output files use mode x.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

STOP = False


def on_term(signum, frame):
    global STOP
    STOP = True


def clock():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def rref(A, width, extras=0):
    A = [[v % 3 for v in row] for row in A]
    piv = []
    row = 0
    for col in range(width):
        at = next((j for j in range(row, len(A)) if A[j][col]), None)
        if at is None:
            continue
        A[row], A[at] = A[at], A[row]
        if A[row][col] == 2:
            A[row] = [(2 * v) % 3 for v in A[row]]
        for j in range(len(A)):
            if j != row and A[j][col]:
                a = A[j][col]
                A[j] = [(x - a * y) % 3 for x, y in zip(A[j], A[row])]
        piv.append(col)
        row += 1
        if row == len(A):
            break
    return A[:row], piv


def kernel(A, width):
    red, piv = rref(A, width)
    free = [c for c in range(width) if c not in piv]
    K = []
    for f in free:
        v = [0] * width
        v[f] = 1
        for row, p in enumerate(piv):
            v[p] = (-red[row][f]) % 3
        K.append(v)
    return K, len(piv)


def matmul(A, B):
    if not A:
        return []
    cols = list(zip(*B)) if B else []
    return [[sum(x * y for x, y in zip(r, c)) % 3 for c in cols] for r in A]


def dm_ok(D, n):
    return all(len({(u - v) % n for u, v in zip(D[i], D[j])}) == n
               for i in range(len(D)) for j in range(i))


def constraints(q, beta):
    n = 3 * q
    k = len(beta)
    if q < 1 or q % 3 == 0 or k < 2:
        raise ValueError("q must be positive and coprime to3; k >=2")
    if any(len(row) != n or any(type(x) is not int or not 0 <= x < q for x in row) for row in beta):
        raise ValueError("bad beta dimensions/residues")
    beta = [[(x - beta[0][c]) % q for c, x in enumerate(row)] for row in beta]
    width = (k - 1) * (n - 1)

    def vindex(i, c):
        return (i - 1) * (n - 1) + c - 1

    def form(terms):
        out = [0] * width
        for i, c, sign in terms:
            if i and c:
                v = vindex(i, c)
                out[v] = (out[v] + sign) % 3
        return out

    A, B = [], []
    triples = []
    for i in range(k):
        for j in range(i):
            by = [[] for _ in range(q)]
            for c in range(n):
                by[(beta[i][c] - beta[j][c]) % q].append(c)
            for d, positions in enumerate(by):
                if len(positions) != 3:
                    raise ValueError("pair %d,%d beta residue%d count%d !=3" % (i, j, d, len(positions)))
                a, b, c = positions
                A.append(form([(i, p, 1) for p in positions] + [(j, p, -1) for p in positions]))
                B.append(form([(i, a, 1), (j, a, -1), (i, b, -1), (j, b, 1)]))
                triples.append((i, j, d, positions))
    return beta, A, B, width, triples


def solve_pattern(q, beta, seconds):
    t0 = time.monotonic()
    beta, A, B, width, triples = constraints(q, beta)
    k, n = len(beta), 3 * q
    K, rank = kernel(A, width)
    dim = len(K)
    projected = [[sum(x * y for x, y in zip(row, z)) % 3 for z in K] for row in B]
    rec = {"q": q, "n": n, "k": k, "sum_equations": len(A), "variables_after_gauge": width,
           "rank": rank, "kernel_dimension": dim, "inequalities": len(B), "nodes": 0}
    if any(not any(row) for row in projected):
        rec.update(verdict="EXHAUSTED-PATTERN", obstruction="projected zero inequality", wall_s=time.monotonic() - t0)
        return rec, None
    # Incremental basis of the row space of projected; record original independent forms.
    echelon = {}
    selected = []
    for f in projected:
        v = f[:]
        for p in sorted(echelon):
            if v[p]:
                a = v[p]
                v = [(x - a * y) % 3 for x, y in zip(v, echelon[p])]
        p = next((i for i, x in enumerate(v) if x), None)
        if p is not None:
            if v[p] == 2:
                v = [(2 * x) % 3 for x in v]
            echelon[p] = v
            selected.append(f)
    r = len(selected)
    # Augmented RREF [Q | I] gives a right inverse (non-pivot coordinates0).
    aug = [row[:] + [int(i == j) for j in range(r)] for i, row in enumerate(selected)]
    red, piv = rref(aug, dim, r)
    right = [[0] * r for _ in range(dim)]
    for i, p in enumerate(piv):
        right[p] = red[i][dim:]
    forms = matmul(projected, right)
    if len(piv) != r:
        raise AssertionError("independent form rank mismatch")
    # Canonicalise scalar-equivalent forms, removing duplicates.
    unique = set()
    for row in forms:
        p = next(i for i, x in enumerate(row) if x)
        if row[p] == 2:
            row = [(2 * x) % 3 for x in row]
        unique.add(tuple(row))
    forms = sorted(unique)
    # Reorder coordinates by participation (coordinate0 remains first, fixing scale).
    order = [0] + sorted(range(1, r), key=lambda j: -sum(row[j] != 0 for row in forms))
    forms = [tuple(row[j] for j in order) for row in forms]
    buckets = [[] for _ in range(r)]
    for row in forms:
        last = max(j for j, x in enumerate(row) if x)
        buckets[last].append([(j, a) for j, a in enumerate(row) if a])
    y = [0] * r
    result = None
    nodes = 0
    interrupted = False

    def dfs(at):
        nonlocal nodes, interrupted, result
        nodes += 1
        if STOP or time.monotonic() - t0 > seconds:
            interrupted = True
            return False
        if at == r:
            result = y[:]
            return True
        for val in ((1,) if at == 0 else (1, 2)):
            y[at] = val
            if all(sum(a * y[j] for j, a in form) % 3 for form in buckets[at]):
                if dfs(at + 1):
                    return True
            if interrupted:
                return False
        y[at] = 0
        return False

    dfs(0)
    rec.update(inequality_rank=r, unique_forms=len(forms), nodes=nodes)
    if result is None:
        rec.update(verdict="UNKNOWN" if interrupted else "EXHAUSTED-PATTERN", wall_s=time.monotonic() - t0)
        return rec, None
    yoriginal = [0] * r
    for j, original in enumerate(order):
        yoriginal[original] = result[j]
    z = [sum(a * b for a, b in zip(row, yoriginal)) % 3 for row in right]
    avector = [sum(K[j][i] * z[j] for j in range(dim)) % 3 for i in range(width)]
    # Separate checks of equations and inequalities before expansion.
    if any(sum(a * b for a, b in zip(row, avector)) % 3 for row in A):
        raise AssertionError("sum equation mismatch")
    if any(sum(a * b for a, b in zip(row, avector)) % 3 == 0 for row in B):
        raise AssertionError("inequality mismatch")
    alpha = [[0] * n]
    for i in range(k - 1):
        alpha.append([0] + avector[i * (n - 1):(i + 1) * (n - 1)])
    c7 = 3 * pow(3, -1, q) if q > 1 else 0
    c3 = q * pow(q, -1, 3)
    D = [[(c7 * b + c3 * a) % n for b, a in zip(br, ar)] for br, ar in zip(beta, alpha)]
    if not dm_ok(D, n):
        raise AssertionError("CRT lift failed direct difference-matrix definition")
    rec.update(verdict="CANDIDATE", wall_s=time.monotonic() - t0)
    return rec, D


def write_solution(prefix, rec, D):
    if D is not None:
        text = "".join(" ".join(map(str, row)) + "\n" for row in D)
        with open(prefix + ".dmraw", "x") as fh:
            fh.write(text)
        rec["dmraw_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    with open(prefix + ".receipt.json", "x") as fh:
        json.dump(rec, fh, indent=1)


def calibrate(outdir, seconds):
    os.mkdir(outdir)
    lane = Path(__file__).resolve().parents[2]
    source21 = lane / "cfr27/controls/dm-orbit-v1/P21-mu1-5cycle.dmraw"
    source33 = lane / "prior-art/sage-dm-33-6-1.dmraw"
    reports = []
    for name, q, path in (("sage21k6", 7, source21), ("sage33k6", 11, source33)):
        D = [[int(x) for x in line.split()] for line in path.read_text().splitlines()]
        if not dm_ok(D, 3 * q):
            raise AssertionError("invalid pinned positive")
        beta = [[x % q for x in row] for row in D]
        rec, lift = solve_pattern(q, beta, seconds)
        rec.update(source=str(path), source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), expected="CANDIDATE")
        write_solution(outdir + "/" + name, rec, lift)
        if rec["verdict"] != "CANDIDATE":
            raise AssertionError(name + " positive not recovered: " + str(rec))
        reports.append(rec)
    for k in (3, 4):
        # q1: every beta entry0, so this is exactly the F3 k-row DM question.
        beta = [[0, 0, 0] for _ in range(k)]
        rec, D = solve_pattern(1, beta, seconds)
        expected = "CANDIDATE" if k == 3 else "EXHAUSTED-PATTERN"
        rec["expected"] = expected
        write_solution(outdir + "/q1k%d" % k, rec, D)
        if rec["verdict"] != expected:
            raise AssertionError("q1 boundary failed")
        reports.append(rec)
    beta = [[(i * c) % 7 for t in range(3) for c in range(7)] for i in range(7)]
    rec, D = solve_pattern(7, beta, seconds)
    rec["expected"] = "EXHAUSTED-PATTERN (three zero-difference columns force a Z3,7;1 DM)"
    write_solution(outdir + "/repeated-field7", rec, D)
    if rec["verdict"] != "EXHAUSTED-PATTERN":
        raise AssertionError("repeated field-table negative failed")
    reports.append(rec)
    try:
        damaged = [row[:] for row in beta]
        damaged[2][4] = (damaged[2][4] + 1) % 7
        solve_pattern(7, damaged, seconds)
    except ValueError as e:
        reports.append({"control": "damaged beta multiplicity", "rejected": True, "reason": str(e)})
    else:
        raise AssertionError("malformed beta accepted")
    with open(outdir + "/controls.json", "x") as fh:
        json.dump({"clock": clock(), "all_as_expected": True, "reports": reports}, fh, indent=1)
    print("CRT CALIBRATION PASS", [(r.get("rank"), r.get("kernel_dimension"), r.get("verdict")) for r in reports])


def main():
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if sys.argv[1] == "calibrate":
        calibrate(sys.argv[2], float(sys.argv[3]))
        return
    data = json.loads(Path(sys.argv[2]).read_text())
    rec, D = solve_pattern(data["q"], data["beta"], float(sys.argv[4]))
    rec.update(clock=clock(), input=sys.argv[2], input_sha256=hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest())
    write_solution(sys.argv[3], rec, D)
    print(json.dumps(rec))
    sys.exit(10 if D is not None else 20 if rec["verdict"] == "EXHAUSTED-PATTERN" else 0)


if __name__ == "__main__":
    main()
