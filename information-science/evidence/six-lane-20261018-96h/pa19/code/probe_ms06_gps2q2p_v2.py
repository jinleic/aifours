#!/usr/bin/env python3
"""PA19 96h lane probe 19 (structural, planning only): exhaustive feasibility of the block-level relaxation of
notes/ms06-block-relaxation-lemmas-v2.md (330a12a6...) for selected open ms06 cases. This is v2 of
probe_ms06_gps2q2p_v1.py (89e85e32..., run once 04:14:12-04:16:12, PID 76093; b68/b151/b162 FEASIBLE,
b73/b74/b77 INCOMPLETE at 40 s). No solver, checker or CNF.

The conditions checked are exactly the v1 conditions (Lemmas 1-8 of the note):
GPS-1 key (D, P6, P7), forced block types, quads/triples per P1 column (T-disjoint, D not inside, the other
column's pair not inside), cross-column |X ∩ Y| <= 1, Q2P and QPL for both P1 columns, and LINK.
Only the search order changes. v2 adds four prefilters, each a CONSEQUENCE of those conditions, so the
feasible set is unchanged:
  F1  per P0 column c: |S_j ∩ Q_c| <= 2 and |R_j ∩ Q_c| <= 3, where S_j = quad rows and R_j = triple rows of
      column j. Blocks are T-disjoint, so Q_c meets each block of column j in at most one row.
  F2  R_j must admit a partition into 3 T-disjoint triples with D and the other column's pair P_k not inside.
      Checked once per (R_j, D, P_k) and cached; later triple choices are filtered from this cached list.
  F3  per-column Q2P with q_k dropped: |T(A)∩T(B)| + ell <= 1 + 2|S∩P_k| - |S∩D|, because q_k >= 0.
  F4  per-column QPL weakened: |T(A) ∪ T(B)| >= 2 + ell, because q_k, x2_k >= 0.
Status per case: FEASIBLE (witness found, independently re-verified: NO elimination), EXHAUSTED_INFEASIBLE
(CANDIDATE elimination: needs a second independent implementation, review of the note and a parent verdict;
not a closure), or INCOMPLETE (budget hit: no information). Per-key counters are recorded for review.
Standard library only. The only child process is /bin/date. Admission and receipt as the other probes. Self
budget 280 s; per-case budget argv[2] seconds, overridable per case as B:SECONDS.
Usage: probe_ms06_gps2q2p_v2.py OUT_JSON PER_CASE_SECONDS B[:SECONDS] [B[:SECONDS] ...]
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
FRONT5 = (RUN + "/review/pa19-parent-frontier-v5.json", "be79dede711b315bd400511d583e20d12fd453c4f4eada8f65d8aa8c2448ed9c")
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
    if any(len(rows[a] & rows[b]) > 1 for a, b in itertools.combinations(range(N), 2)):
        raise ValueError("two rows share two quads")
    return rows


def bounds(t, l):
    return max(0, t + l - 2), min(2, (t + l) // 2)


def keys(rows, conf):
    """GPS-1 keys (E, D), E a sorted tuple of two distinct T-disjoint pairs (identical to v1)."""
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
        self.part_cache = {}
        self.stats = {"keys": 0, "x_choices": 0, "f1_pass": 0, "f2_pass": 0, "f34_pass_pairs": 0, "quad_pairs": 0,
                      "q2p_pass": 0, "triple_pairs": 0, "qpl_pass": 0, "link_checks": 0}
        self.per_key = []
        self.tick = 0

    def time_check(self):
        self.tick += 1
        if self.tick & 255 == 0 and time.monotonic() > self.deadline:
            raise OutOfTime()

    def tdisj(self, S):
        for r in bits(S):
            if self.conf[r] & S:
                return False
        return True

    def quad_ok(self, S, cap):
        return all(pc(S & q) <= cap for q in self.quadmask)

    def base_parts(self, R, dmask, pk):
        key = (R, dmask, pk)
        got = self.part_cache.get(key)
        if got is not None:
            return got
        out = []

        def ok(tr):
            return self.tdisj(tr) and (tr & dmask) != dmask and (tr & pk) != pk

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
        self.part_cache[key] = out
        return out

    def splits(self, S, dmask, pk):
        rs = bits(S)
        r0, rest = rs[0], rs[1:]
        out = []
        for comb in itertools.combinations(rest, 3):
            A = (1 << r0) | sum(1 << x for x in comb)
            B = S ^ A
            if not self.tdisj(A) or not self.tdisj(B):
                continue
            if (A & dmask) == dmask or (B & dmask) == dmask or (A & pk) == pk or (B & pk) == pk:
                continue
            out.append((A, B))
        return out

    def tunion(self, X):
        u = 0
        for r in bits(X):
            u |= self.T[r]
        return u

    def colfilter(self, q, S, Pk, dmask):
        """F3 and F4 on one column's quad splits; returns [(A, B, TA, TB, ell)]."""
        out = []
        rhs = 1 + 2 * pc(S & Pk) - pc(S & dmask)
        for A, B in q:
            TA, TB = self.tunion(A), self.tunion(B)
            ell = 1 if (pc(A & dmask) == 1 and pc(B & dmask) == 1) else 0
            if pc(TA & TB) + ell > rhs:
                continue
            if pc(TA | TB) < 2 + ell:
                continue
            out.append((A, B, TA, TB, ell))
        return out

    def qk(self, A, B, Ak, Bk, Pk):
        n = 0
        for a in bits(A):
            for b in bits(B):
                m = (1 << a) | (1 << b)
                if (Ak & m) == m or (Bk & m) == m or Pk == m:
                    n += 1
        return n

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
                return False
        for r in range(N):
            cols = [c for c in range(6) if not self.T[r] >> c & 1]
            if not self.match(adj, adj[r], 0, cols):
                return False
        return True

    def match(self, adj, rem, used, cols):
        if not rem:
            return True
        s = (rem & -rem).bit_length() - 1
        for w in bits(adj[s] & rem & ~(1 << s)):
            forb = self.T[s] | self.T[w]
            for c in cols:
                if used >> c & 1 or forb >> c & 1:
                    continue
                if self.match(adj, rem & ~((1 << s) | (1 << w)), used | (1 << c), cols):
                    return True
        return False

    def search(self):
        for e1, e2, d in keys(self.rows, self.conf):
            self.stats["keys"] += 1
            kstat = {"key": [list(e1), list(e2), list(d)], "x": 0, "f1": 0, "f2": 0, "pairs": 0}
            self.per_key.append(kstat)
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
            freemask = sum(1 << r for r in free)
            k6 = 8 - pc(R2) - pc(forced6)
            if k6 < 0 or k6 > len(free):
                continue
            base6, base7 = R2 | forced6, R2 | forced7
            if not (self.quad_ok(base6, 2) and self.quad_ok(base7, 2)):
                continue
            for X in itertools.combinations(free, k6):
                self.time_check()
                self.stats["x_choices"] += 1
                kstat["x"] += 1
                Xm = sum(1 << r for r in X)
                S6 = base6 | Xm
                S7 = base7 | (freemask ^ Xm)
                if pc(S6) != 8 or pc(S7) != 8:
                    continue
                R6 = FULL ^ (S6 | P6)
                R7 = FULL ^ (S7 | P7)
                if not (self.quad_ok(S6, 2) and self.quad_ok(S7, 2) and self.quad_ok(R6, 3) and self.quad_ok(R7, 3)):
                    continue
                self.stats["f1_pass"] += 1
                kstat["f1"] += 1
                b6 = self.base_parts(R6, dmask, P7)
                if not b6:
                    continue
                b7 = self.base_parts(R7, dmask, P6)
                if not b7:
                    continue
                self.stats["f2_pass"] += 1
                kstat["f2"] += 1
                q6 = self.colfilter(self.splits(S6, dmask, P7), S6, P7, dmask)
                if not q6:
                    continue
                q7 = self.colfilter(self.splits(S7, dmask, P6), S7, P6, dmask)
                if not q7:
                    continue
                rhs6 = 1 + 2 * pc(S6 & P7) - pc(S6 & dmask)
                rhs7 = 1 + 2 * pc(S7 & P6) - pc(S7 & dmask)
                for A6, B6, TA6, TB6, ell6 in q6:
                    for A7, B7, TA7, TB7, ell7 in q7:
                        self.time_check()
                        self.stats["quad_pairs"] += 1
                        kstat["pairs"] += 1
                        if pc(A6 & A7) > 1 or pc(A6 & B7) > 1 or pc(B6 & A7) > 1 or pc(B6 & B7) > 1:
                            continue
                        qk6 = self.qk(A6, B6, A7, B7, P7)
                        if pc(TA6 & TB6) + qk6 + ell6 > rhs6:
                            continue
                        qk7 = self.qk(A7, B7, A6, B6, P6)
                        if pc(TA7 & TB7) + qk7 + ell7 > rhs7:
                            continue
                        self.stats["q2p_pass"] += 1
                        t6 = [tr for tr in b6 if all(pc(x & A7) <= 1 and pc(x & B7) <= 1 for x in tr)]
                        if not t6:
                            continue
                        t7 = [tr for tr in b7 if all(pc(x & A6) <= 1 and pc(x & B6) <= 1 for x in tr)]
                        for tr6 in t6:
                            for tr7 in t7:
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
                                if self.link_ok([A6, B6, P6] + list(tr6) + [A7, B7, P7] + list(tr7), dmask):
                                    return "FEASIBLE", {"D": list(d), "P6": list(e1), "P7": list(e2),
                                                        "A6": bits(A6), "B6": bits(B6), "triples6": [bits(x) for x in tr6],
                                                        "A7": bits(A7), "B7": bits(B7), "triples7": [bits(x) for x in tr7]}
        return "EXHAUSTED_INFEASIBLE", None


