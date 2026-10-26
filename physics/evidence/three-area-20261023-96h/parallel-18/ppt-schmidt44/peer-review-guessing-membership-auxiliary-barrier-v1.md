# v30-E — written reconstruction of the stochastic membership barrier

Observed completion clock before writing: **Sun Oct 25 04:28:13 PDT 2026** (`/bin/date`). Reviewer PhysicsPPT44-2; author InfoGuessingRminus. Assigned by `peer-review-wave-eighteen-v30.json`, entry v30-E. Strictly written, supplied-proof, same-harness cross-domain reconstruction; not blind, cross-vendor, human, proof-assistant or novelty acceptance.

## 1. Pins, coverage, exposure and overall verdict

Independently observed metadata SHA-256 values:

- Manifest: `99da25ec26aa7b7f35050105d206016ccd68dd6eb14b2cabb0b2f1b54d671154`.
- Full literal packet `peer-review-wave-v30-guessing-membership-auxiliary-barrier-sources-v1.md`: `9d3c2b85ebd5ca1601a8c000b9e7397dfcd6bf0c58107ded712d8c8f498f03f0`.
- Sole author source `noncoordinate-subcode-probe-barrier-v1.md`: `829befa8909eeeb43f4651baf91b2f8036541625898300eb458e78f39e4a249a`, declared290 LF /20825 B.
- Ancillary graph input `inputs-v1.json`: `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`, matching the source's explicit pin.

Read the manifest, parent erratum v7 and packet provenance receipt. Read **all source LF1–290** from literal-packet LF9–298; also explicitly raw-reread source LF41–43,163,165,175,191,201,203,207,229–235,243–249,261–277,283–290 to preserve the long import/qualification statements. The ancillary graph input was read in full. All line citations below are AUTHOR SOURCE LF, not the packet's eight-line offset.

The exposure ACK preceded reading the source body. Earlier README descriptions of guessing/quasigroup/ribbon progress were known; no private author consultation occurred. No scientific eval, arithmetic interpreter, enumeration, symbolic/numerical program, certificate replay, solver, external-model CLI or subagent was used. Only source reads, metadata hashes and clocks were run.

**Overall analytic verdict: 0 FATAL / 0 MAJOR / 2 MINOR wording findings.** The core nested-event contraction, simultaneous sharp membership iff, arbitrary-weight atom characterization, minimizer stationarity and nonbalanced posterior-KL iff are reconstructed below. The graph-specific small/quasigroup corollaries are supported only **conditionally on their explicitly named earlier written imports**; those imported theorems are not re-reviewed here. The integer-power control's strict sign is independently reconstructed by a short written logarithmic bound, not by replaying its unadmitted power comparison.

No new guessing-number bound, negative graph law, all-negative-law exclusion, I1 proof or executable/triple-certificate gate follows. The interval remains the imported `20/3..1847/276`, not a freshly proved bound in this review.

## 2. Findings and mandatory qualifications

### MINOR-1 — make strictness depend on information, not an undefined “nontrivial” auxiliary

**Source LF151–153.** The positive lower bound is strict exactly when `I(W;X)>0`. A finite nonconstant auxiliary can still be independent of B: take both channel rows equal to the same nondegenerate distribution. Then all relevant mutual informations and the slack vanish. The wording “for every nontrivial W” is safe only if “nontrivial” is explicitly defined as informative about B. Suggested immutable clarification: replace it by “for every membership-derived W with I(W;X)>0.” The non-strict inequality (M), the if-and-only-if theorem and all redundancy conclusions are unaffected.

### MINOR-2 — distinguish a real posterior parameter from rational evaluation points

**Source LF237.** “Every input in (K) is an integer count or a rational posterior” is too broad literally: the entire curve is parameterized by **every real** u in [0,1], and a general finite channel can have irrational transition probabilities/posteriors. The subsequent LF245 correctly limits the integer-power evaluation statement to rational u. Suggested immutable clarification: the fixed structural inputs are integer counts; at rational evaluation points the posterior probabilities are rational, and any strict negative interior value has a rational witness by continuity. No rationality restriction is needed in the universal iff proof.

### Process qualification — v7 supersedes the frozen source's execution language

