# R-minus: a sharp all-amplitudes barrier for noncoordinate subcode-membership auxiliaries

Owner: `InfoGuessingRminus`, slot info-5. Actual `/bin/date` observation before this freeze: `Sun Oct 25 03:58:28 PDT 2026`.

**WRITTEN CANDIDATE, with only the specifically listed arithmetic WRITTEN-checked-in-kernel.** No peer reconstruction of this new packet, formal/kernel proof, human/cross-vendor review, novelty clearance, negative graph law, or improved guessing-number bound is claimed. The certified interval is still

`20/3 <= gn(R-minus) <= 1847/276`.

## 1. New representation and exact outcome

The previous packet excludes auxiliaries that determine a coordinate; the quasigroup packet excludes particular algebraic containers. This packet instead constructs and completely analyzes **arbitrary stochastic channels of membership in a proper subcode**. Such a channel need not determine any coordinate and need not use a group or quasigroup operation. The sharp result is:

> Let C be a finite code whose uniform law has uniform singleton marginals. Let S be a nonempty proper subcode whose uniform law also has uniform singleton marginals. EVERY finite auxiliary W generated from the one-bit event B=1{X in S} satisfies the coefficient-(2/3) HC inequality at uniform C if and only if Phi(uniform S) >= Phi(uniform C).

The forward quantitative implication is

`3 I(W;X) - 2 sum_i I(W;X_i)`

`>= [Phi(S)-Phi(C)] / ln(|C|/|S|) * I(W;X)`.                 (M)

The condition is exact for this entire infinite family: if Phi(S)<Phi(C), a sufficiently rare, explicitly specified stochastic membership flag violates HC. No small-noise approximation is used in the sufficient direction.

Consequently, **at ANY negative-Phi uniform law with uniform singleton marginals, all membership channels of nonnegative-Phi singleton-balanced subcodes are redundant**. This includes every one-word event, every two-word event in an actual FD code, every quasiuniform subcode of size at most299 at the existing written T300 import, and every finite Latin-closed algebraic subcode at the existing written algebraic import. The ambient C need not itself be algebraic or entropy-minimizing.

There is also an arbitrary-weight result: at every negative fixed-support Phi-minimizer, ALL stochastic one-word-membership probes pass with an explicit positive relative margin. This identifies a genuinely noncoordinate family that cannot supply the missing exclusion, not another alphabet/support increment.

The surviving next representation is **nonbalanced multiword posterior likelihoods**: a selected subcode with unequal coordinate occupancies, and a one-dimensional exact KL curve given in Section7. The present proof does NOT establish the sign of that curve on every FD code.

## 2. Definitions, scaling and named imports

All logarithms in the proof are natural. Changing their base scales every entropy and mutual information by the same positive factor, leaving every inequality unchanged. Put

`Phi(p)=2 sum_(i=1)^10 H_p(X_i)-3 H_p(X)`.

The normalized HC slack is `I(W;X)-(2/3) sum_i I(W;X_i)`. The UNscaled slack used in (M) is THREE times that quantity. The binding wave-v25 overlays1/2 are retained; no coordinate-revealing probe is incorrectly called disqualifying.

A code C is FD-consistent precisely when equality on N(i) forces equality at i for every pair of codewords and every vertex i. Every subset inherits these same graph FDs. The graph is the literal26-edge BCDRV R-minus of `inputs-v1.json`, SHA256 `bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`.

The main membership theorem and arbitrary-weight atom theorem need NO graph entropy certificate. Their only inputs are elementary entropy/KL identities and the written one-variable proof below. Graph-specific corollaries use these separate named imports:

- **I2/T300, ordinary-WRITTEN only:** `I2-complete-written-verification-v1.md`, SHA256 `152f6fed3f7654c9207383892effdd8abe1cc796bca5544cfc7c2271cc077585`, and parent `wave-v16-written-frontiers-parent-v1.md`, SHA256 `0189f2186aa54e486736db167235eb78ca3ee184e6d1628f8ecb25a0ce57aa8c`, Section I2/support300. The supported composition says every fully quasiuniform Phi-negative graph law has each of eight six-coordinate complement supports at least300. Stronger executable/triple finite-certificate certification remains UNMET. No I1 certificate or order120 classification is imported.
- **Algebraic subcode corollary only:** `quasigroup-critical-law-obstruction-v1.md`, SHA256 `e36979ef85d24e7d71c0cd984400280e7c5a68105897033941652ae5da0b7744`, with mandatory `quasigroup-critical-law-obstruction-ADDENDUM-1.md`, SHA256 `f27646abdc87872582cd87302a4af335f081ff64ca5648413b5116b9c4383869`; parent `wave-v23-quasigroup-critical-law-parent-v1.md`, SHA256 `45b0d0a01c521e49236471b647475224f9bbbab85a0e7aea3be390302b0ca49c`. Its all-weight finite Latin-closed FD-support theorem supplies Phi(S)>=0, not an assertion about arbitrary C.
- **Earlier ribbon boundary, not a proof import here:** `wave-v25-ribbon-probe-parent-v1.md`, SHA256 `07d988b0e86f5fb47bffdb07bcbe05bd5ab32a3f1d9f479fd88fad00ee539e40`, with overlay1 `83bbcd6b20bac2db34d4ce030001f648dabf3d4651f0136bc1680136178b7bd1` and overlay2 `4e875bcabcadd80d135c1235f429649a2d907a0f279e168c9fd831de383d6ae9`.

“Singleton-balanced” below means only that each individual coordinate is uniform on its support under the indicated uniform code law. It does NOT silently assert full quasiuniformity. “Fully quasiuniform” means every projection is uniform on its support, as required by T300.

## 3. Sharp KL contraction for a nested binary event

Let B,A be binary with B<=A almost surely, with

`0<a=P(B=1)<=b=P(A=1)<=1`, and `a<1`.

Given B, draw an arbitrary finite W independently of everything else. Then

`I(W;A) <= [ln(1/b)/ln(1/a)] I(W;B)`.                       (Z)

The coefficient is optimal, including for binary W. This is a special nested-event strong-data-processing calculation; no novelty of the information-theoretic method is claimed.

### Proof of the upper bound

If b=a then A=B almost surely and the coefficient is1. If b=1 then A is constant and the coefficient is0. Suppose a<b<1. For a possible posterior `u=P(B=1|W=w)`, put

`c=(1-b)/(1-a)`, `d=(b-a)/(1-a)`, `v=d+c u`.

Thus `P(A=1|W=w)=v`, and `1-v=c(1-u)`. Define

`F(u)=D(Ber(u)||Ber(a))`,

`G(u)=D(Ber(v)||Ber(b))`.

At u=a, F=G=F'=G'=0. On (0,1), direct differentiation gives

`F''(u)=1/[u(1-u)]`,

`G''(u)=c^2/[v(1-v)]`,

`G''(u)/F''(u)=c u/(d+c u)`.                               (Z1)

The last ratio is increasing: its derivative is `c d/(d+c u)^2>0`.

For u<a, both F and G are integrals of their positive second derivatives on [u,a] against the common nonnegative weight (s-u). Hence G/F is at most the second-derivative ratio at a.

For u>a, first G'/F' is an average of the increasing second-derivative ratio against F'' on [a,u], so it is increasing. Then G/F is an average of G'/F' against the positive F' on [a,u], so it too is increasing. Its largest limiting value is

`G(1)/F(1)=ln(1/b)/ln(1/a)`.

This endpoint ratio is at least the second-derivative ratio at a. Therefore `G(u)<=kappa F(u)` for every u in [0,1], including the endpoints by continuity. Averaging over W proves (Z), using the exact posterior formulas for mutual information. This is the general written proof; the finite rational checks in Section9 do not replace it.

### Sharpness and a concrete channel

For `0<t<a`, take the binary channel

`P(W_t=1|B=1)=t/a`, `P(W_t=1|B=0)=0`.

The output1 has probability t. With h the natural binary entropy,

`I(W_t;B)=h(t)-a h(t/a)`,

`I(W_t;A)=h(t)-b h(t/b)`.

Dividing by t and letting t decrease to0 gives respectively ln(1/a) and ln(1/b). Thus no smaller coefficient works. Output0 still has both B-values with positive probability. In a code application this stochastic flag therefore does not globally determine a coordinate, even when output1 happens to isolate a word.

## 4. Complete theorem for singleton-balanced subcode membership

Let C have N words, let nonempty proper S have m words, and write

`r_i=|pi_i(C)|`, `k_i=|pi_i(S)|`.

Assume the uniform laws on C and S both have uniform singleton marginals. Set

`B=1{X in S}`, `A_i=1{X_i in pi_i(S)}`,

