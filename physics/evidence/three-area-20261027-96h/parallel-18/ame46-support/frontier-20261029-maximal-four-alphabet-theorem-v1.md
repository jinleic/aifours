# A six-marginal obstruction: maximal coefficients cannot all lie in four symbols per party once t>12

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 09:22:05 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. The proof is self-contained finite-dimensional probability and the six AME marginals. It imports no no-OLS(6), no no-Hamming-one lemma, no fixed residual-support profile, and no held material.

## 1. Statement

Fix any normalized complex AME(4,6) state ψ and any product basis. Let P be its t positions with modulus `1/6`, the maximal possible coefficient modulus. Suppose that at each of the four parties the coordinate values appearing in P lie in a set K_i of at most four symbols. Then

`t≤12`.

Equivalently, if t≥13, then at **at least one** party the maximal positions use at least five local symbols. This is not a statement that all four parties must use five symbols.

Since any AME state with N support entries obeys `N≥72−t` (proved below), a hypothetical sub-60 support state must have t≥13. Hence its maximal positions cannot all be confined to four symbols at every party. No bound `N≥60` is claimed for unrestricted states.

The value12 is realized in the known published 60-support construction, but the source state is not a premise of this argument and no independent novelty assertion is made.

## 2. Maximal entries and event masses

Enlarge each K_i to exactly four symbols if necessary, and let H_i be its complementary two-symbol set. No maximal position contains any H_i symbol. Every two-party marginal is `I_36/36`, and every one-party marginal is `I_6/6`; therefore the probability distribution `p(x)=|ψ_x|²` has

`Pr(x_i∈H_i)=2/6`,  `Pr(x_i∈H_i,x_j∈H_j)=4/36` for i≠j.         (1)

For every 2|2 cut, `U=6ψ` is unitary. A modulus-1/6 entry exhausts its entire pair row and pair column, so no other support position shares any coordinate pair with it. The maximal positions are therefore pair-injective, and `t≤|K_i×K_j|=16`.

For `a∈K_i`, let c_i(a) be its number of occurrences in P. In any other party j, these c_i(a) maximal words have distinct j values, all in K_j. Thus `c_i(a)≤4` and `Σ_{a∈K_i} c_i(a)=t`.

Call `a∈K_i` **full** when c_i(a)=4, and let q_i be the number of full symbols. Since the other four-symbol occurrence counts are at most3,

`q_i≥t−12`.                                                        (2)

For a full symbol a, its four P words use all four K_j values at every other party j. Since those pair rows are exhausted, every nonmaximal support position with x_i=a must satisfy `x_j∈H_j` for **all** j≠i.

Let D_{i,a} be the event consisting of those nonmaximal positions with x_i=a. Its probability is exactly

`Pr(D_{i,a})=Pr(x_i=a)−4/36=1/6−4/36=2/36`.                     (3)

Every point in D_{i,a} has exactly three H coordinates. Distinct D_{i,a} events are disjoint, including events at different parties: a point in D_{i,a} has H_j at every other party, whereas the full symbols are in K_j.

## 3. t≥14 is impossible

Suppose t≥13. Then every q_i is at least1 by (2). Fix two parties i,j and let k,l be the other two. The event `H_i∩H_j` contains every D event at k or l. Their disjoint masses from (3) give

`2(q_k+q_l)/36 ≤ Pr(H_i∩H_j)=4/36`, hence `q_k+q_l≤2`.           (4)

This holds for every pair k,l. Since each q_i≥1, every q_i=1. Equation (2) now implies t≤13. Thus t≥14 is impossible under the four-alphabet hypothesis.

## 4. t=13 is impossible

Now t=13 and all four q_i=1. Let D be the union of the four full-symbol residual events. They are disjoint and each has mass2/36, so

`Pr(D)=8/36`,

and every point in D has exactly three H coordinates.

For any pair i,j, the two D events at the other two parties already have total mass4/36, equal to all of `Pr(H_i∩H_j)`. Thus outside D no positive-probability position can have two or more H coordinates.

Write E for the nonmaximal support. Its total probability is `1−13/36=23/36`, since each P coefficient has mass1/36. Therefore

`Pr(E\D)=23/36−8/36=15/36`.

On the other hand, by (1), the expected total number of H coordinates over all support positions is `4·(2/6)=48/36`. P contributes none, and D contributes `3·(8/36)=24/36`. The remaining E\D must contribute

`48/36−24/36=24/36`

to this expectation. But each of its positions has at most one H coordinate, so its contribution is at most its probability15/36. The strict contradiction `24/36>15/36` excludes t=13. Together with §3 this proves t≤12.

All probabilities in this proof are those of the **same tensor** ψ, and every required pair probability in (1) comes from its six specified marginals. No independently chosen supports, basis changes, or unitaries are substituted between cuts.

## 5. Row-count consequence and scope

For any product basis, let t count modulus-1/6 coefficients. In a 36-row 2|2 flattening, t rows contain a maximal singleton; every other row needs at least two nonzero entries. Thus `N≥t+2(36−t)=72−t`. Hence N≤59 would require t≥13, which by this candidate forces the maximal support to use at least five local symbols at some party.

The theorem does not rule out that possibility, does not classify arbitrary AME states, and does not supply a smaller-support witness. It explains why searches that hold two symbols at every party absent from P cannot improve the known 60-term support, even with arbitrary nonmaximal amplitudes and phases.

## 6. Exact controls

`frontier-20261029-maximal-four-alphabet-controls-v1.py`, SHA-256 `29c468f44107722436766d11ac207476e867f33391d1fbfeef793d7481d9167c`; receipt `frontier-20261029-maximal-four-alphabet-controls-v1.json`, SHA-256 `bbb6db689e5229435b5c3387c8c35bc1a99a072fc95e3c774923c0b6907563da`, enumerates the occurrence profiles c_i for t=13,14,15,16, verifies that the HH capacity (4) leaves only `(3,3,3,4)` at every party for t=13 and nothing for t≥14, and checks every mass identity as `fractions.Fraction`. It records the final contradiction margin `1/4`. The nearby t=12 occurrence pattern `(3,3,3,3)` is not excluded by this route.

The control is bounded exact arithmetic; the universal same-tensor probability proof is §§2–4. Same-harness arithmetic is not independent scientific review or formal proof.
