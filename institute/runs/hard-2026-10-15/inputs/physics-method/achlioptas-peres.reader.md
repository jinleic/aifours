URL: https://arxiv.org/pdf/cs/0305009v2
Content-Type: text/markdown
Method: arxiv
Notes: Fetching PDF for full content...; PDF converted via markit

---

# The Threshold for Random k-SAT is 2^k ln2 - O(k)

**Authors:** Dimitris Achlioptas, Yuval Peres
**Published:** 2003-05-14
**Categories:** cs.CC, cond-mat.stat-mech, cs.DM, math.PR
**arXiv:** cs/0305009v2

---

## Abstract

Let F be a random k-SAT formula on n variables, formed by selecting uniformly and independently m = rn out of all possible k-clauses. It is well-known that if r>2^k ln 2, then the formula F is unsatisfiable with probability that tends to 1 as n tends to infinity. We prove that there exists a sequence t_k = O(k) such that if r < 2^k ln 2 - t_k, then the formula F is satisfiable with probability that tends to 1 as n tends to infinity.
  Our technique yields an explicit lower bound for the random k-SAT threshold for every k. For k>3 this improves upon all previously known lower bounds. For example, when k=10 our lower bound is 704.94 while the upper bound is 708.94.

---

## Full Paper

<!-- Page 1 -->

## The Threshold for Random k-SAT is 2<sup>k</sup> log 2 − O(k)

#### Dimitris Achlioptas Microsoft Research, Redmond, WA

#### optas@microsoft.com Yuval Peres<sup>∗</sup>

#### Department of Statistics, University of California, Berkeley, CA peres@stat.berkeley.edu

#### October 26, 2018

Abstract Let F<sub>k</sub>(n, m) be a random k-CNF formula formed by selecting uniformly and independently m out of all possible k-clauses on n variables. It is well-known that if r ≥ 2<sup>k</sup> log 2, then F<sub>k</sub>(n, rn) is unsatisfiable with probability that tends to 1 as n → ∞. We prove that if r ≤ 2<sup>k</sup> log 2 − t<sub>k</sub>, where t<sub>k</sub> = O(k), then F<sub>k</sub>(n, rn) is satisfiable with probability that tends to 1 as n → ∞. Our technique, in fact, yields an explicit lower bound for the random k-SAT threshold for every k. For k ≥ 4 our bounds improve all previously known such bounds.

### 1 Introduction

Call a disjunction of k Boolean variables a k-clause. For a set V of n Boolean variables, let C<sub>k</sub>(V) denote the set of all 2<sup>k</sup>n<sup>k</sup> possible k-clauses on V. A random k-CNF formula F<sub>k</sub>(n,m) is formed by selecting uniformly, independently and with replacement m clauses from C<sub>k</sub> and taking their conjunction<sup>†</sup>. The study of such random k-CNF formulas has attracted substantial interest in logic, optimization, combinatorics, theory of algorithms and, more recently, statistical physics. Say that a sequence of events E<sub>n</sub> occurs with high probability (w.h.p.) if limn→∞P[E<sub>n</sub>] = 1 and with uniformly positive probability if lim infn→∞P[E<sub>n</sub>] > 0. We emphasize that throughout the paper k is arbitrarily large but fixed, while n → ∞. For each k ≥ 2, let

# arXiv:cs/0305009v2 [cs.CC] 8 Sep 2003

r<sub>k</sub> ≡ sup{r : F<sub>k</sub>(n,rn) is satisfiable w.h.p.}, r<sub>k</sub><sup>∗</sup> ≡ inf {r : F<sub>k</sub>(n,rn) is unsatisfiable w.h.p.}.

Clearly, r<sub>k</sub> ≤ r<sub>k</sub><sup>∗</sup>. The Satisfiability Threshold Conjecture asserts that r<sub>k</sub> = r<sub>k</sub><sup>∗</sup> for all k ≥ 3. Our main result establishes an asymptotic form of this conjecture.

Theorem 1 As k → ∞, r<sub>k</sub> = r<sub>k</sub><sup>∗</sup>(1 − o(1)).

As we will see in Section 1.1, a classical and very simple argument gives r<sub>k</sub><sup>∗</sup> ≤ 2<sup>k</sup> log 2. The following theorem implies that this bound is asymptotically tight. The theorem also sharpens the o(1) term in Theorem 1. <sup>∗</sup>Research supported by NSF Grant DMS-0104073, NSF Grant DMS-0244479 and a Miller Professorship at UC Berkeley. Part of this work was done while visiting Microsoft Research. <sup>†</sup>Our results hold in all common models for random k-SAT, e.g., when clause replacement is not allowed. See Section 3.

<!-- Page 2 -->

Theorem 2 There exists a sequence δ<sub>k</sub> → 0 such that for all k ≥ 3,

<sup>k</sup> log 2 r<sub>k</sub> ≥ 2 log 2 − (k + 1) − 1 − δ<sub>k</sub>. 2

Theorem 2 establishes that r<sub>k</sub> ∼ 2<sup>k</sup> log 2, in agreement with the predictions of Monasson and Zecchina [23] based on the “replica method” of statistical mechanics. Like most arguments based on the replica method, the approach in [23] is mathematically sophisticated but far from rigorous. To the best of our knowledge, our result is the first rigorous proof of a replica method prediction for any NP-complete problem at zero temperature.

Obtaining tight bounds for the thresholds r<sub>k</sub>,r<sub>k</sub><sup>∗</sup> is a benchmark problem for a number of analytic and combinatorial techniques of wider applicability [11, 14, 17, 5]. The best bounds prior to our work for general k, from [1] and [9] respectively, differed roughly by a factor of 2:

2<sup>k−1</sup> log 2 − Θ(1) ≤ r<sub>k</sub> ≤ r<sub>k</sub><sup>∗</sup> ≤ 2<sup>k</sup> log 2 − Θ(1).

Traditionally, lower bounds for r<sub>k</sub> have been established by analyzing algorithms for finding satisfying assignments, i.e., by proving in each case that some specific algorithm succeeds w.h.p. on F<sub>k</sub>(n,rn) for r smaller than a certain value. Indeed, until very recently, all lower bounds for r<sub>k</sub> were algorithmic and of the form Ω(2<sup>k</sup>/k). The bound r<sub>k</sub> ≥ 2<sup>k−1</sup> log 2 − Θ(1) from [1], derived via a non-algorithmic argument, was the first to break the 2<sup>k</sup>/k barrier. Our proof of Theorem 2 is also non-algorithmic, based instead on a delicate application of the second moment method. By not going after some particular satisfying truth assignment, as algorithms do, our arguments offer some glimpses of the “geometry” of the set of satisfying truth assignments. Also, the proof yields an explicit lower bound for r<sub>k</sub> for each k ≥ 3. Already for k ≥ 4 this improves all previously known lower bounds for r<sub>k</sub>. Below, we compare our lower bound with the best known algorithmic lower bound [15, 18] and the best known upper bound [10, 9, 19] for some small values of k.

k 3 4 5 7 10 20 21 Upper bound 4.51 10.23 21.33 87.88 708.94 726, 817 1, 453, 635 Our lower bound 2.68 7.91 18.79 84.82 704.94 726, 809 1, 453, 626 Algorithmic lower bound 3.42 5.54 9.63 33.23 172.65 95, 263 181, 453

#### 1.1 Background

Franco and Paull [13], in the early 80’s, observed that r<sub>k</sub><sup>∗</sup> ≤ 2<sup>k</sup> log 2. To see this, fix any truth assignment and observe that a random k-clause is satisfied by it with probability 1 − 2<sup>−k</sup>. Therefore, the expected number of satisfying truth assignments of F<sub>k</sub>(n,rn) is [2(1 − 2<sup>−k</sup>)<sup>r</sup>]<sup>n</sup> = o(1) for r ≥ 2<sup>k</sup> log 2. In 1990, Chao and Franco [3] complemented this by proving that for r < 2<sup>k</sup>/k a simple algorithm, called Unit Clause (uc), finds a satisfying truth assignment with uniformly positive probability. At around the same time, experimental results by Cheeseman, Kanefsky and Taylor [4] and Mitchell, Selman and Levesque [22] suggested that random k-SAT, while a logical model, also behaves like a physical system in the sense that it appears to undergo a phase transition. Perhaps the first statement of the satisfiability threshold conjecture appeared about ten years ago in the work of Chv´atal and Reed [5] who proved r₂ = r₂<sup>∗</sup> = 1 and, by analyzing an extension of uc, established that r<sub>k</sub> ≥ (3/8)2<sup>k</sup>/k. A few years later, Frieze and Suen [15] improved this lower bound to r<sub>k</sub> ≥ c<sub>k</sub>2<sup>k</sup>/k, where limk→∞c<sub>k</sub> = 1.817..., and this remained the best bound for r<sub>k</sub> until recently. In a breakthrough paper, Friedgut [14] proved the existence of a non-uniform threshold.

