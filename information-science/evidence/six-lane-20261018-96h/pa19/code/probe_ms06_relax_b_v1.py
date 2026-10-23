#!/usr/bin/env python3
"""PA19 96h lane probe 20 (structural, planning only): SECOND, INDEPENDENTLY WRITTEN implementation ("B") of the
ms06 block-level relaxation of notes/ms06-block-relaxation-lemmas-v2.md (330a12a6...). It shares no code with
probe_ms06_gps2q2p_v1/v2 ("A") and uses a different enumeration and different arithmetic. It exists to
cross-check any EXHAUSTED_INFEASIBLE result of A before such a candidate goes to review. No solver, checker
or CNF.

Model. Rows are derived from the skeleton entry: types, then 4-deg(v) rows {v} for v = 0..5, then the empty
rows. For each P1 column j in {6, 7}, every row gets a block type e_j(r) in {+1 quad, 0 triple, -1 pair}.
Enumeration:
  outer   the leave pair D = {x, y}: every pair with T(x) ∩ T(y) = ∅;
  middle  e_6(r) row by row, with e_7(r) = 2 - t(r) - l(r) - e_6(r) required in {-1, 0, 1} (row identity).
          Running counts are capped at 8 quad rows, 9 triple rows and 2 pair rows per column. Running per-P0-quad
          counts are capped at 2 (quad rows), 3 (triple rows) and 1 (pair rows) per column, since blocks are
          T-disjoint. The two pair rows of each column must be T-disjoint and differ from D.
          Column symmetry: P6 < P7 lexicographically. Exchanging columns 6 and 7 maps the condition set onto
          itself, so this loses nothing;
  inner   quad splits (two T-disjoint 4-sets, no D or other-column pair inside), triple partitions (three
          T-disjoint 3-sets, no D or other-column pair inside), cross-column |X ∩ Y| <= 1 for every pair of
          blocks, then the counting lemmas (direct form) and LINK.
Counting lemmas, computed directly from the definitions (not from A's closed forms). For column j with quads
A, B and other column k:
  x2  = 16 - #{cross pairs (a in A, b in B) sharing a P0 quad} - #{cross pairs inside a column-k quad or equal
        to the column-k pair} - [D is a cross pair];
  tau = sum over r in A ∪ B of (6 - t(r)) + [r is a column-k triple row];
  Q2P: tau - x2 <= 33;
  QPL: sum over P0 columns c of (3 - |A ∩ Q_c| - |B ∩ Q_c|) + #{column-k triples meeting A and B} <= x2.
LINK: G_res = pairs other than D sharing no P0 quad and no P1 block. Every row r needs exactly 2(6 - t(r))
G_res-neighbours, and some perfect matching of them into G_res-edges {s, w} must admit a system of distinct
representatives: P0 columns c not in T(r) ∪ T(s) ∪ T(w). This is checked by enumerating the matchings, then
bipartite augmenting paths.
Status per case: FEASIBLE (witness), EXHAUSTED_INFEASIBLE, or INCOMPLETE (budget). Self budget 280 s;
per-case budgets as in A (B or B:SECONDS). Standard library only. The only child process is /bin/date. The
receipt with the PID is written before any work.
Usage: probe_ms06_relax_b_v1.py OUT_JSON PER_CASE_SECONDS B[:SECONDS] [B[:SECONDS] ...]
"""
import hashlib
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
SKEL = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
FRONTIER = (RUN + "/review/pa19-parent-frontier-v5.json", "be79dede711b315bd400511d583e20d12fd453c4f4eada8f65d8aa8c2448ed9c")
NR = 19
CAP = {1: 8, 0: 9, -1: 2}
QCAP = {1: 2, 0: 3, -1: 1}
MIN_FREE = 12_200_000_000 + 16 * 1024 * 1024
SELF_BUDGET = 280.0


class Budget(Exception):
    pass


def host_clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def read_pinned(path, digest):
    with open(path, "rb") as fh:
        data = fh.read()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SystemExit("REFUSED pin mismatch " + path)
    return data


def members(mask):
    out = []
    i = 0
    while mask:
        if mask & 1:
            out.append(i)
        mask >>= 1
        i += 1
    return out


def popcount(mask):
    return bin(mask).count("1")


def derive_rows(entry):
    sets = [frozenset(ty) for ty in entry["types"]]
    degree = [0] * 6
    for ty in entry["types"]:
        for v in ty:
            degree[v] += 1
    for v in range(6):
        sets.extend([frozenset([v])] * (4 - degree[v]))
    sets.extend([frozenset()] * entry["empty"])
    if len(sets) != NR or max(degree) > 4:
        raise ValueError("skeleton does not give 19 rows")
    return sets


