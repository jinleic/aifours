#!/usr/bin/env python3
"""Bind the block270 scalar and exact rational universal-bound coefficient; no target evaluation."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import lzma

root = Path(__file__).resolve().parent
source = root / 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
raw = source.read_bytes()
digest = hashlib.sha256(raw).hexdigest()
assert digest == 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
data = json.loads(lzma.decompress(raw))
entry = data['matrices'][270]
assert entry['r'] == 1 and len(entry['values']) == 1 and len(entry['values'][0]) == 2
z = Q(int(entry['values'][0][0]), int(entry['values'][0][1]))
assert z == Q(5994347302661147, 9444732965739290427392) and z > 0
L = 128 ** 4
frame = Q(7, 16 * 45 ** 3)
constant = Q(L) * Q(1, 12) * z * frame * Q(1, 4)
expected = Q(41960431118628029, 2462343096264818688000)
checks = {
    'corrected_data_hash_matches': True,
    'zero_based_block270_is_positive_rank1_scalar': True,
    'exact_rational_coefficient_matches': constant == expected,
    'wrong_twirl_weight_fault_detected': Q(L) * Q(1, 6) * z * frame * Q(1, 4) != expected,
    'wrong_lift_normalization_fault_detected': Q(L) * Q(1, 12) * z * frame * Q(1, 2) != expected,
}
result = {
    'status': 'PASS' if all(checks.values()) else 'FAIL',
    'arithmetic': 'stdlib fractions.Fraction only',
    'source_sha256': digest,
    'source_index_convention': 'zero-based',
    'source_block_index': 270,
    'source_multiplier': str(z),
    'moment_scale_L': L,
    'identity_site_conjugation_weight': '1/12',
    'local_frame_global_purity_lower_bound': str(frame),
    'isometric_lift_s_factor_fourth_power': '1/4',
    'derived_coercive_coefficient': str(constant),
    'checks': checks,
    'scope': 'Source scalar and rational algebra only; does not prove source identity, physical PSD, Haar frame, mathematical proof, target value, formal/human/reviewer or novelty status.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(root / 'frontier-20261028-d4-coercive-constant-source-check-results-v1.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps(result, sort_keys=True))
if result['status'] != 'PASS':
    raise SystemExit(1)
