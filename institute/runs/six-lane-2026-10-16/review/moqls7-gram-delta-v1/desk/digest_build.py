#!/usr/bin/env python3
"""moqls7-gram-delta-v1 desk digests: static reads, SHA-256, byte scans and exact text diffs only.
No solver, encoder, checker, compiler, network or lane write. Output: pin/desk-digests/ (exclusive create).
Usage (cwd = desk root): /usr/bin/python3 -B desk/digest_build.py
"""
import datetime, difflib, hashlib, json, os, re, stat
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.dirname(HERE)
P = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
PIN = os.path.join(HERE, "pin")
OUT = os.path.join(PIN, "desk-digests")
OLD = os.path.join(R, "moqls7-gram-review-inputs-v2")
TZ = ZoneInfo("America/Los_Angeles")
EXPECTED_PINS = {
    "gram_enc.py": "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833",
    "gram_encB.py": "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
    "gram_certify_r4.py": "ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a",
    "k2_classes.py": "b49099e40c31505a163204b330c89bbfddc0fcf0df45170d567ff34a0070b891",
    "classfile": "898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158",
    "drat-trim": "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4",
    "drat-trim.c": "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee",
}


def now():
    return datetime.datetime.now(TZ).isoformat()


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def regular(path):
    return stat.S_ISREG(os.lstat(path).st_mode)


def ts(path):
    st = os.lstat(path)
    out = {"mtime_pt": datetime.datetime.fromtimestamp(st.st_mtime, TZ).isoformat()}
    if hasattr(st, "st_birthtime"):
        out["birthtime_pt"] = datetime.datetime.fromtimestamp(st.st_birthtime, TZ).isoformat()
    return out


def put(name, obj):
    path = os.path.join(OUT, name)
    with open(path, "x") as f:
        if isinstance(obj, str):
            f.write(obj)
        else:
            json.dump(obj, f, indent=1)
            f.write("\n")
    return path


# ---------- 1. exact unified diffs, verified by re-application ----------
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def apply_udiff(old, diff):
    out, i, k = [], 0, 0
    while k < len(diff) and not diff[k].startswith("@@"):
        k += 1
    while k < len(diff):
        m = HUNK.match(diff[k]); k += 1
        s, l = int(m.group(1)), int(m.group(2) if m.group(2) is not None else 1)
        start = s if l == 0 else s - 1
        out.extend(old[i:start]); i = start
        while k < len(diff) and not diff[k].startswith("@@"):
            line = diff[k]; k += 1
            tag, body = line[0], line[1:]
            if tag == " ":
                assert old[i] == body; out.append(body); i += 1
            elif tag == "-":
                assert old[i] == body; i += 1
            elif tag == "+":
                out.append(body)
            else:
                raise ValueError(line)
    out.extend(old[i:])
    return out


DIFFS = [("review/GRAM-ENCODING.r1.md", "review/GRAM-ENCODING.r2.md"),
         ("review/K2-THEOREM.r1.md", "review/K2-THEOREM.r2.md"),
         ("code/gram_certify.py", "code/gram_certify_r2.py"),
         ("code/gram_certify_r2.py", "code/gram_certify_r3.py"),
         ("code/gram_certify_r3.py", "code/gram_certify_r4.py"),
         ("code/gram_certify.py", "code/gram_certify_r4.py")]


