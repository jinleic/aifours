# author-candidate-v1.md — Independent exact finite inverse-source host and arbitrary-host nonextension checks

**Wave:** f423-semigroup-inverse-host-independent-exact-finite-check  
**Role:** FINITE  
**Status:** **UNREVIEWED AUTHOR CANDIDATE; EXECUTABLE CHECK NOT RUN.**

This return supplies complete selected-instance derivations and independent, runnable standard-library code. The active reviewer tool restriction permits read-only patch inspection but prohibits scientific execution and file edits. I therefore did not execute or materialize the code. No machine-verification pass, measured runtime, child-native timestamp, independent hash calculation, parent acceptance, independent-family acceptance, human/kernel verification, or novelty result is claimed.

**Written selected-instance audit:** 0 FATAL / 0 MAJOR / 0 MINOR findings. This is not a review verdict on the universally quantified inverse-source theorem.

## 1. Inputs, chronology, and provenance

The assigned manifest and receipt are:

- Manifest SHA-256: `d4c6b5b2a3b5df702fc5492c6e022d8dea70ed60a03884d9f2a86a93e6cf0988`
- Receipt SHA-256: `65d8f02747639d74d7da2854be062179bac2031ecad7a461580b41c1beb8bea6`
- Literal packet SHA-256: `176f15395aa72e91474617316cc862e985a633f9e26fa60670b87b0b4b8f4a47`
- S1 author body SHA-256: `a9e535a45a44c7638c4db80d4ae2a4c422e13d15fd030d65768f6b4ab143d850`

All hash/byte/LF agreement and the clock `2026-10-30T10:56:06-0700 PDT` are **parent observations**, supplied in `parent-live-metadata-supply-v1.json`. They are not my own hash execution, native start, or completion observations. The S1 metadata records 719 LF characters and selects logical lines 1–720; I do not interpret those different quantities as a discrepancy.

Before scientific development, I read:

1. Required memory and applicable procedural skills.
2. The complete manifest, freeze receipt, dispatch receipt, and parent metadata supply.
3. All seven named permission/status controls through their endings, using them only for permissions and exclusions.
4. The complete literal packet, in order, in raw windows 1–100, 101–200, 201–300, 301–400, 401–500, 501–600, 601–700, and 701–722.
5. The separately pinned S1 ending, lines 701–720.
6. The direct consuming physical-host multiplication check at S1 lines 337–356.

The scoped `git diff` produced no output. No build, test, linter, formatter, scientific interpreter, external-model CLI, installation, deletion, network calculation, or repository write occurred.

The examples and checker below were developed after reading the assigned written definitions. This is independent implementation, not blind reconstruction. No author code, current sibling output, excluded scientific payload, or linked predecessor scientific body was used. No public-source theorem is imported.

## 2. Exact finite claims and quantifiers

For the primary example, the statements below concern exactly:

- All eight elements of \(S=\mathcal P(\{0,1\})\rtimes C_2\).
- Every one of its 64 ordered pairs and 512 ordered triples.
- Every candidate inverse among its eight elements.
- Both sandwich entries \(p\in C_2\), including nonidentity \(p=1\).
- All eight points of \(X=C_2\times E(S)\).
- All 256 subsets of \(X\), including the empty and full subsets.
- Both action elements and all \(256^2\) ordered pairs of subsets.
- All 512 physical-host elements, for the projection-purity square check.
- All 16 functions \(C_4\to C_2\), not merely a preselected list of group homomorphisms.

The additional \(C_3\) instance is a selected negative-control discriminator. It has 24 source elements and a 24-point coordinate set. Its entire \(2^{24}\)-element powerset host is **not** enumerated.

These finite claims do not establish the theorem for arbitrary inverse semigroups, all regular sources, canonical hosts, or unspecified additional host-admissibility conditions.

## 3. Primary non-group inverse source

Represent a subset of \(\{0,1\}\) by its two-bit mask \(A\in\{0,1,2,3\}\). Let \(\theta\) swap the two atoms. Thus

\[
\theta(0)=0,\quad \theta(1)=2,\quad
\theta(2)=1,\quad \theta(3)=3.
\]

Take

\[
S=\{(A,g):A\in\{0,1,2,3\},\ g\in C_2\}
\]

with

\[
(A,g)(B,h)=\bigl(A\cap\theta^g(B),\,g+h\bigr),
\]

where subset intersection is bitwise AND and the second coordinate is modulo 2.

Label the elements \(s_{2A+g}=(A,g)\). The complete multiplication table is:

| Product | \(s_0\) | \(s_1\) | \(s_2\) | \(s_3\) | \(s_4\) | \(s_5\) | \(s_6\) | \(s_7\) |
|---|---|---|---|---|---|---|---|---|
| \(s_0\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) |
| \(s_1\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) |
| \(s_2\) | \(s_0\) | \(s_1\) | \(s_2\) | \(s_3\) | \(s_0\) | \(s_1\) | \(s_2\) | \(s_3\) |
| \(s_3\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_3\) | \(s_2\) | \(s_3\) | \(s_2\) |
| \(s_4\) | \(s_0\) | \(s_1\) | \(s_0\) | \(s_1\) | \(s_4\) | \(s_5\) | \(s_4\) | \(s_5\) |
| \(s_5\) | \(s_1\) | \(s_0\) | \(s_5\) | \(s_4\) | \(s_1\) | \(s_0\) | \(s_5\) | \(s_4\) |
| \(s_6\) | \(s_0\) | \(s_1\) | \(s_2\) | \(s_3\) | \(s_4\) | \(s_5\) | \(s_6\) | \(s_7\) |
| \(s_7\) | \(s_1\) | \(s_0\) | \(s_5\) | \(s_4\) | \(s_3\) | \(s_2\) | \(s_7\) | \(s_6\) |

