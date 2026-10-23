#!/usr/bin/env python3
"""Generate the kernel-checked control modules ControlsFixtures.lean and ControlsPinned.lean.

Inputs, read byte-exactly, each SHA-256 checked against an existing receipt:

* the 97 prep fixtures information-science/evidence/six-lane-20261016/cpcw-optimal-prep/controls/
  {positive,negative,preserving}/*.txt, against controls/receipt.json (which also gives the CLI
  (v, k), the expected verdict, the intended failing stage and, for accepted files, the uncovered
  differences);
* the parent fixtures review/cpcw-parent-controls-v1/*.txt, against negative-result.json there.

Parser stage (this worker's strict reader gen_lean.parse plus the SHA comparison, i.e. exactly the
reader used for the eight certificates, called with the CLI (v, k) of the receipt): crlf,
leading_zero, header_wrong_v, cli_wrong_v, cli_wrong_k and sha_mismatch (expected SHA-256 = 64
zeros, as in the prep's controls.py), and the parent's wrong-v (CLI v = 123), wrong-k (CLI k = 5)
and wrong-sha (expected SHA-256 = 64 zeros) must be rejected; every other fixture must parse and
round-trip byte-exactly.

Kernel stage (ControlsFixtures.lean; every theorem is proved by `decide +kernel` or by the generic
soundness theorem `isCPCW_of_check`):

* positive and preserving fixtures: `Cpcw.IsOptimalCPCW` of the named family, and the receipt's
  uncovered set confirmed by `leaveCheck`;
* changed_element, swapped_elements, duplicated_difference, half_v, repeated_element, and the
  parent's duplicate-codeword, repeated-difference, half-order-pair: `check = false`;
* out_of_range (prep and parent): `check = false` and the shape statement is false;
* missing_codeword (prep and parent): the count identity is false while `check = true` (a valid
  packing below the bound, rejected for the intended reason only);
* extra_codeword: the count identity is false.

Pinned-data controls (ControlsPinned.lean), stated against the pinned literals data{v}k{k}:
one point changed (+1 mod v) in the first and in the last codeword, the last codeword replaced by
the first, a point repeated, and (even v) a pair at distance v/2 inserted are rejected by `check`;
dropping the last codeword keeps `check` true but falsifies the count identity; the same data
under a changed header order v - 1 or v + 1 is rejected by `check`; under a changed weight k - 1
the shape and the count identity are false, and under k + 1 the count identity is false;
translating the first codeword by 1, multiplying all points by the smallest unit m >= 2 and
negating all points are accepted.  Changed targets: one more codeword than the bound is impossible
for every family (`Cpcw.not_exists_of_bound_lt`), and no perfect code (every nonzero residue
exactly once) exists (`Cpcw.card_mul_eq_of_perfect`).

Usage: python3 gen_controls.py OUTDIR
"""
import hashlib
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import gen_lean  # noqa: E402  (same strict reader as the certificate generator)

ROOT = HERE.parents[4]
PREP = ROOT / "information-science/evidence/six-lane-20261016/cpcw-optimal-prep/controls"
PREP_RECEIPT = PREP / "receipt.json"
PARENT = HERE.parent / "cpcw-parent-controls-v1"
PARENT_RECEIPT = PARENT / "negative-result.json"
CASES = [(122, 6, 4), (123, 6, 4), (124, 6, 4), (143, 5, 7), (144, 5, 7), (146, 5, 7), (162, 5, 8),
         (167, 5, 8)]
ZERO_SHA = "0" * 64
PARSER_NEGATIVE = {"crlf", "leading_zero", "header_wrong_v", "cli_wrong_v", "cli_wrong_k", "sha_mismatch"}
CHECK_FALSE = {"changed_element", "swapped_elements", "duplicated_difference", "half_v", "repeated_element"}
ACCEPT = {"positive", "translate", "negate", "reorder"}
PARENT_KIND = {"duplicate-codeword": "check_false", "repeated-difference": "check_false",
               "half-order-pair": "check_false", "out-of-range": "out_of_range",
               "missing-codeword": "missing_codeword", "wrong-v": "parser", "wrong-k": "parser",
               "wrong-sha": "parser"}
