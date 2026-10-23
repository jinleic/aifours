#!/usr/bin/env python3
"""Independent SAT encoding of normalized (Z_N, K; 1) difference matrices, optionally restricted to a
column-multiset action sigma = (mu, pi) (lane cfr33/cfr21, C21 involution / cyclic-action SAT v1).
Encoder and decoder in one file; no child process is ever started.

Usage
  involution_cnf_c21v1.py encode --n N --k K --mu MU --pi P0,...,P{K-1} [--no-zero-gauge]
                                 [--calibration-plant DM] [--max-bytes B] OUT
  involution_cnf_c21v1.py encode --n N --k K --no-sym [--no-zero-gauge] [--calibration-plant DM]
                                 [--max-bytes B] OUT
  involution_cnf_c21v1.py decode OUT.map.json SOLVER_STDOUT CANDIDATE.dmraw

  Frozen involution targets g00, g10, g16 (specs/groups-v1/specs, gens [[mu, [0,2,1,4,3,6,5]]]):
    encode --n 21 --k 7 --pi 0,2,1,4,3,6,5 --mu 1|8|13 OUT
  Order-3 row cycling (1 2 3)(4 5 6):
    encode --n 21 --k 7 --pi 0,2,3,1,5,6,4 --mu 4|16 --no-zero-gauge OUT

encode
  Writes OUT.cnf (DIMACS) and then OUT.map.json, both exclusive-create; a .cnf without its .map.json is
  incomplete and must not be used. The clause stream is generated twice: pass 1 counts clauses and bytes and
  stops, before any file exists, once --max-bytes (default 64 MiB) would be exceeded; pass 2 writes and hashes.
  Memory is O(variables); identical arguments and plant bytes give byte-identical outputs.
  --calibration-plant DM adds a unit clause for every unknown entry of a dm-raw matrix that is in the selected
  gauge (calibration only, labelled in the map, never a target production CNF). The plant need not be a DM or
  invariant: such plants make the CNF unsatisfiable and serve as negative controls.
decode
  Requires exactly one status line 's SATISFIABLE' and a '0'-terminated 'v' assignment (kissat/CaDiCaL stdout)
  that assigns every X variable, rebuilds the complete K x N matrix, checks by definition every row pair and, if
  an action was encoded, column-multiset invariance, compares with the plant if any, and only then writes
  CANDIDATE.dmraw (K LF-terminated lines of N single-space-separated decimals, the dm_check_c21v1.py format)
  with mode 'x'. Any failure prints 'DECODE REJECT: ...', exits 1 and writes nothing. The map must have been
  written by this exact source file (SHA-256 compared).

Model
  DM: K x N array A over Z_N (integers mod N, no field arithmetic) such that for all rows i < j the map
  c -> A[i][c] - A[j][c] is a bijection of Z_N.
  Action sigma = (mu, pi) on columns c in Z_N^K: (sigma c)[pi[r]] = mu*c[r] mod N, the convention of
  audit_group_invariance_c21v1.py and of generators [mu, pi] in specs/groups-v1. Required, else rejected:
  pi is a permutation of the rows with pi[0] = 0, and mu is a unit in 1..N-1 (sigma then has order
  lcm(ord(pi), ord(mu)); mu^ord(pi) = 1 is the special case ord(sigma) = ord(pi)). The restricted model: the
  column multiset of A is sigma-invariant. --no-sym: no action.
  Gauge. Always A[0][t] = 0, and columns are indexed by their row-1 entry, A[1][t] = t. This loses nothing in
  any model: subtracting row 0 columnwise preserves every row difference and commutes with sigma (pi[0] = 0 and
  sigma is additive); re-indexing does not change the column multiset.
  Zero gauge (default): additionally A[r][0] = 0 for every r. Complete (a) without an action: translate each
  row r >= 2 by -A[r][0]; (b) for an involution sigma (pi^2 = id, mu^2 = 1 mod N) with N odd: after the first
  step the N columns are distinct and sigma permutes them with sigma^2 = 1, so odd N gives a column
  c* = sigma(c*); subtracting c* from every column keeps sigma-invariance; re-index by row 1. Any other action
  is rejected in the zero gauge (e.g. order 3 admits fixed-point-free column actions): pass --no-zero-gauge,
  which leaves column 0 free.
  Unknowns: F_r(t) = A[r][t] for r = 2..K-1 and t in T, where T = 1..N-1 in the zero gauge (then necessarily
  F_r(t) is neither 0 nor t: rows 0 and 1 differ from row r by bijections vanishing at t = 0), else T = 0..N-1.
  No other symmetry breaking; nothing is assumed about fixed points of h beyond the chosen gauge.
  Relation. Column t is c(t) = (0, t, F_2(t), ..., F_{K-1}(t)); sigma(c(t)) has row-1 entry mu*F_p(t), where
  p = pi^-1(1). The columns are distinct and sigma is injective, so invariance holds iff sigma(c(t)) = c(h(t))
  for every t, with h(t) = mu*F_p(t); that is, iff F_{pi[r]}(h(t)) = mu*F_r(t) for all r and t. Rows 0 and p
  satisfy it identically, and so does column 0 in the zero gauge. If p = 1 then h(t) = mu*t (linear action).
  For an involution sigma, p = pi[1] and the r = 1 relation F_p(h(t)) = mu*t gives h^2 = id.

Variables (1-based, X first, lexicographic; complete tables in the map)
  X[r,t,v]    F_r(t) = v           r = 2..K-1, t in T, v in V(t): zero gauge V(t) = 1..N-1 minus t, else 0..N-1.
              id = ((r-2)*|T| + t - t0)*|V| + i + 1, t0 = min T, i = position of v in V(t).
  D[r,s,t,d]  F_r(t) - F_s(t) = d  2 <= r < s <= K-1, t in T, d in T (in the zero gauge d != 0).
              id = #X + (q*|T| + t - t0)*|T| + d - t0 + 1, q = lexicographic index of the pair (r, s).
Clause families ('exactly one' = one at-least-one clause plus every pairwise at-most-one clause)
  F_ROW    exactly one v per (r, t).
  F_COL    exactly one t per (r, v): F_r is a bijection (row pair 0, r).
  F_ID     exactly one t with F_r(t) = t + d per (r, d in T): F_r - id is a bijection (row pair 1, r). The
           pairwise at-most-one part alone suffices (|T| columns map injectively into |T| residues); the
           at-least-one clause is redundant.
  D_LINK   X[r,t,a] & X[s,t,b] -> D[r,s,t,a-b]; in the zero gauge a = b gives not (X[r,t,a] & X[s,t,a]).
  D_ROW    exactly one d per (r, s, t).
  D_COL    exactly one t per (r, s, d): F_r - F_s is a bijection (row pair r, s).
           No reverse link D -> X is needed: in a model F_ROW fixes a = F_r(t) and b = F_s(t), D_LINK makes
           D[r,s,t,a-b] true and D_ROW makes every other D[r,s,t,.] false, so D is exactly the difference table
           and D_COL is exactly the bijection condition; conversely every gauge DM satisfies all clauses with D
           set to its difference table.
  SYM_LIN  (p = 1) X[r,t,v] -> X[pi[r],mu*t,mu*v] for r = 2..K-1.
  SYM_ROW1 (p != 1) X[p,t,mu^-1*s] -> X[pi[1],s,mu*t]: the r = 1 relation, guarded by h(t) = s.
  SYM_ROW  (p != 1) X[p,t,mu^-1*s] & X[r,t,v] -> X[pi[r],s,mu*v] for r = 2..K-1, r != p (pi[r] is then an
           unknown row). If the consequent is constant false (only possible in the zero gauge, exactly when
           mu*v = s) the clause equals the D_LINK zero clause not (X[p,t,a] & X[r,t,a]) with a = mu^-1*s and is
           not emitted again; any other constant-false consequent aborts as an internal error.
  PLANT    calibration units X[r,t,A[r][t]].
  With exactly one true X per (r, t), the guarded clauses state the relation for every r and t, so the models
  of the CNF are exactly the gauge DMs of the chosen model, each with its difference tables. Gauge constants
  are substituted (a true literal drops the clause, a false literal is removed); tautologies are dropped and
  counted in the map; no clause is emitted twice (N >= 4).
"""
import argparse
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter
from pathlib import Path

