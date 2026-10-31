# Addendum 7 — shortened-kernel thresholds repair the transport budget and give mixed-prime group classes

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 15:31:54 PDT 2026**.
**NEW complete WRITTEN candidate transport theorem and positive original-group corollary. Not adopted or novelty-cleared.**

## 1. Scope, inputs and distinct method branch

This continues the SAME S1/S2 definition-first release and Main's standing direction. The separate prospective group-algebra/augmentation branch remains STOPPED pending its source/method-separation decision; NOTHING from it is used here.
The present branch uses ONLY the currently admitted original definitions, ordinary exact counting/group quotients, and the explicitly identified current-author polynomial proof inputs below. No new source, old proof, held formula or consumer is opened or used.
Prior exposure remains disclosed, not certified clean or independent.

The original O(G) means EVERY actual2n−1 word in G, n=|G|, has an ORIGINAL-order identity selection of EXACTLY n actual occurrences.
The first transport theorem below is valid for ANY finite G under EXACT stated kernel/quotient hypotheses; it does not assume solvability, split extension, commutativity, a chosen action, symmetry or a word ansatz.
The resulting index-two corollary applies to an ENTIRE mixed-prime group class, not just selected words. The unrestricted all-finite-group question remains open beyond the claimed classes.

## 2. A genuine quantitative transport lemma

Let K be ANY normal subgroup of ANY finite G. Put k=|K|, h=|G/K| and n=kh.
Let D be an integer with0≤D≤k−1.
Assume BOTH actual-word assertions:

- **Short(K,D):** EVERY word of length k+D in K has an ORIGINAL-order identity subsequence of EXACTLY k occurrences.
- **O(G/K):** the ORIGINAL ordered assertion holds for the quotient, at its own2h−1/h threshold.

**Theorem A.** If

`(2h−1)D ≤ k−1`,

then O(G) holds at the FULL original2n−1/n threshold.

**Proof, actual objects throughout.** Fix ANY actual word of length2kh−1 in G.
The numerical hypothesis is exactly

`(k+D)(2h−1) ≤ 2kh−1`.

Partition its first (k+D)(2h−1) positions into k+D consecutive chunks of length2h−1. Any remaining original positions are simply unused.
Apply O(G/K) to the quotient word in EACH chunk and choose exactly h actual positions in increasing order with quotient product1.
These packets are chronologically separated because their entire chunks are separated.
Let their ACTUAL G-products be b_1,…,b_(k+D), all in K.
Apply Short(K,D) to THIS ordered kernel word. It gives exactly k increasing packet indices with product1.
Because the packets are separated, that packet-product concatenation is LITERALLY the original-order product of their union.
The union has EXACTLY kh=n distinct actual occurrences, and its chronological product is identity.
This proves O(G) for EVERY original word. ∎

There is no uncoupled crossing step, no assuming packet products central and no changing cardinality from n to a quotient order.
No general converse to TheoremA is claimed; the numerical condition is sufficient for this separated-chunk construction, not necessary for the original problem.

**Degeneracies.** If K is trivial, k=1,D=0, and the argument is exactly one quotient selector. If h=1, the condition reduces to D≤k−1 and the original word contains a prefix of length k+D to which Short applies. D=0 is permitted as a hypothesis without asserting it for nontrivial kernels.

This explains the failed earlier budget precisely: ordinary O(K) supplies only D=k−1, which cannot meet the inequality when k,h>1. A genuinely SHORTER kernel theorem changes the transport, not a renaming of disjoint packets or erasure of crossing corrections.

## 3. What the current polynomial proofs actually give: Short(K,D)

The following uses explicitly named CURRENT author proofs, not their adoption or a prior review verdict:

- A5 `prerequisite-derivation-addendum-5-class2-prime-exponent-selector-v1.md`,244LF, SHA256 `cefc589575fc1acdd5536e1fbd42a9f78da970148d121701673c9b86442e90aa`;
- A6 `prerequisite-derivation-addendum-6-class2-p-group-carries-v1.md`,282LF, SHA256 `c4641b356ea4f2e9fd2630ed3a4e50707252fdfaded3da970e3210807f054799`.

