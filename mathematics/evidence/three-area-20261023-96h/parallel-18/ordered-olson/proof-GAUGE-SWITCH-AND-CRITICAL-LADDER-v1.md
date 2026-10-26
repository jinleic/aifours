# Selected-rotation gauge switches and an exact critical-ladder obstruction

Observed before exclusive creation: **2026-10-23T14:09:38-0700 PDT**. Owner MathOlson-2, slot math-2. **CANDIDATE written partial theorem / exact necessary obstruction.** The whole R=p+1 band, unrestricted prime-dihedral ordered Olson and the all-finite-groups conjecture remain NOT_PROVED. No executable scientific check is a premise.

## 0. Target, baseline, claimed delta and imports

The frozen target and current source/trust bindings are `selection-v1.md` with `selection-addendum-1-gauge-and-prior-arcs.md`. The governing historical baseline is final-v17 WITH its operative erratum, the October22 EVENING report, and its complete lower-band selector/inverse-insertion manuscript WITH the parent sign-frame qualification. R counts ROTATIONS, not reflections.

Fix any prime p>=7. The immediate actual word has N=4p-1, R=p+1 and F=3p-2 in

    D_(2p)={(v,e):v in F_p,e in{+1,-1}},
    (v,e)(v',e')=(v+ev',ee'), rho_x=(x,+1), sigma_y=(y,-1).

All rotation values INCLUDING0, all reflection values, all actual type patterns/orders, genuine empty gaps, arbitrary constant-block parities and all mixed-selection sizes remain. Nothing below assumes a nonzero opposite rotation pair, an admissible NF, a classification of reflection-only failures, or that the residual is nonempty.

**Delta supplied here:** an exact gauge identity for ANY ACTUAL selected rotation set; actual reflection-pair switches allowed to straddle selected rotations; a self-contained inverse statement at p-2 switches, including its sole missing residue; an odd-component obstruction for EVERY possible even nonempty rotation set; and an explicit critical-ladder condition on leftover labels in the all-rotation branch. These give positive selection criteria and a new stated necessary obstruction, not a proof that all residual words satisfy one of the positive criteria.

**Prior mechanism is not claimed new.** Historical `reflection-round2/proof-REFLHI-arcs-v2.md` already has ARC and prefix-mass ETA in its length-4p-2, one-nonzero-pair/all-odd setting, ETA further at B=0. Reflection packets and additive growth are therefore old mechanisms. The present argument supplies the exact arbitrary-value/selected-K transport and critical inverse/offset formulas without those restrictions. No priority or strict-coverage increment beyond every OLD/GEN/IPGEN provider is certified.

The proofs below use only the displayed group law, elementary arithmetic in F_p, and the elementary finite cyclic-translation lemma proved in section2. **No S(p), Lev, EGZ, Davenport, index-one, Cauchy-Davenport theorem, normal-form theorem, old finite search, or unpromoted certificate theorem is an input to the new theorem.** The historical B1 comparison in section7 retains the old imports at their exact old trust; overlap does not upgrade them.

## 1. Exact selected-rotation gauge identity

List the ACTUAL reflections in original order as f_1,...,f_F, with f_j=sigma_(y_j). Their indices j here name reflection occurrences, not all-word positions. Let K be ANY actual set of rotation positions, and put

    k=|K|, S_K=sum_(r in K) x_r,
    s_K(j)=sum_(r in K, r before f_j in ORIGINAL order) x_r,
    z_j^K=y_j+2 s_K(j).                                      (1)

All sums are in F_p. Unselected rotation and reflection occurrences have no effect. For an even reflection index set J={j_1<...<j_C}, let P(K,J) be the product of the SAME actual selected rotation and reflection positions, in ORIGINAL increasing order.

**Lemma G (exact gauge).**

    P(K,J)=rho_( S_K + sum_(nu=1)^C (-1)^(nu-1) z_(j_nu)^K ). (2)

In particular the product has even reflection parity. If k+C=2p, equation (2)=rho_0 is exactly the original-order identity-2p condition for this K,J.

**Proof.** Let u_0,...,u_C be the sums of the ACTUAL K-rotations respectively before f_(j_1), between successive selected reflections, and after f_(j_C). Rotation-only products on these consecutive stretches are rho_(u_l), without changing any selected order. Put t_n=u_0+...+u_(n-1)=s_K(j_n) and S=u_0+...+u_C=S_K. By cancellation of adjacent inverse rotations, the following is an exact algebraic identity:

    rho_(u_0) f_(j_1) rho_(u_1) ... f_(j_C) rho_(u_C)
      =(rho_(t_1) f_(j_1) rho_(-t_1))
       ... (rho_(t_C) f_(j_C) rho_(-t_C)) rho_S.

