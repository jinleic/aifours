# ALL-R-PAIR-COVER is false as stated: a uniform actual-word counterfamily

Clock observed before exclusive creation: 2026-10-22T02:31:19-0700. Drafting began earlier, AFTER Main explicitly acknowledged the delivered complete Step0 baseline. Status: **CANDIDATE WRITTEN COUNTERFAMILY; NOT ACCEPTED.** This manuscript proves the negation of the frozen universal implication by a family inside its exact domain. It does not silently replace the target by a smaller theorem. The required configured second-family gate is unavailable; source construction, parent handchecking and first-family agreement cannot promote this result.

## 0. Scope, exposure and trust

The frozen target is every prime p>=7 and EVERY length-(4p-2) word over D_(2p) with all rotations in one nonzero pair, every maximal cyclic constant reflection block odd, kappa=p-1-sum floor(ell_i/2) in [2,p-1], at EVERY actual rotation count R. Its conclusion is an increasing ORIGINAL-index selection of EXACTLY 2p letters with identity product. The entire original class remains the object being tested.

The argument below is elementary and self-contained from the literal group law. It uses NO R3 candidate lemma; NO old R-dependent theorem; NO S(p), Lev, CT, NF converse, unrestricted reflection/rotation rigidity, high-core exclusion, realizability surrogate, scientific computation or finite sample. The lengthy Step0 baseline and source authorities are retained for audit/old credit, not as hidden premises of this counterfamily proof. In particular this proof does not require the correctness of any terminal-frontier component, conditional RED/RGR import or B0 structural theorem.

The parent's unverified prescope formulas and the complete prior R3 premature-route exposure were known. No blind corroboration, independent discovery, priority, novelty or strict preregistration is claimed. All earlier process MAJORs/documentary MINORs remain uncured. The present proof began ONLY after the parent explicitly acknowledged the full Step0 delivery.

## 1. The group, word, and exact membership in the entire frozen domain

Fix an arbitrary prime p>=7. Use the group

    D_(2p)={(v,e): v in Z_p, e in {+1,-1}},
    (v,e)(v',e')=(v+e v', ee'),
    rho_x=(x,+1), sigma_y=(y,-1).

The identity is (0,+1). All exponents in the following word count actual occurrences, not residues. Define

    w_p = rho_1^(2p-1) (sigma_0 rho_-1)^(p-1) sigma_0.           (W)

Write its initial rotation segment as U=rho_1^(2p-1), its reflection occurrences in their ORIGINAL order as f_1,...,f_p, and its intervening negative rotation occurrences as t_1,...,t_(p-1). Thus

    w_p = U f_1 t_1 f_2 t_2 ... f_(p-1) t_(p-1) f_p,
    f_j=sigma_0 for 1<=j<=p,  t_j=rho_-1 for 1<=j<=p-1.        (O)

There is exactly one t_j between each two consecutive reflection occurrences. There are no reflections before U, and no rotations after f_p in this ORIGINAL linear presentation.

The exact actual counts are

    A=2p-1, B=p-1, R=A+B=3p-2, F=p,
    |w_p|=(2p-1)+2(p-1)+1=4p-2.

Every rotation lies in the SAME nonzero pair {rho_1,rho_-1}. Because p is odd, these are distinct and 1 is nonzero in Z_p. Every reflection occurrence is separated from the next by a nonempty rotation gap: one t_j inside the suffix and the nonempty segment U across the cyclic boundary. Consequently every maximal CYCLIC CONSTANT reflection block is exactly one f_j, even though all reflection values equal0. There are k=p such blocks, each of length1, with

    H=sum_(j=1)^p floor(1/2)=0, kappa=p-1-H=p-1 in [2,p-1].

There are no empty rotation gaps; the genuine-empty-gap condition is vacuous, not an added hypothesis. The actual runs are one pure positive run of length2p-1 and p-1 pure negative singleton runs. This is merely a particular allowed word; the frozen target permits it because it quantifies over arbitrary B and over pure as well as mixed runs. No target restriction is imposed by choosing it.

