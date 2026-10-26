# Critical raw matching: cross-K rotation rigidity and one-arc concentration

Observed before exclusive creation: **2026-10-23T14:41:31-0700 PDT**. MathOlson-2, math-2. **CANDIDATE written necessary reduction with actual positive selection contrapositives.** Same ordered-Olson primary problem, not a separate problem or a review-only task. No scientific execution. Full MIX remains open.

## 0. Exact setting and what is new

Fix ANY prime p>=7 and ANY ACTUAL word of N=4p-1, R=p+1 rotations, F=3p-2 reflections in D_(2p), with the displayed semidirect-product group law from the frozen selection. Assume actual reflection gaps have 0 or 1 rotations. This is exactly the whole remaining band after the old literal P test; a repeated occupied gap is already P-covered at the original accepted statement. All rotation values INCLUDING0 and arbitrary reflection runs/values/parities remain.

Let M(w) be the CYCLIC graph on actual reflection occurrences, with an edge between consecutive reflections retained if their values differ OR the gap contains a nonzero singleton rotation. This is the possible-switch graph defined in `proof-TWO-FREE-ROTATION-CONTROLS-v1.md`, observed pin **34e8850b4c4c790ca69f7e7ef601523d35d87508cf21984af08175a595b0a914**. That paper constructs actual K from a p-1 raw matching. Its theorem is not assumed accepted here; the needed graph/activation arguments are supplied again below. This paper handles a p-2 raw matching by comparing DIFFERENT actual rotation sets K and DIFFERENT actual singleton fillers, rather than classifying one fixed sumset again.

The exact selected-K gauge and p-2 inverse were fully written in `proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md`, pin **cfc59821268165483319fdbc69f01c5f626904b3332f13076e33f97dc29c9f75**. Its actual separate MathShor reconstruction found no substantive defect at that partial scope; parent review remains separate. The short needed arguments are restated below.

**Consequential delta:** for EVERY possible matching of p-2 raw edges, all its possible active difference values must share ONE nonzero step up to sign; its unmatched rotations must be either ALL identities or ONE nonzero opposite pair; and in the nonzero case ALL p+2 unmatched reflection occurrences must lie in ONE arc between consecutive unmatched rotations. These are DERIVED restrictions on hypothetical survivors, not an assumed common rotation alphabet or a classification of all words. The conclusion about the unmatched rotations is obtained by an actual same-cardinality exchange of selected rotation sets, not from one necessary normal form.

## 1. A critical matching and its exact available choices

Fix any matching E of t=p-2 possible-switch edges, on ACTUAL disjoint adjacent reflection pairs. It need not initially be maximum. Let V be the set of ACTUAL rotation occurrences whose gaps are NOT matched edges; call them free rotations for THIS matching. Since at most p-2 of the p+1 occupied gaps are matched,

    m=|V|>=3.                                             (1)

Let U be the set of reflection occurrences that are NOT endpoints of these matching edges. Then

    |U|=F-2t=p+2.                                         (2)

Choose a cut in the gap of one free rotation. No matched pair crosses that cut. All references to packet order and reflection prefix signs below use this ordinary cut word first, followed by restoration of the original cut.

For a matched edge e, write a_e=y_right-y_left. Its set of POSSIBLE NONZERO gauge differences is

    V_e={a_e} if the gap is empty;
    V_e={a_e,a_e+2x_e} minus{0} if it contains rho_(x_e).    (3)

Each V_e is nonempty, by the definition of M(w). A choice v_e in V_e is realized by choosing whether its actual singleton rotation is selected. Choices for distinct matched edges are independent because their occupied gaps are distinct. Their actual gauge differences depend only on that gap's selection bit, not on choices at free rotations.

For ANY such activation choices, let K_E be the selected rotations in matched gaps and let c=|K_E|. Set

    l=1 if c is odd, and l=2 if c is even.

