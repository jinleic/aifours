# Lower band: a complete signed selector, reflection-only obstruction and inverse-pair insertion closure

Observed `/bin/date` before this exclusive creation: **2026-10-22T22:52:45-0700**. This is a before-creation observation, not an exact physical write time. Written work began only after the WHOLE `PARENT-STEP0-ACK-v1.md` was read. This manuscript is also the substantive post-ACK checkpoint: the complete results and exact remaining word class are below. **CANDIDATE partial results; the entire lower band and unrestricted ordered Olson remain NOT_PROVED.** No scientific computation or external/model call is a premise.

## 1. Frozen target, exposure and imports

Fix ANY prime p>=7. Words are ACTUAL words of length 4p-1 in

    D_(2p)={(v,e):v in F_p,e in{+1,-1}},
    (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1).

The immediate band has **R=p+1 rotations and F=3p-2 reflections**, not the mistaken reflection-count label in the original scope. Every conclusion selects EXACTLY 2p increasing ORIGINAL positions. No nonzero, opposite-pair, rigidity, block-parity, zero-free or unit-language condition is imposed on the whole band. The target is every actual word of `RES^C` in this band, at exactly the Step0 OLD trust. Nothing here advances to R=p+2.

Known parent exposure, not independent discovery: (i) the reflection word in §2; (ii) the Q=0 observation in §3; (iii) adjacent inverse-pair insertion in §6. The selector/parity-allocation proof below was written after ACK; no blind/preregistered novelty claim is made.

The only OLD theorem directly called by the new word proofs is the literal accepted **Theorem P**: for odd prime p, N<=4p-1, F>=1, if

    F+sum_t floor(n_t/2)>=3p-1,

where n_t are the actual cyclic rotation-gap lengths between consecutive reflection occurrences, there is an original-order identity-2p selection. I read WHOLE the immutable `mathematics/evidence/six-lane-20261016/olson/proof-theoremP.md`, the current `review/olson-TheoremP-import-closure-parent-verdict-v1.md` and both complete parent errata v1/v2 under the 96h run. Degree bounds, selected-prefix signs and original-cut restoration keep those corrections; historical finite checks/prime-power/sharpness remarks are not premises.

The complete supplied `proof-EXTENDED-UNITS-AND-SIX-BLOCK-OBSTRUCTION-v1.md` (called **X** below; whole SHA256 `8d6d8a7a9e93d03186d3a31236516ae39d400af33d19c5584a9905f1e3ab9871`) is the load-bearing CANDIDATE companion for its explicit original GEN leaf/rule proofs. It was read whole in Step0 and must accompany §6 if those leaf certificates are used. It is not an accepted OLD interface or an omitted-body waiver. The new insertion rule and the global certificate implication are proved here. No S(p), Lev, index-one, INV-P, RGR or classification theorem is used in the selector or insertion proofs. Those imports remain solely at the original declared trust when the old residual is compared in §7.

All eight old parent scientific outputs remain excluded. This is not a clean global-provenance, independent-family, human, Lean or novelty certificate.

## 2. Complete reflection-only obstruction, and what old P did/did not certify

Let the integers 1,...,p-1 denote their distinct residue classes, in the displayed order, and put

    C_p = sigma_0^(2p-1) sigma_1 sigma_2 ... sigma_(p-1).

**Proposition 2.1.** No selection of exactly 2p reflections in C_p has product identity, for every prime p>=7.

**Proof covering ALL selections.** Such a selection uses t of the final distinct nonzero reflections, for some 1<=t<=p-1: zero-only selection is impossible because there are only 2p-1 zero reflections. Write their selected values as integers

    1<=b_1<b_2<...<b_t<=p-1.

The other 2p-t selected reflections are zero-valued and precede them. The selected reflection count is even, so the product is a rotation. The group law gives its exponent

    sum_(j=1)^t (-1)^(2p-t+j-1) b_j.

For even t this is -L with

    L=(b_2-b_1)+(b_4-b_3)+...+(b_t-b_(t-1)).

Every summand is positive and the disjoint integer intervals lie between b_1 and b_t, so 1<=L<=b_t-b_1<=p-2. For odd t the exponent is again -L, now with

    L=b_1+(b_3-b_2)+(b_5-b_4)+...+(b_t-b_(t-1)).

These positive disjoint intervals lie between 0 and b_t, so 1<=L<=b_t<=p-1. Thus in every possible selection L is an integer strictly between 0 and p. Its negative is nonzero in F_p. The product cannot be identity. This argument exhausts all choices of the zero and nonzero occurrences. QED.

