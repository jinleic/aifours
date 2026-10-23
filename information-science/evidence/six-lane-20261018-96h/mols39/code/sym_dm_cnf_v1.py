#!/usr/bin/env python3
"""sym_dm_cnf_v1.py — symmetric cyclic difference-matrix CNF encoder / evaluator / decoder
(ContinueCFR21, mols39 lane; written from definitions; stdlib only; frozen before any execution).

OBJECT. A k x n array D over Z_n is a (Z_n,k;1) difference matrix (DM) if for all rows i<j the n values
D_i(c) - D_j(c) (c over the n columns) are pairwise distinct. A model fixes a group G of pairs s = (mu, pi)
(mu a unit of Z_n, pi a permutation of the rows, perm[x] = pi(x)) acting EXACTLY on column vectors by
(s.c)_x = mu * c_{pi^-1(x)}, and asks for a DM whose column set is G-invariant.
Optional zero row z: a row fixed by every pi and equal to 0 in every column (any DM with a row r fixed by every
pi can be normalised so: subtract row r column-wise; this commutes with the action because (s.c)_r = mu c_r).
LABELLING. Columns are labelled by u = D_a(c) - D_b(c) for a chosen row pair (a, b) (a bijection C -> Z_n by
the DM property). Every row is represented affinely in u: D_x(u) = base_x(u) + coef_x * u with
  zero row: base none, coef 0;  label row a when b = z: base none, coef 1;
  derived row b when b != z: D_b(u) = D_a(u) - u (base a, coef -1);  all other rows: base x, coef 0 (variable).
VARIABLES. R[x][u][v] <-> D_x(u) = v for variable rows x; E[p,q][u][w] <-> D_p(u) - D_q(u) = w for every pair of
distinct variable rows p<q (auxiliary).
CLAUSES (each tagged):
  onehot    : each variable row x and label u takes exactly one value (ALO + pairwise AMO);
  edef      : E[p,q][u][w] <-> OR_v (R[p][u][v] & R[q][u][v-w]) (two implications per (u,w,v), sound under onehot);
  dm        : for every pair i<j and value w, exactly one label u has D_i(u) - D_j(u) = w (ALO + pairwise AMO);
  transport : for every generator s=(mu,pi), labels u,u', row x, value v:
              [label of s.c(u) is u'] & [D_{pi^-1 x}(u) = v]  ->  [D_x(u') = mu v],
              where label of s.c(u) = mu * (D_{pi^-1 a}(u) - D_{pi^-1 b}(u));
  unit      : optional model facts D_x(u) = v (gauge or anchoring; each must be justified in the model notes).
Soundness/completeness: a 0/1 assignment satisfies all clauses iff it encodes (via the labelling) a G-invariant DM
with the given zero row / label pair and the unit facts (invariance under generators implies invariance under G).
MODES
  stats <model.json>                                   count variables/clauses (no output file)
  write <model.json> <out.cnf>                         DIMACS (exclusive create), two passes
  evaluate <model.json> <raw_dm_file>                  map a known DM into the model assignment, check every clause
  decode <model.json> <solver_stdout> <out_raw>        solver 'v' lines -> raw k x n DM (exclusive create)
All modes print one JSON object."""
import sys, json, hashlib, time, os
T, F = 'T', 'F'
def neg(l):
    if l == T: return F
    if l == F: return T
    return -l
