#!/usr/bin/env python3
"""Independent R7 metadata coverage audit; NOT a theorem or proof verifier.

Require identity, CNF-hash and index consistency before counting a worker's
standard-drat-trim receipt. Never count lrat-check-only or lane-written-LRAT
receipts. Snapshot every consumed JSON record in a new compressed JSONL file.
R5/R6/R8 input binding, mathematical review and parent proof replay are separate.
"""
import argparse
import gzip
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

HEX = re.compile(r"[0-9a-f]{64}\Z")
SINGLE = re.compile(r"f(\d+)(?:_exact|_r\d+)?\.json\Z")
BATCH = re.compile(r"batch_(\d+)_(\d+)(?:_r\d+)?\.json\Z")


def stream_receipt(r):
    d = r.get("drat_trim") or {}
    return (r.get("status") == "UNSAT" and r.get("solver_rc") == 20 and
            r.get("solver_stop") == "self" and r.get("checked") is True and
            r.get("drat_trim_verified") is True and r.get("checker_interrupted") is False and
            d.get("stop") == "self" and d.get("rc") == 0 and d.get("says_verified") is True and
            not d.get("says_timeout", False) and
            ("s_lines" not in d or d["s_lines"] == ["s VERIFIED"]) and
            bool(HEX.fullmatch(r.get("cnf_sha256", ""))) and
            bool(HEX.fullmatch(r.get("drat_sha256", ""))) and
            isinstance(r.get("drat_bytes"), int) and r["drat_bytes"] > 0)


def split_indices(name, r, n, m2):
    """Reject filename/record mismatches and out-of-range or missing indices."""
    m = SINGLE.fullmatch(name)
    if m:
        i = int(m[1])
        if r.get("sub_index" if m2 else "full_index") != i or not 0 <= i < n:
            raise ValueError("single-index mismatch or out of range")
        return [i]
    m = BATCH.fullmatch(name)
    if not m:
        raise ValueError("unrecognized split result filename")
    lo, hi = int(m[1]), int(m[2])
    if not 0 <= lo <= hi < n:
        raise ValueError("batch range outside placement list")
    indices = r.get("indices")
    expected = list(range(lo, hi + 1))
    if indices != expected and not (m2 and indices == [lo, hi]):
        raise ValueError("batch indices do not equal filename range")
    return expected


class Records:
    def __init__(self, lane, out):
        self.lane = lane
        self.cache = {}
        self.issues = []
        self.sats = []
        self.manifest = {}
        self.snap = gzip.open(out / "consumed-records.jsonl.gz", "xt", compresslevel=3)

    def load(self, path):
        path = Path(path)
        if path in self.cache:
            return self.cache[path]
        if not path.is_file():
            return None
        data = path.read_bytes()
        rel = str(path.relative_to(self.lane))
        sha = hashlib.sha256(data).hexdigest()
        try:
            r = json.loads(data)
        except (ValueError, UnicodeDecodeError) as e:
            self.issues.append({"path": rel, "reason": "unreadable/in-flight JSON", "detail": str(e)})
            return None
        self.manifest[rel] = sha
        self.snap.write(json.dumps({"path": rel, "sha256": sha, "record": r}, separators=(",", ":")) + "\n")
        self.cache[path] = r
        if isinstance(r, dict) and r.get("status") == "SAT":
            self.sats.append(rel)
        return r

    def issue(self, path, reason):
        self.issues.append({"path": str(path.relative_to(self.lane)), "reason": reason})


