#!/usr/bin/env python3
"""README E11f: write evidence/mcdsqs128-c21/receipt.json (exclusive create) from the retained E11 files:
hashes of inputs, sources, code, binary and outputs; checker, control and replay results; per-step
/usr/bin/time -l observations; bytes of new E11 data and host free disk.  Run from the lane root.
Usage: e11_receipt.py OUT.json"""
import hashlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402

EV = "evidence/mcdsqs128-c21"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def hashed(*paths):
    return {p: sha(p) for p in paths}


def timing(p):
    t = open(p).read()
    f = lambda rx: float(re.search(rx, t).group(1))  # noqa: E731
    return {"log": p, "real_s": f(r"([\d.]+) real"), "user_s": f(r"([\d.]+) user"), "sys_s": f(r"([\d.]+) sys"),
            "max_rss_bytes": int(f(r"(\d+)\s+maximum resident set size"))}


def tree_bytes(paths):
    n = files = 0
    for top in paths:
        if os.path.isfile(top):
            n += os.path.getsize(top)
            files += 1
            continue
        for d, _, fs in os.walk(top):
            for f in fs:
                n += os.path.getsize(os.path.join(d, f))
                files += 1
    return n, files


def main():
    out = sys.argv[1]
    cert = f"{EV}/mcdsqs128_c21.txt"
    py = json.load(open(f"{EV}/mcdsqs128_c21.py39-check.json"))
    gen = json.load(open(f"{EV}/mutations/mutation-results.json"))
    con = json.load(open(f"{EV}/construction_mutations/construction-mutation-results.json"))
    bic = json.load(open(f"{EV}/builder_input_controls/builder-input-control-results.json"))
    tr = json.load(open("runs/e11/appb_retranscription.json"))
    new_code = ["code/build_mcdsqs128.py", "code/e11_appb_retranscribe.py", "code/e11_builder_input_controls.py",
                "code/e11_receipt.py", "code/mcdsqs/e11_construction_mutations.py"]
    copied = ["code/mcdsqs/check_mcdsqs.py", "code/mcdsqs/check_mcdsqs.c", "code/mcdsqs/mutation_controls_mcdsqs.py"]
    new_paths = ["runs/e11", "sources/e11", EV, "sources/e11-mcdsqs128-frozen-plan.md", "code/bin/check_mcdsqs_c"] \
        + new_code + copied
    nbytes, nfiles = tree_bytes(new_paths)
    du = shutil.disk_usage(".")
    rec = {
        "object": "mcDSQS(128) by Tan-Zhou Construction 2.1 (lines 292-335) with (g, n, s) = (32, 4, 0)",
        "status": "CANDIDATE (worker checks only; parent verification pending)",
        "worker": "MathMcDsqs128 (consequence/reproducibility slice of the math-1 gcDCQS(32^4:0) slot)",
        "frozen_plan": {"path": "sources/e11-mcdsqs128-frozen-plan.md",
                        "sha256": sha("sources/e11-mcdsqs128-frozen-plan.md"),
                        "written": "2026-10-17 after 15:39:09 PDT, before any E11 computation"},
        "certificate": {"path": cert, "sha256": sha(cert), "bytes": os.path.getsize(cert), "points": py["v"],
                        "blocks": py["blocks"], "colours": py["colours"],
                        "derived_triples_per_point": py["derived_triples_per_point"],
                        "class_size_profile_every_point": "42^60 38 37 36^2",
                        "pinned": "2026-10-17 15:43:19 PDT by cp -n from runs/e11/build/mcdsqs128_c21.txt"},
        "minimality": "64 = chi'(127) by (1.1); independently, a partial parallel class on 127 points has <= 42 "
                      "triples and 63*42 = 2646 < 2667 derived triples, so no derived STS(127) has a 63-colouring",
        "inputs": {
            "gcdcqs": {"path": "evidence/gcdcqs32-c23/gcdcqs32_c23.txt",
                       "sha256": sha("evidence/gcdcqs32-c23/gcdcqs32_c23.txt"),
                       "status": "parent-verified gcDCQS(32^4:0) certificate (three routes, per assignment)"},
            "appendix_b_transcription": {
                "path": "sources/tz_appb_mcdsqs32.json", "sha256": sha("sources/tz_appb_mcdsqs32.json"),
                "e0_code": hashed("code/tz_appb_mcdsqs32.py"),
                "e0_controls": hashed(*sorted(os.path.join("controls/e0_appb_controls", f)
                                              for f in os.listdir("controls/e0_appb_controls"))),
                "e0_recheck_output": hashed("runs/e11/e0_recheck.json"),
                "e0_recheck": json.load(open("runs/e11/e0_recheck.json"))},
            "independent_retranscription": {
                "pdf": hashed("../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.pdf"),
                "pdftotext_used_by_e0": hashed("../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt"),
                "route_G_ghostscript_10.06.0_txtwrite_pp23-24": hashed("sources/e11/tz_p23-24_gs_txtwrite.txt"),
                "route_L_arxiv_eprint": {"url": "https://arxiv.org/e-print/2503.11934v1",
                                         "fetched": "2026-10-17 15:40:49 PDT (curl 8.7.1)",
                                         **hashed("sources/e11/arxiv-2503.11934v1-eprint.bin",
                                                  "sources/e11/arxiv-2503.11934v1-eprint.headers.txt",
                                                  "sources/e11/arxiv-2503.11934v1-mcDSQS-0314.tex")},
                "route_V_renders_pdftoppm_26.04.0": hashed("sources/e11/tz_page-23.png", "sources/e11/tz_page-24.png",
                                                           "sources/e11/tz_page23_crop600_underlines-23.png"),
                "comparison": {"code": hashed("code/e11_appb_retranscribe.py"),
                               "output": hashed("runs/e11/appb_retranscription.json"), "result": tr["result"],
                               "route_G": {k: tr["route_G"][k] for k in ("base_equal_E0", "parts_equal_E0")},
                               "route_L": {k: tr["route_L"][k] for k in ("base_equal_E0", "parts_equal_E0",
                                                                          "single_underlined", "double_underlined")},
                               "underlines_match_orbits": tr["underlines_match_orbits"]},
                "route_V_observation": "lane visual check: 16 two-row part groups; single underline under "
                                       "{0,2,16,18}, double underline under {0,8,16,24}"}},
        "builder": {"path": "code/build_mcdsqs128.py", "sha256": sha("code/build_mcdsqs128.py"),
                    "modelled_on": "gcdcqs20-four-groups/code/build_mcdsqs80.py sha256 606321e8ff65a2fc47d3dace53e83f9edae25825f9cb3ac292ecaaddfe33352e",
                    "helpers": hashed("code/seed_tools.py", "code/lane_guard.py"),
                    "python": "/usr/bin/python3 3.9.6 (stdlib)",
                    "command": "PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 code/build_mcdsqs128.py "
                               "evidence/gcdcqs32-c23/gcdcqs32_c23.txt sources/tz_appb_mcdsqs32.json OUT.txt",
                    "internal_checks": ["1240 cyclic blocks form an SQS(32) (every 3-subset of Z32 once)",
                                        "at every a in Z32 the 16 parts + a are PPCs partitioning the derived STS(31) at a",
                                        "GCDCQS 128 4 32, COLOURS 64, HOLEFREE 16, groups 32i..32i+31, 80384 blocks",
                                        "exactly 16 classes avoiding G_i \\ {x} at every x (merged in index order)",
                                        "85344 blocks after adding the four local SQS(32)"],
                    "stdout": open("runs/e11/build/build.stdout.txt").read().strip()},
        "checkers": {
            "python": {"path": "code/mcdsqs/check_mcdsqs.py", "sha256": sha("code/mcdsqs/check_mcdsqs.py"),
                       "copy_of": "gcdcqs20-four-groups/code/mcdsqs/check_mcdsqs.py (cp -n, identical sha256)",
                       "interpreter": "/usr/bin/python3 3.9.6", "result": py["result"],
                       "triples_covered": py["triples_covered"], "output": hashed(f"{EV}/mcdsqs128_c21.py39-check.json")},
            "c": {"source": "code/mcdsqs/check_mcdsqs.c", "sha256": sha("code/mcdsqs/check_mcdsqs.c"),
                  "copy_of": "gcdcqs20-four-groups/code/mcdsqs/check_mcdsqs.c (cp -n, identical sha256); MAXV 128",
                  "binary": "code/bin/check_mcdsqs_c", "binary_sha256": sha("code/bin/check_mcdsqs_c"),
                  "compiler": "Apple clang 17.0.0 (clang-1700.3.19.1), clang -O2 (binary identical to the gcdcqs20 lane binary)",
                  "result": open(f"{EV}/mcdsqs128_c21.c-check.txt").read().strip()},
            "symmetry_assumed": "none (both checkers)"},
        "controls": {
            "generic_mutations": {"dir": f"{EV}/mutations", "script": hashed("code/mcdsqs/mutation_controls_mcdsqs.py"),
                                  "as_intended": gen["as_intended"], "total": gen["mutations"],
                                  "unmutated": [gen["unmutated_python"], gen["unmutated_c"]], "files_retained": True},
            "construction_mutations": {"dir": f"{EV}/construction_mutations",
                                       "script": hashed("code/mcdsqs/e11_construction_mutations.py"),
                                       "as_intended": con["as_intended"], "total": con["mutations"],
                                       "results": {k: [v["python"], v["c"]] for k, v in con["results"].items()},
                                       "files_retained": True},
            "builder_input_controls": {"dir": f"{EV}/builder_input_controls",
                                       "script": hashed("code/e11_builder_input_controls.py"),
                                       "as_intended": bic["as_intended"], "total": bic["controls"],
                                       "results": {k: v["error"] for k, v in bic["results"].items()},
                                       "files_retained": True}},
        "replays": {
            "from_pinned_inputs": {"output": "runs/e11/replay/mcdsqs128_c21_rebuild.txt",
                                   "sha256": sha("runs/e11/replay/mcdsqs128_c21_rebuild.txt")},
            "from_e10_full_chain_gcdcqs": {"gcdcqs_input": hashed("runs/e10/replay/from_replayed_ingredients.txt"),
                                           "output": "runs/e11/replay_fullchain/mcdsqs128_c21_from_e10_full_chain.txt",
                                           "sha256": sha("runs/e11/replay_fullchain/mcdsqs128_c21_from_e10_full_chain.txt")}},
        "consequence_note": hashed(f"{EV}/consequence-note.md"),
        "resources": {
            "steps": {"e0_recheck": timing("runs/e11/e0_recheck.time.txt"),
                      "retranscription": timing("runs/e11/appb_retranscription.time.txt"),
                      "build": timing("runs/e11/build/build.time.txt"),
                      "check_python": timing("runs/e11/build/py-check.time.txt"),
                      "check_c": timing("runs/e11/build/c-check.time.txt"),
                      "generic_mutations": timing("runs/e11/generic_mutations.time.txt"),
                      "construction_mutations": timing("runs/e11/construction_mutations.time.txt"),
                      "builder_input_controls": timing("runs/e11/builder_input_controls.time.txt"),
                      "replay": timing("runs/e11/replay/replay.time.txt"),
                      "replay_full_chain": timing("runs/e11/replay_fullchain/replay.time.txt")},
            "max_concurrent_processes": "<= 2 busy (each control script runs one checker child at a time)",
            "new_e11_data": {"bytes": nbytes, "files": nfiles, "paths": new_paths,
                             "note": "measured before this receipt was written"},
            "host_free_disk_bytes_at_receipt": du.free},
        "code_sha256": hashed(*new_code, *copied, "code/lane_guard.py", "code/seed_tools.py"),
        "claims": "correctness of the explicit mcDSQS(128) certificate only (two definition-first worker checkers, "
                  "no symmetry assumed); no novelty, priority, significance or gate claim; the family statement is "
                  "the source's conditional Corollary 2.6 (see consequence-note.md), not re-proved",
    }
    rec["replays"]["from_pinned_inputs"]["byte_identical"] = rec["replays"]["from_pinned_inputs"]["sha256"] == rec["certificate"]["sha256"] \
        and open("runs/e11/replay/mcdsqs128_c21_rebuild.txt", "rb").read() == open(cert, "rb").read()
    rec["replays"]["from_e10_full_chain_gcdcqs"]["byte_identical"] = \
        open("runs/e11/replay_fullchain/mcdsqs128_c21_from_e10_full_chain.txt", "rb").read() == open(cert, "rb").read()
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(out, "written;", "new E11 data", nbytes, "bytes in", nfiles, "files; free disk", du.free)


if __name__ == "__main__":
    main()
