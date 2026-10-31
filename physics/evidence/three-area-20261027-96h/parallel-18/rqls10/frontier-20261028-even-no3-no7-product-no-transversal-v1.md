# Even roots without factors 3 and 7: Fourier-product no transversal

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 20:48:24 PDT 2026**. The result includes q=20,40,50, etc. and is an additive strengthening of `frontier-20261028-fourier-product-root-frontier-v2.md` SHA **59771270a53f6bf1e3155f09a1a5e9e96059341ceccb643f93956356d8b68b7a**. No pinned files were edited.

## 1. Theorem and exact imports

For EVERY even q with 3∤q and 7∤q, EVERY `K∈BH(10,q)` has a Fourier-product QLS10 with **NO orthogonal transversal**, even for repeated rays and arbitrary gauges/permutations. If 5∤q the five-term half-sum is impossible; otherwise the proof reduces any hypothetical transversal to one for a BH(10,10) matrix.

Named inputs: [Lam–Leung, Cor.3.4 and Thm.4.8](https://arxiv.org/pdf/math/9511209v1); the independently replayed q10 no-transversal candidate `frontier-20261028-all-bh10-10-product-no-transversal-v2.md` SHA **a2814fa152a3e0c2e41993a172a1f4320378667be08a202b0dd8a39ed5dd721f**, which explicitly imports the published 51-class BH10,10 classification; and the standard cyclotomic fact that the roots of unity inside `Q(zeta10)` are exactly mu10. No q>10 class catalog is assumed.

## 2. Five- and ten-root sums

At weight5, the named root theorem gives only a 5-gon or a 2-gon plus 3-gon. Since 3∤q, any zero sum of five q-roots is one regular5-gon; hence no such sum exists if 5∤q. For the remainder suppose 5|q and set `G=mu_q/mu5`, which contains a fixed-point-free involution x→−x.

At weight10, every minimal vanishing sum is a regular prime polygon. With at most two prime divisors this is Lam–Leung Cor.3.4; with three or more, 2 and5 are the two smallest and the third is at least11, so Thm.4.8 bounds asymmetric minimal weight by at least `2*(5-1)+11-5=14`. Since 3 and7 are unavailable, the only decompositions of10 are TWO 5-gons or FIVE 2-gons. The former has one G value ten times or two G values five times each. The latter has equal G multiplicities at x and −x.

## 3. A putative matching makes each half quotient-uniform

A physical transversal supplies a perfect matching of K columns whose quotient has zero sum on BOTH five-coordinate parity halves E and E^c. Each matched half sum is a regular5-gon, so all five terms in each half have the same G coset.

For any two coordinate rows in the same half, their G quotient is equal in each matched column pair. Therefore every G multiplicity is even and there are at most five distinct G values. A `5+5` zero-sum profile with two values has odd multiplicities and is impossible. In a five-2-gon profile m(x)=m(−x); because the involution has no fixed point and EVERY m(x) is even, the total number of terms must be divisible by4, contrary to10. Thus any two rows in the SAME half have a CONSTANT G quotient across all columns.

After q-root row/column dephasing, the G-valued rows on E are all1, and the G-valued rows on E^c are a single repeated pattern `(delta_c)`.

## 4. Constructing a genuine BH(10,10) base

Partition columns by delta_c modulo the order-two subgroup `{+1,-1}` of G. Choose a q-root representative lambda_j for each class j. On E every K entry is in mu5; on E^c a column from class j has entries in `lambda_j * mu10`. Define B by leaving E unchanged and dividing all E^c entries in class j by lambda_j. Thus `B∈mu10^(10×10)`.

For columns in the SAME class, their E^c relative phase is unchanged, so their complete B inner product equals the K inner product. For columns in DISTINCT classes, the original quotient terms lie in two G cosets that are neither equal nor antipodal. Such a ten-term zero sum cannot be five antipodal 2-gons, and must be two5-gons, one in each half. Therefore the two half inner products each vanish, and remain zero after the independent lambda changes. B is genuinely `BH(10,10)`; the row property follows from its square column orthogonality.

## 5. The SAME transversal survives the specialization

For any two physical cells in columns c,d with classes j,k, write their unnormalized inner product as

`X + (conj(lambda_j)*lambda_k) Y`,

where X is the E sum and Y is the E^c sum computed from B, both in `F=Q(zeta10)` because B's entries and the physical row phases are 10th roots. If j=k, the coefficient is1, so the K and B inner products coincide. If j!=k, their quotient `rho=conj(lambda_j)*lambda_k` is a root of unity OUTSIDE mu10 by the definition of the classes. Since F contains no other roots of unity, rho is not in F. Thus a vanishing K inner product `X+rho Y=0`, with X,Y∈F, forces X=Y=0. In particular the B inner product `X+Y` also vanishes.

Every pair of cells of the putative K transversal is therefore orthogonal for B: the same combinatorial transversal survives. The imported universal BH10,10 no-transversal certificate contradicts this.

## 6. Consequences and limits

Combined with the all-odd theorem `frontier-20261028-all-odd-fourier-product-no-transversal-v1.md` SHA **d9422ffac608ddd9b128e979dc105b20c6ca94ad06f4a63af4e086a42e6e9490**, and with the general five-root rule (no T if neither5|q nor6|q), any still-unexcluded root order must satisfy **6|q OR 70|q**. q=6 and12 are separately excluded by their exact catalog-conditional certificates. q=18 remains the smallest generally unexcluded order; q=70 is the smallest unexcluded even order not divisible6.

This proof makes no claim about even q with 3|q or with both5|q and7|q, arbitrary continuous phases, non-Fourier products, or the original unrestricted 1-RQLS10. The source root-sum theorem, base construction, specialization and q10 catalog/certificate require independent full review.
