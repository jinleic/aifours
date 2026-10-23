#!/usr/bin/env python3
"""Assemble receipt-v1.json for cfr27-parent-reproduce-v1 (owner Cfr27ParentReproduce). Usage: python3 -B assemble_receipt_v1.py
Reads only this folder's stage results, re-hashes every file here plus the in-place parent pins and lane originals,
and writes receipt-v1.json exclusively (the receipt cannot hash itself)."""
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
ROOT = REVIEW.parents[3]
RECEIPT = HERE / "receipt-v1.json"


def now():
    return datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d %H:%M:%S %Z")


def sha_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(p):
    return str(Path(p).relative_to(ROOT))


def load(p):
    return json.loads((HERE / p).read_bytes())


def main():
    if not sys.dont_write_bytecode:
        raise SystemExit("run with python3 -B")
    if RECEIPT.exists():
        raise SystemExit("receipt exists")
    pin, build, rep, mr, aud = (load("inputs/pin-result.json"), load("build-savetemps/build-result.json"),
                                load("replay-r1/replay-result.json"), load("model-recompile/model-recompile-result.json"),
                                load("audit-v1/audit-result.json"))
    files = []
    total = 0
    for p in sorted(HERE.rglob("*")):
        if p.is_file() and p != RECEIPT:
            b = p.stat().st_size
            total += b
            files.append({"path": rel(p), "bytes": b, "sha256": sha_file(p)})
    tmp_dirs = {rel(d): sorted(x.name for x in d.iterdir()) for d in sorted(HERE.rglob("tmp")) if d.is_dir()}
    pycache = [rel(p) for p in HERE.rglob("*") if p.name == "__pycache__" or p.suffix == ".pyc"]
    rehash_external = {}
    for e in pin["pins"]:
        rehash_external[e["source"]] = {"frozen_sha256": e["sha256"], "sha256_at_receipt": sha_file(ROOT / e["source"])}
    for path, s in pin["parent_pins_in_place"].items():
        rehash_external[path] = {"frozen_sha256": s, "sha256_at_receipt": sha_file(ROOT / path)}
    external_unchanged = all(v["frozen_sha256"] == v["sha256_at_receipt"] for v in rehash_external.values())
    step = build["steps"][0]
    producer_cases = []
    for c in rep["cases"]:
        r = c["run"]
        producer_cases.append({
            "case": c["case"], "argv": r["argv"], "cwd": r["cwd"], "env_overrides": r["env_overrides"],
            "native_seconds_argument": rep["native_seconds_argument"], "driver_wall_deadline_s": r["deadline_s"],
            "host_time_start": r["host_time_start"], "host_time_end": r["host_time_end"], "wall_s": r["wall_s"],
            "exit_code": r["rc"], "status_line": r["status_line"], "ru_maxrss_bytes": r["ru_maxrss_bytes"],
            "user_s": r["user_s"], "sys_s": r["sys_s"], "sigterm_sent": r["sigterm_sent"], "guard_trip": r["guard_trip"],
            "stdout": r["stdout"], "stdout_sha256": r["stdout_sha256"], "stderr": r["stderr"],
            "stderr_sha256": r["stderr_sha256"], "stderr_bytes": r["stderr_bytes"],
            "dmraw": c["dmraw"], "parent_pin": c["parent_pin"],
            "dmraw_byte_identical_to_parent_pin": c["dmraw_equals_parent_pin"],
            "dmraw_byte_identical_to_worker_dmraw": c["dmraw_equals_worker_dmraw"],
            "stdout_equal_worker_after_normalisation": c["stdout_normalised_equal_worker"],
            "stdout_normalisation": c["stdout_normalisation"],
            "printed_orbits": c["printed_orbits"], "printed_bases_equal_freeze": c["printed_bases_equal_freeze"],
            "verdict": c["verdict"]})
    cands = {}
    for name, a in aud["candidates"].items():
        cands[name] = {
            "group": {k: a["group"][k] for k in ("generators_from_freeze", "order", "structure", "element_orders",
                                                 "faithful_on_normalised_columns", "elements_mu_pi")},
            "model_crosscheck": a["model_crosscheck"],
            "orbit_expansion": {k: a["orbit_expansion"][k] for k in (
                "orbits", "sorted_orbit_sizes", "expected_sorted_orbit_sizes", "orbit_sizes_as_expected",
                "expanded_columns", "expanded_distinct", "expanded_multiset_equals_DM_columns", "zero_column_mode",
                "DM_columns_fixed_by_all_of_G")},
            "invariance": a["invariance"], "action_verdict": a["action_verdict"]}
    dm2cfr = {name: {"raw_dm_check_Z27": a["dm_check_Z27"], "canonical_text_roundtrip": a["canonical_text_roundtrip"],
                     **{k: a["dm_to_cfr"][k] for k in ("rule", "pinned_DM_row0_all_zero", "note", "regenerated",
                                                        "regenerated_sha256", "byte_identical_to_parent_pin",
                                                        "first_row_is_identity", "cfr_check_Z27", "converse")},
                     "dm_to_cfr_verdict": a["dm_to_cfr_verdict"]} for name, a in aud["candidates"].items()}
    producer_pass = rep["verdict"] == "PASS_RAW_DM_BYTE_IDENTICAL_BOTH"
    rec = {
        "receipt": "cfr27-parent-reproduce-v1", "owner": "Cfr27ParentReproduce", "host_time_assembled": now(),
        "scope": ("Post-result parent producer / group-action / DM->CFR equivalence audit of two pinned CFR(5,27) "
                  "candidates. No gate, novelty or priority claim."),
        "verdicts": {
            "producer_reproduction": ("PASS: rebuilt binary from frozen source; both deterministic models regenerate "
                                      "DM raws byte-identical to the parent pins A-DM.raw and B-DM.raw")
            if producer_pass else "NOT_PASS: " + rep["verdict"],
            "rebuilt_binary_equals_worker_binary": build["binary"]["equals_worker_binary"],
            "group_action_orbit_expansion": aud["verdicts"]["group_action_orbit_expansion"],
            "dm_to_cfr_regeneration": aud["verdicts"]["dm_to_cfr_regeneration"],
            "model_recompile_from_spec": mr["verdict"],
            "controls_all_as_expected": aud["verdicts"]["controls_all_as_expected"],
            "external_inputs_unchanged_at_receipt": external_unchanged},
        "non_claims": aud["non_claims"] + [
            "Producer success is not witness validity; raw validity was established by the parent definition-first "
            "checker and is re-confirmed here only as an extra independent definition check."],
        "rules_followed": {
            "exclusive_create": "os.mkdir without exist_ok and open mode 'x' for every new dir/file written by the "
                                "scripts; the three scripts were authored in the freshly created folder (the audit "
                                "script and this assembler received bug-fix edits before their first execution; no "
                                "script was edited after it ran)",
            "tmpdir": "TMPDIR set to a fresh directory inside this folder for every child",
            "tmp_dir_contents_at_receipt": tmp_dirs,
            "pycache": "python3 -B and PYTHONDONTWRITEBYTECODE=1",
            "pycache_or_pyc_files_in_folder_at_receipt": pycache,
            "children": "Popen + os.wait4 polling; SIGTERM at deadline or guard trip, bounded wait; never SIGKILL; "
                        "no subprocess.run(timeout); runs launched from a shell tool call without a deadline",
            "limits": {"busy_cpu": 1, "rss_cap_bytes": 2 * 1024 ** 3, "free_disk_floor_bytes": 12_000_000_000,
                       "native_seconds": 180, "new_data_cap_bytes": 256 * 1024 ** 2},
            "no_lane_writes": "claimant lane and parent pins only read; re-hash result in "
                              "verdicts.external_inputs_unchanged_at_receipt"},
        "disclosures": [
            "Native producer SECONDS argument 180 instead of the worker's 10800 (deterministic search; runs took ~9 s).",
            "Compile adds -save-temps=obj to the frozen flags (intermediates .i/.bc/.s/.o retained); the resulting "
            "binary is nevertheless byte-identical to the worker binary, so the planned two-step build was not run.",
            "Native output exclusivity: dmorbit_xc_v1.c emit() uses open(O_WRONLY|O_CREAT|O_EXCL, 0444) per the source "
            "text; output prefixes were additionally fresh and preflighted absent. stdout/stderr were opened 'x' by the "
            "driver.",
            "Global cache side effect: the per-user xcrun lookup cache %s changed (2514 -> 2670 bytes, mtime "
            "17:52:34 PDT) during the pin stage's toolchain-provenance queries (cc --version, xcrun --find clang, "
            "ld -v), which ran with TMPDIR inside this folder; attribution to those queries is [INFERENCE] from "
            "same-second timing. It was unchanged across the compile itself. Not reverted (no overwrite/deletion)."
            % build["xcrun_db_before"]["path"],
            "Stdout comparison with the worker logs is after normalising limit/time/output-path fields only; node "
            "counts, option counts, root items and printed orbit bases matched.",
            "The spec files' 'orbits' lists are placeholders that the producer ignores (spec note and source comment); "
            "the orbit structure reported here comes from the replay output and the independent expansion.",
            "No CFR(5,27) witness validity rests on the symmetry model or the producer."],
        "inputs": {"pinned_copies": pin["pins"], "parent_pins_in_place": pin["parent_pins_in_place"],
                   "freeze_consistency_checks": pin["freeze_consistency"],
                   "external_rehash_at_receipt": rehash_external},
        "toolchain": {"cc_version": pin["toolchain"]["cc_version"]["stdout_text"],
                      "xcrun_find_clang": pin["toolchain"]["xcrun_find_clang"]["stdout_text"].strip(),
                      "ld_version_stderr": pin["toolchain"]["ld_version"]["stderr_text"],
                      "sw_vers": pin["toolchain"]["sw_vers"]["stdout_text"],
                      "uname": pin["toolchain"]["uname"]["stdout_text"].strip(),
                      "sha256": pin["toolchain"]["sha256"], "python": pin["python"]},
        "compile": {"worker_command": build["worker_compile_command"], "argv": step["argv"], "cwd": step["cwd"],
                    "env_overrides": step["env_overrides"], "difference_from_worker": build["difference_from_worker"],
                    "exit_code": step["rc"], "stderr_text": step["stderr_text"], "wall_s": step["wall_s"],
                    "ru_maxrss_bytes": step["ru_maxrss_bytes"], "host_time_start": step["host_time_start"],
                    "source_sha256": build["source_sha256"], "binary": build["binary"],
                    "codesign_dvv": build["codesign"]["stderr_text"], "build_dir_inventory": build["inventory_after"],
                    "xcrun_db_before_compile": build["xcrun_db_before"],
                    "xcrun_db_after_compile": build["xcrun_db_after"]},
        "producer_replay": {"binary": rep["binary"], "binary_sha256": rep["binary_sha256"],
                            "seconds_disclosure": rep["seconds_disclosure"],
                            "native_output_mode_note": rep["native_output_mode_note"],
                            "term_wait_s": rep["term_wait_s"], "cases": producer_cases, "verdict": rep["verdict"]},
        "model_recompile": {"compiler": mr["compiler"], "compiler_sha256": mr["compiler_sha256"],
                            "cases": [{"tag": c["tag"], "argv": c["run"]["argv"], "exit_code": c["run"]["rc"],
                                       "model_sha256": c.get("model_sha256"),
                                       "equals_pinned_model": c["equals_pinned_model"]} for c in mr["cases"]],
                            "verdict": mr["verdict"]},
        "group_action_audit": {"script": aud["script"], "script_sha256": aud["script_sha256"],
                               "imports": aud["imports"], "arithmetic": aud["arithmetic"],
                               "action_definition": "(g c)_x = mu * c_{pi^-1(x)} mod 27 (pi[i] = image of row i), "
                                                    "then subtract the column's first entry",
                               "candidates": cands},
        "dm_to_cfr": {"per_candidate": dm2cfr, "converse_explanation": aud["converse_explanation"]},
        "controls": aud["controls"],
        "resources": {"max_child_ru_maxrss_bytes": max(c["ru_maxrss_bytes"] for c in producer_cases),
                      "new_data_bytes_excluding_receipt": total, "free_bytes_after_replay": rep["free_bytes_end"]},
        "files_sha256": files,
    }
    # the fixed disclosure sentences above are only true under these observed conditions; refuse otherwise
    guards = {"binary_equals_worker": build["binary"]["equals_worker_binary"],
              "stdout_normalised_equal": all(c["stdout_equal_worker_after_normalisation"] for c in producer_cases),
              "bases_equal_freeze": all(c["printed_bases_equal_freeze"] for c in producer_cases),
              "xcrun_db_unchanged_across_compile": build["xcrun_db_before"] == build["xcrun_db_after"],
              "xcrun_db_size_2670": build["xcrun_db_before"].get("bytes") == 2670}
    if not all(guards.values()):
        raise SystemExit("disclosure preconditions failed: %s" % guards)
    rec["disclosure_preconditions"] = guards
    with open(RECEIPT, "x") as fh:
        fh.write(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({"receipt": rel(RECEIPT), "verdicts": rec["verdicts"], "files": len(files), "bytes": total}, indent=1))


if __name__ == "__main__":
    main()