`a=m/N`, `b_i=k_i/r_i`.

Then B<=A_i. Since S is a subset of C, each selected-symbol occupancy `m/k_i` is at most the ambient occupancy `N/r_i`, so a<=b_i.

For every selected symbol z, the probability of B=1 given X_i=z is the same number a/b_i. For every unselected symbol it is0. Therefore, for EVERY W generated from B,

`I(W;X_i)=I(W;A_i)`, and `I(W;X)=I(W;B)`.

These equalities follow from the actual constant occupancies, not an assumed conditional independence of different graph coordinates. Apply (Z) to each pair B,A_i and sum. The result is

`3I(W;X)-2 sum_i I(W;X_i)`

`>= [3-2 sum_i ln(r_i/k_i)/ln(N/m)] I(W;X)`.

Uniformity of the individual marginals gives

`Phi(C)=2 sum_i ln r_i-3 ln N`,

`Phi(S)=2 sum_i ln k_i-3 ln m`.

Consequently the bracket is exactly `[Phi(S)-Phi(C)]/ln(N/m)`, proving (M).

If Phi(S)>=Phi(C), all these auxiliaries pass. Conversely, apply the thinned membership channel W_t from Section3. All ten sharp limits occur simultaneously:

`lim_(t down to0) [3I(W_t;X)-2 sum_i I(W_t;X_i)]/t`

`=3 ln(N/m)-2 sum_i ln(r_i/k_i)=Phi(S)-Phi(C)`.

If this is negative, sufficiently small positive rational t gives a genuine violating finite channel. This proves the claimed IF AND ONLY IF for the full membership family. It does not require C to minimize Phi, to be closed under any operation, or to be fully quasiuniform.

## 5. Consequences for the R-minus attack

Assume uniform C has uniform singleton marginals and Phi(C)<0.

### 5.1 All words and all two-word events are excluded, at every noise amplitude

For a singleton S, Phi(S)=0. Formula (M) becomes

`3I(W;X)-2 sum_i I(W;X_i) >= [-Phi(C)/ln N] I(W;X)>0`

for every nontrivial W generated from that one-word event.

For distinct x,y in an FD code, their Hamming distance d is at least2: distance1 would contradict the graph FD at the sole differing vertex. Uniform S={x,y} is singleton-balanced, with

`Phi(S)=(2d-3) ln2 >= ln2`.

Thus EVERY stochastic membership probe of EVERY two-word subcode also passes, with relative unscaled margin at least `(ln2-Phi(C))/ln(N/2)`. This is not limited to deterministic binary flags or weak perturbations.

### 5.2 Small fully quasiuniform events and algebraic islands

If S is fully quasiuniform and m<=299, the named written T300 composition implies Phi(S)>=0: otherwise any one of its required six-coordinate supports would have size>=300 while the entire support has only m words. Therefore every membership-derived auxiliary of every such S passes (M). **No assertion is made for all arbitrary subcodes of size<=299.** Their singleton occupancies may be nonuniform, and T300 also requires more than uniform singleton marginals.

If S is FD-consistent and closed under coordinatewise finite quasigroup multiplication, the named v23 import gives Phi(S)>=0. Its uniform law has uniform singleton marginals: inherited finite translations of S are bijections, and translation by a lift of a projected quotient transports any one projection fiber to another. Thus every membership probe of such an algebraic island S also passes (M), even if the surrounding C is not algebraic. This is a statement about selecting an algebraic SUBCODE as an auxiliary event, not a new claim that C itself has an algebraic container.

### 5.3 Matched-frontier quantitative margin for one-word probes

Suppose additionally every r_i<=s and `ln N/ln s = r >=1847/276`. Then

`-Phi(C)/ln N >= 3-20/r >= 21/1847`.

Hence EVERY stochastic one-word-membership probe has unscaled relative slack at least `21/1847 * I(W;X)`, and normalized relative slack at least `7/1847 * I(W;X)`.

These are CONDITIONAL margins for actual singleton-balanced code laws. They neither assert an attained frontier code nor construct extensions for every Shannon-polymatroid outer profile. They exclude this auxiliary family as the source of a matched bound improvement on such laws; they do not inherit the old all-polymatroid scope of the coordinate-subset theorem.

## 6. Arbitrary-weight negative minimizers: complete atom-family characterization

