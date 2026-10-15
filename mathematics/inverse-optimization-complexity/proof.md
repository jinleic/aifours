# Forward versus inverse optimization: precise resolutions

Date: 2026-10-14 (America/Los_Angeles).

## 1. Scope and prior theorem

The natural **full-linear, binary, known-feasible-start** version is already solved, not a new open problem. Andreas S. Schulz, *On the Relative Complexity of 15 Problems Related to 0/1-Integer Programming* (2009), DOI [10.1007/978-3-540-76796-1_19](https://doi.org/10.1007/978-3-540-76796-1_19), Assumptions 1–2 and Theorem 1, proves equivalence of optimization, optimality verification, and inverse optimization under the 1- and infinity-norms. Its author manuscript is `sources/schulz-2009.pdf`. The proof below reproduces the essential verification-to-augmentation and bit-scaling arguments (Lemmas 19 and 5), making their promises explicit and extending the zero-test implication to other positive-definite distances. No novelty is claimed for this equivalence.

The separate feasibility-only counterexamples below deliberately drop full cost-vector freedom. They do **not** refute Schulz's theorem. We did not obtain a natural counterexample with hard optimization after a feasible solution is supplied, nor could one exist in the full-linear binary model unless P=NP.

## 2. Encoded model

An instance descriptor I is a finite binary string. A polynomial-time computable dimension n=n(I) is polynomially bounded in |I|. The feasible set F(I) is a subset of {0,1}^n; membership (I,x) is decidable in polynomial time. F depends on I, not on the objective vector. All integers are binary-encoded, and a rational is a signed numerator and positive denominator in binary. Input size counts all these bits, not numerical magnitudes.

The **full-cost model** allows every c in Q^n. Forward optimization returns x in F minimizing c·x, or reports F empty. The **known-start version** additionally receives x_start in F; consequently its inputs are nonempty. The inverse instance receives (I,c,x0,w), where x0 in F and all distance weights w_i are strictly positive rationals. It must output an exact optimal modified cost d in Q^n. Ties are allowed: x0 must be an optimizer, not the unique optimizer. In the main model d is unrestricted. Its feasible region is the closed rational polyhedral cone

    N(I,x0) = {d : d·(x-x0) >= 0 for every x in F(I)}.

The distances considered are:

- D_1(d,c)=sum_i w_i |d_i-c_i|;
- D_inf(d,c)=max_i w_i |d_i-c_i|;
- D_2(d,c)^2=sum_i w_i (d_i-c_i)^2 (report squared value, avoiding an unnecessary square-root encoding);
- D_Hsum(d,c)=sum_i w_i 1[d_i != c_i];
- D_Hmax(d,c)=max({w_i : d_i != c_i} union {0}).

Sum-Hamming and bottleneck-Hamming are different problems. No forward-P-to-inverse-P claim for sum-Hamming is assumed. The word 'polynomial' means deterministic bit-polynomial time and exact output, not pseudopolynomial time, approximation, or an oracle call counted as a free implementation.

For the norm cases, an optimum exists: N is nonempty (0 belongs to it), closed, and the objective has bounded sublevel sets. For Hamming, only finitely many changed-coordinate supports exist; among supports admitting any feasible d choose one of minimum weight. Feasible rational linear systems have rational solutions of polynomial encoding length here, because their coefficients have polynomial bit size and dimension is polynomial. For squared weighted Euclidean distance, the unique projection is rational: restrict to the minimal face containing the projection and solve its rational equality-constrained quadratic program. A basis of active equations suffices, and determinant bounds give polynomial bit length. Thus the exact formulations above have finite encoded witnesses; they do not silently require a real-number oracle.

## 3. Lemma Z: the inverse zero test is optimality verification

For any listed distance, the exact optimum is zero if and only if x0 minimizes c·x over F. If x0 is optimal, d=c is feasible and has distance zero. Conversely, distance zero implies d=c since every weight is positive; inverse feasibility then says that x0 is optimal under c. This also works if the inverse algorithm returns only its exact minimizing d: test d=c. If the inverse problem imposes additional allowed-cost constraints, this lemma requires c itself to be allowed. It does not allow queries outside the advertised cost domain.

An approximation oracle is not substituted for this exact zero test. For general norms, one cannot decide whether an approximate numerical zero is mathematically zero without further separation bounds.

## 4. Lemma A: verification yields an improving feasible solution

Assume an oracle V(I,q,x0) correctly answers whether the supplied feasible x0 minimizes q·x over F, for every rational q. Given integer c and x0 in F, the following algorithm either certifies optimality or constructs y in F with c·y<c·x0 using at most n+1 oracle calls.

First call V(I,c,x0). If it says yes, stop. Otherwise set M=1+sum_i |c_i|, s_i=2x0_i-1, and S=empty. Process i=1,...,n. Query V at the vector

    q_j = c_j - M s_j 1[j in S union {i}].

If the answer is no, add i to S. If yes, leave S unchanged. Finally output y_j=x0_j for j in S and y_j=1-x0_j otherwise.

**Proof.** For any T and any z in F,

    q(T)·(z-x0) = c·(z-x0) + M |{j in T : z_j != x0_j}|.

The absolute value of c·(z-x0) is at most sum_i |c_i|<M. Therefore z improves on x0 under q(T) if and only if z improves under the original c and agrees with x0 on every coordinate in T.

Let B(S) be the set of original-c improving feasible points agreeing with x0 on S. Initially B(empty) is nonempty. A no answer means B(S union {i}) is nonempty, so the update preserves nonemptiness. A yes answer means every member of the current B(S) differs from x0 at coordinate i. Future B sets are subsets of this one, so this forced difference persists without needing to enforce it by an additional constraint. After all coordinates, B(S) is nonempty, and all its points agree with the reported y on every coordinate. Hence B(S)={y}, which proves feasibility and strict improvement. Costs in every query have bit length polynomial in the original input. No restricted feasible-set oracle, feasibility search, or self-reducibility hypothesis has been smuggled into the proof. QED.

## 5. Theorem F: inverse in P implies forward in P from a feasible start

For the model in Section 2, if any one of its five exact inverse variants is polynomial-time solvable, then the known-start forward problem is polynomial-time solvable.

**Proof.** Lemma Z gives V; Lemma A gives augmentation. Scale rational c by the product of its positive denominators, producing an integer vector of polynomial encoding length with the same optimizers.

For signed coefficients introduce virtual coordinates z_i=x_i when c_i>=0 and z_i=1-x_i when c_i<0. Then c·x equals a constant plus a·z, where a_i=|c_i|>=0. The virtual feasible set is in bijection with F. No new instance-class closure is needed: to query optimality for virtual cost p, query the original oracle with cost q_i=p_i on unflipped coordinates and q_i=-p_i on flipped coordinates, with the correspondingly mapped feasible target. Constants do not affect optimality.

Let L be the maximum bit length of the a_i (L=0 if all are zero). Start with the supplied feasible z and p=0; z is optimal for p. Read the L binary positions of a from most significant to least significant. At each position let b in {0,1}^n be its bit vector and set p_new=2p+b. Repeatedly apply augmentation for p_new until the current z is optimal; then set p=p_new.

At the start of a phase, z is optimal for p. For any z* in F minimizing p_new,

    p_new·(z-z*) = 2p·(z-z*) + b·(z-z*) <= n.

The first term is nonpositive, and each of the n terms in the second sum is at most 1. The gap is a nonnegative integer. Each successful augmentation decreases it by at least 1. Hence a phase uses at most n successful augmentations and one final optimality check. There are L phases. Lemma A uses at most n+1 verification queries per augmentation, so O(n^2 L) verification calls suffice, each of polynomial encoded size. The final virtual cost is a, and mapping back gives a forward optimum. The n=0 and c=0 cases return the supplied point immediately. QED.

**Corollary F1.** If one can find a feasible point or correctly report emptiness in polynomial time, then inverse in P implies the ordinary forward problem in P. In particular, under P!=NP no full-cost binary family whose forward problem is NP-hard *even with a feasible start* can have any of these exact inverse variants in P.

**Corollary F2 (constant cardinality).** Suppose every x in F has the same sum_i x_i. If the inverse zero test is available only for arbitrary nonnegative rational costs, the same conclusion holds: add a sufficiently large common constant to every coefficient of every signed-cost verification query. This makes the queried vector nonnegative while adding the same objective constant to all feasible points. The baseline vector must be admissible in the inverse model; finite upper bounds on all costs would require a separate argument.

**Known reverse implication, with its limits.** For D_1 and D_inf, a forward polynomial algorithm separates the inequalities d·(x-x0)>=0 by minimizing d·x. Linearizing the distance with n absolute-value auxiliary variables or one radius variable yields a rational LP of polynomial dimension and polynomial-size coefficients. The polynomial-time separation-to-optimization theorem solves this LP, including any explicitly given rational cost bounds. Heuberger's Theorem 3.3 states the weighted l1 direction. The weighted l-infinity direction follows from the same separation argument and radius-variable LP formulation; Schulz's Lemma 4 explicitly gives the unweighted infinity-norm case. Together with F1 this gives equivalence for weighted l1 and l-infinity. It is not a proof of the same forward-to-inverse direction for sum-Hamming. Our complete elementary proof above is of the converse, which is the book's question under the stated hypotheses.

## 6. Theorem G: a dummy-solution closure removes the feasible-start obstruction

Assume a family can, in polynomial time, replace I by an instance J of the *same oracle-supported family* with feasible set, up to an explicitly known coordinate renaming,

    F(J) = {(1,0^n)} union {(0,x) : x in F(I)}.

Assume arbitrary rational costs are permitted on all n+1 coordinates. Then polynomial solvability of any inverse variant in Section 2 implies polynomial solvability of the ordinary forward problem, including detecting emptiness.

**Proof.** Let B=1+sum_i |c_i|. Apply Theorem F to J with known starting point (1,0^n) and cost (B,c). Every real feasible point (0,x) has cost c·x<=sum_i |c_i|<B. Thus the returned optimum is the dummy exactly when F(I) is empty; otherwise its last n coordinates form an optimum for I. Everything has polynomial size. QED.

A related threshold reduction uses cost (K+1/2,c) for integral c and integral K: the dummy is optimal if and only if there is **no** x in F(I) with c·x<=K. This turns an inverse zero test into the complement of the forward threshold test. If a problem is also polynomially self-reducible by prefix fixing, these threshold answers recover a witness one bit at a time, after an initial existence check. The stronger known-start proof above does not require prefix closure. Crucially, neither augmentation by a dummy solution nor prefix closure may be presumed for an arbitrary problem class.

## 7. Proposition C: an explicit restricted-cost, feasibility-only counterexample

This is a counterexample to the **broad reading allowing restricted cost parameters and forward infeasibility detection**, not to the full-cost model in Section 2.

Let phi be a CNF formula on m variables and k>=1 be given in unary (or take k=1). Define

    F(phi,k) = {(a,z) : a in {0,1}^m satisfies phi, z in {0,1}^k}.

Feasibility checking is polynomial. Allow **only** cost vectors (0^m,b), b in Q^k, both as baseline and as modified costs. The objective is b·z. The forward task is to return an optimum or report F empty. It is NP-hard: phi is satisfiable if and only if the instance with b=0 has any feasible solution (equivalently, a feasible solution of value <=0). Thus a polynomial forward algorithm would decide SAT, contradicting P!=NP.

For a valid inverse target (a0,z0), ignore the supplied satisfying assignment a0 after verifying it. For each free coordinate j, set

    b'_j = max(b_j,0), if z0_j=0;
    b'_j = min(b_j,0), if z0_j=1.

This is an exact inverse optimum under every distance in Section 2, with weights on the k mutable coordinates. The fixed witness coordinates are zero in both vectors and contribute zero.

**Proof of inverse optimality.** Since phi is satisfiable (a0 is supplied), every z is feasible paired with a0. Thus z0 is optimal precisely when b'_j>=0 for z0_j=0 and b'_j<=0 for z0_j=1, coordinate by coordinate. The displayed clipping is the closest point in each allowed half-line. Every sign-violating coordinate is forced to change, by an absolute amount at least |b_j|; all other coordinates can remain unchanged. These componentwise lower bounds imply optimality for weighted l1, squared weighted l2 and weighted l-infinity. The forced changed-coordinate set gives simultaneous lower bounds for both sum-Hamming and bottleneck-Hamming, achieved by clipping. Runtime is O(m+|phi|+k) arithmetic/comparison operations, with polynomial bit complexity. QED.

**Degeneracy disclosure.** Once any feasible target is supplied, forward optimization is trivial: reuse its satisfying assignment and choose each z_j according to the sign of b_j. All forward hardness comes from locating any feasible witness / detecting emptiness, and arbitrary costs on the witness coordinates are prohibited. Enabling those costs destroys this inverse algorithm; for example, phi=(a1 OR a2), c=(1,1,0), and target (1,1,0) is not optimal, whereas the restricted algorithm would leave it unchanged.

**Natural but equally degenerate example.** The unweighted Hamiltonian-cycle problem can be regarded as minimizing t times the number of chosen edges, where the only parameter is a single rational t. Every Hamiltonian cycle has exactly |V| edges. Given a cycle, the inverse optimum is always zero for any positive-definite distance on t, whereas producing a cycle or reporting none is NP-hard. This is a familiar combinatorial family but it has the same two defects: restricted uniform edge costs and feasibility-only hardness. It is not the weighted traveling-salesman inverse problem. No claim of a natural nondegenerate counterexample is made.

## 8. Proposition L: exact unconstrained weighted l-infinity formula

For any nonempty finite binary F and supplied x0, let s_i=2x0_i-1 and

    r = max( {0} union {
          c·(x0-x) / sum_{i:x_i!=x0_i}(1/w_i)
          : x in F, x!=x0 } ).

Then d_i=c_i-r*s_i/w_i is an optimal inverse cost vector and the minimum weighted l-infinity distance is r. A singleton F gives r=0.

**Proof.** If D_inf(d,c)<=t, then

    d·(x0-x) >= c·(x0-x) - t sum_{i:x_i!=x0_i}(1/w_i).

Optimality of x0 requires the left side to be nonpositive, so t must be at least every positive ratio displayed above. Conversely, the proposed d gives equality in this bound simultaneously for every x: signs of x0_i-x_i are fixed by x0 wherever nonzero. The definition of r then gives d·(x0-x)<=0 for all x. Its distance is r (or zero for r=0). QED.

The formula is a min-max characterization, **not a polynomial algorithm by enumeration**: F may be exponentially large. It supplies an exact independent mathematical reference for the small-instance checks, and connects to the min-max analysis in Bérczi–Mendoza-Cadena–Varga, arXiv:2302.13411, DOI 10.1007/s11590-024-02183-0.

## 8a. Proposition U: the remaining feasibility gap has an unambiguity barrier

Assume exact inverse optimization is in P in the full-cost binary model, without assuming an initial point is available. Let

    T = {(I,c,K) : exists x in F(I) with c·x <= K}.

Then T belongs to UP, the class of languages recognized by polynomial-time nondeterministic machines with at most one accepting computation per input. Consequently, if T is NP-hard under polynomial many-one reductions, NP=UP. This is a conditional barrier, not a proof that P=NP or that NP!=UP. No literature-novelty claim is made for this elementary consequence.

**Proof.** Scale c to an integer vector C by a common positive denominator D; compare C·x with DK. For n coordinates put B=2^n and q_i=B C_i+2^(i-1), i=1,...,n. The binary code sum_i 2^(i-1)x_i lies between 0 and B-1 and is distinct for different binary x. Hence q has a unique minimizer whenever F is nonempty, and that minimizer also minimizes C: a change of at least 1 in C·x dominates the entire tie-breaking code. All q_i have polynomial encoding length.

A nondeterministic verifier guesses exactly n bits x, checks x in F, uses Lemma Z at q to check global q-optimality, and accepts only if C·x<=DK. Empty F has no accepting guess. Nonempty F has at most one globally q-optimal guess, and this guess accepts exactly when the threshold is attainable. Thus T is in UP. Since UP is contained in NP and closed under inverse images of polynomial many-one reductions, NP-hardness of T implies NP=UP. The same argument with c=0 puts the nonemptiness language in UP. QED.

If the class guarantees F nonempty on every valid descriptor (with polynomial-time recognizable validity), the complement threshold can instead accept that same unique optimum when C·x>DK, with invalid descriptors handled deterministically. Thus T is in UP intersect coUP in that setting. NP-hardness would then imply NP=coNP as well. This specifies why Heuberger's coNP warning must not be silently applied to arbitrary infeasible instances.

## 8b. Proposition O: no generic black-box shortcut to the first target

Consider a different, explicitly oracle-only model: an unknown F is either empty or a singleton {s} subset {0,1}^n, accessible only by membership queries. Supply an inverse oracle that, on a feasible target, returns the original cost c (every cost already makes the unique point optimal), and on an infeasible target returns an INVALID flag. This oracle gives exactly the same information as a membership test, regardless of costs, weights, or norm.

Any deterministic algorithm deciding whether F is empty needs 2^n queries in the worst case. Indeed, until every point has been queried, the transcript consisting entirely of negative answers is consistent both with the empty set and with a singleton at any unqueried point. With a nonempty-singleton promise, finding s requires at least 2^n-1 queries in the worst case, since two unqueried candidates remain indistinguishable before that many queries.

This is a proved oracle obstruction, **not** an explicit NPO family with NP-hard forward problem: an explicit polynomial-time feasibility representation might reveal s or expose exploitable structure. It therefore does not settle the remaining full-cost question. It does explain why merely calling the promised-feasible inverse oracle more often cannot replace a structural feasibility argument.

## 8c. Theorem B: the known-start bottleneck converse also holds

Let F be any nonempty family of **nonempty** subsets of E={1,...,n}, with a supplied X0 in F. The forward objective is now genuinely nonlinear:

    f(c,X) = max_{i in X} c_i.

Assume all rational cost vectors, or at least the original costs and every 0/1 vector used below, are admissible. If the inverse problem for making X0 globally optimal under this bottleneck objective is exactly polynomial-time solvable for any positive-definite distance, then forward bottleneck optimization from X0 is polynomial-time solvable. The inverse oracle must work for all supplied feasible targets, although the following reduction only needs this particular X0. This is an elementary additional reduction, not claimed as a new literature result.

**Proof.** The inverse zero test supplies an optimality verifier V for f. For any A subset E, we can decide whether there is X in F with X subset A:

- If X0 subset A, answer yes using X0.
- Otherwise set q_i=0 for i in A and q_i=1 outside A. Then f(q,X0)=1. Since every feasible set is nonempty, a feasible X has f(q,X)=0 exactly when X subset A. Consequently a feasible X subset A exists exactly when V(q,X0) answers **not optimal**.

Every query uses the original instance and a valid target; we never assume that the restricted family {X in F:X subset A} is an allowed instance.

Sort the distinct original costs. The optimal bottleneck value is one of them. For each candidate threshold t define A(t)={i:c_i<=t}. The preceding existence predicate is monotone in t, so binary search with O(log n) verifier calls finds the least feasible threshold. Start with its A=A(t). For each element i, delete it from A if the same predicate remains true for A minus {i}. At the end A still contains a feasible set, and removing any remaining element destroys that property: a failed deletion cannot become feasible when further elements are removed. If some feasible X were a proper subset of final A, an element in A minus X could still be removed, contradiction. Therefore final A itself belongs to F. Its bottleneck is at most the least feasible threshold and hence optimal. There are at most n further verifier calls, sorting is polynomial, and every query cost has one-bit entries. QED.

Thus a minmax/bottleneck formulation with a feasible start is **not** a surviving candidate for the requested counterexample. This conclusion is stronger than merely observing that the linear theorem does not apply.

## 8d. Independent binary features are another solved boundary

Suppose f(c,x)=sum_{j=1}^m c_j phi_j(x), where m is polynomial, every phi_j(x) is binary and polynomial-time computable, all c_j are independently mutable, and phi contains the original coordinates x_1,...,x_n. Then the image F'={phi(x):x in F} is a binary feasible family with polynomial-time membership: read its first n coordinates as x, check x in F, and recompute phi(x). A supplied x0 yields phi(x0), and changing feature costs is exactly the advertised original parameter change. Apply Theorem F to F' and recover x from those first n coordinates. Therefore inverse in P implies forward in P here as well. This covers fully independently parametrized pseudo-Boolean polynomial objectives whose feature lists contain all linear monomials, including full quadratic objectives with linear terms. It does not cover arbitrary nonlinear dependence on costs or tied coefficients.

## 8e. Precisely retained general question and failed attack

The remaining research question is the converse for **general objectives**, not an invented claim that the linear or bottleneck cases are still open. One finite encoded refinement of Heuberger's equations is:

> Fix a uniform family of polynomial-time computable rational-valued objectives f_n(c,x), with polynomial output bit length, f_n(0,x)=0, all rational parameters c in Q^{p(n)}, binary feasible sets F(I) with polynomial membership and a supplied feasible start, and global rather than local optimality. Suppose the unconstrained weighted-l1 inverse problem, given any c and any x0 in F(I), always has a rational minimizing parameter of polynomial encoding length and is exactly polynomial-time solvable. Must forward global optimization be polynomial-time solvable?

The attainment/encoding premise is explicit because a general nonlinear inverse constraint need not have a rational or even attained optimum. The normalization f_n(0,x)=0 prevents making the inverse artificially infeasible at inconvenient targets. The supplied start removes feasibility-only hardness. The zero-test lemma still applies, but our linear augmentation proof requires constructing parameter changes that penalize disagreement with a target without otherwise changing comparisons; an arbitrary f_n need not permit those changes. Bit scaling also need not preserve the objective structure. The bottleneck threshold argument relies on a special subset-existence predicate unavailable for arbitrary f_n. Feature lifting works only when the independent-coordinate and recoverability hypotheses of Section 8d hold.

We have not proved or refuted this general encoded implication. Heuberger's general equations and the 2025 broad-open wording motivate it, but **no opened source states this exact strengthened encoding/normalization refinement verbatim**. Thus its designation here is OPEN as an unresolved research target, not a claim that its precise formulation has a certified community-wide open-status theorem. The book's full general question remains unsolved in this dossier; neither Proposition C nor the rediscovery of Schulz is substituted for it.

## 9. What is and is not settled

1. Full-linear binary problems with arbitrary signed costs and a known/easily found feasible start: **settled affirmatively in prior literature (Schulz 2009)**. The preceding proof is a reproduced argument with executable exact checks. Hamming inverse-P implies forward-P follows by the same zero-test implication; no equivalence for sum-Hamming is asserted.
2. Broad models allowing restricted costs and feasibility-bearing forward tasks: **the literal universal implication is false under P!=NP**, by C. The construction is intentionally degenerate and is not advertised as solving the intended nondegenerate question.
3. Full-cost binary families with arbitrary implicit feasibility, no supplied/easily found initial point, and no dummy closure: **not resolved here**. Our algorithms need their first feasible target. The restricted-cost examples do not provide a counterexample to this exact remaining statement. Proposition U shows that an NP-hard threshold counterexample would imply NP=UP; Proposition O rules out a completely generic membership/inverse-oracle shortcut, but is not an explicit-input counterexample. We make no claim that the literature has proved this most general remaining formulation open; our search did not settle it.
4. The known-start minmax/bottleneck converse and independently parametrized recoverable binary-feature objectives also hold, by Sections 8c–8d. The normalized general-objective refinement in Section 8e remains **OPEN here**. Changing constraints/edge lengths, arbitrary real feasible sets, partial target observations, and KKT points in place of global optima require separate theorems. The July 2025 Springer chapter still calls its broad NP-hard-forward/P-inverse question unresolved in its public abstract. This is evidence about that publication, not a contradiction to Schulz's explicitly conditional theorem or proof that every specialized refinement is open.

## 10. Verification boundary

The complete arguments above, rather than finite experiments, establish the universally quantified claims. `work/check.py` exercises the clipping inverse algorithm, verification-to-forward reduction, bottleneck extension, and unique-optimum certificates against independent exhaustive enumerators on finite test sets. The extended result is `evidence/check-results-extended.json`; `evidence/check-results.json` preserves the earlier run before the additional claims. `work/algorithms.py` exposes the actual reductions and receives only yes/no optimality callbacks, never a hidden optimizing callback. The independent model reviews and resolution record are under `evidence/`. These are mathematical proofs with executable sanity checks, not Lean/kernel-checked formalizations.
