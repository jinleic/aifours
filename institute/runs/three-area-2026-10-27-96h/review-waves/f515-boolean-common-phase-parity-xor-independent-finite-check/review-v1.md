# F515 FINITE — full return

**Execution status: NOT_RUN.** The higher-priority read-only reviewer role prohibits scientific execution and filesystem edits. The complete checker and exact argv are supplied below; no finite PASS, measured runtime, child-native hash, or generated witness is claimed.

## Read and transport record

Before opening the scientific packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all eleven named pre-body controls. I then delivered a **direct pre-body acknowledgment to `agent://Main`**, which the tool reported delivered.

Parent-supplied bindings, not independently recomputed child hashes:

- Manifest: `8565586a3b174df0333b021fa6fc2e70cd2b462698b7403aae8d189d587bdd75`
- Receipt: `faed6745dfbc1d57d158eab3b0947bf4ae71cb3da4c9babb462087633735b29f`
- Literal packet: `bcf278b589cad8802db7888dc8ad711febf8fa33f059d24140c196402512af3c`

After that acknowledgment, I read the entire packet in ordered raw windows of at most 20 LF, through its ending: packet lines 1–518, containing S1 source lines 1–478 and S2 lines 1–38. The additional read starting at packet line 519 returned empty.

I subsequently read only the newly supplied **f513 status/quarantine control**, including its ending. No f513 mathematical history, payload, reasoning, or fragments were opened or used. F513 and all previously named held episodes and consumers remain NONINPUT.

F483’s earlier acknowledgment remains accurately described as **local-only, without observed direct pre-body delivery**. This return neither repairs that transport retrospectively nor treats it as automatic mathematical invalidation under owner addendum2.

## Written reconstruction

No defect was identified in these scoped identities:

1. With \(d=|D_0|,\ p=|Z_2|,\ t=|Z_4|\), support and \(U_0\)-energy give
   \(p+2t=8\) and \(d+p=10\). The \(U_3\)-zero count is \(20+3t\), forcing \(t=1,p=6,d=4\) when that count is 23.

2. For the actual common \(x=U_0\), writing \(p_-=|P|\) and \(n_-=|N|\), the claimed graph congruence gives, when \(p_-\) is even,
   \[
   \widehat x(\xi)\equiv
   4[1-p_-/2-n_-+\xi\cdot(\gamma e+X_P+X_W)]\pmod8.
   \]
   At the fixed \(|W|=10\) scope, vanishing at every frequency is exactly condition (C), not an amplitude statement.

3. The same physical \(u\) gives
   \(F_0+F_1+F_2+F_3\equiv4J\pmod8\).
   Since \(F_1,F_2\equiv4\pmod8\), condition (C) implies
   \(F_3\equiv4J\pmod8\).

4. Divisibility of all even-half coefficients by four forces support XOR zero. Its actual 140-point complement also has XOR zero. Consequently an actual complementary sign assignment has all 256 Walsh coefficients congruent to \(2n_-\pmod4\). Odd negative-sign count gives residue two **modulo four**, not a fixed residue modulo eight.

These are congruence/count reductions. They do **not** supply either even-half amplitude cap, the carried original balance condition, or the complementary odd-half cap.

## Checker coverage and limits

The source below implements:

- Exhaustive enumeration of all 65,536 four-variable truth tables.
- All 896 canonical graph functions and all 64 graph-indicator frequencies per graph.
- Direct quadratic polar ranks and the rank-two/rank-four \(\gamma\) distinction.
- All common-phase membership counts; one common phase per graph is also checked directly on its two fixed fibres.
- All 81 ternary four-point blocks and exact local-template completeness.
- Deterministic actual four-fibre controls using four selected graphs, two common phases per selected graph, two local partitions, and both physical column parities.
- C-true and three intended-reason C-false controls, with all four fibres recomputed from the same ternary \(u\).
- All 23 possible \(D_0\)-cardinalities for the eight-pair/no-peak recipe.
- Actual complementary \(v\) controls with zero, one, two, and three negative signs, checking all 256 Fourier coefficients modulo four.
- Nine named mutation checks: wrong primal direction, wrong \(\gamma\) bit, C-sign parity, omitted cardinality ten, odd-sign parity, wrong odd modulus, independent \(v\), moved balance zero, and omitted amplitude caps.

