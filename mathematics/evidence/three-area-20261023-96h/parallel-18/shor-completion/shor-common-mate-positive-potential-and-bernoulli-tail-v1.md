# Shor common-mate realization — explicit positive harmonic potential and exponentially summable raw returns

Owner MathShor / MathShor-2. Actual `/bin/date` before writing: **Sun Oct 25 19:26:29 PDT 2026**. WRITTEN CANDIDATE, unreviewed. No scientific interpreter/calculator/eval/CAS/program/enumeration/solver/replay/build/test/CLI/nestedagent/new GO. All polynomial/finite-chain calculations below are hand-written, not simulated or executed.

This new primary derivation is AFTER the actual v105-G review return19:14:25 and the SEPARATE prospective primary-resumption ACK19:15:35, `primary-resumption-after-v105-G-ack-v1.json`, SHA256 `71fd5544d6b4896df794f3f9b60bc84ef468f0fe91678fd4bcf961e09d67e797`. The intervening parent notification that it read the348-LF review is not a new review duty, mathematical adoption of this packet or new science permission.

## 0. Exact original interface and what changes representation

The original target remains finite RAW UD factor-complete containment of the literal sixteen Shor words C. There is no new endpoint bound or finite completion here. The common-mate gate has NOT been witnessed.

Assume HYPOTHETICALLY that one A subset Z_n with0inA has direct complements B,D2,D3 containing the prescribed J0,J2,J3, and I={0,3,8,11}subsetA. At the SAME n choose the old existence-normal-form rows

    D_0=B, D_3=D_8=D2, D_11=D3,
    D_i=B at every other i in A,
    Y=union_(i in A) ({i}xD_i).

All pairs and states use canonical representatives0,...,n-1. Each D_i complements the SAME actual A. This is an EXISTENCE construction; the actual one-b set of a hypothetical original completion need not equal Y, and replacing it has not been proved to preserve finite completability.

The preceding `shor-cyclic-one-b-automaton-regular-completion-and-finiteness-v1.md`, SHA256 `17da5c435b348966f1097a79a0c1a9c0c7d7aa43e62dfce74f9cef4ef675af3a`, gives the ACTUAL graph with a-edges v->v+1 and b-edges i->-j for(i,j)inY. Its first-return code X at0 is a regular RAW UD factor-complete extension of canonical M0. For this row-normal form the original seeds force a nonbase directed cycle, so X is INFINITE. These assertions are WRITTEN/unreviewed local dependencies, not a new finite witness.

The new representation here supplies an EXPLICIT positive polynomial harmonic vector for that SAME graph and all Bernoulli parameters. It proves exact Kraft normalization and quantitative exponential return tails directly. Thus neither a failure of summability, a missing positive Perron vector, nor lack of arbitrarily close finite UD approximants explains the finite-realization gap. Those tempting weakenings can be satisfied uniformly while X is still necessarily infinite.

## 1. Actual finite weighted graph, no stochastic experiment

Let t be ANY real parameter with0<t<1, assigning formal Bernoulli letter weights a=t,b=1-t. For every graph vertex v define the positive polynomial

    h_v(t)=sum_(s in A) t^[s-v]_n,                         (1)

where[.]_n is the canonical residue in{0,...,n-1}. Every coefficient is a nonnegative integer, and every h_v is strictly positive. Let a0=|A| (not the letter a). Then

    a0*t^(n-1) <= h_v(t) <= a0.                           (2)

No p-adic prime, old trade-mask parameter or controller-style carry potential is being renamed here; t is a free letter-probability variable.

Let M(t) be the finite nonnegative adjacency matrix, with a-edge weight t and each b-edge weight1-t. If an a-edge and b-edge share endpoints, both labelled edge weights are counted. A b-row is present ONLY at iinA, and its actual outgoing endpoints are-j for j in D_i. There is no arbitrary independent assignment of edge probabilities or row normalization assumption.

## 2. Explicit harmonic identity, derived from the SAME-A tilings

For one s, the difference of the corresponding terms in h_v-t h_(v+1) is0 unless s=v. In that case it is1-t^n, since the residue exponent changes from0 to n-1. Summing gives EXACTLY

    h_v - t h_(v+1) = (1-t^n)*1_A(v).                   (3)

