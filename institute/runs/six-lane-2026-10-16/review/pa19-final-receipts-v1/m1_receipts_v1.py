#!/usr/bin/env python3
"""PA19FinalReceiptAudit: independent M1 receipt-coverage reader v1 (stdlib only, metadata only).

Scope: derive PA(19,8,6) FIRST-METHOD (M1) coverage of the 5577 A2 skeleton cases and the 486 E0 balanced graphs
directly from the lane's underlying per-record receipts. It does NOT import or trust the producer aggregators
(aggregate15/summarize15/STATUS15) and does NOT run any solver, checker, generator or encoder. Parent receipts are
used only as hash references (expected base-CNF SHA-256 per tag, regenerated placement-list SHA-256, sampled
formula-bound record SHA-256). No proof is read; a COVERED verdict here is a receipt/binding statement, never a
native proof replay.

Fail-closed rules: a record qualifies only if every path-specific necessary field is present with the exact value
(type-checked); missing fields are never read as PASS. Retired revision 10, revision 8, lratstrict and LRAT-only
records, proof-free, stopped/UNKNOWN and SAT records never qualify. A split case is covered only if the exact set
union of qualifying records' indices equals range(num_full); one missing index leaves the whole case UNKNOWN. Any
SAT claim on a case path makes that case SAT-CLAIM (never covered).

Usage: m1_receipts_v1.py OUTDIR   (OUTDIR must not exist; created exclusively; files written with mode 'x')
"""
import gzip
import hashlib
import json
import os
import re
import resource
import sys
import time

LANE_ROOT = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review"
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
COUNTS = {1: 3215, 2: 59, 3: 674, 4: 39, 5: 73, 6: 482, 7: 482, 8: 482, 9: 71}

# Parent reference receipts (hash-pinned; values recorded by the parent's own later receipts).
PARENT_PINS = {
    "R0_pin_result": ("pa19-parent-cover-replay-v1/pin-result.json",
                      "429c56278554dfe6c5b6e1b8c721e99c2b1bb336decc56568a6e1f867ea8b7f0"),
    "R2R4_cover_binding": ("pa19-parent-cover-replay-v1/cover-binding-result.json",
                           "f0b1e2823424ab2c73491036b0fccf75a6736b6bdcae91ae3b2c91dfdaed4516"),
    "R5_cnf_binding": ("pa19-cnf-binding-v1/cnf-binding-result.json",
                       "2a14a1dc4eadec733f73ff460814f94ebffa11b81266eb2eaf8c7df7772a22d9"),
    "R6_placement_binding": ("pa19-placement-binding-v1/placement-binding-result.json",
                             "6cd7f1881eec464aa5dda45ea9a3bf86f5f5083c461cc5186b89c3f896921cb5"),
    "R8_subcase_binding": ("pa19-subcase-binding-v1/subcase-binding-result.json",
                           "594e1998839c47af7786dc944ff98415dad325e531fe04f925f45a7b59552377"),
    "R8_inc001": ("pa19-subcase-binding-v1/incremental/inc-001/inc-result.json",
                  "6f510d81a8b2f500a8b87465d0e5ddc04c6f48e90cb5359214ead1f195726483"),
    "R8_inc001_late_census": ("pa19-subcase-binding-v1/incremental/inc-001/late-census.jsonl",
                              "be6a2cbdbf139cc296b9cd369dd1faef72960acd2caeaf93100f151eb3447c40"),
    "ms06_s00150_binding_v2": ("pa19-ms06-placement-binding-v2/result.json",
                               "cc748b23d01011e707a37c838be1187f76a19ce37ddaed62fedc23f32db15040"),
    "R3_generator_semantic": ("pa19-parent-cover-replay-v1/generator-semantic-check-v1.json",
                              "939d1ea79a4a556920097b38497b22718855ffbcc4e5ef7a0d821c05026e3514"),
    "R7_strict_aggregate_v2": ("pa19-strict-aggregate-v2/aggregate.json",
                               "371fb2fdb2dc72784b078978989fcddb30ef2a31708788f60c43210f5b9929eb"),
    "R8_population": ("pa19-subcase-binding-v1/population.jsonl",
                      "e1b4835a98837273c586a92a68a1a9e520dce17110f755a3a55f24aed1e3c73c"),
}
CONTRACT = ("cycle2/s00468-six-unit-contract.json", {
    "target": "ms06_s00468", "base_cnf": "cases19skel/cnf/ms06_s00468.cnf",
    "base_cnf_sha256": "137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994",
    "row_zero_based": 8, "column_zero_based": 6, "unit_literals_by_symbol": [421, 422, 423, 424, 425, 426],
    "symbols": [0, 1, 2, 3, 4, 5]})
CAND = ("cycle2/m1-complete-candidate-20261018T012523.json",
        "cf3e87c5fd8201286aa7a2b1e09999733cab7e5018a7e49c738f91ff13d1d791")
STATUS15 = ("STATUS15.json", "b0dac6b0c7c91244994954bde5a81a39823fea9b69b746a54ddbc47ca32145f3")
LANE_PINS = {  # parent-pinned lane inputs
    "cases19skel/index.json": "977b6afa42e1358914b81c007102c1adbeccd71820d54e729a52dbc85615e947",
    "cases19q0/index.json": "436139a7438377c7a190bf06ec36988e5ee42fce59d2de314a98fd4fad96b1a2",
}
S00468 = {"tag": "ms06_s00468", "row": 8, "column": 6,
          "base_sha": "137407b6532fea61a682467507462e146cef6dd546b9a496a6bd18ad0ceba994"}

# Accepted record revisions -> evidence tier (lower is stronger). Anything else never qualifies.
REV_TIER = {11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 9: 2, 5: 3, 4: 4}
TIER_NAME = {1: "T1-staged-strict(rev11-15)", 2: "T2-exact-sline-streamed(rev9)",
             3: "T3-substring+timeoutflag-streamed(rev5)", 4: "T4-substring-streamed(rev4)",
             5: "T5-old-cycle1-stored-proof(rc-unrecorded)", 6: "T5E-old-cycle1-E0-stored-proof(rc+tail)"}
RETIRED = {10: "retired revision 10 (archive/rev10-superseded)", 8: "revision 8 verdict-parser bug (retired)",
           6: "revision 6 lratstrict pipeline (never counted)"}
PROOFCHECK_KEYS = {"check_seconds", "cnf", "cnf_matches_pass1", "cnf_sha256", "drat_bytes", "drat_sha256",
                   "drat_trim_tail", "drat_trim_verified", "kissat_rc", "lrat_check_rc", "lrat_verified", "ok",
                   "pass1_status", "solve_seconds", "tag"}
E0_RES_KEYS = {"clauses", "cnf", "cnf_sha256", "graph6", "mclass", "multiset", "proof", "proof_bytes",
               "returncode", "seconds", "solver", "status", "tag", "vars"}
E0_CHK_KEYS = {"cnf_sha256_at_solve", "cnf_sha256_now", "drat_trim_rc", "drat_trim_seconds", "drat_trim_tail",
               "drat_trim_verified", "lrat_bytes", "lrat_check_rc", "lrat_check_seconds", "lrat_check_tail",
               "lrat_sha256", "lrat_verified", "ok", "proof_bytes", "proof_sha256", "tag"}
BAD_TAIL = ("s NOT VERIFIED", "s TIMEOUT")
KIND_RANK = {"single": 0, "batch": 1, "r3": 2, "batch_r3": 2, "exact": 3}


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


class Lane:
    """Read-only view of a lane root, with an optional in-memory overlay (rel -> bytes, or None = absent)."""

    def __init__(self, root, overlay=None):
        self.root, self.ov = root, dict(overlay or {})

    def read(self, rel):
        if rel in self.ov:
            return self.ov[rel]
        try:
            with open(os.path.join(self.root, rel), "rb") as f:
                return f.read()
        except (FileNotFoundError, IsADirectoryError, NotADirectoryError):
            return None

    def listdir(self, rel):
        try:
            names = set(os.listdir(os.path.join(self.root, rel)))
        except (FileNotFoundError, NotADirectoryError):
            names = set()
        pre = rel.rstrip("/") + "/"
        for k, v in self.ov.items():
            if k.startswith(pre) and "/" not in k[len(pre):]:
                (names.discard if v is None else names.add)(k[len(pre):])
        return sorted(names)

    def isdir(self, rel):
        return os.path.isdir(os.path.join(self.root, rel)) or any(
            k.startswith(rel.rstrip("/") + "/") and v is not None for k, v in self.ov.items())

    def stat(self, rel):
        if rel in self.ov:
            v = self.ov[rel]
            return None if v is None else (len(v), -1)
        try:
            st = os.stat(os.path.join(self.root, rel))
            return (st.st_size, st.st_mtime_ns)
        except FileNotFoundError:
            return None