Choose ANY subset A of free rotations V with |A|=l, and put K=K_E union A. Then

    k=|K|=c+l is even, 2<=k<=p-1,
    q=p+2-k satisfies 3<=q<=p.                             (4)

Indeed c<=t=p-2; an even c is at most p-3, while an odd c is at most p-2. This choice includes c=0: two free actual rotations supply nonemptiness and even parity, even when their values are0.

Choose ANY q actual occurrences Q from U as singleton reflection packets, together with all t binary matching packets, one occurrence selected from each. There are C=t+q=2p-k packets, an even number, and the total selected size is C+k=2p. Because matching endpoints are ADJACENT in the reflection subsequence, every outside singleton is outside each pair span, so EVERY such Q gives noncrossing ordered packets. Selected rotations inside matched gaps are allowed and are accounted for by the gauge.

The room q between3 and p, with U of size p+2, will permit a genuine singleton exchange in section5. No unused occurrence is invented.

## 2. Exact ordered product and p-2 switch fact

For any actual even reflection set J and selected rotation set K, the product in its ORIGINAL selected order has coordinate

    d(J)+sum_(r in K)epsilon_J(r)x_r,
    d(J)=sum_(j in J in order)(-1)^(rank_J(j)-1)y_j,
    epsilon_J(r)=(-1)^(number of selected J reflections before r). (5)

This follows by induction from (v,e)(v',e')=(v+ev',ee'). Equivalently, with

    z_j^K=y_j+2 sum_(r in K before reflection j)x_r,

the coordinate is S_K+sum_(j in J)(-1)^(rank_J(j)-1)z_j^K. To verify equivalence without commuting terms, factor the original alternating rotation stretches through conjugations rho_s sigma_y rho_(-s)=sigma_(y+2s); adjacent inverse rotations telescope to the SAME selected product. Even reflection parity then makes the final rho_(S_K) add S_K.

Thus, with fixed matching activation and fixed Q, choosing pair endpoints has attainable coordinate set

    B_Q(K)+sum_(e in E){0,delta_e(Q)},                     (6)

where delta_e(Q) is v_e times the ±1 sign of that packet's reflection rank. The signs depend on Q but NOT on which free rotation set A was selected. Free rotations lie in unmatched gaps, so they affect neither v_e nor the pair spans. The baseline B_Q(K) is the actual product coordinate when choosing the left endpoint of every matching pair and all Q singletons.

For t=p-2 NONZERO binary increments, their sumset is either F_p or exactly

    -n d+{0,...,p-2}d=F_p minus{-(n+1)d},                 (7)

where d!=0, EVERY increment is±d, and n counts the negative signs. Here is the elementary proof: nonzero translation raises a proper nonempty subset's size by at least one; two increments not equal up to sign give four distinct subsums and the other p-4 increments force fullness. If every increment is±d, translating the minus factors gives the displayed p-1-point interval. No classical inverse theorem is imported.

Therefore the packet family avoids the identity EXACTLY when its increments are all±d and

    B_Q(K)=(n_Q+1)d.                                     (8)

This is exact for the specified packet family, not a sufficient condition for global word avoidance.

## 3. Uniform local step restriction across all activations

Suppose w has no original-order identity2p selection. The same deductions apply if it merely fails EVERY GS2/GS3 packet in the earlier exact actual residual. For each matching E above, there is d_E!=0 such that

    union_(e in E) V_e subset{d_E,-d_E}.                  (9)

**Proof.** Take ANY tuple v_e in V_e. It is actually realizable in the matched gaps; choose any free set A as in(4) and any Q of the required size. If two tuple values are not equal up to sign, their signed packet increments also are not equal up to sign, and (7) gives an actual identity2p selection. Thus every tuple must share a nonzero step up to sign.

