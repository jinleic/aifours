# author-candidate-v1.md

**Wave:** f381-ame48-t24-simultaneous-residual-support-frontier  
**Status:** **AUTHOR CANDIDATE — UNREVIEWED; NOT ADOPTED.**  
**Result:** A complete written exclusion of the **entire residual alphabet profile \(4444\)** for the actual same complex tensor at support \(48\), \(t=24\).  
**Execution:** No scientific program was run. A complete finite checker is supplied below as **NOTRUN**.

## 1. Exact theorem and target relation

**Theorem — whole-profile \(4444\) exclusion.**  
Let \(\psi\in(\mathbb C^6)^{\otimes4}\) be normalized, and suppose all three balanced flattenings of \(U=6\psi\) are unitary. Suppose \(U\) has exactly \(48\) nonzero entries, exactly \(24\) of which have modulus one. Define the **same** sets
\[
P=\{w:|U_w|=1\},\qquad E=\{w:0<|U_w|<1\}.
\]
If the residual alphabet of \(E\) has size four at **each** party, these hypotheses are contradictory.

The proof handles every support and every nonzero complex amplitude satisfying these hypotheses. It does not restrict phases to real signs or residual moduli to a common value.

The new load-bearing step is a **simultaneous normal form forced by the common \(24\)-word set \(P\)**. It is not a collection of independently selected pair matchings. In that normal form, required residual pair fibers force three corners of a rectangle, while another pair system forbids the fourth corner. Actual complex unitarity is then impossible.

**Dependency boundary.** This proof does **not** use the inherited no-distance-one theorem, the inherited alphabet restriction \(q_i\in\{3,4,5\}\), or no-OLS(6). Thus this particular \(4444\) exclusion has a complete original argument independent of that imported interface. The no-OLS dependency of other inherited conclusions is **not** removed.

This is not a universal \(t=24\) exclusion, a support-\(48\) exclusion, an \(N\ge49\) result, a witness, a novelty claim, or an adoption.

## 2. Access, chronology, and execution disclosure

I read the complete manifest, freeze receipt, parent metadata supply, and all eight named status/permission controls before reading the complete ordered literal source packet:

- S1, logical lines 1–28;
- S2, logical lines 1–374;
- S3, logical lines 1–437.

The packet was read through its ending. The separate dispatch receipt was read **after** the initial mathematical derivation and substantive checkpoint, not before packet reading.

Assigned bindings:

- Manifest: `48dbd61ea396e1689b5729b21c28a6889f1c7c60c6bbe525aa8493b91fd8ee0c`
- Freeze receipt: `364ae02f211d6d9601b6813c535fc6070db81f1b9ddb06fcd358884e9407398a`
- Literal packet: `2a78d178c3405be06ad59213022414ce735fc4eef9fdcfb70ef84149563a38d0`

Matching hashes, byte counts and LF counts are **parent-supplied observations**, not child-executed hash checks.

The observations **2026-10-30T10:13:02-0700 PDT** and **2026-10-30T10:19:37-0700 PDT** were supplied by the parent. Neither is represented as my native start, private derivation time or completion time. I sent a substantive checkpoint describing the whole-class obstruction, followed by the load-bearing normal-form derivation.

The quarantine documents were used for status and boundaries only. No held scientific payload, held \(t=28\) route, compression consumer, PH report consumer, v8 or cp116 was followed or used. No public webpage or paper was opened during this assignment. Public-source statements mentioned inside the supplied packet remain attributed packet content; they are not claimed as newly inspected sources.

All mathematics below is a written author derivation. No interpreter, solver, numerical optimization, enumeration or scientific executable was run. No working-tree file was written. This is the complete body for parent materialization, including the full NOTRUN checker.

## 3. Actual same-tensor consequences

Write the parties as \(1,2,3,4\). For each party \(i\), let \(A_i\) be its four residual symbols and \(B_i\) its other two symbols.

In any balanced flattening, a unit-modulus entry exhausts its row and column. Hence the \(24\) entries of \(P\) occupy distinct rows and distinct columns, and no residual entry can use those rows or columns.

Removing them leaves a \(12\times12\) unitary matrix containing exactly \(24\) nonzero entries. Every remaining row and column has at least two nonzeros: a singleton would have modulus one and belong to \(P\). Consequently every residual row and column has exactly two nonzeros.