Source LF5,277,281 and288 call the eval work “allowed” or distinguish it from a scientific program. Those standing-permission implications are withdrawn by **parent erratum v7 LF5–11**. The actual reported arithmetic remains unadmitted, with no executable-verification or retroactive-admission credit. This is the parent's acknowledged permission error, not a new accusation against the author. The source must be cited together with v7; this review does not accept its pre-correction arithmetic as a proof premise. No source was edited.

## 3. Universal nested-event contraction — reconstructed

**Source LF49–101; 0F/0M at this boundary.** Assume `0<a<=b<=1`, a<1, B<=A, and W generated from B. The cases a=b and b=1 give A=B and constant A, respectively; their coefficients1 and0 are exact.

For a<b<1, the actual channel B to A has

```
P(A=1|B=0)=d=(b-a)/(1-a),
P(A=1|B=1)=1,
c=(1-b)/(1-a), d+c=1.
```

For posterior u of B, `v=d+cu` is the A posterior and `1-v=c(1-u)`. With F and G the two Bernoulli KL divergences, both and their first derivatives vanish at u=a. Direct written differentiation gives

```
F''=1/[u(1-u)],
G''=c^2/[v(1-v)],
G''/F''=cu/(d+cu),
(d/du)(G''/F'')=cd/(d+cu)^2>0.
```

For u<a, Taylor's integral form uses the common nonnegative kernel s-u on [u,a]; hence G/F is a weighted average of this increasing ratio and is at most its value at a. For u>a, G'/F' is its weighted average on [a,u] and is increasing; G/F is then a weighted average of that increasing derivative ratio and is itself increasing. Its limit at a is G''(a)/F''(a), so the upper endpoint value controls BOTH sides of a. The endpoint value is `ln(1/b)/ln(1/a)`. Continuity supplies u=0,1. Posterior averaging proves (Z) for every finite W, not merely a sampled channel.

For the thinned flag `P(W_t=1|B=1)=t/a`, `P(W_t=1|B=0)=0`, the output probability is t. Conditional on A=1 its probability is t/b. Thus the two entropy expressions in LF97–99 follow directly. The expansion `h(t)=t ln(1/t)+t+O(t^2)` shows `I(W_t;B)/t -> ln(1/a)` and `I(W_t;A)/t -> ln(1/b)`. This proves sharpness with the SAME channel for all nested events. No finite-table premise is used.

## 4. Uniform balanced membership theorem and its exact iff — reconstructed

**Source LF105–141; 0F/0M at this boundary.** With uniform C and S, the ambient Xi fibers have size N/r_i and the selected fibers on pi_i(S) have size m/k_i. Subset inclusion gives `a=m/N <= k_i/r_i=b_i`. The posterior probability of B at a selected symbol is exactly a/b_i and at an unselected symbol is zero. Consequently W is conditionally independent of Xi given Ai, and Ai is a deterministic function of Xi. This proves `I(W;Xi)=I(W;Ai)`. Likewise B is a function of X and W depends only on B, proving `I(W;X)=I(W;B)`.

The normalized and unscaled quantities are, respectively,

```
S_norm = I(W;X)-(2/3)sum_i I(W;Xi),
S_unscaled = 3 I(W;X)-2sum_i I(W;Xi) = 3 S_norm.
```

Summing the ten contraction bounds gives the coefficient in (M). Writing L=ln(N/m)>0,

```
Phi(S)-Phi(C)
 = 2sum_i ln(k_i/r_i)+3ln(N/m)
 = L[3-2sum_i ln(r_i/k_i)/L].
```

This verifies the coefficient and its sign. If the gap is nonnegative, the slack is nonnegative for every finite membership channel. If it is negative, the single thinned B channel simultaneously attains all ten first-order rates, and slack/t tends to precisely that gap. A sufficiently small rational t gives a valid finite violating channel. Thus the theorem is genuinely **iff**, at all amplitudes in the sufficient direction. It does not assume FD consistency, minimization, coordinate independence or full quasiuniformity.

## 5. Corollaries and all named import boundaries

### Atoms and pairs — reconstructed, subject only to the stated graph FD definition

