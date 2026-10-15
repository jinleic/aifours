# Local openai/math references: techniques and boundaries

Date: 2026-10-14 (PT). The local `math/` tree was inspected read-only. No new theorem from that repository was assumed to solve P1, and the mathematical source tree and its build outputs were not changed.

## References inspected beyond topic labels

1. `math/lean/OAI/Algebra/Universal/Congruence.lean`
   - `OAI.FiniteCongruence.Congruence.principal` (lines 80–88) defines the generated congruence as intersection over all compatible setoids containing a pair.
   - `principal_le` (93–99) proves containment by evaluating this universal condition, not by assuming the quotient property.
   - `relation_map_of_updates` (109–135) and `compatible_iff_translations` (154–163) prove compatibility by changing one input at a time. For a binary semigroup operation, these are exactly the left/right translation closure tests.
   - **Transfer:** this is an appropriate general formalization pattern for a generated `ξ` relation and for proving `ξ ⊆ ker q` once an actual completely simple quotient has been built. The independent written `xi-purity.md` instead builds the quotient explicitly by equal rows/columns and proves multiplication directly, so the nontrivial work is not hidden in a general congruence axiom.
   - **Boundary:** the module contains no completely-simple-semigroup structure, local-orthodoxy hypothesis, or idempotent-purity theorem. Its finite signature is not finiteness of the carrier. No OAI import is needed for the coordinate proof.

2. `math/lean/OAI/Algebra/OddKaplansky/WreathFourier.lean`
   - `OAI.OddKaplansky.WreathFourier.shift` (39–44) supplies a multiplication-preserving equivalence on functions: `(shift h a)(x)=a(h⁻¹x)`; inverse is substitution by `hx`.
   - `shift_mul` (57–64) proves the action law by `funext` and the group associativity identity.
   - `base_injective`, `top_injective` (88–99) recover elements through product coordinates with `congrArg`; `normal_form` (108–114) checks the two coordinates separately.
   - **Transfer:** use actual function reindexing, prove its action law, then prove an embedding by recovering both coordinates. This is the relevant mechanism in the dossier's derived-category/wreath criterion, not just the word “wreath” in a title.
   - **Boundary:** the OAI base here is a finite cyclic **group**, not a band; later results involve fields, roots of unity and a finite group. The inverse-left-translation convention is not silently equated with the dossier's right-translation convention `(^h f)(g)=f(gh)`.

3. `math/lean/OAI/Algebra/OddKaplansky/Cellular.lean`
   - `OAI.OddKaplansky.Cellular.rightShift` and `shift` (12–19) use exactly the dossier's right-shift orientation: `x(g*u)`. The monoid-homomorphism proof expands both sides pointwise and uses `mul_assoc`.
   - `operator_injective` (36–39) recovers coefficients by applying an operator to a concrete indicator and evaluating at the identity.
   - **Transfer:** confirms the group-action orientation and the principle that a faithful construction needs an explicit recovery test. Replacing the field-valued function space by band-valued functions removes linearity but not the underlying reindexing argument.
   - **Boundary:** the module is about linear cellular operators and group rings. Its inverse/surjectivity conclusions are not regular-semigroup embedding theorems.

4. `math/lean/OAI/Algebra/OddKaplansky/WreathMultiply.lean`
   - `topElt_mul` (18–26) and `normal_mul` (43–55) establish multiplication by expanding and regrouping actual factors.
   - `rho_injective` (72–77) uses normal-coordinate recovery rather than a field postulating faithfulness.
   - **Transfer:** coordinatewise homomorphism/injectivity proof organization. This is a proof-engineering reference, not a theorem dependency for P1.

5. `math/lean/OAI/Algebra/OddKaplansky/WreathActions.lean`
   - `top_represents` (22–40) verifies both left and right actions with explicit reindexing. `conjugate_represents` (68–71) composes the proved representations.
   - **Boundary:** these are matrix representations with finite-group and field hypotheses; no passage to arbitrary bands is provided.

6. `math/lean/OAI/Algebra/OrderedStates/Semigroup.lean`
   - The read sections include `nsmul_compression_iterate` (26–36), `nsmul_unit_order_iff` (57–65), and `cyclicUnitState` (89–102).
   - **Not applicable:** they concern ordered additive **commutative** monoids, positive multiples and real-valued states. The book's noncommutative band identities and natural order are different. A filename containing “Semigroup” does not establish relevance.

7. `math/lean/docs/134.md` and its `OAI/Computability/StarHeight/` module inventory
   - The scoped theorem is a uniform generalized-regular-expression star-height bound. No source-level band/completely-simple embedding theorem was identified in this route. This was a secondary exclusion screen, not a claim that every possible relevant technique in the entire corpus has been exhausted.

## Actual dependencies and trust

The exact imports of the accepted new Lean sources, their `#print` statements and observed transitive axioms are recorded in the delivered `claims.json`, `verification/formal.log`, and source-hash receipts. The OAI references above are technique references only unless explicitly listed there as imports. Reading an OAI proof is not the same as compiling it, replaying its Comparator challenge, or endorsing a different family theorem.

No Comparator fresh-kernel replay or external nanoda validation is claimed for this dossier. The parent owns independent acceptance of the delivered sources.
