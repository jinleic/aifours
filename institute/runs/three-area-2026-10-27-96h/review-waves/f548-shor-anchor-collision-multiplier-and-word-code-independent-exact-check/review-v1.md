# F548 — FINITE full return

**Candidate examined:** f497 `review-v1.md`, as reproduced in the frozen f548 literal packet.  
**Mathematical findings:** FATAL 0 / MAJOR 0 / MINOR 0 within the inspected interfaces.  
**Finite execution:** **NOT_RUN — required by this role’s NOEXEC constraint.**  
**Original anchored-tiling and finite-completion targets:** **NOT_PROVED.**

This return supplies written checks, explicit finite inputs, intended-reason mutation controls, and complete prospective checker source. It does **not** supply an observed executable PASS.

## 1. Input binding and actual chronology

Assignment identifiers:

- Manifest SHA-256: `523efa7193156e02a7280681d0745c152a4714c0576dc24fed809a3c28dadb63`.
- Receipt SHA-256: `99e2211106a315c8bc7656f78a8aab6f9e044e2db674a6d3238b09abec7cb740`.
- Packet SHA-256, attributed to the supplied receipt and parent metadata: `33cc605e4203d4d4444b2c94124439ee329ad95a0a428ce5b3d03232112f5c34`.
- Candidate SHA-256, likewise parent-supplied: `ec0cdf85c4da552b1ccd80982c79a5234512161124e2d476cb06da82c470bb86`.

I did not execute hashing or obtain a child-native clock.

Actual access order:

1. Read the memory guidance and relevant review protocol.
2. Completely read the manifest, freeze receipt, dispatch receipt, supplied metadata, and all twelve listed status/permission controls.
3. Delivered the direct pre-body ACK, explicitly retaining NOEXEC and the exclusion of held episodes and their consumers.
4. Read packet LF 1–522 in contiguous, ordered raw windows of at most 20 lines, including its terminal result. These windows displayed candidate labels `S1|1` through `S1|520`.
5. Read the finite-verification, snapshot-review, and checker-authoring process instructions.
6. Only after the complete packet read, developed the written checks and prospective source below.

The source metadata reports LF 519, while the packet labels its complete rendered body through line 520. My completeness statement concerns the **entire displayed frozen packet**, including its ending; it is not an independently executed whole-file equality or line-ending audit.

No author executable, sibling result, held scientific payload, held consumer, external scientific source, model CLI, build, test, formatter, or scientific interpreter was accessed or executed. No filesystem modification or write bypass was attempted. This is the full body for Main to materialize.

## 2. Actual target and separation of objects

The candidate concerns actual sets satisfying

\[
P\oplus Q=\mathbb Z_n,\qquad n>14,
\]

with

\[
\{0,3,8,11\}\subseteq P,\qquad
\{0,1,7,13,14\}\subseteq Q.
\]

Directness means exactly one ordered representation of every residue, so \(|P||Q|=n\).

The following objects remain separate:

- The actual anchors above are used in every anchor-collision check.
- Exhaustive tilings of groups of order at most 12 check the **dilation interface**, not the anchored target; those orders do not meet \(n>14\).
- The CRT product tilings in §7 are genuine cyclic tilings, but **not anchored witnesses**.
- The changed-word and periodic-residual codes are explicitly synthetic checker controls, not replacements for the original eight words.
- The external RSS theorem remains an unverified conditional import in this return.

## 3. Dilation: multiplicities and the correct coprimality boundary

Candidate occurrence: S1 LF 83–139.

The stated lemma uses

\[
\gcd(k,|A|)=1,
\]

not \(\gcd(k,n)=1\), and not coprimality with the opposite factor.

For a prime \(\ell\nmid |A|\), the candidate’s group-ring calculation yields

\[
A(X^\ell)B(X)\equiv J(X)\pmod\ell.
\]

Retaining every original ordered pair gives integral coefficients

\[
c_x=\#\{(a,b)\in A\times B:\ell a+b=x\bmod n\}.
\]

Each \(c_x\) is nonnegative and congruent to 1 modulo \(\ell\), hence at least 1. Their sum is \(n\), so all \(n\) coefficients equal 1. This also proves injectivity on \(A\): a repeated multiplied image, followed by addition of any fixed \(b\in B\), would give a coefficient at least 2. Successive prime factors handle positive composite \(k\).

**Written positive nonunit control.** In \(\mathbb Z_6\),

\[
A=\{0,3\},\quad B=\{0,1,2\},\quad k=3.
\]

Both the original and multiplied ordered sums have coefficient vector

\[
(1,1,1,1,1,1),
\]

and \(3A=\{0,3\}\) is injective. Here

\[
\gcd(3,|A|)=1,\qquad
\gcd(3,6)=3,\qquad
\gcd(3,|B|)=3.
\]