PARENT_CLI = {"wrong-v": (123, 6, None), "wrong-k": (122, 5, None), "wrong-sha": (122, 6, ZERO_SHA)}


def camel(text):
    return "".join(part[:1].upper() + part[1:] for part in text.replace("-", "_").split("_") if part)


def try_parse(raw, v, k, expected_sha):
    """The certificate generator's reader: SHA comparison, strict parse, byte-exact round trip."""
    if hashlib.sha256(raw).hexdigest() != expected_sha:
        return None, "SHA-256 mismatch"
    try:
        blocks = gen_lean.parse(raw, v, k)
    except SystemExit as exc:
        return None, str(exc)
    if gen_lean.render_raw(blocks, v, k) != raw:
        return None, "not a canonical rendering"
    return blocks, None


def prep_fixtures():
    record = json.loads(PREP_RECEIPT.read_text())
    out, parser = [], {}
    for row in record["rows"]:
        path = PREP / row["file"]
        raw = path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if sha != row["sha256"]:
            raise SystemExit(f"prep fixture {row['file']}: SHA-256 {sha} differs from the receipt")
        stem = pathlib.Path(row["file"]).stem
        if stem.startswith("axioms_"):
            kind, base = "positive", stem[len("axioms_"):]
            name = f"fxPrepAxioms{base.replace('_', 'k')}"
        else:
            v_text, k_text, kind = stem.split("_", 2)
            name = f"fxPrep{v_text}k{k_text}{camel(kind)}"
        v, k = row["cli_v"], row["cli_k"]
        expected_sha = ZERO_SHA if kind == "sha_mismatch" else row["sha256"]
        blocks, reason = try_parse(raw, v, k, expected_sha)
        parser[row["file"]] = {"sha256": sha, "cli": [v, k], "parsed": blocks is not None, "reason": reason}
        if kind in PARSER_NEGATIVE:
            if blocks is not None:
                raise SystemExit(f"parser control failed: {row['file']} was accepted")
            continue
        if blocks is None:
            raise SystemExit(f"parser control failed: {row['file']} was rejected: {reason}")
        if (row["expect"] == "ACCEPT") != (kind in ACCEPT):
            raise SystemExit(f"unexpected receipt verdict for {row['file']}")
        out.append({"name": name, "kind": kind, "v": v, "k": k, "blocks": blocks, "sha": sha,
                    "label": f"prep controls/{row['file']}", "leave": row.get("uncovered")})
    return out, parser


def parent_fixtures():
    record = {t["name"]: t for t in json.loads(PARENT_RECEIPT.read_text())["trials"]}
    out, parser = [], {}
    for stem, kind in PARENT_KIND.items():
        raw = (PARENT / f"{stem}.txt").read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if sha != record[stem]["sha256"]:
            raise SystemExit(f"parent fixture {stem}: SHA-256 {sha} differs from the receipt")
        v, k, wrong_sha = PARENT_CLI.get(stem, (122, 6, None))
        blocks, reason = try_parse(raw, v, k, wrong_sha or sha)
        parser[f"{stem}.txt"] = {"sha256": sha, "cli": [v, k], "parsed": blocks is not None, "reason": reason}
        if kind == "parser":
            if blocks is not None:
                raise SystemExit(f"parser control failed: {stem} was accepted")
            continue
        if blocks is None:
            raise SystemExit(f"parser control failed: {stem} was rejected: {reason}")
        out.append({"name": f"fxParent{camel(stem)}", "kind": kind, "v": v, "k": k, "blocks": blocks,
                    "sha": sha, "label": f"review/cpcw-parent-controls-v1/{stem}.txt", "leave": None})
    return out, parser


def lit(blocks):
    return "[" + ", ".join("[" + ", ".join(str(x) for x in b) + "]" for b in blocks) + "]"


def header(imports, title, body_doc):
    return [*(f"import {m}" for m in imports), "", "/-!", f"# {title}", "",
            "GENERATED by gen_controls.py.  Every theorem is a control of the generic checker, proved by",
            "`decide +kernel` (kernel evaluation) or by `isCPCW_of_check`; no root depends on this module.",
            *body_doc, "-/", "", "namespace Cpcw.Kernel.Controls", "", "open Cpcw.Kernel", ""]


