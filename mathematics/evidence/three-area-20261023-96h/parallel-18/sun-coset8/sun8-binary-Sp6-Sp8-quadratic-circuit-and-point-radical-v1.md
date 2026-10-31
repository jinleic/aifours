# Sun8 for Sp6(2) and Sp8(2) — quadratic consistency, a five-circuit module, and an actual point radical

Owner **MathSun8 / MathSun8-2**. Actual preceding `/bin/date`: **Mon Oct 26 06:25:51 PDT 2026**. **NEW WRITTEN CANDIDATE, not reviewed or adopted.** This is ONE complete manuscript for BOTH remaining binary symplectic ranks, including all new finite-group, quadratic, module, point-radical and original-coset bridges. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay or GO.

## 0. The two exact theorems and the inherited elementary lemma

**Theorem A (elementary rank4).** For G=Sp8(2) or PSp8(2), ANY eight pairwise-disjoint nonempty LEFT cosets of arbitrary actual subgroups have two FULL ORIGINAL indices with gcd>=8.

**Theorem B (rank3 at a named classical import).** The same assertion holds for G=Sp6(2) or PSp6(2), at **Parker–Rowley2002 Theorem1.1, EXACT q=2,n=3**, with the complete new applicability proof in§8. Its original proof's Smith1982/McLaughlin1969/Suzuki ancestry remains NAMED/NOT_RECONSTRUCTED. No binary transvection classification is imported independently.

The operative elementary predecessor is the COMPLETE170LF manuscript `sun8-binary-Sp-all-m-ge5-orthogonal-triad-v1.md`, SHA256 **ec1a0e4bab33ae2f3c1ff1640c92fddcb75096259954083c21be9ee7ee17b332**. Its§2 supplies the fully proved axis-component lemma:

> For a set of binary symplectic transvection axes closed under u+v whenever B(u,v)=1, a connected axis component with nondegenerate span containing an orthogonal triad u,v,u+v contains EVERY nonzero vector of its span. Its full transvections generate the full symplectic group on that span.

This is an ALREADY reconstructed elementary lemma, not a McLaughlin theorem: triad -> all seven axes of a3-space -> radical extension to nondegenerate4-space -> actual projection/orbit growth by2 until the component is full -> explicit symplectic-basis elimination. The complete predecessor, not merely this quotation, belongs to any fresh whole gate for the present manuscript. Its special m>=5 THEOREM is NOT applied at m3/4; the axis lemma has no such rank restriction. All new supporting low-rank detector identities are re-derived below.

The previous170LF theorem is now parent-supported by `sun-binary-Sp-all-m-ge5-entire-parent-v1.md`, actually read completely. Old nonbinary and binary-rank2 adoptions retain their own exact McLaughlin1967/Parker2002/SUN4 imports/editorial MINOR and are not correctness premises of A or B. Theorem A needs no special classical classification; B adds ONLY the named Parker theorem to the elementary predecessor.

Original arbitrary-group Sun8 remains a different unresolved target: no automatic normal/central/composition-factor extension, common-core/infinite reduction, private-source enlargement or abstract-cell-to-coset witness follows. All original subgroups, cosets and indices are retained throughout this manuscript.

## 1. Actual binary Sylow subgroups and two low-rank identities

Let V=F2^m+F2^m, m3 or4, with symplectic basis e_i,f_i and B((x,y),(x',y'))=x^T y'+y^T x'. Put

    D(A)=diag(A,A^(-T)),  u(S)=[I S;0 I],
    U={D(A)u(S): A upper unitriangular, S symmetric},
    L_i=u(E_ii)=T_(e_i), X_ij=u(E_ij+E_ji), A_ij=I+E_ij.

Symplectic-basis counting gives |Sp_(2m)(2)|=2^(m^2) product_(j=1)^m(2^(2j)-1). Since |U|=2^(m^2), this actual matrix U is Sylow. As in the elementary predecessor, direct multiplication, with [a,b]=aba^(-1)b^(-1), gives

    [D(A_ij),L_j]=X_ij L_i=:C_ij,
    [D(A_jk),X_ik]=X_ij  (i<j<k).                    (1)

