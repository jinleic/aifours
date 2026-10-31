# R-minus: exact nonuniform 88-word law and finite type-class witness

**Scope.** On the original source-transcribed R-minus neighbour lists and unrestricted full-neighbour decoders, the explicit binary winning set and positive rational distribution below satisfy

```
H(X_1,...,X_10) > (649/100) max_v H(X_v).
```

The same binary strategy's uniform winning-set law has ratio `log_2 88 < 649/100`. Thus the nonuniform law provably improves this actual strategy's fixed-support entropy ratio. An explicit finite common-alphabet type-class construction below has **more than `q^(649/100)` winners**. **This does not improve the recorded original lower bound `20/3`: 649/100 < 20/3.** No unrestricted upper bound, novelty or solution of the guessing-number problem is claimed.

## 1. Literal original graph and binary support

Vertices are `1,...,10`, with edges:

```
12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10
56 59 5-10 67 68 69 78 7-10 89 8-10
```

The graph was visually transcribed from the supplied public R-minus figure; 3–4 is an edge and 9–10 is absent. An integer word `x` means bit `v-1` is vertex v's binary value. The following two lists are aligned: word `x_i` has probability `w_i/6000`.

```
words = [
0,3,5,6,48,51,53,54,139,142,187,190,192,197,201,204,
240,245,249,252,272,275,277,278,288,291,293,294,411,414,427,430,
464,469,473,476,480,485,489,492,525,526,573,574,576,579,588,591,
624,627,636,639,640,645,646,649,688,693,694,697,711,715,759,763,
797,798,813,814,848,851,860,863,864,867,876,879,912,917,918,921,
928,933,934,937,983,987,999,1003]

weights = [
86,86,128,86,46,47,69,46,86,86,47,46,86,128,86,86,
46,69,47,46,47,47,69,47,47,47,69,46,47,47,47,47,
46,69,47,47,46,69,47,46,128,86,69,46,86,86,86,86,
46,46,46,46,128,191,128,128,69,103,69,69,128,86,69,46,
69,47,69,46,46,46,47,47,46,46,46,46,69,103,69,69,
69,103,69,69,69,47,69,46]
```

The sum of weights is 6000 and every weight is positive. At each vertex v, construct a lookup from the **full original neighbour tuple** of each of these words to its v-bit. The exact checker independently found no conflicting outputs. Complete each lookup by returning 0 on every other neighbour tuple. Exhaustive testing of all 1024 binary words found the resulting full-domain decoder system has **exactly these 88 winners**. The historical file from which the word list was proposed is therefore not used as a correctness premise: the FD and actual decoder checks were redone here.

## 2. Exact homogeneous entropy comparison

For this distribution the counts of 1 at vertices 1–10 are exactly

```
[3530,2474,3526,2475,2474,2468,2469,3529,2476,3523].
```

All have denominator `N=6000`. Binary entropy is symmetric and increases up to one-half, so the maximum marginal entropy occurs at vertex 10, whose two counts are `a=3523` and `b=2477`, the closest pair to equality. For `J=H(X_1,...,X_10)` and `h=H(X_10)`,

```
6000(100 J - 649 h)
 = log( a^(649a) b^(649b) /
        [6000^(549*6000) product_i w_i^(100 w_i)] ).
```

The independent standard-library integer checker explicitly constructs the numerator L and denominator R of that displayed fraction and verifies the stronger inequality

```
L >= 2^4448 R > R.
```

This is an integer-power comparison, not a floating-point entropy estimate. L and R have respectively **45,064,415** and **45,059,967** bits; their big-endian byte SHA256s are recorded in the certificate receipt. Therefore `100J>649h=649 max_v H(X_v)`.

For comparison, the unweighted 88-word support has marginal 1-counts
`[48,40,48,40,44,44,40,48,44,48]`, so its maximum marginal entropy is exactly `ln 2` and its uniform joint entropy is `ln 88`. The integer checker also verifies `2^649 > 88^100`, proving `log_2 88 < 649/100` without a float.

