#!/usr/bin/env python3
"""Standalone verifier for cyclic (v,k,1) difference families (perfect (v,k,1) OOCs).

Written from the definition only (stdlib; imports nothing from the lane's search code).

Certificate format (strict):
    line 1:      "CDF <v> <k>"
    lines 2..n+1: k distinct integers in [0, v), separated by single spaces
    n = (v-1)/(k(k-1)); v = 1 (mod k(k-1)) is required (no short orbits).
    Integers are canonical decimals (no sign, no leading zeros); LF line endings; the file ends with exactly one
    LF after the last block line; no blank lines, comments, tabs, CR or trailing spaces.

Accepted iff all of:
    (F) format, block count, range and within-block distinctness;
    (D) the multiset of ordered differences b - b' (mod v), b != b' in the same block, equals Z_v minus {0},
        each nonzero residue exactly once;
    (P) cross-check: the cyclic development {B_i + t : 1 <= i <= n, t in Z_v} has n*v distinct blocks and covers
        every unordered pair of Z_v exactly once (a strictly cyclic S(2,k,v));
    (C) cross-check: the 0/1 sequences x_i[t] = [t in B_i] of length v have periodic autocorrelation <= 1 at every
        nonzero shift and periodic cross-correlation <= 1 at every shift.

Exit status: 0 accepted, 1 rejected, 2 usage/IO error. A JSON report goes to stdout.
"""
import hashlib
import json
import re
import sys

_INT = re.compile(r"(0|[1-9][0-9]*)\Z")


class Reject(Exception):
    def __init__(self, check, reason):
        super().__init__(reason)
        self.check = check
        self.reason = reason


def _parse_int(tok, where):
    if not _INT.match(tok):
        raise Reject("F", "non-canonical integer token %r at %s" % (tok, where))
    return int(tok)


def parse(data):
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise Reject("F", "file is not ASCII")
    if "\r" in text or "\t" in text:
        raise Reject("F", "CR or TAB present")
    if not text.endswith("\n"):
        raise Reject("F", "file does not end with LF")
    lines = text[:-1].split("\n")
    head = lines[0].split(" ")
    if len(head) != 3 or head[0] != "CDF":
        raise Reject("F", "bad header %r" % lines[0])
    v = _parse_int(head[1], "header v")
    k = _parse_int(head[2], "header k")
    if k < 2 or v <= k:
        raise Reject("F", "need 2 <= k < v, got v=%d k=%d" % (v, k))
    lam = k * (k - 1)
    if (v - 1) % lam != 0:
        raise Reject("F", "v=%d is not 1 mod k(k-1)=%d" % (v, lam))
    n = (v - 1) // lam
    body = lines[1:]
    if len(body) != n:
        raise Reject("F", "expected %d blocks for v=%d k=%d, found %d lines" % (n, v, k, len(body)))
    blocks = []
    for idx, line in enumerate(body, start=2):
        toks = line.split(" ")
        if len(toks) != k:
            raise Reject("F", "line %d: expected %d single-space-separated integers, got %r" % (idx, k, line))
        blk = [_parse_int(t, "line %d" % idx) for t in toks]
        for x in blk:
            if not 0 <= x < v:
                raise Reject("F", "line %d: element %d outside [0,%d)" % (idx, x, v))
        if len(set(blk)) != k:
            raise Reject("F", "line %d: repeated element in block %r" % (idx, blk))
        blocks.append(blk)
    return v, k, n, blocks


def check_differences(v, blocks):
    count = [0] * v
    for blk in blocks:
        for a in blk:
            for b in blk:
                if a != b:
                    count[(a - b) % v] += 1
    if count[0] != 0:
        raise Reject("D", "zero difference occurs")
    missing = [d for d in range(1, v) if count[d] == 0]
    repeated = [d for d in range(1, v) if count[d] > 1]
    if missing or repeated:
        raise Reject("D", "difference multiset is not Z_v\\{0} once each: %d missing (first %s), %d repeated "
                          "(first %s)" % (len(missing), missing[:5], len(repeated), repeated[:5]))
    return sum(count)