MAP_FORMAT = "involution-cnf-c21v1-map"
DEFAULT_MAX_BYTES = 64 * 1024 * 1024
TOKEN = re.compile(r"(0|[1-9][0-9]*)\Z")
LITERAL = re.compile(r"(0|-?[1-9][0-9]*)\Z")
SOURCE_SHA256 = hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()


class Reject(Exception):
    """Invalid input or failed check; reported as '<COMMAND> REJECT: ...' with exit status 1."""


def lcm(a, b):
    return a * b // math.gcd(a, b)


def permutation_order(pi):
    order, seen = 1, set()
    for start in range(len(pi)):
        length, j = 0, start
        while j not in seen:
            seen.add(j)
            j = pi[j]
            length += 1
        if length:
            order = lcm(order, length)
    return order


def sigma_order(mu, pi, n):
    """Order of sigma = (mu, pi): lcm of ord(pi) and the multiplicative order of the unit mu mod N."""
    order, power = 1, mu % n
    while power != 1:
        power = power * mu % n
        order += 1
    return lcm(permutation_order(pi), order)


def check_model(n, k, sym, mu, pi, zero):
    if type(n) is not int or type(k) is not int or n < 4:
        raise Reject("N must be an integer >= 4")
    if not 3 <= k <= n:
        raise Reject("K must satisfy 3 <= K <= N")
    if type(sym) is not bool or type(zero) is not bool:
        raise Reject("symmetric/zero-gauge flags must be booleans")
    if not sym:
        if mu is not None or pi is not None:
            raise Reject("--no-sym excludes --mu and --pi")
        return
    if type(mu) is not int or type(pi) is not list:
        raise Reject("an action needs both --mu and --pi (or use --no-sym)")
    if any(type(e) is not int for e in pi) or sorted(pi) != list(range(k)):
        raise Reject("pi must list the images pi[0], ..., pi[K-1] of a permutation of the K rows")
    if pi[0] != 0:
        raise Reject("pi must fix row 0")
    if not 1 <= mu < n or math.gcd(mu, n) != 1:
        raise Reject("mu must be a unit mod N in 1..N-1")
    if zero and (any(pi[pi[r]] != r for r in range(k)) or mu * mu % n != 1 or n % 2 == 0):
        raise Reject("the zero gauge is proven complete only without an action or for an involution sigma "
                     "(pi^2 = id and mu^2 = 1 mod N) with odd N; pass --no-zero-gauge")


