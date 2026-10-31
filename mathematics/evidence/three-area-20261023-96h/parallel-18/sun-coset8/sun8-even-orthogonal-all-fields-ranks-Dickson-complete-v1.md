# Sun8 direct P7 — BOTH even-dimensional orthogonal types over ALL even fields, including q=2

Owner MathSun8-2. Actual pre-write observation: `Mon Oct 26 10:29:20 PDT 2026`.
**NEW WRITTEN CANDIDATE; unreviewed/unadopted.** All matrix, parity, orbit, field and index proofs are written exact algebra, not interpreter/calculator/program/enumeration/solver/replay evidence. This is a NEW successor source, not an edit of any pinned odd-orthogonal or unitary source.

## 1. Exact model, scope and required application input

Let q=2^f, n=2m>=6. Consider either the explicit split quadratic space `V^+=H^m`, or `V^-=H^(m-1) perpendicular A`, where H has form xy and A is the anisotropic norm plane from K=F_(q^2) to F_q. Use the polar form `B(x,y)=Q(x+y)-Q(x)-Q(y)`, which is nondegenerate. Let G be the ACTUAL projective image of `[O(V),O(V)]`, and **assume G is NONABELIAN SIMPLE**. This is an explicit hypothesis on the group/model, not a new classification or simplicity theorem for every orthogonal group. In characteristic two a scalar isometry has scalar square one and hence is the identity, so the projective map has trivial kernel here.

**Theorem E.** G has NO eight-subgroup index pattern `[G:U_l]=7r_l` with positive pairwise-coprime private r_l. Therefore it supports no direct P7 family. Both types, ALL q including2, ALL n>=6, all original labels/private powers and the possible private-seven owner are included. No odd-dimensional quadratic group, n<6, outer/central extension or unrelated simple model is silently claimed.

No small-representation bound is needed for this characteristic-two family. ALL parity, order, root-membership, Sylow, flag, left-descent and subgroup-index facts required below are reconstructed in this body. The arbitrary-original-group application additionally uses the full already ordinary-written-supported 88-LF normal-section source SHA256 `b401c139141c451755174f8151942b86916e5677f734715ede48299394716202`: direct P7 anywhere gives an ACTUAL finite NONABELIAN SIMPLE factor of an all-eight finite-core quotient, with eight own-label private divisors. The complete 76-LF parent SHA256 `9dbce6f9b7afab2fc0c9e35dbb0034ff47f45c0cb3d8e40ab4c3f739c34ff726` supplies that exact ordinary-written cut. No Dickson theorem, Arf classification, orthogonal-order/subgroup table, Borel–Tits theorem, CFSG, character table, Jordan, McLaughlin or Parker result is imported.

## 2. Complete parity-cocycle proof, not a named Dickson-invariant assumption

In a hyperbolic quadratic space of dimension 2N, let L,M be maximal totally singular N-spaces. Put `d(L,M)=N-dim(L intersect M) mod2`. We prove the cocycle identity for ANY three such spaces.

First suppose L,M are adjacent, with C=L intersect M of dimension N-1. For another maximal singular P write `k=dim(P intersect C)`. Nondegeneracy and P=P^perp give

`dim(P intersect C^perp)=N-((N-1)-k)=k+1`.

Its image in `C^perp/C` is an isotropic line, since its kernel is P intersect C of dimension k. That quotient is a hyperbolic plane and has EXACTLY TWO isotropic lines, L/C and M/C. Thus `dim(P intersect L)` and `dim(P intersect M)` are k and k+1 in one order. Adjacency flips the parity of d(P,-).

The adjacency graph is connected with the needed length. If L intersect M has dimension r<N, choose v in M outside L. Then `C'=L intersect v^perp` is a hyperplane of L because L=L^perp and v is outside it. The space `L'=C'+<v>` is maximal singular, adjacent to L, and its intersection with M has dimension EXACTLY r+1. Repeating yields a path from L to M of length N-r. Each step flips parity relative to ANY P, proving

`d(P,M)=d(P,L)+d(L,M) mod2`.

Now take the hyperbolic space `V perpendicular V` with form Q+Q. Its diagonal Delta and the graph `Gamma_g={(x,gx)}` of any g in O(V) are maximal singular spaces of dimension dim(V). Their intersection is the fixed space of g, so