Thus (W) lies INSIDE the frozen all-R target for EVERY prime p>=7, at its explicitly retained high-R/lower-k corner

    R=3p-2, kappa=p-1, H=0, F=k=p.                           (C)

This is actual word construction, not a feasible relaxed tuple or a numerical diagnostic.

## 2. Exact ordered-product accounting for an arbitrary selection

Suppose that an arbitrary selection I of EXACTLY 2p positions in increasing ORIGINAL index order has been made. Let C be its number of selected reflections, n=2p-C its number of selected rotations. Since exactly p reflection occurrences exist, 0<=C<=p. The second coordinate of the ordered product is (-1)^C. If C is odd, the product is not identity. Hence only EVEN C need consideration; then C<=p-1 because p is odd, and n is even.

For completeness the first-coordinate rule follows directly by induction from the group law: multiplying a next selected letter (a,e) into a current partial product (V,E) replaces V by V+Ea and E by Ee. Thus each selected rotation of original value x contributes

    (-1)^(number of selected reflections preceding it) * x

to the first coordinate. Each selected sigma_0 contributes0 and flips the sign. Unselected reflections do not flip any sign. This is literal prefix parity in the ORIGINAL order, not an independently chosen zone labeling.

Every selected rotation in U contributes +1: no reflection precedes U. A selected t_j has original value -1; it contributes -1 exactly when an EVEN number of selected reflections precede it, and +1 exactly when that number is ODD. Let v be the number of selected rotations whose effective contribution is -1; the other n-v selected rotations contribute +1. For C even, the complete ordered product is therefore

    (n-2v mod p, +1).                                      (P)

No reflection-value term is suppressed: every selected reflection really is sigma_0 and has first-coordinate value0. No cyclic rotation or transport of selections is used.

## 3. The one-letter negative-capacity deficit when C>=2

Assume C>=2 is even, and enumerate the selected reflection occurrences as

    f_(i_1), f_(i_2), ..., f_(i_C),  1<=i_1<...<i_C<=p.

For each a=1,...,C/2 consider the open ORIGINAL-order interval between f_(i_(2a-1)) and f_(i_(2a)). Their indices are distinct, so i_(2a)>i_(2a-1). The interval contains at least the actual rotation occurrence t_(i_(2a-1)), which exists because i_(2a-1)<=p-1. More explicitly the rotation occurrences in it are

    t_(i_(2a-1)), ..., t_(i_(2a)-1).

Between these two consecutive SELECTED reflections, exactly 2a-1 selected reflections precede every such rotation, an ODD number. There may be other unselected reflections in the interval; those do not change this parity. All these negative-valued rotations would therefore contribute +1 if selected, and none can supply an effective -1 contribution.

The C/2 open intervals are pairwise disjoint in ORIGINAL order, so they exclude at least C/2 DISTINCT occurrences from the total p-1 negative-valued rotations as potential effective negatives. The initial U occurrences cannot contribute negatively at all. Consequently

    v <= (p-1)-C/2.                                       (N)

The proof of (N) does not require selecting any of those intervening rotations. They may all be skipped; doing so does not create a replacement negative occurrence. This is a capacity bound on actually available occurrences.

On the other hand C>=2 gives

    n=2p-C even,  n<=2p-2.

If (P) were identity, the integer n-2v would be divisible by p. It is even and lies in [-n,n], hence has absolute value <2p. The ONLY even multiple of odd p with absolute value <2p is0: the other possible nonzero multiples in that interval, +p and -p, are odd. Therefore identity would force

    n-2v=0,  v=n/2=p-C/2.                                (B)

The demand (B) exceeds the available upper bound (N) by EXACTLY ONE. This is impossible for every permitted even C>=2, including C=p-1. Thus no selection with a positive even number of reflections has identity product.

Equivalently (N) gives n-2v>=2, while n-2v<=n<=2p-2 and is even; such an integer is never0 mod odd p. Both readings use the same actual ordered-product calculation.

