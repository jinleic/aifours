# F518 FINITE — complete return

**Disposition: FINITE_NOT_RUN.** No finite PASS, mathematical rejection, or candidate acceptance is issued. The independent source below is complete but **unexecuted**.

## 1. Read chronology and evidence attribution

I completed the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all listed permission/status controls **before sending the direct pre-body ACK to Main**. I then read `literal-packet-v1.md` in ordered, raw chunks of at most 20 LF, covering **LF1–692**, including the endings of **S1 LF1–653** and **S2 LF1–37**.

Only after completing that packet did I construct the independent checker.

The following pins and clock are **parent-observed metadata**, not child-executed measurements:

- Manifest SHA256: `0abaa7bca9c046a43e802cb9d0a38cdd47b75cc9b6c64aa1b9f802bee932a7fa`
- Freeze-receipt SHA256: `055b8a4d9eb87d85163410206ce4160350b85bb6d071ed6e97f9b3f8b1e232f7`
- Literal-packet SHA256: `55da9c80d42fe4dc1dd86d2605ca9b2d0d014ff84bbe4c46ab891a9ee513551f`
- Parent observation: `2026-10-30T12:32:45-0700 PDT`

I did not inspect S1 LF654–916, the optional author checker, scientific sibling outputs, held scientific payloads or their consumers, or new mathematical sources. All listed quarantines remain NONINPUT. No external-model CLI, installation, deletion, credential operation, Git mutation, repository edit, build, test, lint, formatter, or scientific execution was performed.

There is no child-native execution start time, source hash, stdout, exit status, or elapsed-time measurement.

## 2. Independent model construction

The checker constructs the adjoint module from rational \(3\times3\) matrix commutators:

\[
e_1=E_{12},\quad e_2=E_{23},\quad f_1=E_{21},\quad f_2=E_{32},\quad u_0=E_{31}.
\]

The prescribed normalized recursive letters then give

\[
\begin{aligned}
u_1&=-E_{32},&u_2&=E_{21},\\
u_3&=\operatorname{diag}(1,-1,0),&
u_4&=\operatorname{diag}(0,-1,1),\\
u_5&=E_{12},&u_6&=E_{23},&u_7&=E_{13}.
\end{aligned}
\]

The trace-transpose pairing independently constructs the Gram matrix and its inverse, rather than installing the candidate’s inverse-Gram coefficients as the construction rule.

The checker then:

- Builds the complete 28-dimensional exterior source and all four Levi derivations.
- Generates the complete cyclic closures of \(q_r,q_s,y\), checking dimensions \(10,10,8\), direct exhaustion, and stability under all four Levi generators.
- Constructs actual \(F_3\) recursively from \(F_3u_0=-h_3\), commutation with \(E_1,E_2\), the displayed Cartan row, and
  \[
  h_3u_i=(2-ra_i-sb_i)u_i.
  \]
- Builds every rectangular dual word \(W_0,\ldots,W_7\), the complete coevaluation, and the consuming wedge map.
- For \(r=1\), removes the **whole** cyclic relation module and checks its annihilation by \(F_3\), every \(W_i\), and coevaluation.
- Checks full and quotient equivariance, full contraction kernel, quotient ranks, complete \(b=2\) component dimensions, and exact determinants.

The legitimate parameter cases are exactly

\[
(1,2),\ (1,3),\ (2,3),\ (3,4).
\]

Wrong-parameter tables used for mutations are not additional legitimate research cases.

For the boundary, \(s=3,4\), the checker independently solves the grade-\(k\) \(F_3\)-lowest kernel in \(\Lambda^2V_s\), compares it with the authored recurrence, removes the entire \(v\wedge Tv\) closure, and constructs complete surviving node-3 strings. Actual \(F_2\) is derived from its Chevalley recursion, not from the coefficient being tested.

## 3. Actual results and execution limitation

The active runtime instruction restricts bash to read-only diff/log/show/PR-diff commands. Consequently, I did not execute scientific code or seek an alternate execution route.

| Check | Actual status |
|---|---|
| Adjoint Chevalley relations and derived Gram inverse | NOT_RUN |
| Complete \(10+10+8\) exterior decomposition | NOT_RUN |
| Four prescribed parameter cases | NOT_RUN |
| Actual \(F_3q_r,F_3q_s,F_3y\) | NOT_RUN |
| Full relation closure and quotient descent | NOT_RUN |
| All-four-generator full/quotient equivariance | NOT_RUN |
| Kernel, coevaluation, and consuming-bracket checks | NOT_RUN |
| Complete same-grade \(b=2\) dimensions/determinants | NOT_RUN |
| Boundary \(s=3,4\), actual \(F_2\), complete strings | NOT_RUN |
| Every mutation | NOT_RUN |
| Stdout / exit status / elapsed time | NOT_AVAILABLE |

No expected numerical value is reported as an observed result.

The intended mutations cover separate omissions of \(W_5,W_6,W_7\) on raised surviving vectors, wrong inverse-Gram signs, wrong lowering transpose, transposed/swapped parameters, seed-only relation removal, and forced-zero boundary \(F_2\). Each needs a separating witness; absent witnesses produce `NOT_TESTED`, not invented detection.

