# F450 — Independent exact A₂ second-arm candidate

**Role: FINITE. Execution status: NOT RUN. Parent disposition: pending.**

This return contains an independently authored, standard-library exact-rational checker, its complete input specification and argv, and a separate written reconstruction of the assigned finite case. No executable result, elapsed time, source hash, or successful run is claimed.

## 1. Frozen scope and provenance

The assigned case is precisely
\[
(r,s)=(1,3),\qquad
A=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-3&2\end{pmatrix}.
\]

The following observations are **parent-attributed**, not child-executed:

- Manifest SHA256: `8ca3988f90f691910d9a1659d87b417e4b2fa56d786ec7e51b7e13285b46a323`.
- Freeze-receipt SHA256: `58e38a09a3753807aff0e8c1bda1202a56c47d54f969360c975d33706bee9c63`.
- Packet SHA256: `0d0170631e4553ba79a9d6a264f08de4d4151bc148bdb80a979e725c0fffd299`.
- Parent live observation: `2026-10-30T11:31:28-0700 PDT`.
- Parent reports that all assigned hashes, byte counts, and LF counts match.

Actual access chronology:

1. Read the required memory summary and applicable verification/review/orchestration skills as procedural context.
2. Read the complete manifest, freeze receipt, dispatch receipt, and parent live metadata.
3. Read all eight permission/status controls through their endings **before** packet access.
4. Read the complete packet in ordered raw windows of at most twenty LF lines: `1–20`, `21–40`, continuing consecutively through `901–920`, then `921–940`, which ended at packet line 930, `S3|74`.
5. Re-read packet lines `929–930` to confirm its ending.
6. Reconstructed the finite model and authored the checker below.

No linked author program, sibling scientific return, additional public source, or held scientific payload was opened. All F439, PH, AME, CORE, privacy, and L1 quarantine records were used only as status/permission controls. This is an access chronology, not a claim of cognitive isolation.

The fixed case and the vector \(y\) below are already present in the frozen assignment/packet; they are not undisclosed privately selected WRITTEN diagnostics.

## 2. Written reconstruction — not executed output

### 2.1 A concrete 24-dimensional first-arm module

Let \(P_{3,1}\) consist of polynomials homogeneous of degree three in \(x_1,x_2,x_3\) and degree one in \(y_1,y_2,y_3\). Thus
\[
\dim P_{3,1}=10\cdot3=30.
\]
Define
\[
\Delta=\sum_{i=1}^3\partial_{x_i}\partial_{y_i},\qquad
t=\sum_{i=1}^3x_i y_i,\qquad K=\ker\Delta.
\]
For a degree-two polynomial \(f(x)\),
\[
\Delta(tf)=5f.
\]
Consequently \(\Delta:P_{3,1}\to\operatorname{Sym}^2(\mathbb C^3)\) is onto and \(\dim K=30-6=24\).

Use
\[
\begin{aligned}
E_1&=x_1\partial_{x_2}-y_2\partial_{y_1},&
F_1&=x_2\partial_{x_1}-y_1\partial_{y_2},\\
E_3&=x_2\partial_{x_3}-y_3\partial_{y_2},&
F_3&=x_3\partial_{x_2}-y_2\partial_{y_3}.
\end{aligned}
\]
These operators commute with \(\Delta\) and satisfy the \(A_2\) Chevalley relations. For
\[
v=x_3^3y_1,
\]
one obtains
\[
F_1v=F_3v=0,\quad h_1v=-v,\quad h_3v=-3v,\quad
E_1^2v=E_3^4v=0.
\]

This identifies \(K\) with the adopted first-arm module, rather than merely giving it a representation-theoretic name: the lowest-weight module with labels \((1,3)\) has dimension \(24\), and its nonzero lowest vector lies in the \(24\)-dimensional kernel. The checker additionally constructs an explicit kernel basis and checks cyclic generation directly.

For an ambient monomial \(x^p y_j\), its Cartan weights are
\[
h_1=p_1-p_2-\delta_{j1}+\delta_{j2},\qquad
h_3=p_2-p_3-\delta_{j2}+\delta_{j3}.
\]
For coefficient \(b\), actual grading is recovered by
\[
a=\frac{2h_1+h_3+5b}{3},\qquad
n=\frac{h_1+2h_3+7b}{3}.
\]
Thus the checker derives grades from Cartan actions, not from guessed placement.

### 2.2 Both whole relation modules

Inside \(\Lambda^2K\), of dimension \(\binom{24}{2}=276\), take
\[
q_1=v\wedge E_1v,\qquad q_3=v\wedge E_3v.
\]
They are nonzero joint simple-lowest vectors. Their labels and actual starting grades are respectively
\[
(0,7),\ (a,n)=(1,0);
\qquad
(3,4),\ (a,n)=(0,1).
\]
Their irreducible dimensions are
\[
D(0,7)=36,\qquad D(3,4)=90.
\]
The labels differ, so their generated submodules have zero intersection. Hence the finite quotient has dimension
\[
276-36-90=150.
\]

The checker constructs each **complete positive closure**, verifies its invariance under both lowering operators as well, and checks its full graded character against an independently implemented Gelfand–Tsetlin character calculation. It does not substitute two seed ranks for their entire closures.

The identification with the actual second-arm quotient remains conditional on the retained f276 actual-source/whole-ideal bridge and the adopted first-arm identification. This calculation does not independently establish closure of the negative ideal.

### 2.3 The complete top grade

The first-arm top grade is
\[
K_4=\operatorname{span}\{x_1^i x_2^{3-i}y_3:0\le i\le3\}\cong V_3.
\]
Its actual horizontal degrees are \(1,2,3,4\). Therefore the exterior-square character at grade eight is
\[
x^3+x^4+2x^5+x^6+x^7.
\]
The \(q_1\) module ends at grade seven. The \(q_3\) module contributes at grade eight exactly \(V_4\), with character
\[
x^3+x^4+x^5+x^6+x^7.
\]
The quotient therefore has exactly
\[
N_8\cong V_0,\qquad \dim N_{(5,8)}=1,
\]
and no other horizontal degree at third grade eight.

