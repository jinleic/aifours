#!/usr/bin/env python3
"""Read-only structural-row evidence hardening controls; run behind with_token15 (metadata only).
Actual and <=10MiB shadow-tree baselines must match. For every required source, moving it away or replacing bytes
must leave STRUCTURAL_PENDING_BINDING; an unlisted sibling copy cannot bypass the missing expected path. Duplicate
resolved paths/digests and missing/unlisted shadow keys are refused explicitly. Five single-protection in-memory
mutants must each be killed by these controls. No original evidence changes/deletions; fixture originals are moved,
replacement/receipt files use x-mode. These are evidence-binding controls, NOT proof/checker mutation tests.
"""
import hashlib
import json
import os
import time
import types
from pathlib import Path

import structural_b3_acceptance as V

LANE = Path(__file__).resolve().parent.parent


def main():
    root = LANE / 'cycle2' / ('structural-b3-binding-controls-%d' % time.time_ns())
    root.mkdir(exist_ok=False)
    canonical = {k: Path(v['path']).read_bytes() for k,v in V.EXPECTED.items()}
    # Reuse one immutable tiny shadow set, isolating only the source mutated by each control.
    # Even six full suites retain <10MiB, not six copies of every fixture tree.
    assert sum(map(len, canonical.values())) * 32 + 4 * 1024 * 1024 < 10 * 1024 * 1024
    canonical_dir = root / 'canonical-shadow'
    canonical_dir.mkdir(exist_ok=False)
    canonical_paths = {}
    for k, raw in canonical.items():
        p = canonical_dir / (k + '.evidence')
        with p.open('xb') as f:
            f.write(raw)
        canonical_paths[k] = str(p)
    seq = [0]

    def fixture():
        seq[0] += 1
        d = root / ('fixture-%03d' % seq[0])
        d.mkdir(exist_ok=False)
        return d, dict(canonical_paths)

    def isolate(paths, key, d):
        p = d / (key + '.evidence')
        with p.open('xb') as f:
            f.write(canonical[key])
        paths[key] = str(p)

    def moved(path):
        p = Path(path)
        dest = p.parent / ('retained-original-' + p.name)
        assert not dest.exists()
        os.rename(p, dest)
        return dest

    def assert_pending(mod, paths, kind):
        r = mod.verify(paths)
        assert r['accepted'] is False and r['solver_checked'] is False, r
        assert r['error_kind'] == kind, r
        return r['detail']

    def suite(mod):
        checks = []
        d, paths = fixture()
        shadow = mod.verify(paths)
        assert shadow['accepted'] is True and shadow['solver_checked'] is False
        assert {k:v['sha256'] for k,v in shadow['source_bindings'].items()} == {k:v['sha256'] for k,v in V.EXPECTED.items()}
        checks.append('shadow baseline same frozen hashes')
        for key in canonical:
            d, paths = fixture()
            isolate(paths, key, d)
            original = moved(paths[key])
            # Extra valid bytes at an unlisted sibling path must not become a replacement source.
            with (d / ('unlisted-copy-' + key)).open('xb') as f:
                f.write(original.read_bytes())
            detail = assert_pending(mod, paths, 'missing')
            assert key in detail
            checks.append('missing exact source plus unlisted copy: ' + key)
            d, paths = fixture()
            isolate(paths, key, d)
            original = moved(paths[key])
            with Path(paths[key]).open('xb') as f:
                f.write(original.read_bytes() + b'\n')
            detail = assert_pending(mod, paths, 'digest')
            assert key in detail
            checks.append('changed exact source: ' + key)
        d, paths = fixture()
        del paths[next(iter(paths))]
        assert_pending(mod, paths, 'required_set')
        checks.append('missing required shadow key')
        d, paths = fixture()
        paths['unlisted-key'] = str(d / 'unused')
        assert_pending(mod, paths, 'required_set')
        checks.append('unlisted shadow key')
        keys = list(canonical)
        d, paths = fixture()
        paths[keys[1]] = paths[keys[0]]
        assert_pending(mod, paths, 'duplicate_path')
        checks.append('duplicate resolved source path')
        d, paths = fixture()
        isolate(paths, keys[1], d)
        moved(paths[keys[1]])
        with Path(paths[keys[1]]).open('xb') as f:
            f.write(canonical[keys[0]])
        assert_pending(mod, paths, 'duplicate_digest')
        checks.append('duplicate source digest at distinct path')
        assert not (d / 'output.json').exists()
        return checks

    actual = V.verify()
    assert actual['accepted'] is True and actual['solver_checked'] is False
    baseline = suite(V)
    source = Path(V.__file__).read_text()
    mutations = {
        'required_set': ("if set(selected) != set(EXPECTED):", "if False:"),
        'duplicate_path': ("if len(set(resolved.values())) != len(resolved):", "if False:"),
        'duplicate_digest': ("if len(set(digests.values())) != len(digests):", "if False:"),
        'frozen_digest': ("if digests[label] != spec['sha256']:", "if False:"),
        'missing_file_response': ("return pending('missing', 'inventoried %s is missing/unreadable: %s' % (label, exc))", "raise")}
    kills = []
    for name, (anchor, replacement) in mutations.items():
        assert source.count(anchor) == 1, name
        changed = source.replace(anchor, replacement, 1)
        assert changed != source
        mutant_path = root / ('mutant-' + name + '.py')
        with mutant_path.open('x') as f:
            f.write(changed)
        mod = types.ModuleType('structural_b3_mutant_' + name)
        exec(compile(changed, str(mutant_path), 'exec'), mod.__dict__)
        caught = None
        try:
            suite(mod)
        except Exception as exc:
            caught = repr(exc)[:1000]
        kills.append({'protection_removed': name, 'mutant_sha256': hashlib.sha256(changed.encode()).hexdigest(),
                      'killed': caught is not None, 'observed_failure': caught})
        assert caught is not None, ('SURVIVED', name)
    result = {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'module_sha256': hashlib.sha256(source.encode()).hexdigest(),
              'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'actual_row_accepted': actual['accepted'],
              'actual_solver_checked': actual['solver_checked'], 'required_sources': len(canonical),
              'baseline_controls': baseline, 'baseline_control_count': len(baseline), 'single_protection_mutants': kills,
              'all_mutants_killed': all(x['killed'] for x in kills), 'original_evidence_unchanged': True,
              'scope': 'source/document/input binding and shadow-tree controls only; not scientific or solver-proof mutation checks'}
    dest = root / 'receipt.json'
    with dest.open('x') as f:
        json.dump(result, f, indent=1)
    print(dest)
    print(json.dumps({'required_sources':len(canonical),'baseline_control_count':len(baseline),'mutants':len(kills),'all_mutants_killed':result['all_mutants_killed']}))


if __name__ == '__main__':
    main()
