# Sun8 — COMPLETE SL2(q), all finite fields, actual central lifting at NC7

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 17:53:57 PDT 2026**. NEW COMPLETE WRITTEN CANDIDATE, NOT ACCEPTED. Entire current184LF PSL2 proof SHA `0298c21acf78728375ca7f708a70a9f1d22ecc0756089852c57fa1efffe0ad60` is a correctness input, including its actual root/field/Sylow derivations and full q9 normalizer/common-action proof, not merely its theorem headline. This SL2 result does NOT consume the PGL2 theorem or its SUN4 premise.

Permanent OWN cadence PROCESS MAJOR057(16:58:10→17:31:20 observed33m10s, no intervening required JSON) and earlier047metadata-polling/M1/v9/v10/v11/HOLD/source histories remain. No cure/backdating/clean-runtime assertion. No scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nestedagent/newGO.

## 1. Exact original theorem and inputs

> **SL-SUN8:** for EVERY finite field q≥2, EIGHT disjoint nonempty LEFT cosets of arbitrary subgroups of G=SL2(q) force a pair of ACTUAL subgroup indices with gcd≥8.

All original eight cosets/full indices remain. No P7/Sun7/R8/cofactor/minimum/quotient-saturation/rank/natural-subgroup ansatz. In particular the statement does NOT assume every original subgroup contains the centre; that is proved only where needed, and noncentral sources are preserved inside an actual lifted complement.

Research-sized input is ONLY current exact **NC7**,181LF predecessor Part2 SHA `2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8`, at its named A7/Eisenstein boundary, used only q7. No global Sun7/R8, SUN4, Dickson/minimal-index/CFSG/Jordan/Bertrand or historical arithmetic. The full new PSL2 proof remains unaccepted until a whole union gate; ordinary group/field/matrix reasoning here is written, not formal/kernel verification.

## 2. Actual SL2 root argument, not the PGL index-two exception

For even q the centre is trivial and SL2(q)=PSL2(q), settled by the full PSL source. Assume henceforth q=p^f ODD. Here |G|=q(q²−1), centre Z={1,z},z=−I. Upper/lower full root groups generate WHOLE SL2 by the exact elementary matrices in Part1. The projective-line action has kernel Z and B_infinity of orderq(q−1), indexq+1, with root U of orderq.

Every proper p-free-index H contains a full conjugate root U. If it contains an element outside B, adjusting that point by U supplies the full opposite root, hence H=G. Thus ALL proper p-free-index H are Borel-contained, and q+1 divides their ACTUAL index. There is NO remaining index-two PSL exception: in SL2 the two roots generate the whole group, even q3 where simplicity/perfectness is not asserted.

For non-Borel H with a=v_p(I),1≤a<f, write s=p^a,u=q/s. As in the full fixed-point proof, P=H∩U=u(A) has orderu, N_H(P)=H∩B orderu*t. The SL2 torus parameter is a0∈F_q^*, acting on translations by a0². Thus its image of size t/gcd(t,2) stabilizes A. The scalar-stabilizer field has degree e|gcd(f,a), giving

t|gcd(q−1,2*(p^e−1)).                                      (SL-T)

This factor2 is essential; treating the SL torus as a faithful PGL multiplier would lose actual subgroups. Sylow subgroups have distinct unique fixed points, their number n=1+k*u with1≤k≤s. Exact ambient order yields

I=s(q²−1)/(t*(1+k*u));  1+k*u | s²−k².                     (SL-COUNT)

The second relation follows by n|q²−1 and k*u=−1 modn. For u≥s² the positive remainder for k<s is smaller than n, so only k=s, n=q+1 and I=s(q−1)/t. No determinant/computation replay or subgroup classification is used.

## 3. All large odd fields

If p>7, at most one original index is p-divisible; the at least seven p-free ones all share q+1>7 by §2, contradiction.

For p3/5/7 and f≥3, at most one original source has p²-divisible index. Every non-Borel a1 source has u≥p² and t|gcd(q−1,2(p−1)), so its index is a multiple of

p*(q−1)/gcd(q−1,2(p−1)) ≥ p*(q−1)/(2(p−1)) ≥39/2>7.

Every Borel source shares q+1>7. These Borel/high-p²/non-Borel-regular buckets cover ALL sources and each has at most one under gcd≤7. Thus no eight-family. This uses the exact nonfaithful torus bound, not a falsely identical PSL/PGL order.

