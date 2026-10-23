#!/usr/bin/env python3
"""Preserve the previous delivery and downgrade unverified claims for repair."""
import json
from pathlib import Path
import shutil

prior = Path('evidence/previous-delivery')
prior.mkdir(exist_ok=True)
for filename in ('REPORT.md', 'claims.json', 'evidence/manifest.json'):
    target = prior / Path(filename).name
    if not target.exists():
        shutil.copyfile(filename, target)
status = {
    'outcome': 'no-progress',
    'summary': 'Recovery and verification in progress. The previous production endpoint 10341223092224 is provisional until the missing logs are reconstructed and rechecked. The all-orders question is unresolved; novelty is unknown.',
    'claims': [],
    'next_step': 'Recover the compressed logs, validate integrity against both manifests, rerun arithmetic checks, and repair the comparison and replay commands.'
}
Path('claims.json.tmp').write_text(json.dumps(status, indent=2)+'\n')
Path('claims.json.tmp').replace('claims.json')
Path('evidence/recovery-session.json').write_text(json.dumps({
    'start_utc': '2026-10-15 19:02:31 UTC',
    'deliverables_due_utc': '2026-10-15 23:08:31 UTC',
    'hard_stop_utc': '2026-10-15 23:52:31 UTC',
    'scope': 'Continue prior attempt, local files only, no binary execution during replay, no delegation.'
}, indent=2)+'\n')
