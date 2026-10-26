# Sun8 — COMPLETE original eight-coset exclusion in PSL2(q), EVERY finite field

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 17:35:52 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE AT THE EXACT NC7 BOUNDARY; NOT ACCEPTED.** All fields q=p^f, all original subgroups/cosets/indices and the original gcd-at-least8 target are retained. This is an unbounded ENTIRE group-family proof, not a guessed index list, a small-group computer survey, an eight-coset witness or full arbitrary-group Sun8.

**Permanent OWN CADENCE PROCESS MAJOR:** checkpoint056 actual16:58:10 to the next required JSON057 preceded by actual17:31:20 has reported clock gap33m10s, already>30min before057 was written. No intervening required JSON existed; proof/source/clock observations are not it. That finding and earlier histories are NOT cured by this paper, and no uninterrupted-runtime/exact-creation census is asserted. The whole rank-one lead was saved in057, not called independent/preregistered discovery. No scientific interpreter/Eval/calculator/program/CAS/enumeration/symbolic/solver/replay/CLI/nestedagent/newGO.

## 1. Exact theorem and sole named large input

> **L2-SUN8.** For EVERY finite field F_q, q=p^f≥2, EVERY EIGHT pairwise-disjoint LEFT cosets of arbitrary subgroups of G=PSL2(q) have some pair of ACTUAL subgroup indices with gcd≥8.

No P7/r_i hypothesis, Sun7/R8 reduction, normalizer rank, minimum-order/private-sum premise, natural subgroup ansatz or bounded field restriction is imposed. Suppose for contradiction that eight original nonempty disjoint cosets g_iH_i have all pairwise index gcds≤7. Put I_i=[G:H_i]. Every H_i is proper, since a full-group coset would meet all the others. All following order/index constraints concern those ACTUAL H_i, not a converse realization of arithmetic data.

The only named research-sized finite input is **NC7**: six pairwise-disjoint left cosets of index7 subgroups in ANY group have their WHOLE complement equal to ONE index7 subgroup coset. It is used ONLY in the finite base q7, §10. Its complete current written proof is predecessor `sun8-global-kernel-section-complete-v1-part2.md`,181LF SHA `2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8`, at classical A7 simplicity/Eisenstein, parent-supported within the exact45LF current disposition SHA `4d23122673282636bd4c008bae7b1cc1c241090238e1c721b47592af46f88232`. This is NOT the inherited global Sun7 statement. All NEW field/root/Sylow/normalizer/finite-case/volume/completion arguments are reconstructed below.

There is NO Jordan/Bertrand, minimal-index table, Dickson classification, CFSG subgroup catalogue, Guest/HSC theorem, old global F7/Sun5/MS ancestry, normal-section or pending125/99/63 candidate as a correctness premise. Those source searches were route controls; their unread ancestry/programs receive no credit. Part3's M1 class<=2/abelian-exp4 history is unchanged and not used.

## 2. Ordinary root/action setup and generation, fully written

Work in SL2(F_q) modulo its scalar center Z={lambda I:lambda²=1}, of order d=gcd(2,q−1). Counting a nonzero first column and q second columns with determinant1 gives

|G|=q(q²−1)/d.

Write u(t)=[[1,t],[0,1]], l(t)=[[1,0],[t,1]], and use their images in G. On the ACTUAL projective line Omega=F_q∪{infinity}, U={u(t):t∈F_q} acts by translations, fixes infinity and is regular on F_q. Its order is q, the full p-part of |G|, so it is a Sylow p-subgroup. B=G_infinity has order q(q−1)/d and affine form x↦s x+b with multipliers s in the square subgroup of F_q^*, of order(q−1)/d. U is its UNIQUE Sylow p-subgroup, normal and abelian. Its conjugate U_0 is the lower root group fixing0. Every nonidentity element of either root group has precisely its one fixed projective point.

Upper and lower root groups generate G, WITHOUT a subgroup classification. For a≠0,

w(a)=u(a)l(−a^−1)u(a)=[[0,a],[−a^−1,0]],
w(a)w(−1)=diag(a,a^−1).

