# Rank-two completion — intrinsic signed-set classification and the coupled forcing interface

Owner InfoBalancedNL242, info-6. Actual clock before this successor: `Sun Oct 25 07:26:40 PDT 2026`.

**NEW WRITTEN CANDIDATE RESULTS; no scientific computation.** No eval/interpreter, arithmetic/enumeration program, symbolic program, certificate replay or solver was used. Source/metadata tools and written reasoning only. No GO exists. New results below have not received independent reconstruction. No formal, human, cross-model or novelty acceptance is claimed.

This is one consolidated primary-only successor, not another Gold example. It develops restrictions applying to EVERY surviving L16 signed set, an exact code/projection classification interface, an exact conditional graph-S formulation, and a uniform integer forcing equation that keeps the prescribed-XOR half-design and both Boolean transforms. It does **not** establish the requested covers-all slice theorem or an outside class with a completed R witness. The exact missing bridges are isolated in §8; all three entire cases and U2 remain open.

## 1. Accepted base and retained full-target interface

The operative parent support is `institute/runs/three-area-2026-10-23-96h/nl242-rigidity-E116-parent-v1.md`, its receipt and mandatory receipt-addendum-1. The latter preserves the parent's coverage sequencing correction; later complete reading is not backdated. The author has now read the full265-line actual serial review `mathematics/evidence/three-area-20261023-96h/parallel-18/shor-completion/peer-review-nl242-global-rigidity-E116-v1.md`, pinned by that receipt at SHA-256 `5f2880a45bb143e17138eaaf401f888dcdf93745081ec1861c6fee2c92933bcc`. Parent v8 was consumed. Its and all earlier admission qualifications remain binding.

Load-bearing accepted author source: `rank2-completion-consolidated-v2.md`, SHA-256 `82dbda5c851b99c7e6c855d861bdc374ce0b3d3713fd8b41a41310dd78a91fa2`. Its exact older normal-form/pruning imports remain imports, not newly re-certified here. It supports:

- every surviving full target has E empty and necessary (L,u)=(16,24),(16,32),(20,24);
- for every such S array, Hdelta is divisible by4;
- at L16, Hdelta takes0,±4,±8 with absolute counts120,96,40, and the exact signed-triple equivalence;
- at L20, n12+2n16+2n20=8;
- E118/E116 exclude the specified XOR-zero/full-affine-rank slice classes and both explicit Gold profiles, **not every L16 support or q placement**.

All prior files are immutable. Unadmitted eval outputs and tables are not proof inputs.

Use G=F2^8, H²=256I, W a six-space, D=1−1_W, chi=1−2D, U=W-perp and q=2e0−1_U. Put

    h=Hdelta, b=phi(h), C=Hb,
    B=phi(q−b)=q−b  (E empty), T={B=0}.

S says C=4delta on A=supp(delta), |C|=12 off A. A completion is a ternary a supported EXACTLY on T, with a=±1 there, such that

    p=Ha/4 in {0,±2} on W and {±1,±3} off W,
    p(0)=0.                                         (1)

Set beta=phi(p). Hp=64a makes a=phi(Hbeta); a²+B²=1 gives the exact original N and both Boolean signs B+a,B−a. The complete512-bit map remains

    F(x,0)=(1−B−a)/2, F(x,1)=(1+B−a)/2,             (2)

with weight256 and ALL Walsh sectors8p and2HB.

Equivalently choose V subset T, a=1−2*1_V on T, and impose

    |V|=|T|/2,
    XOR(V)_i=|T intersect H_ei|/2+D(e_i) mod2,
    ||V intersect H_v|−|T intersect H_v|/2|<=3
                                      for EVERY v. (3)

The moment identities of the actual T make these integral and exactly equivalent, not a scalar relaxation. Every constraint below concerns this SAME delta,T,V,p; no independent spectrum/stream choice is introduced.

## 2. A universal hyperplane obstruction, not a Gold assumption

**Theorem H2.** Every full-affine-rank L16 S support A meets every affine hyperplane in4,6,8,10 or12 points. In particular a2/14 split is impossible.

The accepted XOR(A)=0 makes every hyperplane intersection even. Full affine rank excludes0/16. It remains to exclude2. Affine changes preserve the S identities, so place the two-point side at r=1 in G=F2 x F2^7. Write delta_1=epsilon_1 e_t1+epsilon_2 e_t2 and let h_0,h_1 be the seven-variable transforms of the two delta slices. Then

    h(s,y)=h_0(y)+(−1)^s h_1(y).

The pair transform h_1 is0 off an affine hyperplane Y of64 points, and on Y it equals2epsilon_1 chi_t1(y). Because both full h entries lie in0,±4,±8, where h_1=+2 the only possible h_0 values are−6,−2,2,6. Direct phi subtraction gives

    phi(h_0+2)−phi(h_0−2)=−2,1,1,−2,