C_p has length 3p-2, no rotations and all rotation gaps empty. It is a sharpness obstruction to lowering P's reflection-only threshold by one, **not** a length-4p-1 word, not a lower-band avoiding word, and not a `RES^C` witness.

The immutable P proof's Remark 1 already records the reflection-coset upper bound and a finite-composite sharpness remark. It does not supply this uniform all-selection argument there; the current accepting P verdict explicitly disclaims sharpness. Thus this proposition is a complete written verification of the exposed elementary lower family, not a new accepted P theorem, a new priority result, or proof that no older literature/source contains it.

More importantly, §5 proves that **every insertion of p+1 arbitrary rotation letters into this very reflection word is solved**. Therefore its reflection-only obstruction does not survive as an obstruction to the actual mixed band.

## 3. Exact first reduction on the whole band

**Proposition 3.1.** Every band word having an actual cyclic reflection gap with at least two rotation letters is covered by OLD P. Consequently every actual band word outside that literal OLD provider has

    Q=sum_t floor(n_t/2)=0, hence every n_t is 0 or 1.

**Proof.** Here F=3p-2. If any n_t>=2, Q>=1 and F+Q>=3p-1, so literal P applies at the actual length 4p-1. If Q=0, each of its nonnegative integer summands is zero, equivalently n_t in{0,1}. Conversely a positive Q supplies P. These are actual reflection-to-reflection gaps, not maximal-block scalars inferred through a normalization. QED.

This is the parent-exposed reduction, not a whole-band proof. It says nothing about reflection values or a common rotation pair. At this count SR2 is outside its explicit R>=2p-1 domain and is neither applied nor negated.

## 4. A complete uniform singleton-selector word theorem

### 4.1 Additive prefix lemma, with its exact role

**Lemma 4.1.** Given ANY p residues x_1,...,x_p in F_p, either some nonempty even-size subset sums to zero, or for EVERY b in F_p some odd-size subset sums to b or -b. The proof in fact supplies a contiguous segment of this residue list in either branch.

**Proof.** Put s_0=0 and s_j=x_1+...+x_j. If two prefix sums with distinct indices of the same parity coincide, the segment between them is a nonempty even-size zero sum. Otherwise the sets

    E={s_j:j even}, O={s_j:j odd}

both have (p+1)/2 distinct elements, because p is odd and the indices run from 0 to p. For any b, E and b+O have total size p+1>p, so they intersect. Thus s_e-s_o=b for an even index e and an odd index o. The segment between the two indices has odd size; its sum is b if e>o and -b if e<o. QED.

This additive lemma is not by itself a word-selection theorem. Its choices become actual ordered word selections only through the next parity allocation.

### 4.2 Actual equal-reflection parity allocation

**Lemma 4.2.** Fix 2p-1 ACTUAL occurrences of one reflection sigma_a, and an even number k of distinct actual rotation occurrences, 2<=k<=p+1. List these k rotations in cyclic order. Prescribe their prefix-reflection signs, each +1 or -1, with either no sign changes or exactly two sign changes around the cycle. Suppose every arc where a sign change is prescribed contains at least one of the fixed sigma_a occurrences. Then one can select exactly 2p-k of the fixed sigma_a occurrences so that these signs are realized, up to the initial cyclic frame. If the prescribed signed rotation sum is zero, the selected k rotations and these 2p-k reflections give an ORIGINAL-order identity-2p selection.

**Proof.** Let z_i count the fixed sigma_a occurrences in the arc from selected rotation i to selected rotation i+1, cyclically. These k arcs partition the fixed occurrences, so sum z_i=2p-1. Let eta_i be 1 on a prescribed sign-change arc and 0 otherwise. The hypothesis says z_i>=eta_i. In each arc the possible selected reflection counts are

    eta_i, eta_i+2, ..., M_i,
    M_i=z_i-[z_i not congruent eta_i mod2].

Let delta count the mismatches in brackets. Since sum z_i is odd and sum eta_i is even, delta is odd. Since k is even and delta<=k, delta<=k-1. Therefore

    sum M_i=2p-1-delta>=2p-k.

The minimum total is sum eta_i, either 0 or 2. The desired total 2p-k is even and at least p-1>=6, so it lies between that minimum and sum M_i, with the correct parity. Sums of the displayed bounded step-2 intervals contain every even total between their minimum and maximum: after subtracting the minima and dividing by two, successively fill the nonnegative integer capacities until the required total is reached. Thus suitable actual counts c_i exist. Choose that many of the fixed reflection occurrences in each actual arc.