Theorem 3 (Friedgut [14]) For each k ≥ 2, there exists a sequence r<sub>k</sub>(n) such that for every ǫ > 0, { 1 if r = (1 − ǫ) r<sub>k</sub>(n) lim P[F<sub>k</sub>(n,rn) is satisfiable] = n→∞0 if r = (1 + ǫ) r<sub>k</sub>(n).

<!-- Page 3 -->

As mentioned earlier, in [1], Moore and the first author established r<sub>k</sub> ≥ 2<sup>k−1</sup> log 2 − 1. Independently, Frieze and Wormald [16] proved that if k is allowed to grow with n, in particular if k − log₂ n → +∞, then random k-SAT has a sharp threshold around m = n(2<sup>k</sup> + O(1)) log 2. See [1] for further background. The rest of the paper is organized as follows. In the next section we recall the argument in [1], highlight its main weakness and discuss how we overcome it. Our main idea can be implemented either by a simple weighting scheme or by a more refined large deviations argument. Both approaches yield 2<sup>k</sup> log 2 as the leading term in the lower bound for r<sub>k</sub>. The weighting scheme argument is more compact and technically simpler. However, it gives away a factor of four in the Θ(k) second order term. The large deviations analysis, on the other hand, is tight for our method, up to an additive O(1). We present the weighting scheme argument in Sections 3—6. The additional material for the large deviations argument appears in Sections 7—9. In Section 10 we describe our derivation of explicit lower bounds for small values of k. We conclude with some discussion and open problems in Section 11.

### 2 Outline and heuristics

For any non-negative random variable X one can get a lower bound on P[X > 0] by the following inequality.

Lemma 1 For any non-negative random variable X,

E[X]² P[X > 0] ≥ <sup>2</sup>

. (1)
E[X]

In particular, if X denotes the number of satisfying assignments of a random formula F<sub>k</sub>(n,rn), one can get a lower bound on the probability of satisfiability by applying (1) to X. We will refer to this approach as the “vanilla” application of the second moment method. Indeed, the following immediate corollary of Theorem 3 implies that if P[X > 0] > 1/C for any constant C > 0, then r<sub>k</sub> ≥ r.

Corollary 1 Fix k ≥ 2. If F<sub>k</sub>(n,rn) is satisfiable with uniformly positive probability then r<sub>k</sub> ≥ r.

Thus, if for a given r we have E[X<sup>2</sup>] = O(E[X]²), then r<sub>k</sub> ≥ r. Unfortunately, as we will see, this is never the case: for every constant r > 0, there exists β = β(r) > 0 such that E[X<sup>2</sup>] > (1 + β)<sup>n</sup> E[X]².

#### 2.1 The vanilla second moment method fails

Given a CNF formula F on n variables let S(F) = {σ : σ satisfies F} ⊂ {0, 1}<sup>n</sup> denote the set of satisfying truth assignments of F and let X = X (F) = |S(F)|. Then, for a k-CNF formula with independent clauses c₁,c₂,...,c<sub>m</sub> (

|)  [|] [|]|
|---|---|---|
|2|||
|σ,τ ∈S(F)|σ,τ ∈S(c|)|
|σ,τ|σ,τ c|σ,τ c|

∑ ∑ ∑ ∏ ∑ ∏ E[X<sup>2</sup>] = E  1σ∈S(F)=E 1 = E 1 <sub>i</sub> = E[1σ,τ ∈S(c<sub>i</sub><sub>)</sub>]. (2) σ <sub>i</sub> <sub>i</sub>

We claim that E[1σ,τ ∈S(c<sub>i</sub><sub>)</sub>], i.e., the probability that a fixed pair of truth assignments σ,τ satisfy the ith random clause, depends only on the number of variables z to which σ and τ assign the same value. Specifically, if the overlap of σ and τ is z = αn, we claim that this probability is

P[σ,τ ∈ S(c<sub>i</sub>)] = 1 − 2<sup>1−k</sup> + 2<sup>−k</sup>α<sup>k</sup> ≡ f<sub>S</sub>(α). (3)

This follows by observing that if c<sub>i</sub> is not satisfied by σ, the only way for it to also not be satisfied by τ is for all k variables in c<sub>i</sub> to lie in the overlap of σ and τ. Thus, f<sub>S</sub> quantifies the correlation between σ being satisfying and τ being satisfying as a function of their overlap. In particular, observe that truth assignments with overlap n/2 are uncorrelated since f<sub>S</sub>(1/2) = (1 − 2<sup>−k</sup>)² = P[σ is satisfying]².

<!-- Page 4 -->

1.6
0.965
1.8 1.4
0.96
1.6
0.955 1.2
1.4 0.95 1
0.945 0.8
1.2
0.94
0.6
1 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 α α α E (α) = 1/(α<sup>α</sup>(1 − α)<sup>1−α</sup>) f<sub>S</sub>(α) = 1 − 2<sup>1−k</sup> + α<sup>k</sup> ΛS (α) = 2E (α)f<sub>S</sub>(α)<sup>r</sup>

Figure 1: k = 5, r = 14, 16, 20 (top to bottom).

<sup>n</sup>

( ) n
Since the number of ordered pairs of assignments with overlap z is 2 z we see that (2) and (3) imply

∑ n( n ) E[X<sup>2</sup>] = 2<sup>n</sup> f<sub>S</sub>(z/n)<sup>m</sup>. z=0 z

( ) n
Writing z = αn and using the approximation <sup>α</sup> <sup>1−α</sup> <sup>−n</sup> z = (α (1 − α)) × poly(n) we get ( [ <sup>r</sup>])<sub>n</sub> ()<sub>n</sub> <sup>2</sup> <sup>n</sup> f<sub>S</sub>(α) E[X]≥2 max <sup>α</sup> <sup>1−α</sup> × poly(n) ≡ max ΛS (α) × poly(n). 0≤α≤1 α (1 − α) 0≤α≤1

( <sup>n</sup> <sup>−k</sup> <sup>rn</sup> )₂ Note now that E[X]² = 2 (1 − 2) = (4f<sub>S</sub>(1/2)<sup>r</sup>)<sup>n</sup> = ΛS (1/2)<sup>n</sup>. Therefore, if there exists some α ∈ [0, 1] such that ΛS (α) > ΛS (1/2), then the second moment is exponentially greater than the square of the expectation and we only get an exponentially small lower bound for P[X > 0]. Put differently, unless the dominant contribution to E[X<sup>2</sup>] comes from uncorrelated pairs of satisfying assignments, i.e., pairs with overlap n/2, the second moment method fails. Indeed, for any constant r > 0 this is precisely what happens as the function ΛS is maximized at some α > 1/2. The reason for this is as follows: while the entropic factor E (α) = 1/(α<sup>α</sup>(1 − α)<sup>1−α</sup>) is maximized when α = 1/2, the function f<sub>S</sub> has a positive derivative in (0, 1). Therefore, the derivative of ΛS is never 0 at 1/2, instead becoming 0 only when the correlation benefit balances with the penalty of decreasing entropy at some α > 1/2.

#### 2.2 Random NAE k-SAT and balance

In [1], the second moment method was applied successfully by considering only those satisfying truth assignments whose complement is also satisfying. Observe that this is equivalent to interpreting F<sub>k</sub>(n,m) as an instance of Not All Equal k-SAT, where σ is a solution iff under σ every clause has at least one satisfied literal and at least one unsatisfied literal. In particular, if σ,τ have overlap z = αn and c is a random clause

P[σ,τ NAE-satisfy c] = 1 − 2<sup>2−k</sup> + 2<sup>1−k</sup>(α<sup>k</sup> + (1 − α)<sup>k</sup>) ≡ f<sub>N</sub> (α).

The key point is that f<sub>N</sub> is symmetric around α = 1/2 and, as a result, the product E (α)f<sub>N</sub> (α)<sup>r</sup> always has a local extremum at 1/2. In [1] it was shown that for r ≤ 2<sup>k−1</sup> log 2 − 1 this extremum is a global maximum, implying that for such r, F<sub>k</sub>(n,m) is w.h.p. [NAE-] satisfiable. It is worth noting that for r ≥ 2<sup>k−1</sup> log 2,

w.h.p. F<sub>k</sub>(n,m) is not NAE-satisfiable, i.e., the second moment method determines the NAE-satisfiability threshold within an additive constant. Intuitively, the symmetry of f<sub>N</sub> stems from the fact that NAE-satisfying assignments come in complementary pairs and, thus, having overlap z with an NAE-satisfying assignment σ (and n − z with σ) is indistinguishable from having overlap n − z with σ (and z with σ).

<!-- Page 5 -->

The suspicion motivating this work is that the correlations behind the failure of the vanilla second moment method are mainly due to the following form of populism: satisfying assignments tend to lean towards the majority vote truth assignment. Observe that truth assignments that satisfy many literal occurrences in the random formula have significantly greater probability of being satisfying. At the same time, such assignments are highly correlated since, in order to satisfy many literal occurrences, they tend to agree with each other (and the majority truth assignment) on more than half the variables. Note that our suspicion regarding populism is consistent with the success of the second moment method for random NAE k-SAT. In that problem, since we need to have at least one satisfied and at least one dissatisfied literal in each clause, leaning towards majority is a disadvantage. As intuition suggests, “middle of the road” assignments have the greatest probability of being NAE-satisfying. Alternatively, observe that conditioning on σ being NAE-satisfying does not increase the expected number of satisfied literal occurrences under σ, whereas conditioning on σ being only satisfying increases this expectation by a factor 2<sup>k</sup>/(2<sup>k</sup> − 1) relative to the unconditional expectation km/2. To overcome these correlations, populism must be discouraged and the delicacy with which this is done determines the accuracy of the resulting bound. An example from a different area, which was another inspiration for our work, is the recent proof of the Erd˝os-Taylor conjecture from 1960 for the simple random walk in the planar square lattice (see [12],[7] and for a popular account [24]). The conjecture was that the number of visits to the most frequently visited lattice site in the first n steps of the walk, is asymptotic to (log n)²/π. Erd˝os and Taylor [12] obtained a (sharp) upper bound via an easy calculation of the expectation of the number X<sub>a</sub> of vertices visited at least a(log n)² times. The lower bound they obtained was four times smaller than the conjectured value. In that setting the vanilla second moment method fails, since the events that two vertices u,v are visited frequently are highly correlated. The conjecture was proved in [7] by first recognizing the main source of the correlation in a certain “populism” (when the random walk spends a long time in the smallest disk containing both u and v). Replacing X<sub>a</sub> by a weighted count that discourages such loitering, confirmed that this was indeed the source of excessive correlations as the weighted second moment was successful.

In a nutshell, our plan is to apply the second moment method to balanced satisfying truth assignments,

i.e., truth assignments that satisfy, approximately, half of all km literal occurrences. As it turns out, choosing a concrete range to represent “approximately half” and only counting the satisfying assignments that fall within the range leads to analytic difficulties due to the polynomial corrections in certain large deviations estimates. Fortunately, these issues can be avoided by i) introducing a scheme that weights satisfying truth assignments according to their number of satisfied literal occurrences, and ii) tuning the scheme’s control parameter so as to concentrate the weight on balanced assignments.
#### 2.3 Weighted second moments: a transform

Recall that for a CNF formula F on n variables, S = S(F) ⊆ {0, 1}<sup>n</sup> denotes the set of satisfying truth assignments of F. An attractive feature of the second moment method is that we are free to apply it to any random variable X = X (F) such that X > 0 implies that S = ∅. Sums of the form ∑ X = w(σ,F) σ

clearly have this property if w(σ,F) = 0 for σ ∈ S(F). Weighting schemes as above can be viewed as transforms of the original problem and can be particularly effective in exploiting insights into the source of correlations. In particular, if w(σ,F) has product structure over the clauses, then clause-independence allows one to replace expectations of products with products of expectations. With this in mind, let us consider random variables of the form ∑ ∏ X = w(σ,c), σ c

where w is some arbitrary function. (Eventually, we will require that w(σ,c) = 0 if σ falsifies c.) For instance, if w(σ,c) is the indicator that c is satisfied by σ, then X simply counts the number of satisfying

<!-- Page 6 -->

truth assignments. By linearity of expectation and clause-independence we see that for any function w, ∑ ∏ E[X] = E[w(σ,c)], (4) σ c ∑ ∏ E[X<sup>2</sup>] = E[w(σ,c) w(τ,c)]. (5) σ,τ c

Since we are interested in random formulas where the literals are drawn uniformly, we will restrict attention to functions that are independent of the variable labels. That is, for every truth assignment σ and every clause c = ℓ₁ ∨ · · · ∨ ℓ<sub>k</sub>, we require that w(σ,c) = w(v), where v<sub>i</sub> = +1 if ℓ<sub>i</sub> is satisfied under σ and −1 if ℓ<sub>i</sub> is falsified under σ. With that assumption, (4) and (5) simplify to

