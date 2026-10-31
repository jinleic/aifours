#!/usr/bin/env python3
"""Generate exact phase-exponent certificate for a maximal QLS(10).

Uses explicit published BH(10,5). The array has NO orthogonal transversal
by a separately checked matching obstruction; it is NOT a 1-RQLS witness.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('b',ROOT/'frontier-20261028-butson10-half-matching-v1.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b);b.validate()
n=10
exponents=[[[ (r*t+2*b.K[t][c])%n for t in range(n)] for c in range(n)] for r in range(n)]
record={'dimension':n,'formula':'psi[r,c][t]=zeta_10^exponents[r][c][t]/sqrt(10)',
        'root':'exp(2*pi*i/10)','exponents':exponents,
        'source':'McNulty 2013 thesis Appendix D B10, independently checked',
        'caveat':'row/column QLS only; no transversal or 1-resolvability claimed'}
out=ROOT/'frontier-20261028-butson-maximal-qls-result-v1.json'
out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print('wrote 100 explicit 10-coordinate tenth-root vectors:',out.name)
print('must independently check original row/column and all4950 ray pairs')
