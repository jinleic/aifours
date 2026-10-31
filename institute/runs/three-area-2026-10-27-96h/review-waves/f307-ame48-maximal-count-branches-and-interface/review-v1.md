# f307 review-v1 — full text for parent materialization

**Overall correctness:** correct for the stated branch/interface theorems, with the non-blocking proof-text corrections below.  
**Findings:** **0 FATAL / 0 MAJOR / 2 MINOR.**  
**Confidence:** 0.97.

The branch restriction \(t\in\{24,27,28\}\) and the unconditional distance-one interface admit universal written reconstructions for arbitrary complex amplitudes. The original proof omits an excess-two subcase and contains a reversed counting label; these remain defects of the frozen text, not retrospectively completed author arguments. The standalone P2 selection theorem is expressly unpaid in S1 and is not independently established by this review; the later S4 composition supplies the required AME-scoped conclusion prospectively.

## 1. Administrative and reading record

- Assigned manifest SHA256 verified:
  `74be5764ec7ffb7038bcba30ae6adf4c09b38d159596c31395e108018f42b7d3`.
- Freeze-receipt SHA256 verified:
  `0f36b892b33f75c8daccf7771a9166785e3cf1a8ff74a894d4172d78d457d70a`.
- Packet SHA256 verified:
  `a3b22a768d95988995b6e122c629b5c9e04ffd19280df860f1dbfebb7439d69a`.
- All four control hashes and all S1–S4 source hashes matched their manifest pins.
- Before mathematical packet reads, I read the complete manifest, receipt and four status-only controls. A PRE-BODY administrative ACK was sent, using the fresh `/bin/date` observation **2026-10-30T13:55:40Z**.
- The entire ordered packet was read raw in windows **1–20, 21–40, 41–60, 61–80, 81–100, 101–114**, including its ending. Coverage was complete: S1 LF1–62, S2 LF1–17, S3 LF1–15, S4 LF1–18. No displayed elision required recovery.
- Fresh substantive-checkpoint observation: **2026-10-30T14:00:10Z**. Fresh observation before final return: **2026-10-30T14:02:29Z**.
- Mathematical work was written and universally quantified. No scientific interpreter, CAS, solver, enumeration, selected graph/tensor/state, author code, external-model CLI or excluded payload was used. No linked prior review body was followed.
- The filesystem write attempt for the reviewer ACK was refused by the `write` tool’s path restriction. No shell or other bypass was attempted. This is the full review text for parent materialization; no `review-v1.md` file was created by me.

## 2. Findings

### Finding 1 — Complete the excess-two classification’s disjoint-support case