Associativity follows directly because both parenthesizations give

\[
\left(A\cap\theta^g(B)\cap\theta^{g+h}(C),\,g+h+k\right).
\]

The identity is \(s_6=(3,0)\). The inverse is

\[
(A,g)^{-1}=(\theta^{-g}(A),-g).
\]

To check uniqueness, suppose \(t=(B,h)\) satisfies \(sts=s\) and \(tst=t\). The group coordinates force \(h=-g\). The subset coordinates then force

\[
A\subseteq\theta^g(B),\qquad B\subseteq\theta^{-g}(A),
\]

and hence \(B=\theta^{-g}(A)\).

Consequently,

\[
ss^{-1}=(A,0),\qquad
s^{-1}s=(\theta^{-g}(A),0).
\]

The idempotents are exactly

\[
E(S)=\{(0,0),(1,0),(2,0),(3,0)\}.
\]

They commute because their multiplication is intersection. There is more than one idempotent, so this is not a group. In particular, \((0,0)\) is not a global absorbing zero: multiplying it by an element with group coordinate 1 gives \((0,1)\).

The inverse-index list in the displayed element order is

\[
(0,1,2,5,4,3,6,7).
\]

The normalized quotient

\[
\bar q(A,g)=g
\]

is onto and a homomorphism, and

\[
\bar q^{-1}(0)=E(S).
\]

Thus it is idempotent-pure.

## 4. Independently computed \(\iota\), \(R_s\), action, and physical embedding

### 4.1 Coordinate convention

Index \(X=C_2\times E(S)\) by

\[
\operatorname{index}(g,(e,0))=4g+e.
\]

From the assigned definition,

\[
\iota(A,g)=\left(g,(\theta^{-g}(A),0)\right).
\]

Its point-index list in source order is

\[
(0,4,1,6,2,5,3,7),
\]

which is a permutation of all eight points.

The action on points is

\[
a\cdot(g,e)=(a+g,e).
\]

For \(a=1\), this swaps the two four-point layers. As a bitset action on \(C=\mathcal P(X)\), it swaps the low and high nibbles of an eight-bit mask.

This is a nontrivial permutation action. Each point permutation induces a bijection on all 256 subsets. For every \(U,V\subseteq X\),

\[
a(U\cap V)=aU\cap aV.
\]

Its inverse is the permutation for \(-a\). Thus these are actual semilattice automorphisms, including at \(U=\varnothing\) and \(U=X\).

### 4.2 The exact range-ideal coordinates

For \(s=(A,g)\), its range idempotent is \(e_s=(A,0)\). Therefore

\[
e_s(B,h)=(B,h)\quad\Longleftrightarrow\quad B\subseteq A.
\]

The assigned definition gives

\[
R_s=\{\iota(B,h):B\subseteq A,\ h\in C_2\}.
\]

This depends on \(A\), not on \(g\). Its two layers are

\[
R_A=
\{(0,e):e\subseteq A\}
\ \cup\
\{(1,e):e\subseteq\theta(A)\}.
\]

The complete coordinates are:

| Element | Inverse | Domain-idempotent mask | \(\iota\) index | \(R_s\) mask |
|---|---|---:|---:|---:|
| \((0,0)\) | \((0,0)\) | 0 | 0 | `0x11` |
| \((0,1)\) | \((0,1)\) | 0 | 4 | `0x11` |
| \((1,0)\) | \((1,0)\) | 1 | 1 | `0x53` |
| \((1,1)\) | \((2,1)\) | 2 | 6 | `0x53` |
| \((2,0)\) | \((2,0)\) | 2 | 2 | `0x35` |
| \((2,1)\) | \((1,1)\) | 1 | 5 | `0x35` |
| \((3,0)\) | \((3,0)\) | 3 | 3 | `0xff` |
| \((3,1)\) | \((3,1)\) | 3 | 7 | `0xff` |

Even the empty-subset source elements have nonempty \(R_s\): their mask is `0x11`, not zero.

For every \(A,B\),

\[
R_A\cap R_B=R_{A\cap B},\qquad
gR_B=R_{\theta^g(B)}.
\]

Hence, for all 64 source pairs,

\[
R_{st}=R_s\cap\bar q(s)R_t.
\]

### 4.3 Both physical sandwich conventions

For either \(p\in C_2\), let \(D_p\) have physical actor-coordinate product

\[
h\star_p k=h+p+k.
\]

Its identity and unique idempotent are \(-p\). The normalization is

\[
\rho_p(h)=h+p.
\]

Use the prescribed physical quotient

\[
q_p(A,g)=g-p.
\]

Then

\[
q_p(st)=q_p(s)\star_p q_p(t),\qquad
\rho_pq_p(A,g)=g.
\]

In particular, \(q_p\) is onto and idempotent-pure for both \(p=0\) and the nonidentity sandwich entry \(p=1\).

The literal physical host consumes its first actor coordinate by

\[
(U,h)(V,k)=
\left(U\cap (h+p)V,\ h+p+k\right).
\]

Define

\[
F_p(A,g)=(R_A,g-p).
\]

Its actual consumed twist is \(h+p=g\), so

\[
\begin{aligned}
F_p(A,g)F_p(B,h)
&=\left(R_A\cap gR_B,\ g+h-p\right)\\
&=\left(R_{A\cap\theta^g(B)},g+h-p\right)\\
&=F_p\bigl((A,g)(B,h)\bigr).
\end{aligned}
\]

