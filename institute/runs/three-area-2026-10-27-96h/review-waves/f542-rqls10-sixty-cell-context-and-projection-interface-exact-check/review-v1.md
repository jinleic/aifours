# f542 — Exact sixty-cell routing and projection-interface check

**Role:** FINITE  
**Verdict:** Correct on the assigned finite and algebraic interfaces; no mathematical defect found.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR** in the candidate’s assigned interfaces.  
**Scientific execution:** **NOT RUN.** The complete independent checker below is supplied as source, not as executed evidence.

This return does **not** adopt the complete f535 operator theorem, establish a physical witness, or provide independent-family, human, kernel, novelty, or unrestricted hundred-ray assurance.

## 1. Inputs, chronology, and boundaries

Before the pre-body ACK, I read the complete:

- Manifest, LF 1–116.
- Freeze receipt, LF 1–47.
- Dispatch receipt.
- Parent live-metadata supply.
- All permission/status controls listed in the manifest.

**Correction to my ACK:** I wrote “13 controls”; the manifest actually lists **12**. All twelve were read through their endings. This was a count misstatement in my acknowledgement, not an omitted control.

After that ACK, I read the literal packet consecutively, in raw ranges of at most twenty lines, **LF 1–461, including its ending**, before deriving the mathematics below. Its scientific coverage was:

- **S1:** Complete f535 candidate, logical source lines 1–430.
- **S2:** Complete original physical-context disposition, source lines 1–29.

The S1 metadata’s 429 LF count and the packet’s 430 logical source lines are compatible with a final logical line lacking a terminating LF; I do not treat this as evidence of missing content.

Bindings supplied by Main:

- Manifest SHA-256: `c607a4664e2e81ffc0ab025543bd77356dd9b09fc45a70d61f34d26677145288`
- Receipt SHA-256: `87958b3dfec8f1ec1f58d6213e767b70103060de91f0033dc990f35e30c55495`
- Packet SHA-256: `a25865a3ffb5cc6ce998c035e920b39224a0bbc0925613b9b3d768e89ee1e0d8`

These are **parent-supplied bindings**, not child-executed hash observations.

I performed no scientific execution, Git operation, source-following, public search, author-code reading, sibling-output reading, external-model call, or filesystem modification. Held episodes and their consumers remained NONINPUT. No child-native clock or elapsed-time observation is claimed.

## 2. Actual physical cells and their consuming contexts

Let

\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2),
\qquad a\in\mathbb Z_5,\ u\in\mathbb Z_2.
\]

This inverse has both required properties:

\[
\operatorname{crt}(a,u)\equiv a\pmod5,\qquad
\operatorname{crt}(a,u)\equiv u\pmod2.
\]

The actual sixty-cell support is

\[
H=\{(r,c)\in\mathbb Z_{10}^2:
(c-r)\bmod10\in\{2,3,4,7,8,9\}\}.
\]

Equivalently, its cells are uniquely parametrized by

\[
r=\operatorname{crt}(a,u),\quad
c=\operatorname{crt}(a+d,v),\quad
d\in\{2,3,4\}.
\]

Thus there are exactly \(5\cdot3\cdot2\cdot2=60\) cells.

The consuming-side context labels are the **physical** labels

\[
R_r,\qquad C_c,\qquad L_{(r+c)\bmod10}.
\]

They yield:

- Ten row contexts, each with six cells.
- Ten column contexts, each with six cells.
- Ten cyclic-symbol contexts, each with six cells.
- Exactly three context memberships per cell, hence 180 memberships in total.

For a symbol whose CRT coordinates are \((s,w)\), the equations

\[
2a+d=s\pmod5,\qquad u+v=w\pmod2
\]

give

\[
a=3(s-d)\pmod5,\qquad v=w-u\pmod2.
\]

The factor **3** is the inverse of 2 modulo 5. It is required by actual \(r+c\) routing, not by a covariance assumption.

### Four-cell blocks

For each \((a,d)\), the four cells indexed by \((u,v)\in\mathbb Z_2^2\) form one block. Every pair shares exactly one actual context:

- Two pairs share rows.
- Two pairs share columns.
- Two pairs share symbols.

Consequently the fifteen blocks have exactly **90 within-block pair certificates**, thirty of each family.

A block uses **six context labels**, not four: two rows, two columns, and two symbols. To cover the assignment’s context-omission control without narrowing it, the checker below treats **every one of those six omissions in every block**—90 omission cases.

