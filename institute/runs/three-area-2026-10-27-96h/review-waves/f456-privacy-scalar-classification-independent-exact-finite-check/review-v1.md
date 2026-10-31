# FINITE f456 — Independent exact reconstruction and checker source

**Status: written reconstruction completed; scientific execution NOT RUN.**  
**New findings: 0 FATAL / 0 MAJOR / 0 MINOR within the checked algebraic scope.**  
The historical privacy penalty-sign **1 MAJOR remains retained**. This return does not adopt the conditional scalar-uniqueness claim or establish actual-regime existence.

No repository file was written. The complete body and independently authored source below are returned for Main materialization.

## 1. Bindings, chronology, and execution boundary

The following are **parent-attributed observations**, not child-executed hashing or a child-native clock:

- Manifest SHA256: `0186acb78ca9bd0ab04adb0dfebcbbf7a80434ed34bf53afa2d37fdcefb60afa`.
- Receipt SHA256: `24b5e2898366d9cb880942f407d6c310832310ef65f203db57533d0e0c61b03d`.
- Packet SHA256: `de9a1ff1175397fd14b519fbbbc5d17da1113b2791c123217de7732d0748bb73`.
- Parent clock: `2026-10-30T11:39:34-0700 PDT`.

Before opening the scientific packet, I read the complete manifest, receipt, parent metadata supply, and all ten permission/status controls through their endings. I then sent Main a direct pre-body ACK identifying the FINITE duty and the execution limitation.

I subsequently read the packet in ordered raw chunks of at most 20 LF: 1–20, 21–40, …, 1061–1080, then the ending through packet line 1090. This included S1 logical line 1049 and S2 line 39. Focused rereads of the full functional and rounded-core correction followed.

The inherited Bash restriction allows only read-only diff/log/show/PR-diff commands. Accordingly:

- No scientific interpreter, CAS, solver, numerical integration, enumeration, build, test, lint, formatter, or external-model CLI was run.
- There is no observed scientific stdout, exit status, elapsed time, child-native start clock, or checker hash.
- I did not bypass that restriction through another execution route.
- All exact values stated below are **written deductions**, not purported program output.
- The full independent program is supplied below with **NOT RUN** status.

The only fixed scientific instance used is the assigned author instance \(m=1/10\), with its prescribed polynomial and bounds. Other calculations retain formal parameters. No additional private selected diagnostic, sibling return, author implementation, or external scientific source was used.

All held privacy-auxiliary, CORE, AME, PHv8/cp116, F439, F444, and F448 scientific episodes and consumers remain NONINPUT. Their controls were read for status and permissions only. This is an access/method disclosure, not a cognitive-isolation certificate.

## 2. Independent reconstruction of the complete signed functional

Write

\[
b=\frac{m}{1+m},\qquad v=m(1+m).
\]

The geometric moment recurrence follows directly from memorylessness:

\[
T_0=1,\qquad
T_n=m\sum_{j=0}^{n-1}\binom njT_j\quad(n\ge1).
\]

It gives

\[
T_1=m,\quad T_2=m+2m^2,\quad
T_3=m+6m^2+6m^3,
\]

\[
T_4=m+14m^2+36m^3+24m^4.
\]

Starting with the supplied area, quadratic moment, and boundary moment definitions—not a truncated signed integrand—gives

\[
\begin{aligned}
(1+m)H_\lambda
={}&Q(F_0)-\lambda A(F_0)\\
&+m\Bigl[
Q(F_1)+mB(F_1)+(A(F_1)+8c^2)T_2
+\frac{16}{3}cT_3+\frac23T_4\\
&\hspace{39mm}-\lambda\{A(F_1)+8cm+2T_2\}
\Bigr].
\end{aligned}
\]

Within the \(F_1\) integral, \(T_2A(F_1)\) contributes \(-8T_2\int_0^c y\,dy=-4c^2T_2\). Combining it with the explicit \(8c^2T_2\) leaves the required deterministic term \(4c^2T_2\). Thus

\[
H_\lambda
=8(1-b)\int_0^a\psi_0(F_0,y)\,dy
+8b\int_0^c\psi_1(F_1,y)\,dy+bC(c;\lambda),
\]

with the complete \(C\) appearing in the packet. In particular, neither the geometric weight \(b\) nor \(C\) can be omitted.

Differentiating the integrand reconstructed from area and moments gives

\[
\partial_z\psi_1
=z^2+2mz+y^2+T_2-\lambda
=(z+m)^2+v+y^2-\lambda.
\]

The active-core pooling identity is

\[
\psi_0(x,y)+m\psi_1(x+1,y)
=(1+m)\psi_1(x,y)+m(\kappa-\lambda),
\]

where \(\kappa=1/3+2v\). Therefore the normalized active-core value contains the essential offset

\[
8ma(\kappa-\lambda).
\]

This offset is a required part of the active coupling calculation; it is not being identified with the entire independent-box penalty \(P\).

The program below independently builds \(A,Q,B\) by polynomial integration for complete piecewise-affine profiles, then compares the resulting full functional with the signed-integrand representation.

## 3. Scalar derivatives, including every moving-endpoint term

