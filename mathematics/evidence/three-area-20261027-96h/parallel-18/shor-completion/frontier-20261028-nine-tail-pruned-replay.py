#!/usr/bin/env python3
"""Replay the dependency-pruned nine-tail symbolic proof."""
import json,runpy
from pathlib import Path
root=Path(__file__).parent
r=runpy.run_path(str(root/'frontier-20261028-nine-tail-proof-replay.py'))
data=json.loads((root/'frontier-20261028-nine-tail-symbolic-proof-pruned-v1.json').read_text())
if data['extra_symbols']!=3 or [r['tup'](x) for x in data['Q']]!=r['Q'] or [r['tup'](x) for x in data['anchors_P']]!=r['A']:
    raise ValueError('wrong statement')
r['replay'](data['tree'],[])
if data['nodes']!=r['stats']['nodes']:raise ValueError('wrong node count')
print('PASS: independently replayed pruned symbolic coverage/collision proof')
print(json.dumps(r['stats'],sort_keys=True))
