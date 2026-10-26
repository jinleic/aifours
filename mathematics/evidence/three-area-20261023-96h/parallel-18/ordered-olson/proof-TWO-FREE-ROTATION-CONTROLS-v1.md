# Cross-K selection: two free rotation controls and an actual flat-gap obstruction

Observed before exclusive creation: **2026-10-23T14:32:28-0700 PDT**. MathOlson-2, math-2. **CANDIDATE written theorem, unrestricted rotation values at R=p+1.** This attacks the cross-K bridge left by the preceding packets, not a new scientific problem. No scientific execution is used. Whole MIX, unrestricted prime-dihedral Olson and all finite groups remain NOT_PROVED.

## 0. Actual whole-band setting and source boundary

For ANY prime p>=7, let w be an ACTUAL word of length4p-1 over

    (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1),

with R=p+1 rotation occurrences and F=3p-2 reflection occurrences. Every value, including x=0, is retained. List the reflection occurrences in cyclic order f_1,...,f_F, with values y_j, indices modulo F. Gap j is the ACTUAL cyclic gap from f_j to f_(j+1).

Initially assume every such gap contains 0 or 1 rotation. This is an actual type-pattern hypothesis, not a normalization. It holds on the entire current lower-band residual by the accepted literal Theorem P: if ANY gap contains at least two rotations, then F+sum floor(n_j/2)>=3p-1 and P solves the original-order identity2p problem already. This paper's Q=0 theorem below does not use P; the extension to arbitrary type patterns uses only that exact old accepted P interface with both mandatory errata, already read in the source freeze. No S(p), Lev, EGZ, Davenport, index-one or normal-form theorem is imported into the new selection argument.

Because R=p+1 and every gap has capacity one, there are EXACTLY p+1 DISTINCT occupied rotation gaps. A zero-valued rotation still occupies its own gap and remains available as an actual selected position.

The selected-K gauge and scalar switch method were developed in `proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md`, pin cfc59821268165483319fdbc69f01c5f626904b3332f13076e33f97dc29c9f75, with the actual MathShor written reconstruction at pin3e7218d0cb6f7c5028650fcafdc47ccf79d2c30f74220f13cabafed1bdae4f8e. The needed gauge and binary-growth arguments are restated/proved in section2 so this new theorem does not hide an unavailable selected-term reordering premise. ARC/ETA are historical mechanism baselines, not claimed new here.

## 1. A rotation-independent graph on ACTUAL reflection occurrences

Define a cyclic graph M(w) with the F reflection occurrences as vertices. Its edge j between f_j and f_(j+1) is retained exactly when

    y_(j+1)-y_j !=0
      OR gap j contains a rotation rho_x with x!=0.       (1)

Call this a **possible switch edge**. It may be made a nonzero selected-K gauge difference by choosing whether its singleton rotation is selected. This statement is proved constructively below, with parity and nonempty K handled rather than assumed.

An edge is absent exactly when its two reflection values are EQUAL and the actual gap is either EMPTY or contains the identity-valued rotation rho_0. Call these absent edges **flat gaps**. An absent gap and an identity-valued rotation are NOT identified as occurrences; they simply have the same zero-difference property in this graph.

Let nu_M be the maximum matching cardinality of this cyclic graph, on actual reflection vertices. No solver or executable matching calculation is a premise.

## 2. Exact elementary selection tools, with original order

For ANY selected actual rotation set K, let k=|K|, S_K=sum_(r in K)x_r and, on any chosen cut word,

    z_j^K=y_j+2 sum_(r in K before f_j)x_r.

For ANY even selected reflection list j_1<...<j_C, its ORIGINAL-order product together with K equals

    rho_(S_K+sum_(a=1)^C(-1)^(a-1)z_(j_a)^K).           (2)

**Proof of (2).** Let u_0,...,u_C be the rotation sums in the actual selected word before, between and after its selected reflections. With t_a=u_0+...+u_(a-1), the product equals

    (rho_(t_1) f_(j_1) rho_(-t_1)) ...
    (rho_(t_C) f_(j_C) rho_(-t_C)) rho_(S_K).