class RelaxB:
    def __init__(self, sets, deadline):
        self.sets = sets
        self.tsize = [len(s) for s in sets]
        self.tmask = [sum(1 << c for c in s) for s in sets]
        self.clash = []
        for r in range(NR):
            m = 0
            for s in range(NR):
                if s != r and self.tmask[r] & self.tmask[s]:
                    m |= 1 << s
            self.clash.append(m)
        self.quad_rows = [sum(1 << r for r in range(NR) if c in sets[r]) for c in range(6)]
        self.deadline = deadline
        self.counter = {"leaves": 0, "leaf_blocks_ok": 0, "quad_pairs": 0, "q2p_ok": 0, "triple_pairs": 0,
                        "qpl_ok": 0, "link_calls": 0, "D_tried": 0}
        self.ticks = 0
        self.qcache = {}
        self.tcache = {}

    def tick(self):
        self.ticks += 1
        if self.ticks % 512 == 0 and time.monotonic() > self.deadline:
            raise Budget()

    def independent(self, mask):
        for r in members(mask):
            if self.clash[r] & mask:
                return False
        return True

    def quad_splits(self, S, dpair, other_pair):
        key = (S, dpair, other_pair)
        if key in self.qcache:
            return self.qcache[key]
        rows = members(S)
        first, rest = rows[0], rows[1:]
        out = []
        n = len(rest)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    A = (1 << first) | (1 << rest[i]) | (1 << rest[j]) | (1 << rest[k])
                    B = S & ~A
                    good = True
                    for X in (A, B):
                        if (X & dpair) == dpair or (X & other_pair) == other_pair or not self.independent(X):
                            good = False
                            break
                    if good:
                        out.append((A, B))
        self.qcache[key] = out
        return out

    def triple_parts(self, R, dpair, other_pair):
        key = (R, dpair, other_pair)
        if key in self.tcache:
            return self.tcache[key]
        out = []

        def go(rem, chosen):
            if rem == 0:
                out.append(tuple(chosen))
                return
            rows = members(rem)
            a = rows[0]
            for i in range(1, len(rows)):
                for j in range(i + 1, len(rows)):
                    X = (1 << a) | (1 << rows[i]) | (1 << rows[j])
                    if (X & dpair) == dpair or (X & other_pair) == other_pair or not self.independent(X):
                        continue
                    go(rem & ~X, chosen + [X])
        go(R, [])
        self.tcache[key] = out
        return out

    def x2_and_tau(self, A, B, Ak, Bk, Pk, Rk, dpair):
        x2 = 16
        for a in members(A):
            for b in members(B):
                pair = (1 << a) | (1 << b)
                if self.tmask[a] & self.tmask[b]:
                    x2 -= 1
                elif (Ak & pair) == pair or (Bk & pair) == pair or Pk == pair:
                    x2 -= 1
                elif pair == dpair:
                    x2 -= 1
        tau = 0
        for r in members(A | B):
            tau += (6 - self.tsize[r]) + (1 if (Rk >> r) & 1 else 0)
        return x2, tau

    def qpl_lhs(self, A, B, triples_k):
        s = 0
        for c in range(6):
            s += 3 - popcount(A & self.quad_rows[c]) - popcount(B & self.quad_rows[c])
        s += sum(1 for X in triples_k if (X & A) and (X & B))
        return s

    def link(self, blocks, dpair):
        nbr = []
        for r in range(NR):
            m = ((1 << NR) - 1) & ~(1 << r)
            if (dpair >> r) & 1:
                m &= ~dpair
            for c in range(6):
                if (self.quad_rows[c] >> r) & 1:
                    m &= ~self.quad_rows[c]
            for X in blocks:
                if (X >> r) & 1:
                    m &= ~X
            nbr.append(m)
        for r in range(NR):
            if popcount(nbr[r]) != 2 * (6 - self.tsize[r]):
                return False
        for r in range(NR):
            free_cols = [c for c in range(6) if not (self.tmask[r] >> c) & 1]
            if not self.row_link(nbr, r, free_cols):
                return False
        return True

    def row_link(self, nbr, r, free_cols):
        target = nbr[r]
        found = [False]

        def sdr(pairs):
            owner = {}

            def augment(i, seen):
                s, w = pairs[i]
                bad = self.tmask[s] | self.tmask[w]
                for c in free_cols:
                    if (bad >> c) & 1 or c in seen:
                        continue
                    seen.add(c)
                    if c not in owner or augment(owner[c], seen):
                        owner[c] = i
                        return True
                return False
            for i in range(len(pairs)):
                if not augment(i, set()):
                    return False
            return True

        def matchings(rem, pairs):
            if found[0]:
                return
            if rem == 0:
                if sdr(pairs):
                    found[0] = True
                return
            rows = members(rem)
            s = rows[0]
            for w in rows[1:]:
                if (nbr[s] >> w) & 1:
                    matchings(rem & ~((1 << s) | (1 << w)), pairs + [(s, w)])
                    if found[0]:
                        return
        matchings(target, [])
        return found[0]

    def solve(self):
        for x in range(NR):
            for y in range(x + 1, NR):
                if self.tmask[x] & self.tmask[y]:
                    continue
                self.counter["D_tried"] += 1
                w = self.with_leave(x, y)
                if w is not None:
                    return "FEASIBLE", w
        return "EXHAUSTED_INFEASIBLE", None

    def with_leave(self, x, y):
        dpair = (1 << x) | (1 << y)
        lv = [1 if r in (x, y) else 0 for r in range(NR)]
        options = []
        for r in range(NR):
            opts = []
            for e6 in (1, 0, -1):
                e7 = 2 - self.tsize[r] - lv[r] - e6
                if -1 <= e7 <= 1:
                    opts.append((e6, e7))
            if not opts:
                return None
            options.append(opts)
        typ6 = [0] * NR
        typ7 = [0] * NR
        cnt = {6: {1: 0, 0: 0, -1: 0}, 7: {1: 0, 0: 0, -1: 0}}
        qcnt = {6: {e: [0] * 6 for e in (1, 0, -1)}, 7: {e: [0] * 6 for e in (1, 0, -1)}}
        pair_rows = {6: [], 7: []}
        result = [None]

        def place(r):
            if result[0] is not None:
                return
            self.tick()
            if r == NR:
                self.counter["leaves"] += 1
                w = self.leaf(typ6, typ7, dpair)
                if w is not None:
                    result[0] = w
                return
            cols_r = members(self.tmask[r])
            for e6, e7 in options[r]:
                if cnt[6][e6] >= CAP[e6] or cnt[7][e7] >= CAP[e7]:
                    continue
                if any(qcnt[6][e6][c] >= QCAP[e6] for c in cols_r) or any(qcnt[7][e7][c] >= QCAP[e7] for c in cols_r):
                    continue
                ok = True
                for col, e in ((6, e6), (7, e7)):
                    if e == -1 and pair_rows[col]:
                        s = pair_rows[col][0]
                        if self.tmask[s] & self.tmask[r] or ((1 << s) | (1 << r)) == dpair:
                            ok = False
                if not ok:
                    continue
                typ6[r], typ7[r] = e6, e7
                cnt[6][e6] += 1
                cnt[7][e7] += 1
                for c in cols_r:
                    qcnt[6][e6][c] += 1
                    qcnt[7][e7][c] += 1
                if e6 == -1:
                    pair_rows[6].append(r)
                if e7 == -1:
                    pair_rows[7].append(r)
                place(r + 1)
                if e6 == -1:
                    pair_rows[6].pop()
                if e7 == -1:
                    pair_rows[7].pop()
                for c in cols_r:
                    qcnt[6][e6][c] -= 1
                    qcnt[7][e7][c] -= 1
                cnt[6][e6] -= 1
                cnt[7][e7] -= 1
                if result[0] is not None:
                    return
        place(0)
        return result[0]

    def leaf(self, typ6, typ7, dpair):
        S6 = sum(1 << r for r in range(NR) if typ6[r] == 1)
        R6 = sum(1 << r for r in range(NR) if typ6[r] == 0)
        P6 = sum(1 << r for r in range(NR) if typ6[r] == -1)
        S7 = sum(1 << r for r in range(NR) if typ7[r] == 1)
        R7 = sum(1 << r for r in range(NR) if typ7[r] == 0)
        P7 = sum(1 << r for r in range(NR) if typ7[r] == -1)
        if popcount(S6) != 8 or popcount(R6) != 9 or popcount(P6) != 2:
            return None
        if popcount(S7) != 8 or popcount(R7) != 9 or popcount(P7) != 2:
            return None
        if P6 == P7 or tuple(members(P6)) > tuple(members(P7)):
            return None
        q6 = self.quad_splits(S6, dpair, P7)
        if not q6:
            return None
        q7 = self.quad_splits(S7, dpair, P6)
        if not q7:
            return None
        t6 = self.triple_parts(R6, dpair, P7)
        if not t6:
            return None
        t7 = self.triple_parts(R7, dpair, P6)
        if not t7:
            return None
        self.counter["leaf_blocks_ok"] += 1
        for A6, B6 in q6:
            for A7, B7 in q7:
                self.tick()
                self.counter["quad_pairs"] += 1
                if max(popcount(A6 & A7), popcount(A6 & B7), popcount(B6 & A7), popcount(B6 & B7)) > 1:
                    continue
                x2_6, tau6 = self.x2_and_tau(A6, B6, A7, B7, P7, R7, dpair)
                if tau6 - x2_6 > 33:
                    continue
                x2_7, tau7 = self.x2_and_tau(A7, B7, A6, B6, P6, R6, dpair)
                if tau7 - x2_7 > 33:
                    continue
                self.counter["q2p_ok"] += 1
                for tr6 in t6:
                    if any(popcount(X & A7) > 1 or popcount(X & B7) > 1 for X in tr6):
                        continue
                    for tr7 in t7:
                        self.tick()
                        if any(popcount(X & A6) > 1 or popcount(X & B6) > 1 for X in tr7):
                            continue
                        self.counter["triple_pairs"] += 1
                        if any(popcount(X & Y) > 1 for X in tr6 for Y in tr7):
                            continue
                        if self.qpl_lhs(A6, B6, tr7) > x2_6 or self.qpl_lhs(A7, B7, tr6) > x2_7:
                            continue
                        self.counter["qpl_ok"] += 1
                        self.counter["link_calls"] += 1
                        blocks = [A6, B6, P6] + list(tr6) + [A7, B7, P7] + list(tr7)
                        if self.link(blocks, dpair):
                            return {"D": members(dpair), "P6": members(P6), "P7": members(P7),
                                    "A6": members(A6), "B6": members(B6), "triples6": [members(X) for X in tr6],
                                    "A7": members(A7), "B7": members(B7), "triples7": [members(X) for X in tr7]}
        return None


