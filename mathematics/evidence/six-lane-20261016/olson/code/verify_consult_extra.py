#!/usr/bin/env python3
"""Provenance driver for the extra numbers quoted in verify-consult.md (review fix):
  * p = 13 core results in the same schema as verify_consult.py (sections A, B, C);
  * positive controls: p = 5 with blocks <= 6, 7, 8; p = 7 with blocks <= 9;
  * eight-letter unit sigma_0 rho_1^4 sigma_{-6}^3 depth at p = 3, 5, 7, 11, 13;
  * parity-preserving isolation counter-control (reviewer's suggestion):
      sigma_0^{p-2} rho_1^{p-3} sigma_1^{p-2} rho_1^{p-2} sigma_2^4 rho_1^4  (F = 2p),
    max depth with blocks < p, at p = 7, 11, 13.
Writes evidence/consult_verification.extra.json.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_consult as vc

def iso_control(p):
    runs = [('F', 0, p - 2), ('R', 1, p - 3), ('F', 1, p - 2), ('R', 1, p - 2), ('F', 2, 4), ('R', 1, 4)]
    w = []
    for c, v, l in runs:
        w += [(c, v % p)] * l
    assert len(w) == 4 * p - 1 and sum(1 for c, _ in w if c == 'F') == 2 * p
    return w

def main():
    out = {}
    p = 13
    w = vc.w_family(p)
    r = {'A_membership_tools_true': vc.section_A(p, w), 'B_direct_solution': vc.section_B(p, w),
         'C_max_depth_blocks_lt_p': vc.max_tiling_depth(w, p, p - 1), 'C_target': 2 * p - 1,
         'C_max_depth_blocks_le_p': vc.max_tiling_depth(w, p, p)}
    for var in ('short_first_rot', 'even_middle'):
        r['C_counter_' + var + '_blocks_lt_p'] = vc.max_tiling_depth(vc.w_family(p, var), p, p - 1)
    out['p13_core'] = r
    out['positive_controls'] = {
        'p5_blocks_le_6': vc.max_tiling_depth(vc.w_family(5), 5, 6),
        'p5_blocks_le_7': vc.max_tiling_depth(vc.w_family(5), 5, 7),
        'p5_blocks_le_8': vc.max_tiling_depth(vc.w_family(5), 5, 8),
        'p7_blocks_le_9': vc.max_tiling_depth(vc.w_family(7), 7, 9)}
    out['eight_letter_depth'] = {q: vc.depth([('F', 0)] + [('R', 1)] * 4 + [('F', (-6) % q)] * 3, q)
                                 for q in (3, 5, 7, 11, 13)}
    out['isolation_parity_preserving_control_blocks_lt_p'] = {
        q: {'max_depth': vc.max_tiling_depth(iso_control(q), q, q - 1), 'target': 2 * q - 1,
            'has_solution_dp': vc.ca.has_solution(iso_control(q), q)} for q in (7, 11, 13)}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'evidence', 'consult_verification.extra.json')
    json.dump(out, open(path, 'w'), indent=1)
    print(json.dumps(out))

if __name__ == '__main__':
    main()