Their COMPLETE load-bearing input is the actual normal form, exact cardinality digit equivalence and fully proved field zero-count lemma, NOT just a displayed degree bound. These source bodies must be included in any review/adoption that consumes the following corollaries.
The independent transport TheoremA itself does not require either polynomial proof; its assumptions are stated as actual-word properties.

### 3.1 All finite class-two p-groups

Let K be ANY finite p-group of class at most2, order k=p^m.
Use A6's ACTUAL cyclic normal-coordinate factors q_i for K/Z(K) and r_j for Z(K), and let q=max q_i, with q=1 when there is no quotient factor.
Define

`D = sum_i(q_i−1) + q sum_j(r_j−1)`.

A6 proves D≤k−1 and constructs the ACTUAL coordinate/carry digit equations with total group-degree cost at most D after its Boolean-to-field substitution.
For a word of length L=k+D rather than2k−1, use the SAME equations and the SAME cardinality digits for multiples of k.
Their total degree cost is at most

`(k−1)+D=L−1<L`.

Because L≤2k−1, those cardinality digits still force support0 OR EXACTLY k; no extra support size enters at the shortened length.
The fully proved zero-count lemma again gives C≡0 modp, and the SAME exact actual-support count is

`C=1+A(p−1)^k`.

Thus A≡1 modp, and Short(K,D) follows for EVERY actual word of this shortened length.
All original-order commutators and central-power carries from A6 remain in the equations. Nothing is discarded by changing L.

For a trivial kernel take D=0 and its immediate single-occurrence selector; no polynomial degeneracy is hidden.

### 3.2 Sharper D in the prime-exponent class

For an odd prime p and ANY finite exponent-dividing-p group K of class at most2, use A5's ACTUAL normal vector coordinates.
Let d=dim(K/Z(K)), c=dim Z(K), so k=p^(d+c)=p^m.
The actual group-equation cost in A5 is

`D=(d+2c)(p−1)`

when K is nonabelian; the bilinear central terms are retained.
If K is abelian, those terms vanish and the sharper actual cost is

`D=m(p−1)`.

The same degree/count argument just given yields Short(K,D) whenever D≤k−1. This is not inferred from O(K) alone; it follows from the COMPLETE coordinate/digit zero-count proof.
In particular all inequalities needed in the next section are proved explicitly and imply D≤k−1.

The count congruence at the shortened length is also A≡1 modp. It is not a numerical estimate or a formal support claim without realizability.

## 4. Full positive mixed-prime class: ALL index-two extensions of sufficiently large prime-exponent class-two kernels

**Theorem B.** Let p be ANY odd prime and m ANY integer at least3.
Let G be ANY finite group with a normal subgroup K of index2 such that

- K has order p^m;
- K has exponent dividing p;
- `[K,K]⊆Z(K)`.

Then O(G) holds for EVERY original word of length2|G|−1, with EXACTLY|G| original occurrences.
No split assumption, restriction on the outer conjugation action, or assertion that G itself is class two is imposed.

**Proof of the short-kernel bound.** If K is abelian, D=m(p−1)≤(2m−2)(p−1), since m≥3.
If K is nonabelian, its central quotient cannot be cyclic: a group whose quotient by its centre is cyclic is abelian, by writing all elements as powers of one lift times central elements.
Thus the quotient vector dimension d is at least2, while m=d+c, so

`D=(d+2c)(p−1)=(2m−d)(p−1) ≤ (2m−2)(p−1)`.

For EVERY p≥3,m≥3,

`p^m−1 ≥ 3(2m−2)(p−1)`.

To prove it without selected checks, divide by p−1. At m=3 the difference is
`(1+p+p²)−12=(p−3)(p+4)+1>0`.
Increasing m adds p^m to the left and6 to the right; p^m≥p(p−1)≥6 throughout the stated domain. Induction proves the inequality.
Hence3D≤k−1 and the actual Short(K,D) proof in §3 applies.

