#!/usr/bin/env python3
"""Run code/verify_cdf.py (as a subprocess) on every fixture in controls/manifest.json and on any extra
certificate paths given on the command line; compare verdict and failing check with the expectation.
Writes a JSON receipt to the path given by --out (default: stdout only)."""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
VERIFY = os.path.join(HERE, "verify_cdf.py")


def run(path):
    t0 = time.time()
    p = subprocess.run([sys.executable, VERIFY, path], capture_output=True, text=True)
    rep = json.loads(p.stdout) if p.stdout.strip() else {}
    return p.returncode, rep, time.time() - t0


def main(argv):
    out = None
    extra = []
    i = 1
    while i < len(argv):
        if argv[i] == "--out":
            out = argv[i + 1]
            i += 2
        else:
            extra.append(argv[i])
            i += 1
    with open(os.path.join(LANE, "controls", "manifest.json")) as fh:
        manifest = json.load(fh)
    rows = []
    bad = 0
    for item in manifest + [dict(file=os.path.abspath(e), expect="ACCEPT", check=None) for e in extra]:
        path = item["file"] if os.path.isabs(item["file"]) else os.path.join(LANE, "controls", item["file"])
        rc, rep, dt = run(path)
        got_checks = rep.get("failed_checks", rep.get("failed_check"))
        ok = (rep.get("verdict") == item["expect"]) and (
            item["expect"] == "ACCEPT" and rc == 0 or
            item["expect"] == "REJECT" and rc == 1 and got_checks == item["check"])
        bad += 0 if ok else 1
        rows.append(dict(file=item["file"], expect=item["expect"], intended_checks=item["check"], rc=rc,
                         verdict=rep.get("verdict"), failed_checks=got_checks, D=rep.get("D"), P=rep.get("P"),
                         C=rep.get("C"), reason=rep.get("reason"), sha256=rep.get("sha256"),
                         seconds=round(dt, 3), ok=ok))
        flag = "ok " if ok else "BAD"
        print("%s %-55s expect=%-6s got=%-6s check=%s %s" % (flag, item["file"][-55:], item["expect"],
                                                          rep.get("verdict"), got_checks,
                                                          (rep.get("reason") or "")[:70]))
    with open(VERIFY, "rb") as fh:
        vsha = hashlib.sha256(fh.read()).hexdigest()
    receipt = dict(verifier=os.path.relpath(VERIFY, LANE), verifier_sha256=vsha, python=sys.version.split()[0],
                   fixtures=len(rows), mismatches=bad, finished_at=time.strftime("%Y-%m-%d %H:%M:%S %Z"),
                   rows=rows)
    if out:
        with open(out, "w") as fh:
            json.dump(receipt, fh, indent=1)
    print("fixtures=%d mismatches=%d verifier_sha256=%s" % (len(rows), bad, vsha))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
