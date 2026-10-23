#!/usr/bin/env python3
"""binding_check.py -- parent binding checker for the LOWER46 computer cases (lane ame46-support).

Written by the parent from SUPPORT_LOWER46.r1.md section 3 and the parent task. The pinned engine (copied and
SHA-verified into pinned_code/) is imported ONLY to regenerate base clauses through SmallGen.build_gen; nothing else
of it is called (no run(), write(), group(), solver, or checker).

Items checked (parent task numbering):
 1. Profiles: independent enumeration of the deficit-profile multisets for (t, e) in CASES (partitions of h = 36 - t
    into parts >= 2, each <= 6, at most 6 parts; 4-multisets filtered by Lemma 12) must equal the JSON report.
 2. Each final-enumeration CNF: strict header, base clauses equal line by line to the regenerated base, then blocking
    clauses (all literals negative, exactly 2h + e distinct point variables, strictly increasing) cut into
    consecutive segments of the reported orbit sizes in JSON representative order; no trailing data.
 3. Each representative: H-orbit by breadth-first search over generators (adjacent coordinate swaps between equal
    partitions; adjacent value swaps inside equal-deficit classes; both contiguous in the normal form, which is
    asserted). The segment must equal the orbit as a set with no duplicate clause; |orbit| must divide |H|; |H|
    must equal the product formula and the JSON group_order.
 4. failures() is an independent N-only predicate (domain, size, line, deficit, orth); every representative and
    every orbit image must satisfy it.
 5. The independent enumerator outputs (enum-runs.json from run_enum.py / enum_nsets.c) must equal the union of the
    blocked orbits per profile, and every enumerated set must satisfy failures().
 6. Completion CNFs: strict DIMACS well-formedness; headers recorded; independent allowed-point count compared with
    the JSON report (their encoding soundness is audited separately).
The integrator mode writes binding-result.json (mode "x"). The functions are imported by controls.py.
"""
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import datetime  # noqa: E402
import hashlib  # noqa: E402
import itertools  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import platform  # noqa: E402
import re  # noqa: E402
import resource  # noqa: E402
from collections import Counter, defaultdict  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
SNAP = HERE.parent / "ame46-lower46-parent-inputs-v1"
EXPLORE = SNAP / "explore" / "large_t_gen"
CASES = [(30, 0), (30, 2), (30, 3), (29, 2), (28, 0)]
PAIRS6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
RSS_CAP_BYTES = int(3.5 * 2 ** 30)
PINNED_CODE = ("large_t_gen.py", "large_t_e0.py", "ame_e0_cnf.py", "phase_check.py")

_P2, _P4 = (2, 2, 2), (2, 2, 2, 2)
# Frozen proof text, SUPPORT_LOWER46.r1.md section 4 (lines 189-209): orbit sizes per (t, e) and profile.
PROOF_TABLE = {
    (30, 0): {((3, 3), _P2, _P2, _P2): [108, 36], (_P2, _P2, _P2, _P2): []},
    (30, 2): {((3, 3), _P2, _P2, _P2): [], (_P2, _P2, _P2, _P2): []},
    (30, 3): {((3, 3), _P2, _P2, _P2): [], (_P2, _P2, _P2, _P2): []},
    (29, 2): {((3, 2, 2),) * 4: []},
    (28, 0): {
        ((4, 4), _P4, _P4, _P4): [2592, 10368, 20736, 13824, 10368, 5184, 5184, 1728, 2592, 2592, 1296, 432, 864,
                                  432],
        ((4, 2, 2), _P4, _P4, _P4): [2592, 5184, 1728, 5184, 5184, 864, 864],
        ((3, 3, 2),) * 4: [16],
        ((3, 3, 2),) * 3 + (_P4,): [],
        ((3, 3, 2),) * 2 + (_P4, _P4): [],
        ((3, 3, 2), _P4, _P4, _P4): [],
        (_P4,) * 4: [10368, 31104, 20736, 2592],
    },
}

HEADER_RE = re.compile(rb"p cnf ([1-9][0-9]*) ([1-9][0-9]*)\n")
BLOCK_RE = re.compile(rb"(?:-[1-9][0-9]* )+0\n")
CLAUSE_RE = re.compile(rb"(?:-?[1-9][0-9]* )*0\n")


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def peak_rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS


def rss_guard():
    if peak_rss() > RSS_CAP_BYTES:
        raise MemoryError("peak RSS above the 3.5 GiB self-imposed cap")


# ----------------------------------------------------------------------------------------------- item 1: profiles
def partitions_indep(h):
    """Partitions of h into parts in [2, 6] with at most 6 parts, as non-increasing tuples (brute force)."""
    found = set()
    for k in range(1, 7):
        for combo in itertools.combinations_with_replacement(range(2, 7), k):
            if sum(combo) == h:
                found.add(tuple(sorted(combo, reverse=True)))
    return sorted(found, reverse=True)


def lemma12_ok(quad):
    """Lemma 12: the largest part of coordinate i is at most the number of parts of every other coordinate."""
    return all(max(quad[i]) <= min(len(quad[j]) for j in range(4) if j != i) for i in range(4))


def canon(prof):
    return tuple(sorted(tuple(p) for p in prof))


def check_profiles(t, e, report):
    h = 36 - t
    parts = partitions_indep(h)
    all_ms = {canon(q) for q in itertools.product(parts, repeat=4)}
    kept = {ms for ms in all_ms if lemma12_ok(ms)}
    listed = [canon(p["profile"]) for p in report["profiles"]]
    fails = []
    if (report.get("t"), report.get("e"), report.get("h")) != (t, e, h):
        fails.append("report_case_mismatch")
    if len(set(listed)) != len(listed):
        fails.append("profile_duplicate")
    if set(listed) - kept:
        fails.append("profile_extra")
    if kept - set(listed):
        fails.append("profile_missing")
    for p in report["profiles"]:
        if "skipped" in p:
            fails.append("profile_skipped")
        if any(sum(q) != h or not all(2 <= x <= 6 for x in q) or len(q) > 6 or list(q) != sorted(q, reverse=True)
               for q in p["profile"]):
            fails.append("profile_malformed")
    dropped = sorted(all_ms - kept)
    return {
        "h": h,
        "partitions": [list(p) for p in parts],
        "multisets_before_lemma12": len(all_ms),
        "kept_by_lemma12": [[list(q) for q in ms] for ms in sorted(kept)],
        "dropped_by_lemma12": len(dropped),
        "json_profiles": [[list(q) for q in ms] for ms in listed],
        "equal": set(listed) == kept and len(set(listed)) == len(listed),
        "fails": sorted(set(fails)),
    }


# ------------------------------------------------------------------------------------------ normal form, numbering
def normal_form(prof):
    """LOWER46 section 3 step 1: V_i = {6 - |V_i|, ..., 5}; parts assigned in the given order to increasing values."""
    V, d = [], []
    for parts in prof:
        vals = list(range(6 - len(parts), 6))
        V.append(vals)
        d.append(dict(zip(vals, parts)))
    return V, d


class Numbering:
    """Point variable = 1 + lexicographic rank in V_0 x V_1 x V_2 x V_3 (last coordinate fastest)."""

    def __init__(self, V):
        self.lo = [v[0] for v in V]
        self.sizes = [len(v) for v in V]
        self.npts = math.prod(self.sizes)

    def var(self, x):
        r = 0
        for i in range(4):
            r = r * self.sizes[i] + (x[i] - self.lo[i])
        return r + 1

    def point(self, v):
        if not 1 <= v <= self.npts:
            raise ValueError("not a point variable")
        k, x = v - 1, [0] * 4
        for i in (3, 2, 1, 0):
            k, r = divmod(k, self.sizes[i])
            x[i] = self.lo[i] + r
        return tuple(x)


def parse_point(s):
    if not re.fullmatch(r"[0-5]{4}", s):
        raise ValueError("bad point string %r" % s)
    return tuple(int(c) for c in s)


