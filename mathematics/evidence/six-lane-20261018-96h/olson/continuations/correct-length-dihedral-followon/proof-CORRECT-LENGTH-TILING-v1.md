# Correct-length D_(2p): a self-contained uniform tiling criterion and complete residual

Actual `/bin/date` observation before exclusive creation: **2026-10-22T03:23:06-0700**. Drafting began earlier AFTER Main's explicit delivered-Step0 acknowledgement. Written mathematics only. **CANDIDATE PARTIAL SUFFICIENT THEOREM; FULL UNRESTRICTED TARGET NOT_PROVED.** No actual second-family gate exists. All process qualifications, including the NEW pre-Step0-route-planning PROCESS MAJOR, remain uncured.

## 0. Target retained; source/exposure/notation boundary

The target is EVERY prime p>=7 and EVERY ordered word of EXACT length4p-1 over the actual group D_(2p), selecting EXACTLY2p positions in increasing ORIGINAL index order with identity product. No pair/nonzero/odd-block/B/kappa/purity/gap/o_F/NF restriction is granted. The theorem below supplies a UNIFORM explicit sufficient criterion on that entire ambient domain, not a claim the criterion always holds. Its complement and concrete failed universal upgrade are stated in full. No word class is silently removed from the assignment.

The historical T0 source was read before the proof gate and inspired use of a commutative GROUP ALGEBRA. T0 has only the stated historical single-family boundary in the baseline and is NOT imported as an accepted theorem. Every mechanism used below is freshly proved completely. No P/GRX/PM*/NF/RED/RGR/S(p)/Lev/CT/old-candidate theorem is a premise of this new argument. Their old accepted statements enter only the baseline/credit/residual comparison at exact trust.

**Essential notation distinction:** J below is an IDEAL, not a matrix. The algebra is explicitly A=F_p[(F_p,+)^2], isomorphic to F_p[s,t]/(s^p,t^p), and J=(s,t). A parent objection concerned the DIFFERENT matrix J(a)=[[0,a],[1,0]], whose square is aI and which is indeed not nilpotent for a!=0. That matrix, its eigenvalues, and evaluation of a nonzero field element for s or t are NEVER used here. The precise quotient and proof of IDEAL nilpotence are given in Section2. A residue a in a basis symbol E_(a,h) is a GROUP COORDINATE/EXPONENT, not a substitution of a for a nilpotent variable. No matrix nilpotence claim or numerical-check workaround is made.

All known prior planning/T0 exposure and same-author continuity are disclosed; no independence, strict preregistration, novelty, priority or matched-SOTA claim. This manuscript is not a full original Olson result, which quantifies over all finite groups. It is not an exact-length counterexample either.

## 1. Ordered group products and elementary selection units

Fix an arbitrary prime p>=7. Use

    D_(2p)={(x,e):x in F_p,e in{+1,-1}},
    (x,e)(x',e')=(x+e x',ee'),
    rho_x=(x,+1), sigma_y=(y,-1), identity=(0,+1).

For selected letters in increasing order, multiplication by a next(x,e) adds E*x to the first coordinate and multiplies the current second coordinate E by e. This follows by induction directly from the displayed law. In particular any selection with an EVEN number of reflections has product rho_v for a uniquely determined v in F_p.

For a selection S with BOTH even cardinality and even reflection count, define

    phi(S)=(v(S), |S|/2 modp) in H=(F_p,+)^2.             (1)

The integer |S|/2 is taken BEFORE reducing modulo p. If selections S_1,...,S_m lie in consecutive disjoint position blocks, each having even cardinality and even reflection count, then their selected products are rotations and

    product(S_1 union ... union S_m)=rho_(sum_i v(S_i)),
    phi(S_1 union ... union S_m)=sum_i phi(S_i).          (2)

The union is read in block order, which is exactly the ORIGINAL order in that linear word. We do not reorder interleaved subsets or multiply arbitrary noncommuting block products; each complete chosen block product already has second coordinate+1.

