# f500 FINITE return — exact local-block census and corrected two-fibre lift

**Proposed body:** `author-candidate-v1.md`  
**Status:** Written mathematical reconstruction completed. Scientific execution **NOT RUN** under this role’s restrictions. The complete prospective checker is supplied below. No file was written.

## 1. Input binding, chronology, and limits

The assignment identifies:

- Manifest SHA-256: `6811b7220ac33c70725ac0f23adf23e990eb7d76debcc25c72dcae70e8c4a920`.
- Freeze-receipt SHA-256: `ba49b71f4e44b5e2fa74623f3ece99fd4937ff91d601ae29a50089ade85efe80`.
- Packet SHA-256, supplied by the parent metadata: `8054242df0c56d4f92a6d6395807607631d950ac1fa7675641b46e41c84816bc`.

These are **parent-supplied bindings**, not child-executed hash observations.

Before displaying the scientific packet, I completely read the manifest, freeze receipt, dispatch receipt, parent-live metadata, and all ten declared controls. I then issued the direct PREBODY ACK. Afterwards I read the packet completely and in order, using raw windows of at most 20 LF:

`1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–216`.

The scientific coverage was exactly:

| ID | Frozen source | Read coverage |
|---|---|---|
| S1 | `f468-parent-boolean-aligned-five-span-canonical-frontier/parent-canonical-five-span-candidate-v1.md` | Complete LF 1–76 |
| S2 | Same directory, `parent-local-lift-original-caller-incompatibility-erratum-v1.md` | Complete LF 1–35 |
| S3 | `f263-nl242-cross-fibre-corrected-normalization/review-v1.md` | Declared LF 1–103 only; not its remaining LF |

A subsequently issued, narrowly scoped `git diff --no-ext-diff` for S2 returned no output. That is not evidence of a tracked patch, source hashing, or scientific execution.

No linked author program, sibling return, undeclared scientific source, or held scientific payload was opened. The controls were used only for status and permissions. No external model, scientific executable, build, test, linter, formatter, installation, network calculation, or filesystem mutation was performed.

The calculations below are **written derivations**, including explicitly assigned finite examples. They are not observed program output.

## 2. Mathematical conclusions

1. All 81 ternary four-point blocks are classified below.
2. Under the stated local meaning of \(H=0\), the named aggregate constraints uniquely force
   \[
   (a,b,c,\mathrm{full}_2,\mathrm{full}_3,\mathrm{empty})
   =(4,6,18,2,1,17).
   \]
3. For the exact eight-inactive-halfblock recipe, all 23 possibilities \(0\le k\le22\) satisfy
   \[
   E_0=48+4k,\qquad Z_3=18+k.
   \]
   None satisfies \(E_0=56\) and \(Z_3=23\) simultaneously.
4. There are valid **single-constraint** examples: \(k=2\) satisfies the energy but has only 20 \(U_3\)-zeros; \(k=5\) satisfies the zero count but has energy 68. It would be false to report absence under either constraint separately.
5. An explicit 256-entry ternary array is constructed below with the corrected census and the complete required \(U_1,U_2\) spectra. Its common graph and phase are verified by symbolic Walsh identities. It is **not an original-target witness**: the remaining four-fibre, balance, rank/eight-zero/\(T\), complementary-\(V\), and odd-fibre requirements are not established.

The census in item 2 is already present in S3 LF 99–103. Neither that census nor the restricted-recipe incompatibility establishes a new whole-branch exclusion.

## 3. Exhaustive classification of all 81 physical blocks

Order \(Q\) as \(0,1,2,3\), with

\[
\chi_1=(1,-1,1,-1),\quad
\chi_2=(1,1,-1,-1),\quad
\chi_3=(1,-1,-1,1).
\]

For \(u=(u_0,u_1,u_2,u_3)\), its unnormalized local Walsh vector is

\[
(U_0,U_1,U_2,U_3)
=(u_0+u_1+u_2+u_3,\;
u_0-u_1+u_2-u_3,\;
u_0+u_1-u_2-u_3,\;
u_0-u_1-u_2+u_3).
\]

The following table lists zero and every nonzero block whose first nonzero entry is \(+1\). **Each nonzero row also represents its negative**, whose entire Walsh vector is negated. Thus the table explicitly covers \(1+2(40)=81\) actual vectors, without identifying distinct blocks.

