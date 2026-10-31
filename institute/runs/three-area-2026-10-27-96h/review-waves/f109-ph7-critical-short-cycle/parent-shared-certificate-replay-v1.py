#!/usr/bin/env python3
"""Parent replay of the frozen independent reviewer, with a new output.

The reviewer engine is reused, not a third independent implementation. Its
verified bytes are compiled from memory; no author program is executed.
"""
import hashlib
import json
import subprocess
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE / 'certificate-replay-v1.py'
ENGINE_PIN = '7142f9c6f2ef2b5efd1d9b54e301c6f05a7b4ee5d6595e18f82e2bfd5e44902f'
OUTPUT = HERE / 'parent-shared-certificate-result-v1.json'
BINDING = HERE / 'parent-shared-certificate-binding-v1.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, text=True, capture_output=True).stdout.strip()


def main():
    if OUTPUT.exists() or BINDING.exists():
        raise FileExistsError('Exclusive parent outputs already exist')
    started = clock()
    source = ENGINE.read_bytes()
    if digest(source) != ENGINE_PIN:
        raise ValueError('ENGINE_HASH_MISMATCH')
    module = types.ModuleType('parent_pinned_independent_reviewer')
    module.__file__ = str(ENGINE)
    exec(compile(source, str(ENGINE), 'exec'), module.__dict__)
    module.RECEIPT = OUTPUT
    module.main()
    if digest(ENGINE.read_bytes()) != ENGINE_PIN:
        raise ValueError('ENGINE_CHANGED_AFTER_EXECUTION')
    result = json.loads(OUTPUT.read_text())
    for name, leaves, entries in [('D', 513, 124659), ('N', 657, 2053125)]:
        row = result['results'][name]
        if row['leaves'] != leaves or row['entries'] != entries:
            raise AssertionError('CERTIFICATE_COVERAGE_MISMATCH')
    binding = {
        'kind': 'PARENT_SHARED_ENGINE_PH7_CERTIFICATE_REPLAY',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'engine': str(ENGINE), 'engine_sha256': ENGINE_PIN,
        'engine_loaded_from_verified_memory_bytes': True,
        'engine_pre_post_match': True,
        'runner_sha256': digest(Path(__file__).read_bytes()),
        'result': str(OUTPUT), 'result_sha256': digest(OUTPUT.read_bytes()),
        'limits': 'Parent replay of the independently authored reviewer engine; '
                  'not a third implementation, independent-model-family, '
                  'human, formal/kernel, novelty or global PH7 proof.',
    }
    with BINDING.open('x', encoding='utf-8') as f:
        json.dump(binding, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(binding, sort_keys=True))


if __name__ == '__main__':
    main()
