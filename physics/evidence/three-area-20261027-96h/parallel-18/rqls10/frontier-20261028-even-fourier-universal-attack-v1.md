# Does an even-order Fourier-product QLS have a transversal?

**WRITTEN AUTHOR CANDIDATE with EXPLICIT PRIMARY-SOURCE IMPORTS; UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:16:47 PDT 2026**. This responds to the source/method question, not a claim of a general even-order theorem. The original order10 unrestricted 1-RQLS target remains open.

## 1. Transversal ⇔ resolution in this family

For ANY order n and ANY complex Hadamard K, put `D=diag(zeta_n^t)` and `psi_(r,c)=D^r k_c`, where the unit columns k_c are the normalized columns of K. If T is a transversal, then shifting every physical row index by k gives a transversal T_k: all corresponding vectors are transformed by the same D^k. As k runs over Z_n these n transversals are disjoint and partition every cell, since T has one cell in each column. Thus a single transversal is equivalent to 1-resolvability **for this Fourier-product family**, even when rays repeat.

After permuting K columns, one may put T on the main diagonal. The condition becomes exactly: the phase matrix K AND its entrywise product with the ordinary Fourier matrix F_n are both complex Hadamards. This is an unrestricted complex-phase matrix-pair formulation, not a root-alphabet assumption.

## 2. All classical Fourier products fail in even order

Suppose n is even and the Fourier-product QLS is classical up to a common unitary and cell phases, i.e. has exactly n rays. Its first row is an ONB and exhausts those rays, so D permutes them. No ray is fixed by D^k for any `1<=k<n`, because every k_c is flat in D's eigenbasis and

`<k_c,D^k k_c>=(1/n)sum_t zeta_n^(k t)=0`.

Hence D acts as a single n-cycle on the n rays. Label these rays by Z_n so the array has symbol `r+a(c)`, where a is a column permutation. A transversal would require c_r and `r+a(c_r)` both permutations. But

`sum_r (r+a(c_r)) = n(n-1) ≡ 0 (mod n)`,

whereas the sum of a permutation of Z_n is `n(n-1)/2 ≡ n/2 (mod n)` for even n. Contradiction. Thus **any even-order counterexample to the proposed universal no-T claim must be nonclassical**; this statement is written and requires no Butson restriction.

## 3. Orders 2,4,6: actual universal no-T theorems

- **n=2:** Every 2×2 quantum Latin square is classical (also follows directly by taking orthogonal complements), so §2 excludes T.
- **n=4:** A transversal gives a resolution by §1. Its transversal labels form a classical QLS orthogonal, in the product-state MOQLS sense, to the Fourier-product QLS. [Ball–Simoens, Theorem11](https://arxiv.org/html/2603.02334v1), proves every pair of 2-MOQLS(4) is classical up to isotopy, so §2 excludes T for **all complex K**. This is an explicitly named primary theorem import.
- **n=6:** The same resolution-to-pair construction would give a pair of (non-entangled) orthogonal QLS(6), but [Ball–Simoens, Theorem6](https://arxiv.org/html/2603.02334v1) proves none exist. Hence T is impossible for **all complex K**. This is not the entangled AME(4,6) problem.

The resolution-to-pair equivalence is also written as [Zhang–Cao Lemma2.2](https://arxiv.org/html/2608.29201v2); the present argument uses only one classical label square. [Zhang–Cao Theorem1.3 and Example2.4](https://arxiv.org/html/2608.29201v2) show that maximal 1-RQLS8 exist in GENERAL, not that they admit the special cyclic Fourier-product representation.

## 4. Odd positive control and the remaining question

For every odd n, take K=F_n. Then `psi_(r,c)` is the Fourier basis ray labelled r+c, and `(r,r)` is a transversal because multiplication by2 is invertible mod n. Thus the general no-T assertion would, if true, genuinely distinguish even from odd order.

The checked primary sources do NOT prove or disprove that arbitrary even n>=8 Fourier-product QLSs have a transversal. In particular neither the existence of general 1-RQLS8 nor a failed search determines the Fourier-product question. A candidate at even n>=8 must be nonclassical, and any actual example would need exact original-vector checks.

A bounded FLOATING discovery run `frontier-20261028-even-fourier-pair-search-v1.py` SHA **68ec4b798a6f9161f634bf661e9b021ef7422b5045efae5cf4e3a0279e93c145**, result SHA **eacc0d4f9c41b8b460cb9e8805afb63ed2a03a0e7113a993797dfc348ebcb8cb**, optimized both Hadamard Gram errors jointly over 8/8/32/8 seeded starts at n=4/6/8/10. Best maximum Gram errors `(K,K∘F)` were approximately `(0.3827,0.3827)`, `(0.2588,0.2588)`, `(0.1566,0.1566)`, `(0.1231,0.1111)` respectively. These are NOT exact matrices, exclusion bounds, exhaustive searches, witnesses, or evidence of a universal theorem. Full checked output and seeds are in the JSON.

## 5. Exact restricted progress and review

For n=10, the all-odd, no3 and no5 written Fourier-product filters together restrict any still-unexcluded root order to multiples30; see `frontier-20261028-fourier-product-root-frontier-v4.md` SHA **27b862f5db447ae2184663c49b158555179882025bbe3716029ed814d1456ea8**. This leaves q30 and arbitrary phases open. The source theorems, shift-to-resolution caller, classical parity argument and numerical limitations require independent review. No universal even-order or unrestricted QLS10 no-go is asserted.
