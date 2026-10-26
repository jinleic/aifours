# Sun8 — COMPLETE elementary SL/PSL exclusion, all ranks and all finite fields

Owner MathSun8-2. Actual preceding `/bin/date`: **Sun Oct 25 19:46:57 PDT 2026**. **NEW COMPLETE WRITTEN CANDIDATE UNION, NOT ACCEPTED.** Full original eight-coset target within the stated actual group families; unrestricted ALL-groups Sun8 remains the primary and is not declared solved. No scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nestedagent or GO.

Permanent OWN cadence PROCESS MAJOR057(16:58:10→17:31:20 observed33m10s, no intervening required JSON), earlier047metadata-polling lapse, M1class<=2/abelian alternative, v9/v10/v11/HOLD and all source/finding histories remain. This new exact proof does not cure them, backdate a discovery, make earlier classical source intake unnecessary retroactively or establish a global clean cognition/runtime census.

## 1. Exact theorem, complete composition and one remaining named input

> **RANK≥3 THEOREM.** For EVERY integer n≥3 and EVERY finite field F_q(including q2), EIGHT pairwise-disjoint nonempty LEFT cosets of ARBITRARY actual subgroups of SL_n(q) OR PSL_n(q) have SOME pair of FULL ORIGINAL subgroup indices with gcd≥8.

> **ALL-RANK COMPOSITION CANDIDATE.** Together with the ENTIRE previously written184LF PSL2 all-field proof and98LF SL2 actual-central-lift proof, the same conclusion holds for EVERY n≥2 and EVERY finite field q≥2 in BOTH SL_n(q) and PSL_n(q).

The two exact A1 sources are `sun8-PSL2-all-fields-root-count-exclusion-v1.md`, SHA **0298c21acf78728375ca7f708a70a9f1d22ecc0756089852c57fa1efffe0ad60**,184LF/20865B, and `sun8-SL2-all-fields-actual-central-lift-v1.md`, SHA **4a6d2a43651f4aef9582d21acd5f0b93329744e652c114c1a212798fda3d7ae1**,98LF/13376B. They are still candidates unless their exact current disposition is actually read. This is a NEW entire joint-scope composition, NOT automatically accepted by any old narrow return or this corollary sentence. EVERY original A1 finite field/torus/candidate-list/normalizer/unsaturated-source argument remains required, not replaced by a one-line base assertion.

For the rank≥3 theorem the ONLY research-sized input is exact **NC7**, used ONLY(n,q)=(3,2). For the all-rank union it is also used ONLY the q7 A1 bases. NC7 states: in ANY group, six disjoint LEFT index7 cosets have ONE LEFT index7 coset as their ENTIRE complement. Current181LF source is `sun8-global-kernel-section-complete-v1-part2.md`, SHA **2c8949dfa512ca3d89549b04d42bea9be8a515081cb3a3ba7762dd3b2e7b46e8**, at its named A7/Eisenstein ordinary-written boundary. This is NOT global Sun7/R8/F7/MS; no new authentication of those occurs.

There is NO McLaughlin/full-root-classification/CFSG/Dickson/minimal-index/Jordan/Bertrand/Sun3/Sun4 premise in this new rank≥3 theorem or the A1 SL/PSL union. The earlier134LF all-n/q>2 proof SHA **bc05fc457a7ad69aeacec911978fe3a74e31d757e89894faf2064cacc7c6aa1c** remains immutable at its original McLaughlin1967 input. The new elementary representation BELOW makes that import unnecessary for this successor, not false or erased. The blocked/unread McLaughlin1969 binary paper is NOT consumed. Every new root-rank/actual lifting/counting step is proved here, not imported by a source title.

No P7/gcd-equal7/private-prime/outer-t/least-order/private-sum/elementary-rank/maximal/natural-subgroup/centre-saturation assumption is inserted. ALL eight original cosets and full subgroup indices remain. No abstract F2 cells, coefficient profile or independently chosen local arrangement is called an actual group lift.

