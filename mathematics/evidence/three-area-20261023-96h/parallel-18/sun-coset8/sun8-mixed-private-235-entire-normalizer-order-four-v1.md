# Sun P7 — the mixed private2/3/5 exception forces the ENTIRE normalizer quotient to have order at most4

Owner **MathSun8-2**. Actual preceding `/bin/date`: **Mon Oct 26 07:56:13 PDT 2026**. **NEW WRITTEN CANDIDATE, not reviewed/adopted.** This is a complete actual-group/fibre/enlargement proof. It does NOT infer a group from an affine drawing, bound only elementary rank, or claim unrestricted Sun8.

## 0. Exact direct theorem and separate application union

Let G be finite with EIGHT pairwise-disjoint original LEFT cosets g_l U_l of indices7r_l, all positive private r_l pairwise coprime. In THIS SAME G choose an ACTUAL such family minimizing the sum of its private indices. Select i, translate ALL eight cosets together so U=U_i is the selected coset, and put N=N_G(U), Q=N/U.

Assume the selected private r_i owns2; one original neighbour j6 owns5 and has full normalizer orbit coefficient alpha_(j6)=6; another original neighbour j5 owns3 and has alpha_(j5)=5. Assume NO other original neighbour has alpha6. The normalizer coefficients, all original subgroups and their actual cell/fibre meanings are derived in§1 rather than treated as formal integers.

**Direct theorem.** The ENTIRE actual Q has order at most4:

- If the six-source is `(beta,c)=(6,1)`, then Q is1,C2 orC2xC2.
- If the six-source is `(beta,c)=(3,2)`, then Q isC2,C4 orC2xC2.

This includes arbitrary starting nonabelian Q, odd factors, hidden neighbours and a possible private7-owner. It is a bound on the ACTUAL group order, not a rank/involution count or a small abstract quotient.

The direct theorem uses only elementary group/index/coset counting and actual minimum-family enlargement, plus the three-coset lemma FULLY proved in§2. It does NOT assume the new142LF mixed-source theorem accepted.

**Application candidate at the full source union:** the complete142LF `sun8-mixed-six-one-five-two-private-235-obstruction-v1.md`, SHA25697f7e607ca3948ff67194904f677473844231deeed4457412c81561aa53235d2, would force precisely the above private2/5/3 ownership in any surviving mixed6+1/5+2 pair at a7-free vertex or a least-order simple direct-P7 example. The already adopted two-six-source bound gives NO second alpha6 at the stated scopes. If those full hypotheses are verified, the present direct theorem reduces the entire remaining normalizer group to the above orders. It does not eliminate those order1/2/4 actual lifts, prove occurrence of the mixed sources, cover5+1+1 sources, or authenticate the general Sun8-to-P7/globalSun7 ancestry.

## 1. ALL original indices, seven-retention and fixed actual fibres

For EVERY original neighbour l let V_l=U cap U_l. Index divisibility and the product-size formula give

    [G:V_l]=7r_i r_l beta_l,
    [U:V_l]=r_l beta_l,
    |U U_l|/|G|=beta_l/7.

Beta_l is an integer1..7. If beta7, U U_l=G and every such coset pair meets, contradicting original disjointness. Thus beta_l<=6 for ALL seven neighbours, visible or hidden.

We first prove7 divides[G:N]. Suppose not, and put d=[G:N]. Then d divides r_i and is coprime to7r_l for EVERY neighbour. Coprime-index subgroups have whole product, so every given neighbour coset meets N and[N:N cap U_l]=7r_l. Put W_l=N cap U_l and H_l=U W_l/U in Q, with c_l=[Q:H_l]. Since U normal N,

    [N:W_l]=c_l[U:U cap U_l]=c_l r_l beta_l.

