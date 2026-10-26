# Full critical raw-matching branch: an actual ordered identity2p selection

Actual returned before-creation clock: **2026-10-24T04:08:52-0700 PDT**. Owner MathOlson-2, math-2. **COMPLETE WRITTEN CANDIDATE FOR NEW RECONSTRUCTION; NOT ACCEPTED.** Exact interface and pre-freeze informal exposure are recorded in `selection-critical-branch-v1.md`; no preregistration or blind-discovery claim is made. No scientific execution, enumeration, solver, arithmetic interpreter, CLI or nested agent.

## 1. Literal whole-branch theorem, not another necessary refinement

Fix ANY prime p>=7. Let w be ANY ACTUAL word in D_(2p), with

    N=4p-1, R=p+1 rotations, F=3p-2 reflections,
    (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1).

Assume its rotations are nonzero and every actual cyclic reflection gap contains0 or1 rotation. These hypotheses are the already supported P/Z1 reductions of the ENTIRE current band, not assumptions on its initial unrestricted rotation alphabet.

Define the raw possible-switch graph on its F reflection occurrences in cyclic order: the edge between two consecutive reflections is present iff their values differ OR their gap contains a nonzero rotation.

**Theorem C (candidate full-branch actual selection).** If this graph contains a matching of p-2 edges, then w has EXACTLY2p actual positions, in increasing ORIGINAL index order, with product identity.

This is stronger than merely excluding a proposed scalar profile: it applies to EVERY actual word with the stated matching, and hence covers the ENTIRE critical branch nu_M=p-2 in the consolidated residual, with every value/order/block pattern retained. A matching larger than p-2 contains one of exactly that size as well. The proof below supplies a genuine original-word selection by finite endpoint choices; no program or unproved sumset classification is a premise.

For a word in the exact residual R_final, REF already excludes a reflection-only identity selection. The theorem's selection must therefore be MIX with an even positive rotation count. The proof nevertheless handles a possible k0 test honestly as an actual reflection-only family, not by applying the earlier k>=2 GS statement out of domain.

The lower raw-matching branch nu_M<=p-3 is NOT covered or discarded. Full R=p+1, other rotation counts, unrestricted D_(2p) and all finite-group Olson are not claimed solved.

## 2. Exact matching blocks, activations and all admissible packet counts

Choose a matching E of EXACTLY

    t=p-2

raw edges. It has disjoint adjacent reflection pairs. At most t of the p+1 occupied rotation gaps are matched, so at least THREE actual rotations are in unmatched gaps. Let V be ALL these free rotation occurrences and m=|V|>=3. Every x_r for r∈V is nonzero. Let U be all unmatched reflection occurrences; then

    n=|U|=F-2t=p+2.                                      (1)

Cut the word in a free rotation gap. No matching pair crosses this cut; all following block and occurrence orders are ordinary linear orders on this cut word. Original-cut restoration is supplied in section10.

For matched pair i, let its actual endpoint values be a_i,b_i in that order. If its gap contains a rotation rho_(x_i), choose a status eta_i∈{0,1}; if empty, put eta_i=0 and x_i=0. Choose the statuses so that

    v_i=b_i-a_i+2eta_i x_i !=0.                           (2)

This is always possible independently in every matched gap: if b_i!=a_i take eta_i=0; otherwise the possible edge has x_i!=0 and eta_i=1 gives2x_i!=0. Fix ONE such activation tuple for the rest of the proof; no uniform-activation theorem is assumed. Let c=sum eta_i be its actual selected matched-gap rotation count, so0<=c<=p-2.

For ANY subset A⊂V and ANY subset Q⊂U satisfying

    k=c+|A| is even, 0<=k<=p+1,
    |Q|=n-c-|A|=n-k>=1,                                 (3)

select the fixed matched rotations, the free rotations A, every reflection in Q, and ONE endpoint of every matched pair. Its total ACTUAL selected length is

    c+|A|+t+|Q|=t+n=2p.                                  (4)

The selected reflection count is t+|Q|=2p-k, hence even; in particular every admissible |Q| is odd. Pair adjacency in the REFLECTION SUBSEQUENCE ensures that U and free rotations are outside every pair span. The only possible other selected factor inside such a span is that pair's own singleton rotation. Thus every endpoint choice is a genuine original-order subset; occurrences are distinct and never reused.

## 3. The exact missing-coordinate midpoint rule

For a fixed activation, the selected factors inside pair i multiply locally as follows:

    choose left:  sigma_(a_i) rho_(eta_i x_i)
                  =sigma_(a_i-eta_i x_i),
    choose right: rho_(eta_i x_i) sigma_(b_i)
                  =sigma_(b_i+eta_i x_i).                 (5)