These identities are used at the active-core scope: the actual \(\lambda=V\), or another parameter for which the stated active-core reduction is valid. They are not a claim that the reduced formula describes arbitrary \(\lambda\) outside that scope.

Put

\[
U(y)=2a-y,\quad k(y)=2a+1-y,\quad s=2a+1-c,
\]

and let \(d(z,y)=\partial_z\psi_1(z,y)\). Define

\[
A=\int_0^a[-d(U(y),y)]_+\,dy,\qquad
L=\int_0^a[d(a,y)]_+\,dy,
\]

\[
B=\int_a^s[d(k(y),y)]_+\,dy.
\]

### Derivative in \(a\)

A lower-face core moves with speed one; an upper-face core moves with speed two. A free coordinate contributes zero through its coordinate derivative. The active corner floor \(k\) moves with speed two.

The shared moving endpoint cancels because \(F_0(a)=a\), \(F_1(a)=a+1\), and

\[
\psi_0(a,a)=0.
\]

Consequently,

\[
\boxed{\frac{h_a}{16}=\frac12L-A+bB.}
\]

The checker derives the derivative directly from the complete area/moment polynomial on both wholly lower-core and wholly upper-core affine strata with the continuous \(k/c\) tail. Its comparison is therefore not merely a restatement of the proposed derivative.

### Derivative in \(c\)

The moving terminal height contributes

\[
\psi_1(c,c)=2mc^2+T_2c.
\]

The deterministic term contributes

\[
\frac{C'(c)}8=cT_2+\frac23T_3-m\lambda.
\]

Their sum is

\[
D_0(c)=2cT_2+2mc^2+\frac23T_3-m\lambda.
\]

Together with the lower-face and upper-face speeds,

\[
\boxed{
\frac{h_c}{8b}
=D_0(c)+\int_s^c[d(c,y)]_+\,dy
-2\int_a^c[-d(2c-y,y)]_+\,dy.
}
\]

At the edge this is the right derivative. Free-interface boundary terms cancel because the competing profile values agree there; the free coordinate derivative is zero.

### Edge derivative

At \(u=a+1/2\), the tail box collapses to \(2u-y\). Direct integration gives

\[
\int_a^u d(2u-y,y)\,dy+\frac12D_0(u)
=(1+m)\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right].
\]

Thus, on the no-lower-core branch,

\[
\boxed{
\frac{e_a}{16}
=m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]-A.
}
\]

This retains both the diagonal endpoint and deterministic tail contributions.

## 4. Corner-root algebra and the negative-curvature calculation

Set \(y=a+x\) in the corner. Then

\[
d(k(a+x),a+x)
=K-2(1+m)x+2x^2,
\]

where

\[
K=(a+1+m)^2+a^2+v-\lambda.
\]

If the corner zero is at \(x=\ell\),

\[
K=2(1+m)\ell-2\ell^2.
\]

Integrating first and only then imposing this constraint gives

\[
B=(1+m)\ell^2-\frac43\ell^3.
\]

At fixed \(\lambda\),

\[
\ell_a=\frac{2a+1+m}{1+m-2\ell},
\]

so

\[
\boxed{B_a=2(2a+1+m)\ell.}
\]

The all-upper-core integral independently gives

\[
A=a(\lambda-T_2)-3ma^2-\frac83a^3.
\]

Therefore

\[
\boxed{
\frac{h_{aa}}{16}
=-\lambda+T_2+6ma+8a^2
+2b(2a+1+m)\ell.
}
\]

Replacing \(\lambda\) by the smaller \(D(u)\) and \(\ell\) by the larger \(1/2\), in the coefficient-positive directions justified by the hypotheses, yields

\[
\frac{h_{aa}}{16}
<6a^2+(4m-2+2b)a-\frac12.
\]

Under the manuscript's derived \(a<1/8\), \(m<1/2\), \(b<1/3\),

\[
\frac{h_{aa}}{16}
<\frac6{64}+\frac1{12}-\frac12
=-\frac{31}{96}<0.
\]

I found no algebraic defect in this estimate. Its use remains conditional on the preceding actual-minimum and pruning hypotheses; it is not a global concavity assertion.

## 5. Both core branches and their matching

For an entirely upper-face core, integration gives

\[
F_{\rm upper}
=\frac83a^3+4ma^2+(2T_2-\lambda)a
+m\left(\kappa-\frac{\lambda}{2}\right).
\]

For a free-root block followed by an upper-face block of length \(q\),

\[
\lambda=D(a)+2mq+2q^2.
\]

Integrating \(-d(U,y)\) over \(y\in[a-q,a]\), and then imposing that constraint, gives

\[
A=mq^2+\frac43q^3.
\]

Hence

\[
F_{\rm free}
=m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]
-mq^2-\frac43q^3.
\]

Implicit differentiation gives

\[
q_a=-\frac{2a+m}{2q+m},
\]

and consequently

\[
\boxed{
(F_{\rm free})_a
=m(2a+1+2m)+2q(2a+m)>0.
}
\]

At \(q=a\), equivalently \(\lambda=R(a)\), both the values and first derivatives match; the common first derivative is \(\lambda\).

The exact error from incorrectly retaining the upper-branch polynomial in the free branch is