The four \(R_A\) masks are distinct, and the actor coordinate separates the two possible \(g\)'s. Thus \(F_p\) is injective and preserves \(q_p\) exactly.

For all 512 host elements, an actor-idempotent coordinate has consumed twist zero, so its square preserves the band coordinate. Conversely, a host idempotent projects to an actor idempotent. This also verifies projection purity for the full finite host, not just for the eight-element source image.

## 5. Independent arbitrary-host nonextension witness

Use the initial actor \(A=C_4\), singleton band \(B=\{*\}\), and trivial band action. Its physical host is the group host

\[
(*,a)(*,b)=(*,a+b\bmod4).
\]

Let the source be \(K=\{0,2\}\le C_4\), and set

\[
r(0)=0,\quad r(2)=2,\qquad
q(0)=0,\quad q(2)=1\in C_2.
\]

Then:

- \(K\) is a regular inverse semigroup, with sole idempotent 0.
- \(f(s)=(*,s)\) is an actual initial-host embedding.
- \(r\) is its actor map.
- \(q\) is an onto isomorphism and is idempotent-pure.
- \(\ker r=\ker q=\{(0,0),(2,2)\}\), so kernel inclusion holds with equality.
- \(r(K)=\{0,2\}\ne C_4\).

All 16 functions \(C_4\to C_2\) are covered by enumeration of their four values. Exactly two satisfy every homomorphism equation:

\[
(0,0,0,0),\qquad (0,1,0,1).
\]

Both send 2 to 0. Thus neither restricts to the prescribed \(q\).

Equivalently, any homomorphism must satisfy

\[
\phi(2)=\phi(1+1)=2\phi(1)=0,
\]

whereas matching requires \(\phi(2)=1\).

Therefore there is no matching actor extension, pure or otherwise, and no whole-initial-host embedding that is actor-respecting through such an extension.

There is nevertheless the separate source-only embedding

\[
F_0:K\hookrightarrow T(\{*\},C_2),\qquad
F_0(s)=(*,q(s)).
\]

It is injective and multiplicative because \(q\) is an isomorphism. The whole-host obstruction is therefore **not** an arbitrary source-embedding obstruction.

## 6. Meaningful negative controls

Each control below preserves specified weaker properties and fails a named required invariant.

1. **Use the second factor’s group coordinate as the twist.**  
   Take \(s=(3,1)\), \(t=(1,0)\). Their product is \((2,1)\). The correct band mask is `0x35`; the second-factor twist produces `0x53`. The source, quotient, action, and separate image injectivity remain unchanged.

2. **Use the range idempotent in \(\iota\), instead of the domain idempotent.**  
   The mutant coordinate is \(\iota'(A,g)=(g,A)\), still a bijection on the eight points. The derived mutant \(R'_A\) masks are `0x11`, `0x33`, `0x55`, `0xff`. For the same pair \(s=(3,1)\), \(t=(1,0)\), the required mask is `0x55`, whereas the host product gives `0x33`. Thus coordinate injectivity alone does not establish the needed multiplication identity.

3. **Use the domain principal ideal for \(R_s\), instead of the range principal ideal.**  
   Retain the correct \(\iota\). For \(s=(3,1)\), \(t=(1,0)\), the mutant required mask is `0x53`, but its host product gives `0x35`. The mutant source map is still injective; multiplicativity fails.

4. **Omit \(p\) from the physical twist when \(p=1\).**  
   Take \(s=(3,0)\), \(t=(1,0)\). The physical actor of \(s\) is 1, but its correct twist is \(1+p=0\). Using the physical actor coordinate alone changes the required `0x53` to `0x35`. The actor-coordinate product itself remains correct.

5. **Invert the twist.**  
   This mutation is invisible on \(C_2\), since \(g=-g\). It must not be counted as a successful discriminating negative control there.  
   To distinguish it, independently take
   \[
   S_3=\mathcal P(\{0,1,2\})\rtimes C_3
   \]
   with cyclic rotation of the atoms. For \(s=(\{0,1,2\},1)\), \(t=(\{0\},0)\), the correct product has subset \(\{1\}\). The inverse twist produces the \(R\)-coordinate for \(\{2\}\). These are distinct. The supplied code checks all 576 pairs for the correct identity before requiring this mutant’s rejection.

6. **Omit idempotent purity using the trivial target.**  
   On the primary eight-element source, the constant quotient onto the trivial group is onto and multiplicative but not pure: \((0,1)\) is not idempotent and maps to an idempotent. Its \(\iota\) collapses \((0,0)\) and \((0,1)\); the corresponding \(F\) also collapses them. Rejection is required separately for purity, coordinate injectivity, and source-image injectivity.

