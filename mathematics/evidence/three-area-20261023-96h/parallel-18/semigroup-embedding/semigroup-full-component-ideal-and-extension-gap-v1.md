# The canonical FULL-CS ideal: a genuine positive region inside every finite CR source

MathSemigroup-2, original math-4. Actual `/bin/date` before writing: **Mon Oct 26 09:40:03 PDT 2026**. AUTHOR-WRITTEN / UNREVIEWED / novelty unresolved. Conventional all-variable proof after explicit prospective v56 permission. No scientific computation or source edit. All prior process and cadence findings remain.

## 1. Hypotheses and exact purpose

Let S be completely regular with its classical semilattice decomposition S=(Y;S_alpha) into completely simple components. Let an actual pure onto q:S→C=M[G;I,Lambda;P] be supplied. For an idempotent e, call H_e FULL if q(H_e)=H_(q(e)), the WHOLE corresponding maximal subgroup of the ACTUAL ambient C. This is relative to C, not merely to the possibly smaller completely simple subsemigroup q(S_alpha).

The first results below need neither local orthodoxy nor local band regularity. For the final embedding application impose the ORIGINAL local r-orthodoxy condition and use the two new complete full-Rees manuscripts as named AUTHOR-WRITTEN inputs:

- Theorem F: `semigroup-full-Rees-CR-local-left-host-v1.md`, SHA256 `32411a8b81b5be9b70e073742b44c1d464a152473347139aa8b5fb9ffa447514`, all145LF.
- Theorem F2: `semigroup-full-Rees-CR-two-sided-embedding-v1.md`, SHA256 `ab87773b6640628eecdf21dee11c191ffd74c6e29d507acdf968bb2eda404ab5`, all109LF.

This application does not adopt either input. The new structural content is that fullness is an entire-component property and propagates DOWN the J-semilattice, yielding an actual canonical ideal rather than an assumed family of separating quotients.

## 2. Fullness propagates within one completely simple component

**Lemma C1.** If q(H_p) is FULL for one idempotent p in a source completely simple component T, then q(H_f) is FULL for EVERY f∈E(T).

*Proof.* In a completely simple semigroup the local monoid fTf is its maximal group H_f. Hence f H_p f⊆H_f. Its image contains

`q(f) H_(q(p)) q(f)`.

This set is the ENTIRE ambient H_(q(f)). To see this explicitly, write q(p)=(i,a,lambda) and q(f)=(j,b,mu), their idempotent coordinates being a=p_(lambda,i)^-1,b=p_(mu,j)^-1. As the middle coordinate g of (i,g,lambda) ranges over all G, the middle coordinate of q(f)(i,g,lambda)q(f) is

`b p_(mu,i) g p_(lambda,j) b`.

Both side factors are fixed invertible group elements, so these products range over ALL G with row j and column mu, precisely H_(q(f)). Conversely q(H_f) is contained in that local group. Thus it is equal. No injectivity or purity is needed for this implication. ∎

So 'the component S_alpha is FULL' unambiguously means that one, equivalently EVERY, one of its maximal subgroups has full image in C.

## 3. Fullness propagates to every lower component

**Lemma C2.** If S_alpha is FULL and gamma≤alpha, then S_gamma is FULL.

*Proof.* Choose e∈E(S_alpha), let T=S_gamma, and consider the nonempty subset X=eTe. Products remain in T by the semilattice multiplication law. Every q(x) for x∈X lies in the ambient GROUP q(e)Cq(e)=H_(q(e)). Also X H_e⊆X: for x=ete and h∈H_e,

`x h=e(t e h)e`,

because he=h; the inner t e h lies in T. Therefore q(X) H_(q(e))⊆q(X), since q(H_e) is FULL. A nonempty subset of a group stable under right multiplication by EVERY group element is the entire group: choose one a in that subset and, for any desired y, multiply a by a^-1y. Hence q(X)=H_(q(e)).

Take any x_0∈X and set p=x_0^0, its maximal-group identity in the COMPLETELY SIMPLE T. The identity p also lies in eSe: from e x_0=x_0=x_0 e, multiplying by x_0^-1 gives ep=p=pe. Consequently q(p)=q(e), because q(p) is an idempotent in H_(q(e)).