The first identity retains the diagonal long-root term. All u(S) commute. Write gamma_(r+1)(U)=[U,gamma_r(U)].

For ONE arbitrary proper H with a=v2([G:H])<=2, choose a Sylow P of H inside a Sylow U of G. Then H cap U=P and [U:P]=2^a<=4. The ACTUAL coset action theta:U->Sym(U/P) has image a2-subgroup of S4, hence class at most2; its kernel lies inside P. Thus gamma3(U)<=P. This uses no normality of P, no assumption about a fixed unrelated Sylow, and no independent conjugation of the original eight-coset family.

For **m4**, formula(1) gives

    X_13=[D(A_34),X_14] in gamma2,
    X_23=[D(A_34),X_24] in gamma2,
    L_2=C_23 X_23 in gamma2,
    X_12=[D(A_23),X_13] in gamma3,
    C_12=[D(A_12),L_2] in gamma3,
    L_1=C_12 X_12 in gamma3.                          (2)

Therefore EVERY such rank4 H contains the ACTUAL transvection T_(e1). This is only one axis, not an isotropic plane; the higher-rank detector is not falsely reused.

For **m3**, the identities instead supply

    X_12=[D(A_23),X_13] in gamma2,
    L_1=C_12 X_12 in gamma2,
    X_12=[D(A_23),C_13] in gamma3,                     (3)

because D(A_23) fixes L_1. These will control the actual D8 image of a transvection-free H. Formula(3) does NOT say L_1 lies in gamma3 in rank3.

## 2. Intrinsic axis components and a quadratic-consistency lemma

For a subgroup H containing at least one transvection, let

    S={v in V minus0 : T_v in H},
    T_v(x)=x+B(x,v)v.

Conjugation gives gT_vg^(-1)=T_(gv); hence S is H-invariant and

    u,v in S, B(u,v)=1  => u+v in S.                 (4)

If H is irreducible, S spans V. Form the axis graph with edges B(u,v)=1. Distinct components have orthogonal spans. Since together they span nondegenerate V, these spans are nondegenerate and their sum is DIRECT: a radical/intersection vector would be orthogonal to all V. H permutes them transitively, since a sum over one permutation orbit would otherwise be a proper invariant subspace. Thus all block dimensions are2d, with kd=m.

An orthogonal triad u,v,u+v lies entirely in ONE such block: if u and v were in different direct blocks, their sum could not be in the union of the blocks. The inherited axis-component lemma then makes that block full-axis, of dimension at least4; H-transitivity makes every block full-axis. This is an elementary consequence of the ACTUAL S, not a theorem about a guessed transvection subgroup's semisimplicity.

### Quadratic consistency

Fix ANY quadratic q0 with polar form B, and for s in S put delta(s)=1+q0(s). We claim:

> If there is no quadratic q with polar B satisfying q(s)=1 for every s in S, then S contains an ODD, pairwise-orthogonal minimal circuit of length at most m+1.

A linear functional extending delta exists exactly when the delta-sum of every F2-linear relation among S is0. If it fails, take a relation with delta-sum1. Whenever two terms u,v pair1, replace them by u+v, which belongs to S by(4). The relation and its delta defect are preserved because

    delta(u)+delta(v)+delta(u+v)=1+B(u,v)=0.

Delete any duplicate pairs. Each operation reduces the number of terms, so eventually the remaining distinct nonzero terms are pairwise orthogonal and still have sum0/defect1. On a pairwise-orthogonal relation q0 of the sum equals the sum of q0 values, hence0; the defect is therefore its length mod2, so that length is ODD.

An odd relation contains an odd minimal circuit: remove a minimal even subrelation if one exists; if a minimal odd one is found, stop. The process strictly decreases size and cannot exhaust an odd relation with even removals. In a minimal circuit every proper subset is independent. Its span is isotropic of dimension at most m, so its length is at most m+1. Length1 is impossible because all axes are nonzero. This proves the claim.

Conversely, if every relation has delta-sum0, delta extends to a linear functional ell on span S=V, and q=q0+ell is the required quadratic. It is UNIQUE because S spans V. Since H permutes S and preserves B, q composed with any h is another such quadratic, so uniqueness makes q H-invariant.

