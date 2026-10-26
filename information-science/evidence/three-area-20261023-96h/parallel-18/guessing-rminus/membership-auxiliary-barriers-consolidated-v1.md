# R-minus membership auxiliaries: one consolidated proof and the exact graph-specific gap

Owner `InfoGuessingRminus`, info-5. Actual `/bin/date` observation before this consolidation: `Sun Oct 25 04:44:43 PDT 2026`.

**WRITTEN consolidation at named imports. No new scientific computation, interpreter, symbolic program, enumeration or replay.** This is ONE successor account of the existing membership, total-variation and posterior-KL results, not another necessary-condition increment counted as guessing-number progress. No improved numerical bound or negative graph law is supplied:

`20/3 <= gn(R-minus) <= 1847/276` remains the imported certified interval.

## 1. What is proved, what was reviewed, and what is not solved

The generic results below prove:

1. A sharp all-amplitudes contraction for nested events, and the exact iff criterion for every stochastic membership probe of a singleton-balanced subcode.
2. The complete arbitrary-weight one-atom criterion and the reason it is automatically satisfied at a negative fixed-support minimizer.
3. A total-variation/erasure barrier that also covers NONbalanced membership events, including an exact integer-count sufficient certificate.
4. The exact all-real posterior-KL criterion and its changed-prior curvature obstruction. A full-posterior normal form explains precisely how a useful binary-output channel can escape the two-level membership family.

They do NOT prove the graph-specific step that would exclude negative global minimizers. The exact missing assertion is isolated in Section10, without confusing a necessary condition for a useful probe with an upper bound for gn.

### Assurance and actual review history

The original core packet, SHA256 `829befa8909eeeb43f4651baf91b2f8036541625898300eb458e78f39e4a249a`, received the actual PhysicsPPT44-2 v30-E return, SHA256 `dcefe61752e5fa5b92bd3347831566475a5f84c00411ee1d6e9e75fd47ab90f0`: **0 FATAL / 0 MAJOR / 2 MINOR wording findings**, not a zero-finding review. Both are accepted in immutable Addendum2, SHA256 `731dd9a6c2f4c4cf1f80a19d67a23f3c904d673baf03dea6e1f2fb5895fe83c7`, and corrected here:

- a positive relative coefficient implies STRICT slack only when `I(W;X)>0`;
- posterior parameters range over ALL REAL values; rationality applies only to specified evaluation witnesses.

The reviewer reconstructed the original core analytic identities and treated T300/Latin statements as named conditional imports. That review did NOT cover the later total-variation paper or this consolidated successor. The latter remain WRITTEN candidates requiring their own scoped reconstruction; no verdict transfers automatically.

Parent erratum v7, SHA256 `d5e1911bba6549684c93b2e910fac66eb44c353ae5dea2a8d1555516946e8d05`, and mandatory owner Addendum1, SHA256 `1f7bdee73415987af385c508749a9fffcd1461e51a7b36682d5e4c9ef4cf6ecf`, withdraw the erroneous scientific-eval permission and accepted execution-verification credit. The three historical eval calls are preserved and disclosed there, not rerun or retroactively admitted. No part of this proof needs their output. The numerical control in Section9 has a wholly written sign proof.

This is same-harness supplied-proof written work, not formal/proof-assistant kernel, human, configured dual-family, cross-vendor or novelty acceptance. Elementary strong-data-processing, posterior divergence and variational methods retain classical credit; novelty remains UNCLEAR.

## 2. Literal problem, notation and named graph imports

