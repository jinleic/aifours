# Sun8: simultaneous index-two collision characters and a normalizer 2-rank bound

**MathSun8 / math-6. NEW WRITTEN candidate, with the finite integer checks explicitly declared in §9.** Actual pre-write clock: **Sun Oct 25 04:03:13 PDT 2026**, returned by `/bin/date`. This is a new representation of the global collision barrier, not another per-overgroup enumeration. No pinned source is edited. The mandatory v28-A reconstruction was completed first in `peer-review-rqls-consolidated-newmath-v1.md`.

## 1. Unchanged target and exact new endpoint

The unrestricted target remains: every eight pairwise disjoint LEFT cosets of finite-index subgroups in any group have two subgroup indices with gcd at least eight. The retained conditional Sun7/normal-section chain reduces a counterexample to actual finite nonabelian simple P7 data; this file does not re-prove that chain or silently assume its conclusion unconditionally.

All NEW theorems below work directly in any finite group G with ACTUAL P7 data:

    eight pairwise disjoint LEFT cosets g_j U_j,
    [G:U_j]=7 r_j,  gcd(r_j,r_k)=1 for j≠k.

No cofactor, group-order or private-seven truncation is added. The new endpoint is a simultaneous statement about **every** actual index-two overgroup of a vertex, expressed inside its ONE normalizer quotient.

### Theorem N2 — simultaneous collision structure

For each vertex put N_i=N_G(U_i). Then:

1. **Normalizer retains seven:** 7 divides [G:N_i], hence |N_i/U_i| divides r_i.
2. If index-two overgroups exist, r_i is even and every other r_j is odd. Normalize the selected coset to U=U_i, set N=N_i and Q=N/U. Each other original coset meeting N determines an ACTUAL quotient coset X_j=x_j H_j in Q, avoiding 1, and a fixed fibre index

       b_j=[U:U∩U_j]=r_j beta_j,
       beta_j∈{1,2,3},
       c_j=[Q:H_j]≥2,  beta_j c_j≤7.

   These data are common to ALL index-two overgroups, not chosen afresh for each one.
3. Index-two overgroups U<M≤G are in bijection with nonidentity involutions t of Q, by M=pi^-1(<t>). Their genuine collision sets are EXACTLY

       J_t={j : t∈X_j}.

4. Every beta=3 quotient support is a negative halfspace for an actual homomorphism Q→C2. There are at most FOUR such original colliders in the entire normalizer; their characters span dimension at most THREE. Thus a normal subgroup K_3 of Q of index at most eight simultaneously avoids every beta=3 collision. Every involution in K_3 has at most TWO genuine collisions, rather than the old general upper bound three.
5. For EVERY elementary abelian 2-subgroup E≤Q, all the nonempty restrictions X_j∩E have a common blind subgroup B_E≤E of codimension at most FOUR: no point of B_E belongs to any X_j. The bound improves to THREE except for the explicitly identified private-three-owner configuration in §7.

### Minimum-witness consequence

In any actual P7 witness in a fixed finite G minimizing sum r_j, a collision-free strict index-two enlargement is impossible. Consequently

    2-rank(N_G(U_i)/U_i) ≤4

for every i, where 2-rank is the maximum rank of an elementary abelian 2-subgroup. It is at most three if no OTHER private cofactor owns three, or if that owner's normalizer collision has beta other than one. If the quotient itself is elementary abelian, its order is at most16 and there are at most15 actual index-two overgroups; in the strengthened case these bounds are8 and7. **No bound of15 is asserted for the number of involutions of an arbitrary nonabelian quotient.**

Only the unique possible even-private vertex can have such overgroups; the other quotients have odd order by item1. Maximal/self-normalizing vertices are not excluded, and a low 2-rank quotient need not be small.

## 2. Imports, assurance and what is not imported

The new proof uses elementary subgroup cardinality/coset facts and the exact classical Sun3 and Sun4 statements: k disjoint finite-index LEFT cosets have a pairwise subgroup-index gcd at least k, for k=3,4. This is Zhu, *On Sun's conjecture concerning disjoint cosets*, Theorem1.1, [arXiv:0807.2207v1](https://arxiv.org/html/0807.2207v1#S1.Thmtheorem1), as explicitly authenticated at the retained parent boundary below. Its published proof is imported, not formally verified here.

Retained boundaries read for this continuation:

- `small-index-enlargement-collisions-v1.md`, SHA `99d29ff3df6ac8c1d047d6efe4b624f089c3faadb700caa8b4dbea27a6f66aef`, complete158LF; governing parent `institute/runs/three-area-2026-10-23-96h/wave-v16-written-frontiers-parent-v1.md`, Sun8 section LF29–37. The existing bounds were at most3/4 for supplied index2/3 enlargements and NONEMPTY collisions in a minimum witness. They did not couple different index-two overgroups.
- `sun8-normal-section-parent-v1.md` in the same run: the arbitrary-group Sun8↔simple-P7 connection is relative to the literal internal Sun7 theorem. That historical chain is not a NEW import needed for N2 itself.
- `sun8-actual-enlargement-parent-v1.md`: achieved minimum-sum witnesses and the old EL/MIN-EL/MV scopes remain intact. N2 does not use the classical mu(S)≤2 theorem, CFSG, G4/F7, the internal Sun7 proof, a subgroup database or an assumed overgroup.

**Status:** WRITTEN candidate / NOVELTY_UNCLEAR, not independently reviewed, parent accepted, Lean/kernel checked, human/cross-vendor verified or a full Sun8 result. Exact finite checks below are in-kernel arithmetic, not formal proof or an eight-coset witness certificate.

## 3. One fixed fibre index per neighbour, before choosing an overgroup

Fix i and left-translate all eight cosets by g_i^-1. The distinguished coset is U=U_i; write the other seven as a_j U_j. Let V_j=U∩U_j. Divisibility of the intersection index and the product-set cardinality give

    [G:V_j]=7 r_i r_j lambda_j,
    [U:V_j]=r_j lambda_j,
    |U U_j|/|G|=lambda_j/7,
    1≤lambda_j≤7.

The two original cosets U and a_jU_j are disjoint. Thus lambda_j cannot equal seven: in that case U U_j=G, forcing every left U-coset to meet every left U_j-coset. Hence

    1≤lambda_j≤6.                                      (3.1)

The V_j and lambda_j depend only on the original subgroups; they do not change when one varies an overgroup of U. No intersection index is incorrectly assumed to divide the product of indices.

### Lemma NR: every normal overgroup of U retains seven

Let U◁L≤G. Suppose 7∤d=[G:L]. Since d divides7r_i and lacks7, d divides r_i. Therefore d is coprime to every7r_j, j≠i. The coprime-index lemma makes L meet every a_jU_j, and

    [L:L∩U_j]=7r_j.

In P=L/U let H_j=(L∩U_j)U/U and let X_j be the projected nonempty intersection coset. Exact index multiplication gives

    [L:L∩U_j]=[P:H_j][U:U∩U_j]
      =c_j r_j lambda_j,
    c_j lambda_j=7.

By (3.1), lambda_j=1 and c_j=7. Each X_j avoids1, for a point above1 would be an original intersection with U. If two X_j overlap at some q, the two actual original pieces in that U-fibre are left cosets of V_j,V_k, of coprime indices r_j,r_k, and therefore intersect. Thus the seven X_j are pairwise disjoint. But each occupies |P|/7 points: they exhaust P while all avoiding1, contradiction.

Hence 7|[G:L]. Taking L=N_G(U) proves item1. In particular U◁G is impossible, but the lemma is stronger: it controls the actual normalizer even though the normalizer need not be normal in G. It is not a claim about arbitrary, nonnormal overgroups.

## 4. The exact simultaneous quotient and incidence representation

Set N=N_G(U), q=[N:U], [G:N]=7s. The proved identity gives r_i=sq. Thus q divides r_i. A subgroup M with [M:U]=2 normalizes U, so every such M lies in N, and its quotient is an order-two subgroup of Q=N/U. Conversely the preimage of each order-two subgroup of Q is a genuine index-two overgroup of U. This proves the claimed bijection, with no existence inferred from a factorization of r_i.

If an index-two overgroup is possible, r_i is even, so all seven other r_j are odd. Fix this case; otherwise the index-two theorem is vacuous. Let I be the set of j for which N meets a_j U_j. Choose x_j in that intersection and W_j=N∩U_j. Then

    N∩a_jU_j=x_j W_j,
    H_j=W_j U/U≤Q,
    X_j=pi(x_j)H_j.

For each q0∈X_j and ONE fixed representative of q0, the original piece in that U-fibre translates into a left V_j-coset inside U. Its index is the SAME b_j=r_j lambda_j from §3. All pieces at a common q0 are pairwise disjoint. Every X_j avoids1; in particular its index c_j is at least two.