class Store:
    """Loads JSON records, recording SHA-256/size/mtime of the exact bytes parsed, and compares each record's bytes
    with parent-recorded snapshot hashes (R7 strict-aggregate-v2 record_manifest, R8 population) when present."""

    def __init__(self, lane, snap=None):
        self.lane, self.manifest, self.sats, self.unreadable = lane, {}, [], []
        self.snap = snap or {}
        self.changed_vs_parent, self.equal_vs_parent = {}, set()

    def load(self, rel):
        b = self.lane.read(rel)
        if b is None:
            return None
        st = self.lane.stat(rel)
        sha = sha256_bytes(b)
        self.manifest[rel] = {"sha256": sha, "size": len(b), "mtime_ns": st[1] if st else None}
        ref = self.snap.get(rel)
        if ref is not None:
            if ref[0] != sha:
                self.changed_vs_parent[rel] = {"now": sha, "parent": ref[0], "snapshot": ref[1]}
            else:
                self.equal_vs_parent.add(rel)
        try:
            r = json.loads(b)
        except (ValueError, UnicodeDecodeError) as e:
            if rel not in {u["path"] for u in self.unreadable}:
                self.unreadable.append({"path": rel, "error": repr(e)[:160]})
            return {"__unreadable__": True}
        if sat_claim(r):
            self.sats.append(rel)
        return r

    def sha(self, rel):
        m = self.manifest.get(rel)
        return m["sha256"] if m else None

    def drift_reason(self, rel):
        c = self.changed_vs_parent.get(rel)
        return None if c is None else "record bytes changed since parent snapshot %s" % c["snapshot"]

    def parent_hash(self, rel):
        return self.snap[rel][1] if rel in self.equal_vs_parent else None


def sat_claim(r, depth=0):
    if depth > 4:
        return False
    if isinstance(r, dict):
        if r.get("status") == "SAT" or r.get("pass1_status") == "SAT":
            return True
        return any(sat_claim(v, depth + 1) for v in r.values() if isinstance(v, (dict, list)))
    if isinstance(r, list):
        return any(sat_claim(v, depth + 1) for v in r[:2000] if isinstance(v, (dict, list)))
    return False


def is_hex(v):
    return isinstance(v, str) and bool(HEX64.fullmatch(v))


def pos_int(v):
    return type(v) is int and v > 0


def solver_family(r):
    s = r.get("solver")
    if not isinstance(s, str):
        return None
    return "kissat" if "kissat" in s else ("cadical" if "cadical" in s else "other")


def checker_rejected(r):
    """Label when drat-trim exited on its own for an UNSAT solve without accepting the proof (surfaced separately,
    never counted): 'nonzero-rc', 'NOT-VERIFIED-line', or 'no-verdict-rc0' (e.g. s TIMEOUT). None otherwise."""
    if not isinstance(r, dict) or r.get("status") != "UNSAT":
        return None
    d = r.get("drat_trim")
    if not isinstance(d, dict) or d.get("stop") != "self":
        return None
    sl = d.get("s_lines") or []
    if any("NOT VERIFIED" in s for s in sl):
        return "NOT-VERIFIED-line"
    if d.get("rc") not in (0, None):
        return "nonzero-rc(%r)" % d.get("rc")
    if d.get("says_verified") is not True:
        return "no-verdict-rc0"
    return None


def lacking(r):
    """Acceptance-relevant fields ABSENT from a record (presence only; for the bridge census)."""
    if not isinstance(r, dict):
        return ["<no record>"]
    d = r.get("drat_trim") if isinstance(r.get("drat_trim"), dict) else None
    out = [k for k in ("solver_stop", "solver_rc") if k not in r]
    if d is None:
        out += ["drat_trim.stop(self-exit)", "drat_trim.rc", "drat_trim.s_lines"]
    else:
        out += [n for k, n in (("stop", "drat_trim.stop(self-exit)"), ("rc", "drat_trim.rc"),
                               ("s_lines", "drat_trim.s_lines")) if k not in d]
    out += [n for k, n in (("replay", "replay(feed-completion)"), ("reader_ok", "reader_ok(compressed-buffer)"))
            if k not in r]
    return out


def stream_predicate(r):
    """Necessary fields for drat-trim stream_check receipts. Returns (reasons, tier)."""
    if not isinstance(r, dict) or r.get("__unreadable__"):
        return ["unreadable record"], None
    rev = r.get("stream_check_revision")
    if type(rev) is not int:
        return ["no integer stream_check_revision"], None
    if rev in RETIRED:
        return [RETIRED[rev]], None
    if rev not in REV_TIER:
        return ["revision %r is not an accepted schema" % rev], None
    tier, why = REV_TIER[rev], []
    s = r.get("solver")
    if not isinstance(s, str):
        why.append("solver string missing")
    else:
        if "lrat-check" in s or "--lrat=true" in s:
            why.append("LRAT-only route (CaDiCaL LRAT + lrat-check), never counted")
        if "drat-trim" not in s:
            why.append("solver string names no drat-trim route")
    if "lratstrict_verified" in r or "lratstrict" in r:
        why.append("lratstrict record, never counted")
    if r.get("status") != "UNSAT":
        why.append("status %r != UNSAT" % r.get("status"))
    if type(r.get("solver_rc")) is not int or r.get("solver_rc") != 20:
        why.append("solver_rc %r != 20" % r.get("solver_rc"))
    if r.get("solver_stop") != "self":
        why.append("solver_stop %r != self" % r.get("solver_stop"))
    if r.get("checked") is not True:
        why.append("checked is not True")
    if r.get("drat_trim_verified") is not True:
        why.append("drat_trim_verified is not True")
    if r.get("checker_interrupted") is not False:
        why.append("checker_interrupted is not False")
    if r.get("events") != []:
        why.append("events not an empty list")
    if "proof_cap_hit" in r:
        why.append("proof_cap_hit present")
    if "admission_denied" in r:
        why.append("admission_denied present")
    if not is_hex(r.get("cnf_sha256")):
        why.append("cnf_sha256 not 64-hex")
    if not pos_int(r.get("cnf_bytes")):
        why.append("cnf_bytes not positive int")
    if not is_hex(r.get("drat_sha256")):
        why.append("drat_sha256 not 64-hex (proof-free)")
    if not pos_int(r.get("drat_bytes")):
        why.append("drat_bytes not positive int (proof-free)")
    d = r.get("drat_trim")
    if not isinstance(d, dict):
        why.append("drat_trim block missing")
    else:
        if d.get("stop") != "self":
            why.append("drat_trim.stop %r != self" % d.get("stop"))
        if type(d.get("rc")) is not int or d.get("rc") != 0:
            why.append("drat_trim.rc %r != 0" % d.get("rc"))
        if d.get("says_verified") is not True:
            why.append("drat_trim.says_verified is not True")
        if "says_timeout" in d and d["says_timeout"] is not False:
            why.append("drat_trim.says_timeout is not False")
        if rev == 5 and "says_timeout" not in d:
            why.append("rev5 drat_trim.says_timeout missing")
        if rev >= 9 or "s_lines" in d:
            sl = d.get("s_lines")
            if not (isinstance(sl, list) and len(sl) == 1 and type(sl[0]) is str and sl[0] == "s VERIFIED"):
                why.append("drat_trim.s_lines %r != ['s VERIFIED'] (exact, CR-stripped only)" % (sl,))
    if rev >= 11:
        if r.get("staged") is not True:
            why.append("staged is not True")
        if r.get("reader_ok") is not True:
            why.append("reader_ok is not True")
        if r.get("replay_ok") is not True:
            why.append("replay_ok is not True")
        if r.get("replay_sha256_matches") is not True:
            why.append("replay_sha256_matches is not True")
        if r.get("aborted_by_sigterm") is not False:
            why.append("aborted_by_sigterm is not False")
        if not pos_int(r.get("zbuf_bytes")):
            why.append("zbuf_bytes not positive int (compressed buffer)")
        if r.get("drat_trim_binary") != "tools/drat-trim/drat-trim":
            why.append("drat_trim_binary not the lane drat-trim")
        rp = r.get("replay")
        if not isinstance(rp, dict):
            why.append("replay block missing")
        else:
            if rp.get("ok") is not True:
                why.append("replay.ok is not True")
            if rp.get("error") is not None:
                why.append("replay.error present")
            if type(rp.get("bytes")) is not int or rp.get("bytes") != r.get("drat_bytes"):
                why.append("replay.bytes != drat_bytes (feed incomplete)")
            if rp.get("sha256") != r.get("drat_sha256"):
                why.append("replay.sha256 != drat_sha256 (feed hash mismatch)")
    return why, tier


def eval_direct(store, rel, tag, base, route):
    r = store.load(rel)
    if r is None:
        return None
    why, tier = stream_predicate(r)
    if store.drift_reason(rel):
        why.append(store.drift_reason(rel))
    if r.get("tag") != tag:
        why.append("tag %r != %s" % (r.get("tag"), tag))
    if r.get("cnf_sha256") != base["sha"]:
        why.append("cnf_sha256 != parent R5 rebuild")
    if r.get("cnf_bytes") != base["bytes"]:
        why.append("cnf_bytes != parent R5 rebuild")
    if r.get("cnf_matches_pass1_sha") is not True:
        why.append("cnf_matches_pass1_sha is not True")
    if route == "b":
        if r.get("cnf_file") != "cases19skel/cnf/%s.cnf" % tag:
            why.append("cnf_file is not the tag's stored CNF")
        if r.get("ok") is not True:
            why.append("ok is not True")
    if route == "c5":
        if r.get("encoder") != "encode_skel.py":
            why.append("encoder %r != encode_skel.py" % r.get("encoder"))
        if r.get("mode") not in ("directk", "directk-staged"):
            why.append("mode %r not a direct kissat mode" % r.get("mode"))
    return {"route": route, "path": rel, "sha256": store.sha(rel), "ok": not why, "reasons": why,
            "tier": tier if not why else None, "rev": r.get("stream_check_revision") if isinstance(r, dict) else None,
            "solver": solver_family(r) if isinstance(r, dict) else None, "sat": sat_claim(r),
            "parent_snapshot_hash_equal": store.parent_hash(rel), "checker_rejection": checker_rejected(r),
            "lacking": lacking(r)}