`delta(g):=d(Delta,Gamma_g)=rank(g-I) mod2`.

The isometry `1+g` on the TWO summands (meaning block-diagonal identity,g, not their sum as operators) sends Delta to Gamma_g and Gamma_h to Gamma_(gh). The cocycle therefore gives `delta(gh)=delta(g)+delta(h)`. This proves the homomorphism for ALL isometries, not merely for displayed generators.

It is onto C2. For v with Q(v)!=0 the symmetry

`s_v(x)=x+B(x,v)/Q(v)*v`

preserves Q, since its two added contributions cancel in characteristic two, and s_v-I has rank one. Such a v exists, for example e+f in H. Hence delta(s_v)=1. In particular

`[O(V),O(V)] <= ker(delta)`, `[O(V):ker(delta)]=2`.

No determinant argument in characteristic two is substituted for this proof.

## 3. Complete quadratic counts and order, including the binary anisotropic base

A nondegenerate even-dimensional quadratic space in characteristic two admits a symplectic-pair decomposition of its polar form into nondegenerate binary planes. A binary plane is either isotropic, hence hyperbolic by choosing an isotropic e and replacing a partner g by `g+Q(g)e`, or anisotropic. An anisotropic binary form is a scalar norm from the quadratic extension: after choosing a vector of nonzero norm, its binary polynomial has no root and defines that extension. The norm map is onto F_q^*: its kernel has at most q+1 roots and its image lies in a group of size q-1, forcing image size q-1. Scalar norm forms are thus isometric. Two anisotropic planes represent the same nonzero value, and the sum of representing vectors is isotropic. This proves that the residual anisotropic dimension is at most two, without an Arf theorem.

For a hyperbolic pair plus W, the equation `xy=-Q_W(z)` has 2q-1 solutions when Q_W(z)=0 and q-1 otherwise. Therefore, counting zero vectors including zero,

`Z_n=(q-1)q^(n-2)+qZ_(n-2)`.

With Z_0=1, Z_(2,-)=1 and Z_(2,+)=2q-1, induction gives the NONZERO singular-vector counts

`z_(2m,+)=(q^(m-1)+1)(q^m-1)`,

`z_(2m,-)=(q^(m-1)-1)(q^m+1)`.

These different zero counts distinguish the two residual types. Thus the complement of ANY extracted hyperbolic pair has the same remaining sign as the given model: invert the recurrence and use the norm-plane identification. No unspecified isometry classification is needed.

For a fixed singular e!=0 the singular f with B(e,f)=1 are exactly `f_0+w+Q(w)e`, w in the complement, giving q^(n-2) choices. The complement identifications just proved allow matching Witt bases, so O(V) is transitive on ordered hyperbolic pairs with stabilizer O_(n-2). The split binary order is 2(q-1).

For the anisotropic binary base, use its norm plane. Any isometry sends1 to a norm-one element; remove that multiplication and assume it fixes1. Choose theta with trace one. Its image has the form theta+beta because it must preserve the polar pairing with1. Norm preservation gives `beta^2+beta=0`, so beta is0 or1. These are identity and field conjugation. Hence the anisotropic binary order is EXACTLY2(q+1). This is the characteristic-TWO argument; the odd-characteristic orthogonal-line-plus/minus argument is NOT being reused.

Counting ordered hyperbolic pairs now gives and proves by induction

`|O_(2m,eps)(q)|=2q^(m(m-1))(q^m-eps) product_(i=1)^(m-1)(q^(2i)-1)`.

Its two-part is `2q^(m(m-1))`; the two-part of ker(delta) is therefore `q^(m(m-1))`. This bound is valid before knowing an exact order for the commutator subgroup.

## 4. ALL positive root groups belong to the ACTUAL commutator subgroup, even at q=2

Use the ordered basis `e_1,...,e_r,A,f_r,...,f_1`, where r=m in split type and r=m-1 with the norm plane A otherwise. The positive matrix groups include

`x_(e_i-e_j)(a)=I+aE_(e_i,e_j)-aE_(f_j,f_i)`, i<j,

`x_(e_i+e_j)(a)=I+aE_(e_i,f_j)-aE_(e_j,f_i)`, i<j,

and, in nonsplit type, the ACTUAL additive groups

