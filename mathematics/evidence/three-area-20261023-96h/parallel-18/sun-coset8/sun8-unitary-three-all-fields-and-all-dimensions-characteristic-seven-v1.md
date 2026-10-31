# Sun8 direct P7 — unitary dimension THREE in ALL fields, and ALL unitary dimensions in characteristic SEVEN

Owner MathSun8-2. Actual pre-write observation: `Mon Oct 26 09:09:07 PDT 2026`.
Actual observation before the unpublished higher-dimensional extension: `Mon Oct 26 09:23:09 PDT 2026`. This file was extended and renamed BEFORE its FIRST SHA-256 source pin/delivery; no pinned/reviewed source was changed.
**NEW WRITTEN CANDIDATE; unreviewed/unadopted.** No scientific interpreter, calculator, program, enumeration, matrix replay or kernel arithmetic was used. All identities and cases below are written exact field/integer reasoning.

## 1. Precise theorem and complete union input

Let q=p^f>=2, let K=F_(q^2), and put bar(x)=x^q. On K^3 use the Hermitian form

`h(v,w)=v_1 bar(w_3)+v_2 bar(w_2)+v_3 bar(w_1)`.

Let SU be the group of determinant-one matrices preserving h, and let G be its actual image in PGL_3(K). **Assume G is NONABELIAN SIMPLE.** This is the explicit hypothesis on the actual finite simple group being considered, not a newly cited or proved classification/simplicity theorem for every unitary matrix group. The assertion covers ALL q whenever this model is the actual simple group. No claim identifies every remaining simple group with this model.

**Theorem U.** Such G supports NO direct P7 family of EIGHT actual nonempty pairwise-disjoint LEFT cosets with ALL original indices `7r_l`, positive pairwise-coprime private r_l, including the possible private-seven owner and all its powers.

**Theorem U7, additionally proved in §8.** For EVERY n>=3 and q=7^f, the projective image of the n-dimensional special unitary matrices, IF the actual group is NONABELIAN SIMPLE, supports no direct P7. This is not a claim for n>=4 in other characteristics. Theorem U retains its separate dimension-three/ALL-field scope.

For p!=7 the proof uses only the exact index pattern, explicit matrices and simplicity. For p=7 it additionally uses the ENTIRE NEW 178-LF `sun8-rank-free-three-source-Gram-Farey-finite-simple-bound-v1.md`, SHA256 `76aa8a6fbfd6a2fcf4587ca5bec29e14215bcdfd5ec81dd47f56de9c4ea60e15`, specifically its rank-free small-constituent theorem A. That predecessor is UNREVIEWED, NOT an accepted import. A whole proof gate must supply and reconstruct BOTH full bodies. No McLaughlin, Parker, Jordan, character table, maximal-subgroup list, Stone–von Neumann theorem or CFSG result is an input.

The additional arbitrary-group existence application uses the complete 88-LF `sun8-rank-free-global-existence-bound-complete-part2-v1.md`, SHA256 `b401c139141c451755174f8151942b86916e5677f734715ede48299394716202`. It is also UNREVIEWED and must be read as a full third body for that joint application, not accepted from a headline. Theorem U itself only assumes the actual G here is simple.

## 2. Full unitary root matrices, field counts and projective kernel

Write `Tr(b)=b+bar(b)` and `N(a)=a bar(a)`. The trace map K->F_q is a nonzero F_q-linear map: in odd characteristic Tr(1)=2; in characteristic two any b outside F_q has b+bar(b)!=0. Thus it is surjective and every trace fibre has q elements. In particular there is a NONZERO b with Tr(b)=0.

The following are actual matrices in SU:

`u(a,b) = [[1,-bar(a),b],[0,1,a],[0,0,1]]`, with `Tr(b)=-N(a)`;

`D(t)=diag(t,bar(t)/t,1/bar(t))`, for t in K^*;

