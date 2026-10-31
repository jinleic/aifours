#!/usr/bin/env python3
"""Frozen, exact-integer replay; writes only the two exclusive replay outputs."""
import copy
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PINS = {
    "manifest-v1.json": ("bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0", 2935, 43),
    "parent-inputs-v1/physical-definition-v1.md": ("3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff", 2115, 11),
    "parent-inputs-v1/witness.json": ("a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413", 8040, 891),
}
N = 8
ORIGINAL_KIND = "ACTUAL_THREE_MOQLS_ONE_NONCLASSICAL_MIXED8"
CONTROL_KIND = "REPLAY_CLASSICAL_THREE_MOLS_CONTROL"
KEYS = {"kind", "source_triple_index", "source_square_index", "quantum_square_numerators", "quantum_square_denominator_squared", "classical_mates", "trade_cells", "normalization", "limits"}


class InputError(Exception):
    def __init__(self, code, detail):
        self.code = code
        super().__init__(detail)


class ReplayError(Exception):
    pass


def insist(condition, detail):
    if not condition:
        raise ReplayError(detail)


def clock():
    return datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z %Z")


def descriptor(raw):
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "LF": raw.count(b"\n")}


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError("duplicate_json_key", "duplicate key: " + key)
        result[key] = value
    return result


def no_constant(value):
    raise InputError("invalid_json_constant", "nonfinite constant: " + value)


def parse_json(raw):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=no_duplicates, parse_constant=no_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise InputError("invalid_json", str(exc)) from exc


def is_int(value):
    return type(value) is int


def valid_square_document(raw, kind=ORIGINAL_KIND):
    doc = parse_json(raw)
    if not isinstance(doc, dict) or set(doc) != KEYS:
        raise InputError("document_keys", "wrong, missing, or extra top-level keys")
    if doc["kind"] != kind:
        raise InputError("kind", "unexpected kind")
    if not all(is_int(doc[key]) for key in ("source_triple_index", "source_square_index")):
        raise InputError("metadata", "source indices must be integers")
    if not all(isinstance(doc[key], str) for key in ("normalization", "limits")):
        raise InputError("metadata", "normalization and limits must be strings")
    nums = doc["quantum_square_numerators"]
    dens = doc["quantum_square_denominator_squared"]
    if not isinstance(nums, list) or len(nums) != 64:
        raise InputError("quantum_shape", "need 64 row-major quantum vectors")
    if not isinstance(dens, list) or len(dens) != 64:
        raise InputError("normalizer_shape", "need 64 row-major normalizers")
    quantum = []
    for index, (vector, denominator) in enumerate(zip(nums, dens)):
        if not isinstance(vector, list) or len(vector) != N or not all(is_int(x) for x in vector):
            raise InputError("quantum_vector_shape", f"cell {index}: need eight integer coordinates")
        if not is_int(denominator) or denominator <= 0:
            raise InputError("bad_normalizer", f"cell {index}: denominator_squared must be a positive integer")
        quantum.append((tuple(vector), denominator))
    mates = doc["classical_mates"]
    if not isinstance(mates, list) or len(mates) != 2:
        raise InputError("mates_shape", "need exactly two classical members")
    squares = [quantum]
    for mi, matrix in enumerate(mates):
        if not isinstance(matrix, list) or len(matrix) != N:
            raise InputError("mate_shape", f"member {mi}: need eight rows")
        square = []
        for row, entries in enumerate(matrix):
            if not isinstance(entries, list) or len(entries) != N:
                raise InputError("mate_shape", f"member {mi}, row {row}: need eight labels")
            for col, label in enumerate(entries):
                if not is_int(label) or not 0 <= label < N:
                    raise InputError("mate_label", f"member {mi}, cell ({row},{col}): invalid label")
                square.append((tuple(int(i == label) for i in range(N)), 1))
        squares.append(square)
    trade = doc["trade_cells"]
    if not isinstance(trade, list) or not all(is_int(x) and 0 <= x < 64 for x in trade):
        raise InputError("trade_cells", "trade cells must be a list of valid integer coordinates")
    if trade != sorted(set(trade)):
        raise InputError("trade_cells", "trade cells must be distinct and increasing")
    return doc, squares


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def summary(matrices, entries, failures, **extra):
    counts = Counter(f["kind"] for f in failures)
    result = {"matrices": matrices, "entries": entries, "failure_count": len(failures),
              "failure_types": dict(sorted(counts.items())), "first_failure": failures[0] if failures else None}
    result.update(extra)
    return result