# ---------------------------------------------------------------------------------- item 4: independent predicate
def failures(N, V, d, e):
    """Violated N-only conditions (empty list: N satisfies the predicate).
    domain : N is a set of points of V_0 x V_1 x V_2 x V_3;
    size   : |N| = 2h + e;
    line   : every line of every coordinate pair meets N in 0 or >= 2 points;
    deficit: for every ordered pair (i, j) and a in V_i exactly d_{i,a} lines (a, b), b in V_j, meet N;
    orth   : in each reshaping and orientation no two distinct rows share exactly one column."""
    bad = set()
    pts = list(N)
    S = set(pts)
    if len(S) != len(pts):
        bad.add("domain")
    for x in pts:
        if not (isinstance(x, tuple) and len(x) == 4 and all(x[i] in V[i] for i in range(4))):
            bad.add("domain")
    hs = {sum(di.values()) for di in d}
    if len(hs) != 1:
        raise ValueError("deficits of different coordinates have different sums")
    h = hs.pop()
    if len(S) != 2 * h + e:
        bad.add("size")
    for i, j in PAIRS6:
        cnt = Counter((x[i], x[j]) for x in S)
        if any(c == 1 for c in cnt.values()):
            bad.add("line")
        for a in V[i]:
            if len({z[1] for z in cnt if z[0] == a}) != d[i][a]:
                bad.add("deficit")
        for b in V[j]:
            if len({z[0] for z in cnt if z[1] == b}) != d[j][b]:
                bad.add("deficit")
    for A, B in PAIRINGS:
        for R, C in ((A, B), (B, A)):
            sup = defaultdict(set)
            for x in S:
                sup[(x[R[0]], x[R[1]])].add((x[C[0]], x[C[1]]))
            rows = sorted(sup)
            for r1, r2 in itertools.combinations(rows, 2):
                if len(sup[r1] & sup[r2]) == 1:
                    bad.add("orth")
                    break
    return sorted(bad)


# --------------------------------------------------------------------------------------------- item 3: H-orbits
def generators(prof):
    V, d = normal_form(prof)
    for i in range(4):
        for k in range(i + 1, 4):
            if prof[i] == prof[k] and any(prof[j] != prof[i] for j in range(i, k + 1)):
                raise AssertionError("equal partitions are not contiguous")
    gens = [("coord", i) for i in range(3) if prof[i] == prof[i + 1]]
    for i in range(4):
        cls = [d[i][a] for a in V[i]]
        for k in range(len(cls)):
            for k2 in range(k + 1, len(cls)):
                if cls[k] == cls[k2] and any(cls[j] != cls[k] for j in range(k, k2 + 1)):
                    raise AssertionError("deficit class is not contiguous")
        gens += [("value", i, a, b) for a, b in zip(V[i], V[i][1:]) if d[i][a] == d[i][b]]
    return gens


def apply_gen(g, x):
    if g[0] == "coord":
        i = g[1]
        return x[:i] + (x[i + 1], x[i]) + x[i + 2:]
    _, i, a, b = g
    if x[i] == a:
        return x[:i] + (b,) + x[i + 1:]
    if x[i] == b:
        return x[:i] + (a,) + x[i + 1:]
    return x


def orbit_bfs(N0, gens):
    start = frozenset(N0)
    seen, frontier = {start}, [start]
    while frontier:
        nxt = []
        for S in frontier:
            for g in gens:
                T = frozenset(apply_gen(g, x) for x in S)
                if T not in seen:
                    seen.add(T)
                    nxt.append(T)
        frontier = nxt
        rss_guard()
    return seen


def group_order_formula(prof):
    _, d = normal_form(prof)
    order = 1
    for c in Counter(tuple(p) for p in prof).values():
        order *= math.factorial(c)
    for i in range(4):
        for c in Counter(d[i].values()).values():
            order *= math.factorial(c)
    return order


# ---------------------------------------------------------------------------------------- item 2: CNF binding
def regenerate_base(prof, e, h):
    """Base clauses from the pinned engine (pinned_code/large_t_gen.py, SmallGen.build_gen only)."""
    sys.path.insert(0, str(HERE / "pinned_code"))
    try:
        import large_t_gen as ltg  # pinned copy, SHA-verified by verify_pins()
    finally:
        sys.path.pop(0)
    if Path(ltg.__file__).resolve().parent != (HERE / "pinned_code").resolve():
        raise RuntimeError("large_t_gen imported from an unexpected location")
    S = ltg.SmallGen([tuple(p) for p in prof])
    S.build_gen(e, h)
    return S.nv, S.cl, dict(S.var), len(S.points)


