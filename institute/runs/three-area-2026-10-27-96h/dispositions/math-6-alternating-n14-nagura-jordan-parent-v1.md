# Alternating groups n≥14: four indices force gcd at least nine

**Disposition: same-harness written support, conditional on two classical statement-level imports.** For every integer `n≥14`, among any four proper subgroups of `A_n`—repetitions allowed—some pair of indices has gcd at least **9**. Hence the eight-disjoint-coset Sun8 assertion holds for these alternating groups, and the analogous coset index inequality holds for 4 through 9 cosets. No n≤13 result, all-simple-group theorem, source-specific P7 equivalence, global Sun8 closure, novelty or formal proof is asserted.

Native clock observed before composing: **2026-10-28T21:19:15-0700 PDT**, not an asserted file-creation time.

## Exact imports and source evidence

1. Nagura, *On The Interval Containing At Least One Prime Number*, Proc. Japan Acad. 28(4), 177–181 (1952), [DOI 10.3792/pja/1195570997](https://doi.org/10.3792/pja/1195570997). The formal theorem on **page 180**, case `a₅=25`, states `25≤x<p<(1+1/5)x` for some prime p. Parent visually read the reviewer raster of that page and page 177 in the hash-pinned source. The strict **lower** endpoint is load-bearing; the informal first-page word “between” is not the only evidence. Nagura's proof was not replayed.
2. Jordan's prime-cycle theorem, [Jones arXiv:1209.5169v1, Theorem 1.1](https://arxiv.org/html/1209.5169v1): a primitive group containing a prime-length cycle fixing at least three points contains `A_n`. Parent and reviewer observed the statement; the classical proof referred to Dixon–Mortimer/Wielandt was not replayed.

No Jones Theorem 1.2, Sylow-overgroup classification, Sun7/R8 or prior research theorem is needed. The three earlier [arithmetic](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json), [fatal seven-index](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json) and [cardinality](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-p7-cardinality-addendum-v1.json) corrections were read before this candidate. The A₇ counterexample to the old assertion remains valid and is outside the present degree range.

## Reconstruction

For `n≥50`, set `m=floor(n/2)≥25`. Nagura supplies `m<r<6m/5`, so `r>n/2`, `r>8`, and `t=n−r>4m/5≥20`. For `14≤n≤49`, the candidate's explicit table supplies respectively r=11 for n=14–21, 13 for 22–25, 17 for 26–33, 19 for 34–37, 23 for 38–45, and 29 for 46–49; each has `n/2<r≤n−3`. In every case `r` is prime, `t≥3` and `t<n/2`.

If a proper subgroup H has r-free index, it contains an r-cycle, because `2r>n` and r occurs once in `|A_n|`. If H were transitive but imprimitive, its block count and block size would both be at most n/2<r. The prime cycle would fix every block but require an r-element orbit inside a block, impossible. A transitive H would therefore be primitive and contain `A_n` by Jordan, also impossible. Thus H is intransitive. The complement of its orbit containing the moved points has size `1≤u≤t`; the corresponding alternating set stabilizer has index `C(n,u)`, which divides `[A_n:H]`.

For `3≤i<j<n/2`, let `A=C(n,i)`, `B=C(n,j)`, `g=gcd(A,B)`. The binomial identity `A C(n−i,j−i)=B C(j,i)` implies `A/g` divides `C(j,i)`. Therefore `g≥A/C(j,i)=∏_{h<i}(n−h)/(j−h)≥(n/j)^i>2^i≥8`, so `g≥9`. Equal u labels also collide since `C(n,u)≥n>8`. In a family with all pairwise gcds at most eight, at most one r-free index can therefore have `u≥3`.

For types u=1 and u=2, `gcd(n,C(n,2))` is n for odd n and n/2 for even n, greater than eight except n=14 and 16. In ordinary degrees at most one index has either type, so there are at most two r-free indices. At n=14, allowed factors are 14,91,364, and the last collides above eight with both others. At n=16, r=11 restricts u≤5 and factors are 16,120,560,1820,4368; type 2 collides above eight with every type 3–5. Since two types ≥3 cannot coexist, at most two r-free indices remain there as well. The u≤t restriction matters: u=6 is not allowed at n=16.

Two r-divisible indices have gcd at least r>8, so there is at most one such index. Total at most three: any four proper subgroups contain a pair with gcd≥9. In any disjoint family of at least two cosets, all subgroup choices are proper; the claimed k=4,…,9 consequences follow. No consequence for k≥10 follows from the threshold nine alone.

## Verification and limits

Parent read the complete 71-LF [candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-nagura-jordan-v1.md), SHA-256 `521a823bd2d27618cde002b72c742f7bb12116985f0ae2bc3d501545c8738d6a`, the complete 119-LF [f143 review](../review-waves/f143-alternating-nagura-jordan-n14/review-v1.md), `e2fabe8abbfb5a8c789e3702563123dfeb7d38bf4238bc2c7213ee5f45e74311`, and the [formal source raster](../review-waves/f143-alternating-nagura-jordan-n14/reviewer-f143-nagura-p180-150dpi.png). The review found 0 FATAL / 0 MAJOR / 1 citation MINOR, discharged by citing page 180 explicitly above, and ran its own exact controls with disclosed earlier reviewer expectation failures.

Parent separately checked all 36 table degrees, 64,988 binomial pairs in a bounded range, and the exceptional gcd matrices; [receipt](../review-waves/f143-alternating-nagura-jordan-n14/parent-prime-binomial-controls-v1.json), `b5fc4599759a459307cc54ffb02780bb6e86969edbb9cdbddb0bf3711c89ebff`. Boundary examples n=14 and n=16 demonstrate why small u types need separate treatment. The finite checks support arithmetic only; the universal proof and both classical imports are not formally verified.

This is a prospective n≥14 result, not a repair of the false all-n seven-index assertion. Small-degree and broader finite-group successor packets remain separate unreviewed candidates. Same-harness evidence is not human, independent-model-family or formal/kernel acceptance.
