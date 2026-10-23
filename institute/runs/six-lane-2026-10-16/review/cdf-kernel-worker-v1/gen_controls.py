#!/usr/bin/env python3
"""Generate the kernel-checked control modules Controls.lean, Controls801.lean, Controls901.lean.

Inputs, read byte-exactly: the parent's checker-control fixtures
review/cdf-checker-controls-v2-fixtures/*.txt, whose SHA-256 must equal the values recorded in
review/cdf-checker-controls-v2.json.  Real-certificate mutations are stated in Lean against the
pinned data modules (CdfKernel.Data{v}), so they need no input here.

Parser controls (this worker's strict parser gen_lean.parse, with the header order read from the
file): bad_header, noncanonical_token and tab_separator must be rejected; every other fixture must
parse and round-trip byte-exactly.  The emitted Lean controls, each a theorem, are:

* the five literature positives (v = 81, 121, 141, 221, 381) yield Cdf.IsCDF via isCDF_of_check;
* changed_element, duplicated_block, repeated_point, out_of_range: the coverage check is false
  (`coverMask v n d ≠ fullMask v`), and out_of_range also fails the shape check;
* dropped_block, wrong_v: the count identity `20 * n + 1 = v` is false and coverage is false;
* for every pinned order: one residue changed (+1 mod v) in the first block and in the last block,
  the last block replaced by the first, and the last block dropped are all rejected, while
  translating the first block by 1 and multiplying all residues by 2 (a unit, v odd) are accepted.

Usage: python3 gen_controls.py OUTDIR
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import gen_lean  # noqa: E402  (same strict parser as the certificate generator)

FIXTURES = HERE.parent / "cdf-checker-controls-v2-fixtures"
FIXTURE_RECORD = HERE.parent / "cdf-checker-controls-v2.json"
PARSER_NEGATIVE = ["bad_header", "noncanonical_token", "tab_separator"]
POSITIVE = ["positive_81", "positive_121", "positive_141", "positive_221", "positive_381"]
COVER_NEGATIVE = ["changed_element", "duplicated_block", "repeated_point", "out_of_range"]
COUNT_NEGATIVE = ["dropped_block", "wrong_v"]
ORDERS = {321: 16, 501: 25, 621: 31, 681: 34, 801: 40, 901: 45}
HEADER = re.compile(r"CDF (0|[1-9][0-9]*) 5")


def camel(name):
    return "fx" + "".join(part.capitalize() for part in name.split("_"))


def parse_fixture(raw):
    first = raw.split(b"\n", 1)[0].decode("ascii", "replace")
    match = HEADER.fullmatch(first)
    if not match:
        raise SystemExit(f"gen_lean.py: unexpected header {first!r}")
    v = int(match.group(1))
    blocks = gen_lean.parse(raw, v)
    if gen_lean.render_raw(blocks, v) != raw:
        raise SystemExit("gen_lean.py: raw bytes are not the canonical rendering of the parsed blocks")
    return v, blocks


def load_fixtures():
    record = json.loads(FIXTURE_RECORD.read_text())["fixtures"]
    out, parser_results = {}, {}
    for name in PARSER_NEGATIVE + POSITIVE + COVER_NEGATIVE + COUNT_NEGATIVE:
        raw = (FIXTURES / f"{name}.txt").read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if sha != record[name]["sha256"]:
            raise SystemExit(f"fixture {name}: SHA-256 {sha} differs from the parent record")
        try:
            v, blocks = parse_fixture(raw)
            parser_results[name] = {"sha256": sha, "parsed": True, "v": v, "blocks": len(blocks)}
            out[name] = (v, blocks, sha)
        except SystemExit as exc:
            parser_results[name] = {"sha256": sha, "parsed": False, "reason": str(exc)}
    for name in PARSER_NEGATIVE:
        if parser_results[name]["parsed"]:
            raise SystemExit(f"parser control failed: {name} was accepted")
    for name in POSITIVE + COVER_NEGATIVE + COUNT_NEGATIVE:
        if not parser_results[name]["parsed"]:
            raise SystemExit(f"parser control failed: {name} was rejected")
    return out, parser_results


def lit(blocks):
    return "[" + ", ".join("[" + ", ".join(str(x) for x in b) + "]" for b in blocks) + "]"


def order_controls(v, n):
    d = f"data{v}"
    return [
        f"/-! ### Mutations of the pinned `{d}` ({n} blocks) -/",
        "",
        f"theorem cdf{v}_bumpFirst_rejected : coverMask {v} {n} (bump {v} {d} 0 1) ≠ fullMask {v} := by",
        "  decide +kernel",
        "",
        f"theorem cdf{v}_bumpLast_rejected : coverMask {v} {n} (bump {v} {d} {n - 1} 4) ≠ fullMask {v} := by",
        "  decide +kernel",
        "",
        f"theorem cdf{v}_dupBlock_rejected : coverMask {v} {n} (dupFirst {d} {n - 1}) ≠ fullMask {v} := by",
        "  decide +kernel",
        "",
        f"theorem cdf{v}_dropBlock_rejected : coverMask {v} {n - 1} {d} ≠ fullMask {v} := by",
        "  decide +kernel",
        "",
        f"theorem cdf{v}_translate_accepted :",
        f"    coverMask {v} {n} (translateBlock {v} {d} 0 1) = fullMask {v} := by",
        "  decide +kernel",
        "",
        f"theorem cdf{v}_scale2_accepted : coverMask {v} {n} (scale {v} 2 {d}) = fullMask {v} := by",
        "  decide +kernel",
        "",
    ]


def header(imports, title, body_doc):
    return [*(f"import {m}" for m in imports), "", "/-!", f"# {title}", "",
            "GENERATED by gen_controls.py.  Every theorem is a control of the generic checker, proved by",
            "`decide +kernel` (kernel evaluation) or by `isCDF_of_check`; no root depends on this module.",
            *body_doc, "-/", "", "namespace Cdf.Kernel.Controls", "", "open Cdf.Kernel", ""]


def render_main(fixtures):
    lines = header(["CdfKernel.Mutations", "CdfKernel.Data321", "CdfKernel.Data501",
                    "CdfKernel.Data621", "CdfKernel.Data681"],
                   "Kernel controls: parent fixtures and the four original orders",
                   ["Fixture literals are copied verbatim from review/cdf-checker-controls-v2-fixtures/",
                    "(SHA-256 values as in review/cdf-checker-controls-v2.json)."])
    for name in POSITIVE + COVER_NEGATIVE + COUNT_NEGATIVE:
        v, blocks, sha = fixtures[name]
        lines += [f"/-- `{name}.txt`, SHA-256 {sha}. -/",
                  f"def {camel(name)} : List (List Nat) := {lit(blocks)}", ""]
    lines += ["/-! ### Literature positives: accepted, with the semantic conclusion -/", ""]
    for name in POSITIVE:
        v, blocks, _ = fixtures[name]
        n = len(blocks)
        lines += [f"theorem {camel(name)}_isCDF : Cdf.IsCDF (blockOf {v} (by decide) {n} {camel(name)}) :=",
                  f"  isCDF_of_check {v} {n} (by decide) {camel(name)} (by decide +kernel) (by decide +kernel)", ""]
    lines += ["/-! ### Negative fixtures: rejected by the kernel-evaluated checks -/", ""]
    for name in COVER_NEGATIVE:
        v, blocks, _ = fixtures[name]
        n = len(blocks)
        lines += [f"theorem {camel(name)}_rejected : coverMask {v} {n} {camel(name)} ≠ fullMask {v} := by",
                  "  decide +kernel", ""]
    v, blocks, _ = fixtures["out_of_range"]
    lines += [f"theorem {camel('out_of_range')}_shape_rejected :",
              f"    ¬ (∀ b ∈ {camel('out_of_range')}, b.length = 5 ∧ ∀ x ∈ b, x < {v}) := by",
              "  decide +kernel", ""]
    for name in COUNT_NEGATIVE:
        v, blocks, _ = fixtures[name]
        n = len(blocks)
        lines += [f"theorem {camel(name)}_rejected :",
                  f"    20 * {n} + 1 ≠ {v} ∧ coverMask {v} {n} {camel(name)} ≠ fullMask {v} := by",
                  "  decide +kernel", ""]
    for v in [321, 501, 621, 681]:
        lines += order_controls(v, ORDERS[v])
    lines += ["end Cdf.Kernel.Controls", ""]
    return "\n".join(lines)


def render_order(v):
    lines = header(["CdfKernel.Mutations", f"CdfKernel.Data{v}"],
                   f"Kernel controls for the separately added order {v}", [])
    lines += order_controls(v, ORDERS[v])
    lines += ["end Cdf.Kernel.Controls", ""]
    return "\n".join(lines)


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    fixtures, parser_results = load_fixtures()
    files = {"Controls.lean": render_main(fixtures),
             "Controls801.lean": render_order(801),
             "Controls901.lean": render_order(901)}
    hashes = {}
    for name, text in files.items():
        data = text.encode("utf-8")
        (out / name).write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    print(json.dumps({"parser_controls": parser_results, "generated_sha256": hashes}, indent=2))


if __name__ == "__main__":
    sys.exit(main())