Hence c_l beta_l=7; beta<=6 forces beta1,c7. Each projected neighbour coset avoids identity, else its actual N-intersection meets U. Any two projected neighbour overlaps would put two ACTUAL left V_l-cosets of private-coprime indices r_l,r_k in the SAME U-fibre, so those pieces meet. Thus the seven projected cosets are disjoint, each of index7 in Q, yet all avoid identity. Their total cardinality is|Q|, contradiction.

Consequently

    [G:N]=7s, q=|Q|, r_i=sq.

No normality of N in G is asserted; Omega=G/N is only the set of7s LEFT cells. Because gcd(s,r_l)=1, index divisibility gives

    [N:W_l]=r_l alpha_l,
    alpha_l=beta_l c_l<=7,
    [U_l:W_l]=s alpha_l.                             (1)

The given neighbour hits EXACTLY s alpha_l of the actual left N-cells. In any hit cell gN choose y in its intersection with that neighbour; the intersection is yW_l. Translation into N gives a left coset of the SAME fixed W_l, whose quotient support is a left coset of the SAME fixed H_l. In a common U-fibre, the actual pieces are left cosets of the SAME V_l and have index r_l beta_l. These facts hold in ALL cells, not only the initial N-cell.

Initial supports mean neighbours actually meeting N. They avoid identity in Q, so c_l>=2. An actual subgroup L<=Q missing EVERY initial support has inverse image U' in N containing U, avoiding every original neighbour: hidden neighbours miss N altogether, and visible ones miss the projected L. If L is nontrivial, the new private index r_i/|L| is a smaller integer divisor of r_i, so all private coprimalities and ALL other original cosets remain, contradicting the achieved minimum sum. Therefore

    EVERY actual blind subgroup L in Q is trivial.        (BLIND)

This is source-preserving enlargement in the SAME group, not deletion of an arithmetic factor.

## 2. The needed three-coset index2 obstruction, entirely proved

**Lemma.** In a finite P, three left cosets of subgroups L_1,L_2,L_3 with indices2u_1,2u_2,2u_3 and pairwise-coprime u_l cannot be pairwise disjoint.

Suppose they were. For each pair, index divisibility gives[P:L_a cap L_b]=2u_a u_b delta with delta1 or2. Delta2 would make L_a L_b=P and force every coset pair to meet, so delta1. Within L_1 the two intersection indices are u_2,u_3, coprime; their further intersection has index u_2u_3. Thus

    [P:L_1 cap L_2 cap L_3]=2u_1u_2u_3.

Consider ALL8u_1u_2u_3 ordered triples of subgroup cosets. Let E_ab be the event that cosets a,b meet. Meeting pairs are in bijection with P/(L_a cap L_b), so each E_ab has4u_1u_2u_3 triples after choosing the third coset. For E_12 cap E_13, choose the first coset in2u_1 ways; there are u_2 cosets of L_2 and u_3 of L_3 meeting it, giving2u_1u_2u_3. The other two event-pair intersections have the SAME count. All-three-event intersection contains at least the2u_1u_2u_3 triples with a COMMON point, counted by the triple subgroup intersection.

Inclusion-exclusion therefore makes the union size at least

    (3*4-3*2+2)u_1u_2u_3=8u_1u_2u_3,

the whole universe. There is no triple with no meeting pair, contradiction. This is finite coset counting in writing, not a program or an opaque Sun3 import. Only this needed actual-fibre lemma is asserted here.

## 3. Complete initial-type restriction, including the possible index7 support

Private ownership implies ALL neighbour r_l are odd; r_(j6) is3-free and r_(j5) is5-free; every OTHER neighbour private factor is both3- and5-free. Since q divides r_i, Q is3-free and5-free. It may initially have any2-power, other prime factors, or nonabelian structure.

Alpha5 factors only as beta5,c1 or beta1,c5. The latter is impossible because c5 would divide q. Thus j5 has beta5,c1, a FULL Q-footprint in every hit N-cell, and is initially HIDDEN: a full initial footprint would meet selected U at identity.