Adjacent inverse rotations telescope to the original ordered product. The group law gives rho_t sigma_y rho_(-t)=sigma_(y+2t); an even reflection product has alternating coordinate and parity+1, so the final rho_(S_K) adds S_K. This proves (2) without commuting any selected terms.

For an actual adjacent reflection pair across gap j, its gauge difference is precisely

    D_j^K=y_(j+1)-y_j
           +2x_j [the rotation in gap j is selected],    (3)

where the second term is absent for an empty gap. Selected rotations in OTHER gaps change both endpoint prefixes equally, or neither, and do not change (3).

If A is a nonempty proper subset of F_p and d!=0, then |A union(A+d)|>=|A|+1: otherwise A would be invariant under a nonzero translation, whose length-p orbit is all F_p. Repeating this fact shows that p-1 NONZERO binary increments fill F_p.

Accordingly, suppose K is even and nonempty, 2<=k<=p+1, and p-1 disjoint adjacent reflection pairs have nonzero gauge differences. Put C=2p-k. Add C-(p-1)=p+1-k singleton reflection packets outside these pairs. There are F-2(p-1)=p outside occurrences, enough for that nonnegative number. Adjacent pairs in the reflection subsequence cannot cross an outside reflection singleton, even if selected rotations lie between the two reflections of a pair.

