from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

p = Path(__file__).resolve().parent
old = (p / 'reviewer-control-v1.py').read_bytes()
text = old.decode()
replacements = [
    ('reviewer-control-receipt-v1.json', 'reviewer-control-receipt-v2.json', 2),
    ('from itertools import product', 'from itertools import permutations, product', 1),
    ("    # Non-normal six-element band, concretely verified, with generator-swap\n    # automorphism. Words with both letters reduce to their first/last letters.\n    band = ['a', 'b', 'ab', 'ba', 'aba', 'bab']\n    def reduce_word(w):\n        if len(set(w)) == 1:\n            return w[0]\n        if w[0] != w[-1]:\n            return w[0] + w[-1]\n        return w[0] + ('b' if w[0] == 'a' else 'a') + w[0]", "    # Non-normal 15-element left regular band: nonempty words on abc with\n    # no repeated letter; multiplication retains each letter's first occurrence.\n    # The action swaps a,b and fixes c.\n    band = [''.join(w) for k in range(1, 4) for w in permutations('abc', k)]\n    def reduce_word(w):\n        return ''.join(dict.fromkeys(w))", 1),
    ("need(len(idempotents(bt)) == 6, 'B not a band')", "need(len(idempotents(bt)) == 15, 'B not a band')", 1),
    ('product(range(6), repeat=3)', 'product(range(len(band)), repeat=3)', 1),
    ('len(he) == len(ue) == 24', 'len(he) == len(ue) == 60', 1),
    ('96->48 Pastijn quotient, nontrivial action, 24 unique idempotent lifts, group fibers, 576 order pairs',
     '240->120 Pastijn quotient, nontrivial action, 60 unique idempotent lifts, group fibers, 3600 order pairs', 1),
]
for before, after, expected in replacements:
    if text.count(before) != expected:
        raise RuntimeError('replacement count: ' + before)
    text = text.replace(before, after)
now = datetime.now(timezone.utc).isoformat()
failure = {
    'kind': 'REVIEWER_CONTROL_FAILED_ATTEMPTS',
    'observed_after_failures_UTC_upper_bound': now,
    'script': 'reviewer-control-v1.py',
    'script_sha256': sha256(old).hexdigest(),
    'tool_observed_exit_code': 1,
    'tool_observed_exception': 'ControlFailure: test band unexpectedly normal',
    'failure_source': 'Reviewer incorrectly selected a six-element normal band as a non-normal fixture.',
    'meaning': 'This failed reviewer premise is not evidence of a candidate defect; no success receipt was emitted.',
    'failed_derivation': {
        'script': 'reviewer-derive-control-v2.py',
        'sha256': sha256((p / 'reviewer-derive-control-v2.py').read_bytes()).hexdigest(),
        'exit_code': 1,
        'exception': 'RuntimeError: replacement must match once: reviewer-control-receipt-v1.json',
        'cause': 'Receipt filename occurs twice (docstring and actual target), not once.',
        'outputs_created_before_failure': [],
    },
    'repair': 'Preserve old scripts unchanged; v2 uses a verified 15-element left regular band on three generators.',
    'new_script_sha256': sha256(text.encode()).hexdigest(),
}
with (p / 'reviewer-control-attempt-v1.json').open('x') as f:
    f.write(json.dumps(failure, indent=2) + '\n')
with (p / 'reviewer-control-v2.py').open('x') as f:
    f.write(text)
print('Preserved failed scripts; created v2 with a non-normal three-generator left regular band.')
print('observed_after_failures_UTC_upper_bound=' + now)
print('v1_sha256=' + failure['script_sha256'])
print('v2_sha256=' + failure['new_script_sha256'])
