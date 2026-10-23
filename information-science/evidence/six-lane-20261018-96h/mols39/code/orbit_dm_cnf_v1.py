#!/usr/bin/env python3
"""orbit_dm_cnf_v1.py — orbit-representative CNF encoder / evaluator / decoder for G-invariant cyclic difference
matrices (ContinueCFR21, mols39 lane; written from definitions; stdlib only; frozen before execution).

OBJECT: a k x n array over Z_n whose column set C is invariant under a finite group G of pairs s = (mu, pi)
(perm[x] = pi(x)) acting EXACTLY on column vectors, (s.c)_x = mu * c_{pi^-1(x)}; DM: for all rows i<j the n values
c_i - c_j (c in C) are pairwise distinct.
MODEL: C is a disjoint union of G-orbits of prescribed types; type T = (stabiliser generators H_T, multiplicity m_T).
Each orbit r of type T has a representative c^r (one-hot coordinate variables X[r][x][v]) with s.c^r = c^r for every
generator s of H_T (exact equalities). The orbit is enumerated as {g.c^r : g in R_T}, R_T = left-coset representatives
of H_T in G (so |orbit| = |G|/|H_T| whenever Stab(c^r) = H_T; a larger stabiliser repeats a column, which the DM
constraints exclude automatically). Optional fixed coordinates (e.g. a zero row) and unit facts.
DM CONSTRAINTS only for one ordered representative (i,j) of every G-orbit of row pairs (the other pairs follow by
invariance): slot variables S[r][g][P][w] <-> mu_g (c^r_{pi_g^-1 i} - c^r_{pi_g^-1 j}) = w, and for every value w
exactly one slot (over all orbits r and coset representatives g) takes w. Count check: sum over orbits of |R_T| must
be n (else the model is rejected).
Every satisfying assignment decodes (union of the enumerated orbits) to a G-invariant DM; conversely every G-invariant
DM with the prescribed orbit-type multiplicities and representatives chosen with stabiliser exactly H_T satisfies it.
MODES: stats <model>; write <model> <out.cnf>; evaluate <model> <raw_dm>; decode <model> <solver_stdout> <out_raw>."""
import sys, json, hashlib, time, itertools
T, F = 'T', 'F'
def neg(l): return F if l == T else (T if l == F else -l)
def compose(n, a, b):            # (a o b): apply b then a
    mu = (a[0] * b[0]) % n; pa, pb = a[1], b[1]
    return (mu, tuple(pa[pb[x]] for x in range(len(pa))))
def gen_group(n, k, gens):
    e = (1, tuple(range(k))); G = {e}; frontier = [e]
    gens = [(g[0] % n, tuple(g[1])) for g in gens]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = compose(n, g, x)
                if y not in G: G.add(y); nf.append(y)
        frontier = nf
    return sorted(G)
def act(n, s, c):
    mu, perm = s; k = len(perm); pinv = [0] * k
    for x in range(k): pinv[perm[x]] = x
    return tuple((mu * c[pinv[x]]) % n for x in range(k))
