"""Generate the six FINAL CNF instances (K2/K3/K4 x encoders A/B) with the exact argv fixed by the parent, into a
FRESH directory, and write a receipt (argv, encoder SHA, Python version, stdout/stderr, exit, map, full CNF SHA).
Optionally compares each CNF hash with an earlier CNF whose solver runs / proofs already exist.

python -B make_final_instances.py --outdir ../evidence/final_v1
No file is deleted or overwritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.normpath(os.path.join(HERE, "..", "evidence"))
CLASSES = {
    "K2": ["--quantum", "12", "--ngeneric", "2", "--p4", "12"],
    "K3": ["--quantum", "123", "--ngeneric", "1", "--p4", "123"],
    "K4": ["--quantum", "1234", "--ngeneric", "0", "--p4", "1234"],
}
EARLIER = {("A", "K2"): "k2/a_generic_sb2.cnf", ("B", "K2"): "k2/b_generic_sb2.cnf",
           ("A", "K3"): "k3/a_k3_sb2.cnf", ("B", "K3"): "k3/b_k3_sb2.cnf",
           ("A", "K4"): "k4/a_k4_sb2.cnf", ("B", "K4"): "k4/b_k4_sb2.cnf"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    rec = {"argv": sys.argv, "python": sys.version, "script_sha256": sha(__file__), "instances": []}
    for enc_tag, enc in (("A", "k2_encode_a.py"), ("B", "k2_encode_b.py")):
        enc_path = os.path.join(HERE, enc)
        for cls, args in CLASSES.items():
            cnf = os.path.join(a.outdir, "%s_%s.cnf" % (enc_tag.lower(), cls))
            argv = [sys.executable, "-B", enc_path, "--mode", "generic", "--sb2"] + args + ["--cnf", cnf]
            if enc_tag == "A":
                argv += ["--map", cnf + ".map.json"]
            r = subprocess.run(argv, capture_output=True, text=True)
            item = {"encoder": enc_tag, "class": cls, "argv": argv, "encoder_sha256": sha(enc_path),
                    "exit": r.returncode, "stdout": r.stdout, "stderr": r.stderr, "cnf": os.path.relpath(cnf, EV)}
            if r.returncode == 0:
                item["cnf_sha256"] = sha(cnf)
                item["cnf_bytes"] = os.path.getsize(cnf)
                item["map"] = os.path.relpath(cnf + ".map.json", EV)
                item["map_sha256"] = sha(cnf + ".map.json")
                old = os.path.join(EV, EARLIER[(enc_tag, cls)])
                item["earlier_cnf"] = EARLIER[(enc_tag, cls)]
                item["earlier_cnf_sha256"] = sha(old) if os.path.exists(old) else None
                item["identical_to_earlier"] = item["earlier_cnf_sha256"] == item["cnf_sha256"]
            rec["instances"].append(item)
            print(json.dumps({k: item.get(k) for k in ("encoder", "class", "exit", "cnf_sha256",
                                                        "identical_to_earlier")}), flush=True)
    with open(os.path.join(a.outdir, "INSTANCES_RECEIPT.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    if not all(i["exit"] == 0 for i in rec["instances"]):
        sys.exit("ENCODER FAILURE")


if __name__ == "__main__":
    main()
