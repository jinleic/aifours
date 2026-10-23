#!/usr/bin/env python3
"""Parent replay of the AME(4,6) s=48 engine-v5 proof-mode evidence (lane ame46-support, read-only).

Subcommands
  run      Pin small inputs into OUT/inputs-<tag>/; enumerate normal-form deficit profiles and recompute Lemma 17
           independently; regenerate every final CNF from the WRITTEN schema review/V4_PROOF_SCHEMA.r2.md (r1 as
           written is also generated, and its first differing clause is recorded); stream each gz LRAT stream as
           addition-only DRAT (hints and deletions discarded) into the pinned parent drat-trim -I -U, checked
           against the exact regenerated text passed through an anonymous pipe (/dev/fd/N). Nothing large is stored.
  convert  gz ASCII LRAT -> addition-only ASCII DRAT on stdout. NOT a verifier. Stats JSON on stderr, including
           the SHA-256 of the compressed bytes actually read.

Base families B1-B4 come from the pinned lane generator large_t_gen.SmallGen.build_gen (snapshot copy), as in the
LOWER48 parent replay. The officer CNF (C1-C3 with the Sinz counter that the schema incorporates by reference to
ame_e0_cnf.CNF.at_most_k lines 48-68), the J linking, W (e = 0 only), the lex-leader chains, the blocking clauses
and the DIMACS composition are written here from the schema text; no lane code is imported for them.
Limits: <= 1.5 GiB sampled aggregate RSS (driver + children), free-disk floor 12e9 B, native drat-trim -t,
SIGTERM plus bounded wait only (never SIGKILL); a trip or timeout is UNKNOWN.
"""
import _thread
import argparse
import gzip
import hashlib
import io
import itertools
import json
import os
import resource
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LANE = ROOT / "physics/evidence/six-lane-20261016/ame46-support"
DT = HERE / "moqls7-parent-proofcheck-v1/drat-trim"
DT_SHA = "a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37"
SMOKE_SRC = HERE / "ame46-lower46-parent-inputs-v1/conversion-smoke-v1"
RSS_CAP = 1536 * 2 ** 20
FREE_FLOOR = 12_000_000_000
DT_LIMIT = 1200
WALL_GRACE = 300
TERM_WAIT = 30
PAIRINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))

# Lane files copied into the snapshot; the SHA-256 values are the ones pinned by the assignment, the specs they cite,
# or (marked) observed at the first pin and re-checked on every run.
LANE_PINS = {
    "review/ENGINE_V5.r1.md": "5393238f0aee2f37bf1641e644b0555691320ffbd4fccfdb65838b135e06bf0a",
    "review/V4_PROOF_SCHEMA.r1.md": "f558e75b6d7f87ea5db3f8025be8475694715d1f8e2f94f88673094936e0b986",
    "review/V4_PROOF_SCHEMA.r2.md": "ef692d9df4303b77a09b919abdd3e6bfb5f73661bbb03ccc92db73ac3f7c9309",
    "review/ENGINE_V3.r1.md": "fd7c7447d7140d934d3311a27e2e368dd1167334cf370bf7e8b3ddac1bd74449",  # observed
    "review/ENGINE_V4.r1.md": "fd1d47f2c6361e4d467369bb914e16b587b27bb5d9e3d660d38400b74b258c12",
    "review/SUPPORT_LOWER48.r2.md": "70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e",  # observed
    "code/large_t_gen.py": "28c0c1f9e32089d0080869689be6ea7fd3dd93ae5239cf0c7131cf4c4607bcfd",
    "code/large_t_e0.py": "67033dcfc2e41d29f73c235ac422857be33f684135102e7c5739b303a755466c",
    "code/ame_e0_cnf.py": "97e30ae4e825440653a50e3de84389b00122fa70d3bbddb42924ccdd6ed78a26",
    "code/phase_check.py": "0c591d1b1188a536c88831fb632f92b78b5f771c473d2d2f6fdff99ca728f693",
}
PARENT_PINS = {
    "ame46-lower48-lex-prefix-clarification-v1.md": "8b971680c64f20c0df3080dc1de73da8f14719acbaa89eb1ce2e3704ede647ef",
}

# Pair orders, written from the schema documents.
R1_PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]   # r1 section 0: a single order for every family
R2_BPAIRS = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]  # r2 section 0: B1 hole indicators and J linking
R2_SPAIRS = list(itertools.combinations(range(4), 2))         # r2 section 0: first loop of the officer CNF only
SCHEMAS = {
    "r2": {"doc": "review/V4_PROOF_SCHEMA.r2.md", "hl_pairs": R2_BPAIRS, "officer_pairs": R2_SPAIRS,
           "link_pairs": R2_BPAIRS},
    "r1-as-written": {"doc": "review/V4_PROOF_SCHEMA.r1.md", "hl_pairs": R1_PAIRS, "officer_pairs": R1_PAIRS,
                      "link_pairs": R1_PAIRS},
}
FAMILIES = ("base", "officer", "link", "W", "lex", "block")


def sha_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip()


def write_json(path, obj):
    with Path(path).open("x") as f:
        json.dump(obj, f, indent=1)
        f.write("\n")


# ----------------------------------------------------------------------------------------------- converter
class HashingRaw(io.RawIOBase):
    def __init__(self, f):
        self.f, self.h, self.n = f, hashlib.sha256(), 0

    def readable(self):
        return True

    def readinto(self, b):
        n = self.f.readinto(b)
        if n:
            self.h.update(memoryview(b)[:n])
            self.n += n
        return n


def convert(path, maximum, original):
    raw = open(path, "rb", buffering=0)
    hashed = HashingRaw(raw)
    buffered = io.BufferedReader(hashed, 1 << 20)
    out = sys.stdout.buffer
    lines = comments = additions = deletions = out_bytes = 0
    raw_hash, add_hash = hashlib.sha256(), hashlib.sha256()
    last, empty, empty_last = original, 0, False
    with gzip.GzipFile(fileobj=buffered, mode="rb") as source:
        for line in source:
            lines += 1
            raw_hash.update(line)
            tok = line.split()
            if not tok:
                continue
            if tok[0] == b"c":
                comments += 1
                continue
            if int(tok[0]) <= 0:
                raise ValueError("nonpositive step id")
            if len(tok) > 1 and tok[1] == b"d":
                if tok[-1] != b"0" or any(int(v) <= 0 for v in tok[2:-1]):
                    raise ValueError("malformed deletion record")
                deletions += 1
                continue
            step = int(tok[0])
            if step <= last:
                raise ValueError("addition id not above the CNF clause count / previous addition")
            last = step
            stop = tok.index(b"0", 1)
            lits = [int(v) for v in tok[1:stop]]
            if any(v == 0 or abs(v) > maximum for v in lits):
                raise ValueError("literal outside the original variable range")
            hints = tok[stop + 1:]
            if not hints or hints[-1] != b"0" or b"0" in hints[:-1]:
                raise ValueError("malformed hint suffix")
            row = (" ".join(map(str, lits)) + " 0\n").encode() if lits else b"0\n"
            out.write(row)
            add_hash.update(row)
            additions += 1
            out_bytes += len(row)
            empty_last = not lits
            empty += not lits
    out.flush()
    while buffered.read(1 << 20):
        pass
    size = os.fstat(raw.fileno()).st_size
    if hashed.n != size:
        raise ValueError("compressed bytes read differ from file size")
    print(json.dumps({"gz_sha256": hashed.h.hexdigest(), "gz_bytes": hashed.n,
                      "uncompressed_lrat_sha256": raw_hash.hexdigest(), "lines": lines, "comments": comments,
                      "additions": additions, "addition_bytes": out_bytes, "addition_sha256": add_hash.hexdigest(),
                      "deletions_discarded": deletions, "empty_clauses": empty, "last_addition_empty": empty_last,
                      "last_step_id": last}), file=sys.stderr)


