# Sun8: binary common kernel globally reduced to order four or sixteen; fractional branch eliminated — v1

Owner MathSun8 / math-6. Actual clock: `Sun Oct 25 13:49:33 PDT 2026`.
Status: **NEW WRITTEN CANDIDATE at the literal binary/NC7/UNIFORM-SIX union**, not accepted by composition. HOLD/v9/v10/v11: no scientific interpreter, program, arithmetic eval, enumeration, symbolic execution, replay, external CLI or nested agent.

## 1. Exact actual input; no new applicability claim

Use the SAME actual minimum finite-P7 family in G, selected original coset U and seven other original left cosets a_jU_j, indices 7r_i and 7r_j, all private r's pairwise coprime. N=N_G(U), [G:N]=7s, N/U=C2^3=Q, r_i=8s. Let B<=U be ACTUAL and normal N. The six regular original neighbours satisfy [B:B∩U_j]=r_j, [N:N∩U_j]=6r_j. Either S=U/B=C3 and N0=N/B=C3 semidirect Q, with A_j=B(N∩U_j)/B complementary to C3 and projecting onto ker chi_j; or S=S3 and N0=S3 times Q, with A_j=P_j times ker chi_j for order-two P_j<=S3. The SIX global chi_j have three paired independent classes a,b,c. No condition says all three classes are initially visible.

The exceptional kernel is either r_e/3 (ordinary) or 2r_e/3 (fractional, in its actual binary source branch). In particular 3|r_e, so 3 does NOT divide s. In the fractional case the regular private r_j are odd, making all other B-kernel indices pairwise coprime. There is no claim that these literal kernels cover binary rank<=2 or arbitrary nonabelian N/U.

Named new imports: `sun8-prime-seven-completion-core-normalizer-v1.md` (187 LF, SHA256 `53e917db64bc74d60aedb0acf0f25f671ee51633d9aade17747a766a1ab33caf`) and `sun8-core-normalizer-uniform-six-descent-v1.md` (119 LF, SHA256 `b19775f9052b06bbc37e31ab40592b41b2007d955acb937096230838f635c634`). They are UNREVIEWED candidate premises here. The literal binary kernel sources are named at the end; no transitive import is silently re-proved.

At that boundary M=N_G(B) has index 7t with t|s; h=[M:N]=s/t is three-free. Set R=M/B, S=U/B and N0=N/B. For ALL SIX regular j, K_j=B(M∩U_j)/B has index SIX, R=N0 K_j, and the original coset has support 6t among the ACTUAL 7t left M-cells. Also N_R(S)=N0 exactly. Thus C_R(S) is contained in N0.

Let C be the intersection of core_R(K_j) over ALL SIX original regular subgroups. The imported uniform-six candidate gives C∩N0=1, |C| divides h, and R/C embeds faithfully in (S6)^6. It also gives: if e misses the initial M-cell then C=1; otherwise C acts faithfully on R/K_e, where gamma=[R:K_e] is 3 alpha_e (ordinary) or 3 alpha_e/2 (fractional), 1<=alpha_e<=7. All C-orbits in that space have the SAME size d. For ordinary kernels d divides alpha_e and |C|; for fractional ones d divides alpha_e/2 and |C|. The entire group R has three-part EXACTLY three.

Only REGULAR/REGULAR and REGULAR/EXCEPTION disjointness is retained on passing from R to barR=R/C: regular cosets are full C-fibres because C<=K_j. Selected S/exception disjointness after C is NOT available and is never used below.

## 2. Three independent regular footprints saturate every S-fibre they jointly meet

Here is the local reconstruction needed for the global exclusion. Suppose L<=barR has index THREE. The kernel of the three-point coset action has three-free order: the transitive image has three-part three, just as barR does. An order-three subgroup P3 of the selected S therefore maps to a three-cycle. Consequently the embedded N0 is TRANSITIVE on barR/L.