def verify_witness(rows, w):
    """Independent re-check of a FEASIBLE witness (block sizes, coverage, T-disjointness, V1 pair cover, row
    identity); identical in content to v1's verifier."""
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
    cases = []
    for x in sys.argv[3:]:  # "B" uses the default per-case budget, "B:SECONDS" overrides it
        b, _, s = x.partition(":")
        cases.append((int(b), float(s) if s else per_case))
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
    F5 = json.loads(pinned(*FRONT5))
    open6 = {x["b_index"]: x for x in F5["ms06_undecided"]}
    results = []
    for b, case_budget in cases:
        remaining = BUDGET - 10 - (time.monotonic() - T0)
        if remaining <= 1:
            results.append({"b": b, "status": "NOT_RUN_BUDGET"})
            continue
        sk = D6["skeletons"][b]
        rows = rows_of(sk)
        c = Case(rows, time.monotonic() + min(case_budget, remaining))
        t1 = time.monotonic()
        try:
            status, wit = c.search()
        except OutOfTime:
            status, wit = "INCOMPLETE", None
        rec = {"b": b, "open_in_frontier_v5": b in open6, "s_tag": open6[b]["s_tag"] if b in open6 else None,
               "types": sk["types"], "empty": sk["empty"], "case_budget_seconds": case_budget, "status": status,
               "seconds": round(time.monotonic() - t1, 3),
               "stats": c.stats, "partition_cache_entries": len(c.part_cache), "witness": wit,
               "per_key_counts": c.per_key if status == "EXHAUSTED_INFEASIBLE" else None}
        if wit is not None:
            rec["witness_verified_independently"] = verify_witness(rows, wit)
        results.append(rec)
    res = {"schema": "PA19-96H-PROBE-MS06-GPS2Q2P-v2", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK6, "frontier_v5": FRONT5, "lemmas_note": ["notes/ms06-block-relaxation-lemmas-v2.md",
                                                                             "330a12a63200b6543031c0dabe88af2341a8ced6192875103e9ee824eb2dfe91"]},
           "per_case_seconds": per_case, "results": results,
           "scope": "planning only: FEASIBLE = relaxation satisfiable (no elimination); EXHAUSTED_INFEASIBLE = CANDIDATE "
                    "needing a second independent implementation, note review and a parent verdict; INCOMPLETE = no "
                    "information; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data),
          [(r["b"], r["status"], r.get("seconds")) for r in results], flush=True)


if __name__ == "__main__":
    main()
