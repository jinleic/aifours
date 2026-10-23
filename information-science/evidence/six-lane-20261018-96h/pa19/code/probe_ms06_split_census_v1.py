#!/usr/bin/env python3
"""PA19 96h lane probe 10 -- FROZEN SOURCE, NOT RUN: ms06 leave-pair / pair-block split census.

Planning experiment 1 of notes/ms06-structural-split-plan-v1.md (section 8). Running it needs a parent
decision. The author only compiled it in memory to check syntax and never executed it.

For each open ms06 case b (frontier-v1 ms06_undecided, 86 cases) it computes, with no solver, no checker
and no CNF file:
  1. rows in exactly the encode_skel_b.build_v2 member order (types as listed, then the 4-deg(v) private
     rows of each P0 column v = 0..5, then the empty rows); T(r) = P0-quad set, t(r) = |T(r)|; the class of
     r is T(r);
  2. all GPS-1 keys (E, D). E is two distinct row pairs (the pair blocks of the two P1 columns) and D is the
     leave pair. Conditions: P1, pairs T-disjoint; P2, every row has max(0,t+l-2) <= n2 <= min(2,(t+l)//2)
     with l = [r in D]; P3, D T-disjoint and not in E. Two independent enumerators (A: D first; B: E first)
     must give equal key sets;
  3. class-level signatures at three split levels: E (class pairs of the pair blocks), D (class pair of the
     leave pair) and ED (both). It computes their orbits under Aut(types), i.e. the P0 column permutations
     preserving the type multiset (as in extend_b), checks that the signature set is Aut-invariant, and
     cross-checks the canonical forms by union-find;
  4. cross-checks: |Aut| equals 'aut' in evidence/probes/ms06-dp-v1.json; the GPS-1 receipt witness of b is
     among the keys; the frontier skeleton fields equal the skeleton file;
  5. for ONE pilot case it regenerates the base CNF in process with build_v2(...), using the vendored encoder
     and the same call as the direct attempts. It compares the digest with the direct-attempt record, checks
     the U numbering U(i) = 913 + 49 i and its witness clauses against the clause list, and computes in memory
     the sub-case CNF digests for every Level-E and Level-D orbit representative. Only the JSON is written.
Pilot rule: among the open cases whose direct build_v2 attempt timed out (old rev-15 b68, b73, b77, b162;
v6 b74, b151), take the one with the fewest Level-E orbits (ties: the smaller b).
Admission: fresh statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate marker. Self budget 280 s; no
output if it is exceeded. The exclusive receipt with the PID is written before any work, and the output is
created exclusively under LANE/evidence/probes/.
Scope: planning counts and pins only; no coverage, no exclusion, no PA19 claim.
Usage: probe_ms06_split_census_v1.py OUT_JSON
"""
import hashlib
import importlib.util
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
FRONT = (LANE + "/evidence/probes/frontier-v1.json", "0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46")
DP = (LANE + "/evidence/probes/ms06-dp-v1.json", "8c2c44b28ac991f5cfb08b3011214817b971bf541d2088aa2b98c4ff48713ae7")
GPS1 = (OLD + "/cycle2/gps1-probe-20261018T140007.json", "67170e7b6934cf2e5594985922e8385f3c46f646714c862e3d6f94014fe52218")
M6C = (OLD + "/cycle2/m2-ms06-initial-v6-contract-20261018T075542.json",
       "dc343809b7597804dde1c71802edd142fe87472d5e20f6220c21e7f234fc2413")
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
PILOT_POOL = (68, 73, 77, 162, 74, 151)
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0
N, K, Q, C0, M, DC = 19, 8, 6, 6, 2, 2   # rows, columns, symbols, P0 columns, P1 columns, D = N - 1 - 2K
SIG1, SIG2, PAIR = 6, 7, 5               # build_v2: P1 columns 6, 7; label 5 is the count-2 label
U0, USTEP = N * K * Q + 1, 1 + K * Q     # U of the i-th pair of combinations(range(19), 2) = 913 + 49 i
PAIRS19 = list(itertools.combinations(range(N), 2))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS19)}
LEVELS = ("E", "D", "ED")


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def budget(stage):
    if time.monotonic() - T0 > BUDGET:
        raise SystemExit("REFUSED: self budget exhausted at %s; no output" % stage)


