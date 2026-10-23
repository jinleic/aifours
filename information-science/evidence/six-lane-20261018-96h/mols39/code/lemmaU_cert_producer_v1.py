#!/usr/bin/env python3
"""lemmaU_cert_producer_v1.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only).

Produces a Lemma U certificate in the exact format of
  evidence/lemmaU-certificate-format-v1.md (sha256 1b6537a42dd936a16337c58fd65039ece9e150099e2b8a297ab21d206dfd6ba0)
for a pinned raw (Z_n, k; 1) difference matrix with n = 3q, gcd(3, q) = 1.
Method: build the J fibre-sum equations e_j over the U gauged unknowns (format section 2), full Gauss-Jordan
elimination over F_3 with every working row tracked as a combination of the ORIGINAL equations (rank witness =
the reduced rows and their combinations), nullspace basis from the free columns, then all 3^dim points are tested
for the rainbow property; for every non-rainbow point the smallest failing fibre index is recorded.
Internal self-checks (not a substitute for the independent checker): every basis vector solves every equation,
every witness row recomputed from its combination has the RREF pivot pattern, alpha_hat and minus_alpha_hat are
rainbow and lie in the span.
CLI: python3.14 -I -B lemmaU_cert_producer_v1.py --anchor RAW --anchor-sha256 HEX --out CERT_JSON [--budget-s S]
Exit codes: 0 OK; 2 bad input / pin mismatch / existing output; 3 input is not a DM or a fibre size is not 3;
4 internal self-check failure; 5 self budget exceeded. Exactly one JSON summary line is printed in every case."""
import sys, os, json, time, hashlib, argparse

FORMAT = "lemmaU-cert-v1"


class Stop(Exception):
    def __init__(self, code, status, reason):
        super().__init__(reason)
        self.code, self.status, self.reason = code, status, reason


