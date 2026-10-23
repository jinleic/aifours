"""Definition-first Bhaskar Rao witness checker; imports no worker code.
CLI: FILE V B R K LAMBDA EXPECTED_SHA OUTPUT_JSON
Strict header 'BRD V B R K LAMBDA', exactlyV rows of exactlyB tokens from {-1,0,1}, single spaces and finalLF.
Repeated columns are permitted. Validity is checked by counting the positive/negative products directly.
"""
import hashlib
import json
import sys
from collections import Counter


class CertificateError(Exception):
    def __init__(self, reason, detail=''):
        super().__init__(reason)
        self.reason, self.detail = reason, detail


def parse(raw, params):
    v, b, r, k, lam = params
    if not raw.endswith(b'\n') or raw.endswith(b'\n\n'):
        raise CertificateError('final-LF')
    if b'\r' in raw or b'\t' in raw:
        raise CertificateError('forbidden-whitespace')
    lines = raw[:-1].split(b'\n')
    if len(lines) != v + 1:
        raise CertificateError('line-count')
    if lines[0] != ('BRD ' + ' '.join(map(str, params))).encode():
        raise CertificateError('header')
    M = []
    for i, line in enumerate(lines[1:]):
        toks = line.split(b' ')
        if len(toks) != b:
            raise CertificateError('row-length', str(i))
        if any(t not in (b'-1', b'0', b'1') for t in toks):
            raise CertificateError('alphabet', str(i))
        M.append([int(t) for t in toks])
    return M


def verify(M, params):
    v, b, r, k, lam = params
    if lam % 2:
        raise CertificateError('odd-lambda')
    for i, row in enumerate(M):
        if sum(x != 0 for x in row) != r:
            raise CertificateError('row-weight', str(i))
    for j in range(b):
        if sum(M[i][j] != 0 for i in range(v)) != k:
            raise CertificateError('column-weight', str(j))
    hist = Counter()
    for i in range(v):
        for t in range(i):
            p = [M[i][j] * M[t][j] for j in range(b)]
            pos, neg = p.count(1), p.count(-1)
            if pos != lam // 2 or neg != lam // 2:
                raise CertificateError('pair-sign-balance', '%d,%d: +%d -%d' % (t, i, pos, neg))
            hist[(pos, neg, p.count(0))] += 1
    cols = [tuple(M[i][j] for i in range(v)) for j in range(b)]
    return {'row_checks': v, 'column_checks': b, 'pair_checks': v * (v - 1) // 2,
            'pair_product_histogram': [{'plus': p, 'minus': n, 'zero': z, 'pairs': count}
                                       for (p, n, z), count in sorted(hist.items())],
            'distinct_columns': len(set(cols)), 'columns_containing_minus': sum(-1 in c for c in cols)}


def main():
    path, params, expected, out = sys.argv[1], list(map(int, sys.argv[2:7])), sys.argv[7], sys.argv[8]
    raw = open(path, 'rb').read()
    rec = {'file': path, 'params': params, 'sha256': hashlib.sha256(raw).hexdigest(),
           'checker_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}
    try:
        if rec['sha256'] != expected:
            raise CertificateError('sha256')
        M = parse(raw, params)
        rec.update(verify(M, params))
        rec['result'] = 'VALID'
    except CertificateError as e:
        rec.update({'result': 'INVALID', 'reason': e.reason, 'detail': e.detail})
    with open(out, 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))
    sys.exit(0 if rec['result'] == 'VALID' else 1)


if __name__ == '__main__':
    main()