class Enc:
    def __init__(self, M):
        self.M = M; n = self.n = M["n"]; k = self.k = M["k"]
        self.G = gen_group(n, k, M["gens"])
        self.types = []
        for t in M["orbit_types"]:
            H = gen_group(n, k, t["stab_gens"]) if t["stab_gens"] else [(1, tuple(range(k)))]
            Hs = set(H)
            if not Hs <= set(self.G): raise ValueError("stabiliser not in G")
            reps = []; covered = set()
            for g in self.G:          # left cosets gH
                if g in covered: continue
                reps.append(g)
                for h in H: covered.add(compose(n, g, h))
            self.types.append({"name": t["name"], "H": H, "Hgens": [(x[0] % n, tuple(x[1])) for x in t["stab_gens"]],
                               "mult": int(t["mult"]), "reps": reps, "fixed": {int(a): int(b) % n for a, b in t.get("fixed_coords", {}).items()}})
        tot = sum(len(t["reps"]) * t["mult"] for t in self.types)
        if tot != n: raise ValueError("orbit sizes sum to %d, not n" % tot)
        self.orbits = []
        for ti, t in enumerate(self.types):
            for m in range(t["mult"]): self.orbits.append(ti)
        # pair orbit representatives
        seen = set(); self.pairs = []
        for i in range(k):
            for j in range(i + 1, k):
                if (i, j) in seen: continue
                self.pairs.append((i, j))
                for g in self.G:
                    a, b = g[1][i], g[1][j]; seen.add((min(a, b), max(a, b)))
        # variable layout
        self.nX = len(self.orbits) * k * n
        self.slots = []
        for r, ti in enumerate(self.orbits):
            for gi, g in enumerate(self.types[ti]["reps"]): self.slots.append((r, gi))
        self.si = {s: i for i, s in enumerate(self.slots)}
        self.nS = len(self.slots) * len(self.pairs) * n
        self.nvars = self.nX + self.nS
        self.units = [tuple(u) for u in M.get("units", [])]     # [orbit_index, row, value]
    def X(self, r, x, v):
        fx = self.types[self.orbits[r]]["fixed"]
        if x in fx: return T if v % self.n == fx[x] else F
        return 1 + (r * self.k + x) * self.n + (v % self.n)
    def S(self, r, gi, pi_, w):
        return 1 + self.nX + ((self.si[(r, gi)] * len(self.pairs)) + pi_) * self.n + (w % self.n)
    def slot_rows(self, r, gi, pair):
        g = self.types[self.orbits[r]]["reps"][gi]; mu, perm = g; k = self.k
        pinv = [0] * k
        for x in range(k): pinv[perm[x]] = x
        return mu, pinv[pair[0]], pinv[pair[1]]
    def clauses(self):
        n, k = self.n, self.k
        for r in range(len(self.orbits)):
            for x in range(k):
                lits = [self.X(r, x, v) for v in range(n)]
                if T in lits: continue
                lits2 = [l for l in lits if l != F]
                yield 'onehot', lits2
                for a in range(len(lits2)):
                    for b in range(a + 1, len(lits2)): yield 'onehot', [-lits2[a], -lits2[b]]
            t = self.types[self.orbits[r]]
            for s in t["Hgens"]:            # stabiliser: (s.c)_x = c_x, i.e. mu c_{pinv x} = c_x
                mu, perm = s; pinv = [0] * k
                for x in range(k): pinv[perm[x]] = x
                for x in range(k):
                    for v in range(n):
                        yield 'stab', [neg(self.X(r, pinv[x], v)), self.X(r, x, (mu * v) % n)]
        for pi_, pair in enumerate(self.pairs):
            for (r, gi) in self.slots:
                mu, p, q = self.slot_rows(r, gi, pair)
                muinv = pow(mu, -1, n)
                for w in range(n):
                    s = self.S(r, gi, pi_, w); w2 = (muinv * w) % n
                    for v in range(n):
                        xp = self.X(r, p, v); xq = self.X(r, q, v - w2)
                        yield 'sdef', [neg(xp), neg(xq), s]
                        yield 'sdef', [-s, neg(xp), xq]
            for w in range(n):
                lits = [self.S(r, gi, pi_, w) for (r, gi) in self.slots]
                yield 'dm', lits
                for a in range(len(lits)):
                    for b in range(a + 1, len(lits)): yield 'dm', [-lits[a], -lits[b]]
        for (r, x, v) in self.units: yield 'unit', [self.X(r, x, v)]
    def simplified(self):
        for tag, lits in self.clauses():
            if T in lits: continue
            yield tag, [l for l in lits if l != F]
    def columns_from_reps(self, reps):
        cols = []
        for r, ti in enumerate(self.orbits):
            for g in self.types[ti]["reps"]: cols.append(act(self.n, g, reps[r]))
        return cols