def line_grams(square, axes=("row", "column")):
    failures = []
    entries = 0
    matrices = 0
    for axis in axes:
        for fixed in range(N):
            indices = [N * fixed + p if axis == "row" else N * p + fixed for p in range(N)]
            matrices += 1
            for i in range(N):
                for j in range(N):
                    left, ld = square[indices[i]]
                    right, rd = square[indices[j]]
                    value = dot(left, right)
                    expected = ld if i == j else 0
                    entries += 1
                    if value != expected:
                        failures.append({"kind": "diagonal" if i == j else "off_diagonal", "axis": axis,
                                         "slice": fixed, "left_cell": indices[i], "right_cell": indices[j],
                                         "integer_inner_product": value, "expected_integer": expected,
                                         "left_denominator_squared": ld, "right_denominator_squared": rd})
    return summary(matrices, entries, failures)


def tensor_gram(left, right):
    # Construct the complete 64-coordinate tensor numerator, not a product of
    # two precomputed member Gram entries. The physical denominator is sqrt(d).
    tensors = []
    denominators = []
    for (u, du), (v, dv) in zip(left, right):
        tensors.append(tuple(x * y for x in u for y in v))
        denominators.append(du * dv)
    insist(len(tensors) == 64 and all(len(t) == 64 for t in tensors), "tensor construction dimensions")
    failures = []
    for i in range(64):
        for j in range(64):
            value = dot(tensors[i], tensors[j])
            expected = denominators[i] if i == j else 0
            if value != expected:
                failures.append({"kind": "diagonal" if i == j else "off_diagonal", "left_cell": i,
                                 "right_cell": j, "integer_inner_product": value, "expected_integer": expected,
                                 "left_denominator_squared": denominators[i],
                                 "right_denominator_squared": denominators[j]})
    counts = Counter(denominators)
    return summary(1, 4096, failures, tensor_dimensions=[64, 64],
                   diagonal_normalizer_counts={str(k): counts[k] for k in sorted(counts)})