An absent rotation means rho0 in these equalities only as the identity PRODUCT; no fictitious selected occurrence is added. Equation(5) groups consecutive SELECTED factors inside their actual block. It does not reorder factors elsewhere.

Write L_i=a_i-eta_i x_i and R_i=b_i+eta_i x_i. Their difference is v_i!=0, and their midpoint is

    h_i=(L_i+R_i)/2=(a_i+b_i)/2,                          (6)

independent of the activation. Since p is odd, division by2 is well defined in F_p.

For fixed admissible A,Q, order all t pair packets and |Q| singleton reflection packets, with the free rotations A at their actual positions. The rank of every selected-reflection packet is independent of its endpoint choice. Direct induction on the actual group law therefore gives the option COORDINATE set

    B(A,Q)+sum_(i=1)^t {0,delta_i(Q)},
    delta_i(Q)=alpha_i(Q)v_i,
    alpha_i(Q)=(-1)^(number of preceding reflection packets). (7)

Free rotations do not flip reflection parity, so alpha_i does not depend on A. Rotations inside a pair were already grouped in(5); free rotations lie outside those spans. The coordinate is affine in reflection labels because their selected parities/order are fixed. Every option product is a ROTATION because the total reflection count is even.

Define a VIRTUAL midpoint template by replacing each whole matched pair block, including its possible rotation, by the single reflection sigma_(h_i). Keep U as optional reflection occurrences in their original relative order and V as optional free rotation positions outside those blocks. Let Pi(A,Q) be its ordered product with all t midpoint reflections, U-subset Q and V-subset A. It is a rotation at every admissible pair in(3). By affine dependence on each reflection label, its coordinate is exactly

    B(A,Q)+(1/2)sum_i delta_i(Q).                         (8)

The virtual template is NOT asserted to be an actual subword or an avoidance-preserving normalization. Its purpose is to identify the omitted actual option PRODUCT. A virtual IDENTITY is never mapped back as a witness. A virtual NONIDENTITY will force an actual identity among the options in(7).

### Elementary p-2 binary fact, fully proved

A nonzero translation d raises the cardinality of a nonempty proper subset S⊂F_p by at least1. Otherwise S+d=S, and iterating the length-p translation cycle would force S=F_p.

For t=p-2 nonzero increments, if two a,b are not equal up to sign, their four subsums0,a,b,a+b are distinct. The other p-4 nonzero increments then fill F_p by the preceding growth fact. Otherwise every increment is±d for some d!=0. If s are negative, their sumset is

    -sd+{0,1,...,p-2}d,

which misses EXACTLY the single residue-(s+1)d. Moreover

    (1/2)sum_i delta_i
       =((p-2-2s)/2)d=-(s+1)d in F_p.                   (9)

Thus either the actual option coordinate set(7) is all F_p, or it is F_p minus the coordinate(8) of the VIRTUAL midpoint product. The first case already gives an actual identity2p selection. In the second case an actual identity exists whenever Pi(A,Q) is NOT identity. These are exact field/group statements over actual options, not finite evaluations or an imported inverse theorem.

## 4. Contradiction hypothesis and the virtual coherence identity

Assume, for contradiction, that w has NO actual identity2p selection. Then the fixed nonzero tuple v_i must be equal up to sign: if it were not, any admissible packet system in(3) would fill F_p as just proved. Such admissible systems certainly exist by the standard counts below. Fix the resulting d!=0.

For EVERY A,Q obeying(3), signs alpha_i preserve equality up to sign, so the second case of the binary fact applies. Since no actual option can equal identity, its unique omitted product must be the identity itself. Therefore

    Pi(A,Q)=1  for EVERY admissible A,Q.                  (10)

This is a conditional consequence of the hypothetical failure, not a definition of arbitrary residual words. All the remaining proof uses(10) to force an ACTUAL admissible family whose virtual omitted product is nonidentity, yielding the contradiction by section3.

## 5. Standard free cardinality: signed free values and one-arc location

Put

    ell=1 if c is odd; ell=2 if c is even,
    k0=c+ell; q0=n-k0.

Then

    2<=k0<=p-1,  3<=q0<=p=n-2,                           (11)

and both k0 is even and q0 odd. There are m>=3 free rotations, enough for every ell-subset. The upper bounds follow because an even c<=p-2 is at most p-3; an odd c is at most p-2. For EVERY Q⊂U of size q0, (10) holds for EVERY A⊂V of size ell.

For ANY odd-size Q, let H(Q)∈F_p be the coordinate of Pi(empty,Q), retaining all midpoint reflections but NO free rotation factors. Define

    epsilon_Q(r)=(-1)^(number of midpoint/Q reflections before r).