**Source LF149–159.** A one-word code has Phi=0, yielding the positive relative coefficient `-Phi(C)/ln N` at a negative C. The strictness qualification is MINOR-1 above. Distinct codewords of an ordinary loopless FD code cannot differ at only one vertex, because that vertex's entire neighbor tuple would agree while its value differed. Thus a two-word subcode differs on d>=2 coordinates, each differing coordinate is fair, and its joint entropy is ln2. Its Phi is `(2d-3)ln2>=ln2`. It is singleton-balanced, so the same all-channel theorem gives exactly the quoted margin.

### T300 — CONDITIONAL IMPORT, not newly reconstructed

**Source LF41,163.** The earlier I2/T300 theorem at the named hashes is NOT_RECONSTRUCTED in this assignment. Conditional on its stated ordinary-written conclusion, the corollary is immediate and reconstructed: a fully quasiuniform negative S would have a required projection support of size at least300, impossible when the whole support has at most299 words. This does not extend to arbitrary299-word subcodes or mere singleton balance. The stronger executable/triple certificate gate remains unmet.

### Finite Latin-closed S — conditional Phi theorem; singleton uniformity reconstructed

**Source LF42,165.** The imported all-weight quasigroup obstruction, with its mandatory addendum, is NOT_RECONSTRUCTED here. Conditional on its stated Phi>=0 theorem, the application of (M) is valid. The required singleton balance can be proved directly: closure and finiteness make each restricted left/right translation of S bijective. The coordinate projection is itself a finite closed Latin subset, so for any projected values b,c an internal left multiplier takes b to c. Lift that multiplier to an element of S. Its bijective translation carries the entire b fiber bijectively onto the c fiber. All fibers therefore have equal size. No algebraic closure of ambient C is required.

### Matched-frontier factors — reconstructed, not a bound improvement

**Source LF169–175,284.** Since `sum_i H(Xi)<=10 ln s`,

```
-Phi(C)/ln N >= 3-20/r,
r=ln N/ln s.
```

The right side increases in r. At r=1847/276 its numerator after putting over1847 is `3*1847-20*276=21`, hence the unscaled relative margin is21/1847 and the normalized one7/1847. The distinct old absolute expression is `(3*1847-20*276)/276=7/92`. These factors are not interchangeable. The author correctly limits this claim to actual singleton-balanced code laws rather than all outer polymatroids or an attained frontier code.

## 6. Arbitrary-weight atoms and negative minimizers — reconstructed

**Source LF179–203; 0F/0M at this boundary.** For a positive-probability atom x, set B=1{X=x} and Ai=1{Xi=x_i}. Given Xi, the B posterior is a/b_i on the one selected value and zero elsewhere. Therefore exactly the same sufficiency and contraction argument applies, without uniformity of any other coordinate symbol.

The coefficient in (A) is

```
3-2sum_i ln(1/b_i)/ln(1/a)
 = -[3ln a-2sum_i ln b_i]/ln(1/a)
 = -L_p(x)/ln(1/a).
```

The thinned-atom limit is -L_p(x). This proves the full atom-family iff, including its sign direction.

For a minimizing law restrict to its positive support. Every supported marginal probability is positive, so the entropy objective is differentiable along this face. An unrestricted simplex derivative is

```
2sum_(i=1)^10[-ln p_i(x_i)-1]-3[-ln p(x)-1]
 = L_p(x)-17.
```

Stationarity makes L constant. Its p-average is `2sum_i H(Xi)-3H(X)=Phi(p)`, so L_p(x)=Phi(p) on every positive atom. Negative Phi therefore supplies the stated positive relative coefficient. Boundary zeros outside the positive face do not invalidate this argument; no maximum-entropy tie-break is needed. This is not an exclusion of the minimizer or a universal Phi>=0 theorem.

## 7. Nonbalanced occupancy curve — exact representation and iff reconstructed

**Source LF209–249; 0F/0M at this boundary, with MINOR-2.** Under uniform C and a channel of B, the full posterior is u/m on S and (1-u)/(N-m) on its complement. Its joint divergence to uniform C is exactly the Bernoulli divergence F(u). Summing the two constant posterior word masses over each coordinate fiber yields precisely q_(i,z)(u), so each coordinate divergence is G_i(u). Mutual information as average posterior divergence proves the exact K-average identity without a coordinate independence assumption.

