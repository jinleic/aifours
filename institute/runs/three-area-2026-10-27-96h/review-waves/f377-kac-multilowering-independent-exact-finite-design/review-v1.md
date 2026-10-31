# f377 — independent exact finite checker

**Status: COMPLETE SOURCE, NOTRUN.** No scientific executable was run, and no file was written. The role’s tools prohibit execution and filesystem edits; this is the requested direct materialization fallback, not a failed experiment or evidence of contamination.

Actual model, supplied by runtime context: `anthropic/claude-fable-5-1`.

## Scope and dispositions

| Claim | Disposition | Evidence and limits |
|---|---|---|
| Full finite positive ideal can be constructed using all six positive Serre seeds and generator-adjoint closure | **SUPPORTED as the construction below**, conditional on the named actual-source bridge | S2 LF3, 7–10, 19. Binary tensor-Lie spans and the ideal recurrence below do not assume the claimed quotient basis or matrix. No numerical ranks are asserted before execution. |
| At \(r=s=a=b=1,n=2\), the actual contraction is the scalar \(6\) | **SUPPORTED by the finite written reconstruction below** | S1 LF585–650; actual-source and exclusion of extra positive relations from negative Serres remain conditional on S2 LF7–10. |
| The requested arbitrary-degree component \((r,s,a,b,n)=(1,3,2,1,4)\) is nonzero | **SUPPORTED by the written nonvacuity argument below** | Uses the named level-one adjoint-Levi module and Chevalley relations, not a postulated full component dimension. |
| The other selected matrices, characteristic polynomials, positivity checks, and mutation rejections | **INCONCLUSIVE / NOTRUN** | The complete checker implements them; no execution output is fabricated. |
| The supplied \((3,7,1,1,8)\) matrix and spectrum | **INCONCLUSIVE / NOTRUN** | Explicitly checked against independently constructed operators after construction; S1 LF679–730. |
| Uniform Theorems A/B, the generalized-primary consequences, or the original whole target | **Not established by this finite duty** | S1 LF118–124 and 768–774 retain their separate imports and unpaid gates. |

**Findings:** no FATAL/MAJOR/minor mathematical defect established in the candidate by this return. This is not clearance of the unexecuted checks.

## Two finite written results

### 1. The active mixed-Gram corner

For \(r=s=1\), in free positive degree \((1,1,2)\), put
\[
X_i=(\operatorname{ad}e_3)^i e_1,\quad
Y_j=(\operatorname{ad}e_3)^j e_2,\quad
Z_{i,j}=[X_i,Y_j].
\]

The free tensor-Lie component has basis \(Z_{0,2},Z_{1,1},Z_{2,0}\). For example, tensor words \(1233\) and \(2133\) distinguish the first and third vectors, and \(3123\) distinguishes the middle vector. Jacobi gives spanning. All four fixed positive Serre seeds are excluded from this degree by their horizontal coordinates. The two remaining seeds are \(X_2,Y_2\); their complete closures in this degree kill exactly \(Z_{2,0},Z_{0,2}\). Thus the actual component is one-dimensional, conditional on f276’s positive-source/full-ideal bridge.

Write \(x=Z_{1,1}\). Direct Chevalley normal ordering gives
\[
E_3F_3x=2x,\quad W_1x=-Y_1,\quad W_2x=X_1,\quad
W_3x=e_3,\quad W_4x=-e_3.
\]
The higher targets are zero. Also
\[
[u_1,W_1x]=x,\quad [u_2,W_2x]=x,\quad
[u_3,e_3]=x,\quad [u_4,e_3]=-x.
\]

