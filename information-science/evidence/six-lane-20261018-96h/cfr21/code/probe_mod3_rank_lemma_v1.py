#!/usr/bin/env python3
"""probe_mod3_rank_lemma_v1.py (ContinueCFR21; frozen before execution; stdlib only; self wall budget 280 s).
Machine checks of the finite combinatorial steps behind 'mod-3 affine rank >= 5 for every (Z_n,7;1)-DM, 3 || n':
 Part1: for every nonzero translation-invariant character chi in F3^7 (sum chi = 0) of support <= 5, exhibit roots
        r1, r2 such that every nonzero w in span(r1, r2) is congruent mod <chi> to a nonzero multiple of a root and
        w is not in <chi>  (=> 2-dim uniformity contradiction 21/9). Count such planes for support 6/7 too.
 Part2: no 2-dim subspace of {sum = 0} has all nonzero vectors of support >= 6 (Griesmer step), exhaustively.
 Part3: for each support-6/7 chi, search 3-dim subspaces W (W cap <chi> = 0) all of whose 13 lines are root lines
        mod <chi> (3-dim uniformity would give 21/27); report counts.
 Part4: parent lead: all 7-point caps of AG(3,3) containing 0 (translation fix): affine rank and number of determined
        directions (of 13); histogram.
Prints one JSON object."""
import sys, json, time, itertools
T0 = time.monotonic(); BUD = 280.0
def over(): return time.monotonic() - T0 > BUD
K = 7
def add(x, y): return tuple((a + b) % 3 for a, b in zip(x, y))
def sc(t, x): return tuple((t * a) % 3 for a in x)
def supp(x): return sum(1 for a in x if a)
ZERO = (0,) * K
allv = [v for v in itertools.product(range(3), repeat=K) if sum(v) % 3 == 0 and any(v)]
roots = []
for i in range(K):
    for j in range(K):
        if i != j:
            r = [0] * K; r[i] = 1; r[j] = 2; roots.append(tuple(r))
rootset = set(roots)
def is_root_mod(w, chi):
    # w congruent mod <chi> to a nonzero multiple of a root, and w not in <chi>
    span_chi = {ZERO, chi, sc(2, chi)}
    if w in span_chi: return False
    for t in range(3):
        if add(w, sc(t, chi)) in rootset: return True  # roots set is closed under negation
    return False
def plane_ok(r1, r2, chi):
    for a in range(3):
        for b in range(3):
            if a == 0 and b == 0: continue
            w = add(sc(a, r1), sc(b, r2))
            if not is_root_mod(w, chi): return False
    return True
out = {"status": "OK"}
# Part 1
p1 = {}
witness_missing = []
canon_shapes = {}
for chi in allv:
    s = supp(chi)
    found = None; count = 0
    for r1, r2 in itertools.combinations(roots, 2):
        if r2 in (r1, sc(2, r1)): continue
        if plane_ok(r1, r2, chi):
            count += 1
            if found is None: found = (r1, r2)
            if s <= 5: break
    key = str(s)
    rec = p1.setdefault(key, {"chars": 0, "with_2d_witness": 0})
    rec["chars"] += 1
    if found: rec["with_2d_witness"] += 1
    elif s <= 5: witness_missing.append(chi)
    shape = tuple(sorted(chi))
    if shape not in canon_shapes: canon_shapes[shape] = {"support": s, "example_chi": chi, "witness": found}
out["part1_by_support"] = p1
out["part1_support_le5_without_witness"] = [list(c) for c in witness_missing]
out["part1_shapes"] = {str(k): {"support": v["support"], "example_chi": list(v["example_chi"]), "witness": [list(x) for x in v["witness"]] if v["witness"] else None} for k, v in canon_shapes.items()}
# Part 2
heavy = [v for v in allv if supp(v) >= 6]
bad2 = 0
for x, y in itertools.combinations(heavy, 2):
    if y in (sc(2, x),): continue
    if all(supp(add(sc(a, x), sc(b, y))) >= 6 for a in range(3) for b in range(3) if (a, b) != (0, 0)):
        bad2 += 1
out["part2_heavy_vectors"] = len(heavy); out["part2_2dim_subspaces_all_support_ge6"] = bad2
# Part 3
reps = {}
for v in heavy:
    reps.setdefault(tuple(sorted(v)), v)
p3 = {}
for shape, chi in reps.items():
    if over(): out["status"] = "INCOMPLETE_BUDGET"; break
    gens = []
    for r in roots:
        for t in range(3):
            g = add(r, sc(t, chi))
            if g not in gens: gens.append(g)
    hits = 0; tested = 0
    for g1, g2, g3 in itertools.combinations(gens, 3):
        # span must avoid <chi> and have 13 lines all root mod chi
        vecs = set()
        ok = True
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if (a, b, c) == (0, 0, 0): continue
                    w = add(add(sc(a, g1), sc(b, g2)), sc(c, g3))
                    if w == ZERO or not is_root_mod(w, chi): ok = False; break
                    vecs.add(w)
                if not ok: break
            if not ok: break
        tested += 1
        if ok and len(vecs) == 26: hits += 1
    p3[str(shape)] = {"support": supp(chi), "generators": len(gens), "triples_tested": tested, "3dim_all_root_subspaces": hits}
out["part3"] = p3
# Part 4: caps of size 7 in AG(3,3) containing origin
P = list(itertools.product(range(3), repeat=3))
others = [p for p in P if p != (0, 0, 0)]
def collinear(a, b, c): return all((x + y + z) % 3 == 0 for x, y, z in zip(a, b, c))
def dirkey(v):
    v = tuple(x % 3 for x in v)
    f = next(x for x in v if x)
    return v if f == 1 else tuple((2 * x) % 3 for x in v)
hist = {}; rank_hist = {}; ncaps = 0
def rank3(vs):
    rows = [list(v) for v in vs]; r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = 1 if rows[r][col] == 1 else 2
        rows[r] = [(x * inv) % 3 for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                f = rows[i][col]; rows[i] = [(a - f * b) % 3 for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
def ext(cap, start):
    global ncaps
    if over(): return
    if len(cap) == 7:
        ncaps += 1
        dirs = set(dirkey(tuple(a - b for a, b in zip(x, y))) for x, y in itertools.combinations(cap, 2))
        hist[len(dirs)] = hist.get(len(dirs), 0) + 1
        rk = rank3([p for p in cap if p != (0, 0, 0)])
        rank_hist[rk] = rank_hist.get(rk, 0) + 1
        return
    for idx in range(start, len(others)):
        p = others[idx]
        if all(not collinear(a, b, p) for a, b in itertools.combinations(cap, 2)):
            ext(cap + [p], idx + 1)
ext([(0, 0, 0)], 0)
out["part4_caps7_containing_origin"] = ncaps
out["part4_direction_count_hist"] = {str(a): b for a, b in sorted(hist.items())}
out["part4_affine_rank_hist"] = {str(a): b for a, b in sorted(rank_hist.items())}
if over(): out["status"] = "INCOMPLETE_BUDGET"
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
