"""Copy under delivery limits, then run every nonempty claims.json command.

Run from the task directory. The working copy is hidden so a later delivery
does not recursively include it. All load-bearing source artifacts remain
visible. No network, shell, external file, or locally built binary is used.
Commands use preinstalled Python and run with a 300-second individual and
1,800-second aggregate limit. The output records success/failure and timing;
it does not verify the universal mathematical argument.
"""
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import time


MAX_FILE_BYTES = 5_000_000
MAX_TOTAL_BYTES = 50_000_000
MAX_FILES = 2_000
PER_COMMAND_SECONDS = 300
TOTAL_COMMAND_SECONDS = 1_800


def delivery_files(root):
    """Select files in global relative-path order without traversing symlinks."""
    candidates, skipped = [], []
    for directory, dirs, files in os.walk(root, topdown=True, followlinks=False):
        parent = Path(directory)
        keep_dirs = []
        for name in sorted(dirs):
            path = parent / name
            relative = path.relative_to(root).as_posix()
            if name.startswith('.') or name == '__pycache__':
                skipped.append({'path': relative + '/', 'reason': 'hidden/cache directory'})
            elif path.is_symlink():
                skipped.append({'path': relative + '/', 'reason': 'symlink'})
            else:
                keep_dirs.append(name)
        dirs[:] = keep_dirs
        for name in sorted(files):
            path = parent / name
            relative = path.relative_to(root).as_posix()
            if name.startswith('.'):
                skipped.append({'path': relative, 'reason': 'hidden file'})
            elif path.is_symlink():
                skipped.append({'path': relative, 'reason': 'symlink'})
            elif path.is_file():
                candidates.append((relative, path))
    selected, total = [], 0
    for relative, path in sorted(candidates):
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            skipped.append({'path': relative, 'reason': 'file size limit'})
        elif len(selected) >= MAX_FILES:
            skipped.append({'path': relative, 'reason': 'file count limit'})
        elif total + size > MAX_TOTAL_BYTES:
            skipped.append({'path': relative, 'reason': 'total byte limit'})
        else:
            selected.append((relative, path, size))
            total += size
    return selected, sorted(skipped, key=lambda item: item['path']), total


def main():
    root = Path(__file__).resolve().parent.parent
    assert Path.cwd().resolve() == root, 'Run from the task directory'
    work = root / '.delivery-replay'
    assert not work.is_symlink(), 'Refusing a symlink work directory'
    work.mkdir(exist_ok=True)
    snapshot = work / 'snapshot'
    assert not snapshot.is_symlink(), 'Refusing a symlink snapshot'
    if snapshot.exists():
        shutil.rmtree(snapshot)
    snapshot.mkdir()

    selected, skipped, total = delivery_files(root)
    manifest = []
    for relative, source, size in selected:
        destination = snapshot / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        digest = hashlib.sha256(destination.read_bytes()).hexdigest()
        assert hashlib.sha256(source.read_bytes()).hexdigest() == digest
        manifest.append({'path': relative, 'bytes': size, 'sha256': digest})
    (snapshot / 'SKIPPED.json').write_text(json.dumps(skipped, indent=2) + '\n')
    ledger = json.loads((snapshot / 'claims.json').read_text())
    selected_names = {item['path'] for item in manifest}
    for claim in ledger['claims']:
        for evidence in claim['evidence']:
            assert evidence in selected_names, f'Load-bearing evidence skipped: {evidence}'
    print(f'SNAPSHOT: {len(selected)} files, {total} bytes; all claim evidence included.', flush=True)

    commands = [('schema', 'verify_command', 'python3 code/validate_claims.py')]
    commands.extend((claim['cid'], role, claim[role])
                    for claim in ledger['claims']
                    for role in ('verify_command', 'check_command', 'control_command')
                    if claim[role])
    logdir = root / 'logs' / 'delivery-commands'
    logdir.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    records = []
    all_passed = True
    for index, (cid, role, command) in enumerate(commands):
        remaining = TOTAL_COMMAND_SECONDS - (time.monotonic() - start)
        assert remaining > 0, 'Aggregate replay budget exhausted'
        args = shlex.split(command)
        assert args[0] == 'python3', f'Only preinstalled Python allowed: {command}'
        begin = time.monotonic()
        try:
            result = subprocess.run([sys.executable] + args[1:], cwd=snapshot,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    text=True, timeout=min(PER_COMMAND_SECONDS, remaining))
            returncode, output = result.returncode, result.stdout
            passed = returncode != 0 if role == 'control_command' else returncode == 0
        except subprocess.TimeoutExpired as exc:
            output = exc.stdout or ''
            if isinstance(output, bytes):
                output = output.decode(errors='replace')
            output += '\nTIMEOUT\n'
            returncode, passed = None, False
        seconds = time.monotonic() - begin
        filename = f'{index:02d}-{cid}-{role}.txt'
        (logdir / filename).write_text(output)
        records.append({'cid': cid, 'role': role, 'command': command,
                        'returncode': returncode, 'seconds': round(seconds, 6),
                        'passed': passed, 'output': f'logs/delivery-commands/{filename}'})
        all_passed = all_passed and passed
        print(f"{'PASS' if passed else 'FAIL'} {cid} {role}: exit={returncode}, {seconds:.2f}s", flush=True)
    elapsed = time.monotonic() - start
    assert elapsed <= TOTAL_COMMAND_SECONDS, 'Aggregate replay limit exceeded'
    report = {
        'all_passed': all_passed,
        'snapshot_file_count': len(selected), 'snapshot_bytes': total,
        'per_command_seconds_limit': PER_COMMAND_SECONDS,
        'aggregate_seconds_limit': TOTAL_COMMAND_SECONDS,
        'aggregate_seconds': round(elapsed, 6),
        'commands': records, 'snapshot_files': manifest, 'skipped': skipped,
        'scope': 'Execution and arithmetic audit only; the written analytic proof is not formally verified.',
    }
    (root / 'logs' / 'delivery-replay.json').write_text(json.dumps(report, indent=2) + '\n')
    assert all_passed, 'At least one delivery-copy command failed; inspect logs/delivery-replay.json'
    print(f'ALL DELIVERY-COPY COMMANDS PASSED: {len(records)} commands in {elapsed:.2f}s.', flush=True)


if __name__ == '__main__':
    main()