## 4. Entire q25/49 bases, including all enlarged torus candidates

For f2, a1 has e1, so t divides2(p−1). The same complete k-remainders as Part1 leave k1/3/5 for q25 and k1/2/7 for q49. Using(SL-COUNT), the FULL necessary over-approximations are:

|q|k|ALL t giving integral I|ALL I|shared divisor|
|---|---|---|---|---|
|25|1|1,2,4,8|520,260,130,65|65|
|25|3|1|195|195|
|25|5|1,2,4,8|120,60,30,15|15|
|49|1|1,2,3,4,6,12|2100,1050,700,525,350,175|175|
|49|2|1,2,4|1120,560,280|280|
|49|7|1,2,3,4,6,12|336,168,112,84,56,28|28|

q25,k3 has I195/t, so no even t works; q49,k2 has I1120/t, so no3-divisible t works. Every displayed row has common divisor>7, giving at most three regular sources. The Borel and high-p² buckets add at most two. Hence at most five, not eight. Some candidates(e.g. q25,k3,t1) may violate the central involution condition below; retaining them is a safe NECESSARY over-approximation, not an actual subgroup or lift claim. No valid subgroup was dropped by that over-approximation.

## 5. Entire q3/5 small odd bases, no SUN4 input

For q3 the group has order24. ROOT excludes all p3-free proper indices not divisible4, including2. Necessary indices are{3,4,6,8,12,24}. Among8/12/24 at most two can occur:24 has forbidden gcd>7 with either other, and repetitions of high values are forbidden. At least six original indices are≤6; their mass already≥1, with the remaining nonempty cosets adding positive mass. If more than six are low their mass is>1 already. Disjointness is impossible.

For q5 the group has order120. ROOT excludes p5-free proper indices not divisible6, including2/3/4/8. Necessary indices are{5,6,10,12,15,20,24,30,40,60,120}. If5 occurs,6/12/24 cannot coexist by coprime-index intersection. Of10/15/20/30/40/60/120 only pairs joining15 to10/20/40 have gcd≤7. Thus at most two high sources plus at most five index5 sources: fewer than eight.

Without5, a compatible high set in{10,12,15,20,24,30,40,60,120} has size≤3:60/120 are isolated,30 has only incompatible neighbours12/24; otherwise at most one of{12,24}, one of{10,20,40}, plus15 can occur. Eight would require at least five index6 sources. Six fill G, so exactly five. Every ACTUAL index6 subgroup is Borel-contained by ROOT and has the same index as B, hence equals an actual Borel. All five cosets are point constraints in the SAME natural projective action on SIX points. That action is two-transitive(root translations already make a point stabilizer transitive on the other five); faithfulness is not required.

Disjoint constraints are a rook clique, hence their whole complement is the missing sixth index6 coset. Each of the three remaining original cosets must lie wholly there and have index divisible6. In the high candidates only{12,24,30,60,120} qualify, and a compatible set of those has size≤2:60/120 are isolated,12/24 incompatible,30 joins at most one. Contradiction. With neither5 nor6, there are at most three sources from the high graph. This is an actual common-action lift argument, not the PGL theorem, an S5 isomorphism or SUN4.

## 6. Entire q7 base, NC7 only

Here |G|336 has7-part7; every7-free proper index is Borel index8 times an integer, so at most one. Among at least seven7-divisible sources write I_j=7r_j,r_j|48; gcd≤7 implies r_j pairwise coprime. At most two r_j>1, so at least five source cosets have index7. Any7-free source would meet each ordinary index7 coset by coprime-index intersection; thus none occurs. All eight are7r_j and at least six ordinary.

Exact NC7 gives the ONE index7 complement of six original ordinary cosets. The remaining two whole original cosets lie there. Their subgroup indices inside this actual complement are their original coprime r_j, forcing intersection. No source was independently enlarged or projected. Kernel Z/fibre parity was not presumed; NC7's full ANY-group scope is the named input here.

## 7. q9 actual central mechanism, including noncentral hidden sources

This is the only surviving low-index regular base. First, over an odd field the ONLY nonidentity involution in SL2 is z=−I: A²=1 has a square-free minimal polynomial dividing(X−1)(X+1), so A is diagonalizable with eigenvalues±1; determinant1 forces both eigenvalues equal, hence A=±I. In any even-order subgroup, inverse-pairing leaves a nonidentity self-inverse element, so every even-order subgroup contains z. This is a written elementary argument, not an imported split-lift assumption.