7. **Alter the subgroup quotient.**  
   Replace \(q(2)=1\) by \(q'(2)=0\), retaining target \(C_2\). This remains a homomorphism and retains kernel inclusion, but loses surjectivity and purity. Both \(C_4\to C_2\) homomorphisms now extend it. Thus an indiscriminate “no extension” checker must reject this mutated conclusion.  
   With trivial target instead, the altered quotient is onto but not pure and has a unique extension from \(C_4\). This separately distinguishes loss of purity from loss of surjectivity.

8. **Extension need not be pure when it exists.**  
   For the selected contrast \(K=\{0,3\}\le C_6\), \(q(3)=1\in C_2\), a matching extension exists: parity. Its kernel is \(\{0,2,4\}\), so it is not pure.  
   For \(H=K=C_2\) and \(q\) the identity, the matching extension is pure. These are selected positive controls, not a finite proof of the entire subgroup-family theorem.

## 7. Complete independent runnable checker — NOT RUN

Suggested invocation after Main materializes the source:

`python3 -B f423_finite_check.py`

The program uses only the standard library, has no application file access, network access, child processes, installation, deletion, or external mutation, and uses a cooperative 55-second calculation deadline. It does not allocate the \(C_3\) powerset host. No successful completion within that deadline has been observed.

The source below is supplied unfenced. The BEGIN/END marker lines are not part of the Python source.

BEGIN PYTHON SOURCE

import itertools
import time


START = time.monotonic()
DEADLINE = START + 55.0


class InvariantFailure(RuntimeError):
    def __init__(self, invariant, witness=None):
        self.invariant = invariant
        self.witness = witness
        super().__init__(invariant + ": " + repr(witness))


class CalculationDeadline(RuntimeError):
    pass


def tick():
    if time.monotonic() >= DEADLINE:
        raise CalculationDeadline("55-second cooperative calculation limit")


def require(condition, invariant, witness=None):
    if not condition:
        raise InvariantFailure(invariant, witness)


def negative(invariant, operation):
    try:
        operation()
    except InvariantFailure as error:
        require(
            error.invariant == invariant,
            "NEGATIVE_CONTROL_WRONG_REASON",
            (invariant, error.invariant, error.witness),
        )
        print("REJECTED", invariant, repr(error.witness))
        return
    raise InvariantFailure("NEGATIVE_CONTROL_NOT_REJECTED", invariant)


def rotate(mask, g, n):
    g %= n
    result = 0
    for atom in range(n):
        if mask & (1 << atom):
            result |= 1 << ((atom + g) % n)
    return result


def source_model(n):
    width = 1 << n
    source = tuple((a, g) for a in range(width) for g in range(n))
    idempotents = tuple((a, 0) for a in range(width))

    def multiply(s, t):
        return (
            s[0] & rotate(t[0], s[1], n),
            (s[1] + t[1]) % n,
        )

    def inverse(s):
        return (rotate(s[0], -s[1], n), (-s[1]) % n)

    return source, idempotents, multiply, inverse


def validate_source(n, source, idempotents, multiply, inverse):
    universe = set(source)
    expected_e = set(idempotents)
    identity = ((1 << n) - 1, 0)

    require(len(source) == n * (1 << n), "SOURCE_CARDINALITY", n)
    require(
        {s for s in source if multiply(s, s) == s} == expected_e,
        "SOURCE_IDEMPOTENTS",
    )
    require(len(expected_e) > 1, "SOURCE_NON_GROUP")
    require({s[1] for s in source} == set(range(n)), "Q_ONTO")

    for s in source:
        tick()
        si = inverse(s)
        require(si in universe, "INVERSE_CLOSURE", s)
        require(inverse(si) == s, "INVERSE_INVOLUTION", s)
        require(multiply(multiply(s, si), s) == s, "INVERSE_FIRST", s)
        require(multiply(multiply(si, s), si) == si, "INVERSE_SECOND", s)
        require(multiply(s, si) in expected_e, "RANGE_IDEMPOTENT", s)
        require(multiply(si, s) in expected_e, "DOMAIN_IDEMPOTENT", s)
        require(
            multiply(identity, s) == s and multiply(s, identity) == s,
            "SOURCE_IDENTITY",
            s,
        )
        candidates = tuple(
            t for t in source
            if multiply(multiply(s, t), s) == s
            and multiply(multiply(t, s), t) == t
        )
        require(candidates == (si,), "INVERSE_UNIQUE", (s, candidates))
        require((s[1] == 0) == (s in expected_e), "NORMALIZED_Q_PURITY", s)

        for t in source:
            st = multiply(s, t)
            require(st in universe, "SOURCE_CLOSURE", (s, t))
            require(
                inverse(st) == multiply(inverse(t), inverse(s)),
                "INVERSE_ANTIMULTIPLICATIVE",
                (s, t),
            )
            require(
                st[1] == (s[1] + t[1]) % n,
                "NORMALIZED_Q_HOMOMORPHISM",
                (s, t),
            )
            for u in source:
                require(
                    multiply(st, u) == multiply(s, multiply(t, u)),
                    "SOURCE_ASSOCIATIVITY",
                    (s, t, u),
                )

    for e in idempotents:
        for f in idempotents:
            require(
                multiply(e, f) == multiply(f, e),
                "IDEMPOTENTS_COMMUTE",
                (e, f),
            )


def make_iota(n, multiply, inverse, use_range=False, forget_group=False):
    width = 1 << n

    def coordinate(s):
        if use_range:
            e = multiply(s, inverse(s))
        else:
            e = multiply(inverse(s), s)
        g = 0 if forget_group else s[1]
        return g * width + e[0]

    return coordinate


def derive_ranges(source, multiply, inverse, coordinate, use_domain=False):
    ranges = {}
    for s in source:
        tick()
        if use_domain:
            e = multiply(inverse(s), s)
        else:
            e = multiply(s, inverse(s))
        mask = 0
        for x in source:
            if multiply(e, x) == x:
                mask |= 1 << coordinate(x)
        ranges[s] = mask
    return ranges


def shift(mask, g, n):
    width = 1 << n
    result = 0
    for point in range(n * width):
        if mask & (1 << point):
            layer, e = divmod(point, width)
            image = ((layer + g) % n) * width + e
            result |= 1 << image
    return result


def validate_action(n, enumerate_whole_band):
    width = 1 << n
    points = n * width
    point_universe = set(range(points))

    for g in range(n):
        tick()
        permutation = tuple(
            ((point // width + g) % n) * width + point % width
            for point in range(points)
        )
        require(set(permutation) == point_universe, "POINT_PERMUTATION", g)
        for point in range(points):
            singleton = 1 << point
            require(
                shift(singleton, g, n) == 1 << permutation[point],
                "POINT_ACTION_IMPLEMENTATION",
                (g, point),
            )
            for h in range(n):
                require(
                    shift(shift(singleton, h, n), g, n)
                    == shift(singleton, (g + h) % n, n),
                    "POINT_ACTION_GROUP_LAW",
                    (g, h, point),
                )

    if not enumerate_whole_band:
        return

    band_size = 1 << points
    transforms = tuple(
        tuple(shift(mask, g, n) for mask in range(band_size))
        for g in range(n)
    )

    for g in range(n):
        for u in range(band_size):
            tick()
            require(transforms[0][u] == u, "BAND_ACTION_IDENTITY", u)
            require(
                transforms[(-g) % n][transforms[g][u]] == u,
                "BAND_ACTION_INVERSE",
                (g, u),
            )
            for v in range(band_size):
                require(
                    transforms[g][u & v]
                    == (transforms[g][u] & transforms[g][v]),
                    "BAND_ACTION_INTERSECTION",
                    (g, u, v),
                )


def check_range_identity(n, source, multiply, ranges, twist, invariant):
    for s in source:
        tick()
        for t in source:
            expected = ranges[multiply(s, t)]
            actual = ranges[s] & shift(ranges[t], twist(s, t), n)
            require(
                actual == expected,
                invariant,
                (s, t, actual, expected),
            )


def check_purity(source, multiply, target_idempotents, quotient, invariant):
    for s in source:
        require(
            (quotient(s) in target_idempotents) == (multiply(s, s) == s),
            invariant,
            s,
        )


def validate_physical_c2(source, multiply, inverse, ranges, p):
    def q(s):
        return (s[1] - p) % 2

    def actor_multiply(h, k):
        return (h + p + k) % 2

    def physical_multiply(left, right):
        u, h = left
        v, k = right
        return (
            u & shift(v, (h + p) % 2, 2),
            actor_multiply(h, k),
        )

    actor_e = {
        h for h in range(2) if actor_multiply(h, h) == h
    }
    require(actor_e == {(-p) % 2}, "PHYSICAL_ACTOR_IDEMPOTENTS", p)
    require({q(s) for s in source} == {0, 1}, "PHYSICAL_Q_ONTO", p)
    check_purity(source, multiply, actor_e, q, "PHYSICAL_Q_PURITY")

    for h, k, ell in itertools.product(range(2), repeat=3):
        require(
            actor_multiply(actor_multiply(h, k), ell)
            == actor_multiply(h, actor_multiply(k, ell)),
            "PHYSICAL_ACTOR_ASSOCIATIVITY",
            (p, h, k, ell),
        )

    def physical_iota(s):
        domain = multiply(inverse(s), s)
        return ((q(s) + p) % 2) * 4 + domain[0]

    physical_ranges = derive_ranges(
        source, multiply, inverse, physical_iota
    )
    require(
        physical_ranges == ranges,
        "SANDWICH_COORDINATE_CONVERSION",
        p,
    )

    image = {s: (physical_ranges[s], q(s)) for s in source}
    require(
        len(set(image.values())) == len(source),
        "PHYSICAL_F_INJECTIVE",
        p,
    )

    for s in source:
        tick()
        require(image[s][1] == q(s), "EXACT_ACTOR_PROJECTION", (p, s))
        for t in source:
            require(
                q(multiply(s, t)) == actor_multiply(q(s), q(t)),
                "PHYSICAL_Q_HOMOMORPHISM",
                (p, s, t),
            )
            require(
                physical_multiply(image[s], image[t])
                == image[multiply(s, t)],
                "PHYSICAL_HOST_MULTIPLICATION",
                (p, s, t),
            )

    for u in range(256):
        tick()
        for h in range(2):
            host_element = (u, h)
            require(
                (physical_multiply(host_element, host_element) == host_element)
                == (h in actor_e),
                "WHOLE_HOST_PROJECTION_PURITY",
                (p, u, h),
            )

    print(
        "PRIMARY_PHYSICAL",
        "p=", p,
        "source_image=", len(image),
        "pair_products=", len(source) ** 2,
        "host_elements=", 512,
    )


def primary_checks():
    source, idempotents, multiply, inverse = source_model(2)
    validate_source(2, source, idempotents, multiply, inverse)
    validate_action(2, True)

    expected_table = (
        (0, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 0),
        (0, 1, 2, 3, 0, 1, 2, 3),
        (1, 0, 1, 0, 3, 2, 3, 2),
        (0, 1, 0, 1, 4, 5, 4, 5),
        (1, 0, 5, 4, 1, 0, 5, 4),
        (0, 1, 2, 3, 4, 5, 6, 7),
        (1, 0, 5, 4, 3, 2, 7, 6),
    )
    index = {s: i for i, s in enumerate(source)}
    actual_table = tuple(
        tuple(index[multiply(s, t)] for t in source)
        for s in source
    )
    require(actual_table == expected_table, "EXPLICIT_SOURCE_TABLE")
    require(
        tuple(index[inverse(s)] for s in source)
        == (0, 1, 2, 5, 4, 3, 6, 7),
        "EXPLICIT_INVERSE_TABLE",
    )

    coordinate = make_iota(2, multiply, inverse)
    require(
        tuple(coordinate(s) for s in source)
        == (0, 4, 1, 6, 2, 5, 3, 7),
        "EXPLICIT_IOTA_TABLE",
    )
    require(
        {coordinate(s) for s in source} == set(range(8)),
        "IOTA_EXACT_POINT_UNIVERSE",
    )

    ranges = derive_ranges(source, multiply, inverse, coordinate)
    require(
        tuple(ranges[s] for s in source)
        == (0x11, 0x11, 0x53, 0x53, 0x35, 0x35, 0xff, 0xff),
        "EXPLICIT_RANGE_TABLE",
    )
    require(all(ranges[s] != 0 for s in source), "RANGES_NONEMPTY")
    require(
        shift(ranges[(1, 0)], 1, 2) == ranges[(2, 0)]
        and ranges[(1, 0)] != ranges[(2, 0)],
        "NONTRIVIAL_ACTION_ON_SOURCE_COORDINATES",
    )
    check_range_identity(
        2, source, multiply, ranges,
        lambda s, t: s[1],
        "CORRECT_C2_RANGE_IDENTITY",
    )

    for p in (0, 1):
        validate_physical_c2(source, multiply, inverse, ranges, p)

    negative(
        "SECOND_FACTOR_TWIST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, ranges,
            lambda s, t: t[1],
            "SECOND_FACTOR_TWIST_MULTIPLICATION",
        ),
    )

    wrong_coordinate = make_iota(
        2, multiply, inverse, use_range=True
    )
    require(
        len({wrong_coordinate(s) for s in source}) == 8,
        "RANGE_COORDINATE_MUTANT_STILL_INJECTIVE",
    )
    wrong_ranges = derive_ranges(
        source, multiply, inverse, wrong_coordinate
    )
    require(
        len({(wrong_ranges[s], s[1]) for s in source}) == 8,
        "RANGE_COORDINATE_MUTANT_F_STILL_INJECTIVE",
    )
    negative(
        "RANGE_COORDINATE_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, wrong_ranges,
            lambda s, t: s[1],
            "RANGE_COORDINATE_HOST_MULTIPLICATION",
        ),
    )

    domain_ranges = derive_ranges(
        source, multiply, inverse, coordinate, use_domain=True
    )
    require(
        len({(domain_ranges[s], s[1]) for s in source}) == 8,
        "DOMAIN_IDEAL_MUTANT_F_STILL_INJECTIVE",
    )
    negative(
        "DOMAIN_IDEAL_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, domain_ranges,
            lambda s, t: s[1],
            "DOMAIN_IDEAL_HOST_MULTIPLICATION",
        ),
    )

    negative(
        "OMITTED_SANDWICH_TWIST",
        lambda: check_range_identity(
            2, source, multiply, ranges,
            lambda s, t: (s[1] - 1) % 2,
            "OMITTED_SANDWICH_TWIST",
        ),
    )

    check_range_identity(
        2, source, multiply, ranges,
        lambda s, t: (-s[1]) % 2,
        "C2_INVERSE_TWIST_IS_IDENTICAL",
    )
    print("NONDISCRIMINATING_CONTROL", "inverse twist on C2")

    trivial_q = lambda s: 0
    require({trivial_q(s) for s in source} == {0}, "TRIVIAL_Q_ONTO")
    require(
        all(
            trivial_q(multiply(s, t)) == 0
            for s in source for t in source
        ),
        "TRIVIAL_Q_HOMOMORPHISM",
    )
    negative(
        "TRIVIAL_Q_PURITY",
        lambda: check_purity(
            source, multiply, {0}, trivial_q, "TRIVIAL_Q_PURITY"
        ),
    )

    collapsed_coordinate = make_iota(
        2, multiply, inverse, forget_group=True
    )
    negative(
        "TRIVIAL_IOTA_INJECTIVE",
        lambda: require(
            len({collapsed_coordinate(s) for s in source}) == len(source),
            "TRIVIAL_IOTA_INJECTIVE",
        ),
    )
    collapsed_ranges = derive_ranges(
        source, multiply, inverse, collapsed_coordinate
    )
    negative(
        "TRIVIAL_F_INJECTIVE",
        lambda: require(
            len({(collapsed_ranges[s], 0) for s in source}) == len(source),
            "TRIVIAL_F_INJECTIVE",
        ),
    )