Indeed consecutive displayed factors telescope to rho_(-t_n)rho_(t_(n+1))=rho_(u_n); the initial and final factors give rho_(u_0) and rho_(u_C). The group law gives

    rho_t sigma_y rho_(-t)=sigma_(y+2t).

Thus the same original product is sigma_(z_(j_1)) ... sigma_(z_(j_C)) rho_S. Inducting on this displayed product, an even number C of reflections has coordinate sum_(nu)(-1)^(nu-1)z_(j_nu) and parity +1; multiplication by rho_S then adds S. This proves (2). We have proved an equality of products, not permission to commute or permute actual selected terms. QED.

For comparison with the original MIX formula, the latter is also obtained directly by prefix-reflection parity. Lemma G is an equivalent expression at fixed K, with arbitrary interleaving encoded in the labels z^K. In particular two candidate reflection occurrences may have selected rotations between them: the change 2s_K in their labels precisely accounts for that fact.

## 2. Complete elementary binary-growth and critical-inverse lemma

For sets A,B in F_p, A+B means their scalar sumset. This commutative notation will be used only AFTER an exact ordered-product formula has been proved.

**Lemma T (translation growth).** If A is a nonempty proper subset of F_p and d!=0, then

    |A union(A+d)|>=|A|+1.

**Proof.** Otherwise A+d, which has size |A|, would be contained in A and hence equal A. Iterating gives A+nd=A for every integer n. Because p is prime and d!=0, {nd:n=0,...,p-1}=F_p. A nonempty invariant A would then be all F_p, a contradiction. QED.

Given t nonzero residues d_1,...,d_t, put

    U_t={0,d_1}+...+{0,d_t}.

Repeated Lemma T gives |U_t|>=min(p,t+1); once fullness is reached, further additions preserve it. Consequently **p-1 nonzero binary switches fill F_p**.

**Lemma CI (exact p-2 inverse and missing residue).** For t=p-2, U_t is proper IF AND ONLY IF there is d!=0 with every d_i in{d,-d}. If so, write d_i=epsilon_i d, epsilon_i in{+1,-1}, and let m be the number of minus signs. Then

    U_t=-m d+{0,1,...,p-2}d
       =F_p minus{-(m+1)d}.                               (3)

**Proof.** If two increments a,b are not equal up to sign, the four points 0,a,b,a+b are distinct: any coincidence would force a=0, b=0, a=b or a=-b. Starting with these two switches gives four residues. The remaining t-2=p-4 nonzero switches, by Lemma T, fill at least min(p,4+p-4)=p residues. Thus a proper U_t forces every pair of increments to be equal up to sign, hence all lie in{d,-d} for d=d_1.

Conversely each minus factor {0,-d} equals -d+{0,d}. Sums of t copies of {0,d} are exactly {0,1,...,t}d, since every integer between 0 and t is a possible number of chosen d's. Since t=p-2, these p-1 residues are distinct, missing only -d before the translation. This proves (3) and properness. QED.

For a fixed scalar B, (3) gives the exact criterion

    0 notin B+U_(p-2)  IFF  B=(m+1)d.                    (4)

Changing d to -d changes m to p-2-m and leaves the right-hand residue unchanged modulo p. There is no sign-normalization ambiguity.

## 3. Actual reflection packets and positive mixed-selection criteria

Fix an even k with 2<=k<=p+1 and ANY ACTUAL K of k rotations. Set

    C=2p-k;  C is even and C>=p-1.

An ordered C-packet system consists of C nonempty sets of ACTUAL reflection occurrences P_1,...,P_C such that

    max P_i < min P_(i+1)

in the original reflection order. For the binary systems here, each P_i is either one singleton occurrence or two specified occurrences a_i<b_i. Other reflection occurrences, including any between a_i and b_i, are unselected by this system. Select exactly ONE occurrence from every packet, and all K rotations.

Because packet order is fixed independently of choices, Lemma G gives EXACTLY the scalar option set

    B+sum_(i binary){0,delta_i},
    B=S_K+sum_(i=1)^C (-1)^(i-1)z_(a_i)^K,
    delta_i=(-1)^(i-1)(z_(b_i)^K-z_(a_i)^K),               (5)

