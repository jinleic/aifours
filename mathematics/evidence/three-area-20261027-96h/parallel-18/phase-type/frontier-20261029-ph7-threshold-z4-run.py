#!/usr/bin/env python3
"""Run the pinned z3 generator or its pinned stdlib replay at z4 = 33/40.

The z3 sources are read, their SHA-256 is asserted, and ONLY the literal ratio
constant, the certificate file name and two print labels are replaced (each
replacement must occur exactly once); the resulting source is executed
unchanged otherwise. Usage:  python3 <this> generate | replay
"""
import hashlib, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PINS = {
    'generate': ('frontier-20261029-ph7-threshold-z3-check.py',
                 '802dfcdb686c85ab24166ffda1c8119f032536d4ff146dcf995bfdbf0fc34440',
                 [("Z3 = R(83, 100)", "Z3 = R(33, 40)"),
                  ("frontier-20261029-ph7-threshold-z3-certificate-v1.json", "frontier-20261029-ph7-threshold-z4-certificate-v1.json"),
                  ("'z3': '83/100',", "'z3': '33/40',"),
                  ("'z3=83/100 exact PASS: QO'", "'z4=33/40 exact PASS: QO'")]),
    'replay': ('frontier-20261029-ph7-threshold-z3-integer-replay.py',
               '3ccb226fa299de1307d6db51525035bb5783ba5df338fd9938a9053581d269c1',
               [("Z3 = Q(83, 100)", "Z3 = Q(33, 40)"),
                ("frontier-20261029-ph7-threshold-z3-certificate-v1.json", "frontier-20261029-ph7-threshold-z4-certificate-v1.json"),
                ("'Independent stdlib replay PASS at z3=83/100: QO'", "'Independent stdlib replay PASS at z4=33/40: QO'")]),
}
mode = sys.argv[1]
name, sha, reps = PINS[mode]
src_bytes = (ROOT / name).read_bytes()
assert hashlib.sha256(src_bytes).hexdigest() == sha, 'pinned source changed'
src = src_bytes.decode()
for old, new in reps:
    assert src.count(old) == 1, old
    src = src.replace(old, new)
print('running pinned', name, 'with z replaced by 33/40')
exec(compile(src, str(ROOT / name) + ' [z4 substitution]', 'exec'), {'__name__': '__main__', '__file__': str(ROOT / name)})