def check_pairs(v, blocks):
    seen = set()
    pair_count = bytearray(v * v)
    developed = 0
    for blk in blocks:
        for t in range(v):
            dev = sorted((b + t) % v for b in blk)
            key = tuple(dev)
            if key in seen:
                raise Reject("P", "developed block %r occurs twice" % (key,))
            seen.add(key)
            developed += 1
            for i in range(len(dev)):
                for j in range(i + 1, len(dev)):
                    p = dev[i] * v + dev[j]
                    if pair_count[p] >= 1:
                        raise Reject("P", "pair {%d,%d} lies in two developed blocks" % (dev[i], dev[j]))
                    pair_count[p] = 1
    uncovered = 0
    first = None
    for x in range(v):
        row = x * v
        for y in range(x + 1, v):
            if pair_count[row + y] != 1:
                uncovered += 1
                if first is None:
                    first = (x, y)
    if uncovered:
        raise Reject("P", "%d unordered pairs uncovered, first %r" % (uncovered, first))
    return developed, v * (v - 1) // 2


def check_correlations(v, blocks):
    seqs = []
    for blk in blocks:
        s = [0] * v
        for b in blk:
            s[b] = 1
        seqs.append(s)
    worst_auto = 0
    worst_cross = 0
    for i, xi in enumerate(seqs):
        support_i = [t for t in range(v) if xi[t]]
        for j, xj in enumerate(seqs):
            for s in range(v):
                if i == j and s == 0:
                    continue
                r = 0
                for t in support_i:
                    r += xj[(t + s) % v]
                if i == j:
                    if r > worst_auto:
                        worst_auto = r
                elif r > worst_cross:
                    worst_cross = r
                if r > 1:
                    kind = "auto" if i == j else "cross"
                    raise Reject("C", "%s-correlation %d > 1 for codewords %d,%d at shift %d" % (kind, r, i, j, s))
    return worst_auto, worst_cross


def verify_bytes(data):
    """Run F first; if the file parses, run D, P and C independently (none short-circuits another), so a
    corrupted family shows which of the three independent checks reject it."""
    report = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    try:
        v, k, n, blocks = parse(data)
    except Reject as exc:
        report.update({"verdict": "REJECT", "failed_check": exc.check, "reason": exc.reason, "F": "fail"})
        return 1, report
    report.update({"v": v, "k": k, "blocks": n, "F": "pass"})
    failures = []
    try:
        report["ordered_differences"] = check_differences(v, blocks)
        report["D"] = "pass"
    except Reject as exc:
        report["D"] = "fail: " + exc.reason
        failures.append(exc)
    try:
        developed, pairs = check_pairs(v, blocks)
        report.update({"developed_blocks": developed, "pairs_covered_once": pairs, "P": "pass"})
    except Reject as exc:
        report["P"] = "fail: " + exc.reason
        failures.append(exc)
    try:
        wa, wc = check_correlations(v, blocks)
        report.update({"max_auto_correlation_nonzero_shift": wa, "max_cross_correlation": wc, "C": "pass"})
    except Reject as exc:
        report["C"] = "fail: " + exc.reason
        failures.append(exc)
    if failures:
        report.update({"verdict": "REJECT", "failed_check": failures[0].check, "reason": failures[0].reason,
                       "failed_checks": "".join(f.check for f in failures)})
        return 1, report
    report["verdict"] = "ACCEPT"
    return 0, report


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: verify_cdf.py CERTIFICATE\n")
        return 2
    try:
        with open(argv[1], "rb") as fh:
            data = fh.read()
    except OSError as exc:
        sys.stderr.write("cannot read %s: %s\n" % (argv[1], exc))
        return 2
    status, report = verify_bytes(data)
    report["file"] = argv[1]
    print(json.dumps(report, sort_keys=True))
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv))