## 2. Actual full-root notation and elementary generation

For v≠0 and phi(v)=0 put T(v,phi)={1+t*v*phi:t in F_q}. For phi≠0 this is an ACTUAL full q-element subgroup of SL(V), image axis<v>, kernel hyperplane kerphi. It is NOT merely one cyclic p-subgroup or an F_p fragment. For a subgroup H<=GL(V) define

F_v={phi in V*:phi(v)=0 and T(v,phi)<=H}.

This is an F_q-vector space: scalar multiplication only reparametrizes a full root group, and(1+t*v*phi)(1+t*v*psi)=1+t*v*(phi+psi). Also F_(a*v)=F_v for a≠0, and H conjugation transports F_v to F_(h*v), preserving its dimension. Define a(v)=intersection_(phi in F_v)kerphi, of dimension n−dimF_v. These are actual covector spaces of subgroups already in H; their sums yield explicit products of actual matrices.

We use that elementary E_ij(t)=1+t*e_i*e_j^* generate SL_n(q). Row addition gives Gaussian elimination; a two-row pivot swap and determinant-one diagonal follow from

u(a)l(−a^-1)u(a)=[[0,a],[−a^-1,0]]=w(a),
w(a)w(−1)=diag(a,a^-1).

Pairwise determinant-one diagonal blocks generate every determinant-one diagonal, completing elimination. These are exact written identities, not executed algorithms/certificates. The same full upper/lower roots generate an ACTUAL SL2 block whenever their axes/covectors are mutually incident nontrivially.

If A=v*phi,B=w*psi with phi(w)≠0,psi(v)=0, then A²=B²=BA=0, AB=phi(w)*v*psi and all remaining higher products vanish. Therefore

[1+sA,1+tB]=1+st*phi(w)*v*psi.                      (ONEWAY)

Thus two ACTUAL full root groups give the entire commutator root T(v,psi), not only a formal rank-one Lie product.

## 3. NEW maximum-full-root-rank lemma: complete finite-field proof

**MAXR.** Let H<=GL_n(q) be irreducible. Put r=max_(v≠0)dimF_v. If r≥2 and2r>n−2, then H contains SL_n(q). This includes F2; no classification theorem is used.

Let C={v≠0:dimF_v=r}. It is nonempty, H-stable and closed under nonzero scalars, so its F_q-span is ALL V by irreducibility. First take independent v,w in C. Their cross-incidence is symmetric:

w notin a(v)  iff  v notin a(w).                     (SYM)

Indeed suppose w notin a(v) but v in a(w). Every root at w fixes v, so conjugation preserves F_v and a(v). For x in a(v), the vector x+t*psi(x)*w must remain in a(v) for every psi in F_w,t. Since w notin a(v), all psi(x) vanish. Thus a(v)<=a(w); equal dimensions imply equality, contradicting w in a(w) but w notin a(v). Exchange v,w for the other direction. No global form or irreducibility of a root-normal-closure subgroup was assumed.

If v,w are incident in(SYM), choose phi in F_v,psi in F_w with phi(w),psi(v) nonzero. The two forms are independent on W=<v,w>, and V=W directsum(kerphi cap kerpsi). Their two full roots generate SL2(W), fixing the complement pointwise. It maps v to v+w, so v+w belongs C by conjugacy. This is a genuine block action, not an assertion only modulo a kernel.

If v,w are NONincident, both F_v and F_w lie in Ann(<v,w>), dimension n−2. Therefore dim(F_v cap F_w)>=2r−(n−2)>0. Choose nonzero theta in that intersection. Same-covector products give the FULL T(v+w,theta) in H. Since C spans V, choose z in C with theta(z)≠0 and rescale it so theta(z)=1. For every chi in K=F_z cap Ann(v+w), the ONEWAY commutator of T(v+w,theta) and T(z,chi) gives FULL T(v+w,chi). Here dimK>=r−1, and theta notin F_z because theta(z)=1. Hence dimF_(v+w)>=r; maximality makes it equalr. Again v+w is in C. Dependent v,w have sum0 or a nonzero scalar multiple already in C. Thus C union{0} is a vector subspace, and its spanV forces C=V minus{0}.