Fix one reference tuple and call its common step d_E. For any e and any alternative v in V_e, change only that coordinate of the tuple. Since t=p-2>=5, another coordinate remains equal to±d_E. The changed tuple must still be parallel up to sign, forcing v in{d_E,-d_E}. This proves(9) for ALL possible activation choices, not just the chosen reference tuple. QED.

A concrete consequence, with NO assumption that rotations had a paired alphabet: for every matched occupied gap its actual rotation value obeys

    x_e in{0, ±d_E/2, ±d_E}.                              (10)

To derive this, if a_e=0, nonemptiness gives x_e!=0 and2x_e=±d_E. If a_e!=0 then a_e=±d_E. If a_e+2x_e=0, x_e=-a_e/2. If both values are nonzero, they either agree (x_e=0) or are opposites (x_e=-a_e). These cases exhaust the literal two-element set(3). Equation(10) concerns MATCHED rotation gaps for THIS matching; it is not silently applied to unmatched rotations or arbitrary words.

## 4. Actual same-cardinality K exchanges force free-rotation rigidity

Fix any activation tuple v_e and its K_E,c,l,k,q from section1. Fix ANY Q subset U of size q. Let J_Q be the reflection set consisting of each matched pair's LEFT endpoint and all Q singleton occurrences. Its size C is even. Formula(5) gives

    B_Q(K_E union A)=B_Q(K_E)+sum_(r in A)epsilon_(J_Q)(r)x_r. (11)

Here B_Q(K_E) denotes this scalar baseline at the fixed J_Q; its selected total count need not itself be2p, which is immaterial for the algebraic identity. The full K_E union A DOES have the required count.

For fixed Q, the signed increments in(6) and their negative count n_Q do not depend on A. By global avoidance and(8), the sum over A in(11) must be the SAME scalar for EVERY A subset V with |A|=l. Put v_r=epsilon_(J_Q)(r)x_r.

* If l=1, equality of all one-element sums forces all v_r equal.
* If l=2, equality of all two-element sums, with |V|>=3, again forces all v_r equal: compare pairs{a,b} and{a,c}, then use another pair to include a. This is equality in F_p, not an inequality or a count of feasible tuples.

Consequently, for EVERY such Q,

    epsilon_(J_Q)(r)x_r is the SAME value for all r in V.  (12)

This is the cross-K bridge. The actual free rotation sets have the SAME cardinality l, the same matched activation and SAME actual reflection baseline, so no hidden change in target size or filler signs occurs.

It follows that either:

* ALL free rotations have value0; or
* ALL free rotations are nonzero and lie in ONE pair{c_E,-c_E}, c_E!=0.

A mixture of identity and nonidentity free rotations, or two nonzero free values not equal up to sign, produces an actual identity selection by the contrapositive of(7)-(12). This is a positive all-value criterion, not an assumed restriction of the problem.

## 5. Different Q exchanges force one-arc concentration

Assume now that the free rotations are nonzero. Consider two distinct actual free rotations r,s, and the cyclic arc I from r to s, with the complementary arc I^c. Suppose there is an unmatched reflection u in U∩I and another v in U∩I^c.

Because |U|=p+2 and3<=q<=p, choose ANY q-1 other unmatched reflections Q_0 disjoint from{u,v}; enough actual occurrences exist. Set

    Q=Q_0 union{u},  Q'=Q_0 union{v}.

