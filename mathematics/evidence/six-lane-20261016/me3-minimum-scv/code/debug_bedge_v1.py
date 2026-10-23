"""EXPLORATORY debug: intermediates of me3dual_v3.test_bedge on one failing calibration box."""
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
sl, sh, dl, dh, wh = fmpq(15, 256), fmpq(1, 16), fmpq(1309, 64), fmpq(655, 32), fmpq(1, 320)
sb, db = D.ball(sl, sh), D.ball(dl, dh)
g0, g1, g2, g3 = D.gk_real_generic(acb(sb), acb(db), kap)
whb = arb(wh)
c0 = (2 * kap - 1).sqrt()
zR = acb(1 + db, -(arb(0).union(whb)))
v1 = kap * sb / (kap * sb * zR - (1 - sb) * acb(1, c0))
v2 = kap * sb / (kap * sb * zR - (1 - sb) * acb(1, -c0))
a1, a2, az = abs(v1), abs(v2), 1 / abs(zR)
M5 = 24 * (a1 ** 5 + a2 ** 5 + 3 * az ** 5)
out = {k: str(v) for k, v in {"g0": g0, "g1": g1, "g2": g2, "g3": g3, "v1": v1, "v2": v2, "M5": M5,
                               "imlow": -g1.real - whb * whb * abs(g3.real) / 6 - whb ** 4 * M5 / 120}.items()}
out["test"] = D.test_bedge(sl, sh, dl, dh, wh, kap)
with lane_guard.xopen(RUN + "/debug.json") as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