def fixture_theorems(fx):
    name, kind, v, k = fx["name"], fx["kind"], fx["v"], fx["k"]
    n = len(fx["blocks"])
    count = f"{n} = ({v} - 1) / ({k} * ({k} - 1))"
    shape = f"(∀ b ∈ {name}, b.length = {k} ∧ ∀ x ∈ b, x < {v})"
    if kind in ACCEPT:
        leave = "[" + ", ".join(str(x) for x in fx["leave"]) + "]"
        return [f"theorem {name}_optimal : Cpcw.IsOptimalCPCW (blockOf {v} (by decide) {k} {n} {name}) :=",
                f"  ⟨isCPCW_of_check {v} {k} {n} (by decide) {name} (by decide +kernel), by decide +kernel⟩", "",
                f"theorem {name}_leave : leaveCheck {v} {k} {n} {name} {leave} = true := by",
                "  decide +kernel", ""]
    if kind in CHECK_FALSE or kind == "check_false":
        return [f"theorem {name}_rejected : check {v} {k} {n} {name} = false := by", "  decide +kernel", ""]
    if kind == "out_of_range":
        return [f"theorem {name}_rejected : check {v} {k} {n} {name} = false ∧ ¬ {shape} := by",
                "  decide +kernel", ""]
    if kind == "missing_codeword":
        return [f"theorem {name}_rejected : ¬ ({count}) ∧ check {v} {k} {n} {name} = true := by",
                "  decide +kernel", ""]
    if kind == "extra_codeword":
        return [f"theorem {name}_rejected : ¬ ({count}) := by", "  decide +kernel", ""]
    raise SystemExit(f"no kernel control for kind {kind}")


def render_fixtures(fixtures):
    lines = header(["CpcwKernel.Mutations"], "Kernel controls: prep and parent fixtures",
                   ["Fixture literals are copied verbatim (codewords in file order) from the prep fixtures",
                    "information-science/evidence/six-lane-20261016/cpcw-optimal-prep/controls/ (SHA-256 as in",
                    "its controls/receipt.json) and the parent fixtures review/cpcw-parent-controls-v1/ (SHA-256 as",
                    "in its negative-result.json)."])
    for fx in fixtures:
        lines += [f"/-- {fx['label']} (CLI v = {fx['v']}, k = {fx['k']}; kind {fx['kind']}),",
                  f"SHA-256 {fx['sha']}. -/",
                  f"def {fx['name']} : List (List Nat) := {lit(fx['blocks'])}", ""]
    for fx in fixtures:
        lines += fixture_theorems(fx)
    lines += ["end Cpcw.Kernel.Controls", ""]
    return "\n".join(lines)