def parse_block(line, n, npts):
    reasons = []
    try:
        vals = [int(tok) for tok in line.split()]
    except ValueError:
        return None, ["block_malformed"]
    if not line.endswith(b"\n") or not vals or vals[-1] != 0 or 0 in vals[:-1]:
        return None, ["block_malformed"]
    lits = vals[:-1]
    if any(lit > 0 for lit in lits):
        reasons.append("block_literal_positive")
    vs = [abs(lit) for lit in lits]
    if len(vs) != n:
        reasons.append("block_length")
    if len(set(vs)) != len(vs):
        reasons.append("block_duplicate_literal")
    if any(v > npts for v in vs):
        reasons.append("block_var_out_of_range")
    if any(b <= a for a, b in zip(vs, vs[1:])):
        reasons.append("block_unsorted")
    if not reasons and not BLOCK_RE.fullmatch(line):
        reasons.append("block_malformed")
    return (None if reasons else vs), reasons


def check_final_cnf(path, prof, e, rep_sizes, base):
    """Stream one final-enumeration CNF. Returns (info, segments, fails)."""
    h = sum(prof[0])
    n = 2 * h + e
    V, _ = normal_form(prof)
    num = Numbering(V)
    nv, cl, engine_var, engine_npts = base
    fails, info = [], {}
    if engine_npts != num.npts or len(engine_var) != num.npts or any(
            num.var(x) != v for x, v in engine_var.items()):
        fails.append("numbering_mismatch")
    if any(not 1 <= abs(lit) <= nv for c in cl for lit in c):
        fails.append("base_var_out_of_range")
    expected_blocks = sum(rep_sizes)
    info.update(base_clauses=len(cl), nv=nv, point_vars=num.npts, expected_blocks=expected_blocks,
                expected_header="p cnf %d %d" % (nv, len(cl) + expected_blocks))
    segments = []
    with open(path, "rb") as fh:
        header = fh.readline()
        info["header"] = header.decode(errors="replace").rstrip("\n")
        if not HEADER_RE.fullmatch(header):
            fails.append("header_format")
            return info, segments, fails
        if info["header"] != info["expected_header"]:
            fails.append("header_mismatch")
        for k, c in enumerate(cl):
            line = fh.readline()
            if line != (" ".join(map(str, c)) + " 0\n").encode():
                fails.append("base_line_mismatch")
                info["first_base_mismatch_file_line"] = k + 2
                return info, segments, fails
        info["base_lines_identical"] = len(cl)
        eof = False
        for size in rep_sizes:
            seg = []
            for _ in range(size):
                line = fh.readline()
                if not line:
                    fails.append("premature_eof")
                    eof = True
                    break
                vs, why = parse_block(line, n, num.npts)
                if why:
                    fails.extend(why)
                    seg.append(None)
                    continue
                seg.append(frozenset(num.point(v) for v in vs))
            segments.append(seg)
            if eof:
                break
        if not eof and fh.read(1):
            fails.append("trailing_data")
    return info, segments, sorted(set(fails))


