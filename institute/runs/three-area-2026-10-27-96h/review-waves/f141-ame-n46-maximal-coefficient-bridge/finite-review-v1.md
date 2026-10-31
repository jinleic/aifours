# Finite review: support graphs and active-incidence arithmetic

**Finite-only verdict: 0 FATAL / 0 MAJOR / 0 MINOR within the checks stated below.** For the explicitly enumerated `n=2,3,4` and excesses `1,2,3`, the observed support-graph counts agree with the corresponding small cases; both nonempty survivor classes have explicit exact unitary realizations. The `44−12` contradiction is valid under the precise set/projection assumptions in §4. This verdict does **not** pass, reject, or otherwise decide the all-dimensional support classification or any physical implication. The finite counts cannot establish those results.

Native clock observed immediately before composing this review: `2026-10-28T21:00:48-0700 PDT`. This is a preceding observation, not a claimed exact creation time. This is a same-harness reviewer-written program and review, not human, independent-model-family, formal/kernel, or novelty review. No author code was imported or executed.

## 1. Inputs and evidence binding

Manifest `manifest-v1.json`, SHA-256 `dc1c9fea4f62d9c90d77ec8bdce1985667b9e8866f9a22d36982239e1213fc65`, was read completely. Its five declared UTF-8 texts were verified by full SHA-256, byte count and LF count before interpretation, and then read completely in the declared order:

| Order | Manifest input role | SHA-256 | Bytes | LF |
|---:|---|---|---:|---:|
| 1 | main bridge candidate | `635e3ed2fe790efb70b297fa9dab119cbda31e0d256114e9591d89ce60014dde` | 9,586 | 85 |
| 2 | two-excess classification and its correction | `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0` | 5,264 | 43 |
| 3 | three-excess classification | `a37a958ab0fca716ddeddd527a5e0cc4e8e35938c628f42e264f815488742bc2` | 4,992 | 35 |
| 4 | prior maximal-coefficient disposition, context only | `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b` | 5,473 | 28 |
| 5 | separate branch disposition, context only | `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0` | 5,552 | 25 |

The manifest declares no PDF, page, or separate certificate-data file; none was therefore hashed, visually inspected or parsed as such. The third text names an earlier one-excess result as an author-side import; it was not replayed as an all-dimensional theorem here. The two prior dispositions and their classical imports are context, not premises used to establish the finite counts or the incidence arithmetic.

The reviewer-authored standard-library-only [program](finite-enumerate-v1.py) has SHA-256 `a4f047cff040e7657dbb77893da7005fa2ee81e6357ad4769c3e0b63c0058639`; its [receipt](finite-receipt-v1.json) has SHA-256 `f8439fe50a141d2fc103dad1da50164fd38275919a70d928e4e4d6098b42c9e8`. Run from this review directory as `python3 -B finite-enumerate-v1.py`, it completed with exit status 0; shell clock observations before and after were both `2026-10-28T21:00:15-0700 PDT`. The program records start `2026-10-28T21:00:15.302298-07:00`, end **before receipt creation** `2026-10-28T21:00:15.432242-07:00`, and 0.12995 s monotonic elapsed to that point. Receipt records Python 3.14.3, platform, input pins, all counts, exact matrices and 19 reason-specific controls. The shell's post-run clock/hash commands executed after the Python process, corroborating its zero exit status; no exact completion or file-creation timestamp is inferred.

## 2. Exhaustive labeled graph counts

For each `n` and `m=2n+r`, the program iterates every `m`-subset of the `n²` labeled cells, verifies the number enumerated equals `binomial(n²,m)`, and applies these necessary conditions in this order:

1. every row and column has degree at least two;
2. no two rows have exactly one common nonzero column;
3. no two columns have exactly one common nonzero row;
4. each connected bipartite component has equally many row and column vertices.

The one-overlap conditions follow because a one-term inner product of nonzero entries cannot vanish. A component of a unitary must be square because its isolated submatrix has both orthonormal rows and orthonormal columns. These graph conditions are **necessary, not generally sufficient**, for a complex unitary.