class Enc:
    def __init__(self, M):
        self.M = M
        self.n = n = M["n"]; self.k = k = M["k"]; self.z = z = M.get("zero_row")
        a, b = M["label"]; self.a, self.b = a, b
        if a == b or a == z: raise ValueError("bad label pair")
        self.gens = [(g[0] % n, list(g[1])) for g in M["gens"]]
        for mu, perm in self.gens:
            if sorted(perm) != list(range(k)): raise ValueError("bad perm")
            if z is not None and perm[z] != z: raise ValueError("zero row not fixed")
            if pow(mu, -1, n) is None: raise ValueError("mu not unit")
        self.base = {}; self.coef = {}
        for x in range(k):
            if x == z: self.base[x], self.coef[x] = None, 0
            elif x == a and b == z: self.base[x], self.coef[x] = None, 1
            elif x == b and b != z: self.base[x], self.coef[x] = a, -1
            else: self.base[x], self.coef[x] = x, 0
        if b != z and self.base[a] != a: raise ValueError("label row a must be variable when b is not the zero row")
        self.varrows = sorted(x for x in range(k) if self.base[x] == x)
        self.vi = {x: i for i, x in enumerate(self.varrows)}
        self.auxpairs = [(p, q) for i, p in enumerate(self.varrows) for q in self.varrows[i + 1:]]
        self.pi_ = {pq: i for i, pq in enumerate(self.auxpairs)}
        self.NR = len(self.varrows) * n * n
        self.NE = len(self.auxpairs) * n * n
        self.nvars = self.NR + self.NE
        self.units = [tuple(t) for t in M.get("units", [])]
    def R(self, x, u, v):
        n = self.n; return 1 + (self.vi[x] * n + u) * n + (v % n)
    def E(self, pq, u, w):
        n = self.n; return 1 + self.NR + (self.pi_[pq] * n + u) * n + (w % n)
    def L(self, x, u, v):
        n = self.n; bx = self.base[x]; c = self.coef[x]
        if bx is None: return T if (v - c * u) % n == 0 else F
        return self.R(bx, u, (v - c * u) % n)
    def dlit(self, i, j, u, w):
        n = self.n; bi, bj = self.base[i], self.base[j]
        w2 = (w - (self.coef[i] - self.coef[j]) * u) % n
        if bi is None and bj is None: return T if w2 == 0 else F
        if bj is None: return self.R(bi, u, w2)
        if bi is None: return self.R(bj, u, -w2)
        if bi == bj: return T if w2 == 0 else F
        if bi < bj: return self.E((bi, bj), u, w2)
        return self.E((bj, bi), u, -w2)
    def clauses(self):
        n, k = self.n, self.k
        # onehot
        for x in self.varrows:
            for u in range(n):
                lits = [self.R(x, u, v) for v in range(n)]
                yield 'onehot', lits
                for i in range(n):
                    for j in range(i + 1, n): yield 'onehot', [-lits[i], -lits[j]]
        # edef
        for (p, q) in self.auxpairs:
            for u in range(n):
                for w in range(n):
                    e = self.E((p, q), u, w)
                    for v in range(n):
                        rp = self.R(p, u, v); rq = self.R(q, u, v - w)
                        yield 'edef', [-rp, -rq, e]
                        yield 'edef', [-e, -rp, rq]
        # dm
        for i in range(k):
            for j in range(i + 1, k):
                bi, bj = self.base[i], self.base[j]
                if (bi is None and bj is None) or (bi is not None and bi == bj):
                    from math import gcd
                    if gcd((self.coef[i] - self.coef[j]) % n, n) != 1: yield 'dm', []
                    continue
                for w in range(n):
                    lits = [self.dlit(i, j, u, w) for u in range(n)]
                    yield 'dm', lits
                    for s in range(n):
                        for t in range(s + 1, n): yield 'dm', [neg(lits[s]), neg(lits[t])]
        # transport
        for mu, perm in self.gens:
            pinv = [0] * k
            for x in range(k): pinv[perm[x]] = x
            muinv = pow(mu, -1, n)
            for u in range(n):
                for u2 in range(n):
                    P = self.dlit(pinv[self.a], pinv[self.b], u, (muinv * u2) % n)
                    if P == F: continue
                    for x in range(k):
                        for v in range(n):
                            l1 = self.L(pinv[x], u, v)
                            if l1 == F: continue
                            yield 'transport', [neg(P), neg(l1), self.L(x, u2, (mu * v) % n)]
        for (x, u, v) in self.units:
            yield 'unit', [self.L(x, u, v)]
    def simplified(self):
        for tag, lits in self.clauses():
            if T in lits: continue
            yield tag, [l for l in lits if l != F]
def load(path):
    raw = open(path, 'rb').read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()
