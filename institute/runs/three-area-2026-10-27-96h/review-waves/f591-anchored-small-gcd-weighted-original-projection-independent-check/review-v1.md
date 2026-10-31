# F591 — Independent small-gcd support and weighted-projection check

**Role: FINITE. Scientific execution: NOT_RUN. Complete independent source is supplied below.**

**Mathematical outcome:** the finite support identities and positive-weight contradictions in the proposed small-gcd obstruction are consistent with the independent reconstruction below. No mathematical defect was identified. This return is **not an executed finite-gate PASS**, an actual anchored-tiling witness, or an adoption of the proposed theorem.

## 1. Frozen scope and provenance

Assigned wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f591-anchored-small-gcd-weighted-original-projection-independent-check/`

Binding metadata:

- Manifest SHA-256: `0718c4fce7ee6619bff40902d72555fc5929c70afe993dd58e4183abfac699d3`
- Freeze-receipt SHA-256: `5c644dbc0f9b5a21984ebb1abf982a0a283c00c0689d2a4ce1474cc6bcae3ebe`
- Literal-packet SHA-256: `d65b0ce850e7dcb14161d8deb27088da3088b22cce5cbcde1657129f18a3a349`
- S1 author-body SHA-256: `63a833c5c54b369d072208a0543d15a9b1e4b51e90b4c6b8622cb75a3d333909`
- S2 actual-anchor disposition SHA-256: `d8dfa1b1323f81c3c1be627fbf08794144d52b73de3efbcdded64ac6c3ad6d26`

These hashes, byte/LF counts, and the observation `2026-10-30T13:57:02-0700 PDT` are **parent-observed metadata**, supplied in `parent-live-metadata-supply-v1.json`. They are not my own hash execution, native clock execution, or observed start time.

Actual chronology:

1. Read the required memory summary and applicable acceptance skills.
2. Read the manifest, freeze receipt, parent metadata, and **all twelve controls completely**, including their endings. The initially truncated manifest research-task line was reread raw in full.
3. Sent the direct pre-body ACK to Main.
4. Read the entire literal packet **in ordered, exact raw windows of at most twenty lines**, packet lines 1–727, through its ending. This included S1 logical labels 1–694 and S2 labels 1–31.
5. Only afterward began the mathematical reconstruction and independent checker design.
6. Inspected the mounted-device inventory. It contains Gmail/Slack devices, not an authorized scientific evaluator.
7. Read the dispatch receipt confirming the FINITE role.

No held scientific payload, held consumer, sibling review, author code, new external source, external-model CLI, scientific executable, build, test, lint, or formatter was used. No working-tree file was edited. No execution was delegated to evade the runtime restriction.

The runtime restricts Bash to read-only review commands and forbids edits/builds. Therefore the source below was **not materialized or run**. Its runtime, exit status, stdout, stderr, and source SHA are **NOT_OBSERVED**.

## 2. Exact target and original-factor boundary

The proposed statement concerns actual sets satisfying

\[
P\oplus Q=\mathbb Z_n,\qquad n>14,
\]
\[
\{0,3,8,11\}\subseteq P,\qquad
\{0,1,7,13,14\}\subseteq Q,
\]

and an **actual direct factor** \(P=\{u,u+d\}\oplus C\), with two distinct points.

After absorbing \(u\), let \(P=\{0,d\}\oplus C\) and \(T=C\oplus Q\). Directness gives

\[
1_T(x)+1_T(x-d)=1.
\]

Writing \(g=\gcd(d,n)\), the \(d\)-cycles have even length, hence \(2g\mid n\). Also \(\gcd(2d,n)=2g\), so \(T\) consists of complete residue classes modulo \(2g\). Its occupied classes form \(V\subseteq\mathbb Z_{2g}\) with

\[
V\sqcup(V+g)=\mathbb Z_{2g}.
\]

Because \(0\in P\), either \(0\in C\) or \(-d\in C\). In the latter case replace \(d\) by \(-d\) and \(C\) by \(C+d\); this preserves the actual set \(P\). Thus the orientation \(0\in C\bmod 2g\) is justified.

For the **original multiplicities**

\[
c_i=\#(C\cap(i+2g\mathbb Z)),\qquad
q_j=\#(Q\cap(j+2g\mathbb Z)),\qquad
L=n/(2g),
\]

the consuming equation is exactly

\[
\sum_i c_iq_{s-i}=L1_V(s).
\]

It is not an unweighted quotient tiling. The implementation retains repeated projections of the original anchors with `Counter`; in particular it does not silently replace their lower multiplicity bounds by cardinalities of image sets.

The factor hypothesis is not implied by the four head anchors. No result here supplies that missing global factor.

## 3. Exhaustive support screen

For each \(g=1,\ldots,14\), enumerate all \(2^g\) antipodal selectors

\[
V=\{r+g\varepsilon_r:0\le r<g,\ \varepsilon_r\in\{0,1\}\}.
\]

Set \(S=\{0,1,7,13,14\}\bmod 2g\). Require \(S\subseteq V\), then compute

\[
D=\{c:S+c\subseteq V\}.
\]

The necessary head condition is, for each \(a\in\{0,3,8,11\}\),

\[
D\cap\{a,a-g\}\ne\varnothing.
\]

This is an exact support-feasibility screen without enumerating subsets of \(D\). It is **not an original-tiling solver or a positive-weight solver**.

The following counts are **written-derived expectations**, not observed program output:

| \(g\) | All selectors | Tail-compatible selectors | Head-compatible support shadows |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | 4 | 0 | 0 |
| 3 | 8 | 1 | 0 |
| 4 | 16 | 0 | 0 |
| 5 | 32 | 1 | 0 |
| 6 | 64 | 0 | 0 |
| 7 | 128 | 0 | 0 |
| 8 | 256 | 8 | 1 |
| 9 | 512 | 16 | 0 |
| 10 | 1,024 | 32 | 1 |
| 11 | 2,048 | 64 | 1 |
| 12 | 4,096 | 0 | 0 |
| 13 | 8,192 | 0 | 0 |
| 14 | 16,384 | 0 | 0 |
| **Total** | **32,766** | **122** | **3** |

For \(g=1,2,4,6,7,12,13,14\), the original tail differences \(1,14,12,6,7,12,13,14\), respectively, are congruent to \(g\bmod 2g\). Thus their tail projections already contain an antipodal pair.

The three surviving support shadows are:

| \(g\) | Forced \(V\) | Allowed \(C\)-support \(D\) | Forced positive \(C\)-residues \(M\) | Allowed \(Q\)-support upper bound |
|---:|---|---|---|---|
| 8 | \(0,1,3,4,7,10,13,14\) | \(0,3\) | \(0,3\) | \(0,1,4,7,10,13,14\) |
| 10 | \(0,1,2,6,7,8,9,13,14,15\) | \(0,1,7,8,13,14\) | \(0,1,8,13\) | \(0,1,7,13,14\) |
| 11 | \(0,1,5,6,7,8,9,13,14,15,21\) | \(0,8,14\) | \(0,8,14\) | \(0,1,7,13,14,15,21\) |

Here the \(Q\)-bound is \(\bigcap_{c\in M}(V-c)\). Optional allowed variables are nonnegative, **not assumed positive**.

For each row, \(M+S=V\) and the head anchors lie in \(M+\{0,g\}\). These are genuine **support-only shadows**, not actual anchored tilings.

### Direct incompatibilities for \(g=3,5,9\)

- **\(g=3\):** \(S=\{0,1,2\}\subseteq\mathbb Z_6\) already fills \(V\). Its translation stabilizer is trivial, so \(D=\{0\}\). The head anchor \(8\bmod6=2\) has neither \(2\) nor \(5\) in \(D\).
- **\(g=5\):** \(S=\{0,1,3,4,7\}\subseteq\mathbb Z_{10}\) fills \(V\). A nontrivial translation stabilizer would have order five and make \(S\) a parity coset, which it is not. Thus \(D=\{0\}\), incompatible with head anchor \(3\).
- **\(g=9\):** head anchor \(3\) must use \(C\)-residue \(12\), because choosing \(3\) puts \(10=3+7\) opposite the tail residue \(1\). Head anchor \(8\) must use residue \(17\), because choosing \(8\) puts \(9=8+1\) opposite \(0\). These forced shifts put both \(8=12+14\) and \(17=17+0\) in \(V\), an antipodal pair.

## 4. Complete supporting coefficient incidences

Each pair \((i,j)\) below represents the monomial \(c_iq_j\), with coefficient exactly one. All unlisted residues have zero incidence. The supplied program constructs rows for **every** residue, including those zero rows.

### \(g=8\), modulo 16

| Residue | Supporting pairs |
|---:|---|
| 0 | \((0,0),(3,13)\) |
| 1 | \((0,1),(3,14)\) |
| 3 | \((3,0)\) |
| 4 | \((0,4),(3,1)\) |
| 7 | \((0,7),(3,4)\) |
| 10 | \((0,10),(3,7)\) |
| 13 | \((0,13),(3,10)\) |
| 14 | \((0,14)\) |

### \(g=10\), modulo 20

| Residue | Supporting pairs |
|---:|---|
| 0 | \((0,0),(7,13),(13,7)\) |
| 1 | \((0,1),(1,0),(7,14),(8,13),(14,7)\) |
| 2 | \((1,1),(8,14)\) |
| 6 | \((13,13)\) |
| 7 | \((0,7),(7,0),(13,14),(14,13)\) |
| 8 | \((1,7),(7,1),(8,0),(14,14)\) |
| 9 | \((8,1)\) |
| 13 | \((0,13),(13,0)\) |
| 14 | \((0,14),(1,13),(7,7),(13,1),(14,0)\) |
| 15 | \((1,14),(8,7),(14,1)\) |

### \(g=11\), modulo 22

| Residue | Supporting pairs |
|---:|---|
| 0 | \((0,0),(8,14)\) |
| 1 | \((0,1),(8,15)\) |
| 5 | \((14,13)\) |
| 6 | \((14,14)\) |
| 7 | \((0,7),(8,21),(14,15)\) |
| 8 | \((8,0)\) |
| 9 | \((8,1)\) |
| 13 | \((0,13),(14,21)\) |
| 14 | \((0,14),(14,0)\) |
| 15 | \((0,15),(8,7),(14,1)\) |
| 21 | \((0,21),(8,13),(14,7)\) |

## 5. Exact positive-weight contradictions

These arguments apply to nonnegative real weights with the stated forced positive entries, so in particular to the original integer multiplicities.

### \(g=8\)

The singleton rows give

\[
L=c_3q_0,\qquad L=c_0q_{14}.
\]

The other two rows give

\[
L=c_0q_0+c_3q_{13}>c_0q_0,
\]
\[
L=c_0q_1+c_3q_{14}>c_3q_{14}.
\]

Consequently \(c_3>c_0\) and \(c_0>c_3\).

The strict witnesses are \(c_3q_{13}\) and \(c_0q_1\). Positivity comes from forced \(C\)-residues and the **provided original tail anchors** 13 and 1.

### \(g=10\)

The singleton rows give

\[
L=c_{13}q_{13},\qquad L=c_8q_1.
\]

At residues 1 and 14,

\[
L>c_8q_{13},\qquad L>c_{13}q_1,
\]

with strict witnesses \(c_0q_1\) and \(c_0q_{14}\), respectively. Therefore \(c_{13}>c_8\) and \(c_8>c_{13}\).

No positivity of the optional \(c_7,c_{14}\), or of any unprovided tail residue, is used.

### \(g=11\)

The singleton rows give

\[
L=c_{14}q_{14},\qquad L=c_8q_0.
\]

At residues 0 and 14,

\[
L=c_0q_0+c_8q_{14}>c_8q_{14},
\]
\[
L=c_0q_{14}+c_{14}q_0>c_{14}q_0.
\]

Thus \(c_{14}>c_8\) and \(c_8>c_{14}\).

Only the original tail anchors 0 and 14 supply the required tail positivity. In particular \(q_{15}\) and \(q_{21}\) are not assumed positive.

The source independently checks these certificates by exact `Fraction` coefficient subtraction, verifies a positive remainder monomial using only forced positivity, and checks the resulting strict two-cycle. This is a symbolic certificate check, **not numerical optimization or a general feasibility solver**.

## 6. Genuine non-target tilings for every \(g=1,\ldots,14\)

For every listed \(g\), define

\[
m=2g,\qquad
L=\left\lceil\frac{15}{2g}\right\rceil,\qquad
n=2gL,\qquad d=g,\qquad C=\{0\},
\]
\[
Q=\{x\in\mathbb Z_n:x\bmod 2g\in\{0,\ldots,g-1\}\}.
\]

Then \(n>14\), \(\gcd(d,n)=g\), and

\[
\{0,d\}\oplus C\oplus Q=\mathbb Z_n
\]

is an actual direct tiling: in each block of length \(2g\), \(Q\) supplies its lower half and \(Q+g\) its upper half. These fixtures are **not anchored-target witnesses**.

| \(g\) | \(n\) | Missing head anchors | Missing tail anchors |
|---:|---:|---|---|
| 1 | 16 | 3, 8, 11 | 1, 7, 13 |
| 2 | 16 | 3, 8, 11 | 7, 14 |
| 3 | 18 | 8, 11 | none |
| 4 | 16 | 3, 8, 11 | 7, 13, 14 |
| 5 | 20 | 3, 8, 11 | 7 |
| 6 | 24 | 3, 8, 11 | 7 |
| 7 | 28 | 3, 8, 11 | 7, 13 |
| 8 | 16 | 3, 11 | 13, 14 |
| 9 | 18 | 3, 8, 11 | 13, 14 |
| 10 | 20 | 3, 8, 11 | 13, 14 |
| 11 | 22 | 3, 8 | 13, 14 |
| 12 | 24 | 3, 8, 11 | 13, 14 |
| 13 | 26 | 3, 8, 11 | 13, 14 |
| 14 | 28 | 3, 8, 11 | 14 |

These are written-verified constructions. Their programmatic coefficient checks remain **NOT_RUN**.

## 7. Mutation controls and their exact limits

### Dropping the head anchors

A genuine counterexample to the head-omitted exclusion is

\[
n=18,\ d=3,\ C=\{0\},
\]
\[
Q=\{0,1,2,6,7,8,12,13,14\}.
\]

It retains all five original tail anchors and has an actual two-point direct factor with gcd 3. It misses head anchors 8 and 11.

The proposed program accepts its actual direct tiling and tail anchors, then rejects the full anchored check specifically with `HEAD_ANCHOR`.

### Dropping the tail anchors

A genuine counterexample to the tail-omitted exclusion is

\[
n=24,\ d=1,\ C=\{0,2,4,6,8,10\},\qquad Q=\{0,12\}.
\]

Here \(P=\{0,1\}\oplus C=\{0,\ldots,11\}\), so all four original head anchors occur. Also \(P\oplus Q=\mathbb Z_{24}\), with gcd 1. Tail anchors 1, 7, 13, and 14 are missing.

The proposed program rejects the full anchored check specifically with `TAIL_ANCHOR`.

### Dropping weighted multiplicity equations

At \(g=8\), take the support shadow

\[
C_{\rm supp}=\{0,3\},\qquad Q_{\rm supp}=\{0,1,7,13,14\},
\]
\[
V=\{0,1,3,4,7,10,13,14\}.
\]

It satisfies the antipodal-selector, anchor, support-compatibility, and support-coverage conditions. With unit support weights, the convolution has coefficient 2 at residues 0 and 1 and coefficient 1 at the other occupied residues.

Thus it is a concrete false positive for replacing the weighted equation by support coverage. Moreover, §5 proves that **no permitted positive weights** repair it.

This control is **PROJECTION_ONLY / NOT_AN_ACTUAL_ANCHORED_TILING**. It does not become an actual counterexample by setting \(n=16\).

### Dropping the actual original-\(P\) factor hypothesis

**NOT_TESTED as an actual-target mutation.** No actual \(P\oplus Q\) tiling with all original anchors and without the required factor was constructed. A quotient shadow, a replacement tile, or the mere presence of the four-point rectangle would not be a valid substitute.

No counterexample or necessity claim for that mutation is reported.

All programmatic mutation outcomes remain **NOT_RUN**.

## 8. Complete independent standard-library source

Proposed filename: `independent-small-gcd-anchored-projection-v1.py`

**NOT_RUN. Not materialized. Source SHA: NOT_OBSERVED.**

The scientific source performs no file access, network access, subprocess creation, installation, deletion, or external mutation. It returns its complete result in `RESULT` and has a cooperative 55-second limit. No runtime bound is claimed to have been observed.

Each line below has the literal prefix `SRC|`; removing that prefix, and only that prefix, recovers the complete proposed source. `SRC|` alone denotes a blank line.

SRC|from collections import Counter
SRC|from fractions import Fraction
SRC|from math import gcd
SRC|from time import perf_counter
SRC|
SRC|HEAD = (0, 3, 8, 11)
SRC|TAIL = (0, 1, 7, 13, 14)
SRC|LIMIT_SECONDS = 55.0
SRC|
SRC|
SRC|class CheckError(Exception):
SRC|    pass
SRC|
SRC|
SRC|def need(condition, reason):
SRC|    if not condition:
SRC|        raise CheckError(reason)
SRC|
SRC|
SRC|def guard(start):
SRC|    need(perf_counter() - start < LIMIT_SECONDS, "LIMIT_55_SECONDS")
SRC|
SRC|
SRC|def sums_mod(A, B, modulus):
SRC|    return {(a + b) % modulus for a in A for b in B}
SRC|
SRC|
SRC|def support_shadow(g, V, C, Q):
SRC|    m = 2 * g
SRC|    V, C, Q = set(V), set(C), set(Q)
SRC|    universe = set(range(m))
SRC|    need(V <= universe and C <= universe and Q <= universe,
SRC|         "SUPPORT_RANGE")
SRC|    need(len(V) == g, "SELECTOR_SIZE")
SRC|    need(not (V & {(v + g) % m for v in V}), "ANTIPODAL_PAIR")
SRC|    need(V | {(v + g) % m for v in V} == universe,
SRC|         "SELECTOR_COVERAGE")
SRC|    need(0 in C, "C_ORIENTATION")
SRC|    need({q % m for q in TAIL} <= Q, "TAIL_SUPPORT")
SRC|    need({a % m for a in HEAD} <= sums_mod(C, (0, g), m),
SRC|         "HEAD_SUPPORT")
SRC|    occupied = sums_mod(C, Q, m)
SRC|    need(occupied <= V, "SUPPORT_OUTSIDE_V")
SRC|    need(occupied == V, "SUPPORT_MISSING_V")
SRC|    return Counter((c + q) % m for c in C for q in Q)
SRC|
SRC|
SRC|def enumerate_supports(start):
SRC|    statistics = []
SRC|    survivors = {}
SRC|    for g in range(1, 15):
SRC|        guard(start)
SRC|        m = 2 * g
SRC|        q_lower = Counter(q % m for q in TAIL)
SRC|        h_lower = Counter(a % m for a in HEAD)
SRC|        S = set(q_lower)
SRC|        seen = 0
SRC|        tail_count = 0
SRC|        candidates = []
SRC|        for mask in range(1 << g):
SRC|            if mask % 256 == 0:
SRC|                guard(start)
SRC|            seen += 1
SRC|            V = {r + g * ((mask >> r) & 1) for r in range(g)}
SRC|            if not S <= V:
SRC|                continue
SRC|            tail_count += 1
SRC|            D = {c for c in range(m)
SRC|                 if all((s + c) % m in V for s in S)}
SRC|            need(0 in D, "NORMALIZED_C_ZERO_LOST")
SRC|            options = {
SRC|                a: D & {a % m, (a - g) % m}
SRC|                for a in HEAD
SRC|            }
SRC|            if any(not choice for choice in options.values()):
SRC|                continue
SRC|            forced = {0}
SRC|            for choice in options.values():
SRC|                if len(choice) == 1:
SRC|                    forced.update(choice)
SRC|            Qmax = {
SRC|                q for q in range(m)
SRC|                if all((c + q) % m in V for c in forced)
SRC|            }
SRC|            need(S <= Qmax, "FORCED_Q_BOUND_LOST_TAIL")
SRC|            support_shadow(g, V, forced, S)
SRC|            minimal_head = Counter(
SRC|                (c + b) % m for c in forced for b in (0, g)
SRC|            )
SRC|            need(all(minimal_head[r] >= k for r, k in h_lower.items()),
SRC|                 "ORIGINAL_HEAD_LOWER_MULTIPLICITY")
SRC|            candidates.append({
SRC|                "g": g,
SRC|                "modulus": m,
SRC|                "V": tuple(sorted(V)),
SRC|                "Cmax": tuple(sorted(D)),
SRC|                "forced_C": tuple(sorted(forced)),
SRC|                "Qmax": tuple(sorted(Qmax)),
SRC|                "head_lower": tuple(sorted(h_lower.items())),
SRC|                "tail_lower": tuple(sorted(q_lower.items())),
SRC|                "head_options": tuple(
SRC|                    (a, tuple(sorted(options[a]))) for a in HEAD
SRC|                ),
SRC|            })
SRC|        need(seen == 1 << g, "SELECTOR_ENUMERATION_COUNT")
SRC|        statistics.append((g, seen, tail_count, len(candidates)))
SRC|        if candidates:
SRC|            survivors[g] = candidates
SRC|    return statistics, survivors
SRC|
SRC|
SRC|EXPECTED_SHAPES = {
SRC|    8: {
SRC|        "V": (0, 1, 3, 4, 7, 10, 13, 14),
SRC|        "Cmax": (0, 3),
SRC|        "forced_C": (0, 3),
SRC|        "Qmax": (0, 1, 4, 7, 10, 13, 14),
SRC|    },
SRC|    10: {
SRC|        "V": (0, 1, 2, 6, 7, 8, 9, 13, 14, 15),
SRC|        "Cmax": (0, 1, 7, 8, 13, 14),
SRC|        "forced_C": (0, 1, 8, 13),
SRC|        "Qmax": (0, 1, 7, 13, 14),
SRC|    },
SRC|    11: {
SRC|        "V": (0, 1, 5, 6, 7, 8, 9, 13, 14, 15, 21),
SRC|        "Cmax": (0, 8, 14),
SRC|        "forced_C": (0, 8, 14),
SRC|        "Qmax": (0, 1, 7, 13, 14, 15, 21),
SRC|    },
SRC|}
SRC|
SRC|
SRC|def incidence(record):
SRC|    m = record["modulus"]
SRC|    rows = {s: {} for s in range(m)}
SRC|    for c in record["Cmax"]:
SRC|        for q in record["Qmax"]:
SRC|            row = rows[(c + q) % m]
SRC|            pair = (c, q)
SRC|            row[pair] = row.get(pair, Fraction(0)) + Fraction(1)
SRC|    V = set(record["V"])
SRC|    need({s for s in range(m) if rows[s]} == V,
SRC|         "INCIDENCE_OCCUPIED_ROWS")
SRC|    return rows
SRC|
SRC|
SRC|def strict_edge(record, rows, singleton_s, comparison_s,
SRC|                smaller_c, positive_witness):
SRC|    V = set(record["V"])
SRC|    need(singleton_s in V and comparison_s in V,
SRC|         "CERTIFICATE_NOT_TWO_OCCUPIED_ROWS")
SRC|    single = rows[singleton_s]
SRC|    need(len(single) == 1, "CERTIFICATE_NOT_SINGLETON")
SRC|    (larger_c, shared_q), coefficient = next(iter(single.items()))
SRC|    need(coefficient == Fraction(1), "CERTIFICATE_SINGLETON_COEFFICIENT")
SRC|    forced = set(record["forced_C"])
SRC|    q_lower = dict(record["tail_lower"])
SRC|    need(larger_c in forced and smaller_c in forced,
SRC|         "CERTIFICATE_UNFORCED_C_POSITIVITY")
SRC|    need(q_lower.get(shared_q, 0) > 0,
SRC|         "CERTIFICATE_UNPROVIDED_SHARED_Q_POSITIVITY")
SRC|    remainder = dict(rows[comparison_s])
SRC|    target = (smaller_c, shared_q)
SRC|    remainder[target] = remainder.get(target, Fraction(0)) - Fraction(1)
SRC|    need(all(value >= 0 for value in remainder.values()),
SRC|         "CERTIFICATE_NEGATIVE_REMAINDER")
SRC|    need(remainder.get(positive_witness, Fraction(0)) > 0,
SRC|         "CERTIFICATE_MISSING_STRICT_WITNESS")
SRC|    witness_c, witness_q = positive_witness
SRC|    need(witness_c in forced,
SRC|         "CERTIFICATE_UNFORCED_WITNESS_C_POSITIVITY")
SRC|    need(q_lower.get(witness_q, 0) > 0,
SRC|         "CERTIFICATE_UNPROVIDED_WITNESS_Q_POSITIVITY")
SRC|    return {
SRC|        "strict_edge": (larger_c, smaller_c),
SRC|        "shared_positive_q": shared_q,
SRC|        "singleton_row": singleton_s,
SRC|        "comparison_row": comparison_s,
SRC|        "positive_witness": positive_witness,
SRC|        "nonnegative_remainder": tuple(
SRC|            (c, q, str(value))
SRC|            for (c, q), value in sorted(remainder.items())
SRC|            if value
SRC|        ),
SRC|    }
SRC|
SRC|
SRC|CERTIFICATES = {
SRC|    8: ((3, 0, 0, (3, 13)), (14, 1, 3, (0, 1))),
SRC|    10: ((6, 1, 8, (0, 1)), (9, 14, 13, (0, 14))),
SRC|    11: ((6, 0, 8, (0, 0)), (8, 14, 14, (0, 14))),
SRC|}
SRC|
SRC|
SRC|def verify_symbolic_cycle(record, rows):
SRC|    evidence = [
SRC|        strict_edge(record, rows, *spec)
SRC|        for spec in CERTIFICATES[record["g"]]
SRC|    ]
SRC|    first, second = (item["strict_edge"] for item in evidence)
SRC|    need(first[0] != first[1], "CERTIFICATE_TRIVIAL_EDGE")
SRC|    need(first == (second[1], second[0]),
SRC|         "CERTIFICATE_NO_STRICT_TWO_CYCLE")
SRC|    return {
SRC|        "status": "INFEASIBLE_BY_EXACT_POSITIVE_WEIGHT_CERTIFICATE",
SRC|        "evidence": tuple(evidence),
SRC|    }
SRC|
SRC|
SRC|def residues(values, n, name):
SRC|    values = tuple(values)
SRC|    need(bool(values), name + "_EMPTY")
SRC|    need(all(type(x) is int and 0 <= x < n for x in values),
SRC|         name + "_RANGE")
SRC|    need(len(set(values)) == len(values), name + "_DUPLICATE")
SRC|    return values
SRC|
SRC|
SRC|def actual_tiling(n, d, C, Q):
SRC|    need(type(n) is int and n > 14, "N_GT_14")
SRC|    need(type(d) is int and 0 < d < n, "DISTINCT_TWO_POINT_FACTOR")
SRC|    C = residues(C, n, "C")
SRC|    Q = residues(Q, n, "Q")
SRC|    P_ordered = tuple((c + b) % n for c in C for b in (0, d))
SRC|    need(len(set(P_ordered)) == 2 * len(C), "ORIGINAL_P_FACTOR_NOT_DIRECT")
SRC|    P = set(P_ordered)
SRC|    total = Counter(
SRC|        (c + b + q) % n for c in C for b in (0, d) for q in Q
SRC|    )
SRC|    need(all(total[x] == 1 for x in range(n)),
SRC|         "ORIGINAL_ORDERED_SUM_NOT_EXACTLY_ONE")
SRC|    t_counts = Counter((c + q) % n for c in C for q in Q)
SRC|    need(all(value == 1 for value in t_counts.values()),
SRC|         "C_PLUS_Q_NOT_DIRECT")
SRC|    g = gcd(d, n)
SRC|    m = 2 * g
SRC|    need(n % m == 0, "TWO_POINT_ORDER_NOT_EVEN")
SRC|    L = n // m
SRC|    T = set(t_counts)
SRC|    V = {x % m for x in T}
SRC|    need(T == {x for x in range(n) if x % m in V},
SRC|         "ACTUAL_T_NOT_COMPLETE_RESIDUE_CLASSES")
SRC|    need(len(V) == g and not (V & {(v + g) % m for v in V}),
SRC|         "ACTUAL_T_NOT_ANTIPODAL_SELECTOR")
SRC|    c_counts = Counter(c % m for c in C)
SRC|    q_counts = Counter(q % m for q in Q)
SRC|    coefficients = tuple(
SRC|        sum(c_counts[i] * q_counts[(s - i) % m] for i in range(m))
SRC|        for s in range(m)
SRC|    )
SRC|    need(coefficients == tuple(L * int(s in V) for s in range(m)),
SRC|         "ORIGINAL_WEIGHTED_PROJECTION_EQUATION")
SRC|    return {
SRC|        "n": n, "d": d, "g": g, "L": L,
SRC|        "C": tuple(sorted(C)), "Q": tuple(sorted(Q)),
SRC|        "P": tuple(sorted(P)), "V": tuple(sorted(V)),
SRC|        "projected_C_counts": tuple(sorted(c_counts.items())),
SRC|        "projected_Q_counts": tuple(sorted(q_counts.items())),
SRC|        "weighted_coefficients": coefficients,
SRC|        "missing_head": tuple(a for a in HEAD if a not in P),
SRC|        "missing_tail": tuple(q for q in TAIL if q not in set(Q)),
SRC|    }
SRC|
SRC|
SRC|def anchor_check(record, require_head=True, require_tail=True):
SRC|    if require_head:
SRC|        need(not record["missing_head"],
SRC|             "HEAD_ANCHOR:" + repr(record["missing_head"]))
SRC|    if require_tail:
SRC|        need(not record["missing_tail"],
SRC|             "TAIL_ANCHOR:" + repr(record["missing_tail"]))
SRC|
SRC|
SRC|def expect_reason(operation, prefix):
SRC|    try:
SRC|        operation()
SRC|    except CheckError as error:
SRC|        reason = str(error)
SRC|        need(reason.startswith(prefix), "WRONG_CONTROL_REASON:" + reason)
SRC|        return reason
SRC|    raise CheckError("CONTROL_NOT_REJECTED:" + prefix)
SRC|
SRC|
SRC|def run():
SRC|    start = perf_counter()
SRC|    statistics, survivors = enumerate_supports(start)
SRC|    expected_tail = (0, 0, 1, 0, 1, 0, 0, 8, 16, 32, 64, 0, 0, 0)
SRC|    expected_head = (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0)
SRC|    need(tuple(row[2] for row in statistics) == expected_tail,
SRC|         "TAIL_SELECTOR_COUNT_DISAGREEMENT")
SRC|    need(tuple(row[3] for row in statistics) == expected_head,
SRC|         "HEAD_SUPPORT_COUNT_DISAGREEMENT")
SRC|    need(sum(row[1] for row in statistics) == 32766,
SRC|         "TOTAL_SELECTOR_COUNT")
SRC|    need(set(survivors) == {8, 10, 11}, "UNEXPECTED_SUPPORT_SURVIVOR")
SRC|    tables = {}
SRC|    proofs = {}
SRC|    selected = {}
SRC|    for g in (8, 10, 11):
SRC|        guard(start)
SRC|        need(len(survivors[g]) == 1, "NONUNIQUE_SUPPORT_SHADOW")
SRC|        record = survivors[g][0]
SRC|        for key, expected in EXPECTED_SHAPES[g].items():
SRC|            need(record[key] == expected,
SRC|                 "SUPPORT_SHAPE_DISAGREEMENT:" + repr((g, key)))
SRC|        rows = incidence(record)
SRC|        tables[g] = tuple(
SRC|            (s, tuple(sorted(rows[s]))) for s in range(record["modulus"])
SRC|        )
SRC|        proofs[g] = verify_symbolic_cycle(record, rows)
SRC|        selected[g] = record
SRC|    genuine = {}
SRC|    for g in range(1, 15):
SRC|        guard(start)
SRC|        m = 2 * g
SRC|        L = (15 + m - 1) // m
SRC|        n = m * L
SRC|        Q = tuple(x for x in range(n) if x % m < g)
SRC|        record = actual_tiling(n, g, (0,), Q)
SRC|        need(record["g"] == g, "GENUINE_FIXTURE_WRONG_GCD")
SRC|        need(bool(record["missing_head"]), "GENUINE_FIXTURE_ACCIDENTAL_TARGET")
SRC|        genuine[g] = record
SRC|    head_control = genuine[3]
SRC|    anchor_check(head_control, require_head=False, require_tail=True)
SRC|    head_reason = expect_reason(
SRC|        lambda: anchor_check(head_control), "HEAD_ANCHOR:"
SRC|    )
SRC|    tail_control = actual_tiling(
SRC|        24, 1, tuple(range(0, 12, 2)), (0, 12)
SRC|    )
SRC|    anchor_check(tail_control, require_head=True, require_tail=False)
SRC|    tail_reason = expect_reason(
SRC|        lambda: anchor_check(tail_control), "TAIL_ANCHOR:"
SRC|    )
SRC|    shadow8 = selected[8]
SRC|    unit_counts = support_shadow(
SRC|        8, shadow8["V"], shadow8["forced_C"], TAIL
SRC|    )
SRC|    need(len({unit_counts[s] for s in shadow8["V"]}) > 1,
SRC|         "WEIGHTED_CONTROL_NOT_NONCONSTANT")
SRC|    need(proofs[8]["status"] ==
SRC|         "INFEASIBLE_BY_EXACT_POSITIVE_WEIGHT_CERTIFICATE",
SRC|         "WEIGHTED_CONTROL_MISSING_ALL_WEIGHT_CERTIFICATE")
SRC|    controls = {
SRC|        "drop_head": {
SRC|            "status": "GENUINE_NON_TARGET_COUNTEREXAMPLE",
SRC|            "fixture": head_control,
SRC|            "intended_full_check_rejection": head_reason,
SRC|        },
SRC|        "drop_tail": {
SRC|            "status": "GENUINE_NON_TARGET_COUNTEREXAMPLE",
SRC|            "fixture": tail_control,
SRC|            "intended_full_check_rejection": tail_reason,
SRC|        },
SRC|        "drop_weighted_multiplicities": {
SRC|            "status": "PROJECTION_ONLY_SUPPORT_FALSE_POSITIVE",
SRC|            "not_an_actual_anchored_tiling": True,
SRC|            "g": 8,
SRC|            "C_support": shadow8["forced_C"],
SRC|            "Q_support": TAIL,
SRC|            "V": shadow8["V"],
SRC|            "unit_convolution": tuple(sorted(unit_counts.items())),
SRC|            "all_positive_weights_rejected_by": proofs[8],
SRC|        },
SRC|        "drop_actual_original_P_factor": {
SRC|            "status": "NOT_TESTED",
SRC|            "reason": (
SRC|                "No actual tiling with all original anchors and without "
SRC|                "the factor was constructed; shadows are not substitutes."
SRC|            ),
SRC|        },
SRC|    }
SRC|    guard(start)
SRC|    return {
SRC|        "method": (
SRC|            "EXHAUSTIVE_NECESSARY_PROJECTED_SUPPORT_SCREEN_AND_"
SRC|            "EXACT_SYMBOLIC_POSITIVE_WEIGHT_CERTIFICATES"
SRC|        ),
SRC|        "not_an_original_tiling_solver": True,
SRC|        "head_anchors": HEAD,
SRC|        "tail_anchors": TAIL,
SRC|        "selector_statistics": tuple(statistics),
SRC|        "support_shadows": selected,
SRC|        "all_residue_incidence_tables": tables,
SRC|        "positive_weight_certificates": proofs,
SRC|        "genuine_non_target_tilings": genuine,
SRC|        "mutation_controls": controls,
SRC|        "scope": (
SRC|            "Necessary shadows excluded for g=1..14; no unrestricted "
SRC|            "anchored nonexistence, original factor existence, novelty, "
SRC|            "independent-family, human, or kernel assurance."
SRC|        ),
SRC|        "elapsed_seconds": perf_counter() - start,
SRC|    }
SRC|
SRC|
SRC|RESULT = run()

### Proposed execution command — NOT_RUN

After ordinary parent materialization and source review, the corresponding transparent receipt-producing invocation would be:

`python3 -B -c "import runpy; from pprint import pprint; pprint(runpy.run_path('independent-small-gcd-anchored-projection-v1.py')['RESULT'])"`

This command is supplied for reproducibility only. I did not execute it, invoke an adapter, or observe its output. The source contains no fabricated saved result.

## 9. Disposition and remaining gates

- **Independent written reconstruction:** no mathematical defect identified in the periodic reduction, orientation, support exclusions, complete incidence rows, or positive-weight contradictions.
- **Finite execution gate:** **NOT_RUN / NOT_PASSED**, due to the disclosed runtime restriction.
- **Actual-target witnesses:** none supplied. The fourteen genuine tilings are explicitly non-target controls; the three anchored support shadows are explicitly not actual tilings.
- **Actual-factor mutation:** **NOT_TESTED**; no false counterexample is claimed.
- **Unpaid original-target step:** establish a suitable actual global two-point factor for the remaining heads, or exclude those heads by another argument. This return does neither.
- **Assurance ceiling:** same-harness independent checker authorship and written reconstruction only. No external-family, human, kernel/formal, novelty, priority, complete-family, or unrestricted anchored-nonexistence credit.

**Findings:** No evidence-backed mathematical defect identified.

**overall_correctness:** correct

**explanation:** The proposed small-gcd obstruction survives the independent written reconstruction, including the original-factor consuming equation and all three positive-weight contradictions. The complete independent finite checker is supplied but was not run, so this return does not pass the finite execution gate. The actual-factor hypothesis and unrestricted anchored problem remain outside the established conclusion.

**confidence:** 0.94