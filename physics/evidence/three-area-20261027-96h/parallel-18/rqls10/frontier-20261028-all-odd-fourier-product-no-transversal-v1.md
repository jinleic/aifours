# Every odd-root Fourier-product QLS10 has no transversal

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 20:45:52 PDT 2026**. This is a strictly stronger additive successor to the odd-q filters and residual class analysis in `frontier-20261028-odd-root-hadamard-reduction-v1.md` SHA **5b14644b2f59f7a108372b3296e65772041b90412b9e95330a4596200989697d**, `frontier-20261028-odd105-quotient-classes-v1.md` SHA **334ad2097c9d11b66fcac1b6843f85591dfdd45d6af8c72cbe8394ebf05eb643**, and `frontier-20261028-odd105-eliminate-442-v1.md` SHA **3615bba5a18cb03c8eefe85062613b92bbb64d83f52dd76ae7a8feade3a5864f**. Their unexcluded odd105 patterns are now ruled out by a different, simpler argument; no existing bytes are changed.

## 1. Result and explicit imports

For EVERY odd positive integer q and EVERY `K in BH(10,q)`, the actual Fourier-product QLS

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`

has **NO orthogonal transversal**, even if rays repeat, for arbitrary K row/column gauges and permutations. This also excludes every 1-resolution in this restricted family.

The proof imports two named inputs:

1. [Lam–Leung, On vanishing sums of roots of unity, Cor.3.4 and Thm.4.8](https://arxiv.org/pdf/math/9511209v1), used exactly as in §2 below.
2. The universal BH(10,5) Fourier-product no-transversal certificate `frontier-20261028-all-bh10-5-product-obstruction-v1.md` SHA **44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678**; this is an exact independently replayed finite candidate, not a prior classification import.

No BH(10,q) classification, root-order bound, general-QS claim, formal proof, human review, or novelty assertion is used or claimed.

## 2. Root-sum facts

Lam–Leung implies every zero sum of at most10 odd-q roots decomposes into regular odd-prime polygons: the asymmetric minimal weight is at least14 when q has at least three odd prime factors, and with at most two factors all minimal sums are symmetric. Thus every FIVE-term zero sum is one regular5-gon, while every TEN-term zero sum is either `5+5` or `3+7`.

If 5 does not divide q, the five-term condition is impossible and the physical half-matching below immediately rules out a transversal. Otherwise put `G=mu_q/mu5`, an odd-order group. A ten-term `5+5` sum has one G value appearing ten times or two G values each appearing five times; call this LOW. A `3+7` sum has at least nine distinct G values: the order3 and order7 subgroups inject into G and their rotated cosets meet in at most one point. Call this HIGH. These conclusions are independent of the size of q.

## 3. The matching forces two uniform row halves

Assume a transversal. Pair its cells at physical row indices r and r+5. Since their column labels are all distinct, these are five disjoint pairs of K columns. K column orthogonality plus orthogonality of the corresponding physical vectors gives zero sums on BOTH coordinate parity halves E and E^c, each of size5.

For any matched pair of K columns c,d, the five ratios `K_(t,c)/K_(t,d)` on E form a regular5-gon and hence all have the SAME G value; the same is true on E^c, possibly a different G value. Therefore, for any two coordinate rows s,t BOTH in E, the G-valued row quotient has equal values in each of the five matched column pairs. The same holds for s,t both in E^c.

Each such ten-column row quotient consequently has AT MOST FIVE distinct G values and EVERY multiplicity even. The two distinct coordinate rows are orthogonal. Their ten-term root sum is LOW or HIGH by §2; HIGH requires at least nine values, while a nonconstant LOW profile has multiplicities5 and5, not even. Thus every row quotient within E is CONSTANT in G across all ten columns, and likewise within E^c.

Dephase using q-root row and column phases. The G-valued matrix now has all entries1 on E, and a single G row pattern `(delta_c)` repeated on E^c. (Row phases first make the five rows in each half identical in G; column phases then dephase the E pattern.) This phase equivalence preserves all Hadamard and physical orthogonality properties.

## 4. Tight-frame parity forces a BH(10,5) matrix

Group the ten columns by their delta value. Any two columns from distinct groups have their ten quotient terms in two distinct G cosets, exactly five per coset. Their zero sum must be LOW, so each half sum vanishes separately. Let `A_i` be the 5×m_i submatrix of E-rows and columns in group i. The spaces col(A_i) are pairwise orthogonal, and Hadamard row orthogonality yields

`sum_i A_i A_i† = 10 I_5`.

Consequently `A_i A_i†=10 P_i`, where P_i projects onto col(A_i). Since each entry has modulus1,

`5*m_i = Tr(A_i A_i†)=10*rank(A_i)`,

so EVERY group size m_i is even. Therefore there are at most five groups.

Now compare an E row to an E^c row. Its G quotient takes the distinct values delta_c with even multiplicities m_i. It has at most five distinct values, so cannot be HIGH. It also cannot have the nonconstant LOW profile 5+5, because every multiplicity is even. Hence it has a single G value: **all delta_c are equal**. A final q-root row phase makes every quotient entry1. Thus K is row/column phase-equivalent to a BH(10,5) matrix.

The q5 certificate excludes a physical transversal for EVERY such matrix. Row phases induce a common coordinate unitary, column phases multiply individual vectors by unit phases, and row/column permutations are accounted for by the universal q5 certificate. These operations preserve transversal orthogonality. Contradiction.

## 5. Exact scope and unresolved work

This is a catalog-free reduction of the entire odd-q Fourier-product transversal problem to the independently replayed finite q5 base certificate, with the explicitly named Lam–Leung root-sum import. It does NOT prove that every odd-q BH(10,q) is BH(10,5)-equivalent without the hypothetical transversal. It does NOT cover even q, arbitrary continuous phases, non-Fourier products, or unrestricted QLS10. In particular q18 remains unresolved as a whole, although specific subfamilies have exact no-T certificates. Full independent review of the root-sum theorem, half-matching and quotient/tight-frame proof, the q5 certificate and the physical symmetry caller is required before adoption.