A *unit* below is an ACTUAL consecutive position block together with a finite list of ACTUAL selectable subsets of that block. Every option has even size and even reflection count, and the EMPTY option is distinguished. Formal coefficients of options are in F_p and need not be nonnegative integers. Coefficients are proof weights, not numbers of occurrences or probabilities.

## 2. The EXACT algebra and nilpotence statement

Let A=F_p[H]. Concretely, A has F_p-basis E_(a,h), (a,h) in H, with multiplication

    E_(a,h) E_(b,k)=E_(a+b,h+k), 1_A=E_(0,0).

It is a COMMUTATIVE algebra of dimension p^2 because H is an abelian group of order p^2. Write X=E_(1,0), Y=E_(0,1). Then X^p=Y^p=1_A. Set

    s=X-1_A, t=Y-1_A.

In characteristic p the binomial coefficients strictly between0 andp vanish. Hence

    s^p=(X-1_A)^p=X^p-1_A=0,
    t^p=0.                                               (3)

The map F_p[s,t]/(s^p,t^p) -> A sending the variables to these elements is surjective: X=1+s,Y=1+t generate every basis element E_(a,h)=X^aY^h, using representatives0..p-1. The quotient has basis s^i t^j for0<=i,j<=p-1 and dimension p^2; therefore this surjective linear map between equal finite dimensions is an isomorphism. In particular

    A is isomorphic to F_p[s,t]/(s^p,t^p).                (4)

Let epsilon:A->F_p be the augmentation map epsilon(sum c_g E_g)=sum c_g and let J=ker(epsilon). Under(4), epsilon sets s=t=0, so J=(s,t). Every product of 2p-1 elements of J is a sum of monomials of total degree at least2p-1. In any such monomial either the s exponent is at leastp or the t exponent is at leastp; it vanishes by(3). Thus

    J^(2p-1)={0}.                                       (5)

This is the nilpotence of an IDEAL in the explicit quotient(4), not nilpotence of a nonzero-parameter matrix/operator. The matrix [[0,a],[1,0]] with a!=0 does not satisfy the relations(3) as a proposed image of s; it is not an object in this argument.

Modulo J^2, a basis element has expansion

    E_(a,h)=(1+s)^a(1+t)^h = 1+a*s+h*t modJ^2.           (6)

This is independent of the choice of residue representatives; a,h in the right side are the corresponding elements of F_p. Therefore for theta=sum c_(a,h) E_(a,h),

    theta in J^2 iff
    sum c_(a,h)=0, sum a*c_(a,h)=0, sum h*c_(a,h)=0.      (7)

These are just the constant/s/t coefficients in(4); no external classification or matrix spectral claim is involved.

## 3. A depth-one unit for any two letters of the SAME type

For an actual two-letter RR block rho_x rho_z, the two allowed options are EMPTY and BOTH letters, with phi values(0,0) and(x+z,1). The formal option sum

    theta_RR=1_A-E_(x+z,1) in J                          (8)

has coefficient1 on the EMPTY option.

For an actual FF block sigma_y sigma_t, BOTH letters multiply to rho_(y-t), so

    theta_FF=1_A-E_(y-t,1) in J.                        (9)

These statements allow ANY values, including x=0,z=0,y=t and rotations whose sum is0. The coordinate1 in the second component records the actual selection size2. No reflection block parity, pair alphabet or nonzero assumption is introduced.

Call either of these an allowed *two-unit*, of depth1.

## 4. COMPLETE depth-two criterion for a balanced four-letter block

Consider an actual ordered block B with exactly TWO rotations and TWO reflections. Let x,z be its rotation values in their occurrence order, and y,t its reflection values in their occurrence order. Its even-size/even-reflection options are exactly:

* EMPTY, phi=(0,0);
* its two rotations, phi=(a,1), where a=x+z;
* its two reflections, phi=(b,1), where b=y-t;
* ALL four letters, phi=(c,2), where c is their ACTUAL ordered-product coordinate.

No one-rotation/one-reflection option has even reflection parity. There are no other2letter options of the required parity. All4letters do have even reflection parity. These four actual options are distinct position subsets even when their phi values coincide.

We seek a formal option sum with EMPTY coefficient1,

    theta_B=1_A+u E_(a,1)+v E_(b,1)+w E_(c,2),           (10)

