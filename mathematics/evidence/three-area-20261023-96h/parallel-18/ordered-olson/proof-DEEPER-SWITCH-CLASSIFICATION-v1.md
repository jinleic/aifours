# First deeper Olson obstruction: exact p-3 switch classification and two-singleton constraints

Observed before exclusive creation: **2026-10-23T14:23:39-0700 PDT**. Owner MathOlson-2, math-2. **CANDIDATE written extension, not whole-band closure.** This resumes the SAME primary problem after the assigned Sun8 peer reconstruction. It addresses the first deeper o_K=p+4 branch left by the earlier gauge-switch manuscript; it does not open another problem or silently impose a rotation alphabet.

## 0. Exact predecessor and present claim

Predecessor `proof-GAUGE-SWITCH-AND-CRITICAL-LADDER-v1.md`, SHA256 **cfc59821268165483319fdbc69f01c5f626904b3332f13076e33f97dc29c9f75**, supplies the exact selected-K gauge product, elementary binary translation growth, actual ordered packets, and odd-component obstruction. Its complete actual MathShor reconstruction has observed SHA256 **3e7218d0cb6f7c5028650fcafdc47ccf79d2c30f74220f13cabafed1bdae4f8e**; it found no substantive defect at its stated scope. Parent review is separate. Neither that peer return nor this extension is a formal, human, novelty or full-target acceptance.

Throughout p>=7 is any prime. The word is ACTUAL N=4p-1, R=p+1, F=3p-2 over D_(2p), with unrestricted values including identity rotations. For ANY actual even rotation set K, 2<=k=|K|<=p+1, put C=2p-k and

    S_K=sum_(r in K)x_r,
    z_j^K=y_j+2 sum_(r in K before actual reflection f_j)x_r.

The predecessor's proved identity is

    product of K and actual even reflection list j_1<...<j_C
      =rho_(S_K+sum_nu(-1)^(nu-1)z_(j_nu)^K).             (G)

Its proof telescopes conjugations and never commutes selected terms. Scalar switch sumsets below are licensed only after (G). Actual cyclic cuts require recomputing the labels and restoring the same original indices by conjugation.

**Claim supplied here:** a COMPLETE classification of proper binary sumsets with p-3 nonzero increments. They have either one common step up to sign or one exceptional double-step, with every missing residue explicit. Applying this exact inverse to actual packets adds necessary restrictions in the first deeper matching branch, at EVERY even K/cut. With all rotations selected, the two remaining singleton choices force an explicit pair-difference restriction inside every unused gap, not merely an entropy bound.

This is elementary finite-field additive reasoning, not a claimed new classical inverse theorem or strict new OLD-provider coverage. Historical ARC/ETA overlap and all old residual trust remain unchanged. No S(p), Lev, EGZ, Davenport, index-one or Cauchy-Davenport theorem is needed in the new proof; the elementary lemmas are proved below. No scientific program is used.

## 1. Equality under cyclic translation

Let A be a nonempty proper subset of F_p and d!=0. Translation by d is a single cycle of length p on F_p. Its directed edges are x→x+d.

**Lemma E1.** If |A union(A+d)|=|A|+1, then

    A=u+{0,1,...,L-1}d, L=|A|.                            (1)

**Proof.** Because A+d has size |A|, the number of elements in (A+d) minus A is exactly1. This is the number of directed edges from A to its complement in the d-cycle. Decomposing the nonempty proper A into its maximal consecutive occupied stretches in that cycle, each stretch has exactly one such outgoing edge. Thus there is exactly one occupied stretch, proving (1). Conversely any such proper stretch has exactly one outgoing edge and grows by one. QED.

**Lemma E2 (unique one-growth direction).** If A is an arithmetic interval of step d and length 2<=L<=p-2, and e!=0 satisfies |A union(A+e)|=L+1, then e in{d,-d}.

**Proof.** Translate and scale to A={0,...,L-1}, d=1, and write e=r with 1<=r<=p-1 as an integer representative. Directly counting the two possible overlap intervals on the cyclic representatives gives

    |A intersect(A+r)|=max(0,L-r)+max(0,L-(p-r)).          (2)

The union has size L+1 exactly when this overlap is L-1. If both summands in (2) are positive, their sum is 2L-p<=L-2, because L<=p-2. If only the first is positive, equality L-1 forces r=1. If only the second is positive, it forces r=p-1. If neither is positive it cannot equal L-1. Thus r=±1, giving e=±d. QED.

The upper limit p-2 is essential: an interval of p-1 residues grows by one under every nonzero translation, so no such direction rigidity is asserted there.

## 2. Four-point parallelogram equality

