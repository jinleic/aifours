#!/usr/bin/env python3
"""checker_b.py -- route B: explicit MOLS verification of a raw (Z_n,k;1) difference matrix.

Usage:
    python3 -I -B checker_b.py DM_FILE [--n N] [--k K] [--emit SQUARES_FILE]

Input ("raw DM"): plain ASCII, exactly k non-empty lines, each with exactly n
whitespace-separated integers in [0, n).  Line i is row D_i; position c is column c.
Strict grammar, so that the matrix is unambiguous:
  * the only bytes allowed are 0-9, space, TAB, LF, and CR immediately before LF;
  * lines without any token are ignored; every other line is one row, in file order;
  * n = token count of the first non-empty line; every row must have n tokens; k >= 2;
  * every token is a canonical decimal ("0" or no leading zero) with value < n;
  * --n / --k, when given, must equal the input's n / k.

Properties (all evaluated on explicit data):
  dm          for every row pair i < j the sorted list of (D_i(c) - D_j(c)) mod n,
              c = 0..n-1, equals list(range(n))  (sorting, not set sizes).
  latin       squares L_t[c][g] = (D_t(c) - D_0(c) + g) mod n, t = 1..k-1, are built
              as explicit n x n lists of ints; every row and every column of every
              square must have a collections.Counter equal to Counter(range(n)).
  orthogonal  for every pair of squares s < t an n x n boolean incidence table of the
              superimposed ordered pairs (L_s[c][g], L_t[c][g]) is filled cell by
              cell; PASS iff no ordered pair is met twice and all n*n entries are set.
Diagnostic bridge_agreement (cannot change the verdict): compares per pair the dm
verdict with the MOLS-side verdict that is equivalent to it -- row pair (0,t) with
"columns of L_t are Latin", row pair (s,t), 1 <= s < t, with "L_s orthogonal to
L_t"; the rows of every L_t are Latin for any D (each row is a cyclic shift).

Output: exactly one JSON line on stdout.
Exit status: 0 PASS (dm, latin and orthogonal all PASS); 1 FAIL (some property
FAILs); 2 MALFORMED (input unreadable or outside the grammar, --n/--k mismatch,
bad command line); 3 ERROR (--emit file cannot be created or written, internal
exception).  With exit status 2 or 3 no property verdict is reported.

--emit SQUARES_FILE: write the squares to a NEW file (open mode 'xb'; an existing
file is never touched): L_1, ..., L_{k-1} in this order, each as n lines (line c =
row c) of n integers separated by single spaces, one blank line between
consecutive squares, LF line ends, final LF.  The file is written before the
properties are evaluated, from the same in-memory squares that are then checked,
and is read back and compared byte for byte.
"""

import argparse
import hashlib
import json
import os
import sys
from collections import Counter

CHECKER = 'checker_b'
VERSION = '1'
WITNESS_CAP = 8  # at most this many witnesses per property in the JSON line

DIGITS = frozenset(b'0123456789')
BLANKS = frozenset(b' \t')
LF = 0x0A
CR = 0x0D


class Malformed(Exception):
    """The input violates the raw-DM grammar or the requested dimensions."""


def print_json(obj):
    sys.stdout.write(json.dumps(obj, separators=(',', ':')) + '\n')
    sys.stdout.flush()


class JsonArgumentParser(argparse.ArgumentParser):
    """Command-line errors still produce exactly one JSON line (exit status 2)."""

    def error(self, message):
        self.print_usage(sys.stderr)
        print_json({'checker': CHECKER, 'version': VERSION, 'verdict': 'MALFORMED', 'exit_code': 2,
                    'well_formed': False, 'reason': 'command line: ' + message})
        sys.exit(2)


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def self_sha256():
    with open(os.path.abspath(__file__), 'rb') as fh:
        return sha256_hex(fh.read())


def parse_raw_dm(data, want_n=None, want_k=None):
    """Return D as a list of k rows (lists of n ints), or raise Malformed."""
    line = 1
    size = len(data)
    for off in range(size):
        b = data[off]
        if b in DIGITS or b in BLANKS:
            continue
        if b == LF:
            line += 1
            continue
        if b == CR and off + 1 < size and data[off + 1] == LF:
            continue
        raise Malformed('disallowed byte 0x%02x at byte offset %d (line %d)' % (b, off, line))

    rows = []  # (physical line number, tokens) of the non-empty lines
    for lineno, raw in enumerate(data.split(b'\n'), start=1):
        if raw.endswith(b'\r'):
            raw = raw[:-1]
        tokens = raw.split()
        if tokens:
            rows.append((lineno, tokens))
    k = len(rows)
    if k < 2:
        raise Malformed('need at least 2 non-empty lines (rows), found %d' % k)
    n = len(rows[0][1])
    for lineno, tokens in rows:
        if len(tokens) != n:
            raise Malformed('line %d: expected %d integers (n is set by the first non-empty line), found %d'
                            % (lineno, n, len(tokens)))
    if want_n is not None and n != want_n:
        raise Malformed('dimension mismatch: input has n=%d but --n %d was required' % (n, want_n))
    if want_k is not None and k != want_k:
        raise Malformed('dimension mismatch: input has k=%d but --k %d was required' % (k, want_k))

    max_len = len(str(n - 1))
    D = []
    for lineno, tokens in rows:
        row = []
        for c, tok in enumerate(tokens):
            text = tok.decode('ascii')
            if len(text) > 1 and text[0] == '0':
                raise Malformed('line %d, column %d (0-based): non-canonical integer token %r (leading zero)'
                                % (lineno, c, text[:24]))
            if len(text) > max_len or int(text) >= n:
                raise Malformed('line %d, column %d (0-based): integer %s not in [0, %d)'
                                % (lineno, c, text[:24], n))
            row.append(int(text))
        D.append(row)
    return D


