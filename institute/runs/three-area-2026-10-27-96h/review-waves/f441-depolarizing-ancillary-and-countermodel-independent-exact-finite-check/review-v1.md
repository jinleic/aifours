# FINITE return — f441

**Execution status: NOTRUN — role-limited.** The higher-priority review role prohibits scientific execution and file edits. I have therefore completed the written adjudication and supplied a fresh, standalone exact checker below, without executing or materializing it. **No finite-test PASS, runtime, exit status, or machine-verification credit is claimed.**

## 1. Input and method receipt

Before reading scientific content, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply, and all seven named permission/quarantine controls. I then read the literal packet **in order, LF 1–734**, including the complete endings of **S1 LF 1–595** and **S2 LF 1–137**.

The identifiers supplied by the parent are:

- Manifest: `1d717b7631dd77dd20fb04358840042c2c4704a2786c7ad1d5d8954573fa06ba`
- Freeze receipt: `68495c83f96201c031b930f6c4efd372bd0dab5ac535e1789e190c01629535df`
- Literal packet: `f4e86cc939d7e48c1425a5de7c756545fe0069b33c71ebf8ee3008291818ca75`
- S1: `84fb421b024feb5a296de66212323357703672c96487a66b0ad67c963fba45ad`
- S2: `e5ea40f15d472862bc9219e76fcbfc472382a0de758643c0828fec3033168b00`

These hashes and the recorded clock are **parent-attributed observations**, not child-native recomputations.

The PH/v8/cp116, AME/t28, CORE, privacy, L1, and other held payloads and their consumers remained **NONINPUT**. No held scientific payload, sibling return, author program, or sibling program was opened. The checker was independently written from the displayed definitions **after reading the complete packet**; it is not a blind reconstruction.