For ANY actual mate D_i, its direct tiling with A enumerates EVERY residue once. Therefore

    sum_(j inD_i) h_(-j)
      = sum_(j inD_i,s inA) t^[s+j]_n
      = 1+t+...+t^(n-1).                                (4)

Multiplying(4) by1-t gives1-t^n. At v notinA there are no b-edges, and(3) is exactly the a-recursion. At iinA, (3)/(4) give

    h_i=t h_(i+1)+(1-t)sum_(j inD_i)h_(-j).              (5)

Thus the ENTIRE finite matrix satisfies

    M(t) h(t)=h(t)                                       (6)

for EVERY0<t<1, with explicit h>0. This checks all actual unknown mate rows at once. It uses neither an unsupplied Perron theorem nor a characteristic-root calculation, prime-field reduction or program.

Equation(6) gives the exact positive diagonal similarity

    K(t)_(v,u)=M(t)_(v,u)*h_u(t)/h_v(t).                  (7)

Its row sums are1, so it is a genuine finite transition matrix. At the labelled-edge level an a-edge has probability t*h_(v+1)/h_v, and an actual b-edge i->-j has probability(1-t)*h_(-j)/h_i. These probabilities are all positive on existing edges. The a-cycle alone connects all vertices, so the finite chain is irreducible. This is an exact algebraic construction, not a generated Markov simulation.

## 3. Exact first-return weights and a direct uniform hitting bound

For any finite graph path, the h ratios in its transition probability telescope. A path0->0 with label w therefore has EXACT probability

    t^(|w|_a)*(1-t)^(|w|_b).                              (8)

The earlier all-t border injection makes a loop label unambiguous: no distinct0->0 graph paths have the same binary word. Consequently each first-return word contributes precisely its one ordinary Bernoulli weight, not a hidden multiplicity or a probability assigned to a surrogate code.

Let tau be the first POSITIVE return time to0 from0. More generally, from any nonzero state v, following only a-edges reaches0 in d=n-v steps,1<=d<=n-1, without an earlier visit. Its probability is exactly

    t^d*h_0/h_v >= t^(d+n-1) >= t^(2n-1).                (9)

At state0 the all-a path returns for the first time after n steps with probability t^n>=t^(2n-1). Thus from EVERY state, including a new return experiment at0, the probability of reaching0 within n steps is at least

    delta(t)=t^(2n-1)>0.                                 (10)

This estimate needs no recurrence theorem and does not take a minimum over an unspecified stationary distribution. Applying the finite Markov property at deterministic multiples of n gives

    P(tau>kn) <= (1-delta(t))^k   for EVERY integerk>=0.  (11)

Hence return occurs with probability1, and the actual first-return code satisfies

    sum_(w inX) t^(|w|_a)*(1-t)^(|w|_b) = 1.              (12)

The equality is proved by the explicit chain and path unambiguity; it is not simply inferred from an abstract infinite-code Kraft theorem or factor completeness.

The same tail gives

    E tau <= n/delta(t).                                 (13)

More strongly choose ANY theta>0 with exp(theta*n)*(1-delta(t))<1. Partition tau into n-step bins; the geometric bound makes E exp(theta*tau) finite. Thus X has a genuine exponentially summable length distribution at EVERY fixed Bernoulli parameter0<t<1, despite its infinite support. No numerical theta or approximation was chosen/evaluated.

## 4. Uniform finite UD approximants, and why no truncation is complete

Fix ANY epsilon with0<epsilon<=1/2. For all t in[epsilon,1-epsilon], use the common lower bound

    delta_epsilon=epsilon^(2n-1)>0.

For an integerL>=0 let

    X_L={w inX:|w|<=L}.

This is a FINITE subset of the same actual raw UD code. For L>=2n-1 it contains ALL canonical M0, since a^n has lengthn and every one-b word has lengthi+j+1<=2n-1. In particular it contains the literal Shor C under the hypothetical gate.

Combining(8)/(11)/(12) gives the exact UNIFORM bound

    0 <= 1 - sum_(w inX_L)t^(|w|_a)*(1-t)^(|w|_b)
      = P(tau>L)
      <= (1-delta_epsilon)^(floor(L/n))                 (14)

