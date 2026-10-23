#!/usr/bin/env python3
"""C21_ARCS_V1 catalogue generator for the CFR(6,21) common-parallel-line CRT family (lane cfr21, protocol
notes/offset-arcs-protocol-v1.txt). Prepared as source only; Main generates, checks and freezes the catalogue.

Usage (Main only; cwd = lane root):
    python3 code/gen_offset_arcs_c21v1.py OUTDIR WALL_SECONDS
OUTDIR must be a NEW directory strictly inside the cfr21 lane (os.mkdir, never reused). WALL_SECONDS is the
Main-chosen bound, 1..10800, enforced internally with a monotonic clock. Every file is opened exclusively ('x'):
  start.json                  written at once (arguments, generator SHA-256, interpreter);
  catalog.txt + summary.json  only after every producer self-check passed (summary status COMPLETE-CATALOG);
  partial.json                on SIGTERM/SIGINT, wall expiry, self-check failure or exception: NOT a catalogue.
Exit codes: 0 complete; 2 refused (usage, WALL range, OUTDIR exists or lies outside the lane); 3 stopped by signal
or wall; 4 self-check failed; anything else = uncaught exception (partial.json best effort). Accept a catalogue only
with exit 0, summary.json status COMPLETE-CATALOG, the catalog.sha256 it records, and the C consumer's independent
validation. Pure stdlib Python, one process, imports no lane code: no solver import, no solver replay, no native work.

ABI (strict canonical decimals, single spaces, one LF per line including the last, no comments):
  C21_ARCS_V1
  N R S E
  N lines, IDs 0..N-1 in increasing function-vector order:  id P rep_id a b l f0 f1 f2 f3 f4 f5 f6
  R lines, increasing representative ID:                      rep_id stab_count a b l a b l ...
  E lines, sorted, duplicate-free:                            first_rep_id second_id
Only ARC functions get IDs. P = membership in P23. T_(a,b,l) maps the function to rep_id, the least element of its
G orbit (this producer picks the lexicographically least such (a,b,l); representatives get 1 0 1). Stabiliser lists
are complete, duplicate-free, lexicographic in (a,b,l). S = sum of stab_count. EXCLUDE lines are canonical pairs of
completed old-sampler inputs outside P23 x P23. No N*252 table and no case list is ever written.

Mathematics (every transformation acts on the whole projected matrix at once)
1. Representation. Rows i in F7, columns (t,c), t in {0,1,2}, c in F7:
       beta_i(t,c) = i*c + f_t(i) mod 7,   f_0 = 0,   f_t(0) = f_t(1) = 0 (t = 1,2).
   A normalised function is its vector (f(0),...,f(6)) with f(0) = f(1) = 0; there are 7^5 = 16807 of them. Vector
   order equals numeric order of code(f) = base-7 number f(2)f(3)f(4)f(5)f(6) (f(2) most significant).
2. ARC filter (necessary, a proof). In a cyclic (Z21,7;1)-DM any two columns x,y have seven pairwise distinct row
   differences D_i(x)-D_i(y): equality in rows i,j would give the row pair (i,j) the same difference at x and y. If
   four rows shared the mod-7 part beta_i(x)-beta_i(y), their mod-3 parts lie in F3, so two full differences agree:
   contradiction. Hence every mod-7 fibre has size <= 3. Inside one block the values i*(c-d), c != d, are distinct.
   Across blocks t != t' the values are g(i) - s*i with g = f_t - f_t' and s = d - c running over F7, where
   g in {+-f1, +-f2, +-(f1-f2)}; g at slope s and -g at slope -s have the same multiplicities. So:
       ARC(f) :<=> for every s in F7 no value of i -> f(i) - s*i has multiplicity > 3,
   and (f1,f2) is admissible iff ARC(f1), ARC(f2), ARC(f1-f2). f = 0 is not ARC (s = 0 gives multiplicity 7).
3. The group G of 252 actions (a,b,l), a,l in 1..6, b in 0..6. With phi(i) = a*i+b and the projection
   N(g)(i) = g(i) - g(0) - i*(g(1)-g(0)) that removes the affine part of g:
       T_(a,b,l)(f) = l*N(f o phi),   i.e.   T(f)(i) = l*(f(a*i+b) - f(b) - i*(f(a+b)-f(b))) mod 7.
   DM derivation (protocol): new row i := old row a*i+b; subtract row b from every column; multiply every entry by
   the CRT unit L (L = 1 mod 3, L = l mod 7); in block t re-index c' = l*a*c + l*K_t with K_t = f_t(a+b) - f_t(b):
       beta'_i(t,c') = l*(beta_{a*i+b}(t,c) - beta_b(t,c)) = l*(a*i*c + f_t(a*i+b) - f_t(b)) = i*c' + T(f_t)(i).
   Row permutations, subtracting a constant from a column, column permutations and multiplication by a unit of Z21
   preserve the cyclic (Z21,7;1)-DM property (cyclic arithmetic mod 21, never GF(21)) and map lifts of beta to
   lifts of beta' and back. These are validity-preserving DM operations, not CFR row-isotopy claims. T(0) = 0 keeps
   block 0. Facts used:
   * N is linear, kills affine functions, and N(N(g) o psi) = N(g o psi) for affine psi. Hence
         T_(a1,b1,l1) o T_(a2,b2,l2) = T_(a1*a2, a2*b1+b2, l1*l2),    T_(a,b,l)^-1 = T_(1/a, -b/a, 1/l),
     so the 252 maps form a group acting F7-linearly on the 5-dimensional space V of normalised functions
     (faithfully, already on P23 below), and T(f)(0) = T(f)(1) = 0.
   * ARC is G-invariant: with j = a*i+b, T(f)(i) - s*i = l*(f(j) - s'*j) + const where s' = (l*K + s)/(a*l),
     K = f(a+b) - f(b), and s -> s' is a bijection of F7. Linearity gives T(f1) - T(f2) = T(f1 - f2), so
     admissibility of pairs is G-invariant.
   * P23 = {u*(i^2-i) + v*(i^3-i) : u,v in F7} (49 normalised functions) is a G-invariant subspace:
         T(i^2-i) = l*a^2*(i^2-i),    T(i^3-i) = l*(a^3*(i^3-i) + 3*a^2*b*(i^2-i)).
     Every nonzero element is ARC (f(i) - s*i is a nonconstant polynomial of degree <= 3, so each value has at most 3
     preimages). They form two orbits: v = 0 (size 6, stabiliser l*a^2 = 1, order 42) and v != 0 (size 42: for each
     a exactly one (b,l) maps (u,v) to a given (u',v'), stabiliser order 6).
   * Burnside cross-check. On the monomials i^2..i^6 (mod affine) T is triangular with diagonal l*a^k. Fixed spaces:
     identity 7^5; a = 1, b != 0, l = 1: 7 (span of i^2); a = 1, l != 1: 1; a != 1 (a translation conjugates to
     b = 0): 7^#{k in 2..6 : l*a^k = 1}. The sum is 21672 = 252*86, so by hand V has 86 orbits. The program does NOT
     rely on this number: it compares sum_g 7^(5 - rank(T_g - I)) (exact rank over F7) with 252 times the number of
     enumerated orbits and only records the hand value.
4. Representatives, normalisers, stabilisers. Orbits are enumerated over all of V in increasing code order; the
   first unvisited function is the least element of its orbit (checked). For each member h the normaliser is the
   lexicographically least (a,b,l) with T(h) = rep, computed as the least inverse among the actions mapping rep to h
   and then re-verified by direct evaluation for every one of the 16807 functions. The stabiliser of a representative
   is the list of ALL (a,b,l) with T(rep) = rep from direct evaluation of the 252 actions; |orbit|*|stab| = 252 and
   disjointness/coverage of the orbits are checked, as is G-invariance of ARC on every orbit.
5. Block orders. For s in S3 the pair (f1,f2) (with f0 = 0) becomes (f_s1 - f_s0, f_s2 - f_s0): permute the three
   column blocks and subtract the row constant f_s0(i) (mod-7 part; mod-3 part 0) from row i, which shifts each
   row-pair difference multiset by a constant. G commutes with these maps (T linear, T(0) = 0), so the full group is
   G x S3 and the canonical pair is the least ID pair of the orbit:
       min over s of ( rep(g1), min_{sigma in Stab(rep(g1))} ID(sigma(T_n(g2))) ),   (g1,g2) the re-based pair,
   n any normaliser of g1 (the inner minimum does not depend on n). The six orders are compared lexicographically.
   P23 x P23 is mapped to itself (linear subspace), so the P23 exclusion is invariant under every equivalence.
6. Exclusions (never fabricated; a missing justification becomes an explicit HOLE, i.e. redundant re-testing,
   never a skipped case).
   * P23: every pair with both offsets in P23 is always excluded by the consumer via the P flag and is never listed
     in EXCLUDE. Recorded provenance only: runs/crt3-common-all-v1/record.json (pinned), the exact-solver scan of
     all 2401 P23 x P23 patterns, single-program restricted evidence.
   * Old sampler code/crt3_affine_sample_c21v1.py, run runs/crt3-seed21001-v1 (seed 21001, 43628 completed draws).
     The draw stream is replayed input-only with random.Random(21001), mirroring the sampler's draw loop call for
     call (two shuffles of [2..6] unless family 2, then ten randrange(7) offsets for family 0 or two (u,v) pairs).
     Nothing is solved and no lane module is imported. The replay is trusted only if the pinned SHA-256 of the
     sampler, record.json, start.json and notes/crt-sample-resolution-v1.json match; record/start name that sampler,
     seed 21001 and 43628 draws; family and verdict tallies are consistent; and every recorded pattern checkpoint
     (runs/crt3-seed21001-v1/example-*.json, runs/crt3-timeout-replay-v1/pattern-index43627.json) equals the replayed
     draw field by field, with checkpoints at the last draw and in every family. Only literal draws whose two slope
     permutations are the identity are members of this family (draws with other slopes are never claimed to be
     equivalent and are never excluded). For literal draws:
       both offsets in P23            -> left to the P23 rule (counted only);
       not admissible (ARC fails)     -> not a production case (listed, nothing to exclude);
       admissible, not both in P23    -> EXCLUDE its canonical pair iff record.json shows every draw of its family
                                         with verdict EXHAUSTED-PATTERN (the sampler kept no per-draw verdicts);
                                         otherwise an exact HOLE naming the draw.
     Families 1 and 2 with identity slopes are P23 by construction, so non-P23 literal draws can only come from the
     affine-random family (identity slopes with probability 1/14400 per draw). A failed provenance check yields one
     HOLE covering all sampler-derived exclusions and no sampler EXCLUDE line.
7. Bounded run. SIGTERM/SIGINT only set a flag that is never reset; the flag and the wall deadline are polled at every
   phase boundary and every 1024 loop steps. A stop before the final write leaves start.json + partial.json and no
   catalog.txt. The final write blocks SIGTERM/SIGINT/SIGALRM, re-polls, writes catalog.txt (<= 8 MiB, re-read and
   hash-checked) and then summary.json (<= 1 MiB), and restores the signal mask.
8. Resources (estimate, not measured): N <= 16806 lines of <= 34 bytes, so catalog.txt < 0.6 MB; R <= 85; about
   1e5 action evaluations plus a 43628-draw replay; seconds of CPU and tens of MiB RSS in one process.
No claim of existence, nonexistence or novelty is made by this program or its outputs.
"""
import collections
import hashlib
import itertools
import json
import os
import platform
import random
import re
import resource
import signal
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

