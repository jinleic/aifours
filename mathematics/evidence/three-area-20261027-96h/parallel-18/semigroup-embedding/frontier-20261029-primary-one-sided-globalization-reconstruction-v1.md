# Literal primary-source globalization support, and the exact local gap

**Status: NEW AUTHOR WRITTEN reconstruction/support, UNREVIEWED / UNADOPTED; NOT a new all-source scientific result.** This expands a known global one-sided theorem rather than pretending to settle the matching LOCAL one-sided source gap.

## 1. Complete primary proof now pinned and read

M. B. Szendrei, *E-unitary R-unipotent semigroups*, Semigroup Forum32(1985),87–96, was accessed through the OPEN EUDML/Göttingen scan archive, <https://eudml.org/doc/134770>. All ten pages87–96 were read in full. The exact source kit is `frontier-20261029-szendrei-1985-public-scan-index-v2.json`, SHA `92eed241f971b13e338bf70d12cb4a13da2d2df35e02c17e3ab3566e37181b2b`, which pins each of ten retained page images by URL/bytes/SHA. Total image bytes7136358; the full297-page volume was NOT downloaded. The source title uses R-unipotent to mean each R-class contains ONE idempotent; for regular semigroups this is equivalent to orthodox with GLOBAL LEFTREGULAR E, not merely locally one-sided.

Theorem2.2(p90) says every E-unitary R-unipotent S embeds in a band-by-group product with band in var(E(S)); the opposite gives the GLOBAL RIGHTREGULAR version. Proposition2.1(i) and Lemma2.3(pp91–94) are reconstructed below. The stronger variety-preserving theorem also uses its leftnormal case, Lemma2.4(pp94–95), and the subvariety classification; these remain named primary-source imports at their exact scopes.

## 2. All-derivation invariant for the global LRB case

The source's Takizawa model(p88–89) has X=E×G, total copies gY of the LEFTREGULAR band Y=E×{1}, a partially defined operation ∘ whose value retains the FIRST factor's G-label, and a G-action permuting copies. The precise imported model axioms are: A1 idempotence; A2 if x∘y and y∘z are defined, both bracketings are defined and equal; A3 if y∘z and x∘(y∘z) are defined then x∘y is defined; A4 Y is the total E-subband; A5 `y≼x iff x∘y=y` is a PARTIAL ORDER and Y is an order ideal; A6 the G-action preserves defined products. Takizawa's realization theorem1.1, rather than its original proof, is imported here.

Let F=X⁺. Quotient by the LRB congruence together with all partial-product relations `x=yz` whenever y∘z=x. Define the evaluation of a word by LEFT-ASSOCIATING its partial product, only when all needed products are defined. The key statement is: EVERY elementary LRB deletion/insertion or partial-product rewrite preserves definedness and the exact value, in BOTH directions, for every defined word.

For an LRB insertion, write p=q x r where the inserted letter x already occurs in the prefix p. If p evaluates, all its prefix evaluations lie in the SAME translated total band gY. Their chain is descending in ≼ because `a∘(a∘b)=a∘b` by A1/A2. Restricted to gY, ≼ is the ordinary natural order of the LRB. Thus `eval(p)≼eval(qx)` and `eval(p)∘eval(qx)=eval(p)`. Also `eval(qx)∘x=eval(qx)` by A1/A2, since qx ends in x. A2 now shows `eval(p)∘x` is defined and equals eval(p). Conversely p x defined implies p defined by left-association. So inserting or deleting an already-used letter leaves the entire evaluation unchanged, including any suffix context. These elementary steps generate the full LRB congruence.

For a partial-product step x=y∘z and a nonempty prefix p with value a, A3 and A2 give `a∘x defined iff (a∘y)∘z defined`, with equality. For an empty prefix this is the given partial-product relation itself. Suffix contexts then preserve equality/definedness. This proves the all-step statement, not just an examination of short derivations.

A derivation identifying letters a,b∈Y therefore consists entirely of defined words with invariant value a, so its final value b equals a. Hence Y embeds in the constructed LRB. The letterwise G-action preserves the generated congruence by A6, so descends to band automorphisms. The Takizawa model `PL(X,Y,G)` maps homomorphically by `(a,g)↦([a],g)` and is injective by Y-injectivity and the retained group coordinate, giving the source's global embedding. This is WRITTEN reasoning with exact primary dependencies, not a machine-checked universal proof.

## 3. The precise obstruction to simply replacing GLOBAL by LOCAL

A5 is load-bearing, not a harmless technical convenience. If a translated band gY contains distinct R-related idempotents a,b, then a∘b=b and b∘a=a. The proposed A5 relation has both b≼a and a≼b, contradicting antisymmetry. Therefore A5 already excludes every nontrivial R-class in Y and encodes GLOBAL LRB behavior. LocallyLRB/LEFTSN bands can contain nontrivial R-classes (the five-band and its opposite do), so the same model/invariant cannot simply be relabelled as their proof. A new preorder-plus-Green-class invariant or a genuinely different model is still needed. No original matchingLEFTSN-L/RIGHTSN-R step has been paid by this source reading.

## 4. A transparent reconstruction of the already-known GLOBALREG-E subclass

For E-unitary regular S with E(S) a GLOBALREG band, let λ,ρ be its least right-inverse and left-inverse congruences. Named primary import: Petrich, *Onesided inverses for semigroups*(2006), theorem7.5(pp16–17), says λ∩ρ is the least regular-orthodox congruence. Therefore λ∩ρ=0 here. Both are generated by idempotent pairs and lie in the pure group kernel σ. Hence S/λ and S/ρ inherit pure group quotients, remain E-unitary, and have GLOBAL RRB/LRB E-bands respectively (right-inverse=L-unipotent; left-inverse=R-unipotent). The diagonal S→S/λ×S/ρ is injective.

Apply the source's theorem2.2 and its dual to these quotients, then take the product hosts. Their band product is GLOBALREG and belongs to var(E(S)), because idempotents lift through regular quotients and both factor E-bands are homomorphic images of E(S). A group-product actor suffices; no unverified SAME-ACTUAL-q assertion is needed for this existence proof. This recovers a known subclass already imported earlier, not a new solution or novelty. The public Petrich PDF is `frontier-20261029-petrich-2006-one-sided-public-source.pdf`, SHA `0514fe1fe0239bcc06965713b0976d8573594ae1a7c360b66db206463b57ab09`.

The actual remaining problem is the genuinely nonorthodox LOCAL one-sided extension/globalization, not the global theorem reproduced here. All ordinary structural/model imports and the new exposition remain subject to disjoint review; no independent/Lean/formal or originalQ1/Q2 acceptance is asserted.
