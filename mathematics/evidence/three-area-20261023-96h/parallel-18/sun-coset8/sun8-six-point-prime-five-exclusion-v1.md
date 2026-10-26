# Sun8: catalogue-free six-point prime-five exclusion; binary core-normalizer expansion is a two-power — v1

Owner MathSun8 / math-6. Actual clock: `Sun Oct 25 13:55:38 PDT 2026`.
Status: **NEW WRITTEN CANDIDATE**, a complete finite-group argument at the explicitly named binary-kernel union below. No computed subgroup catalogue, CFSG, scientific interpreter, enumeration, symbolic program or certificate replay. HOLD/v9/v10/v11 and no external CLI/nested agent/new GO remain binding.

## 1. Exact finite-group statement and its actual Sun8 boundary

The new group-theoretic statement is this. Suppose a finite group X has three-part EXACTLY three, has a subgroup A of order at least 24 normalizing an order-three subgroup P, and has a family of SIX faithful-in-combination TRANSITIVE six-point permutation actions. Assume A is transitive in EACH action. Then **five does not divide |X|**. It is essential that P is nontrivial in each action; here that follows automatically because the image's three-part and X's three-part are both three. The proof is §§2–7.

For the literal binary Sun8 application put R=M/B and C=intersection of the six regular cores, exactly as in `sun8-binary-core-kernel-small-residuals-v1.md` (107 LF, SHA256 `379ebd7deec4ee5f55d102c4409cf265dc60d93ad9f6ce839e8e1c57e7c01164`). At its UNREVIEWED candidate boundary, C is a two-group of order 1,4 or16, C∩N0=1, |R| has three-part three, and X=R/C acts faithfully in combination on the six coset spaces of K_j/C, each of size six. R=N0 K_j makes N0 transitive in each. A is its embedded N0, of order24 or48. The selected P is S=C3, or the characteristic order-three subgroup of S=S3. N0 normalizes P. Thus every hypothesis of the finite-group statement is an ACTUAL property at that literal candidate union, not an arbitrary cell arrangement.

Its upstream candidate imports are NC7 and UNIFORM-SIX, named in that 107-LF source; this successor does not claim that any of them or their complete joint applicability has been accepted. The present finite-group proof does not use scientific execution or an unprovided classification of degree-six groups.

## 2. Any transitive six-point image containing five is two-transitive

Let F<=S6 be transitive, with three-part exactly three, and suppose 5 divides |F|. A five-element is a five-cycle on six letters. It fixes one point, and its cyclic subgroup is transitive on the OTHER five points. That point stabilizer is therefore transitive on the other five; conjugating by F shows F is TWO-TRANSITIVE and hence primitive.

Since |F| divides 6! and is divisible by30 but not by nine, the ONLY possible orders are 30,60,120,240. We now reconstruct all four, rather than cite a catalogue. We use standard Sylow/Cauchy, orbit-stabilizer and the elementary groups of orders four and six. A nontrivial normal subgroup of a faithful primitive group is transitive; this follows because its orbits form an invariant block partition.

Order30 is impossible. The number of Sylow-five subgroups is one or six. The first would make a normal order-five subgroup transitive on six points, impossible. Likewise the number of Sylow-three subgroups divides10 and is 1 mod3, so is one or ten; normality of an order-three subgroup is impossible for the same reason. Thus there would be 24 nonidentity five-elements and20 nonidentity three-elements, plus1, already more than30.

Order240 is impossible for a different elementary reason. The stabilizer of the point fixed by a five-cycle has order40 and is a subgroup of S5 on the remaining five letters. Its Sylow-five count divides8 and is 1 mod5, hence is one. It lies in the normalizer of a regular C5 in S5, whose order is 5 times4=20, a contradiction. The normalizer order follows by specifying a translation and an automorphism of C5.

## 3. Order60: simplicity reconstructed without a classification import

Suppose |F|=60. Any nontrivial proper normal subgroup is transitive on six points, so its order must be 6,12 or30. A transitive subgroup of order30 is already impossible by §2, since containing a five-cycle makes it two-transitive too.

A transitive normal subgroup T of order six would act REGULARLY. A regular group's permutation normalizer has order |T| times |Aut(T)|: a normalizing permutation is specified by the image of the identity and the induced automorphism. The groups of order six are C6 or S3, with automorphism groups of orders two or six, respectively. Their regular normalizers have order at most36, too small to contain F of order60.

