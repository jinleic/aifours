"""Extend (do not rerun) the pinned r1 order controls by the new k=3 case
of K5_RESIDUAL_NORMAL_FORM.r2.md. This is only a finite bit-order check.
The continuum-vector projection lemma remains a written proof obligation.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
old_path = root / 'evidence/k5_split_v1/NORMAL_FORM_BIT_CONTROLS_v1.json'
old_bytes = old_path.read_bytes()
if hashlib.sha256(old_bytes).hexdigest() != 'a85a0609ace1ef55af8834b351ac73c61bec790d7c02122c65bd50dc56599edd':
    raise RuntimeError('old control pin mismatch')
old = json.loads(old_bytes)
B = (4, 5, 6, 7)
sets = [frozenset(S) for k in (3, 4) for S in itertools.combinations(B, k)]
vec = lambda S: tuple(int(i in S) for i in range(1, 8))
families = checks = 0
for mask in range(1, 1 << len(sets)):
    family = [S for i, S in enumerate(sets) if (mask >> i) & 1]
    if min(map(len, family)) != 3:
        continue
    families += 1
    chosen = next(S for S in family if len(S) == 3)
    for perm in itertools.permutations(B):
        sigma = dict(zip(B, perm))
        target = frozenset((5, 6, 7))
        if frozenset(sigma[x] for x in chosen) == target:
            image = [frozenset(sigma[x] for x in S) for S in family]
            if min(image, key=vec) != target:
                raise RuntimeError('k3 order failure')
            checks += 1
mixed = 0
for b in range(1, 128):
    S = {k + 1 for k in range(7) if (b >> k) & 1}
    if S & {1, 2, 3}:
        if not vec(S) > vec({5, 6, 7}):
            raise RuntimeError('mixed order failure')
        mixed += 1
negative = min([{4, 5, 6}, {5, 6, 7}], key=vec) != {4, 5, 6}
r = {'old_receipt_sha256': hashlib.sha256(old_bytes).hexdigest(),
     'proof_note_sha256': hashlib.sha256((root/'review/K5_RESIDUAL_NORMAL_FORM.r2.md').read_bytes()).hexdigest(),
     'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'additional_k3_families': families, 'additional_permutation_checks': checks,
     'additional_A_order_checks': mixed, 'combined_family_count': old['families'] + families,
     'combined_permutation_checks': old['family_permutation_checks'] + checks,
     'wrong_leftmost_k3_rejected': negative, 'all_pass': old['all_pass'] is True and negative,
     'scope': 'support-order controls only; projection lemma not computationally proved'}
with Path(sys.argv[1]).open('x') as f:
    json.dump(r, f, indent=1)
print(json.dumps(r))
