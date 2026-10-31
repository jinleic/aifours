#!/usr/bin/env python3
"""Exact, author-code-independent physical verification of the frozen witness.

Run once as: python3 -B verifier-check-v1.py
The sole invocation creates seven retained mutation fixtures and a receipt,
without overwriting any existing output. It does not address source priority.
"""

import copy
import hashlib
import json
import sys
import traceback
from datetime import datetime
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
N = 8
CELLS = N * N
PINS = {
    "manifest": ("manifest-v1.json", "bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0", 2935, 43),
    "definition": ("parent-inputs-v1/physical-definition-v1.md", "3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff", 2115, 11),
    "witness": ("parent-inputs-v1/witness.json", "a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413", 8040, 891),
}
FIELDS = {
    "kind", "source_triple_index", "source_square_index",
    "quantum_square_numerators", "quantum_square_denominator_squared",
    "classical_mates", "trade_cells", "normalization", "limits",
}


class WitnessError(Exception):
    def __init__(self, code, **detail):
        super().__init__(code)
        self.code = code
        self.detail = detail


class IntegrityError(Exception):
    pass


class ControlError(Exception):
    pass


def now():
    return datetime.now().astimezone().isoformat(timespec="microseconds")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pinned_bytes(role):
    path, sha, size, lf = PINS[role]
    data = (HERE / path).read_bytes()
    actual = {"path": path, "sha256": digest(data), "bytes": len(data),
              "LF": data.count(b"\n"), "CR": data.count(b"\r"),
              "ends_with_LF": data.endswith(b"\n")}
    if (actual["sha256"], actual["bytes"], actual["LF"], actual["CR"],
            actual["ends_with_LF"]) != (sha, size, lf, 0, True):
        raise IntegrityError("pin mismatch for " + role + ": " + repr(actual))
    return data, actual


def object_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise WitnessError("duplicate_json_key", key=key)
        result[key] = value
    return result


def invalid_constant(value):
    raise WitnessError("invalid_json_constant", value=value)


def parse_json(data):
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=object_pairs,
                          parse_constant=invalid_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise WitnessError("invalid_json", message=str(error)) from error


def is_integer(value):
    # bool is a subclass of int, but is not an integer in this file format.
    return type(value) is int