Under the hypothetical ONB assumptions, these pair certificates make the four block projections mutually orthogonal. Therefore

\[
F_{a,d}=\sum_{u,v}p_{a,d}^{uv}
\]

is an actual rank-four orthogonal projection, and

\[
E_{a,d}=I_6-F_{a,d}
\]

is an actual rank-two orthogonal projection. No incidence mask is substituted for either operator.

## 3. Deriving the fifteen scalar equations from physical contexts

Pair the two physical contexts in a family having the same residue modulo five. Their union consists of twelve cells, partitioned into three complete four-cell blocks.

Adding their two ONB equations gives

\[
\sum_{\text{three blocks}}F_{a,d}=2I_6.
\]

Substituting \(F=I_6-E\) gives

\[
\sum_{\text{three blocks}}E_{a,d}=I_6.
\]

This derives the missing-projection equations from the physical contexts:

\[
R_a:\quad \sum_{d=2}^4E_{a,d}=I_6,
\]

\[
C_b:\quad \sum_{d=2}^4E_{b-d,d}=I_6,
\]

\[
L_s:\quad \sum_{d=2}^4E_{3(s-d),d}=I_6.
\]

There are fifteen equations in fifteen operator unknowns. Their scalar coefficient matrix \(M\) is obtained by applying these equations to any fixed matrix entry. This scalar reduction does not assert that arbitrary solutions of the linear equations are physical projection solutions.

The supplied checker constructs \(M\) by collecting cells from the actual thirty contexts. It does **not** initialize \(M\) by copying these three displayed formulas.

## 4. Exact rational rank, nullspace, and row-span certificates

Write

\[
A_a=E_{a,2},\qquad B_a=E_{a,3},\qquad C_a=E_{a,4}.
\]

For row-span calculations, use \(R_a,C_b,L_s\) for the corresponding **coefficient row vectors**. Their right-hand sides are all the same identity.

Define

\[
h_a=C_a-A_{a+1},
\qquad
q_a=2A_{a+3}-A_a-A_{a+1}.
\]

All indices below are modulo five.

### Certificate 1: \(h_a\) is constant

The exact row identity is

\[
\boxed{h_a-h_{a-1}=R_a-C_{a+3}.}
\]

The right-hand sides cancel, so every solution satisfies \(h_a=h_{a-1}\). This verifies the candidate’s \(C_a-A_{a+1}=K\) interface.

### Certificate 2: the averaging relation

The exact row identity is

\[
\boxed{
q_a=L_{2a+3}+C_{a+4}+C_a-R_a-R_{a+1}-R_{a+2}.
}
\]

Again the right-hand sides cancel. Hence

\[
2A_{a+3}=A_a+A_{a+1}.
\]

### Certificate 3: constancy follows from the linear equations alone

A further exact identity is

\[
\boxed{
5(A_{a+1}-A_a)
=q_{a+1}-3q_{a+2}+3q_{a+3}-q_{a+4}.
}
\]

Therefore all \(A_a\) are equal. Certificate 1 then makes all \(C_a\) equal, and the row equations make all \(B_a\) equal.

This is stronger than needed for the candidate’s projection-average step: **the scalar linear equations already exclude every nonconstant mode**. The candidate’s projection-average argument remains valid; its use of projection structure at that point is unnecessary, not erroneous.

### Rank and affine difference space

The complete scalar solution set is exactly

\[
A_a=\alpha,\qquad
B_a=\beta,\qquad
C_a=1-\alpha-\beta
\quad\text{for every }a.
\]

Thus

\[
\boxed{\operatorname{rank}_{\mathbb Q}M=13,\qquad
\dim_{\mathbb Q}\ker M=2.}
\]

The augmented system also has rank 13.

An affine origin is the vector with every \(A_a=B_a=0\) and every \(C_a=1\). A basis for its homogeneous difference space is

\[
v_A:\ (A_a,B_a,C_a)=(1,0,-1),
\]

\[
v_B:\ (A_a,B_a,C_a)=(0,1,-1).
\]

These statements concern the fifteen scalar coordinates, or one operator matrix entry at a time—not a two-dimensional moduli space of physical realizations.

### Omitting an entire context family

For each of the three possible family omissions, the remaining ten-row scalar matrix has

\[
\boxed{\operatorname{rank}=9,\qquad \operatorname{nullity}=6.}
\]