**Lemma P4.** Let a,b!=0 with b notin{a,-a}. Suppose {0,a,b,a+b} is a four-term arithmetic interval of step d!=0 in F_p. Then one of a,b lies in{d,-d} and the other in{2d,-2d}.

**Proof.** The four points are distinct. Write their set as u+{0,d,2d,3d}. The original opposite pairs {0,a+b} and {a,b} have equal sums. In a four-term progression the outer pair and inner pair have equal sums, whereas the two other pair partitions have sums differing respectively by4d and2d. These differences are nonzero for p>=7. Thus outer/inner is the UNIQUE equal-sum pair partition. If the point0 is at progression position j in{0,1,2,3}, its opposite a+b is at position3-j, leaving a,b at the other two positions. Subtracting position j gives respectively

    {a,b} in {{d,2d},{-d,2d},{d,-2d},{-d,-2d}}.

This is exactly the claim. QED.

## 3. COMPLETE p-3 binary inverse with exact missing residues

Let t=p-3, and let d_1,...,d_t be ANY nonzero residues. Put

    U={0,d_1}+...+{0,d_t}.

A nonzero translation raises the size of a nonempty proper subset by at least one: otherwise invariance under its length-p translation cycle forces fullness. This is the predecessor's elementary Lemma T and its proof is the same directed-cycle observation used above.

**Theorem I3.** U is proper IF AND ONLY IF it has one of the following two increment types.

**Type I — one step:** for some d!=0, EVERY increment is ±d. Let m count its negative increments. Then

    U=-md+{0,...,p-3}d,
    F_p minus U={-(m+1)d, -(m+2)d}.                       (3)

Thus |U|=p-2.

**Type II — one double-step:** for some d!=0, exactly ONE increment is ±2d and the other p-4 increments are ±d. Let m count the negative ordinary increments, and let eta=1 if the exceptional increment is -2d and eta=0 if it is +2d. Put q=m+2eta. Then

    U=-qd+{0,...,p-2}d,
    F_p minus U={-(q+1)d}.                               (4)

Thus |U|=p-1.

If neither type holds, U=F_p. No assumption on ordering or distinctness of the increments is imposed; repeated increments and either sign are allowed.

**Proof of necessity.** If all increments are equal up to sign, Type I holds. Otherwise choose a,b among them with b notin{a,-a}. Their binary sumset S={0,a,b,a+b} has four distinct elements. There are t-2=p-5 remaining nonzero increments. If U is proper, it has size at most p-1, while repeated translation growth gives size at least4+(p-5)=p-1. Therefore its size is exactly p-1, and EVERY one of those p-5 additions, from the initial four-point set, raises size by EXACTLY1. A growth of at least2 at any one step would already force fullness at the end.

Since p>=7, p-5>=2, so choose one remaining increment d. Lemma E1 applied to the first addition shows that S is a four-term arithmetic interval of step d. Lemma P4 implies that a,b are one ±d and one ±2d. After this first addition the sumset is still an interval of step d, now of length5. Before every subsequent addition its length is between5 and p-2 inclusive. Each such addition grows by one, so Lemma E2 forces its increment to be ±d. Adding ±d keeps an interval of the same step, translated if needed. Induction proves that ALL the remaining increments are ±d. Together with a,b this is exactly Type II: one exceptional double-step and p-4 ordinary steps. This proves the exhaustive necessity.

**Proof of sufficiency and missing residues.** In Type I replace each {0,-d} by -d+{0,d}. The p-3 ordinary binary factors give the interval in (3), whose p-2 residues are distinct and whose missing two residues are precisely those displayed.

In Type II the negative factors translate by -qd. The remaining positive-factor sumset is

    {0,...,p-4}d+{0,2d}
      =({0,...,p-4} union{2,...,p-2})d
      ={0,...,p-2}d.

The integer intervals overlap because p-4>=3. Its p-1 residues are distinct and miss exactly -d. Translation proves (4). Both types are proper, completing both directions. QED.

For a fixed scalar B, the EXACT zero-avoidance rules are therefore

    Type I: 0 notin B+U IFF B in{(m+1)d,(m+2)d};
    Type II:0 notin B+U IFF B=(q+1)d.                     (5)

The d↦-d normalization is harmless. In Type I it exchanges the two offset choices. In Type II q changes to p-2-q, leaving (q+1)d unchanged modulo p. No ambiguity is hidden in the offset condition.

## 4. Actual ordered packet theorem at every mixed count

Fix ANY actual K of even size 2<=k<=p+1. Select C=2p-k ordered noncrossing reflection packets, one actual occurrence from each, together with K. Let exactly t=p-3 packets be binary pairs of occurrences and let the remaining

    C-t=p+3-k

packets be actual singletons. Every packet's members precede every member of the next packet. Selected rotations may occur inside a pair's span, because their effects have already been captured by (G).