For **m3**, an odd circuit of length<=4 must have length3, exactly an orthogonal triad. Thus absent a triad, an irreducible transvection-containing H preserves a quadratic form. For **m4**, absent a triad and absent such a quadratic, the circuit has length EXACTLY5 and isotropic rank4. No classification or computer search has been used.

## 3. Exact quadratic-form orbits and their indices

All quadratic forms with polar B are

    q_(a,b)(x,y)=x dot y+a dot x+b dot y,
    a,b in F2^m.

Summing first over y gives the exact Gauss identity

    sum_(x,y)(-1)^q_(a,b)(x,y)=2^m(-1)^(a dot b).

There are2^(m-1)(2^m+1) forms with a dot b=0 and2^(m-1)(2^m-1) with a dot b=1. To see that each is ONE Sp orbit rather than merely a count, use an elementary Witt basis. In dimension>=4 choose two independent B-orthogonal vectors u,v; if neither is isotropic, q(u+v)=1+1+0=0. Thus a nonzero isotropic e exists. Choose f with B(e,f)=1 and replace f by f+q(f)e to obtain q(f)=0. Split this hyperbolic plane off and continue. At the last2-space there is either another hyperbolic plane or the unique anisotropic form. The Gauss signs distinguish the two outcomes. Hence forms of each sign have an isometric symplectic basis and Sp acts transitively on each sign class.

Therefore their ACTUAL stabilizers O(q) have indices

    [Sp_(2m)(2):O(q)] = 2^(m-1)(2^m+1) or2^(m-1)(2^m-1).  (5)

For m3 the values are36 and28; for m4 they are136 and120, both divisible by8. This is a proved orbit count, not an atlas order or a minimal-index assertion.

## 4. Rank4: dispose of the triad and quadratic cases

Let H<Sp8(2) be irreducible with a=v2([G:H])<=2. It has a transvection by(2), so§2 applies.

If S contains an orthogonal triad, its full-axis block has dimension2d>=4. With kd=4 the proper decomposition possibility is k2,d2 (k1 would give H=G). Its decomposition normalizer Sp4(2)^2 semidirect S2 has2-part2^(4+4+1)=2^9, whereas G has2-part2^16. Thus a>=7>2, impossible.

If S admits the quadratic of§2, H<=O(q) and(5) makes8 divide its index, also impossible. The ONLY remaining possibility is an orthogonal5-circuit C={c1,...,c5}, sum_i c_i=0, with every four independent. We exclude it next with a complete ACTUAL module argument.

## 5. Rank4 five-circuit: all45 axes and their coherent model

The span E=<C> is a4-dimensional Lagrangian. All c_i lie in ONE axis component: projection of the circuit relation into any different direct block would give a forbidden proper subrelation. A nondegenerate block containing this isotropic rank4 already has dimension at least8, so this is the ENTIRE V and the axis graph is connected.

### 5.1 Exactly five axes in E; exactly two pairing positions outside E

The15 nonzero vectors of E are precisely the five c_i and the ten sums c_i+c_j, i<j. The latter are distinct and not c_k by minimality of the5-circuit. Any such sum being an axis would make an orthogonal triad, excluded here. Hence

    S intersect E = C.                               (6)

For an outside axis x, its pattern I(x)={i:B(x,c_i)=1} has even size because sum c_i=0. It is nonempty since E is Lagrangian. If it had size4, the four corresponding independent c_i span E, and conjugating T_x by their commuting transvections gives EVERY x+y, y in E, as an axis. Let k be the missing index and choose i in I(x). Then x and x+c_i+c_k pair1, so c_i+c_k would be an axis, contradicting(6). Therefore

    EVERY outside axis has pattern EXACTLY{i,j}.      (7)

### 5.2 Exactly four lifts of each populated pair pattern

The pairing pattern determines the coset modulo E, because E=Eperp. Fix an axis x of pattern{i,j}. Conjugations by T_ci,T_cj give all four x+<c_i,c_j> as axes.