For any y∈H_(q(e)), choose x∈X with q(x)=y. Then p x p∈pTp=H_p and q(pxp)=q(e)yq(e)=y. Thus H_p is FULL relative to C. Lemma C1 now gives fullness of EVERY H_f in T. This proves C2 for arbitrary gamma≤alpha, without a finiteness or covering-chain assumption. ∎

This is NOT an assertion that all components are full: it gives a downward implication only. Nonfull upper components can survive above a full lower component.

## 4. The actual ideal and its actor

Define the subset

`Y_full={alpha∈Y:S_alpha is FULL}`, `S_full=union_(alpha∈Y_full) S_alpha`.

By C2, Y_full is a downward-closed subset of Y. Hence S_full, when nonempty, is an ACTUAL two-sided ideal of S: multiplying a full-component element in S_alpha by an arbitrary element of S_beta puts the product in S_(alpha∧beta), which is full. It is completely regular and q restricted to it is pure.

Because q:S→C is onto, q(S_full) is an ideal of C whenever S_full is nonempty: for c∈C lift it to S and multiply a preimage from S_full. A completely simple semigroup is simple, so any nonempty ideal is all of C. Thus

`q|_(S_full):S_full→C is ONTO`.

FULL-CS holds for EVERY maximal subgroup of S_full by its definition. No new/coarser actor or quotient is introduced.

If S is in the original locally r-orthodox class, so is the ideal S_full: for e∈E(S_full), its local idempotent bands and closure are inherited from eSe, and in fact eSe⊆S_full because S_full is an ideal. Therefore Theorem F2 supplies an explicit embedding of the ENTIRE S_full over the SAME q into an allowed physical P(B,C), B∈V. This is a uniform complete positive construction on the actual ideal, not a restriction to finitely many tested elements.

## 5. When nonemptiness is guaranteed

If S has an ACTUAL completely simple ideal K, then q(K) is a nonempty ideal of C and hence equals C. For e∈E(K) and y∈H_(q(e)), choose k∈K with q(k)=y. The element e k e belongs to eKe=H_e and maps to q(e)yq(e)=y. Thus EVERY H_e in K is FULL; equivalently K⊆S_full, so S_full is nonempty.

In particular every FINITE nonempty completely regular S has such an ideal: its finite semilattice Y has a least element, the meet of all its elements, and the corresponding completely simple component is an ideal. This argument is purely structural, not an enumeration or finite witness. Thus EVERY finite CR original-class source with supplied pure q has the nonempty canonical allowed-host-embeddable ideal S_full, even when S itself has upper components not covered by F2.

For infinite Y, no least element or full component is assumed. The argument gives an implication from an actual completely simple ideal, not a new existence theorem. It also does not supply q in an arbitrary infinite source.

## 6. Precise extension obstruction left open

The original whole-source problem is now localized, for this CR setting, to extending the known S_full embedding across the NONFULL component complement while preserving ALL original mixed products. S_full being an ideal and having a host does NOT give S a host. No retraction onto S_full, congruence collapsing its complement, splitting section, induced action, separating total-map family or faithful extension is asserted.

The lower-host property does not recover the missing r(e,w,f) of Theorem F for a NONFULL upper e: its required element lies in H_e, not in an arbitrary lower full group. Replacing it by a lower element would alter the source component and the mixed multiplication constraints. This is exactly why the canonical ideal result does not remove FULL-CS from the full-source theorem.

Not supplied: a complete extension across every nonfull component; a source-valid failure invariant for ALL allowed physical hosts; a non-CR theorem; an arbitrary-infinite pure-CS existence theorem; the restricted-action R reading; novelty/formal/kernel/human/configured-family acceptance. Original unrestricted acceptance remains UNMET.

## 7. Imports and process boundary

Named classical imports: Clifford's CR semilattice of completely simple components, Rees representation, the local-group property eTe=H_e in a CS semigroup, and simplicity of C. Sections2–5 prove all new deductions explicitly. The embedding conclusion additionally consumes the ENTIRE F/F2 candidate union, with all its declared classical imports and unreviewed status. No old false CG/RU-LU claim or LI2003 proof is imported.

No identity was machine-checked. No scientific interpreter/calculator/program/CAS, numeric/state/control/magnitude/decimal probe, enumeration/table/checker, solver/replay, build/test, external CLI, nested agent or GO. No withdrawn-guidance reuse, frozen/shared edits, retrospective permission or clean-history claim. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/prospective substantive30minJSON/no early park or round closeout.