def eval_proofcheck(store, lane, rel, tag, base, p1):
    r = store.load(rel)
    if r is None:
        return None
    why = [store.drift_reason(rel)] if store.drift_reason(rel) else []
    if not isinstance(r, dict) or r.get("__unreadable__"):
        why.append("unreadable record")
        r = {}
    keys = set(r)
    if keys != PROOFCHECK_KEYS:
        why.append("old proofcheck schema deviation: missing %s extra %s" % (sorted(PROOFCHECK_KEYS - keys),
                                                                             sorted(keys - PROOFCHECK_KEYS)))
    if r.get("tag") != tag:
        why.append("tag mismatch")
    if r.get("pass1_status") != "UNSAT" or not (isinstance(p1, dict) and p1.get("status") == "UNSAT"
                                                 and p1.get("returncode") == 20):
        why.append("pass-1 not UNSAT/rc20")
    if r.get("cnf") != "cases19skel/cnf/%s.cnf" % tag:
        why.append("cnf path is not the tag's stored CNF")
    if r.get("cnf_sha256") != base["sha"]:
        why.append("cnf_sha256 != parent R5 rebuild")
    if r.get("cnf_matches_pass1") is not True:
        why.append("cnf_matches_pass1 is not True")
    if type(r.get("kissat_rc")) is not int or r.get("kissat_rc") != 20:
        why.append("kissat_rc != 20")
    if r.get("drat_trim_verified") is not True:
        why.append("drat_trim_verified is not True")
    if r.get("ok") is not True:
        why.append("ok is not True")
    if not is_hex(r.get("drat_sha256")) or not pos_int(r.get("drat_bytes")):
        why.append("proof hash/bytes missing (proof-free)")
    tail = r.get("drat_trim_tail")
    if not (isinstance(tail, list) and tail and all(type(x) is str for x in tail)):
        why.append("drat_trim_tail missing")
    else:
        if not tail[-1].startswith("c verification time:"):
            why.append("drat_trim_tail lacks final verification-time line")
        if any(x.strip("\r") in BAD_TAIL for x in tail):
            why.append("drat_trim_tail contradicts (NOT VERIFIED/TIMEOUT)")
    st = lane.stat("cases19skel/proof/%s.drat" % tag)
    stored = {"path": "cases19skel/proof/%s.drat" % tag, "exists": st is not None,
              "size_equals_drat_bytes": bool(st and st[0] == r.get("drat_bytes"))}
    return {"route": "a", "path": rel, "sha256": store.sha(rel), "ok": not why, "reasons": why,
            "tier": 5 if not why else None, "rev": None, "solver": "kissat", "sat": sat_claim(r),
            "stored_proof": stored, "parent_snapshot_hash_equal": store.parent_hash(rel), "lacking": lacking(r)}


NAME_RES = [
    ("single", re.compile(r"f(\d{5,})\.json\Z")),
    ("exact", re.compile(r"f(\d{5,})_exact\.json\Z")),
    ("r2", re.compile(r"f(\d{5,})_r2\.json\Z")),
    ("r3", re.compile(r"f(\d{5,})_r3\.json\Z")),
    ("batch", re.compile(r"batch_(\d{5,})_(\d{5,})\.json\Z")),
    ("batch_r2", re.compile(r"batch_(\d{5,})_(\d{5,})_r2\.json\Z")),
    ("batch_r3", re.compile(r"batch_(\d{5,})_(\d{5,})_r3\.json\Z")),
]
NON_RECORD = re.compile(r"(ext\.json|summary\.json|summary_batched\.json|extend-receipt-\d{8}T\d{6}\.json|"
                        r"extend-failed-\d{8}T\d{6}\.json)\Z")
EXPECT_ENC = {("a3", "single"): "encode_full.py", ("a3", "exact"): "encode_full2.py", ("a3", "r3"): "encode_full.py",
              ("part", "single"): "encode_partq.py", ("part", "r3"): "encode_partq.py",
              ("part", "batch"): "encode_partbatch.py", ("part", "batch_r3"): "encode_partbatch.py"}
SINGLE_FIELD = {("a3", "single"): "full_index", ("a3", "exact"): "full_index", ("part", "single"): "sub_index",
                ("a3", "r3"): "index", ("part", "r3"): "index", ("a3", "r2"): "index", ("part", "r2"): "index"}
R3_KIND = {"a3": "a3", "part": "part"}


def classify(name):
    for kind, rx in NAME_RES:
        m = rx.fullmatch(name)
        if m:
            nums = [int(x) for x in m.groups()]
            canon = {"single": "f%05d.json", "exact": "f%05d_exact.json", "r2": "f%05d_r2.json",
                     "r3": "f%05d_r3.json", "batch": "batch_%05d_%05d.json", "batch_r2": "batch_%05d_%05d_r2.json",
                     "batch_r3": "batch_%05d_%05d_r3.json"}[kind] % tuple(nums)
            return kind, nums, canon == name
    return None, None, False


def ranges(sorted_idx):
    out, start, prev = [], None, None
    for i in sorted_idx:
        if start is None:
            start = prev = i
        elif i == prev + 1:
            prev = i
        else:
            out.append([start, prev])
            start = prev = i
    if start is not None:
        out.append([start, prev])
    return out


