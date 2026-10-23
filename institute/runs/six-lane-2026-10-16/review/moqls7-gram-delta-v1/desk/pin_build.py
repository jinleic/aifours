#!/usr/bin/env python3
"""moqls7-gram-delta-v1 pin builder (static copy + hash only; no solver/encoder/compiler/network).
Copies regular text/evidence files (never FIFOs, never CNFs > 64 KiB, never large SAT-model logs) into pin/,
exclusive-create only, verifies copy hash == source hash and source mtime unchanged, and writes pin/MANIFEST.json.
Usage (cwd = desk root moqls7-gram-delta-v1): /usr/bin/python3 -B desk/pin_build.py
"""
import datetime, hashlib, json, os, stat, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # desk root
R = os.path.dirname(HERE)
P = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
PIN = os.path.join(HERE, "pin")
MAX_TOTAL = 10 * 1000 * 1000

def now():
    return datetime.datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

LANE_FILES = [
    "README.md",
    "review/GRAM-ENCODING.r1.md", "review/GRAM-ENCODING.r2.md", "review/LEMMAS.md",
    "review/REVIEW-CORRECTIONS.r2.json", "review/K2-THEOREM.r1.md", "review/K2-THEOREM.r2.md",
    "review/K2-REVIEW-DELTA.r2.json", "review/K2-CLASSIFICATION-SOURCE.r1.json",
    "review/K1-THEOREM.r1.md", "review/K1-THEOREM.r2.md", "review/K1-THEOREM.r3.md",
    "review/AMENDMENT-1.r1.md", "review/AMENDMENT-2.r1.md",
    "review/CERTIFY-DRIVER-DELTA.r2.json", "review/CERTIFY-DRIVER-DELTA.r3.json", "review/CERTIFY-DRIVER-DELTA.r4.json",
    "review/K3-CERTIFICATION-DRIVER-DELTA.r2.json",
    "code/gram_enc.py", "code/gram_encB.py", "code/gram_certify.py", "code/gram_certify_r2.py",
    "code/gram_certify_r3.py", "code/gram_certify_r4.py", "code/k2_classes.py", "code/k2_classesB.py",
    "code/gram_cert_summary.py", "code/gram_review_controls.py", "code/gram_controls.py", "code/gram_controlsB.py",
    "code/proof_stream.py", "code/proof_stream_controls.py", "code/k3_cube_certify_r2.py", "code/ls_classes.c",
    "evidence/ls7_main_classes.txt", "evidence/LOG.md",
    "evidence/gram/k2A_cert_summary_r4.json", "evidence/gram/k2B_cert_summary_r4.json",
    "evidence/gram/gram_controlsA_frozen.json", "evidence/gram/gram_controlsB_frozen.json",
    "evidence/gram/controls_code_sha256.txt",
    "sources/2607.12933v2.layout.txt", "sources/1406.3681v2.layout.txt",
]
LANE_DIRS = {   # directory -> admitted regular-file suffixes (FIFOs and CNFs/SAT logs excluded by rule below)
    "evidence/gram/cert_r4": (".json", ".checker.log", ".solver.log"),
    "evidence/gram/cert_r2": (".json", ".checker.log", ".solver.log"),
    "evidence/gram/cert_r3": (".json", ".checker.log", ".solver.log"),
    "evidence/gram/review_controls_r1": (".json",),
    "evidence/gram/transport_controls_r1": (".cnf", ".log", ".jsonl", ".json"),
    "evidence/gram/transport_controls_r2": (".cnf", ".log", ".jsonl", ".json", ".drat"),
}
PARENT_FILES = [
    "moqls7-gram-review-codex-v1.note.md", "moqls7-gram-review-codex-v1.receipt.json",
    "moqls7-gram-review-claude-v2.note.md", "moqls7-gram-review-claude-v2.receipt.json",
    "moqls7-gram-review-claude-v1.receipt.json",
    "moqls7-gram-review-inputs-v2/manifest.json",
    "moqls7-k1-parent-verdict.md",
    "moqls7-ls147-parent-v1/REPORT.md", "moqls7-ls147-parent-v1/result.json",
]
SMALL = 64 * 1024   # per-file cap for directory sweeps (excludes CNFs and SAT-model logs)