E[X] = 2<sup>n</sup> (E[w(σ,c)])<sup>m</sup>, (6) ∑ E[X<sup>2</sup>] = (E[w(σ,c) w(σ,τ)])<sup>m</sup>. (7) σ,τ

Let A = {−1, +1}<sup>k</sup>. Since literals are drawn uniformly and independently we see that for every σ, ∑ E[w(σ,c)] = w(v) 2<sup>−k</sup>. v∈A

Similarly, for every pair of truth assignments σ,τ with overlap z = αn,

∑ ∏k() E[w(σ,c) w(σ,τ)] = w(u)w(v) 2<sup>−k</sup> α¹ ui =vi (1 − α)¹ ui =vi u,v∈A i=1 ∑ ≡ w(u)w(v) Φ<sub>u,v</sub>(α) u,v∈A ≡ f<sub>w</sub>(α). (8)

In particular, observe that E[w(σ,c)]² = f<sub>w</sub>(1/2), i.e., for every function w the weights assigned to truth assignments with overlap n/2 are independent.

( )
Recalling the approximation n z = (α<sup>α</sup>(1 − α)<sup>1−α</sup>)<sup>−n</sup> × poly(n) we see that (7),(8) imply

∑ n( n ) E[X<sup>2</sup>] = 2<sup>n</sup> f<sub>w</sub>(z/n)<sup>m</sup> (9) z=0 z ( [ <sup>r</sup>])<sub>n</sub> <sup>n</sup> f<sub>w</sub>(α) ≤ 2 max <sup>α</sup> <sup>1−α</sup> × poly(n) 0≤α≤1 α (1 − α) ()<sub>n</sub> ≡ max Λ<sub>w</sub>(α) × poly(n). (10) 0≤α≤1

Observe that Λ<sub>w</sub>(1/2)<sup>n</sup> = (4f<sub>w</sub>(1/2)<sup>r</sup>)<sup>n</sup> = E[X]². Moreover, we will see later that a more careful analysis of the sum in (9) allows one to replace the polynomial factor in (10) by O(1). Therefore, if Λ<sub>w</sub>(1/2) is the global maximum of Λ<sub>w</sub> then E[X<sup>2</sup>]/E[X]² = O(1) and the second moment method succeeds. A necessary condition for Λ<sub>w</sub>(1/2) to be a global maximum is that Λ<sup>′w</sup>(1/2) = 0. Since Λ<sub>w</sub>(α) = 2E (α)f<sub>w</sub>(α)<sup>r</sup> and E<sup>′</sup>(1/2) = 0, this dictates f<sub>w</sub><sup>′</sup> (1/2) = 0. Differentiating f<sub>w</sub> we get ∑ f<sub>w</sub><sup>′</sup> (α) = w(u)w(v) Φ<sub>u,v</sub>(α) [ log Φ<sub>u,v</sub>(α)]<sup>′</sup> u,v∈A ∑ ∑ k( 1 u =v1u =v ) = w(u)w(v) Φ<sub>u,v</sub>(α) i <sub>i</sub> − i <sub>i</sub>. i=1 α 1 − α u,v∈A

<!-- Page 7 -->

In particular, letting u · v denote the inner product of u and v, we see that () () ∑ ∑ ∑ f<sub>w</sub><sup>′</sup> (1/2) = 2<sup>−2k+1</sup> w(u)w(v) u · v = 2<sup>−2k+1</sup> w(u)u · w(v)v. (11) u,v∈A u∈A v∈A

Therefore, for any function w ∑ f<sub>w</sub><sup>′</sup> (1/2) = 0 ⇐⇒ w(v)v = 0. (12) v∈A We can interpret the vanilla application of the first moment method as using a function w = w<sub>S</sub> which assigns 0 to ( ∑ −1,..., −1) and 1/(2<sup>k</sup> − 1) to all other vectors. (It is convenient to always normalize w so that <sub>v</sub> w(v) = 1.) The fact that w<sub>S</sub> violates the r.h.s. of (12), implies that this attempt must fail. In [1], on the
other hand, w = w<sub>N</sub> assigns 0 both to (−1,..., −1) and to (+1,..., +1) (and 1/(2<sup>k</sup> − 2) to all other vectors),
thus satisfying (12) and enabling the second moment method. Nevertheless, this particular rebalancing of the vectors is rather heavy-handed since it makes it is twice as likely to assign zero to a random clause. To achieve better results we would like to choose a function w that is “as close as possible” to w<sub>S</sub> while satisfying (12). That is, we would like w to have minimal relative entropy with respect to w<sub>S</sub> subject to (12) (see Definition 2.15 of [8]). Since w<sub>S</sub> is constant over all v = (−1,..., −1) and we
must have w(−1,..., −1) = w<sub>S</sub>(−1,..., −1) = 0, this means that w should have maximum entropy over
v = (−1,..., −1) while satisfying (12). So, all in all, we are seeking a maximum-entropy collection of weights for the vectors in A such that i) the all -1s vector has weight 0, ii) the weighted vectors cancel out. For x ∈ A, let |x| denote the number of +1s in x. By summing the r.h.s. of (12) over the coordinates we see that a necessary condition for the optimality of w is ∑ w(v)(2|v| − k) = 0. (13) v=(−1,...,−1)

Maximizing entropy subject to (13) is a standard Lagrange multipliers problem. Its unique solution is

1|v| w(v) = λ, (14) Z

where Z is a normalizing constant and λ satisfies (1 + λ)<sup>k−1</sup> = 1/(1 − λ) so that (13) is satisfied, i.e.,

∑ k( k ) () λ (2j − k) = k j 1 − (1 + λ)<sup>k−1</sup>(1 − λ) = 0. (15) j=1 j ∑ Note now that for w given by (14), symmetry ensures that all coordinates of <sub>v</sub> w(v)v are equal. Since, by (15), the sum over these coordinates vanishes, we see that in fact (12) must hold as well. Therefore, w is indeed the optimal solution for our original problem. We plot below the functions ∑ f<sub>w</sub> and Λ<sub>w</sub> corresponding to this weighting, for the values of k,r in Figure 1. (With a normalization for <sub>u</sub> w(u) which makes the plot scale analogous to that in Figure 1 and which will be more convenient for computing f<sub>w</sub> and Λ<sub>w</sub> in the next section.)

In conclusion, if L(σ,F) denotes the number of satisfied literal occurrences in F under σ, we will take ∏ w(σ,F) ∝ λ<sup>L(σ,c)</sup>1σ∈S(c), (16) c

where (1 + λ)<sup>k−1</sup> = 1/(1 − λ). The above weighting scheme yields Theorem 4, below, which we will prove in Sections 3—6. Theorem 4 has the same leading term as Theorem 2 but a linear correction term 4 times greater. This lost factor of 4 is due to our insistence that w(σ,F) factorizes perfectly over the clauses. In Sections 7—9 we go beyond what can be achieved with perfect factorization by performing a truncation. This will allow us to prove Theorem 2 which gives a lower bound for r<sub>k</sub> that is within an additive constant of the upper bound for the existence of balanced satisfying assignments.

<!-- Page 8 -->

0.965 1.4
0.96
1.2
0.955
0.95 1
0.945
0.8
0.94
0.935 0.6 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1
α α f<sub>w</sub>(α) Λ<sub>w</sub>(α) = 2E (α)f<sub>w</sub>(α)<sup>r</sup>

Figure 2: k = 5, r = 14, 16, 20 (top to bottom).

Theorem 4 There exists a sequence β<sub>k</sub> → 0 such that for all k ≥ 3,

r<sub>k</sub> ≥ 2<sup>k</sup> log 2 − 2(k + 1) log 2 − 1 − β<sub>k</sub>.

### 3 Groundwork

Given a k-CNF formula F on n variables, recall that S(F) is the set of satisfying truth assignments of F. Given σ ∈ {0, 1}<sup>n</sup> let H = H (σ,F) be the number of satisfied literal occurrences in F under σ less the number of unsatisfied literal occurrences in F under σ. For any 0 < γ ≤ 1, let ∑ X = γ<sup>H(σ,F)</sup>1σ∈S(F). σ

(Note that γ<sup>H(σ,F)</sup> = γ 2S(σ,F)−km, so this is consistent with (16) for γ² = λ.) Recall that in F<sub>k</sub>(n,m) the m clauses {c<sub>i</sub>}<sup>m</sup>i=1are i.i.d. random variables, c<sub>i</sub> being the conjunction of k

i.i.d. random variables {ℓ<sub>ij</sub>}<sup>k</sup>j=1, each ℓ<sub>ij</sub> being a uniformly random literal. Clearly, in this model a clause may be improper, i.e., it might contain repeated and/or contradictory literals. At the same time, though, observe that the probability that a random clause is improper is smaller than k²/n and, moreover, the proper clauses are uniformly selected among all proper clauses. Therefore w.h.p. the number of improper clauses is o(n) implying that if for a given r, F<sub>k</sub>(n,rn) is satisfiable w.h.p. then for m = rn − o(n), the same is true in the model where we only select among proper clauses. The issue of selecting clauses without replacement is completely analogous as w.h.p. there are o(n) clauses that contain the same k variables as some other clause.
#### 3.1 The first moment

For any fixed truth assignment σ and a random k-clause c = ℓ₁ ∨ · · · ∨ ℓ<sub>k</sub>, since the literals ℓ₁,...,ℓ<sub>k</sub> are

i.i.d. we have
E[γ<sup>H(σ,c)</sup>1σ∈S(c)] = E[γ<sup>H(σ,c)</sup>] − E[γ<sup>−k</sup>1σ∈S(c)] [] ∏ = E γ<sup>H(σ,ℓ</sup><sup>i</sup> ) − (2γ)<sup>−k</sup> ℓ<sub>i</sub> ( <sup>−1</sup> )<sub>k</sub> γ + γ = − (2γ)<sup>−k</sup> 2 ≡ ψ(γ).

<!-- Page 9 -->

Thus, since the m = rn clauses c₁,c₂,...,c<sub>m</sub> are i.i.d. [] ∑ E[X] = E γ<sup>H(σ,F)</sup>1σ∈S(F)

<sup>σ</sup>[] ∑ ∏ = E γ<sup>H(σ,c</sup><sup>i</sup><sup>)</sup>1σ∈S(c<sub>i</sub>) σ c<sub>i</sub> ∑ ∏ [] = E γ<sup>H(σ,c</sup><sup>i</sup><sup>)</sup>1σ∈S(c<sub>i</sub>) σ c<sub>i</sub> = (2ψ(γ)<sup>r</sup>)<sup>n</sup>. (17)

#### 3.2 The second moment