def eval_split(store, lane, fam, tag, refs):
    d = "cycle2/%s/%s" % (fam, tag)
    if not lane.isdir(d):
        return None
    names = lane.listdir(d)
    out = {"route": "d" if fam == "a3" else "e", "dir": d, "ok": False, "reasons": [], "tier": None, "sat": False}
    E = store.load(d + "/ext.json")
    ext = {"path": d + "/ext.json", "sha256": store.sha(d + "/ext.json")}
    out["ext"] = ext
    others = [n for n in names if n != "ext.json" and n.endswith(".json") and NON_RECORD.fullmatch(n)]
    for n in others:  # never trusted; SAT-scanned only
        rr = store.load(d + "/" + n)
        if sat_claim(rr):
            out["sat"] = True
            out["reasons"].append("SAT claim in %s" % n)
    if not isinstance(E, dict) or E.get("__unreadable__"):
        out["reasons"].append("ext.json missing/unreadable")
        out["unrecognized"] = [n for n in names if not NON_RECORD.fullmatch(n) and classify(n)[0] is None]
        return out
    n, full = E.get("num_full"), E.get("full")
    if type(n) is not int or n < 0 or not isinstance(full, list) or len(full) != n:
        out["reasons"].append("ext.json num_full does not equal stored list length")
        return out
    if E.get("source") != tag + ".json":
        out["reasons"].append("ext.json source identity mismatch")
        return out
    ext.update({"num_full": n, "raw": E.get("raw"), "parent_snapshot_hash_equal": store.parent_hash(d + "/ext.json")})
    del full, E
    if store.drift_reason(d + "/ext.json"):
        out["reasons"].append("ext.json " + store.drift_reason(d + "/ext.json"))
        return out
    ref = refs.get((fam, tag))
    if ref is None:
        ext["binding"] = "worker-only (no parent placement replay)"
    elif ref["sha256"] == ext["sha256"]:
        ext["binding"] = ref["label"]
    else:
        ext["binding"] = "MISMATCH vs %s" % ref["label"]
        out["reasons"].append("ext.json sha256 != parent placement reference (%s)" % ref["label"])
        return out
    recs, rejected, unrecognized, alarms, out_of_range = [], {}, [], [], []
    sat_idx = set()
    for name in names:
        if NON_RECORD.fullmatch(name):
            continue
        kind, nums, canon = classify(name)
        rel = d + "/" + name
        if kind is None:
            unrecognized.append(name)
            rr = store.load(rel) if name.endswith(".json") else None
            if rr is not None and sat_claim(rr):
                out["sat"] = True
                out["reasons"].append("SAT claim in unrecognized file %s" % name)
            continue
        r = store.load(rel)
        why = [store.drift_reason(rel)] if store.drift_reason(rel) else []
        if not canon:
            why.append("non-canonical filename")
        if kind in ("batch", "batch_r2", "batch_r3"):
            lo, hi = nums
            idx = list(range(lo, hi + 1)) if 0 <= lo <= hi < n else None
            if idx is None:
                why.append("batch range outside placement list")
                out_of_range.append(name)
        else:
            lo = hi = nums[0]
            idx = [lo] if 0 <= lo < n else None
            if idx is None:
                why.append("single index outside placement list")
                out_of_range.append(name)
        if isinstance(r, dict) and sat_claim(r):
            out["sat"] = True
            if idx:
                sat_idx.update(idx)
            why.append("SAT claim")
        if kind in ("r2", "batch_r2"):
            why.append("_r2 rerun = CaDiCaL LRAT + lrat-check (LRAT-only), never counted")
        if not isinstance(r, dict) or r.get("__unreadable__"):
            why.append("unreadable record")
            r = {}
        sw, tier = stream_predicate(r)
        why += sw
        if r.get("tag") != tag:
            why.append("tag %r != directory %s" % (r.get("tag"), tag))
        exp_enc = EXPECT_ENC.get((fam, kind))
        if kind not in ("r2", "batch_r2") and r.get("encoder") != exp_enc:
            why.append("encoder %r != %r" % (r.get("encoder"), exp_enc))
        if kind in ("single", "exact", "r2", "r3"):
            fields = [k for k in ("full_index", "sub_index", "index") if k in r]
            need = SINGLE_FIELD.get((fam, kind))
            if need not in r:
                why.append("required index field %r missing" % need)
            if any(type(r[k]) is not int or r[k] != lo for k in fields):
                why.append("record index field(s) != filename index")
            if "indices" in r and r["indices"] is not None:
                why.append("single record carries an indices list")
        else:
            ind = r.get("indices")
            if not (isinstance(ind, list) and idx is not None and ind == idx and all(type(x) is int for x in ind)):
                why.append("indices list != filename range (explicit list required)")
            for k in ("full_index", "sub_index"):
                if k in r:
                    why.append("batch record carries %s" % k)
            if kind == "batch_r3" and r.get("index") != "batch_%05d_%05d" % (lo, hi):
                why.append("batch _r3 index label != filename")
        if kind in ("r3", "batch_r3"):
            if kind == "r3" and r.get("kind") != R3_KIND[fam]:
                why.append("_r3 kind %r unexpected" % r.get("kind"))
            if kind == "batch_r3":
                if r.get("kind") != "partbatch":
                    why.append("batch _r3 kind %r != partbatch" % r.get("kind"))
                if "cnf_matches_original_sha" in r and r["cnf_matches_original_sha"] is not True:
                    why.append("cnf_matches_original_sha is not True")
            bname = ("f%05d.json" % lo) if kind == "r3" else ("batch_%05d_%05d.json" % (lo, hi))
            br = store.load(d + "/" + bname)
            if not isinstance(br, dict) or br.get("__unreadable__"):
                why.append("_r3 has no readable original record to bind its CNF")
            elif br.get("cnf_sha256") != r.get("cnf_sha256") or br.get("cnf_bytes") != r.get("cnf_bytes"):
                why.append("_r3 cnf_sha256/bytes != original record's")
        rec = {"name": name, "kind": kind, "lo": lo, "hi": hi, "sha256": store.sha(rel), "ok": not why,
               "tier": tier if not why else None, "rev": r.get("stream_check_revision"),
               "solver": solver_family(r), "reasons": why, "psnap": int(store.parent_hash(rel) is not None),
               "lacking": "|".join(lacking(r))}
        if rec["ok"]:
            recs.append(rec)
        else:
            for w in why:
                rejected[w] = rejected.get(w, 0) + 1
            rejected.setdefault("__files__", []).append(name)
            if checker_rejected(r):
                alarms.append([name, checker_rejected(r)])
    best = [None] * n
    for k, rec in enumerate(recs):
        key = (rec["tier"], KIND_RANK[rec["kind"]], rec["name"])
        for i in range(rec["lo"], rec["hi"] + 1):
            b = best[i]
            if b is None or key < (recs[b]["tier"], KIND_RANK[recs[b]["kind"]], recs[b]["name"]):
                best[i] = k
    covered_mult = [0] * n
    for rec in recs:
        for i in range(rec["lo"], rec["hi"] + 1):
            covered_mult[i] += 1
    holes = [i for i in range(n) if best[i] is None or i in sat_idx]
    used = sorted(set(b for b in best if b is not None))
    out.update({"num_full": n, "records_qualifying": len(recs), "records_rejected_files": rejected.pop("__files__", []),
                "rejected_reason_counts": rejected, "unrecognized": unrecognized,
                "holes": ranges(holes), "hole_count": len(holes),
                "overlap_indices": sum(1 for c in covered_mult if c > 1)})
    chosen = [recs[k] for k in used]
    tiers = {}
    for rec in chosen:
        tiers[rec["tier"]] = tiers.get(rec["tier"], 0) + 1
    out["chosen"] = [[d + "/" + rec["name"], rec["sha256"], rec["lo"], rec["hi"], rec["tier"], rec["rev"],
                      rec["solver"], rec["kind"], rec["psnap"]] for rec in chosen]
    out["checker_rejected_records"] = alarms
    lk = {}
    for rec in chosen:
        lk[rec["lacking"]] = lk.get(rec["lacking"], 0) + 1
    out["chosen_lacking"] = lk
    out["chosen_tiers"] = {str(k): v for k, v in sorted(tiers.items())}
    out["chosen_kinds"] = {}
    for rec in chosen:
        out["chosen_kinds"][rec["kind"]] = out["chosen_kinds"].get(rec["kind"], 0) + 1
    out["index_map_digest"] = sha256_bytes(json.dumps([c[:4] for c in out["chosen"]], separators=(",", ":")).encode())
    if out["sat"]:
        out["reasons"].append("SAT claim on a split record")
    if out_of_range:
        out["reasons"].append("record(s) reference indices outside the placement list: %s" % out_of_range)
    if holes:
        out["reasons"].append("%d placement indices not covered by a qualifying record" % len(holes))
    out["ok"] = not out["reasons"] and n > 0 and not holes
    out["empty_cover"] = n == 0
    if n == 0:  # parent rule 2026-10-18: an empty list is never a DRAT/0-of-0 PASS; distinct count only
        out["reasons"].append("EMPTY-COVER: num_full == 0; needs an explicitly accepted structural route")
        out["ok"] = False
    out["tier"] = max(tiers) if out["ok"] else None
    return out


def eval_cell(store, lane, base):
    """ms06_s00468 frozen six-unit cover of cell (row 8, column 6)."""
    tag, row, col = S00468["tag"], S00468["row"], S00468["column"]
    out = {"route": "cell", "dir": "cycle2/cell-cover/%s/r08_c06" % tag, "ok": False, "reasons": [], "tier": None,
           "sat": False, "records": []}
    names = lane.listdir(out["dir"])
    extra_units = [nme for nme in names if re.fullmatch(r"s\d+\.json", nme) and not re.fullmatch(r"s0[0-5]\.json", nme)]
    if extra_units:
        out["reasons"].append("unexpected unit records beyond s00..s05: %s" % extra_units)
    sib = [x for x in lane.listdir("cycle2/cell-cover/%s" % tag) if x != "r08_c06"]
    out["sibling_cell_dirs"] = sib
    if sib:
        out["reasons"].append("cell-cover tree has entries other than the frozen r08_c06: %s" % sib)
    cr = store.load(CONTRACT[0])
    out["contract"] = {"path": CONTRACT[0], "sha256": store.sha(CONTRACT[0]),
                       "fields_equal": isinstance(cr, dict) and all(cr.get(k) == v for k, v in CONTRACT[1].items())}
    if not out["contract"]["fields_equal"]:
        out["reasons"].append("six-unit contract fields differ from the frozen expectation")
    for nme in names:
        if not re.fullmatch(r"s0[0-5]\.json", nme) and nme.endswith(".json"):
            rr = store.load(out["dir"] + "/" + nme)
            if sat_claim(rr):
                out["sat"] = True
                out["reasons"].append("SAT claim in %s" % nme)
            if nme.startswith("deferred") and not (isinstance(rr, dict) and rr.get("status") == "UNKNOWN"):
                out["reasons"].append("deferred record %s not an UNKNOWN stop record" % nme)
    cnf_rel = "cases19skel/cnf/%s.cnf" % tag
    bb = lane.read(cnf_rel)
    if bb is None:
        out["reasons"].append("base CNF missing")
        return out
    bsha = sha256_bytes(bb)
    out["base_cnf"] = {"path": cnf_rel, "sha256": bsha, "bytes": len(bb)}
    if bsha != S00468["base_sha"] or bsha != base["sha"] or len(bb) != base["bytes"]:
        out["reasons"].append("base CNF sha/bytes != contract and parent R5 rebuild")
        return out
    head, sep, body = bb.partition(b"\n")
    hp = head.split()
    if not (sep and len(hp) == 4 and hp[:2] == [b"p", b"cnf"] and bb.endswith(b"\n")):
        out["reasons"].append("base CNF header malformed")
        return out
    nv, nc = int(hp[2]), int(hp[3])
    lits = [1 + (row * 8 + col) * 6 + s for s in range(6)]
    alo = (" ".join(map(str, lits)) + " 0").encode()
    lines = body.split(b"\n")
    out["alo_clause_present"] = alo in lines
    out["alo_clause"] = alo.decode()
    out["clause_lines"] = len(lines) - 1 if lines and lines[-1] == b"" else len(lines)
    if not out["alo_clause_present"]:
        out["reasons"].append("base CNF lacks the at-least-one clause for cell (8,6): six units not exhaustive")
    if out["clause_lines"] != nc:
        out["reasons"].append("base clause count != header")
    if any(not (1 <= l <= nv) for l in lits):
        out["reasons"].append("unit literal outside variable range")
    body_sha = sha256_bytes(body)
    del lines
    for s in range(6):
        rel = "%s/s%02d.json" % (out["dir"], s)
        r = store.load(rel)
        unit = ("%d 0\n" % lits[s]).encode()
        expected = ("p cnf %d %d\n" % (nv, nc + 1)).encode() + body + unit
        esha, elen = sha256_bytes(expected), len(expected)
        del expected
        why = []
        if r is None:
            why.append("record missing")
            r = {}
        elif not isinstance(r, dict) or r.get("__unreadable__"):
            why.append("unreadable record")
            r = {}
        sw, tier = stream_predicate(r) if r else (["no record"], None)
        why += sw
        if r and r.get("stream_check_revision") not in (13, 14):
            why.append("revision not in the frozen cell-cover set (13, 14)")
        checks = {"tag": tag, "row": row, "column": col, "symbol": s, "unit_literal": lits[s],
                  "unit_clause": unit.decode(), "base_header": head.decode(), "base_cnf_sha256": bsha,
                  "base_body_sha256": body_sha, "base_byte_identical": True, "exact_one_unit_append": True,
                  "base_bytes": len(bb), "cnf_sha256": esha, "cnf_bytes": elen,
                  "encoder": "encode_skel.py + exactly one cell unit"}
        for k, v in checks.items():
            got = r.get(k)
            if type(got) is not type(v) or got != v:
                why.append("field %s != expected" % k)
        out["records"].append({"symbol": s, "path": rel, "sha256": store.sha(rel), "expected_cnf_sha256": esha,
                               "ok": not why, "tier": tier if not why else None, "reasons": why,
                               "rev": r.get("stream_check_revision"), "solver": solver_family(r) if r else None,
                               "lacking": lacking(r) if r else ["<no record>"]})
        if sat_claim(r):
            out["sat"] = True
    bad = [x["symbol"] for x in out["records"] if not x["ok"]]
    if bad:
        out["reasons"].append("unit subcases not qualifying: %s" % bad)
    if out["sat"]:
        out["reasons"].append("SAT claim on a cell subcase path")
    out["ok"] = not out["reasons"] and len(out["records"]) == 6
    out["tier"] = max(x["tier"] for x in out["records"]) if out["ok"] else None
    return out