## 3. Complete actual finite-word caller

Set `t=100`, `n=6000t=600000`. Take every row sequence of length n over the 88 words having exactly `t w_i` copies of word i. Its size is the integer

```
M = (600000)! / product_i (100 w_i)!
```

At vertex v the binary column has a fixed number `100 a_v` of 1s, with the `a_v` from the ten-count vector above. Its type alphabet size is `binom(600000,100 a_v)`. The largest occurs at vertex 10 and is

```
q = Q = binom(600000,247700).
```

For each v inject its possible binary columns into `[q]` by lexicographic rank. On a full q-ary neighbour tuple, first unrank each label if valid for that neighbour's column type; then apply that vertex's binary decoder rowwise, and rank the resulting output column if it has v's prescribed type. If any input label is invalid or the result has the wrong type, output a fixed q-symbol. This gives a **full-domain original-neighbour decoder**, not a partial lookup valid only on the desired set. Every row sequence in the type class yields a winning word, and distinct row sequences have different 10-column tuples.

To prove the strict bound without computing or enumerating `M`, `Q` or the enormous q-ary domain, use the standard elementary type estimates for this actual 88-symbol law:

```
M >= exp(n J) / (n+1)^88,      Q <= exp(n h).
```

The first follows because the exact type `t w_i` is a most probable multinomial type under its own law: moving one count from a coordinate above its integer expectation to one below it increases type probability; at most `(n+1)^88` types exist. The second follows since the probability of a fixed binary type under its empirical Bernoulli law is at most 1. These statements use positive weights and the counts given above, not an unconstructed entropy vector.

The certified power gap yields `n(100J-649h) >= 4448t ln 2 = 444800 ln 2`. The checker separately verifies the exact integer inequality

```
2^444800 > 600001^8800.
```

Consequently

```
log(M^100 / Q^649)
 >= n(100J-649h) - 8800 log(n+1) > 0,
```

so the explicit actual strategy has at least M winning words and `M^100 > Q^649`. This is a construction/existence proof; it does not enumerate those enormous words or claim the total winning set is exactly M.

## 4. Experiments, pins and boundaries

The historical candidate word file was used solely as a proposal and independently verified; its SHA256 is `64e4cefcf5a10a89d44466c81507da4e2e0b30212897f968eaef6f1677d41588`. A deterministic, bounded numpy search over its 88-word support used seed `20261028`, 12 restarts and 144000 updates. It proposed the rational weights above; the search's approximate best ratio `6.498881921406667` is **not** itself an exact witness. Its pinned output, containing the exact aligned lists and rounded 6000-denominator law, is `frontier-20261028-fd-law-search-precise-result.json`, SHA256 `c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc`.

The separate integer-only checker `frontier-20261028-weighted-fd-certificate.py`, SHA256 `d62dfb26cb63fa6460a7f808744579263f1c27a4fbb4a5f2898f1cfcde2e20c5`, rechecks graph neighbourhood lookups, all 1024 actual binary decoder inputs, weight/marginal counts, the 45-million-bit comparison, the uniform-baseline comparison and the finite-type inequality. Its executed receipt `frontier-20261028-weighted-fd-certificate-result.json`, SHA256 `5efe17b8065bba5d1203beebc3b0e5fffbaf707e8bcef8f97b61f7a141a8b047`, records these outputs. The actual run took approximately **45.17 seconds** and finished **Wed Oct 28 17:07:44 PDT 2026**. No enormous type class was enumerated.

A first coarse rounding at denominator 600 failed the `649/100` integer check; it is not a witness. The finer rational candidate was separately checked as above. The numerical search's independent exact `20/3` test returned false for this rounded law; no claim about other weights or support sets follows. The source-transcribed graph, written bridge proof and standalone exact checker still need appropriate independent review. This is not formal proof, scientific consensus, current SOTA/novelty clearance, or an improvement on `20/3`.

**END.**
