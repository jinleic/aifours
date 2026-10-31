# Alternating groups: three-index collision for n≥500000

**Disposition: same-harness written support, conditional on the precise named statement-level imports below.** For every integer `n≥500000`, among any three proper subgroups of `A_n`—repetitions allowed—two subgroup indices have greatest common divisor at least 8. Consequently any eight pairwise disjoint cosets in these `A_n` have two subgroup indices with gcd at least 8: none of their subgroups can equal the whole group. This says nothing about other degrees or other simple groups. No source-specific P7 equivalence, new global Sun8 result, priority, human, independent-model-family, or formal/kernel verification is asserted.

Native clock observed before composing: **2026-10-28T20:41:44-0700 PDT**; this is not an asserted creation time.

## Imports

1. Dusart [arXiv:1002.0442](https://arxiv.org/abs/1002.0442), Proposition 6.8: for `x≥396738` a prime lies in `(x, x(1+1/(25 ln²x))]`. The reviewer read the named PDF statement; its proof was not replayed by parent or reviewer.
2. Jordan's prime-cycle theorem, [Jones arXiv:1209.5169v1, Theorem 1.1](https://arxiv.org/html/1209.5169v1): a primitive permutation group containing a prime cycle fixing at least three points contains `A_n`. Parent and reviewer observed this statement in the source; its proof was not replayed. Jones attributes CFSG reliance to his separate Theorem 1.2, not to Theorem 1.1.
3. Standard Sylow, orbit-stabilizer, alternating-group subset transitivity, block-system and binomial identities. No Sun7/R8 or other prior research result is imported.

## Reconstruction

Put `x=6n/7`. The Dusart import yields a prime `r>x` with `r<156n/175<n−3`; the last step uses `19n>525`. Thus `t=n−r≥4`, `7t<n`, and `r>n/2` and `r>7`.

For any proper subgroup `H<A_n` whose index is not divisible by `r`, a Sylow `r`-subgroup lies in `H`. Because `2r>n`, an element of order `r` is an `r`-cycle fixing `t≥4` points. If `H` were transitive but imprimitive, its block system would have fewer than `r` blocks, so the cycle would fix each block and place all `r` moved points in one; a nontrivial block system would require `n≥2r`, a contradiction. Jordan then excludes a proper transitive `H`. Hence `H` is intransitive, and the complement of its orbit containing the moved points has size `1≤u≤t`; `C(n,u)` divides `[A_n:H]`.

For `1≤i<j≤t`, let `A=C(n,i)`, `B=C(n,j)`, `g=gcd(A,B)`. The identity `A C(n−i,j−i)=B C(j,i)` and coprimality of `A/g,B/g` imply `A/g` divides `C(j,i)`. But `A/C(j,i)=∏_{h<i}(n−h)/(j−h)≥n/j>7`; hence `g≤7` would make the positive divisor `A/g` larger than `C(j,i)`. Therefore `g>7`. Equal factors also have gcd `C(n,i)≥n>7` since `i≤t<n/2`.

Among any three proper subgroup indices, two divisible by `r` already have gcd at least `r>7`; otherwise at least two are `r`-free and their binomial divisors have gcd greater than 7. This proves the stated collision theorem, including repeated subgroups.

## Evidence and limits

- [Candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-large-degrees-v1.md), 42 LF, SHA-256 `be1dd7df8b322eac2bd06439be560b1d8b31967f8b3e6c220067a45bd12232f0`; parent read its complete body after the earlier [arithmetic overlay](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json). This candidate is separate from the later corrected all-degree candidate.
- [f132 review](../review-waves/f132-alternating-large-degrees-jordan-dusart/review-v1.md), `84372c2a7060347d1694dca15121796dd42754a71b4295163aec0fa379ea0db0`: 0 FATAL / 0 MAJOR / 2 presentational MINORs, repaired in this wording (`r²∤n!` made explicit; natural logarithm used). Its independently written [integer-control receipt](../review-waves/f132-alternating-large-degrees-jordan-dusart/reviewer-binomial-gcd-control-v1.receipt.json), `a3add4cf74ca51ad97ff24c72f5ba5357ce7cd94c91a17305c950ed633f69b52`, reports 89,089 strict-inequality pair checks and 6,339 equal-factor checks, plus boundary controls; it is a finite check, not a proof of the universal theorem.
- Parent independently spot-checked the exact binomial/divisibility identity and strictness in-session: `(n,i,j)=(24,1,3)` and `(64,1,8)` give gcd 8, while boundary `(14,1,2)` has gcd 7. These are controls only.

The separate candidate claiming all alternating degrees has a fatal small-degree counterexample and is not imported here. Novelty and priority are unknown; the imported theorem proofs remain unreplayed.
