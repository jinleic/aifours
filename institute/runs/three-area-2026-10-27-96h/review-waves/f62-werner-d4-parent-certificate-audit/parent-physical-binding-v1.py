#!/usr/bin/env python3
"""Independent parent physical-row and equality-coordinate binding checks.

Reads certificate data only. Compares the inspected global checker's literal
row mapping to separately constructed physical scalar-factor multisets. This
is not a separate implementation of the full corrected orbit identity.
"""
import collections
import hashlib
import importlib.util
import io
import json
import lzma
import pickle
import tarfile
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart')
ARCHIVE = ROOT / 'frontier-20261028-tomar-release-ep3-v3.tar.gz'
CORRECTED = ROOT / 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
GLOBAL = ROOT / 'frontier-20261028-independent-d4-global-identity-check.py'
OUT = Path(__file__).with_name('parent-physical-binding-result-v1.json')
EXPECTED_ARCHIVE = '2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3'
EXPECTED_MEMBER = '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
EXPECTED_CORRECTED = 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
EXPECTED_GLOBAL = 'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d'
LETTERS = {'31': 'aaab', '22': 'aabb', '13': 'bbba'}


class DataOnly(pickle.Unpickler):
    def find_class(self, module, name):
        raise pickle.UnpicklingError('CLASS_FORBIDDEN')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def physical_factors(row, col):
    out = collections.Counter()
    a, b = row.split(), col.split()
    if len(a) != 4 or len(b) != 4:
        raise ValueError('ROW_LENGTH')
    for j, (x, y) in enumerate(zip(a, b)):
        if x not in ('a', 'b', 'a*', 'b*') or y not in ('a', 'b', 'a*', 'b*'):
            raise ValueError('ROW_TOKEN')
        if x.endswith('*') != y.endswith('*'):
            raise ValueError('STAR_MISMATCH')
        out[(x[0], 'i', j, x.endswith('*'))] += 1
        out[(y[0], 'j', j, not y.endswith('*'))] += 1
    return out


def mapped_factors(family, ket, bra):
    out = collections.Counter()
    for letter, (side, slot) in zip(LETTERS[family], ket):
        out[(letter, side, slot, False)] += 1
    for letter, (side, slot) in zip(LETTERS[family], bra):
        out[(letter, side, slot, True)] += 1
    return out


def module_dimension(pkg, side, name):
    if side == 'S':
        f, left, right = name.split('|')[-1].split('_')
        partition = lambda v: () if v == 'e' else tuple(map(int, v))
        _, matrix = pkg['diagrams'][(3, ())][(int(f[1:]), partition(left), partition(right))]
    elif side == 'A':
        matrix = pkg['aux'][name]
    else:
        raise ValueError('SIDE')
    r = len(matrix[0])
    if r < 1 or any(len(row) != r for row in matrix):
        raise ValueError('COMPRESSION_SHAPE')
    return r


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    archive = ARCHIVE.read_bytes(); corrected = CORRECTED.read_bytes()
    if sha(archive) != EXPECTED_ARCHIVE or sha(corrected) != EXPECTED_CORRECTED or sha(GLOBAL.read_bytes()) != EXPECTED_GLOBAL:
        raise ValueError('INPUT_HASH')
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as tf:
        member = tf.getmember('release_ep3/certs/ep3_perd_d4.pkl.xz')
        if not member.isfile() or member.size > 2_000_000:
            raise ValueError('MEMBER')
        raw = tf.extractfile(member).read()
    if sha(raw) != EXPECTED_MEMBER:
        raise ValueError('MEMBER_HASH')
    pkg = DataOnly(io.BytesIO(lzma.decompress(raw, memlimit=256 * 1024 * 1024))).load()
    corr = json.loads(lzma.decompress(corrected, memlimit=256 * 1024 * 1024))
    if (pkg['format'], pkg['k'], pkg['d'], corr['copies'], corr['dimension']) != ('ep3-perd-v1', 3, 4, 3, 4):
        raise ValueError('TARGET')
    if corr['source_member_sha256'] != EXPECTED_MEMBER:
        raise ValueError('SOURCE_BINDING')
    spec = importlib.util.spec_from_file_location('parent_mapping_under_test', GLOBAL)
    mapping = importlib.util.module_from_spec(spec);spec.loader.exec_module(mapping)
    checked = 0; distinct = set()
    for typ in pkg['types']:
        for row in typ['rows']:
            for col in typ['rows']:
                family, ket, bra = mapping.literal_rule(row, col)
                if physical_factors(row, col) != mapped_factors(family, ket, bra):
                    raise ValueError('PHYSICAL_FACTORS')
                distinct.add((row, col));checked += 1
    if len(pkg['types']) != 1237 or (checked, len(distinct)) != (1570, 17):
        raise ValueError('TYPE_COUNT')
    paired = {}
    for name in ('aab', 'abb'):
        parts = pkg['eq_groups'][name]['parts']
        if len(parts) != 2 or {part['sign'] for part in parts} != {-1, 1}:
            raise ValueError('EQUALITY_SIGN')
        for j in range(4):
            left, right = parts[0]['local'][j], parts[1]['local'][j]
            if left[0] != right[0] or left[4] != right[4]:
                raise ValueError('PAIRED_COMPRESSION_KEYS')
        paired[name] = True
    valid = 0
    for item in corr['equality_coefficients']:
        parts = pkg['eq_groups'][item['group']]['parts']
        ix = item['index']
        if len(ix) != 4 or any(type(j) is not int for j in ix):
            raise ValueError('LAMBDA_INDEX')
        for part in parts:
            if len(part['local']) != 4:
                raise ValueError('LOCAL_FACTORS')
            for j, spec in zip(ix, part['local']):
                side, _, _, _, names = spec
                size = sum(module_dimension(pkg, side, name) ** 2 for name in names)
                if not 0 <= j < size:
                    raise ValueError('LAMBDA_RANGE')
        valid += 1
    if valid != 329:
        raise ValueError('LAMBDA_COUNT')
    # The rule under test is not the physical reference. Flip one conjugation
    # in its mapped scalar factors and require inequality of the multisets.
    row, col = next(iter(distinct))
    family, ket, bra = mapping.literal_rule(row, col)
    broken = mapped_factors(family, ket, bra)
    term = next(iter(broken));broken[term] -= 1
    if not broken[term]:del broken[term]
    wrong = (*term[:3], not term[3]);broken[wrong] += 1
    if physical_factors(row, col) == broken:
        raise ValueError('CONJUGATION_CONTROL')
    result = {'verdict': 'PASS', 'archive_sha256': EXPECTED_ARCHIVE,
              'source_certificate_sha256': EXPECTED_MEMBER, 'corrected_data_sha256': EXPECTED_CORRECTED,
              'mapping_under_test_sha256': EXPECTED_GLOBAL, 'physical_row_pair_occurrences': checked,
              'distinct_physical_row_pairs': len(distinct), 'paired_equality_module_keys_equal': paired,
              'corrected_lambda_coordinates_valid_in_every_signed_part': valid,
              'conjugation_mutation_rejected': True,
              'method': 'Data-only unpickler; separately formed original complex scalar-factor multisets and actual ordered compression dimension/key validation.',
              'scope': 'Physical row reindexing/equality-coordinate binding only; full source-span, identity, PSD and mathematical implication remain separate.'}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with OUT.open('x', encoding='utf-8') as f:f.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
