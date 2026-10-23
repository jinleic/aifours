#!/usr/bin/env python3
"""moduli_cert_tests.py: controls for large_t_gen.verify_moduli_certificate (lane ame46-support).

 NEG1 (intended reason): Pandya's N with w = +1 on every hole line of pair {1,2} and -1 on every hole line of pair
      {3,4}. Then A^T w = 0 and b^T w = 0 while w != 0. It must be REJECTED: such a w gives no contradiction.
 NEG2: Pandya's N with w = +1 on one hole line only. Then b^T w = 1 > 0, so it must be REJECTED.
 NEG3: Pandya's N with w = -1 on one hole line. Then A^T w has negative entries, so it must be REJECTED.
 POS1: toy N = {0000, 0011}. Its hole lines force m_0000 = m_0011 = 1 (pair {3,4}) and m_0000 + m_0011 = 1 (pair
      {1,2}), so no positive moduli exist. The certificate found by moduli_certificate must be ACCEPTED, and the
      hand certificate w = +1 on the {1,2}-line (0,0), -1 on both {3,4}-lines must be ACCEPTED.
 SEARCH: moduli_certificate(Pandya's N) returns None (m = 1/2 is feasible), and the t = 30 representative also
      returns None.
Writes evidence/moduli_cert_tests.json; exit status 0 iff all outcomes match.
"""
import json
import os
import sys

import large_t_gen as g
import pandya_control as pc

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    W = pc.build()
    N = [x for x, v in W.items() if v != pc.R2]
    S, lines = g.hole_lines(N)
    res = {}
    w1 = [1 if P == (0, 1) else (-1 if P == (2, 3) else 0) for P, z, L in lines]
    res["NEG1_ATw0_bTw0_rejected"] = not g.verify_moduli_certificate(N, w1)
    w2 = [0] * len(lines)
    w2[0] = 1
    res["NEG2_bTw_positive_rejected"] = not g.verify_moduli_certificate(N, w2)
    w3 = [0] * len(lines)
    w3[0] = -1
    res["NEG3_ATw_negative_rejected"] = not g.verify_moduli_certificate(N, w3)
    toy = [(0, 0, 0, 0), (0, 0, 1, 1)]
    cert = g.moduli_certificate(toy)
    res["POS1_found_and_verified"] = bool(cert is not None and cert["verified"])
    St, lt = g.hole_lines(toy)
    wh = [1 if (P == (0, 1) and z == (0, 0)) else (-1 if P == (2, 3) else 0) for P, z, L in lt]
    res["POS1_hand_certificate_accepted"] = g.verify_moduli_certificate(toy, wh)
    res["SEARCH_pandya_none"] = g.moduli_certificate(N) is None
    rep30 = [tuple(int(c) for c in s) for s in ["4343", "4354", "4434", "4445", "4533", "4555", "5343", "5354",
                                                "5434", "5445", "5533", "5555"]]
    res["SEARCH_t30_rep_none"] = g.moduli_certificate(rep30) is None
    res["all_required_true"] = all(res.values())
    with open(os.path.join(HERE, "..", "evidence", "moduli_cert_tests.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
    sys.exit(0 if res["all_required_true"] else 1)


if __name__ == "__main__":
    main()
