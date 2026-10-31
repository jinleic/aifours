#!/usr/bin/env python3
"""Independent structural and exact-PSD audit of Tomar v3's *uncorrected* d=4 data.

No package verifier/construction code is imported or executed. The public data are
unpickled with global/class loading forbidden. This checks the stored dyadic base
multipliers, not the corrected certificate identity or corrected multiplier PSD.
"""
import collections
import hashlib
import io
import json
import lzma
import os
import pickle
import tarfile
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(ROOT / 'frontier-20261028-python-deps'))
import flint

ARCHIVE = ROOT / 'frontier-20261028-tomar-release-ep3-v3.tar.gz'
OUT = ROOT / 'frontier-20261028-independent-d4-base-check-results.json'
ARCHIVE_SHA256 = '2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
MEMBER = 'release_ep3/certs/ep3_perd_d4.pkl.xz'
MEMBER_SHA256 = '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'


class DataOnlyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        raise pickle.UnpicklingError('global/class loading is forbidden')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sign_pattern_psd(nums, n):
    """Real symmetric integer A PSD iff every coefficient of det(tI+A) >= 0."""
    A = flint.fmpz_mat(n, n, nums)
    coeff = A.charpoly()  # det(tI-A), integer coefficients
    signed = [((-1) ** (n - i)) * int(coeff[i]) for i in range(n + 1)]
    return all(c >= 0 for c in signed), signed[0] > 0


def exact_schur_psd(nums, n):
    """Independent rational Schur elimination, including zero pivots/rows."""
    a = [[Fraction(nums[i * n + j]) for j in range(n)] for i in range(n)]
    while a:
        k = len(a)
        if any(a[i][i] < 0 for i in range(k)):
            return False
        for i in range(k):
            if a[i][i] == 0 and any(a[i][j] != 0 for j in range(k)):
                return False
        p = next((i for i in range(k) if a[i][i] > 0), None)
        if p is None:
            return True
        piv = a[p][p]
        keep = [i for i in range(k) if i != p]
        a = [[a[i][j] - a[i][p] * a[p][j] / piv for j in keep] for i in keep]
    return True


def parse_key(k):
    side, raw_cut, label = k.split('|')
    cut = tuple(int(t) for t in raw_cut.split(',')) if raw_cut else ()
    f, left, right = label.split('_')
    parse_partition = lambda x: () if x == 'e' else tuple(int(c) for c in x)
    return side, cut, (int(f[1:]), parse_partition(left), parse_partition(right))


def canonical_equalities():
    def parts(fam, sign, site_slot, order, aux_kind):
        site = ('S', site_slot, order, 'del')
        aux = ('A', site_slot, order, aux_kind)
        return fam, sign, [site, site, site, aux]
    return {
        'stiefel31': [parts('31', 1, 0, (1, 2, 3), 'stiefel_aux')],
        'stiefel22': [parts('22', 1, 0, (1, 2, 3), 'stiefel_aux')],
        'stiefel13': [parts('13', 1, 3, (0, 1, 2), 'stiefel_aux')],
        'aab': [parts('31', 1, 2, (0, 1, 3), 'del'),
                parts('22', -1, 2, (0, 1, 3), 'del')],
        'abb': [parts('22', 1, 1, (0, 2, 3), 'del'),
                parts('13', -1, 1, (3, 0, 2), 'del')],
    }


def structural_checks(pkg):
    errors = []
    kinds = collections.Counter()
    shapes = collections.Counter()
    allowed = {'31': sorted('aaab'), '22': sorted('aabb'), '13': sorted('bbba')}
    for i, t in enumerate(pkg['types']):
        n = t['r']
        kinds[t['kind']] += 1
        shapes[n] += 1
        if type(n) is not int or n < 1 or len(t['Znum']) != n * n:
            errors.append(f'type {i}: invalid multiplier shape')
            continue
        if any(type(x) is not int for x in t['Znum']) or type(t['Zexp']) is not int:
            errors.append(f'type {i}: noninteger dyadic data')
        if any(t['Znum'][a*n+b] != t['Znum'][b*n+a] for a in range(n) for b in range(n)):
            errors.append(f'type {i}: nonsymmetric multiplier')
        mods = t['modules']
        try:
            parsed = [parse_key(m) for m in mods]
            if len(parsed) != 4 or [a[0] for a in parsed] != ['S','S','S','A']:
                raise ValueError('module sides')
            if any(a[1] != parsed[0][1] for a in parsed):
                raise ValueError('different cuts on local factors')
            dims = []
            for side, cut, lab in parsed[:3]:
                keys, cmat = pkg['diagrams'][(4, cut)][lab]
                if not keys or len(cmat) != len(keys) or not cmat[0] or any(len(row) != len(cmat[0]) for row in cmat):
                    raise ValueError('diagram compression shape')
                if any(type(x) is not int for row in cmat for x in row):
                    raise ValueError('noninteger diagram compression')
                dims.append(len(cmat[0]))
            aux = pkg['aux'][mods[3]]
            if len(aux) != 16 or not aux[0] or any(len(row) != len(aux[0]) for row in aux):
                raise ValueError('auxiliary compression shape')
            if any(type(x) is not int for row in aux for x in row):
                raise ValueError('noninteger auxiliary compression')
            dims.append(len(aux[0]))
            rows = t['rows']
            product = 1
            for x in dims:
                product *= x
            if len(t['W']) != len(rows) * product or any(len(row) != n for row in t['W']):
                raise ValueError('joint compression shape')
            if any(type(x) is not int for row in t['W'] for x in row):
                raise ValueError('noninteger joint compression')
            cut = set(parsed[0][1])
            if t['kind'] == 'src':
                if len(rows) != 1 or t['family'] not in allowed:
                    raise ValueError('invalid single family')
                tokens = rows[0].split()
                if len(tokens) != 4 or any(x not in ('a','b','a*','b*') for x in tokens):
                    raise ValueError('invalid single row tokens')
                if sorted(x[0] for x in tokens) != allowed[t['family']]:
                    raise ValueError('single-row family mismatch')
                if {j for j,x in enumerate(tokens) if x.endswith('*')} != cut:
                    raise ValueError('single-row cut mismatch')
            elif t['kind'] == 'gram':
                if tuple(rows) != ('a a b a*','b b a b*') or cut != {3}:
                    raise ValueError('coupled Gram row/cut mismatch')
            elif t['kind'] == 'gram2':
                if tuple(rows) != ('a a a* b*','a b b* b*') or cut != {2,3}:
                    raise ValueError('Gram2 row/cut mismatch')
            else:
                raise ValueError('unknown block family')
        except (KeyError, TypeError, ValueError, IndexError) as exc:
            errors.append(f'type {i}: {exc}')
    expected = canonical_equalities()
    if set(pkg['eq_groups']) != set(expected):
        errors.append('equality group names mismatch')
    for name, want in expected.items():
        try:
            actual = pkg['eq_groups'][name]['parts']
            if len(actual) != len(want):
                raise ValueError('part count')
            for got, (family, sign, local) in zip(actual, want):
                if got['family'] != family or got['sign'] != sign:
                    raise ValueError('family/sign')
                sig = [(x[0], x[1], tuple(x[2]), x[3]) for x in got['local']]
                if sig != local:
                    raise ValueError('local slot/reordering/operator')
        except (KeyError, TypeError, ValueError, IndexError) as exc:
            errors.append(f'equality {name}: {exc}')
    return errors, dict(kinds), dict(sorted(shapes.items()))


