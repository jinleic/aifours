# f534 — Independent exact finite verifier for the forty-ray construction

**FINITE gate status: NOT_RUN.** The complete independent checker is supplied below. Scientific shell execution and filesystem edits are excluded by my active role constraints; I did not bypass them. No exit status, execution duration, mutation rejection, or computed vector listing is claimed as observed.

**Findings:** No evidence-backed defect identified in the frozen mathematical construction or its additive-context routing.

**overall_correctness:** correct  
**explanation:** The supplied forty-ray formulas and their transport to actual row, column, and \(L(r,c)=r+c\) contexts are consistent at the written level. The independently authored checker remains unexecuted, so this return does **not** pass the independent FINITE gate or establish a 100-ray solution.  
**confidence:** 0.92

## 1. Input boundary and chronology

Before reading the scientific body, I completely read:

- Manifest, including its ending: LF 1–116.
- Freeze receipt, including its ending: LF 1–47.
- Dispatch receipt.
- Parent live-metadata supply, including its ending.
- All twelve permission/status controls, in manifest order, including their endings.

I then sent the required direct pre-body ACK to Main. Only afterward did I read the complete literal packet, LF 1–363, in consecutive raw ranges of at most twenty LF, including the ending.

The scientific inputs actually read were:

- **S1:** f496 mathematical body, source LF 1–332 only. Its optional checker and all subsequent source lines were excluded and were not inspected.
- **S2:** the complete 29-LF disposition supplying the actual cyclic context definition and original-target boundary.

I did not follow scientific links, read sibling reviews, inspect the excluded author checker, invoke another model, or consume held scientific payloads. The quarantine controls were status/permissions inputs only. This describes observable access and chronology, not a clean-cognition certificate.

The following hashes, byte counts and LF counts are **parent-supplied observations**, not hashes or clocks independently executed by me:

| Item | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Manifest | e3b20ce36be5f12d20ac8fcc2af269ab0cbd62cfe1d6a5d1545c9d37fd06b29f | 7350 | 116 |
| Freeze receipt | ffc4d8093ef247959824a06a3e32a6eca4330e24cf8db3a2713cf0a46dcd3bf6 | 1851 | 47 |
| Literal packet | 89a3321892378e5daf6556b59e0211e2e1a66947c60a35cfd269faa2b601da51 | 21507 | 363 |
| S1 whole source, selected LF 1–332 | b12cd548fbb850d1c13d2cb06cc0e2a47adf7a34b919bec68bff70d4ed0a6784 | 21042 | 584 |
| S2 complete source | a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b | 6588 | 29 |

The whole-source S1 hash does not imply that its excluded lines were read.

## 2. Exact physical coordinates

Put
\[
h=1/\sqrt2,\qquad c_j=\cos(j\pi/16),\qquad s_j=\sin(j\pi/16).
\]

For each \(i,\epsilon\), the following table gives two explicit two-component columns \(w_i^\epsilon=(x,y)\) and \(v_i^\epsilon=(p,q)\). Here \(v_i^\epsilon=U_i^\dagger w_i^\epsilon\); the entries below follow by direct multiplication of the displayed unitaries, not by inspecting the author’s checker.

| \(i\) | \(\epsilon\) | \(w_i^\epsilon\) | \(v_i^\epsilon\) |
|---:|:---:|---|---|
| 0 | + | \(h(1,i)\) | \(h(1,i)\) |
| 0 | − | \(h(1,-i)\) | \(h(1,-i)\) |
| 1 | + | \((1,0)\) | \((-1,0)\) |
| 1 | − | \((0,1)\) | \((0,1)\) |
| 2 | + | \((c_2,s_2)\) | \((-c_2,s_2)\) |
| 2 | − | \((-s_2,c_2)\) | \((-s_2,-c_2)\) |
| 3 | + | \((c_1,s_1)\) | \((c_3,-s_3)\) |
| 3 | − | \((-s_1,c_1)\) | \((-s_3,-c_3)\) |
| 4 | + | \((c_3,s_3)\) | \((s_3,-c_3)\) |
| 4 | − | \((-s_3,c_3)\) | \((c_3,s_3)\) |

Define the four-component physical vectors, for \(\eta=\pm1\), by
\[
Q_i^{U}(\epsilon,\eta)=h(x,y,\eta p,\eta q),
\]
\[
Q_i^{V}(\epsilon,\eta)
=h\bigl(x,y,-i(-1)^i\eta p,-i(-1)^i\eta q\bigr).
\]
Thus every entry in the following table specifies four exact complex coordinates, with no free parameter or equation-solving step. Signs in the arguments are the numerical signs \(\pm1\).