\[
\boxed{
F_{\rm free}-F_{\rm upper}
=-(a-q)^2\left(m+\frac23a+\frac43q\right),
}
\]

after the free-branch constraint is imposed. Thus omitting the free branch is a genuine algebraic error, not an innocuous alternative parametrization.

The turning-point substitution in the upper branch gives

\[
F(\theta_\lambda;\lambda)
=\frac13v(1+2m)-\frac23(\lambda/2-v)^{3/2}.
\]

The necessary strict negativity is exactly

\[
\lambda>2v+2^{1/3}[v(1+2m)]^{2/3}.
\]

This supports the manuscript's necessary bound. It does not establish existence or a sufficient parameter interval.

## 6. Full value equation and the prescribed \(m=1/10\) instance

For diamond profiles, direct area/moment integration gives

\[
H_{\rm diam}(t;\lambda)
=\frac23M_4(t)-2\lambda M_2(t).
\]

The memoryless moment identity checked in the source is

\[
(1+m)M_j(t)=t^j+mM_j(t+1).
\]

It verifies that the expression includes the entire geometric tail, rather than merely the first two visible diamonds.

For a rounded core, the exact cubic identity is

\[
\psi_1(U)-\psi_1(r)
=(U-r)d(r)+(U-r)^2\left(\frac{U+2r}{3}+m\right).
\]

On the free root \(d(r)=0\), so the full value is

\[
e(a;\lambda)
=\frac23M_4(2a)-2\lambda M_2(2a)
-8\int_0^{a-\tau}(U-r)^2
\left(\frac{U+2r}{3}+m\right)\,dy.
\]

No rational numerical value is claimed for a nontrivial radical integral. The supplied program checks the polynomial cubic identity; the integral statement remains a written identity.

### Prescribed diamond instance

At \(m=1/10\),

\[
T_2=\frac3{25},\qquad
T_3=\frac{83}{500},\qquad T_4=\frac{174}{625}.
\]

Deriving the elimination polynomial from the moment products gives

\[
250(2M_3M_2-M_4M_1)
=250t^5+125t^4+80t^3-47t^2-48t+3=p(t).
\]

Written exact arithmetic confirms

\[
p(11/20)=-147/512,\qquad p(3/5)=51/5,
\]

\[
p'(1/2)=845/8.
\]

In addition,

\[
p''(1/2+x)=1146+5730x+9000x^2+5000x^3,
\]

so \(p''>0\) for \(t\ge1/2\). This proves the unique root in the assigned interval.

