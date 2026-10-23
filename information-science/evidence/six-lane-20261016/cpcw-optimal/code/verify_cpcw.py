#!/usr/bin/env python3
"""Standalone verifier for OPTIMAL (v,k,1) binary cyclically permutable constant-weight codes (= (v,k,1) optical
orthogonal codes with lambda_a = lambda_c = 1 of Johnson-bound size).  Stdlib only, written from the definition.

Usage: verify_cpcw.py CERT --v V --k K --sha256 HEX
  The expected v, k and the SHA-256 of the certificate bytes are REQUIRED; any mismatch is a rejection.

Certificate format (strict): line 1 "CPCW <v> <k>"; then exactly s = floor((v-1)/(k(k-1))) lines, each with k
distinct canonical decimal integers in [0,v) separated by single spaces; LF line endings; one final LF; nothing else.

Accepted iff all of:
  (F) format, header = CLI (v,k), SHA-256 = CLI, s lines, range, distinct elements per codeword;
  (D) the k(k-1)s ordered within-codeword differences are nonzero and pairwise distinct across the whole code;
  (C) cross-check: 0/1 sequences of length v have periodic autocorrelation <= 1 at every nonzero shift and
      periodic cross-correlation <= 1 at every shift;
  (P) cross-check: the cyclic development (s*v translates) contains every unordered pair of Z_v at most once and
      leaves exactly v*|U|/2 pairs uncovered, U = uncovered nonzero differences from (D).
The report lists U exactly (sorted), |U|, whether v/2 is in U for even v (it must be), and "perfect" if U is empty.
Exit status: 0 accepted, 1 rejected, 2 usage/IO error.  JSON report on stdout.
"""
import hashlib
import json
import re
import sys

_INT = re.compile(r"(0|[1-9][0-9]*)\Z")


class Reject(Exception):
    def __init__(self, check, reason):
        super().__init__(reason)
        self.check, self.reason = check, reason


def _int(tok, where):
    if not _INT.match(tok):
        raise Reject("F", "non-canonical integer %r at %s" % (tok, where))
    return int(tok)


def parse(data, ev, ek):
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise Reject("F", "not ASCII")
    if "\r" in text or "\t" in text or not text.endswith("\n"):
        raise Reject("F", "CR/TAB present or missing final LF")
    lines = text[:-1].split("\n")
    head = lines[0].split(" ")
    if len(head) != 3 or head[0] != "CPCW":
        raise Reject("F", "bad header %r" % lines[0])
    v, k = _int(head[1], "header v"), _int(head[2], "header k")
    if (v, k) != (ev, ek):
        raise Reject("F", "header (v,k)=(%d,%d) differs from expected (%d,%d)" % (v, k, ev, ek))
    if k < 2 or v <= k:
        raise Reject("F", "need 2 <= k < v")
    s = (v - 1) // (k * (k - 1))
    body = lines[1:]
    if len(body) != s:
        raise Reject("F", "expected s=%d codewords for an optimal (%d,%d,1) code, found %d" % (s, v, k, len(body)))
    code = []
    for idx, line in enumerate(body, start=2):
        toks = line.split(" ")
        if len(toks) != k:
            raise Reject("F", "line %d: expected %d integers" % (idx, k))
        cw = [_int(t, "line %d" % idx) for t in toks]
        if any(not 0 <= x < v for x in cw):
            raise Reject("F", "line %d: element outside [0,%d)" % (idx, v))
        if len(set(cw)) != k:
            raise Reject("F", "line %d: repeated element" % idx)
        code.append(cw)
    return v, k, s, code


def check_differences(v, code):
    seen = {}
    for i, cw in enumerate(code):
        for a in cw:
            for b in cw:
                if a != b:
                    d = (b - a) % v
                    if d in seen:
                        raise Reject("D", "difference %d occurs twice (codewords %d and %d)" % (d, seen[d], i))
                    seen[d] = i
    return sorted(d for d in range(1, v) if d not in seen)


def check_correlations(v, code):
    seqs = []
    for cw in code:
        x = [0] * v
        for b in cw:
            x[b] = 1
        seqs.append(x)
    for i, xi in enumerate(seqs):
        sup = [t for t in range(v) if xi[t]]
        for j, xj in enumerate(seqs):
            for sh in range(v):
                if i == j and sh == 0:
                    continue
                r = sum(xj[(t + sh) % v] for t in sup)
                if r > 1:
                    raise Reject("C", "%s-correlation %d at codewords %d,%d shift %d" % (
                        "auto" if i == j else "cross", r, i, j, sh))


def check_pairs(v, code, nunc):
    cover = bytearray(v * v)
    for cw in code:
        for t in range(v):
            dev = sorted((b + t) % v for b in cw)
            for x in range(len(dev)):
                for y in range(x + 1, len(dev)):
                    p = dev[x] * v + dev[y]
                    if cover[p]:
                        raise Reject("P", "pair {%d,%d} in two translates" % (dev[x], dev[y]))
                    cover[p] = 1
    missing = sum(1 for x in range(v) for y in range(x + 1, v) if not cover[x * v + y])
    if 2 * missing != v * nunc:
        raise Reject("P", "uncovered pairs %d != v*|U|/2 = %d" % (missing, v * nunc // 2))
    return missing


def main(argv):
    args = argv[1:]
    try:
        cert = args[0]
        opts = dict(zip(args[1::2], args[2::2]))
        ev, ek, esha = int(opts["--v"]), int(opts["--k"]), opts["--sha256"].lower()
        if len(args) != 7:
            raise KeyError
    except (IndexError, KeyError, ValueError):
        sys.stderr.write("usage: verify_cpcw.py CERT --v V --k K --sha256 HEX\n")
        return 2
    try:
        data = open(cert, "rb").read()
    except OSError as exc:
        sys.stderr.write("cannot read %s: %s\n" % (cert, exc))
        return 2
    sha = hashlib.sha256(data).hexdigest()
    rep = {"file": cert, "sha256": sha, "expected": {"v": ev, "k": ek, "sha256": esha}}
    try:
        if sha != esha:
            raise Reject("F", "SHA-256 mismatch")
        v, k, s, code = parse(data, ev, ek)
        rep.update(v=v, k=k, s=s)
        unc = check_differences(v, code)
        rep.update(D="pass", uncovered=unc, uncovered_count=len(unc), perfect=not unc)
        if v % 2 == 0:
            rep["half_v_uncovered"] = (v // 2) in unc
            if not rep["half_v_uncovered"]:
                raise Reject("D", "v/2 covered (impossible for a valid code)")
        check_correlations(v, code)
        rep["C"] = "pass"
        rep["uncovered_pairs"] = check_pairs(v, code, len(unc))
        rep["P"] = "pass"
        rep["verdict"] = "ACCEPT"
        print(json.dumps(rep, sort_keys=True))
        return 0
    except Reject as exc:
        rep.update(verdict="REJECT", failed_check=exc.check, reason=exc.reason)
        print(json.dumps(rep, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