def eval_e0(store, lane, g):
    tag = g["tag"]
    res_rel, chk_rel = "cases19q0/results/%s.json" % tag, "cases19q0/results/%s.check.json" % tag
    a, c = store.load(res_rel), store.load(chk_rel)
    why = [store.drift_reason(p) for p in (res_rel, chk_rel) if store.drift_reason(p)]
    if not isinstance(a, dict) or a.get("__unreadable__"):
        why.append("result record missing/unreadable")
        a = {}
    if not isinstance(c, dict) or c.get("__unreadable__"):
        why.append("check record missing/unreadable")
        c = {}
    if a and set(a) != E0_RES_KEYS:
        why.append("E0 result schema deviation")
    if c and set(c) != E0_CHK_KEYS:
        why.append("E0 check schema deviation")
    if a.get("tag") != tag or c.get("tag") != tag:
        why.append("tag mismatch")
    if a.get("status") != "UNSAT" or type(a.get("returncode")) is not int or a.get("returncode") != 20:
        why.append("solve status/rc not UNSAT/20")
    if a.get("graph6") != g["graph6"]:
        why.append("graph6 != pinned index")
    if a.get("cnf") != "cases19q0/cnf/%s.cnf" % tag or a.get("proof") != "cases19q0/proof/%s.drat" % tag:
        why.append("cnf/proof path not the tag's stored files")
    ca = a.get("cnf_sha256")
    if not is_hex(ca) or c.get("cnf_sha256_now") != ca or c.get("cnf_sha256_at_solve") != ca:
        why.append("CNF sha not consistent between solve and check")
    if not is_hex(c.get("proof_sha256")) or not pos_int(c.get("proof_bytes")) or c.get("proof_bytes") != a.get("proof_bytes"):
        why.append("proof hash/bytes missing or inconsistent (proof-free)")
    if type(c.get("drat_trim_rc")) is not int or c.get("drat_trim_rc") != 0:
        why.append("drat_trim_rc != 0")
    if c.get("drat_trim_verified") is not True or c.get("ok") is not True:
        why.append("drat_trim_verified/ok not True")
    tail = c.get("drat_trim_tail")
    if not (isinstance(tail, list) and tail and all(type(x) is str for x in tail)):
        why.append("drat_trim_tail missing")
    else:
        if sum(1 for x in tail if x == "s VERIFIED") != 1:
            why.append("retained tail lacks exactly one exact 's VERIFIED' line")
        if any(x.strip("\r") in BAD_TAIL for x in tail):
            why.append("tail contradicts (NOT VERIFIED/TIMEOUT)")
        if not tail[-1].startswith("c verification time:"):
            why.append("tail lacks final verification-time line")
    pst = lane.stat("cases19q0/proof/%s.drat" % tag)
    return {"tag": tag, "graph6": g["graph6"], "ok": not why, "reasons": why, "tier": 6 if not why else None,
            "result": {"path": res_rel, "sha256": store.sha(res_rel), "parent_snapshot": store.parent_hash(res_rel)},
            "check": {"path": chk_rel, "sha256": store.sha(chk_rel), "parent_snapshot": store.parent_hash(chk_rel)},
            "cnf_sha256": ca, "proof_sha256": c.get("proof_sha256"), "sat": sat_claim(a) or sat_claim(c),
            "stored_proof": {"path": "cases19q0/proof/%s.drat" % tag, "exists": pst is not None,
                             "size_equals_proof_bytes": bool(pst and pst[0] == c.get("proof_bytes"))}}


def load_refs():
    """Load parent reference receipts; a receipt whose SHA-256 differs from its pin is NOT used (fail closed)."""
    pins, out = {}, {}
    for key, (rel, exp) in PARENT_PINS.items():
        with open(os.path.join(REVIEW, rel), "rb") as f:
            b = f.read()
        sha = sha256_bytes(b)
        pins[key] = {"path": "review/" + rel, "sha256": sha, "expected": exp, "match": sha == exp}
        out[key] = b if sha == exp else None
    base, prefs, fmap = {}, {}, {}
    if out["R5_cnf_binding"] is not None:
        r5 = json.loads(out["R5_cnf_binding"])
        for t in r5["per_tag"]:
            pass1 = "cases19skel/results/%s.json" % t["tag"]
            base[t["tag"]] = {"sha": t.get("cnf_sha256"), "bytes": t.get("cnf_bytes"),
                              "spec_sha256": t.get("spec_sha256"),
                              "pass1_bound": pass1 in (t.get("matching") or []) and not t.get("mismatching")}
    if out["R6_placement_binding"] is not None:
        r6 = json.loads(out["R6_placement_binding"])
        for c in r6["cases"]:
            fam = "a3" if c["multiset"] == 1 else "part"
            regen = (c.get("shas") or {}).get("m1_regen")
            if c.get("status") == "REPLAYED_MATCH" and is_hex(regen):
                prefs[(fam, c["tag"])] = {"sha256": regen,
                                          "label": "parent-R6-regenerated (%s)" % c.get("m1_binding")}
        for it in (r6.get("incremental_binding") or {}).get("m1_lists_absent_at_read", []):
            key = ("part" if it["tag"].startswith("ms09") else "a3", it["tag"])
            if key not in prefs and is_hex(it.get("predicted_sha256")) and it.get("now_equals_predicted") is True:
                prefs[key] = {"sha256": it["predicted_sha256"], "label": "parent-R6-predicted-then-equal"}
    if out["ms06_s00150_binding_v2"] is not None:
        v2 = json.loads(out["ms06_s00150_binding_v2"])
        if v2.get("verdict") == "PASS" and v2.get("semantic_equal_except_source") is True:
            prefs[("part", "ms06_s00150")] = {"sha256": v2["pins"]["ext-live.json"],
                                              "label": "parent-replay-semantic-equal-except-source (ms06-binding-v2)"}
    if out["R8_subcase_binding"] is not None:
        for it in json.loads(out["R8_subcase_binding"])["items"]:
            if it.get("status") == "PASS":
                fmap[it["path"]] = {"sha256": it["record_sha256"], "label": "parent-R8-formula-bound"}
    if out["R8_inc001_late_census"] is not None and out["ms06_s00150_binding_v2"] is not None:
        for line in out["R8_inc001_late_census"].decode().splitlines():
            if not line.strip():
                continue
            it = json.loads(line)
            if it.get("status") in ("PASS", "FORMULA_EQUAL_LIST_UNVERIFIED"):
                fmap.setdefault(it["path"], {"sha256": it["record_sha256"],
                                             "label": "parent-R8-inc001-formula-equal (+ms06-binding-v2 list)"})
    snap = {}
    if out["R7_strict_aggregate_v2"] is not None:
        for k, v in json.loads(out["R7_strict_aggregate_v2"])["record_manifest"].items():
            snap[k] = (v, "R7-strict-aggregate-v2@2026-10-17T14:39")
    out["R7_strict_aggregate_v2"] = None
    if out["R8_population"] is not None:
        for line in out["R8_population"].decode().splitlines():
            if line.strip():
                it = json.loads(line)
                prev = snap.get(it["path"])
                if prev is not None and prev[0] != it["sha256"]:
                    snap[it["path"]] = ("<conflicting parent snapshots>", "R7-vs-R8-population-conflict")
                elif prev is None:
                    snap[it["path"]] = (it["sha256"], "R8-population@2026-10-17T14:56")
    out["R8_population"] = None
    return pins, base, prefs, fmap, snap


def inventory(lane, roots):
    inv = {}
    for root in roots:
        p = os.path.join(lane.root, root)
        try:
            with os.scandir(p) as it:
                for e in it:
                    if e.is_file(follow_symlinks=False):
                        st = e.stat(follow_symlinks=False)
                        inv[root + "/" + e.name] = (st.st_size, st.st_mtime_ns)
        except FileNotFoundError:
            pass
    return inv


