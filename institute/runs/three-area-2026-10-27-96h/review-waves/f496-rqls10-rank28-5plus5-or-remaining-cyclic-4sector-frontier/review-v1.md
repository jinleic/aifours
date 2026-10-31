# f496 — Explicit complex realization of the remaining two-antipodal-pair four-sector support

**GENERAL AUTHOR CANDIDATE — UNREVIEWED.**

## 1. Result and original-target status

I obtain an explicit family of **40 pairwise nonparallel unit vectors in \(\mathbb C^4\)** on the cyclic support
\[
S=\{0,1,5,6\},\qquad H_S=\{(r,c):c-r\in S\pmod {10}\}.
\]
Every restricted row, column and cyclic resolution class is an orthonormal basis of \(\mathbb C^4\). The construction covers the entire ten-mask affine orbit of \(S\) by cell relabeling, without any covariance assumption on the rays.

Thus this orbit does not merely survive incidence and zero-pattern tests: **its four-dimensional subsystem is physically realizable with all 40 rays distinct.** A contradiction confined to those four-dimensional orthogonality requirements cannot exclude it.

This is **not a 100-ray solution**. The remaining obligation is exactly the existence or impossibility of 60 pairwise nonparallel vectors in \(\mathbb C^6\) on the complementary support, with all thirty restricted contexts orthonormal. No such six-dimensional array is supplied here. The rank-28 \(5+5\) branch and the other residual four-support orbit are not decided.

The delivered outcome is the permitted corrected theorem/feasibility result, not the requested full-target closure.

## 2. Input boundary, chronology and execution status

Before scientific derivation I read:

1. The frozen manifest, freeze receipt and parent metadata supply.
2. All ten permission/status controls completely, including their endings.
3. I sent the direct pre-body ACK.
4. The complete 194-LF literal packet in consecutive raw ranges of at most twenty LF, through its ending.

The frozen metadata is **parent-supplied**, not independently executed by me:

- Manifest SHA-256: `275f1a62a49847f4f5aff90a21f3fd2b5f944f46ba18c63da28f376db98746e2`.
- Receipt SHA-256: `4548b38930d07ef0be971e22e835873ecaba1b223bbc34198846ebed08e71d75`.
- Packet SHA-256: `130efd9aa18b7daf2e5cc15895831cbfdfc1f75324856176252fa433045c1673`.
- The supplied clock observation is attributable to Main only. I made no native clock/hash execution claim.

After the complete packet read, I developed the block/observable construction below and selected the displayed exact angles as fresh general-author research. Public searches and a partial read of Alex Arkhipov, *Extending and Characterizing Quantum Magic Games*, [arXiv:1209.3819v1](https://arxiv.org/html/1209.3819v1), supplied background about commuting-observable parity arrangements. **No theorem from that paper is needed in the proof below.** This was not a complete literature or novelty review.

All held payloads and their consumers remained NONINPUT; their links were not followed.

**Scientific execution: NOTRUN.** Active runtime restrictions prohibit scientific shell execution and filesystem edits in this role. I did not bypass them. The full exact checker is returned in Section 10; its prospective output is not represented as observed output. No file-write refusal or successful materialization is claimed.

## 3. Coordinates and the forty selected cells

Use Chinese-remainder coordinates
\[
r\longleftrightarrow(a,u)=(r\bmod5,r\bmod2),\qquad
c\longleftrightarrow(b,v)=(c\bmod5,c\bmod2).
\]
The inverse is
\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2),\qquad 0\le a<5,\quad u\in\{0,1\}.
\]

Membership in \(H_S\) is equivalent to
\[
b-a\in\{0,1\}\pmod5.
\]
Accordingly define ten four-cell blocks:
\[
A_a=\{((a,u),(a,v)):u,v\in\{0,1\}\},
\]
\[
B_a=\{((a,u),(a+1,v)):u,v\in\{0,1\}\}.
\]

All indices \(a\) are modulo five. The restricted contexts are:

- Row \((a,u)\): the two \(A_a\)-cells and two \(B_a\)-cells with that \(u\).
- Column \((b,v)\): the two \(A_b\)-cells and two \(B_{b-1}\)-cells with that \(v\).
- Symbol \((s,w)\), meaning \(r+c=(s,w)\): put \(a=3s\pmod5\). Its cells are the two \(A_a\)-cells and two \(B_{a+2}\)-cells with \(u+v=w\pmod2\).

