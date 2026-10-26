# Small-index actual enlargement collisions in P7 — candidate v1

MathSun8, retained math-6 / unrestricted Sun8. Actual clock observed before writing: **2026-10-24T04:11:35-0700 PDT**, from `/bin/date`; not an inferred exact creation time. **CANDIDATE / PARTIAL / NOVELTY_UNCLEAR**, requiring its own separate reconstruction and parent disposition. No scientific executable, interpreter arithmetic, enumeration, solver, compilation, old runtime, external-model CLI or nested agent ran.

## 1. Exact continuation, unchanged target and imports

The global target remains the book's unrestricted eight-disjoint-LEFT-coset statement in `selection-v1.md`; no group, valuation, private-cofactor or overgroup-existence restriction is silently added. The supported reduction leaves actual P7 in an unrestricted finite nonabelian simple group S. The present lemmas work in ANY finite group G possessing actual P7:

    eight pairwise disjoint LEFT cosets g_j U_j,
    [G:U_j]=7r_j,       gcd(r_j,r_k)=1 for j!=k.

Every r_j is unrestricted, including one possible arbitrary private7-power. The lemmas are conditional statements about an ACTUAL supplied overgroup of one vertex. They do not assert that such an overgroup exists in every P7 witness.

The preceding supported mechanism is `simple-group-enlargement-v1.md`, SHA256 `203755a0c2a6a290dc49cb73a79995bb31f706305f5dd4073f1e9fc8375e0702`, read with `institute/runs/three-area-2026-10-23-96h/sun8-actual-enlargement-parent-v1.md`, SHA256 `90889a2920c208da0b99c26ae6c72277019d42e1611a5d8cae9f64e2822ed1de`. That parent supports EL/MIN-EL and the precisely classical-mu-relative maximal-vertex corollary, not Sun8. EL permits collision-free actual enlargement when its index is coprime to210. Here the next obstruction is attacked at actual enlargement indices2 and3; both are excluded from EL's sufficient condition. The new result bounds the NUMBER of genuine collisions, rather than calling an index factor a realizable overgroup.

### Separate exact classical inputs

The only non-elementary imports for the NEW lemmas are Sun3 and Sun4 at their literal published statements:

> For k=3 or4, every family of k pairwise disjoint left cosets of finite-index subgroups of any group has a pair of subgroup indices with gcd at least k.

Primary source freshly read: Wan-Jie Zhu, *On Sun's Conjecture concerning Disjoint Cosets*, International Journal of Modern Mathematics3(2008),197–206, [arXiv:0807.2207v1, Theorem1.1](https://arxiv.org/html/0807.2207v1#S1.Thmtheorem1). The literal theorem, left-coset definitions, introduction and coprime-index Lemma2.1(iii)–(iv) were read from the primary HTML, including mathematical annotations. The theorem is imported as a classical result, not re-proved or kernel-checked here. Its k=3 part is used below for actual subgroup fibres; its k=4 part is used only for the index-two collision bound. The baseline selection already declared these as separate classical imports.

The NEW lemmas do not consume the internal Sun7 proof, G4/F7, a transitive-group database, mu(S)<=2 or CFSG. Mapping an arbitrary original Sun8 counterexample into the current finite simple P7 residual still retains the earlier literal internal-Sun7/reduction trust boundary. No new openness or novelty certificate follows from rereading Zhu.

## 2. Common actual-intersection setup

Fix i and an ACTUAL overgroup

    U_i < M <= G,        [G:M]=7s,
    a=[M:U_i],          r_i=a s.

Normalize by multiplying ALL original left cosets on the left by g_i^-1. The selected coset is now U_i and its enlargement is M; write all other selected cosets as a_j U_j. Define the genuine collision set

    J={j!=i : M intersects a_j U_j}.

Thus J counts whole original cosets whose intersections become newly possible on replacing U_i by M, not abstract index pairs. For j in J choose x_j in M intersect a_j U_j and put W_j=M intersect U_j. Then

    M intersect a_j U_j = x_j W_j,

and these intersection cosets are pairwise disjoint, because the original eight cosets are. They also avoid U_i.

For every such j, gcd(s,r_j)=1. Index divisibility and the finite product-set formula give

    [G:W_j]=7s r_j alpha_j,
    |M U_j|/|G|=alpha_j/7 <=1,
    1<=alpha_j<=7,
    [M:W_j]=r_j alpha_j.                         (A)

Here M U_j is only a SET; no product-subgroup or commutativity assumption is made. The integer alpha_j can introduce extra small primes, so it cannot be deleted arithmetically.

One elementary fact used repeatedly is: coprime subgroup indices force every pair of the corresponding left cosets to meet. In a finite ambient group, the intersection index is a multiple of their index product and at most that product, so equality holds and the subgroup product is the whole group. Consequently actual disjoint subgroup cosets cannot have coprime indices.