Suppose x+y is any other axis in that coset, y in E. If B(x,y)=1, (4) makes y an axis in E, and(6)/(7) give y=c_i orc_j. If B(x,y)=0, x+y+c_i is an axis and pairs1 with x; thus y+c_i is an axis in E and has pairing1 with x, so y+c_i is c_i orc_j. In either case y belongs to<c_i,c_j>. Thus EXACTLY four lifts occur, not an unproved full16-point fibre.

Let Gamma be the graph on labels1..5 whose edges are populated pair patterns. If ij and jk occur, change an axis of pattern ij by c_j if needed to make it pair1 with an axis of pattern jk. Their sum is an axis of pattern ik. Therefore every connected Gamma-component is a clique.

If Gamma had more than one component, axes supported on different label-components would all pair0: a pairing1 between two disjoint pair patterns would produce a forbidden size4 pattern. A c_i pairs only with axes whose pattern contains i. Hence the ENTIRE axis graph would split according to Gamma-components (including any isolated c_i), contrary to its connectedness. Gamma is therefore K5. By(6) and the exact four-lift result,

    |S| = 5+4*10 = 45.                               (8)

### 5.3 All phase bits are globally coherent

Choose x_i of pattern{i,5}, i1..4, and write b_ij=B(x_i,x_j). For any distinct i,j,k, replace x_i by x_i+eta c5 with eta=1+b_ij. It now pairs1 with x_j, so their sum is an axis of pattern ij. Its pattern is disjoint from that of x_k, so its pairing with x_k MUST be0 (else a size4 pattern). Hence

    b_ij+b_ik+b_jk=1  for EVERY triple i,j,k.          (9)

Set eta1=0 and eta_i=1+b_1i for i2..4; replace every x_i by x_i+eta_i c5. Formula(9) now gives

    B(x_i,x_j)=1 for ALL i!=j.                        (10)

This is ONE simultaneous choice of four representatives, not independently chosen local phases. Also B(c_j,x_i)=delta_ij for i,j1..4. The eight vectors c1..c4,x1..x4 form a basis: pairing with all c_j first kills every x coefficient, then independence of c1..c4 kills the rest.

### 5.4 The actual deleted10-point module and the order obstruction

Let D be the even-weight subspace of F2^10, modulo its all-ones vector. The ordinary dot product is alternating on the even-weight space; its radical is exactly the all-ones line, so D is a nondegenerate symplectic8-space. In D put

    c_i'=e_(2i-1)+e_(2i), i1..5,
    x_i'=e_(2i-1)+e9, i1..4.

Then c5'=sum_(i=1)^4 c_i', B(c_j',x_i')=delta_ij and B(x_i',x_j')=1 for i!=j. Thus the basis map c_i->c_i',x_i->x_i' is an ACTUAL symplectic isometry by(10), not merely a matching of support dimensions.

It maps S onto ALL45 weight2 edge vectors of K10. The five c_i are the within-pair edges. Each pattern{i,5} has its four edges by adding c_i,c5. For i,j<=4, x_i+x_j is an axis by(10), and its four-lift orbit gives all four edges between those two pairs. All45 edge classes are distinct modulo the all-ones line: a difference of two weight2 vectors cannot have weight10.

Two such axes pair1 exactly when their two edges meet in one endpoint. Thus the ACTUAL axis graph is the line graph of K10. Its ten stars are intrinsically the maximal9-cliques. To verify uniqueness, any pairwise-intersecting edge family with edges ab,ac either has all edges through a, or contains bc; in the latter case it is contained in that triangle. Hence every clique of size>3 lies in a star. A graph automorphism permutes these ten stars faithfully, since each edge is the intersection of its two endpoint stars.

H acts faithfully on S: over F2 a fixed axis ray is a fixed vector, and S spans V. Therefore H embeds in Sym10. But

    v2(|H|)<=v2(10!)=5+2+1=8,
    v2(|Sp8(2)|)=16,

so a>=8>2, contradiction. This exhausts the five-circuit case and proves:

**Every proper subgroup of Sp8(2) with2-index at most4 is reducible.**

## 6. Rank4: actual parabolics and the eight ORIGINAL indices