respectively; the h_1=−2 case reverses the sign. Hence

    Q(y)=phi(h_0+h_1)−phi(h_0−h_1)
       =epsilon_1 chi_t1(y)(1−3e(y)) on Y,
       =0 off Y,                                    (4)

where e is a0/1 function. Its seven-variable Walsh transform is the r=1 slice of C. That slice has two entries4epsilon_i and126 entries of magnitude12. Parseval therefore gives

    128 sum Q²=2*16+126*144,
    sum Q²=142,
    64+3|supp e|=142,
    |supp e|=26.

But evaluating HQ at the ACTUAL t1 gives epsilon_1(64−3*26)=−14epsilon_1, whereas S requires4epsilon_1. Contradiction. The complementary14 split is excluded by the same argument.

This is a globally applicable exact obstruction on all intrinsic L16 supports. It does not by itself supply a slice covering theorem.

### Coding interpretation and the missing projection bridge

Let C_A be the binary code of evaluations on the16 distinct points of A of all affine functions on F2^8. Its dimension is9 by full affine rank. It contains the all-ones word; Theorem H2 gives minimum distance at least4, and all weights are even. This conclusion applies to every surviving L16 A, independently of its signs or a graph parametrization.

A four-bit linear projection is bijective on A iff C_A contains a five-dimensional affine-Hadamard subcode: one containing constants and with every nonconstant word of weight8. One direction is evaluation of the four projected bits. Conversely, choose four independent nonconstant functions in such a subcode. The sixteen evaluation tuples have every nontrivial character sum0; Fourier inversion makes every four-bit tuple occur exactly once. Their linear parts therefore give a graph projection of A.

The existence of that subcode has NOT been proved here. Moreover an excluded-slice argument needs a projection compatible with the actual U, not merely some graph projection: its four linear coordinate forms must contain U so the q correction stays in the appropriate single fiber. Neither bridge is supplied by the distance bound alone.

## 3. Cubic phase and a universal collision-power dichotomy

For L16 write

    C/4=zeta=delta+3eta,

where eta is0 on A and±1 off A. The Boolean sign

    tau=eta−delta                                   (5)

is intrinsic, not a selected Gold sign. Put j=(zeta−1)/2. H j is divisible by32 because H zeta=64b; the integer divisibility/face-parity lemma gives degree(j modulo2)<=3. Pointwise (−1)^j=delta−eta=−tau. Thus tau is a cubic-or-lower Boolean sign.

Its transform is

    Htau=(64b−4h)/3,

so at h=±4 it is four times h, and at h=±8 it is minus four times h. Consequently

    (Htau)²=16h²,
    AC_tau(w)=sum_x tau(x)tau(x+w)
             =16(delta star delta)(w).              (6)

The signs in this identity matter: Heta=(64b−h)/3. No sign reversal from an independently chosen off-support triple sign is used.

For w!=0, the derivative of a cubic Boolean phase is quadratic and invariant under translation by w. Its polar rank is at most6. Its exponential sum is therefore0 or±32,±64,±128,±256, by the elementary quadratic-sum formula. If |delta star delta(w)|=16, Cauchy equality makes delta(x+w)=±delta(x), forcing h to have support in a128-point character hyperplane, contradicting its136 nonzeros. Hence the following **universal collision obstruction** holds:

    (delta star delta)(w) in {0,±2,±4,±8}, w!=0.      (7)

In particular magnitude6,10,12,14 or16 at any nonzero shift is impossible for EVERY intrinsic L16 S candidate.

The accepted h counts give

    sum_(w!=0) (delta star delta)(w)²=480.            (8)

If only0,±2 occur, there are exactly120 nonzero shifts. Each requires an unordered pair of A, and A has exactly120 unordered pairs. Thus every pair difference is unique: A is Sidon. Conversely a Sidon A has only0,±2 correlations. Therefore the classification splits exactly into:

- a signed Sidon branch;
- a collision branch with at least one magnitude4 or8 correlation, corresponding by(6) to a cubic derivative bias64 or128.

Cancellation of signs means this is NOT a proof that the collision branch is empty.

In the Sidon branch A is maximal: the signed triple identity is nonzero at every point outside A, so every such point is a sum of three distinct A points and cannot be added. Two different such triples cannot share a point. At most five can occur for a fixed outside point; five would use15 A points, and XOR(A)=0 would make their common sum equal the leftover A point, a contradiction. Their signed sum is±1, so their number is odd. Thus each outside point has exactly one or three triples. This is still not an affine-equivalence classification of all such maximal Sidon sets.

## 4. A full-spectrum zero-set fact, with a symbolic placement consequence