Alpha6 can only be beta6,c1 or beta3,c2, because c3/c6 are unavailable in the3-free Q. For any OTHER initial neighbour, c>=2, c|q and beta*c<=7 leave ONLY

    A2=(1,2), B2=(2,2), C2=(3,2), A4=(1,4), A7=(1,7).

C2 would be a SECOND alpha6 source and is excluded by the explicit hypothesis. A7 is retained until its actual exclusion below; no private7 possibility is silently dropped. A c1 source cannot be initial. This list concerns the INITIAL supports only; arbitrary hidden types are not deleted from the original family.

## 4. FULL-footprint six-source: ENTIRE Q is elementary of order at most4

Assume j6 has beta6,c1. Its support hits6s N-cells and misses only s. For any other beta1 source with c>=2, its U-fibre index r_l is coprime to6r_(j6): r_l is odd,3-free and private-coprime to r_(j6). In a common N-cell, its quotient coset MUST meet the six-source's full Q footprint. Actual U pieces with coprime indices would then meet, impossible. Hence it cannot share ANY six-source cell.

But that beta1 source hits cs>=2s cells and cannot fit inside the six-source's s missing cells. Thus A2,A4,A7 are excluded GLOBALLY, not just initially. The only possible initial supports are B2, negative affine halfspaces of actual nonzero binary characters lambda_l:Q->F2.

Their common kernel misses every initial support, so(BLIND) makes it trivial. Therefore Q embeds in the elementary abelian character image, not merely in an unspecified small quotient. If the character rank were>=3, three independent initial characters would simultaneously equal1 at some q in Q. In that ONE actual U-fibre their three pieces have indices2r_l with pairwise-coprime private r_l, contrary to§2. The rank is at most2, hence

    Q is1,C2 orC2xC2.

If there are no initial characters, Q itself is blind and must be1. No hidden-neighbour condition was discarded in applying(BLIND), and no rank bound was turned into a group-order bound before the kernel was proved trivial.

## 5. HALF-footprint six-source: all initial directions lie in one kernel

Assume j6 has beta3,c2. Write its fixed index2 subgroup as K=ker lambda in Q. Its actual offset may vary by N-cell; it need not be initially visible.

For another A2/B2 source, its U-fibre index r_l or2r_l is coprime to3r_(j6). If its fixed binary character differed from lambda, the two nonzero binary characters would be independent, so ANY affine pair of their halfspaces intersects. Their actual supports must share a cell because they hit at least2s versus the six-source's6s in7s cells. Coprime U-fibre indices then force an original intersection. Therefore EVERY global A2/B2 source has the SAME character lambda.

For A4, its4s hit cells share cells with the six-source's6s. In a common cell its index4 quotient coset must avoid the six-source halfspace, since their U-fibre indices r_l and3r_(j6) are coprime. The entire index4 coset is therefore contained in the OTHER coset of K. Taking differences inside that coset proves its SAME fixed subgroup H_l is contained in K. One verified common cell is enough to obtain this GLOBAL direction inclusion; no affine subgroup is invented independently.

For A7, its quotient index7 is coprime to the six-source index2, so their cosets ALWAYS meet in every common cell. It hits ALL7s cells while the six-source hits6s, again forcing an original intersection. Thus A7 is excluded even if Q owns a private7 factor.

Consequently all initial index2 supports, including j6 if visible, are the UNIQUE nonidentity coset lambda=1 and lie OUTSIDE K. Every initial A4 has direction H_l<=K. Its coset is either contained in K or disjoint from K.

## 6. The ACTUAL blind subgroup closes the entire quotient, not an abstract slice

Initial A4 quotient cosets are MUTUALLY DISJOINT: an overlap would give two actual left U-fibre cosets of indices r_l,r_k, coprime, and force original intersection. Each has size q/4 and avoids identity. Inside K (of size q/2), there can be at most ONE such initial coset; two would cover K completely while both avoid identity.