class Model:
    """Parameters, gauge constants and the closed-form variable numbering of the module docstring."""

    def __init__(self, n, k, sym, mu, pi, zero):
        check_model(n, k, sym, mu, pi, zero)
        self.n, self.k, self.sym, self.mu, self.pi, self.zero = n, k, sym, mu, pi, zero
        self.p = pi.index(1) if sym else None
        self.free = range(1, n) if zero else range(n)
        self.t0, self.w = self.free[0], len(self.free)
        self.nvals = n - 2 if zero else n
        m = k - 2
        self.nx = m * self.w * self.nvals
        self.nvars = self.nx + m * (m - 1) // 2 * self.w * self.w

    def ok(self, t, v):
        """(t, v) is a possible unknown entry F_r(t) = v."""
        return t in self.free and v in self.free and not (self.zero and v == t)

    def dom(self, t):
        return [v for v in self.free if self.ok(t, v)]

    def x(self, r, t, v):
        """Literal of F_r(t) = v (t, v taken mod N): a gauge constant (bool) or a variable number."""
        n = self.n
        t, v = t % n, v % n
        if r == 0:
            return v == 0
        if r == 1:
            return v == t
        if self.zero and t == 0:
            return v == 0
        if not self.ok(t, v):
            return False
        i = (v - 1 if v < t else v - 2) if self.zero else v
        return ((r - 2) * self.w + t - self.t0) * self.nvals + i + 1

    def d(self, r, s, t, dd):
        """Variable of F_r(t) - F_s(t) = dd for 2 <= r < s <= K-1, t and dd in T."""
        m, a, b = self.k - 2, r - 2, s - 2
        q = a * (m - 1) - a * (a - 1) // 2 + (b - a - 1)
        return self.nx + (q * self.w + t - self.t0) * self.w + dd - self.t0 + 1