The actual N/U_j product formula yields

    [N:W_j]=r_j alpha_j,  1≤alpha_j≤7.

But exact index multiplication through U gives [N:W_j]=c_j b_j, so

    alpha_j=c_j lambda_j≤7.

Set beta_j=lambda_j. Since c_j≥2, beta_j∈{1,2,3}. Thus beta=3 forces c=2; beta=2 permits c=2 or3; beta=1 permits c=2,...,7. The actual c is always a divisor of |Q|.

For an involution t≠1, the enlarged coset M_t=pi^-1({1,t}) meets a_jU_j exactly when X_j meets {1,t}. Since 1∉X_j, this is exactly t∈X_j. Therefore J_t is the ACTUAL collision set, not a feasible incidence surrogate.

## 5. Fibre gcds and the global sign-character budget

Write A,B,C for the neighbours with beta=1,2,3. Their fibre indices are respectively r_j,2r_j,3r_j. The private r_j are pairwise coprime and odd. The exact gcd table is

| Types | gcd of actual fibre indices |
|---|---|
| A,A |1|
| A,B |1|
| B,B |2|
| C,C |3|
| A,C |3 if the A cofactor owns3; otherwise1|
| B,C |3 if the B cofactor owns3; otherwise1|

There is at most ONE private-three owner e among these seven neighbours. These statements allow arbitrary private powers of three or seven; no squarefree condition is used.

At any quotient point, coprime fibre indices forbid simultaneous presence. Three B pieces would violate Sun3 inside U; four C pieces would violate Sun4 there. In fact EVERY pair of occurring fibre indices has gcd at most three, so four pieces of any types at one point violate Sun4. Thus the total multiplicity is at most three at EVERY point of Q, not just involutions. A pieces are mutually disjoint and disjoint from B; a non-three-owner A or B is disjoint from every C.

Every C has c_j=2, so H_j is normal of index two. Its unique nonidentity coset X_j is the negative set of a nonzero homomorphism chi_j:Q→F2 (additive notation chi_j=1). Four independent such characters would take value1 simultaneously on some actual element of Q, contradicting multiplicity≤3. Thus their span has dimension≤3.

### Character-count lemma

A multiset of nonzero F2-linear characters whose negative halfspaces have multiplicity≤3 contains at most FOUR members. Its span already has rank≤3. At rank one the conclusion is immediate. At rank two, with multiplicities a,b,c on the three possible characters, the three nonzero image points give a+b≤3, a+c≤3, b+c≤3, hence a+b+c≤4. At rank three choose three independent present characters. An extra copy of one of them or their triple sum would give four negatives at image point111. The only possible extras are their three pair sums. Two copies of the same pair sum give four negatives by setting its two input bits differently and the third bit to1. Two distinct pair sums give four by setting their shared bit to0 and the other two to1. Thus at most one extra exists. This proves the bound including repetitions.

The same argument with multiplicity≤2 gives span rank≤2 and at most THREE members: at rank two the inequalities become a+b,a+c,b+c≤2, and rank one is immediate.

Apply the first statement to C. There are at most four C neighbours, and K_3=intersection ker chi_j is normal in Q of index≤8. At an involution in K_3 only A/B collisions remain. If A occurs it is the sole collision; otherwise Sun3 permits at most two B pieces. Hence |J_t|≤2 for ALL involutions in K_3 simultaneously. Writing T for the set of nonidentity involutions of Q gives the global count

    sum_(t∈T) |J_t| ≤3|T| - |T∩K_3|.              (5.1)

This couples all overgroups through one actual normal subgroup and at most four original C neighbours; it is stronger than separately repeating |J_t|≤3.

## 6. Elementary-abelian slices: a common blind subgroup of codimension four

Let E≤Q be any elementary abelian 2-subgroup, viewed as an F2-vector space of dimension d. Restrict the actual quotient supports to E and discard the empty restrictions. A nonempty restriction is an actual affine coset

    S_j=X_j∩E=a_j+L_j,
    [E:L_j]≤[Q:H_j]=c_j,
    0∉S_j.

No normality of H_j in Q is required: the common-point intersection formula in E gives the affine coset. For A, [E:L_j] is a power of two between two and seven, hence two or four. For B or C it is exactly two. Thus A consists of affine hyperplanes or affine codimension-two subspaces; B and C are negative character halfspaces. All the actual disjointness and multiplicity constraints of §5 survive restriction.