`w=[[0,0,1],[0,-1,0],[1,0,0]]`.

For u the first and third columns pair to one; the middle column has norm one; the middle/third pairing is `-bar(a)+bar(a)=0`; the third norm is `Tr(b)+N(a)=0`. Its determinant is one. The diagonal D preserves the first/third pairing and has middle norm one and determinant one. The swap in w and its middle minus sign similarly preserve h and give determinant one. These checks also hold in characteristic two.

Let U be all the u(a,b), and T be all D(t). Direct matrix multiplication gives

`u(a,b)u(c,d)=u(a+c,b+d-bar(a)c)`.

The trace constraint is preserved since the new norm is `N(a+c)=N(a)+N(c)+a bar(c)+bar(a)c`. Thus U is a group of size `q^2*q=q^3`. The projection u(a,b)->a is a surjective homomorphism to the additive K, with central kernel `Z_U={u(0,b):Tr(b)=0}` of order q. Diagonal conjugation gives

`D(t)u(a,b)D(t)^-1 = u((bar(t)^2/t)a, N(t)b)`.

The norm of the new a is `N(t)N(a)`, so this is indeed in U. Hence T normalizes U. Also `w^-1 D(t)w=D(1/bar(t))`, so T normalizes the opposite group `U^-=wUw^-1` as well.

The kernel Z of SU->PGL consists exactly of scalar matrices zeta I satisfying `zeta^3=1` and `zeta bar(zeta)=1`. Its order divides both 3 and q+1, and is prime to p. U has no nonidentity scalar matrix, so it embeds in G. We use the same symbols for its projective image and for T,w,B below. No assumption that an unspecified central extension is simple is made.

## 3. Every isotropic point, the exact stabilizer, and Sylow p

Let infinity be the line K e_1 and zero the line K e_3. An isotropic line other than infinity has a representative with third coordinate one: if its third coordinate were zero then its middle norm would be zero and it would be infinity. It therefore has the UNIQUE form

`K(b,a,1)`, with `Tr(b)=-N(a)`.

There are exactly q^3 such points. The matrices u(a,b) send zero to these points bijectively, so U acts REGULARLY on the q^3 points other than infinity. The matrix w swaps infinity and zero. Thus SU and G are transitive on the actual q^3+1 isotropic points.

The FULL stabilizer of infinity in SU is `B=TU=UT`, not a claimed subgroup of the stabilizer. Indeed its first column is t e_1; unitarity forces the third row `(0,0,1/bar(t))`. The middle diagonal entry is bar(t)/t by the determinant-one condition. Dividing by D(t), the remaining upper triangular unitary matrix has exactly the u(a,b) form: the middle/third pairing forces its (1,2) entry to be -bar(a), and the third norm forces Tr(b)=-N(a). Conversely every D(t)u(a,b) fixes infinity. The factorization is unique, so

`|B_in_SU|=q^3(q^2-1)`, `|SU|=q^3(q^2-1)(q^3+1)`.

In the projective image B is still the FULL point stabilizer and has index q^3+1. Because the scalar kernel is p-free and the two factors q^2-1 and q^3+1 are p-free, U of order q^3 is a Sylow p-subgroup of G.

The same point computation gives the whole rank-one double-coset decomposition without a catalogue. If g does not fix infinity, choose u in U with `uw.infinity=g.infinity`; then `(uw)^-1g` fixes infinity. Hence

`G = B union B w B`.

No assertion about higher-rank groups or an independent building classification is made.

## 4. Every proper overgroup of a Sylow p-subgroup lies in the actual B

Put `E=<U,U^->` in G. T normalizes both groups; U is contained in E. Consequently B=UT normalizes E.

Choose b!=0 with Tr(b)=0, so bar(b)=-b. Also `c=-b^-1` has trace zero. With `v(c)=w u(0,c)w^-1`, the following multiplication is in the original SU matrices:

`u(0,b) v(-b^-1) u(0,b)`