def neg(lit):
    return (not lit) if type(lit) is bool else -lit


def normalize_clause(lits):
    """Substitute constants; None for a satisfied clause or tautology."""
    out = []
    for lit in lits:
        if lit is True:
            return None
        if lit is False:
            continue
        if -lit in out:
            return None
        if lit not in out:
            out.append(lit)
    if not out:
        raise Reject("internal error: empty clause")
    return out


def clause_line(clause):
    return " ".join(map(str, clause)) + " 0\n"


def raw_clauses(model, plant):
    """Yield (family, literals) in a fixed order; literals may still contain gauge constants."""
    n, k, mu, pi, x, d, free = model.n, model.k, model.mu, model.pi, model.x, model.d, model.free
    unknown = range(2, k)

    def exactly_one(family, lits):
        yield family, lits
        for i in range(len(lits)):
            for j in range(i + 1, len(lits)):
                yield family, [neg(lits[i]), neg(lits[j])]

    for r in unknown:
        for t in free:
            yield from exactly_one("F_ROW", [x(r, t, v) for v in model.dom(t)])
    for r in unknown:
        for v in free:
            yield from exactly_one("F_COL", [x(r, t, v) for t in free if model.ok(t, v)])
    for r in unknown:
        for dd in free:
            yield from exactly_one("F_ID", [x(r, t, t + dd) for t in free if model.ok(t, (t + dd) % n)])
    for r in unknown:
        for s in range(r + 1, k):
            for t in free:
                values = model.dom(t)
                for a in values:
                    for b in values:
                        if model.zero and a == b:
                            yield "D_LINK", [neg(x(r, t, a)), neg(x(s, t, a))]
                        else:
                            yield "D_LINK", [neg(x(r, t, a)), neg(x(s, t, b)), d(r, s, t, (a - b) % n)]
                yield from exactly_one("D_ROW", [d(r, s, t, dd) for dd in free])
            for dd in free:
                yield from exactly_one("D_COL", [d(r, s, t, dd) for t in free])
    if model.sym:
        p = model.p
        if p == 1:
            for r in unknown:
                for t in free:
                    for v in model.dom(t):
                        yield "SYM_LIN", [neg(x(r, t, v)), x(pi[r], mu * t, mu * v)]
        else:
            mu_inv = pow(mu, -1, n)
            for r in [1] + [r for r in unknown if r != p]:
                family = "SYM_ROW1" if r == 1 else "SYM_ROW"
                for t in free:
                    values = [t] if r == 1 else model.dom(t)
                    for s in range(n):
                        g = x(p, t, mu_inv * s)
                        if g is False:
                            continue
                        for v in values:
                            c = x(pi[r], s, mu * v)
                            if c is False:
                                if not (model.zero and r != 1 and mu * v % n == s):
                                    raise Reject("internal error: unexpected constant-false consequent")
                                continue
                            yield family, [neg(g), neg(x(r, t, v)), c]
    if plant is not None:
        for r in unknown:
            for t in free:
                yield "PLANT", [x(r, t, plant[r][t])]