For each A support let W_j=L_j^perp≤E* be its annihilator, of dimension one or two, and ell_j:W_j→F2 the evaluation at its offset. The affine support avoids0 exactly because ell_j≠0. A character vanishing identically on this support belongs to ker ell_j within W_j, of dimension at most one.

### Affine lemma: disjoint A supports have joint annihilator rank≤3

There are at most three A supports: each has density at least1/4, their supports are disjoint, and their union excludes0. For one support the rank is≤2. For two, disjointness of their affine equations requires an inconsistent value on a common character, so their annihilators intersect nontrivially and have total dimension≤3.

For three, none can be a hyperplane, because densities1/2+1/4+1/4 would already exhaust E while avoiding0. All three annihilators are two-dimensional and meet pairwise. If their total span had dimension≥4, take two distinct ones, whose sum has dimension three. The third is not contained in that sum. Its intersections with the first two must be the SAME line, since two different intersection lines would span it inside that sum. Thus all three pairwise intersections are that one common line. Pairwise affine disjointness would require three pairwise different offset values on its one nonzero character, impossible over F2. Hence total rank≤3.

We now bound the span W of ALL A annihilators and all B/C characters.

**Case A has at least two supports.** At most one owns private3, so choose a regular A. Every B/C character must vanish on it, since its support is disjoint from those negative halfspaces. These characters all lie in the at-most-one-dimensional ker ell of that A, hence in the joint A span. The affine lemma gives dim W≤3.

**Case A has one regular support.** The same argument puts all B/C characters inside its annihilator. Thus dim W≤2.

**Case A has one support, belonging to the private-three owner.** Every B character still vanishes on it, so B adds no rank outside its annihilator W_A. The C span W_C has rank≤3. If dim(W_A+W_C)≥5, necessarily dim W_A=2, dim W_C=3 and their intersection is zero. Choose three independent PRESENT C characters. The independent combined equations then admit a point in the A support where all three C characters equal1, giving four actual colliders. Contradiction. Therefore dim W≤4. If W_A has dimension one, a total rank four similarly makes its one affine equation consistent with those three C negatives and is forbidden, so that subcase has rank≤3.

**Case A is empty.** B and C individually have character ranks≤2 and≤3. If both types occur, any regular B is impossible: its negative hyperplane meets EVERY negative C hyperplane, contradicting coprime fibre indices. Thus B consists of the single possible private-three owner. If its character and three independent present C characters were independent, four simultaneous negatives would contradict the multiplicity bound. Hence the combined span has rank≤3. If just one type occurs the same rank≤3 bound is immediate.

In all cases dim W≤4. Set

    B_E=intersection_(chi∈W) ker chi.

Then [E:B_E]≤16. No A support contains a point of B_E, since its offset functional is nonzero, while every defining character is zero there. No B/C support contains such a point either. Thus B_E is genuinely blind to every original neighbour simultaneously. The rank≤3 improvement fails only in the explicitly exceptional single-owner-A/codimension-two case.

This proof quantifies over ALL elementary abelian 2-subgroups E and all actual support restrictions. It does not assume Q itself abelian, identify a quotient point with an arbitrary phase or coset certificate, or presume an overgroup exists.

## 7. Minimum witnesses and the exact rank-four remaining slice

Choose a P7 witness in fixed finite G minimizing the achieved positive integer sum r_j. Every nonidentity involution t in Q must have J_t nonempty: otherwise the actual replacement U by M_t preserves all seven other original cosets and the P7 indices while changing r_i to r_i/2, strictly lowering that sum.

If an elementary abelian E has rank d≥5, its blind subgroup B_E has positive rank and a nonidentity t. That t supplies exactly the forbidden collision-free replacement. Therefore every such E has rank≤4, proving the stated normalizer 2-rank bound. If there is no private-three-owner A support, the rank≤3 proof gives the stronger bound. In particular a rank-four E in a minimum witness requires another original neighbour e with 3|r_e, beta_e=1, and its nonempty restriction has codimension TWO.

There is a more precise necessary rank-four profile. In a fully collisionful rank-four E:

- A consists of exactly that single e support; two A supports or a regular sole A would give a blind line.
- C is nonempty. Every B is then regular (e already owns3), so B/C hyperplanes cannot coexist; hence B is empty.
- The C characters have rank exactly three and consist of three or four original neighbours. If their rank were≤2, their common kernel inside E would have dimension≥2. Its nonzero points would have to be covered by the single A support, but the intersection of an affine coset avoiding0 with a vector space has at most half that space and cannot contain all its nonzero points when its dimension is≥2.
- The two-dimensional A annihilator and three-dimensional C span have one-dimensional intersection: their combined span must be four (otherwise a blind line remains), and the rank bound forbids five.

Thus the rank-four residual is a very specific PRIVATE-THREE configuration, not an arbitrary covering by seven independent damaged vertices. At most five distinct original neighbours collide with any of the fifteen overgroups belonging to E. This is necessary geometry only; it does not eliminate that geometry or construct a P7 realization.

## 8. A sharp necessary-character control — explicitly NOT a Sun8 witness

The exceptional rank-four character pattern really survives the constraints just proved. On E=F2^4 with coordinates x1,x2,x3,x4, take

    S_e={x3=0, x4=1}, beta_e=1, r_e=3;
    S_1={x1=1}, S_2={x2=1}, S_3={x3=1},
    beta_1=beta_2=beta_3=3,
    (r_1,r_2,r_3)=(5,11,13).

The fibre indices3,15,33,39 have pairwise gcd3. The actual E-support indices are4,2,2,2, giving beta*c equal4,6,6,6, all≤7. All supports avoid0; their union is E outside0; multiplicity is at most three because the A support requires x3=0 and therefore never meets the third C support. The defining characters span all four dual dimensions. The common blind subgroup is exactly0.

This is an exact control on the NECESSARY quotient/fibre constraints, with four overlapping quotient supports. It is NOT a group G with eight disjoint original cosets, does not supply compatible actual U_j or fibres in U, and is not a Sun8 counterexample. It shows that a universal rank≤3 conclusion cannot be obtained from these character/capacity constraints alone. A further source-preserving group-geometric input is genuinely needed.

## 9. Declared exact finite checks

The mathematical proof is written. The following finite supplementary checks were performed in this owner's eval kernel using integers, bit parity and exact combinatorial set operations, with no floating arithmetic:

1. All multisets of up to seven nonzero characters of F2^3 were checked for pointwise negative multiplicity≤3. There were169 admissible multisets (including the empty one), with maximum size4, agreeing with the C character-count lemma.
2. The analogous F2^2/multiplicity≤2 check gave11 admissible multisets and maximum size3, agreeing with B.
3. All120 affine codimension-one or -two supports avoiding0 in F2^4 were formed. The1470 disjoint pairs and1505 disjoint triples all had joint annihilator rank≤3. This checks the finite shadow of the affine lemma; the proof for arbitrary dimension is the written argument in §6, not an extrapolation from F2^4.
4. For the §8 rank-four control, the exact point multiplicities on binary labels0,...,15 were

       0,1,1,2,1,2,2,3,1,2,2,3,1,2,2,3.

   Union, avoidance of0, maximum3 and defining-character rank4 were checked exactly. This is NOT finite-witness certification or an actual eight-disjoint-coset certificate.

No native scientific process, solver, external model CLI, publication or git operation was used. The earlier review's discarded float helper initialization is disclosed in that REVIEW, not credited as primary arithmetic. This primary's parity checks used integers only.

## 10. Parkable exact residual and non-claims

This continuation supplies a global simultaneous representation, not a source-preserving elimination of every collision. In an achieved minimum P7 witness, the unique possible even-private vertex has normalizer quotient with 2-rank≤4 (usually≤3); on a normal subgroup of quotient index≤8 its index-two enlargements have at most two collisions; a rank-four elementary slice must have the precise private-three profile above.

Still unproved: exclusion or source-preserving rearrangement of those low-rank collision families; whether the sharp necessary rank-four pattern lifts to actual subgroup/fibre geometry; all maximal/self-normalizing vertices, where Q may be trivial; odd/private5/private7 or composite small-index enlargement barriers; and the unrestricted finite nonabelian simple P7 residual. No uniform existence of an index-two overgroup is inferred. No actual eight-coset certificate has been delivered. The unchanged unrestricted Sun8 target remains unresolved at the inherited Sun7/descent trust boundary.

The NEW theorem needs its own separate supplied-proof reconstruction and parent disposition. The old C2/C3 or enlargement reviews do not automatically accept it. No novelty, formal/kernel, human or cross-vendor assurance is claimed.