`= n_b := [[0,0,b],[0,1,0],[-b^-1,0,0]] = D(b)w`.

Thus n_b lies in E and `w=D(b)^-1 n_b`. Since `G=<B,w>=<B,n_b>`, E is a NONTRIVIAL NORMAL subgroup of G: B normalizes E and n_b is in E. The explicit nonabelian-SIMPLE hypothesis therefore gives E=G. This proves the needed generation statement; we do not invoke an external theorem that opposite unitary root groups generate a simple group.

Now suppose a proper subgroup J contains U. If g in J were outside B, write `g=b_1 n_b b_2` using §3. Since b_2 normalizes U and n_b conjugates U to U^-,

`gUg^-1=b_1 U^- b_1^-1`.

As b_1 normalizes U, the subgroup generated by U and this conjugate is `b_1 E b_1^-1=G`, contradicting J proper. Hence J<=B. By conjugation, EVERY proper subgroup containing ANY Sylow p-subgroup is contained in the corresponding conjugate of B. This conclusion comes from the actual matrix/point argument, not an unprovided maximal-subgroup classification.

## 5. ALL characteristics other than seven: keep the eight original indices

Suppose p!=7 and a P7 family exists. Pairwise-coprimality of its private r_l means at most ONE r_l is divisible by p. At least SEVEN of the actual original indices 7r_l are therefore p-free. Each corresponding U_l contains a Sylow p-subgroup of G, since its order has the full p-part of |G|. After conjugation, §4 puts it in B.

For ANY TWO of these original subgroups, their indices are both divisible by `[G:B]=q^3+1`. But their gcd is exactly 7. This would require `q^3+1` to divide 7, impossible because q>=2 gives q^3+1>=9. No assumption about which label owns private 7 was made. The original cosets/indices were not projected, thinned or enlarged. This excludes the entire p!=7 case; it does not need the rank-free predecessor.

## 6. Complete faithful-representation lower bound q(q-1), with no character-table import

We next prove an elementary lower bound valid for EVERY faithful complex representation V of this projective G. It uses the ACTUAL embedded U from §2.

The commutator formula from that multiplication law is

`[u(a,b),u(c,d)]=u(0,bar(c)a-bar(a)c)`.

Let A be the inverse image of the additive F_q subset of K under u(a,b)->a. It is normal in U, has order q^2 and index q, and is ABELIAN: for a,c in F_q the displayed commutator vanishes. It contains Z_U.

Choose any NONTRIVIAL character psi of Z_U that occurs in V. One exists because V is faithful and Z_U is nontrivial. Its weight space V_psi is U-invariant. On this space the finite abelian group A has at least one occurring complex character chi, with restriction psi to Z_U.

If x=u(a,b) is outside A, then a is not in F_q. As c varies in F_q, the commutators of x with elements of A have parameters

`bar(c)a-bar(a)c = c(a-bar(a))`.

Since a-bar(a)!=0 and is trace-zero, these parameters exhaust the ENTIRE one-dimensional F_q-space of trace-zero elements, namely Z_U. If x fixed chi under conjugation it would force psi to be trivial on all these commutators, a contradiction. Thus the stabilizer of chi in U is exactly A. Its U-orbit has q distinct characters, all occurring in V_psi with positive multiplicity. Therefore

`dim(V_psi)>=q`.

It remains to count the central characters forced by the torus. The norm homomorphism `K^* -> F_q^*`, t->t^(q+1), is surjective: its kernel has at most q+1 elements by the polynomial degree, so its image has at least `(q^2-1)/(q+1)=q-1` elements, while it is contained in F_q^*. By §2 the torus acts on Z_U by EVERY nonzero scalar in F_q. This action on nontrivial additive characters is free: if scalar s!=1 fixed psi, then `psi((s-1)z)=1` for every z, making psi trivial. There are q-1 nontrivial additive characters, so the action is transitive on all of them.

