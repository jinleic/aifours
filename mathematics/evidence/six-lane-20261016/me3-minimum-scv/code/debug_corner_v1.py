"""EXPLORATORY debug: intermediates of me3dual_v7.test_corner on one failing calibration box (k04-cal-SWC)."""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3dual_v7 as D  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128
kap = arb(fmpq(50, 61))
sl, sh = fmpq(919, 1024), fmpq(115, 128)
out = {}
for (dl, dh, wl, wh) in [(fmpq(0), fmpq(1, 1280), fmpq(0), fmpq(1, 1280)), (fmpq(1, 1280), fmpq(2, 1280), fmpq(1, 1280), fmpq(2, 1280))]:
    sb, db, wb = D.ball(sl, sh), D.ball(dl, dh), D.ball(wl, wh)
    N1 = D.N1f(sb, kap)
    A = (2 * kap * sb * sb - 2 * sb * (1 - sb)) / N1
    B = kap * sb * sb / N1
    psi, ig = D.corner_series_stable(acb(sb), acb(db), acb(wb), kap, 20)
    out[f"{float(dl)}-{float(wh)}"] = {"A": str(A), "B": str(B), "4B-A2": str(4 * B - A * A), "psi": str(psi), "ig": str(ig),
                                       "test": D.test_corner(sl, sh, dl, dh, wl, wh, kap, 20)}
with lane_guard.xopen(RUN + "/debug.json") as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