For q9, a1,u3,t|4. The complete k-list is1(n4) or3(n10), since k2 fails7|5. Both Sylow counts are EVEN, so every regular H has even order and contains z. Since z is central it lies in N_H(P), making t EVEN. Thus t2/4 only; the ACTUAL necessary indices are

k1:60/t=30,15;  k3:24/t=12,6.

The tempting t1 indices60/24 are impossible here; in contrast, their safe over-approximations were allowed in §4. All these q9 regular source cosets are Z-saturated. Borel sources(q+1=10) number at most one, high-p²=9 sources at most one, hence at least six originals are regular.

Among non6 regular values12/15/30, there are at most two compatible sources(15 and30 are incompatible, repetitions exceed7). Hence index6 exists, in fact at least four. Its subgroup contains Z, giving a genuine index6 subgroup in Q=G/Z=PSL2(9). Q is simple of order360 by the full root/perfect/primitive derivation in Part1; its index6 action is faithful, lies in A6 by perfectness, and has order360, so identifies Q with the actual A6 action.

The whole written q9 normalizer proof in Part1 now excludes order30 subgroups of this actual A6: a Sylow5 count1 puts the subgroup in a normalizer of size10; count6 accounts for24 elements of order5, forcing the Sylow3 subgroup normal(ten would contribute20 further elements), whereas the normalizers of BOTH possible3-cycle types have size18. Thus no order30 subgroup, without a subgroup catalogue. An original index12 regular subgroup contains Z and would map to just such an order30 subgroup of Q; therefore NONE occurs.

The non6 regular set is now{15,30}, with at most one. Consequently at least FIVE index6 source cosets occur. They are all Z-saturated, so their images in Q are disjoint. Fix one actual degree6 action as above. Any other index6 image subgroup cannot act transitively in that action: transitivity makes its product with the first point stabilizer equal Q and forces the two actual source cosets to meet. A nontransitive order60 subgroup in A6 fixes a point, because fixed-point-free orbit stabilizers have orders at most24(4+2),18(3+3),4(2+2+2), all<60. Hence ALL five belong to the SAME actual degree6 point-stabilizer action, not independently chosen outer actions.

Six index6 sources would already fill G, so exactly five occur. Their images have ONE missing index6 coset as complement in Q by the actual two-transitive rook argument. Its FULL preimage is ONE actual index6 coset C in SL2(9), exactly the complement of those five ORIGINAL sources. Every other original coset is therefore contained in C WHETHER OR NOT ITS SUBGROUP CONTAINS Z. No noncentral Borel/high9 source is discarded or projected as a full coset.

There are three remaining sources. At most one is regular(non6) and at most one each Borel/high9, so all three types must occur. All their ORIGINAL indices are divisible6 by actual containment in C. The non6 regular value15/30 is therefore30. The Borel index is a multiple of10 AND6, hence of30. These two distinct original sources have gcd≥30, contradiction. The high9 source was kept intact throughout; no relative-index or half-fibre substitution was made.

## 8. Entire coverage, source union and assurance

Even fields reduce by ACTUAL equality SL2=PSL2. Odd p>7/allf, odd p3/5/7 f≥3, odd f2 q9/25/49 and odd f1 q3/5/7 have ALL been closed above. The only research-sized import NC7 is used q7; no SUN4 was necessary for this SL2 theorem. All normalizer torus factors, unsaturated source possibilities, field/Sylow conditions and common-action completions were treated with their actual groups/full original indices.

A joint ENTIRE review must cover the whole184LF PSL source and this complete SL source, not infer its q9 central lift from a headline or a single even-order subgroup. In the broader current union, the108LF PGL extension is a separate third complete body with its own SUN4 index2 boundary; all three belong to ONE root/Sylow mechanism, not independent discovery counts. All are unaccepted candidates pending whole frozen review and current disposition.

No semilinear/field-automorphism group, GL2 arbitrary scalar extension, exceptional3/6-cover of PSL2(9), higher rank, arbitrary infinite G or full Sun8 is claimed. Novelty/priority/SOTA remain UNCLEAR/UNPERFORMED, and the permanent OWN33m10s cadence MAJOR/earlier047/M1/source/correction histories are not cured. WRITTEN is not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/fulltarget/root/cutoff/deadline/v9v10v11/HOLD, no scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nestedagent/GO. Primary continues at the full original arbitrary-group/source-lift residual.
