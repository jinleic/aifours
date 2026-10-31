# Sun8 for binary Sp/PSp in every rank m>=5 — an elementary orthogonal-triad route

Owner MathSun8 / MathSun8-2. Actual preceding `/bin/date`: **Mon Oct 26 05:13:49 PDT 2026**. **WRITTEN CANDIDATE, not reviewed or adopted.** All arguments are exact handwritten group/linear/cyclotomic algebra; no interpreter, calculator, program, enumeration, solver or replay. This is a COMPLETE theorem for the stated family, NOT unrestricted Sun8.

## 0. Exact theorem, independent premises, old boundaries

**Theorem.** Let m>=5 and G=Sp_(2m)(2), or G=PSp_(2m)(2). For ANY eight arbitrary actual subgroups H_1,...,H_8 and ANY eight pairwise-disjoint nonempty LEFT cosets g_i H_i, there are distinct i,j with

    gcd([G:H_i],[G:H_j]) >= 8.

All FULL ORIGINAL indices are used. No normalizer/private-factor replacement, minimum-counterexample assumption, source saturation, rank-one quotient or independent alteration of the eight cosets is made.

This proof uses only basic finite-group Sylow theorems, finite-dimensional linear algebra over F2, and the elementary order/cyclotomic identities derived below. In particular it uses NO McLaughlin1967/1969 transvection classification, Parker–Rowley, SUN3/SUN4, NC7/globalSun7, root-type/CFSG/minimal-index table, orthogonal-group classification, or earlier Sun-family conclusion.

The prior nonbinary Sp/PSp and binary Sp4 base have their own independently supported scopes/imports. Parent records `sun-Sp-odd-even-entire-parent-v1.md` and `sun-Sp4-exception-binary-base-and-nonbinary-composition-parent-v1.md` were ACTUALLY read after the separate post-v112 primary ACK; they are NOT correctness premises here. The latter now supports all q>2,m>=2 at McLaughlin1967+Parker2002, and q2,m2 at SUN4. **Binary m3 and m4 remain OPEN in this manuscript.** Combining accepted families with this NEW candidate is not automatic adoption of the candidate, not arbitrary-group Sun8, and not a normal/composition-factor extension theorem.

The new reasoning was already exposed in checkpoint079 BEFORE the latest send-order ACK; no false post-ACK discovery/preregistration. Checkpoint079's invented parent-source LF46 is withdrawn by the distinct source-count exactness finding: actual38LF/8187B, prior raw1-100 did reach the true END. All permanent OWN057/047/078/count findings, M1 class-at-most-two/abelian alternative and every parent history remain. No earlier unadmitted computation is a premise.

## 1. The actual binary Sylow and its lower-central detector

Write V=F2^m+F2^m with basis e_1,...,e_m,f_1,...,f_m and

    B((x,y),(x',y')) = x^T y' + y^T x'.

For A upper unitriangular and S symmetric, put

    D(A)=diag(A,A^(-T)),    u(S)=[I S;0 I].

Their products form U=UT_m(2) semidirect Sym_m(2), of order2^(m(m-1)/2+m(m+1)/2)=2^(m^2). The symplectic-basis count chooses a nonzero e in2^(2j)-1 ways and a partner f with B(e,f)=1 in2^(2j-1) ways, then continues in the orthogonal complement. Thus

    |Sp_(2m)(2)| = 2^(m^2) product_(j=1)^m (2^(2j)-1),

so this ACTUAL U is Sylow. For v!=0 write T_v(x)=x+B(x,v)v. It is a rank-one symplectic involution and gT_vg^(-1)=T_(gv). In particular L_i=u(E_ii)=T_(e_i). Let X_ij=u(E_ij+E_ji), and A_ij=I+E_ij, i<j. All u(S) commute. With [a,b]=aba^(-1)b^(-1), direct multiplication gives

    D(A)u(S)D(A)^(-1)=u(ASA^T),
    C_ij := [D(A_ij),L_j] = X_ij L_i,                  (1)
    [D(A_jk),X_ik] = X_ij  for i<j<k.                 (2)

For (1), A_ij E_jj A_ij^T+E_jj=E_ij+E_ji+E_ii. For (2), the two off-diagonal additions are E_ij,E_ji and the diagonal term is0. Thus no characteristic2 long-root term is dropped.

Let gamma_1(U)=U, gamma_(r+1)(U)=[U,gamma_r(U)]. Formula(2) gives X_ij in gamma2 whenever j<m. Combining with(1) gives L_i in gamma2 for i<=m-2. For each i<=m-3 choose FOUR distinct ordered indices i<j<k<ell. First X_ik is in gamma2 by using ell in(2); hence X_ij is in gamma3 by using j,k in(2). Also L_j is in gamma2 because j<=m-2, so C_ij is in gamma3 by(1). Therefore

    L_i = C_ij X_ij is in gamma3(U)  for EVERY i<=m-3.  (3)