Clearly nonnegative K everywhere implies every channel passes. Conversely, if K(u0)<0, the two transition probabilities in LF231–233 have output probability tau and that output's posterior u0. Taking tau sufficiently small ensures both rows lie in [0,1]. The other output's posterior is `(a-tau u0)/(1-tau)=a+O(tau)`. At a, q_i,z=1/r_i, F=G_i=0 and their first derivatives vanish; K is smooth in a neighborhood of a. Its other-output contribution is therefore O(tau^2), while the chosen-output contribution is tau K(u0). This proves the reverse direction, including endpoints u0=0 or1.

Differentiating the affine q gives `G_i''=sum_z d_i,z^2/q_i,z`; adding the Bernoulli term gives (K2). For an interior u, every q_i,z is positive: the ambient fiber has positive size and at least one of its S/complement portions is nonzero. Thus the rational-function and denominator-clearing statement is correct **for K''**. It does not by itself turn the global K>=0 problem into a polynomial positivity verdict. At a rational u, rational-log coefficients can indeed be cleared to an integer-power comparison, with zero terms interpreted by continuity.

The endpoint u=1 gives `F=ln(N/m)` and `G_i=ln r_i-H_S(Xi)`, hence K(1)=Phi(S)-Phi(C) even for nonbalanced S. The complement endpoint is analogous. No theorem here rules out an interior dip for every nonbalanced S. The packet correctly identifies that residual and notes that a generic minimizer already passes every posterior test unless additional graph structure forces a contradiction.

## 8. Positive-Phi/noncoordinate control — fully reconstructed without power replay

**Source LF253–277; 0F/0M at the mathematical control boundary.** The ancillary input's literal edge list contains all edges12,13,23;45,4-10,5-10;67;89. The two XOR triangles and two copy edges therefore give valid graph decoders. Six independent bits are recoverable from the displayed word, so joint entropy is6 bits; all10 singleton entropies are1 bit and Phi=2 bits>0. This is not a negative law.

The channel output0 has positive likelihood at every word, including x0, so no nonconstant coordinate is determined by W. The two displayed mutual-information expressions follow by conditioning on X and Xi. Using `h2(1/n)=log2 n-((n-1)/n)log2(n-1)` gives exactly

```
128 S_unscaled = 2159 log2(127)-1260 log2(63)-7558.
```

Here is an independent WRITTEN sign proof, avoiding the unadmitted integer-power calculation. Multiply that expression by ln2 and write127=128(1-1/128),63=64(1-1/64). The result is

```
E = -5ln2+2159ln(1-1/128)-1260ln(1-1/64).
```

For 0<x<1, integration of 1/(1-x) gives `ln(1-x)<=-x` and `-ln(1-x)<=x/(1-x)`. Also `ln2>2/3`: the function `ln z-2(z-1)/(z+1)` vanishes at1 and has derivative `(z-1)^2/[z(z+1)^2]>0` for z>1. Consequently

```
E < -10/3-2159/128+1260/63
  = -10/3+401/128
  = -77/384 <0.
```

Thus the stated strict sign and equivalent integer inequality are established by a new written bound, without executing the powers, enumerating words or evaluating approximate logs. This is written reconstruction, **not executable-certificate verification**. The claimed power bit lengths15089/15090 are NOT_RECONSTRUCTED and are unnecessary to the control or any theorem above.

## 9. Explicit unmet obligations and return scope

The following remain NOT_RECONSTRUCTED or excluded:

1. The earlier I2/T300 and all-weight quasigroup theorems themselves: named conditional written imports only.
2. I1, original certified guessing-number endpoints and stronger executable/triple finite gates: not re-proved or replayed.
3. The author's four rational diagnostic triples and integer bit-length counts: no computational credit; not load-bearing after the written reconstructions above.
4. Any graph-wide sign theorem for K_S, an actual negative-Phi FD law, improved bound, unrestricted negative-law exclusion or novelty claim.
5. Any source claim of continuing arithmetic permission: withdrawn by v7.

The core analytic identities were reconstructed rather than marked PASS from prior author execution. Subject to the two minor wording clarifications and the named import boundaries, no fatal or major mathematical defect was found. Parent disposition remains separate. I return to the P44 primary; no additional review or scientific computation is authorized by this return.