Let σ,τ be any pair of truth assignments that agree on z = αn variables. If ℓ₁,ℓ₂,...ℓ<sub>k</sub> are i.i.d. uniformly random literals and c = ℓ₁ ∨ ℓ₂ ∨ · · · ∨ ℓ<sub>k</sub> then ( γ₂) [] )+H(τ,ℓ<sub>i</sub>)+ γ<sup>−2</sup> E γ<sup>H(σ,ℓ</sup><sup>i</sup> = α + 1 − α, 2 [] () )+H(τ,ℓ<sub>i</sub> E γ<sup>H(σ,ℓ</sup><sup>i</sup><sup>)</sup>1σ∈S(c)= 2<sup>−k</sup> αγ<sup>−2</sup> + (1 − α), [] () )+H(τ,ℓ<sub>i</sub> E γ<sup>H(σ,ℓ</sup><sup>i</sup><sup>)</sup>1σ,τ ∈S(c)= 2<sup>−k</sup> αγ<sup>−2</sup>.

Since ℓ₁,ℓ₂,...ℓ<sub>k</sub> are i.i.d., writing γ² = 1 − ε, we have [] [ ()] H(σ,c)+H(τ,c) H(σ,c)+H(τ,c) E γ 1σ,τ ∈S(c)= E γ 1−1σ∈S(c)− 1τ ∈S(c)+ 1σ,τ ∈S(c) [] ∏<sub>)</sub>() )+H(τ,ℓ<sub>i</sub> = E γ<sup>H(σ,ℓ</sup><sup>i</sup> 1−1σ∈S(c)− 1τ ∈S(c)+ 1σ,τ ∈S(c) i ( ())<sub>k</sub> γ² + γ<sup>−2</sup> ()<sub>k</sub> ()<sub>k</sub> = α + 1 − α − 2<sup>1−k</sup> αγ<sup>−2</sup> + (1 − α) + 2<sup>−k</sup> αγ<sup>−2</sup> 2 (2 − 2ε + αε²)<sup>k</sup> − 2(1 − ε + αε)<sup>k</sup> + α<sup>k</sup> = (18) 2 (1 − ε)k <sup>k</sup>

f (α) ≡, (19) 2 (1 − ε)k <sup>k</sup>

where the dependence of f on ε = 1 − γ² is implicit. (Taking ε = 1 − λ in (18) yields the f<sub>w</sub> of Figure 2.) Thus, for a random k-CNF formula whose m = rn clauses c₁,c₂,...,c<sub>m</sub> are constructed independently []₂ ∑ E[X<sup>2</sup>] = E γ<sup>H(σ,F)</sup>1σ∈S(F)

∑ <sup>σ</sup>[] H(σ,F)+H(τ,F) = E γ 1σ,τ ∈S(F) σ,τ [] ∑ ∏ )+H(τ,c<sub>i</sub> = E γ<sup>H(σ,c</sup><sup>i</sup><sup>)</sup>1σ,τ ∈S(c<sub>i</sub>) σ,τ c<sub>i</sub> ∑ ∏ [] )+H(τ,c<sub>i</sub> = E γ<sup>H(σ,c</sup><sup>i</sup><sup>)</sup>1σ,τ ∈S(c<sub>i</sub>). (20) σ,τ c<sub>i</sub>

<!-- Page 10 -->

( ) n
Since the number of ordered pairs of assignments with overlap z is 2<sup>n</sup> and since the m = rn clauses z are identically distributed, (20) and (19) imply n()()<sub>rn</sub> ∑ n f (z/n) E[X<sup>2</sup>] = 2<sup>n</sup>. (21) z 2 (1 − ε)k <sup>k</sup> z=0

Observe now that for, any fixed value of ε, f<sup>r</sup> is a real, positive and twice-differentiable. Thus, to bound the sum in (21) we can use the following lemma of [1]. The idea is that sums of these type are dominated by the contribution of Θ(n<sup>1/2</sup>) terms around the maximum term and the proof follows by applying the Laplace method of asymptotic analysis [6].

Lemma 2 Let φ be any real, positive, twice-differentiable function on [0, 1] and let n() ∑ n S<sub>n</sub> = φ(z/n)<sup>n</sup>. z z=0

Letting 0<sup>0</sup> ≡ 1, define g on [0, 1] as φ(α) g(α) =. α<sup>α</sup> (1 − α)<sup>1−α</sup>

If there exists α<sub>max</sub> ∈ (0, 1) such that g(α<sub>max</sub>) ≡ g<sub>max</sub> > g(α) for all α = α<sub>max</sub>, and g<sup>′′</sup>(α<sub>max</sub>) < 0, then there exist constants B,C > 0 such that for all sufficiently large n

B × g<sub>max</sub><sup>n</sup> ≤ S<sub>n</sub> ≤ C × g<sub>max</sub><sup>n</sup>.

With Lemma 2 in mind, let us define

f (α)<sup>r</sup> g<sub>r</sub>(α) =. (22) α<sup>α</sup>(1 − α)<sup>1−α</sup>

Let s<sub>k</sub> = 2<sup>k</sup> log 2 − 2 log 2(k + 1) − 1 − 3/k.

We will prove that

Lemma 3 Let ε be such that ε(2 − ε)<sup>k−1</sup> = 1. (23)

For all k ≥ 22, if r ≤ s<sub>k</sub> then g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α = 1/2, and g<sub>r′′</sub>(1/2) < 0.

As a result, for r,k,ε as in Lemma 3 we have ()<sub>n</sub> 2g<sub>r</sub>(1/2) E[X<sup>2</sup>] < C ×, (24) (2(1 − ε))<sup>kr</sup>

where C = C(k) is independent of n. Observe now that (17) and the fact γ² = 1 − ε imply

E[X]² = [(2ψ(γ)<sup>r</sup>)<sup>n</sup>]² ()<sub>rn</sub> f (1/2) = 4<sup>n</sup> 2 (1 − ε)k <sup>k</sup> ()<sub>n</sub> 2g<sub>r</sub>(1/2)<sup>n</sup> =. (25) (2(1 − ε))<sup>kr</sup>

Therefore, by (24) and (25) we see that for r,k,ε as in Lemma 3 we have

##### E[X<sup>2</sup>] < C × E[X]².

<!-- Page 11 -->

By Lemma 1, this implies P[X > 0] > 1/C and, hence, Lemma 3 along with Corollary 1 imply Theorem 4.

To prove Lemma 3 we will prove the following three lemmata. The first lemma holds for any ε ∈ [0, 1) and reduces the proof to the case α ≥ 1/2. The second lemma controls the behavior of f (and thus g<sub>r</sub>) around α = 1/2 and demands the judicious choice of ε specified by (23). We note that this is the only value of ε for which g<sub>r</sub> has a local maximum at 1/2, for any r > 0. The third lemma deals with α near 1. That case needs to be handled separately because g<sub>r</sub> has another local maximum in that region. The condition r ≤ s<sub>k</sub> aims precisely at keeping the value of g<sub>r</sub> at this other local maximum smaller than g<sub>r</sub>(1/2).

Lemma 4 For all ε,x > 0, g<sub>r</sub>(1/2 + x) > g<sub>r</sub>(1/2 − x).

Lemma 5 Let ε satisfy (23). For all k ≥ 22, if r ≤ 2<sup>k</sup> log 2 then g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α ∈ (1/2, 4/5] and g<sub>r′′</sub>(1/2) < 0.

Lemma 6 Let ε satisfy (23). For all k ≥ 22, if r ≤ s<sub>k</sub> then g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α ∈ (4/5, 1].

The following bound will be useful. If ε satisfies (23), then

2<sup>1−k</sup> + k4<sup>−k</sup> < ε < 2<sup>1−k</sup> + 3k4<sup>−k</sup>. (26)

To prove (26) let q(x) = x − 1/(2 − x)<sup>k−1</sup> and observe that for all k ≥ 3, the quantity q(2<sup>1−k</sup> + ck4<sup>−k</sup>) is negative for c = 1 but positive for c = 3.

### 4 Proof of Lemma 4

Observe that α<sup>α</sup>(1 − α)<sup>1−α</sup> is symmetric around 1/2 and that r > 0. Therefore, it suffices to prove that f (1/2 + x) > f (1/2 − x), for all x > 0. To do this we first note that for all x = 0,

<sup>k</sup> ()<sub>k</sub> 2 f (1/2 + x) = (2 − ε)² + 2xε² − 2 (2 − ε + 2xε)<sup>k</sup> + (1 + 2x)<sup>k</sup>

∑ k( k ) [] = (2 − ε)<sup>2(k−j)</sup>(2xε²)<sup>j</sup> − 2(2 − ε)<sup>k−j</sup>(2xε)<sup>j</sup> + (2x)<sup>j</sup> j=0 j

∑ k( k ) [] = (2x)<sup>j</sup> (2 − ε)<sup>2(k−j)</sup>ε<sup>2j</sup> − 2(2 − ε)<sup>k−j</sup>ε<sup>j</sup> + 1 j=0 j

∑ k( k ) = (2x)<sup>j</sup>[(2 − ε)<sup>k−j</sup>ε<sup>j</sup> − 1]². (27) j=0 j

Thus, for all x > 0,

∑ k( k ) f (1/2 + x) − f (1/2 − x) = 2<sup>−k</sup> 2<sup>j</sup>[(2 − ε)<sup>k−j</sup>ε<sup>j</sup> − 1]²(x<sup>j</sup> − (−x)<sup>j</sup>) > 0. j=0 j

### 5 Proof of Lemma 5

We will prove that for all k ≥ 22 and r ≤ 2<sup>k</sup> log 2, g<sub>r</sub> is strictly decreasing in (1/2, 4/5]. We have

<sup>′</sup> [ <sup>k−1</sup> <sup>k−1</sup> <sup>k−1</sup>] f (α) = k (2 − 2ε + αε²) ε² − 2(1 − ε + αε) ε + α,

f (α)<sup>r−1</sup> (rf<sup>′</sup>(α) + f (α)(log(1 − α) − log α)) g<sub>r′</sub> (α) = <sup>α</sup> <sup>1−α</sup>

. (28)
α (1 − α)

<!-- Page 12 -->

<sup>′</sup> <sup>−k+1</sup> ( <sup>k−1</sup> )₂ So, f (1/2) = k2 (2 − ε) ε − 1 and since, by (23), we have (2 − ε)<sup>k−1</sup>ε = 1 we get

g<sub>r′</sub> (1/2) = f<sup>′</sup>(1/2) = 0. (29)

Since g<sub>r′</sub> (1/2) = 0 and, by (27), f (α) > 0 for all α we see that (28) implies that to prove that g<sub>r</sub> is decreasing in (1/2, 4/5] it suffices to prove that the derivative of

rf<sup>′</sup>(α) + f (α)(log(1 − α) − log α) (30)

is negative in (1/2, 4/5]. We will actually prove this claim for α ∈ [1/2, 4/5]. Since f<sup>′</sup>(1/2) = 0 this also establishes our claim that g<sub>r′′</sub>(1/2) < 0. The derivative of (30) is () <sup>′′</sup> <sup>′</sup> 1 1 rf (α) + f (α)(log(1 − α) − log α) − f (α) +. (31) α 1 − α

By considering (27), we see that f is non-decreasing in [1/2, 1]. Since log(1 − α) ≤ log α for α ∈ [1/2, 1), it follows that in order to prove that the expression in (31) is negative it suffices to show that () <sup>′′</sup> 1 1 rf (α) ≤ f (α) +. α 1 − α

Since, by definition, ε < 1 it follows that αε² ≤ 2ε implying that we can bound f<sup>′′</sup> as

<sup>′′</sup> ( <sup>k−2</sup> <sup>k−2</sup> <sup>k−2</sup> ) f (α) = k(k − 1) (2 − 2ε + αε²) ε⁴ − 2(1 − ε + αε) ε² + α ( <sup>k−2</sup> <sup>k−2</sup> ) ≤ k² 2 ε⁴ + (4/5). (32)

At the same time, 1/α + 1/(1 − α) ≥ 4 and f (α) ≥ f (1/2) = 2<sup>−k</sup>((2 − ε)<sup>k</sup> − 1)². Therefore, if ε<sub>u</sub> is any upper bound on ε it suffices to establish ( <sup>k−2</sup> <sup>k−2</sup> ) r × k² 2 ε⁴<sub>u</sub> + (4/5) ≤4×2<sup>−k</sup>((2 − ε<sub>u</sub>)<sup>k</sup> − 1)². (33)

Invoking (26) to take ε<sub>u</sub> = 2<sup>1−k</sup> + 3k4<sup>−k</sup>, it is easy to verify that (33) holds for k ≥ 22 and r = 2<sup>k</sup> log 2.

Corollary 2 For all k ≥ 65, if r ≤ 2<sup>k</sup> log 2 then g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α ∈ (1/2, 9/10] and g<sub>r′′</sub>(1/2) < 0.

Proof. If in (33) we replace 4/5 with 9/10 and take r = 2<sup>k</sup> log 2, then the inequality is valid for all k ≥ 65.

### 6 Proof of Lemma 6

First observe that the inequality g<sub>r</sub>(1/2) > g<sub>r</sub>(α) is equivalent to ()<sub>r</sub> f (α) < 2α<sup>α</sup>(1 − α)<sup>1−α</sup>. (34) f (1/2)

Recall now that, by (27), f is increasing in (1/2, 1] implying f (α) − f (1/2) > 0 and that for all x ≥ 0, log(1 + x) ≤ x. Thus, the logarithm of the left hand side above can be bounded as () () f (α) f (α) − f (1/2) r log = r log 1 + f (1/2) f (1/2) () f (α) − f (1/2) ≤ r. f (1/2)

<!-- Page 13 -->

So, if we let h(α) = −α log α − (1 − α) log(1 − α) we see that (34) holds if

f (1/2) r < (log 2 − h(α)) ×. f (α) − f (1/2)

To get a lower bound on f (1/2) we use the upper bound for ε from (26), yielding

f (1/2) = (2 − 2ε + ε²/2)<sup>k</sup> − 2(1 − ε/2)<sup>k</sup> + (1/2)<sup>k</sup> > (2(1 − ε))<sup>k</sup> − 2 > 2<sup>k</sup>(1 − kε) − 2 > 2<sup>k</sup>(1 − k(2<sup>1−k</sup> + 3k4<sup>−k</sup>)) − 2 = 2<sup>k</sup> − 2k − 2 − 3k²2<sup>−k</sup>. (35)

To get an upper bound on f (α) − f (1/2) we let α = 1/2 + x and consider the sum in (27). By our choice of ε in (23) we see that: i) the term corresponding to j = 1 vanishes yielding (36), and ii) for all j > 1, 0 < (2 − ε)<sup>k−j</sup>ε<sup>j</sup> < 1 yielding (37). That is,

