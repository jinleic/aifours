#!/usr/bin/env python3
"""Create small deliberately corrupted witnesses for recovery/checker tests."""
import json
from pathlib import Path

rows = [json.loads(s) for s in Path('logs/python-main.records.jsonl').read_text().splitlines()]
first = min(rows, key=lambda r: r['index'])
assert int(first['residue']) != 0
first['residue'] = '0'
Path('evidence/recovery-broken-shared.records.jsonl').write_text(json.dumps(first)+'\n')

path = Path('evidence/prefix-chunks/00.json')
if path.exists():
    broken = json.loads(path.read_text())
    broken['every_n_decision_full_residue_sha256'] = '0'*64
    Path('evidence/prefix-chunk-broken.json').write_text(json.dumps(broken, indent=2)+'\n')

directory = Path('selection-inputs/first-attempt-logs')
broken_manifest = json.loads((directory / 'MANIFEST.json').read_text())
broken_manifest['sources'][0]['parts'][0]['compressed_sha256'] = '0'*64
(directory / 'BROKEN-MANIFEST.json').write_text(json.dumps(broken_manifest, indent=2)+'\n')