If NONE lies inside K, K misses every initial support, all of which lie outside it. By(BLIND), K1, hence q2.

If ONE lies inside K, write it gH with H<=K and |H|=q/4. It avoids identity, so it is disjoint from its own subgroup H. Every other initial support is outside K; therefore H misses ALL initial supports and is an ACTUAL blind subgroup. By(BLIND), H1, hence q4.

The six-source character exists, so q>=2. We have proved

    q=2 or4, Q isC2,C4 orC2xC2.

This covers arbitrary original nonabelian/odd/private7 starting Q; no elementary-slice assumption, simultaneous independent phase choice or total-involution count replaces the ACTUAL inverse-image enlargement. ALL seven original neighbour cosets, visible and hidden, remain unchanged.

## 7. Composition with the complete mixed-source theorem and exact residual

The direct result above is complete under its explicit private-owner/alpha/NO-second-six hypotheses. Applying it to a surviving mixed6+1/5+2 normalizer pair requires the ENTIRE142LF mixed theorem and the old actual two-six capacity bound, at their exact selected7-free or least-GROUP-ORDER/simple scopes. At a least-order finite simple existence example one may choose a minimum-private-SUM family WITHIN that SAME least-order G; the two minima are distinct and neither is silently substituted for the other.

Thus a surviving mixed exception would have EVEN actual outer s, the unique selected private2 owner, six-source private5 owner, five-source private3 owner, its stated common-irrep dimension ceiling, AND the ENTIRE Q of order1/2/4 just proved. This is a candidate restriction, NOT contradiction for those actual small-quotient lifts. No theorem makes every alpha5 a TWO-orbit5+2 source;5+1+1/Hom3 remains open, as do mixed cases not forcing these sources, other alpha values, private-composite/odd/maximal/self-normalizing legal-enlargement collisions and all full original fibre coherence.

The original general Sun8/globalSun7/finite-core/normal-section ancestry remains at its named boundary. Even the separately supported ALL Sp/PSp theorem is not a reduction of arbitrary groups to those families. Older644 kernel-section/M1 class-AT-MOST2/abelian-exponent4 alternative, high-source136, unrestricted-private125/two-source99/least-order63, EA8 C/O/E/all hidden-neighbour/s/outert/power, An/GLPGL/other-Lie/extension/infinite leads are retained, not removed by this local global-quotient bound. No actual8-coset witness, t/group-size bound, full Sun8, novelty or SOTA claim follows.

## 8. Chronology and permanent assurance

The complete proof above was ALREADY held before v123 receipt and saved in whole088, not derived while the review was live or retroactively preregistered. This manuscript follows ACTUAL v123 review RETURN, NEW whole089 and separate primary ACK4be7796b680853acb4f372216d481cf35fbae7dd78a268dc013b08ff116220fe WRITTEN+SENT BEFORE prospective primary work. The earlier source proofs200/142 remain separate NEW candidates pending their own complete gates; none is silently adopted here.

OWN05733m10s cadence,047 metadata-poll,078 premature park, COUNT38-not46, M1, v26 receipt-through081 primary-pause violation, v31 TWO historical Shor no-scout/delayed-disclosure findings, v33 post-return/pre-ACK order and all parent/author/reviewer findings remain permanent. Withdrawn trial/guidance has ZERO credit and is not repeated/replayed/back-converted. Correct mathematics is no clean cognition/runtime/history census or process cure.

All counts/group/algebra arguments are exact WRITTEN proofs, not machine/kernel checked. Only static source reads, metadata hashes/LF and actual clocks were tools. No scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, dead-kernel restart, author/shared/frozen edit, git, deletion or publication. Same18/exclusiveOWN/HOLD/science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/substantive<=30min checkpoints; no formal/human/family/kernel/executable/triple/priority/novelty acceptance, new owner/deadline, early final park or round closeout. Original research continues.