The primary-source basis here is the supplied S2 reader excerpt of [Amosov, arXiv:2103.08515v6](https://arxiv.org/html/2103.08515v6), not an independent web visit, original-HTML comparison, or subscription-journal comparison.

## 2. Claimwise adjudication

| Claim | Disposition |
|---|---|
| Depolarizing one-leg ancillary majorization, full CP interval | **The written proof is valid.** |
| Extension to mixed inputs | **Valid:** the proof uses positivity and trace one, not purity. |
| Negative-\(t\) branch and endpoints | **Valid with the stated decreasing rearrangement.** |
| Universal ancillary orbit dimension \(d\) | **False:** the Bell orbit has dimension four for \(d=2\). |
| Genuine same-Pauli-orbit/common-projector countermodel | **Valid as exact written algebra.** |
| Ordering, twirl, row bounds, and conjugated-state Ky Fan bounds suffice for tensorization | **False as a standalone implication.** |
| The displayed \(R\) is admissible under the proposition’s \(\Omega\)-output hypothesis | **False:** its conditional output violates a necessary constraint. |
| Counterexample to full Proposition 5 | **Not supplied.** |
| Refutation of Proposition 4’s inequality | **Not supplied.** |
| General group-channel Proposition 4 | **Not adjudicated.** |
| Unrestricted tensor-product/four-qubit claim | **Neither proved nor refuted.** |
| Executed independent finite verification | **NOTRUN.** |
| Novelty, priority, cross-family/human/kernel verification | **Not established.** |

### 2.1 Independent reconstruction of the one-leg proof

Write
\[
t=1-p,\qquad b=p/d,\qquad
R=t\rho+b\rho_A\otimes I_d.
\]
The normalized Choi eigenvalues are \(t+p/d^2\) and \(p/d^2\), so \(R\ge0\) and \(\operatorname{Tr}R=1\) throughout \(0\le p\le d^2/(d^2-1)\).

A useful exact certificate is
\[
R\le \mu I+C,\qquad C\ge0,
\]
which implies, for every rank-\(k\) orthogonal projector,
\[
\operatorname{Tr}(PR)\le k\mu+\operatorname{Tr}C.
\]

For \(k<d\):

- If \(t\ge0\), take \(\mu=b,\ C=t\rho\). The slack is
  \[
  bI+t\rho-R=b(I-\rho_A\otimes I_d)\ge0.
  \]
  The bound is \(kb+t\).
- If \(t<0\), take \(\mu=b,\ C=0\). The slack is
  \[
  bI-R=b(I-\rho_A\otimes I_d)-t\rho\ge0.
  \]
  The bound is \(kb\).

For \(k\ge d\), take \(\mu=0,\ C=R\), giving the bound one.

These are exactly the prefixes of
\[
q^\downarrow=
\begin{cases}
(t+b,b,\ldots,b),&t\ge0,\\
(b,\ldots,b,t+b),&t<0,
\end{cases}
\]
padded by zeros. This also explains precisely why the negative branch must be sorted. Product pure inputs attain the reference. No disputed orbit assertion is used.

### 2.2 Independent reconstruction of the countermodel

In the specified basis, the actual matrices are
\[
R=
\begin{pmatrix}
2/3&0&0&0\\
0&1/4&\sqrt3/12&0\\
0&\sqrt3/12&1/12&0\\
0&0&0&0
\end{pmatrix},
\quad
Q=
\begin{pmatrix}
1&0&0&0\\
0&3/4&\sqrt3/4&0\\
0&\sqrt3/4&1/4&0\\
0&0&0&0
\end{pmatrix}.
\]
Their orthogonal-projector decompositions establish \(\lambda(R)=(2/3,1/3,0,0)\) and that \(Q\) is an orthogonal rank-two projector.

The genuine conjugations by \(I,Z,X,XZ\) on the **first** tensor leg give:

| Consuming vector | \(I\) | \(Z\) | \(X\) | \(XZ\) |
|---|---:|---:|---:|---:|
| \(|00\rangle\) | \(2/3\) | \(2/3\) | \(1/12\) | \(1/12\) |
| \(v\) | \(1/3\) | \(1/12\) | \(1/6\) | \(1/6\) |
| Same \(Q\) | \(1\) | \(3/4\) | \(1/4\) | \(1/4\) |

The marginal is \(\sigma=\operatorname{diag}(3/4,1/4)\), and the orbit sum is exactly \(2I\otimes\sigma\). Unitary conjugation preserves the orthogonal-projector decomposition of \(R\), so the stated conjugated-state Ky Fan inequalities hold for **every** consuming projector, not just this \(Q\).

The physical Pauli channel with weights \((5/8,1/8,1/8,1/8)\) is \(\mathcal D_{1/2,2}\). Applying its actual matrix-unit map on the first leg gives
\[
Y=\frac1{48}
\begin{pmatrix}
25&0&0&0\\
0&9&2\sqrt3&0\\
0&2\sqrt3&11&0\\
0&0&0&3
\end{pmatrix}.
\]
The **same** \(Q\) consumes this \(Y\):
\[
\operatorname{Tr}(QY)=\frac{25}{32}>
\frac34=K_2\!\left((3/4,1/4)^{\otimes2}\right).
\]
The central \(2\times2\) block, multiplied by 48, has trace 20 and determinant 87, yielding the stated roots \(10\pm\sqrt{13}\). No floating-point eigenvalue calculation is necessary.

### 2.3 Admissibility is essential

For any actual intermediate state
\[
R=(\operatorname{id}\otimes\Omega)(|f\rangle\langle f|),
\]
conditioning on an ancilla vector gives
\[
C_a=\Omega(|f_a\rangle\langle f_a|),\qquad
w_a=\operatorname{Tr}C_a=\|f_a\|^2.
\]
Thus the pure-output hypothesis necessarily gives \(\lambda(C_a)\prec w_aq\).

Here,
\[
C_1=\operatorname{diag}(1/12,0),\qquad w_1=1/12,
\]
but
\[
\lambda_{\max}(C_1)=1/12> w_1(3/4)=1/16.
\]
After correct normalization, \(C_1/w_1\) is pure. Therefore **no channel satisfying the prescribed pure-output bound can generate this \(R\) from a pure bipartite input**. This obstruction already applies without imposing the additional mixed-unitary requirement.

The false proof implication and the truth or falsity of the full theorem are consequently separate questions.

## 3. Complete independent checker — unexecuted source

**Invocation:** executable `python3`; arguments `-I`, `-B`, `-c`, followed by the exact source argument below. It is also standalone Python source.

The source uses only `fractions` and `time`; all scientific arithmetic is exact in \(\mathbb Q(\sqrt3,i)\). It contains no explicit file access, network access, subprocess, installation, deletion, paid call, or model CLI. Its cooperative deadline is 50 seconds, checked throughout the bounded computations; **the actual runtime has not been observed**.

It covers:

- Actual Pauli superoperators on every qubit matrix unit.
- Actual \(R,Q,v\), both marginals, orbit, table, twirl, and \(Y\).
- Physical pure-output reconstruction of \(q\) and sorted \(q\otimes q\).
- The conditional admissibility rejection.
- Bell-orbit orthogonality.
- **30 one-leg finite cases:** \(d=2,3\), three inputs each, positive/negative parameters and endpoints; including genuinely mixed complex densities.
- Exact Choi positivity and exact PSD prefix certificates.
- **10 targeted mutations**, each required to fail for its designated reason.

The following is an inline source payload, not an execution receipt:

`exec("import time\nfrom fractions import Fraction as F\n\nSTOP = time.monotonic() + 50\n\ndef tick():\n    if time.monotonic() > STOP:\n        raise RuntimeError('time cap: NOT CERTIFIED')\n\nclass ExactFailure(Exception):\n    pass\n\ndef need(ok, tag):\n    if not ok:\n        raise ExactFailure(tag)\n\nclass E:\n    __slots__ = ('a', 'b', 'c', 'd')\n    def __init__(self, a=0, b=0, c=0, d=0):\n        self.a, self.b, self.c, self.d = map(F, (a, b, c, d))\n    def __add__(self, x):\n        x = e(x)\n        return E(self.a+x.a, self.b+x.b, self.c+x.c, self.d+x.d)\n    __radd__ = __add__\n    def __neg__(self):\n        return E(-self.a, -self.b, -self.c, -self.d)\n    def __sub__(self, x):\n        return self + (-e(x))\n    def __rsub__(self, x):\n        return e(x) + (-self)\n    def __mul__(self, x):\n        x = e(x)\n        a,b,c,d = self.a,self.b,self.c,self.d\n        u,v,w,z = x.a,x.b,x.c,x.d\n        return E(a*u+3*b*v-c*w-3*d*z,\n                 a*v+b*u-c*z-d*w,\n                 a*w+3*b*z+c*u+3*d*v,\n                 a*z+b*w+c*v+d*u)\n    __rmul__ = __mul__\n    def conj(self):\n        return E(self.a, self.b, -self.c, -self.d)\n    def __truediv__(self, x):\n        x = e(x)\n        n = x*x.conj()\n        den = n.a*n.a - 3*n.b*n.b\n        if not den:\n            raise ZeroDivisionError('exact field division by zero')\n        return self*x.conj()*E(n.a/den, -n.b/den)\n    def __rtruediv__(self, x):\n        return e(x)/self\n    def __eq__(self, x):\n        x = e(x)\n        return (self.a,self.b,self.c,self.d) == (x.a,x.b,x.c,x.d)\n    def __bool__(self):\n        return bool(self.a or self.b or self.c or self.d)\n\ndef e(x):\n    return x if isinstance(x, E) else E(x)\n\ndef sign(x):\n    x = e(x)\n    need(not x.c and not x.d, 'nonreal comparison')\n    a,b = x.a,x.b\n    sa = (a > 0) - (a < 0)\n    sb = (b > 0) - (b < 0)\n    if not b:\n        return sa\n    if not a:\n        return sb\n    if sa == sb:\n        return sa\n    z = a*a - 3*b*b\n    return sa*((z > 0) - (z < 0))\n\ndef zero(r, c=None):\n    c = r if c is None else c\n    return [[E() for j in range(c)] for i in range(r)]\n\ndef eye(n):\n    A = zero(n)\n    for i in range(n):\n        A[i][i] = E(1)\n    return A\n\ndef diag(xs):\n    A = zero(len(xs))\n    for i,x in enumerate(xs):\n        A[i][i] = e(x)\n    return A\n\ndef unit(n, j):\n    return [E(int(i == j)) for i in range(n)]\n\ndef matrix_unit(n, i, j):\n    A = zero(n)\n    A[i][j] = E(1)\n    return A\n\ndef dag(A):\n    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]\n\ndef add(A, B):\n    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(A,B)]\n\ndef scale(x, A):\n    x = e(x)\n    return [[x*y for y in row] for row in A]\n\ndef sub(A, B):\n    return add(A, scale(-1, B))\n\ndef mm(A, B):\n    tick()\n    C = zero(len(A), len(B[0]))\n    for i in range(len(A)):\n        for k in range(len(B)):\n            if A[i][k]:\n                for j in range(len(B[0])):\n                    C[i][j] = C[i][j] + A[i][k]*B[k][j]\n    return C\n\ndef tr(A):\n    return sum((A[i][i] for i in range(len(A))), E())\n\ndef outer(v):\n    v = [e(x) for x in v]\n    return [[x*y.conj() for y in v] for x in v]\n\ndef act(A, v):\n    return [sum((A[i][j]*e(v[j]) for j in range(len(v))), E()) for i in range(len(A))]\n\ndef inner(v, w):\n    return sum((e(x).conj()*e(y) for x,y in zip(v,w)), E())\n\ndef value(v, A):\n    return inner(v, act(A,v))\n\ndef kron(A, B):\n    return [[A[i][j]*B[r][s] for j in range(len(A[0])) for s in range(len(B[0]))]\n            for i in range(len(A)) for r in range(len(B))]\n\ndef sum_mats(items):\n    C = zero(len(items[0]), len(items[0][0]))\n    for A in items:\n        C = add(C,A)\n    return C\n\ndef conjugate(U, A):\n    return mm(mm(U,A),dag(U))\n\ndef psd(A):\n    tick()\n    n = len(A)\n    if any(len(row) != n for row in A) or A != dag(A):\n        return False\n    H = [row[:] for row in A]\n    for k in range(n):\n        tick()\n        q = H[k][k]\n        if q.c or q.d or sign(q) < 0:\n            return False\n        if not q:\n            if any(H[k][j] for j in range(k+1,n)):\n                return False\n            continue\n        for i in range(k+1,n):\n            for j in range(k+1,n):\n                H[i][j] = H[i][j] - H[i][k]*H[k][j]/q\n    return True\n\ndef state(A, tag):\n    need(A == dag(A) and tr(A) == 1 and psd(A), tag)\n\ndef projector(A, rank, tag):\n    need(A == dag(A) and mm(A,A) == A and tr(A) == rank and psd(A), tag)\n\ndef marginal_a(A, a, d):\n    return [[sum((A[i*d+r][j*d+r] for r in range(d)), E()) for j in range(a)] for i in range(a)]\n\ndef marginal_b(A, a, d):\n    return [[sum((A[i*d+r][i*d+s] for i in range(a)), E()) for s in range(d)] for r in range(d)]\n\ndef conditional(A, a, d, i):\n    return [[A[i*d+r][i*d+s] for s in range(d)] for r in range(d)]\n\ndef dep_unit(d, i, j, p):\n    p = F(p)\n    A = scale(1-p, matrix_unit(d,i,j))\n    return add(A, scale(p/d,eye(d))) if i == j else A\n\ndef apply_leg(A, a, d, p, leg):\n    tick()\n    need(leg in (0,1), 'invalid tensor leg')\n    n = a*d\n    need(len(A) == n and all(len(row) == n for row in A), 'tensor shape')\n    dim = a if leg == 0 else d\n    maps = {(i,j): dep_unit(dim,i,j,p) for i in range(dim) for j in range(dim)}\n    C = zero(n)\n    for i in range(a):\n        tick()\n        for j in range(a):\n            for r in range(d):\n                for s in range(d):\n                    c = A[i*d+r][j*d+s]\n                    if not c:\n                        continue\n                    if leg == 0:\n                        B = maps[i,j]\n                        for u in range(a):\n                            for v in range(a):\n                                C[u*d+r][v*d+s] = C[u*d+r][v*d+s] + c*B[u][v]\n                    else:\n                        B = maps[r,s]\n                        for u in range(d):\n                            for v in range(d):\n                                C[i*d+u][j*d+v] = C[i*d+u][j*d+v] + c*B[u][v]\n    return C\n\ndef psi(d):\n    if d == 2:\n        return [E(F(3,5)), E(0,0,F(4,5))]\n    need(d == 3, 'unsupported example dimension')\n    return [E(F(1,3)), E(0,0,F(2,3)), E(F(2,3))]\n\ndef physical_q(d, p):\n    p = F(p)\n    P = outer(psi(d))\n    projector(P,1,'single-input projector')\n    B = apply_leg(P,1,d,p,1)\n    b = p/d\n    alpha = 1-p+b\n    expected = add(scale(alpha,P),scale(b,sub(eye(d),P)))\n    need(B == expected, 'physical pure-output decomposition')\n    state(B,'physical pure-output state')\n    return sorted([alpha]+[b]*(d-1), reverse=True)\n\ndef majorized(xs, ys):\n    xs,ys = sorted(xs,reverse=True),sorted(ys,reverse=True)\n    return len(xs) == len(ys) and sum(xs) == sum(ys) and all(sum(xs[:k]) <= sum(ys[:k]) for k in range(1,len(xs)+1))\n\ndef check_choi(d, p):\n    p = F(p)\n    need(0 <= p <= F(d*d,d*d-1), 'CP parameter interval')\n    w = [E(int(i == j)) for i in range(d) for j in range(d)]\n    J = scale(F(1,d),outer(w))\n    projector(J,1,'maximally entangled projector')\n    C = apply_leg(J,d,d,p,1)\n    need(C == add(scale(1-p,J),scale(p/(d*d),eye(d*d))), 'Choi matrix-unit identity')\n    need(p/(d*d) >= 0 and 1-p+p/(d*d) >= 0, 'Choi scalar eigenvalues')\n    state(C,'exact Choi positivity')\n\ndef prefix_certificates(A, d, p, q):\n    p = F(p)\n    n = 2*d\n    state(A,'ancillary input density')\n    MA = marginal_a(A,2,d)\n    state(MA,'ancillary marginal density')\n    need(psd(sub(eye(2),MA)), 'marginal upper bound')\n    R = apply_leg(A,2,d,p,1)\n    t,b = 1-p,p/d\n    need(R == add(scale(t,A),scale(b,kron(MA,eye(d)))), 'ancillary matrix-unit map')\n    state(R,'ancillary output density')\n    ref = q+[F(0)]*(n-d)\n    small_C = scale(t,A) if t >= 0 else zero(n)\n    for k in range(1,n+1):\n        tick()\n        C,mu = (small_C,b) if k < d else (R,F(0))\n        slack = sub(add(scale(mu,eye(n)),C),R)\n        need(psd(C) and psd(slack), 'exact Ky Fan PSD certificate')\n        need(E(k*mu)+tr(C) == E(sum(ref[:k])), 'sorted reference prefix')\n\ndef check_examples():\n    count = 0\n    for d,params in ((2,(F(0),F(1,2),F(1),F(7,6),F(4,3))),\n                     (3,(F(0),F(1,2),F(1),F(17,16),F(9,8)))):\n        P = outer(psi(d))\n        product = kron(outer(unit(2,0)),P)\n        other = kron(outer(unit(2,1)),P)\n        v = [E() for i in range(2*d)]\n        if d == 2:\n            v[0],v[3] = E(F(3,5)),E(0,0,F(4,5))\n        else:\n            v[0],v[4],v[5] = E(F(1,3)),E(0,0,F(2,3)),E(F(2,3))\n        entangled = outer(v)\n        projector(entangled,1,'entangled input projector')\n        mixed = add(scale(F(2,5),entangled),scale(F(3,5),other))\n        state(mixed,'mixed complex input density')\n        need(sign(E(1)-tr(mm(mixed,mixed))) > 0, 'genuinely mixed input')\n        need(any(x.c or x.d for row in mixed for x in row), 'complex input coverage')\n        for p in params:\n            check_choi(d,p)\n            q = physical_q(d,p)\n            for A in (product,entangled,mixed):\n                prefix_certificates(A,d,p,q)\n                count += 1\n    need(count == 30,'finite case count')\n    return count\n\nBAD = 0\n\ndef rejects(label, reason, f):\n    global BAD\n    try:\n        f()\n    except ExactFailure as exc:\n        need(str(exc) == reason, 'wrong mutation reason: '+label)\n        BAD += 1\n    else:\n        raise ExactFailure('mutation not rejected: '+label)\n\ns = E(0,1)\nii = E(0,0,1)\nneed(s*s == 3 and ii*ii == -1, 'field multiplication controls')\nz = E(2,1,1,1)\nneed(z/z == 1 and s.conj() == s and ii.conj() == -ii, 'field inverse/conjugation controls')\nneed(sign(E(2)-s) > 0 and sign(E(1)-s) < 0 and sign(s-E(2)) < 0 and sign(s-E(1)) > 0, 'exact surd sign controls')\nI2 = eye(2)\nZ = diag([1,-1])\nX = [[E(),E(1)],[E(1),E()]]\nUS = [I2,Z,X,mm(X,Z)]\nfor U in US:\n    need(mm(U,dag(U)) == I2 and mm(dag(U),U) == I2, 'Pauli unitarity')\nweights = [F(5,8),F(1,8),F(1,8),F(1,8)]\n\ndef check_weights(w):\n    tag = 'Pauli weight/channel identity'\n    need(sum(w) == 1 and all(x >= 0 for x in w), tag)\n    for i in range(2):\n        for j in range(2):\n            A = matrix_unit(2,i,j)\n            B = sum_mats([scale(w[k],conjugate(US[k],A)) for k in range(4)])\n            need(B == dep_unit(2,i,j,F(1,2)), tag)\n    need(all(w[j] <= w[i] for i in (0,1) for j in (2,3)), tag)\n    need([sum(w[:2]),sum(w[2:])] == [F(3,4),F(1,4)], tag)\n\ncheck_weights(weights)\ne0 = unit(4,0)\nv = [E(),s/2,E(1)/2,E()]\nP0,V = outer(e0),outer(v)\nprojector(P0,1,'first spectral projector')\nprojector(V,1,'second spectral projector')\nneed(mm(P0,V) == zero(4) and inner(e0,v) == 0, 'orthogonal spectral decomposition')\nQ = add(P0,V)\nR = add(scale(F(2,3),P0),scale(F(1,3),V))\nprojector(Q,2,'common rank-two projector')\nstate(R,'countermodel state')\nR_exp = diag([F(2,3),F(1,4),F(1,12),0])\nR_exp[1][2] = R_exp[2][1] = s/12\nneed(R == R_exp,'actual countermodel entries')\nq = physical_q(2,F(1,2))\nneed(q == [F(3,4),F(1,4)], 'physical qubit reference')\nneed(majorized([F(2,3),F(1,3),F(0),F(0)],q+[F(0),F(0)]), 'global spectral bound')\nproducts = sorted([x*y for x in q for y in q],reverse=True)\nneed(products == [F(9,16),F(3,16),F(3,16),F(1,16)], 'sorted physical tensor reference')\nsigma = diag([F(3,4),F(1,4)])\n\ndef check_marginal(S):\n    need(marginal_b(R,2,2) == S,'second-system marginal')\n\ncheck_marginal(sigma)\nneed(marginal_a(R,2,2) == diag([F(11,12),F(1,12)]), 'first-system marginal')\nTABLE = [[F(2,3),F(2,3),F(1,12),F(1,12)],\n         [F(1,3),F(1,12),F(1,6),F(1,6)]]\n\ndef make_orbit(leg=0, correct_adjoint=True):\n    out = []\n    for U in US:\n        W = kron(U,I2) if leg == 0 else kron(I2,U)\n        out.append(mm(mm(W,R),dag(W) if correct_adjoint else W))\n    return out\n\ndef check_orbit(O):\n    for B in O:\n        state(B,'orbit density/conjugation')\n    S = sum_mats(O)\n    need(S == scale(2,kron(I2,sigma)), 'twirl leg/marginal')\n    need(psd(sub(scale(F(3,2),eye(4)),S)), 'sharpened row bound')\n    for r,h in enumerate((e0,v)):\n        for j,B in enumerate(O):\n            need(value(h,B) == TABLE[r][j], 'actual orbit table')\n\ndef check_consumer(C, O):\n    projector(C,2,'consumer projector validity')\n    for j,B in enumerate(O):\n        need(tr(mm(C,B)) == TABLE[0][j]+TABLE[1][j], 'same-projector consumer')\n\nO = make_orbit()\ncheck_orbit(O)\ncheck_consumer(Q,O)\nfor U in US:\n    W = kron(U,I2)\n    need(mm(dag(W),W) == eye(4), 'orbit spectral invariance')\nY = sum_mats([scale(weights[j],O[j]) for j in range(4)])\nneed(Y == apply_leg(R,2,2,F(1,2),0), 'physical first-leg output map')\nY_exp = diag([25,9,11,3])\nY_exp[1][2] = Y_exp[2][1] = 2*s\nY_exp = scale(F(1,48),Y_exp)\nneed(Y == Y_exp,'actual Y entries')\nstate(Y,'actual Y density')\nneed(tr(mm(Q,Y)) == E(F(25,32)), 'same-Q output witness')\nneed(F(25,32) > sum(products[:2]) == F(3,4), 'strict product-prefix violation')\nB = scale(48,[[Y[1][1],Y[1][2]],[Y[2][1],Y[2][2]]])\nneed(tr(B) == 20 and B[0][0]*B[1][1]-B[0][1]*B[1][0] == 87, 'exact Y spectral polynomial')\nneed(mm(B,B) == sub(scale(20,B),scale(87,I2)), 'exact Y block characteristic identity')\nneed(1 < 13 < 49 and 13 < 225, 'Y root ordering and strict prefix gap')\nC1 = conditional(R,2,2,1)\nw1 = tr(C1)\nneed(C1 == diag([F(1,12),0]) and w1 == E(F(1,12)), 'actual conditional block')\nneed(w1*q[0] == E(F(1,16)), 'conditional pure-output cap')\nneed(sign(value(unit(2,0),C1)-w1*q[0]) > 0, 'conditional strict violation')\n\ndef check_conditional(C, w):\n    need(C == conditional(R,2,2,1), 'conditional block normalization')\n    need(e(w) == tr(C), 'conditional trace normalization')\n\ndef require_admissible():\n    C = conditional(R,2,2,1)\n    w = tr(C)\n    check_conditional(C,w)\n    need(psd(sub(scale(w*q[0],I2),C)), 'conditional pure-output admissibility')\n\ncheck_conditional(C1,w1)\nbell_raw = [E(1),E(),E(),E(1)]\nbell_vectors = [act(kron(I2,U),bell_raw) for U in US]\nfor i in range(4):\n    for j in range(4):\n        need(inner(bell_vectors[i],bell_vectors[j]) == E(2 if i == j else 0), 'Bell orbit orthogonality')\nbell_projectors = [scale(F(1,2),outer(h)) for h in bell_vectors]\nfor P in bell_projectors:\n    projector(P,1,'Bell orbit projector')\nneed(sum_mats(bell_projectors) == eye(4), 'Bell orbit full dimension')\nbell_out = sum_mats([scale(weights[j],bell_projectors[j]) for j in range(4)])\nneed(bell_out == apply_leg(bell_projectors[0],2,2,F(1,2),1), 'Bell physical ancillary map')\nneed(majorized(weights,q+[F(0),F(0)]), 'Bell non-refutation spectral bound')\n\ndef wrong_negative_reference():\n    p = F(4,3)\n    A = apply_leg(outer(psi(2)),1,2,p,1)\n    h = [E(F(4,5)),E(0,0,F(-3,5))]\n    need(inner(h,h) == 1 and inner(psi(2),h) == 0, 'negative witness normalization')\n    alpha = 1-p+p/2\n    need(sign(E(alpha)-value(h,A)) >= 0, 'negative sorted prefix')\n\nrejects('wrong Pauli weight','Pauli weight/channel identity',\n        lambda: check_weights([F(1,8),F(5,8),F(1,8),F(1,8)]))\nrejects('missing adjoint','orbit density/conjugation',\n        lambda: check_orbit(make_orbit(0,False)))\nrejects('wrong tensor leg','twirl leg/marginal',\n        lambda: check_orbit(make_orbit(1,True)))\nrejects('stale projector','same-projector consumer',\n        lambda: check_consumer(add(P0,outer(unit(4,1))),O))\nrejects('independent projector','same-projector consumer',\n        lambda: check_consumer(add(P0,outer(unit(4,3))),O))\nrejects('wrong marginal','second-system marginal',\n        lambda: check_marginal(diag([F(1,4),F(3,4)])))\nrejects('normalized block substituted for raw block','conditional block normalization',\n        lambda: check_conditional(scale(12,C1),w1))\nrejects('conditional probability discarded','conditional trace normalization',\n        lambda: check_conditional(C1,E(1)))\nrejects('unsorted negative branch','negative sorted prefix',wrong_negative_reference)\nrejects('false acceptance as Omega output','conditional pure-output admissibility',require_admissible)\nneed(BAD == 10,'mutation count')\nCASES = check_examples()\ntick()\nprint('COUNTERMODEL: exact Pauli orbit, common Q, marginal and Y identities certified')\nprint('CONSUMER: Tr(QY)=25/32 > K2(q tensor q)=3/4')\nprint('ADMISSIBILITY: C1 trace=1/12; largest eigenvalue=1/12 > 1/16; rejected')\nprint('ANCILLARY: '+str(CASES)+' finite cases; d=2,3; positive, negative, endpoints; complex mixed inputs')\nprint('CONTROLS: '+str(BAD)+' intended failures rejected')\nprint('RESULT: PASS (finite identities and certificates only)')\n")`

**Expected behavior, not observed output:** successful execution reaches the six final print statements with case count 30 and intended-rejection count 10. Any wrong rejection reason, unexpected exception, expired deadline, failed identity, or failed PSD certificate prevents that final PASS. The source uses explicit checks rather than optimization-removable assertions.

## 4. Parent disposition boundary

The written mathematics supports the **depolarizing ancillary repair** and the **countermodel to the weakened tensorization implication**. It does not support importing the unrestricted tensorization conclusion.

The returned checker requires an authorized parent execution before receiving finite-verification credit. Parent disposition remains mandatory. This return is same-harness work, not independent-family, human, kernel/formal, novelty, priority, or automatic acceptance evidence.

**Findings:** None against f427’s explicitly qualified written claims. The defects in the older proof are already identified and correctly distinguished from theorem falsity in that candidate.

**Overall correctness:** correct

**Explanation:** The scoped ancillary proof and exact countermodel are mathematically sound, including the conditional-admissibility exclusion. They neither supply an admissible two-channel counterexample nor prove or refute the unrestricted tensor-product claim; the independent checker above remains unexecuted.

**Confidence:** 0.98