def build_squares(D, n):
    """The k-1 explicit squares L_t[c][g] = (D_t(c) - D_0(c) + g) mod n, t = 1..k-1."""
    D0 = D[0]
    squares = []
    for t in range(1, len(D)):
        Dt = D[t]
        squares.append([[(Dt[c] - D0[c] + g) % n for g in range(n)] for c in range(n)])
    return squares


def squares_text(squares):
    blocks = ['\n'.join(' '.join(str(v) for v in row) for row in sq) for sq in squares]
    return '\n\n'.join(blocks) + '\n'


def check_dm(D, n):
    """Every row pair i < j: the sorted differences must be exactly 0, 1, ..., n-1."""
    k = len(D)
    target = list(range(n))
    failing, witnesses = [], []
    for i in range(k):
        for j in range(i + 1, k):
            Di, Dj = D[i], D[j]
            tagged = sorted(((Di[c] - Dj[c]) % n, c) for c in range(n))
            if [d for d, _ in tagged] == target:
                continue
            failing.append([i, j])
            if len(witnesses) < WITNESS_CAP:
                w = {'rows': [i, j]}
                for p in range(n - 1):
                    if tagged[p][0] == tagged[p + 1][0]:
                        w['difference'] = tagged[p][0]
                        w['columns'] = [tagged[p][1], tagged[p + 1][1]]
                        break
                w['distinct_differences'] = 1 + sum(tagged[p][0] != tagged[p + 1][0] for p in range(n - 1))
                witnesses.append(w)
    return {'verdict': 'FAIL' if failing else 'PASS', 'pairs_checked': k * (k - 1) // 2,
            'failing_pairs': failing, 'witnesses': witnesses}


def repeated_symbol(line):
    """Smallest symbol occurring more than once in line, with its first two positions."""
    counts = Counter(line)
    for sym in sorted(counts):
        if counts[sym] > 1:
            return sym, [p for p, v in enumerate(line) if v == sym][:2]
    return None, []


def check_latin(squares, n):
    """Every row and every column of every square: its Counter must equal Counter(range(n))."""
    full = Counter(range(n))
    failing, details = [], []
    for t, sq in enumerate(squares, start=1):
        columns = [[sq[c][g] for c in range(n)] for g in range(n)]
        bad_rows = [c for c in range(n) if Counter(sq[c]) != full]
        bad_cols = [g for g in range(n) if Counter(columns[g]) != full]
        if not bad_rows and not bad_cols:
            continue
        failing.append(t)
        d = {'square': t, 'bad_rows': len(bad_rows), 'bad_columns': len(bad_cols)}
        if bad_rows:
            sym, pos = repeated_symbol(sq[bad_rows[0]])
            d['row_witness'] = {'row': bad_rows[0], 'symbol': sym, 'columns': pos}
        if bad_cols:
            sym, pos = repeated_symbol(columns[bad_cols[0]])
            d['column_witness'] = {'column': bad_cols[0], 'symbol': sym, 'rows': pos}
        details.append(d)
    return {'verdict': 'FAIL' if failing else 'PASS', 'squares_checked': len(squares),
            'failing_squares': failing, 'details': details}


def check_orthogonal(squares, n):
    """Every pair of squares: n x n boolean incidence table of superimposed ordered pairs."""
    m = len(squares)
    failing, witnesses = [], []
    for s in range(m):
        A = squares[s]
        for t in range(s + 1, m):
            B = squares[t]
            seen = [[False] * n for _ in range(n)]
            repeats = 0
            first = None
            for c in range(n):
                Ac, Bc = A[c], B[c]
                for g in range(n):
                    a, b = Ac[g], Bc[g]
                    if seen[a][b]:
                        repeats += 1
                        if first is None:
                            first = (a, b, c, g)
                    else:
                        seen[a][b] = True
            covered = sum(r.count(True) for r in seen)
            if repeats == 0 and covered == n * n:
                continue
            failing.append([s + 1, t + 1])
            if len(witnesses) < WITNESS_CAP and first is not None:
                a, b, c2, g2 = first
                c1, g1 = next((c, g) for c in range(n) for g in range(n) if A[c][g] == a and B[c][g] == b)
                witnesses.append({'squares': [s + 1, t + 1], 'pair': [a, b],
                                  'cells': [[c1, g1], [c2, g2]], 'distinct_pairs': covered})
    return {'verdict': 'FAIL' if failing else 'PASS', 'pairs_checked': m * (m - 1) // 2,
            'failing_pairs': failing, 'witnesses': witnesses}