def main():
    out_path = os.path.abspath(sys.argv[1])
    default_budget = float(sys.argv[2])
    work = []
    for arg in sys.argv[3:]:
        b, _, secs = arg.partition(":")
        work.append((int(b), float(secs) if secs else default_budget))
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")) or not work:
        raise SystemExit("REFUSED: bad arguments")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as fh:
        own_sha = hashlib.sha256(fh.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": own_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": host_clock(), "self_budget_seconds": SELF_BUDGET, "output": out_path,
               "scope": "structural planning probe (implementation B); children /bin/date only; no solver/checker/CNF"}
    with open(receipt_path, "xb") as fh:
        fh.write(json.dumps(receipt, indent=1, sort_keys=True).encode())
    print("RECEIPT", receipt_path, receipt["pid"], flush=True)
    vfs = os.statvfs(LANE)
    free_start = vfs.f_bavail * vfs.f_frsize
    markers = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
               if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free_start < MIN_FREE or markers:
        raise SystemExit(f"REFUSED free={free_start} markers={markers}")
    started = host_clock()
    skel = json.loads(read_pinned(*SKEL))
    front = json.loads(read_pinned(*FRONTIER))
    open_cases = {e["b_index"]: e["s_tag"] for e in front["ms06_undecided"]}
    results = []
    for b, secs in work:
        left = SELF_BUDGET - 10 - (time.monotonic() - T0)
        if left <= 1:
            results.append({"b": b, "status": "NOT_RUN_BUDGET"})
            continue
        entry = skel["skeletons"][b]
        solver = RelaxB(derive_rows(entry), time.monotonic() + min(secs, left))
        t1 = time.monotonic()
        try:
            status, witness = solver.solve()
        except Budget:
            status, witness = "INCOMPLETE", None
        results.append({"b": b, "s_tag": open_cases.get(b), "open_in_frontier_v5": b in open_cases,
                        "case_budget_seconds": secs, "status": status, "seconds": round(time.monotonic() - t1, 3),
                        "counters": solver.counter, "witness": witness})
    res = {"schema": "PA19-96H-PROBE-MS06-RELAX-B-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": host_clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": own_sha,
           "admission": {"free_start": free_start, "floor": MIN_FREE, "markers": markers},
           "pins": {"skeletons": SKEL, "frontier_v5": FRONTIER}, "results": results,
           "scope": "planning only; second implementation for cross-checking implementation A; no closure, no "
                    "PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as fh:
        fh.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data),
          [(r["b"], r["status"], r.get("seconds")) for r in results], flush=True)


if __name__ == "__main__":
    main()