Start the cyclic frame at a selected rotation prescribed +1 (all applications below have one). Passing through c_i selected reflections changes its sign exactly by eta_i, as required. There are an even number of selected reflections overall. Their own coordinate contributions alternate +a,-a and sum to zero; unselected letters have no effect. The selected product coordinate is precisely the prescribed signed rotation sum, hence zero. The total selected size is k+(2p-k)=2p and its reflection parity is even.

Finally write original w=AB and the cut word BA. If the selected products in the two original portions are P_A,P_B, identity in the cut order means P_B P_A=1, and then P_A P_B=1 by conjugation. The SAME actual selected positions therefore give identity in increasing ORIGINAL order. QED.

### 4.3 Singleton selector

**Theorem SEL (CANDIDATE, self-contained).** Let w be ANY actual band word. Suppose for some a it has at least 2p-1 occurrences of sigma_a and contains an actual cyclic consecutive triple

    sigma_a rho_b sigma_a.

Then w has an original-order identity-2p selection. Every rotation value, including b=0, is allowed. No condition is imposed on the other reflection values, other gaps or type pattern.

**Proof.** Fix 2p-1 of the sigma_a occurrences, including the two distinct neighbors of the displayed rho_b. There are exactly p OTHER actual rotations. Apply Lemma 4.1 to their residues in any fixed actual order.

If it gives a nonempty even-size zero-sum subset, select those k rotations, not rho_b, and prescribe every sign +1. There are no change arcs, so Lemma 4.2 applies directly.

Otherwise choose an odd-size subset of the other rotations whose sum is c in{b,-b}. Select these and rho_b; their total k is even and 2<=k<=p+1. Prescribe sign +1 on every selected other rotation. If c=-b prescribe +1 on rho_b; if c=b prescribe -1 on rho_b. When b=c=0 either choice is valid; choose +1. The prescribed signed rotation sum is zero.

There are now either no change arcs or just the two adjacent to rho_b. Each of those two arcs contains one of its fixed neighboring sigma_a occurrences: the triple is ACTUALLY consecutive, so no other rotation can intervene between rho_b and either of those neighbors. Both neighbors were included in the fixed set. Lemma 4.2 applies and supplies exactly 2p original positions with identity product. QED.

This is a uniform ACTUAL-word criterion, not an unordered-to-word inference. The separate parity-allocation proof is precisely what licenses the additive subset choices. No claim is made that SEL is disjoint from all earlier OLD, TILE, GEN or deletion coverage, or that a previously uncovered word has been located.

## 5. Every mixed insertion into the exposed critical reflection word is covered

**Corollary 5.1.** For EVERY p>=7 and EVERY actual insertion of exactly p+1 rotations, with arbitrary values and arbitrary placements, into C_p from §2, the resulting correct-length word has an original-order identity-2p selection. Cyclic cuts of this statement are allowed by the proved conjugation argument.

**Proof.** The reflection subsequence has exactly 3p-2 letters. If any reflection gap has at least two rotations, Proposition 3.1/P solves it. Otherwise every gap has at most one rotation.

Inside the consecutive reflection-subsequence block of 2p-1 copies of sigma_0, there are 2p-2 internal gaps. Among the total 3p-2 cyclic reflection gaps, only p are not such internal gaps. With p+1 rotations and capacity at most one in each gap, at least one internal sigma_0-to-sigma_0 gap contains a rotation. It is the actual triple sigma_0 rho_b sigma_0. Theorem SEL applies. This exhausts every placement and every rotation value. QED.

In particular, the complete negative all-selection result for C_p is a reflection-only method obstruction; it is NOT an obstruction for these actual mixed words. No inserted-word avoider or residual witness is claimed.

## 6. Parent-exposed adjacent inverse-pair insertion: exact proof and word-certificate boundary

### 6.1 Ring and actual options

For an actual selected subset S with even size and even reflection count, let its ordered product be rho_(v(S)) and put

    phi(S)=(v(S),|S|/2 modp) in H=F_p^2.

For consecutive disjoint actual blocks, selected even-reflection products are rotations, so phi adds when their selections are concatenated IN BLOCK ORDER. This does not apply to interleaved products.

Let A=F_p[H], with basis E_(v,h), and J its augmentation ideal. Writing X=E_(1,0), Y=E_(0,1), s=X-1, t=Y-1 gives

    A = F_p[s,t]/(s^p,t^p), J=(s,t), J^(2p-1)=0.

For completeness: X,Y generate the group basis; s^p=t^p=0 in characteristic p. The resulting quotient surjects onto A and both have dimension p^2, so it is an isomorphism. A monomial of total degree at least 2p-1 has one exponent at least p, hence vanishes. No matrix or forbidden experimental output is involved.