NFUNC = 7 ** 5
GROUP_ORDER = 252
MAGIC = "C21_ARCS_V1"
CATALOG_CAP = 8 * 1024 * 1024
SUMMARY_CAP = 1024 * 1024
INPUT_CAP = 1024 * 1024
WALL_MAX = 10800.0
POLL_EVERY = 1024
HAND_ORBITS_ON_V = 86

SEED = 21001
DRAWS = 43628
FAMILIES = ("affine-random", "polynomial23", "common-slope-polynomial23")
IDENTITY = list(range(7))

PROTOCOL = "notes/offset-arcs-protocol-v1.txt"
GATE_LOG = "logs/offset-source-wave-gate-v1.json"
SAMPLER = "code/crt3_affine_sample_c21v1.py"
SAMPLE_DIR = "runs/crt3-seed21001-v1"
SAMPLE_RECORD = SAMPLE_DIR + "/record.json"
SAMPLE_START = SAMPLE_DIR + "/start.json"
RESOLUTION = "notes/crt-sample-resolution-v1.json"
TIMEOUT_PATTERN = "runs/crt3-timeout-replay-v1/pattern-index43627.json"
P23_RECORD = "runs/crt3-common-all-v1/record.json"
PINS = {
    PROTOCOL: "cd7de0679b8c9d1b1d3ca3eb93c7ab88c734badaa721a8c48a7d7d79a4a76ec5",
    SAMPLER: "99b71aaf1a19d508ebd206a9ec87f0cbf307e02c608ff9b4f3ade1d782e695ab",
    SAMPLE_RECORD: "bd56ac83a37cd74d4663dcd940d7836ec6679c9b116fa964f79dd3b6e3b02dba",
    SAMPLE_START: "abdbeabae21fe65c64bb7449baec9607dfc8a3e9e324bdaff8ab2318d537a836",
    RESOLUTION: "0d333471f0eaa1d3e2fcc32a3c860e8ed95d02a0c4b51c623c698493505d8379",
    P23_RECORD: "4f3d1db33f1188decdbdb761e83432649fa9f215e4d1b8392572229d3e836e61",
}
SAMPLER_PINNED = (SAMPLER, SAMPLE_RECORD, SAMPLE_START, RESOLUTION)
RESOLUTION_KEYS = ("sampled_draws", "original_timeouts", "common_family_timeouts", "other_timeout_index",
                   "remaining_timeouts", "candidate_count", "scope")
