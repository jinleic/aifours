#!/usr/bin/env python3
"""Re-certification of the E0 independent replication (M2'): the cycle-1 M2' results (m2q0b/,
CaDiCaL LRAT + lrat-check) are UNCERTIFIED because lrat-check is unsound. Here every quad graph
is re-encoded with the unchanged independent encoder encode_q0b.py (CNF captured from its
stdout, trailing JSON summary line removed), solved by CaDiCaL with binary DRAT streamed into
drat-trim (stream_check5, acceptance on drat-trim only). Results: m2q0c/results/gNNN.json.
Usage: run_m2q0c.py LIMIT_S CHECK_BUDGET_S [first last]
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check5 as S  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "m2q0c", "results")


def main():
    limit, budget = float(sys.argv[1]), float(sys.argv[2])
    gs = [l.strip() for l in open(os.path.join(LANE, "data", "quadgraphs-8v-13to16e-D4.g6")) if l.strip()]
    a, b = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, len(gs) - 1)
    os.makedirs(OUT, exist_ok=True)
    for i in range(a, b + 1):
        p = os.path.join(OUT, "g%03d.json" % i)
        if os.path.exists(p):
            continue
        enc = subprocess.run([sys.executable, os.path.join(HERE, "encode_q0b.py"), gs[i], "/dev/stdout"],
                             capture_output=True)
        lines = enc.stdout.split(b"\n")
        while lines and not lines[-1].strip():
            lines.pop()
        info = json.loads(lines.pop().decode())
        cnf = b"\n".join(lines) + b"\n"
        r = S.cadical_drat(cnf, os.path.join(LANE, "scratch", "fifo", "m2q0c_g%03d" % i), limit, budget)
        r.update({"graph_index": i, "graph6": gs[i], "encoder": "encode_q0b.py", "encoder_info": info,
                  "runner": "run_m2q0c.py"})
        r["solver_out"] = ""
        json.dump(r, open(p, "w"), indent=1)
        print(time.strftime("%H:%M:%S"), i, r["status"], r["checked"], r["solve_seconds"], r.get("check_seconds"), flush=True)


if __name__ == "__main__":
    main()