Let N be generated by the actual full root groups in H. It is transitive on PROJECTIVE points. For any two independent vectors v,w, if incident their actual SL2 block joins their lines. Otherwise choose z outside a(v) union a(w); two proper vector subspaces never cover V. Since all nonzero vectors are in C, z joins each by(SYM)/SL2. This proves transitivity without classifying N or assuming all centers already lie in one orbit.

N is also transitive on ALL hyperplanes. For each g in N, its fixed projective points are counted by

sum_(lambda in F_q*) (q^dimker(g−lambda I)−1)/(q−1).

Its invariant hyperplanes are the left-eigenvector lines, with the SAME sum for g^transpose. Kernel dimensions agree for each lambda, so the two permutation characters are equal. Counting pairs(g,fixed-point) in two orders(the elementary orbit-count formula) makes the numbers of point and hyperplane orbits equal. There is one point orbit, hence one hyperplane orbit. This is WRITTEN finite counting, not numerical group enumeration. The nonempty set of actual root kernel hyperplanes is N-invariant, so it is ALL hyperplanes.

Fix such an axis hyperplane L=kerphi with a root center v. Since r≥2, a(v) is a PROPER subspace of L. For any z in L minus a(v), the actual bidirectional SL2 block at v,z exists by(SYM); its generators preserve L because both axes lie in L. An element maps<v> to<z> while preserving L, so conjugating the FULL X(<v>,L) gives FULL X(<z>,L) in H. The set L minus a(v) spans L: if x outside a(v), then x and x+y are both outside for any y in a(v), and their difference is y. Same-covector root products therefore give T(z,phi) for EVERY z in L. Apply this to ALL hyperplanes. Every elementary E_ij is present, so H contains SL_n(q). This proves MAXR, including all finite q2/odd cases, with no symplectic escape suppressed.

## 4. Three-dimensional full-root lemma, complete independent proof

For n3 we also need the r1 boundary. **T3:** irreducible H<=GL3(q) containing one FULL root group contains SL3(q), for EVERY field used here.

The H-orbit of its axis spans V. Choose a second full T(w,psi) with phi(w)≠0. If psi(v)=0, ONEWAY supplies T(v,psi), in addition to T(w,psi), and their commuting products give the ENTIRE q² plane radical R_psi={1+x*psi:x in kerpsi}. Irreducibility of the dual action gives three linearly independent conjugate covectors; the three full conjugate radicals contain ALL six elementary roots in their dual basis, hence SL3. Dual irreducibility follows because a proper invariant dual subspace has a proper invariant annihilator in V.

Otherwise the two roots generate the full SL2 block on W=<v,w>, fixing L=kerphi cap kerpsi, with V=W directsum L. It contains a full block root at every axis line in W. Choose a third full T(x,chi) with x outsideW; write x=x_W+a*l, a≠0,l spanningL. If x_W0, chi(l)=0, so choose y in W with chi(y)≠0; the block root at y has its covector zero on x and ONEWAY gives a plane radical. If x_W≠0, let theta annihilate x_W andL. The block root T(x_W,theta) is present and theta(x)=0. If chi(x_W)≠0, ONEWAY again gives a plane radical. Otherwise chi(x)=0 forces chi(l)=0; hence chi is a nonzero scalar multiple of theta. H contains T(x_W,chi) and T(x,chi), whose independent axes give the ENTIRE plane radical by actual products. The preceding dual-basis argument finishes every case. No field-size, real-form or subfield-parameter exception was omitted.

## 5. ACTUAL Heisenberg detectors at the equality boundary