Thus substituting either the group order or the opposite cardinality would falsely reject an admissible dilation.

**Written multiplicity mutation control.** In \(\mathbb Z_4\),

\[
A=\{0,2\},\quad B=\{0,1\},\quad k=2.
\]

This deliberately violates the lemma’s coprimality hypothesis. Retaining original pairs gives

\[
(2,2,0,0);
\]

first replacing \(2A\) by its unweighted image set gives

\[
(1,1,0,0).
\]

The latter loses total mass: 2 rather than 4. The prospective checker therefore requires the unweighted mutation to fail specifically with `MASS`, and the weighted but nondirect result to fail with `DIRECTNESS`. This control is not presented as a counterexample to the lemma.

### Exhaustive bounded scope

The checker enumerates every ordered pair of zero-containing subsets with \(|A||B|=n\), for \(1\le n\le12\), and keeps exactly those whose original coefficient vector is all ones.

This normalization does not lose the property being checked. Translating arbitrary factors to contain zero preserves original directness; after dilation, the translated sum differs from the original multiplied sum by one overall translation. Injectivity is also translation-invariant.

For each retained tiling, the checker considers \(1\le k\le n\). Because \(|A|\mid n\), both the multiplied residues and the coprimality condition are periodic modulo \(n\). Thus this covers every positive multiplier’s behavior for those bounded groups.

**Execution and enumeration counts: NOT_RUN; no counts are claimed.**

## 4. All five actual-anchor collisions

These are the candidate’s actual occurrences, not shadow examples.

| Conclusion forced | Candidate LF | Dilation if divisibility fails | Actual distinct ordered pairs | Integer identity |
|---|---:|---|---|---|
| \(2\mid |P|\) | 152–160 | Dilate \(P\) by 2 | \((3,1),(0,7)\) | \(2\cdot3+1=2\cdot0+7=7\) |
| \(2\mid |Q|\) | 164–168 | Dilate \(Q\) by 8 | \((8,0),(0,1)\) | \(8+8\cdot0=0+8\cdot1=8\) |
| \(3\mid |Q|\) | 170–174 | Dilate \(Q\) by 3 | \((3,0),(0,1)\) | \(3+3\cdot0=0+3\cdot1=3\) |
| \(5\mid |Q|\) | 176–180 | Dilate \(Q\) by 5 | \((8,0),(3,1)\) | \(8+5\cdot0=3+5\cdot1=8\) |
| \(11\mid |Q|\) | 182–188 | Dilate \(Q\) by 11 | \((11,0),(0,1)\) | \(11+11\cdot0=0+11\cdot1=11\) |

For head dilation, the unchanged \(Q\)-entries distinguish the pairs. For tail dilation, the unchanged \(P\)-entries distinguish them. All these unequal entries remain unequal modulo every \(n>14\).

The cardinality guards are exactly:

- \(\gcd(2,s)=1\) iff \(s\) is odd;
- \(\gcd(8,s)=1\) iff \(s\) is odd;
- for \(r=3,5,11\), \(\gcd(r,s)=1\) iff \(r\nmid s\).

Consequently the candidate correctly derives

\[
2\mid |P|,\qquad 330\mid |Q|,\qquad 660\mid n.
\]

## 5. CRT multiplier: written reconstruction and selected inputs

Candidate occurrence: S1 LF 199–279.

Suppose

\[
n=4m,\quad m\text{ odd},\quad 3\nmid |P|.
\]

Choose a positive odd \(k\) with \(2k\equiv3\pmod m\). An explicit construction is

\[
k_0=\frac{m+3}{2},\qquad
k=\begin{cases}
k_0,&k_0\text{ odd},\\
k_0+m,&k_0\text{ even}.
\end{cases}
\]

Every odd prime divisor of \(|P|\) divides \(m\). If it also divided \(k\), the congruence would force it to be 3, contrary to \(3\nmid |P|\). Oddness handles the prime 2. Hence \(\gcd(k,|P|)=1\).

Moreover,

\[
m\mid2k-3
\quad\Longrightarrow\quad
4m\mid8k-12.
\]

The **actual** anchors \(8,0\in P\) and \(1,13\in Q\) then give

\[
8k+1\equiv 0k+13\pmod n.
\]

The unchanged tail entries 1 and 13 distinguish the two ordered pairs. This checks the claimed contradiction.

### Explicit finite cardinality cases

These are numerical cardinality/congruence controls, **not constructed anchored tilings**. The following values were obtained by written substitution, not program execution.

| Odd head part \(u\) | Odd tail part \(w\) | \(n=4uw\) | Positive odd \(k\) | \(8k-12\) |
|---:|---:|---:|---:|---:|
| 25 | 165 | 16,500 | 6,189 | \(3n\) |
| 125 | 825 | 412,500 | 154,689 | \(3n\) |
| 121 | 165 | 79,860 | 29,949 | \(3n\) |
| 121 | 1,815 | 878,460 | 109,809 | \(n\) |
| 55 | 165 | 36,300 | 4,539 | \(n\) |
| 3,025 | 165 | 1,996,500 | 748,689 | \(3n\) |