These formulas specify all ten contexts of each type, not a subset.

## 4. Explicit four-component vectors

Let
\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]
and
\[
N(\theta)=\cos\theta\,Z+\sin\theta\,X.
\]

Set
\[
\theta_1=0,\qquad
\theta_2=\frac{\pi}{4},\qquad
\theta_3=\frac{\pi}{8},\qquad
\theta_4=\frac{3\pi}{8},
\]
and \(N_i=N(\theta_i)\) for \(1\le i\le4\).

Define five two-dimensional unitaries:
\[
\begin{aligned}
U_0&=I,\\
U_1&=-Z,\\
U_2&=-e^{-iY\pi/4},\\
U_3&=N(-\pi/8),\\
U_4&=-iY.
\end{aligned}
\]
Equivalently, they obey
\[
U_i=(-1)^iN_iU_{i-1}\quad(1\le i\le4).
\]

For \(\epsilon\in\{+1,-1\}\), define unit vectors
\[
w_0^\epsilon=\frac1{\sqrt2}(1,\epsilon i)^T.
\]
For \(1\le i\le4\), define
\[
w_i^+=
\begin{pmatrix}\cos(\theta_i/2)\\ \sin(\theta_i/2)\end{pmatrix},
\qquad
w_i^-=
\begin{pmatrix}-\sin(\theta_i/2)\\ \cos(\theta_i/2)\end{pmatrix}.
\]
Thus \(Yw_0^\epsilon=\epsilon w_0^\epsilon\), and
\(N_iw_i^\epsilon=\epsilon w_i^\epsilon\).

The following are explicit vectors in \(\mathbb C^2\oplus\mathbb C^2\):
\[
Q_i^{\mathsf U}(\epsilon,\eta)
=\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\]
\[
Q_i^{\mathsf V}(\epsilon,\eta)
=\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
-i(-1)^i\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\qquad \epsilon,\eta\in\{+1,-1\}.
\]

Use this complete block lookup:

| Block | \(i\) | Branch |
|---|---:|---|
| \(A_0\) | 0 | \(\mathsf U\) |
| \(A_1\) | 3 | \(\mathsf V\) |
| \(A_2\) | 1 | \(\mathsf V\) |
| \(A_3\) | 4 | \(\mathsf U\) |
| \(A_4\) | 2 | \(\mathsf U\) |
| \(B_0\) | 4 | \(\mathsf V\) |
| \(B_1\) | 2 | \(\mathsf V\) |
| \(B_2\) | 0 | \(\mathsf V\) |
| \(B_3\) | 3 | \(\mathsf U\) |
| \(B_4\) | 1 | \(\mathsf U\) |

For each of the four cells of \(A_a\), assign
\[
q_{A_a;u,v}
=
Q_i^{\text{branch}}\bigl((-1)^{u+v},\,(-1)^v\bigr).
\]
For each of the four cells of \(B_a\), assign
\[
q_{B_a;u,v}
=
Q_i^{\text{branch}}\bigl(-(-1)^{u+v},\,-(-1)^u\bigr).
\]

This is a closed formula for every one of the forty vectors; there are no remaining parameters or implicit equation-solving steps.

## 5. Exact operator certificate

The following certificate proves all thirty ONB claims.

For a two-dimensional unitary \(U\), write
\[
T(U)=
\begin{pmatrix}0&U\\U^\dagger&0\end{pmatrix},
\qquad
J(U)=T(iU).
\]
Define
\[
t_i=T(U_i),\qquad b_i=(-1)^iJ(U_i).
\]
Define
\[
g_0=\operatorname{diag}(Y,Y),
\]
and, for \(1\le i\le4\),
\[
g_i=
\operatorname{diag}\bigl(N_i,\ U_{i-1}^\dagger N_iU_{i-1}\bigr).
\]

All \(g_i,t_i,b_i\) are Hermitian involutions with two \(+1\) and two \(-1\) eigenvalues. For \(1\le i\le4\),
\[
t_i=(-1)^ig_it_{i-1},\qquad
b_i=-(-1)^ig_ib_{i-1}.
\]
The factors in each displayed product commute.