Every regular barK_j=K_j/C also has index six and barR=N0 barK_j. Thus its given left coset meets EVERY left N0-coset, and so does a coset of L. To see the orientation explicitly, N0 barK_j=barR implies barK_j N0=barR by inversion; hence x barK_j intersects gN0 for every g. The same holds for L.

Restrict three regular cosets of the independent global classes a,b,c and one L-coset to one common left N0-coset and translate into N0. The three regular intersections are left cosets of the ACTUAL A_j. Their Q-footprints are affine hyperplanes chi_j(q)=epsilon_j in the three independent binary directions. They have a common Q-point regardless of the three affine constants. In its S-fibre the intersections have cardinality |S|/3 each. Their disjointness therefore makes them cover the ENTIRE S-fibre: three singletons if S=C3, or three pairs if S=S3.

The fourth intersection is a coset of an index-three subgroup H of N0. This H has order eight when |S|=3 and sixteen when |S|=6. It is a two-group. Its intersection with S has order at most |S|/3, so its projection onto Q has order at least eight and is ALL Q. Its coset consequently meets the saturated S-fibre, contradicting pairwise disjointness.

We have proved a concrete statement with full quantifiers:

> **THREE-CLASS SATURATION:** in one actual M-cell, three simultaneously present regular neighbours of the three independent global classes cannot be disjoint from an exceptional barR-image of index three.

The argument uses the SAME N0, the SAME original regular intersections A_j, and the SAME global classes. It does not choose separate local cores or require those three neighbours to be visible initially.

## 3. The support count removes every large C-orbit and the fractional kernel

Choose one original regular neighbour from each class a,b,c. Each has M-cell support 6t. The exception has support alpha_e t. Their FOUR common support has size at least

3(6t)+alpha_e t-3(7t)=(alpha_e-3)t.

Thus if alpha_e>3, there is an ACTUAL M-cell containing all four original cosets. Their projected disjointness in barR, insofar as a regular coset is involved, follows from its full C-fibres and the original B-kernel coprimalities. If the exceptional image in barR has index three, §2 then gives a contradiction.

Ordinary kernel: gamma=3 alpha_e divides |R|, whose three-part is three. Hence alpha_e is in {1,2,4,5,7}. If C>1, faithful action rules out d=1; d is three-free and divides alpha_e. The possibilities are d=2,4,5,7. Whenever d=alpha_e is 4,5 or7, the exceptional image in barR has index gamma/d=3 and alpha_e>3; it is excluded by the preceding four-source support count. Thus the ONLY nontrivial possibilities are

d=2, alpha_e=2, or d=2, alpha_e=4.

Fractional kernel: gamma=3 alpha_e/2 is integral and has three-part at most three. Therefore alpha_e is even, and alpha_e=6 would give forbidden index nine; only alpha_e=2 or4 remains. If C>1 then d>1 divides alpha_e/2, forcing alpha_e=4 and d=2. But its image in barR has index gamma/d=3 and alpha_e=4>3, again contradicting §2 and the actual four-source intersection. Therefore

> **FRACTIONAL BINARY KERNEL: C=1.**

No large-prime d=5/7, d=4, or fractional-kernel common-action core survives this GLOBAL argument.

## 4. In the ordinary residual the common kernel is exactly elementary abelian of order four or sixteen

In both remaining ordinary alternatives d=2, so C acts faithfully on a union of two-point orbits. Each orbit image is C2. Hence C is ELEMENTARY ABELIAN over F2, not merely of bounded elementary rank. The number of those orbits is gamma/d=3 when alpha_e=2, and six when alpha_e=4.

The selected S has no nonzero common fixed vector in C: such a vector would centralize S and lie in C∩N0=1. If S=C3, an order-three generator P3 therefore has no nonzero fixed vector. If S=S3, let F be the fixed space of its normal order-three subgroup P3. F is stable under S and the action on F factors through S/P3=C2. Any involution on a nonzero F2-space has a nonzero fixed vector: a nonfixed v gives the nonzero fixed vector v+tau(v), while a fixed v already suffices. Thus F would give a nonzero S-fixed vector. Hence F=0 here too.

