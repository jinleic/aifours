"""Run one prompt-only independent mathematical note; preserve every outcome."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REGISTRY = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1].replace('-', '').isalnum():
        raise SystemExit('Usage: run_claude_note.py prompt-name')
    name = sys.argv[1]
    prompt_path = HERE / f'{name}.prompt.txt'
    prompt = prompt_path.read_text()
    outputs = [HERE / f'{name}.{ext}' for ext in ('stdout.json', 'stderr.txt', 'note.md', 'receipt.json')]
    if any(path.exists() for path in outputs):
        raise SystemExit('Refusing to overwrite prior delegate evidence; use a new prompt name')
    cfg = json.loads(REGISTRY.read_text())['claude']
    args = ['claude', '--model', cfg['model'], '--effort', cfg['effort'],
            '--safe-mode', '--no-chrome', '--tools', '', '--permission-mode', 'dontAsk',
            '--no-session-persistence', '--output-format', 'json', '-p', prompt]
    started = time.monotonic()
    receipt = {'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'requested_model': cfg['model'], 'requested_effort': cfg['effort'],
               'prompt_sha256': hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
               'tools': [], 'timeout_seconds': 2400, 'status': 'FAILED'}
    out = ''
    err = ''
    try:
        result = subprocess.run(args, cwd=HERE, stdin=subprocess.DEVNULL,
                                capture_output=True, text=True, timeout=2400)
        out, err = result.stdout, result.stderr
        receipt['returncode'] = result.returncode
        if result.returncode == 0:
            events = json.loads(out)
            if isinstance(events, dict):
                events = [events]
            finals = [e for e in events if e.get('type') == 'result']
            if finals:
                final = finals[-1]
                receipt['reported_init_models'] = [e.get('model') for e in events if e.get('type') == 'system']
                receipt['reported_model_usage'] = final.get('modelUsage', {})
                if final.get('subtype') == 'success' and not final.get('is_error', False):
                    outputs[2].write_text(final['result'].rstrip() + '\n')
                    receipt['status'] = 'NOTE_RETURNED_UNVERIFIED'
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout or ''
        err = exc.stderr or ''
        if isinstance(out, bytes):
            out = out.decode(errors='replace')
        if isinstance(err, bytes):
            err = err.decode(errors='replace')
        receipt['status'] = 'TIMEOUT_NO_VERDICT'
    except (OSError, ValueError, KeyError) as exc:
        receipt['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        outputs[0].write_text(out)
        outputs[1].write_text(err)
        receipt['duration_seconds'] = time.monotonic() - started
        receipt['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        outputs[3].write_text(json.dumps(receipt, indent=2) + '\n')
        print(json.dumps(receipt, indent=2))
    return 0 if receipt['status'] == 'NOTE_RETURNED_UNVERIFIED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