There is also a distinct decreasing positive root: \(p(0)>0\), \(p(11/20)<0\), while \(p'''\) has positive coefficients, \(p''(0)<0\), and \(p'(0)<0<p'(1/2)\). Hence \(p'\) has exactly one positive zero, the intervening minimum of \(p\) is negative, and the earlier crossing is decreasing. The checker independently supplies a rational Sturm calculation using only the natural boundary zero and assigned interval endpoints.

The orientation matters because

\[
p'(t)=250\{6M_2(t)^2-M_4(t)\}
=750M_2(t)\left(2M_2(t)-\lambda(t)\right),
\]

where \(\lambda(t)=M_4(t)/(3M_2(t))\). Thus the earlier decreasing root has negative edge curvature and must not be accepted as a local-minimum root.

For the assigned increasing root \(t_0\), positive-coefficient moment bounds give the slightly more explicit lower bound

\[
\frac{M_4(11/20)}{3M_2(3/5)}
=\frac{54371}{96000}>\frac59,
\]

and

\[
\lambda_0<
\frac{M_4(3/5)}{3M_2(11/20)}
=\frac{256}{355}<\frac34.
\]

Furthermore,

\[
2M_3-3M_1M_2
=-t^3-\frac3{10}t^2+\frac3{10}t+\frac{37}{125}.
\]

Its derivative is negative throughout the assigned interval, and its value at \(3/5\) is \(19/125>0\). Therefore \(\lambda_0>M_2(t_0)=R(a_0)\): the diamond branch is valid.

The curvature bound is

\[
F_a(a_0;\lambda_0)
>\frac{213}{200}-\frac34
=\frac{63}{200}>0.
\]

Finally,

\[
c_0>\frac{31}{40},\qquad
D(c_0)>2(31/40)^2=\frac{961}{800}>1>\lambda_0.
\]

The upper-face negative-gradient integral in the normal formula vanishes, while

\[
D_0(c_0)
=m(D(c_0)-\lambda_0)+2c_0v+
\left(\frac23m+3m^2+2m^3\right)>0.
\]

Thus the prescribed candidate has the stated strict normal. These deductions do **not** prove global minimality, \(\lambda_0=V\), or actual-regime existence at \(b=1/11\).

## 7. Complete independent source — NOT RUN

**Proposed argv, not executed:**

- argv[0]: `python3`
- argv[1]: `-I`
- argv[2]: `-B`
- argv[3]: `-c`
- argv[4]: the complete source below, reconstructed by removing the initial literal `PY|` from each source line and joining the resulting lines with LF, including a final LF.

The source performs no filesystem access, network access, subprocess creation, installation, or deletion. It uses only standard-library exact rational arithmetic and small polynomial operations. It contains a cooperative 50-second calculation guard; no elapsed-time or completion claim is made without execution.

The mutation controls reject their intended invariant violations: missing \(b\), missing deterministic tail constant, missing moving endpoint, missing active-core pooling offset, flipped normal, missing free branch, and accepting a decreasing root as a minimum. A nonzero polynomial discrepancy or a specific root-orientation failure is required; an unrelated exception does not count as a successful mutation rejection.

Each following line prefixed `PY|` is source, not observed output.

PY|from fractions import Fraction as R
PY|from math import comb
PY|from time import monotonic
PY|
PY|started = monotonic()
PY|deadline = started + 50
PY|
PY|class CheckFailure(Exception):
PY|    pass
PY|
PY|def tick():
PY|    if monotonic() > deadline:
PY|        raise CheckFailure("calculation budget exhausted; no completed receipt")
PY|
PY|NAMES = ("a", "c", "m", "L", "y", "ell", "q", "z", "r", "t")
PY|INDEX = {name: i for i, name in enumerate(NAMES)}
PY|ZERO = (0,) * len(NAMES)
PY|
PY|class P:
PY|    def __init__(self, value=0):
PY|        tick()
PY|        if isinstance(value, P):
PY|            self.c = value.c.copy()
PY|        elif isinstance(value, dict):
PY|            self.c = {e: R(v) for e, v in value.items() if v}
PY|        else:
PY|            self.c = {} if not value else {ZERO: R(value)}
PY|
PY|    def __add__(self, other):
PY|        out = self.c.copy()
PY|        for e, v in P(other).c.items():
PY|            out[e] = out.get(e, R(0)) + v
PY|            if not out[e]:
PY|                del out[e]
PY|        return P(out)
PY|
PY|    __radd__ = __add__
PY|
PY|    def __neg__(self):
PY|        return P({e: -v for e, v in self.c.items()})
PY|
PY|    def __sub__(self, other):
PY|        return self + (-P(other))
PY|
PY|    def __rsub__(self, other):
PY|        return P(other) - self
PY|
PY|    def __mul__(self, other):
PY|        out = {}
PY|        other = P(other)
PY|        for e, v in self.c.items():
PY|            tick()
PY|            for f, w in other.c.items():
PY|                g = tuple(x + y for x, y in zip(e, f))
PY|                out[g] = out.get(g, R(0)) + v * w
PY|        return P(out)
PY|
PY|    __rmul__ = __mul__
PY|
PY|    def __truediv__(self, scalar):
PY|        scalar = R(scalar)
PY|        if not scalar:
PY|            raise CheckFailure("division by zero")
PY|        return P({e: v / scalar for e, v in self.c.items()})
PY|
PY|    def __pow__(self, exponent):
PY|        if not isinstance(exponent, int) or exponent < 0:
PY|            raise CheckFailure("non-polynomial exponent")
PY|        out = P(1)
PY|        for unused in range(exponent):
PY|            out = out * self
PY|        return out
PY|
PY|    def d(self, name):
PY|        j = INDEX[name]
PY|        out = {}
PY|        for e, v in self.c.items():
PY|            if e[j]:
PY|                f = list(e)
PY|                f[j] -= 1
PY|                out[tuple(f)] = v * e[j]
PY|        return P(out)
PY|
PY|    def anti(self, name):
PY|        j = INDEX[name]
PY|        out = {}
PY|        for e, v in self.c.items():
PY|            f = list(e)
PY|            f[j] += 1
PY|            out[tuple(f)] = v / f[j]
PY|        return P(out)
PY|
PY|    def sub(self, name, replacement):
PY|        j = INDEX[name]
PY|        replacement = P(replacement)
PY|        out = P()
PY|        for e, v in self.c.items():
PY|            f = list(e)
PY|            power = f[j]
PY|            f[j] = 0
PY|            out = out + P({tuple(f): v}) * replacement ** power
PY|        return out
PY|
PY|    def scalar(self):
PY|        if any(e != ZERO for e in self.c):
PY|            raise CheckFailure("nonconstant used as rational number")
PY|        return self.c.get(ZERO, R(0))
PY|
PY|def variable(name):
PY|    e = list(ZERO)
PY|    e[INDEX[name]] = 1
PY|    return P({tuple(e): R(1)})
PY|
PY|a, c, m, L, y, ell, q, z, r, t = [variable(n) for n in NAMES]
PY|checks = 0
PY|mutations = 0
PY|
PY|def need(name, condition):
PY|    global checks
PY|    tick()
PY|    if not condition:
PY|        raise CheckFailure(name)
PY|    checks += 1
PY|
PY|def eq(name, left, right=0):
PY|    need(name, P(left).c == P(right).c)
PY|
PY|def reject_eq(name, mutated, reference, reason):
PY|    global mutations
PY|    need("mutation survived: " + name, P(mutated).c != P(reference).c)
PY|    mutations += 1
PY|    print("MUTANT_REJECT", name, reason)
PY|
PY|def reject_accept(name, mutated_accepts, correct_accepts, reason):
PY|    global mutations
PY|    need("mutation not discriminated: " + name,
PY|         mutated_accepts and not correct_accepts)
PY|    mutations += 1
PY|    print("MUTANT_REJECT", name, reason)
PY|
PY|def I(f, lo, hi):
PY|    primitive = P(f).anti("y")
PY|    return primitive.sub("y", hi) - primitive.sub("y", lo)
PY|
PY|def positive_coefficients(f):
PY|    f = P(f)
PY|    return bool(f.c) and all(v > 0 for v in f.c.values())
PY|
PY|T = [P(1)]
PY|for n in range(1, 5):
PY|    T.append(m * sum((comb(n, j) * T[j] for j in range(n)), P()))
PY|T2, T3, T4 = T[2], T[3], T[4]
PY|v = m * (1 + m)
PY|kappa = R(1, 3) + 2 * v
PY|eq("derived T2", T2, m + 2 * m ** 2)
PY|eq("derived T3", T3, m + 6 * m ** 2 + 6 * m ** 3)
PY|eq("derived T4", T4, m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4)
PY|
PY|def area_density(x):
PY|    return x - y
PY|
PY|def moment_density(x):
PY|    return x ** 3 / 3 + y ** 2 * x - 4 * y ** 3 / 3
PY|
PY|def boundary_density(x):
PY|    return x ** 2 + y ** 2
PY|
PY|def psi0(x):
PY|    return moment_density(x) - L * area_density(x)
PY|
PY|def psi1(x):
PY|    return psi0(x) + m * boundary_density(x) + T2 * x
PY|
PY|C = (8 * c ** 2 * T2 + 16 * c * T3 / 3 + 2 * T4 / 3
PY|     - L * (8 * c * m + 2 * T2) - 8 * T2 * I(y, 0, c))
PY|eq("deterministic constant from raw functional", C,
PY|   4 * c ** 2 * T2 + 16 * c * T3 / 3 + 2 * T4 / 3
PY|   - L * (8 * c * m + 2 * T2))
PY|
PY|dz = psi1(z).d("z")
PY|def dcoord(x):
PY|    return dz.sub("z", x)
PY|
PY|eq("coordinate derivative from densities", dz,
PY|   (z + m) ** 2 + v + y ** 2 - L)
PY|eq("active core pooling", psi0(z) + m * psi1(z + 1),
PY|   (1 + m) * psi1(z) + m * (kappa - L))
PY|eq("first-core diagonal endpoint", psi0(a).sub("y", a))
PY|
PY|def geometric_integrals(f, lo, hi):
PY|    return (8 * I(area_density(f), lo, hi),
PY|            8 * I(moment_density(f), lo, hi),
PY|            8 * I(boundary_density(f), lo, hi))
PY|
PY|def raw_parts(f0, tails):
PY|    A0, Q0, unused = geometric_integrals(f0, 0, a)
PY|    A1, Q1, B1 = geometric_integrals(f0 + 1, 0, a)
PY|    for f, lo, hi in tails:
PY|        aa, qq, bb = geometric_integrals(f, lo, hi)
PY|        A1, Q1, B1 = A1 + aa, Q1 + qq, B1 + bb
PY|    first = Q0 - L * A0
PY|    tail = (Q1 + m * B1 + (A1 + 8 * c ** 2) * T2
PY|            + 16 * c * T3 / 3 + 2 * T4 / 3
PY|            - L * (A1 + 8 * c * m + 2 * T2))
PY|    return first, tail
PY|
PY|def raw_value(f0, tails):
PY|    first, tail = raw_parts(f0, tails)
PY|    return first + m * tail
PY|
PY|def signed_value(f0, tails):
PY|    tail_integral = I(psi1(f0 + 1), 0, a)
PY|    for f, lo, hi in tails:
PY|        tail_integral = tail_integral + I(psi1(f), lo, hi)
PY|    return 8 * I(psi0(f0), 0, a) + 8 * m * tail_integral + m * C
PY|
PY|U = 2 * a - y
PY|k = 2 * a + 1 - y
PY|s = 2 * a + 1 - c
PY|u = a + R(1, 2)
PY|tails = [(k, a, s), (c, s, c)]
PY|endpoint = psi1(c).sub("y", c)
PY|D0 = endpoint + C.d("c") / 8
PY|eq("moving diagonal endpoint", endpoint, 2 * m * c ** 2 + T2 * c)
PY|eq("complete D0", D0,
PY|   2 * c * T2 + 2 * m * c ** 2 + 2 * T3 / 3 - m * L)
PY|eq("tail interface joins", k.sub("y", s), c)
PY|
PY|affine = {}
PY|for label, f0 in (("lower", a), ("upper", U)):
PY|    H = raw_value(f0, tails)
PY|    affine[label] = H
PY|    eq(label + " complete functional", H, signed_value(f0, tails))
PY|    da_shape = (8 * (1 + m) * I(dcoord(f0) * f0.d("a"), 0, a)
PY|                + 16 * m * I(dcoord(k), a, s))
PY|    dc_shape = 8 * m * (D0 + I(dcoord(c), s, c))
PY|    eq(label + " raw a derivative", H.d("a"), da_shape)
PY|    eq(label + " raw c derivative", H.d("c"), dc_shape)
PY|
PY|def edge_value(f0):
PY|    return raw_value(f0, [(k, a, c)]).sub("c", u)
PY|
PY|Eupper = edge_value(U)
PY|Elower = edge_value(a)
PY|Aupper = -I(dcoord(U), 0, a)
PY|Llower = I(dcoord(a), 0, a)
PY|W = a ** 2 + (1 + 2 * m) * a + kappa - L / 2
PY|eq("edge endpoint-and-corner simplification",
PY|   I(dcoord(k), a, u) + D0.sub("c", u) / 2, (1 + m) * W)
PY|eq("upper edge derivative from complete raw value",
PY|   Eupper.d("a"), 16 * (1 + m) * (m * W - Aupper))
PY|eq("lower edge derivative from complete raw value",
PY|   Elower.d("a"), 16 * (1 + m) * (m * W + Llower / 2))
PY|eq("all-upper A", Aupper,
PY|   a * (L - T2) - 3 * m * a ** 2 - 8 * a ** 3 / 3)
PY|G = 8 * a ** 3 / 3 + 4 * m * a ** 2 + (2 * T2 - L) * a
PY|G = G + m * (kappa - L / 2)
PY|eq("upper F from raw derivative", m * W - Aupper, G)
PY|eq("upper F first derivative", G.d("a"),
PY|   8 * a ** 2 + 8 * m * a + 2 * T2 - L)
PY|eq("upper F second derivative", G.d("a").d("a"), 16 * a + 8 * m)
PY|
PY|def D(x):
PY|    return 2 * x ** 2 + 2 * m * x + T2
PY|
PY|def Rfront(x):
PY|    return 4 * x ** 2 + 4 * m * x + T2
PY|
PY|Braw = I(dcoord(k), a, a + ell)
PY|lambda_ell = dcoord(k).sub("y", a + ell) + L
PY|Broot = Braw.sub("L", lambda_ell)
PY|eq("corner B after implicit root constraint", Broot,
PY|   (1 + m) * ell ** 2 - 4 * ell ** 3 / 3)
PY|Ba = Braw.d("a").sub("L", lambda_ell)
PY|eq("corner B_a from unsimplified integral", Ba, 2 * (2 * a + 1 + m) * ell)
PY|eq("corner implicit derivative consistency",
PY|   Broot.d("ell") * (2 * a + 1 + m),
PY|   (1 + m - 2 * ell) * Ba)
PY|curvature = -(1 + m) * Aupper.d("a") + m * Ba
PY|eq("normalized h_aa algebra", curvature,
PY|   (1 + m) * (-L + T2 + 6 * m * a + 8 * a ** 2)
PY|   + 2 * m * (2 * a + 1 + m) * ell)
PY|bound = curvature.sub("L", D(u)).sub("ell", R(1, 2))
PY|eq("curvature bound after strict endpoint replacements", bound,
PY|   (1 + m) * (6 * a ** 2 + (4 * m - 2) * a - R(1, 2))
PY|   + 2 * m * a)
PY|need("negative curvature rational bound",
PY|     R(6, 64) + R(1, 12) - R(1, 2) == -R(31, 96))
PY|
PY|lambda_q = D(a) + 2 * m * q + 2 * q ** 2
PY|Aq = (-I(dcoord(U), a - q, a)).sub("L", lambda_q)
PY|eq("free-branch A from integration", Aq, m * q ** 2 + 4 * q ** 3 / 3)
PY|Ffree = m * W - Aq
PY|Fa_free = m * (2 * a + 1 + 2 * m) + 2 * q * (2 * a + m)
PY|eq("free F derivative under fixed-lambda implicit constraint",
PY|   (2 * q + m) * Ffree.d("a") - (2 * a + m) * Ffree.d("q"),
PY|   (2 * q + m) * Fa_free)
PY|need("free F_a positive for positive a,m,q", positive_coefficients(Fa_free))
PY|eq("branch values match",
PY|   Ffree.sub("q", a).sub("L", Rfront(a)), G.sub("L", Rfront(a)))
PY|eq("free derivative at branch frontier", Fa_free.sub("q", a), Rfront(a))
PY|eq("upper derivative at branch frontier",
PY|   G.d("a").sub("L", Rfront(a)), Rfront(a))
PY|missing_branch_gap = (Ffree - G).sub("L", lambda_q)
PY|eq("exact missing-free-branch error", missing_branch_gap,
PY|   -(a - q) ** 2 * (m + 2 * a / 3 + 4 * q / 3))
PY|
PY|eq("full rounded-core cubic identity",
PY|   psi1(z) - psi1(r),
PY|   (z - r) * dcoord(r) + (z - r) ** 2 * ((z + 2 * r) / 3 + m))
PY|
PY|def M(n, shift):
PY|    return sum((comb(n, j) * P(shift) ** (n - j) * T[j]
PY|                for j in range(n + 1)), P())
PY|
PY|for n in range(5):
PY|    eq("memoryless shifted moment " + str(n),
PY|       (1 + m) * M(n, t), t ** n + m * M(n, t + 1))
PY|eq("complete diamond value from raw area and moments", Eupper,
PY|   (1 + m) * (2 * M(4, 2 * a) / 3 - 2 * L * M(2, 2 * a)))
PY|
PY|m0 = R(1, 10)
PY|MM = [M(n, t).sub("m", m0) for n in range(5)]
PY|Pexpr = 2 * MM[3] * MM[2] - MM[4] * MM[1]
PY|p = 250 * Pexpr
PY|eq("prescribed quintic derived from moment products", p,
PY|   250 * t ** 5 + 125 * t ** 4 + 80 * t ** 3 - 47 * t ** 2 - 48 * t + 3)
PY|
PY|def value(f, at):
PY|    return P(f).sub("t", at).scalar()
PY|
PY|lo, hi, half = R(11, 20), R(3, 5), R(1, 2)
PY|need("quintic lower endpoint", value(p, lo) == -R(147, 512))
PY|need("quintic upper endpoint", value(p, hi) == R(51, 5))
PY|need("quintic derivative at half", value(p.d("t"), half) == R(845, 8))
PY|shifted_second = p.d("t").d("t").sub("t", half + t)
PY|eq("shifted second derivative", shifted_second,
PY|   1146 + 5730 * t + 9000 * t ** 2 + 5000 * t ** 3)
PY|need("second derivative positive at and above half",
PY|     positive_coefficients(shifted_second))
PY|need("third derivative positive on nonnegative axis",
PY|     positive_coefficients(p.d("t").d("t").d("t")))
PY|need("initial signs for unique positive turning point",
PY|     value(p, 0) > 0 and value(p.d("t"), 0) < 0
PY|     and value(p.d("t").d("t"), 0) < 0)
PY|
PY|Ht = Eupper.sub("a", t / 2).sub("m", m0)
PY|St = Eupper.d("a").sub("a", t / 2).sub("m", m0)
PY|eq("diamond value is affine in lambda", Ht.d("L").d("L"))
PY|eq("exact full value zero after cross multiplication",
PY|   3 * MM[2] * Ht.sub("L", 0) + MM[4] * Ht.d("L"))
PY|eq("stationarity numerator is precisely elimination polynomial",
PY|   3 * MM[2] * St.sub("L", 0) + MM[4] * St.d("L"),
PY|   8 * (1 + m0) * Pexpr)
PY|eq("root-orientation curvature identity", p.d("t"),
PY|   250 * (6 * MM[2] ** 2 - MM[4]))
PY|need("positive moment denominators", positive_coefficients(MM[1])
PY|     and positive_coefficients(MM[2]))
PY|
PY|lower_value = value(MM[4], lo) / (3 * value(MM[2], hi))
PY|upper_value = value(MM[4], hi) / (3 * value(MM[2], lo))
PY|need("exact lower value bound",
PY|     lower_value == R(54371, 96000) and lower_value > R(5, 9))
PY|need("exact upper value bound",
PY|     upper_value == R(256, 355) and upper_value < R(3, 4))
PY|branch_gap = 2 * MM[3] - 3 * MM[1] * MM[2]
PY|eq("diamond clipping inequality numerator", branch_gap,
PY|   -t ** 3 - 3 * t ** 2 / 10 + 3 * t / 10 + R(37, 125))
PY|need("clipping numerator decreases on assigned interval",
PY|     positive_coefficients(-branch_gap.d("t").sub("t", lo + t)))
PY|need("clipping numerator stays strictly positive",
PY|     value(branch_gap, hi) == R(19, 125))
PY|need("positive candidate edge curvature bound",
PY|     2 * lo ** 2 + R(2, 5) * lo + R(6, 25) == R(213, 200)
PY|     and R(213, 200) - R(3, 4) == R(63, 200))
PY|need("strict candidate normal separation",
PY|     2 * R(31, 40) ** 2 == R(961, 800) and R(961, 800) > 1
PY|     and upper_value < 1)
PY|v0 = m0 * (1 + m0)
PY|w0 = v0 * (1 + 2 * m0)
PY|need("assigned lower value exceeds stronger necessary threshold",
PY|     R(5, 9) - 2 * v0 > 0
PY|     and (R(5, 9) - 2 * v0) ** 3 - 2 * w0 ** 2
PY|     == R(267427, 91125000))
PY|
PY|def udict(f):
PY|    out = {}
PY|    for e, coef in P(f).c.items():
PY|        if any(power for j, power in enumerate(e) if j != INDEX["t"]):
PY|            raise CheckFailure("Sturm input is not univariate in t")
PY|        out[e[INDEX["t"]]] = coef
PY|    return out
PY|
PY|def upoly(coefficients):
PY|    return sum((coef * t ** degree for degree, coef in coefficients.items()), P())
PY|
PY|def remainder(numerator, denominator):
PY|    work = udict(numerator)
PY|    den = udict(denominator)
PY|    if not den:
PY|        raise CheckFailure("zero Sturm divisor")
PY|    degree_den = max(den)
PY|    while work and max(work) >= degree_den:
PY|        tick()
PY|        degree_work = max(work)
PY|        shift = degree_work - degree_den
PY|        factor = work[degree_work] / den[degree_den]
PY|        for degree, coef in den.items():
PY|            key = degree + shift
PY|            new_value = work.get(key, R(0)) - factor * coef
PY|            if new_value:
PY|                work[key] = new_value
PY|            else:
PY|                work.pop(key, None)
PY|    return upoly(work)
PY|
PY|def sturm_chain(f):
PY|    chain = [f, f.d("t")]
PY|    while chain[-1].c:
PY|        rem = remainder(chain[-2], chain[-1])
PY|        if not rem.c:
PY|            break
PY|        chain.append(-rem)
PY|    return chain
PY|
PY|def sign(number):
PY|    return (number > 0) - (number < 0)
PY|
PY|def variations(signs):
PY|    signs = [s for s in signs if s]
PY|    return sum(left * right < 0 for left, right in zip(signs, signs[1:]))
PY|
PY|chain = sturm_chain(p)
PY|need("quintic squarefree", max(udict(chain[-1])) == 0)
PY|
PY|def variation_at(at):
PY|    return variations([sign(value(f, at)) for f in chain])
PY|
PY|def roots_between(left, right):
PY|    return variation_at(left) - variation_at(right)
PY|
PY|def root_only_accepts(left, right):
PY|    return roots_between(left, right) == 1
PY|
PY|def minimum_root_accepts(left, right):
PY|    return (root_only_accepts(left, right)
PY|            and value(p, left) < 0 < value(p, right))
PY|
PY|variation_infinity = variations([
PY|    sign(udict(f)[max(udict(f))]) for f in chain
PY|])
PY|need("exactly two positive quintic roots",
PY|     variation_at(0) - variation_infinity == 2)
PY|need("one earlier decreasing root", roots_between(0, lo) == 1)
PY|need("one assigned increasing root", roots_between(lo, hi) == 1)
PY|need("assigned root passes orientation gate", minimum_root_accepts(lo, hi))
PY|
PY|H = affine["upper"]
PY|first, tail = raw_parts(U, tails)
PY|reject_eq("omit-b", first + (1 + m) * tail, H,
PY|          "geometric mixture coefficient becomes 1 rather than b")
PY|reject_eq("omit-tail-constant", H - m * C, H,
PY|          "complete deterministic geometric-tail contribution is lost")
PY|reject_eq("omit-moving-endpoint", H.d("c") - 8 * m * endpoint, H.d("c"),
PY|          "terminal-height derivative 8*m*psi1(c,c) is missing")
PY|reject_eq("omit-active-core-offset", H - 8 * m * a * (kappa - L), H,
PY|          "required active-core pooling offset is missing")
PY|normal = H.d("c").sub("c", u)
PY|eq("edge normal on positive-gradient affine stratum", normal,
PY|   8 * m * D0.sub("c", u))
PY|reject_eq("flip-normal", -normal, normal,
PY|          "right derivative has the opposite normal orientation")
PY|reject_eq("omit-free-branch",
PY|          Ffree.sub("L", lambda_q), G.sub("L", lambda_q),
PY|          "nonzero -(a-q)^2*(m+2*a/3+4*q/3) discrepancy")
PY|reject_accept("decreasing-root-as-minimum",
PY|              root_only_accepts(0, lo), minimum_root_accepts(0, lo),
PY|              "full value and stationarity do not replace positive curvature")
PY|
PY|need("all seven intended mutation classes discriminated", mutations == 7)
PY|need("finite execution bound", monotonic() - started < 55)
PY|print("ENDPOINTS", value(p, lo), value(p, hi))
PY|print("VALUE_BOUNDS", lower_value, upper_value)
PY|print("ASSERTIONS", checks, "INTENDED_MUTATION_CLASSES", mutations)
PY|print("SCOPE exact finite algebra; assigned synthetic candidate only")
PY|print("LIMIT not a continuum proof, actual-regime existence, or adoption")
PY|print("ELAPSED_SECONDS", monotonic() - started)

## 8. Disposition and remaining assurance boundary

The written reconstruction supports the load-bearing algebra in the conditional argument:

- complete \(H\), including the geometric weight and deterministic tail constant;
- both scalar derivatives and the edge derivative;
- corner \(A/B\), implicit \(B_a\), and the negative-curvature estimate;
- free/upper matching and strict positive free-branch derivative;
- complete diamond value and rounded-core correction;
- the assigned quintic, endpoint arithmetic, root orientation, clipping inequality, value bounds, and strict normal.

**No scientific execution result is supplied.** The independent finite gate remains **NOT RUN** until an authorized parent execution actually completes and its source, argv, output, exit status, and elapsed time are recorded. The source above must not be described as having passed merely because it has been returned.

Actual-cutoff-two existence remains a hypothesis. Conditional scalar uniqueness is not automatically adopted. No global sufficiency theorem, full parameter interval, original-target completion, family-independent review, human verification, formal/kernel verification, or novelty claim follows from this return. The earlier penalty-sign MAJOR is not withdrawn.

**overall_correctness:** correct

**explanation:** I found no new algebraic defect in the supplied conditional manuscript within this finite-check assignment’s written reconstruction. The independently authored checker is returned in full but was not executed; this verdict is not parent adoption or evidence of actual-regime existence.

**confidence:** 0.88