def overlap_summary(square):
    counts = Counter()
    first_proper = None
    for i in range(64):
        for j in range(i + 1, 64):
            u, du = square[i]
            v, dv = square[j]
            overlap = Fraction(dot(u, v) ** 2, du * dv)
            counts[overlap] += 1
            if first_proper is None and 0 < overlap < 1:
                first_proper = {"left_cell": i, "right_cell": j, "left_rc": [i // 8, i % 8],
                                "right_rc": [j // 8, j % 8], "left_numerator": list(u),
                                "right_numerator": list(v), "left_denominator_squared": du,
                                "right_denominator_squared": dv, "squared_overlap": str(overlap)}
    return {"unordered_pairs": 2016, "squared_overlap_counts": {str(k): counts[k] for k in sorted(counts)},
            "first_strictly_between_zero_and_one": first_proper}


def canonical(doc):
    return json.dumps(doc, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")


def fixture(raw):
    return {"encoding": "UTF-8", "canonical_or_literal_utf8": raw.decode("utf-8"), **descriptor(raw)}


def all_line_results(squares):
    return {name: line_grams(square) for name, square in zip(("Q", "A", "B"), squares)}


def all_pair_results(squares):
    return {name: tensor_gram(squares[i], squares[j]) for name, i, j in
            (("Q-A", 0, 1), ("Q-B", 0, 2), ("A-B", 1, 2))}


def all_pass(results):
    return all(item["failure_count"] == 0 for item in results.values())


def require_only_failure(result, kind, reason):
    insist(result["failure_count"] > 0, reason + ": expected a failure")
    insist(set(result["failure_types"]) == {kind}, reason + ": incorrect failure type " + repr(result["failure_types"]))


def pair_control(raw, pair):
    _, squares = valid_square_document(raw)
    lines = all_line_results(squares)
    insist(all_pass(lines), "the mutation must preserve all individual row/column bases")
    left, right = pair
    result = tensor_gram(squares[left], squares[right])
    require_only_failure(result, "off_diagonal", "same-cell tensor pairing")
    return {"preserved_all_member_line_grams": True, "failure": result}


def sign_control(raw):
    _, squares = valid_square_document(raw)
    result = line_grams(squares[0], ("row",))
    require_only_failure(result, "off_diagonal", "opposite-sign replacement")
    first = result["first_failure"]
    insist((first["slice"], first["left_cell"], first["right_cell"], first["integer_inner_product"]) == (2, 18, 19, 2),
           "opposite-sign mutation did not produce the intended row-2 overlap")
    return {"failure": result}


def scale_control(raw):
    _, squares = valid_square_document(raw)
    result = line_grams(squares[0], ("row",))
    insist(result["failure_count"] == 1 and result["failure_types"] == {"diagonal": 1}, "scale must fail only the row diagonal")
    first = result["first_failure"]
    insist((first["left_cell"], first["integer_inner_product"], first["expected_integer"]) == (0, 4, 1),
           "wrong scaling failure")
    return {"failure": result}


def row_swap_cells_control(raw):
    _, squares = valid_square_document(raw)
    rows = line_grams(squares[0], ("row",))
    columns = line_grams(squares[0], ("column",))
    insist(rows["failure_count"] == 0, "same-row swap must preserve all rows")
    require_only_failure(columns, "off_diagonal", "same-row swap must break a column")
    first = columns["first_failure"]
    insist((first["axis"], first["slice"], first["left_cell"], first["right_cell"]) == ("column", 0, 0, 8),
           "wrong same-row swap column failure")
    return {"preserved_all_quantum_rows": True, "failure": columns}


def relabel_control(raw):
    _, squares = valid_square_document(raw)
    result = line_grams(squares[1], ("row",))
    require_only_failure(result, "off_diagonal", "one classical relabel")
    first = result["first_failure"]
    insist((first["slice"], first["left_cell"], first["right_cell"], first["integer_inner_product"]) == (0, 0, 1, 1),
           "wrong classical relabel failure")
    return {"failure": result}


def invalid_input_control(raw, expected):
    try:
        valid_square_document(raw)
    except InputError as exc:
        insist(exc.code == expected, "wrong parser rejection: " + exc.code)
        return {"failure": {"code": exc.code, "detail": str(exc)}}
    raise ReplayError("invalid input was accepted; expected " + expected)


def record_control(records, name, reason, raw, verifier):
    item = {"name": name, "intended_reason": reason, "fixture": fixture(raw)}
    try:
        item["evidence"] = verifier(raw)
        item["result"] = "PASS"
    except Exception as exc:
        item["result"] = "FAIL"
        item["error"] = type(exc).__name__ + ": " + str(exc)
    records.append(item)


def build_positive(doc):
    control = copy.deepcopy(doc)
    control["kind"] = CONTROL_KIND
    changed = []
    for index, (vector, denominator) in enumerate(zip(control["quantum_square_numerators"], control["quantum_square_denominator_squared"])):
        support = [k for k, x in enumerate(vector) if x != 0]
        if len(support) == 2:
            insist(support == [0, 1] and denominator == 2 and vector[0] == 1 and vector[1] in (-1, 1),
                   "positive control requires precisely the observed +/- e0,e1 structure")
            label = 0 if vector[1] == 1 else 1
            control["quantum_square_numerators"][index] = [int(k == label) for k in range(N)]
            control["quantum_square_denominator_squared"][index] = 1
            changed.append(index)
        else:
            insist(len(support) == 1 and vector[support[0]] ** 2 == denominator,
                   "non-mixed quantum cell is not a normalized basis vector")
    insist(changed == doc["trade_cells"] and len(changed) == 8, "unexpected control replacement cells")
    control["trade_cells"] = []
    raw = canonical(control)
    _, squares = valid_square_document(raw, CONTROL_KIND)
    insist(all(sum(x != 0 for x in v) == 1 and dot(v, v) == d for square in squares for v, d in square),
           "positive control is not classical in the supplied basis")
    lines = all_line_results(squares)
    pairs = all_pair_results(squares)
    overlaps = {name: overlap_summary(square) for name, square in zip(("Q_classical", "A", "B"), squares)}
    insist(all_pass(lines), "positive classical control failed a member Gram")
    insist(all_pass(pairs), "positive classical control failed a pair Gram")
    insist(all(item["first_strictly_between_zero_and_one"] is None for item in overlaps.values()),
           "positive control contains a nonclassical overlap")
    return {"result": "PASS", "construction": "Replace each (e0+e1)/sqrt(2) by e0 and each (e0-e1)/sqrt(2) by e1; leave both supplied classical members unchanged.",
            "replaced_cells": changed, "fixture": fixture(raw), "line_grams": lines,
            "pair_grams": pairs, "overlaps": overlaps}


def render_report(record):
    lines = ["# Independent exact replay of the three-member physical witness", "",
             "**RESULT: " + record["result"] + "**", "",
             "Observed clock before this report: " + record["observed_clock_before_report"] + ".", "",
             "## Byte binding", ""]
    for name, info in record.get("inputs", {}).items():
        lines.append(f"- `{name}`: SHA-256 `{info['sha256']}`, {info['bytes']} bytes, {info['LF']} LF.")
    code = record["checker"]
    lines += [f"- `replay-check-v1.py`: SHA-256 `{code['sha256']}`, {code['bytes']} bytes, {code['LF']} LF.",
              "", "The frozen manifest and its first two input pins were compared to the hard-coded full hashes, byte counts and LF counts before calculation.",
              "", "## Method and finite result", "",
              "A cell is an eight-integer numerator and a positive integer squared denominator. For each member and each row/column, every one of the 8×8 integer Gram entries is checked: diagonal numerator equals its denominator, and every off-diagonal numerator is zero. For each pair, this replay explicitly constructs all 64 length-64 Kronecker numerators with squared denominator equal to the product of the two cell denominators, then checks all 64×64 integer Gram entries against the corresponding diagonal denominators and off-diagonal zeros. Thus no floating point or factorized Gram shortcut is used."]
    actual = record.get("witness")
    if actual:
        lines += ["", "| Check | Matrices | Entries | Mismatches |", "|---|---:|---:|---:|"]
        for name, item in actual["line_grams"].items():
            lines.append(f"| {name} row/column | {item['matrices']} | {item['entries']} | {item['failure_count']} |")
        for name, item in actual["pair_grams"].items():
            lines.append(f"| {name} tensor Gram | {item['matrices']} | {item['entries']} | {item['failure_count']} |")
        lines += ["", f"Quantum mixed cells relative to the supplied basis: {actual['mixed_cells']} (count {len(actual['mixed_cells'])}); stated trade cells: {actual['stated_trade_cells']}."]
        for name, item in actual["overlaps"].items():
            lines.append(f"{name} distinct-cell squared-overlap histogram: `{json.dumps(item['squared_overlap_counts'], sort_keys=True)}` (2016 unordered pairs).")
        proof = actual["overlaps"]["Q"]["first_strictly_between_zero_and_one"]
        if proof:
            lines += ["", f"Nonclassicality certificate: Q cells {proof['left_rc']} and {proof['right_rc']} have exact squared overlap **{proof['squared_overlap']}**, with numerator vectors `{proof['left_numerator']}` and `{proof['right_numerator']}` and squared denominators {proof['left_denominator_squared']} and {proof['right_denominator_squared']}. A single global orthonormal output frame with per-cell phases permits only overlap squares 0 or 1; this strict intermediate value rules it out. The mixed count by itself is not the certificate."]
    positive = record.get("positive_control")
    if positive:
        lines += ["", "## Positive classical control", "", positive["construction"],
                  f"The transformed cells are {positive['replaced_cells']}. All three members consist of normalized standard-basis vectors; all 48 member line Grams and all three 64×64 pair Grams pass. This gives an independently checked classical three-member control from the two supplied mates and the observed exact +/- structure. The complete canonical control fixture is retained, hashed, in the receipt."]
    lines += ["", "## Intended-reason negative controls", ""]
    for item in record.get("negative_controls", []):
        failure = item.get("evidence", {}).get("failure", {})
        observed = failure.get("first_failure") or failure
        lines.append(f"- **{item['result']}** `{item['name']}` — {item['intended_reason']}; observed `{json.dumps(observed, sort_keys=True)}`. Fixture SHA-256 `{item['fixture']['sha256']}`.")
        if item.get("error"):
            lines.append("  Control error: " + item["error"])
    lines += ["", "Each complete literal/canonical mutated fixture, its hash, every control's intended reason and the observed diagnostics are preserved in `replay-receipt-v1.json`.",
              "", "## Limits", "",
              "This is one same-harness independent implementation of a finite physical check, not a human, independent-family, external-vendor, formal/kernel or exhaustive review. It does not audit the external source definition, current literature or priority, and does not establish any M(8) claim. It checks only three members; the registered four-family alternative remains open from this result. No author producer/checker, solver, catalog, held mathematics, external model, or network source was used."]
    if record.get("errors"):
        lines += ["", "## Failures", ""] + ["- " + e for e in record["errors"]]
    return ("\n".join(lines) + "\n").encode("utf-8")


def main():
    report_path = ROOT / "replay-review-v1.md"
    receipt_path = ROOT / "replay-receipt-v1.json"
    if report_path.exists() or receipt_path.exists():
        raise SystemExit("Refusing to overwrite either replay output")
    record = {"schema_version": 1, "kind": "INDEPENDENT_SAME_HARNESS_EXACT_PHYSICAL_REPLAY",
              "observed_clock_at_start": clock(), "checker": descriptor(Path(__file__).read_bytes()),
              "inputs": {}, "negative_controls": [], "errors": [], "result": "FAIL"}
    try:
        raws = {}
        for name, (sha, size, lf) in PINS.items():
            raw = (ROOT / name).read_bytes()
            raws[name] = raw
            observed = descriptor(raw)
            record["inputs"][name] = observed
            insist(observed == {"sha256": sha, "bytes": size, "LF": lf}, "frozen byte pin mismatch: " + name)
        manifest = parse_json(raws["manifest-v1.json"])
        for index, path in enumerate(("parent-inputs-v1/physical-definition-v1.md", "parent-inputs-v1/witness.json")):
            item = manifest["inputs_in_read_order"][index]
            pin = record["inputs"][path]
            insist(item["path"] == str(ROOT / path), "manifest path mismatch: " + path)
            insist({key: item[key] for key in ("sha256", "bytes", "LF")} == pin, "manifest pin mismatch: " + path)
        witness_raw = raws["parent-inputs-v1/witness.json"]
        doc, squares = valid_square_document(witness_raw)
        lines = all_line_results(squares)
        pairs = all_pair_results(squares)
        mixed = [i for i, (v, _) in enumerate(squares[0]) if sum(x != 0 for x in v) > 1]
        overlaps = {name: overlap_summary(square) for name, square in zip(("Q", "A", "B"), squares)}
        record["witness"] = {"line_grams": lines, "pair_grams": pairs, "mixed_cells": mixed,
                             "stated_trade_cells": doc["trade_cells"], "overlaps": overlaps}
        if not all_pass(lines):
            record["errors"].append("Physical witness has an 8×8 row/column Gram mismatch")
        if not all_pass(pairs):
            record["errors"].append("Physical witness has a 64×64 tensor Gram mismatch")
        if len(mixed) != 8 or mixed != doc["trade_cells"]:
            record["errors"].append("Eight mixed cells do not agree with the stated coordinates")
        if overlaps["Q"]["first_strictly_between_zero_and_one"] is None:
            record["errors"].append("No strictly intermediate squared overlap certifies nonclassicality")
        if any(overlaps[name]["first_strictly_between_zero_and_one"] is not None for name in ("A", "B")):
            record["errors"].append("A supplied classical member has a nonclassical overlap")
        record["positive_control"] = build_positive(doc)
        controls = record["negative_controls"]

        mutation = copy.deepcopy(doc)
        rows = mutation["classical_mates"][0]
        rows[0], rows[1] = rows[1], rows[0]
        record_control(controls, "row_permute_only_A", "all member bases survive, but A-B same-cell tensor orthogonality fails", canonical(mutation), lambda raw: pair_control(raw, (1, 2)))

        mutation = copy.deepcopy(doc)
        old_q = mutation["quantum_square_numerators"]
        old_d = mutation["quantum_square_denominator_squared"]
        mutation["quantum_square_numerators"] = [old_q[8 * c + r] for r in range(8) for c in range(8)]
        mutation["quantum_square_denominator_squared"] = [old_d[8 * c + r] for r in range(8) for c in range(8)]
        record_control(controls, "transpose_only_Q", "all member bases survive, but Q-A same-cell tensor orthogonality fails", canonical(mutation), lambda raw: pair_control(raw, (0, 1)))

        mutation = copy.deepcopy(doc)
        mutation["quantum_square_numerators"][18] = list(mutation["quantum_square_numerators"][19])
        record_control(controls, "replace_plus_by_minus", "the two superpositions in quantum row 2 have nonzero off-diagonal overlap", canonical(mutation), sign_control)

        mutation = copy.deepcopy(doc)
        mutation["quantum_square_numerators"][0] = [2 * x for x in mutation["quantum_square_numerators"][0]]
        record_control(controls, "double_without_normalizer", "the quantum row-0 Gram diagonal is 4 instead of 1", canonical(mutation), scale_control)

        mutation = copy.deepcopy(doc)
        for row in mutation["classical_mates"][0]:
            row[0], row[1] = row[1], row[0]
        record_control(controls, "column_permute_only_A", "all member bases survive, but A-B same-cell tensor orthogonality fails", canonical(mutation), lambda raw: pair_control(raw, (1, 2)))

        mutation = copy.deepcopy(doc)
        q = mutation["quantum_square_numerators"]
        d = mutation["quantum_square_denominator_squared"]
        q[0], q[1] = q[1], q[0]
        d[0], d[1] = d[1], d[0]
        record_control(controls, "swap_two_Q_cells_in_one_row", "every quantum row survives, but column 0 has a nonzero off-diagonal overlap", canonical(mutation), row_swap_cells_control)

        mutation = copy.deepcopy(doc)
        mutation["classical_mates"][0][0][0] = mutation["classical_mates"][0][0][1]
        record_control(controls, "duplicate_one_A_label", "a single relabel creates a nonzero classical row Gram off-diagonal", canonical(mutation), relabel_control)

        mutation = copy.deepcopy(doc)
        mutation["quantum_square_denominator_squared"][0] = 0
        record_control(controls, "zero_denominator", "strict input validation rejects a nonpositive squared denominator", canonical(mutation), lambda raw: invalid_input_control(raw, "bad_normalizer"))

        duplicate = b'{"kind":"INJECTED",\n' + witness_raw[1:]
        record_control(controls, "duplicate_json_key", "strict JSON parsing rejects a duplicated top-level key", duplicate, lambda raw: invalid_input_control(raw, "duplicate_json_key"))

        mutation = copy.deepcopy(doc)
        mutation["quantum_square_numerators"][0].pop()
        record_control(controls, "short_quantum_vector", "strict input validation rejects a seven-coordinate vector", canonical(mutation), lambda raw: invalid_input_control(raw, "quantum_vector_shape"))

        if len(controls) != 10 or any(item["result"] != "PASS" for item in controls):
            record["errors"].append("One or more intended-reason negative controls failed")
        if not record["errors"]:
            record["result"] = "PASS"
    except Exception as exc:
        record["errors"].append(type(exc).__name__ + ": " + str(exc))

    record["observed_clock_before_report"] = clock()
    report = render_report(record)
    with report_path.open("xb") as out:
        out.write(report)
    record["report"] = {"path": report_path.name, **descriptor(report)}
    record["observed_clock_before_receipt"] = clock()
    receipt = (json.dumps(record, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8")
    with receipt_path.open("xb") as out:
        out.write(receipt)
    print(json.dumps({"result": record["result"], "errors": record["errors"],
                      "controls": {item["name"]: item["result"] for item in record["negative_controls"]},
                      "report": record["report"], "receipt": descriptor(receipt)}, sort_keys=True))
    return 0 if record["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