Conjugation by T therefore forces ALL q-1 nontrivial central-character spaces to occur in V. Each has dimension at least q by the preceding argument. Hence

`dim(V) >= q(q-1)`.

This proves the full lower bound using only displayed matrices, actual subgroup/character weights and the exact norm map. No Stone–von Neumann classification, chosen small matrix, numerical test or table is being imported. Copies and other weight spaces of V can only add dimension.

## 7. Characteristic seven, ALL exponents: combine the full rank-free theorem

Now p=7, q=7^f. If a P7 family exists in this SIMPLE G, apply the entire rank-free theorem A in the 178-LF predecessor to ANY THREE of the original eight cosets. It gives a NONTRIVIAL irreducible representation W of degree d<=1728. Simplicity makes W faithful. Section 6 therefore implies

`q(q-1)<=d<=1728`.

If f>=2 then q>=49, so `q(q-1)>=49*48=2352>1728`, a contradiction. This is the exhaustive symbolic exponent case, not a selected parameter trial or numerical scout. The ONLY surviving value is the FORCED theorem base case f=1, q=7, handled next.

At q=7 the scalar projective kernel has order dividing BOTH 3 and q+1=8, hence is trivial. The exact order from §3 factors as

`|G|=7^3*(7^3+1)*(7^2-1)=7^3*344*48=2^7*3*7^3*43`.

Here `344=8*43` and `48=16*3`. The number 43 is prime: its possible prime divisors below its square root are 2,3,5, none of which divides it, since `6^2<43<7^2`. Thus `|G|/7` has ONLY FOUR distinct prime owners, namely 2,3,7,43.

Each ORIGINAL private r_l divides |G|/7, because its original index 7r_l divides |G|. Pairwise-coprime nonunit r_l must own distinct primes from this four-element set. Hence at most FOUR of the eight r_l are nonunit; at least FOUR original subgroups have index EXACTLY seven. For any such subgroup, the actual degree-seven coset action of SIMPLE G is nontrivial and has a proper normal kernel, so is faithful. It would embed G in S_7. But 43 divides |G| and does not divide 7!, contradicting the subgroup-order formula. This excludes q=7 with ALL private-seven powers still accounted for in `|G|/7=2^7*3*7^2*43`.

Thus every p=7 exponent is excluded. Together with §5, Theorem U holds for ALL fields at its explicit simple-model hypothesis.

## 8. ALL unitary dimensions n>=3 in characteristic seven

We now prove Theorem U7 completely. Put m=n-2>=1 and use the nondegenerate Hermitian form with block matrix

`J_n=[[0,0,1],[0,I_m,0],[1,0,0]]`

over K=F_(q^2). Let G_n be the actual projective image of its determinant-one unitary matrices, with the EXPLICIT hypothesis that G_n is NONABELIAN SIMPLE. No theorem classifying simple groups or proving simplicity of every such matrix model is being imported.

### 8.1 Full higher-dimensional central-weight lower bound

The actual block matrices

`P(a,b)=[[1,-bar(a)^T,b],[0,I_m,a],[0,0,1]]`, with `a in K^m` and `Tr(b)=-bar(a)^T a`,

form a subgroup of order `q^(2m+1)`. Their multiplication and commutator are exactly the scalar formulas of §2/§6 with `bar(a)c` replaced by `bar(a)^T c`. They preserve J_n and have determinant one by the same column pairings. The scalar projective kernel meets this unipotent group trivially.

Its central subgroup is the actual order-q group `Z={P(0,b):Tr(b)=0}`. Let A be the preimage of `F_q^m` under P(a,b)->a. It is NORMAL and ABELIAN, of order `q^(m+1)` and index `q^m`. For x=P(a,b) outside A, at least one coordinate a_j is outside F_q. Commutators with c in F_q^m have parameters

`sum_j c_j(a_j-bar(a_j))`.