Two residual rows cannot intersect in exactly one column, because their inner product would be one nonzero product. Thus intersecting residual rows have the same two columns, giving full \(2\times2\) residual blocks.

For every coordinate pair \(ij\), define
\[
R_{ij}=\pi_{ij}(E).
\]
Then:

1. \(|R_{ij}|=12\);
2. each value in \(R_{ij}\) has exactly two extensions in \(E\);
3. \(P\) projects injectively onto that pair;
4. for the **same \(P\)** in all six pair systems,
   \[
   \pi_{ij}(P)=[6]^2\setminus R_{ij}. \tag{1}
   \]

For \(a\in A_i\), let \(p_i(a)\) be its multiplicity in \(P\), and let \(r_i(a)\) be its degree in \(R_{ij}\). Equation (1) gives
\[
r_i(a)=6-p_i(a),\qquad
\sum_{a\in A_i}r_i(a)=12. \tag{2}
\]
In particular, the degree is independent of the partner party.

None of this uses a no-distance-one assumption.

## 4. Every maximal word has exactly two residual-alphabet coordinates

For \(w\in P\), let
\[
k(w)=|\{i:w_i\in A_i\}|.
\]
At each party,
\[
\sum_{a\in A_i}p_i(a)=4\cdot6-12=12.
\]
Therefore
\[
\sum_{w\in P}k(w)=48. \tag{3}
\]

For every pair \(ij\), exactly \(4\cdot4-12=4\) internal pair values belong to \(P\). Hence
\[
\sum_{w\in P}\binom{k(w)}2=6\cdot4=24. \tag{4}
\]
It follows that
\[
\sum_{w\in P}(k(w)-2)^2
=2\cdot24-3\cdot48+4\cdot24=0.
\]
Thus
\[
\boxed{k(w)=2\quad\text{for every }w\in P.} \tag{5}
\]

Fix \(i\) and \(a\in A_i\). Each maximal word containing \(a\) has exactly one other internal coordinate. Counting that coordinate using the other three pair systems gives
\[
p_i(a)=\sum_{j\ne i}(4-r_i(a))=12-3r_i(a).
\]
Together with (2),
\[
6-r_i(a)=12-3r_i(a),
\]
so
\[
\boxed{r_i(a)=3,\qquad p_i(a)=3.} \tag{6}
\]

Consequently
\[
M_{ij}:=(A_i\times A_j)\setminus R_{ij}
\]
is a perfect matching for every pair \(ij\).

For each unordered pair \(ij\), exactly four words of \(P\) have internal coordinates \(i,j\). Denote this set by \(P_{ij}\). Its projection onto \(A_i\times A_j\) is \(M_{ij}\), and its projection onto the complementary outside alphabets \(B_k\times B_l\) is bijective.

The task is now to determine the six matchings **simultaneously**, using the common \(P\).

## 5. Simultaneous normal-form lemma

### 5.1 Binary functions obtained from the actual common \(P\)

Label each outside alphabet \(B_i\) by bits \(0,1\).

For four distinct indices \(i,j,k,l\), let
\[
\varepsilon(i,j,k,l)\in\mathbb F_2
\]
be the parity of the permutation \((i,j,k,l)\) of \((1,2,3,4)\).

Fix \(i\), \(a\in A_i\), and \(k\ne i\). Choose either of the other two parties as \(j\), with the remaining party called \(l\). There is exactly one word of \(P_{ij}\) with symbol \(a\) at \(i\). Let its outside bit at \(k\) be \(b_k\), and define
\[
t_{ik}(a)=b_k+\varepsilon(i,j,k,l)\quad\text{in }\mathbb F_2. \tag{7}
\]

This definition is independent of choosing \(j\) or \(l\):

- the two relevant maximal words must have different bits at \(k\), or they repeat the pair value \((a,b_k)\);
- swapping \(j,l\) also changes permutation parity.

Both terms therefore flip.

For fixed \(i\), the map
\[
a\longmapsto (t_{ik}(a),t_{il}(a))
\]
is bijective for every two distinct \(k,l\ne i\). Indeed, it is the outside-pair projection of \(P_{ij}\), up to fixed bit complements.

Thus the four triples
\[
(t_{ik}(a))_{k\ne i},\qquad a\in A_i,
\]
have every two-coordinate projection bijective.