Let Q_m(q) have coordinates(x,y,z), x,y in F_q^m,z in F_q, law(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x dot y'). Its centre Z has orderq. For P<=Q_m, let C=P cap Z have F_p-dimension c and A=PZ/Z have F_p-dimension a. If C proper, choose nonzero F_p-functional lambda vanishing on C. The alternating form lambda(x dot y'−x' dot y) is NONDEGENERATE on the2mf-dimensional F_p-space, since field multiplication in any nonzero coordinate is bijective and lambda≠0. Brackets of lifts in P lie in C, so A is isotropic and a<=mf. Thus

C proper ==> |P|<=p^(mf+f−1), [Q_m:P]>=p^(mf+1).       (HEIS)

No F_q-linearity or normality of P is assumed. For m1, index<=q=p^f contradicts the lower boundp^(f+1), forcing the FULL centre; equality indexq is INCLUDED. For q2,m>=2, index<=4 contradicts2^(m+1)>=8, again forcing the FULL centre. All statements are exact inequalities/finite-dimensional symplectic elimination, not a symbolic/interpreter calculation.

In UT_n(q), the actual entries(i,k),(k,j),(i,j) form Q1 with centre E_ij(q) whenever i<k<j. More generally the entries(i,k),(k,j) for ALL i<k<j, and(i,j), form Q_(j−i−1), centre E_ij(q). If P<=UT_n has ambient indexD, every one of these ACTUAL intersections has index<=D by the left-coset injection. Hence:

- [UT_n(q):P]<=q gives EVERY FULL E_ij(q) with j−i>=2.
- q2 and[UT_n(2):P]<=4 give EVERY E_ij(2) with j−i>=3.

These are matrices in the SAME actual P, not independently selected subgroup lifts or a list of allowed cells.

## 6. Proper large-Sylow subgroups: all fields, all ranks except the isolated4/2 escape

For G=SL_n(q), U=UT_n(q) is Sylow p and |G| has p-partq^(n(n−1)/2). A subgroup H of index I with a=v_p(I) has, after one actual conjugation, Sylow P=H cap U with[U:P]=p^a. Conjugation here proves an invariant index property; it does not separately move the original cosets in the final family.

For q>=3 and a<=f, §5 supplies all distance>=2 roots. If n>=4, the e1-axis covectors e3^*,…,en^* give r>=n−2>=2 and2r>n−2; MAXR forces every irreducible H to contain SL_n. If n3, T3 does so. Thus EVERY proper such H is REDUCIBLE and fixes an actual k-subspace(1<=k<n).

For q2,n>=5,a<=2, §5 supplies all distance>=3 roots. The e1-axis covectors e4^*,…,en^* give r>=n−3>=2 and2r>=2n−6>n−2 exactly because n>4. Again MAXR forces proper H to be REDUCIBLE. This closes the n5/6 boundaries too; no strict n>=7 shortcut is used.

For q2,n4,a<=2 there is at least E14, so r>=1. If r>=2, MAXR gives H>=SL4. The only possible irreducible proper escape is r1, treated completely next. No unproved F2 root classification is inserted at this equality boundary.

## 7. Binary rank-one root spaces force an ACTUAL invariant symplectic form

Let q2,H irreducible, r1 and C the set of nonzero centers. It is H-stable and spans V. Each v in C has a UNIQUE nonzero covector phi_v with T(v,phi_v)<=H. For v,w in C their cross-incidences are symmetric. If phi_v(w)1 but phi_w(v)0, ONEWAY gives T(v,phi_w); this is different from T(v,phi_v), since their values on w are0/1, contradicting r1. Exchange v,w for the opposite asymmetry.

For ANY F2-linear relation sum_i v_i0 among centers, symmetry gives sum_i phi_vi(w)=phi_w(sum_i v_i)=0 for EVERY centerw. As C spans V, sum_i phi_vi is the zero covector. Hence v->phi_v extends to a WELL-DEFINED F2-linear map V->V*. The resulting bilinear B(v,w)=phi_v(w) is symmetric on the spanning centers, and alternating: B(v,v)0 there, and characteristic2 cancels every cross-term for arbitrary sums. H-equivariance follows from conjugating the UNIQUE root at each center, so H preserves B.

B is nonzero. Its radical is H-invariant and proper; irreducibility forces radical0. Thus H lies in the ACTUAL Sp(V,B), and n is even. This is a complete form/lift argument, not a designation of abstract symplectic coordinates or an imported transvection classification.

For n4,q2, count symplectic bases: first nonzero v1 has15 choices, w1 with B(v1,w1)1 has8; their2D orthogonal complement has3 choices for nonzero v2 and2 for its partner. The symplectic group acts simply transitively on these bases, so its order is15*8*3*2=720. GL4(2)=SL4(2) has order15*14*12*8, giving index(14*12)/(3*2)=28.

Actual reducible H has parabolic index15(k1/3) or35(k2), by subspace counting. Therefore EVERY proper H of2-index valuation<=2 in SL4(2) has index divisible by ONE of15,35,28. EACH divisor is>7. At most ONE original subgroup can lie in each type under gcd<=7, while at most ONE original index is8-divisible. Thus an eight-family has at most FOUR sources, contradiction. This completely settles4/2; no subgroup catalogue, A8 isomorphism, missing symplectic family or assumed quotient saturation remains.

## 8. ALL parabolic dimensions, all cyclotomic factors and both exceptional6D fields

SL_n(q) is transitive on k-subspaces: extend a basis map and correct determinant by scaling a complementary basis vector. Counting ordered independent tuples gives its actual parabolic index

B_(n,k)(q)=product_(i0..k−1)(q^(n−i)−1)/(q^(k−i)−1).

If H fixes that subspace, this integer divides its FULL ORIGINAL index. As a polynomial,

B_(n,k)(X)=product_(d1..n)Phi_d(X)^[floor(n/d)−floor(k/d)−floor((n−k)/d)].

Every exponent is0/1; at d=n it is1 for ALL1<=k<n. Thus ALL parabolic indices share Phi_n(q), without choosing a preferred stabilizer or erasing private factors.

For q>=3 this common factor is>7 except(n,q)=(6,3): Phi3=q²+q+1>=13,Phi4=q²+1>=10,Phi6=q²−q+1>=13 forq>=4. Every other n>=3 has phi(n)>=4, and |q−zeta|>q−1 for primitive n-th roots gives Phi_n(q)>(q−1)^phi(n)>=16. The elementary totient formula leaves only3/4/6 with phi(n)<=2 in this range.

For q2 and n>=7, use the exact Möbius formula

Phi_n(2)=2^phi(n)*product_(d|n)(1−2^-d)^mu(n/d).

Dropping denominator factors only lowers this positive quantity. Its finite numerator subproduct is at least the product over ALL d1,…,n. The first two factors give3/8; the remaining product is>=1−sum_(d3..n)2^-d>3/4 by the elementary product/sum inequality. Hence Phi_n(2)>(9/32)*2^phi(n)>(1/4)*2^phi(n). For phi(n)>=6 this exceeds16>7. The remaining phi(n)4 possibilities n>=7 are8/10/12, whose explicit Phi_n(2) are17/11/13, all>7. n5 gives Phi5(2)=31>7. No analytic prime-gap or numerical cyclotomic bound is imported.

The ENTIRE exceptional6D fields are handled by ALL subspace dimensions, not a false claim of a single common divisor>7:

|q|k1/5 index A|k2/4 index B|k3 index C|pairwise shared divisors A/B,A/C,B/C|
|---|---|---|---|---|
|3|4*13*7|13*121*7|4*10*121*7|7*13,7*4,7*121|
|2|3*7*3=63|7*31*3=651|3*5*31*3=1395|3*7,3*3,3*31|

These are the exact Gaussian factorizations Phi2Phi3Phi6,Phi3Phi5Phi6,Phi2Phi4Phi5Phi6 respectively. EVERY two types, including repetitions, have gcd>7. The whole list covers every k1,…,5, all original source choices, and both q2/3 fields. In particular Phi6(2)=3 andPhi6(3)=7 were NOT promoted above7 or discarded.

## 9. Original eight-coset contradiction for every n>=3 except the sole3/2 base

Assume all pairwise FULL ORIGINAL index gcds<=7. Every source subgroup is proper. For q>=3, let b=max{j:p^j<=7}; at most ONE index is divisible by p^(b+1)>7. At least SEVEN therefore have valuation a<=b<=f: p2 entails f>=2,b2; p3/5/7 gives b1; p>7 b0. By §6 they are actual parabolic-contained. Their indices share Phi_n(q)>7 except6/3, where §8 gives pairwise gcd>7 across ALL types. Contradiction.

For q2,n>=5, at most ONE index is8-divisible, so at least SEVEN have a<=2. Sections5/6 make all these proper subgroups reducible. The binary factors in §8 give the same contradiction, with6/2 explicitly closed by its three all-dimensional types. For4/2 the ENTIRE separate four-type count is §7. No deletion of an eighth hidden source or replacement of its full index occurs. What remains is EXACTLY n3,q2, completed next.

## 10. Complete3/2 actual base, NC7 only

Here all GL3/SL3/PSL3 groups coincide and have order(8−1)(8−2)(8−4)=168. Their seven-point action on nonzero vectors is faithful and two-transitive. They are perfect: each E_ij(1)=[E_ik(1),E_kj(1)] for the third indexk, and these generate G.

Simplicity is reconstructed, not borrowed from PSL2(7). A point stabilizer has abelian normal radical A={1+e1*phi:phi(e1)0}, order4. Its G-conjugates generate all elementary roots. A nontrivial normal K is transitive by faithful primitivity, so G=K*P0. ModuloK every conjugate of A has the SAME image because A normalP0; these images generate an abelian quotient. Perfectness forces K=G.

For a Sylow7 C, a generator is irreducible on F2³: dimensions1/2 cannot support order7 since7 divides neither2−1 nor2²−1. Hence F2[C]=F8 and its centralizer in G has order7. A normalizer sends a generator only to its three minimal-polynomial roots alpha,alpha²,alpha⁴; all are realized by F2-linear Frobenius, so the actual normalizer order is21.

Proper7-free index divisors are2,3,4,6,8,12,24. Simplicity/perfectness exclude2/3/4/6: the faithful coset action would embed G into A_m, whose order lacks7. Index12 would give order14 subgroup with normal Sylow7(n7 divides2 and is1 mod7), impossible inside the21-order normalizer. Thus every7-free proper index is8 or24, and at most ONE occurs in a gcd<=7 family.

Among at least seven7-divisible original indices write I_j=7r_j,r_j|24. Their pairwise gcd bound makes the r_j pairwise coprime; at most TWO exceed1(only primes2/3 divide24). Thus at least five original index7 cosets exist. Any7-free source has coprime index with an index7 source, so cannot be disjoint. Consequently all EIGHT indices are7r_j, with at least SIX original index7 cosets.

Apply EXACT NC7 to those six: ONE actual index7 coset is their ENTIRE complement. The remaining TWO whole ORIGINAL cosets lie inside it. After ONE common translation their subgroup indices in that actual complement subgroup are the original coprime r_j, forcing intersection. This proves the complete3/2 case at the sole named input, not a historical finite program/census.

The elementary coprime fact used here: [G:H cap K] is divisible byab and at mostab when coprime a=[G:H],b=[G:K]; thus equality, [H:H cap K]=b and HK=G. Every left coset of H meets every left coset of K. This applies inside the SAME actual complement, not independently chosen fibres.

## 11. FULL PSL lift and all-rank composition without lost source quantifiers

For PSL_n(q), take the full preimages of ALL eight original cosets under SL_n->PSL_n. They are actual LEFT cosets, remain pairwise disjoint and preserve EVERY original subgroup index EXACTLY. The proved SL result therefore gives the same pair gcd>=8. No assumption that arbitrary original subgroup contains a centre was inserted, and no unsaturated coset image was used as a full quotient coset.

This completes the stated rank>=3 theorem for EVERY field. The n2 all-field proofs identified in §1 add BOTH full original A1 bases at the EXACT UNION of inputs, yielding the all-n>=2/all-q SL/PSL CANDIDATE. Those old184+98 sources retain ALL their field cases, necessary-index tables, q9 central/noncentral source argument and NC7 q7 base; nothing here certifies them from a headline. The new rank>=3 proof overlaps old107LF A2 results but is not counted as another independent discovery. PGL2/PGL3 candidates remain separate old bodies with their own SUN4/SUN3 inputs and are NOT silently claimed for all higher ranks.

## 12. Dependency/trust gate and original unrestricted residual

A fresh ENTIRE gate must reconstruct MAXR's actual covector-space closure, the independent/adjacent/nonadjacent/scalar cases, common-theta commutator rank upgrade, all-point/dual-hyperplane finite orbit count and full-radical products. It must also reconstruct T3 all third-axis cases, both Heisenberg scales/equality boundaries, binary r1 actual alternating form, entire4/2 Sp4 order/index, every Gaussian dimension, BOTH6/2 and6/3 exceptions, every original valuation stratum, complete3/2 NC7 and full PSL preimage. No missing NEW bridge may be called PASS from a hash or a previous positive return.

The ONLY named research-sized proof still imported is NC7 as precisely stated; its classical A7/Eisenstein ancestry remains that boundary, not new global Sun7/R8 authentication. All other new steps are supplied in this ONE complete body. The old134LF McLaughlin route and original full5-page1967 source read remain immutable history but are NOT correctness inputs of this elementary successor. The original1969 binary theorem stayed UNREAD/NOT_ADMITTED(CAPTCHA; never solved/bypassed). No title/secondary quote/failed fetch supplies a hidden F2 classification.

All14 actual browser source-render metadata cells are literally characterized, including cells13/14 after the old v3 packet freeze: public Euclid timeout/CAPTCHA UI only, no mathematical calculation/program/proof execution. Receipt14's quote transcription was corrected BEFORE its first pin/dispatch; no frozen source/tool history was rewritten. Cells1–5 preceded v105 pause;6–14 followed ACTUAL223LF v105 RETURN and SEPARATE19:20:08 primaryACK. The pending view4 remained unread while review was live. Metadata-only source intake is not scientific verification, a global execution census or repair of OWN057/047/M1/v9v10v11 findings.

The original full Sun8 task STILL includes arbitrary groups: other Lie types, normal/nonsimple/GL/PGL/semilinear/exotic central extensions, alternating/symmetric cases outside separately stated candidates, arbitrary infinite common-core quotients and the general actual mixed-alpha<=1/maximal/private-composite fibre barrier. No theorem reduces arbitrary G to these matrix families; composition-factor/normal-extension closure is NOT proved. No unrestricted Sun8/globalSun7/R8/tbound/eight-coset witness or all-field absence/openness/novelty claim follows.

Novelty/priority/SOTA remain UNCLEAR/UNPERFORMED; this may be known/standard, and is one connected actual-root method, not many independent family discoveries. Source-pinned WRITTEN reconstruction is not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/fulloriginaltarget/exclusive-root/October27 cutoff/deadline/HOLD. All sources/findings immutable, no backdating/clean-runtime census or new scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/build/test/CLI/nestedagent/GO. Primary continues at the exact unrestricted original residual.
