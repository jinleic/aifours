from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
p = Path(__file__).resolve().parent
old = (p / 'reviewer-control-v2.py').read_bytes()
s = old.decode()
changes = [
    ('reviewer-control-receipt-v2.json', 'reviewer-control-receipt-v3.json', 2),
    ('    e, f = labels.index((0, 0, 0)), labels.index((1, 1, 1))',
     '    e9, f9 = labels.index((0, 0, 0)), labels.index((1, 1, 1))', 1),
    ('    ef = s[e][f]', '    ef = s[e9][f9]', 1),
    ("need(e in es and f in es and ef == labels.index((0, 1, 1)), 'e/f/product mismatch')",
     "need(e9 in es and f9 in es and ef == labels.index((0, 1, 1)), 'e/f/product mismatch')", 1),
    ('    mutated[0][e] = e', '    mutated[0][e9] = e9', 1),
    ("'e_f_ef_ef_squared': [e, f, ef, s[ef][ef]]", "'e_f_ef_ef_squared': [e9, f9, ef, s[ef][ef]]", 1),
    ("'change': [0, e, s[0][e], mutated[0][e]]", "'change': [0, e9, s[0][e9], mutated[0][e9]]", 1),
]
for before, after, n in changes:
    if s.count(before) != n:
        raise RuntimeError('unexpected replacement count: ' + before)
    s = s.replace(before, after)
now = datetime.now(timezone.utc).isoformat()
failure = {
    'kind': 'REVIEWER_CONTROL_FAILED_ATTEMPT',
    'observed_after_failure_UTC_upper_bound': now,
    'script': 'reviewer-control-v2.py',
    'script_sha256': sha256(old).hexdigest(),
    'tool_observed_exit_code': 1,
    'tool_observed_exception': 'IndexError: list index out of range',
    'failure_site': "return receipt field 'change': [0, e, s[0][e], mutated[0][e]]",
    'cause': 'Reviewer reused e/f as loop variables in the larger quotient control, shadowing nine-element labels.',
    'evidence_limit': 'v2 reached receipt assembly but emitted no receipt; no successful v2 run is claimed.',
    'repair': 'v3 names the nine-element labels e9/f9 and preserves v2 unchanged.',
    'new_script_sha256': sha256(s.encode()).hexdigest(),
}
with (p / 'reviewer-control-attempt-v2.json').open('x') as f:
    f.write(json.dumps(failure, indent=2) + '\n')
with (p / 'reviewer-control-v3.py').open('x') as f:
    f.write(s)
print('observed_after_failure_UTC_upper_bound=' + now)
print('v3_sha256=' + failure['new_script_sha256'])
