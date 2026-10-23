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
import os
import struct
import errno
import sys
import types
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'evidence/n8_refine_r5_static_controls_v1'


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
    except (RuntimeError, OSError):
        return True
    return False


def main():
    free = shutil.disk_usage(ROOT).free
    M = load('darwin_process_metrics_r2')
    used = M.allocated_bytes(ROOT)
    if free - 1000000 < 12200000000 or used + 1000000 > 10200547328:
        raise SystemExit('DEFERRED: static-controls fresh disk/lane gate failed')
    T = load('run_n8_fone_refine_r5')
    A = load('launch_n8_fone_refine_r5')
    B = load('n8_fone_refine_bytes')
    # AST/data only: do NOT import/call the actual supervisor here.
    forbidden = {'kill', 'killpg', 'setsid', 'start_new_session', 'Popen'}
    for name in ('run_n8_fone_refine_r5', 'launch_n8_fone_refine_r5'):
        tree = ast.parse((ROOT / 'code' / (name + '.py')).read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                f = node.func
                token = f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''
                assert token not in forbidden, (name, token)
                assert not any(k.arg == 'start_new_session' for k in node.keywords)
    pins = {n: sha((ROOT / 'code' / (n + '.py')).read_bytes()) for n in
            ('run_n8_fone_refine_r5', 'launch_n8_fone_refine_r5', 'n8_fone_refine_bytes', 'control_n8_refine_r5',
             'k5_resplit_r4', 'k5_cover', 'n8_one_p4_formula', 'darwin_process_metrics_r2')}
    assert pins['n8_fone_refine_bytes'] == 'd9f191bfd940f5aad09300197a570192880e7c92f09b1a47c66828fc47a57853'
    assert pins['k5_resplit_r4'] == T.R_SHA and pins['k5_cover'] == T.C_SHA and pins['n8_one_p4_formula'] == T.F_SHA
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

    for name in ('run_n8_fone_refine_r5', 'darwin_process_metrics_r2'):
        tree = ast.parse((ROOT / 'code' / (name + '.py')).read_text())
        assert not any(isinstance(n, ast.Import) and any(a.name=='subprocess' for a in n.names) for n in ast.walk(tree))
    raw_args = (struct.pack('=i', 3) + b'/fixture/python\0\0' + b'python\0\0/marker/path\0' + b'SECRET=not-argv\0')
    assert M.parse_procargs2(raw_args) == (b'python', b'', b'/marker/path')
    malformed = [b'x', struct.pack('=i', 0)+b'/x\0\0x\0', struct.pack('=i', 1)+b'/unterminated',
                 struct.pack('=i', 1)+b'/x\0\0unterminated-argv']
    parser_rejections = [rejected(lambda r=r: M.parse_procargs2(r)) for r in malformed]
    assert all(parser_rejections)
    before = {'start': [1, 2], 'comm': 'Python'}
    with patch.object(M, 'read_argv', lambda *a: (b'python', b'/marker/path')):
        with patch.object(M, 'bsd_identity', lambda pid: ('alive', dict(before))):
            assert M.argv_matches(12345, (b'/marker',), None, before)
        with patch.object(M, 'bsd_identity', lambda pid: ('alive', {'start':[1,3], 'comm':'Python'})):
            identity_change_rejected = rejected(lambda: M.argv_matches(12345, (b'/marker',), None, before))
        with patch.object(M, 'bsd_identity', lambda pid: ('alive', {'start':[1,2], 'comm':'cadical'})):
            exec_change_rejected = rejected(lambda: M.argv_matches(12345, (b'/marker',), None, before))
    def denied(*a):
        raise PermissionError(errno.EPERM, 'fixture denied, no retry')
    with patch.object(M, 'read_argv', denied):
        with patch.object(M, 'bsd_identity', lambda pid: ('alive', dict(before))):
            denied_alive_rejected = rejected(lambda: M.argv_matches(12345, (b'/marker',), None, before))
        with patch.object(M, 'bsd_identity', lambda pid: ('gone', {'pid':pid})):
            departed_not_selected = not M.argv_matches(12345, (b'/marker',), None, before)
    assert identity_change_rejected and exec_change_rejected and denied_alive_rejected and departed_not_selected
    Sfake = types.SimpleNamespace(PROC_PGRP_ONLY=2, list_pids=lambda *a: [],
                                 probe=lambda pid: ('alive', 8192, {'pid':pid,'fixture_only':True}))
    with patch.object(M, 'supervisor', lambda: Sfake):
        assert M.rss_kb([12345]) == 8
        Sfake.probe = lambda pid: ('unknown', 0, {'pid':pid,'errno':1,'fixture_only':True})
        unknown_rejected = rejected(lambda: M.rss_kb([12345]))
        Sfake.probe = lambda pid: ('unknown', 0, {'pid':pid,'reason':'zero resident size','fixture_only':True})
        zero_unknown_rejected = rejected(lambda: M.rss_kb([12345]))
    assert unknown_rejected and zero_unknown_rejected
    disk_fixture = OUT / 'allocated'
    disk_fixture.mkdir()
    payload = disk_fixture / 'payload'
    payload.write_bytes(b'x'*8192)
    os.link(payload, disk_fixture/'hardlink')
    os.symlink('payload', disk_fixture/'symlink-file')
    os.symlink('.', disk_fixture/'symlink-dir')
    expected_blocks = sum(p.lstat().st_blocks for p in (disk_fixture,payload,disk_fixture/'symlink-file',disk_fixture/'symlink-dir')) * 512
    assert M.allocated_bytes(disk_fixture) == ((expected_blocks+1023)//1024)*1024
    oldR = (ROOT / 'code/k5_resplit_r2.py').read_text()
    cert = oldR[oldR.index('def certify('):oldR.index('\n\ndef main():')]
    assert sha(cert.encode()) == '25ef2728799ac0cb1f4b1dcc1f48f13d97098eb7ead3d64ae0f1e6219b44cfba'
    assert (ROOT / 'code/k5_resplit_r4.py').read_text().endswith(cert + '\n')
    anchor = ROOT / 'evidence/n8_one_p4_template_runs_v1/refine_v4/P1-B1/LEDGER.v006.json'
    anchor_hash = '628d64a3ff275777a8ae7f16c289b00d0313c66a561f5398896a10a23a510310'
    imported = T.import_source_epoch(anchor, anchor_hash, 'P1-B1',
                                    'bcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19',
                                    units42, {'fixture_only':True})
    assert imported['active_seconds'] == 454.5896603760775
    assert all(imported['nodes']['P1-B1.L1.%03d'%b]['state']=='REFINED' for b in (0,1,2))
    assert imported['version'] == 0 and imported['status'] == 'OPEN'
    assert sha(anchor.read_bytes()) == anchor_hash
    assert rejected(lambda: T.import_source_epoch(anchor, '0'*64, 'P1-B1',
                                                  imported['source16_results_sha256'], units42, {}))
    continuation_next = sorted((n for n in imported['nodes'].values() if n['state']=='UNSTARTED'),
                               key=lambda n:(n['level'],n['b'],-1 if n['c'] is None else n['c']))[0]['id']
    assert continuation_next == 'P1-B1.L1.003'

    admission_path = ROOT.parents[3] / 'institute/runs/six-lane-2026-10-16/review/moqls8-lane-admissions-v1/pilot-P1-B1-admission-v1.json'
    admission_raw = admission_path.read_bytes()
    assert sha(admission_raw) == A.HELD_PILOT
    released_admission_rejected = rejected(lambda: T.read_admission(admission_path, A.HELD_PILOT))
    assert released_admission_rejected
    historical_cap_fixture = {'sha256': A.HELD_PILOT, 'grant': json.loads(admission_raw)}
    own, declared = A.caps_for(historical_cap_fixture)
    assert own == 6 * 2 ** 30 and declared == {'N8FoneParentReplay': 0}
    future = {'sha256': 'fixture-not-an-admission', 'grant': {'other_declared_phys1_caps_bytes': {'fixture-other': 4 * 2 ** 30}}}
    future_own, _ = A.caps_for(future)
    no_future_guess = rejected(lambda: A.caps_for({'sha256': 'fixture-not-an-admission', 'grant': {}}))
    assert future_own == 4 * 2 ** 30 and no_future_guess
    assert T.capacity_available({'foreign_RSS_bytes': 4 * 2 ** 30, 'foreign_native_count': 2}, future_own)
    result = {'host': datetime.now().astimezone().isoformat(), 'status': 'PASS_STATIC_INTEGRATION_ONLY',
              'source_pins': pins, 'supervisor_sha256': A.SUP_SHA,
              'no_setuid_controls': {'direct_RSS_positive': True, 'unknown_EPERRSS_rejected': unknown_rejected,
                                      'zero_unknown_rejected': zero_unknown_rejected,
                                      'parser_corruptions_rejected': parser_rejections,
                                      'identity_change_rejected': identity_change_rejected,
                                      'exec_change_rejected': exec_change_rejected,
                                      'denied_alive_rejected': denied_alive_rejected,
                                      'departed_not_selected': departed_not_selected, 'allocated_hardlink_symlink_check': True,
                                      'certify_bytes_unchanged': True, 'continuation_next': continuation_next,
                                      'old_ledger_not_modified': True},
              'native_processes_or_supervise_invocations': 0, 'supervisor_imported': False,
              'old_admission_released_rejected': released_admission_rejected,
              'historical_cap_fixture_not_launch_authority': A.HELD_PILOT,
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