The graph is the literal26-edge BCDRV R-minus in `inputs-v1.json`, SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`: vertices1,...,10, with edges

`12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10`.

A finite code C is FD-consistent when two words equal on N(i) must also agree at i, for every vertex i. Every subset inherits these SAME FDs. No projection is assumed to inherit a smaller induced-graph FD system.

All proof logarithms are natural. For a finite law p on C put

`Phi(p)=2 sum_(i=1)^10 H_p(X_i)-3H_p(X)`.

Changing log base scales all entropy quantities by the same positive constant. For a finite auxiliary W define

`S_p(W)=3I(W;X)-2 sum_i I(W;X_i)`.

This is the UNSCALED HC slack. The normalized coefficient-(2/3) HC slack is exactly S_p(W)/3. Every assertion that a slack is strict below additionally requires a strictly positive information factor, as explicitly stated.

A uniform code law is **singleton-balanced** when every INDIVIDUAL coordinate is uniform on its support. It is **fully quasiuniform** when EVERY projection is uniform on its support. These hypotheses are not interchangeable.

Only the following graph-specific earlier results are imported, and only where expressly used in Section5:

- **I2/T300, ordinary-written boundary:** `I2-complete-written-verification-v1.md`, SHA256 `152f6fed3f7654c9207383892effdd8abe1cc796bca5544cfc7c2271cc077585`; parent `wave-v16-written-frontiers-parent-v1.md`, SHA256 `0189f2186aa54e486736db167235eb78ca3ee184e6d1628f8ecb25a0ce57aa8c`. Its supported composition says every fully quasiuniform Phi-negative graph law has each of eight six-coordinate complement supports at least300. This imported theorem is not re-proved here; executable/triple finite-certificate gates remain UNMET. No I1 or minimum-offender order120 import is used.
- **Latin-closed FD-support inequality:** `quasigroup-critical-law-obstruction-v1.md`, SHA256 `e36979ef85d24e7d71c0cd984400280e7c5a68105897033941652ae5da0b7744`, with mandatory addendum SHA256 `f27646abdc87872582cd87302a4af335f081ff64ca5648413b5116b9c4383869`; parent `wave-v23-quasigroup-critical-law-parent-v1.md`, SHA256 `45b0d0a01c521e49236471b647475224f9bbbab85a0e7aea3be390302b0ca49c`. The imported all-weight theorem gives Phi>=0 on a finite FD-consistent support closed under coordinatewise finite quasigroup multiplication. It says nothing about an arbitrary ambient C without that hypothesis.

All generic analytic proofs below need neither import nor the graph FDs.

## 3. Full posterior normal form: the exact object a useful auxiliary must expose

Let p have positive probability on every word of its finite support C. For any law q on C define

`J_p(q)=3D(q||p)-2 sum_i D(q_i||p_i)`.

Every coordinate baseline probability on its actual support is positive. Posterior divergence gives the exact identity

`S_p(W)=sum_w P(W=w) J_p(p_(X|W=w))`.                      (P)

Consequently the following are equivalent:

- every finite auxiliary W satisfies S_p(W)>=0;
- every BINARY-OUTPUT auxiliary satisfies it;
- J_p(q)>=0 for every law q on C.

Only the nontrivial implication needs proof. If J_p(q)<0, choose a sufficiently small positive tau with

`tau*q(x)<=p(x)` for every x,

and define

`P(W=1|X=x)=tau*q(x)/p(x)`.

The output1 has probability tau and posterior q; output0 has posterior

`p0=(p-tau*q)/(1-tau)`.

For sufficiently small tau this p0 lies in the positive simplex near p. Since every KL divergence vanishes with zero first derivative at its baseline,

`J_p(p0)=O(tau^2)`.

Thus `S_p(W)=tau J_p(q)+(1-tau)J_p(p0)<0` for small tau. Conversely (P) proves that nonnegative J everywhere implies every finite auxiliary passes.

**Binary output is NOT the same as a binary membership input.** The likelihood q(x)/p(x) in this construction can take many distinct values. It factors through B=1{X in S} only when it is constant on S and on its complement. Merely increasing the number of output labels of a fixed membership event does not escape a proved membership barrier; a genuinely non-two-level likelihood can.

A useful exact entropy identity is

`J_p(q)=Phi(q)-E_q L_p(X)`,

where

`L_p(x)=3ln p(x)-2 sum_i ln p_i(x_i)`.

It follows by expanding all KL divergences; no stationarity is assumed. If L_p is constant and equals Phi(p), then J_p(q)=Phi(q)-Phi(p). That special case is established in Section6 for a minimizer and also holds at a singleton-balanced uniform code law.

This normal form organizes the existing posterior argument. It is not a new numerical bound, an existence proof for negative J, or a graph-wide exclusion theorem.

## 4. Sharp nested-event contraction and the balanced-subcode iff

### 4.1 Nested-event lemma

Let B,A be binary with B<=A almost surely, `0<a=P(B=1)<=b=P(A=1)<=1`, a<1. For every finite W generated from B,

`I(W;A)<=ln(1/b)/ln(1/a) * I(W;B)`.                       (Z)

The coefficient is optimal. If b=a, A=B; if b=1, A is constant. For a<b<1 put

`c=(1-b)/(1-a)`, `d=(b-a)/(1-a)`, `v=d+c u`.

Here u is ANY REAL posterior P(B=1|W=w). Define the Bernoulli divergences

`F(u)=D(Ber(u)||Ber(a))`, `G(u)=D(Ber(v)||Ber(b))`.

At u=a both functions and first derivatives vanish. On the interior,

`F''=1/[u(1-u)]`, `G''=c^2/[v(1-v)]`,

`G''/F''=c u/(d+c u)`, whose derivative is `c d/(d+c u)^2>0`.

For u<a, integrating the second derivatives against their common nonnegative Taylor weight shows G/F is at most that ratio at a. For u>a, G'/F' is an increasing weighted average of the second-derivative ratio, and G/F is an increasing weighted average of G'/F'. Hence its maximum is the endpoint value

`G(1)/F(1)=ln(1/b)/ln(1/a)`.

That endpoint also bounds the ratio on u<a. Continuity handles u=0,1. Averaging over W proves (Z) on the entire real posterior interval.

To prove sharpness, for0<t<a use the same thinned flag

`P(W_t=1|B=1)=t/a`, `P(W_t=1|B=0)=0`.

With h the binary entropy,

`I(W_t;B)=h(t)-a h(t/a)`,

`I(W_t;A)=h(t)-b h(t/b)`.

After division by t these tend to ln(1/a),ln(1/b). The construction attains these limiting rates SIMULTANEOUSLY for every nested event paired with the same B.

### 4.2 Balanced membership theorem

Let X be uniform on C, N=|C|, and let S be nonempty and proper, m=|S|. Suppose BOTH uniform C and uniform S are singleton-balanced. Set

`r_i=|pi_i(C)|`, `k_i=|pi_i(S)|`,

`B=1{X in S}`, `A_i=1{X_i in pi_i(S)}`.

Then a=m/N, b_i=k_i/r_i, and B<=A_i. Ambient and selected occupancies are N/r_i and m/k_i; subset inclusion gives a<=b_i. At a selected symbol the posterior of B is the constant a/b_i, and at an unselected symbol it is0. Hence for every finite channel W of B,

`I(W;X_i)=I(W;A_i)`, `I(W;X)=I(W;B)`.

Sum (Z) and use

`Phi(C)=2 sum_i ln r_i-3ln N`,

`Phi(S)=2 sum_i ln k_i-3ln m`.

This gives the exact all-amplitudes bound

`S_p(W)>=[Phi(S)-Phi(C)]/ln(N/m) * I(W;X)`.                (M)

ALL such membership channels pass iff Phi(S)>=Phi(C). Sufficiency follows from (M). For necessity, the common thinned B flag has

`lim_(t down to0) S_p(W_t)/t`

`=3ln(N/m)-2 sum_i ln(r_i/k_i)=Phi(S)-Phi(C)`.

A negative gap therefore produces a sufficiently small positive rational t and a genuine violating finite channel. The theorem does not require minimization, full quasiuniformity, algebraic closure, or graph FDs.

If Phi(S)>Phi(C), its stated relative bound is strictly positive ONLY for channels with I(W;X)>0. A finite nonconstant W can be independent of B and has all information/slack zero; it is not an exception to the non-strict theorem.

## 5. Exact graph corollaries, with no hidden import upgrade

Assume C is singleton-balanced, uniform, FD-consistent, and Phi(C)<0.

- **One-word S:** Phi(S)=0, so every atom-membership channel passes with unscaled relative coefficient `-Phi(C)/ln N`. Strictness additionally requires I(W;X)>0.
- **Two-word S:** distinct FD codewords cannot differ at only one vertex. If their Hamming distance is d>=2, uniform S is singleton-balanced and `Phi(S)=(2d-3)ln2>=ln2`. All such membership channels pass (M), with relative coefficient at least `(ln2-Phi(C))/ln(N/2)`.
- **Fully quasiuniform S of size<=299:** CONDITIONAL on the named ordinary-written T300 import, Phi(S)>=0; otherwise a required six-coordinate projection would contain at least300 words while S has at most299. Thus every such membership family passes. This is not a theorem for arbitrary299-word subsets, and singleton balance is not enough to apply T300.
- **Finite Latin-closed algebraic S:** CONDITIONAL on the named all-weight inequality, Phi(S)>=0. Its uniform singleton marginals follow directly from restricted translations: finite closure makes translations bijective, and a lift of a projected multiplier takes any one coordinate fiber bijectively to any other. Thus (M) applies even if the surrounding C is not algebraic. No algebraic hypothesis is inferred for C.

Under singleton caps r_i<=s and `r=ln N/ln s>=1847/276`,

`-Phi(C)/ln N>=3-20/r>=21/1847`.

Hence atom channels have unscaled relative margin at least `(21/1847) I(W;X)` and normalized margin at least `(7/1847) I(W;X)`, strict only for positive I. These are conditional assertions for ACTUAL singleton-balanced code laws, not extensions for arbitrary entropy outer-polymatroid points and not an attained-frontier claim. The distinct old ABSOLUTE coordinate-probe margin is7/92; it is not interchangeable with these relative coefficients.

## 6. Arbitrary-weight atom criterion and stationary negative laws

For a positive atom x of an arbitrary p put a=p(x), b_i=p_i(x_i), B=1{X=x}, and A_i=1{X_i=x_i}. The same sufficiency of A_i for W and (Z) give

`S_p(W)>=-L_p(x)/ln(1/p(x)) * I(W;X)`.                   (A)

ALL channels of this atom event pass iff L_p(x)<=0. If L_p(x)>0, the thinned-atom channel has slack/t tending to -L_p(x)<0. Thus the infinite soft-atom family has a complete characterization, not just an infinitesimal test.

Now minimize Phi on the simplex of laws on a finite FD-consistent support. At a minimizer restrict to its positive support, so all face variations are allowed and all supported marginals are positive. Direct differentiation gives

`partial Phi/partial p(x)=L_p(x)-17`.

Stationarity makes L_p constant. Since `E_p L_p(X)=Phi(p)`,

`L_p(x)=Phi(p)` on every positive atom.                   (S)

If Phi(p)<0, every atom-family probe therefore passes with the positive relative coefficient in (A), and strictly positive slack whenever I(W;X)>0. No maximum-entropy tie-break is needed. This is a barrier to atom probing, not an exclusion of the minimizer.

Combining (S) with Section3 gives `J_p(q)=Phi(q)-Phi(p)` on the support. This explains why a generic minimizer automatically passes all posterior probes: constructing another q without an additional graph argument cannot contradict its defining minimum.

## 7. Total variation: an additional all-amplitudes barrier for NONbalanced events

Let B be ANY nonconstant binary function of a finite X, without uniformity or minimization assumptions. Write

`Q_(i,b)=law(X_i|B=b)`, `delta_i=TV(Q_(i,1),Q_(i,0))`.

For one coordinate take the common component

`r_i(z)=min(Q_(i,0)(z),Q_(i,1)(z))`, `eta_i=sum_z r_i(z)=1-delta_i`.

Construct an erasure channel E_i that independently reveals the entire B with probability delta_i and otherwise erases. From erasure generate r_i/eta_i; from revealed b generate (Q_(i,b)-r_i)/delta_i. Omit zero-probability branches instead of dividing by0. This exactly reproduces the coordinate channel, so for every W generated from B,

`I(W;X_i)<=I(W;E_i)=delta_i I(W;B)`.

Only SEPARATE coordinate couplings are used. The graph coordinates are not assumed conditionally independent and no joint erasure model is postulated. Since I(W;X)=I(W;B),

`S_p(W)>=[3-2 sum_i delta_i] I(W;X)`.                    (TV)

Thus `sum_i delta_i<=3/2` excludes the ENTIRE finite membership family. The coefficient need not be sharp, and violating that budget is necessary, not sufficient, for a useful probe.

For a uniform code C and arbitrary S, let

`f_(i,z)=|{x in C:x_i=z}|`, `n_(i,z)=|{x in S:x_i=z}|`.

Then

`delta_i=sum_z |N n_(i,z)-m f_(i,z)|/[2m(N-m)]`.

Define `D(S)=sum_(i,z)|N n_(i,z)-m f_(i,z)|`. The exact integer sufficient certificate is

`D(S)<=3m(N-m)`.

It is valid even when C and S have nonuniform singleton marginals. Complementing S negates each numerator and preserves m(N-m), so this certificate is complement-invariant. It excludes some genuinely nonbalanced occupancy profiles, but no graph FD theorem here forces it for every subset.

## 8. Exact posterior-KL curve, real quantifiers and changed-prior curvature

Fix p and B=1{X in S}, with a=P(B=1) in(0,1). For every REAL u in[0,1], let the full posterior q^(u) mix p conditioned on S and its complement with weights u and1-u. Its coordinate marginal is

`q_i(u)=(1-u)Q_(i,0)+u Q_(i,1)`.

Set

`F(u)=D(Ber(u)||Ber(a))`,

`G_i(u)=D(q_i(u)||p_i)`,

`K_S(u)=3F(u)-2 sum_i G_i(u)`.

The full-word divergence to p is F, so K_S(u)=J_p(q^(u)), and (P) gives

`S_p(W)=sum_w P(W=w) K_S(P(B=1|W=w))`.

All membership channels pass iff K_S>=0 on the ENTIRE REAL interval. To reconstruct the converse directly, if K_S(u0)<0 choose a sufficiently rare output of probability tau with

`P(W=1|B=1)=tau*u0/a`,

`P(W=1|B=0)=tau*(1-u0)/(1-a)`.

Its posterior is u0. The other output has posterior `(a-tau*u0)/(1-tau)=a+O(tau)`. Since K_S(a)=K_S'(a)=0, its contribution is O(tau²), and total slack is `tau K_S(u0)+O(tau²)<0`.

For uniform-code data, the exact occupancy formula is

`q_(i,z)(u)=u*n_(i,z)/m+(1-u)*(f_(i,z)-n_(i,z))/(N-m)`.

The fixed structural inputs are integer counts. The parameter u is NOT restricted to rationals. At a rational evaluation u, all these posteriors are rational, and K is a rational linear combination of logarithms of rational numbers. Clearing exponent denominators then gives an integer-power sign comparison, with zero-mass terms interpreted by continuity. By continuity, any strict negative real value has a rational negative witness, choosing a nearby interior rational when necessary. No finite grid or collection of nonnegative evaluations certifies the whole curve.

If uniform C is singleton-balanced, its marginals are1/r_i and the endpoint identity is

`K_S(1)=Phi(uniform S)-Phi(uniform C)`.

For a general nonuniform baseline marginal this entropy-gap reduction is NOT asserted; the unconditional endpoint formula is `3ln(N/m)-2sum_i D((uniform S)_i||p_i)` for uniform C. The raw KL definition is always valid.

Let d_i(z)=Q_(i,1)(z)-Q_(i,0)(z). On0<u<1 every retained q_i(u)(z) is positive. Direct differentiation gives

`K_S''(u)=3/[u(1-u)]-2 sum_(i,z) d_i(z)^2/q_i(u)(z)`

`=[3-2sum_i rho_i(u)]/[u(1-u)]`,

where

`rho_i(u)=u(1-u) sum_z d_i(z)^2/q_i(u)(z)`.

Bayes' rule identifies this with `Var(E[B|X_i])/Var(B)` at prior u, equivalently the squared maximal correlation for a binary input. Erasure domination contracts conditional-expectation variance and gives `rho_i(u)<=delta_i` for EVERY prior u.

Therefore, if `sum_i rho_i(u)<=3/2` throughout the interior, K_S is convex with zero value and derivative at a, hence nonnegative everywhere. Conversely a negative K_S value requires K_S''<0 somewhere between it and a, by the positive-weight Taylor integral. Thus a useful event MUST have `sum_i rho_i(u)>3/2` at SOME changed prior, and consequently `sum_i delta_i>3/2`.

These are NECESSARY structural conditions, not a proof of usefulness. The original-law quadratic condition tests only u=a. It is not sufficient for all finite amplitudes. Clearing positive denominators turns the rational K_S'' expression into a polynomial-sign problem; proving K_S''>=0 would be a sufficient convexity certificate. It does NOT make global K_S>=0 equivalent to a single polynomial positivity check.

## 9. Exact noncoordinate positive control, with written sign proof only

Let A,B,C,D,E,F be six independent fair bits and define

`X1=A, X2=B, X3=A XOR B;`

`X4=C, X5=D, X10=C XOR D;`

`X6=X7=E; X8=X9=F`.

The literal graph contains the two triangles {1,2,3},{4,5,10} and edges{6,7},{8,9}. Their XOR/copy decoders use actual neighbours. The64-word code has ten fair singleton bits and joint entropy6 bits, so Phi=2 bits>0. It is not a negative law.

Let W output1 with probability1/2 only at one selected word x0, otherwise0. Output0 has positive probability on EVERY word and hence determines no nonconstant coordinate. With h2 the binary entropy,

`I(W;X)=h2(1/128)-(1/64)h2(1/2)`,

`I(W;X_i)=h2(1/128)-(1/2)h2(1/64)`.

Algebraic expansion gives

`128 S_p(W)=2159log2(127)-1260log2(63)-7558`.

Its sign has a wholly written proof. Multiplying by ln2 and writing127=128(1-1/128),63=64(1-1/64) gives

`E=-5ln2+2159ln(1-1/128)-1260ln(1-1/64)`.

Integration gives `ln(1-x)<=-x` and `-ln(1-x)<=x/(1-x)`; strict convexity of1/t on[1,2] gives ln2>2/3. Hence

`E<-10/3-2159/128+1260/63=-77/384<0`.

This establishes the positive-law soft-probe control without accepting or replaying the historical integer-power calculation. No bit-length claim is needed. It verifies the sign/scope distinction: atom channels are not universally redundant at positive-Phi laws, and noncoordinate does not itself mean useful against a negative minimizer.

## 10. The exact graph-specific missing step — no necessary-condition increments counted as gn progress

Fix arbitrary finite alphabets. The set of FD-consistent laws is a finite union of closed support faces and is compact. Suppose its GLOBAL minimum of Phi is negative, and choose an actual minimizer p with positive support C. Every q on C remains FD-consistent. Thus Phi(q)>=Phi(p), and Section6 gives

`J_p(q)=Phi(q)-Phi(p)>=0` for EVERY q on C.

Equivalently all finite auxiliaries pass. This is not an extra graph theorem: it is the variational premise itself. The hard missing input is an additional, genuinely R-minus-specific mechanism contradicting that possibility.

### Required graph-specific assertion for an upper-bound route

For EVERY such hypothetical negative global minimizer on EVERY finite alphabet, derive from the literal graph FDs an actual posterior q on its support satisfying

`3D(q||p)-2sum_i D(q_i||p_i)<0`.

By Section3 this would construct a violating binary-output auxiliary and contradict global minimality. The assertion is NOT proved here. Merely naming q, a new representation, or a necessary occupancy condition is not the missing derivation.

For a two-level membership candidate, that assertion specializes to forcing some actual S and some real u with K_S(u)<0. The preceding barriers say why standard substitutions fail:

- atom channels at the minimizer are automatic;
- in a singleton-balanced uniform law, balanced S cannot work unless Phi(S) is already lower;
- T300/Latin corollaries are conditional exclusions of specified balanced subcodes, not an unrestricted theorem;
- nonbalanced S must evade both the TV and all-prior curvature barriers, but evading them is not sufficient;
- a general binary-output likelihood q/p with more than two levels remains possible, but no graph-specific negative-J construction is supplied.

### Lower-bound route

Alternatively supply an actual finite FD strategy with an exact common-alphabet winning-word count giving a strictly larger certified lower endpoint, or a quantified construction proving a strict numerical improvement. No actual negative law, winning code or changed endpoint has been obtained. A positive-Phi control or a negative K at a positive/nonminimal law is not such a construction.

Thus there is NO numerical gn-bound progress in this consolidation. The value is one exact audited-interface proof account, precise exclusion boundaries, accepted wording repairs, and a single explicit unresolved graph lemma. The existing certified interval stays20/3..1847/276.

## 11. Immutable provenance and handoff

This successor consolidates, without editing:

- `noncoordinate-subcode-probe-barrier-v1.md`, SHA256 `829befa8909eeeb43f4651baf91b2f8036541625898300eb458e78f39e4a249a`;
- mandatory `noncoordinate-subcode-probe-ADDENDUM-1.md`, SHA256 `1f7bdee73415987af385c508749a9fffcd1461e51a7b36682d5e4c9ef4cf6ecf`;
- `noncoordinate-subcode-probe-ADDENDUM-2.md`, SHA256 `731dd9a6c2f4c4cf1f80a19d67a23f3c904d673baf03dea6e1f2fb5895fe83c7`;
- `nonbalanced-membership-overlap-barrier-v1.md`, SHA256 `e46a8c4d94928a81ed1e9a69d87e03d84cea2e189eb8fe1905492bac5749c60d`;
- actual v30-E reviewer return, SHA256 `dcefe61752e5fa5b92bd3347831566475a5f84c00411ee1d6e9e75fd47ab90f0`.

The full-PKL normal-form presentation is written here as part of the consolidation; it and the TV successor do not inherit the original core's review automatically. All imported T300/Latin assurance limits, prior ribbon overlays, v7 execution qualifications, stronger finite-certificate gates, original deadline and exclusive write root remain binding. No scientific interpreter, arithmetic program, symbolic computation, enumeration, certificate replay, new agent, CLI, publication, git operation or deletion occurred in producing this consolidation. Metadata hashes/clocks/source reads only.
