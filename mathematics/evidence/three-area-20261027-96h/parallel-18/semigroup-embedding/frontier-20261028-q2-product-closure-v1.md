# Finite-product closure of the natural seminormal-by-CS image target

**Status: NEW AUTHOR WRITTEN, with a finite WRITTEN-checked-in-kernel control; unreviewed/unadopted.** The closure theorem below is direct and does not import Hartmann or Dombi. The consequences for particular source classes import those results at the explicitly qualified scopes cited at the end.

## 1. Closure theorem

Define Q(S) to mean: S embeds in U, where `π:P(B,D)→U` is an onto idempotent-separating homomorphism, B is a seminormal band, and D is completely simple. This is one specific natural generalized Fact2 target, not a claim about the uniquely intended meaning of printed Q2.

**Theorem.** If `Q(S₁),...,Q(Sₙ)` for finite n≥1, then Q holds for every subsemigroup of their direct product. In particular it holds for every regular subsemigroup, the domain of the original Q2 formulation.

Proof for two factors, iterated finitely: choose `H_k=P(B_k,D_k)` and idempotent-separating surjections `π_k:H_k→U_k` with embeddings `S_k→U_k`. Let `D_k=M[G_k;I_k,Λ_k;P^k]`. Their direct product is a Rees completely simple semigroup over `G₁×G₂`, with row set `I₁×I₂`, column set `Λ₁×Λ₂`, and sandwich matrix entry `(P¹_(λ₁,i₁),P²_(λ₂,i₂))`. Let `B=B₁×B₂`, which is seminormal because it is a direct product in the SN variety; let `G₁×G₂` act coordinatewise. Regrouping coordinates gives a literal isomorphism

`P(B₁,D₁)×P(B₂,D₂) ≅ P(B₁×B₂,D₁×D₂)`.

The product homomorphism `π₁×π₂` is onto and idempotent-separating: an idempotent of `H₁×H₂` is precisely a pair of idempotents, so equality of its component images forces equality of both components. The product of the given embeddings embeds `S₁×S₂` in `U₁×U₂`; restriction embeds each subsemigroup. This proves Q, with no assumption that the subsemigroup is regular and without any extension-of-congruences step. □

This does not assert closure under arbitrary homomorphic images, or extension of an idempotent-separating congruence from a subsemigroup to its ambient product.

## 2. A strict expansion beyond the orthodox/straight-locally-inverse union

Let A be the three-element monoid obtained by adjoining 1 to a two-element right-zero band `{a,b}`. Multiplication is `xy=y` whenever y is a or b, and `x1=x`. A is a seminormal band: a word evaluates to its rightmost nonidentity letter, and the two sides of `xyzux=xyzx zux` have the same rightmost nonidentity choice. Its full corner at 1 has noncommuting idempotents `ab=b` and `ba=a`, so A is not locally inverse.

Let D be the explicit 8-element nonorthodox completely simple semigroup in `frontier-20261028-straight-locally-inverse-q2-v1.md`, SHA `61fde8c421f151c0a526c559ba49a7f6df845fbf7ed478410e9d477607226699`. It is straight locally inverse. The 24-element semigroup `S=A×D` is regular; it is nonorthodox because E(D) is not closed, and it is not locally inverse since the corner at `(1,e₀₀)` contains the noncommuting idempotents `(a,e₀₀)` and `(b,e₀₀)`. Consequently S lies outside both the orthodox class and the straight locally inverse class, but Q(S) holds even directly: use B=A and actor D with the trivial group action, and take the identity quotient. Thus finite-product closure of the union is **strictly** larger than the union, already on this simple example. This example is not an obstruction or an unresolved case.

The exact Python-kernel checker `frontier-20261028-q2-product-outside-union-control-v1.py`, SHA-256 `b6f40e63737d5dc1193c4af4f8eed916ba08119c287dded6a8de7da721b2b010`, completed before Wed Oct 28 21:17:46 PDT 2026. It used only integer operations and checked all 13,824 associativity triples, all 81 seminormal substitutions in A, 12 idempotents, an inverse for each S-element, nonclosure of E(S), and two noncommuting idempotents in the displayed local corner. Its result is finite evidence, not an independent general proof.

## 3. Implication and limit

The Dombi source-backed inclusion of straight locally inverse S is recorded in the cited predecessor; its full source proof was not read. The separate Hartmann-source-dependent proposed inclusion of orthodox locally-r S is `frontier-20261028-orthodox-q2-band-variety-characterization-v1.md`, SHA `3ce438c1814af2211eb0f5927730bf27c32fe1c6c76038c5c14a7751caf7e375`, and additionally depends on the unreviewed equivalence local-regular band = seminormal band. Conditional on those inputs, the regular subsemigroups of all finite products of members of those two classes form a strictly larger explicit positive Q2 subclass.

This theorem does not settle whether every locally r-orthodox regular semigroup belongs to the Q2 target, and does not solve the original weakly-E-unitary embedding Q1. The original nonorthodox cases remain open outside the actual positive families and conditional source inputs. No cross-vendor or formal proof review is claimed.
