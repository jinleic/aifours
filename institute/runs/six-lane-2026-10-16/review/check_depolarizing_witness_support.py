"""Discharge review finding M1: exact index-level witness premises for the depolarizing certificate.

Usage: check_depolarizing_witness_support.py WITNESS.json EXPECTED_RAW_SHA256 EXPECTED_CANONICAL_SHA256 OUTPUT.json
Checks (no floating-point comparison is used for support: hex floats are decoded exactly and compared to 0):
  supp(a_i) subset of {x : x = r_i mod k}; r_i pairwise distinct mod k; k >= 2; K = max len(a_i) - 1 <= M;
  every amplitude real; weights q_i positive rationals summing to 1.
"""
from datetime import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def fail(reason):
    raise SystemExit(f'FAIL: {reason}')


def main():
    if len(sys.argv) != 5:
        raise SystemExit(__doc__)
    path, raw_expected, canon_expected, out = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
    if out.exists():
        fail('refusing to overwrite prior evidence')
    raw = path.read_bytes()
    obj = json.loads(raw)
    raw_sha = hashlib.sha256(raw).hexdigest()
    canon_sha = hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()
    if raw_sha != raw_expected or canon_sha != canon_expected:
        fail(f'hash mismatch raw={raw_sha} canonical={canon_sha}')
    k, residues, M = obj.get('k'), obj.get('residues'), int(obj['M'])
    if not isinstance(k, int) or k < 2:
        fail(f'k must be an integer >= 2, got {k!r}')
    rows = obj['amps']
    if not isinstance(residues, list) or len(residues) != len(rows):
        fail('one residue per amplitude row required')
    if len({r % k for r in residues}) != len(residues):
        fail('residues not pairwise distinct mod k')
    weights = [Fraction(q) for q in obj['q']]
    if len(weights) != len(rows) or sum(weights) != 1 or min(weights) <= 0:
        fail('weights must be positive rationals summing to 1, one per row')
    details = []
    for i, row in enumerate(rows):
        if row and isinstance(row[0], list):
            fail(f'row {i} is complex; real witness required for this certificate path')
        values = [float.fromhex(a) for a in row]
        support = [x for x, value in enumerate(values) if value != 0.0]
        off = [x for x in support if x % k != residues[i] % k]
        if off:
            fail(f'row {i} has support outside residue class {residues[i]} mod {k}: first {off[:5]}')
        if not support:
            fail(f'row {i} is identically zero')
        details.append({'row': i, 'residue': residues[i], 'length': len(values), 'support_size': len(support),
                        'max_support_index': max(support)})
    K = max(len(row) for row in rows) - 1
    if K > M:
        fail(f'K={K} exceeds M={M}')
    result = {'status': 'M1_WITNESS_PREMISES_PASS', 'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'witness': str(path), 'raw_sha256': raw_sha, 'canonical_json_sha256': canon_sha,
              'k': k, 'residues': residues, 'weights': [str(q) for q in weights], 'M': M, 'K': K,
              'loss_chain_width': K + 1, 'real_witness': True, 'rows': details}
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