def check_profile(t, e, entry, enum_sets=None, cnf_path=None):
    """Items 2-5 for one profile entry of a JSON report (cnf_path overrides the pinned CNF, for controls only)."""
    prof = tuple(tuple(p) for p in entry["profile"])
    h = 36 - t
    tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)
    path = EXPLORE / (tag + ".cnf") if cnf_path is None else Path(cnf_path)
    V, d = normal_form(prof)
    reps = [[parse_point(s) for s in r["N"]] for r in entry["reps"]]
    sizes = [r["orbit_size"] for r in entry["reps"]]
    out = {"tag": tag, "cnf": str(path.relative_to(SNAP) if cnf_path is None else path.relative_to(HERE)),
           "profile": [list(p) for p in prof],
           "orbits_json": entry["orbits"], "orbit_sizes_json": sizes}
    fails = []
    if entry["orbits"] != len(reps):
        fails.append("orbit_count_mismatch")
    table = PROOF_TABLE.get((t, e), {}).get(prof)
    out["proof_table_sizes"] = table
    if table != sizes:
        fails.append("proof_table_mismatch")
    gorder = group_order_formula(prof)
    out["group_order_formula"] = gorder
    out["group_order_json"] = entry["group_order"]
    if gorder != entry["group_order"]:
        fails.append("group_order_mismatch")
    base = regenerate_base(prof, e, h)
    info, segments, cfails = check_final_cnf(path, prof, e, sizes, base)
    out["cnf_check"] = info
    fails += cfails
    gens = generators(prof)
    out["generators"] = len(gens)
    rep_results, union = [], set()
    pred_checked = pred_failed = 0
    for k, (N0, size) in enumerate(zip(reps, sizes)):
        r = {"index": k, "orbit_size_json": size, "rep_points": len(N0)}
        rfails = []
        rep_pred = failures(N0, V, d, e)
        r["rep_predicate_failures"] = rep_pred
        if rep_pred:
            rfails.append("rep_predicate_fail")
        orb = orbit_bfs(N0, gens)
        r["orbit_size_bfs"] = len(orb)
        r["stabilizer_order"] = gorder // len(orb) if gorder % len(orb) == 0 else None
        if gorder % len(orb):
            rfails.append("orbit_size_not_dividing_H")
        if len(orb) != size:
            rfails.append("orbit_size_mismatch")
        bad_images = 0
        for img in orb:
            pred_checked += 1
            if failures(img, V, d, e):
                bad_images += 1
        pred_failed += bad_images
        r["orbit_images_failing_predicate"] = bad_images
        if bad_images:
            rfails.append("orbit_image_predicate_fail")
        seg = segments[k] if k < len(segments) else []
        r["segment_clauses"] = len(seg)
        clean = [s for s in seg if s is not None]
        r["segment_distinct"] = len(set(clean))
        if len(set(clean)) != len(seg):
            rfails.append("segment_duplicate_or_malformed")
        r["segment_equals_orbit"] = set(clean) == orb and len(seg) == len(orb)
        if not r["segment_equals_orbit"]:
            rfails.append("segment_orbit_mismatch")
        r["rep_in_segment"] = frozenset(N0) in set(clean)
        if union & orb:
            rfails.append("orbits_overlap")
        union |= orb
        r["verdict"] = "FAIL" if rfails else "PASS"
        r["fails"] = rfails
        rep_results.append(r)
        fails += rfails
        rss_guard()
    out["reps"] = rep_results
    out["blocked_sets"] = len(union)
    out["predicate_images_checked"] = pred_checked
    out["predicate_images_failed"] = pred_failed
    if enum_sets is not None:
        extra_bad = sum(1 for s in enum_sets - union if failures(s, V, d, e))
        both_bad = sum(1 for s in enum_sets & union if failures(s, V, d, e)) if enum_sets & union else 0
        out["enum"] = {"enumerated": len(enum_sets), "blocked": len(union), "common": len(enum_sets & union),
                       "only_enumerated": len(enum_sets - union), "only_blocked": len(union - enum_sets),
                       "only_enumerated_failing_predicate": extra_bad, "common_failing_predicate": both_bad}
        if enum_sets != union:
            fails.append("enumeration_mismatch")
        if extra_bad or both_bad:
            fails.append("enumerated_set_failing_predicate")
    out["fails"] = sorted(set(fails))
    out["verdict"] = "FAIL" if fails else "PASS"
    return out


