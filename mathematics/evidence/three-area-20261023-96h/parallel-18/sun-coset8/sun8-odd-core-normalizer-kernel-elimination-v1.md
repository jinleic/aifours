# Sun8: odd core-normalizer kernel eliminated globally; only three actual section types remain — v1

Owner MathSun8 / math-6. Actual clock: `Sun Oct 25 13:29:57 PDT 2026`.
Status: **NEW WRITTEN CANDIDATE at the named literal-odd/NC7/UNIFORM-SIX union.** No pending source is silently accepted and no local model is called an actual group/coset witness. HOLD/v9/v10/v11: no scientific eval, program, arithmetic interpreter, enumeration, symbolic execution, replay, external CLI or nested agent.

## 1. Exact imported boundary

Use ONLY the odd literal-kernel case of `sun8-core-normalizer-uniform-six-descent-v1.md` (119 LF, SHA256 `b19775f9052b06bbc37e31ab40592b41b2007d955acb937096230838f635c634`), whose NC7 input is the separate 187-LF candidate `sun8-prime-seven-completion-core-normalizer-v1.md` (SHA256 `53e917db64bc74d60aedb0acf0f25f671ee51633d9aade17747a766a1ab33caf`). The actual odd kernels originate in `sun8-odd-normalizer-ternary-character-reduction-v1.md` (190 LF, SHA256 `195f7f0e6f867bd4d3736a0dabdbd415d305af951f1e938411f7da729c96dd42`). Applicability of that entire source to all unhandled Sun8 vertices is NOT assumed.

Explicitly, in the SAME finite group G and achieved minimum-P7 family the selected original coset is U, [G:U]=7r_i, the other seven original left cosets are a_jU_j with indices 7r_j, and all private r's are pairwise coprime. Put N=N_G(U), [G:N]=7s, N/U=C3^2, r_i=9s odd. There is an ACTUAL subgroup B<=U normal N with U/B=C2, N/B=C2 times Q for Q=C3^2. Six regular neighbours have [B:B∩U_j]=r_j and [N:N∩U_j]=6r_j. Their N/B intersections are {1} times ker chi_j, with three of each of TWO independent ternary directions a,b. The exceptional private r_e is even and [B:B∩U_e]=r_e/2.

At the imported candidate boundary M=N_G(B) has index 7t, t|s, h=[M:N]=s/t odd. Set R=M/B, S=U/B=C2 and N0=N/B=C2 times Q. UNIFORM-SIX gives for ALL SIX original regular subgroups K_j=B(M∩U_j)/B of index SIX in R, and their support in the ACTUAL 7t M-cells has size 6t. The normalizer of S in R is EXACTLY N0: normalizing U/B in M/B is equivalent to normalizing its full inverse image U in M. Since N<=M, that normalizer is N/B. An involution's normalizer is its centralizer.

Let C be the intersection of core_R(K_j) over all SIX regular j. The imported candidate proves C∩N0=1, |C| divides h, and R/C embeds in (S6)^6. If e misses the initial M-cell then C=1. Otherwise C acts faithfully on the exceptional coset space R/K_e, whose index is 2 alpha_e with 1<=alpha_e<=7; all C-orbits have the SAME size d dividing alpha_e and |C|. The selected subgroup S must NOT be declared disjoint from the exception after quotienting by C. The following proof only uses disjointness of REGULAR/REGULAR and REGULAR/EXCEPTION images, which remains valid because regular images are full C-fibres.

## 2. An odd normal subgroup and its elementary-ternary quotient

The two-part of |R|=18h is exactly two. There is a normal odd-order subgroup P of index two. For completeness, use the sign of the LEFT regular action of R on itself: every involution is a product of |R|/2 transpositions, an ODD number, so the sign homomorphism is onto C2 and its kernel has odd order. Every odd-order subgroup of R lies in this kernel. In particular all K_j lie in P, because their index six removes the entire two-part of |R|. Also C<=P, and S is an actual order-two complement to P.

Consider a six-point coset action R/K_j. Since P is normal, all P-orbits in this transitive action have equal sizes dividing six. Their sizes are odd, hence one or three. They cannot be one: then P would act trivially and the whole action would factor through R/P=C2, which is not transitive on six points. Thus there are TWO three-point P-orbits. An odd-order permutation group on three letters is contained in A3=C3. The image of P in this action is consequently contained in C3 times C3.

Taking all six actions, their common kernel is C by definition. Hence **P/C is elementary abelian of exponent three**. No classification of transitive degree-six groups, solvability theorem, computed catalogue or finite enumeration is imported.