def main():
    mode = sys.argv[1]; raw = open(sys.argv[2], 'rb').read(); M = json.loads(raw); enc = Enc(M); n, k = enc.n, enc.k
    out = {"mode": mode, "model": M.get("name"), "model_sha256": hashlib.sha256(raw).hexdigest(), "n": n, "k": k,
           "group_order": len(enc.G), "orbits": len(enc.orbits), "pair_reps": enc.pairs, "nvars": enc.nvars}
    t0 = time.monotonic()
    if mode == 'stats':
        cnt = {}; lits = 0; empty = 0
        for tag, cl in enc.simplified():
            cnt[tag] = cnt.get(tag, 0) + 1; lits += len(cl); empty += (not cl)
        out.update({"clauses_by_tag": cnt, "clauses": sum(cnt.values()), "literals": lits, "empty_clauses": empty})
    elif mode == 'write':
        path = sys.argv[3]; nc = sum(1 for _ in enc.simplified()); h = hashlib.sha256(); size = 0
        with open(path, 'x') as f:
            hdr = "p cnf %d %d\n" % (enc.nvars, nc); f.write(hdr); h.update(hdr.encode()); size += len(hdr); buf = []
            for tag, cl in enc.simplified():
                buf.append(" ".join(map(str, cl)) + " 0\n")
                if len(buf) >= 100000:
                    ch = "".join(buf); f.write(ch); h.update(ch.encode()); size += len(ch); buf = []
            ch = "".join(buf); f.write(ch); h.update(ch.encode()); size += len(ch)
        out.update({"cnf": path, "clauses": nc, "bytes": size, "cnf_sha256": h.hexdigest()})
    elif mode == 'evaluate':
        rb = open(sys.argv[3], 'rb').read(); out["dm_sha256"] = hashlib.sha256(rb).hexdigest()
        rows = [[int(t) % n for t in ln.split()] for ln in rb.decode().splitlines() if ln.strip()]
        cols = set(tuple(r[c] for r in rows) for c in range(len(rows[0])))
        # orbit decomposition and representative choice with stabiliser exactly H_T
        remaining = set(cols); reps = [None] * len(enc.orbits); used = [0] * len(enc.types); err = None
        while remaining and err is None:
            c = min(remaining); orb = {act(n, g, c) for g in enc.G}
            if not orb <= remaining: err = "orbit not contained in column set"; break
            remaining -= orb; placed = False
            for ti, t in enumerate(enc.types):
                if len(t["reps"]) != len(orb) or used[ti] >= t["mult"]: continue
                cand = [d for d in sorted(orb) if all(act(n, h, d) == d for h in t["H"]) and all(d[x] == v for x, v in t["fixed"].items())]
                if not cand: continue
                idx = [r for r, tt in enumerate(enc.orbits) if tt == ti][used[ti]]
                reps[idx] = cand[0]; used[ti] += 1; placed = True; break
            if not placed: err = "no orbit type for orbit of size %d" % len(orb)
        if err or any(r is None for r in reps):
            out["error"] = err or "orbit type multiplicities do not match"; print(json.dumps(out)); return 2
        truth = bytearray(enc.nvars + 1)
        for r in range(len(enc.orbits)):
            for x in range(k):
                l = enc.X(r, x, reps[r][x])
                if l not in (T, F): truth[l] = 1
        for pi_, pair in enumerate(enc.pairs):
            for (r, gi) in enc.slots:
                mu, p, q = enc.slot_rows(r, gi, pair)
                truth[enc.S(r, gi, pi_, (mu * (reps[r][p] - reps[r][q])) % n)] = 1
        bad = {}; total = 0
        for tag, cl in enc.simplified():
            total += 1
            if not any((l > 0 and truth[l]) or (l < 0 and not truth[-l]) for l in cl): bad[tag] = bad.get(tag, 0) + 1
        out.update({"clauses": total, "violated_by_tag": bad, "verdict": "SATISFIES_ALL" if not bad else "VIOLATES",
                    "reps": [list(r) for r in reps]})
    elif mode == 'decode':
        txt = open(sys.argv[3], 'rb').read(); out["solver_stdout_sha256"] = hashlib.sha256(txt).hexdigest(); pos = set()
        for ln in txt.decode(errors='replace').splitlines():
            if ln.startswith('v '):
                for tk in ln.split()[1:]:
                    x = int(tk)
                    if x > 0: pos.add(x)
        reps = []; ok = True
        for r in range(len(enc.orbits)):
            c = []
            for x in range(k):
                vs = [v for v in range(n) if (lambda l: l == T or (l not in (T, F) and l in pos))(enc.X(r, x, v))]
                if len(vs) != 1: ok = False
                c.append(vs[0] if vs else 0)
            reps.append(tuple(c))
        cols = enc.columns_from_reps(reps)
        rows = [[c[x] for c in cols] for x in range(k)]
        path = sys.argv[4]
        with open(path, 'x') as f: f.write("\n".join(" ".join(map(str, r)) for r in rows) + "\n")
        out.update({"onehot_ok": ok, "raw": path, "raw_sha256": hashlib.sha256(open(path, 'rb').read()).hexdigest(), "reps": [list(r) for r in reps]})
    out["wall_s"] = round(time.monotonic() - t0, 3)
    print(json.dumps(out, sort_keys=True))
    return 0
if __name__ == '__main__':
    sys.exit(main())