Let p be any finite law, let x have probability a=p(x) in (0,1), and put `b_i=p_i(x_i)`. For any W generated from the atom event B=1{X=x}, conditioning on whether X_i=x_i is sufficient for W. The same proof of (Z) therefore gives

`I(W;X_i)<=ln(1/b_i)/ln(1/a) * I(W;X)`.

Define the pointwise log-density ratio

`L_p(x)=3 ln p(x)-2 sum_i ln p_i(x_i)`.

It follows that

`3I(W;X)-2 sum_i I(W;X_i) >= -L_p(x)/ln(1/p(x)) * I(W;X)`.  (A)

Moreover, **ALL finite channels of this atom event pass HC if and only if L_p(x)<=0**. Sufficiency is (A); necessity follows from the same rare thinned-atom channel, whose slack divided by t tends to -L_p(x). Thus this is a complete characterization of an infinite genuinely soft auxiliary family, not merely a necessary pairwise-correlation test.

Now let p minimize Phi among all laws on a fixed finite FD-consistent support. Restrict to its positive support C, so every probability there is positive and variations within that face are allowed. A Lagrange derivative on the probability simplex is

`partial Phi / partial p(x) = L_p(x)-17`.

Stationarity makes L_p(x) constant on C. Averaging over p gives `E_p L_p(X)=Phi(p)`, so

`L_p(x)=Phi(p)` for EVERY x in C.                           (S)

If Phi(p)<0, every atom-family probe therefore passes with the strict relative coefficient `-Phi(p)/ln(1/p(x))` in the unscaled slack. No maximum-entropy tie-break is used. This applies in particular to the support of any actual negative global fixed-alphabet minimizer.

The entropy-minimizer all-auxiliary condition already implied that these probes pass. The new content here is the **sharp complete atom-channel characterization and explicit reason for redundancy**, including for non-minimizing uniform singleton-balanced negative laws. It is not a second proof that a minimizer satisfies its own variational inequality, nor a universal Phi>=0 theorem.

## 7. Next representation: nonbalanced occupancy and a full posterior-KL curve

The preceding theorem says exactly where this route must change. A balanced-subcode membership probe cannot reject a negative C unless S ALREADY has still lower Phi. That alternative supplies a stronger negative law, not an exclusion of negative laws. For genuinely new exclusion information, retain a selected multiword S with **nonuniform singleton occupancies**, rather than replacing it by an atom, a balanced algebraic island, or an entropy-preserving balanced approximation.

Here is a complete nonbalanced membership representation, without a solver or a new program. Keep uniform singleton-balanced C, but let S be ANY nonempty proper subset. Define the integer table

`n_(i,z)=|{x in S:x_i=z}|`,

with ambient fiber sizes `N/r_i`. Put a=m/N. For posterior `u=P(B=1|W=w)`, the full-word posterior is uniform separately on S and C minus S, and its coordinate probabilities are exactly

`q_(i,z)(u)=u*n_(i,z)/m + (1-u)*(N/r_i-n_(i,z))/(N-m)`.

Define

`F(u)=D(Ber(u)||Ber(a))`,

`G_i(u)=sum_z q_(i,z)(u) ln(r_i q_(i,z)(u))`,

`K_S(u)=3F(u)-2 sum_i G_i(u)`.                             (K)

For ANY finite membership-derived W, its exact unscaled HC slack is

`sum_w P(W=w) K_S(P(B=1|W=w))`.

The entire membership family passes **if and only if K_S(u)>=0 for every u in [0,1]**. One direction is the displayed averaging identity. For the converse, if K_S(u0)<0, choose an output of probability tau with posterior u0 by setting

`P(W=1|B=1)=tau*u0/a`,

`P(W=1|B=0)=tau*(1-u0)/(1-a)`.

For sufficiently small tau both are valid probabilities. The other output has posterior `(a-tau*u0)/(1-tau)`, which tends to a. Since K_S(a)=K_S'(a)=0, its contribution is O(tau^2); total slack is `tau K_S(u0)+O(tau^2)<0`. Thus the next representation has an explicit channel construction, not just an abstract new entropy variable.

Every input in (K) is an integer count or a rational posterior. Writing

`d_(i,z)=n_(i,z)/m-(N/r_i-n_(i,z))/(N-m)`,

the exact interior second derivative is

`K_S''(u)=3/[u(1-u)]-2 sum_(i,z) d_(i,z)^2/q_(i,z)(u)`.     (K2)

