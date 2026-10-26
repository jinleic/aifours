# Operative birth-order refinement of the combined bridge construction

MathSemigroup, math-4. Actual clock returned immediately before creation: **2026-10-23T14:49:57-0700**.

Applies to immutable `coherent-bridge-forest-v1.md`, SHA-256 `62446a4ba2f3b6923aa5ad2253d26d7d1a864b69efa086f8e23ac16dd80af721`. **CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** The original sufficient criterion remains valid. This addendum proves that its two residual graph descriptions are not independent for an actual derivation starting at a path, and constructs a canonical birth-anchor assignment handling some repeated/cyclic loads too. No claim that all loads are handled is made.

## 1. New structural fact: every bridge class has an earliest birth

Keep the occurrence-variable construction exactly as specified in the source. Consider a finite derivation starting at a path, so initially there are no gaps and no bridge variables. Trace variables through the step rules before taking their final equivalence classes.

- M_G creates no new gap origin: every gap on the expanded/contracted side corresponds to a context gap on the other side.
- An LR_P rewrite creates no new origin: every internal formal-block gap has a corresponding occurrence of the same block on the other side, and every possible incompatible boundary pair PZ,ZP,PX,XP,PY,YP occurs on both sides. Newly repeated occurrences are identified with old occurrences by the stated rules. The step may merge previously distinct origins, but introduces none.
- In U→UU, internal copied gaps are identified with old gaps in U, and outer context gaps are transported. If U is a loop no additional gap occurs. If U is a nonloop exactly ONE genuinely new origin is introduced: the between-copy gap beta. Its recorded equation is w beta w=w, where w is the completed OLD word U and hence involves only previously existing origins.
- A contraction removes gap occurrences and introduces no origins.

Thus every final equivalence class of bridge variables contains at least one origin born at a nonloop idempotency expansion. Order those birth steps in the actual finite derivation. For each final class beta, choose its **earliest** origin. The completed load word recorded at that birth, after passage to final variable classes, is denoted A_beta, the birth anchor.

**Birth-anchor proposition.** A_beta contains no beta, and every variable class alpha occurring in A_beta has strictly earlier minimum birth than beta.

**Proof.** At the selected birth, the old U contains only origins born strictly earlier. If one of those old origins were eventually identified with beta, beta's final class would have an earlier origin than the one selected, a contradiction. For every other class alpha containing such an old origin, its minimum birth is at most that old origin's birth, hence strictly earlier than beta's minimum birth. QED.

This proof concerns final equivalence classes, so it does not ignore later LR identifications that merge older bridge occurrences. Taking the MINIMUM birth is exactly what makes those identifications harmless to the ordering argument.

## 2. All designated anchor equations are constructively solvable

Process final bridge classes by increasing minimum birth. Every input of A_beta is already assigned by the proposition. Evaluate it to a_beta in S, and choose

    beta in V_S(a_beta).

The bridge grade is inverse to that of its load, so the chosen mutual inverse has precisely the required absolute-object grade. This satisfies the designated birth constraint

    a_beta beta a_beta=a_beta,
    beta a_beta beta=beta.                        (A)

No outside element, common inverse for a whole grade fibre, global endpoint section or new environment is required. Regularity supplies each inverse inside S. The assignment is finite and explicit up to actual choices of existing mutual inverses.

This does NOT imply that every later equation targeting beta holds. The distinction between a designated birth load and all subsequent loads is the remaining mathematical content.

**Corollary.** If the original occurrence system is single-load after its specified syntactic deduplication, then its full dependency graph is automatically acyclic: its only load for each beta is its birth-anchor word, whose inputs have strictly earlier minimum birth. Therefore the original 'single-load plus acyclic' sufficient condition can, for these actual path-origin derivations, be shortened to single-load.

A directed cycle among the full load words can occur only when a bridge has additional distinct loads beyond its birth anchor. The old disjunction 'multiple loads or cycles' remains logically sound, but these are not independent obstruction counts. **Operatively, do not count cycle-only systems as a separate residual family once the actual birth construction is used.**

## 3. A direct absorption lemma handles some genuinely repeated/cyclic loads

Let beta have grade h^(-1), and let a have grade h, with beta a beta=beta. Let b be ANY element of grade h, even one whose defining expression itself involves beta or other later bridge variables. Purity gives both beta b and b beta idempotent. Then the two elements

    w=a beta b,        w_tilde=b beta a

automatically satisfy their respective inner-inverse equations with the SAME beta.

Indeed,

    (a beta b) beta (a beta b)
       =a beta b (beta a beta) b
       =a beta b beta b
       =a (beta b)^2
       =a beta b,

and

    (b beta a) beta (b beta a)
       =b (beta a beta) b beta a
       =b beta b beta a
       =(b beta)^2 a
       =b beta a.                                (ABS)

This is an actual source algebra identity under the stated purity and mutual-inverse condition, not a formal-band substitution. It permits beta to occur repeatedly inside b; the proof only uses the evaluated b's grade. Acyclicity of those later load expressions is not needed for this absorption once the anchor assignment exists.

## 4. The birth-anchor sufficient condition, covering arbitrary gaps and contexts

For each target class beta retain the formal word A_beta from §1. Suppose every recorded load word w targeting beta, after the specified variable identifications, has ONE of the following literal forms:

1. w=A_beta;
2. w=A_beta beta B;
3. w=B beta A_beta;

where B is a nonempty completed word of the required load grade. This is a syntactic sufficient condition, not an assumed normal form for all source words. It requires no equality oracle in S, no extra source relation and no executable test.

Construct all beta values in birth order using §2. Every constraint of type1 holds by the chosen inverse. Every constraint of type2 or3 holds by (ABS), with a equal to the evaluated anchor and b equal to the evaluated B. B may contain beta or other bridge classes whose values are assigned later; all variables are assigned before this final argument, and only their fixed grades enter the absorption calculation.

Consequently **ALL** recorded INV equations hold. The completed-value proof in the source packet now identifies the actual values of the endpoint paths. This gives a sufficient bridge construction even when the old full dependency graph has self-loops, directed cycles or multiple loads, provided the additional loads have the displayed anchor-absorption form.

The scope still allows arbitrary raw gap counts and arbitrary rewriting contexts. The progress is therefore in the combined R1/R2 mechanism, not another assumption that excursions stay isolated. The earlier finite fork control remains valid: its two independent bridge classes have constant birth anchors and no incompatible additional load.

## 5. Exact combined residual after this refinement

Every actual finite derivation starting at a path has a grade-correct assignment satisfying one designated inverse equation per bridge class. That fact is unconditional within the source hypotheses. The unsolved issue is compatibility with the remaining loads.

A hypothetical canonical collapse of distinct source idempotents must therefore have at least one class beta with a later load not covered by the three literal absorption forms above (or need a different analysis of such loads). Graph cycles produced by those unmatched loads are evidence of this same coherence problem, not a separate proof of nonembeddability.

A complete answer would require proving that such unmatched loads can always be absorbed using the actual local regular-band constraints, or constructing a genuine source-preserving collapse that resists every allowed separating construction. Neither has been done. The criteria can fail on a particular proof diagram even for an embeddable S; failure alone is never an accepted counterexample.

The orthodox/pure group grading remains explicit. Purity is used in the completion proof and in (ABS); the concrete nonpure control in `isolated-excursion-addendum-v1.md` remains operative. No extension to arbitrary nonorthodox Rees grading, no full finite embedding, no kernel verification or novelty claim is inferred.

All original snapshots remain unchanged. This new combined refinement needs actual parent and separate bounded reconstruction before written acceptance. No scientific execution, nested agent or outside-model CLI occurred.