Take j=i+1,k=i+2,ell=i+3; all are available. This is the binary four-index argument, not the q>=4 two-distinct-scalar argument.

Now analyze ONE arbitrary proper subgroup H with a=v2([G:H])<=2. Choose a Sylow P of H and a Sylow U of G containing P. Then H cap U=P (any larger intersection would be a larger2-subgroup of H), and [U:P]=2^a<=4. Choose the above flag basis for THIS U. The action of U on U/P has image a2-subgroup of S4, hence is contained in a Sylow D8 and has nilpotency class at most2. This includes indices1 and2. Its kernel is inside P even if P is NOT normal. Therefore gamma3(U) is inside P.

For every nonzero v in E=<e_1,...,e_(m-3)>, let i be its last nonzero coordinate. An upper unitriangular A sends e_i to v. Normality of gamma3(U) in U and(3) give

    T_v in gamma3(U) subset P subset H  for ALL v in E minus0.  (4)

For m>=5 this is an entire totally isotropic plane of transvection axes, not just two unrelated axes. Different H may require different Sylow/flag bases; that is an invariant INDIVIDUAL-subgroup analysis. No independently conjugated eight-coset family is ever substituted for the original one.

## 2. An elementary binary transvection-axis closure lemma

Let S be the nonzero axes whose transvections belong to a symplectic subgroup. It is stable under conjugation by those transvections. Hence

    u,v in S and B(u,v)=1  =>  u+v in S.              (5)

This follows from T_u(v)=u+v; all uses of(5) below have pairing exactly1. No closure under arbitrary orthogonal addition is assumed.

### 2.1 Radical-extension lemma

Suppose EVERY nonzero vector of a subspace W belongs to S, and r in rad(W) satisfies B(r,x)=1 for an axis x in S. Then EVERY nonzero vector of W+<x> belongs to S.

Indeed x is outside W. For y in W with B(x,y)=1, (5) gives x+y. If B(x,y)=0, then y+r is nonzero, belongs to W and pairs1 with x, so x+y+r belongs to S. Its pairing with r is1, so adding r by(5) gives x+y. This covers all y including0. The whole original W was already present.

### 2.2 An orthogonal triad creates a full nondegenerate4-space

Suppose u,v,u+v are axes, u,v independent and B(u,v)=0, inside a connected axis component whose span is nondegenerate. Choose an axis w pairing nontrivially with <u,v>. After changing the basis of that plane, arrange B(u,w)=1,B(v,w)=0. The vectors u+w and u+v+w follow from(5); pairing the latter with u then gives v+w. Thus ALL seven nonzero vectors of W3=<u,v,w> are axes. Its radical is <v>.

Nondegeneracy of the component span supplies an axis x with B(v,x)=1. The radical-extension lemma produces ALL nonzero vectors of W4=W3+<x>. The original rank2 form on W3 and the new pair(v,x) give a nondegenerate4-space. No unproved binary classification has entered.

### 2.3 Grow a full nondegenerate block by2 dimensions

Let W be nondegenerate, dimW>=4, and all its nonzero vectors axes in ONE connected component S_0 with nondegenerate span V_0. If W!=V_0, a path in that component has a first axis a outside W adjacent to an axis in W. Write its orthogonal projection

    a=t+z,  t in W minus0, z in W^perp minus0.

The subgroup K_W generated by the transvections at ALL nonzero W vectors fixes W^perp pointwise and is transitive on W minus0. To check transitivity: when B(s,t)=1, T_(s+t) sends s to t. When distinct s,t have pairing0, the two independent linear functionals B(s,.),B(t,.) admit c with both values1, and s->c->t is obtained by two such transvections. Each conjugation preserves the connected component: it fixes its own axis and is an automorphism of the axis graph.

It follows that z+w is an axis for EVERY w in W minus0. Since z belongs to V_0 and V_0 is nondegenerate, choose an axis x in S_0 with B(z,x)=1. If x has zero W-projection, replace it by x+a, which is an axis by(5), still pairs1 with z, and now has W-projection t!=0. Thus assume s=x_W!=0.

Choose v in s^perp cap W with v neither0 nor s; this exists because dimW>=4. K_W's orbit on x gives x+v as an axis, since s+v!=0. Also z+v is an axis. Their pairing is

    B(x+v,z+v)=B(x,z)+B(s,v)=1.

