from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

p = Path(__file__).resolve().parent
old = (p / 'reviewer-control-v1.py').read_bytes()
text = old.decode()
replacements = [
    ('reviewer-control-receipt-v1.json', 'reviewer-control-receipt-v2.json'),
    ('from itertools import product', 'from itertools import permutations, product'),
    ("    # Non-normal six-element band, concretely verified, with generator-swap\n    # automorphism. Words with both letters reduce to their first/last letters.\n    band = ['a', 'b', 'ab', 'ba', 'aba', 'bab']\n    def reduce_word(w):\n        if len(set(w)) == 1:\n            return w[0]\n        if w[0] != w[-1]:\n            return w[0] + w[-1]\n        return w[0] + ('b' if w[0] == 'a' else 'a') + w[0]", "    # Non-normal 15-element left regular band: nonempty words on abc with\n    # no repeated letter; multiplication retains each letter's first occurrence.\n    # The action swaps a,b and fixes c.\n    band = [''.join(w) for k in range(1, 4) for w in permutations('abc', k)]\n    def reduce_word(w):\n        return ''.join(dict.fromkeys(w))"),
    ("need(len(idempotents(bt)) == 6, 'B not a band')", "need(len(idempotents(bt)) == 15, 'B not a band')"),
    ('product(range(6), repeat=3)', 'product(range(len(band)), repeat=3)'),
    ('len(he) == len(ue) == 24', 'len(he) == len(ue) == 60'),
    ('96->48 Pastijn quotient, nontrivial action, 24 unique idempotent lifts, group fibers, 576 order pairs',
     '240->120 Pastijn quotient, nontrivial action, 60 unique idempotent lifts, group fibers, 3600 order pairs'),
]
for before, after in replacements:
    if text.count(before) != 1:
        raise RuntimeError('replacement must match once: ' + before)
    text = text.replace(before, after)
now = datetime.now(timezone.utc).isoformat()
failure = {
    'kind': 'REVIEWER_CONTROL_FAILED_ATTEMPT',
    'observed_after_failure_UTC_upper_bound': now,
    'script': 'reviewer-control-v1.py',
    'script_sha256': sha256(old).hexdigest(),
    'tool_observed_exit_code': 1,
    'tool_observed_exception': 'ControlFailure: test band unexpectedly normal',
    'failure_source': 'Reviewer incorrectly selected a six-element normal band as a non-normal fixture.',
    'meaning': 'This failed reviewer premise is not evidence of a candidate defect; no success receipt was emitted.',
    'repair': 'Preserve v1 unchanged; v2 uses a concretely verified 15-element left regular band on three generators.',
    'new_script_sha256': sha256(text.encode()).hexdigest(),
}
with (p / 'reviewer-control-attempt-v1.json').open('x') as f:
    f.write(json.dumps(failure, indent=2) + '\n')
with (p / 'reviewer-control-v2.py').open('x') as f:
    f.write(text)
print('Preserved failed v1; created v2 with a non-normal three-generator left regular band.')
print('observed_after_failure_UTC_upper_bound=' + now)
print('v1_sha256=' + failure['script_sha256'])
print('v2_sha256=' + failure['new_script_sha256'])
