"""Run one read-only Codex review from NAME.prompt.txt; preserve evidence, refuse overwrite."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REGISTRY = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r'[a-zA-Z0-9-]+', sys.argv[1]):
        raise SystemExit('Usage: run_codex_note.py NAME')
    name = sys.argv[1]
    prompt_path = HERE / (name + '.prompt.txt')
    outputs = {key: HERE / (name + '.' + suffix) for key, suffix in
               [('note', 'note.md'), ('stdout', 'stdout.txt'), ('stderr', 'stderr.txt'), ('receipt', 'receipt.json')]}
    if any(p.exists() for p in outputs.values()):
        raise SystemExit('Refusing to overwrite prior review evidence; use a new name')
    prompt = prompt_path.read_text()
    cfg = json.loads(REGISTRY.read_text())['codex']
    command = ['codex', 'exec', '-m', cfg['model'], '-c', 'model_reasoning_effort=' + cfg['effort'],
               '--sandbox', 'read-only', '--ephemeral', '--skip-git-repo-check', '-C', str(HERE),
               '-o', str(outputs['note']), prompt]
    receipt = {'started_at_pt': stamp(), 'requested_model': cfg['model'], 'requested_effort': cfg['effort'],
               'prompt_sha256': hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
               'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'sandbox': 'read-only', 'status': 'FAILED', 'timeout_seconds': 2400}
    started = time.monotonic()
    try:
        with outputs['stdout'].open('x') as stdout, outputs['stderr'].open('x') as stderr:
            proc = subprocess.run(command, cwd=HERE, stdin=subprocess.DEVNULL,
                                  stdout=stdout, stderr=stderr, text=True, timeout=2400)
        receipt['returncode'] = proc.returncode
        if proc.returncode == 0 and outputs['note'].is_file():
            note = outputs['note'].read_bytes()
            if note.strip():
                receipt['status'] = 'NOTE_RETURNED_UNVERIFIED'
                receipt['note_sha256'] = hashlib.sha256(note).hexdigest()
    except (OSError, subprocess.TimeoutExpired) as exc:
        receipt['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        receipt['duration_seconds'] = time.monotonic() - started
        receipt['finished_at_pt'] = stamp()
        if outputs['stderr'].exists():
            header = outputs['stderr'].read_text(errors='replace')
            receipt['reported_identity'] = dict(re.findall(r'^(model|provider|sandbox|reasoning effort): (.+)$', header, re.M))
        with outputs['receipt'].open('x') as f:
            json.dump(receipt, f, indent=2)
            f.write('\n')
        print(json.dumps(receipt, indent=2))
    return 0 if receipt['status'] == 'NOTE_RETURNED_UNVERIFIED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