`R_i(a):(x_i,z,y_i)->(x_i-B_A(a,z)-Q_A(a)y_i,z+a*y_i,y_i)`, a in A.

All preserve Q and have determinant one; the signs are retained symbolically though minus equals plus in this characteristic. Direct substitution gives `R_i(a)R_i(b)=R_i(a+b)`.

If q>2 choose t in F_q^* with t!=1. A hyperbolic diagonal D_i(t) scales each indicated root parameter by t, so the commutator `[D_i(t),x(a/(t-1))]` gives the entire corresponding root group. Likewise it gives every R_i(a). Thus these groups are in O'.

At q=2 this scalar argument is NOT used. In SPLIT type r=m>=3, multiplication of matrix units gives

`[x_(e_1-e_2)(1),x_(e_2-e_3)(a)]=x_(e_1-e_3)(a)`.

For a=1 this is the full nontrivial root group over F2. The commutator subgroup is normal in O(V); coordinate pair permutations and single pair flips in O(V) conjugate this onto every positive and negative e_i+-e_j group. Thus every needed root group is in O' also at q=2.

In NONSPLIT type q=2, identify A with F4 and its norm. The norm-one scalars have order3, so choose tau!=1 among them. Its anisotropic-plane isometry acts on R_i(a) by a->tau*a. Since tau-1 is invertible in F4,

`R_i(a)=[tau,R_i(a/(tau-1))]`.

Every full short-root group of size4 lies in O'. For distinct i,j, direct multiplication of the displayed Eichler matrices gives

`[R_i(a),R_j(b)]=x_(e_i+e_j)(-B_A(a,b))`.

The cross terms add -B_A(a,b)y_j to x_i and +B_A(a,b)y_i to x_j; this long-root correction commutes with both R_i and R_j, proving the exact commutator formula. Nondegeneracy of the polar form on A gives a,b with B_A(a,b)=1. Since r=m-1>=2, this supplies the full long F2 group. O-conjugation supplies every remaining positive and negative long group. No rank-two q=2 case is dropped.

The positive groups generate the FULL positive unipotent U. Stripping the first/last hyperbolic pair leaves q^(n-2) free Eichler parameters and a middle positive group; its last corner is forced by Q, not an extra parameter. Uniqueness follows from its columns. Starting with no positive group on the anisotropic kernel or the split hyperbolic plane gives `|U|=q^(m(m-1))` in BOTH types. By the preceding membership proof,

`U<=O'<=ker(delta)`.

Its order equals the full two-part allowed by §3. Thus U is a FULL Sylow2-subgroup of G=O', not a smaller one-cut block or an asserted Sylow of the larger full O group.

## 5. Actual Weyl representatives, parity and full flag reduction

Adjacent pair representatives are `u(1)v(-1)u(1)` products of the corresponding positive/negative root matrices, giving the usual paired SL2 swaps. In split type the last simple root e_(m-1)+e_m gives a TWO-pair signed swap by the same product. All representatives belong to O' by §4.

In nonsplit type write the last four-space as `Q=xy-N(z)` over K=F_(q^2). The determinant of the Hermitian matrix `[[x,z],[bar(z),y]]` is this Q. The action `H->gH g*` of SL2(K) preserves it. Its upper and lower unipotents are exactly the full R_i(a) and their opposites; `u(t)v(-t^-1)u(t)` gives a representative flipping the last hyperbolic pair and conjugating/rescaling the norm plane. It is a product of the actual O' root groups already proved, including at q=2.

For a split maximal singular space L, its FULL stabilizer in O(V) has Levi `diag(A,A^(-T))` and upper unipotents with alternating top/right matrix S. The Levi has `rank(g-I)=2rank(A-I)`; an alternating matrix has even rank, by extracting nondegenerate two-by-two blocks successively. Thus both factors have delta0, and by §2 the whole stabilizer has delta0. A single hyperbolic-pair flip has rank(g-I)=1 and delta1, while a pair permutation has even rank and delta0. Therefore coordinate profiles of elements of O' in split type are EVEN signed permutations. This replaces, rather than misuses, the odd-field determinant test.