Both are allowed filler sets of the SAME cardinality q, with matching activation and l fixed. The parity of selected baseline reflections between r and s differs by ONE between J_Q and J_(Q'). The matching LEFT endpoints contribute the same fixed count in that arc. Thus

    epsilon_(J_Q)(r)/epsilon_(J_Q)(s)
      =-epsilon_(J_(Q'))(r)/epsilon_(J_(Q'))(s).           (13)

This relative-sign statement is invariant under the common cyclic frame, because both selected reflection counts are even. It may equivalently be checked on a cut just before r, in its unmatched gap.

But(12) for Q and Q' separately requires each displayed ratio to equal x_s/x_r. Since both actual values are nonzero and p is odd, (13) makes this impossible. Therefore no pair of free rotations can separate U into two nonempty pieces.

List all m>=3 free rotations cyclically. If U occupied TWO different arcs between consecutive free rotations, the endpoints of either occupied arc would split U into a nonempty part and a nonempty complement, just excluded. Hence:

    ALL p+2 unmatched reflections lie in ONE arc
    between consecutive free rotations.                  (14)

This does NOT say all reflections, all rotations, or every constant block lies in that arc. Matched pair endpoints and matched-gap rotations are still present elsewhere. In the all-zero free-rotation branch the division by x_r is not licensed, and no concentration conclusion is asserted there.

## 6. Complete necessary reduction and positive contrapositives

For EVERY actual matching E of p-2 possible-switch edges in a hypothetical avoider (or in the earlier actual residual failing all GS2/GS3 families), the following have now been DERIVED:

1. There exists a nonzero d_E with every possible nonzero activation difference in one pair±d_E, not merely one selected-K tuple.
2. Every matched rotation belongs to{0,±d_E/2,±d_E} by the explicit local cases.
3. Either all unmatched rotations are identities, OR they are all in one nonzero opposite pair±c_E AND all unmatched reflection occurrences U lie in one free-rotation arc.
4. For every matching activation and every permitted Q the full exact critical offset(8) remains REQUIRED; the magnitude/concentration consequences do not replace it.

For a fixed matching in the nonzero branch the GLOBAL actual rotation alphabet is therefore contained in

    {0, ±d_E/2, ±d_E, ±c_E},                              (15)

with c_E not claimed related to d_E. In the zero branch replace±c_E by0. This is a NECESSARY consequence at that matching, not a new premise, an unrestricted inverse theorem, a finite-group solution, or a classification claiming that all such words avoid. Different matchings may yield different d_E and c_E.

If an actual word has some matching E violating ANY of these proved requirements, the preceding constructive choices/exchanges provide an identity2p selection by contraposition: otherwise(7)-(14) would all hold. That existential implication is written over ACTUAL choices; it is not an unadmitted search result or a claim that a relaxed scalar profile is feasible.

## 7. Exact scope and still-unproved full target

The two-free-control paper addressed p-1 raw matchings. This paper converts the universal selected-K constraints at a p-2 raw matching into actual local-step, free-value and reflection-location rigidity. It does not add another counted problem or pretend to be a strict new class disjoint from the earlier GS provider: all its positive choices are instances of those already proved packet mechanisms. Its scientific role is the new cross-K/cross-Q STRUCTURAL input on the remaining whole-word class.

The full assigned residual still includes:

* raw possible-switch matching number <=p-3, where the present p-2 matching need not exist;
* the critical p-2 raw class with all free rotations0;
* the critical p-2 raw class with nonzero free pair and one-arc concentration, retaining ALL exact offsets for every activation/filler/matching, arbitrary matched pair placements, zero-valued rotations where allowed, and all earlier OLD/REF/SEL/IPGEN/DS3 failures.

No claim is made that any such residual member exists or is an avoider, nor that an individual matching's profile is a full-word normal form. Full MIX, every actual R=p+1 word, unrestricted D_(2p) and all finite groups remain NOT_PROVED.

The next load-bearing task is to turn the one-arc concentration/step restrictions OR the all-zero-free branch into an actual permitted mixed/reflection-only selection or a literal old caller, while retaining the lower raw-matching branch. No rotation values are silently discarded in that task.

The graph, group law, actual packet bridge and elementary cyclic-translation fact are the only direct mathematical inputs here. Old S(p)/Lev/classical trust remains solely in the inherited residual comparison, and prior process errors are not cured. This snapshot needs its own actual separate reconstruction and parent check; earlier peer returns do not cover it. No program, enumeration, solver, compilation, old checker/job, model CLI, Lean/kernel, human review or novelty certification occurred.