def variable_tables(model):
    k, free = model.k, model.free
    xmap = [[r, t, v, model.x(r, t, v)] for r in range(2, k) for t in free for v in model.dom(t)]
    dmap = [[r, s, t, dd, model.d(r, s, t, dd)]
            for r in range(2, k) for s in range(r + 1, k) for t in free for dd in free]
    if [e[-1] for e in xmap + dmap] != list(range(1, model.nvars + 1)):
        raise Reject("internal error: variable numbering is not 1..%d in table order" % model.nvars)
    return xmap, dmap


def parse_pi(text):
    toks = text.split(",")
    if not all(TOKEN.match(tok) for tok in toks):
        raise Reject("--pi must be comma-separated canonical decimals, e.g. 0,2,1,4,3,6,5")
    return [int(tok) for tok in toks]


def read_plant(raw, model):
    n, k = model.n, model.k
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        raise Reject("plant is not ASCII")
    if not text.endswith("\n") or "\r" in text:
        raise Reject("plant must consist of LF-terminated lines")
    lines = text[:-1].split("\n")
    if len(lines) != k:
        raise Reject("plant has %d rows, expected K = %d" % (len(lines), k))
    matrix = []
    for i, line in enumerate(lines):
        toks = line.split(" ")
        if len(toks) != n or not all(TOKEN.match(tok) for tok in toks):
            raise Reject("plant row %d is not %d single-space-separated decimals" % (i, n))
        row = [int(tok) for tok in toks]
        if max(row) >= n:
            raise Reject("plant row %d has an entry >= N" % i)
        matrix.append(row)
    if any(matrix[0]) or matrix[1] != list(range(n)):
        raise Reject("plant is not in the gauge: row 0 must be 0 and row 1 must be 0..N-1")
    for r in range(2, k):
        for t in range(n):
            if model.x(r, t, matrix[r][t]) is False:
                raise Reject("plant entry A[%d][%d] = %d is outside the %s gauge domain"
                             % (r, t, matrix[r][t], "zero" if model.zero else "free"))
    return matrix


def model_description(model):
    n, zero = model.n, model.zero
    desc = {
        "n": n, "k": model.k, "symmetric": model.sym, "mu": model.mu, "pi": model.pi, "zero_gauge": zero,
        "arithmetic": "cyclic Z_N (integers mod N); no field arithmetic",
        "dm_definition": "K x N array A; for every row pair i < j, c -> A[i][c] - A[j][c] mod N is a bijection",
        "gauge": ("A[0][t] = 0, A[1][t] = t, A[r][0] = 0; unknown F_r(t) = A[r][t] for r = 2..K-1, t = 1..N-1, "
                  "F_r(t) not in {0, t}" if zero else
                  "A[0][t] = 0, A[1][t] = t; unknown F_r(t) = A[r][t] for r = 2..K-1, t = 0..N-1 (column 0 free)"),
        "decoded_matrix": "dm-raw row r, column t is F_r(t); row 0 is 0 and row 1 is t",
    }
    if not zero:
        desc["gauge_completeness"] = ("complete for every N and every admissible (mu, pi): subtract row 0 "
                                      "columnwise (commutes with sigma since pi[0] = 0), index columns by row 1")
    elif not model.sym:
        desc["gauge_completeness"] = ("complete for every N without an action: subtract row 0 columnwise, "
                                      "index columns by row 1, translate each row r >= 2 by -A[r][0]")
    else:
        desc["gauge_completeness"] = ("complete for involutions with odd N: subtract row 0 columnwise (commutes "
                                      "with sigma), index columns by row 1; sigma permutes the N distinct columns "
                                      "with sigma^2 = 1, so a column c* = sigma(c*) exists; subtracting c* from "
                                      "every column keeps sigma-invariance; index columns by row 1 again")
    if model.sym:
        p, mu = model.p, model.mu
        desc.update({
            "action": "sigma = (mu, pi) on columns: (sigma c)[pi[r]] = mu*c[r] mod N; the column multiset of A is "
                      "sigma-invariant (convention of audit_group_invariance_c21v1.py and of generators [mu, pi] "
                      "in specs/groups-v1)",
            "sigma_order": sigma_order(mu, model.pi, n),
            "p": p,
            "h": ("h(t) = mu*t mod N (pi fixes row 1; linear action)" if p == 1 else
                  "h(t) = mu*F_%d(t) mod N, p = pi^-1(1) = %d" % (p, p)),
            "guard": ("none: h is known" if p == 1 else
                      "h(t) = s <=> X[%d,t,%d*s] (mu^-1 = %d)" % (p, pow(mu, -1, n), pow(mu, -1, n))),
            "relation": "F_{pi[r]}(h(t)) = mu*F_r(t) mod N for every row r and column t (sigma maps column t "
                        "to column h(t))",
            "scope": "restricted model: SAT yields a candidate for the independent gates; UNSAT excludes only "
                     "(mu, pi)-invariant DMs in this gauge, never unrestricted DM/CFR existence",
        })
    return desc