These are exact matrix products. For a determinant1 matrix [[a,b],[c,e]] with a≠0, left multiplication by l(−c/a) makes it [[a,b],[0,a^−1]], which is diag(a,a^−1)u(b/a). If a0, left multiplication by w(1) makes the first entry nonzero. This is ordinary two-row Gaussian elimination in the actual FIELD, not a CAS identity or an assumption about arbitrary composite rings.

The action is faithful (its scalar kernel has already been divided out), transitive and two-transitive because U is transitive on the other q points. Thus it is primitive.

For the finite bases we also need simplicity for q>3; here is its COMPLETE standard root argument. Choose a∈F_q^* with a²≠1, possible since q−1>2. The diagonal commutator

[diag(a,a^−1),u(t/(a²−1))]=u(t)

puts all U in G'. Its conjugates generate G, so G'=G. If1<K<G is normal, primitivity and faithfulness make K transitive. Hence G=KB. In G/K the images of ALL conjugates of U coincide with the image of U: write g=kb and use U normal B. These images generate the quotient and are abelian. But a quotient of perfect G is perfect, so an abelian quotient is trivial, contradiction. Thus G is simple for q>3. No exceptional PSL2(9)≅A6 or PSL2(4/5)≅A5 is imported; the needed action identifications below are derived when an actual low-index subgroup appears.

## 3. Actual root containment: every p-free proper index is a multiple of q+1

If H is proper and p∤[G:H], H contains a full Sylow p-subgroup; conjugate it to U for this SUBGROUP PROPERTY only, not to independently alter the original coset family. If H contained g outside B, write g(infinity)=z∈F_q and h=u(−z)g∈H, so h(infinity)=0. Then hUh^−1 is a Sylow p-subgroup fixing0; it is contained in B_0 and equals its UNIQUE normal root group U_0. H would contain U and U_0 and therefore G, contradiction. Hence H≤B.

For the ORIGINAL H this says H is contained in SOME actual conjugate Borel. Therefore

p∤[G:H], H proper  ==>  q+1 divides [G:H].                  (ROOT)

All subgroup-specific conjugations have been removed from the conclusion; the SAME q+1 works for every actual original subgroup. More generally any H contained in a Borel has index a multiple of q+1. When q+1>7 at most ONE of the original eight counterexample sources can be Borel-contained, regardless of its p-valuation.

If p>7, at most ONE original I_i can be divisible by p. The other at least seven are proper p-free indices and all contain q+1>7 by(ROOT), contradicting their pairwise gcd≤7. This already proves L2-SUN8 for EVERY field of characteristic>7, independently of NC7 or any remaining finite case.

## 4. COMPLETE normalizer/field/Sylow-count constraints for a small p-drop

Let H NOT be contained in a Borel. By(ROOT), a=v_p([G:H])≥1. Suppose a<f, so a Sylow p-subgroup P of H has order u=p^(f−a)>1. Conjugate it inside U; then P=H∩U=u(A) for an additive F_p-subspace A⊂F_q of dimension f−a. This is its actual intersection, not a chosen root subgroup of a convenient size.

Because P is nontrivial, its common fixed set is exactly{infinity}. Thus N_H(P)≤B. Conversely H∩B normalizes H∩U=P because U normal B. Therefore

N_H(P)=H∩B,  |N_H(P)|=u*t,

where t is the order of its ACTUAL affine-multiplier image. It divides(q−1)/d and stabilizes A by scalar multiplication.

The scalar stabilizer K(A)={0}∪{s≠0:sA=A} is a SUBFIELD: products/inverses preserve A; if s+t≠0 then(s+t)A⊆A and injectivity on finite A makes equality. It contains F_p. If |K(A)|=p^e, then e|f and A is a vector space over K(A), so e|(f−a); hence e|gcd(f,a). Consequently

t | p^e−1 with e|gcd(f,a), and t | (q−1)/d.                 (TORUS)

No field/subgroup classification is invoked.

Two Sylow p-subgroups of H with the SAME fixed projective point would both equal H's intersection with the UNIQUE root group there; therefore they are the SAME. Sylow conjugacy identifies their number with the size of H's orbit of infinity. P acts semiregularly on finite points, in orbits of size u. Since H is not Borel-contained, that orbit consists of infinity plus k such orbits, for some1≤k≤p^a. Write s=p^a. Then

nu_p(H)=1+k*u,  1≤k≤s,
[G:H]=s(q²−1)/(d*t*(1+k*u)).                               (COUNT)