So x+z is an axis. Its pairing with x is1, forcing z itself to be an axis. We now have ALL nonzero vectors of W+<z>, whose radical is<z>. Apply2.1 with x. This yields ALL axes on W+<z,x>, a nondegenerate space of dimension dimW+2: after subtracting x_W, the new pair in W^perp has pairing1.

Iterating finishes V_0. The iteration is a finite-dimensional proof, not a vector enumeration. Consequently:

**Axis-component lemma.** A connected axis component with nondegenerate span that contains an orthogonal triad u,v,u+v contains EVERY nonzero vector of its span.

### 2.4 Full transvections generate the full symplectic group

For completeness this last group identification is also elementary. The transitivity argument moves an arbitrary nonzero first basis vector to e_1. After fixing e_1, let a be the image of f_1, so B(e_1,a)=1. If a=f_1 do nothing. If B(a,f_1)=1, T_(a+f_1) maps a to f_1 and fixes e_1. If B(a,f_1)=0, first apply T_(e_1), then T_(a+e_1+f_1); both fix e_1 and the composition sends a to f_1. Continue in the symplectic orthogonal complement. Induction expresses every isometry as a product of the available transvections. Thus a full-axis component supplies Sp on that component, fixing its orthogonal complement pointwise.

## 3. Excluding proper irreducible H of2-index at most4

Assume H is irreducible on V and satisfies the hypothesis of§1. Put S={v!=0:T_v in H}. It is nonempty by(4), is H-invariant, and therefore spans V. Form its graph with edges exactly B(u,v)=1. Distinct components have orthogonal spans V_i. Since they together span nondegenerate V, each V_i is nondegenerate and their sum is DIRECT: a radical vector or an intersection vector would be orthogonal to ALL V. H permutes the components/spans. Irreducibility forces this permutation to be transitive, since the sum over any component orbit is H-invariant. All blocks therefore have one dimension2d, with kd=m.

All nonzero vectors of E from(4) lie in the union of these direct blocks. An entire vector subspace contained in a union of direct summands must lie in ONE summand: if it contained nonzero vectors from two different summands, their sum would lie in neither. Thus E lies in one V_i. It contains an orthogonal triad, so§2 makes ALL nonzero V_i axes. H-transitivity gives this property for EVERY block. Therefore H contains the direct product of their full symplectic groups and is contained in the decomposition normalizer

    Sp_(2d)(2)^k semidirect S_k.

Moreover E is isotropic of dimension m-3, so d>=m-3 and

    k <= m/(m-3),  kd=m.                             (6)

For m>=7, (6) forces k=1. For m5 it gives k<=2, while k divides5, so k=1. In either case full transvections give H=G, contrary to properness. For m6 the only additional possibility is k2,d3. The normalizer then has2-part2^(2*3^2+1)=2^19, whereas G has2-part2^36. Hence

    v2([G:H]) >= 36-19 = 17 > 2,

again impossible. This covers EVERY m>=5, not only sufficiently large ranks.

We have proved: **every proper H with v2([G:H])<=2 is reducible**, without McLaughlin1969, a root-type classification, an orthogonal-overgroup theorem, or a prior Sp-family result.

## 4. Every such reducible H lies in an actual isotropic parabolic

Choose a nonzero proper H-invariant subspace W. If W is nondegenerate, dimW=2r with1<=r<m, and H embeds in Sp(W)xSp(W^perp). The order formula gives

    v2([G:H]) >= m^2-r^2-(m-r)^2 = 2r(m-r)
                   >= 2(m-1) > 2,

contradiction. Otherwise R=W cap W^perp is nonzero, H-stable and totally isotropic. Thus H lies in the ACTUAL stabilizer P_R of an r-dimensional isotropic space,1<=r<=m. Its index is

    J_(m,r)(2) = product_(i=m-r+1)^m (2^(2i)-1)
                 / product_(j=1)^r (2^j-1).          (7)

One can count ordered isotropic bases: after j vectors, the next choice is2^(2m-j)-2^j=2^j(2^(2(m-j))-1); dividing by the ordered GL_r-basis count cancels the2-powers and gives(7). All r, including maximal isotropic r=m, are covered.

## 5. One common factor greater than7 for ALL parabolic types

The polynomial J_(m,r)(x) equals the Gaussian binomial {m choose r}_(x^2) times product_(j=1)^r(x^j+1). Every cyclotomic exponent is nonnegative: for the Gaussian factor the exponent belonging to divisor order e is floor(m/e)-floor((m-r)/e)-floor(r/e)>=0, and each x^j+1 is itself a product of cyclotomic polynomials. Directly in(7), Phi_(2m)(x) occurs ONCE in the numerator (i=m) and never in the denominator (j<=m<2m). Therefore

    Phi_(2m)(2) divides J_(m,r)(2)  for EVERY r.       (8)