By varying that single c_j, these exhaust ALL trace-zero parameters, hence all Z. Exactly the character-stabilizer argument of §6 now gives, for EVERY occurring nontrivial central character psi, an A-character orbit of size q^m inside its weight space. Thus `dim(V_psi)>=q^m` for any faithful complex representation V.

The needed torus is not asserted to be scalar on the middle block. For t in K^*, set

`S(t)=diag(bar(t)/t,1,...,1)` on K^m,

`D_n(t)=diag(t,S(t),1/bar(t))`.

It is unitary for J_n and has determinant one. Conjugation sends `a -> bar(t)S(t)a` and `b -> N(t)b`; the middle unitary factor makes the new norm `N(t)bar(a)^T a`. The norm is surjective by §6. Its action therefore forces ALL q-1 nontrivial central-character spaces. Consequently EVERY faithful complex representation has

`dim(V)>=q^m(q-1)=q^(n-2)(q-1)`.

For n>3 this block subgroup is NOT asserted to be a Sylow p-subgroup or to have the §4 proper-overgroup property. Neither assertion is needed here.

If direct P7 existed in SIMPLE G_n, the full 178-LF rank-free predecessor would give a faithful W with d<=1728. For q=7^f with f>=2, the lower bound is at least `49*48=2352>1728`. For f=1 and n>=5 it is at least `7^3*6=2058>1728`. Thus the ONLY cases left by these exhaustive symbolic inequalities are q=7 with n=3 or n=4. The n=3 case was excluded in §7. We prove the n=4 case without a table.

### 8.2 Complete ordinary unitary order formula needed for n=4

Every nondegenerate Hermitian form over K has an orthonormal basis. To justify this elementary fact here, if all self-pairings were zero, then for every v,w and every alpha in K, the self-pairing of v+alpha*w would give `Tr(alpha*h(w,v))=0`. Surjectivity of the trace would force every h(w,v)=0, contradicting nondegeneracy. Thus a vector of nonzero norm exists; surjectivity of N scales it to norm one. Its orthogonal complement is nondegenerate, so induction gives an orthonormal basis. This proves the required equivalence to the diagonal form, not a classification of groups.

For the diagonal form, let F_j count vectors in K^j of norm zero and E_j count vectors of norm one. Nonzero norm values all have E_j representatives, by scalar norm-surjectivity. A single coordinate has one representative of norm zero and q+1 of each nonzero norm. Counting the last coordinate gives

`F_j+(q-1)E_j=q^(2j)`,

`F_(j+1)=F_j+(q^2-1)E_j`,

`E_(j+1)=(q+1)F_j+(q^2-q-1)E_j`.

With F_0=1,E_0=0, subtraction yields `F_j-E_j=(-q)^j`. Thus, for j>=1,

`E_j=q^(j-1)(q^j-(-1)^j)`.

Counting ordered orthonormal bases one vector and its orthogonal complement at a time gives

`|U(n,q)|=product_(j=1)^n E_j=q^(n(n-1)/2) product_(j=1)^n (q^j-(-1)^j)`.

The determinant map is onto the norm-one scalars, of order q+1: the matrices diag(zeta,1,...,1) realize each such zeta. Dividing by q+1 gives the ENTIRE determinant-one order formula

`|SU(n,q)|=q^(n(n-1)/2) product_(j=2)^n (q^j-(-1)^j)`.

No character/subgroup/order table has been used.

### 8.3 The remaining forced q=7,n=4 case, with every original index

The formula just proved gives

`|SU(4,7)|=7^6*48*344*2400=2^12*3^2*5^2*7^6*43`.

Here `2400=2^5*3*5^2`, and §7 already gave the exact 48/344 factors and primality of 43. The scalar projective kernel has order dividing BOTH 4 and q+1=8, hence is a power of two at most four. Passing to G_4 cannot remove 43 or introduce a new prime. Thus `|G_4|/7` has at most FIVE distinct prime owners, all in `{2,3,5,7,43}`, and 43 still divides |G_4|.

