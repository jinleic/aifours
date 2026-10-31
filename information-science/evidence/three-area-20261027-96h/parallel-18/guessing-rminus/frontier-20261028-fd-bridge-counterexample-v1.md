# R-minus: a fixed-winning-set uniformization shortcut is false

Owner: InfoGuessingRminus-2. Original target is the guessing number of the ten-vertex graph R-minus, with arbitrary finite common alphabets and full original-neighbour decoders. This is a **new exact obstruction to a proposed FD-law search shortcut and an actual finite-word construction**, not an improved original bound or an upper inequality. The historical interval `20/3 <= gn(R-minus) <= 1847/276` is unchanged. Prior process outcomes are not used as acceptance of this calculation.

## Precise falsified implication

The following assertion is false, even when the support is the **entire winning set of an actual binary R-minus strategy**:

> Replacing an FD law on a fixed winning support by the uniform law on that SAME support cannot decrease `H(X_1,...,X_10) / max_v H(X_v)`.

This does **not** contradict the separate, correct type-class observation that uniform laws on appropriately enlarged finite supports can approximate a nonuniform law's ratio. It only rules out discarding nonuniform weights while retaining the same winning support.

## Original graph and actual binary strategy

Use the previously source-transcribed neighbourhoods, one-based:

```
1: 2 3 4 5 6 7       2: 1 3 7 9 10
3: 1 2 4 8 9         4: 1 3 5 8 10
5: 1 4 6 9 10        6: 1 5 7 8 9
7: 1 2 6 8 10        8: 3 4 6 7 9 10
9: 2 3 5 6 8        10: 2 4 5 7 8
```

Define four binary words by their sets of 1-vertices:

```
A = {1,2}, B = {1,3}, C = {4}, D = {5}.
```

The six symmetric-difference supports are `{2,3}`, `{4,5}`, `{1,2,4}`, `{1,2,5}`, `{1,3,4}`, `{1,3,5}`. Each has no isolated vertex in the ORIGINAL graph: respectively the relevant edges are `2–3`, `4–5`, `1–2` and `1–4`, `1–2` and `1–5`, `1–3` and `1–4`, `1–3` and `1–5`.

For binary words, two words violate an FD at vertex v exactly when their difference contains v but contains no neighbour of v. Hence the four words satisfy every FD. Explicitly define each full-domain binary decoder `f_v` as follows: on an observed neighbour tuple appearing among these four words return that word's v-bit (unique by the FD); on every other neighbour tuple return 0. The complete binary enumeration described below independently finds that the resulting actual winning set is **exactly** `{A,B,C,D}`; this equality is not assumed from FD consistency alone.

## Strictly better law on the SAME winning set

Let `h(p)=-p ln p-(1-p) ln(1-p)`. Under the uniform distribution on the four winning words, `X_1` is Bernoulli(1/2), `X_2,...,X_5` are Bernoulli(1/4), and all other variables are constant. Thus

```
H(X_1,...,X_10) = ln 4,   max_v H(X_v) = ln 2,
ratio = 2.
```

Now use positive probabilities `(1/3,1/3,1/6,1/6)` on `(A,B,C,D)`. The marginals are

```
P(X_1=1)=2/3; P(X_2=1)=P(X_3=1)=1/3;
P(X_4=1)=P(X_5=1)=1/6; X_6,...,X_10 constant.
```

Because binary entropy is symmetric and strictly increasing on `(0,1/2)`, the largest marginal entropy is `h(1/3)=h(2/3)`. Conditional on `X_1`, the two possible winning words in either fibre are equiprobable, hence

```
H(X_1,...,X_10) = h(2/3) + ln 2,
H(X_1,...,X_10) / max_v H(X_v) = 1 + ln 2 / h(2/3) > 2.
```

The final strict inequality is exact: `h(2/3)=ln 3-(2/3)ln 2 < ln 2` because `3^3=27<32=2^5`. No floating-point comparison is needed.

## Actual finite-alphabet realization, not just a limiting law

Take length `n=24` and all row sequences with counts `(8,8,4,4)` of `(A,B,C,D)`. Their number is

```
M = 24! / (8! 8! 4! 4!) = 662585823900.
```

At vertex 1 the binary column has exactly 16 ones; at vertices 2 and 3 it has 8 ones; at vertices 4 and 5 it has 4 ones; all other columns are the all-zero string. The largest marginal type-class alphabet has size

```
q = C(24,8) = C(24,16) = 735471,
q^2 = 540917591841 < M.
```

For each vertex, lexicographically rank its possible binary columns and inject them into `[q]`. Define its full `[q]`-alphabet decoder on each observed neighbour tuple by undoing the valid neighbour-column ranks, applying the binary `f_v` above independently at every row, and ranking the resulting v-column when it has the required type. For an invalid neighbour label or an output column of the wrong type, return a fixed symbol. This explicitly defines a decoder on the **entire** original neighbour input domain.

Every listed 24-row sequence gives an actual q-ary winning word, since every row is one of the four binary winning words and all of its column labels are valid. The labelled map is injective: recovering all ten binary columns recovers the full row sequence. Therefore an actual finite common-alphabet strategy has at least `M>q^2` winning words. The experiment does not enumerate this huge q-ary space; the all-domain construction and injectivity are proved above.

This finite strategy demonstrates the nonuniform-law/type-class bridge on the ORIGINAL graph. Its exponent is far below the already known `20/3` lower bound; it is **not** an improvement of that bound. The finding does not exclude any other code family, alphabet, nonlinear decoder or universal inequality.

## Exact experiment and verification performed

The bounded standard-library Python experiment `frontier-20261028-fd-bridge-counterexample.py` has SHA256 `a2d7420e802c24537976dab0e55198f2c81ac4c8e055d9f941707331dbaef875`; it was executed once with `python3` on 2026-10-28. Its newly created receipt `frontier-20261028-fd-bridge-counterexample-result.json` has SHA256 `68296148d53fe82941335102fd9c1ae2ddd1b98c4da23cffb57be6db6f0a2016`.

Observed results: the embedded graph is symmetric, has 26 edges, contains 3–4 and omits 9–10; all 60 pair/vertex FD comparisons pass; the defined FULL binary decoders have exactly four winners after all 1024 binary inputs are checked; weighted marginal counts are `[4,2,2,1,1,0,0,0,0,0]` out of 6; and exact integer factorial/binomial arithmetic gives the displayed M, q and positive gap `121668232059`. The script tests `n=6b` in increasing `b=1,...,1000` and finds `b=4` first; this is only a search result for this one prescribed type family, not a global minimal block length or bound.

The proof of the original neighbour list is a visual transcription of the public graph figure, not re-certified here. No model CLI, prior unvalidated review result or historical quarantined proof was used. Written proof plus one exact local implementation is not independent expert review, a formal proof, novelty clearance, or an accepted original-target result.

**END.**
