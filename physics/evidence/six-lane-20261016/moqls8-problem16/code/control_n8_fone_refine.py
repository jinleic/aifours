"""Producer-side static controls only; NEVER invokes native solvers/checkers or
mints an admission. All potential child hashes are PLANNED, not measured feeds.
The two-level cover is checked for every possible L1-refinement subset and all
64 valuations; five corrupted wire/cover fixtures must be rejected separately.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'evidence/n8_fone_refine_static_v2'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'code' / (name + '.py'))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def make_json(path, obj):
    raw = json.dumps(obj, indent=1).encode()
    with path.open('xb') as f:
        f.write(raw)
    return sha(raw)


def main():
    start = time.monotonic()
    free = shutil.disk_usage(ROOT).free
    used = int(subprocess.run(['du', '-sk', str(ROOT)], capture_output=True, text=True, check=True).stdout.split()[0]) * 1024
    if free - 500000 < 12200000000 or used + 500000 > 10200547328:
        raise SystemExit('DEFERRED static stage: fresh disk/lane gate failed; no native stage')
    B = load('n8_fone_refine_bytes')
    F = load('n8_one_p4_formula')
    T = load('run_n8_fone_refine')
    R = load('k5_resplit_r2')
    C = load('k5_cover')
    pins = {n: sha((ROOT / 'code' / (n + '.py')).read_bytes()) for n in
            ('n8_fone_refine_bytes', 'n8_one_p4_formula', 'run_n8_fone_refine', 'k5_resplit_r2', 'k5_cover', 'control_n8_fone_refine')}
    assert pins['n8_one_p4_formula'] == T.F_SHA
    assert pins['k5_resplit_r2'] == T.R_SHA
    assert pins['k5_cover'] == T.C_SHA
    design, cases = B.load_inputs()
    base, recipe = F.build()
    assert base.sha == B.BASE_SHA == T.SOURCE_SHA
    assert (base.nv, base.nc) == (509915, 5740226)
    prefix = {}
    for count in (45, 48):
        h = hashlib.sha256(('p cnf %d %d\n' % (base.nv, base.nc + count)).encode())
        h.update(base.body)
        prefix[count] = h
    plans = {}
    for name, x in cases.items():
        assert base.leaf_sha(x['units']) == x['cnf_sha256']
        assert len({abs(u) for u in x['units']}) == 42
        for b in range(8):
            for c in [None] + list(range(8)):
                units = B.path_units(x['units'], b, c)
                count = 45 if c is None else 48
                assert units[:42] == x['units'] and len(units) == count
                assert B.header(units) == ('p cnf %d %d\n' % (base.nv, base.nc + count)).encode()
                # Direct serializer independent of Formula.leaf_sha's cache.
                suffix = b''.join((str(v) + ' 0\n').encode() for v in units)
                assert suffix == B.tail(units)
                h = prefix[count].copy()
                h.update(suffix)
                expected = h.hexdigest()
                assert expected == base.leaf_sha(units)
                node = name + '.L1.%03d' % b
                if c is not None:
                    node += '.L2.%03d' % c
                plans[node] = {'CNF_sha256_PLANNED': expected, 'units': count, 'clauses': base.nc + count}
    assert len(plans) == 1152
    idx = {v: i for i, v in enumerate(B.Z1 + B.Z2)}
    s1 = [B.signs(B.Z1, b) for b in range(8)]
    s2 = [B.signs(B.Z2, c) for c in range(8)]

    def failures(nodes):
        bad = []
        for val in range(64):
            count = sum(all(bool((val >> idx[abs(u)]) & 1) == (u > 0) for u in n) for n in nodes)
            if count != 1:
                bad.append({'valuation6bits_little_endian': val, 'matches': count})
        return bad

    for mask in range(256):
        nodes = []
        for b in range(8):
            nodes.extend([s1[b] + t for t in s2] if (mask >> b) & 1 else [s1[b]])
        assert not failures(nodes)
    mutations = []
    bad = failures(s1[1:])
    assert bad
    mutations.append({'name': 'missing_L1_000', 'rejected': True, 'first_failure': bad[0]})
    dup = [list(x) for x in s1]
    dup[0] = list(dup[1])
    bad = failures(dup)
    assert bad
    mutations.append({'name': 'L1_000_replaced_by_duplicate_001', 'rejected': True, 'first_failure': bad[0]})
    nodes = [list(x) for x in s1[1:]] + [s1[0] + x for x in s2]
    nodes[7] = list(nodes[7])
    nodes[7][3] *= -1
    bad = failures(nodes)
    assert bad
    mutations.append({'name': 'L2_000_first_bit_flipped', 'rejected': True, 'first_failure': bad[0]})
    fixture = list(next(iter(cases.values()))['units'])
    fixture[0] = -B.Z1[0]
    rejected = False
    try:
        B.path_units(fixture, 0)
    except ValueError:
        rejected = True
    assert rejected
    mutations.append({'name': 'template_unit_overlaps_Z1', 'rejected': True, 'reason': 'non-disjoint path rejected'})
    valid_units = B.path_units(next(iter(cases.values()))['units'], 0)
    bad_header = ('p cnf %d %d\n' % (base.nv, base.nc + len(valid_units) - 1)).encode()
    assert bad_header != B.header(valid_units)
    mutations.append({'name': 'header_clause_count_minus1', 'rejected': True, 'reason': 'not base_nc+45'})
    model_controls = {'positive': T.model_check('v 1 2 0\n', b'1 -2 0\n2 0\n', [1], 2),
                      'flipped_literal_rejected': not T.model_check('v -1 2 0\n', b'1 -2 0\n2 0\n', [1], 2),
                      'conflicting_literal_rejected': not T.model_check('v 1 2 -1 0\n', b'1 -2 0\n2 0\n', [1], 2),
                      'out_of_range_rejected': not T.model_check('v 1 2 3 0\n', b'1 -2 0\n2 0\n', [1], 2)}
    assert all(model_controls.values())
    capacity_controls = {'empty_positive': T.capacity_available({'foreign_RSS_bytes': 0, 'foreign_native_count': 0}),
                         'boundary8GiB4native_positive': T.capacity_available({'foreign_RSS_bytes': 2 * 2 ** 30, 'foreign_native_count': 2}),
                         '9GiB_projection_rejected': not T.capacity_available({'foreign_RSS_bytes': 3 * 2 ** 30, 'foreign_native_count': 1}),
                         '5native_projection_rejected': not T.capacity_available({'foreign_RSS_bytes': 1 * 2 ** 30, 'foreign_native_count': 3})}
    assert all(capacity_controls.values())
    OUT.mkdir(parents=True, exist_ok=True)
    ph = make_json(OUT / 'POTENTIAL_CHILD_HASHES.json', plans)
    result = {'schema': 'n8-fone-refinement-static-controls/2', 'host': datetime.now().astimezone().isoformat(),
              'status': 'PASS_PRODUCER_STATIC_ONLY', 'native_solver_or_checker_invoked': False,
              'admission_minted_or_guessed': False, 'source_pins': pins, 'design_sha256': B.DESIGN_SHA,
              'WMAN_sha256': B.WMAN_SHA, 'base_sha256': base.sha, 'base_body_sha256': sha(base.body),
              'source16_root_hashes_matched': 16, 'potential_child_images_checked': 1152,
              'potential_hash_file_sha256': ph, 'L1_refinement_masks_checked': 256,
              'valuations_per_mask': 64, 'total_exact_partition_checks': 16384,
              'wire_mutations': mutations, 'model_checker_controls': model_controls,
              'synthetic_capacity_predicate_controls': capacity_controls,
              'delivered_solver_feed_sha256': None, 'delivered_checker_feed_sha256': None,
              'scope': 'producer byte/Boolean-cover controls only; not an independent final verifier or physical exclusion',
              'authority': 'parent separately measured-feed replay ONLY counts terminal refutations',
              'new_CNF_or_proof_files': False, 'source_gram_a_rerun': False,
              'fresh_free_bytes': free, 'fresh_lane_bytes': used, 'active_seconds': time.monotonic() - start}
    rh = make_json(OUT / 'RESULT.json', result)
    print(json.dumps({'RESULT_sha256': rh, 'potential_hash_file_sha256': ph, 'source_pins': pins,
                      'status': result['status'], 'seconds': result['active_seconds'], 'native_run': False}), flush=True)


if __name__ == '__main__':
    main()