The semidirect-product formula gives

    coordinate Pi(A,Q)=H(Q)+sum_(r∈A)epsilon_Q(r)x_r.       (12)

This equation is algebraic for any A, even when that A,Q pair is not an actual target-count family. Its use as an actual witness is restricted to(3).

For fixed standard Q, (10),(12) make the sum over A constant for every ell-subset. If ell1, all signed free values are equal immediately. If ell2, choose a third free occurrence and compare pairs sharing it; m>=3 forces the same conclusion. Thus for each standard Q,

    epsilon_Q(r)x_r is the SAME NONZERO value for all r∈V. (13)

Nonzeroness uses the actual zero-free hypothesis; it is not inferred from the nonempty cardinality of A.

Suppose unmatched reflections u,v∈U lie on opposite cyclic arcs between two free rotations r,s. Choose q0-1 other U occurrences disjoint from u,v. This is possible because n-2=p and q0-1<=p-1. Replacing u by v gives two actual standard Q sets of the SAME cardinality. The relative reflection-prefix parity between r,s flips: midpoint reflections are fixed, while precisely one selected U reflection moves across that arc. Hence

    epsilon_Q(r)/epsilon_Q(s)
      =-epsilon_(Q')(r)/epsilon_(Q')(s).

But(13) requires BOTH ratios to equal x_s/x_r. This is impossible in odd characteristic, since these actual free values are nonzero. Therefore no pair of free rotations separates U into two nonempty pieces. Listing consecutive free rotations cyclically shows that

    ALL U lies in ONE arc between consecutive free rotations. (14)

If two such arcs contained U occurrences, the endpoints of either occupied arc would provide exactly the excluded split. No claim is made that U is consecutive among all reflection occurrences; matched midpoint factors may be interspersed there.

## 6. The SAME nonzero signed free value for every ODD Q

The cut was chosen in a free rotation gap. The open arc in(14) contains no free rotation, so that cut does not split U into two linear pieces. Every free rotation position is before ALL U or after ALL U in this linear order. For ANY odd subset Q⊂U, its contribution to the reflection-prefix parity at a free rotation is therefore either0 or the same odd parity1. The midpoint-prefix count is fixed.

Consequently epsilon_Q(r) is independent of Q whenever |Q| is odd, including different odd cardinalities. Choose one standard Q and call the common nonzero value in(13) v. Then

    epsilon_Q(r)x_r=v!=0
    for EVERY r∈V and EVERY odd Q⊂U.                      (15)

This step is stronger than assuming unsigned free values coincide: it fixes the actual ordered PREFIX SIGNS across all the odd Q sizes needed next. It uses the proved one-arc location and does not commute selected rotations through reflections.

Substituting standard |A|=ell in(10),(12),(15) yields

    H(Q)=-ell*v  for EVERY q0-element subset Q of U.        (16)

We now exploit constancy over ALL subsets of this ONE interior cardinality, not merely a single fixed profile.

## 7. Constant-size product coherence for optional involutions

**Lemma OI.** Consider any group word of fixed factors and N ordered optional involutions s_1,...,s_N. If its selected product, keeping all fixed factors, is the SAME for EVERY q-element optional subset at one fixed1<=q<N, then after transporting the fixed factors all optional involutions are identical. If q is odd, the selected product is therefore the SAME for EVERY odd-size optional subset, of any cardinality between1 and N.

**Proof.** Write the word as

    F0 s1 F1 s2 ... sN FN,

where each F_j is the product of the fixed factors in that stretch, possibly empty. Put g_j=F0...F_(j-1), g=F0...FN and tau_j=g_j s_j g_j^(-1). Exact telescoping gives, for ANY optional subset Q,

    selected product=(product_(j∈Q increasing)tau_j) g.    (17)

This identity is valid in a NONCOMMUTATIVE group: adjacent inverse fixed prefixes cancel to exactly the intervening fixed stretches. No optional factor is moved past another optional factor.

Fix adjacent optional indices i,i+1. Choose q-1 other indices outside them; N-2>=q-1 makes this possible. Compare the constant products for that common subset plus i or plus i+1. In the transported order the common selected prefix/suffix are the same, because no other optional index lies between i and i+1. Left/right cancellation in the group therefore gives tau_i=tau_(i+1). Thus ALL tau_j equal one involution tau, since conjugation preserves being an involution.

For any odd optional subset the transported product is tau^odd=tau. It agrees with the product at the original odd q; multiplication by the SAME fixed tail g in(17) preserves equality. This proves the lemma. It does not assert equality between even and odd cardinalities. QED.