# ------------------------------------------------------------------------------------------- resource guard
class Guard:
    def __init__(self, folder):
        self.folder, self.children, self.lock = folder, set(), threading.Lock()
        self.trip, self.peak, self.window_peak, self.min_free = None, 0, 0, None
        self.stop = threading.Event()
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def add(self, p):
        with self.lock:
            self.children.add(p)

    def drop(self, p):
        with self.lock:
            self.children.discard(p)

    def window(self):
        peak, self.window_peak = self.window_peak, 0
        return peak

    def loop(self):
        while not self.stop.wait(0.5):
            with self.lock:
                kids = [p for p in self.children if p.returncode is None]
            ids = [os.getpid()] + [p.pid for p in kids]
            ps = subprocess.run(["ps", "-o", "rss=", "-p", ",".join(map(str, ids))], capture_output=True, text=True)
            total = sum(int(v) for v in ps.stdout.split() if v.isdigit()) * 1024
            st = os.statvfs(self.folder)
            free = st.f_bavail * st.f_frsize
            self.peak = max(self.peak, total)
            self.window_peak = max(self.window_peak, total)
            self.min_free = free if self.min_free is None else min(self.min_free, free)
            why = ("aggregate RSS %d B > cap %d B" % (total, RSS_CAP) if total > RSS_CAP else
                   "free disk %d B < floor %d B" % (free, FREE_FLOOR) if free < FREE_FLOOR else None)
            if why and self.trip is None:
                self.trip = why
                for p in kids:
                    if p.returncode is None:
                        p.terminate()
                _thread.interrupt_main()


def reap(p, deadline, guard):
    """Bounded wait through wait4 (exact child ru_maxrss); SIGTERM at the deadline or a guard trip; no SIGKILL."""
    termed = None
    while True:
        pid, status, ru = os.wait4(p.pid, os.WNOHANG)
        if pid == p.pid:
            p.returncode = os.waitstatus_to_exitcode(status)
            guard.drop(p)
            return {"rc": p.returncode, "maxrss_bytes": ru.ru_maxrss, "user_s": round(ru.ru_utime, 3),
                    "sys_s": round(ru.ru_stime, 3), "sigterm_sent": termed is not None}
        t = time.monotonic()
        if termed is None and (t > deadline or guard.trip):
            p.terminate()
            termed = t
        elif termed is not None and t - termed > TERM_WAIT:
            return {"rc": None, "maxrss_bytes": None, "sigterm_sent": True, "survived_sigterm": True}
        time.sleep(0.02)


def check_rup(text, nv, m, gz, guard, expect_gz_sha=None, want_core=False):
    """Pinned drat-trim -I -U on the exact text (anonymous pipe) and the converted additions (stdin).

    At most two busy processes: driver writer + checker while the CNF is parsed, then converter + checker."""
    if sha_file(DT) != DT_SHA:
        raise ValueError("parent drat-trim changed")
    start = time.monotonic()
    deadline = start + DT_LIMIT + WALL_GRACE
    guard.window()
    drv = subprocess.run(["ps", "-o", "rss=", "-p", str(os.getpid())], capture_output=True, text=True).stdout.strip()
    driver_rss = int(drv) * 1024 if drv.isdigit() else None
    cnf_r, cnf_w = os.pipe()
    prf_r, prf_w = os.pipe()
    fds = [cnf_r]
    args = [str(DT), "/dev/fd/%d" % cnf_r, "-I", "-U", "-t", str(DT_LIMIT)]
    core_r = core_w = None
    if want_core:
        core_r, core_w = os.pipe()
        fds.append(core_w)
        args += ["-c", "/dev/fd/%d" % core_w]
    checker = subprocess.Popen(args, stdin=prf_r, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, pass_fds=fds)
    guard.add(checker)
    os.close(cnf_r)
    os.close(prf_r)
    if want_core:
        os.close(core_w)
    out, core, err, writer_errors = [], [], [], []

    def drain(stream, sink):
        with stream:
            sink.append(stream.read())

    readers = [threading.Thread(target=drain, args=(checker.stdout, out), daemon=True)]
    if want_core:
        readers.append(threading.Thread(target=drain, args=(os.fdopen(core_r, "rb"), core), daemon=True))
    for r in readers:
        r.start()

    def writer():
        try:
            with os.fdopen(cnf_w, "wb") as f:
                f.write(text)
        except OSError as e:
            writer_errors.append(str(e))

    w = threading.Thread(target=writer, daemon=True)
    w.start()
    stopped_early = False
    while w.is_alive():
        w.join(0.05)
        if (time.monotonic() > deadline or guard.trip) and checker.returncode is None:
            checker.terminate()
            stopped_early = True
            break
    w.join(TERM_WAIT)
    conv = conv_r = None
    if not writer_errors and not stopped_early and not w.is_alive():
        conv = subprocess.Popen([sys.executable, "-B", str(Path(__file__).resolve()), "convert", str(gz), str(nv),
                                 str(m)], stdout=prf_w, stderr=subprocess.PIPE)
        guard.add(conv)
        os.close(prf_w)
        er = threading.Thread(target=drain, args=(conv.stderr, err), daemon=True)
        er.start()
        conv_r = reap(conv, deadline, guard)
        er.join(TERM_WAIT)
    else:
        os.close(prf_w)
    chk_r = reap(checker, deadline, guard)
    for r in readers:
        r.join(TERM_WAIT)
    wall = time.monotonic() - start
    text_out = out[0] if out else b""
    lines = [ln.decode(errors="replace").strip() for ln in text_out.split(b"\n")]
    lines = [ln for ln in lines if ln]
    statuses = [ln for ln in lines if ln.startswith("s ")]
    stats = None
    if err and err[0].strip():
        try:
            stats = json.loads(err[0].strip().splitlines()[-1])
        except ValueError:
            stats = {"stderr_tail": err[0].decode(errors="replace")[-2000:]}
    gz_ok = (stats is not None and "gz_sha256" in stats and
             (expect_gz_sha is None or stats["gz_sha256"] == expect_gz_sha))
    verified = (not writer_errors and conv_r is not None and conv_r["rc"] == 0 and chk_r["rc"] == 0 and
                not conv_r["sigterm_sent"] and not chk_r["sigterm_sent"] and statuses == ["s VERIFIED"] and gz_ok and
                guard.trip is None)
    return {"cnf_sha256": hashlib.sha256(text).hexdigest(), "cnf_bytes": len(text), "cnf_variables": nv,
            "cnf_clauses": m, "proof": str(gz), "expected_gz_sha256": expect_gz_sha, "converter": stats,
            "converter_proc": conv_r, "gz_sha_ok": gz_ok, "checker_proc": chk_r, "checker_rc": chk_r["rc"],
            "statuses": statuses, "not_verified_seen": "s NOT VERIFIED" in statuses,
            "checker_tail": lines[-9:], "checker_output_sha256": hashlib.sha256(text_out).hexdigest(),
            "writer_errors": writer_errors, "stopped_early": stopped_early, "wall_seconds": round(wall, 3),
            "peak_aggregate_rss_sampled_bytes": guard.window(), "driver_rss_at_start_bytes": driver_rss,
            "aggregate_upper_bound_bytes": (driver_rss + chk_r["maxrss_bytes"] + conv_r["maxrss_bytes"]
                                            if driver_rss and conv_r and conv_r["maxrss_bytes"] and
                                            chk_r["maxrss_bytes"] else None),
            "guard_trip": guard.trip, "verified": verified,
            "core": core[0] if (want_core and core) else None}