Let Z={h=0}, of size120. It is not contained in any affine hyperplane. Indeed, if Z lay in chi_w=epsilon, that128-point band would have only eight nonzero h sites and squared h-energy at most8*64=512. But Fourier inversion and(7) give its exact energy

    [4096+epsilon*256(delta star delta)(w)]/2>=1024,

a contradiction.

In fact

    Z+Z+Z=G.                                        (9)

Here is an elementary proof, not an imported additive-combinatorics classification. If v were missing, R=Z+v would be a sum-free120-set. For r in R, R+r lies in its136-point complement. For d=r1+r2 in R+R,

    |R intersect(R+d)|>=120+120−136=104.

Thus its symmetric difference under such a shift is at most32. For d,e in R+R the triangle inequality makes overlap under d+e at least88>0, so R+R is closed under addition. Its size lies between120 and136, hence it is a128-point subgroup. R lies in a coset of it; translating back would put Z in an affine hyperplane, already excluded. This proves(9).

Consequently, for EVERY actual signed S array and EVERY v with |h(v)|=4, one can choose three distinct zeros z1,z2,z3 with z1+z2+z3=v. These four points form an affine two-plane with exactly one nonzero h entry. Modulating delta by chi_v and a common sign moves that entry to0 with b(0)=q(0)=1. Taking U to be the translated two-plane gives E empty, alpha1 and the actual S-side count data n=118.

This is a symbolic S/q-placement family with existence proved from the whole signed-set structure, not from an evaluated example. Its four signed support sums across the U-annihilator cosets have magnitude1, because Hdelta|U has only the entry±4. Therefore all four unsigned support occupancies are ODD. In particular this family has no U-compatible bijective four-bit graph projection, which would put exactly four A points in each such coset.

**Limit:** this proves a genuine obstruction to that graph-cover route, not that these placements evade every possible E118 structural test. No R-completable member is supplied. The coupled attempt for these actual placements is the rank-one integer system in the next section; it is not a magnitude-only construction or an NL242 witness.

## 5. Exact coupled R forcing for ALL S arrays

All formulas here use the same actual half-subset V from(3); a(x)=1−2*1_V(x) on T, p=Ha/4. Fourier multiplication gives the exact integer identity

    delta star p=(1/4)H(h*a),                        (10)

where h*a on the right is POINTWISE multiplication. This retains both Boolean transforms through the support/norm condition, the zero p(0), every XOR/slab constraint and all512 coefficients in(2).

### L16, alpha0: (16,32)

b is0 on all U; outside U, a is nonzero exactly at h=0. Thus h*a=0 everywhere, and EVERY full completion must satisfy

    delta star p=0 at ALL256 points.                 (11)

This is an integer annihilator condition, not only a modulo3 congruence. It is uniform over every intrinsic signed16-point S support, with no Gold or graph assumption.

### L16, alpha1: (16,24)

There is one actual v in U with b(v)=q(v), all other b|U=0. The product h*a is supported exactly at v. Hence

    delta star p=kappa*chi_v,
    kappa=h(v)a(v)/4 in {±1,±2}.                    (12)

The sign is NOT chosen independently: a(v)=1−2*1_V(v), with that v in the SAME T and half-subset. The |h(v)|=4 placements of §4 force kappa=±1. Any coupled attempt for that symbolic outside-graph family must meet all256 exact equations(12), the prescribed-XOR slabs(3), and the original norm/support. None has been solved here.

### L20, alpha0: (20,24)

The only h nonzeros with b=0 have magnitude12. Let X12={x:|h(x)|=12}. On U, a=0. Therefore h*a=12e, with

    e(x)=h(x)a(x)/12 on X12 outside U, and0 elsewhere.

This is a signed array on the ACTUAL exceptional sites, not independent data. Since |X12|<=8 by the accepted budget,

    delta star p=3H e,
    H(delta star p)=768e,                            (13)

with at most eight Fourier modes. Signs and membership follow the same V. This gives the sparse exceptional-site completion interface for the ENTIRE L20 case, not a new selected profile.

Equations(11)–(13) are exact global restrictions. They do not by themselves prove nonexistence: forgetting the ternary/norm/support condition on Ha or the XOR/slabs would turn them into a larger relaxation, which is not authorized.

## 6. Conditional graph classification beyond the quadratic Gold assumption

This section applies to EVERY intrinsic S array that has a four-bit graph projection; it does not assume the projection bridge from §2. Write A={(t,F(t)):t in F2^4}, delta(t,F(t))=epsilon(t). Then

    h(a,L)=H4[psi_L](a), psi_L(t)=epsilon(t)(−1)^(L dot F(t)).

Every component has spectrum0,±4,±8. Its Boolean exponent has degree at most3 (divide the sign spectrum by2 to apply the four-variable parity-degree bound). All quartic terms are absent.

There are exactly three analytic component types:

- quadratic rank4: sixteen coefficients4, no zeros;
- quadratic rank2: four coefficients8, twelve zeros;
- cubic: eight coefficients4, two coefficients8, six zeros.

For the last assertion, a nonzero cubic3-form in four variables can be put in x1x2x3 form. Write its phase as x1x2x3+Q(x1,x2,x3)+x4*ell(x1,x2,x3). If ell were constant the remaining three-variable cubic would produce a coefficient12, forbidden. Otherwise change the first three variables to make ell=x3. Summation in x4 restricts x3 to its frequency bit. The two resulting two-variable phases differ in their x1x2 coefficient, so one is bent and one affine. Their transforms give exactly the stated eight4/two8/six0 pattern. No finite function enumeration is used.

The cubic coefficient vector of the component exponent is affine in L. If r components are cubic, q have rank2 and e have rank4, the120 zero sites give2q+r=20, while q+r+e=16. An affine cubic-vector map has either no zero, or2^(4-k) zeros. These constraints leave only

    (r,q,e)=(0,10,6),(8,6,2),(12,4,0).              (14)

These are NECESSARY component configurations, not realized outside classes. In particular assuming all components quadratic silently deletes two genuine unresolved branches.

### Exact S matrix, not just the component counts

Let g_L(t)=H4_a[phi(h(a,L))](t). In the three cases above,

    g_L(t)=lambda_L(t)*psi_L(t), lambda_L(t) in{4,−2}.

For rank4 lambda is constantly4; for rank2 constantly−2. For a cubic component it is4 on the bent branch and−2 on the affine branch, an actual affine halfspace of t. The cubic formula follows by separating the two8 coefficients from the eight4 coefficients in the preceding normal form: the affine branch is precisely the part whose Walsh amplitude is8.

Define M(t,L)=(lambda_L(t)+2)/6. Then

    C(t,y)=epsilon(t) sum_L (−1)^(L dot(y+F(t))) lambda_L(t).

The full S condition is EXACTLY: for every t, the Boolean function L -> M(t,L) is a bent weight6 function. Indeed graph evaluation requires sum lambda=4, giving row weight6; every off-graph value must have magnitude12, giving H4 M=±2 at nonzero frequencies. Thus1−2M has all Walsh magnitudes4. A four-variable bent function is quadratic (the same cubic normal-form argument would leave one affine two-variable slice and violate flatness).

Therefore M is quadratic in L for every row and affine in t for every column, with the actual component/sign binding above. It cannot be chosen as an independent array of row spectra. This is the exact conditional S classification interface for the mixed branches in(14), not an argument that the two marginal properties alone create an F,epsilon or a Boolean pair.

## 7. Literature boundary, not an unverified classification import

A bounded public search did not supply a usable all-cases code/graph classification. The primary paper Czerwinski–Pott, [Sidon sets, sum-free sets and linear codes, arXiv:2304.07906v3](https://arxiv.org/html/2304.07906v3), Section2 explicitly says that its authors did not classify all maximal Sidon sets in dimensions7 and8; Proposition2.8 gives possible sizes through computer calculations. That source is read for this scope warning only. Its finite tables, enumerations and examples are NOT imported as certificates, not replayed, and not used to claim that every sixteen-point Sidon set is Gold. The Sidon/projection arguments above were proved directly.

## 8. Exact current classification gap and case verdicts

The following are NEW written uniform obstructions/interfaces, not another Gold example:

1. No intrinsic L16 S support has a2/14 hyperplane cut; its affine evaluation code has dimension9 and distance at least4.
2. Its cubic phase forces all nonzero signed pair correlations into0,±2,±4,±8; the first branch is exactly maximal Sidon, while the collision branch must exhibit a4/8 derivative bias.
3. Every R completion obeys the exact annihilator/rank-one/eight-mode forcing(11)–(13), with the SAME half-subset, prescribed XOR, slabs, both inverse signs, balance and512 coefficients.
4. If a graph projection exists, the non-Gold possibilities are not arbitrary spectra: the three component configurations(14) and the row-bent/column-affine bound matrix are exact necessary S data, with their actual phase binding retained.

What is STILL missing is precisely the requested full bridge: prove every admitted signed set and ACTUAL q/U placement falls into an excluded slice class, or give an actual outside class with a completed original R/N half-design. Neither has been obtained. Even a graph projection is unproved in general; U compatibility is a further separate obligation. The symbolic placements in §4 explain why that second obligation cannot simply be assumed.

Thus(16,24),(16,32),(20,24) and U2 all remain OPEN. No literal completed half-design family or full witness is supplied. The next single attack is the intrinsic collision/projection classification with equations(11)–(13) imposed throughout, not an independent-stream or magnitude-only construction. No computation, new GO, independent review, formal proof, novelty clearance, publication or deadline reset is claimed.