Apply OI to the virtual template defining H(Q), with midpoint reflections as the fixed factors and U's actual reflections as the optional involutions. Equation(16) is equality of group products rho_(-ell*v), not just of an unbound scalar statistic. Counts(11) ensure1<=q0<n and q0 odd. Therefore

    H(Q')=-ell*v for EVERY ODD subset Q'⊂U,               (18)

including cardinalities q0-2 or q0+2 when present. The lemma transports fixed factors by conjugation; it does NOT claim the original unmatched reflection labels themselves are all equal.

## 8. Two complete cardinality cases produce an actual witness

### Case E: c even, ell=2

Choose A'=empty and ANY Q' of size q0+2=n-c. This is an odd number at most n and positive. The actual selected rotation count is k'=c, even and between0 and p-3. Hence this is a legitimate family(3), with total ACTUAL selected size exactly2p.

By(18) its virtual midpoint product has coordinate

    H(Q')=-2v!=0.

This contradicts(10), and by the exact missing-coordinate rule it yields an actual endpoint selection of product identity and length2p.

The boundary c0 is INCLUDED: then k'0, Q'=U and the actual packet family selects exactly2p reflections. We used the direct elementary option proof in section3, not the earlier GS theorem outside its k>=2 domain. On the consolidated residual this would contradict REF failure; it is a valid actual identity selection in the broad word theorem.

### Case O: c odd, ell=1

Choose ANY THREE free rotations as A', possible because m>=3, and ANY Q' of size q0-2>=1. This size is odd. The actual rotation count k'=c+3 is even and at most p+1, since c<=p-2. Also |Q'|=n-c-3, so the actual total remains EXACTLY2p as in(3)-(4), including the endpoint k'=p+1,|Q'|=1.

Equations(12),(15),(18) give its virtual midpoint coordinate

    H(Q')+3v=-v+3v=2v!=0.

Again(10) is contradicted and section3 supplies an ACTUAL endpoint selection of product identity and length2p. The term3v is the sum of THREE ACTUAL signed rotation contributions from(15), not an unsigned commutation of free terms.

These two parity cases exhaust every possible matched activation count c, and both return an actual original-word target selection. The hypothetical absence of such a selection is impossible. This proves Theorem C on the chosen cut word. QED modulo the explicit original-cut restoration below.

## 9. Exact scope of the new closure

The proof is a WHOLE-branch solution, not an additional necessary restriction. It covers EVERY zero-free Q=0 band word with a raw matching of p-2 edges. It imposes no paired rotation alphabet, all-odd block, normal form, equal-reflection reservoir, numerical prime cutoff or preselected arrangement. The one-arc and signed-value properties were derived ONLY under the contradiction hypothesis and then destroyed by multi-cardinality coherence.

In the supported consolidated residual, matching>=p-1 was already GS1-covered and Z1/P already dealt with original identity rotations and repeated occupied gaps. Theorem C would now close the ENTIRE remaining critical branch nu_M=p-2. Since REF is excluded there, its actual witness is necessarily mixed. It does not assert that every hypothetical scalar profile is realizable, or infer a word theorem from a necessary normal form.

**The lower raw branch nu_M<=p-3 remains ENTIRELY open under all its original data and applicable old/GS/DS3 failures.** No feasibility/nonemptiness assertion for that branch, full R=p+1 closure, other-R conclusion, full D_(2p) result or every-finite-group theorem follows from this manuscript. Further count corollaries and compositions are not silently promoted before this new proof has its actual checks.

## 10. Original order, dependencies and review boundary

The selected endpoint factors in(5) are grouped inside disjoint actual blocks on a cut that crosses no matching pair. For original w=AB and cut BA, write P_A,P_B for the selected products in the two original portions. Identity in cut order means P_B P_A=1; then P_A P_B=P_B^(-1)(P_B P_A)P_B=1. The SAME actual chosen positions therefore have identity in increasing ORIGINAL index order, with cardinality unchanged. This completes Theorem C as originally stated.

Theorem C itself uses only the displayed group law, actual counts, elementary nonzero-translation growth in F_p, division by2 in odd characteristic, and the FULLY PROVED optional-involution coherence lemma. It does not import S(p), Lev, EGZ, Davenport, index-one, a normal form, a historical computation or an external entropy argument. Applying it to the historical ENTIRE residual retains all old imports solely where that residual was previously defined; P/Z1 are called at their supported actual interfaces, not upgraded by this new theorem.

The gauge/arc/binary-growth mechanisms are prior internal baselines already credited in earlier packets. The new midpoint/coherence/multi-cardinality closure needs its OWN actual separate reconstruction and parent full-body review. The earlier v11 return does NOT certify these bytes. No kernel/human/novelty/strict-new-provider-coverage claim is made and no scientific program or parameter experiment was run. All snapshots are immutable; any correction must use a numbered successor/addendum.
