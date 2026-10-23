#!/usr/bin/env python3
"""Matched fail-closed controls for m1_receipts_v1.py (evidence-PARSER checks, NOT proof mutations).

Fixtures are real lane records read read-only and copied into an in-memory overlay; each control changes exactly
one thing in the overlay (never on disk) and re-runs the production evaluate() for that single case. A control
passes only if the targeted route stops qualifying for the intended reason and the case state is the expected one.
Baselines (empty overlay) must be COVERED. Fixture cases are selected deterministically from the production output.
Usage: controls_v1.py PRODUCTION_OUTDIR OUTFILE
"""
import json
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import m1_receipts_v1 as M  # noqa: E402
from token_ro import ReadOnlyToken  # noqa: E402


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def pick(rows):
    cov = [r for r in rows if r["state"] == "COVERED"]

    def first(pred, key=lambda r: 0):
        c = sorted((r for r in cov if pred(r)), key=lambda r: (key(r), r["tag"]))
        return c[0]["tag"] if c else None

    ch = lambda r: r["chosen"]  # noqa: E731
    only = lambda r, s: "+".join(sorted(x["route"] for x in r["routes"] if x["ok"])) == s  # noqa: E731
    clean = lambda r: not ch(r).get("records_rejected_files") and not ch(r).get("overlap_indices")  # noqa: E731
    return {
        "split_T1_worker_ext": first(lambda r: ch(r)["route"] == "e" and set(ch(r)["chosen_tiers"]) == {"1"}
                                     and only(r, "e") and clean(r) and "worker-only" in ch(r)["ext"]["binding"]
                                     and set(ch(r)["chosen_kinds"]) == {"batch"},
                                     key=lambda r: ch(r)["records_chosen"]),
        "split_T2_ms06_s00150": first(lambda r: r["tag"] == "ms06_s00150" and ch(r)["route"] == "e"),
        "split_singles_R6": first(lambda r: ch(r)["route"] == "e" and set(ch(r)["chosen_kinds"]) == {"single"}
                                  and clean(r) and "parent-R6" in ch(r)["ext"]["binding"],
                                  key=lambda r: ch(r)["records_chosen"]),
        "split_a3": first(lambda r: ch(r)["route"] == "d" and set(ch(r)["chosen_kinds"]) == {"single"} and clean(r),
                          key=lambda r: ch(r)["records_chosen"]),
        "split_batch_r3": first(lambda r: ch(r)["route"] == "e" and "batch_r3" in ch(r)["chosen_kinds"],
                                key=lambda r: ch(r)["records_chosen"]),
        "direct_b_rev4_only": first(lambda r: ch(r)["route"] == "b" and ch(r)["rev"] == 4 and only(r, "b")),
        "direct_c5_T1_only": first(lambda r: ch(r)["route"] == "c5" and ch(r)["tier"] == 1 and only(r, "c5")),
        "direct_c5_rev5_only": first(lambda r: ch(r)["route"] == "c5" and ch(r)["rev"] == 5 and only(r, "c5")),
        "route_a_only": first(lambda r: ch(r)["route"] == "a" and only(r, "a")),
        "hard_plus_c5": first(lambda r: ch(r)["route"] == "c5" and only(r, "c5")
                              and any(x["route"] == "hard" for x in r["routes"])),
        "cell": "ms06_s00468",
    }


