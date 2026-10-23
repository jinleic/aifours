#!/usr/bin/env python3
"""ext_search_beta_v1.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib only;
single process, no threads, no subprocess).

Beta-route producer for the one-row extension problem of evidence/ext-search-spec-v1.md (problem section 2,
chunks section 3, CLI section 4, output section 5). Scope: evidence/scope-note-beta-route-search-v1.md.
For n = 3q with q % 3 != 0, write f = CRT(h, g) with g = f mod q and h = f mod 3, and b = D mod q, a = D mod 3. By the
CRT, D_x - f is a bijection of Z_n iff
  (S1) every b_x - g is 3-to-1 onto Z_q, and
  (S2) on each of its fibres T_x(t) = {c : b_x(c) - g(c) = t (mod q)} the three values a_x(c) - h(c) are distinct.
Stage 1 enumerates every g with g[0] = 0 and the chunk's values on the split columns, satisfying (S1). It is a
multiplicity exact cover: items (x, t) have demand 3, each column chooses one value, and option (c, w) hits
(x, b_x(c) - w) for every row x. Counters are incremental: remaining demand, a block count per option (saturated
items it hits), feasible-option supply per item and feasible-value count per column. The search branches on the
unassigned column with the fewest feasible values (smallest index on ties), trying values in increasing order. It
prunes when an item's supply is below its remaining demand or a column has no feasible value.
Stage 2 enumerates, for each stage-1 g, every h with h[0] = 0 and the chunk's values, satisfying (S2). (S2) is the
set of binary constraints h[c] - h[c'] != a_x(c) - a_x(c') (mod 3) for each pair in each fibre. Stage 2 is a
depth-first search with forward checking: smallest domain first, smallest index on ties, values in increasing
order.
Every f = CRT(h, g) is re-checked directly against section 2 before it is reported.
Each solution is found exactly once: the stage-1 search assigns each column once, so leaves are distinct; stage 2
likewise; and CRT is a bijection. Completeness: pruning removes only states with no completion. A column with no
feasible value, or an item whose supply is below its demand, cannot be completed, because every remaining hit of an
item comes from a distinct unassigned column through its unique value for that item."""
import sys, os, json, math, time, random, hashlib

RAW_CAP = 1 << 20
MAX_BUDGET_S = 10000.0
PROGRAM = "ext_search_beta_v1"
EXIT = {"COMPLETE": 0, "ESTIMATE": 0, "STOPPED_AT_SOLUTIONS": 1, "INCOMPLETE_BUDGET": 5, "BAD_INPUT": 2,
        "INPUT_PIN_MISMATCH": 2, "IO_ERROR": 2, "NOT_DM": 3, "INTERNAL_ERROR": 4}
KEYS = ("status", "reason", "program", "n", "q", "k", "m", "chunk_lo", "chunk_hi", "mode", "chunks", "solutions",
        "solutions_sha256", "input_sha256", "program_sha256", "extra", "wall_s")
FLAGS = ("--raw", "--raw-sha256", "--m", "--chunk-lo", "--chunk-hi", "--max-solutions", "--budget-s", "--mode",
         "--probes", "--seed")
REQUIRED = FLAGS[:7]


class Stop(Exception):
    def __init__(self, status, reason):
        super().__init__(reason)
        self.status, self.reason = status, reason


class OutOfTime(Exception):
    pass


class EnoughSolutions(Exception):
    pass


def parse_g1(raw):
    lines = raw.split(b"\n")
    if lines[-1] == b"":
        lines.pop()
    rows = []
    for line in lines:
        tokens = line.split()
        if not tokens:
            raise Stop("BAD_INPUT", "G1: a line has no token")
        row = []
        for tok in tokens:
            digits = tok[1:] if tok[:1] in (b"+", b"-") else tok
            if not digits.isdigit():
                raise Stop("BAD_INPUT", "G1: a token is not a decimal integer")
            try:
                row.append(int(tok))
            except ValueError:
                raise Stop("BAD_INPUT", "G1: integer too long") from None
        rows.append(row)
    return rows