def inverse_twist_c3_control():
    source, idempotents, multiply, inverse = source_model(3)
    validate_source(3, source, idempotents, multiply, inverse)
    validate_action(3, False)

    coordinate = make_iota(3, multiply, inverse)
    require(
        {coordinate(s) for s in source} == set(range(24)),
        "C3_IOTA_EXACT_POINT_UNIVERSE",
    )
    ranges = derive_ranges(source, multiply, inverse, coordinate)
    require(
        len({(ranges[s], s[1]) for s in source}) == 24,
        "C3_CORRECT_F_INJECTIVE",
    )
    check_range_identity(
        3, source, multiply, ranges,
        lambda s, t: s[1],
        "CORRECT_C3_RANGE_IDENTITY",
    )

    s = (7, 1)
    t = (1, 0)
    require(multiply(s, t) == (2, 1), "C3_SELECTED_PRODUCT")
    require(
        ranges[s] & shift(ranges[t], 1, 3) == ranges[(2, 1)],
        "C3_SELECTED_CORRECT_TWIST",
    )
    require(
        ranges[s] & shift(ranges[t], -1, 3) == ranges[(4, 1)],
        "C3_SELECTED_REVERSED_TWIST",
    )
    require(
        ranges[(2, 1)] != ranges[(4, 1)],
        "C3_CONTROL_DISCRIMINATES",
    )

    negative(
        "INVERSE_TWIST_C3_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            3, source, multiply, ranges,
            lambda s, t: (-s[1]) % 3,
            "INVERSE_TWIST_C3_HOST_MULTIPLICATION",
        ),
    )
    print("C3_CONTROL", "source=24", "points=24", "pair_products=576")