The only closing calculation required is
\[
N_4N_3=N_2N_1=e^{-iY\pi/4},
\]
so
\[
U_4=N_4N_3N_2N_1=-iY.
\]
Consequently
\[
b_4=g_0t_0,\qquad b_0t_4=-g_0.
\]
These identities establish the closing vertices as well as the four recurrence vertices.

The four \(Q_i^{\mathsf U}\) are the joint eigenbasis of \((g_i,t_i)\), with eigenvalues \((\epsilon,\eta)\). The four \(Q_i^{\mathsf V}\) are the joint eigenbasis of \((g_i,b_i)\), with the same eigenvalue labels.

Now name the shared row, column and symbol observables:

| \(a\) | \(R_a\) | \(C_a\) | \(D_a\) |
|---:|---|---|---|
| 0 | \(b_4\) | \(t_0\) | \(g_0\) |
| 1 | \(b_2\) | \(b_3\) | \(g_3\) |
| 2 | \(b_0\) | \(b_1\) | \(g_1\) |
| 3 | \(t_3\) | \(t_4\) | \(g_4\) |
| 4 | \(t_1\) | \(t_2\) | \(g_2\) |

At block \(A_a\), the commuting triple is
\[
(R_a,C_a,D_a),\qquad R_aC_aD_a=I.
\]
At block \(B_a\), it is
\[
(R_a,C_{a+1},D_{a-2}),\qquad
R_aC_{a+1}D_{a-2}=-I.
\]

These statements follow directly from the recurrences and the two closing identities. They also identify the eigenvalues of the assigned cell vectors:

| Block | Row observable | Column observable | Symbol observable |
|---|---|---|---|
| \(A_a;u,v\) | \((-1)^u\) | \((-1)^v\) | \((-1)^{u+v}\) |
| \(B_a;u,v\) | \(-(-1)^u\) | \(-(-1)^v\) | \(-(-1)^{u+v}\) |

The observables in the second row are \(R_a,C_{a+1},D_{a-2}\), respectively.

## 6. Proof of every restricted context

Each block is an ONB, since it is a joint eigenbasis of two commuting independent Hermitian involutions.

For a fixed row \((a,u)\):

- Its two \(A_a\)-vectors form an ONB of the two-dimensional \(R_a=(-1)^u\) eigenspace.
- Its two \(B_a\)-vectors form an ONB of the complementary \(R_a=-(-1)^u\) eigenspace.

Their union is therefore an ONB of \(\mathbb C^4\).

For a fixed column \((b,v)\):

- Its two \(A_b\)-vectors occupy \(C_b=(-1)^v\).
- Its two \(B_{b-1}\)-vectors occupy \(C_b=-(-1)^v\).

Again these are complementary two-dimensional eigenspaces.

For a symbol \((s,w)\), put \(a=3s\pmod5\):

- The two relevant \(A_a\)-vectors occupy \(D_a=(-1)^w\).
- The two relevant \(B_{a+2}\)-vectors occupy \(D_a=-(-1)^w\), because \(D_{(a+2)-2}=D_a\).

This proves all ten symbol contexts. These arguments quantify over every row, column and symbol and use exact complex orthogonality.

## 7. Proof that all forty rays are different

Every displayed vector has a nonzero first two-component block proportional to \(w_i^\epsilon\).

For different \(i\), those first-block rays cannot coincide. Their Bloch axes are
\[
Y,\quad Z,\quad N(\pi/4),\quad N(\pi/8),\quad N(3\pi/8),
\]
which are pairwise different even up to sign. Therefore their two-element eigenray sets are disjoint.

For a fixed \(i\):

- Different \(\epsilon\) give orthogonal first-block rays.
- For fixed \(\epsilon\), the two \(\mathsf U\)-vectors have relative lower-block multipliers \(+1,-1\).
- The two \(\mathsf V\)-vectors have relative lower-block multipliers \(+i,-i\), in some order.

Because both component blocks are nonzero, none of these four multipliers produces the same ray as another. There are eight distinct rays per \(i\), hence forty globally distinct rays.

No numerical tolerance or generic-parameter assertion is involved.

## 8. Entire orbit and exact remaining original obligation

