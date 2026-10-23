"""Run one prompt-only independent mathematical note; preserve every outcome.
Cooperative variant of run_claude_note.py: on timeout it sends SIGTERM and waits a bounded time; it never sends
SIGKILL. If the CLI is still running after the grace period it is left running and its pid is recorded.
Usage: python3 -B run_claude_note_coop.py NAME
"""
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
TIMEOUT, GRACE = 2400, 60


def note_text(events, final):
    """Claude can continue across turns while result.result contains only the final tail."""
    parts = [
        block['text']
        for event in events if event.get('type') == 'assistant'
        for block in event.get('message', {}).get('content', [])
        if block.get('type') == 'text' and block.get('text')
    ]
    return '\n\n'.join(parts) if parts else final['result']


def main() -> int:
    if len(sys.argv) != 2 or not sys.argv[1].replace('-', '').isalnum():
        raise SystemExit('Usage: run_claude_note_coop.py prompt-name')
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
               'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'tools': [], 'timeout_seconds': TIMEOUT, 'status': 'FAILED',
               'stop_policy': 'SIGTERM then bounded wait; never SIGKILL'}
    try:
        with outputs[0].open('x') as stdout, outputs[1].open('x') as stderr:
            proc = subprocess.Popen(args, cwd=HERE, stdin=subprocess.DEVNULL,
                                    stdout=stdout, stderr=stderr, text=True)
            try:
                proc.wait(timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                receipt['timed_out'] = True
                receipt['status'] = 'TIMEOUT_NO_VERDICT'
                proc.terminate()
                try:
                    proc.wait(timeout=GRACE)
                except subprocess.TimeoutExpired:
                    receipt['still_running_pid'] = proc.pid
        receipt['returncode'] = proc.returncode
        if proc.returncode == 0 and not receipt.get('timed_out'):
            events = json.loads(outputs[0].read_text())
            if isinstance(events, dict):
                events = [events]
            finals = [e for e in events if e.get('type') == 'result']
            if finals:
                final = finals[-1]
                receipt['reported_init_models'] = sorted({e.get('model') for e in events
                                                          if e.get('type') == 'system' and e.get('model')})
                receipt['reported_model_usage'] = final.get('modelUsage', {})
                if final.get('subtype') == 'success' and not final.get('is_error', False):
                    with outputs[2].open('x') as f:
                        f.write(note_text(events, final).rstrip() + '\n')
                    receipt['note_assembly'] = 'all assistant text chunks; final result fallback if none'
                    receipt['status'] = 'NOTE_RETURNED_UNVERIFIED'
    except (OSError, ValueError, KeyError) as exc:
        receipt['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        receipt['duration_seconds'] = time.monotonic() - started
        receipt['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
        with outputs[3].open('x') as f:
            f.write(json.dumps(receipt, indent=2) + '\n')
        print(json.dumps(receipt, indent=2))
    return 0 if receipt['status'] == 'NOTE_RETURNED_UNVERIFIED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