Here nu denotes the NUMBER of Sylow subgroups, not a p-adic valuation. Because1+ku is prime to p and the index is an integer,1+ku divides q²−1. As q=s*u and ku≡−1 modulo1+ku, multiplying by k² gives

1+k*u divides s²−k².                                      (DIV)

These are NECESSARY constraints on every actual H, not a claim that every surviving parameter tuple is realizable. If u≥s², all k<s fail because0<s²−k²<1+ku. Hence k=s, nu_p(H)=q+1, and

[G:H]=s(q−1)/(d*t).                                       (FULL)

All index tables and infinite cases below follow only from(TORUS)/(COUNT)/(DIV)/(FULL), with integer divisibility and exact group orders.

## 5. ALL remaining large fields, no prime-to-small-number hypothesis

Let b be the largest integer with p^b≤7. A counterexample has at most ONE index divisible by p^(b+1). Every original proper H is either Borel-contained, has that high p-valuation, or is a NON-BOREL regular source with1≤a≤b. These are actual covering types; overlapping high/Borel cases only improve the upper bound.

For p=3,5,7 we have b1. When f≥3, u=p^(f−1)≥p²=s², so(FULL) holds. From(TORUS), t|p−1. Put

D=(q−1)/gcd(q−1,2(p−1)).

Since dt=2t divides both q−1 and2(p−1), EVERY non-Borel regular index is a multiple of the SAME pD. Moreover

pD≥p(q−1)/(2(p−1))≥p(p²+p+1)/2≥39/2>7.

Thus at most ONE such source occurs. The Borel bucket has at most ONE because q+1>7, and the high p² bucket has at most ONE because p²>7. At most three original sources are possible under gcd≤7, not eight. This covers EVERY f≥3 in these three characteristics.

For p2, b2. If f≥6, then for BOTH a1 and a2, u≥s². In a1(TORUS) gives t1; in a2 it gives t1 or3. Every non-Borel regular index is a multiple of

D=(q−1)/gcd(q−1,3)≥(q−1)/3≥21>7.

Again at most one regular source, at most one Borel source(q+1>7), and at most one high8 source. Thus L2-SUN8 holds for ALL q=2^f with f≥6.

## 6. COMPLETE characteristic-two finite remainder: q8,16,32

The following are ALL necessary non-Borel regular indices from(COUNT)/(DIV). Borel indices share q+1>7, and high p³=8 indices share8>7, so those two buckets each contain at most ONE original source. Each displayed candidate index is>7 and therefore can occur at most once in a gcd≤7 counterexample.

|q|a,u|ALL surviving k|ALL t|ALL possible indices|
|---|---|---|---|---|
|8|1,4|2|1|14|
|8|2,2|1,3,4|1|84,36,28|
|16|1,8|2|1|30|
|16|2,4|1,4|1,3|204,68;60,20|
|32|1,16|2|1|62|
|32|2,8|4|1|124|

For a1 the only omitted k1 would require u+1 dividing3, impossible. At q8,a2 the omitted k2 requires5|12. At q16,a2 omitted k2/k3 require9|12 or13|7. At q32,a2 omitted k1/k2/k3 require9|15,17|12,25|7. All fail by written integer division. The t values follow from e|gcd(f,a): only f4,a2 permits e2 and t3; odd f forces e1,t1. Substituting |G|504,4080,32736 in(COUNT) gives the table exactly.

There are only FOUR,FIVE,TWO distinct candidate regular indices respectively, so even adding the two exceptional buckets permits at most6,7,4 original sources. Each is strictly below eight. No subgroup list, executable enumeration, field calculator or realizability assumption was used.

## 7. COMPLETE q25 and q49 finite remainders

Here a1,u=p and t|p−1. The high p² bucket and Borel(q+1) bucket each contain at most ONE source.

|q|k and nu_p(H)|ALL t with integer index|ALL possible regular indices|shared divisor|
|---|---|---|---|---|
|25|1,6|1,2,4|260,130,65|65|
|25|5,26|1,2,4|60,30,15|15|
|49|1,8|1,2,3,6|1050,525,350,175|175|
|49|2,15|1,2|560,280|280|
|49|7,50|1,2,3,6|168,84,56,28|28|

