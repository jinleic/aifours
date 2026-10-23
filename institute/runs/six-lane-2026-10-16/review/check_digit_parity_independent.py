"""Check the general Walsh-digit parity identity without importing worker code."""
from __future__ import annotations

import hashlib
import json
import random

N = 512


def rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            bit = row.bit_length() - 1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def hyperplane_basis(h: int) -> list[int]:
    pivot = (h & -h).bit_length() - 1
    return [(1 << i) ^ (((h >> i) & 1) << pivot)
            for i in range(9) if i != pivot]


def check_support(support: set[int]) -> dict:
    if len(support) != 256:
        raise ValueError('A control must be balanced')
    moments = [0] * 9
    for x in support:
        for i in range(9):
            if (x >> i) & 1:
                moments[i] ^= x
    # Direct character sums, not FWHT and not the worker's digit function.
    walsh = [sum((-1 if x in support else 1) *
                 (-1 if (a & x).bit_count() % 2 else 1) for x in range(N))
             for a in range(N)]
    digits = [((w // 4) % 16 >> 3) & 1 for w in walsh]
    parity_checks = 0
    for h in range(1, N):
        basis = hyperplane_basis(h)
        restricted = []
        for u in basis:
            beta_u = 0
            for i in range(9):
                if (u >> i) & 1:
                    beta_u ^= moments[i]
            row = sum((((beta_u & v).bit_count() % 2) << j)
                      for j, v in enumerate(basis))
            restricted.append(row)
        determinant = int(rank(restricted) == 8)
        for c in (0, 1):
            actual = sum(digits[a] for a in range(N)
                         if (a & h).bit_count() % 2 == c) % 2
            if actual != determinant:
                raise RuntimeError(f'Hyperplane digit parity failed at h={h},c={c}')
            parity_checks += 1
    return {'support_sha256': hashlib.sha256(bytes(int(x in support) for x in range(N))).hexdigest(),
            'hyperplanes_checked': parity_checks, 'max_abs_walsh': max(map(abs, walsh)),
            'negative_walsh_count': sum(w < 0 for w in walsh),
            'digit3_weight': sum(digits)}


def main() -> None:
    rng = random.Random(20261016)
    controls = [set(rng.sample(range(N), 256)) for _ in range(3)]
    # A complemented linear balanced function violates any attempt to omit the cap-28 premise
    # from the negative-sign version, but must satisfy the GENERAL digit identity.
    complement_linear = {x for x in range(N) if not (x & 1)}
    controls.append(complement_linear)
    records = [check_support(support) for support in controls]
    if records[-1]['negative_walsh_count'] != 1 or records[-1]['digit3_weight'] != 0:
        raise RuntimeError('The sign-versus-digit scope control did not discriminate')
    print(json.dumps({'status': 'PASS', 'method': 'Direct 512-by-512 character sums and bitset GF2 rank; no worker imports',
                      'controls': records, 'total_affine_hyperplanes_checked': sum(r['hyperplanes_checked'] for r in records),
                      'scope_control': 'Complemented linear f has one negative coefficient -512 but digit3=0 everywhere. The negative-sign theorem needs the cap premise.',
                      'limits': 'Finite controls for the general digit identity, not examples of balanced NL242 or a universal proof.'}, indent=2))


if __name__ == '__main__':
    main()