def pinned(path, h):
    with open(path, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED pin mismatch " + path)
    return raw


def bounds(t, l):
    return max(0, t + l - DC), min(M, (M - DC + t + l) // 2)


def rows_of(sk):
    types = [frozenset(t) for t in sk["types"]]
    if not all(len(t) >= 2 and t <= frozenset(range(C0)) for t in types):
        raise ValueError("bad type")
    deg = [sum(1 for t in types if v in t) for v in range(C0)]
    if any(d > 4 for d in deg):
        raise ValueError("quad degree > 4")
    rows = types + [frozenset([v]) for v in range(C0) for _ in range(4 - deg[v])] + [frozenset()] * sk["empty"]
    if len(rows) != N or any(len(rows[a] & rows[b]) > 1 for a, b in PAIRS19):
        raise ValueError("row count or two rows sharing two quads")
    return rows


def keys_a(rows):
    """D first: every T-disjoint leave pair d, then every E of two distinct T-disjoint pairs != d."""
    t = [len(r) for r in rows]
    out = set()
    for d in PAIRS19:
        if rows[d[0]] & rows[d[1]]:
            continue
        b = [bounds(t[r], 1 if r in d else 0) for r in range(N)]
        if any(lo > hi for lo, hi in b):
            continue
        need = [r for r in range(N) if b[r][0] >= 1]
        elig = [r for r in range(N) if b[r][1] >= 1]
        cand = [p for p in itertools.combinations(elig, 2) if not rows[p[0]] & rows[p[1]] and p != d]
        for e1, e2 in itertools.combinations(cand, 2):
            cnt = {}
            for r in e1 + e2:
                cnt[r] = cnt.get(r, 0) + 1
            if all(b[r][0] <= c <= b[r][1] for r, c in cnt.items()) and all(r in cnt for r in need):
                out.add((e1, e2, d))
    return out


def keys_b(rows):
    """E first (GPS-1 search order, exhaustive): rows whose n2 violates the l=0 bounds must be leave rows."""
    t = [len(r) for r in rows]
    b0 = [bounds(x, 0) for x in t]
    b1 = [bounds(x, 1) for x in t]
    pairs = [(a, c) for a, c in PAIRS19
             if not rows[a] & rows[c] and max(b0[a][1], b1[a][1]) >= 1 and max(b0[c][1], b1[c][1]) >= 1]
    disjoint = [p for p in PAIRS19 if not rows[p[0]] & rows[p[1]]]
    out = set()
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            e1, e2 = pairs[i], pairs[j]
            n2 = [0] * N
            for r in e1 + e2:
                n2[r] += 1
            forced = [r for r in range(N) if not b0[r][0] <= n2[r] <= b0[r][1]]
            if len(forced) > 2 or any(not b1[r][0] <= n2[r] <= b1[r][1] for r in forced):
                continue
            if len(forced) == 2:
                ds = [tuple(forced)] if not rows[forced[0]] & rows[forced[1]] else []
            elif len(forced) == 1:
                f = forced[0]
                ds = [tuple(sorted((f, y))) for y in range(N) if y != f and not rows[f] & rows[y]]
            else:
                ds = disjoint
            for d in ds:
                if d != e1 and d != e2 and all(b1[r][0] <= n2[r] <= b1[r][1] for r in d):
                    out.add((e1, e2, d))
    return out


def cls(rows, r):
    return tuple(sorted(rows[r]))


def sig(rows, key, level):
    e1, e2, d = key
    se = tuple(sorted(tuple(sorted((cls(rows, p[0]), cls(rows, p[1])))) for p in (e1, e2)))
    sd = tuple(sorted((cls(rows, d[0]), cls(rows, d[1]))))
    return {"E": se, "D": sd, "ED": (se, sd)}[level]


def mapc(alpha, c):
    return tuple(sorted(alpha[v] for v in c))


def map_sig(alpha, s, level):
    if level == "D":
        return tuple(sorted((mapc(alpha, s[0]), mapc(alpha, s[1]))))
    if level == "E":
        return tuple(sorted(tuple(sorted((mapc(alpha, a), mapc(alpha, b)))) for a, b in s))
    return (map_sig(alpha, s[0], "E"), map_sig(alpha, s[1], "D"))


def automorphisms(sk):
    types = [tuple(sorted(t)) for t in sk["types"]]
    tset = sorted(types)
    return [p for p in itertools.permutations(range(C0))
            if sorted(tuple(sorted(p[v] for v in t)) for t in types) == tset]


def orbits(sigs, auts, level):
    sset = set(sigs)
    canon = {s: min(map_sig(a, s, level) for a in auts) for s in sset}
    closed = all(map_sig(a, s, level) in sset for s in sset for a in auts)
    parent = {s: s for s in sset}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for s in sset:
        for a in auts:
            s2 = map_sig(a, s, level)
            if s2 in parent:
                ra, rb = find(s), find(s2)
                if ra != rb:
                    parent[ra] = rb
    groups = {}
    for s in sset:
        groups.setdefault(find(s), set()).add(canon[s])
    reps = sorted(set(canon.values()))
    consistent = closed and all(len(v) == 1 for v in groups.values()) and len(groups) == len(reps)
    return reps, consistent, closed


def var(r, c, s):
    return 1 + K * Q * r + Q * c + s


def uvar(x, y):
    return U0 + USTEP * PAIR_INDEX[(min(x, y), max(x, y))]


def class_rows(rows, c):
    return [r for r in range(N) if cls(rows, r) == c]


def extra_clauses(rows, level, s, nv):
    """Appended clauses Phi_s of notes/ms06-structural-split-plan-v1.md section 5; returns (clauses, added_vars)."""
    out, add = [], 0
    se = s if level == "E" else (s[0] if level == "ED" else None)
    sd = s if level == "D" else (s[1] if level == "ED" else None)
    if se is not None:
        (a1, a2), (b1, b2) = se
        if a1 == a2 or b1 == b2:
            raise ValueError("pair block inside one class")

        def one_of(c, col, guard):
            return guard + [var(r, col, PAIR) for r in class_rows(rows, c)]

        if (a1, a2) == (b1, b2):
            for col in (SIG1, SIG2):
                out += [one_of(a1, col, []), one_of(a2, col, [])]
        else:
            z = nv + 1
            add = 1
            out += [one_of(a1, SIG1, [-z]), one_of(a2, SIG1, [-z]), one_of(b1, SIG2, [-z]), one_of(b2, SIG2, [-z]),
                    one_of(b1, SIG1, [z]), one_of(b2, SIG1, [z]), one_of(a1, SIG2, [z]), one_of(a2, SIG2, [z])]
    if sd is not None:
        x1, x2 = sd
        lits = sorted({uvar(x, y) for x in class_rows(rows, x1) for y in class_rows(rows, x2) if x != y})
        if not lits:
            raise ValueError("empty leave clause")
        out.append(lits)
    return out, add


def direct_history(b, front, m6rows):
    """Pinned direct-attempt records of case b (old rev-15 via the v6 contract rows; v6 via the frontier)."""
    hist = []
    row = m6rows.get(b)
    if row is not None and row["original_status"] is not None:
        rec = json.loads(pinned(OLD + "/" + row["original_record"], row["original_sha256"]))
        hist.append({"route": "rev15 direct", "record": row["original_record"], "status": rec["status"],
                     "encoder": rec.get("encoder"), "solver": rec.get("solver_info", {}).get("version"),
                     "solve_seconds": rec.get("solve_seconds"), "solver_rc": rec.get("solver_rc"),
                     "cnf_sha256": rec["cnf_sha256"], "cnf_bytes": rec["cnf_bytes"]})
    v6 = front["ms06_v6_attempt_records"].get(str(b))
    if v6 is not None:
        rec = json.loads(pinned(OLD + "/" + v6["record"], v6["sha256"]))
        hist.append({"route": "v6 direct", "record": v6["record"], "status": rec["status"], "encoder": rec.get("encoder"),
                     "solver": rec.get("solver_name"),
                     "solver_status_lines": rec["native_result"]["solver_collector"]["status_lines"],
                     "native_limit_seconds": rec.get("native_limit_seconds"),
                     "cnf_sha256": rec["cnf_sha256"], "cnf_bytes": rec["cnf_bytes"]})
    return hist


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only planning census; children /bin/date only; no solver/checker; no CNF file"}
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
    front = json.loads(pinned(*FRONT))
    dp = {r["b_index"]: r for r in json.loads(pinned(*DP))["rows"]}
    gps = {c["index"]: c for c in json.loads(pinned(*GPS1))["results"]["ms06"]["cases"]}
    m6rows = {r["b_index"]: r for r in json.loads(pinned(*M6C))["rows"]}
    if not (D6["c0"] == C0 and D6["L"] == 1 and len(D6["profiles"]) == K
            and sorted(map(list, D6["profiles"])) == [[4, 3, 3, 3, 3, 3]] * C0 + [[4, 4, 3, 3, 3, 2]] * M):
        raise SystemExit("REFUSED: unexpected ms06 header")
    open06 = front["ms06_undecided"]
    if len(open06) != 86:
        raise SystemExit("REFUSED: frontier ms06 count != 86")
    cases, store = [], {}
    for x in open06:
        b = x["b_index"]
        sk = D6["skeletons"][b]
        rows = rows_of(sk)
        ka, kb = keys_a(rows), keys_b(rows)
        auts = automorphisms(sk)
        w = gps[b]["witness"]
        wkey = None
        if w is not None:
            e = sorted(tuple(sorted(p)) for p in w["pairs"])
            wkey = (e[0], e[1], tuple(sorted(w["leave"])))
        rec = {"b_index": b, "s_tag": x["s_tag"], "types": sk["types"], "empty": sk["empty"],
               "t_hist": {str(k): sum(1 for r in rows if len(r) == k) for k in range(5)},
               "classes": len({cls(rows, r) for r in range(N)}), "aut": len(auts), "raw_keys": len(ka),
               "keys_equal_AB": ka == kb, "keys_B": len(kb), "gps1_witness_in_keys": wkey in ka,
               "dp_aut_equal": dp[b]["aut"] == len(auts), "dp_raw_upper_bound": dp[b]["raw_upper_bound"],
               "frontier_fields_equal": x["skeleton_types"] == sk["types"] and x["skeleton_empty"] == sk["empty"],
               "direct_history": direct_history(b, front, m6rows), "signatures": {}, "orbits": {},
               "orbit_consistent": {}, "orbit_closed": {}}
        for lv in LEVELS:
            reps, consistent, closed = orbits([sig(rows, k, lv) for k in ka], auts, lv)
            rec["signatures"][lv] = len({sig(rows, k, lv) for k in ka})
            rec["orbits"][lv] = len(reps)
            rec["orbit_consistent"][lv] = consistent
            rec["orbit_closed"][lv] = closed
            store[(b, lv)] = reps
        cases.append(rec)
        budget("case %d" % b)
    tot = {"cases": len(cases), "raw_keys": sum(c["raw_keys"] for c in cases),
           "orbits": {lv: sum(c["orbits"][lv] for c in cases) for lv in LEVELS},
           "max_orbits": {lv: max(c["orbits"][lv] for c in cases) for lv in LEVELS},
           "dp_raw_upper_bound_sum": sum(c["dp_raw_upper_bound"] for c in cases)}
    checks = {"every_case_has_keys": all(c["raw_keys"] > 0 for c in cases),
              "keys_equal_AB": all(c["keys_equal_AB"] for c in cases),
              "gps1_witness_in_keys": all(c["gps1_witness_in_keys"] for c in cases),
              "dp_aut_equal": all(c["dp_aut_equal"] for c in cases),
              "frontier_fields_equal": all(c["frontier_fields_equal"] for c in cases),
              "orbits_consistent_and_closed": all(c["orbit_consistent"][lv] and c["orbit_closed"][lv]
                                                  for c in cases for lv in LEVELS)}
    # pilot case: binding of the base CNF and in-memory sub-case digests (Level E and Level D representatives)
    byb = {c["b_index"]: c for c in cases}
    pool = [b for b in PILOT_POOL if b in byb]
    pb = min(pool, key=lambda b: (byb[b]["orbits"]["E"], b))
    hist = byb[pb]["direct_history"]
    timed_out = [h for h in hist if h["status"] == "UNKNOWN" and h.get("solver_rc") != 20
                 and not h.get("solver_status_lines")]
    rec_cnf = (hist[-1]["cnf_sha256"], hist[-1]["cnf_bytes"]) if hist else None
    pinned(*ENC)
    spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
    E = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(E)
    sk = D6["skeletons"][pb]
    rows = rows_of(sk)
    special = [p for p in D6["profiles"] if list(p) != [4, 3, 3, 3, 3, 3]]
    nv, cl = E.build_v2(D6["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
    base = E.cnf_bytes(nv, cl)
    budget("pilot base")
    head = b"p cnf %d %d\n" % (nv, len(cl))
    header_ok = base.startswith(head)
    body = base[len(head):]
    long_cl = {tuple(c) for c in cl if len(c) == K * Q + 1}
    bin_cl = {tuple(c) for c in cl if len(c) == 2}
    u_ok = all(tuple(range(U0 + USTEP * i + 1, U0 + USTEP * i + USTEP)) + (U0 + USTEP * i,) in long_cl
               for i in range(len(PAIRS19)))
    w_ok = all((-(U0 + USTEP * i + 1 + Q * c + s), var(r, c, s)) in bin_cl
               and (-(U0 + USTEP * i + 1 + Q * c + s), var(r2, c, s)) in bin_cl
               for i, (r, r2) in enumerate(PAIRS19) for c in range(K) for s in range(Q))
    del long_cl, bin_cl

    def sub_bytes(extra, add):
        return (b"p cnf %d %d\n" % (nv + add, len(cl) + len(extra)) + body
                + "".join(" ".join(map(str, c)) + " 0\n" for c in extra).encode())

    first_extra, first_add = extra_clauses(rows, "E", store[(pb, "E")][0], nv)
    serial_ok = sub_bytes(first_extra, first_add) == E.cnf_bytes(nv + first_add, cl + first_extra)
    subcases = {}
    for lv in ("E", "D"):
        subcases[lv] = []
        for s in store[(pb, lv)]:
            extra, add = extra_clauses(rows, lv, s, nv)
            data = sub_bytes(extra, add)
            subcases[lv].append({"signature": s, "extra_clauses": extra, "added_vars": add,
                                 "header": data[:data.index(b"\n")].decode(), "bytes": len(data),
                                 "sha256": hashlib.sha256(data).hexdigest()})
            del data
            budget("pilot sub-cases")
    pilot = {"rule": "fewest Level-E orbits among open direct-timeout cases %r (ties: smaller b)" % (PILOT_POOL,),
             "b_index": pb, "s_tag": byb[pb]["s_tag"], "direct_history": hist,
             "direct_attempts_timed_out": len(timed_out) == len(hist) and bool(hist),
             "base": {"call": "encode_skel_b.build_v2(6, types, empty, [[4,4,3,3,3,2]]*2) then cnf_bytes",
                      "header": head.decode().strip(), "bytes": len(base), "sha256": hashlib.sha256(base).hexdigest(),
                      "record_cnf": rec_cnf,
                      "equals_record": rec_cnf == (hashlib.sha256(base).hexdigest(), len(base))},
             "header_ok": header_ok, "u_numbering_ok": u_ok, "witness_clauses_ok": w_ok,
             "serialization_self_check_ok": serial_ok,
             "subcases": subcases, "level_ED_orbits_not_pinned": len(store[(pb, "ED")])}
    checks["pilot_binding"] = (pilot["base"]["equals_record"] and header_ok and u_ok and w_ok and serial_ok
                               and pilot["direct_attempts_timed_out"])
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-MS06-SPLIT-CENSUS-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK6, "frontier": FRONT, "dp": DP, "gps1": GPS1, "m6_contract": M6C, "encoder": ENC},
           "cases": cases, "totals": tot, "checks": checks, "all_ok": all(checks.values()), "pilot": pilot,
           "scope": "planning counts and sub-case pins only; a signature count is not a coverage claim; no case is "
                    "closed or excluded by this probe; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    budget("before output")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", res["all_ok"], flush=True)


if __name__ == "__main__":
    main()