k() ∑ k f (1/2 + x) = f (1/2) + 2<sup>−k</sup> (2x)<sup>j</sup>[(2 − ε)<sup>k−j</sup>ε<sup>j</sup> − 1]² (36) j j=2 k() ∑ k ≤ f (1/2) + 2<sup>−k</sup> (2x)<sup>j</sup> (37) j j=0 = f (1/2) + α<sup>k</sup>. (38)

Therefore, we see that (34) holds as long as

log 2 − h(α) r ≤ × f (1/2) ≡ φ(α) × f (1/2). α<sup>k</sup>

We start by getting a lower bound for φ for all α ∈ (1/2, 1]. For that, we let y = 1 − α and observe that for all 0 < y ≤ 1/2 −h(1 − y) > log(1 − y) + y log y > −y − y² + y log y (39)

and 1 > (1 + y)<sup>k</sup> > 1 + ky. (1 − y)<sup>k</sup>

Therefore,

log 2 − h(1 − y) φ(1 − y) = (1 − y)<sup>k</sup> > (1 + ky)(log 2 − y(1 + y − log y)). (40)

Writing y = d/2<sup>k</sup> and substituting into (40) we get that for all 1/2 ≤ α < 1,

φ(α) = φ(1 − d2<sup>−k</sup>) ()( ()) > 1 + kd2<sup>−k</sup> log 2 − d2<sup>−k</sup> 1 + d2<sup>−k</sup> − log(d2<sup>−k</sup>) d² ( ()) = log 2 + d(log d − 1)2<sup>−k</sup> − 1 + k 1 + d2<sup>−k</sup> − log(d2<sup>−k</sup>) 4<sup>k</sup> d² ( ()) ≥ log 2 − 2<sup>−k</sup> − 1 + k 1 + d2<sup>−k</sup> − log(d2<sup>−k</sup>) 4<sup>k</sup> = log 2 − 2<sup>−k</sup> − (1 − α)² (1 + k (2 − α − log(1 − α))) ≡ b(α). (41)

<!-- Page 14 -->

Since φ is differentiable, to bound it in (4/5, 1] it suffices to consider its value at 4/5, 1 and wherever

<sup>′</sup> α log α − α log(1 − α) − k log 2 + kh(α) φ (α) = <sup>k+1</sup> = 0. (42) α

We start by observing that for k ≥ 6 φ<sup>′</sup>(4/5) < 0.

At the other end, we see that φ<sup>′</sup>(α) lim = −1, α→1 log(1 − α)

implying that the derivative of φ becomes positively infinite as we approach 1. Therefore, we can limit our search to the interior of (4/5, 1) for k ≥ 6. By setting φ<sup>′</sup> to zero, (42) gives

k log 2 − kh(α) log(1 − α) = log α − α

which, since 1/2 < α < 1, implies

log(1 − α) ≤ −k(log 2 − h(α)). (43)

Moreover, since log 2 − h(4/5) > 1/6, we see that (43) implies α > 1 − e<sup>−k/6</sup> for all k. Note now that if α > 1 − e<sup>−ck</sup> for any c > 0 then (39) implies h(α) < e<sup>−ck</sup>(1 + e<sup>−ck</sup> + ck). Since α > 1 − e<sup>−k/6</sup>, we thus get

h(α) < e<sup>−k/6</sup>(1 + e<sup>−k/6</sup> + k/6) < e<sup>−k/6</sup>(2 + k/6) ≡ Q(k). (44)

Plugging (44) into (43), we conclude that

α > 1 − e −k(log 2−Q(k)) ≡ α<sup>∗</sup><sub>k</sub>. (45)

Since for k ≥ 12 we have α<sup>∗</sup><sub>k</sub> > 4/5, this means that φ is decreasing in (4/5,α<sup>∗</sup><sub>k</sub>] for k ≥ 12. Note now that the function b bounding φ from below in (41) is increasing in [0, 1]. Combined with the fact that φ is decreasing in (4/5,α<sup>∗</sup><sub>k</sub>] this implies that b(α<sup>∗</sup><sub>k</sub>) is a lower bound for φ in (4/5, 1], i.e.,

φ(α) > b(α<sup>∗</sup><sub>k</sub>) > log 2 − 2<sup>−k</sup> − 2/(k2<sup>k</sup>), (46)

where (46) holds for all k ≥ 22. Combining (46) with (35), we get that for all k ≥ 22 if

r < 2<sup>k</sup> log 2 − 2 log 2(k + 1) − 1 − 3/k

then g(1/2) > g(α) for all α = 1/2.

### 7 Further refinement: truncation and weighting

Given a k-CNF formula F on n variables, recall that S = S (F ) ⊆ {0, 1}<sup>n</sup> is the set of satisfying truth assignments of F. Recall also that for σ ∈ {0, 1}<sup>n</sup>, by H (σ,F) we denote the number of satisfied literal occurrences in F under σ less the number of unsatisfied literal occurrences. Let S<sup>+</sup> = {σ ∈ S : H (σ,F) ≥ 0}. For any 0 < γ ≤ 1 let ∑ X = γ<sup>H(σ,F)</sup>, σ∈S ∑ X<sub>+</sub> = γ<sup>H(σ,F)</sup>. σ∈S<sup>+</sup>

<!-- Page 15 -->

In computing the second moment of X in the previous sections, it becomes clear that one needs to control the contribution to E[X<sup>2</sup>] from pairs of truth assignments with high overlap. Close examination of these pairs shows that the dominant contributions come from those pairs amongst them that have fewer than half of their literals satisfied. If we compute the second moment of X<sub>+</sub> instead, these highly correlated pairs are avoided. Our argument for this is motivated by Cramer’s classical “change of measure” technique in large deviation theory.

Specifically, let ε₀ < 1 satisfy 1 ε₀ = <sup>k−1</sup>

. (47)
(2 − ε₀)

Lemma 7 below asserts that if γ² = 1 − ε₀, where ε₀ is specified by (47), then the first moments of X and X<sub>+</sub> are comparable.

Lemma 7 If γ² = 1 − ε₀ then as n → ∞

E[X<sub>+</sub>] → 1/2. E[X]

Let σ,τ be any pair of truth assignments that agree on z = αn variables. If we write θ² = 1 − ε then from (18) we have

[] (2 − 2ε + αε²)<sup>k</sup> − 2(1 − ε + αε)<sup>k</sup> + α<sup>k</sup> E θ H(σ,c)+H(τ,c) 1σ,τ ∈S(c)= k <sup>k</sup> 2 (1 − ε) ≡ f (α,ε). (48)

(Observe that the function f (α,ε) in (48) above is identical to f (α)(2(1 − ε))<sup>−k</sup>, where f (α) is as in (19). In the earlier sections, since ε was fixed, this dependence on ε was suppressed to simplify notation.) Thus, if F is a random formula consisting of m = rn independent clauses then for any θ² = 1 − ε ≥ γ<sup>2</sup>, [] [] E γ H(σ,F)+H(τ,F) 1σ,τ ∈S<sup>+</sup>(F)≤ E θ H(σ,F)+H(τ,F) 1σ,τ ∈S<sup>+</sup>(F) [] ≤ E θ H(σ,F)+H(τ,F) 1σ,τ ∈S(F)

