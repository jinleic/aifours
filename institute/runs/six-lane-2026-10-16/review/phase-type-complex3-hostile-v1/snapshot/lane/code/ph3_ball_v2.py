"""Ball-arithmetic instance smoke, version 2 (supersedes the consistency tolerances of ph3_ball_v1.py).

Why v2: run b01-ball (v1, 320 bits) flagged 10/98 instances (n = 20, 24, 32) only on the *absolute* radius
threshold 2^-150 for the consistency enclosures q(1), q(i beta) and the division remainder; all PH checks of
those instances passed. Those three quantities are cancellations of coefficients of size up to prod|m_i|, so v2
(i) records the enclosures themselves, (ii) separates "encloses 0" from "radius small", and (iii) measures the
radius relative to the coefficient scale sum_k |q_k| (threshold 2^-100). Precision raised to 640 bits and the
grid extended to n = 48, 64. v1 and its output stay unchanged.

argv[1] = run directory. Writes ball.json (exclusive create). Finite instances only; not an all-n argument.
"""
import sys
import json
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import ph3lib_v1 as L  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 640
NS = list(range(3, 13)) + [16, 20, 24, 32, 48, 64]
FS = [fmpq(1), fmpq(3, 4), fmpq(1, 2), fmpq(1, 4), fmpq(1, 100), fmpq(1, 10 ** 6), fmpq(1, 10 ** 12)]
CD = [(fmpq(1), fmpq(1)), (fmpq(1, 1000), fmpq(1)), (fmpq(50), fmpq(3))]
REL = arb(2) ** -100


def rel_ok(val_ball, scale):
    """encloses 0 and radius <= REL * scale (scale = coefficient magnitude bound)."""
    if hasattr(val_ball, "real") and not isinstance(val_ball, arb):
        inside = bool(val_ball.real.contains(0) and val_ball.imag.contains(0))
        radius = abs(val_ball).upper()
    else:
        inside = bool(val_ball.contains(0))
        radius = val_ball.rad()
    return inside, bool(radius <= REL * scale), L.fstr(radius, 5)


t_start = time.time()
recs = []
all_ok = True
for n in NS:
    for f in FS:
        t1 = time.time()
        o = L.construct(n, f)
        pi = arb.pi()
        beta = o["beta"]
        r = {"n": n, "f": str(f), "beta": L.fstr(beta, 20), "t_info": o["t_info"]}
        upper_cot = (pi / n).cot()
        lower_ok = bool(beta > (pi / (n - 1)).cot()) if n >= 4 else bool(beta > 0)
        upper_ok = bool(beta.overlaps(upper_cot)) if f == 1 else bool(beta < upper_cot)
        r["band_nstar_eq_n"] = lower_ok and upper_ok
        r["ok_angles"] = o["ok_angles"]
        if not o["ok_angles"]:
            r["OK"] = False
            all_ok = False
            recs.append(r)
            print(n, f, "ANGLE FAILURE", o["t_info"])
            continue
        r["theta1"] = L.fstr(o["thetas"][0], 15)
        r["m1"] = L.fstr(o["m"][0], 15)
        r["G_at_t_contains_0"] = o["G_at_t_contains_0"]
        r["one_minus_m_pos"] = o["ok_one_minus_m_pos"]
        r["W"] = L.fstr(o["W"], 15)
        r["ck_pos"] = o["ok_ck_pos_k_le_n_minus_4"]
        q = L.poly_from_roots(o["m"])
        q[0] = q[0] - o["W"]
        scale = arb(0)
        for cq in q:
            scale = scale + abs(cq)
        scale = scale.upper()
        r["q_coeff_scale"] = L.fstr(scale, 5)
        i1, s1, rad1 = rel_ok(o["q_at_1"], scale)
        i2, s2, rad2 = rel_ok(o["q_at_ibeta"], scale * (1 + beta) ** n)
        rem_in = all(bool(c.contains(0)) for c in o["rem"])
        rem_small = all(bool(c.rad() <= REL * scale) for c in o["rem"])
        r["q1_encloses_0"], r["q1_rel_small"], r["q1_radius"] = i1, s1, rad1
        r["q_ibeta_encloses_0"], r["q_ibeta_rel_small"], r["q_ibeta_radius"] = i2, s2, rad2
        r["remainder_encloses_0"], r["remainder_rel_small"] = rem_in, rem_small
        r["P_monic"] = bool(o["P"][-1].contains(1))
        tc, tp = o["t_closed"], o["t_poly"]
        r["exits_closed_vs_poly_overlap"] = all(bool(tc[i].overlaps(tp[i])) for i in range(n))
        r["exits_pos_j_ge_3"] = all(bool(tc[i] > 0) for i in range(2, n))
        r["exits_zero_j_le_2"] = all(bool(tc[i] == 0) for i in range(2))
        r["min_exit_hat_j_ge_4"] = L.fstr(min(tc[3:], key=lambda b: float(b.mid())), 10) if n >= 4 else None
        M = L.cycle_matrix(o["m"], o["W"])
        uu = o["perron_u"]
        Mu_ok = True
        for i in range(n):
            s_ = arb(0)
            for j in range(n):
                s_ = s_ + M[i, j] * uu[j]
            if not (s_ - uu[i]).contains(0):
                Mu_ok = False
        r["perron_Mu_eq_u"] = Mu_ok and all(bool(x > 0) for x in uu)
        keys = ["band_nstar_eq_n", "ok_angles", "G_at_t_contains_0", "one_minus_m_pos", "ck_pos",
                "q1_encloses_0", "q1_rel_small", "q_ibeta_encloses_0", "q_ibeta_rel_small",
                "remainder_encloses_0", "remainder_rel_small", "P_monic",
                "exits_closed_vs_poly_overlap", "exits_pos_j_ge_3", "exits_zero_j_le_2", "perron_Mu_eq_u"]
        core_ok = all(r[k] for k in keys)
        r["failed_keys"] = [k for k in keys if not r[k]]
        r["ph"] = []
        for (c, delta) in CD:
            ph = L.ph_from_normalized(o["m"], o["W"], tc, beta, c, delta)
            v = ph["v"]
            chk = L.check_ph(ph["alpha"], ph["T"], ph["a"], ph["b"], ph["c"], eig=(n <= 16))
            chk["v_pos"] = all(bool(x > 0) for x in v)
            chk["v1_contains_1"] = bool(v[0].contains(1))
            chk["c"], chk["a_minus_c"] = str(c), str(delta)
            r["ph"].append(chk)
            if not (chk["PH_OK"] and chk["v_pos"] and chk["v1_contains_1"]
                    and chk.get("eig_all_re_neg", True) and chk.get("eig_contains_poles", True)):
                core_ok = False
                r["failed_keys"].append(f"ph(c={c},a-c={delta})")
        r["OK"] = core_ok
        r["seconds"] = round(time.time() - t1, 3)
        all_ok = all_ok and core_ok
        recs.append(r)
        print(n, str(f), "OK" if core_ok else "FAIL " + ",".join(r["failed_keys"]), r["seconds"])

summary = {"prec_bits": 640, "n_values": NS, "f_values": [str(f) for f in FS], "cd_values": [[str(c), str(d)] for c, d in CD],
           "instances": len(recs), "ph_checks": sum(len(r.get("ph", [])) for r in recs), "ALL_OK": all_ok,
           "n_ok": sum(1 for r in recs if r.get("OK")), "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/ball.json") as fh:
    json.dump({"summary": summary, "records": recs}, fh, indent=1)
print("SUMMARY", json.dumps(summary))
