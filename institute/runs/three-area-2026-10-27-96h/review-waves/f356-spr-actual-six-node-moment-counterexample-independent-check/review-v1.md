# f356 independent finite verification

**Disposition: the scoped finite mathematical claims are correct by written exact verification. The supplied verifier is NOTRUN.**

No Python, CAS, numerical-root calculation, scientific executable, or filesystem write was performed. The review-role Bash whitelist does not permit Python execution; I did not use another transport to bypass that restriction. The complete standalone source and intended argv are supplied below for parent inspection, materialization, freezing, and execution.

This return checks **S1 §7’s actual one-parameter box, six-node example, both five-node orientations, and the failure of the specified frozen-data W1-only bridge**. It does not accept S1’s separate universal reduction theorem, produce a strict-negative certificate, settle the original all-box question, synthesize a strict SPR numerator, or establish novelty.

## 1. Inputs, exposure, and chronology

I read:

- The complete f356 manifest and freeze receipt.
- All six named permission/quarantine controls, including their endings. Their linked held scientific payloads were not opened.
- The entire literal packet, including S1’s ending and all of S2, in physical windows **1–180, 181–360, 361–540, 541–720, 721–880, 881–959**.
- The complete parent metadata supply.

The opening packet window was read concurrently with the manifest/receipt, before the six controls. The controls and the entire packet were nevertheless read before scientific conclusions. I do not claim a stricter controls-before-first-body-access chronology.

No author checker, sibling review, historical held mathematical payload, or linked earlier review was read.

The following matching hashes and byte/LF counts are **parent-observed metadata, not my hash executions**:

| Item | SHA-256 |
|---|---|
| Manifest | `2355a491094cb32daab714de39a28feff6b0fb5cd1bed5e3b7131cc48c4d964c` |
| Receipt | `07495b83dfc0622de474a49c303551e249cb132b9982539c24ca0fc3bdf2e9aa` |
| Packet | `b6a7432a6333d4805ed13af4ca87ab58140aaead37a85d8db3bb38675f4b994e` |
| S1 | `bf4af736bc4e85355cd5682ecc14ee2f00ed39f8d8d440f724bfa601f3ee7353` |
| S2 | `a4f1f48c3521a8b4a5635aa861f9a5afbb9d6f6e5ea7ead79d8183be5308788b` |

Parent supplied observations **2026-10-30T09:06:30-0700 PDT** and **2026-10-30T09:13:03-0700 PDT**. Neither is asserted as my native start, completion, private calculation, or execution time.

## 2. Exact proof for the whole parameter interval

The literal polynomial is
\[
a_\delta(s)=s^7+s^6+9s^5+\frac{13}{2}s^4
+23s^3+11s^2+(15+\delta)s+4,\qquad \delta\in[-1,1].
\]

Writing \(a_\delta(i\omega)=E(t)+i\omega O_\delta(t)\), \(t=\omega^2\), gives
\[
E(t)=\left(\frac12-t\right)(2-t)(4-t),
\qquad
O_\delta(t)=(1-t)(3-t)(5-t)+\delta.
\]

The following are **interval evaluations over every \(\delta\in[-1,1]\)**, not sampled parameter values or sampled roots:

| \(t\) | Exact range of \(O_\delta(t)\) |
|---|---|
| \(0\) | \([14,16]\) |
| \(1/2\) | \([37/8,53/8]\) |
| \(2\) | \([-4,-2]\) |
| \(4\) | \([2,4]\) |
| \(6\) | \([-16,-14]\) |

Thus every \(O_\delta\) has a root in each of
\[
(1/2,2),\qquad (2,4),\qquad (4,6).
\]
These intervals are disjoint. A cubic with a root in each has exactly those three distinct roots, all simple.