= f (α,ε)<sup>m</sup>. (49)

The crucial point is that (49) holds for any ε ≤ 1 − γ<sup>2</sup>, allowing us to optimize ε with respect to α. In particular if γ² = 1 − ε₀ then (49) implies

[] []<sub>m</sub> E γ H(σ,F)+H(τ,F) 1σ,τ ∈S<sup>+</sup>(F)≤ inf f (z/n,ε). ε≤ε₀

Thus, following the derivation of (21), we deduce that

∑ n( n )[]<sub>rn</sub> E[X²<sub>+</sub>]≤2<sup>n</sup> inf f (z/n,ε). (50) z ε≤ε₀ z=0

Let us define f<sup>r</sup>(α,ε) g<sub>r</sub>(α,ε) = <sup>α</sup> <sup>1−α</sup>. α (1 − α)

Observe that by Lemma 7 and (25),

3E[X<sub>+</sub>]² > E[X]² = g<sub>r</sub>(1/2,ε₀)<sup>n</sup>. (51)

Assume now that there exists a piecewise-constant function ξ such that for some value of r we have g<sub>r</sub>(1/2,ε₀) > g<sub>r</sub>(α,ξ(α)) for all α = 1/2. Then, by decomposing the sum in (50) along the pieces of ξ and

<!-- Page 16 -->

applying Lemma 2 to each piece, we can conclude that E[X²<sub>+</sub>] < C × E[X<sub>+</sub>]², for some C = C(k). Lemma 1 and Corollary 1 then imply r<sub>k</sub> ≥ r. Let <sup>k</sup> log 2 ρ<sub>k</sub> = 2 log 2 − (k + 1) − 1 − 50k³ 2<sup>−k</sup>. 2 We will prove

Lemma 8 Let   ε⁰ if α ∈ [1/10, 9/10] ξ(α) =   ε₀/2 otherwise.

For all k ≥ 166, if r ≤ ρ<sub>k</sub> then g<sub>r</sub>(1/2,ε₀) > g<sub>r</sub>(α,ξ(α)) for all α = 1/2, and the second derivative of g<sub>r</sub> with respect to α is negative at α = 1/2.

To prove Lemma 8 we first observe that since ξ is symmetric around 1/2, Lemma 4 implies that we only

|need to consider the case α ≥ 1/2.|Also, since ξ(α) = ε₀ for α ∈ [1/2, 9/10], Corollary 2 establishes both|||
|---|---|---|---|
|our claim regarding the second derivative of g Thus, besides Lemma 7, it suffices to prove that||(1/2,ε₀) > g|(α,ξ(α)) for α ∈ (1/2, 9/10].|
|Lemma 9 For all k ≥ 166, if r ≤ ρ|then for all α ∈ (9/10, 1] g|(1/2,ε₀) > g|(α,ε₀/2).|

<sub>r</sub> at α = 1/2 and g<sub>r</sub> <sub>r</sub>

<sub>k</sub> <sub>r</sub> <sub>r</sub>

### 8 Proof of Lemma 7

By linearity of expectation, it suffices to prove that for γ² = 1 − ε₀ and every σ

E[γ<sup>H(σ,F)</sup>1σ∈S<sup>+</sup><sub>(F)</sub>] 1 <sup>H(σ,F)</sup> →. (52) E[γ 1σ∈S(F)] 2

Recalling that formulas in our model are sequences of i.i.d. random literals ℓ₁,...,ℓ<sub>km</sub>, let P(·) denote the probability assigned by our distribution to any such sequence, i.e., (2n)<sup>−km</sup>. Now, fix any truth assignment σ and consider an auxiliary distribution P<sub>γ</sub> on k-CNF formulas where the km literals are again i.i.d., but where now for each fixed literal ℓ γ P<sub>γ</sub>[H (σ,ℓ) = 1] = <sup>−1</sup>. γ + γ

Observe that since γ ≤ 1 this probability is at most 1/2. Thus,

γ − γ<sup>−1</sup> γ² − 1 −ε₀ E<sub>γ</sub>[H (σ,ℓ)] = <sup>−1</sup> = =. γ + γ γ² + 1 2 − ε₀

##### So, for a random k-clause c

E<sub>γ</sub>[H (σ,c)1σ∈S(c)] = E<sub>γ</sub>[H (σ,c)] − E<sub>γ</sub>[−k1σ∈S(c)] ( <sup>−1</sup> )<sub>k</sub> −kε₀ γ = + k 2 − ε₀ γ + γ<sup>−1</sup> ( () ) k ε₀ 1 = k − +. 2 − ε₀ 2 − ε₀

Since ε₀ = 1/(2 − ε₀)<sup>k−1</sup> we see that E<sub>γ</sub>[H (σ,c)1σ∈S(c)] = 0. By literal independence, for any specific clause c₀

γ<sup>H(σ,c</sup><sup>0</sup><sup>)</sup>P(c₀) P<sub>γ</sub>(c₀) = <sup>−1</sup> <sup>k</sup>

. (53)
(γ + γ)

<!-- Page 17 -->

Let Z(γ) = E<sub>γ</sub>[1σ∈S(c)] and Z₁(γ) = Z(γ)(γ + γ<sup>−1</sup>)<sup>k</sup>. For any clause c₀, define

H(σ,c₀ <sub>γ</sub>(c₀)1σ∈S(c₀)<sup>)</sup>P(c₀)1σ∈S(c₀) P˜<sub>γ</sub>(c₀) = P = γ, (54) Z(γ) Z₁(γ)

where the second equality follows from (53). Now pick m i.i.d. clauses with the distribution in (54). Any fixed formula F₀ will be obtained with probability

H(σ,F₀ <sup>)</sup>P(F₀)1σ∈S(F₀) P˜ <sub>γ</sub>(F₀) = γ. (55) Z₁(γ)<sup>m</sup>

Since Ẽ<sub>γ</sub>[H (σ,c)] = 0, the central limit theorem yields,

P˜ <sub>γ</sub>[H (σ,F) ≥ 0] → 1 2

as n → ∞. By (55), this is equivalent to (52).

### 9 Proof of Lemma 9

Write ε₁ = ε₀/2 (to simplify notation). Observe that the inequality g<sub>r</sub>(1/2,ε₀) > g<sub>r</sub>(α,ε₁) is equivalent to ()<sub>r</sub> f (α,ε₁) < 2α<sup>α</sup>(1 − α)<sup>1−α</sup>. (56) f (1/2,ε₀)

If h(α) = −α log α − (1 − α) log(1 − α) denotes the entropy function, then (56) is equivalent to

log 2 − h(α) r <, log(1 + w)

where f (α,ε₁) − f (1/2,ε₀) w =. f (1/2,ε₀)

We will prove f (α,ε₁) − f (1/2,ε₀)<2<sup>1−k</sup>. Therefore, recalling that for all x > −1,

1 1 1 x ≥ + −, log(1 + x) x 2 12

##### we see that (56) holds if

r f (1/2,ε₀) 1 1 < + −. (57) log 2 − h(α) f (α,ε₁) − f (1/2,ε₀) 2 2<sup>k</sup>f (1/2,ε₀)

To get a lower bound on f (1/2,ε₀) we use the upper bound for ε₀ from (26). Thus, for all k ≥ 5

(2 − 2ε₀ + ε₀<sup>2</sup>/2)<sup>k</sup> − 2(1 − ε₀/2)<sup>k</sup> + (1/2)<sup>k</sup> 2<sup>k</sup>f (1/2,ε₀) = (1 − ε₀)<sup>k</sup> (2 − 2ε₀)<sup>k</sup> − 2 > (1 − ε₀)<sup>k</sup> 2 = 2<sup>k</sup> − (1 − ε₀)<sup>k</sup> > 2<sup>k</sup> −2− 2(1 + kε₀)

> 2<sup>k</sup> − 2 − k2<sup>−k+1</sup>. (58)

<!-- Page 18 -->

To get an upper bound on the numerator of w we let α = 1/2 + x and consider the sum in (27) (recall that (27) holds for all ε and that f (α) in (27) is merely 2<sup>k</sup>(1 − ε)<sup>k</sup>f (α,ε)). First, we observe that for all ε ∈ [0, 1),

k() ∑ k 2<sup>k</sup>(1 − ε)<sup>k</sup>f (α,ε) = 2<sup>−k</sup> (2α − 1)<sup>j</sup>[(2 − ε)<sup>k−j</sup>ε<sup>j</sup> − 1]² j j=0 k() ∑ k ≡ T₂(α,ε) + 2<sup>−k</sup> (2α − 1)<sup>j</sup>[(2 − ε)<sup>k−j</sup>ε<sup>j</sup> − 1]² j j=2 k() ∑ k ≤ T₂(α,ε) + 2<sup>−k</sup> (2α − 1)<sup>j</sup> j j=2 = T₂(α,ε) + α<sup>k</sup> − k2<sup>−k</sup>(2α − 1) − 2<sup>−k</sup>. (59)

Next, we will prove that ()₂ ()₂ ()₂ T₂(α,ε₁) (2 − ε₁)<sup>k</sup> − 1 k(2α − 1) (2 − ε₁)<sup>k−1</sup>ε₁ − 1 (2 − ε₀)<sup>k</sup> − 1 − f (1/2,ε₀) = + − 2<sup>k</sup>(1 − ε₁)<sup>k</sup> 4<sup>k</sup>(1 − ε₁)<sup>k</sup> 4<sup>k</sup>(1 − ε₁)<sup>k</sup> 4<sup>k</sup>(1 − ε₀)<sup>k</sup> < αk2<sup>−2k−1</sup>(1 − ε₀)<sup>−k−1</sup>. (60)

For this, define Υ₁(ε) = 1 − (2 − ε)<sup>k−1</sup>ε so that Υ₁(ε₀) = 0. For ε < ε₀ we infer that

0<Υ₁(ε) ≤ 1 − (2 − ε₀)<sup>k−1</sup>ε = 1 − ε/ε₀. (61)

Therefore, the function k(2α − 1)Υ₁(ε)² Υ₂(ε) = (1 − ε)<sup>k</sup>

satisfies k(2α − 1) k(α − 1/2) Υ₂(ε₁) ≤ <. (62) 4(1 − ε₁)<sup>k</sup> 2(1 − ε₀)<sup>k+1</sup>

Next, define ()₂ (2 − ε)<sup>k</sup> − 1 Υ₃(ε) =. (1 − ε)<sup>k</sup>