belonging to J^2. By(7), the equations are

    1+u+v+w=0,
    u+v+2w=0,
    a*u+b*v+c*w=0.                                     (11)

Subtracting the first equation from the second gives w=1; hence u+v=-2 and a*u+b*v=-c. This is soluble EXACTLY when

    a!=b OR c=2a in F_p.                               (GOOD)

Indeed:

* If a!=b, take

       w=1, u=(2b-c)/(a-b), v=(c-2a)/(a-b).             (12)

  Their sum u+v=-2 and weighted sum a*u+b*v=-c follow by the displayed numerator identities. Division is only by the stated nonzero field element a-b.
* If a=b and c=2a, take w1,u=-2,v0.
* If a=b and c!=2a, then u+v=-2 forces a*u+b*v=-2a, which cannot equal-c. Thus NO option sum of form(10) with EMPTY coefficient1 lies in J^2 on these four selections.

This proves both sufficiency and the precise FAILURE of this local depth2 ansatz. Failure of(GOOD) is NOT a statement the four-letter block/full word avoids an identity2p selection, and not a no-go for different units/proof methods.

For reproducibility, the ACTUAL value c for ALL SIX possible type orders is:

| Actual type order and value order | a | b | c |
|---|---|---|---|
| rho_x rho_z sigma_y sigma_t (RRFF) | x+z | y-t | a+b |
| rho_x sigma_y rho_z sigma_t (RFRF) | x+z | y-t | b+x-z |
| rho_x sigma_y sigma_t rho_z (RFFR) | x+z | y-t | a+b |
| sigma_y rho_x rho_z sigma_t (FRRF) | x+z | y-t | b-a |
| sigma_y rho_x sigma_t rho_z (FRFR) | x+z | y-t | b-x+z |
| sigma_y sigma_t rho_x rho_z (FFRR) | x+z | y-t | a+b |

Every row follows by multiplying left to right with the law in Section1. For example FRRF gives y-x-z-t=b-a; RFRF gives x+y-z-t=b+x-z. We do not confuse a two-rotation selection with the signs of those same rotations in the four-letter selection. The table is a handwritten symbolic case distinction, not enumeration by code.

An actual balanced four-letter block satisfying(GOOD) is an allowed *four-unit*, of depth2. All arbitrary/identity-valued rotations and every reflection value remain;(GOOD) is an explicit test, not an ambient target restriction.

## 5. The UNIFORM correct-length tiling theorem

Define a *TILING certificate* for a word w of length4p-1 as:

1. choose an ACTUAL cyclic cut of w, giving a linear cyclic rotation w';
2. omit ONE ACTUAL letter occurrence of w', producing its ordered length4p-2 subword u;
3. partition ALL positions of u CONSECUTIVELY into allowed two-units and four-units from Sections3–4.

The omission/cut/partition are finite explicit combinatorial data. Their existence is NOT assumed for every target word. In particular, each unit has even numbers of both letter types, so the remaining u has even reflection count; the certificate itself enforces that necessary typing condition.

> **Theorem TILE (CANDIDATE).** For EVERY prime p>=7 and EVERY word w of length4p-1 over D_(2p), if w has a TILING certificate as just defined, w has EXACTLY2p positions in increasing ORIGINAL index order with identity product.

**Proof.** Construct theta_i in A for each actual unit, by(8)/(9)/(10)–(12), with depth d_i=1 or2. Its expansion is explicitly a sum over actual options, each having even size/even reflection parity, with the EMPTY option having coefficient1. Let L_i=2 or4 be its number of positions. Then d_i=L_i/2, and

    sum_i d_i=(sum_i L_i)/2=(4p-2)/2=2p-1.

Thus Theta=product_i theta_i lies in J^(2p-1)={0} by(5).

Expand the product FORMALLY before collecting equal basis points. Choosing one option in each consecutive unit gives an actual selected subset S of u; the union follows unit order and thus u's order. By(2), its basis point is E_(phi(S)). Its coefficient is the product of the option coefficients. The all-EMPTY option choice has actual selected set EMPTY, coefficient1 and basis point E_(0,0). Every other option choice is nonempty, since a nonempty unit option selects2or4 actual positions and units are disjoint.