for EVERY t in that whole compact interval. No runtime enumeration of X_L is needed for the existence/proof; the finite graph/length definition specifies the actual finite code.

For the original row-normal form X is INFINITE by the actual wrapped-pair cycle already proved. Therefore, for EVERY finiteL, some first-return word lies outside X_L and has strictly positive weight at EVERY0<t<1. The left-hand deficit in(14) is consequently STRICTLY positive. Finite X_L is NOT factor-complete: the elementary finite complete-UD Bernoulli identity would require Kraft mass1. Near1 is not1.

This provides a precise conditional method control. If the common-mate gate has a witness, then finite RAW UD supersets of C can be chosen with arbitrarily small Bernoulli mass deficit, uniformly on any prescribed compact parameter interval, while ALL these finite truncations remain incomplete. It does not assert that such a common-mate witness has actually been found. It does not approximate an unknown proof into a genuine finite completion.

## 5. Relation to the previous unbounded carry obstruction

The earlier carry packet `shor-common-mate-carry-cocycle-and-reset-control-v1.md`, SHA256 `5cd70c2f82e473c7e651856f8ed2da5babfe22f072cbe3383f801cc39a0820f7`, forbids a uniformly bounded additive STATE/history potential plus INPUT-only surcharge representing the integer carries of a particular residue decoder. The present h(t) does NOT contradict that result.

Here log h transforms PROBABILITY weights of the cyclic graph and cancels only along an entire graph path. It is not a bounded correction that removes raw a^n insertions along every decoder-input sequence, and it does not eliminate a nonbase directed cycle. A finite chain may have exponential first-return tails and nevertheless permit arbitrarily many turns through such a cycle. The integer raw lengths remain unbounded.

Likewise the earlier finite complementary-state automaton/linear border test concerns residue-fibre multiplicities. Positive harmonic normalization, finite expected return length and exponential tails add exact analytic information about the regular realization, but NONE is a finite raw STAB/GP theorem or an actual isolated-word PR lift.

## 6. Original residual, exact dependencies and scientific ceiling

The new load-bearing algebra is fully supplied in(1)–(14), using the SAME actual mates, raw graph and return language. Ordinary imports are finite nonnegative matrix algebra, elementary finite Markov path probabilities/conditioning, geometric-series convergence and the elementary necessary Bernoulli identity for finite complete UD codes. The preceding graph's raw UD/completeness and its forced infinite normal-form cycle are explicitly named WRITTEN/unreviewed local dependencies; no hidden classical classification/H* is inserted.

The complete original Shor alternatives remain unchanged: exhibit an ACTUAL finite RAW UD factor-complete extension of C, or prove a C-specific obstruction for EVERY actual finite PR-saturated raw prefix, arbitrary endpoint tiles/orders/one-b arrays/higher-b bridge words/heterogeneous delays/arity and raw STAB. The common-mate gate remains unwitnessed, k7/Phi_n-divisible and ALLlargertrade cases remain, and a hypothetical completion's actualY need not equal the selected rownormal form.

This result excludes only particular EASIER surrogates for finite realization: positive Perron normalization, finite mean return, exponential-tail summability or near-unit finite Kraft mass cannot be substituted for an actual finite complete code. It does not show that every other finite graph/history splitting fails. The earlier n2 finite-prefix control still proves that an infinite unsplit cyclic first-return code need not obstruct a different finite completion.

Hstar stays FALSE/WITHDRAWN; FACT660-order scope is not silently narrowed to extra full-code1320 orders; old seed/multiplier/cardinality filters remain inherited. No new lower/upper bound, full noncompletion, world-wide openness/priority/SOTA or discovery count is claimed. The packet is an exact new representation/control in the original realization attack, not a completed target.

No formal/kernel/human/configured-family/executable/finite-triple-witness acceptance, scientific execution or new GO. All old chronology/root/cadence/exposure/unadmitted-execution findings remain. Every write stays in the exclusive Shor owner root; no frozen/source/shared file is changed. Same original eighteen slots, cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38. The96-hour round is not closed.