For every unit \(h\in\{1,3,7,9\}\) and \(t\in\mathbb Z_{10}\), the relabeling
\[
(r,c)\longmapsto(hr,hc+t)
\]
preserves rows, columns and cyclic symbol classes, up to permutation, and sends \(H_S\) to \(H_{hS+t}\). Transporting the vector assignment therefore realizes every support in the affine orbit.

The orbit consists exactly of the ten choices of two antipodal pairs. This follows either from the frozen input’s orbit classification or directly: translation normalizes the first antipodal pair, and an odd unit normalizes the nonzero difference modulo five of the second pair.

For a fixed support in this orbit, the following equivalence now holds:

> A full orthogonal \(4+6\) realization with that support exists if and only if its complementary sixty cells admit sixty pairwise nonparallel rays in \(\mathbb C^6\), with each of the thirty restricted contexts an ONB.

Necessity is sector restriction. For sufficiency, take the orthogonal direct sum of this forty-ray construction and any such sixty-ray construction. Each full context is then a ten-element ONB. Rays on opposite sides of the orthogonal sum cannot be parallel.

The **first unpaid step** is therefore precisely that sixty-ray, thirty-context complex-vector problem. In CRT coordinates its support is
\[
b-a\in\{2,3,4\}\pmod5.
\]
No necessary incidence selector is substituted for those vectors.

A further elementary restriction is available: a two-dimensional sector is impossible under global nonparallelness. A row and column through one selected cell would give two two-element ONBs sharing that ray; their other rays would necessarily be parallel at distinct cells. Together with the frozen cyclic even-sector theorem, this rules out splitting a putative six-dimensional complement into smaller orthogonal sectors. It does not construct or exclude the required irreducible six-dimensional array.

## 9. Evidence classification and exclusions

- **AUTHOR written construction/proof:** Sections 3–8.
- **Executed scientific calculation:** none.
- **Exact finite checker:** complete source below, **NOTRUN**.
- **100-ray witness:** not supplied.
- **Full-target no-go:** not supplied.
- **Rank-28 \(5+5\):** unchanged.
- **Other surviving four-support orbit:** unchanged.
- **Disjoint review / parent adoption:** not performed here.
- **Independent-family, human, formal/kernel or novelty credit:** none.

No source status or earlier acceptance label substitutes for the new proof.

## 10. Complete prospective exact checker — NOTRUN

Companion filename: `f496-four-sector-exact.py`.

The source is rendered as numbered plain-text lines. Removing only each initial `NNN|` recovers the complete Python source. It uses standard-library arithmetic in \(\mathbb Q(\zeta_{32})\), represented modulo \(\zeta_{32}^{16}+1\), and has a cooperative 55-second deadline. It checks forty vectors, all thirty restricted contexts and all 780 distinct pairs. It also prints the exact vector coefficients and complete context lists. **No stdout or successful run is claimed.**