At q25, k2/k4 require11|21 or21|9, impossible; k3 passes16|16 but its index is195/(2t), nonintegral for t1,2,4. At q49, k3/4/5/6 require22|40,29|33,36|24,43|13, all false. At k2 integrality removes t3/6 from560/t. All remaining values are the literal substitutions of |G|7800/58800 into(COUNT), not asserted subgroup realizations.

Within each row all indices share its displayed divisor>7, so at most ONE original source belongs to that row. q25 has at most2 regular +2 exceptional sources; q49 at most3+2. Neither permits eight. This covers all f2 odd-characteristic fields except q9, addressed fully next.

## 8. COMPLETE q9, including every actual low-index overlap

Here |G|360, p3,f2,d2,u3,a1,t1/2. (DIV) leaves k1 or3 (k2 requires7|5). Their necessary non-Borel regular indices are

{30,15} from k1, and {12,6} from k3.

Borel indices share10>7; high3² indices share9>7. Thus at least SIX sources in a hypothetical eight-family would be non-Borel regular. The non6 candidates12,15,30 have at most TWO representatives: duplicates exceed7 and15/30 cannot coexist. Therefore an index6 source exists (indeed at least four).

By §2 G is simple and perfect. An index6 action is faithful, has image in A6 by perfectness, and |G|360=|A6|. Hence this ACTUAL coset action identifies G with A6; no exceptional isomorphism is assumed.

There is NO subgroup of order30 in A6, as follows. Its Sylow5 count is1 or6. In the first case it lies in N_A6(C5), of order10: the S6 normalizer has order20 and has an odd order4 multiplier, so its alternating half is10. In the second case24 nonidentity order5 elements already occur. Its Sylow3 count is1 or10; ten groups would supply20 further nonidentity elements, exceeding29. Hence its C3 is normal and it lies in a C3 normalizer. Both order3 types in A6 have normalizer order18. For a single3-cycle the S6 normalizer is S3×S3 of order36 with odd elements; for a double3-cycle the centralizer is C3 wreath C2 of order18, the inversion gives normalizer36, and the odd swap of its two cycles halves it to18 in A6. Neither normalizer can contain order30. This exhausts the Sylow alternatives.

Consequently index12 is absent. At most ONE non6 regular source remains(15 and30 have gcd15), so at least FIVE original cosets have index6. Six such cosets would already fill the whole group and leave no room for two more nonempty cosets, so exactly five occur.

**Actual five-coset completion in this same A6 action:** fix the faithful degree6 action of one index6 subgroup. Any other index6 subgroup K has order60. If it were transitive in that action, the product with the point stabilizer would be G and ANY such cosets would meet, contradicting the original disjointness. A nontransitive order60 subgroup of A6 must fix a point: without a fixed point the possible orbit stabilizers have orders at most24(4+2),18(3+3), or4(2+2+2). Thus it equals a natural point stabilizer in this SAME action. All five cosets are constraints g(x)=y in the same two-transitive action. Pairwise disjoint constraints form one rook row/column; their WHOLE complement is the missing sixth index6 subgroup coset. No independent outer action is glued into it.

The remaining three ACTUAL original cosets lie inside this complement. At least one is non6 regular, and at least one is Borel: the other covering buckets each have capacity1. Containment in an index6 coset forces all their indices divisible6. Thus the non6 regular index is30, not15. The Borel index is divisible10 and6, hence30 too. Those two original indices have gcd≥30>7, contradiction. This closes q9 without an unproved subgroup catalogue, a missing field case or a separate local-partition choice.

## 9. COMPLETE q4/q5 finite base, order60, plus q2/q3

For q4/q5, §2 gives a simple group of order60. An index2/3/4 subgroup would give an injective action in S4 of smaller order, impossible. Therefore all proper indices lie in the NECESSARY divisor list

{5,6,10,12,15,20,30,60}.

Only necessary indices are used; no converse existence is asserted. The elementary coprime-index coset fact is: intersection index is a multiple of the coprime product and at most that product, so HK=G and EVERY two such left cosets meet.

If index5 occurs, neither6 nor12 can occur by coprimality. Among the remaining high candidates10,15,20,30,60 the only compatible pairs(gcd≤7) are10/15 and15/20; at most two high cosets occur, since duplicates have gcd>7. At most five index5 cosets fit by volume. Thus at most seven sources, not eight.

