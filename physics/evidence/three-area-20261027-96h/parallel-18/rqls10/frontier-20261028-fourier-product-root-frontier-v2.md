# Updated Fourier-product root-alphabet frontier

**COMPOSITE AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the last constituent replay: **Wed Oct 28 20:32:13 PDT 2026**. This replaces the conservative q<=17 table in `frontier-20261028-fourier-product-q17-exclusion-v1.md` SHA **33e2b7eb22021056c53c2ed322f38415760a7a73bb66a7648a6ed5174e8252ab**, without modifying it. Every claim concerns ONLY the actual Fourier-product family `psi_(r,c)(t)=zeta10^(r t)K_(t,c)/sqrt(10)` with K Butson, not arbitrary 1-RQLS10.

## 1. All q<=17: no transversal at all

Subject to the cited prior class-completeness and published root-sum imports, for EVERY q<=17 either no `BH(10,q)` exists or its Fourier-product QLS has **NO orthogonal transversal**, even when rays repeat:

- q=1: no Hadamard K.
- q=2,3,4,7,8,9,11,13,14,16,17: no five-root half sum, by the written root-length theorem `frontier-20261028-hadamard-product-root-obstruction-v1.md` SHA **420834dd39bd8e66f18bea3e02ea52b9e1d6e6f00ae8b7310cc974b7f6c51ff5** and/or the named Lam–Leung theorem.
- q=5: universal finite no-transversal certificate `frontier-20261028-all-bh10-5-product-obstruction-v1.md` SHA **44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678**, which does NOT import matrix-classification uniqueness.
- q=6: 34-class source import + full physical-order certificate `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de**.
- q=10: **upgraded from NO MAX to NO T**, including repeated-ray branches, by `frontier-20261028-all-bh10-10-product-no-transversal-v2.md` SHA **a2814fa152a3e0c2e41993a172a1f4320378667be08a202b0dd8a39ed5dd721f** (51-class source import).
- q=12: 577-class source import + complete 475200-order proof `frontier-20261028-all-bh10-12-product-no-transversal-v1.md` SHA **c227f7146ab82709cf860bc9327f9163c6c1e6071e7a111f76556e5035b04ccd**.
- q=15: one-class source import + all252 half graphs lack a matching, independently checked by SHA **9b23c82a87156534a0d35b8530313075898542d3112651a74b811398c9ce3e16**. It is also covered by the odd-q reduction below.

The class counts and equivalence are from [Lampio–Östergård–Szöllősi, Theorem4.1/Table2](https://arxiv.org/html/1707.02287v1) and their [Aalto supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence); that previous classification was NOT regenerated here. The q10/q12 retained root/branch certificates are independently replayed on EVERY stated order and leaf; the named files detail scope and symmetry callers.

## 2. Infinite odd and general-q filters

`frontier-20261028-odd-root-hadamard-reduction-v1.md` SHA **5b14644b2f59f7a108372b3296e65772041b90412b9e95330a4596200989697d** gives a written odd-quotient two-polygon rigidity proof: all BH(2p,p^e), p odd prime, reduce by root phases to BH(2p,p); and, importing Lam–Leung low-weight root-sum classification, any BH(10,q) with odd q, 5|q and 21∤q reduces to BH(10,5). Combined with the q5 no-T certificate and the five-root half-sum rule, it gives

```text
odd q with 105 not dividing q: NO T;
any q with neither 5|q nor 6|q: NO T.
```

The named imported root theorem is [Lam–Leung, Cor.3.4 and Thm.4.8](https://arxiv.org/pdf/math/9511209v1); asymmetric minimal vanishing sums have weight>=6 in general and >=14 for odd q with >=3 prime factors. The actual source and its use require independent review.

Thus a still-unexcluded root order must be EITHER an odd multiple of105 OR an even q divisible by5 or6, excluding the already settled q=6,10,12. The smallest unexcluded order is18. q25,35,45,55, etc. are now covered by the odd-q filter, correcting the older q17 report's deliberately conservative q25 status.

## 3. Exact q18 partial progress and open original problem

Some, but not all, q18 matrices are excluded: `frontier-20261028-q18-multirect-all-no-transversal-v1.md` SHA **46c91c89a696daea81f2a7274a440156058bed64951cc2f6c4dbc26971e71d60** covers compatible BH6 multi-rectangle affine-family specializations at 18th roots. It includes24 explicit NONbinary-gaugeable q18 matrices whose identity-coordinate physical products are independently verified 100-ray QLSs but lack transversals. It does NOT classify all BH(10,18).

All source classifications, written proofs, finite certificates, and physical symmetry callers remain pending independent review. The root filters do not touch arbitrary continuous Hadamard phases, non-Fourier products, other construction families, or general nonproduct 1-RQLSs. The original100-ray 1-RQLS10 still has neither a witness nor an unrestricted impossibility proof here.