For a normal transitive T of order12, first prove that Aut(T) has no element of order five. Such an automorphism would permute the one or three Sylow-two subgroups trivially. It would restrict trivially on each subgroup of order four, whose automorphism group has order two (C4) or six (C2^2). It therefore fixes at least four elements. Its fixed elements form a subgroup of T; its order divides12 and is congruent to12 modulo five, since the other automorphism orbits have size five. The only possibilities are two or twelve, so at least four forces twelve and the automorphism is trivial.

An element of order five in F normalizing T must consequently centralize T. But the centralizer in S6 of ANY transitive subgroup acts semiregularly: an element commuting with it and fixing one point fixes all points. Its order therefore divides six, so it contains no five-element. This contradiction excludes normal T of order12.

All proper nontrivial normal orders are exhausted. Therefore F is SIMPLE. It is nonabelian because its order is composite. In particular its six-letter sign is trivial, so F<=A6.

## 4. Order60 is A5, with its unique degree-six action

The Sylow-five count is six. The Sylow-three count divides20 and is 1 mod3, hence is one, four or ten. One contradicts simplicity; four would give a faithful homomorphism of the simple F into S4, impossible for order60. Thus the count is ten. The 24 nonidentity five-elements and20 three-elements leave only fifteen other nonidentity elements.

A Sylow-two subgroup cannot be cyclic of order four. Its order-four generator in the LEFT regular action of F would have fifteen four-cycles and hence odd sign, giving a nontrivial homomorphism from the simple F to C2. Thus every Sylow-two subgroup is C2^2.

An involution in F<=A6 is a double transposition. Its centralizer in S6 has order16: centralize two transposed pairs and permute the two fixed letters. The centralizer has equally many even and odd elements (multiplication by the transposition of the fixed letters reverses sign), so its centralizer in A6 has order8. Its centralizer in F therefore has order dividing gcd(60,8)=4, and contains the Sylow-two C2^2 containing it. It has order exactly four. Thus every involution class in F has size fifteen. There are at most fifteen remaining nonidentity elements, so there are exactly fifteen involutions.

Each involution is in a UNIQUE Sylow-two subgroup: any such C2^2 lies in its centralizer of order four. Hence there are exactly FIVE Sylow-two subgroups. The conjugation action on them is nontrivial and faithful by simplicity, embedding F into S5 with order60 and index two. The unique index-two subgroup is A5: all transpositions are conjugate and generate S5, so a nontrivial C2 quotient has exactly the sign kernel. Thus F is A5. This simultaneously establishes the needed simplicity of this abstract A5 in the case under consideration.

Any point stabilizer of its six-point action has order ten. Its Sylow-five subgroup is unique, so the stabilizer equals its normalizer in A5, a dihedral D10. All six such normalizers are conjugate. Thus the degree-six action is exactly the action on the SIX Sylow-five normalizers. No alternative degree-six embedding is omitted.

## 5. Order120 is S5, again without a catalogue

Suppose |F|=120. Its point stabilizer has order20 and lies in S5 on the other five letters. A Sylow-five subgroup there is normal (its count divides four and is 1 mod5), so the stabilizer is the full affine normalizer C5 semidirect C4. It includes an odd four-cycle on those five letters. Therefore the sign on F is onto C2 and its kernel F0 has order60. It is a nontrivial normal subgroup of the primitive F, hence transitive; §§3–4 identify it as a simple A5 in its six-point action.

The centralizer in S6 of this TWO-TRANSITIVE F0 is trivial. Indeed if a commuting permutation takes p to q other than p, the point stabilizer of p would fix q, contrary to its transitivity on the other five points; a commuting permutation fixing p fixes all points. Thus conjugation embeds F into Aut(A5).

For completeness, Aut(A5)=S5 is also reconstructed. An automorphism permutes the FIVE Sylow-two subgroups C2^2. If it fixes all five, its permutation intertwines the faithful inner action of A5 on those five subgroups: for every g, the actions of g and of its automorphic image on them coincide, so the image equals g. Thus Aut(A5) injects into S5. Conversely conjugation by the natural S5 normalizing A5 injects into Aut(A5), since the centralizer of the two-transitive A5 on five letters is trivial. Hence Aut(A5) has order120 and equals S5. Consequently F is S5.

Any index-six subgroup of S5 has order20 and unique Sylow-five subgroup, and so equals that subgroup's normalizer C5 semidirect C4. All are conjugate. Its faithful degree-six action is therefore unique up to relabeling as well.

We have proved the ENTIRE required classification:

> A transitive F<=S6 with three-part three and containing five is A5 or S5, in the respective specified degree-six action. Orders30 and240 are excluded, not dropped.

