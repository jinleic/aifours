# Actual private-prime coset enlargement in the simple P7 residual — candidate v1

Observed before exclusive creation: **2026-10-23T15:55:29-0700** (actual `/bin/date`). MathSun8, math-6. **CANDIDATE / PARTIAL / NOVELTY_UNCLEAR.** This is the ONE resumed consequential actual-subgroup/coset step requested after the parent normal-section disposition. It is not a bounded group survey, an integer partition argument or a full Sun8 proof. No scientific executable, arithmetic program, enumeration, solver, CLI or nested agent has run.

## 1. Exact live target and authority boundary

The live residual is actual P7 in an unrestricted finite nonabelian simple group S:

    eight pairwise disjoint LEFT cosets g_i U_i,
    [S:U_i]=7r_i,       gcd(r_i,r_j)=1 for i≠j.

The r_i are unrestricted positive integers, with one permitted to carry an arbitrary7-power. No new restriction on them is silently imposed here.

Read operative `institute/runs/three-area-2026-10-23-96h/sun8-normal-section-parent-v1.md`, actual observed SHA256 `8a8480e2d66f0098fc80ae2960bafcdab36a9976e80b671ddee01c5048fec475`. It supports the new normal-section descent and the global Sun8↔simple-P7 existence reduction **conditional on the literal inherited Sun7 theorem**. It is not unrestricted Sun8 acceptance or a fresh parent reproof of all R4/G4/F7 ancestors.

The consolidated source remains `consolidated-chain-v1.md`, SHA256 `72b8988f698c9b5442dd08546fb434e4ef40f342e37806ade8caabdf8deb7d9e`, read with its actual review disposition. The present enlargement lemma itself uses ONLY the actual P7 indices, ordinary finite subgroup/cardinality facts, and the elementary coprime-index left-coset intersection lemma. It imports neither S7 nor G4/F7. Its later maximal-subgroup corollary additionally declares one exact classical simple-group theorem in §5.

## 2. The genuine geometric obstruction to careless enlargement

Enlarging U_i to a subgroup M_i can create intersections between the original disjoint cosets. A divisor of7r_i is not automatically the index of a suitable overgroup. We therefore begin with an ACTUAL given overgroup, not an arithmetic prime deletion.

Fix i and assume

    U_i≤M≤S,       [S:M]=7s,
    a=[M:U_i],     r_i=a s.

Suppose

    gcd(a,210)=1.                                      (E)

Thus every prime of the enlargement index a is greater than7; a=1 is harmless and allowed. Nothing says the full r_i has this property, or that such M exists.

**Enlargement lemma EL.** Under these exact hypotheses, replacing the original coset g_iU_i by the LARGER actual coset g_iM preserves pairwise disjointness from ALL seven other original cosets. The new eight-coset configuration is still P7, with r_i replaced by the actual divisor s.

### Complete proof

Fix j≠i and let W=M∩U_j. Since [S:M]=7s divides7r_i and gcd(r_i,r_j)=1,

    gcd([S:M],[S:U_j])=7,
    lcm([S:M],[S:U_j])=7s r_j.

Write

    [S:W]=7s r_j α,

where α is a positive integer. The finite subgroup-product formula gives

    |M U_j|/|S| = [S:W]/([S:M][S:U_j]) = α/7 ≤1.

Therefore1≤α≤7, and

    [M:W]=r_j α.                                      (F)

No divisibility of [S:W] into the product of the two original indices is asserted; α may introduce additional small primes. That is exactly the feature the argument must control.

Because a divides r_i, it is coprime to r_j. Condition(E) also makes it coprime to every integer α between1 and7. Hence

    gcd([M:U_i],[M:W])=gcd(a,r_j α)=1.                 (G)

Apply the elementary coprime-index lemma INSIDE M: every left U_i-coset in M meets every left W-coset in M.

Suppose, toward a contradiction, that g_iM meets g_jU_j, and choose x in their intersection. Then

    g_iM=xM,       g_jU_j=xU_j,
    g_iM∩g_jU_j=xW.

Write g_i=xm with m∈M. Inside M, (G) makes mU_i meet W. Multiplying by x shows that g_iU_i=xmU_i meets xW, which is contained in g_jU_j. This contradicts the ORIGINAL disjointness.

Thus g_iM is disjoint from each g_jU_j. All eight cosets remain nonempty. The enlarged index7s still has gcd exactly7 with every7r_j, because s divides r_i, so the replacement is genuine P7. QED.

This proof does not assume any subgroup normal, any two products commuting, or any quotient action of degree7. It is actual intersection geometry at x(M∩U_j), not a local index-pattern realization.

## 3. A slightly sharper exact local obstruction

The proof needs only gcd(a,α)=1 for the α attached to that ACTUAL pair(M,U_j). Therefore if an actual enlargement creates a new intersection, its pair must have

    gcd(a,α)>1,       1≤α≤7.                          (H)

In particular some prime from{2,3,5,7} divides both a and that pair's intersection multiplier. This is a necessary obstruction to the actual enlargement, not a sufficient criterion that an intersection exists. Condition(E) is the uniform assumption that rules out all such pair obstructions at once.

The prime7 is retained in210: if a removes a private7-factor, α=7 is not excluded by this argument. The one possible higher7 cofactor is therefore NOT silently treated as absent. Nor can one strip just a large prime from a composite enlargement index containing2/3/5/7 without first constructing an actual intermediate subgroup of the appropriate index.

## 4. Minimal-index actual witnesses have a structural maximality condition

Suppose a fixed finite S supports P7. Among its ACTUAL eight-coset P7 witnesses choose one minimizing

    R=r_1+...+r_8.