A nondegenerate proper invariant2r-space puts H in Sp_(2r)(2)xSp_(8-2r)(2), with2-index valuation2r(4-r)>=6>2, impossible. Otherwise the nonzero radical of an invariant subspace is ACTUALLY H-stable and totally isotropic, so H lies in an isotropic parabolic of some dimension1<=r<=4.

Its exact index is J_(4,r)(2)=product_(i=5-r)^4(2^(2i)-1)/product_(j=1)^r(2^j-1). Gaussian-binomial factorization has nonnegative cyclotomic exponents, and Phi8(x) occurs once in the numerator and never the denominator. Hence the SAME Phi8(2)=17 divides EVERY such index and therefore the FULL ORIGINAL [G:H]. The elementary count/nonnegative-factor proof is supplied in the complete predecessor§§4–5 and applies verbatim here; its m>=5 numerical bound is not needed because the present factor is explicitly17.

If every pair among eight original disjoint left-coset indices had gcd<=7, at most ONE could be divisible by8. The other at least SEVEN subgroups are proper (a whole-G coset meets every nonempty coset) and have2-index at most4. They are all reducible by§§4–5, hence their ORIGINAL indices are all17-divisible, contradiction. This proves Theorem A.

## 7. Rank3 if H contains a transvection

Let H<Sp6(2) be irreducible and have a transvection. Its axis set spans V. If it contains an orthogonal triad, the elementary component lemma gives a full block of dimension>=4; transitive equal blocks have kd=3 and d>=2, forcing k1 and H=G, impossible. Without a triad, the quadratic-consistency lemma§2 gives an H-invariant quadratic with polar B. Thus by(5)

    28 divides [G:H] or36 divides [G:H].             (11)

This contains NO separately imported binary transvection classification. The transvection-FREE case is handled by the exact named theorem only AFTER its actual X is constructed next.

## 8. Rank3 without transvections: SAME-D8 fibres give the ACTUAL Parker X

Suppose H is irreducible, a<=2 and contains NO transvection. Retain its actual Sylow P=H cap U, the action theta on U/P, and R={u(S):S symmetric3x3}, an elementary abelian normal subgroup of U of order64.

### 8.1 A rank-one quadratic detector in R

If R cap P had codimension at most1 in R, either it would be all R or the kernel of a nonzero linear functional lambda on Sym3. For v in F2^3,

    lambda(vv^T)

is a polynomial of degree at most2 with zero constant term. Sum its values in F2 over ALL v symbolically: each degree<=2 monomial has an unused binary coordinate and occurs an even number of times, so the sum is0. Its number of zeros is therefore even;0 is a zero, so there is another nonzero zero. Then vv^T gives the actual transvection u(vv^T)=T_(sum v_i e_i) in P, contradiction.

Thus [R:R cap P]>=4. But [R:R cap P]<=[U:P]<=4, so equality holds throughout and [U:P]=4. This is an exact polynomial parity proof, not executed vector enumeration or a trial quadratic instance.

### 8.2 The two DIFFERENT V4 images in ONE D8

By(3), L1 lies in gamma2(U) and is not in P, so theta(U) is nonabelian. Its order is8 and it is the transitive D8 subgroup of S4. Theta(P) is a point stabilizer of order2, a noncentral reflection.

The image theta(R) is normal elementary abelian, and R acts transitively on the four cosets because [R:R cap P]=4. Consequently theta(R) is a REGULAR V4, with theta(R) cap theta(P)=1. Let z be the nontrivial centre/derived element of D8. The image of L1 is z, while theta(X12)=1 by(3). Since C12=X12 L1, its image is z. Therefore theta(D(A12)) does NOT centralize theta(R), and lies OUTSIDE this first V4.

Define the ACTUAL point subgroup

    Q=<D(A12),D(A13),X12,X13,L1>.

These five independent involutions commute by direct matrix conjugation, so Q is elementary abelian of order32. Its image contains z and the outside reflection theta(D(A12)); hence theta(Q) is the OTHER V4 of the SAME D8. Every reflection outside the first V4 lies in this second V4, so theta(P)<=theta(Q). Because ker theta<=P,

    [Q:Q cap P] = [theta(Q):theta(Q) cap theta(P)] = 2.