def diffs():
    recs = []
    for a, b in DIFFS:
        ta = open(os.path.join(PIN, "lane", a)).read(); tb = open(os.path.join(PIN, "lane", b)).read()
        assert ta.endswith("\n") and tb.endswith("\n")
        la, lb = ta.splitlines(True), tb.splitlines(True)
        d = list(difflib.unified_diff(la, lb, fromfile=a, tofile=b, n=3))
        assert "".join(apply_udiff(la, d)) == tb
        name = "diff__" + a.replace("/", "_") + "__to__" + b.replace("/", "_") + ".diff"
        path = put(name, "".join(d))
        sm = difflib.SequenceMatcher(None, la, lb, autojunk=False)
        recs.append({"from": a, "from_sha256": sha(os.path.join(PIN, "lane", a)), "to": b,
                     "to_sha256": sha(os.path.join(PIN, "lane", b)), "diff": name, "diff_sha256": sha(path),
                     "context_lines": 3, "reapplication_reproduces_target_exactly": True,
                     "old_lines": len(la), "new_lines": len(lb),
                     "unchanged_lines": sum(x.size for x in sm.get_matching_blocks()),
                     "opcodes": [[t, i1 + 1, i2, j1 + 1, j2] for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal"]})
    return recs


# ---------- 2. old parent manifest LF erratum + citation-line confirmation ----------
ABBR = {"AMENDMENT": "review/AMENDMENT-1.r1.md", "README": "README.md", "GRAM": "review/GRAM-ENCODING.r1.md"}
EXPL = re.compile(r"`?((?:review|code|explore|evidence|sources)/[A-Za-z0-9_.\-/]+|manifest\.json|README\.md|"
                  r"AMENDMENT|README|GRAM):(\d+)`?(?:\s*[-\u2013]\s*`?:?(\d+))?")
BARE = re.compile(r"(?<![\w/.`:\-])`?:(\d+)`?(?:\s*[-\u2013]\s*(\d+))?")


def old_text(rel):
    return open(os.path.join(OLD, rel), encoding="utf-8").read()


def lf_erratum():
    om = json.load(open(os.path.join(OLD, "manifest.json")))
    rows = []
    for e in om["files"]:
        path = os.path.join(OLD, e["path"])
        t = open(path, encoding="utf-8").read()
        n_split = len(t.split("\n"))
        rows.append({"path": e["path"], "sha256_still_equal": sha(path) == e["sha256"], "lf_count_recorded": e["lf_count"],
                     "lf_count_actual": t.count("\n"), "ends_with_lf": t.endswith("\n"),
                     "lines_split_LF_recorded": e["lines_split_LF"], "len_text_split_LF": n_split,
                     "erratum": e["lines_split_LF"] == n_split - 1,
                     "corrected_lines_split_LF": n_split,
                     "last_nonempty_line": max(i + 1 for i, s in enumerate(t.split("\n")) if s.strip())})
    return om, rows


def citations(om_rows):
    files = {r["path"]: old_text(r["path"]).split("\n") for r in om_rows}
    files["manifest.json"] = old_text("manifest.json").split("\n")
    lfc = {k: (len(v) - 1 if v and v[-1] == "" else len(v)) for k, v in files.items()}
    notes = ["moqls7-gram-review-codex-v1.note.md", "moqls7-gram-review-claude-v2.note.md"]
    out = []
    for note in notes:
        last = None
        for ln, line in enumerate(open(os.path.join(R, note), encoding="utf-8").read().split("\n"), 1):
            spans = []
            for m in EXPL.finditer(line):
                f = ABBR.get(m.group(1), m.group(1)); last = f
                spans.append((m.start(), m.end()))
                out.append({"note": note, "note_line": ln, "file": f, "from": int(m.group(2)),
                            "to": int(m.group(3)) if m.group(3) else int(m.group(2)), "kind": "explicit"})
            for m in BARE.finditer(line):
                if any(a <= m.start() < b for a, b in spans) or last is None:
                    continue
                out.append({"note": note, "note_line": ln, "file": last, "from": int(m.group(1)),
                            "to": int(m.group(2)) if m.group(2) else int(m.group(1)), "kind": "bare-resolved-to-last-explicit-file (heuristic)"})
    for c in out:
        lines = files.get(c["file"])
        if lines is None:
            c["status"] = "file not in old snapshot manifest (not checkable)"; continue
        a, b = c["from"], max(c["from"], c["to"])
        c["in_range_1_to_lf_count"] = 1 <= a <= b <= lfc[c["file"]]
        c["targets_extra_trailing_element"] = b == lfc[c["file"]] + 1
        c["first_line_nonempty"] = 1 <= a <= len(lines) and bool(lines[a - 1].strip())
        c["first_line_text"] = lines[a - 1][:160] if 1 <= a <= len(lines) else None
    return out


# ---------- 3. K2 r4 production receipts: per-instance binding table ----------
def cert_r4():
    classes = [l.split() for l in open(os.path.join(P, "evidence/ls7_main_classes.txt")) if l.strip()]
    assert len(classes) == 147 and all(len(c) == 3 and len(c[0]) == 36 for c in classes)
    table, agg = [], {}
    for enc, solver in (("A", "cadical"), ("B", "kissat")):
        summ = json.load(open(os.path.join(P, "evidence/gram/k2%s_cert_summary_r4.json" % enc)))
        assert summ["pins"] == EXPECTED_PINS
        bad, starts, ends, cnfs = [], [], [], set()
        for row in summ["rows"]:
            i = row["class"]; label = "k2%s_%d" % (enc, i)
            d = os.path.join(P, "evidence/gram/cert_r4")
            rp, sp, cp = (os.path.join(d, label + s) for s in (".json", ".solver.log", ".checker.log"))
            r = json.load(open(rp))
            cl = open(cp, "rb").read().decode("utf-8", "replace").replace("\r", "\n").splitlines()
            status = [s.strip() for s in cl if s.strip().startswith("s ")]
            want_cmd0 = (["cadical", "-q", "-t", "1800"] if enc == "A" else ["kissat", "-q", "-f", "--time=1800"])
            checks = {
                "receipt_sha256_matches_summary": sha(rp) == row["receipt_sha256"],
                "instance_label": r["instance"] == "k2%s:%d" % (enc, i),
                "verified_unsat_rc20_rc0_no_stop": r["verified_unsat"] is True and r["solver_rc"] == 20 and r["checker_rc"] == 0 and r["safety_stop_reason"] is None,
                "status_lines_exact": r["checker_status_lines"] == ["s VERIFIED"] and status == ["s VERIFIED"],
                "pins_expected": r["pins"] == EXPECTED_PINS,
                "solver_log_sha256": sha(sp) == r["solver_log_sha256"],
                "checker_log_sha256": sha(cp) == r["checker_log_sha256"] == row["checker_log_sha256"],
                "cnf_sha256_matches_summary": r["cnf_sha256"] == row["cnf_sha256"],
                "solver_command_shape": r["solver_command"][:4] == want_cmd0 and r["solver_command"][4].endswith("explore/scratch/cert_r4_current.cnf") and r["solver_command"][5].endswith("cert_r4/%s.drat.fifo" % label),
                "caps_1800_3600": r["solver_seconds"] == 1800 and r["checker_seconds"] == 3600,
                "solver_log_says_unsat": open(sp).read().strip() == "s UNSATISFIABLE",
            }
            ok = all(checks.values())
            if not ok:
                bad.append({"label": label, "failed": [k for k, v in checks.items() if not v]})
            starts.append(r["started_at"]); ends.append(r["finished_at"]); cnfs.add(r["cnf_sha256"])
            table.append({"encoder": enc, "class": i, "class_key": classes[i][0], "claimed_reduced": int(classes[i][1]),
                          "claimed_par": int(classes[i][2]), "receipt": "cert_r4/%s.json" % label,
                          "receipt_sha256": row["receipt_sha256"], "cnf_sha256": r["cnf_sha256"],
                          "solver_log_sha256": r["solver_log_sha256"], "checker_log_sha256": r["checker_log_sha256"],
                          "started_at": r["started_at"], "finished_at": r["finished_at"], "all_static_checks_ok": ok})
        assert sorted(row["class"] for row in summ["rows"]) == list(range(147))
        agg[enc] = {"summary": "evidence/gram/k2%s_cert_summary_r4.json" % enc,
                    "summary_sha256": sha(os.path.join(P, "evidence/gram/k2%s_cert_summary_r4.json" % enc)),
                    "receipts": len(summ["rows"]), "indices_0_to_146_exact": True, "distinct_cnf_sha256": len(cnfs),
                    "failed_static_checks": bad, "first_start": min(starts), "last_finish": max(ends),
                    "pins": summ["pins"]}
    return table, agg


# ---------- 4. review_controls_r1: underlying-file hashes and byte-level CNF form ----------
def cnf_bytes_check(path):
    b = open(path, "rb").read()
    head, _, body = b.partition(b"\n")
    hp = head.split()
    nv, nc = int(hp[2]), int(hp[3])
    lines = body.split(b"\n")
    if lines and lines[-1] == b"":
        lines = lines[:-1]
    return {"bytes": len(b), "header": head.decode(), "vars": nv, "clauses_header": nc, "clause_lines": len(lines),
            "header_count_matches": nc == len(lines), "contains_None": b"None" in b,
            "empty_clause_line": any(l.strip() == b"0" for l in lines[:1]) or (b"\n0\n" in body) or body.startswith(b"0\n"),
            "every_line_ends_with_0": all(l.endswith(b" 0") or l == b"0" for l in lines)}


def review_controls():
    d = os.path.join(P, "evidence/gram/review_controls_r1")
    summ = json.load(open(os.path.join(d, "summary.json")))
    out = []
    for rec in summ["records"]:
        base = os.path.join(d, rec["encoder"] + "_" + rec["name"])
        cnf, log, rj, fx = base + ".cnf", base + ".solver.log", base + ".json", os.path.join(d, rec["name"] + ".fix.json")
        Lp = os.path.join(d, rec["name"] + ".L.json")
        rcpt = json.load(open(rj))
        status = [l for l in open(log, errors="replace").read().splitlines() if l.startswith("s ")]
        row = {"encoder": rec["encoder"], "name": rec["name"], "expected": rec["expected"], "observed": rec["observed"],
               "solver_rc": rec["solver_rc"], "cnf_sha256_ok": sha(cnf) == rec["cnf_sha256"],
               "solver_log_sha256_ok": sha(log) == rec["solver_log_sha256"], "fix_sha256_ok": sha(fx) == rec["fix_sha256"],
               "per_case_receipt_equals_summary_record": rcpt == rec, "solver_status_lines": status,
               "status_consistent_with_rc": (rec["solver_rc"] == 10 and status == ["s SATISFIABLE"]) or (rec["solver_rc"] == 20 and status == ["s UNSATISFIABLE"]),
               "L_json": os.path.basename(Lp) if os.path.exists(Lp) else None,
               "L_sha256": sha(Lp) if os.path.exists(Lp) else None,
               "cnf_form": cnf_bytes_check(cnf), "files_timestamps": {"cnf": ts(cnf), "receipt": ts(rj)}}
        out.append(row)
    return summ, out


# ---------- 5. transport_controls_r2: hash bindings of the small retained files ----------
def transport():
    d = os.path.join(P, "evidence/gram/transport_controls_r2")
    summ = json.load(open(os.path.join(d, "summary.json")))
    hashes = {}
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if regular(p):
            hashes[name] = {"sha256": sha(p), "bytes": os.lstat(p).st_size, **ts(p)}
        else:
            hashes[name] = {"non_regular": "FIFO (never opened)"}
    found = []
    for c in summ["controls"]:
        for k, v in c.items():
            if k.endswith("sha256") and isinstance(v, str):
                match = [n for n, h in hashes.items() if h.get("sha256") == v]
                found.append({"control": c.get("control"), "solver": c.get("solver"), "field": k, "value": v, "matching_files": match})
    return summ, hashes, found


# ---------- 6. chronology ----------
def chronology(agg, rc_rows):
    lane = lambda rel: os.path.join(P, rel)
    ev = []
    def add(label, when, source):
        ev.append({"when_pt": when, "event": label, "source": source})
    om = json.load(open(os.path.join(OLD, "manifest.json")))
    add("old Gram review snapshot pinned (inputs-v2)", om["pin_started_at_pt"], "parent moqls7-gram-review-inputs-v2/manifest.json pin_started_at_pt")
    for rcpt in ("moqls7-gram-review-codex-v1.receipt.json", "moqls7-gram-review-claude-v1.receipt.json", "moqls7-gram-review-claude-v2.receipt.json"):
        r = json.load(open(os.path.join(R, rcpt)))
        add(rcpt.replace(".receipt.json", "") + " started", r["started_at_pt"], rcpt)
        add(rcpt.replace(".receipt.json", "") + " finished (" + r["status"] + ")", r["finished_at_pt"], rcpt)
    for rel in ("evidence/gram/controls_code_sha256.txt", "evidence/gram/gram_controlsA_frozen.json", "evidence/gram/gram_controlsB_frozen.json"):
        add("file written: " + rel, ts(lane(rel))["mtime_pt"], "mtime")
    for rel in ("review/CERTIFY-DRIVER-DELTA.r2.json", "review/CERTIFY-DRIVER-DELTA.r3.json", "review/CERTIFY-DRIVER-DELTA.r4.json"):
        add("driver delta frozen: " + rel, json.load(open(lane(rel)))["frozen_at"], rel + " frozen_at")
    for e in ("A", "B"):
        add("K2 producer certificates %s first start" % e, agg[e]["first_start"], "cert_r4 receipts")
        add("K2 producer certificates %s last finish" % e, agg[e]["last_finish"], "cert_r4 receipts")
        add("K2 %s inventory recorded" % e, json.load(open(lane("evidence/gram/k2%s_cert_summary_r4.json" % e)))["recorded_at"], "summary recorded_at")
    for rel in ("review/K2-THEOREM.r1.md", "review/LEMMAS.md", "review/K1-THEOREM.r3.md", "review/GRAM-ENCODING.r2.md", "review/GRAM-ENCODING.md", "review/K2-THEOREM.r2.md"):
        add("file written: " + rel, ts(lane(rel))["mtime_pt"], "mtime")
    for rel, key in (("review/K2-CLASSIFICATION-SOURCE.r1.json", "recorded_at"), ("review/REVIEW-CORRECTIONS.r2.json", "recorded_at"),
                     ("review/K2-REVIEW-DELTA.r2.json", "recorded_at"), ("review/K3-CERTIFICATION-DRIVER-DELTA.r2.json", "frozen_at")):
        add("recorded: " + rel, json.load(open(lane(rel)))[key], rel + " " + key)
    rc_times = sorted(r["files_timestamps"]["receipt"]["mtime_pt"] for r in rc_rows)
    add("26 matched review controls: first per-case receipt written", rc_times[0], "review_controls_r1 receipt mtimes")
    add("26 matched review controls: last per-case receipt written", rc_times[-1], "review_controls_r1 receipt mtimes")
    add("26 matched review controls summary recorded", json.load(open(lane("evidence/gram/review_controls_r1/summary.json")))["recorded_at"], "summary recorded_at")
    tr = json.load(open(lane("evidence/gram/transport_controls_r2/summary.json")))
    add("transport controls r2 first start", min(c["started_at"] for c in tr["controls"] if c.get("started_at")), "transport summary")
    add("transport controls r2 last finish", max(c["finished_at"] for c in tr["controls"] if c.get("finished_at")), "transport summary")
    add("rejected transport trial r1 (/dev/fd) files", ts(lane("evidence/gram/transport_controls_r1/cadical_UNSAT.checker.log"))["mtime_pt"], "mtime")
    ls = json.load(open(os.path.join(R, "moqls7-ls147-parent-v1/result.json")))
    add("parent LS147 result created", ls["created"], "moqls7-ls147-parent-v1/result.json created")
    ev.sort(key=lambda x: datetime.datetime.fromisoformat(x["when_pt"]))
    k2_last = max(datetime.datetime.fromisoformat(agg[e]["last_finish"]) for e in ("A", "B"))
    rc_first = datetime.datetime.fromisoformat(rc_times[0])
    k3d = datetime.datetime.fromisoformat(json.load(open(lane("review/K3-CERTIFICATION-DRIVER-DELTA.r2.json")))["frozen_at"])
    tr_last = datetime.datetime.fromisoformat(max(c["finished_at"] for c in tr["controls"] if c.get("finished_at")))
    codex_fin = datetime.datetime.fromisoformat(json.load(open(os.path.join(R, "moqls7-gram-review-codex-v1.receipt.json")))["finished_at_pt"])
    k2_first = min(datetime.datetime.fromisoformat(agg[e]["first_start"]) for e in ("A", "B"))
    derived = {"review_controls_first_receipt_after_last_K2_certificate_seconds": (rc_first - k2_last).total_seconds(),
               "transport_r2_last_finish_before_K3_driver_delta_r2_frozen_seconds": (k3d - tr_last).total_seconds(),
               "old_codex_note_returned_before_first_K2_certificate_seconds": (k2_first - codex_fin).total_seconds()}
    return ev, derived


def main():
    os.mkdir(OUT)
    started = now()
    d = diffs()
    om, err = lf_erratum()
    cites = citations(err)
    table, agg = cert_r4()
    rsumm, rc = review_controls()
    tsumm, thashes, tfound = transport()
    ev, derived = chronology(agg, rc)
    files = {}
    files["diffs.json"] = put("diffs.json", d)
    files["old-manifest-lf-erratum.json"] = put("old-manifest-lf-erratum.json", {
        "old_manifest": "parent moqls7-gram-review-inputs-v2/manifest.json (immutable; not rewritten)",
        "old_manifest_sha256": sha(os.path.join(OLD, "manifest.json")),
        "old_convention_text": om["line_numbering"],
        "correct_convention": "line N = element N of text.split('\\n'); for LF-terminated text len(text.split('\\n')) = lf_count + 1 (last element empty)",
        "rows": err, "erratum_rows": sum(r["erratum"] for r in err)})
    files["old-review-citation-lines.json"] = put("old-review-citation-lines.json", {
        "notes": ["moqls7-gram-review-codex-v1.note.md", "moqls7-gram-review-claude-v2.note.md"],
        "method": "regex extraction of path:N[-M] and bare :N (resolved to last explicit file; heuristic) against the immutable old snapshot",
        "citations": cites})
    files["k2-cert-r4-binding-table.json"] = put("k2-cert-r4-binding-table.json", {"aggregate": agg, "rows": table,
        "class_key_binding": "class_key = first field of the i-th nonempty line of evidence/ls7_main_classes.txt (driver parse rows[int(idx)][0])"})
    files["review-controls-r1-file-checks.json"] = put("review-controls-r1-file-checks.json", {
        "summary_sha256": sha(os.path.join(P, "evidence/gram/review_controls_r1/summary.json")),
        "summary_recorded_at": rsumm["recorded_at"], "summary_pins": rsumm["pins"], "rows": rc})
    files["transport-controls-r2-file-checks.json"] = put("transport-controls-r2-file-checks.json", {
        "summary_sha256": sha(os.path.join(P, "evidence/gram/transport_controls_r2/summary.json")),
        "files": thashes, "recorded_hash_fields": tfound})
    files["chronology.json"] = put("chronology.json", {"events": ev, "derived": derived})
    man = {"digest_builder_sha256": sha(os.path.abspath(__file__)), "started_at_pt": started, "finished_at_pt": now(),
           "files": {k: {"sha256": sha(v), "bytes": os.path.getsize(v)} for k, v in sorted(files.items())},
           "diff_files": {r["diff"]: r["diff_sha256"] for r in d}}
    put("DIGEST-MANIFEST.json", man)
    print(json.dumps({"diffs": len(d), "erratum_rows": sum(r["erratum"] for r in err), "citations": len(cites),
                      "k2_rows": len(table), "k2_failed": {e: len(agg[e]["failed_static_checks"]) for e in agg},
                      "review_controls": len(rc), "chronology_events": len(ev), "derived": derived}))


if __name__ == "__main__":
    main()