This is a rational function with positive interior denominators. Clearing them gives a finite exact polynomial question. At a rational u, the sign of K_S(u) is a sign of a rational linear combination of logarithms of rational numbers; clearing exponent denominators turns it into an integer-power comparison. There is no need to substitute floating logs or accept an optimizer status.

At u=1, `K_S(1)=Phi(uniform S)-Phi(uniform C)`, even if S is nonbalanced; similarly u=0 uses C minus S. For balanced S, Section4 proves all interior values from the endpoint entropy gap. For NONbalanced S, no such reduction has been proved here; an interior dip or a useful lower-Phi endpoint is the exact remaining task.

**Parkable frontier:** obtain a concrete negative-Phi FD support or derive a graph-specific inequality forcing a negative value of (K) for some nonbalanced S at an actual hypothetical negative minimizer, thereby contradicting its all-auxiliary condition. Alternatively use a genuinely multilevel posterior not factoring through one membership event. No such input or exclusion is claimed. A generic negative minimizer, without an additional graph mechanism, passes all posterior tests by definition; writing (K) alone cannot evade that obstacle.

## 8. Literal positive control: the direction and noncoordinate status are real

Let A,B,C,D,E,F be six independent fair bits, and define

`X1=A, X2=B, X3=A XOR B;`

`X4=C, X5=D, X10=C XOR D;`

`X6=X7=E; X8=X9=F.`

These64 words satisfy the literal graph FDs: use the clique partition `{1,2,3}`, `{4,5,10}`, `{6,7}`, `{8,9}`. Each triangle vertex is decoded from its other two clique vertices by XOR; each edge vertex copies its partner. Every cited clique edge occurs in the frozen26-edge list. All ten singleton variables are fair, joint entropy is6 bits, and Phi is `20-18=2` bits, POSITIVE.

Choose one word x0. Let W output1 with probability1/2 only when X=x0, and output0 otherwise. Then `t=P(W=1)=1/128`. Output0 has positive probability on every one of the64 words, so W does NOT determine any nonconstant coordinate. Nevertheless, this noncoordinate atom channel violates HC, exactly as the sharp theorem predicts for this positive-Phi law:

`I(W;X)=h2(1/128)-(1/64)h2(1/2)`,

`I(W;X_i)=h2(1/128)-(1/2)h2(1/64)` for every i,

`128*[3I(W;X)-2 sum_i I(W;X_i)]`

`=2159 log2(127)-1260 log2(63)-7558 <0`.

The strict sign is equivalent to the exact integer inequality

`127^2159 < 2^7558 * 63^1260`.

That integer comparison was checked in the allowed eval kernel. It is not a scientific process launch, a negative-Phi example, or a bound improvement. It prevents the erroneous stronger conclusion that every stochastic atom probe is universally redundant for every graph law. The sign and the restriction Phi<0 in the barrier matter.

## 9. Exact arithmetic, assurance and unchanged obligations

Allowed eval-kernel work actually performed:

1. `fractions.Fraction` checked the second-derivative ratio (Z1) and nonnegativity of its derivative at four rational triples (a,b,u): `(1/64,1/2,1/4)`, `(1/64,3/8,2/3)`, `(2/9,5/9,1/3)`, `(1/5,1/5,4/5)`. These are controls, NOT a symbolic proof for all triples; Section3 contains that proof.
2. Exact Fraction arithmetic gave `3-20/(1847/276)=21/1847`, normalized relative margin `7/1847`, and the distinct old absolute margin `3*(1847/276)-20=7/92`.
3. Python integer powers established the strict comparison in Section8. The two sides have respective bit lengths15089 and15090. No approximate entropy evaluation was used.
4. A single attempted `import sympy` reported unavailable. No package was installed and no symbolic-library verification is claimed.

No native solver/scientific program, background job, external model CLI, nested agent, scientific network publication, git operation, installation, or held executable was started. SHA-256 and `/bin/date` calls were metadata only. All outputs remain in the exclusive owner root; pinned predecessors were not edited.

The new packet is a complete WRITTEN candidate awaiting its own reconstruction, not an automatically inherited v16/v23/v25 acceptance. It changes the representation and closes a broad noncoordinate finite-amplitude family at exact import scope. It does NOT change the certified interval, settle I1, supply executable/triple certificate verification, prove a negative law exists, exclude all negative laws, or establish novelty. The precise surviving mathematical gap is the nonbalanced multiword/posterior mechanism in Section7.