The radical-from-invertibility control is deliberately limited: it checks that a nonzero \(A\)-stable surviving summand can coexist with invertible \(A\), and that its \(F_3\)-image invokes the separate lower-grade ideal premise. It does **not** construct or compute the actual \(\tau/J\).

## 4. Scope and unpaid interfaces

The finite quotient construction remains conditional on the frozen actual-source interfaces. It does not independently establish:

- Exclusion of additional positive consequences of the complete negative Serre ideal.
- Full-Cartan injection or Cartan-disjointness of \(\tau/J\).
- The adopted \((\tau/J)\cap M=0\) theorem.

Those require their separate written/parent dispositions. Even a successful run would corroborate only the four prescribed level-two cases and boundary \(s=3,4\), not universal Theorems A/B, global \(J=\tau\), B8, whole level eight, novelty, or human/family/formal-kernel acceptance.

**Findings:** No evidence-backed mathematical defect established.  
**Finite verdict:** NOT_RUN; no candidate correctness verdict issued.  
**Parent retains final disposition.**

The return artifacts are:

- `local://f518-finite-result-v1.md`
- `local://f518-independent-finite-v1.py`

## 5. Complete independent source

Proposed argv consists of `python3`, `-I`, `-S`, `-B`, `-c`, followed by the complete source as one argument. The source uses only `fractions` and `time`, performs no filesystem/network/subprocess operations, and enforces a cooperative 54-second deadline.

The literal source follows without a code block. Strip the initial `SRC|` from every source line, preserve the remaining whitespace, and join with LF plus a final LF.