Together with the simple even roots \(1/2,2,4\), this gives
\[
0<e_1<o_1<e_2<o_2<e_3<o_3.
\]
The orientation is the Hurwitz one: \(a_0=4>0\), \(a_6=a_7=1>0\), and
\[
E'(1/2)=-21/4,\quad E'(2)=3,\quad E'(4)=-7,
\]
so \(E'(e_j)O_\delta(e_j)<0\) throughout the parameter interval.

By the stated classical Hermite–Biehler interface, **every actual member of this entire independent coefficient box is strictly Hurwitz**. No approximate roots are needed.

## 3. Exact six-node data and positive weights

The literal nodes and parameters give the following exact values. The derivatives and weights below are written reconstructions, **not observed program output**.

| \(i\) | \(u_i\) | \(\delta_i\) | \(O_{\delta_i}(u_i)\) | \(H_6'(u_i)\) | \(\mu_i\) |
|---|---:|---:|---:|---:|---:|
| 1 | \(9/10\) | \(-961/1000\) | \(-1/10\) | \(-1/202500\) | \(2250000\) |
| 2 | \(14/15\) | \(-3107/6750\) | \(1/10\) | \(1/1012500\) | \(75937500/7\) |
| 3 | \(29/30\) | \(-10081/27000\) | \(-1/10\) | \(-1/2025000\) | \(607500000/29\) |
| 4 | \(1\) | \(1/10\) | \(1/10\) | \(1/2025000\) | \(20250000\) |
| 5 | \(31/30\) | \(4321/27000\) | \(-1/10\) | \(-1/1012500\) | \(303750000/31\) |
| 6 | \(16/15\) | \(4097/6750\) | \(1/10\) | \(1/202500\) | \(3796875/2\) |

Every parameter is strictly between \(-1\) and \(1\). For
\[
H_6(t)=\prod_{i=1}^6(t-u_i),
\]
the formula
\[
H_6'(u_i)=30^{-5}(-1)^i(i-1)!(6-i)!
\]
follows directly by multiplying the five nonzero node differences. Its sign matches \(O_{\delta_i}(u_i)\), so
\[
\mu_i=\frac{1}{u_iO_{\delta_i}(u_i)H_6'(u_i)}>0.
\]

## 4. All four odd moments and all eight aggregate signs

Deriving the row directly from the numerator monomials gives
\[
r_{2k}(a,t)=(-t)^kE_a(t),\qquad
r_{2k+1}(a,t)=t(-t)^kO_a(t),\quad k=0,1,2,3.
\]

For a polynomial \(P\) of degree at most four, compare the \(t^5\) coefficients in its six-node Lagrange interpolation formula. This gives
\[
\sum_{i=1}^6\frac{u_i^k}{H_6'(u_i)}=0,\qquad k=0,1,2,3,4.
\]
Consequently, each of the four signed odd aggregate coordinates is exactly
\[
\sum_i\mu_i(-1)^ku_i^{k+1}O_i
=(-1)^k\sum_i\frac{u_i^k}{H_6'(u_i)}=0.
\]

Every node lies in \((1/2,2)\), where \(E(u_i)<0\). Define the positive rational numbers
\[
S_k=\sum_i\mu_i u_i^k[-E(u_i)]>0,\qquad k=0,1,2,3.
\]
The **complete** raw aggregate is therefore exactly
\[
(-S_0,\ 0,\ S_1,\ 0,\ -S_2,\ 0,\ S_3,\ 0).
\]

Its sign pattern is
\[
\boxed{(-,\ 0,\ +,\ 0,\ -,\ 0,\ +,\ 0)}.
\]

**This is not a strict-negative certificate.** In particular, four coordinates vanish and two are positive.

## 5. Both five-node orientations and exact decomposition

Extend the two five-node vectors by zero outside their supports. Direct derivative-product reconstruction gives
\[
\mu^L=
\left(
375000,\ \frac{10125000}{7},\ \frac{60750000}{29},\
1350000,\ \frac{10125000}{31},\ 0
\right),
\]
and
\[
\mu^R=
\left(
0,\ \frac{2531250}{7},\ \frac{40500000}{29},\
2025000,\ \frac{40500000}{31},\ \frac{1265625}{4}
\right).
\]

The left support has odd signs \((-,+,-,+,-)\); the right has \((+,-,+,-,+)\). Their weights are respectively
\[
-\frac{1}{u_iO_iH_L'(u_i)},\qquad
+\frac{1}{u_iO_iH_R'(u_i)},
\]
and are strictly positive on their supports. Five-node Lagrange interpolation makes all four odd moments zero in each case.

Since \(u_6-u_1=1/6\),
\[
\mu_i^L=(u_6-u_i)\mu_i,\qquad
\mu_i^R=(u_i-u_1)\mu_i,
\]
including the zero endpoint entries. Hence, coordinate by coordinate,
\[
\boxed{\mu=6(\mu^L+\mu^R)}.
\]

### Exhaustion of frozen five-node possibilities

For five distinct nodes with nonzero odd values, the four odd-moment equations have rank four. Their nullspace is one-dimensional, with
\[
w_i u_iO_i=C/H_5'(u_i).
\]
Positive weights are possible exactly when the odd signs are one of the two alternating orientations.

All six frozen five-node subsets are:

| Omitted node | Remaining odd-sign word | Positive annihilator orientation |
|---|---|---|
| 1 | \(+,-,+,-,+\) | positive-first |
| 2 | \(-,-,+,-,+\) | none |
| 3 | \(-,+,+,-,+\) | none |
| 4 | \(-,+,-,-,+\) | none |
| 5 | \(-,+,-,+,+\) | none |
| 6 | \(-,+,-,+,-\) | negative-first |

Supports of size at most four have full column rank and admit no nonzero zero-odd-moment vector.

Thus **every admissible positive-first five-node vector on these frozen data has first coordinate zero**, while
\[
\mu_1=2250000>0.
\]
No nonnegative combination of such positive-first vectors can equal \(\mu\).

This falsifies precisely the stated **moment-only, same-nodes, same-actual-odd-values W1-only bridge**. It does not falsify a different reduction that assumes all four additional strict even inequalities, changes the frozen data, or uses both orientations.

## 6. Intended-failing controls

The complete source below implements nine controls. These have **not been executed**; their rejection reasons and the following arithmetic are written specifications.

| Mutation | Required rejection |
|---|---|
| Replace \(\delta_1\) by \(-1001/1000\) | `ACTUAL_BOX`: parameter outside the box |
| Increase \(\delta_1\) by \(1/1000\) | `ODD_VALUE`: first odd value becomes \(-99/1000\), not \(-1/10\) |
| Increase \(\mu_1\) by \(1\) | `ODD_MOMENT_0`: zeroth signed odd moment becomes \(-9/100\) |
| Negate \(\mu_1\) | `POSITIVE_WEIGHT` |
| Force positive-first orientation on the left support | `RAY_ORIENTATION` |
| Force negative-first orientation on the right support | `RAY_ORIENTATION` |
| Enlarge the parameter interval to \([-1,3]\) | `HB_SIGN_2`: the upper odd value at \(t=2\) is zero |
| Replace decomposition multiplier \(6\) by \(5\) | `DECOMPOSITION` |
| Propose \(6\mu^R\) as the reconstruction | `FROZEN_FIRST_COORDINATE` |

The enlarged-box control has a concrete mathematical failure: at \(\delta=3\), both \(E(2)\) and \(O_3(2)\) vanish, giving imaginary-axis zeros. An arbitrary exception does not count as a successful mutation rejection.

## 7. Execution status and intended argv

**NOTRUN.** There is no checker stdout, exit status, measured runtime/RSS, or materialized checker SHA to report.

After parent inspection and exclusive materialization as `fraction-verifier-v1.py`, the intended argv is:

`python3 -B /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check/fraction-verifier-v1.py /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f356-spr-actual-six-node-moment-counterexample-independent-check`

The program uses only the standard library, performs no writes/network/subprocess calls, hashes its own materialized source, verifies the frozen input metadata and literal packet rendering, prints all exact scientific results, requires invariant-specific mutation failures, and records actual runtime metadata if executed. Its arithmetic workload is finite and small; runtime has not been measured.

## 8. Complete verifier source

Each source line below carries the literal transport prefix `PY|`. Remove exactly that three-character prefix from each line between the BEGIN/END markers; preserve the remaining indentation and newlines.

BEGIN COMPLETE PYTHON SOURCE
PY|from fractions import Fraction as Q
PY|from itertools import combinations
PY|from math import prod
PY|from pathlib import Path
PY|from hashlib import sha256
PY|from datetime import datetime, timezone
PY|import json
PY|import os
PY|import resource
PY|import sys
PY|import time
PY|
PY|
PY|class VerificationError(Exception):
PY|    def __init__(self, code, detail=""):
PY|        self.code = code
PY|        super().__init__(code + (": " + detail if detail else ""))
PY|
PY|
PY|def need(condition, code, detail=""):
PY|    if not condition:
PY|        raise VerificationError(code, detail)
PY|
PY|
PY|def sign(x):
PY|    return (x > 0) - (x < 0)
PY|
PY|
PY|def show(values):
PY|    return "(" + ", ".join(str(x) for x in values) + ")"
PY|
PY|
PY|def blob(path, expected_sha, expected_bytes, expected_lf):
PY|    try:
PY|        data = path.read_bytes()
PY|    except OSError as error:
PY|        raise VerificationError("INPUT_READ", str(error)) from error
PY|    actual_sha = sha256(data).hexdigest()
PY|    need(actual_sha == expected_sha, "INPUT_SHA256", str(path))
PY|    need(len(data) == expected_bytes, "INPUT_BYTES", str(path))
PY|    need(data.count(b"\n") == expected_lf, "INPUT_LF", str(path))
PY|    print("PIN", str(path), actual_sha, len(data), data.count(b"\n"))
PY|    return data
PY|
PY|
PY|def record_blob(record):
PY|    return blob(
PY|        Path(record["path"]), record["sha256"],
PY|        record["bytes"], record["LF"]
PY|    )
PY|
PY|
PY|def verify_frozen_inputs(root):
PY|    expected = (
PY|        ("manifest-v1.json",
PY|         "2355a491094cb32daab714de39a28feff6b0fb5cd1bed5e3b7131cc48c4d964c",
PY|         5750, 80),
PY|        ("freeze-receipt-v1.json",
PY|         "07495b83dfc0622de474a49c303551e249cb132b9982539c24ca0fc3bdf2e9aa",
PY|         1943, 47),
PY|        ("literal-packet-v1.md",
PY|         "b6a7432a6333d4805ed13af4ca87ab58140aaead37a85d8db3bb38675f4b994e",
PY|         43052, 959),
PY|    )
PY|    data = {}
PY|    for name, digest, size, lf in expected:
PY|        data[name] = blob(root / name, digest, size, lf)
PY|    manifest = json.loads(data["manifest-v1.json"])
PY|    receipt = json.loads(data["freeze-receipt-v1.json"])
PY|    need(receipt["manifest"]["sha256"] == expected[0][1],
PY|         "RECEIPT_MANIFEST")
PY|    need(receipt["packet"]["sha256"] == expected[2][1],
PY|         "RECEIPT_PACKET")
PY|    need([item["id"] for item in manifest["inputs"]] == ["S1", "S2"],
PY|         "INPUT_ORDER")
PY|    for item in manifest["controls_before_body"]:
PY|        record_blob(item)
PY|    rendered = ["# Frozen prospective author inputs\n\n"]
PY|    for item in manifest["inputs"]:
PY|        source = record_blob(item).decode("utf-8")
PY|        lines = source.split("\n")
PY|        first, last = item["allowed_lines"]
PY|        need(1 <= first <= last <= len(lines), "SOURCE_RANGE")
PY|        for number in range(first, last + 1):
PY|            rendered.append(
PY|                item["id"] + "|" + str(number) + "|" +
PY|                lines[number - 1] + "\n"
PY|            )
PY|    need("".join(rendered).encode("utf-8") == data["literal-packet-v1.md"],
PY|         "PACKET_LITERAL_ROUNDTRIP")
PY|    print("PACKET_LITERAL_ROUNDTRIP=PASS")
PY|
PY|
PY|# Literal original polynomial coefficients, ascending powers of s.
PY|C = (Q(4), Q(15), Q(11), Q(23), Q(13, 2), Q(9), Q(1), Q(1))
PY|U = (Q(27, 30), Q(28, 30), Q(29, 30),
PY|     Q(30, 30), Q(31, 30), Q(32, 30))
PY|D = (Q(-961, 1000), Q(-3107, 6750), Q(-10081, 27000),
PY|     Q(1, 10), Q(4321, 27000), Q(4097, 6750))
PY|EVEN_POLY = tuple(((-1) ** k) * C[2 * k] for k in range(4))
PY|
PY|
PY|def poly_mul(p, q):
PY|    result = [Q(0)] * (len(p) + len(q) - 1)
PY|    for i, x in enumerate(p):
PY|        for j, y in enumerate(q):
PY|            result[i + j] += x * y
PY|    return tuple(result)
PY|
PY|
PY|def poly_value(p, t):
PY|    result = Q(0)
PY|    for coefficient in reversed(p):
PY|        result = result * t + coefficient
PY|    return result
PY|
PY|
PY|def poly_derivative(p):
PY|    return tuple(Q(k) * p[k] for k in range(1, len(p)))
PY|
PY|
PY|def parity(delta, t):
PY|    even = sum((C[2 * k] * (-t) ** k for k in range(4)), Q(0))
PY|    odd = delta + sum(
PY|        (C[2 * k + 1] * (-t) ** k for k in range(4)), Q(0)
PY|    )
PY|    return even, odd
PY|
PY|
PY|def raw_row(delta, t):
PY|    even, odd = parity(delta, t)
PY|    # Re(s^(2k) conjugate(a)) = (-t)^k E.
PY|    # Re(s^(2k+1) conjugate(a)) = t (-t)^k O at s=i*sqrt(t).
PY|    return tuple(
PY|        ((-t) ** (j // 2)) * (even if j % 2 == 0 else t * odd)
PY|        for j in range(8)
PY|    )
PY|
PY|
PY|def aggregate(weights):
PY|    need(len(weights) == 6, "WEIGHT_LENGTH")
PY|    return tuple(
PY|        sum((weights[i] * raw_row(D[i], U[i])[j]
PY|             for i in range(6)), Q(0))
PY|        for j in range(8)
PY|    )
PY|
PY|
PY|def hb_interval(lo, hi):
PY|    need(lo <= hi, "PARAMETER_INTERVAL")
PY|    roots = (Q(1, 2), Q(2), Q(4))
PY|    factorized = (Q(1),)
PY|    for root in roots:
PY|        factorized = poly_mul(factorized, (root, Q(-1)))
PY|    need(factorized == EVEN_POLY, "EVEN_FACTORIZATION")
PY|    need(C[0] > 0 and C[6] > 0 and C[7] == 1,
PY|         "HB_LEADING_ORIENTATION")
PY|    probes = ((Q(0), 1), (Q(1, 2), 1),
PY|              (Q(2), -1), (Q(4), 1), (Q(6), -1))
PY|    bounds = []
PY|    for t, wanted in probes:
PY|        base = parity(Q(0), t)[1]
PY|        lower, upper = base + lo, base + hi
PY|        strict = lower > 0 if wanted == 1 else upper < 0
PY|        need(strict, "HB_SIGN_" + str(t), show((lower, upper)))
PY|        bounds.append((t, lower, upper))
PY|    derivative = poly_derivative(EVEN_POLY)
PY|    for root in roots:
PY|        slope = poly_value(derivative, root)
PY|        lower = parity(lo, root)[1]
PY|        upper = parity(hi, root)[1]
PY|        need(slope * lower < 0 and slope * upper < 0,
PY|             "HB_ORIENTATION", str(root))
PY|    return tuple(bounds)
PY|
PY|
PY|def selected_values(deltas):
PY|    need(len(deltas) == 6, "PARAMETER_LENGTH")
PY|    for i, delta in enumerate(deltas):
PY|        need(Q(-1) <= delta <= Q(1),
PY|             "ACTUAL_BOX", str(i + 1) + ": " + str(delta))
PY|    evens, odds = [], []
PY|    for i, (t, delta) in enumerate(zip(U, deltas)):
PY|        even, odd = parity(delta, t)
PY|        wanted = Q(-1 if i % 2 == 0 else 1, 10)
PY|        need(odd == wanted, "ODD_VALUE",
PY|             str(i + 1) + ": " + str(odd))
PY|        evens.append(even)
PY|        odds.append(odd)
PY|    return tuple(evens), tuple(odds)
PY|
PY|
PY|def node_derivatives(nodes):
PY|    need(all(t > 0 for t in nodes), "POSITIVE_NODE")
PY|    need(all(nodes[i] < nodes[i + 1] for i in range(len(nodes) - 1)),
PY|         "NODE_ORDER")
PY|    polynomial = (Q(1),)
PY|    for t in nodes:
PY|        polynomial = poly_mul(polynomial, (-t, Q(1)))
PY|    derivative = poly_derivative(polynomial)
PY|    values = tuple(poly_value(derivative, t) for t in nodes)
PY|    direct = tuple(
PY|        prod((t - other for j, other in enumerate(nodes) if j != i),
PY|             start=Q(1))
PY|        for i, t in enumerate(nodes)
PY|    )
PY|    need(values == direct, "DERIVATIVE_PRODUCT")
PY|    need(all(x != 0 for x in values), "NONZERO_DERIVATIVE")
PY|    return polynomial, values
PY|
PY|
PY|def odd_moments(weights, odds):
PY|    need(len(weights) == len(odds) == 6, "MOMENT_LENGTH")
PY|    return tuple(
PY|        sum((weights[i] * U[i] * odds[i] * (-U[i]) ** r
PY|             for i in range(6)), Q(0))
PY|        for r in range(4)
PY|    )
PY|
PY|
PY|def positive_weights(weights):
PY|    need(all(weight > 0 for weight in weights), "POSITIVE_WEIGHT")
PY|
PY|
PY|def zero_odd_moments(weights, odds):
PY|    values = odd_moments(weights, odds)
PY|    for r, value in enumerate(values):
PY|        need(value == 0, "ODD_MOMENT_" + str(r), str(value))
PY|    return values
PY|
PY|
PY|def matrix_rank(matrix):
PY|    if not matrix:
PY|        return 0
PY|    a = [[Q(x) for x in row] for row in matrix]
PY|    row = 0
PY|    for column in range(len(a[0])):
PY|        if row == len(a):
PY|            break
PY|        pivot = next(
PY|            (r for r in range(row, len(a)) if a[r][column] != 0), None
PY|        )
PY|        if pivot is None:
PY|            continue
PY|        a[row], a[pivot] = a[pivot], a[row]
PY|        scale = a[row][column]
PY|        a[row] = [x / scale for x in a[row]]
PY|        for r in range(len(a)):
PY|            if r != row:
PY|                scale = a[r][column]
PY|                a[r] = [x - scale * y for x, y in zip(a[r], a[row])]
PY|        row += 1
PY|    return row
PY|
PY|
PY|def moment_matrix(support, odds):
PY|    return [
PY|        [U[i] * odds[i] * (-U[i]) ** r for i in support]
PY|        for r in range(4)
PY|    ]
PY|
PY|
PY|def five_ray(support, orientation, odds):
PY|    need(len(support) == 5, "RAY_SUPPORT")
PY|    need(orientation in (-1, 1), "RAY_ORIENTATION")
PY|    need(matrix_rank(moment_matrix(support, odds)) == 4, "RAY_RANK")
PY|    nodes = tuple(U[i] for i in support)
PY|    _, derivatives = node_derivatives(nodes)
PY|    need(
PY|        all(sign(odds[i]) == orientation * sign(derivatives[j])
PY|            for j, i in enumerate(support)),
PY|        "RAY_ORIENTATION",
PY|        str(tuple(i + 1 for i in support)) + ": " + str(orientation)
PY|    )
PY|    weights = [Q(0)] * 6
PY|    for j, i in enumerate(support):
PY|        weights[i] = Q(orientation) / (U[i] * odds[i] * derivatives[j])
PY|    need(all(weights[i] > 0 for i in support), "RAY_POSITIVE_WEIGHT")
PY|    zero_odd_moments(weights, odds)
PY|    need(all(aggregate(weights)[2 * r + 1] == 0 for r in range(4)),
PY|         "RAY_RAW_ODD_COORDINATES")
PY|    return tuple(weights)
PY|
PY|
PY|def check_decomposition(target, left, right, multiplier):
PY|    candidate = tuple(multiplier * (x + y) for x, y in zip(left, right))
PY|    need(candidate == target, "DECOMPOSITION", show(candidate))
PY|
PY|
PY|def check_first_coordinate(target, proposed):
PY|    need(target[0] == proposed[0], "FROZEN_FIRST_COORDINATE",
PY|         str(target[0]) + " != " + str(proposed[0]))
PY|
PY|
PY|def expected_failure(label, wanted_code, action):
PY|    try:
PY|        action()
PY|    except VerificationError as error:
PY|        need(error.code == wanted_code, "WRONG_MUTATION_FAILURE",
PY|             label + ": " + str(error))
PY|        print("EXPECTED_FAILURE", label, str(error))
PY|        return 1
PY|    raise VerificationError("MUTATION_ACCEPTED", label)
PY|
PY|
PY|def main():
PY|    need(len(sys.argv) == 2, "ARGV", "verifier.py FROZEN_WAVE_DIRECTORY")
PY|    started = time.perf_counter()
PY|    print("RUN_START_UTC", datetime.now(timezone.utc).isoformat())
PY|    print("PID", os.getpid(), "PGID", os.getpgid(0))
PY|    print("PYTHON", sys.version.splitlines()[0])
PY|    print("EXECUTABLE", sys.executable)
PY|    print("ARGV", repr(sys.argv))
PY|    print("SELF_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
PY|    verify_frozen_inputs(Path(sys.argv[1]))
PY|    need(time.perf_counter() - started < 60, "TIME_BOUND")
PY|
PY|    bounds = hb_interval(Q(-1), Q(1))
PY|    need(bounds == (
PY|        (Q(0), Q(14), Q(16)),
PY|        (Q(1, 2), Q(37, 8), Q(53, 8)),
PY|        (Q(2), Q(-4), Q(-2)),
PY|        (Q(4), Q(2), Q(4)),
PY|        (Q(6), Q(-16), Q(-14)),
PY|    ), "HB_EXACT_BOUNDS")
PY|    for t, lower, upper in bounds:
PY|        print("HB_INTERVAL", str(t), str(lower), str(upper))
PY|    print("HB_EXACT_INTERVAL_HYPOTHESES=PASS")
PY|    print("HURWITZ_CONCLUSION_USES_CLASSICAL_HERMITE_BIEHLER")
PY|
PY|    evens, odds = selected_values(D)
PY|    polynomial, derivatives = node_derivatives(U)
PY|    weights = tuple(
PY|        Q(1) / (U[i] * odds[i] * derivatives[i]) for i in range(6)
PY|    )
PY|    positive_weights(weights)
PY|    need(weights == (
PY|        Q(2250000), Q(75937500, 7), Q(607500000, 29),
PY|        Q(20250000), Q(303750000, 31), Q(3796875, 2)
PY|    ), "SIX_WEIGHT_VALUES")
PY|    need(derivatives == (
PY|        Q(-1, 202500), Q(1, 1012500), Q(-1, 2025000),
PY|        Q(1, 2025000), Q(-1, 1012500), Q(1, 202500)
PY|    ), "SIX_DERIVATIVE_VALUES")
PY|    print("H6_ASCENDING_COEFFICIENTS", show(polynomial))
PY|    for i in range(6):
PY|        print("ATOM", i + 1, "t=" + str(U[i]), "delta=" + str(D[i]),
PY|              "E=" + str(evens[i]), "O=" + str(odds[i]),
PY|              "Hprime=" + str(derivatives[i]), "mu=" + str(weights[i]))
PY|    lagrange = tuple(
PY|        sum((U[i] ** k / derivatives[i] for i in range(6)), Q(0))
PY|        for k in range(6)
PY|    )
PY|    need(lagrange == (Q(0), Q(0), Q(0), Q(0), Q(0), Q(1)),
PY|         "SIX_LAGRANGE_IDENTITIES")
PY|    print("SIX_LAGRANGE_SUMS_POWERS_0_TO_5", show(lagrange))
PY|    moments = zero_odd_moments(weights, odds)
PY|    raw = aggregate(weights)
PY|    need(tuple(raw[2 * r + 1] for r in range(4)) == moments,
PY|         "RAW_ODD_MOMENT_AGREEMENT")
PY|    signs = tuple(sign(value) for value in raw)
PY|    need(signs == (-1, 0, 1, 0, -1, 0, 1, 0), "AGGREGATE_SIGNS")
PY|    need(not all(value < 0 for value in raw), "STRICT_CERTIFICATE_STATUS")
PY|    print("ODD_SIGNED_MOMENTS", show(moments))
PY|    print("RAW_AGGREGATE", show(raw))
PY|    print("RAW_AGGREGATE_SIGNS", show(signs))
PY|    print("STRICT_NEGATIVE_CERTIFICATE=False")
PY|
PY|    short_support_count = 0
PY|    for size in range(1, 5):
PY|        for support in combinations(range(6), size):
PY|            need(matrix_rank(moment_matrix(support, odds)) == size,
PY|                 "SHORT_SUPPORT_RANK", str(support))
PY|            short_support_count += 1
PY|    need(short_support_count == 56, "SHORT_SUPPORT_COUNT")
PY|    print("FULL_COLUMN_RANK_SUPPORTS_OF_SIZE_1_TO_4", short_support_count)
PY|
PY|    admissible = {1: [], -1: []}
PY|    positive_first_rays = []
PY|    for support in combinations(range(6), 5):
PY|        need(matrix_rank(moment_matrix(support, odds)) == 4,
PY|             "FIVE_SUBSET_RANK")
PY|        _, dp = node_derivatives(tuple(U[i] for i in support))
PY|        orientations = tuple(
PY|            epsilon for epsilon in (-1, 1)
PY|            if all(sign(odds[i] * dp[j]) == epsilon
PY|                   for j, i in enumerate(support))
PY|        )
PY|        print("FIVE_SUBSET", tuple(i + 1 for i in support),
PY|              "ODD_SIGNS", tuple(sign(odds[i]) for i in support),
PY|              "ADMISSIBLE_ORIENTATIONS", orientations)
PY|        for epsilon in orientations:
PY|            ray = five_ray(support, epsilon, odds)
PY|            admissible[epsilon].append(support)
PY|            if epsilon == 1:
PY|                positive_first_rays.append(ray)
PY|    need(admissible[1] == [(1, 2, 3, 4, 5)],
PY|         "POSITIVE_FIRST_EXHAUSTION")
PY|    need(admissible[-1] == [(0, 1, 2, 3, 4)],
PY|         "NEGATIVE_FIRST_EXHAUSTION")
PY|
PY|    left = five_ray((0, 1, 2, 3, 4), -1, odds)
PY|    right = five_ray((1, 2, 3, 4, 5), 1, odds)
PY|    need(left == (
PY|        Q(375000), Q(10125000, 7), Q(60750000, 29),
PY|        Q(1350000), Q(10125000, 31), Q(0)
PY|    ), "LEFT_RAY_VALUES")
PY|    need(right == (
PY|        Q(0), Q(2531250, 7), Q(40500000, 29),
PY|        Q(2025000), Q(40500000, 31), Q(1265625, 4)
PY|    ), "RIGHT_RAY_VALUES")
PY|    length = U[-1] - U[0]
PY|    need(length == Q(1, 6), "ENDPOINT_DISTANCE")
PY|    need(left == tuple((U[-1] - U[i]) * weights[i] for i in range(6)),
PY|         "LEFT_DERIVATIVE_RELATION")
PY|    need(right == tuple((U[i] - U[0]) * weights[i] for i in range(6)),
PY|         "RIGHT_DERIVATIVE_RELATION")
PY|    check_decomposition(weights, left, right, Q(1) / length)
PY|    need(matrix_rank(moment_matrix(tuple(range(6)), odds)) == 4,
PY|         "SIX_MOMENT_RANK")
PY|    need(matrix_rank([left, right]) == 2, "TWO_KERNEL_DIRECTIONS")
PY|    need(left[0] > 0 and left[-1] == 0 and
PY|         right[0] == 0 and right[-1] > 0, "CONE_ENDPOINT_STRUCTURE")
PY|    need(weights[0] > 0 and
PY|         all(ray[0] == 0 for ray in positive_first_rays),
PY|         "W1_FIRST_COORDINATE_OBSTRUCTION")
PY|    print("LEFT_NEGATIVE_FIRST_RAY", show(left))
PY|    print("LEFT_ODD_MOMENTS", show(odd_moments(left, odds)))
PY|    print("RIGHT_POSITIVE_FIRST_RAY", show(right))
PY|    print("RIGHT_ODD_MOMENTS", show(odd_moments(right, odds)))
PY|    print("DECOMPOSITION_MULTIPLIERS", show((Q(6), Q(6))))
PY|    print("TARGET_FIRST_COORDINATE", weights[0])
PY|    print("ALL_POSITIVE_FIRST_RAYS_FIRST_COORDINATE=0")
PY|    print("W1_ONLY_FROZEN_DATA_BRIDGE=FALSE")
PY|
PY|    outside_delta = (Q(-1001, 1000),) + D[1:]
PY|    shifted_delta = (D[0] + Q(1, 1000),) + D[1:]
PY|    incremented_weight = (weights[0] + Q(1),) + weights[1:]
PY|    negative_weight = (-weights[0],) + weights[1:]
PY|    need(odd_moments(incremented_weight, odds)[0] == Q(-9, 100),
PY|         "WEIGHT_MUTATION_EXACT_EFFECT")
PY|    controls = (
PY|        ("delta_outside_box", "ACTUAL_BOX",
PY|         lambda: selected_values(outside_delta)),
PY|        ("delta_wrong_odd_value", "ODD_VALUE",
PY|         lambda: selected_values(shifted_delta)),
PY|        ("weight_increment", "ODD_MOMENT_0",
PY|         lambda: zero_odd_moments(incremented_weight, odds)),
PY|        ("weight_sign", "POSITIVE_WEIGHT",
PY|         lambda: positive_weights(negative_weight)),
PY|        ("left_wrong_orientation", "RAY_ORIENTATION",
PY|         lambda: five_ray((0, 1, 2, 3, 4), 1, odds)),
PY|        ("right_wrong_orientation", "RAY_ORIENTATION",
PY|         lambda: five_ray((1, 2, 3, 4, 5), -1, odds)),
PY|        ("expanded_parameter_interval", "HB_SIGN_2",
PY|         lambda: hb_interval(Q(-1), Q(3))),
PY|        ("wrong_decomposition_multiplier", "DECOMPOSITION",
PY|         lambda: check_decomposition(weights, left, right, Q(5))),
PY|        ("W1_only_reconstruction", "FROZEN_FIRST_COORDINATE",
PY|         lambda: check_first_coordinate(
PY|             weights, tuple(Q(6) * value for value in right))),
PY|    )
PY|    rejected = sum(expected_failure(*control) for control in controls)
PY|    need(rejected == 9, "MUTATION_COUNT")
PY|    print("INTENDED_REASON_MUTATIONS_REJECTED", rejected)
PY|
PY|    elapsed = time.perf_counter() - started
PY|    need(elapsed < 60, "TIME_BOUND", str(elapsed))
PY|    maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
PY|    maxrss_bytes = int(maxrss if sys.platform == "darwin" else maxrss * 1024)
PY|    print("ELAPSED_SECONDS", format(elapsed, ".9f"))
PY|    print("MAXRSS_BYTES", maxrss_bytes)
PY|    print("RUN_END_UTC", datetime.now(timezone.utc).isoformat())
PY|    print("SCOPE=EXACT_FINITE_CHECK_PLUS_WRITTEN_CLASSICAL_HB")
PY|    print("NO_GLOBAL_CERTIFICATE_OR_STRICT_SPR_OR_NOVELTY_CLAIM")
PY|    print("RESULT=PASS")
PY|
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        main()
PY|    except VerificationError as error:
PY|        print("RESULT=FAIL", str(error), file=sys.stderr)
PY|        raise SystemExit(1)
END COMPLETE PYTHON SOURCE

## Verdict fields

**Findings:** None in the scoped finite claims.

**Overall correctness:** correct.

**Explanation:** Exact interval signs establish the entire stated box’s Hurwitz interlacing, and exact interpolation establishes the six-node moment cancellation, complete non-strict aggregate sign pattern, both-orientation decomposition, and frozen-data W1-only obstruction. The independent machine verifier remains **NOTRUN**, so no computational acceptance or broader theorem acceptance is claimed.

**Confidence:** 0.97 for the written finite mathematics; the supplied implementation still requires parent inspection and execution.