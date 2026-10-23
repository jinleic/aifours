"""Real-process negative-path smoke for the review wrappers; no model calls.
The Popen launch is redirected to an owned, bounded Python process. Both actual SIGTERM handling and
ignored-SIGTERM/natural-exit paths are exercised. A synthetic partial Codex note must never become an
accepted review after a timeout. All logs and fixtures are retained. Run python3 -B smoke.py.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
REAL_POPEN = subprocess.Popen


class OwnedChild(REAL_POPEN):
    events = []

    def terminate(self):
        self.events.append({'pid': self.pid, 'signal': 'SIGTERM'})
        return super().terminate()

    def kill(self):
        raise RuntimeError('SIGKILL forbidden in this smoke')


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    rows = []
    original_argv = list(sys.argv)
    try:
        for cli in ('codex', 'claude'):
            for mode in ('graceful', 'survives-grace'):
                case = HERE / (cli + '-' + mode)
                case.mkdir(exist_ok=False)
                spec = importlib.util.spec_from_file_location('runner_under_smoke', REVIEW / f'run_{cli}_note_coop.py')
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                mod.HERE, mod.TIMEOUT, mod.GRACE = case, 0.2, 0.05
                name = 'owned-process-fixture'
                (case / (name + '.prompt.txt')).write_text('Synthetic timeout fixture: no model is invoked.\n')
                children = []
                OwnedChild.events = []

                def launch(command, **kwargs):
                    setup = "import signal,sys,time\n"
                    if mode == 'graceful':
                        setup += "def handle(sig,frame):\n print('saw_SIGTERM',flush=True)\n sys.exit(0)\nsignal.signal(signal.SIGTERM,handle)\n"
                    else:
                        setup += "signal.signal(signal.SIGTERM,signal.SIG_IGN)\n"
                    if cli == 'codex':
                        note = command[command.index('-o') + 1]
                        setup += f"from pathlib import Path\nPath({note!r}).write_text('SYNTHETIC PARTIAL NOTE — MUST NOT BE ACCEPTED\\n')\n"
                    setup += "print('started_fixture',flush=True)\nprint('fixture_stderr',file=sys.stderr,flush=True)\ntime.sleep(1.0)\nprint('natural_exit',flush=True)\n"
                    proc = OwnedChild([sys.executable, '-B', '-u', '-c', setup], **kwargs)
                    children.append(proc)
                    return proc

                subprocess.Popen = launch
                sys.argv = [str(REVIEW / f'run_{cli}_note_coop.py'), name]
                captured = io.StringIO()
                with contextlib.redirect_stdout(captured):
                    rc = mod.main()
                subprocess.Popen = REAL_POPEN
                sys.argv = original_argv
                receipt = json.loads((case / (name + '.receipt.json')).read_text())
                if receipt['status'] != 'TIMEOUT_NO_VERDICT' or rc != 1 or not receipt.get('timed_out'):
                    raise ValueError('timeout incorrectly accepted')
                if mode == 'survives-grace' and receipt.get('still_running_pid') != children[0].pid:
                    raise ValueError('surviving process not recorded')
                if mode == 'graceful' and receipt['returncode'] != 0:
                    raise ValueError('cooperative exit was not observed')
                for child in children:
                    child.wait(timeout=3)
                suffix = '.stdout.txt' if cli == 'codex' else '.stdout.json'
                logs = (case / (name + suffix)).read_text()
                if 'started_fixture' not in logs or ('saw_SIGTERM' if mode == 'graceful' else 'natural_exit') not in logs:
                    raise ValueError('partial or later output lost')
                if not (case / (name + '.stderr.txt')).read_text().strip():
                    raise ValueError('stderr lost')
                if not OwnedChild.events or any(e['signal'] != 'SIGTERM' for e in OwnedChild.events):
                    raise ValueError('non-cooperative signal')
                row = {'cli_wrapper': cli, 'mode': mode, 'runner_sha256': sha(REVIEW / f'run_{cli}_note_coop.py'),
                       'status': receipt['status'], 'exit': rc, 'logs_preserved': True,
                       'signals': OwnedChild.events, 'all_children_exited_naturally_or_cooperatively': True,
                       'fixture_only_no_model_call': True}
                rows.append(row)
                print(json.dumps(row), flush=True)
        result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                  'status': 'COOPERATIVE_REVIEW_WRAPPER_REAL_PROCESS_SMOKE_PASS', 'rows': rows,
                  'limits': 'Negative-path process behavior only; not mathematical or model-review evidence.'}
        with (HERE / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
    finally:
        subprocess.Popen = REAL_POPEN
        sys.argv = original_argv


if __name__ == '__main__':
    main()