def evaluate(lane, refs, scope_tags=None, e0_scope=None):
    """Core evaluation. scope_tags/e0_scope restrict cases (controls); production passes None (all)."""
    pins, base_map, prefs, fmap, snap = refs
    store = Store(lane, snap)
    idx = store.load("cases19skel/index.json")
    q0 = store.load("cases19q0/index.json")
    problems = []
    for rel, exp in LANE_PINS.items():
        if store.sha(rel) != exp:
            problems.append("lane input %s sha != parent pin" % rel)
    cases = idx["cases"]
    tags = [c["tag"] for c in cases]
    seen, per_ms = set(), {}
    for c in cases:
        if c["tag"] != "ms%02d_s%05d" % (c["multiset"], c["skel"]) or c["tag"] in seen:
            problems.append("index identity problem %r" % c.get("tag"))
        seen.add(c["tag"])
        per_ms[c["multiset"]] = per_ms.get(c["multiset"], 0) + 1
    if per_ms != COUNTS or len(cases) != 5577:
        problems.append("A2 index counts %r != expected" % per_ms)
    rows = []
    for c in cases:
        tag, mi = c["tag"], c["multiset"]
        if scope_tags is not None and tag not in scope_tags:
            continue
        base = base_map.get(tag)
        row = {"tag": tag, "ms": mi, "skel": c["skel"], "routes": [], "state": "UNKNOWN", "reasons": []}
        if base is None or not is_hex(base["sha"]) or not pos_int(base["bytes"]) or not base["pass1_bound"]:
            row["reasons"].append("no parent R5 base CNF binding")
            rows.append(row)
            continue
        row["base_cnf_sha256"] = base["sha"]
        p1rel = "cases19skel/results/%s.json" % tag
        p1 = store.load(p1rel)
        row["pass1"] = {"path": p1rel, "sha256": store.sha(p1rel),
                        "status": p1.get("status") if isinstance(p1, dict) else None}
        if not (isinstance(p1, dict) and p1.get("tag") == tag and p1.get("cnf_sha256") == base["sha"]):
            row["reasons"].append("pass-1 record identity/CNF sha != parent R5")
        if store.drift_reason(p1rel):
            row["reasons"].append("pass-1 " + store.drift_reason(p1rel))
        sat = sat_claim(p1)
        cand = []
        a = eval_proofcheck(store, lane, "cases19skel/proofcheck/%s.json" % tag, tag, base, p1)
        if a:
            cand.append(a)
        for route, sub in (("b", "cycle2/proofstream"), ("c5", "cycle2/hard5")):
            x = eval_direct(store, "%s/%s.json" % (sub, tag), tag, base, route)
            if x:
                cand.append(x)
        hr = "cycle2/hard/%s.json" % tag
        h = store.load(hr)
        if h is not None:
            hw, _ = stream_predicate(h) if isinstance(h, dict) else (["unreadable"], None)
            cand.append({"route": "hard", "path": hr, "sha256": store.sha(hr), "ok": False,
                         "reasons": ["cycle2/hard is the CaDiCaL LRAT + lrat-check route, never counted"] + hw,
                         "tier": None, "rev": h.get("stream_check_revision") if isinstance(h, dict) else None,
                         "solver": solver_family(h) if isinstance(h, dict) else None, "sat": sat_claim(h)})
        for fam in ("a3", "part"):
            s = eval_split(store, lane, fam, tag, prefs)
            if s:
                cand.append(s)
        if tag == S00468["tag"] or lane.isdir("cycle2/cell-cover/%s" % tag):
            if tag == S00468["tag"]:
                cand.append(eval_cell(store, lane, base))
            else:
                cand.append({"route": "cell", "dir": "cycle2/cell-cover/%s" % tag, "ok": False,
                             "reasons": ["unexpected cell-cover tree (only ms06_s00468 is frozen)"], "tier": None,
                             "sat": False})
        sat = sat or any(x.get("sat") for x in cand)
        quals = [x for x in cand if x["ok"]]
        for x in cand:
            row["routes"].append(compact_route(x, fmap))
        if sat:
            row["state"] = "SAT-CLAIM"
            row["reasons"].append("a SAT claim exists on this case path")
        elif quals and not row["reasons"]:
            order = {"b": 0, "c5": 1, "a": 2, "cell": 3, "d": 4, "e": 5}
            best = min(quals, key=lambda x: (x["tier"], order[x["route"]]))
            row["state"] = "COVERED"
            row["chosen"] = compact_route(best, fmap)
            row["chosen_tier"] = TIER_NAME[best["tier"]]
            prod = [r for r in ("a", "b", "c5", "d", "e", "cell") if any(q["route"] == r for q in quals)]
            row["producer_order_route"] = prod[0]
        elif not quals:
            row["reasons"].append("no qualifying M1 route")
        rows.append(row)
    e0 = []
    gl = q0["cases"]
    if len(gl) != 486 or q0.get("num_cases") != 486 or len(set(g["tag"] for g in gl)) != 486:
        problems.append("E0 index count/identity problem")
    for i, g in enumerate(gl):
        if g["tag"] != "g%03d" % i:
            problems.append("E0 tag order problem at %d" % i)
        if e0_scope is not None and g["tag"] not in e0_scope:
            continue
        e0.append(eval_e0(store, lane, g))
    return store, rows, e0, problems, tags


def compact_route(x, fmap):
    c = {"route": x["route"], "ok": x["ok"], "tier": x.get("tier")}
    if x["route"] in ("a", "b", "c5", "hard"):
        c.update({"path": x["path"], "sha256": x["sha256"], "rev": x.get("rev"), "solver": x.get("solver"),
                  "parent_snapshot_hash_equal": x.get("parent_snapshot_hash_equal"), "lacking": x.get("lacking")})
        if x.get("checker_rejection"):
            c["checker_rejection"] = x["checker_rejection"]
        if x["route"] == "a":
            c["stored_proof"] = x.get("stored_proof")
        if x["ok"]:
            c["cnf_binding"] = ("record cnf_sha256 (stored CNF file hashed at check time) == parent R5 rebuild"
                                if x["route"] == "a" else "record cnf_sha256 and cnf_bytes == parent R5 rebuild")
        else:
            c["reasons"] = x["reasons"]
    elif x["route"] == "cell":
        c.update({"dir": x["dir"], "base_cnf": x.get("base_cnf"), "alo_clause_present": x.get("alo_clause_present"),
                  "alo_clause": x.get("alo_clause"), "contract": x.get("contract"),
                  "sibling_cell_dirs": x.get("sibling_cell_dirs"),
                  "records": [{k: r[k] for k in ("symbol", "path", "sha256", "expected_cnf_sha256", "ok", "tier", "rev",
                                                 "solver", "lacking")} | ({"reasons": r["reasons"]} if not r["ok"] else {})
                              for r in x.get("records", [])]})
        if not x["ok"]:
            c["reasons"] = x["reasons"]
    else:
        ch = x.get("chosen") or []
        fb = sum(1 for p in ch if fmap.get(p[0], {}).get("sha256") == p[1])
        c.update({"dir": x["dir"], "ext": x.get("ext"), "num_full": x.get("num_full"),
                  "records_qualifying": x.get("records_qualifying"), "records_chosen": len(ch),
                  "chosen_tiers": x.get("chosen_tiers"), "chosen_kinds": x.get("chosen_kinds"),
                  "overlap_indices": x.get("overlap_indices"), "hole_count": x.get("hole_count"),
                  "holes": x.get("holes"), "rejected_reason_counts": x.get("rejected_reason_counts"),
                  "records_rejected_files": x.get("records_rejected_files"), "unrecognized": x.get("unrecognized"),
                  "index_map_digest": x.get("index_map_digest"), "chosen_formula_bound_by_parent_R8": fb,
                  "chosen_parent_snapshot_hash_equal": sum(p[8] for p in ch),
                  "checker_rejected_records": x.get("checker_rejected_records"),
                  "chosen_lacking": x.get("chosen_lacking"),
                  "empty_cover": x.get("empty_cover", False)})
        if not x["ok"]:
            c["reasons"] = x["reasons"]
        c["_chosen"] = ch
    return c