One way to see this exactly is to decompose the cyclic scalar coordinates algebraically into fifth-root modes. This is a decomposition of arbitrary data, not an imposed covariance of vectors.

For a mode \(t^5=1\), the three reindexed rows are proportional to

\[
(1,1,1),\qquad (t,1,t^{-1}),\qquad
(t^3,1,t^{-3}).
\]

At \(t=1\), any two have rank one. At each nonconstant fifth-root mode, any two have rank two: proportionality would force respectively \(t=1\), \(t^3=1\), or \(t^2=1\), all impossible for a nontrivial fifth root. Hence \(1+4\cdot2=9\).

The checker independently obtains these ranks by rational elimination and returns a nonconstant kernel witness for each omission. These witnesses certify loss of the **linear rigidity**, not physical feasibility of an altered problem.

## 5. Universal three-partition commutation interface

Suppose

\[
\sum_{i=1}^3E_i=I,\qquad \sum_{i=1}^3T_i=I
\]

are orthogonal projection partitions and \(T_iE_i=0\). Taking adjoints also gives \(E_iT_i=0\).

For \(j\ne k\):

- If \(i=j\), then \(E_jT_iE_k=0\).
- If \(i=k\), then \(E_jT_iE_k=0\).
- Otherwise the three indices are distinct, and

\[
E_jT_iE_k
=E_j(I-T_j-T_k)E_k
=0.
\]

Thus every off-diagonal \(E\)-block of \(T_i\) vanishes. Consequently

\[
\boxed{[T_i,E_j]=0\quad\text{for all }i,j.}
\]

This is a universal operator-algebra proof, valid in every dimension and over complex Hilbert spaces. It is not an inference from selected \(6\times6\) examples.

The checker verifies all eighteen off-diagonal index certificates using formal noncommuting words and the stated relations.

## 6. Universal individual-ray intersection interface

Inside one four-cell block, let its mutually orthogonal rank-one projections be \(p^{uv}\). Define

\[
\mathsf R_u=p^{u0}+p^{u1},\qquad
\mathsf C_v=p^{0v}+p^{1v}.
\]

Expanding the product, the common term is \(p^{uv}p^{uv}=p^{uv}\), and each other term is zero by block orthogonality. Therefore

\[
\boxed{\mathsf R_u\mathsf C_v=p^{uv}.}
\]

If both plane projections commute with every \(E_j\), then

\[
[p^{uv},E_j]
=\mathsf R_u[\mathsf C_v,E_j]
+[\mathsf R_u,E_j]\mathsf C_v
=0.
\]

This explicitly checks the consuming-side step from row and column planes to the **individual cell projection**. Plane commutation alone is not silently promoted to ray commutation.

For a rank-one projection \(p\) commuting with an orthogonal projection partition, each \(E_j\) preserves its one-dimensional range and acts there as 0 or 1. Their sum acts as 1, so precisely one acts as 1. This justifies the individual-ray sector conclusion under the preceding hypotheses.

### Plane-only mutation

Commutation of a plane does not by itself imply commutation of each ray in that plane. In formal \(2\times2\) matrix units, take

\[
R=e_{00}+e_{11},\qquad E=e_{00},\qquad
p=\tfrac12(e_{00}+e_{01}+e_{10}+e_{11}).
\]

Then \(R\) and \(p\) are projections, \(p\) has rank one, and

\[
[R,E]=0,\qquad
[p,E]=\tfrac12(e_{10}-e_{01})\ne0.
\]

This is an interface countermodel, **not** a sixty-cell ONB solution.

## 7. Distinct cells and the nonparallelness consumer

For any physical cell \(q=(r,c)\), its row and column intersect only at \(q\). Consequently any other row cell \(x\) and any other column cell \(y\) are distinct. There are \(60\cdot5\cdot5=1500\) such cell-separation checks.

Conditionally on the candidate’s sector conclusion, the row and column partners of a ray in its two-dimensional sector are both orthogonal to it and hence parallel to each other. Their cells are distinct by the preceding physical intersection fact.

**Global pairwise nonparallelness is the premise that makes this repeated ray a contradiction.** Removing that premise invalidates this final contradiction consumer. This observation neither supplies a repeated-ray sixty-cell solution nor proves that such a solution exists.

## 8. Mutation coverage and interpretation

The returned checker contains intended-reason controls for:

1. Omitting each complete row, column, or symbol family: rank 9, nullity 6, with a nonconstant kernel witness.
2. Reversing \(c-r\) to \(r-c\): the resulting cell set is not the frozen support, despite still containing sixty cells.
3. Using \(a+5u\) as the CRT inverse: it fails the claimed parity coordinate.
4. Replacing the symbol inverse factor 3 by 1: the emitted cells fail actual \(r+c\) membership.
5. Omitting every one of the six required physical context labels from every four-cell block: exactly one of that block’s six pair certificates is lost.
6. Omitting each of the six formal block-orthogonality relations: at least one row-plane/column-plane product certificate fails.
7. Replacing individual-ray commutation by plane-only commutation: rejected by the formal matrix-unit countermodel.
8. Removing global nonparallelness: rejected at the final proof consumer, without claiming altered-problem feasibility.

The reversed-difference mutation is rejected as a **target-routing mismatch**, not because an affinely related support must have different abstract counts or rank.

## 9. Complete independent checker — NOT RUN

The source below uses only the standard library. It performs no file I/O, printing, networking, subprocess creation, installation, deletion, or filesystem mutation. It has a cooperative 55-second deadline and leaves its result in `RESULTS`; a successful invocation would otherwise be silent.

No invocation, exit status, runtime, or checker output is claimed here.

### Exact proposed argv

- `argv[0]`: `python3`
- `argv[1]`: `-I`
- `argv[2]`: `-B`
- `argv[3]`: `-c`
- `argv[4]`: the complete source represented below: remove the initial `PY|` from every source line, join the resulting lines with LF, and append one final LF.

The executable name has not been resolved or hash-pinned by this reviewer.

BEGIN COMPLETE SOURCE

