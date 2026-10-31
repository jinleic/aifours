from fractions import Fraction as Q
from itertools import combinations
from math import prod
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import os
import resource
import sys
import time


class VerificationError(Exception):
    def __init__(self, code, detail=""):
        self.code = code
        super().__init__(code + (": " + detail if detail else ""))


def need(condition, code, detail=""):
    if not condition:
        raise VerificationError(code, detail)


def sign(x):
    return (x > 0) - (x < 0)


def show(values):
    return "(" + ", ".join(str(x) for x in values) + ")"


def blob(path, expected_sha, expected_bytes, expected_lf):
    try:
        data = path.read_bytes()
    except OSError as error:
        raise VerificationError("INPUT_READ", str(error)) from error
    actual_sha = sha256(data).hexdigest()
    need(actual_sha == expected_sha, "INPUT_SHA256", str(path))
    need(len(data) == expected_bytes, "INPUT_BYTES", str(path))
    need(data.count(b"\n") == expected_lf, "INPUT_LF", str(path))
    print("PIN", str(path), actual_sha, len(data), data.count(b"\n"))
    return data


def record_blob(record):
    return blob(
        Path(record["path"]), record["sha256"],
        record["bytes"], record["LF"]
    )


def verify_frozen_inputs(root):
    expected = (
        ("manifest-v1.json",
         "2355a491094cb32daab714de39a28feff6b0fb5cd1bed5e3b7131cc48c4d964c",
         5750, 80),
        ("freeze-receipt-v1.json",
         "07495b83dfc0622de474a49c303551e249cb132b9982539c24ca0fc3bdf2e9aa",
         1943, 47),
        ("literal-packet-v1.md",
         "b6a7432a6333d4805ed13af4ca87ab58140aaead37a85d8db3bb38675f4b994e",
         43052, 959),
    )
    data = {}
    for name, digest, size, lf in expected:
        data[name] = blob(root / name, digest, size, lf)
    manifest = json.loads(data["manifest-v1.json"])
    receipt = json.loads(data["freeze-receipt-v1.json"])
    need(receipt["manifest"]["sha256"] == expected[0][1],
         "RECEIPT_MANIFEST")
    need(receipt["packet"]["sha256"] == expected[2][1],
         "RECEIPT_PACKET")
    need([item["id"] for item in manifest["inputs"]] == ["S1", "S2"],
         "INPUT_ORDER")
    for item in manifest["controls_before_body"]:
        record_blob(item)
    rendered = ["# Frozen prospective author inputs\n\n"]
    for item in manifest["inputs"]:
        source = record_blob(item).decode("utf-8")
        lines = source.split("\n")
        first, last = item["allowed_lines"]
        need(1 <= first <= last <= len(lines), "SOURCE_RANGE")
        for number in range(first, last + 1):
            rendered.append(
                item["id"] + "|" + str(number) + "|" +
                lines[number - 1] + "\n"
            )
    need("".join(rendered).encode("utf-8") == data["literal-packet-v1.md"],
         "PACKET_LITERAL_ROUNDTRIP")
    print("PACKET_LITERAL_ROUNDTRIP=PASS")


# Literal original polynomial coefficients, ascending powers of s.
C = (Q(4), Q(15), Q(11), Q(23), Q(13, 2), Q(9), Q(1), Q(1))
U = (Q(27, 30), Q(28, 30), Q(29, 30),
     Q(30, 30), Q(31, 30), Q(32, 30))
D = (Q(-961, 1000), Q(-3107, 6750), Q(-10081, 27000),
     Q(1, 10), Q(4321, 27000), Q(4097, 6750))
EVEN_POLY = tuple(((-1) ** k) * C[2 * k] for k in range(4))


def poly_mul(p, q):
    result = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return tuple(result)


def poly_value(p, t):
    result = Q(0)
    for coefficient in reversed(p):
        result = result * t + coefficient
    return result


def poly_derivative(p):
    return tuple(Q(k) * p[k] for k in range(1, len(p)))


def parity(delta, t):
    even = sum((C[2 * k] * (-t) ** k for k in range(4)), Q(0))
    odd = delta + sum(
        (C[2 * k + 1] * (-t) ** k for k in range(4)), Q(0)
    )
    return even, odd