def main():
    outdir = sys.argv[1]
    os.mkdir(outdir)  # exclusive: fails if it exists
    t_start = now()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from token_ro import ReadOnlyToken
    self_sha = sha256_bytes(open(os.path.abspath(__file__), "rb").read())
    with ReadOnlyToken() as tok:
        tokinfo = {"name": tok.name, "acquired_at": tok.acquired_at, "waited_s": tok.waited_s}
        lane = Lane(LANE_ROOT)
        roots = ["cases19skel/results", "cases19skel/proofcheck", "cycle2/proofstream", "cycle2/hard", "cycle2/hard5",
                 "cases19q0/results", "cycle2/cell-cover/ms06_s00468/r08_c06"]
        for fam in ("a3", "part"):
            roots.append("cycle2/" + fam)
            roots += ["cycle2/%s/%s" % (fam, n) for n in sorted(os.listdir(os.path.join(LANE_ROOT, "cycle2", fam)))
                      if os.path.isdir(os.path.join(LANE_ROOT, "cycle2", fam, n))]
        inv0 = inventory(lane, roots)
        t_inv0 = now()
        refs = load_refs()
        store, rows, e0, problems, tags = evaluate(lane, refs)
        t_eval = now()
        # Every JSON under the route trees is loaded once more for SAT/orphan accounting if not yet consumed.
        orphans = []
        tagset = set(tags)
        for rel in sorted(inv0):
            if not rel.endswith(".json") or rel in store.manifest:
                continue
            r = store.load(rel)
            base = os.path.basename(rel)
            if rel.startswith(("cases19skel/", "cycle2/proofstream/", "cycle2/hard/", "cycle2/hard5/")):
                if base[:-5] not in tagset:
                    orphans.append(rel)
            else:
                orphans.append(rel)
        archive_sat, archive_rev10 = [], 0
        for dp, dn, fn in os.walk(os.path.join(LANE_ROOT, "archive")):
            for f in fn:
                if f.endswith(".json"):
                    p = os.path.join(dp, f)
                    try:
                        r = json.loads(open(p, "rb").read())
                    except (ValueError, OSError):
                        continue
                    if sat_claim(r):
                        archive_sat.append(os.path.relpath(p, LANE_ROOT))
                    if isinstance(r, dict) and r.get("stream_check_revision") == 10:
                        archive_rev10 += 1
        side = side_checks(store, lane, rows, refs)
        inv1 = inventory(lane, roots)
        t_inv1 = now()
    rootset = set(roots)
    changed = sorted(k for k in store.manifest if k in inv0 and inv0[k][1] != store.manifest[k]["mtime_ns"])
    late = sorted(k for k in store.manifest if os.path.dirname(k) in rootset and k not in inv0)
    drift = {"inventory_start": t_inv0, "inventory_end": t_inv1, "files_start": len(inv0), "files_end": len(inv1),
             "added_after_start": sorted(set(inv1) - set(inv0)), "removed_after_start": sorted(set(inv0) - set(inv1)),
             "changed_after_start": sorted(k for k in set(inv0) & set(inv1) if inv0[k] != inv1[k]),
             "consumed_mtime_differs_from_start_inventory": changed, "consumed_not_in_start_inventory": late}
    write_outputs(outdir, self_sha, tokinfo, t_start, t_eval, refs, store, rows, e0, problems, drift, orphans,
                  archive_sat, archive_rev10, side)


def side_checks(store, lane, rows, refs):
    """Hash rechecks of small metadata and producer-summary comparison (informational; nothing inherited)."""
    out = {}
    for key, (rel, exp) in (("candidate", CAND), ("STATUS15", STATUS15)):
        r = store.load(rel)
        out[key] = {"path": rel, "sha256": store.sha(rel), "pinned": exp, "match": store.sha(rel) == exp}
        snap = (r or {}).get("strict_snapshot", r) if key == "candidate" else r
        if isinstance(snap, dict):
            mine = {}
            for row in rows:
                m = mine.setdefault("ms%02d" % row["ms"], {"M1_certified": 0, "M1_how": {}})
                if row["state"] == "COVERED":
                    m["M1_certified"] += 1
                    how = {"cell": "cell-six-unit"}.get(row["producer_order_route"], row["producer_order_route"])
                    m["M1_how"][how] = m["M1_how"].get(how, 0) + 1
            prod = {k: {"M1_certified": v.get("M1_certified"), "M1_how": v.get("M1_how")}
                    for k, v in (snap.get("per_multiset") or {}).items()}
            out[key]["producer_vs_independent_per_multiset_equal"] = prod == mine
            out[key]["diff"] = {k: {"producer": prod.get(k), "independent_producer_order": mine.get(k)}
                                for k in sorted(set(prod) | set(mine)) if prod.get(k) != mine.get(k)}
            out[key]["producer_M1_open"] = snap.get("M1_open")
            out[key]["producer_E0"] = snap.get("E0_ms00")
    src = {}
    for f in ("stream_check4.py", "stream_check5.py", "stream_check9.py", "stream_check12.py", "stream_check13.py",
              "stream_check14.py", "stream_check15.py", "run_proofpass.py", "check_proofs.py", "run_hard5.py",
              "run_hard6.py", "run_hard8.py", "run_hard9.py", "run_hard12.py", "run_hard13.py", "run_hard14.py",
              "run_hard15.py", "rerun_exact.py", "rerun5.py", "rerun_batch12.py", "rerun_batch15.py",
              "run_s00468_cell.py", "run_s00468_cell14.py", "summarize12.py", "encode_skel.py", "encode_full.py",
              "encode_full2.py", "encode_partq.py", "encode_partbatch.py", "extend_p1.py", "extend_p1q.py",
              "encode_q0.py", "run_cases.py", "run_proofpass_stream.py", "aggregate15.py", "summarize15.py"):
        b = lane.read("src/" + f)
        src[f] = sha256_bytes(b) if b is not None else None
    out["src_sha256_now"] = src
    c = store.load(CONTRACT[0]) or {}
    out["contract_runner_aggregator"] = {
        "runner_pinned": c.get("runner_sha256"), "runner_now": src.get("run_s00468_cell.py"),
        "runner_match": c.get("runner_sha256") == src.get("run_s00468_cell.py"),
        "aggregator_pinned": c.get("aggregator_sha256"), "aggregator_now": src.get("summarize12.py"),
        "aggregator_match": c.get("aggregator_sha256") == src.get("summarize12.py")}
    g = store.load("cycle2/guard15-freeze-20261018T004542.json") or {}
    out["guard15_freeze_files_match_now"] = {k: (src.get(k) == v if k in src else sha256_bytes(lane.read("src/" + k) or b"") == v)
                                             for k, v in (g.get("files_sha256") or {}).items()}
    pr = json.loads(open(os.path.join(REVIEW, PARENT_PINS["R0_pin_result"][0]), "rb").read())
    dt_pin = (pr.get("files") or {}).get("tools/drat-trim/drat-trim")
    dt_now = sha256_bytes(lane.read("tools/drat-trim/drat-trim") or b"")
    out["drat_trim_binary"] = {"parent_R0_pin": dt_pin, "now": dt_now, "match": dt_pin == dt_now,
                               "source_commit": (lane.read("tools/drat-trim/COMMIT.txt") or b"").decode().strip()}
    bp = store.load("cycle2/binding-pass1.json")
    out["worker_binding_pass1"] = {"sha256": store.sha("cycle2/binding-pass1.json"),
                                   "parent_R5_pinned_sha256": "659f18eaf3c6bbeb5fbd9984914c7309750040aeb7436191e89795bdd19b1472",
                                   "summary": (bp or {}).get("summary")}
    return out


def summarize(rows, e0):
    per_ms, tiers, alt, holes, empty = {}, {}, {}, [], []
    prov = {"direct_base_cnf_R5": {}, "split_ext_binding": {}, "split_records_chosen": 0,
            "split_records_formula_bound_parent_R8": 0, "split_records_formula_worker_only": 0,
            "split_cases_by_weakest_tier": {}, "cell": None, "chosen_direct_record_hash_equals_parent_snapshot": 0,
            "chosen_split_records_hash_equals_parent_snapshot": 0, "checker_rejections_seen": []}
    for r in rows:
        m = per_ms.setdefault("ms%02d" % r["ms"], {"cases": 0, "COVERED": 0, "UNKNOWN": 0, "SAT-CLAIM": 0,
                                                    "chosen_route": {}, "producer_order_route": {}})
        m["cases"] += 1
        m[r["state"]] += 1
        if any(x.get("empty_cover") for x in r["routes"]):
            empty.append(r["tag"])
        for x in r["routes"]:
            if x.get("checker_rejection"):
                prov["checker_rejections_seen"].append([r["tag"], x["path"], x["checker_rejection"]])
            for f, lab in x.get("checker_rejected_records") or []:
                prov["checker_rejections_seen"].append([r["tag"], "%s/%s" % (x["dir"], f), lab])
        if r["state"] == "COVERED":
            c = r["chosen"]
            cr = c["route"]
            m["chosen_route"][cr] = m["chosen_route"].get(cr, 0) + 1
            m["producer_order_route"][r["producer_order_route"]] = m["producer_order_route"].get(r["producer_order_route"], 0) + 1
            tiers[r["chosen_tier"]] = tiers.get(r["chosen_tier"], 0) + 1
            q = "+".join(sorted(x["route"] for x in r["routes"] if x["ok"]))
            alt[q] = alt.get(q, 0) + 1
            if cr in ("a", "b", "c5"):
                prov["direct_base_cnf_R5"][cr] = prov["direct_base_cnf_R5"].get(cr, 0) + 1
                prov["chosen_direct_record_hash_equals_parent_snapshot"] += int(bool(c.get("parent_snapshot_hash_equal")))
            elif cr in ("d", "e"):
                lab = "%s|%s" % (cr, c["ext"]["binding"])
                prov["split_ext_binding"][lab] = prov["split_ext_binding"].get(lab, 0) + 1
                prov["split_records_chosen"] += c["records_chosen"]
                prov["split_records_formula_bound_parent_R8"] += c["chosen_formula_bound_by_parent_R8"]
                prov["split_records_formula_worker_only"] += c["records_chosen"] - c["chosen_formula_bound_by_parent_R8"]
                prov["chosen_split_records_hash_equals_parent_snapshot"] += c["chosen_parent_snapshot_hash_equal"]
                prov["split_cases_by_weakest_tier"][TIER_NAME[c["tier"]]] = prov["split_cases_by_weakest_tier"].get(TIER_NAME[c["tier"]], 0) + 1
            elif cr == "cell":
                prov["cell"] = {"tag": r["tag"], "base_cnf": c["base_cnf"], "alo_clause_present": c["alo_clause_present"],
                                "subcase_cnf_sha256": "auditor recomputed from base CNF bytes + one unit; equal to records",
                                "contract": c["contract"]}
        else:
            holes.append({"tag": r["tag"], "state": r["state"], "reasons": r["reasons"],
                          "route_reasons": {x["route"]: x.get("reasons") for x in r["routes"] if not x["ok"]}})
    return per_ms, tiers, alt, holes, empty, prov