def main():
    start = time.monotonic()
    raw_archive = ARCHIVE.read_bytes()
    if digest(raw_archive) != ARCHIVE_SHA256:
        raise ValueError('archive SHA256 differs from pinned file')
    with tarfile.open(fileobj=io.BytesIO(raw_archive), mode='r:gz') as t:
        item = t.getmember(MEMBER)
        if not item.isfile() or item.size > 2_000_000:
            raise ValueError('certificate member not a bounded regular file')
        member = t.extractfile(item).read()
    if digest(member) != MEMBER_SHA256:
        raise ValueError('certificate member SHA256 mismatch')
    decoded = lzma.decompress(member, memlimit=256*1024*1024)
    pkg = DataOnlyUnpickler(io.BytesIO(decoded)).load()
    if (pkg['format'], pkg['k'], pkg['d'], pkg['nrow']) != ('ep3-perd-v1',3,4,4675):
        raise ValueError('unexpected target/format metadata')
    errors, kinds, shapes = structural_checks(pkg)
    psd_bad, algorithms_disagree, positive_definite = [], [], 0
    for i,t in enumerate(pkg['types']):
        n, nums = t['r'], t['Znum']
        if len(nums) != n*n or any(nums[a*n+b] != nums[b*n+a] for a in range(n) for b in range(n)):
            psd_bad.append(i)
            continue
        char_pass, definite = sign_pattern_psd(nums, n)
        schur_pass = exact_schur_psd(nums, n)
        if not char_pass or not schur_pass:
            psd_bad.append(i)
        if char_pass != schur_pass:
            algorithms_disagree.append(i)
        positive_definite += bool(char_pass and definite)
    result = {
        'kind':'independent_exact_uncorrected_d4_certificate_data_audit',
        'archive_sha256':digest(raw_archive), 'archive_md5':hashlib.md5(raw_archive).hexdigest(),
        'member':MEMBER, 'member_sha256':digest(member), 'member_compressed_bytes':len(member),
        'member_decompressed_bytes':len(decoded), 'package_format':pkg['format'],
        'k':pkg['k'], 'd':pkg['d'], 'source_orbit_rows_metadata':pkg['nrow'],
        'type_count':len(pkg['types']), 'kind_counts':kinds, 'size_histogram':shapes,
        'equality_group_names':sorted(pkg['eq_groups']),
        'equality_multiplier_count':sum(len(v) for v in pkg['lam'].values()),
        'correction_row_count':len(pkg['R']), 'correction_column_count':len(pkg['S']),
        'structural_errors':errors, 'base_psd_fail_indices':psd_bad,
        'psd_algorithms_disagree_indices':algorithms_disagree,
        'base_positive_definite_count':positive_definite,
        'base_psd_singular_count':len(pkg['types'])-positive_definite-len(psd_bad),
        'methods':['independent canonical family/cut/equality tag and compression-shape checks',
                   'FLINT integer characteristic-polynomial coefficient signs',
                   'independent Python Fraction symmetric Schur-complement PSD elimination'],
        'flint_version':flint.__version__, 'elapsed_seconds':round(time.monotonic()-start,3),
        'scope':'Stored dyadic BASE multipliers only. Exact corrected multipliers, all-orbit identity, diagram map semantics and full EP3 remain unverified by this script.',
        'verdict':'PASS' if not errors and not psd_bad and not algorithms_disagree else 'FAIL'
    }
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result['verdict']=='PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