Write a_i for the singleton or the first occurrence of packet i, b_i for the second occurrence of a binary packet, and put

    B=S_K+sum_(i=1)^C (-1)^(i-1)z_(a_i)^K,
    delta_i=(-1)^(i-1)(z_(b_i)^K-z_(a_i)^K)  for binary i. (6)

The exact attainable coordinate set is B+sum{0,delta_i}. Assume all binary increments are nonzero.

**Theorem DS3 (deeper-switch positive criterion and exact packet obstruction).** These packets yield an original-order identity-2p selection unless their signed increments and B satisfy one of the two COMPLETE obstructions in (5), at the Type I/II classification of Theorem I3. Conversely either obstruction in (5) excludes zero from this particular packet family's attainable coordinate set.

**Proof.** Apply the complete sumset theorem to (6). If the increment list is neither classified type, it fills F_p; otherwise the displayed missing residues give exactly (5). Formula (G) turns inclusion of zero into the identity on exactly k+C=2p ACTUAL increasing-original-index positions. This proves the positive implication and the precisely scoped packet-family converse. It does not claim that the particular packet family exhausts all selections of the word. QED.

Thus the missing ingredient is not an unproved arbitrary sumset inverse: the inverse and ALL its offsets are supplied. The unresolved part is whether the actual whole-word residual can satisfy all these constraints simultaneously.

## 5. Application to the first deeper odd-component branch

For each K, let nu_K and o_K be the actual unequal-gauge adjacency matching number and odd path-component count from the predecessor. At F=3p-2,

    nu_K=(3p-2-o_K)/2.

The preceding candidate showed a surviving word must have o_K>=p+2. Its first deeper value o_K=p+4 is EXACTLY nu_K=p-3.

For ANY actual matching of p-3 adjacent reflection pairs whose gauge differences are nonzero, there are

    F-2(p-3)=p+4

outside reflection occurrences. The required p+3-k singleton fillers are nonnegative and at most p+1 because k>=2; enough actual outside occurrences therefore exist. Adjacency IN THE REFLECTION SUBSEQUENCE ensures that no chosen filler crosses a pair, regardless of intervening selected rotations. Every choice of those fillers gives an actual packet system from section4.

Consequently every hypothetical all-selection avoider, and every actual residual word outside DS3 coverage, must satisfy the following for EVERY even K, EVERY actual cut, EVERY p-3 matching, and EVERY allowed filler choice:

1. The signed pair differences have Type I or Type II. In particular a matching with two or more independent exceptional directions beyond the one allowed double-step solves the word.
2. The exact B of the actual ordered filler system obeys (5); a cardinality-only condition is not sufficient.

This applies whenever a matching of size p-3 exists, not just when it is maximum. It therefore also supplies additional tests in the old critical branch without claiming duplicate independent problem/results counts. If nu_K<=p-4, this packet construction is not asserted available; that deeper branch remains.

## 6. Two-singleton restrictions with all rotations selected

Now take K to be all p+1 rotations, so C=p-1. Fix any p-3 adjacent unequal-gauge pairs (a_i,b_i), i=1,...,t, in order, and abbreviate z_j=z_j^K, S=S_K. There are p+4 unused reflection occurrences and exactly TWO singleton fillers are needed.

Set the ordinary pair-only baseline and signed increments

    P=sum_(i=1)^t (-1)^(i-1)z_(a_i),
    delta_i=(-1)^(i-1)(z_(b_i)-z_(a_i)).

Gap j, 0<=j<=t, contains the unused reflection occurrences after the first j pairs and before the next pair. Suppose both singleton fillers u<v are chosen in the SAME gap j. The two singleton insertions change every later packet rank by TWO, so all pair signs and all delta_i remain exactly as displayed. The new baseline is

    B_j(u,v)=S+P+(-1)^j(z_u-z_v).                         (7)

This formula follows from the actual order: the two filler ranks are consecutive j+1,j+2. No actual selection is reordered.

### 6.1 Type I: a complete two-value ordered difference obstruction

For Type I let m count the negative delta_i relative to d and define the two-element set

    E_j=(-1)^j( {(m+1)d,(m+2)d}-S-P ).                    (8)

The DS3 family with these two fillers avoids identity EXACTLY when

    z_u-z_v in E_j.                                      (9)

Thus if the word avoids all identity selections, EVERY ordered pair u<v of unused occurrences in gap j must obey (9).

The following elementary structural consequence is fully proved, not a guessed normal form.

**Lemma D2.** Suppose a finite ordered residue list v_1,...,v_L has v_i-v_j in a fixed TWO-element set E for every i<j, over F_p with p>=7.