def bridge_census(rows, e0):
    """Counted (chosen) records by route x revision x solver, and counted records by actually-absent acceptance
    fields (presence check on the record itself, not inferred from the revision)."""
    cen, lack = {}, {}

    def add(route, rev, solver, n=1):
        k = "%s|rev=%s|%s" % (route, "absent" if rev is None else rev, solver)
        cen[k] = cen.get(k, 0) + n

    def lackadd(route, fields, n=1):
        for f in (fields or "").split("|") if isinstance(fields, str) else (fields or []):
            if f:
                k = "%s|%s" % (route, f)
                lack[k] = lack.get(k, 0) + n

    for r in rows:
        if r["state"] != "COVERED":
            continue
        c = r["chosen"]
        if c["route"] in ("a", "b", "c5"):
            add(c["route"], c["rev"], c["solver"])
            lackadd(c["route"], c.get("lacking"))
        elif c["route"] == "cell":
            for x in c["records"]:
                add("cell", x["rev"], x["solver"])
                lackadd("cell", x.get("lacking"))
        else:
            for p in c["_chosen"]:
                add(c["route"], p[5], p[6])
            for sig, n in (c.get("chosen_lacking") or {}).items():
                lackadd(c["route"], sig, n)
    for g in e0:
        if g["ok"]:
            add("E0", None, "kissat")
            lackadd("E0", ["solver_stop", "drat_trim.stop(self-exit flag; check ran to completion via subprocess.run)",
                           "drat_trim.s_lines (retained tail holds the exact 's VERIFIED' line instead)",
                           "replay(feed-completion)", "reader_ok(compressed-buffer)"])
    return {"counted_records_by_route_rev_solver": dict(sorted(cen.items())),
            "counted_records_lacking_fields": dict(sorted(lack.items())),
            "note": "route a = cycle-1 proofcheck schema (kissat_rc + drat_trim_verified + 2-line tail; drat-trim rc and "
                    "self-exit not recorded); E0 = cycle-1 .check.json schema (drat_trim_rc recorded, 3-line tail)."}


def write_outputs(outdir, self_sha, tokinfo, t_start, t_eval, refs, store, rows, e0, problems, drift, orphans,
                  archive_sat, archive_rev10, side):
    pins = refs[0]
    per_ms, tiers, alt, holes, empty, prov = summarize(rows, e0)
    e0_ok = sum(1 for g in e0 if g["ok"])
    e0_holes = [{"tag": g["tag"], "reasons": g["reasons"]} for g in e0 if not g["ok"]]
    split_map = []
    with open(os.path.join(outdir, "cases-A2.jsonl"), "x") as f:
        for r in rows:
            rr = json.loads(json.dumps(r))
            for x in rr["routes"] + ([rr["chosen"]] if "chosen" in rr else []):
                x.pop("_chosen", None)
            f.write(json.dumps(rr, separators=(",", ":"), sort_keys=True) + "\n")
            if r["state"] == "COVERED" and r["chosen"]["route"] in ("d", "e"):
                split_map.append({"tag": r["tag"], "route": r["chosen"]["route"], "ext": r["chosen"]["ext"],
                                  "chosen[path,sha256,lo,hi,tier,rev,solver,kind]": r["chosen"]["_chosen"]})
    with open(os.path.join(outdir, "cases-E0.jsonl"), "x") as f:
        for g in e0:
            f.write(json.dumps(g, separators=(",", ":"), sort_keys=True) + "\n")
    with gzip.open(os.path.join(outdir, "split-index-map.jsonl.gz"), "xt", compresslevel=6) as f:
        for s in split_map:
            f.write(json.dumps(s, separators=(",", ":")) + "\n")
    with gzip.open(os.path.join(outdir, "consumed-manifest.tsv.gz"), "xt", compresslevel=6) as f:
        f.write("path\tsha256\tsize\tmtime_ns\n")
        for k in sorted(store.manifest):
            m = store.manifest[k]
            f.write("%s\t%s\t%d\t%s\n" % (k, m["sha256"], m["size"], m["mtime_ns"]))
    covered = sum(1 for r in rows if r["state"] == "COVERED")
    sats = sorted(set(store.sats))
    pin_bad = [k for k, v in pins.items() if not v["match"]]
    consumed_drift = drift["consumed_mtime_differs_from_start_inventory"] + drift["consumed_not_in_start_inventory"]
    direct_dirs = ("cases19skel/results/", "cases19skel/proofcheck/", "cycle2/proofstream/", "cycle2/hard5/",
                   "cycle2/hard/", "cases19q0/results/")
    rec_changed, other_changed = {}, {}
    for k, v in sorted(store.changed_vs_parent.items()):
        b = os.path.basename(k)
        is_rec = classify(b)[0] is not None or b == "ext.json" or k.startswith(direct_dirs)
        (rec_changed if is_rec else other_changed)[k] = v
    psd = {"records_or_lists_changed_since_parent_snapshot": rec_changed,
           "other_files_changed_since_parent_snapshot": other_changed,
           "consumed_files_equal_to_parent_snapshot": len(store.equal_vs_parent),
           "snapshots": "R7 strict-aggregate-v2 record_manifest (2026-10-17 14:39 PDT) and R8 population.jsonl "
                        "(2026-10-17 14:56 PDT); files created later have no parent snapshot hash"}
    if problems or pin_bad or consumed_drift or store.unreadable:
        verdict = "INCONCLUSIVE (input pin/drift/unreadable problem; see fields)"
    elif sats or archive_sat:
        verdict = "SAT-CLAIM-PRESENT"
    elif covered == 5577 and len(rows) == 5577 and e0_ok == 486 and len(e0) == 486 and not rec_changed:
        verdict = "ALL-M1-RECEIPTS-QUALIFY (metadata only; schema limits and binding obligations listed)"
    else:
        verdict = "M1-RECEIPT-HOLES (see not_covered / parent_snapshot_drift)"
    res = {
        "title": "PA19FinalReceiptAudit independent M1 receipt coverage v1 (metadata only)",
        "scope": "Receipt/binding metadata only. No solver, checker, generator, encoder or model CLI ran. COVERED means "
                 "a qualifying receipt chain exists under the stated schema limits; it is NOT a native proof replay, "
                 "not an encoder-soundness or cover-completeness verdict, and not parent acceptance. M2 is out of scope "
                 "and not complete.",
        "reader_verdict": verdict,
        "started": t_start, "evaluated": t_eval, "finished": now(),
        "reader": {"path": "review/pa19-final-receipts-v1/m1_receipts_v1.py", "sha256": self_sha,
                   "python": sys.version.split()[0], "maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
        "token": tokinfo,
        "parent_reference_pins": pins,
        "lane_input_pins": {k: {"expected": v, "current": store.sha(k), "match": store.sha(k) == v} for k, v in LANE_PINS.items()},
        "input_problems": problems,
        "A2": {"cases": len(rows), "COVERED": covered, "UNKNOWN": sum(1 for r in rows if r["state"] == "UNKNOWN"),
               "SAT_CLAIM": sum(1 for r in rows if r["state"] == "SAT-CLAIM"),
               "EMPTY_COVER_NOT_ACCEPTED_cases": empty, "per_multiset": per_ms,
               "chosen_tier_counts": tiers, "qualifying_route_sets": dict(sorted(alt.items())),
               "not_covered": holes},
        "E0": {"graphs": len(e0), "COVERED": e0_ok, "not_covered": e0_holes,
               "SAT_CLAIM": sum(1 for g in e0 if g["sat"]),
               "stored_proof_exists_size_equal": sum(1 for g in e0 if g["stored_proof"]["size_equals_proof_bytes"])},
        "binding_provenance": prov,
        "sat_claims_in_consumed_records": sats,
        "sat_claims_in_archive": archive_sat, "archive_rev10_records": archive_rev10,
        "unreadable_records": store.unreadable, "orphan_or_unindexed_files": orphans,
        "drift": drift, "parent_snapshot_drift": psd, "bridge_census": bridge_census(rows, e0), "side_checks": side,
        "consumed_files": len(store.manifest),
    }
    with open(os.path.join(outdir, "RESULT-core.json"), "x") as f:
        json.dump(res, f, indent=1, sort_keys=False)
        f.write("\n")
    print(json.dumps({"verdict": verdict, "A2_COVERED": covered, "A2_cases": len(rows), "E0_COVERED": e0_ok,
                      "E0": len(e0), "SAT": len(sats), "problems": problems, "pin_bad": pin_bad,
                      "drift_added": len(drift["added_after_start"]), "drift_changed": len(drift["changed_after_start"]),
                      "consumed_drift": len(consumed_drift), "records_changed_vs_parent": len(rec_changed),
                      "other_changed_vs_parent": len(other_changed), "maxrss": res["reader"]["maxrss_bytes"]}))


if __name__ == "__main__":
    main()