Embed C into F2^m by the actions on its m two-point orbits, with m=3 or6. Conjugation by P3 permutes these coordinates EXACTLY, since C2 has no nontrivial automorphism. For any vector of C the sum v+sigma(v)+sigma^2(v) is P3-fixed and is zero. Each coordinate fixed by sigma is therefore zero, and on each three-cycle the three coordinates sum to zero. There are at most floor(m/3) such cycles, giving dimension at most 2 floor(m/3).

The dimension is positive and even: the nonzero vectors form three-cycles under P3, so 3 divides 2^r-1, forcing r even. Consequently

* alpha_e=2 forces C=C2^2, of order FOUR;
* alpha_e=4 permits only C=C2^2 or C2^4, of order FOUR or SIXTEEN.

These are exact necessary isomorphism types of an ACTUAL normal subgroup of M/B. They do not bound G's involutions by its elementary rank or assert that any listed type lifts to an actual eight-coset family.

## 5. The alpha-four residual has an expanded C-type exception, not a whole footprint

Suppose alpha_e=4 and C>1. The exceptional subgroup L=K_e C/C has index SIX in barR. It is three-free, because both K_e (index twelve in R) and C are three-free. Consequently H=N0∩L has index divisible by three and at most six in N0: its index is THREE or SIX.

There is an actual M-cell containing the three independent regular classes and e, by §3. Choose a left N0-coset met by that exceptional image; all three regular images meet it too, since barR=N0 barK_j. If [N0:H]=3, §2's saturation contradiction applies. Hence [N0:H]=6. If H projected onto ALL Q, its coset would again meet the saturated S-fibre at the joint point of the three regular footprints. Thus its Q-projection has index two, ker delta, and |H∩S|=|S|/3.

For S=C3, H is complementary to S over that binary hyperplane. For S=S3, H is a two-subgroup of S3 times Q. Its S3-projection has order at most two, while H∩S3 already has order two; hence H=P_e times ker delta for an order-two P_e. Thus the EXPANDED exceptional intersection at N0 has precisely the regular C-type form. No claim is made here that delta is one of a,b,c, or that the original exception is disjoint from selected S after quotienting C.

This is an actual full subgroup intersection in the same barR, not an arbitrary local partition. The original A_e=N0∩K_e is contained in H with index at most two; its original Q-footprint must remain a subgroup of this index-two Q-footprint. The source's exact original endpoint patterns, when used, remain additional named imports and are not replaced by an invented beta=1 assertion.

## 6. Whole original footprints have C=1; alpha-two forces the missing-class A2 corner

For this refinement use the original Q-footprint of A_e and the achieved-minimum blind-overgroup argument, rather than identify a pattern from alpha_N alone. A WHOLE footprint means A_e projects onto ALL Q; this includes the ordinary beta-two whole case when S=S3, not just the beta-one whole case.

Such an exceptional GIVEN coset cannot meet N: an image with full Q-footprint meets Q=0, whose full S-fibre is selected U/B. All visible regular Q-footprints are normalized chi_j=1, since they avoid selected U. If their visible characters did not span Q^*, their common kernel would contain a nontrivial subgroup of Q. Its actual inverse image in N would enlarge U, avoid every original coset visible in N and also every original coset absent from N, and lower a private index by a divisor. Minimum forbids that. Thus in the whole case THREE independent regular classes are visible in N and jointly fill an S-fibre at chi_a=chi_b=chi_c=1.

If the residual had alpha_e=2, its barR-image has index three and meets N0 in a coset projecting onto ALL Q. The three visible original regular images persist unchanged in N0, since regular images are full C-fibres and C∩N0=1. Their saturated fibre would meet that exception, a contradiction. If alpha_e=4, §5 says the expanded exceptional Q-footprint has index two; it cannot contain the original full Q-footprint. Thus