The labels generated from \(E_{12},E_{23},E_{31}\) give the Frobenius Gram block
\[
G_{34}=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
Its inverse contributes \(2x\). Consequently the full operator is \(6x\); omitting the mixed block produces **\(4x\), still invertible but scientifically wrong**. The negative control therefore tests the defining contraction, not merely invertibility.

### 2. Nonvacuity of the arbitrary-degree case

For \((r,s)=(1,3)\), the actual level-one vector
\[
u_5=-\tfrac12 E_1^2E_2e_3
\]
is nonzero by the named adjoint-Levi identification. Its \(h_3\)-weight is \(-3\). Its \(F_3\)-target has Levi degree \((2,1,0)\), which is zero in \(\mathfrak{sl}_3\), so \(F_3u_5=0\).

Chevalley’s string identity then gives
\[
F_3^3E_3^3u_5=36u_5\ne0.
\]
Therefore \(E_3^3u_5\) is a nonzero vector in degree \((2,1,4)\). The checker nevertheless derives the **whole** component’s quotient and basis by binary spans; it does not use this argument to postulate its dimension or matrix.

## Checker design

For each prescribed downbox, the checker constructs:

1. Every free Lie component by **all binary bracket splits in the three-generator tensor algebra**.
2. All six seeds \((\operatorname{ad}e_i)^{1-a_{ij}}e_j\).
3. The entire positive ideal in the downbox using
   \[
   I_d=\operatorname{span}\bigl(\text{seeds in }d,\ [e_i,I_{d-\alpha_i}]\text{ for every }i\bigr).
   \]
   Closure under simple-generator adjoints is closure under all Lie adjoints by Jacobi. Both complete Levi raising modules and mixed-seed overlap are therefore included. Positive grading makes this finite downbox exact, not a height approximation to its components.
4. Quotient complements, before comparison with any claimed \(Z\)-basis.
5. Actual lowerings by normal-ordering \([f_i,e_j]=-\delta_{ij}h_i\):
   \[
   F_iP=-\sum_w c_w\sum_{k:w_k=i}
   \left(\sum_{\ell>k}a_{i,w_\ell}\right)w_{\widehat k}.
   \]
   It separately checks cancellation of the right-normal-ordered \(h_i\) coefficient.
6. Every \(W_j\) by the anti-involution’s **reversed commutator order**.
7. The Gram matrix solely from the generated \(3\times3\) Levi labels. Matrix multiplication is **never** used for tensor-Lie words.
8. The consuming operation
   \[
   \sum_{i,j}(G^{-1})_{ij}[u_i,W_jx],
   \]
   including the full mixed block.

The negative controls omit \(W_1\), omit the mixed block, reverse the \(W_1\) commutator, omit each remaining seed, and omit each relevant fixed seed in the arbitrary-degree downbox. Only rejection for the **specified scientific invariant** counts.

The program has a cooperative **50-second calculation deadline**. Deadline, error, missing relation, or incomplete computation cannot produce PASS. No signal handlers, subprocesses, network operations, package dependencies, file reads, or file writes are installed or performed by the checker body. It writes its report only to stdout.

## Materialization and invocation

Materialize the following complete body as `f377_exact_checker_v1.py`. Pin its actual bytes and the interpreter independently before running.

Argv:

`python3 -I -B -S /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f377-kac-multilowering-independent-exact-finite-design/f377_exact_checker_v1.py`

**Observed execution result in this return: NOTRUN.** Runtime, output hashes, finite ranks, and mutation outcomes remain unobserved.

BEGIN FILE f377_exact_checker_v1.py
#!/usr/bin/env python3
"""Exact finite tensor-Lie/Serre/coeval checker. Stdlib only; stdout only."""
import sys
import time
import json
from fractions import Fraction as F
from itertools import product
from math import factorial

START = time.monotonic()
DEADLINE = START + 50.0

class ScientificFailure(Exception):
    def __init__(self, code, detail=""):
        self.code = code
        self.detail = detail
        super().__init__(code + (": " + detail if detail else ""))

class Incomplete(Exception):
    pass

def guard():
    if time.monotonic() >= DEADLINE:
        raise Incomplete("cooperative 50-second calculation deadline")

def need(condition, code, detail=""):
    if not condition:
        raise ScientificFailure(code, detail)

def put(p, word, value):
    if value:
        new = p.get(word, F(0)) + value
        if new:
            p[word] = new
        else:
            p.pop(word, None)

def lin(terms):
    out = {}
    for c, p in terms:
        if c:
            for w, v in p.items():
                put(out, w, c * v)
    return out

def scale(p, c):
    return {w: c * v for w, v in p.items() if c * v}

def bracket(p, q):
    guard()
    out = {}
    for x, c in p.items():
        for y, d in q.items():
            put(out, x + y, c * d)
            put(out, y + x, -c * d)
    return out

E = [{(i,): F(1)} for i in range(3)]

def adpower(x, y, k):
    need(k >= 0, "NEGATIVE_AD_POWER")
    out = y
    for unused in range(k):
        guard()
        out = bracket(x, out)
    return out

def degree_word(w):
    return tuple(w.count(i) for i in range(3))

def degree_check(p, d):
    need(all(degree_word(w) == d for w in p),
         "HOMOGENEOUS_DEGREE", str(d))

def subdegree(d, e):
    return tuple(d[i] - e[i] for i in range(3))

def addunit(d, i):
    x = list(d)
    x[i] += 1
    return tuple(x)

def subunit(d, i):
    x = list(d)
    x[i] -= 1
    return tuple(x)

class Span:
    """Sparse echelon span with exact, fully reduced quotient normal form."""
    def __init__(self):
        self.rows = {}

    def vectors(self):
        return [self.rows[p] for p in sorted(self.rows)]

    def __len__(self):
        return len(self.rows)

    def reduce(self, p):
        work = dict(p)
        out = {}
        while work:
            guard()
            pivot = min(work)
            c = work.pop(pivot)
            row = self.rows.get(pivot)
            if row is None:
                put(out, pivot, c)
            else:
                for w, v in row.items():
                    if w != pivot:
                        put(work, w, -c * v)
        return out

    def insert(self, p):
        r = self.reduce(p)
        if not r:
            return False
        pivot = min(r)
        self.rows[pivot] = scale(r, F(1) / r[pivot])
        return True

    def coords(self, p):
        pivots = sorted(self.rows)
        where = {p: i for i, p in enumerate(pivots)}
        ans = [F(0)] * len(pivots)
        work = dict(p)
        while work:
            guard()
            pivot = min(work)
            c = work.pop(pivot)
            need(pivot in self.rows, "COORDINATE_OUTSIDE_SPAN")
            ans[where[pivot]] += c
            for w, v in self.rows[pivot].items():
                if w != pivot:
                    put(work, w, -c * v)
        return ans

def lower(p, i, A):
    """Move every -h_i to the right; retain and audit its coefficient."""
    guard()
    out = {}
    hcoefficient = {}
    for w, c in p.items():
        suffix_weight = 0
        for k in range(len(w) - 1, -1, -1):
            j = w[k]
            if j == i:
                deleted = w[:k] + w[k + 1:]
                put(out, deleted, -c * suffix_weight)
                put(hcoefficient, deleted, -c)
            suffix_weight += A[i][j]
    need(not hcoefficient, "UNEXPECTED_CARTAN_REMAINDER",
         "This finite checker only applies F to non-Cartan targets.")
    return out

def gen(i):
    return ("g", i)

def bt(x, y):
    return ("b", x, y)

def st(c, x):
    return ("s", F(c), x)

T1, T2, T3 = gen(0), gen(1), gen(2)
UT = [
    T3,
    bt(T1, T3),
    bt(T2, T3),
    bt(T1, bt(T2, T3)),
    bt(T2, bt(T1, T3)),
    st(F(-1, 2), bt(T1, bt(T1, bt(T2, T3)))),
    st(F(1, 2), bt(T2, bt(T2, bt(T1, T3)))),
]
UT.append(bt(T1, UT[6]))

def tensor_tree(t):
    if t[0] == "g":
        return E[t[1]]
    if t[0] == "s":
        return scale(tensor_tree(t[2]), t[1])
    if t[0] == "b":
        return bracket(tensor_tree(t[1]), tensor_tree(t[2]))
    raise ScientificFailure("UNKNOWN_TENSOR_TREE_NODE")

def theta_action(t, p, A):
    """theta([v,w])=[theta(w),theta(v)], as actual operator composition."""
    guard()
    if not p:
        return {}
    if t[0] == "g":
        return lower(p, t[1], A)
    if t[0] == "s":
        return scale(theta_action(t[2], p, A), t[1])
    if t[0] == "b":
        left, right = t[1], t[2]
        first = theta_action(right, theta_action(left, p, A), A)
        second = theta_action(left, theta_action(right, p, A), A)
        return lin(((F(1), first), (F(-1), second)))
    raise ScientificFailure("UNKNOWN_THETA_TREE_NODE")

U = [tensor_tree(t) for t in UT]
UD = [degree_word(next(iter(u))) for u in U]
for u, d in zip(U, UD):
    degree_check(u, d)

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def matcols(cols, nrows):
    need(all(len(c) == nrows for c in cols), "MATRIX_COLUMN_SHAPE")
    return [[cols[j][i] for j in range(len(cols))]
            for i in range(nrows)]

def mm(A, B):
    guard()
    if not A:
        return []
    need(bool(B), "MATRIX_PRODUCT_EMPTY_INNER")
    need(len(A[0]) == len(B), "MATRIX_PRODUCT_SHAPE")
    return [
        [sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
         for j in range(len(B[0]))]
        for i in range(len(A))
    ]

def madd(A, B):
    need(len(A) == len(B), "MATRIX_ADD_SHAPE")
    need(all(len(x) == len(y) for x, y in zip(A, B)),
         "MATRIX_ADD_SHAPE")
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(A, B)]