PY|from fractions import Fraction as F
PY|from itertools import combinations
PY|from time import monotonic
PY|
PY|START = monotonic()
PY|
PY|class Failure(Exception):
PY|    def __init__(self, reason):
PY|        super().__init__(reason)
PY|        self.reason = reason
PY|
PY|def tick():
PY|    if monotonic() - START > 55:
PY|        raise Failure("deadline")
PY|
PY|def need(condition, reason):
PY|    tick()
PY|    if not condition:
PY|        raise Failure(reason)
PY|
PY|def expect(reason, operation):
PY|    try:
PY|        operation()
PY|    except Failure as error:
PY|        need(error.reason == reason, "wrong_mutation_reason")
PY|    else:
PY|        raise Failure("mutation_not_rejected")
PY|
PY|def crt(a, u):
PY|    a %= 5
PY|    u %= 2
PY|    return a + 5 * ((u - a) % 2)
PY|
PY|def linear(terms, n=15):
PY|    answer = [F(0) for _ in range(n)]
PY|    for coefficient, vector in terms:
PY|        answer = [x + F(coefficient) * y
PY|                  for x, y in zip(answer, vector)]
PY|    return tuple(answer)
PY|
PY|def dot(a, b):
PY|    return sum((x * y for x, y in zip(a, b)), F(0))
PY|
PY|def rref(rows):
PY|    tick()
PY|    a = [list(map(F, row)) for row in rows]
PY|    if not a:
PY|        return a, []
PY|    n = len(a[0])
PY|    need(all(len(row) == n for row in a), "matrix_shape")
PY|    pivot_row = 0
PY|    pivots = []
PY|    for column in range(n):
PY|        tick()
PY|        chosen = next((k for k in range(pivot_row, len(a))
PY|                       if a[k][column]), None)
PY|        if chosen is None:
PY|            continue
PY|        a[pivot_row], a[chosen] = a[chosen], a[pivot_row]
PY|        divisor = a[pivot_row][column]
PY|        a[pivot_row] = [x / divisor for x in a[pivot_row]]
PY|        for k in range(len(a)):
PY|            if k != pivot_row and a[k][column]:
PY|                factor = a[k][column]
PY|                a[k] = [x - factor * y
PY|                        for x, y in zip(a[k], a[pivot_row])]
PY|        pivots.append(column)
PY|        pivot_row += 1
PY|        if pivot_row == len(a):
PY|            break
PY|    return a, pivots
PY|
PY|def kernel(rows):
PY|    a, pivots = rref(rows)
PY|    n = len(rows[0])
PY|    answer = []
PY|    for free in range(n):
PY|        if free in pivots:
PY|            continue
PY|        vector = [F(0) for _ in range(n)]
PY|        vector[free] = F(1)
PY|        for k, pivot in enumerate(pivots):
PY|            vector[pivot] = -a[k][free]
PY|        answer.append(tuple(vector))
PY|    return answer
PY|
PY|def reduce_word(word, orthogonality):
PY|    word = list(word)
PY|    i = 0
PY|    while i + 1 < len(word):
PY|        left, right = word[i], word[i + 1]
PY|        if left[0] == right[0] and left[0] in ("e", "t", "p"):
PY|            if left == right:
PY|                word[i:i + 2] = [left]
PY|                i = max(0, i - 1)
PY|                continue
PY|            if left[0] != "p":
PY|                return None
PY|            if frozenset((left[1], right[1])) in orthogonality:
PY|                return None
PY|        elif {left[0], right[0]} == {"e", "t"}:
PY|            if left[1] == right[1]:
PY|                return None
PY|        i += 1
PY|    return tuple(word)
PY|
PY|def normal(terms, orthogonality=frozenset()):
PY|    answer = {}
PY|    for coefficient, word in terms:
PY|        reduced = reduce_word(word, orthogonality)
PY|        if reduced is not None:
PY|            answer[reduced] = answer.get(reduced, F(0)) + F(coefficient)
PY|    return {word: value for word, value in answer.items() if value}
PY|
PY|def product_residual(u, v, orthogonality):
PY|    terms = [(F(1), (("p", 2 * u + x), ("p", 2 * y + v)))
PY|             for x in range(2) for y in range(2)]
PY|    terms.append((F(-1), (("p", 2 * u + v),)))
PY|    return normal(terms, orthogonality)
PY|
PY|def matrix_product(a, b):
PY|    answer = {}
PY|    for (i, j), x in a.items():
PY|        for (k, ell), y in b.items():
PY|            if j == k:
PY|                key = (i, ell)
PY|                answer[key] = answer.get(key, F(0)) + x * y
PY|    return {key: value for key, value in answer.items() if value}
PY|
PY|def matrix_difference(a, b):
PY|    return {key: a.get(key, F(0)) - b.get(key, F(0))
PY|            for key in set(a) | set(b)
PY|            if a.get(key, F(0)) != b.get(key, F(0))}
PY|
PY|def commutator(a, b):
PY|    return matrix_difference(matrix_product(a, b), matrix_product(b, a))
PY|
PY|def consume_repetition(nonparallel):
PY|    need(nonparallel, "nonparallel_required")
PY|
PY|def run():
PY|    delta = {2, 3, 4, 7, 8, 9}
PY|    cells = frozenset((r, c) for r in range(10) for c in range(10)
PY|                      if (c - r) % 10 in delta)
PY|    need(len(cells) == 60, "cell_count")
PY|    contexts = {}
PY|    for label in range(10):
PY|        contexts[("R", label)] = frozenset(x for x in cells if x[0] == label)
PY|        contexts[("C", label)] = frozenset(x for x in cells if x[1] == label)
PY|        contexts[("L", label)] = frozenset(x for x in cells
PY|                                         if sum(x) % 10 == label)
PY|    need(len(contexts) == 30, "context_count")
PY|    need(all(len(x) == 6 for x in contexts.values()), "context_size")
PY|    need(sum(map(len, contexts.values())) == 180, "membership_count")
PY|    need(all(sum(x in group for group in contexts.values()) == 3
PY|             for x in cells), "cell_degree")
PY|    keys = tuple((a, d) for a in range(5) for d in (2, 3, 4))
PY|    index = {key: k for k, key in enumerate(keys)}
PY|    blocks = {key: frozenset(x for x in cells
PY|                            if x[0] % 5 == key[0]
PY|                            and (x[1] - x[0]) % 5 == key[1])
PY|              for key in keys}
PY|    need(all(len(block) == 4 for block in blocks.values()), "block_size")
PY|    need(frozenset().union(*blocks.values()) == cells, "block_cover")
PY|    need(sum(map(len, blocks.values())) == 60, "block_partition")
PY|
PY|    def check_routes(inverse):
PY|        emitted = []
PY|        for a, d in keys:
PY|            for u in range(2):
PY|                for v in range(2):
PY|                    r, c = inverse(a, u), inverse((a + d) % 5, v)
PY|                    need((r % 5, r % 2) == (a, u), "crt_parity")
PY|                    need((c % 5, c % 2) == ((a + d) % 5, v),
PY|                         "crt_parity")
PY|                    emitted.append((r, c))
PY|        need(len(emitted) == len(set(emitted)) == 60, "crt_bijection")
PY|        need(frozenset(emitted) == cells, "support")
PY|
PY|    check_routes(crt)
PY|
PY|    def check_symbols(inverse_two):
PY|        for s in range(5):
PY|            for w in range(2):
PY|                emitted = []
PY|                for d in (2, 3, 4):
PY|                    a = inverse_two * (s - d) % 5
PY|                    for u in range(2):
PY|                        r = crt(a, u)
PY|                        c = crt(a + d, w - u)
PY|                        need((r + c) % 10 == crt(s, w), "symbol_routing")
PY|                        emitted.append((r, c))
PY|                need(frozenset(emitted) == contexts[("L", crt(s, w))],
PY|                     "symbol_routing")
PY|
PY|    check_symbols(3)
PY|    routes = {}
PY|    block_pairs = {}
PY|    pair_counts = {"R": 0, "C": 0, "L": 0}
PY|    for key, block in blocks.items():
PY|        pairs = tuple(frozenset(pair) for pair in combinations(sorted(block), 2))
PY|        block_pairs[key] = pairs
PY|        for pair in pairs:
PY|            shared = frozenset(label for label, group in contexts.items()
PY|                               if pair <= group)
PY|            need(len(shared) == 1, "block_pair")
PY|            need(pair not in routes, "duplicate_block_pair")
PY|            routes[pair] = shared
PY|            pair_counts[next(iter(shared))[0]] += 1
PY|    need(len(routes) == 90, "block_pair_count")
PY|    need(pair_counts == {"R": 30, "C": 30, "L": 30}, "pair_family_counts")
PY|
PY|    rows, rowmap, families = [], {}, []
PY|    for family in ("R", "C", "L"):
PY|        for residue in range(5):
PY|            first = contexts[(family, crt(residue, 0))]
PY|            second = contexts[(family, crt(residue, 1))]
PY|            need(not first & second, "paired_context_disjointness")
PY|            joined = first | second
PY|            counts = [len(blocks[key] & joined) for key in keys]
PY|            need(len(joined) == 12, "paired_context_size")
PY|            need(all(count in (0, 4) for count in counts), "whole_block_union")
PY|            coefficient = tuple(F(int(count == 4)) for count in counts)
PY|            need(sum(coefficient) == 3, "three_blocks")
PY|            need(sum(coefficient) - 2 == 1, "derived_rhs")
PY|            rows.append(coefficient)
PY|            families.append(family)
PY|            rowmap[(family, residue)] = coefficient
PY|    need(len(rows) == 15, "equation_count")
PY|
PY|    def unit(a, d):
PY|        wanted = index[(a % 5, d)]
PY|        return tuple(F(int(k == wanted)) for k in range(15))
PY|
PY|    def row(family, residue):
PY|        return rowmap[(family, residue % 5)]
PY|
PY|    rank = len(rref(rows)[1])
PY|    nullspace = kernel(rows)
PY|    augmented_rank = len(rref([tuple(r) + (F(1),) for r in rows])[1])
PY|    need(rank == augmented_rank == 13, "full_rank")
PY|    need(len(nullspace) == 2, "full_nullity")
PY|    origin = tuple(F(int(d == 4)) for a, d in keys)
PY|    basis_a = tuple(F(int(d == 2) - int(d == 4)) for a, d in keys)
PY|    basis_b = tuple(F(int(d == 3) - int(d == 4)) for a, d in keys)
PY|    need(all(dot(r, origin) == 1 for r in rows), "affine_origin")
PY|    need(all(dot(r, v) == 0 for r in rows for v in (basis_a, basis_b)),
PY|         "constant_difference_basis")
PY|    for vector in nullspace:
PY|        need(all(vector[index[(a, d)]] == vector[index[(0, d)]]
PY|                 for a, d in keys), "nonconstant_mode")
PY|        need(sum(vector[index[(0, d)]] for d in (2, 3, 4)) == 0,
PY|             "constant_sum_constraint")
PY|
PY|    q = {}
PY|    for a in range(5):
PY|        h_difference = linear([(1, unit(a, 4)), (-1, unit(a + 1, 2)),
PY|                               (-1, unit(a - 1, 4)), (1, unit(a, 2))])
PY|        need(h_difference == linear([(1, row("R", a)),
PY|                                     (-1, row("C", a + 3))]), "h_certificate")
PY|        q[a] = linear([(1, row("L", 2 * a + 3)),
PY|                       (1, row("C", a + 4)), (1, row("C", a)),
PY|                       (-1, row("R", a)), (-1, row("R", a + 1)),
PY|                       (-1, row("R", a + 2))])
PY|        need(q[a] == linear([(2, unit(a + 3, 2)), (-1, unit(a, 2)),
PY|                             (-1, unit(a + 1, 2))]), "q_certificate")
PY|    for a in range(5):
PY|        certificate = linear([(F(1, 5), q[(a + 1) % 5]),
PY|                              (F(-3, 5), q[(a + 2) % 5]),
PY|                              (F(3, 5), q[(a + 3) % 5]),
PY|                              (F(-1, 5), q[(a + 4) % 5])])
PY|        need(certificate == linear([(1, unit(a + 1, 2)),
PY|                                    (-1, unit(a, 2))]), "constancy_certificate")
PY|
PY|    family_mutants = {}
PY|    for omitted in ("R", "C", "L"):
PY|        retained = [r for r, family in zip(rows, families) if family != omitted]
PY|        mutant_rank = len(rref(retained)[1])
PY|        mutant_kernel = kernel(retained)
PY|        need(mutant_rank == 9 and len(mutant_kernel) == 6, "family_mutant_rank")
PY|        witnesses = [v for v in mutant_kernel
PY|                     if any(v[index[(a, d)]] != v[index[(0, d)]]
PY|                            for a, d in keys)]
PY|        need(bool(witnesses), "family_mutant_nonconstant_witness")
PY|        witness = witnesses[0]
PY|        need(all(dot(r, witness) == 0 for r in retained), "mutant_kernel")
PY|        need(any(dot(r, witness) != 0 for r in rows), "mutant_detected_by_full")
PY|        family_mutants[omitted] = (mutant_rank, len(mutant_kernel), witness)
PY|
PY|    def check_support(candidate):
PY|        need(candidate == cells, "support")
PY|
PY|    reversed_cells = frozenset((r, c) for r in range(10) for c in range(10)
PY|                               if (r - c) % 10 in delta)
PY|    need(len(reversed_cells) == 60, "reversed_count_control")
PY|    expect("support", lambda: check_support(reversed_cells))
PY|    expect("crt_parity", lambda: check_routes(lambda a, u: a + 5 * u))
PY|    expect("symbol_routing", lambda: check_symbols(1))
PY|
PY|    def check_block_pairs(pairs, allowed):
PY|        for pair in pairs:
PY|            need(len(routes[pair] & allowed) == 1, "block_pair")
PY|
PY|    omission_cases = 0
PY|    allowed = frozenset(contexts)
PY|    for key, pairs in block_pairs.items():
PY|        required = frozenset().union(*(routes[pair] for pair in pairs))
PY|        need(len(required) == 6, "block_required_context_count")
PY|        for omitted in required:
PY|            reduced_allowed = allowed - {omitted}
PY|            need(sum(not (routes[pair] & reduced_allowed) for pair in pairs) == 1,
PY|                 "one_pair_lost")
PY|            expect("block_pair",
PY|                   lambda: check_block_pairs(pairs, reduced_allowed))
PY|            omission_cases += 1
PY|    need(omission_cases == 90, "omission_case_count")
PY|
PY|    off_diagonal_certificates = 0
PY|    for i in range(3):
PY|        for j in range(3):
PY|            for k in range(3):
PY|                if j == k:
PY|                    continue
PY|                ej, ek = ("e", j), ("e", k)
PY|                if i == j or i == k:
PY|                    terms = [(1, (ej, ("t", i), ek))]
PY|                else:
PY|                    terms = [(1, (ej, ek)),
PY|                             (-1, (ej, ("t", j), ek)),
PY|                             (-1, (ej, ("t", k), ek))]
PY|                need(not normal(terms), "partition_commutation_certificate")
PY|                off_diagonal_certificates += 1
PY|    need(off_diagonal_certificates == 18, "partition_certificate_count")
PY|
PY|    orthogonality = frozenset(frozenset(pair)
PY|                              for pair in combinations(range(4), 2))
PY|    for u in range(2):
PY|        for v in range(2):
PY|            need(not product_residual(u, v, orthogonality), "ray_intersection")
PY|    weakened_orthogonality_cases = 0
PY|    for omitted in orthogonality:
PY|        weakened = orthogonality - {omitted}
PY|        need(any(product_residual(u, v, weakened)
PY|                 for u in range(2) for v in range(2)),
PY|             "missing_orthogonality_not_detected")
PY|        weakened_orthogonality_cases += 1
PY|    need(weakened_orthogonality_cases == 6, "orthogonality_mutant_count")
PY|
PY|    plane = {(0, 0): F(1), (1, 1): F(1)}
PY|    sector = {(0, 0): F(1)}
PY|    ray = {(i, j): F(1, 2) for i in range(2) for j in range(2)}
PY|    need(matrix_product(plane, plane) == plane, "plane_projection")
PY|    need(matrix_product(sector, sector) == sector, "sector_projection")
PY|    need(matrix_product(ray, ray) == ray, "ray_projection")
PY|    need(ray[(0, 0)] + ray[(1, 1)] == 1, "ray_rank_one_trace")
PY|    need(ray[(0, 1)] == ray[(1, 0)], "ray_hermitian")
PY|    need(not commutator(plane, sector), "plane_commutes")
PY|    need(commutator(ray, sector) == {(1, 0): F(1, 2), (0, 1): F(-1, 2)},
PY|         "plane_only_mutant")
PY|
PY|    separated_pairs = 0
PY|    for qcell in cells:
PY|        row_others = contexts[("R", qcell[0])] - {qcell}
PY|        column_others = contexts[("C", qcell[1])] - {qcell}
PY|        for x in row_others:
PY|            for y in column_others:
PY|                need(x != y, "row_column_partner_cells")
PY|                separated_pairs += 1
PY|    need(separated_pairs == 1500, "partner_separation_count")
PY|    consume_repetition(True)
PY|    expect("nonparallel_required", lambda: consume_repetition(False))
PY|    tick()
PY|    return {
PY|        "cells": len(cells),
PY|        "contexts": len(contexts),
PY|        "memberships": 180,
PY|        "blocks": len(blocks),
PY|        "block_pairs": len(routes),
PY|        "pair_family_counts": pair_counts,
PY|        "scalar_rank": rank,
PY|        "augmented_rank": augmented_rank,
PY|        "scalar_nullity": len(nullspace),
PY|        "affine_origin": origin,
PY|        "difference_basis": (basis_a, basis_b),
PY|        "family_mutants": family_mutants,
PY|        "row_span_certificates": 15,
PY|        "physical_context_omissions": omission_cases,
PY|        "partition_certificates": off_diagonal_certificates,
PY|        "ray_product_certificates": 4,
PY|        "orthogonality_omissions": weakened_orthogonality_cases,
PY|        "partner_cell_separations": separated_pairs,
PY|        "scope": "FINITE_AND_FORMAL_INTERFACES_ONLY"
PY|    }
PY|
PY|RESULTS = run()

