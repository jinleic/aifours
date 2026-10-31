#!/usr/bin/env python3
"""UNRUN candidate: replay only six frozen emitted-pencil certificates.

No command-line inputs, writes, subprocesses, network, or imports of producer code.
A parent must whole-read and separately authorize this exact source before running.
The internal wall-clock alarm is 40 seconds; the parent must impose an external
bound of at most 55 seconds and retain stdout, stderr, status, and timing.
"""

import copy
import hashlib
import json
import math
import re
import signal
import sys


ROOT = "/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-six-symbolic-minor-dossiers-v1/"
# The source may explicitly read only these six files, once each.
INPUTS = (
    ("weight-1-2.json", "945d4dd07897fd9fdc24bc6c44b71aa16a8c6aabf98417f06f0e0e726ce4ae1f", ("1", "2"), ("4", "1"), 4, True),
    ("weight-2-1.json", "73507164325c2d489753b4b578dda12336044b3b3f409e08e88d65efb10502f0", ("2", "1"), ("1", "4"), 4, True),
    ("weight-2-2.json", "5e1f7c3c83ad9b1be8bd393460f278d3a615000ebd1506d08ecae5ea2d663b55", ("2", "2"), ("2", "2"), 7, True),
    ("weight-2-3.json", "a4ba7e05a07cf9e69c7b52a72261f79d98147f96630c8a2bc06fa91c7ed64a0a", ("2", "3"), ("3", "0"), 6, False),
    ("weight-3-2.json", "0467fbf56e335ec150419bb7bde6e7149a1eb99783081b2a87b1ef3a5d2dd29b", ("3", "2"), ("0", "3"), 6, False),
    ("weight-3-3-compact.json", "757dc7ca0390aa9bd658e1ed888b1b710a9755887833653f94d3670097ebd3c7", ("3", "3"), ("1", "1"), 8, False),
)
DECIMAL = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z")


class Reject(Exception):
    def __init__(self, reason, detail):
        super().__init__(detail)
        self.reason = reason
        self.detail = detail


def fail(reason, detail):
    raise Reject(reason, detail)


def expired(_signum, _frame):
    fail("TIMEOUT", "internal 40-second alarm")


def bad_number(_text):
    fail("FORMAT", "floating-point or non-finite JSON number")


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            fail("FORMAT", "duplicate JSON object key: " + key)
        out[key] = value
    return out


def decimal(value, where):
    if not isinstance(value, str) or DECIMAL.fullmatch(value) is None:
        fail("FORMAT", "noncanonical decimal string at " + where)
    return int(value)


def sparse(vector, where):
    # Earlier dossiers use objects; later ones use arrays of [word, value].
    if isinstance(vector, dict):
        pairs = vector.items()
    elif isinstance(vector, list):
        pairs = vector
    else:
        fail("FORMAT", "sparse vector is neither object nor pair list at " + where)
    result = {}
    for pair in pairs:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            fail("FORMAT", "bad sparse pair at " + where)
        word, value = pair
        if not isinstance(word, str) or not word or word in result:
            fail("FORMAT", "bad or duplicate sparse word at " + where)
        result[word] = decimal(value, where + "/" + word)
    return result


def columns(value, n, where):
    if not isinstance(value, list) or len(value) != n:
        fail("FORMAT", "wrong vector count at " + where)
    return [sparse(vector, where + "/" + str(j)) for j, vector in enumerate(value)]


def square_matrix(value, n, where):
    if not isinstance(value, list) or len(value) != n:
        fail("FORMAT", "wrong matrix height at " + where)
    out = []
    for row in value:
        if not isinstance(row, list) or len(row) != n:
            fail("FORMAT", "wrong matrix width at " + where)
        out.append([decimal(entry, where) for entry in row])
    return out


def from_columns(rows, cols):
    return [[col.get(word, 0) for col in cols] for word in rows]


def check_binding(rows, a, b, constant, slope):
    if a != from_columns(rows, constant) or b != from_columns(rows, slope):
        fail("ROW_BINDING", "selected matrix differs from row-labeled full column families")


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def polynomial_determinant(a, b):
    # Multilinear Leibniz expansion, accumulated by the set of used columns.
    # Appending column j creates one inversion for each used column > j.
    n = len(a)
    dp = {0: [1]}
    for row in range(n):
        nxt = {}
        for mask, poly in dp.items():
            for col in range(n):
                bit = 1 << col
                if mask & bit or (a[row][col] == 0 and b[row][col] == 0):
                    continue
                inversions = bin(mask >> (col + 1)).count("1")
                sign = -1 if inversions % 2 else 1
                target = nxt.setdefault(mask | bit, [0] * (row + 2))
                for degree, coefficient in enumerate(poly):
                    target[degree] += sign * coefficient * a[row][col]
                    target[degree + 1] += sign * coefficient * b[row][col]
        dp = nxt
    return trim(dp.get((1 << n) - 1, [0]))