Here \(|P|=2u,\ |Q|=2w\). The cases include:

- shared powers of 5;
- shared powers of 11;
- mixed 5-and-11 head factors;
- 3 in the tail and not the head;
- multipliers that are not units modulo \(n\).

The checker performs only integer arithmetic for these orders; it does not allocate or iterate over these large cyclic groups.

### Intended-reason multiplier mutations

- **Wrong parity representative:** replace \(k=6189\) by \(k+m=10314\), with \(m=4125\). The congruence modulo \(m\) survives, but oddness fails. Intended rejection: `ODD_REPRESENTATIVE`.
- **Wrong difference:** replace 12 by 10. Intended rejection: `ANCHOR_DIFFERENCE`; 12 is the actual difference \(13-1\).
- **Allow 3 in the head:** use \(u=3,w=165,m=495,k=249\). The odd representative and congruence hold, but \(\gcd(249,6)=3\). Intended rejection: `HEAD_COPRIMALITY`.
- **Use the wrong coprimality object:** the admissible \((u,w)=(25,165)\) case has \(k=6189\) sharing a factor with both the group order and tail cardinality. Those substituted guards falsely reject it.

These controls test the stated interface; none supplies a positive anchored witness.

## 6. Literal eight-word code and complete residual analysis

Candidate occurrence: S1 LF 385–423.

The original code is exactly

\[
X=\{b,a^3b,a^8b,a^{11}b,ba,ba^7,ba^{13},ba^{14}\}.
\]

Its initial nonempty proper-prefix residual set is

\[
R_1=\{a,a^6,a^7,a^{12},a^{13},a^{14}\}.
\]

The next set is exactly

\[
R_2=\{ab,a^2b,a^4b,a^5b,a^7b,a^{10}b\}.
\]

These exponents arise from the positive differences \(p-d\), with \(p\in\{3,8,11\}\), \(d\in\{1,6,7,12,13,14\}\), and \(d<p\). No equality \(d=p\) occurs.

Every member of \(R_2\) begins with \(a\), so it cannot compare with a \(b\)-initial codeword. Its terminal-\(b\) position also differs from those of all three \(a\)-initial codewords. Therefore

\[
R_3=\varnothing,
\]

without obtaining \(\epsilon\). This checks unique decodability of the **actual original eight words**.

The prospective source implements both:

- a complete residual queue, suppressing revisits but detecting \(\epsilon\);
- level-set iteration, explicitly detecting empty termination, repeated-state cycles, and \(\epsilon\).

It requires the original level sequence to equal precisely \((R_1,R_2,\varnothing)\).

### Changed-word negative control

Only for this control, replace \(a^8b\) by \(a^7b\), leaving the other seven words unchanged. Then

\[
(ba^7)b=b(a^7b)
\]

gives two different sequences of mutant codewords with the same concatenation.

The residual path is

\[
a^7\longrightarrow b\longrightarrow\epsilon.
\]

The checker requires rejection specifically with `SP_EPSILON`, and checks the displayed two-factorization witness.

### Cycle control

The separate synthetic code \(\{0,01,11\}\) has residual set \(\{1\}\), which repeats without \(\epsilon\). The checker requires the level implementation to recognize the cycle as epsilon-free and the queue implementation to exhaust its visited-state search. This checks termination behavior; it is not an original-word witness.

## 7. Actual cyclic local barriers, not anchored witnesses

Candidate occurrence: S1 LF 333–383.

The integrality quantity is

\[
\frac{2^{a+b}p^{j+t-2}}{2^bp^t}=2^ap^{j-2}.
\]

For \(j=1\), it is \(2^a/p\), nonintegral for the listed odd primes. For \(j=2\), it is \(2^a\), integral. The prospective source uses exact rational arithmetic and requires a mutation that asserts nonintegrality at \(j=2\) to fail with `FIBER_NONINTEGRAL`.

The explicit product construction is

\[
A_p=\{0,\ldots,p^j-1\},\qquad
B_p=\{p^jh:0\le h<p^{v-j}\},
\]

\[
A_2=\{2h:0\le h<2^a\},\qquad B_2=\{0,1\}.
\]

The source checks these finite parameter tuples \((p,a,j,v)\):

\[
(3,1,2,3),\ (5,1,2,3),\ (11,1,2,3),\
(5,2,2,3),\ (3,1,3,4).
\]

Their cyclic orders are respectively

\[
108,\ 500,\ 5324,\ 1000,\ 324.
\]

