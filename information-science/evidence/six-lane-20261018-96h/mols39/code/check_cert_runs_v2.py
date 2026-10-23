#!/usr/bin/env python3
"""check_cert_runs_v2.py (ContinueCFR21, mols39 lane; written 2026-10-19; NOT executed when frozen; stdlib; reads only
except one exclusive-created output file).
Compares the outputs of a finished Lemma U certificate wave with the expectations preregistered in the pinned run plan
(evidence/lemmaU-cert-run-plan-v1.json). For each job it reads <base>/<item>/stdout.txt (exactly one JSON line) and,
for checker jobs, the checker's --out file, which must equal the stdout object. Receipts and settlement are audited
separately (supervisor and parent); this script only judges the scientific outputs.
Exit 0 iff every evaluated job is AS_EXPECTED; 1 if any deviates or is missing; 2 for a pin mismatch or bad arguments.
v2 (supersedes v1 7ce2b4e0ef402623ffcc12f8505dc87f03e5971a32203ee35b347a6bb3093522, never executed): optional 5th argument UPTO_ITEM evaluates the jobs in plan order up to and
including that item only, so the wave can be stopped after any job whose output deviates.
Args: plan_json plan_sha256 base_dir out_json(new) [upto_item]"""
import sys, os, json, hashlib


def one_line(path):
    try:
        lines = [ln for ln in open(path).read().splitlines() if ln.strip()]
    except OSError:
        return None
    if len(lines) != 1:
        return None
    try:
        return json.loads(lines[0])
    except ValueError:
        return None


def main(argv):
    if len(argv) not in (4, 5):
        print(json.dumps({"status": "BAD_INPUT", "reason": "usage: plan plan_sha base out [upto_item]"}))
        return 2
    plan_p, plan_sha, base, outp = argv[:4]
    upto = argv[4] if len(argv) == 5 else None
    pb = open(plan_p, "rb").read()
    if hashlib.sha256(pb).hexdigest() != plan_sha:
        print(json.dumps({"status": "INPUT_PIN_MISMATCH", "reason": "plan sha256"}))
        return 2
    if os.path.exists(outp):
        print(json.dumps({"status": "BAD_INPUT", "reason": "output exists"}))
        return 2
    plan = json.loads(pb)
    if upto is not None and upto not in [j["item"] for j in plan["jobs"]]:
        print(json.dumps({"status": "BAD_INPUT", "reason": "unknown upto item"}))
        return 2
    outs, manifest, results = {}, None, []
    for job in plan["jobs"]:
        item, kind, exp = job["item"], job["kind"], job["expect"]
        if kind == "expectations":
            continue
        d = os.path.join(base, item)
        o = one_line(os.path.join(d, "stdout.txt"))
        rec = {"item": item, "kind": kind, "problems": []}
        if o is None:
            rec["problems"].append("stdout.txt missing or not exactly one JSON line")
        else:
            outs[item] = o
            if kind == "producer":
                for key, val in exp.items():
                    if o.get(key) != val:
                        rec["problems"].append("%s = %r, expected %r" % (key, o.get(key), val))
            elif kind == "generator":
                if o.get("status") != "OK":
                    rec["problems"].append("generator status %r" % (o.get("status"),))
                mp = exp["manifest_path"]
                try:
                    manifest = json.load(open(mp))
                except (OSError, ValueError):
                    manifest = None
                    rec["problems"].append("manifest unreadable")
                if manifest is not None:
                    src = outs.get(exp["source_from"], {}).get("cert_sha256")
                    if manifest.get("source_cert_sha256") != src:
                        rec["problems"].append("manifest source sha %r != producer cert sha %r" % (manifest.get("source_cert_sha256"), src))
                    names = [m["item"] for m in manifest.get("mutants", [])]
                    if names != exp["mutants"]:
                        rec["problems"].append("mutant list %r" % (names,))
                    for m in manifest.get("mutants", []):
                        if not os.path.exists(m["path"]) or hashlib.sha256(open(m["path"], "rb").read()).hexdigest() != m["sha256"]:
                            rec["problems"].append("mutant file %s missing or hash differs" % m["item"])
                        if m["item"] == "nc0_identity" and m["sha256"] != src:
                            rec["problems"].append("nc0 bytes differ from the source certificate")
            elif kind == "checker":
                f = one_line(exp["out_path"])
                if f != o:
                    rec["problems"].append("checker --out file differs from stdout line")
                for key, val in exp["fields"].items():
                    if o.get(key) != val:
                        rec["problems"].append("%s = %r, expected %r" % (key, o.get(key), val))
                src = exp["cert_sha256_from"]
                if src.startswith("producer:"):
                    want = outs.get(src.split(":", 1)[1], {}).get("cert_sha256")
                else:
                    want = None
                    if manifest is not None:
                        for m in manifest.get("mutants", []):
                            if m["item"] == src.split(":", 1)[1]:
                                want = m["sha256"]
                if want is None or o.get("cert_sha256") != want:
                    rec["problems"].append("cert_sha256 %r, expected %r" % (o.get("cert_sha256"), want))
            else:
                rec["problems"].append("unknown kind")
        rec["verdict"] = "AS_EXPECTED" if not rec["problems"] else "DEVIATION"
        results.append(rec)
        if upto is not None and item == upto:
            break
    allok = all(r["verdict"] == "AS_EXPECTED" for r in results)
    claim = None
    ca = outs.get(plan["claim_item"])
    if ca is not None:
        pred = plan["claim_predicate_fields"]
        claim = all(ca.get(key) == val for key, val in pred.items())
    summary = {"status": "OK", "plan_sha256": plan_sha, "upto": upto, "evaluated": [r["item"] for r in results],
               "all_as_expected": allok, "claim_predicate_holds": claim,
               "certificate_route_qualified": allok and upto is None, "results": results}
    with open(outp, "x") as fh:
        fh.write(json.dumps(summary, indent=1, sort_keys=True) + "\n")
    print(json.dumps({"status": "OK", "all_as_expected": allok, "claim_predicate_holds": claim,
                      "deviations": [r["item"] for r in results if r["verdict"] != "AS_EXPECTED"]}, sort_keys=True))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