The coefficient of E_(0,0) in Theta=0 is therefore

    0 = 1 + sum_(NONEMPTY option choices with phi(S)=0) coefficient(choice).

If there were no such nonempty option choice with nonzero coefficient, the right side would be1, a contradiction. Hence at least one NONEMPTY ACTUAL selection S has phi(S)=(0,0). This argument permits coinciding basis points and cancellations; it never mistakes formal option weights for counts. It uses only the unique all-empty choice's coefficient1, not an unproved injectivity/positivity premise.

Every selected option has even size and even reflection count, so |S| is a positive even integer at most|u|=4p-2, the selected product is rho_(v(S)), and phi(S)=0 gives v(S)=0 and |S|/2=0 modp. Consequently

    1<=|S|/2<=2p-1 and p divides |S|/2,

so |S|/2=p and |S|=2p. Its product is rho_0=identity.

The selected positions of u embed increasingly into w' by skipping the one omitted occurrence; their order/product is unchanged. Finally write the original word as AB so that w'=BA. Let P_A,P_B be the selected ordered products in the respective original portions. The constructed identity in w' says P_B P_A=1. The ORIGINAL increasing-index product is

    P_A P_B=P_A(P_B P_A)P_A^(-1)=1.

The same2p ORIGINAL positions therefore give identity in the ORIGINAL index order. This remains valid when one portion's selection is empty, when a unit crosses the omitted position in w' (that position is simply not selected), and for cuts through any letter type. No rearrangement of selected noncommuting letters, inverse normalization or old4p-2theorem transfer occurs. QED.

This theorem applies uniformly at the full correct-length ambient word domain; the added certificate is an explicit sufficient hypothesis, not a concealed reduction of the stated whole target. The unresolved complement is Section8.

## 6. A concrete UNBOUNDED certificate class beyond the basic pair/o_F/numerical bands

For EVERY p>=7 and ANY2p choices x_0,...,x_(2p-1) in{1,2}, form the actual word

    W(x)=rho_(x_0) sigma_0 rho_(x_1) sigma_0 ...
         rho_(x_(2p-2)) sigma_0 rho_(x_(2p-1)).            (13)

It has R=2p,F=2p-1,N4p-1 and o_F=2p-1 singleton cyclic constant reflection blocks. The first and last rotations are consecutive across the cyclic boundary, so every reflection is still cyclically singleton. Delete the FIRST sigma_0 in this displayed linear word. Its first two remaining rotations form one RR two-unit. The rest partitions, consecutively, into p-1 units of type

    sigma_0 rho_(x_(2j)) sigma_0 rho_(x_(2j+1)),
    1<=j<=p-1.

For each such FRFR unit, b=0, a is one of2,3,4, and c=-x_(2j)+x_(2j+1). Since p>=7, a!=0=b, so(GOOD) holds, with no need to constrain c. TheoremTILE supplies an original-order identity2p selection for EVERY assignment in(13), not a list of sampled parameters.

This includes genuinely NON-OPPOSITE-PAIR rotation alphabets: if both1and2 occur, {1,2} is not contained in{c,-c} for p>=7. Thus this class is not an invocation of RGR-LONG's pair hypothesis. It has o_F=2p-1>p, outside the old ASSEMBLY-P numerical odd-block class. Its countR2p is below3p-1; its cyclic gaps consist of one2rotation gap and the other1rotation gaps, so Q1 and F+Q2p<3p-1, outside the universal P criterion.

For a sharper baseline comparison, choose exactly p-1 values1 and p+1 values2 in ANY order. The only rotation-only2p selection is the full rotation multiset, whose sum is(p-1)+2(p+1)=3p+1=1 modp, so that exact old rotation-only test fails. Every gap is nonempty; for every Davenport-alpha I, |I|+rotationsoutsideI<=R=2p<3p-1, so that filter also fails. Both rotation multiplicities are at leastp-1; making the alphabet an opposite pair by deleting letters needs at leastp-1 deletions, beyond the historical Rprime p-3 allowance. Ordinary reflection runs are2p-1 singleton odd runs, so historical T0's at-most-one-odd-run hypothesis fails.

