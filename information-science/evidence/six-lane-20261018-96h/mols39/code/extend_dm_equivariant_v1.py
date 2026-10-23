#!/usr/bin/env python3
"""extend_dm_equivariant_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; self budget).
Exact search for ONE new row f extending a pinned k-row DM D over Z_n to a (k+1)-row DM, with f equivariant under a
pinned group G of pairs (mu, pi) that maps the EXACT column set of D onto itself (pi permutes the old rows only; the new
row is fixed by every pi):   f(g.c) = mu_g * f(c)  for all g in G and columns c.
Mode 'equivariant' (default): on each G-orbit O with representative c and stabiliser H_c, f(c) = w ranges over
{w : (mu_h - 1) w = 0 for all h in H_c}, and f on O is forced. Option (O, w) covers, for every old row i, the values
D_i(c') - f(c') (c' in O); options with an internal repeat are discarded. A (k+1)-row DM is exactly a choice of one option
per orbit covering every (i, value) item once (k*n items). All solutions are enumerated (DLX-style exact cover with
minimum-remaining-values item choice); each is written as a raw (k+1) x n file (exclusive create) and its count reported.
Mode 'free': every column is its own orbit (no symmetry), options (c, w) for all w; same exact cover (larger search).
Checks before search: D is a DM; G maps the column set onto itself exactly (else exit 3 'NOT_INVARIANT').
Args: raw raw_sha n gens_json mode budget_s out_dir(new) [max_solutions]"""
import sys, json, hashlib, time, os
T0 = time.monotonic()
raw_p, raw_sha, n, gens_s, mode, BUD, outd = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], float(sys.argv[6]), sys.argv[7]
MAXSOL = int(sys.argv[8]) if len(sys.argv) > 8 else 1000
rb = open(raw_p, 'rb').read(); h = hashlib.sha256(rb).hexdigest()
if h != raw_sha: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": h})); sys.exit(2)
rows = [[int(t) % n for t in ln.split()] for ln in rb.decode().splitlines() if ln.strip()]
k = len(rows); cols = [tuple(r[c] for r in rows) for c in range(n)]
out = {"input_sha256": h, "n": n, "k_old": k, "mode": mode}
dm_ok = all(len({(rows[i][c] - rows[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
out["old_dm_ok"] = dm_ok
if not dm_ok or len(set(cols)) != n: out["status"] = "OLD_NOT_DM"; print(json.dumps(out)); sys.exit(3)
gens = [(g[0] % n, tuple(g[1])) for g in json.loads(gens_s)]
def act(s, c):
    mu, perm = s; pinv = [0] * k
    for x in range(k): pinv[perm[x]] = x
    return tuple((mu * c[pinv[x]]) % n for x in range(k))
def compose(a, b): return ((a[0] * b[0]) % n, tuple(a[1][b[1][x]] for x in range(k)))
G = {(1, tuple(range(k)))}; fr = list(G)
while fr:
    nf = []
    for x in fr:
        for g in gens:
            y = compose(g, x)
            if y not in G: G.add(y); nf.append(y)
    fr = nf
G = sorted(G); S = set(cols)
if mode == 'equivariant' and not all(act(g, c) in S for g in G for c in cols):
    out["status"] = "NOT_INVARIANT"; print(json.dumps(out)); sys.exit(3)
out["group_order"] = len(G)
# orbits and options
if mode == 'equivariant':
    seen = set(); orbits = []
    for c in sorted(cols):
        if c in seen: continue
        orb = {}
        for g in G:
            d = act(g, c)
            orb.setdefault(d, g)          # d = g.c with first g reaching it
        seen |= set(orb); orbits.append((c, orb))
else:
    orbits = [(c, {c: (1, tuple(range(k)))}) for c in cols]
options = []      # (orbit index, w, list of item ids, f-values per column)
for oi, (c, orb) in enumerate(orbits):
    if mode == 'equivariant':
        stab = [g for g in G if act(g, c) == c]
        allowed = [w for w in range(n) if all(((g[0] - 1) * w) % n == 0 for g in stab)]
    else:
        allowed = list(range(n))
    for w in allowed:
        fvals = {d: (g[0] * w) % n for d, g in orb.items()}
        items = []; ok = True; seen_it = set()
        for d, fv in fvals.items():
            for i in range(k):
                it = i * n + (d[i] - fv) % n
                if it in seen_it: ok = False; break
                seen_it.add(it); items.append(it)
            if not ok: break
        if ok: options.append((oi, w, sorted(items), fvals))
out["orbits"] = len(orbits); out["orbit_sizes"] = sorted(len(o[1]) for o in orbits); out["options"] = len(options)
# exact cover: primary items = k*n (each exactly once) + orbit items (each exactly once)
NI = k * n; NO = len(orbits)
item_opts = [[] for _ in range(NI + NO)]
for idx, (oi, w, items, fv) in enumerate(options):
    for it in items: item_opts[it].append(idx)
    item_opts[NI + oi].append(idx)
covered = [False] * (NI + NO); blocked = [0] * len(options)
opt_items = [items + [NI + oi] for (oi, w, items, fv) in options]
sols = []; nodes = [0]; status = ["COMPLETE"]
def choose():
    best = None; bc = None
    for it in range(NI + NO):
        if covered[it]: continue
        cnt = 0
        for o in item_opts[it]:
            if not blocked[o]: cnt += 1
        if bc is None or cnt < bc:
            best, bc = it, cnt
            if cnt <= 1: break
    return best, bc
def search():
    nodes[0] += 1
    if (nodes[0] & 1023) == 0 and time.monotonic() - T0 > BUD: status[0] = "INCOMPLETE_BUDGET"; return True
    it, bc = choose()
    if it is None:
        sols.append([o for o in chosen]); return len(sols) >= MAXSOL
    if bc == 0: return False
    for o in list(item_opts[it]):
        if blocked[o]: continue
        # select o: cover its items, block every option sharing an item
        newly = []
        for j in opt_items[o]:
            covered[j] = True
            for o2 in item_opts[j]:
                if blocked[o2] == 0: newly.append(o2)
                blocked[o2] += 1
        chosen.append(o)
        stop = search()
        chosen.pop()
        for j in opt_items[o]:
            covered[j] = False
            for o2 in item_opts[j]: blocked[o2] -= 1
        if stop: return True
    return False
chosen = []
search()
if len(sols) >= MAXSOL and status[0] == "COMPLETE": status[0] = "STOPPED_AT_MAX_SOLUTIONS"
out.update({"status": status[0], "solutions": len(sols), "nodes": nodes[0]})
if sols:
    os.makedirs(outd, exist_ok=False)
    written = []
    for si, sol in enumerate(sols[:20]):
        f = {}
        for o in sol: f.update(options[o][3])
        newrow = [f[c] for c in cols]
        allrows = rows + [newrow]
        p = os.path.join(outd, 'ext_solution_%03d.raw' % si)
        with open(p, 'x') as fh: fh.write("\n".join(" ".join(map(str, r)) for r in allrows) + "\n")
        okdm = all(len({(allrows[i][c] - allrows[j][c]) % n for c in range(n)}) == n for i in range(k + 1) for j in range(i + 1, k + 1))
        written.append({"path": p, "sha256": hashlib.sha256(open(p, 'rb').read()).hexdigest(), "dm_ok": okdm,
                        "new_row_constant": len(set(newrow)) == 1})
    out["written"] = written
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