In nonsplit type conjugation of the norm plane has rank(conjugation-I)=1, since its fixed field is F_q. It has delta1. Combining it with one hyperbolic-pair flip gives delta0 and realizes the last signed reflection above. The Weyl coordinate groups are thus full signed permutations in nonsplit type and even signed permutations in split type. Monomial conjugation takes each FULL root group to its indicated positive or negative group, including the WHOLE q^2 norm-plane group. It normalizes the actual flag torus intersection T_G.

Here is the actual flag reduction. The last nonzero coordinate of a singular vector cannot lie only in A, since A is anisotropic. For an e_j pivot use the e_i-e_j matrices to clear earlier coordinates. For an f_j pivot clear other f_l by e_j-e_l, then e_i with i!=j by e_i+e_j, then its A component by R_j(a) with a equal to minus that component divided by the pivot. The remaining `alpha e_j+beta f_j` is singular only when alpha=0. The SAME actual U matrices act on the WHOLE flag. Passing to L^perp/L removes paired coordinates; induction reduces the remaining flag to a coordinate one, with its unique ordinary pivot/intersection profile.

For split type, §2's delta and the delta0 full maximal stabilizer force the even sign parity just established. In nonsplit type all signed profiles are represented by the actual root products. If B_G is the full flag stabilizer in G, removal of the U part gives `B_G=U T_G`; the negative-type anisotropic part in delta0 is its norm-one rotation torus, not its delta1 conjugation. Thus T_G is a genuine p-free torus intersection, and

`G=disjoint union_(w in W) B_G n_w B_G`, `G=<B_G,all simple n_i>`.

The reduction also shows G and ker(delta) have the SAME flag orbits. In nonsplit type the full O flag stabilizer contains the delta1 anisotropic conjugation, so O and ker(delta) have the same flag orbits too. In split type there are TWO maximal singular families; a delta1 pair flip interchanges them and conjugates O' to itself. G is transitive on each, and their indices are equal. No assertion that the two families form one G orbit is made.

## 6. Complete proper-Sylow-overgroup proof, with the fork and torus retained

Let H<=G contain U, and let I be the set of simple indices whose FULL negative group lies in H. It then contains n_i for every i in I by the literal rank-one products of §5.

For an actual `g=u t n_w b in H`, undo ONLY u in U<=H to get `g_0=t n_w b in H`. Since b normalizes U and the torus normalizes its n_w-conjugate,

`g_0 U g_0^-1=n_w U n_w^-1`.

We do NOT assume t or B_G lies in H. A nonidentity signed/even-signed w has a left descent i with w^-1(alpha_i) negative. Its FULL negative simple root group is inside this conjugate, so i lies in I and n_i lies in H. The actual element `n_i^-1 g_0` belongs to the shorter cell s_i w: moving n_i past t changes only a torus factor. Simple coordinate reflections permute positive roots except their own, so each descent lowers the finite inversion length by one; a signed permutation preserving the ordered positive chamber is identity. Repetition gives a word for every H-cell using ONLY indices in I.

If I were all simple indices, E generated by U and every negative simple group would be normalized by B_G and contain all n_i. It would be NONTRIVIAL NORMAL in G, hence G by the explicit simplicity hypothesis, forcing H=G. A PROPER H therefore omits an index.

In nonsplit type an omitted j gives the actual space `<e_1,...,e_j>` fixed by B_G and all the remaining simple representatives. In split type an omitted j<=m-2 gives that space; omitting the last difference-root gives `<e_1,...,e_(m-1),f_m>`, while omitting the last sum-root gives `<e_1,...,e_m>`. All H-cells fix the indicated space. Thus every proper overgroup of any Sylow2-subgroup lies in one of these ACTUAL parabolics, with BOTH split fork families retained. This is the full bridge, not a Borel–Tits/headline import.

## 7. ALL parabolic indices and the common divisor, using the same actual group

Choose ordered independent vectors spanning a j-dimensional singular space. After an a-dimensional singular space is chosen, its orthogonal quotient has dimension n-2a and the SAME type; each nonzero singular quotient vector has q^a singular lifts. Dividing by the number of ordered bases yields

`N_j=product_(a=0)^(j-1) z_(n-2a) / product_(s=1)^j(q^s-1)`.

The q^(sum a) lift factors cancel those in the basis count. Section 5 proves these are ACTUAL G indices, not full-O indices silently transferred through an unknown two-factor. For split maximal spaces take ONE of the TWO equally sized families, not their union.