These are written character calculations, not program output.

### 2.4 Every consuming target at grade eight

Retain all eight f306 terms, including its mixed inverse Gram block. Their final targets on input \((a,2,n)\) are:

| Operators | Final target |
|---|---|
| \(W_0\) | \(N_{(a,n-1)}\) |
| \(W_1\) | \(N_{(a-1,n-1)}\) |
| \(W_2\) | \(M_{(a,n-1)}\) |
| \(W_3,W_4\) | \(M_{(a-1,n-1)}\) |
| \(W_5\) | \(M_{(a-2,n-1)}\) |
| \(W_6\) | \((\mathfrak g_{13})_{(a-1,n-1)}\) |
| \(W_7\) | \((\mathfrak g_{13})_{(a-2,n-1)}\) |

Here \(M_7=0\), and the positive \(A_2\) roots of \(\mathfrak g_{13}\) have third grade at most one. Thus **only after checking the consuming targets** may \(W_2,\ldots,W_7\) be discarded at grade eight.

Writing
\[
T=E_3,\quad Z=[E_1,E_3],\quad D=[F_3,F_1],
\]
the full contraction there is
\[
A^0=TF_3+ZD.
\]
Both \(T\) and \(Z\) kill the top grade. Since
\[
[Z,D]=h_1+h_3,
\]
its restriction is \(h_1+2h_3\). At \((a,b,n)=(5,2,8)\), the weights are \((h_1,h_3)=(0,5)\), giving
\[
\overline A_8=10I.
\]

The same final-target vanishing applies to grades six and seven in this fixed case. The supplied program includes exact rank checks there, but these have not been executed.

### 2.5 Actual \(F_2\), and an actually active omitted-arm control

Let
\[
y=[Tv,T^2v].
\]
The actual Chevalley relations give
\[
F_2v=-h_2,\qquad F_2Tv=-e_3,\qquad F_2T^2v=0,
\]
so
\[
F_2y=-T^3v.
\]
This follows by derivation and Cartan normal ordering, not by defining \(F_2\) as an adjoint on the finite model. The source below checks the corresponding formal associative-polynomial identity using only
\[
[f_2,e_3]=0,\quad[f_2,v]=-h_2,\quad
[h_2,e_3]=-e_3,\quad[h_2,v]=2v.
\]

The repeated-node-two relation implies \(F_3y=0\); also \(F_1y=0\). Since
\[
F_3^3T^3v=36v\ne0,
\]
the actual identity proves \(y\ne0\). Its grade is \((a,b,n)=(0,2,3)\).

There is a nontrivial control for an **actually active** other-arm consumer:
\[
W_2y=[F_3,F_2]y=-3T^2v,\qquad u_2=-Tv,
\]
hence
\[
[u_2,W_2y]=3y.
\]
Here \(A^0y=0\), and \(W_3,\ldots,W_7\) have negative horizontal final coordinates. Consequently the full f306 contraction satisfies
\[
\overline A_3y=3y.
\]
Omitting \(u_2W_2\) gives a nonzero residual \(3y\). This tests one actual vector, not the entire grade-three matrix.

Finally,
\[
x=E_3^5E_1^5y
\]
is a nonzero vector in the sole top component. The checker tests this in the finite quotient as well.

## 3. Checker contract and controls

The complete source below:

- constructs the kernel basis independently, without importing author code;
- checks the differential representation, simple Serres, cyclic generation, and Cartan-derived grading;
- constructs all \(276\) wedge basis elements;
- closes both relation modules and checks their lowering invariance;
- compares their complete graded characters with independent Gelfand–Tsetlin characters;
- constructs all \(150\) quotient basis classes and all four simple actions;
- checks quotient Chevalley relations and graded routing;
- checks the complete top component and \(10I\);
- checks exact ranks in grades six and seven;
- checks the actual formal \(F_2y\) rewrite and the active \(W_2\) consumer.

Intended-reason controls are:

1. Omit the whole \(q_1\) module: reject for `missing_relation_q1`; mutant quotient dimension \(186\).
2. Omit the whole \(q_3\) module: reject for `missing_relation_q3`; mutant quotient dimension \(240\).
3. Remove the \(q_1\) starting-grade shift: reject for `relation_q1_grade_character`.
4. Remove the \(q_3\) starting-grade shift: reject for `relation_q3_grade_character`.
5. Reverse the dual commutator to \([F_1,F_3]\): reject for `reversed_dual_top_scalar`.
6. Omit the actually active \(ZD\) top consumer: reject for `omitted_Z_top_scalar`.
7. Omit the actually active \(u_2W_2\) consumer on \(y\): reject for `omitted_active_W2_consumer_y`.

A control counts only when the designated check raises the designated named error with a nonzero mathematical residual or character difference. An unrelated exception is not accepted as a successful control.

**Not tested:** corruption of the mixed \(W_3,W_4\) inverse Gram coefficients. Those consumers vanish on both the chosen top component and \(y\). Claiming sensitivity there would be incorrect. Their actual normalization remains the f306 import.

## 4. Execution, argv, and limitations

**NOT RUN.** The available Bash duty is expressly read-only and restricted to review commands; it does not permit executing this scientific Python program. I did not bypass that restriction through another tool.

Accordingly:

- Actual scientific argv invoked: **none**.
- Actual scientific stdout/stderr: **none**.
- Actual exit status, elapsed time, peak RSS, and source SHA256: **unobserved**.
- The dimensions and scalars above are written derivations and specified checker oracles, not fabricated execution results.