def raw_row(delta, t):
    even, odd = parity(delta, t)
    # Re(s^(2k) conjugate(a)) = (-t)^k E.
    # Re(s^(2k+1) conjugate(a)) = t (-t)^k O at s=i*sqrt(t).
    return tuple(
        ((-t) ** (j // 2)) * (even if j % 2 == 0 else t * odd)
        for j in range(8)
    )


def aggregate(weights):
    need(len(weights) == 6, "WEIGHT_LENGTH")
    return tuple(
        sum((weights[i] * raw_row(D[i], U[i])[j]
             for i in range(6)), Q(0))
        for j in range(8)
    )


def hb_interval(lo, hi):
    need(lo <= hi, "PARAMETER_INTERVAL")
    roots = (Q(1, 2), Q(2), Q(4))
    factorized = (Q(1),)
    for root in roots:
        factorized = poly_mul(factorized, (root, Q(-1)))
    need(factorized == EVEN_POLY, "EVEN_FACTORIZATION")
    need(C[0] > 0 and C[6] > 0 and C[7] == 1,
         "HB_LEADING_ORIENTATION")
    probes = ((Q(0), 1), (Q(1, 2), 1),
              (Q(2), -1), (Q(4), 1), (Q(6), -1))
    bounds = []
    for t, wanted in probes:
        base = parity(Q(0), t)[1]
        lower, upper = base + lo, base + hi
        strict = lower > 0 if wanted == 1 else upper < 0
        need(strict, "HB_SIGN_" + str(t), show((lower, upper)))
        bounds.append((t, lower, upper))
    derivative = poly_derivative(EVEN_POLY)
    for root in roots:
        slope = poly_value(derivative, root)
        lower = parity(lo, root)[1]
        upper = parity(hi, root)[1]
        need(slope * lower < 0 and slope * upper < 0,
             "HB_ORIENTATION", str(root))
    return tuple(bounds)


def selected_values(deltas):
    need(len(deltas) == 6, "PARAMETER_LENGTH")
    for i, delta in enumerate(deltas):
        need(Q(-1) <= delta <= Q(1),
             "ACTUAL_BOX", str(i + 1) + ": " + str(delta))
    evens, odds = [], []
    for i, (t, delta) in enumerate(zip(U, deltas)):
        even, odd = parity(delta, t)
        wanted = Q(-1 if i % 2 == 0 else 1, 10)
        need(odd == wanted, "ODD_VALUE",
             str(i + 1) + ": " + str(odd))
        evens.append(even)
        odds.append(odd)
    return tuple(evens), tuple(odds)


def node_derivatives(nodes):
    need(all(t > 0 for t in nodes), "POSITIVE_NODE")
    need(all(nodes[i] < nodes[i + 1] for i in range(len(nodes) - 1)),
         "NODE_ORDER")
    polynomial = (Q(1),)
    for t in nodes:
        polynomial = poly_mul(polynomial, (-t, Q(1)))
    derivative = poly_derivative(polynomial)
    values = tuple(poly_value(derivative, t) for t in nodes)
    direct = tuple(
        prod((t - other for j, other in enumerate(nodes) if j != i),
             start=Q(1))
        for i, t in enumerate(nodes)
    )
    need(values == direct, "DERIVATIVE_PRODUCT")
    need(all(x != 0 for x in values), "NONZERO_DERIVATIVE")
    return polynomial, values


def odd_moments(weights, odds):
    need(len(weights) == len(odds) == 6, "MOMENT_LENGTH")
    return tuple(
        sum((weights[i] * U[i] * odds[i] * (-U[i]) ** r
             for i in range(6)), Q(0))
        for r in range(4)
    )


def positive_weights(weights):
    need(all(weight > 0 for weight in weights), "POSITIVE_WEIGHT")


def zero_odd_moments(weights, odds):
    values = odd_moments(weights, odds)
    for r, value in enumerate(values):
        need(value == 0, "ODD_MOMENT_" + str(r), str(value))
    return values


def matrix_rank(matrix):
    if not matrix:
        return 0
    a = [[Q(x) for x in row] for row in matrix]
    row = 0
    for column in range(len(a[0])):
        if row == len(a):
            break
        pivot = next(
            (r for r in range(row, len(a)) if a[r][column] != 0), None
        )
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][column]
        a[row] = [x / scale for x in a[row]]
        for r in range(len(a)):
            if r != row:
                scale = a[r][column]
                a[r] = [x - scale * y for x, y in zip(a[r], a[row])]
        row += 1
    return row


def moment_matrix(support, odds):
    return [
        [U[i] * odds[i] * (-U[i]) ** r for i in support]
        for r in range(4)
    ]


def five_ray(support, orientation, odds):
    need(len(support) == 5, "RAY_SUPPORT")
    need(orientation in (-1, 1), "RAY_ORIENTATION")
    need(matrix_rank(moment_matrix(support, odds)) == 4, "RAY_RANK")
    nodes = tuple(U[i] for i in support)
    _, derivatives = node_derivatives(nodes)
    need(
        all(sign(odds[i]) == orientation * sign(derivatives[j])
            for j, i in enumerate(support)),
        "RAY_ORIENTATION",
        str(tuple(i + 1 for i in support)) + ": " + str(orientation)
    )
    weights = [Q(0)] * 6
    for j, i in enumerate(support):
        weights[i] = Q(orientation) / (U[i] * odds[i] * derivatives[j])
    need(all(weights[i] > 0 for i in support), "RAY_POSITIVE_WEIGHT")
    zero_odd_moments(weights, odds)
    need(all(aggregate(weights)[2 * r + 1] == 0 for r in range(4)),
         "RAY_RAW_ODD_COORDINATES")
    return tuple(weights)


def check_decomposition(target, left, right, multiplier):
    candidate = tuple(multiplier * (x + y) for x, y in zip(left, right))
    need(candidate == target, "DECOMPOSITION", show(candidate))


def check_first_coordinate(target, proposed):
    need(target[0] == proposed[0], "FROZEN_FIRST_COORDINATE",
         str(target[0]) + " != " + str(proposed[0]))


def expected_failure(label, wanted_code, action):
    try:
        action()
    except VerificationError as error:
        need(error.code == wanted_code, "WRONG_MUTATION_FAILURE",
             label + ": " + str(error))
        print("EXPECTED_FAILURE", label, str(error))
        return 1
    raise VerificationError("MUTATION_ACCEPTED", label)


def main():
    need(len(sys.argv) == 2, "ARGV", "verifier.py FROZEN_WAVE_DIRECTORY")
    started = time.perf_counter()
    print("RUN_START_UTC", datetime.now(timezone.utc).isoformat())
    print("PID", os.getpid(), "PGID", os.getpgid(0))
    print("PYTHON", sys.version.splitlines()[0])
    print("EXECUTABLE", sys.executable)
    print("ARGV", repr(sys.argv))
    print("SELF_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
    verify_frozen_inputs(Path(sys.argv[1]))
    need(time.perf_counter() - started < 60, "TIME_BOUND")

    bounds = hb_interval(Q(-1), Q(1))
    need(bounds == (
        (Q(0), Q(14), Q(16)),
        (Q(1, 2), Q(37, 8), Q(53, 8)),
        (Q(2), Q(-4), Q(-2)),
        (Q(4), Q(2), Q(4)),
        (Q(6), Q(-16), Q(-14)),
    ), "HB_EXACT_BOUNDS")
    for t, lower, upper in bounds:
        print("HB_INTERVAL", str(t), str(lower), str(upper))
    print("HB_EXACT_INTERVAL_HYPOTHESES=PASS")
    print("HURWITZ_CONCLUSION_USES_CLASSICAL_HERMITE_BIEHLER")

    evens, odds = selected_values(D)
    polynomial, derivatives = node_derivatives(U)
    weights = tuple(
        Q(1) / (U[i] * odds[i] * derivatives[i]) for i in range(6)
    )
    positive_weights(weights)
    need(weights == (
        Q(2250000), Q(75937500, 7), Q(607500000, 29),
        Q(20250000), Q(303750000, 31), Q(3796875, 2)
    ), "SIX_WEIGHT_VALUES")
    need(derivatives == (
        Q(-1, 202500), Q(1, 1012500), Q(-1, 2025000),
        Q(1, 2025000), Q(-1, 1012500), Q(1, 202500)
    ), "SIX_DERIVATIVE_VALUES")
    print("H6_ASCENDING_COEFFICIENTS", show(polynomial))
    for i in range(6):
        print("ATOM", i + 1, "t=" + str(U[i]), "delta=" + str(D[i]),
              "E=" + str(evens[i]), "O=" + str(odds[i]),
              "Hprime=" + str(derivatives[i]), "mu=" + str(weights[i]))
    lagrange = tuple(
        sum((U[i] ** k / derivatives[i] for i in range(6)), Q(0))
        for k in range(6)
    )
    need(lagrange == (Q(0), Q(0), Q(0), Q(0), Q(0), Q(1)),
         "SIX_LAGRANGE_IDENTITIES")
    print("SIX_LAGRANGE_SUMS_POWERS_0_TO_5", show(lagrange))
    moments = zero_odd_moments(weights, odds)
    raw = aggregate(weights)
    need(tuple(raw[2 * r + 1] for r in range(4)) == moments,
         "RAW_ODD_MOMENT_AGREEMENT")
    signs = tuple(sign(value) for value in raw)
    need(signs == (-1, 0, 1, 0, -1, 0, 1, 0), "AGGREGATE_SIGNS")
    need(not all(value < 0 for value in raw), "STRICT_CERTIFICATE_STATUS")
    print("ODD_SIGNED_MOMENTS", show(moments))
    print("RAW_AGGREGATE", show(raw))
    print("RAW_AGGREGATE_SIGNS", show(signs))
    print("STRICT_NEGATIVE_CERTIFICATE=False")

    short_support_count = 0
    for size in range(1, 5):
        for support in combinations(range(6), size):
            need(matrix_rank(moment_matrix(support, odds)) == size,
                 "SHORT_SUPPORT_RANK", str(support))
            short_support_count += 1
    need(short_support_count == 56, "SHORT_SUPPORT_COUNT")
    print("FULL_COLUMN_RANK_SUPPORTS_OF_SIZE_1_TO_4", short_support_count)

    admissible = {1: [], -1: []}
    positive_first_rays = []
    for support in combinations(range(6), 5):
        need(matrix_rank(moment_matrix(support, odds)) == 4,
             "FIVE_SUBSET_RANK")
        _, dp = node_derivatives(tuple(U[i] for i in support))
        orientations = tuple(
            epsilon for epsilon in (-1, 1)
            if all(sign(odds[i] * dp[j]) == epsilon
                   for j, i in enumerate(support))
        )
        print("FIVE_SUBSET", tuple(i + 1 for i in support),
              "ODD_SIGNS", tuple(sign(odds[i]) for i in support),
              "ADMISSIBLE_ORIENTATIONS", orientations)
        for epsilon in orientations:
            ray = five_ray(support, epsilon, odds)
            admissible[epsilon].append(support)
            if epsilon == 1:
                positive_first_rays.append(ray)
    need(admissible[1] == [(1, 2, 3, 4, 5)],
         "POSITIVE_FIRST_EXHAUSTION")
    need(admissible[-1] == [(0, 1, 2, 3, 4)],
         "NEGATIVE_FIRST_EXHAUSTION")

    left = five_ray((0, 1, 2, 3, 4), -1, odds)
    right = five_ray((1, 2, 3, 4, 5), 1, odds)
    need(left == (
        Q(375000), Q(10125000, 7), Q(60750000, 29),
        Q(1350000), Q(10125000, 31), Q(0)
    ), "LEFT_RAY_VALUES")
    need(right == (
        Q(0), Q(2531250, 7), Q(40500000, 29),
        Q(2025000), Q(40500000, 31), Q(1265625, 4)
    ), "RIGHT_RAY_VALUES")
    length = U[-1] - U[0]
    need(length == Q(1, 6), "ENDPOINT_DISTANCE")
    need(left == tuple((U[-1] - U[i]) * weights[i] for i in range(6)),
         "LEFT_DERIVATIVE_RELATION")
    need(right == tuple((U[i] - U[0]) * weights[i] for i in range(6)),
         "RIGHT_DERIVATIVE_RELATION")
    check_decomposition(weights, left, right, Q(1) / length)
    need(matrix_rank(moment_matrix(tuple(range(6)), odds)) == 4,
         "SIX_MOMENT_RANK")
    need(matrix_rank([left, right]) == 2, "TWO_KERNEL_DIRECTIONS")
    need(left[0] > 0 and left[-1] == 0 and
         right[0] == 0 and right[-1] > 0, "CONE_ENDPOINT_STRUCTURE")
    need(weights[0] > 0 and
         all(ray[0] == 0 for ray in positive_first_rays),
         "W1_FIRST_COORDINATE_OBSTRUCTION")
    print("LEFT_NEGATIVE_FIRST_RAY", show(left))
    print("LEFT_ODD_MOMENTS", show(odd_moments(left, odds)))
    print("RIGHT_POSITIVE_FIRST_RAY", show(right))
    print("RIGHT_ODD_MOMENTS", show(odd_moments(right, odds)))
    print("DECOMPOSITION_MULTIPLIERS", show((Q(6), Q(6))))
    print("TARGET_FIRST_COORDINATE", weights[0])
    print("ALL_POSITIVE_FIRST_RAYS_FIRST_COORDINATE=0")
    print("W1_ONLY_FROZEN_DATA_BRIDGE=FALSE")

    outside_delta = (Q(-1001, 1000),) + D[1:]
    shifted_delta = (D[0] + Q(1, 1000),) + D[1:]
    incremented_weight = (weights[0] + Q(1),) + weights[1:]
    negative_weight = (-weights[0],) + weights[1:]
    need(odd_moments(incremented_weight, odds)[0] == Q(-9, 100),
         "WEIGHT_MUTATION_EXACT_EFFECT")
    controls = (
        ("delta_outside_box", "ACTUAL_BOX",
         lambda: selected_values(outside_delta)),
        ("delta_wrong_odd_value", "ODD_VALUE",
         lambda: selected_values(shifted_delta)),
        ("weight_increment", "ODD_MOMENT_0",
         lambda: zero_odd_moments(incremented_weight, odds)),
        ("weight_sign", "POSITIVE_WEIGHT",
         lambda: positive_weights(negative_weight)),
        ("left_wrong_orientation", "RAY_ORIENTATION",
         lambda: five_ray((0, 1, 2, 3, 4), 1, odds)),
        ("right_wrong_orientation", "RAY_ORIENTATION",
         lambda: five_ray((1, 2, 3, 4, 5), -1, odds)),
        ("expanded_parameter_interval", "HB_SIGN_2",
         lambda: hb_interval(Q(-1), Q(3))),
        ("wrong_decomposition_multiplier", "DECOMPOSITION",
         lambda: check_decomposition(weights, left, right, Q(5))),
        ("W1_only_reconstruction", "FROZEN_FIRST_COORDINATE",
         lambda: check_first_coordinate(
             weights, tuple(Q(6) * value for value in right))),
    )
    rejected = sum(expected_failure(*control) for control in controls)
    need(rejected == 9, "MUTATION_COUNT")
    print("INTENDED_REASON_MUTATIONS_REJECTED", rejected)

    elapsed = time.perf_counter() - started
    need(elapsed < 60, "TIME_BOUND", str(elapsed))
    maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    maxrss_bytes = int(maxrss if sys.platform == "darwin" else maxrss * 1024)
    print("ELAPSED_SECONDS", format(elapsed, ".9f"))
    print("MAXRSS_BYTES", maxrss_bytes)
    print("RUN_END_UTC", datetime.now(timezone.utc).isoformat())
    print("SCOPE=EXACT_FINITE_CHECK_PLUS_WRITTEN_CLASSICAL_HB")
    print("NO_GLOBAL_CERTIFICATE_OR_STRICT_SPR_OR_NOVELTY_CLAIM")
    print("RESULT=PASS")


if __name__ == "__main__":
    try:
        main()
    except VerificationError as error:
        print("RESULT=FAIL", str(error), file=sys.stderr)
        raise SystemExit(1)