The C-sign-parity and omitted-cardinality-ten mutations coincide algebraically in their wrong constant parity at this fixed cardinality. They are exercised with different intended-reason controls, **not represented as independent mathematical evidence**.

The positive controls are positive for their stated local/count/congruence conditions only. They intentionally retain failed amplitude caps and are not fabricated original callers.

The program has an internal 54-second cooperative calculation deadline. A deadline or invariant failure prevents its PASS output. Its runtime and successful completion have **not** been observed.

## Exact argv — NOT_RUN

Interpreter requirement: Python 3.10 or newer, standard library only. Interpreter version and executable hash were not observed.

Proposed source filename: `independent-boolean-common-phase-parity-check-v1.py`

Exact command, after Main materializes the verbatim source at that path:

python3 -I -B -S /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f515-boolean-common-phase-parity-xor-independent-finite-check/independent-boolean-common-phase-parity-check-v1.py

The source performs no data-file access or writes, network operations, child launches, installation, deletion, or external-model calls. Results go only to stdout/stderr.

## Full source

BEGIN VERBATIM PYTHON SOURCE

import sys
from time import monotonic

START = 0.0
MAX_SECONDS = 54.0
PRIMAL_E = 1
DUAL_NU = 7 << 3
DB = (1, 2, 4, 7)
SMALL_G_FREQUENCIES = {0, 1 << 3, 2 << 3, 4 << 3}


class BudgetExceeded(RuntimeError):
    pass


class CheckFailure(RuntimeError):
    pass


def tick():
    if monotonic() - START >= MAX_SECONDS:
        raise BudgetExceeded("54-second internal calculation deadline")


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def dot(a, b):
    return (a & b).bit_count() & 1


def character(a, b):
    return 1 - 2 * dot(a, b)


def bit(table, x):
    return (table >> x) & 1


def xor_points(points):
    value = 0
    for point in points:
        value ^= point
    return value


def fwht(values):
    tick()
    out = list(values)
    n = len(out)
    need(n > 0 and (n & (n - 1)) == 0, "non-power-of-two transform")
    step = 1
    while step < n:
        for start in range(0, n, 2 * step):
            for offset in range(step):
                i = start + offset
                j = i + step
                a = out[i]
                b = out[j]
                out[i] = a + b
                out[j] = a - b
        step *= 2
    return out


