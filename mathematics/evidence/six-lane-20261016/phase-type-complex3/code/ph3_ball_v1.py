"""Ball-arithmetic instance smoke (python-flint arb, 320 bits) of the Part B construction + definition-first checker.

argv[1] = run directory. Writes ball.json (exclusive create). Finite instances only; not an all-n argument.
Grid: n in 3..12 and 16,20,24,32; band fraction f in {1 (upper endpoint), 3/4, 1/2, 1/4, 1/100, 1e-6, 1e-12}
(f -> 0 approaches the excluded lower endpoint beta = cot(pi/(n-1))); original-time (c, a-c) in
{(1,1), (1/1000,1), (50,3)}, so a = c + (a-c), b = beta (a-c).
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
flint.ctx.prec = 320
NS = list(range(3, 13)) + [16, 20, 24, 32]
FS = [fmpq(1), fmpq(3, 4), fmpq(1, 2), fmpq(1, 4), fmpq(1, 100), fmpq(1, 10 ** 6), fmpq(1, 10 ** 12)]
CD = [(fmpq(1), fmpq(1)), (fmpq(1, 1000), fmpq(1)), (fmpq(50), fmpq(3))]
TOL = arb(2) ** -150

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
        # band membership: n* = n
        upper_cot = (pi / n).cot()
        if n >= 4:
            lower_ok = bool(beta > (pi / (n - 1)).cot())
        else:
            lower_ok = bool(beta > 0)
        if f == 1:
            upper_ok = bool(beta.overlaps(upper_cot))
        else:
            upper_ok = bool(beta < upper_cot)
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
        r["q1_contains_0"] = bool(o["q_at_1"].contains(0)) and bool(o["q_at_1"].rad() < TOL)
        qib = o["q_at_ibeta"]
        r["q_ibeta_contains_0"] = bool(qib.real.contains(0) and qib.imag.contains(0) and abs(qib).upper() < TOL)
        r["remainder_contains_0"] = all(bool(c.contains(0)) and bool(c.rad() < TOL) for c in o["rem"])
        r["P_monic"] = bool(o["P"][-1].contains(1))
        tc, tp = o["t_closed"], o["t_poly"]
        r["exits_closed_vs_poly_overlap"] = all(bool(tc[i].overlaps(tp[i])) for i in range(n))
        r["exits_pos_j_ge_3"] = all(bool(tc[i] > 0) for i in range(2, n))
        r["exits_zero_j_le_2"] = all(bool(tc[i] == 0) for i in range(2))
        r["min_exit_hat"] = L.fstr(min(tc[2:], key=lambda b: float(b.mid())), 10)
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
        core_ok = all(r[k] for k in ["band_nstar_eq_n", "ok_angles", "G_at_t_contains_0", "one_minus_m_pos", "ck_pos",
                                     "q1_contains_0", "q_ibeta_contains_0", "remainder_contains_0", "P_monic",
                                     "exits_closed_vs_poly_overlap", "exits_pos_j_ge_3", "exits_zero_j_le_2",
                                     "perron_Mu_eq_u"])
        r["ph"] = []
        for (c, delta) in CD:
            ph = L.ph_from_normalized(o["m"], o["W"], tc, beta, c, delta)
            v = ph["v"]
            chk = L.check_ph(ph["alpha"], ph["T"], ph["a"], ph["b"], ph["c"], eig=(n <= 12))
            chk["v_pos"] = all(bool(x > 0) for x in v)
            chk["v1_contains_1"] = bool(v[0].contains(1))
            chk["c"], chk["a_minus_c"] = str(c), str(delta)
            r["ph"].append(chk)
            if not (chk["PH_OK"] and chk["v_pos"] and chk["v1_contains_1"]
                    and chk.get("eig_all_re_neg", True) and chk.get("eig_contains_poles", True)):
                core_ok = False
        r["OK"] = core_ok
        r["seconds"] = round(time.time() - t1, 3)
        all_ok = all_ok and core_ok
        recs.append(r)
        print(n, str(f), "OK" if core_ok else "FAIL", r["seconds"], "m1", r["m1"][:20], "min_exit", r["min_exit_hat"][:20])

summary = {"prec_bits": 320, "n_values": NS, "f_values": [str(f) for f in FS], "cd_values": [[str(c), str(d)] for c, d in CD],
           "instances": len(recs), "ph_checks": sum(len(r.get("ph", [])) for r in recs), "ALL_OK": all_ok,
           "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/ball.json") as fh:
    json.dump({"summary": summary, "records": recs}, fh, indent=1)
print("SUMMARY", json.dumps(summary))
