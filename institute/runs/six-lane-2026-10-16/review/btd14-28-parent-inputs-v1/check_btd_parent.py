"""Parent definition-first checker for a balanced ternary design witness. Standard library only; no worker code.

Usage: python3 -B check_btd_parent.py FILE V B RHO1 RHO2 R K LAMBDA EXPECTED_SHA256 OUTPUT_JSON

Strict format: first line "BTD V B RHO1 RHO2 R K LAMBDA"; then exactly V lines of B space-separated entries
from {0,1,2}; one final LF; no blank, comment, tab, CR or extra token. Checks every row composition, every
column sum and every distinct-row inner product directly from the matrix. Writes OUTPUT_JSON with mode x.
"""
import hashlib
import json
import sys


class CertificateError(Exception):
    def __init__(self, reason, detail=''):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


def parse(raw, V, B, params):
    if not raw.endswith(b'\n') or raw.endswith(b'\n\n'):
        raise CertificateError('final-LF')
    if b'\r' in raw or b'\t' in raw:
        raise CertificateError('forbidden-whitespace')
    lines = raw[:-1].split(b'\n')
    if len(lines) != V + 1:
        raise CertificateError('line-count', str(len(lines)))
    header = lines[0].decode('ascii', 'strict')
    if header != 'BTD ' + ' '.join(map(str, params)):
        raise CertificateError('header', header)
    M = []
    for i, line in enumerate(lines[1:]):
        toks = line.decode('ascii', 'strict').split(' ')
        if len(toks) != B:
            raise CertificateError('row-length', str(i))
        if any(t not in ('0', '1', '2') for t in toks):
            raise CertificateError('alphabet', str(i))
        M.append([int(t) for t in toks])
    return M


def check(M, V, B, rho1, rho2, R, K, lam):
    for i, row in enumerate(M):
        if row.count(1) != rho1 or row.count(2) != rho2:
            raise CertificateError('row-composition', str(i))
        if sum(row) != R:
            raise CertificateError('row-sum', str(i))
    for j in range(B):
        if sum(M[i][j] for i in range(V)) != K:
            raise CertificateError('column-sum', str(j))
    for i in range(V):
        for k in range(i):
            if sum(a * b for a, b in zip(M[i], M[k])) != lam:
                raise CertificateError('inner-product', '%d,%d' % (k, i))
    cols = [tuple(M[i][j] for i in range(V)) for j in range(B)]
    return {'distinct_columns': len(set(cols)),
            'column_types': sorted({(c.count(1), c.count(2)) for c in cols}),
            'repeated_column_groups': [sorted(j for j in range(B) if cols[j] == c)
                                       for c in sorted(set(cols)) if cols.count(c) > 1]}


def main():
    path = sys.argv[1]
    params = list(map(int, sys.argv[2:9]))
    expected, out = sys.argv[9], sys.argv[10]
    V, B, rho1, rho2, R, K, lam = params
    raw = open(path, 'rb').read()
    rec = {'file': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'params': params,
           'checker_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}
    try:
        if rec['sha256'] != expected:
            raise CertificateError('sha256-mismatch')
        M = parse(raw, V, B, params)
        rec.update(check(M, V, B, rho1, rho2, R, K, lam))
        rec['result'] = 'VALID'
    except CertificateError as e:
        rec['result'] = 'INVALID'
        rec['reason'] = e.reason
        rec['detail'] = e.detail
    with open(out, 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))
    sys.exit(0 if rec['result'] == 'VALID' else 1)


if __name__ == '__main__':
    main()