## 3. Index-two enlargement: at most three genuine collisions

**Theorem C2.** If a=2, then |J|<=3. All intersections lie in the OTHER U_i-coset of M. If |J|=3, translating that other coset to U_i produces an actual three-disjoint-left-coset configuration in U_i with all three pairwise index gcds exactly3, hence indices3t_j with pairwise coprime t_j.

### 3.1 The intersections lie in one actual fibre

Index2 forces U_i normal in M; no normality in G is inferred. Let pi:M->M/U_i=C2. Since x_j W_j avoids U_i, its projected coset cannot contain the identity. If pi(W_j)=C2, that projected coset would be all C2 and would contain the identity. Therefore W_j<=U_i and x_j lies outside U_i.

Choose ONE t in M outside U_i. All intersection cosets x_j W_j lie inside the same left coset tU_i. Translating by t^-1 gives pairwise disjoint actual left cosets

    y_j W_j in U_i,       y_j=t^-1 x_j in U_i.     (B)

Because r_i=2s, every other private r_j is odd. From (A), [M:W_j] is even and alpha_j must be2,4 or6. Write alpha_j=2 beta_j. The actual indices in U_i are

    b_j=[U_i:W_j]=r_j beta_j,
    beta_j in{1,2,3}.                             (C)

### 3.2 Every local pair gcd is at most3

The private r_j are pairwise coprime and odd. If two beta values coincide, their b-index gcd is that common value. With distinct beta values, {1,2} gives coprime indices. For {1,3} or {2,3}, the gcd divides3: the only possible cross-prime is3, and the index on the beta=3 side is odd, so2 cannot also occur. Therefore

    gcd(b_j,b_k) in{1,2,3} for all distinct j,k.   (D)

This is about the actual cosets (B), not a realizability assumption for an invented pattern. If four members of J existed, four of (B) would violate the literal Sun4 theorem, because all their pairwise gcds are at most3. Thus |J|<=3.

### 3.3 Equality forces an actual P3 triple, not a contradiction

If |J|=3, no pair gcd in (D) can be1 by the elementary coprime-index lemma. Sun3 supplies a gcd3 pair, say gcd(b_1,b_2)=3. If gcd(b_1,b_3)=2, then3 does not divide b_3, so gcd(b_2,b_3), which is at least2 and at most3, must be2. Both b_1,b_2 would then be even, making their gcd divisible by6, contradiction. Thus gcd(b_1,b_3)=3, and symmetrically gcd(b_2,b_3)=3.

Hence every b_j is3t_j and gcd(t_j,t_k)=1. Together with the actual cosets (B), this is a genuine P3 configuration INSIDE U_i. It is allowed at the sharp three-coset threshold, not a three-coset counterexample, and it does not construct or contradict the original eight-coset P7 configuration. QED C2.

In particular at least FOUR of the other seven original cosets remain disjoint from the enlarged g_i M. This is a count of actual preserved cosets, not permission to drop the up-to-three damaged vertices from Sun8.

## 4. Index-three enlargement: at most four genuine collisions

**Theorem C3.** If a=3, then |J|<=4, with no normality assumption on U_i in M. The proof treats both actual faithful degree-three quotients, including the nonnormal S3 branch and its possible private-even cofactor.

### 4.1 Actual degree-three action and fibre indices

Let N=core_M(U_i), pi:M->K be the faithful image of the action on M/U_i, and H=pi(U_i). Thus U_i=pi^-1(H), [K:H]=3, and K is a transitive subgroup of S3. Elementary order divisibility gives K=C3 or S3; no classification table is used.

For j in J put J_j=pi(W_j), d_j=[K:J_j], and X_j=pi(x_j) J_j. Since x_j W_j avoids pi^-1(H), its projected coset X_j avoids H. If d_j were coprime to3, the coprime-index lemma inside K would force X_j to meet H, contradiction. Therefore

    3 divides d_j,       d_j is3 or6,

with d_j=3 in the C3 branch. As 3 does not divide any other r_j and d_j divides r_j alpha_j, (A) gives

    alpha_j in{3,6},
    b_j=[N:N intersect W_j]=r_j alpha_j/d_j.       (E)

For every q in X_j, the nonempty intersection of x_j W_j with the fibre pi^-1(q), translated into N using ONE fixed representative of q, is an actual left coset of N intersect W_j in N, of index b_j. All such cosets at a common q are pairwise disjoint. This follows from the ordinary common-point intersection formula; it does not replace the global cosets by an arbitrary capacity pattern.

### 4.2 Normal branch K=C3