001|from fractions import Fraction as F
002|from itertools import combinations, product
003|from time import monotonic
004|
005|START = monotonic()
006|
007|def budget():
008|    if monotonic() - START >= 55:
009|        raise SystemExit("NOT_COMPLETED_TIME_LIMIT")
010|
011|class E:
012|    def __init__(self, value=0):
013|        if isinstance(value, E):
014|            self.c = value.c
015|        elif isinstance(value, (tuple, list)):
016|            if len(value) != 16:
017|                raise ValueError("Expected 16 field coefficients")
018|            self.c = tuple(F(x) for x in value)
019|        else:
020|            self.c = (F(value),) + (F(0),) * 15
021|
022|    def __add__(self, other):
023|        other = E(other)
024|        return E(tuple(a + b for a, b in zip(self.c, other.c)))
025|
026|    __radd__ = __add__
027|
028|    def __neg__(self):
029|        return E(tuple(-a for a in self.c))
030|
031|    def __sub__(self, other):
032|        return self + (-E(other))
033|
034|    def __rsub__(self, other):
035|        return E(other) + (-self)
036|
037|    def __mul__(self, other):
038|        budget()
039|        other = E(other)
040|        out = [F(0)] * 16
041|        for j, a in enumerate(self.c):
042|            if not a:
043|                continue
044|            for k, b in enumerate(other.c):
045|                if not b:
046|                    continue
047|                degree = j + k
048|                if degree < 16:
049|                    out[degree] += a * b
050|                else:
051|                    out[degree - 16] -= a * b
052|        return E(out)
053|
054|    __rmul__ = __mul__
055|
056|    def __eq__(self, other):
057|        return self.c == E(other).c
058|
059|    def bar(self):
060|        out = [F(0)] * 16
061|        out[0] = self.c[0]
062|        for j in range(1, 16):
063|            out[16 - j] -= self.c[j]
064|        return E(out)
065|
066|def zp(k):
067|    k %= 32
068|    out = [F(0)] * 16
069|    out[k % 16] = F(1 if k < 16 else -1)
070|    return E(out)
071|
072|ZERO = E(0)
073|ONE = E(1)
074|IM = zp(8)
075|
076|def cs(k):
077|    return F(1, 2) * (zp(k) + zp(-k))
078|
079|def sn(k):
080|    return F(1, 2) * (-IM) * (zp(k) - zp(-k))
081|
082|H = cs(4)
083|
084|def eye(n):
085|    return tuple(tuple(E(int(i == j)) for j in range(n))
086|                 for i in range(n))
087|
088|def sm(s, A):
089|    return tuple(tuple(s * x for x in row) for row in A)
090|
091|def mm(A, B):
092|    budget()
093|    return tuple(tuple(sum((A[i][k] * B[k][j]
094|                            for k in range(len(B))), ZERO)
095|                       for j in range(len(B[0])))
096|                 for i in range(len(A)))
097|
098|def adj(A):
099|    return tuple(tuple(A[j][i].bar() for j in range(len(A)))
100|                 for i in range(len(A[0])))
101|
102|def mv(A, v):
103|    return tuple(sum((x * y for x, y in zip(row, v)), ZERO)
104|                 for row in A)
105|
106|def vs(s, v):
107|    return tuple(s * x for x in v)
108|
109|def inner(v, w):
110|    return sum((x.bar() * y for x, y in zip(v, w)), ZERO)
111|
112|def diag(A, B):
113|    return tuple(tuple(
114|        A[i][j] if i < 2 and j < 2 else
115|        B[i - 2][j - 2] if i >= 2 and j >= 2 else ZERO
116|        for j in range(4)) for i in range(4))
117|
118|def T(U):
119|    V = adj(U)
120|    return tuple(tuple(
121|        U[i][j - 2] if i < 2 <= j else
122|        V[i - 2][j] if j < 2 <= i else ZERO
123|        for j in range(4)) for i in range(4))
124|
125|def N(k):
126|    return ((cs(k), sn(k)), (sn(k), -cs(k)))
127|
128|I2 = eye(2)
129|I4 = eye(4)
130|Y = ((ZERO, -IM), (IM, ZERO))
131|NN = (Y, N(0), N(4), N(2), N(6))
132|UU = [I2]
133|for j in range(1, 5):
134|    UU.append(sm((-1) ** j, mm(NN[j], UU[-1])))
135|assert UU[4] == sm(-IM, Y)
136|
137|gg = [diag(Y, Y)]
138|for j in range(1, 5):
139|    lower = mm(mm(adj(UU[j - 1]), NN[j]), UU[j - 1])
140|    gg.append(diag(NN[j], lower))
141|tt = [T(U) for U in UU]
142|bb = [sm((-1) ** j, T(sm(IM, U))) for j, U in enumerate(UU)]
143|
144|for M in gg + tt + bb:
145|    assert adj(M) == M
146|    assert mm(M, M) == I4
147|    assert sum((M[j][j] for j in range(4)), ZERO) == ZERO
148|
149|def w(j, eps):
150|    if j == 0:
151|        return (H, H * eps * IM)
152|    k = {1: 0, 2: 2, 3: 1, 4: 3}[j]
153|    if eps == 1:
154|        return (cs(k), sn(k))
155|    return (-sn(k), cs(k))
156|
157|def Q(j, side, eps, eta):
158|    top = w(j, eps)
159|    low = mv(adj(UU[j]), top)
160|    gamma = E(eta) if side == 0 else -IM * ((-1) ** j) * eta
161|    return vs(H, top) + vs(H * gamma, low)
162|
163|R = (bb[4], bb[2], bb[0], tt[3], tt[1])
164|C = (tt[0], bb[3], bb[1], tt[4], tt[2])
165|D = (gg[0], gg[3], gg[1], gg[4], gg[2])
166|AMAP = ((0, 0), (3, 1), (1, 1), (4, 0), (2, 0))
167|BMAP = ((4, 1), (2, 1), (0, 1), (3, 0), (1, 0))
168|
169|def crt(a, bit):
170|    a %= 5
171|    return a + 5 * ((bit - a) % 2)
172|
173|rays = {}
174|for typ, mapping in enumerate((AMAP, BMAP)):
175|    sign = 1 if typ == 0 else -1
176|    for a, (j, side) in enumerate(mapping):
177|        ER = R[a]
178|        EC = C[a if typ == 0 else (a + 1) % 5]
179|        ED = D[a if typ == 0 else (a - 2) % 5]
180|        assert mm(ER, EC) == mm(EC, ER)
181|        assert mm(ER, ED) == mm(ED, ER)
182|        assert mm(EC, ED) == mm(ED, EC)
183|        assert mm(mm(ER, EC), ED) == sm(sign, I4)
184|        for ub, vb in product(range(2), repeat=2):
185|            eps = sign * ((-1) ** (ub + vb))
186|            eta = (-1) ** vb if typ == 0 else -((-1) ** ub)
187|            q = Q(j, side, eps, eta)
188|            cell = (crt(a, ub), crt(a + typ, vb))
189|            assert cell not in rays
190|            rays[cell] = q
191|            assert mv(ER, q) == vs(sign * ((-1) ** ub), q)
192|            assert mv(EC, q) == vs(sign * ((-1) ** vb), q)
193|            assert mv(ED, q) == vs(sign * ((-1) ** (ub + vb)), q)
194|
195|S = frozenset((0, 1, 5, 6))
196|expected = {(r, c) for r in range(10) for c in range(10)
197|            if (c - r) % 10 in S}
198|assert set(rays) == expected
199|assert len(rays) == 40
200|
201|contexts = []
202|for r in range(10):
203|    contexts.append(("R" + str(r),
204|                     tuple(sorted(x for x in rays if x[0] == r))))
205|for c in range(10):
206|    contexts.append(("C" + str(c),
207|                     tuple(sorted(x for x in rays if x[1] == c))))
208|for s in range(10):
209|    contexts.append(("L" + str(s),
210|                     tuple(sorted(x for x in rays
211|                                  if sum(x) % 10 == s))))
212|assert len(contexts) == 30
213|
214|for cell, q in rays.items():
215|    assert inner(q, q) == ONE, cell
216|for name, cells in contexts:
217|    budget()
218|    assert len(cells) == 4, name
219|    for x, y in combinations(cells, 2):
220|        assert inner(rays[x], rays[y]) == ZERO, (name, x, y)
221|
222|for x, y in combinations(sorted(rays), 2):
223|    budget()
224|    z = inner(rays[x], rays[y])
225|    assert z * z.bar() != ONE, ("PARALLEL", x, y)
226|
227|orbit = {frozenset((h * s + t) % 10 for s in S)
228|         for h in (1, 3, 7, 9) for t in range(10)}
229|assert len(orbit) == 10
230|for mask in orbit:
231|    assert all((s + 5) % 10 in mask for s in mask)
232|
233|budget()
234|print("FIELD: Q(zeta_32), zeta_32^16 = -1")
235|print("COEFFICIENT ORDER: 1,zeta_32,...,zeta_32^15")
236|for cell in sorted(rays):
237|    coefficients = tuple(tuple(str(a) for a in x.c) for x in rays[cell])
238|    print("CELL", cell, "COEFFICIENTS", coefficients)
239|for name, cells in contexts:
240|    print("CONTEXT", name, cells)
241|print("AFFINE_SUPPORT_ORBIT", tuple(sorted(tuple(sorted(m)) for m in orbit)))
242|print("RESULT: PASS_40_RAY_PARTIAL_ARRAY_ONLY")
243|print("NO_C6_EXTENSION_SUPPLIED; NO_100_RAY_WITNESS; NO_GLOBAL_CLOSURE")
244|print("ELAPSED_MONOTONIC_SECONDS", monotonic() - START)

**End of complete author return.**