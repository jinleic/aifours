#!/usr/bin/env python3
"""README E11d: builder input controls (standard library).  Corrupted copies of the Appendix B
transcription and wrong GCDCQS inputs must make code/build_mcdsqs128.py abort with the intended
AssertionError before it writes any output.  Corrupted inputs are retained in OUTDIR.
Usage: e11_builder_input_controls.py TRANSCRIPTION.json GCDCQS_CERT KEMPE_MUTANT G8_CERT OUTDIR"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402


def main():
    trp, cert, kempe, g8, outdir = sys.argv[1:6]
    os.mkdir(outdir)
    tr = json.load(open(trp))
    tr_muts = {
        "tr_base_block_digit": (lambda d: d["base_blocks"].__setitem__(5, [0, 1, 7, 31]), r"not an SQS\(32\)"),
        "tr_drop_base_block": (lambda d: d["base_blocks"].pop(12), r"1208 blocks, expected 1240"),
        "tr_part_triple_digit": (lambda d: d["parts"][15].__setitem__(7, [23, 24, 28]),
                                 r"class is not a partial parallel class"),
        "tr_parts_move_triple": (lambda d: d["parts"][0].append(d["parts"][1].pop(0)),
                                 r"class is not a partial parallel class"),
    }
    cases = {}
    for name, (f, rx) in tr_muts.items():
        d = json.loads(json.dumps(tr))
        f(d)
        p = os.path.join(outdir, name + ".json")
        with xopen(p) as fh:
            json.dump(d, fh, indent=1)
        cases[name] = (cert, p, rx)
    cases["gcdcqs_kempe_15_avoiding"] = (kempe, trp, r"point 0: 15 hole-avoiding classes")
    cases["gcdcqs_wrong_order_g8"] = (g8, trp, r"GCDCQS header")
    res, ok_all = {}, True
    for name, (c, t, rx) in cases.items():
        outp = os.path.join(outdir, name + ".must-not-exist.txt")
        r = subprocess.run([sys.executable, os.path.join(HERE, "build_mcdsqs128.py"), c, t, outp],
                           capture_output=True, text=True)
        last = (r.stderr.strip().splitlines() or [""])[-1]
        ok = r.returncode != 0 and last.startswith("AssertionError") and re.search(rx, last) is not None \
            and not os.path.exists(outp)
        res[name] = {"gcdcqs_input": [c, hashlib.sha256(open(c, "rb").read()).hexdigest()],
                     "transcription_input": [t, hashlib.sha256(open(t, "rb").read()).hexdigest()],
                     "returncode": r.returncode, "error": last, "output_written": os.path.exists(outp),
                     "as_intended": ok}
        ok_all &= ok
        print(name, "|", last, "|", ok)
    summary = {"builder": os.path.join(HERE, "build_mcdsqs128.py"), "controls": len(res),
               "as_intended": sum(v["as_intended"] for v in res.values()), "results": res}
    with xopen(os.path.join(outdir, "builder-input-control-results.json")) as fh:
        json.dump(summary, fh, indent=1)
    print(f"{summary['as_intended']}/{summary['controls']} builder input controls as intended")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