def parse_int(text, name):
    if not (text.isdigit() and text.isascii()):
        raise Stop("BAD_INPUT", name + " is not a non-negative decimal integer")
    return int(text)


def parse_args(argv):
    got = {}
    if len(argv) % 2:
        raise Stop("BAD_INPUT", "arguments must be --flag value pairs")
    for i in range(0, len(argv), 2):
        flag, value = argv[i], argv[i + 1]
        if flag not in FLAGS or flag in got:
            raise Stop("BAD_INPUT", "unknown or repeated flag")
        got[flag] = value
    for flag in REQUIRED:
        if flag not in got:
            raise Stop("BAD_INPUT", "missing " + flag)
    a = {"raw": got["--raw"], "pin": got["--raw-sha256"], "m": parse_int(got["--m"], "--m"),
         "lo": parse_int(got["--chunk-lo"], "--chunk-lo"), "hi": parse_int(got["--chunk-hi"], "--chunk-hi"),
         "K": parse_int(got["--max-solutions"], "--max-solutions"), "mode": got.get("--mode", "search")}
    try:
        a["S"] = float(got["--budget-s"])
    except ValueError:
        raise Stop("BAD_INPUT", "--budget-s is not a number") from None
    if not (math.isfinite(a["S"]) and 0.0 < a["S"] <= MAX_BUDGET_S):
        raise Stop("BAD_INPUT", "--budget-s must be finite with 0 < S <= 10000")
    if a["mode"] not in ("search", "estimate"):
        raise Stop("BAD_INPUT", "--mode must be search or estimate")
    if a["mode"] == "estimate":
        if "--probes" not in got or "--seed" not in got:
            raise Stop("BAD_INPUT", "estimate mode needs --probes and --seed")
        a["P"] = parse_int(got["--probes"], "--probes")
        a["seed"] = parse_int(got["--seed"], "--seed")
        if a["P"] < 1:
            raise Stop("BAD_INPUT", "--probes must be >= 1")
    elif "--probes" in got or "--seed" in got:
        raise Stop("BAD_INPUT", "--probes and --seed are only for estimate mode")
    return a


def write_new(name, data):
    fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    try:
        view = memoryview(data)
        while view:
            view = view[os.write(fd, view):]
    finally:
        os.close(fd)