### 5.2 The four triples have one parity

Four binary triples with all two-coordinate projections bijective are exactly one of the two parity classes:
\[
\sum_{k\ne i}t_{ik}(a)=c_i,\qquad c_i\in\mathbb F_2. \tag{8}
\]

For completeness, use any two coordinates as the labels \((x,y)\in\mathbb F_2^2\). The third coordinate \(z(x,y)\) must take both values in every row and every column of its \(2\times2\) table. Hence
\[
z(x,y)=x+y+c_i.
\]
This proves (8), without an external classification result.

### 5.3 The missing matchings are linked across parties

Suppose \((a,b)\in M_{ij}\), and let \(k,l\) be complementary to \(i,j\). The corresponding word of \(P_{ij}\) has the same outside bit when viewed from \(i\) or \(j\). Because swapping \(i,j\) changes permutation parity, equation (7) gives
\[
t_{ik}(a)+t_{jk}(b)=1,\qquad
t_{il}(a)+t_{jl}(b)=1. \tag{9}
\]

Conversely, these equations identify exactly one \(b\), since the two-coordinate map at party \(j\) is bijective. Therefore (9) characterizes the entire matching \(M_{ij}\).

This is where the common \(P\), rather than independent pairwise choices, enters decisively.

### 5.4 Simultaneous normalization of all four parity constants

Put
\[
C=c_1+c_2+c_3+c_4,\qquad v_k=c_k+C.
\]
Complement the outside bit at party \(k\) by \(v_k\). This replaces every \(t_{ik}\), \(i\ne k\), by \(t_{ik}+v_k\).

Since
\[
\sum_kv_k=C,
\]
the new parity at party \(i\) is
\[
c_i+\sum_{k\ne i}v_k=c_i+C+v_i=0. \tag{10}
\]
The matching equations (9) are unchanged because the same \(v_k\) is added on both sides.

Thus all four triple systems can be normalized simultaneously to even parity.

### 5.5 Canonical labels and all six matchings

At party \(i\), relabel its four internal symbols by \(a\in\{1,2,3,4\}\) so that
\[
t_{ik}(a)=
\begin{cases}
0,&a\in\{i,k\},\\
1,&a\notin\{i,k\}.
\end{cases} \tag{11}
\]
These are precisely the four even-parity triples: label \(a=i\) gives \(000\), while label \(a\ne i\) has its unique zero at coordinate \(a\).

Let \(k,l\) be complementary to \(i,j\). Substitution in (9) shows that the missing matching is
\[
M_{ij}=\{(a,f_{ij}(a)):a\in\{1,2,3,4\}\},
\]
where
\[
\boxed{f_{ij}=(k\ l),\quad\text{fixing }i,j.} \tag{12}
\]

Explicitly:

| Pair | Missing matching permutation |
|---|---|
| \(12\) | \((3\ 4)\) |
| \(13\) | \((2\ 4)\) |
| \(14\) | \((2\ 3)\) |
| \(23\) | \((1\ 4)\) |
| \(24\) | \((1\ 3)\) |
| \(34\) | \((1\ 2)\) |

These are **not** six independently selected permutations and are not assumed to be one common equality matching. They are forced simultaneously by the actual common \(P\).

## 6. Explicit common \(24\)-word packing

To make the simultaneous realization explicit, write the two outside symbols at each party as \(o_0,o_1\), distinct from the four internal labels.

The normal form above forces the following common \(P\):

| Internal positions | Four maximal words |
|---|---|
| \(12\) | \((1,1,o_0,o_1)\), \((2,2,o_1,o_0)\), \((3,4,o_0,o_0)\), \((4,3,o_1,o_1)\) |
| \(13\) | \((1,o_1,1,o_0)\), \((3,o_0,3,o_1)\), \((2,o_1,4,o_1)\), \((4,o_0,2,o_0)\) |
| \(14\) | \((1,o_0,o_1,1)\), \((4,o_1,o_0,4)\), \((2,o_0,o_0,3)\), \((3,o_1,o_1,2)\) |
| \(23\) | \((o_0,2,2,o_1)\), \((o_1,3,3,o_0)\), \((o_0,1,4,o_0)\), \((o_1,4,1,o_1)\) |
| \(24\) | \((o_1,2,o_0,2)\), \((o_0,4,o_1,4)\), \((o_1,1,o_1,3)\), \((o_0,3,o_0,1)\) |
| \(34\) | \((o_0,o_1,3,3)\), \((o_1,o_0,4,4)\), \((o_0,o_0,1,2)\), \((o_1,o_1,2,1)\) |