# ------------------------------------------------------------------------------------- item 6: completion CNFs
def check_completion_cnf(path, rep_N, allowed_json):
    info, fails = {}, []
    with open(path, "rb") as fh:
        header = fh.readline()
        info["header"] = header.decode(errors="replace").rstrip("\n")
        mh = HEADER_RE.fullmatch(header)
        if not mh:
            return info, ["header_format"]
        nv, nc = int(mh[1]), int(mh[2])
        count = empty = maxvar = nlits = 0
        lens = Counter()
        for line in fh:
            if not CLAUSE_RE.fullmatch(line):
                fails.append("clause_malformed")
                break
            lits = [int(tok) for tok in line.split()[:-1]]
            if lits and max(abs(x) for x in lits) > nv:
                fails.append("var_out_of_range")
            if len(set(lits)) != len(lits):
                fails.append("duplicate_literal")
            count += 1
            empty += not lits
            nlits += len(lits)
            maxvar = max([maxvar] + [abs(x) for x in lits])
            lens[len(lits)] += 1
    if count != nc:
        fails.append("clause_count_mismatch")
    holes = {P: {(x[P[0]], x[P[1]]) for x in rep_N} for P in PAIRS6}
    allowed = sum(1 for x in itertools.product(range(6), repeat=4)
                  if all((x[i], x[j]) not in holes[(i, j)] for i, j in PAIRS6))
    if allowed != allowed_json:
        fails.append("allowed_points_mismatch")
    if allowed > nv:
        fails.append("fewer_vars_than_allowed_points")
    info.update(nv=nv, clauses_header=nc, clauses_read=count, empty_clauses=empty, max_var=maxvar, literals=nlits,
                clause_length_histogram={str(k): v for k, v in sorted(lens.items())},
                allowed_points_independent=allowed, allowed_points_json=allowed_json)
    return info, sorted(set(fails))


# ----------------------------------------------------------------------------------------------- pins and I/O
def verify_pins():
    receipt = SNAP / "parent-pin-receipt.json"
    pins = json.loads(receipt.read_text())
    files = pins["files"]
    out = {"parent_pin_receipt_sha256": sha256_file(receipt), "checked": {}, "fails": []}
    wanted = ["review/SUPPORT_LOWER46.r1.md"] + ["code/" + n for n in PINNED_CODE] + [
        "evidence/large_t_gen_t%d_e%d.json" % c for c in CASES]
    wanted += [k for k in files if k.startswith("explore/large_t_gen/") and k.endswith(".cnf")]
    for rel in wanted:
        got = sha256_file(SNAP / rel)
        out["checked"][rel] = got
        if files.get(rel) != got:
            out["fails"].append("pin_mismatch:" + rel)
    for name in PINNED_CODE:
        got = sha256_file(HERE / "pinned_code" / name)
        out["checked"]["pinned_code/" + name] = got
        if files.get("code/" + name) != got:
            out["fails"].append("pinned_copy_mismatch:" + name)
    on_disk = sorted(p.name for p in EXPLORE.glob("*.cnf"))
    pinned = sorted(Path(k).name for k in files if k.startswith("explore/large_t_gen/") and k.endswith(".cnf"))
    out["cnf_files_on_disk"] = len(on_disk)
    out["cnf_files_pinned"] = len(pinned)
    if on_disk != pinned:
        out["fails"].append("cnf_file_set_differs_from_pins")
    pair_cnfs = sorted(Path(p["cnf"]).name for p in pins["pairs"])
    if pair_cnfs != pinned:
        out["fails"].append("pair_list_differs_from_pinned_cnfs")
    return out, pins