# --------------------------------------------------------------------------------- profiles and Lemma 17
def partitions_by_counts(h):
    """Parts in {2..6} (L42-8(a); d <= 6), at most 6 parts (|V_i| <= 6), summing to h; via part multiplicities."""
    sizes = (6, 5, 4, 3, 2)
    out = []
    for counts in itertools.product(*(range(h // k + 1) for k in sizes)):
        if sum(k * n for k, n in zip(sizes, counts)) == h and sum(counts) <= 6:
            out.append(tuple(k for k, n in zip(sizes, counts) for _ in range(n)))
    return out


def normal_profiles(h):
    """All multisets of four partitions with max part of p_i <= |p_j| for j != i (L46-12); brute force on 4-tuples."""
    parts = partitions_by_counts(h)
    found = set()
    for combo in itertools.product(parts, repeat=4):
        if all(max(combo[i]) <= min(len(combo[j]) for j in range(4) if j != i) for i in range(4)):
            found.add(tuple(sorted(combo)))
    return found, len(parts)


def lemma17(prof, t):
    h = 36 - t
    v = [len(p) for p in prof]
    k1 = 6 * sum(v) - 4 * h
    k2 = sum(v[i] * v[j] for i in range(4) for j in range(i + 1, 4)) - 6 * h

    def f(a):
        return k2 - a * k1 + (a + 1) * a // 2 * t

    f04 = [f(a) for a in range(5)]
    wide = min(f(a) for a in range(-40, 41))
    return {"kappa0": t, "kappa1": k1, "kappa2": k2, "f_0_4": f04, "min_f_0_4": min(f04), "min_f_-40_40": wide,
            "excluded": min(f04) < 0}


# ------------------------------------------------------------------------------- written-schema regeneration
def amk(cl, nv, lits, k):
    """AMK(L, k): Sinz sequential counter, clause order of ame_e0_cnf.CNF.at_most_k lines 48-68 (schema 0)."""
    m = len(lits)
    if k >= m:
        return nv
    if k == 0:
        for l in lits:
            cl.append([-l])
        return nv
    s = []
    for _ in range(m - 1):
        s.append(list(range(nv + 1, nv + k + 1)))
        nv += k
    cl.append([-lits[0], s[0][0]])
    for j in range(1, k):
        cl.append([-s[0][j]])
    for i in range(1, m - 1):
        cl.append([-lits[i], s[i][0]])
        cl.append([-s[i - 1][0], s[i][0]])
        for j in range(1, k):
            cl.append([-lits[i], -s[i - 1][j - 1], s[i][j]])
            cl.append([-s[i - 1][j], s[i][j]])
        cl.append([-lits[i], -s[i - 1][k - 1]])
    cl.append([-lits[m - 1], -s[m - 2][k - 1]])
    return nv


OFFICER_POINTS = list(itertools.product(range(6), repeat=4))
OFFICER_VAR = {y: k + 1 for k, y in enumerate(OFFICER_POINTS)}


def officer_line(j, k, b, c):
    return [OFFICER_VAR[y] for y in OFFICER_POINTS if y[j] == b and y[k] == c]


def officer_cnf(V, d, pairs):
    """Schema 2.2: C1/C2 for (j,k) in `pairs`, then C3; own numbering, officer variables 1..1296."""
    cl, nv = [], 1296
    for (j, k) in pairs:
        for b in range(6):
            for c in range(6):
                L = officer_line(j, k, b, c)
                if not (b in V[j] and c in V[k]):
                    cl.append(list(L))
                nv = amk(cl, nv, L, 1)
    for j in range(4):
        for k in range(4):
            if k == j:
                continue
            for a in V[j]:
                inds = []
                for b in V[k]:
                    nv += 1
                    inds.append(nv)
                    L = officer_line(j, k, a, b)
                    cl.append([-nv] + L)
                    for l in L:
                        cl.append([-l, nv])
                nv = amk(cl, nv, inds, len(V[k]) - d[j][a])
                nv = amk(cl, nv, [-v for v in inds], d[j][a])
    return nv, cl


def triangle_clauses(V, var):
    """Schema 2.4 (e = 0): direct construction in the stated loop order (z2, z3 filters enumerated in Z order)."""
    out = []
    for i in range(4):
        c1, c2, c3 = [c for c in range(4) if c != i]

        def pt(a, z, i=i, c1=c1, c2=c2, c3=c3):
            x = [0] * 4
            x[i], x[c1], x[c2], x[c3] = a, z[0], z[1], z[2]
            return var[tuple(x)]

        for a, a2 in itertools.combinations(V[i], 2):
            for z1 in itertools.product(V[c1], V[c2], V[c3]):
                for u in V[c2]:
                    for w in V[c3]:
                        if u == z1[1] or w == z1[2]:
                            continue
                        z2 = (z1[0], u, w)
                        for s in V[c1]:
                            if s == z1[0]:
                                continue
                            z3 = (s, u, z1[2])
                            out.append([-pt(a, z1), -pt(a2, z1), -pt(a, z2), -pt(a2, z2), -pt(a, z3), -pt(a2, z3)])
    return out


def triangle_clauses_literal(V, var):
    """Schema 2.4 transcribed literally (triple loop over Z); only for cross-checking small product spaces."""
    out = []
    for i in range(4):
        c1, c2, c3 = [c for c in range(4) if c != i]
        Z = list(itertools.product(V[c1], V[c2], V[c3]))

        def pt(a, z, i=i, c1=c1, c2=c2, c3=c3):
            x = [0] * 4
            x[i], x[c1], x[c2], x[c3] = a, z[0], z[1], z[2]
            return var[tuple(x)]

        for a, a2 in itertools.combinations(V[i], 2):
            for z1 in Z:
                for z2 in Z:
                    if z2[0] == z1[0] and z2[1] != z1[1] and z2[2] != z1[2]:
                        for z3 in Z:
                            if z3[1] == z2[1] and z3[2] == z1[2] and z3[0] != z1[0]:
                                out.append([-pt(a, z1), -pt(a2, z1), -pt(a, z2), -pt(a2, z2), -pt(a, z3),
                                            -pt(a2, z3)])
    return out


def check_triangles(W, V, points):
    """Count 2*prod |V_k|(|V_k|-1), no duplicates, six distinct points in three doubled pairs with ONE common value
    pair {a,a'} on one coordinate i, the three z's pairwise agreeing in exactly one coordinate, all three distinct."""
    expect = 2
    for v in V:
        expect *= len(v) * (len(v) - 1)
    if len(W) != expect or len({tuple(sorted(c)) for c in W}) != len(W):
        raise ValueError("W count or duplicate failure")
    for c in W:
        if len(c) != 6 or any(l >= 0 for l in c) or len(set(c)) != 6:
            raise ValueError("W clause shape")
        xs = [points[-l - 1] for l in c]
        diff = {k for k in range(4) if len({x[k] for x in xs}) > 1}
        cands = [i for i in range(4) if len({x[i] for x in xs}) == 2 and
                 len({tuple(x[k] for k in range(4) if k != i) for x in xs}) == 3]
        if len(cands) != 1:
            raise ValueError("W clause: no unique doubled coordinate")
        i = cands[0]
        zs = {}
        for x in xs:
            zs.setdefault(tuple(x[k] for k in range(4) if k != i), set()).add(x[i])
        pair = {frozenset(s) for s in zs.values()}
        if len(pair) != 1 or any(len(s) != 2 for s in zs.values()):
            raise ValueError("W clause: doubled pairs do not share one value pair")
        z = list(zs)
        agree = []
        for p, q in ((0, 1), (1, 2), (0, 2)):
            same = [k for k in range(3) if z[p][k] == z[q][k]]
            if len(same) != 1:
                raise ValueError("W clause: an edge does not agree in exactly one coordinate")
            agree.append(same[0])
        if len(set(agree)) != 3 or not diff:
            raise ValueError("W clause: edges do not use three distinct coordinates")
    return expect


def generators(prof):
    """Schema 2.5: coordinate swaps (i,i+1) with p_i = p_{i+1}; then per i the d-classes of V_i in order of first
    occurrence, adjacent pairs in increasing order."""
    gens = []
    for i in range(3):
        if list(prof[i]) == list(prof[i + 1]):
            gens.append(("coord", i, i + 1))
    for i in range(4):
        values = list(range(6 - len(prof[i]), 6))
        classes = {}
        for k, a in enumerate(values):
            classes.setdefault(prof[i][k], []).append(a)
        for members in classes.values():
            for a, b in zip(members, members[1:]):
                gens.append(("value", i, a, b))
    return gens


def apply_gen(g, x):
    y = list(x)
    if g[0] == "coord":
        y[g[1]], y[g[2]] = x[g[2]], x[g[1]]
    else:
        _, i, a, b = g
        y[i] = b if x[i] == a else a if x[i] == b else x[i]
    return tuple(y)


def lex_chain(points, var, g, nv, cl):
    """Schema 2.5 with the q0 = true substitution at k = 1 (parent clarification v1)."""
    prev = None
    for x in points:
        p, q_ = var[x], var[apply_gen(g, x)]
        if p == q_:
            continue
        cl.append([-p, q_] if prev is None else [-prev, -p, q_])
        nv += 1
        q = nv
        if prev is None:
            cl += [[-p, -q_, q], [p, q_, q]]
        else:
            cl += [[-q, prev], [-prev, -p, -q_, q], [-prev, p, q_, q]]
        cl += [[-q, -p, q_], [-q, p, -q_]]
        prev = q
    return nv


def lines_of(clauses, shift=0):
    if shift:
        return "".join(" ".join(str(l + shift if l > 0 else l - shift) for l in c) + " 0\n" for c in clauses)
    return "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)


def regenerate(base, prof, t, e, Ys, variants):
    """Return {variant: (text, meta)} for the final CNF of one profile, base shared, the rest written here."""
    h = 36 - t
    prof = [list(p) for p in prof]
    V = [list(range(6 - len(p), 6)) for p in prof]
    d = [{a: p[k] for k, a in enumerate(V[i])} for i, p in enumerate(prof)]
    points = list(itertools.product(*V))
    var = {x: k + 1 for k, x in enumerate(points)}
    S = base.SmallGen(prof)
    S.build_gen(e, h)
    if S.V != V or S.d != d or S.points != points or S.var != var:
        raise ValueError("base generator conventions differ from schema 0")
    nv0 = S.nv
    hl = dict(S.hl)
    base_text = lines_of(S.cl).encode()
    n_base = len(S.cl)
    if any(not c for c in S.cl):
        raise ValueError("empty clause in the base")
    del S
    W = []
    if e == 0:
        W = triangle_clauses(V, var)
        check_triangles(W, V, points)
        if len(points) <= 128 and W != triangle_clauses_literal(V, var):
            raise ValueError("direct W construction differs from the literal schema loop")
    W_text = lines_of(W).encode()
    blocks = []
    for Y in Ys:
        lits = sorted(var[tuple(int(c) for c in s)] for s in Y)
        blocks.append([-v for v in lits])
    block_text = lines_of(blocks).encode()
    gens = generators(prof)
    out = {}
    for name in variants:
        sch = SCHEMAS[name]
        order = [(i, j, a, b) for (i, j) in sch["hl_pairs"] for a in V[i] for b in V[j]]
        hl_as_doc = hl == {key: len(points) + 1 + k for k, key in enumerate(order)}
        Fnv, F = officer_cnf(V, d, sch["officer_pairs"])
        officer_text = lines_of(F, nv0).encode()
        link = []
        for (i, j) in sch["link_pairs"]:
            for a in V[i]:
                for b in V[j]:
                    hv = hl[(i, j, a, b)]
                    lam = [nv0 + o for o in officer_line(i, j, a, b)]
                    link += [[-hv, -o] for o in lam]
                    link.append([hv] + lam)
        link_text = lines_of(link).encode()
        nv = nv0 + Fnv
        lex = []
        for g in gens:
            nv = lex_chain(points, var, g, nv, lex)
        lex_text = lines_of(lex).encode()
        counts = {"base": n_base, "officer": len(F), "link": len(link), "W": len(W), "lex": len(lex),
                  "block": len(blocks)}
        m = sum(counts.values())
        text = b"".join([("p cnf %d %d\n" % (nv, m)).encode(), base_text, officer_text, link_text, W_text, lex_text,
                         block_text])
        out[name] = (text, {"sha256": hashlib.sha256(text).hexdigest(), "bytes": len(text), "variables": nv,
                            "clauses": m, "nv0": nv0, "officer_nv": Fnv, "counts": counts,
                            "generators": [list(g) for g in gens], "hl_numbering_as_documented": hl_as_doc})
        del F, link, lex
    return out


def first_difference(a, b, counts):
    """First differing DIMACS line (header = line 1) of two texts with a common prefix, and its clause family."""
    n = min(len(a), len(b))
    k, step = 0, 1 << 16
    while k < n and a[k:k + step] == b[k:k + step]:
        k += step
    while k < n and a[k] == b[k]:
        k += 1
    if k == n and len(a) == len(b):
        return None
    start = a.rfind(b"\n", 0, k) + 1
    line = a.count(b"\n", 0, start) + 1
    clause = line - 2
    fam, acc = None, 0
    for f in FAMILIES:
        if clause < acc + counts[f]:
            fam = (f, clause - acc)
            break
        acc += counts[f]
    end_a, end_b = a.find(b"\n", start), b.find(b"\n", start)
    return {"dimacs_line": line, "clause_index0": clause, "family": fam[0] if fam else None,
            "index_in_family0": fam[1] if fam else None, "this_text": a[start:end_a].decode(),
            "other_text": b[start:end_b].decode()}


# --------------------------------------------------------------------------------------- recorded supports
def phase_certificate(N, cert):
    """LOWER48 r2 section 3 closure criteria (adapted from the parent LOWER48 replay)."""
    forms, weight = Counter(), 0
    for entry in cert:
        w, k, pts = entry["w"], entry["k"], entry["corners"]
        if type(w) is not int or w == 0 or k not in range(3) or len(pts) != 4:
            raise ValueError("bad compact certificate entry")
        a, b, c, d = pts
        if not all(x in N for x in pts):
            raise ValueError("phase corner outside support")
        rp, cp = PAIRINGS[k]

        def row(x, rp=rp):
            return tuple(x[i] for i in rp)

        def col(x, cp=cp):
            return tuple(x[i] for i in cp)

        if not (row(a) == row(b) and row(c) == row(d) and row(a) != row(c) and
                col(a) == col(c) and col(b) == col(d) and col(a) != col(b)):
            raise ValueError("phase corners not a rectangle")
        R, C = defaultdict(set), defaultdict(set)
        for x in N:
            R[row(x)].add(col(x))
            C[col(x)].add(row(x))
        if any(len(R[row(x)]) != 2 or len(C[col(x)]) != 2 for x in pts):
            raise ValueError("phase rectangle not a closed component")
        for x, sign in ((a, 1), (b, -1), (c, -1), (d, 1)):
            forms[x] += w * sign
        weight += w
    if any(forms.values()) or weight % 2 != 1:
        raise ValueError("phase weighted form nonzero or weight sum even")
    return {"forms": len(cert), "weight_sum": weight, "verdict": "PASS"}


# ------------------------------------------------------------------------------------------------- run
def pin_inputs(snap, receipt_rel, receipt_sha, cases):
    snap.mkdir(exist_ok=False)
    files, problems = {}, []
    wanted = dict(LANE_PINS)
    wanted[receipt_rel] = receipt_sha
    for (t, e, rsha) in cases:
        wanted["evidence/large_t_joint5_t%d_e%d.json" % (t, e)] = rsha
    sources = [(LANE / rel, snap / "lane" / rel, "lane/" + rel, expect) for rel, expect in wanted.items()]
    sources += [(HERE / rel, snap / "parent" / rel, "parent/" + rel, expect) for rel, expect in PARENT_PINS.items()]
    dirs = set()
    for _, dest, _, _ in sources:
        p = dest.parent
        while p != snap:
            dirs.add(p)
            p = p.parent
    for p in sorted(dirs, key=lambda q: len(q.parts)):
        p.mkdir(exist_ok=False)
    for src, dest, key, expect in sources:
        data = src.read_bytes()
        got = hashlib.sha256(data).hexdigest()
        with dest.open("xb") as f:
            f.write(data)
        files[key] = {"source": str(src), "sha256": got, "bytes": len(data), "expected": expect, "ok": got == expect}
        if got != expect:
            problems.append(key)
    receipt = {"recorded_at_pt": now(), "files": files, "all_ok": not problems, "problems": problems,
               "not_copied": "gz LRAT streams are read in place from the lane; the converter hashes the exact "
                             "compressed bytes it streams"}
    write_json(snap / "pin-receipt.json", receipt)
    if problems:
        raise ValueError("input pin mismatch: %s" % problems)
    return receipt


def case_header(report, t, e):
    h = 36 - t
    checks = {"engine": report.get("engine") == "large_t_joint5 v5", "mode": report.get("mode") == "proof",
              "joint": report.get("joint") is True, "triangles": report.get("triangles") is (e == 0),
              "t_e_h": (report.get("t"), report.get("e"), report.get("h")) == (t, e, h),
              "guard_tripped_null": "guard_tripped" in report and report["guard_tripped"] is None,
              "outcome": report.get("outcome") == "EXCLUDED", "excluded": report.get("excluded") is True,
              "no_candidates": report.get("candidates") == []}
    return checks


def run(args):
    dry = args.dry_run
    out = HERE / args.out
    if not dry and not out.exists():
        out.mkdir(exist_ok=False)
    started = now()
    guard = Guard(HERE if dry else out)
    cases = []
    for spec in args.case:
        t, e, rsha = spec.split(":")
        cases.append((int(t), int(e), rsha))
    rrel, rsha = args.receipt.split(":")
    snap = out / ("inputs-" + args.tag)
    checks_dir = out / ("checks-" + args.tag)
    log = None if dry else (out / ("run-" + args.tag + ".log")).open("x")

    def say(obj):
        line = json.dumps(obj)
        print(line, flush=True)
        if log:
            log.write(line + "\n")
            log.flush()

    result = {"started_at_pt": started, "driver": str(Path(__file__).resolve()),
              "driver_sha256": sha_file(Path(__file__)), "python": sys.version, "drat_trim": str(DT),
              "drat_trim_sha256_start": sha_file(DT), "limits": {"aggregate_rss_cap_bytes": RSS_CAP,
              "free_floor_bytes": FREE_FLOOR, "drat_trim_t": DT_LIMIT, "wall_deadline_s": DT_LIMIT + WALL_GRACE},
              "tag": args.tag, "dry_run": dry, "verdict": "UNKNOWN", "cases": [], "controls": None, "smoke": None}
    verdict_ok = True
    try:
        if result["drat_trim_sha256_start"] != DT_SHA:
            raise ValueError("parent drat-trim changed")
        if dry:
            src = LANE
            bad = [rel for rel, s in list(LANE_PINS.items()) + [(rrel, rsha)] +
                   [("evidence/large_t_joint5_t%d_e%d.json" % (t, e), s) for (t, e, s) in cases]
                   if sha_file(LANE / rel) != s]
            if bad:
                raise ValueError("input pin mismatch: %s" % bad)
        else:
            result["pins"] = pin_inputs(snap, rrel, rsha, cases)
            src = snap / "lane"
        sys.path.insert(0, str(src / "code"))
        import large_t_gen as base
        result["base_generator_sha256"] = sha_file(base.__file__)
        if not dry:
            checks_dir.mkdir(exist_ok=False)
        receipt = json.loads((src / rrel).read_text())
        rcases = {(c["t"], c["e"]): c for c in receipt["cases"]}
        all_report_shas = {}
        reports = {}
        for (t, e, rs) in cases:
            reports[(t, e)] = json.loads((src / ("evidence/large_t_joint5_t%d_e%d.json" % (t, e))).read_text())
            for p in reports[(t, e)]["profiles"]:
                if p.get("final_cnf_sha256"):
                    all_report_shas[p["final_cnf_sha256"]] = (t, e, p["index"])
        for (t, e, rs) in cases:
            h = 36 - t
            report = reports[(t, e)]
            rc = rcases.get((t, e))
            header = case_header(report, t, e)
            crow = {"t": t, "e": e, "h": h, "report": "evidence/large_t_joint5_t%d_e%d.json" % (t, e),
                    "report_sha256": rs, "header_checks": header, "header_ok": all(header.values()),
                    "receipt_case_present": rc is not None}
            verdict_ok &= crow["header_ok"] and rc is not None
            if rc is not None:
                crow["receipt_binding"] = {"report_path": rc["report"] == crow["report"],
                                           "report_sha": rc["report_sha256"] == rs, "t_e": (rc["t"], rc["e"]) == (t, e),
                                           "profile_count": len(rc["profiles"]) == len(report["profiles"])}
                verdict_ok &= all(crow["receipt_binding"].values())
            expected, nparts = normal_profiles(h)
            listed = [tuple(sorted(tuple(p) for p in pr["profile"])) for pr in report["profiles"]]
            prof_ok = []
            for pr in report["profiles"]:
                p = pr["profile"]
                prof_ok.append(all(list(q) == sorted(q, reverse=True) and sum(q) == h and 1 <= len(q) <= 6 and
                                   all(2 <= x <= 6 for x in q) for q in p) and len(p) == 4)
            crow["profiles_check"] = {"partitions_of_h": nparts, "independent_count": len(expected),
                                      "report_count": len(listed), "duplicates": len(listed) - len(set(listed)),
                                      "missing": sorted(map(list, expected - set(listed))),
                                      "extra": sorted(map(list, set(listed) - expected)),
                                      "all_listed_well_formed": all(prof_ok)}
            crow["profiles_complete"] = (set(listed) == expected and len(listed) == len(expected) and all(prof_ok))
            verdict_ok &= crow["profiles_complete"]
            crow["profiles"] = []
            Ys_total = 0
            for k, pr in enumerate(report["profiles"]):
                L17 = lemma17(pr["profile"], t)
                row = {"index": pr["index"], "profile": pr["profile"], "status": pr["status"], "lemma17": L17,
                       "lemma17_report_match": pr.get("lemma17_f") == L17["f_0_4"],
                       "lemma17_wide_adds_nothing": (L17["min_f_-40_40"] < 0) == (L17["min_f_0_4"] < 0)}
                rp = rc["profiles"][k] if rc is not None and k < len(rc["profiles"]) else None
                row["receipt_row_status_index"] = (rp is not None and rp.get("index") == pr["index"] and
                                                   rp.get("status") == pr["status"])
                ok = row["lemma17_report_match"] and row["lemma17_wide_adds_nothing"] and row["receipt_row_status_index"]
                if pr["status"] == "EXCLUDED-BY-LEMMA":
                    ok &= L17["excluded"] and pr.get("reps") == []
                    gen = regenerate(base, pr["profile"], t, e, [], ["r2"])
                    meta = gen["r2"][1]
                    row["wrong_profile_control_cnf_sha256"] = meta["sha256"]
                    row["wrong_profile_control_matches_any_report_sha"] = meta["sha256"] in all_report_shas
                    ok &= not row["wrong_profile_control_matches_any_report_sha"]
                    del gen
                elif pr["status"] in ("ENUMERATED", "EMPTY"):
                    ok &= not L17["excluded"]
                    reps = pr.get("reps", [])
                    Ys = [rep["N"] for rep in reps]
                    Ys_total += len(Ys)
                    V = [list(range(6 - len(p), 6)) for p in pr["profile"]]
                    ych = []
                    seen = set()
                    for rep in reps:
                        N = rep["N"]
                        pts = [tuple(int(c) for c in s) for s in N]
                        y = {"size": len(N), "size_is_2h_plus_e": len(N) == 2 * h + e,
                             "distinct": len(set(N)) == len(N) and frozenset(N) not in seen,
                             "in_product": all(len(s) == 4 and all(x[i] in V[i] for i in range(4))
                                               for s, x in zip(N, pts)),
                             "product_order": pts == sorted(pts)}
                        seen.add(frozenset(N))
                        cert = rep.get("phase_certificate_compact")
                        if rep.get("excluded") is True and cert:
                            try:
                                y["phase"] = phase_certificate(set(N), cert)
                            except ValueError as ex:
                                y["phase"] = {"verdict": "FAIL", "reason": str(ex)}
                        else:
                            y["phase"] = {"verdict": "UNCHECKED", "reason": "no compact phase certificate"}
                        y["ok"] = (y["size_is_2h_plus_e"] and y["distinct"] and y["in_product"] and
                                   y["phase"]["verdict"] == "PASS")
                        ych.append(y)
                    row["recorded_Y"] = {"solutions_field": pr.get("solutions"), "reps": len(reps),
                                         "consistent": pr.get("solutions") == len(reps), "checks": ych}
                    ok &= row["recorded_Y"]["consistent"] and all(y["ok"] for y in ych)
                    row["report_fields"] = {"bindings_asserted": pr.get("bindings_asserted"),
                                            "generators": pr.get("generators"),
                                            "triangle_clauses": pr.get("triangle_clauses"),
                                            "final_cnf_sha256": pr.get("final_cnf_sha256"),
                                            "worker_checkers": {k2: pr.get("final_proof", {}).get(k2)
                                                                for k2 in ("C", "py")}}
                    fp = pr.get("final_proof") or {}
                    stream = (rp or {}).get("stream") or {}
                    row["receipt_stream"] = stream
                    row["stream_binding"] = {"path_eq": stream.get("proof") == fp.get("proof"),
                                             "sha_eq": stream.get("proof_gz_sha256") == fp.get("proof_gz_sha256"),
                                             "cnf_sha_eq": rp is not None and rp.get("final_cnf_sha256") ==
                                             pr.get("final_cnf_sha256")}
                    ok &= all(row["stream_binding"].values()) and pr.get("bindings_asserted") is True
                    gen = regenerate(base, pr["profile"], t, e, Ys, ["r2", "r1-as-written"])
                    text, meta = gen["r2"]
                    text1, meta1 = gen["r1-as-written"]
                    row["regen_r2"] = meta
                    row["regen_r2"]["matches_report"] = meta["sha256"] == pr.get("final_cnf_sha256")
                    row["regen_r2"]["matches_other_profile_report"] = [
                        v for s, v in all_report_shas.items() if s == meta["sha256"] and v != (t, e, pr["index"])]
                    row["regen_r2"]["generators_match_report"] = len(meta["generators"]) == pr.get("generators")
                    row["regen_r2"]["W_matches_report"] = meta["counts"]["W"] == pr.get("triangle_clauses")
                    row["regen_r2"]["blocking_clauses"] = meta["counts"]["block"]
                    row["regen_r1_as_written"] = {"sha256": meta1["sha256"],
                                                  "matches_report": meta1["sha256"] == pr.get("final_cnf_sha256"),
                                                  "hl_numbering_as_documented": meta1["hl_numbering_as_documented"],
                                                  "first_difference_vs_r2_text":
                                                  first_difference(text1, text, meta1["counts"])}
                    del text1, gen
                    ok &= (row["regen_r2"]["matches_report"] and not row["regen_r2"]["matches_other_profile_report"]
                           and row["regen_r2"]["generators_match_report"] and row["regen_r2"]["W_matches_report"]
                           and meta["counts"]["block"] == len(Ys) and meta["hl_numbering_as_documented"])
                    gz = LANE / fp["proof"]
                    if not row["regen_r2"]["matches_report"]:
                        row["proof_check"] = {"skipped": "regenerated text does not match the report SHA"}
                        ok = False
                    else:
                        chk = check_rup(text, meta["variables"], meta["clauses"], gz, guard,
                                        expect_gz_sha=stream.get("proof_gz_sha256"))
                        chk.pop("core")
                        chk["expected_gz_bytes"] = stream.get("proof_gz_bytes")
                        chk["gz_bytes_ok"] = (chk["converter"] or {}).get("gz_bytes") == stream.get("proof_gz_bytes")
                        chk["empty_clause_last"] = (chk["converter"] or {}).get("last_addition_empty") is True
                        if not dry:
                            write_json(checks_dir / ("t%d_e%d_p%d.json" % (t, e, pr["index"])), chk)
                        row["proof_check"] = chk
                        ok &= chk["verified"] and chk["gz_bytes_ok"]
                        say({"t": t, "e": e, "profile": pr["index"], "verified": chk["verified"],
                             "statuses": chk["statuses"], "wall_s": chk["wall_seconds"],
                             "dt_maxrss": chk["checker_proc"]["maxrss_bytes"]})
                    if stream.get("satisfied_hints") or stream.get("strict_info") is False:
                        row["worker_strict_mode_note"] = (
                            "receipt strict_info=%s satisfied_hints=%s; the parent RUP replay discards hints, so this "
                            "stream is checked exactly like the others" % (stream.get("strict_info"),
                                                                            stream.get("satisfied_hints")))
                    del text
                else:
                    ok = False
                row["ok"] = bool(ok)
                verdict_ok &= row["ok"]
                crow["profiles"].append(row)
            crow["recorded_Y_total"] = Ys_total
            enum = [r for r in crow["profiles"] if "regen_r2" in r]
            crow["final_cnfs_without_blocking_clauses"] = all(r["regen_r2"]["blocking_clauses"] == 0 for r in enum)
            crow["load_bearing_unsat"] = sum(1 for r in crow["profiles"] if "proof_check" in r)
            crow["load_bearing_verified"] = sum(1 for r in crow["profiles"]
                                                if r.get("proof_check", {}).get("verified"))
            crow["worker_strict_mode_nonstrict_streams"] = [
                {"index": r["index"], "profile": r["profile"], "proof": r["receipt_stream"].get("proof"),
                 "strict_info": r["receipt_stream"].get("strict_info"),
                 "satisfied_hints": r["receipt_stream"].get("satisfied_hints"),
                 "worker_checker_messages": {k2: (v or {}).get("msg") for k2, v in
                                             r["report_fields"]["worker_checkers"].items()},
                 "parent_rup_verified": r.get("proof_check", {}).get("verified")}
                for r in enum if "worker_strict_mode_note" in r]
            crow["report_top"] = {k2: report.get(k2) for k2 in ("guard_tripped", "outcome", "excluded", "candidates",
                                                                "peak_rss_bytes_sampled", "bytes_written_before_report",
                                                                "min_free_bytes_sampled", "caps")}
            crow["case_ok"] = (crow["header_ok"] and crow["profiles_complete"] and
                               all(r["ok"] for r in crow["profiles"]))
            interrupted = any(r.get("proof_check", {}).get("stopped_early") or
                              (r.get("proof_check", {}).get("checker_proc") or {}).get("sigterm_sent") or
                              (r.get("proof_check", {}).get("converter_proc") or {}).get("sigterm_sent")
                              for r in crow["profiles"])
            crow["case_status"] = ("UNKNOWN" if report.get("guard_tripped") is not None or interrupted else
                                   "PASS" if crow["case_ok"] else "FAIL")
            result["cases"].append(crow)
            say({"case": [t, e], "case_status": crow["case_status"], "verified": crow["load_bearing_verified"],
                 "of": crow["load_bearing_unsat"]})
        if args.controls:
            if not dry:
                result["smoke"] = smoke(out / ("smoke-" + args.tag), guard)
                verdict_ok &= result["smoke"]["all_ok"]
            result["controls"] = controls(base, reports, guard, say)
            verdict_ok &= result["controls"]["all_ok"]
        result["drat_trim_sha256_end"] = sha_file(DT)
        verdict_ok &= result["drat_trim_sha256_end"] == DT_SHA and guard.trip is None
        statuses = [c["case_status"] for c in result["cases"]]
        result["verdict"] = ("PASS" if verdict_ok and all(s == "PASS" for s in statuses) else
                             "FAIL" if "FAIL" in statuses or guard.trip is None and "UNKNOWN" not in statuses else
                             "UNKNOWN")
        result["scope"] = ("Parent replay of the four e>0 engine-v5 proof-mode reports: profile completeness and "
                           "Lemma 17 recomputed; every final CNF regenerated from V4_PROOF_SCHEMA.r2 (officer CNF, "
                           "J, lex and composition written here; base from the pinned build_gen) and SHA-compared; "
                           "each gz LRAT stream converted to addition-only RUP and checked by the pinned parent "
                           "drat-trim -I -U. Partial evidence toward s>=49 only; (24,0) is not covered; Lemmas 17, "
                           "19 and the completeness argument are reviewed elsewhere.")
    except KeyboardInterrupt:
        result["verdict"] = "UNKNOWN"
        result["stopped"] = "guard trip: %s" % guard.trip
    except Exception as ex:  # recorded, never excluded
        result["verdict"] = "UNKNOWN" if guard.trip else "FAIL"
        result["stopped"] = "%s: %s" % (type(ex).__name__, ex)
    guard.stop.set()
    result["guard"] = {"trip": guard.trip, "peak_aggregate_rss_sampled_bytes": guard.peak,
                       "min_free_bytes_sampled": guard.min_free,
                       "driver_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                       "children_maxrss_bytes": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
    result["ended_at_pt"] = now()
    if dry:
        say({"dry_run_verdict": result["verdict"], "stopped": result.get("stopped"),
             "cases": [{"t": c["t"], "e": c["e"], "status": c["case_status"], "verified": c["load_bearing_verified"],
                        "of": c["load_bearing_unsat"], "bad_rows": [r["index"] for r in c["profiles"] if not r["ok"]]}
                       for c in result["cases"]],
             "controls_ok": (result["controls"] or {}).get("all_ok"), "guard": result["guard"]})
        return 0 if result["verdict"] == "PASS" else 1
    written = sum(p.stat().st_size for p in out.rglob("*") if p.is_file())
    result["bytes_in_output_dir_before_result"] = written
    write_json(out / args.result, result)
    say({"verdict": result["verdict"], "result": str(out / args.result), "stopped": result.get("stopped")})
    log.close()
    return 0 if result["verdict"] == "PASS" else 1


def smoke(folder, guard):
    """Converter + drat-trim negative/positive controls on the six LOWER46 conversion-smoke cases."""
    folder.mkdir(exist_ok=False)
    rows = []
    for p in sorted(SMOKE_SRC.glob("*.lrat")):
        gz = folder / (p.name + ".gz")
        with gz.open("xb") as f:
            f.write(gzip.compress(p.read_bytes(), mtime=0))
        cnf = p.with_suffix(".cnf").read_bytes()
        hdr = cnf.split(b"\n", 1)[0].split()
        r = check_rup(cnf, int(hdr[2]), int(hdr[3]), gz, guard, expect_gz_sha=sha_file(gz))
        r.pop("core")
        expected = p.name.startswith("unsat-")
        rows.append({"case": p.stem, "expected_verified": expected, "verified": r["verified"],
                     "statuses": r["statuses"], "checker_rc": r["checker_rc"],
                     "converter_rc": (r["converter_proc"] or {}).get("rc"), "ok": r["verified"] == expected})
    return {"source": str(SMOKE_SRC), "rows": rows, "all_ok": len(rows) == 6 and all(r["ok"] for r in rows)}


def controls(base, reports, guard, say):
    res = {"rule": ("core = drat-trim -c output on the unmodified text (read from a pipe, not stored); "
                    "MUT-DROP drops the first core clause in CNF order, MUT-FLIP negates that clause's first "
                    "literal; J-DROP drops J-family (officer/link) core clauses of (28,4) p0 in CNF order until "
                    "the first rejection, at most 6 attempts, all recorded. The rule was fixed after an in-memory "
                    "exploration showed that some single core-clause drops remain refutable by the same proof "
                    "(redundant derivations), which is not a checker defect.")}
    ok = True

    def proof_of(t, e, idx):
        pr = [p for p in reports[(t, e)]["profiles"] if p["index"] == idx][0]
        return pr, LANE / pr["final_proof"]["proof"], pr["final_proof"]["proof_gz_sha256"]

    def body_of(text):
        lines = text.split(b"\n")
        return lines[0], [ln for ln in lines[1:] if ln]

    def assemble(nv, body):
        return ("p cnf %d %d\n" % (nv, len(body))).encode() + b"\n".join(body) + b"\n"

    def core_indices(text, nv, m, gz, gsha, body):
        r = check_rup(text, nv, m, gz, guard, expect_gz_sha=gsha, want_core=True)
        index = {}
        for k, ln in enumerate(body):
            index.setdefault(tuple(sorted(map(int, ln.split()[:-1]))), k)
        core = r.pop("core") or b""
        keys = [tuple(sorted(map(int, ln.split()[:-1])))
                for ln in core.split(b"\n") if ln and ln[:1] not in (b"p", b"c")]
        idx = sorted(index[key] for key in keys if key in index)
        r["core_lines"], r["core_unmatched"] = len(keys), sum(key not in index for key in keys)
        return r, idx

    # (30,6) profile 1: drop / flip
    pr, gz, gsha = proof_of(30, 6, 1)
    text, meta = regenerate(base, pr["profile"], 30, 6, [], ["r2"])["r2"]
    _, body = body_of(text)
    base_run, cidx = core_indices(text, meta["variables"], meta["clauses"], gz, gsha, body)
    k = cidx[0]
    drop = assemble(meta["variables"], body[:k] + body[k + 1:])
    r1 = check_rup(drop, meta["variables"], meta["clauses"] - 1, gz, guard, expect_gz_sha=gsha)
    toks = body[k].split()
    toks[0] = str(-int(toks[0])).encode()
    flip = assemble(meta["variables"], body[:k] + [b" ".join(toks)] + body[k + 1:])
    r2 = check_rup(flip, meta["variables"], meta["clauses"], gz, guard, expect_gz_sha=gsha)
    res["t30_e6_p1"] = {"unmodified_sha256": meta["sha256"], "unmodified_verified": base_run["verified"],
                        "core_clauses": len(cidx), "chosen_clause_index0": k, "chosen_clause": body[k].decode(),
                        "MUT-DROP": {"sha256": r1["cnf_sha256"], "verified": r1["verified"],
                                     "statuses": r1["statuses"], "checker_rc": r1["checker_rc"],
                                     "expected": "rejected", "ok": not r1["verified"] and r1["statuses"] == [
                                         "s NOT VERIFIED"]},
                        "MUT-FLIP": {"sha256": r2["cnf_sha256"], "flipped_clause": b" ".join(toks).decode(),
                                     "verified": r2["verified"], "statuses": r2["statuses"],
                                     "checker_rc": r2["checker_rc"], "expected": "rejected",
                                     "ok": not r2["verified"] and r2["statuses"] == ["s NOT VERIFIED"]}}
    ok &= (base_run["verified"] and res["t30_e6_p1"]["MUT-DROP"]["ok"] and res["t30_e6_p1"]["MUT-FLIP"]["ok"])
    say({"control": "t30_e6_p1", "drop_rejected": res["t30_e6_p1"]["MUT-DROP"]["ok"],
         "flip_rejected": res["t30_e6_p1"]["MUT-FLIP"]["ok"]})
    # wrong e for the same profile
    wrong = {}
    for e2 in (5, 7):
        txt, mt = regenerate(base, pr["profile"], 30, e2, [], ["r2"])["r2"]
        wrong["e=%d" % e2] = {"sha256": mt["sha256"], "matches_report": mt["sha256"] == pr["final_cnf_sha256"]}
        del txt
    res["wrong_e_t30_p1"] = wrong
    ok &= not any(v["matches_report"] for v in wrong.values())
    del text, body, drop, flip
    # (28,4) profile 0: J sensitivity
    pr, gz, gsha = proof_of(28, 4, 0)
    text, meta = regenerate(base, pr["profile"], 28, 4, [], ["r2"])["r2"]
    _, body = body_of(text)
    base_run, cidx = core_indices(text, meta["variables"], meta["clauses"], gz, gsha, body)
    c = meta["counts"]
    lo, hi = c["base"], c["base"] + c["officer"] + c["link"]
    fam = Counter("base" if i < c["base"] else "officer" if i < c["base"] + c["officer"] else
                  "link" if i < hi else "lex" for i in cidx)
    attempts = []
    for i in [i for i in cidx if lo <= i < hi][:6]:
        txt = assemble(meta["variables"], body[:i] + body[i + 1:])
        r = check_rup(txt, meta["variables"], meta["clauses"] - 1, gz, guard, expect_gz_sha=gsha)
        attempts.append({"clause_index0": i, "family": "officer" if i < c["base"] + c["officer"] else "link",
                         "clause_prefix": body[i][:120].decode(), "verified": r["verified"],
                         "statuses": r["statuses"]})
        if not r["verified"]:
            break
    res["t28_e4_p0_J"] = {"unmodified_verified": base_run["verified"], "core_family_counts": dict(fam),
                          "attempts": attempts,
                          "ok": base_run["verified"] and any(not a["verified"] for a in attempts)}
    ok &= res["t28_e4_p0_J"]["ok"]
    say({"control": "t28_e4_p0_J", "ok": res["t28_e4_p0_J"]["ok"], "attempts": len(attempts)})
    res["all_ok"] = bool(ok)
    return res


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("convert")
    c.add_argument("gz")
    c.add_argument("maximum", type=int)
    c.add_argument("original", type=int)
    r = sub.add_parser("run")
    r.add_argument("--out", default="ame46-s48-parent-replay-v1")
    r.add_argument("--tag", required=True)
    r.add_argument("--case", action="append", required=True, help="T:E:REPORT_SHA256")
    r.add_argument("--receipt", required=True, help="LANE_REL_PATH:SHA256")
    r.add_argument("--result", default="result.json")
    r.add_argument("--controls", action="store_true")
    r.add_argument("--dry-run", action="store_true", help="write nothing; read lane inputs in place; no smoke")
    a = ap.parse_args()
    if a.cmd == "convert":
        convert(a.gz, a.maximum, a.original)
        return 0
    return run(a)


if __name__ == "__main__":
    raise SystemExit(main())