**Quotient input paid.** O(C2) follows by pigeonhole: in ANY three quotient letters, two agree, and both elements of C2 square to identity. Thus an index-two quotient satisfies the needed assertion, not an imported unresolved quotient theorem.
TheoremA with h=2 and3D≤k−1 now gives the full original O(G), preserving every actual occurrence and order. ∎

This covers mixed-prime orders2p^m with the stated kernel property, including all permitted extension actions, not just a chosen semidirect construction.
It is a positive GROUP-CLASS candidate at the ORIGINAL threshold, not another architecture/word-family exclusion.
It may already be known; no novelty/SOTA/priority claim is inferred.

The theorem deliberately does NOT assert the m=1 case of order2p, nor all m=2 cases. In particular it does not smuggle the old unresolved odd-prime dihedral route into the result.
Failure of the sufficient budget for an omitted case is not a counterexample to O(G) or proof that no other method works.

## 5. General normal extensions to which the same proof applies

For ANY normal K with an ACTUAL Short(K,D) theorem and ANY quotient H with an ACTUAL O(H) theorem, TheoremA applies whenever `(2|H|−1)D≤|K|−1`.
The quotient may be taken from the class-two p-group theorem when its entire proof is included at that gate; no same-prime or coprime hypothesis is required by the transport itself.
This is a conditional reusable reduction, not a claim that every original group has such a short kernel or that every quotient is already settled.

There is no appeal to centrality of K, independent overlap models, a fixed noncrossing matching or arbitrary kernel labels. Consecutive chunks preserve chronology literally; the shorter kernel threshold supplies ENOUGH such chunks at the original length.
The selected k packet products are an ACTUAL K-word to which the stated short theorem applies.
Conversely an arbitrary original selector need not have this chunk certificate; no necessity is used or claimed.

For the earlier alternating index-two obstruction, the capacity floor((4k−1)/3) was too small for2k−1 packets but IS sufficient for k+D when3D≤k−1. The new theorem changes the proved premise quantitatively, so it does not contradict or silently withdraw that counterfamily.
This is not repair of a held historical formula: the complete current S1 conditional packet argument and the newly supplied full polynomial short-threshold proof are the declared inputs.

## 6. Dependency/application and exact assurance ceiling

TheoremA is proved entirely from elementary group quotients, chunk counting and the two EXPLICIT actual-word hypotheses. O(K) and O(H) are not assumed true merely because they are names of the original conjecture.
TheoremB depends on the COMPLETE A5 actual coordinate/digit/zero-count proof and its exact shortened-length reuse, plus the elementary O(C2) proof and the universal bound supplied here.
The arbitrary-exponent §3.1 statement depends on the COMPLETE A6 carry/divisibility proof, not only its theorem header. Those bodies are current author-written candidates, not already accepted imports.
Every later adoption must freeze/review that full mathematical AND dependency/application union. No already frozen scope is enlarged by this file.

Original all-finite-group O(G), all mixed-prime kernels/quotients without these hypotheses, higher-class p-groups and the old odd-prime dihedral intermediate bridge remain outside what is proved here.
No actual avoiding word, global no-go or unrestricted solution is claimed.
The progress is a genuine short-threshold/normal-extension coupling and a full original-order positive proper group class, not a coordinate restatement alone.

Every STOP/HOLD/ZERO outside S1 and the separately stopped prospective group-algebra branch remains. All nine held formulas/consumers, v214-A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and old process findings persist.
No new source, old proof/guide, scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numerical/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
Prior exposure is not erased; no clean-cognition/noninfluence/global-runtime certificate. WRITTEN/same harness, not Main adoption/formal/kernel/human/configured-family/executable/novelty acceptance.
Same18/new exclusive append-only root/actual substantive20min target and honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE SHORT-KERNEL TRANSPORT AND INDEX-TWO EXTENSION THEOREM.**