Write barR=R/C and barP=P/C. The embedded Q in N0 survives injectively because C∩N0=1. Every barK_j=K_j/C is a hyperplane of the ternary vector space barP: its index there is three. Its intersection with Q is ker chi_j. Thus a regular of class a and a regular of class b define INDEPENDENT linear forms on barP, since their restrictions to Q already have independent directions.

Within a fixed one of the TWO cosets of barP in barR, cosets of those two different hyperplanes ALWAYS intersect. This is the surjectivity of the map barP -> F3^2 given by two independent linear forms. Therefore disjoint regular images of different global classes must occupy OPPOSITE barP parities in any M-cell where both original cosets are present.

## 3. If C were nontrivial, its involution action would force a prime orbit size

Suppose C>1. Then e meets M, by the imported minimum argument. The involution S normalizes C and has no nonidentity fixed point there: a fixed c would centralize S, so c would lie in C∩C_R(S)=C∩N0=1.

Here is the elementary fixed-point-free involution argument, rather than a Frobenius-kernel or Thompson import. Let sigma denote conjugation by the generator of S. The map f(c)=c^{-1}sigma(c) is injective: equality for c_1,c_2 implies c_2 c_1^{-1}=sigma(c_2 c_1^{-1}), hence c_1=c_2. Finiteness makes f bijective. Also sigma(f(c))=f(c)^{-1}. Thus sigma is inversion on ALL of C. Inversion being an automorphism implies that C is ABELIAN. It is odd-order because |C| divides h.

On any C-orbit in R/K_e an abelian transitive group acts regularly after factoring out the point stabilizer. All orbit sizes equal d, where d|alpha_e<=7 and d is odd. Faithfulness and C>1 rule out d=1. Consequently d is one of the PRIMES 3,5,7. Each orbit image is cyclic of order d, so C even embeds in a product of copies of C_d; no stronger group-theoretic input is needed.

Because [R:K_e]=2 alpha_e divides |R| and |R| has two-part exactly two, alpha_e is ODD. The only odd multiple of d not exceeding seven is d itself. Hence

alpha_e=d in {3,5,7}, and [barR:barK_e]=[R:K_e C]=(2 alpha_e)/d=2.

This index-two subgroup barK_e must be barP: it is odd-order and any odd-order subgroup of barR lies in its normal odd subgroup barP. Therefore the projected exceptional coset in barR is ONE ENTIRE parity of barP.

## 4. A global three-source cell is forced, giving C=1

Choose ONE original regular neighbour j of global class a and ONE k of global class b. Their actual M-cell supports each have size 6t. The exception has support alpha_e t=d t. The common support of these THREE original cosets has size at least

(6t)+(6t)+(d t)-2(7t)=(d-2)t>0.

This is a written union bound on the complements of three actual supports. It uses the same seven original neighbours and actual G/M, not separately selected local configurations. Select a cell in that nonempty intersection and translate it into M.

The regular projected cosets in R are full C-fibres because C<=K_j,K_k and C is normal R. Thus their pairwise disjointness, and their disjointness from the exceptional projected coset, persist on passing to barR. In contrast, selected S/exception disjointness is NOT asserted after this projection and is not used.

By §2 the two regular cosets have opposite barP parities, since their hyperplane directions are independent on the actual Q. By §3 the exceptional projected coset is one ENTIRE parity. It therefore meets one of those two regular cosets. Lifting that overlap through the full C-fibre of the regular coset gives an overlap already in R. The private B-kernel coprimalities then give an intersection of original cosets in G, a contradiction.

We conclude:

> **ODD CORE-KERNEL ELIMINATION: C=1.**

This is a GLOBAL exclusion of the actual common kernel, including both whole and aligned exceptional branches and every possible d=3,5,7. It is not an abstract no-lift assertion or a rank bound. The genuine one-exception-collision enlargement from the preceding packet cannot survive in this odd literal-kernel setting.

## 5. Class partners have the SAME actual subgroup; only dimensions 0,1,2 remain

Now P itself is elementary abelian over F3, by §2 and C=1. R=P semidirect S. The fixed space of S on P is EXACTLY Q: C_R(S)=N0=S times Q. Because two is invertible in F3, decompose P=Q direct-sum T, with S acting as +1 on Q and -1 on T. These are the written projections (1+sigma)/2 and (1-sigma)/2; no interpreter is involved.

All six regular M-cell supports have size 6t in a universe of size 7t. Their simultaneous intersection therefore has size at least 7t-6(t)=t>0. In one such actual cell ALL SIX projected regular cosets are pairwise disjoint index-six cosets in R. Each lies in one parity and cuts that parity by a ternary affine hyperplane.

