# Frozen review w1-tuscan-gluing

**Reviewer:** MathSemigroup-2. **Author:** InfoRecursiveMDS18-2 (info-4).

First actual review-wake clock: **Tue Oct 27 14:47:28 PDT 2026**. Actual native clock immediately before writing: **Tue Oct 27 14:48:16 PDT 2026**.

## Verdict and counts

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE.**

- FATAL: **0**.
- MAJOR: **0**.
- MINOR: **0**.

The equivalence and the all-n>=3 reflection counterfamily hold as written. The counterfamily refutes the **pairwise-only relaxation**, not Tuscan-2(11). No original witness, universal no-go, new support bound, independent-model gate or novelty acceptance follows.

## 1. Frozen inputs, complete reading and exposure

I first read the complete manifest, SHA `6dd48203cb3d4385318f5c84c65532f85eda8817ddea53828bf02f7cfadec58c` (28 LF), then the **entire 191-LF packet**, SHA `02d23b3ea4f770a68b14adc60ec6b4d65913706a79ce99943d95fe392ac336de` (19744 bytes), including both source endings, before forming this verdict.

The packet supplies:

- **S1:** full37-LF context, SHA `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`. The original definition is its outer S1:31–33; nested LF labels are not separate source reads.
- **S2:** full146-LF author candidate, SHA `5c7e2c40f979b41c30608da7d75de7039ae458bfce949a50bc259f3d7a6b0b76`.

References below use these **outer source labels and their original LF numbers**.

Prior Tuscan-related review/authorship exposure in the preceding round, including the inherited v106 ordered-read finding, survives; I am not blind or clean-room. No old proof, review, checkpoint, private method, verdict or held guide was reopened or used. I reconstructed the arguments below from these literals and elementary finite-set facts. There was no author contact, scientific execution, calculator/Eval, CAS, enumeration, selected instance/probe or external source fetch. I wrote only this output file.

The context provides a documented modern primary-definition literal. Its upstream raw response, book-page equivalence, current openness and external provenance were **not** independently checked here; none is a hidden premise for the elementary statements reviewed. Same-harness WRITTEN review is not formal/kernel/human/configured-family/executable/novelty acceptance.

## 2. Claim-by-claim dispositions

| Claim / literal scope | Mathematics | Dependency/application boundary |
|---|---|---|
| Actual linear row/event object, S2:24–34 | CORRECT | Exactly S1:31–33: each row a permutation, distinct directed pairs, separate linear distances1 and2, no wraparound or column condition. |
| Pairwise collision equivalence, S2:36–52 | CORRECT | Uses actual common symbols and genuine bijections. The apparent missing starting-position guard in the second row follows from the equality and image bounds; no endpoint is lost. |
| Noncollision implies exact distance1 coverage, S2:54 | CORRECT | Uses exactly n rows of length n, no within-row duplicates, and finite counting. It does not impose distance2 coverage. |
| Identity, reciprocity, triangle product and necessity, S2:58–76 | CORRECT | All row identities, including repeated indices; the same intermediate row labelling is essential. |
| Simultaneous converse and common-symbol uniqueness, S2:78–92 | CORRECT | Explicit n actual rows from one anchor, not independent pair realizations. Uniqueness is only up to one common symbol relabelling. |
| Degeneracies, S2:94–98 | CORRECT at stated scope | Original n=11; nonempty row set for anchoring. Distance2 is vacuous for positive n<3. Repeated identities are excluded only from admissibility, not the triangle law. |
| Uniform reflection counterfamily, S2:110–130 | CORRECT for every integer n>=3 | Every non-diagonal map passes both same-distance collision tests, reciprocity and individual two-row realization; every triangle with **three distinct row identities** fails. Repeated-index triangles do not fail and are not claimed to. |
| Failed implication and original-target ceiling, S2:100–108,132–146 | ACCURATE | Local pair success does not imply a common array. The original eleven-row existence/no-go question and every support case remain open. The sign-consistency investigation at S2:144 is a proposal, not a proved result. |

## 3. Direct reconstruction of the actual-object equivalence

### 3.1 Pairwise collision test and endpoints

Fix distinct rows r,s, a distance d in {1,2}, and a legal i in row r. Put x=a_r(i) and y=a_r(i+d). Because p_s is the inverse of the **same** row bijection a_s, their positions in row s are F_rs(i) and F_rs(i+d).

The directed pair is a distance-d event in row s exactly when

F_rs(i+d)=F_rs(i)+d.

If this equality holds, let j=F_rs(i). Both images lie in {1,...,n}, so j>=1 and j+d<=n. Thus j is automatically a legal starting position. Conversely any repeated directed event supplies such i,j and therefore that equality. This proves S2:50–52 in both directions without cyclic positions, a sign ambiguity, or a forgotten endpoint.

Within a single row an ordered pair at a fixed distance cannot appear twice: its first symbol occurs at one position only. Consequently all repeated events at that distance are exactly the cross-row collisions just characterized.

The two distances remain **separate**. A pair once at distance1 and once at distance2 is not excluded. The test does not compare events of different distances or reversed directed pairs.

### 3.2 Distance1 count is exactly the original coverage condition