SRC|from fractions import Fraction as Q
SRC|from time import monotonic
SRC|
SRC|START = monotonic()
SRC|LIMIT = 54.0
SRC|ZERO, ONE = Q(0), Q(1)
SRC|GAPS = []
SRC|
SRC|
SRC|def tick():
SRC|    if monotonic() - START > LIMIT:
SRC|        print('TIMEOUT: no overall verification result', flush=True)
SRC|        raise SystemExit(3)
SRC|
SRC|
SRC|def require(condition, label):
SRC|    tick()
SRC|    if not condition:
SRC|        print('FAIL: ' + label, flush=True)
SRC|        raise SystemExit(1)
SRC|
SRC|
SRC|def zeros(m, n):
SRC|    return [[ZERO] * n for _ in range(m)]
SRC|
SRC|
SRC|def eye(n):
SRC|    out = zeros(n, n)
SRC|    for i in range(n):
SRC|        out[i][i] = ONE
SRC|    return out
SRC|
SRC|
SRC|def unit(n, i):
SRC|    return tuple(ONE if j == i else ZERO for j in range(n))
SRC|
SRC|
SRC|def column(a, j):
SRC|    return tuple(row[j] for row in a)
SRC|
SRC|
SRC|def columns(vectors, n):
SRC|    if not vectors:
SRC|        return zeros(n, 0)
SRC|    require(all(len(v) == n for v in vectors), 'column dimensions')
SRC|    return [list(row) for row in zip(*vectors)]
SRC|
SRC|
SRC|def transpose(a):
SRC|    return [list(row) for row in zip(*a)]
SRC|
SRC|
SRC|def select(a, rows, cols):
SRC|    return [[a[i][j] for j in cols] for i in rows]
SRC|
SRC|
SRC|def vlin(*terms):
SRC|    n = len(terms[0][1])
SRC|    out = [ZERO] * n
SRC|    for c, v in terms:
SRC|        for i, x in enumerate(v):
SRC|            if c and x:
SRC|                out[i] += c * x
SRC|    return tuple(out)
SRC|
SRC|
SRC|def mlin(*terms):
SRC|    first = terms[0][1]
SRC|    out = zeros(len(first), len(first[0]))
SRC|    for c, a in terms:
SRC|        for i, row in enumerate(a):
SRC|            for j, x in enumerate(row):
SRC|                if c and x:
SRC|                    out[i][j] += c * x
SRC|    return out
SRC|
SRC|
SRC|def mv(a, v):
SRC|    tick()
SRC|    return tuple(sum((x * y for x, y in zip(row, v) if x and y), ZERO)
SRC|                 for row in a)
SRC|
SRC|
SRC|def mm(a, b):
SRC|    tick()
SRC|    require(len(a[0]) == len(b), 'matrix product dimensions')
SRC|    out = zeros(len(a), len(b[0]))
SRC|    for i, row in enumerate(a):
SRC|        tick()
SRC|        for k, x in enumerate(row):
SRC|            if x:
SRC|                for j, y in enumerate(b[k]):
SRC|                    if y:
SRC|                        out[i][j] += x * y
SRC|    return out
SRC|
SRC|
SRC|def bracket(a, b):
SRC|    return mlin((ONE, mm(a, b)), (-ONE, mm(b, a)))
SRC|
SRC|
SRC|def rref(a, n=None):
SRC|    tick()
SRC|    n = len(a[0]) if a else (0 if n is None else n)
SRC|    out = [list(row) for row in a]
SRC|    pivots = []
SRC|    row = 0
SRC|    for col in range(n):
SRC|        tick()
SRC|        pivot = next((i for i in range(row, len(out)) if out[i][col]), None)
SRC|        if pivot is None:
SRC|            continue
SRC|        out[row], out[pivot] = out[pivot], out[row]
SRC|        scale = out[row][col]
SRC|        out[row] = [x / scale for x in out[row]]
SRC|        for i in range(len(out)):
SRC|            if i != row and out[i][col]:
SRC|                scale = out[i][col]
SRC|                out[i] = [x - scale * y for x, y in zip(out[i], out[row])]
SRC|        pivots.append(col)
SRC|        row += 1
SRC|        if row == len(out):
SRC|            break
SRC|    return out, pivots
SRC|
SRC|
SRC|def rank(a, n=None):
SRC|    return len(rref(a, n)[1])
SRC|
SRC|
SRC|def inverse(a):
SRC|    n = len(a)
SRC|    augmented = [row[:] + eye(n)[i] for i, row in enumerate(a)]
SRC|    reduced, pivots = rref(augmented)
SRC|    require(pivots == list(range(n)), 'inverse has full left rank')
SRC|    return [row[n:] for row in reduced]
SRC|
SRC|
SRC|def nullspace(a, n):
SRC|    reduced, pivots = rref(a, n)
SRC|    free = [j for j in range(n) if j not in pivots]
SRC|    answer = []
SRC|    for j in free:
SRC|        v = [ZERO] * n
SRC|        v[j] = ONE
SRC|        for i, p in enumerate(pivots):
SRC|            v[p] = -reduced[i][j]
SRC|        answer.append(tuple(v))
SRC|    return answer
SRC|
SRC|
SRC|def determinant(a):
SRC|    if not a:
SRC|        return ONE
SRC|    out = [row[:] for row in a]
SRC|    result = ONE
SRC|    for col in range(len(out)):
SRC|        tick()
SRC|        pivot = next((i for i in range(col, len(out)) if out[i][col]), None)
SRC|        if pivot is None:
SRC|            return ZERO
SRC|        if pivot != col:
SRC|            out[col], out[pivot] = out[pivot], out[col]
SRC|            result = -result
SRC|        scale = out[col][col]
SRC|        result *= scale
SRC|        for i in range(col + 1, len(out)):
SRC|            if out[i][col]:
SRC|                factor = out[i][col] / scale
SRC|                for j in range(col + 1, len(out)):
SRC|                    out[i][j] -= factor * out[col][j]
SRC|                out[i][col] = ZERO
SRC|    return result
SRC|
SRC|
SRC|class Span:
SRC|    def __init__(self, n):
SRC|        self.n = n
SRC|        self.pivots = {}
SRC|        self.vectors = []
SRC|        self.tags = []
SRC|
SRC|    def residual(self, v):
SRC|        tick()
SRC|        out = list(v)
SRC|        for p in sorted(self.pivots):
SRC|            c = out[p]
SRC|            if c:
SRC|                out = [x - c * y for x, y in zip(out, self.pivots[p])]
SRC|        return tuple(out)
SRC|
SRC|    def contains(self, v):
SRC|        return not any(self.residual(v))
SRC|
SRC|    def add(self, v, tag=''):
SRC|        out = self.residual(v)
SRC|        p = next((i for i, x in enumerate(out) if x), None)
SRC|        if p is None:
SRC|            return False
SRC|        self.pivots[p] = tuple(x / out[p] for x in out)
SRC|        self.vectors.append(tuple(v))
SRC|        self.tags.append(tag)
SRC|        return True
SRC|
SRC|
SRC|def span_of(vectors, n):
SRC|    answer = Span(n)
SRC|    for v in vectors:
SRC|        answer.add(v)
SRC|    return answer
SRC|
SRC|
SRC|def cyclic(seed, operators):
SRC|    space = Span(len(seed))
SRC|    space.add(seed, 'seed')
SRC|    index = 0
SRC|    while index < len(space.vectors):
SRC|        tick()
SRC|        v, tag = space.vectors[index], space.tags[index]
SRC|        for name, a in operators:
SRC|            space.add(mv(a, v), name + '(' + tag + ')')
SRC|        index += 1
SRC|    return space
SRC|
SRC|
SRC|def require_stable(space, operators, label):
SRC|    for name, a in operators:
SRC|        for v in space.vectors:
SRC|            require(space.contains(mv(a, v)), label + ' stable under ' + name)
SRC|
SRC|
SRC|def exterior_pairs(n):
SRC|    return [(i, j) for i in range(n) for j in range(i + 1, n)]
SRC|
SRC|
SRC|def wedge(v, w, pairs):
SRC|    return tuple(v[i] * w[j] - v[j] * w[i] for i, j in pairs)
SRC|
SRC|
SRC|def exterior_action(a, pairs):
SRC|    n = len(a)
SRC|    standard = [unit(n, i) for i in range(n)]
SRC|    return columns([
SRC|        vlin((ONE, wedge(column(a, i), standard[j], pairs)),
SRC|             (ONE, wedge(standard[i], column(a, j), pairs)))
SRC|        for i, j in pairs
SRC|    ], len(pairs))
SRC|
SRC|
SRC|def homogeneous(v, degrees):
SRC|    support = {degrees[i] for i, x in enumerate(v) if x}
SRC|    require(len(support) == 1, 'nonzero homogeneous cyclic basis vector')
SRC|    return next(iter(support))
SRC|
SRC|
SRC|def mutant(label, witness):
SRC|    tick()
SRC|    if witness is None:
SRC|        GAPS.append(label)
SRC|        print('NOT_TESTED: ' + label + ': no separating witness', flush=True)
SRC|    else:
SRC|        print('DETECTED: ' + label + ': ' + witness, flush=True)
SRC|
SRC|
SRC|def cell(i, j):
SRC|    out = zeros(3, 3)
SRC|    out[i][j] = ONE
SRC|    return out
SRC|
SRC|
SRC|# The eight source letters are constructed, not imported as action tables.
SRC|e1, e2, f1, f2 = cell(0, 1), cell(1, 2), cell(1, 0), cell(2, 1)
SRC|u0 = cell(2, 0)
SRC|u1, u2 = bracket(e1, u0), bracket(e2, u0)
SRC|u3, u4 = bracket(e1, u2), bracket(e2, u1)
SRC|u5 = mlin((-Q(1, 2), bracket(e1, u3)))
SRC|u6 = mlin((Q(1, 2), bracket(e2, u4)))
SRC|u7 = bracket(e1, u6)
SRC|U = [u0, u1, u2, u3, u4, u5, u6, u7]
SRC|DEGREES = [(0, 0), (1, 0), (0, 1), (1, 1), (1, 1),
SRC|           (2, 1), (1, 2), (2, 2)]
SRC|FLAT = [tuple(x for row in a for x in row) for a in U]
SRC|P = columns(FLAT, 9)
SRC|row_space, selected_rows = Span(8), []
SRC|for i, row in enumerate(P):
SRC|    if row_space.add(row):
SRC|        selected_rows.append(i)
SRC|require(len(selected_rows) == 8, 'adjoint letters have dimension eight')
SRC|P_INV = inverse(select(P, selected_rows, list(range(8))))
SRC|
SRC|
SRC|def coordinates(a):
SRC|    flat = tuple(x for row in a for x in row)
SRC|    out = mv(P_INV, tuple(flat[i] for i in selected_rows))
SRC|    require(mv(P, out) == flat, 'matrix lies in adjoint span')
SRC|    return out
SRC|
SRC|
SRC|def adjoint(a):
SRC|    return columns([coordinates(bracket(a, u)) for u in U], 8)
SRC|
SRC|
SRC|EV = [adjoint(e1), adjoint(e2)]
SRC|FV = [adjoint(f1), adjoint(f2)]
SRC|HV = [bracket(EV[i], FV[i]) for i in range(2)]
SRC|A12 = [[2, -1], [-1, 2]]
SRC|for i in range(2):
SRC|    for j in range(2):
SRC|        require(bracket(HV[i], EV[j]) == mlin((A12[i][j], EV[j])),
SRC|                'adjoint Cartan/raising relation')
SRC|        require(bracket(HV[i], FV[j]) == mlin((-A12[i][j], FV[j])),
SRC|                'adjoint Cartan/lowering relation')
SRC|        if i != j:
SRC|            require(not any(map(any, bracket(EV[i], FV[j]))),
SRC|                    'adjoint mixed Chevalley relation')
SRC|            require(not any(map(any, bracket(EV[i], bracket(EV[i], EV[j])))),
SRC|                    'adjoint positive A2 Serre')
SRC|            require(not any(map(any, bracket(FV[i], bracket(FV[i], FV[j])))),
SRC|                    'adjoint negative A2 Serre')
SRC|GRAM = [[sum((x * y for x, y in zip(a, b)), ZERO) for b in FLAT]
SRC|        for a in FLAT]
SRC|GRAM_INV = inverse(GRAM)
SRC|expected_gram = eye(8)
SRC|expected_gram[3][3] = expected_gram[4][4] = Q(2)
SRC|expected_gram[3][4] = expected_gram[4][3] = ONE
SRC|require(GRAM == expected_gram, 'derived trace-transpose Gram block')
SRC|require(GRAM_INV[3][3] == Q(2, 3) and GRAM_INV[3][4] == -Q(1, 3),
SRC|        'derived inverse Gram thirds')
SRC|for i in range(2):
SRC|    require(mm(transpose(EV[i]), GRAM) == mm(GRAM, FV[i]),
SRC|            'derived contravariant form')
SRC|PAIRS = exterior_pairs(8)
SRC|PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
SRC|D28 = len(PAIRS)
SRC|require(D28 == 28, 'exterior source dimension')
SRC|EH = [exterior_action(a, PAIRS) for a in EV]
SRC|FH = [exterior_action(a, PAIRS) for a in FV]
SRC|OPS = [('E1', EH[0]), ('E2', EH[1]), ('F1', FH[0]), ('F2', FH[1])]
SRC|PAIR_DEGREES = [(DEGREES[i][0] + DEGREES[j][0],
SRC|                 DEGREES[i][1] + DEGREES[j][1]) for i, j in PAIRS]
SRC|qr = unit(D28, PAIR_INDEX[(0, 1)])
SRC|qs = unit(D28, PAIR_INDEX[(0, 2)])
SRC|y = vlin((ONE, unit(D28, PAIR_INDEX[(0, 3)])),
SRC|         (-ONE, unit(D28, PAIR_INDEX[(0, 4)])),
SRC|         (-ONE, unit(D28, PAIR_INDEX[(1, 2)])))
SRC|for seed in [qr, qs, y]:
SRC|    for a in FH:
SRC|        require(not any(mv(a, seed)), 'three seeds are Levi-lowest')
SRC|CYCLIC = [cyclic(seed, OPS[:2]) for seed in [qr, qs, y]]
SRC|require([len(s.vectors) for s in CYCLIC] == [10, 10, 8],
SRC|        'independently generated complete cyclic dimensions')
SRC|for i, space in enumerate(CYCLIC):
SRC|    require_stable(space, OPS, 'complete summand ' + str(i))
SRC|BASIS_VECTORS = [v for space in CYCLIC for v in space.vectors]
SRC|B = columns(BASIS_VECTORS, D28)
SRC|B_INV = inverse(B)
SRC|B_DEGREES = [homogeneous(v, PAIR_DEGREES) for v in BASIS_VECTORS]
SRC|B_TAGS = [tag for space in CYCLIC for tag in space.tags]
SRC|EMIT = [columns([wedge(unit(8, i), unit(8, j), PAIRS)
SRC|                 for j in range(8)], D28) for i in range(8)]
SRC|MU = [[x for a in EMIT for x in a[i]] for i in range(D28)]
SRC|
SRC|
SRC|def f3_matrix(r, s):
SRC|    h3 = zeros(8, 8)
SRC|    for i, (a, b) in enumerate(DEGREES):
SRC|        h3[i][i] = Q(2 - r * a - s * b)
SRC|    require(bracket(h3, EV[0]) == mlin((-r, EV[0])), 'h3 row/r parameter')
SRC|    require(bracket(h3, EV[1]) == mlin((-s, EV[1])), 'h3 row/s parameter')
SRC|
SRC|    def raise_extended(value, e, p):
SRC|        x, t = value
SRC|        return mlin((ONE, bracket(e, x)), (t * p, e)), ZERO
SRC|
SRC|    def scale_extended(c, value):
SRC|        x, t = value
SRC|        return mlin((c, x)), c * t
SRC|
SRC|    # F3u0=-h3; [F3,E1]=[F3,E2]=0.  On Levi12,
SRC|    # [e1,h3]=r e1 and [e2,h3]=s e2.
SRC|    b0 = (zeros(3, 3), -ONE)
SRC|    b1 = raise_extended(b0, e1, r)
SRC|    b2 = raise_extended(b0, e2, s)
SRC|    b3 = raise_extended(b2, e1, r)
SRC|    b4 = raise_extended(b1, e2, s)
SRC|    b5 = scale_extended(-Q(1, 2), raise_extended(b3, e1, r))
SRC|    b6 = scale_extended(Q(1, 2), raise_extended(b4, e2, s))
SRC|    b7 = raise_extended(b6, e1, r)
SRC|    values = [b0, b1, b2, b3, b4, b5, b6, b7]
SRC|    actions = [mlin((ONE, adjoint(x)), (t, h3)) for x, t in values]
SRC|    return columns([vlin((ONE, column(actions[i], j)),
SRC|                         (-ONE, column(actions[j], i))) for i, j in PAIRS], 8)
SRC|
SRC|
SRC|def dual_words(d, gv, rv, gh, rh):
SRC|    def comm(w, av, ah):
SRC|        return mlin((ONE, mm(w, ah)), (-ONE, mm(av, w)))
SRC|    w0 = d
SRC|    w1, w2 = comm(w0, gv, gh), comm(w0, rv, rh)
SRC|    w3, w4 = comm(w2, gv, gh), comm(w1, rv, rh)
SRC|    w5 = mlin((-Q(1, 2), comm(w3, gv, gh)))
SRC|    w6 = mlin((Q(1, 2), comm(w4, rv, rh)))
SRC|    w7 = comm(w6, gv, gh)
SRC|    return [w0, w1, w2, w3, w4, w5, w6, w7]
SRC|
SRC|
SRC|def contraction(words, gram_inverse):
SRC|    blocks = [mlin(*[(gram_inverse[i][j], words[j]) for j in range(8)
SRC|                     if gram_inverse[i][j]]) for i in range(8)]
SRC|    c = [row[:] for block in blocks for row in block]
SRC|    a = mlin(*[(ONE, mm(EMIT[i], blocks[i])) for i in range(8)])
SRC|    require(a == mm(MU, c), 'all eight coevaluation blocks reach consuming bracket')
SRC|    return a, c
SRC|
SRC|
SRC|def spectral_witness(a, active, lambdas, raised_only=False):
SRC|    for j in active:
SRC|        if raised_only and B_TAGS[j] == 'seed':
SRC|            continue
SRC|        residual = mv(B_INV, vlin((ONE, mv(a, BASIS_VECTORS[j])),
SRC|                                 (-lambdas[j], BASIS_VECTORS[j])))
SRC|        visible = [(i, str(residual[i])) for i in active if residual[i]]
SRC|        if visible:
SRC|            return ('basis=' + str(j) + ', degree=' + str(B_DEGREES[j]) +
SRC|                    ', word=' + B_TAGS[j] + ', quotient residual=' + str(visible))
SRC|    return None
SRC|
SRC|
SRC|for r, s in [(1, 2), (1, 3), (2, 3), (3, 4)]:
SRC|    label = 'r=' + str(r) + ',s=' + str(s)
SRC|    d = f3_matrix(r, s)
SRC|    for i in range(2):
SRC|        require(mm(d, EH[i]) == mm(EV[i], d), 'F3 commutes with E' + str(i + 1))
SRC|    for j, degree in enumerate(PAIR_DEGREES):
SRC|        require(all(not d[i][j] or DEGREES[i] == degree for i in range(8)),
SRC|                'F3 retains both horizontal degrees')
SRC|    require(mv(d, qr) == vlin((2 * (r - 1), unit(8, 1))), 'actual F3 qr')
SRC|    require(mv(d, qs) == vlin((2 * (s - 1), unit(8, 2))), 'actual F3 qs')
SRC|    require(mv(d, y) == vlin((3 * r + 2 * s - 2, unit(8, 3)),
SRC|                            (-(2 * r + 3 * s - 2), unit(8, 4))), 'actual F3 y')
SRC|    words = dual_words(d, FV[0], FV[1], FH[0], FH[1])
SRC|    a, c = contraction(words, GRAM_INV)
SRC|    for name, op in OPS:
SRC|        require(mm(a, op) == mm(op, a), 'all-four full Levi equivariance ' + name)
SRC|    lr, ls, l0 = Q(4 * (r - 1)), Q(4 * (s - 1)), Q(5 * (r + s) - 4)
SRC|    lambdas = [lr] * 10 + [ls] * 10 + [l0] * 8
SRC|    expected = zeros(D28, D28)
SRC|    for j, value in enumerate(lambdas):
SRC|        expected[j][j] = value
SRC|    in_basis = mm(B_INV, mm(a, B))
SRC|    require(in_basis == expected, 'full independently constructed spectrum ' + label)
SRC|    active = list(range(10 if r == 1 else 0, D28))
SRC|    relation = CYCLIC[0] if r == 1 else Span(D28)
SRC|    for v in relation.vectors:
SRC|        require(not any(mv(d, v)), 'whole relation killed by F3')
SRC|        for w in words:
SRC|            require(not any(mv(w, v)), 'whole relation killed by each dual channel')
SRC|        require(not any(mv(c, v)), 'coevaluation descends through entire relation')
SRC|    kernel = nullspace(a, D28)
SRC|    require(len(kernel) == len(relation.vectors), 'full contraction kernel dimension')
SRC|    require(all(relation.contains(v) for v in kernel), 'kernel equals entire relation')
SRC|    aq = select(in_basis, active, active)
SRC|    require(rank(aq) == len(active), 'actual quotient invertibility')
SRC|    require(all(lambdas[j] > 0 for j in active), 'all surviving scalars positive')
SRC|    cq = mm(c, columns([BASIS_VECTORS[j] for j in active], D28))
SRC|    require(rank(cq) == len(active), 'actual coevaluation has zero kernel')
SRC|    require(rank(mm(MU, cq)) == rank(cq), 'image C meets kernel mu trivially')
SRC|    for name, op in OPS:
SRC|        oq_full = mm(B_INV, mm(op, B))
SRC|        if r == 1:
SRC|            require(not any(oq_full[i][j] for i in active for j in range(10)),
SRC|                    'complete relation ideal stability ' + name)
SRC|        oq = select(oq_full, active, active)
SRC|        require(mm(aq, oq) == mm(oq, aq), 'quotient equivariance ' + name)
SRC|    slice_determinant = ONE
SRC|    slice_dimension = 0
SRC|    maximum_a = max(degree[0] for degree in PAIR_DEGREES)
SRC|    for horizontal in range(maximum_a + 1):
SRC|        indices = [j for j in active if B_DEGREES[j] == (horizontal, 2)]
SRC|        block = select(in_basis, indices, indices)
SRC|        actual_dimension = len(indices)
SRC|        actual_determinant = determinant(block)
SRC|        if horizontal in (1, 2, 3):
SRC|            middle = horizontal == 2
SRC|            predicted_dimension = (2 if r == 1 else 3) + int(middle)
SRC|            predicted_determinant = l0 ** (2 if middle else 1) * ls
SRC|            if r != 1:
SRC|                predicted_determinant *= lr
SRC|        else:
SRC|            predicted_dimension, predicted_determinant = 0, ONE
SRC|        require(actual_dimension == predicted_dimension, 'complete b2 component dimension')
SRC|        require(actual_determinant == predicted_determinant, 'complete b2 determinant')
SRC|        slice_dimension += actual_dimension
SRC|        slice_determinant *= actual_determinant
SRC|        print('COMPONENT ' + label + ',a=' + str(horizontal) + ',b=2,n=2: dim=' +
SRC|              str(actual_dimension) + ',det=' + str(actual_determinant), flush=True)
SRC|    predicted_total = l0 ** 4 * ls ** 3 * (lr ** 3 if r != 1 else ONE)
SRC|    require(slice_determinant == predicted_total, 'whole b2 determinant')
SRC|    require(slice_dimension == (7 if r == 1 else 10), 'whole b2 dimension')
SRC|    print('BASELINE ' + label + ': whole level2 dim=' + str(len(active)) +
SRC|          ',full-kernel-dim=' + str(len(kernel)), flush=True)
SRC|    for omitted in (5, 6, 7):
SRC|        broken = words[:]
SRC|        broken[omitted] = zeros(8, D28)
SRC|        bad, unused = contraction(broken, GRAM_INV)
SRC|        mutant(label + ' omit W' + str(omitted) + ' on raised actual vectors',
SRC|               spectral_witness(bad, active, lambdas, True))
SRC|    broken_gram = [row[:] for row in GRAM_INV]
SRC|    broken_gram[3][4] = broken_gram[4][3] = Q(1, 3)
SRC|    bad, unused = contraction(words, broken_gram)
SRC|    mutant(label + ' wrong mixed inverse-Gram signs', spectral_witness(bad, active, lambdas))
SRC|    transposed_words = dual_words(d, transpose(FV[0]), transpose(FV[1]),
SRC|                                 transpose(FH[0]), transpose(FH[1]))
SRC|    bad, unused = contraction(transposed_words, GRAM_INV)
SRC|    mutant(label + ' wrong lowering transpose', spectral_witness(bad, active, lambdas))
SRC|    for name, mr, ms in [('transposed Cartan row', 1, 1), ('swapped r,s', s, r)]:
SRC|        wrong_d = f3_matrix(mr, ms)
SRC|        delta = vlin((ONE, mv(wrong_d, qs)), (-ONE, mv(d, qs)))
SRC|        if not any(delta):
SRC|            delta = vlin((ONE, mv(wrong_d, qr)), (-ONE, mv(d, qr)))
SRC|        mutant(label + ' ' + name,
SRC|               ('actual F3 seed difference=' + str(delta)) if any(delta) else None)
SRC|    if r == 1:
SRC|        seed_only = span_of([qr], D28)
SRC|        outside = mv(EH[1], qr)
SRC|        mutant(label + ' remove only relation seed',
SRC|               ('E2(qr) outside rank-one relation; full rank=' +
SRC|                str(len(relation.vectors))) if not seed_only.contains(outside) else None)
SRC|    # This is a logical scope guard, not a model of the actual radical.
SRC|    ys = CYCLIC[2]
SRC|    antecedent = determinant(aq) != 0 and len(ys.vectors) > 0
SRC|    antecedent = antecedent and all(ys.contains(mv(a, v)) for v in ys.vectors)
SRC|    mutant(label + ' infer radical vanishing from invertibility alone',
SRC|           ('nonzero eight-dimensional A-stable y-summand coexists with invertible A; '
SRC|            'its F3(y) is nonzero, so ideal exclusion needs the separate lower-grade premise')
SRC|           if antecedent and any(mv(d, y)) else None)
SRC|
SRC|
SRC|for s in (3, 4):
SRC|    n = s + 1
SRC|    pairs = exterior_pairs(n)
SRC|    index = {pair: i for i, pair in enumerate(pairs)}
SRC|    size = len(pairs)
SRC|    t, lower = zeros(n, n), zeros(n, n)
SRC|    for i in range(n):
SRC|        if i < s:
SRC|            t[i + 1][i] = ONE
SRC|        if i:
SRC|            lower[i - 1][i] = Q(i * (s - i + 1))
SRC|    h = zeros(n, n)
SRC|    for i in range(n):
SRC|        h[i][i] = Q(2 * i - s)
SRC|    require(bracket(t, lower) == h, 'boundary node3 string Chevalley action')
SRC|    th, lh = exterior_action(t, pairs), exterior_action(lower, pairs)
SRC|    relation = cyclic(unit(size, index[(0, 1)]), [('T', th)])
SRC|    require(len(relation.vectors) == 2 * s - 1, 'whole boundary relation dimension')
SRC|    require_stable(relation, [('T', th), ('F3', lh)], 'boundary relation')
SRC|    # Derive F2(T^i v) recursively: F2v=-h2,
SRC|    # [e3,h2]=e3 and [e3,e3]=0.  Pairs hold h2/e3 coefficients.
SRC|    values = [(-ONE, ZERO)]
SRC|    for i in range(s):
SRC|        values.append((ZERO, values[-1][0]))
SRC|
SRC|    def action(value, j):
SRC|        a0, b0 = value
SRC|        out = vlin((a0 * (2 - j), unit(n, j)))
SRC|        if j < s:
SRC|            out = vlin((ONE, out), (b0, unit(n, j + 1)))
SRC|        return out
SRC|
SRC|    f2_boundary = columns([
SRC|        vlin((ONE, action(values[i], j)), (-ONE, action(values[j], i)))
SRC|        for i, j in pairs
SRC|    ], n)
SRC|    require(mm(f2_boundary, th) == mm(t, f2_boundary), 'boundary F2 commutes with E3')
SRC|    require(all(not any(mv(f2_boundary, v)) for v in relation.vectors),
SRC|            'boundary F2 annihilates complete relation closure')
SRC|    strings = []
SRC|    f2_mutation_witness = None
SRC|    for k in range(3, s + 1, 2):
SRC|        support = [j for j, (a0, b0) in enumerate(pairs) if a0 + b0 == k]
SRC|        targets = [j for j, (a0, b0) in enumerate(pairs) if a0 + b0 == k - 1]
SRC|        kernels = nullspace(select(lh, targets, support), len(support))
SRC|        require(len(kernels) == 1, 'unique boundary lowest line from independent kernel')
SRC|        coefficients = kernels[0]
SRC|        leading = support.index(index[(0, k)])
SRC|        require(coefficients[leading] != 0, 'boundary lowest vector leading normalization')
SRC|        coefficients = tuple(x / coefficients[leading] for x in coefficients)
SRC|        lowest = [ZERO] * size
SRC|        for i, j in enumerate(support):
SRC|            lowest[j] = coefficients[i]
SRC|        lowest = tuple(lowest)
SRC|        require(not any(mv(lh, lowest)), 'boundary yk is F3-lowest')
SRC|        require(not relation.contains(lowest), 'boundary lowest survives actual quotient')
SRC|        coefficient = ONE
SRC|        for i in range((k - 1) // 2 + 1):
SRC|            require(lowest[index[(i, k - i)]] == coefficient, 'author yk recurrence matches kernel')
SRC|            if i < (k - 1) // 2:
SRC|                coefficient *= -Q((k - i) * (s - k + i + 1), (i + 1) * (s - i))
SRC|        actual = mv(f2_boundary, lowest)
SRC|        expected_coefficient = Q((k - 1) * (2 * s - k), s)
SRC|        require(actual == vlin((expected_coefficient, unit(n, k))), 'actual nonzero F2 yk')
SRC|        require(any(actual), 'actual F2 yk does not vanish')
SRC|        f2_mutation_witness = 's=' + str(s) + ',k=' + str(k) + ',F2yk=' + str(actual)
SRC|        z = unit(n, k)
SRC|        for i in range(k):
SRC|            z = mv(lower, z)
SRC|        factor = ONE
SRC|        for i in range(1, k + 1):
SRC|            factor *= i * (s - i + 1)
SRC|        require(z == vlin((factor, unit(n, 0))), 'nonzero finite node3 return to v')
SRC|        string = cyclic(lowest, [('T', th)])
SRC|        length = 2 * s - 2 * k + 1
SRC|        require(len(string.vectors) == length, 'complete boundary survivor string dimension')
SRC|        for j, v in enumerate(string.vectors):
SRC|            require(homogeneous(v, [a0 + b0 for a0, b0 in pairs]) == k + j,
SRC|                    'boundary survivor exact grade')
SRC|            previous = string.vectors[j - 1] if j else (ZERO,) * size
SRC|            require(mv(lh, v) == vlin((j * (length - j), previous)),
SRC|                    'complete boundary survivor lowering coefficients')
SRC|        require(not any(mv(th, string.vectors[-1])), 'complete boundary string top')
SRC|        strings.append(string)
SRC|        print('BOUNDARY s=' + str(s) + ',k=' + str(k) + ',string-dim=' + str(length) +
SRC|              ',F2-coefficient=' + str(expected_coefficient), flush=True)
SRC|    all_vectors = relation.vectors + [v for string in strings for v in string.vectors]
SRC|    require(len(all_vectors) == size and rank(columns(all_vectors, size)) == size,
SRC|            'boundary relation plus complete survivors exhaust exterior source')
SRC|    degrees = [a0 + b0 for a0, b0 in pairs]
SRC|    relation_degrees = [homogeneous(v, degrees) for v in relation.vectors]
SRC|    actual_degrees = [homogeneous(v, degrees) for string in strings for v in string.vectors]
SRC|    dimensions = []
SRC|    for grade in range(2 * s + 1):
SRC|        raw = sum(degree == grade for degree in degrees)
SRC|        removed = sum(degree == grade for degree in relation_degrees)
SRC|        actual_dim = sum(degree == grade for degree in actual_degrees)
SRC|        formula = sum(k <= grade <= 2 * s - k for k in range(3, s + 1, 2))
SRC|        require(raw - removed == actual_dim == formula, 'complete boundary component dimension')
SRC|        dimensions.append(actual_dim)
SRC|    mutant('boundary forced-zero F2 coefficient', f2_mutation_witness)
SRC|    print('BOUNDARY s=' + str(s) + ': dimensions n=0..' + str(2 * s) + ': ' +
SRC|          str(dimensions), flush=True)
SRC|
SRC|print('SCOPE: exact finite models conditional on frozen actual-source interfaces; '
SRC|      'no universal negative-Serre bridge or actual tau/J computed', flush=True)
SRC|if GAPS:
SRC|    print('BASELINES_PASS; MUTATION_GAPS: ' + '; '.join(GAPS), flush=True)
SRC|    raise SystemExit(2)
SRC|print('BASELINES_PASS; ALL_LISTED_MUTATIONS_DETECTED; elapsed=' +
SRC|      format(monotonic() - START, '.6f') + 's', flush=True)