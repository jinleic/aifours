# Exact straightness boundary for semilattice-by-CS idempotent-separating images

**Status: NEW AUTHOR WRITTEN NECESSITY with exact finite kernel control; source-dependent sufficiency; UNREVIEWED / UNADOPTED.** This concerns a stronger, semilattice-band instance of the natural generalized Fact2 target, not the whole seminormal-band target and not Q1. It upgrades the earlier Dombi-scope note from a one-way inclusion to a proposed exact characterization.

## 1. Statement and named imports

For a regular semigroup S, the following are equivalent:

1. S embeds in an idempotent-separating homomorphic image of a physical Pastijn product `P(L,D)` with L a semilattice and D completely simple.
2. S is straight locally inverse.

**2⇒1 is an external theorem**, stated in Erzsébet Dombi's abstract for *Almost factorisable straight locally inverse semigroups*, Acta Sci. Math. 69 (2003), 569–589: <https://strathprints.strath.ac.uk/43425/>. The article's repository at <https://acta.bibl.u-szeged.hu/15988/> marks the full PDF SZTE-network-restricted. We did not access it or independently reconstruct its proof. We use only the exact abstract statement, and the product convention from the survey <https://arxiv.org/html/1909.05280v1> §5.2.

The forward direction below imports two standard results about locally inverse semigroups and their pseudosemilattices: (Y) every semigroup homomorphism between locally inverse semigroups preserves the binary sandwich operation ∧, stated as Yeh's lemma 2.1 in <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A8E436582D0BBDF2DDE4A7D37DE49F2/S0008439500014090a.pdf/on_the_lattice_of_existence_varieties_of_locally_inverse_semigroups.pdf>; and (ST) a locally inverse semigroup is straight exactly when the maximal subsemilattices of its idempotent pseudosemilattice are disjoint. For the disjoint-maximal-semiltattice structure, see <https://arxiv.org/html/1309.7390v1> §1; for its use as straightness terminology see the preceding 2019 survey §5.2. These source interfaces must be independently checked. The specific ∧ formula and necessity argument are written here, not inferred from a finite test.

## 2. The host idempotent pseudosemilattice

Let `D=M[G;I,Λ;P]`, G act on L by automorphisms, and `H=P(L,D)` with

`(a,(i,g,λ))(b,(j,h,μ))=(a∧(gP_(λj)·b),(i,gP_(λj)h,μ))`.

H is regular. Every local monoid eHe has a semilattice of idempotents, hence is inverse: writing `e=(a,d)` where d is an actor idempotent, `E(eHe)={(b,d):b∈aLa}` with multiplication in L. Thus H is locally inverse. Its idempotents are exactly

`e=(a,d_(iλ))`, where `d_(iλ)=(i,P_(λi)⁻¹,λ)`.

For idempotents `e=(a,d_(iλ))` and `f=(b,d_(jμ))`, their pseudosemilattice operation is

`e∧f = (a∧(P_(μi)⁻¹ P_(μj)·b), d_(iμ))`.       (★)

Here ∧ on the right is semilattice meet in L. To check (★), use the standard characterization `h=e∧f` as the greatest idempotent satisfying `h=e h=h f`, under the natural idempotent order. These two equations force the actor cell `(i,μ)`. Write the band part of h as u. The first equation is `u≤a`, and the second is `u≤P_(μi)⁻¹ P_(μj)·b`. Their greatest common lower bound is exactly the stated meet; the natural order within a fixed actor-idempotent cell is the L order. The same equations also show the displayed element belongs to the required sandwich set.

For `E_(iλ)={(a,d_(iλ)):a∈L}`, (★) restricts to the original semilattice on L. Conversely, if e and f commute under ∧, the actor cells of `e∧f` and `f∧e` are `(i,μ)` and `(j,λ)`, forcing `i=j, λ=μ`. Thus a subsemilattice cannot contain idempotents from two different cells, while every whole cell is a semilattice. The cells are exactly the maximal subsemilattices, so they are pairwise disjoint.

## 3. Idempotent-separating images and regular subsemigroups

Let `π:H→U` be onto and idempotent-separating. U is regular. Every `e∈E(U)` has an idempotent lift e₀ in H: pick x with π(x)=e and an inverse z of x²; then xzx is idempotent and maps to e. Moreover `π:E(e₀He₀)→E(eUe)` is onto: for `f∈E(eUe)` sandwich any preimage by e₀ and apply the same xzx lift in the regular local monoid. It is also injective, so E(eUe) is a semilattice. Hence U is locally inverse.

Every regular subsemigroup S of U is locally inverse as well: each eSe is regular, and its idempotents are a multiplicatively closed subset of the semilattice E(eUe). By the quoted homomorphism lemma (Y), both π and the inclusion S→U preserve ∧. The map `π|E(H)` is bijective by idempotent separation and lifting, hence is an isomorphism of pseudosemilattices. Under that isomorphism, E(S) is a subpseudosemilattice of E(H).

For each host cell E_(iλ), its intersection with E(S) is either empty or a subsemilattice, because the intersection is closed under ∧. No semilattice in E(S) can mix host cells: two elements from different host cells fail to commute by §2. Consequently those nonempty intersections are precisely the maximal subsemilattices of E(S), and they are pairwise disjoint. By the named straightness characterization (ST), S is straight locally inverse. This proves 1⇒2.

The explicit assumption that S is regular matters in the local-inverse and ∧-subalgebra steps. Nothing here says all locally inverse semigroups are straight, nor that an arbitrary seminormal-band product has the same maximal-cell property. A normal or seminormal band factor is not a semilattice in general.

## 4. Exact finite check and limits

The Python eval-kernel script `frontier-20261028-pastijn-semilattice-pseudosemilattice-control-v1.py`, SHA-256 `3daef95e7d4bdfb30b8b022016489ab5626c687aa5d9715cc02ff0b1799ab4c8`, completed before Wed Oct 28 21:25:34 PDT 2026. It uses a four-element Boolean semilattice with nontrivial C₂ atom-swap action and the twisted 8-element C₂ Rees actor. For the resulting 32-element H, it verifies the greatest-sandwich property and formula (★) for all 256 ordered idempotent pairs, and verifies that ∧-commutation holds exactly within the four cells, each a four-element semilattice. These checks are exact integers, finite, same-author, and do not prove the universal statement.

The older note `frontier-20261028-straight-locally-inverse-q2-v1.md`, SHA `61fde8c421f151c0a526c559ba49a7f6df845fbf7ed478410e9d477607226699`, remains unchanged; this candidate adds a separately reviewable forward implication. The 24-element nonorthodox/non-locally-inverse example in `frontier-20261028-q2-product-closure-v1.md`, SHA `9b3cbe5360404898de582cfea279e26fb649f8d7ff8725a01a7b0f5f1d72fdc4`, has a seminormal-band target but is outside this exact semilattice-band target. No general Q2 or Q1 resolution, formal proof, independent proof review, or novelty is claimed.