For each case it constructs the actual CRT map to \(\mathbb Z_{p^v2^{a+1}}\), checks its coordinate identities and full-universe bijection, and checks every ordered sum coefficient of the resulting cyclic factors.

It also checks:

- the tail is constant modulo \(p^2\);
- the tail contains both parities;
- both cardinalities have a factor \(p\);
- every head residue class modulo \(p^2\) has the stated count;
- the head is entirely even and specifically **misses the required anchor 3**.

Thus these are legitimate local barrier controls but **not counterexamples to the original anchored problem**.

**Execution: NOT_RUN.** The construction’s written quotient/remainder, parity, and CRT arguments are distinct from an observed exhaustive coefficient check.

## 8. Border direction and external-import ceiling

Candidate occurrences: S1 LF 429–469.

For the literal original code, extracting the one-\(b\) left and right exponents in their stated order gives

\[
P_X=\{0,3,8,11\},\qquad
Q_X=\{0,1,7,13,14\}.
\]

The checker verifies those exact sets. A direction-swapping mutation must fail with `BORDER_HEAD`.

This verifies the finite **membership and direction interface only**. It does not establish the Restivo–Salemi–Sportelli theorem, finite maximality, the pure-letter-order fact, existence of a finite completion, or nonexistence of such a completion.

The Cordero/RSS citation in the candidate was not followed by this role. Its mathematical use therefore remains explicitly conditional on the candidate’s stated external import.

## 9. Complete prospective checker source — NOT RUN

**Prospective filename:** `f548-finite-checker-v1.py`.

**Prospective argv, not executed:**  
`python3 -I -B f548-finite-checker-v1.py`

Requires Python 3.8 or later for modular inversion via `pow`.

The source has no explicit filesystem, network, subprocess, input, or output operations. On a future authorized execution, all checks run at module entry; failures raise an exception, while the in-memory receipt is assigned to `RESULT`. No external receipt is emitted.

It uses a cooperative 50-second deadline. **No wall time, RSS, or ≤55-second execution result was observed here.** Histogram arrays are needed only for orders at most 5324; the larger multiplier cases use scalar arithmetic only.

To reconstruct the exact source below, remove the initial three characters `PY|` from every source line, join the remaining lines with LF, and append a final LF. No source hash is claimed before Main materializes its bytes.

SOURCE START