def text_stats(b):
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        return {"utf8": False}
    return {"utf8": True, "lf_count": t.count("\n"), "ends_with_lf": t.endswith("\n"),
            "split_elements": len(t.split("\n")), "carriage_returns": t.count("\r"), "form_feeds": t.count("\f")}


def copy_one(src, dst_rel, origin, excluded):
    st = os.lstat(src)
    if not stat.S_ISREG(st.st_mode):
        excluded.append({"source": src, "reason": "not a regular file (FIFO/symlink/other); never opened"})
        return None
    with open(src, "rb") as f:
        data = f.read()
    h0 = hashlib.sha256(data).hexdigest()
    dst = os.path.join(PIN, dst_rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)   # only below the fresh pin/ root
    with open(dst, "xb") as f:
        f.write(data)
    st2 = os.lstat(src)
    rec = {"pin_path": dst_rel, "origin": origin, "source": src, "bytes": len(data), "sha256": h0,
           "source_mtime_pt": datetime.datetime.fromtimestamp(st.st_mtime, ZoneInfo("America/Los_Angeles")).isoformat(),
           "copied_at_pt": now(), "copy_sha256_equal": sha(dst) == h0 == sha(src),
           "source_mtime_unchanged": st.st_mtime_ns == st2.st_mtime_ns}
    rec.update(text_stats(data))
    return rec


def main():
    os.mkdir(PIN)
    started = now()
    files, excluded = [], []
    for rel in LANE_FILES:
        r = copy_one(os.path.join(P, rel), os.path.join("lane", rel), "lane", excluded)
        if r: files.append(r)
    for d, suffixes in LANE_DIRS.items():
        for name in sorted(os.listdir(os.path.join(P, d))):
            src = os.path.join(P, d, name)
            st = os.lstat(src)
            if not stat.S_ISREG(st.st_mode):
                excluded.append({"source": src, "reason": "not a regular file (FIFO); never opened"})
                continue
            if not name.endswith(suffixes):
                excluded.append({"source": src, "reason": "suffix not admitted (CNF/SAT-model log/input not copied; hash recorded in evidence digest)"})
                continue
            if st.st_size > SMALL:
                excluded.append({"source": src, "reason": "size %d > %d; hash recorded in evidence digest" % (st.st_size, SMALL)})
                continue
            r = copy_one(src, os.path.join("lane", d, name), "lane", excluded)
            if r: files.append(r)
    for rel in PARENT_FILES:
        r = copy_one(os.path.join(R, rel), os.path.join("parent", rel), "parent", excluded)
        if r: files.append(r)
    total = sum(f["bytes"] for f in files)
    assert total <= MAX_TOTAL, total
    assert all(f["copy_sha256_equal"] and f["source_mtime_unchanged"] for f in files)
    canon = os.path.join(P, "review/GRAM-ENCODING.md")
    manifest = {"manifest": "moqls7-gram-delta-v1/pin", "created_by": "M7GramDeltaDesk (parent-side delta desk, sub-agent of Main)",
                "pin_started_at_pt": started, "pin_finished_at_pt": now(),
                "lane_root": P, "parent_root": R,
                "line_numbering": "line N = element N (1-based) of text.split('\\n'). A file ending in LF has split_elements = lf_count + 1; its last element is empty and is never a citation target.",
                "builder_sha256": sha(os.path.abspath(__file__)),
                "total_bytes": total, "file_count": len(files), "files": files,
                "not_copied": excluded,
                "unversioned_canonical_alias": {"path": "review/GRAM-ENCODING.md", "sha256": sha(canon),
                                                 "equals_r2": sha(canon) == sha(os.path.join(P, "review/GRAM-ENCODING.r2.md"))}}
    with open(os.path.join(PIN, "MANIFEST.json"), "x") as f:
        json.dump(manifest, f, indent=1)
        f.write("\n")
    print(json.dumps({"files": len(files), "bytes": total, "not_copied": len(excluded), "manifest_sha256": sha(os.path.join(PIN, "MANIFEST.json"))}))


if __name__ == "__main__":
    main()