def full_split(store, directory, tag, mi, bi=None):
    m2 = bi is not None
    E = store.load(directory / "ext.json")
    if E is None:
        return None
    key, items = ("num_placements", "placements") if m2 else ("num_full", "full")
    n = E.get(key)
    if not isinstance(n, int) or n < 0 or not isinstance(E.get(items), list) or len(E[items]) != n:
        store.issue(directory / "ext.json", "placement count does not match stored list")
        return None
    if m2:
        identity_ok = E.get("index") == bi
    else:
        identity_ok = Path(E.get("source", "")).name == tag + ".json"
    if not identity_ok:
        store.issue(directory / "ext.json", "placement source identity mismatch")
        return None
    covered, used = set(), []
    for f in sorted(directory.glob("*.json")):
        if not (SINGLE.fullmatch(f.name) or BATCH.fullmatch(f.name)):
            continue
        r = store.load(f)
        if not isinstance(r, dict):
            continue
        identity_ok = ((r.get("multiset") == mi and r.get("b_index") == bi) if m2 else r.get("tag") == tag)
        if not identity_ok:
            store.issue(f, "split result case identity mismatch")
            continue
        try:
            indices = split_indices(f.name, r, n, m2)
        except ValueError as e:
            store.issue(f, str(e))
            continue
        if stream_receipt(r):
            covered.update(indices)
            used.append(str(f.relative_to(store.lane)))
    return {"count": n, "covered": len(covered), "open_indices": sorted(set(range(n)) - covered),
            "complete": len(covered) == n, "records": used}


