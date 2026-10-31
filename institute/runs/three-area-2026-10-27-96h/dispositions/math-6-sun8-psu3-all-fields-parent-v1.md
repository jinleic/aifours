# Sun8 for every PSU(3,q), q≥3: conditional written disposition

Native clock observed before writing: **2026-10-28T18:04:10-0700 PDT**. The statement is an infinite-family deduction from named group-theory and primitive-prime imports. It does not establish arbitrary-group Sun8, novelty or priority, human/cross-model review, or formal-kernel verification.

## Statement and imports

For every prime power `q≥3`, **conditional on the named unitary order/simplicity, unique-Sylow-maximal-overgroup and Zsigmondy statements**, every eight pairwise-disjoint actual left cosets in `PSU(3,q)` have a pair of original subgroup indices with gcd at least 8. This argument does **not** import Sun7. The exceptional `PSU(3,2)` is outside the claim.

The parent read the full [145-LF candidate](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/sun-coset8/frontier-20261028-psu3-all-fields-v1.md), complete [f65 review](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-review-f65-psu3-all-fields-v1.md), and the operative published statements:

- [Korchmáros–Lia–Timpanella, arXiv:1902.10201v1, §3](https://arxiv.org/html/1902.10201v1): for `q≥3`, `PSU(3,q)` is simple of order `q³(q³+1)(q²−1)/gcd(3,q+1)`.
- [Baumeister–Burness–Guralnick–Tong-Viet, arXiv:2307.13976v2](https://arxiv.org/html/2307.13976v2): Theorem 2, Table B, Remark 9.2 and §2.1. For `G=T=U₃(q)`, the relevant odd defining-characteristic `p` row gives a unique maximal Sylow-p overgroup; the primitive `r₆` row gives one under `β(3,−1)` and its stated `f>1` or prime-field conditions. The source expressly handles `q=3,4,5` with Magma before the displayed general proof; using its q=4 row imports that small-case treatment. Zsigmondy's standard primitive-divisor exceptions are also quoted there.

The source's excluded alternative presentation `G₂(2)'≅U₃(3)` is not an exclusion of U₃(3) from the surviving unitary notation. The exceptional `(q,r)=(3,7)` row is **not** used to satisfy an `r>7` condition. Neither the subgroup classification, its small-case Magma computation, unitary order/simplicity, nor the original Zsigmondy proof is rederived here.

## Reconstruction

**Unique-overgroup lemma.** Let `r>7` divide the order of a finite group, and suppose a fixed Sylow r-subgroup has a unique maximal proper overgroup M of index at least 8. In a supposed Sun8 counterconfiguration, at most one of the eight original indices is divisible by r, because two such indices have gcd≥r. Every other subgroup contains a Sylow r-subgroup; conjugate it to the fixed one, then extend it to a maximal subgroup. Uniqueness forces containment in a conjugate of M, so every such original index is divisible by `[G:M]≥8`. Two already contradict the assumed gcd≤7. No common conjugate, normality, covering or Sun7 assumption is required.

**Proper-index bound.** The imported group is nonabelian simple, so its action on cosets of any proper subgroup is faithful. The order formula gives `|G|≥6048>7!` for q=3 and at least 20800 for q≥4; hence every proper subgroup index is at least 8.

**Extension fields.** For `q=p^f` and `f≥2`, Zsigmondy supplies a prime r with `ord_r(p)=6f`: the `(2,6)` and degree-2 exceptions do not apply. Thus `r≡1 mod 6f`, so `r≥13`; and `ord_r(q)=6`, so `r` divides `q³+1` and the group order. For every odd prime `k|f`, `(q^(1/k))³` cannot be `−1 mod r`, since squaring would make `p^(6f/k)=1 mod r` below the primitive order. This pays the source's complete β condition. The f>1 row gives the unique overgroup, and the two lemmas prove Sun8. In particular q=4 uses r=13 and the source's small-case theorem.

**Prime fields.** For `p≥11`, use the defining-characteristic row with r=p. For p=7, use r=43: `7³≡−1 mod 43` and the order of 7 modulo 43 is 6, β is vacuous, and the source's r>7 alternative applies. The remaining fields q=3,5 have orders `2⁵·3³·7` and `2⁴·3²·5³·7` and no index 2–7. In a counterconfiguration, pairwise gcds lie in [2,7], since coprime-index actual cosets intersect. Among indices divisible by 7, each has a seven-free cofactor >1 and the cofactors are pairwise coprime, so at most three exist. Among seven-free indices, only primes 2,3,5 occur: the complete singleton/mixed-support case split in f65 gives at most four. Thus there are at most seven indices, a contradiction. The all-prime-support proof, not the finite experiment below, covers those endpoints.

## Verification and remaining scope

The f65 review found **0 FATAL / 0 MAJOR / 0 MINOR** at these imports, independently reconstructed the full logic and source conditions, and ran exact checks including primitive-prime controls and q=3/5 divisor graphs. Its first script execution failed on a missing standard-library import; its corrected final execution and actual output are reported in f65, not retroactively represented as an initial pass.

The parent independently enumerated all divisors ≥8 of 6048 and 126000 and computed the maximum pairwise gcd-[2,7] compatibility cliques: respectively **4 among 42 vertices** and **5 among 113 vertices**. These graphs overapproximate subgroup-index possibilities and do not construct actual subgroups or cosets. Separate exact checks confirmed `ord₁₃(2)=12`, `ord₁₃(4)=6` and `ord₄₃(7)=6`. These bounded computations do not prove the all-q classification or Zsigmondy theorem.

This excludes only the named simple unitary family at the explicit source imports. The separate higher-dimensional unitary author candidate is unreviewed; prior held unitary leads are not premises. No complete public/repository priority census has been performed and no new theorem or publication priority is claimed.
