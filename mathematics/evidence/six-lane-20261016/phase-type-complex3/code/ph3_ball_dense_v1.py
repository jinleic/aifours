"""Dense bounded falsification sweep (python-flint balls; finite smoke, not proof). Run after the candidate pin.

For every band n = 3..40: f = k/40 (k = 1..40, f = 1 is the upper endpoint) plus f = 1e-3 and 1e-9; for n in
{64, 100, 128}: f in {1, 1/2, 1e-9}. Per instance: certified angle bracket, 1 - m_i > 0, c_k > 0 (k <= n-4),
exits closed form vs polynomial route, enclosures of q(1), q(i beta), remainder (relative radius 2^-100), Perron
vector, then the definition-first checker in original units for (c, a-c) = (1, 1) and one seeded log-uniform pair in
[1e-3, 1e3]^2. Precision: 640 bits for n <= 40, 2048 bits for n >= 64.
argv[1] = run directory; writes dense.json (exclusive create).
"""
import sys
import json
import time
import random
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import ph3lib_v1 as L  # noqa: E402

RUN = sys.argv[1]
SEED = 1018
rng = random.Random(SEED)
REL = arb(2) ** -100
grid = []
for n in range(3, 41):
    for k in range(1, 41):
        grid.append((n, fmpq(k, 40)))
    grid.append((n, fmpq(1, 1000)))
    grid.append((n, fmpq(1, 10 ** 9)))
for n in (64, 100, 128):
    for f in (fmpq(1), fmpq(1, 2), fmpq(1, 10 ** 9)):
        grid.append((n, f))

t_start = time.time()
fails = []
n_inst = 0
n_ph = 0
worst_tr = {}
for (n, f) in grid:
    flint.ctx.prec = 640 if n <= 40 else 2048
    o = L.construct(n, f)
    n_inst += 1
    bad = []
    if not o["ok_angles"]:
        fails.append({"n": n, "f": str(f), "failed": ["angles"], "t_info": o["t_info"]})
        continue
    pi = arb.pi()
    beta = o["beta"]
    if n >= 4 and not bool(beta > (pi / (n - 1)).cot()):
        bad.append("band_lower")
    if f == 1:
        if not bool(beta.overlaps((pi / n).cot())):
            bad.append("band_upper_eq")
    elif not bool(beta < (pi / n).cot()):
        bad.append("band_upper")
    for key in ("ok_one_minus_m_pos", "ok_ck_pos_k_le_n_minus_4", "G_at_t_contains_0"):
        if not o[key]:
            bad.append(key)
    q = L.poly_from_roots(o["m"])
    q[0] = q[0] - o["W"]
    scale = arb(0)
    for cq in q:
        scale = scale + abs(cq)
    scale = scale.upper()
    q1 = o["q_at_1"]
    if not (bool(q1.contains(0)) and bool(q1.rad() <= REL * scale)):
        bad.append("q1")
    qi = o["q_at_ibeta"]
    if not (bool(qi.real.contains(0)) and bool(qi.imag.contains(0)) and bool(abs(qi).upper() <= REL * scale * (1 + beta) ** n)):
        bad.append("q_ibeta")
    if not all(bool(c.contains(0)) and bool(c.rad() <= REL * scale) for c in o["rem"]):
        bad.append("remainder")
    tc, tp = o["t_closed"], o["t_poly"]
    if not all(bool(tc[i].overlaps(tp[i])) for i in range(n)):
        bad.append("exits_closed_vs_poly")
    if not all(bool(tc[i] > 0) for i in range(2, n)):
        bad.append("exits_pos")
    M = L.cycle_matrix(o["m"], o["W"])
    uu = o["perron_u"]
    for i in range(n):
        s_ = arb(0)
        for j in range(n):
            s_ = s_ + M[i, j] * uu[j]
        if not (s_ - uu[i]).contains(0):
            bad.append("perron")
            break
    lc, ld = rng.uniform(-3, 3), rng.uniform(-3, 3)
    cr = fmpq(int(round(10 ** lc * 10 ** 6)), 10 ** 6) if lc > -3 else fmpq(1, 1000)
    dr = fmpq(int(round(10 ** ld * 10 ** 6)), 10 ** 6) if ld > -3 else fmpq(1, 1000)
    for (c, delta) in ((fmpq(1), fmpq(1)), (cr, dr)):
        ph = L.ph_from_normalized(o["m"], o["W"], tc, beta, c, delta)
        chk = L.check_ph(ph["alpha"], ph["T"], ph["a"], ph["b"], ph["c"], eig=False)
        n_ph += 1
        if not (chk["PH_OK"] and all(bool(x > 0) for x in ph["v"]) and bool(ph["v"][0].contains(1))):
            bad.append(f"ph(c={c},a-c={delta}):" + ",".join(k for k, v in chk.items() if v is False))
        worst_tr[n] = max(worst_tr.get(n, 0.0), float(arb(chk["transform_worst_abs_upper"].split(" +/-")[0].strip("["))))
    if bad:
        fails.append({"n": n, "f": str(f), "failed": bad})
    if n_inst % 200 == 0:
        print("progress", n_inst, len(fails), round(time.time() - t_start, 1), flush=True)

summary = {"seed": SEED, "instances": n_inst, "ph_checks": n_ph, "failures": len(fails), "ALL_OK": not fails,
           "worst_transform_abs_by_n": {str(k): v for k, v in sorted(worst_tr.items())},
           "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/dense.json") as fh:
    json.dump({"summary": summary, "failures": fails}, fh, indent=1)
print("SUMMARY", json.dumps(summary))