## 6. The A5 image cannot have the required normalizer transitivity

In A5, the normalizer D=N_{A5}(P3) of an order-three subgroup has order six and is S3. In the natural five-letter model, P3 is a three-cycle; its normalizer in S5 is S3 times S2 of order12, and the even half is that S3. It has three involutions.

Each of the six D10 point stabilizers has five involutions. The fifteen involutions of A5 form one conjugacy class, so each belongs to exactly TWO of the six D10's, by the total incidence count six times five. A D10 contains at most ONE of the three involutions of D: two distinct involutions of an S3 have a product of order three, impossible in D10. The three D-involutions contribute six incidences across the six D10's, so EACH D10 contains exactly one. Thus D meets every degree-six point stabilizer in order two and has two orbits of size three, not one orbit of size six.

In an image of X, the selected P remains nontrivial: the coset image is transitive of degree six, so its three-part is three and the kernel of that map from X is three-free. The image of A normalizes this P and is required to be transitive on six points. The preceding normalizer calculation makes an A5 image IMPOSSIBLE.

## 7. A single S5 image would force all six images to be the same S5

Let F_j be the six images of X. They are transitive of degree six, their three-parts are three, and the combined map is faithful. Suppose one image is S5. Pair it with any F_j; their paired image H is subdirect in S5 times F_j.

Here is the exact Goursat order calculation. The kernels of the two projections give normal subgroups whose quotients identify a common quotient T; equivalently, if N_1={x:(x,1) in H} and N_2={y:(1,y) in H}, then S5/N_1 is isomorphic to F_j/N_2=T and |H|=|S5||F_j|/|T|. Both numerator groups have three-part three, whereas H is an image of X and has three-part at most three. Hence T must have three-part THREE.

The ONLY normal subgroups of S5 are 1,A5,S5. To check rather than merely import this: intersection with the simple A5 is either 1 or A5. In the latter case the subgroup is A5 or S5. In the former, its commutators with A5 lie in the intersection and it centralizes A5; the centralizer is trivial by two-transitivity. Thus the quotient list is S5,C2,1. Only S5 has a factor three, so T=S5.

It follows that F_j surjects onto S5. Its order divides 6! with three-part three, so the only possible multiples of120 are120 or240. The latter was excluded in §2, and the former is S5 by §5. Both pair kernels are therefore trivial: the paired image is the GRAPH of an isomorphism between two S5's.

This holds for every j. Faithfulness of the combined six actions now makes the first S5 projection itself injective: an element trivial in it is trivial in all the paired graphs and hence in all six actions. Consequently X is S5.

But A embeds in X and normalizes its P3. In S5 the normalizer of an order-three subgroup has order12, preserving its support of three letters and its complement of two. It cannot contain A of order at least24. This contradiction excludes the S5 case and completes the promised theorem: five does NOT divide |X|.

## 8. Actual binary transport consequence and exact remaining gap

Apply the proved finite-group statement to X=R/C at the literal binary candidate boundary in §1. Its possible six-point images have no prime larger than five by Lagrange. The prime five has now been excluded, so X has only primes two and three. Since C is a two-group, R=M/B has only primes two and three as well. Since |R|=|N0|h with h three-free,

> **BINARY CORE-NORMALIZER EXPANSION: h=[N_G(B):N_G(U)] is a POWER OF TWO.**

Every ODD prime factor of the selected s, with its FULL multiplicity, is retained in t=[G:N_G(B)]/7. In particular if s is odd, then M=N. This is an actual full-source normalizer statement, not deletion of an odd private factor from the original coset family. The odd rank-two branch has its separate h=1,3 or9 theorem; it is not imported into this proof.

The genuine full-source normalizer indices [U_j:N_{U_j}(B)]=6t for all six regular neighbours and the original seven cosets are unchanged. The whole/fractional branches have C=1; the ordinary aligned residuals retain C2^2 or C2^4, and the newly visible missing-class A2 corner remains unexcluded. Even X being a {2,3}-group does NOT show that M is a collision-free enlargement or authenticate the global Sun7 reduction.

**First unproved step:** classify/exclude the actual remaining two-power kernel-normalizer sections together with the exceptional collision and FULL original U_j outside-M motion, or find a genuine source-preserving enlargement. No actual eight-coset witness, unrestricted Sun8 solution, finite computational certificate, formal/kernel proof, configured-family acceptance, independent-parent acceptance, numerical-bound promotion, novelty clearance or round completion is claimed. This successor is additive and no frozen predecessor is altered.