Differentiation gives ()<sub>k</sub> (2 − ε)<sup>k</sup> − 1 2 − ε Υ₁(ε) −Υ<sup>′3</sup>(ε) = k Υ₁(ε) ≤ k. (1 − ε)<sup>k+1</sup> 1 − ε 1 − ε₀ 2 Since is increasing in ε, we deduce using (61) that for ε < ε₀, 1−−εε () (2 − ε₀)<sup>k</sup> ε −Υ<sup>′3</sup>(ε) ≤ k 1 −. (1 − ε₀)<sup>k+1</sup> ε₀ ∫ <sub>ε</sub> As (1 − ε/ε₀) dε = ε₀/8, we conclude that ε₁₀

(2 − ε₀)<sup>k</sup>ε₀ k Υ₃(ε₁)−Υ₃(ε₀) ≤ k ≤. (63) 8(1 − ε₀)<sup>k+1</sup> 4(1 − ε₀)<sup>k+1</sup>

Adding the inequalities (62) and (63), then dividing by 4<sup>k</sup>, yields (60).

<!-- Page 19 -->

Combining (59) and (60) and requiring k ≥ 6 for (64) we get

T₂(α,ε₁) + α<sup>k</sup> − k2<sup>−k</sup>(2α − 1) − 2<sup>−k</sup> f (α,ε₁) − f (1/2,ε₀) < − f (1/2,ε₀) 2 (1 − ε₁k)<sup>k</sup>

αk2<sup>−2k−1</sup> α<sup>k</sup> − k2<sup>−k</sup>(2α − 1) − 2<sup>−k</sup> < + (1 − ε₀)<sup>k+1</sup> 2 (1 − εk)<sup>k</sup> ()¹ ε)<sub>1k</sub>)<sup>k</sup> α<sup>k</sup> − αk2<sup>−k−1</sup> 4 −+1+ 2<sup>−k</sup>(k − 1) (1(1−−ε<sub>0</sub> = 2 (1 − ε₁k)<sup>k</sup> () α<sup>k</sup> − αk2<sup>−k−1</sup> 3 − k2<sup>−k+1</sup> + 2<sup>−k</sup>(k − 1) < (64) 2 (1 − ε₁k)<sup>k</sup>

α<sup>k</sup> − 3αk2<sup>−k−1</sup> + 2<sup>−k</sup>(k − 1) + 4<sup>−k</sup>k² <. (65) 2 (1 − ε₁k)<sup>k</sup>

Observe now that for k ≥ 3 (65) establishes our promised claim f (α,ε₁) − f (1/2,ε₀)<2<sup>−k+1</sup>. Moreover, combining (58) and (65) we get (66), while the fact α > 9/10 implies (67)

f (1/2,ε₀) 2<sup>k</sup> − 2 − k2<sup>−k+1</sup> > (1 − ε₁)<sup>k</sup> × (66) f (α,ε₁) − f (1/2,ε₀) α<sup>k</sup> − 3αk2<sup>−k−1</sup> + 2<sup>−k</sup>(k − 1) + k²4<sup>−k</sup> 2<sup>k</sup> − 2 > (1 − ε₁)<sup>k</sup> × − (2/3)<sup>k</sup>. (67) α<sup>k</sup> − 3αk2<sup>−k−1</sup> + 2<sup>−k</sup>(k − 1)

Recall now that for any 0 < α < 1 and 0 ≤ q < α<sup>k</sup>,

1 ≥ 1 + k(1 − α) + q. α<sup>k</sup> − q

Observe that 3αk2<sup>−k−1</sup> − 2<sup>−k</sup>(k − 1) < α<sup>k</sup> for α ≥ 2/3. Since α > 9/10, we thus have

1 ≥ 1 + k(1 − α) + 3αk2<sup>−k−1</sup> − 2<sup>−k</sup>(k − 1). α<sup>k</sup> − 3αk2<sup>−k−1</sup> + 2<sup>−k</sup>(k − 1)

Thus, by (57),(58) and (67) we see that (56) holds as long as r < (1 − ε₁)<sup>k</sup>φ(α) − 2 × (2/3)<sup>k</sup> where ( ()) () 1 7 φ(α) ≡ log 2 − h(α) 2<sup>k</sup>(k + 1) − 3k − − αk 2<sup>k</sup> −. 2 2

We are thus left to minimize φ in (9/10, 1]. It will be convenient to define

1 B = 2<sup>k</sup>(k + 1) − 3k − (68) 2 () 7 C = k 2<sup>k</sup> − (69) 2

and rewrite () φ(α) = log 2 − h(α) (B − αC).

Since φ is differentiable its minima can only occur at 9/10, 1 or where () α φ<sup>′</sup>(α) = log (B − αC) − (log 2 − h(α)) C = 0. (70) 1 − α

Note now that ′ φ (α) lim = −(B − C ) < 0 α→1 log(1 − α)

<!-- Page 20 -->

and, thus, the derivative of φ becomes positively infinite as we approach 1. At the same time,

##### φ<sup>′</sup>(9/10) < 2.2B − 2.3C

which is negative for k ≥ 23. Therefore, φ is minimized in the interior of (9/10, 1] for all k ≥ 23. Setting the derivative of φ to zero gives

C − log(1 − α) = (log 2 − h(α)) × − log α B − αC k = (log 2 − h(α)) × − log α. (71) k+6 1 + k(1 − α) + 2<sup>k+1</sup>−7

By “bootstrapping” we will derive a tightening series of bounds on the solution of (71) in α ∈ (9/10, 1). Note first that we have an easy upper bound,

− log(1 − α) < k log 2 − log α. (72)

At the same time, if k ≥ 3 then (k + 6)/(2<sup>k+1</sup> − 7) ≤ 1, implying

k (log 2 − h(α)) − log(1 − α) ≥ − log α. (73) 2 + k(1 − α)

If we write k(1 − α) = D then (73) becomes () log 2 − h(α) D − log(1 − α) ≥ − log α. (74) 1 − α D + 2

By inspection, if D ≥ 3 the r.h.s. of (74) is greater than the l.h.s. for all α > 9/10, yielding a contradiction. Therefore, k(1 − α) < 3 for all k ≥ 3. Since log 2 − h(α) > 0.36 for α > 9/10, we see that for k ≥ 3, (73) implies

− log(1 − α) > 0.07 k or, equivalently, (75) −0.07 k 1 − α < e. (76)

Observe now that (76) implies k(1 − α) < k e<sup>−0.07k</sup>, (77)

and, hence, as k increases the denominator of (71) actually approaches 1. To bootstrap, we first note that since α > 1/2 we have

h(α) ≤ −2(1 − α) log(1 − α) (78) −0.07 k < 2 e (k log 2 − log 0.9) (79) −0.07 k < 2 k e (80)

where (79) relies on (76) and (72). Moreover, α > 1/2 implies − log α ≤ 2(1 − α) which, by (76) implies −0.07 k − log α < 2 e. Thus, starting with (71), using (77), taking k ≥ 3 and using (80), and finally using 1/(1 + x) > 1 − x for all x > 0 we get

k (log 2 − h(α)) − log(1 − α) > 1 + k e−0.07 k+k+6 2<sup>k+1</sup>−7 −0.07 k k (log 2 − 2 k e) > 1 + 2 k e−0.07 k −0.07 k −0.07 k > k (log 2 − 2 k e)(1 − 2 k e) −0.07 k > k log 2 − 4 k² e. (81)

<!-- Page 21 -->

For k ≥ 166, 4 k² e −0.07 k < 1. Thus, for such k, (81) implies 1 − α < 3 × 2<sup>−k</sup>. This, in turn, implies − log α ≤ 2(1 − α) < 6 × 2<sup>−k</sup> and so, by (78) and (72), we have that for all k ≥ 166 and α > 9/10

h(α) < 6 × 2<sup>−k</sup>(k log 2 − log α) < 5 k 2<sup>−k</sup>. (82)

Plugging (82) into (71) to bootstrap again, we get (analogously to the derivation of(81)) that

k (log 2 − 5 k 2<sup>−k</sup>) − log(1 − α) > <sup>−k</sup> k+6 1 + 3 k 2 + 2<sup>k+1</sup>−7 k (log 2 − 5 k 2<sup>−k</sup>) > 1 + 6 k 2<sup>−k</sup> > k (log 2 − 5 k 2<sup>−k</sup>)(1 − 6 k 2<sup>−k</sup>) > k log 2 − 11 k² 2<sup>−k</sup>.

Since e<sup>x</sup> < 1 + 2x for x < 1 and 11 k²2<sup>−k</sup> < 1 for k > 10, we see that

1 − α < 2<sup>−k</sup> + 22 k²2<sup>−2k</sup>.

Plugging into (72) the fact − log α < 6 × 2<sup>−k</sup> we get − log(1 − α) < k log 2 + 6 × 2<sup>−k</sup>. Using that e<sup>−x</sup> ≥ 1 − x for x ≥ 0, we get the closely matching upper bound,

##### 1 − α > 2<sup>−k</sup> −6×2<sup>−2k</sup>.

Thus, we see that for k ≥ 166, φ is minimized at an α<sub>min</sub> which is within δ of 1−2<sup>−k</sup>, where δ = 22 k² 2<sup>−2k</sup>. Let T be the interval [1 − 2<sup>−k</sup> − δ, 1 − 2<sup>−k</sup> + δ]. Clearly the minimum of φ is at least

φ(1 − 2<sup>−k</sup>) − δ × max |φ<sup>′</sup>(α)|. α∈T

Using very crude bounds, it is easy to see from (70) that if α ∈ T then |φ<sup>′</sup>(α)| ≤ 2 k 2<sup>k</sup>. Now, since for k ≥ 1 we have log(1 − 2<sup>−k</sup>) > −2<sup>−k</sup> − 2<sup>−2k</sup>, a simple calculation gives

<sup>−k</sup> <sup>k</sup> log 2 φ(1 − 2)>2 log 2 + (k − 1) − 1 − 2k² 2<sup>−k</sup>. (83) 2 Therefore,

<sup>k</sup> log 2 φ<sub>min</sub> > 2 log 2 + (k − 1) − 1 − 46 k³ 2<sup>−k</sup>. 2 Finally, recall that (56) holds as long as r < (1 − ε₁)<sup>k</sup>φ<sub>min</sub> −2× (2/3)<sup>k</sup>. Using the upper bound for ε₀ from (26) we get ()<sub>k</sub> () <sup>k</sup> <sup>−k</sup> 2k <sup>k</sup> log 2 46k³ (1 − ε₁) × φ<sub>min</sub> > 1−2 − <sup>k</sup> × 2 log 2 + (k − 1) − 1 − 4 2 2<sup>k</sup> () () <sup>−k</sup> 2k² <sup>k</sup> log 2 46k³ > 1 − k2 − <sup>k</sup> × 2 log 2 + (k − 1) − 1 − 4 2 2<sup>k</sup>

<sup>k</sup> log 2 50k³ > 2 log 2 − (k + 1) − 1 − 2 2<sup>k</sup> = ρ<sub>k</sub>.

### 10 Bounds for specific values of k

Recall from our discussion in Section 3 that in order to establish r ≥ r<sub>k</sub> it suffices to prove that there exists some ε ∈ [0, 1) for which the function g<sub>r</sub> defined in (22), i.e., ( <sup>k</sup> <sup>k</sup> <sup>k</sup> )<sub>r</sub> f (α)<sup>r</sup> (2 − 2ε + αε²) − 2(1 − ε + αε) + α g<sub>r</sub>(α) = <sup>α</sup> <sup>1−α</sup> = <sup>α</sup> <sup>1−α</sup>, (84) α (1 − α) α (1 − α)

<!-- Page 22 -->

has a unique global maximum at 1/2. Recall also that for any r the only choice of ε for which g<sub>r′′</sub>(1/2) < 0 is the one mandated by (23). Thus, for any fixed k one can get a lower bound for r<sub>k</sub> by: i) solving (23), ii) substituting the solution to (84), and iii) plotting the resulting function to check whether g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α = 1/2. As g<sub>r</sub> never has more than three local maxima this is very straightforward and yields the lower bounds referred to as “simple” lower bounds in Table 10 below. As mentioned in the Introduction, the simple weighting scheme yielding Theorem 4 does not yield the best possible lower bound afforded by applying the second moment method to balanced satisfying assignments. For that, one has to use the significantly more refined argument which we presented in Sections 7—9. That argument also eventually reduces to proving g<sub>r</sub>(1/2) > g<sub>r</sub>(α) for all α = 1/2. Now, though, ε is allowed to depend on α, subject only to ε ≤ ε₀, where ε₀ is the solution of (23). Naturally, at α = 1/2 one still has to take ε = ε₀ so that the derivative of g<sub>r</sub> vanishes, but for larger α (where the danger is) it turns out that decreasing ε somewhat helps. The bounds reported in Table 1 in the Introduction (and replicated below as the “refined” bounds) are, indeed, the result of such optimization of ε as a function of α. Specifically, for k ≤ 5 we considered 10,000 equally spaced values of α ∈ [0, 1] and for each such value found ε ≤ ε₀ such that the condition g<sub>r</sub>(α,ε) < g<sub>r</sub>(1/2,ε₀) holds with a bit of room. (For k > 4 we solved (23), defining ε₀, numerically to 10 digits of accuracy. For the optimization we exploited convexity to speed up the search.) Having determined such values of ε, we (implicitly) assigned to every not-chosen point in [0, 1] the value of ε at the nearest chosen point. Finally, we computed a (crude) upper bound on the derivative of g<sub>r</sub> with respect to α in [0, 1]. This bound on the derivative, along with our room factor, then implied that for every point that we did not check, the value of g<sub>r</sub> was sufficiently close to its value at the corresponding chosen point to also be dominated by g<sub>r</sub>(1/2,ε₀). For k > 5, we only partitioned [0, 1] into two intervals, namely [1/10, 9/10] and its complement. Assigning the values ε₀ and ε₀/2, respectively, to all the points in each interval yielded the bounds for such k.