SAMPLER_RULE = ("Input-only replay of %s (seed %d, %d draws). Literal identity-slope draws only: both offsets in P23 "
                "-> P23 rule; inadmissible -> not a production case; otherwise EXCLUDE the canonical pair iff "
                "record.json shows every draw of the family EXHAUSTED-PATTERN, else HOLE." % (SAMPLE_DIR, SEED, DRAWS))
STATUS_SCOPE = ("Producer self-checks passed. The C consumer must independently validate ARC membership and "
                "completeness, P flags, orbit minima, normalisers, complete stabilisers and EXCLUDE pairs before use. "
                "Restricted common-parallel-line CRT family only: no existence, nonexistence or novelty claim. "
                "P23 and sampler exclusions rest on recorded single-program solver evidence.")
USAGE = ("usage: gen_offset_arcs_c21v1.py OUTDIR WALL_SECONDS   (OUTDIR new, strictly inside the cfr21 lane; "
         "1 <= WALL_SECONDS <= 10800)")

ACTIONS = tuple((a, b, l) for a in range(1, 7) for b in range(7) for l in range(1, 7))
INVERSE = {g: (pow(g[0], -1, 7), (-g[1] * pow(g[0], -1, 7)) % 7, pow(g[2], -1, 7)) for g in ACTIONS}
TOKEN = re.compile(r"0|[1-9][0-9]*")
STOP = {"signal": None}


class Stopped(Exception):
    """SIGTERM/SIGINT flag or wall deadline observed; the run is incomplete."""


class CheckError(Exception):
    """A producer self-check failed; no catalogue is blessed."""


def need(cond, message):
    if not cond:
        raise CheckError(message)


def on_signal(signum, frame):
    if STOP["signal"] is None:
        STOP["signal"] = signum


def clock():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def dumps(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + "\n").encode("ascii")


