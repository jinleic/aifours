# author-candidate-v1.md — Independent exact finite lemmas for the actual \(3555\) branch

**Role:** FINITE, f531.  
**Status:** Written reconstruction and complete independent checker source returned. **Scientific execution: NOT_RUN.** No finite-run PASS or whole-branch adoption is claimed.

## 1. Input binding, chronology, and execution boundary

Frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f531-ame3555-independent-exact-prism-and-incidence-finite-check/`

Assigned pins:

- Manifest: `e24a828cd478e3531a8a408f04c1d9de017175b6d8179f7cf554fd998ae66c14`
- Freeze receipt: `1116f5cd09c7e48e7a70aabe598179231e241a6e844a47bf030b4e2d56a1c872`
- Literal packet: `ae30fc939191474b4c411a7e33eab356c9413ae31bbe055a4ac942c196ec9f1c`
- Sole scientific source S1: `6a3013bc0168976faf830287ebeb41af608f57441e835f7316d411c81f666338`

The matching hashes, byte/LF counts, and clock `2026-10-30T12:40:23-0700 PDT` are **parent-supplied observations** from `parent-live-metadata-supply-v1.json`, not my native hash computation, execution receipt, or start time.

Before opening the scientific packet, I read the complete manifest, receipt, dispatch receipt, parent metadata supply, and every declared permission/status control through its ending. I then sent Main a direct pre-body ACK. After that ACK, I read packet LF 1–643 in strictly increasing, exact raw windows of at most 20 lines, including the final window LF 641–643. This covered all S1 logical lines 1–641; the supplied source metadata records 640 LF bytes.

No held scientific payload, linked scientific source, sibling result, author code, or external scientific source was opened. No external-model CLI, subprocess campaign, installation, network calculation, file mutation, or scientific executable was used. This is a same-harness check, not independent-family, human, formal-kernel, or novelty certification.

Although the frozen FINITE task permits bounded calculations, the active higher-priority runtime restricts shell use to read-only review commands and forbids file edits. I did not bypass that restriction through another executor. The checker below is therefore **unexecuted source**, with an exact prospective argv and clearly separated written expectations. No file was materialized.

## 2. Actual target and what this return checks

The source proposes exclusion of one actual tensor \(U=6\psi\) satisfying:

1. All three balanced flattenings of the same \(U\) are unitary.
2. There are 48 nonzero tensor entries.
3. Exactly 24 entries have modulus one.
4. The remaining 24 entries use residual alphabets of sizes \(q=(3,5,5,5)\).

Let \(P\) denote the 24 modulus-one words and \(E\) the other 24 words. A modulus-one entry exhausts its row and column. Consequently, in every balanced flattening, deleting the 24 singleton rows and columns leaves a \(12\times12\) unitary with 24 nonzeros. Every remaining row and column has degree two.

A simple degree-two bipartite support graph is a union of even cycles. A cycle longer than four supplies two rows with exactly one common nonzero column, which cannot be orthogonal over \(\mathbb C\). Thus every residual flattening consists of six full \(2\times2\) blocks. Every physical pair value occurring in \(E\) has exactly two extensions, and every physical pair projection has size 12.

The calculations below check necessary finite interfaces derived from that actual common-support setting. In particular:

- A twelve-word prism is **not** an AME witness.
- A synthetic 24-word set passing pair-multiplicity checks is **not** an actual admissible residual tensor.
- Locally compatible outside-degree interfaces are **not** a reconstruction of a common \(P,E\).
- Finite support checks do **not** constitute an exhaustive complex-amplitude calculation.

## 3. Written reconstruction of the integer shadows

### 3.1 Moments and maximal-word types

Put \(b=(3,1,1,1)\), where \(b_i=6-q_i\). Let \(n_s\) count maximal words with exactly \(s\) internal coordinates.

Single-coordinate incidences give

\[
\sum_s n_s=24,\qquad
\sum_s s n_s=\sum_i(24-6b_i)=60.
\]

Internal physical-pair incidences give

\[
\sum_s\binom{s}{2}n_s
=\sum_{i<j}(q_iq_j-12)
=3(15)+3(25)-72=48.
\]

Subtracting twice the first-moment equation and adding three times the total-count equation yields

\[
3n_0+n_1+n_4=0.
\]

Therefore the unique nonnegative integer profile is

\[
(n_0,n_1,n_2,n_3,n_4)=(0,0,12,12,0).
\]

This binds the second moment to **48**, not 49. If 49 is substituted, the nonnegative profiles instead include exactly

\[
(0,1,10,13,0),\qquad (0,0,13,10,1).
\]

They are negative controls, not legal \(3555\) profiles.

For a maximal double internal at \(i,j\), its two outside coordinates exhaust one outside-pair value. Thus

\[
d_{ij}=b_kb_l.
\]

In physical-pair order \(01,02,03,12,13,23\), the counts are

\[
(1,1,1,3,3,3).
\]

The number of maximal triples missing coordinate \(i\) is

\[
\tau_i=6b_i-b_i\sum_{j\ne i}b_j=b_i^2,
\]

giving \((9,1,1,1)\).

The outside-containing physical pair counts are independently fixed:

- \(B_0B_j\): 3;
- \(B_jB_k\), \(j,k\in\{1,2,3\}\): 1;
- \(A_0B_j\): 3;
- \(A_jB_0\): 15;
- \(A_jB_k\), distinct five-symbol parties: 5.

### 3.2 Symbol degrees and profiles

For an internal symbol at party \(i\), let \(r\) be its residual degree in any other physical-pair system. Its maximal multiplicity is \(6-r\). If \(d,t\) count its maximal double and triple occurrences, then

\[
d+t=6-r,\qquad 2d+t=6-b_i,
\]

so

\[
d=r-b_i,\qquad t=6+b_i-2r.
\]

At party 0, nonnegativity and the sum of degrees force

\[
r_0=(4,4,4),\qquad(d,t)=(1,1)
\]

at every symbol.

At each other party, \(2\le r\le3\), and five degrees sum to 12. Hence

\[
r=(3,3,2,2,2).
\]

There are ten ordered degree vectors per five-symbol party, corresponding to the choice of its two high symbols. A high has \((d,t)=(2,1)\); a low has \((d,t)=(1,3)\).

### 3.3 The low-label gauge is physical, not independent per pair

Let \(a_i\) be the party-0 symbol used by the unique maximal double internal at \(0,i\). Its unique other maximal occurrence is the triple missing party \(i\). Label each low at party \(j\) by the physical missing pair:

\[
(a_i,\ell_j^i)\notin R_{0j}.
\]

These labels are anchored to the same maximal words. In particular, the triple missing party \(i\) forces

\[
(\ell_j^i,\ell_k^i)\notin R_{jk},
\qquad \{i,j,k\}=\{1,2,3\}.
\]

A genuine relabelling of a party is allowed if all words and incidences are transformed covariantly. What is invalid is changing a local missing-pair map while holding the physical words fixed. The checker includes both a positive covariant-relabelling control and a negative inconsistent-gauge control.

## 4. Six-edge prisms: exact enumeration domain and incidence proof

An abstract prism base has six distinct edges in a simple \(3\times3\) bipartite graph, with all vertex degrees two. Its complement is a perfect matching, so there are exactly \(3!=6\) labelled graphs. Each is a six-cycle.

Assign three edge colors, each used twice, with no equal colors at incident edges. For one fixed cycle, the number is 24. One direct count starts with \(6!/(2!^3)=90\) cyclic position assignments. For each color, its two occurrences are adjacent in 36 assignments; for each pair of colors both adjacencies occur in 18; all three occur in 12. Inclusion–exclusion gives

\[
90-3(36)+3(18)-12=24.
\]

Thus there are \(6\cdot24=144\) labelled colored bases.

For a base \(W\), lift every colored edge to both values of a two-symbol high alphabet:

\[
\{(a,j,k,h):(a,j,k)\in W,\ h\in\{0,1\}\}.
\]

This has twelve distinct words. Independently checking all six physical pair systems gives:

- projection size six in each system;
- exactly two extensions of every occurring pair;
- no repeated physical \(0j\) or \(0k\) pair in the colored base;
- three \(K_{2,2}\) components in each balanced cut.

These are **partial-support incidence facts**. They neither normalize a full \(36\times36\) flattening nor produce an actual AME state.

For the source’s physical prism lemma, an off-label low–low edge fixes its party-0 color to the third label. Block closure forces both extensions to be the two high symbols at the remaining party, and forces every color’s two base edges to duplicate at both highs. The full residual multiplicity of those two high symbols exhausts the twelve-word prism. This is the consuming-side connection to the common \(E\); an independently selected local prism would not suffice.

## 5. All eight interaction graphs

Let \(G\) have vertices \(1,2,3\), with an edge precisely when that physical pair system contains an off-label low–low edge. The checker iterates masks 0 through 7 explicitly.

For every active prism center \(l\), it enumerates its two three-symbol vertex sets, every six-cycle on them, admissible physical colorings, and every simple six-edge outside graph with degree sequences

\[
r_j(v)-2\,1_{v\in V_j},\qquad
r_k(w)-2\,1_{w\in V_k}.
\]

It enforces disjoint inside/outside pair supports, the physical forbidden equal-label pair, the implications of absent \(G\)-edges, and identical high neighborhoods when another prism center is active. These remain necessary local interfaces, not global realizations.

The written case exhaustion is:

- **One edge:** Both prism vertex sets must contain only lows. The twelve outside words would need six distinct pairs in a \(2\times2\) high box, which has only four.
- **Two edges:** At a suitable prism, one vertex set is all lows and the other is both highs plus one low. Outside degrees force a two-edge high–high matching. The second prism instead requires the two high symbols to have identical neighborhoods.
- **Three edges, an empty high–high block:** Outside degrees again force a two-edge matching in another high–high block. With prisms at all centers, every such block must be empty or complete.
- **Three edges, all high–high blocks complete:** Every prism has one low vertex on each side, and its generating low–low edge is present. Its six-cycle therefore has \(6-2-2+1=3\) high–high edges. The same common residual support consequently induces six distinct binary high triples with all three pair projections of size three.

The last condition is impossible. There are only \(\binom86=28\) six-subsets of a binary cube. Written classification by the two omitted vertices gives:

- 4 subsets with signature \((3,4,4)\);
- 4 with \((4,3,4)\);
- 4 with \((4,4,3)\);
- 16 with \((4,4,4)\).

No signature is \((3,3,3)\). Indeed, already two nonfull pair projections are impossible at cardinality six. Consequently, omitting the third projection is a coverage defect but cannot create a mathematical false positive if the other two size-three conditions and cardinality six remain enforced. The corresponding control below tests **coverage**, not a nonexistent six-element counterexample.

## 6. Zero-edge case, stars, and the complex obstruction

When \(G\) is empty, multiple lows in one residual word must share a label. Three lows are impossible because their physical pair opposite that label’s party is forbidden by the maximal triple.

Let \(N_t\) count residual words with \(t\) lows. Then

\[
N_0+N_1+N_2=24,\qquad N_1+2N_2=36.
\]

If \(m\) is the number of occurring low–low pair values, then \(N_2=2m\). Exactly six equal-label low–low pair values are allowable: for each label, the two-edge star centered at its own party. Thus \(m\le6\), forcing

\[
(N_0,N_1,N_2,m)=(0,12,12,6).
\]

All six allowable star edges occur.

For a fixed label \(i\), the center low has one peripheral low and one high neighbor at either other party. The peripheral-low/peripheral-low pair is forbidden. Its four words therefore use the two cross pairs twice each. Distinctness forces the two allowed party-0 values to occur once each. Pair exhaustion then forces the other words containing either peripheral low to use the opposite high at the other peripheral party, again once at each allowed party-0 value.

Hence

\[
E=\bigsqcup_{i=1}^3 (A_0\setminus\{a_i\})\times F_i,
\]

with four triples in each \(F_i\). This pairing is derived; distance-one pairs have not been excluded.

Fix a high \(h\) at party \(j\). If \(f_i\) counts triples in \(F_i\) using \(h\), the three \(0j\)-pair multiplicities give

\[
f_2+f_3=f_1+f_3=f_1+f_2=2.
\]

Thus \(f_1=f_2=f_3=1\). Their other-party pairs \(c_i\) are distinct because each contains a low of its own label. The three rows \((a_s,h)\) therefore have exactly the complement-diagonal pattern

\[
\text{row }s\text{ contains column }i \iff s\ne i.
\]

Each two rows overlap in exactly one column.

This last contradiction is an **all-complex written argument**, not a finite phase experiment. If the two nonzero entries in their unique shared column are \(x,y\), their inner product is \(x\overline y\ne0\). Equivalently, for \(x=u+iv\), \(y=s+it\),

\[
|x\overline y|^2=(u^2+v^2)(s^2+t^2)>0.
\]

No phase choice, unequal modulus, or shared-variable coupling can make that single nonzero product vanish.

## 7. Independent checker: execution status and exact argv

**Observed execution results:** none. The source below has not been parsed or executed by an interpreter in this duty.

**Written expectations:** the moment profiles, degree-profile counts, 144 abstract colored prisms, binary-cube histogram, zero-case count shadow, and reason-specific control outcomes follow from the arguments above. The enumerator’s detailed local-interface counts and synthetic weak-support count are deliberately not guessed.

Prospective argv consists of exactly four arguments:

- argv[0]: `python3`
- argv[1]: `-B`
- argv[2]: `-c`
- argv[3]: the complete source below, reconstructed by removing the initial three characters `PY|` from each source line and joining the resulting lines with LF, including a final LF.

The source uses only the standard library, does not open files or sockets, creates no children, and performs no installation or deletion. It has a cooperative 55-second deadline. A deadline exception means **INCOMPLETE**, never PASS. The final completion message is reached only after every declared check and control.

### Complete source — NOT_RUN

PY|from collections import Counter, defaultdict
PY|from functools import lru_cache
PY|from itertools import combinations, permutations, product
PY|from time import monotonic
PY|
PY|START = monotonic()
PY|Q = (3, 5, 5, 5)
PY|B = tuple(6 - x for x in Q)
PY|I = (1, 2, 3)
PY|H = (3, 4)
PY|PAIRS = tuple(combinations(range(4), 2))
PY|GEDGES = tuple(combinations(I, 2))
PY|CUBE_PAIRS = tuple(combinations(range(3), 2))
PY|VSETS = tuple(combinations(range(5), 3))
PY|GRAPHS = ()
PY|BY_GRAPH = {}
PY|
PY|class Bad(Exception):
PY|    pass
PY|
PY|def tick():
PY|    if monotonic() - START >= 55:
PY|        raise RuntimeError("INCOMPLETE_55_SECOND_DEADLINE")
PY|
PY|def need(ok, reason):
PY|    if not ok:
PY|        raise Bad(reason)
PY|
PY|def accepted(fn):
PY|    try:
PY|        fn()
PY|    except Bad:
PY|        return False
PY|    return True
PY|
PY|def expect_bad(reason, fn):
PY|    try:
PY|        fn()
PY|    except Bad as exc:
PY|        need(str(exc) == reason, "WRONG_REJECTION_REASON")
PY|        return reason
PY|    raise Bad("NEGATIVE_CONTROL_ACCEPTED")
PY|
PY|def compositions(total, length):
PY|    if length == 1:
PY|        yield (total,)
PY|        return
PY|    for first in range(total + 1):
PY|        for rest in compositions(total - first, length - 1):
PY|            yield (first,) + rest
PY|
PY|def moment_profiles(second):
PY|    found = []
PY|    for v in compositions(24, 5):
PY|        tick()
PY|        if sum(s * v[s] for s in range(5)) != 60:
PY|            continue
PY|        if sum(s * (s - 1) // 2 * v[s] for s in range(5)) == second:
PY|            found.append(v)
PY|    return tuple(sorted(found))
PY|
PY|def check_moment_profile(v):
PY|    need(len(v) == 5 and all(type(x) is int and x >= 0 for x in v),
PY|         "PROFILE_DOMAIN")
PY|    need(sum(v) == 24, "WORD_TOTAL")
PY|    need(sum(s * v[s] for s in range(5)) == 60, "FIRST_MOMENT")
PY|    need(sum(s * (s - 1) // 2 * v[s] for s in range(5)) == 48,
PY|         "SECOND_MOMENT")
PY|
PY|def degree_profiles(i):
PY|    upper = min(Q[j] for j in range(4) if j != i)
PY|    out = []
PY|    for rs in product(range(2, upper + 1), repeat=Q[i]):
PY|        tick()
PY|        if sum(rs) != 12:
PY|            continue
PY|        if all(r - B[i] >= 0 and 6 + B[i] - 2 * r >= 0 for r in rs):
PY|            out.append(rs)
PY|    return tuple(out)
PY|
PY|def pair_tables(words):
PY|    return {p: Counter((w[p[0]], w[p[1]]) for w in words) for p in PAIRS}
PY|
PY|def check_pair_interface(words, projection_size):
PY|    need(len(set(words)) == len(words), "DISTINCT_TENSOR_WORDS")
PY|    for counts in pair_tables(words).values():
PY|        need(all(n == 2 for n in counts.values()), "PAIR_EXTENSION_TWO")
PY|        need(len(counts) == projection_size, "PAIR_PROJECTION_SIZE")
PY|
PY|def check_rows(rows):
PY|    need(all(len(nbrs) == 2 for nbrs in rows.values()), "ROW_DEGREE_TWO")
PY|    cols = Counter(c for nbrs in rows.values() for c in nbrs)
PY|    need(all(n == 2 for n in cols.values()), "COLUMN_DEGREE_TWO")
PY|    for r, s in combinations(rows, 2):
PY|        need(len(rows[r] & rows[s]) != 1, "ONE_COLUMN_OVERLAP")
PY|    groups = Counter(frozenset(nbrs) for nbrs in rows.values())
PY|    need(all(n == 2 for n in groups.values()), "NOT_K22_COMPONENTS")
PY|    return len(groups)
PY|
PY|def block_counts(words):
PY|    out = []
PY|    for left in ((0, 1), (0, 2), (0, 3)):
PY|        right = tuple(i for i in range(4) if i not in left)
PY|        rows = defaultdict(set)
PY|        for w in words:
PY|            rows[tuple(w[i] for i in left)].add(tuple(w[i] for i in right))
PY|        out.append(check_rows(rows))
PY|    return tuple(out)
PY|
PY|def make_stars():
PY|    out = []
PY|    for i in I:
PY|        a = i - 1
PY|        d = [a, 5, 5, 5]
PY|        d[i] = a
PY|        t = [a, a, a, a]
PY|        t[i] = 5
PY|        out.extend((tuple(d), tuple(t)))
PY|    return tuple(out)
PY|
PY|def check_gauge(stars, maps):
PY|    need(len(maps) == 3 and all(set(p) == {0, 1, 2} for p in maps),
PY|         "LOW_LABEL_MAP_DOMAIN")
PY|    for j in I:
PY|        actual = {(w[0], w[j]) for w in stars if w[j] < 5}
PY|        expected = {(a, maps[j - 1][a]) for a in range(3)}
PY|        need(actual == expected, "COMMON_PHYSICAL_LOW_GAUGE")
PY|
PY|def transform_stars(stars, maps):
PY|    out = []
PY|    for w in stars:
PY|        v = list(w)
PY|        for j in I:
PY|            if v[j] < 3:
PY|                v[j] = maps[j - 1][v[j]]
PY|        out.append(tuple(v))
PY|    return tuple(out)
PY|
PY|def check_w(w):
PY|    need(len(w) == 6, "SIX_COLORED_TRIPLES")
PY|    need(len(set(w)) == 6, "SIX_DISTINCT_COLORED_TRIPLES")
PY|    need(all(all(x in range(3) for x in e) for e in w), "PRISM_ALPHABET")
PY|    need(len({(j, k) for a, j, k in w}) == 6, "REPEATED_JK_EDGE")
PY|    need(Counter(a for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
PY|         "COLOR_MULTIPLICITY_TWO")
PY|    need(Counter(j for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
PY|         "PRISM_LEFT_DEGREE_TWO")
PY|    need(Counter(k for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
PY|         "PRISM_RIGHT_DEGREE_TWO")
PY|    need(len({(a, j) for a, j, k in w}) == 6, "REPEATED_0J_PAIR")
PY|    need(len({(a, k) for a, j, k in w}) == 6, "REPEATED_0K_PAIR")
PY|    adj = defaultdict(set)
PY|    for a, j, k in w:
PY|        adj[(0, j)].add((1, k))
PY|        adj[(1, k)].add((0, j))
PY|    seen = {(0, 0)}
PY|    todo = [(0, 0)]
PY|    while todo:
PY|        for v in adj[todo.pop()]:
PY|            if v not in seen:
PY|                seen.add(v)
PY|                todo.append(v)
PY|    need(len(seen) == 6, "NOT_SIX_CYCLE")
PY|
PY|def enumerate_prisms():
PY|    graphs = []
PY|    by_graph = {}
PY|    for edges in combinations(tuple(product(range(3), repeat=2)), 6):
PY|        tick()
PY|        if Counter(j for j, k in edges) != Counter({0: 2, 1: 2, 2: 2}):
PY|            continue
PY|        if Counter(k for j, k in edges) != Counter({0: 2, 1: 2, 2: 2}):
PY|            continue
PY|        graphs.append(edges)
PY|        colored = []
PY|        for colors in product(range(3), repeat=6):
PY|            if Counter(colors) != Counter({0: 2, 1: 2, 2: 2}):
PY|                continue
PY|            w = tuple((a, j, k) for a, (j, k) in zip(colors, edges))
PY|            if accepted(lambda: check_w(w)):
PY|                colored.append(w)
PY|        by_graph[edges] = tuple(colored)
PY|    need(len(graphs) == 6, "BARE_CYCLE_COUNT")
PY|    need(all(len(by_graph[g]) == 24 for g in graphs), "BALANCED_COLOR_COUNT")
PY|    for g in graphs:
PY|        for w in by_graph[g]:
PY|            lift = tuple((a, j, k, h) for a, j, k in w for h in range(2))
PY|            check_pair_interface(lift, 6)
PY|            need(block_counts(lift) == (3, 3, 3), "PRISM_BLOCK_COUNTS")
PY|    return tuple(graphs), by_graph
PY|
PY|@lru_cache(maxsize=100)
PY|def degree_graphs(rd, cd):
PY|    need(sum(rd) == 6 and sum(cd) == 6, "OUTSIDE_EDGE_TOTAL")
PY|    out = []
PY|    def visit(row, rem, edges):
PY|        tick()
PY|        if row == 5:
PY|            if not any(rem):
PY|                out.append(frozenset(edges))
PY|            return
PY|        available = tuple(c for c in range(5) if rem[c] > 0)
PY|        if len(available) < rd[row]:
PY|            return
PY|        for selected in combinations(available, rd[row]):
PY|            new = list(rem)
PY|            for c in selected:
PY|                new[c] -= 1
PY|            remaining_positive_rows = sum(x > 0 for x in rd[row + 1:])
PY|            if any(x > remaining_positive_rows for x in new):
PY|                continue
PY|            visit(row + 1, tuple(new),
PY|                  edges + tuple((row, c) for c in selected))
PY|    visit(0, cd, ())
PY|    return tuple(out)
PY|
PY|def edge(a, b):
PY|    return tuple(sorted((a, b)))
PY|
PY|def active_centers(g):
PY|    return {next(x for x in I if x not in e) for e in g}
PY|
PY|def local_interfaces(g, l):
PY|    centers = active_centers(g)
PY|    j, k = tuple(x for x in I if x != l)
PY|    count = 0
PY|    shapes = set()
PY|    for u, v in product(VSETS, repeat=2):
PY|        tick()
PY|        hu = sum(x in H for x in u)
PY|        hv = sum(x in H for x in v)
PY|        if hu and edge(j, l) not in g:
PY|            continue
PY|        if hv and edge(k, l) not in g:
PY|            continue
PY|        if (j in centers and hu == 1) or (k in centers and hv == 1):
PY|            continue
PY|        rd = tuple((2 if x < 3 else 3) - 2 * (x in u) for x in range(5))
PY|        cd = tuple((2 if x < 3 else 3) - 2 * (x in v) for x in range(5))
PY|        outside_graphs = degree_graphs(rd, cd)
PY|        for bare in GRAPHS:
PY|            inside = frozenset((u[r], v[c]) for r, c in bare)
PY|            if not any(x < 3 and y < 3 and x != y for x, y in inside):
PY|                continue
PY|            color_ok = any(
PY|                all((u[r] >= 3 or a != u[r]) and
PY|                    (v[c] >= 3 or a != v[c]) for a, r, c in w)
PY|                for w in BY_GRAPH[bare])
PY|            if not color_ok:
PY|                continue
PY|            for outside in outside_graphs:
PY|                if inside & outside:
PY|                    continue
PY|                whole = inside | outside
PY|                if any(x < 3 and y < 3 and
PY|                       ((x == y == l - 1) or
PY|                        (x != y and edge(j, k) not in g))
PY|                       for x, y in whole):
PY|                    continue
PY|                if j in centers:
PY|                    if {y for x, y in whole if x == 3} != \
PY|                       {y for x, y in whole if x == 4}:
PY|                        continue
PY|                if k in centers:
PY|                    if {x for x, y in whole if y == 3} != \
PY|                       {x for x, y in whole if y == 4}:
PY|                        continue
PY|                count += 1
PY|                shapes.add((hu, hv))
PY|    return count, shapes
PY|
PY|def cube_table(t):
PY|    return {p: len({(w[p[0]], w[p[1]]) for w in t}) for p in CUBE_PAIRS}
PY|
PY|def check_cube_coverage(table):
PY|    need(set(table) == set(CUBE_PAIRS), "ALL_THREE_PAIR_PROJECTIONS")
PY|
PY|def make_f(i, hj, hk, ownj, ownk):
PY|    j, k = tuple(x for x in I if x != i)
PY|    low = i - 1
PY|    assignments = (
PY|        {i: low, j: low, k: hk},
PY|        {i: low, j: hj, k: low},
PY|        {i: ownj, j: low, k: 7 - hk},
PY|        {i: ownk, j: 7 - hj, k: low})
PY|    return tuple(tuple(a[x] for x in I) for a in assignments)
PY|
PY|def assemble(fs):
PY|    return tuple((a,) + t for i, f in enumerate(fs)
PY|                 for a in range(3) if a != i for t in f)
PY|
PY|def fixture_from_targets(p):
PY|    need(len(p) == 3 and all(p[i] in range(3) and p[i] != i
PY|                            for i in range(3)), "TARGET_MAP_DOMAIN")
PY|    fs = []
PY|    for i in I:
PY|        j, k = tuple(x for x in I if x != i)
PY|        ownj = 4 if p[i - 1] == j - 1 else 3
PY|        ownk = 4 if p[i - 1] == k - 1 else 3
PY|        fs.append(make_f(i, 3, 3, ownj, ownk))
PY|    return assemble(tuple(fs))
PY|
PY|def check_zero_case():
PY|    allowed = tuple((j, k, s) for j, k in GEDGES
PY|                    for s in range(3) if s != 5 - j - k)
PY|    need(len(allowed) == 6, "SIX_ALLOWED_LL_PAIRS")
PY|    for s in range(3):
PY|        star = {(j, k) for j, k, t in allowed if t == s}
PY|        expected = {edge(s + 1, x) for x in I if x != s + 1}
PY|        need(star == expected, "PHYSICAL_LL_STAR")
PY|    shadows = []
PY|    for n0, n1, n2 in compositions(24, 3):
PY|        for m in range(7):
PY|            if n1 + 2 * n2 == 36 and n2 == 2 * m:
PY|                shadows.append((n0, n1, n2, m))
PY|    need(shadows == [(0, 12, 12, 6)], "ZERO_CASE_COUNT_SHADOW")
PY|    subset_survivors = []
PY|    for mask in range(64):
PY|        chosen = {allowed[t] for t in range(6) if mask & (1 << t)}
PY|        if len(chosen) == shadows[0][3]:
PY|            subset_survivors.append(chosen)
PY|    need(subset_survivors == [set(allowed)], "FULL_LL_STAR_UNIVERSE")
PY|    f_solutions = tuple(f for f in product(range(5), repeat=3)
PY|                        if all(sum(f[i] for i in range(3) if i != s) == 2
PY|                               for s in range(3)))
PY|    need(f_solutions == ((1, 1, 1),), "HIGH_F_COUNTS")
PY|    choices = tuple(tuple(make_f(i, *z) for z in product(H, repeat=4))
PY|                    for i in I)
PY|    weak = 0
PY|    overlap_rejections = 0
PY|    for fs in product(*choices):
PY|        tick()
PY|        words = assemble(fs)
PY|        if not accepted(lambda: check_pair_interface(words, 12)):
PY|            continue
PY|        weak += 1
PY|        for j in I:
PY|            for h in H:
PY|                f = tuple(sum(t[j - 1] == h for t in family) for family in fs)
PY|                need(f == (1, 1, 1), "DERIVED_HIGH_F_COUNTS")
PY|        expect_bad("ONE_COLUMN_OVERLAP", lambda: block_counts(words))
PY|        overlap_rejections += 1
PY|    need(weak > 0 and overlap_rejections == weak, "ZERO_WEAK_INTERFACE_AUDIT")
PY|    return weak
PY|
PY|def main():
PY|    global GRAPHS, BY_GRAPH
PY|    print("START: exact finite checker; cooperative limit 55 seconds")
PY|    m48 = moment_profiles(48)
PY|    m49 = moment_profiles(49)
PY|    need(m48 == ((0, 0, 12, 12, 0),), "MOMENT_48_EXHAUSTION")
PY|    need(set(m49) == {(0, 1, 10, 13, 0), (0, 0, 13, 10, 1)},
PY|         "MOMENT_49_CONTROL_EXHAUSTION")
PY|    profiles = tuple(degree_profiles(i) for i in range(4))
PY|    need(profiles[0] == ((4, 4, 4),), "PARTY_ZERO_DEGREES")
PY|    need(all(len(profiles[i]) == 10 and
PY|             all(tuple(sorted(r)) == (2, 2, 2, 3, 3) for r in profiles[i])
PY|             for i in I), "FIVE_SYMBOL_DEGREES")
PY|    doubles = {}
PY|    for p in PAIRS:
PY|        k, l = tuple(i for i in range(4) if i not in p)
PY|        doubles[p] = B[k] * B[l]
PY|    triples = tuple(6 * B[i] - B[i] * sum(B[j] for j in range(4) if j != i)
PY|                    for i in range(4))
PY|    need(tuple(doubles[p] for p in PAIRS) == (1, 1, 1, 3, 3, 3),
PY|         "MAXIMAL_DOUBLE_COUNTS")
PY|    need(triples == (9, 1, 1, 1), "MAXIMAL_TRIPLE_COUNTS")
PY|    oo = {p: B[p[0]] * B[p[1]] for p in PAIRS}
PY|    io = {(i, j): Q[i] * B[j] for i in range(4)
PY|          for j in range(4) if i != j}
PY|    print("moments", m48, "degree_vector_counts", tuple(map(len, profiles)))
PY|    print("double_counts", doubles, "triple_counts", triples)
PY|    print("outside_outside", oo, "internal_outside", io)
PY|    stars = make_stars()
PY|    need(len(set(stars)) == 6 and
PY|         all(len({(w[i], w[j]) for w in stars}) == 6 for i, j in PAIRS),
PY|         "STAR_POSITIVE_PAIR_INJECTIVITY")
PY|    perms = tuple(permutations(range(3)))
PY|    literal = 0
PY|    covariant = 0
PY|    for maps in product(perms, repeat=3):
PY|        literal += accepted(lambda: check_gauge(stars, maps))
PY|        check_gauge(transform_stars(stars, maps), maps)
PY|        covariant += 1
PY|    need(literal == 1 and covariant == 216, "GAUGE_CONTROL_COUNTS")
PY|    GRAPHS, BY_GRAPH = enumerate_prisms()
PY|    prism_count = sum(len(BY_GRAPH[g]) for g in GRAPHS)
PY|    need(prism_count == 144, "TOTAL_COLORED_PRISMS")
PY|    cube = tuple(product(range(2), repeat=3))
PY|    hist = Counter()
PY|    for t in combinations(cube, 6):
PY|        tick()
PY|        table = cube_table(t)
PY|        check_cube_coverage(table)
PY|        hist[tuple(table[p] for p in CUBE_PAIRS)] += 1
PY|    need(hist == Counter({(3, 4, 4): 4, (4, 3, 4): 4,
PY|                          (4, 4, 3): 4, (4, 4, 4): 16}),
PY|         "BINARY_SIX_SUBSET_HISTOGRAM")
PY|    need(hist[(3, 3, 3)] == 0, "BINARY_HIGH_TRIPLE_IMPOSSIBILITY")
PY|    print("abstract_prisms", prism_count, "binary_histogram", dict(hist))
PY|    for mask in range(8):
PY|        tick()
PY|        g = {GEDGES[t] for t in range(3) if mask & (1 << t)}
PY|        summary = {l: local_interfaces(g, l) for l in sorted(active_centers(g))}
PY|        if 0 < mask < 7:
PY|            need(all(n == 0 for n, shapes in summary.values()),
PY|                 "UNEXPECTED_ONE_OR_TWO_EDGE_INTERFACE")
PY|        if mask == 7:
PY|            need(all(shapes <= {(2, 2)} for n, shapes in summary.values()),
PY|                 "NONFULL_HIGH_BLOCK_SURVIVED")
PY|        print("G_mask", mask, "local_necessary_interfaces", summary)
PY|    weak_zero = check_zero_case()
PY|    print("zero_case_pair_interface_fixtures", weak_zero,
PY|          "all rejected for one-column overlap")
PY|    base = ((0, 0, 0), (1, 1, 1), (2, 2, 2),
PY|            (2, 0, 1), (0, 1, 2), (1, 2, 0))
PY|    check_w(base)
PY|    positive_weak = fixture_from_targets((1, 2, 0))
PY|    check_pair_interface(positive_weak, 12)
PY|    controls = []
PY|    controls.append(expect_bad("SECOND_MOMENT",
PY|                    lambda: check_moment_profile((0, 1, 10, 13, 0))))
PY|    bad_maps = ((1, 0, 2), (0, 1, 2), (0, 1, 2))
PY|    controls.append(expect_bad("COMMON_PHYSICAL_LOW_GAUGE",
PY|                    lambda: check_gauge(stars, bad_maps)))
PY|    repeated_edge = base[:-1] + ((1, 0, 0),)
PY|    controls.append(expect_bad("REPEATED_JK_EDGE",
PY|                    lambda: check_w(repeated_edge)))
PY|    wrong_cycle = fixture_from_targets((1, 0, 0))
PY|    controls.append(expect_bad("PAIR_EXTENSION_TWO",
PY|                    lambda: check_pair_interface(wrong_cycle, 12)))
PY|    partial_table = cube_table(cube[:6])
PY|    del partial_table[(1, 2)]
PY|    controls.append(expect_bad("ALL_THREE_PAIR_PROJECTIONS",
PY|                    lambda: check_cube_coverage(partial_table)))
PY|    rows = {r: {c for c in range(3) if c != r} for r in range(3)}
PY|    need(all(len(rows[r] & rows[s]) == 1 for r, s in combinations(rows, 2)),
PY|         "ONE_OVERLAP_CONTROL_SHAPE")
PY|    controls.append(expect_bad("ONE_COLUMN_OVERLAP",
PY|                    lambda: check_rows(rows)))
PY|    fake_six = ((0, 0, 0), (1, 1, 1), (2, 2, 2)) * 2
PY|    controls.append(expect_bad("SIX_DISTINCT_COLORED_TRIPLES",
PY|                    lambda: check_w(fake_six)))
PY|    bad_0j = ((2, 0, 0), (1, 1, 1), (0, 2, 2),
PY|              (2, 0, 1), (0, 1, 2), (1, 2, 0))
PY|    controls.append(expect_bad("REPEATED_0J_PAIR",
PY|                    lambda: check_w(bad_0j)))
PY|    need(len(controls) == 8 and len(set(controls)) == 8,
PY|         "REASON_SPECIFIC_CONTROL_COUNT")
PY|    tick()
PY|    print("negative_control_reasons", tuple(controls))
PY|    print("COMPLETE: all declared finite checks and eight controls completed")
PY|    print("LIMIT: weak interfaces only; no physical AME or complex-phase witness")
PY|
PY|if __name__ == "__main__":
PY|    main()

## 8. Control interpretation

All outcomes in this table are **specified expectations, not observed execution results**.

| Control | Targeted failure | Expected reason |
|---|---|---|
| Second moment 49 | Admits a maximal-word profile forbidden by the actual \(3555\) moments | `SECOND_MOMENT` |
| Independent low-label gauge | Changes a missing-pair map without transforming the fixed physical maximal words | `COMMON_PHYSICAL_LOW_GAUGE` |
| Repeated colored physical edge | Two distinct colored triples reuse one \(j,k\) pair | `REPEATED_JK_EDGE` |
| Wrong three-cycle | Replaces the directed three-cycle fixture by a two-cycle with an incoming tail, producing a repeated high–high physical pair | `PAIR_EXTENSION_TWO` |
| Missing third pair projection | Omits one physical pair system from the projection audit | `ALL_THREE_PAIR_PROJECTIONS` |
| Permit one-column overlap | Accepts a complement-diagonal three-row support despite its nonzero single-product inner products | `ONE_COLUMN_OVERLAP` |
| Fake six words from three repeated words | Satisfies superficial multiplicity totals while having only three distinct triples | `SIX_DISTINCT_COLORED_TRIPLES` |
| Repeated physical \(0j\) pair | Preserves bare edges and balanced color counts but violates physical color-pair injectivity | `REPEATED_0J_PAIR` |

The missing-third-projection control is intentionally identified as a coverage control. The third size-three condition is mathematically redundant for a six-subset once two such conditions are enforced; claiming otherwise would invent a counterexample.

## 9. Disposition and remaining acceptance boundary

The written reconstruction supports the stated moment, profile, prism-incidence, interaction-graph, zero-star, and one-overlap lemmas. It exposes no evidence-backed mathematical defect in the supplied \(3555\) argument.

Nevertheless:

- The finite checker is **NOT_RUN**, and its source has not received interpreter verification.
- No executed enumeration counts, runtime, checker hash, or control PASS receipt are claimed.
- The synthetic pair-interface fixtures do not establish a common maximal support \(P\), an admissible tensor, or simultaneous unitary amplitudes.
- This return does not itself adopt the whole \(3555\) exclusion. Disjoint written checking and parent disposition remain separate gates.
- No other residual-alphabet branch, exact-\(t=28\) branch, full support-48 no-go, lower bound 49, AME support minimum, or novelty claim is settled.

**Findings:** No evidence-backed mathematical defect identified in the assigned source.

**Overall correctness:** correct.

**Explanation:** The supplied \(3555\) argument’s necessary common-support interfaces and final complex one-overlap obstruction reconstruct consistently. This verdict does not convert the unexecuted finite checker into run evidence or grant whole-branch adoption.

**Confidence:** 0.89.