def coordinates(index):
    return [index // N, index % N]


def parse_witness(data):
    obj = parse_json(data)
    if type(obj) is not dict:
        raise WitnessError("root_not_object")
    if set(obj) != FIELDS:
        raise WitnessError("object_fields", missing=sorted(FIELDS - set(obj)),
                           unexpected=sorted(set(obj) - FIELDS))
    if obj["kind"] != "ACTUAL_THREE_MOQLS_ONE_NONCLASSICAL_MIXED8":
        raise WitnessError("kind")
    for name in ("source_triple_index", "source_square_index"):
        if not is_integer(obj[name]) or obj[name] < 0:
            raise WitnessError("metadata_integer", field=name)
    for name in ("normalization", "limits"):
        if type(obj[name]) is not str:
            raise WitnessError("metadata_string", field=name)

    nums = obj["quantum_square_numerators"]
    if type(nums) is not list or len(nums) != CELLS:
        raise WitnessError("quantum_vector_count", expected=CELLS,
                           actual=len(nums) if type(nums) is list else None)
    for index, vector in enumerate(nums):
        if type(vector) is not list or len(vector) != N:
            raise WitnessError("quantum_vector_length", cell=coordinates(index),
                               expected=N, actual=len(vector) if type(vector) is list else None)
        for component, value in enumerate(vector):
            if not is_integer(value):
                raise WitnessError("quantum_component_not_integer", cell=coordinates(index),
                                   component=component)

    denoms = obj["quantum_square_denominator_squared"]
    if type(denoms) is not list or len(denoms) != CELLS:
        raise WitnessError("denominator_count", expected=CELLS,
                           actual=len(denoms) if type(denoms) is list else None)
    for index, value in enumerate(denoms):
        if not is_integer(value) or value <= 0:
            raise WitnessError("denominator_not_positive_integer", cell=coordinates(index))

    mates = obj["classical_mates"]
    if type(mates) is not list or len(mates) != 2:
        raise WitnessError("classical_member_count", expected=2,
                           actual=len(mates) if type(mates) is list else None)
    for which, matrix in enumerate(mates, start=1):
        if type(matrix) is not list or len(matrix) != N:
            raise WitnessError("classical_row_count", member=which)
        for row, labels in enumerate(matrix):
            if type(labels) is not list or len(labels) != N:
                raise WitnessError("classical_row_length", member=which, row=row)
            for column, label in enumerate(labels):
                if not is_integer(label) or not 0 <= label < N:
                    raise WitnessError("classical_label", member=which,
                                       cell=[row, column])

    trade = obj["trade_cells"]
    if type(trade) is not list or len(trade) != 8:
        raise WitnessError("trade_cell_count", expected=8,
                           actual=len(trade) if type(trade) is list else None)
    if any(not is_integer(x) or not 0 <= x < CELLS for x in trade):
        raise WitnessError("trade_cell_index")
    if len(set(trade)) != len(trade):
        raise WitnessError("trade_cell_duplicate")
    return obj


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def squared_norm(vector):
    numerator, denominator_squared = vector
    return Fraction(dot(numerator, numerator), denominator_squared)


def squared_overlap(left, right):
    a, da = left
    b, db = right
    return Fraction(dot(a, b) ** 2, da * db)


def squared_tensor_overlap(left_a, left_b, right_a, right_b):
    a, da = left_a
    b, db = left_b
    c, dc = right_a
    d, dd = right_b
    return Fraction((dot(a, c) * dot(b, d)) ** 2, da * db * dc * dd)


def validate_latin(mates):
    universe = set(range(N))
    for member, matrix in enumerate(mates, start=1):
        for row, labels in enumerate(matrix):
            if set(labels) != universe:
                raise WitnessError("classical_latin_row", member=member, row=row,
                                   labels=labels)
        for column in range(N):
            labels = [matrix[row][column] for row in range(N)]
            if set(labels) != universe:
                raise WitnessError("classical_latin_column", member=member, column=column,
                                   labels=labels)


def build_vectors(obj):
    quantum = [(tuple(vector), denom) for vector, denom in
               zip(obj["quantum_square_numerators"], obj["quantum_square_denominator_squared"])]
    basis = [tuple(int(component == label) for component in range(N))
             for label in range(N)]
    members = [quantum]
    for matrix in obj["classical_mates"]:
        members.append([(basis[label], 1) for row in matrix for label in row])
    return members


def check_lines(members):
    line_count = norm_count = overlap_count = 0
    for member, square in enumerate(members):
        for axis in ("row", "column"):
            for line in range(N):
                indices = ([line * N + x for x in range(N)] if axis == "row"
                           else [x * N + line for x in range(N)])
                line_count += 1
                for index in indices:
                    norm = squared_norm(square[index])
                    norm_count += 1
                    if norm != 1:
                        raise WitnessError("line_norm", member=member, axis=axis, line=line,
                                           cell=coordinates(index), squared_norm=str(norm))
                for first in range(N):
                    for second in range(first + 1, N):
                        i, j = indices[first], indices[second]
                        overlap = squared_overlap(square[i], square[j])
                        overlap_count += 1
                        if overlap != 0:
                            raise WitnessError("line_overlap", member=member, axis=axis,
                                               line=line, cells=[coordinates(i), coordinates(j)],
                                               squared_overlap=str(overlap))
    return {"lines": line_count, "norms": norm_count,
            "unordered_off_diagonal_overlaps": overlap_count,
            "expected_lines": 3 * 2 * N, "expected_norms": 3 * 2 * N * N,
            "expected_unordered_overlaps": 3 * 2 * N * (N * (N - 1) // 2)}


def check_product_grams(members):
    results = []
    for first, second in ((0, 1), (0, 2), (1, 2)):
        checked = diagonal = off_diagonal = unique_cross = 0
        for i in range(CELLS):
            for j in range(CELLS):
                overlap = squared_tensor_overlap(members[first][i], members[second][i],
                                                 members[first][j], members[second][j])
                checked += 1
                if i == j:
                    diagonal += 1
                    if overlap != 1:
                        raise WitnessError("pair_norm", members=[first, second],
                                           cell=coordinates(i), squared_norm=str(overlap))
                else:
                    off_diagonal += 1
                    if i < j:
                        unique_cross += 1
                    if overlap != 0:
                        raise WitnessError("pair_overlap", members=[first, second],
                                           cells=[coordinates(i), coordinates(j)],
                                           squared_overlap=str(overlap))
        results.append({"members": [first, second], "ordered_gram_entries": checked,
                        "diagonal": diagonal, "ordered_off_diagonal": off_diagonal,
                        "unique_cross_grams": unique_cross})
    return results


def check_nonclassical_and_mixed(obj, quantum):
    witness = None
    for i in range(CELLS):
        for j in range(i + 1, CELLS):
            value = squared_overlap(quantum[i], quantum[j])
            if 0 < value < 1:
                witness = {"member": 0, "cells": [coordinates(i), coordinates(j)],
                           "squared_overlap": str(value)}
                break
        if witness is not None:
            break
    if witness is None:
        raise WitnessError("nonclassical_overlap_missing")
    mixed = []
    for index, (numerator, denom) in enumerate(quantum):
        support = [k for k, x in enumerate(numerator) if x != 0]
        if len(support) > 1:
            mixed.append({"index": index, "cell": coordinates(index), "support": support,
                          "basis_squared_overlaps": [str(Fraction(numerator[k] ** 2, denom))
                                                     for k in support]})
    actual_indices = {item["index"] for item in mixed}
    stated_indices = set(obj["trade_cells"])
    if len(mixed) != 8 or actual_indices != stated_indices:
        raise WitnessError("mixed_cells_mismatch", count=len(mixed),
                           actual=sorted(actual_indices), stated=sorted(stated_indices))
    return {"nonclassical_invariant": witness, "mixed_cell_count": len(mixed),
            "mixed_cells": mixed, "trade_cells_match": True}


def verify_witness(data):
    obj = parse_witness(data)
    validate_latin(obj["classical_mates"])
    members = build_vectors(obj)
    lines = check_lines(members)
    grams = check_product_grams(members)
    quantum = check_nonclassical_and_mixed(obj, members[0])
    return obj, {"order": N, "member_count": len(members),
                 "quantum_denominator_squared_values": sorted(set(obj["quantum_square_denominator_squared"])),
                 "classical_latin_rows_checked": 2 * N,
                 "classical_latin_columns_checked": 2 * N,
                 "line_checks": lines, "product_gram_checks": grams, **quantum}


def mutate_swapped_labels(obj):
    row = obj["classical_mates"][0][0]
    row[0], row[1] = row[1], row[0]


def mutate_duplicate_label(obj):
    row = obj["classical_mates"][0][0]
    row[0] = row[1]


def mutate_relabel_member(obj):
    # Globally relabel the FIRST member and use it as the SECOND: both remain
    # Latin, but their joint labels can no longer enumerate all 64 pairs.
    obj["classical_mates"][1] = [[(label + 1) % N for label in row]
                                 for row in obj["classical_mates"][0]]


def mutate_sign(obj):
    obj["quantum_square_numerators"][18][1] *= -1


def mutate_denominator(obj):
    obj["quantum_square_denominator_squared"][18] = 3


def mutate_vector_length(obj):
    obj["quantum_square_numerators"][18].pop()


def mutate_basis_replacement(obj):
    obj["quantum_square_numerators"][18] = [1, 0, 0, 0, 0, 0, 0, 0]
    obj["quantum_square_denominator_squared"][18] = 1


CONTROLS = [
    ("swapped-row-labels", mutate_swapped_labels, "classical_latin_column",
     {"member": 1, "column": 0},
     "Swap columns 0 and 1 in classical member 1, row 0; the row remains a permutation but its column does not."),
    ("duplicate-label", mutate_duplicate_label, "classical_latin_row",
     {"member": 1, "row": 0},
     "Duplicate a label in classical member 1, row 0."),
    ("relabeled-classical-member", mutate_relabel_member, "pair_overlap",
     {"members": [1, 2], "cells": [[0, 0], [1, 3]], "squared_overlap": "1"},
     "Replace classical member 2 by member 1 with every symbol cyclically relabeled; both remain Latin but their product basis fails."),
    ("superposition-sign-flip", mutate_sign, "line_overlap",
     {"member": 0, "axis": "row", "line": 2, "cells": [[2, 2], [2, 3]], "squared_overlap": "1"},
     "Flip the second nonzero coordinate of quantum cell (2,2), making it identical to (2,3)."),
    ("altered-denominator", mutate_denominator, "line_norm",
     {"member": 0, "axis": "row", "line": 2, "cell": [2, 2], "squared_norm": "2/3"},
     "Change quantum cell (2,2)'s squared denominator from 2 to 3."),
    ("truncated-vector", mutate_vector_length, "quantum_vector_length",
     {"cell": [2, 2], "expected": 8, "actual": 7},
     "Remove the last coordinate of quantum cell (2,2)."),
    ("mixed-cell-basis-replacement", mutate_basis_replacement, "line_overlap",
     {"member": 0, "axis": "row", "line": 2, "cells": [[2, 2], [2, 3]], "squared_overlap": "1/2"},
     "Replace quantum cell (2,2) by normalized standard basis vector e0."),
]


def run_controls(obj, receipt):
    controls = receipt["mutation_controls"]
    # Create every fixture before executing any negative control, retaining all
    # of them even if an intended-reason check subsequently fails.
    for name, mutate, code, detail, description in CONTROLS:
        mutated = copy.deepcopy(obj)
        mutate(mutated)
        data = (json.dumps(mutated, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
        filename = "verifier-mutation-" + name + "-v1.json"
        with (HERE / filename).open("xb") as handle:
            handle.write(data)
        stored = (HERE / filename).read_bytes()
        if stored != data:
            raise IntegrityError("fixture differs from written bytes: " + filename)
        controls.append({"fixture": filename, "sha256": digest(stored),
                         "bytes": len(stored), "LF": stored.count(b"\n"),
                         "description": description, "expected_code": code,
                         "expected_detail": detail})
    failures = []
    for result in controls:
        data = (HERE / result["fixture"]).read_bytes()
        if digest(data) != result["sha256"]:
            raise IntegrityError("fixture changed during replay: " + result["fixture"])
        try:
            verify_witness(data)
        except WitnessError as error:
            result["actual_code"] = error.code
            result["actual_detail"] = error.detail
            matching_detail = all(error.detail.get(key) == value
                                  for key, value in result["expected_detail"].items())
            passed = error.code == result["expected_code"] and matching_detail
            result["result"] = "rejected_as_intended" if passed else "wrong_rejection"
        except Exception as error:
            result["result"] = "unexpected_exception"
            result["exception"] = type(error).__name__ + ": " + str(error)
            passed = False
        else:
            result["result"] = "incorrectly_accepted"
            passed = False
        if not passed:
            failures.append(result["fixture"])
    if failures:
        raise ControlError("controls not rejected for their intended reason: " + ", ".join(failures))


def main():
    source = Path(__file__).resolve().read_bytes()
    receipt = {
        "schema_version": 1,
        "kind": "INDEPENDENT_EXACT_THREE_MOQLS_PHYSICAL_VERIFICATION",
        "started_at": now(),
        "command": "python3 -B verifier-check-v1.py",
        "python_executable": sys.executable,
        "python_version": sys.version,
        "bytecode_disabled": sys.dont_write_bytecode,
        "checker": {"path": Path(__file__).name, "sha256": digest(source),
                    "bytes": len(source), "LF": source.count(b"\n")},
        "inputs": {},
        "mutation_controls": [],
        "limitations": [
            "Same-harness verifier independently written from the physical definition; no author code, solver or catalog was used.",
            "No independent-family, human or formal/kernel proof review is asserted.",
            "No claim about M(8), source priority, novelty, a fourth family, or closure of the four-family target follows."
        ],
    }
    exit_code = 1
    try:
        if not sys.dont_write_bytecode:
            raise IntegrityError("run with python3 -B")
        pinned = {}
        for role in ("manifest", "definition", "witness"):
            pinned[role], receipt["inputs"][role] = pinned_bytes(role)
        manifest = json.loads(pinned["manifest"].decode("utf-8"))
        entries = manifest["inputs_in_read_order"]
        for position, role in ((0, "definition"), (1, "witness")):
            expected = PINS[role]
            entry = entries[position]
            if (entry["sha256"], entry["bytes"], entry["LF"]) != expected[1:]:
                raise IntegrityError("manifest does not bind expected " + role + " pin")
            if not entry["path"].endswith("/" + expected[0]):
                raise IntegrityError("manifest path does not bind expected " + role)
        obj, result = verify_witness(pinned["witness"])
        receipt["physical_checks"] = result
        run_controls(obj, receipt)
        receipt["verdict"] = "VALID"
        exit_code = 0
    except WitnessError as error:
        receipt["verdict"] = "INVALID"
        receipt["failure"] = {"code": error.code, "detail": error.detail}
    except Exception as error:
        receipt["verdict"] = "INCONCLUSIVE"
        receipt["failure"] = {"type": type(error).__name__, "message": str(error),
                              "traceback": traceback.format_exc()}
    receipt["recorded_at"] = now()
    output = (json.dumps(receipt, indent=2, ensure_ascii=True) + "\n").encode("utf-8")
    try:
        with (HERE / "verifier-receipt-v1.json").open("xb") as handle:
            handle.write(output)
    except Exception as error:
        print("Receipt could not be created without overwriting: " + str(error), file=sys.stderr)
        print(json.dumps(receipt, indent=2), file=sys.stderr)
        return 1
    print("verdict=" + receipt["verdict"])
    print("recorded_at=" + receipt["recorded_at"])
    print("checker_sha256=" + receipt["checker"]["sha256"])
    if "witness" in receipt["inputs"]:
        print("witness_sha256=" + receipt["inputs"]["witness"]["sha256"])
    print("controls_rejected_as_intended=" + str(sum(
        item.get("result") == "rejected_as_intended" for item in receipt["mutation_controls"])))
    if "failure" in receipt:
        print("failure=" + json.dumps(receipt["failure"], sort_keys=True))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