The family is nonempty by hypothesis; positive-integer well ordering supplies a minimum. The choice does not bound S, its order or its private primes, and changes no existence question.

**Corollary MIN-EL.** In such a minimum-R witness, no vertex U_i has a strict overgroup M with7|[S:M] and gcd([M:U_i],210)=1.

**Proof.** EL would replace g_iU_i by g_iM, leaving actual P7 but decreasing r_i by the proper factor [M:U_i]>1. This contradicts the definition of R. QED.

Let

    L={i:gcd(r_i,210)=1}.

At most four vertices lie outside L: each of the four primes2,3,5,7 can divide at most one private cofactor, and coincident owners only decrease that number. Thus |L|≥4, without assuming any cofactor missing7. For i∈L, ANY strict7-retaining overgroup M has [M:U_i] dividing r_i and therefore coprime to210. MIN-EL forbids it. Thus every U_i with i∈L is **maximal among proper overgroups retaining a7-divisible ambient index**.

This is not yet the same as being maximal in S: a strict maximal overgroup could have index NOT divisible by7. That gap is treated only with the explicitly imported theorem next.

## 5. A legitimate, limited application of the classical coprime-index bound

Define μ(S) to be the maximum number of proper subgroups of S whose ACTUAL indices in S are pairwise coprime. The exact classical input is:

> For a finite nonabelian simple group S, μ(S)≤2.

Primary source actually read: Dolfi–Guralnick–Praeger–Spiga, *On the maximal number of coprime subdegrees in finite primitive permutation groups*, [arXiv:1203.2728v1](https://arxiv.org/pdf/1203.2728v1), Definition2.1, Remark2.2 and Lemma2.3 with its displayed proof. Lemma2.3 states the stronger bound for a central product of isomorphic quasisimple factors; take one factor S (nonabelian simple implies perfect and centerless). Its proof invokes the earlier simple-product result [10,Lemma5.2]; that original classification-based ancestry is a declared classical theorem trust boundary, NOT re-proved or kernel-replayed here.

This is NOT a direct application to indices7r_i, which are never coprime. We apply it only after constructing actual overgroups with genuinely coprime indices.

**Maximal-vertex corollary MV.** In the minimum-R witness above, at least |L|−2≥2 of the vertices U_i with i∈L are actual maximal subgroups of S. If no private r_i carries7, then |L|≥5 and at least three are actual maximal subgroups. The latter is an explicitly conditional strengthening, not an ambient restriction.

**Proof.** For each i∈L whose U_i is NOT maximal in S, choose an actual proper maximal overgroup M_i strictly containing U_i; finiteness of S supplies it. MIN-EL forces

    7 does NOT divide m_i=[S:M_i].

Because m_i divides7r_i and lacks7, it divides r_i. It is greater than1 because M_i is proper. For distinct such i,j the numbers m_i,m_j are therefore genuinely coprime, since r_i,r_j are. In particular these are distinct proper maximal subgroups: equality would force the same index>1 to divide two coprime private cofactors.

If there were three such nonmaximal U_i, their three actual M_i would violate μ(S)≤2. Thus at most two indices of L are nonmaximal vertices, proving MV. If all r_i lack7, only2,3,5 can own a small private prime, so |L|≥5 and the stated three-maximal conclusion follows. QED.

The original selected cosets are unchanged in this μ application: the M_i serve ONLY to contradict a three-coprime-index subgroup family. We do NOT assume their larger cosets are disjoint, and do not replace the original U_i by those7-free-index overgroups.

## 6. Exact consequential frontier and first obstruction

The new elementary step EL proves a genuine family of source-preserving coset enlargements. It licenses prime removal only when an ACTUAL7-retaining overgroup of the prescribed coprime enlargement index exists. A bare factorization7r_i=7s·a does not supply that overgroup.

Consequently, if the unrestricted simple-group P7 residual is nonempty, it has an actual minimum-index witness in which:

- each private-small-prime-free vertex has NO strict7-retaining overgroup;
- relative to the precisely declared μ(S)≤2 theorem, at least two of these vertices are actual maximal subgroups of S (at least three in the explicit no-private7 subcase);
- the rest of the eight actual disjoint cosets and every cofactor remain present. No group family, order, valuation or private-prime universe has been bounded.

The first unresolved actual-group obstruction is now concrete: such a minimal witness can be blocked from further EL enlargement by primitive/maximal subgroup vertices or by enlargements whose actual multiplier shares2/3/5/7. The supplied classical coprime-index theorem stops after controlling the7-FREE maximal overgroups; it gives no contradiction for the remaining maximal vertices of indices7r_i. Dividing those indices by7 again would reintroduce the unproved prime-deletion/action bridge that this proof deliberately avoids.

A consequential next step is therefore a theorem about the actual simple-group maximal vertices together with their original disjoint cosets and other six vertices, or a sharper geometric treatment of the small-multiplier obstruction(H). Neither is proved here. An arithmetic index list or a partial numerical survey cannot be reported as a genuine counterexample or full exclusion.

## 7. Review and execution boundary

This new snapshot has not yet had a separate reconstruction or parent disposition. The old normal-section parent record and the previous chain's reviews do not cover EL/MIN-EL/MV automatically. EL itself is elementary and independent of the inherited Sun7/Sun5/local G4/F7 chain; mapping a full Sun8 counterexample into this simple-group setting remains conditional on the already recorded Sun7/R8/descent interface. MV additionally imports the exact classical μ bound and its unreplayed ancestry.

No full Sun8 proof, actual eight-coset witness, global maximal-subgroup classification, formal/kernel verification, human review or novelty clearance is claimed. The enlargement mechanism may have earlier equivalents. No scientific program or modelCLI has run.