||3|4|5|7|10|20|21|
|---|---|---|---|---|---|---|---|
|Upper bound|4.51|10.23|21.33|87.88|708.94|726, 817|1, 453, 635|
|Refined lower bound|2.68|7.91|18.79|84.82|704.94|726, 809|1, 453, 626|
|Simple lower bound|2.54|7.31|17.61|82.63|701.53|726, 802|1, 453, 619|

k

### 11 Conclusions

We proved that the random k-SAT threshold satisfies r<sub>k</sub> ∼ 2<sup>k</sup> log 2. In particular, we proved that random k-CNF formulas with density 2<sup>k</sup> log 2 − k(log 2)/2 − O(1) have exponentially many balanced satisfying truth assignments. That is, truth assignments that have at least one satisfied literal in every clause yet, in total, satisfy only as many literal occurrences as a random truth assignment. Our argument leaves a gap of order Θ(k) with the first moment upper bound 2<sup>k</sup> log 2. With respect to this gap it is worth pointing out that the best known techniques [9, 19] for improving this upper bound only give r<sub>k</sub> ≤ 2<sup>k</sup> log 2 − b<sub>k</sub> where b<sub>k</sub> → (1 + log 2)/2. At the same time, it is not hard to prove that for r = 2<sup>k</sup> log 2 − k(log 2)/2, i.e., within an additive constant from our lower bound, w.h.p. there are no satisfying truth assignments that satisfy only km/2 + o(km) literal occurrences. Thus, any asymptotic improvement over our lower bound would mean that tendencies toward the majority assignment become essential as we approach the threshold. The gap between the upper bound and the best algorithmic lower bound r<sub>k</sub> = Ω(2<sup>k</sup>/k), seems to us much more significant (and is certainly much bigger!). The lack of progress in the last ten years suggests the possibility that no polynomial time algorithm can improve the lower bound asymptotically. At the same time, in a completely different direction, M´ezard and Zecchina [21] recently used the non-rigorous cavity method of statistical physics to obtain detailed predictions for the satisfiability threshold suggesting that r<sub>k</sub> = 2<sup>k</sup> log 2 − O(1). (See also [20] for an overview.) Insights from this analysis led them to an intriguing algorithm called “survey propagation” (described in [21, 2]) that seems to perform well on random instances

<!-- Page 23 -->

of k-SAT close to the threshold, at least for small k. (Its performance is especially impressive for k = 3.) A rigorous analysis of this algorithm is still lacking, though, and it remains unclear whether its success for values of r close to the threshold extends to large k. The success of the second moment method for balanced satisfying truth assignments suggests that such assignments form a “mist” in {0, 1}<sup>n</sup> and, as a result, they might be hard to find by algorithms based on local updates. Moreover, as k increases the influence exerted by the majority vote assignment becomes less and less significant as most literals occur very close to their expected kr/2 times. As a result, the structure of the space of solutions may well be different for small k (e.g. k = 3, 4) and for larger k.

To summarize, the following key questions remain:

1. Is 2<sup>k</sup> log 2 − r<sub>k</sub> bounded?
2. Is there an algorithmic threshold λ<sub>k</sub> = o(2<sup>k</sup>) so that for r > λ<sub>k</sub>, no polynomial-time algorithm can find a satisfying truth assignment for the random formula F<sub>k</sub>(n,rn) with uniformly positive probability?
### Acknowledgments

We are grateful to Cris Moore for illuminating conversations and to Mike Molloy for helpful comments. We are indebted to Chris Calabro for a careful reading and for a correction to a previous version of this paper. Part of this work was done while the authors participated in the focused research group on discrete probability at BIRS, July 12-26, 2003.

### References

[1] D. Achlioptas and C. Moore. The asymptotic order of the random k-SAT threshold. In Proc. 43th Annual Symposium on Foundations of Computer Science, pages 126–127, 2002.

[2] A. Braunstein, M. M´ezard, and R. Zecchina. Survey propagation: an algorithm for satisfiability. Preprint, 2002.

[3] M.-T. Chao and J. Franco. Probabilistic analysis of a generalization of the unit-clause literal selection heuristics for the k-satisfiability problem. Inform. Sci., 51(3):289–314, 1990.

[4] P. Cheeseman, B. Kanefsky, and W. Taylor. Where the really hard problems are. In Proc. 12th International Joint Conference on Artificial Intelligence (IJCAI-91) Vol. 1, pages 331–337, 1991.

[5] V. Chv´atal and B. Reed. Mick gets some (the odds are on his side). In Proc. 33th Annual Symposium on Foundations of Computer Science, pages 620–627, 1992.

[6] N. G. de Bruijn. Asymptotic methods in analysis. Dover Publications Inc., New York, 3rd edition, 1981.

[7] A. Dembo, Y. Peres, J. Rosen and O. Zeitouni. Thick points for planar Brownian motion and the Erd˝os-Taylor conjecture on random walk. Acta Math., 186:239–270, 2001.

[8] A. Dembo and O. Zeitouni. Large deviations techniques and applications. Springer Verlag, New York, 2nd edition, 1998.

[9] O. Dubois and Y. Boufkhad. A general upper bound for the satisfiability threshold of random r-SAT formulae. J. Algorithms, 24(2):395–420, 1997.

[10] O. Dubois, Y. Boufkhad, and J. Mandler. Typical random 3-SAT formulae and the satisfiability threshold. In Proc. 11th Annual Symposium on Discrete Algorithms, pages 126–127, 2000.

[11] P. Erd˝os and L. Lov´asz. Problems and results on 3-chromatic hypergraphs and some related questions. Colloq. Math. Soc. J´anos Bolyai, Vol. 10, 609–627.

<!-- Page 24 -->

[12] P. Erd˝os and S. J. Taylor. Some problems concerning the structure of random walk paths. Acta Sci. Hung. 11:137–162, 1960.

[13] J. Franco and M. Paull. Probabilistic analysis of the Davis–Putnam procedure for solving the satisfiability problem. Discrete Appl. Math., 5(1):77–87, 1983.

[14] E. Friedgut. Necessary and sufficient conditions for sharp thresholds of graph properties, and the k-SAT problem. J. Amer. Math. Soc., 12:1017–1054, 1999.

[15] A. M. Frieze and S. Suen. Analysis of two simple heuristics on a random instance of k-SAT. J. Algorithms, 20(2):312–355, 1996.

[16] A. Frieze and N. C. Wormald. Random k-SAT: a tight threshold for moderately growing k. In Proc. 5th International Symposium on Theory and Applications of Satisfiability Testing, pages 1–6, 2002.

[17] S. Janson, Y. C. Stamatiou, and M. Vamvakari. Bounding the unsatisfiability threshold of random 3-SAT. Random Structures Algorithms, 17(2):103–116, 2000.

[18] A. Kaporis, L. M. Kirousis, and E. G. Lalas. The probabilistic analysis of a greedy satisfiability algorithm. In Proc. 10th Annual European Symposium on Algorithms, volume 2461 of Lecture Notes in Computer Science, pages 574–585. Springer, 2002.

[19] L. M. Kirousis, E. Kranakis, D. Krizanc, and Y. Stamatiou. Approximating the unsatisfiability threshold of random formulas. Random Structures Algorithms, 12(3):253–269, 1998.

[20] M. M´ezard, G. Parisi, and R. Zecchina. Analytic and Algorithmic Solution of Random Satisfiability Problems. Science, 297: 812-815, 2002.

[21] M. M´ezard and R. Zecchina. Random K-satisfiability: from an analytic solution to a new efficient algorithm. Phys. Rev. E, 66, 056126, 2002.

[22] D. G. Mitchell, B. Selman, and H. J. Levesque. Hard and easy distributions of SAT problems. In Proc. 10th National Conference on Artificial Intelligence, pages 459–462, 1992.

[23] R. Monasson and R. Zecchina. Statistical mechanics of the random K-satisfiability model. Phys. Rev. E (3), 56(2):1357–1370, 1997.

[24] I. Stewart. Where drunkards hang out. Nature, News and Views, October 18, 2001.