where a_i denotes the singleton itself for singleton packets. These are actual selections of k+C=2p original positions. The selected C reflections are even in number; (5) is not an unordered-to-word inference.

**Theorem GS (gauge-switch sufficient theorem).** An original-order identity-2p selection exists whenever one such packet system has either:

1. p-1 binary packets with nonzero increments; or
2. p-2 binary packets, all increments nonzero, with two increments not equal up to sign; or
3. p-2 binary packets whose increments all lie in{d,-d}, d!=0, but whose B from (5) does NOT equal (m+1)d, where m counts the negative signed increments.

**Proof.** In case1 Lemma T fills F_p. In case2 Lemma CI fills F_p. In case3 equations (3)-(4) show that the sole omitted scalar is not zero. In every case zero is in the ACTUAL option set (5). Lemma G gives the ordered identity and the exact count. QED.

Conversely, in the p-2/nonzero case, the packet system has NO identity selection exactly when its increments have one common nonzero value up to sign AND the critical offset equality in (4) holds. This converse concerns this particular packet family, not every possible selection of the word.

No packet is allowed to cross another packet or a fixed singleton. Selected rotations inside a packet's span ARE allowed by Lemma G. This is the explicit extension beyond reflection-run-only packet reasoning.

## 4. A new exact odd-component obstruction for EVERY selected K

For the same K, form the path on reflection occurrences 1,...,F, retaining its adjacent edge (j,j+1) precisely when

    D_j^K=z_(j+1)^K-z_j^K !=0.                            (6)

Let nu_K be its maximum matching cardinality: the maximum number of disjoint adjacent reflection pairs with unequal gauge labels. This is a literal actual-order statistic, not an NF parameter or a solver relaxation.

**Theorem OM.** If nu_K>=p-1 for SOME even nonempty K, the word has an original-order identity-2p selection. Consequently every actual word avoiding ALL identity-2p selections satisfies, for EVERY even K with 2<=|K|<=p+1,

    nu_K<=p-2.                                            (7)

**Proof.** Choose p-1 disjoint adjacent pairs from the matching. To obtain C=2p-k packets, add C-(p-1)=p+1-k singleton reflections from outside those pairs. There are F-2(p-1)=p available outside occurrences, at least p+1-k because k>=2. As each pair is ADJACENT IN THE REFLECTION SUBSEQUENCE, no added singleton lies strictly inside it. Sorting these pairs and singletons therefore makes a valid packet system. Rotations between the endpoints are harmless by section1. Every binary increment is nonzero, so GS1 applies. QED.

Let L_1,...,L_q be the vertex lengths of the path components in (6), including isolated vertices, and let o_K count those lengths that are odd. A path on L vertices has maximum matching floor(L/2): a matching uses two vertices per edge, and pairing its first-second, third-fourth, etc. attains that bound. Components are independent. Hence

    nu_K=sum_i floor(L_i/2)=(F-o_K)/2.

At the actual F=3p-2, condition (7) is equivalent to

    o_K>=p+2.                                             (8)

If equality does NOT hold in (8), its parity forces o_K>=p+4. Therefore every hypothetical avoider has, for EVERY such K, either:

* the deeper branch o_K>=p+4; or
* the critical branch o_K=p+2, nu_K=p-2, with the full critical switch/offset constraints below.

In particular there must be at least p+1 zero edges in (6), since the number q of components is one more than the number of zero edges and q>=o_K.

For actual consecutive reflection occurrences the edge value is

    D_j^K=y_(j+1)-y_j
          +2 sum_(selected K rotations strictly between f_j,f_(j+1)) x_r. (9)

Thus these components are NOT maximal constant raw-reflection blocks. At the lower-band Q=0 reduction, an actual reflection gap has 0 or 1 rotations, so (9) is literally either y_(j+1)-y_j or that quantity plus 2x_r when its singleton rotation belongs to K. Zero-valued rotations are retained and cause no exception. This gives a word-level switched-edge obstruction, not a commutative shadow being declared sufficient.

When nu_K=p-2, take ANY matching of that size. Its p-2 oriented differences must ALL lie in one common nonzero pair{d,-d}; otherwise GS2 applies after filling the remaining C-(p-2)=p+2-k singleton slots. There are F-2(p-2)=p+2 outside reflection occurrences, enough for these singleton slots. For EVERY actual choice of those singleton slots, the resulting signed increments and B must satisfy (4); otherwise GS3 applies. This is a quantified actual-occurrence obstruction at EVERY mixed rotation count, not only the all-rotation branch.