class Ctl:
    def __init__(self, lane_root, refs):
        self.root, self.refs, self.results = lane_root, refs, []
        self.base = M.Lane(lane_root)

    def rec(self, rel):
        return json.loads(self.base.read(rel))

    def run(self, tag, overlay, e0=None):
        lane = M.Lane(self.root, overlay)
        store, rows, e0r, problems, _ = M.evaluate(lane, self.refs, scope_tags={tag} if tag else set(),
                                                   e0_scope={e0} if e0 else set())
        return (rows[0] if rows else None), (e0r[0] if e0r else None), problems

    @staticmethod
    def text(row, route):
        out = []
        for x in row["routes"]:
            if x["route"] != route:
                continue
            out += x.get("reasons") or []
            out += list((x.get("rejected_reason_counts") or {}).keys())
            for r in x.get("records") or []:
                out += r.get("reasons") or []
        return " | ".join(out)

    def control(self, cid, what, tag, route, overlay, expect_state, expect_sub, expect_holes=None, e0=None,
                route_fails=None):
        t0 = now()
        row, g, problems = self.run(tag, overlay, e0)
        if e0:
            ok_state = (not g["ok"]) if expect_state != "COVERED" else g["ok"]
            text = " | ".join(g["reasons"])
            if expect_state == "SAT-CLAIM":
                ok_state = g["sat"] and not g["ok"]
            state, route_ok, holes = ("COVERED" if g["ok"] else ("SAT-CLAIM" if g["sat"] else "UNKNOWN")), g["ok"], None
        else:
            state = row["state"]
            rt = [x for x in row["routes"] if x["route"] == route]
            route_ok = any(x["ok"] for x in rt)
            text = " | ".join(row["reasons"] + [self.text(row, route)])
            holes = sum(x.get("hole_count") or 0 for x in rt)
            ok_state = state == expect_state
        rf = (expect_state != "COVERED") if route_fails is None else route_fails
        passed = ok_state and (expect_sub in text) and route_ok == (not rf) and not problems
        if expect_holes is not None:
            passed = passed and holes == expect_holes
        self.results.append({"id": cid, "what": what, "case": tag or e0, "route": route,
                             "overlay": {k: ("<deleted>" if v is None else "<mutated %d bytes>" % len(v))
                                         for k, v in overlay.items()},
                             "expected_state": expect_state, "expected_reason_substring": expect_sub,
                             "expected_holes": expect_holes, "observed_state": state, "observed_route_ok": route_ok,
                             "observed_holes": holes, "observed_reason_excerpt": text[:600], "problems": problems,
                             "pass": bool(passed), "started": t0, "ended": now()})

    def mut(self, rel, fn):
        r = self.rec(rel)
        fn(r)
        return {rel: json.dumps(r, indent=1).encode()}


def first_file(lane, d, prefix):
    return sorted(n for n in lane.listdir(d) if n.startswith(prefix) and n.endswith(".json")
                  and "_r" not in n and "_exact" not in n)


