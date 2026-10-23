"""EXPLORATORY debug: evaluate the general-chart dual test on one failing calibration box and print intermediates."""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3dual_v3 as D  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128
kap = arb(fmpq(50, 61))
out = []
for (sl, sh, dl, dh, wl, wh) in [((15, 256), (1, 16), (2291, 128), (1146, 64), (763, 128), (191, 32))]:
    sl, sh, dl, dh, wl, wh = [fmpq(*x) for x in (sl, sh, dl, dh, wl, wh)]
    sb, db, wb = D.ball(sl, sh), D.ball(dl, dh), D.ball(wl, wh)
    W = D.W_generic(acb(sb), acb(db), acb(wb), kap)
    rec = {"W": str(W), "absW": str(abs(W)), "argW": str(W.arg()),
           "small_rhs": str((-2 * arb.pi() * db / wb).exp())}
    c, mode = D._branch_const(W)
    rec["mode"] = mode
    if mode:
        alpha = W.arg() + c
        rec["phi"] = str(wb * abs(W).log() + db * alpha)
    for sv in [sl, (sl + sh) / 2, sh]:
        Wp = D.W_generic(acb(arb(sv)), acb(arb((dl + dh) / 2)), acb(arb((wl + wh) / 2)), kap)
        rec[f"W_at_s={float(sv):.5f}"] = [str(Wp), str(Wp.arg())]
    rec["test"] = D.test_general(sl, sh, dl, dh, wl, wh, kap, None)
    out.append(rec)
with lane_guard.xopen(RUN + "/debug.json") as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