The statements remain true after ANY actual cyclic cut: derive them on that cut word, then restore the SAME original selected positions by conjugation as in section6. Gauge labels must be recalculated on the chosen cut, not presumed periodic or globally unchanged by a cut.

## 5. Exact critical ladder in the all-rotation branch

Take K to be ALL p+1 rotations, so S=S_K, z_j=z_j^K, C=p-1. Suppose nu_K=p-2. Choose ANY critical matching of t=p-2 adjacent unequal reflection pairs, ordered

    (a_1,b_1),...,(a_t,b_t).

If two differences are not equal up to sign, GS2 already solves the word. In the remaining case write

    z_(b_i)-z_(a_i)=epsilon_i d, epsilon_i in{+1,-1}, d!=0.

There are exactly F-2t=p+2 unpaired reflection occurrences. Gap j, for 0<=j<=t, means the unused occurrences after the first j matching pairs and before the next pair, with the obvious initial/final convention. Some gaps may be empty.

Define

    m_0=#{i: (-1)^i epsilon_i=-1},
    A_0=(m_0+1)d-S-sum_(i=1)^t (-1)^i z_(a_i),
    A_j=z_(a_j)+z_(b_j)-A_(j-1),   1<=j<=t.              (10)

**Theorem CL (critical ladder, exact for this matching family).** The word has NO identity selection obtained by choosing one endpoint of EVERY matching pair and ONE arbitrary unpaired reflection if and only if EVERY unpaired occurrence u in gap j has

    z_u=A_j.                                             (11)

If even ONE actual unpaired occurrence violates (11), these packets give an original-order identity-2p selection. Thus every full-target avoider must satisfy the complete ladder for EVERY critical matching, while failure of a particular ladder family is NOT a full-target avoider certificate.

**Proof.** Put one singleton u in gap j. The signed endpoint increments are alpha_i^j epsilon_i d, where

    alpha_i^j=(-1)^(i-1) for i<=j,
    alpha_i^j=(-1)^i     for i>j.

Let m_j count their negative signs and P_j=sum_i alpha_i^j z_(a_i). The baseline in (5) is

    B_j(u)=S+P_j+(-1)^j z_u.

By Lemma CI this particular packet family's sole missing scalar is

    M_j(u)=B_j(u)-(m_j+1)d.                               (12)

For j=0, definition (10) gives M_0(u)=z_u-A_0. Advancing the singleton past pair j changes that pair's sign from (-1)^j to (-1)^(j-1). Therefore

    P_j-P_(j-1)=2(-1)^(j-1)z_(a_j),
    m_j-m_(j-1)=-(-1)^(j-1)epsilon_j.

The recurrence in (10), using z_(b_j)=z_(a_j)+epsilon_j d, now gives by direct subtraction

    S+P_j-(m_j+1)d=(-1)^(j+1)A_j.

This holds initially and inductively at every j. Substitution in (12) gives

    M_j(u)=(-1)^j(z_u-A_j).

Since (12) is the UNIQUE missing scalar, zero is absent exactly when M_j(u)=0, equivalently z_u=A_j. Quantify over every actual u to obtain (11) and its stated equivalence. Every such choice uses p-2+1=p-1 reflections and p+1 rotations, total exactly2p. QED.

Formula (10) defines virtual values even for empty gaps; (11) imposes a condition only where an ACTUAL unused occurrence exists. No empty-gap occurrence or fictitious zero is introduced.

## 6. Why the all-rotation branch cannot replace the whole MIX target

Here is a correct-length, completely explicit obstruction to that tempting replacement, not an Olson counterexample and not a new residual witness. For every p>=7 let a=-2 in F_p and write, in the displayed original order,

    w_p=rho_1 sigma_(-2)^(2p-3) sigma_(-1)
         (product_(i=2,...,p) rho_1 sigma_(1-2i))
         rho_2 sigma_(-3).                                (13)

The indicated product is concatenation with i increasing, not a commutative product. The word has R=p+1, F=3p-2, N=4p-1. Every cyclic rotation gap has 0 or 1 rotation. Its rotations take values1 and2, which are not an opposite pair at p>=7. Its p+2 maximal cyclic CONSTANT reflection blocks are all odd, so o_F=p+2. This is not the previously covered C_p insertion family: value a occurs 2p-2 times, and every other reflection value at most twice, so no reflection value has multiplicity2p-1.

