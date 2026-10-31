# author-candidate-v1.md — FINITE return

**Status: written exact derivation; independent checker supplied but NOTRUN.** The admissible Bell example falsifies the manuscript’s ancillary orbit-dimension and irreducibility step. **It does not falsify Proposition 4’s majorization inequality:** that inequality holds for this example, including every required partial sum.

This is the complete body for Main materialization. No working-tree file was written.

## 1. Inputs, chronology, and verification boundary

The frozen identifiers used were:

- Manifest: `6feac13ed8c2764f2107328e447f821f8f2b56abc5ee20a60695f9c0411d15eb`.
- Freeze receipt: `de3e31f203cbce2a9dc45e87d18258e10bbab4e38aef45cece74245ab3482c89`.
- Packet, as reported by the parent receipt: `cb998ed7bb982c8e444607c651e44a55f294cb555d5c1cadc0af1e9ac6902e7a`.

I read the complete manifest and receipt, all seven listed status/permission controls, the parent metadata and dispatch records, and then the complete ordered packet, including S1 lines 1–44 and S2 lines 1–33 and their endings. The hashes and clocks above are **parent-supplied metadata, not child-native hash or clock observations**.

After the packet, I directly read the public manuscript. One raw-HTML ranged request returned portions of §§2–3 rather than the intended rendered §6; I then used the rendered source artifact and separately read the complete long paragraph containing the disputed inference. The relevant directly inspected material was:

- [Amosov, arXiv:2103.08515v6, §4, equations (10)–(12)](https://arxiv.org/html/2103.08515v6#S4): projective multiplication, cocycles, and phase changes.
- [§5, equations (14)–(16)](https://arxiv.org/html/2103.08515v6#S5): mixed-unitary channel, coset sums, and cross-coset ordering.
- [§6, Propositions 1 and 4, and Proposition 4’s complete proof](https://arxiv.org/html/2103.08515v6#S6).

The derivation below was made after exposure to S1’s selected example. It is therefore **not a blind discovery claim**. The checker was derived here from matrix definitions; no parent or sibling program was read or imported. Held scientific payloads and their consumers were not followed or used.

**Execution boundary:** the role’s tools prohibit executing Python or other scientific programs and prohibit file edits. The frozen task explicitly permits a NOTRUN return under that restriction. Accordingly, there was no scientific execution, timing measurement, memory measurement, executed mutation test, interpreter-hash observation, or program-hash observation. All numerical expressions below are exact written calculations, not reported machine output.

## 2. Exact issue in the primary manuscript

In §6, Proposition 4’s proof defines

\[
L=\operatorname{span}\{(I_K\otimes U_g)f:g\in G\}
\]

for an arbitrary unit vector \(f\in K\otimes H\). After asserting linear independence of the \(n^2\) matrices \(U_g\), it states **“Hence dim \(L=n\)”** and asserts that the action restricted to \(L\) is irreducible.

Linear independence of the matrices does not imply that dimension for an entangled vector. In the explicit admissible instance below, those matrices form a basis of \(M_2(\mathbb C)\), but the four orbit vectors are orthonormal. Thus \(\dim L=4\), whereas \(n=2\).

This identifies an invalid intermediate inference in the inspected public manuscript. It does not establish that a subscription journal version contains identical text.

## 3. Verification of the actual representation hypotheses

Set \(H=K=\mathbb C^2\), \(G=\mathbb Z_2^2\), and order its elements as \((0,0),(0,1),(1,0),(1,1)\). Define

\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
J=XZ=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

All four are unitary. In particular, \(J^*=-J\) and \(J^2=-I\), so \(J^*J=I\).

For \(g=(a,b)\), put \(U_g=X^aZ^b\). Direct multiplication gives

\[
U_{(a,b)}U_{(c,d)}
=(-1)^{bc}U_{(a\oplus c,b\oplus d)}.
\]

The complete product table is:

| Left \ Right | \(I\) | \(Z\) | \(X\) | \(J\) |
|---|---|---|---|---|
| \(I\) | \(I\) | \(Z\) | \(X\) | \(J\) |
| \(Z\) | \(Z\) | \(I\) | \(-J\) | \(-X\) |
| \(X\) | \(X\) | \(J\) | \(I\) | \(Z\) |
| \(J\) | \(J\) | \(X\) | \(-Z\) | \(-I\) |

The multiplier \(\omega(g,h)=(-1)^{bc}\) satisfies the cocycle identity: both sides have exponent \(bc+be+de\) modulo two when \(h=(c,d)\) and the third element is \((e,f)\).

Take \(T=\{(0,0),(0,1)\}\). It is normal and Abelian, and \(|G/T|=2=\dim H\). Its restriction is the **ordinary** representation \(\{I,Z\}\), because \(Z^2=I\) and the multiplier is one on \(T\times T\).

### Irreducibility, checked by exact linear constraints

Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) commute with every \(U_g\).

- \(AZ=ZA\) implies \(b=c=0\).
- \(AX=XA\) then implies \(a=d\).

Thus the commutant is precisely \(\mathbb C I\). For a unitary representation, an invariant subspace has an invariant orthogonal complement, so its orthogonal projection belongs to the commutant. There is no proper nonzero such projection. The projective representation on \(H\) is irreducible.

### Linear independence

\[
aI+bZ+cX+dJ
=
\begin{pmatrix}a+b&c-d\\c+d&a-b\end{pmatrix}.
\]

If this is zero, all four coefficients vanish. Hence \(I,Z,X,J\) form a basis of \(M_2(\mathbb C)\). The checker encodes both this rank-four condition and the rank-three homogeneous commutator constraint system.

## 4. Direct orbit vectors and exact Gram matrices

Use computational order \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\).

### Product control

For \(f_P=|00\rangle\), the orbit vectors in the stated group order are

\[
|00\rangle,\quad |00\rangle,\quad |01\rangle,\quad |01\rangle.
\]

Their Gram matrix is

\[
G_P=
\begin{pmatrix}
1&1&0&0\\
1&1&0&0\\
0&0&1&1\\
0&0&1&1
\end{pmatrix},
\qquad \operatorname{rank}G_P=2.
\]

Here the orbit span is \(|0\rangle\otimes H\), so its dimension is indeed \(n=2\).

### Bell counterexample to the proof step

For \(f_B=(|00\rangle+|11\rangle)/\sqrt2\), the four orbit vectors are

\[
\begin{aligned}
b_I&=(|00\rangle+|11\rangle)/\sqrt2,\\
b_Z&=(|00\rangle-|11\rangle)/\sqrt2,\\
b_X&=(|01\rangle+|10\rangle)/\sqrt2,\\
b_J&=(|01\rangle-|10\rangle)/\sqrt2.
\end{aligned}
\]

Their normalized Gram matrix is exactly \(G_B=I_4\). Therefore

\[
\dim L_B=\operatorname{rank}G_B=4\ne2.
\]

On this full four-dimensional orbit span, both \(|0\rangle\otimes H\) and \(|1\rangle\otimes H\) are invariant. The action is the direct sum of two equivalent copies of the original irreducible action, not an irreducible four-dimensional action.

### Correct dimension under the matrix-span hypothesis

More generally, suppose the \(U_g\) span \(\operatorname{End}(H)\), and write a Schmidt decomposition

\[
f=\sum_{i=1}^{r}s_i e_i\otimes h_i,\qquad s_i>0.
\]

For any prescribed \(y_1,\ldots,y_r\in H\), a linear operator \(A\) can be chosen with \(Ah_i=y_i/s_i\). Consequently,

\[
\operatorname{span}\{(I\otimes A)f:A\in\operatorname{End}(H)\}
=\operatorname{span}\{e_1,\ldots,e_r\}\otimes H.
\]

Thus \(\dim L=nr\), and the action is \(r\) copies of the action on \(H\). The source’s dimension and irreducibility conclusion holds in this setting only when the Schmidt rank is one.

## 5. Physical channel, actual pure-output \(q\), and exact outputs

To avoid confusing the source’s coset-distribution notation with a noise parameter, write the depolarizing noise as \(\eta\in[0,1]\). Use

\[
w(\eta)=\left(1-\frac{3\eta}{4},\frac{\eta}{4},
\frac{\eta}{4},\frac{\eta}{4}\right).
\]

These weights are nonnegative and sum to one. They define a completely positive, trace-preserving mixed-unitary channel

\[
\Phi_\eta(A)=\sum_g w_g(\eta)U_g A U_g^*.
\]

The two cosets are \(\{I,Z\}\) and \(\{X,J\}\). Their sums are \(1-\eta/2\) and \(\eta/2\). Every weight in the latter coset is at most every weight in the former because \(\eta/4\le1-3\eta/4\). Hence the cross-coset ordering in source equation (16) also holds.

Direct matrix multiplication, equivalently checking the four matrix units, gives

\[
\sum_g U_g A U_g^*=2\operatorname{Tr}(A)I,
\qquad
\Phi_\eta(A)=(1-\eta)A+\frac{\eta}{2}\operatorname{Tr}(A)I.
\]

For **every complex unit vector** \(e\), not merely a selected real test vector,

\[
\Phi_\eta(|e\rangle\langle e|)
=(1-\eta)|e\rangle\langle e|+\frac{\eta}{2}I.
\]

Its actual spectrum is therefore

\[
q(\eta)=(1-\eta/2,\eta/2).
\]

Thus \(q\) is obtained from the channel’s genuine pure outputs; it is not a fabricated comparison distribution.

The independent bipartite matrix formula is

\[
(\operatorname{id}\otimes\Phi_\eta)(A)
=(1-\eta)A+\frac{\eta}{2}\operatorname{Tr}_H(A)\otimes I.
\]

The checker compares this formula against explicit local matrix conjugations on all sixteen \(4\times4\) matrix units at each selected parameter, in addition to testing the two specified states.

### Required midpoint \(\eta=1/2\)

The weights are \((5/8,1/8,1/8,1/8)\), and \(q=(3/4,1/4)\).

For the product input,

\[
\sigma_P=\operatorname{diag}(3/4,1/4,0,0).
\]

For the Bell input, the direct orbit mixture is

\[
\sigma_B=\sum_g w_g|b_g\rangle\langle b_g|
=
\begin{pmatrix}
3/8&0&0&1/4\\
0&1/8&0&0\\
0&0&1/8&0\\
1/4&0&0&3/8
\end{pmatrix}.
\]

It has trace one and the complete orthonormal eigenbasis \((b_I,b_Z,b_X,b_J)\), with spectrum

\[
\mu_B=(5/8,1/8,1/8,1/8).
\]

Every eigenvalue is positive. The independent matrix-channel formula gives

\[
\sigma_B=\tfrac12|f_B\rangle\langle f_B|+\tfrac18 I_4,
\]

which is exactly the same matrix.

Every majorization partial sum is:

| \(k\) | Bell sum \(\sum_{j=1}^k\mu_j^\downarrow\) | Sum for \(q\oplus(0,0)\) | Slack |
|---|---:|---:|---:|
| 1 | \(5/8\) | \(3/4\) | \(1/8\) |
| 2 | \(3/4\) | \(1\) | \(1/4\) |
| 3 | \(7/8\) | \(1\) | \(1/8\) |
| 4 | \(1\) | \(1\) | \(0\) |

### Endpoint controls and the complete Bell noise family

For every \(\eta\in[0,1]\), the Bell spectrum is the already sorted vector \(w(\eta)\). Against \(q(\eta)\oplus(0,0)\), its four partial-sum slacks are

\[
(\eta/4,\eta/2,\eta/4,0).
\]

In particular:

| \(\eta\) | Product spectrum | Bell spectrum | Bell slacks |
|---|---|---|---|
| \(0\) | \((1,0,0,0)\) | \((1,0,0,0)\) | \((0,0,0,0)\) |
| \(1/2\) | \((3/4,1/4,0,0)\) | \((5/8,1/8,1/8,1/8)\) | \((1/8,1/4,1/8,0)\) |
| \(1\) | \((1/2,1/2,0,0)\) | \((1/4,1/4,1/4,1/4)\) | \((1/4,1/2,1/4,0)\) |

The Bell **orbit** rank remains four at \(\eta=0\), even though the channel output then has rank one. Orbit rank and weighted-mixture rank must not be conflated.

## 6. Intended-reason controls

These are exact written consequences and implemented controls, **not executed test results**.

| Control | Required rejection or acceptance |
|---|---|
| Assert normalized Bell orbit Gram rank two | Reject with `orbit_rank`; its rank is four. |
| Ignore all projective signs | Reject with `product_rule`; \(ZX=-J\), not \(J\). |
| Replace \(J\) with a duplicate \(X\) | Reject with `projective_product`; \(ZX\) is not either sign of the matrix assigned to \((1,1)\). |
| Weights \((1/2,1/8,1/8,1/8)\) | Reject with `trace`; output trace is \(7/8\). |
| Weights \((5/8,0,1/4,1/8)\) | Accept as a physical mixture, then reject with `coset_order`; the later-coset weight \(1/4\) exceeds the earlier-coset weight zero. |
| Substitute comparison vector \((1/2,1/2,0,0)\) | Reject with `majorization`; \(5/8>1/2\) at \(k=1\). |
| Substitute partial transpose for a local channel output | Reject with `positivity`, while trace remains one. |
| Gauge change \(J\mapsto-J\) | **Accept** projective closure with the adjusted cocycle and accept identical channel output. A legitimate phase change is not a physical counterexample. |

For the partial-transpose control, \(\sigma_B^{T_H}\) has middle block

\[
\begin{pmatrix}1/8&1/4\\1/4&1/8\end{pmatrix}.
\]

Its determinant is \(-3/64\), and its antisymmetric eigenvector has eigenvalue \(-1/8\). This distinguishes the mistaken operation using positivity, not an unrelated exception.

No Gaussian-complex selected example is needed here. The implemented matrices and examples are real and exactly rational. The analytic pure-output argument above covers complex unit vectors; the checker is not described as a general complex-arithmetic implementation.

## 7. Complete independent standard-library checker — NOTRUN

**Invocation specification:** argv is `("python3", "-I", "-S", "-B", "-c", PROGRAM)`, where `PROGRAM` is exactly the source below. It has no explicit file or network I/O, subprocesses, installation, random inputs, or background work. Its largest matrices are \(4\times4\); positivity is checked using all nonempty principal minors. A cooperative 50-second deadline is included. Actual runtime and memory use remain unmeasured.

To preserve the no-code-block output restriction, each inline span between BEGIN_PROGRAM and END_PROGRAM is one source line. Concatenate them with LF, removing only the enclosing backticks.

BEGIN_PROGRAM

`from fractions import Fraction as F`  
`from itertools import combinations, permutations, product`  
`from time import monotonic`  
`DEADLINE = monotonic() + 50`  
`class AuditError(Exception):`  
`    def __init__(self, tag, detail=""):`  
`        self.tag = tag`  
`        super().__init__(tag + ": " + detail)`  
`def need(condition, tag, detail=""):`  
`    if monotonic() > DEADLINE:`  
`        raise AuditError("deadline", "cooperative 50-second bound")`  
`    if not condition:`  
`        raise AuditError(tag, detail)`  
`def mat(rows):`  
`    return [[F(x) for x in row] for row in rows]`  
`def eye(n):`  
`    return [[F(i == j) for j in range(n)] for i in range(n)]`  
`def unit(n, i, j):`  
`    return [[F(a == i and b == j) for b in range(n)] for a in range(n)]`  
`def transpose(A):`  
`    return [list(row) for row in zip(*A)]`  
`def flat(A):`  
`    return [x for row in A for x in row]`  
`def scale(t, A):`  
`    return [[F(t) * x for x in row] for row in A]`  
`def add(A, B):`  
`    return [[x + y for x, y in zip(a, b)] for a, b in zip(A, B)]`  
`def mm(A, B):`  
`    cols = transpose(B)`  
`    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in cols] for row in A]`  
`def mv(A, v):`  
`    return tuple(sum((x * y for x, y in zip(row, v)), F(0)) for row in A)`  
`def dot(v, w):`  
`    return sum((x * y for x, y in zip(v, w)), F(0))`  
`def outer(v):`  
`    return [[x * y for y in v] for x in v]`  
`def rho(v):`  
`    return scale(1 / dot(v, v), outer(v))`  
`def trace(A):`  
`    return sum((A[i][i] for i in range(len(A))), F(0))`  
`def diag(values):`  
`    return [[values[i] if i == j else F(0) for j in range(len(values))] for i in range(len(values))]`  
`def kron(A, B):`  
`    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))] for i in range(len(A)) for k in range(len(B))]`  
`def rank(A):`  
`    a = mat(A)`  
`    r = 0`  
`    for c in range(len(a[0])):`  
`        if r == len(a):`  
`            break`  
`        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)`  
`        if pivot is None:`  
`            continue`  
`        a[r], a[pivot] = a[pivot], a[r]`  
`        divisor = a[r][c]`  
`        a[r] = [x / divisor for x in a[r]]`  
`        for i in range(len(a)):`  
`            if i != r and a[i][c]:`  
`                factor = a[i][c]`  
`                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]`  
`        r += 1`  
`    return r`  
`def determinant(A):`  
`    n = len(A)`  
`    answer = F(0)`  
`    for perm in permutations(range(n)):`  
`        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))`  
`        term = F((-1) ** inversions)`  
`        for i, j in enumerate(perm):`  
`            term *= A[i][j]`  
`        answer += term`  
`    return answer`  
`def state(A):`  
`    need(trace(A) == 1, "trace", str(trace(A)))`  
`    need(A == transpose(A), "hermiticity", "real-matrix checker")`  
`    for size in range(1, len(A) + 1):`  
`        for indices in combinations(range(len(A)), size):`  
`            minor = [[A[i][j] for j in indices] for i in indices]`  
`            need(determinant(minor) >= 0, "positivity", str(indices))`  
`def gram(vectors, norm_squared):`  
`    return [[dot(v, w) / norm_squared for w in vectors] for v in vectors]`  
`I = eye(2)`  
`OPS = [I, mat([[1, 0], [0, -1]]), mat([[0, 1], [1, 0]]), mat([[0, -1], [1, 0]])]`  
`G = tuple(range(4))`  
`T = (0, 1)`  
`def projective(ops):`  
`    need(ops[0] == I, "identity")`  
`    for A in ops:`  
`        need(mm(transpose(A), A) == I, "unitarity")`  
`    omega = {}`  
`    for i, j in product(G, repeat=2):`  
`        actual = mm(ops[i], ops[j])`  
`        target = ops[i ^ j]`  
`        if actual == target:`  
`            omega[i, j] = 1`  
`        elif actual == scale(-1, target):`  
`            omega[i, j] = -1`  
`        else:`  
`            raise AuditError("projective_product", str((i, j)))`  
`    for i, j, k in product(G, repeat=3):`  
`        need(omega[i, j] * omega[i ^ j, k] == omega[i, j ^ k] * omega[j, k], "cocycle")`  
`    for i, j in product(T, repeat=2):`  
`        need(omega[i, j] == 1, "ordinary_T")`  
`    return omega`  
`def product_rule(ops, omega):`  
`    for i, j in product(G, repeat=2):`  
`        need(mm(ops[i], ops[j]) == scale(omega[i, j], ops[i ^ j]), "product_rule", str((i, j)))`  
`def check_weights(w):`  
`    need(len(w) == 4 and sum(w, F(0)) == 1 and all(x >= 0 for x in w), "weights")`  
`def cosets(w):`  
`    check_weights(w)`  
`    need(w[0] + w[1] >= w[2] + w[3], "coset_order")`  
`    need(all(w[j] <= w[i] for i in (0, 1) for j in (2, 3)), "coset_order")`  
`def weights(eta):`  
`    need(0 <= eta <= 1, "noise_range")`  
`    return (1 - 3 * eta / 4, eta / 4, eta / 4, eta / 4)`  
`def mix(A, w, ops):`  
`    local_ops = ops if len(A) == 2 else [kron(I, U) for U in ops]`  
`    answer = scale(0, A)`  
`    for weight, U in zip(w, local_ops):`  
`        answer = add(answer, scale(weight, mm(mm(U, A), transpose(U))))`  
`    return answer`  
`def partial_trace_H(A):`  
`    return [[sum((A[2 * a + h][2 * b + h] for h in range(2)), F(0)) for b in range(2)] for a in range(2)]`  
`def channel_formula(A, eta):`  
`    if len(A) == 2:`  
`        noise = scale(eta * trace(A) / 2, I)`  
`    else:`  
`        noise = scale(eta / 2, kron(partial_trace_H(A), I))`  
`    return add(scale(1 - eta, A), noise)`  
`def partial_transpose_H(A):`  
`    return [[A[2 * (i // 2) + j % 2][2 * (j // 2) + i % 2] for j in range(4)] for i in range(4)]`  
`def majorized(a, b):`  
`    a, b = tuple(sorted(a, reverse=True)), tuple(sorted(b, reverse=True))`  
`    need(len(a) == len(b) and sum(a, F(0)) == sum(b, F(0)) == 1, "majorization")`  
`    need(all(x >= 0 for x in a + b), "majorization")`  
`    slacks = tuple(sum(b[:k], F(0)) - sum(a[:k], F(0)) for k in range(1, len(a) + 1))`  
`    need(all(x >= 0 for x in slacks), "majorization", str(slacks))`  
`    return slacks`  
`def reject(label, expected_tag, operation):`  
`    try:`  
`        operation()`  
`    except AuditError as exc:`  
`        need(exc.tag == expected_tag, "wrong_rejection", label + ": " + str(exc))`  
`        print("REJECT", label, expected_tag)`  
`    else:`  
`        raise AuditError("missed_mutation", label)`  
`omega = projective(OPS)`  
`canonical = {(i, j): (-1) ** ((i & 1) * ((j >> 1) & 1)) for i, j in product(G, repeat=2)}`  
`product_rule(OPS, canonical)`  
`need(omega == canonical, "canonical_cocycle")`  
`need({i ^ j for i in T for j in T} == set(T), "subgroup")`  
`need(all((g ^ t ^ g) in T for g in G for t in T), "normal_subgroup")`  
`need(set(T).isdisjoint({2 ^ t for t in T}) and set(T) | {2 ^ t for t in T} == set(G), "coset_partition")`  
`need(rank([flat(U) for U in OPS]) == 4, "operator_basis")`  
`need(len({tuple(flat(scale(s, U))) for s in (-1, 1) for U in OPS}) == 8, "signed_group")`  
`units2 = [unit(2, i, j) for i, j in product(range(2), repeat=2)]`  
`constraints = []`  
`for U in OPS:`  
`    columns = [flat(add(mm(E, U), scale(-1, mm(U, E)))) for E in units2]`  
`    constraints.extend(transpose(columns))`  
`need(rank(constraints) == 3, "commutant_dimension")`  
`need(all(mm(I, U) == mm(U, I) for U in OPS), "commutant_identity")`  
`vP = tuple(map(F, (1, 0, 0, 0)))`  
`vB = tuple(map(F, (1, 0, 0, 1)))`  
`VP = [mv(kron(I, U), vP) for U in OPS]`  
`VB = [mv(kron(I, U), vB) for U in OPS]`  
`GP, GB = gram(VP, F(1)), gram(VB, F(2))`  
`need(GP == mat([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]), "product_gram")`  
`need(GB == eye(4), "bell_gram")`  
`need(rank(GP) == rank(VP) == 2, "product_orbit_rank")`  
`need(rank(GB) == rank(VB) == 4, "bell_orbit_rank")`  
`rP, rB = rho(vP), rho(vB)`  
`state(rP)`  
`state(rB)`  
`need(rank(rP) == rank(rB) == 1, "pure_inputs")`  
`print("CHECKED group, cocycle, ordinary T, operator basis, and scalar commutant")`  
`print("Product normalized Gram:", GP)`  
`print("Bell normalized Gram:", GB)`  
`formula_checks = 0`  
`for eta in (F(0), F(1, 2), F(1)):`  
`    w = weights(eta)`  
`    cosets(w)`  
`    for n in (2, 4):`  
`        for i, j in product(range(n), repeat=2):`  
`            E = unit(n, i, j)`  
`            need(mix(E, w, OPS) == channel_formula(E, eta), "matrix_unit_formula", str((eta, n, i, j)))`  
`            formula_checks += 1`  
`    single = mix(unit(2, 0, 0), w, OPS)`  
`    state(single)`  
`    need(single[0][1] == single[1][0] == 0, "actual_q_diagonal")`  
`    q = (single[0][0], single[1][1])`  
`    need(q == (1 - eta / 2, eta / 2), "actual_q")`  
`    qpad = q + (F(0), F(0))`  
`    outP, outB = mix(rP, w, OPS), mix(rB, w, OPS)`  
`    state(outP)`  
`    state(outB)`  
`    need(outP == diag(qpad), "product_output")`  
`    need(outP == channel_formula(rP, eta) and outB == channel_formula(rB, eta), "state_formula")`  
`    for eigenvalue, eigenvector in zip(w, VB):`  
`        need(mv(outB, eigenvector) == tuple(eigenvalue * x for x in eigenvector), "bell_eigenpair")`  
`    need(rank(outP) == (1 if eta == 0 else 2), "product_output_rank")`  
`    need(rank(outB) == (1 if eta == 0 else 4), "bell_output_rank")`  
`    need(majorized(qpad, qpad) == (F(0),) * 4, "product_majorization")`  
`    slacks = majorized(w, qpad)`  
`    need(slacks == (eta / 4, eta / 2, eta / 4, F(0)), "bell_partial_sums")`  
`    print("eta =", eta, "actual q =", q, "product spectrum =", qpad, "Bell spectrum =", w, "Bell slacks =", slacks)`  
`    if eta == F(1, 2):`  
`        print("Bell midpoint output:", outB)`  
`need(formula_checks == 60, "formula_check_count")`  
`mid_weights = weights(F(1, 2))`  
`mid = mix(rB, mid_weights, OPS)`  
`reject("wrong_Bell_orbit_rank_two", "orbit_rank", lambda: need(rank(GB) == 2, "orbit_rank"))`  
`all_plus = {(i, j): 1 for i, j in product(G, repeat=2)}`  
`reject("ignored_projective_signs", "product_rule", lambda: product_rule(OPS, all_plus))`  
`duplicate = OPS[:3] + [OPS[2]]`  
`reject("duplicated_X_in_place_of_XZ", "projective_product", lambda: projective(duplicate))`  
`bad_trace_weights = (F(1, 2), F(1, 8), F(1, 8), F(1, 8))`  
`reject("subnormalized_weights", "trace", lambda: state(mix(rB, bad_trace_weights, OPS)))`  
`bad_coset_weights = (F(5, 8), F(0), F(1, 4), F(1, 8))`  
`check_weights(bad_coset_weights)`  
`state(mix(rB, bad_coset_weights, OPS))`  
`reject("interlaced_coset_weights", "coset_order", lambda: cosets(bad_coset_weights))`  
`wrong_qpad = (F(1, 2), F(1, 2), F(0), F(0))`  
`reject("incorrect_single_output_bound", "majorization", lambda: majorized(mid_weights, wrong_qpad))`  
`pt = partial_transpose_H(mid)`  
`need(trace(pt) == 1, "partial_transpose_trace_control")`  
`need(determinant([[pt[1][1], pt[1][2]], [pt[2][1], pt[2][2]]]) == F(-3, 64), "partial_transpose_minor")`  
`reject("partial_transpose_as_local_channel", "positivity", lambda: state(pt))`  
`gauge = OPS[:3] + [scale(-1, OPS[3])]`  
`projective(gauge)`  
`need(rank([flat(U) for U in gauge]) == 4, "gauge_operator_basis")`  
`need(mix(rB, mid_weights, gauge) == mid, "gauge_channel_invariance")`  
`print("ACCEPT legitimate sign-gauge change with adjusted cocycle")`  
`print("All exact checks and intended-reason controls completed.")`

END_PROGRAM

The final printed completion sentence is part of the **unexecuted program**, not a claim that its checks passed here.

## 8. Scope, significance, and remaining gates

**Established by the displayed written calculations:**

1. The example satisfies the actual projective-representation, subgroup, irreducibility, operator-basis, physical-channel, and pure-output comparison assumptions.
2. The product and Bell orbit ranks are respectively two and four.
3. The manuscript’s asserted ancillary orbit dimension and irreducibility fail on the Bell example.
4. The specified Bell output nevertheless satisfies the proposed majorization bound, at every \(k\).
5. The same product/Bell conclusions and comparison hold throughout the displayed depolarizing noise interval, including its endpoints.

**Not established or claimed:**

- A counterexample to Proposition 4, Proposition 5, a general tensor-product majorization theorem, or any capacity conclusion.
- A replacement proof of unrestricted Proposition 4.
- Resolution of the original four-qubit target.
- Identity between the inspected manuscript and a published journal proof.
- Novelty, priority, formal/kernel verification, human acceptance, or independent-model-family review.
- Successful execution of the supplied checker.

Changing the dimension assertion to \(nr\) repairs that dimension statement, but **does not repair the proof’s subsequent identification of the ancillary action/channel with a single copy**. That argument requires separate justification; merely substituting the corrected dimension is insufficient.

The remaining acceptance gates are Main’s independent mathematical review/disposition and, if computational evidence is desired, an actual bounded replay of the supplied program with its bytes, interpreter, argv, observed results, intended rejection reasons, and runtime recorded. These gates have not been self-granted.

**Overall correctness:** correct.

**Explanation:** The frozen candidate correctly identifies a false intermediate orbit-dimension/irreducibility assertion using an admissible physical instance, while correctly preserving the majorization inequality for that instance. The supplied independent checker is NOTRUN, and neither unrestricted theorem falsity nor original-target resolution follows.

**Confidence:** 0.99 for the displayed mathematical assessment; no execution-confidence claim.