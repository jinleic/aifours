# A universal Rees-group presentation for the least CS quotient

**Status: NEW AUTHOR WRITTEN GENERAL CONSTRUCTION; UNREVIEWED / UNADOPTED.** This constructs the least completely simple quotient of ANY regular semigroup, without assuming weak E-unitarity, local-r, or that the syntactic quotient is CS. It does not prove a physical band host exists or settle original SEP/R/L.

## 1. Source row/column partitions and group presentation

Let S be a nonempty regular semigroup. Let R be the least equivalence relation containing `(s,st)` for all s,t, and C the least equivalence containing `(t,st)`. Choose base classes R₀∈R, C₀∈C. Introduce group generators `x_s` for s∈S and `p_(C,R)` for each C,R, with normalization relations

`p_(C₀,R)=1=p_(C,R₀)` for every C,R,

and source relations

`x_(st)=x_s p_(C_s,R_t) x_t` for every s,t∈S.            (1)

Let G be the group defined by this presentation, P its matrix of represented p-elements, and `D=M[G;R,C;P]`. Define

`η:S→D`, `η(s)=(R_s,x_s,C_s)`.

**Theorem.** η is onto, and is the universal onto CS quotient of S: every homomorphism from S into any CS semigroup factors uniquely through η. Consequently `kerη` is the least CS congruence ν, and this construction realizes the abstract quotient from `frontier-20261028-least-cs-congruence-v1.md`, SHA `c0d26221b553b74f9a420806b6b0463cfcccccc9b9cfb2eacdfed5c13180d1a8`.

## 2. Full onto-ness

Equation (1) and `R_(st)=R_s`, `C_(st)=C_t` make η a homomorphism. Its image U is regular because S is regular, hence CS as a regular subsemigroup of the CS semigroup D. This standard argument is explicitly proved in the cited least-CS note and uses Green-preorder inheritance plus Rees–Suschkewitsch. U occupies every source R-row and every C-column. By closure under products it occupies each cross-cell. Its H-cells are group subsemigroups with the corresponding ambient cell identities.

The normalized matrix therefore gives in U the idempotents

`E_R=(R,1,C₀)`, `F_C=(R₀,1,C)`, and `e₀=(R₀,1,C₀)`.

For every source s, `e₀η(s)e₀=(R₀,x_s,C₀)` belongs to the base subgroup `H_U=U∩({R₀}×G×{C₀})`. For every matrix generator, `F_C E_R=(R₀,p_(C,R),C₀)` also belongs to H_U. Hence H_U contains every generator of G and, being a subgroup, equals G. Now `E_R (R₀,g,C₀) F_C=(R,g,C)` belongs to U for every R,C,g. Thus U=D, proving full surjectivity even for infinite S or G.

The word 'group' in the H-cell assertion is justified: U is CS by the regular-subsemigroup argument, and its Green R,L classes are inherited from D, so each occupied ambient cell is exactly an H-class group of U with the same ambient identity. No unsupported statement about arbitrary nonregular subsemigroups is used.

## 3. Universal factorization

Let `r:S→T` be a homomorphism to any CS semigroup T. Its image is regular and hence CS; replace T by that image. Actor rows of r(st) are those of r(s), and columns those of r(t), so r induces onto row and column maps `ρ:R→I_T`, `κ:C→Λ_T`. Normalize the Rees representation of T at the base row ρ(R₀), column κ(C₀); write its group H and matrix Q with that row and column all1. Write `r(s)=(ρ(R_s),g_s,κ(C_s))`.

Assign `x_s↦g_s` and `p_(C,R)↦Q_(κ(C),ρ(R))`. These assignments satisfy normalization and (1), because r is a semigroup homomorphism. They induce a group homomorphism `φ:G→H`. The Rees map

`h(R,g,C)=(ρ(R),φ(g),κ(C))`

is a homomorphism by the assigned sandwich entries, and `r=hη`. Since η is onto, h is unique. Reinsert the image inclusion into the original target if necessary. This proves the theorem. □

## 4. Finiteness and purity boundaries

If S is finite, η onto implies `|R||G||C|≤|S|`; in particular G is finite. The presentation has |S|+|R||C| group generators and at most |S|²+|R|+|C| normalization/source equations (some repeated), but finite presentation size does NOT by itself give an efficient algorithm. A finite quotient/congruence search on S is one independent terminating way to compute ν; the presentation theorem is not a license to assume an unknown group word problem has been solved.

η is pure exactly when the actual idempotence-context quotient S/τ is CS, by the least-CS note. In that case the universal group presentation agrees up to S-compatible isomorphism with the explicit finest pure actor built using q's group. Without that condition the universal quotient still exists but need not be pure. For example, in the four-element monoid table recorded in `frontier-20261028-natural-order-weu-audit-erratum-v1.md`, SHA `801f699bb640bd1e58eed095779c05b882e7d9eddd0ea1c470b522ecbc345c28`, R,C are singleton, the left-zero relation `0·2=0` forces x₂=1 in every group quotient, and the whole least CS quotient is trivial; it is not pure. That monoid is NOT weakly E-unitary.

The construction is a universal actor only. It does not build a band-valued cocycle, prove any same-actor idempotent separation, identify original printed conventions, or establish novelty. All source/Rees arguments remain same-author candidates pending disjoint proof review.