Choosing one endpoint per pair and every fixed singleton gives C actual reflections in a fixed packet order. Formula (2) yields a scalar option set B+sum_(i=1)^(p-1){0,d_i}, with every d_i!=0 (the packet's sign only multiplies it by ±1). The binary growth argument fills F_p, regardless of B. Some actual choice therefore has product rho_0, with exact selected length C+k=2p and even reflection parity.

## 3. The two-free-controls theorem

**Theorem FC.** If M(w) has a matching of size at least p-1, then w has an identity2p subword in increasing ORIGINAL index order. More specifically, an even selected rotation set K with

    2<=|K|<=p-1

can be chosen constructively; this is not confined to the all-rotation branch.

**Proof.** Choose EXACTLY p-1 disjoint possible-switch edges from a matching. At most p-1 of the p+1 occupied rotation gaps are matched edges. Hence at least TWO actual rotation occurrences lie in unmatched gaps. Reserve two of them as free controls r_0,r_1. This count is on ACTUAL distinct occupied gaps; it uses the Q=0 condition and does not assume any rotation value is nonzero.

For every matched edge, choose its singleton rotation status as follows:

* If the two endpoint reflection values differ, leave that gap's rotation unselected, if it has one. Formula (3) is then their nonzero raw difference.
* If the endpoint reflection values agree, the edge's presence in M(w) means its gap contains an actual NONZERO rotation. Select that rotation. Formula (3) is then2x!=0, because p is odd.

For matched empty gaps the first case necessarily applies. These choices independently make ALL p-1 matched differences nonzero. Let c be the number of rotations selected by these forced choices; 0<=c<=p-1. Initially leave every other rotation unselected.

Now use the TWO free controls, whose gaps are not matched:

* If c>0 is even, leave both free controls unselected.
* If c is odd, select r_0 and leave r_1 unselected.
* If c=0, select BOTH r_0 and r_1.

The resulting K is nonempty and even. Its cardinality is at most p-1: a positive even c already is at most p-1; an odd c is at most p-2; and the zero case gives2. Selecting a free control, including a possible rho_0, does not affect ANY matched difference because it lies in another actual gap. In particular the two controls solve both parity and nonemptiness, not just parity.

Cyclically cut the word in the unmatched gap containing r_0. No chosen matching pair crosses this cut, so its reflection pairs are disjoint adjacent pairs in the resulting ordinary reflection order. Their gauge differences remain nonzero by (3), calculated anew on that cut. Section2 then selects EXACTLY2p actual positions with identity product.

Finally write the original word AB and the cut word BA. If P_A,P_B are the selected products in the two original portions and P_B P_A=1, then P_A P_B=P_B^(-1)(P_B P_A)P_B=1. Thus the SAME actual positions have identity in increasing ORIGINAL order. QED.

This is the explicit cross-K bridge: the rotation set is constructed only AFTER the actual matching is chosen. No fixed signed multiset is silently substituted for all K, and no unknown Boolean optimization is being called a proof.

## 4. EXACT elimination of the all-K p-1-switch predicate

Let P1(w) mean that for some actual cyclic cut and some even nonempty K, an ordered reflection-packet system has p-1 binary packets with NONZERO gauge increments and sufficient fixed singleton packets to give exact total2p, as in the first manuscript's GS1. Packets may have nonadjacent endpoint occurrences, but their spans are noncrossing in that cut's reflection order.

**Theorem EQ.** On the whole actual Q=0 band,

    P1(w)  IFF  nu_M>=p-1.                               (4)

**Proof.** The backward direction is FC and section2. For the forward direction take each binary packet's ordered endpoints a<b. Their nonzero gauge difference telescopes as

    z_b^K-z_a^K=sum_(j=a)^(b-1) D_j^K.

Thus some adjacent edge INSIDE that packet span has D_j^K!=0, hence is a possible switch edge by (1)/(3). Different packet spans are disjoint in reflection order, so choosing one such adjacent edge per binary packet gives p-1 disjoint edges, a matching in M(w). This uses only actual spans on the chosen cut; the same edges are valid in the cyclic graph. QED.

Therefore the all-K/all-cut p-1-switch failure is not merely bounded below by a convenient raw statistic: it is EXACTLY the raw matching obstruction nu_M<=p-2. This is exactness for this SUFFICIENT PACKET PREDICATE only. It does NOT characterize all identity selections, the p-2/p-3 tests, full MIX, or avoiders.

Because B2 already subtracts all GS coverage, (4) is an explicit structural equivalent of one inherited failure predicate; it is NOT a claim of an additional independently counted coverage class or a newly shrunken B2. Its value is the proved cross-K choice, which eliminates an unresolved universal selected-rotation quantifier for this component.

## 5. Rotation-independent odd-component and flat-gap consequences

If M(w) is the full cycle, F=3p-2 is odd and its matching number is floor(F/2)=(3p-3)/2>=p-1, so FC solves w. Otherwise delete its absent flat-gap edges and let L_1,...,L_q be the vertex lengths of the resulting PATH components, including isolated vertices. Their matching number is

    nu_M=sum floor(L_i/2)=(F-o_M)/2,

where o_M counts odd component lengths. This follows by matching successive vertices in each path, which attains floor(L_i/2).

Consequently every hypothetical identity2p avoider, and every actual word outside P1, has

    o_M>=p+2.                                            (5)

For a cycle with at least one deleted edge, its number of path components is EXACTLY its number of deleted edges, not deleted-edges+1. Hence there are at least p+2 ACTUAL flat gaps. This is stronger than quoting the fixed-cut zero-edge bound without doing the cross-K/cyclic argument.

Let k_F be the number of maximal CYCLIC CONSTANT reflection blocks in the ORIGINAL ACTUAL word; rotation occurrences separate blocks even when the neighboring reflection values agree. Let Z_0 be the number of identity-valued rotations rho_0 whose immediate predecessor and successor REFLECTION occurrences in cyclic reflection order have the same value. The Q=0 condition means these neighbors are the literal two neighboring reflections around that singleton rotation.

The number of flat gaps is exactly

    T_flat=F-k_F+Z_0.                                    (6)

Indeed every constant reflection block of length ell supplies ell-1 empty equal-reflection gaps, totalling F-k_F. The remaining flat gaps are exactly the Z_0 occupied identity-rotation gaps with equal endpoint reflections. These two kinds are disjoint actual gaps; no occurrence is identified or omitted.

Equations (5)-(6) therefore give the necessary original-word bound

    k_F<=2p-4+Z_0.                                      (7)

Equivalently, any Q=0 band word with k_F>2p-4+Z_0 is solved by FC. This is an arbitrary-rotation-value positive criterion, with zeros retained through the ACTUAL Z_0 term.

For optional bookkeeping define on the SAME actual constant blocks

    H=sum floor(ell_i/2),
    o_F=number of ODD constant blocks,
    e_F=number of EVEN constant blocks,
    kappa=p-1-H.

These are not terminal-NF parameters. The exact actual identities are

    F=2H+o_F,  k_F=o_F+e_F,
    o_F=p+2kappa,
    T_flat=2H-e_F+Z_0.

Thus the same necessary bound can be written

    2kappa+e_F<=p-4+Z_0.                                (8)

No kappa range or converse is presumed; (8) is derived on actual word data only.

### Consequential scoped corollaries

1. **All values, H=0:** every band word with H=0 is solved. Here k_F=F=3p-2, while Z_0<=R=p+1, so (7) would require 3p-2<=3p-3, impossible. This retains arbitrary identity rotations and nonconstant reflection runs. It is not a terminal-NF exclusion.
2. **Explicit zero-free corollary, not an ambient restriction:** if all rotations happen to be nonzero, Z_0=0 and any remaining word must satisfy2kappa+e_F<=p-4. In particular kappa>=(p-3)/2 is solved. This corollary does NOT discard zero-containing words: their full condition is (7)/(8).
3. At p=7, for words satisfying that explicit zero-free premise, a residual also retaining the old trust-relative o_F>=p+2 must have kappa=1 and e_F<=1. The lower bound kappa>=1 here uses ONLY that separately stated historical residual import; the new matching proof does not acquire S(p)/Lev through this comparison. This is a necessary remaining actual parameter band, not a proof of residual feasibility, all-word classification or full D_14 Olson.

These are consequences of ONE cross-K matching theorem and are not counted as distinct scientific problems or independent discoveries. Strict coverage beyond EVERY historical provider is not certified.

## 6. What remains, without replacing the whole target

The entire current B3 actual residual, including every original mixed count, value, order, old caller failure, p-2 critical offset/ladder and p-3 deeper constraints, remains the target. In that residual the GS1 failure can now be expressed EXACTLY as the rotation-independent actual graph condition

    M(w) has at least p+2 odd path components,
    equivalently nu_M<=p-2,

with at least p+2 flat gaps and (7)/(8). This gives a real cross-K structural ingredient, not an unrestricted normal form or a sufficient realization condition.

Universal MIX is STILL unproved on words with this graph obstruction. Neither (7) nor (8) asserts that these words are avoiders; they can have reflection-only, p-2, p-3 or other literal old selections. No length4p-1 avoiding word, B1/B2/B3 nonemptiness, full prime-dihedral or all-group theorem is claimed. The older critical insertion family remains already covered and is not being reproved here.

The next consequential obligation is no longer to guess a selected K for large matching graphs: FC does that. It is to use the at-least-p+2 flat gaps and their component ordering, together with the exact lower-switch offset constraints, to force an actual permitted selection or a literal old caller in the remaining small-matching graph class. Arbitrary rotation values INCLUDING0 and every original mixed selection size stay in that obligation.

## 7. Verification and trust

This manuscript gives a complete written actual-position construction and a converse for its precisely named packet predicate. No scientific program, matching solver, enumeration, code check, compilation, old job/checker, Lean/kernel or model CLI was run. Metadata hashes attest only bytes. The earlier peer review covers the earlier pinned proof, not FC/EQ or these corollaries; this snapshot needs its own actual separate reconstruction and parent check before acceptance.

New FC/EQ proofs are self-contained group-law and elementary finite-field arguments. The full-band handling of non-Q=0 words explicitly imports the old accepted P statement. Historical S(p) secondary-statement, Lev statement-level, classical/transitive proof limitations, unpromoted SEL/IPGEN status, and prior process deviations remain unchanged wherever the historical residual is compared. Correctness, scope, novelty, significance and full-target resolution remain separate.
