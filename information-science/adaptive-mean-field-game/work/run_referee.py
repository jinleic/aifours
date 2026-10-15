#!/usr/bin/env python3
"""Run the assigned other-vendor proof review; preserve exact input and receipts."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')


def main():
    proof = (ROOT / 'proof.md').read_text()
    prompt = (
        'Act as a hostile independent mathematical referee. Audit the COMPLETE proof below, '
        'not its plausibility. No tools, no delegation. Check the finite-N instrumental moment '
        'identities, matrix ordering, conditional bounded-differences proof with overlapping '
        'samples, all constants, sparse-calibration schedule and almost-sure rates, stability '
        'without circularity, the original sample-path cost and unilateral-deviation lower '
        'bound, local-information restriction, and every counterexample. Look for a concrete '
        'counterexample before accepting. The underlying book asks for unrestricted unknown '
        'local AND global matrices; this text explicitly claims only its H1-H4 subclass, not '
        'a full solution or novelty. Return JSON with verdict (correct / correct-with-fixes / '
        'incorrect), findings (array of id, severity, location, issue, correction), and a '
        'concise scope assessment. If no errors, state precisely what was checked.\n\n' + proof
    )
    evidence = ROOT / 'evidence'
    (evidence / 'referee-prompt.txt').write_text(prompt)
    model = json.loads(CONFIG.read_text())['claude']
    command = ['claude', '--model', model['model'], '--effort', model['effort'],
               '--safe-mode', '--no-chrome', '--tools', '', '--permission-mode', 'dontAsk',
               '--no-session-persistence', '--output-format', 'json', '-p', prompt]
    receipt = {'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'command_prefix': command[:-1], 'prompt_path': str(evidence / 'referee-prompt.txt'),
               'proof_sha256': hashlib.sha256(proof.encode()).hexdigest(),
               'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
               'stdin': '/dev/null', 'timeout_seconds': 2700}
    start = time.monotonic()
    try:
        proc = subprocess.run(command, cwd=ROOT, stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, timeout=2700)
        (evidence / 'referee-raw.json').write_text(proc.stdout)
        (evidence / 'referee-stderr.txt').write_text(proc.stderr)
        receipt['returncode'] = proc.returncode
        events = json.loads(proc.stdout)
        if isinstance(events, dict):
            events = [events]
        result = [e for e in events if e.get('type') == 'result'][-1]
        receipt['result_subtype'] = result.get('subtype')
        receipt['is_error'] = result.get('is_error')
        receipt['reported_model_usage'] = result.get('modelUsage')
        if proc.returncode != 0 or result.get('subtype') != 'success' or result.get('is_error'):
            raise RuntimeError('Referee result is not a successful result event')
        text = result.get('result', '')
        (evidence / 'referee-result.txt').write_text(text)
        if '```json' in text:
            text = text.split('```json', 1)[1].split('```', 1)[0]
        elif text.strip().startswith('```'):
            text = text.strip().split('\n', 1)[1].split('```', 1)[0]
        parsed = json.loads(text)
        (evidence / 'referee-findings.json').write_text(json.dumps(parsed, indent=2))
        receipt['parsed'] = True
    except Exception as exc:
        receipt['error'] = repr(exc)
        raise
    finally:
        receipt['duration_seconds'] = time.monotonic() - start
        (evidence / 'referee-command.json').write_text(json.dumps(receipt, indent=2))
    print(json.dumps({'verdict': parsed['verdict'], 'findings': parsed['findings'],
                      'duration_seconds': receipt['duration_seconds']}))


if __name__ == '__main__':
    main()
