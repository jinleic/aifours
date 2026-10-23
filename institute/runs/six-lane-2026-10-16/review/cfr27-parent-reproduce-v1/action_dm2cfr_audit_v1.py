#!/usr/bin/env python3
"""Independent stdlib group-action / orbit-expansion audit and definition-first DM -> CFR derivation for the two
pinned CFR(5,27) candidates (owner Cfr27ParentReproduce, v1).

Usage: python3 -B action_dm2cfr_audit_v1.py          (writes audit-v1/ exclusively; imports no lane code)

Definitions used (all arithmetic in the CYCLIC group Z_27, integers mod 27; never GF(27)):
  DM(6,27;1) over Z_27: 6 x 27 array; for every pair of rows the 27 entrywise differences mod 27 are all residues once.
  CFR(5,27): 5 permutations of 0..26; for every ordered distinct symbols (a,b) and nonzero d mod 27 at most one row
             has pos(b) - pos(a) = d (mod 27).
  Group action (from the freeze record): element (mu, pi) with pi[i] = image of row i acts on a column c by
             (g c)_x = mu * c_{pi^-1(x)} mod 27, then the column is normalised by subtracting its first entry.
             Implemented as the monomial matrix M[x][y] = mu if y == pi^-1(x), composition = matrix product mod 27.
  DM -> CFR: b_j[c] = (D_j[c] - D_0[c]) mod 27; label x = b_1[c]; CFR row (j-1) has symbol x at position b_j[c].
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
ROOT = REVIEW.parents[3]
PARENT_INPUTS = REVIEW / "cfr27-parent-inputs-v1"
PIN = HERE / "inputs"
OUT = HERE / "audit-v1"
N, K = 27, 6
FREE_FLOOR = 12_000_000_000

FREEZE_SHA = "c24cb110443749d14e2d0746d48d54179baaab12628bd7fb807aebb5db6a73f5"
PARENT_PINS = {
    "A-DM.raw": "b8eec25f6d575aecfce12933a067b582774dd1be8738604797d5c76169c6c65c",
    "A-CFR.raw": "6ceed793b3cd733461b8bec06091c282e300b1f1feeef9c95cf6d1c679588c7a",
    "B-DM.raw": "3f45f8c33d4f2379a154dd4d6bb21da6ef40beb50b7548d56ee3bf799357b664",
    "B-CFR.raw": "a9faf3dd0d2c2bbff53499d869ed00eeeb7b876abbb75c294680b10969b35f0a",
}
MODEL_SHA = {"T10": "b9233e7ed7a1833c4f377ebad0419ed0a77368198cd0f826a1e6babb27582abc",
             "S3a": "6540d72cb28d245a37702694cc89a53da86a3dbfc51056e01e9d374694962e7a"}
SPEC_SHA = {"T10": "1378292cf8a156e7c14cc114cd91bb4feac5364aa791eb7b4dd5042c7aae2178",
            "S3a": "808e3dfff2dbf199b36b8881e61150221c57291c131dcb223fb3b1759605b622"}
# name, parent letter, model tag, zero column included, expected sorted orbit sizes (incl. zero column)
CANDS = [("T10-zero-first", "A", "T10", True, [1, 2, 6, 6, 6, 6]),
         ("S3a-nozero-first", "B", "S3a", False, [3, 6, 6, 6, 6])]


def now():
    return datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d %H:%M:%S %Z")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def require(ok, why):
    if not ok:
        raise RuntimeError(why)


def rel(p):
    return str(Path(p).relative_to(ROOT))


def write_x(path, data):
    with open(path, "xb") as fh:
        fh.write(data)


# ------------------------------------------------------------------ raw parsing (canonical cfr-raw / dm-raw text)
def parse_matrix(data, rows):
    require(b"\r" not in data and data.endswith(b"\n"), "line endings")
    lines = data[:-1].split(b"\n")
    require(len(lines) == rows, "row count %d" % len(lines))
    M = []
    for ln in lines:
        toks = ln.split(b" ")
        require(len(toks) == N, "token count")
        row = []
        for t in toks:
            require(t.isdigit() and (t == b"0" or not t.startswith(b"0")), "token %r" % t)
            v = int(t)
            require(0 <= v < N, "range")
            row.append(v)
        M.append(row)
    return M


def ser(M):
    return "".join(" ".join(str(x) for x in r) + "\n" for r in M).encode("ascii")


def columns(D):
    return [tuple(D[x][c] for x in range(len(D))) for c in range(N)]


# ------------------------------------------------------------------ group arithmetic
def sub_cyclic(a, b):
    return (a - b) % N


def digits3(a):
    return (a % 3, (a // 3) % 3, a // 9)


def sub_z3cubed(a, b):  # elementary-abelian (additive group of GF(27)) control arithmetic on base-3 digits
    return tuple((x - y) % 3 for x, y in zip(digits3(a), digits3(b)))


def dm_bad_pairs(D, sub):
    bad = []
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            vals = [sub(D[i][c], D[j][c]) for c in range(N)]
            if len(set(vals)) != N:
                bad.append([i, j, N - len(set(vals))])
    return bad


def inv(p):
    q = [None] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    require(None not in q, "not a permutation")
    return tuple(q)


def mat(mu, pi, convention="freeze"):
    """freeze: (g c)_x = mu * c_{pi^-1(x)};  swapped (control only): (g c)_x = mu * c_{pi(x)}."""
    src = inv(pi) if convention == "freeze" else tuple(pi)
    return tuple(tuple((mu % N) if y == src[x] else 0 for y in range(K)) for x in range(K))


def mul(A, B):
    return tuple(tuple(sum(A[x][y] * B[y][z] for y in range(K)) % N for z in range(K)) for x in range(K))


IDENT = mat(1, tuple(range(K)))


def closure(gens):
    S, frontier = {IDENT}, [IDENT]
    while frontier:
        nxt = []
        for X in frontier:
            for G in gens:
                Y = mul(G, X)
                if Y not in S:
                    S.add(Y)
                    nxt.append(Y)
        frontier = nxt
    return S


def decode(M):
    """monomial matrix -> (mu, pi) with pi[i] = image of row i (so M[x][pi^-1(x)] = mu)."""
    src, mus = [], set()
    for x in range(K):
        nz = [(y, v) for y, v in enumerate(M[x]) if v]
        require(len(nz) == 1, "not monomial")
        src.append(nz[0][0])
        mus.add(nz[0][1])
    require(len(mus) == 1, "not scalar-monomial")
    return mus.pop(), inv(tuple(src))


def order(M):
    m, X = 1, M
    while X != IDENT:
        X, m = mul(M, X), m + 1
    return m


def normalize(v):
    return tuple((x - v[0]) % N for x in v)


def act(M, c):
    return normalize([sum(M[x][y] * c[y] for y in range(K)) % N for x in range(K)])


def orbit(G, b):
    return frozenset(act(M, b) for M in G)


def invariance(M, cols):
    img = [act(M, c) for c in cols]
    cc = Counter(cols)
    return {"invariant": Counter(img) == cc, "images_outside_column_set": sum(1 for v in img if v not in cc)}


def pair_orbits(G):
    perms = [decode(M)[1] for M in G]
    seen, orbs = set(), []
    for i in range(K):
        for j in range(i + 1, K):
            if (i, j) in seen:
                continue
            o = set()
            for pi in perms:
                a, b = pi[i], pi[j]
                o.add((min(a, b), max(a, b)))
            seen |= o
            orbs.append(sorted(o))
    return orbs


# ------------------------------------------------------------------ DM <-> CFR
def dm_to_cfr(D):
    b = [[(D[j][c] - D[0][c]) % N for c in range(N)] for j in range(K)]
    rows = []
    for j in range(1, K):
        row = [None] * N
        for c in range(N):
            p, x = b[j][c], b[1][c]
            if row[p] is not None:
                return None, "b_%d is not a bijection columns -> positions" % j
            row[p] = x
        if sorted(row) != list(range(N)):
            return None, "labels b_1 are not a bijection"
        rows.append(row)
    return rows, None


def cfr_violations(R, sub):
    for row in R:
        require(sorted(row) == list(range(N)), "row not a permutation")
    pos = [[None] * N for _ in R]
    for r, row in enumerate(R):
        for p, s in enumerate(row):
            pos[r][s] = p
    seen, viol = {}, 0
    for r in range(len(R)):
        for a in range(N):
            for b in range(N):
                if a != b:
                    key = (a, b, sub(pos[r][b], pos[r][a]))
                    if key in seen:
                        viol += 1
                    else:
                        seen[key] = r
    return viol, len(seen)


def cfr_to_dm(R):
    pos = []
    for row in R:
        p = [None] * N
        for i, s in enumerate(row):
            p[s] = i
        pos.append(p)
    return [[0] * N] + pos  # columns indexed by symbol s: (0, pos_R0(s), ..., pos_R4(s))


def parse_model(text):
    lines = text.split("\n")
    require(lines[0] == "DMORBIT-MODEL v1" and lines[1] == "%d %d" % (N, K), "model header")
    m = re.fullmatch(r"G (\d+)", lines[2])
    ng = int(m.group(1))
    group = set()
    for ln in lines[3:3 + ng]:
        v = [int(t) for t in ln.split()]
        group.add((v[0], tuple(v[1:])))
    m = re.fullmatch(r"REPPAIRS (\d+)", lines[3 + ng])
    nr = int(m.group(1))
    reps = [tuple(int(t) for t in ln.split()) for ln in lines[4 + ng:4 + ng + nr]]
    spec_line = [ln for ln in lines if ln.startswith("SPEC_SHA256 ")]
    return ng, group, reps, spec_line[0].split()[1] if spec_line else None


# ------------------------------------------------------------------ main
def main():
    require(sys.dont_write_bytecode, "run with python3 -B")
    st = os.statvfs(HERE)
    require(st.f_bavail * st.f_frsize >= FREE_FLOOR, "free floor")
    os.mkdir(OUT)
    res = {"script": rel(__file__), "script_sha256": sha(Path(__file__).read_bytes()), "host_time_start": now(),
           "imports": "stdlib only (hashlib json os re sys collections datetime pathlib zoneinfo); no lane code",
           "arithmetic": "cyclic Z_27 (integers mod 27) everywhere except the explicitly labelled Z_3^3 controls",
           "inputs": {}, "candidates": {}, "controls": []}
    fz_bytes = (PIN / "freeze-v1.json").read_bytes()
    require(sha(fz_bytes) == FREEZE_SHA, "freeze hash")
    res["inputs"]["freeze"] = {"path": rel(PIN / "freeze-v1.json"), "sha256": FREEZE_SHA}
    fz = json.loads(fz_bytes)
    raw = {}
    for name, want in PARENT_PINS.items():
        b = (PARENT_INPUTS / name).read_bytes()
        require(sha(b) == want, "parent pin " + name)
        raw[name] = b
        res["inputs"][name] = {"path": rel(PARENT_INPUTS / name), "sha256": want, "bytes": len(b)}
    for tag in ("T10", "S3a"):
        for kind, table in (("model", MODEL_SHA), ("spec.json", SPEC_SHA)):
            p = PIN / "specs" / ("%s.%s" % (tag, kind))
            require(sha(p.read_bytes()) == table[tag], "pinned %s %s" % (tag, kind))
            res["inputs"]["%s.%s" % (tag, kind)] = {"path": rel(p), "sha256": table[tag]}

    action_ok, dm2cfr_ok = True, True
    fzc = dict((c["name"], c) for c in fz["candidates"])
    for name, letter, tag, zero_mode, want_sizes in CANDS:
        out = {}
        D = parse_matrix(raw[letter + "-DM.raw"], K)
        R_pin = parse_matrix(raw[letter + "-CFR.raw"], K - 1)
        out["canonical_text_roundtrip"] = {"DM": ser(D) == raw[letter + "-DM.raw"],
                                           "CFR": ser(R_pin) == raw[letter + "-CFR.raw"]}
        cols = columns(D)
        out["dm_row0_all_zero_columns_normalised"] = all(c[0] == 0 for c in cols)
        out["dm_distinct_columns"] = len(set(cols)) == N
        # ---- direct definition checks of the raw DM (cyclic) and the Z_3^3 control
        bad = dm_bad_pairs(D, sub_cyclic)
        out["dm_check_Z27"] = {"row_pairs_checked": K * (K - 1) // 2, "bad_pairs": bad, "pass": not bad}
        bad3 = dm_bad_pairs(D, sub_z3cubed)
        out["dm_check_Z3cubed_control"] = {"bad_pairs": len(bad3), "pairs_failing": [p[:2] for p in bad3],
                                           "is_Z3cubed_DM": not bad3}
        # ---- group from the freeze generators
        gens_raw = fzc[name]["group"]
        gens = [mat(mu, tuple(pi)) for mu, pi in gens_raw]
        G = closure(gens)
        ords = Counter(order(M) for M in G)
        abelian = all(mul(A, B) == mul(B, A) for A in G for B in G)
        probes = [tuple(1 if y == t else 0 for y in range(K)) for t in range(1, K)] + [(0, 1, 3, 7, 12, 20)]
        faithful = len({tuple(act(M, p) for p in probes) for M in G}) == len(G)
        elements = sorted(decode(M) for M in G)
        out["group"] = {"generators_from_freeze": gens_raw, "order": len(G),
                        "element_orders": dict(sorted(ords.items())), "abelian": abelian,
                        "cyclic": any(o == len(G) for o in ords),
                        "faithful_on_normalised_columns": faithful,
                        "elements_mu_pi": [[mu, list(pi)] for mu, pi in elements],
                        "structure": ("cyclic C6" if any(o == len(G) for o in ords) and len(G) == 6 else
                                      "non-abelian order 6 (S3)" if len(G) == 6 and not abelian else "other")}
        # ---- the producer's model lists (mu, pi^-1) for the whole group; compare as sets
        mtext = (PIN / "specs" / (tag + ".model")).read_text()
        ng, mgroup, reps, spec_sha = parse_model(mtext)
        mine = {(mu, inv(pi)) for mu, pi in elements}
        porbs = pair_orbits(G)
        rep_ok = (len(reps) == len(porbs) and all(sum(1 for r in reps if tuple(r) in o) == 1 for o in porbs))
        out["model_crosscheck"] = {"model_group_order": ng, "model_group_equals_freeze_group_as_mu_piinv": mgroup == mine,
                                   "row_pair_orbits": porbs, "model_reppairs": [list(r) for r in reps],
                                   "one_reppair_per_row_pair_orbit": rep_ok, "model_spec_sha256_line": spec_sha,
                                   "spec_line_matches_pinned_spec": spec_sha == SPEC_SHA[tag]}
        # ---- orbit expansion of the printed base columns (freeze JSON) + zero column
        bases = [tuple(b) for b in fz["expander"]["independent_python_reexpansion"][name]["bases"]]
        orbs, sizes = [], []
        for b in bases:
            require(len(b) == K and b[0] == 0, "base not normalised")
            o = orbit(G, b)
            stab = sum(1 for M in G if act(M, b) == b)
            orbs.append(o)
            sizes.append({"base": list(b), "orbit_size": len(o), "stabiliser_order": stab,
                          "orbit_stabiliser_ok": len(o) * stab == len(G)})
        expanded = []
        zero = tuple([0] * K)
        if zero_mode:
            expanded.append(zero)
            sizes.insert(0, {"base": list(zero), "orbit_size": len(orbit(G, zero)),
                             "stabiliser_order": sum(1 for M in G if act(M, zero) == zero), "zero_column": True})
        for o in orbs:
            expanded.extend(sorted(o))
        got_sizes = sorted(s["orbit_size"] for s in sizes)
        fixed_cols = [list(c) for c in cols if len(orbit(G, c)) == 1]
        out["orbit_expansion"] = {
            "bases_from_freeze": [list(b) for b in bases], "orbits": sizes, "sorted_orbit_sizes": got_sizes,
            "expected_sorted_orbit_sizes": want_sizes, "orbit_sizes_as_expected": got_sizes == want_sizes,
            "expanded_columns": len(expanded), "expanded_distinct": len(set(expanded)) == len(expanded),
            "expanded_multiset_equals_DM_columns": Counter(expanded) == Counter(cols),
            "zero_column_mode": "zero column included" if zero_mode else "no zero column",
            "DM_columns_fixed_by_all_of_G": fixed_cols,
            "expanded_columns_sorted": [list(c) for c in sorted(expanded)]}
        # ---- invariance under every freeze generator and every group element
        gen_inv = [dict(generator=g, **invariance(M, cols)) for g, M in zip(gens_raw, gens)]
        all_inv = all(invariance(M, cols)["invariant"] for M in G)
        out["invariance"] = {"per_generator": gen_inv, "all_group_elements_invariant": all_inv}
        # ---- required invalid control: mu = 1, swap rows 0 and 1
        sw = invariance(mat(1, (1, 0, 2, 3, 4, 5)), cols)
        res["controls"].append({"candidate": name, "control": "required invalid generator (mu=1, swap rows 0/1)",
                                "expected": "NOT invariant", "observed": sw,
                                "as_expected": not sw["invariant"]})
        # ---- discrimination controls (observed values recorded; expectation stated per control)
        if name == "T10-zero-first":
            for lab, g in (("mu=1 with the 6-cycle", (1, (1, 2, 3, 4, 5, 0))),
                           ("mu=19 with the 6-cycle (not a group element)", (19, (1, 2, 3, 4, 5, 0)))):
                r = invariance(mat(*g), cols)
                res["controls"].append({"candidate": name, "control": "wrong multiplier: " + lab,
                                        "expected": "NOT invariant", "observed": r, "as_expected": not r["invariant"]})
            Gs = closure([mat(mu, tuple(pi), "swapped") for mu, pi in gens_raw])
            ex = ([zero] if zero_mode else []) + [c for b in bases for c in sorted(orbit(Gs, b))]
            r = {"invariant_under_swapped_generator": invariance(mat(10, (1, 2, 3, 4, 5, 0), "swapped"), cols)["invariant"],
                 "swapped_expansion_equals_DM": Counter(ex) == Counter(cols)}
            res["controls"].append({"candidate": name,
                                    "control": "convention swap c_{pi(x)} instead of c_{pi^-1(x)} (group <(10, pi^-1)>)",
                                    "expected": "NOT invariant and expansion mismatch (convention matters for T10)",
                                    "observed": r, "as_expected": not any(r.values())})
        else:
            r = invariance(mat(10, (1, 2, 0, 4, 5, 3)), cols)
            res["controls"].append({"candidate": name, "control": "wrong multiplier: mu=10 with (012)(345)",
                                    "expected": "NOT invariant", "observed": r, "as_expected": not r["invariant"]})
            Gs = closure([mat(mu, tuple(pi), "swapped") for mu, pi in gens_raw])
            r = {"swapped_group_equals_freeze_group": Gs == G}
            res["controls"].append({"candidate": name,
                                    "control": "convention swap c_{pi(x)} (mu=1 and the permutation group is closed "
                                               "under inverses, so the same group is expected: non-discriminating)",
                                    "expected": "same group", "observed": r,
                                    "as_expected": r["swapped_group_equals_freeze_group"]})
        bb = [list(b) for b in bases]
        bb[0][-1] = (bb[0][-1] + 1) % N
        ex = ([zero] if zero_mode else []) + [c for b in bb for c in sorted(orbit(G, tuple(b)))]
        res["controls"].append({"candidate": name, "control": "perturbed first base (last entry +1 mod 27)",
                                "expected": "expansion != DM columns",
                                "observed": {"expansion_equals_DM": Counter(ex) == Counter(cols)},
                                "as_expected": Counter(ex) != Counter(cols)})
        # ---- DM -> CFR from the definitions, byte-identical regeneration
        R, why = dm_to_cfr(D)
        require(R is not None, "dm_to_cfr failed: %s" % why)
        regen = ser(R)
        regen_path = OUT / ("%s-CFR.regen.raw" % letter)
        write_x(regen_path, regen)
        v27, keys = cfr_violations(R, sub_cyclic)
        v3, _ = cfr_violations(R, sub_z3cubed)
        Dc = cfr_to_dm(R_pin)
        out["dm_to_cfr"] = {
            "rule": "b_j[c]=(D_j[c]-D_0[c]) mod 27; x=b_1[c]; CFR row j-1 has symbol x at position b_j[c] (j=1..5)",
            "pinned_DM_row0_all_zero": all(v == 0 for v in D[0]),
            "note": ("row 0 of the pinned DM is all zero, so the column subtraction is the identity for these inputs; "
                     "the cyclic (mod 27) arithmetic is what the DM/CFR validity checks below depend on"),
            "regenerated": rel(regen_path), "regenerated_sha256": sha(regen), "regenerated_bytes": len(regen),
            "byte_identical_to_parent_pin": regen == raw[letter + "-CFR.raw"],
            "first_row_is_identity": R[0] == list(range(N)),
            "cfr_check_Z27": {"violations": v27, "distinct_keys": keys, "expected_keys": (K - 1) * N * (N - 1),
                              "pass": v27 == 0 and keys == (K - 1) * N * (N - 1)},
            "cfr_check_Z3cubed_control": {"violations": v3},
            "converse": {"rule": "D'_0 = 0, D'_j[s] = pos of symbol s in CFR row j-1 (columns indexed by symbols)",
                         "D_prime_is_Z27_DM": not dm_bad_pairs(Dc, sub_cyclic),
                         "D_prime_columns_equal_pinned_DM_columns": Counter(columns(Dc)) == Counter(cols)}}
        # ---- mutated-DM control (swap entries of row 2 at columns 1 and 2)
        Dm = [row[:] for row in D]
        Dm[2][1], Dm[2][2] = Dm[2][2], Dm[2][1]
        Rm, whym = dm_to_cfr(Dm)
        mcfr = None if Rm is None else cfr_violations(Rm, sub_cyclic)[0]
        obs = {"dm_check_Z27_bad_pairs": len(dm_bad_pairs(Dm, sub_cyclic)),
               "orbit_expansion_equals_mutated_columns": Counter(expanded) == Counter(columns(Dm)),
               "regenerated_cfr_equals_pin": (Rm is not None and ser(Rm) == raw[letter + "-CFR.raw"]),
               "regenerated_cfr_Z27_violations": mcfr, "conversion_error": whym}
        res["controls"].append({"candidate": name, "control": "mutated DM: swap row 2 entries at columns 1 and 2",
                                "expected": "DM check fails, expansion mismatch, regenerated CFR != pin",
                                "observed": obs,
                                "as_expected": obs["dm_check_Z27_bad_pairs"] > 0 and
                                not obs["orbit_expansion_equals_mutated_columns"] and
                                not obs["regenerated_cfr_equals_pin"]})
        res["controls"].append({"candidate": name, "control": "group sensitivity: same DM/CFR under Z_3^3 digit arithmetic",
                                "expected": "fails (objects are cyclic Z_27 objects, not over GF(27)^+ = Z_3^3)",
                                "observed": {"DM_bad_pairs_Z3cubed": len(bad3), "CFR_violations_Z3cubed": v3},
                                "as_expected": len(bad3) > 0 and v3 > 0})
        a_ok = (out["dm_row0_all_zero_columns_normalised"] and len(G) == 6 and faithful and
                out["orbit_expansion"]["orbit_sizes_as_expected"] and
                out["orbit_expansion"]["expanded_multiset_equals_DM_columns"] and
                out["orbit_expansion"]["expanded_distinct"] and
                all(s.get("orbit_stabiliser_ok", True) for s in sizes) and
                all(g["invariant"] for g in gen_inv) and all_inv and
                out["model_crosscheck"]["model_group_equals_freeze_group_as_mu_piinv"] and rep_ok and
                (zero_mode or not fixed_cols))
        d_ok = (all(out["canonical_text_roundtrip"].values()) and out["dm_check_Z27"]["pass"] and
                out["dm_to_cfr"]["byte_identical_to_parent_pin"] and out["dm_to_cfr"]["cfr_check_Z27"]["pass"] and
                out["dm_to_cfr"]["converse"]["D_prime_is_Z27_DM"] and
                out["dm_to_cfr"]["converse"]["D_prime_columns_equal_pinned_DM_columns"])
        out["action_verdict"] = "PASS" if a_ok else "FAIL"
        out["dm_to_cfr_verdict"] = "PASS" if d_ok else "FAIL"
        action_ok = action_ok and a_ok
        dm2cfr_ok = dm2cfr_ok and d_ok
        res["candidates"][name] = out
    controls_ok = all(c["as_expected"] for c in res["controls"])
    res["converse_explanation"] = (
        "DM -> CFR: subtracting D_0 columnwise keeps every row-pair difference multiset, so b_0 = 0 and each b_j "
        "(j >= 1) is a bijection columns -> Z_27 (pair (0,j)); hence CFR row j-1 (symbol b_1[c] at position b_j[c]) is "
        "a permutation. If rows j != j' shared (a,b,d) with a = b_1[c] != b = b_1[c'], then b_j[c'] - b_j[c] = "
        "b_j'[c'] - b_j'[c], i.e. (b_j - b_j')[c] = (b_j - b_j')[c'], contradicting the DM property of pair (j,j'). "
        "Converse CFR -> DM: with D'_0 = 0 and D'_j[s] = pos_{j-1}(s), pair (0,j) is a bijection because each row is a "
        "permutation, and a repeated difference in pair (j,j') at symbols a != b is exactly a shared (a,b,d) with "
        "d != 0. Every subtraction is mod 27 (Z_27); the Z_3^3 controls show the same arrays are not DMs/CFRs over the "
        "additive group of GF(27).")
    res["non_claims"] = [
        "No claim that A and B are non-isomorphic, or isomorphic, under any equivalence; nothing was tested.",
        "The G-invariance is a statement about the DM column multiset with columns taken modulo constants; no CFR "
        "row-isotopy, CFR automorphism or CFR-level symmetry is claimed.",
        "No gate, novelty or priority claim; a search miss is not novelty.",
        "Raw witness validity rests on the definition checks of the raw bytes, not on the symmetry model or producer."]
    res["verdicts"] = {"group_action_orbit_expansion": "PASS" if action_ok else "FAIL",
                       "dm_to_cfr_regeneration": "PASS" if dm2cfr_ok else "FAIL",
                       "controls_all_as_expected": controls_ok}
    res["host_time_end"] = now()
    write_x(OUT / "audit-result.json", (json.dumps(res, indent=1) + "\n").encode())
    print(json.dumps({"verdicts": res["verdicts"],
                      "candidates": {k: [v["action_verdict"], v["dm_to_cfr_verdict"]] for k, v in res["candidates"].items()},
                      "controls": [(c["candidate"], c["control"][:40], c["as_expected"]) for c in res["controls"]]},
                     indent=1))


if __name__ == "__main__":
    main()
