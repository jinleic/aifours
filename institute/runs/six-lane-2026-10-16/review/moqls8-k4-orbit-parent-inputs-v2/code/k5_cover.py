"""K5 split cover ledger and validator (README §8.2; Codex audit fix 2). Ledger versions are new files
evidence/k5_split_v1/ledger/LEDGER.vNNN.json (exclusive create, each binding the SHA-256 of its predecessor); nothing is
ever rewritten. A ledger lists EVERY leaf ever created (roots, refined leaves and their children) with
id, depth, index, ancestor, complete literal list, state ∈ {UNSTARTED, CERTIFIED, UNKNOWN, REFINED} and evidence
(receipt file relative to evidence/k5_split_v1 + SHA-256 of the exact receipt line).

validate (also run by every other subcommand on its input ledger, and by the runner) rejects unless:
 base CNF SHA-256/header and the declared chain V1..V8 equal the frozen values; ids unique (duplicate JSON keys are
 rejected too); roots are exactly c000..c127 with lits = canonical assignment of V1; every other leaf has a REFINED
 ancestor of depth d−1, id "<ancestor>.L<d>.<bbb>" and lits = ancestor lits + canonical assignment of V_d; every REFINED
 leaf has exactly the 128 children b = 0..127 and no non-REFINED leaf has children; UNSTARTED leaves carry no evidence;
 every other leaf's receipt line exists (by SHA-256) and matches the leaf's identity (id/depth/ancestor/lits, base SHA,
 leaf-CNF SHA recomputed here from the base CNF); CERTIFIED ⇔ strict receipt satisfying the strict conjunction;
 worker-root evidence (old §8 records) is admissible only for UNKNOWN/REFINED roots and only if it is a non-UNSAT
 record. complete ⇔ no problem and every terminal (non-REFINED) leaf is CERTIFIED.
Subcommands: init | ingest --kind strict|worker-root --results F[,F] | refine [--ids ...] | validate
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPLIT_DIR = os.path.normpath(os.path.join(HERE, "..", "evidence", "k5_split_v1"))
LEDGER_DIR = os.path.join(SPLIT_DIR, "ledger")
SCHEMA = "k5-cover-ledger/1"
BASE_SHA = "6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b"
CHAIN = {  # README §8 (V1) and §8.1 (V2..V8), frozen
    1: [57, 106, 155, 204, 253, 302, 351],
    2: [64, 113, 162, 211, 260, 309, 358],
    3: [71, 120, 169, 218, 267, 316, 365],
    4: [78, 127, 176, 225, 274, 323, 372],
    5: [85, 134, 183, 232, 281, 330, 379],
    6: [92, 141, 190, 239, 288, 337, 386],
    7: [1625, 1674, 1723, 1772, 1821, 1870, 1919],
    8: [1632, 1681, 1730, 1779, 1828, 1877, 1926],
}
STATES = ("UNSTARTED", "CERTIFIED", "UNKNOWN", "REFINED")
STRICT_FIELDS = ("solver_returncode", "solver_status_lines", "checker_returncode", "checker_status_lines",
                 "relay_errors", "feed_errors", "rss_guard_tripped", "self_exit")


def canon(V, b):
    return [v if (b >> k) & 1 else -v for k, v in enumerate(V)]


def root_id(b):
    return "c%03d" % b


def child_id(pid, d, b):
    return "%s.L%d.%03d" % (pid, d, b)


def strict_ok(r):
    if any(k not in r for k in STRICT_FIELDS):
        return False
    return (r["self_exit"] is True and r["rss_guard_tripped"] is False and r["solver_returncode"] == 20
            and "s UNSATISFIABLE" in r["solver_status_lines"] and r["checker_returncode"] == 0
            and "s VERIFIED" in r["checker_status_lines"] and "s NOT VERIFIED" not in r["checker_status_lines"]
            and not r["relay_errors"] and not r["feed_errors"])


class Base:
    def __init__(self, path):
        with open(path, "rb") as fh:
            header = fh.readline()
            self.body = fh.read()
        h = hashlib.sha256(header)
        h.update(self.body)
        self.sha = h.hexdigest()
        p = header.decode().split()
        self.nv, self.nc = int(p[2]), int(p[3])
        self._pref = {}

    def leaf_sha(self, lits):
        k = len(lits)
        if k not in self._pref:
            h = hashlib.sha256(("p cnf %d %d\n" % (self.nv, self.nc + k)).encode())
            h.update(self.body)
            self._pref[k] = h
        h = self._pref[k].copy()
        h.update("".join("%d 0\n" % l for l in lits).encode())
        return h.hexdigest()


class Receipts:
    def __init__(self):
        self.cache = {}

    def get(self, rel, line_sha):
        p = os.path.join(SPLIT_DIR, rel)
        if p not in self.cache:
            d = {}
            if os.path.exists(p):
                for line in open(p, "rb").read().split(b"\n"):
                    if line.strip():
                        d.setdefault(hashlib.sha256(line).hexdigest(), line)
            self.cache[p] = d
        line = self.cache[p].get(line_sha)
        return json.loads(line) if line is not None else None


def _nodup(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate JSON key in ledger: %r" % sorted({k for k in keys if keys.count(k) > 1}))
    return dict(pairs)


def load_ledger(path):
    raw = open(path, "rb").read()
    return json.loads(raw, object_pairs_hook=_nodup), hashlib.sha256(raw).hexdigest()


def identity_ok(kind, r, x, base):
    leaf_sha = base.leaf_sha(x["lits"])
    if kind == "strict":
        return (r.get("id") == x["id"] and r.get("depth") == x["depth"] and r.get("ancestor") == x["ancestor"]
                and r.get("index") == x["index"] and r.get("lits") == x["lits"]
                and r.get("base_cnf_sha256") == base.sha and r.get("cnf_sha256") == leaf_sha)
    if kind == "worker-root":
        return (x["depth"] == 1 and r.get("cube") == x["index"] and r.get("lits") == x["lits"]
                and r.get("cnf_sha256") == leaf_sha)
    return False


def validate(L, base, receipts):
    problems = []
    bad = lambda *x: problems.append(list(x))
    if L.get("schema") != SCHEMA:
        bad("schema")
    if base.sha != BASE_SHA or L.get("base_cnf_sha256") != base.sha:
        bad("base sha", base.sha, L.get("base_cnf_sha256"))
    if [L.get("base_vars"), L.get("base_clauses")] != [base.nv, base.nc]:
        bad("base header")
    if {int(k): v for k, v in L.get("chain", {}).items()} != CHAIN:
        bad("chain differs from the frozen V1..V8")
    leaves = L.get("leaves", [])
    byid = {}
    for x in leaves:
        if x["id"] in byid:
            bad("duplicate id", x["id"])
        byid[x["id"]] = x
    kids, roots = {}, []
    for x in leaves:
        d, b = x["depth"], x["index"]
        if not (type(b) is int and 0 <= b < 128 and type(d) is int and d in CHAIN):
            bad("index/depth", x["id"])
            continue
        if d == 1:
            if x["ancestor"] is not None or x["id"] != root_id(b) or x["lits"] != canon(CHAIN[1], b):
                bad("root identity", x["id"])
            roots.append(b)
        else:
            a = byid.get(x["ancestor"])
            if a is None or a["state"] != "REFINED" or a["depth"] != d - 1:
                bad("ancestry", x["id"])
                continue
            if x["id"] != child_id(a["id"], d, b) or x["lits"] != a["lits"] + canon(CHAIN[d], b):
                bad("child identity", x["id"])
            kids.setdefault(a["id"], []).append(b)
    if sorted(roots) != list(range(128)):
        bad("roots are not exactly c000..c127")
    for x in leaves:
        if x["state"] == "REFINED" and sorted(kids.get(x["id"], [])) != list(range(128)):
            bad("REFINED leaf without exactly the 128 children", x["id"])
        if x["state"] != "REFINED" and x["id"] in kids:
            bad("children under a non-REFINED leaf", x["id"])
    for x in leaves:
        st, ev = x["state"], x.get("evidence")
        if st not in STATES:
            bad("state", x["id"])
            continue
        if st == "UNSTARTED":
            if ev is not None:
                bad("UNSTARTED leaf with evidence", x["id"])
            continue
        if not ev:
            bad("missing evidence", x["id"])
            continue
        r = receipts.get(ev["file"], ev["line_sha256"])
        if r is None:
            bad("receipt line not found", x["id"])
            continue
        if not identity_ok(ev["kind"], r, x, base):
            bad("receipt identity mismatch", x["id"], ev["kind"])
        ok = ev["kind"] == "strict" and strict_ok(r)
        if ev["kind"] == "worker-root" and (st == "CERTIFIED" or r.get("solver_status") == "UNSAT"):
            bad("worker-root evidence used beyond a non-UNSAT UNKNOWN root", x["id"])
        if st == "CERTIFIED" and not ok:
            bad("CERTIFIED without a strict receipt", x["id"])
        if st in ("UNKNOWN", "REFINED") and ok:
            bad("strictly certified leaf recorded as " + st, x["id"])
    term = [x for x in leaves if x["state"] != "REFINED"]
    counts = {s: sum(x["state"] == s for x in leaves) for s in STATES}
    by_depth = {}
    for x in term:
        by_depth.setdefault(str(x["depth"]), {}).setdefault(x["state"], 0)
        by_depth[str(x["depth"])][x["state"]] += 1
    return {"problems": problems, "leaves": len(leaves), "terminal": len(term), "counts": counts,
            "terminal_by_depth": by_depth, "complete": (not problems) and all(x["state"] == "CERTIFIED" for x in term)}


def write_next(L, prev_sha, note):
    os.makedirs(LEDGER_DIR, exist_ok=True)
    L = dict(L)
    L["version"] = (L.get("version") or 0) + 1
    L["prev_sha256"] = prev_sha
    L["note"] = note
    L["writer_argv"] = sys.argv
    L["writer_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    path = os.path.join(LEDGER_DIR, "LEDGER.v%03d.json" % L["version"])
    data = json.dumps(L, indent=0).encode()
    with open(path, "xb") as fh:
        fh.write(data)
    return path, hashlib.sha256(data).hexdigest()


def need_valid(L, base, rc):
    v = validate(L, base, rc)
    if v["problems"]:
        raise SystemExit("input ledger invalid: %s" % json.dumps(v["problems"][:20]))
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["init", "ingest", "refine", "validate"])
    ap.add_argument("--base", required=True)
    ap.add_argument("--ledger")
    ap.add_argument("--kind", choices=["strict", "worker-root"])
    ap.add_argument("--results", help="comma-separated receipt files (paths relative to evidence/k5_split_v1)")
    ap.add_argument("--ids", default=None, help="refine: comma-separated UNKNOWN terminal ids (default: all)")
    a = ap.parse_args()
    base = Base(a.base)
    rc = Receipts()
    if a.mode == "init":
        L = {"schema": SCHEMA, "version": 0, "base_cnf_sha256": base.sha, "base_vars": base.nv,
             "base_clauses": base.nc, "chain": {str(k): v for k, v in CHAIN.items()},
             "leaves": [{"id": root_id(b), "depth": 1, "index": b, "ancestor": None, "lits": canon(CHAIN[1], b),
                         "state": "UNSTARTED", "evidence": None} for b in range(128)]}
        v = validate(L, base, rc)
        print(json.dumps(v["problems"][:5]))
        print(json.dumps(write_next(L, None, "init: 128 roots")))
        return
    L, lsha = load_ledger(a.ledger)
    v = need_valid(L, base, rc)
    if a.mode == "validate":
        out = os.path.splitext(a.ledger)[0] + ".validation.%s.json" % hashlib.sha256(
            open(__file__, "rb").read()).hexdigest()[:8]
        v.update({"ledger": a.ledger, "ledger_sha256": lsha, "validator_sha256":
                  hashlib.sha256(open(__file__, "rb").read()).hexdigest()})
        if not os.path.exists(out):
            with open(out, "x") as fh:
                json.dump(v, fh, indent=1)
        print(json.dumps({k: v[k] for k in ("problems", "leaves", "terminal", "counts", "terminal_by_depth",
                                            "complete")}))
        return
    byid = {x["id"]: x for x in L["leaves"]}
    if a.mode == "ingest":
        changed, ignored, seen = 0, [], {}
        for rel in a.results.split(","):
            for line in open(os.path.join(SPLIT_DIR, rel), "rb").read().split(b"\n"):
                if not line.strip():
                    continue
                r = json.loads(line)
                ev = {"kind": a.kind, "file": rel, "line_sha256": hashlib.sha256(line).hexdigest()}
                lid = r["id"] if a.kind == "strict" else root_id(r["cube"])
                x = byid.get(lid)
                if x is None or not identity_ok(a.kind, r, x, base):
                    raise SystemExit("receipt does not match the ledger identity: %s" % lid)
                if lid in seen:
                    raise SystemExit("two receipts for one leaf: %s" % lid)
                seen[lid] = ev
                if a.kind == "worker-root":
                    if r.get("solver_status") == "UNSAT":
                        ignored.append(lid)      # worker positives never certify; strict re-run pending (§8.2)
                        continue
                    if r.get("solver_status") == "SAT":
                        raise SystemExit("SAT root record — stop and report: %s" % lid)
                    new = "UNKNOWN"
                else:
                    new = "CERTIFIED" if strict_ok(r) else "UNKNOWN"
                if x["state"] == "UNSTARTED":
                    x["state"], x["evidence"] = new, ev
                    changed += 1
                elif x.get("evidence") != ev:
                    raise SystemExit("leaf already decided by other evidence: %s" % lid)
        v2 = validate(L, base, rc)
        if v2["problems"]:
            raise SystemExit("ingest would produce an invalid ledger: %s" % json.dumps(v2["problems"][:20]))
        print(json.dumps({"changed": changed, "ignored_worker_positive": len(ignored), "counts": v2["counts"]}))
        print(json.dumps(write_next(L, lsha, "ingest %s %s" % (a.kind, a.results))))
        return
    if a.mode == "refine":
        term_unknown = [x for x in L["leaves"] if x["state"] == "UNKNOWN"]
        sel = term_unknown if a.ids is None else [byid[i] for i in a.ids.split(",")]
        if any(x["state"] != "UNKNOWN" for x in sel):
            raise SystemExit("only UNKNOWN terminal leaves can be refined")
        for x in sel:
            d = x["depth"] + 1
            if d not in CHAIN:
                raise SystemExit("no declared variable list for depth %d" % d)
            x["state"] = "REFINED"
            for b in range(128):
                L["leaves"].append({"id": child_id(x["id"], d, b), "depth": d, "index": b, "ancestor": x["id"],
                                    "lits": x["lits"] + canon(CHAIN[d], b), "state": "UNSTARTED", "evidence": None})
        v2 = validate(L, base, rc)
        if v2["problems"]:
            raise SystemExit("refine would produce an invalid ledger: %s" % json.dumps(v2["problems"][:20]))
        print(json.dumps({"refined": [x["id"] for x in sel], "counts": v2["counts"]}))
        print(json.dumps(write_next(L, lsha, "refine %s" % ",".join(x["id"] for x in sel))))


if __name__ == "__main__":
    main()