We verify uniformly that this factor is greater than7 for m>=5. The Möbius product identity gives

    Phi_N(2)=2^phi(N) product_(d|N)(1-2^(-d))^mu(N/d).

The denominator factors are all less than1. The numerator is at least the product of ALL factors1-2^(-d),1<=d<=N. For d>=3, the finite inequality product(1-a_d)>=1-sum a_d gives a lower bound strictly greater than3/4; including d1,2 gives a product greater than9/32>1/4. Hence

    Phi_N(2) > 2^phi(N)/4.                           (9)

For an even N>=10, phi(N)<=4 is possible only for N10 or12: any prime divisor has p-1 dividing phi(N), so only2,3,5 occur; their exponent formula immediately gives those two even cases above8. In the remaining cases phi(N)>=6 and(9) gives Phi_N(2)>16>7. Explicitly

    Phi_10(2)=16-8+4-2+1=11,
    Phi_12(2)=16-4+1=13.

Thus(8) supplies one SAME integer greater than7 in every proper H index with v2([G:H])<=2. This is a full ORIGINAL index divisibility: [G:H]=[G:P_R][P_R:H], not a private quotient or a separately enlarged source claimed to preserve disjointness.

## 6. The eight ORIGINAL cosets and the PSp transfer

Suppose the theorem failed and every pair of full original indices had gcd<=7. Each H_i is proper: a whole-G coset cannot be disjoint from another nonempty coset. At most ONE original index can be divisible by8, since two such indices already have gcd>=8. Therefore at least SEVEN original subgroups have v2([G:H_i])<=2.

Sections1–5 apply to EACH of these original subgroups, using a suitable individual Sylow/flag only to prove its invariant containment property. Their original indices ALL have the common divisor Phi_(2m)(2)>7. Any pair among them contradicts the assumed gcd<=7. At no point were original cosets translated separately, projected through an unproved common kernel, replaced by independent fibre arrangements, or counted after source loss.

For PSp, take full preimages under Sp->PSp. Full preimages preserve left-coset disjointness and EVERY index exactly. Applying the Sp theorem gives the result for PSp. This transfer requires no assumption that the original subgroups are already saturated, no arbitrary central-extension closure, and no new computational witness.

## 7. Exact residual, complete-union status and assurance

The theorem as written is a NEW CANDIDATE for ALL binary m>=5. The elementary axis-component lemma and its actual gamma3 detector are both proved here rather than named from the unread1969 source. An independent whole mathematics/dependency/application gate is still required; no author claim is adopted by this file.

The exact binary-family residual is m3,m4. In m3 the detector E is empty; in m4 it is only one-dimensional and does NOT supply an orthogonal triad. Proper binary orthogonal overgroups in m3 can have2-index4, so size alone does not close that case. A bare index4 intersection with the point radical does not provide Parker's order2^(2m-2) transvection-free X. The local m4 D8-module lead saved in079 can still leave only the e1 axis; it is not a group/coset witness or an exclusion. No claim about these two ranks is made.

With the separately accepted nonbinary/the binary m2 base, prospective symplectic coverage would be all m>=2,q except q2,m3/4, at the UNION of the older named imports and this elementary theorem. That is a composition candidate until the NEW whole gate, not a retroactive v110/v112 verdict. Original arbitrary-group Sun8 remains unresolved: other Lie types, higher GL/PGL/semilinear or nonsimple/exotic-central/normal extensions, remaining alternating/symmetric degrees, infinite/common-core reductions and the actual mixed-alpha/private-source fibre barrier remain. The earlier finite-P7/minimum/rank/kernel results retain their exact named scopes/M1 and are not hidden premises here. No global Sun7/R8/t-bound, actual eight-coset counterexample, or automatic extension/composition-factor principle follows.

All identities/counts in this manuscript are **WRITTEN**, not checked in an arithmetic or proof kernel. Only source reads, metadata hashes/LF counts and actual clocks were used as tools. Both Eval kernels stay dead; no scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, source/shared/frozen edit, deletion, git or publication. All owner count/cadence/turn-end/metadata/M1 and parent v9/v10/v11/v17–v19/v23 histories remain permanent, not cured by prospective correctness. No clean-thought/runtime/execution census, formal/human/configured-family/kernel/executable/priority/novelty acceptance, new owner/deadline, or early final park. Same18, original science cutoff2026-10-27T11:05:38-07:00 and delivery12:35:38.