PY|from collections import Counter, deque
PY|from fractions import Fraction
PY|from itertools import combinations
PY|from math import gcd
PY|from time import monotonic
PY|
PY|STOP = monotonic() + 50.0
PY|P = (0, 3, 8, 11)
PY|Q = (0, 1, 7, 13, 14)
PY|WORDS = (
PY|    "b", "a" * 3 + "b", "a" * 8 + "b", "a" * 11 + "b",
PY|    "ba", "b" + "a" * 7, "b" + "a" * 13, "b" + "a" * 14,
PY|)
PY|
PY|
PY|class CheckFailure(ValueError):
PY|    pass
PY|
PY|
PY|def tick():
PY|    if monotonic() > STOP:
PY|        raise CheckFailure("DEADLINE")
PY|
PY|
PY|def need(condition, reason):
PY|    tick()
PY|    if not condition:
PY|        raise CheckFailure(reason)
PY|
PY|
PY|def expect_failure(reason, thunk):
PY|    try:
PY|        thunk()
PY|    except CheckFailure as exc:
PY|        need(str(exc) == reason, "WRONG_MUTANT_REASON")
PY|        return reason
PY|    raise CheckFailure("MUTANT_SURVIVED")
PY|
PY|
PY|def coefficients(n, a, b, k=1, drop_multiplicities=False):
PY|    tick()
PY|    mapped = tuple((k * x) % n for x in a)
PY|    if drop_multiplicities:
PY|        mapped = tuple(sorted(set(mapped)))
PY|    result = [0] * n
PY|    for x in mapped:
PY|        tick()
PY|        for y in b:
PY|            result[(x + y) % n] += 1
PY|    return tuple(result)
PY|
PY|
PY|def unit_histogram(n, histogram):
PY|    need(len(histogram) == n, "LENGTH")
PY|    need(sum(histogram) == n, "MASS")
PY|    need(all(c == 1 for c in histogram), "DIRECTNESS")
PY|
PY|
PY|def admissible(k, size):
PY|    need(gcd(k, size) == 1, "ADMISSIBILITY")
PY|
PY|
PY|def exhaustive_small_tilings():
PY|    rows = []
PY|    total_nonunits = 0
PY|    for n in range(1, 13):
PY|        pairs = tilings = multipliers = nonunits = 0
PY|        for size_a in range(1, n + 1):
PY|            if n % size_a:
PY|                continue
PY|            size_b = n // size_a
PY|            for aa in combinations(range(1, n), size_a - 1):
PY|                a = (0,) + aa
PY|                for bb in combinations(range(1, n), size_b - 1):
PY|                    tick()
PY|                    b = (0,) + bb
PY|                    pairs += 1
PY|                    original = coefficients(n, a, b)
PY|                    if any(c != 1 for c in original):
PY|                        continue
PY|                    unit_histogram(n, original)
PY|                    tilings += 1
PY|                    for k in range(1, n + 1):
PY|                        if gcd(k, size_a) != 1:
PY|                            continue
PY|                        admissible(k, size_a)
PY|                        image = tuple((k * x) % n for x in a)
PY|                        need(len(set(image)) == size_a, "INJECTIVITY")
PY|                        unit_histogram(n, coefficients(n, a, b, k))
PY|                        multipliers += 1
PY|                        if gcd(k, n) != 1:
PY|                            nonunits += 1
PY|        total_nonunits += nonunits
PY|        rows.append((n, pairs, tilings, multipliers, nonunits))
PY|    need(total_nonunits > 0, "NONUNIT_COVERAGE")
PY|    return tuple(rows)
PY|
PY|
PY|def check_anchor_collisions():
PY|    cases = (
PY|        ("P", 2, 3, 1, 0, 7, 2),
PY|        ("Q", 8, 8, 0, 0, 1, 2),
PY|        ("Q", 3, 3, 0, 0, 1, 3),
PY|        ("Q", 5, 8, 0, 3, 1, 5),
PY|        ("Q", 11, 11, 0, 0, 1, 11),
PY|    )
PY|    rows = []
PY|    for side, k, p1, q1, p2, q2, prime in cases:
PY|        need(p1 in P and p2 in P, "ACTUAL_HEAD_ANCHORS")
PY|        need(q1 in Q and q2 in Q, "ACTUAL_TAIL_ANCHORS")
PY|        hp, hq = (k, 1) if side == "P" else (1, k)
PY|        left = hp * p1 + hq * q1
PY|        right = hp * p2 + hq * q2
PY|        need(left == right, "ANCHOR_IDENTITY")
PY|        need((p1, q1) != (p2, q2), "ORDERED_PAIR_IDENTITY")
PY|        if side == "P":
PY|            need(q1 != q2, "UNCHANGED_TAIL_DISTINCT")
PY|        else:
PY|            need(p1 != p2, "UNCHANGED_HEAD_DISTINCT")
PY|        for size in range(1, 65):
PY|            need(
PY|                (gcd(k, size) == 1) == (size % prime != 0),
PY|                "COPRIMALITY_EQUIVALENCE",
PY|            )
PY|        rows.append((side, k, (p1, q1), (p2, q2), left))
PY|    return tuple(rows)
PY|
PY|
PY|def odd_multiplier(m):
PY|    need(m > 0 and m % 2 == 1, "ODD_MODULUS")
PY|    k = (m + 3) // 2
PY|    if k % 2 == 0:
PY|        k += m
PY|    return k
PY|
PY|
PY|def verify_multiplier(m, head_size, k, difference=12):
PY|    need(m > 0 and m % 2 == 1, "ODD_MODULUS")
PY|    need(k > 0 and k % 2 == 1, "ODD_REPRESENTATIVE")
PY|    need((2 * k - 3) % m == 0, "CONGRUENCE_2K")
PY|    need(gcd(k, head_size) == 1, "HEAD_COPRIMALITY")
PY|    n = 4 * m
PY|    need((8 * k - difference) % n == 0, "ANCHOR_DIFFERENCE")
PY|    need((8 * k + 1 - 13) % n == 0, "ACTUAL_ANCHOR_COLLISION")
PY|    return (n, head_size, k, gcd(k, n))
PY|
PY|
PY|def check_multiplier_cases():
PY|    cases = (
PY|        (25, 165), (125, 825), (121, 165),
PY|        (121, 1815), (55, 165), (3025, 165),
PY|    )
PY|    rows = []
PY|    for u, w in cases:
PY|        need(u > 0 and w > 0 and (u * w) % 2 == 1,
PY|             "CARDINALITY_PARITY")
PY|        need(u % 3 != 0, "HEAD_HAS_THREE")
PY|        need(w % 165 == 0, "TAIL_PRIMES")
PY|        m = u * w
PY|        k = odd_multiplier(m)
PY|        result = verify_multiplier(m, 2 * u, k)
PY|        need(gcd(k, 4 * m) > 1, "NONUNIT_GROUP_CONTROL")
PY|        need(gcd(k, 2 * w) > 1, "NONUNIT_TAIL_CONTROL")
PY|        rows.append((u, w, result, (8 * k - 12) // (4 * m)))
PY|    return tuple(rows)
PY|
PY|
PY|def fiber_count(p, a, b, j, t):
PY|    need(p in (3, 5, 11), "FIBER_PRIME")
PY|    need(min(a, b, j, t) >= 1, "FIBER_PARAMETERS")
PY|    return Fraction(
PY|        2 ** (a + b) * p ** (j + t - 2),
PY|        2 ** b * p ** t,
PY|    )
PY|
PY|
PY|def require_nonintegral(value):
PY|    need(value.denominator != 1, "FIBER_NONINTEGRAL")
PY|
PY|
PY|def check_integrality():
PY|    rows = []
PY|    for p in (3, 5, 11):
PY|        for a in (1, 2):
PY|            first = fiber_count(p, a, 1, 1, 1)
PY|            second = fiber_count(p, a, 1, 2, 1)
PY|            need(first.denominator == p, "J1_NONINTEGRAL")
PY|            need(second == 2 ** a, "J2_INTEGRAL")
PY|            rows.append((p, a, first, second))
PY|    return tuple(rows)
PY|
PY|
PY|def check_cyclic_barriers():
PY|    cases = (
PY|        (3, 1, 2, 3), (5, 1, 2, 3), (11, 1, 2, 3),
PY|        (5, 2, 2, 3), (3, 1, 3, 4),
PY|    )
PY|    rows = []
PY|    for p, a, j, v in cases:
PY|        need(p in (3, 5, 11) and a >= 1 and j >= 2 and v >= j + 1,
PY|             "BARRIER_PARAMETERS")
PY|        odd = p ** v
PY|        two = 2 ** (a + 1)
PY|        n = odd * two
PY|        inverse = pow(odd, -1, two)
PY|
PY|        def crt(x, y):
PY|            return (x + odd * (((y - x) * inverse) % two)) % n
PY|
PY|        universe = set()
PY|        for x in range(odd):
PY|            tick()
PY|            for y in range(two):
PY|                z = crt(x, y)
PY|                need(z % odd == x and z % two == y, "CRT_COORDINATES")
PY|                universe.add(z)
PY|        need(universe == set(range(n)), "CRT_FULL_UNIVERSE")
PY|        head = tuple(sorted({
PY|            crt(x, y)
PY|            for x in range(p ** j)
PY|            for y in range(0, two, 2)
PY|        }))
PY|        tail = tuple(sorted({
PY|            crt(p ** j * h, y)
PY|            for h in range(p ** (v - j))
PY|            for y in (0, 1)
PY|        }))
PY|        need(len(head) == 2 ** a * p ** j, "BARRIER_HEAD_SIZE")
PY|        need(len(tail) == 2 * p ** (v - j), "BARRIER_TAIL_SIZE")
PY|        unit_histogram(n, coefficients(n, head, tail))
PY|        need(all(x % 2 == 0 for x in head), "BARRIER_HEAD_EVEN")
PY|        need(3 not in head, "BARRIER_MISSES_HEAD3")
PY|        need({x % 2 for x in tail} == {0, 1}, "BARRIER_TAIL_PARITIES")
PY|        need(all(x % (p * p) == 0 for x in tail), "BARRIER_TAIL_P2")
PY|        need(len(head) % p == 0 and len(tail) % p == 0,
PY|             "BARRIER_SHARED_PRIME")
PY|        counts = Counter(x % (p * p) for x in head)
PY|        expected = 2 ** a * p ** (j - 2)
PY|        need(set(counts) == set(range(p * p)), "BARRIER_HEAD_COSETS")
PY|        need(all(c == expected for c in counts.values()),
PY|             "BARRIER_COSET_COUNTS")
PY|        rows.append((p, a, j, v, n, len(head), len(tail), "NOT_ANCHORED"))
PY|    return tuple(rows)
PY|
PY|
PY|def validate_words(words):
PY|    need(len(words) == len(set(words)), "DUPLICATE_WORD")
PY|    need(all(isinstance(w, str) and w for w in words), "EMPTY_WORD")
PY|
PY|
PY|def first_states(words):
PY|    return frozenset(
PY|        y[len(x):]
PY|        for x in words
PY|        for y in words
PY|        if x != y and y.startswith(x)
PY|    )
PY|
PY|
PY|def next_states(states, words):
PY|    result = set()
PY|    for residual in states:
PY|        tick()
PY|        for word in words:
PY|            if word.startswith(residual):
PY|                result.add(word[len(residual):])
PY|            if residual.startswith(word):
PY|                result.add(residual[len(word):])
PY|    return frozenset(result)
PY|
PY|
PY|def sp_queue(words):
PY|    validate_words(words)
PY|    initial = first_states(words)
PY|    queue = deque(sorted(initial))
PY|    seen = set(initial)
PY|    while queue:
PY|        tick()
PY|        residual = queue.popleft()
PY|        if residual == "":
PY|            return (False, "EPSILON", len(seen))
PY|        for successor in sorted(next_states((residual,), words)):
PY|            if successor not in seen:
PY|                seen.add(successor)
PY|                queue.append(successor)
PY|    return (True, "EXHAUSTED", len(seen))
PY|
PY|
PY|def sp_levels(words):
PY|    validate_words(words)
PY|    state = first_states(words)
PY|    seen = set()
PY|    layers = []
PY|    while True:
PY|        tick()
PY|        layers.append(state)
PY|        if "" in state:
PY|            return (False, "EPSILON", tuple(layers))
PY|        if not state:
PY|            return (True, "EMPTY", tuple(layers))
PY|        if state in seen:
PY|            return (True, "CYCLE", tuple(layers))
PY|        seen.add(state)
PY|        state = next_states(state, words)
PY|
PY|
PY|def require_ud(words):
PY|    valid, reason, count = sp_queue(words)
PY|    if not valid:
PY|        need(reason == "EPSILON", "SP_UNEXPECTED_FAILURE")
PY|        raise CheckFailure("SP_EPSILON")
PY|    return count
PY|
PY|
PY|def word_borders(words):
PY|    head = frozenset(
PY|        len(w) - 1 for w in words
PY|        if w.endswith("b") and w.count("b") == 1
PY|        and set(w[:-1]) <= {"a"}
PY|    )
PY|    tail = frozenset(
PY|        len(w) - 1 for w in words
PY|        if w.startswith("b") and w.count("b") == 1
PY|        and set(w[1:]) <= {"a"}
PY|    )
PY|    return head, tail
PY|
PY|
PY|def verify_borders(head, tail):
PY|    need(head == frozenset(P), "BORDER_HEAD")
PY|    need(tail == frozenset(Q), "BORDER_TAIL")
PY|
PY|
PY|def check_words():
PY|    need(len(WORDS) == 8, "EIGHT_ORIGINAL_WORDS")
PY|    expected = (
PY|        frozenset("a" * d for d in (1, 6, 7, 12, 13, 14)),
PY|        frozenset("a" * d + "b" for d in (1, 2, 4, 5, 7, 10)),
PY|        frozenset(),
PY|    )
PY|    valid, reason, layers = sp_levels(WORDS)
PY|    need(valid and reason == "EMPTY", "ORIGINAL_LEVEL_UD")
PY|    need(layers == expected, "EXACT_RESIDUAL_LAYERS")
PY|    valid_queue, queue_reason, count = sp_queue(WORDS)
PY|    need(valid_queue and queue_reason == "EXHAUSTED", "ORIGINAL_QUEUE_UD")
PY|    need(count == 12, "ORIGINAL_QUEUE_RESIDUAL_COUNT")
PY|    mutant = tuple(
PY|        "a" * 7 + "b" if w == "a" * 8 + "b" else w
PY|        for w in WORDS
PY|    )
PY|    mutation_reason = expect_failure(
PY|        "SP_EPSILON", lambda: require_ud(mutant)
PY|    )
PY|    mv, mr, ml = sp_levels(mutant)
PY|    need(not mv and mr == "EPSILON", "MUTANT_LEVEL_EPSILON")
PY|    need(len(ml) == 3 and "" in ml[-1], "MUTANT_EPSILON_STAGE")
PY|    left = ("b" + "a" * 7, "b")
PY|    right = ("b", "a" * 7 + "b")
PY|    need(left != right, "MUTANT_DISTINCT_FACTORIZATIONS")
PY|    need(set(left + right) <= set(mutant), "MUTANT_WITNESS_WORDS")
PY|    need("".join(left) == "".join(right), "MUTANT_WITNESS_CONCATENATION")
PY|    cycle_words = ("0", "01", "11")
PY|    cv, cr, cl = sp_levels(cycle_words)
PY|    need(cv and cr == "CYCLE", "CYCLE_CONTROL_LEVELS")
PY|    cq, qr, unused_count = sp_queue(cycle_words)
PY|    need(cq and qr == "EXHAUSTED", "CYCLE_CONTROL_QUEUE")
PY|    head, tail = word_borders(WORDS)
PY|    verify_borders(head, tail)
PY|    border_reason = expect_failure(
PY|        "BORDER_HEAD", lambda: verify_borders(tail, head)
PY|    )
PY|    return (WORDS, layers, count, cl, mutation_reason, border_reason)
PY|
PY|
PY|def check_basic_controls():
PY|    weighted = coefficients(4, (0, 2), (0, 1), 2)
PY|    unweighted = coefficients(
PY|        4, (0, 2), (0, 1), 2, drop_multiplicities=True
PY|    )
PY|    need(weighted == (2, 2, 0, 0), "WEIGHTED_FOLD_CONTROL")
PY|    need(unweighted == (1, 1, 0, 0), "UNWEIGHTED_FOLD_CONTROL")
PY|    reasons = []
PY|    reasons.append(("drop_multiplicities", expect_failure(
PY|        "MASS", lambda: unit_histogram(4, unweighted)
PY|    )))
PY|    reasons.append(("weighted_nondirect", expect_failure(
PY|        "DIRECTNESS", lambda: unit_histogram(4, weighted)
PY|    )))
PY|    a, b, k = (0, 3), (0, 1, 2), 3
PY|    unit_histogram(6, coefficients(6, a, b))
PY|    admissible(k, len(a))
PY|    unit_histogram(6, coefficients(6, a, b, k))
PY|    need(len({k * x % 6 for x in a}) == len(a), "NONUNIT_INJECTIVITY")
PY|    reasons.append(("gcd_with_group", expect_failure(
PY|        "ADMISSIBILITY", lambda: admissible(k, 6)
PY|    )))
PY|    reasons.append(("gcd_with_opposite_factor", expect_failure(
PY|        "ADMISSIBILITY", lambda: admissible(k, len(b))
PY|    )))
PY|    m = 25 * 165
PY|    correct = odd_multiplier(m)
PY|    verify_multiplier(m, 50, correct)
PY|    reasons.append(("wrong_odd_representative", expect_failure(
PY|        "ODD_REPRESENTATIVE",
PY|        lambda: verify_multiplier(m, 50, correct + m),
PY|    )))
PY|    reasons.append(("wrong_anchor_difference", expect_failure(
PY|        "ANCHOR_DIFFERENCE",
PY|        lambda: verify_multiplier(m, 50, correct, difference=10),
PY|    )))
PY|    reasons.append(("three_in_head", expect_failure(
PY|        "HEAD_COPRIMALITY",
PY|        lambda: verify_multiplier(495, 6, odd_multiplier(495)),
PY|    )))
PY|    reasons.append(("j2_nonintegrality_claim", expect_failure(
PY|        "FIBER_NONINTEGRAL",
PY|        lambda: require_nonintegral(fiber_count(5, 1, 1, 2, 1)),
PY|    )))
PY|    return tuple(reasons)
PY|
PY|
PY|def run():
PY|    controls = check_basic_controls()
PY|    anchors = check_anchor_collisions()
PY|    multipliers = check_multiplier_cases()
PY|    integrality = check_integrality()
PY|    words = check_words()
PY|    barriers = check_cyclic_barriers()
PY|    small = exhaustive_small_tilings()
PY|    tick()
PY|    return (
PY|        ("status", "ALL_CHECKS_COMPLETED"),
PY|        ("controls", controls),
PY|        ("actual_anchor_collisions", anchors),
PY|        ("cardinality_multiplier_cases", multipliers),
PY|        ("fiber_integrality", integrality),
PY|        ("literal_word_checks", words),
PY|        ("nonanchored_cyclic_barriers", barriers),
PY|        ("normalized_small_tilings", small),
PY|    )
PY|
PY|
PY|RESULT = run()

SOURCE END

The string `ALL_CHECKS_COMPLETED` above is a prospective program return value, **not an observed result of this assignment**.

## 10. Result and precise remaining obligations

### What this return supports

The written checks found no defect in:

- the multiplicity-preserving coprime-dilation argument;
- the five actual-anchor divisibility collisions;
- the odd CRT multiplier and its actual \(8k+1\equiv13\) collision;
- the distinction between \(j=1\) nonintegrality and \(j\ge2\) integrality;
- the stated local product construction and its failure to meet the head anchors;
- the exact original eight-word residual computation;
- the ordered left/right border membership.

### What remains unpaid

1. **Executable FINITE evidence:** NOT_RUN. No enumeration counts, observed mutation rejections, timings, memory measurements, executable-source hash, or machine PASS are supplied.
2. **Remaining higher-power anchored cases:** the candidate does not settle the families with
   \[
   |P|=2^ap^j,\quad |Q|=2^bp^tR,\quad
   j\ge2,\ a,b,t\ge1,\quad
   \gcd(R,2p)=1,\quad (165/p)\mid R,
   \]
   where \(p=3\), or where \(p=5,11\) and \(a+b\ge3\). This is a statement of this candidate’s limits, not a globally audited historical frontier.
3. **First missing step in the fiber route:** a valid anchored replacement for the every-fiber-nonconstant-modulo-\(p^2\) premise at \(j\ge2\), or another contradiction using the undilated anchors.
4. **Finite completion:** neither the RSS import nor the pure-letter-order fact was independently verified here, and nonexistence of a finite maximal completion remains unproved.

There is no human, kernel/formal, independent-model-family, novelty, original-source-authentication, or unrestricted Shor-completion credit.

**overall_correctness:** correct

**explanation:** No mathematical defect was found in the frozen candidate’s inspected algebra and literal interfaces. The executable FINITE gate remains NOT_RUN under NOEXEC, so this return does not grant a finite-machine PASS or close either unrestricted original target.

**confidence:** 0.94 — applies to the written inspection, not to unperformed execution.