### All forty actual cells

| Row | Cell assignments, in increasing column order |
|---:|---|
| 0 | \(0:Q_0^U(+,+)\); \(1:Q_4^V(+,-)\); \(5:Q_0^U(-,-)\); \(6:Q_4^V(-,-)\) |
| 1 | \(1:Q_3^V(+,-)\); \(2:Q_2^V(+,+)\); \(6:Q_3^V(-,+)\); \(7:Q_2^V(-,+)\) |
| 2 | \(2:Q_1^V(+,+)\); \(3:Q_0^V(+,-)\); \(7:Q_1^V(-,-)\); \(8:Q_0^V(-,-)\) |
| 3 | \(3:Q_4^U(+,-)\); \(4:Q_3^U(+,+)\); \(8:Q_4^U(-,+)\); \(9:Q_3^U(-,+)\) |
| 4 | \(0:Q_1^U(-,-)\); \(4:Q_2^U(+,+)\); \(5:Q_1^U(+,-)\); \(9:Q_2^U(-,-)\) |
| 5 | \(0:Q_0^U(-,+)\); \(1:Q_4^V(-,+)\); \(5:Q_0^U(+,-)\); \(6:Q_4^V(+,+)\) |
| 6 | \(1:Q_3^V(-,-)\); \(2:Q_2^V(-,-)\); \(6:Q_3^V(+,+)\); \(7:Q_2^V(+,-)\) |
| 7 | \(2:Q_1^V(-,+)\); \(3:Q_0^V(-,+)\); \(7:Q_1^V(+,-)\); \(8:Q_0^V(+,+)\) |
| 8 | \(3:Q_4^U(-,-)\); \(4:Q_3^U(-,-)\); \(8:Q_4^U(+,+)\); \(9:Q_3^U(+,-)\) |
| 9 | \(0:Q_1^U(+,+)\); \(4:Q_2^U(-,+)\); \(5:Q_1^U(-,+)\); \(9:Q_2^U(+,-)\) |

These are exactly the cells with \(c-r\in\{0,1,5,6\}\pmod {10}\).

For distinct \(i\), the first two-component rays are eigenrays of different, non-antipodal Bloch axes
\[
Y,\ Z,\ N(\pi/4),\ N(\pi/8),\ N(3\pi/8).
\]
Their eigenray sets are disjoint. For fixed \(i,\epsilon\), the four possible relative lower-block factors are \(1,-1,i,-i\), and both blocks are nonzero. This establishes the written nonparallelness argument independently of a numerical tolerance.

## 3. All thirty actual consumer contexts

For a row, the listed numbers are columns. For a column, they are rows.

| Label | Row-context columns | Column-context rows |
|---:|---|---|
| 0 | 0, 1, 5, 6 | 0, 4, 5, 9 |
| 1 | 1, 2, 6, 7 | 0, 1, 5, 6 |
| 2 | 2, 3, 7, 8 | 1, 2, 6, 7 |
| 3 | 3, 4, 8, 9 | 2, 3, 7, 8 |
| 4 | 0, 4, 5, 9 | 3, 4, 8, 9 |
| 5 | 0, 1, 5, 6 | 0, 4, 5, 9 |
| 6 | 1, 2, 6, 7 | 0, 1, 5, 6 |
| 7 | 2, 3, 7, 8 | 1, 2, 6, 7 |
| 8 | 3, 4, 8, 9 | 2, 3, 7, 8 |
| 9 | 0, 4, 5, 9 | 3, 4, 8, 9 |

The **additive** symbol contexts are:

| \(k\) | Cells satisfying \(r+c=k\pmod {10}\) |
|---:|---|
| 0 | (0,0), (2,8), (5,5), (7,3) |
| 1 | (0,1), (3,8), (5,6), (8,3) |
| 2 | (1,1), (3,9), (6,6), (8,4) |
| 3 | (1,2), (4,9), (6,7), (9,4) |
| 4 | (2,2), (4,0), (7,7), (9,5) |
| 5 | (0,5), (2,3), (5,0), (7,8) |
| 6 | (0,6), (3,3), (5,1), (8,8) |
| 7 | (1,6), (3,4), (6,1), (8,9) |
| 8 | (1,7), (4,4), (6,2), (9,9) |
| 9 | (2,7), (4,5), (7,2), (9,0) |

There are forty norm obligations, thirty four-vector Gram-matrix obligations, and \(30\binom42=180\) distinct prescribed orthogonal pairs. There are \(\binom{40}{2}=780\) global nonparallelness obligations. These are the exact combinatorial counts, **not a report that the checker executed them**.