This is a valid common **partial packing**, not an AME witness.

Its pair projections can be checked directly:

- internal–internal pairs give exactly the four matching values in (12);
- outside–outside pairs give all four outside pairs exactly once;
- for any fixed internal symbol and any other outside party, the two applicable words have opposite outside bits.

Thus every pair projection is injective and its complement is precisely
\[
R_{ij}=\{1,2,3,4\}^2\setminus M_{ij}.
\]
All six residual pair graphs are therefore linked to one explicit \(P\). What fails next is their simultaneous completion by an actual residual tensor.

## 7. Required residual fibers force an impossible rectangle

Let
\[
I=(1,2,3,4),
\]
and let \(T_{kl}\) be obtained from \(I\) by exchanging its coordinates \(k,l\).

### Forced-fiber claim

For distinct \(i,j\), with complementary indices \(k,l\), the **only** words compatible with all six residual pair graphs and satisfying
\[
w_i=i,\qquad w_j=j
\]
are
\[
I,\qquad T_{kl}. \tag{13}
\]

To prove this, first note that \((i,j)\in R_{ij}\), since \(f_{ij}\) fixes \(i\), not \(j\).

For a compatible word with these two coordinates fixed, the pair involving party \(i\) forbids either remaining coordinate from taking label \(i\). The pair involving party \(j\) similarly forbids label \(j\). Therefore
\[
w_k,w_l\in\{k,l\}.
\]
The permutation \(f_{kl}\) fixes \(k,l\), so residual compatibility requires \(w_k\ne w_l\). This leaves exactly the two words in (13), both of which satisfy the other pair constraints.

Every residual pair value has **two** extensions in the actual \(E\). Consequently both words in (13) must belong to \(E\).

In particular,
\[
I=(1,2,3,4),\quad
T_{12}=(2,1,3,4),\quad
T_{34}=(1,2,4,3)
\]
are all forced into \(E\).

Now use the actual flattening \(12\mid34\).

- Row \((1,2)\) has its two nonzero entries at columns \((3,4)\) and \((4,3)\), supplied by \(I,T_{34}\).
- Row \((2,1)\) has a nonzero entry at column \((3,4)\), supplied by \(T_{12}\).

Their orthogonality forces a nonzero entry at the fourth rectangle corner
\[
D=(2,1,4,3). \tag{14}
\]
Otherwise their inner product is exactly the single nonzero product
\[
U_I\,\overline{U_{T_{12}}},
\]
which cannot vanish.

But \(D\) has coordinate-pair value
\[
(D_1,D_3)=(2,4).
\]
Since \(f_{13}=(2\ 4)\),
\[
(2,4)\in M_{13},
\]
so \(D\) is forbidden in \(E\).

It cannot belong to \(P\) either: it has four internal coordinates, whereas every word of \(P\) has exactly two. Equivalently, its pair value is already occupied by \(P\), so no further tensor entry can use it.

Thus the fourth corner is simultaneously required and forbidden. This contradiction proves the theorem. \(\square\)

**Complex-amplitude boundary:** The contradiction uses only nonvanishing and actual row orthogonality. No real-phase restriction, phase ansatz, equal-modulus assumption or relaxed degree model is involved.

## 8. Complete finite checker — NOTRUN

**Purpose and coverage.** The checker below:

1. checks all \(70\) four-element subsets of the eight binary triples for the local parity lemma;
2. checks the parity normalization for all \(16\) parity vectors;
3. checks all six canonical missing matchings;
4. constructs the explicit common \(24\)-word \(P\) and verifies every pair complement;
5. examines all \(4^4=256\) canonical residual words and checks every forced fiber (13);
6. checks the forbidden fourth corner and the rectangle obstruction;
7. includes six intended-reason negative controls and positive controls.

It does **not** enumerate all raw supports or all raw \(P\)'s. The universal reduction from an arbitrary actual tensor to the canonical system is the written proof in §§3–5, not a claimed exhaustive computation.

Positive controls include the common \(P\), a complete single-cut rectangle, and the exact integer Gram identity for the unnormalized \(2\times2\) Hadamard matrix. The latter two are local controls, **not** four-party witnesses.