Thus the ACTUAL X=Q cap P has order16, lies in H, and contains no transvection. No unrelated plane radical, separately selected X, approximate size, changed H or independently conjugated eight-family has been substituted.

### 8.3 Q is EXACTLY O2 of the NONZERO-vector stabilizer

Let e=e1, f=f1, and W0=<e2,e3,f2,f3>. The stabilizer J=Stab_G(e) acts onto Sp(W0) on eperp/<e>, with a splitting fixing e,f. Its kernel consists of the maps

    n(w,t)e=e,
    n(w,t)z=z+B(w,z)e  (z in W0),
    n(w,t)f=f+w+t e,   w in W0,t in F2.

They preserve B directly and have law

    n(w,t)n(w',t')=n(w+w',t+t'+B(w,w')).

In F2 this group is abelian and every element squares1 because B is alternating. It has order2^5=32. The displayed five generators of Q lie in this kernel and are independent, so Q is exactly this kernel, not just an unverified point-stabilizer subgroup.

Sp(W0)=Sp4(2) has O2=1: a finite normal2-subgroup fixes a nonzero vector by orbit counting on the even-size F2^4 (the fixed-point count is even and includes0); its fixed subspace is nonzero and Sp4-invariant. Natural Sp4 is irreducible, since its transvections act transitively on nonzero vectors, so the fixed subspace is all W0. Faithfulness makes that normal2-subgroup trivial. Therefore O2(J)=Q.

The input to Parker is now fully reconstructed: nonzero VECTOR e, X<=O2(Stab(e)), |X|=16=2^(2*3-2), NO transvection, H irreducible, q2,n3. In particular q=n=2 is FALSE here, so no exceptional Alt6/GammaL2(4) alternative is available.

### 8.4 Exact classical import and newly checked application

Theorem1.1 of Parker–Rowley2002 then says H acts naturally as Sp6, Omega6+/Omega6- or O6+/O6-. Proper H excludes Sp6. The natural orthogonal alternatives preserve a quadratic with the given polar B and lie in its O(q). Thus(11) also holds in the transvection-free case.

This is the ONLY new special classical import in Theorem B. The actual original saved rasters `parker-rowley-original-view-1-v1.png` and `...view-2-v1.png` were visually re-read AFTER the qualified prospective primary release, covering the full Theorem1.1 statement across printed85/86 and every listed alternative, not just an abstract/hash. The bound29LF source boundary b36e71f65856278caae8598bdf17fa6f48f9c83601dacbc6b576586214e280b0 was also completely re-read. Its old sentence “our intended use ONLYq4,n2” describes that OLD application, not a restriction in the original theorem; the present q2,n3 application is NEW and needs its own entire gate.

Parker's original proof uses the NAMED Smith1982 generation lemma and McLaughlin1969/Suzuki/module ancestry; those proofs remain NOT_RECONSTRUCTED. The1969 body is CAPTCHA-blocked/unread, no bypass. The already read complete Parker article is not an independent formalization/full-DAG proof of its theorem. Do not call Theorem B import-free or inherit the old q4,n2 gate without rechecking these new X/hypotheses.

## 9. Rank3 reducible sources and the full eight-coset contradiction

For a proper H with a<=2, a nondegenerate invariant2r-space would give2-index valuation2r(3-r)>=4>2. Otherwise its actual invariant radical is nonzero/isotropic, giving a parabolic of dimension r1,2 or3. Their exact indices from isotropic-basis counting are

    J_(3,1)=63,
    J_(3,2)=15*63/3=315,
    J_(3,3)=3*15*63/(3*7)=135.

The pairwise gcds of these three type indices are63,9,45, ALL greater than7. Thus ANY TWO reducible low2-index original sources already have full-index gcd>7, even if their parabolic dimensions differ.

If eight disjoint original cosets had all pairwise gcds<=7, at least SEVEN original indices would have2-valuation<=2. Each corresponding subgroup is proper. By§§7–8, an irreducible one has index divisible by28 or36; by the preceding paragraph a reducible one belongs to the parabolic class. At most ONE source can belong to each of these THREE categories: two28-divisible indices share28; two36-divisible share36; two reducible indices share at least9. Assign any overlap to either legitimate category. Seven objects cannot fit into three singleton-capacity categories. This proves Theorem B.

For BOTH A and B, full preimages under Sp->PSp preserve left-coset disjointness and EVERY original index exactly. Applying the Sp statements proves the PSp versions without a source-saturation assumption or a general normal-extension theorem.

## 10. Full symplectic composition and the unchanged unrestricted problem

The previously accepted binary m>=5 theorem, binary m2/S6 base, and all q>2 symplectic families keep their original exact statements/imports. If BOTH new Theorems A/B pass a fresh ENTIRE mathematics AND dependency/application gate, their parameter union would cover

    ALL Sp_(2m)(q), PSp_(2m)(q), ALL m>=2, ALL finite q.

That is a CANDIDATE composition at the UNION of the older McLaughlin1967/Parker2002/SUN4 imports and this new rank3 Parker application, NOT automatic adoption by this manuscript. The only NEW special import is Parker1.1 at q2,n3; the rank4 theorem and its five-circuit module proof are elementary. Rank1 remains the separate SL2/A1 theorem. An editorial old binary-base section-reference MINOR and all ancestry/source histories remain.

Original arbitrary-group Sun8 is still NOT_PROVED. Other Lie types, higher GL/PGL/semilinear or nonsimple/exotic-central/normal extensions, remaining alternating/symmetric degrees, infinite/common-core reductions and the ACTUAL mixed-alpha/private-source fibre/enlargement barrier remain. The entire older kernel/section644/M1 class-AT-MOST2/abelian-exponent4 alternative, actual high-source136, uniform-private/two-source/least-GROUP-ORDER-versus-private-SUM125/99/63 and EA8 C/O/E/all-hidden-neighbour source leads retain their exact scopes and are not erased by a symplectic result. No unrestricted reduction, globalSun7/R8/t-bound or eight-coset counterexample is supplied.

## 11. Permanent process, timing and assurance

The held m3/m4 leads were already exposed in081. Their elaboration after v117 receipt THROUGH081 composition violated the primary pause and remains a distinct permanent MAJOR; earlier STOPNOW/saving-only clean-stop implications were withdrawn by qualified ACK and parentv26. This manuscript is conventional SOURCE/proof work AFTER actual v117 review RETURN, the separate whole qualified ACK eabc459d6ad87c3084d6e8aae98bfdd85d2969699681a4ac0f627da94d1fb9ba WRITTEN+SENT, and explicit parentv33 future-only release. No false post-ACK discovery/preregistration or retroactive cure is claimed.

The TWO late historical Shor-v112 findings (no-numeric-scout scope and delayed-disclosure/continued-review control) remain under parentv31: the ENTIRE withdrawn trial and every consuming guide receive ZERO credit and are not repeated, rerun or back-converted. They are not premises of this independent binary group argument. The new post-return/pre-ACK rehearsal-order MAJOR underv33 remains separately, as do OWN05733m10s cadence,047 metadata-poll,078 premature primary park, COUNT(actual38 not46), M1 and every parent/owner/reviewer v9/v10/v11/v17–v23/v26/v31/v33 finding. Correct mathematics is not a process-clean count or historical repair.

All finite algebra/counts above are WRITTEN exact symbolic/F2/integer identities, not machine-checked, formally kernel-checked or enumerated. The only tools were static source/raster reads, metadata hashes/LF counts and actual clocks. No scientific interpreter/calculator/Eval/program/CAS/enumeration/solver/replay/build/test/CLI/nested agent/GO, dead-kernel restart, author/shared/frozen edit, git, deletion or publication. No formal/human/configured-family/kernel/executable/triple/priority/novelty/SOTA gate, exhaustive cognition/runtime census, new owner/deadline, round closeout or early final park. Same18 original owners, science cutoff2026-10-27T11:05:38-07:00 and delivery12:35:38; primary continues on the original unrestricted gap after this parkable full packet.