| `n` | `m` | All labeled edge sets | Min degree both sides | No single row overlap | No single overlap either side | Square-component survivors |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 0 | 0 | 0 | 0 | 0 |
| 2 | 6 | 0 | 0 | 0 | 0 | 0 |
| 2 | 7 | 0 | 0 | 0 | 0 | 0 |
| 3 | 7 | 36 | 18 | 0 | 0 | 0 |
| 3 | 8 | 9 | 9 | 9 | 9 | 9 |
| 3 | 9 | 1 | 1 | 1 | 1 | 1 |
| 4 | 9 | 11,440 | 816 | 0 | 0 | 0 |
| 4 | 10 | 8,008 | 2,040 | 72 | 0 | 0 |
| 4 | 11 | 4,368 | 2,304 | 0 | 0 | 0 |

The `n=2` cases are vacuous because `m>n²`. Counts are labeled, not quotiented by permutations. For `n=4,m=10`, testing only rows would incorrectly retain 72 graphs; the column test eliminates them all. No graph in this bounded enumeration passes both overlap tests and then fails the square-component test; §3 supplies a separate control where the square test is essential.

There are exactly two survivor shape classes, each connected. Row masks use bit `j` for column `j`, with independent row/column permutations canonicalized:

- `n=3,m=8`: 9 labeled graphs, one `3×3` component with canonical row masks `(3,7,7)` and row- and column-degree sequences `(2,3,3)`; equivalently the full 3×3 support with one cell removed.
- `n=3,m=9`: 1 labeled graph, one full `3×3` component with canonical row masks `(7,7,7)` and row- and column-degree sequences `(3,3,3)`.

The program computes component vertex counts, edge counts, degree sequences and canonical masks, not merely a component-count statistic; the complete shape records are in the receipt.

### Exact complex-unitary positive controls

Both candidate shapes are not just graph survivors. The following eight-entry real rational orthogonal matrix was checked by exact integer row and column Gram products:

```text
          1     [ 15   20    0 ]
U₈  =    --  ×  [-12    9   20 ] .
          25    [ 16  -12   15 ]
```

Its numerator has Gram matrix `625 I₃` on both sides. Every one of the nine labeled `3×3` single-zero supports follows by independently permuting rows and columns, preserving unitarity. For the full support the control is

`F₃ = (1/√3) [[1,1,1],[1,ω,ω²],[1,ω²,ω]]`, where `ω²+ω+1=0` and `conj(ω)=ω²`.

The program computes both Gram products exactly in `ℤ[ω]` before normalization and obtains `3 I₃`. Thus **all ten** bounded graph survivors are realized; this does not make the graph filters sufficient outside the enumerated cases.

## 3. Weaker-filter false positive and intended-reason controls

Starting from the independently Gram-checked `U₈ ⊕ (1/5)[[3,4],[-4,3]]`, whose five row masks are `(3,7,7,24,24)`, move the column-2 edges from rows 1 and 2 to rows 3 and 4, using zero-based indices. The resulting five masks are

```text
(3,3,3,28,28),   columns (7,7,24,24,24).
```

The support has 12 entries (`2n+2`), every row and column has degree at least two, and no pair of rows or columns overlaps in exactly one position. It nevertheless has disconnected `3×2` and `2×3` complete components, so fails the square-component test. In particular, the three nonzero row vectors in the `3×2` component cannot be mutually orthogonal in `ℂ²`; **no complex unitary has this support**. This is one independently constructed targeted example, not a complete `n=5` enumeration. It also respects the source's mandatory correction that overlap-only filtering can retain rectangular components.

The receipt records 19 passing checks, including these mutations and their exact intended failure categories:

| Mutation/control | Observed reason |
|---|---|
| delete one entry so a row has degree 1 | `MIN_DEGREE` |
| delete an entry creating a one-column row intersection | `ROW_SINGLE_OVERLAP` |
| add two entries to a `2×2 ⊕ 2×2` support; row overlaps remain permissible but two columns meet once | `COLUMN_SINGLE_OVERLAP` |
| move the four entries as in the five-dimensional example | `RECTANGULAR_COMPONENT` |
| fill the missing cell of the 8-entry support while checking the original expected shape | `SHAPE_MISMATCH` |
| negate one nonzero entry of `U₈`, preserving support and all individual row/column norms | `GRAM_OFFDIAGONAL` |
| increase a nonzero entry of `U₈` by one numerator unit | `GRAM_DIAGONAL` |
| replace one `ω` by `1` in the Fourier numerator | `GRAM_OFFDIAGONAL` |

The positive `U₈`, Fourier, four-dimensional direct sum and five-dimensional direct sum are explicitly checked before the related graph or Gram mutations. Each control records both expected and actual reason; an arbitrary exception is not accepted as the intended rejection.

## 4. Exact `44−12` incidence contradiction

This calculation is a conditional finite set statement. Its assumptions are:

- Four coordinate sets `Q_i` each have exactly 6 symbols. `P` and `E` are disjoint sets of distinct four-coordinate words, with `|P|=29` and, in the stated instance, `|E|=17`.
- For each coordinate `i`, `A_i=π_i(E)` has exactly 3 symbols. For every pair `i<j`, `|π_ij(E)|=7`.
- For every pair `i<j`, the projection `P→Q_i×Q_j` is injective and `π_ij(P)` is disjoint from `π_ij(E)`.

The size 17 and multiplicities of `E` are not used in the final arithmetic once the stated alphabet and pair-projection cardinalities are given. Nor is an amplitude or an actual unitary needed for this conditional counting step. The assumptions that establish the alphabet sizes and the disjoint/injective pair projections are **not** independently derived by this finite control.

For every pair `i,j`, injectivity gives `|π_ij(P)|=29`; disjointness and `29+7=6²` make `π_ij(P)` and `π_ij(E)` a partition of all 36 ordered symbol pairs. Fix `i` and any partner `j`. Exactly `3·6=18` pairs have their `i` symbol in `A_i`, all seven `E` pairs are among them, and the remaining 11 are `P` pairs. Injectivity identifies them with exactly 11 words of `P` active at coordinate `i`. Similarly, all seven `E` pairs lie in the `3×3` active/active rectangle, so exactly `9−7=2` `P` words are active at **both** coordinates of each pair.

Writing `k(x)` for the number of active coordinates of `x∈P`, these exact counts give

```text
Σ_x k(x) = 4·11 = 44,
Σ_x binom(k(x),2) = 6·2 = 12.
```

For `k=0,1,2,3,4`, the values of `k−binom(k,2)` are `0,1,1,0,−2`. Hence each is at most 1, whereas the sums would require `44−12=32 > |P|=29`. This is a contradiction. The partition/saturation, injectivity, active alphabet size three and seven distinct `E` pair values are load-bearing; merely counting words without those hypotheses does not establish the two sums.

As an independent finite arithmetic control, the program enumerates all `binomial(33,4)=40,920` nonnegative histograms of 29 words by `k∈{0,1,2,3,4}`. Exactly 213 have pair-incidence sum 12, none also has single-incidence sum 44, and the maximum possible single-incidence sum among those 213 is 41. The receipt also records two intended boundary mutations as **abstract incidence multisets only**, not actual `P/E` supports:

- With 32 words, two two-active words per coordinate pair plus five one-active words per coordinate produce exactly 11 per coordinate and 2 per pair (`44−12=32`).
- With 29 words and pair total relaxed from 12 to 15, an explicit multiset still has 11 active incidences per coordinate and total 44 (`44−15=29`), with pair multiplicities `3,3,2,3,2,2`.

These controls show the counting contradiction responds to the intended bound; neither is claimed realizable as a four-coordinate set with the remaining projection assumptions.

## 5. Explicit limits

The complete enumeration covers only `n=2,3,4` and the three specified support sizes. The `n=5` example is an isolated negative control; dimensions 7, 8 and 9, general support classifications, and the derivation of the incidence assumptions were not decided by it. The inputs contain previously supported and author-proposed results, but no prior theorem, human review, external-family review, formal certificate, physical implication, novelty or global claim is adopted by this finite verdict.