END COMPLETE SOURCE

## 10. Disposition and remaining acceptance boundaries

**Overall correctness: correct on the assigned interfaces.** The actual-cell routing supports all thirty required contexts; their paired equations have scalar rank 13 and exclude all nonconstant modes. The two operator interfaces—three-partition commutation and recovery of an individual ray as a row-plane/column-plane product—have universal algebraic proofs, not merely selected numerical support.

**Confidence: 0.97 for the written interface conclusions.** The checker is independently authored but unexecuted; no execution confidence or PASS receipt is asserted.

This return supplies:

- Complete physical routing and counts.
- Exact rational rank/nullspace conclusions with explicit row-span certificates.
- Universal proofs of the two named algebraic interfaces.
- Full reproducible checker source and exact proposed argv.
- Meaningful negative controls and their precise limitations.

It does **not** supply:

- An executed finite-check receipt.
- A sixty-ray or hundred-ray witness.
- An exhaustive search over complex vectors.
- A new unrestricted hundred-ray impossibility theorem.
- A contradiction of the standalone forty-ray construction.
- Adoption of the full f535 theorem or its affine-orbit consequence.
- Human, kernel, independent-family, novelty, or priority clearance.

The checker’s execution remains unperformed. Complete-theorem acceptance and parent disposition remain separate from this FINITE interface return.