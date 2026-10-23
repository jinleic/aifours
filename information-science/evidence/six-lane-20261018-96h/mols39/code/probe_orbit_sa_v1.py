#!/usr/bin/env python3
"""probe_orbit_sa_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; self budget).
Calibration probe (NOT a target search claim): simulated annealing over orbit representatives of a pinned orbit model
(orbit_dm_cnf_v1.py, imported by path after a SHA-256 check, used only for its Enc class: group, orbit types, coset
representatives, pair-orbit representatives, fixed coordinates, stabiliser generators).
State: representatives c^r; stabiliser constraints are kept exact by parametrising each representative by the orbits of
its stabiliser on rows (a rep fixed by s=(mu,pi) satisfies c_x = mu c_{pi^-1 x}; the probe supports stabilisers whose
generators fix every coordinate orbit through a single free 'leader' coordinate, which holds for the models used).
Cost = sum over pair representatives P and values w of max(0, count_P(w) - 1). Moves: change one free coordinate.
Metropolis acceptance at temperature T(t) = T0 * (T1/T0)^(t/budget). On cost 0 the representatives are decoded into
a raw DM (exclusive create) for independent checking.
Args: encoder enc_sha model model_sha seed budget_s T0 T1 out_dir(new)"""
import sys, json, hashlib, time, random, importlib.util, os, math
T_START = time.monotonic()
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
pinned(sys.argv[1], sys.argv[2]); M = json.loads(pinned(sys.argv[3], sys.argv[4]))
seed, BUD, T0, T1, outd = int(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), sys.argv[9]
spec = importlib.util.spec_from_file_location("orbenc", sys.argv[1]); mod = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True; spec.loader.exec_module(mod)
enc = mod.Enc(M); n, k = enc.n, enc.k
rng = random.Random(seed)
# parametrisation: for each orbit r, coordinates are determined by leaders: coordinate x = coef * leader_value
param = []          # per orbit: dict x -> (leader, coef) or ('const', value)
for r, ti in enumerate(enc.orbits):
    t = enc.types[ti]; fx = t["fixed"]
    # union-find over rows under stabiliser generators: c_x = mu * c_{pinv x}
    lead = {}
    for x in range(k):
        if x in fx: lead[x] = ('const', fx[x])
    changed = True
    rel = {}
    for (mu, perm) in t["Hgens"]:
        pinv = [0] * k
        for x in range(k): pinv[perm[x]] = x
        for x in range(k): rel.setdefault(x, []).append((pinv[x], mu))
    # BFS from each unassigned row
    for x in range(k):
        if x in lead: continue
        lead[x] = (x, 1); stack = [x]
        while stack:
            y = stack.pop(); ly, cy = lead[y]
            # c_y = mu * c_{pinv y}  => c_{pinv y} = mu^-1 c_y ; also neighbours mapping to y
            for (z, mu) in rel.get(y, []):
                if z not in lead: lead[z] = (ly, (pow(mu, -1, n) * cy) % n); stack.append(z)
            for z in range(k):
                for (w, mu) in rel.get(z, []):
                    if w == y and z not in lead: lead[z] = (ly, (mu * cy) % n); stack.append(z)
    param.append(lead)
free = [(r, x) for r in range(len(enc.orbits)) for x in range(k) if param[r][x][0] == x]
vals = {fx: rng.randrange(n) for fx in free}
def rep(r):
    out = []
    for x in range(k):
        l, c = param[r][x]
        out.append(c % n if l == 'const' else (c * vals[(r, l)]) % n)
    return out
# slot formulas: for pair index p, slot (r, gi): mu, prow, qrow
slots = {r: [] for r in range(len(enc.orbits))}
for pi_, pair in enumerate(enc.pairs):
    for (r, gi) in enc.slots:
        mu, p, q = enc.slot_rows(r, gi, pair); slots[r].append((pi_, mu, p, q))
P = len(enc.pairs)
cnt = [[0] * n for _ in range(P)]
reps = [rep(r) for r in range(len(enc.orbits))]
def contrib(r, c):
    return [(pi_, (mu * (c[p] - c[q])) % n) for (pi_, mu, p, q) in slots[r]]
cur = {r: contrib(r, reps[r]) for r in range(len(enc.orbits))}
for r in cur:
    for (pi_, w) in cur[r]: cnt[pi_][w] += 1
def cost(): return sum(max(0, x - 1) for row in cnt for x in row)
C = cost(); best = C; steps = 0; accepted = 0
dep = {}
for (r, x) in free:
    dep.setdefault((r, x), r)
found = None
while time.monotonic() - T_START < BUD:
    steps += 1
    (r, x) = free[rng.randrange(len(free))]
    old = vals[(r, x)]; new = rng.randrange(n)
    if new == old: continue
    vals[(r, x)] = new
    c2 = rep(r); con2 = contrib(r, c2)
    delta = 0
    for (pi_, w) in cur[r]:
        delta -= 1 if cnt[pi_][w] >= 2 else 0
        cnt[pi_][w] -= 1
    for (pi_, w) in con2:
        delta += 1 if cnt[pi_][w] >= 1 else 0
        cnt[pi_][w] += 1
    frac = (time.monotonic() - T_START) / BUD
    temp = T0 * (T1 / T0) ** frac
    if delta <= 0 or rng.random() < math.exp(-delta / temp):
        reps[r] = c2; cur[r] = con2; C += delta; accepted += 1
        if C < best: best = C
        if C == 0:
            found = [list(rep(rr)) for rr in range(len(enc.orbits))]; break
    else:
        for (pi_, w) in con2: cnt[pi_][w] -= 1
        for (pi_, w) in cur[r]: cnt[pi_][w] += 1
        vals[(r, x)] = old
out = {"status": "OK", "model": M.get("name"), "seed": seed, "steps": steps, "accepted": accepted, "best_cost": best,
       "final_cost": C, "found": found is not None, "wall_s": round(time.monotonic() - T_START, 3)}
if found:
    os.makedirs(outd, exist_ok=False)
    cols = enc.columns_from_reps([tuple(c) for c in found])
    rows = [[col[x] for col in cols] for x in range(k)]
    path = os.path.join(outd, 'sa_solution.raw')
    with open(path, 'x') as f: f.write("\n".join(" ".join(map(str, rr)) for rr in rows) + "\n")
    out["raw"] = path; out["raw_sha256"] = hashlib.sha256(open(path, 'rb').read()).hexdigest()
print(json.dumps(out, sort_keys=True))