**Credit qualification:** this does NOT establish disjointness from EVERY old raw Doubling or qualified4p-2deletion-provider instance, and NO all-old-provider-new-cell count/novelty is claimed. Any such overlap keeps OLD credit. The new manuscript proves a uniform explicit local-block/correct-length sufficient criterion and a genuine unrestricted-value word class, not a full literature/SOTA improvement or a proof that all these words were previously unresolved. This exact distinction prevents merely relabeling old coverage as discovery.

## 7. A COMPLETE uniform counterexample to UNIVERSALITY OF THIS CERTIFICATE (NOT to Olson)

There is a concrete first failed overreach. A balanced block is not automatically good: for

    B=rho_1 sigma_0 rho_-1 sigma_0,

one has a=b=0,c=2!=0 in F_p. By Section4, no theta of form(10) with EMPTY coefficient1 lies in J^2. This is a LOCAL method failure only.

More strongly, for every prime p>=7 the correct-length word

    V_p=(rho_1 sigma_0 rho_-1 sigma_0)^(p-1)
         rho_1 sigma_0 rho_-1                              (14)

has NO TILING certificate, even though it DOES have an identity2p subword. This shows the certificate class is a proper partial class of the ambient target, not an unproved universal hypothesis disguised as a method.

**Actual domain and solvability.** There are2p rotations in(14), alternating values+1,-1 in their cyclic occurrence order, and2p-1 singleton sigma_0 reflections. The word has length4p-1. Selecting ALL2p rotations gives value p-p=0 and no reflection, so identity2p already exists by the old rotation-only test. Thus(14) is emphatically NOT a counterexample to the target.

**No-certificate proof.** Every allowed unit contains an even number of reflections. OriginalF=2p-1 is odd, so any possible one-letter omission in a certificate MUST remove a reflection, not a rotation. After omitting a reflection, all remaining reflections are still singleton and every two adjacent rotation OCCURRENCES in rotation-occurrence order have opposite values. No remaining FF adjacency exists.

Cyclically the original word has exactly ONE RR adjacency edge: the last/first rotations. Removing one reflection adds exactly ONE more RR adjacency edge between its former neighboring rotations, so after deletion the cyclic remaining word has exactly TWO RR adjacency edges. If the removed reflection adjoins the old2rotation gap, that gap becomes3rotations and has two edges; otherwise there are two2rotation gaps with one edge each. This is a direct adjacency count, independent of where a subsequent linear cut is placed. A linear cut can remove a cyclic edge from the linear adjacency list, never add one.

Classify a possible unit in this remaining word:

* A two-unit cannot be FF (no FF adjacency). Therefore it must be RR, and it uses an RR adjacency edge.
* A balanced four-unit cannot be RRFF,RFFR,orFFRR, because these require an FF adjacency. If it is RFRF or FRFR, its two rotations are adjacent in rotation-occurrence order and opposite, so a0,b0 while c is respectively +2or-2, nonzero; the unit is BAD by(GOOD). The only possible GOOD balanced four-unit type is FRRF, which contains an RR adjacency edge (and in fact has a=b=c0, so is good).

Thus EVERY allowed unit in any possible certificate must contain exactly TWO rotation occurrences and use an RR adjacency edge. Distinct disjoint consecutive units cannot use the same RR edge because that edge's endpoint positions would have to belong to both units. At most TWO allowed units can occur, as only two RR edges exist. But all2p remaining rotation occurrences must be covered and each allowed unit contains exactly2, requiring p units. Since p>=7>2, this is impossible.

This exhausts EVERY cyclic cut, EVERY possible omitted letter and EVERY allowed2/4unit partition, without enumeration or a program. Therefore(14) lacks the certificate. It disproves the blanket auxiliary statement “every correct-length word has this certificate”, not the ordered Olson implication, and it does not prove that a word failing the certificate is an avoider. Old filters already solve this particular certificate obstruction.