Here U_i=N, H is the identity, and the projected sets X_j are single points in the two-point complement K outside H. Equation(E) gives b_j=r_j beta_j with beta_j in{1,2}. The r_j are pairwise coprime; at most one is even. Consequently every pair gcd of these b-indices is at most2, including the possible even private cofactor.

Three colliders through one quotient point would give three actual disjoint cosets in N with all pair gcds at most2, violating Sun3. Thus at most two occur at each of the two points and |J|<=4.

### 4.3 Nonnormal branch K=S3: the private-even exception is retained

Now H has order2 and the complement Omega=K outside H has FOUR points. The projected coset X_j has cardinality6/d_j, namely2 or1.

Call j regular if r_j is odd. At most ONE member e of J is not regular, since the private r_j are pairwise coprime. Because regular r_j is coprime to6, d_j divides alpha_j, so

    b_j=r_j beta_j,       beta_j in{1,2}.

For a regular beta_j=2, necessarily alpha_j=6 and d_j=3, so |X_j|=2. For regular beta_j=1, |X_j| is1 or2.

If the private-even e exists, retain it rather than treating d_e as a divisor of alpha_e without justification. Equation(E) permits exactly

    b_e in{r_e/2, r_e, 2r_e},

where the actually occurring value is an integer. This is an ACTUAL quotient/fibre factorization, not arithmetic deletion from a global index. It follows that every regular beta=1 index r_j is coprime to b_e, and every regular beta=2 index2r_j has gcd at most2 with b_e. The same coprimality/at-most2 assertions hold among the regular indices of the corresponding types.

**Exclusive-point property.** If q belongs to X_j for a regular beta_j=1, no other X_k can contain q: their actual fibre cosets in N would have coprime indices. Thus this j occupies every point of X_j exclusively.

**Two-per-point property for the rest.** At a point not occupied by a regular beta=1 collider, all present colliders are regular beta=2 members, possibly together with the single e. Their actual fibre indices have all pair gcds at most2. Sun3 in N therefore permits at most two present colliders.

Charge weight2 per occupied point to each regular beta=1 collider, and weight1 per occupied point to every other collider, including e. The two properties show that the total charge at EACH point of Omega is at most2. Summing over its four actual points gives total charge at most8.

Every regular beta=1 collider contributes at least2, since X_j is nonempty. Every regular beta=2 collider contributes exactly2, since |X_j|=2. The possible exceptional e contributes at least1. Therefore, with m=|J|,

    2m<=8 if no e occurs;
    2m-1<=8 if e occurs.

In either case integrality gives m<=4. This proves the S3 branch without assuming regularity of every private cofactor, normality of U_i, or an unproved symmetry restriction. Together with the C3 branch this proves C3.

Thus at least THREE of the other seven original cosets remain disjoint from the actual index-three enlargement.

## 5. Exact consequence in a minimum-index simple P7 witness

Relative to the previously supported reduction, choose an actual P7 witness in fixed finite simple S minimizing sum_j r_j, as in MIN-EL. If an actual seven-retaining overgroup M of a vertex has [M:U_i]=2 or3, its collision set J cannot be empty: otherwise replacing g_i U_i by g_i M would preserve ALL eight disjoint cosets and P7 while decreasing r_i to s. Consequently

    1<=|J|<=3 for an actual index-two enlargement;
    1<=|J|<=4 for an actual index-three enlargement.

This uses the actual minimal witness, not assumed existence of the relevant overgroups. In the index-two equality case the three genuine collisions contain the specified actual P3 triple in U_i. These statements refine the small-multiplier obstruction in EL; they do NOT turn a damaged enlargement into a legal P7 replacement.

## 6. Honest remaining bridge and review boundary

The unrestricted simple-P7 residual remains unresolved. The new bounds leave potentially nonempty collision sets; their intersections have not been removed while preserving every original coset. The actual P3 triple in the index-two equality case is not forbidden by Sun3, and the degree-three quotient/fibre capacities can likewise be nonempty. No local pattern has been claimed to lift to an eight-coset counterexample.

The exact missing group-geometric input is a source-preserving elimination or rearrangement theorem for these remaining actual intersection cosets, together with the still-uncontrolled primitive/maximal vertices and enlargement indices involving5,7 or other small-prime mixtures. Dividing indices by2 or3 without their ACTUAL overgroup/action/fibre data, deleting the damaged original vertices, or applying a coprime-index theorem to7r_j would not supply that input.

This candidate therefore gives two completed, explicitly classical-Sun3/4-relative lemmas about real eight-coset geometry and one precise continuing barrier. It asserts neither universal existence of the small-index overgroups nor a restriction of the global target to them. There is no Sun8 proof, genuine Sun8 counterexample, novelty/publication claim, formal/kernel proof, human/cross-vendor verdict or scientific execution. Old snapshots and parent scopes remain unchanged; this new source has not yet received its own separate reconstruction or parent acceptance.