The Gaussian integer `C_q(k,j)=product_(s=k-j+1)^k(q^s-1)/product_(s=1)^j(q^s-1)` counts j-subspaces by ordered bases. Substitution of §3 gives

`nonsplit 2m: N_j=C_q(m-1,j) product_(s=m-j+1)^m(q^s+1)`, 1<=j<=m-1;

`split 2m: N_j=C_q(m,j) product_(s=m-j)^(m-1)(q^s+1)`, for nonfork j<=m-2;

`split EACH maximal family: N_max=product_(s=1)^(m-1)(q^s+1)`.

Thus EVERY possible parabolic overgroup index is divisible by the SAME integer D: `q^m+1` in nonsplit type, `q^(m-1)+1` in split type. It is greater than1 and does NOT divide seven: that would force D=7 and a positive power of the power-of-two q equal six. No independent primitive-prime selection, missing half-family factor or q=2 exception is hidden here.

## 8. ALL original sources and finish

Suppose the original eight subgroup indices are 7r_l/private pairwise coprime. At most ONE private r_l is even, so at least SEVEN unchanged original indices are odd. Their proper subgroups contain Sylow2-subgroups. Section 6 puts each in SOME conjugate of an actual parabolic; its type may differ between sources and may be either split fork. Section 7 still makes every such original index divisible by the SAME D.

ANY TWO then have gcd divisible by D, contradicting that their actual gcd is exactly seven and D does not divide seven. This proves Theorem E in ALL even fields, including the separate root-membership controls at q=2. No subgroup was enlarged in a purported disjoint family; containment supplied only a divisor of its original index. No original label, full private power, private-seven owner or actual hidden fibre was removed.

## 9. Application, source cut and exact remaining scope

The direct family proof uses only the actual matrix model plus its explicit NONABELIAN-SIMPLE hypothesis, ordinary finite field/group/linear-algebra facts and the fully displayed parity/order/root/flag/index arguments. It needs neither the rank-free representation bound nor an external classical theorem. The arbitrary-group application uses the full supported 88-LF normal-section proof: an actual finite simple P7 factor S of the all-eight finite-core quotient cannot be one of these even-field EVEN-dimensional orthogonal models if this NEW theorem is supported. This does not classify every remaining S or bound arbitrary original ambient size/indices.

The separate 216-LF odd-orthogonal source SHA256 `3fd02a97bb0dd73bf1e871b5102c0ea3b73f71ae04259edf29b8a9fe2181c247` covers ALL odd fields in dimensions>=5; it remains a separate NEW/UNREVIEWED source, not an accepted premise here. Its ordinary root/flag strategy was reconstructed afresh with the characteristic-two corrections: NO determinant-as-Dickson substitution, NO q=2 scalar t!=1, NO odd-characteristic binary norm-base shortcut, and NO dropped nonsplit rank-two case. A later combined orthogonal gate must read BOTH entire bodies and their exact supported inputs.

Odd-dimensional characteristic-two quadratic groups, n<6, other extensions/models and other finite simple families are OUTSIDE this theorem. One may separately prove/consume an actual isomorphism to symplectic groups for the odd quadratic case, but no such unprovided identity or old Sp theorem is silently used. The earlier ALL Sp/PSp and SL/PSL results retain their original named ancestry and assurance boundaries. General Sun8-to-P7/global Sun7, remaining finite simple P7 cases below B, actual eight-coset witnesses, finite assays, numerical R8, unrestricted Sun8 and novelty/priority/SOTA remain unestablished.

The frozen v9 request remains qualified RAW_UTF8_NOT_VALID_JSON under the permanent documentary SYNTAX MINOR and additive author qualification; it was NOT edited or reparsed to confirm the reported failure. All OWN057/047/078/COUNT/M1/v26/v31-two-findings/v33 and parent/reviewer histories remain, with withdrawn historical trial guidance ENTIRELY ZERO. Both Eval kernels stay dead. This is exact WRITTEN primary work after actual v123-C RETURN and a separately WRITTEN-AND-SENT primary ACK; no scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO/source-author-shared-frozen edit was used. No formal/kernel/human/configured-family/executable/novelty acceptance, clean cognition/runtime census or round closeout is claimed. Original arbitrary-group research continues at its exact residual; this is not an early final park.
