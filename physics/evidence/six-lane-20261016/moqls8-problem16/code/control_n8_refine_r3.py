"""STATIC integration controls; run only after Main source PASS.
No supervise()/R.certify(), Popen, native command or fake admission is used.
Owned-group OS lifecycle tests belong to the separately observed/pinned phys2
supervisor receipt3c77be50...99de; these controls do NOT re-test that lifecycle.
Fixtures are x-created and retained in this lane; never delete/reset them.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import types
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'evidence/n8_refine_r3_static_controls_v1'


def load(name):
    path = ROOT / 'code' / (name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rejected(fn):
    try:
        fn()
    except (RuntimeError, FileExistsError, FileNotFoundError):
        return True
    return False


def main():
    free = shutil.disk_usage(ROOT).free
    used = int(subprocess.run(['du', '-sk', str(ROOT)], capture_output=True, text=True, check=True).stdout.split()[0]) * 1024
    if free - 1000000 < 12200000000 or used + 1000000 > 10200547328:
        raise SystemExit('DEFERRED: static-controls fresh disk/lane gate failed')
    T = load('run_n8_fone_refine')
    A = load('launch_n8_fone_refine_r3')
    B = load('n8_fone_refine_bytes')
    # AST/data only: do NOT import/call the actual supervisor here.
    forbidden = {'kill', 'killpg', 'setsid', 'start_new_session', 'Popen'}
    for name in ('run_n8_fone_refine', 'launch_n8_fone_refine_r3'):
        tree = ast.parse((ROOT / 'code' / (name + '.py')).read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                f = node.func
                token = f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''
                assert token not in forbidden, (name, token)
                assert not any(k.arg == 'start_new_session' for k in node.keywords)
    pins = {n: sha((ROOT / 'code' / (n + '.py')).read_bytes()) for n in
            ('run_n8_fone_refine', 'launch_n8_fone_refine_r3', 'n8_fone_refine_bytes', 'control_n8_refine_r3',
             'k5_resplit_r2', 'k5_cover', 'n8_one_p4_formula')}
    assert pins['n8_fone_refine_bytes'] == '72a2737d944f6727ba2176de4def66f60164c989d0d4b833948f9f7cd1efa96c'
    assert pins['k5_resplit_r2'] == T.R_SHA and pins['k5_cover'] == T.C_SHA and pins['n8_one_p4_formula'] == T.F_SHA
    assert sha(A.SUPERVISOR.read_bytes()) == A.SUP_SHA
    OUT.mkdir()
    fixture_root = OUT / 'refines'
    family = fixture_root / 'P1-B1'
    identity = {'fixture_only': True}
    with patch.object(T, 'REFINES', fixture_root):
        T.prepare_directories(family, 'P1-B1', identity, 'fixture-source', True, True)
        T.prepare_directories(family, 'P1-B1', identity, 'fixture-source', False, False)
        init_again = rejected(lambda: T.prepare_directories(family, 'P1-B1', identity, 'fixture-source', True, True))
        family_again = rejected(lambda: T.prepare_directories(family, 'P1-B1', identity, 'fixture-source', False, True))
        wrong_identity = rejected(lambda: T.prepare_directories(family, 'P1-B1', {'wrong': True}, 'fixture-source', False, False))
        orphan = fixture_root / 'orphan'
        orphan.mkdir()
        orphan_rejected = rejected(lambda: T.prepare_directories(orphan, 'orphan', identity, 'fixture-source', False, False))
    assert init_again and family_again and wrong_identity and orphan_rejected

    # Stop-channel adapter: an in-memory fake probe tests ONLY delegation/control
    # flow, never a fake process status in a production or acceptance receipt.
    sentinel = ('fixture-alive', 123, {'fixture_only': True})
    fake = types.SimpleNamespace(probe=lambda pid: sentinel)
    stop = OUT / 'fixture-stop.json'
    obs = {'stop_requested': False}
    probe = A.make_stop_probe(fake, stop, obs)
    assert probe(12345) is sentinel
    T.new_json(stop, {'fixture_only': True})
    first_reject = rejected(lambda: probe(12345))
    cleanup_delegates = probe(12345) is sentinel
    assert first_reject and cleanup_delegates and obs['stop_requested']

    _, cases = B.load_inputs()
    units42 = cases['P1-B1']['units']
    plans = []
    for c in range(8):
        plans.append({'id': 'P1-B1.L1.000.L2.%03d' % c, 'level': 2, 'b': 0, 'c': c,
                      'ancestor': 'P1-B1.L1.000', 'state': 'UNSTARTED',
                      'units': B.path_units(units42, 0, c), 'receipt': None})
    nid = 'P1-B1.L1.000'
    fixture = {'status': 'OPEN', 'nodes': {nid: {'id': nid, 'level': 1, 'state': 'LEGACY_CANDIDATE',
                                              'planned_L2_children': plans, 'outer_completed_cleanly': None}}}
    pending_not_closed = not T.closure(fixture)
    positive = copy.deepcopy(fixture)
    A.qualify_node(positive, nid, True)
    positive_closed = T.closure(positive)
    negative = copy.deepcopy(fixture)
    A.qualify_node(negative, nid, False)
    unknown_refined = (negative['nodes'][nid]['state'] == 'REFINED' and len(T.leaves(negative)) == 8
                       and all(x['state'] == 'UNSTARTED' for x in T.leaves(negative)) and not T.closure(negative))
    l2 = {'status': 'OPEN', 'nodes': {'fixtureL2': {'id': 'fixtureL2', 'level': 2, 'state': 'LEGACY_CANDIDATE'}}}
    A.qualify_node(l2, 'fixtureL2', False)
    no_l3 = len(l2['nodes']) == 1 and l2['nodes']['fixtureL2']['state'] == 'UNKNOWN'
    missing = copy.deepcopy(fixture)
    missing['nodes'][nid]['planned_L2_children'] = []
    missing_plan_reject = rejected(lambda: A.qualify_node(missing, nid, False))
    assert pending_not_closed and positive_closed and unknown_refined and no_l3 and missing_plan_reject

    admission_path = ROOT.parents[3] / 'institute/runs/six-lane-2026-10-16/review/moqls8-lane-admissions-v1/pilot-P1-B1-admission-v1.json'
    admission = T.read_admission(admission_path, A.HELD_PILOT)
    own, declared = A.caps_for(admission)
    assert own == 6 * 2 ** 30 and declared == {'N8FoneParentReplay': 0}
    future = {'sha256': 'fixture-not-an-admission', 'grant': {'other_declared_phys1_caps_bytes': {'fixture-other': 4 * 2 ** 30}}}
    future_own, _ = A.caps_for(future)
    no_future_guess = rejected(lambda: A.caps_for({'sha256': 'fixture-not-an-admission', 'grant': {}}))
    assert future_own == 4 * 2 ** 30 and no_future_guess
    assert T.capacity_available({'foreign_RSS_bytes': 4 * 2 ** 30, 'foreign_native_count': 2}, future_own)
    result = {'host': datetime.now().astimezone().isoformat(), 'status': 'PASS_STATIC_INTEGRATION_ONLY',
              'source_pins': pins, 'supervisor_sha256': A.SUP_SHA,
              'native_processes_or_supervise_invocations': 0, 'supervisor_imported': False,
              'actual_admission_checked_not_minted': A.HELD_PILOT,
              'directory_controls': {'init_and_recorded_reuse': True, 'repeat_root_init_rejected': init_again,
                                     'repeat_family_init_rejected': family_again, 'wrong_identity_rejected': wrong_identity,
                                     'unrecorded_existing_dir_rejected': orphan_rejected},
              'stop_channel_controls': {'absent_delegates': True, 'present_raises_once': first_reject,
                                        'subsequent_cleanup_probe_delegates': cleanup_delegates},
              'qualification_controls': {'pending_outer_not_closed': pending_not_closed, 'clean_outer_qualifies': positive_closed,
                                         'unclean_L1_all8L2': unknown_refined, 'unclean_L2_noL3': no_l3,
                                         'missing_L2_plan_rejected': missing_plan_reject},
              'declared_cap_controls': {'held_pilot_6GiB_other0': True, 'future_other4GiB_leaves4GiB': True,
                                         'future_unknown_caps_rejected': no_future_guess},
              'scope': 'AST/metadata/file-only adapter controls; not OS lifecycle coverage or mathematical refutation',
              'external_lifecycle_evidence': 'PhysEpQutrit supervise_controls_r3.json3c77be50...99de, separately observed/accepted by Main',
              'measured_solver_feed_sha256': None, 'measured_checker_feed_sha256': None,
              'fresh_free_bytes': free, 'fresh_lane_bytes': used}
    rh = T.new_json(OUT / 'RESULT.json', result)
    print(json.dumps({'status': result['status'], 'RESULT_sha256': rh, 'source_pins': pins, 'native_invocations': 0}), flush=True)


if __name__ == '__main__':
    main()