def main():
    mode = sys.argv[1]; M, msha = load(sys.argv[2]); enc = Enc(M); n, k = enc.n, enc.k
    out = {"mode": mode, "model": M.get("name"), "model_sha256": msha, "n": n, "k": k, "nvars": enc.nvars,
           "varrows": enc.varrows, "auxpairs": len(enc.auxpairs)}
    t0 = time.monotonic()
    if mode == 'stats':
        cnt = {}; empty = 0; lits = 0
        for tag, cl in enc.simplified():
            cnt[tag] = cnt.get(tag, 0) + 1; lits += len(cl)
            if not cl: empty += 1
        out.update({"clauses_by_tag": cnt, "clauses": sum(cnt.values()), "literals": lits, "empty_clauses": empty})
    elif mode == 'write':
        path = sys.argv[3]; nc = 0
        for _ in enc.simplified(): nc += 1
        h = hashlib.sha256(); size = 0
        with open(path, 'x') as f:
            hdr = "p cnf %d %d\n" % (enc.nvars, nc); f.write(hdr); h.update(hdr.encode()); size += len(hdr)
            buf = []
            for tag, cl in enc.simplified():
                s = " ".join(map(str, cl)) + " 0\n"; buf.append(s)
                if len(buf) >= 100000:
                    chunk = "".join(buf); f.write(chunk); h.update(chunk.encode()); size += len(chunk); buf = []
            chunk = "".join(buf); f.write(chunk); h.update(chunk.encode()); size += len(chunk)
        out.update({"cnf": path, "clauses": nc, "bytes": size, "cnf_sha256": h.hexdigest()})
    elif mode == 'evaluate':
        rawb = open(sys.argv[3], 'rb').read(); out["dm_sha256"] = hashlib.sha256(rawb).hexdigest()
        rows = [[int(t) % n for t in ln.split()] for ln in rawb.decode().splitlines() if ln.strip()]
        if len(rows) != k or any(len(r) != n for r in rows): out["error"] = "shape"; print(json.dumps(out)); return 2
        if enc.z is not None:
            rows = [[(rows[x][c] - rows[enc.z][c]) % n for c in range(n)] for x in range(k)]
        lab = [(rows[enc.a][c] - rows[enc.b][c]) % n for c in range(n)]
        if sorted(lab) != list(range(n)): out["error"] = "label_not_bijective"; print(json.dumps(out)); return 2
        col = {lab[c]: c for c in range(n)}
        val = {x: [rows[x][col[u]] for u in range(n)] for x in range(k)}
        # affine rows must match their representation
        aff_ok = all((val[x][u] - (val[enc.base[x]][u] if enc.base[x] is not None else 0) - enc.coef[x] * u) % n == 0
                     for x in range(k) for u in range(n))
        out["affine_consistent"] = aff_ok
        truth = bytearray(enc.nvars + 1)
        for x in enc.varrows:
            for u in range(n): truth[enc.R(x, u, val[x][u])] = 1
        for (p, q) in enc.auxpairs:
            for u in range(n): truth[enc.E((p, q), u, (val[p][u] - val[q][u]) % n)] = 1
        bad = {}; examples = []; total = 0
        for tag, cl in enc.simplified():
            total += 1
            if not any((l > 0 and truth[l]) or (l < 0 and not truth[-l]) for l in cl):
                bad[tag] = bad.get(tag, 0) + 1
                if len(examples) < 5: examples.append([tag, cl[:8]])
        out.update({"clauses": total, "violated_by_tag": bad, "violated": sum(bad.values()), "examples": examples,
                    "verdict": "SATISFIES_ALL" if not bad and aff_ok else "VIOLATES"})
    elif mode == 'decode':
        txt = open(sys.argv[3], 'rb').read(); out["solver_stdout_sha256"] = hashlib.sha256(txt).hexdigest()
        pos = set()
        for ln in txt.decode(errors='replace').splitlines():
            if ln.startswith('v '):
                for t in ln.split()[1:]:
                    x = int(t)
                    if x > 0: pos.add(x)
        val = {}
        ok = True
        for x in enc.varrows:
            val[x] = []
            for u in range(n):
                vs = [v for v in range(n) if enc.R(x, u, v) in pos]
                if len(vs) != 1: ok = False; vs = vs[:1] or [0]
                val[x].append(vs[0])
        rows = []
        for x in range(k):
            bx = enc.base[x]
            rows.append([((val[bx][u] if bx is not None else 0) + enc.coef[x] * u) % n for u in range(n)])
        out["onehot_ok"] = ok
        path = sys.argv[4]
        with open(path, 'x') as f: f.write("\n".join(" ".join(map(str, r)) for r in rows) + "\n")
        out["raw"] = path; out["raw_sha256"] = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    out["wall_s"] = round(time.monotonic() - t0, 3)
    print(json.dumps(out, sort_keys=True))
    return 0
if __name__ == '__main__':
    sys.exit(main())