Tags are:

- \(T\): \(U_1=\pm3\).
- \(A\): magnitude-two pair in slots \((0,2)\).
- \(B\): magnitude-two pair in slots \((0,3)\).
- \(C\): magnitude-two pair in slots \((2,3)\).
- \(F_s\): a single magnitude-four peak in slot \(s\).
- \(O\): empty.
- “Outside”: \(U_1\notin\{0,\pm3\}\).

| Physical block \(u\) | \((U_0,U_1,U_2,U_3)\) | Tag |
|---|---|---|
| \((0,0,0,0)\) | \((0,0,0,0)\) | \(O\) |
| \((1,0,0,0)\) | \((1,1,1,1)\) | Outside |
| \((0,1,0,0)\) | \((1,-1,1,-1)\) | Outside |
| \((0,0,1,0)\) | \((1,1,-1,-1)\) | Outside |
| \((0,0,0,1)\) | \((1,-1,-1,1)\) | Outside |
| \((1,1,0,0)\) | \((2,0,2,0)\) | \(A\) |
| \((1,-1,0,0)\) | \((0,2,0,2)\) | Outside |
| \((1,0,1,0)\) | \((2,2,0,0)\) | Outside |
| \((1,0,-1,0)\) | \((0,0,2,2)\) | \(C\) |
| \((1,0,0,1)\) | \((2,0,0,2)\) | \(B\) |
| \((1,0,0,-1)\) | \((0,2,2,0)\) | Outside |
| \((0,1,1,0)\) | \((2,0,0,-2)\) | \(B\) |
| \((0,1,-1,0)\) | \((0,-2,2,0)\) | Outside |
| \((0,1,0,1)\) | \((2,-2,0,0)\) | Outside |
| \((0,1,0,-1)\) | \((0,0,2,-2)\) | \(C\) |
| \((0,0,1,1)\) | \((2,0,-2,0)\) | \(A\) |
| \((0,0,1,-1)\) | \((0,2,0,-2)\) | Outside |
| \((1,1,1,0)\) | \((3,1,1,-1)\) | Outside |
| \((1,1,-1,0)\) | \((1,-1,3,1)\) | Outside |
| \((1,-1,1,0)\) | \((1,3,-1,1)\) | \(T\) |
| \((1,-1,-1,0)\) | \((-1,1,1,3)\) | Outside |
| \((1,1,0,1)\) | \((3,-1,1,1)\) | Outside |
| \((1,1,0,-1)\) | \((1,1,3,-1)\) | Outside |
| \((1,-1,0,1)\) | \((1,1,-1,3)\) | Outside |
| \((1,-1,0,-1)\) | \((-1,3,1,1)\) | \(T\) |
| \((1,0,1,1)\) | \((3,1,-1,1)\) | Outside |
| \((1,0,1,-1)\) | \((1,3,1,-1)\) | \(T\) |
| \((1,0,-1,1)\) | \((1,-1,1,3)\) | Outside |
| \((1,0,-1,-1)\) | \((-1,1,3,1)\) | Outside |
| \((0,1,1,1)\) | \((3,-1,-1,-1)\) | Outside |
| \((0,1,1,-1)\) | \((1,1,1,-3)\) | Outside |
| \((0,1,-1,1)\) | \((1,-3,1,1)\) | \(T\) |
| \((0,1,-1,-1)\) | \((-1,-1,3,-1)\) | Outside |
| \((1,1,1,1)\) | \((4,0,0,0)\) | \(F_0\), forbidden by \(H=0\) |
| \((1,1,1,-1)\) | \((2,2,2,-2)\) | Outside |
| \((1,1,-1,1)\) | \((2,-2,2,2)\) | Outside |
| \((1,1,-1,-1)\) | \((0,0,4,0)\) | \(F_2\) |
| \((1,-1,1,1)\) | \((2,2,-2,2)\) | Outside |
| \((1,-1,1,-1)\) | \((0,4,0,0)\) | Outside |
| \((1,-1,-1,1)\) | \((0,0,0,4)\) | \(F_3\) |
| \((1,-1,-1,-1)\) | \((-2,2,2,2)\) | Outside |

Checks available directly from this enumeration:

- Support-size counts are \(1,8,24,32,16\) for support \(0,1,2,3,4\).
- Counts of \(U_1=-4,-3,\ldots,4\) are
  \[
  1,4,10,16,19,16,10,4,1.
  \]
- The \(U_1=0\) blocks comprise:
  - four actual blocks of each pair type \(A,B,C\);
  - two actual blocks of each peak type \(F_0,F_2,F_3\);
  - one empty block.
- There are eight actual \(T\)-blocks.
- Consequently the local \(U_1\in\{0,\pm3\}\), \(H=0\) alphabet has \(8+12+4+1=25\) actual blocks.

For prescribed \(U_1=3a\), \(a\in\{\pm1\}\), every \(T\)-block has the form

\[
u(w)=a\chi_1(w)\quad(w\ne w_0),\qquad u(w_0)=0.
\]

Then

\[
U_0=-a\chi_1(w_0),\quad
U_2=-a\chi_3(w_0),\quad
U_3=-a\chi_2(w_0).
\]

For prescribed \(U_2=g\in\{\pm1\}\), exactly two holes satisfy \(\chi_3(w_0)=-g/a\). This checks the physical ternarity and the two choices asserted in S1.

For \(U_1=0\), the allowed \(U_2\)-cases under \(H=0\) are exactly:

| \(U_2\) | Possible shapes |
|---|---|
| \(\pm4\) | \(F_2\) |
| \(\pm2\) | \(A\) or \(C\) |
| \(0\) | \(B,F_3,O\) |

There is no additional local shape hidden by the pair notation.

## 4. Unique integer census

Let \(a,b,c\) count \(A,B,C\)-blocks, let \(p_3\) count \(F_3\)-blocks, and let \(o\) count empty blocks. The \(F_2\)-count is fixed at two.

The stipulated 22 magnitude-two \(U_2\)-blocks give

\[
a+c=22.
\]

The 24 inactive \(U_1=U_2=0\) blocks give

\[
b+p_3+o=24.
\]

The 16 support-three blocks, two \(F_2\)-blocks, and 22 \(U_2\)-pair blocks already contribute

\[
16\cdot3+2\cdot4+22\cdot2=100
\]

nonzeros. Thus \(m=116\) requires

\[
b+2p_3=8.
\]

The \(U_0\)-energy condition is

\[
16+4a+4b=56,\qquad a+b=10.
\]

The \(U_3\)-zero count is

\[
2+a+o=23.
\]

These equations exhaust the nonnegative integer possibilities because Section 3 exhausts the physical local alphabet. Substituting \(a=10-b\) and \(o=21-a\) into the inactive-block equation gives

\[
2b+p_3=13.
\]

Together with \(b+2p_3=8\), this forces

\[
b=6,\quad p_3=1,\quad a=4,\quad c=18,\quad o=17.
\]

Therefore

\[
\boxed{(a,b,c,p_2,p_3,o)=(4,6,18,2,1,17).}
\]

The reconstructed \(U_3\)-energy is also correct:

\[
16+4(b+c)+16p_3=16+96+16=128.
\]

The support count is

\[
48+2(4+6+18)+4(2+1)=116.
\]

