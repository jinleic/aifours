# A Fourier-product transversal forces sqrt(5) into the Hadamard field

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:05:59 PDT 2026**. This is an additive field-theoretic consequence of `frontier-20261028-no5-field-product-no-transversal-v1.md` SHA **69849d0dad81748b50771dea667176fb3818aa54fb728268340d2fbff064fc36**; it is not an unrestricted QLS10 theorem or a novelty claim.

## 1. Necessary field inclusion

Let K be any order10 complex Hadamard, with no assumption on its phases. If its Fourier-product QLS contains three pairwise-orthogonal cells in distinct same-parity rows and distinct columns, then the conjugation-stable field

`F=Q( all K_(t,c), all conjugate(K_(t,c)) )`

MUST contain `sqrt(5)`. The same necessary condition holds if there is a transversal.

**Proof.** The predecessor proves that such three cells cannot exist if Phi5 is irreducible over F. For a characteristic-zero field F, Phi5 is reducible over F if and only if `sqrt(5)∈F`: if sqrt5 is in F, it factors into the two familiar real quadratic factors. Conversely, F(zeta5)/F is a Galois extension whose group is a subgroup of cyclic `(Z/5Z)^×` of order4. Reducibility makes this subgroup proper, so it is contained in its unique subgroup of order2. That subgroup fixes `zeta5+zeta5^(-1)=(sqrt5-1)/2`, which consequently lies in F. This proves the inclusion.

If K has algebraic entries, F is a number field, so a transversal requires `[F:Q]` even and the rational prime5 to ramify in F: 5 ramifies in Q(sqrt5), and ramification indices multiply up the tower. This is a necessary condition only.

## 2. Continuous families and genuine generic exclusion

Let E be a conjugation-stable number field not containing sqrt5. Let `K(z1,...,zm)` be a Fourier-product input complex Hadamard for the parameter tuples in some open subset of the m-torus, with every matrix entry a rational function over E in the unit phases z_j (and hence their inverses); exclude poles. For any tuple whose z_j are algebraically independent over E, the evaluated entries and their conjugates lie in `E(z1,...,zm)`, which has no new algebraic constants, in particular no sqrt5. By §1 there is NO transversal at that tuple.

Because E is countable, the algebraically dependent tuples form a countable union of proper Laurent-polynomial zero sets and have Haar measure zero in the torus. Thus the family has no Fourier-product transversal for Haar-almost-every parameter tuple. This conclusion is independent of any base-point no-T certificate and applies to arbitrary rational-in-phase families with the stated coefficient field, not only to rectangle deformations. It does NOT exclude dependent/algebraic parameter tuples.

For m=1, the assertion is pointwise: any transversal parameter z must be algebraic over E, must make `sqrt5∈E(z)`, and thus must satisfy `[E(z):E]` even. Transcendental unit phases and algebraic phases of odd extension degree over E are excluded. The q30 phase can have an even extension and remains unresolved.

## 3. Scope

The arguments are written algebra and standard field/Galois facts, with no catalog or finite search input. They show a necessary field feature and generic-family exclusion; they do not prove impossibility over fields containing sqrt5, classify exceptional parameter tuples, or address non-Fourier products. Independent full review is required.