def matrix_rank(rows):
    work = list(rows)
    pivot_row = 0
    for column in range(4):
        pivot = next(
            (
                r
                for r in range(pivot_row, 4)
                if (work[r] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        for r in range(4):
            if r != pivot_row and ((work[r] >> column) & 1):
                work[r] ^= work[pivot_row]
        pivot_row += 1
    return pivot_row


def quadratic_rank(table):
    values = [bit(table, x) for x in range(16)]
    linear = [values[1 << i] ^ values[0] for i in range(4)]
    coefficients = {}
    rows = [0] * 4
    for i in range(4):
        for j in range(i + 1, 4):
            coefficient = (
                values[(1 << i) | (1 << j)]
                ^ values[1 << i]
                ^ values[1 << j]
                ^ values[0]
            )
            coefficients[(i, j)] = coefficient
            if coefficient:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
    for x in range(16):
        predicted = values[0]
        for i in range(4):
            if (x >> i) & 1:
                predicted ^= linear[i]
        for (i, j), coefficient in coefficients.items():
            if ((x >> i) & 1) and ((x >> j) & 1):
                predicted ^= coefficient
        need(predicted == values[x], "truth table is not quadratic")
    return matrix_rank(rows)


def graph_support(f):
    points = []
    for b in range(4):
        d = 1 ^ (3 if b & 1 else 0) ^ (5 if b & 2 else 0)
        need(d == DB[b], "inconsistent b-to-d encoding")
        for j in range(4):
            variable = j | (b << 2)
            h = (j << 1) | bit(f, variable)
            points.append(h | (d << 3))
    need(len(set(points)) == 16, "graph points are not distinct")
    return tuple(sorted(points))


def geometry(f, r, rank):
    support = graph_support(f)
    support_set = set(support)
    a = [0] * 64
    for b in range(4):
        for j in range(4):
            variable = j | (b << 2)
            h = (j << 1) | bit(f, variable)
            c = h | (DB[b] << 3)
            a[c] = 1 - 2 * bit(r, variable)
    g = [0] * 64
    for h in range(8):
        g[h] = 4 if h in (0, 1) else -2
    b_blocks = set()
    for b, d in enumerate(DB):
        rho = 1 if b == 3 else -1
        for h in range(8):
            c = h | (d << 3)
            b_blocks.add(c)
            g[c] = rho * (-2 + 3 * (c in support_set))
    e_blocks = set(range(8))
    full = {0, 1}
    d_blocks = (e_blocks | b_blocks) - full - support_set
    z_blocks = set(range(64)) - e_blocks - b_blocks
    need(len(d_blocks) == 22, "incorrect D cardinality")
    need(len(z_blocks) == 24, "incorrect Z cardinality")
    need(rank in (2, 4), "unexpected canonical graph rank")
    return {
        "f": f,
        "r": r,
        "rank": rank,
        "S": support,
        "a": a,
        "g": g,
        "D": tuple(sorted(d_blocks)),
        "Z": tuple(sorted(z_blocks)),
    }


def check_g_spectrum(spectrum):
    for frequency, value in enumerate(spectrum):
        if frequency in SMALL_G_FREQUENCIES:
            need(value == 4, "named small g coefficient/sign")
        else:
            need(abs(value) == 12, "non-small g magnitude")


def canonical_census(killed):
    bent = []
    for table in range(1 << 16):
        spectrum = fwht([1 - 2 * bit(table, x) for x in range(16)])
        if all(abs(value) == 4 for value in spectrum):
            bent.append(table)
    need(len(bent) == 896, "four-variable bent census")
    for table in bent:
        need(quadratic_rank(table) == 4, "bent polar rank")
    q = sum(
        (1 ^ (((x >> 2) & 1) * ((x >> 3) & 1))) << x
        for x in range(16)
    )
    need(quadratic_rank(q) == 2, "q polar rank")
    bent_set = set(bent)
    graphs = sorted(table ^ q for table in bent)
    need(len(set(graphs)) == 896, "canonical graph census")
    ranks = {}
    phase_extrema = {}
    rank_counts = {2: 0, 4: 0}
    phase_pairs = 0
    graph_frequency_checks = 0
    for f in graphs:
        tick()
        rank = quadratic_rank(f)
        need(rank in rank_counts, "canonical graph has wrong rank")
        ranks[f] = rank
        rank_counts[rank] += 1
        phases = [r for r in bent if (r ^ f) in bent_set]
        need(len(phases) == 384, "common-phase count for one graph")
        phase_extrema[f] = (phases[0], phases[-1])
        phase_pairs += len(phases)
        geo = geometry(f, phases[0], rank)
        indicator = [int(c in geo["S"]) for c in range(64)]
        indicator_hat = fwht(indicator)
        gamma = int(rank == 4)
        need(f.bit_count() % 2 == 0, "graph weight parity")
        need(
            (f.bit_count() // 2) % 2 == gamma,
            "weight/rank gamma equivalence",
        )
        for frequency, value in enumerate(indicator_hat):
            expected = 4 * gamma * dot(frequency, PRIMAL_E)
            need((value - expected) % 8 == 0, "graph mod-eight identity")
            graph_frequency_checks += 1
        if rank == 4:
            need(
                any(
                    (
                        indicator_hat[frequency]
                        - 4 * dot(frequency, DUAL_NU)
                    ) % 8 != 0
                    for frequency in range(64)
                ),
                "wrong-direction mutant not distinguished",
            )
            killed.add("gamma-direction")
        need(
            any(
                (
                    indicator_hat[frequency]
                    - 4 * (1 - gamma) * dot(frequency, PRIMAL_E)
                ) % 8 != 0
                for frequency in range(64)
            ),
            "wrong-gamma-bit mutant not distinguished",
        )
        killed.add("gamma-bit")
        need(
            all(abs(value) == 4 for value in fwht(geo["a"])),
            "direct common-phase a spectrum",
        )
        check_g_spectrum(fwht(geo["g"]))
    need(rank_counts == {2: 512, 4: 384}, "canonical rank census")
    need(phase_pairs == 344064, "total common-phase census")
    need(graph_frequency_checks == 896 * 64, "graph frequency coverage")
    return graphs, ranks, phase_extrema, graph_frequency_checks, phase_pairs


def block_catalogue():
    catalogue = {}
    count = 0
    for encoded in range(81):
        remaining = encoded
        block = []
        for unused in range(4):
            block.append(remaining % 3 - 1)
            remaining //= 3
        spectrum = fwht(block)
        need(
            fwht(spectrum) == [4 * value for value in block],
            "four-point inverse roundtrip",
        )
        x, u1, g, y = spectrum
        if u1 == 0:
            nonzero = [abs(value) for value in spectrum if value]
            need(
                not nonzero
                or nonzero == [4]
                or (len(nonzero) == 2 and all(v == 2 for v in nonzero)),
                "incomplete U1-zero block classification",
            )
        if not (u1 == 0 and abs(x) == 4):
            bucket = catalogue.setdefault((u1, g), {})
            need((x, y) not in bucket, "non-unique four-point inverse")
            bucket[(x, y)] = tuple(block)
        count += 1
    need(count == 81, "ternary block coverage")
    for a in (-1, 1):
        for g in (-1, 1):
            expected = {
                (alpha, -a * g * alpha)
                for alpha in (-1, 1)
            }
            need(
                set(catalogue[(3 * a, g)]) == expected,
                "S block template completeness",
            )
    for g in (-4, 4):
        need(
            set(catalogue[(0, g)]) == {(0, 0)},
            "full block template completeness",
        )
    for g in (-2, 2):
        expected = {(2, 0), (-2, 0), (0, 2), (0, -2)}
        need(
            set(catalogue[(0, g)]) == expected,
            "D block template completeness",
        )
    expected_z = {
        (0, 0), (2, 2), (2, -2), (-2, 2), (-2, -2),
        (0, 4), (0, -4),
    }
    need(
        set(catalogue[(0, 0)]) == expected_z,
        "Z block template completeness under H=0",
    )
    return catalogue


def minimal_even_subset(support, target):
    states = {(0, 0): 0}
    for index, point in enumerate(support):
        tick()
        following = dict(states)
        for (value, parity), mask in states.items():
            key = (value ^ point, parity ^ 1)
            candidate = mask | (1 << index)
            previous = following.get(key)
            if previous is None or (
                candidate.bit_count(), candidate
            ) < (
                previous.bit_count(), previous
            ):
                following[key] = candidate
        states = following
    need((target, 0) in states, "required even graph subset unavailable")
    mask = states[(target, 0)]
    result = {
        point
        for index, point in enumerate(support)
        if (mask >> index) & 1
    }
    need(len(result) % 2 == 0, "subset solver parity")
    need(xor_points(result) == target, "subset solver XOR")
    need(len(result) <= 6, "minimal even-subset bound")
    return result


def epsilon_signs(p_set, w_points):
    need(len(p_set) % 2 == 0, "epsilon helper requires even P")
    negative_parity = 1 ^ ((len(p_set) // 2) & 1)
    return {
        point: (-1 if negative_parity and index == 0 else 1)
        for index, point in enumerate(w_points)
    }


def selected_partition(geo, variant):
    e_free = [point for point in geo["D"] if point < 8]
    need(len(e_free) == 6, "E-minus-F size")
    d0 = set(e_free[variant:variant + 4])
    z2 = set(geo["Z"][6 * variant:6 * variant + 6])
    z4 = {next(point for point in geo["Z"] if point not in z2)}
    need((len(d0), len(z2), len(z4)) == (4, 6, 1), "selected counts")
    return d0, z2, z4


def lift(geo, catalogue, d0, z2, z4, p_set, eps, requested_j):
    tick()
    s_set = set(geo["S"])
    d_set = set(geo["D"])
    z_set = set(geo["Z"])
    need(d0 <= d_set, "D0 outside D")
    need(z2 <= z_set and z4 <= z_set and not z2 & z4, "Z partition")
    need(p_set <= s_set, "P outside S")
    w_points = d0 | z2
    need(set(eps) == w_points, "epsilon domain")
    need(all(value in (-1, 1) for value in eps.values()), "epsilon signs")
    x = [0] * 64
    y = [0] * 64
    for c in geo["S"]:
        x[c] = -1 if c in p_set else 1
        y[c] = -geo["a"][c] * geo["g"][c] * x[c]
    for c in d_set:
        if c in d0:
            x[c] = 2 * eps[c]
        else:
            y[c] = 2
    for c in z2:
        x[c] = 2 * eps[c]
        y[c] = 2 * eps[c]
    for c in z4:
        y[c] = 4

    def assemble():
        actual = []
        for c in range(64):
            bucket = catalogue.get((3 * geo["a"][c], geo["g"][c]))
            need(bucket is not None, "missing fixed-fibre block class")
            block = bucket.get((x[c], y[c]))
            need(block is not None, "nonphysical requested block")
            actual.extend(block)
        return actual

    u = assemble()
    j = sum(u[4 * c] != 0 for c in range(64)) % 2
    if requested_j is not None and j != requested_j:
        need(bool(z2), "no Z2 block to change column parity")
        c = min(z2)
        y[c] = -y[c]
        u = assemble()
        j = sum(u[4 * c] != 0 for c in range(64)) % 2
    if requested_j is not None:
        need(j == requested_j, "physical J control")
    need(len(u) == 256, "physical u length")
    need(all(value in (-1, 0, 1) for value in u), "physical u alphabet")
    fibres = [[0] * 64 for unused in range(4)]
    for c in range(64):
        actual = fwht(u[4 * c:4 * c + 4])
        for slot in range(4):
            fibres[slot][c] = actual[slot]
    need(fibres[0] == x, "actual U0 disagrees with requested x")
    need(fibres[1] == [3 * value for value in geo["a"]], "actual U1")
    need(fibres[2] == geo["g"], "actual U2")
    need(fibres[3] == y, "actual U3 disagrees with requested y")
    spectra = [fwht(fibre) for fibre in fibres]
    return {
        "geo": geo,
        "u": u,
        "U": fibres,
        "F": spectra,
        "J": j,
    }


def audit_actual_l_case(record):
    tick()
    u = record["u"]
    fibres = record["U"]
    spectra = record["F"]
    geo = record["geo"]
    need(sum(value != 0 for value in u) == 116, "L support")
    need(sum(value * value for value in fibres[0]) == 56, "L U0 energy")
    need(sum(value * value for value in fibres[3]) == 128, "L U3 energy")
    need(sum(value == 0 for value in fibres[3]) == 23, "L U3 zeros")
    need(
        sum(
            fibres[1][c] == 0 and abs(fibres[0][c]) == 4
            for c in range(64)
        ) == 0,
        "L H=0",
    )
    need(all(abs(value) == 12 for value in spectra[1]), "actual F1")
    check_g_spectrum(spectra[2])
    need(all(value % 8 == 4 for value in spectra[1]), "F1 residue")
    need(all(value % 8 == 4 for value in spectra[2]), "F2 residue")
    s_set = set(geo["S"])
    p_set = {c for c in s_set if fibres[0][c] < 0}
    w_set = {c for c in range(64) if abs(fibres[0][c]) == 2}
    n_set = {c for c in w_set if fibres[0][c] < 0}
    need(len(w_set) == 10, "physical W cardinality ten")
    p = len(p_set)
    n = len(n_set)
    p_even = p % 2 == 0
    sign_ok = p_even and ((p // 2 + n) % 2 == 1)
    gamma = int(geo["rank"] == 4)
    xor_ok = (
        xor_points(p_set) ^ xor_points(w_set)
    ) == gamma * PRIMAL_E
    condition_c = p_even and sign_ok and xor_ok
    divisible = all(value % 8 == 0 for value in spectra[0])
    need(condition_c == divisible, "C iff all actual F0 divisible by eight")
    for frequency in range(64):
        need(
            (
                sum(spectra[slot][frequency] for slot in range(4))
                - 4 * record["J"]
            ) % 8 == 0,
            "same-u physical column identity",
        )
    if condition_c:
        need(
            all(
                (value - 4 * record["J"]) % 8 == 0
                for value in spectra[3]
            ),
            "D congruence from physical J",
        )
    full_transform = fwht(u)
    for frequency in range(256):
        need(
            full_transform[frequency]
            == spectra[frequency & 3][frequency >> 2],
            "four-fibre/full-transform routing",
        )
    support = {point for point, value in enumerate(u) if value}
    support_xor = xor_points(support)
    for frequency, value in enumerate(full_transform):
        need(
            (
                value
                - full_transform[0]
                + 2 * dot(frequency, support_xor)
            ) % 4 == 0,
            "support-XOR versus full Walsh mod four",
        )
    if condition_c:
        need(
            all(value % 4 == 0 for value in full_transform),
            "even-half four-divisibility",
        )
        need(support_xor == 0, "actual support XOR")
        complement = set(range(256)) - support
        need(len(complement) == 140, "actual complement cardinality")
        need(xor_points(complement) == 0, "actual complement XOR")
    return {
        "C": condition_c,
        "divisible": divisible,
        "p": p,
        "n": n,
        "p_even": p_even,
        "sign_ok": sign_ok,
        "xor_ok": xor_ok,
        "W": w_set,
    }


def complementary_checks(record, killed):
    u = record["u"]
    complement = [point for point in range(256) if u[point] == 0]
    complement_set = set(complement)
    need(len(complement) == 140, "complementary test size")
    need(xor_points(complement) == 0, "complementary test XOR")
    for negative_count in range(4):
        tick()
        negative = set(complement[:negative_count])
        v = [
            -1 if point in negative else (
                1 if point in complement_set else 0
            )
            for point in range(256)
        ]
        need(
            all(u[point] * v[point] == 0 for point in range(256)),
            "actual uv=0",
        )
        need(
            all(
                u[point] * u[point] + v[point] * v[point] == 1
                for point in range(256)
            ),
            "actual u-square plus v-square",
        )
        need(sum(value < 0 for value in v) == negative_count, "negative count")
        spectrum = fwht(v)
        expected_residue = 2 * (negative_count % 2)
        need(
            all(value % 4 == expected_residue for value in spectrum),
            "all 256 complementary Walsh residues",
        )
        odd_congruence = all(value % 4 == 2 for value in spectrum)
        need(
            odd_congruence == bool(negative_count & 1),
            "odd congruence iff negative-sign count odd",
        )
        need(
            spectrum[0] == 140 - 2 * negative_count,
            "complementary DC",
        )
        need(
            not all(abs(value) <= 14 for value in spectrum),
            "complementary controls must not be advertised as capped",
        )
        if negative_count == 0:
            mutant_accepts = negative_count % 2 == 0
            need(
                mutant_accepts and not odd_congruence,
                "even-sign-parity mutant intended reason",
            )
            killed.add("odd-sign-parity")
        if negative_count == 3:
            need(
                odd_congruence and spectrum[0] % 8 == 6,
                "mod-eight overclaim mutant intended reason",
            )
            killed.add("odd-modulus-8")
        if negative_count == 1 and "independent-v" not in killed:
            bad_v = None
            for translation in range(1, 256):
                tick()
                candidate = [
                    v[point ^ translation] for point in range(256)
                ]
                if any(
                    u[point] * candidate[point] != 0
                    for point in range(256)
                ):
                    bad_v = candidate
                    break
            need(bad_v is not None, "independent-v mutation unavailable")
            bad_spectrum = fwht(bad_v)
            need(
                [abs(value) for value in bad_spectrum]
                == [abs(value) for value in spectrum],
                "independent-v mutant preserves every marginal magnitude",
            )
            need(
                all(value % 4 == 2 for value in bad_spectrum),
                "independent-v mutant preserves odd residues",
            )
            need(
                sum(value != 0 for value in bad_v) == 140
                and sum(value < 0 for value in bad_v) == 1,
                "independent-v mutant preserves support/sign counts",
            )
            need(
                any(u[point] * bad_v[point] != 0 for point in range(256)),
                "independent-v mutant must fail actual complementarity",
            )
            killed.add("independent-v")


def balance_zero_check(record, killed):
    if "moved-balance-zero" in killed:
        return
    spectrum = record["F"][0]
    need(spectrum[0] != 0, "balance control needs nonzero normalized DC")
    zeros = [frequency for frequency, value in enumerate(spectrum) if value == 0]
    need(bool(zeros), "C/energy control has no zero")
    carried_t = zeros[0]
    need(carried_t != 0, "carried zero must differ from normalized DC")
    u_normalized = record["u"]
    u_original = [
        character(carried_t, point >> 2) * u_normalized[point]
        for point in range(256)
    ]
    original_x = [
        sum(u_original[4 * c:4 * c + 4])
        for c in range(64)
    ]
    original_spectrum = fwht(original_x)
    need(sum(u_original) == 0, "explicit original-coordinate balance")
    need(original_spectrum[0] == 0, "original DC balance")
    need(
        all(
            original_spectrum[frequency] == spectrum[frequency ^ carried_t]
            for frequency in range(64)
        ),
        "explicit common-R modulation transport",
    )
    need(
        original_spectrum[0] == 0 and spectrum[0] != 0,
        "normalized-DC balance mutant intended reason",
    )
    killed.add("moved-balance-zero")


def eight_pair_recipe_checks(geo, catalogue):
    z2 = set(geo["Z"][:8])
    repaired = 0
    for d_count in range(23):
        tick()
        d0 = set(geo["D"][:d_count])
        eps = {point: 1 for point in d0 | z2}
        record = lift(
            geo, catalogue, d0, z2, set(), set(), eps, None
        )
        fibres = record["U"]
        support_size = sum(value != 0 for value in record["u"])
        x_energy = sum(value * value for value in fibres[0])
        y_energy = sum(value * value for value in fibres[3])
        y_zeros = sum(value == 0 for value in fibres[3])
        need(support_size == 116, "eight-pair actual support")
        need(x_energy == 48 + 4 * d_count, "eight-pair U0 energy formula")
        need(y_energy == 136 - 4 * d_count, "eight-pair U3 energy formula")
        need(y_zeros == 18 + d_count, "eight-pair U3-zero formula")
        need(
            not (x_energy == 56 and y_zeros == 23),
            "eight-pair recipe incorrectly accepted as named caller",
        )
        if x_energy == 56:
            need(d_count == 2 and y_zeros == 20, "energy-repaired recipe")
            repaired += 1
    need(repaired == 1, "eight-pair energy-repair coverage")


def run():
    global START
    START = monotonic()
    need(sys.version_info >= (3, 10), "Python 3.10 or newer required")
    need(len(sys.argv) == 1, "this checker accepts no data-file arguments")
    killed = set()
    graphs, ranks, phase_extrema, graph_checks, phase_pairs = canonical_census(
        killed
    )
    catalogue = block_catalogue()
    selected = []
    for rank in (2, 4):
        members = [f for f in graphs if ranks[f] == rank]
        selected.extend((members[0], members[-1]))
    need(len(set(selected)) == 4, "selected graph coverage")
    true_controls = 0
    false_controls = 0
    both_caps_failed = 0
    odd_controls = 0
    for f in selected:
        for r in phase_extrema[f]:
            geo = geometry(f, r, ranks[f])
            for variant in (0, 1):
                d0, z2, z4 = selected_partition(geo, variant)
                w_points = sorted(d0 | z2)
                target = xor_points(w_points)
                if ranks[f] == 4:
                    target ^= PRIMAL_E
                p_set = minimal_even_subset(geo["S"], target)
                eps = epsilon_signs(p_set, w_points)
                for requested_j in (0, 1):
                    record = lift(
                        geo, catalogue, d0, z2, z4,
                        p_set, eps, requested_j
                    )
                    facts = audit_actual_l_case(record)
                    need(facts["C"], "constructed C-true control")
                    need(
                        record["F"][0][0]
                        == 16 - 2 * facts["p"] + 2 * len(w_points)
                        - 4 * facts["n"],
                        "actual cardinality-ten DC formula",
                    )
                    need(
                        (
                            16 - 2 * facts["p"] - 4 * facts["n"]
                        ) % 8 != 0,
                        "omitted-cardinality-ten mutant intended reason",
                    )
                    killed.add("omitted-cardinality-10")
                    cap0 = all(abs(value) <= 8 for value in record["F"][0])
                    cap3 = all(abs(value) <= 12 for value in record["F"][3])
                    need(
                        not cap0 and not cap3,
                        "deterministic controls must retain unpaid caps",
                    )
                    both_caps_failed += 1
                    if requested_j == 1:
                        need(
                            facts["C"] and record["J"] == 1
                            and not cap0 and not cap3,
                            "congruence-implies-caps mutant intended reason",
                        )
                        killed.add("caps-are-not-implied")
                    complementary_checks(record, killed)
                    odd_controls += 4
                    balance_zero_check(record, killed)
                    true_controls += 1

                    bad_p = p_set ^ {geo["S"][0]}
                    bad_record = lift(
                        geo, catalogue, d0, z2, z4,
                        bad_p, eps, requested_j
                    )
                    bad_facts = audit_actual_l_case(bad_record)
                    need(
                        not bad_facts["p_even"] and not bad_facts["C"],
                        "odd-P negative control intended reason",
                    )
                    false_controls += 1

                    bad_eps = dict(eps)
                    bad_eps[w_points[0]] *= -1
                    bad_record = lift(
                        geo, catalogue, d0, z2, z4,
                        p_set, bad_eps, requested_j
                    )
                    bad_facts = audit_actual_l_case(bad_record)
                    need(
                        bad_facts["p_even"]
                        and not bad_facts["sign_ok"]
                        and bad_facts["xor_ok"]
                        and not bad_facts["C"],
                        "C-sign-parity negative control intended reason",
                    )
                    mutant_accepts = (
                        bad_facts["p_even"]
                        and not bad_facts["sign_ok"]
                        and bad_facts["xor_ok"]
                    )
                    need(
                        mutant_accepts and not bad_facts["divisible"],
                        "C-sign-parity mutant intended reason",
                    )
                    killed.add("C-sign-parity")
                    false_controls += 1

                    bad_p = p_set ^ {geo["S"][0], geo["S"][1]}
                    repaired_eps = epsilon_signs(bad_p, w_points)
                    bad_record = lift(
                        geo, catalogue, d0, z2, z4,
                        bad_p, repaired_eps, requested_j
                    )
                    bad_facts = audit_actual_l_case(bad_record)
                    need(
                        bad_facts["p_even"]
                        and bad_facts["sign_ok"]
                        and not bad_facts["xor_ok"]
                        and not bad_facts["C"],
                        "XOR-only negative control intended reason",
                    )
                    false_controls += 1

    first_f = selected[0]
    first_r = phase_extrema[first_f][0]
    eight_pair_recipe_checks(
        geometry(first_f, first_r, ranks[first_f]),
        catalogue,
    )
    required_mutants = {
        "gamma-direction",
        "gamma-bit",
        "C-sign-parity",
        "omitted-cardinality-10",
        "odd-sign-parity",
        "odd-modulus-8",
        "independent-v",
        "moved-balance-zero",
        "caps-are-not-implied",
    }
    need(killed == required_mutants, "mutation coverage mismatch")
    need(true_controls == 32, "C-true control coverage")
    need(false_controls == 96, "C-false control coverage")
    need(both_caps_failed == 32, "explicit failed-cap coverage")
    need(odd_controls == 128, "complementary parity-control coverage")
    tick()
    elapsed = monotonic() - START
    print("STATUS: PASS -- scoped finite checks only")
    print("truth_tables=65536; bent_functions=896; canonical_graphs=896")
    print("rank_two_graphs=512; rank_four_graphs=384")
    print("graph_frequency_checks=" + str(graph_checks))
    print("common_phase_pairs=" + str(phase_pairs))
    print("direct_fixed_fibre_phase_checks=one_per_graph")
    print("actual_ternary_blocks=81")
    print("actual_C_true_controls=" + str(true_controls))
    print("actual_C_false_controls=" + str(false_controls))
    print("true_controls_failing_both_amplitude_caps=" + str(both_caps_failed))
    print("actual_complementary_parity_controls=" + str(odd_controls))
    print("eight_pair_D0_cardinality_controls=23")
    print("mutants_killed=" + ",".join(sorted(killed)))
    print("elapsed_seconds=" + format(elapsed, ".6f"))
    print(
        "LIMIT: no capped even-half construction, capped complementary V, "
        "original-caller witness, NL242 closure, or novelty conclusion"
    )


if __name__ == "__main__":
    try:
        run()
    except BudgetExceeded as error:
        print("STATUS: INCOMPLETE -- " + str(error), file=sys.stderr)
        raise SystemExit(2)
    except CheckFailure as error:
        print("STATUS: FAIL -- " + str(error), file=sys.stderr)
        raise SystemExit(1)

END VERBATIM PYTHON SOURCE

## Disposition ceiling

**Overall correctness: correct.**

**Explanation:** No defect was identified in the frozen count and congruence reductions under their explicit common-physical-object assumptions. The checker above is an unexecuted source candidate, so finite corroboration remains **NOT_RUN**, not PASS; neither amplitude feasibility, an original balanced caller, nor the full NL242 target is established.

**Confidence: 0.93** for the scoped written assessment, not for an unobserved execution.

No working-tree files were written, no scientific executable or tests were run, and no external source, model, sibling scientific return, or held payload was used. Same-harness authorship is not independent-family, human, kernel, novelty, or parent-adoption assurance.