def integer_rank(rows, n):
    # Exact row elimination. Dividing a row by its gcd is an invertible rational
    # scaling; no floating point, interpolation, or determinant calculation.
    matrix = [row[:] for row in rows]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        p = matrix[rank][col]
        for i in range(rank + 1, len(matrix)):
            q = matrix[i][col]
            if q == 0:
                continue
            matrix[i] = [p * u - q * v for u, v in zip(matrix[i], matrix[rank])]
            divisor = 0
            for value in matrix[i]:
                divisor = math.gcd(divisor, value)
            if divisor > 1:
                matrix[i] = [value // divisor for value in matrix[i]]
        rank += 1
        if rank == n:
            break
    return rank


def coefficient_list(value, n, where):
    if not isinstance(value, list) or not 1 <= len(value) <= n + 1:
        fail("FORMAT", "bad determinant coefficient count at " + where)
    result = [decimal(entry, where) for entry in value]
    if len(result) > 1 and result[-1] == 0:
        fail("FORMAT", "noncanonical trailing determinant zero at " + where)
    return result


def check_coefficients(cert, raw, n, explicit_normalization):
    if raw[0] == 0:
        fail("ZERO_CONSTANT", "computed determinant constant is zero")
    if explicit_normalization:
        multiplier = decimal(cert["determinant_normalization_multiplier"], "multiplier")
        if multiplier not in (-1, 1) or multiplier * raw[0] <= 0:
            fail("BAD_SIGN", "normalization multiplier does not make raw constant positive")
        claimed = coefficient_list(cert["normalized_determinant_coefficients_low_to_high"], n, "normalized")
        normalized = [multiplier * value for value in raw]
        if claimed != normalized:
            fail("DET_COEFFICIENTS", "normalized coefficients differ from exact determinant")
    else:
        claimed = coefficient_list(cert["determinant_coefficients_ascending_in_t"], n, "raw")
        if claimed[0] == 0 or (claimed[0] > 0) != (raw[0] > 0):
            fail("BAD_SIGN", "reported raw determinant has wrong constant sign")
        if claimed != raw:
            fail("DET_COEFFICIENTS", "raw coefficients differ from exact determinant")
        multiplier = 1 if raw[0] > 0 else -1
        normalized = [multiplier * value for value in raw]
    if normalized[0] <= 0 or any(value < 0 for value in normalized):
        fail("NONNEGATIVE", "normalized coefficients do not have the required sign")
    return multiplier, normalized


def expect(reason, operation):
    try:
        operation()
    except Reject as exc:
        if exc.reason != reason:
            fail("CONTROL_WRONG_REASON", "expected " + reason + ", received " + exc.reason)
        return reason
    fail("CONTROL_SURVIVED", "expected " + reason)


def replay(item):
    filename, expected_hash, weight, label, n, explicit = item
    path = ROOT + filename
    with open(path, "rb") as stream:
        raw_bytes = stream.read()
    actual_hash = hashlib.sha256(raw_bytes).hexdigest()
    if actual_hash != expected_hash:
        fail("INPUT_HASH", path + " expected=" + expected_hash + " actual=" + actual_hash)
    doc = json.loads(raw_bytes.decode("utf-8"), object_pairs_hook=unique_object,
                     parse_float=bad_number, parse_constant=bad_number)
    if doc["kind"] != "CAPTURED_COMPLETE_LOWEST_PENCIL_CERTIFICATE":
        fail("FORMAT", "wrong dossier kind")
    if tuple(doc["weight"]) != weight or tuple(doc["label"]) != label:
        fail("IDENTITY", "unexpected weight or label in " + filename)
    if decimal(doc["multiplicity"], "multiplicity") != n:
        fail("IDENTITY", "unexpected multiplicity in " + filename)
    # Parse every emitted tensor and both complete column families, not just rows.
    columns(doc["lowest_tensors"], n, "lowest_tensors")
    constant = columns(doc["constant_columns"], n, "constant_columns")
    slope = columns(doc["coefficient_columns"], n, "coefficient_columns")
    cert = doc["certificate"]
    if not explicit and (tuple(cert["weight"]) != weight or tuple(cert["type"]) != label):
        fail("IDENTITY", "certificate weight/type mismatch in " + filename)
    rows = cert["rows"] if explicit else cert["tensor_rows"]
    if (not isinstance(rows, list) or len(rows) != n or
            any(not isinstance(row, str) or not row for row in rows) or len(set(rows)) != n):
        fail("ROW_BINDING", "invalid selected row labels in " + filename)
    support = set().union(*(set(col) for col in constant + slope))
    if not set(rows).issubset(support):
        fail("ROW_BINDING", "selected row absent from full emitted column support")
    if explicit:
        a = square_matrix(cert["matrix_constant_s4"], n, "matrix_constant_s4")
        b = square_matrix(cert["matrix_shift_coefficient"], n, "matrix_shift_coefficient")
        binding_mode = "emitted matrices checked against full columns"
    else:
        a = from_columns(rows, constant)
        b = from_columns(rows, slope)
        binding_mode = "matrix reconstructed from row labels and full columns; no separate emitted matrix"
    check_binding(rows, a, b, constant, slope)
    determinant = polynomial_determinant(a, b)
    multiplier, normalized = check_coefficients(cert, determinant, n, explicit)

    all_rows = sorted(support)
    a_all = from_columns(all_rows, constant)
    b_all = from_columns(all_rows, slope)
    rank4 = integer_rank(a_all, n)
    rank5 = integer_rank([[u + v for u, v in zip(arow, brow)]
                          for arow, brow in zip(a_all, b_all)], n)
    if rank4 != n or rank5 != n:
        fail("RANK", "full column family rank at s=4 or s=5 is not multiplicity")

    controls = {}
    changed_coefficient = copy.deepcopy(cert)
    coefficient_key = ("normalized_determinant_coefficients_low_to_high" if explicit
                       else "determinant_coefficients_ascending_in_t")
    old = decimal(changed_coefficient[coefficient_key][0], "control coefficient")
    changed_coefficient[coefficient_key][0] = str(old + (1 if old > 0 else -1))
    controls["coefficient_corruption"] = expect(
        "DET_COEFFICIENTS", lambda: check_coefficients(changed_coefficient, determinant, n, explicit))

    changed_sign = copy.deepcopy(cert)
    if explicit:
        changed_sign["determinant_normalization_multiplier"] = str(-multiplier)
    else:
        changed_sign[coefficient_key] = [str(-decimal(value, "control sign"))
                                         for value in changed_sign[coefficient_key]]
    controls["sign_corruption"] = expect(
        "BAD_SIGN", lambda: check_coefficients(changed_sign, determinant, n, explicit))

    changed_a = [row[:] for row in a]
    changed_a[0][0] += 1
    controls["matrix_entry_row_binding_corruption"] = expect(
        "ROW_BINDING", lambda: check_binding(rows, changed_a, b, constant, slope))
    changed_rows = rows[:]
    changed_rows[0], changed_rows[1] = changed_rows[1], changed_rows[0]
    if explicit:
        controls["row_label_swap"] = expect(
            "ROW_BINDING", lambda: check_binding(changed_rows, a, b, constant, slope))
    else:
        swapped_det = polynomial_determinant(from_columns(changed_rows, constant),
                                             from_columns(changed_rows, slope))
        controls["row_label_swap"] = expect(
            "BAD_SIGN", lambda: check_coefficients(cert, swapped_det, n, False))

    return {
        "input": path,
        "input_sha256": actual_hash,
        "weight": list(weight),
        "label": list(label),
        "multiplicity": str(n),
        "rows_in_order": rows,
        "row_binding_mode": binding_mode,
        "raw_determinant_coefficients_low_to_high": [str(value) for value in determinant],
        "normalization_multiplier": str(multiplier),
        "normalization_origin": "emitted" if explicit else "derived from raw constant sign",
        "normalized_determinant_coefficients_low_to_high": [str(value) for value in normalized],
        "full_column_rank_s4": str(rank4),
        "full_column_rank_s5": str(rank5),
        "intended_reason_controls": controls,
    }


def main():
    if len(sys.argv) != 1:
        fail("ARGUMENTS", "this replay takes no arguments")
    signal.signal(signal.SIGALRM, expired)
    signal.alarm(40)
    try:
        results = [replay(item) for item in INPUTS]
    finally:
        signal.alarm(0)
    print(json.dumps({
        "status": "REPLAY_COMPLETE",
        "method": "exact subset-accumulated multilinear determinant and independent integer rank",
        "scope": "emitted pencil certificates only; not source, quotient, tensor provenance, or union verification",
        "results": results,
    }, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    try:
        main()
    except Reject as exc:
        print("REPLAY_REJECT " + exc.reason + ": " + exc.detail, file=sys.stderr)
        sys.exit(1)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print("REPLAY_ERROR " + type(exc).__name__ + ": " + str(exc), file=sys.stderr)
        sys.exit(1)
