#!/usr/bin/env python3
"""Print exact finite-block matrices for the reviewer's independent construction."""
from contextlib import redirect_stdout
from io import StringIO
import json
import runpy

with redirect_stdout(StringIO()):
    state = runpy.run_path('reviewer-exact-controls-v1.py')
H = state['Hmat']
PT = state['Rgamma']
def block(m, ids):
    return [[str(m[i][j]) for j in ids] for i in ids]
def show(m, groups):
    return [{'indices': ids, 'matrix': block(m, ids)} for ids in groups]
print(json.dumps({
    'H_nonsingleton_blocks': show(H, [[0,6,12,18,24], [1,7], [5,11]]),
    'H_singletons': show(H, [[x] for x in [2,3,4,8,9,10,13,14,15,16,17,19,20,21,22,23]]),
    'PT_nonsingleton_blocks': show(PT, [[1,5], [2,6,10], [4,17], [7,11], [13,15]])
}, indent=2))