Each of n rows has n-1 legal adjacent starts, so the adjacent-event domain has n(n-1) elements. Its codomain, ordered pairs of **distinct** symbols, also has n(n-1) elements. Row bijectivity prevents equal-symbol events and within-row repetitions; admissibility of every non-diagonal F_rs prevents all cross-row repetitions.

Thus the adjacent-event map is an injection between finite sets of equal cardinality, hence a bijection. Every ordered pair appears exactly once. This pays the word **exactly** in S1:31, not just an at-most-once relaxation.

At distance2 the same reasoning establishes precisely noncollision. There is no inference of full pair coverage. This distinction is correctly retained at S2:54.

### 3.3 Necessity of the full permutation-valued coupling

For actual rows, F_rs=p_s a_r gives:

- F_rr=p_r a_r=id;
- F_sr=a_r^-1 a_s=(a_s^-1 a_r)^-1=F_rs^-1;
- F_st F_rs=p_t a_s p_s a_r=p_t a_r=F_rt.

The last cancellation uses a_s p_s=id on the **single common symbol set**, not merely equal counts or independently selected pairwise labels. Multiplying by F_tr on the left gives the closed-triangle identity.

If indices repeat, these equations reduce to identity or reciprocity and remain valid; no exceptional repeated-index constraint is discarded. This verifies S2:62–74.

### 3.4 Converse: one actual family realizes all relations simultaneously

Given the full bijective F-system with these identities, fix one row identity o and a bijection lambda from positions to symbols. Define

a_r=lambda F_or^-1,   p_r=F_or lambda^-1.

These are inverse bijections for every r. With r=o, the identity F_oo=id gives a_o=lambda. The cocycle on o,r,s says

F_rs F_or=F_os,

so F_rs=F_os F_or^-1=p_s a_r. This realizes **every** ordered row pair at once. The construction supplies actual symbol orders with their own endpoints, not just an event margin or a pairwise abstract graph.

Adding admissibility gives exactly both original conditions by §§3.1–3.2 above. Conversely the actual Tuscan array supplies that admissible cocycle system. No old completed-turn or row-realization theorem is needed.

For uniqueness, take any other realization a'_r and use the same anchor o. It satisfies a'_r=a'_o F_or^-1. Hence a'_r=(a'_o a_o^-1)a_r for all r, with **one common symbol permutation** a'_o a_o^-1. There is no independent row-specific relabelling freedom. This proves the stated uniqueness at S2:80–90.

## 4. Direct reconstruction of the uniform non-gluing family

Let n be any integer at least3, and J(i)=n+1-i on the linear position set. J maps the set bijectively to itself and J(J(i))=i. For any legal i,d,

J(i+d)-J(i)=-d.

Since d is a positive ordinary integer, -d is not d. Both d=1 and d=2 therefore pass (A) at every legal start; no modular identification is used. If n is odd, the fixed middle position does not cause a forbidden short positive jump.

Put F_rs=J for every distinct r,s and F_rr=id. Inversion gives reciprocity for every pair. Identity/repeated-index cases also satisfy the corresponding two-edge inverse relations.

Each **individual** pair really is realizable: choose any labelled row a_r, and define p_s=J p_r, so a_s=a_r J^-1=a_r J. Then p_s a_r=J and p_r a_s=J. By the preceding event test the two rows share no directed event at the same distance1 or2. This verifies the local claim without calling two rows a full n-row Tuscan array.

Now choose arbitrary **distinct** r,s,t. Then

F_st F_rs=J J=id,

whereas F_rt=J. J is not the identity for n>=3, for example its symbolic endpoint image J(1)=n differs from1. Thus the triangle equation fails for every such ordered triple. Equivalently the three-edge closed product is J, not id. This is a uniform all-n formula, not an inspected instance or a selected boundary test.

Necessity of the cocycle rules out any common simultaneous rows for this family. It does not rule out other coherent admissible families; that separation of conclusions is explicit at S2:132–134.

**Lower-order boundary:** n>=3 is needed to have three distinct row identities. For n=2 there is no such triple and the all-reflection two-row system can be realized; this is outside Theorem4's claimed range, not a defect. For positive n<3 the empty distance2 domain and the earlier equivalence proofs cause no contradiction. No claim about an empty row-identity set is needed for the n=11 target or n>=3 counterfamily.

## 5. Imports, original caller and exclusions

All load-bearing steps use elementary composition/inversion of finite bijections, injective finite counting, and directed linear event indexing, exactly as S2:18 states. Every application is paid in §§3–4; there is no additional NR theorem under the reviewed claims.

The literal original n=11 conclusion is:

- a coherent admissible system produces the required eleven actual rows;
- every such array produces a coherent admissible system;
- an incoherent but locally admissible reciprocal family demonstrates why pairwise data alone is insufficient.

Neither the representation nor the reflection counterfamily gives an original T2(11) witness or universal impossibility, and the author does not promote them as such. No omitted row-realization assumption, Latin-column condition, wraparound, support theorem, m-range restriction, old type8 construction or excluded guide is used here.

The same-harness review supports only the supplied mathematical equivalence and the stated failure of pairwise-only gluing. No scientific adoption, priority, current-openness or original-target success is certified.