Each of the EIGHT original private r_l divides |G_4|/7. Pairwise coprimality permits at most five nonunit r_l, so at least THREE original subgroups have index seven. The same faithful degree-seven coset action as in §7 would embed SIMPLE G_4 in S_7, impossible because of the prime 43. All possible higher private-seven powers in the original indices were retained in this divisor argument.

This excludes the last case. Theorem U7 holds for ALL n>=3 and ALL q=7^f at the explicit simple-model hypothesis. It is NOT a claim for n>=4 in characteristic different from seven: the higher-dimensional block group was not treated as a full Sylow subgroup, nor was an unprovided parabolic-overgroup theorem used.

## 9. Complete application and proof boundaries

The whole family conclusion is a SAME-G exclusion: all eight original subgroups, pairwise-coprime private factors, exact indices and possible private-seven owner were retained. The p!=7 branch uses the actual Sylow subgroups/full Borel index, not independently selected one-cut cores or abstract quotient cells. The p=7 branch uses the actual small representation promised by the FULL rank-free predecessor, not a claimed bound on the whole orbital module or a multiplicity-one assumption. The representation lower bound applies to that faithful W regardless of its other weights or copies.

For the arbitrary-original-group existence application, the prospective complete 266-LF manuscript first constructs an actual finite NONABELIAN SIMPLE P7 factor S of a finite-core quotient, with eight labelled private divisors. If S is identified with the projective SU3 model over ANY field, Theorem U contradicts P7; if identified with projective SU(n,7^f) for ANY n>=3, Theorem U7 does so. These remove exactly those simple-factor families, not all finite simple factors or the arbitrary original group's order. Simplicity is the explicit output of the complete 88-LF normal-fibre proof; no new global Sun7 or general Sun8-to-P7 reduction is supplied here.

All load-bearing model/order/Sylow/point/Bruhat/overgroup/central-weight identities are reconstructed in this body. The only special NEW direct-mathematics dependency is the ENTIRE 178-LF rank-free theorem, and the arbitrary-group application additionally needs the ENTIRE 88-LF normal-section composition. These are literal full proof inputs to a fresh whole-union gate, not accepted source labels. The older ALL SL/PSL and Sp/PSp family proofs are NOT inputs, and their McLaughlin/Parker/Smith1969/Suzuki ancestry and process findings are not erased or silently reused. No classical simplicity classification is certified beyond the explicit hypothesis on G.

## 10. Exact residual, process and assurance

The new global direct-P7 manuscript's finite-simple bound B does not search or exclude ALL its finite cases. Theorems U/U7 would remove dimension-three projective unitary models over ALL fields and ALL unitary dimensions n>=3 in characteristic SEVEN IF their FULL proof and dependency/application gates pass. Higher unitary dimensions in other characteristics, all other unexcluded simple models/coset configurations, full source/fibre problems and the general Sun8-to-P7/global Sun7 boundary remain. No unrestricted Sun8, actual eight-coset witness, completed finite assay, numerical R8, novelty/priority/SOTA or public-refutation claim is made. No original label, full integer index or private power is replaced by an initial elementary rank.

This proof was developed in the separately acknowledged primary period after actual v123-C RETURN. OWN057/047/078/COUNT/M1/v26/v31-two-findings/v33 and all received parent/reviewer findings remain permanent; all withdrawn historical trial guidance receives ENTIRELY ZERO credit. The forced q=7 base case is a displayed proof branch of the universal theorem, not reuse of any withdrawn input or a private numerical capacity probe. Both Eval kernels stay dead; no scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/new GO/source-author-shared-frozen edit was used. WRITTEN work is not formal/kernel/human/configured-family/executable/novelty acceptance, a clean cognition/runtime census or round closeout. Original research continues at the exact remaining arbitrary-group gap, not an early final park.