For K equal to all rotations, S=p+2=2 modp. Formula (1) gives the reflection-gauge sequence

    0^(2p-3) 1^(p+1).

In ANY even reflection subsequence of this two-block sequence, the alternating sum is0 if it selects an even number of ones and -1 if it selects an odd number of ones. In particular every choice of C=p-1 reflections has coordinate2 or1 in (2), never0. Thus NO identity2p selection uses all p+1 rotations. This excludes that entire branch by a complete all-choice argument at the CORRECT original length.

Nevertheless w_p is already REF-covered. Select all 2p-3 initial sigma_a, then the first sigma_(a+1), the sigma_a at i=(p+3)/2, and the final sigma_(a-1). The index (p+3)/2 is an actual integer between2 andp. These exactly2p ACTUAL reflections have product

    sigma_a^(2p-3) sigma_(a+1) sigma_a sigma_(a-1)
      =sigma_a sigma_(a+1) sigma_a sigma_(a-1)
      =rho_(a-(a+1)+a-(a-1))=rho_0.

This explicit positive selection is why (13) is NOT a B1 witness or counterexample. It earns no new coverage credit. It demonstrates, without computation, that proving only the all-rotation branch is not equivalent to the assigned whole-word theorem. The new obstruction in sections4-5 remains a necessary selection obstruction, not a universal proof route.

**Original-cut restoration for all earlier cyclic statements.** Write the original word AB and a cut word BA. If P_A,P_B are the selected products in the two original portions and P_B P_A=1 in the cut order, then P_A P_B=P_B^(-1)(P_B P_A)P_B=1. Hence the SAME actual selected positions have identity in increasing ORIGINAL order. This applies whether the cut divides a packet's original linear span or not; packets were constructed as ordinary noncrossing packets on the chosen cut word first.

## 7. Exact remaining whole-band obligation and verification boundary

Keep the complete actual B1_p definition and ALL old qualifications from the October22 manuscript section7. Let GS_p be the actual words admitting SOME even nonempty K, SOME actual cut and SOME packet system covered by Theorem GS. Define

    B2_p=B1_p minus GS_p.                                 (14)

This removes only a proved sufficient actual-word class. It does NOT assert that B2 is nonempty or consists of avoiders, that some strict new B1 coverage has been located, or that the packet language exhausts all selections.

For every actual member of B2, ALL old tests/caller failures, all actual values/gaps/block parities/orders, REF/SEL/IPGEN failures, and the complete old GRX sign/even-endpoint qualifications remain. In addition, for EVERY actual cut and every even K with 2<=|K|<=p+1:

* the switched-edge path satisfies nu_K<=p-2, equivalently o_K>=p+2;
* every critical matching has one common nonzero difference up to sign and satisfies the exact critical offset for EVERY permitted choice of singleton filler occurrences;
* at K equal to all rotations, every such critical matching satisfies the full ladder (10)-(11), not just a scalar count or one chosen filler.

The FIRST unproved universal implication is STILL the original MIX statement on this ENTIRE actual B2: find actual even k=2h rotation positions K and C=2p-k reflection positions J such that

    S_K+sum_(nu=1)^C (-1)^(nu-1)z_(j_nu)^K=0.             (15)

By Lemma G this is exactly the same remaining ordered selection equation, not a relaxed parameter feasibility claim. We have supplied necessary obstructions and positive criteria, not a proof that the full obstruction system is impossible. The deeper o_K>=p+4 branch and simultaneous critical-profile compatibility over ALL K/cuts remain uncovered; no silent bound on rotation values is introduced.

The new GS/OM/CL results are self-contained written mathematics at the displayed group-law/elementary finite-field level. Historical OLD/S(p) SECONDARY-statement trust, Lev STATEMENT-level trust, classical theorem ancestry, unpromoted SEL/IPGEN status and all historical process limitations remain unchanged in the B1 comparison. If old imports are withheld, their dependent old exclusions rejoin the residual; the new sufficient theorems themselves do not change.

No Python/Fraction calculation, enumeration, native job, solver, compilation, old checker, Lean/kernel, external-model CLI or paid fallback was used. Metadata hashes are only byte identities. A completed candidate requires actual separate in-harness reconstruction and parent review before any acceptance claim; neither is certified by this author snapshot. Correctness, import trust, scope, novelty and significance remain separate.