def enumerate_homomorphisms(m, n):
    retained = []
    total = 0
    for values in itertools.product(range(n), repeat=m):
        tick()
        total += 1
        if all(
            values[(a + b) % m] == (values[a] + values[b]) % n
            for a in range(m) for b in range(m)
        ):
            retained.append(values)
    require(total == n ** m, "ALL_FUNCTIONS_ENUMERATED", (m, n, total))
    return total, tuple(retained)


def cyclic_group_checks(m):
    elements = tuple(range(m))
    multiply = lambda a, b: (a + b) % m
    require(
        {a for a in elements if multiply(a, a) == a} == {0},
        "CYCLIC_IDEMPOTENTS",
        m,
    )
    for a in elements:
        tick()
        require(
            multiply(a, (-a) % m) == 0
            and multiply((-a) % m, a) == 0,
            "CYCLIC_INVERSE",
            (m, a),
        )
        for b in elements:
            for c in elements:
                require(
                    multiply(multiply(a, b), c)
                    == multiply(a, multiply(b, c)),
                    "CYCLIC_ASSOCIATIVITY",
                    (m, a, b, c),
                )


def subgroup_host_checks():
    cyclic_group_checks(4)
    cyclic_group_checks(2)

    source = (0, 2)
    multiply = lambda a, b: (a + b) % 4
    r = {0: 0, 2: 2}
    q = {0: 0, 2: 1}
    f = {s: (0, s) for s in source}

    def initial_product(left, right):
        return (0, (left[1] + right[1]) % 4)

    require(
        {s for s in source if multiply(s, s) == s} == {0},
        "SUBGROUP_SOURCE_IDEMPOTENTS",
    )
    require(
        all((-s) % 4 in source for s in source),
        "SUBGROUP_INVERSE_CLOSURE",
    )
    require(len(set(f.values())) == 2, "INITIAL_HOST_EMBEDDING_INJECTIVE")
    require(set(r.values()) == {0, 2}, "INITIAL_ACTOR_SOURCE_IMAGE")
    require(set(r.values()) != set(range(4)), "INITIAL_ACTOR_NOT_SATURATED")
    require(set(q.values()) == {0, 1}, "SUBGROUP_Q_ONTO")

    for s in source:
        for t in source:
            st = multiply(s, t)
            require(st in source, "SUBGROUP_SOURCE_CLOSURE", (s, t))
            require(
                initial_product(f[s], f[t]) == f[st],
                "INITIAL_PHYSICAL_HOST_MULTIPLICATION",
                (s, t),
            )
            require(r[st] == (r[s] + r[t]) % 4, "SUBGROUP_R_HOM", (s, t))
            require(q[st] == (q[s] + q[t]) % 2, "SUBGROUP_Q_HOM", (s, t))

    check_purity(source, multiply, {0}, q.__getitem__, "SUBGROUP_Q_PURITY")
    check_purity(source, multiply, {0}, r.__getitem__, "SUBGROUP_R_PURITY")

    ker_r = {(s, t) for s in source for t in source if r[s] == r[t]}
    ker_q = {(s, t) for s in source for t in source if q[s] == q[t]}
    diagonal = {(s, s) for s in source}
    require(ker_r == ker_q == diagonal, "EXACT_KERNEL_EQUALITY")
    require(ker_r <= ker_q, "KERNEL_INCLUSION")

    total, homomorphisms = enumerate_homomorphisms(4, 2)
    require(total == 16, "C4_TO_C2_FUNCTION_COUNT")
    require(
        homomorphisms == ((0, 0, 0, 0), (0, 1, 0, 1)),
        "EXACT_C4_TO_C2_HOMOMORPHISMS",
        homomorphisms,
    )
    matching = tuple(
        values for values in homomorphisms
        if all(values[r[s]] == q[s] for s in source)
    )
    require(matching == (), "C4_NO_MATCHING_ACTOR_EXTENSION", matching)

    source_only = {s: (0, q[s]) for s in source}
    require(
        len(set(source_only.values())) == 2,
        "SOURCE_ONLY_EMBEDDING_INJECTIVE",
    )
    for s in source:
        for t in source:
            actual = (
                0,
                (source_only[s][1] + source_only[t][1]) % 2,
            )
            require(
                actual == source_only[multiply(s, t)],
                "SOURCE_ONLY_PHYSICAL_MULTIPLICATION",
                (s, t),
            )

    q_zero = {s: 0 for s in source}
    require(
        all(
            q_zero[multiply(s, t)] == (q_zero[s] + q_zero[t]) % 2
            for s in source for t in source
        ),
        "ALTERED_C2_QUOTIENT_STILL_HOM",
    )
    require(set(q_zero.values()) != {0, 1}, "ALTERED_C2_QUOTIENT_NOT_ONTO")
    require(
        {s for s in source if q_zero[s] == 0} != {0},
        "ALTERED_C2_QUOTIENT_NOT_PURE",
    )
    altered_kernel = {
        (s, t) for s in source for t in source if q_zero[s] == q_zero[t]
    }
    require(ker_r <= altered_kernel, "ALTERED_QUOTIENT_KERNEL_INCLUSION")
    altered_matching = tuple(
        values for values in homomorphisms
        if all(values[r[s]] == q_zero[s] for s in source)
    )
    require(len(altered_matching) == 2, "ALTERED_C2_EXTENSION_COUNT")
    negative(
        "ALTERED_C2_QUOTIENT_NO_EXTENSION",
        lambda: require(
            not altered_matching,
            "ALTERED_C2_QUOTIENT_NO_EXTENSION",
            altered_matching,
        ),
    )

    _, trivial_homomorphisms = enumerate_homomorphisms(4, 1)
    require(
        trivial_homomorphisms == ((0, 0, 0, 0),),
        "TRIVIAL_TARGET_UNIQUE_EXTENSION",
    )
    require({q_zero[s] for s in source} == {0}, "ALTERED_TRIVIAL_Q_ONTO")
    negative(
        "ALTERED_TRIVIAL_QUOTIENT_NO_EXTENSION",
        lambda: require(
            not trivial_homomorphisms,
            "ALTERED_TRIVIAL_QUOTIENT_NO_EXTENSION",
            trivial_homomorphisms,
        ),
    )

    cyclic_group_checks(6)
    source6 = (0, 3)
    multiply6 = lambda a, b: (a + b) % 6
    q6 = {0: 0, 3: 1}
    require(set(q6.values()) == {0, 1}, "C6_SUBGROUP_Q_ONTO")
    check_purity(
        source6, multiply6, {0}, q6.__getitem__, "C6_SUBGROUP_Q_PURITY"
    )
    require(
        all(
            q6[multiply6(s, t)] == (q6[s] + q6[t]) % 2
            for s in source6 for t in source6
        ),
        "C6_SUBGROUP_Q_HOM",
    )
    total6, homomorphisms6 = enumerate_homomorphisms(6, 2)
    require(total6 == 64, "C6_TO_C2_FUNCTION_COUNT")
    matching6 = tuple(
        values for values in homomorphisms6
        if all(values[s] == q6[s] for s in source6)
    )
    require(
        matching6 == ((0, 1, 0, 1, 0, 1),),
        "C6_MATCHING_EXTENSION",
        matching6,
    )
    phi6 = matching6[0]
    require(
        {a for a in range(6) if phi6[a] == 0} == {0, 2, 4},
        "C6_EXTENSION_EXACT_KERNEL",
    )
    negative(
        "C6_MATCHING_EXTENSION_PURITY",
        lambda: check_purity(
            tuple(range(6)), multiply6, {0},
            lambda a: phi6[a],
            "C6_MATCHING_EXTENSION_PURITY",
        ),
    )

    _, homomorphisms2 = enumerate_homomorphisms(2, 2)
    matching2 = tuple(
        values for values in homomorphisms2
        if values == (0, 1)
    )
    require(matching2 == ((0, 1),), "WHOLE_ACTOR_POSITIVE_EXTENSION")
    check_purity(
        (0, 1), lambda a, b: (a + b) % 2, {0},
        lambda a: matching2[0][a],
        "WHOLE_ACTOR_POSITIVE_EXTENSION_PURITY",
    )

    print(
        "SUBGROUP_HOST",
        "functions_C4_C2=", total,
        "homomorphisms=", homomorphisms,
        "matching_extensions=", matching,
        "source_only_image=", tuple(source_only[s] for s in source),
    )


