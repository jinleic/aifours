"""Elaborate one Lean source and retain its exact source, output, and command."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path('/Users/jinleic/jinleic-workspace/scratch/rh-quasi-lean-2026-10-07/lean')
name = sys.argv[1] if len(sys.argv) > 1 else 'Formal.lean'
source = ROOT / name
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
destination = ROOT / 'evidence' / 'lean-attempts' / stamp
destination.mkdir(parents=True, exist_ok=False)
shutil.copyfile(source, destination / source.name)
command = ['/Users/jinleic/.elan/bin/lake', 'env', 'lean', str(source)]
env = dict(os.environ, LEAN_NUM_THREADS='2')
result = subprocess.run(command, cwd=CACHE, env=env, text=True,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
(destination / 'transcript.log').write_text(result.stdout)
receipt = {'created_at_utc': stamp, 'command': command, 'cwd': str(CACHE),
           'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'returncode': result.returncode, 'lean_num_threads': 2,
           'transcript': str((destination / 'transcript.log').relative_to(ROOT))}
(destination / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
print(result.stdout)
sys.exit(result.returncode)
