"""Mutations, version 2 (640-bit balls). Adds to m01 (ph3_mutations_v1.py, unchanged):

1. H corrected. In m01, scaling every exit by 1 + 2^-30 was NOT rejected (0/15). Reason: v = (-T0)^-1 t scales by the
   same factor and T' = D_v^-1 T0 D_v, t' = D_v^-1 t are invariant, so with alpha hard-coded to e_1 the "mutant" is the
   identical representation. Here (a) that invariance is checked entrywise, and (b) the meaningful normalization
   mutation alpha' = e_1 D_v = v_1 e_1 (the proof's formula, with the mutated v_1 = 1 + 2^-30) must be rejected.
2. Ordering exploration. In m01 both tested reorderings kept all exits >= 0 (0/24 rejected), refuting the screen's
   expectation that a wrong ordering yields a negative exit. Here every distinct arrangement of the angle multiset
   {theta1, theta2, theta2, psi^(n-3)} with alpha = e_1 is tried for n = 5, 6, 7 (exits forced by the transform via
   Newton coefficients); certified-negative, undecided and nonnegative counts are recorded and nonnegative ones are
   passed through the checker.
3. Start-state mutations alpha = e_k, k = 2..n, with the proof's exits (must be rejected).
4. Orientation flip m_i = +beta cot theta_i on non-degenerate instances (at n = 4, f = 1 all theta_i = pi/2 and the
   flip is the identity, which is why m01 did not reject it there).
argv[1] = run directory; writes mutations2.json (exclusive create).
"""
import sys
import json
import time
import itertools
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import ph3lib_v1 as L  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 640
EPS = arb(2) ** -30
c0, d0 = fmpq(1), fmpq(1)
out = {"H_invariance": [], "H_corrected": [], "orderings": [], "start_state": [], "orientation": []}
t_start = time.time()


def ph(o, t_hat):
    return L.ph_from_normalized(o["m"], o["W"], t_hat, o["beta"], c0, d0)


for n in [4, 5, 6, 8, 12]:
    for f in [fmpq(1), fmpq(1, 2), fmpq(1, 10 ** 6)]:
        o = L.construct(n, f)
        tc = o["t_closed"]
        p0 = ph(o, tc)
        p1 = ph(o, [x * (1 + EPS) for x in tc])
        same_T = all(bool(p0["T"][i, j].overlaps(p1["T"][i, j])) for i in range(n) for j in range(n))
        out["H_invariance"].append({"n": n, "f": str(f), "T_unchanged_under_exit_scaling": same_T,
                                    "v1_scaled_contains_1": bool(p1["v"][0].contains(1))})
        alpha_formula = [p1["v"][0]] + [arb(0)] * (n - 1)  # alpha' = e_1 D_v with mutated v
        chk = L.check_ph(alpha_formula, p1["T"], p1["a"], p1["b"], p1["c"], eig=False)
        out["H_corrected"].append({"n": n, "f": str(f), "rejected": not chk["PH_OK"],
                                   "alpha_sum_is_1": chk["alpha_sum_is_1"], "transform_match": chk["transform_match"]})
        for k in range(1, n):
            alpha = [arb(0)] * n
            alpha[k] = arb(1)
            chk = L.check_ph(alpha, p0["T"], p0["a"], p0["b"], p0["c"], eig=False)
            out["start_state"].append({"n": n, "f": str(f), "alpha_state": k + 1, "rejected": not chk["PH_OK"],
                                       "transform_match": chk["transform_match"]})
        if f != 1:
            oc = L.construct(n, f, orient=+1)
            rem_nonzero = any(not bool(cc.contains(0)) for cc in oc["rem"])
            try:
                pc = ph(oc, oc["t_closed"])
                chk = L.check_ph(pc["alpha"], pc["T"], pc["a"], pc["b"], pc["c"], eig=False)
                rej = not chk["PH_OK"]
            except Exception as e:  # noqa: BLE001
                rej, chk = True, {"error": repr(e)[:160]}
            out["orientation"].append({"n": n, "f": str(f), "rejected": rej, "remainder_certified_nonzero": rem_nonzero,
                                       "one_minus_m_pos": oc["ok_one_minus_m_pos"]})

for n in [5, 6, 7]:
    types = ["a", "b", "b"] + ["p"] * (n - 3)
    patterns = sorted(set(itertools.permutations(types)))
    for f in [fmpq(1, 2), fmpq(1, 10 ** 6)]:
        counts = {"certified_negative_exit": 0, "undecided": 0, "all_exits_nonneg": 0, "nonneg_and_checker_pass": 0}
        neg_examples = []
        for pat in patterns:
            pool = {"a": [0], "b": [1, 2], "p": list(range(3, n))}
            order = [pool[ch].pop(0) for ch in pat]
            ob = L.construct(n, f, theta_order=order)
            tp = ob["t_poly"]
            negs = [j + 1 for j in range(n) if bool(tp[j] < 0)]
            und = [j + 1 for j in range(n) if not bool(tp[j] < 0) and not bool(tp[j] >= 0)]
            if negs:
                counts["certified_negative_exit"] += 1
                if len(neg_examples) < 6:
                    neg_examples.append({"pattern": "".join(pat), "negative_exit_states": negs})
            elif und:
                counts["undecided"] += 1
            else:
                counts["all_exits_nonneg"] += 1
                pb = ph(ob, tp)
                chk = L.check_ph(pb["alpha"], pb["T"], pb["a"], pb["b"], pb["c"], eig=False)
                counts["nonneg_and_checker_pass"] += int(chk["PH_OK"])
        out["orderings"].append({"n": n, "f": str(f), "distinct_arrangements": len(patterns), **counts,
                                 "negative_examples": neg_examples})
        print(n, str(f), counts, round(time.time() - t_start, 2))

out["summary"] = {
    "H_T_invariant_all": all(r["T_unchanged_under_exit_scaling"] for r in out["H_invariance"]),
    "H_corrected_rejected": sum(r["rejected"] for r in out["H_corrected"]), "H_corrected_total": len(out["H_corrected"]),
    "start_state_rejected": sum(r["rejected"] for r in out["start_state"]), "start_state_total": len(out["start_state"]),
    "orientation_rejected": sum(r["rejected"] for r in out["orientation"]), "orientation_total": len(out["orientation"]),
    "orderings": [{k: r[k] for k in ("n", "f", "distinct_arrangements", "certified_negative_exit", "undecided",
                                     "all_exits_nonneg", "nonneg_and_checker_pass")} for r in out["orderings"]],
    "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/mutations2.json") as fh:
    json.dump(out, fh, indent=1)
print("SUMMARY", json.dumps(out["summary"]))