Negative controls reject:

- a duplicated maximal word;
- an incorrect missing matching;
- removal of a forced residual extension;
- the globally forbidden fourth corner;
- the three-corner nonrectangle;
- a non-Latin local binary triple set.

**Execution status:** **NOTRUN.** No output, elapsed time or PASS is claimed. The loops are finite and small; a cooperative 55-second guard is included. There are no packages, file reads, file writes, network calls, solver calls or background jobs.

**Materialization:** Save the following complete single source line as `simultaneous-4444-checker-v1.py`. The escaped newlines are intentional; Python’s `exec` expands them.

`exec("from itertools import combinations, product\nfrom time import monotonic\nstart = monotonic()\ndef require(ok, msg):\n  if not ok:\n    raise RuntimeError(msg)\ndef guard():\n  require(monotonic() - start < 55, 'cooperative deadline exceeded')\nV = tuple(range(1, 5))\npairs = list(combinations(V, 2))\nB = (0, 5)\ndef independent(S):\n  return len(S) == 4 and all(len({(w[a], w[b]) for w in S}) == 4 for a, b in combinations(range(3), 2))\ntriples = list(product(range(2), repeat=3))\ngood = set()\nfor S in combinations(triples, 4):\n  guard()\n  if independent(S):\n    good.add(frozenset(S))\nexpected = {frozenset(w for w in triples if sum(w) % 2 == c) for c in range(2)}\nrequire(good == expected, 'local parity classification')\nfor c in product(range(2), repeat=4):\n  guard()\n  C = sum(c) % 2\n  v = tuple(x ^ C for x in c)\n  require(all((c[i] ^ (sum(v[k] for k in range(4) if k != i) % 2)) == 0 for i in range(4)), 'simultaneous parity normalization')\ndef eps(p):\n  return sum(p[a] > p[b] for a in range(4) for b in range(a + 1, 4)) % 2\ndef f(i, j, a):\n  k, l = [x for x in V if x not in (i, j)]\n  return l if a == k else k if a == l else a\ndef t(i, a, k):\n  return int(a not in (i, k))\ndef proj(w, p):\n  return tuple(w[x - 1] for x in p)\nM = {(i, j): {(a, f(i, j, a)) for a in V} for i, j in pairs}\nR = {p: set(product(V, repeat=2)) - M[p] for p in pairs}\nfor i, j in pairs:\n  k, l = [x for x in V if x not in (i, j)]\n  actual = {(a, b) for a, b in product(V, repeat=2) if (t(i, a, k) ^ t(j, b, k)) == 1 and (t(i, a, l) ^ t(j, b, l)) == 1}\n  require(actual == M[(i, j)], 'canonical matching characterization')\nP = []\nfor i, j in pairs:\n  guard()\n  k, l = [x for x in V if x not in (i, j)]\n  e = eps((i, j, k, l))\n  for a in V:\n    w = [None] * 4\n    w[i - 1] = a\n    w[j - 1] = f(i, j, a)\n    w[k - 1] = B[t(i, a, k) ^ e]\n    w[l - 1] = B[t(i, a, l) ^ e ^ 1]\n    P.append(tuple(w))\ndef valid_p(Q, rs):\n  universe = set(product(range(6), repeat=2))\n  return len(Q) == 24 and len(set(Q)) == 24 and all(len({proj(w, p) for w in Q}) == 24 and {proj(w, p) for w in Q} == universe - rs[p] for p in pairs)\nrequire(valid_p(P, R), 'common P and all six complements')\nrequire(all(sum(x in V for x in w) == 2 for w in P), 'P has exactly two internal coordinates')\ndef compatible(w, rs):\n  return all(proj(w, p) in rs[p] for p in pairs)\nCands = set()\nfor w in product(V, repeat=4):\n  guard()\n  if compatible(w, R):\n    Cands.add(w)\nI = V\ndef swap(i, j):\n  w = list(V)\n  w[i - 1], w[j - 1] = w[j - 1], w[i - 1]\n  return tuple(w)\nfor i, j in pairs:\n  k, l = [x for x in V if x not in (i, j)]\n  require({w for w in Cands if proj(w, (i, j)) == (i, j)} == {I, swap(k, l)}, 'forced residual fiber')\nT12, T34 = swap(1, 2), swap(3, 4)\nF = {I, T12, T34}\nD = (2, 1, 4, 3)\nrequire(F <= Cands, 'forced three corners are compatible')\nrequire(proj(D, (1, 3)) in M[(1, 3)], 'fourth corner forbidden in pair13')\ndef cut_closed(S, p):\n  q = tuple(x for x in V if x not in p)\n  rows, cols = {}, {}\n  for w in S:\n    r, c = proj(w, p), proj(w, q)\n    rows.setdefault(r, set()).add(c)\n    cols.setdefault(c, set()).add(r)\n  return bool(S) and all(len(cs) == 2 for cs in rows.values()) and all(len(rs) == 2 for rs in cols.values()) and all(rows[r2] == cs for cs in rows.values() for c in cs for r2 in cols[c])\nrequire(cut_closed(F | {D}, (1, 2)), 'positive complete rectangle control')\nH = ((1, 1), (1, -1))\nrequire(all(sum(H[r][c] * H[s][c] for c in range(2)) == (2 if r == s else 0) for r, s in product(range(2), repeat=2)), 'positive exact Hadamard Gram control')\nneg = []\ndef reject(ok, label):\n  require(not ok, 'negative control unexpectedly accepted: ' + label)\n  neg.append(label)\nreject(valid_p(P[:-1] + [P[0]], R), 'duplicate maximal word')\nbadR = dict(R)\nbadR[(1, 3)] = set(product(V, repeat=2)) - {(a, a) for a in V}\nreject(valid_p(P, badR), 'incorrect missing matching')\nbadC = Cands - {T34}\nreject({w for w in badC if proj(w, (1, 2)) == (1, 2)} == {I, T34}, 'missing forced extension')\nreject(compatible(D, R), 'forbidden fourth corner')\nreject(cut_closed(F, (1, 2)), 'three-corner nonrectangle')\nreject(independent(((0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1))), 'non-Latin local triples')\nrequire(len(neg) == 6, 'negative control count')\nguard()\nprint('PASS: canonical common P/all six complements; local normal form; forced fibers; forbidden rectangle; P words=', len(P), '; compatible residual words=', len(Cands), '; intended negative controls=', len(neg))\n")`