> **ANY WHOLE ORIGINAL EXCEPTIONAL FOOTPRINT: C=1**, including the ordinary S3 beta-two case. The fractional case already has C=1 by §3.

Now consider the ordinary alpha_e=2 residual. Its expanded exceptional intersection H at N0 has index three. Since [K_e C:K_e]=d=2, the original A_e has index at most two in H. Its Q-projection consequently has index at most two. Whole footprints were just excluded, so it has index exactly two, say ker delta, with the ordinary A2 fibre size |S|/3. It is not an A4 footprint or a beta-two whole footprint.

The same N0 saturation shows that there cannot be THREE original regular cosets visible in N: their characters are drawn from the three independent global classes and all visible footprints have value one, so any such three have a common Q-point; their disjoint S-fibres fill it. The expanded index-three exceptional coset would meet it.

There must nevertheless be enough visible footprint directions to span Q^*: otherwise the actual inverse-image blind overgroup lowers the selected private index. With at most two visible regular directions, the A2 exception must itself be visible in N, and exactly TWO regular cosets are visible, from distinct classes X,Y. Their directions together with delta span rank three. Thus delta lies OUTSIDE span(X,Y): writing Z for the missing global regular class,

delta=Z+epsilon_X X+epsilon_Y Y, with epsilon_X,epsilon_Y in F2.

We have therefore localized this remaining case to the **genuinely visible missing-class A2 corner**, with actual C=C2^2 and alpha_e=2. This does not exclude that corner or manufacture its full group/coset lift.

## 7. Arithmetic/source transport consequences and exact residual

In the ordinary branch either C=1, or the only unresolved common kernels are the displayed C2^2/C2^4 aligned residuals. In the fractional and all whole-footprint branches C=1. Since R/C embeds in (S6)^6 and C is a two-group, every prime divisor of |R| is in {2,3,5}. Since h=[M:N] is three-free, **h has only primes TWO and FIVE**. Thus every prime at least seven in the selected s keeps its FULL multiplicity in t=[G:M]/7. This is stricter than the preceding seven-smooth bound, but it does not itself delete any original private prime.

The full-source equalities [U_j:N_{U_j}(B)]=6t and M=N(M∩U_j) for all six regular neighbours remain in force. If C>1, its inverse-image subgroup C0 and the actual Tlift=C0∩ALL SIX U_j still give U Tlift as a global enlargement preserving all six original left cosets; only the genuine exceptional collision remains. No fake replacement by M or independent local lift is asserted.

**First unproved step:** eliminate the actual order-four missing-class A2 kernel, or the alpha-four order-four/order-sixteen aligned kernel, or the faithful C=1 section, while retaining the full original U_j and outside-M motion. The R/C six-point quotients may still involve the prime five; it has NOT been excluded by an unprovided transitive-group catalogue. Other binary global-character-rank<=2/nonabelian N/U/maximal branches outside the literal kernel data, and unrestricted Sun8/global Sun7 provenance, remain open.

Literal kernel imports, not re-reviewed here: `sun8-six-fibre-quotient-rigidity-v1.md` (210 LF, SHA256 `6bf2f0a5ab5d2269d4fb7f8b88cece184101c19f00646b72cb0b9c614da47589`); `sun8-global-kernel-e-lift-union-candidate-v1.md` (139 LF, SHA256 `4ebb50bf5a5c9daadf7dfc9a48b9fb1fc0401da56f45b1bb10a768fa8f868f03`); `sun8-global-character-rank-three-reduction-v1.md` (202 LF, SHA256 `129bf888485c1539ab955298a8b3130294730ed841496f35f298441a854540c5`). No claim extends to a source-preserving actual eight-coset witness, formal/kernel proof, configured-family acceptance, independent-parent acceptance, numerical bound, novelty clearance or round completion.
