"""Run one prompt-only configured subscription review; preserve all outcomes and stop with SIGTERM only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time

RUN = Path(__file__).resolve().parent.parent
REGISTRY = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], text=True).strip()


def write_new(path, value):
    with path.open('x') as handle:
        json.dump(value, handle, indent=2)
        handle.write('\n')
        handle.flush()
        os.fsync(handle.fileno())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt')
    parser.add_argument('--budget-seconds', type=int, default=2400)
    args = parser.parse_args()
    prompt_path = Path(args.prompt).resolve()
    if not prompt_path.is_relative_to(RUN) or not 60 <= args.budget_seconds <= 3600:
        raise SystemExit('Invalid scoped prompt or self-budget')
    base = prompt_path.with_suffix('')
    paths = {key: Path(str(base) + suffix) for key, suffix in
             [('stdout', '.stdout.json'), ('stderr', '.stderr.txt'), ('receipt', '.receipt.json'),
              ('note', '.note.md'), ('launch', '.launch.json')]}
    if any(p.exists() for p in paths.values()):
        raise SystemExit('Refusing to overwrite review evidence')
    cfg = json.loads(REGISTRY.read_text())['claude']
    cmd = ['claude', '--model', cfg['model'], '--effort', cfg['effort'], '--safe-mode', '--no-chrome',
           '--tools', '', '--permission-mode', 'dontAsk', '--no-session-persistence',
           '--output-format', 'json', '-p', prompt_path.read_text()]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', TMPDIR=str(RUN / 'control/tmp'),
               TMP=str(RUN / 'control/tmp'), TEMP=str(RUN / 'control/tmp'))
    begin = time.monotonic()
    record = {'started_at': clock(), 'requested_model': cfg['model'], 'requested_effort': cfg['effort'],
              'prompt_sha256': hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'tools': [],
              'self_budget_seconds': args.budget_seconds, 'status': 'NO_VERDICT'}
    with paths['stdout'].open('x') as stdout, paths['stderr'].open('x') as stderr:
        proc = subprocess.Popen(cmd, cwd=RUN, env=env, stdin=subprocess.DEVNULL,
                                stdout=stdout, stderr=stderr, start_new_session=True)
        write_new(paths['launch'], dict(record, pid=proc.pid, pgid=os.getpgid(proc.pid), cwd=str(RUN),
                                       argv_sha256=hashlib.sha256(json.dumps(cmd).encode()).hexdigest()))
        while proc.poll() is None and time.monotonic() - begin < args.budget_seconds:
            time.sleep(1)
        if proc.poll() is None:
            record['stop_requested_at'] = clock()
            record['status'] = 'SELF_BUDGET_SIGTERM_NO_VERDICT'
            os.killpg(proc.pid, signal.SIGTERM)
            settle_end = time.monotonic() + 60
            while proc.poll() is None and time.monotonic() < settle_end:
                time.sleep(0.2)
            if proc.poll() is None:
                record['unsettled_pid'] = proc.pid
        record['returncode'] = proc.poll()
    if record['returncode'] == 0 and 'stop_requested_at' not in record:
        try:
            events = json.loads(paths['stdout'].read_text())
            if isinstance(events, dict):
                events = [events]
            finals = [e for e in events if e.get('type') == 'result']
            final = finals[-1]
            record['reported_init_models'] = sorted({e['model'] for e in events if e.get('type') == 'system' and e.get('model')})
            record['reported_model_usage'] = final.get('modelUsage', {})
            if final.get('subtype') == 'success' and not final.get('is_error', False):
                chunks = [b['text'] for e in events if e.get('type') == 'assistant'
                          for b in e.get('message', {}).get('content', [])
                          if b.get('type') == 'text' and b.get('text')]
                note = '\n\n'.join(chunks) if chunks else final.get('result', '')
                with paths['note'].open('x') as handle:
                    handle.write(note.rstrip() + '\n')
                record['status'] = 'REVIEW_RETURNED_UNVERIFIED'
        except (ValueError, KeyError, IndexError, OSError) as exc:
            record['parse_error'] = str(exc)
    record['finished_at'] = clock()
    record['duration_seconds'] = time.monotonic() - begin
    write_new(paths['receipt'], record)
    print(json.dumps(record, indent=2), flush=True)
    return 0 if record['status'] == 'REVIEW_RETURNED_UNVERIFIED' else 1


if __name__ == '__main__':
    raise SystemExit(main())