## 4. Exact arithmetic and independence of the checker

The implementation below uses only the defining vector formulas and actual cell/context definitions.

Its arithmetic is
\[
\mathbb Z[\zeta_{32},1/2]\subset\mathbb Q(\zeta_{32}),
\qquad \zeta_{32}^{16}=-1,
\]
represented by sixteen integer coefficients and a common power-of-two denominator. No approximate complex arithmetic is used.

This representation has a valid equality test: \(x^{16}+1=\Phi_{32}(x)\) is irreducible over \(\mathbb Q\). Indeed \((x+1)^{16}+1\) is Eisenstein at two: its constant term is two, all intermediate binomial coefficients are even, and its leading coefficient is one.

Conjugation sends \(\zeta_{32}^k\) to \(\zeta_{32}^{-k}\). The checker independently compares multiplication and conjugation with the complete 32-power algebra, checks the trigonometric identities used by the coordinates, and checks unitary recurrence and closing identities before validating the physical array.

The global test is exactly
\[
|\langle q_p,q_q\rangle|^2\ne1.
\]
For normalized complex vectors, equality to one is equivalent to parallelness by equality in Cauchy–Schwarz.

### Mutation contract

All mutations are generated in memory. No fixture file is written or deleted.

| Mutation | Intended rejection | Status here |
|---|---|---|
| Use \(r-c\) symbol routing | CONTEXT_MEMBERSHIP | NOT_RUN |
| Use quotient bits \(r//5,c//5\), i.e. erroneous inverse-CRT bit convention | CONTEXT_GRAM | NOT_RUN |
| Omit the imaginary factor in the V branch | PARALLEL_PAIR | NOT_RUN |
| Duplicate one context | CONTEXT_ID | NOT_RUN |
| Duplicate one ray | PARALLEL_PAIR | NOT_RUN |
| Replace \(U_4=-iY\) by \(+iY\) | CONTEXT_GRAM | NOT_RUN |
| Remove both B-block minus signs | CONTEXT_GRAM | NOT_RUN |
| Supply only 39 rays | CELL_DOMAIN | NOT_RUN |

An unexpected exception is not counted as an intended rejection. An unexpected rejection tag fails the control campaign. A mutation that passes is printed as **NOTTESTED_NONDISCRIMINATING**, and prevents the final PASS_FINITE_ONLY result.

For the erroneous inverse-CRT convention, both blockwise bit maps remain bijective, so it is important not to mistake preservation of forty distinct rays for correctness. The resulting additive-symbol routing changes: for example, the A\(_0\) and B\(_2\) contributions to symbol zero occupy the same \(g_0\) eigenspace instead of complementary eigenspaces. The physical Gram test, not merely a ray count, is therefore required.

## 5. Complete prospective argv

**NOT_RUN.** Interpreter availability, version, binary hash, elapsed time, exit code, stdout and stderr have not been observed by this role.

- Executable: python3
- Argument 1: -B
- Argument 2: -c
- Argument 3: the complete literal source between the BEGIN SOURCE and END SOURCE markers below, excluding the markers
- Argument 4: --max-seconds
- Argument 5: 55
- Standard input: closed / DEVNULL
- No shell expansion, subprocess, network, package installation, or explicit filesystem access is used by the program.

The code has a cooperative 55-second deadline. Reaching it produces an inconclusive result, never a PASS. Whether this implementation finishes within that bound is unobserved.

## 6. Complete independent checker source

BEGIN SOURCE

import sys
import time


class CheckFailure(Exception):
    def __init__(self, tag, detail):
        self.tag = tag
        super().__init__(tag + ": " + detail)


class BudgetExceeded(Exception):
    pass


DEADLINE = None


def tick():
    if DEADLINE is not None and time.monotonic() >= DEADLINE:
        raise BudgetExceeded("cooperative 55-second deadline reached")


def need(condition, tag, detail):
    if not condition:
        raise CheckFailure(tag, detail)


class E:
    """sum(n[k] * zeta**k, k=0..15) / 2**e; zeta**16 = -1."""

    __slots__ = ("n", "e")

    def __init__(self, coefficients, exponent=0):
        n = tuple(coefficients)
        need(
            len(n) == 16 and all(type(x) is int for x in n),
            "ARITHMETIC_SHAPE",
            "sixteen integer coefficients required",
        )
        need(
            type(exponent) is int and exponent >= 0,
            "ARITHMETIC_DENOMINATOR",
            "nonnegative dyadic exponent required",
        )
        if not any(n):
            self.n = (0,) * 16
            self.e = 0
            return
        while exponent and all((x & 1) == 0 for x in n):
            n = tuple(x // 2 for x in n)
            exponent -= 1
        self.n = n
        self.e = exponent

    def __bool__(self):
        return any(self.n)

    def __eq__(self, other):
        return (
            isinstance(other, E)
            and self.e == other.e
            and self.n == other.n
        )

    def __neg__(self):
        return E(tuple(-x for x in self.n), self.e)

    def __add__(self, other):
        if not isinstance(other, E):
            return NotImplemented
        exponent = max(self.e, other.e)
        left_shift = exponent - self.e
        right_shift = exponent - other.e
        return E(
            tuple(
                (a << left_shift) + (b << right_shift)
                for a, b in zip(self.n, other.n)
            ),
            exponent,
        )

    def __sub__(self, other):
        if not isinstance(other, E):
            return NotImplemented
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, E):
            return NotImplemented
        if not self or not other:
            return ZERO
        result = [0] * 16
        for a, x in enumerate(self.n):
            if not x:
                continue
            for b, y in enumerate(other.n):
                if not y:
                    continue
                degree = a + b
                if degree < 16:
                    result[degree] += x * y
                else:
                    result[degree - 16] -= x * y
        return E(result, self.e + other.e)

    def scale(self, integer):
        need(type(integer) is int, "ARITHMETIC_SCALAR", "integer required")
        return E(tuple(integer * x for x in self.n), self.e)

    def half(self):
        return E(self.n, self.e + 1)

    def conjugate(self):
        result = [0] * 16
        result[0] = self.n[0]
        for k in range(1, 16):
            result[16 - k] = -self.n[k]
        return E(result, self.e)

    def text(self):
        return (
            "2^(-" + str(self.e) + ")*("
            + ",".join(str(x) for x in self.n)
            + ")"
        )


ZERO = E((0,) * 16)
ONE = E((1,) + (0,) * 15)


def power(k):
    k %= 32
    result = [0] * 16
    result[k % 16] = 1 if k < 16 else -1
    return E(result)


IMAG = power(8)


def cosine(k):
    return (power(k) + power(-k)).half()


def sine(k):
    return ((power(k) - power(-k)) * (-IMAG)).half()


HALF_ROOT = cosine(4)


def sign(k):
    return -1 if k % 2 else 1


def esum(values):
    result = ZERO
    for value in values:
        result = result + value
    return result


def audit_field():
    zeta = power(1)
    current = ONE
    for k in range(32):
        tick()
        need(current == power(k), "POWER_ALGEBRA", "power " + str(k))
        current = current * zeta
    need(current == ONE, "POWER_ALGEBRA", "zeta^32 must be one")
    need(power(16) == -ONE, "FIELD_RELATION", "zeta^16 must be -1")
    for a in range(32):
        tick()
        pa = power(a)
        need(
            pa.conjugate() == power(-a),
            "CONJUGATION",
            "power " + str(a),
        )
        need(
            pa.conjugate().conjugate() == pa,
            "CONJUGATION",
            "involution at power " + str(a),
        )
        for b in range(32):
            tick()
            product = pa * power(b)
            need(
                product == power(a + b),
                "POWER_ALGEBRA",
                "product " + str((a, b)),
            )
            need(
                product.conjugate()
                == pa.conjugate() * power(b).conjugate(),
                "CONJUGATION",
                "product " + str((a, b)),
            )
    need(IMAG * IMAG == -ONE, "IMAGINARY_UNIT", "i^2")
    need(IMAG.conjugate() == -IMAG, "IMAGINARY_UNIT", "conjugate(i)")
    need(
        HALF_ROOT * HALF_ROOT == ONE.half(),
        "NORMALIZATION_CONSTANT",
        "(1/sqrt(2))^2",
    )
    for k in range(32):
        tick()
        c, s = cosine(k), sine(k)
        need(
            c.conjugate() == c and s.conjugate() == s,
            "TRIG_REALITY",
            "angle index " + str(k),
        )
        need(
            c * c + s * s == ONE,
            "TRIG_IDENTITY",
            "angle index " + str(k),
        )


I2 = ((ONE, ZERO), (ZERO, ONE))
Y = ((ZERO, -IMAG), (IMAG, ZERO))


def dagger(matrix):
    return tuple(
        tuple(matrix[j][i].conjugate() for j in range(len(matrix)))
        for i in range(len(matrix[0]))
    )


def matrix_product(left, right):
    return tuple(
        tuple(
            esum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def matrix_scale(matrix, scalar):
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in matrix
    )


def matrix_vector(matrix, vector):
    return tuple(
        esum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    )


ANGLE_HALF_INDICES = (0, 0, 2, 1, 3)


def reflection(k):
    c, s = cosine(k), sine(k)
    return ((c, s), (s, -c))


def unitaries():
    h = HALF_ROOT
    c, s = cosine(2), sine(2)
    return (
        I2,
        ((-ONE, ZERO), (ZERO, ONE)),
        ((-h, h), (-h, -h)),
        ((c, -s), (-s, -c)),
        ((ZERO, -ONE), (ONE, ZERO)),
    )


def audit_unitaries(values):
    need(len(values) == 5, "UNITARY_COUNT", "five matrices required")
    for i, matrix in enumerate(values):
        tick()
        need(
            matrix_product(dagger(matrix), matrix) == I2,
            "UNITARITY",
            "U_" + str(i),
        )
    need(values[0] == I2, "UNITARY_START", "U_0")
    need(
        values[4] == matrix_scale(Y, -IMAG),
        "U4_CLOSURE",
        "U_4 must equal -iY",
    )
    for i in range(1, 5):
        tick()
        ni = reflection(2 * ANGLE_HALF_INDICES[i])
        expected = matrix_scale(
            matrix_product(ni, values[i - 1]),
            ONE.scale(sign(i)),
        )
        need(
            values[i] == expected,
            "UNITARY_RECURRENCE",
            "index " + str(i),
        )


A_MAP = ((0, "U"), (3, "V"), (1, "V"), (4, "U"), (2, "U"))
B_MAP = ((4, "V"), (2, "V"), (0, "V"), (3, "U"), (1, "U"))
SUPPORT = (0, 1, 5, 6)
CELLS = tuple(
    (r, c)
    for r in range(10)
    for c in range(10)
    if (c - r) % 10 in SUPPORT
)


def upper_vector(i, epsilon):
    need(epsilon in (-1, 1), "EIGENVALUE_LABEL", str(epsilon))
    if i == 0:
        return (HALF_ROOT, (HALF_ROOT * IMAG).scale(epsilon))
    k = ANGLE_HALF_INDICES[i]
    c, s = cosine(k), sine(k)
    return (c, s) if epsilon == 1 else (-s, c)


def physical_vector(i, branch, epsilon, eta, values, omit_imaginary=False):
    need(eta in (-1, 1), "EIGENVALUE_LABEL", str(eta))
    need(branch in ("U", "V"), "BRANCH_LABEL", str(branch))
    upper = upper_vector(i, epsilon)
    lower = tuple(
        x.scale(eta)
        for x in matrix_vector(dagger(values[i]), upper)
    )
    if branch == "V":
        phase = (-ONE if omit_imaginary else -IMAG).scale(sign(i))
        lower = tuple(phase * x for x in lower)
    return tuple(HALF_ROOT * x for x in upper + lower)


def make_array(
    wrong_crt=False,
    omit_imaginary=False,
    wrong_u4=False,
    bad_b_signs=False,
):
    values = list(unitaries())
    if wrong_u4:
        values[4] = matrix_scale(values[4], -ONE)
    result = {}
    for r, c in CELLS:
        tick()
        a, b = r % 5, c % 5
        u = r // 5 if wrong_crt else r % 2
        v = c // 5 if wrong_crt else c % 2
        delta = (b - a) % 5
        need(delta in (0, 1), "SUPPORT_CRT", str((r, c)))
        if delta == 0:
            i, branch = A_MAP[a]
            epsilon, eta = sign(u + v), sign(v)
        else:
            i, branch = B_MAP[a]
            epsilon, eta = -sign(u + v), -sign(u)
            if bad_b_signs:
                epsilon, eta = -epsilon, -eta
        result[(r, c)] = physical_vector(
            i, branch, epsilon, eta, values, omit_imaginary
        )
    return result


def make_contexts(cells, minus_symbol=False):
    result = []
    for kind in ("R", "C", "L"):
        for label in range(10):
            tick()
            if kind == "R":
                group = tuple(p for p in cells if p[0] == label)
            elif kind == "C":
                group = tuple(p for p in cells if p[1] == label)
            else:
                group = tuple(
                    p for p in cells
                    if (
                        (p[0] - p[1]) if minus_symbol
                        else (p[0] + p[1])
                    ) % 10 == label
                )
            result.append((kind, label, group))
    return tuple(result)


def expected_context(kind, label):
    if kind == "R":
        return tuple(sorted((label, (label + d) % 10) for d in SUPPORT))
    if kind == "C":
        return tuple(sorted(((label - d) % 10, label) for d in SUPPORT))
    return tuple(
        (r, (label - r) % 10)
        for r in range(10)
        if (label - 2 * r) % 10 in SUPPORT
    )


def audit_context_layout(contexts):
    need(len(contexts) == 30, "CONTEXT_COUNT", "exactly thirty required")
    expected_ids = {(kind, k) for kind in ("R", "C", "L") for k in range(10)}
    seen = set()
    for kind, label, group in contexts:
        tick()
        identifier = (kind, label)
        need(
            identifier in expected_ids and identifier not in seen,
            "CONTEXT_ID",
            str(identifier),
        )
        seen.add(identifier)
        need(
            tuple(group) == expected_context(kind, label),
            "CONTEXT_MEMBERSHIP",
            str(identifier),
        )
        need(len(group) == 4, "CONTEXT_SIZE", str(identifier))
    need(seen == expected_ids, "CONTEXT_ID", "missing context")


def inner(left, right):
    return esum(a.conjugate() * b for a, b in zip(left, right))


def verify(vectors, contexts):
    tick()
    need(
        set(vectors) == set(CELLS),
        "CELL_DOMAIN",
        "expected exactly the forty actual support cells",
    )
    audit_context_layout(contexts)
    for cell in CELLS:
        tick()
        vector = vectors[cell]
        need(
            len(vector) == 4 and all(isinstance(x, E) for x in vector),
            "VECTOR_SHAPE",
            str(cell),
        )
        need(
            inner(vector, vector) == ONE,
            "UNIT_NORM",
            str(cell),
        )
    gram = {}
    zero_pairs = 0
    for i, left_cell in enumerate(CELLS):
        for right_cell in CELLS[i + 1:]:
            tick()
            value = inner(vectors[left_cell], vectors[right_cell])
            squared_absolute = value.conjugate() * value
            need(
                squared_absolute.conjugate() == squared_absolute,
                "PAIR_REALITY",
                str((left_cell, right_cell)),
            )
            need(
                squared_absolute != ONE,
                "PARALLEL_PAIR",
                str((left_cell, right_cell)),
            )
            gram[(left_cell, right_cell)] = value
            if value == ZERO:
                zero_pairs += 1
    need(len(gram) == 780, "PAIR_COUNT", str(len(gram)))
    prescribed = set()
    context_pair_count = 0
    for kind, label, group in contexts:
        for i, left_cell in enumerate(group):
            for right_cell in group[i + 1:]:
                tick()
                pair = tuple(sorted((left_cell, right_cell)))
                need(
                    gram[pair] == ZERO,
                    "CONTEXT_GRAM",
                    str((kind, label, pair)),
                )
                prescribed.add(pair)
                context_pair_count += 1
    need(
        context_pair_count == 180 and len(prescribed) == 180,
        "CONTEXT_PAIR_COUNT",
        str((context_pair_count, len(prescribed))),
    )
    return (40, 30, context_pair_count, len(gram), zero_pairs)


def audit_orbit(vectors, contexts):
    full_grid = tuple((r, c) for r in range(10) for c in range(10))
    expected_masks = {
        tuple(sorted((a, a + 5, b, b + 5)))
        for a in range(5)
        for b in range(a + 1, 5)
    }
    hits = {}
    transformations = 0
    transported_contexts = 0
    for h in (1, 3, 7, 9):
        for t in range(10):
            tick()

            def image(cell):
                r, c = cell
                return ((h * r) % 10, (h * c + t) % 10)

            need(
                {image(p) for p in full_grid} == set(full_grid),
                "ORBIT_GRID_BIJECTION",
                str((h, t)),
            )
            for r, c in full_grid:
                tick()
                rr, cc = image((r, c))
                need(
                    (rr + cc) % 10 == (h * ((r + c) % 10) + t) % 10,
                    "ORBIT_SYMBOL_ROUTING",
                    str((h, t, r, c)),
                )
            mask = tuple(sorted((h * d + t) % 10 for d in SUPPORT))
            target_cells = tuple(
                (r, c)
                for r, c in full_grid
                if (c - r) % 10 in mask
            )
            transported = {image(p): vectors[p] for p in CELLS}
            need(
                len(transported) == 40 and set(transported) == set(target_cells),
                "ORBIT_SUPPORT",
                str((h, t, mask)),
            )
            for p in CELLS:
                need(
                    transported[image(p)] == vectors[p],
                    "ORBIT_VECTOR_TRANSPORT",
                    str((h, t, p)),
                )
            target_contexts = {
                (kind, label): group
                for kind, label, group in make_contexts(target_cells)
            }
            for kind, label, group in contexts:
                tick()
                new_label = (
                    (h * label) % 10 if kind == "R"
                    else (h * label + t) % 10
                )
                actual_image = tuple(sorted(image(p) for p in group))
                need(
                    actual_image == target_contexts[(kind, new_label)],
                    "ORBIT_CONTEXT_TRANSPORT",
                    str((h, t, kind, label)),
                )
                transported_contexts += 1
            hits[mask] = hits.get(mask, 0) + 1
            transformations += 1
    need(set(hits) == expected_masks, "ORBIT_MASK_SET", str(sorted(hits)))
    need(
        transformations == 40
        and transported_contexts == 1200
        and all(value == 4 for value in hits.values()),
        "ORBIT_COUNTS",
        str((transformations, transported_contexts, sorted(hits.values()))),
    )
    return hits


def run_control(name, operation, expected_tag):
    tick()
    try:
        operation()
    except CheckFailure as error:
        need(
            error.tag == expected_tag,
            "CONTROL_WRONG_REASON",
            name + ": expected " + expected_tag + ", received " + str(error),
        )
        return (name, "REJECTED_INTENDED", error.tag)
    return (name, "NOTTESTED_NONDISCRIMINATING", "no rejection")


PINS = (
    (
        "manifest_parent_supplied",
        "e3b20ce36be5f12d20ac8fcc2af269ab0cbd62cfe1d6a5d1545c9d37fd06b29f",
    ),
    (
        "freeze_receipt_parent_supplied",
        "ffc4d8093ef247959824a06a3e32a6eca4330e24cf8db3a2713cf0a46dcd3bf6",
    ),
    (
        "literal_packet_parent_supplied",
        "89a3321892378e5daf6556b59e0211e2e1a66947c60a35cfd269faa2b601da51",
    ),
    (
        "S1_whole_source_parent_supplied_SELECTED_LF_1_332_ONLY",
        "b12cd548fbb850d1c13d2cb06cc0e2a47adf7a34b919bec68bff70d4ed0a6784",
    ),
    (
        "S2_whole_source_parent_supplied_COMPLETE_LF_1_29",
        "a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b",
    ),
)


def main():
    global DEADLINE
    need(
        sys.argv[1:] == ["--max-seconds", "55"],
        "ARGV",
        "required arguments: --max-seconds 55",
    )
    started = time.monotonic()
    DEADLINE = started + 55.0
    audit_field()
    audit_unitaries(unitaries())
    need(len(CELLS) == 40, "SUPPORT_SIZE", str(len(CELLS)))
    base = make_array()
    contexts = make_contexts(CELLS)
    counts = verify(base, contexts)
    masks = audit_orbit(base, contexts)

    duplicate_ray = dict(base)
    duplicate_ray[CELLS[1]] = base[CELLS[0]]
    duplicate_context = list(contexts)
    duplicate_context[-1] = duplicate_context[-2]
    short_array = {p: base[p] for p in CELLS[:-1]}

    tests = (
        (
            "wrong_symbol_r_minus_c",
            lambda: verify(base, make_contexts(CELLS, minus_symbol=True)),
            "CONTEXT_MEMBERSHIP",
        ),
        (
            "wrong_inverse_CRT_bits",
            lambda: verify(make_array(wrong_crt=True), contexts),
            "CONTEXT_GRAM",
        ),
        (
            "omitted_imaginary_phase",
            lambda: verify(make_array(omit_imaginary=True), contexts),
            "PARALLEL_PAIR",
        ),
        (
            "duplicate_context",
            lambda: verify(base, tuple(duplicate_context)),
            "CONTEXT_ID",
        ),
        (
            "duplicate_ray",
            lambda: verify(duplicate_ray, contexts),
            "PARALLEL_PAIR",
        ),
        (
            "wrong_U4_closing",
            lambda: verify(make_array(wrong_u4=True), contexts),
            "CONTEXT_GRAM",
        ),
        (
            "bad_B_signs",
            lambda: verify(make_array(bad_b_signs=True), contexts),
            "CONTEXT_GRAM",
        ),
        (
            "only_39_rays",
            lambda: verify(short_array, contexts),
            "CELL_DOMAIN",
        ),
    )
    control_results = tuple(
        run_control(name, operation, expected)
        for name, operation, expected in tests
    )
    tick()

    print("ARITHMETIC Q(zeta_32), zeta_32^16=-1")
    print("ENTRY_FORMAT 2^(-e)*(n0,...,n15) in basis 1,zeta,...,zeta^15")
    print("PIN_STATUS declared parent-supplied pins; no source-file reads")
    for name, digest in PINS:
        print("DECLARED_PIN", name, digest)
    print("SOURCE_BOUNDARY S1 LF1-332 only; author checker excluded")
    for r, c in CELLS:
        tick()
        print(
            "VECTOR", r, c,
            " | ".join(entry.text() for entry in base[(r, c)]),
        )
    for kind, label, group in contexts:
        tick()
        print(
            "CONTEXT", kind, label,
            " ".join("(%d,%d)" % p for p in group),
        )
    for mask in sorted(masks):
        print(
            "ORBIT_MASK",
            ",".join(str(d) for d in mask),
            "AFFINE_PREIMAGES", masks[mask],
        )
    for name, status, reason in control_results:
        print("CONTROL", name, status, reason)
    print(
        "COUNTS",
        "unit_norms", counts[0],
        "contexts", counts[1],
        "prescribed_orthogonal_pairs", counts[2],
        "global_nonparallel_pairs", counts[3],
        "all_zero_inner_product_pairs", counts[4],
    )
    print("ORBIT_COUNTS masks 10 affine_maps 40 transported_contexts 1200")
    print("LIMIT full100 NOT_ESTABLISHED; complementary60 NOT_SUPPLIED")
    print("LIMIT no human, kernel, independent-family, priority or novelty claim")
    tick()
    print("ELAPSED_MONOTONIC_SECONDS", "%.6f" % (time.monotonic() - started))
    if any(status != "REJECTED_INTENDED" for _, status, _ in control_results):
        print("RESULT: FINITE_POSITIVE_VALID_CONTROLS_INCOMPLETE")
        return 2
    print("RESULT: PASS_FINITE_ONLY")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BudgetExceeded as error:
        print("RESULT: INCONCLUSIVE_TIME_LIMIT", file=sys.stderr)
        print(str(error), file=sys.stderr)
        sys.exit(2)
    except CheckFailure as error:
        print("RESULT: FAIL_FINITE", file=sys.stderr)
        print(str(error), file=sys.stderr)
        sys.exit(1)

END SOURCE

## 7. Orbit and remaining sixty-ray obligation

The ten masks addressed by affine transport are exactly:

- {0,1,5,6}
- {0,2,5,7}
- {0,3,5,8}
- {0,4,5,9}
- {1,2,6,7}
- {1,3,6,8}
- {1,4,6,9}
- {2,3,7,8}
- {2,4,7,9}
- {3,4,8,9}

For \(h\in\{1,3,7,9\}\) and \(t\in\mathbb Z_{10}\), the cell map
\[
(r,c)\mapsto(hr,hc+t)
\]
takes row label \(r\) to \(hr\), column label \(c\) to \(hc+t\), and the **actual additive symbol label** \(k\) to \(hk+t\). The code checks this at the consuming contexts, not only at the support producer. Transport is a permutation of assigned vectors; no unitary covariance of the rays is assumed.

For the representative mask, the unsupplied complement is precisely
\[
c-r\in\{2,3,4,7,8,9\}\pmod {10},
\]
equivalently \(b-a\in\{2,3,4\}\pmod5\) in CRT coordinates.

The unpaid physical obligation is:

- sixty actual unit vectors in \(\mathbb C^6\), one per complementary cell;
- all sixty rays pairwise nonparallel;
- each of the ten restricted rows, ten restricted columns and ten additive-symbol contexts a six-vector ONB.

That would require sixty norm checks, 450 distinct prescribed orthogonal-pair conditions, and 1,770 global nonparallel-pair conditions. **No such vectors or proof of impossibility are supplied here.**

If that complement is constructed, its orthogonal direct sum with the forty-ray sector gives the full 100-ray array. The existence of the forty-ray sector alone does not supply that complement.

## 8. Final evidence disposition

- Independent checker implementation: **complete source supplied**.
- Independent checker execution: **NOT_RUN**.
- Intended-reason mutation results: **NOT_RUN**, not credited.
- Independent FINITE gate: **unpassed**.
- Parent’s earlier author-checker execution: not reproduced or adopted as my independent execution.
- Full 100-ray construction or unrestricted no-go: **not established**.
- Other surviving support orbit, rank-28 \(5+5\), noncirculant supports and other resolutions: unchanged.
- Triple verification, independent-family, human, formal/kernel, priority and novelty assurance: **none claimed**.
- Files written or modified by this role: none.