def inverse(A, code="SINGULAR_MATRIX"):
    n = len(A)
    if not n:
        return []
    need(all(len(row) == n for row in A), "INVERSE_SHAPE")
    B = [list(map(F, row)) + eye(n)[i] for i, row in enumerate(A)]
    for k in range(n):
        guard()
        pivot = next((i for i in range(k, n) if B[i][k]), None)
        need(pivot is not None, code)
        B[k], B[pivot] = B[pivot], B[k]
        c = B[k][k]
        B[k] = [v / c for v in B[k]]
        for i in range(n):
            if i != k and B[i][k]:
                c = B[i][k]
                B[i] = [x - c * y for x, y in zip(B[i], B[k])]
    return [row[n:] for row in B]

def determinant(A):
    n = len(A)
    if not n:
        return F(1)
    need(all(len(row) == n for row in A), "DETERMINANT_SHAPE")
    B = [list(map(F, row)) for row in A]
    out = F(1)
    for k in range(n):
        guard()
        pivot = next((i for i in range(k, n) if B[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            B[k], B[pivot] = B[pivot], B[k]
            out = -out
        c = B[k][k]
        out *= c
        for i in range(k + 1, n):
            factor = B[i][k] / c
            if factor:
                for j in range(k + 1, n):
                    B[i][j] -= factor * B[k][j]
            B[i][k] = F(0)
    return out

def rank(A):
    if not A:
        return 0
    B = [list(map(F, row)) for row in A]
    nrows, ncols = len(B), len(B[0])
    out = 0
    for j in range(ncols):
        guard()
        pivot = next((i for i in range(out, nrows) if B[i][j]), None)
        if pivot is None:
            continue
        B[out], B[pivot] = B[pivot], B[out]
        c = B[out][j]
        B[out] = [v / c for v in B[out]]
        for i in range(out + 1, nrows):
            c = B[i][j]
            if c:
                B[i] = [x - c * y for x, y in zip(B[i], B[out])]
        out += 1
        if out == nrows:
            break
    return out

def charpoly(A):
    n = len(A)
    if not n:
        return [F(1)]
    B = eye(n)
    coefficients = [F(1)]
    for k in range(1, n + 1):
        guard()
        B = mm(A, B)
        c = -sum((B[i][i] for i in range(n)), F(0)) / F(k)
        coefficients.append(c)
        for i in range(n):
            B[i][i] += c
    return coefficients

def polymul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out

def positive_symmetric(A, code):
    n = len(A)
    need(all(A[i][j] == A[j][i]
             for i in range(n) for j in range(n)), code + "_SYMMETRY")
    minors = []
    for k in range(1, n + 1):
        guard()
        value = determinant([row[:k] for row in A[:k]])
        need(value > 0, code + "_LEADING_MINOR", str(k))
        minors.append(value)
    return minors

def matrix_unit(i, j):
    x = [F(0)] * 9
    x[3 * i + j] = F(1)
    return tuple(x)

LABEL_GENERATORS = [
    matrix_unit(0, 1), matrix_unit(1, 2), matrix_unit(2, 0)
]

def label_product(a, b):
    return tuple(
        sum((a[3 * i + k] * b[3 * k + j] for k in range(3)), F(0))
        for i in range(3) for j in range(3)
    )

def label_tree(t):
    if t[0] == "g":
        return LABEL_GENERATORS[t[1]]
    if t[0] == "s":
        return tuple(t[1] * x for x in label_tree(t[2]))
    if t[0] == "b":
        a, b = label_tree(t[1]), label_tree(t[2])
        ab, ba = label_product(a, b), label_product(b, a)
        return tuple(x - y for x, y in zip(ab, ba))
    raise ScientificFailure("UNKNOWN_LABEL_TREE_NODE")

def gram_from_labels():
    labels = [label_tree(t) for t in UT]
    G = [[sum((x * y for x, y in zip(a, b)), F(0))
          for b in labels] for a in labels]
    positive_symmetric(G, "LEVI_GRAM")
    Gi = inverse(G, "LEVI_GRAM_SINGULAR")
    need(mm(G, Gi) == eye(8), "LEVI_GRAM_INVERSE")
    for i in range(8):
        for j in range(8):
            if Gi[i][j]:
                need(UD[i] == UD[j], "GRAM_WEIGHT_BLOCK")
    return labels, G, Gi

class Model:
    def __init__(self, r, s, box, omitted=()):
        guard()
        self.r, self.s, self.box = r, s, tuple(box)
        self.A = [[2, -1, -1], [-1, 2, -1], [-r, -s, 2]]
        self.omitted = set(omitted)
        self.degrees = sorted(
            (d for d in product(*(range(x + 1) for x in box)) if any(d)),
            key=lambda d: (sum(d), d)
        )
        self.L, self.I, self.Q = {}, {}, {}
        self.seeds = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    exponent = 1 - self.A[i][j]
                    p = adpower(E[i], E[j], exponent)
                    d = [0, 0, 0]
                    d[i], d[j] = exponent, 1
                    self.seeds.append(
                        ("s%d%d" % (i + 1, j + 1), tuple(d), p, exponent)
                    )
        self.build()

    def fits(self, d):
        return all(0 <= d[i] <= self.box[i] for i in range(3))

    def build(self):
        # Free Lie construction: all homogeneous binary brackets.
        for d in self.degrees:
            guard()
            span = Span()
            if sum(d) == 1:
                span.insert(E[d.index(1)])
            else:
                for left in product(*(range(x + 1) for x in d)):
                    if not any(left):
                        continue
                    right = subdegree(d, left)
                    if not any(right) or left > right:
                        continue
                    lv = self.L[left].vectors()
                    rv = self.L[right].vectors()
                    for i, x in enumerate(lv):
                        for j, y in enumerate(rv):
                            if left == right and i >= j:
                                continue
                            span.insert(bracket(x, y))
            self.L[d] = span

        # Whole positive ideal in this downbox; all seeds share one span.
        for d in self.degrees:
            guard()
            ideal = Span()
            for name, sd, p, exponent in self.seeds:
                if sd == d and name not in self.omitted:
                    ideal.insert(p)
            for i in range(3):
                previous = subunit(d, i)
                if previous in self.I:
                    for p in self.I[previous].vectors():
                        ideal.insert(bracket(E[i], p))
            self.I[d] = ideal
            for p in ideal.vectors():
                need(not self.L[d].reduce(p), "IDEAL_NOT_IN_FREE_LIE", str(d))
            quotient = Span()
            for p in self.L[d].vectors():
                quotient.insert(ideal.reduce(p))
            self.Q[d] = quotient
            need(len(quotient) + len(ideal) == len(self.L[d]),
                 "QUOTIENT_DIMENSION", str(d))

    def dim(self, d):
        return len(self.Q[d]) if d in self.Q else 0

    def basis(self, d):
        return self.Q[d].vectors() if d in self.Q else []

    def normal(self, p, d):
        if not p:
            return {}
        need(self.fits(d) and any(d), "NONPOSITIVE_OR_OUTSIDE_TARGET", str(d))
        degree_check(p, d)
        need(not self.L[d].reduce(p), "IMAGE_NOT_IN_FREE_LIE", str(d))
        return self.I[d].reduce(p)

    def coords(self, p, d):
        q = self.normal(p, d)
        if d not in self.Q:
            need(not q, "OUTSIDE_QUOTIENT_TARGET", str(d))
            return []
        return self.Q[d].coords(q)

    def audit(self):
        # Check the literal raw relations first, including deliberately omitted ones.
        relevant = []
        for name, d, p, exponent in self.seeds:
            item = {
                "name": name, "degree": d, "exponent": exponent,
                "relevant": self.fits(d), "raw_tensor_support": len(p)
            }
            if self.fits(d):
                need(not self.normal(p, d),
                     "MISSING_POSITIVE_SERRE_" + name, str(d))
                item["relation_zero"] = True
            else:
                item["exclusion"] = "positive degree exceeds downbox"
            relevant.append(item)

        closure_count = 0
        ideal_lowering_count = 0
        free_lowering_count = 0
        for d in self.degrees:
            guard()
            for p in self.I[d].vectors():
                for i in range(3):
                    target = addunit(d, i)
                    if self.fits(target):
                        need(not self.normal(bracket(E[i], p), target),
                             "WHOLE_POSITIVE_IDEAL_CLOSURE", str((d, i)))
                        closure_count += 1
                    target = subunit(d, i)
                    need(not self.normal(lower(p, i, self.A), target),
                         "LOWERING_DOES_NOT_DESCEND", str((d, i)))
                    ideal_lowering_count += 1
            if sum(d) > 1:
                for p in self.L[d].vectors():
                    for i in range(3):
                        self.normal(lower(p, i, self.A), subunit(d, i))
                        free_lowering_count += 1

        return {
            "seeds": relevant,
            "generator_closure_checks": closure_count,
            "ideal_lowering_checks": ideal_lowering_count,
            "free_lowering_checks": free_lowering_count,
            "mixed_seed_handling": "one joint span; no sum-of-ranks assumption",
            "dimensions": [
                {"degree": d, "free": len(self.L[d]),
                 "ideal": len(self.I[d]), "quotient": len(self.Q[d])}
                for d in self.degrees
            ]
        }

def coeval(M, d, p, Gi, mode="full"):
    need(mode in ("full", "omit-W1", "omit-mixed", "reverse-W1"),
         "UNKNOWN_CONTRACTION_MODE")
    words = []
    for j in range(8):
        y = theta_action(UT[j], p, M.A)
        y = M.normal(y, subdegree(d, UD[j]))
        if j == 1 and mode == "omit-W1":
            y = {}
        if j == 1 and mode == "reverse-W1":
            y = scale(y, F(-1))
        words.append(y)
    out = {}
    for i in range(8):
        for j in range(8):
            c = Gi[i][j]
            if mode == "omit-mixed" and i in (3, 4) and j in (3, 4):
                c = F(0)
            if c:
                out = lin(((F(1), out), (c, bracket(U[i], words[j]))))
    return M.normal(out, d)

def endomorphism(M, d, action):
    basis = M.basis(d)
    return matcols([M.coords(action(p), d) for p in basis], len(basis))

def ef_action(M, p):
    return bracket(E[2], lower(p, 2, M.A))

def correction_one(M, p):
    return bracket(U[1], theta_action(UT[1], p, M.A))

def makeZ(i, j):
    if i < 0 or j < 0:
        return {}
    return bracket(adpower(E[2], E[0], i), adpower(E[2], E[1], j))

def vector_dump(p):
    return [
        ["".join(str(i + 1) for i in w), str(c)]
        for w, c in sorted(p.items())
    ]

def matrix_dump(A):
    return [[str(x) for x in row] for row in A]

def matrix_nonzero(A):
    return any(x for row in A for x in row)

def principal(A, indices):
    return [[A[i][j] for j in indices] for i in indices]

def ell(r, s, n, i):
    return {0: n * (s - n + 1),
            1: 2 * n - 2 - s - r * n,
            2: 2 * (r - 1)}.get(i, 0)

def kappa(r, s, n, i):
    return {n: -n * (r - n + 1),
            n - 1: r + s * n - 2 * n + 2,
            n - 2: -2 * (s - 1)}.get(i, 0)

def horizontal_check(M, d, Aactual, EFactual, C1actual):
    r, s, n = M.r, M.s, d[2]
    indices = list(range(max(0, n - s), min(r, n) + 1))
    m = M.dim(d)
    need(m == len(indices), "HORIZONTAL_ACTUAL_DIMENSION")
    z = [makeZ(i, n - i) for i in indices]

    # Verify invalid X/Y words really vanish in the constructed quotient.
    for i in range(n + 1):
        if i not in indices:
            need(not M.normal(makeZ(i, n - i), d),
                 "INVALID_STRING_SURVIVES", str(i))

    P = matcols([M.coords(p, d) for p in z], m)
    Pi = inverse(P, "CLAIMED_Z_VECTORS_NOT_A_BASIS")
    AZ = mm(mm(Pi, Aactual), P) if m else []
    BZ = mm(mm(Pi, EFactual), P) if m else []
    C1Z = mm(mm(Pi, C1actual), P) if m else []
    where = {i: k for k, i in enumerate(indices)}
    Bclaim = [[F(0)] * m for unused in range(m)]

    for column, i in enumerate(indices):
        j = n - i
        ai = i * (r - i + 1)
        bi = j * (s - j + 1)
        for rowindex, value in ((i - 1, ai), (i, ai + bi), (i + 1, bi)):
            if rowindex in where:
                Bclaim[where[rowindex]][column] += value
        expectedF = lin(((F(ai), makeZ(i - 1, j)),
                         (F(bi), makeZ(i, j - 1))))
        need(M.normal(lower(z[column], 2, M.A), subunit(d, 2))
             == M.normal(expectedF, subunit(d, 2)),
             "HORIZONTAL_F3_TABLE")
        for k, expected in (
            (1, scale(adpower(E[2], E[1], n - 1), F(ell(r, s, n, i)))),
            (2, scale(adpower(E[2], E[0], n - 1), F(kappa(r, s, n, i))))
        ):
            target = subdegree(d, UD[k])
            need(M.normal(theta_action(UT[k], z[column], M.A), target)
                 == M.normal(expected, target),
                 "HORIZONTAL_W%d_TABLE" % k)

        if n == 2:
            table3 = [4 * (s - 1), r, -2 * (r - 1)]
            table4 = [2 * (s - 1), -s, -4 * (r - 1)]
            for k, table in ((3, table3), (4, table4)):
                target = subdegree(d, UD[k])
                need(M.normal(theta_action(UT[k], z[column], M.A), target)
                     == M.normal(scale(E[2], F(table[i])), target),
                     "N2_W%d_TABLE" % k)
            zero_indices = range(5, 8)
        else:
            zero_indices = range(3, 8)
        for k in zero_indices:
            need(not M.normal(theta_action(UT[k], z[column], M.A),
                              subdegree(d, UD[k])),
                 "HIGHER_W_TARGET_NOT_ZERO", str(k))

    need(BZ == Bclaim, "HORIZONTAL_EF_MATRIX")
    expected_characteristic = [F(1)]
    spectrum_evidence = {}

    if n == 2:
        literal = [
            [F(4 * (s - 1)), F(5 * r + s, 3), F(0)],
            [F(0), F(5 * (r + s) - 4), F(0)],
            [F(0), F(r + 5 * s, 3), F(4 * (r - 1))]
        ]
        expected = [[literal[i][j] for j in indices] for i in indices]
        need(AZ == expected, "N2_FULL_MIXED_GRAM_MATRIX")
        eigenvalues = [literal[i][i] for i in indices]
        need(all(x > 0 for x in eigenvalues), "N2_POSITIVE_SPECTRUM")
        for value in eigenvalues:
            expected_characteristic = polymul(
                expected_characteristic, [F(1), -value])
        spectrum_evidence = {"positive_eigenvalues": list(map(str, eigenvalues))}
        if r == s == 1:
            need(AZ == [[F(6)]], "N2_ACTIVE_GRAM_CORNER_SCALAR")
    else:
        expected = [row[:] for row in Bclaim]
        for column, i in enumerate(indices):
            if 1 in where:
                expected[where[1]][column] -= ell(r, s, n, i)
            if n - 1 in where:
                expected[where[n - 1]][column] += kappa(r, s, n, i)
        need(AZ == expected, "HORIZONTAL_FULL_CONTRACTION_MATRIX")

        marked = [i for i in (1, n - 1) if i in where]
        values = []
        for i in marked:
            value = ((n + 1) * r + n * (s - n + 1)
                     if i == 1 else
                     (n + 1) * s + n * (r - n + 1))
            need(value > 0, "MARKED_EIGENVALUE_NOT_POSITIVE")
            row = where[i]
            need(all(AZ[row][c] == (value if c == row else 0)
                     for c in range(m)), "MARKED_ROW_CANCELLATION")
            values.append(F(value))
        remaining = [where[i] for i in indices if i not in marked]
        block = principal(BZ, remaining)
        weights = []
        for coordinate in remaining:
            i = indices[coordinate]
            j = n - i
            weight = (
                factorial(i) * factorial(r) // factorial(r - i)
                * (factorial(j) * factorial(s) // factorial(s - j))
            )
            need(weight > 0, "AUXILIARY_METRIC_WEIGHT")
            weights.append(F(weight))
        hermitian = [
            [weights[i] * block[i][j] for j in range(len(block))]
            for i in range(len(block))
        ]
        minors = positive_symmetric(hermitian, "REMAINING_PRINCIPAL_BLOCK")
        expected_characteristic = charpoly(block)
        for value in values:
            expected_characteristic = polymul(
                expected_characteristic, [F(1), -value])
        spectrum_evidence = {
            "marked_positive_eigenvalues": list(map(str, values)),
            "remaining_indices": [indices[i] for i in remaining],
            "weighted_positive_leading_minors": list(map(str, minors))
        }

    cp = charpoly(AZ)
    need(cp == expected_characteristic, "SPECTRUM_CHARACTERISTIC_FACTORIZATION")
    F3matrix = matcols(
        [M.coords(lower(p, 2, M.A), subunit(d, 2)) for p in M.basis(d)],
        M.dim(subunit(d, 2))
    )
    kernel = m - rank(F3matrix)
    need(kernel == (1 if n <= min(r, s) else 0),
         "HORIZONTAL_F3_KERNEL_DIMENSION")

    if (r, s, n) == (3, 7, 8):
        need(BZ == [[10, 4, 0], [7, 16, 3], [0, 12, 18]],
             "SUPPLIED_N8_EF")
        need(C1Z == [[17, -4, 0], [0, 0, 0], [0, 0, 0]],
             "SUPPLIED_N8_NONZERO_W1_CORRECTION")
        need(AZ == [[27, 0, 0], [7, 16, 3], [0, 12, 18]],
             "SUPPLIED_N8_FULL_MATRIX")
        need(cp == list(map(F, [1, -61, 1170, -6804])),
             "SUPPLIED_N8_CHARACTERISTIC")
        need(17 * 17 > 37, "SUPPLIED_N8_POSITIVE_QUADRATIC_ROOTS")
        spectrum_evidence["exact_eigenvalues"] = [
            "27", "17 + sqrt(37)", "17 - sqrt(37)"
        ]
        need(matrix_nonzero(C1Z), "SUPPLIED_N8_W1_MUST_BE_NONZERO")

    return {
        "Z_indices": indices,
        "actual_matrix_in_Z_basis": matrix_dump(AZ),
        "actual_EF_in_Z_basis": matrix_dump(BZ),
        "actual_W1_correction_in_Z_basis": matrix_dump(C1Z),
        "characteristic_descending": list(map(str, cp)),
        "F3_kernel_dimension": kernel,
        "positive_spectrum_evidence": spectrum_evidence,
        "zero_component": m == 0
    }

def arbitrary_check(M, d, Aactual, EFactual, C1actual, Wmatrices):
    a, b, n = d
    r, s = M.r, M.s
    t = r * a + s * b
    defect = t - n
    need(r < s and 1 <= r <= 3 and a >= 1 and b >= 1
         and 0 <= defect <= s - 2 and 2 * defect < t,
         "ARBITRARY_CASE_OUTSIDE_STATED_STRIP")
    need(M.dim(d) > 0, "NONVACUOUS_ARBITRARY_DEGREE")
    for j in range(2, 8):
        need(not matrix_nonzero(Wmatrices[j]), "STRIP_HIGHER_W_NOT_ZERO", str(j))
    need(Aactual == madd(EFactual, C1actual), "ARBITRARY_STRIP_CONTRACTION")
    need(matrix_nonzero(C1actual), "ARBITRARY_W1_CORRECTION_MUST_BE_NONZERO")

    # Independently explicit nonzero vector in the requested case.
    need((r, s, a, b, n) == (1, 3, 2, 1, 4),
         "UNEXPECTED_ARBITRARY_CASE")
    udegree = (2, 1, 1)
    base = M.normal(U[5], udegree)
    need(bool(base), "LEVEL_ONE_U5_MUST_BE_NONZERO")
    need(not M.normal(lower(U[5], 2, M.A), (2, 1, 0)),
         "U5_LOWEST_STRING_VECTOR")
    v = adpower(E[2], U[5], 3)
    nv = M.normal(v, d)
    need(bool(nv), "EXPLICIT_ARBITRARY_VECTOR_MUST_BE_NONZERO")
    fv = v
    for unused in range(3):
        fv = lower(fv, 2, M.A)
    need(M.normal(fv, udegree) == scale(base, F(36)),
         "ARBITRARY_NONVACUITY_CHEVALLEY_IDENTITY")
    return {
        "explicit_nonzero_vector_coordinates": list(map(str, M.coords(v, d))),
        "F3_cubed_E3_cubed_u5_factor": "36",
        "whole_component_dimension_derived_not_postulated": M.dim(d)
    }

def compute_case(r, s, a, b, n, Gi):
    d = (a, b, n)
    M = Model(r, s, d)
    audit = M.audit()
    basis = M.basis(d)
    m = len(basis)

    # All needed W maps are constructed before any closed-matrix comparison.
    Wmatrices = []
    targets = {}
    Wreport = []
    for j in range(8):
        target = subdegree(d, UD[j])
        cols = [M.coords(theta_action(UT[j], p, M.A), target) for p in basis]
        Wmatrix = matcols(cols, M.dim(target))
        Wmatrices.append(Wmatrix)
        if target in M.Q:
            targets[str(target)] = [vector_dump(p) for p in M.basis(target)]
        Wreport.append({
            "j": j, "target_degree": target,
            "shape": [M.dim(target), m],
            "matrix": matrix_dump(Wmatrix)
        })

    Aactual = endomorphism(M, d, lambda p: coeval(M, d, p, Gi))
    EFactual = endomorphism(M, d, lambda p: ef_action(M, p))
    C1actual = endomorphism(M, d, lambda p: correction_one(M, p))
    cp = charpoly(Aactual)
    det = determinant(Aactual)
    need(cp[-1] == ((-1) ** m) * det, "CHARACTERISTIC_DETERMINANT_AGREEMENT")
    need(det != 0, "CLAIMED_FINITE_INVERTIBILITY")

    report = {
        "input_r_s_a_b_n": [r, s, a, b, n],
        "h3_weight": 2 * n - r * a - s * b,
        "dimension": m,
        "quotient_basis_tensor_polynomials": [vector_dump(p) for p in basis],
        "W_target_bases": targets,
        "all_W_maps": Wreport,
        "actual_coeval_bracket_matrix": matrix_dump(Aactual),
        "actual_EF_matrix": matrix_dump(EFactual),
        "actual_W1_correction_matrix": matrix_dump(C1actual),
        "characteristic_descending": list(map(str, cp)),
        "determinant": str(det),
        "full_positive_ideal_audit": audit
    }
    if a == b == 1:
        report["horizontal_comparison"] = horizontal_check(
            M, d, Aactual, EFactual, C1actual)
    else:
        report["arbitrary_degree_comparison"] = arbitrary_check(
            M, d, Aactual, EFactual, C1actual, Wmatrices)
    return M, Aactual, report

def intended_rejection(name, expected_code, action, additional=None):
    try:
        action()
    except ScientificFailure as exc:
        need(exc.code == expected_code, "WRONG_NEGATIVE_CONTROL_FAILURE",
             name + ": " + exc.code + " instead of " + expected_code)
        out = {
            "name": name,
            "status": "REJECTED_FOR_INTENDED_SCIENTIFIC_INVARIANT",
            "invariant": exc.code,
            "detail": exc.detail
        }
        if additional is not None:
            out["mutation_data"] = additional
        return out
    raise ScientificFailure("NEGATIVE_CONTROL_WAS_ACCEPTED", name)

CASES = [
    (1, 1, 1, 1, 2),  # singular full-Cartan corner; active mixed Gram
    (1, 2, 1, 1, 2),  # unequal, positive h3
    (1, 3, 1, 1, 2),  # unequal, zero h3
    (2, 3, 1, 1, 2),  # unequal, negative h3; all three n2 coordinates
    (2, 4, 1, 1, 3),  # unequal, zero h3, n >= 3
    (2, 5, 1, 1, 3),  # unequal, negative h3, n >= 3
    (3, 5, 1, 1, 3),  # nonzero F3 kernel; full operator still invertible
    (3, 7, 1, 1, 8),  # supplied nonzero W1 boundary correction
    (1, 3, 2, 1, 4),  # nonvacuous arbitrary-degree two-lowering strip
    (1, 2, 1, 1, 4),  # explicitly reported zero-space boundary control
]

def run():
    labels, G, Gi = gram_from_labels()
    records = []
    models = {}
    baselines = {}
    for case in CASES:
        guard()
        M, Aactual, report = compute_case(*case, Gi)
        models[case] = M
        baselines[case] = Aactual
        records.append(report)

    controls = []
    key8 = (3, 7, 1, 1, 8)
    key2 = (1, 1, 1, 1, 2)
    M8, M2 = models[key8], models[key2]
    for name, model, key, mode, invariant in (
        ("omitted_W1", M8, key8, "omit-W1",
         "COEVALUATION_BRACKET_CONTRACTION"),
        ("omitted_n2_mixed_Gram", M2, key2, "omit-mixed",
         "FULL_MIXED_GRAM_COEVALUATION"),
        ("wrong_W1_commutator_order", M8, key8, "reverse-W1",
         "THETA_COMMUTATOR_ORDER_CONTRACTION")
    ):
        d = key[2:]
        mutant = endomorphism(
            model, d, lambda p, model=model, d=d, mode=mode:
            coeval(model, d, p, Gi, mode))
        baseline = baselines[key]
        controls.append(intended_rejection(
            name, invariant,
            lambda mutant=mutant, baseline=baseline, invariant=invariant:
            need(mutant == baseline, invariant),
            {"mutant_matrix": matrix_dump(mutant),
             "definition_matrix": matrix_dump(baseline)}
        ))

    # Omit each remaining seed and each relevant fixed seed separately.
    for name, r, s, d, seed in (
        ("omitted_remaining_X4", 3, 7, (1, 1, 8), "s31"),
        ("omitted_remaining_Y8", 3, 7, (1, 1, 8), "s32"),
        ("omitted_fixed_s12", 1, 3, (2, 1, 4), "s12"),
        ("omitted_fixed_s13", 1, 3, (2, 1, 4), "s13")
    ):
        guard()
        broken = Model(r, s, d, omitted=(seed,))
        controls.append(intended_rejection(
            name, "MISSING_POSITIVE_SERRE_" + seed, broken.audit))

    guard()
    return {
        "scope": "exact prescribed finite cases only; not a uniform proof",
        "actual_source_import":
            "f276 displayed full-Cartan/free-source/full-Serre-ideal bridge",
        "negative_relations":
            "only via that named bridge; no finite test promoted to all-height",
        "Levi_labels_flat_row_major":
            [[str(x) for x in label] for label in labels],
        "Gram": matrix_dump(G),
        "inverse_Gram": matrix_dump(Gi),
        "cases": records,
        "negative_controls": controls,
        "all_claimed_case_and_control_checks_completed": True
    }

def entry():
    code = 3
    try:
        need(len(sys.argv) == 1, "CLI_ARGUMENTS",
             "This checker has fixed finite inputs and accepts no arguments.")
        report = run()
        guard()
        report["status"] = "PASS_EXACT_FINITE"
        code = 0
    except Incomplete as exc:
        report = {"status": "INCOMPLETE", "reason": str(exc)}
        code = 2
    except ScientificFailure as exc:
        report = {
            "status": "FAIL_SCIENTIFIC_INVARIANT",
            "invariant": exc.code,
            "detail": exc.detail
        }
        code = 1
    except Exception as exc:
        report = {
            "status": "ERROR_NOT_PASS",
            "exception_type": type(exc).__name__,
            "reason": str(exc)
        }
        code = 3
    report["observed_monotonic_seconds"] = time.monotonic() - START
    report["calculation_deadline_seconds"] = 50
    report["asserts_used_as_gates"] = False
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return code

if __name__ == "__main__":
    sys.exit(entry())
END FILE f377_exact_checker_v1.py

## Chronology, attribution, and unpaid gates

- Read the complete manifest and freeze receipt, then all six status/permission controls, **before** scientific packet access.
- Read the complete ordered literal packet, raw, through LF893: ranges 1–100, 101–200, 201–300, 301–400, 401–500, 501–600, 601–700, 701–800, 801–893. This included S1’s ending LF790, all S2 LF1–27, and all S3 LF1–74.
- Read the parent live metadata supply. The supplied matching hashes, sizes, LF counts, and **2026-10-30T09:54:48-0700 PDT** observation are **parent observations**, not child hash execution or a child-native start.
- The later **2026-10-30T10:00:14-0700 PDT** clock was likewise supplied by the parent. Substantive derivation checkpoints were sent; no unobserved native cadence or completion timestamp is claimed.
- No sibling outcomes, held scientific payloads, sealed data, author code, external models, public web sources, packages, or scientific executables were read or run.

Remaining gates are precise: Main must independently inspect and pin the returned source, run it once with the stated finite bound, bind stdout and exit status, and dispose its actual results. A timeout or exception is **INCOMPLETE/ERROR**, not successful verification. Even a successful run establishes only the printed finite instances under the named source/negative-ideal bridge. It does not establish either uniform theorem, independent-family/human/kernel verification, original-source authenticity, novelty, generalized-primary imports, or whole-target acceptance.