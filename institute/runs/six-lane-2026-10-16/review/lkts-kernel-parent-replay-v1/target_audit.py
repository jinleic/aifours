"""Close semantic-review R1 and inspect actual generator arguments/raw syntax (D1-D3)."""
import hashlib
import json
from pathlib import Path
import re
from parent_replay import HERE, ALLOWED_AXIOMS, require, run, stamp


def main():
    output = HERE / 'parent-target-audit-result.json'
    require(not output.exists(), 'Refusing to overwrite prior target-audit evidence')
    result = {'status': 'FAILED', 'started_at_pt': stamp(), 'steps': [], 'generator_hardening_checks': {},
              'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    try:
        previous = json.loads((HERE / 'parent-result.json').read_text())
        require(previous['status'] == 'PARENT_REBUILD_AND_FRESH_KERNEL_REPLAY_PASS', 'Parent rebuild prerequisite')
        expected = json.loads((HERE / 'result.json').read_text())
        for v in [57, 87]:
            raw = (HERE / f'raw{v}.txt').read_bytes()
            require(all(byte == 10 or 32 <= byte <= 126 for byte in raw), 'Noncanonical raw control/non-ASCII byte')
            counts = {'header': 0, 'systems': 0, 'classes': 0, 'rows': 0}
            integer = re.compile(r'(?:0|[1-9][0-9]*)\Z')
            for line in raw.decode('ascii').split('\n'):
                if not line or line.startswith('#'):
                    continue
                tokens = line.split(' ')
                if tokens[0] in ('LKTS', 'KTS', 'CLASS'):
                    require(len(tokens) == 2 and integer.fullmatch(tokens[1]), 'Noncanonical label token')
                    counts[{'LKTS': 'header', 'KTS': 'systems', 'CLASS': 'classes'}[tokens[0]]] += 1
                else:
                    require(len(tokens) == 3 and all(integer.fullmatch(x) for x in tokens), 'Noncanonical row token')
                    counts['rows'] += 1
            require(counts == {'header': 1, 'systems': v - 2, 'classes': (v - 2) * ((v - 1) // 2),
                               'rows': (v - 2) * ((v - 1) // 2) * (v // 3)}, 'Canonical raw counts')
            generation = [step for step in previous['steps'] if step['command'][:4] ==
                          [step['command'][0], '-B', 'gen_data.py', f'raw{v}.txt']]
            require(len(generation) == 1, 'Unique recorded generator invocation')
            command = generation[0]['command']
            name, label = command[command.index('--name') + 1], command[command.index('--label') + 1]
            require(re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', name) is not None, 'Safe actual Lean identifier')
            require('/-' not in label and '-/' not in label and all(ord(ch) >= 32 for ch in label), 'Safe actual comment label')
            data_path = HERE / 'LktsKernel' / f'Data{v}.lean'
            disk_sha = hashlib.sha256(data_path.read_bytes()).hexdigest()
            require(disk_sha == expected['sources_sha256'][f'LktsKernel/Data{v}.lean'], 'On-disk generated data hash')
            require(data_path.read_bytes() == (HERE / 'regenerated' / f'Data{v}.lean').read_bytes(), 'On-disk regeneration comparison')
            result['generator_hardening_checks'][str(v)] = {'canonical_counts': counts, 'actual_name': name,
                'actual_label': label, 'comment_interpolation_safe': True, 'generated_on_disk_sha256': disk_sha,
                'noncanonical_token_controls_rejected': all(integer.fullmatch(x) is None for x in ['+5', '05', '5_0'])}
        for module in ['AuditTarget', 'AuditRoots']:
            run(['sh', 'build_module.sh', f'LktsKernel/{module}.lean'], f'build-{module}', result['steps'])
        log = (HERE / 'logs/AuditRoots.build.log').read_text()
        axioms = {name: [x.strip() for x in listed.split(',') if x.strip()]
                  for name, listed in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log)}
        require(set(axioms) == {'Kirkman.Audit.exists57', 'Kirkman.Audit.exists87'}, 'Both closed target roots reported')
        require(all(set(values) <= ALLOWED_AXIOMS for values in axioms.values()), 'Standard target-root axioms')
        replay = run(['sh', '-c', '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v "$1"',
                      'parent-target-fresh', 'LktsKernel.AuditRoots'], 'fresh-AuditRoots', result['steps'], timeout=1200)
        require('replaying' in replay and 'LktsKernel.AuditRoots' in replay, 'Target-root fresh replay marker')
        result['axioms'] = axioms
        result['audit_source_sha256'] = {name: hashlib.sha256((HERE / 'LktsKernel' / f'{name}.lean').read_bytes()).hexdigest()
                                          for name in ['AuditTarget', 'AuditRoots']}
        result['status'] = 'TARGET_STATEMENTS_AND_BINDING_AUDIT_PASS'
        result['limit'] = 'Fixed pinned inputs and actual generation arguments inspected; this does not harden the generic generator for untrusted future CLI inputs. Same Lean kernel implementation, no Comparator or second kernel.'
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        result['finished_at_pt'] = stamp()
        with output.open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
        print(json.dumps({'status': result['status'], 'result': str(output), 'error': result.get('error')}, indent=2), flush=True)
    return 0 if result['status'] == 'TARGET_STATEMENTS_AND_BINDING_AUDIT_PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
