"""Designed mutations / negative controls for the Part B construction (python-flint arb, 640 bits).

Each mutation alters one ingredient; the definition-first checker check_ph() (or the generator's own exact-sign
gate) must reject it. Positive controls (unmutated, and permutations of the first three states, which the proof
says cannot change the exits) must pass. Ordering mutations are exploratory: an alternative ordering with all
exits >= 0 would be another valid representation, not an error, and is reported as such.
argv[1] = run directory; writes mutations.json (exclusive create).
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
NS = [4, 5, 6, 8, 12]
FS = [fmpq(1), fmpq(1, 2), fmpq(1, 10 ** 6)]
c0, d0 = fmpq(1), fmpq(1)
EPS = arb(2) ** -30
out = {"positive_controls": [], "mutations": [], "order_minus_one": [], "lower_endpoint_with_n": []}
t_start = time.time()


def ph_check(o, t_hat, alpha_index=0):
    ph = L.ph_from_normalized(o["m"], o["W"], t_hat, o["beta"], c0, d0)
    alpha = [arb(0)] * len(o["m"])
    alpha[alpha_index] = arb(1)
    chk = L.check_ph(alpha, ph["T"], ph["a"], ph["b"], ph["c"], eig=False)
    return chk


def summary(chk):
    return {k: chk[k] for k in ["alpha_sum_is_1", "metzler", "rowsum_le_0", "hurwitz_certificate", "transform_match",
                                "transform_worst_abs_upper", "PH_OK"]}


for n in NS:
    for f in FS:
        base = L.construct(n, f)
        assert base["ok_angles"]
        tc = base["t_closed"]
        # positive control: unmutated
        pc = ph_check(base, tc)
        out["positive_controls"].append({"n": n, "f": str(f), "kind": "unmutated", **summary(pc)})
        # positive control: permute the first three states (exits must be unchanged)
        perm = [2, 0, 1] + list(range(3, n))
        o3 = L.construct(n, f, theta_order=perm)
        same = all(bool(o3["t_poly"][i].overlaps(tc[i])) for i in range(n))
        pc3 = ph_check(o3, o3["t_poly"])
        out["positive_controls"].append({"n": n, "f": str(f), "kind": "first-three permuted", "exits_unchanged": same,
                                         **summary(pc3)})
        muts = []
        # MUT-A: perturb the last exit by factor 1 + 2^-30
        ta = list(tc)
        ta[n - 1] = ta[n - 1] * (1 + EPS)
        muts.append(("A_exit_perturbed", ph_check(base, ta), None))
        # MUT-H: all exits scaled (wrong K / normalization)
        th = [x * (1 + EPS) for x in tc]
        muts.append(("H_K_scaled", ph_check(base, th), None))
        # MUT-I: initial vector on state 2 instead of 1
        muts.append(("I_alpha_e2", ph_check(base, tc, alpha_index=1), None))
        # MUT-G: Taylor jet attached in reversed order (n >= 5)
        if n >= 5:
            tg = list(tc[:3]) + list(reversed(tc[3:]))
            muts.append(("G_jet_reversed", ph_check(base, tg), None))
        # MUT-C: rate orientation flipped, m_i = +beta cot theta_i
        oc = L.construct(n, f, orient=+1)
        rem_nonzero = any(not bool(c.contains(0)) for c in oc["rem"])
        try:
            chk_c = ph_check(oc, oc["t_closed"])
        except Exception as e:  # noqa: BLE001
            chk_c = {"PH_OK": False, "error": repr(e)[:160]}
        muts.append(("C_orientation_flipped", chk_c, {"remainder_certified_nonzero": rem_nonzero,
                                                       "one_minus_m_pos": oc["ok_one_minus_m_pos"]}))
        # MUT-D: repeated angle psi -> psi (1 + 1/1000)
        od = L.construct(n, f, rep_angle_scale=fmpq(1001, 1000))
        q_ib = od["q_at_ibeta"]
        q_nonzero = not bool(q_ib.real.contains(0) and q_ib.imag.contains(0))
        muts.append(("D_repeated_angle_scaled", ph_check(od, od["t_closed"]), {"q_ibeta_certified_nonzero": q_nonzero}))
        for name, chk, extra in muts:
            rec = {"n": n, "f": str(f), "mutation": name, "rejected": not chk["PH_OK"]}
            rec.update({k: chk[k] for k in chk if k in ("transform_match", "transform_worst_abs_upper", "rowsum_le_0",
                                                          "metzler", "error")})
            if extra:
                rec.update(extra)
            out["mutations"].append(rec)
        # MUT-B: ordering mutations (exploratory) -- exits forced by the transform for alpha = e_1
        if n >= 5:
            orders = {"special_states_last": list(range(3, n)) + [0, 1, 2],
                      "rotate_theta1_to_end": list(range(1, n)) + [0]}
            for oname, order in orders.items():
                ob = L.construct(n, f, theta_order=order)
                negs = [j + 1 for j in range(n) if bool(ob["t_poly"][j] < 0)]
                undecided = [j + 1 for j in range(n) if not bool(ob["t_poly"][j] < 0) and not bool(ob["t_poly"][j] >= 0)]
                chk_b = ph_check(ob, ob["t_poly"])
                out["mutations"].append({"n": n, "f": str(f), "mutation": "B_order_" + oname,
                                         "certified_negative_exit_states": negs, "undecided_states": undecided,
                                         "rejected": not chk_b["PH_OK"], "rowsum_le_0": chk_b["rowsum_le_0"],
                                         "transform_match": chk_b["transform_match"],
                                         "note": "rejected only via negative exit; else a valid alternative ordering"})
        print(n, str(f), "done", round(time.time() - t_start, 2))

# Order n-1 at beta in band n: sector bound (Theorem 6 / Appendix A) forbids it; the IVT bracket also fails.
for n in range(4, 13):
    for f in FS:
        pi = arb.pi()
        psi = L.band_psi(n, f)
        phi = (pi - psi) / 2
        beta = phi.tan()
        n1 = n - 1
        S1 = 2 * pi - (n1 - 3) * psi
        G_hi = L.G_fun(S1 / 3, S1, phi)
        out["order_minus_one"].append({"n": n, "f": str(f), "sector_violated_beta_gt_cot_pi_over_n_minus_1":
                                       bool(beta > (pi / n1).cot()),
                                       "G_at_S1_over_3_certified_negative": bool(G_hi < 0),
                                       "S1_gt_3psi": bool(S1 > 3 * psi)})

# Exactly at the lower endpoint beta = cot(pi/(n-1)) with n states: G(t0)=0, bracket refused (band rule uses n-1).
for n in range(4, 13):
    o = L.construct(n, fmpq(0))
    out["lower_endpoint_with_n"].append({"n": n, "construction_refused": not o["ok_angles"],
                                         "t_info": o["t_info"]})

pc_ok = all(p["PH_OK"] and p.get("exits_unchanged", True) for p in out["positive_controls"])
core_muts = [m for m in out["mutations"] if not m["mutation"].startswith("B_order_")]
out["summary"] = {"positive_controls_all_pass": pc_ok, "core_mutations": len(core_muts),
                  "core_mutations_rejected": sum(1 for m in core_muts if m["rejected"]),
                  "order_mutations": len(out["mutations"]) - len(core_muts),
                  "order_mutations_rejected": sum(1 for m in out["mutations"]
                                                  if m["mutation"].startswith("B_order_") and m["rejected"]),
                  "order_minus_one_all_sector_violated": all(r["sector_violated_beta_gt_cot_pi_over_n_minus_1"]
                                                             for r in out["order_minus_one"]),
                  "order_minus_one_all_G_negative": all(r["G_at_S1_over_3_certified_negative"]
                                                        for r in out["order_minus_one"]),
                  "lower_endpoint_all_refused": all(r["construction_refused"] for r in out["lower_endpoint_with_n"]),
                  "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/mutations.json") as fh:
    json.dump(out, fh, indent=1)
print("SUMMARY", json.dumps(out["summary"]))