def write_new(path, data):
    with open(path, "xb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())


def load_json(data):
    if data is None:
        return None
    try:
        return json.loads(data)
    except ValueError:
        return None


def as_dict(obj):
    return obj if isinstance(obj, dict) else {}


def histogram(values):
    return [[key, count] for key, count in sorted(collections.Counter(values).items())]


class Run:
    def __init__(self, root, outdir, wall):
        self.root = root
        self.outdir = outdir
        self.wall = wall
        self.t0 = time.monotonic()
        self.deadline = self.t0 + wall
        self.phase = "startup"
        self.phase_t = self.t0
        self.phase_seconds = {}
        self.progress = {}
        self.sources = {}
        self.generator_sha = None
        self.catalog_written = False
        self.completed = False

    def poll(self):
        if STOP["signal"] is not None:
            raise Stopped("signal %d received" % STOP["signal"])
        if time.monotonic() >= self.deadline:
            raise Stopped("wall limit %.3f s reached" % self.wall)

    def enter(self, phase):
        now = time.monotonic()
        self.phase_seconds[self.phase] = round(now - self.phase_t, 6)
        self.phase, self.phase_t = phase, now
        self.progress = {}
        self.poll()

    def read(self, rel):
        """Bytes of a small lane input, or None if refused/unreadable; the outcome is recorded in self.sources."""
        path = (self.root / rel).resolve()
        if self.root not in path.parents:
            self.sources[rel] = "REFUSED-OUTSIDE-LANE"
            return None
        try:
            with open(path, "rb") as fh:
                data = fh.read(INPUT_CAP + 1)
        except OSError as exc:
            self.sources[rel] = "UNREADABLE-" + type(exc).__name__
            return None
        if len(data) > INPUT_CAP:
            self.sources[rel] = "REFUSED-ABOVE-1MiB"
            return None
        self.sources[rel] = sha256(data)
        return data


def decode(k):
    return (0, 0, k // 2401 % 7, k // 343 % 7, k // 49 % 7, k // 7 % 7, k % 7)


def code(f):
    return (((f[2] * 7 + f[3]) * 7 + f[4]) * 7 + f[5]) * 7 + f[6]


def sub(f, g):
    return tuple((x - y) % 7 for x, y in zip(f, g))


def act(g, f):
    """T_(a,b,l)(f)(i) = l*(f(a*i+b) - f(b) - i*(f(a+b) - f(b))) mod 7."""
    a, b, l = g
    fb = f[b]
    slope = (f[(a + b) % 7] - fb) % 7
    return tuple((l * (f[(a * i + b) % 7] - fb - i * slope)) % 7 for i in range(7))


def is_arc(f):
    for s in range(7):
        count = [0] * 7
        for i in range(7):
            count[(f[i] - s * i) % 7] += 1
        if max(count) > 3:
            return False
    return True


def p23_functions():
    return {tuple((u * (i * i - i) + v * (i ** 3 - i)) % 7 for i in range(7)) for u in range(7) for v in range(7)}


def rank_mod7(rows):
    m = [list(row) for row in rows]
    rank = 0
    for col in range(len(m[0])):
        pivot = next((r for r in range(rank, len(m)) if m[r][col]), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        inv = pow(m[rank][col], -1, 7)
        m[rank] = [(x * inv) % 7 for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col]:
                factor = m[r][col]
                m[r] = [(x - factor * y) % 7 for x, y in zip(m[r], m[rank])]
        rank += 1
    return rank


def burnside_sum():
    """sum over G of |Fix_V(g)| = 7^(5 - rank(T_g - I)), T_g written on the unit functions u_2..u_6 of V."""
    total = 0
    for g in ACTIONS:
        rows = []
        for j in range(2, 7):
            image = act(g, tuple(1 if i == j else 0 for i in range(7)))
            rows.append([(image[i] - (1 if i == j else 0)) % 7 for i in range(2, 7)])
        total += 7 ** (5 - rank_mod7(rows))
    return total


def arc_flags(run):
    flags = bytearray(NFUNC)
    for k in range(NFUNC):
        if k % POLL_EVERY == 0:
            run.progress = {"code": k}
            run.poll()
        flags[k] = 1 if is_arc(decode(k)) else 0
    return flags


def check_p23(run, flags):
    p23 = p23_functions()
    need(len(p23) == 49, "P23 must consist of 49 distinct functions")
    for f in sorted(p23):
        run.poll()
        need(f[0] == 0 and f[1] == 0, "P23 function is not normalised")
        need(flags[code(f)] == (1 if any(f) else 0), "nonzero P23 functions must be ARC and zero must not be")
        for g in ACTIONS:
            need(act(g, f) in p23, "P23 is not G-invariant")
    return p23


def orbits_on_v(run, flags):
    """All G orbits on V in increasing code order: (rep code, orbit size, complete stabiliser) per orbit."""
    rep_code = [-1] * NFUNC
    norm = [None] * NFUNC
    orbits = []
    for k in range(NFUNC):
        if k % POLL_EVERY == 0:
            run.progress = {"code": k, "orbits": len(orbits)}
            run.poll()
        if rep_code[k] >= 0:
            continue
        f = decode(k)
        least = {}
        stab = []
        for g in ACTIONS:
            h = act(g, f)
            need(h[0] == 0 and h[1] == 0, "an action broke normalisation")
            hk = code(h)
            if hk == k:
                stab.append(g)
            gi = INVERSE[g]
            old = least.get(hk)
            if old is None or gi < old:
                least[hk] = gi
        need(min(least) == k, "representative is not the least element of its orbit")
        need(len(least) * len(stab) == GROUP_ORDER, "orbit-stabiliser identity fails")
        for hk, gi in least.items():
            need(rep_code[hk] < 0, "orbits overlap")
            need(flags[hk] == flags[k], "ARC is not G-invariant")
            rep_code[hk] = k
            norm[hk] = gi
        orbits.append((k, len(least), stab))
    return rep_code, norm, orbits


def check_normalisers(run, rep_code, norm):
    for k in range(NFUNC):
        if k % POLL_EVERY == 0:
            run.progress = {"code": k}
            run.poll()
        need(act(norm[k], decode(k)) == decode(rep_code[k]), "normaliser does not map a function to its representative")


def build_catalogue(flags, rep_code, norm, orbits, p23):
    arc_codes = [k for k in range(NFUNC) if flags[k]]
    id_of = [-1] * NFUNC
    for i, k in enumerate(arc_codes):
        id_of[k] = i
    funcs = [decode(k) for k in arc_codes]
    rep_id = [id_of[rep_code[k]] for k in arc_codes]
    norms = [norm[k] for k in arc_codes]
    pflag = [1 if f in p23 else 0 for f in funcs]
    reps = [(id_of[k], stab) for k, size, stab in orbits if flags[k]]
    need(all(r >= 0 for r in rep_id), "representative outside the ARC catalogue")
    need(all(rep_id[r] == r for r, _ in reps), "representative does not represent itself")
    need(all(norms[r] == (1, 0, 1) for r, _ in reps), "representative normaliser must be the identity")
    return id_of, funcs, rep_id, norms, pflag, reps


def make_canon(id_of, rep_id, norms, stabs):
    zero = (0,) * 7

    def canon(f1, f2):
        """Least (first_rep_id, second_id) over the G x S3 orbit of the admissible pair (f1, f2)."""
        blocks = (zero, f1, f2)
        best = None
        for s in itertools.permutations(range(3)):
            g1 = sub(blocks[s[1]], blocks[s[0]])
            g2 = sub(blocks[s[2]], blocks[s[0]])
            i1, i2 = id_of[code(g1)], id_of[code(g2)]
            need(i1 >= 0 and i2 >= 0, "block re-basing left the ARC catalogue")
            first = rep_id[i1]
            h2 = act(norms[i1], g2)
            second = min(id_of[code(act(sigma, h2))] for sigma in stabs[first])
            need(second >= 0, "stabiliser image left the ARC catalogue")
            if best is None or (first, second) < best:
                best = (first, second)
        return best

    return canon


def p23_basis(run):
    rec = as_dict(load_json(run.read(P23_RECORD)))
    fields = {key: rec.get(key) for key in ("total_family", "settled_cases", "unknown_indices", "verdicts", "status",
                                             "program_sha256", "solver_sha256")}
    return {
        "rule": "Protocol: every pair with both offsets in P23 is always excluded (consumer uses the P flag); such "
                "pairs are never listed in EXCLUDE.",
        "basis_record": P23_RECORD,
        "pin_ok": run.sources.get(P23_RECORD) == PINS[P23_RECORD],
        "record_fields": fields,
        "record_reports_complete_scan": bool(fields["total_family"] == 2401 and fields["settled_cases"] == 2401
                                             and fields["unknown_indices"] == []
                                             and fields["verdicts"] == {"EXHAUSTED-PATTERN": 2401}),
        "evidence_scope": "single-program exact-solver scan of the 2401 P23 x P23 patterns as recorded; "
                          "independent-certificate status is tracked in the lane README, not asserted here",
    }


def replay_draws(run):
    """Input-only replay of the draw loop of code/crt3_affine_sample_c21v1.py: same RNG calls, same order."""
    rng = random.Random(SEED)
    for index in range(DRAWS):
        if index % POLL_EVERY == 0:
            run.progress = {"draw": index}
            run.poll()
        typ = index % 3
        slopes = [list(range(7)) for _ in range(3)]
        for t in (1, 2):
            if typ != 2:
                tail = list(range(2, 7))
                rng.shuffle(tail)
                slopes[t] = [0, 1] + tail
        offsets = [[0] * 7 for _ in range(3)]
        coefficients = []
        for t in (1, 2):
            if typ == 0:
                for i in range(2, 7):
                    offsets[t][i] = rng.randrange(7)
            else:
                u, v = rng.randrange(7), rng.randrange(7)
                coefficients.append([u, v])
                for i in range(2, 7):
                    a = slopes[t][i]
                    offsets[t][i] = (u * (a * a - a) + v * (a ** 3 - a)) % 7
        yield index, FAMILIES[typ], slopes, offsets, coefficients


def beta_of(slopes, offsets):
    return [[(slopes[t][i] * c + offsets[t][i]) % 7 for t in range(3) for c in range(7)] for i in range(7)]


def pattern_matches(pattern, index, family, slopes, offsets, coefficients):
    return (pattern.get("q") == 7 and pattern.get("index") == index and pattern.get("family") == family
            and pattern.get("slopes") == slopes and pattern.get("offsets") == offsets
            and pattern.get("polynomial_coefficients") == coefficients
            and pattern.get("beta") == beta_of(slopes, offsets))


def provenance_hole(reason):
    return {"scope": "every literal identity-slope, admissible, non-P23 draw of %s (set not established)" % SAMPLE_DIR,
            "reason": reason,
            "consequence": "no sampler-derived EXCLUDE line; any such input stays a production case"}


def sampler_exclusions(run, flags, p23, canon):
    """Recover completed literal common-slope sampler inputs; returns (report, sorted canonical EXCLUDE pairs)."""
    report = {"rule": SAMPLER_RULE, "checks": {}, "holes": []}
    checks, holes = report["checks"], report["holes"]
    raw = {rel: run.read(rel) for rel in SAMPLER_PINNED}
    for rel in SAMPLER_PINNED:
        checks["pin " + rel] = run.sources.get(rel) == PINS[rel]
    record, start, note = (as_dict(load_json(raw[rel])) for rel in (SAMPLE_RECORD, SAMPLE_START, RESOLUTION))
    expected = {FAMILIES[t]: len(range(t, DRAWS, 3)) for t in range(3)}
    hist = record.get("histogram")
    hist_ok = isinstance(hist, list)
    per_family, per_verdict, exhausted = collections.Counter(), collections.Counter(), collections.Counter()
    for item in (hist if hist_ok else ()):
        signature = item.get("signature") if isinstance(item, dict) else None
        n = item.get("count") if isinstance(item, dict) else None
        if not (isinstance(signature, list) and len(signature) == 4 and signature[0] in FAMILIES
                and isinstance(signature[3], str) and isinstance(n, int) and n >= 0):
            hist_ok = False
            break
        per_family[signature[0]] += n
        per_verdict[signature[3]] += n
        if signature[3] == "EXHAUSTED-PATTERN":
            exhausted[signature[0]] += n
    checks["record seed is %d" % SEED] = record.get("seed") == SEED
    checks["start seed is %d" % SEED] = start.get("seed") == SEED
    checks["record names pinned sampler"] = record.get("sampler_sha256") == PINS[SAMPLER]
    checks["start names pinned sampler"] = start.get("sampler_sha256") == PINS[SAMPLER]
    checks["record draw count is %d" % DRAWS] = record.get("patterns") == DRAWS
    checks["record family tallies"] = record.get("families") == expected
    checks["histogram tallies"] = bool(hist_ok and dict(per_family) == expected
                                       and dict(per_verdict) == record.get("verdicts"))
    checks["resolution note names pinned record"] = bool(note.get("sample") == SAMPLE_DIR
                                                         and note.get("sample_record_sha256") == PINS[SAMPLE_RECORD])
    checks["resolution note draw count is %d" % DRAWS] = note.get("sampled_draws") == DRAWS
    all_exhausted = {fam: bool(hist_ok and exhausted[fam] == expected[fam]) for fam in FAMILIES}
    report.update({
        "sampler": SAMPLER,
        "seed": SEED,
        "draws": DRAWS,
        "family_draws": expected,
        "family_all_exhausted_in_record": all_exhausted,
        "recorded_python": record.get("python"),
        "replay_python": sys.version,
        "recorded_solver_sha256": record.get("solver_sha256"),
        "resolution_note": {key: note.get(key) for key in RESOLUTION_KEYS},
    })
    failed = sorted(name for name, ok in checks.items() if not ok)
    if failed:
        holes.append(provenance_hole("provenance checks failed: " + "; ".join(failed)))
        report["replay"] = "NOT RUN"
        return report, []

    checkpoints = collections.defaultdict(list)
    bad = []
    names = [SAMPLE_DIR + "/" + p.name for p in sorted((run.root / SAMPLE_DIR).glob("example-*.json"))]
    report["example_files"] = len(names)
    report["example_files_equal_histogram_signatures"] = len(names) == len(hist)
    for rel in names + [TIMEOUT_PATTERN]:
        obj = load_json(run.read(rel))
        pattern = obj if rel == TIMEOUT_PATTERN else as_dict(obj).get("pattern")
        index = pattern.get("index") if isinstance(pattern, dict) else None
        if isinstance(index, int) and 0 <= index < DRAWS:
            checkpoints[index].append((rel, pattern))
        else:
            bad.append(rel)
    digest = hashlib.sha256()
    literal, literal_p23 = collections.Counter(), collections.Counter()
    candidates = []
    matched = []
    for index, family, slopes, offsets, coefficients in replay_draws(run):
        digest.update(json.dumps([index, family, slopes, offsets, coefficients],
                                 separators=(",", ":")).encode("ascii") + b"\n")
        for rel, pattern in checkpoints.get(index, ()):
            ok = pattern_matches(pattern, index, family, slopes, offsets, coefficients)
            matched.append({"source": rel, "sha256": run.sources.get(rel), "index": index, "family": family,
                            "match": ok})
            if not ok:
                bad.append(rel)
        if slopes[1] == IDENTITY and slopes[2] == IDENTITY:
            literal[family] += 1
            f1, f2 = tuple(offsets[1]), tuple(offsets[2])
            if f1 in p23 and f2 in p23:
                literal_p23[family] += 1
            else:
                candidates.append((index, family, f1, f2))
    total = sum(len(found) for found in checkpoints.values())
    checks["replay checkpoints all match"] = bool(not bad and matched and len(matched) == total)
    checks["replay checkpoint at last draw"] = any(c["match"] and c["index"] == DRAWS - 1 for c in matched)
    checks["replay checkpoint in every family"] = {c["family"] for c in matched if c["match"]} == set(FAMILIES)
    report.update({
        "replay_inputs_sha256": digest.hexdigest(),
        "checkpoints": matched,
        "unusable_or_mismatched_checkpoints": sorted(set(bad)),
        "literal_identity_slope_draws": {fam: literal[fam] for fam in FAMILIES},
        "literal_both_offsets_in_p23": {fam: literal_p23[fam] for fam in FAMILIES},
    })
    failed = sorted(name for name, ok in checks.items() if not ok)
    if failed:
        holes.append(provenance_hole("replay validation failed: " + "; ".join(failed)))
        report["literal_non_p23_draws"] = "WITHHELD: replay not validated"
        return report, []

    entries = []
    pairs = set()
    for index, family, f1, f2 in candidates:
        arc = [bool(flags[code(f1)]), bool(flags[code(f2)]), bool(flags[code(sub(f1, f2))])]
        entry = {"index": index, "family": family, "f1": list(f1), "f2": list(f2), "arc_f1_f2_difference": arc}
        if not all(arc):
            entry["status"] = "NOT-IN-FAMILY (inadmissible: ARC fails; never a production case)"
        elif not all_exhausted[family]:
            entry["status"] = "HOLE"
            holes.append({"scope": "draw %d (%s) offsets f1=%s f2=%s" % (index, family, list(f1), list(f2)),
                          "reason": "record.json has non-EXHAUSTED verdicts in this family and no per-draw verdicts",
                          "consequence": "not excluded; stays a production case"})
        else:
            pair = canon(f1, f2)
            pairs.add(pair)
            entry["status"] = "EXCLUDED"
            entry["canonical_pair"] = list(pair)
            entry["basis"] = ("%s: all %d %s draws have verdict EXHAUSTED-PATTERN from the sampler's exact CRT/F3 "
                              "lift solver (recorded solver_sha256 %s); single-program evidence, not independently "
                              "certified" % (SAMPLE_RECORD, expected[family], family, record.get("solver_sha256")))
        entries.append(entry)
    report["literal_non_p23_draws"] = entries
    return report, sorted(pairs)


def serialise(funcs, pflag, rep_id, norms, reps, pairs):
    s_count = sum(len(stab) for _, stab in reps)
    out = [MAGIC, "%d %d %d %d" % (len(funcs), len(reps), s_count, len(pairs))]
    for i, f in enumerate(funcs):
        out.append(" ".join(map(str, (i, pflag[i], rep_id[i]) + norms[i] + f)))
    for r, stab in reps:
        out.append(" ".join(map(str, [r, len(stab)] + [x for g in stab for x in g])))
    for r, x in pairs:
        out.append("%d %d" % (r, x))
    return ("\n".join(out) + "\n").encode("ascii"), (len(funcs), len(reps), s_count, len(pairs))


def reparse(data, funcs, pflag, rep_id, norms, reps, pairs):
    """Strict round trip of the serialised bytes against the in-memory catalogue."""
    need(data.endswith(b"\n") and b"\r" not in data, "catalogue line endings")
    lines = data.decode("ascii").split("\n")[:-1]

    def ints(line):
        tokens = line.split(" ")
        need(all(TOKEN.fullmatch(t) for t in tokens), "non-canonical decimal token")
        return [int(t) for t in tokens]

    need(len(lines) >= 2 and lines[0] == MAGIC, "catalogue magic line")
    header = ints(lines[1])
    need(len(header) == 4, "catalogue header")
    n, r_count, s_count, e_count = header
    need(n == len(funcs) and r_count == len(reps) and e_count == len(pairs), "catalogue header counts")
    need(len(lines) == 2 + n + r_count + e_count, "catalogue line count")
    for i in range(n):
        need(ints(lines[2 + i]) == [i, pflag[i], rep_id[i]] + list(norms[i]) + list(funcs[i]), "function line %d" % i)
    total = 0
    previous = -1
    for j, (r, stab) in enumerate(reps):
        v = ints(lines[2 + n + j])
        need(len(v) >= 2 and v[0] == r > previous and v[1] == len(stab) >= 1 and len(v) == 2 + 3 * v[1],
             "stabiliser line %d" % j)
        need(v[2:] == [x for g in stab for x in g], "stabiliser actions %d" % j)
        previous = r
        total += v[1]
    need(total == s_count, "S must equal the sum of stabiliser counts")
    previous = None
    for j, pair in enumerate(pairs):
        v = tuple(ints(lines[2 + n + r_count + j]))
        need(len(v) == 2 and v == tuple(pair) and (previous is None or v > previous), "EXCLUDE line %d" % j)
        previous = v


def produce(run, argv):
    me = Path(__file__).resolve()
    run.generator_sha = sha256(me.read_bytes())
    generator = {"path": str(me.relative_to(run.root)), "sha256": run.generator_sha}
    clock_start = clock()
    write_new(run.outdir / "start.json", dumps({
        "clock": clock_start, "argv": list(argv), "wall_limit_s": run.wall, "generator": generator,
        "python": sys.version, "platform": platform.platform(), "pid": os.getpid(),
        "note": "start record only; a catalogue exists only with summary.json status COMPLETE-CATALOG"}))
    run.enter("sources")
    run.read(PROTOCOL)
    run.read(GATE_LOG)
    run.enter("arc-flags")
    flags = arc_flags(run)
    need(flags[0] == 0, "the zero function must not be ARC")
    run.enter("p23")
    p23 = check_p23(run, flags)
    run.enter("orbits")
    rep_code, norm, orbits = orbits_on_v(run, flags)
    run.enter("burnside")
    fixed_sum = burnside_sum()
    need(fixed_sum == GROUP_ORDER * len(orbits), "Burnside fixed-point sum disagrees with the orbit enumeration")
    run.enter("normalisers")
    check_normalisers(run, rep_code, norm)
    run.enter("catalogue")
    id_of, funcs, rep_id, norms, pflag, reps = build_catalogue(flags, rep_code, norm, orbits, p23)
    stabs = dict(reps)
    sizes = {r: GROUP_ORDER // len(stab) for r, stab in reps}
    p23_sizes = sorted(sizes[r] for r, _ in reps if pflag[r])
    need(p23_sizes == [6, 42], "the ARC part of P23 must be two orbits of sizes 6 and 42")
    canon = make_canon(id_of, rep_id, norms, stabs)
    run.enter("p23-basis")
    p23_report = p23_basis(run)
    run.enter("sampler-replay")
    sampler_report, pairs = sampler_exclusions(run, flags, p23, canon)
    run.enter("exclusion-check")
    for r, x in pairs:
        need(rep_id[r] == r, "EXCLUDE first entry is not a representative")
        need(id_of[code(sub(funcs[r], funcs[x]))] >= 0, "EXCLUDE pair is not admissible")
        need(not (pflag[r] and pflag[x]), "EXCLUDE pair lies in P23 x P23")
        need(canon(funcs[r], funcs[x]) == (r, x), "EXCLUDE pair is not canonical")
    run.enter("serialise")
    data, (n, r_count, s_count, e_count) = serialise(funcs, pflag, rep_id, norms, reps, pairs)
    need(len(data) <= CATALOG_CAP, "catalogue above 8 MiB")
    reparse(data, funcs, pflag, rep_id, norms, reps, pairs)
    cat_sha = sha256(data)
    holes = sampler_report["holes"]
    summary = {
        "status": "COMPLETE-CATALOG",
        "status_scope": STATUS_SCOPE,
        "abi": MAGIC,
        "catalog": {"file": "catalog.txt", "bytes": len(data), "sha256": cat_sha,
                    "N": n, "R": r_count, "S": s_count, "E": e_count},
        "exclude_pairs": [list(p) for p in pairs],
        "exclusion_status": "HOLES-RECORDED" if holes else "COMPLETE",
        "counts": {
            "normalised_functions": NFUNC,
            "arc_functions": n,
            "non_arc_functions": NFUNC - n,
            "orbits_on_all_normalised": len(orbits),
            "hand_derived_orbits_on_all_normalised": HAND_ORBITS_ON_V,
            "burnside_fixed_point_sum": fixed_sum,
            "arc_orbits": r_count,
            "stabiliser_entries": s_count,
            "p23_functions": len(p23),
            "p23_arc_functions": sum(pflag),
            "p23_arc_orbit_sizes": p23_sizes,
            "arc_orbit_size_histogram": histogram(sizes.values()),
            "arc_stabiliser_size_histogram": histogram(len(stab) for _, stab in reps),
            "all_normalised_orbit_size_histogram": histogram(size for _, size, _ in orbits),
        },
        "group": {
            "order": GROUP_ORDER,
            "action": "T(f)(i) = l*(f(a*i+b) - f(b) - i*(f(a+b)-f(b))) mod 7; a,l in 1..6; b in 0..6",
            "composition": "T(a1,b1,l1) o T(a2,b2,l2) = T(a1*a2, a2*b1+b2, l1*l2)",
            "normaliser_choice": "lexicographically least (a,b,l) with T(f) = rep; 1 0 1 for representatives",
            "stabiliser_order": "all (a,b,l) with T(rep) = rep, lexicographic",
            "block_orders": "(f1,f2) -> (f_s1-f_s0, f_s2-f_s0), f0 = 0, s in S3; canonical pair = least ID pair "
                            "over G x S3",
        },
        "p23_exclusion": p23_report,
        "sampler_exclusions": sampler_report,
        "pins": {rel: {"expected": pin, "observed": run.sources.get(rel), "ok": run.sources.get(rel) == pin}
                 for rel, pin in PINS.items()},
        "sources_sha256": run.sources,
        "generator": generator,
        "python": sys.version,
        "platform": platform.platform(),
        "clock_start": clock_start,
        "wall_limit_s": run.wall,
        "phase_seconds": run.phase_seconds,
    }
    run.enter("write")
    blocked = {signal.SIGTERM, signal.SIGINT, signal.SIGALRM}
    old_mask = signal.pthread_sigmask(signal.SIG_BLOCK, blocked)
    try:
        run.poll()
        write_new(run.outdir / "catalog.txt", data)
        run.catalog_written = True
        need(sha256((run.outdir / "catalog.txt").read_bytes()) == cat_sha, "catalog.txt re-read hash mismatch")
        summary["clock_end"] = clock()
        summary["elapsed_s"] = round(time.monotonic() - run.t0, 6)
        summary["peak_rss_ru_maxrss"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        summary["ru_maxrss_unit"] = "bytes on Darwin, KiB on Linux"
        blob = dumps(summary)
        need(len(blob) <= SUMMARY_CAP, "summary above 1 MiB")
        write_new(run.outdir / "summary.json", blob)
        run.completed = True
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)
    print(json.dumps({"status": "COMPLETE-CATALOG", "N": n, "R": r_count, "S": s_count, "E": e_count,
                      "catalog_sha256": cat_sha, "exclusion_status": summary["exclusion_status"],
                      "signal_after_completion": STOP["signal"]}), flush=True)


def finish_partial(run, status, reason, exit_code):
    blessed = "; catalog.txt exists but is NOT blessed" if run.catalog_written else ""
    obj = {
        "status": status,
        "complete_catalog": False,
        "reason": reason,
        "phase": run.phase,
        "progress": run.progress,
        "catalog_txt_written": run.catalog_written,
        "signal": STOP["signal"],
        "clock": clock(),
        "elapsed_s": round(time.monotonic() - run.t0, 6),
        "wall_limit_s": run.wall,
        "phase_seconds": run.phase_seconds,
        "generator_sha256": run.generator_sha,
        "sources_sha256": run.sources,
        "note": "NOT A CATALOG: nothing in this directory may be used as a C21_ARCS_V1 catalogue%s; rerun in a "
                "fresh OUTDIR." % blessed,
    }
    try:
        write_new(run.outdir / "partial.json", dumps(obj))
    except OSError:
        pass
    print(json.dumps({"status": status, "reason": reason, "phase": run.phase}), flush=True)
    return exit_code


def main(argv):
    if len(argv) != 3:
        print(USAGE, file=sys.stderr)
        return 2
    root = Path(__file__).resolve().parents[1]
    outdir = Path(argv[1]).resolve()
    try:
        wall = float(argv[2])
    except ValueError:
        wall = float("nan")
    if not 1.0 <= wall <= WALL_MAX or root not in outdir.parents:
        print(USAGE, file=sys.stderr)
        return 2
    for signum in (signal.SIGTERM, signal.SIGINT):
        signal.signal(signum, on_signal)
    run = Run(root, outdir, wall)
    try:
        os.mkdir(outdir)
    except OSError as exc:
        print("refused: OUTDIR must be a new directory inside the lane (%s)" % exc, file=sys.stderr)
        return 2
    try:
        produce(run, argv)
    except Stopped as exc:
        return finish_partial(run, "STOPPED-INCOMPLETE-NOT-A-CATALOG", str(exc), 3)
    except CheckError as exc:
        return finish_partial(run, "SELF-CHECK-FAILED-NOT-A-CATALOG", str(exc), 4)
    except BaseException as exc:
        if not run.completed:
            finish_partial(run, "ABORTED-NOT-A-CATALOG", repr(exc), 1)
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