## 8. ENTIRE remaining actual-word class and exact first unproved global step

Let W_p denote ALL actual words of length4p-1 over D_(2p), with no added alphabet/parity/count assumptions. Let OLD_p be the actual words covered by the complete literal accepted-provider/caller audit of `STEP0-OWN-BASELINE-v1.md`, at each OLD interface's EXACT classical/S(p)/Lev/conditional trust. In particular old P/two-EGZ/Doubling/Davenport/RGR-LONG/few-odd/ASSEMBLY word scopes are not widened; old R3 and ALL-R candidates are not included as premises. Any further particular accepted deletion-caller must actually satisfy all its own hypotheses before being counted OLD.

Let TILE_p be the actual words possessing some certificate of Section5. The ENTIRE new unresolved actual-word class relative to the declared old imports is

    RES_p = W_p minus (OLD_p union TILE_p),               (15)
    for EVERY prime p>=7, with ALL original word data retained.

This is a FULL symbolic residual, not a claim relaxed data are feasible or a finite prime/configuration list. It contains only actual words failing EVERY allowed cut/one-letter-omission/good-unit partition. It does not drop any unresolved R, mixed/even/odd block, identity-rotation, high-o_F, terminal or original-order case. It does not assert RES_p is nonempty: the method-obstruction family(14) is OLD-covered and hence is NOT a residual-avoider witness.

Every hypothetical remaining avoider retains the complete old actual-word necessary system from Step0, including entire R in[p+1,3p-2], F4p-1-R, every literal Doubling/Davenport/rotation-only/P failure, failure of actual RGR-LONG condition, and o_F>=p+1 only relative to the exact stated ASSEMBLY-P secondary/Lev/classical trust. Its arbitrary rotation occurrences (0allowed), actual reflection values/maximal cyclic blocks, genuine empty-gap distinction, correct-length count identities and EVERY GRX sign pattern/admissible EVEN C (including n0/n2p where applicable) remain. No normal-form inverse or false old4p-2terminal theorem is inserted.

**First unproved whole-target step:** prove identity2p for EVERY actual word in the ENTIRE unbounded union of(15), or construct a genuine exact4p-1 avoiding word with a complete all-selection written proof. TheoremTILE settles only TILE_p. The universal-certificate shortcut is concretely FALSE by(14); the weaker claim that every OLD-uncovered word has a certificate is NOT established or assumed. Neither the local bad block nor(14) is a no-go theorem for other proof methods. No full correct-length target, full all-groups conjecture, rigidity/inverse classification or residual feasibility has been proved.

## 9. Trust, process, source and next gates

This proof is self-contained elementary group/order/group-algebra/linear algebra, with all explicit assumptions and coefficient formulas supplied. It imports no historical T0 correctness claim or matrix nilpotence. The parent matrix objection is honored for that different matrix; Section2 supplies the different ACTUAL algebra/ideal and its exact quotient/nilpotence proof. No numerical multiplication or experiment was run by this worker. The manuscript requires independent parent handcheck of the ACTUAL definitions and argument, not an assumed acceptance of CP01.

All parent prescope/T0/same-author exposure and the NEW permanent pre-Step0-route-planning MAJOR, old R3 MAJORs/documentary qualifications and source/clock history remain uncured. New proof work began only after Main acknowledged the complete Step0 delivery; that later gate did not cure the earlier planning departure. Old P/GRX/assembly trust is not upgraded by the new sufficient criterion. All used direct bodies/OWN scopes/mandatory overlays or honest non-premise/accepted-statement boundaries must travel in the complete source package.

Required actual Claude gate is still NOT_LAUNCHED/BLOCKED untilOct26 after the deadline. No workaround/model/account/provider/payment/configuration change or promotion; parent/Codex support cannot replace the actual second family. No scientific code, enumeration, assertion/test, solver, Lean/native, modelCLI/API, network, nested agent, Git, deletion or old-file mutation. Same ENTIRE target, one existing math slot/two total threads, <=4parts/100000B source caps, one complete context per family, substantive checkpoint cadence and08:00stop/08:15handoff/global cutoffs remain unchanged.