A certified block carries an explicit FORMAL sum of actual even-size/even-reflection options,

    theta=sum_S lambda_S E_(phi(S)) in J^d,

whose formal EMPTY coefficient is 1. Coincident basis points are allowed; the collected E_(0,0) coefficient need not be 1.

### 6.2 Exact new closure rule

**Lemma IP.** Insert two ACTUALLY ADJACENT inverse letters g,g^(-1) at ANY gap of a certified block, including either end. The expanded block has an explicit actual option element

    theta_new=theta_old*(1-E_(0,1)) in J^(d+1),

with formal EMPTY coefficient 1. Its options still have even size/even reflection count. If the old depth is at least half the old block length, the new depth is at least half the expanded length.

**Proof.** For each old actual option S, take either its increasing embedded copy alone, with coefficient lambda_S, or that copy together with BOTH new positions, with coefficient -lambda_S. If the old selected products before and after the insertion are A_0,B_0, the second option has product

    A_0 g g^(-1) B_0=A_0 B_0.

The pair is adjacent at this construction step; there is no selected or unselected original letter between its members. This equality does not require the prefix reflection parity to be even. Thus the coordinate v is unchanged and half-size increases by one, giving the displayed factor. In D_(2p), inverse pairs have the same type: rho_x rho_(-x), including x=0, or sigma_y sigma_y. Adding both therefore preserves even reflection count and increases even size by two.

The factor 1-E_(0,1) has augmentation zero, so the ideal depth gains at least one. Only old-empty with the pair absent yields the formal empty choice; its coefficient remains 1. The length/depth assertion follows from adding two positions and one depth. QED.

Repeated use is valid by a FINITE explicit construction tree. A reverse-removal presentation must remove an actually adjacent inverse pair in the CURRENT intermediate word at each step, then reverse those steps; it is not permission to delete a nonadjacent pair or infer an avoidance-preserving normal form. Later insertions may separate a pair from an earlier construction step, but every step's option interpretation was already proved in its own actual word.

### 6.3 Exact extended grammar and its sufficient word theorem

Define IPGEN certificates by the following finite rules, with their full actual option data:

1. the original explicit same-type two-letter, GOOD balanced four-letter, and SIX bases of X §§3/6;
2. consecutive concatenation of certified blocks;
3. the original rotation-wrap rule of X §4;
4. Lemma IP at any gap of a certified block.

There is no new reflection-wrap rule. The GOOD criterion and all SIX coefficients/hypotheses are EXACTLY those of the complete companion X, not arbitrary six-letter half-depth certificates. The original five-rule GEN language is a sublanguage by simply not using rule 4. This is a rule-inclusion claim, NOT a strictness or new-cell claim.

Let IPGEN_p be the ACTUAL band word class for which some actual cyclic cut and one actual-letter omission leaves 4p-2 positions completely partitioned into blocks with such explicit finite certificates. No universal certificate-existence assertion is made.