If index6 occurs and5 does not, high candidates are10,12,15,20,30,60. Their ONLY compatible triples are{10,12,15} and{12,15,20}; all other compatible sets have size at most two. This follows directly from pair gcds:30 connects only12,60 connects none, and the remaining four form those two triangles. To reach eight would require five index6 cosets and three high cosets; six index6 cosets already exhaust G. But every allowed high triple has reciprocal mass at least1/12+1/15+1/20=1/5>1/6, exceeding the mass left by five index6 cosets. Disjoint cosets require total reciprocal mass≤1, not a complete-partition assumption. Contradiction. With neither5 nor6 the high list has at most three sources. Thus q4/q5 are fully closed by written index-divisor/volume facts.

For q2, |G|6, so eight disjoint nonempty cosets cannot exist. For q3, |G|12. Under pairwise gcd≤7 at most one coset has index12, and every other index is≤6. Seven such cosets would already have reciprocal mass≥7/6>1. This closes both nonsimple small fields without importing their isomorphism labels.

## 10. COMPLETE q7 and the exact NC7 use

Here |G|168 and its7-part is7. Every7-free proper index is a multiple of8 by(ROOT), so at most ONE such original source occurs. At least seven of the eight hypothetical sources therefore have index7r, r|24. Among these r are pairwise coprime because their original index gcds are≤7. At most two r can exceed1, since24 has only prime factors2/3. Thus at least FIVE original cosets have index7.

An index7 coset cannot be disjoint from any7-free-index coset, by the coprime-index lemma. Hence in fact NO7-free source occurs. All eight indices are7r, r|24, and at least SIX are exactly7. NC7 says their WHOLE complement is ONE index7 subgroup coset. It contains the two remaining entire original cosets. After one translation into that subgroup their indices are the ORIGINAL coprime r values, so those cosets must intersect. Contradiction.

This is the sole NC7 dependency. It does not assume a partition of the original eight cosets, multiply incompatible local sections, or invoke global Sun7. The common complement is supplied by the exact separately written/parent-supported NC7 theorem, not guessed from density.

## 11. Exhaustiveness, contribution and exact remaining original scope

The cases exhaust EVERY prime power: characteristic>7 all f by §3; p3/5/7 with f≥3 by §5 and f2 q9/25/49 by §§7–8; p2 f≥6 by §5 and f3/4/5 q8/16/32 by §6; f1 q2/3/5/7 and q4 by §§9–10. All finite identities/divisions/table remainders are displayed WRITTEN integer calculations, not kernel/program checks. The normalizer multiplier/subfield and all Sylow parameters were derived on the ACTUAL original subgroups and are only necessary constraints, so no unproved realizability converse enters.

Thus L2-SUN8 is a NEW WRITTEN CANDIDATE for the ENTIRE original target in ALL G=PSL2(q), at NC7/current classical boundary. It is independent of the global Sun7/R8 route and also gives P7-freeness in this whole family as a weaker consequence. Original coset representatives are never independently normalized or replaced: conjugating a subgroup to analyze its index proves a conjugacy-invariant property for the original source, and final density/common-action arguments use the actual disjoint cosets together.

This may be known/routine; bounded public source searches do NOT establish priority, novelty or SOTA. No first/publication/major-discovery claim or independent discovery count is made. Fresh whole-proof reconstruction and explicit parent disposition are REQUIRED; no old/narrow/v99 return covers this mathematics. Written is not formal/kernel, human, configured-family, executable or worldwide-novelty acceptance. The source access/read limits and permanent OWN cadence finding above remain part of every trust statement; no historical computation/program is promoted.

The FULL arbitrary-group Sun8 problem remains OPEN here: other finite simple families/high rank, alternating/symmetric cases outside separately proved candidate families, arbitrary infinite groups and the general actual mixed-alpha<=1/maximal/nonabelian/private-composite source-lift barrier are not eliminated. No eight-coset witness, group-size/index cutoff substitute or full-book closure is supplied. Same original18owners/fulltarget/root/cutoff/deadline, immutable previous125/99/63/136/217/58/M1 findings and v9/v10/v11/HOLD. No scientific execution or newGO; primary continues at that exact unrestricted residual.