def load_enum_sets(enum_runs, tag):
    run = enum_runs["final"].get(tag)
    if run is None or not run.get("complete"):
        return None
    path = HERE / run["output"]
    if sha256_file(path) != run["output_sha256"]:
        raise RuntimeError("enumerator output changed: " + run["output"])
    sets = set()
    with open(path) as fh:
        for line in fh:
            sets.add(frozenset(parse_point(s) for s in line.split()))
    if len(sets) != run["solutions"]:
        raise RuntimeError("enumerator output has duplicate or missing lines: " + run["output"])
    return sets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--enum-runs", default="enum-runs.json")
    ap.add_argument("--controls", default="controls-result.json")
    ap.add_argument("--output", default="binding-result.json")
    a = ap.parse_args()
    started = now()
    result = {"started": started, "python": platform.python_version(), "scope": (
        "Binding of the 14 pinned final-enumeration CNFs and the 4 completion CNFs to the claimed mathematics "
        "(profile completeness, base encoding identity, orbit blocking, independent predicate, independent "
        "enumeration). UNSAT of the CNFs is the parent's separate replay; completion-CNF encoding soundness and the "
        "phase/completion exclusions are audited separately. This receipt does not accept the theorem.")}
    pins_out, pins = verify_pins()
    result["pins"] = pins_out
    fails = list(pins_out["fails"])
    enum_path = HERE / a.enum_runs
    enum_runs = json.loads(enum_path.read_text())
    result["enum_runs_sha256"] = sha256_file(enum_path)
    cases = {}
    completion_jobs = []
    for t, e in CASES:
        rep_path = SNAP / "evidence" / ("large_t_gen_t%d_e%d.json" % (t, e))
        report = json.loads(rep_path.read_text())
        prof_res = check_profiles(t, e, report)
        fails += ["%s:t%d_e%d" % (f, t, e) for f in prof_res["fails"]]
        per_profile = []
        for entry in report["profiles"]:
            tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in entry["profile"])
            enum_sets = load_enum_sets(enum_runs, tag)
            res = check_profile(t, e, entry, enum_sets)
            if enum_sets is None:
                res["enum"] = "UNKNOWN (no complete enumerator run)"
                res["fails"] = sorted(set(res["fails"]) | {"enumeration_unknown"})
                res["verdict"] = "FAIL"
            per_profile.append(res)
            fails += ["%s:%s" % (f, tag) for f in res["fails"]]
            for k, r in enumerate(entry["reps"]):
                if r.get("completion_status") is not None:
                    completion_jobs.append((tag, k, r))
        cases["t%d_e%d" % (t, e)] = {"profiles": prof_res, "per_profile": per_profile}
    result["cases"] = cases
    comp = {}
    pinned_completion = sorted(Path(k).name for k in pins["files"]
                               if k.startswith("explore/large_t_gen/") and k.endswith("_completion.cnf"))
    expected_completion = sorted("%s_rep%d_completion.cnf" % (tag, k) for tag, k, _ in completion_jobs)
    if pinned_completion != expected_completion:
        fails.append("completion_cnf_set_mismatch")
    for tag, k, r in completion_jobs:
        name = "%s_rep%d_completion.cnf" % (tag, k)
        info, cf = check_completion_cnf(EXPLORE / name, [parse_point(s) for s in r["N"]],
                                        r["completion_allowed_points"])
        info["completion_status_json"] = r["completion_status"]
        info["sha256"] = pins_out["checked"].get("explore/large_t_gen/" + name)
        info["fails"] = cf
        info["verdict"] = "FAIL" if cf else "PASS"
        comp[name] = info
        fails += ["%s:%s" % (f, name) for f in cf]
    result["completion_cnfs"] = comp
    ctrl_path = HERE / a.controls
    if ctrl_path.exists():
        ctrl = json.loads(ctrl_path.read_text())
        result["controls"] = {"file": a.controls, "sha256": sha256_file(ctrl_path), "verdict": ctrl.get("verdict")}
        if ctrl.get("verdict") != "PASS":
            fails.append("controls_not_pass")
    else:
        result["controls"] = None
        fails.append("controls_missing")
    if enum_runs.get("verdict") != "PASS":
        fails.append("enum_runs_not_pass")
    pins_after, _ = verify_pins()
    result["pins_rechecked_at_end_equal"] = pins_after["checked"] == pins_out["checked"] and not pins_after["fails"]
    if not result["pins_rechecked_at_end_equal"]:
        fails.append("pins_changed_during_run")
    code = {name: sha256_file(HERE / name) for name in
            ("binding_check.py", "run_enum.py", "controls.py", "enum_nsets.c", "enum_nsets")}
    code.update({"pinned_code/" + n: sha256_file(HERE / "pinned_code" / n) for n in PINNED_CODE})
    result["code_sha256"] = code
    result["limits"] = {"cpu": "single process, single thread", "rss_cap_self_imposed_bytes": RSS_CAP_BYTES,
                        "peak_rss_bytes": peak_rss(), "new_data_cap_bytes": 2 ** 30}
    result["fails"] = fails
    result["verdict"] = "FAIL" if fails else "PASS"
    result["ended"] = now()
    with open(HERE / a.output, "x") as fh:
        json.dump(result, fh, indent=1)
        fh.write("\n")
    print(json.dumps({"verdict": result["verdict"], "fails": fails[:20], "peak_rss_bytes": peak_rss()}))


if __name__ == "__main__":
    main()
