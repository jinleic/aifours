#!/usr/bin/env python3
"""reviewer-exact-reproduction-v1.py

Reviewer's exact reproduction of the state-dependent figures QUOTED in
frontier-20261028-98-rank6-global-k10.md section 4 (and printed by the
read-only author checker 97), using only the reviewer's own exact library
(reviewer-exact-controls-v1.py).  No author code is imported or executed.

Quoted (packet 98 section 4), for the projector spanned by
(24|0000>+7|1111>)/25, |0001>, |0010>, |0011>, |0100>, |1000> and the state
(2|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/3:
   Tr Q (H1(rho) + spinflip(rho)) = 79606/5625  (>= 7)
   Tr Q H2(rho)                   = 67243/5625  (>= 1)
   Tr[Q Phi_{2/3}(rho)] = Tr[spinflip(Q) Phi_{4/3}(rho)] = 68864/151875 > 13/81
   remainder at p=2/3 of the retained-erasure bound = (3 rho + F(rho)/2)/81

Packet 100's state-dependent figures are NOT reproduced here: its text does not
name which five/six weight-two basis vectors its rank-10/11 projectors use.

Run: python3 -B reviewer-exact-reproduction-v1.py
"""
import importlib
import json
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
L = importlib.import_module('reviewer-exact-controls-v1')


def main():
    t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    va = L.vec({0: Fr(24, 25), 15: Fr(7, 25)})
    Q = L.proj([va, L.ket(1), L.ket(2), L.ket(3), L.ket(4), L.ket(8)])
    assert L.is_projector(Q, 6)
    psi = L.vec({0: Fr(2, 3), 5: Fr(1, 3), 6: Fr(1, 3), 9: Fr(1, 3), 10: Fr(1, 3), 15: Fr(1, 3)})
    assert L.inner(psi, psi) == L.ONE
    rho = L.proj([psi])
    h1, h2, sfr, F = L.H1(rho), L.H2(rho), L.spinflip(rho), L.F_map(rho)
    ident = L.meq(L.madd(L.msub(h2, h1), L.eye(L.D)), L.madd(L.madd(rho, sfr), L.mscale(F, Fr(1, 2))))
    t1 = L.tr_prod(Q, L.madd(h1, sfr))
    t2 = L.tr_prod(Q, h2)
    p = Fr(2, 3)
    out23 = L.channel(rho, p)
    out43 = L.channel(rho, Fr(4, 3))
    tq23 = L.tr_prod(Q, out23)
    tq43 = L.tr_prod(L.spinflip(Q), out43)
    t, b = 1 - p, p / 2
    lower = L.madd(L.madd(L.eye(L.D, b ** 4), L.mscale(h1, t * b ** 3)), L.mscale(h2, t ** 2 * b ** 2))
    rem = L.msub(out23, lower)
    rem_claim = L.mscale(L.madd(L.mscale(rho, 3), L.mscale(F, Fr(1, 2))), Fr(1, 81))
    results = {
        'identity_(8)_exact_on_this_state': ident,
        'trQ(H1+spinflip)': str(t1.re), 'quoted': '79606/5625', 'match_1': t1 == L.G(Fr(79606, 5625)),
        'trQH2': str(t2.re), 'quoted_2': '67243/5625', 'match_2': t2 == L.G(Fr(67243, 5625)),
        'trQ_Phi_2/3': str(tq23.re), 'tr_sfQ_Phi_4/3': str(tq43.re), 'quoted_3': '68864/151875',
        'match_3': tq23 == L.G(Fr(68864, 151875)) and tq43 == L.G(Fr(68864, 151875)),
        'product_bottom6_at_2/3': str(L.ref_bottom(6, p)), 'quoted_bottom6': '13/81',
        'match_bottom6': L.ref_bottom(6, p) == Fr(13, 81),
        'remainder_equals_(3rho+F/2)/81': L.meq(rem, rem_claim),
        'sequential_equals_expansion_at_2/3_and_4/3': L.meq(out23, L.channel_expansion(rho, p)) and L.meq(out43, L.channel_expansion(rho, Fr(4, 3))),
    }
    ok = all(v for k, v in results.items() if isinstance(v, bool))
    out = {'scope': 'exact reproduction of packet-98 quoted finite figures with reviewer code; one state and one projector; not a universal proof',
           'receipts': {'clock_start_utc': t0, 'clock_end_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                        'script_sha256': L.sha256_file(os.path.abspath(__file__)),
                        'library_sha256': L.sha256_file(os.path.join(HERE, 'reviewer-exact-controls-v1.py'))},
           'all_quoted_figures_reproduced': ok, 'results': results}
    with open(os.path.join(HERE, 'reviewer-exact-reproduction-v1.result.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps(out, indent=1, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