## 4. The C=0 case, with the endpoint 2p treated separately

Now let C=0, so n=2p and every selected rotation retains its original sign. All selected letters are rotations. Let v be the number of selected rho_-1 occurrences. Its availability bound is

    0<=v<=p-1.

The first coordinate is 2p-2v mod p. Because p is odd, divisibility by p is equivalent to v=0 mod p. In the displayed interval the only possibility is v=0. But this would require selecting 2p positive rotations, and only A=2p-1 exist. Therefore C0 is impossible too.

The same case can be described by the general two-value rotation test: an identity2p selection from a pair requires0,p,or2p negative occurrences; 0 would need2p positive occurrences, p/2p exceed B=p-1. Treating C0 separately is essential because the even coordinate +2p, unlike the C>=2 range, is divisible by p.

## 5. Exhaustion and exact scientific outcome

An arbitrary original-index selection of exactly2p positions has either C odd (wrong reflection parity), C0 (Section4 impossible), or C even>=2 (Section3 impossible). These cases exhaust all selections; no pattern, frame, small prime or occurrence placement has been sampled or omitted. Hence

> **Uniform counterfamily theorem, CANDIDATE:** For EVERY prime p>=7, the explicit actual word (W) has length4p-2, belongs to the ENTIRE frozen pair/all-odd/kappa2..p-1 word class, and has NO identity subword of exactly2p positions in increasing ORIGINAL index order.

Therefore the frozen universal ALL-R-PAIR-COVER implication is **FALSE AS STATED if this written candidate proof is upheld**. It is not merely lacking a uniform continuation, and a full proof of that implication cannot honestly be delivered. This is the exact first failed assertion: the implication already fails on the UNBOUNDED family (C), not just one selected prime or a method-specific inequality. The family's construction does not require or assert the rest of the residual feasible.

This result does NOT invalidate accepted old providers. The family has k=p, not terminalp+1; B=kappa=p-1, not the strict B<kappa condition of RES_<; and R=3p-2 is not R=p+1,p+2,p+3 for any prime in the frozen range. Its rotation multiplicities are below2p and B<p, so the old rotation-only tests correctly fail. It lies on the EXACT boundary R=2p+kappa-1 allowed by Zbound, not in the excluded R>=2p+kappa range. Its lack of an empty gap means conditional TRANSFER's reflection-run-constancy conclusion would say something already true, not create an identity2p selection. The old baseline and high-k necessary systems do not assert this lower-k corner excluded.

## 6. Entire residual/credit and nonpromotion

The entire original target and the complete old union/residual/actual-word filters remain those of `STEP0-OWN-BASELINE-v1.md`; no R or kappa was removed from that audit. New manuscript (W) supplies actual words inside its residual, uniformly for every p, and refutes the full universal implication. It does NOT claim that all other residual words avoid, that it classifies every avoider, or that its complement is now proved. No repaired new target such as kappa<p-1, R<=3p-3, B<kappa, k>=p+1 or nonconstant reflection values is proposed as a substitute. Such a target would require a fresh owner/parent freeze, outside this assignment.

Old P/end-range/ROT/Zbound/Rp/DELTA1/DELTA2/NFdiag/I14/SEG-k/Bprime/structural-filter credit is OLD. The elementary explicit counterfamily proof above is the new candidate result; no novelty or priority claim is made. It may be a familiar extremal family; determining its literature history would require a separately authorized source audit and is not claimed here. It says nothing about identity2p existence at length4p-1, unrestricted ordered Olson, INV*, other groups, or even-block words. No source or tool calculation is used as mathematical evidence.

This manuscript is handwritten mathematics, not a finite checker, solver output, code certificate, Lean/kernel proof, human-referee verdict or completed two-family acceptance. Main has exclusive responsibility for parent handcheck, source reconstruction and any permitted first-family gate. The configured Claude reset after the deadline remains a hard external blocker: no launch, retry workaround, model/account/provider/payment/configuration change, quota substitute or promotion is authorized. All prior process qualifications travel in the source packet and handoff unchanged.
