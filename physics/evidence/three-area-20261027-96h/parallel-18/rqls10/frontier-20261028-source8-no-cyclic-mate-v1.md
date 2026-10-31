# The published QLS8 has no cyclic-Latin orthogonal mate

**EXACT FINITE AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:27:08 PDT 2026**. This strengthens `frontier-20261028-source8-not-cyclic-fourier-v1.md` SHA **01c7d44bdd9922c858b1e60aaa5d3a5d91755b8c506a391e1d7f7182efc1cfbb** for the SAME published example only. It is NOT a no-go for all 1-RQLS8s, even-order Fourier products or order10.

## Result and exact evidence

The actual maximal 1-RQLS8 in [Zhang–Cao Example2.4](https://arxiv.org/html/2608.29201v2#S2.Thmtheorem4) has exactly **16** orthogonal transversals. Viewed as permutations `row -> column`, these 16 permutations form a subgroup of S8 of order16 with element-order distribution

```text
order1: 1; order2: 11; order4: 4; order8: 0.
```

Consequently it has NO 1-resolution whose classical label square is isotopic to the cyclic Latin square Z8. In particular it is not necessary even to assume cyclic Fourier covariance to reject this one example as a cyclic-Fourier counterexample. The same conclusion holds after transposing the array, since the transversal permutation set is a group and hence closed under inverses.

Exact all-transversal enumerator `frontier-20261028-source8-cyclic-resolution-v1.py` SHA **e8427751c5f64be096bfc813cb14b1433f0d01ac42455c44d442a4ce5f18d02b** uses the pinned Q(zeta8) original-vector parser and checks all column choices with exact Gram zero. Its JSON SHA **0e2f088f08144bae4a52388084c4e8fb0f98177e89ea24f3aa605c1b37212bf8** supplies the entire list of16 row-to-column permutations. It also directly tests all5040 8-cycles and every listed transversal, with80640 first-shift membership tests and no cyclic resolution.

The independent finite group-property caller `frontier-20261028-source8-transversal-group-v1.py` SHA **f1852fb1088fbe993bb3a0eb81271d5cce0682b1a33933592e1d058de81be195**, result SHA **8c7121484ca1db1771b492ac8302be874de6eef994b40b6b85100c9f4af91f14**, reads that exact list, checks all256 compositions for closure, and reports the element orders above. This is a check of the same enumerated list, not an independent regeneration of the original source vectors.

## Why this excludes a cyclic label square

Any resolution isotopic to the cyclic Latin square has the form `T_k=S^k T_0`, where S is one 8-cycle on rows, acting while columns stay fixed. Conversely any such orbit of eight transversals gives a cyclic label square. If T_0 and S T_0 are the row-to-column permutations t,t', then `S=(t')^(-1) t`. Since the source example's COMPLETE set of transversals is a group, S would lie in that group, but it has no element of order8. This rules out the resolution, invariantly under global row and column relabelling.

The primary 64-vector source, exact Gram arithmetic, exhaustive enumeration and finite group caller all need independent full review. The result leaves OTHER order8 arrays, arbitrary cyclic quantum mates and the universal even-order Fourier-product question open.