**Severity:** MINOR  
**Priority:** P2  
**Confidence:** 1.00  
**File:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261030-n48-t-branch-and-distance-one-interface-v1.md`  
**Lines:** 22–22

In the two-degree-three-row case, the proof excludes intersection size two and then concludes that the supports coincide, without excluding disjoint supports; unique overlap excludes intersection size one, not zero. Since Lemma C′ supplies the \(t=26\) exclusion, its written case split needs the disjoint case explicitly: every degree-two row meeting one degree-three row is supported entirely inside that row’s support, and subsequent degree-two neighbours remain there, so it cannot connect to a degree-three row with disjoint support. In the coincident-support case, the conclusion that exactly one further row exists should invoke component squareness, not connectivity alone. Both closures follow from already stated hypotheses, but they are absent from the frozen argument.

### Finding 2 — Correct the residual-versus-maximal partner count

**Severity:** MINOR  
**Priority:** P3  
**Confidence:** 1.00  
**File:** `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261030-n48-t-branch-and-distance-one-interface-v1.md`  
**Lines:** 30–30

The parenthesis initially labels \(6-d_i(a)\) values as E-carried, whereas \(d_i(a)\) is defined immediately before and after it as the number of E-carried partner values. The correct split is \(d_i(a)\) E-carried values and \(6-d_i(a)\) P-carried values. The subsequent identity and the reconstructed proof use the correct convention, so this does not invalidate the theorem, but the contradictory label should be corrected.

## 3. Per-claim dispositions

| Claim | Disposition | Boundary |
|---|---|---|
| Residual unitary reduction, row bound and excess identity | **SUPPORTED** | Direct reconstruction; A1 supplies only the upper bound on \(t\). |
| No excess-one component, Lemma B′ | **SUPPORTED** | Universal support/orthogonality argument. |
| Excess-two classification, Lemma C′ | **SUPPORTED by reviewer reconstruction** | Original omitted case preserved as Finding 1. |
| \(t=25,26\) exclusion and \(t\in\{24,27,28\}\) | **SUPPORTED** | Conditional on adopted A1 and its declared provenance. |
| Distance-one propagation, closure and isolation | **SUPPORTED** | No classical no-OLS import or f293 premise needed. |
| Complex-amplitude bipartition argument | **SUPPORTED** | Does not require real amplitudes or equal nonzero moduli. |
| Exhaustion of \(m=6,8,10,12\) | **SUPPORTED** | As reconstructed below. |
| “Iff unless” consequence | **SUPPORTED at the qualified scope below** | Uses f293 as the explicit conditional input. |
| P2 implies the stated OA contradiction | **SUPPORTED conditionally** | P2 is not proved or assumed in S1. |
| Standalone universal P2 theorem | **INCONCLUSIVE here; expressly unpaid** | No independent proof of that separate lemma is supplied by this packet review. |
| “P2 is exactly the content” of the underlying f296 source | **INCONCLUSIVE as an exact source-identity assertion** | The frozen input contains S4’s disposition, not that source’s complete standalone lemma. |
| Later no-distance-one/no-six-symbol composition | **SUPPORTED as explicit adopted input S4** | Prospective, AME-scoped, conditional on no-OLS(6); not a retroactive repair of S1. |

No asserted branch/interface theorem was refuted.

## 4. Universal reconstruction of the maximal-count branches

For every paired cut, \(U=6\psi\) is unitary. A modulus-one entry exhausts its row and column norms, so the \(t\) maximal entries occupy distinct singleton rows and columns. Removing them leaves an \(n\times n\) unitary, \(n=36-t\), supported on E.

Every residual line has degree at least two: a singleton residual line would have a modulus-one entry and would already have been removed. Consequently,

\[
48-t=|E|\ge 2(36-t),\qquad t\ge24,
\]
and the residual excess is
\[
e=|E|-2n=t-24.
\]

Adopted A1 gives \(t\le28\), with its declared f113/classical provenance retained.

### Support-component facts

Two distinct rows cannot share exactly one nonzero column, because their inner product would have exactly one nonzero summand. The transposed statement applies to columns.

A connected support component is square: its orthonormal rows give “number of rows \(\le\) number of columns,” and its orthonormal columns give the reverse inequality. Its excess is nonnegative.

A degree-two row supported on a column pair forces any other row meeting that pair to contain both columns.

### Excess zero

Every row and column has degree two. Rows meeting one degree-two row must have the same column pair. Each of those columns has degree two, so the component contains exactly two rows and two columns and is a full \(2\times2\) block.

### Excess one

There is exactly one degree-three row \(R\); every other row has degree two. Any row meeting \(R\) is supported on a two-subset of its three columns. Distinct such two-subsets would meet in exactly one column, which is forbidden.

Thus all such rows use the same pair, leaving the third column of \(R\) with degree one. This contradicts the residual minimum degree.

### Excess two: one degree-four row

Every other row has degree two. Rows meeting the degree-four row use two-subsets of its support, and these pairs must be equal or disjoint.

Minimum column degree requires coverage of all four columns, forcing two disjoint pairs. A column from each pair then shares exactly the degree-four row with the other column, contradicting column orthogonality.

### Excess two: two degree-three rows

Let their supports be \(A\) and \(B\). All other rows have degree two.

- **\(|A\cap B|=1\):** forbidden directly by unique overlap.
- **\(|A\cap B|=2\):** a column in \(A\setminus B\) needs another incident row. Such a degree-two row must use that column and one of the shared columns to avoid a one-column overlap with the first degree-three row. It then meets the second degree-three row in exactly one column, impossible.
- **\(A\cap B=\varnothing\):** any degree-two row meeting the first degree-three row lies wholly in \(A\). A degree-two row adjacent to it must use the same column pair. Therefore no chain of degree-two rows can connect this region to the second degree-three row. This contradicts their membership in one connected component.
- **\(A=B\):** every further row meeting this support uses a two-subset of the common three-column support. Those subsets must all coincide. Connectivity prevents any additional columns, and squareness therefore gives exactly three rows. The component has two degree-three rows and one degree-two row: a \(3\times3\), eight-entry component with row and column degree multisets \((2,3,3)\).

This exhausts the component cases without selecting an instance or assuming amplitudes beyond nonzero support entries and unitarity.

### Consequences

- For \(t=25\), total excess is one. Some component would have excess one, impossible.
- For \(t=26\), total excess is two. With excess-one components impossible, there must be one three-row excess-two component; all remaining components have two rows. Hence \(n\) is odd, contradicting \(n=36-26=10\).

Therefore the supported branch theorem is precisely

\[
\boxed{N=48\ \Longrightarrow\ t\in\{24,27,28\}}
\]

at the adopted A1 import boundary. No exclusion of \(27\) or \(28\), and no existence claim for any surviving profile, follows.

## 5. Universal reconstruction of the distance-one interface

At \((N,t)=(48,24)\), every residual cut has twelve rows and columns and twenty-four entries. Every residual line consequently has degree exactly two. Each of the six pair projections has twelve values, each with exactly two extensions.

For any residual symbol \(a\) at party \(i\),

\[
|E_i(a)|=2d_i(a),
\]

where \(d_i(a)\) is the number of partner values in any one of the other parties. This count is independent of the partner party. Also \(d_i(a)\ge2\): if it were one, all three other coordinates would be fixed throughout a two-word fiber, making those two words identical.

### Closure and complex phases

Starting from an arbitrary distance-one pair whose differing coordinate is D, the two AD rows share one BC column. Degree two and orthogonality force them to share the other BC column as well. Thus a second triple with the same D pair is forced. The other two cuts give the corresponding operations for B and C.

The closure \(S\) has:

- exactly two triples containing each occurring base symbol;
- injective base-pair projections;
- exactly three distinct neighbours of every triple, one for each base coordinate.

It is therefore a connected simple cubic graph on triples.

For each triple \(s\), set

\[
x_s=\psi(s,d_0)\overline{\psi(s,d_1)}\ne0.
\]

Orthogonality gives \(x_{s'}=-x_s\) along every edge. An odd cycle would imply \(x_s=-x_s\), impossible. This argument is valid over arbitrary complex amplitudes; it introduces no reality or common-modulus hypothesis.

Thus the graph is bipartite. Its two parts have equal size, each at least three. Since its triples use distinct base-pair values among twelve available values,

\[
m=|S|\in\{6,8,10,12\}.
\]

### Isolation

Every pair value used by \(S\times\{d_0,d_1\}\) already has its two extensions inside that set:

- a base-pair value comes from one triple and both D values;
- a base–D value comes from the two triples containing the base symbol.

No E word outside the closure can share any such pair value. The complement C is therefore isolated in every paired cut, with \(24-2m\) words and \(12-m\) values per pair system, each of multiplicity two.

The same fiber identity and lower bound \(d\ge2\) hold inside C.

### The four cases

- **\(m=12\):** C is empty. Each base symbol occurs in two triples, so each of the three base parties has exactly six E symbols. This is the six-symbol alternative; S1 correctly does not exclude it unconditionally.

- **\(m=10\):** C has four words and two pair values per system. Fiber degrees are at least two and sum to two, so every party has a singleton C alphabet. Four distinct support words cannot lie in a one-point box.

- **\(m=8\):** C has eight words and four pair values per system. Every C alphabet has at most two symbols. A singleton alphabet would require four partner symbols, contradicting the bound of two for the other parties. Hence every alphabet has exactly two symbols and every pair value occurs twice.

  The C subtensor has a unitary \(4\times4\) residual flattening in all three cuts. Its squared norm is \(4/36\); after normalization, twice its flattening is unitary. It would therefore be an AME(4,2) state.

  For its Pauli weight sums, two-uniformity gives \(A_1=A_2=0\). Each three-qubit marginal has purity \(1/2\), giving weight-three sum three on each triple and therefore \(A_3=12\). Global purity gives \(A_4=3\). The positive spin-flipped state would satisfy

  \[
  \operatorname{Tr}(\rho\widetilde\rho)
   =\frac{A_0-A_1+A_2-A_3+A_4}{16}
   =-\frac12,
  \]

  impossible for two positive semidefinite operators. This exclusion covers complex states.

- **\(m=6\):** C has twelve words and six values per pair system. Its fiber degrees are at least two and sum to six, so every C alphabet has at most three symbols.

This establishes S1’s unconditional interface exactly: a distance-one pair forces either a six-symbol party or the isolated \(m=6\) decomposition.

## 6. The precise “iff unless” statement

Write:

- \(H\): E contains a distance-one pair;
- \(Z\): some party has six E symbols;
- \(M\): the specified isolated \(m=6\) decomposition occurs.

The explicit f293 input supplies

\[
\neg H\Rightarrow\neg Z,
\quad\text{equivalently}\quad Z\Rightarrow H.
\]

The reconstructed interface supplies

\[
H\Rightarrow Z\lor M.
\]

Consequently, the supported qualified equivalence is

\[
\boxed{\neg M\Rightarrow(H\Longleftrightarrow Z)}
\]

or equivalently the stated absence-property equivalence outside M.

“Unless” identifies the only remaining possible exception; it does **not** assert that M exists or that equivalence necessarily fails inside M.

## 7. P2 and prospective composition

### What the conditional P2 argument establishes

In the \(m=6\) branch, bipartition assigns one D value to each part of S. The resulting six words have injective pair projections: base-pair projections were already injective, while the two triples containing any base symbol lie in opposite parts and receive different D values.

If C additionally admits the P2 six-word pair-injective selection, its pair values are disjoint from those of this S selection and from P. Their union with the twenty-four P words has thirty-six words with all six pair projections injective. Every projection must therefore cover all thirty-six pair values, producing an \(\mathrm{OA}(36,4,6,2)\), contrary to the declared no-OLS(6) import.

This conditional argument is **SUPPORTED**.

### What is not independently established here

S1 expressly leaves P2 unreviewed and unassumed. This review does not certify its separate universal formulation, nor infer an unrestricted source-free selection lemma from S4’s AME-scoped conclusion.

Any application to C must retain the actual residual hypotheses: distinct support words, multiplicity two in every pair system, simultaneous residual unitarity in all three cuts, and isolation from the other support.

### What S4 supplies now

S4 is an explicit permitted input establishing, conditional on no-OLS(6), that an AME state at \(N=48,t=24\) has:

1. no residual distance-one pair;
2. no six-symbol residual party, with residual alphabet sizes \(3,4,5\).

It therefore removes the practical need to leave the no-distance-one premise unpaid in a **new prospective composition**. It does not make S1’s original P2 proof exist, verify a broader standalone lemma, or erase the original excess-two proof omission.

## 8. Final accepted boundary

The packet supports:

- \(N=48\Rightarrow t\in\{24,27,28\}\), at the adopted A1 provenance;
- the unconditional distance-one closure/isolation interface at \(t=24\);
- prospectively, using explicit S4 and no-OLS(6), no distance-one pair and no six-symbol residual party at \(t=24\).

It does **not** establish a standalone unrestricted P2 theorem, exclude \(t=27\) or \(28\), exclude support 48, prove any \(N\ge49\) bound, or provide a witness.