def use_label(model, planted):
    if planted:
        return ("CALIBRATION ONLY: unit clauses fix every unknown entry to a supplied matrix; never a target "
                "production CNF")
    if model.sym:
        return "restricted symmetric model (see model.scope)"
    return "unrestricted normalized model (gauge complete, see model.gauge_completeness)"


def write_cnf(path, model, plant, header):
    digest, count, size = hashlib.sha256(), 0, 0
    with open(path, "xb") as fh:
        def put(text):
            nonlocal size
            data = text.encode("ascii")
            fh.write(data)
            digest.update(data)
            size += len(data)

        put(header)
        chunk = []
        for _family, lits in raw_clauses(model, plant):
            clause = normalize_clause(lits)
            if clause is None:
                continue
            chunk.append(clause_line(clause))
            count += 1
            if len(chunk) == 65536:
                put("".join(chunk))
                chunk = []
        put("".join(chunk))
    return count, size, digest.hexdigest()


def encode(args):
    pi = None if args.pi is None else parse_pi(args.pi)
    model = Model(args.n, args.k, not args.no_sym, args.mu, pi, not args.no_zero_gauge)
    if args.max_bytes < 1:
        raise Reject("--max-bytes must be positive")
    plant = plant_record = None
    if args.calibration_plant is not None:
        raw = Path(args.calibration_plant).read_bytes()
        plant = read_plant(raw, model)
        plant_record = {"path": args.calibration_plant, "sha256": hashlib.sha256(raw).hexdigest(),
                        "matrix": plant}
    cnf_path, map_path = args.out + ".cnf", args.out + ".map.json"
    for path in (cnf_path, map_path):
        if os.path.lexists(path):
            raise Reject("refusing to overwrite %s" % path)

    families, tautologies, nclauses, body = Counter(), Counter(), 0, 0
    for family, lits in raw_clauses(model, plant):
        clause = normalize_clause(lits)
        if clause is None:
            tautologies[family] += 1
            continue
        families[family] += 1
        nclauses += 1
        body += len(clause_line(clause))
        if body > args.max_bytes:
            raise Reject("the CNF would exceed --max-bytes %d; nothing written" % args.max_bytes)
    header = "p cnf %d %d\n" % (model.nvars, nclauses)
    size = len(header) + body
    if size > args.max_bytes:
        raise Reject("the CNF would exceed --max-bytes %d; nothing written" % args.max_bytes)
    xmap, dmap = variable_tables(model)

    try:
        written = write_cnf(cnf_path, model, plant, header)
    except OSError as exc:
        raise Reject("writing %s failed (%s); any partial file has no map and must not be used" % (cnf_path, exc))
    if written[:2] != (nclauses, size):
        raise Reject("internal error: pass 2 differs from pass 1; %s has no map and must not be used" % cnf_path)
    cnf_sha = written[2]

    m = model.k - 2
    info = {
        "format": MAP_FORMAT,
        "encoder": {"file": Path(__file__).name, "sha256": SOURCE_SHA256},
        "use": use_label(model, plant is not None),
        "model": model_description(model),
        "plant": plant_record,
        "cnf": {"file": Path(cnf_path).name, "sha256": cnf_sha, "bytes": size, "variables": model.nvars,
                "clauses": nclauses},
        "clause_families": dict(families),
        "tautologies_dropped": dict(tautologies),
        "variables": {
            "T": "1..N-1" if model.zero else "0..N-1",
            "X": {"first": 1, "last": model.nx, "count": model.nx, "meaning": "X[r,t,v] true iff F_r(t) = v",
                  "order": "lexicographic (r, t, v): r = 2..K-1, t in T, v in V(t)"},
            "D": {"first": model.nx + 1, "last": model.nvars, "count": model.nvars - model.nx,
                  "pairs": m * (m - 1) // 2,
                  "meaning": "D[r,s,t,d] true iff F_r(t) - F_s(t) = d mod N",
                  "order": "lexicographic (r, s, t, d): 2 <= r < s <= K-1, t in T, d in T"},
        },
        "xmap": xmap,
        "dmap": dmap,
    }
    text = (json.dumps(info, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    with open(map_path, "xb") as fh:
        fh.write(text)
    print(json.dumps({"cnf": cnf_path, "cnf_sha256": cnf_sha, "map": map_path,
                      "map_sha256": hashlib.sha256(text).hexdigest(), "variables": model.nvars,
                      "clauses": nclauses, "bytes": size, "clause_families": dict(families),
                      "tautologies_dropped": dict(tautologies), "use": info["use"],
                      "encoder_sha256": SOURCE_SHA256}, sort_keys=True))


def read_assignment(raw, nvars):
    status, value, ended = [], {}, False
    for line in raw.decode("utf-8", errors="replace").splitlines():
        if line.startswith("s "):
            status.append(line.rstrip())
        elif line.startswith("v "):
            for tok in line.split()[1:]:
                if ended or not LITERAL.match(tok):
                    raise Reject("malformed or trailing value token %r" % tok)
                lit = int(tok)
                if lit == 0:
                    ended = True
                elif abs(lit) > nvars or abs(lit) in value:
                    raise Reject("literal %d is out of range or repeated" % lit)
                else:
                    value[abs(lit)] = lit > 0
    if status != ["s SATISFIABLE"]:
        raise Reject("solver status lines %r; exactly ['s SATISFIABLE'] is required" % status)
    if not ended:
        raise Reject("the 'v' assignment lacks its terminating 0")
    return value


def check_rows(matrix, n):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if sorted((matrix[i][c] - matrix[j][c]) % n for c in range(n)) != list(range(n)):
                raise Reject("rows %d and %d: differences are not a permutation of Z_%d" % (i, j, n))


def check_action(matrix, n, mu, pi):
    k = len(matrix)
    columns = Counter(tuple(matrix[r][c] for r in range(k)) for c in range(n))
    images = Counter()
    for column, multiplicity in columns.items():
        image = [0] * k
        for r in range(k):
            image[pi[r]] = mu * column[r] % n
        images[tuple(image)] += multiplicity
    if images != columns:
        raise Reject("the column multiset is not invariant under (mu, pi) = (%d, %s)" % (mu, pi))


def decode(args):
    map_raw = Path(args.map).read_bytes()
    info = json.loads(map_raw.decode("ascii"))
    if type(info) is not dict or info.get("format") != MAP_FORMAT:
        raise Reject("%s is not a %s file" % (args.map, MAP_FORMAT))
    if info["encoder"]["sha256"] != SOURCE_SHA256:
        raise Reject("map written by encoder source %s, but this decoder is %s"
                     % (info["encoder"]["sha256"], SOURCE_SHA256))
    desc = info["model"]
    model = Model(desc["n"], desc["k"], desc["symmetric"], desc["mu"], desc["pi"], desc["zero_gauge"])
    n, k, zero = model.n, model.k, model.zero
    nvars = info["cnf"]["variables"]
    if type(nvars) is not int or nvars < 1:
        raise Reject("map has no valid variable count")
    cols = range(1, n) if zero else range(n)
    expected = {(r, t, v) for r in range(2, k) for t in cols for v in cols if not (zero and v == t)}
    xvar = {}
    for entry in info["xmap"]:
        if type(entry) is not list or len(entry) != 4 or any(type(e) is not int for e in entry):
            raise Reject("malformed xmap entry %r" % (entry,))
        key, var = tuple(entry[:3]), entry[3]
        if key in xvar or not 1 <= var <= nvars:
            raise Reject("xmap entry %r is repeated or out of range" % (entry,))
        xvar[key] = var
    if set(xvar) != expected or len(set(xvar.values())) != len(xvar):
        raise Reject("xmap does not map the X domain injectively")

    solver_raw = Path(args.solver_out).read_bytes()
    value = read_assignment(solver_raw, nvars)
    matrix = [[0] * n, list(range(n))]
    for r in range(2, k):
        row = [0] * n
        for t in cols:
            hits = []
            for v in cols:
                if zero and v == t:
                    continue
                var = xvar[(r, t, v)]
                if var not in value:
                    raise Reject("X[%d,%d,%d] (variable %d) is not assigned" % (r, t, v, var))
                if value[var]:
                    hits.append(v)
            if len(hits) != 1:
                raise Reject("row %d column %d has %d true values" % (r, t, len(hits)))
            row[t] = hits[0]
        matrix.append(row)
    check_rows(matrix, n)
    if model.sym:
        check_action(matrix, n, model.mu, model.pi)
    plant = info["plant"]
    if plant is not None and plant["matrix"] != matrix:
        raise Reject("decoded matrix differs from the planted calibration matrix")

    text = "".join(" ".join(map(str, row)) + "\n" for row in matrix).encode("ascii")
    with open(args.candidate, "xb") as fh:
        fh.write(text)
    print(json.dumps({"candidate": args.candidate, "candidate_sha256": hashlib.sha256(text).hexdigest(),
                      "n": n, "k": k, "symmetric": model.sym, "mu": model.mu, "pi": model.pi,
                      "zero_gauge": zero, "row_pairs_checked": k * (k - 1) // 2,
                      "action_checked": model.sym, "planted": plant is not None, "use": info["use"],
                      "map_sha256": hashlib.sha256(map_raw).hexdigest(),
                      "solver_out_sha256": hashlib.sha256(solver_raw).hexdigest(),
                      "decoder_sha256": SOURCE_SHA256}, sort_keys=True))
    print("DECODE PASS (definition and claimed action rechecked; independent gates still required)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    enc = sub.add_parser("encode", allow_abbrev=False)
    enc.add_argument("--n", type=int, required=True)
    enc.add_argument("--k", type=int, required=True)
    enc.add_argument("--mu", type=int)
    enc.add_argument("--pi", help="images pi[0],...,pi[K-1], comma-separated")
    enc.add_argument("--no-sym", action="store_true")
    enc.add_argument("--no-zero-gauge", action="store_true")
    enc.add_argument("--calibration-plant", metavar="DM")
    enc.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    enc.add_argument("out", metavar="OUT")
    dec = sub.add_parser("decode", allow_abbrev=False)
    dec.add_argument("map", metavar="MAP_JSON")
    dec.add_argument("solver_out", metavar="SOLVER_STDOUT")
    dec.add_argument("candidate", metavar="CANDIDATE_DMRAW")
    args = parser.parse_args()
    try:
        encode(args) if args.command == "encode" else decode(args)
    except Reject as exc:
        print("%s REJECT: %s" % (args.command.upper(), exc))
        sys.exit(1)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("%s REJECT: %s: %s" % (args.command.upper(), type(exc).__name__, exc))
        sys.exit(1)


if __name__ == "__main__":
    main()