class Beta:
    """Stage 1 and stage 2 for one input; one instance per chunk (fresh state)."""

    def __init__(self, D, n, q, deadline, counter):
        self.D, self.n, self.q, self.k = D, n, q, len(D)
        self.deadline, self.counter = deadline, counter
        k = self.k
        self.b = [[v % q for v in row] for row in D]
        self.a = [[v % 3 for v in row] for row in D]
        self.cols = list(range(1, n))
        # options: oid = c * q + w for c in 1..n-1
        self.opt_items = [None] * (n * q)
        self.item_opts = [[] for _ in range(k * q)]
        for c in self.cols:
            for w in range(q):
                its = [x * q + (self.b[x][c] - w) % q for x in range(k)]
                oid = c * q + w
                self.opt_items[oid] = its
                for i in its:
                    self.item_opts[i].append(oid)
        self.dem = [3] * (k * q)
        for x in range(k):
            self.dem[x * q + self.b[x][0] % q] -= 1            # column 0 fixed: g[0] = 0
        self.blocks = [0] * (n * q)
        self.assigned = [-1] * n
        self.assigned[0] = 0
        self.supply = [len(self.item_opts[i]) for i in range(k * q)]
        self.colfeas = [0] + [q] * (n - 1)
        for i in range(k * q):                                 # items already saturated at the start
            if self.dem[i] == 0:
                self.saturate(i)
            elif self.dem[i] < 0:
                raise Stop("INTERNAL_ERROR", "negative initial demand")

    def tick(self):
        self.counter[0] += 1
        if (self.counter[0] & 1023) == 0 and time.monotonic() > self.deadline:
            raise OutOfTime()

    def feasible(self, oid):
        return self.assigned[oid // self.q] < 0 and self.blocks[oid] == 0

    def saturate(self, i):
        q = self.q
        for oid in self.item_opts[i]:
            self.blocks[oid] += 1
            if self.blocks[oid] == 1 and self.assigned[oid // q] < 0:
                for j in self.opt_items[oid]:
                    self.supply[j] -= 1
                self.colfeas[oid // q] -= 1

    def unsaturate(self, i):
        q = self.q
        for oid in self.item_opts[i]:
            self.blocks[oid] -= 1
            if self.blocks[oid] == 0 and self.assigned[oid // q] < 0:
                for j in self.opt_items[oid]:
                    self.supply[j] += 1
                self.colfeas[oid // q] += 1

    def assign(self, c, w):
        q = self.q
        saved = self.colfeas[c]
        for w2 in range(q):
            oid = c * q + w2
            if self.blocks[oid] == 0:
                for j in self.opt_items[oid]:
                    self.supply[j] -= 1
        self.assigned[c] = w
        self.colfeas[c] = 0
        for j in self.opt_items[c * q + w]:
            self.dem[j] -= 1
            if self.dem[j] == 0:
                self.saturate(j)
        return saved

    def unassign(self, c, w, saved):
        q = self.q
        for j in reversed(self.opt_items[c * q + w]):
            if self.dem[j] == 0:
                self.unsaturate(j)
            self.dem[j] += 1
        self.assigned[c] = -1
        for w2 in range(q):
            oid = c * q + w2
            if self.blocks[oid] == 0:
                for j in self.opt_items[oid]:
                    self.supply[j] += 1
        self.colfeas[c] = saved

    def dead(self):
        for i, d in enumerate(self.dem):
            if d > self.supply[i] or d < 0:
                return True
        for c in self.cols:
            if self.assigned[c] < 0 and self.colfeas[c] == 0:
                return True
        return False

    def pick(self):
        best, bc = -1, None
        for c in self.cols:
            if self.assigned[c] < 0:
                cf = self.colfeas[c]
                if bc is None or cf < bc:
                    best, bc = c, cf
        return best

    def values(self, c):
        return [w for w in range(self.q) if self.blocks[c * self.q + w] == 0]

    def stage1(self, on_leaf):
        self.tick()
        if self.dead():
            return
        c = self.pick()
        if c < 0:
            if any(self.dem):
                raise Stop("INTERNAL_ERROR", "complete stage-1 assignment with residual demand")
            on_leaf([self.assigned[cc] for cc in range(self.n)])
            return
        for w in self.values(c):
            saved = self.assign(c, w)
            try:
                self.stage1(on_leaf)
            finally:
                self.unassign(c, w, saved)

    def stage2(self, g, fixed_h, on_solution, stats):
        """All h with the fixed values, satisfying (S2) for this g."""
        n, q, k = self.n, self.q, self.k
        nbrs = [[] for _ in range(n)]
        for x in range(k):
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[(self.b[x][c] - g[c]) % q].append(c)
            for t in range(q):
                T = buckets[t]
                if len(T) != 3:
                    raise Stop("INTERNAL_ERROR", "stage-1 leaf with a fibre of size != 3")
                for i1 in range(3):
                    for i2 in range(3):
                        if i1 != i2:
                            c1, c2 = T[i1], T[i2]
                            nbrs[c1].append((c2, (self.a[x][c1] - self.a[x][c2]) % 3))
        dom = [7] * n
        for c, v in fixed_h.items():
            dom[c] = 1 << v
        h = [-1] * n

        def forward(c, v, changed):
            for (c2, d) in nbrs[c]:
                if h[c2] < 0:
                    bad = 1 << ((v - d) % 3)                 # h[c] - h[c2] != d  <=>  h[c2] != v - d
                    if dom[c2] & bad:
                        dom[c2] &= ~bad
                        changed.append((c2, bad))
                        if dom[c2] == 0:
                            return False
            return True

        def dfs():
            self.tick()
            stats[0] += 1
            best, bsize = -1, 4
            for c in range(n):
                if h[c] < 0:
                    s = bin(dom[c]).count("1")
                    if s < bsize:
                        best, bsize = c, s
            if best < 0:
                on_solution(list(h))
                return
            for v in range(3):
                if not (dom[best] >> v) & 1:
                    continue
                h[best] = v
                changed = []
                if forward(best, v, changed):
                    dfs()
                for (c2, bit) in changed:
                    dom[c2] |= bit
                h[best] = -1
        dfs()


def crt(h, g, n, q):
    for y in range(n):
        if y % 3 == h and y % q == g:
            return y
    raise Stop("INTERNAL_ERROR", "CRT failed")


def is_extension(D, f, n):
    return f[0] == 0 and all(len({(row[c] - f[c]) % n for c in range(n)}) == n for row in D)


def chunk_values(idx, m, n):
    vals = []
    for _ in range(m):
        vals.append(idx % n)
        idx //= n
    vals.reverse()
    return vals                                            # v_1 most significant


def run(a, t0, out):
    try:
        with open(a["raw"], "rb") as fh:
            raw = fh.read(RAW_CAP + 1)
    except OSError as exc:
        raise Stop("IO_ERROR", "cannot read raw: " + type(exc).__name__) from None
    if len(raw) > RAW_CAP:
        raise Stop("BAD_INPUT", "raw exceeds 1 MiB")
    out["input_sha256"] = hashlib.sha256(raw).hexdigest()
    if out["input_sha256"] != a["pin"]:
        raise Stop("INPUT_PIN_MISMATCH", "raw sha256 differs from --raw-sha256")
    rows = parse_g1(raw)
    k = len(rows)
    n = len(rows[0]) if rows else 0
    if not (2 <= k <= 12) or any(len(r) != n for r in rows) or n > 120 or n % 3 or (n // 3) < 2 or (n // 3) % 3 == 0:
        raise Stop("BAD_INPUT", "need 2 <= k <= 12 rows of one length n = 3q, q >= 2, q % 3 != 0, n <= 120")
    q = n // 3
    m, lo, hi = a["m"], a["lo"], a["hi"]
    if not (m <= 3 and m <= n - 1 and lo < hi <= n ** m):
        raise Stop("BAD_INPUT", "chunk parameters out of range")
    out.update({"n": n, "q": q, "k": k, "m": m, "chunk_lo": lo, "chunk_hi": hi, "mode": a["mode"]})
    D = [[v % n for v in r] for r in rows]
    for x in range(k):
        for y in range(x + 1, k):
            if len({(D[x][c] - D[y][c]) % n for c in range(n)}) != n:
                raise Stop("NOT_DM", "rows %d, %d" % (x, y))
    deadline = t0 + a["S"]
    counter = [0]
    stats = {"stage1_solutions": 0, "stage2_nodes": 0}
    sols = []
    chunks = []
    try:
        for idx in range(lo, hi):
            if time.monotonic() > deadline:
                raise OutOfTime()
            vals = chunk_values(idx, m, n)
            entry = {"chunk": idx, "status": "NOT_COMPLETE", "nodes": 0}
            chunks.append(entry)
            start = counter[0]
            eng = Beta(D, n, q, deadline, counter)
            ok = True
            saves = []
            for i, v in enumerate(vals, start=1):
                w = v % q
                if not eng.feasible(i * q + w):
                    ok = False
                    break
                saves.append((i, w, eng.assign(i, w)))
            fixed_h = {0: 0}
            for i, v in enumerate(vals, start=1):
                fixed_h[i] = v % 3
            if a["mode"] == "estimate":
                rng = random.Random(a["seed"] * 1000003 + idx)
                total = 0.0
                for _ in range(a["P"]):
                    est, weight = 1.0, 1.0
                    path = []
                    if ok:
                        while True:
                            eng.tick()
                            if eng.dead():
                                break
                            c = eng.pick()
                            if c < 0:
                                break
                            vs = eng.values(c)
                            weight *= len(vs)
                            est += weight
                            w = vs[rng.randrange(len(vs))]
                            path.append((c, w, eng.assign(c, w)))
                        for (c, w, sv) in reversed(path):
                            eng.unassign(c, w, sv)
                    total += est
                entry.update({"status": "ESTIMATE", "estimate": total / a["P"], "probes": a["P"]})
                del entry["solutions"] if "solutions" in entry else None
                entry["nodes"] = counter[0] - start
                continue
            found = []
            if ok:
                def on_leaf(g):
                    stats["stage1_solutions"] += 1
                    st = [0]

                    def on_solution(h):
                        f = [crt(h[c], g[c], n, q) for c in range(n)]
                        if not is_extension(D, f, n) or [f[i] for i in range(1, m + 1)] != vals:
                            raise Stop("INTERNAL_ERROR", "a reported f fails the direct re-check")
                        found.append(f)
                        sols.append(f)
                        if a["K"] and len(sols) >= a["K"]:
                            raise EnoughSolutions()
                    try:
                        eng.stage2(g, fixed_h, on_solution, st)
                    finally:
                        stats["stage2_nodes"] += st[0]
                eng.stage1(on_leaf)
            entry.update({"status": "COMPLETE", "solutions": len(found)})
            entry["nodes"] = counter[0] - start
        status = "ESTIMATE" if a["mode"] == "estimate" else "COMPLETE"
    except OutOfTime:
        status = "INCOMPLETE_BUDGET"
    except EnoughSolutions:
        status = "STOPPED_AT_SOLUTIONS"
    for entry in chunks:
        if entry["status"] == "NOT_COMPLETE":
            entry["solutions"] = sum(1 for f in sols if chunk_values(entry["chunk"], m, n) == f[1:m + 1])
    if status in ("INCOMPLETE_BUDGET", "STOPPED_AT_SOLUTIONS"):
        last = chunks[-1] if chunks else None
        if last is not None and status == "STOPPED_AT_SOLUTIONS":
            last["status"] = "NOT_COMPLETE"
            last["solutions"] = sum(1 for f in sols if chunk_values(last["chunk"], m, n) == f[1:m + 1])
            last["nodes"] = counter[0] - sum(e["nodes"] for e in chunks[:-1])
        elif last is not None and last["status"] == "NOT_COMPLETE":
            last["nodes"] = counter[0] - sum(e["nodes"] for e in chunks[:-1])
    sols.sort()
    out["chunks"] = chunks
    out["solutions"] = sols
    out["solutions_sha256"] = hashlib.sha256(json.dumps(sols, separators=(",", ":")).encode("ascii")).hexdigest()
    out["extra"] = stats
    if time.monotonic() > deadline and status in ("COMPLETE", "ESTIMATE"):
        status = "INCOMPLETE_BUDGET"
        for entry in chunks:
            if entry["status"] == "COMPLETE":
                pass
    return status


def main(argv):
    t0 = time.monotonic()
    out = {key: None for key in KEYS}
    out["program"] = PROGRAM
    out["chunks"], out["solutions"], out["extra"] = [], [], {}
    out["solutions_sha256"] = hashlib.sha256(b"[]").hexdigest()
    try:
        with open(os.path.abspath(__file__), "rb") as fh:
            out["program_sha256"] = hashlib.sha256(fh.read()).hexdigest()   # informational only
    except (OSError, NameError):
        out["program_sha256"] = None
    status, reason = "INTERNAL_ERROR", None
    try:
        a = parse_args(argv)
        status = run(a, t0, out)
    except Stop as s:
        status, reason = s.status, s.reason
    except RecursionError:
        status, reason = "INTERNAL_ERROR", "RecursionError"
    except MemoryError:
        status, reason = "INTERNAL_ERROR", "MemoryError"
    except Exception as exc:
        status, reason = "INTERNAL_ERROR", type(exc).__name__
    out["status"], out["reason"] = status, reason
    out["wall_s"] = round(time.monotonic() - t0, 3)
    line = json.dumps(out, sort_keys=True, separators=(",", ":"))
    try:
        write_new("result.json", (line + "\n").encode("ascii"))
    except OSError as exc:
        out["status"], out["reason"] = "IO_ERROR", "cannot write result.json: " + type(exc).__name__
        line = json.dumps(out, sort_keys=True, separators=(",", ":"))
    try:
        print(line, flush=True)
    except OSError:
        return EXIT["IO_ERROR"]
    return EXIT[out["status"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