def main():
    primary_checks()
    inverse_twist_c3_control()
    subgroup_host_checks()
    tick()
    print(
        "COMPLETED_ALL_NAMED_INVARIANTS",
        "elapsed_seconds=%.6f" % (time.monotonic() - START),
    )


if __name__ == "__main__":
    main()

END PYTHON SOURCE

## 8. Results, imports, and unpaid gates

### Written results

The selected finite mathematics establishes:

- An actual non-group eight-element inverse source with an onto pure quotient to \(C_2\).
- Explicit \(\iota\) and range-ideal coordinates from the assigned definitions.
- A nontrivial action on the exact 256-element semilattice host.
- Injective physical-host embeddings for both \(C_2\) sandwich entries.
- A complete \(C_4\to C_2\) finite nonextension witness satisfying the stated source, initial-host, purity, and kernel conditions.
- A separate source-only embedding in that nonextension example.
- Explicit discriminating mutations, including the reason inverse-twist reversal cannot be detected on \(C_2\) alone.

These are written derivations, **not observed program results**.

### Exact imports

The only scientific imports are the assigned S1 definitions:

- Physical host multiplication: S1 lines 33–65.
- Normalization \(h\mapsto hp\): S1 lines 141–164.
- \(\iota(x)=(\bar q(x),x^{-1}x)\): S1 lines 174–184.
- Point action: S1 lines 209–227.
- \(R_s=\iota(ss^{-1}S)\): S1 lines 232–265.
- Physical consuming multiplication and source map: S1 lines 326–356.
- The specified subgroup-host witness: S1 lines 461–583.

No general theorem from S1 is assumed to prove the finite instances. The checker imports no author implementation.

### Remaining gates and limits

1. **Execution:** The complete checker remains NOT RUN. Its stdout, runtime, successful completion, and implementation correctness have not received machine confirmation.
2. **Independent checking:** No independent-family, human, or kernel check has been performed by this return.
3. **Parent disposition:** This candidate remains unreviewed until a separate parent disposition.
4. **General inverse-source theorem:** Selected finite instances do not verify its universal quantifiers.
5. **General regular sources:** No construction or obstruction for all regular sources is proved.
6. **Canonical/restricted hosts:** The nonextension example concerns a supplied arbitrary host only.
7. **Arbitrary embedding:** Failure to extend an actor from the entire initial host does not obstruct the separately supplied source-only embedding.
8. **Other source/admissibility/novelty claims:** No printed-problem authentication, Fact1, canonical-host, SN/RIGHTSN, unspecified Horn/free-band, original-target closure, or novelty certification is supplied.

overall_correctness: correct

explanation: No defect was found in the selected finite written constructions or the arbitrary-host nonextension witness. The supplied independent checker is complete but NOT RUN under the active tool restriction, so no computational verification or universal theorem acceptance is asserted.

confidence: 0.94