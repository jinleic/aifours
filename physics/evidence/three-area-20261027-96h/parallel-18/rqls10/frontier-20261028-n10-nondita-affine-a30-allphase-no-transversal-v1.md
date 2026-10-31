# A non-Diţă two-parameter order10 family has no Fourier transversal at any phase

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:25:47 PDT 2026**. This advances the original order10 Fourier-product search outside the earlier Diţă families; it is not a no-go for arbitrary order10 Hadamards or unrestricted 1RQLS(10).

## 1. Explicit family and claim

Let `w=zeta12=exp(2 pi i/12)` and let a,b be ANY unit complex numbers. Take the literal matrix (A.30) in [Bruzda, *Block-Circulant Complex Hadamard Matrices*, Appendix A.4](https://arxiv.org/html/2204.11727v2#A1):

```text
1  1   1    1    1    1     1      1      1      1
1  1  -i    i    i   -i     w^4    w^4    w^8    w^8
1  1   i   -1   -1    i     w^11   w^11   w^7    w^7
1  i   w^8  w^10 w^7  w^11  a     -a      w^4    w^4
1  i   w^4  w^2  w^11 w^7   w^8    w^8    b     -b
1 -i   w^8  w^4  w^7  w^5   ai    -ai     w      w
1 -i   w^4  w^8  w^11 w     w^5    w^5    bi    -bi
1 -1   1   -1    1   -1     aw^11 -aw^11  bw^7  -bw^7
1 -1  -i   -i    i    i     aw^7  -aw^7   bw^11 -bw^11
1 -1   i    1   -1   -i    -a      a     -b      b
```

The source prose calls the family Y10D while the displayed equation labels it Y10C; the claim is about the literal matrix above. All90 row/column Gram pairs vanish as Laurent identities in unit a,b, independently recomputed below.

**Claim.** For every a,b on the unit circle, every source-row permutation, and any row/column gauges and column permutations, the cyclic Fourier-product QLS built from this matrix has NO orthogonal transversal, regardless of repeated rays. The conclusion includes all special algebraic phases, not just generic phases.

The family genuinely goes beyond both order10 Diţă orientations for generic a,b: exact symbolic row-ratio multiplicities contain no 5+5 row pair, while column ratios contain only pairs (6,7) and (8,9) (zero-based) with 5+5 multiplicities. A 2×5 Diţă matrix requires five disjoint such row pairs, and a 5×2 matrix requires five disjoint such column pairs by the transpose argument. These pair multiplicities are invariant under monomial equivalence. The generic qualifier excludes special phases causing extra ratio coincidences. Its cross-ratio a also gives non-Butson examples, e.g. for transcendental unit a.

## 2. Halfgraph forces both parameters into Q(zeta12)

Suppose a transversal exists. Pair its physical rows r and r+5, producing a perfect matching of its ten selected columns. Column orthogonality of K, together with the Fourier Gram equation at difference5, implies that each matched pair's K-column inner product vanishes separately on the five source coordinates in E and the five in its complement, where E is the set occupying even source coordinates. Every five-subset is possible a priori; because the total inner product is zero, E and its complement give the same halfgraph. Normalize `0 in E`, leaving 126 subsets.

Each possible half-edge inner product is an exact Laurent polynomial in a,b over `F=Q(zeta12)`:

- A nonzero monomial cannot vanish. A binomial whose coefficient norms differ cannot vanish on the unit torus.
- For the remaining binomial edges, an equation `a^u b^v=n/d` has n,d in F and d nonzero. Repeated exponent pairs with incompatible ratios exclude the matching.
- Across all126 E, **116** have no possible perfect matching even before imposing simultaneous phase equations. The remaining 10 have **1152** candidate matchings. Of these, **720** have inconsistent binomial ratios, **288** explicitly force each of a and b into F, and **144** force one into F and, after exact substitution into their sole multinomial edge, yield a two-term Laurent equation with consecutive exponents in the other parameter and both coefficients nonzero. Thus those 144 also force both a,b into F.

Consequently ANY putative transversal forces `a,b in F`. This conclusion uses no assumption that unrelated edge equations can be solved simultaneously; pruning only uses necessary conditions.

## 3. Field obstruction at every surviving phase

The field F is conjugation-stable, and Phi5 is irreducible over F: `F=Q(i,sqrt3)` has quadratic subfields Q(i), Q(sqrt3), Q(sqrt(-3)), while the unique quadratic subfield of the cyclic quartic Q(zeta5) is Q(sqrt5). Hence their intersection is Q.

For any two transversal cells in distinct columns c,d and the same physical-row parity, Fourier orthogonality gives `sum_(u=0)^4 A_u zeta5^(ku)=0` with nonzero k mod5 and

`A_u = conjugate(K_(u,c)) K_(u,d) + conjugate(K_(u+5,c)) K_(u+5,d)`.

Irreducibility forces all five A_u equal. Ordinary K-column orthogonality gives their sum zero, so every A_u=0. Thus, for each fixed source-coordinate pair `(u,u+5)`, the two-component restrictions of any such selected columns are pairwise orthogonal and nonzero. A transversal has five cells in rows of one parity and five distinct columns, impossible in C². This proves the claim for all surviving a,b.

## 4. Exact calculation, independent replay, limits

`frontier-20261028-n10-a30-halfgraph-symbolic-v1.py` SHA **e8c50ef8571237c6d0d2643eb775c95bda16cf6ee95d9194abfa5c0883f92913**, result SHA **b287bad235520a9c3f61a9e7c76a327facc626a170ff6ad6caf7943edbfe75f3**, uses exact Z[zeta12]/(x^4-x²+1), reconstructs all90 symbolic row/column Grams and halfgraph edge types. `frontier-20261028-n10-a30-phase-elimination-v1.py` SHA **123dc2474c156b222bad8f0a5c08a325beaa708b279916f815089c8ec68b2745**, result SHA **5ce40b43d1269ddb4c790365be44262e34e6dc0d512e19c7683e2ab358377abb**, records every 1152 matching, consistency decision and substituted polynomial where applicable.

Independently transcribed `frontier-20261028-n10-a30-phase-independent-v1.py` SHA **0c87ac4e05d552cc162ba20503ef40b8007ce3b7956c619c43cc11327ecd7267**, result SHA **d604ae538273b087701ab9702953a5ca418c491fdd23d49509b8508a81f00251**, uses the distinct integral basis `1,i,sqrt3,i sqrt3`, 252 rather than 126 halves, and explicitly enumerates all945 perfect matchings per half; it obtains 1440/576/288 and no unresolved branch. Literal per-half/per-matching decisions match on all1152 keys in `frontier-20261028-n10-a30-coverage-comparison-v1.py` SHA **eb5e18837bf1b8cf545882f30499439f3c58bd11e58394c3217b016684664a16**, result SHA **a13e34204cbb10af4da9a593c6c0a4bc2fc2f6b1508ae111d79c543716ee705a**. Both programs share the same published matrix and caller idea but use independently transcribed representations and algebra.

The source transcription, halfgraph completeness, Laurent substitutions, field intersection and original-vector correspondence require independent full review. This is not a formal proof, external-model review or novelty finding.