The program accepts no external input, reads/writes no files, uses no network, creates no children, and imports only standard-library modules. Its cooperative deadline is 54 seconds, leaving margin within the prescribed 55-second assay allowance. This is a cooperative deadline, not an OS-enforced runtime or memory guarantee.

Exact proposed argv, as ordered argument values:

- Argument 0: `python3`
- Argument 1: `-I`
- Argument 2: `-B`
- Argument 3: `-c`
- Argument 4: **SOURCE**, defined as the source below after removing exactly the leading four characters `SRC|` from every source line, preserving the remaining characters and indentation, joining with LF, and retaining one final LF.

The `SRC|` prefix is only lossless transport; it is not part of the Python source.

### Complete independently authored source

SRC|import sys
SRC|import time
SRC|START = time.monotonic()
SRC|LIMIT = 54.0
SRC|from fractions import Fraction as Q
SRC|from collections import Counter, deque
SRC|
SRC|
SRC|class Failure(Exception):
SRC|    def __init__(self, reason, detail=""):
SRC|        self.reason = reason
SRC|        self.detail = detail
SRC|        super().__init__(reason + ": " + detail)
SRC|
SRC|
SRC|class Deadline(Exception):
SRC|    pass
SRC|
SRC|
SRC|def guard():
SRC|    if time.monotonic() - START >= LIMIT:
SRC|        raise Deadline()
SRC|
SRC|
SRC|def require(ok, reason, detail=""):
SRC|    guard()
SRC|    if not ok:
SRC|        raise Failure(reason, detail)
SRC|
SRC|
SRC|def bump(out, key, value):
SRC|    if value:
SRC|        new = out.get(key, 0) + value
SRC|        if new:
SRC|            out[key] = new
SRC|        else:
SRC|            out.pop(key, None)
SRC|
SRC|
SRC|def accumulate(out, factor, vector):
SRC|    guard()
SRC|    if factor:
SRC|        for key, value in vector.items():
SRC|            bump(out, key, factor * value)
SRC|
SRC|
SRC|def linear(*terms):
SRC|    out = {}
SRC|    for factor, vector in terms:
SRC|        accumulate(out, factor, vector)
SRC|    return out
SRC|
SRC|
SRC|def scale(vector, factor):
SRC|    return linear((factor, vector))
SRC|
SRC|
SRC|def unit(i):
SRC|    return {i: Q(1)}
SRC|
SRC|
SRC|def sparse_text(vector):
SRC|    return repr([(key, str(vector[key])) for key in sorted(vector)])
SRC|
SRC|
SRC|def apply(matrix, vector):
SRC|    out = {}
SRC|    for index, coefficient in vector.items():
SRC|        accumulate(out, coefficient, matrix[index])
SRC|    return out
SRC|
SRC|
SRC|def compose(left, right):
SRC|    return [apply(left, column) for column in right]
SRC|
SRC|
SRC|def matadd(left, right, factor=1):
SRC|    require(len(left) == len(right), "matrix_size")
SRC|    return [
SRC|        linear((1, a), (factor, b))
SRC|        for a, b in zip(left, right)
SRC|    ]
SRC|
SRC|
SRC|def comm(left, right):
SRC|    return matadd(compose(left, right), compose(right, left), -1)
SRC|
SRC|
SRC|def matrix_zero(matrix):
SRC|    return all(not column for column in matrix)
SRC|
SRC|
SRC|def power(matrix, exponent, vector):
SRC|    result = vector
SRC|    for _ in range(exponent):
SRC|        result = apply(matrix, result)
SRC|    return result
SRC|
SRC|
SRC|class Span:
SRC|    def __init__(self):
SRC|        self.rows = {}
SRC|
SRC|    def reduce(self, vector):
SRC|        guard()
SRC|        result = dict(vector)
SRC|        for pivot in sorted(self.rows):
SRC|            coefficient = result.get(pivot, 0)
SRC|            if coefficient:
SRC|                accumulate(result, -coefficient, self.rows[pivot])
SRC|        return result
SRC|
SRC|    def insert(self, vector):
SRC|        result = self.reduce(vector)
SRC|        if not result:
SRC|            return None
SRC|        pivot = min(result)
SRC|        result = scale(result, Q(1) / result[pivot])
SRC|        self.rows[pivot] = result
SRC|        return result
SRC|
SRC|    def __len__(self):
SRC|        return len(self.rows)
SRC|
SRC|
SRC|def closure(seed, operators):
SRC|    result = Span()
SRC|    first = result.insert(seed)
SRC|    require(first is not None, "closure_zero_seed")
SRC|    queue = deque([first])
SRC|    while queue:
SRC|        guard()
SRC|        vector = queue.popleft()
SRC|        for operator in operators:
SRC|            new = result.insert(apply(operator, vector))
SRC|            if new is not None:
SRC|                queue.append(new)
SRC|    return result
SRC|
SRC|
SRC|def invariant(space, operators, reason):
SRC|    for name, operator in operators.items():
SRC|        for vector in space.rows.values():
SRC|            residual = space.reduce(apply(operator, vector))
SRC|            require(not residual, reason, name + " " + sparse_text(residual))
SRC|
SRC|
SRC|def triples(total):
SRC|    return [
SRC|        (a, b, total - a - b)
SRC|        for a in range(total + 1)
SRC|        for b in range(total - a + 1)
SRC|    ]
SRC|
SRC|
SRC|def plus_index(p, index):
SRC|    out = list(p)
SRC|    out[index] += 1
SRC|    return tuple(out)
SRC|
SRC|
SRC|def grade_from_weight(h1, h3, b):
SRC|    aa = 2 * h1 + h3 + 5 * b
SRC|    nn = h1 + 2 * h3 + 7 * b
SRC|    require(aa % 3 == 0 and nn % 3 == 0, "nonintegral_grade")
SRC|    return aa // 3, nn // 3
SRC|
SRC|
SRC|def homogeneous(vector, grades):
SRC|    require(bool(vector), "zero_homogeneous_vector")
SRC|    values = {grades[index] for index in vector}
SRC|    require(len(values) == 1, "inhomogeneous_vector", repr(values))
SRC|    return next(iter(values))
SRC|
SRC|
SRC|def character(vectors, grades):
SRC|    result = Counter()
SRC|    for vector in vectors:
SRC|        result[homogeneous(vector, grades)] += 1
SRC|    return dict(result)
SRC|
SRC|
SRC|def gt_character(p, q, shift=(0, 0)):
SRC|    result = Counter()
SRC|    for m1 in range(p, p + q + 1):
SRC|        for m2 in range(p + 1):
SRC|            for k in range(m2, m1 + 1):
SRC|                guard()
SRC|                w1 = k
SRC|                w2 = m1 + m2 - k
SRC|                w3 = 2 * p + q - m1 - m2
SRC|                h1, h3 = w1 - w2, w2 - w3
SRC|                aa = 2 * h1 + h3 + 2 * p + q
SRC|                nn = h1 + 2 * h3 + p + 2 * q
SRC|                require(aa % 3 == 0 and nn % 3 == 0, "GT_integrality")
SRC|                result[(aa // 3 + shift[0], nn // 3 + shift[1])] += 1
SRC|    return dict(result)
SRC|
SRC|
SRC|def exterior_character(char):
SRC|    grades = []
SRC|    for grade, multiplicity in sorted(char.items()):
SRC|        grades.extend([grade] * multiplicity)
SRC|    result = Counter()
SRC|    for i, first in enumerate(grades):
SRC|        for second in grades[i + 1:]:
SRC|            result[(first[0] + second[0], first[1] + second[1])] += 1
SRC|    return dict(result)
SRC|
SRC|
SRC|def check_char(actual, expected, reason):
SRC|    difference = {}
SRC|    for key in set(actual) | set(expected):
SRC|        value = actual.get(key, 0) - expected.get(key, 0)
SRC|        if value:
SRC|            difference[key] = value
SRC|    require(not difference, reason, repr(sorted(difference.items())))
SRC|
SRC|
SRC|def check_laws(ops, tag):
SRC|    e1, f1 = ops["E1"], ops["F1"]
SRC|    e3, f3 = ops["E3"], ops["F3"]
SRC|    h1, h3 = ops["H1"], ops["H3"]
SRC|    require(comm(e1, f1) == h1, tag + "_E1F1")
SRC|    require(comm(e3, f3) == h3, tag + "_E3F3")
SRC|    require(matrix_zero(comm(e1, f3)), tag + "_E1F3")
SRC|    require(matrix_zero(comm(e3, f1)), tag + "_E3F1")
SRC|    require(matrix_zero(comm(h1, h3)), tag + "_Cartan")
SRC|    for h, weights in ((h1, (2, -1)), (h3, (-1, 2))):
SRC|        for e, f, weight in ((e1, f1, weights[0]), (e3, f3, weights[1])):
SRC|            require(
SRC|                comm(h, e) == [scale(c, weight) for c in e],
SRC|                tag + "_HE"
SRC|            )
SRC|            require(
SRC|                comm(h, f) == [scale(c, -weight) for c in f],
SRC|                tag + "_HF"
SRC|            )
SRC|    for first, second in ((e1, e3), (e3, e1), (f1, f3), (f3, f1)):
SRC|        require(
SRC|            matrix_zero(comm(first, comm(first, second))),
SRC|            tag + "_simple_Serre"
SRC|        )
SRC|
SRC|
SRC|def build_kernel():
SRC|    monomials = [(p, j) for p in triples(3) for j in range(3)]
SRC|    index = {monomial: i for i, monomial in enumerate(monomials)}
SRC|    require(len(monomials) == 30, "ambient_dimension")
SRC|
SRC|    def delta(vector):
SRC|        out = {}
SRC|        for k, coefficient in vector.items():
SRC|            p, j = monomials[k]
SRC|            if p[j]:
SRC|                beta = list(p)
SRC|                beta[j] -= 1
SRC|                bump(out, tuple(beta), coefficient * p[j])
SRC|        return out
SRC|
SRC|    basis = []
SRC|    descriptors = []
SRC|    for k, (p, j) in enumerate(monomials):
SRC|        if p[j] == 0:
SRC|            basis.append({k: Q(1)})
SRC|            descriptors.append((k, 1))
SRC|    for beta in triples(2):
SRC|        pivot = index[(plus_index(beta, 0), 0)]
SRC|        for j in (1, 2):
SRC|            free = index[(plus_index(beta, j), j)]
SRC|            basis.append({
SRC|                free: Q(beta[0] + 1),
SRC|                pivot: Q(-(beta[j] + 1))
SRC|            })
SRC|            descriptors.append((free, beta[0] + 1))
SRC|    require(len(basis) == 24, "kernel_basis_dimension")
SRC|    require(len({k for k, _ in descriptors}) == 24, "kernel_free_coordinates")
SRC|    for vector in basis:
SRC|        require(not delta(vector), "kernel_basis_contraction")
SRC|
SRC|    def coordinates(vector):
SRC|        require(not delta(vector), "operator_preserves_contraction_kernel")
SRC|        result = {}
SRC|        reconstructed = {}
SRC|        for k, (ambient_free, divisor) in enumerate(descriptors):
SRC|            coefficient = Q(vector.get(ambient_free, 0)) / divisor
SRC|            if coefficient:
SRC|                result[k] = coefficient
SRC|                accumulate(reconstructed, coefficient, basis[k])
SRC|        require(
SRC|            reconstructed == vector,
SRC|            "kernel_coordinate_reconstruction",
SRC|            sparse_text(linear((1, vector), (-1, reconstructed)))
SRC|        )
SRC|        return result
SRC|
SRC|    def ambient_action(vector, i, j):
SRC|        out = {}
SRC|        for k, coefficient in vector.items():
SRC|            p, dual = monomials[k]
SRC|            if p[j]:
SRC|                moved = list(p)
SRC|                moved[j] -= 1
SRC|                moved[i] += 1
SRC|                bump(out, index[(tuple(moved), dual)], coefficient * p[j])
SRC|            if dual == i:
SRC|                bump(out, index[(p, j)], -coefficient)
SRC|        return out
SRC|
SRC|    def monomial_weight(monomial):
SRC|        p, dual = monomial
SRC|        d = [p[i] - int(i == dual) for i in range(3)]
SRC|        return d[0] - d[1], d[1] - d[2]
SRC|
SRC|    weights = []
SRC|    for vector in basis:
SRC|        ws = {monomial_weight(monomials[k]) for k in vector}
SRC|        require(len(ws) == 1, "kernel_weight_basis")
SRC|        weights.append(next(iter(ws)))
SRC|    grades = [grade_from_weight(h1, h3, 1) for h1, h3 in weights]
SRC|    require(all(a >= 0 and n >= 0 for a, n in grades), "kernel_positive_grades")
SRC|    ops = {}
SRC|    for name, i, j in (
SRC|        ("E1", 0, 1), ("F1", 1, 0),
SRC|        ("E3", 1, 2), ("F3", 2, 1)
SRC|    ):
SRC|        ops[name] = [coordinates(ambient_action(c, i, j)) for c in basis]
SRC|    for name, component in (("H1", 0), ("H3", 1)):
SRC|        ops[name] = [
SRC|            {i: Q(weight[component])} if weight[component] else {}
SRC|            for i, weight in enumerate(weights)
SRC|        ]
SRC|    v = coordinates({index[((0, 0, 3), 0)]: Q(1)})
SRC|    return ops, grades, weights, v
SRC|
SRC|
SRC|def build_wedge(mops, mgrades, mweights):
SRC|    pairs = [(i, j) for i in range(24) for j in range(i + 1, 24)]
SRC|    pair_index = {pair: k for k, pair in enumerate(pairs)}
SRC|
SRC|    def wedge(left, right):
SRC|        out = {}
SRC|        for i, a in left.items():
SRC|            for j, b in right.items():
SRC|                if i < j:
SRC|                    bump(out, pair_index[(i, j)], a * b)
SRC|                elif i > j:
SRC|                    bump(out, pair_index[(j, i)], -a * b)
SRC|        return out
SRC|
SRC|    grades = [
SRC|        (mgrades[i][0] + mgrades[j][0], mgrades[i][1] + mgrades[j][1])
SRC|        for i, j in pairs
SRC|    ]
SRC|    weights = [
SRC|        (mweights[i][0] + mweights[j][0], mweights[i][1] + mweights[j][1])
SRC|        for i, j in pairs
SRC|    ]
SRC|    for grade, weight in zip(grades, weights):
SRC|        require(grade == grade_from_weight(*weight, 2), "wedge_Cartan_grade")
SRC|    ops = {}
SRC|    for name, matrix in mops.items():
SRC|        ops[name] = [
SRC|            linear(
SRC|                (1, wedge(matrix[i], unit(j))),
SRC|                (1, wedge(unit(i), matrix[j]))
SRC|            )
SRC|            for i, j in pairs
SRC|        ]
SRC|    return ops, grades, wedge
SRC|
SRC|
SRC|def poly_multiply(left, right):
SRC|    out = {}
SRC|    for first, a in left.items():
SRC|        for second, b in right.items():
SRC|            bump(out, first + second, a * b)
SRC|    return out
SRC|
SRC|
SRC|def poly_bracket(left, right):
SRC|    return linear(
SRC|        (1, poly_multiply(left, right)),
SRC|        (-1, poly_multiply(right, left))
SRC|    )
SRC|
SRC|
SRC|def poly_ad(t, exponent, vector):
SRC|    for _ in range(exponent):
SRC|        vector = poly_bracket(t, vector)
SRC|    return vector
SRC|
SRC|
SRC|def actual_F2_normal_order(poly):
SRC|    out = {}
SRC|    cartan_weight = {"t": -1, "v": 2}
SRC|    for word, coefficient in poly.items():
SRC|        require(
SRC|            all(letter in cartan_weight for letter in word),
SRC|            "rewrite_positive_word"
SRC|        )
SRC|        for i, letter in enumerate(word):
SRC|            if letter == "v":
SRC|                prefix, suffix = word[:i], word[i + 1:]
SRC|                positive_word = prefix + suffix
SRC|                bump(out, positive_word + ("h",), -coefficient)
SRC|                weight = sum(cartan_weight[x] for x in suffix)
SRC|                bump(out, positive_word, -coefficient * weight)
SRC|    return out
SRC|
SRC|
SRC|CONTROLS = []
SRC|
SRC|
SRC|def expect_control(name, reason, action):
SRC|    try:
SRC|        action()
SRC|    except Failure as error:
SRC|        require(
SRC|            error.reason == reason,
SRC|            "control_wrong_reason",
SRC|            name + ": " + error.reason
SRC|        )
SRC|        CONTROLS.append((name, reason, error.detail))
SRC|        return
SRC|    raise Failure("control_not_rejected", name)
SRC|
SRC|
SRC|def scalar_check(matrix, indices, scalar, reason):
SRC|    for i in indices:
SRC|        residual = linear((1, matrix[i]), (-scalar, unit(i)))
SRC|        require(not residual, reason, sparse_text(residual))
SRC|
SRC|
SRC|def main():
SRC|    mops, mgrades, mweights, v = build_kernel()
SRC|    check_laws(mops, "M")
SRC|    require(not apply(mops["F1"], v), "v_F1_lowest")
SRC|    require(not apply(mops["F3"], v), "v_F3_lowest")
SRC|    require(apply(mops["H1"], v) == scale(v, -1), "v_H1")
SRC|    require(apply(mops["H3"], v) == scale(v, -3), "v_H3")
SRC|    require(not power(mops["E1"], 2, v), "v_E1_Serre")
SRC|    require(not power(mops["E3"], 4, v), "v_E3_Serre")
SRC|    cyclic = closure(v, [mops["E1"], mops["E3"]])
SRC|    require(len(cyclic) == 24, "M_cyclic_dimension")
SRC|    mchar = dict(Counter(mgrades))
SRC|    check_char(mchar, gt_character(1, 3), "M_grade_character")
SRC|    require(max(n for a, n in mgrades) == 4, "M_maximum_grade")
SRC|
SRC|    wops, wgrades, wedge = build_wedge(mops, mgrades, mweights)
SRC|    require(len(wgrades) == 276, "wedge_dimension")
SRC|    q1 = wedge(v, apply(mops["E1"], v))
SRC|    q3 = wedge(v, apply(mops["E3"], v))
SRC|    for q, expected_grade, h1, h3, name in (
SRC|        (q1, (1, 0), 0, -7, "q1"),
SRC|        (q3, (0, 1), -3, -4, "q3")
SRC|    ):
SRC|        require(bool(q), name + "_nonzero")
SRC|        require(homogeneous(q, wgrades) == expected_grade, name + "_start_grade")
SRC|        require(not apply(wops["F1"], q), name + "_F1_lowest")
SRC|        require(not apply(wops["F3"], q), name + "_F3_lowest")
SRC|        require(apply(wops["H1"], q) == scale(q, h1), name + "_H1")
SRC|        require(apply(wops["H3"], q) == scale(q, h3), name + "_H3")
SRC|
SRC|    r1 = closure(q1, [wops["E1"], wops["E3"]])
SRC|    r3 = closure(q3, [wops["E1"], wops["E3"]])
SRC|    require(len(r1) == 36, "q1_whole_module_dimension")
SRC|    require(len(r3) == 90, "q3_whole_module_dimension")
SRC|    invariant(r1, wops, "q1_full_g_invariance")
SRC|    invariant(r3, wops, "q3_full_g_invariance")
SRC|    r1char = character(r1.rows.values(), wgrades)
SRC|    r3char = character(r3.rows.values(), wgrades)
SRC|    check_char(r1char, gt_character(0, 7, (1, 0)), "relation_q1_grade_character")
SRC|    check_char(r3char, gt_character(3, 4, (0, 1)), "relation_q3_grade_character")
SRC|
SRC|    relations = Span()
SRC|    for space in (r1, r3):
SRC|        for row in space.rows.values():
SRC|            relations.insert(row)
SRC|    require(len(relations) == 126, "relation_sum_dimension")
SRC|    require(len(r1) + len(r3) - len(relations) == 0, "relation_intersection")
SRC|
SRC|    def relation_check(space):
SRC|        for q, reason in ((q1, "missing_relation_q1"), (q3, "missing_relation_q3")):
SRC|            residual = space.reduce(q)
SRC|            require(not residual, reason, sparse_text(residual))
SRC|        invariant(space, wops, "whole_relation_invariance")
SRC|        require(len(space) == 126, "whole_relation_dimension")
SRC|
SRC|    relation_check(relations)
SRC|    require(276 - len(r3) == 186, "omit_q1_control_dimension")
SRC|    require(276 - len(r1) == 240, "omit_q3_control_dimension")
SRC|    expect_control("omit_whole_q1_module", "missing_relation_q1", lambda: relation_check(r3))
SRC|    expect_control("omit_whole_q3_module", "missing_relation_q3", lambda: relation_check(r1))
SRC|    expect_control(
SRC|        "wrong_q1_start_grade",
SRC|        "relation_q1_grade_character",
SRC|        lambda: check_char(
SRC|            r1char, gt_character(0, 7, (0, 0)), "relation_q1_grade_character"
SRC|        )
SRC|    )
SRC|    expect_control(
SRC|        "wrong_q3_start_grade",
SRC|        "relation_q3_grade_character",
SRC|        lambda: check_char(
SRC|            r3char, gt_character(3, 4, (0, 0)), "relation_q3_grade_character"
SRC|        )
SRC|    )
SRC|
SRC|    free = [i for i in range(276) if i not in relations.rows]
SRC|    free_index = {ambient: i for i, ambient in enumerate(free)}
SRC|    require(len(free) == 150, "quotient_dimension")
SRC|
SRC|    def quotient(vector):
SRC|        reduced = relations.reduce(vector)
SRC|        require(all(i in free_index for i in reduced), "quotient_pivot_remains")
SRC|        return {free_index[i]: coefficient for i, coefficient in reduced.items()}
SRC|
SRC|    ngrades = [wgrades[i] for i in free]
SRC|    nops = {
SRC|        name: [quotient(apply(matrix, unit(i))) for i in free]
SRC|        for name, matrix in wops.items()
SRC|    }
SRC|    nchar = dict(Counter(ngrades))
SRC|    expected = Counter(exterior_character(gt_character(1, 3)))
SRC|    expected.subtract(gt_character(0, 7, (1, 0)))
SRC|    expected.subtract(gt_character(3, 4, (0, 1)))
SRC|    require(all(value >= 0 for value in expected.values()), "negative_expected_character")
SRC|    expected = {key: value for key, value in expected.items() if value}
SRC|    check_char(nchar, expected, "quotient_full_grade_character")
SRC|    require(sum(nchar.values()) == 150, "quotient_character_dimension")
SRC|    check_laws(nops, "N")
SRC|
SRC|    shifts = {"E1": (1, 0), "F1": (-1, 0), "E3": (0, 1), "F3": (0, -1)}
SRC|    for name, (da, dn) in shifts.items():
SRC|        for i, column in enumerate(nops[name]):
SRC|            a, n = ngrades[i]
SRC|            require(
SRC|                all(ngrades[j] == (a + da, n + dn) for j in column),
SRC|                "quotient_action_grade_routing",
SRC|                name
SRC|            )
SRC|    for i, (a, n) in enumerate(ngrades):
SRC|        h1, h3 = 2 * a - 2 - n, -a - 6 + 2 * n
SRC|        require(nops["H1"][i] == scale(unit(i), h1), "N_actual_H1")
SRC|        require(nops["H3"][i] == scale(unit(i), h3), "N_actual_H3")
SRC|
SRC|    z = comm(nops["E1"], nops["E3"])
SRC|    d = comm(nops["F3"], nops["F1"])
SRC|    tf = compose(nops["E3"], nops["F3"])
SRC|    zd = compose(z, d)
SRC|    a0 = matadd(tf, zd)
SRC|    require(comm(z, d) == matadd(nops["H1"], nops["H3"]), "ZD_Cartan_commutator")
SRC|    top = [i for i, grade in enumerate(ngrades) if grade[1] == 8]
SRC|    require(len(top) == 1, "top_grade_dimension")
SRC|    require(ngrades[top[0]] == (5, 8), "top_horizontal_placement")
SRC|    require(max(n for a, n in ngrades) == 8, "N_maximum_grade")
SRC|    scalar_check(a0, top, 10, "top_scalar_10")
SRC|    scalar_check(tf, top, 5, "active_TF3_top_scalar")
SRC|    scalar_check(zd, top, 5, "active_ZD_top_scalar")
SRC|    expect_control(
SRC|        "reversed_theta_dual_commutator",
SRC|        "reversed_dual_top_scalar",
SRC|        lambda: scalar_check(matadd(tf, zd, -1), top, 10, "reversed_dual_top_scalar")
SRC|    )
SRC|    expect_control(
SRC|        "omit_active_ZD_consumer",
SRC|        "omitted_Z_top_scalar",
SRC|        lambda: scalar_check(tf, top, 10, "omitted_Z_top_scalar")
SRC|    )
SRC|
SRC|    def degree_add(first, second):
SRC|        return tuple(a + b for a, b in zip(first, second))
SRC|
SRC|    f_degree, g_degree, r_degree = (0, 0, 1), (1, 0, 0), (0, 1, 0)
SRC|    wd = [f_degree]
SRC|    wd.append(degree_add(wd[0], g_degree))
SRC|    wd.append(degree_add(wd[0], r_degree))
SRC|    wd.append(degree_add(wd[2], g_degree))
SRC|    wd.append(degree_add(wd[1], r_degree))
SRC|    wd.append(degree_add(wd[3], g_degree))
SRC|    wd.append(degree_add(wd[4], r_degree))
SRC|    wd.append(degree_add(wd[6], g_degree))
SRC|    roots13 = {(1, 0), (0, 1), (1, 1)}
SRC|
SRC|    def other_arm_target_exists(a, n, j):
SRC|        da, db, dn = wd[j]
SRC|        aa, bb, nn = a - da, 2 - db, n - dn
SRC|        require(n >= 2 and nn >= 1, "consumer_target_domain")
SRC|        if aa < 0:
SRC|            return False
SRC|        if bb == 1:
SRC|            return bool(mchar.get((aa, nn), 0))
SRC|        if bb == 0:
SRC|            return (aa, nn) in roots13
SRC|        raise Failure("unhandled_consumer_target_b", repr((j, aa, bb, nn)))
SRC|
SRC|    high_ranks = []
SRC|    for n in (6, 7, 8):
SRC|        indices = [i for i, grade in enumerate(ngrades) if grade[1] == n]
SRC|        require(bool(indices), "high_grade_nonempty", str(n))
SRC|        image = Span()
SRC|        for i in indices:
SRC|            a, _ = ngrades[i]
SRC|            for j in range(2, 8):
SRC|                require(
SRC|                    not other_arm_target_exists(a, n, j),
SRC|                    "discarded_consumer_has_actual_target",
SRC|                    repr((a, n, j))
SRC|                )
SRC|            require(
SRC|                all(ngrades[k][1] == n for k in a0[i]),
SRC|                "A0_grade_routing"
SRC|            )
SRC|            image.insert(a0[i])
SRC|        require(len(image) == len(indices), "high_grade_exact_rank", str(n))
SRC|        high_ranks.append((n, len(indices), len(image)))
SRC|
SRC|    tword, vword = {("t",): 1}, {("v",): 1}
SRC|    tvword = poly_ad(tword, 1, vword)
SRC|    t2vword = poly_ad(tword, 2, vword)
SRC|    t3vword = poly_ad(tword, 3, vword)
SRC|    yword = poly_bracket(tvword, t2vword)
SRC|    require(actual_F2_normal_order(vword) == {("h",): -1}, "actual_F2_v")
SRC|    require(actual_F2_normal_order(tvword) == {("t",): -1}, "actual_F2_Tv")
SRC|    require(not actual_F2_normal_order(t2vword), "actual_F2_T2v")
SRC|    require(
SRC|        actual_F2_normal_order(yword) == scale(t3vword, -1),
SRC|        "actual_formal_F2_y"
SRC|    )
SRC|    require(
SRC|        not actual_F2_normal_order(poly_bracket(vword, tvword)),
SRC|        "actual_F2_repeated_node2_relation"
SRC|    )
SRC|
SRC|    tv = apply(mops["E3"], v)
SRC|    t2v = apply(mops["E3"], tv)
SRC|    t3v = apply(mops["E3"], t2v)
SRC|    require(bool(t3v), "T3v_nonzero")
SRC|    require(power(mops["F3"], 3, t3v) == scale(v, 36), "actual_string_36")
SRC|    y = quotient(wedge(tv, t2v))
SRC|    require(bool(y), "actual_y_quotient_nonzero")
SRC|    require(homogeneous(y, ngrades) == (0, 3), "actual_y_grade")
SRC|    require(not apply(nops["F1"], y), "actual_y_F1_lowest")
SRC|    require(not apply(nops["F3"], y), "actual_y_F3_lowest")
SRC|    require(not apply(a0, y), "actual_y_A0_zero")
SRC|    for j in range(3, 8):
SRC|        require(not other_arm_target_exists(0, 3, j), "actual_y_other_target_zero")
SRC|    w2y = scale(apply(mops["F3"], t3v), -1)
SRC|    require(w2y == scale(t2v, -3), "actual_W2_y")
SRC|    w2_consumer = quotient(wedge(scale(tv, -1), w2y))
SRC|    residual = linear((1, w2_consumer), (-3, y))
SRC|    require(not residual, "actual_full_y_scalar_3", sparse_text(residual))
SRC|
SRC|    def omitted_w2_check():
SRC|        residual = linear((1, apply(a0, y)), (-3, y))
SRC|        require(
SRC|            not residual,
SRC|            "omitted_active_W2_consumer_y",
SRC|            sparse_text(residual)
SRC|        )
SRC|
SRC|    expect_control(
SRC|        "omit_active_other_arm_W2_consumer",
SRC|        "omitted_active_W2_consumer_y",
SRC|        omitted_w2_check
SRC|    )
SRC|    x = power(nops["E3"], 5, power(nops["E1"], 5, y))
SRC|    require(bool(x), "explicit_top_vector_nonzero")
SRC|    require(homogeneous(x, ngrades) == (5, 8), "explicit_top_vector_grade")
SRC|    require(set(x).issubset(set(top)), "explicit_top_vector_full_component")
SRC|    require(len(CONTROLS) == 7, "control_count")
SRC|    guard()
SRC|
SRC|    print("RESULT: PASS_FIXED_FINITE_MODEL")
SRC|    print("SCOPE: r=1 s=3; conditional actual-source bridge; no global conclusion")
SRC|    print("DIMENSIONS: M=24 wedge=276 R1=36 R3=90 intersection=0 N=150")
SRC|    print("TOP: a=5 b=2 n=8 dimension=1 full_normalized_contraction=10I")
SRC|    print("ACTUAL_REWRITE: F2[y]=-T^3v; F3^3T^3v=36v")
SRC|    print("ACTIVE_OTHER_ARM: ad(u2)W2[y]=3y; A0[y]=0")
SRC|    print("HIGH_GRADE_RANKS:", repr(high_ranks))
SRC|    for name, reason, detail in CONTROLS:
SRC|        print("CONTROL_REJECT:", name, reason, detail)
SRC|    print("MIXED_GRAM_MUTATION: NOT_TESTED_IN_THIS_SCOPE")
SRC|    print("N_CHARACTER:", repr(sorted(nchar.items())))
SRC|    print("ELAPSED_MONOTONIC_SECONDS:", format(time.monotonic() - START, ".6f"))
SRC|
SRC|
SRC|if __name__ == "__main__":
SRC|    try:
SRC|        main()
SRC|    except Deadline:
SRC|        print("RESULT: INCOMPLETE_COOPERATIVE_DEADLINE", file=sys.stderr)
SRC|        sys.exit(3)
SRC|    except KeyboardInterrupt:
SRC|        print("RESULT: INCOMPLETE_INTERRUPTED", file=sys.stderr)
SRC|        sys.exit(3)
SRC|    except Failure as error:
SRC|        print("RESULT: FAIL", error.reason, error.detail, file=sys.stderr)
SRC|        sys.exit(2)

## 5. Remaining gates and exact nonclaims

The finite program has been supplied completely but has not earned an execution receipt. Its prospective `PASS_FIXED_FINITE_MODEL` string above is source text, **not observed stdout**.

The retained imports are:

- **f276:** actual free-source/whole-Serre-ideal bridge, full-Cartan injection, and exclusion of extra positive consequences from the negative ideal.
- **Adopted first arm:** identification of the actual \(b=1\) module and its separately scoped radical statement.
- **f306:** actual theta-duals, normalization, complete inverse Gram, descended coevaluation, and consuming bracket.
- **f314:** retained only if a parent separately derives projected-seed consequences using the whole two-seed ideal and full generalized-primary interface; this return does not independently verify that interface.

Unpaid work is explicitly limited to:

- a parent-authorized execution and inspection of this newly authored checker;
- independent review of the checker itself;
- any full low-grade matrix with active mixed-Gram consumers;
- reconstruction of the imported manuscripts;
- any assertion beyond this fixed case, including all \(r,s\), general \(b=2\) radical equality, global generalized-primary control, whole-level-eight closure, \(B_8=0\), or global \(J=\tau\);
- original-source authentication, novelty/current-status review, independent-model-family or human review, and formal/kernel acceptance.

No paid/heavy/remote computation, model CLI, installation, file mutation, or external action was performed or requested as an automatic next step. No candidate is self-adopted, and no global target is closed.

**overall_correctness:** correct

**explanation:** No substantive defect was identified in the assigned fixed-case written mathematics at its retained import boundaries. The independent executable checker is complete but NOT RUN, so this return supplies written reconstruction and an unexecuted verification artifact—not an executed finite PASS or a disposition of the broader author candidate.

**confidence:** 0.89