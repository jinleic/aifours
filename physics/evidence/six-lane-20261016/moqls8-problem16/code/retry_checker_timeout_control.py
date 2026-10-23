"""Follow-up to retry_smoke's PHP(8,7), which completed before the 1 s checker limit.
Exercise the SAME certify() path using a larger PHP(11,10) with native solver
limit 120 s and native checker limit 1 s. Record actual outcome; never assume
that a timeout occurred. Intended control: solver UNSAT, checker TIMEOUT, and
strict verified=False. No production leaf is involved.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("retry_smoke", HERE / "retry_smoke.py")
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)

out = HERE.parent / "evidence/k5_split_v1/retry_timeout_control_v1"
out.mkdir(exist_ok=False)
fifos = tuple(str(out / ("w0.%s.fifo" % key)) for key in ("cnf_s", "cnf_c", "proof"))
for path in fifos:
    os.mkfifo(path)
nv, nc, body = S.php(11, 10)
r = S.R.certify("php11_10_checker1s", [], nv, nc, body, str(out), fifos,
                120, 6 * 2 ** 30, checker_limit=1)
r["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
r["control_pass"] = (r["solver_returncode"] == 20 and
                     "s TIMEOUT" in r["checker_status_lines"] and
                     r["verified"] is False)
with (out / "RECEIPT.json").open("x") as f:
    json.dump(r, f, indent=1)
print(json.dumps(r), flush=True)