def controls():
    sha = "a" * 64
    good = {"status": "UNSAT", "solver_rc": 20, "solver_stop": "self", "checked": True,
            "drat_trim_verified": True, "checker_interrupted": False, "cnf_sha256": sha,
            "drat_sha256": sha, "drat_bytes": 1,
            "drat_trim": {"stop": "self", "rc": 0, "says_verified": True, "s_lines": ["s VERIFIED"]}}
    cases = {"standard_receipt": stream_receipt(good)}
    for key, value in (("solver_stop", "term"), ("checker_interrupted", True),
                       ("status", "SAT"), ("drat_sha256", "bad")):
        r = dict(good, **{key: value})
        cases["reject_" + key] = not stream_receipt(r)
    r = dict(good, drat_trim={"stop": "self", "rc": 0, "says_verified": True,
                              "s_lines": ["s TIMEOUT", "s VERIFIED"]})
    cases["reject_timeout_even_with_checked_flag"] = not stream_receipt(r)
    try:
        split_indices("batch_00000_00099.json", {"indices": [0, 99]}, 100, False)
        cases["reject_missing_M1_batch_indices"] = False
    except ValueError:
        cases["reject_missing_M1_batch_indices"] = True
    cases["M2_declared_range"] = len(split_indices("batch_00000_00099.json", {"indices": [0, 99]}, 100, True)) == 100
    try:
        split_indices("f00001.json", {"full_index": 0}, 2, False)
        cases["reject_wrong_single_identity"] = False
    except ValueError:
        cases["reject_wrong_single_identity"] = True
    return cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()
    args.output_dir.mkdir(exist_ok=False)
    lane, out = args.lane.resolve(), args.output_dir
    store = Records(lane, out)
    idx = store.load(lane / "cases19skel/index.json")
    maps = {mi: store.load(lane / f"cycle2/skel-b/compare-map-ms{mi:02d}.json") for mi in range(1, 10)}
    rows, per = [], {}
    for c in idx["cases"]:
        tag, mi, si = c["tag"], c["multiset"], c["skel"]
        if tag != f"ms{mi:02d}_s{si:05d}":
            raise ValueError("case index tag mismatch")
        p = store.load(lane / f"cases19skel/results/{tag}.json")
        expected = p.get("cnf_sha256") if p else None
        m1, m2 = [], []
        for sub in ("cases19skel/proofcheck", "cycle2/proofstream", "cycle2/hard5"):
            path = lane / sub / (tag + ".json")
            r = store.load(path)
            if not isinstance(r, dict):
                continue
            if r.get("tag") != tag or r.get("cnf_sha256") != expected:
                store.issue(path, "direct case identity/CNF mismatch")
                continue
            old = (sub == "cases19skel/proofcheck" and r.get("ok") is True and
                   r.get("drat_trim_verified") is True and r.get("kissat_rc") == 20 and
                   p.get("status") == "UNSAT")
            if old or stream_receipt(r):
                m1.append(str(path.relative_to(lane)))
        for sub in ("a3", "part"):
            s = full_split(store, lane / "cycle2" / sub / tag, tag, mi)
            if s and s["complete"]:
                m1.extend(s["records"] or [f"cycle2/{sub}/{tag}/ext.json (empty placement set)"])
        bmap = maps[mi]
        bi = bmap["a_to_b"][si] if bmap and bmap.get("bijection") else None
        if bi is not None:
            btag = f"ms{mi:02d}_b{bi:05d}"
            path = lane / "cycle2/m2skel_drat" / (btag + ".json")
            r = store.load(path)
            if isinstance(r, dict):
                if r.get("multiset") != mi or r.get("b_index") != bi:
                    store.issue(path, "M2 case identity mismatch")
                elif stream_receipt(r):
                    m2.append(str(path.relative_to(lane)))
            s = full_split(store, lane / "cycle2/m2part_drat" / btag, tag, mi, bi)
            if s and s["complete"]:
                m2.extend(s["records"] or [f"cycle2/m2part_drat/{btag}/ext.json (empty placement set)"])
        rows.append({"tag": tag, "M2_b_index": bi, "base_cnf_sha256": expected,
                     "M1_records": m1, "M2_records": m2})
        q = per.setdefault(f"ms{mi:02d}", Counter())
        q.update(cases=1, M1_recorded=int(bool(m1)), M2_recorded=int(bool(m2)), both=int(bool(m1 and m2)))
    # Do not hide a SAT claim in a superseded result path or after finding an UNSAT route.
    roots = [lane / "cases19skel/results", lane / "cases19q0/results", lane / "m2q0b/results", lane / "m2q0c/results"]
    roots += [p for p in (lane / "cycle2").iterdir() if p.is_dir() and
              re.fullmatch(r"(?:hard\d*|a3|part|proofstream|m2skel[^/]*|m2part[^/]*)", p.name)]
    for root in roots:
        for f in sorted(root.rglob("*.json")):
            if f.name != "ext.json":
                store.load(f)
    e0 = []
    graphs = store.load(lane / "cases19q0/index.json")["cases"]
    for g in graphs:
        tag = g["tag"]
        a = store.load(lane / f"cases19q0/results/{tag}.json") or {}
        c = store.load(lane / f"cases19q0/results/{tag}.check.json") or {}
        b = store.load(lane / f"m2q0c/results/{tag}.json") or {}
        ca = a.get("cnf_sha256")
        ok1 = (a.get("status") == "UNSAT" and a.get("graph6") == g["graph6"] and
               c.get("tag") == tag and c.get("cnf_sha256_now") == ca and
               c.get("cnf_sha256_at_solve") == ca and c.get("drat_trim_rc") == 0 and
               c.get("drat_trim_verified") is True and c.get("ok") is True)
        ok2 = stream_receipt(b) and b.get("graph6") == g["graph6"] and b.get("graph_index") == int(tag[1:])
        e0.append({"tag": tag, "M1_recorded": bool(ok1), "M2_recorded": bool(ok2)})
    ctrl = controls()
    store.snap.close()
    result = {"recorded_at_pt": subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip(),
              "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "R7 worker-receipt metadata coverage ONLY; R5/R6/R8, reviews and parent proof replay remain separate",
              "cases": rows, "per_multiset": per, "balanced_graphs": e0,
              "M1_open_tags": [r["tag"] for r in rows if not r["M1_records"]],
              "M2_open_tags": [r["tag"] for r in rows if not r["M2_records"]],
              "SAT_claims": sorted(set(store.sats)), "issues": store.issues,
              "record_manifest": store.manifest, "controls": ctrl,
              "verdict": "METADATA-AUDIT-COMPLETE" if all(ctrl.values()) else "CONTROL-FAIL"}
    with (out / "aggregate.json").open("x") as f:
        json.dump(result, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": result["verdict"], "M1_open": len(result["M1_open_tags"]),
                      "M2_open": len(result["M2_open_tags"]), "SAT_claims": len(result["SAT_claims"]),
                      "issues": len(result["issues"])}))
    return 0 if all(ctrl.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