* If 0 notin E, then L<=3. At L=3 the consecutive differences are equal to a nonzero c and E={c,2c}.
* If 0 in E, write E={0,c}, c!=0. The list uses at most two values. If two occur, it consists of one constant block of a followed by one constant block of b, with a-b=c. A return to the earlier value is impossible.

**Proof.** If zero is absent, all list values are distinct. For three indices1<2<3, their differences a=v_1-v_2, b=v_2-v_3 and a+b=v_1-v_3 lie in E. If a and b were the distinct two elements of E, their sum could equal neither one without the other being zero. Thus a=b=c and the other element is2c. For four indices, applying this to1,2,3 and2,3,4 forces all three consecutive differences equal c, while the first-fourth difference3c would have to lie in{c,2c}, impossible at p>=7. Hence L<=3.

If E={0,c}, three distinct values in increasing-index order would require consecutive differences c and c but total2c notin{0,c}. Thus at most two values occur. Once a precedes b with a-b=c, any later return to a would give b-a=-c notin{0,c}. Hence the two values occur in the displayed block order. The converse block property directly satisfies all pair differences. QED.

Applied to (8)-(9), each unused gap is therefore EITHER of length at most3 when 0 notin E_j, OR has at most two monotonically ordered constant gauge blocks when 0 in E_j. This is a necessary condition on ACTUAL leftover labels for EVERY matching in Type I. It does not assert that arbitrary words have such a decomposition or that this condition by itself realizes an avoider.

### 6.2 Type II: a single forced ordered difference

In Type II use q from Theorem I3 and put

    c_j=(-1)^j((q+1)d-S-P).

All choices of two fillers in the same gap avoid identity EXACTLY when

    z_u-z_v=c_j  for EVERY actual u<v in that gap.         (10)

If the gap has at least THREE unused occurrences, (10) forces c_j=0 and all their gauge labels equal: for u<v<w, differences u-v and v-w are both c_j, while u-w is2c_j and also c_j. If the gap has exactly two occurrences, their single ordered difference must be c_j. Gaps with zero or one unused occurrence supply no same-gap two-filler condition.

These are exact tests for the specified same-gap packet families. Fillers in DIFFERENT gaps are still retained in the full quantified DS3 condition (5)-(6), not silently discarded after these convenient corollaries.

## 7. Entire updated residual and the exact remaining obstruction

Keep the actual B2_p from the first manuscript, with its ENTIRE B1 complement, every prior caller/grammar failure, every original value/order/gap/block parity, every admissible mixed count and every old trust qualification. Let DS3_p denote actual words admitting some actual cut, some even nonempty K and some packet system satisfying the positive side of Theorem DS3. Define

    B3_p=B2_p minus DS3_p.                                (11)

This is an ACTUAL-word complement of proved sufficient classes. No strict new B2 member covered by DS3 has been exhibited, no residual nonemptiness is claimed, and no classical novelty/SOTA claim follows from the inverse lemma.

Every actual B3 member has all prior constraints AND the complete Type I/II and offset constraints at p-3 switches over EVERY K/cut/matching/filler. In the all-rotation branch, its same-gap leftovers obey section6, while every different-gap filler system must still obey the exact general condition. These are necessary restrictions; there is no converse, relaxed-feasibility certificate, all-word normal form or actual avoiding example.

**Still unproved:** universal MIX on the whole actual B3. The uncovered obstruction includes (a) nu_K<=p-4 where p-3 matchings may not exist, and (b) simultaneous compatibility of the exact critical and deeper profiles over all K/cuts. Neither Theorem I3 nor an individual matching's restricted gap profile closes that universal compatibility problem. We do not silently change the target to a common rotation pair, the all-rotation branch, a selected prime, a short word or a local obstruction.

The old S(p) secondary-statement, Lev statement-level and classical ancestry qualifications travel only in the inherited residual comparison; this proof introduces none of them as direct premises. Historical errors and process limitations are not cured. The full R=p+1 band, unrestricted D_(2p) and all-finite-groups ordered Olson remain NOT_PROVED.

## 8. Verification boundary and next bounded obligation

The load-bearing finite-field inverse, equality classification, missing residues, actual packet bridge, counts and two-filler formulas are complete written arguments above. No scientific execution, parameter loop, enumeration, solver, compilation, old runtime/checker, Lean/kernel or model CLI was performed. A fresh SHA pin and actual independent reconstruction/parent review are needed before acceptance; the earlier peer review covers ONLY the earlier pinned manuscript, not this new extension.

The next consequential whole-word obligation is to use the constraints across DISTINCT choices of K, rather than proving another single-packet inverse in isolation: either force a forbidden switch/offset for some actual K/cut, or derive an actual reflection-only/SEL/other literal old caller from universal profile compatibility. Until that cross-K bridge is proved, all the remaining actual words stay in the target.