**Runnable argv, NOTRUN:** `python3 simultaneous-4444-checker-v1.py`

Any future successful output would be a finite check of the specified canonical objects and controls, not an independent formal verification of the entire written reduction.

## 9. Findings and verification boundaries

| Item | Status |
|---|---|
| Same-tensor pair complements and \(2\times2\) block closure | Reconstructed directly from actual unitarity |
| \(4444\) forces every maximal word to have exactly two internal coordinates | Written proof, §4 |
| All six missing matchings have one simultaneous normal form | Written author proof, §5 |
| One explicit common \(24\)-word \(P\) realizes those six complements | Explicit construction, §6 |
| Every compatible residual completion contains \(I,T_{12},T_{34}\) | Written proof using exact two-extension fibers, §7 |
| Complex unitarity requires a forbidden fourth corner | Written whole-class contradiction, §7 |
| Complete \(4444\) class exclusion | **PROVED IN THIS AUTHOR DERIVATION; UNREVIEWED** |
| No-OLS(6) needed for this class exclusion | **No; the complete argument above avoids that import** |
| Finite checker | Complete source supplied; **NOTRUN** |
| Prior public material | Elementary block-orthogonality and binary Latin facts are re-derived, not advertised as new science |
| Independent check, adoption, novelty | **Not performed / not granted** |

The negative result is not merely that one selected support fails: **every actual \(4444\) tensor is reduced to the same simultaneous pair system, and every residual completion of that system encounters the forbidden rectangle.**

## 10. Exact unpaid work

The following remain unpaid:

1. A disjoint reconstruction of the full normal-form lemma and rectangle contradiction.
2. Parent materialization and, if desired, one bounded execution of the supplied checker with actual results recorded separately.
3. Parent disposition of this author candidate.
4. Research on the other surviving profiles \(3555,4445,4455,4555,5555\), at their existing dependency boundaries.
5. Public-source priority/novelty screening.

There is **no missing support case, phase case or modulus case within the stated \(4444\) theorem**. The missing work is independent verification and the other profiles—not completion of a narrowed \(4444\) argument.