#!/usr/bin/env python3
"""PA19 96h lane probe 16 (structural, planning only): exhaustive feasibility of a block-level relaxation
("GPS-2F + Q2P + QPL + LINK") for selected open ms06 cases. No solver, checker or CNF.

Setting. An ms06 case b has N=19 rows with P0 quad sets T(r) in {0..5} (build_v2 member order), 6 P0
columns (one quad and five triples each) and 2 P1 columns 6, 7 (blocks 4,4,3,3,3,2), with L=1. A valid
array gives, for each column, the partition of the rows into equal-symbol blocks. The validity facts used are:
  V1  two rows share at most one block over all 8 columns;
  V2  exactly one pair D shares no block, and every other pair shares exactly one block (counting:
      6*(6+15) + 2*(6+6+3+3+3+1) = 170 = C(19,2) - 1).
From V1 and V2 this probe checks the existence of
  (E, D)  a GPS-1 key: the P1 pair blocks P6, P7 and D. For the unordered E the probe takes P6 = E[0] and
          P7 = E[1], which loses nothing because every condition below is symmetric under exchanging columns
          6 and 7;
  n2(r), l(r), n4(r) = 2 - l - t + n2  (row identity), which forces each row's block types (Q = quad,
          P = pair, T = triple) in columns 6 and 7;
  quads   A6, B6 (column 6) and A7, B7 (column 7), each a 4-set of pairwise T-disjoint rows (V1 against the
          P0 quads), D not inside one block, each pair block not inside a block of the other column, and
          |X ∩ Y| <= 1 for every column-6 quad X and column-7 quad Y (V1);
  triples three per P1 column on the remaining 9 rows, each pairwise T-disjoint, with D not inside, meeting every
          block of the other P1 column in <= 1 row (V1);
  Q2P     for each P1 column j (other column k), with S = A_j ∪ B_j:
            q_j + ell_j <= 1 + 2 |S ∩ P_k| - |S ∩ D|,
          where q_j = |T(A_j) ∩ T(B_j)| + #{A_j-B_j cross pairs inside A_k, B_k or P_k} and ell_j = [D is an
          A_j-B_j cross pair] (notes/production-plan-v1.md cites the lemma; the derivation is in the standalone
          note that accompanies any use of this probe);
  QPL     for each P1 column j: |T(A_j) ∪ T(B_j)| >= 2 + qk_j + ell_j + x2k_j, where qk_j is the second
          summand of q_j and x2k_j = #{column-k triples meeting both A_j and B_j} (P0-column pigeonhole);
  LINK    with G_res = all pairs minus D minus pairs inside P0 quads or P1 blocks, every row r has exactly
          2(6 - t(r)) G_res-neighbours, and these neighbours split into 6 - t(r) pairs {s, w} with s-w in G_res,
          each pair assigned a distinct P0 column c not in T(r) ∪ T(s) ∪ T(w) (row r's P0 triples).
Status per case: FEASIBLE (witness found: the relaxation is satisfiable, NO elimination), EXHAUSTED_INFEASIBLE
(no structure exists: a CANDIDATE elimination that needs a standalone exact proof, a second implementation and
parent review before any use), or INCOMPLETE (per-case budget hit: no information).
Standard library only. The only child process is /bin/date. Admission and receipt as the other probes. Self
budget 280 s; per-case budget argv[2] seconds.
Usage: probe_ms06_gps2q2p_v1.py OUT_JSON PER_CASE_SECONDS B [B ...]
"""
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
T0 = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
SK6 = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
FRONT4 = (RUN + "/review/pa19-parent-frontier-v4.json", "5bc070391d61c6e65fb49c9851d776b5468bcd4fa60bf9bdb04a6c079c52adc4")
N = 19
FULL = (1 << N) - 1
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def pinned(path, h):
    with open(path, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED pin mismatch " + path)
    return raw


def pc(x):
    return bin(x).count("1")


def bits(x):
    out = []
    while x:
        lo = x & -x
        out.append(lo.bit_length() - 1)
        x ^= lo
    return out


class OutOfTime(Exception):
    pass


def rows_of(sk):
    types = [frozenset(t) for t in sk["types"]]
    deg = [sum(1 for t in types if v in t) for v in range(6)]
    rows = types + [frozenset([v]) for v in range(6) for _ in range(4 - deg[v])] + [frozenset()] * sk["empty"]
    if len(rows) != N or any(d > 4 for d in deg):
        raise ValueError("bad skeleton")
    return rows


def bounds(t, l):
    return max(0, t + l - 2), min(2, (t + l) // 2)


def keys(rows, conf):
    """GPS-1 keys (E, D) with E a sorted tuple of two distinct T-disjoint pairs (D first, as in the census)."""
    t = [len(r) for r in rows]
    out = []
    for d in itertools.combinations(range(N), 2):
        if conf[d[0]] >> d[1] & 1:
            continue
        b = [bounds(t[r], 1 if r in d else 0) for r in range(N)]
        if any(lo > hi for lo, hi in b):
            continue
        need = [r for r in range(N) if b[r][0] >= 1]
        elig = [r for r in range(N) if b[r][1] >= 1]
        cand = [p for p in itertools.combinations(elig, 2) if not conf[p[0]] >> p[1] & 1 and p != d]
        for e1, e2 in itertools.combinations(cand, 2):
            cnt = {}
            for r in e1 + e2:
                cnt[r] = cnt.get(r, 0) + 1
            if all(b[r][0] <= c <= b[r][1] for r, c in cnt.items()) and all(r in cnt for r in need):
                out.append((e1, e2, d))
    return out


class Case:
    def __init__(self, rows, deadline):
        self.rows = rows
        self.t = [len(r) for r in rows]
        self.T = [sum(1 << c for c in r) for r in rows]
        self.conf = [sum(1 << s for s in range(N) if s != r and self.T[r] & self.T[s]) for r in range(N)]
        self.quadmask = [sum(1 << r for r in range(N) if c in rows[r]) for c in range(6)]
        self.deadline = deadline
        self.stats = {"keys": 0, "x_choices": 0, "quad_pairs": 0, "q2p_pass": 0, "triple_pairs": 0, "qpl_pass": 0,
                      "link_checks": 0}
        self.tick = 0

    def tdisj(self, S):
        for r in bits(S):
            if self.conf[r] & S:
                return False
        return True

    def splits(self, S, dmask, forbid_pairs):
        """Unordered {A, B} with A ∪ B = S, |A| = |B| = 4, each T-disjoint, D not inside, no forbidden pair inside."""
        rs = bits(S)
        r0, rest = rs[0], rs[1:]
        out = []
        for comb in itertools.combinations(rest, 3):
            A = (1 << r0) | sum(1 << x for x in comb)
            B = S ^ A
            ok = True
            for X in (A, B):
                if not self.tdisj(X) or (X & dmask) == dmask:
                    ok = False
                    break
                for fp in forbid_pairs:
                    if (X & fp) == fp:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                out.append((A, B))
        return out

    def triple_parts(self, R, dmask, blocks_other):
        """Partitions of R (9 rows) into 3 T-disjoint triples, D not inside, each meeting every block of the other
        P1 column in <= 1 row."""
        out = []
        rs = bits(R)

        def ok(tr):
            if not self.tdisj(tr) or (tr & dmask) == dmask:
                return False
            return all(pc(tr & X) <= 1 for X in blocks_other)

        def rec(rem, acc):
            if not rem:
                out.append(tuple(acc))
                return
            rr = bits(rem)
            r0 = rr[0]
            for a, b in itertools.combinations(rr[1:], 2):
                tr = (1 << r0) | (1 << a) | (1 << b)
                if ok(tr):
                    acc.append(tr)
                    rec(rem ^ tr, acc)
                    acc.pop()
        rec(R, [])
        return out

    def time_check(self):
        self.tick += 1
        if self.tick & 255 == 0 and time.monotonic() > self.deadline:
            raise OutOfTime()

    def q_terms(self, A, B, Ak, Bk, Pk, dmask):
        TA = 0
        for r in bits(A):
            TA |= self.T[r]
        TB = 0
        for r in bits(B):
            TB |= self.T[r]
        qk = 0
        for a in bits(A):
            for b in bits(B):
                m = (1 << a) | (1 << b)
                if (Ak & m) == m or (Bk & m) == m or Pk == m:
                    qk += 1
        ell = 1 if (pc(A & dmask) == 1 and pc(B & dmask) == 1) else 0
        return TA, TB, qk, ell

    def link_ok(self, blocks, dmask):
        adj = [FULL ^ (1 << r) for r in range(N)]
        d0, d1 = bits(dmask)
        adj[d0] &= ~(1 << d1)
        adj[d1] &= ~(1 << d0)
        for X in list(self.quadmask) + list(blocks):
            for r in bits(X):
                adj[r] &= ~X
        for r in range(N):
            if pc(adj[r]) != 2 * (6 - self.t[r]):
                return False, "degree"
        for r in range(N):
            cols = [c for c in range(6) if not self.T[r] >> c & 1]
            if not self.match(adj, adj[r], 0, cols, r):
                return False, "link row %d" % r
        return True, None

    def match(self, adj, rem, used, cols, r):
        if not rem:
            return True
        s = (rem & -rem).bit_length() - 1
        cand = adj[s] & rem & ~(1 << s)
        for w in bits(cand):
            forb = self.T[s] | self.T[w]
            for c in cols:
                if used >> c & 1 or forb >> c & 1:
                    continue
                if self.match(adj, rem & ~((1 << s) | (1 << w)), used | (1 << c), cols, r):
                    return True
        return False

    def search(self):
        """Returns ('FEASIBLE', witness) or ('EXHAUSTED_INFEASIBLE', None); raises OutOfTime."""
        for e1, e2, d in keys(self.rows, self.conf):
            self.stats["keys"] += 1
            dmask = (1 << d[0]) | (1 << d[1])
            P6 = (1 << e1[0]) | (1 << e1[1])
            P7 = (1 << e2[0]) | (1 << e2[1])
            l = [1 if dmask >> r & 1 else 0 for r in range(N)]
            n2 = [(P6 >> r & 1) + (P7 >> r & 1) for r in range(N)]
            n4 = [2 - l[r] - self.t[r] + n2[r] for r in range(N)]
            R2 = sum(1 << r for r in range(N) if n4[r] == 2)
            one = [r for r in range(N) if n4[r] == 1]
            forced6 = sum(1 << r for r in one if P7 >> r & 1)
            forced7 = sum(1 << r for r in one if P6 >> r & 1)
            free = [r for r in one if not (P6 | P7) >> r & 1]
            k6 = 8 - pc(R2) - pc(forced6)
            if k6 < 0 or k6 > len(free):
                continue
            for X in itertools.combinations(free, k6):
                self.stats["x_choices"] += 1
                Xm = sum(1 << r for r in X)
                S6 = R2 | forced6 | Xm
                S7 = R2 | forced7 | (sum(1 << r for r in free) ^ Xm)
                if pc(S6) != 8 or pc(S7) != 8 or S6 & P6 or S7 & P7:
                    continue
                q6s = self.splits(S6, dmask, [P7])
                if not q6s:
                    continue
                q7s = self.splits(S7, dmask, [P6])
                if not q7s:
                    continue
                R6 = FULL ^ (S6 | P6)
                R7 = FULL ^ (S7 | P7)
                for A6, B6 in q6s:
                    for A7, B7 in q7s:
                        self.time_check()
                        self.stats["quad_pairs"] += 1
                        if pc(A6 & A7) > 1 or pc(A6 & B7) > 1 or pc(B6 & A7) > 1 or pc(B6 & B7) > 1:
                            continue
                        TA6, TB6, qk6, ell6 = self.q_terms(A6, B6, A7, B7, P7, dmask)
                        if pc(TA6 & TB6) + qk6 + ell6 > 1 + 2 * pc(S6 & P7) - pc(S6 & dmask):
                            continue
                        TA7, TB7, qk7, ell7 = self.q_terms(A7, B7, A6, B6, P6, dmask)
                        if pc(TA7 & TB7) + qk7 + ell7 > 1 + 2 * pc(S7 & P6) - pc(S7 & dmask):
                            continue
                        self.stats["q2p_pass"] += 1
                        t6s = self.triple_parts(R6, dmask, [A7, B7, P7])
                        if not t6s:
                            continue
                        t7s = self.triple_parts(R7, dmask, [A6, B6, P6])
                        for tr6 in t6s:
                            for tr7 in t7s:
                                self.time_check()
                                self.stats["triple_pairs"] += 1
                                if any(pc(x & y) > 1 for x in tr6 for y in tr7):
                                    continue
                                x2k6 = sum(1 for y in tr7 if y & A6 and y & B6)
                                if pc(TA6 | TB6) < 2 + qk6 + ell6 + x2k6:
                                    continue
                                x2k7 = sum(1 for y in tr6 if y & A7 and y & B7)
                                if pc(TA7 | TB7) < 2 + qk7 + ell7 + x2k7:
                                    continue
                                self.stats["qpl_pass"] += 1
                                self.stats["link_checks"] += 1
                                ok, why = self.link_ok([A6, B6, P6] + list(tr6) + [A7, B7, P7] + list(tr7), dmask)
                                if ok:
                                    return "FEASIBLE", {"D": list(d), "P6": list(e1), "P7": list(e2),
                                                        "A6": bits(A6), "B6": bits(B6), "triples6": [bits(x) for x in tr6],
                                                        "A7": bits(A7), "B7": bits(B7), "triples7": [bits(x) for x in tr7]}
        return "EXHAUSTED_INFEASIBLE", None


def verify_witness(rows, w):
    """Independent re-check of a FEASIBLE witness against V1/V2-derived conditions (except LINK, re-run here)."""
    T = [set(r) for r in rows]
    t = [len(r) for r in rows]
    D = set(w["D"])
    blocks6 = [set(w["A6"]), set(w["B6"]), set(w["P6"])] + [set(x) for x in w["triples6"]]
    blocks7 = [set(w["A7"]), set(w["B7"]), set(w["P7"])] + [set(x) for x in w["triples7"]]
    for blocks in (blocks6, blocks7):
        if sorted(len(x) for x in blocks) != [2, 3, 3, 3, 4, 4] or set().union(*blocks) != set(range(N)) \
                or sum(len(x) for x in blocks) != N:
            return False
        for X in blocks:
            if D <= X or any(T[a] & T[b] for a, b in itertools.combinations(sorted(X), 2)):
                return False
    for X in blocks6:
        for Y in blocks7:
            if len(X & Y) > 1:
                return False
    quads = [set(r for r in range(N) if c in T[r]) for c in range(6)]
    cover = {}
    for X in quads + blocks6 + blocks7:
        for a, b in itertools.combinations(sorted(X), 2):
            cover[(a, b)] = cover.get((a, b), 0) + 1
    if any(v > 1 for v in cover.values()) or tuple(sorted(D)) in cover:
        return False
    for r in range(N):
        l = 1 if r in D else 0
        e6 = [len(X) - 3 for X in blocks6 if r in X][0]
        e7 = [len(X) - 3 for X in blocks7 if r in X][0]
        if t[r] + e6 + e7 != 2 - l:
            return False
    return True


def main():
    out_path = os.path.abspath(sys.argv[1])
    per_case = float(sys.argv[2])
    cases = [int(x) for x in sys.argv[3:]]
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")) or not cases:
        raise SystemExit("REFUSED: bad arguments")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "structural planning probe; children /bin/date only; no solver/checker/CNF"}
    with open(receipt_path, "xb") as f:
        f.write(json.dumps(receipt, indent=1, sort_keys=True).encode())
    print("RECEIPT", receipt_path, receipt["pid"], flush=True)
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    D6 = json.loads(pinned(*SK6))
    F4 = json.loads(pinned(*FRONT4))
    open6 = {x["b_index"]: x for x in F4["ms06_undecided"]}
    results = []
    for b in cases:
        remaining = BUDGET - 10 - (time.monotonic() - T0)
        if remaining <= 1:
            results.append({"b": b, "status": "NOT_RUN_BUDGET"})
            continue
        sk = D6["skeletons"][b]
        rows = rows_of(sk)
        c = Case(rows, time.monotonic() + min(per_case, remaining))
        t1 = time.monotonic()
        try:
            status, wit = c.search()
        except OutOfTime:
            status, wit = "INCOMPLETE", None
        rec = {"b": b, "open_in_frontier_v4": b in open6, "s_tag": open6[b]["s_tag"] if b in open6 else None,
               "types": sk["types"], "empty": sk["empty"], "status": status, "seconds": round(time.monotonic() - t1, 3),
               "stats": c.stats, "witness": wit}
        if wit is not None:
            rec["witness_verified_independently"] = verify_witness(rows, wit)
            ok, why = c.link_ok([sum(1 << r for r in wit[k]) for k in ("A6", "B6", "P6")]
                                + [sum(1 << r for r in x) for x in wit["triples6"]]
                                + [sum(1 << r for r in wit[k]) for k in ("A7", "B7", "P7")]
                                + [sum(1 << r for r in x) for x in wit["triples7"]],
                                sum(1 << r for r in wit["D"]))
            rec["witness_link_recheck"] = ok
        results.append(rec)
    res = {"schema": "PA19-96H-PROBE-MS06-GPS2Q2P-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK6, "frontier_v4": FRONT4}, "per_case_seconds": per_case, "results": results,
           "scope": "planning only: FEASIBLE means the relaxation is satisfiable (no elimination); "
                    "EXHAUSTED_INFEASIBLE is a CANDIDATE needing a standalone exact proof, a second implementation and "
                    "parent review; INCOMPLETE carries no information; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data),
          [(r["b"], r["status"], r.get("seconds")) for r in results], flush=True)


if __name__ == "__main__":
    main()
