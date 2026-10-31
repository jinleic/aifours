# A non-affine T8B exceptional grid: no order-eight Fourier transversal

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:27:24 PDT 2026**. This checks an algebraically dependent part of the non-affine [Valtonen T8B family](https://arxiv.org/html/2505.22947v1), outside the generic algebraic-independence theorem. It is not a no-go for arbitrary parameters or general even orders.

## Claim and tested parameter domain

Take the source's exact `T8B(a,b,c,d)` matrix with `a,b,c` any eighth roots and

`d=(1+ab+ac+bc)/(a+b+c+abc)`

when its denominator is nonzero. Of 512 triples, **42** have zero denominator and are EXCLUDED from this claim; the other **470** give exact Hadamards. For ALL470 points, their ordinary Fourier-product QLS8 has **NO orthogonal transversal**, under any source-row ordering, arbitrary row/column phases and column permutations, and with no ray-cardinality assumption.

Among these470, **64** have d not in mu8. Since d∈Q(zeta8), whose only roots of unity are mu8, d is not any root of unity; the dephased matrix has cross-ratio `-d`, so these points are genuinely outside every finite Butson monomial class. The remaining406 have d∈mu8. Some points may be monomially equivalent; 64 counts parameter triples, not inequivalent matrices.

## Exact search and replay

For unit a,b,c set `N=1+ab+ac+bc`, `D=a+b+c+abc`. The source relation gives `N=abc*conj(D)`, hence D≠0 also N≠0 and d is unit. Each K column-product half sum is computed after multiplication by nonzero ND, using `D²`, `ND`, or `N²` according as its d-exponent difference is −1,0,1. Thus all Gram zero tests are exact in Z[zeta8], with no numeric threshold or assumption that d is a root.

`frontier-20261028-t8b-eighth-phase-counterexample-v1.cpp` SHA **afbeffc8783aaf7ac5773c9ff2319234901861a02dbbfb458c7c126ee613218e**, result SHA **fa52e9cc3e337aad4ba38011810e9074034ff99d04fad840691d38b30bbbac8b**, checks source column Gram zero, all **16450** normalized halfgraphs, and the **10050** with perfect matchings. Each normalized half has144 physical orders: **1447200** orders, with complete MRV search of **1746336** nodes, no T. The caller is the same exact r/r+4 half-matching necessity and coordinate/physical-row normalization spelled out in `frontier-20261028-n8-bh16-counterexample-scan-v1.md` SHA **1bcd402fb3dc2873de1d2c19778d9522bc88c86362bc561592fd71f21a7c9560**.

Independent `frontier-20261028-t8b-eighth-phase-replay-v1.cpp` SHA **538bfa2c9e10982b76de72277a182cf99449ea6aa58256a2206cb88b90eff513**, result SHA **cfbf6c074bfa05dba57430d715a894f4d27e59891bc28d105c766b1dafa204ea**, reconstructs K as a common nonzero multiple `4D*K` in the distinct integer basis `1,i,sqrt2,i sqrt2`, validates its column Grams, independently counts64 nonroot d values, uses subset-DP matching and fixed-row DFS, and repeats the same470/42/16450/10050/1447200 counts with **2073888** DFS nodes and no T. These are full re-executions, not retained per-order proof certificates; they share the source transcription and symmetry theorem.

The source formulas, 42-point exclusion, field-root claim, symmetry caller and both code paths need independent full review. Other T8B parameters (including denominator-zero limits), other non-affine families, arbitrary K, and unrestricted 1-RQLS10 remain open.