This is the same census already derived in S3 LF 99–103, with its explicit local definition \(H=\#F_0=0\). No equivalence to an undisplayed historical definition of \(H\) is asserted.

## 5. Exhaustion of the exact eight-halfblock recipe

For this recipe, \(b=8\), \(p_3=0\), \(o=16\), \(a=k\), and \(c=22-k\). Hence

\[
E_0=16+4k+32=48+4k,\qquad
Z_3=2+k+16=18+k.
\]

The complete integer range is:

| \(k\) | \(E_0\) | \(Z_3\) |
|---:|---:|---:|
| 0 | 48 | 18 |
| 1 | 52 | 19 |
| 2 | **56** | 20 |
| 3 | 60 | 21 |
| 4 | 64 | 22 |
| 5 | 68 | **23** |
| 6 | 72 | 24 |
| 7 | 76 | 25 |
| 8 | 80 | 26 |
| 9 | 84 | 27 |
| 10 | 88 | 28 |
| 11 | 92 | 29 |
| 12 | 96 | 30 |
| 13 | 100 | 31 |
| 14 | 104 | 32 |
| 15 | 108 | 33 |
| 16 | 112 | 34 |
| 17 | 116 | 35 |
| 18 | 120 | 36 |
| 19 | 124 | 37 |
| 20 | 128 | 38 |
| 21 | 132 | 39 |
| 22 | 136 | 40 |

Thus:

- **Energy-only positive example:** \(k=2\), with \((E_0,Z_3)=(56,20)\).
- **Zero-count-only positive example:** \(k=5\), with \((E_0,Z_3)=(68,23)\).
- **Joint requirement:** no solution.

Both single-constraint examples can use the same valid graph and common phase constructed next. Changing an off-support \(U_2=\pm2\) block between \(A\) and \(C\) preserves its prescribed \(U_1,U_2\). The inactive halfblocks also preserve both. These are genuine two-fibre examples, not just formal integer tuples.

## 6. Explicit corrected 256-entry ternary array

This construction supplies one actual array with the corrected counts **and** the complete \(U_1,U_2\) Fourier requirements. Its verification is written, not an executed assay.

### 6.1 Common graph and phase

Write

\[
j=(x,y),\qquad b=(p,t)\in\mathbb F_2^2,
\]

and define

\[
f(j,b)=xp+yt,\qquad
r(j,b)=xy+pt+xp,\qquad
q_B(b)=1+pt.
\]

All expressions in these Boolean functions are over \(\mathbb F_2\).

For Walsh frequency \((\alpha,\beta,\gamma,\delta)\), summing the appropriate linear variables gives

\[
W_{f+q_B}
=4(-1)^{1+\alpha\beta+\gamma\alpha+\delta\beta},
\]

\[
W_r
=4(-1)^{\beta(\alpha+\delta)+\gamma\delta},
\]

\[
W_{r+f}
=4(-1)^{\beta\alpha+\gamma(\alpha+\delta)}.
\]

Thus \(f+q_B,r,r+f\) are all bent, using the **same** \(f,r\).

Use integer bit notation

\[
d_b=1\mathbin{\mathrm{XOR}}3p\mathbin{\mathrm{XOR}}5t,
\]

so \(d_b=(1,2,4,7)\) for \(b=0,1,2,3\). Put

\[
\rho_b=(-1)^{1+pt},\qquad
S=\{(2j+f(j,b),d_b):j,b\in\mathbb F_2^2\}.
\]

Define \(a=(-1)^r\) on \(S\), and zero elsewhere. Define

\[
g(h,0)=
\begin{cases}
4,&h=0,1,\\
-2,&h=2,\ldots,7,
\end{cases}
\]

\[
g(h,d_b)=\rho_b(-2+3\mathbf1_S(h,d_b)),
\]

with \(g=0\) on \(d=3,5,6\).

### 6.2 Complete verification of the two Fourier fibres

Let \(y_h=\ell+2v\) be an \(h\)-frequency and let \(z\) be a \(d\)-frequency. Set \(w(z)=(z\cdot3,z\cdot5)\). Direct substitution gives

\[
\widehat a(y_h,z)
=(-1)^{z\cdot1}W_{r+\ell f}(v,w(z)).
\]

The displayed bent identities therefore give \(|\widehat a|=4\) at **all 64 frequencies**.

For \(g\):

- At \(y_h=0\),
  \[
  \widehat g(0,z)
  =-4\left(1+\sum_b\rho_b(-1)^{z\cdot d_b}\right).
  \]
  The sum is \(-2\) for \(z=0,1,2,4\), and \(+2\) for \(z=3,5,6,7\). Thus the four named small coefficients are \(+4\), and the other four are \(-12\).
- At \(\ell=0,v\ne0\), the \(E\)-contribution is \(12\), and every \(B\)-contribution vanishes, giving \(\widehat g=12\).
- At \(\ell=1\),
  \[
  \widehat g(y_h,z)
  =3(-1)^{z\cdot1}W_{f+q_B}(v,w(z)),
  \]
  which has magnitude 12.

This verifies the full \(4/12\) spectrum and its four named small positions. It does not infer global spectra from local counts.

### 6.3 Every physical block

The following rules specify all 256 entries, without an unspecified placement or sign choice.

On \(S\), let

\[
w_0=
\begin{cases}
0,&-g(h,d)a(h,d)=1,\\
1,&-g(h,d)a(h,d)=-1.
\end{cases}
\]

Set \(u(h,d,w)=a(h,d)\chi_1(w)\) except \(u(h,d,w_0)=0\).

Off \(S\), use:

| Locations | Physical row \(u(h,d,\cdot)\) |
|---|---|
| \(d=0,\ h=0,1\) | \(\chi_2\) |
| \(d=0,\ h=2,3,4,5\) | \(-(\chi_0+\chi_2)/2\) |
| Every other off-\(S\), \(|g|=2\) location | \((g/2)(\chi_2+\chi_3)/2\) |
| \(d=3,\ h=0,\ldots,5\) | \((\chi_0+\chi_3)/2\) |
| \(d=3,\ h=6\) | \(\chi_3\) |
| All remaining locations | \(0\) |

These rows are all ternary. Their local transforms give respectively:

- 16 \(T\)-blocks;
- two \(F_2\)-blocks;
- four \(A\)-blocks;
- eighteen \(C\)-blocks;
- six \(B\)-blocks;
- one \(F_3\)-block;
- seventeen empty blocks.

Every row has \(U_1=3a\) and \(U_2=g\). Therefore the full common graph/phase spectra proved above are preserved, not merely the aggregate counts.

This array has support 116, \(H=0\), \(E_0=56\), and \(Z_3=23\).

**Limitation:** its displayed-coordinate sum is \(-4\), not zero. Indeed, its support-three rows contribute \(\sum U_0=-8\), the four \(A\)-rows contribute \(-8\), and the six \(B\)-rows contribute \(12\). No conclusion is drawn about whether some allowed re-normalization could restore balance while meeting the other unproved requirements. This construction is a **two-fibre, aggregate-compatible lift**, not an original balanced Boolean caller.

## 7. Controls and intended outcomes

The following outcomes are established algebraically above and are encoded in the unexecuted checker. They are **not observed execution results**.

| Control | Intended outcome and exact reason |
|---|---|
| Corrected array from Section 6 | Accept the scoped requirements; summary \((m,E_0,Z_3)=(116,56,23)\) |
| Eight-halfblock recipe, \(k=2\), energy requirement only | Accept; summary \((116,56,20)\) |
| Same \(k=2\) array, both requirements | Reject specifically `U3_ZERO_COUNT:20` |
| Eight-halfblock recipe, \(k=5\), zero-count requirement only | Accept; summary \((116,68,23)\) |
| Same \(k=5\) array, both requirements | Reject specifically `U0_ENERGY:68` |
| Replace an empty corrected block by \((1,1,1,1)\) | Reject specifically `H0_FORBIDDEN`, before the altered mass can mask the reason |
| Delete the first entry of a positive full-\(U_2\) block by changing it to zero | Reject specifically `U1_MISMATCH`; the mutated local \(U_1\) is \(-1\) |

The rejection harness accepts only the stated `CheckError` reason. An arbitrary exception, timeout, or unrelated failure does not count as a successful control.

## 8. Complete prospective checker — NOT RUN

**Prospective argv:** argument 0 is `python3`; argument 1 is `-B`; argument 2 is `-c`; argument 3 is the complete source below.

Every source line has a literal `PY|` prefix. Remove only that prefix, preserving the remaining indentation and line breaks. No source portion is omitted.

The program uses only the standard library, fixed in-memory inputs, and stdout. It has no file, network, child-process, author-code, or external-source input. A cooperative 50-second budget check is included within the bounded calculations; no elapsed time or successful run is claimed.

PY|from itertools import product
PY|from time import perf_counter
PY|
PY|START = perf_counter()
PY|
PY|class CheckError(Exception):
PY|    pass
PY|
PY|def need(condition, reason):
PY|    if not condition:
PY|        raise CheckError(reason)
PY|
PY|def budget():
PY|    if perf_counter() - START > 50:
PY|        raise RuntimeError("COOPERATIVE_BUDGET_50S")
PY|
PY|def chi(s, w):
PY|    return 1 if (s & w).bit_count() % 2 == 0 else -1
PY|
PY|def walsh(v):
PY|    n = len(v)
PY|    need(n > 0 and (n & (n - 1)) == 0, "POWER_OF_TWO")
PY|    out = []
PY|    for s in range(n):
PY|        budget()
PY|        out.append(sum(v[w] * chi(s, w) for w in range(n)))
PY|    return tuple(out)
PY|
PY|def shape(v):
PY|    t = walsh(v)
PY|    if abs(t[1]) == 3:
PY|        need(sum(x != 0 for x in v) == 3, "ODD_SUPPORT")
PY|        need(all(abs(t[s]) == 1 for s in (0, 2, 3)), "ODD_SHAPE")
PY|        return "T"
PY|    if t[1] != 0:
PY|        return "OUT"
PY|    nz = tuple(s for s in range(4) if t[s] != 0)
PY|    if not nz:
PY|        need(not any(v), "ZERO_INVERSE")
PY|        return "O"
PY|    if len(nz) == 1 and abs(t[nz[0]]) == 4:
PY|        return "F" + str(nz[0])
PY|    if len(nz) == 2 and all(abs(t[s]) == 2 for s in nz):
PY|        for pair, label in (((0, 2), "A"), ((0, 3), "B"), ((2, 3), "C")):
PY|            if nz == pair:
PY|                return label
PY|    raise CheckError("UNCLASSIFIED_U1_ZERO_BLOCK")
PY|
PY|local = tuple(product((-1, 0, 1), repeat=4))
PY|need(len(local) == 81 and len(set(local)) == 81, "LOCAL_UNIVERSE")
PY|support_hist = tuple(sum(sum(x != 0 for x in v) == m for v in local) for m in range(5))
PY|need(support_hist == (1, 8, 24, 32, 16), "SUPPORT_HISTOGRAM")
PY|u1_hist = tuple(sum(walsh(v)[1] == k for v in local) for k in range(-4, 5))
PY|need(u1_hist == (1, 4, 10, 16, 19, 16, 10, 4, 1), "U1_HISTOGRAM")
PY|labels = ("T", "A", "B", "C", "F0", "F2", "F3", "O", "OUT")
PY|shape_hist = tuple(sum(shape(v) == label for v in local) for label in labels)
PY|need(shape_hist == (8, 4, 4, 4, 2, 2, 2, 1, 54), "SHAPE_HISTOGRAM")
PY|for v in local:
PY|    print("BLOCK", v, "WALSH", walsh(v), "SUPPORT", sum(x != 0 for x in v), "CLASS", shape(v))
PY|print("SUPPORT_HISTOGRAM", support_hist)
PY|print("U1_HISTOGRAM", u1_hist)
PY|print("SHAPE_HISTOGRAM", tuple(zip(labels, shape_hist)))
PY|
PY|integer_solutions = []
PY|for aa in range(23):
PY|    for bb in range(25):
PY|        for p3 in range(25 - bb):
PY|            budget()
PY|            cc = 22 - aa
PY|            oo = 24 - bb - p3
PY|            if 100 + 2 * bb + 4 * p3 != 116:
PY|                continue
PY|            if 16 + 4 * (aa + bb) != 56:
PY|                continue
PY|            if 2 + aa + oo != 23:
PY|                continue
PY|            integer_solutions.append((aa, bb, cc, 2, p3, oo))
PY|need(integer_solutions == [(4, 6, 18, 2, 1, 17)], "INTEGER_CENSUS")
PY|print("INTEGER_SOLUTIONS", tuple(integer_solutions))
PY|
PY|D = (1, 2, 4, 7)
PY|a = [0] * 64
PY|g = [0] * 64
PY|for h, d in product(range(8), repeat=2):
PY|    i = 8 * h + d
PY|    if d == 0:
PY|        g[i] = 4 if h < 2 else -2
PY|    elif d in D:
PY|        b = D.index(d)
PY|        j = h // 2
PY|        x, y = j & 1, (j >> 1) & 1
PY|        p, t = b & 1, (b >> 1) & 1
PY|        f = (x * p + y * t) & 1
PY|        r = (x * y + p * t + x * p) & 1
PY|        on_support = (h & 1) == f
PY|        rho = 1 if p * t else -1
PY|        a[i] = (-1 if r else 1) if on_support else 0
PY|        g[i] = rho * (-2 + 3 * int(on_support))
PY|a, g = tuple(a), tuple(g)
PY|full2 = tuple(i for i in range(64) if abs(g[i]) == 4)
PY|twos = tuple(i for i in range(64) if a[i] == 0 and abs(g[i]) == 2)
PY|inactive = tuple(i for i in range(64) if a[i] == 0 and g[i] == 0)
PY|need(sum(x != 0 for x in a) == 16, "GRAPH_SIZE")
PY|need((len(full2), len(twos), len(inactive)) == (2, 22, 24), "GRAPH_PARTITION")
PY|
PY|def make_array(A, B, F3):
PY|    A, B, F3 = set(A), set(B), set(F3)
PY|    need(A <= set(twos), "A_DOMAIN")
PY|    need(B <= set(inactive) and F3 <= set(inactive), "INACTIVE_DOMAIN")
PY|    need(not (B & F3), "INACTIVE_OVERLAP")
PY|    rows = []
PY|    for i in range(64):
PY|        if a[i] != 0:
PY|            hole = 0 if -g[i] * a[i] == 1 else 1
PY|            row = tuple(0 if w == hole else a[i] * chi(1, w) for w in range(4))
PY|        elif abs(g[i]) == 4:
PY|            row = tuple((g[i] // 4) * chi(2, w) for w in range(4))
PY|        elif abs(g[i]) == 2:
PY|            sig = g[i] // 2
PY|            if i in A:
PY|                row = tuple(sig * (1 + chi(2, w)) // 2 for w in range(4))
PY|            else:
PY|                row = tuple(sig * (chi(2, w) + chi(3, w)) // 2 for w in range(4))
PY|        elif i in B:
PY|            row = tuple((1 + chi(3, w)) // 2 for w in range(4))
PY|        elif i in F3:
PY|            row = tuple(chi(3, w) for w in range(4))
PY|        else:
PY|            row = (0, 0, 0, 0)
PY|        rows.append(row)
PY|    return tuple(rows)
PY|
PY|def check_array(rows, require_energy=True, require_zeros=True):
PY|    need(len(rows) == 64, "BLOCK_COUNT")
PY|    transforms = []
PY|    for i, row in enumerate(rows):
PY|        budget()
PY|        need(len(row) == 4 and all(x in (-1, 0, 1) for x in row), "TERNARITY")
PY|        u = walsh(row)
PY|        need(not (u[1] == 0 and abs(u[0]) == 4), "H0_FORBIDDEN")
PY|        need(u[1] == 3 * a[i], "U1_MISMATCH")
PY|        need(u[2] == g[i], "U2_MISMATCH")
PY|        transforms.append(u)
PY|    mass = sum(x != 0 for row in rows for x in row)
PY|    energy = sum(u[0] ** 2 for u in transforms)
PY|    zeros = sum(u[3] == 0 for u in transforms)
PY|    need(mass == 116, "SUPPORT_NOT_116")
PY|    wa = walsh(tuple(u[1] // 3 for u in transforms))
PY|    wg = walsh(tuple(u[2] for u in transforms))
PY|    need(all(abs(x) == 4 for x in wa), "A_COMPLETE_SPECTRUM")
PY|    for frequency, value in enumerate(wg):
PY|        if frequency in (0, 1, 2, 4):
PY|            need(value == 4, "G_NAMED_SMALL_SPECTRUM")
PY|        else:
PY|            need(abs(value) == 12, "G_COMPLETE_LARGE_SPECTRUM")
PY|    if require_energy:
PY|        need(energy == 56, "U0_ENERGY:" + str(energy))
PY|    if require_zeros:
PY|        need(zeros == 23, "U3_ZERO_COUNT:" + str(zeros))
PY|    return mass, energy, zeros
PY|
PY|good_A = tuple(8 * h for h in (2, 3, 4, 5))
PY|good_B = tuple(8 * h + 3 for h in range(6))
PY|good_F3 = (8 * 6 + 3,)
PY|good = make_array(good_A, good_B, good_F3)
PY|need(check_array(good) == (116, 56, 23), "CORRECTED_SUMMARY")
PY|census_labels = ("A", "B", "C", "F2", "F3", "O")
PY|physical_census = tuple(sum(shape(row) == label for row in good) for label in census_labels)
PY|need(physical_census == (4, 6, 18, 2, 1, 17), "PHYSICAL_CENSUS")
PY|flat_good = tuple(x for row in good for x in row)
PY|need(len(flat_good) == 256, "ARRAY_LENGTH")
PY|need(sum(flat_good) == -4, "DISPLAYED_BALANCE_DIAGNOSTIC")
PY|print("CORRECTED_SUMMARY", check_array(good))
PY|print("CORRECTED_PHYSICAL_CENSUS", physical_census)
PY|print("CORRECTED_ARRAY_256", flat_good)
PY|print("DISPLAYED_COORDINATE_SUM", sum(flat_good))
PY|
PY|def recipe(k):
PY|    need(0 <= k <= 22, "K_RANGE")
PY|    return make_array(twos[:k], inactive[:8], ())
PY|
PY|energy_only, zeros_only, joint = [], [], []
PY|for k in range(23):
PY|    summary = check_array(recipe(k), False, False)
PY|    need(summary == (116, 48 + 4 * k, 18 + k), "RECIPE_FORMULA")
PY|    if summary[1] == 56:
PY|        energy_only.append(k)
PY|    if summary[2] == 23:
PY|        zeros_only.append(k)
PY|    if summary[1:] == (56, 23):
PY|        joint.append(k)
PY|    print("RECIPE", k, summary)
PY|need(energy_only == [2] and zeros_only == [5] and joint == [], "RECIPE_EXHAUSTION")
PY|need(check_array(recipe(2), True, False) == (116, 56, 20), "ENERGY_ONLY_POSITIVE")
PY|need(check_array(recipe(5), False, True) == (116, 68, 23), "ZEROS_ONLY_POSITIVE")
PY|print("ENERGY_ONLY_K", tuple(energy_only))
PY|print("ZEROS_ONLY_K", tuple(zeros_only))
PY|print("JOINT_K", tuple(joint))
PY|
PY|def expect_failure(label, action, reason):
PY|    try:
PY|        action()
PY|    except CheckError as error:
PY|        need(str(error) == reason, "CONTROL_WRONG_REASON:" + label + ":" + str(error))
PY|        print("CONTROL_REJECTED", label, reason)
PY|    else:
PY|        raise CheckError("CONTROL_UNEXPECTED_PASS:" + label)
PY|
PY|expect_failure("energy_only_fails_zeros", lambda: check_array(recipe(2)), "U3_ZERO_COUNT:20")
PY|expect_failure("zeros_only_fails_energy", lambda: check_array(recipe(5)), "U0_ENERGY:68")
PY|bad_h = list(good)
PY|empty_index = next(i for i, row in enumerate(good) if shape(row) == "O")
PY|bad_h[empty_index] = (1, 1, 1, 1)
PY|expect_failure("forbidden_U0_peak", lambda: check_array(tuple(bad_h)), "H0_FORBIDDEN")
PY|bad_u1 = list(good)
PY|full_index = full2[0]
PY|bad_u1[full_index] = (0,) + bad_u1[full_index][1:]
PY|expect_failure("damaged_full_U2_block", lambda: check_array(tuple(bad_u1)), "U1_MISMATCH")
PY|budget()
PY|print("CHECKER_STATUS: PASS")
PY|print("ELAPSED_SECONDS", perf_counter() - START)

## 9. Relationship to the actual target and disposition

The original f468 recipe remains a valid local ternary lift with support 116 and the stipulated two Fourier fibres. Its deliberate local scope is not invalidated by its failure to meet additional original-caller conditions.

S2 correctly strengthens that warning: **the particular eight-halfblock/no-inactive-full-block recipe cannot satisfy both named aggregate imports**. S2 also correctly credits f263 with the already-derived full local census.

The corrected construction in this return shows that the unique aggregate census can coexist with the canonical graph and common phase at the two-fibre level. It does not establish the global \(U_0,U_3\) Walsh requirements, original balance, named rank/eight-zero/\(T\) conditions, a common complementary 140-support \(V\), or the global odd Walsh caps. Neither five-span nor either six-span branch is excluded.

**Findings:** No defect found in the additive erratum at its declared scope.

**Overall correctness:** correct.

**Explanation:** The exact eight-halfblock recipe has incompatible energy and zero-count requirements, and the corrected census agrees with the earlier f263 derivation. The written reconstruction additionally supplies a graph/phase-compatible aggregate lift, but no scientific execution or original-target completion is claimed.

**Confidence:** 0.98 for the written conclusions. The supplied program remains **NOT RUN**, not a passed finite verification, independent-family review, human review, kernel proof, or novelty determination.