Different global classes cannot occupy the same parity by §2. Since both classes occur, all three a-cosets occupy one parity and all three b-cosets the other. Three disjoint affine hyperplanes in one parity must be parallel: two nonparallel hyperplanes in a vector space always intersect. Thus ALL THREE class-a subgroups K_j are one ACTUAL hyperplane K_a of P, and ALL THREE class-b subgroups are one ACTUAL hyperplane K_b. This is equality of the full subgroups in M/B, not just equality of their intersections with N/B.

Choose defining nonzero linear forms ell_a,ell_b on P, scaled so their restrictions to Q are the independent original a,b. Write ell_a=a+f_a and ell_b=b+f_b on Q direct-sum T. Since P is abelian, core_R(K_a)=K_a∩K_a^S, and similarly for b. The defining four forms are a+f_a, a-f_a, b+f_b, b-f_b. Their common kernel is zero because C=1. As two is invertible, that common kernel is equally the common kernel of a,b,f_a,f_b. The first two separate Q; hence f_a,f_b separate T, so k=dim T<=2.

Therefore at this EXACT candidate union the ACTUAL section and indices obey

> R=M/B is isomorphic to C3^2 times (C3^k semidirect_{inversion} C2), with k=0,1 or2; |R|=18,54 or162; and h=[M:N]=3^k=1,3 or9.

The list is NECESSARY, not a claim that all three lift to actual eight-coset counterexamples. For k=1,2 the section is nonabelian. The full G and B are not bounded. In particular all prime factors other than three in s retain their FULL multiplicity in t. If 3 does not divide s, then M=N. The earlier optional simple-G exclusion t=1 stays an additional named boundary, not a proof of the remaining cases.

The actual global factorizations remain M=N(M∩U_j), and the SIX full original normalizer indices are still [U_j:N_{U_j}(B)]=6t. This classification does not replace the full original U_j by their small images.

## 6. The exception is also actually aligned at M, not just at N

The actual subgroup K_e exists irrespective of whether its GIVEN coset meets the initial M-cell. Its index in R is 2 alpha_e, with 1<=alpha_e<=7. Since |R|=2 times a power of three, necessarily alpha_e=1 or3.

If alpha_e=1, K_e=P, so any coset of K_e in R contains one element of S. The exceptional coset therefore CANNOT meet the initial M-cell, because the selected original U is disjoint from it and selected S/exception disjointness DOES hold in R when C=1. This is actual hiddenness in M, stronger than merely in N.

If alpha_e=3, K_e is an index-three hyperplane in P. Suppose it differs from BOTH K_a and K_b. Take again one original a-regular and one b-regular. Their supports are 6t each and the exception's is 3t, so all three are present in at least t actual cells. In such a cell three pairwise disjoint cosets with three distinct hyperplane directions would have to occupy two parities. Two of them share a parity, where distinct hyperplanes always intersect. This contradiction proves **K_e=K_a or K_b**. It is equality of actual subgroups of M/B, not mere coincidence of the character direction on N/U.

For the last interpretation also import the literal odd endpoint alternatives [N:N∩U_e]=r_e (whole) or 3r_e (aligned). In the whole case A_e=B(N∩U_e)/B has index two in N0 and equals Q; in the aligned case it has index six and is the corresponding line ker delta in Q. But K_a∩N0 and K_b∩N0 are lines, not Q. Thus the whole case cannot have alpha_e=3: it has alpha_e=1, K_e=P and the given exceptional coset misses M. The aligned case has alpha_e>=3 and hence alpha_e=3; its K_e is EXACTLY the regular class identified by delta.

No unproved finite computation is promoted in this argument. Actual e index, whole/line subgroup intersections and full-source support sizes are all used in the same quotient and same global cells.

## 7. Exact residual and assurance

This successor eliminates the ENTIRE common regular-action kernel in the literal odd branch, classifies its actual M/B section into the three displayed necessary types, proves global class-partner subgroup equality and upgrades exceptional alignment/hiddenness to M. It applies equally to the initial-rank-one aligned pattern: no step required two regular classes to be visible in the INITIAL N-cell; only the TWO GLOBAL original classes and forced triple-cell intersections were used.

**First remaining step:** eliminate the actual k=0,1,2 section lifts with all full U_j motions of index 6t and all outer G/M cells, or construct a genuine source-preserving enlargement beyond the now-faithful section. Whole and aligned e support sizes are respectively t and3t. A bounded section does not bound the outer odd t, authenticate global Sun7, exclude an arbitrary Sun8 counterexample or produce an actual eight-coset witness.

The odd regular-character-rank<=1 branch and every binary low-rank/nonabelian/maximal/self-normalizing branch outside the explicit literal kernels remain open. There is no configured-family review, formal/kernel proof, independent-parent acceptance, numerical-bound promotion, novelty clearance or round completion. This is an ADDITIVE written candidate and all frozen predecessors/errata remain unchanged.