def pinned_theorems(v, k, n):
    tag = f"{v}k{k}"
    d, c = f"data{tag}", f"cpcw{tag}"
    unit = next(m for m in range(2, v) if math.gcd(m, v) == 1)
    out = [f"/-! ### Mutations of the pinned `{d}` ({n} codewords) -/", "",
           f"theorem {c}_bumpFirst_rejected : check {v} {k} {n} (bump {v} {d} 0 1) = false := by",
           "  decide +kernel", "",
           f"theorem {c}_bumpLast_rejected : check {v} {k} {n} (bump {v} {d} {n - 1} {k - 1}) = false := by",
           "  decide +kernel", "",
           f"theorem {c}_dupCodeword_rejected : check {v} {k} {n} (dupFirst {d} {n - 1}) = false := by",
           "  decide +kernel", "",
           f"theorem {c}_repeatPoint_rejected :",
           f"    check {v} {k} {n} (setPoint {d} 0 1 (rawAt {d} 0 0)) = false := by",
           "  decide +kernel", ""]
    if v % 2 == 0:
        out += [f"theorem {c}_halfPair_rejected :",
                f"    check {v} {k} {n} (setPoint {d} 0 {k - 1} ((rawAt {d} 0 0 + {v // 2}) % {v})) = false := by",
                "  decide +kernel", ""]
    out += [f"theorem {c}_dropCodeword_rejected :",
            f"    ¬ ({n - 1} = ({v} - 1) / ({k} * ({k} - 1))) ∧ check {v} {k} {n - 1} {d} = true := by",
            "  decide +kernel", "",
            f"theorem {c}_headerDown_rejected : check {v - 1} {k} {n} {d} = false := by",
            "  decide +kernel", "",
            f"theorem {c}_headerUp_rejected : check {v + 1} {k} {n} {d} = false := by",
            "  decide +kernel", "",
            f"theorem {c}_weightDown_rejected :",
            f"    ¬ (∀ b ∈ {d}, b.length = {k - 1} ∧ ∀ x ∈ b, x < {v}) ∧",
            f"      ¬ ({n} = ({v} - 1) / ({k - 1} * ({k - 1} - 1))) := by",
            "  decide +kernel", "",
            f"theorem {c}_weightUp_rejected : ¬ ({n} = ({v} - 1) / ({k + 1} * ({k + 1} - 1))) := by",
            "  decide +kernel", "",
            f"theorem {c}_translate_accepted : check {v} {k} {n} (translateBlock {v} {d} 0 1) = true := by",
            "  decide +kernel", "",
            f"theorem {c}_scale{unit}_accepted : check {v} {k} {n} (scale {v} {unit} {d}) = true := by",
            "  decide +kernel", "",
            f"theorem {c}_negate_accepted : check {v} {k} {n} (scale {v} {v - 1} {d}) = true := by",
            "  decide +kernel", "",
            f"/-- Changed target: no `({v}, {k}, 1)` CPCW code has {n + 1} codewords. -/",
            f"theorem {c}_oneMore_impossible : ¬ ∃ B : Fin {n + 1} → Fin {k} → Fin {v}, Cpcw.IsCPCW B :=",
            "  Cpcw.not_exists_of_bound_lt (by decide) (by decide)", "",
            f"/-- Changed target: no perfect `({v}, {k}, 1)` code (every nonzero residue exactly once). -/",
            f"theorem {c}_perfect_impossible : ¬ ∃ m : ℕ, ∃ B : Fin m → Fin {k} → Fin {v},",
            f"    (∀ e : Fin {v}, e.val ≠ 0 → (Cpcw.diffs B).count e = 1) ∧",
            f"      (∀ e : Fin {v}, e.val = 0 → (Cpcw.diffs B).count e = 0) := by",
            "  rintro ⟨m, B, h1, h0⟩",
            "  have h := Cpcw.card_mul_eq_of_perfect h1 h0",
            "  omega", ""]
    return out


def render_pinned():
    lines = header(["CpcwKernel.Mutations", "CpcwKernel.Optimality",
                    *(f"CpcwKernel.Data{v}k{k}" for v, k, _ in CASES)],
                   "Kernel controls: mutations of the eight pinned certificates and changed targets",
                   ["Mutations are stated against the pinned literals `data{v}k{k}` (CpcwKernel.Mutations)."])
    for v, k, n in CASES:
        lines += pinned_theorems(v, k, n)
    lines += ["end Cpcw.Kernel.Controls", ""]
    return "\n".join(lines)


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    prep, prep_parser = prep_fixtures()
    parent, parent_parser = parent_fixtures()
    files = {"ControlsFixtures.lean": render_fixtures(prep + parent), "ControlsPinned.lean": render_pinned()}
    hashes = {}
    for name, text in files.items():
        data = text.encode("utf-8")
        (out / name).write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    kinds = {}
    for fx in prep + parent:
        kinds[fx["kind"]] = kinds.get(fx["kind"], 0) + 1
    print(json.dumps({"parser_controls": {"prep": prep_parser, "parent": parent_parser},
                      "kernel_fixture_kinds": kinds, "generated_sha256": hashes,
                      "prep_receipt_sha256": hashlib.sha256(PREP_RECEIPT.read_bytes()).hexdigest(),
                      "parent_receipt_sha256": hashlib.sha256(PARENT_RECEIPT.read_bytes()).hexdigest()},
                     indent=2))


if __name__ == "__main__":
    sys.exit(main())