def main():
    prod, outfile = sys.argv[1], sys.argv[2]
    rows = [json.loads(l) for l in open(os.path.join(prod, "cases-A2.jsonl"))]
    fx = pick(rows)
    started = now()
    with ReadOnlyToken() as tok:
        tokinfo = {"name": tok.name, "acquired_at": tok.acquired_at, "waited_s": tok.waited_s}
        refs = M.load_refs()
        # Field-predicate controls run WITHOUT the parent snapshot hash check, so the intended field predicate (not
        # byte drift) must reject; the snapshot check itself has its own controls (Z01-Z03) with the snapshot on.
        C = Ctl(M.LANE_ROOT, refs[:4] + ({},))
        Z = Ctl(M.LANE_ROOT, refs)
        L = C.base
        # Baselines
        for k, tag in fx.items():
            if tag:
                route = {"split_T1_worker_ext": "e", "split_T2_ms06_s00150": "e", "split_singles_R6": "e",
                         "split_a3": "d", "split_batch_r3": "e", "direct_b_rev4_only": "b", "direct_c5_T1_only": "c5",
                         "direct_c5_rev5_only": "c5", "route_a_only": "a", "hard_plus_c5": "c5", "cell": "cell"}[k]
                C.control("B-" + k, "baseline, empty overlay", tag, route, {}, "COVERED", "")
        C.control("B-E0", "baseline E0 g000", None, "E0", {}, "COVERED", "", e0="g000")
        # ---- split T1 (rev11-15 staged batches, worker-only ext) ----
        t = fx["split_T1_worker_ext"]
        d = "cycle2/part/%s" % t
        b = first_file(L, d, "batch_")
        b0, b1 = d + "/" + b[0], d + "/" + b[1]
        lo, hi = [int(x) for x in b[0][6:-5].split("_")]
        C.control("S01", "drop ONE essential batch receipt", t, "e", {b0: None}, "UNKNOWN",
                  "placement indices not covered", expect_holes=hi - lo + 1)
        C.control("S02", "batch indices list shortened by one (batch bound)", t, "e",
                  C.mut(b0, lambda r: r["indices"].pop()), "UNKNOWN", "indices list != filename range",
                  expect_holes=hi - lo + 1)
        C.control("S03", "wrong case tag in one batch", t, "e", C.mut(b0, lambda r: r.update(tag="ms06_s99999")),
                  "UNKNOWN", "tag ")
        C.control("S04", "checker s-line keeps CR ('\\rs VERIFIED')", t, "e",
                  C.mut(b0, lambda r: r["drat_trim"].update(s_lines=["\rs VERIFIED"])), "UNKNOWN", "drat_trim.s_lines")
        C.control("S05", "checker s-line padded ('s VERIFIED ')", t, "e",
                  C.mut(b0, lambda r: r["drat_trim"].update(s_lines=["s VERIFIED "])), "UNKNOWN", "drat_trim.s_lines")
        C.control("S06", "contradictory s-lines (VERIFIED + TIMEOUT)", t, "e",
                  C.mut(b0, lambda r: r["drat_trim"].update(s_lines=["s VERIFIED", "s TIMEOUT"])), "UNKNOWN",
                  "drat_trim.s_lines")
        C.control("S07", "negative s-line with says_verified still True", t, "e",
                  C.mut(b0, lambda r: r["drat_trim"].update(s_lines=["s NOT VERIFIED"])), "UNKNOWN", "drat_trim.s_lines")
        C.control("S08", "drat-trim rc flipped to 1", t, "e", C.mut(b0, lambda r: r["drat_trim"].update(rc=1)),
                  "UNKNOWN", "drat_trim.rc")
        C.control("S09", "drat-trim stop flipped to term (not self-exit)", t, "e",
                  C.mut(b0, lambda r: r["drat_trim"].update(stop="term")), "UNKNOWN", "drat_trim.stop")
        C.control("S10", "solver stop flipped to term", t, "e", C.mut(b0, lambda r: r.update(solver_stop="term")),
                  "UNKNOWN", "solver_stop")
        C.control("S11", "solver rc flipped to 0 (status left UNSAT)", t, "e", C.mut(b0, lambda r: r.update(solver_rc=0)),
                  "UNKNOWN", "solver_rc")
        C.control("S12", "feed incomplete: replay.bytes = drat_bytes - 1", t, "e",
                  C.mut(b0, lambda r: r["replay"].update(bytes=r["drat_bytes"] - 1)), "UNKNOWN", "replay.bytes")
        C.control("S13", "feed hash mismatch: replay.sha256 altered", t, "e",
                  C.mut(b0, lambda r: r["replay"].update(sha256="0" * 64)), "UNKNOWN", "replay.sha256")
        C.control("S14", "replay_ok flipped False", t, "e", C.mut(b0, lambda r: r.update(replay_ok=False)), "UNKNOWN",
                  "replay_ok")
        C.control("S15", "reader_ok flipped False (compressed buffer reader)", t, "e",
                  C.mut(b0, lambda r: r.update(reader_ok=False)), "UNKNOWN", "reader_ok")
        C.control("S16", "aborted_by_sigterm flipped True", t, "e", C.mut(b0, lambda r: r.update(aborted_by_sigterm=True)),
                  "UNKNOWN", "aborted_by_sigterm")
        C.control("S17", "zbuf_bytes zero (empty compressed buffer)", t, "e", C.mut(b0, lambda r: r.update(zbuf_bytes=0)),
                  "UNKNOWN", "zbuf_bytes")
        C.control("S18", "retired revision 10 injected into a counted batch", t, "e",
                  C.mut(b0, lambda r: r.update(stream_check_revision=10)), "UNKNOWN", "retired revision 10")
        lrat = C.rec(b0)
        lrat.update(solver="cadical 3.0.1 -q -t 600 --lrat=true --binary=false; LRAT streamed to lrat-check",
                    stream_check_revision=4, kind="partbatch", index=b[0][:-5])
        lrat.pop("drat_trim", None)
        lrat["drat_trim_verified"] = None
        C.control("S19", "LRAT-only _r2 injected for a dropped batch", t, "e",
                  {b0: None, b0[:-5] + "_r2.json": json.dumps(lrat).encode()}, "UNKNOWN", "LRAT-only",
                  expect_holes=hi - lo + 1)
        C.control("S20", "SAT status in one batch", t, "e", C.mut(b0, lambda r: r.update(status="SAT")), "SAT-CLAIM",
                  "SAT claim")
        C.control("S21", "admission_denied injected", t, "e", C.mut(b0, lambda r: r.update(admission_denied="stop file")),
                  "UNKNOWN", "admission_denied")
        C.control("S22", "proof_cap_hit injected", t, "e", C.mut(b0, lambda r: r.update(proof_cap_hit="raw")), "UNKNOWN",
                  "proof_cap_hit")
        C.control("S23", "non-empty events", t, "e",
                  C.mut(b0, lambda r: r.update(events=[{"process": "drat-trim", "action": "SIGTERM"}])), "UNKNOWN", "events")
        C.control("S24", "proof-free: drat_bytes 0", t, "e", C.mut(b0, lambda r: r.update(drat_bytes=0)), "UNKNOWN",
                  "drat_bytes")
        C.control("S25", "checked flipped False only", t, "e", C.mut(b0, lambda r: r.update(checked=False)), "UNKNOWN",
                  "checked is not True")
        C.control("S26", "encoder label changed", t, "e", C.mut(b0, lambda r: r.update(encoder="encode_partq.py")),
                  "UNKNOWN", "encoder")
        n_e = json.loads(L.read(d + "/ext.json"))["num_full"]
        last = sorted(first_file(L, d, "batch_"))[-1]
        llo, lhi = [int(x) for x in last[6:-5].split("_")]

        def drop_last_placement(r):
            r["full"].pop()
            r["num_full"] -= 1

        def append_placement(r):
            r["full"].append(r["full"][-1])
            r["num_full"] += 1
        C.control("S27", "ext.json: drop ONE placement (list and num_full) in a worker-only list (last batch hi=%d, "
                  "n=%d)" % (lhi, n_e), t, "e", C.mut(d + "/ext.json", drop_last_placement), "UNKNOWN",
                  "outside the placement list")
        C.control("S28", "ext.json: num_full != list length", t, "e",
                  C.mut(d + "/ext.json", lambda r: r.update(num_full=r["num_full"] + 1)), "UNKNOWN",
                  "num_full does not equal stored list length")
        C.control("S29", "ext.json: source identity of another case", t, "e",
                  C.mut(d + "/ext.json", lambda r: r.update(source="ms06_s00001.json")), "UNKNOWN", "source identity")
        C.control("S30", "ext.json: one extra placement appended (denominator grows by one)", t, "e",
                  C.mut(d + "/ext.json", append_placement), "UNKNOWN", "1 placement indices not covered",
                  expect_holes=1)
        C.control("S31", "ext.json emptied (num_full 0): an empty list is never a generic 0/0 PASS", t, "e",
                  C.mut(d + "/ext.json", lambda r: r.update(full=[], num_full=0)), "UNKNOWN", "EMPTY-COVER")
        # ---- split singles with parent-R6 ext ----
        t = fx["split_singles_R6"]
        d = "cycle2/part/%s" % t
        fs = first_file(L, d, "f")
        f0 = d + "/" + fs[len(fs) // 2]
        i0 = int(fs[len(fs) // 2][1:6])
        C.control("P01", "drop ONE essential placement receipt (single)", t, "e", {f0: None}, "UNKNOWN",
                  "placement indices not covered", expect_holes=1)
        C.control("P02", "single sub_index != filename index", t, "e", C.mut(f0, lambda r: r.update(sub_index=i0 + 1)),
                  "UNKNOWN", "record index field(s) != filename index", expect_holes=1)
        C.control("P03", "non-canonical 6-digit filename for the same index", t, "e",
                  {f0: None, d + "/f%06d.json" % i0: L.read(f0)}, "UNKNOWN", "non-canonical filename", expect_holes=1)
        C.control("P04", "rev4 says_verified flipped False", t, "e",
                  C.mut(f0, lambda r: r["drat_trim"].update(says_verified=False)), "UNKNOWN", "says_verified")
        C.control("P05", "wrong CNF hash cannot hide: rev4 cnf_sha256 not hex", t, "e",
                  C.mut(f0, lambda r: r.update(cnf_sha256="x" * 64)), "UNKNOWN", "cnf_sha256 not 64-hex")
        C.control("P06", "ext.json one placement dropped in a parent-R6-bound list", t, "e",
                  C.mut(d + "/ext.json", lambda r: (r["full"].pop(0), r.update(num_full=r["num_full"] - 1))), "UNKNOWN",
                  "ext.json sha256 != parent placement reference")
        # ---- a3 ----
        t = fx["split_a3"]
        d = "cycle2/a3/%s" % t
        fs = first_file(L, d, "f")
        f0 = d + "/" + fs[0]
        C.control("A01", "a3 full_index mismatch", t, "d", C.mut(f0, lambda r: r.update(full_index=r["full_index"] + 7)),
                  "UNKNOWN", "record index field(s) != filename index", expect_holes=1)
        C.control("A02", "a3 record lacks required full_index field", t, "d", C.mut(f0, lambda r: r.pop("full_index")),
                  "UNKNOWN", "required index field 'full_index' missing", expect_holes=1)
        C.control("A03", "a3 batch-style indices injected into a single", t, "d",
                  C.mut(f0, lambda r: r.update(indices=[0, 1])), "UNKNOWN", "single record carries an indices list")
        # ---- batch _r3 precedence ----
        t = fx["split_batch_r3"]
        if t:
            d = "cycle2/part/%s" % t
            r3 = sorted(n for n in L.listdir(d) if n.endswith("_r3.json"))[0]
            r3p = d + "/" + r3
            lo, hi = [int(x) for x in r3[6:-8].split("_")]
            C.control("R01", "drop the _r3 that covers an UNKNOWN original batch", t, "e", {r3p: None}, "UNKNOWN",
                      "placement indices not covered", expect_holes=hi - lo + 1)
            C.control("R02", "_r3 CNF differs from original batch", t, "e",
                      C.mut(r3p, lambda r: r.update(cnf_sha256="1" * 64)), "UNKNOWN", "_r3 cnf_sha256/bytes != original")
            C.control("R03", "_r3 original batch record missing", t, "e", {d + "/" + r3[:-8] + ".json": None}, "UNKNOWN",
                      "_r3 has no readable original record")
            C.control("R04", "_r3 claims SAT", t, "e", C.mut(r3p, lambda r: r.update(status="SAT")), "SAT-CLAIM",
                      "SAT claim")
        # ---- direct routes ----
        t = fx["direct_b_rev4_only"]
        if t:
            p = "cycle2/proofstream/%s.json" % t
            C.control("D01", "route b: wrong CNF hash", t, "b", C.mut(p, lambda r: r.update(cnf_sha256="2" * 64)), "UNKNOWN",
                      "cnf_sha256 != parent R5 rebuild")
            C.control("D02", "route b: wrong case tag", t, "b", C.mut(p, lambda r: r.update(tag="ms08_s99999")), "UNKNOWN",
                      "tag ")
            C.control("D03", "route b: LRAT-only solver string", t, "b",
                      C.mut(p, lambda r: r.update(solver="cadical 3.0.1 -q --lrat=true; LRAT streamed to lrat-check")),
                      "UNKNOWN", "LRAT-only")
            C.control("D04", "route b: rev4 drat-trim rc missing", t, "b", C.mut(p, lambda r: r["drat_trim"].pop("rc")),
                      "UNKNOWN", "drat_trim.rc")
            C.control("D05", "route b: checker_interrupted True", t, "b",
                      C.mut(p, lambda r: r.update(checker_interrupted=True)), "UNKNOWN", "checker_interrupted")
            reformatted = {p: json.dumps(C.rec(p), indent=2).encode()}
            Z.control("Z00", "baseline with parent snapshot hash check on", t, "b", {}, "COVERED", "")
            Z.control("Z01", "field-identical byte reformat of a parent-snapshotted record", t, "b", reformatted,
                      "UNKNOWN", "record bytes changed since parent snapshot")
            p1 = "cases19skel/results/%s.json" % t
            Z.control("Z02", "field-identical byte reformat of the pass-1 record (row-level fail, route b intact)", t,
                      "b", {p1: json.dumps(C.rec(p1), indent=2).encode()}, "UNKNOWN",
                      "pass-1 record bytes changed since parent snapshot", route_fails=False)
        t = fx["split_singles_R6"]
        if t:
            d = "cycle2/part/%s" % t
            f0 = d + "/" + first_file(L, d, "f")[0]
            Z.control("Z03", "field-identical reformat of a snapshotted split record", t, "e",
                      {f0: json.dumps(C.rec(f0), indent=2).encode()}, "UNKNOWN",
                      "record bytes changed since parent snapshot", expect_holes=1)
        t = fx["direct_c5_rev5_only"]
        if t:
            p = "cycle2/hard5/%s.json" % t
            C.control("D06", "route c5 rev5: says_timeout True", t, "c5",
                      C.mut(p, lambda r: r["drat_trim"].update(says_timeout=True)), "UNKNOWN", "says_timeout")
            C.control("D07", "route c5 rev5: says_timeout field missing", t, "c5",
                      C.mut(p, lambda r: r["drat_trim"].pop("says_timeout")), "UNKNOWN", "says_timeout missing")
            C.control("D08", "route c5: encoder not encode_skel", t, "c5",
                      C.mut(p, lambda r: r.update(encoder="encode_partq.py")), "UNKNOWN", "encoder")
        t = fx["direct_c5_T1_only"]
        if t:
            p = "cycle2/hard5/%s.json" % t
            C.control("D09", "route c5 T1: replay.ok False", t, "c5", C.mut(p, lambda r: r["replay"].update(ok=False)),
                      "UNKNOWN", "replay.ok")
            C.control("D10", "route c5 T1: cnf_bytes off by one", t, "c5", C.mut(p, lambda r: r.update(cnf_bytes=r["cnf_bytes"] + 1)),
                      "UNKNOWN", "cnf_bytes != parent R5 rebuild")
            C.control("D11", "route c5 T1: s_lines CR kept", t, "c5",
                      C.mut(p, lambda r: r["drat_trim"].update(s_lines=["\rs VERIFIED"])), "UNKNOWN", "drat_trim.s_lines")
        t = fx["route_a_only"]
        if t:
            p = "cases19skel/proofcheck/%s.json" % t
            C.control("D12", "route a: drat_trim_verified False", t, "a",
                      C.mut(p, lambda r: r.update(drat_trim_verified=False)), "UNKNOWN", "drat_trim_verified")
            C.control("D13", "route a: kissat_rc missing (not read as PASS)", t, "a", C.mut(p, lambda r: r.pop("kissat_rc")),
                      "UNKNOWN", "kissat_rc")
            C.control("D14", "route a: negative s-line in retained tail", t, "a",
                      C.mut(p, lambda r: r.update(drat_trim_tail=["s NOT VERIFIED", "c verification time: 1 seconds"])),
                      "UNKNOWN", "contradicts")
            C.control("D15", "route a: wrong CNF hash", t, "a", C.mut(p, lambda r: r.update(cnf_sha256="3" * 64)), "UNKNOWN",
                      "cnf_sha256 != parent R5 rebuild")
            C.control("D16", "route a: blank tail (no verification-time line)", t, "a",
                      C.mut(p, lambda r: r.update(drat_trim_tail=[""])), "UNKNOWN", "verification-time")
        t = fx["hard_plus_c5"]
        if t:
            C.control("D17", "only the LRAT-only cycle2/hard record left (hard5 removed)", t, "hard",
                      {"cycle2/hard5/%s.json" % t: None}, "UNKNOWN", "never counted")
        # ---- s00468 six-unit cover ----
        t, d = "ms06_s00468", "cycle2/cell-cover/ms06_s00468/r08_c06"
        C.control("X01", "drop ONE cube symbol (s03)", t, "cell", {d + "/s03.json": None}, "UNKNOWN",
                  "unit subcases not qualifying: [3]")
        C.control("X02", "duplicate symbol (s02 claims symbol 3)", t, "cell", C.mut(d + "/s02.json", lambda r: r.update(symbol=3)),
                  "UNKNOWN", "field symbol")
        C.control("X03", "wrong subcase CNF hash (s01)", t, "cell", C.mut(d + "/s01.json", lambda r: r.update(cnf_sha256="4" * 64)),
                  "UNKNOWN", "field cnf_sha256")
        C.control("X04", "wrong base CNF hash (s05)", t, "cell",
                  C.mut(d + "/s05.json", lambda r: r.update(base_cnf_sha256="5" * 64)), "UNKNOWN", "field base_cnf_sha256")
        C.control("X05", "wrong unit literal (s00)", t, "cell", C.mut(d + "/s00.json", lambda r: r.update(unit_literal=427)),
                  "UNKNOWN", "field unit_literal")
        C.control("X06", "extra unit record s06 present", t, "cell", {d + "/s06.json": L.read(d + "/s05.json")}, "UNKNOWN",
                  "unexpected unit records")
        C.control("X07", "s04 revision outside frozen set", t, "cell",
                  C.mut(d + "/s04.json", lambda r: r.update(stream_check_revision=12)), "UNKNOWN", "frozen cell-cover set")
        C.control("X08", "stale deferred record claims UNSAT", t, "cell",
                  C.mut(d + "/" + [n for n in L.listdir(d) if n.startswith("deferred")][0], lambda r: r.update(status="UNSAT")),
                  "UNKNOWN", "not an UNKNOWN stop record")
        C.control("X09", "contract unit literals altered", t, "cell",
                  C.mut(M.CONTRACT[0], lambda r: r.update(unit_literals_by_symbol=[421, 422, 423, 424, 425, 427])),
                  "UNKNOWN", "contract fields differ")
        C.control("X10", "s03 checker rc flipped", t, "cell", C.mut(d + "/s03.json", lambda r: r["drat_trim"].update(rc=1)),
                  "UNKNOWN", "drat_trim.rc")
        # ---- E0 ----
        g = "g000"
        rp, cp = "cases19q0/results/%s.json" % g, "cases19q0/results/%s.check.json" % g
        C.control("E01", "E0 check record dropped", None, "E0", {cp: None}, "UNKNOWN", "check record missing", e0=g)
        C.control("E02", "E0 graph6 of another graph", None, "E0", C.mut(rp, lambda r: r.update(graph6="G?bvbw")), "UNKNOWN",
                  "graph6 != pinned index", e0=g)
        C.control("E03", "E0 drat-trim rc flipped", None, "E0", C.mut(cp, lambda r: r.update(drat_trim_rc=1)), "UNKNOWN",
                  "drat_trim_rc", e0=g)
        C.control("E04", "E0 tail negative verdict", None, "E0",
                  C.mut(cp, lambda r: r.update(drat_trim_tail=["s NOT VERIFIED", "", r["drat_trim_tail"][-1]])), "UNKNOWN",
                  "s VERIFIED", e0=g)
        C.control("E05", "E0 tail padded verdict", None, "E0",
                  C.mut(cp, lambda r: r.update(drat_trim_tail=["s VERIFIED ", "", r["drat_trim_tail"][-1]])), "UNKNOWN",
                  "exactly one exact 's VERIFIED'", e0=g)
        C.control("E06", "E0 CNF hash changed between solve and check", None, "E0",
                  C.mut(cp, lambda r: r.update(cnf_sha256_now="6" * 64)), "UNKNOWN", "CNF sha not consistent", e0=g)
        C.control("E07", "E0 SAT status", None, "E0", C.mut(rp, lambda r: r.update(status="SAT")), "SAT-CLAIM",
                  "solve status", e0=g)
    allr = C.results + Z.results
    res = {"title": "Matched fail-closed controls for m1_receipts_v1 (in-memory overlays of real records; parser "
                    "checks, NOT proof mutations; no lane file modified)",
           "reader_sha256": M.sha256_bytes(open(os.path.join(HERE, "m1_receipts_v1.py"), "rb").read()),
           "controls_sha256": M.sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
           "token": tokinfo, "started": started, "finished": now(), "fixtures": fx,
           "snapshot_check": "C* controls ran with the parent snapshot hash check disabled; Z* controls with it on",
           "count": len(allr), "passed": sum(1 for r in allr if r["pass"]),
           "all_pass": all(r["pass"] for r in allr), "controls": allr}
    with open(outfile, "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({k: res[k] for k in ("count", "passed", "all_pass", "started", "finished")} |
                     {"failed": [r["id"] for r in allr if not r["pass"]]}))


if __name__ == "__main__":
    main()