def check_bridge(dm, latin, orth, k):
    """Diagnostic: the dm verdict of every row pair against its MOLS-side equivalent."""
    dm_fail = {tuple(p) for p in dm['failing_pairs']}
    col_fail = {d['square'] for d in latin['details'] if d['bad_columns']}
    row_fail = sorted(d['square'] for d in latin['details'] if d['bad_rows'])
    orth_fail = {tuple(p) for p in orth['failing_pairs']}
    mismatches = []
    if row_fail:
        mismatches.append('rows not Latin in squares %s (impossible for cyclic-shift rows)' % row_fail)
    for t in range(1, k):
        if ((0, t) in dm_fail) != (t in col_fail):
            mismatches.append('row pair (0,%d) vs columns of L_%d' % (t, t))
    for s in range(1, k):
        for t in range(s + 1, k):
            if ((s, t) in dm_fail) != ((s, t) in orth_fail):
                mismatches.append('row pair (%d,%d) vs L_%d orthogonal to L_%d' % (s, t, s, t))
    return {'verdict': 'FAIL' if mismatches else 'PASS', 'mismatch_count': len(mismatches),
            'mismatches': mismatches[:WITNESS_CAP]}


def finish(result, verdict, code, **extra):
    result.update(extra)
    result['verdict'] = verdict
    result['exit_code'] = code
    print_json(result)
    return code


def main(argv=None):
    ap = JsonArgumentParser(prog='checker_b.py', allow_abbrev=False,
                            description='Route B: explicit MOLS check of a raw (Z_n,k;1) difference matrix.')
    ap.add_argument('dm', help='raw DM file')
    ap.add_argument('--n', type=int, help='required order n (MALFORMED if different)')
    ap.add_argument('--k', type=int, help='required number of rows k (MALFORMED if different)')
    ap.add_argument('--emit', metavar='SQUARES_FILE',
                    help='also write the k-1 squares to this NEW file (exclusive create)')
    args = ap.parse_args(argv)

    result = {'checker': CHECKER, 'version': VERSION, 'verdict': None, 'exit_code': None,
              'checker_sha256': self_sha256(), 'input': args.dm}
    try:
        with open(args.dm, 'rb') as fh:
            data = fh.read()
    except OSError as exc:
        return finish(result, 'MALFORMED', 2, well_formed=False,
                      reason='cannot read input: %s: %s' % (type(exc).__name__, exc))
    result['input_sha256'] = sha256_hex(data)
    result['input_bytes'] = len(data)
    try:
        D = parse_raw_dm(data, args.n, args.k)
    except Malformed as exc:
        return finish(result, 'MALFORMED', 2, well_formed=False, reason=str(exc))
    k, n = len(D), len(D[0])
    result.update(well_formed=True, n=n, k=k, num_squares=k - 1)

    handle = None
    if args.emit is not None:
        try:
            handle = open(args.emit, 'xb')
        except OSError as exc:
            return finish(result, 'ERROR', 3,
                          reason='cannot create --emit file: %s: %s' % (type(exc).__name__, exc))

    squares = build_squares(D, n)

    if handle is not None:
        payload = squares_text(squares).encode('ascii')
        try:
            with handle:
                handle.write(payload)
            with open(args.emit, 'rb') as fh:
                written = fh.read()
        except OSError as exc:
            return finish(result, 'ERROR', 3,
                          reason='cannot write --emit file: %s: %s' % (type(exc).__name__, exc))
        if written != payload:
            return finish(result, 'ERROR', 3, reason='--emit file does not read back byte-identical')
        result['emit'] = {'path': args.emit, 'sha256': sha256_hex(written), 'bytes': len(written)}

    dm = check_dm(D, n)
    latin = check_latin(squares, n)
    orth = check_orthogonal(squares, n)
    bridge = check_bridge(dm, latin, orth, k)
    verdicts = {'dm': dm['verdict'], 'latin': latin['verdict'], 'orthogonal': orth['verdict']}
    ok = all(v == 'PASS' for v in verdicts.values())
    result['verdicts'] = verdicts
    result['properties'] = {'dm': dm, 'latin': latin, 'orthogonal': orth}
    result['diagnostics'] = {'bridge_agreement': bridge}
    if ok:
        result['summary'] = ('%d mutually orthogonal Latin squares of order %d '
                             '(bridge from a (Z_%d,%d;1) difference matrix)' % (k - 1, n, n, k))
        return finish(result, 'PASS', 0)
    result['summary'] = 'FAIL: ' + ', '.join(name for name, v in verdicts.items() if v != 'PASS')
    return finish(result, 'FAIL', 1)


if __name__ == '__main__':
    try:
        status = main()
    except Exception as exc:  # a crash must never look like FAIL (1) or PASS (0)
        print_json({'checker': CHECKER, 'version': VERSION, 'verdict': 'ERROR', 'exit_code': 3,
                    'reason': 'internal exception: %s: %s' % (type(exc).__name__, exc)})
        status = 3
    sys.exit(status)