def main(argv):
    t0 = time.monotonic()
    summary = {"status": None, "reason": None, "n": None, "q": None, "k": None, "U": None, "J": None, "rank": None,
               "dim": None, "rainbow_count": None, "alpha_hat_idx": None, "minus_alpha_hat_idx": None,
               "cert_path": None, "cert_sha256": None, "anchor_sha256": None, "wall_s": None}
    try:
        ap = argparse.ArgumentParser(add_help=False)
        ap.add_argument("--anchor", required=True)
        ap.add_argument("--anchor-sha256", required=True)
        ap.add_argument("--out", required=True)
        ap.add_argument("--budget-s", type=float, default=240.0)
        try:
            a = ap.parse_args(argv)
        except SystemExit:
            raise Stop(2, "BAD_INPUT", "bad command line")

        def budget():
            if time.monotonic() - t0 > a.budget_s:
                raise Stop(5, "BUDGET_EXCEEDED", "self wall budget exceeded")

        if os.path.exists(a.out):
            raise Stop(2, "BAD_INPUT", "output path already exists")
        try:
            raw = open(a.anchor, "rb").read()
        except OSError as e:
            raise Stop(2, "BAD_INPUT", "cannot read anchor: %r" % (e,))
        h = hashlib.sha256(raw).hexdigest()
        summary["anchor_sha256"] = h
        if h != a.anchor_sha256:
            raise Stop(2, "INPUT_PIN_MISMATCH", "anchor sha256 differs from --anchor-sha256")
        try:
            rows = [[int(t) for t in ln.split()] for ln in raw.decode("ascii").splitlines() if ln.strip()]
        except (UnicodeDecodeError, ValueError):
            raise Stop(2, "BAD_INPUT", "anchor is not k lines of integers")
        k = len(rows)
        n = len(rows[0]) if rows else 0
        if k < 2 or n < 3 or any(len(r) != n for r in rows):
            raise Stop(2, "BAD_INPUT", "ragged or too small anchor")
        q = n // 3
        if n % 3 != 0 or q % 3 == 0:
            raise Stop(2, "BAD_INPUT", "n must be 3q with gcd(3,q) = 1")
        D = [[v % n for v in r] for r in rows]
        summary.update({"n": n, "q": q, "k": k})
        # DM check
        for x in range(k):
            for y in range(x + 1, k):
                if len({(D[x][c] - D[y][c]) % n for c in range(n)}) != n:
                    raise Stop(3, "NOT_DM", "rows %d,%d: differences not a bijection" % (x, y))
        E = [[(D[x][c] - D[0][c]) % n for c in range(n)] for x in range(k)]
        Bq = [[v % q for v in r] for r in E]
        T3 = [[v % 3 for v in r] for r in E]
        pairs = [(x, y) for x in range(k) for y in range(x + 1, k)]
        U = (k - 1) * (n - 1)
        J = len(pairs) * q
        summary.update({"U": U, "J": J})

        def var(x, c):
            return None if (x == 0 or c == 0) else (x - 1) * (n - 1) + (c - 1)

        fibres = []          # j -> (x, y, [c1, c2, c3])
        for (x, y) in pairs:
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[(Bq[x][c] - Bq[y][c]) % q].append(c)
            for t in range(q):
                if len(buckets[t]) != 3:
                    raise Stop(3, "FIBRE_SIZE", "pair (%d,%d) fibre %d has %d columns" % (x, y, t, len(buckets[t])))
                fibres.append((x, y, buckets[t]))
        # equation vectors (dense, mod 3)
        eqs = []
        for (x, y, cols) in fibres:
            e = [0] * U
            for c in cols:
                vx, vy = var(x, c), var(y, c)
                if vx is not None:
                    e[vx] = (e[vx] + 1) % 3
                if vy is not None:
                    e[vy] = (e[vy] + 2) % 3
            eqs.append(e)
        # Gauss-Jordan over F_3 with combination tracking
        work = [list(e) for e in eqs]
        combs = [{j: 1} for j in range(J)]
        pivots = []
        r = 0
        for col in range(U):
            budget()
            piv = None
            for i in range(r, J):
                if work[i][col]:
                    piv = i
                    break
            if piv is None:
                continue
            work[r], work[piv] = work[piv], work[r]
            combs[r], combs[piv] = combs[piv], combs[r]
            inv = 1 if work[r][col] == 1 else 2          # 2 * 2 = 4 = 1 (mod 3)
            if inv != 1:
                work[r] = [(v * inv) % 3 for v in work[r]]
                combs[r] = {j: (cf * inv) % 3 for j, cf in combs[r].items()}
            for i in range(J):
                if i != r and work[i][col]:
                    f = work[i][col]
                    wr = work[r]
                    work[i] = [(vi - f * vr) % 3 for vi, vr in zip(work[i], wr)]
                    ci = combs[i]
                    for j, cf in combs[r].items():
                        nv = (ci.get(j, 0) - f * cf) % 3
                        if nv:
                            ci[j] = nv
                        else:
                            ci.pop(j, None)
            pivots.append(col)
            r += 1
            if r == J:
                break
        rank = r
        pivset = set(pivots)
        free = [col for col in range(U) if col not in pivset]
        dim = U - rank
        if len(free) != dim:
            raise Stop(4, "SELF_CHECK", "free column count mismatch")
        basis = []
        for fcol in free:
            b = [0] * U
            b[fcol] = 1
            for i, p in enumerate(pivots):
                b[p] = (-work[i][fcol]) % 3
            basis.append(b)
        summary.update({"rank": rank, "dim": dim})
        # self-check 1: basis solves all equations
        for b in basis:
            for e in eqs:
                if sum(ev * bv for ev, bv in zip(e, b)) % 3:
                    raise Stop(4, "SELF_CHECK", "basis vector fails an equation")
        # self-check 2: witness rows recomputed from combinations have the pivot pattern
        witness = []
        for i in range(rank):
            budget()
            R = [0] * U
            for j, cf in combs[i].items():
                ej = eqs[j]
                R = [(rv + cf * ev) % 3 for rv, ev in zip(R, ej)]
            if R != work[i]:
                raise Stop(4, "SELF_CHECK", "combination does not reproduce reduced row %d" % i)
            for m, p in enumerate(pivots):
                if R[p] != (1 if m == i else 0):
                    raise Stop(4, "SELF_CHECK", "pivot pattern broken in row %d" % i)
            witness.append({"pivot": pivots[i], "combination": [[j, cf] for j, cf in sorted(combs[i].items()) if cf % 3]})
        # points
        fib_idx = [(x, y, [(var(x, c), var(y, c)) for c in cols]) for (x, y, cols) in fibres]

        def first_bad_fibre(A):
            for j, (x, y, cv) in enumerate(fib_idx):
                vals = set()
                for (vx, vy) in cv:
                    ax = 0 if vx is None else A[vx]
                    ay = 0 if vy is None else A[vy]
                    vals.add((ax - ay) % 3)
                if len(vals) != 3:
                    return j
            return None

        rainbow, failures = [], []
        total = 3 ** dim
        for idx in range(total):
            if (idx & 1023) == 0:
                budget()
            z = []
            rem = idx
            for _ in range(dim):
                z.append(rem % 3)
                rem //= 3
            z.reverse()                                    # z[0] most significant
            A = [0] * U
            for zr, b in zip(z, basis):
                if zr:
                    A = [(av + zr * bv) % 3 for av, bv in zip(A, b)]
            j = first_bad_fibre(A)
            if j is None:
                rainbow.append(idx)
            else:
                failures.append([idx, j])
        # self-check 3: alpha_hat and its negative are rainbow points in the span
        ah = [0] * U
        for x in range(1, k):
            for c in range(1, n):
                ah[var(x, c)] = (T3[x][c] - T3[x][0]) % 3
        mah = [(3 - v) % 3 for v in ah]

        def index_of(vec):
            z = [vec[f] for f in free]
            A = [0] * U
            for zr, b in zip(z, basis):
                if zr:
                    A = [(av + zr * bv) % 3 for av, bv in zip(A, b)]
            if A != vec:
                return None
            idx = 0
            for zr in z:
                idx = idx * 3 + zr
            return idx

        ia, ima = index_of(ah), index_of(mah)
        if ia is None or ima is None or ia not in rainbow or ima not in rainbow:
            raise Stop(4, "SELF_CHECK", "alpha_hat or minus_alpha_hat is not a listed rainbow point")
        summary.update({"rainbow_count": len(rainbow), "alpha_hat_idx": ia, "minus_alpha_hat_idx": ima})
        own = os.path.abspath(__file__)
        cert = {"format": FORMAT, "anchor_sha256": h, "n": n, "q": q, "k": k, "U": U, "J": J, "dim": dim,
                "basis": basis, "free_columns": free, "rank_witness": witness, "rainbow": rainbow,
                "failures": failures,
                "producer": {"name": os.path.basename(own), "sha256": hashlib.sha256(open(own, "rb").read()).hexdigest()}}
        text = json.dumps(cert, sort_keys=True, separators=(",", ":")) + "\n"
        with open(a.out, "x") as fh:
            fh.write(text)
        summary.update({"status": "OK", "cert_path": os.path.abspath(a.out),
                        "cert_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
        code = 0
    except Stop as s:
        summary.update({"status": s.status, "reason": s.reason})
        code = s.code
    summary["wall_s"] = round(time.monotonic() - t0, 3)
    print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