**Theorem IPGEN (CANDIDATE, relative to X's complete supplied base/old-rule proofs).** Every word in IPGEN_p has an original-order identity-2p selection.

**Proof.** X supplies the explicit actual-option proofs for rules 1–3; Lemma IP proves every new rule instance. Every resulting block has formal empty coefficient 1, all option parities even, and ideal depth at least half its length. Concatenating the root blocks multiplies their elements in J to total depth at least (4p-2)/2=2p-1, so the product is zero.

Expand FORMALLY. The all-empty choice has coefficient 1 at E_(0,0). Since the product vanishes, some NONEMPTY actual option choice with phi=0 must have nonzero coefficient; otherwise that basis coefficient would be 1. Coincident points or cancellation among other formal options do not invalidate existence. The actual selected union has positive even size at most 4p-2 and half-size divisible by p, so its size is exactly 2p. Its even-reflection product coordinate is zero. Omission embedding and the explicit cyclic-conjugation argument of Lemma 4.2 restore the SAME original increasing positions. QED.

This theorem requires the complete current X body for its bases; neither an earlier gate nor a filename can replace it. The nilpotence/global-selection/new-IP arguments are supplied here, not assumed. No use of IPGEN in §7 asserts that every residual word admits its grammar, that any OLD-uncovered member has been found, or that an earlier obstruction proves failure for every cut/tree.

## 7. ENTIRE lower-band remainder and exact first unproved statement

Keep the original actual residual `RES^C_p` exactly as in the whole delivered Step0 and its parent ACK. Define the entire starting band

    B^0_p = {w in RES^C_p : R(w)=p+1}.

Let REF_p mean actual band words with an actual reflection-only identity-2p selection, and SEL_p mean the actual sufficient class in Theorem SEL. The exact remaining band after this manuscript is

    B^1_p = B^0_p minus(REF_p union SEL_p union IPGEN_p).

This is an ACTUAL-word complement. It is not a scalar-feasibility claim, proof of nonempty/empty remainder, or claim that every member is an avoider. REF is an explicit immediate word-selection case, possibly already OLD-covered; it earns no new credit. IPGEN contains original GEN by the complete candidate proof, not by promotion of the old name. All overlaps retain OLD/earlier credit; strict new coverage outside every prior provider has NOT been established.

Every word in B^1 retains the ENTIRE old residual definition/qualifications, every old caller failure, every original cut/omission/unit failure, all value/type/block/gap/order data and all GRX sign patterns/admissible even endpoints. In particular:

* the actual reflection gaps all have length 0 or 1, by literal OLD P and §3;
* the old trust-relative `o_F>=p+2`, recorded zero multiplicity cap, DEL3 eligibility bound, complete EVDEL caller exclusion and conditional no-ABA-center conclusion remain exactly at their recorded trust, not strengthened by overlap;
* SR2's out-of-domain cap is not applied or negated;
* there is no reflection-only identity-2p selection;
* every reflection-value multiplicity is at most 2p-1, since 2p equal reflections alone would supply REF;
* if a value a has multiplicity 2p-1, there is no actual cyclic triple sigma_a rho_b sigma_a. Because gap lengths are 0/1, every gap between consecutive reflection occurrences both equal to sigma_a is consequently EMPTY;
* every actual IPGEN certificate fails; no one selected cut or failed reduction is substituted for this universal certificate failure.

The last two items are the exact new structural restrictions supplied here. All lower reflection multiplicities, mixed/even/odd maximal blocks, arbitrary rotations INCLUDING0, arbitrary nonconstant reflection runs, all genuine empty gaps and all actual orderings outside the proved classes remain. No paired alphabet, normalization, all-oddness or purity is added. Corollary 5.1 removes the exposed critical-reflection insertion family from this remainder, but is not a classification of all reflection-only extremal sequences.

Here is the concrete remaining lemma, with a COMPLETE original-order all-selection interface rather than a guessed local obstruction. For every actual w in B^1_p, one must find:

    1<=h<=(p+1)/2,
    J={j_1<...<j_C} actual reflection positions, C=2p-2h,
    K actual rotation positions, |K|=2h,

such that, writing

    d(J)=sum_(nu=1)^C (-1)^(nu-1) y_(j_nu),
    epsilon_J(r)=(-1)^(#{j in J:j<r}),

one has

    d(J)+sum_(r in K) epsilon_J(r) x_r = 0 in F_p.       (MIX)

**Exactness of this interface.** The displayed group law, by induction along the ACTUAL selected positions, gives exactly this coordinate and reflection parity +1. Therefore any such J,K proves the required original-order conclusion. Conversely ANY identity-2p selection has an even number of selected reflections, hence an even number 2h of rotations. There are only p+1 rotations available, so h is in the displayed range, except possibly h=0. The latter is precisely REF and has been removed from B^1. Thus (MIX), with actual occurrences and these full ranges, exhausts ALL remaining identity-2p selections. Unselected reflections never flip a sign. No multiset ordering, inverse NF composition or relaxed tuple substitution is used.

**UNPROVED:** the universal existence of J,K satisfying (MIX) for every actual word in this ENTIRE B^1. No all-selection avoiding word in B^1 has been produced either. In particular no classification forcing every reflection-only failure into the C_p insertion family is available or assumed. The failure to prove this universal mixed-selection step is the exact remaining blocker, not a no-go theorem or a full-target claim.

## 8. Substantive checkpoint, status and stop

Completed written results: the all-selection reflection-only obstruction; whole-band P/Q reduction; complete prefix/parity selector theorem; all-rotation-value/all-placement coverage of the exposed critical reflection insertion family; exact adjacent-inverse insertion closure and its candidate word-certificate theorem; the ENTIRE updated band and exact remaining mixed-selection lemma.

This completes the mathematical deliverable for this bounded worker round as a CANDIDATE partial/obstruction packet, not a completed band. No R=p+2 work was begun. New derivations stop on creation of this manuscript; remaining actions are only permitted clock/hash/receipt/delivery metadata, then PARK. The parent may check the complete written proofs and retain the remaining lemma; no worker computation, model CLI, nested review, test/build/lint or prohibited old-file mutation is requested or authorized. The required blocked two-family promotion gate and every prior provenance/process qualification remain unchanged.
